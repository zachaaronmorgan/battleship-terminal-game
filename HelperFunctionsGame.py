# Imports to aid in helper functions
import string
import numpy as np
import os
import inquirer

from rich.console import Console
from rich.panel import Panel
from rich.text import Text

def greet():
    console = Console()

    title = Text()
    title.append("BATTLEGRID", style="bold blue")
    title.append(" — Terminal Edition", style="blue")

    CELL_WIDTH = 6  # wider than original 4


    # Build the number header line
    number_line = " " * 2 + "".join(f"{i:^{CELL_WIDTH}}" for i in range(1, 11))




    # Grid borders
    top_border = " ┌" + ("─" * (CELL_WIDTH - 1) + "┬") * 9 + "─" * (CELL_WIDTH - 1) + "┐"
    mid_border = " ├" + ("─" * (CELL_WIDTH - 1) + "┼") * 9 + "─" * (CELL_WIDTH - 1) + "┤"
    bottom_border = " └" + ("─" * (CELL_WIDTH - 1) + "┴") * 9 + "─" * (CELL_WIDTH - 1) + "┘"


    # Build the lettered rows with separating lines
    rows = ""
    for index, letter in enumerate("ABCDEFGHIJ"):
        rows += f"{letter}│" + (" " * (CELL_WIDTH - 1) + "│") * 10 + "\n"
        if index < 9:
            rows += mid_border + "\n"


    grid = f"{number_line}\n{top_border}\n{rows}{bottom_border}"
    console.print(Panel(grid, title=title, border_style="blue", padding=0, width=len(max(grid.splitlines(), key=len)) + 2))






# run when you want the terminal to be clean for readability (multiplatform)
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')



# sets up number and letter labels for board where the letters represent each row and the numbers the columns
letter_labels = np.array(list(string.ascii_uppercase[:10])) 
number_labels = np.array([str(i) for i in range(1, 11)])


def label_to_coord(label_val):
    # Column and row set the coordinates on the board based on the given value
    column = int(label_val[1:])  
    row = np.where(letter_labels == label_val[0])[0][0] + 1
    return row, column

def check_orientations(size, row, column): # function outputs the possible orientations for a given ship size and starting position 
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

def get_strike_position():
    position = input("Enter the location you would like to strike: ")
    if not position:
        return get_strike_position()
    
    if (position[0] in letter_labels and position[1:] in number_labels):
        return label_to_coord(position)
    else:
        return get_strike_position()

def get_place_position():
    position = input("Enter the location you would like to place your ship: ")
    if not position:
        return get_place_position()
    
    if (position[0] in letter_labels and position[1:] in number_labels):
        return label_to_coord(position)
    else:
        print("Invalid selection. Please enter a value starting with a letter between A and J followed by a number between 1 and 10 like A1 or H6")
        return get_place_position()

def get_ship_choice(ship_lst=['Carrier','Battleship','Cruiser','Submarine','Destroyer']):
    # ship_lst = ['carrier','battleship','cruiser','submarine','destroyer']
    ship_question = [inquirer.List('ship', message="Choose a ship", choices=ship_lst)]
    chosen_ship = inquirer.prompt(ship_question)
    return chosen_ship['ship']

def get_ship_orientation(orientation_lst):
    # orientation_lst = ['up','down','right','left']
    ship_question = [inquirer.List('orientation', message="Choose the orientation for your ship", choices=orientation_lst)]
    chosen_ship = inquirer.prompt(ship_question)
    return chosen_ship['orientation']

def get_user_input(message):
    answer = input(f"{message} (y/n) ")
    if not answer:
        return get_user_input(message)
    
    if answer.strip().lower() not in ['y', 'n']:
        return get_user_input(message)
    else:
        return answer.strip().lower()
