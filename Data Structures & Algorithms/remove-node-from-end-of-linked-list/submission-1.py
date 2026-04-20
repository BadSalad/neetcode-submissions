# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        c = 0
        while temp:
            c += 1
            temp = temp.next
        
        k = 0 
        curr = head
        prev =ListNode()
        while curr:
            k +=1
            if(c==n):
                head=head.next
                break
            if(c-k == n-1):
                prev.next = curr.next
                break
            prev = curr
            curr = curr.next
        
        return head