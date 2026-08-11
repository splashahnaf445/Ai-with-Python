
#Eucledean distance
import math



coords = {
    'S': (0, 0), 'A': (1, 2), 'B': (2, 1), 'G': (3, 3)
}

def eucledean(start,goal):
    x1,y1 = coords[start]
    x2,y2 = coords[goal]
    return round(math.sqrt((x2-x1)**2 + (y2-y1)**2))


goal = 'G'

heuristic = {
    node : eucledean(node,goal) for node in coords
}

print(heuristic)

#Manhattan distance

def manhattan(start,goal):
    x1,y1 = coords[start]
    x2,y2 = coords[goal]
    return abs(x2-x1)+abs(y2-y1)

goal = 'G'

heuristic2 = {
    node : manhattan(node,goal) for node in coords
}

print(heuristic2)