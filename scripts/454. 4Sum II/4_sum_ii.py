class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        zero_count = 0
        dict_A = {}
        for i in nums1:
            for j in nums2:
                total = i + j
                if total not in dict_A:
                    dict_A[total] = 1
                else:
                    dict_A[total] += 1
                    
        for k in nums3:
            for l in nums4:
                total = k + l
                if -total in dict_A:
                    zero_count += dict_A[-total]
                
        return zero_count