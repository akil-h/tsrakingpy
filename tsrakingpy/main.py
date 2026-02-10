import numpy as np

def _create_V_diag(c_v: np.ndarray, v: np.ndarray):
    diag_vector = np.multiply(c_v, v)
    return np.diag(diag_vector)

def _solve_gls_raking(x, G, g, V_e, V_epsilon):
    """
	-Form A = G V_e G' + V_eps
	-Solve A y = (g - Gx) = rhs
    Instead of using np.linalg.inv(A) for A^{-1}, 
    """
    A = G @ V_e @ G.T + V_epsilon

    try:
        y = np.linalg.solve(A, g-(G @ x))
    except np.linalg.LinAlgError:
        # We use Moore-Penrose generalized matrix inversion if not full rank
        y = np.linalg.pinv(A) @ (g-G.dot(x))
    
    theta_hat = x + (V_e @ G.T @ y)
    return theta_hat


def tsrake(x: np.ndarray,
        G: np.ndarray,
        g: np.ndarray,
        cx,
        cg):
        """
        This is a low-level solver for the raking adjustment. It takes in an unraked 
        vector of observations x, the design matrix G, the target vector g, and 
        adjustment coefficient vectors cx and cg. This public function returns the
        raked observations theta_hat.

        :param x: Vector of flattened matrix observations
        :param G: Design matrix which encodes the sums
        :param g: Vector of target totals
        :param cx: Scalar/Vector
        :param cg: Scalar/Vector
        """
        x = np.asarray(x, dtype=float).reshape(-1)  # flatten into 1D arrays
        g = np.asarray(g, dtype=float).reshape(-1)
        G = np.asarray(G, dtype=float)

        # Verify dimensions
        m, n = G.shape
        if x.size != n:
            raise ValueError(f"{x} has length {x.size}; must have length {n}")
        if g.size != m:
            raise ValueError(f"{g} has length {g.size}; must have length {m}")
        
        # Account for different dtypes for cx, cg
        if np.isscalar(cx):
            cx = np.full(n, fill_value=float(cx))
        else:
            cx = np.asarray(cx, dtype=float).reshape(-1)
            if cx.size != n:
                raise ValueError(f"{cx} has length {cx.size}; must be scalar or be an array of size {n}")
            
        if np.isscalar(cg):
            cg = np.full(m, fill_value=float(cg))
        else:
            cg = np.asarray(cg, dtype=float).reshape(-1)
            if cg.size != m:
                raise ValueError(f"{cg} has length {cg.size}; must be scalar or be an array of size {m}")

        # Create variance matrices
        V_e = _create_V_diag(cx, x)
        V_epsilon = _create_V_diag(cg, g)

        # Output raked vector
        theta_hat = _solve_gls_raking(x, G, g, V_e, V_epsilon)
        return theta_hat