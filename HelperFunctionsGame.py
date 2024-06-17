
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
number_labels = np.array([str(i) for i in range(1, 11)])

def label_to_coord(label_val):
    if label_val[0] in letter_labels and label_val[1:] in number_labels:
        column = int(label_val[1:])  
        row = np.where(letter_labels == label_val[0])[0][0] + 1
        return row, column
    else:
        raise ValueError("Please enter a letter between A and J followed by a number between 1 and 10 (e.g. A1)")

def check_orientations(size, start_position):
    row, column = label_to_coord(start_position)
    possible_orientations = []

    orientations = {
        'up': list(range(row - size, row)),
        'down': list(range(row, row + size)),
        'left': list(range(column - size, column)),
        'right': list(range(column, column + size))
    }

    # Ensure orientations do not go off the board
    maximum_val, minimum_val = 10, 1
    for direction, indices in orientations.items():
        if all(minimum_val <= i <= maximum_val for i in indices):
            possible_orientations.append(direction)

    return possible_orientations

def multiple_choice(prompt: str, options: list) -> str:
    keys = list(string.ascii_uppercase)
    m_choice_opt = dict(zip(keys,options))
    print(prompt)
    for choice, content in m_choice_opt.items():
        print(f"{choice}: {content}")
    while True:
        try:  
            answer = input("Enter the letter of the choice you would like: ")
            return m_choice_opt[answer]
        except KeyError:
            print("Invalid choice. Please enter one of the displayed letters")
    
