class Node:

    def __init__(self, value):
        self.value = value
        self.nextNode = None

    def __str__(self):
        if self.nextNode is not None:
            return str(self.value) + " " + str(self.nextNode)
        return str(self.value)

def linked_list(l):
    prev = None
    head = None
    for item in l:
        node = Node(item)
        if prev is not None:
            prev.nextNode = node
        else:
            head = node
        prev = node
    return head
    
def print_linked_list(node):
    if node is not None:
        print node.value
        print_linked_list(node.nextNode)

def append_to_end(head,node):
    tail = find_tail(head)
    tail.nextNode = node
    return head

def find_tail(head):
    current_node = head
    while current_node.nextNode is not None:
        current_node = current_node.nextNode
    return current_node

def partition(head, partition_value):
    """ Returns linked list such that all nodes less than the partition value are the left of others"""
    head_small = None
    head_large = None
    node = head

    while (node is not None):
        new_node = Node(node.value)
        if new_node.value < partition_value:
            if head_small is None:
                head_small = new_node
            else:
                append_to_end(head_small,new_node)
        else:
            if head_large is None:
                head_large = new_node
            else:
                append_to_end(head_large,new_node)
        node = node.nextNode

    tail_small = find_tail(head_small)
    if tail_small is not None:
        tail_small.nextNode = head_large
    return head_small
