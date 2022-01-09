def MaxCompo(g):
    Max = 0
    for node in g:
        size = getSize(g, node)
        Max = max(size, Max)
    return Max

def getSize(g, node, visited = []): #return size of the graph
    if node == []: return 0
    if node in visited: return 0

    size = 1
    visited.append(node)
    for neighbor in g[node]:
        size += getSize(g, neighbor, visited)
    
    return size

def main():
    graph = {0: [8,1,5], 1:[0], 5:[0,8], 8:[0,5], 2:[3,4], 3:[2,4], 4:[3,2]}
    print(MaxCompo(graph))

main()