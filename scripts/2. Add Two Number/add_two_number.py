# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        l3 = ListNode() 
        dummy = l3
        carry_forward = 0
        while (l1 != None) or (l2 != None) or (carry_forward != 0):
            
            total = 0
            
            if l1:
                total += l1.val
                l1 = l1.next
                
            if l2:
                total += l2.val
                l2 = l2.next
                
            dummy.val = total + carry_forward
            
            carry_forward = 0
            if dummy.val >= 10:
                carry_forward = 1
                dummy.val -= 10
            
            if (l1 != None) or (l2 != None) or (carry_forward != 0):
                next_node = ListNode()
                dummy.next = next_node
                dummy = dummy.next  
                
        return l3
            