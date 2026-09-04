# 1. Problem Setup
N = 8
VARIABLES = list(range(N))  # Rows: 0 to N-1
COLUMNS = list(range(N))    # Columns: 0 to N-1
domains = {row: COLUMNS.copy() for row in VARIABLES}

# 2. MRV Heuristic (Identical to graph coloring)
def select_mrv(assignment, domains):
    unassigned = [row for row in domains if row not in assignment]
    return min(unassigned, key=lambda r: len(domains[r]))

# 3. Forward Checking: Prune same column and diagonals from other rows
def forward_check(row, col, assignment, domains):
    new_domains = {r: list(cols) for r, cols in domains.items()}
    new_domains[row] = [col]

    for other_row in domains:
        if other_row not in assignment and other_row != row:
            diff = abs(other_row - row)
            # Attack positions: same column, diagonal left, diagonal right
            attacked = {col, col - diff, col + diff}

            # Remove attacked columns from other_row's domain
            new_domains[other_row] = [c for c in new_domains[other_row] if c not in attacked]

            # Domain Wipeout: early failure detected
            if len(new_domains[other_row]) == 0:
                return None
    return new_domains

# 4. Improved Backtracking Algorithm (Exact same structure)
def improved_backtracking(assignment, domains):
    if len(assignment) == len(domains):
        return assignment

    row = select_mrv(assignment, domains)

    for col in domains[row]:
        new_domains = forward_check(row, col, assignment, domains)
        if new_domains is None:
            continue  # Prune branch

        assignment[row] = col
        result = improved_backtracking(assignment, new_domains)
        if result is not None:
            return result
        del assignment[row]  # Backtrack

    return None

# Execution
solution = improved_backtracking({}, domains)
print("Solution (row: col):", solution)