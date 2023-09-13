from colorama import Fore, init
from datetime import datetime

from functions import line_break, close_script, back_to_menu
from sheet_data import *


allowed_keys = {'1', '2', '3', 'esc'}
init(autoreset=True)


def main():
    """
    Welcome message and navigation overview
    """
    line_break()
    print(Fore.YELLOW + "Trading Statistics\n\n")
    print("Display your trading statistics.\n")
    print("Please press one of the following buttons to continue:\n")
    print("'1' to enter a number of past trades.")
    print("'2' to display todays trades.")
    print("'3' to display all past trades.\n")
    print(Fore.RED + "'ESC' to exit the program.")


def handle_input_statistics():
    """
    Handles key presses to navigate menu
    1: Enter number of past trades statistic to display
    2: Display todays trades statistic
    3: Display all past trades statistic
    ESC: to exit the program; using sys.exit
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


def past_num_trades_statistic():
    """
    Enter a number to get data from past trades.
    If the number is higher than all past trades,
    an error message will appear with the max. number of all past trades.
    Instead redirects to show all past trades statistic.
    """
    line_break()
    print("Display your past trades statistic.\n")
    num_of_past_trades = input("Number of past trades: \n")
    total_rows_with_data = sum(
            1 for i, row in enumerate(data)
            if any(row) and i != 0
            )

    try:
        num_of_past_trades = int(num_of_past_trades)
    except ValueError:
        line_break()
        print(Fore.RED + "Invalid input. Please enter a number.")
        past_num_trades_statistic()

    if num_of_past_trades <= 0:
        print(Fore.RED + "Invalid input. Please enter a positive number.")
        line_break()
        past_num_trades_statistic()

    if num_of_past_trades > total_rows_with_data:
        line_break()
        print(Fore.RED + f"Requested {num_of_past_trades} rows," +
              f" but there are only {total_rows_with_data}" +
              " rows with data.\n")
        print(Fore.RED + "Here are all past trades statistics instead.")
        all_trades_statistic()
        return

    last_n_rows = [
        row for row in reversed(data[1:])
        if any(row)
        ][:num_of_past_trades]
    total_profit_loss = calculate_total_profit_loss(last_n_rows)
    total_trades = len(last_n_rows)
    short_trades = sum(1 for row in last_n_rows if row[3] == "Short")
    long_trades = sum(1 for row in last_n_rows if row[3] == "Long")
    winning_trades = sum(
        1 for row in last_n_rows
        if (row[3] == "Long" and row[4] < row[5])
        or (row[3] == "Short" and row[4] > row[5])
        )
    losing_trades = num_of_past_trades - winning_trades
    win_ratio = winning_trades / num_of_past_trades * 100

    line_break()
    print(f"Total profit or loss from" +
          f"the past {num_of_past_trades} trades: ${total_profit_loss:.2f}")
    print(f"Total number of trades: {total_trades}")
    print(f"Number of 'Short' trades: {short_trades}")
    print(f"Number of 'Long' trades: {long_trades}")
    print(f"Number of winning trades: {winning_trades}")
    print(f"Number of losing trades: {losing_trades}")
    print(f"Win ratio: {win_ratio:.2f}\n")

    back_to_menu()
    handle_input_statistics()


def todays_num_trades_statistic():
    """
    Get all past trades statistic with today's date.
    """
    today_date_str = datetime.now().strftime('%d.%m.%Y')
    filtered_rows = [
        row for row in data
        if any(row) and row[0] == today_date_str
        ]
    total_profit_loss = calculate_total_profit_loss(filtered_rows)
    total_trades = len(filtered_rows)
    short_trades = sum(1 for row in filtered_rows if row[3] == "Short")
    long_trades = sum(1 for row in filtered_rows if row[3] == "Long")
    winning_trades = sum(
        1 for row in filtered_rows
        if (row[3] == "Long" and row[4] < row[5])
        or (row[3] == "Short" and row[4] > row[5])
        )
    losing_trades = total_trades - winning_trades
    win_ratio = winning_trades / total_trades * 100

    if not filtered_rows:
        line_break()
        print(Fore.RED + "No trades with today's date found.\n")
        back_to_menu()
        handle_input_statistics()

    line_break()
    print("Todays trades statistic:\n")
    print(f"Requested today's trades profit or loss" +
          f" amount to ${total_profit_loss:.2f}\n")
    print(f"Total number of trades: {total_trades}")
    print(f"Number of 'Short' trades: {short_trades}")
    print(f"Number of 'Long' trades: {long_trades}")
    print(f"Number of winning trades: {winning_trades}")
    print(f"Number of losing trades: {losing_trades}")
    print(f"Win ratio: {win_ratio:.2f}\n")

    back_to_menu()
    handle_input_statistics()


def all_trades_statistic():
    """
    Get all past trades statistic.
    """
    all_n_rows = [row for row in reversed(data[1:]) if any(row)]
    total_profit_loss = calculate_total_profit_loss(all_n_rows)
    total_trades = len(all_n_rows)
    short_trades = sum(1 for row in all_n_rows if row[3] == "Short")
    long_trades = sum(1 for row in all_n_rows if row[3] == "Long")
    winning_trades = sum(
        1 for row in all_n_rows if
        (row[3] == "Long" and row[4] < row[5])
        or (row[3] == "Short" and row[4] > row[5])
        )
    losing_trades = total_trades - winning_trades
    win_ratio = winning_trades / total_trades * 100

    line_break()
    print("All trades statistic:\n")
    print(f"Requested all trades profit or loss" +
          f" amount to ${total_profit_loss:.2f}\n")
    print(f"Total number of trades: {total_trades}")
    print(f"Number of 'Short' trades: {short_trades}")
    print(f"Number of 'Long' trades: {long_trades}")
    print(f"Number of winning trades: {winning_trades}")
    print(f"Number of losing trades: {losing_trades}")
    print(f"Win ratio: {win_ratio:.2f}\n")

    back_to_menu()
    handle_input_statistics()


def calculate_total_profit_loss(last_n_rows):
    """
    Calculates the total profits
    Short = entry_price - exit_price * num_of_shares
    Long = exit_price - entry_price * num_of_shares
    """
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
