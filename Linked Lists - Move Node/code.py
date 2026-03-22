class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
    
def move_node(source, dest):
    if source is None:
        raise ValueError
    if dest:
        prev_dest = dest
        dest = Node(source.data)
        dest.next = prev_dest
    else:
        dest = Node(source.data)
    source = source.next
    return Context(source, dest)
