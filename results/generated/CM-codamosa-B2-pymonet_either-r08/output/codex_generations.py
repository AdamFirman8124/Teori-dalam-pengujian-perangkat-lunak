

# Generated at 2026-10-24 12:34:06.015796
# Unit test for method to_validation of class Left

# Generated at 2026-10-24 12:34:08.431342
# Unit test for method to_validation of class Left

# Generated at 2026-10-24 12:34:10.847722
# Unit test for method to_validation of class Left

# Generated at 2026-10-24 12:34:13.405197
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 12:34:15.820192
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 12:34:18.235265
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 12:34:20.650077
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 12:34:23.064475
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 12:34:25.479792
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 12:34:35.086841
# Unit test for constructor of class Either
def test_Either():
    either = Either(42)

    # constructor stores the value
    assert either.value == 42

    # equality compares value + is_right()
    assert Either(42) == Either(42)
    assert Either(42) != Either(43)

    # base Either is neither Left nor Right
    assert either.is_right() is None
    assert either.is_left() is not True
    assert Either(42) != Right(42)
    assert Either(42) != Left(42)

# Generated at 2026-10-24 12:34:47.583675
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

# Generated at 2026-10-24 12:34:54.925637
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

# Generated at 2026-10-24 12:34:57.350763
# Unit test for method to_validation of class Right

# Generated at 2026-10-24 12:34:59.759495
# Unit test for method to_validation of class Right

# Generated at 2026-10-24 12:35:02.171657
# Unit test for method to_validation of class Right

# Generated at 2026-10-24 12:35:04.586259
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 12:35:06.998799
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 12:35:09.411409
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 12:35:11.824976
# Unit test for method ap of class Left

# Generated at 2026-10-24 12:35:14.237915
# Unit test for method ap of class Left

# Generated at 2026-10-24 12:35:16.656152
# Unit test for method ap of class Left

# Generated at 2026-10-24 12:35:19.073032
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 12:35:21.484483
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 12:35:23.897062
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 12:35:26.309903
# Unit test for method to_maybe of class Right

# Generated at 2026-10-24 12:35:28.723515
# Unit test for method to_maybe of class Right

# Generated at 2026-10-24 12:35:31.135736
# Unit test for method to_maybe of class Right

# Generated at 2026-10-24 12:35:33.548917
# Unit test for method case of class Either

# Generated at 2026-10-24 12:35:35.966157
# Unit test for method case of class Either

# Generated at 2026-10-24 12:35:38.378155
# Unit test for method case of class Either

# Generated at 2026-10-24 12:35:40.792145
# Unit test for method to_validation of class Right

# Generated at 2026-10-24 12:35:43.206113
# Unit test for method to_validation of class Right

# Generated at 2026-10-24 12:35:45.619701
# Unit test for method to_validation of class Right

# Generated at 2026-10-24 12:35:48.032258
# Unit test for method to_validation of class Right

# Generated at 2026-10-24 12:35:50.449553
# Unit test for method to_validation of class Right

# Generated at 2026-10-24 12:35:52.865008
# Unit test for method to_validation of class Right

# Generated at 2026-10-24 12:35:55.280227
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 12:35:57.693422
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 12:36:00.102511
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 12:36:02.517092
# Unit test for method to_validation of class Right

# Generated at 2026-10-24 12:36:04.930456
# Unit test for method to_validation of class Right

# Generated at 2026-10-24 12:36:07.345571
# Unit test for method to_validation of class Right

# Generated at 2026-10-24 12:36:09.753538
# Unit test for method case of class Either

# Generated at 2026-10-24 12:36:12.171084
# Unit test for method case of class Either

# Generated at 2026-10-24 12:36:14.582892
# Unit test for method case of class Either

# Generated at 2026-10-24 12:36:16.996988
# Unit test for method ap of class Left

# Generated at 2026-10-24 12:36:19.410677
# Unit test for method ap of class Left

# Generated at 2026-10-24 12:36:21.821836
# Unit test for method ap of class Left

# Generated at 2026-10-24 12:36:24.235087
# Unit test for method case of class Either

# Generated at 2026-10-24 12:36:26.652635
# Unit test for method case of class Either

# Generated at 2026-10-24 12:36:29.069384
# Unit test for method case of class Either

# Generated at 2026-10-24 12:36:31.483341
# Unit test for method case of class Either

# Generated at 2026-10-24 12:36:33.895660
# Unit test for method case of class Either

# Generated at 2026-10-24 12:36:36.309804
# Unit test for method case of class Either

# Generated at 2026-10-24 12:36:38.723328
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 12:36:41.137862
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 12:36:43.551438
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 12:36:45.964000
# Unit test for method to_validation of class Right

# Generated at 2026-10-24 12:36:48.377514
# Unit test for method to_validation of class Right

# Generated at 2026-10-24 12:36:50.790473
# Unit test for method to_validation of class Right

# Generated at 2026-10-24 12:36:53.203117
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 12:36:55.616177
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 12:36:58.028886
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 12:37:00.445418
# Unit test for method to_validation of class Right

# Generated at 2026-10-24 12:37:02.861949
# Unit test for method to_validation of class Right

# Generated at 2026-10-24 12:37:05.273677
# Unit test for method to_validation of class Right

# Generated at 2026-10-24 12:37:07.686439
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 12:37:10.099249
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 12:37:12.512952
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 12:37:14.924272
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 12:37:17.337656
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 12:37:19.749478
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 12:37:22.162329
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 12:37:24.575312
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 12:37:26.990718
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 12:37:29.400996
# Unit test for method case of class Either

# Generated at 2026-10-24 12:37:31.813714
# Unit test for method case of class Either

# Generated at 2026-10-24 12:37:34.226829
# Unit test for method case of class Either

# Generated at 2026-10-24 12:37:36.642923
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 12:37:39.058643
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 12:37:41.483393
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 12:37:43.896093
# Unit test for method case of class Either

# Generated at 2026-10-24 12:37:46.309681
# Unit test for method case of class Either

# Generated at 2026-10-24 12:37:48.724015
# Unit test for method case of class Either

# Generated at 2026-10-24 12:37:51.135852
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 12:37:53.548390
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 12:37:55.961322
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 12:37:58.374931
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 12:38:00.798992
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 12:38:03.214684
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 12:38:05.625712
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 12:38:08.040283
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 12:38:10.454957
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 12:38:12.871544
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 12:38:15.287950
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 12:38:17.704768
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 12:38:20.116049
# Unit test for method case of class Either

# Generated at 2026-10-24 12:38:22.528817
# Unit test for method case of class Either

# Generated at 2026-10-24 12:38:24.942444
# Unit test for method case of class Either

# Generated at 2026-10-24 12:38:27.353761
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 12:38:29.766389
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 12:38:32.179066
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 12:38:34.592068
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 12:38:37.004637
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 12:38:39.417720
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 12:38:41.830487
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 12:38:44.243897
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 12:38:46.656519
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 12:38:49.074027
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 12:38:51.489999
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 12:38:53.901075
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 12:38:56.313480
# Unit test for method case of class Either

# Generated at 2026-10-24 12:38:58.725983
# Unit test for method case of class Either

# Generated at 2026-10-24 12:39:01.138101
# Unit test for method case of class Either

# Generated at 2026-10-24 12:39:03.550600
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 12:39:05.963403
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 12:39:08.376610
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 12:39:10.789900
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 12:39:13.202259
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 12:39:15.615822
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 12:39:18.028447
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 12:39:20.441375
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 12:39:22.854903
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 12:39:25.267585
# Unit test for method case of class Either

# Generated at 2026-10-24 12:39:27.712824
# Unit test for method case of class Either

# Generated at 2026-10-24 12:39:30.092609
# Unit test for method case of class Either

# Generated at 2026-10-24 12:39:32.504943
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 12:39:34.917677
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 12:39:37.330666
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 12:39:45.164429
# Unit test for method case of class Either
def test_Either_case():calls = []


# Generated at 2026-10-24 12:40:02.923983
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

# Generated at 2026-10-24 12:40:04.357323
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

# Generated at 2026-10-24 12:40:05.831096
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

# Generated at 2026-10-24 12:40:07.178394
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

# Generated at 2026-10-24 12:40:08.562498
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

# Generated at 2026-10-24 12:40:10.009407
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

# Generated at 2026-10-24 12:40:11.442870
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

# Generated at 2026-10-24 12:40:12.876394
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

# Generated at 2026-10-24 12:40:15.477604
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 12:40:17.891323
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 12:40:20.305030
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 12:40:23.603615
# Unit test for method case of class Either

# Generated at 2026-10-24 12:40:26.016349
# Unit test for method case of class Either

# Generated at 2026-10-24 12:40:28.429818
# Unit test for method case of class Either

# Generated at 2026-10-24 12:40:30.843837
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 12:40:33.255981
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 12:40:35.669648
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 12:40:38.083588
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 12:40:40.495825
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 12:40:42.908021
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 12:41:19.131620
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 12:41:36.745520
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

# Generated at 2026-10-24 12:41:39.176591
# Unit test for method case of class Either

# Generated at 2026-10-24 12:41:41.595809
# Unit test for method case of class Either

# Generated at 2026-10-24 12:41:44.013680
# Unit test for method case of class Either

# Generated at 2026-10-24 12:41:46.431648
# Unit test for method case of class Either

# Generated at 2026-10-24 12:41:51.086949
# Unit test for method case of class Either
def test_Either_case():assert Left("error").case(lambda value: f"failed: {value}", lambda value: f"success: {value}") == "failed: error"

# Generated at 2026-10-24 12:41:54.766619
# Unit test for method case of class Either
def test_Either_case():error = lambda value: f"error: {value}"

# Generated at 2026-10-24 12:41:56.086588
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

# Generated at 2026-10-24 12:42:23.233111
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

# Generated at 2026-10-24 12:42:28.455806
# Unit test for method case of class Either
def test_Either_case():assert Left("error").case(lambda value: f"left: {value}", lambda value: f"right: {value}") == "left: error"

# Generated at 2026-10-24 12:42:31.104252
# Unit test for method case of class Either

# Generated at 2026-10-24 12:42:33.518914
# Unit test for method case of class Either

# Generated at 2026-10-24 12:42:35.935568
# Unit test for method case of class Either

# Generated at 2026-10-24 12:42:38.354916
# Unit test for method case of class Either

# Generated at 2026-10-24 12:42:40.901780
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 12:42:43.318488
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 12:42:45.732107
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 12:42:49.114162
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 12:43:01.738249
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

# Generated at 2026-10-24 12:43:23.345599
# Unit test for method case of class Either
def test_Either_case():
    error_handler = lambda value: f"error: {value}"
    success_handler = lambda value: f"success: {value}"

    assert Left("failure").case(error_handler, success_handler) == "error: failure"
    assert Right("result").case(error_handler, success_handler) == "success: result"

# Generated at 2026-10-24 12:43:27.042981
# Unit test for method case of class Either
def test_Either_case():assert Right(3).case(lambda value: f"error:{value}", lambda value: value * 2) == 6

# Generated at 2026-10-24 12:43:32.153649
# Unit test for method case of class Either
def test_Either_case():assert Right(42).case(
        lambda value: f"error: {value}",
        lambda value: f"success: {value}",
    ) == "success: 42"

# Generated at 2026-10-24 12:43:33.557690
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

# Generated at 2026-10-24 12:43:35.056823
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

# Generated at 2026-10-24 12:43:36.462187
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

# Generated at 2026-10-24 12:43:37.766654
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

# Generated at 2026-10-24 12:43:39.082907
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

# Generated at 2026-10-24 12:43:41.502051
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 12:43:43.918057
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 12:43:46.332393
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 12:43:48.748867
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 12:43:51.165401
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 12:43:57.339588
# Unit test for method __eq__ of class Either
def test_Either___eq__():assert Left(42) == Left(42)

# Generated at 2026-10-24 12:43:58.660552
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

# Generated at 2026-10-24 12:44:03.191563
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

# Generated at 2026-10-24 12:44:04.610411
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

# Generated at 2026-10-24 12:44:05.978565
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