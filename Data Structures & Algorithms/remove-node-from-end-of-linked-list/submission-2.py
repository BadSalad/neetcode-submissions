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

        if(c==n):
                return head.next
    
        k = 0 
        curr = head
        while curr:
            k +=1
            if(c-k == n):
                curr.next = curr.next.next
                break
            curr = curr.next
        
        return head