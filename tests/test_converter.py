# -*- coding: utf-8 -*-
import pytest

from roman_numerals import convert


def test_it_works():
    assert 1 == 1


def test_it_fail_on_zero_or_negative_number():
    with pytest.raises(ValueError):
        convert(0)

    with pytest.raises(ValueError):
        convert(-1)
