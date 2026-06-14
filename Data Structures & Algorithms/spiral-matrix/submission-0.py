class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l , r , t , b = 0, len(matrix[0])-1, 0, len(matrix)-1
        res = []
        while l <= r:
            for i in range(l, r+1):
                res.append(matrix[t][i])
            t+=1
            if t  > b: break
            for j in range(t, b+1):
                res.append(matrix[j][r])
            
            r-=1
            if l > r: break
            for k in range(r, l-1, -1):
                res.append(matrix[b][k])
            b-=1

            if t  > b: break
            for m in range(b, t-1, -1):
                res.append(matrix[m][l])
            l+=1
        return res


            

