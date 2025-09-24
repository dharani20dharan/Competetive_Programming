# Leet Code : Number of Islands

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        islands = 0
        
        def dfs(r, c):
            # Check bounds and whether the cell is water
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
                return
            # Mark current land as visited (sink it)
            grid[r][c] = "0"
            # Explore 4 directions
            dfs(r+1, c)  # down
            dfs(r-1, c)  # up
            dfs(r, c+1)  # right
            dfs(r, c-1)  # left
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":  # Found a new island
                    islands += 1
                    dfs(r, c)  # Sink the whole island
        
        return islands