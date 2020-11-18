from classes import deck, color
import random

color = color.color()
print(color.GREEN + '\nWelcome to House of Cards!' + color.END)

classdeck = deck.Deck()
deck = []
deck_set = []
extend = 'y'
design = "-" * 150
print("")
print(color.YELLOW + design)
print(color.BLUE + design + color.END)
deck_set = classdeck.full_deck()
for set in deck_set:
    print(set)
print(color.BLUE + design)
print(color.YELLOW + design + color.END)
print("")

# deck = classdeck.mixSets()
deck = [1,2,3,4,5,6]
i = 1
while extend == 'y':
    try:
        suffled = classdeck.shuffleDeck(deck)
        card_num = random.randrange(0,len(deck))
        print(i)
        # card_num = input(color.GREEN + 'Pick a card by entering number between 1 to '+ str(len(deck)) +': ' + color.END)
        print("The card chosen: " + str(deck[int(card_num)]))
        deck.remove(deck[int(card_num)])
        print("")
        i = i + 1
        extend = 'y'
        # extend = input('Do you wanna pick another one?(y/n): ')
    except IndexError:
        print("Oops! you have entered a number out of range. Please try again...")
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
    except Exception as e:
        print("There is something wrong " + str(e)) 
