class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        maxSum = -sys.maxsize
        for num in nums:
            total = max(total+num, num)
            maxSum = max(maxSum, total)
        return maxSum