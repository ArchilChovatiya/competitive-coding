class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            res = min(res, nums[l])
            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m
        return res

