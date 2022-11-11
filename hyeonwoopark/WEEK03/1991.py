# 백준 1991 트리 순회

import sys

n = int(sys.stdin.readline())
tree = {}

for i in range(n):
    root, left, right = sys.stdin.readline().strip().split(" ")
    tree[root] = [left, right]

def preOrder(tree: dict, key: str):
    print(key, end="")
    
    if tree[key][0] != '.':
        preOrder(tree, tree[key][0])
    
    if tree[key][1] != '.':
        preOrder(tree, tree[key][1])

def inOrder(tree: dict, key: str):
    if tree[key][0] != '.':
        inOrder(tree, tree[key][0])
    
    print(key, end="")
    
    if tree[key][1] != '.':
        inOrder(tree, tree[key][1])

def postOrder(tree: dict, key: str):
    if tree[key][0] != '.':
        postOrder(tree, tree[key][0])
    
    if tree[key][1] != '.':
        postOrder(tree, tree[key][1])
    
    print(key, end="")

preOrder(tree, 'A')
print()
inOrder(tree, 'A')
print()
postOrder(tree, 'A')