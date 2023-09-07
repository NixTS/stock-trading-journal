from datetime import datetime
from tabulate import tabulate

import time

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
SHEET = GSPREAD_CLIENT.open('trading-journal')

stock_data = SHEET.worksheet('stock_data')

data = stock_data.get_all_values()


def line_break():
    print("__________________________________________________\n")

def handle_input_statistics():
    """
    Gives an option to either get statistics for a number of trades,
    or todays trades or all trades.
    """
    line_break()
    print("Trading statistics\n\n")
    print("If you want to get statistics for your trades, please follow the instructions given to you.\n")
    print("Press '1' on your keyboard to enter a number.")
    print("Or:")
    print("Press '2', if you want to get todays trades.")
    print("Or:")
    print("Press '3', if you want to get all your past trades.\n")

    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            past_num_trades_statistic()
        elif choice == "2":
            todays_num_trades_statistic()
        elif choice == "3":
            all_num_trades_statistic()
        else:
            line_break()
            print("Invalid format, please enter '1' or '2' or '3'.")


def past_num_trades_statistic():
    print("he")

def todays_num_trades_statistic():
    print("today_num_trades_statistic() works")


def all_num_trades_statistic():
    print("all_num_trades_statistic() works")




def main():
    """
    Run all program functions
    """
    past_num_trades_statistic()
    todays_num_trades_statistic()
    all_num_trades_statistic()

main()