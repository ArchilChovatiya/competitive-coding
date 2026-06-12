class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n , m = len(board), len(board[0])
        visited = set()
        def helper(i, j, target):
            if target == len(word):
                return True
            if i < 0 or j < 0 or i >=n or j>=m or (i,j) in visited:
                return False
            if board[i][j] == word[target]:
                visited.add((i,j))
                res = helper(i+1,j,target+1) or helper(i,j+1, target+1) or helper(i-1,j, target+1) or helper(i,j-1, target+1)
                visited.remove((i,j))
                return res
        for i in range(n):
            for j in range(m):
                if helper(i,j,0):
                    return True
        return False
