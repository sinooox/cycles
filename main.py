import math

#1
def square():
    n = int(input('N: '))
    result = ''

    for i in range(n+1):
        if i == 0:
            continue

        if i**2 <= n:
            result += f'{i**2} '

    print(result)

square()