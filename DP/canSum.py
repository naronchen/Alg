def canSum(target, nums, d={}):
    if target in d: return d[target]
    if target == 0: return True
    if target < 0: return False

    for i in nums:
        if canSum(target-i, nums,d) is True: 
            d[target] = True
            return True
    
    d[target] = False
    return False

print(canSum(300, [7,14]))