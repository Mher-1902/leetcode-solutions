class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        counter = 0
        rows = len(grid)
        columns = len(grid[0])
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 1:
                    counter += 4
                    if i < rows - 1 and grid[i+1][j] == 1:
                        counter -= 2
                    if j < columns - 1 and grid[i][j+1] == 1:
                        counter -= 2

        return counter
        