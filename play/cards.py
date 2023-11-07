import random

def builddeck():
    """
    Generate the Uno deck of 121 cards
    Parametres : None
    Return values : deck->list
    """
    deck = []
    colours = ["Red","Green","Blue","Yellow","White"]
    values = [0,1,2,3,4,5,6,7,8,9,"+2","skip","Reverse"]
    for colour in colours:
        for value in values:
            cardVal = "{} {}".format(colour, value)
            deck.append(cardVal)
            if value != 0:
                deck.append(cardVal)
    return deck

   
def shuffleDeck(deck):
    """
    Shuffles a list of items passed into it
    Parametre : deck->list
    Return values : deck->list
    """
    random.shuffle(deck)
    return deck

print(shuffleDeck(builddeck()))