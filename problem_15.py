import math

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))

progress_ = Progress("Problem 015: Lattice paths", 0, answers_list[15])

n = math.factorial(40)//(math.factorial(20)**2)

progress_.count = n
progress_.progress()
