class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cumSum = 0
        ans = 0
        hashmap = {}
        for num in nums:
            cumSum += num
            # If cumulative sum equals to k, one continuous subarray is found
            if cumSum == k:
                ans += 1
                
            # If current cumulative minus k is found in hashmap, one continuous subarray is found
            # eg. subarray: 1, 3, 4, 5, 6, 1, 7
            #     cumSum =  1, 4, 8, 13, 19, 20, 27
            # In this case when cumSum = 20, 20 -7 = 13 will be found in hashmap [6 and 1 is actually a cont. subarray]
            # The difference between cumSum at x and x + y position will result in a subarray of y length.
            # With sum of numbers between position x and position x + y
            if cumSum - k in hashmap:
                ans += hashmap[cumSum - k]
                
            # Records cumulative sum in hashmap
            if cumSum in hashmap:
                hashmap[cumSum] += 1
            else:
                hashmap[cumSum] = 1
        return subarrays

            
            
            