

# Generated at 2026-10-24 14:14:44.885412
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

# Generated at 2026-10-24 14:14:46.216724
# Unit test for method case of class Either
def test_Either_case():
    assert Left(42).case(lambda error: error + 1, lambda success: success * 2) == 43
    assert Right(21).case(lambda error: error + 1, lambda success: success * 2) == 42
    assert Left('boom').case(lambda error: f'error: {error}', lambda success: f'ok: {success}') == 'error: boom'
    assert Right('value').case(lambda error: f'error: {error}', lambda success: f'ok: {success}') == 'ok: value'

# Generated at 2026-10-24 14:14:47.612172
# Unit test for method case of class Either
def test_Either_case():
    assert Left(42).case(lambda error: error + 1, lambda success: success * 2) == 43
    assert Right(21).case(lambda error: error + 1, lambda success: success * 2) == 42
    assert Left('boom').case(lambda error: f'error: {error}', lambda success: f'ok: {success}') == 'error: boom'
    assert Right('value').case(lambda error: f'error: {error}', lambda success: f'ok: {success}') == 'ok: value'

# Generated at 2026-10-24 14:14:54.464858
# Unit test for method to_validation of class Left
def test_Left_to_validation():
    assert Left(42).to_validation() == Validation.fail([42])

# Generated at 2026-10-24 14:14:56.885501
# Unit test for method is_left of class Left

# Generated at 2026-10-24 14:14:59.305558
# Unit test for method is_left of class Left

# Generated at 2026-10-24 14:15:01.990811
# Unit test for method is_left of class Left

# Generated at 2026-10-24 14:15:04.550651
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:15:06.965521
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:15:09.382061
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:15:11.796951
# Unit test for method ap of class Either

# Generated at 2026-10-24 14:15:14.217272
# Unit test for method ap of class Either

# Generated at 2026-10-24 14:15:16.635995
# Unit test for method ap of class Either

# Generated at 2026-10-24 14:15:19.054091
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:15:21.472608
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:15:23.890621
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:15:25.304308
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

# Generated at 2026-10-24 14:15:35.833489
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    lazy = Right(42).to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.get() == 42

    lazy_left = Left('error').to_lazy()
    assert isinstance(lazy_left, Lazy)
    assert lazy_left.get() == 'error'

# Generated at 2026-10-24 14:15:51.994518
# Unit test for method ap of class Left
def test_Left_ap():
    left = Left("error")

    # ap with Right should be ignored -> copy of self
    result = left.ap(Right(42))
    assert isinstance(result, Left)
    assert result == Left("error")
    assert result.value == "error"
    assert result.is_left() is True
    assert result.is_right() is False
    assert result is not left

    # ap with Left should keep original error, not argument error
    other = Left("other error")
    result2 = left.ap(other)
    assert isinstance(result2, Left)
    assert result2 == Left("error")
    assert result2 == left
    assert result2 != other

    # function inside Left must not be applied
    fn_left = Left(lambda x: x + 1)
    result3 = fn_left.ap(Right(5))
    assert isinstance(result3, Left)
    assert result3 is not fn_left
    assert result3.value is fn_left.value

# Generated at 2026-10-24 14:15:53.319295
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

# Generated at 2026-10-24 14:15:59.795823
# Unit test for method is_right of class Left
def test_Left_is_right():
    """Left.is_right() should return False."""
    assert Left(42).is_right() is False

# Generated at 2026-10-24 14:16:01.122021
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

# Generated at 2026-10-24 14:16:17.622252
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

# Generated at 2026-10-24 14:16:18.932447
# Unit test for method case of class Either
def test_Either_case():
    assert Left(42).case(lambda error: error + 1, lambda success: success * 2) == 43
    assert Right(21).case(lambda error: error + 1, lambda success: success * 2) == 42
    assert Left('boom').case(lambda error: f'error: {error}', lambda success: f'ok: {success}') == 'error: boom'
    assert Right('value').case(lambda error: f'error: {error}', lambda success: f'ok: {success}') == 'ok: value'

# Generated at 2026-10-24 14:16:21.589796
# Unit test for method case of class Either

# Generated at 2026-10-24 14:16:24.001978
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 14:16:54.068470
# Unit test for method __eq__ of class Either
def test_Either___eq__():assert Left(1).__eq__(Left(1)) is True

# Generated at 2026-10-24 14:17:10.661894
# Unit test for method case of class Either
def test_Either_case():
    # Right should call `success` with its value
    assert Right(10).case(
        lambda err: "error",
        lambda value: value * 2
    ) == 20

    # Left should call `error` with its value
    assert Left("fail").case(
        lambda err: f"got {err}",
        lambda value: "success"
    ) == "got fail"

    # Only the matching branch is executed
    calls = []
    def error_fn(value):
        calls.append(("error", value))
        return "error-result"

    def success_fn(value):
        calls.append(("success", value))
        return "success-result"

    assert Right(42).case(error_fn, success_fn) == "success-result"
    assert calls == [("success", 42)]

    calls.clear()

    assert Left("oops").case(error_fn, success_fn) == "error-result"
    assert calls == [("error", "oops")]

# Generated at 2026-10-24 14:17:13.424068
# Unit test for method case of class Either

# Generated at 2026-10-24 14:17:16.003190
# Unit test for method case of class Either

# Generated at 2026-10-24 14:17:18.414557
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:17:20.828241
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:17:23.383569
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:17:25.798300
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:17:28.217161
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:17:30.629138
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:17:33.045439
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 14:17:35.460296
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 14:17:37.873915
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 14:17:40.286650
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:17:42.698806
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:17:45.113905
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:17:47.533184
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:17:49.945363
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:17:52.361941
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:17:54.778408
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:17:57.195016
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:17:59.618736
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:18:02.035959
# Unit test for method case of class Either

# Generated at 2026-10-24 14:18:04.454375
# Unit test for method case of class Either

# Generated at 2026-10-24 14:18:06.873817
# Unit test for method case of class Either

# Generated at 2026-10-24 14:18:09.292744
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:18:11.709890
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:18:14.122564
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:18:16.538401
# Unit test for method case of class Either

# Generated at 2026-10-24 14:18:18.952731
# Unit test for method case of class Either

# Generated at 2026-10-24 14:18:21.362988
# Unit test for method case of class Either

# Generated at 2026-10-24 14:18:23.776166
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 14:18:26.189952
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 14:18:36.150321
# Unit test for method __eq__ of class Either
def test_Either___eq__():assert Left(1) == Left(1)

# Generated at 2026-10-24 14:18:37.533306
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

# Generated at 2026-10-24 14:18:39.028827
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

# Generated at 2026-10-24 14:18:40.379278
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

# Generated at 2026-10-24 14:18:56.848302
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

# Generated at 2026-10-24 14:18:59.380525
# Unit test for method case of class Either

# Generated at 2026-10-24 14:19:01.799074
# Unit test for method case of class Either

# Generated at 2026-10-24 14:19:04.223554
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:19:06.755450
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:19:09.158969
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:19:11.572779
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:19:13.990227
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:19:16.414353
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:19:18.831093
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:19:21.249838
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:19:23.667578
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:19:26.083611
# Unit test for method case of class Either

# Generated at 2026-10-24 14:19:28.498622
# Unit test for method case of class Either

# Generated at 2026-10-24 14:19:30.912809
# Unit test for method case of class Either

# Generated at 2026-10-24 14:19:33.324643
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:19:35.742099
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:19:38.152120
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:19:54.809674
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

# Generated at 2026-10-24 14:19:56.133527
# Unit test for method case of class Either
def test_Either_case():
    assert Left(42).case(lambda error: error + 1, lambda success: success * 2) == 43
    assert Right(21).case(lambda error: error + 1, lambda success: success * 2) == 42
    assert Left('boom').case(lambda error: f'error: {error}', lambda success: f'ok: {success}') == 'error: boom'
    assert Right('value').case(lambda error: f'error: {error}', lambda success: f'ok: {success}') == 'ok: value'

# Generated at 2026-10-24 14:19:57.462677
# Unit test for method case of class Either
def test_Either_case():
    assert Left(42).case(lambda error: error + 1, lambda success: success * 2) == 43
    assert Right(21).case(lambda error: error + 1, lambda success: success * 2) == 42
    assert Left('boom').case(lambda error: f'error: {error}', lambda success: f'ok: {success}') == 'error: boom'
    assert Right('value').case(lambda error: f'error: {error}', lambda success: f'ok: {success}') == 'ok: value'

# Generated at 2026-10-24 14:19:58.815231
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

# Generated at 2026-10-24 14:20:00.237570
# Unit test for method case of class Either
def test_Either_case():
    assert Left(42).case(lambda error: error + 1, lambda success: success * 2) == 43
    assert Right(21).case(lambda error: error + 1, lambda success: success * 2) == 42
    assert Left('boom').case(lambda error: f'error: {error}', lambda success: f'ok: {success}') == 'error: boom'
    assert Right('value').case(lambda error: f'error: {error}', lambda success: f'ok: {success}') == 'ok: value'

# Generated at 2026-10-24 14:20:01.665757
# Unit test for method case of class Either
def test_Either_case():
    assert Left(42).case(lambda error: error + 1, lambda success: success * 2) == 43
    assert Right(21).case(lambda error: error + 1, lambda success: success * 2) == 42
    assert Left('boom').case(lambda error: f'error: {error}', lambda success: f'ok: {success}') == 'error: boom'
    assert Right('value').case(lambda error: f'error: {error}', lambda success: f'ok: {success}') == 'ok: value'

# Generated at 2026-10-24 14:20:18.362587
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

# Generated at 2026-10-24 14:20:20.775520
# Unit test for method case of class Either

# Generated at 2026-10-24 14:20:23.190535
# Unit test for method case of class Either

# Generated at 2026-10-24 14:20:25.605849
# Unit test for method case of class Either

# Generated at 2026-10-24 14:20:28.024516
# Unit test for method case of class Either

# Generated at 2026-10-24 14:20:30.440249
# Unit test for method case of class Either

# Generated at 2026-10-24 14:20:32.856714
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 14:20:35.278430
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 14:20:37.800075
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 14:20:40.219926
# Unit test for method case of class Either

# Generated at 2026-10-24 14:20:41.592370
# Unit test for method case of class Either
def test_Either_case():
    assert Left(42).case(lambda error: error + 1, lambda success: success * 2) == 43
    assert Right(21).case(lambda error: error + 1, lambda success: success * 2) == 42
    assert Left('boom').case(lambda error: f'error: {error}', lambda success: f'ok: {success}') == 'error: boom'
    assert Right('value').case(lambda error: f'error: {error}', lambda success: f'ok: {success}') == 'ok: value'

# Generated at 2026-10-24 14:20:42.910649
# Unit test for method case of class Either
def test_Either_case():
    assert Left(42).case(lambda error: error + 1, lambda success: success * 2) == 43
    assert Right(21).case(lambda error: error + 1, lambda success: success * 2) == 42
    assert Left('boom').case(lambda error: f'error: {error}', lambda success: f'ok: {success}') == 'error: boom'
    assert Right('value').case(lambda error: f'error: {error}', lambda success: f'ok: {success}') == 'ok: value'

# Generated at 2026-10-24 14:20:44.326814
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

# Generated at 2026-10-24 14:20:45.656120
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

# Generated at 2026-10-24 14:20:46.999782
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

# Generated at 2026-10-24 14:20:48.321720
# Unit test for method case of class Either
def test_Either_case():
    assert Left(42).case(lambda error: error + 1, lambda success: success * 2) == 43
    assert Right(21).case(lambda error: error + 1, lambda success: success * 2) == 42
    assert Left('boom').case(lambda error: f'error: {error}', lambda success: f'ok: {success}') == 'error: boom'
    assert Right('value').case(lambda error: f'error: {error}', lambda success: f'ok: {success}') == 'ok: value'

# Generated at 2026-10-24 14:20:49.632585
# Unit test for method case of class Either
def test_Either_case():
    assert Left(42).case(lambda error: error + 1, lambda success: success * 2) == 43
    assert Right(21).case(lambda error: error + 1, lambda success: success * 2) == 42
    assert Left('boom').case(lambda error: f'error: {error}', lambda success: f'ok: {success}') == 'error: boom'
    assert Right('value').case(lambda error: f'error: {error}', lambda success: f'ok: {success}') == 'ok: value'

# Generated at 2026-10-24 14:20:50.960446
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

# Generated at 2026-10-24 14:20:52.298195
# Unit test for method case of class Either
def test_Either_case():
    assert Left(42).case(lambda error: error + 1, lambda success: success * 2) == 43
    assert Right(21).case(lambda error: error + 1, lambda success: success * 2) == 42
    assert Left('boom').case(lambda error: f'error: {error}', lambda success: f'ok: {success}') == 'error: boom'
    assert Right('value').case(lambda error: f'error: {error}', lambda success: f'ok: {success}') == 'ok: value'

# Generated at 2026-10-24 14:20:53.629107
# Unit test for method case of class Either
def test_Either_case():
    assert Left(42).case(lambda error: error + 1, lambda success: success * 2) == 43
    assert Right(21).case(lambda error: error + 1, lambda success: success * 2) == 42
    assert Left('boom').case(lambda error: f'error: {error}', lambda success: f'ok: {success}') == 'error: boom'
    assert Right('value').case(lambda error: f'error: {error}', lambda success: f'ok: {success}') == 'ok: value'

# Generated at 2026-10-24 14:20:54.988257
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

# Generated at 2026-10-24 14:20:57.609270
# Unit test for method case of class Either

# Generated at 2026-10-24 14:21:00.025606
# Unit test for method case of class Either

# Generated at 2026-10-24 14:21:02.675630
# Unit test for method case of class Either

# Generated at 2026-10-24 14:21:05.088616
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:21:07.502506
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:21:09.919695
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:21:12.330934
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 14:21:14.748466
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 14:21:17.162435
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 14:21:19.576530
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:21:21.991763
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:21:24.405487
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:21:26.833265
# Unit test for method case of class Either

# Generated at 2026-10-24 14:21:29.268217
# Unit test for method case of class Either

# Generated at 2026-10-24 14:21:31.695988
# Unit test for method case of class Either

# Generated at 2026-10-24 14:21:34.109797
# Unit test for method case of class Either

# Generated at 2026-10-24 14:21:36.551156
# Unit test for method case of class Either

# Generated at 2026-10-24 14:21:38.979049
# Unit test for method case of class Either

# Generated at 2026-10-24 14:21:41.395496
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:21:43.810256
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:21:46.226054
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:21:48.640989
# Unit test for method case of class Either

# Generated at 2026-10-24 14:21:51.056570
# Unit test for method case of class Either

# Generated at 2026-10-24 14:21:53.493179
# Unit test for method case of class Either

# Generated at 2026-10-24 14:21:55.935405
# Unit test for method case of class Either

# Generated at 2026-10-24 14:21:58.365060
# Unit test for method case of class Either

# Generated at 2026-10-24 14:22:00.778275
# Unit test for method case of class Either

# Generated at 2026-10-24 14:22:03.192269
# Unit test for method case of class Either

# Generated at 2026-10-24 14:22:05.606935
# Unit test for method case of class Either

# Generated at 2026-10-24 14:22:08.021195
# Unit test for method case of class Either

# Generated at 2026-10-24 14:22:11.639752
# Unit test for method case of class Either

# Generated at 2026-10-24 14:22:14.052083
# Unit test for method case of class Either

# Generated at 2026-10-24 14:22:16.468701
# Unit test for method case of class Either

# Generated at 2026-10-24 14:22:18.883113
# Unit test for method case of class Either

# Generated at 2026-10-24 14:22:21.296958
# Unit test for method case of class Either

# Generated at 2026-10-24 14:22:23.714209
# Unit test for method case of class Either

# Generated at 2026-10-24 14:22:26.127600
# Unit test for method case of class Either

# Generated at 2026-10-24 14:22:29.033737
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

# Generated at 2026-10-24 14:22:30.556005
# Unit test for method case of class Either
def test_Either_case():
    # Right should call `success` with its value
    assert Right(10).case(
        lambda err: "error",
        lambda value: value * 2
    ) == 20

    # Left should call `error` with its value
    assert Left("fail").case(
        lambda err: f"got {err}",
        lambda value: "success"
    ) == "got fail"

    # Only the matching branch is executed
    calls = []
    def error_fn(value):
        calls.append(("error", value))
        return "error-result"

    def success_fn(value):
        calls.append(("success", value))
        return "success-result"

    assert Right(42).case(error_fn, success_fn) == "success-result"
    assert calls == [("success", 42)]

    calls.clear()

    assert Left("oops").case(error_fn, success_fn) == "error-result"
    assert calls == [("error", "oops")]

# Generated at 2026-10-24 14:22:31.989464
# Unit test for method case of class Either
def test_Either_case():
    assert Left(42).case(lambda error: error + 1, lambda success: success * 2) == 43
    assert Right(21).case(lambda error: error + 1, lambda success: success * 2) == 42
    assert Left('boom').case(lambda error: f'error: {error}', lambda success: f'ok: {success}') == 'error: boom'
    assert Right('value').case(lambda error: f'error: {error}', lambda success: f'ok: {success}') == 'ok: value'

# Generated at 2026-10-24 14:22:33.423836
# Unit test for method case of class Either
def test_Either_case():
    assert Left(42).case(lambda error: error + 1, lambda success: success * 2) == 43
    assert Right(21).case(lambda error: error + 1, lambda success: success * 2) == 42
    assert Left('boom').case(lambda error: f'error: {error}', lambda success: f'ok: {success}') == 'error: boom'
    assert Right('value').case(lambda error: f'error: {error}', lambda success: f'ok: {success}') == 'ok: value'

# Generated at 2026-10-24 14:22:34.856709
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

# Generated at 2026-10-24 14:22:36.289894
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

# Generated at 2026-10-24 14:22:37.725629
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

# Generated at 2026-10-24 14:22:39.157896
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

# Generated at 2026-10-24 14:22:40.520857
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

# Generated at 2026-10-24 14:22:56.978317
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

# Generated at 2026-10-24 14:22:59.396123
# Unit test for method case of class Either

# Generated at 2026-10-24 14:23:01.978046
# Unit test for method case of class Either

# Generated at 2026-10-24 14:23:05.797859
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 14:23:08.213190
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 14:23:10.628574
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 14:23:13.260138
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 14:23:15.672134
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 14:23:18.086837
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 14:23:20.505922
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 14:23:22.916100
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 14:23:25.339157
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 14:23:27.757112
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 14:23:30.171646
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 14:23:32.588043
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 14:23:35.002312
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:23:37.417854
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:23:39.062280
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():from pymonet.either import Left, Right
from pymonet.lazy import Lazy

right = Right(42).to_lazy()
assert isinstance(right, Lazy)
assert right.get() == 42

left = Left('error').to_lazy()
assert isinstance(left, Lazy)
assert left.get() == 'error'

called = []
def make():
    called.append(1)
    return 1
lazy_from_call = Right(make).to_lazy()
assert lazy_from_call.get()() == 1
assert called == [1]

# Generated at 2026-10-24 14:23:40.496367
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

# Generated at 2026-10-24 14:23:41.823764
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

# Generated at 2026-10-24 14:23:43.270922
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

# Generated at 2026-10-24 14:23:44.578435
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

# Generated at 2026-10-24 14:23:46.029433
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

# Generated at 2026-10-24 14:23:49.013836
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

# Generated at 2026-10-24 14:23:50.436289
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

# Generated at 2026-10-24 14:23:51.863670
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

# Generated at 2026-10-24 14:23:53.186299
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

# Generated at 2026-10-24 14:23:54.626522
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

# Generated at 2026-10-24 14:23:56.060068
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

# Generated at 2026-10-24 14:23:57.596472
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

# Generated at 2026-10-24 14:23:59.036061
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

# Generated at 2026-10-24 14:24:00.434607
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

# Generated at 2026-10-24 14:24:02.972011
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:24:05.386902
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:24:07.949016
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:24:14.339584
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:24:16.754814
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:24:19.170419
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:24:21.584851
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 14:24:23.999559
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 14:24:26.414324
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 14:24:28.835525
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:24:31.250759
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:24:33.669766
# Unit test for method to_lazy of class Either