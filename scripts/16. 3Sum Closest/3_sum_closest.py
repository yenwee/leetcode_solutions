class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        distance = sum(nums[-3:])
        for i in range(0,len(nums) - 3):
            l , r = i + 1, len(nums) - 1
            while ((i < l) and (l < r)):
                curr = nums[i] + nums[l] + nums[r]
                if curr > target:
                    r -= 1
                if curr < target:
                    l += 1
                if curr == target:
                    return curr
                if (abs(curr - target) < abs(distance - target)):
                    distance = curr
            if sum(nums[i+1:i+3]) > target :
                break
        return distance