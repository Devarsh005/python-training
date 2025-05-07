# Create a custom math module with functions: is_prime(), gcd(), lcm(), factorial() — import it in another script and use it.

def is_prime(number):
    for i in range(2,(number//2)):
        if number % i == 0:
            print(f'{number} is not prime')
            break
    else:
        print(f'{number} is prime')

def factorial(number):
    if number < 1:
        return 1
    else :
        return number * factorial(number-1)
    
