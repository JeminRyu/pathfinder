from graphMaker import Graph

graph = Graph(15)

def bfs(graph):
    graph.print()
    q = [graph.getStart()]
    endRow, endCol = graph.getEnd()
    while(q):
        cur = q.pop(0)
        if(graph.seen(cur[0], cur[1])):
            continue
        q.extend(graph.getAdj(cur[0], cur[1]))
        if(cur[0] == endRow and cur[1] == endCol):
            print("BFS search on graph")
            graph.print()
            return
        else:
            graph.setSeen(cur[0], cur[1])
    graph.print()
    print("No path available to end.")

def dfs(graph):
    graph.print()
    stk = [graph.getStart()]
    endRow, endCol = graph.getEnd()
    while(stk):
        cur = stk.pop()
        if(graph.seen(cur[0], cur[1])):
            continue
        stk.extend(graph.getAdj(cur[0], cur[1]))
        if(cur[0] == endRow and cur[1] == endCol):
            print("DFS search on graph")
            graph.print()
            return
        else:
            graph.setSeen(cur[0], cur[1])
    graph.print()
    print("No path available to end.")

def djikstras(graph):
    graph.print()
    pathDict = {}
    for r in range(graph.getLength()):
        for c in range(graph.getLength()):
            pathDict[(r, c)] = [float("inf"), [0, 0]]
    pathDict[(graph.getStart()[0], graph.getStart()[1])] = [0, graph.getStart()]
    


dfs(graph)


