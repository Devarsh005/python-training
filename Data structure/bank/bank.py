import validations
class Bank:
    bank_name = "HDFC bank"
    def __init__(self):
        self.list_of_accounts = {}
        self.balance = 1_00_00_000
    # create a new account
    def create_account(self,name,password,account_number):
        if account_number in self.list_of_accounts:
            return False
        else:
            account = Account(name,password,account_number)
            self.list_of_accounts[account_number] = account
            return True
    def authentication(self,account_number,password):
        account = self.list_of_accounts.get(account_number)
        if account and account.check_password(password):
            return account
        return None
    def get_account(self,account_number):
        return self.list_of_accounts.get(account_number)
    def display(self):
        print(self.list_of_accounts)
    # open particular account
    # 

class Account:
    def __init__(self,name,password,account_number):
        self.name = name
        self.account_number = account_number
        self.password = password
        self.balance = 0
        self.transactions = []
        self.info = {"name":self.name , "account_number":self.account_number , "balance":self.balance}
    def profile(self):
        print(self.info)
    def check_password(self,password):
        if password == self.password:
            return True
        else:
            return False
    def add_money(self,money):
        self.balance += money
        self.info["balance"] = self.balance
        self.transactions.append(f"{money} cash added")
    def send_money(self,money):
        self.balance -= money
        self.info["balance"] = self.balance
        self.transactions.append(f"{money} cash withdraw")
    def transfer_amount(self,reciever,amount):
        # account_number.add
        reciever.balance += amount
        self.balance -= amount
        self.info["balance"] = self.balance
        reciever.info["balance"] = reciever.balance
        self.transactions.append(f"{self.name} sent {amount} to {reciever.name}")
        reciever.transactions.append(f"{reciever.name} credited {amount} from {self.name} ")
    def transaction(self):
        for transaction in self.transactions:
            print(transaction)
    def check_balance(self):
        return self.balance


# create a user dictionary to store accounts only
users = open("users.json","a")
if __name__ == "__main__":
    bank = Bank()

    cases = """
    1. create a account
    2. login
    3. logout
    4. add money
    5. withdraw money
    6. close account
    7. transfer amount
    8. display profile
    9. show transaction
    10. show menu script
                """
    print(cases)
    flag = True
    while flag:
        operation = input("\nchoose option - \n") 
        match operation:
            case "1":
                """create an account"""
                try:
                    name = input("enter your name - ")
                    validations.is_valid_name(name)
                    account_number = input("enter account number - ")
                    validations.is_valid_account(account_number)
                    password = input("enter your password - ")
                    # valid name
                    # account number
                    # password
                    account = bank.create_account(name,password,account_number) 
                    if account:
                        print("Account created successfully")
                    else:
                        print("Account number already exits")
                except Exception as e:
                    print(e)
                
            case "2":
                """login"""
                account_number = input("enter the account number - ")
                validations.is_valid_account(account_number)
                password = input("enter the password - ")
                if bank.authentication(account_number,password):
                    print("login successfully")
                else:
                    print("invalid credential")
                    break

            case "3":
                """logout"""
                print("logout successfully")
                break

            case "4":
                """add money"""
                account_number = input("enter the account number - ")
                password = input("enter the password - ")
                account = bank.authentication(account_number,password)
                amount = float(input("enter amount - "))
                account.add_money(amount)
                print(f"{amount} added . current balance - {account.check_balance()}")

            case "5":
                """withdraw money"""
                account_number = input("enter the account number - ")
                password = input("enter the password - ")
                account = bank.authentication(account_number,password)
                amount = float(input("enter amount - "))
                account.send_money(amount)
                print(f"{amount} withdraw . current balance - {account.check_balance()}")

            case "6":
                """close account"""
                account_number = input("enter the account number - ")
                del bank.list_of_accounts[account_number]
                print(f"close the account")

            case "7":
                "transfer amount"
                account_number = input("enter the sender account number - ")
                password = input("enter the sender password - ")
                sender = bank.authentication(account_number,password)

                amount = float(input("enter amount - "))

                account_number = input("enter the reciever account number - ")
                password = input("enter the reciever password - ")
                reciever = bank.authentication(account_number,password)

                sender.transfer_amount(reciever,amount)
                print(f"{sender.name} sent {amount} to {reciever.name}")

            case "8":
                "display profile"
                account_number = input("enter the account number - ")
                password = input("enter the password - ")
                account = bank.authentication(account_number,password)
                account.profile()
            case "9":
                "show transaction"
                account_number = input("enter the account number - ")
                password = input("enter the password - ")
                account = bank.authentication(account_number,password)
                account.transaction()
            case "10":
                "show Menu script"
                print(cases)

            case _:
                flag = False
