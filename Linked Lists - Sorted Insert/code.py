""" For your information:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
"""

def sorted_insert(head, data):
    # Your code goes here.
    # Make sure to return the head of the list.
    if head is None or data <= head.data:
        new_node = Node(data)
        new_node.next = head
        return new_node

    head.next = sorted_insert(head.next, data)

    return head
