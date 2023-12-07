import cards_basic as cb
from math import floor as fl
from random import shuffle


def load_players() -> [str]:
    """
    Get the Person input for the players names
    
    :return [str] - List with all the name of the players
    """
    players = []

    print("If only 3 players are going to play, after giving their names press enter WITHOUT any input")
    while True:

        print("\n"*3)
        name = input("Please enter the name of the player: ")

        # If name is empty ask to write the name again
        if (len(players)==3 and len(name)==0):
            break
        elif (len(name)==0 or (name in players)):
            print("The player name can not be empty or be the same as other player")
            continue
        elif len(players)==4:
            break

        players.append(name)
    return players


def initialize_variables(players:[str]) -> ({str:int}, {str:list}):
    """
    Initialize all the variables for the players

    :param players: list with the name of all players
    :return: two dictionaries with the variables
    """

    cardset = cb.create_card_list(4) # Not sure how many cards are supposed to be in the game

    shuffle(cardset)

    hands = cb.hand_out_cards(cardset, len(players), fl(len(cardset)/len(players)))  # Also not sure how many cards should be given

    score = {x:0 for x in players}
    cards = {x:y for x in players for y in hands}

    return score, cards

def check_card(card:(int,str), player_hand:list, trump:str) -> bool:
    """
    Check if the player has a card of the trump type in its hand
    
    :param card: that wants to play
    :param player_hand: all the cards from the player
    :return bool: - true if it has a card with the trump, false otherwise
    """

    if card[1]==trump:   # True if the trump is the same 
        return True
    
    if (card[1]!=trump and any(c[1]==trump for c in player_hand)): # False if the trump is not the same and has a card with that trump in hand
        return False
    else:
        return True

def play_card(player_hand:list, trump:str) -> ((int, str), list):
    """
    Plays the card from the hand of the player
    """

    getcard = True

    while True:

        print(f"================ Your cards ; Trump is {trump} ================\n")

        for i, c in enumerate(player_hand):
            print(f"{i+1}.  {c}")

        while getcard:
            try:
                n = int(input(f"Please give the number of the card you want to choose from 1 to {len(player_hand)}:  "))
                if 1 <= n <= len(player_hand):
                    getcard = False
            except ValueError:
                print("Please try again")

        card = player_hand[n-1]

        if check_card(card, player_hand, trump):
            break
        else: getcard = True
    
    player_hand.pop(n-1)

    return (card, player_hand)

def get_winner(current_trick: list, trump: str) -> int:
    """
    Returns the index of the person that won

    :param current_trick: list with all the cards played in the round
    :param trump: color of the round
    :return int: index of the winner
    """

    best = tuple(-1, "none")

    for c in current_trick:
        n = cb.compare_two_cards_trump(c, best, trump)
        if n == 2:
            best = c

    return current_trick.index(best) # Due to how it works this will always have one winner
                                     # multiple winners can not happen

def update_score(won_cards:list, player:str, score:{str:int}) -> {str: int}:
    """
    Updates the score from the player
    """
    score[player] = score[player] + 1

    return score

def update_cards(won_cards:list, player:str, cardsdict:{str:list}) -> {str:list}:
    """
    Update the value of the cards
    """
    cardsdict[player] = cardsdict[player].extend(won_cards)

    return cardsdict


def determine_winner(scores: {str: int}) -> list:
    """
    Return a list with all the people that won
    """
    maxval = max(scores.values())

    return [k for k, v in scores.items() if v == maxval]


if __name__ == "__main__":
    pass
