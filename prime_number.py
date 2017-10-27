# A Python program in Python to check if the number is prime or not
# input from the user

# prime numbers are greater than 1
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


if __name__ == '__main__':
    num = int(input("Enter a number: "))
    print("{} {} a prime number".format(num, "is" if is_prime(num) else "is not"))
