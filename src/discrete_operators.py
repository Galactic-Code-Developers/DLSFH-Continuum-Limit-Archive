import numpy as np

def discrete_laplacian(mesh, field, eps):
    """
    Compute the DLSFH discrete Laplacian:
    Δ_ε φ(v) = (1/ε²) ∑_{u~v} c_uv (φ(u) - φ(v))
    """
    result = np.zeros_like(field)
    for v, neighbors in mesh["adjacency"].items():
        total = 0.0
        for (u, w) in neighbors:
            total += w * (field[u] - field[v])
        result[v] = total / (eps * eps)
    return result
