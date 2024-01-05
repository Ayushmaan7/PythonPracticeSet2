import re

def is_valid_email(email):
    # Regular expression for a basic email validation
    email_pattern = re.compile(r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$')

    # Check if the provided email matches the pattern
    return bool(re.match(email_pattern, email))

if __name__ == "__main__":
    input_email = input("Enter an email address: ")

    if is_valid_email(input_email):
        print(f"The email address '{input_email}' is valid.")
    else:
        print(f"The email address '{input_email}' is not valid.")
