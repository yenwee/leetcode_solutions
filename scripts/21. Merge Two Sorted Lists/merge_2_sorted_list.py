# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return None
        
        merged = []
        while list1 != None:
            merged.append(list1.val)
            list1 = list1.next
        
        while list2 != None:
            merged.append(list2.val)
            list2 = list2.next
        
        merged.sort()
        ans = pointer = ListNode()
        for i in range(len(merged)):
            pointer.val = merged[i]
            
            if i != len(merged) - 1:
                pointer.next = ListNode()
                pointer = pointer.next
            
        return ans
        