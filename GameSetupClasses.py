# Imports 
from HelperFunctionsGame import *
import numpy as np
from rich import print as rprint

class Battleship_Board(): # sets up the battleship board so that each instance of the board has a certain size and is labeled appropriately 
    
    def __init__(self):
        self.board = np.full((11, 11), '   ')
        self.board[0, 1:] = np.array([f'  {i} ' if i < 10 else f'{i}  ' for i in range(1, 11)])
        self.board[1:, 0] = letter_labels
        self.board[0, 0] = '' # for readability purposed the top left corner of the board is set to no space (does not impact functions)
    
    def __repr__(self): # every time the board is printed the following will print along with it to give whether it is currently in use
        return f"\n{np.array2string(self.board, separator=' ')}\nThis is an battleship board."
    

    def display_board(self):
        for row in range(self.board.shape[0]):
            for col in range(self.board.shape[1]):
                symbol = self.board[row, col]
                if symbol in [' A ', ' B ', ' C ', ' S ', ' D ']:
                    rprint(f'[grey] {symbol} [/grey]', end=' ')
                elif row == 0 and col > 0:
                    rprint(f" [green]{symbol}[/green] ", end=' ')
                elif col == 0 and row > 0:
                    rprint(f" [green]{symbol}[/green] ", end=' ')
                elif symbol == ' X ':
                    rprint(f'[red] {symbol} [/red]', end=' ')
                elif symbol == ' O ':
                    rprint(f'[blue] {symbol} [/blue]',end='')
                else:
                    rprint(f' {symbol} ', end=' ')
            rprint("")
            
# Defines the types of ships available in the game
class Ship():
    def __init__(self, ship_type, size, status, s):
        self.ship_type = ship_type
        self.size = size
        self.status = status
        self.s = s
        self.health = size

    def __repr__(self):
        return f"The symbol for this ship is {self.s} and it has a maximum health of {self.size}" 

def create_ship(ship_type):
    ships = {
        'carrier': ('Carrier', 5, 'Functional', ' A '),
        'battleship': ('Battleship', 4, 'Functional', ' B '),
        'cruiser': ('Cruiser', 3, 'Functional', ' C '),
        'submarine': ('Submarine', 3, 'Functional', ' S '),
        'destroyer': ('Destroyer', 2, 'Functional', ' D ')
    }
    
    return Ship(*ships[ship_type.lower()])


class Player():
    def __init__(self, name, num_ships=5, ships=None, ships_destroyed=None):
        self.name = name 
        self.num_ships = num_ships
        self.ships = ships if ships is not None else {}
        self.ships_destroyed = ships_destroyed if ships_destroyed is not None else []
        self.friendly_board = Battleship_Board()
        self.target_board = Battleship_Board()
    
    def __repr__(self):
        return f"Your player name is {self.name}. You have a friendly board that displays your ships and ship placement and a target board that displays where you have struck on the enemies board. You currently have {self.num_ships} ships remaining. They are as follows: {self.ships}"
    
    def display_friendly_board(self):
        self.friendly_board.display_board()
    
    def display_target_board(self):
        self.target_board.display_board()
        
    def spot_occupied(self, size, row, column, orientation):
        
        if orientation.lower() == 'up':
            
            return any(self.friendly_board.board[row-i, column] != '   ' for i in range(size))
        
        elif orientation.lower() == 'down':
            
            return any(self.friendly_board.board[row+i, column] != '   ' for i in range(size))
        
        elif orientation.lower() == 'right':
            
            return any(self.friendly_board.board[row, column+i] != '   ' for i in range(size))
        
        elif orientation.lower() == 'left':
            
            return any(self.friendly_board.board[row, column-i] != '   ' for i in range(size))
    

    def place_ship(self, ship, row, column, orientation):
        positions = []
        
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
            
        self.ships[ship.ship_type] = positions

    
    def strike(self, enemy, row, column):
        ship_symbols = [' A ', ' B ', ' C ', ' S ', ' D ']
        if enemy.friendly_board.board[row, column] in ship_symbols:
            enemy.friendly_board.board[row, column] = ' X '
            self.target_board.board[row, column] = ' X '
            print("\nNice you hit a ship!")
            
        elif enemy.friendly_board.board[row, column] == '   ':
            enemy.friendly_board.board[row,column] = ' O '
            self.target_board.board[row, column] = ' O '
            print("\nDon't worry! You'll get em' next turn")

        else:
            print("\nYou have already struck there. Please pick a new location to strike.")
            new_row, new_column = get_strike_position()
            return self.strike(enemy,new_row,new_column)


    def display_ships(self):
        for ship_type, ship_coordinates in self.ships.items():
            print(f"{ship_type}: {ship_coordinates}")
            
    def get_ship_coordinates(self, ship_type):
        return self.ships[ship_type]
    
    def get_all_ships_coord(self):
        return self.ships.values()
    
    def remove_ship(self, ship_type):
        ship_coord_l = self.get_ship_coordinates(ship_type)  # Retrieve ship coordinates
        for r, c in ship_coord_l:  # Loop over each list in the dictionary values
            self.friendly_board.board[r,c] = '   '  # Reset the position to the original state
        self.ships[ship_type] = None  # Reset the the specific value for that ship type 

    def remove_all_ships(self):
        ship_coord = self.ships.values()
        for coord in ship_coord:
            for r, c in coord:
                self.friendly_board.board[r,c] = '   '
        self.ships = {}
    
    def ship_destroyed(self, ship_type):            #Refers to whoever's ship it is 
        ship_coord_l = self.get_ship_coordinates(ship_type)
        spots_hit = []
        for r, c in ship_coord_l:
            if self.friendly_board.board[r,c] == ' X ':
                spots_hit.append((r,c))
            else:
                pass
            
        return len(spots_hit) == len(ship_coord_l)
    
    def all_ships_destroyed(self, enemy):
        destroyed_ships = []
        for ship in self.ships.keys():
            if self.ship_destroyed(ship):
                if ship not in destroyed_ships:
                    destroyed_ships.append(ship)
                else:
                    pass
            else:
                pass
        enemy.ships_destroyed = destroyed_ships
        
        return len(destroyed_ships) == len(self.ships)


    def display_ships_destroyed(self):
        print(f"{self.name} you have destroyed the following enemy ships: {self.ships_destroyed}")
        
    
def get_player_names():
    player_1 = input("\nEnter player 1's name: ")
    player_2 = input("\nEnter player 2's name: ")
    return [Player(player_1), Player(player_2)]

def ship_placement(new_ship, player):
    row, column = get_place_position()
    orientations_lst = check_orientations(new_ship.size,row,column)
    chosen_orientation = get_ship_orientation(orientations_lst)
    
    if player.spot_occupied(new_ship.size,row,column,chosen_orientation):
        print("I am sorry, but this spot is already occupied by another ship. Please choose a new position and orientation to continue.")
        return ship_placement(new_ship,player)
    
    else:
        print("Ship is good to go")
        player.place_ship(new_ship,row,column,chosen_orientation)

def reset_board(player):
    reset_board_choice = get_user_input("Would you like to reset your board? ")
    
    if reset_board_choice == 'y':
        print("Resetting your board...")
        player.remove_all_ships()
        ship_lst = ['carrier','battleship','cruiser','submarine','destroyer']
    
        while len(ship_lst) > 0:
            
            ship_choice = get_ship_choice(ship_lst)
            ship_lst.remove(ship_choice)
            new_ship = create_ship(ship_choice)
            
            ship_placement(new_ship,player)
            
        player.display_friendly_board()
        return reset_board(player)
    
    else:
        return

def reset_ship(player):
    reset_ship_choice = get_user_input("Would you like to reset one ship on your board? ")
    
    if reset_ship_choice == 'y':
        ship_choice = get_ship_choice()
        player.remove_ship(ship_choice)
        new_ship = create_ship(ship_choice)
        ship_placement(new_ship,player)
            
        player.display_friendly_board()
        return reset_ship(player)
    else:
        return
            