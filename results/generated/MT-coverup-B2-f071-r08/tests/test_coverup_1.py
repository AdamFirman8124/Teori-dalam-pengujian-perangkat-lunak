# file: project/f071/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5]]}

from f071 import triangle_area


def test_invalid_first_condition_a_plus_b_le_c():
    assert triangle_area(1, 2, 3) == -1


def test_invalid_second_condition_a_plus_c_le_b():
    # 2 + 2 <= 5 is False for first check (2+5<=2 False), True for second (2+2<=5 True)
    assert triangle_area(2, 5, 2) == -1


def test_invalid_third_condition_b_plus_c_le_a():
    # first two or-operands False, third True: 5+2<=2 False, 5+2<=2 False, 2+2<=5 True
    assert triangle_area(5, 2, 2) == -1


def test_valid_right_triangle():
    # s = 6, area = sqrt(6*3*2*1) = 6.0
    assert triangle_area(3, 4, 5) == 6.0


def test_valid_isosceles_with_rounding():
    # s = 8, area = sqrt(8*3*3*2) = 12.0
    assert triangle_area(5, 5, 6) == 12.0
    # s = 3.5, area = sqrt(3.9375) ~= 1.9843 -> 1.98
    assert triangle_area(2, 2, 3) == 1.98
