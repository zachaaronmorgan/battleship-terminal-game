
# Helper Variables/Functions
import string
import numpy as np
import os
import platform

def clear_screen():
    if os.name == 'nt':
        
        if 'MINGW' in platform.system() or 'CYGWIN' in platform.system():
            os.system('clear')  
        else:
            os.system('cls')  
    else:
        os.system('clear')  


letter_labels = np.array(list(string.ascii_uppercase[:10])) 
letter_labels_indices = [n for n in letter_labels]
number_labels = np.array(range(1, 11))  

def label_to_coord(label_val):
    column = int(label_val[1:])
    row = letter_labels_indices.index(label_val[0])+1
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
            if min(orientation[1]) >= minimum_val and max(orientation[1]) <= maximum_val:
                possible_orientations.append(orientation[0])
            else:
                continue
    else:
        raise ValueError("Please enter a valid position on the board for your ship")
    
    return possible_orientations

def multiple_choice(prompt: str, options: list) -> str:
    keys = list(string.ascii_uppercase)
    m_choice_opt = dict(zip(keys,options))
    print(prompt)
    for choice, content in m_choice_opt.items():
        print(f"{choice}: {content}")
    answer = input("Enter the letter of the choice you would like: ")
    return m_choice_opt[answer]
