# this is the b method
import a as a_module
def method_of_b():
    print('method of b')

a_module.method_of_a()
if __name__ == '__main__':
    method_of_b()
