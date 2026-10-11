from qiskit_optimization import QuadraticProgram
from qiskit_optimization.algorithms import MinimumEigenOptimizer
from qiskit_algorithms import QAOA
from qiskit_algorithms.optimizers import COBYLA
from qiskit.primitives import StatevectorSampler
from grid_map import SpaceGridMap

def solve_space_routing_with_qaoa():
    # 1. Use 3x3 grid (9 nodes) for fast, reliable quantum simulation
    space_map = SpaceGridMap(size=3, custom_debris=[4, 5])
    space_map.display_map_summary()
    
    qp = QuadraticProgram(name="Fast_Space_Route_Optimization")
    for i in range(space_map.num_nodes):
        qp.binary_var(name=f"x_{i}")
        
    linear_costs = {}
    for i in range(space_map.num_nodes):
        cost = space_map.base_fuel_cost
        if i in space_map.debris_nodes:
            cost += space_map.debris_penalty
        linear_costs[f"x_{i}"] = cost

    qp.minimize(linear=linear_costs)
    qp.linear_constraint(linear={f"x_{space_map.start_node}": 1.0}, sense="==", rhs=1.0, name="start_mandatory")
    qp.linear_constraint(linear={f"x_{space_map.end_node}": 1.0}, sense="==", rhs=1.0, name="end_mandatory")
    
    print("\n--- Running Hybrid Quantum-Classical QAOA Solver ---")
    
    # 2. Set up StatevectorSampler and optimizer with fewer iterations for speed
    sampler = StatevectorSampler()
    optimizer = COBYLA(maxiter=30)  # Keep it fast!
    
    # 3. Configure QAOA
    qaoa = QAOA(sampler=sampler, optimizer=optimizer, reps=1)
    
    # 4. Solve using Minimum Eigen Optimizer
    optimizer_algo = MinimumEigenOptimizer(qaoa)
    result = optimizer_algo.solve(qp)
    
    print("\n=== Quantum Optimization Results ===")
    print(f"Optimal Solution Vector (Bitstring): {result.x}")
    print(f"Total Objective Cost Value: {result.fval}")
    
    return result

if __name__ == "__main__":
    solve_space_routing_with_qaoa()