import torch

class ADMMSolver:
    """
    Alternating Direction Method of Multipliers (ADMM) solver in PyTorch
    for Staged Advantage Estimation (SAE).

    Solves:
        min (1/2) * ||a - r0||_2^2
        s.t. 1^T a = 0
             ||a||_2^2 <= N
             L a + delta <= 0
    """
    def __init__(self, rho_y: float = 1.0, rho_z: float = 1.0, max_iter: int = 100, tol: float = 1e-6, device: str = 'cpu'):
        self.rho_y = rho_y
        self.rho_z = rho_z
        self.max_iter = max_iter
        self.tol = tol
        self.device = device

    def solve(self, r0: torch.Tensor, L: torch.Tensor, delta: torch.Tensor) -> torch.Tensor:
        """
        Args:
            r0: (N,) tensor, the unconstrained baseline advantages
            L: (M, N) tensor, the constraint matrix
            delta: (M,) tensor, the margins

        Returns:
            a: (N,) tensor, the constrained advantages
        """
        N = r0.shape[0]
        M = L.shape[0] if len(L.shape) > 1 else 0

        # Initialize primal and dual variables
        a = r0.clone().to(self.device)
        y = torch.zeros_like(a) # auxiliary for norm/mean constraints
        z = torch.zeros(M, device=self.device) if M > 0 else None # auxiliary for inequality constraints
        u = torch.zeros_like(a) # dual for a = y
        v = torch.zeros(M, device=self.device) if M > 0 else None # dual for La = z

        # Pre-factor the system matrix H
        I = torch.eye(N, device=self.device)
        if M > 0:
            H = (1 + self.rho_y) * I + self.rho_z * torch.matmul(L.T, L)
        else:
            H = (1 + self.rho_y) * I

        # Compute Cholesky factorization of H once for O(N^2) backsubstitution
        # H is symmetric positive definite
        L_chol = torch.linalg.cholesky(H)

        for iteration in range(self.max_iter):
            # 1. a-update
            # (I + rho_y * I + rho_z * L^T L) a = r0 + rho_y * (y - u) + rho_z * L^T (z - v)
            rhs = r0 + self.rho_y * (y - u)
            if M > 0:
                rhs += self.rho_z * torch.matmul(L.T, z - v)

            # Solve H a = rhs using Cholesky
            a_new = torch.cholesky_solve(rhs.unsqueeze(1), L_chol, upper=False).squeeze(1)

            # 2. y-update (Project onto mean=0 and ||y||^2 <= N)
            y_unc = a_new + u
            # Project onto 1^T y = 0
            y_mean_zero = y_unc - torch.mean(y_unc)
            # Project onto ||y||^2 <= N
            norm_sq = torch.sum(y_mean_zero ** 2)
            if norm_sq > N:
                y_new = y_mean_zero * torch.sqrt(N / norm_sq)
            else:
                y_new = y_mean_zero

            # 3. z-update (Project onto L a + delta <= 0, which means z <= -delta)
            if M > 0:
                z_unc = torch.matmul(L, a_new) + v
                z_new = torch.clamp(z_unc, max=-delta)

            # 4. Dual updates
            u = u + a_new - y_new
            if M > 0:
                v = v + torch.matmul(L, a_new) - z_new

            # 5. Convergence check
            primal_res_1 = torch.norm(a_new - y_new)
            primal_res_2 = torch.norm(torch.matmul(L, a_new) - z_new) if M > 0 else 0.0
            dual_res_1 = self.rho_y * torch.norm(y_new - y)
            dual_res_2 = self.rho_z * torch.norm(torch.matmul(L.T, z_new - z)) if M > 0 else 0.0

            if max(primal_res_1, primal_res_2, dual_res_1, dual_res_2) < self.tol:
                a = a_new
                break

            a = a_new
            y = y_new
            if M > 0:
                z = z_new

        return a
