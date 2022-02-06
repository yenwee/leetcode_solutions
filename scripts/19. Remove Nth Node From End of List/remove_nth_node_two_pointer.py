# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pointer_one = pointer_two = head
    
        for i in range(n):
            pointer_one = pointer_one.next
        
        if not pointer_one: 
            return head.next
        
        while pointer_one.next:
            pointer_one = pointer_one.next
            pointer_two = pointer_two.next
            
        pointer_two.next = pointer_two.next.next

        return head

            
            
        