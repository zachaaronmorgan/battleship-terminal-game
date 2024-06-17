# Imports 
import HelperFunctionsGame as HFG
import numpy as np
class Battleship_Board(): # sets up the battleship board so that each instance of the board has a certain size and is labeled appropriately 
    
    def __init__(self):
        self.board = np.full((11, 11), '   ')
        self.board[0, 1:] = np.array([f'{i}  ' if i < 10 else f'{i} ' for i in range(1, 11)])
        self.board[1:, 0] = HFG.letter_labels
        self.board[0, 0] = '' # for readability purposed the top left corner of the board is set to no space (does not impact functions)
    
    def __repr__(self): # every time the board is printed the following will print along with it to give whether it is currently in use
        return f"\n{np.array2string(self.board, separator=' ')}\nThis is an battleship board."

# Defines the types of ships available in the game
class Ship():
    def __init__(self, ship_type, size, status, s):
        self.ship_type = ship_type
        self.size = size
        self.status = status
        self.s = s
        self.health = size

    def __repr__(self):
        return f"The symbol for this ship is {self.s}" 

def create_ship(ship_type):
    ships = {
        'carrier': ('Carrier', 5, 'Functional', ' S '),
        'battleship': ('Battleship', 4, 'Functional', ' S '),
        'cruiser': ('Cruiser', 3, 'Functional', ' S '),
        'submarine': ('Submarine', 3, 'Functional', ' S '),
        'destroyer': ('Destroyer', 2, 'Functional', ' S ')
    }
    
    if ship_type.lower() in ships:
        
        return Ship(*ships[ship_type.lower()])
    
    raise ValueError("Unknown ship type")

class Player():
    def __init__(self, name, num_ships=5, ships=None):
        self.name = name 
        self.num_ships = num_ships
        self.ships = ships if ships is not None else {}
        self.friendly_board = Battleship_Board()
        self.target_board = Battleship_Board()
    
    def __repr__(self):
        return f"Your player name is {self.name}. You have a friendly board that displays your ships and ship placement and a target board that displays where you have struck on the enemies board. You currently have {self.num_ships} ships remaining. They are as follows: {self.ships}"
    
    def display_friendly_board(self):
        print("This is your friendly board: \n", self.friendly_board.board ,"\n")
    
    def display_target_board(self):
        print("This is your target board: \n", self.target_board.board ,"\n")
        
    def is_occupied(self, size, start_position, orientation):
        row, column = HFG.label_to_coord(start_position)
        if orientation.lower() == 'up':
            
            return any(self.friendly_board.board[row-i, column] != '   ' for i in range(size))
        
        elif orientation.lower() == 'down':
            
            return any(self.friendly_board.board[row+i, column] != '   ' for i in range(size))
        
        elif orientation.lower() == 'right':
            
            return any(self.friendly_board.board[row, column+i] != '   ' for i in range(size))
        
        elif orientation.lower() == 'left':
            return any(self.friendly_board.board[row, column-i] != '   ' for i in range(size))
    

    def place_ship(self, type_ship, start_position, orientation):
        positions = []
        ship = create_ship(type_ship)
        row, column = HFG.label_to_coord(start_position)
        
        if orientation.lower() == 'up':
            
            self.friendly_board.board[row-ship.size+1:row+1, column] = ship.s
            positions = [(row-i, column) for i in range(ship.size)]
            
        elif orientation.lower() == 'down':
            
            self.friendly_board.board[row:row+ship.size, column] = ship.s
            positions = [(row+i, column) for i in range(ship.size)]
            
        elif orientation.lower() == 'right':
            
            self.friendly_board.board[row, column:column+ship.size] = ship.s
            positions = [(row, column+i) for i in range(ship.size)]
            
        elif orientation.lower() == 'left':
            
            self.friendly_board.board[row, column-ship.size+1:column+1] = ship.s
            positions = [(row, column-i) for i in range(ship.size)]
            
        self.ships[ship] = positions

    
    def strike(self, enemy, location):
        row, column = HFG.label_to_coord(location)
        
        if enemy.friendly_board.board[row, column] == ' S ':
            enemy.friendly_board.board[row, column] = ' H '
            self.target_board.board[row, column] = ' H '
            print("Nice you hit a ship!")
            
        elif enemy.friendly_board.board[row, column] == '   ':
            enemy.friendly_board.board[row,column] = ' M '
            self.target_board.board[row, column] = ' M '
            print("Don't worry! You'll get em' next turn")
            
        elif enemy.friendly_board.board[row, column] in [' M ', ' H ']:
            print("You have already struck here. Please select a new location")

    def display_ships(self):
        for ship in self.ships.values():
            print(ship)
            
    def get_ship_coordinates(self):
        ship_coordinates = {1: [],2: [],3: [],4: [],5: []}
        for key, ship in zip(ship_coordinates.keys(), self.ships.values()):
            ship_coordinates[key] = ship
        return ship_coordinates
    
    def remove_ships(self):
        ship_coord = self.get_ship_coordinates()  # Retrieve ship coordinates
        for coordinates_list in ship_coord.values():  # Loop over each list in the dictionary values
            for coordinates in coordinates_list:  # Loop over each tuple in the list
                if isinstance(coordinates, tuple) and len(coordinates) == 2:
                    # Properly access the board using tuple indexing
                    self.friendly_board.board[coordinates] = '   '  # Reset the position to the original state
        self.ships = {}  # Reset the ships dictionary

    def check_all_ships_hit(self):
        all_hit = True
        for positions in self.ships.items():
            for position in positions:
                if self.friendly_board.board[position] != ' H ':
                    all_hit = False
                    break
            if not all_hit:
                break
        return all_hit