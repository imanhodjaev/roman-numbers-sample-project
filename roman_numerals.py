# -*- coding: utf-8 -*-


__all__ = ['convert']


def convert(number: int) -> str:
    """Convert decimal (arabic) numbers to roman numerals"""
    check_input(number)
    return ''


def check_input(number: int):
    if type(number) != int:
        raise ValueError('Input number must be integer')

    if number <= 0:
        raise ValueError('Input number must be positive integer')
