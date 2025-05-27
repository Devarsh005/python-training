import dis

def anyfunction(alist):
    return len(alist)

dis.dis(anyfunction)
bytecode = dis.Bytecode(anyfunction)
print('bytecode instruction is ')
# for instruction in bytecode:
#     print(instruction)

def divison(dividend,divisor):
    return dividend / divisor
print(f"10 divided by 5 = {divison(10,5)}")
print(dis.code_info(divison))

