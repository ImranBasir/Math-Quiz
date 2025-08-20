import random

print("——————————Math Quiz——————————")
print()
print("Welcome to the Math Quiz!")
print("You will be given a math problem to solve.")
print("If you get it right, you get a point!")
print("Type, 00000 if you don't know the answer. Remember. Type 0, 5 times.")

while True:
    multiples = int(input("First you choose what multiples you want to test yourself on. "))

    score = 0
    for i in range(1, 11):
        a_number =  random.randint(0, 12)
        correct_answer = multiples * a_number

        print(a_number, "x", multiples)
        answer = int(input("> "))
        if answer == correct_answer:
            print('Correct!')
            score += 1
        elif answer == 00000:
            print(correct_answer)
        else:
            print('Wrong!')
            print(correct_answer)
            continue

    if score == 10:
        print("You got all questions correct! 🏆🏆🥇🙌🙌")
    elif score >= 7:
        print("You got", score, "out of 10 questions correct. Great job! 👍")
    elif score >= 5:
        print("You got", score, "out of 10 questions correct. Not bad! 👌")
    elif score >= 3:
        print("You got", score, "out of 10 questions correct. You can do better! 👎")
    elif score >= 1:
        print("You got", score, "out of 10 questions correct. You need to practice more! 👎👎")
    else:
        print("You got", score, "out of 10 questions correct.")


    playAgain = input("Do you want to play again? (yes/no). ")
    if playAgain.lower() == "no":
        break
    elif playAgain.lower() == "yes":
        continue