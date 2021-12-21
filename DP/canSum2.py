def canSum(target, nums):
    l = target + 1
    t = [False]*l
    t[0] = True


    for i in range(len(t)):
        if t[i] is True: 
            for n in nums:
                if i+n < len(t): t[i + n] = True 
        
    print(t[-1])

canSum(100, [7,15])