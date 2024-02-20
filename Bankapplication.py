class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def create_account(self, account_number, initial_deposit):
        if account_number in self.accounts:
            print("Account already exists.")
            return
        if initial_deposit < 0:
            print("Initial deposit must be non-negative.")
            return
        self.accounts[account_number] = initial_deposit
        print("Account created successfully.")

    def deposit(self, account_number, amount):
        if account_number not in self.accounts:
            print("Account does not exist.")
            return
        if amount < 0:
            print("Deposit amount must be non-negative.")
            return
        self.accounts[account_number] += amount
        print("Deposit successful.")

    def withdraw(self, account_number, amount):
        if account_number not in self.accounts:
            print("Account does not exist.")
            return
        if amount < 0:
            print("Withdrawal amount must be non-negative.")
            return
        if amount > self.accounts[account_number]:
            print("Insufficient funds.")
            return
        self.accounts[account_number] -= amount
        print("Withdrawal successful.")

    def bank_balance(self, account_number):
        if account_number not in self.accounts:
            print("Account does not exist.")
            return
        print("Your balance is:", self.accounts[account_number])

    def mini_statement(self, account_number):
        if account_number not in self.accounts:
            print("Account does not exist.")
            return
        print("Mini Statement:")
        print("Account Number:", account_number)
        print("Balance:", self.accounts[account_number])

    def bank_detail(self):
        print("Bank Name:", self.name)
        print("Total Accounts:", len(self.accounts))
        print("Account Details:")
        for account_number, balance in self.accounts.items():
            print("Account Number:", account_number, "| Balance:", balance)


def main():
    bank_name = "ＢＡＮＫ ＯＦ ＧＯＵＲＩ'Ｓ"
    bank = Bank(bank_name)

    print("\n\n ＷＥＬＣＯＭＥ ＴＯ", bank_name)

    while True:
        print("\n\n   𝚂𝙴𝙴 𝚈𝙾𝚄𝚁 𝙲𝙷𝙾𝙸𝙲𝙴 𝙷𝙴𝚁𝙴  ↓:\n")
        print("1. CREATE ACCOUNT\n")
        print("2. DEPOSIT\n")
        print("3. WITHDRAW\n")
        print("4. CHECK BALANCE\n")
        print("5. MINI STATEMENT\n")
        print("6. BANK DETAILS\n")
        print("7. EXIT\n")

        choice = input("\n\nPLEASE SELECT YOUR OPTION= ")

        if choice == '1':
            account_number = input("Enter account number: ")
            initial_deposit = float(input("Enter initial deposit: "))
            bank.create_account(account_number, initial_deposit)

        elif choice == '2':
            account_number = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))
            bank.deposit(account_number, amount)

        elif choice == '3':
            account_number = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))
            bank.withdraw(account_number, amount)

        elif choice == '4':
            account_number = input("Enter account number: ")
            bank.bank_balance(account_number)

        elif choice == '5':
            account_number = input("Enter account number: ")
            bank.mini_statement(account_number)

        elif choice == '6':
            bank.bank_detail()

        elif choice == '7':
            print("\n\n THANKYOU FOR VISITING > ", bank_name)
            print("\n\n")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
