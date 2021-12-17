def gridTraveler(r, c, d={}):
    key = str(r) + " " + str(c)
    alterKey = str(c) + " " + str(r)
    if key in d: return d[key]
    if alterKey in d: return d[alterKey]
    if r == 0 or c == 0: return 0
    if r == 1 and c == 1: return 1
    d[key] =  gridTraveler(r-1, c, d) + gridTraveler(r, c-1, d)
    return d[key]
    
print(gridTraveler(18,18))