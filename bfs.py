# Initialize a list to keep track of visited nodes
visited = []

# Define a class for a Node in a binary tree
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

# Breadth-First Search function
def BFS(root):
    if root is None:
        return None
    else:
        # Initialize a queue with the root node
        queue = [root]

        # Loop until the queue is empty
        while len(queue) > 0:
            # Print the current state of the queue
            print("queue: ", [item.data for item in queue])

            # Mark the node at the front of the queue as visited and print it
            visited.append(queue[0].data)
            print("Pops: ", queue[0].data)
            print("visited: ", visited)

            # Remove the visited node from the queue
            node = queue.pop(0)
            print("new queue: ", [item.data for item in queue], "\n")

            # Add the left child of the visited node to the queue if it exists
            if node.left is not None:
                queue.append(node.left)

            # Add the right child of the visited node to the queue if it exists
            if node.right is not None:
                queue.append(node.right)


if __name__ == '__main__':
    # Create a binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.right.left = Node(8)
    root.left.right.right = Node(9)

    # Perform BFS on the binary tree
    BFS(root)