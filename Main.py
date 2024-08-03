# Display art
from Art import logo, vs
from Game_Data import data
import random
from replit import clear


def format_data(account):
    """Formats the account data into printable format."""
    acc_name = account["name"]
    acc_des = account["description"]
    acc_country = account["country"]
    return f"{acc_name}, a{acc_des}, from {acc_country}"


def check_answer(guess, a_followers, b_followers):
    """Takes the user guess and followers count and return if they have it right. """
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


print(logo)
score = 0
game_should_continue = True
acc_2 = random.choice(data)
while game_should_continue:
    acc_1 = acc_2
    acc_2 = random.choice(data)
    while acc_1 == acc_2:
        acc_2 = random.choice(data)
    # Format the account data into printable format.
    print(f"Compare A: {format_data(acc_1)}")
    print(vs)
    print(f"Against B: {format_data(acc_2)}")

    # Ask user for a guess.
    guess = input("Who has more followers? Type 'A' or 'B'").lower()
    # Check if  user is correct.
    a_follower = acc_1["follower_count"]
    b_follower = acc_2["follower_count"]
    # Get follower count of each account.
    is_correct = check_answer(guess, a_follower, b_follower)
    clear()
    print(logo)
    if is_correct:
        score += 1
        print(f"You're correct!!! Current score is {score}")
    else:
        game_should_continue = False
        print(f"Nah son that's wrong Final score is {score}")
