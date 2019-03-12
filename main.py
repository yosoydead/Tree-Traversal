from bst import BST

tree = BST()
tree.insert(10)
tree.insert(6)
tree.insert(15)
tree.insert(3)
tree.insert(8)
tree.insert(20)

x = tree.BFS()
print(x)