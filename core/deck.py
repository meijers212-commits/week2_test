import random
def build_standard_deck() -> list[dict]:
    c_list = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    c_types = ["H","C","S","D"]
    c_dict = []
    for rank in c_list:
        for suite in c_types:
            c_dict.append({"rank": rank, "suite": suite})
    return c_dict


def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:
    for _ in range(swaps):
        while True:
            i = random.randint(0, len(deck) - 1)
            j = random.randint(0, len(deck) - 1)
            if i == j:
                continue
            suit = deck[i]["suite"]
            if suit == "H" and j % 5 == 0:
                break
            elif suit == "C" and j % 3 == 0:
                break
            elif suit == "D" and j % 2 == 0:
                break
            elif suit == "S" and j % 7 == 0:
                break
        deck[i], deck[j] = deck[j], deck[i]
    return deck



