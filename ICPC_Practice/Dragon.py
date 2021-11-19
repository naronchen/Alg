line = input().split()
n, m = int(line[0]), int(line[1])
while (n != 0 and m != 0): 
    D = []
    K = []
    for i in range(n):
        D.append(int(input()))
    for i in range(m):
        K.append(int(input()))

    D.sort()
    K.sort()

    b=True
    if (m < n): 
        b=False

    head = 0
    knight = -1
    cost = 0
    while (head < n):
        knight+=1     
        while (knight < m and K[knight] < D[head]):
            knight += 1
        if (knight == m):
            break
        cost += K[knight]
        head +=1

    if (head != n-1 or b==False):
        print ("Loowater is doomed!")
    else:
        print(cost)
    
    line = input().split()
    n, m = int(line[0]), int(line[1])






