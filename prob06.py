import random

min, max = 1, 100

random.randrange(max) + min

while True:
    n = random.randrange(max) + min
    print(n)

    if n == int(input('수 입력 : ')):
        break