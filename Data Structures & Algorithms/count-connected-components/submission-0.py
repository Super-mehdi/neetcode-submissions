class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        d = {i:[] for i in range(n)}
        for a,b in edges:
            d[a].append(b)
            d[b].append(a)

        visit = set()

        def dfs(node,par):
            if node in visit:
                return
            visit.add(node)
            for nei in d[node]:
                if nei == par:
                    continue
                dfs(nei,node)
            return 
        
        cnt = 0
        for x in d.keys():
            if x not in visit :
                dfs(x,-1)
                cnt+=1
        return cnt
            
        