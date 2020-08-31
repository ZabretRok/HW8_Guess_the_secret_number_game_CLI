import datetime
import json
import random



player = input("Hi, what is your name? ")

def play_game():
    secret = random.randint(1, 30)
    attempts = 0
    score_list = get_score_list()
    wrong_guesses = []

    while True:
        guess = int(input("Guess the secret number (between 1 and 30): "))
        attempts += 1

        if guess == secret:
            score_list.append({"player_name": player, "attempts": attempts, "date": str(datetime.datetime.now()), "secret_number": secret, "wrong_guesses": wrong_guesses})
            with open("score_list.txt", "w") as score_file:
                score_file.write(json.dumps(score_list))

            print("You've guessed it - congratulations! It's number " + str(secret))
            print("Attempts needed: " + str(attempts))
            break
        elif guess > secret:
            print("Your guess is not correct... try something smaller")
        elif guess < secret:
            print("Your guess is not correct... try something bigger")
        wrong_guesses.append(guess)

        class Result():
            def __init__(self, score, player_name, date):
                self.score = str(attempts+1)
                self.player_name = player
                self.date = str(datetime.datetime.now())

        new_result = Result(score = str(attempts), player_name=player, date=str(datetime.datetime.now()))

        with open("results.txt", "w") as result_file:
            result_file.write(json.dumps(str(new_result.__dict__)))

def get_score_list():
    with open("score_list.txt", "r") as score_file:
        score_list = json.loads(score_file.read())
        return score_list


def get_top_scores():
    score_list = get_score_list()
    top_3 = sorted(score_list, key=lambda x: x['attempts'])[:3]
    return top_3

while True:
    selection = input("Would you like to A) play a new game, B) see the best scores, or C) quit? ")

    if selection.upper() == "A":
        play_game()
    elif selection.upper() == "B":
        for score_dict in get_top_scores():
            print("Player: " + score_dict.get("player_name") + ", attempts: " + str(
            score_dict.get("attempts")) + ", date: " + score_dict.get("date") + ", number was " + str(
            score_dict.get("secret_number"))
              + ". These were the wrong guesses: " + str(score_dict.get("wrong_guesses")))
    else:
        break




