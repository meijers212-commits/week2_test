from core.deck import build_standard_deck, shuffle_by_suit
from core.player_io import ask_player_action
from core.game_logic import run_full_game

if __name__ == "__main__":
   card_list = build_standard_deck()
   deck = shuffle_by_suit(card_list)
   player = {"hand": []}
   dealer = {"hand": []}
   run_full_game(deck, player, dealer)



