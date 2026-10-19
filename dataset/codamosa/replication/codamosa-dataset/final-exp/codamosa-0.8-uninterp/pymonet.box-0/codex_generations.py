

# Generated at 2022-06-14 03:01:29.852157
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert Box(1).to_lazy().get() == 1



# Generated at 2022-06-14 03:01:30.823136
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    box1 = Box(2)
    box2 = Box(2)
    assert box1 == box2



# Generated at 2022-06-14 03:01:33.709251
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(9).to_lazy() == Lazy(lambda: 9)

# Generated at 2022-06-14 03:01:37.901480
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(10) == Box(10)
    assert not Box(10) == Box(20)
    assert not Box(10) == [1, 2, 3]
    assert not Box(10) == None



# Generated at 2022-06-14 03:01:39.973083
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(1) == Box(1)
    assert Box(1) != Box('1')
    assert Box(1) != None


# Generated at 2022-06-14 03:01:42.319467
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    lazy = Box(1).to_lazy()

    assert isinstance(lazy, Lazy) and lazy.fold() == 1

# Generated at 2022-06-14 03:01:45.126884
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1) == Box(1).to_lazy()



# Generated at 2022-06-14 03:01:48.732926
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(3).to_lazy().bind(int.__add__, 3) == 6


# Generated at 2022-06-14 03:01:51.136881
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:01:55.560857
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(23).to_lazy() == Lazy(lambda: 23)



# Generated at 2022-06-14 03:02:01.005445
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 'a') == Box('a').to_lazy()
    assert Lazy(lambda: 1) == Box(1).to_lazy()



# Generated at 2022-06-14 03:02:05.001446
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 5) == Box(5).to_lazy()



# Generated at 2022-06-14 03:02:08.522604
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test to_lazy method of Box class.

    :returns: nothing
    :rtype: None
    """
    box_value = 'box value!'
    box = Box(box_value)
    assert box.to_lazy().force() == box_value

# Generated at 2022-06-14 03:02:11.576231
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1).to_box() == Box(1)
    assert Box(Lazy(lambda: 1)).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:02:13.233816
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box('string').to_lazy() == Lazy(lambda: 'string')

# Generated at 2022-06-14 03:02:19.528921
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.validation import Validation
    from pymonet.monad_try import Try

    assert Validation(['test_error_1', 'test_error_2']).to_lazy() == \
           Lazy(lambda: Validation(['test_error_1', 'test_error_2']))
    assert Try('Test').to_lazy() == Lazy(lambda: Try('Test'))



# Generated at 2022-06-14 03:02:20.642075
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy().value() == 1



# Generated at 2022-06-14 03:02:23.733684
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    # Test 1
    # Test case data
    v = 5
    b = Box(v)
    # Test action
    result = b.to_lazy()
    # Test assertions
    assert isinstance(result, Lazy)
    assert result.value() == v



# Generated at 2022-06-14 03:02:34.127247
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad import Identity
    from pymonet.maybe import Maybe
    from pymonet.either import Right
    from pymonet.monad_try import Try
    from pymonet.validation import Validation

    # Check if value is available in lazy context
    assert Box('a').to_lazy().force() == 'a'
    # Check if lazy decorator is working
    assert Lazy(lambda: 'b').to_lazy() == Lazy(lambda: 'b')
    # Check if identity is working with Box and Lazy
    assert Box('c').to_lazy().to_box().value == 'c'
    assert Lazy(lambda: 'd').to_box().to_lazy() == Lazy(lambda: 'd')
    # Check if

# Generated at 2022-06-14 03:02:36.301514
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert_that(Box(2).to_lazy(), is_(Lazy(lambda: 2)))

# Generated at 2022-06-14 03:02:40.339352
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1).map(lambda x: x + 1) == Box(2).to_lazy().map(lambda x: x + 1)


# Generated at 2022-06-14 03:02:53.191353
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.monad import bind
    from pymonet.monad_option import map as option_map
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try
    from pymonet.monad_option import Some
    from pymonet.monad import lift

    # Test for not folded lazy
    original = Box(10)
    lazy = original.to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy == Lazy(lambda: original.value)

    # Test for folded lazy
    original = Box(10)
    lazy = original.to_lazy().fold()

    assert isinstance(lazy, Box)
    assert lazy == original

    # Test for lazy function with function in it
    original = Box(lambda x: x + 1)


# Generated at 2022-06-14 03:02:55.749579
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Box(42).to_lazy() == Lazy(lambda: 42)

# Generated at 2022-06-14 03:03:01.006462
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    # Given
    input_str = "input string"
    box = Box(input_str)

    # When
    lazy_value = box.to_lazy().get_value()

    # Then
    assert lazy_value() == input_str



# Generated at 2022-06-14 03:03:04.402326
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Box(10).to_lazy() == Lazy(lambda: 10)


# Generated at 2022-06-14 03:03:06.195527
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1) == Box(1).to_lazy()

# Generated at 2022-06-14 03:03:09.942793
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    value = 2
    box = Box(value)

    to_lazy = box.to_lazy()


# Generated at 2022-06-14 03:03:14.248565
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    def to_lazy():
        return Box(10).to_lazy()
    test_to_lazy = to_lazy()
    assert test_to_lazy.value() == 10
    assert repr(test_to_lazy) == 'Lazy[value=10]'

# Generated at 2022-06-14 03:03:19.863207
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Box(1).to_lazy() == Lazy(lambda: 1)
    assert Box(1).to_lazy().map(int) == Lazy(lambda: 1)
    assert Try(1).to_lazy().fold(int) == 1


# Generated at 2022-06-14 03:03:24.233326
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():

    def f():
        return 1

    assert Box(1).to_lazy().force() == 1
    assert Box(f).to_lazy().force()() == 1

# Generated at 2022-06-14 03:03:28.993369
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy() == (lambda: 1)



# Generated at 2022-06-14 03:03:32.779865
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    def get_value():
        return "some test"

    assert Box(get_value).to_lazy() == Lazy(get_value)



# Generated at 2022-06-14 03:03:34.955457
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Box(5).to_lazy() == Lazy(lambda: 5)

# Generated at 2022-06-14 03:03:37.209794
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert Box(1).to_lazy().value() == 1
    assert Box(100500).to_lazy().value() == 100500


# Generated at 2022-06-14 03:03:40.346281
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    # Given
    value = "test"

    # When
    lazy = Box(value).to_lazy()

    # Then
    assert lazy.value() == value

# Generated at 2022-06-14 03:03:42.223549
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    value = 'value'

    assert Box(value).to_lazy().force() == value


# Generated at 2022-06-14 03:03:45.812348
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Box(10).to_lazy().value == Lazy.unit(
        lambda: 10).value



# Generated at 2022-06-14 03:03:55.334743
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.immutable import ImmutableList
    from pymonet.immutable import ImmutableDictionary
    from pymonet.immutable import ImmutableSet
    from pymonet.immutable import ImmutableTuple

    assert Box(42).to_lazy() == Lazy(lambda: 42)
    assert Box('abc').to_lazy() == Lazy(lambda: 'abc')
    assert Box([1, 2, 3]).to_lazy() == Lazy(lambda: [1, 2, 3])
    assert Box((1, 2, 3)).to_lazy() == Lazy(lambda: (1, 2, 3))

# Generated at 2022-06-14 03:03:58.520515
# Unit test for method to_lazy of class Box
def test_Box_to_lazy(): # pragma: no cover
    from pymonet.lazy import Lazy

    lazy = Box(1).to_lazy()

    assert lazy == Lazy(lambda: 1)


# Generated at 2022-06-14 03:03:59.738376
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(2).to_lazy().value() == 2


# Generated at 2022-06-14 03:04:05.243171
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:04:12.263545
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    unit = Box(1).to_lazy()
    f = Lazy(lambda: Try(lambda x: x + 2, is_success=True))
    g = Lazy(lambda: Try(lambda x: x * 2, is_success=True))
    actual = unit.ap(f).ap(g).eval()
    expected = Try(6, is_success=True)
    assert(actual == expected)

# Generated at 2022-06-14 03:04:14.490959
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert isinstance(Box(42).to_lazy(), Lazy)

# Generated at 2022-06-14 03:04:16.926946
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    test transformation Box into Lazy with returning value function.

    :returns: None
    :rtype: None
    """
    from pymonet.lazy import Lazy

    assert Box(100).to_lazy() == Lazy(lambda: 100)



# Generated at 2022-06-14 03:04:20.939537
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Testing 'to_lazy' method of class Box
    """
    from pymonet.lazy import Lazy

    lazy = Box(5).to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy.fold() == 5

# Generated at 2022-06-14 03:04:24.741955
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    # given
    num: int = 5
    box: Box[int] = Box(num)

    # when
    lazy: Lazy[Callable[[], int]] = box.to_lazy()

    # then
    assert lazy.value() == num



# Generated at 2022-06-14 03:04:31.821333
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test for method to_lazy of class Box
    """
    from pymonet.lazy import Lazy

    a = 1
    assert Box(a).to_lazy() == Lazy(lambda: a),\
        'Box.to_lazy() did not return a Lazy monad.'

# Generated at 2022-06-14 03:04:42.655584
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.helpers import identity

    assert Box(7).to_lazy() == Lazy(lambda: 7)
    assert Box(7).to_lazy().map(lambda x: x + 1) == Lazy(lambda: 8)
    assert Box(7).to_lazy().map(identity) == Lazy(lambda: 7)
    assert Box(7).to_lazy().map2(Lazy(lambda: 8), lambda x, y: x + y) == Lazy(lambda: 15)
    assert Box(7).to_lazy().fold(identity, lambda _: 0) == 7
    assert Box(7).to_lazy().apply(Lazy(lambda: lambda x: x + 1)).fold(identity, lambda _: 0) == 8
   

# Generated at 2022-06-14 03:04:45.678716
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test case template function
    """
    assert Box(1).to_lazy().eval() == 1

# Generated at 2022-06-14 03:04:50.952126
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    box = Box(5)
    lazy = box.to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.value() == 5

# Generated at 2022-06-14 03:04:58.947147
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test function for method to_lazy of class Box.

    :returns: nothing
    :rtype: None
    """
    assert Box(10).to_lazy().fold() == 10



# Generated at 2022-06-14 03:05:03.702017
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    box = Box(42)
    lazy = box.to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.value.value == 42
    assert lazy.is_folded is False
# end test_Box_to_lazy


# Generated at 2022-06-14 03:05:07.520901
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box
    """
    lazy = Box(1).to_lazy()
    assert lazy.value() == 1

# Generated at 2022-06-14 03:05:09.035939
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Should return not folded lazy with function returning value.

    :return: None
    """
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:05:12.417594
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    lazy = Box(2).to_lazy()

    assert lazy.is_folded() == False
    assert lazy.unfold()() == 2

# Generated at 2022-06-14 03:05:20.265146
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    def get_inc_x():
        x = 0
        while True:
            x += 1
            yield x

    inc_x = get_inc_x()
    lazy_inc_x = Lazy(lambda: next(inc_x))
    assert lazy_inc_x.fold(lambda x: x) == 1
    assert lazy_inc_x.fold(lambda x: x) == 1
    assert lazy_inc_x.fold(lambda x: x) == 2
    assert lazy_inc_x.fold(lambda x: x) == 2
    assert lazy_inc_x.fold(lambda x: x) == 3
    assert lazy_inc_x.fold(lambda x: x) == 3

    inc_x = get_inc_x()
    box_inc_x = Box

# Generated at 2022-06-14 03:05:23.017173
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    m = Box(1).to_lazy()

    assert isinstance(m, Lazy)
    assert not m.is_folded()
    assert m.value() == 1

# Generated at 2022-06-14 03:05:25.667458
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy().fold() == 1

# Generated at 2022-06-14 03:05:29.549946
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.monad import Monad
    from pymonet.lazy import Lazy
    value = 42
    assert (Box(value).to_lazy() is Monad.pure(Lazy, value))

# Generated at 2022-06-14 03:05:31.187298
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(3).to_lazy() == Box(3).to_maybe().to_lazy()

# Generated at 2022-06-14 03:05:38.936750
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe
    result = Box(lambda : 1).to_lazy()
    assert result.fold(lambda : None)() == 1



# Generated at 2022-06-14 03:05:41.521822
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    """
    Test transform Box into Lazy
    """
    assert Box(1).to_lazy().fold() == 1



# Generated at 2022-06-14 03:05:43.151830
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert isinstance(
        Box(100).to_lazy(),
        Lazy,
    )



# Generated at 2022-06-14 03:05:47.204824
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.monad_maybe import Maybe
    from pymonet.monad_try import Try

    m = Maybe(42)
    t = Try(43, True)

    assert Box(123).to_lazy().value(lambda x: m.bind(lambda i: t.map(lambda j: i == x + j))) == Maybe.just(True)



# Generated at 2022-06-14 03:05:52.242818
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """Unit test for method `to_lazy` of class `Box`."""

    from pymonet.lazy import Lazy

    assert box_str.to_lazy() == Lazy(lambda: 'str_val')
    assert box_int.to_lazy() == Lazy(lambda: 1)
    assert box_obj.to_lazy() == Lazy(lambda: obj)


# Generated at 2022-06-14 03:05:55.894784
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    # 1. Set up
    from pymonet.lazy import Lazy

    # 2. Act
    lazy = Box(42).to_lazy()

    # 3. Assert
    assert isinstance(lazy, Lazy)
    assert lazy.value == 42

# Generated at 2022-06-14 03:05:58.904275
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    box = Box(42)
    lazy = box.to_lazy()
    assert lazy.value() == 42


# Generated at 2022-06-14 03:06:01.211073
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:06:03.037795
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy() == 2



# Generated at 2022-06-14 03:06:06.416593
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(0).to_lazy() == Lazy(lambda: 0)

# Generated at 2022-06-14 03:06:23.052904
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    import pytest

    from pymonet.monad_try import Failure

    box_value = Box(5)
    assert box_value.to_lazy().unsafe_run() == 5

    box_none = Box(None)
    assert box_none.to_lazy().unsafe_run() is None

    box_exc = Box(Failure(Exception()))

    with pytest.raises(Exception):
        box_exc.to_lazy().unsafe_run()

# Generated at 2022-06-14 03:06:26.071709
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert repr(Box(10).to_lazy()) == '<pymonet.Lazy monad at 0x7f979fc2d1f0>'


# Generated at 2022-06-14 03:06:28.382977
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    b = Box(1)
    assert b.to_lazy().fold() == 1



# Generated at 2022-06-14 03:06:31.847220
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit testing for to_lazy method of Box class.
    """
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:06:33.365411
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Lazy(lambda: 1) == Box(1).to_lazy()

# Generated at 2022-06-14 03:06:38.036706
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test for method to_lazy of class Box.

    :return: None
    """
    def func():  # pragma: no cover
        print('Hello')

    box = Box(func)
    lazy = box.to_lazy()

    assert lazy.value == box.value

# Generated at 2022-06-14 03:06:43.211987
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)
    assert Box((lambda x: x + 1)).to_lazy() == Lazy(lambda: lambda x: x + 1)



# Generated at 2022-06-14 03:06:46.262519
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box.
    """
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:06:48.496345
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    box = Box(100)
    lazy = box.to_lazy()
    assert lazy.get() == box.value


# Generated at 2022-06-14 03:06:50.182292
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(55).to_lazy().force() == 55

# Generated at 2022-06-14 03:07:01.992016
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:07:03.642084
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert Box(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:07:06.111578
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(10).to_lazy() == Lazy(lambda: 10)
    assert Box(11).to_lazy() == Lazy(lambda: 11)

# Generated at 2022-06-14 03:07:11.219226
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    import pymonet
    import pytest

    assert isinstance(Box(42).to_lazy(), pymonet.Lazy)

    with pytest.raises(TypeError):
        Box(42).to_lazy().eval(None)

    assert Box(42).to_lazy().eval() == 42



# Generated at 2022-06-14 03:07:13.124905
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert isinstance(Box(True).to_lazy(), Lazy)



# Generated at 2022-06-14 03:07:15.394775
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    b = Box(3)
    assert b.to_lazy().get() == 3

# Generated at 2022-06-14 03:07:20.608728
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(7).to_lazy().value() == 7
    assert Box('7').to_lazy().value() == '7'
    assert Box(['7', 'a']).to_lazy().value() == ['7', 'a']
    assert Box({"7": "a"}).to_lazy().value() == {"7": "a"}

# Generated at 2022-06-14 03:07:27.475242
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Take function returns value and applied this function on current box value and returns new box with mapped value.

    :param mapper: mapper function
    :type mapper: Function(A) -> B
    :returns: new box with mapped value
    :rtype: Box[B]
    """
    x = Box(1)
    assert x.bind(lambda x: x + 1) == 2


# Generated at 2022-06-14 03:07:29.294253
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(10).to_lazy() == Lazy(lambda: 10)
    assert Box(10).to_lazy().force() == 10



# Generated at 2022-06-14 03:07:31.373564
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for Box.to_lazy method
    """

    assert Lazy(lambda: 1) == Box(1).to_lazy()

# Generated at 2022-06-14 03:07:55.250237
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert isinstance(Box(10).to_lazy(), Lazy)
    assert Box(10).to_lazy().value() == 10
    assert Box(Box).to_lazy().value() == Box



# Generated at 2022-06-14 03:07:59.610503
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    """
    Tests for method to_lazy of class Box
    """
    assert Box(1).to_lazy().get() == 1
    assert Box('1').to_lazy().get() == '1'

# Generated at 2022-06-14 03:08:01.547547
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(10).to_lazy() == Lazy(lambda: 10)



# Generated at 2022-06-14 03:08:11.855934
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    """
    Unit test for method to_lazy of class Box.
    """
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try
    from pymonet.validation import Validation

    assert Lazy(lambda: 1) == Box(1).to_lazy()
    assert Lazy(lambda: Try(1, is_success=True)) == Box(Try(1, is_success=True)).to_lazy()
    assert Lazy(lambda: Validation.success(None)) == Box(Validation.success(None)).to_lazy()

# Generated at 2022-06-14 03:08:14.864750
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert str(Box(5).to_lazy()) == 'Lazy[value=5]'


# Generated at 2022-06-14 03:08:19.042227
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box
    """
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:08:24.053199
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from nose.tools import assert_equal
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    result = Box(3).to_lazy()

    assert_equal(result, Lazy(3))



# Generated at 2022-06-14 03:08:26.887391
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    box = Box(lambda x: x)
    lazy = Lazy(lambda: lambda x: x)
    assert box.to_lazy() == lazy, 'To lazy function of class Box are work incorrectly'

# Generated at 2022-06-14 03:08:33.025245
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Implements unit tests for Box.to_lazy method.
    """
    from pymonet.lazy import Lazy

    lazy_box = Lazy(lambda: 'five')

    assert Box(5).to_lazy() == lazy_box


# Generated at 2022-06-14 03:08:36.365862
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 12) == Box(12).to_lazy()


# Generated at 2022-06-14 03:09:20.648599
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(3).to_lazy() == Lazy(lambda: 3)

# Generated at 2022-06-14 03:09:26.914558
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe
    from pymonet.either import Right

    box = Box(Maybe)

    assert box.to_lazy() == Lazy(Maybe)

    assert box.to_lazy().get() == Maybe

    assert box.to_lazy().map(lambda m: m.no_value()).get() == Maybe.no_value()

    assert box.to_lazy().map(lambda m: m.just(Right)).get() == Maybe.just(Right)

    assert box.to_lazy().map(lambda m: m.just(Right).value).get() == Maybe.just(Right).value

# Generated at 2022-06-14 03:09:31.200274
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.monad_try import Try

    def inc(x):
        return x + 1

    side_effect = None

    def side_effect_fun(x):
        nonlocal side_effect

        side_effect = x

        return x

    box = Box(1).to_lazy().bind(lambda x: Lazy(lambda: inc(x))).bind(lambda x: Lazy(lambda: side_effect_fun(x))).bind(lambda x: Lazy(lambda: x + 1))

    assert box == Lazy(lambda: 4)

    assert side_effect == 2

# Generated at 2022-06-14 03:09:32.790692
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(3).to_lazy() == Lazy(lambda: 3)

# Generated at 2022-06-14 03:09:34.945980
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:09:44.032964
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    def test_function_1(value):
        return Lazy.unit(value)

    def test_function_2(value):
        return Try.success(value)

    assert Box(test_function_1(test_function_2(4))).to_lazy().value() == test_function_1(test_function_2(4)).value()



# Generated at 2022-06-14 03:09:46.515016
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(10).to_lazy() == Lazy(lambda: 10)

# Generated at 2022-06-14 03:09:50.198685
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    normal_box = Box(10)
    lazy_box = normal_box.to_lazy()
    assert lazy_box.value() == 10

    normal_box = Box(15)
    lazy_box = normal_box.to_lazy()
    assert lazy_box.value() == 15



# Generated at 2022-06-14 03:09:54.328988
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box.
    """
    # Test in not folded state
    assert Box(1).to_lazy() == Lazy(lambda: 1)
    assert Box('TEST').to_lazy() == Lazy(lambda: 'TEST')

    # Test in folded state
    assert Box(1).to_lazy().fold(to_value=True) == 1
    assert Box('TEST').to_lazy().fold(to_value=True) == 'TEST'

# Generated at 2022-06-14 03:10:11.684447
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box

    Function uses doctest.
    """
    from pymonet.lazy import Lazy
    from pymonet.doctest_helper import run_doctest
    doctest_data: str = """
    >>> box: Box[int] = Box(2 + 3)
    >>> box.to_lazy() == Lazy(lambda: 2 + 3)
    True
    """
    run_doctest(doctest_data, globals(), locals())

# Generated at 2022-06-14 03:11:00.940506
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box
    """
    assert Box(1).to_lazy().force() == 1



# Generated at 2022-06-14 03:11:05.003253
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(5).to_lazy() == Lazy(lambda: 5)
"""
##### Syntax sugar #####
"""
# Syntax sugar for __init__ method

# Generated at 2022-06-14 03:11:11.263026
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from random import randrange
    from pymonet.lazy import Lazy
    from pymonet.either import Right

    lazy_value = randrange(0, 100)
    box = Box(lazy_value)
    lazy_box = box.to_lazy()

    assert lazy_box == Lazy(lambda: lazy_value)
    assert lazy_box.value() == lazy_value



# Generated at 2022-06-14 03:11:15.534215
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    box = Box(1)
    lazy_value = Lazy(lambda: 1)

    assert box.to_lazy() == lazy_value



# Generated at 2022-06-14 03:11:22.452275
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert isinstance(Box(1).to_lazy(), Lazy)
    assert isinstance(Box(1).to_lazy().get_value(), int)
    assert Box(1).to_lazy().get_value() == 1


# Generated at 2022-06-14 03:11:26.209994
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Create Box with integer value and convert Box into Lazy Monad.
    """
    from pymonet.lazy import Lazy

    box = Box(1)
    lazy = box.to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy.value() == 1


# Generated at 2022-06-14 03:11:29.343136
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 0).to_lazy() == Lazy(lambda: 0)