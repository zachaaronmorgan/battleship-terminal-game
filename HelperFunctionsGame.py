
# Helper Variables/Functions
import string
import numpy as np

letter_labels_orig = np.array(list(string.ascii_uppercase[:10])) 
letter_labels = np.array([' ' + letter + ' ' for letter in letter_labels_orig])
letter_labels_indices = [n for n in letter_labels_orig]
number_labels = np.array(range(1, 11))  

def label_to_coord(label_val):
    row = int(label_val[1:])
    column = letter_labels_indices.index(label_val[0])+1
    return row, column

def check_orientations(size, start_position):
    possible_orientations = []
    orientations = ['up', 'down', 'right', 'left']
    row, column = label_to_coord(start_position)
    maximum_val, minimum_val = 10, 1
    for orientation in orientations:
        if orientation == 'up':
            if row - size >= minimum_val:
                possible_orientations.append(orientation)
            else:
                continue 
        elif orientation == 'down':
            if row + size <= maximum_val:
                possible_orientations.append(orientation)
            else:
                continue
        elif orientation == 'right':
            if column + size <= maximum_val:
                possible_orientations.append(orientation)
            else:
                continue
        elif orientation == 'left':
            if column - size >= minimum_val:
                possible_orientations.append(orientation)
            else:
                continue
    return possible_orientations