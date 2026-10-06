# file: script_95.py:1-34
# asked: {"lines": [13, 14, 16, 17, 19, 20, 21, 22, 23, 24, 25, 26, 28, 29, 30, 31, 33, 34], "branches": [[13, 14], [13, 16], [17, 19], [17, 34], [19, 20], [19, 22], [22, 23], [22, 29], [23, 24], [23, 25], [25, 26], [25, 28], [29, 30], [29, 33]]}
# gained: {"lines": [13, 14, 16, 17, 19, 20, 21, 22, 23, 24, 25, 26, 28, 29, 30, 31, 33, 34], "branches": [[13, 14], [13, 16], [17, 19], [17, 34], [19, 20], [19, 22], [22, 23], [22, 29], [23, 24], [23, 25], [25, 26], [25, 28], [29, 30], [29, 33]]}

import pytest
import sys
import os

# Import the function from script_95.py
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from script_95 import check_dict_case


def test_empty_dict():
    assert check_dict_case({}) == False


def test_non_string_key():
    assert check_dict_case({"a": "apple", 8: "banana"}) == False


def test_all_uppercase_keys():
    assert check_dict_case({"STATE": "NC", "ZIP": "12345"}) == True


def test_all_lowercase_keys():
    assert check_dict_case({"a": "apple", "b": "banana"}) == True


def test_mixed_case_keys():
    assert check_dict_case({"a": "apple", "A": "banana", "B": "banana"}) == False


def test_key_neither_upper_nor_lower():
    assert check_dict_case({"Name": "John", "Age": "36"}) == False


def test_uppercase_then_lowercase():
    assert check_dict_case({"ABC": "test", "def": "test"}) == False


def test_lowercase_then_uppercase():
    assert check_dict_case({"abc": "test", "DEF": "test"}) == False


def test_single_uppercase_key():
    assert check_dict_case({"ABC": "value"}) == True


def test_single_lowercase_key():
    assert check_dict_case({"abc": "value"}) == True


def test_single_mixed_case_key():
    assert check_dict_case({"Abc": "value"}) == False
