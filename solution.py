from utils import *

assignments = []

def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """

    # Find all instances of naked twins
    naked_pair = []
    for box in boxes:
        if len(values[box]) == 2:
            for i, unit in enumerate(unitlist): #record the index of unit
                if box in unit:
                    for item in unit:
                        if values[box] == values[item] and box != item: #find the pair
                            a = (box,item, i)
                            naked_pair.append(a) #record the pair and their unit
    # Eliminate the naked twins as possibilities for their peers
    for u, v, num in naked_pair:
        for char in values[u]:
            for item in unitlist[num]:
                if item != u and item != v: # peers should not be the pair itself
                    values[item] = values[item].replace(char, "")
        
    
    #for box in boxes: #traverse each box
        #if len(values[box]) == 2: #only focus on those boxes with 2 digit
            #for unit in unitlist:
                #if box in unit: #see peers of the current box traversed
                    #for item in unit:
                        #if values[box] == values[item] and box != item: #compare peers to the current box
                            #for box2 in unit: #if the pair with same value has been found, traverse peers again
                                #if box2 != box and box2!= item:
                                    #for char in values[box]: # Eliminate the naked twins as possibilities for their peers
                                        #if char in values[box2]:
                                            #values[box2] = values[box2].replace(char, "")
    
    return values
                
                
    
        

def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    values = []
    for item in grid:
        if item == '.':
            values.append("123456789")
        else:
            values.append(item)
    
    assert len(values) == 81
    return dict(zip(boxes, values))

def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return

def eliminate(values):
    """Eliminate values from peers of each box with a single value.
    Go through all the boxes, and whenever there is a box with a single value,
    eliminate this value from the set of values of all its peers.
    Args:
        values: Sudoku in dictionary form.
    Returns:
        Resulting Sudoku in dictionary form after eliminating values.
    """
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    for box in solved_values:
        v = values[box]
        for peer in peers[box]:
            values[peer] = values[peer].replace(v,"")
    return values

def only_choice(values):
    """
    Finalize all values that are the only choice for a unit.
    Go through all the units, and whenever there is a unit with a value
    that only fits in one box, assign the value to this box.
    Input: Sudoku in dictionary form.
    Output: Resulting Sudoku in dictionary form after filling in only choices.
    """
    for box in units.keys():
        if len(values[box]) == 1:
            continue
        else:
            for num in values[box]:
                valid_list = []
                for peer in peers[box]:
                    if num in values[peer] and len(values[peer]) == 1:
                        values[box] = values[box].replace(num,"")
    return values

def reduce_puzzle(values):
    """
    Iterate eliminate() and only_choice(). If at some point, there is a box with no available values, return False.
    If the sudoku is solved, return the sudoku.
    If after an iteration of both functions, the sudoku remains the same, return the sudoku.
    Input: A sudoku in dictionary form.
    Output: The resulting sudoku in dictionary form.
    """

    stalled = False
    while not stalled:
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
        values = eliminate(values)
        values = only_choice(values)
        values = naked_twins(values)
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        stalled = solved_values_before == solved_values_after
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values

def search(values):
    "Using depth-first search and propagation, create a search tree and solve the sudoku."
    # First, reduce the puzzle using the previous function
    values = reduce_puzzle(values)
    if values is False:
        return False ## Failed earlier

    if all(len(values[s]) == 1 for s in boxes): 
        return values
    # Choose one of the unfilled squares with the fewest possibilities
    length_min = 9
    key_min = ""
    for item in boxes:
        length = len(values[item])
        if length < length_min and length > 1:
            length_min = length
            key_min = item
    #length_min,key_min = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
            
    # Now use recursion to solve each one of the resulting sudokus, and if one returns a value (not False), return that answer!
    for value in values[key_min]:
        value_copy = values.copy()
        value_copy[key_min] = value
        success = search(value_copy)
        if success:
            return success

def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    table1 = grid_values(grid)
    table2 = reduce_puzzle(table1)
    table3 = search(table2)

    return table3
    

if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
