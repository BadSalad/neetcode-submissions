# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        h1 = list1
        h2 = list2
        if not h1:
            return h2
        if not h2:
            return h1
        if(h1.val <= h2.val):
            head = h1
        else:
            head = h2
        curr = ListNode()
        prev = ListNode()
        while(h1 or h2):
            if not h1:
                prev = curr
                curr = h2
                prev.next=curr
                break

            if not h2:
                prev = curr
                curr = h1
                prev.next=curr
                break            
            
            if(h1.val <= h2.val):
                prev = curr
                curr = h1
                prev.next=curr
                h1 = h1.next
            else:
                prev = curr
                curr = h2
                prev.next=curr
                h2 = h2.next
        return head


        