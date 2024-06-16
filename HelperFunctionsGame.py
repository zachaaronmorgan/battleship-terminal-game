
# Helper Variables/Functions
import string
import numpy as np

letter_labels = np.array(list(string.ascii_uppercase[:10])) 
letter_labels_indices = [n for n in letter_labels]
number_labels = np.array(range(1, 11))  

def label_to_coord(label_val):
    row = int(label_val[1:])
    column = letter_labels_indices.index(label_val[0])+1
    return row, column

def check_orientations(size, start_position):
    row, column = label_to_coord(start_position)
    possible_orientations = []
    # Method 1
    if start_position[0] in letter_labels and column in number_labels:
        orientations = {
            'up': list(range(row, row-size, -1)),
            'down': list(range(row,row+size)),
            'left': list(range(column,column-size,-1)),
            'right': list(range(column,column+size))
        }
        maximum_val, minimum_val = 10, 1
        for orientation in orientations.items():
            if min(orientations[orientation]) >= minimum_val and max(orientations[orientation]) <= maximum_val:
                possible_orientations.append(orientation)
            else:
                continue
    else:
        raise ValueError("Please enter a valid position on the board for your ship")
    
    return possible_orientations


