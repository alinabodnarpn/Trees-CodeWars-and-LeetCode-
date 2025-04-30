def tree_by_levels(node):
    if node is None:
        return []
    tree = []
    queue = [node]

    while queue:
        current_node = queue.pop(0)
        tree.append(current_node.value)
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

    return tree
