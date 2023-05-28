import random
import sys
from termcolor import colored

print(colored("**** WAR: Attack on Titan Edition ****", 'red'))
 
suits = ('Hearts', 'Spades', 'Clubs', 'Diamonds')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 11,
          'Queen': 12, 'King': 13, 'Ace': 14}
ts = colored("Titan Strength:", 'magenta')
fp = colored("Fire Power:", 'magenta')

def print_directions():
    print(colored("**** WAR: Attack on Titan Edition ****", 'red'))
    print(colored("Directions / Description:", 'cyan'))
    # Provide the directions for the game
    print(colored("-" * 50, 'red'))
    print('1. The game is called "WAR: Attack on Titan Edition". It is a card game that pits two factions, Marly and Eldia, against each other.\n')
    print("2. At the beginning of the game, you will be prompted to choose whether you want to start a war between Marly and Eldia. Enter 'Y' for yes or 'N' for no.\n")
    print("3. If you choose to start the war, the game will begin. Otherwise, the program will exit.\n")
    print("4. The deck of cards is shuffled, and each player is dealt 26 cards from the shuffled deck.\n")
    print("5. The game consists of multiple rounds, also known as battles. Each round involves players comparing their top cards.\n")
    print('6. In each round, the top card of each' "player's" "deck is revealed, and their respective strengths are displayed. Marly's strength is represented as" '"Fire Power"', "and Eldia's" 'strength is represented as "Titan Strength".\n')
    print("7 If the strengths of the two cards are equal, a war occurs. This means that the top 5 cards from each player's deck are compared to determine the winner. The highest combination of card values wins the war.\n")
    print("8. If one player's card has a higher strength than the other, that player wins the round, and the cards are added to the bottom of their deck.\n")
    print("9. The game continues until one player runs out of cards. The player who runs out of cards loses, and the other player wins the war.\n")
    print("10. After the game ends, the winner is announced: either Marly or Eldia, based on who won the war.\n")
    print("11. The game is designed to simulate the game of War but with an Attack on Titan theme, where the strengths of the factions are determined by the values of the playing cards.\n")
    print('12. Enjoy the intense battles and strategic gameplay of "WAR: Attack on Titan Edition"!\n')
    print(colored("-" * 50, 'red'))

def ask_for_directions():
    choice = input(colored("Do you want to see the games directions? (Y/N): ", 'cyan')).upper()

    if choice == "Y":
        print_directions()

    elif choice == "N":
        pass

    else:
        print("Invalid choice. Please enter 'Y' or 'N'.")
        ask_for_directions()

directions = ask_for_directions()

def play():
    choice = 'Wrong'
    while choice not in ['Y', 'N']:
        choice = input(colored('Do you want to start a WAR between Marly and Eldia (Y or N): ', 'cyan')).upper()

        if choice not in ['Y', 'N']:
            print(colored('WAR is not a joke, select Y or N. The 2000 year Glory could be yours.', 'cyan'))

    if choice == 'Y':
        return True
    else:
        sys.exit(0)  # Exit the program

playgame = play()

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if isinstance(new_cards, list):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f"{self.name}:"


def start_war():
    player_one_cards = []
    player_two_cards = []

    for _ in range(5):
        if len(player_one.all_cards) == 0 or len(player_two.all_cards) == 0:
            break
        player_one_cards.append(player_one.remove_one())
        player_two_cards.append(player_two.remove_one())

    print(colored("!!WAR!!", 'magenta'))
    print(f"{player_one} {fp} {', '.join(str(card) for card in player_one_cards)}")
    print(f"{player_two} {ts} {', '.join(str(card) for card in player_two_cards)}")

    if len(player_one_cards) == 0 or len(player_two_cards) == 0:
        return 0

    player_one_battle_value = sum(card.value for card in player_one_cards)
    player_two_battle_value = sum(card.value for card in player_two_cards)
    print(f"{player_one} battle value: {player_one_battle_value}")
    print(f"{player_two} battle value: {player_two_battle_value}")
    if player_one_battle_value > player_two_battle_value:
        return 1
    elif player_one_battle_value < player_two_battle_value:
        return -1
    else:
        return None


player_one = Player(colored("The Marlians", 'cyan'))
player_two = Player(colored("The Eldians", 'yellow'))

new_deck = Deck()
new_deck.shuffle()

for _ in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True
round_num = 0

while game_on:
    round_num += 1
    print(colored(f"Battle#: {round_num}", 'green'))

    if len(player_one.all_cards) == 0:
        print(colored("The Marlians have been wiped out!", 'red'),colored("The Eldians have won the WAR!", 'green'))
        game_on = False
        break
    if len(player_two.all_cards) == 0:
        print(colored("e Eldians, **Island Devils** were eradicated!", 'red'),colored("The Marlians won the WAR!", 'green'))
        game_on = False
        break

    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    print(f"{player_one} {player_one_cards[0]} ({len(player_one.all_cards)} cards)")
    print(f"{player_two} {player_two_cards[0]} ({len(player_two.all_cards)} cards)")

    at_war = True

    while at_war:
        if player_one_cards[-1].value == player_two_cards[-1].value:
            print(colored("Battle strength is Equal!! 2000 year WAR continues...", 'magenta'))
            result = start_war()

            if result == 1:
                player_one.add_cards(player_one_cards)
                player_one.add_cards(player_two_cards)
                print(f"{player_one}",colored("won the BATTLE!", 'green'))
                at_war = False

            elif result == -1:
                player_two.add_cards(player_one_cards)
                player_two.add_cards(player_two_cards)
                print(f"{player_two}", colored("won the BATTLE!", 'green'))
                at_war = False

            else:
                print(colored("War continues...", 'magenta'))
                if len(player_one.all_cards) < 5 or len(player_two.all_cards) < 5:
                    
                    if len(player_one.all_cards) < 5:
                        print(f"{player_one}",colored("Lost the WAR!", 'red'))
                        print(f"{player_two}",colored("Won the WAR!", 'green'))

                    else:
                        print(f"{player_two}",colored("Lost the WAR!", 'red'))
                        print(f"{player_one}",colored("Won the WAR!", 'green'))
                    game_on = False
                    break

                else:
                    for _ in range(5):
                        player_one_cards.append(player_one.remove_one())
                        player_two_cards.append(player_two.remove_one())

        elif player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            print(f"{player_one}",colored("won the BATTLE!", 'green'))
            at_war = False
        else:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            print(f"{player_two}",colored("won the BATTLE!", 'green'))
            at_war = False
