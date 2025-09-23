




def count_and_display_divisors(number):
    
    divisors = [i for i in range(1, number + 1) if number % i == 0]

    
    print("Divisors:", divisors)
    print("Count of divisors:", len(divisors))


number = int(input("Enter a positive integer: "))  
count_and_display_divisors(number) 
