import card
import random

class Game:
    players = []
    karten_in_mitte = []
    turn = 0

    turn_passen = -1

    def __init__(self, players):
        self.players = players
    
    def new_game(self):
        self.reset_game()

        # let random player start
        self.turn = random.randint(0, len(self.players)-1)

        print("Neue Runde!")
        self.karten_austeilen()

        for player in self.players:
            player.calculate_punkte()

    def karten_austeilen(self):
        # create cards
        karten = []
        number_of_cards_needed = len(self.players) * 3 + 3
        for _ in range(number_of_cards_needed):
            # create random card
            karte = card.Card()

            # generate new card if the card is already used
            while self.karte_schon_benutzt(karten, karte):
                karte = card.Card()
            
            karten.append(karte)
        
        # assign the first three cards to the first player and so on
        for i in range(len(self.players)):
            spieler_karten = [karten[3*i], karten[3*i+1], karten[3*i+2]]
            self.players[i].karten_in_hand = spieler_karten

        # put the last three cards on the table
        self.karten_in_mitte = [karten[len(karten)-1], karten[len(karten)-2], karten[len(karten)-3]]

    def print_state(self):
        # print turn
        print(self.players[self.turn].name + " ist an der Reihe\n")

        # print leben der spieler
        print("Leben:")
        for player in self.players:
            print(player.name + ": " + str(player.leben))

        print()

        self.print_player(self.players[self.turn])
        print()

        #print karten in der mitte
        print("Mitte:")
        for karte in self.karten_in_mitte:
            print(str(karte.farbe) + " " + str(karte.typ), end=', ')

        print() # new line
        print() # new line

    def print_player(self, player):
        player.calculate_punkte()

        print(player.name + ": " + str(player.punkte))
        # print karten
        for karte in player.karten_in_hand:
            print(str(karte.farbe) + " " + str(karte.typ), end=', ')

        print() # new line

    def make_move(self, player_input):
        player_input = player_input.lower()
    	
        if player_input == "exit" or player_input == "schließen":
            exit()
        elif player_input == "alle tauschen":
            karten_mitte = self.karten_in_mitte
            karten_spieler = self.players[self.turn].karten_in_hand
            
            self.karten_in_mitte = karten_spieler
            self.players[self.turn].karten_in_hand = karten_mitte
        elif "tauschen" in player_input:
            karten_zum_tauschen = player_input.replace("tauschen", "").strip().split(",")
            karte_player_index = int(karten_zum_tauschen[0]) - 1
            karte_mitte_index = int(karten_zum_tauschen[1]) - 1

            # karten speichern, die der spieler tauschen will
            karte_player = self.players[self.turn].karten_in_hand[karte_player_index]
            karte_mitte = self.karten_in_mitte[karte_mitte_index]

            # karten austauschen
            self.players[self.turn].karten_in_hand[karte_player_index] = karte_mitte
            self.karten_in_mitte[karte_mitte_index] = karte_player
        elif "passen" in player_input:
            if self.turn_passen == -1:
                self.turn_passen = self.turn
        elif "schieben" in player_input:
            pass # nichts tun
        else:
            print("Das gibt es nicht. Du kannst entweder tauschen, passen oder schieben, schreibe schließen zum beenden.")
            return

        # change turn
        self.turn = (self.turn + 1) % len(self.players)

    def check_passen(self):
        if self.turn_passen == self.turn:
            print(self.turn_passen, self.turn)
            # eine Runde vorbei
            return True
        return False

    def check_winner(self):
        self.update_player_punkte()

        print("Runde vorbei.")
        # compare the player scores
        worst_players = []
        worst_player_points = 100
        for player in self.players:
            if player.punkte < worst_player_points:
                # wenn spieler schlechter als schlechtester
                # worst players zurücksetzten
                worst_players = [player]
                worst_player_points = player.punkte
            elif player.punkte == worst_player_points:
                # wenn genauso schlecht wie schlechtester
                # zu worst players hinzufügen
                worst_players.append(player)
        
        # zieh den schlechtesten spielern ein leben ab
        for player in worst_players:
            player.leben -= 1
        
        self.untergegangene_spieler_loeschen()
    
    def update_player_punkte(self):
        for player in self.players:
            player.calculate_punkte()

    def untergegangene_spieler_loeschen(self):
        untergegangen = []
        for i in range(len(self.players)):
            if self.players[i].leben < 0:
                print(self.players[i].name + " ist untergegangen")
                untergegangen.append(i)
        
        for x in untergegangen:
            self.players.pop(x)

    def karte_schon_benutzt(self, karten, current_karte):
        for karte in karten:
            if current_karte.typ == karte.typ and current_karte.farbe == karte.farbe:
                return True
        
        # karte noch nicht benutzt
        return False
    
    def reset_game(self):
        self.karten_in_mitte = []
        self.turn_passen = -1
        self.turn = 0
