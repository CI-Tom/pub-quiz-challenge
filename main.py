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


def start_new_quiz():
    pass


def check_correct_answer():
    pass


def player_score():
    pass


def play_again():
    pass


science = {
    question_data[1][0]: answer_a_data[1][0],
    question_data[2][0]: answer_c_data[2][0],
    question_data[3][0]: answer_b_data[3][0],
    question_data[4][0]: answer_a_data[4][0],
    question_data[5][0]: answer_c_data[5][0]
}

sports = {
    question_data[1][1]: answer_b_data[1][1],
    question_data[2][1]: answer_b_data[2][1],
    question_data[3][1]: answer_c_data[3][1],
    question_data[4][1]: answer_a_data[4][1],
    question_data[5][1]: answer_a_data[5][1],
}

movies_tv = {
    question_data[1][2]: answer_b_data[1][2],
    question_data[2][2]: answer_a_data[2][2],
    question_data[3][2]: answer_c_data[3][2],
    question_data[4][2]: answer_b_data[4][2],
    question_data[5][2]: answer_c_data[5][2],
}

music = {
    question_data[1][3]: answer_b_data[1][3],
    question_data[2][3]: answer_b_data[2][3],
    question_data[3][3]: answer_b_data[3][3],
    question_data[4][3]: answer_a_data[4][3],
    question_data[5][3]: answer_c_data[5][3],
}

history = {
    question_data[1][4]: answer_c_data[1][4],
    question_data[2][4]: answer_a_data[2][4],
    question_data[3][4]: answer_b_data[3][4],
    question_data[4][4]: answer_a_data[4][4],
    question_data[5][4]: answer_b_data[5][4],
}

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
