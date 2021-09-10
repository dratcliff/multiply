import random
from os import system
from timeit import default_timer as timer

choices = []
for i in range(1, 13):
    for j in range(1, 13):
        choices.append((i, j))

incorrect_ct = 0
correct_ct = 0

start = timer()
while len(choices) > 0:
    c = random.choice(choices)
    a = input(str(c[0]) + " x " + str(c[1]) + " = ")
    try:
        i = int(a)
    except ValueError:
        input(a + " couldn't be converted to a number. Press enter to continue")
        system("cls")
        continue
    if i == c[0] * c[1]:
        correct_ct += 1
        choices.remove(c)
        system("cls")
    else:
        incorrect_ct += 1
        input("Incorrect. Press enter to continue")
        system("cls")

end = timer()
print("Total correct: " + str(correct_ct) + ". Total incorrect: " + str(incorrect_ct))
print("Elapsed time: " + str(end-start) + " seconds")
