# This is the class to create a deck of cards.
# Made by Aneesh.

import random

class Deck:
    def __init__(self):
        """
        Initializing all the variables and other elements
        Also creates the full deck
        """
        self.suits = ["Spades","Hearts","Clubs","Diamonds"]
        self.card = []
        self.set = []
        self.deck = []
        for suit in self.suits:
            for rank in range(1, 14):
                if rank == 1:
                    rankName = "Ace"
                elif rank == 11:
                    rankName = "Jack"
                elif rank == 12:
                    rankName = "Queen"
                elif rank == 13:
                    rankName = "King"
                else:
                    rankName = rank
                self.card.append(rankName)
                self.card.append(suit)
                self.set.append(self.card)
                self.card = []
            self.deck.append(self.set)
            self.set = []

    def full_deck(self):
        """
        Returns a list containing the set of all cards.
        """
        return(self.deck)

    def mixSets(self):
        """
        Returns a list that contains deck with out set array
        """
        try:
            mixed = []
            for set in self.deck:
                for card in set:
                    mixed.append(card)
            return mixed
        except Exception as e:
            print("There is something wrong " + str(e))

    def shuffle(self, deck):
        """
        This method will return a deck with suffled cards
        """
        try:
            shuffled = []
            total_cards = len(deck)
            if total_cards > 2:
                for card_pos in range(total_cards):
                    shift_pos = random.randrange(0,total_cards)
                    swap_a = deck[card_pos]
                    swap_b = deck[shift_pos]
                    deck[shift_pos] = swap_a
                    deck[card_pos] = swap_b
                shuffled = deck
            elif total_cards == 2:
                choose_to_swap_2 = random.randrange(0,2)
                if choose_to_swap_2 == 0:
                    swap_a = deck[0]
                    swap_b = deck[1]
                    deck[0] = swap_b
                    deck[1] = swap_a
                    shuffled = deck
                else:
                    shuffled = deck
            else:
                shuffled = deck
            return shuffled
        except Exception as e:
            print("There is something wrong " + str(e))
