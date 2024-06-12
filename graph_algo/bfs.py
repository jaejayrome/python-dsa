'''
Breadth First Search Algorithm: 
classic graph algorithm that can be used for searching at a breadth manner
this assumes that the graph is being stored in an adjacency list

this could be used to determine the number of connected components as well for an undirected graph

TODO: add in how can we backtrack using path

Optimised Time Complexity: O(V+E), where V is the number of vertices and E is the number of edges
'''
# Question assumes that we are trying to store a graph using an adj list
def bfs(graph, startNode):
    # assuming that graph is non-empty (means cardinality of vertex set is > 0)
    queue = []
    visited = []

    # enqueue the starting node
    queue.append(startNode)
    visited.append(startNode)

    # assuming that the queue is non-empty
    while queue:
        targetNode = queue.pop()
        neighbours = graph[targetNode]
        for _, neighbour in enumerate(neighbours):
            if neighbour not in visited:
                queue.append(neighbour)
                visited.append(neighbour)