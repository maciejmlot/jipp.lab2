from collections import deque

def bfs(graph, start:int, destination:int):
    q = deque([[start]])
    visited = []

    while q:
        path = []
        path = q.popleft()
        vertex = path[-1]

        if vertex == destination:
            return path
        
        if vertex not in visited:
            visited.append(vertex)

            for neighbor in graph.get(vertex, []):
                if neighbor not in visited:
                    newPath = path + [neighbor]
                    q.append(newPath)

    return None

def zad2():
    verticesCount = int(input("Podaj liczbe wierzchołków "))
    graph = {}
    for i in range(1, verticesCount+1):
        print("Podaj sąsiadów wierzchołka ", i)
        graph [i] = list(map(int, input(" po przecinkach ").split(",")))
    else:
        print("Lepiej żeby sie zgadzało")
        print(graph)
    startVertex = int(input("Podaj wierzchołek startowy "))
    finishVertex = int(input("Podaj wierzchołek końcowy "))

    print("najkrotsza sciezka to ", bfs(graph, startVertex, finishVertex))