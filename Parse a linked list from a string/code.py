from preloaded import Node

def linked_list_from_string(list_repr: str) -> Node | None:
    if list_repr == "None":
        return None
    repr = list_repr.split(' -> ')[:-1]
    def build_node(rest):
        if not rest:
            return None
        return Node(int(rest[0]), build_node(rest[1:]))
    return build_node(repr)
