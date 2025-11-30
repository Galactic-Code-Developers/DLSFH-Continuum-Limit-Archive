# DLSFH Continuum Limit Archive  
### Reference Simulations, Parameters, and Convergence Proof Artifacts  
### Supporting WP1 of the Unified Pre-Physical Framework  
Maintained by: The Kapodistrian Academy of Science  
Author: Antonios Valamontes  

---

## 📌 Purpose of This Repository

This repository provides the **archival simulation data**, **parameters**,  
**numerical operators**, and **convergence logs** necessary to reproduce  
the continuum-limit results for the Dodecahedron Linear String Field  
Hypothesis (DLSFH), as developed in:

**Appendix A — Discrete–to–Continuum Limits for the DLSFH Lattice**

This archive is meant to remain functional for:
- physicists,
- mathematicians,
- numerical analysts,
- historians of science,

even **100 years from now**, without requiring any explanations  
from the original author.

---

## 📁 Repository Structure

See the “Repository Tree” section in the top-level documentation.

---

## 🔬 What This Repository Contains

### 1. **Standardized Input Parameters**
Stored in `config/`:
- `lattice_parameters.yaml`: combinatorics, weights, scaling laws.
- `sgcv_parameters.yaml`: condensate amplitudes, potential coefficients.
- `mc_parameters.yaml`: coherence-length and kernel definitions.

---

### 2. **Reference Meshes (`data/reference_meshes/`)**
These encode the DLSFH geometries for:
- ε = 0.50  
- ε = 0.25  
- ε = 0.125  

Each file contains:
- vertex positions  
- adjacency lists  
- edge weights  
- symmetry metadata (A5)  

---

### 3. **Propagator Data (`data/propagators/`)**
Reference propagators:
- discrete: `G_epsilon_*.h5`
- continuum benchmark: `G_continuum_reference.h5`

Used for validating:
- Proposition A.2 (strong resolvent convergence)
- Corollary A.3 (propagator limit)

---

### 4. **Convergence Logs**
Stored exactly as produced by numerical experiments:
- Laplacian convergence  
- Resolvent convergence  
- Propagator convergence  

These logs prove:
- rate = O(ε¹) for Laplacian  
- resolvent convergence  
- path-sum convergence  

---

### 5. **SGCV / MC Sample Data**
Field samples used to compute:
- vacuum-induced curvature terms  
- coherence kernels with finite coherence length  

---

### 6. **Python Source Code (`src/`)**
Includes:
- DLSFH geometry generator  
- Discrete Laplacian  
- SGCV and MC field couplings  
- Continuum operator  
- Convergence tools  
- Propagator solvers  

---

### 7. **Jupyter Notebooks (`examples/`)**
Demonstrate:
- how to load meshes  
- how to compute discrete operators  
- how to compare discrete and continuum propagators  
- how SGCV & MC modify continuum operators  

---

### 8. **Unit Tests (`tests/`)**
Validating:
- Proposition A.1  
- Proposition A.2  
- Corollary A.3  
- SGCV / MC coupling convergence  

These tests guarantee mathematical reproducibility.

---

## 🔧 Reproducibility Requirements  
All code is:
- Python 3.10+
- Uses only open-source dependencies  
- Compatible with future interpreters  
- No GPU dependencies  

Full environment specification stored in:
