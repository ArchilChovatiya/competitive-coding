class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = [False,False,False]
        for triplet in triplets:
            if not res[0] and triplet[0] == target[0] and triplet[1] <= target[1] and triplet[2] <=target[2]:
                res[0] = True 
            if not res[1] and triplet[1] == target[1] and triplet[0] <= target[0] and triplet[2] <=target[2]:
                res[1] = True 
            if not res[2] and triplet[2] == target[2] and triplet[1] <= target[1] and triplet[0] <=target[0]:
                res[2] = True 
        return res[0] and res[1] and res[2]