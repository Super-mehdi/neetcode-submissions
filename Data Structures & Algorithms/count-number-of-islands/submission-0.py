class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS,COLS = len(grid),len(grid[0])
        def dfs(r,c):
            if r>= ROWS or c>= COLS or r<0 or c<0 or grid[r][c] == "0":
                return False
            grid[r][c] = "0"

            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1) 

            return True
        islands = 0
        for i in range(ROWS):
            for j in range(COLS):
                islands += 1 if dfs(i,j) else 0
        return islands


        