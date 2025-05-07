
def sum_of_list(*args):
    return sum(args)

def mul(*args):
    result = 1
    for item in args:
        result = result*item
    return result
def print_message():
    print("this is the default run when import the module")
# __name__ = 'app'
if __name__ =='__main__':
    # print_message()

