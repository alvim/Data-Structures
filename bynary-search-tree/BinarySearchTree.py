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
