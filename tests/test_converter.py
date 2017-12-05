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
