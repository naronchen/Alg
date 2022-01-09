def undirectedPath(edges, src, target):
    graph = buildGraph(edges)
    return hasPath(graph, src, target)

def hasPath(g, src, t, visited = []):
    if src == t : return True
    if src in visited: return False
    visited.append(src)

    for node in g[src]:
        if hasPath(g, node, t, visited) is True: 
            return True  

    
    return False

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
    edges = [ ["i", "j"], ["k", "i"], ["m","k"], ["k", "l"], ["o","n"] ] 
    result = undirectedPath(edges,"j","m") # tell whether it is opssible from to go from j to m
    print(result)

main()
