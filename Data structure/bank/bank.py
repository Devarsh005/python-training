import validations
import random
class Bank:
    bank_name = "HDFC bank"
    def __init__(self):
        self.list_of_accounts = {}
        self.balance = 1_00_000
        self.loan_users = []
    # create a new account
    def create_account(self,name,password,account_number):
        """create Account if it is not exits"""
        if account_number in self.list_of_accounts:
            return False
        else:
            account = Account(name,password,account_number)
            self.list_of_accounts[account_number] = account
            return True
    def authentication(self,account_number,password)->'Account':
        """return the account if the credential is right"""
        account = self.list_of_accounts.get(account_number)
        if account and account.check_password(password):
            return account
        else:
            raise validations.AccountNotFoundError("AccountNotFoundError: this account not registered in bank")
    def is_user(self,account_number)->'Account':
        if account_number in self.list_of_accounts:
            user = self.list_of_accounts.get(account_number)
            return user
        else:
            raise validations.AccountNotFoundError("AccountNotFoundError: This account not registerd in bank")
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
        self.minimum_balance = 5000
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
    def add_money(self,money,sender="you"):
        """Add a cash money to user account """
        self.balance += money
        self.info["balance"] = self.balance
        if sender == "you":
            self.transactions.append(f"{money} cash added")
        else:
            self.transactions.append(f"credited {amount} from {sender}")
    def withdraw_money(self,money,reciever="you"):
        """withdraw a cash money from user account"""
        if self.balance >= money:
            if self.balance-money > self.minimum_balance:
                self.balance -= money
                self.info["balance"] = self.balance
                if reciever == "you":
                    self.transactions.append(f"{money} cash withdraw")
                else:
                    self.transactions.append(f"{self.name} sent {money} to {reciever}")
            else:
                print(f"minimum account balace is {self.minimum_balance} and after withdraw {money} from account , balance is {self.balance-money} which is less than minimum amount so you can't withdraw money")
        else:
            raise validations.InsuffiecientFundError("InsuffiecientFundError: insuffiecient balance")
    def transfer_amount(self,reciever:'Account',amount):
        """transfer the amount to one account to another account"""
        if self.account_number == reciever.account_number:
            raise validations.DuplicateAccountError("DuplicateAccountError: Reciever cannot be sender")
        elif self.balance-amount >self.minimum_balance:
            self.withdraw_money(amount,reciever.name)
            reciever.add_money(amount,self.name)
            # self.transactions.append(f"{self.name} sent {amount} to {reciever.name}")
            # reciever.transactions.append(f"credited {amount} from {self.name}")
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
        """give a loan from bank to user"""
        interest_rate = 7
        monthly_interest = 7/12
        total_with_interest = amount + (amount*monthly_interest/100)*duration
        emi = total_with_interest/duration
        self.balance += amount
        self.info['balance'] = self.balance
        print("loan passed")
        print(f"your minimum due per month is {emi}")
        self.transactions.append(f"{self.name} take {amount} borrowed from Bank ")
        return total_with_interest,emi
    def pay_emi(self , due_amount,remaining_amount,duration):
        """give minimum due to bank """
        remaining_amount -= due_amount
        duration -= 1
        self.balance -= due_amount
        self.info["balance"] = self.balance
        self.transactions.append(f"{self.name} paid emi of ruppes {due_amount} to bank")
        return remaining_amount,duration


if __name__ == "__main__":
    bank = Bank()

    cases = """
    1. create a account
    2. login
    3. close account
    4. show Bank profile
    5. show all users
    6. show menu
    7. loan_candidates_details
    8. Exit
                """
    print(cases)
    flag = True
    while flag:
        print("press 6 for menu ")
        operation = input("\nchoose option - \n") 
        match operation:
            case "1":
                """create an account"""
                try:
                    name = input("enter your name - ")
                    validations.is_valid_name(name)
                    random_acc_num = random.randint(10_00_000,11_00_000)
                    account_number = None
                    while not account_number:
                        if not random_acc_num in bank.list_of_accounts:
                            account_number = random_acc_num
                        else:
                            random_acc_num = random.randint(10_00_000,11_00_000)
                    # validations.is_valid_account(account_number)
                    password = input("enter your password - ")
                    validations.is_valid_password(password)
                    account = bank.create_account(name,password,account_number) 
                    if account:
                        print(f"user name : {name}\nuser_account_number: {account_number}\nAccount created successfully")
                    else:
                        print("Account number already exits\n please login")
                except Exception as e:
                    print(e)
                
            case "2":
                """login"""
                try:
                    account_number = input("enter the account number - ")
                    account_number = validations.is_valid_account(account_number) # return integer account number
                    password = input("enter the password - ")
                    validations.is_valid_password(password)
                    user_account = bank.authentication(account_number,password)
                    if user_account:
                        print(f"{user_account.name} login successfully")
                        case = """
    1. add money
    2. withdraw money
    3. transfer amount
    4. display profile
    5. show transaction
    6. take a loan
    7. pay emi
    8. show menu script
    9. logout
        """             
                        print(case)
                        flag = True
                        while flag:
                            print("press 8 for menu ")
                            operation = input("\nchoose option - \n") 
                            match operation:
                                case "1":
                                    """add money"""
                                    try:
                                        amount = float(input("enter amount - "))
                                        user_account.add_money(amount)
                                        print(f"{amount} cash added . current balance - {user_account.check_balance()}")
                                        bank.balance += amount
                                    except Exception as e:
                                        print(e)
                                case "2":
                                    """withdraw money"""
                                    try:
                                        amount = float(input("enter amount - "))
                                        user_account.withdraw_money(amount)
                                        print(f"{amount} withdraw . current balance - {user_account.check_balance()}")
                                        bank.balance -= amount
                                    except Exception as e:
                                        print(e)
                                case "3":
                                    "transfer amount"
                                    try:
                                        account_number = input("enter the reciever account number - ")
                                        account_number = validations.is_valid_account(account_number) # return the integer account number if the account number is valid
                                        # password = input("enter the reciever password - ")
                                        reciever = bank.is_user(account_number)
                                        amount = float(input("enter amount - "))
                                        user_account.transfer_amount(reciever,amount)
                                        print(f"{user_account.name} sent {amount} to {reciever.name}")
                                    except Exception as e:
                                        print(e)
                                case "4":
                                    "display profile"
                                    try:
                                        user_account.profile()
                                    except Exception as e:
                                        print(e)
                                case "5":
                                    "show transaction"
                                    try:
                                        user_account.transaction()
                                    except Exception as e:
                                        print(e)
                                case "6":
                                    """take a loan from bank"""
                                    try:
                                        amount = int(input("enter amount of loan - "))
                                        if user_account.balance >=15000:
                                            if amount < (bank.balance*20/100) :
                                                bank.loan_users.append(user_account.account_number)
                                                duration = int(input("enter duration for loan (in month) - "))
                                                total_amount_with_interest , due_amount = user_account.take_a_loan(amount,duration)
                                                print(f"{user_account.name} account balance is {user_account.balance}")
                                                bank.balance -= amount
                                            else:
                                                print(f"amount is larger , amount should be less than {bank.balance*20/100}")
                                        else:
                                            print(f"{user_account.name} you are not eligible for loan, taking loan minimum balance is greater than 15000")
                                    except Exception as e:
                                        print(e)
                                case "7":
                                    """pay emi"""
                                    try:
                                        if account_number in bank.loan_users:
                                            if duration != 0:
                                                total_amount_with_interest , duration = user_account.pay_emi(due_amount,total_amount_with_interest,duration)
                                                bank.balance += due_amount
                                                print(f"{due_amount} is paid and user current balance is {user_account.balance}")
                                                print(f"{duration} are remaining")
                                            else:
                                                print("all dues are paid ")
                                    except Exception as e:
                                        print(e)
                                case "8":
                                    "show Menu script"
                                    print(case)
                                case "9":
                                    print(f"{user_account.name} logout successfully")
                                    break

                    else:
                        print("invalid credential")
                except Exception as e:
                    print(e)
            case "3":
                """close account"""
                try:
                    account_number = input("enter the account number - ")
                    account_number = validations.is_valid_account(account_number) # return the integer account numer
                    password = input("enter tha password -  ")
                    validations.is_valid_password(password)
                    account = bank.authentication(account_number,password)
                    bank.balance -= account.balance
                    del bank.list_of_accounts[account_number]
                    print(f"close the account")
                except Exception as e:
                    print(e)

            case "4":
                """show bank info"""
                if bank:
                    bank.bank_info()
                else:
                    print("The bank has no users")
            case "5":
                """show all users"""
                if bank.list_of_accounts:
                    for account_number,account in bank.list_of_accounts.items():
                        print(f"{account_number} : {account.info}")
                else:
                    print("The Bank has no users")
            case "6":
                "show Menu script"
                print(cases)
            case "7":
                if bank.loan_users:
                    print(f"loan users list{bank.loan_users}")
                else:
                    print("There is no loan users")
            case "8":
                flag = False
