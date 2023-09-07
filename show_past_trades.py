from functions import line_break
from sheet_data import *

from datetime import datetime
from tabulate import tabulate

import re
import time


def handle_input_past_trades():
    """
    Gives an option to either view a certain number of trade,
    todays trades, or all past trades.
    """
    line_break()
    print("Trading journal\n\n")
    print("If you want to display your past trades, please follow the instructions given to you.\n")
    print("Press '1' on your keyboard to enter a number.")
    print("Or:")
    print("Press '2', if you want see todays trades.")
    print("Or:")
    print("Press '3', if you want see all your past trades.\n")

    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            num_of_trades()
        elif choice == "2":
            todays_trades()
        elif choice == "3":
            all_trades()
        else:
            line_break()
            print("Invalid format, please enter '1' or '2' or '3'.")

def num_of_trades():
    """
    Enter a number to display past trades.
    If the number is higher than all past trades,
    an error message will appear with the number of all past trades
    """
    line_break()
    num_of_past_trades = input("Enter the number of last trades to display: \n")

    try:
        num_of_past_trades = int(num_of_past_trades)
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    total_rows_with_data = sum(1 for row in data if any(row))

    if num_of_past_trades <= 0:
        print("Invalid input. Please enter a positive number.")
        return

    if num_of_past_trades > total_rows_with_data:
        line_break()
        print(f"Requested {num_of_past_trades} rows, but there are only {total_rows_with_data} rows with data.")
        num_of_trades()

    line_break()
    headers = stock_data.row_values(1)
    last_n_rows = [row for row in reversed(data) if any(row)][:num_of_past_trades]

    print(f"Here you can see your past {num_of_past_trades} trades:\n")
    if num_of_past_trades <= total_rows_with_data:
        print(tabulate(last_n_rows, headers, tablefmt="github"))
        print("\n")

    while True:
        print("Press '1' to enter another number of past trades.")
        print("Or:")
        print("Press '2' to go back to the past trades menu.\n")
        choice = input("Enter your choice: ")
        if choice == "1":
            num_of_trades()
        elif choice == "2":
            handle_input_past_trades()
        else:
            line_break()
            print("Invalid format, please enter '1' or '2'.")


def todays_trades():
    """
    Display all past trades with today's date.
    """
    today_date_str = datetime.now().strftime('%d.%m.%Y')

    filtered_rows = [row for row in data if any(row) and row[0] == today_date_str]

    if not filtered_rows:
        print("No trades with today's date found.")
        return
    
    line_break()
    headers = stock_data.row_values(1)

    print("Here you can see all trades from today:\n")
    print(tabulate(filtered_rows, headers, tablefmt="github"))
    print("\n")
    
    while True:
        print("Press '1' to go back to the past trades menu.\n")
        choice = input("Enter your choice: ")
        if choice == "1":
            handle_input_past_trades()
        else:
            line_break()
            print("Invalid format, please enter '1'.")


def all_trades():
    """
    Display all trades in google sheet without header row.
    """
    headers = stock_data.row_values(1)
    all_rows = list(data)

    if all_rows and all_rows[0] == headers:
        all_rows.pop(0)

    line_break()
    print("Here you can see all your past trades:\n")
    print("This may take a while . . .\n")
    time.sleep(2)
    print(tabulate(all_rows, headers, tablefmt="github"))
    print("\n")

    while True:
        print("Press '1' to go back to the past trades menu.\n")
        choice = input("Enter your choice: ")
        if choice == "1":
            handle_input_past_trades()
        else:
            line_break()
            print("Invalid format, please enter '1'.")


def main():
    """
    Run all program functions
    """
    handle_input_past_trades()

if __name__ == "__main__":
    main()