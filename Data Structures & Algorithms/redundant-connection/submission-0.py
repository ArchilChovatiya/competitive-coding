class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]
        def find(n):
            if parent[n]!=n:
                parent[n] = find(parent[n])
            return parent[n]
                
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return [n1, n2]
            parent[p1] = parent[p2]
            return False
        for [v1,v2] in edges:
            if union(v1,v2):
                return [v1,v2]
            

