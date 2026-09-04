COLORS = ["Red", "Green", "Blue", "Yellow"]

EDGES = [
    ("A", "B"), ("A", "C"), ("A", "D"), ("B", "C"), ("B", "E"), ("B", "F"),
    ("C", "D"), ("C", "E"), ("C", "F"), ("D", "E"), ("D", "G"), ("E", "F"),
    ("E", "G"), ("E", "H"), ("F", "G"), ("F", "H"), ("G", "H"),
]


VARIABLES = sorted(set(v for edge in EDGES for v in edge))

neighbors = {v : set() for v in VARIABLES}
for x,y in EDGES:
    neighbors[x].add(y)
    neighbors[y].add(x)

# 1. Setup Domains Dictionary: {node: [available_colors]}
domains = {v: COLORS.copy() for v in VARIABLES}

#forward checking requires keeping track of each variable's dynamic domain of valid colors.

# 2. MRV Heuristic: Choose variable with fewest remaining legal colors
def select_mrv(assignment, domains):
    unassigned = [v for v in domains if v not in assignment]  #Filters out already colored variables.
    return min(unassigned, key=lambda v: len(domains[v]))  #Selects the variable with the smallest number of valid colors left in its domain.

#from unassigned variables list,
#key=lambda v: means varaible with value : compare with len of domains e.g A has [B,W] , so len returns 2, C returns 1 ; so choose C as MRV

# 3. Forward Checking: Prune neighbor domains based on assignment
def forward_check(var, color, assignment, domains, neighbors):  #Propagates constraints one step forward to adjacent unassigned nodes.
    
    new_domains = {v: list(vals) for v, vals in domains.items()}  #Creates a lightweight copy of the domains mapping
    new_domains[var] = [color]   #Confines the selected variable's domain to the chosen color.
 
    for neighbor in neighbors[var]:  #Evaluates only nodes directly connected by a constraint edge.
        if neighbor not in assignment:   #Only prunes variables that have not yet been assigned.
            if color in new_domains[neighbor]:   
                new_domains[neighbor].remove(color)  #Deletes the chosen color from the neighbor's options since adjacent regions cannot share it.
            # Early Failure Detection. If any unassigned neighbor has zero colors left, this branch is guaranteed to fail, 
            # so it returns None immediately.
            if len(new_domains[neighbor]) == 0:
                return None
    return new_domains

# 4. Improved Backtracking Algorithm
def improved_backtracking(assignment, domains, neighbors):
    if len(assignment) == len(domains):
        return assignment

    var = select_mrv(assignment, domains)

    for color in domains[var]:
        new_domains = forward_check(var, color, assignment, domains, neighbors) 
        #Attempts the assignment and prunes neighbor domains.
        if new_domains is None:
            continue  
        # forward checking caused a domain wipeout, skip this color immediately without recursing.

        assignment[var] = color
        result = improved_backtracking(assignment, new_domains, neighbors)
        #recurse passing down the newly pruned new_domains ; propagation to goal
        if result is not None:
            return result
        del assignment[var]  # Backtrack if subsequent recursive calls fail.

    return None

# Execution / Main



solution = improved_backtracking({}, domains, neighbors)
print("Solution:", solution)

