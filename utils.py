
rows = 'ABCDEFGHI'
cols = '123456789'

def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [i+j for i in A for j in B]

boxes = cross(rows, cols)

row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
#diagonal units added here
diagonal_units = [[r+c for r,c in zip(rows,cols)], [r+c for r,c in zip(rows,cols[::-1])]]
unitlist = row_units + column_units + square_units + diagonal_units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)
