from classes import deck, color
import random

"""
Initializing the classes
"""
color = color.color()
classdeck = deck.Deck()

print(color.GREEN + '\nWelcome to House of Cards!' + color.END)

"""
Initializing the variables
"""
deck = []
deck_set = []
chosen_card = []
choice = 'y'
design = "-" * 150

"""
Printing the Deck by set basis
"""
print("")
print(color.YELLOW + design)
print(color.BLUE + design + color.END)
deck_set = classdeck.full_deck()
for set in deck_set:
    print(set)
print(color.BLUE + design)
print(color.YELLOW + design + color.END)
print("")

"""
Mixing the sets to one whole deck of 52s
"""
deck = classdeck.mixSets()
shuffled = deck
i = 1

"""
While Loop to run the pick if the user is interested to continue
to let user choose the card from the shuffled deck and removes
from it and contiues until the deck is empty.
Error handinlins are also put in place
"""
while choice in ['y','Y']:
    try:
        shuffled = classdeck.shuffle(shuffled)
        # card_num = random.randrange(0,len(shuffled)) + 1
        # print('Pick a card by entering number between 1 to '+ str(len(shuffled)) +': ' + str(card_num)) # Uncomment to automate
        print(color.PURPLE + 'Round: ' + str(i) + color.END)
        i = i + 1
        card_num = int(input(color.GREEN + 'Pick a card by entering number between 1 to '+ str(len(shuffled)) +': ' + color.END))  # Comment to automate
        chosen_card = shuffled[card_num - 1]
        print(color.DARKCYAN + "The card chosen: " + str(chosen_card) + color.END)
        shuffled.remove(chosen_card)
        print("")
        if not shuffled:
            print("Deck is now empty")
            break
        # choice = 'y' # Uncomment to automate
        # Comment below 6 lines to automate
        question = 'Do you wanna pick another one?(y/Y or n/N): '
        choice = input(question)
        while choice not in ['y', 'Y', 'n', 'N']:
                print(color.RED + 'Please enter a valid pick intention' + color.END)
                print("")
                choice = input(question)
    except IndexError:
        print(color.RED + "Oops! you have entered a number out of range. Please try again..." + color.END)
        print("")
    except ValueError:
        print(color.RED + "Oops!  That was no valid number.  Try again..." + color.END)
        print("")
    except Exception as e:
        print(color.RED + "There is something wrong " + str(e) + color.END)
        print("")
