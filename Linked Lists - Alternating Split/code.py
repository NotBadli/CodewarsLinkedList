class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    if not head or not head.next:
        raise ValueError
    first_head = head
    second_head = head.next
    current1 = first_head
    current2 = second_head
    while current1 and current2:
        current1.next = current2.next
        current1 = current1.next
        if current1:
            current2.next = current1.next
            current2 = current2.next
    return Context(first_head, second_head)
