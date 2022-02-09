class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        d= {}
        unique_nums = list(set(nums))  
        for num in unique_nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1

        if k == 0:
            return sum(1 for num in unique_nums if nums.count(num) > 1)
        
        else:
            return len([num for num, count in d.items() if num + k in d.keys()])