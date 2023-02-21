import random
import os
from game_data import data

score = 0

while True:
    def format_data(account_data):
        '''Takes the account data and returns printable format'''
        account_name = account_data["name"]
        account_description = account_data["description"]
        account_country = account_data["country"]
        return f"{account_name}, who is a {account_description}, from {account_country}"

    def check_answer(guess, a_followers, b_followers):
        '''Checks user guess against follower account and returns if it is correct.'''
        if a_followers > b_followers:
            return guess == "a"
        else:
            return guess == "b"

            # select random accounts
    account_a = random.choice(data)
    account_b = random.choice(data)
    if account_b == account_a:
        account_b = random.choice(data)

    # get follower counts from accounts
    a_followers = int(account_a["follower_count"])
    b_followers = int(account_b["follower_count"])

    # present choices
    print(f"Option A: {format_data(account_a)}")
    print(f"Option B: {format_data(account_b)}")
    guess = input("Who has more Instagram followers? A or B?\n").lower()

    is_correct = check_answer(guess, a_followers, b_followers)

    if is_correct:
        score += 1
        os.system('cls||clear')
        print(
            f"Correct! Your score is now {score}.")
    else:
        os.system('cls||clear')
        print(
            f"Sorry, that is not correct. Your final score was {score}.")
        break
