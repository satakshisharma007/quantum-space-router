import matplotlib.pyplot as plt
import numpy as np
from grid_map import SpaceGridMap

def plot_space_route(grid_size=3, debris_nodes=[4, 5]):
    space_map = SpaceGridMap(size=grid_size, custom_debris=debris_nodes)
    
    # Create a grid representation for plotting
    fig, ax = plt.subplots(figsize=(6, 6))
    
    # Plot nodes
    for i in range(space_map.num_nodes):
        r, c = space_map.get_node_coordinate(i)
        
        # Color code based on node type
        if i == space_map.start_node:
            color = 'limegreen'
            label = 'Start'
        elif i == space_map.end_node:
            color = 'dodgerblue'
            label = 'Destination'
        elif i in space_map.debris_nodes:
            color = 'crimson'
            label = 'Debris Hazard' if i == space_map.debris_nodes[0] else ""
        else:
            color = 'lightgray'
            label = 'Clear Space' if i == 1 else ""
            
        ax.scatter(c, -r, s=800, c=color, edgecolors='black', linewidths=1.5, zorder=3)
        ax.text(c, -r, f"Node {i}\n({r},{c})", ha='center', va='center', fontsize=9, fontweight='bold', zorder=4)

    ax.set_xlim(-0.5, grid_size - 0.5)
    ax.set_ylim(-(grid_size - 0.5), 0.5)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.grid(True, linestyle='--', alpha=0.5)
    
    plt.title(f"Quantum Space Routing Prototype ({grid_size}x{grid_size} Grid)\nDebris Avoidance via QAOA", fontsize=12, fontweight='bold', pad=15)
    plt.xlabel("Grid Column", fontsize=10)
    plt.ylabel("Grid Row", fontsize=10)
    
    print("--- Opening Visual Map Window ---")
    plt.show()

if __name__ == "__main__":
    plot_space_route(grid_size=3, debris_nodes=[4, 5])