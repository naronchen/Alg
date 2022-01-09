def shortestPath(edges, src, target):
    g = buildGraph(edges)
    print(g)
    return BFS(g, src, target)

def BFS(g, src, t):
    queue = [ (src, 0) ]
    visited = []
    while len(queue) > 0:
        curNode, dist = queue.pop()
        # print(curNode)
        if curNode == t:    return dist
        for neighbor in g[curNode]:
            if neighbor not in visited:
                queue.append((neighbor, dist + 1))
                visited.append(curNode)
    return -1
            

def buildGraph(edges):
    g = {}
    for edge in edges:
        nodeA = edge[0]
        nodeB = edge[1]
        if nodeA not in g: g[nodeA] = []
        if nodeB not in g: g[nodeB] = []

        g[nodeA].append(nodeB)
        g[nodeB].append(nodeA)
    
    return g

def main():
    edges = [['w', 'x'], ['x','y'], ['z', 'y'], ['z', 'v'], ['w', 'v']]
    print(shortestPath(edges, 'w', 'z'))


main()