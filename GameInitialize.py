import GameSetupClasses as GSP
player = GSP.Player("John")
print(GSP.check_orientations(5, 'B10'))
player.ship_to_board('carrier', 'B9', 'up')
player.ship_to_board('battleship','C6', 'right')
player.display_friendly_board()
print(player)