# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        if head != None:
            pointer = head.next
            if pointer != None:
                pointer.next, head.next = head, pointer.next
                pointer.next.next = self.swapPairs(pointer.next.next)
                return pointer 
        return head