#printing leaf nodes
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Binary_tree:
    def create_node(self,data):
        return Node(data)
    def insert(self,node,data):
        if node is None:
            return self.create_node(data)
        if data<node.data:
            node.left=self.insert(node.left,data)
        else:
            node.right=self.insert(node.right,data)
        return node
    def evenodddiff(self,root):
        if root is None:#empty//no root node
            return 0
        if (root.data)%2==0:
            return self.evenodddiff(root.left)+self.evenodddiff(root.right)+root.data
        return self.evenodddiff(root.left)+self.evenodddiff(root.right)-root.data
            
        
            
        
tree=Binary_tree()
root=tree.create_node(10)
#print("root node:",root.data)
tree.insert(root,20)
tree.insert(root,5)
tree.insert(root,2)
tree.insert(root,40)
tree.insert(root,12)
print(abs(tree.evenodddiff(root)))



