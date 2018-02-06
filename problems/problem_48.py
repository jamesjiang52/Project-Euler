from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 048: Self powers", 0, 1000)

sum_power = 0
for i in range(1, 1001):
    progress_.count = i
    progress_.progress()
    sum_power += i**i

progress_.count = int(str(sum_power)[-10:])
progress_.total = answers_list[48]
progress_.progress()
