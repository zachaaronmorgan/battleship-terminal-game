import GameSetupClasses as GSP
# user_name_1 = input("Hello welcome to my Battleship Terminal Game, to start please enter Player 1 name: ")
# user_name_2 = input("Hello welcome to my Battleship Terminal Game, to start please enter Player 2 name: ")

player_1 = GSP.Player('Zach')
player_2 = GSP.Player('John')

player_2.ship_to_board('destroyer', 'E6', 'right')
player_2.ship_to_board('carrier', 'B6', 'up')
player_1.strike(player_2, 'D5')
player_2.display_friendly_board()
player_1.display_target_board()

print(player_2.ships)

# Loop to run once game has started
is_running = True
while is_running:
    
    # Player 1 places their ships on their friendly board 
    
    # Player 2 places their ships on their friendly board
    
    is_running = False