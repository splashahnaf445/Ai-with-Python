COLORS = ['Red','Green','Blue']
EDGES = [
    ('WA','NT'),('WA','SA'),('NT','Q'),('SA','NT'),('SA','NSW'),('Q','NSW'),('Q','SA'),('NSW','V'),('SA','V')
]

VARIABLES = sorted(set(v for edge in EDGES for v in edge))
VARIABLES.append('T')

DOMAINS = {v:COLORS.copy() for v in VARIABLES}

neighbors = {v:set() for v in VARIABLES}
for x,y in EDGES:
    neighbors[x].add(y)
    neighbors[y].add(x)

def MRV(assignment,domains):
    unassigned = [v for v in domains if v not in assignment]
    return min(unassigned, key=lambda v: len(domains[v]))

def forward_check(var,color,assignment,domains,neighbors):
    new_domains = {v: list(vals) for v,vals in domains.items()}
    new_domains[var]=[color]
    for neighbor in neighbors[var]:
        if neighbor not in assignment:
            if color in new_domains[neighbor]:
                new_domains[neighbor].remove(color)
            if len(new_domains[neighbor])==0:
                return None
    return new_domains

def improvedCSP(assignment,domains,neighbor):
    if len(assignment)==len(domains):
        return assignment
    var = MRV(assignment,domains)

    for color in domains[var]:
        new_domain = forward_check(var,color,assignment,domains,neighbor)
        if new_domain is None:
            continue
        assignment[var]=color
        result=improvedCSP(assignment,new_domain,neighbor)
        if result is not None:
            return result
        del assignment[var]

    return None

solution = improvedCSP({},DOMAINS,neighbors)
print(f'The solution is : {solution}')