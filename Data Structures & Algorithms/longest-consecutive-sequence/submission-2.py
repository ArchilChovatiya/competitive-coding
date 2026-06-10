class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        visited = set()
        maxLength = 0
        for num in nums:
            if num in visited:
                continue
            curr = num
            length = 0
            while curr in nums:
                visited.add(curr)
                length+=1
                curr+=1
            maxLength = max(maxLength,length)
        return maxLength

