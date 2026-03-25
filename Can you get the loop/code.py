def loop_size(node):
    slow = node
    fast = node.next
    while slow != fast:
        slow = slow.next
        fast = fast.next.next
    fast = fast.next
    counter = 1
    while slow != fast:
        fast = fast.next
        counter += 1
    return counter
