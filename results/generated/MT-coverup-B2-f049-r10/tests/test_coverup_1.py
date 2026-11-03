# file: project/f049/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[4, 5], [4, 6]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[4, 5], [4, 6]]}

from f049 import modp


def test_modp_executes_loop_body_and_return():
    # n > 0: executes lines 3 (ret = 1), 4 (loop), 5 (loop body), and 6 (return)
    assert modp(3, 5) == 3        # 2^3 = 8 -> 8 % 5 == 3
    assert modp(3, 11) == 8       # 2^3 = 8 -> 8 % 11 == 8
    assert modp(10, 101) == 14    # 2^10 = 1024 -> 1024 % 101 == 14
    assert modp(100, 101) == 1    # Fermat's little theorem: 2^100 ≡ 1 (mod 101)
    assert modp(1101, 101) == 2   # 2^1101 ≡ 2^(1101 % 100) = 2^1 = 2 (mod 101)


def test_modp_zero_iterations():
    # n == 0: loop body (line 5) is skipped, but lines 3, 4, and 6 still execute
    assert modp(0, 101) == 1      # 2^0 = 1 -> 1 % 101 == 1
    assert modp(0, 5) == 1        # 2^0 = 1 -> 1 % 5 == 1
