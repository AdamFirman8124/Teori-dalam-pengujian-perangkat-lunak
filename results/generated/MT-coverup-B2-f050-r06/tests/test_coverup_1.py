# file: project/f050/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f050 import encode_shift


def test_encode_shift_executes_line_3():
    """Calling encode_shift with a non-empty string executes line 3
    (the list-comprehension return statement) and verifies the +5
    Caesar-shift postcondition."""
    # Basic shift: each letter moves 5 positions forward in the alphabet.
    assert encode_shift("hello") == "mjqqt"

    # Wrap-around branch: 'z' wraps back to 'e' via the modulo operation.
    assert encode_shift("xyz") == "cde"

    # 'a' maps to 'f'.
    assert encode_shift("a") == "f"

    # Empty string still executes line 3 (with an empty comprehension).
    assert encode_shift("") == ""
