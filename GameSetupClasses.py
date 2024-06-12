# Imports 
import string
import numpy as np

# Helper Variables/Functions
letter_labels = np.array(list(string.ascii_uppercase[:10])) 
letter_labels_indices = [n for n in letter_labels]
number_labels = np.array(range(1, 11))  

def label_to_coord(label_val):
    row = int(label_val[1])
    column = letter_labels_indices.index(label_val[0])+1
    return row, column

def check_orientations(ship_type, start_position):
    possible_orientations = []
    

class Battleship_Board():

    board = np.full((11, 11), ' ')

    board[0, 1:] = letter_labels

    board[1:, 0] = number_labels

    board[0, 0] = ' '
    
    def __init__(self, state):
        self.state = state
    
    def __repr__(self):
        return "This is a battleship board"

# Defines the types of ships available in the game
class Ship():
    def __init__(self, ship_type, health, location, is_active):
        self.ship_type = ship_type


label_val = 'B5'
print(label_to_coord(label_val))