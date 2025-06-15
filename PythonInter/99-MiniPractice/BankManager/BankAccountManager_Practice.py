import json

class BankAccount:
    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        # TODO: Add amount to balance
        pass

    def withdraw(self, amount):
        # TODO: Subtract amount from balance (only if enough funds)
        pass

    def to_dict(self):
        # TODO: Return a dictionary with 'name' and 'balance'
        pass

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["balance"])


# -------- File I/O --------
def load_accounts(filename="bank_data.json"):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            return [BankAccount.from_dict(acc) for acc in data]
    except FileNotFoundError:
        return []

def save_accounts(accounts, filename="bank_data.json"):
    with open(filename, "w") as f:
        json.dump([acc.to_dict() for acc in accounts], f, indent=2)


# -------- CLI Program --------
def find_account(accounts, name):
    for acc in accounts:
        if acc.name == name:
            return acc
    return None

def main():
    accounts = load_accounts()

    while True:
        print("\n1. Create account\n2. Deposit\n3. Withdraw\n4. View accounts\n5. Save & Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter new account name: ")
            if find_account(accounts, name):
                print("Account already exists.")
            else:
                accounts.append(BankAccount(name))
        elif choice == "2":
            name = input("Enter account name: ")
            acc = find_account(accounts, name)
            if acc:
                amt = float(input("Amount to deposit: "))
                acc.deposit(amt)
            else:
                print("Account not found.")
        elif choice == "3":
            name = input("Enter account name: ")
            acc = find_account(accounts, name)
            if acc:
                amt = float(input("Amount to withdraw: "))
                acc.withdraw(amt)
            else:
                print("Account not found.")
        elif choice == "4":
            for acc in accounts:
                print(f"{acc.name}: ${acc.balance:.2f}")
        elif choice == "5":
            save_accounts(accounts)
            print("Accounts saved. Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
