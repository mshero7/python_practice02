import random

mininum, maximun = 1, 100
try_count = 1
flag = True

while True:
    if flag:
        rand_num = random.randrange(maximun) + mininum
        print('수를 결정하였습니다. 맞추어 보세요')
        flag = False
    print(rand_num)
    print(mininum, '-', maximun)
    print(try_count, '>>')

    answer = int(input())

    if rand_num == answer:
        print('맞췄습니다.')
        while True:
            a = input('다시 하시겠습니까?(y/n)>>')

            if a == 'y':
                flag = True
                break
            elif a == 'n':
                exit(0)
            else:
                print('y 혹은 n 으로 입력해주세요')
    else:
        if answer > rand_num:
            print('더 낮게')
            if answer < maximun:
                maximun = answer
        elif answer < rand_num:
            print('더 크게')
            if answer > mininum:
                mininum = answer
