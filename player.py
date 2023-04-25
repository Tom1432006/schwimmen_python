class Player:
    name = ""
    leben = 0
    karten_in_hand = []
    punkte = 0

    def __init__(self, name, leben, karten_in_hand):
        self.name = name
        self.leben = leben
        self.karten_in_hand = karten_in_hand

    def calculate_punkte(self):
        # wenn alle karten den gleichen typ haben 30.5 punkte
        if self.karten_in_hand[0].typ == self.karten_in_hand[1].typ and self.karten_in_hand[0].typ == self.karten_in_hand[2].typ:
            self.punkte = 30.5
            return

        # punkte normal errechnen
        karten_farben = ["Kreuz", "Pik", "Herz", "Karo"]
        punkte_pro_farbe = [0, 0, 0, 0]

        for karte in self.karten_in_hand:
            # get the farbe
            karten_farbe = karte.farbe
            karten_farbe_index = karten_farben.index(karten_farbe)

            punkte_pro_farbe[karten_farbe_index] += karte.punkte
        
        self.punkte = max(punkte_pro_farbe)
        