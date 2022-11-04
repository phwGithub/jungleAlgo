import sys
from typing import Any, Type
from __future__ import annotations

class Node:

    def __init__(self, key: Any, value: Any, left: Node = None, right: Node = None) -> None:
        self.key = key
        self.value = value
        self.left = left
        self.right = right

class BinarySearchTree:
    
    def __init__(self) -> None:
        self.root = None

    def search(self, key: Any):
        p = self.root

        while True:
            if p is None:
                return None
            
            if key == p.key:
                return p.value
            elif key < p.key:
                p = p.left
            else:
                p = p.right

    def add(self, key: Any, value: Any):
        return