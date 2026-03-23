class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    # Your code goes here.
    # Remember to return the head of the list.
    if head is None or head.next is None:
        return head
    cur_node = head
    while cur_node.next is not None:
        if cur_node.next.data == cur_node.data:
            cur_node.next = cur_node.next.next
        else:
            cur_node = cur_node.next
    return head
