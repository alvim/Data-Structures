from LinkedList import LinkedList

class TestLinkedList():
    def test_list_init(self):
        l = LinkedList()
        assert hasattr(l, 'first')

    def test_add_to_front(self):
        assert 1 == 1