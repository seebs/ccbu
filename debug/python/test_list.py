from linked_list import LinkedList
import pytest

def test_list_creation():
    with pytest.raises(ValueError):
        empty = LinkedList[int].from_list([])

def test_list_contains():
    l1: LinkedList[int] = LinkedList[int].from_list(3, 4)
    l2: LinkedList[int] = LinkedList[int].from_list([3, 4])
    assert l1.contains(3)
    assert l1.contains(4)
    assert l2.contains(3)
    assert l2.contains(4)
    assert not l1.contains(5)

def test_cycle_detection():
    nodes = [LinkedList[int](i) for i in range(5)]
    nodes[0].next = nodes[1]
    nodes[1].next = nodes[2]
    nodes[2].next = nodes[3]
    nodes[3].next = nodes[4]
    nodes[4].next = nodes[0]
    assert not nodes[0].contains(23)
    assert nodes[0].contains(3)
    nodes[4].next = nodes[2]
    assert not nodes[0].contains(23)
    assert nodes[0].contains(3)
