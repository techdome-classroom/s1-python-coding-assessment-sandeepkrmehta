class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:

        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c):
            grid[r][c] = 'W'
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 'L':
                    dfs(nr, nc)
        
        island_count = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'L':
                    dfs(r, c)
                    island_count += 1
        
        return island_count