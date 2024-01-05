from datetime import datetime

def date_difference_in_days(date_str1, date_str2):
    # Convert the date strings to datetime objects
    date1 = datetime.strptime(date_str1, "%Y-%m-%d")
    date2 = datetime.strptime(date_str2, "%Y-%m-%d")

    # Calculate the difference in days
    difference = abs((date2 - date1).days)

    return difference

if __name__ == "__main__":
    # Example usage
    date_str1 = input("Enter the first date (YYYY-MM-DD): ")
    date_str2 = input("Enter the second date (YYYY-MM-DD): ")

    try:
        difference_in_days = date_difference_in_days(date_str1, date_str2)
        print(f"The difference between the two dates is {difference_in_days} days.")
    except ValueError:
        print("Invalid date format. Please use the format YYYY-MM-DD.")
