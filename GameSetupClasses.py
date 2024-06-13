# Imports 
import HelperFunctionsGame as HFG
import numpy as np

class Battleship_Board():
    def __init__(self, state):
        self.state = state
        self.board = np.full((11, 11), '   ')
        self.board[0, 1:] = HFG.letter_labels
        self.board[1:, 0] = np.array([f'{i} ' if i < 10 else f'{i}' for i in range(1, 11)])
        self.board[0, 0] = '  '
    
    def __repr__(self):
        return f"\n{np.array2string(self.board, separator=' ')}\nThis is an {self.state} battleship board."
    
class Friendly_Board(Battleship_Board):
    pass

class Target_Board(Battleship_Board):
    pass

# Defines the types of ships available in the game
class Ship():
    def __init__(self, ship_type, size, status, s='S'):
        self.ship_type = ship_type
        self.size = size
        self.status = status
        self.s = s
        self.health = size

    def __repr__(self):
        return f"This is a {self.ship_type} with a size of {self.size}. The current status of this ship is {self.status}. The symbol for this ship is {self.s}" 
        

class Carrier(Ship):
    def __init__(self, status):
        super().__init__(ship_type='Carrier', size=5, status=status)
        
class Battleship(Ship):
    def __init__(self, status):
        super().__init__(ship_type='Battleship', size=4, status=status)

class Cruiser(Ship):
    def __init__(self, status):
        super().__init__(ship_type='Cruiser', size=3, status=status)
        
class Submarine(Ship):
    def __init__(self, status):
        super().__init__(ship_type='Submarine', size=3, status=status)

class Destroyer(Ship):
    def __init__(self, status):
        super().__init__(ship_type='Destroyer', size=2, status=status)

def create_ship(ship_type):
    ships = {
        'carrier': ('Carrier', 5, 'Functional', ' S '),
        'battleship': ('Battleship', 4, 'Functional', ' S '),
        'cruiser': ('Cruiser', 3, 'Functional', 'S'),
        'submarine': ('Submarine', 3, 'Functional', ' S '),
        'destroyer': ('Destroyer', 2, 'Functional', ' S ')
    }
    if ship_type.lower() in ships:
        return Ship(*ships[ship_type.lower()])
    raise ValueError("Unknown ship type")

class Player():
    def __init__(self, name, num_ships=5):
        self.name = name 
        self.num_ships = num_ships
        self.friendly_board = Friendly_Board('Active')
        self.target_board = Target_Board('Active')
    
    def __repr__(self):
        return f"This player's name is {self.name}. They have an {self.friendly_board.state} friendly board and an {self.target_board.state} target board. They currently have {self.num_ships} ships remaining"
    
    def display_friendly_board(self):
        print(self.friendly_board.board)
    
    def display_target_board(self):
        print(self.target_board.board)
    
    def ship_to_board(self, ship_type, start_position, orientation):
        new_ship = create_ship(ship_type)
        row, column = HFG.label_to_coord(start_position)
        if orientation.lower() == 'up':
            self.friendly_board.board[row-new_ship.size+1:row+1, column] = new_ship.s
        elif orientation.lower() == 'down':
            self.friendly_board.board[row:row+new_ship.size, column] = new_ship.s
        elif orientation.lower() == 'right':
            self.friendly_board.board[row, column:column+new_ship.size] = new_ship.s
        elif orientation.lower() == 'left':
            self.friendly_board.board[row, column-new_ship.size+1:column+1] = new_ship.s
    
    def strike(self, enemy, location):
        row, column = HFG.label_to_coord(location)
        
        if enemy.friendly_board.board[row, column] == ' S ':
            enemy.friendly_board.board[row, column] = ' H '
            self.target_board.board[row, column] = ' H '
            
        elif enemy.friendly_board.board[row, column] == '   ':
            enemy.friendly_board.board[row,column] = ' M '
            self.target_board.board[row, column] = ' M '
            
        elif enemy.friendly_board.board[row, column] in [' M ', ' H ']:
            print("You have already struck here. Please select a new location")
        
        
            
        

