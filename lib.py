import math
from functools import reduce
from timeit import default_timer as timer
import operator as op


###########################################
############## Problem 1 ##################
###########################################
def is_perfect_square(num: int) -> bool:
    sqrt_num = abs(num**0.5)
    return math.ceil(sqrt_num) == math.floor(sqrt_num)


def is_fibonancci(num: int) -> bool:
    return is_perfect_square(5 * num * num - 4) or is_perfect_square(5 * num * num + 4)


def question1():
    print(
        """
###########################################
############## Problem 1 ##################
###########################################
"""
    )
    while True:
        try:
            num = int(input("Type your number: "))
            break
        except ValueError:
            print("Please just type number!!!")
            continue
    return f"{num} is fibonancci" if is_fibonancci(num) else f"{num} is not fibonancci"


def first_digit(num: int) -> int:
    return int(str(num)[:1])


def last_digit(num: int) -> int:
    return int(str(num)[-1])


def concat_two_digit2(digit1: int, digit2: int) -> int:
    return int(f"{digit1}{digit2}")


def is_gapful(num):
    return num % concat_two_digit2(first_digit(num), last_digit(num)) == 0


def question2():
    print(
        """
###########################################
############## Problem 2 ##################
###########################################
"""
    )
    while True:
        try:
            num = int(input("Your number at least 3 digits: "))
            if len(str(num)) >= 3:
                break
            else:
                print("Type at least 3 digits")
                continue
        except ValueError:
            print("Please just type number!!!")
            continue
    return (
        f"{num} is gapfull number" if is_gapful(num) else f"{num} is not gapfull number"
    )


def edges_not_zeros(a: float, b: float, c: float) -> bool:
    return a != 0 and b != 0 and c != 0


def is_nondegenerate_triangle(a: float, b: float, c: float) -> bool:
    a, b, c = sorted((a, b, c))
    return a + b > c


def is_degenerate_triangle(a: float, b: float, c: float) -> bool:
    return a + b == c or b + c == a or c + a == b


def is_normal_triangle(a: float, b: float, c: float) -> bool:
    return is_nondegenerate_triangle(a, b, c) and edges_not_zeros(a, b, c)


def is_right_triangle(a: float, b: float, c: float) -> bool:
    a, b, c = sorted((a, b, c))
    return a**2 + b**2 == c**2 and is_normal_triangle(a, b, c)


def median(a: int, b: int, c: int) -> float:
    a, b, c = sorted((a, b, c))
    return c / 2


def question3():
    print(
        """
###########################################
############## Problem 3 ##################
###########################################
"""
    )
    while True:
        try:
            a = int(input("Type a: "))
            b = int(input("Type b: "))
            c = int(input("Type c: "))
            break
        except ValueError:
            print("Please just type number!!!")
            continue
    return median(a, b, c) if is_right_triangle(a, b, c) else 0
