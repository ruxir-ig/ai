n = int(input("Enter grid size (for NxN grid): "))
grid = []
print("Enter grid elements (0 for free, 1 for obstacle):")
for i in range(n):
    row = []
    for j in range(n):
        val = int(input(f"Enter value for cell [{i}][{j}]: "))
        row.append(val)
    grid.append(row)
print("\nGrid:")
for i in range(n):
    print(grid[i])

# ----------------------------------------------------------------------
start = (0, 0)
end = (n - 1, n - 1)

def h(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

open_list = [start]
came = {}
g = {start: 0}

while open_list:
    curr = min(open_list, key=lambda x: g.get(x, 9999) + h(x, end))
    if curr == end:
        break
    open_list.remove(curr)
    # ----------------------------------------------------------------------
    x, y = curr
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
            new_g = g[curr] + 1
            if (nx, ny) not in g or new_g < g[(nx, ny)]:
                g[(nx, ny)] = new_g
                came[(nx, ny)] = curr
                open_list.append((nx, ny))

# ----------------------------------------------------------------------
path = [end]
while path[-1] in came:
    path.append(came[path[-1]])
path.reverse()
print("\nPath found using A*:")
print(path)
