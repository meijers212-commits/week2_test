def ask_player_action() -> str:
    while True:
        choice = input("please choose 'H 'for 'hit' or S for 'stand'")
        choice = choice.lower()
        if choice == "h" or "s":
            break
    return choice


