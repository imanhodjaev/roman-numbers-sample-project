# -*- coding: utf-8 -*-

"""This package provides utility function to convert decimal (Arabic)
numbers to Roman numerals.
"""

import argparse

from collections import OrderedDict


# We just want to export entry point and converter
__all__ = ['convert', 'main']

# Define mapping of known numbers to roman values
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
    """Convert decimal (arabic) numbers to roman numerals

    :param number: int
    :return: Decimal number converted to Roman representation
    """
    check_input(number)
    result = ''

    for num in PAIRS.keys():
        count, rem = divmod(number, num)
        result += PAIRS[num] * count
        number -= num * count

    return result


def check_input(number: int):
    """Checks validity of a given input and fails if input is malformed

    :param number: int
    :return: None
    """
    if type(number) != int:
        raise ValueError('Input number must be integer')

    if number <= 0:
        raise ValueError('Input number must be positive integer')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--number', type=int, help='Number to convert to roman representation')

    args = parser.parse_args()

    if args.number:
        print(convert(int(args.number)))


if __name__ == '__main__':
    main()
