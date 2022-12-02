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

def start_quiz():
    """
    Function to allow the user to start a new quiz and select a topic
    """
    print("\n-------------------------------------------------------------------------------------------------------------------------------------------------")
    print(" _______  __   __  _______    _______  __   __  ___   _______    _______  __   __  _______  ___      ___      _______  __    _  _______  _______ ")
    print("|       ||  | |  ||  _    |  |       ||  | |  ||   | |       |  |    ___||  | |  ||   _   ||   |    |   |    |       ||  |  | ||       ||       |")
    print("|    _  ||  | |  || |_|   |  |   _   ||  | |  ||   | |____   |  |   /    |  |_|  ||  |_|  ||   |    |   |    |    ___||   |_| ||    ___||    ___|")
    print("|   |_| ||  |_|  ||       |  |  | |  ||  |_|  ||   |  ____|  |  |  |     |       ||       ||   |    |   |    |   |___ |       ||   | __ |   |___ ")
    print("|    ___||       ||  _   |   |  |_|  ||       ||   | | ______|  |  |     |   _   ||   _   ||   |___ |   |___ |    ___||  _    ||   ||  ||    ___|")
    print("|   |    |       || |_|   |  |      | |       ||   | | |_____   |   \___ |  | |  ||  | |  ||       ||       ||   |___ | | |   ||   |_| ||   |___ ")
    print("|___|    |_______||_______|  |____||_||_______||___| |_______|  |_______||__| |__||__| |__||_______||_______||_______||_|  |__||_______||_______|\n")
    print("-------------------------------------------------------------------------------------------------------------------------------------------------")
    print("")

    start = input("Would you like to play? Type Y/N: ").upper()

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

topic_choice = input("Choose a topic from 1-5 above: ")