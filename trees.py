class Node:
    def __init__(self,name):
        self.name = name
        self.children = []

class BinaryNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        
def in_order_traversal(node):
    if node is not None:
        in_order_traversal(node.left)
        print node.value
        in_order_traversal(node.right)

def pre_order_traversal(node):
    if node is not None:
        print node.value
        in_order_traversal(node.left)
        in_order_traversal(node.right)

def post_order_traversal(node):
    if node is not None:
        in_order_traversal(node.left)
        in_order_traversal(node.right)
        print node.value

def reverse_binary_tree(node):
    if node is not None:
        temp = node.right
        node.right = node.left
        node.left = temp
        reverse_binary_tree(node.left)
        reverse_binary_tree(node.right)


class MaxHeap:
    """ A complete binary tree structure where each node is smaller than its children """
    def __init__(self, vals):
        sorted_vals = sorted_vals
        self.root = sorted_vals

# Create a tree
root = BinaryNode(5)

for val in [3,4,6,7]:
    node = BinaryNode(val)
    parent = root
    prev = None
    while parent is not None:
        if val < parent.value:
            if parent.left is not None:
                parent = parent.left
            else:
                parent.left = node
                break
        else:
            if parent.right is not None:
                parent = parent.right
            else:
                parent.right = node
                break



### Graphs ###

g = {
    0: [1,2],
    1: [0],
    2: [3],
    3: [4, 5],
    4: [],
    5: [0,3]
}

def dfs(graph, start, goal):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node == goal:
            return node
        neighbors = set(graph[node]) - visited
        stack.extend(neighbors)
        print "visited %d" % node
        visited.add(node)

def dfs_recursive(graph,start,goal,visited=None):
    
    if visited is None:
        visited = set()
    stack = set(graph[start]) - visited
    visited.add(start)
    for node in stack:
        if node == goal:
            return node, visited
        new_visited = visited.union({node})
        return dfs_recursive(graph,node,goal,new_visited)
        
    

def bfs(graph, start, goal):
    visited = set()
    queue = [(start, [])]
    while queue:
        node, path = queue.pop(0)
        if node == goal:
            return node, path
        neighbors = set(graph[node]) - visited
        new_path = path + [node]
        add_to_queue = [(neighbor, new_path) for neighbor in neighbors]
        queue.extend(add_to_queue)
        visited.add(node)

