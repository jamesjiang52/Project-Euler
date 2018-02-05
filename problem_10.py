from functions import *

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 010: Summation of primes", 0, answers_list[10])

for i in range(1, 2000000):
    if is_prime(i):
        progress_.count += i
        progress_.progress()
