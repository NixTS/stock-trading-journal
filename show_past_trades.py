import time
from colorama import Fore, init
from datetime import datetime
from tabulate import tabulate

from functions import line_break, close_script, back_to_menu
from sheet_data import *

init(autoreset=True)


def main():
    """
    Welcome message and navigation overview
    """
    line_break()
    print(Fore.YELLOW + "Trading Journal\n\n")
    print("Display your past Trades.\n")
    print("Please enter one of the following options to continue:\n")
    print("'1' to display a number of past trades.")
    print("'2' to display todays trades.")
    print("'3' to display all past trades.\n")


def handle_input_past_trades():
    """
    Handles key presses to navigate menu
    1: Enter number of past trades to display
    2: Display todays trades
    3: Display all past trades
    ESC: to exit the program; using sys.exit
    """
    main()

    allowed_keys = {'1', '2', '3'}

    while True:
        choice = input("Enter Option: \n").lower()

        if choice in allowed_keys:
            if choice == '1':
                num_of_trades()
            elif choice == '2':
                todays_trades()
            elif choice == '3':
                all_trades()
        else:
            line_break()
            print(Fore.RED + "Please enter a valid option.")
            print(Fore.RED + "1, 2 or 3")
            main()


def num_of_trades():
    """
    Enter a number to display past trades.
    If the number is higher than all past trades,
    an error message will appear with the number of all past trades
    Instead shows all past trades.
    """
    line_break()
    print("Display your past trades.\n")
    num_of_past_trades = input("Number of past trades: \n")
    total_rows_with_data = sum(1 for row in data if any(row))

    try:
        num_of_past_trades = int(num_of_past_trades)
    except ValueError:
        line_break()
        print(Fore.RED + "Invalid input. Please enter a number.")
        num_of_trades()

    if num_of_past_trades <= 0:
        line_break()
        print(Fore.RED + "Invalid input. Please enter a positive number.")
        num_of_trades()

    if num_of_past_trades > total_rows_with_data:
        line_break()
        print(Fore.RED + f"Requested {num_of_past_trades} rows," +
              f" but there are only {total_rows_with_data}" +
              " rows with data.\n")
        print(Fore.RED + "Here are all past trades instead.")
        all_trades()

    line_break()
    headers = stock_data.row_values(1)
    last_n_rows = [
        row for row in reversed(data[1:])
        if any(row)
        ][:num_of_past_trades]

    print(f"Your past {num_of_past_trades} trades:\n")
    if num_of_past_trades <= total_rows_with_data:
        print(
            tabulate(last_n_rows, headers, tablefmt="github", floatfmt=".2f")
        )
        print("\n")
    back_to_menu()
    handle_input_past_trades()


def todays_trades():
    """
    Display all past trades with today's date.
    """
    today_date_str = datetime.now().strftime('%d.%m.%Y')

    filtered_rows = [
        row for row in data if any(row) and row[0] == today_date_str
    ]

    if not filtered_rows:
        print(Fore.RED + "No trades with today's date found.")
        handle_input_past_trades()

    line_break()
    headers = stock_data.row_values(1)

    print("All trades with todays date:\n")
    print(tabulate(filtered_rows, headers, tablefmt="github", floatfmt=".2f"))
    print("\n")
    back_to_menu()
    handle_input_past_trades()


def all_trades():
    """
    Display all trades in google sheet.
    """
    headers = stock_data.row_values(1)
    all_rows = list(data[1:])

    if all_rows and all_rows[0] == headers:
        all_rows.pop(0)

    line_break()
    print("All your past trades:\n")
    print("This may take a while . . .\n")
    time.sleep(2)
    print(tabulate(all_rows, headers, tablefmt="github", floatfmt=".2f"))
    print("\n")
    back_to_menu()
    handle_input_past_trades()


if __name__ == "__main__":
    main()
    handle_input_past_trades()
