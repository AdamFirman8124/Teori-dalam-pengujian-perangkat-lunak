

# Generated at 2026-10-24 15:27:53.572407
# Unit test for method is_right of class Right

# Generated at 2026-10-24 15:27:55.984466
# Unit test for method is_right of class Right

# Generated at 2026-10-24 15:27:58.398012
# Unit test for method is_right of class Right

# Generated at 2026-10-24 15:28:00.813354
# Unit test for method to_maybe of class Left

# Generated at 2026-10-24 15:28:03.226333
# Unit test for method to_maybe of class Left

# Generated at 2026-10-24 15:28:05.638894
# Unit test for method to_maybe of class Left

# Generated at 2026-10-24 15:28:08.250342
# Unit test for method bind of class Left

# Generated at 2026-10-24 15:28:10.665201
# Unit test for method bind of class Left

# Generated at 2026-10-24 15:28:13.077591
# Unit test for method bind of class Left

# Generated at 2026-10-24 15:28:15.491141
# Unit test for method bind of class Right

# Generated at 2026-10-24 15:28:17.904053
# Unit test for method bind of class Right

# Generated at 2026-10-24 15:28:20.316824
# Unit test for method bind of class Right

# Generated at 2026-10-24 15:28:22.729191
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 15:28:25.142322
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 15:28:27.555617
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 15:28:29.968123
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:28:32.382463
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:28:34.796978
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:28:37.209989
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 15:28:39.624280
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 15:28:42.038387
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 15:28:44.449647
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 15:28:46.862646
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 15:28:49.273926
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 15:28:51.686204
# Unit test for method case of class Either

# Generated at 2026-10-24 15:28:54.100885
# Unit test for method case of class Either

# Generated at 2026-10-24 15:28:56.512682
# Unit test for method case of class Either

# Generated at 2026-10-24 15:28:58.929150
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:29:01.342362
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:29:03.756043
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:29:06.173044
# Unit test for method to_validation of class Left

# Generated at 2026-10-24 15:29:08.585082
# Unit test for method to_validation of class Left

# Generated at 2026-10-24 15:29:10.997393
# Unit test for method to_validation of class Left

# Generated at 2026-10-24 15:29:12.370786
# Unit test for method to_validation of class Left
def test_Left_to_validation():
    assert Left(42).to_validation() == Validation.fail([42])

# Generated at 2026-10-24 15:29:13.682762
# Unit test for method to_validation of class Left
def test_Left_to_validation():
    assert Left(42).to_validation() == Validation.fail([42])

# Generated at 2026-10-24 15:29:14.997309
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # Right == Right when values match
    assert Right(42) == Right(42)

    # Right != Right when values differ
    assert Right(42) != Right(43)

    # Left == Left when values match
    assert Left(42) == Left(42)

    # Left != Left when values differ
    assert Left(42) != Left(43)

    # Same value but different sides -> not equal
    assert Right(42) != Left(42)
    assert Left(42) != Right(42)

    # Comparison against non-Either is False, not an error
    assert Right(42) != 42
    assert Left(42) != "42"
    assert Right(42) != None

    # Works with None values on both sides
    assert Right(None) == Right(None)
    assert Left(None) == Left(None)

    # Nested values compared by equality
    assert Right([1, 2]) == Right([1, 2])
    assert Right([1, 2]) != Right([1, 3])

# Generated at 2026-10-24 15:29:16.365402
# Unit test for method case of class Either
def test_Either_case():
    # Right: success handler is called with the value
    assert Right(42).case(lambda v: f"error: {v}", lambda v: f"success: {v}") == "success: 42"

    # Left: error handler is called with the value
    assert Left("boom").case(lambda v: f"error: {v}", lambda v: f"success: {v}") == "error: boom"

    # Only one handler runs â track calls
    calls = []

    def error_handler(v):
        calls.append(("error", v))
        return "from_error"

    def success_handler(v):
        calls.append(("success", v))
        return "from_success"

    # Right calls only success
    result = Right(7).case(error_handler, success_handler)
    assert result == "from_success"
    assert calls == [("success", 7)]

    # Left calls only error
    calls.clear()
    result = Left(7).case(error_handler, success_handler)
    assert result == "from_error"
    assert calls == [("error", 7)]

    # Handlers returning different types work (case is not type-restricted)
    assert Right(10).case(lambda v: [v], lambda v: v * 2) == 20
    assert Left(10).case(lambda v: [v], lambda v: v * 2) == [10]

    # Value passed through unchanged, identity handlers
    assert Right("x").case(lambda v: v, lambda v: v) == "x"
    assert Left("x").case(lambda v: v, lambda v: v) == "x"


if __name__ == "__main__":
    test_Either_case()
    print("All test_Either_case assertions passed.")

# Generated at 2026-10-24 15:29:17.775643
# Unit test for method case of class Either
def test_Either_case():
    assert Left(42).case(lambda error: error + 1, lambda success: success * 2) == 43
    assert Right(21).case(lambda error: error + 1, lambda success: success * 2) == 42
    assert Left('boom').case(lambda error: f'error: {error}', lambda success: f'ok: {success}') == 'error: boom'
    assert Right('value').case(lambda error: f'error: {error}', lambda success: f'ok: {success}') == 'ok: value'

# Generated at 2026-10-24 15:29:20.642032
# Unit test for method case of class Either
def test_Either_case():
    assert Left(42).case(lambda error: error + 1, lambda success: success * 2) == 43
    assert Right(21).case(lambda error: error + 1, lambda success: success * 2) == 42
    assert Left('boom').case(lambda error: f'error: {error}', lambda success: f'ok: {success}') == 'error: boom'
    assert Right('value').case(lambda error: f'error: {error}', lambda success: f'ok: {success}') == 'ok: value'

# Generated at 2026-10-24 15:29:21.963881
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # Right == Right when values match
    assert Right(42) == Right(42)

    # Right != Right when values differ
    assert Right(42) != Right(43)

    # Left == Left when values match
    assert Left(42) == Left(42)

    # Left != Left when values differ
    assert Left(42) != Left(43)

    # Same value but different sides -> not equal
    assert Right(42) != Left(42)
    assert Left(42) != Right(42)

    # Comparison against non-Either is False, not an error
    assert Right(42) != 42
    assert Left(42) != "42"
    assert Right(42) != None

    # Works with None values on both sides
    assert Right(None) == Right(None)
    assert Left(None) == Left(None)

    # Nested values compared by equality
    assert Right([1, 2]) == Right([1, 2])
    assert Right([1, 2]) != Right([1, 3])

# Generated at 2026-10-24 15:29:23.333695
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # Right == Right when values match
    assert Right(42) == Right(42)

    # Right != Right when values differ
    assert Right(42) != Right(43)

    # Left == Left when values match
    assert Left(42) == Left(42)

    # Left != Left when values differ
    assert Left(42) != Left(43)

    # Same value but different sides -> not equal
    assert Right(42) != Left(42)
    assert Left(42) != Right(42)

    # Comparison against non-Either is False, not an error
    assert Right(42) != 42
    assert Left(42) != "42"
    assert Right(42) != None

    # Works with None values on both sides
    assert Right(None) == Right(None)
    assert Left(None) == Left(None)

    # Nested values compared by equality
    assert Right([1, 2]) == Right([1, 2])
    assert Right([1, 2]) != Right([1, 3])

# Generated at 2026-10-24 15:29:24.749271
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # Right == Right when values match
    assert Right(42) == Right(42)

    # Right != Right when values differ
    assert Right(42) != Right(43)

    # Left == Left when values match
    assert Left(42) == Left(42)

    # Left != Left when values differ
    assert Left(42) != Left(43)

    # Same value but different sides -> not equal
    assert Right(42) != Left(42)
    assert Left(42) != Right(42)

    # Comparison against non-Either is False, not an error
    assert Right(42) != 42
    assert Left(42) != "42"
    assert Right(42) != None

    # Works with None values on both sides
    assert Right(None) == Right(None)
    assert Left(None) == Left(None)

    # Nested values compared by equality
    assert Right([1, 2]) == Right([1, 2])
    assert Right([1, 2]) != Right([1, 3])

# Generated at 2026-10-24 15:29:26.107108
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # Right == Right when values match
    assert Right(42) == Right(42)

    # Right != Right when values differ
    assert Right(42) != Right(43)

    # Left == Left when values match
    assert Left(42) == Left(42)

    # Left != Left when values differ
    assert Left(42) != Left(43)

    # Same value but different sides -> not equal
    assert Right(42) != Left(42)
    assert Left(42) != Right(42)

    # Comparison against non-Either is False, not an error
    assert Right(42) != 42
    assert Left(42) != "42"
    assert Right(42) != None

    # Works with None values on both sides
    assert Right(None) == Right(None)
    assert Left(None) == Left(None)

    # Nested values compared by equality
    assert Right([1, 2]) == Right([1, 2])
    assert Right([1, 2]) != Right([1, 3])

# Generated at 2026-10-24 15:29:27.462019
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # Right == Right when values match
    assert Right(42) == Right(42)

    # Right != Right when values differ
    assert Right(42) != Right(43)

    # Left == Left when values match
    assert Left(42) == Left(42)

    # Left != Left when values differ
    assert Left(42) != Left(43)

    # Same value but different sides -> not equal
    assert Right(42) != Left(42)
    assert Left(42) != Right(42)

    # Comparison against non-Either is False, not an error
    assert Right(42) != 42
    assert Left(42) != "42"
    assert Right(42) != None

    # Works with None values on both sides
    assert Right(None) == Right(None)
    assert Left(None) == Left(None)

    # Nested values compared by equality
    assert Right([1, 2]) == Right([1, 2])
    assert Right([1, 2]) != Right([1, 3])

# Generated at 2026-10-24 15:29:28.849308
# Unit test for method case of class Either
def test_Either_case():
    # Right: success handler is called with the value
    assert Right(42).case(lambda v: f"error: {v}", lambda v: f"success: {v}") == "success: 42"

    # Left: error handler is called with the value
    assert Left("boom").case(lambda v: f"error: {v}", lambda v: f"success: {v}") == "error: boom"

    # Only one handler runs â track calls
    calls = []

    def error_handler(v):
        calls.append(("error", v))
        return "from_error"

    def success_handler(v):
        calls.append(("success", v))
        return "from_success"

    # Right calls only success
    result = Right(7).case(error_handler, success_handler)
    assert result == "from_success"
    assert calls == [("success", 7)]

    # Left calls only error
    calls.clear()
    result = Left(7).case(error_handler, success_handler)
    assert result == "from_error"
    assert calls == [("error", 7)]

    # Handlers returning different types work (case is not type-restricted)
    assert Right(10).case(lambda v: [v], lambda v: v * 2) == 20
    assert Left(10).case(lambda v: [v], lambda v: v * 2) == [10]

    # Value passed through unchanged, identity handlers
    assert Right("x").case(lambda v: v, lambda v: v) == "x"
    assert Left("x").case(lambda v: v, lambda v: v) == "x"


if __name__ == "__main__":
    test_Either_case()
    print("All test_Either_case assertions passed.")

# Generated at 2026-10-24 15:29:30.193464
# Unit test for method case of class Either
def test_Either_case():
    assert Left(42).case(lambda error: error + 1, lambda success: success * 2) == 43
    assert Right(21).case(lambda error: error + 1, lambda success: success * 2) == 42
    assert Left('boom').case(lambda error: f'error: {error}', lambda success: f'ok: {success}') == 'error: boom'
    assert Right('value').case(lambda error: f'error: {error}', lambda success: f'ok: {success}') == 'ok: value'

# Generated at 2026-10-24 15:29:31.739584
# Unit test for method case of class Either
def test_Either_case():
    assert Left(42).case(lambda error: error + 1, lambda success: success * 2) == 43
    assert Right(21).case(lambda error: error + 1, lambda success: success * 2) == 42
    assert Left('boom').case(lambda error: f'error: {error}', lambda success: f'ok: {success}') == 'error: boom'
    assert Right('value').case(lambda error: f'error: {error}', lambda success: f'ok: {success}') == 'ok: value'

# Generated at 2026-10-24 15:29:34.363558
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:29:36.775042
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:29:39.188458
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:29:41.636504
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:29:44.017734
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:29:46.429986
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:29:48.848427
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:29:51.262238
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:29:53.681657
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:29:56.093050
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 15:29:58.506671
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 15:30:00.919403
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 15:30:03.493408
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 15:30:05.906755
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 15:30:08.320246
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 15:30:10.732876
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 15:30:13.161873
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 15:30:15.575755
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 15:30:17.988598
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 15:30:20.401939
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 15:30:22.814544
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 15:30:25.227957
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:30:27.640686
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:30:30.053763
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:30:32.468715
# Unit test for method case of class Either

# Generated at 2026-10-24 15:30:35.145862
# Unit test for method case of class Either
def test_Either_case():# Right: case should call the success handler with the value
    right = Right(5)
    result = right.case(lambda x: x * 2, lambda x: x + 1)
    assert result == 6, "Right.case should call success handler: expected 6, got %r" % (result,)

    # Left: case should call the error handler with the value
    left = Left(5)
    result = left.case(lambda x: x * 2, lambda x: x + 1)
    assert result == 10, "Left.case should call error handler: expected 10, got %r" % (result,)

    # Right: only the success handler is invoked (error handler must not run)
    right = Right("ok")
    sentinel = []
    right.case(lambda x: sentinel.append("error"), lambda x: sentinel.append("success"))
    assert sentinel == ["success"], "Right.case must call only success handler, got %r" % (sentinel,)

    # Left: only the error handler is invoked (success handler must not run)
    left = Left("oops")
    sentinel = []
    left.case(lambda x: sentinel.append("error"), lambda x: sentinel.append("success"))
    assert sentinel == ["error"], "Left.case must call only error handler, got %r" % (sentinel,)

    # Handlers may return different types than the stored value
    right = Right(3)
    assert right.case(lambda x: ["err", x], lambda x: "val-%d" % x) == "val-3"
    left = Left(3)
    assert left.case(lambda x: ["err", x], lambda x: "val-%d" % x) == ["err", 3]

# Generated at 2026-10-24 15:30:36.621564
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    # Right case preserves value inside Lazy
    right_lazy = Right(42).to_lazy()
    assert isinstance(right_lazy, Lazy)
    assert right_lazy.get() == 42

    # Left case preserves value inside Lazy
    left_lazy = Left("error").to_lazy()
    assert isinstance(left_lazy, Lazy)
    assert left_lazy.get() == "error"

# Generated at 2026-10-24 15:30:53.028912
# Unit test for method case of class Either
def test_Either_case():
    # Right: success handler is called with the value
    assert Right(42).case(lambda v: f"error: {v}", lambda v: f"success: {v}") == "success: 42"

    # Left: error handler is called with the value
    assert Left("boom").case(lambda v: f"error: {v}", lambda v: f"success: {v}") == "error: boom"

    # Only one handler runs â track calls
    calls = []

    def error_handler(v):
        calls.append(("error", v))
        return "from_error"

    def success_handler(v):
        calls.append(("success", v))
        return "from_success"

    # Right calls only success
    result = Right(7).case(error_handler, success_handler)
    assert result == "from_success"
    assert calls == [("success", 7)]

    # Left calls only error
    calls.clear()
    result = Left(7).case(error_handler, success_handler)
    assert result == "from_error"
    assert calls == [("error", 7)]

    # Handlers returning different types work (case is not type-restricted)
    assert Right(10).case(lambda v: [v], lambda v: v * 2) == 20
    assert Left(10).case(lambda v: [v], lambda v: v * 2) == [10]

    # Value passed through unchanged, identity handlers
    assert Right("x").case(lambda v: v, lambda v: v) == "x"
    assert Left("x").case(lambda v: v, lambda v: v) == "x"


if __name__ == "__main__":
    test_Either_case()
    print("All test_Either_case assertions passed.")

# Generated at 2026-10-24 15:30:54.367001
# Unit test for method case of class Either
def test_Either_case():
    assert Left(42).case(lambda error: error + 1, lambda success: success * 2) == 43
    assert Right(21).case(lambda error: error + 1, lambda success: success * 2) == 42
    assert Left('boom').case(lambda error: f'error: {error}', lambda success: f'ok: {success}') == 'error: boom'
    assert Right('value').case(lambda error: f'error: {error}', lambda success: f'ok: {success}') == 'ok: value'

# Generated at 2026-10-24 15:30:55.687632
# Unit test for method case of class Either
def test_Either_case():
    assert Left(42).case(lambda error: error + 1, lambda success: success * 2) == 43
    assert Right(21).case(lambda error: error + 1, lambda success: success * 2) == 42
    assert Left('boom').case(lambda error: f'error: {error}', lambda success: f'ok: {success}') == 'error: boom'
    assert Right('value').case(lambda error: f'error: {error}', lambda success: f'ok: {success}') == 'ok: value'

# Generated at 2026-10-24 15:30:57.000977
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # Right == Right when values match
    assert Right(42) == Right(42)

    # Right != Right when values differ
    assert Right(42) != Right(43)

    # Left == Left when values match
    assert Left(42) == Left(42)

    # Left != Left when values differ
    assert Left(42) != Left(43)

    # Same value but different sides -> not equal
    assert Right(42) != Left(42)
    assert Left(42) != Right(42)

    # Comparison against non-Either is False, not an error
    assert Right(42) != 42
    assert Left(42) != "42"
    assert Right(42) != None

    # Works with None values on both sides
    assert Right(None) == Right(None)
    assert Left(None) == Left(None)

    # Nested values compared by equality
    assert Right([1, 2]) == Right([1, 2])
    assert Right([1, 2]) != Right([1, 3])

# Generated at 2026-10-24 15:30:58.338635
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # Right == Right when values match
    assert Right(42) == Right(42)

    # Right != Right when values differ
    assert Right(42) != Right(43)

    # Left == Left when values match
    assert Left(42) == Left(42)

    # Left != Left when values differ
    assert Left(42) != Left(43)

    # Same value but different sides -> not equal
    assert Right(42) != Left(42)
    assert Left(42) != Right(42)

    # Comparison against non-Either is False, not an error
    assert Right(42) != 42
    assert Left(42) != "42"
    assert Right(42) != None

    # Works with None values on both sides
    assert Right(None) == Right(None)
    assert Left(None) == Left(None)

    # Nested values compared by equality
    assert Right([1, 2]) == Right([1, 2])
    assert Right([1, 2]) != Right([1, 3])

# Generated at 2026-10-24 15:30:59.665338
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # Right == Right when values match
    assert Right(42) == Right(42)

    # Right != Right when values differ
    assert Right(42) != Right(43)

    # Left == Left when values match
    assert Left(42) == Left(42)

    # Left != Left when values differ
    assert Left(42) != Left(43)

    # Same value but different sides -> not equal
    assert Right(42) != Left(42)
    assert Left(42) != Right(42)

    # Comparison against non-Either is False, not an error
    assert Right(42) != 42
    assert Left(42) != "42"
    assert Right(42) != None

    # Works with None values on both sides
    assert Right(None) == Right(None)
    assert Left(None) == Left(None)

    # Nested values compared by equality
    assert Right([1, 2]) == Right([1, 2])
    assert Right([1, 2]) != Right([1, 3])

# Generated at 2026-10-24 15:31:00.988983
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # Right == Right when values match
    assert Right(42) == Right(42)

    # Right != Right when values differ
    assert Right(42) != Right(43)

    # Left == Left when values match
    assert Left(42) == Left(42)

    # Left != Left when values differ
    assert Left(42) != Left(43)

    # Same value but different sides -> not equal
    assert Right(42) != Left(42)
    assert Left(42) != Right(42)

    # Comparison against non-Either is False, not an error
    assert Right(42) != 42
    assert Left(42) != "42"
    assert Right(42) != None

    # Works with None values on both sides
    assert Right(None) == Right(None)
    assert Left(None) == Left(None)

    # Nested values compared by equality
    assert Right([1, 2]) == Right([1, 2])
    assert Right([1, 2]) != Right([1, 3])

# Generated at 2026-10-24 15:31:02.308246
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # Right == Right when values match
    assert Right(42) == Right(42)

    # Right != Right when values differ
    assert Right(42) != Right(43)

    # Left == Left when values match
    assert Left(42) == Left(42)

    # Left != Left when values differ
    assert Left(42) != Left(43)

    # Same value but different sides -> not equal
    assert Right(42) != Left(42)
    assert Left(42) != Right(42)

    # Comparison against non-Either is False, not an error
    assert Right(42) != 42
    assert Left(42) != "42"
    assert Right(42) != None

    # Works with None values on both sides
    assert Right(None) == Right(None)
    assert Left(None) == Left(None)

    # Nested values compared by equality
    assert Right([1, 2]) == Right([1, 2])
    assert Right([1, 2]) != Right([1, 3])

# Generated at 2026-10-24 15:31:03.725687
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    # Right case preserves value inside Lazy
    right_lazy = Right(42).to_lazy()
    assert isinstance(right_lazy, Lazy)
    assert right_lazy.get() == 42

    # Left case preserves value inside Lazy
    left_lazy = Left("error").to_lazy()
    assert isinstance(left_lazy, Lazy)
    assert left_lazy.get() == "error"

# Generated at 2026-10-24 15:31:05.340385
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # Right == Right when values match
    assert Right(42) == Right(42)

    # Right != Right when values differ
    assert Right(42) != Right(43)

    # Left == Left when values match
    assert Left(42) == Left(42)

    # Left != Left when values differ
    assert Left(42) != Left(43)

    # Same value but different sides -> not equal
    assert Right(42) != Left(42)
    assert Left(42) != Right(42)

    # Comparison against non-Either is False, not an error
    assert Right(42) != 42
    assert Left(42) != "42"
    assert Right(42) != None

    # Works with None values on both sides
    assert Right(None) == Right(None)
    assert Left(None) == Left(None)

    # Nested values compared by equality
    assert Right([1, 2]) == Right([1, 2])
    assert Right([1, 2]) != Right([1, 3])

# Generated at 2026-10-24 15:31:07.969281
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:31:10.382851
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:31:12.934503
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:31:15.437977
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:31:17.850515
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:31:20.269396
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:31:22.681988
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:31:25.095469
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:31:27.842775
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:31:30.259760
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:31:32.671960
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:31:35.085797
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:31:37.500764
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:31:39.919180
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:31:42.331099
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:31:44.745430
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 15:31:47.161384
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 15:31:49.573571
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 15:31:51.989975
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 15:31:54.399607
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 15:31:56.814182
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 15:31:59.225981
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:32:01.639150
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:32:04.052037
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:32:06.465081
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 15:32:08.878986
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 15:32:11.293929
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 15:32:13.705177
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:32:16.121488
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:32:18.541342
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:32:20.958261
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:32:23.369861
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:32:25.784343
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:32:28.196162
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:32:30.607811
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:32:33.021133
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:32:35.432739
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 15:32:37.844366
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 15:32:40.256456
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 15:32:42.669630
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:32:45.083165
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:32:47.495571
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:32:49.912065
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:32:52.324157
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:32:54.736820
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:32:57.148743
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 15:32:59.560016
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 15:33:01.972855
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 15:33:04.386110
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:33:06.803456
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:33:09.223276
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:33:11.633392
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:33:14.045194
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:33:16.456428
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:33:18.868468
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:33:21.279985
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:33:23.692703
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:33:26.105710
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:33:28.519089
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:33:30.931684
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:33:33.344433
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:33:59.708085
# Unit test for method __eq__ of class Either
def test_Either___eq__():assert Left(1).__eq__(Left(1)) is True

# Generated at 2026-10-24 15:35:04.310814
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # Same side + same value -> equal
    assert Right(1) == Right(1)
    assert Left(1) == Left(1)
    assert Right("a") == Right("a")
    assert Left("a") == Left("a")

    # Same side + different value -> not equal
    assert Right(1) != Right(2)
    assert Left(1) != Left(2)
    assert not (Right(1) == Right(2))
    assert not (Left(1) == Left(2))

    # Same value + different side -> not equal
    assert Right(1) != Left(1)
    assert Left(1) != Right(1)
    assert not (Right(1) == Left(1))
    assert not (Left(1) == Right(1))

    # Different value + different side -> not equal
    assert Right(1) != Left(2)
    assert Left(1) != Right(2)

    # Comparison with non-Either -> not equal / False
    assert not (Right(1) == 1)
    assert not (Left(1) == 1)
    assert Right(1) != 1
    assert Left(1) != 1
    assert not (Right(1) == None)  # noqa: E711
    assert not (Left(1) == None)  # noqa: E711
    assert not (Right(1) == "1")
    assert Right(1) != object()

# Generated at 2026-10-24 15:35:31.355531
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # Same side + same value -> equal
    assert Right(1) == Right(1)
    assert Left(1) == Left(1)
    assert Right("a") == Right("a")
    assert Left("a") == Left("a")

    # Same side + different value -> not equal
    assert Right(1) != Right(2)
    assert Left(1) != Left(2)
    assert not (Right(1) == Right(2))
    assert not (Left(1) == Left(2))

    # Same value + different side -> not equal
    assert Right(1) != Left(1)
    assert Left(1) != Right(1)
    assert not (Right(1) == Left(1))
    assert not (Left(1) == Right(1))

    # Different value + different side -> not equal
    assert Right(1) != Left(2)
    assert Left(1) != Right(2)

    # Comparison with non-Either -> not equal / False
    assert not (Right(1) == 1)
    assert not (Left(1) == 1)
    assert Right(1) != 1
    assert Left(1) != 1
    assert not (Right(1) == None)  # noqa: E711
    assert not (Left(1) == None)  # noqa: E711
    assert not (Right(1) == "1")
    assert Right(1) != object()

# Generated at 2026-10-24 15:36:19.053873
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 15:36:44.674519
# Unit test for method __eq__ of class Either
def test_Either___eq__():right = Right(42)

# Generated at 2026-10-24 15:36:46.213095
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # Same side + same value -> equal
    assert Right(1) == Right(1)
    assert Left(1) == Left(1)
    assert Right("a") == Right("a")
    assert Left("a") == Left("a")

    # Same side + different value -> not equal
    assert Right(1) != Right(2)
    assert Left(1) != Left(2)
    assert not (Right(1) == Right(2))
    assert not (Left(1) == Left(2))

    # Same value + different side -> not equal
    assert Right(1) != Left(1)
    assert Left(1) != Right(1)
    assert not (Right(1) == Left(1))
    assert not (Left(1) == Right(1))

    # Different value + different side -> not equal
    assert Right(1) != Left(2)
    assert Left(1) != Right(2)

    # Comparison with non-Either -> not equal / False
    assert not (Right(1) == 1)
    assert not (Left(1) == 1)
    assert Right(1) != 1
    assert Left(1) != 1
    assert not (Right(1) == None)  # noqa: E711
    assert not (Left(1) == None)  # noqa: E711
    assert not (Right(1) == "1")
    assert Right(1) != object()

# Generated at 2026-10-24 15:36:47.643832
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # Same side + same value -> equal
    assert Right(1) == Right(1)
    assert Left(1) == Left(1)
    assert Right("a") == Right("a")
    assert Left("a") == Left("a")

    # Same side + different value -> not equal
    assert Right(1) != Right(2)
    assert Left(1) != Left(2)
    assert not (Right(1) == Right(2))
    assert not (Left(1) == Left(2))

    # Same value + different side -> not equal
    assert Right(1) != Left(1)
    assert Left(1) != Right(1)
    assert not (Right(1) == Left(1))
    assert not (Left(1) == Right(1))

    # Different value + different side -> not equal
    assert Right(1) != Left(2)
    assert Left(1) != Right(2)

    # Comparison with non-Either -> not equal / False
    assert not (Right(1) == 1)
    assert not (Left(1) == 1)
    assert Right(1) != 1
    assert Left(1) != 1
    assert not (Right(1) == None)  # noqa: E711
    assert not (Left(1) == None)  # noqa: E711
    assert not (Right(1) == "1")
    assert Right(1) != object()

# Generated at 2026-10-24 15:36:50.432564
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    # Right case preserves value inside Lazy
    right_lazy = Right(42).to_lazy()
    assert isinstance(right_lazy, Lazy)
    assert right_lazy.get() == 42

    # Left case preserves value inside Lazy
    left_lazy = Left("error").to_lazy()
    assert isinstance(left_lazy, Lazy)
    assert left_lazy.get() == "error"

# Generated at 2026-10-24 15:36:51.806203
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    # Right case preserves value inside Lazy
    right_lazy = Right(42).to_lazy()
    assert isinstance(right_lazy, Lazy)
    assert right_lazy.get() == 42

    # Left case preserves value inside Lazy
    left_lazy = Left("error").to_lazy()
    assert isinstance(left_lazy, Lazy)
    assert left_lazy.get() == "error"

# Generated at 2026-10-24 15:36:53.166470
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    # Right case preserves value inside Lazy
    right_lazy = Right(42).to_lazy()
    assert isinstance(right_lazy, Lazy)
    assert right_lazy.get() == 42

    # Left case preserves value inside Lazy
    left_lazy = Left("error").to_lazy()
    assert isinstance(left_lazy, Lazy)
    assert left_lazy.get() == "error"

# Generated at 2026-10-24 15:36:54.556078
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    # Right case preserves value inside Lazy
    right_lazy = Right(42).to_lazy()
    assert isinstance(right_lazy, Lazy)
    assert right_lazy.get() == 42

    # Left case preserves value inside Lazy
    left_lazy = Left("error").to_lazy()
    assert isinstance(left_lazy, Lazy)
    assert left_lazy.get() == "error"

# Generated at 2026-10-24 15:36:55.931198
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    # Right case preserves value inside Lazy
    right_lazy = Right(42).to_lazy()
    assert isinstance(right_lazy, Lazy)
    assert right_lazy.get() == 42

    # Left case preserves value inside Lazy
    left_lazy = Left("error").to_lazy()
    assert isinstance(left_lazy, Lazy)
    assert left_lazy.get() == "error"

# Generated at 2026-10-24 15:36:57.302574
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    # Right case preserves value inside Lazy
    right_lazy = Right(42).to_lazy()
    assert isinstance(right_lazy, Lazy)
    assert right_lazy.get() == 42

    # Left case preserves value inside Lazy
    left_lazy = Left("error").to_lazy()
    assert isinstance(left_lazy, Lazy)
    assert left_lazy.get() == "error"

# Generated at 2026-10-24 15:37:04.694611
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    # Right case preserves value inside Lazy
    right_lazy = Right(42).to_lazy()
    assert isinstance(right_lazy, Lazy)
    assert right_lazy.get() == 42

    # Left case preserves value inside Lazy
    left_lazy = Left("error").to_lazy()
    assert isinstance(left_lazy, Lazy)
    assert left_lazy.get() == "error"

# Generated at 2026-10-24 15:37:11.912017
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    # Right case preserves value inside Lazy
    right_lazy = Right(42).to_lazy()
    assert isinstance(right_lazy, Lazy)
    assert right_lazy.get() == 42

    # Left case preserves value inside Lazy
    left_lazy = Left("error").to_lazy()
    assert isinstance(left_lazy, Lazy)
    assert left_lazy.get() == "error"

# Generated at 2026-10-24 15:37:15.496834
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    # Right case preserves value inside Lazy
    right_lazy = Right(42).to_lazy()
    assert isinstance(right_lazy, Lazy)
    assert right_lazy.get() == 42

    # Left case preserves value inside Lazy
    left_lazy = Left("error").to_lazy()
    assert isinstance(left_lazy, Lazy)
    assert left_lazy.get() == "error"

# Generated at 2026-10-24 15:37:16.916227
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    # Right case preserves value inside Lazy
    right_lazy = Right(42).to_lazy()
    assert isinstance(right_lazy, Lazy)
    assert right_lazy.get() == 42

    # Left case preserves value inside Lazy
    left_lazy = Left("error").to_lazy()
    assert isinstance(left_lazy, Lazy)
    assert left_lazy.get() == "error"

# Generated at 2026-10-24 15:37:47.342632
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    # Right case preserves value inside Lazy
    right_lazy = Right(42).to_lazy()
    assert isinstance(right_lazy, Lazy)
    assert right_lazy.get() == 42

    # Left case preserves value inside Lazy
    left_lazy = Left("error").to_lazy()
    assert isinstance(left_lazy, Lazy)
    assert left_lazy.get() == "error"

# Generated at 2026-10-24 15:37:48.775839
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    # Right case preserves value inside Lazy
    right_lazy = Right(42).to_lazy()
    assert isinstance(right_lazy, Lazy)
    assert right_lazy.get() == 42

    # Left case preserves value inside Lazy
    left_lazy = Left("error").to_lazy()
    assert isinstance(left_lazy, Lazy)
    assert left_lazy.get() == "error"

# Generated at 2026-10-24 15:37:50.151330
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    # Right case preserves value inside Lazy
    right_lazy = Right(42).to_lazy()
    assert isinstance(right_lazy, Lazy)
    assert right_lazy.get() == 42

    # Left case preserves value inside Lazy
    left_lazy = Left("error").to_lazy()
    assert isinstance(left_lazy, Lazy)
    assert left_lazy.get() == "error"

# Generated at 2026-10-24 15:38:00.040020
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    # Right case preserves value inside Lazy
    right_lazy = Right(42).to_lazy()
    assert isinstance(right_lazy, Lazy)
    assert right_lazy.get() == 42

    # Left case preserves value inside Lazy
    left_lazy = Left("error").to_lazy()
    assert isinstance(left_lazy, Lazy)
    assert left_lazy.get() == "error"