

# Generated at 2022-06-14 03:16:50.718791
# Unit test for method case of class Either
def test_Either_case():
    from pymonet.maybe import Maybe
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try
    from pymonet.validation import Validation

    maybe_lazy = lambda x: Maybe.just(lambda y: Try.success(lambda z: Either.Right(z + y + 2)))
    maybe_lazy_err = lambda x: Maybe.just(lambda y: Try.success(lambda z: Either.Left(z + y + 2)))

    def test_case_string(x: str) -> str:
        return x


# Generated at 2022-06-14 03:16:53.832743
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Right(3) == Right(3)
    assert Left(3) == Left(3)
    assert Right(3) != Left(3)


# Generated at 2022-06-14 03:16:58.655406
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.functions import _compose
    from pymonet.box import Box

    assert _compose(Box.to_lazy, Right(1).to_box).value == 1
    assert _compose(Box.to_lazy, Left(1).to_box).value == 1


# Generated at 2022-06-14 03:17:02.688242
# Unit test for method case of class Either
def test_Either_case():
    """
    Testing case method of class Either.
    """
    def error_handler(value):
        return -value

    def success_handler(value):
        return value

    assert Left(1).case(error_handler, success_handler) == -1
    assert Right(1).case(error_handler, success_handler) == 1

# Generated at 2022-06-14 03:17:08.683315
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # Comparing two instances of the same class
    # with the same values
    assert Right(1) == Right(1)
    assert Left(1) == Left(1)

    # Comparing two instances of different subclasses
    # with the same values
    assert Right(1) != Left(1)

    # Comparing two instances of the same class
    # with different values
    assert Right(1) != Right(2)
    assert Left(1) != Left(2)

    # Comparing two instances of different subclasses
    # with different values
    assert Right(1) != Left(2)



# Generated at 2022-06-14 03:17:11.667779
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    left = Left(3)
    second_left = Left(3)
    right = Right(3)
    not_right = Right(2)

    assert left == second_left
    assert right == right
    assert right != not_right
    assert left != right



# Generated at 2022-06-14 03:17:30.147177
# Unit test for method case of class Either
def test_Either_case():
    def error(e):
        return "Left"

    def success(a):
        return "Right"

    assert Left(None).case(lambda e: e, lambda a: a) == None
    assert Right(None).case(lambda e: e, lambda a: a) == None
    assert Left(10).case(lambda e: e, lambda a: a) == 10
    assert Right(10).case(lambda e: e, lambda a: a) == 10

    assert Left(1).case(error, success) == "Left"
    assert Right(1).case(error, success) == "Right"

    assert Left(None).case(lambda e: e, success) == None
    assert Right(None).case(lambda e: e, success) == None
    assert Right(10).case(lambda e: e, success) == 10
   

# Generated at 2022-06-14 03:17:34.468223
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    left1 = Left(1)
    left2 = Left(1)
    right1 = Right(1)
    right2 = Right(1)
    assert left1 == left2
    assert right1 == right2
    assert left1 != right1


# Generated at 2022-06-14 03:17:42.218349
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    x = Left('x')
    y = Left('x')
    z = Left('z')
    
    a = Right('x')
    b = Right('x')
    c = Right('z')
    
    assert (x == x == True) and (a == a == True)
    assert (x == y == True) and (a == b == True)
    assert (x != z == True) and (a != c == True)

    assert (x != a == True) and (a != x == True)

# Generated at 2022-06-14 03:17:55.515244
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    left_class_instance = Left('foo')
    assert left_class_instance == left_class_instance
    assert left_class_instance == Left('foo')

    right_class_instance = Right('foo')
    assert right_class_instance == right_class_instance
    assert right_class_instance == Right('foo')

    assert left_class_instance != right_class_instance
    assert left_class_instance != Right('foo')
    assert right_class_instance != Left('foo')
    assert right_class_instance != Left('bar')
    assert right_class_instance != 'foo'
    assert right_class_instance != 42
    assert right_class_instance != []



# Generated at 2022-06-14 03:18:02.308441
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Right(1) == Right(2) == Right([1, 2, 3])
    assert Left(1) == Left(2) == Left([1, 2, 3])
    assert Right(1) != Left(1)


# Generated at 2022-06-14 03:18:06.017565
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Left(2) == Left(2)
    assert Right(2) == Right(2)

    assert Left(2) != Right(2)
    assert Right(2) != Left(2)



# Generated at 2022-06-14 03:18:08.674868
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Either(2).to_lazy() == Lazy(lambda: 2)



# Generated at 2022-06-14 03:18:13.188504
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)



# Generated at 2022-06-14 03:18:15.856381
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """Unit test for method to_lazy of class Either"""

    value = 5
    right = Right(value)
    assert right.to_lazy().value() == value

    error = 'error'
    left = Left(error)
    assert left.to_lazy().value() == error


# Generated at 2022-06-14 03:18:20.038669
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    from pymonet.box import Box

    left_either = Left(Box(2))
    second_left_either = Left(Box(2))
    assert left_either == second_left_either

    right_either = Right(Box(2))
    second_right_either = Right(Box(2))
    assert right_either == second_right_either
    assert left_either != right_either

    assert left_either != Box(2)

# Generated at 2022-06-14 03:18:24.618814
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Left(5) == Left(5)
    assert Right(5) == Right(5)
    assert Left(5) != Right(5)
    assert Right('5') == Right('5')
    assert Right(5) != Right('5')



# Generated at 2022-06-14 03:18:30.665384
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 2) == Either(2).to_lazy()
    assert Lazy(lambda: 2) == Right(2).to_lazy()
    assert Lazy(lambda: 2) == Left(2).to_lazy()
    assert Lazy(lambda: 2).value() == Right(2).to_lazy().value()
    assert None == Left(2).to_lazy().value()



# Generated at 2022-06-14 03:18:40.296613
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Left(1) == Left(1)
    assert Left(1) != Left(2)
    assert Left(1) != Right(1)
    assert Right(1) == Right(1)
    assert Right(1) != Right(2)
    assert Right(1) != Left(1)
    assert Left(1) != 1
    assert Left(1) != object()
    assert Left(1) != Either(1)
    assert Right(1) != 1
    assert Right(1) != object()
    assert Right(1) != Either(1)
    assert Either(1) != 1
    assert Either(1) != object()



# Generated at 2022-06-14 03:18:41.800293
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(1).to_lazy().force() == 1



# Generated at 2022-06-14 03:18:51.502973
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Left(1) == Left(1)
    assert Left(2) != Left(1)
    assert Right(1) == Right(1)
    assert Right(2) != Right(1)
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)


# Generated at 2022-06-14 03:18:56.183811
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    def function(x, y):
        return x + y

    result = Right(lambda x, y: x + y).to_lazy()
    assert isinstance(result, Lazy)
    assert isinstance(result.get(), Callable)
    assert result.get()(1, 2) == 3
    assert result.get()(*[1, 2]) == 3


# Generated at 2022-06-14 03:18:59.662980
# Unit test for method __eq__ of class Either
def test_Either___eq__():

    assert Right(2) == Right(2)
    assert not Right(2) == Left(2)
    assert not Right(2) == Right(5)

    assert Left(2) == Left(2)
    assert not Left(2) == Left(5)
    assert not Left(2) == Right(2)


# Generated at 2022-06-14 03:19:04.257928
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    left = Left(1)
    right = Right(1)
    left_copy = Left(1)

    assert left == right
    assert right == left
    assert left == left_copy
    assert left_copy == left

# Generated at 2022-06-14 03:19:07.242683
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert (Left(1).to_lazy()).evaluate() == Left(1)
    assert (Right(1).to_lazy()).evaluate() == Right(1)


# Generated at 2022-06-14 03:19:09.779732
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    either = Either(5)
    lazy = either.to_lazy()

    assert isinstance(lazy, Lazy)



# Generated at 2022-06-14 03:19:18.286789
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # GIVEN
    left_1 = Left("value")
    left_2 = Left("value")
    left_3 = Left("other value")
    right_1 = Right("value")
    right_2 = Right("value")
    right_3 = Right("other value")
    # THEN
    assert left_1 == left_2
    assert not left_1 == left_3
    assert not left_1 == right_1
    assert not left_1 == right_2
    assert not left_1 == right_3
    assert not left_3 == right_1
    assert not left_3 == right_2
    assert not left_3 == right_3


# Generated at 2022-06-14 03:19:21.981578
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Right(1) == Right(1)
    assert Left('a') == Left('a')
    assert Right(1) != Left('a')
    assert Right(1) != Right('a')
    assert Left('a') != Left(1)



# Generated at 2022-06-14 03:19:24.606641
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(2).to_lazy() == Lazy(lambda: 2)



# Generated at 2022-06-14 03:19:30.876999
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    from pymonet.box import Box

    assert(Left(1) == Left(1))
    assert(Right(2) == Right(2))
    assert(not (Left(1) == Right(1)))
    assert(not (Right(2) == Left(2)))
    assert(not (Left(1) == Box(1)))
    assert(not (Right(1) == Box(1)))



# Generated at 2022-06-14 03:19:39.443173
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Either.Left(5).to_lazy() == Lazy(lambda: 5)
    assert Either.Right(5).to_lazy() == Lazy(lambda: 5)


# Generated at 2022-06-14 03:19:42.678390
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():

    assert Left("Error").to_lazy() == Lazy(lambda: "Error")
    assert Right("Value").to_lazy() == Lazy(lambda: "Value")



# Generated at 2022-06-14 03:19:51.442686
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:20:00.623474
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.box import Box

    def func():
        return 'test'

    # to_lazy
    given = Right(func).to_lazy()
    expected = Lazy(func)
    assert given == expected

    given = Left(Box(func)).to_lazy()
    expected = Lazy(func)
    assert given == expected


# Generated at 2022-06-14 03:20:13.513920
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    # Given
    value = Right(10)

    # When
    result = value.to_lazy()

    # Then
    assert isinstance(result, Lazy)
    assert result.get() == 10



# Generated at 2022-06-14 03:20:22.863440
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Either.__init__ is not None

    # Unit test for method to_lazy of class Either
    def test_Either_to_lazy():
        from pymonet.lazy import Lazy

        assert Either.__init__ is not None

        left = Left(1)
        right = Right(1)

        assert isinstance(left.to_lazy(), Lazy)
        assert isinstance(right.to_lazy(), Lazy)

        assert right.to_lazy().get() == right.value
        assert left.to_lazy().get() == left.value

        assert right.to_lazy().value.get() == right.value
        assert left.to_lazy().value.get() == left.value



# Generated at 2022-06-14 03:20:25.715625
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    def value():
        return 2

    some_right = Right(value)
    assert some_right.to_lazy().value() == value()


# Generated at 2022-06-14 03:20:29.199121
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 'lazy') == Left('lazy').to_lazy()
    assert Lazy(lambda: 'lazy') == Right('lazy').to_lazy()



# Generated at 2022-06-14 03:20:33.604841
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    # GIVEN
    value = 1

    # WHEN
    actual = Right(value).to_lazy()

    # THEN
    expected = Lazy(value)
    assert actual == expected



# Generated at 2022-06-14 03:20:36.348987
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Either(5).to_lazy() == Lazy(lambda: 5)



# Generated at 2022-06-14 03:20:45.953753
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 7) == Right(7).to_lazy()
    assert Lazy(lambda: 7) == Left(7).to_lazy()


# Generated at 2022-06-14 03:20:51.823098
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    lazy_result = Right('result value').to_lazy()
    assert isinstance(lazy_result, Lazy)
    assert lazy_result.eval() == 'result value'

    lazy_result = Left('error value').to_lazy()
    assert lazy_result.eval() == 'error value'

# Generated at 2022-06-14 03:20:55.665357
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(2).to_lazy() == Lazy(lambda: 2)


# Generated at 2022-06-14 03:20:59.046356
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(2).to_lazy() == Lazy(lambda: 2)


# Generated at 2022-06-14 03:21:03.380958
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert isinstance(Right(2).to_lazy(), Lazy)
    assertRight(Right(2).to_lazy().evaluate(), 2)
    assert isinstance(Left(2).to_lazy(), Lazy)
    assertLeft(Left(2).to_lazy().evaluate(), 2)

# Generated at 2022-06-14 03:21:07.590213
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left("test").to_lazy() == Lazy(lambda: "test")
    assert Right("test").to_lazy() == Lazy(lambda: "test")


# Generated at 2022-06-14 03:21:10.675244
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    lazy = Right(0).to_lazy()

    assert lazy.evaluate() == 0
    assert Right(0).to_lazy().evaluate() == 0
    assert Left(0).to_lazy().evaluate() == 0



# Generated at 2022-06-14 03:21:14.645855
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe

    def make_lazy_with_to_lazy():
        return Maybe(2).to_lazy()

    assert Lazy(lambda: 2) == make_lazy_with_to_lazy()


# Generated at 2022-06-14 03:21:16.843011
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:21:20.187598
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Unit test for method to_lazy of class Either

    :returns: Nothing
    :rtype: None
    :raises: AssertionError if test failed
    """
    assert Right(1).to_lazy() == Lazy(lambda: 1)
    assert Left('err').to_lazy() == Lazy(lambda: 'err')



# Generated at 2022-06-14 03:21:35.870699
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Either(3).to_lazy() == Lazy(3)
    assert Either('foo').to_lazy() == Lazy('foo')
    assert Either([1, 2, 3]).to_lazy() == Lazy([1, 2, 3])


# Generated at 2022-06-14 03:21:40.344226
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """Unit test by example"""
    either_left = Left("data")
    assert(either_left.to_lazy().value() == "data")

    either_right = Right(123)
    assert(either_right.to_lazy().value() == 123)

# Generated at 2022-06-14 03:21:43.320484
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left('error').to_lazy() == Lazy(lambda : 'error')
    assert Right(5).to_lazy() == Lazy(lambda : 5)



# Generated at 2022-06-14 03:21:46.737318
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    # given
    either = Right(10)
    # when
    lazy = either.to_lazy()
    # then
    assert lazy.evaluate() == 10
    # when
    either2 = Left("Something goes wrong")
    # then
    assert either2.to_lazy().evaluate() == "Something goes wrong"


# Generated at 2022-06-14 03:21:52.352000
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    assert Left(0).to_lazy() == Lazy(lambda: 0)
    assert Right(0).to_lazy() == Lazy(lambda: 0)


# Generated at 2022-06-14 03:21:55.922102
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    expected = 5
    assert Lazy(lambda: 5) == Either.left(None).to_lazy() == Either.right(5).to_lazy()



# Generated at 2022-06-14 03:22:09.736982
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.box import Box
    from pymonet.lazy import Lazy

    assert Either(Box(1)).to_lazy() == Lazy(lambda: Box(1))
    assert Either(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:22:17.352281
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    # given
    from pymonet.lazy import Lazy
    from pymonet.box import Box
    from pymonet.maybe import Maybe

    left_lazy = Lazy(lambda: 1)
    right_lazy = Lazy(lambda: 2)

    left_maybe = Maybe.just(1)
    right_maybe = Maybe.nothing()

    # when
    left_box_lazy = left_lazy.to_lazy()
    right_box_lazy = right_lazy.to_lazy()

    left_box_maybe = left_maybe.to_lazy()
    right_box_maybe = right_maybe.to_lazy()

    # then
    assert left_box_lazy == Box(1)
    assert right_box_lazy == Box(2)
    assert left_box

# Generated at 2022-06-14 03:22:22.170385
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    assert Right(3).to_lazy() == Lazy(3)
    assert Left(3).to_lazy() == Lazy(3)


# Generated at 2022-06-14 03:22:31.562033
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    lazy_empty = Lazy(lambda: [])
    lazy_list = Lazy(lambda: [1, 2, 3])

    assert Right(lazy_list).to_lazy() == lazy_list
    assert Left(lazy_list).to_lazy() == lazy_list

    assert Right(lazy_empty).to_lazy() == lazy_empty
    assert Left(lazy_empty).to_lazy() == lazy_empty



# Generated at 2022-06-14 03:22:59.683967
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Lazy(lambda: 1).force() == Right(1).to_lazy().force()
    assert Lazy(lambda: 1).force() == Left(1).to_lazy().force()


# Generated at 2022-06-14 03:23:01.659180
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    assert isinstance(Left(1).to_lazy(), Lazy)
    assert isinstance(Right(1).to_lazy(), Lazy)


# Generated at 2022-06-14 03:23:08.110369
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Either(1).to_lazy() == Lazy(lambda: 1)
    assert Either(1).to_lazy().force() == 1
    assert Either(2).to_lazy().force() == 2
    assert Left(2).to_lazy().force() == 2
    assert Right(1).to_lazy().force() == 1


# Generated at 2022-06-14 03:23:09.207473
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    either = Either(Lazy(lambda: 100))

    assert either.to_lazy().get() == 100



# Generated at 2022-06-14 03:23:12.535751
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():

    import pymonet.lazy
    from pymonet.lazy import Lazy

    def f():
        return 5

    x = Right(f).to_lazy()
    assert isinstance(x, Lazy) and x.value() == 5



# Generated at 2022-06-14 03:23:20.515288
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    def test_Either_to_lazy():
        """Unit test for method to_lazy of class Either"""
        assert Left(3).to_lazy().evaluate() == 3
        assert Right(3).to_lazy().evaluate() == 3



# Generated at 2022-06-14 03:23:24.044133
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.monad_lazy import Lazy

    assert Lazy(lambda: 1) == Left(1).to_lazy()
    assert Lazy(lambda: 1) == Right(1).to_lazy()



# Generated at 2022-06-14 03:23:25.210817
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Either(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:23:27.455867
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.either import Left, Right

    # Test for Left Either
    assert Left(4).to_lazy() == Lazy(lambda: 4)

    # Test for Right Either
    assert Right(5).to_lazy() == Lazy(lambda: 5)



# Generated at 2022-06-14 03:23:32.020629
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Test monad Either with method to_lazy.

    >>> test_Either_to_lazy()
    True
    """
    from pymonet.lazy import Lazy

    return (Right(10).to_lazy() == Lazy(lambda: 10)) and\
        (Left(20).to_lazy() == Lazy(lambda: 20))

# Create unit test for method ap of class Either

# Generated at 2022-06-14 03:24:26.571115
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    def f():
        return 4

    assert Right(1).to_lazy() == Lazy(func=f)

# Generated at 2022-06-14 03:24:29.806079
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    def add(a, b):
        return a + b

    l = Lazy(add)(1, 2)
    e = Right(l)
    assert e.to_lazy() == l

# Generated at 2022-06-14 03:24:32.690535
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    lazy = Lazy(lambda: 11)
    result = Either.to_lazy(Right(10))
    assert result.value() == lazy.value()



# Generated at 2022-06-14 03:24:36.317086
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.box import Box

    left = Left(Box(3.14))
    assert left.to_lazy() == Lazy(left.value)

    right = Right(3.14)
    assert right.to_lazy() == Lazy(right.value)


# Generated at 2022-06-14 03:24:39.974457
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(10).to_lazy() == Lazy(lambda: 10)
    assert Left([10, 20]).to_lazy() == Lazy(lambda: [10, 20])



# Generated at 2022-06-14 03:24:45.667119
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Test is lazy monad.
    """
    from pymonet.lazy import Lazy

    # given
    right = Either.unit(lambda: 1)
    # then
    assert right is not None
    assert right.to_lazy() == Lazy(lambda: 1)

    # given
    left = Either.unit(lambda: None)
    # then
    assert left is not None
    assert left.to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:24:47.123556
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    e = Left("I'm error")
    assert e.to_lazy() == Lazy(lambda: e)

# Generated at 2022-06-14 03:24:49.909643
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(2).to_lazy() == Lazy(lambda: 2)
    assert Right(2).to_lazy() == Lazy(lambda: 2)


# Generated at 2022-06-14 03:24:51.957158
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(1).to_lazy().force() == Left(1).to_lazy().force() == 1

# Generated at 2022-06-14 03:24:56.613864
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    # Left
    either = Left(1)
    lazy = either.to_lazy()
    assert lazy.value() == 1
    assert lazy == Lazy(lambda: 1)

    # Right
    either = Right('hola')
    lazy = either.to_lazy()
    assert lazy.value() == 'hola'
    assert lazy == Lazy(lambda: 'hola')
