class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        edgs = {}
        for [x,y] in edges:
            if x not in edgs: edgs[x] = []
            if y not in edgs: edgs[y] = []
            edgs[x].append(y)
            edgs[y].append(x)
        
        visited = set()
        def helper(i , prev):
            if i in visited: return False
            visited.add(i)
            for j in edgs.get(i,[]):
                if j != prev:
                    if not helper(j , i): 
                        return False
            return True
        if not helper(0,-1):
            return False
        return len(visited) == n
