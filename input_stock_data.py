from datetime import datetime

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
    print(trading_journal_entry)
    

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
    print(trading_journal_entry)


def main():
    """
    Run all program functions
    """
    handle_input_date()


print("Please input your stock trading data by following the instructions given to you.\n")
main()