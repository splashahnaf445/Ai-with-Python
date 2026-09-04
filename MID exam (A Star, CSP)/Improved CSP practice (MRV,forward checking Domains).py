COLORS = ["Red", "Green", "Blue", "Yellow"]

EDGES = [
    ("A", "B"), ("A", "C"), ("A", "D"), ("B", "C"), ("B", "E"), ("B", "F"),
    ("C", "D"), ("C", "E"), ("C", "F"), ("D", "E"), ("D", "G"), ("E", "F"),
    ("E", "G"), ("E", "H"), ("F", "G"), ("F", "H"), ("G", "H"),
]

VARIABLES = sorted(set(v for edge in EDGES for v in edge))
print(f"The Variables are :     {VARIABLES}")

neighbor = {v: set() for v in VARIABLES}
for x,y in EDGES:
    neighbor[x].add(y)
    neighbor[y].add(x)

domain= {v:COLORS.copy() for v in VARIABLES}

def MRV(assignment,domains):
    unassigned = [v for v in domains if v not in assignment]
    return min(unassigned, key=lambda v:len(domains[v]))


def forwardCheck(var, color, assignment, domains, neighbors):
    new_domains = {v: list(vals) for v, vals in domains.items()}
    new_domains[var] = [color]
    for neighbor in neighbors[var]: 
            if neighbor not in assignment:   #Only prunes variables that have not yet been assigned.
                if color in new_domains[neighbor]:   
                    new_domains[neighbor].remove(color)  #Deletes the chosen color from the neighbor's options since adjacent regions cannot share it.
                # Early Failure Detection. If any unassigned neighbor has zero colors left, this branch is guaranteed to fail, 
                # so it returns None immediately.
                if len(new_domains[neighbor]) == 0:
                    return None
    return new_domains


def improvedCSP(assignment,domains,neighbors):
    if len(assignment) == len(domains):
        return assignment
    var = MRV(assignment,domains)

    for color in domains[var]:
        newDomains = forwardCheck(var,color,assignment,domains,neighbors)
        if newDomains is None:
            continue
        assignment[var]=color
        result = improvedCSP(assignment,newDomains,neighbors)
        if result is not None:
            return result
        del assignment[var]

    return None
    


solution = improvedCSP({},domain,neighbor)
print(solution)