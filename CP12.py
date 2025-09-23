




def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_primes_smaller_than(n):
    primes = [num for num in range(2, n) if is_prime(num)]
    print(f"Prime numbers smaller than {n}: {', '.join(map(str, primes))}")

#Main execution
n = int(input("Enter a positive integer: "))  #Get user input
print_primes_smaller_than(n)  #Call the function