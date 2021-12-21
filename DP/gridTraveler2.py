def gridT(m,n):
    numR = m+1
    numC = n+1
    t = [[0]*numC]*numR
    for r in range(1, numR):
        for c in range(1,numC):
            if r == 1 and c == 1: fill = 1
            else: fill = t[r-1][c] + t[r][c-1]
            t[r][c] = fill
    
    print(t[-1][-1])

gridT(1,1)
gridT(2,3)
gridT(3,2)
gridT(3,3)
gridT(18,18)


