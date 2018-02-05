import math
import collections

def is_prime(x):
    """
    Checks if x is prime
    """
    if x <= 1:
        return False
    for i in range(2, round(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    else:
        return True

def factors(x):
    """
    Returns list of distinct factors of x
    """
    factors_list = []
    if x % 2 == 1:
        step = 2
    else:
        step = 1
    for i in range(1, round(math.sqrt(x)) + 1, step):
        if x % i == 0:
            if i**2 == x:
                factors_list.append(i)
            else:
                factors_list.extend([i, x//i])
    return(factors_list)

def prime_factors(x):
    """
    Returns list of prime factors of x, not necessarily distinct
    """
    out_list = []
    while x != 1:
        n = 2
        out_list_temp = []
        for n in range(2, x + 1):
            if x % n == 0:
                for i in range(2, round(math.sqrt(n)) + 2):
                    if (n % i == 0) and (n != i):
                        break
                else:
                    out_list_temp.append(n)
        for i in out_list_temp:
            x = int(x/i)
        out_list.extend(out_list_temp)
    out_list.sort()
    return(out_list)

def num_factors(x):
    """
    Returns number of distinct factors of x
    """
    return(len(factors(x)))

def num_prime_factors(x):
    """
    Returns number of distinct prime factors of x
    """
    prime_factors_list = [1 for j in factors(x) if is_prime(j)]
    return(len(prime_factors_list))

def sum_factors(x):
    """
    Returns sum of distinct factors of x, not including x itself
    """
    return(sum(factors(x)) - x)

def is_abundant(x):
    """
    Checks if the sum of distinct factors of x, not including x itself, is larger than x
    """
    return(sum_factors(x) > x)


def is_pandigital(x):
    """
    Checks if x contains all digits between 1 and 9 (inclusive) exactly once
    """
    digits = [int(i) for i in str(x)]
    digits.sort()
    return(digits == list(range(1, 10)))

def is_palindrome(string):
    """
    Checks if string is a palindrome
    """
    return(string == string[::-1])

def collatz(x):
    """
    Generates the next term of the Collatz sequence, given the previous term x
    """
    if x % 2 == 0:
        return(x//2)
    else:
        return(3*x + 1)

def written(x):
    """
    For x >= 0 and x <= 1000, returns the number of letters required to write out x in words
    """
    total_letters = 0
    if x == 1000:
        return(11)
    elif x in range(10, 20):
        if x == 10:
            return(3)
        elif x in [11, 12]:
            return(6)
        elif x in [13, 14, 18, 19]:
            return(8)
        elif x in [15, 16]:
            return(7)
        elif x == 17:
            return(9)
    elif x in range(0, 10):
        if x in [1, 2, 6]:
            return(3)
        elif x in [4, 5, 9]:
            return(4)
        elif x in [3, 7, 8]:
            return(5)
        else:
            return(0)
    elif x in range(20, 100):
        if int(str(x)[0]) in [2, 3, 8, 9]:
            total_letters += 6
        elif int(str(x)[0]) in [4, 5, 6]:
            total_letters += 5
        else:
            total_letters += 7
        total_letters += written(int(str(x)[1]))
        return(total_letters)
    else:
        total_letters += 7
        total_letters += written(int(str(x)[0]))
        total_letters += written(int(str(x)[1:]))
        if str(x)[1:] != '00':
            total_letters += 3
        return(total_letters)

def score(letter):
    """
    Returns index of letter in alphabet e.g. A -> 1, B -> 2, ...
    """
    string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return(string.index(letter) + 1)

def fib(x):
    """
    Returns the xth term of the Fibonacci sequence
    """
    a, b = 1, 1
    for i in range(1, x):
        a, b = b, a + b
        x += 1
    return(a)

def recurring_decimals_length(x):
    """
    Returns the cycle length of the reciprocal of x, if x is a prime number with more than one digit
    """
    k = 9
    while True:
        if k % x == 0:
            return(len(str(k)))
            break
        k = 10*k + 9

def coin_solutions(total, coin_index):
    """
    Returns the number of ways the total amount can be made, with the coin at coin_index being the largest available coin value
    """
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    if coin_index == 0:
        return(1)
    else:
        num_solutions = 0
        while total >= 0:
            num_solutions += coin_solutions(total, coin_index - 1)
            total -= coins[coin_index]
        return(num_solutions)

def arrangements(x):
    """
    Returns list of the circular arrangements of the digits of x
    """
    output_list = []
    circular = collections.deque(str(x))
    for i in range(len(circular)):
        output_list.append(int(''.join(list(circular))))
        circular.rotate(1)
    return(output_list)

def is_digits_divisible(x):
    """
    Checks if any digit of x is 0, 2, 4, 5, 6, or 8
    In other words, returns False when x only contains 1, 3, 7, and 9
    """
    if len(str(x)) == 1:
        return False
    allowable = [0, 2, 4, 5, 6, 8]
    for digit in str(x):
        if int(digit) in allowable:
            return True
    else:
        return False

def is_triangle(x):
    """
    Checks if x is a triangle number
    """
    n = int(math.sqrt(2*x))
    return(n*(n + 1) == 2*x)

def is_pentagon(n):
    """
    Checks if x is a pentagon number
    """
    return((1 + math.sqrt(24*n + 1))/6 == round((1 + math.sqrt(24*n + 1))/6))

def truncate(x):
    """
    Returns list of numbers produced by truncating consecutive digits of x
    """
    numbers = [x]
    for i in range(1, len(str(x))):
        numbers.extend([x % 10**i, x//10**i])
    return(numbers)

