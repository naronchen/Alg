import copy 

def bestSum(target, nums, d = {}):
    if target in d: 
        return d[target]
    if target == 0: 
        return []
    if target < 0: 
        return None

    minComb = None

    for i in nums:
        temp = bestSum(target - i, nums, d)
        if temp is not None:
            temp.append(i)
            if minComb is None or len(temp) < len(minComb) : 
                minComb = temp
                # print("Target: ", target, "minComb: ", minComb)

    d[target] = copy.deepcopy(minComb)
    return minComb
    

print(bestSum(4,[1,2]))