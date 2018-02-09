import itertools

if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 024: Lexicographic permutations", 0, 1)
progress_.progress()

result = list(itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
result.sort()

progress_.count = (int(''.join([str(i) for i in result[999999]])))
progress_.total = answers_list[24]
progress_.progress()

if __name__ == '__main__':
    input()
