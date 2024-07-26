"""
B025 - https://leetcode.com/problems/delete-node-in-a-linked-list/
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteNode(node):
    node.val = node.next.val
    node.next = node.next.next
