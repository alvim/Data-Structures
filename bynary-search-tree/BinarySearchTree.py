class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    getValue(self):
        return self.value

    setValue(self, value):
        self.value = value

    getLeft(self):
        return self.left

    setLeft(self, node):
        self.left = node

    getRight(self):
        return self.right

    setRight(self, node):
        self.right = node


class BinarySearchTree:
    def __init__(self):
        self.root = None

    _getNext(self, node, curr_node):
        if node.getValue() < curr_node.getValue():
            return curr_node.getLeft()
        else:
            return curr_node.getRight()

    search(self, value):

    successor(self, value):

    show(self, value):

    insert(self, value):
        n = Node(value)
        curr_node = self.root

        if curr_node is None:
            return self.root = n

        next_node = self._getNext(n, curr_node)

        while next_node is not None:
            curr_node = next_node
            next_node = self._getNext(n, curr_node)
        
        if curr_node.getValue() > n.getValue():
            curr_node.setLeft(n)
        else:
            curr_node.setRight(n)

    remove(self, value):