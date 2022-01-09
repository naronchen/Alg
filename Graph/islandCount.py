def islandCount(grid):
    count = 0
    visited = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            land = grid[i][j]
            if (i,j) not in visited and land == 'L':
                temp = DFS(grid, i, j)
                visited+=temp
                count += 1 

    return count

def DFS(grid, r, c): #return a list of visited node
    stack = [(r,c)]
    visited = []
    while len(stack) > 0:
        rNow, cNow = stack.pop()
        UDLR = [False, False, False, False]
        if rNow > 0 and grid[rNow-1][cNow] == 'L': 
            UDLR[0] = (rNow-1, cNow)
        if rNow < len(grid) - 1 and grid[rNow+1][cNow] == 'L': 
            UDLR[1] = (rNow+1, cNow)
        if cNow > 0 and grid[rNow][cNow-1] == 'L': 
            UDLR[2] = (rNow, cNow-1)
        if cNow < len(grid[0]) - 1 and grid[rNow][cNow+1] == 'L': 
            UDLR[3] = (rNow, cNow+1)

        for i in range(len(UDLR)):
            cur = UDLR[i]
            if cur is not False and cur not in visited:     
                stack.append((cur))
                visited.append(cur)
    return visited
            

def main():
    grid = [
    ['W','L','W','W','W'],
    ['L','L','L','W','L'],
    ['W','L','L','L','W'],
    ]

    print(islandCount(grid))

main()