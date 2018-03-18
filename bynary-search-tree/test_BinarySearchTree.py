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
        assert l.root.getValue() == 50