import random

colors = ["Spader", "Klöver", "Hjärter", "Ruter"]
values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Knekt", "Dam", "Kung", "Ess "]

cards = []
for card_color in colors:
    for card_value in values:
        cards.append((card_color, card_value))

random.shuffle(cards)
card = cards.pop()
card2 = cards.pop()
card3 = cards.pop()
card4 = cards.pop()
print (card, card2, card3, card4)
