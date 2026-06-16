class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t , b , l , r = 0 , len(matrix)-1, 0 , len(matrix[0])-1
        while t <= b:
            v = t + (b-t)//2
            if target < matrix[v][0]:
                b = v - 1
            elif target > matrix[v][-1]:
                t = v + 1
            else:
                while l <= r:
                    m = l + (r-l)//2
                    if target == matrix[v][m]:
                        return True
                    elif target < matrix[v][m]:
                        r = m - 1
                    else:
                        l = m + 1
                return False
        return False  