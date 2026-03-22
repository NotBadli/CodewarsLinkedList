from preloaded import Node

# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
    
def get_nth(node, index):
    # Your code goes here.
    if node is None:
        raise ValueError
    if index == 0:
        return node
    if node.next is None:
        raise IndexError
    return get_nth(node.next, index - 1)
