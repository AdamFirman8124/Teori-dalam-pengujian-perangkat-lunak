

# Generated at 2022-06-14 03:16:53.224337
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Right(1) == Right(1)
    assert Left(2) != Right(2)
    assert Left(3) != Left(4)
    assert Left(3) == Left(3)
    assert Left(3) != Right(3)
    assert Right(3) != Left(3)



# Generated at 2022-06-14 03:17:00.204105
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    left_either = Left(5)
    left_either2 = Left(3)
    right_either = Right(5)
    right_either2 = Right(3)

    assert left_either == left_either
    assert right_either == right_either
    assert left_either == left_either2
    assert right_either == right_either2

    assert left_either != right_either
    assert right_either != left_either2
    assert left_either != right_either2
    assert right_either != left_either



# Generated at 2022-06-14 03:17:02.810058
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Right(1) == Right(1)
    assert Left(1) == Left(1)
    assert Right(1) != Left(1)


# Generated at 2022-06-14 03:17:06.847626
# Unit test for method case of class Either
def test_Either_case():
    """
    >>> either = Left("test")
    >>> either.case(error=lambda x: x, success=lambda x: 2*x)
    'test'
    >>> another_either = Right(4)
    >>> another_either.case(error=lambda x: x, success=lambda x: 2*x)
    8
    """
    pass



# Generated at 2022-06-14 03:17:14.729733
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)
    assert not Left(1) == Right(1)
    assert not Right(1) == Left(1)


# Generated at 2022-06-14 03:17:20.198622
# Unit test for method case of class Either
def test_Either_case():
    def success(x):
        return x ** 2

    def error(x):
        return x ** 3

    assert Right(3).case(error, success) == 9
    assert Left(3).case(error, success) == 27



# Generated at 2022-06-14 03:17:23.332191
# Unit test for method case of class Either
def test_Either_case():
    assert Either(2).case(lambda x: x * 2, lambda x: x * 3) == 6
    assert Either('error').case(lambda x: x * 2, lambda x: x * 3) == 'errorerror'


# Generated at 2022-06-14 03:17:34.096343
# Unit test for method case of class Either
def test_Either_case():
    """
    Test method case of class Either

    Test case is based on this example:
        http://hackage.haskell.org/package/base-4.11.1.0/docs/Data-Either.html#t:Either
    """

    def test_map_error(value):
        return str(value) + ' is not a number'

    def test_map_success(value):
        return value + 1

    assert Right(10).case(test_map_error, test_map_success) == 11
    assert Left('foo').case(test_map_error, test_map_success) == 'foo is not a number'



# Generated at 2022-06-14 03:17:36.622900
# Unit test for method case of class Either
def test_Either_case():
    assert Left(5).case(lambda v: v + 2, lambda v: v * 2) == 7
    assert Right(5).case(lambda v: v + 2, lambda v: v * 2) == 10


# Generated at 2022-06-14 03:17:41.480546
# Unit test for method case of class Either
def test_Either_case():
    assert Left("bla bla").case(lambda x: "Not Right", lambda x: "Right") == "Not Right"
    assert Right("try").case(lambda x: "Not Right", lambda x: "Right") == "Right"



# Generated at 2022-06-14 03:17:49.812683
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    test_val = 'test'
    assert Lazy(lambda: test_val) == Lazy(test_val)
    assert Lazy(test_val) == Lazy(test_val)
    assert Lazy(0) == Lazy(0)
    assert Lazy(1) == Lazy(1)
    assert Lazy(True) == Lazy(True)
    assert Lazy(None) == Lazy(None)


# Generated at 2022-06-14 03:17:53.034637
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Right(1).to_lazy() == Lazy(lambda: 1)
    assert Left(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:17:58.061301
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Right(1).to_lazy() == Lazy(lambda: 1)
    assert Left(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:18:01.752825
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    right = Right(42)
    left = Left(42)
    assert right.to_lazy().get() == left.to_lazy().get() == 42


# Generated at 2022-06-14 03:18:05.379140
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(1).to_lazy() == Lazy(lambda: 1)
    assert Left(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:18:08.282642
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    # Given
    right = Right('value')

    # When
    result = right.to_lazy()

    # Then
    assert result.value() == right.value



# Generated at 2022-06-14 03:18:12.386833
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert(Left(1).to_lazy() == Lazy(lambda: 1))
    assert(Right(2).to_lazy() == Lazy(lambda: 2))


# Generated at 2022-06-14 03:18:16.697143
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1) == Either(1).to_lazy()
    assert Lazy(lambda: 1) == Left(1).to_lazy()
    assert Lazy(lambda: 1) == Right(1).to_lazy()


# Generated at 2022-06-14 03:18:24.329608
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.box import Box
    from pymonet.lazy import Lazy

    # Given
    lazy_either_left = Left(Box(1)).to_lazy()
    lazy_either_right = Right(Box(2)).to_lazy()

    # Then
    assert lazy_either_left == Lazy(lambda: Box(1)), "Should return lazy Copy intance of Left with new value"
    assert lazy_either_right == Lazy(lambda: Box(2)), "Should return lazy Copy intance of Right with new value"



# Generated at 2022-06-14 03:18:28.770515
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    assert Lazy(lambda: 'value') == Either.to_lazy(Right('value'))
    assert Lazy(lambda: 'error') == Either.to_lazy(Left('error'))


# Generated at 2022-06-14 03:18:46.709458
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.box import Box
    from pymonet.maybe import Maybe
    from pymonet.monad_try import Try
    from pymonet.validation import Validation

    assert Right(5).to_lazy() == Lazy(lambda: 5)
    assert Left(5).to_lazy() == Lazy(lambda: 5)


# Generated at 2022-06-14 03:18:48.771356
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.box import Box
    assert isinstance(Right(Box(6)).to_lazy(), Lazy)



# Generated at 2022-06-14 03:18:59.491814
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    def square(x):
        return lambda: x * x

    assert Left("Error").to_lazy() == Lazy(square("Error"))
    assert Right("Success").to_lazy() == Lazy(square("Success"))



# Generated at 2022-06-14 03:19:04.777148
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Either(1).to_lazy() == Lazy(lambda: 1)
    assert Either(-1).to_lazy() == Lazy(lambda: -1)
    assert Either(None).to_lazy() == Lazy(lambda: None)
    assert Either('spam').to_lazy() == Lazy(lambda: 'spam')


# Generated at 2022-06-14 03:19:05.665993
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Either(6).to_lazy() == Lazy(lambda: 6)


# Generated at 2022-06-14 03:19:09.262364
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """Unit test for method to_lazy of class Either"""

    assert Left(2).to_lazy() == Lazy(lambda: 2)
    assert Right(2).to_lazy() == Lazy(lambda: 2)


# Generated at 2022-06-14 03:19:12.099639
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(5).to_lazy().value() == 5
    assert Left("Something wrong").to_lazy().value() == "Something wrong"


# Generated at 2022-06-14 03:19:15.824688
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    def f():
        return 'test'
    lazy = Lazy(f)
    right = Right(lazy)

    assert right.to_lazy() == lazy



# Generated at 2022-06-14 03:19:18.861766
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    right = Right(2)
    left = Left(2)
    lazy1 = right.to_lazy()
    assert lazy1.eval_() == 2
    lazy2 = left.to_lazy()
    assert lazy2.eval_() == 2



# Generated at 2022-06-14 03:19:21.711934
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    def helper():
        return 'result'

    monad = Right('result')

    result = monad.to_lazy()

    assert isinstance(result, Lazy)
    assert result() == helper()



# Generated at 2022-06-14 03:19:31.187337
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert isinstance(Left(9).to_lazy(), Lazy)
    assert isinstance(Right(9).to_lazy(), Lazy)
    assert Lazy._is_lazy(Left(9).to_lazy())
    assert Lazy._is_lazy(Right(9).to_lazy())
    assert Left(9).to_lazy().evaluate() == 9
    assert Right(9).to_lazy().evaluate() == 9


# Generated at 2022-06-14 03:19:34.096297
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:19:42.915623
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Unit test for method to_lazy of class Either.
    """

    from pymonet.lazy import Lazy

    left = Left(ValueError())
    lazy = left.to_lazy()
    assert isinstance(lazy, Lazy) and isinstance(lazy.value(), ValueError)

    right = Right(1)
    lazy = right.to_lazy()
    assert isinstance(lazy, Lazy) and lazy.value() == 1



# Generated at 2022-06-14 03:19:46.805755
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Right(1).to_lazy() == Lazy(lambda: 1)
    assert Left(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:19:52.771471
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert isinstance(Right(1).to_lazy(), Lazy)
    assert Right(1).to_lazy().value() == 1
    assert Right(1).to_lazy().value() == 1
    assert isinstance(Left(1).to_lazy(), Lazy)
    assert Left(1).to_lazy().value() == 1
    assert Left(1).to_lazy().value() == 1


# Generated at 2022-06-14 03:19:55.164005
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(2).to_lazy().get() == 2
    

# Generated at 2022-06-14 03:20:03.064444
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.box import Box
    from pymonet.lazy import Lazy

    assert Left('error').to_lazy() == Lazy(lambda: 'error')
    assert Left('error').to_lazy().force() == 'error'

    assert Right(3).to_lazy() == Lazy(lambda: 3)
    assert Right(3).to_lazy().force() == 3


# Generated at 2022-06-14 03:20:04.996278
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(1).to_lazy() == Lazy(lambda: 1)
    assert Left("left").to_lazy() == Lazy(lambda: "left")



# Generated at 2022-06-14 03:20:08.342575
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    def to_lazy(x):
        return x.to_lazy()

    assert to_lazy(Right(1)) == Lazy(lambda: 1)
    assert to_lazy(Left(2)) == Lazy(lambda: 2)


# Generated at 2022-06-14 03:20:13.596703
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(None).to_lazy().__str__() == 'Lazy(None)'
    assert Right(1).to_lazy().__str__() == 'Lazy(1)'



# Generated at 2022-06-14 03:20:30.731775
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:20:36.603218
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    lazy_left = Left('value').to_lazy()
    lazy_right = Right('value').to_lazy()

    assert lazy_left.value() == 'value'
    assert lazy_right.value() == 'value'

# Generated at 2022-06-14 03:20:40.845083
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    def multiply(x, y):
        return x * y

    left_either = Left(4)
    assert left_either.to_lazy() == Lazy(lambda: 4)
    assert left_either.to_lazy().to_box().bind(multiply, 5).to_box().value == 20

    right_either = Right(4)
    assert right_either.to_lazy() == Lazy(lambda: 4)
    assert right_either.to_lazy().to_box().bind(multiply, 5).to_box().value == 20

# Generated at 2022-06-14 03:20:42.890330
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    # Given
    from pymonet.lazy import Lazy

    def fn():
        return 10

    lazy_expected = Lazy(fn)
    either = Right(10)

    # When
    lazy = either.to_lazy()

    # Then
    assert lazy_expected == lazy


# Generated at 2022-06-14 03:20:51.515211
# Unit test for method to_lazy of class Either

# Generated at 2022-06-14 03:20:53.032996
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Lazy(lambda: 1) == Either(1).to_lazy()


# Generated at 2022-06-14 03:20:56.992526
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    This test checks if method to_lazy of class Either returns correct result.

    :returns: Nothing
    :rtype: None
    """
    from pymonet.lazy import Lazy

    assert Right(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:21:00.646882
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Either(3).to_lazy() == Lazy(lambda: 3)
    assert Either("hello").to_lazy() == Lazy(lambda: "hello")


# Generated at 2022-06-14 03:21:02.772396
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(1).to_lazy().value() == 1
    assert Right(1).to_lazy().value() == 1


# Generated at 2022-06-14 03:21:05.368951
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    value = 'value'
    # Either.to_lazy()
    assert Right(value).to_lazy().value() == value
    assert Left(value).to_lazy().value() == value


# Generated at 2022-06-14 03:21:17.102834
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Either.to_lazy(Right(2)) == Either.to_lazy(Right(2))


# Generated at 2022-06-14 03:21:18.471178
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(1).to_lazy().force() == 1
    assert Left(1).to_lazy().force() == 1


# Generated at 2022-06-14 03:21:23.126481
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    assert Lazy(lambda: 3) == Lazy(3)
    assert Lazy(lambda: 3) == Lazy(Right(3))
    assert Lazy(lambda: 3) == Lazy(Left(3))


# Generated at 2022-06-14 03:21:26.850288
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:21:33.340136
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    def check_case(case, expected):
        either = Either.case(case, Left, Right)
        assert either.to_lazy().value() == expected

    test_case = [
        (1, 1),
        ((1,), 1),
        ([1], 1),
        (iter([1]), 1),
        ("test", "test"),
        (None, None)
    ]
    for case, expected in test_case:
        yield check_case, case, expected


# Generated at 2022-06-14 03:21:36.059717
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    test_value = 5
    assert Either(test_value).to_lazy() == Lazy(lambda: test_value)


# Generated at 2022-06-14 03:21:45.608126
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left('test').to_lazy() == Lazy(lambda: 'test')
    assert Right('test').to_lazy() == Lazy(lambda: 'test')


# Generated at 2022-06-14 03:21:51.299404
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Right(1).to_lazy() == Lazy(lambda: 1)
    assert Left([1]).to_lazy() == Lazy(lambda: [1])


# Generated at 2022-06-14 03:21:57.093433
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe

    assert Lazy(lambda: 1) == Either(1).to_lazy()
    assert Lazy(lambda: Maybe.just(1)) == Either(Maybe.just(1)).to_lazy()
    assert Lazy(lambda: Maybe.nothing()) == Either(Maybe.nothing()).to_lazy()

# Generated at 2022-06-14 03:22:03.894695
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.box import Box

    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(1).to_lazy() == Lazy(lambda: 1)
    assert Left(Box(1)).to_lazy() == Lazy(lambda: Box(1))
    assert Right(Box(1)).to_lazy() == Lazy(lambda: Box(1))



# Generated at 2022-06-14 03:22:27.994656
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Either(1).to_lazy() == Lazy(lambda: 1)
    assert Either(1).to_lazy().force_get() == 1
    assert Either("error").to_lazy() == Lazy(lambda: "error")
    assert Either("error").to_lazy().force_get() == "error"



# Generated at 2022-06-14 03:22:31.893424
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Lazy(lambda: 1) == Either(1).to_lazy()
    assert Lazy(lambda: 2) == Either(2).to_lazy()


# Generated at 2022-06-14 03:22:35.557602
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Either.to_lazy() == 'Either.to_lazy() not implemented'
    assert Left(3).to_lazy().f() == 3
    assert Right(3).to_lazy().f() == 3


# Generated at 2022-06-14 03:22:37.164938
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from random import randint

    number = randint(0, 10)

    assert Right.unit(number).to_lazy() == Lazy(lambda: number)

# Generated at 2022-06-14 03:22:39.668189
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left(None).to_lazy() == (Lazy(lambda: None))
    assert Right(None).to_lazy() == (Lazy(lambda: None))


# Generated at 2022-06-14 03:22:45.959783
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.lazy import lazy

    @lazy
    def test_method():
        return 123

    assert Either(123).to_lazy() == Lazy(lambda: 123)
    assert Either('123').to_lazy() == Lazy(lambda: '123')
    assert Either(test_method).to_lazy() == Lazy(lambda: test_method)



# Generated at 2022-06-14 03:22:48.548017
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(1).to_lazy().value() == 1
    assert Left([]).to_lazy().value() == []


# Generated at 2022-06-14 03:22:51.918393
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Right(3).to_lazy() == Lazy(lambda: 3)
    assert Left(3).to_lazy() == Lazy(lambda: 3)


# Generated at 2022-06-14 03:22:54.567229
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(2).to_lazy() == Lazy.from_value(2)
    assert Left('a').to_lazy() == Lazy.from_value('a')


# Generated at 2022-06-14 03:23:03.673883
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    lazy_success = Right(5).to_lazy()
    assert lazy_success.value() == 5
    assert lazy_success.is_evaluated() == False

    lazy_failure = Left(5).to_lazy()
    assert lazy_failure.value() == 5
    assert lazy_failure.is_evaluated() == False


# Generated at 2022-06-14 03:23:52.267263
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    >>> Left(1).to_lazy()
    <pymonet.lazy.Lazy object at 0x7fc8842c36d8>

    >>> Right(1).to_lazy()
    <pymonet.lazy.Lazy object at 0x7fc8842c3588>
    """
    pass


# Generated at 2022-06-14 03:23:58.937464
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.either import Left
    from pymonet.either import Right

    assert Left("error").to_lazy() == Lazy(lambda: "error")
    assert Right("success").to_lazy() == Lazy(lambda: "success")


# Generated at 2022-06-14 03:24:02.167868
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Lazy(lambda: 1) == Either(Try(1, is_success=True)).to_lazy()


# Generated at 2022-06-14 03:24:05.159152
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    def increment(x):
        return x + 1

    assert Right(2).to_lazy() == Lazy(lambda: 2)
    assert Left(2).to_lazy() == Lazy(lambda: 2)


# Generated at 2022-06-14 03:24:06.833976
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(1).to_lazy().value() == 1
    assert Right(1).to_lazy().value() == 1


# Generated at 2022-06-14 03:24:17.707420
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.exceptions import LazyResolveError

    def identity(x):
        return x

    lazy: Lazy[Callable[[Any], Any]] = Either(identity).to_lazy()

    assert lazy is not None
    assert lazy.resolve == identity
    assert lazy.resolve(1) == 1
    assert lazy.resolve("hello") == "hello"
    assert isinstance(lazy.resolve(None), type(None))
    assert lazy.resolve([1, 2, 3]) == [1, 2, 3]
    assert lazy.resolve((1, 2, 3)) == (1, 2, 3)

# Generated at 2022-06-14 03:24:24.074861
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    def add_two_to_lazy_value(lazy: Lazy[int]) -> int:
        return Lazy(lambda: lazy.value() + 2).value()

    lazy_value = Lazy(lambda: 3)

    expected = Lazy(lambda: 5)

    assert add_two_to_lazy_value(lazy_value) == expected.value()

# Generated at 2022-06-14 03:24:26.969164
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """Unit test for to_lazy method of class Either."""
    assert some_lazy().unwrap() == 1
    assert another_lazy().unwrap() == "1"
    assert isinstance(some_lazy().unwrap(), int)
    assert isinstance(another_lazy().unwrap(), str)


# Generated at 2022-06-14 03:24:28.415407
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(1).to_lazy().call() == 1
    assert Right(1).to_lazy().call() == 1


# Generated at 2022-06-14 03:24:33.343360
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    def test_function(arg: int) -> str:
        return str(arg)

    class TestException(Exception):
        pass

    test_value = 0
    assert test_function(test_value) ==\
        Either.right(test_value).to_lazy().get()
    assert Either.left(TestException()).to_lazy().get() ==\
        Either.left(TestException()).to_lazy().get()

# Generated at 2022-06-14 03:25:29.964610
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Either(3).to_lazy().get() == 3
    assert Either('s').to_lazy().get() == 's'


# Generated at 2022-06-14 03:25:34.374443
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:25:41.844974
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe
    from pymonet.monad_try import Try
    from pymonet.box import Box

    lazy = Lazy(lambda: 2)
    try_ = Try(2)
    box = Box(2)
    maybe = Maybe.just(2)

    assert lazy == lazy.to_lazy()
    assert lazy == try_.to_lazy()
    assert lazy == box.to_lazy()
    assert lazy == maybe.to_lazy()

    assert Left(2).to_lazy() == Lazy(lambda: 2)
    assert Right(2).to_lazy() == Lazy(lambda: 2)



# Generated at 2022-06-14 03:25:45.904231
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Test for method to_lazy of class Either.
    """
    assert Right(1).to_lazy().get_value()(0) == 1
    assert Left(2).to_lazy().get_value()(0) == 2


# Generated at 2022-06-14 03:25:49.666491
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(100).to_lazy().get() == 100
    assert Left(100).to_lazy().get() == 100


# Generated at 2022-06-14 03:25:58.648946
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """Unit test for method to_lazy of class Either."""
    from pymonet.lazy import Lazy
    from pymonet.either import Left
    from pymonet.either import Right

    assert Left(None).to_lazy() == Lazy(lambda: None)
    assert Right(7).to_lazy() == Lazy(lambda: 7)

    assert Left(None).to_lazy() != Lazy(lambda: 7)
    assert Right(7).to_lazy() != Lazy(lambda: None)


# Generated at 2022-06-14 03:26:01.735266
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    lazy = Lazy(lambda: 10)
    assert Right(10).to_lazy() == lazy
    assert Left(10).to_lazy() == lazy


# Generated at 2022-06-14 03:26:03.466676
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Right(5).to_lazy() == Lazy(lambda : 5)


# Generated at 2022-06-14 03:26:05.034904
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    import pytest

    assert Right(1).to_lazy().value() == 1
    assert Left(2).to_lazy().value() == 2


# Generated at 2022-06-14 03:26:09.218380
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(2).to_lazy() == Lazy(lambda: 2)
    assert Left(3).to_lazy() == Lazy(lambda: 3)