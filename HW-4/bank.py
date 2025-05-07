class Bank:
    def __init__(self, name):
        self.name = name
        self.clients = {}

    def add_clients(self, client):
        if client.id_number in self.clients:
            raise Exception(f"Client with ID {client.id_number} already exist")
        self.clients[client.id_number] = client


class Client:
    def __init__(self, id_number):
        self.id_number = id_number
        self.accounts = {}

    def add_account(self, currency):
        if currency in self.accounts:
            raise Exception(
                f"Client {self.id_number} have already account in {currency} currency"
            )
        self.accounts[currency] = BankAccount(currency)

    def close_account(self, currency):
        if currency not in self.accounts:
            raise Exception(f"Client with ID {self.id_number} doesn't exist")
        del self.accounts[currency]

    def get_total_balance(self):
        total_balance = sum(
            account.balance for account in self.accounts.values()
        )
        return total_balance


class BankAccount:
    def __init__(self, currency):
        self.currency = currency
        self.balance = 0

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0 or amount > self.balance:
            raise ValueError("Invalid withdraw amount or insufficient funds")
        self.balance -= amount

    def transfer(self, amount, recipent_account):
        if amount <= 0:
            raise ValueError("Transfer amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds for transfer")
        self.withdraw(amount)
        recipent_account.deposite(amount)


def terminal_interface(bank):
    print("Entering terminal interface...")
    while True:
        print("Inside the menu loop...")
        print("\nMenu:")
        print("1. Add a Client")
        print("2. Add an account")
        print("3. Close an account")
        print("4. Deposite an account")
        print("5. Withdraw an account")
        print("6. Transfer")
        print("7. Make a statement of accounts")
        print("8. Exit")

        choice = input("Make youre choice: ").strip()
        print(f"User selected choice: '{choice}'")

        if choice == "8":
            break

        if choice == "1":
            client_id = input("Input ID number: ")
            if client_id in bank.clients:
                print(f"Client with ID {client_id} already exists.")
            else:
                new_client = Client(client_id)
                bank.add_clients(new_client)
                print(f"New client with ID {new_client.id_number} registered.")
                print(f"Current clients: {bank.clients}")
            continue

        if choice in ["2", "3", "4", "5", "6", "7"]:
            client_id = input("Input ID number: ")
            if client_id not in bank.clients:
                print(f"Client with ID {client_id} doesn't exist.")
                continue
            client = bank.clients[client_id]

        if choice == "2":
            currency = input("Input the currency: ")
            try:
                client.add_account(currency)
                print(
                    f"Client with ID {client.id_number} opened new account in {currency} currency"
                )
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "3":
            currency = input("Input the currency: ")
            try:
                client.close_account(currency)
                print(
                    f"Client with ID {client.id_number} closed an account in {currency} currency"
                )
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "4":
            currency = input("Input the currency: ")
            try:
                amount = float(input("Input amount to deposit: "))
                client.accounts[currency].deposit(amount)
                print("Deposit the account completed successfully")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "5":
            currency = input("Input the currency: ")
            try:
                amount = float(input("Input amount to withdraw: "))
                client.accounts[currency].withdraw(amount)
                print("Withdrawal from account completed successfully")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "6":
            donate_account = input(
                "Enter the currency you want to transfer from: "
            )
            recipient_account = input(
                "enter the currency you want to convert to: "
            )
            try:
                amount = float(input("Input the amount to transfer: "))
                client.accounts[donate_account].transfer(
                    amount, client.accounts[recipient_account]
                )
                print(
                    f"Amount {amount} was transfered from donate account to recipient account successfully"
                )
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "7":
            file_name = f"{client_id}_summary.txt"
            try:
                with open(file_name, "w") as file:
                    file.write(
                        f"Account statement for client with ID: {client_id}\n"
                    )
                    total_balance = sum(
                        account.balance for account in client.accounts.values()
                    )
                    for currency, account in client.accounts.items():
                        file.write(
                            f"Account in currency {currency}: balance: {account.balance}\n"
                        )
                    file.write(f"Total balance: {total_balance}\n")
                print(
                    "the account statement has been saved to file {file_name}"
                )
            except Exception as e:
                print(f"Error: {e}")

        else:
            print("Invalid input. Please try again.")


my_bank = Bank("My Bank")
print("Testing function call...")
terminal_interface(my_bank)
