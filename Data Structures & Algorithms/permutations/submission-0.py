class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        if not nums:
            return [[]]
        perms = self.permute(nums[1:])

        res = []
        for perm in perms:
            for i in range(len(nums)):
                perm_copy = perm[:]
                perm_copy.insert(i,nums[0])
                res.append(perm_copy)
        return res