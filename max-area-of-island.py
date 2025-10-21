from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r,c):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0):
                return 0
            grid[r][c] = 0
            return (1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1))

        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r, c))
            
        return area

Solution = Solution()

grid = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]
]
print(Solution.maxAreaOfIsland(grid))  # Output: 6

# Time Complexity
# The time complexity of the maxAreaOfIsland function is O(ROWS * COLS), where ROWS is the number of rows in the grid and COLS is the number of columns.
# In the worst case, the DFS will visit every cell in the grid once.

# Space Complexity
# The space complexity of the maxAreaOfIsland function is O(ROWS * COLS) in the worst case, as the recursion stack could go as deep as the number of cells in the grid.

# Iterative DFS
# An alternative approach to avoid deep recursion is to use an iterative DFS with a stack. This can help manage the recursion depth and avoid hitting Python's recursion limit.

# Leetcode 695. Max Area of Island
# Link : https://leetcode.com/problems/max-area-of-island/
# Tags : Depth-First Search, Breadth-First Search, Union Find, Matrix

# Explanation
# The function maxAreaOfIsland calculates the maximum area of an island in a 2D grid. An island is defined as a group of connected 1s (land) surrounded by 0s
# (water). The function uses Depth-First Search (DFS) to explore each island and calculate its area, updating the maximum area found during the traversal.
# The provided example grid contains several islands, and the function correctly identifies the largest one with an
# area of 6.