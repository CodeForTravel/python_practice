class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class TreeTraversal:
    def in_order_traversal(self, root):
        if root:
            # traversing left tree
            self.in_order_traversal(root.left)

            # printing root node
            print(str(root.val) + "->", end="")

            # traversing right tree
            self.in_order_traversal(root.right)

    def pre_order_traversal(self, root):
        if root:
            # printing root node
            print(str(root.val) + "->", end="")
            # traversing left tree
            self.pre_order_traversal(root.left)
            # traversing right tree
            self.pre_order_traversal(root.right)

    def post_order_traversal(self, root):
        if root:
            # traversing left tree
            self.post_order_traversal(root.left)
            # traversing right tree
            self.post_order_traversal(root.right)
            # printing root node
            print(str(root.val) + "->", end="")


root = Node(1)
root.left = Node(2)
root.right = Node(4)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.left = Node(9)
root.right.right = Node(10)


traverse = TreeTraversal()

print("In Order traversal")
traverse.in_order_traversal(root)

print("\nPre Order traversal")
traverse.pre_order_traversal(root)

print("\nPost Order traversal")
traverse.post_order_traversal(root)
