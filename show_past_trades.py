import keyboard
import time
from functions import line_break, close_script
from sheet_data import *
from datetime import datetime
from tabulate import tabulate


allowed_keys = {'1', '2', 'y', 'n', 'esc'}


def main():
    """
    Welcome message and navigation overview
    """
    line_break()
    print("Trading journal\n\n")
    print("If you want to display your past trades, please follow the instructions given to you.\n")
    print("Press '1' on your keyboard to enter a number.")
    print("Or:")
    print("Press '2', if you want see todays trades.")
    print("Or:")
    print("Press '3', if you want see all your past trades.\n")


def handle_input_past_trades():
    """
    Gives an option to either view a certain number of trade,
    todays trades, or all past trades.
    """
    main()
    while True:
        event = keyboard.read_event(suppress=True)
        if event.event_type == keyboard.KEY_UP:
            choice = event.name
            if choice == "1":
                num_of_trades()
                break
            elif choice == "2":
                todays_trades()
                break
            elif choice == "3":
                all_trades()
            elif choice == 'esc':
                close_script()


def num_of_trades():
    """
    Enter a number to display past trades.
    If the number is higher than all past trades,
    an error message will appear with the number of all past trades
    """
    line_break()
    print("Here you can display your past trades.\n")
    num_of_past_trades = input("Enter the number of past trades: ")

    try:
        num_of_past_trades = int(num_of_past_trades)
    except ValueError:
        line_break()
        print("Invalid input. Please enter a number.")
        num_of_trades()

    total_rows_with_data = sum(1 for row in data if any(row))

    if num_of_past_trades <= 0:
        line_break()
        print("Invalid input. Please enter a positive number.")
        num_of_trades()

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

    print("Returning to main menu.")
    time.sleep(2)
    main()


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
    
    print("Returning to main menu.")
    time.sleep(2)
    main()


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

    print("Returning to main menu.")
    time.sleep(2)
    main()


if __name__ == "__main__":
    main()
    handle_input_past_trades()