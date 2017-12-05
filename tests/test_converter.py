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


def test_it_work_with_other_numbers():
    assert convert(1776) == 'MDCCLXXVI'     # Date written on the book held by the Statue of Liberty
    assert convert(1954) == 'MCMLIV'        # As in the trailer for the movie The Last Time I Saw Paris
    assert convert(1990) == 'MCMXC'         # Used as the title of musical project Enigma's debut album MCMXC a.D., named after the year of its release.
    assert convert(2014) == 'MMXIV'         # The year of the games of the XXII (22nd) Olympic Winter Games (in Sochi)
    assert convert(2017) == 'MMXVII'
    assert convert(2018) == 'MMXVIII'
    assert convert(717) == 'DCCXVII'
    assert convert(777) == 'DCCLXXVII'
    assert convert(888) == 'DCCCLXXXVIII'
    assert convert(36) == 'XXXVI'
