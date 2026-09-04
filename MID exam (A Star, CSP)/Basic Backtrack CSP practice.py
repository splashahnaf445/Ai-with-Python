COLORS = ['Red','Green','Blue']

EDGES = [
    ('WA','NT'),
    ('WA','SA'),
    ('NT','Q'),
    ('Q','NSW'),
    ('SA','NSW'),
    ('SA','V'),
]

VARIABLES = sorted(set(v for edge in EDGES for v in edge))
VARIABLES.append('T')

print(VARIABLES)

NEIGHBOR = {v : set() for v in VARIABLES }
for x,y in EDGES:
    NEIGHBOR[x].add(y)
    NEIGHBOR[y].add(x)

print(NEIGHBOR)

def consistent(var, color, assignment, neighbors):
    for neighbor in neighbors[var]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def basicBacktrack(assignment,color,variables, neigh):
    if len(assignment) == len(VARIABLES):
        return assignment

    var = next(v for v in variables if v not in assignment)

    for col in color:
     if consistent(var,col,assignment,neigh):
         assignment[var]=col
         result = basicBacktrack(assignment,color,variables,neigh)
         if result is not None:
             return result
         del assignment[var]

    return None


solution =  basicBacktrack({},COLORS,VARIABLES,NEIGHBOR)
print(solution)