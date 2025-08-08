cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def main():
    while True:
        player_input = get_player_input("PSSSTTTT, Wanna play a game of blackjack?! (Y/N)")
        play_game(player_input)


def get_player_input(prompt):        
  player_input = input(f"{prompt}: ").capitalize()
  return player_input

def play_game(player_input):
    match(player_input):
        case "Y":
            pass
        case "N":
            pass
        case "T":
            pass
        case "S":
            pass
        case "Q":
            pass
        















if __name__ == "__main__":
    main()