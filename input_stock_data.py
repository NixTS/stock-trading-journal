from datetime import datetime
import re

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
    Placeholder print
    """
    print(f"The current date '{datetoday}' has been parsed to your journal.")

    trading_journal_entry.append(datetoday)
    

def input_date_manually():
    """
    Enter a date in the format DD.MM.YYYY. Prints the ValueError
    to the terminal if the wrong format is used.
    """
    date_str = input("Enter a date (DD.MM.YYYY): ")

    try:
        date_obj = datetime.strptime(date_str, "%d.%m.%Y")
        print(f"Your input '{datetoday}' has been parsed to your journal.")
    except ValueError:
        print("Invalid date format, please use DD.MM.YYYY format.")
    
    trading_journal_entry.append(date_str)


def input_ticker():
    while True:
        ticker = input("Enter ticker: ")

        if re.match(r"^[a-zA-Z]{1,4}$", ticker):
            break
        else:
            print("Invalid input, please enter 1 to 4 letters.")

    trading_journal_entry.append(ticker)


def input_shares_amount():
    while True:
        shares_amount = input("Shares amount traded: ")

        if re.match(r"^([\s\d]+)$", shares_amount):
            break
        else:
            print("Invalid input, please enter a number.")

    trading_journal_entry.append(shares_amount)


def input_direction():
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

    print(trading_journal_entry)


def main():
    """
    Run all program functions
    """
    handle_input_date()
    input_ticker()
    input_shares_amount()
    input_direction()


print("Please input your stock trading data by following the instructions given to you.\n")
main()