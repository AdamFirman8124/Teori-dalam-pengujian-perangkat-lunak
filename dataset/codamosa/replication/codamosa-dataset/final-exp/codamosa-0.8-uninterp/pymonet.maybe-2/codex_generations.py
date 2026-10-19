

# Generated at 2022-06-14 03:31:33.338449
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    """
    Method __eq__ of class Maybe should compare self and passed value.
    """
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(2) == Maybe.just(2)
    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:31:36.873516
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(5).filter(lambda x: x > 4) == Maybe.just(5)
    assert Maybe.just(5).filter(lambda x: x > 10) == Maybe.nothing()


# Generated at 2022-06-14 03:31:46.696307
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(None) == Maybe.just(None)
    assert Maybe.just('1') == Maybe.just('1')
    assert Maybe.just([1, 2, 3]) == Maybe.just([1, 2, 3])
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.just(None)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(None)



# Generated at 2022-06-14 03:31:52.153589
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(3).filter(lambda value: value % 2 == 1) == Maybe.just(3)
    assert Maybe.just(4).filter(lambda value: value % 2 == 1) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda value: value % 2 == 1) == Maybe.nothing()



# Generated at 2022-06-14 03:31:57.127632
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from basic_classes.lazy import Lazy

    maybe = Maybe.just(42)
    assert maybe.to_lazy() == Lazy(lambda: 42)
    maybe = Maybe.nothing()
    assert maybe.to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 03:32:01.163325
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()


# Generated at 2022-06-14 03:32:10.140440
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.just(1) != object



# Generated at 2022-06-14 03:32:15.014248
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(10).filter(lambda x: x > 5) == Maybe.just(10)
    assert Maybe.just(10).filter(lambda x: x > 15) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x > 15) == Maybe.nothing()



# Generated at 2022-06-14 03:32:19.003627
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    x1 = Maybe.just(1)
    y1 = Maybe.just(2)

    assert x1 != y1
    assert y1 != Maybe.nothing()
    assert y1 == Maybe.just(2)
    assert Maybe.just(None) == Maybe.just(None)
    assert Maybe.just(None) == Maybe.just(None)



# Generated at 2022-06-14 03:32:27.655553
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just("a") == Maybe.just("a")
    assert Maybe.just("a") != Maybe.just("b")
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just({1, 2}) == Maybe.just({1, 2})
    assert Maybe.just({1, 2}) != Maybe.just({1, 2, 3})


# Generated at 2022-06-14 03:32:39.059639
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just("hello") == Maybe.just("hello")
    assert Maybe.just("hello") == Maybe.just("hello")
    assert Maybe.nothing() == Maybe.nothing()
    assert not Maybe.just("hello") == Maybe.nothing()
    assert not Maybe.nothing() == Maybe.just("hello")
    assert not Maybe.just("hello") == Maybe.just("hello1")
    assert not Maybe.just("hello") == "hello"
    assert not Maybe.just("hello") == object()
    assert Maybe.just(None) == Maybe.just(None)



# Generated at 2022-06-14 03:32:42.519161
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Maybe.just(3).to_lazy() == Lazy(3)
    assert Maybe.nothing().to_lazy() == Lazy(None)


# Generated at 2022-06-14 03:32:50.363279
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    """
    Unit test for method filter of class Maybe.
    """
    from pymonet.box import Box

    assert Maybe.nothing().filter(lambda x: x == 1) == Maybe.nothing()
    assert Maybe.just(1).filter(lambda x: x == 1) == Maybe.just(1)
    assert Maybe.just(2).filter(lambda x: x == 1) == Maybe.nothing()
    assert Maybe.just(2).filter(lambda x: x == 2) == Maybe.just(2)

    assert Maybe.just(Box(1)).filter(lambda x: x.contains() == 1) == Maybe.just(Box(1))
    assert Maybe.just(Box(2)).filter(lambda x: x.contains() == 1) == Maybe.nothing()

# Generated at 2022-06-14 03:32:54.903791
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(5) == Maybe.just(5)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(5) != Maybe.just(6)
    assert Maybe.just(5) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(6)



# Generated at 2022-06-14 03:33:02.413937
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    def test_filterer(value):
        return value > 5

    maybe_int = Maybe.just(10)
    maybe_int_filtered = maybe_int.filter(test_filterer)
    assert maybe_int_filtered.get_or_else(None) == 10

    maybe_int = Maybe.just(3)
    maybe_int_filtered = maybe_int.filter(test_filterer)
    assert maybe_int_filtered.get_or_else(None) is None

    maybe_int = Maybe.nothing()
    maybe_int_filtered = maybe_int.filter(test_filterer)
    assert maybe_int_filtered.get_or_else(None) is None


# Generated at 2022-06-14 03:33:06.929847
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just('A') == Maybe.just('A')
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just('A') != Maybe.just('B')
    assert Maybe.just('A') != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just('A')



# Generated at 2022-06-14 03:33:09.431814
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe.just(5).to_lazy() == Lazy(lambda: 5)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:33:15.644884
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.just("Ham")
    assert Maybe.just("Spam") != Maybe.just("eggs")
    assert Maybe.nothing() != Maybe.just("Ham")
    assert Maybe.just("Spam") != Maybe.nothing()



# Generated at 2022-06-14 03:33:21.074245
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    def identity(value):
        return value

    assert Maybe(1, True) == Maybe.nothing()
    assert Maybe(1, False) == Maybe.just(1)
    assert Maybe.just(identity) == Maybe.just(identity)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.just(identity) != Maybe.nothing()


# Generated at 2022-06-14 03:33:25.633003
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    from pymonet.maybe import Maybe
    def is_even(value):
        return value % 2 == 0
    assert Maybe.just(2).filter(is_even) == Maybe.just(2)
    assert Maybe.just(1).filter(is_even) == Maybe.nothing()
    assert Maybe.nothing().filter(is_even) == Maybe.nothing()


# Generated at 2022-06-14 03:33:33.865613
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.nothing().__eq__(Maybe.nothing())
    assert Maybe.just(1).__eq__(Maybe.just(1))
    assert Maybe.just(1).__eq__(Maybe.just(2)) == False
    assert Maybe.nothing().__eq__(Maybe.just(1)) == False



# Generated at 2022-06-14 03:33:41.850104
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe(1, True) == Maybe(1, True)
    assert Maybe(1, False) == Maybe(1, False)
    assert Maybe(1, True) == Maybe(2, True)
    assert Maybe(1, False) == Maybe(2, False)
    assert Maybe(1, True) == Maybe(2, False)
    assert Maybe(1, False) == Maybe(2, True)
    assert Maybe(1, True) != Maybe(1, False)


# Generated at 2022-06-14 03:33:45.232273
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(2) == Maybe.just(2)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(2) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(2)


# Generated at 2022-06-14 03:33:51.494648
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    nothing = Maybe.nothing()
    just_3 = Maybe.just(3)
    just_3_copy = Maybe.just(3)
    just_5 = Maybe.just(5)
    assert nothing == Maybe.nothing()
    assert just_3 == Maybe.just(3)
    assert just_3 == just_3_copy
    assert not nothing == just_5
    assert not nothing == just_3
    assert not just_3 == just_5


# Generated at 2022-06-14 03:33:56.750520
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(2) == Maybe.just(2)
    assert Maybe.just(2) != Maybe.just(3)
    assert Maybe.just(3) == Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(None)



# Generated at 2022-06-14 03:34:01.121589
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)

    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) != Maybe.nothing()



# Generated at 2022-06-14 03:34:07.974779
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert not Maybe.just(1) == Maybe.just(2)
    assert Maybe.just(1) == Maybe.just(1)
    assert not Maybe.just(1) == Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()
    assert not Maybe.nothing() == Maybe.just(1)



# Generated at 2022-06-14 03:34:13.690535
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 'foo') == Maybe.just('foo').to_lazy()
    assert Lazy(lambda: None) == Maybe.nothing().to_lazy()


# Generated at 2022-06-14 03:34:18.346820
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    # returns nothing
    assert Maybe(3, False).filter(lambda x: x == 2) \
        == Maybe.nothing()

    # returns value
    assert Maybe(2, False).filter(lambda x: x == 2) \
        == Maybe(2, False)

    # returns default
    assert Maybe(None, True).filter(lambda x: x == 2) \
        == Maybe.nothing()


# Generated at 2022-06-14 03:34:26.266406
# Unit test for method filter of class Maybe
def test_Maybe_filter():

    constants = (
        (
            Maybe.just(1),
            Maybe.nothing(),
            Maybe.just(2)
        ),
        (
            Maybe.just(2),
            Maybe.nothing(),
            Maybe.just(1)
        ),
        (
            Maybe.just(0),
            Maybe.nothing(),
            Maybe.just(0)
        )
    )

    def filterer(x):
        return x > 0

    for args in constants:
        maybe = args[0].filter(filterer)

        assert maybe == args[1]

    for args in constants:
        maybe = args[0].filter(filterer, args[2])

        assert maybe == args[2]

# Generated at 2022-06-14 03:34:33.160243
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Maybe.just(2).to_lazy() == Lazy(lambda: 2)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:34:37.421983
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda v: v > 0) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda v: v < 0) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda v: v > 0) == Maybe.nothing()


# Generated at 2022-06-14 03:34:42.579810
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(2) == Maybe.just(2)
    assert not (Maybe.just(1) == Maybe.just(2))

    assert Maybe.nothing() == Maybe.nothing()
    assert not (Maybe.just(1) == Maybe.nothing())
    assert not (Maybe.nothing() == Maybe.just(1))


# Generated at 2022-06-14 03:34:54.099103
# Unit test for method filter of class Maybe
def test_Maybe_filter():

    def filterer(value):
        return value % 2 == 0

    def filterer1(value):
        return value % 2 == 0

    def filterer2(value):
        return value % 2 == 0

    assert Maybe(2, False).filter(filterer) == Maybe.just(2)
    assert Maybe(2, False).filter(filterer1).filter(filterer2) == Maybe.just(2)
    assert Maybe(3, False).filter(filterer) == Maybe.nothing()
    assert Maybe(None, True).filter(filterer) == Maybe.nothing()
    assert Maybe(2, False).filter(filterer).filter(None) == Maybe.nothing()
    assert Maybe(2, False).filter(None) == Maybe.nothing()


# Generated at 2022-06-14 03:34:59.912323
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    # Given
    maybe = Maybe.just(1)
    # When
    maybe2 = maybe.filter(lambda x: x == 1)
    maybe3 = maybe.filter(lambda x: x == 2)
    # Then
    assert maybe2.value == 1
    assert maybe3.is_nothing



# Generated at 2022-06-14 03:35:06.605182
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Maybe.just(1).to_lazy() == Lazy(lambda: 1)
    assert Maybe.just(1).to_lazy() != Lazy(lambda: 2)
    assert Maybe.just(1).to_lazy() != Maybe.just(1).to_lazy().map(lambda x: x + 1)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 03:35:11.809928
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    class SomeClass(object):
        def __init__(self, id):
            self.id = id

        def __eq__(self, other):
            return self.__dict__ == other.__dict__

    some_class = SomeClass(1)

    assert Maybe.just(some_class) == Maybe.just(some_class)
    assert NotImplemented == Maybe.just(some_class).__eq__(None)
    assert NotImplemented == Maybe.just(some_class).__eq__(1)
    assert NotImplemented == Maybe.just(some_class).__eq__([1, 2, 3])
    assert NotImplemented == Maybe.just(some_class).__eq__({1: 1, 2: 2})


# Generated at 2022-06-14 03:35:16.965312
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(5).filter(lambda x: x == 5) == Maybe.just(5)
    assert Maybe.just(5).filter(lambda x: x != 5) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x == 5) == Maybe.nothing()



# Generated at 2022-06-14 03:35:23.151811
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    some = Maybe.just(1)
    another_some = Maybe.just(1)
    nothing = Maybe.nothing()
    another_nothing = Maybe.nothing()

    assert some == another_some
    assert nothing == another_nothing
    assert some != nothing
    assert some != another_nothing
    assert nothing != some
    assert nothing != another_some



# Generated at 2022-06-14 03:35:27.163145
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(42) == Maybe.just(42)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(42) != Maybe.just(24)
    assert Maybe.just(42) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(42)


# Generated at 2022-06-14 03:35:31.147316
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(is_positive) == Maybe.just(1)
    assert Maybe.just(-1).filter(is_positive) == Maybe.nothing()



# Generated at 2022-06-14 03:35:34.987028
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    maybe = Maybe.just(1)
    maybe2 = Maybe.just(2)
    nothing = Maybe.nothing()

    assert maybe != maybe2
    assert maybe == Maybe.just(1)
    assert maybe.value != maybe2.value
    assert nothing == Maybe.nothing()


# Generated at 2022-06-14 03:35:44.979845
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    """
    Unit test for filter method of Maybe class.

    :returns: True when test is ok, other case return False
    :rtype: Boolean
    """
    m = Maybe.just(2)
    return m.filter(lambda v: v % 2 == 0) == Maybe.just(2) and \
           m.filter(lambda v: v % 2 == 1) == Maybe.nothing() and \
           Maybe.nothing().filter(lambda v: v % 2 == 1) == Maybe.nothing() and \
           Maybe.nothing().filter(lambda v: v % 2 == 0) == Maybe.nothing()


# Generated at 2022-06-14 03:35:49.931503
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe

    lazy_value = Maybe.just(10).to_lazy()

    assert isinstance(lazy_value, Lazy), 'lazy_value is not a Lazy object'

# Generated at 2022-06-14 03:35:55.084836
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    def test_func():
        return 42

    maybe = Maybe.just(test_func)
    lazy = maybe.to_lazy()
    assert lazy == Lazy(test_func)

# Generated at 2022-06-14 03:36:01.530734
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    from pymonet.number import Number
    from pymonet.box import Box

    def filterer(value):
        return value % 2 == 0

    assert Maybe.just(3).filter(filterer) is Maybe.nothing()
    assert Maybe.just(4).filter(filterer) == Maybe.just(4)
    assert Maybe.just(4.0).filter(filterer) == Maybe.just(4.0)
    assert Maybe.just(Number(4)).filter(filterer) == Maybe.just(Number(4))
    assert Maybe.just(Box(4)).filter(filterer) == Maybe.just(Box(4))



# Generated at 2022-06-14 03:36:09.641079
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(None) == Maybe.just(None)
    assert Maybe.just(None) != Maybe.just(1)
    assert Maybe.just(None) == Maybe.just(None)
    assert Maybe.just(None) != Maybe.just(1)
    assert Maybe.just(None) == Maybe.nothing()
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(None)
    assert Maybe.nothing() != Maybe.just(1)


# Generated at 2022-06-14 03:36:11.765998
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Lazy(lambda: 1) == Maybe.just(1).to_lazy()
    assert Lazy(lambda: None) == Maybe.nothing().to_lazy()



# Generated at 2022-06-14 03:36:13.501115
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: x < 2) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda x: x < 1) == Maybe.nothing()



# Generated at 2022-06-14 03:36:22.608722
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    print('Unit test for method __eq__ of class Maybe:')
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just('Hello') == Maybe.just('Hello')
    assert Maybe.just('Hello') != Maybe.just(1)
    assert Maybe.just(1) != Maybe.just('Hello')
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(123)
    assert Maybe.just(123) != Maybe.nothing()
    print('Unit test for method __eq__ of class Maybe - done.')
    print()


# Generated at 2022-06-14 03:36:30.405160
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.just(2) != Maybe.just(1)
    assert Maybe.just([1]) != Maybe.just([1])



# Generated at 2022-06-14 03:36:35.702210
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()

    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(2)
    assert Maybe.nothing() != None


# Generated at 2022-06-14 03:36:39.400085
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe(2, False) == Maybe(2, False)
    assert Maybe(2, True) == Maybe(2, True)
    assert Maybe(2, False) != Maybe(2, True)
    assert Maybe(2, True) != Maybe(2, False)



# Generated at 2022-06-14 03:36:43.433761
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe(10, False) == Maybe(10, False)
    assert Maybe(10, True) == Maybe(10, True)
    assert Maybe(10, True) != Maybe(10, False)


# Generated at 2022-06-14 03:36:48.603796
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():

    assert Maybe.just(2) == Maybe.just(2)
    assert Maybe.just(2) != Maybe.just(3)
    assert Maybe.just(2) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(2)


# Generated at 2022-06-14 03:36:52.106930
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe(5, True) == Maybe.nothing()
    assert Maybe.just(5) != Maybe.nothing()
    assert Maybe.just(5) == Maybe.just(5)


# Generated at 2022-06-14 03:36:56.565229
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()

    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.nothing() != Maybe.just(2)

    assert Maybe.just(1) != 1
    assert Maybe.nothing() != None
    assert Maybe.nothing() != object()



# Generated at 2022-06-14 03:37:01.927479
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.identity import Identity

    assert Maybe.just(10).to_lazy().map(lambda x: x + 10).value() == Lazy(Identity(20)).map(lambda x: x + 10).value()



# Generated at 2022-06-14 03:37:05.229174
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda v: v % 2 == 1) == Maybe.just(1)
    assert Maybe.just(2).filter(lambda v: v % 2 == 1) == Maybe.nothing()


# Generated at 2022-06-14 03:37:09.113679
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Maybe.just(10).to_lazy() == Lazy(lambda: 10)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:37:22.022396
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    """
    Test filter method of class Maybe.

    :returns: None
    :rtype: NoneType
    """
    assert Maybe.just(1).filter(lambda x: x == 1) == Maybe.just(1)
    assert Maybe.just(2).filter(lambda x: x == 1) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x == 1) == Maybe.nothing()



# Generated at 2022-06-14 03:37:26.266800
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1) == Maybe.just(1).to_lazy()
    assert Lazy(lambda: None) == Maybe.nothing().to_lazy()


# Generated at 2022-06-14 03:37:30.576206
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    """
    Checks Maybe.filter method behaviour.
    """
    assert Maybe.just(1).filter(lambda x: x == 1) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda x: x == 2) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x == 1) == Maybe.nothing()


# Generated at 2022-06-14 03:37:38.215804
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.nothing().filter(lambda x: x % 2 != 0) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x % 2 == 0) == Maybe.nothing()
    assert Maybe.just(1).filter(lambda x: x % 2 != 0) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda x: x % 2 == 0) == Maybe.nothing()
    assert Maybe.just(2).filter(lambda x: x % 2 != 0) == Maybe.nothing()
    assert Maybe.just(2).filter(lambda x: x % 2 == 0) == Maybe.just(2)

# Generated at 2022-06-14 03:37:46.431330
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    maybe_1 = Maybe(1, False)
    maybe_2 = Maybe.just(1)
    equals = Maybe(1, False) == Maybe(1, False)
    assert equals
    maybe_1 == maybe_2
    maybe_1 != Maybe.nothing()
    maybe_1 != Maybe(2, False)
    maybe_1 != Maybe(1, True)

    maybe_1 == Maybe(value=1, is_nothing=False)
    assert maybe_1 == Maybe(value=1, is_nothing=False)
    assert maybe_1 != Maybe(value=1, is_nothing=True)


# Generated at 2022-06-14 03:37:49.213747
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert id(Maybe(1, False).to_lazy().value()) == id(Maybe(1, False).value)
    assert Maybe.nothing().to_lazy().value() is None


# Generated at 2022-06-14 03:37:53.707447
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda value: value > 2) == Maybe.nothing()
    assert Maybe.just(1).filter(lambda value: value > 0) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda value: value > 1) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda value: value > 2) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda value: value > 0) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda value: value > 1) == Maybe.nothing()



# Generated at 2022-06-14 03:37:59.656441
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just('1') == Maybe.just('1')
    assert Maybe.just(1) != Maybe.just('1')
    assert Maybe.just('1') != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just('1')


# Generated at 2022-06-14 03:38:02.381370
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just("Hi") == Maybe.just("Hi")
    assert Maybe.just("Hi") != Maybe.just("hi")
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) != Maybe.nothing()


# Generated at 2022-06-14 03:38:09.820394
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(2) == Maybe.just(2)
    assert Maybe.nothing() == Maybe.nothing()
    assert not (Maybe.just(1) == Maybe.just(2))
    assert not (Maybe.just(1) == Maybe.nothing())
    assert not (Maybe.just(1) == object())
    assert not (Maybe.nothing() == object())


# Generated at 2022-06-14 03:38:18.942799
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    maybe_nothing = Maybe.just(None)
    maybe_1 = Maybe.just(1)

    assert maybe_nothing.to_lazy().run() is None
    assert maybe_1.to_lazy().run() == 1


# Generated at 2022-06-14 03:38:23.844461
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda v: v % 2 == 0) == Maybe.nothing()
    assert Maybe.just(2).filter(lambda v: v % 2 == 0) == Maybe.just(2)



# Generated at 2022-06-14 03:38:31.959359
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    expected_result = Maybe.just(5)

    result = Maybe.just(5) \
        .filter(lambda x: x == 5)

    assert expected_result == result, 'Should return Maybe.just(5) for lambda x: x == 5'

    result = Maybe.just(5) \
        .filter(lambda x: x == 2)

    assert Maybe.nothing() == result, 'Should return Maybe.nothing() for lambda x: x == 5'



# Generated at 2022-06-14 03:38:41.941462
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    @Lazy.thunk
    def thunk():
        return 'thunk'

    # Maybe.just(T) -> Maybe[T]
    assert Maybe.just(5) == Maybe(5, False)
    assert Maybe.just(5).to_lazy() == Lazy(lambda: 5)
    assert Maybe.just(5).to_lazy().evaluate() == 5
    assert Maybe.just(thunk).to_lazy().evaluate() == 'thunk'

    # Maybe.nothing -> Maybe[None]
    assert Maybe.nothing() == Maybe(None, True)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)
    assert Maybe.nothing().to_lazy().evaluate() is None


# Generated at 2022-06-14 03:38:46.052207
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    # Create Maybe
    maybe = Maybe.just(10)

    # Transform it to Lazy
    lazy = maybe.to_lazy()

    # Check that all values are equal
    assert(isinstance(lazy, Lazy))
    assert(maybe.is_nothing == lazy._is_nothing)
    assert(maybe.value == lazy._f())

# Generated at 2022-06-14 03:38:49.647382
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    maybe_a = Maybe.just(5)
    maybe_b = Maybe.nothing()

    assert maybe_a.to_lazy() == Lazy(lambda: 5)
    assert maybe_b.to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:38:57.925962
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    def add(x: int, y: int) -> int:
        return x + y

    assert Maybe.just(1).to_lazy() == Lazy(lambda: 1)
    assert Maybe.just(1).to_lazy().map(lambda x: x + 1) == Lazy(lambda: 2).map(lambda x: x + 1)
    assert Maybe.nothing().to_lazy().map(lambda x: x + 1) == Lazy(lambda: None).map(lambda x: x + 1)



# Generated at 2022-06-14 03:39:02.052977
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.box import Box
    from pymonet.lazy import Lazy

    assert Box(10).to_lazy().force() == Lazy(lambda: 10).force()



# Generated at 2022-06-14 03:39:06.240799
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: x > 0) == Maybe.just(1)
    assert Maybe.just(0).filter(lambda x: x > 1) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x > 0) == Maybe.nothing()


# Generated at 2022-06-14 03:39:11.046456
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(0).filter(lambda x: x % 2 == 0) == Maybe.just(0)
    assert Maybe.just(1).filter(lambda x: x % 2 == 0) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x % 2 == 0) == Maybe.nothing()



# Generated at 2022-06-14 03:39:22.343256
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    def test_value(value):
        return value == 5

    assert Maybe.just(5).filter(test_value) == Maybe.just(5)
    assert Maybe.just(10).filter(test_value) == Maybe.nothing()
    assert Maybe.nothing().filter(test_value) == Maybe.nothing()


# Generated at 2022-06-14 03:39:33.065392
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    test_cases = [
        {
            "input": (Maybe.just(10), lambda x: x > 5,),
            "output": Maybe.just(10)
        },
        {
            "input": (Maybe.just(4), lambda x: x > 5,),
            "output": Maybe.nothing()
        },
        {
            "input": (Maybe.nothing(), None,),
            "output": Maybe.nothing()
        },
    ]
    for test_case in test_cases:
        assert (
            Maybe.from_value(*test_case['input']).filter(test_case['input'][1]) ==
            test_case['output']
        )

# Generated at 2022-06-14 03:39:42.823765
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    from pymonet.box import Box

    assert Maybe.just(10).filter(lambda x: x > 10) == Maybe.nothing()
    assert Maybe.just(10).filter(lambda x: x < 10) == Maybe.nothing()
    assert Maybe.just(10).filter(lambda x: x == 10) == Maybe.just(10)

    assert Maybe.nothing().filter(lambda x: x > 10) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x < 10) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x == 10) == Maybe.nothing()



# Generated at 2022-06-14 03:39:46.850653
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    def filterer(value):
        return value == 'foo'

    assert Maybe.just('bar').filter(filterer) == Maybe.just('bar')
    assert Maybe.just('foo').filter(filterer) == Maybe.just('foo')



# Generated at 2022-06-14 03:39:57.550756
# Unit test for method filter of class Maybe
def test_Maybe_filter():

    m_int = Maybe(12, False)
    m_str = Maybe('asd', False)
    m_none = Maybe.nothing()

    assert m_int.filter(lambda x: x < 100).get_or_else(-1) == 12
    assert m_int.filter(lambda x: x > 100).get_or_else(-1) == -1

    assert m_str.filter(lambda x: len(x) < 10).get_or_else('') == 'asd'
    assert m_str.filter(lambda x: len(x) > 10).get_or_else('') == ''

    assert m_none.filter(lambda x: True).get_or_else(False) == False
    assert m_none.filter(lambda x: False).get_or_else(True) == True


#

# Generated at 2022-06-14 03:40:02.382526
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    """
    Tests for method filter for class Maybe.
    """
    assert Maybe.just(1).filter(lambda x: x > 0) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda x: x < 0) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x > 0) == Maybe.nothing()



# Generated at 2022-06-14 03:40:09.398493
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.monad_try import Try

    assert Try(
        Maybe.just(1).to_lazy().value, is_success=True
    ) == Try(
        1, is_success=True
    )
    assert Try(
        Maybe.nothing().to_lazy().value, is_success=True
    ) == Try(
        None, is_success=True
    )


# Generated at 2022-06-14 03:40:23.273059
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    """
        Test filter method of Maybe class.

        :return: Nothing
        :rtype: None
    """
    from .test_utils import assert_maybe_equals  # pylint: disable=import-error

    # pylint: disable=unused-variable
    predicate = lambda x: x > 5

    # pylint: disable=expression-not-assigned

    # pylint: disable=unused-variable
    assert_maybe_equals(
        Maybe.just(10).filter(lambda x: x > 5),
        Maybe.just(10)
    )

    # pylint: disable=unused-variable
    assert_maybe_equals(
        Maybe.just(4).filter(lambda x: x > 5),
        Maybe.nothing()
    )

    # pylint: disable=unused

# Generated at 2022-06-14 03:40:25.468699
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: True) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda x: False) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: True) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: False) == Maybe.nothing()



# Generated at 2022-06-14 03:40:30.659214
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    f = lambda: 2
    maybe_lazy = Maybe.just(f).to_lazy()
    assert isinstance(maybe_lazy, Lazy)
    assert callable(maybe_lazy.value)
    assert maybe_lazy.value() == f()
    assert callable(maybe_lazy.to_maybe().value)
    assert maybe_lazy.to_maybe().value() == f()


# Generated at 2022-06-14 03:40:43.202632
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda value: value == 0) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda value: value == 0) == Maybe.nothing()


# Generated at 2022-06-14 03:40:50.421763
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    from pymonet.box import Box

    assert Maybe.just(100).filter(lambda x: x >= 100) == Maybe.just(100)
    assert Maybe.just(100).filter(lambda x: x < 100) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x >= 100) == Maybe.nothing()
    assert Maybe.just(100).filter(lambda x: x >= 100).to_box() == Box(100)


# Generated at 2022-06-14 03:40:52.453394
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: x > 0) == Maybe.just(1)



# Generated at 2022-06-14 03:40:57.487591
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    # given
    x = Maybe.just(1)
    empty = Maybe.nothing()

    # when
    result = x.filter(lambda x: x % 2 == 0)
    empty_result = empty.filter(lambda x: x % 2 == 0)

    # then
    assert result == Maybe.nothing()
    assert empty_result == Maybe.nothing()


# Generated at 2022-06-14 03:41:00.813338
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: len(str(x)) > 1) == Maybe.nothing()
    assert Maybe.just(15).filter(lambda x: len(str(x)) > 1) == Maybe.just(15)

# Generated at 2022-06-14 03:41:04.411024
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)
    assert Maybe.just('a').to_lazy() == Lazy(lambda: 'a')



# Generated at 2022-06-14 03:41:09.256978
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)
    assert Maybe.just(1).to_lazy() == Lazy(lambda: 1)
    assert Maybe.just(1).bind(lambda x: Maybe.nothing()).to_lazy() == Lazy(lambda: None)
    assert Maybe.just(1).bind(lambda x: Maybe.just(2)).to_lazy() == Lazy(lambda: 2)
    

# Generated at 2022-06-14 03:41:16.042783
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just('T').filter(lambda a: a == 'T') \
        == Maybe.just('T')

    assert Maybe.just('T').filter(lambda a: a == 'F') \
        == Maybe.nothing()

    assert Maybe.nothing().filter(lambda a: a == 'T') \
        == Maybe.nothing()


# Generated at 2022-06-14 03:41:20.364296
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe.just(10).to_lazy() == Lazy(lambda: 10)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:41:22.013469
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe.just('lazy').to_lazy() == Lazy(lambda: 'lazy')
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)