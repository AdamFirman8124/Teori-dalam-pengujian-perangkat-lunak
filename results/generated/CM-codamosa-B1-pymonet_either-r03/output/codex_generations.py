

# Generated at 2026-10-24 13:53:43.083803
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

# Generated at 2026-10-24 13:53:47.712869
# Unit test for method bind of class Right
def test_Right_bind():
    right = Right(2)

    result = right.bind(lambda value: Right(value * 3))

    assert result == Right(6)

# Generated at 2026-10-24 13:53:54.840562
# Unit test for method is_right of class Either
def test_Either_is_right():
    assert Right(1).is_right() is True
    assert Left(1).is_right() is False
    assert Right(None).is_right() is True   # value type doesn't affect the flag
    assert Left(None).is_right() is False

# Generated at 2026-10-24 13:53:57.269093
# Unit test for method map of class Right

# Generated at 2026-10-24 13:53:59.841227
# Unit test for method map of class Right

# Generated at 2026-10-24 13:54:02.281970
# Unit test for method map of class Right

# Generated at 2026-10-24 13:54:04.700826
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 13:54:07.111446
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 13:54:09.524785
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 13:54:11.938122
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 13:54:14.363434
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 13:54:16.999996
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 13:54:19.411672
# Unit test for method to_maybe of class Right

# Generated at 2026-10-24 13:54:31.035347
# Unit test for method to_maybe of class Right
def test_Right_to_maybe():from pymonet.maybe import Maybe


# Generated at 2026-10-24 13:54:35.694355
# Unit test for method is_left of class Left
def test_Left_is_left():
    left = Left("error")

    assert left.is_left() is True

# Generated at 2026-10-24 13:54:37.026994
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

# Generated at 2026-10-24 13:54:49.211101
# Unit test for method to_maybe of class Right
def test_Right_to_maybe():
    from pymonet.maybe import Maybe

    value = 42
    maybe = Right(value).to_maybe()

    assert isinstance(maybe, Maybe)
    assert maybe.is_just() is True
    assert maybe.is_nothing() is False
    assert maybe.value == value

    # sanity check: the Maybe still maps like a Just
    assert maybe.map(lambda x: x + 1).value == 43

# Generated at 2026-10-24 13:54:50.542255
# Unit test for method to_maybe of class Right
def test_Right_to_maybe():
    from pymonet.maybe import Maybe

    value = 42
    maybe = Right(value).to_maybe()

    assert isinstance(maybe, Maybe)
    assert maybe.is_just() is True
    assert maybe.is_nothing() is False
    assert maybe.value == value

    # sanity check: the Maybe still maps like a Just
    assert maybe.map(lambda x: x + 1).value == 43

# Generated at 2026-10-24 13:54:54.927210
# Unit test for method is_left of class Left
def test_Left_is_left():
    left = Left("error")

    assert left.is_left() is True

# Generated at 2026-10-24 13:54:56.266082
# Unit test for method to_maybe of class Right
def test_Right_to_maybe():
    from pymonet.maybe import Maybe

    value = 42
    maybe = Right(value).to_maybe()

    assert isinstance(maybe, Maybe)
    assert maybe.is_just() is True
    assert maybe.is_nothing() is False
    assert maybe.value == value

    # sanity check: the Maybe still maps like a Just
    assert maybe.map(lambda x: x + 1).value == 43

# Generated at 2026-10-24 13:55:03.042386
# Unit test for method to_box of class Either
def test_Either_to_box():
    from pymonet.box import Box

    right_box = Right(42).to_box()
    left_box = Left("error").to_box()

    assert isinstance(right_box, Box)
    assert right_box.value == 42

    assert isinstance(left_box, Box)
    assert left_box.value == "error"

# Generated at 2026-10-24 13:55:05.458795
# Unit test for method to_box of class Either

# Generated at 2026-10-24 13:55:07.873485
# Unit test for method to_box of class Either

# Generated at 2026-10-24 13:55:10.453392
# Unit test for method to_box of class Either

# Generated at 2026-10-24 13:55:12.867657
# Unit test for method case of class Either

# Generated at 2026-10-24 13:55:15.457715
# Unit test for method case of class Either

# Generated at 2026-10-24 13:55:17.868080
# Unit test for method case of class Either

# Generated at 2026-10-24 13:55:20.386408
# Unit test for method ap of class Either

# Generated at 2026-10-24 13:55:22.803524
# Unit test for method ap of class Either

# Generated at 2026-10-24 13:55:28.944610
# Unit test for method ap of class Either
def test_Either_ap():result = Right(lambda value: value + 1).ap(Right(2))

# Generated at 2026-10-24 13:55:30.378288
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

# Generated at 2026-10-24 13:55:32.015958
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

# Generated at 2026-10-24 13:55:33.460378
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

# Generated at 2026-10-24 13:55:35.095506
# Unit test for method ap of class Either
def test_Either_ap():
    add_one = lambda x: x + 1

    # Right.ap (inherited from Either): applicative.map(self.value)
    # -> Right(fn).ap(Right(v)) == Right(fn(v))
    assert Right(add_one).ap(Right(1)) == Right(2)

    # Right.ap works with any applicative that has .map, e.g. Box
    from pymonet.box import Box
    assert Right(add_one).ap(Box(1)) == Box(2)

    # Left.ap ignores the applicative and returns a copy of itself
    assert Left(add_one).ap(Right(1)) == Left(add_one)
    assert Left(add_one).ap(Box(1)) == Left(add_one)

    # ap on Left does not call the function
    def boom(_):
        raise AssertionError("function must not be called")
    Left(add_one).ap(Right(boom))  # no exception raised

# Generated at 2026-10-24 13:55:36.526407
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

# Generated at 2026-10-24 13:55:37.879398
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

# Generated at 2026-10-24 13:55:39.279970
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

# Generated at 2026-10-24 13:55:40.588073
# Unit test for method ap of class Either
def test_Either_ap():
    add_one = lambda x: x + 1

    # Right.ap (inherited from Either): applicative.map(self.value)
    # -> Right(fn).ap(Right(v)) == Right(fn(v))
    assert Right(add_one).ap(Right(1)) == Right(2)

    # Right.ap works with any applicative that has .map, e.g. Box
    from pymonet.box import Box
    assert Right(add_one).ap(Box(1)) == Box(2)

    # Left.ap ignores the applicative and returns a copy of itself
    assert Left(add_one).ap(Right(1)) == Left(add_one)
    assert Left(add_one).ap(Box(1)) == Left(add_one)

    # ap on Left does not call the function
    def boom(_):
        raise AssertionError("function must not be called")
    Left(add_one).ap(Right(boom))  # no exception raised

# Generated at 2026-10-24 13:56:15.027498
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

# Generated at 2026-10-24 13:56:17.691434
# Unit test for method case of class Either

# Generated at 2026-10-24 13:56:20.115015
# Unit test for method case of class Either

# Generated at 2026-10-24 13:56:22.534718
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 13:56:24.953769
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 13:56:27.372940
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 13:56:28.801315
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

# Generated at 2026-10-24 13:56:30.286746
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

# Generated at 2026-10-24 13:56:31.717138
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

# Generated at 2026-10-24 13:56:33.094388
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

# Generated at 2026-10-24 13:56:34.430480
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

# Generated at 2026-10-24 13:56:35.811144
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

# Generated at 2026-10-24 13:56:52.421562
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

# Generated at 2026-10-24 13:57:17.489713
# Unit test for method case of class Either
def test_Either_case():assert Left("err").case(lambda x: f"got error {x}", lambda x: f"got success {x}") == "got error err"

# Generated at 2026-10-24 13:57:19.902935
# Unit test for method case of class Either

# Generated at 2026-10-24 13:57:22.563491
# Unit test for method case of class Either

# Generated at 2026-10-24 13:57:24.983657
# Unit test for method case of class Either

# Generated at 2026-10-24 13:57:27.403844
# Unit test for method case of class Either

# Generated at 2026-10-24 13:57:29.819811
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 13:57:32.240603
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 13:57:34.655061
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 13:57:37.072664
# Unit test for method case of class Either

# Generated at 2026-10-24 13:57:44.933958
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

# Generated at 2026-10-24 13:57:46.364552
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

# Generated at 2026-10-24 13:57:47.728390
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

# Generated at 2026-10-24 13:57:49.127277
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

# Generated at 2026-10-24 13:57:50.563608
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

# Generated at 2026-10-24 13:58:07.987161
# Unit test for method case of class Either
def test_Either_case():assert Left("err").case(lambda x: f"got error {x}", lambda x: f"got success {x}") == "got error err"

# Generated at 2026-10-24 13:58:13.911322
# Unit test for method case of class Either
def test_Either_case():
    assert Left(42).case(lambda error: error + 1, lambda success: success * 2) == 43
    assert Right(21).case(lambda error: error + 1, lambda success: success * 2) == 42
    assert Left('boom').case(lambda error: f'error: {error}', lambda success: f'ok: {success}') == 'error: boom'
    assert Right('value').case(lambda error: f'error: {error}', lambda success: f'ok: {success}') == 'ok: value'

# Generated at 2026-10-24 13:58:16.494269
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 13:58:18.911695
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 13:58:21.329914
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 13:58:23.741762
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 13:58:26.362225
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 13:58:28.781873
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 13:58:31.625783
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 13:58:34.039293
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 13:58:36.454002
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 13:58:38.865897
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 13:58:40.276325
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    from pymonet.either import Either, Left, Right

    # Right vs Right
    assert Right(1) == Right(1)
    assert not (Right(1) == Right(2))

    # Left vs Left
    assert Left(1) == Left(1)
    assert not (Left(1) == Left(2))

    # Left vs Right with equal values must NOT be equal
    assert not (Left(1) == Right(1))
    assert not (Right(1) == Left(1))

    # Comparison with non-Either objects
    assert not (Right(1) == 1)
    assert not (Left(1) == 1)
    assert not (Right(1) == object())

    # Base Either compares value and is_right()
    assert Either(3) == Either(3)
    assert not (Either(3) == Either(4))

# Generated at 2026-10-24 13:58:41.727627
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

# Generated at 2026-10-24 13:58:43.092747
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

# Generated at 2026-10-24 13:58:44.526716
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

# Generated at 2026-10-24 13:58:45.962455
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

# Generated at 2026-10-24 13:58:47.393821
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

# Generated at 2026-10-24 13:58:48.827228
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

# Generated at 2026-10-24 13:58:50.269940
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

# Generated at 2026-10-24 13:58:51.694655
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

# Generated at 2026-10-24 13:58:53.127872
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

# Generated at 2026-10-24 13:58:54.562001
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

# Generated at 2026-10-24 13:58:56.013518
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

# Generated at 2026-10-24 13:58:57.428756
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

# Generated at 2026-10-24 13:58:58.863645
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

# Generated at 2026-10-24 13:59:01.505051
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 13:59:04.118398
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 13:59:06.533023
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 13:59:09.132655
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 13:59:11.546579
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 13:59:13.964437
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 13:59:16.379924
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 13:59:18.797207
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 13:59:21.209112
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 13:59:23.622120
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 13:59:26.038149
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 13:59:28.451838
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 13:59:30.863706
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 13:59:33.277472
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 13:59:35.691034
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 13:59:38.106527
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 13:59:40.518336
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 13:59:42.933152
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 13:59:45.346105
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 13:59:47.759143
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 13:59:50.172251
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 13:59:52.782949
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 13:59:55.195752
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 13:59:57.610424
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:00:00.023672
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:00:02.436301
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:00:03.784155
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

# Generated at 2026-10-24 14:00:05.629700
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

# Generated at 2026-10-24 14:00:07.045813
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

# Generated at 2026-10-24 14:00:08.709844
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

# Generated at 2026-10-24 14:00:10.237049
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

# Generated at 2026-10-24 14:00:11.618889
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

# Generated at 2026-10-24 14:00:13.046754
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

# Generated at 2026-10-24 14:00:14.416512
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

# Generated at 2026-10-24 14:00:15.792628
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

# Generated at 2026-10-24 14:00:17.758372
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

# Generated at 2026-10-24 14:00:19.250370
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

# Generated at 2026-10-24 14:00:20.786610
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

# Generated at 2026-10-24 14:00:22.216252
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

# Generated at 2026-10-24 14:00:23.650078
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

# Generated at 2026-10-24 14:00:26.065033
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:00:28.585952
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:00:30.999533
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:00:33.412219
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:00:35.824193
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:00:38.544713
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:00:40.957275
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:00:43.372554
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:00:45.785118
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:00:48.197278
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:00:50.611058
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:00:53.225746
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:00:55.640121
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:00:58.053778
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:01:00.467055
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:01:05.185732
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:01:07.598241
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:01:14.160165
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():from pymonet.either import Either, Left, Right

# Generated at 2026-10-24 14:01:15.670288
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

# Generated at 2026-10-24 14:01:17.206857
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

# Generated at 2026-10-24 14:01:18.635624
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

# Generated at 2026-10-24 14:01:20.054413
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

# Generated at 2026-10-24 14:01:21.507399
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

# Generated at 2026-10-24 14:01:22.891393
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

# Generated at 2026-10-24 14:01:24.285388
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

# Generated at 2026-10-24 14:01:25.660825
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

# Generated at 2026-10-24 14:01:27.022186
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

# Generated at 2026-10-24 14:01:37.498391
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

# Generated at 2026-10-24 14:01:40.187725
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:01:42.605291
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:01:45.162853
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:01:47.580940
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:01:50.101560
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:01:52.511955
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:01:54.924570
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:01:57.480889
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:01:59.893119
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:02:02.305797
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:02:04.716891
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:02:07.129969
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:02:09.543321
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:02:11.955239
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:02:14.368483
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:02:16.781503
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:02:19.194547
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:02:21.610330
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:02:24.020963
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:02:26.433669
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:02:28.846578
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:02:31.259453
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:02:33.672084
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:02:36.086168
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:02:38.498229
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:02:40.910623
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:02:43.324115
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 14:03:03.702563
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

# Generated at 2026-10-24 14:03:05.238574
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

# Generated at 2026-10-24 14:03:06.768796
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

# Generated at 2026-10-24 14:03:08.209331
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

# Generated at 2026-10-24 14:03:09.795532
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

# Generated at 2026-10-24 14:03:11.283951
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

# Generated at 2026-10-24 14:03:13.027216
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

# Generated at 2026-10-24 14:03:14.398327
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

# Generated at 2026-10-24 14:03:15.888236
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

# Generated at 2026-10-24 14:03:17.302497
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