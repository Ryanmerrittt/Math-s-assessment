# main routine starts here
import random



def int_check(question):
    while True:
        error = "please enter a number that is 1 or more."
        to_check = input(question)

        try:
            response = int(to_check)
            if response < 1:
                print(error)
            else:
                return response
        except ValueError:
            print(error)




def yes_no(question):
    while True:
        response = input(question).lower()
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes / no")


def instructions():
    print("""
   *** Instructions ****

This is an addition maths quiz.

You will enter the number of questions you want to do.

Then you will try and complete as many questions as you can.

Good luck!
    """)




# Start of program
print("➕➕ Addition maths quiz! ➕➕ ")
print()

# instructions stuff
want_instructions = yes_no("Do you want to see the instructions? ")

if want_instructions == "yes":
    instructions()

# round stuff
mode = "regular"
rounds_played = 1
rounds_lost = 0
game_history = []

# checks how many rounds users want
num_rounds = int_check("How many questions would you like? ")

# Game loop starts here
while rounds_played <= num_rounds:
    print(f"\n💿💿💿 Question {rounds_played} of {num_rounds} 💿💿💿\n")


    # addition variables
    num1 = random.randint(1, 30)
    num2 = random.randint(1, 30)

    # addition questions
    math_question = int_check(f"What is {num1} + {num2}? = ")
    answer = num1 + num2

    # if user enters (Y) or (N)
    # check if users answer is correct
    if math_question == answer:
        print("✔️✔️✔️ You got it correct! ✔️✔️✔️")
        result = "✔️You got it correct! ✔️"
    else:
        print("❌❌❌ You got it incorrect ❌❌❌")
        result = "❌You got it incorrect❌"
        rounds_lost += 1

    # round feedback
    round_feedback = f"{math_question} vs {answer}, {result}"
    history_item = f"Round: {rounds_played} - {round_feedback}"
    print(round_feedback)

    game_history.append(history_item)
    rounds_played += 1


# Game summary
if len(game_history) > 0:
    rounds_won = num_rounds - rounds_lost
    print("\n📊📊📊 Game Statistics 📊📊📊")
    print(f"👍 Correct: {rounds_won} \t 👎 Incorrect: {rounds_lost}")

    # see game history stuff
    see_history = yes_no("\nDo you want to see your game history? ")
    if see_history == "yes":
        for item in game_history:
            print(item)

    # end of game text
    print("\nThanks for playing!")
else:
    print("🐔🐔🐔 Oops - You chickened out! 🐔🐔🐔")

