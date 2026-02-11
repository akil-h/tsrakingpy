# TSRaking

**TSRaking** is a Python library for generalized time series raking (benchmarking) and constrained adjustment of multi-dimensional data.

It implements a Generalized Least Squares (GLS) raking procedure that reconciles:

- High-frequency predictions (e.g., monthly estimates)
- Low-frequency totals (e.g., annual constraints)
- Cross-sectional constraints (e.g., provincial totals summing to national totals)

TSRaking is designed for statistical agencies, researchers, and practitioners who need to enforce accounting identities or hierarchical consistency in time series data.

---

## Features

- Generalized least squares raking
- Lightweight (NumPy-based)
- Suitable for hierarchical time series benchmarking and frequency table rebalancing

The raking adjustment is computed via:

$$\hat{\theta}
= x + V_e G^\top (G V_e G^\top + V_\varepsilon)^{-1} (g - Gx)$$

If the constraint system is rank-deficient, then Moore–Penrose matrix inversion is used to obtain a unique solution.

---

## System Requirements

### Software Requirements

- Python ≥ 3.8
- NumPy

Optional (for development):
- pytest

### Operating Systems

The development version of TSRaking has been tested on:

- Linux (Ubuntu 20.04+)
- macOS
- Windows 10/11

The package is pure Python and should run on any operating system that supports Python 3.8+.

---

## Installation

### Install from PyPI

Create a virtual environment (recommended):

```bash
python -m venv tsraking-env
source tsraking-env/bin/activate  # macOS/Linux
# or
tsraking-env\Scripts\activate     # Windows

```

For developers or users who want the latest features from the main branch:

```bash
git clone https://github.com/akil-h/tsrakingpy.git
cd tsrakingpy

python -m venv tsraking-env
source tsraking-env/bin/activate  # macOS/Linux
# or
tsraking-env\Scripts\activate     # Windows

pip install -e .
```

## License

License

This project is licensed under the MIT License.