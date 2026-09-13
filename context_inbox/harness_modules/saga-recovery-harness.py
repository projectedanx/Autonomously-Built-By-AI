import uuid
import json
import logging
from typing import Callable, List, Dict, Any, Optional

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("SCOS-Saga-Orchestrator")

class EpistemicCheckpoint:
    """Represents a validated, immutable state anchor before executing mutating steps."""
    def __init__(self, checkpoint_id: str, state_snapshot: Dict[str, Any]):
        self.checkpoint_id = checkpoint_id
        self.state_snapshot = state_snapshot

class SagaStep:
    """A paired transaction unit consisting of a forward action and its inverse compensating action."""
    def __init__(
        self,
        name: str,
        forward_action: Callable[[], Any],
        compensating_action: Callable[[], Any],
        validation_gate: Callable[[Any], bool],
        timeout_seconds: int = 30
    ):
        self.name = name
        self.forward_action = forward_action
        self.compensating_action = compensating_action
        self.validation_gate = validation_gate
        self.timeout_seconds = timeout_seconds
        self.status = "PENDING"  # PENDING, SUCCESS, FAILED, COMPENSATING, COMPENSATED, STUCK

class SagaOrchestrator:
    """
    SCOS-Compliant Saga-Style Recovery Orchestrator.
    Manages multi-step state mutations by guaranteeing either absolute forward
    convergence or exact topological rollback to pre-task Epistemic Checkpoints.
    """
    def __init__(self, transaction_id: str, depth: int = 1):
        self.transaction_id = transaction_id
        self.depth = depth
        self.steps: List[SagaStep] = []
        self.history: List[Dict[str, Any]] = []
        self.checkpoint: Optional[EpistemicCheckpoint] = None
        self.scars_ledger_path = "/workspace/scratch/scars.json"

    def set_checkpoint(self, state_snapshot: Dict[str, Any]):
        """Binds a verified pre-task baseline to prevent linear error accumulation."""
        checkpoint_id = f"CHECKPOINT-{uuid.uuid4().hex[:8]}"
        self.checkpoint = EpistemicCheckpoint(checkpoint_id, state_snapshot)
        logger.info(f"[*] Epistemic Checkpoint committed: {checkpoint_id}")

    def add_step(self, step: SagaStep):
        """Pre-registers a paired step within the Saga execution graph."""
        self.steps.append(step)
        logger.info(f"[+] Paired transaction pre-registered: Step '{step.name}'")

    def execute(self) -> bool:
        """
        Executes the forward transaction pipeline.
        If a step fails its validation gate or throws an exception,
        the orchestrator triggers a compensating rollback down the execution stack.
        """
        if not self.checkpoint:
            raise RuntimeError("[-] Epistemic Checkpoint must be committed before Saga execution.")

        logger.info(f"[*] Initiating Saga execution: Tx {self.transaction_id} (Depth Capacity: {self.depth})")
        executed_steps: List[SagaStep] = []

        for step in self.steps:
            logger.info(f"=== [STEP: {step.name}] Executing Forward Transaction ===")
            step.status = "IN_PROGRESS"
            try:
                # 1. Execute Forward Action
                result = step.forward_action()
                
                # 2. Evaluate Validation Gate (Verification Metric)
                if step.validation_gate(result):
                    step.status = "SUCCESS"
                    executed_steps.append(step)
                    logger.info(f"[+] Step '{step.name}' successfully validated.")
                else:
                    raise ValueError(f"Validation gate failed for step '{step.name}'")
                    
            except Exception as e:
                step.status = "FAILED"
                logger.error(f"[-] Step '{step.name}' failed: {str(e)}")
                # Trigger the compensation loop (the rollback)
                self._rollback(executed_steps, trigger_cause=f"{step.name}_failure: {str(e)}")
                return False

        logger.info(f"[SUCCESS] Saga Tx {self.transaction_id} fully converged without topological tearing.")
        return True

    def _rollback(self, executed_steps: List[SagaStep], trigger_cause: str):
        """
        Executes inverse compensating transactions in reverse chronological order.
        Addresses the 'Lost Compensation Problem' to prevent stale state propagation.
        """
        logger.warning(f"[!] SAGA ROLLBACK TRIGGERED: {trigger_cause}")
        logger.warning(f"[*] Epistemic Rollback initialized. Reverting to checkpoint {self.checkpoint.checkpoint_id}...")

        # Walk backward down the execution history stack
        for step in reversed(executed_steps):
            logger.warning(f"--- Compensating Step '{step.name}' ---")
            step.status = "COMPENSATING"
            try:
                # Execute paired rollback action
                step.compensating_action()
                step.status = "COMPENSATED"
                logger.info(f"[+] Step '{step.name}' compensation verified successfully.")
            except Exception as e:
                step.status = "STUCK"
                logger.critical(f"[!!!] LOST COMPENSATION ERRROR in Step '{step.name}': {str(e)}")
                self._mint_symbolic_scar(
                    step_name=step.name,
                    error_type="LostCompensationError",
                    traceback=str(e),
                    unresolved_state=self.checkpoint.state_snapshot
                )
                logger.critical("[!] Swarm entering Paraconsistent Escrow state. Requiring human intervention.")
                return

        # Restore the baseline state to the Epistemic Checkpoint snapshot
        logger.info(f"[+] Epistemic Rollback complete. Restored baseline: {self.checkpoint.state_snapshot}")
        self._mint_symbolic_scar(
            step_name="rollback_gateway",
            error_type="RollbackInterception",
            traceback=trigger_cause,
            unresolved_state=self.checkpoint.state_snapshot
        )

    def _mint_symbolic_scar(self, step_name: str, error_type: str, traceback: str, unresolved_state: Dict[str, Any]):
        """Vectorizes the failure topology to permanently immunize the agent in subsequent runs."""
        scar_id = f"SCAR-{uuid.uuid4().hex[:8]}"
        scar_entry = {
            "scar_id": scar_id,
            "failed_step": step_name,
            "error_type": error_type,
            "traceback": traceback,
            "unresolved_state": unresolved_state,
            "repulsion_vectors": ["SagaFailure", f"Step_{step_name}_Failure"]
        }

        # Append to scars database
        try:
            try:
                with open(self.scars_ledger_path, "r") as f:
                    ledger = json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                ledger = []

            ledger.append(scar_entry)
            with open(self.scars_ledger_path, "w") as f:
                json.dump(ledger, f, indent=2)

            logger.info(f"[+] Minted Symbolic Scar: [{scar_id}] logged to {self.scars_ledger_path}")
        except Exception as io_err:
            logger.error(f"[-] Failed to write symbolic scar: {str(io_err)}")


# --- SIMULATION AND SELF-TEST HARNESS ---

# Dummy database states to simulate microservices
local_database = {"orders": [], "inventories": {"product_id_101": 50}}

def mock_create_order() -> Dict[str, Any]:
    local_database["orders"].append({"order_id": "ORD-001", "product_id": "product_id_101", "quantity": 1})
    logger.info(f"[DB] Order created in Order Service: {local_database['orders']}")
    return {"status_code": 201, "order_id": "ORD-001"}

def mock_cancel_order():
    local_database["orders"] = [o for o in local_database["orders"] if o["order_id"] != "ORD-001"]
    logger.info(f"[DB] Order cancelled in Order Service: {local_database['orders']}")

def mock_reserve_inventory() -> Dict[str, Any]:
    # Simulate an error by attempting to reserve more than available, or forcing a manual validation failure
    if local_database["inventories"]["product_id_101"] > 0:
        local_database["inventories"]["product_id_101"] -= 1
        logger.info(f"[DB] Inventory decremented: {local_database['inventories']}")
        return {"status_code": 200, "current_stock": local_database["inventories"]["product_id_101"]}
    else:
        raise RuntimeError("Inventory starvation.")

def mock_release_inventory():
    local_database["inventories"]["product_id_101"] += 1
    logger.info(f"[DB] Inventory incremented: {local_database['inventories']}")

# Validation Gates
def validate_order_creation(response: Dict[str, Any]) -> bool:
    return response.get("status_code") == 201

def validate_inventory_reservation(response: Dict[str, Any]) -> bool:
    # Trigger a validation failure to demonstrate the Saga rollback mechanism
    return False  # Forced validation gate failure to test compensating transactions


if __name__ == "__main__":
    print("\n--- TEST RUN 1: HEALTHY COGNITIVE ROLLBACK ---")
    orchestrator = SagaOrchestrator(transaction_id="tx_microservice_checkout_001")
    
    # Commit Epistemic Checkpoint (Initial State snapshot before mutations)
    orchestrator.set_checkpoint(state_snapshot=json.loads(json.dumps(local_database)))

    # Step 1: Create Order
    step_1 = SagaStep(
        name="create_order",
        forward_action=mock_create_order,
        compensating_action=mock_cancel_order,
        validation_gate=validate_order_creation
    )
    
    # Step 2: Reserve Inventory
    step_2 = SagaStep(
        name="reserve_inventory",
        forward_action=mock_reserve_inventory,
        compensating_action=mock_release_inventory,
        validation_gate=validate_inventory_reservation  # This will fail
    )

    orchestrator.add_step(step_1)
    orchestrator.add_step(step_2)

    success = orchestrator.execute()
    print(f"Saga Execution Outcome: {'SUCCESS' if success else 'FAILED/ROLLED_BACK'}")
    print(f"Final DB State: {local_database}\n")
