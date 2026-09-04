# 1. Problem Setup
EDGES = [
    ("A", "B"), ("A", "C"), ("A", "D"), ("B", "C"), ("B", "E"), ("B", "F"),
    ("C", "D"), ("C", "E"), ("C", "F"), ("D", "E"), ("D", "G"), ("E", "F"),
    ("E", "G"), ("E", "H"), ("F", "G"), ("F", "H"), ("G", "H"),
]

VARIABLES = sorted(set(node for edge in EDGES for node in edge)) #VARIABLES = sorted(set(...)):
#Flattens all edge pairs into a sorted, unique list of region identifiers ['A', 'B', ...].

COLORS = ["Red", "Green", "Blue", "Yellow"]

# Build adjacency list: {node: {neighbors}}
neighbors = {v: set() for v in VARIABLES}  #neighbors = {v: set() for v in VARIABLES}: Initializes an empty adjacency set for each variable.
for u, v in EDGES:
    neighbors[u].add(v)
    neighbors[v].add(u)   #created an undirected graph with edges and variables

# 2. Consistency Checker #def is_consistent(var, color, assignment, neighbors): 
# Validates if assigning color to var violates constraints with already assigned adjacent regions.

def is_consistent(var, color, assignment, neighbors):  #Jei color assign krbo, seita already neihbor ee ache kina
    for neighbor in neighbors[var]:
        if neighbor in assignment and assignment[neighbor] == color:
            # Checks if an adjacent node already holds the identical color.
            return False   #Rejects the assignment if any neighbor shares the color; otherwise, accept
    return True

# 3. Basic Backtracking Algorithm
def basic_backtracking(assignment, variables, colors, neighbors):
    if len(assignment) == len(variables):  
        return assignment  #Base case. If every variable has a valid color assigned, the search terminates successfully.

    # Fixed variable ordering: pick the first unassigned variable
    var = next(v for v in variables if v not in assignment)

    #var = next(v for v in variables if v not in assignment): Fixed ordering heuristic. Takes the first variable that has not yet been given a color.

    for color in colors:   #Tries every color in the fixed list sequentially.
        if is_consistent(var, color, assignment, neighbors):  #Prunes illegal moves before making recursive calls.
            assignment[var] = color   #Tentatively assigns the color
            result = basic_backtracking(assignment, variables, colors, neighbors)  #Recursive call : attempts to color the rest of the graph.
            if result is not None:
                return result     #Propagates success upward once the goal state is found.
            del assignment[var]  # Backtrack ; Removes the assignment if the path reached a dead end.

    return None   #Signals that no color in the domain satisfied the constraints for this branch.

# Execution
solution = basic_backtracking({}, VARIABLES, COLORS, neighbors)
print("Solution:", solution)