"""
A* Search — compact version built on heapq
--------------------------------------------
f(n) = g(n) + h(n). Always expand the lowest f. Stop when goal is popped.
"""

# frontier is your to-do list of nodes waiting to be explored — kept as a min-heap
# It starts with just the start node, paired with its f-score
# At the very beginning, g(start) = 0, so f(start) = 0 + h(start) = heuristic[start] — that's why the tuple is (heuristic[start], start)

import heapq


def a_star(graph, heuristic, start, goal):
    frontier = [(heuristic[start], start)]   # heap of (f, node) 
    
    g_score = {start: 0}                      # best known cost to reach each node
    came_from = {}                             # for rebuilding the path
    visited = set()

# Pull out the item with the smallest f-value — this is the single most important line in A* : f, current = heapq.heappop(frontier)
# heapq.heappop does the "find the minimum" work for you
# Unpacks the tuple: f = that node's f-score, current = the node itself

    while frontier:
        f, current = heapq.heappop(frontier)   # lowest f always comes out first(Heap : (heuristic,node) )
        if current == goal:                     # goal check happens on POP, not on generation
            return reconstruct(came_from, current), g_score[goal]
        if current in visited:
            continue  # A node can get pushed onto the heap more than once (if we found multiple ways to reach it)
                       #If we've already finalized this node before, this copy is stale — skip it and go pop the next item
                    #continue jumps straight back to the top of the while loop
        visited.add(current)  #We're committing to this node now — mark it as done so it's never reprocessed (visited na, goal na so take it)

        for neighbor, cost in graph[current].items():  #Loop through every neighbor of the current node
                                        #graph[current] is a dict like {"A": 1, "B": 4} → .items() gives you (neighbor, cost) pairs one at a time
            tentative_g = g_score[current] + cost #"If I went from current to neighbor right now, what would my total cost-so-far be?"
                                                    #= cost to reach current + cost of this one edge
            if tentative_g < g_score.get(neighbor, float('inf')):

                #Compare: is this new route to neighbor cheaper than the best one we knew before?
                #g_score.get(neighbor, float('inf')) = "look up neighbor's best cost so far, or treat it as infinity if we've never reached it" — this one line replaces writing a separate if neighbor not in g_score check
                #f tentative_g is smaller → we just found a better path, so update everything below
                g_score[neighbor] = tentative_g  #Save this new, cheaper cost as the best known cost to reach neighbor
                came_from[neighbor] = current   #Remember: "the best way to reach neighbor right now is by coming from current"
                heapq.heappush(frontier, (tentative_g + heuristic[neighbor], neighbor))
                #Add neighbor to the to-do list with its updated f-score = new g + its heuristic

    return None, float('inf')   # goal unreachable


def reconstruct(came_from, current):
    path = [current]   #Start a list with just the goal node in it (since that's where we're starting the walk-back from)
                        #Right now path = [goal]
    while current in came_from:   #Keep going as long as the current node has a recorded "came from"
                                    #The start node is the only one that was never reached from anywhere (it's where we began), 
                                    #so it's the only node missing from came_from — that's exactly what stops this loop
        current = came_from[current]  #Step one node backward: "who did I arrive at current from?"
                                        #Update current to that previous node
        path.append(current)   #Add that previous node onto the end of the list
                                #So path is being built in reverse order: goal → ... → start
    return path[::-1]     #[::-1] is Python slice notation for "reverse this list" — no loop needed, one built-in slice does it



graph = {
        "S": {"A": 1, "B": 4},
        "A": {"S": 1, "B": 2, "C": 2},
        "B": {"S": 4, "A": 2, "G": 5},
        "C": {"A": 2, "G": 3},
        "G": {"B": 5, "C": 3},
    }
heuristic = {"S": 7, "A": 6, "B": 4, "C": 2, "G": 0}

path, cost = a_star(graph, heuristic, "S", "G")
print("Path:", path)
print("Cost:", cost)