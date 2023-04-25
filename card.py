import random

# generates a new random card
class Card:
    typ = ""
    farbe = 0
    punkte = 0

    possible_types = ["7", "8", "9", "10", "B", "Q", "K", "A"]
    possible_farben = ["Kreuz", "Pik", "Herz", "Karo"]

    def __init__(self):
        # innitialize a random card
        random_typ = self.possible_types[random.randint(0, len(self.possible_types)-1)]
        random_farbe = self.possible_farben[random.randint(0, len(self.possible_farben)-1)]

        self.typ = random_typ
        self.farbe = random_farbe
        self.punkte = self.calculate_punkte()

    def calculate_punkte(self):
        if self.typ == "7":
            return 7
        elif self.typ == "8":
            return 8
        elif self.typ == "9":
            return 9
        elif self.typ == "10" or self.typ == "B" or self.typ == "Q" or self.typ == "K":
            return 10
        elif self.typ == "A":
            return 11
        else:
            return 0