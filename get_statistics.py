from functions import line_break
from sheet_data import *

from datetime import datetime
from tabulate import tabulate

import time


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
            all_trades_statistic()
        else:
            line_break()
            print("Invalid format, please enter '1' or '2' or '3'.")


def past_num_trades_statistic():
    """
    Enter a number to get data from past trades.
    If the number is higher than all past trades,
    an error message will appear with the number of all past trades
    """
    line_break()
    num_of_past_trades = input("Enter the number of last trades to get data from: \n")
    total_rows_with_data = sum(1 for i, row in enumerate(data) if any(row) and i != 0)

    try:
        num_of_past_trades = int(num_of_past_trades)
    except ValueError:
        line_break()
        print("Invalid input. Please enter a number.")
        return

    if num_of_past_trades <= 0:
        print("Invalid input. Please enter a positive number.")
        line_break()
        return

    if num_of_past_trades > total_rows_with_data:
        line_break()
        print(f"Requested {num_of_past_trades} rows, but there are only {total_rows_with_data} rows with data.")
        return

    line_break()
    last_n_rows = [row for row in reversed(data[1:]) if any(row)][:num_of_past_trades]

    total_profit_loss = calculate_total_profit_loss(last_n_rows)

    print(f"Total profit or loss from the past {num_of_past_trades} trades: ${total_profit_loss:.2f}")


def todays_num_trades_statistic():
    """
    Get all past trades statistic with today's date.
    """
    today_date_str = datetime.now().strftime('%d.%m.%Y')

    filtered_rows = [row for row in data if any(row) and row[0] == today_date_str]

    if not filtered_rows:
        print("No trades with today's date found.")
        return

    total_profit_loss = calculate_total_profit_loss(filtered_rows)
    
    line_break()
    print("Here you can see your statistics from today's trades:\n")
    print(f"Requested today's trades profit or loss amount to ${total_profit_loss:.2f}")

    while True:
        line_break()
        print("Press '1' to go back to the trades statistic menu.\n")
        choice = input("Enter your choice: ")
        if choice == "1":
            handle_input_statistics()
        else:
            line_break()
            print("Invalid format, please enter '1'.")


def all_trades_statistic():
    last_n_rows = [row for row in reversed(data[1:]) if any(row)]
    
    line_break()
    print("Here you can see your statistics from all trades:\n")

    total_profit_loss = calculate_total_profit_loss(last_n_rows)
    print(f"Requested all trades profit or loss amount to ${total_profit_loss:.2f}")

    while True:
        line_break()
        print("Press '1' to go back to the trades statistic menu.\n")
        choice = input("Enter your choice: ")
        if choice == "1":
            handle_input_statistics()
        else:
            line_break()
            print("Invalid format, please enter '1'.")


def calculate_total_profit_loss(last_n_rows):
    total_profit_loss = 0

    for row in last_n_rows:
        entry_price = float(row[4])
        exit_price = float(row[5])
        num_of_shares = float(row[2])

        if row[3] == "Short":
            short_calc_result = (entry_price - exit_price) * num_of_shares
            total_profit_loss += short_calc_result
        else:
            long_calc_result = (exit_price - entry_price) * num_of_shares
            total_profit_loss += long_calc_result

    return total_profit_loss



def main():
    """
    Run all program functions
    """
    handle_input_statistics()

if __name__ == "__main__":
    main()