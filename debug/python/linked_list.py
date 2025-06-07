from dataclasses import dataclass
from typing import Any, Generic, Iterable, TypeVar, Union, cast

T = TypeVar("T")

@dataclass
class LinkedList(Generic[T]):
    value: T
    next: "LinkedList | None" = None

    @property
    def _next(self) -> "LinkedList[T]":
        # This exists to get pyright to stop spuriously
        # complaining that l_slow.next could be None in
        # the contains logic. Since l_slow is following
        # l_fast, it never reaches a value that hasn't
        # already been checked.
        return cast("LinkedList[T]", self.next)

    @classmethod
    def from_list(cls, items: Union[list[T], T], *extra_items: T) -> "LinkedList[T]":
        first: T
        rest: Iterable[T]
        if isinstance(items, list):
            if len(items) == 0:
                raise ValueError("empty lists not supported")
            first, rest = items[0], items[1:]
        else:
            first, rest = items, extra_items
        head = LinkedList[T](first)
        cur = head
        for item in rest:
            new_node = LinkedList[T](item)
            cur.next = new_node
            cur = new_node
        return head

    def contains(self, value: T) -> bool:
        l_fast: "LinkedList | None" = self
        l_slow: "LinkedList | None" = self
        while l_fast is not None:
            if l_fast.value == value:
                return True
            l_fast = l_fast._next
            if l_fast == l_slow:
                return False
            if l_fast.value == value:
                return True
            l_fast = l_fast._next
            if l_fast == l_slow:
                return False
            l_slow = l_slow._next
        return False

    def __init__(self, value: T):
        self.value = value
