def sum(*items):
    sum = 0
    for i in items:
        sum += i
    return sum

print(sum(1,2,3,4,5))
print(sum(1,2))
