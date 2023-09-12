import sys

def line_break():
    """
    Adds a line and a blank line underneath.
    For visual pleasure.
    """
    print("__________________________________________________\n")

def close_script():
    print("\nExiting the program.")
    line_break()
    sys.exit(0)