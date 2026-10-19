

# Generated at 2022-06-14 03:01:29.985648
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet import Lazy

    f = lambda: 5

    assert Box(10).to_lazy() == Lazy(f)

# Generated at 2022-06-14 03:01:34.089163
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box
    """
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)
    assert Box('a').to_lazy() == Lazy(lambda: 'a')
    assert Box((1, 2)).to_lazy() == Lazy(lambda: (1, 2))
    assert Box([1, 2]).to_lazy() == Lazy(lambda: [1, 2])
    assert Box({'x': 1, 'y': 2}).to_lazy() == Lazy(lambda: {'x': 1, 'y': 2})



# Generated at 2022-06-14 03:01:38.816976
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    lazy_box = Box(42).to_lazy()

    assert isinstance(lazy_box, Lazy)
    assert lazy_box.fold(lambda: None) == 42

# Generated at 2022-06-14 03:01:41.934644
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test Box.to_lazy() function.

    :return: None
    :rtype: None
    """
    box = Box(lambda x: x ** 2)
    assert box.to_lazy().force()(5) == 25

# Generated at 2022-06-14 03:01:45.241672
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    # GIVEN
    value = 1
    box = Box(value)

    # WHEN
    actual = box.to_lazy()

    # THEN
    assert actual == Lazy(lambda: 1)



# Generated at 2022-06-14 03:01:47.298848
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    # Given
    v = 5

    # When
    res = Box(v).to_lazy()

    # Then
    assert res.value() == v


# Generated at 2022-06-14 03:01:48.348502
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(42).to_lazy().fold() == 42


# Generated at 2022-06-14 03:01:50.905653
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    assert Box(2).to_lazy() == Lazy(lambda: 2)

# Generated at 2022-06-14 03:01:58.152412
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(1) == Box(1)
    assert Box(1) != Box(2)
    assert Box('abc') == Box('abc')
    assert Box((1, 'abc', [1, 2])) == Box((1, 'abc', [1, 2]))



# Generated at 2022-06-14 03:02:01.172330
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(1) == Box(1)
    assert Box('unit-test') != Box('unit-test1')
    assert not isinstance(Box(1), int)


# Generated at 2022-06-14 03:02:07.548594
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box
    """
    # given
    box = Box(lambda x: x + 1)
    lazy = box.to_lazy()

    # when
    result = lazy()

    # then
    assert result == box.value


# Generated at 2022-06-14 03:02:08.837273
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:02:12.840969
# Unit test for method __eq__ of class Box
def test_Box___eq__():  # pragma: no cover
    assert Box(1) == Box(1)
    assert Box(None) == Box(None)
    assert Box('Some') == Box('Some')
    assert Box((1, 2)) == Box((1, 2))
    assert Box({1: 2}) == Box({1: 2})
    assert Box(1) != Box(2)



# Generated at 2022-06-14 03:02:18.426739
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(1) == Box(1)
    assert Box('a') == Box('a')
    assert Box([1, 2]) == Box([1, 2])
    assert Box({1, 2}) == Box({1, 2})
    assert Box({1: 'a', 2: 'b'}) == Box({1: 'a', 2: 'b'})



# Generated at 2022-06-14 03:02:20.348634
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    box = Box(12)

    assert box == Box(12)
    assert box != Box(11)
    assert box != 12


# Generated at 2022-06-14 03:02:24.790156
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy
    from pymonet.functor import Functor

    box = Box(42)
    actual = box.to_lazy()
    expected = Lazy(42)

    assert (isinstance(actual, Lazy))
    assert (isinstance(Functor.map(actual, lambda x: x * 2), Lazy))
    assert (actual == expected)

# Generated at 2022-06-14 03:02:29.508612
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(1) == Box(1)
    assert not Box(1) == Box(2)
    assert not Box(1) == None



# Generated at 2022-06-14 03:02:37.852537
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy
    from pymonet.monad_list import List

    lazy: Lazy = Box([1,2,3,4,5,6]).to_lazy().map(lambda x: List(*x).filter(lambda x: x % 2 == 0))
    assert lazy.value() == [2, 4, 6]

# Generated at 2022-06-14 03:02:39.570376
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(1) == Box(1)
    assert Box(1) != Box(2)



# Generated at 2022-06-14 03:02:44.920465
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(1) == Box(1)
    assert not (Box(1) == Box(2))
    assert not (Box(1) == None)
    assert not (Box(1) == 1)
    assert not (Box(1) == '1')



# Generated at 2022-06-14 03:02:48.093306
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy().fold() == 1


# Generated at 2022-06-14 03:02:52.129993
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    # Assert that lazy monad, returned from to_lazy method is not folded
    assert Box(12).to_lazy().is_folded() is False


# Unit test of method to_maybe of Box

# Generated at 2022-06-14 03:02:55.552524
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_funcs import to_lazy
    assert to_lazy(Box(123)) == Lazy(lambda: 123)

# Generated at 2022-06-14 03:02:58.165448
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(12).to_lazy() == Box(12).to_lazy().force()

# Generated at 2022-06-14 03:03:00.942820
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    val = Box(1).to_lazy()

    assert val.to_box().value == 1

# Generated at 2022-06-14 03:03:05.399342
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:03:08.176163
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    def _f():
        return 5

    assert Box(_f()).to_lazy().fold()() == _f()



# Generated at 2022-06-14 03:03:11.108559
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    # given
    box = Box(1)

    # when
    lazy = box.to_lazy()

    # then
    assert lazy == Lazy(lambda: 1)

# Generated at 2022-06-14 03:03:12.222028
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert Box(5).to_lazy().value() == 5

# Generated at 2022-06-14 03:03:14.038539
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover

    from pymonet.lazy import Lazy

    assert Box(12).to_lazy() == Lazy(lambda: 12)

# Generated at 2022-06-14 03:03:17.636287
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet import Lazy

    l = Lazy(lambda: 1)

    assert l == Box(1).to_lazy()

# Generated at 2022-06-14 03:03:20.952147
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box.
    """
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 42) == Box(42).to_lazy()

# Generated at 2022-06-14 03:03:23.141058
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert Box(1).to_lazy().is_folded is False
    assert Box(1).to_lazy().value() == 1


# Generated at 2022-06-14 03:03:26.207759
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box.

    :return: none
    """
    assert Box(3).to_lazy().fold()() == 3



# Generated at 2022-06-14 03:03:28.993447
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(5).to_lazy().call() == 5

# Generated at 2022-06-14 03:03:31.232393
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy().fold() == 1


# Generated at 2022-06-14 03:03:33.434457
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(42).to_lazy().get() == 42
    assert Box('test').to_lazy().get() == 'test'


# Generated at 2022-06-14 03:03:36.617004
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box.
    """
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 2) == Box(2).to_lazy()



# Generated at 2022-06-14 03:03:39.378526
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:03:43.442862
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad import is_monad

    assert Lazy.unit(10) == Box(10).to_lazy()
    assert is_monad(Box(10).to_lazy())



# Generated at 2022-06-14 03:03:48.521760
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert isinstance(Box(1).to_lazy(), Lazy)



# Generated at 2022-06-14 03:03:52.236831
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    # GIVEN
    data = 'python'

    # WHEN
    actual_data = Box(data).to_lazy()

    # THEN
    assert not actual_data.is_folded
    assert actual_data.value() == data



# Generated at 2022-06-14 03:03:53.529009
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy().value() == 1

# Generated at 2022-06-14 03:03:59.189063
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Failure

    assert Lazy(lambda: 5).to_box() == Box(5)
    assert Lazy(lambda: [1, 2, 3]).to_box() == Box([1, 2, 3])
    assert Lazy(lambda: Failure(exception=ValueError('error'))).to_box() == Box(Failure(exception=ValueError('error')))



# Generated at 2022-06-14 03:04:04.796570
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy, foldl

    assert Box(10).to_lazy() == Lazy(lambda: 10)  # equals of lazies
    assert foldl(Box(10).to_lazy()) == foldl(Lazy(lambda: 10))  # foldl of lazy (function calling) of Box and Lazy with function


# Generated at 2022-06-14 03:04:08.896503
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box.
    """

    # Test on empty Box
    box = Box(1)
    lazy = box.to_lazy()
    assert lazy.fold() == 1


# Generated at 2022-06-14 03:04:10.395969
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(5).to_lazy().fold(lambda: 5) == 5

# Generated at 2022-06-14 03:04:13.319632
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    def value_func():
        return 'lazy_value_func'

    lazy_value_func = Lazy(value_func)
    assert Box(lazy_value_func).to_lazy() == lazy_value_func

# Generated at 2022-06-14 03:04:16.648825
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    value = 5
    box = Box(value)
    lazy = box.to_lazy()

    assert lazy == Lazy(lambda: value)

# Generated at 2022-06-14 03:04:18.337523
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(5).to_lazy() == Lazy(lambda: 5)


# Generated at 2022-06-14 03:04:26.497886
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    box = Box(1)
    lazy = box.to_lazy()

    assert box == lazy.value()

# Generated at 2022-06-14 03:04:29.514540
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    def f():
        return 1

    assert Box(f).to_lazy()._lz_f() == 1

# Generated at 2022-06-14 03:04:32.381431
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:04:34.456110
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1) == (Box(1).to_lazy())

# Generated at 2022-06-14 03:04:39.130261
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box.
    """

    # Check that Box[A].to_lazy() returns Lazy[Function(() -> A)]
    assert Box(3).to_lazy().value() == 3

# Generated at 2022-06-14 03:04:40.361905
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(10).to_lazy().get_or_else(0) == 10

# Generated at 2022-06-14 03:04:42.965419
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert isinstance(Box(1).to_lazy(), Lazy)



# Generated at 2022-06-14 03:04:48.043128
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for Box_to_lazy method.
    """
    from pymonet.lazy import Lazy
    assert Box(100).to_lazy() == Lazy(lambda: 100)

# Generated at 2022-06-14 03:04:57.288575
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe

    x = Box(1)
    lazy = x.to_lazy()
    assert type(lazy) == Lazy
    # check that lazy is not evaluated and return Box with value 1
    assert lazy.eval() == x
    assert lazy.bind(lambda y: Maybe.just(y)).eval() == Maybe.just(1)
    assert lazy.map(lambda y: y * 2).bind(lambda y: Maybe.just(y)).eval() == Maybe.just(2)
    assert lazy.ap(Lazy(lambda: lambda y: y * 2)).bind(lambda y: Maybe.just(y)).eval() == Maybe.just(2)

# Generated at 2022-06-14 03:05:03.976516
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Transform Box into Lazy with returning value function.

    :returns: not folded Lazy monad with function returning previous value
    :rtype: Lazy[Function(() -> A)]
    """
    from pymonet.lazy import Lazy

    assert Box(10).to_lazy() == Lazy(lambda: 10)
    assert Box('1').to_lazy() == Lazy(lambda: '1')


# Generated at 2022-06-14 03:05:14.060881
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1) == Box(1).to_lazy()

# Generated at 2022-06-14 03:05:16.093677
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(42).to_lazy() == Lazy(lambda: 42)



# Generated at 2022-06-14 03:05:19.166420
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test class method to_lazy.
    """

    from pymonet.lazy import Lazy

    message = 'test message'
    lazy = Box(message).to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy.fold() == message



# Generated at 2022-06-14 03:05:22.503455
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box.
    """
    from pymonet.lazy import Lazy  # circular import with pymonet/lazy.py

    assert Box(10).to_lazy() == Lazy(lambda: 10)

# Generated at 2022-06-14 03:05:25.853922
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert Box(3).to_lazy() == Box(3).to_lazy()


# Generated at 2022-06-14 03:05:29.363450
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    result = Box(42).to_lazy()

    assert isinstance(result, Lazy)
    assert result.evaluate() == 42



# Generated at 2022-06-14 03:05:39.718716
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe
    from pymonet.either import Right
    from pymonet.validation import Validation

    assert Box(2).to_lazy() == Lazy(lambda: 2)
    assert Box(2).to_lazy() != Lazy(lambda: 3)
    assert Box(2).to_lazy() != Lazy(lambda: None)
    assert Box(2).to_lazy() != Lazy(None)
    assert Box(2).to_lazy() != Lazy(None)
    assert Box(2).to_lazy() != Lazy(3)


# Generated at 2022-06-14 03:05:40.992764
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(10).to_lazy() == Lazy(lambda: 10)


# Generated at 2022-06-14 03:05:44.079425
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    def create_lazy(value):
        return Lazy(lambda: value)

    def check_value(value):
        return value

    box = Box(10)
    assert box == create_lazy(10).bind(check_value)

# Generated at 2022-06-14 03:05:45.943781
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(2).to_lazy() == Lazy(lambda: 2)



# Generated at 2022-06-14 03:06:05.797483
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(42).to_lazy().force() == 42

# Generated at 2022-06-14 03:06:08.027722
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(8).to_lazy().value() == 8

# Generated at 2022-06-14 03:06:10.564221
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box('Hello world').to_lazy() == Lazy(lambda: 'Hello world')

# Generated at 2022-06-14 03:06:14.854909
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(5).to_lazy() == Lazy(lambda: 5)
    assert Box('a').to_lazy() == Lazy(lambda: 'a')


# Generated at 2022-06-14 03:06:18.617011
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    expected = Lazy(lambda: 10)
    assert Box(10).to_lazy() == expected



# Generated at 2022-06-14 03:06:23.052689
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box.
    """

    def validate_box_to_lazy(a):
        print(a)
        assert a == 1

    validate_box_to_lazy(Box(1).to_lazy().value())

# Generated at 2022-06-14 03:06:25.631891
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:06:26.471833
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(42).to_lazy() == Lazy(lambda: 42)



# Generated at 2022-06-14 03:06:34.460512
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    # Test for Box[int]
    assert Box(10).to_lazy() == Lazy(lambda: 10)

    # Test for Box[bool]
    assert Box(True).to_lazy() == Lazy(lambda: True)

    # Test for Box[float]
    assert Box(23.8).to_lazy() == Lazy(lambda: 23.8)

    # Test for Box[string]
    assert Box('some string').to_lazy() == Lazy(lambda: 'some string')

    # Test for Box[int array]
    assert Box([1, 2, 3]).to_lazy() == Lazy(lambda: [1, 2, 3])

    # Test for Box[bool array]
    assert Box([True, False]).to_lazy() == L

# Generated at 2022-06-14 03:06:38.604387
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    :type _: int
    :returns: 1
    :rtype: int
    """
    from pymonet.lazy import Lazy

    return Box(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:07:20.252088
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box('test_value').to_lazy() == Lazy(lambda: 'test_value')

# Generated at 2022-06-14 03:07:24.012506
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_maybe import Maybe

    assert Maybe.unit(Box(1)).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:07:27.812831
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Lazy(lambda: 5).bind(lambda a: Lazy(lambda: a + 1)).value() == Lazy(lambda: 5).to_lazy().bind(lambda a: a + 1).value()

# Generated at 2022-06-14 03:07:29.850396
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():

    value = 'Some value'
    box = Box(value)
    assert box.to_lazy().unpack() == value



# Generated at 2022-06-14 03:07:31.934532
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(5).to_lazy() == Lazy(lambda: 5)

# Generated at 2022-06-14 03:07:33.670982
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test to_lazy method of Box class.

    """
    assert Box(5).to_lazy().fork() == 5


# Generated at 2022-06-14 03:07:36.970616
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(2).to_lazy().fold() == 2
    assert Box(-1).to_lazy().fold() == -1


# Generated at 2022-06-14 03:07:41.960212
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    b1 = Box(1)
    l1 = b1.to_lazy()

    assert id(b1) != id(l1)
    assert isinstance(l1, Lazy)
    assert l1.is_folded() is False
    assert l1.get_value() is None
    assert b1.value == 1


if __name__ == '__main__':  # pragma: no cover
    test_Box_to_lazy()

# Generated at 2022-06-14 03:07:44.113311
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert(Box(2).to_lazy() == Lazy(lambda: 2))


# Generated at 2022-06-14 03:07:48.955265
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 0).fold(lambda x: x) == Box(0).to_lazy().fold(lambda x: x)
    assert str(Lazy(lambda: 'Hello')) == str(Box('Hello').to_lazy())


# Generated at 2022-06-14 03:09:18.964619
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    import pymonet.lazy

    # type: () -> int
    # This function return 1
    f = lambda: 1

    # type: pymonet.lazy.Lazy[int]
    # Lazy monad that contains f
    lazy = Box(f).to_lazy()

    assert isinstance(lazy, pymonet.lazy.Lazy)
    assert lazy.value == f


# Generated at 2022-06-14 03:09:22.119979
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(lambda: 2).to_lazy().value() == Box(lambda: 2).to_lazy().value()



# Generated at 2022-06-14 03:09:26.585130
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(5).to_lazy().is_success()
    assert not Box(5).to_lazy().is_failure()

    assert Box(5).to_lazy().fold() == 5



# Generated at 2022-06-14 03:09:29.179065
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    boxed = Box(100)
    lazy = boxed.to_lazy()

    assert lazy == Lazy(lambda: 100)



# Generated at 2022-06-14 03:09:30.798606
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert Box(2).to_lazy().get() == 2

# Generated at 2022-06-14 03:09:35.621797
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test function to_lazy of class Box
    """
    assert Box(42).to_lazy() == Box(42).to_maybe().to_lazy() == Box(42).to_either().to_lazy()

# Generated at 2022-06-14 03:09:39.907664
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    value = 1
    box = Box(value)

    assert box.to_lazy() == Lazy(lambda: value)



# Generated at 2022-06-14 03:09:48.521730
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box
    """
    assert Box(1).to_lazy().value() == 1
    assert Box('b').to_lazy().value() == 'b'
    assert Box(True).to_lazy().value() == True
    assert Box([1, 2, 3]).to_lazy().value() == [1, 2, 3]
    assert Box({1, 2, 3}).to_lazy().value() == {1, 2, 3}
    assert Box({'a': 1, 'b': 2}).to_lazy().value() == {'a': 1, 'b': 2}

# Generated at 2022-06-14 03:09:50.235439
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:09:51.740955
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(10).to_lazy().is_folded() == False
    assert Box(20).to_lazy().value() == 20


# Generated at 2022-06-14 03:11:29.841219
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    box1 = Box(5)
    lazy1 = box1.to_lazy()
    assert lazy1 == Lazy(lambda: 5)
