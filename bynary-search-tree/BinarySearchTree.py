class Node:
    def __init__(self, value):
        self.value = value
        self.left = null
        self.right = null
    
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
        self.root = null

    _getNext(self, node, curr_node):
        if node.getValue() < curr_node.getValue():
            return curr_node.getLeft()
        else:
            return curr_node.getRight()

    getRoot(self):
        return self.root

    search(self, value):

    successor(self, value):

    show(self, value):

    insert(self, value):
        n = Node(value)
        curr_node = self.root
        next_node = self._getNext(n, curr_node)

        while next_node:
            curr_node = next_node
            next_node = self._getNext(n, curr_node)
        
        # aqui next_node já é null
        # agora, esse next_node deve ser o n
        # como referenciar ele, sem repetir a
        # comparação já feita dentro de getNext()?
        # talvez se eu acessar next_node por referência...

    remove(self, value):