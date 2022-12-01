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

# questions = SHEET.worksheet('questions')
# answers = SHEET.worksheet('answers')

# question_data = questions.get_all_values()
# answer_data = answers.get_all_values()

# print(question_data[1])
# print(answer_data[1])

def start_quiz():
    """
    Start screen with option to start quiz
    """
    print("")
    print(" _______  __   __  _______    _______  __   __  ___   _______    _______  __   __  _______  ___      ___      _______  __    _  _______  _______")
    print("|       ||  | |  ||  _    |  |       ||  | |  ||   | |       |  |    ___||  | |  ||   _   ||   |    |   |    |       ||  |  | ||       ||       |")
    print("|    _  ||  | |  || |_|   |  |   _   ||  | |  ||   | |____   |  |   /    |  |_|  ||  |_|  ||   |    |   |    |    ___||   |_| ||    ___||    ___|")
    print("|   |_| ||  |_|  ||       |  |  | |  ||  |_|  ||   |  ____|  |  |  |     |       ||       ||   |    |   |    |   |___ |       ||   | __ |   |___")
    print("|    ___||       ||  _   |   |  |_|  ||       ||   | | ______|  |  |     |       ||       ||   |___ |   |___ |    ___||  _    ||   ||  ||    ___|")
    print("|   |    |       || |_|   |  |      | |       ||   | | |_____   |   \___ |   _   ||   _   ||       ||       ||   |___ | | |   ||   |_| ||   |___ ")
    print("|___|    |_______||_______|  |____||_||_______||___| |_______|  |_______||__| |__||__| |__||_______||_______||_______||_|  |__||_______||_______|")
    print("")

start_quiz()