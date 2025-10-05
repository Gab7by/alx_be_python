from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in 'YYYY-MM-DD HH:MM:SS' format.
    """
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date

def calculate_future_date(current_date):
    """
    Prompts the user for a number of days, calculates and displays the future date.
    """
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        future_date = current_date + timedelta(days=days_to_add)
        formatted_future = future_date.strftime("%Y-%m-%d")
        print(f"Future date: {formatted_future}")
    except ValueError:
        print("Invalid input. Please enter an integer value for the number of days.")

def main():
    # Part 1: Display current date and time
    current_date = display_current_datetime()

    # Part 2: Calculate future date
    calculate_future_date(current_date)

if __name__ == "__main__":
    main()
