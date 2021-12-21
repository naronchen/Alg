def bestSum(target, nums):
    l = target + 1
    t = [None] * l
    t[0] = []

    for i in range(l):
        if t[i] is not None:
            for n in nums:
                if n+i < l:
                    print(i)
                    if t[i+n] is None or len(t[i+n]) > len(t[i]) + 1:
                        t[i+n] = t[i] + [n]
    
    return t[-1]

print(bestSum(200,[10,9,55]))


