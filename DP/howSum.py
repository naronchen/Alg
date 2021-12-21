def howSum(target, nums, d = {}):
    if target in d: return d[target]
    if target == 0: return []
    if target < 0: return None

    for i in nums:
        temp = howSum(target - i, nums, d)
        if temp is not None:
            d[target] = temp.append(i)
            return d[target]

    d[target] = None
    return None

print(howSum(300, [7,14]))