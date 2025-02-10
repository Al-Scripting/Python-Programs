from random import randint
from time import time


# This definition converts the unix time into hours, mins and sec
def quizTimerConvert(sec):
    minutes = sec // 60
    sec = sec % 60
    hours = minutes // 60
    minutes = minutes % 60
    print("\nTime Lapsed = {0}:{1}:{2}".format(int(hours), int(minutes), sec))


while True:
    # these are the variables to allow the quiz to happen more than once
    correct = int(0)
    count = int(0)
    totalQuestions = int(5)

    # rules
    print("This is an exponent quiz, Try your best to answer all the question in the shortest time possible\nYou have "
          "1 attempt pre question and your time starts after you press enter"
          "\nGood Luck !!")

    # ask user to start the quiz so that the timer starts when they want
    input("\nPress Enter to Start the Quiz\n>")
    startTime = time()

    # for loop to print and make new questions for the quiz

    print("Quiz has started !")
    for i in range(totalQuestions):

        # generates 2 random integers
        num1 = randint(0, 9)
        num2 = randint(0, 9)

        # prints the question with the question number
        print("\n(", str(i + 1), ") What is ", num1, "**", num2, "?")
        userAns = input("> ")
        userAns = int(userAns)

        # after each question the total question decrease and the count increases
        totalQuestions = totalQuestions - 1
        count = count + 1

        # calculates the right answer form the random intergers
        answer = num1 ** num2

        # checks users answers to see if it is right or wrong
        if userAns != answer:
            print("ou are wrong! Correct answer is ", answer)
        else:
            print("you are correct!")
            correct = correct + 1

    # once all the questions are done the program ends the timer
    endTime = time()
    time_taken = endTime - startTime
    quizTimerConvert(time_taken)

    # displays the time lapsed and the amount of questions answers plus there total score
    print("You have answered ", count, " questions")
    print("\nhe number of points received are ", str(correct), " out of 5")

    # ask user if they want to retake the quiz
    restart = input("Do you want to retake the quiz? Type Y/N\n>").lower()
    if restart == 'n' or restart == 'stop' or restart == 'exit' or restart == 'no':
        print("Take you for taking part of this quiz")
        break
    elif restart == 'y' or restart == 'yes':
        print("")
