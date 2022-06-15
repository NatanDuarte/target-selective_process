from math import sqrt


def isPerfectSquare(number: int) -> bool:
    square = int(sqrt(number))
    return (
        square**2 == number
        and
        number > 0
    )


def isFibonacci(number: int) -> bool:
    return (
        isPerfectSquare(5 * number**2 + 4)
        or
        isPerfectSquare(5 * number**2 - 4)
    )


def main():
    try:
        value = int(input('Numero: '))
    except ValueError:
        print('Entrada invalida')
        exit(1)

    if isFibonacci(value):
        print(f'{value} pertence à sequência Fibonacci.')
    else:
        print(f'{value} não pertence à sequência Fibonacci.')


main()
