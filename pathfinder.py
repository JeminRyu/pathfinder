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
            graph.graph[endRow][endCol] = 4
            print("\n")
            graph.print()
            return
        else:
            graph.setSeen(cur[0], cur[1])
    print("\n")
    graph.print()
    print("No path available to end.")

bfs(graph)


