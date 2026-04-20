# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c=0
        num1 =0 
        while l1:
            num1 = int(l1.val*math.pow(10,c)+num1)
            l1 = l1.next
            c+=1
        c=0
        num2 =0 
        while l2:
            num2 = int(l2.val*math.pow(10,c)+num2)
            l2 = l2.next
            c+=1

        final = num1 + num2
    
        dummy= prev = ListNode(0)
        if final == 0:
            return dummy

        while final > 0:
            d = final%10
            new = ListNode(d)
            prev.next = new
            prev = new
            final = int(final/10)
        
        return dummy.next
        