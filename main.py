from __future__ import annotations
from typing import Optional


class Node:
    """Simple singly linked list node."""
    def __init__(self, value: int, next: Optional["Node"] = None) -> None:
        self.value = value
        self.next = next

    def __repr__(self) -> str:
        return f"Node({self.value})"


def remove_cars(head: Optional[Node], target: int) -> Optional[Node]:
    """
    Remove all nodes from the linked list whose value equals target.
    Return the new head of the list.
    """
    # Skip any leading nodes that match the target
    while head is not None and head.value == target:
        head = head.next

    # Traverse the list, unlinking nodes with the target value
    current = head
    while current is not None and current.next is not None:
        if current.next.value == target:
            current.next = current.next.next
        else:
            current = current.next

    return head