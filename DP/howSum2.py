def howSum(target, nums):
    l = target + 1
    t = [None] * l
    t[0] = []

    for i in range(len(t)):
        if t[i] is not None:
            for n in nums:
                if i+n < (len(t)): t[i + n] = t[i] + [n]
    
    print(t[-1])

howSum(300, [7,15])