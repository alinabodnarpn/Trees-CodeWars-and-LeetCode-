class Solution(object):
    def deleteNode(self, root, key):
        if not root:
            return None
        parent = None
        current = root

        while current and current.val != key:
            parent = current
            if key < current.val:
                current = current.left
            else:
                current = current.right
        if not current:
            return root
        if not current.left and not current.right:
            if not parent:
                return None
            if parent.left == current:
                parent.left = None
            else:
                parent.right = None
        elif not current.left or not current.right:
            child = current.left if current.left else current.right
            if not parent:
                return child
            if parent.left == current:
                parent.left = child
            else:
                parent.right = child
        else:
            next_larger_parent = current
            next_larger = current.right
            while next_larger.left:
                next_larger_parent = next_larger
                next_larger = next_larger.left
            current.val = next_larger.val

            if next_larger_parent.left == next_larger:
                next_larger_parent.left = next_larger.right
            else:
                next_larger_parent.right = next_larger.right
        return root
