class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    def _reverse(current, previous):
        if current is None:
            return previous
        nxt = current.next
        current.next = previous
        return _reverse(nxt, current)
    return _reverse(head, None)
