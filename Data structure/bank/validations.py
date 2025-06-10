def is_valid_name(name:str):
    if name:
        for character in name:
            if character.isdigit():
                raise TypeError("TypeError: name cannot be a int , float , bool or None")
        if name.lower() in ["true","false","none"]:
            raise ValueError("ValueError: value could not true , false and none")
        else:
            return True
    else:
        raise ValueError("name cannot be an empty")
# def is_valid_account(account_number):
#     if isinstance(account_number,int):
#         return account_number
#     else:
#         raise Exception("account should be an integer")
# def is_strong_password(account_number):
#     ...
# try:
#     name = input("enter a name")
#     x =is_valid_name(name)
#     print(x)
# except Exception as e:
#     print(e)