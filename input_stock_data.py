from functions import line_break
from sheet_data import *

from datetime import datetime
from tabulate import tabulate

import re
import time
import keyboard

allowed_keys = {'1', '2', 'esc'}

today = datetime.today()
datetoday = today.strftime("%d.%m.%Y")

trading_journal_entry = []

def handle_input_date():
    """
    Shows the current date and asks for input if
    the current date should be used or
    if one wants to input a date manually.
    """

    trading_journal_entry.clear()

    line_break()
    print("Here you can input a new entry to your trading journal.\n")
    print("Please press one of the following buttons on your keyboard to continue:\n")
    print(f"'1' if you want to use the current date: {datetoday}.")
    print("'2' if you want to enter a date manually.\n")
    print("'ESC' if you want to return to the main menu.")

    while True:
        event = keyboard.read_event(suppress=True)
        if event.event_type == keyboard.KEY_UP:
            choice = event.name
            if choice == "1":
                input_date_today()
                break
            elif choice == "2":
                input_date_manually()
                break


def input_date_today():
    """
    If option 1 is selected, prints a message showing the current date
    and append the date to the list.
    """
    line_break()
    print(f"The current date '{datetoday}' has been parsed to your journal.")

    trading_journal_entry.append(datetoday)
    input_ticker()
    

def input_date_manually():
    """
    Enter a date in the format DD.MM.YYYY. 
    Prints a ValueError to the terminal if the wrong format is used, input repeats.
    """
    line_break()
    print("Here you can enter a date manually 'DD.MM.YYYY'.\n" )
    date_str = input("Enter a date: ")

    try:
        date_obj = datetime.strptime(date_str, "%d.%m.%Y")
        line_break()
        print(f"Your input '{datetoday}' has been parsed to your journal.")
        trading_journal_entry.append(date_str)
    except ValueError:
        line_break()
        print(ValueError)
        print("Invalid date or format, please use DD.MM.YYYY format.")
        input_date_manually()


def input_ticker():
    """
    Asks for a stock ticker input, only letters from a - z, A - Z
    and only 1-4 characters are allowed.
    Loop repeats if input was incorrect.
    The ticker will be appended to the list.
    """
    while True:
        line_break()
        ticker = input("Enter ticker: ")

        if re.match(r"^[a-zA-Z]{1,4}$", ticker):
            trading_journal_entry.append(ticker.upper())
            break
        else:
            line_break()
            print("Invalid input, please enter 1 to 4 letters.")


def input_shares_amount():
    """
    Asks for shares traded amount, only numbers are allowed.
    Loop repeats if input was incorrect.
    The shares amount will be appended to the list.
    """
    while True:
        line_break()
        shares_amount = input("Shares amount traded: ")

        if re.match(r"^([\s\d]+)$", shares_amount):
            trading_journal_entry.append(shares_amount)
            break
        else:
            line_break()
            print("Invalid input, please enter a number.")


def input_direction():
    """
    Asks for trade direction, only l L and s S input allowed.
    converts l L = Long and s S = .Short
    Loop repeats if input was incorrect.
    The word Long/Short will be appended to the list.
    """

    while True:
        line_break()
        print("For a long trade please enter 'L'.\n")
        print("For a short short please enter 'S'.\n\n")
        direction = input("Enter trade direction: ")

        if re.match(r"^[lL]$", direction):
            trading_journal_entry.append("Long")
            break
        elif re.match(r"^[sS]$", direction):
            trading_journal_entry.append("Short")        
            break
        else:
            line_break()
            print("Invalid input, please enter 'L' for Long, and 'S' for a short trade.")


def input_prices():
    """
    Asks for entry and exit price, only numbers are allowed.
    Input will be appended to the prices list, prices list will be extended to list.
    Loop repeats if input was incorrect.
    The shares amount will be appended to the list.
    """

    prices = []

    while True:
        line_break()
        print("Enter your entry and exit prices.\n")
        entry_price = input("Enter your trade entry price: ")

        if re.match(r"^([\s\d]+)$", entry_price):
            prices.append(entry_price)
            break
        else:
            line_break()
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
    total_profit_loss = 0

    entry_price = float(trading_journal_entry[4])
    exit_price = float(trading_journal_entry[5])
    num_of_shares = float(trading_journal_entry[2])

    if trading_journal_entry[3] == "Short":
        short_calc_result = (entry_price - exit_price) * num_of_shares
        total_profit_loss += float(short_calc_result)
    else:
        long_calc_result = (exit_price - entry_price) * num_of_shares
        total_profit_loss += float(long_calc_result)

    this_trade_winner_loser = "Winner" if total_profit_loss >= 0 else "Loser"
    this_trade_profit_loss = "Profit" if total_profit_loss >= 0 else "Loss"
    
    line_break()
    print("This is the data you put in:\n")

    table = [
        ["Date:", trading_journal_entry[0]],
        ["Ticker:", trading_journal_entry[1]],
        ["Amount of Shares:", trading_journal_entry[2]],
        ["Direction:", trading_journal_entry[3]],
        ["Entry Price:", "$ " + trading_journal_entry[4]],
        ["Exit Price:", "$ " + trading_journal_entry[5]]
    ]
    print(tabulate(table), "\n")
    print(f"Your trade is a {this_trade_winner_loser}")
    print(f"The total {this_trade_profit_loss} is $ {total_profit_loss:.2f}")

    push_input_to_sheet()


def push_input_to_sheet():
    """
    Input if data is correct "Y", is not correct input "N".
    If data in table is correct, data will be pushed to sheet, process repeats.
    If not, process repeats.
    """
    while True:
        print("\n")
        push_data = input("If this is correct, type 'Y', if you want to restart type 'N'.")

        if re.match(r"^[yY]$", push_data):
            line_break()
            print("Pushing to journal . . .\n")
            stock_data = SHEET.worksheet('stock_data')
            stock_data.append_row(trading_journal_entry)
            time.sleep(2)
            print("Push successful! Your entry is now stored in your trading journal!\n")
            time.sleep(2)
            print("Restarting process . . .\n")
            print("This takes only 5 seconds . . .")
            time.sleep(5)
            main()
            break
        elif re.match(r"^[nN]$", push_data):
            trading_journal_entry.clear()
            main()
            break
        else:
            line_break()
            print("Invalid input, please enter 'Y' to push entry, or 'N' to start over.")

    
def main():
    """
    Run all program functions
    """
    handle_input_date()

if __name__ == "__main__":
    main()