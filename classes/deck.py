# This is the class to create a deck of cards.
# Made by Aneesh.

import random
from .color import color

class Deck:
    def __init__(self):
        """
        Initializing all the variables and other elements
        Also creates the full deck
        """
        self.suits = ["Spades","Hearts","Clubs","Diamonds"]
        self.card = []
        self.deck = []
        self.shuffled = []
        self.color = color()
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
                self.deck.append(self.card)
                self.card = []

    def full_deck(self):
        """
        Returns a list containing the set of all cards.
        """
        return(self.deck)

    def shuffle(self):
        """
        Shuffle returns no value, but results in the cards in the deck being randomly permuted.
        no usage of shuffle function
        """
        try:
            total_cards = len(self.deck)
            if total_cards > 2:
                for card_pos in range(total_cards):
                    shift_pos = random.randrange(0,total_cards)
                    swap_a = self.deck[card_pos]
                    swap_b = self.deck[shift_pos]
                    self.deck[shift_pos] = swap_a
                    self.deck[card_pos] = swap_b
            elif total_cards == 2:
                choose_to_swap_2 = random.randrange(0,2)
                if choose_to_swap_2 == 0:
                    swap_a = self.deck[0]
                    swap_b = self.deck[1]
                    self.deck[0] = swap_b
                    self.deck[1] = swap_a
        except Exception as e:
            print(self.color.RED + "There is something wrong in shuffle fuction: " + str(e) + color.END)

    def dealOneCard(self):
        """
        This function should return one card from the deck to the caller.
        """
        try:
            if not self.deck:
                chosen_card = "empty"
            else:
                card_num = random.randrange(0,len(self.deck))
                chosen_card = self.deck[card_num]
                self.deck.remove(chosen_card)
            return(chosen_card)
        except Exception as e:
            print(self.color.RED + "There is something wrong in dealOneCard function: " + str(e) + color.END)
