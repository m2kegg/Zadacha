import math
graph = {}
graphWithoutDist = {}

src = open("precize3.csv", 'rt')
for line in src:
    name1, name2, dist, az = line.split(",")
    dist = float(dist)
    az = math.radians(float(az))
    if name1 not in graph and name1 not in graphWithoutDist:
        graph[name1] = []
        graphWithoutDist[name1] = []
    graph[name1].append((name2, dist, az))
    graphWithoutDist[name1].append(name2)
    if name2 not in graph:
        graph[name2] = []
        graphWithoutDist[name2] = []
    graph[name2].append((name1, dist, az - math.pi))
    graphWithoutDist[name2].append(name1)
src.close()

def dfs(graph, start):
    visited, stack = [], [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            stack.extend(set(graph[vertex]) - set(visited))
    return visited

def getCoords(graph, ways):
    x = 0
    y = 0
    coords = {"A00" : [0, 0]}
    for way in range(1, len(ways)):
        x += coords[ways[way - 1]][0] + graph[ways[way - 1]][0][1] if ways[way - 1] == graph[ways[way - 1]][0][0] else graph[ways[way - 1]][1][1] * math.sin(graph[ways[way - 1]][0][2] if ways[way - 1] == graph[ways[way - 1]][0][0] else graph[ways[way - 1]][1][2])
        y += coords[ways[way - 1]][1] + graph[ways[way - 1]][0][1] if ways[way - 1] == graph[ways[way - 1]][0][0] else graph[ways[way - 1]][1][1] * math.cos(graph[ways[way - 1]][0][2] if ways[way - 1] == graph[ways[way - 1]][0][0] else graph[ways[way - 1]][1][2])
        coords[ways[way]] = [x, y]
    return coords

print(getCoords(graph, dfs(graphWithoutDist, "A00")))        
