def factorial(x):
    if x > 0:
        return x * factorial(x - 1)
    else:
        return 1


def approx_sin(x, n):
    if n <= 0:
        return print('n should be greater than 0')
    answer = 0
    for i in range(n + 1):
        answer += (-1) ** i * (x ** (2 * i + 1) / factorial(2 * i + 1))
    return print(answer)


def approx_cos(x, n):
    if n <= 0:
        return print('n should be greater than 0')
    answer = 0
    for i in range(n + 1):
        answer += (-1) ** i * (x ** (2 * i) / factorial(2 * i))
    return print(answer)


def approx_sinh(x, n):
    if n <= 0:
        return print('n should be greater than 0')
    answer = 0
    for i in range(n + 1):
        answer += (x ** (2 * i + 1) / factorial(2 * i + 1))
    return print(answer)


def approx_cosh(x, n):
    if n <= 0:
        return print('n should be greater than 0')
    answer = 0
    for i in range(n + 1):
        answer += (x ** (2 * i) / factorial(2 * i))
    return print(answer)


approx_sin(x=3.14,n=10)
approx_cos(x=3.14,n=10)
approx_sinh(x=3.14,n=10)
approx_cosh(x=3.14,n=10)