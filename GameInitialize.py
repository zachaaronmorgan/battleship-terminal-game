import GameSetupClasses as GSP
from HelperFunctionsGame import multiple_choice, check_orientations, clear_screen, label_to_coord
user_name_1 = input("Hello welcome to my Battleship Terminal Game, to start please enter Player 1 name: ")
user_name_2 = input("Hello welcome to my Battleship Terminal Game, to start please enter Player 2 name: ")

# Creates two players (player 1 and 2) each with their own
player_1 = GSP.Player(user_name_1)
player_2 = GSP.Player(user_name_2)

ships = ['Carrier', 'Battleship', 'Cruiser', 'Submarine', 'Destroyer']
players = [player_1, player_2]
for player in players:
    while True:
        ships_available = ships.copy()
        clear_screen()
        
        for ship in ships:
            ship_choice = multiple_choice(f"Which ship would you like to place {player.name}: ", ships_available)
            ships_available.remove(ship_choice)
            new_ship = GSP.create_ship(ship_choice)
            user_within_bounds = False
                
            while user_within_bounds == False:
                try: 
                    start_position = input("Which position on the board would you like to place it: ")
                    start_coord = label_to_coord(start_position)
                    user_within_bounds = True
                except ValueError as e:
                    print(e)
            
            orientations = check_orientations(new_ship.size, start_position)
            chosen_orientation = multiple_choice("In which orientation would you like to place the ship: ", orientations)
            
            while player.is_occupied(new_ship.size,start_position,chosen_orientation):
                print("This spot is occupied by another ship. Please choose a different location")
                user_within_bounds = False
                while user_within_bounds == False:    
                    try:
                        start_position = input("Which position on the board would you like to place it: ")
                        orientations = check_orientations(new_ship.size, start_position)
                        chosen_orientation = multiple_choice("In which orientation would you like to place the ship: ", orientations)
                        user_within_bounds = True
                    except ValueError as e:
                        print(e)
                
            player.place_ship(ship_choice, start_position, chosen_orientation)
            player.display_friendly_board()
        player.display_ships()
        remove_ships = input("Would you like to restart the ship placing process (y/n): ").strip().lower()
        
        if remove_ships == 'y':
            all_or_one = input("Would you like to clear the entire board (y/n): ").strip().lower()
            if all_or_one == 'y':
                player.remove_all_ships()
                player.display_friendly_board()
                while True:
                    ships_available = ships.copy()
                    clear_screen()
                    
                    for ship in ships:
                        ship_choice = multiple_choice(f"Which ship would you like to place {player.name}: ", ships_available)
                        ships_available.remove(ship_choice)
                        new_ship = GSP.create_ship(ship_choice)
                        user_within_bounds = False
                            
                        while user_within_bounds == False:
                            try: 
                                start_position = input("Which position on the board would you like to place it: ")
                                start_coord = label_to_coord(start_position)
                                user_within_bounds = True
                            except ValueError as e:
                                print(e)
                        
                        orientations = check_orientations(new_ship.size, start_position)
                        chosen_orientation = multiple_choice("In which orientation would you like to place the ship: ", orientations)
                        
                        while player.is_occupied(new_ship.size,start_position,chosen_orientation):
                            print("This spot is occupied by another ship. Please choose a different location")
                            while user_within_bounds == False:    
                                try:
                                    start_position = input("Which position on the board would you like to place it: ")
                                    orientations = check_orientations(new_ship.size, start_position)
                                    chosen_orientation = multiple_choice("In which orientation would you like to place the ship: ", orientations)
                                    user_within_bounds = True
                                except ValueError as e:
                                    print(e)
                                    
                        player.place_ship(ship_choice, start_position, chosen_orientation)
                        player.display_friendly_board()
                    player.display_ships()
            else:
                while True:
                    ships_available = ['Carrier', 'Battleship', 'Cruiser', 'Submarine', 'Destroyer']
                    ship_type = multiple_choice(f"Which ship would you like to replace {player.name}: ", ships_available)
                    player.remove_ship(ship_type)
                    new_ship = GSP.create_ship(ship_type)
                    user_within_bounds = False
                    while user_within_bounds == False:
                        try: 
                            start_position = input("Which position on the board would you like to place it: ")
                            start_coord = label_to_coord(start_position)
                            user_within_bounds = True
                        except ValueError as e:
                            print(e)
                    orientations = check_orientations(new_ship.size, start_position)
                    chosen_orientation = multiple_choice("In which orientation would you like to place the ship: ", orientations)
                    
                    while player.is_occupied(new_ship.size,start_position,chosen_orientation):
                        print("This spot is occupied by another ship. Please choose a different location")
                        start_position = input("Which position on the board would you like to place it: ")
                        orientations = check_orientations(new_ship.size, start_position)
                        chosen_orientation = multiple_choice("In which orientation would you like to place the ship: ", orientations)
                
                    player.place_ship(ship_type, start_position, chosen_orientation)
                    player.display_ships()
                    player.display_friendly_board()
                    finished = input("Are you finished editing your ship locations (y/n): ").strip().lower()
                    if finished == 'y':
                        print("You have selected to end replacing ships")
                        break
                    else:
                        continue
        else:
            break
        
        break

# Loop to run once game has started
is_running = True
while is_running:
    for player in players:
        clear_screen()
        enemy = players[1] if player == players[0] else players[0]
        print(f"It is {player.name}'s turn!")
        player.display_friendly_board()
        player.display_target_board()
        
        user_within_bounds = False 
        while user_within_bounds == False:
            try: 
                strike_location = input("Which position on the board would you like to strike: ")
                strike_coord = label_to_coord(strike_location)
                user_within_bounds = True
            except ValueError as e:
                print(e)
        
        if player.target_board.board[strike_coord] in [' M ', ' H ']:
            user_within_bounds = False 
            while user_within_bounds == False:
                try: 
                    strike_location = input("You have already struck at this location please select a new location: ")
                    strike_coord = label_to_coord(strike_location)
                    if player.target_board.board[strike_coord] in [' M ', ' H ']:
                        continue
                    else:
                        user_within_bounds = True
                except ValueError as e:
                    print(e)
        else:
            player.strike(enemy, strike_location)
                            
        player.strike(enemy, strike_location)
    
    if enemy.all_ships_destroyed():
        player.display_friendly_board()
        enemy.display_friendly_board()
        is_running = False
        print(f"The winner is {player.name}!")
    else:
        continue

