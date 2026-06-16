class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.curr = []
        res = []
        def dfs(index):
            if index == len(nums):
                res.append(self.curr[:])
                return
            self.curr.append(nums[index])
            dfs(index+1)
            self.curr.pop()
            dfs(index+1)
        dfs(0)
        return res
