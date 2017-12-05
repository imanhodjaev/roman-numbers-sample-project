# -*- coding: utf-8 -*-
from collections import OrderedDict

__all__ = ['convert']

PAIRS = OrderedDict({
    1000: 'M',
    900: 'CM',
    500: 'D',
    400: 'CD',
    100: 'C',
    90: 'XC',
    50: 'L',
    40: 'XL',
    10: 'X',
    9: 'IX',
    5: 'V',
    4: 'IV',
    1: 'I',
})


def convert(number: int) -> str:
    """Convert decimal (arabic) numbers to roman numerals"""
    check_input(number)
    result = ''

    for num in PAIRS.keys():
        count, rem = divmod(number, num)
        result += PAIRS[num] * count
        number -= num * count

    return result


def check_input(number: int):
    if type(number) != int:
        raise ValueError('Input number must be integer')

    if number <= 0:
        raise ValueError('Input number must be positive integer')
