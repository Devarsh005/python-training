class PeterDog :
    spec = 'peter class'
    def __init__(self):
        self.name = 'peter'



dog1 = PeterDog()
print(dog1.name)
print(dog1.spec)

class Dog:
    spec = 'dog class'
    def __init__(self,name,age,breed):
        self.name = name
        self.breed = breed


# dog2 = Dog('ccc',age=4,name='bully') >> #  dog2 = Dog('ccc',age=4,name='bully')
                                        #            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                                        # TypeError: Dog.__init__() got multiple values for argument 'name'
dog2 = Dog('bully',4,'ccc')
# print(dog2.age)     >>  #print(dog2.age)
                    #         ^^^^^^^^
                    # AttributeError: 'Dog' object has no attribute 'age'
print(dog2.name)

# memory address of object is same or distinct 
# print(id(dog1))
# print(id(dog2))
def is_id_same(dog1,dog2):
    if id(dog1) is id(dog2):
        return True
    else:
        return False
print(f"dog1 and dog2 id same: {is_id_same(dog1,dog2)}")

print(dog2.name)
dog2.name = 'buddy'
print(dog2.name)