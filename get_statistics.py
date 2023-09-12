import keyboard
import time
from functions import line_break, close_script, back_to_menu
from sheet_data import *
from datetime import datetime
from tabulate import tabulate


allowed_keys = {'1', '2', '3', 'esc'}


def main():
    """
    Welcome message and navigation overview
    """
    line_break()
    print("Trading statistics\n\n")
    print("If you want to get statistics for your trades, please follow the instructions given to you.\n")
    print("Press '1' on your keyboard to enter a number.")
    print("Or:")
    print("Press '2', if you want to get todays trades.")
    print("Or:")
    print("Press '3', if you want to get all your past trades.\n")


def handle_input_statistics():
    """
    Gives an option to either get statistics for a number of trades,
    or todays trades or all trades.
    """
    main()
    while True:
            event = keyboard.read_event(suppress=True)
            if event.event_type == keyboard.KEY_UP:
                choice = event.name

                if choice in allowed_keys:
                    if choice == "1":
                        past_num_trades_statistic()
                        break
                    elif choice == "2":
                        todays_num_trades_statistic()
                        break
                    elif choice == '3':
                        all_trades_statistic()
                    elif choice == 'esc':
                        close_script()
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
    print("Here you can get your past trades statistic.\n")
    num_of_past_trades = input("Enter the number of past trades: ")
    total_rows_with_data = sum(1 for i, row in enumerate(data) if any(row) and i != 0)

    try:
        num_of_past_trades = int(num_of_past_trades)
    except ValueError:
        line_break()
        print("Invalid input. Please enter a number.")
        past_num_trades_statistic()

    if num_of_past_trades <= 0:
        print("Invalid input. Please enter a positive number.")
        line_break()
        past_num_trades_statistic()

    if num_of_past_trades > total_rows_with_data:
        line_break()
        print(f"Requested {num_of_past_trades} rows, but there are only {total_rows_with_data} rows with data.\n")
        print("Here are your all time trade statistics instead.")
        all_trades_statistic()
        return

    line_break()
    last_n_rows = [row for row in reversed(data[1:]) if any(row)][:num_of_past_trades]

    total_profit_loss = calculate_total_profit_loss(last_n_rows)

    print(f"Total profit or loss from the past {num_of_past_trades} trades: ${total_profit_loss:.2f}\n")
    back_to_menu()
    handle_input_statistics()


def todays_num_trades_statistic():
    """
    Get all past trades statistic with today's date.
    """
    today_date_str = datetime.now().strftime('%d.%m.%Y')

    filtered_rows = [row for row in data if any(row) and row[0] == today_date_str]

    if not filtered_rows:
        line_break()
        print("No trades with today's date found.\n")
        back_to_menu()
        handle_input_statistics()
        

    total_profit_loss = calculate_total_profit_loss(filtered_rows)
    
    line_break()
    print("Here you can see your statistics from today's trades:\n")
    print(f"Requested today's trades profit or loss amount to ${total_profit_loss:.2f}\n")
    print("Returning to main menu.")
    time.sleep(2)
    handle_input_statistics()


def all_trades_statistic():
    last_n_rows = [row for row in reversed(data[1:]) if any(row)]
    
    line_break()
    print("Here you can see your statistics from all trades:\n")

    total_profit_loss = calculate_total_profit_loss(last_n_rows)
    print(f"Requested all trades profit or loss amount to ${total_profit_loss:.2f}\n")
    back_to_menu()
    handle_input_statistics()


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


if __name__ == "__main__":
    main()
    handle_input_statistics()