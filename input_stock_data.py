from datetime import datetime
from tabulate import tabulate

import re
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


today = datetime.today()
datetoday = today.strftime("%d.%m.%Y")

trading_journal_entry = []



def handle_input_date():
    """
    Shows the current date and asks for input if
    the current date should be used or
    if one wants to input a date manually.
    """
    print(f"Today is the {datetoday}. If you want to enter this date:\n")
    print("press '1' on your keyboard.")
    print("Or:")
    print("press '2', if you want to enter a date manually.\n")

    
    while True:
        choice = input("Enter your choice:")
        if choice == "1":
            input_date_today()
            break
        elif choice == "2":
            input_date_manually()
            break
        else:
            print("Invalid format, please enter '1' or '2'.")


def input_date_today():
    """
    If option 1 is selected, prints a message showing the current date
    and append the date to the list.
    """
    print(f"The current date '{datetoday}' has been parsed to your journal.")

    trading_journal_entry.append(datetoday)
    

def input_date_manually():
    """
    Enter a date in the format DD.MM.YYYY. 
    Prints a ValueError to the terminal if the wrong format is used, input repeats.
    """
    date_str = input("Enter a date (DD.MM.YYYY): ")

    try:
        date_obj = datetime.strptime(date_str, "%d.%m.%Y")
        print(f"Your input '{datetoday}' has been parsed to your journal.")
    except ValueError:
        print("Invalid date format, please use DD.MM.YYYY format.")
    
    trading_journal_entry.append(date_str)


def input_ticker():
    """
    Asks for a stock ticker input, only letters from a - z, A - Z
    and only 1-4 characters are allowed.
    Loop repeats if input was incorrect.
    The ticker will be appended to the list.
    """
    while True:
        ticker = input("Enter ticker: ")

        if re.match(r"^[a-zA-Z]{1,4}$", ticker):
            break
        else:
            print("Invalid input, please enter 1 to 4 letters.")

    trading_journal_entry.append(ticker)


def input_shares_amount():
    """
    Asks for shares traded amount, only numbers are allowed.
    Loop repeats if input was incorrect.
    The shares amount will be appended to the list.
    """
    while True:
        shares_amount = input("Shares amount traded: ")

        if re.match(r"^([\s\d]+)$", shares_amount):
            break
        else:
            print("Invalid input, please enter a number.")

    trading_journal_entry.append(shares_amount)


def input_direction():
    """
    Asks for trade direction, only l L and s S input allowed.
    converts l L = Long and s S = .Short
    Loop repeats if input was incorrect.
    The word Long/Short will be appended to the list.
    """
    print("For a long trade please enter 'L'.")
    print("For a short short please enter 'S'.")

    while True:
        direction = input("Enter trade direction: ")

        if re.match(r"^[lL]$", direction):
            trading_journal_entry.append("Long")
            break
        elif re.match(r"^[sS]$", direction):
            trading_journal_entry.append("Short")        
            break
        else:
            print("Invalid input, please enter 'L' for Long, and 'S' for a short trade.")


def input_prices():
    """
    Asks for entry and exit price, only numbers are allowed.
    Input will be appended to the prices list, prices list will be extended to list.
    Loop repeats if input was incorrect.
    The shares amount will be appended to the list.
    """
    print("Enter your entry and exit prices.")

    prices = []

    while True:
        entry_price = input("Enter your trade entry price: ")

        if re.match(r"^([\s\d]+)$", entry_price):
            prices.append(entry_price)
            break
        else:
            print("Invalid input, please enter a number.")

    while True:
        exit_price = input("Enter your trade exit price: ")

        if re.match(r"^([\s\d]+)$", exit_price):
            prices.append(exit_price)
            break
        else:
            print("Invalid input, please enter a number.")

    trading_journal_entry.extend(prices)


def show_input():
    """
    After successful input of all entries and overview
    in form of a table will be displayed.
    """
    print("This is the data you put in:")

    table = [["Date:", trading_journal_entry[0]],["Ticker:", trading_journal_entry[1]],["Amount of Shares:", trading_journal_entry[2]],["Direction:", trading_journal_entry[3]],["Entry Price:", "$ " + trading_journal_entry[4]],["Exit Price:", "$ " + trading_journal_entry[5]]]
    print(tabulate(table))

    push_input_to_sheet()


def push_input_to_sheet():
    """
    Input if data is correct "Y", is not correct input "N".
    If data in table is correct, data will be pushed to sheet, process repeats.
    If not, process repeats.
    """
    while True:
        push_data = input("If this is correct, type 'Y', if you want to restart type 'N'.")

        if re.match(r"^[yY]$", push_data):
            print("Pushing to journal . . .\n")
            stock_data = SHEET.worksheet('stock_data')
            stock_data.append_row(trading_journal_entry)
            time.sleep(1)
            print("Push successful! Your entry is now stored in your trading journal!\n")
            time.sleep(1)
            print("Restarting process . . .\n")
            time.sleep(1)
            main()
            break
        elif re.match(r"^[nN]$", direction):
            main()
            break
        else:
            print("Invalid input, please enter 'Y' to push entry, or 'N' to start over.")

    
def main():
    """
    Run all program functions
    """
    handle_input_date()
    input_ticker()
    input_shares_amount()
    input_direction()
    input_prices()
    show_input()


print("Please input your stock trading data by following the instructions given to you.\n")
main()