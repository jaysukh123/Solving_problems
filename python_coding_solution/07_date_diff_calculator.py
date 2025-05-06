from datetime import datetime

# Function to calculate the difference in days between two dates
def calculate_date_difference(birthdate, current_date):
    # Convert string input to datetime objects
    birth_date = datetime.strptime(birthdate, "%d-%m-%Y")
    current_date = datetime.strptime(current_date, "%d-%m-%Y")

    # Calculate the difference in days
    delta = current_date - birth_date
    return delta.days

# Input: Get the birthdate and current date from the user
birthdate = input("Enter your birthdate (dd-mm-yyyy): ")
current_date = input("Enter today's date (dd-mm-yyyy): ")

# Calculate and display the difference in days
days_lived = calculate_date_difference(birthdate, current_date)
print(f"You have lived for {days_lived} days.")
