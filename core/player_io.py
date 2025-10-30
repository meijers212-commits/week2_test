def ask_player_action() -> str:
    while True:
        choice = input("please choose 'H 'for 'hit' or S for 'stand'")
        choice = choice.lower()
        if choice in ["h","s"]:
            break
    return choice


