

# Generated at 2022-06-14 03:31:37.724838
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda value: value == 1) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda value: value == 0) == Maybe.nothing()

    assert Maybe.nothing().filter(lambda value: value == 1) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda value: value == 0) == Maybe.nothing()



# Generated at 2022-06-14 03:31:43.145832
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    def gt_three(value):
        return value > 3
    assert Maybe.just(2).filter(gt_three) == Maybe.nothing()
    assert Maybe.nothing().filter(gt_three) == Maybe.nothing()
    assert Maybe.just(5).filter(gt_three) == Maybe.just(5)

# Generated at 2022-06-14 03:31:50.365343
# Unit test for method filter of class Maybe
def test_Maybe_filter():

    # Positive case
    maybe = Maybe.just(4)
    filtered = maybe.filter(lambda x: x % 4 == 0)
    assert filtered == Maybe.just(4)

    # Negative case
    maybe = Maybe.just(4)
    filtered = maybe.filter(lambda x: x % 3 == 0)
    assert filtered == Maybe.nothing()

    # Empty case
    maybe = Maybe.nothing()
    filtered = maybe.filter(lambda x: x % 3 == 0)
    assert filtered == Maybe.nothing()


# Generated at 2022-06-14 03:31:52.850284
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()

    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()


# Generated at 2022-06-14 03:32:01.363380
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    task_list = [
        {'input': (lambda x: x % 2 == 0, Maybe.just(2)), 'expected': Maybe.just(2)},
        {'input': (lambda x: x % 2 == 0, Maybe.just(21)), 'expected': Maybe.nothing()},
        {'input': (lambda x: True, Maybe.nothing()), 'expected': Maybe.nothing()}
    ]
    for task in task_list:
        assert task['input'][1].filter(task['input'][0]) == task['expected']


# Generated at 2022-06-14 03:32:07.815798
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(None)


# Generated at 2022-06-14 03:32:12.772124
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) == Maybe.just(1.0)
    assert Maybe.just(1) == Maybe.just('1')
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)


# Generated at 2022-06-14 03:32:17.667156
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Maybe[int].just(2).to_lazy() == Lazy(lambda: 2)
    assert Maybe[int].nothing().to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 03:32:26.556961
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert (
            Maybe.just(1)
            .filter(lambda x: x == 1)
            .get_or_else(-1)
    ) == 1

    assert (
            Maybe.just(1)
            .filter(lambda x: x == 2)
            .get_or_else(-1)
    ) == -1

    assert (
            Maybe.nothing()
            .filter(lambda x: x == 2)
            .get_or_else(-1)
    ) == -1



# Generated at 2022-06-14 03:32:29.807198
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe(5, False) == Maybe(5, False)
    assert Maybe(5, False) != Maybe(4, False)
    assert Maybe(5, True) == Maybe(5, True)
    assert Maybe(5, False) != Maybe(5, True)



# Generated at 2022-06-14 03:32:39.827365
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != '1'


# Generated at 2022-06-14 03:32:43.246501
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 123) == Maybe.just(123).to_lazy()
    assert Lazy(lambda: None) == Maybe.nothing().to_lazy()

# Generated at 2022-06-14 03:32:53.940297
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.box import Box
    from pymonet.lazy import Lazy
    from pymonet.either import Left, Right
    from pymonet.validation import Validation

    assert isinstance(Maybe.just(1).to_lazy(), Lazy)
    assert isinstance(Maybe.just(1).to_lazy().run(), int)
    assert Maybe.just(1).to_lazy().run() == 1

    assert isinstance(Maybe.nothing().to_lazy(), Lazy)
    assert isinstance(Maybe.nothing().to_lazy().run(), type(None))
    assert Maybe.nothing().to_lazy().run() == None

# Generated at 2022-06-14 03:33:00.655442
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    maybe_success_value = Maybe.just(1)
    maybe_success_value_filter_result = maybe_success_value.filter(lambda x: x > 0)
    assert maybe_success_value_filter_result.is_nothing is False
    assert maybe_success_value_filter_result.value == 1

    maybe_failed_value = Maybe.just(-1)
    maybe_failed_value_filter_result = maybe_failed_value.filter(lambda x: x > 0)
    assert maybe_failed_value_filter_result.is_nothing is True



# Generated at 2022-06-14 03:33:04.505286
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    maybe_value = Maybe.just(5)
    lazy_value = maybe_value.to_lazy()
    assert lazy_value.force() == 5


# Generated at 2022-06-14 03:33:08.165120
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) != Maybe.nothing()


# Generated at 2022-06-14 03:33:12.987779
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(2) == Maybe.just(2)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(2) != Maybe.nothing()
    assert Maybe.just(2) != Maybe.just(3)
    assert Maybe.just(3) == Maybe.just(3)
    assert Maybe.just(3) != Maybe.nothing()


# Generated at 2022-06-14 03:33:16.513481
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(3) == Maybe.just(3)
    assert Maybe.just(3).value == 3
    assert Maybe.just(3) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:33:20.451253
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)
    assert Maybe.just(1) != Maybe.nothing()

# Generated at 2022-06-14 03:33:25.366408
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(True) == Maybe.just(True)
    assert Maybe.just('hello') == Maybe.just('hello')
    assert Maybe.nothing() == Maybe.nothing()

    assert Maybe.nothing() != Maybe.just(1)
    assert Maybe.just([1, 2, 3]) != Maybe.just(True)
    assert Maybe.just(False) != Maybe.just('hello')


# Generated at 2022-06-14 03:33:35.411784
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    five = Maybe(5, False)
    filtered_five = five.filter(lambda v: v < 10)
    assert filtered_five == Maybe(5, False)

    ten = Maybe(10, False)
    filtered_ten = ten.filter(lambda v: v < 10)
    assert filtered_ten == Maybe(None, True)



# Generated at 2022-06-14 03:33:39.220215
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Maybe.just('value').to_lazy() == Lazy(lambda: 'value')
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:33:43.375785
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1), 'Should be True'
    assert Maybe.just(2) == Maybe.just(1), 'Should be False'
    assert Maybe.nothing() == Maybe.just(1), 'Should be False'
    assert Maybe.nothing() == Maybe.nothing(), 'Should be True'



# Generated at 2022-06-14 03:33:48.314966
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    from pymonet.box import Box

    assert(Maybe.just(1) == Maybe.just(1))
    assert(Maybe.just(1) != Maybe.nothing())
    assert(Maybe.nothing() == Maybe.nothing())
    assert(Maybe.just(1) != Maybe.just(2))
    assert(Maybe.just(1) != Box(1))


# Generated at 2022-06-14 03:33:57.478414
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda v: v == 2) == Maybe.nothing()
    assert Maybe.just(1).filter(lambda v: v == 1) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda v: v == 1).filter(lambda v: v == 1) == Maybe.just(1)
    assert Maybe.nothing().filter(lambda v: True) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda v: False) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda v: False).filter(lambda v: True) == Maybe.nothing()


# Generated at 2022-06-14 03:34:00.363030
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe.just(100).to_lazy().eval() == 100
    assert Maybe.nothing().to_lazy().eval() is None

# Generated at 2022-06-14 03:34:04.386490
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    result = Maybe.just(20).to_lazy()

    assert isinstance(result, Lazy)
    assert result.unwrap() == 20


# Generated at 2022-06-14 03:34:15.554098
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    from pymonet.maybes import Maybe

    assert Maybe.just(1).filter(lambda x: x % 2 == 0) == Maybe.nothing()
    assert Maybe.just(2).filter(lambda x: x % 2 == 0) == Maybe.just(2)
    assert Maybe.just(2).filter(lambda x: x + 1 == 0) == Maybe.nothing()
    assert Maybe.just(2).filter(lambda x: x + 3 == 0) == Maybe.nothing()
    assert Maybe.just(2).filter(lambda x: x + 1 == 3) == Maybe.nothing()
    assert Maybe.just(2).filter(lambda x: x + 3 == 5) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x == 0) == Maybe.nothing()


# Generated at 2022-06-14 03:34:19.160928
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: x > 0) == Maybe.just(1)
    assert Maybe.just(-1).filter(lambda x: x > 0) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x > 0) == Maybe.nothing()


# Generated at 2022-06-14 03:34:24.386112
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)


# Generated at 2022-06-14 03:34:32.566038
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.nothing() is False
    assert Maybe.just(1) == Maybe.just(1) is True
    assert Maybe.nothing() == Maybe.nothing() is True



# Generated at 2022-06-14 03:34:42.540203
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    from pymonet.monad_test import MonadTest
    from pymonet.asserts import assert_equals

    number: Maybe[int] = Maybe.just(42)
    not_number: Maybe[int] = Maybe.just(None)
    just_nothing: Maybe[None] = Maybe.nothing()

    def is_even(value: int) -> bool:
        return value % 2 == 0

    is_odd = lambda value: not is_even(value)

    assert_equals(number.filter(is_even), Maybe.just(42))
    assert_equals(number.filter(is_odd), Maybe.nothing())

    assert_equals(not_number.filter(is_even), Maybe.nothing())
    assert_equals(not_number.filter(is_odd), Maybe.nothing())

    assert_

# Generated at 2022-06-14 03:34:51.265873
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    @pytest.mark.parametrize('value, filterer, expected', [
        (1, lambda x: x > 0, Just(1)),
        (1, lambda x: x == 0, Nothing),
        (None, lambda x: x is None, Just(None)),
        (None, lambda x: x is not None, Nothing)
    ])
    def test_Maybe_filter(value, filterer, expected):
        assert Maybe.just(value).filter(filterer) == expected

    test_Maybe_filter()

# Generated at 2022-06-14 03:34:59.480904
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe(True, False).filter(lambda x: x == True) == Maybe.just(True)
    assert Maybe(True, False).filter(lambda x: x == False) == Maybe.nothing()
    assert Maybe(True, True).filter(lambda x: x == True) == Maybe.nothing()
    assert Maybe(None, False).filter(lambda x: x == None) == Maybe.just(None)
    assert Maybe(10, False).filter(lambda x: x > 10) == Maybe.nothing()
    assert Maybe(10, False).filter(lambda x: x < 10) == Maybe.nothing()
    assert Maybe(10, False).filter(lambda x: x == 10) == Maybe.just(10)
    assert Maybe(10, False).filter(lambda x: x != 10) == Maybe.nothing()

# Generated at 2022-06-14 03:35:02.564721
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    maybe = Maybe.just(1)
    assert maybe == Maybe.just(1)
    assert maybe != Maybe.nothing()


# Generated at 2022-06-14 03:35:10.345235
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Maybe.just(True).to_lazy() == Lazy(lambda: True)
    assert Maybe.just(False).to_lazy() == Lazy(lambda: False)
    assert Maybe.just('string').to_lazy() == Lazy(lambda: 'string')
    assert Maybe.just(UUID('e668e799-c2f1-4023-b9d9-973a9de7bf82')).to_lazy() == Lazy(lambda: UUID('e668e799-c2f1-4023-b9d9-973a9de7bf82'))
    assert Maybe.just(42).to_lazy() == Lazy(lambda: 42)
    assert Maybe.just(42.0).to_lazy() == Lazy

# Generated at 2022-06-14 03:35:15.727311
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe(1, False) == Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe(1, False) != Maybe(2, False)
    assert Maybe(1, False) != Maybe.nothing()
    assert Maybe(1, False) != 1


# Generated at 2022-06-14 03:35:22.095134
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    """
    Unit test for Maybe.__eq__().

    :return: None
    :rtype: None
    """
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(5) == Maybe.just(5)
    assert Maybe.just(5) != Maybe.nothing()
    assert Maybe.just(5) != Maybe.just(10)
    assert Maybe.nothing() != Maybe.just(10)


# Generated at 2022-06-14 03:35:27.477021
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    maybe1 = Maybe(1, True)
    maybe2 = Maybe(2, True)
    maybe3 = Maybe.nothing()
    maybe4 = Maybe(1, False)

    assert maybe1 == maybe2
    assert maybe3 == Maybe.nothing()
    assert Maybe.just(1) == maybe4
    assert Maybe.just(2) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(2)


# Generated at 2022-06-14 03:35:30.881664
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(2) == Maybe.just(2)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)


# Generated at 2022-06-14 03:35:44.037928
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(10) == Maybe.just(10)
    assert Maybe.just(10) != Maybe.just(3)
    assert Maybe.just(10) == Maybe.just(10)
    assert Maybe.just(10) != Maybe.just(3)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(3)
    assert Maybe.just(10) == Maybe.just(10)
    assert Maybe.just(10) != Maybe.just(3)


# Generated at 2022-06-14 03:35:51.381382
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe(1, False) == Maybe(1, False), "__eq__ for equal Maybes does not work"
    assert Maybe(None, True) == Maybe(None, True), "__eq__ for equal Maybes does not work"
    assert Maybe(1, False) != Maybe(2, False), "__eq__ for non-equal Maybes does not work"
    assert Maybe(1, False) != Maybe(None, True), "__eq__ for non-equal Maybes does not work"
    assert Maybe(1, False) != None, "__eq__ for non-equal Maybes does not work"
    assert Maybe(1, True) != None, "__eq__ for non-equal Maybes does not work"
    assert Maybe(None, True) != None, "__eq__ for non-equal Maybes does not work"



# Generated at 2022-06-14 03:35:57.649063
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    x = Maybe(1, False)
    y = Maybe(2, False)
    z = Maybe(1, False)
    w = Maybe(2, False)
    assert x == z
    assert x != y
    assert y == w
    assert x != (1, 2)
    assert not x.__eq__(None)


# Generated at 2022-06-14 03:36:06.776265
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(42) == Maybe.just(42)
    assert Maybe.just(42.0) == Maybe.just(42.0)
    assert Maybe.just('42') == Maybe.just('42')
    assert Maybe.just(42) == 42
    assert Maybe.just(42.0) == 42.0
    assert Maybe.just('42') == '42'
    assert Maybe.just(42) != 24
    assert Maybe.just(42.0) != 24.0
    assert Maybe.just('42') != '24'
    assert Maybe.just(42) != Maybe.just(24)
    assert Maybe.just(42.0) != Maybe.just(24.0)
    assert Maybe.just('42') != Maybe.just('24')
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just

# Generated at 2022-06-14 03:36:10.223848
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    x = Maybe.just(True)
    y = Maybe.just(True)
    z = Maybe.just(False)
    assert x == y
    assert not x == z


# Generated at 2022-06-14 03:36:17.328958
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    from pymonet.monad_try import Try
    from pymonet.validation import Validation

    def filter_maybe_by_len(x: Maybe[str]) -> Maybe[int]:
        return x.filter(lambda x: len(x) > 4)

    assert Maybe.just("hamster").filter(lambda x: len(x) > 4) == \
        Maybe.just("hamster")

    assert Maybe.just("hamster").filter(lambda x: len(x) > 5) == \
        Maybe.nothing()

    assert Maybe.nothing().filter(lambda x: len(x) > 4) == \
        Maybe.nothing()

    assert filter_maybe_by_len(Maybe.just("hamster")) == \
        Maybe.just("hamster")

    assert filter_maybe_by_len(Maybe.just("dog"))

# Generated at 2022-06-14 03:36:24.964406
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():

    assert (Maybe(1, is_nothing=False) == Maybe("1", is_nothing=False)) is False
    assert (Maybe("1", is_nothing=False) == Maybe("1", is_nothing=False)) is True
    assert (Maybe("1", is_nothing=False) == Maybe("2", is_nothing=False)) is False
    assert (Maybe("1", is_nothing=False) == Maybe("1", is_nothing=True)) is False
    assert (Maybe("1", is_nothing=True) == Maybe("1", is_nothing=False)) is False
    assert (Maybe("1", is_nothing=True) == Maybe("1", is_nothing=True)) is False


# Generated at 2022-06-14 03:36:33.224814
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(10).filter(lambda x: x > 5) == Maybe.just(10)
    assert Maybe.just(4).filter(lambda x: x > 5) == Maybe.nothing()
    assert Maybe.just(16).filter(lambda x: x > 5) == Maybe.just(16)
    assert Maybe.just(27).filter(lambda x: x > 5) == Maybe.just(27)
    assert Maybe.nothing().filter(lambda x: x > 0) == Maybe.nothing()



# Generated at 2022-06-14 03:36:38.327751
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)  # type: ignore
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.just(1) != Maybe.just(2)  # type: ignore
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)  # type: ignore


# Generated at 2022-06-14 03:36:41.545089
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Lazy(lambda: 1).equals(Maybe.just(1).to_lazy())
    assert Lazy(lambda: None).equals(Maybe.nothing().to_lazy())



# Generated at 2022-06-14 03:36:51.244612
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(2).filter(lambda i: i % 2 == 0) == Maybe.just(2)
    assert Maybe.just(3).filter(lambda i: i % 2 == 0) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda i: i % 2 == 0) == Maybe.nothing()



# Generated at 2022-06-14 03:36:57.973432
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    def filterer(value):
        return value % 2 == 0

    result = Maybe.just(10).filter(filterer)
    Maybe.just(10).filter(filterer).get_or_else(0) == 10
    Maybe.just(9).filter(filterer).get_or_else(0) == 0

    assert isinstance(result, Maybe[int])
    assert result.get_or_else(0) == 10

    result = Maybe.nothing().filter(filterer)
    assert isinstance(result, Maybe[None])
    assert result.get_or_else(0) == 0

# Generated at 2022-06-14 03:37:02.077483
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Maybe(1, False).to_lazy() == Lazy(lambda: 1)
    assert Maybe(None, True).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:37:05.776258
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    maybe = Maybe.just(1)

    assert maybe.to_lazy() == Lazy(lambda: 1)

    maybe = Maybe.nothing()

    assert maybe.to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:37:10.090830
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert(Lazy(lambda: 5) == Maybe.just(5).to_lazy())
    assert(Lazy(lambda: None) == Maybe.nothing().to_lazy())


# Generated at 2022-06-14 03:37:12.036022
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    test_value = 1
    maybe = Maybe.just(test_value)
    lazy = maybe.to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.eval() == test_value



# Generated at 2022-06-14 03:37:15.832212
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe(10, False).filter(lambda x: x % 2 == 0) == Maybe.just(10)
    assert Maybe(10, True).filter(lambda x: x % 2 == 0) == Maybe.nothing()



# Generated at 2022-06-14 03:37:20.982147
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    def action():
        print("Action!")
        return "Hello!"
    maybe = Maybe.just("Hello!")
    assert maybe.to_lazy().force() == "Hello!"
    assert maybe.to_lazy().bind(lambda x: Lazy(action)).force() == "Action!"

# Generated at 2022-06-14 03:37:26.704303
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe(True, False).filter(lambda x: x).value == True
    assert Maybe(None, True).filter(lambda x: x).is_nothing == True
    assert Maybe(2, False).filter(lambda x: x % 2 == 0).value == 2
    assert Maybe(2, False).filter(lambda x: x % 2 == 1).is_nothing == True

# Generated at 2022-06-14 03:37:28.850857
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: x < 2) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda x: x > 2) == Maybe.nothing()



# Generated at 2022-06-14 03:37:35.609065
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe(1, is_nothing=False).to_lazy() == Lazy(lambda: 1)
    assert Maybe(None, is_nothing=True).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:37:39.937042
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)
    assert Maybe.just(10).to_lazy() == Lazy(lambda: 10)

# Generated at 2022-06-14 03:37:43.335926
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.option import Option
    from operator import add

    assert isinstance(
        Option(1).to_lazy(),
        Lazy
    )

# Generated at 2022-06-14 03:37:45.877650
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)
    assert Maybe.just(5).to_lazy() == Lazy(lambda: 5)


# Generated at 2022-06-14 03:37:49.103076
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Maybe.just(4).to_lazy() == Lazy(lambda: 4)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 03:37:52.059576
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    maybe_1 = Maybe.just(3)
    maybe_2 = Maybe.nothing()
    lazy_1 = maybe_1.to_lazy()
    lazy_2 = maybe_2.to_lazy()

    assert lazy_1.value() == 3
    assert lazy_2.value() is None

# Generated at 2022-06-14 03:37:56.276731
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Maybe.just(1).to_lazy() == Lazy(lambda: 1)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:38:00.673508
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe.just(
        5
    ).to_lazy() == Lazy(lambda: 5)
    assert Maybe.nothing(
    ).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:38:05.743189
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    a = Maybe.just(123)
    b = Maybe.nothing()
    assert a.to_lazy() == Lazy(lambda: 123)
    assert b.to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 03:38:12.166978
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe
    from pymonet.either import Right

    def add(x, y):
        return x + y

    function = lambda: add(1, 2)

    maybe = Maybe.just(function)

    expected = Lazy(function)
    actual = maybe.to_lazy()

    assert expected == actual

# Generated at 2022-06-14 03:38:18.827333
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    m = Maybe.just(123)
    assert m.to_lazy().value() == Lazy(lambda: 123).value()



# Generated at 2022-06-14 03:38:21.074449
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    expected = Lazy(lambda: 5)
    assert Maybe.just(5).to_lazy() == expected


# Generated at 2022-06-14 03:38:26.263359
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 6) == Lazy.force(Maybe.just(3).map(lambda x: x * 2).to_lazy())
    assert Lazy(lambda: None) == Lazy.force(Maybe.nothing().map(lambda x: x * 2).to_lazy())
    assert Lazy(lambda: 6) == Lazy.force(Maybe.just(3).map(lambda x: x * 2).to_lazy())


# Generated at 2022-06-14 03:38:32.254864
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    def add_ten_maybe(x: int) -> Maybe[int]:
        if x < 0:
            return Maybe.nothing()
        return Maybe.just(x + 10)

    res = add_ten_maybe(5).to_lazy()
    assert res.value() == 15

    res = add_ten_maybe(-5).to_lazy()
    assert res.value() is None

# Generated at 2022-06-14 03:38:42.818473
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy, LazyResult

    val = Maybe.just(1)
    assert isinstance(val.to_lazy(), Lazy)
    assert isinstance(val.to_lazy()[0], LazyResult)
    assert val.to_lazy()[0] == LazyResult(1)

    val_nothing = Maybe.nothing()
    assert isinstance(val_nothing.to_lazy(), Lazy)
    assert isinstance(val_nothing.to_lazy()[0], LazyResult)
    assert val_nothing.to_lazy()[0] == LazyResult(None)

    val_nothing = Maybe.nothing()
    assert isinstance(val_nothing.to_lazy(), Lazy)

# Generated at 2022-06-14 03:38:50.546265
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.box import Box
    from pymonet.maybe import Maybe

    assert Maybe.just('a').to_lazy() == Lazy(lambda: 'a')
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)

    assert Maybe.just(Box(3)).to_lazy().flat_map(lambda x: Lazy(lambda: x.value + 1)) == Lazy(lambda: 4)
    assert Maybe.nothing().to_lazy().flat_map(lambda x: Lazy(lambda: x.value + 1)) == Lazy(lambda: None)


# Generated at 2022-06-14 03:38:57.396866
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_list import List

    # Test for mapper
    assert Maybe.just([1, 2, 3, 4]).to_lazy() == Lazy(lambda: [1, 2, 3, 4])
    assert Maybe.just(List.just(1)).to_lazy() == Lazy(lambda: List.just(1))



# Generated at 2022-06-14 03:38:59.378545
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe.just(1).to_lazy() == Lazy(lambda: 1)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:39:06.098599
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.monad_try import Failure
    from pymonet.lazy import Lazy
    from pymonet.either import Right
    from pymonet.box import Box

    # Test transformation of empty Maybe to Lazy
    result = Maybe.nothing().to_lazy()
    assert isinstance(result, Lazy)
    assert result.value() is None

    # Test transformation of not empty Maybe to Lazy
    result = Maybe.just(1).to_lazy()
    assert isinstance(result, Lazy)
    assert result.value() == 1



# Generated at 2022-06-14 03:39:08.980811
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe.nothing().to_lazy().value() is None
    assert Maybe.just(1).to_lazy().value() == 1

# Generated at 2022-06-14 03:39:22.101126
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    x = Maybe.just(1)
    res = x.to_lazy()
    assert res.value() == 1
    assert res.is_failed == False
    assert res.is_success == True

    y = Maybe.nothing()
    res = y.to_lazy()
    assert res.is_failed == False
    assert res.is_success == True
    assert res.value() is None



# Generated at 2022-06-14 03:39:28.463912
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    expected_lazy = Lazy(lambda: "value")
    actual_lazy = Maybe.just("value").to_lazy()
    assert actual_lazy == expected_lazy

    expected_lazy = Lazy(lambda: None)
    actual_lazy = Maybe.nothing().to_lazy()
    assert actual_lazy == expected_lazy



# Generated at 2022-06-14 03:39:33.662267
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    """
    Unit test for method to_lazy of class Maybe.

    :return: None
    :rtype: None
    """
    from pymonet.monad_try import Try

    def add1(x):
        return x + 1

    def to_str(x):
        return str(x)

    def add_to_str(x):
        return to_str(x) + '1'

    maybe = Maybe.just(1)

    assert maybe.to_lazy() == Lazy(lambda: 1)
    assert maybe.to_lazy().map(add1).map(add_to_str) == Lazy(lambda: '21')
    assert maybe.to_lazy().map(add1).map(to_str).map(lambda x: x + '1') == Lazy(lambda: '21')

# Generated at 2022-06-14 03:39:36.266795
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    mi = Maybe.just(1)
    m = mi.to_lazy()
    assert m.force() == 1



# Generated at 2022-06-14 03:39:40.682148
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.monad_try import Try

    assert Maybe.just(5).to_lazy() == Lazy(lambda: 5)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:39:43.627239
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet import Lazy
    f = lambda: 1
    assert (Maybe(1, False).to_lazy() == Lazy(f))



# Generated at 2022-06-14 03:39:46.418923
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe(2, False).to_lazy() == Lazy(lambda: 2)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:39:49.401008
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Maybe.just(12).to_lazy() == Lazy(lambda: 12)

    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)

# Generated at 2022-06-14 03:39:53.076786
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    maybe = Maybe(1, False)
    lazy = Lazy(lambda: 1)
    assert maybe.to_lazy() == lazy


# Generated at 2022-06-14 03:39:55.606279
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe.just(5).to_lazy() == Lazy(lambda: 5)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:40:11.640630
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    """
    Test case for method to_lazy of class Maybe.
    """

    from pymonet.lazy import Lazy

    assert Maybe.just(10).to_lazy() == Lazy(lambda: 10)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:40:15.625912
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.monad_try import Try

    assert Maybe.just(42).to_lazy().get() == 42
    assert Try(lambda: Maybe.nothing().to_lazy().get()).is_failure()

# Generated at 2022-06-14 03:40:17.453516
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe(32, False).to_lazy()._function.__name__ == '<lambda>'



# Generated at 2022-06-14 03:40:28.375617
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.maybe import Maybe
    from pymonet.lazy import Lazy

    # Lambda function returns value
    def func(value):
        return value

    assert Maybe.just(10).to_lazy() == Lazy(lambda: 10)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)

    # lambda in monad
    assert Maybe.just(lambda: 10).to_lazy() == Lazy(lambda: lambda: 10)
    assert Maybe.just(lambda: None).to_lazy() == Lazy(lambda: lambda: None)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)

    # Function
    assert Maybe.just(func).to_lazy() == Lazy(lambda: func)
    assert Maybe.just(func(10)).to

# Generated at 2022-06-14 03:40:29.146827
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    value = Maybe.just(42).to_lazy()
    assert value.value() == 42



# Generated at 2022-06-14 03:40:33.491344
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    print(Maybe.just(1).to_lazy())
    assert Maybe.just(1).to_lazy() == Lazy(lambda: 1)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:40:37.754581
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    maybe = Maybe.just(123).to_lazy()
    assert maybe.value() == 123

    maybe = Maybe.nothing().to_lazy()
    assert maybe.value() == None


# Generated at 2022-06-14 03:40:43.406281
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation, SuccessValidation

    assert Maybe.just(5).to_lazy() == Lazy(lambda: 5)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 03:40:47.901936
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.monad import unit
    from pymonet.lazy import Lazy

    value = 1
    maybe = Maybe.just(value)
    assert(maybe.to_lazy() == Lazy(lambda: value))


# Generated at 2022-06-14 03:40:51.752771
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Maybe(10, False).to_lazy() == Lazy(lambda: 10)
    assert Maybe(10, True).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:41:04.820071
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    def test_func():
        return 'value'

    Maybe.just('value').to_lazy() == Lazy(test_func)



# Generated at 2022-06-14 03:41:07.436850
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    f = lambda: 10
    result = Maybe.just(10).to_lazy()
    assert isinstance(result, Lazy)
    assert result.value() == f()
    assert result.is_equals(Lazy(f))



# Generated at 2022-06-14 03:41:16.414232
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.box import Box

    def test0():
        m = Box(Maybe.just(5))
        assert m.to_lazy() == Lazy(lambda: Maybe.just(5))

    def test1():
        m = Box(Maybe.nothing())
        assert m.to_lazy() == Lazy(lambda: Maybe.nothing())

    test0()
    test1()



# Generated at 2022-06-14 03:41:22.429283
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    lazy_none = Maybe.just(1).to_lazy()
    assert lazy_none == Lazy(lambda: 1)

    lazy_1 = Maybe.nothing().to_lazy()
    assert lazy_1 == Lazy(lambda: None)



# Generated at 2022-06-14 03:41:27.813176
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    maybe_1 = Maybe.just(1)
    maybe_2 = Maybe.nothing()

    assert maybe_1.to_lazy() == Lazy(lambda: 1)
    assert maybe_2.to_lazy() == Lazy(lambda: None)

