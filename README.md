# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: 
First of all, I traversed each box and its peers unit to find if there are any other boxes in the same unit with the same value. If so, traversed peers other than this pair of boxes and find if values of their peers in the same unit included the values of the box pair. Then eliminated values of the box pair from other peers if they have any of them. 

Typically, a pair of boxes with the same value is in one or two different units. For the occasion of one unit, they might be in the same row or column or diagonal unit. For the occasion of two units, they might be in the same row or diagonal or column unit plus square unit. The function goes through each box in the same unit as the box pair is in. 

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: Compared to traditional sudoku problem without diagonal condition, I only add diagonal unit into the unit list.

It firstly replaces blank with string "123456789" and converts it into a dictionary with grid_value function. Then it eliminates those values which have already been determined for undetermined boxes with eliminate function. Then it continue to go through each box, determining boxes which have only one choice with one_choice function. Boxes undetermined are compared to their peers in the row, column, square and diagonal if there is any, respectively, to decide if they qualify the one choice requirements. Lastly, a box with the smallest string is picked and its values are tried through depth first search with search function. 


### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solutions.py` - This file was modified. 
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in solution.py

### Data

The data consists of a text file of diagonal sudokus for you to solve.
