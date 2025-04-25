import json

class Node():
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BinarySearchTree():
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if value < current_node.value:
                    if current_node.left == None:
                        current_node.left = new_node
                        return self
                    else:
                        current_node = current_node.left
                else:
                    if current_node.right == None:
                        current_node.right = new_node
                        return self
                    else:
                        current_node = current_node.right

    def lookup(self, value):
        if self.root == None:
            return False
        else:
            current_node = self.root
            while current_node != None:
                if value > current_node.value:
                    current_node = current_node.right
                elif value < current_node.value:
                    current_node = current_node.left
                else:
                    return True
            else:
                return False
                
    def remove(self, value):
        if self.root == None:
            return None
        else:
            current_node = self.root
            parent_node = None
            while current_node:
                if value > current_node.value:
                    parent_node = current_node
                    current_node = current_node.right
                elif value < current_node.value:
                    parent_node = current_node
                    current_node = current_node.left
                else:       # everything starts here
                    if current_node.right == None:          # if no right node
                        if parent_node == None:
                            self.root = current_node.left
                        else:
                            if parent_node.left < current_node.left:
                                parent_node.left = current_node.left
                            else:
                                parent_node.right = current_node.left
                        return self
                    elif current_node.right.left == None:           # if no left node of right
                        if parent_node == None:
                            self.root = current_node.right
                        else:
                            current_node.right.left = current_node.left
                            if current_node.value < parent_node.value:
                                parent_node.left = current_node.right
                            elif current_node.value > parent_node.value:
                                parent_node.right = current_node.right
                        return self
                    
                    else:           # if both
                        leftmost = current_node.right.left
                        leftmost_parent = current_node.right
                        while leftmost != None:
                            leftmost_parent = leftmost
                            leftmost = leftmost.left

                        leftmost_parent.left = leftmost.right
                        leftmost.left = current_node.left
                        leftmost.right = current_node.right

                        if parent_node == None:
                            self.root = leftmost
                        else:
                            if current_node.value < parent_node.value:
                                parent_node.left = leftmost
                            elif current_node.value > parent_node.value:
                                parent_node.right = leftmost
            else:
                return True
                        
                    




def traverse(node):
    tree = {'value': node.value }
    tree['left'] = None if node.left is None else traverse(node.left)
    tree['right'] = None if node.right is None else traverse(node.right)
    return tree



bst = BinarySearchTree()
bst.insert(9)
bst.insert(17)
bst.insert(125)
bst.insert(1)
bst.insert(8)
bst.insert(12)
bst.remove(17)
print(bst.lookup(17))

print(json.dumps(traverse(bst.root)))