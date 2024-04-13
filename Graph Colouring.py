import networkx as nx
import matplotlib.pyplot as plt
import random

# Parameters
num_nodes = 50
radius = 0.125
colors = ['red', 'blue', 'green', 'yellow', 'purple']

# Generate a Random Geometric Graph
def generate_rgg(num_nodes, radius):
    return nx.random_geometric_graph(num_nodes, radius)

# Assign random colors to the nodes of the graph
def assign_colors(graph, colors):
    return {node: random.choice(colors) for node in graph.nodes()}

# Function to resolve conflicts and stop iterations if conflicts get to zero
def resolve_conflicts(graph, color_map, colors, iterations=100):
    conflict_counts = []
    for _ in range(iterations):
        conflicts = 0
        for node in graph.nodes():
            neighbors = graph.neighbors(node)
            if any(color_map[node] == color_map[neighbour] for neighbour in neighbors):
                conflicts += 1
                color_map[node] = random.choice([color for color in colors if color != color_map[node]])
        conflict_counts.append(conflicts)
        print(f'Iteration {_+1}: {conflicts} conflicts')
        if conflicts == 0:
            break
    return conflict_counts

# Main application
if __name__ == "__main__":
    # Generate graph
    G = generate_rgg(num_nodes, radius)
    
    # Assign different colors
    color_map = assign_colors(G, colors)
    
    # Resolve conflicts
    conflict_counts = resolve_conflicts(G, color_map, colors)
    
    # Plot the final graph
    pos = nx.get_node_attributes(G, 'pos')
    nx.draw(G, pos, node_color=[color_map[node] for node in G.nodes()], with_labels=True, node_size=50)
    plt.show()
    
    # Plot the conflicts over time and see if it gets an iteration where there are no conflicts
    plt.plot(conflict_counts)
    plt.xlabel('Iteration')
    plt.ylabel('Number of Conflicts')
    plt.title('Conflict Resolution Over Time')
    plt.show()