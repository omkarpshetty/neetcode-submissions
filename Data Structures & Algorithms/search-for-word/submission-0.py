class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def dfs(r, c, i):
            # Base case: matched all characters
            if i == len(word):
                return True
            # Out of bounds, wrong char, or already visited
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                board[r][c] != word[i] or
                (r, c) in visited):
                return False

            visited.add((r, c))  # mark as visited

            # Explore all 4 directions
            found = (dfs(r+1, c, i+1) or
                     dfs(r-1, c, i+1) or
                     dfs(r, c+1, i+1) or
                     dfs(r, c-1, i+1))

            visited.remove((r, c))  # backtrack (unmark)
            return found

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):  # try starting from every cell
                    return True
        return False