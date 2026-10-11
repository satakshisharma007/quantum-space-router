# 🌌 Quantum Space Routing: Fuel-Optimal Pathfinding & Debris Avoidance via QAOA

An innovative hybrid quantum-classical prototype built for the Qiskit Hackathon. This project solves space traffic management and orbital routing challenges by leveraging **Quantum Optimization concepts, Quadratic Unconstrained Binary Optimization (QUBO), and the Quantum Approximate Optimization Algorithm (QAOA)**.

## 👥 Team
* **Satakshi Sharma**
* **Sanika Purohit**
* **Aaryan Powale**

## 🚀 Problem Statement

Navigating spacecraft through congested orbital sectors requires finding optimal trajectories that minimize **fuel consumption** while avoiding high-risk **space debris hazard zones**. Traditional classical routing algorithms struggle with combinatorial explosion as grid sizes scale. This project demonstrates how variational quantum algorithms (QAOA) can be applied to handle complex spatial constraint optimization.

## 🛠️ Tech Stack & Libraries

- **Python 3.10+**
- **Qiskit** (Quantum SDK & Primitives)
- **Qiskit Optimization** (`QuadraticProgram`)
- **Qiskit Algorithms** (`QAOA`, `COBYLA`)
- **NumPy & Matplotlib** (Data processing & spatial visualization)

## 📁 Project Structure

- `grid_map.py`: Dynamic spatial grid creator defining start/end nodes and custom debris hazard penalties.
- `quantum_router.py`: Hybrid quantum-classical router translating constraints into QUBO and solving via Qiskit's QAOA.
- `visualizer.py`: Matplotlib plotting script rendering the space grid and hazard zones for analysis.

## ⚙️ How to Run

1. **Activate your virtual environment:**
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```
