class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))
        
        
    def helper(self, nums):    
        res = [0] * len(nums)
        res[0], res[1] = nums[0] , max(nums[0],nums[1])
        for i in range(2,len(nums)):
            res[i] = max(res[i-2]+nums[i],res[i-1])
        return res[-1]