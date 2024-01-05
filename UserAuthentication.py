def authenticate_user():
    # Predefined username and password
    correct_username = "user123"
    correct_password = "pass123"

    # Get user input
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the credentials are correct
    if username == correct_username and password == correct_password:
        print("Authentication successful. Welcome, {}!".format(username))
    else:
        print("Authentication failed. Please check your username and password.")

if __name__ == "__main__":
    authenticate_user()
