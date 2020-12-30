from random import shuffle 

# Creating the Card class with Card classname
class Card():
    # initialize the method with values and suits instance 
    def __init__(self,values, suits):
        # use the self word to connect with card class
        self.values = values
        self.suits = suits

    # Representation method (__repr__) it makes nice way of printing 
    # (techincally for my understanding it changes the object adderss into the way of human reading )
    def __repr__(self):
        return f"{self.values} of {self.suits}"


# create the deck class
class Deck():
    # Initialize the method for creating the deck of cards:
    def __init__(self):
        # assign the values for value and suit 
        self.suit = ["Hearts","Diamonds", "Clubs", "Spades"]
        self.value = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        # Using the list comprehension for double for loop 
        self.card = [ Card(card_value, card_suit) for card_value in self.value for card_suit in self.suit]
        # Above list comprehension is equal to :
        #for card_value in self.value:
            #for card_suit in self.suit:
                #self.card = Card(card_value, card_suit)
        
        # Then pirnt and check whether out values are getting correctly and we can't return 
        # anythig in the __init__ method
        print(self.card, "\n")

    # define a count method
    def count(self):
        return len(self.card)
        # Above line is equal to below line

        # self.count = len(self.card)
        # return self.count

    #  Define __repr__ method
    def __repr__(self):
        # We can return in any form that we want
        return f"Deck of {self.count()} card"

    # card_shuffle method is used to shuffle the cards with the help of random module
    def card_shuffle(self):
        # We haave a condition that count is less than a 52 (deck of cards) we raise a error 
        if self.count() < 52:
            # Here we raise the error
            raise ValueError ("We can only shuffle the Deck of cards ")
        # Here we shuffe our card
        shuffle(self.card)
        
    # Its a private method (if we mention the _ sign before the name of the method 
    # we assign it is a private method)
    def _deal(self, no_of):
        # We assigna remove_card variable to get the input value for deal the card 
        remove_card = min([self.count(), no_of])
        # We must have atleast one card to deal if card count is 0, we raise the error 
        if self.count == 0:
            raise ValueError ("All cards have been Dealt")
        # assign the variable for return the dealing cards
        
        cards = self.card[-remove_card:]
        self.card = self.card[:-remove_card]
        return cards 
    # this deal_cards method is used to deal the cards with the help of _deal method 
    def deal_card(self, card_no):
        # we deal the card with the help of _deal() (private) method and return 
        return self._deal(card_no)
    

d = Deck()
print(d,"\n")
print(d.card_shuffle())
print(d.deal_card(5), "\n")

