# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        d = {}
        for linked_lists in lists:
            while linked_lists != None:
                if linked_lists.val not in d:
                    d[linked_lists.val] = 1
                else:
                    d[linked_lists.val] += 1 
                linked_lists = linked_lists.next
        print(d)
        ans = ListNode()
        if not d:
            ans.val = ''
            return ans
        dummy = ans
        key_list = sorted(d.keys())
        for keys in key_list:
            for k in range(0,d[keys]):
                dummy.val = keys
                if ((keys == key_list[len(key_list)-1]) and (k == d[keys] - 1)):
                    break
                else:
                    dummy.next = ListNode()
                    dummy = dummy.next
        return ans