from classes import deck, color
import random

"""
Initializing the classes
"""
color = color.color()
classdeck = deck.Deck()

print(color.BOLD + color.GREEN + '\nWelcome to House of Cards!' + color.END)

"""
Initializing the variables
"""
deck = []
deck_set = []
design = "-" * 30
round = 1

"""
Printing the Deck by set basis
"""
print("")
print(color.YELLOW + design + color.END)
print(color.BOLD + 'All cards in the deck' + color.END)
print(color.BLUE + design + color.END)

deck_set = classdeck.full_deck()
for set in deck_set:
    if set[0] == 'Ace':
        print("")
        print(color.BOLD + set[1] + color.END)
        print(color.BLUE + design + color.END)
    print(set)
print("")

print(color.BLUE + design + color.END)
print(color.YELLOW + design + color.END)
print("")

"""
A call to shuffle followed by 52 calls to dealOneCard() results in the caller being provided all 52 cards of the deck in a random order.
If the caller then makes a 53rd call dealOneCard(), no card is dealt.
"""
try:
    while True:
        classdeck.shuffle()
        card = classdeck.dealOneCard()
        print(color.PURPLE + 'Round: ' + str(round) + color.END)
        if card != "empty":
            print(color.DARKCYAN + "The card chosen: " + str(card) + color.END)
            print("")
        elif card == "empty":
            print(color.BOLD + 'no card is dealt' + color.END)
            print("")
            break
        round += 1
except Exception as e:
    print(color.RED + "There is something wrong in choosing the card: " + str(e) + color.END)
