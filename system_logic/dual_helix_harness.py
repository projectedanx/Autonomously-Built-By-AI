from dual_helix_state import DualHelixState

try:
    from langgraph.graph import StateGraph, END
except ImportError:
    class StateGraph:
        def __init__(self, state_schema): self.nodes = {}; self.edges = []
        def add_node(self, name, func): self.nodes[name] = func
        def add_edge(self, src, dst): self.edges.append((src, dst))
        def add_conditional_edges(self, src, func, mapping): pass
        def set_entry_point(self, name): pass
    END = "__end__"

def node_think(state: DualHelixState): return state
def node_write(state: DualHelixState): return state
def node_code(state: DualHelixState): return state
def node_evaluate(state: DualHelixState): return state
def node_reforge(state: DualHelixState): return state
def route_eval(state: DualHelixState): return "CODE" if state.get("evaluation_status") == "fail" else "RE_FORGE"

def build_dual_helix_graph():
    graph = StateGraph(DualHelixState)
    graph.add_node("THINK", node_think)
    graph.add_node("WRITE", node_write)
    graph.add_node("CODE", node_code)
    graph.add_node("EVALUATE", node_evaluate)
    graph.add_node("RE_FORGE", node_reforge)
    graph.set_entry_point("THINK")
    graph.add_edge("THINK", "WRITE")
    graph.add_edge("WRITE", "CODE")
    graph.add_edge("CODE", "EVALUATE")
    graph.add_conditional_edges("EVALUATE", route_eval, {"CODE": "CODE", "RE_FORGE": "RE_FORGE"})
    graph.add_edge("RE_FORGE", END)
    return graph
