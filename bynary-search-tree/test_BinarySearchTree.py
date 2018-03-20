from BinarySearchTree import BinarySearchTree

t = BinarySearchTree()

class TestBinarySearchTree():
    def test_init(self):
        assert hasattr(t, 'root')
        assert hasattr(t, 'getRoot')
        # assert hasattr(t, 'getSuccessor')
        assert hasattr(t, 'search')
        assert hasattr(t, 'show')
        assert hasattr(t, 'insert')
        assert hasattr(t, 'remove')
    
    def test_insert_root(self):
        assert l.getRoot() == null
        l.insert(50)
        assert l.getRoot.getValue() == 50

    def test_search(self):
        node = l.search(40)
        assert node = False
        node = l.search(50)
        assert node != False
        assert node.getValue() = 50

    def test_not_insert(self):
        assert l.insert(50) == False
    
    def test_inserts(self):
        assert l.search(10) == False
        assert l.search(52) == False
        assert l.search(58) == False
        assert l.search(15) == False
        l.insert(10)
        l.insert(52)
        l.insert(58)
        l.insert(15)
        assert l.search(10)
        assert l.search(52)
        assert l.search(58)
        assert l.search(15)

    def test_remove(self):
        assert l.search(52)
        l.remove(52)
        assert l.search(52) == False
    
    def test_show(self):
        l.insert(14)
        l.insert(9)
        l.insert(99)
        l.insert(67)
        l.insert(2)
        l.insert(6)
        l.insert(27)
        l.insert(45)
        l.insert(77)
        l.insert(72)
        l.show() == '50, 10, 9, 2, 6, 15, 14, 27, 45, 52, 58, 67, 77, 72, 99'

# 50, 10, 52, 58, 15, 14, 9, 99, 67, 2, 6, 27, 45, 77, 72
# 50, 10, 9, 2, 6, 15, 14, 27, 45, 52, 58, 67, 77, 72, 99