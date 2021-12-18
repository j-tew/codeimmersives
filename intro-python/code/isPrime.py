def is_prime(number):
    for n in range(2,int(number**1/2)+1):
        if number%n==0:
            return False
    return True