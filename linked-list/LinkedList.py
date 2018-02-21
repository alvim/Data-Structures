class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

    def getKey(self):
        return self.key

    def setKey(self, key):
        self.key = key

    def getNext(self):
        return self.next

    def setNext(self, node):
        self.next = node

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def pushFront(self, key):
        n = Node(key)

        if not self.empty():
            n.setNext(self.head)

        self.head = n
        self.length += 1

    def topFront(self):
        return self.head.getKey()

    def popFront(self):
        self.head = self.head.next
        self.length -= 1

    def pushBack(self, key):
        n = Node(key)

        curr_node = self.head
        next_node = curr_node.next

        while curr_node.next != None:
            curr_node = curr_node.next

        curr_node.setNext(n)
        self.length += 1

    def topBack(self):
        curr_node = self.head

        while curr_node.next != None:
            curr_node = curr_node.next

        return curr_node.getKey()

    def popBack(self):
        prev_node = None
        curr_node = self.head

        while curr_node.next != None:
            prev_node = curr_node
            curr_node = curr_node.next

        prev_node.setNext(None)

    def find(self, key):
        curr_node = self.head

        while curr_node.next != None:
            if curr_node.getKey() == key:
                return True
            curr_node = curr_node.next

        return False

    def erase(self, key):
        prev_node = None
        curr_node = self.head

        while curr_node.next != None:
            if curr_node.getKey() == key:
                # Erase first
                if prev_node == None:
                    self.head = curr_node.next
                # Erase last
                elif curr_node.next == None:
                    prev_node.setNext(None)
                # Erase middle
                else:
                    prev_node.setNext(curr_node.next)

                self.length -= 1
                return True

            prev_node = curr_node
            curr_node = curr_node.next

        return False

    def empty(self):
        return self.length == 0

    def addBefore(self, node, key):
        prev_node = None
        curr_node = self.head

        while curr_node.next != None:
            if curr_node.getKey() == node:
                n = Node(key)
                n.setNext(curr_node)
                # Add not first
                if prev_node != None:
                    prev_node.setNext(n)
                else:
                    self.head = n

                return True

            curr_node = curr_node.next

        return False


l = LinkedList()
