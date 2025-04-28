from dis import dis
a=2
b=3
sum = a+b
print(sum)
def mul(a,b):
    return a*b
dis(mul)
# how the ast create a tree internally in python
import ast
code= "x=1+2"
tree = ast.parse(code)
print(ast.dump(tree,indent=4))