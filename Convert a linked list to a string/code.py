def stringify(node):
    if node is None:
        return 'None'
    output = str(node.data)
    output += ' -> '
    output += stringify(node.next)
    return output
