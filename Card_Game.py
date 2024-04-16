import random

suits = ("Heart", "Diamond", "Spades", "clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10,
          "Jack": 11, "Queen": 12, "King": 13, "Ace": 14}


class Card:
    """
    To understand :
        suit of card (i.e. Heart, Diamond, Spades, clubs )
        Rank (1 to 13)
        value
    """

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:
    """
    To initiate a new deck
        Create all 52 Card objects
        Hold a list of Cards objects
    Shuffle Deck through a method
    Pop card from the deck
    """

    def __init__(self):
        self.Deck_of_cards = []

        for suit in suits:
            for rank in ranks:
                self.Deck_of_cards.append(Card(suit, rank))

    def shuffle_deck(self):
        random.shuffle(self.Deck_of_cards)

    def deal_one(self):
        return self.Deck_of_cards.pop()


class Player:
    """
    To hold a player's current list of cards
    Player should be able to add or remove card from list of card object
    Player should be able to add single or multiple card to their list
    """

    def __init__(self, name):
        self.name = name
        self.player_cards = []

    def remove_one(self):
        return self.player_cards.pop(0)

    def add_card(self, new_card):
        if isinstance(new_card, list):
            # Can't use append method because it will add a list inside original list{Nesting}.
            self.player_cards.extend(new_card)
        else:
            self.player_cards.append(new_card)

    def __str__(self):
        return f"Player {self.name} has {len(self.player_cards)} cards."


Player_1 = Player("Kumar")
Player_2 = Player("Manglam")

Deck = Deck()
Deck.shuffle_deck()

for card in range(26):
    Player_1.add_card(Deck.deal_one())
    Player_2.add_card(Deck.deal_one())

game = True
round_number = 0

while game:
    round_number += 1
    print("Round Number- ", round_number)
    if len(Player_2.player_cards) == 0:
        game = False
        print(f"!!! {Player_1.name} Won !!!!")
        break
    elif len(Player_1.player_cards) == 0:
        game = False
        print(f"!!! {Player_2.name} Won !!!!")
        break

    card_from_Player_1 = []
    card_from_Player_1.append(Player_1.remove_one())
    card_from_Player_2 = []
    card_from_Player_2.append(Player_2.remove_one())

    War = True

    while War:

        if card_from_Player_1[-1].value > card_from_Player_2[-1].value:
            Player_1.add_card(card_from_Player_1)
            Player_1.add_card(card_from_Player_2)
            War = False

        elif card_from_Player_1[-1].value < card_from_Player_2[-1].value:
            Player_2.add_card(card_from_Player_1)
            Player_2.add_card(card_from_Player_2)
            War = False

        else:
            print("!!!WAR!!!")

            if len(Player_1.player_cards) < 5:
                print(f"{Player_1.name} have less than 5 card.......\n"
                      f"{Player_2.name} WON !!!!!")
                game = False
                break

            elif len(Player_2.player_cards) < 5:
                print(f"{Player_2.name} have less than 5 card.......\n"
                      f"{Player_1.name} WON !!!!!")
                game = False
                break

            else:
                for x in range(5):
                    card_from_Player_1.append(Player_1.remove_one())
                    card_from_Player_2.append(Player_2.remove_one())
