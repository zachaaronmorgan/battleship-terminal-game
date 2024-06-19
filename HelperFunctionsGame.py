
# Imports to aid in helper functions
import string
import numpy as np
import os

# run when you want the terminal to be clean for readability (multiplatform)
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# sets up number and letter labels for board where the letters represent each row and the numbers the columns
letter_labels = np.array(list(string.ascii_uppercase[:10])) 
number_labels = np.array([str(i) for i in range(1, 11)])


def label_to_coord(label_val):
    if label_val[0] in letter_labels and label_val[1:] in number_labels: # Separates the given input into letter which is the first index and the number which is the second index onward and checks to see if the values exist in the label arrays
        # Column and row set the coordinates on the board based on the given value
        column = int(label_val[1:])  
        row = np.where(letter_labels == label_val[0])[0][0] + 1
        return row, column
    else:
        raise ValueError("Please enter a letter between A and J followed by a number between 1 and 10 (e.g. A1)") # if the input is not found in the lists then this will raise a value error 

def check_orientations(size, start_position): # function outputs the possible orientations for a given ship size and starting position
    row, column = label_to_coord(start_position) # uses earlier function to convert coordinates into usable index elements
    possible_orientations = [] # empty list to store the possible orientations
    
    # dictionary containing the different orientations as the keys and values are the list of coordinates for the given orientation 
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

# sets up function to take in a list of options and assign them to letter keys and then create a question based on this so the keys could be used to select certain option
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
    
