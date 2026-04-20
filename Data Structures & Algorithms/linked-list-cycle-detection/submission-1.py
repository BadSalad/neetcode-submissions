# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node = set()    
        while head:
            if head.next not in node:
                node.add(head) #head.next would not work in case of fully circular linked lists
                head = head.next
            else:
                return True
        return False
        