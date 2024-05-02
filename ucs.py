import heapq

def uniform_cost_search(goal, start):
    global graph, cost

    # Initialize priority queue with starting node and its cost
    queue = []
    heapq.heappush(queue, (0, start, [start]))

    # Initialize dictionary to keep track of minimum cost to reach each node
    visited = {node: float('inf') for node in graph}
    visited[start] = 0

    # Loop until all reachable nodes are explored
    while queue:
        # Pop node with smallest cost so far from the priority queue
        cost_so_far, node, path = heapq.heappop(queue)

        # Check if goal node is reached
        if node in goal:
            return cost_so_far, path

        # Explore neighbors of the current node
        for neighbor, edge_cost in graph[node].items():
            # Calculate total cost to reach neighbor
            total_cost = cost_so_far + edge_cost

            # Update minimum cost to reach neighbor if a cheaper path is found
            if total_cost < visited[neighbor]:
                visited[neighbor] = total_cost
                # Add neighbor to the priority queue with its updated cost and path
                heapq.heappush(queue, (total_cost, neighbor, path + [neighbor]))

    # If goal node is not reached, return failure
    return -1, None

if __name__ == '__main__':
    # Define the weighted graph
    graph = {
        "S": {"F": 99, "R": 80},
        "F": {"B": 211},
        "R": {"P": 97},
        "P": {"B": 101},
        "B": {} 
    }

    # Specify the goal and start nodes
    goal = "B"
    start = "S"

    # Perform uniform cost search
    min_cost, path = uniform_cost_search(goal, start)
   
    # Print the minimum cost and path
    print("Minimum cost from " + start + " to " + goal + " is =", min_cost)
    print("Path:", ' -> '.join(path))