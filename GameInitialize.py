from GameSetupClasses import *
from HelperFunctionsGame import *
import time

greet()

players = get_player_names()

for player in players:
    print(f"\nIt is {player.name}'s turn to place their ships\n")
    ship_lst = ['Carrier','Battleship','Cruiser','Submarine','Destroyer']
    
    while len(ship_lst) > 0:
        
        ship_choice = get_ship_choice(ship_lst)
        ship_lst.remove(ship_choice)
        new_ship = create_ship(ship_choice)
        
        ship_placement(new_ship,player)
        
    player.display_friendly_board()
    reset_board(player)
    reset_ship(player)

is_running = True

while is_running:
    for player in players:
        clear_screen()
        enemy = players[1] if player == players[0] else players[0]
        player.display_ships_destroyed()
        player.display_target_board()
        player.display_friendly_board()
        print(f"It is {player.name}'s turn to strike!")
        row,column = get_strike_position()
        player.strike(enemy,row,column)
        if enemy.all_ships_destroyed(player):
            print(f"{player.name} wins the game!")
            is_running = False
            break
for player in players:
    print(player.display_friendly_board())
