"""
Grid Pathfinding
-----------------------------------------------
Find the shortest path from S (start) to G (goal) on a fixed grid,
where '#' cells are walls and every step costs 1.
YOUR TASK: adapt this into A* search.
import heapq
ROWS, COLS = 12, 16
START = (0, 0)
GOAL = (11, 15)
_GRID_ROWS = [
    "S....#.......#..",
    ".....#.......#..",
    ".....#........##",
    ".....#..........",
    ".....#....#.....",
    ".....#.#..#.....",
    ".....#....#.....",
    ".....#....#.....",
    "..........#.####",
    "..........#.....",
    "..........#.####",
    "..........#....G",
]
"""

import heapq

def AStar(grid, start, goal):
    rows = len(grid)
    cols = len(grid[0])

    def heuristic(position):
        return abs(position[0] - goal[0]) + abs(position[1] - goal[1])

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    frontier = [(heuristic(start), start)]
    pathcost = {start: 0}
    came_from = {}
    visited = set()

    while frontier:
        f, current = heapq.heappop(frontier)

        if current == goal:
            return backtrack(came_from, current, pathcost[goal])

        if current in visited:
            continue

        visited.add(current)

        for dr, dc in directions:
            neighbor = (current[0] + dr, current[1] + dc)

            # Ignore positions outside the grid
            if not (0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols):
                continue

            # Ignore walls
            if grid[neighbor[0]][neighbor[1]] == '#':
                continue

            # Every step costs 1
            cost = 1
            tent_cost = pathcost[current] + cost

            if tent_cost < pathcost.get(neighbor, float('inf')):
                pathcost[neighbor] = tent_cost
                came_from[neighbor] = current

                f_cost = tent_cost + heuristic(neighbor)
                heapq.heappush(frontier, (f_cost, neighbor))

    return [], -1


def backtrack(came_from, current, cost):
    path = [current]

    while current in came_from:
        current = came_from[current]
        path.append(current)

    path.reverse()

    return path, cost


GRID_ROWS = [
    "S....#.......#..",
    ".....#.......#..",
    ".....#........##",
    ".....#..........",
    ".....#....#.....",
    ".....#.#..#.....",
    ".....#....#.....",
    ".....#....#.....",
    "..........#.####",
    "..........#.....",
    "..........#.####",
    "..........#....G",
]

START = (0, 0)
GOAL = (11, 15)

L = AStar(GRID_ROWS, START, GOAL)
print(L)
