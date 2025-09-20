# create a custom Exception
class DuplicateAccountError(Exception):
    ...
class InsuffiecientFundError(Exception):
    ...
class AccountNotFoundError(Exception):
    ...
def is_valid_name(name:str):
    """raise Error if the name is invalid"""
    if name:
        for character in name:
            if character.isdigit():
                raise TypeError("TypeError: name cannot be a int , float , bool or None")
        if name.lower() in ["true","false","none"]:
            raise ValueError("ValueError: value could not true , false and none")
    else:
        raise ValueError("name cannot be an empty")
    
def is_valid_account(account_number:str):
    """Raise Error if the account number is not valid"""
    if account_number:
        for digit in account_number:
            if  not digit.isdigit():
                raise TypeError("TypeError: Account number must numeric")
        if not int(account_number)>0:
            raise ValueError("valueError: account number should be greater than zero")
        else:
            return int(account_number)
    else:
        raise ValueError("ValueError: account number cannot empty")

def is_valid_password(password:str):
    """check the password is valid or not"""
    if password:
        size = len(password)
        special_character = ["@","$","!","#","%","^","&","*","(",")",",","."]
        def must_one_special_character(password,special_character):
            """return true if the password must have special character otherwise return false"""
            for char in password:
                if char in special_character:
                    return True
            else:
                return False
        def any_uppercase(password:str):
            """return True if any uppercase chracter in password"""
            for char in password:
                if char.isupper():
                    return True
            else:
                return False
        def any_lowercase(password:str):
            """return True if any lowercase chracter in password"""
            for char in password:
                if char.islower():
                    return True
            else:
                return False
        if not size>=8 :
            raise ValueError("ValueError: password length must be greater than 8")
        elif not must_one_special_character(password,special_character):
            raise ValueError("ValueError: password must have one special character")
        elif not any_uppercase(password):
            raise ValueError("ValueError: password must have one uppercase character")
        elif not any_lowercase(password):
            raise ValueError("ValueError: password must have one lowercase character")
    else:
        raise ValueError("ValueError: password cannot be empty")
    

