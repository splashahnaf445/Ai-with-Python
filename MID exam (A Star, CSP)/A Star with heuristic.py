import heapq

# coords = {
#     "A":(1,3),"B":(4,3),"C":(5,9),"D":(0,4),"G":(9,9)
#     }

# def heuristicx(start,goal):
#     x1,y1 = coords[start]
#     x2,y2 = coords[goal]
#     #Manhattan
#     return abs(x1-x2)+abs(y1-y2)

# goal = 'G'
# manhattan = {
#     node:heuristicx(node,goal) for node in coords
# }
# print(manhattan)

def Astar(graph,heuristic,start,goal):
    frontier = [(heuristic[start],start)]
    pathcost = {start:0}
    came_from = {}
    visited = set()

    while frontier:
        f,current = heapq.heappop(frontier)
        if current == goal:
            return backtrack(came_from,current),pathcost[goal]
        if current in visited:
            continue
        visited.add(current)
        for neighbour,cost in graph[current].items():
            tent_cost = pathcost[current]+cost
            if tent_cost < pathcost.get(neighbour, float ('inf')):
                pathcost[neighbour] = tent_cost
                came_from[neighbour]=current
                fcost = tent_cost+heuristic[neighbour]
                heapq.heappush(frontier, (fcost, neighbour))
    return None,float('inf')


def backtrack(came_from, current):
        path = [current]
        while current in came_from:
            current=came_from[current]
            path.append(current)
        return path[::-1]
            

graph = {
        "S": {"A": 1, "B": 4},
        "A": {"S": 1, "B": 2, "C": 2},
        "B": {"S": 4, "A": 2, "G": 5},
        "C": {"A": 2, "G": 3},
        "G": {"B": 5, "C": 3},
    }
heuristic = {"S": 7, "A": 6, "B": 4, "C": 2, "G": 0}

path, cost = Astar(graph, heuristic, "S", "G")
print("Path:", path)
print("Cost:", cost)