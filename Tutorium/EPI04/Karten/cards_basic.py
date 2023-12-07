import random

def create_card_list(number_of_cards: int) -> [(int, str)]:
    """
    creates a list of tuple's (cards), with the colors green, red, yellow, blue (in german) and of the range 1 to number_of_cards.

    :param number_of_cards: number card of each type of cards
    :return: [(int, str)] - list of all the card for a game, len of the list is number_of_cards * 4
    """
    list_cards = []
    for i in range(1, number_of_cards + 1):
        for j in ["Pik", "Kreuz", "Herz", "Karo"]:
            list_cards.append((i, j))
    return list_cards


def compare_two_cards(card_one: (int, str), card_two: (int, str)) -> int:
    """
    returns a number encoding if card_one has a larger value than card_two

    :param card_one: first card, contains value and the color
    :type card_one: (int, str)
    :param card_two: second card, contains value and the color
    :type card_two: (int, str)
    :return: number - 0: if card_one is lower than card_two; 1: if card_one is equal card_two; 2: if card_one is larger
    than card_two;
    """
    if card_one[0] > card_two[0]:
        return 2
    elif card_one[0] == card_two[0]:
        return 1
    else:
        return 0
    
    
def compare_two_cards_trump(card_one: (int, str), card_two: (int, str), trumpf: str) -> int:
    """
    returns a number with declares if card_one is bigger than the other

    :param card_one: first card, contains value and the color
    :type card_one: (int, str)
    :param card_two: second card, contains value and the color
    :type card_two: (int, str)
    :param trumpf: str - color with has a bigger weight than the others
    :return: number - 0: if card_one is lower than card_two; 1: if card_one is equal card_two; 2: if card_one is bigger
    than card_two;
    """

    if card_one[1] == trumpf:
        # card one is trumpf
        if card_two[1] == trumpf:
            # card two is trumpf, check bigger number of both cards
            if card_one[0] > card_two[0]:
                return 2
            elif card_one[0] == card_two[0]:
                return 1
            else:
                return 0
        else:
            # card two is no trumpf -> card one is bigger
            return 2
    elif card_two[1] == trumpf:
        # card one no trumpf & card two is trumpf -> card two is bigger
        return 0
    else:
        # no trumpf card - only value
        if card_one[0] > card_two[0]:
            return 2
        elif card_one[0] == card_two[0]:
            return 1
        else:
            return 0


def hand_out_cards(list_cards: [(int, str)], players: int, number_of_cards: int) -> [[(int, str)]]:
    """
    deals the cards of the deck to the players

    :param list_cards: shuffled list
    :param players: number of players, with get cards
    :param number_of_cards: number of card per player
    :return: [[(int, str)]] - returns players sublist with the corresponding cards
    :rtype [[(int, str)]]
    """
    return_list = []
    for i in range(players):
        return_list.append(list_cards[i * number_of_cards:i * number_of_cards + number_of_cards])
    return return_list



def main():
    cards = create_card_list(8)
    #print(cards)
    hands = hand_out_cards(cards,6,4)
    print(hands)
    #card1 = cards[2][:]
    #print(card1)
    #card2 = cards[7][:]
    #print(card2)
    #comp = compare_two_cards(card2,card1)
    #print(comp)
    #comp_trump = compare_two_cards_trump(card1,card2,"Herz")
    #print(comp_trump)

    
if __name__ == '__main__':
    main()
else:
    print("name", __name__)