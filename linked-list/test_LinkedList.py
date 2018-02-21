from LinkedList import LinkedList

l = LinkedList()

class TestLinkedList():
    def test_init(self):
        assert hasattr(l, 'head')
        assert hasattr(l, 'length')
        assert hasattr(l, 'pushFront')
        assert hasattr(l, 'topFront')
        assert hasattr(l, 'popFront')
        assert hasattr(l, 'pushBack')
        assert hasattr(l, 'topBack')
        assert hasattr(l, 'popBack')
        assert hasattr(l, 'find')
        assert hasattr(l, 'erase')
        assert hasattr(l, 'empty')
        assert hasattr(l, 'addBefore')

    def test_empty(self):
        assert l.empty() == True
        l.pushFront(1)
        assert l.empty() == False

    def test_front_methods(self):
        assert l.topFront() != 10
        l.pushFront(10)
        assert l.topFront() == 10
        l.popFront()
        assert l.topFront() != 10

    def test_back_methods(self):
        assert l.topBack() != 20
        l.pushBack(20)
        assert l.topBack() == 20
        l.popBack()
        assert l.topBack() != 20

    def test_find_and_erase(self):
        assert l.find(15) == False
        l.pushFront(5)
        l.pushFront(15)
        l.pushFront(105)
        assert l.find(15) == True
        l.erase(15)
        assert l.find(15) == False

    def test_add_before(self):
        assert l.find(88) == False
        assert l.topFront() == 105
        l.addBefore(105, 88)
        assert l.find(88) == True
