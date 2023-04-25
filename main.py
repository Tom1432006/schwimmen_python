import game
import player

if __name__ == "__main__":
    # create players
    player1 = player.Player("spieler1", 3, [])
    player2 = player.Player("spieler2", 3, [])
    players = [player1, player2]

    # create new game
    game = game.Game(players)

    game.new_game()

    new_round = False
    
    #game loop
    while True:
        if new_round == True:
            game.new_game()
            new_round = False
        game.print_state()

        player_input = input(">>>")
        game.make_move(player_input)
        if game.check_passen() == True:
            game.check_winner()
            new_round = True
        
        if len(game.players) == 1:
            exit(game.players[0].name + " hat gewonnen")