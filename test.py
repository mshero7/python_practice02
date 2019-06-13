def sum_digit(number):
    if number < 10:
        return number
    else:
        return number % 10 + sum_digit(number // 10)

a = 2.0
print(type(a) is int)
print(a.is_integer())

print(4 / 3)

a, b = divmod(2,3)
print(a)
print(b)
print(divmod(2,3))