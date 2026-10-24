import numpy as np

class SpaceGridMap:
    def __init__(self, size=3, custom_debris=None):
        self.size = size
        self.num_nodes = size * size
        
        # Define start (top-left) and end (bottom-right) coordinates
        self.start_node = 0  
        self.end_node = self.num_nodes - 1  
        
        # Allow custom debris zones, or default to some hazardous nodes
        if custom_debris is not None:
            self.debris_nodes = custom_debris
        else:
            # Default debris scattered across the grid for 3x3
            self.debris_nodes = [4, 5] if size == 3 else [6, 9, 10]
            
        self.debris_penalty = 100.0  # Massive hazard cost penalty
        self.base_fuel_cost = 2.0    # Normal movement fuel cost

    def get_node_coordinate(self, node_index):
        """Convert a flat node index to (row, col) coordinates."""
        row = node_index // self.size
        col = node_index % self.size
        return (row, col)

    def display_map_summary(self):
        print(f"=== {self.size}x{self.size} Dynamic Space Grid Map ===")
        print(f"Total Nodes: {self.num_nodes}")
        print(f"Start Node:  {self.start_node} {self.get_node_coordinate(self.start_node)}")
        print(f"End Node:    {self.end_node} {self.get_node_coordinate(self.end_node)}")
        print(f"Debris Zones: {self.debris_nodes}")
        print(f"Base Fuel Cost: {self.base_fuel_cost} | Debris Penalty: {self.debris_penalty}")

if __name__ == "__main__":
    # Test a 3x3 grid with custom debris at nodes 4 and 5 (matching your visualizer)
    custom_map = SpaceGridMap(size=3, custom_debris=[4, 5])
    custom_map.display_map_summary()