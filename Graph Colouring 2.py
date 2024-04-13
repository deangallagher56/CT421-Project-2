import networkx as nx
import matplotlib.pyplot as plt
import random
import statistics

# Parameters
num_nodes = 50
radii = [0.05 * i for i in range(1, 5)] 
colors = ['red', 'blue', 'green', 'yellow', 'purple']
iterations_limit = 100
runs_per_radius = 10

# Generate a Random Geometric Graph
def generate_rgg(num_nodes, radius):
    return nx.random_geometric_graph(num_nodes, radius)

# Assign random colors to nodes
def assign_colors(graph, colors):
    return {node: random.choice(colors) for node in graph.nodes()}

# Function for resolving conflicts
def resolve_conflicts(graph, color_map, colors):
    for iteration in range(iterations_limit):
        conflicts = 0
        for node in graph.nodes():
            neighbors = list(graph.neighbors(node))
            if any(color_map[node] == color_map[neighbour] for neighbour in neighbors):
                conflicts += 1
                # Exclude the current colour of the node and its neighbours
                available_colors = [color for color in colors if color not in [color_map[neighbour] for neighbour in neighbors]]
                color_map[node] = random.choice(available_colors) if available_colors else color_map[node]
        if conflicts == 0:
            return iteration + 1
    return iteration + 1  # Return the limit if no solution is found

# Main
avg_iterations_per_radius = []
for radius in radii:
    iterations_for_radius = []
    for _ in range(runs_per_radius):
        G = generate_rgg(num_nodes, radius)
        color_map = assign_colors(G, colors)
        iterations = resolve_conflicts(G, color_map, colors)
        iterations_for_radius.append(iterations)
    avg_iterations = statistics.mean(iterations_for_radius)
    avg_iterations_per_radius.append(avg_iterations)
    print(f"Radius: {radius}, Average Iterations: {avg_iterations}")

# Plot results
plt.plot(radii, avg_iterations_per_radius, marker='o')
plt.xlabel('Radius')
plt.ylabel('Average Number of Iterations')
plt.title('Effect of Graph Density on Graph Colouring Algorithm Performance')
plt.grid(True)
plt.show()