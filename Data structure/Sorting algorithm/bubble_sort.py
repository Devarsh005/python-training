numbers = [7,19,-3,4,0]
n = len(numbers)

for i in range(1,n):
    for j in range(0,n-i):
        if numbers[j] > numbers[j+1]:
            numbers[j] , numbers[j+1] = numbers[j+1] , numbers[j]
print(numbers)