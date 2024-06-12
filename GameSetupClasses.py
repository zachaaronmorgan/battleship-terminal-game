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
            if row - size <= maximum_val:
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

class Battleship_Board():

    board = np.full((11, 11), ' ')

    board[0, 1:] = letter_labels

    board[1:, 0] = number_labels

    board[0, 0] = ' '
    
    def __init__(self, state):
        self.state = state
    
    def __repr__(self):
        return f"This is an {self.state} battleship board"
    
class Friendly_Board(Battleship_Board):
    def __init__(self, state):
        super().__init__(state)

class Target_Board(Battleship_Board):
    def __init__(self, state):
        super().__init__(state)

# Defines the types of ships available in the game
class Ship():
    def __init__(self, ship_type, health, status):
        self.ship_type = ship_type
        self.health = health
        self.status = status

    def __repr__(self):
        return f"This is a {self.ship_type} with {self.health} hits remaining. The current status of this ship is {self.status}" 
        

class Carrier(Ship):
    def __init__(self, status):
        super().__init__(ship_type='Carrier', health=5, status=status)
        
class Battleship(Ship):
    def __init__(self, location, status):
        super().__init__(ship_type='Battleship', health=4, status=status)

class Cruiser(Ship):
    def __init__(self, location, status):
        super().__init__(ship_type='Cruiser', health=3, status=status)
        
class Submarine(Ship):
    def __init__(self, location, status):
        super().__init__(ship_type='Submarine', health=3, status=status)

class Destroyer(Ship):
    def __init__(self, location, status):
        super().__init__(ship_type='Destroyer', health=2, status=status)

def create_ship(ship_type):
    if ship_type.lower() == 'carrier':
        return Carrier('Functional')
    elif ship_type.lower() == 'battleship':
        return Battleship('Functional')
    elif ship_type.lower() == 'battleship':
        return Cruiser('Functional')
    elif ship_type.lower() == 'battleship':
        return Submarine('Functional')
    else:
        return Destroyer('Functional')
class Player():
    def __init__(self, name, num_ships=5):
        self.name = name 
        self.num_ships = num_ships
        self.friendly_board = Friendly_Board('Active')
        self.target_board = Target_Board('Active')
    
    def __repr__(self):
        return f"This player's name is {self.name}. They have an {self.friendly_board.state} friendly board and an {self.target_board.state} target board. They currently have {self.num_ships} ships remaining"
    
#     def ship_to_board(self, ship_type, start_position, orientation):
        

# player_1 = Player('Zach')
# print(player_1.ship_to_board('Carrier'))
