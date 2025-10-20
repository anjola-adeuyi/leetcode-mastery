from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def bfs(r, c):
            q = deque()
            grid[r][c] = "0"
            q.append((r, c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if(nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == "0"):
                        continue

                    q.append((nr, nc))
                    grid[nr][nc] = "0"


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1

        return islands


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0"):
                return
            grid[r][c] = "0"
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1

        return islands
        

Solution = Solution()
grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
print(Solution.numIslands(grid))  # Output: 1

# Time: O(R*C) where R is number of rows and C is number of columns
# Space: O(min(R, C)) for the queue in BFS


# Leetcode 200. Number of Islands
# https://leetcode.com/problems/number-of-islands/
# Medium
# Tags: Array, Depth-First Search, Breadth-First Search, Union Find, Matrix


## Explanation:
# We traverse each cell in the grid. When we find a '1' (land),
# we initiate a BFS to mark all connected '1's as '0's (water),
# effectively marking the entire island as visited.
# We increment our island count each time we start a new BFS.
# The BFS explores all four possible directions (up, down, left, right)
# from the current cell, adding valid land cells to the queue for further exploration.
# This process continues until all cells in the grid have been checked.
# Example:
# Input:
# 11110
# 11010
# 11000
# 00000
# Output: 1
# Explanation: There is one island in the grid.


