import random





cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

playing = True

player_total= 0
dealer_total = 0
play_again = ""
player_bust = False


def sum_hand(hand):
    total = 0
    total = sum(hand)

    while True:
        if total > 21:
            if 11 in hand:
                total -= 10
            else:
                return 0
        else:
           return total




def deal_hand(hand):
    hand.append(random.choice(cards))
    hand.append(random.choice(cards))

def player_stick_twist(hand,dealer_hand):
    print(f"Dealer hand is [X , {dealer_hand[1]}].")
    player_total = sum_hand(hand)
    stick_or_twist = input(f"Your hand is {player_hand}.Your total is {player_total}. Do you wish to twist (T) or stick(S)?").upper()

    if stick_or_twist == "T":
        hand.append(random.choice(cards))
        player_total = sum_hand(hand)
        print(f"Your total is {player_total}")

        if player_total > 21:
            print(f"You are bust!")
            return

        player_stick_twist(hand,dealer_hand)
    else:
        player_total = sum_hand(hand)
        print(f"Your total is {player_total}")
        return


def dealer_stick_twist(hand):

    dealer_total=sum_hand(hand)
    while dealer_total <21:

        if dealer_total < 17:
            hand.append(random.choice(cards))
            dealer_total = sum_hand(hand)
        else:
            return






while playing:
    player_hand = []
    dealer_hand = []
    deal_hand(player_hand)
    deal_hand(dealer_hand)

    player_stick_twist(player_hand,dealer_hand)

    if sum_hand(player_hand) <= 21:
        dealer_stick_twist(dealer_hand)


    player_total= sum_hand(player_hand)
    dealer_total=sum_hand(dealer_hand)

    if player_total > dealer_total:
        if dealer_total >21:
            print("Dealer went bust")

        print("You win!")
        print(f"You scored {player_total}.  Dealer scored {dealer_total}.")

    else:
        print("You lose")
        print(f"You scored {player_total}.  Dealer scored {dealer_total}.")


    play_again = input("Play again?(Y/N)").lower()

    if play_again == "n":
        playing = False



