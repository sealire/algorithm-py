from struct.node import TreeNode


class Bst:
    def __init__(self):
        self.size = 0
        self.root = None

    def insert(self, value):
        if value:
            self.size = self.size + 1
            if self.root is None:
                self.root = TreeNode(value)
            else:
                self.inserttree(self.root, value)

    def inserttree(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self.inserttree(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self.inserttree(node.right, value)

    def leftprint(self):
        if self.root:
            self.leftprinttree(self.root)

    def leftprinttree(self, node):
        print(node.value)
        if node.left:
            self.leftprinttree(node.left)
        if node.right:
            self.leftprinttree(node.right)

    def middleprint(self):
        if self.root:
            self.middleprinttree(self.root)

    def middleprinttree(self, node):
        if node.left:
            self.middleprinttree(node.left)
        print(node.value)
        if node.right:
            self.middleprinttree(node.right)

    def rightprint(self):
        if self.root:
            self.rightprinttree(self.root)

    def rightprinttree(self, node):
        if node.left:
            self.rightprinttree(node.left)
        if node.right:
            self.rightprinttree(node.right)
        print(node.value)


bst = Bst()
# bst.root = TreeNode("100")
bst.insert(100)
bst.insert(101)
bst.insert(107)
bst.insert(102)
bst.insert(82)


bst.middleprint()
bst.leftprint()
bst.rightprint()
