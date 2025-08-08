import random
from game_data import data
from art import vs, logo

def choose_celeb():
    """Choose a random celeb from celebs in data"""
    return random.choice(data)

def display_celebs(CelebA,CelebB):
    """Print opening statements about celebrities"""
    print(f"Compare A: {CelebA["name"]}, a {CelebA["description"]} from {CelebA["country"]}.")
    print(vs)
    print(f"Against B: {CelebB["name"]}, a {CelebB["description"]} from {CelebB["country"]}.")

def compare_celebs(CelebA,CelebB, player_choice):
    """Compare the followers of the 2 celebs with the player choice and return if they were correct"""

    if CelebA["follower_count"] > CelebB["follower_count"] and player_choice == "A":
        return True
    elif CelebA["follower_count"] < CelebB["follower_count"] and player_choice == "B":
        return True
    else:
        return False

def print_header(score):
    """Prints logo , then if they have passed first round prints score"""
    print(logo)
    if score > 0:
        print(f"You're right! Current Score {score}")

def game():

    running = True
    celeb_choice_A = choose_celeb()
    celeb_choice_B = choose_celeb()
    score = 0

    while running:
        print_header(score)
        while True:
            #Make sure not the same celeb
            if celeb_choice_A == celeb_choice_B:
                celeb_choice_B = choose_celeb()
            else:
                break

        display_celebs(celeb_choice_A,celeb_choice_B)

    while True:
        #Get player choice input and check if valid
        choice = input("Who has more followers? Type 'A' or 'B'").upper()
        if choice == "A" or choice =="B":
            break
        else:
            print("Selection is not valid")

    if compare_celebs(celeb_choice_A,celeb_choice_B,choice):
        score +=1
        celeb_choice_A = celeb_choice_B
        celeb_choice_B = choose_celeb()
    else:
        running = False
        print(f"Sorry, thats wrong.  Final score: {score}")

game()