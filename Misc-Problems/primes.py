def isPrime(x):
    """
        Find if a number is a prime number
        
        INPUT
        -----------
        x : integer
        
    """
    rm = range(1,10); primeCount = 0
    
    if x > 0:
        if x == 1:
            print("1 is not prime number")
        else:
            for i in rm:
                if x % i == 0:
                    primeCount += 1;
            if primeCount == 2:
                print("{} is a prime number".format(x))
            else:
                print("{} is not a prime number".format(x))
    else:
        print("Entered number is not a positive integer")