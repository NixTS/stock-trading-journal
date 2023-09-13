import keyboard
import re
import time
from colorama import Fore, init
from datetime import datetime, date
from tabulate import tabulate

from functions import line_break, close_script
from sheet_data import *


allowed_keys = {'1', '2', 'y', 'n', 's', 'l', 'esc'}
init(autoreset=True)


today = datetime.today()
datetoday = today.strftime("%d.%m.%Y")

trading_journal_entry = []


def main():
    """
    Welcome message and shows the current date
    """
    line_break()
    print(Fore.YELLOW + "Trading Journal Input\n\n")
    print("Submit a new entry into your trading journal.\n")
    print("Please press one of the following buttons to continue:\n")
    print(f"'1' to use the current date: {datetoday}.")
    print("'2' to enter a date manually.\n")
    print(Fore.RED + "'ESC' to exit the program.")


def handle_input_date():
    """
    Handles key presses to navigate menu
    1: Push current date
    2: Push manually entered date
    ESC: to exit the program; using sys.exit
    """
    main()
    trading_journal_entry.clear()

    while True:
        event = keyboard.read_event(suppress=True)
        if event.event_type == keyboard.KEY_UP:
            choice = event.name

            if choice in allowed_keys:
                if choice == "1":
                    input_date_today()
                    break
                elif choice == "2":
                    input_date_manually()
                    break
                elif choice == 'esc':
                    close_script()
                    break


def input_date_today():
    """
    If option 1 is selected, prints a message showing the current date
    and pushes the current date to the list.
    """
    line_break()
    print(Fore.GREEN + f"The current date '{datetoday}'" +
          "will be parsed to your journal.")

    trading_journal_entry.append(datetoday)
    input_ticker()


def input_date_manually():
    """
    Enter a date in the format DD.MM.YYYY.
    Prints a ValueError to the terminal if,
    the wrong format is used, input repeats.
    """
    line_break()
    print("Please enter a date manually 'DD.MM.YYYY'.\n")
    date_str = input("Date:\n")

    try:
        parsed_date = datetime.strptime(date_str, "%d.%m.%Y").date()
        today = date.today()

        if parsed_date <= today:
            line_break()
            print(Fore.GREEN + f"Your input '{date_str}'" +
                  "will be parsed to your journal.")
            trading_journal_entry.append(parsed_date)
            input_ticker()
        else:
            line_break()
            print(Fore.RED + "Invalid date." +
                  "Please enter a date from today or the past.")
            input_date_manually()
    except ValueError:
        line_break()
        print(Fore.RED + "Invalid date format." +
              "Please use DD.MM.YYYY format.")
        input_date_manually()


def input_ticker():
    """
    Asks for a stock ticker input, only letters from a - z, A - Z
    and only 1-4 characters are allowed.
    Loop repeats if input was incorrectly formatted.
    The ticker will be pushed to the list.
    """
    while True:
        line_break()
        print("Please enter the stock ticker symbol.\n")
        print("Input restricted to 1 - 4 letters.")
        print("Input will be converted to uppercase automatically.\n")
        ticker = input("Ticker Symbol:\n")

        if re.match(r"^[a-zA-Z]{1,4}$", ticker):
            trading_journal_entry.append(ticker.upper())
            line_break()
            print(Fore.GREEN + f"Your input ticker symbol {ticker.upper()}" +
                  "will be parsed to your journal.")
            input_shares_amount()
            break
        else:
            line_break()
            print(Fore.RED + "Invalid input." +
                  "Please enter 1 to 4 letters.")


def input_shares_amount():
    """
    Asks for shares traded amount, only numbers are allowed.
    Loop repeats if input was incorrectly formatted.
    The shares amount will be pushed to the list.
    """
    while True:
        line_break()
        print("Please enter the amount of shares traded.\n")
        print("Input restricted to numbers.\n")
        shares_amount = input("Shares amount traded:\n")

        if re.match(r"^([\s\d]+)$", shares_amount):
            trading_journal_entry.append(shares_amount)
            line_break()
            print(Fore.GREEN + f"Your input of {shares_amount} shares" +
                  "will be parsed to your journal.")
            input_direction()
            break
        else:
            line_break()
            print(Fore.RED + "Invalid input, please enter a number.")


def input_direction():
    """
    Asks for trade direction
    Key press to input
    L = Long
    S = Short
    On key press each word will be pushed respectively
    """
    line_break()
    print("Please enter the direction of your trade.\n")
    print("'L' for a 'long' direction.")
    print("'S' for a short direction.")
    direction_output = " "

    while True:
        event = keyboard.read_event(suppress=True)
        if event.event_type == keyboard.KEY_UP:
            choice = event.name

            if choice in allowed_keys:
                if choice == "l":
                    trading_journal_entry.append("Long")
                    direction_output = "Long"
                    line_break()
                    print(Fore.GREEN + f"Your trade direction of" +
                          "{str(direction_output)}" +
                          "will be parsed to your journal.")
                    input_prices()
                    break
                elif choice == "s":
                    trading_journal_entry.append("Short")
                    direction_output = "Short"
                    line_break()
                    print(Fore.GREEN + f"Your trade direction of" +
                          "{str(direction_output)}" +
                          "will be parsed to your journal.")
                    input_prices()
                    break


def input_prices():
    """
    Asks for entry and exit price
    only numbers are allowed.
    Input will be pushed to the prices list,
    prices list will be extended to list.
    Loop repeats if input was incorrect.
    The shares amount will be pushed to the list.
    """

    prices = []

    while True:
        line_break()
        print("Please enter the entry and exit prices of your trade.\n")
        print("Enter the entry price first.\n")
        print("Input is restricted to numbers only.\n")
        print("For Example: 6.45, 12.00, 293.20")
        entry_price = input("Entry price:\n")

        if re.match(r"^\d+\.\d{2}$", entry_price):
            prices.append(entry_price)
            break
        else:
            line_break()
            print(Fore.RED + "Invalid input." +
                  "Please enter a number with exactly two decimals.")
            print(Fore.RED + "for example: 6.45, 12.00, 293.20")

    while True:
        exit_price = input("Exit price:\n")

        if re.match(r"^\d+\.\d{2}$", exit_price):
            prices.append(exit_price)
            break
        else:
            line_break()
            print(Fore.RED + "Invalid input." +
                  "Please enter a number with exactly two decimals.")
            print(Fore.RED + "for example: 6.45, 12.00, 293.20")

    line_break()
    print(Fore.GREEN + f"Your input of entry price $ {entry_price}" +
          "and exit price $ {exit_price} will be parsed to your journal.")
    trading_journal_entry.extend(prices)
    show_input()


def show_input():
    """
    After successful input of all entries
    overview in form of a table will be displayed.
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

    this_trade_winner_loser = (
        Fore.GREEN + "Winner"
        ) if total_profit_loss >= 0 else (
        Fore.RED + "Loser"
        )
    this_trade_profit_loss = "Profit" if total_profit_loss >= 0 else "Loss"

    line_break()
    print("This is your input:\n")

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
    print(f"The total {this_trade_profit_loss} is $ {total_profit_loss:.2f}\n")

    push_input_to_sheet()


def push_input_to_sheet():
    """
    Input if data is correct "Y", is not correct input "N".
    If data in table is correct, data will be pushed to sheet, process repeats.
    If not, process repeats.
    """
    print("If this is correct, press 'Y', if you want to restart press 'N'.")
    while True:
        event = keyboard.read_event(suppress=True)
        if event.event_type == keyboard.KEY_UP:
            choice = event.name

            if choice in allowed_keys:
                if choice == 'y':
                    line_break()
                    print(Fore.GREEN + "Pushing to journal . . .\n")
                    stock_data = SHEET.worksheet('stock_data')
                    stock_data.append_row(trading_journal_entry)
                    time.sleep(2)
                    print(Fore.GREEN + "Push successful!" +
                          "Your entry is stored in your trading journal!\n")
                    line_break()
                    time.sleep(2)
                    print("Restarting process . . .\n")
                    print("This takes only 5 seconds . . .")
                    sort_sheet_by_date()
                    break
                elif choice == 'n':
                    line_break()
                    print(Fore.RED + "Push declined!" +
                          "Your entry will be deleted!\n")
                    line_break()
                    time.sleep(2)
                    print("Restarting process . . .\n")
                    print("This takes only 5 seconds . . .")
                    time.sleep(5)
                    main()
                    break


def sort_sheet_by_date():
    """
    After successfully pushing the data to the sheet
    sheet will be sorted by date
    in case an older date was pushed
    """
    headers = data[0]
    stock_data.sort((headers.index("Date") + 1, 'asc'))
    time.sleep(5)
    main()


if __name__ == "__main__":
    main()
    handle_input_date()
