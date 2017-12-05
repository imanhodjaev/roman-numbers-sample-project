# -*- coding: utf-8 -*-
import pytest

from roman_numerals import convert


def test_it_works():
    assert 1 == 1


def test_it_fails_on_zero_or_negative_number():
    with pytest.raises(ValueError):
        convert(0)

    with pytest.raises(ValueError):
        convert(-1)


def test_it_fails_when_input_type_is_not_an_int_number():
    with pytest.raises(ValueError):
        convert({})

    with pytest.raises(ValueError):
        convert(1.0)

    with pytest.raises(ValueError):
        convert('random string')


def test_it_works_and_converts_basic_roman_numerals():
    """Given table of basic literals, test if converting works correctly
    | Symbol |  I  |  V  |  X   |   L   |   C   |   D   |   M   |
    |--------|-----|-----|------|-------|-------|-------|-------|
    | Value  |  1  |  5  |  10  |   50  |  100  |  500  | 1000  |
    """
    assert convert(1) == 'I'
    assert convert(5) == 'V'
    assert convert(10) == 'X'
    assert convert(50) == 'L'
    assert convert(100) == 'C'
    assert convert(500) == 'D'
    assert convert(1000) == 'M'
