def compress(row):
    """Remove zeros and compress the row to the left."""
    filtered = [num for num in row if num != 0]
    return filtered + [0] * (4 - len(filtered))

def merge(row):
    """Merge adjacent equal elements and return the new row."""
    row = compress(row)
    for i in range(3):
        if row[i] == row[i + 1] and row[i] != 0:
            row[i] *= 2
            row[i + 1] = 0
    return compress(row)

def move_left(grid):
    """Apply the left move to the entire grid."""
    return [merge(row) for row in grid]

# Exemplo de uso:
grid = [
    [2, 2, 4, 4],
    [4, 4, 8, 8],
    [16, 0, 16, 0],
    [0, 0, 0, 0]
]

new_grid = move_left(grid)
for row in new_grid:
    print(row)

