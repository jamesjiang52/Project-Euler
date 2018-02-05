from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 028: Number spiral diagonals", 1, answers_list[28])

for a in range(2, 502):
    spiral = list(range((2*a - 3)**2 + 1, (2*a - 1)**2 + 1))
    progress_.count += spiral[2*a - 3]
    progress_.count += spiral[4*a - 5]
    progress_.count += spiral[6*a - 7]
    progress_.count += spiral[8*a - 9]
    progress_.progress()
