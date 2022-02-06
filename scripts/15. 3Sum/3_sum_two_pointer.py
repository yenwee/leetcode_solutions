class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        listed = []
        for i in range(0, len(nums) - 1):
            l, r = i + 1 , len(nums) - 1
            if (nums[i] == nums[i - 1]) and (i != 0):
                continue
            while (l < r):
                curr = nums[i] + nums[l] + nums [r]
                
                if curr  > 0:
                    r -= 1
                elif curr < 0:
                    l += 1
                if (l == r):
                    break
                if curr == 0:
                    listed.append([nums[i],nums[l],nums[r]])  
                    left = nums[l]
                    right = nums[r]
                    while nums[l] == left:
                        l += 1
                        if (l > len(nums) - 1):
                            break
                    while nums[r] == right:
                        r -= 1
                        if (r < i):
                            break
        return listed