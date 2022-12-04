"""
Importing required modules
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

answers = SHEET.worksheet('answers')
answer_data = answers.get_all_values()

# print(question_data[1][1])
# print(answer_data[1][1])

science_questions = question_data[1][0], question_data[2][0], question_data[3][0], question_data[4][0], question_data[5][0] # pylint: disable=line-too-long # noqa
sports_questions = question_data[1][1], question_data[2][1], question_data[3][1], question_data[4][1], question_data[5][1] # pylint: disable=line-too-long # noqa
movies_questions = question_data[1][2], question_data[2][2], question_data[3][2], question_data[4][2], question_data[5][2] # pylint: disable=line-too-long # noqa
music_questions = question_data[1][3], question_data[2][3], question_data[3][3], question_data[4][3], question_data[5][3] # pylint: disable=line-too-long # noqa
history_questions = question_data[1][4], question_data[2][4], question_data[3][4], question_data[4][4], question_data[5][4] # pylint: disable=line-too-long # noqa


science_answers = answer_data[1][0], answer_data[2][0], answer_data[3][0], answer_data[4][0], answer_data[5][0] # pylint: disable=line-too-long # noqa
sports_answers = answer_data[1][1], answer_data[2][1], answer_data[3][1], answer_data[4][1], answer_data[5][1] # pylint: disable=line-too-long # noqa
movies_answers = answer_data[1][2], answer_data[2][2], answer_data[3][2], answer_data[4][2], answer_data[5][2] # pylint: disable=line-too-long # noqa
music_answers = answer_data[1][3], answer_data[2][3], answer_data[3][3], answer_data[4][3], answer_data[5][3] # pylint: disable=line-too-long # noqa
history_answers = answer_data[1][4], answer_data[2][4], answer_data[3][4], answer_data[4][4], answer_data[5][4] # pylint: disable=line-too-long # noqa


def start_quiz():
    """
    Function to allow the user to start a new quiz and select a topic
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

    start = input("Would you like to play, Y/N: ").upper()

    print("")

    if start == "Y":
        print(f"1. {question_data[0][0]}")
        print(f"2. {question_data[0][1]}")
        print(f"3. {question_data[0][2]}")
        print(f"4. {question_data[0][3]}")
        print(f"5. {question_data[0][4]}\n")
    else:
        quit()


start_quiz()

topic = input("Choose a topic from 1-5 above: ")


def topic_choice():
    """
    Provide feedback to user after choosing a topic
    """
    if topic == "1":
        print("\nYou have selected " + "'" + question_data[0][0] + "'\n")
    elif topic == "2":
        print("\nYou have selected " + "'" + question_data[0][1] + "'\n")
    elif topic == "3":
        print("\nYou have selected " + "'" + question_data[0][2] + "'\n")
    elif topic == "4":
        print("\nYou have selected " + "'" + question_data[0][3] + "'\n")
    elif topic == "5":
        print("\nYou have selected " + "'" + question_data[0][4] + "'\n")
    else:
        quit()


topic_choice()
