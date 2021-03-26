# user guess random number
# if incorrect, hint is given and score is reduce

import random
attempted = []

def score():
    if len(attempted) <= 0:
        print("No high score yet")
    else:
        print("The current high score is {} attempts".format(min(attempted)))

def start():
    random_number = int(random.randint(1,50))
    print("Lets play!")
    name = input("what is your name?")
    want_to_play = input("Would you like to play? yes/no")
    attempts = 0
    score()

    while want_to_play =="yes":
        guess = input("pick a number between 1 and 50: ")
        if int(guess) <1 or int(guess) > 50:
            print("please give a number within range")
        if int(guess) == random_number:
            print("Correct answer!")
            attempts += 1
            attempted.append(attempts)
            print("it took you {} attempts".format(attempts))
            play_again = input("Would you like to play again? yes/no")

            attempts = 0
            score()
            random_number = int(random.randint(1,50))
            if play_again == "no":
                print("Goodbye")
                break
        elif int(guess) > random_number:
            print("the number is lower")
            attempts += 1
        elif int(guess) < random_number:
            print("the number is higher")
            attempts += 1
    else:
        print("Goodbye")

if __name__ =='__main__':
    start()

