9# Function to record and process transactions
def bank_transaction_analyzer():
    balance = 0  # Initial balance is 0
    transaction_history = []  # List to store transaction details

    while True:
        # Ask for user input
        transaction_type = input("Enter transaction type (credit/debit) or 'exit' to finish: ").strip().lower()

        if transaction_type == 'exit':
            break

        if transaction_type not in ['credit', 'debit']:
            print("Invalid transaction type! Please enter 'credit' or 'debit'.")
            continue

        # Get the transaction amount
        try:
            amount = float(input("Enter the transaction amount: "))
            if amount <= 0:
                print("Transaction amount should be greater than 0.")
                continue
        except ValueError:
            print("Invalid amount! Please enter a valid number.")
            continue

        # Process the transaction
        if transaction_type == 'credit':
            balance += amount
            transaction_history.append(f"Credit: ₹{amount}")
        elif transaction_type == 'debit':
            if amount > balance:
                print("Insufficient funds for this debit!")
                continue
            balance -= amount
            transaction_history.append(f"Debit: ₹{amount}")

        # Print the balance after each transaction
        print(f"Balance after this transaction: ₹{balance}")

    # Final summary of all transactions
    print("\nTransaction Summary:")
    for transaction in transaction_history:
        print(transaction)
    print(f"Final Balance: ₹{balance}")


# Start the program
bank_transaction_analyzer()
