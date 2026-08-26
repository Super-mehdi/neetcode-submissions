class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        d = {i:[] for i in range(n)}
        for a,b in edges:
            d[a].append(b)
            d[b].append(a)

        visit = set()

        def dfs(node):
            if node in visit:
                return
            visit.add(node)
            for nei in d[node]:
                dfs(nei)
            return 
        
        cnt = 0
        for x in range(n):
            if x not in visit :
                dfs(x)
                cnt+=1
        return cnt
            
        