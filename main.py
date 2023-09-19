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

#2
def cube():
    a = int(input('A: '))
    b = int(input('B: '))
    result = ''

    for i in range(a, b+1):
        if i**3 <= b:
            result += f'{i**3} '

    print(result)

#3
def degree():
    n = int(input('N: '))
    degree = int(input('degree: '))
    result = 1

    if degree > 0:
        for i in range(degree+1):
            if i == 0:
                continue

            result *= n
    else:
        print('error')

    print(result)

#4
def factorial():
    n = int(input('N: '))
    result = 1

    for i in range(n+1):
        if i == 0:
            continue

        result *= i

    print(result)

#5
def fibo():
    n = int(input('N: '))
    result = [0, 1]

    for i in range(n+1):
        if n <= 1:
            break
        elif i == 0:
            continue

        result.append(result[i-1]+result[i])
    
    if n > 1:
        result.pop(-1)

    print(result)

#6
def extract(n):
    lst = []

    if n < 0:
        print('error')
    else:
        while n != 0:
            lst.append(n % 10)
            n = n // 10

    lst.reverse()
    print(lst)

    return lst

#7
def extract_even():
    n = int(input('N: '))
    result = 0

    for i in extract(n):
        if i % 2 == 0:
            result += i

    print(result)

#8
def extract_sum():
    n = int(input('N: '))
    result1 = 0
    result2 = 1

    for i in extract(n):
        result1 += i
        result2 *= i

    print(result1)
    print(result2)

extract_sum()