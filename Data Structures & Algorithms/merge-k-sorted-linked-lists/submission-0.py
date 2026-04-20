# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        hash = [0]*2001

        for l in lists:
            temp = l
            while temp:
                hash[temp.val+1000] += 1
                temp = temp.next
        
        dummy = prev = ListNode(0)

        for i in range(len(hash)):
            if hash[i]!=0:
                t = hash[i]
                while t:
                    new_node = ListNode(i-1000)
                    prev.next = new_node
                    prev = new_node
                    t-=1

        return dummy.next
        