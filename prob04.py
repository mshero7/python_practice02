#
# 문제4
# 반복문을 이용하여 369게임에서 박수를 쳐야 하는 경우의 수를 순서대로 화면에
# 출력해보세요. 1부터 99까지만 실행하세요.
#

# 자리수 구하는 함수
def calc_digit(number, count):
    if number < 10:
        return count
    else:
        count += 1
        return calc_digit(number // 10, count)

def calc_three(number):
    number_map = map(int, str(number))
    count = 0
    for item in number_map:
        if item % 3 == 0 and item != 0:
            count += 1
    return count

for i in range(1,101):
    if calc_three(i) != 0:
        print(i, ' ', '짝' * calc_three(i))


