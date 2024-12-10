def find_valid_paths(grid):
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    valid_paths = []

    def dfs(path, x, y, current_value):
        if current_value == 9:
            valid_paths.append(path[:])
            return
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == current_value + 1:
                dfs(path + [(nx, ny)], nx, ny, current_value + 1)

    # Start DFS from all cells with value 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                dfs([(i, j)], i, j, 0)

    return valid_paths

# Example input
grid = [
    [8, 9, 0, 1, 0, 1, 2, 3],
    [7, 8, 1, 2, 1, 8, 7, 4],
    [8, 7, 4, 3, 0, 9, 6, 5],
    [9, 6, 5, 4, 9, 8, 7, 4],
    [4, 5, 6, 7, 8, 9, 0, 3],
    [3, 2, 0, 1, 9, 0, 1, 2],
    [0, 1, 3, 2, 9, 8, 0, 1],
    [1, 0, 4, 5, 6, 7, 3, 2],
]

# Find all valid paths
result_paths = find_valid_paths(grid)
print("Valid paths from 0 to 9:")
for path in result_paths:
    print(path)
print(len(result_paths))