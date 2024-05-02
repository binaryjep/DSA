# Define the graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# List to keep track of visited nodes
visited = []

# Depth-First Search (DFS) function
def dfs(graph, start):
    # Print the currently visited node
    print(f"Visiting node: {start}")
    # Mark the node as visited by appending it to the 'visited' list
    visited.append(start)
    # Print the current state of visited nodes
    print(f"Current visited nodes: {visited}")
    
    # Iterate over the adjacent nodes of the current node
    for n in graph[start]:
        # If the adjacent node hasn't been visited yet
        if n not in visited:
            # Recursively call DFS on the adjacent node
            dfs(graph, n)
            # Print the backtracking step
            print(f"Backtracking to: {start}")

    # Print a message indicating there are no unvisited child nodes left for the current node
    print(f"No unvisited child nodes left for {start}\n")

# Start DFS from node 'A'
dfs(graph, 'A')
# Print the order of visited nodes using DFS
print(f"Order of visited nodes using DFS: {visited}")