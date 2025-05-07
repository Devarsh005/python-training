# the method of a a

def method_of_a():
    print("method of a")
def call():
    import b
    b.method_of_b()
if __name__ =='__main__':
    method_of_a()
    call()


# import b
# b.method_of_b()