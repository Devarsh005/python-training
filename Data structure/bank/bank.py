import validations
class Bank:
    bank_name = "HDFC bank"
    def __init__(self):
        self.list_of_accounts = {}
        self.balance = 1_00_000
        self.loan_users = []
    # create a new account
    def create_account(self,name:str,password:str,account_number:str):
        """create Account if it is not exits"""
        if account_number in self.list_of_accounts:
            return False
        else:
            account = Account(name,password,account_number)
            self.list_of_accounts[account_number] = account
            return True
    def authentication(self,account_number:str,password:str)->'Account':
        """return the account if the credential is right"""
        account = self.list_of_accounts.get(account_number)
        if account and account.check_password(password):
            return account
        else:
            raise validations.AccountNotFoundError("AccountNotFoundError: this account not registered in bank")
    def bank_info(self):
        """shows the bank name , bank balance , bank account list"""
        print("HDFC BANK")
        print(f"Bank balanace = {self.balance}")
        print(f"accounts list {self.list_of_accounts.keys()}")
    
    
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
        """show the user profile information like name , account_number and balance"""
        print(self.info)
    def check_password(self,password):
        """return True if password is matched"""
        if password == self.password:
            return True
        else:
            return False
    def add_money(self,money):
        """Add a cash money to user account """
        self.balance += money
        self.info["balance"] = self.balance
        self.transactions.append(f"{money} cash added")
    def withdraw_money(self,money):
        """withdraw a cash money from user account"""
        if self.balance > 0:
            self.balance -= money
            self.info["balance"] = self.balance
            self.transactions.append(f"{money} cash withdraw")
        else:
            raise validations.InsuffiecientFundError("InsuffiecientFundError: insuffiecient balance")
    def transfer_amount(self,reciever,amount):
        """transfer the amount to one account to another account"""
        if self.account_number == reciever.account_number:
            raise validations.DuplicateAccountError("DuplicateAccountError: Reciever cannot be sender")
        elif self.balance >0:
            reciever.balance += amount
            self.balance -= amount
            self.info["balance"] = self.balance
            reciever.info["balance"] = reciever.balance
            self.transactions.append(f"{self.name} sent {amount} to {reciever.name}")
            reciever.transactions.append(f"{reciever.name} credited {amount} from {self.name} ")
        else:
            raise validations.InsuffiecientFundError("InsuffiecientFundError: insuffiecient balance")
    def transaction(self):
        """show the transaction history of user"""
        for transaction in self.transactions:
            print(transaction)
    def check_balance(self):
        """return the balance of user """
        return self.balance
    def take_a_loan(self,amount,duration):
        interest_rate = 7
        total_with_interest = amount + (amount*interest_rate/100)
        emi = total_with_interest/duration
        self.balance += amount
        self.info['balance'] = self.balance
        print("loan passed")
        print(f"your minimum due per month is {emi}")
        return total_with_interest,emi
    def pay_emi(self , due_amount,remaining_amount,duration):
        remaining_amount -= due_amount
        duration -= 1
        self.balance -= due_amount
        self.info["balance"] = self.balance
        return remaining_amount,duration


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
    11. show all users
    12. show Bank profile
    13. take a loan
    14. pay emi
                """
    print(cases)
    flag = True
    while flag:
        print("press 10 for menu ")
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
                    validations.is_valid_password(password)
                    account = bank.create_account(name,password,account_number) 
                    if account:
                        print("Account created successfully")
                    else:
                        print("Account number already exits\n please login")
                except Exception as e:
                    print(e)
                
            case "2":
                """login"""
                try:
                    account_number = input("enter the account number - ")
                    validations.is_valid_account(account_number)
                    password = input("enter the password - ")
                    validations.is_valid_password(password)
                    if bank.authentication(account_number,password):
                        print("login successfully")
                    else:
                        print("invalid credential")
                except Exception as e:
                    print(e)

            case "3":
                """logout"""
                print("logout successfully")
                break

            case "4":
                """add money"""
                try:
                    account_number = input("enter the account number - ")
                    password = input("enter the password - ")
                    account = bank.authentication(account_number,password)
                    amount = float(input("enter amount - "))
                    account.add_money(amount)
                    print(f"{amount} added . current balance - {account.check_balance()}")
                    bank.balance += amount
                except Exception as e:
                    print(e)

            case "5":
                """withdraw money"""
                try:
                    account_number = input("enter the account number - ")
                    password = input("enter the password - ")
                    account = bank.authentication(account_number,password)
                    amount = float(input("enter amount - "))
                    account.withdraw_money(amount)
                    print(f"{amount} withdraw . current balance - {account.check_balance()}")
                    bank.balance -= amount
                except Exception as e:
                    print(e)

            case "6":
                """close account"""
                try:
                    account_number = input("enter the account number - ")
                    password = input("enter tha password")
                    account = bank.authentication(account_number,password)
                    bank.balance -= account.balance
                    del bank.list_of_accounts[account_number]
                    print(f"close the account")
                except Exception as e:
                    print(e)

            case "7":
                "transfer amount"
                try:
                    account_number = input("enter the sender account number - ")
                    password = input("enter the sender password - ")
                    sender = bank.authentication(account_number,password)

                    amount = float(input("enter amount - "))

                    account_number = input("enter the reciever account number - ")
                    password = input("enter the reciever password - ")
                    reciever = bank.authentication(account_number,password)
                    sender.transfer_amount(reciever,amount)
                    print(f"{sender.name} sent {amount} to {reciever.name}")
                except Exception as e:
                    print(e)

            case "8":
                "display profile"
                try:
                    account_number = input("enter the account number - ")
                    password = input("enter the password - ")
                    account = bank.authentication(account_number,password)
                    account.profile()
                except Exception as e:
                    print(e)
            case "9":

                "show transaction"
                try:
                    account_number = input("enter the account number - ")
                    password = input("enter the password - ")
                    account = bank.authentication(account_number,password)
                    account.transaction()
                except Exception as e:
                    print(e)
            case "10":
                "show Menu script"
                print(cases)
            case "11":
                """show all users"""
                for account_number,account in bank.list_of_accounts.items():
                    print(f"{account_number} : {account.info}")
            case "12":
                """show bank info"""
                bank.bank_info()
            case "13":
                """take a loan from bank"""
                try:
                    account_number = input("enter the account number - ")
                    password = input("enter the password - ")
                    account = bank.authentication(account_number,password)
                    amount = int(input("enter amount of loan"))
                    if amount < (bank.balance*20/100) :
                        bank.loan_users.append(account.account_number)
                        duration = int(input("enter duration for loan"))
                        total_amount_with_interest , due_amount = account.take_a_loan(amount,duration)
                        print(f"{account.name} account balance is {account.balance}")
                        bank.balance -= amount
                    else:
                        print(f"amount is larget , amount should be less than {bank.balance*20/100}")
                except Exception as e:
                    print(e)
            case "14":
                """pay emi"""
                try:
                    account_number = input("enter the account number - ")
                    password = input("enter the password - ")
                    account = bank.authentication(account_number,password)
                    if account_number in bank.loan_users:
                        if duration != 0:
                            total_amount_with_interest , duration = account.pay_emi(due_amount,total_amount_with_interest,duration)
                            bank.balance += due_amount
                            print(f"{due_amount} is paid and user current balance is {account.balance}")
                            print(f"{duration} are remaining")
                        else:
                            print("all dues are paid ")
                            break
                except Exception as e:
                    print(e)
                    

            case _:
                flag = False
