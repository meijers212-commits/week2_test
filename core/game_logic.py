import random
from core.player_io import ask_player_action


def calculate_hand_value(hand: list[dict]) -> int:
    count = 0
    for card in hand:
        rank = card["rank"]
        if rank in ["J", "Q", "K"]:
            count += 10
        elif rank == "A":
            count += 11 if count + 11 <= 21 else 1
        else:
            count += int(rank)
    return count


def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
    for i in range(2):
        card = deck.pop()
        player["hand"].append(card)
    print(f"the player hand value is {calculate_hand_value(player['hand'])}")

    for i in range(2):
        card = deck.pop()
        dealer["hand"].append(card)
    print(f"the dealer's hand value is {calculate_hand_value(dealer['hand'])}")


def dealer_play(deck: list[dict], dealer: dict) -> bool:
    while True:
        count = calculate_hand_value(dealer["hand"])
        if count < 17:
            card = deck.pop()
            dealer["hand"].append(card)
        else:
            break

    count = calculate_hand_value(dealer["hand"])
    if count > 21:
        print(f"dealer busts with {count}! :)")
        return False

    print(f"dealer stands with {count}.")
    return True


def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    flag1 = True
    while flag1:
        deal_two_each(deck, player, dealer)
        while True:
            print(f"your current cards are {player["hand"]} \n"
                  f"dealers current cards are {dealer["hand"]}")
            choice = ask_player_action()
            if choice == "h":
                card = deck.pop()
                player["hand"].append(card)
                hand_v = calculate_hand_value(player["hand"])
                if hand_v > 21:
                    print(f"your hand value is {hand_v}. you lose :(.")
                    flag1 = False
                    break
                elif hand_v == 21:
                    print(f"nice! you won :) your hand value is {hand_v}\n"
                          f"your hand wos: {player['hand']}")
                    flag1 = False
                    break
                else:
                    print(f"your current hand value is {calculate_hand_value(player["hand"])}")
                    continue

            elif choice == "s":
                dealer_won = dealer_play(deck, dealer)
                player_val = calculate_hand_value(player["hand"])
                dealer_val = calculate_hand_value(dealer["hand"])
                if dealer_won:
                    if dealer_val > player_val:
                        print(f"the dealer won! dealer hand value is: {dealer_val}\n "
                              f"player hand value: {player_val}")
                    elif player_val > dealer_val:
                        print(f"the player won :) player hand value is: {player_val}\n "
                              f"dealer hand value is: {dealer_val}")
                    else:
                        print(f"it's a tie :|.\n "
                              f"player hand value: {player_val}\n "
                              f"dealer hand value: {dealer_val}")
                else:
                    print(f"player won :).\n "
                          f"dealer hand: {dealer['hand']}\n "
                          f"player hand: {player['hand']}")

                flag1 = False
                break

            else:
                print("invalid choice. please enter 'h' to hit or 's' to stand.")

