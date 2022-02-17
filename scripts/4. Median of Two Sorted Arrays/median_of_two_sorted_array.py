class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        array_one_len = len(nums1)
        array_two_len = len(nums2)
        
        if array_two_len > array_one_len :
            self.findMedianSortedArrays(nums2, nums1)
            
            
        loop = (array_one_len + array_two_len) // 2 + 1

        if loop == 0:
            return nums1[0]
        
        x = 0
        y = 0
        
        for _ in loop:
            