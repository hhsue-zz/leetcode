#!/usr/bin/python

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        node = head
        prev = None
        while node:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node
        return prev

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a.next = b
b.next = c

print a.val
print a.next.val
print a.next.next.val

s = Solution()
print s.reverseList(a)

