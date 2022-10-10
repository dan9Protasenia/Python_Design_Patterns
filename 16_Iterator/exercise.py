"""Iterator pattern task

You are given a definition of Node class. Please implement preorder traversal directly in the Node class.

The returned sequence should be a sequence of values, not the nodes themselves."""


"""
# *Start template
class Node:
    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value

        self.parent = None

        if left:
            self.left.parent = self
        if right:
            self.right.parent = self

    def traverse_preorder(self):
        pass
        # ToDo - return inorder values (not Nodes)
"""


# ?Solution
class Node:
    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value

        self.parent = None

        if left:
            self.left.parent = self
        if right:
            self.right.parent = self

    def traverse_preorder(self):
        pass
        # ToDo - return inorder values (not Nodes)
