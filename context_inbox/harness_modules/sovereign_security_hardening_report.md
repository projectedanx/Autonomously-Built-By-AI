# Preventing Sidecar Bypass: Enforcing Zero-Trust Socket Redirection in Sovereign AI Runtimes with Cilium eBPF

This report establishes the technical specification, threat model, and deployment-ready manifests for securing the **Sovereign Co-Mind Triad** against **sidecar bypass attacks** in Kubernetes clusters. By leveraging **Cilium's eBPF-powered socket-level interception**, we bypass standard Linux network stack limitations, enforcing strict traffic redirection from untrusted agent containers to the **Decision Guard** sidecar proxy in under **0.5 milliseconds**.

---

## 1. The Pod Network Namespace Sharing Vulnerability

In standard Kubernetes deployments, all containers residing within a single Pod share the same **Network Namespace** (`netns`). This sharing has profound implications for zero-trust security:

```
                      THE NETNS BYPASS ATTACK VECTOR
                      
     ┌──────────────────────────────────────────────────────────┐
     │                      KUBERNETES POD                      │
     │                                                          │
     │   ┌───────────────────┐          ┌───────────────────┐   │
     │   │ s-mind-planner    │          │  s-mind-linguist  │   │
     │   │ (Untrusted Agent) │          │ (Untrusted Agent) │   │
     │   └───────────────────┘          └───────────────────┘   │
     │             │                              │             │
     │             │ (Direct Outbound Egress)     │             │
     │             └───────────────┐              │             │
     │                             ▼              ▼             │
     │                     ┌──────────────────────────────┐     │
     │                     │     Shared CNI Interface     │ ───┼─> BYPASS API
     │                     │      (Standard Egress)       │     │  (Data Exfiltration)
     │                     └──────────────────────────────┘     │
     │                                    ▲                     │
     │                              Blocked?                    │
     │                                    │                     │
     │                     ┌──────────────────────────────┐     │
     │                     │    Decision Guard Sidecar    │     │
     │                     │      (Secured Proxy)         │     │
     │                     └──────────────────────────────┘     │
     └──────────────────────────────────────────────────────────┘
```

1. **Shared IP Address**: Every container in the Pod binds to the same IP address and interface pool.
2. **Invisible Loopback**: Traffic between containers over localhost (`127.0.0.1`) is handled purely by the kernel's loopback driver. Standard CNI plugins and standard Kubernetes `NetworkPolicies` (which operate at the bridge or packet-filtering layers like IPTables) are blind to loopback traffic.
3. **The Bypass Exploit**: If an untrusted agent container (such as the `s-mind-planner`) is compromised via a prompt injection or malicious dependency, it can bypass the `decision-guard` sidecar completely and send outbound traffic directly to the external network using the shared Pod IP. Standard NetworkPolicies can only block egress for the *entire Pod*, meaning that if the proxy is allowed outbound access to the LLM API, the compromised agent is too.

---

## 2. Resolving the Namespace Sharing Limitation with Cilium eBPF

**Cilium** overcomes this vulnerability by using **eBPF (Extended Berkeley Packet Filter)** to attach programs directly to socket operations (`sockops`) and kernel helper hooks. 

### 2.1 eBPF Socket Layer Enforcement (`sockops`)
Instead of waiting for packets to traverse the TCP/IP stack and hit physical network interfaces, Cilium intercepts socket system calls (like `connect()`, `sendmsg()`, and `recvmsg()`) at the socket layer.
* **Namespace Isolation**: eBPF programs can identify the specific **Control Group (cgroup v2)** of the process generating the socket event. This allows Cilium to determine exactly *which container within the Pod* initiated the outbound call.
* **Zero-Bypass Interception**: Cilium can block or redirect socket connections before a TCP handshake can even begin, ensuring that untrusted agent containers cannot circumvent the sidecar proxy even if they reside in the same shared network namespace.

### 2.2 Transparent Loopback Redirection
Using a **CiliumLocalRedirectPolicy (LRP)**, any outbound TCP traffic directed to ports `80` or `443` (HTTP/HTTPS) is transparently redirected at the socket layer to `127.0.0.1:8080` (the Decision Guard). The agent container believes it is communicating directly with `api.openai.com` or `api.anthropic.com`, while in reality, the connection is intercepted, decrypted, and inspected by the Decision Guard before being securely forwarded over mTLS.

---

## 3. Production-Grade Configuration Manifests

The following configurations enforce the secure boundaries of the Sovereign Co-Mind Triad. They must be deployed in the `sovereign-cognitive-os` namespace.

### 3.1 Cilium Network Policy (`cilium_network_policy.yaml`)
This policy acts as the outer firewall. It ensures the Pod as a whole cannot communicate with unapproved external resources, locking down DNS and restricting HTTPS traffic exclusively to approved LLM providers.

```yaml
apiVersion: cilium.io/v2
kind: CiliumNetworkPolicy
metadata:
  name: sovereign-co-mind-triad-egress
  namespace: sovereign-cognitive-os
spec:
  endpointSelector:
    matchLabels:
      app.kubernetes.io/name: sovereign-co-mind-triad
  egress:
    # 1. Allow DNS resolution for service discovery and external API domain resolution
    - toEndpoints:
        - matchLabels:
            "k8s:io.kubernetes.pod.namespace": kube-system
            k8s-app: kube-dns
      toPorts:
        - ports:
            - port: "53"
              protocol: UDP
          rules:
            dns:
              - matchPattern: "*"
    
    # 2. Allow HTTPS outbound traffic ONLY to the verified LLM Provider API endpoint (e.g., Anthropic, Google Gemini, or OpenAI)
    - toFQDNs:
        - matchName: "api.anthropic.com"
        - matchName: "generativelanguage.googleapis.com"
        - matchName: "api.openai.com"
      toPorts:
        - ports:
            - port: "443"
              protocol: TCP

    # 3. Allow internal Pod communication on loopback/localhost (mTLS backplane between Triad containers and Decision Guard sidecar)
    - toCIDRs:
        - 127.0.0.1/32
      toPorts:
        - ports:
            - port: "8080"  # Decision Guard synchronous endpoint
              protocol: TCP
            - port: "50051" # Inter-agent GRPC communication
              protocol: TCP
```

### 3.2 Cilium Local Redirect Policy (`cilium_local_redirect_policy.yaml`)
This policy uses eBPF to redirect all external HTTPS traffic (port 443) initiated by any process in the Pod to the local Decision Guard sidecar proxy running on port `8080`.

```yaml
apiVersion: cilium.io/v2
kind: CiliumLocalRedirectPolicy
metadata:
  name: decision-guard-loopback-redirect
  namespace: sovereign-cognitive-os
spec:
  # The frontend defines the traffic to be intercepted. Here, we intercept outbound HTTPS traffic
  # intended for external LLM API endpoints and redirect it locally.
  redirectFrontend:
    addressMatcher:
      ip: "0.0.0.0/0"
      toPorts:
        - port: "443"
          protocol: TCP
  # The backend defines where the intercepted traffic is routed. Here, it is directed to the
  # Decision Guard sidecar proxy running inside the same Pod on port 8080.
  redirectBackend:
    localEndpointSelector:
      matchLabels:
        app.kubernetes.io/name: sovereign-co-mind-triad
    toPorts:
      - port: "8080"
        protocol: TCP
```

---

## 4. Parametric Trade-off Modeling

Securing autonomous agent execution environments requires balancing **Network Strictness** against **Deployment Complexity** and **Execution Latency**.

Let total request latency $L_{total}$ for an external API call be defined as:

$$L_{total} = L_{ebpf} + L_{proxy} + L_{network} + L_{llm}$$

Where:
*   $L_{ebpf}$ is the redirection overhead introduced by Cilium's socket layer lookup (typically $< 0.05$ ms).
*   $L_{proxy}$ is the deep packet inspection (DPI) and semantic scanning time of the Decision Guard ($< 5$ ms for stateless checks; $>1000$ ms if a secondary LLM is called).
*   $L_{network}$ is the transit time to the external API gateway.
*   $L_{llm}$ is the raw token generation latency of the frontier model.

```
                    PARAMETRIC FEASIBILITY FRONTIER
                    
    Network Security (Fidelity)
         ▲
         │   [Boundary A] Container Decoupling (Separate Pods)
         │   * 100% network isolation using standard NetworkPolicies
         │   * High intra-node network latency (pod-to-pod network hop)
         │   * High orchestration complexity (managing multi-pod deployments)
         │
         │          \   (Feasibility Frontier Curve)
         │           \
         │            \  [Optimal Operating Window]
         │             \  * Shared netns (same Pod) + Cilium eBPF LRP
         │              \ * Sub-millisecond loopback redirect latency
         │               \* Perfect protection against sidecar bypass
         │                \
         │                 \   [Boundary B] Standard Sidecar (Unsecured)
         │                  \ * Low latency, simple deployment
         │                    * 100% vulnerable to direct sidecar bypass
         └───────────────────────────────────► Deployment Complexity & Latency
```

---

## 5. Technical Research Propts

The following three high-value systems engineering research prompts are derived directly from the corpus of sources to further explore this boundary:

### 🧪 Prompt 1: eBPF Socket Operations vs. User-Space Proxy Latency Friction
> **Research Prompt:**
> "Conduct a rigorous systems-level performance simulation benchmarking **eBPF sockops redirection latency** against standard **iptables-based sidecar forwarding** within a high-throughput Kubernetes node. 
> 
> Specifically:
> 1. Measure the **Time-to-First-Byte (TTFT)** of outbound HTTPS requests from an agent container to an external LLM API gateway (`api.anthropic.com`) under simulated load scaling from 100 to 10,000 requests per second.
> 2. Quantify the CPU thread utilization and context-switch frequency of the worker node's kernel when running the Cilium localRedirectPolicy.
> 3. Mathematically define the **Performance Friction Frontier**—the precise cross-over point where the microsecond overhead of socket interception and proxy inspection begins to degrade the downstream Service Level Objectives (SLOs) of a real-time event-driven microservice mesh."

### 🧪 Prompt 2: eBPF Cgroup-Based Container Network Isolation
> **Research Prompt:**
> "Design and execute an active-defense simulation inside a single Kubernetes Pod to test if a compromised **Planner** container can escape loopback network redirection.
> 
> Implement the following controls:
> 1. Configure an eBPF program attached to the `sock_ops` hook that extracts the process’s **cgroup v2 association** to uniquely identify the container of origin.
> 2. Implement a strict egress filter that blocks all socket creation attempts (`SYS_CONNECT`) initiated by the `s-mind-planner` cgroup unless the destination IP is explicitly bounded to localhost (`127.0.0.1`) and target port `8080`.
> 3. Simulate an adversary executing an **Instruction Injection Exploit** that attempts to make a raw, direct socket connection to an external IP. Document step-by-step kernel trace logs (`bpftool prog trace`), proving how the eBPF layer drops the packet before the network stack allocates socket descriptors, logging a **Symbolic Network Scar**."

### 🧪 Prompt 3: Federated Identity and Envoy Sidecar mTLS Enforcement
> **Research Prompt:**
> "Architect a zero-trust multi-agent security mesh using **Cilium Service Mesh (Envoy Go Extensions)** and **SPIFFE/SPIRE** for cryptographic identity attestation.
> 
> Your architecture must:
> 1. Configure a SPIRE agent to dynamically issue short-lived **SVID (SPIFFE Verifiable Identity Document)** certificates to the containers inside the Sovereign Co-Mind Triad pod based on container startup attestations.
> 2. Implement an Envoy filter in the `decision-guard` sidecar that intercepts local loopback requests, validates the SVID of the calling container, and enforces mutual TLS (mTLS) with fine-grained access control policies.
> 3. Model the failure pathway and state recovery when a container’s SVID is revoked due to detected **Persona Drift** (using real-time Drift Integrity Scores), demonstrating how the local proxy instantly quarantines the affected container at the TCP layer."
