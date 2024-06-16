import GameSetupClasses as GSP
from HelperFunctionsGame import multiple_choice, check_orientations, clear_screen
# user_name_1 = input("Hello welcome to my Battleship Terminal Game, to start please enter Player 1 name: ")
# user_name_2 = input("Hello welcome to my Battleship Terminal Game, to start please enter Player 2 name: ")

player_1 = GSP.Player('Zach')
player_2 = GSP.Player('John')
ships = ['Carrier', 'Battleship', 'Cruiser', 'Submarine', 'Destroyer']
players = [player_1]
for player in players:
    while True:
        ships_available = ships.copy()
        clear_screen()
        for ship in ships:
            ship_choice = multiple_choice("Which ship would you like to place: ", ships_available)
            ships_available.remove(ship_choice)
            new_ship = GSP.create_ship(ship_choice)
            start_position = input("Which position on the board would you like to place it: ")
            orientations = check_orientations(new_ship.size, start_position)
            chosen_orientation = multiple_choice("In which orientation would you like to place the ship: ", orientations)
            while player_1.is_occupied(new_ship.size,start_position,chosen_orientation):
                print("This spot is occupied by another ship. Please choose a different location")
                start_position = input("Which position on the board would you like to place it: ")
                orientations = check_orientations(new_ship.size, start_position)
                chosen_orientation = multiple_choice("In which orientation would you like to place the ship: ", orientations)
                
            player.place_ship(ship_choice, start_position, chosen_orientation)
            player.display_friendly_board()
        start_over = input("Would you like to restart the ship placing process (y/n): ").strip().lower()
        if start_over == 'y':
            player.remove_ships()
            continue
        else:
            break
        

# player_1.place_ship('carrier', 'E6', 'right')
# player_1.place_ship('destroyer', 'J3', 'right')
# player_1.place_ship('submarine', 'A2', 'down')
# player_1.place_ship('battleship', 'H5', 'right')
# player_1.place_ship('cruiser', 'A9', 'up')
# player_1.display_friendly_board()
# # ship_coord = player_1.get_ship_coordinates()
# # print(ship_coord)
# player_1.remove_ships()

# player_1.display_friendly_board()
# # player_2.ship_to_board('destroyer', 'E6', 'right')
# # player_2.ship_to_board('carrier', 'B6', 'up')
# # player_1.strike(player_2, 'D5')
# # player_2.display_friendly_board()
# # player_1.display_target_board()

# print(player_2.ships)

# Loop to run once game has started
is_running = True
while is_running:
    
    # Player 1 places their ships on their friendly board 
    
    # Player 2 places their ships on their friendly board
    
    is_running = False

