"""
Import required modules
"""
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('pub_quiz_challenge')

questions = SHEET.worksheet('questions')
question_data = questions.get_all_values()

answers_a = SHEET.worksheet('answers_a')
answer_a_data = answers_a.get_all_values()

answers_b = SHEET.worksheet('answers_b')
answer_b_data = answers_b.get_all_values()

answers_c = SHEET.worksheet('answers_c')
answer_c_data = answers_c.get_all_values()

leaderboard = SHEET.worksheet('leaderboard')
leaderboard_data = leaderboard.get_all_values()


# Create dictionaries to contain questions and correct answer pairs for topics
science = {
    question_data[1][0]: "A",
    question_data[2][0]: "C",
    question_data[3][0]: "B",
    question_data[4][0]: "A",
    question_data[5][0]: "C"
}

sports = {
    question_data[1][1]: "B",
    question_data[2][1]: "B",
    question_data[3][1]: "C",
    question_data[4][1]: "A",
    question_data[5][1]: "A",
}

movies_tv = {
    question_data[1][2]: "B",
    question_data[2][2]: "A",
    question_data[3][2]: "C",
    question_data[4][2]: "A",
    question_data[5][2]: "C",
}

music = {
    question_data[1][3]: "B",
    question_data[2][3]: "B",
    question_data[3][3]: "B",
    question_data[4][3]: "A",
    question_data[5][3]: "C",
}

history = {
    question_data[1][4]: "C",
    question_data[2][4]: "A",
    question_data[3][4]: "B",
    question_data[4][4]: "A",
    question_data[5][4]: "B",
}

# Create lists with embedded lists of possible answers from worksheet
science_choices = [
    [answer_a_data[1][0], answer_b_data[1][0], answer_c_data[1][0]],
    [answer_a_data[2][0], answer_b_data[2][0], answer_c_data[2][0]],
    [answer_a_data[3][0], answer_b_data[3][0], answer_c_data[3][0]],
    [answer_a_data[4][0], answer_b_data[4][0], answer_c_data[4][0]],
    [answer_a_data[5][0], answer_b_data[5][0], answer_c_data[5][0]]
]

sports_choices = [
    [answer_a_data[1][1], answer_b_data[1][1], answer_c_data[1][1]],
    [answer_a_data[2][1], answer_b_data[2][1], answer_c_data[2][1]],
    [answer_a_data[3][1], answer_b_data[3][1], answer_c_data[3][1]],
    [answer_a_data[4][1], answer_b_data[4][1], answer_c_data[4][1]],
    [answer_a_data[5][1], answer_b_data[5][1], answer_c_data[5][1]]
]

movies_tv_choices = [
    [answer_a_data[1][2], answer_b_data[1][2], answer_c_data[1][2]],
    [answer_a_data[2][2], answer_b_data[2][2], answer_c_data[2][2]],
    [answer_a_data[3][2], answer_b_data[3][2], answer_c_data[3][2]],
    [answer_a_data[4][2], answer_b_data[4][2], answer_c_data[4][2]],
    [answer_a_data[5][2], answer_b_data[5][2], answer_c_data[5][2]]
]

music_choices = [
    [answer_a_data[1][3], answer_b_data[1][3], answer_c_data[1][3]],
    [answer_a_data[2][3], answer_b_data[2][3], answer_c_data[2][3]],
    [answer_a_data[3][3], answer_b_data[3][3], answer_c_data[3][3]],
    [answer_a_data[4][3], answer_b_data[4][3], answer_c_data[4][3]],
    [answer_a_data[5][3], answer_b_data[5][3], answer_c_data[5][3]]
]

history_choices = [
    [answer_a_data[1][4], answer_b_data[1][4], answer_c_data[1][4]],
    [answer_a_data[2][4], answer_b_data[2][4], answer_c_data[2][4]],
    [answer_a_data[3][4], answer_b_data[3][4], answer_c_data[3][4]],
    [answer_a_data[4][4], answer_b_data[4][4], answer_c_data[4][4]],
    [answer_a_data[5][4], answer_b_data[5][4], answer_c_data[5][4]]
]


def select_topic():
    """
    Allow user to select topic from options provided
    """
    answers = []
    correct_answers = 0
    num_question = 1

    print(f"1. {question_data[0][0]}")
    print(f"2. {question_data[0][1]}")
    print(f"3. {question_data[0][2]}")
    print(f"4. {question_data[0][3]}")
    print(f"5. {question_data[0][4]}\n")

    selection = input("Enter 1, 2, 3, 4 or 5 to start: \n")

    if selection == "1":
        print("\nYou have selected "+"'"+question_data[0][0]+"', let's begin!")

        for key in science:
            print("--------------------------------------------------------\n")
            print(key)
            for i in science_choices[num_question-1]:
                print("")
                print(i)

            choice = input("Enter you answer (A, B or C): \n").upper()
            answers.append(choice)

            correct_answers += check_answer(science.get(key), choice)
            num_question += 1

        player_score(correct_answers, answers)

    elif selection == "2":
        print("\nYou have selected "+"'"+question_data[0][1]+"', let's begin!")

        for key in sports:
            print("--------------------------------------------------------\n")
            print(key)
            for i in sports_choices[num_question-1]:
                print("")
                print(i)

            choice = input("Enter you answer (A, B or C): \n").upper()
            answers.append(choice)

            correct_answers += check_answer(sports.get(key), choice)
            num_question += 1

        player_score(correct_answers, answers)

    elif selection == "3":
        print("\nYou have selected "+"'"+question_data[0][2]+"', let's begin!")

        for key in movies_tv:
            print("--------------------------------------------------------\n")
            print(key)
            for i in movies_tv_choices[num_question-1]:
                print("")
                print(i)

            choice = input("Enter you answer (A, B or C): \n").upper()
            answers.append(choice)

            correct_answers += check_answer(movies_tv.get(key), choice)
            num_question += 1

        player_score(correct_answers, answers)

    elif selection == "4":
        print("\nYou have selected "+"'"+question_data[0][3]+"', let's begin!")

        for key in music:
            print("--------------------------------------------------------\n")
            print(key)
            for i in music_choices[num_question-1]:
                print("")
                print(i)

            choice = input("Enter you answer (A, B or C): \n").upper()
            answers.append(choice)

            correct_answers += check_answer(music.get(key), choice)
            num_question += 1

        player_score(correct_answers, answers)

    elif selection == "5":
        print("\nYou have selected "+"'"+question_data[0][4]+"', let's begin!")

        for key in history:
            print("--------------------------------------------------------\n")
            print(key)
            for i in history_choices[num_question-1]:
                print("")
                print(i)

            choice = input("Enter you answer (A, B or C): \n").upper()
            answers.append(choice)

            correct_answers += check_answer(history.get(key), choice)
            num_question += 1

        player_score(correct_answers, answers)

    else:
        print("\nYou entered an incorrect value.Please try again.\n")
        select_topic()


def start_new_quiz():
    """
    Player must enter their first name and select a topic to begin
    """

    print("\n--------------------------------------------------------------")
    print(" _______  __   __  _______    _______  __   __  ___   _______ ")
    print("|       ||  | |  ||  _    |  |       ||  | |  ||   | |       |")
    print("|    _  ||  | |  || |_|   |  |   _   ||  | |  ||   | |____   |")
    print("|   |_| ||  |_|  ||       |  |  | |  ||  |_|  ||   |  ____|  |")
    print("|    ___||       ||  _   |   |  |_|  ||       ||   | | ______|")
    print("|   |    |       || |_|   |  |      | |       ||   | | |_____ ")
    print("|___|    |_______||_______|  |____||_||_______||___| |_______|\n")
    print("--------------------------------------------------------------")
    print("")

    player_name()

    select_topic()


def player_name():
    """
    Allows user to enter their first name at start of quiz
    """
    while True:
        player = input("Welcome to Pub Quiz! Enter your first name to start: ")
        print()
        player = player.capitalize()

        if not player.isalpha():
            print("You must enter a name using only letters. \n")
            continue
        else:
            print(f"\nHi {player}, please choose a topic below: \n")
            break


def check_answer(answer, choice):
    """
    Checks answer and provides feedback for correct and incorrect answers
    """
    if answer == choice:
        print("You are correct!")
        return 1
    else:
        print()
        print("Sorry, you are wrong! The correct answer is " + answer)
        return 0


def player_score(correct_answers, answers):
    """
    Displays score in percent format by checking number of correct answers
    against number of questions
    """
    print("\n------------------------------------------------------\n")

    score = int((correct_answers/len(answers)) * 100)
    print("You scored: " + str(score) + "%\n")


def play_again():
    """
    Allows player to play another game and select a different topic
    """
    replay = input("\nWould you like to play again? Enter Y / N: \n").upper()

    if replay == "Y":
        return True
    else:
        return False


def main():
    """
    Main function to run quiz
    """
    start_new_quiz()

    while play_again():
        start_new_quiz()

    print("\nOK Goodbye. Thanks for Playing!\n")


main()
