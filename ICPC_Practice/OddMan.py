n = int(input())
#Set cannot have two with the same value
for i in range(n):
    m = int(input())
    v = list(map(int, input().split()))
    d = set() #chuxianguolede
    poss = set(v)
    for j in v.copy():
        if j in d:
            poss.remove(j)
            d.remove(j) # if not found, no remove, if remove works, it means it appears for the second time
        d.add(j)
    print('Case #{}: {}'.format(i+1, poss.pop()))