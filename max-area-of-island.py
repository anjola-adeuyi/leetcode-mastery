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
print(grid)

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


def maxAreaIter(grid):
    if not grid or not grid[0]: return 0
    R, C = len(grid), len(grid[0])
    visited = set()
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    best = 0
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 1 and (r,c) not in visited:
                area = 0
                stack = [(r,c)]
                visited.add((r,c))
                while stack:
                    x,y = stack.pop()
                    area += 1
                    for dx,dy in dirs:
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] == 1 and (nx,ny) not in visited:
                            visited.add((nx,ny))
                            stack.append((nx,ny))
                best = max(best, area)
    return best

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
print(maxAreaIter(grid))  # Output: 6
print(grid)

# The maxAreaIter function implements an iterative DFS approach to find the maximum area of an island in a 2D grid.
# It uses a stack to explore each island and a set to keep track of visited cells, ensuring that each cell is processed only once.
# The time and space complexity remain the same as the recursive version: O(ROWS * COLS) for both time and space in the worst case.
