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


def past_num_trades_statistic():
    print("past_num_trades_statistic() works")

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