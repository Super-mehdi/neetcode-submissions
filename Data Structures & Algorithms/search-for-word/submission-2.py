class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def dfs(l,c,i):
            if i == len(word):
                return True
            if ( l >= ROWS or l<0 or c<0 or c >= COLS or board[l][c] == '#' or board[l][c] != word[i] ):
                return False
            board[l][c] = '#'
            res = (
                dfs(l+1,c,i+1) or
                dfs(l,c+1,i+1) or
                dfs(l-1,c,i+1) or
                dfs(l,c-1,i+1)
            )
            board[l][c] = word[i]
            return res
        for l in range(ROWS):
            for c in range(COLS):
                if dfs(l,c,0):
                    return True
        return False




