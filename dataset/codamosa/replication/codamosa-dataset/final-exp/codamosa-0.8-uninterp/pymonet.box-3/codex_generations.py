

# Generated at 2022-06-14 03:01:30.895884
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(42).to_lazy() == Lazy(lambda: 42)



# Generated at 2022-06-14 03:01:35.712279
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(1) == Box(1)
    assert Box(2) == Box(2)
    assert Box(1) != Box(2)
    assert Box('3') == Box('3')
    assert Box('4') == Box('4')
    assert Box('3') != Box('4')



# Generated at 2022-06-14 03:01:36.314088
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    box = Box(1)
    assert box == Box(1)



# Generated at 2022-06-14 03:01:38.519592
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(1) == Box(1)
    assert Box(1) != Box(2)



# Generated at 2022-06-14 03:01:40.441375
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(1) != Box(2)
    assert Box(1) != []
    assert Box(1) == Box(1)


# Generated at 2022-06-14 03:01:47.995776
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.base_monad_test import BaseMonadTest
    from pymonet.lazy import Lazy

    BaseMonadTest.test_value_map(
        box=Box(5),
        expected_value=5
    )

    BaseMonadTest.test_value_bind(
        box=Box(5),
        expected_value=5
    )

    BaseMonadTest.test_value_ap(
        box=Box(5),
        expected_value=5
    )

    BaseMonadTest.test_to_lazy(
        box=Box(5),
        expected_value=Lazy(lambda: 5)
    )



# Generated at 2022-06-14 03:01:52.285888
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    # Given: two box with same values
    box1 = Box(True)
    box2 = Box(True)

    # When: do check for equality
    result = box1 == box2

    # Then: function should return True
    assert result is True


# Generated at 2022-06-14 03:02:00.351482
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    def func(x):
        return x + 1
    box = Box(10).map(func)
    lazy = box.to_lazy()
    assert isinstance(lazy, Lazy)
    assert box.value != lazy.run()
    assert box.value == lazy.force().run()


# Generated at 2022-06-14 03:02:06.132324
# Unit test for method __eq__ of class Box
def test_Box___eq__():  # pragma: no cover
    box1 = Box(1)
    box1_1 = Box(1)
    box2 = Box(2)

    assert(box1.__eq__(box1_1) is True)
    assert(box1.__eq__(box2) is False)

# Generated at 2022-06-14 03:02:08.841190
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    box = Box(1).to_lazy()
    assert box.is_folded() is False
    assert box.value() == 1
    assert str(box) == 'Lazy(lambda: 1)'



# Generated at 2022-06-14 03:02:11.393201
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Lazy[str]().unit('test') == Box('test').to_lazy().unit('test')

# Generated at 2022-06-14 03:02:12.765888
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:02:16.299399
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    import pytest

    from pymonet.lazy import Lazy

    box = Box(1)
    assert box.to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:02:23.346089
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box.
    """
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Failure

    assert Lazy(lambda: 1) == Box(1).to_lazy()
    assert Lazy(lambda: 1).map(lambda value: value + 1) == Box(1).to_lazy().map(lambda value: value + 1)
    assert Failure('error 1') == Box('error 1').to_lazy().get()
    assert Failure('error 1').map(lambda value: value + 1) == Box('error 1').to_lazy().map(lambda value: value + 1)

# Generated at 2022-06-14 03:02:29.698416
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box
    """
    from pymonet.lazy import Lazy
    from pymonet.exceptions import MonetError

    lazy = Box(5).to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy == Lazy(lambda: 5)

    try:
        lazy.get_value()
        assert False
    except MonetError:
        pass

# Generated at 2022-06-14 03:02:33.150448
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box.

    :return: nothing
    """
    box = Box(3)
    assert box.to_lazy().value() == 3

# Generated at 2022-06-14 03:02:37.793720
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy().value() == 1
    assert Box('a').to_lazy().value() == 'a'
    assert Box(True).to_lazy().value() is True
    assert Box([]).to_lazy().value() == []


# Generated at 2022-06-14 03:02:50.030264
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.operators import eq

    assert Lazy(lambda: 2) == eq(Box(2).to_lazy(), Lazy(lambda: 2)), "Box value didn't converted to expected Lazy monad"
    assert Lazy(lambda: 'abc') == eq(Box('abc').to_lazy(), Lazy(lambda: 'abc')), "Box value didn't converted to expected Lazy monad"
    assert Lazy(lambda: [1, 2, 3]) == eq(Box([1, 2, 3]).to_lazy(), Lazy(lambda: [1, 2, 3])), "Box value didn't converted to expected Lazy monad"

# Generated at 2022-06-14 03:02:51.576352
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(10).to_lazy().value(None) == 10

# Generated at 2022-06-14 03:02:56.627762
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert isinstance(Box(5).to_lazy(), Lazy)
    assert Box(5).to_lazy().__str__() == "Lazy[value=<function <lambda> at 0x10f612f28>]"
    assert Box(5).to_lazy().fold()() == 5


# Generated at 2022-06-14 03:02:59.270563
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    lazy = Box(42).to_lazy()

    assert lazy.value == 42



# Generated at 2022-06-14 03:03:01.150404
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    box = Box(5)
    lazy_value = box.to_lazy()
    lazy_value.fold(lambda x: x) == 5

    assert lazy_value.fold(lambda x: x) == 5

# Generated at 2022-06-14 03:03:06.714596
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    """Unit test for method to_lazy of class Box"""
    from pymonet.lazy import Lazy

    box = Box(1337)
    assert box.to_lazy() == Lazy(lambda: 1337)


# Generated at 2022-06-14 03:03:14.427509
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Box(5).to_lazy() == Lazy(lambda: 5)
    assert Box(5).to_lazy().fold() == 5
    assert Box(5).to_lazy().fold() == 5
    assert Box('lol').to_lazy().fold() == 'lol'
    assert Box({'key': 'value'}).to_lazy().fold() == {'key': 'value'}



# Generated at 2022-06-14 03:03:16.765146
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert Box(1).to_lazy().value() == 1


# Generated at 2022-06-14 03:03:18.849912
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy
    assert Box(3).to_lazy() == Lazy(lambda: 3)



# Generated at 2022-06-14 03:03:23.245214
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test Box.to_lazy() method
    """

    # Arrange
    box = Box(5)

    # Act
    result = box.to_lazy()

    # Assert
    assert result.is_error() is False
    assert result.get_value() == 5



# Generated at 2022-06-14 03:03:27.173746
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    def function_to_test() -> int:
        return 42

    box = Box(42)

    assert box.to_lazy() == Lazy(lambda: 42)
    assert box.to_lazy() == Lazy(function_to_test)



# Generated at 2022-06-14 03:03:31.411770
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert type(Box(1).to_lazy()) == Lazy


# Generated at 2022-06-14 03:03:37.209862
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    def func():
        return Try(5)

    box = Box(func())
    lazy_monad = box.to_lazy()

    assert isinstance(lazy_monad, Lazy), 'box.to_lazy() is not instance of Lazy'
    assert lazy_monad.eval() == Try(5), 'box.to_lazy() is not function returning previous value'

# Generated at 2022-06-14 03:03:40.715576
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.monoid import Sum

    a = Sum(1)
    b = Box(a)
    c = b.to_lazy()
    d = c.fold()

    assert b == Box(Sum(1))
    assert d == Sum(1)

# Generated at 2022-06-14 03:03:43.103049
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:03:45.437563
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    def func():
        return 1

    assert Box(1).to_lazy() == Lazy(func)

# Generated at 2022-06-14 03:03:46.737697
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    lazy = Box(12).to_lazy()

    assert lazy.evaluate() == 12

# Generated at 2022-06-14 03:03:51.272905
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 4).to_lazy() == Lazy(lambda: 4)
    assert Box(4).to_lazy() == Lazy(lambda: 4)
    assert Lazy(lambda: Box(4)).to_lazy() == Lazy(lambda: Lazy(lambda: Box(4)))

# Generated at 2022-06-14 03:03:54.458783
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy() == Box(1).to_lazy()
    assert Box(1).to_lazy().to_lazy() == Box(1).to_lazy()

# Generated at 2022-06-14 03:03:56.167451
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Box(5).to_lazy() == Lazy(lambda: 5)

# Generated at 2022-06-14 03:03:59.149115
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe

    assert isinstance(Box(Maybe.just(42)).to_lazy(), Lazy)

# Generated at 2022-06-14 03:04:01.096546
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(12).to_lazy() == Lazy(lambda: 12)



# Generated at 2022-06-14 03:04:04.983833
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy() == Box(1).to_lazy()
    assert Box(1).to_lazy().run() == Box(1).to_lazy().run()



# Generated at 2022-06-14 03:04:09.429896
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    lazy_value = Lazy(lambda: 10)
    assert Box(10).to_lazy() == lazy_value

# Generated at 2022-06-14 03:04:12.929381
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    import pytest

    test_data = [
        (42, 42),
        ('test', 'test'),
     ]

    for value, expected in test_data:
        with pytest.raises(AssertionError):
            Lazy(lambda: expected) == Box(value).to_lazy()



# Generated at 2022-06-14 03:04:15.518003
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:04:19.190262
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.functor import Functor

    box = Box([1, 2, 3])
    lazy = box.to_lazy()
    assert isinstance(lazy, Lazy)
    assert isinstance(lazy, Functor)
    assert lazy == Lazy(lambda: [1, 2, 3])
    assert lazy.equals(Lazy(lambda: [1, 2, 3]))



# Generated at 2022-06-14 03:04:21.317086
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box.to_lazy(Box(5)) == 5

# Generated at 2022-06-14 03:04:25.415674
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    value = 'value'
    box = Box(value)

    from pymonet.lazy import Lazy

    assert box.to_lazy() == Lazy(lambda: value)

# Generated at 2022-06-14 03:04:34.930463
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    """
    Test Box monad method to_lazy.
    """

    from pymonet.lazy import Lazy

    box = Box(10)
    lazy = box.to_lazy()

    def lazy_to_str(lazy):
        return "[" + str(lazy.value()) + "]"

    assert lazy == Lazy(lambda: 10), 'Box.to_lazy() function return incorrect lazy'

    assert lazy_to_str(lazy) == "[10]", 'Lazy of Box is incorrect'

# Generated at 2022-06-14 03:04:37.363113
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    value = 5
    box = Box(value)
    lazy = box.to_lazy()
    assert lazy() == value

# Generated at 2022-06-14 03:04:41.000386
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    f = lambda: 5

    actual = Box(5).to_lazy()

    assert isinstance(actual, Lazy)
    assert actual.is_folded() is False
    assert actual.value() == f()



# Generated at 2022-06-14 03:04:45.007512
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:04:55.694132
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Lazy(lambda: 1).to_box() == Box(1)
    assert Lazy(Try(lambda: 1 / 0)).to_box() == Try(lambda: 1 / 0).to_box()
    assert Lazy(Try(lambda: 1 / 0)).map(lambda x: x + 1).to_box() == Box(Try(lambda: 1 / 0))

# Generated at 2022-06-14 03:04:58.084662
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Try(Box(42).to_lazy()).is_success
    assert Try(Box(42).to_lazy()).get_or_else(Lazy.of(lambda: -1)) == 42

# Generated at 2022-06-14 03:05:02.306032
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    box = Box(1)
    lazy = box.to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.value() == 1


# Generated at 2022-06-14 03:05:04.072355
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert Box('a').to_lazy() == Lazy(lambda: 'a')

# Generated at 2022-06-14 03:05:06.189218
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():

    assert Box(1).to_lazy().value == 1
    assert Box("foo").to_lazy().value == "foo"

# Generated at 2022-06-14 03:05:09.254532
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy
    from pymonet.boxes import Box

    # Check that lazy value is not evaluated
    lazy = Box(1).to_lazy()
    assert lazy == Lazy(lambda: 1)

# Generated at 2022-06-14 03:05:12.658589
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Tests for method to_lazy of class Box
    """
    assert Box(42).to_lazy().fold() == 42

# Generated at 2022-06-14 03:05:13.940204
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box('smth').to_lazy() == Lazy(lambda: 'smth')

# Generated at 2022-06-14 03:05:16.567022
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert Box(1).to_lazy() == Box(1)
    assert Box(1).to_lazy().to_lazy() == Box(1)



# Generated at 2022-06-14 03:05:17.724291
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(True).to_lazy().unsafe_get() == True

# Generated at 2022-06-14 03:05:26.801341
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from random import randint
    from time import time

    before_time = time()
    assert Box(randint(1, 100)).to_lazy() == Lazy(lambda: randint((time() - before_time) * 100, 100))



# Generated at 2022-06-14 03:05:29.130905
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:05:32.312668
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(2).to_lazy().get() == 2


# Generated at 2022-06-14 03:05:34.290896
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.container import test_container_to_lazy

    test_container_to_lazy(Box, Lazy)


# Generated at 2022-06-14 03:05:36.970561
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Box(42).to_lazy() == Lazy(lambda: 42)



# Generated at 2022-06-14 03:05:39.127036
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:05:42.422790
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    box = Box(3)
    lazy = box.to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.fold(lambda: 0) == box.value



# Generated at 2022-06-14 03:05:45.728868
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    b = Box(42)
    l = Lazy(lambda: 42)
    assert b.to_lazy() == l
    assert l.force() == 42
    assert b.value == 42

# Generated at 2022-06-14 03:05:47.135026
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    box = Box(8)
    assert box.to_lazy() == Lazy(8)


# Generated at 2022-06-14 03:05:56.484073
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)
    assert Box(-1).to_lazy() == Lazy(lambda: -1)
    assert Box(1.0).to_lazy() == Lazy(lambda: 1.0)
    assert Box(True).to_lazy() == Lazy(lambda: True)
    assert Box([]).to_lazy() == Lazy(lambda: [])
    assert Box(()).to_lazy() == Lazy(lambda: ())
    assert Box({}).to_lazy() == Lazy(lambda: {})
    assert Box('').to_lazy() == Lazy(lambda: '')

# Generated at 2022-06-14 03:06:12.380617
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    """
    Unit test for method to_lazy of class Box
    """
    from pymonet.lazy import Lazy

    def foo():
        return Box(42)

    a = foo()
    b = Lazy.create(foo).map(lambda x: x.value)

    assert a.value == b.force()

# Generated at 2022-06-14 03:06:14.465429
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(2).to_lazy().fold() == 2

# Generated at 2022-06-14 03:06:18.675839
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    def test_function(_: None) -> int:
        return 5

    assert Box(5).to_lazy() == Lazy(test_function)


# Generated at 2022-06-14 03:06:24.129998
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    box = Box("MyValue")
    assert box.to_lazy() == Lazy(lambda: "MyValue")


# Generated at 2022-06-14 03:06:28.020540
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monet import Monet

    assert Box(123).to_lazy() == Lazy(Monet.return_)


# Generated at 2022-06-14 03:06:29.542568
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    assert Box(42).to_lazy() == Lazy(lambda: 42)


# Generated at 2022-06-14 03:06:35.202974
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
   lazy = Box(lambda x: x + 1).to_lazy()
   assert_equal(lazy, Lazy(lambda: x + 1))

   lazy = Box(lambda y: y * y).to_lazy()
   assert_equal(lazy, Lazy(lambda: y * y))


# Generated at 2022-06-14 03:06:37.029825
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(2).to_lazy().get() == 2

# Generated at 2022-06-14 03:06:38.263483
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy
    box = Box('test')
    assert Lazy(lambda: 'test') == box.to_lazy()

# Generated at 2022-06-14 03:06:43.358756
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box
    """
    # given
    box = Box(2)

    # when
    lazy = box.to_lazy()

    # then
    assert lazy.is_nothing()

    assert lazy.get_or_raise() == 2

# Generated at 2022-06-14 03:07:04.994545
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy, sum
    from pymonet.list_ import List

    assert Box(100).to_lazy() == Lazy(lambda: 100)  # Check if to_lazy doesn't create different Lazy

    # Check if to_lazy is lazy
    assert sum(List(1, 2, 3)).to_lazy().to_list() == [6]



# Generated at 2022-06-14 03:07:11.421852
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    """
    Unit test for method to_lazy of class Box

    """
    from pymonet.lazy import Lazy
    from pymonet.functor import Functor

    box = Box(5)
    lazy_value = box.to_lazy()

    assert isinstance(lazy_value, Lazy)
    assert isinstance(lazy_value, Functor)
    assert lazy_value.value() == 5

# Generated at 2022-06-14 03:07:12.594315
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy().value() == 1

# Generated at 2022-06-14 03:07:17.749673
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pylint: disable=W0612
    from pymonet.lazy import Lazy

    box = Box(42)
    lazy = box.to_lazy()
    assert lazy.is_lazy()
    assert isinstance(lazy.value, Lazy)

# Generated at 2022-06-14 03:07:20.493309
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1) == Box(1).to_lazy()



# Generated at 2022-06-14 03:07:23.445002
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(4).to_lazy() == Lazy(lambda: 4)

# Generated at 2022-06-14 03:07:26.200486
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    lazy = Box(3).to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.is_folded() == False


# Generated at 2022-06-14 03:07:29.306413
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    # Given
    box = Box(1)

    # When
    lazy = box.to_lazy()

    # Then
    assert lazy.value == 1


# Generated at 2022-06-14 03:07:32.052850
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.monad_try import Try

    box = Box(1)
    assert box.to_lazy().fold() == 1

    try_ = Try(1)
    assert box.to_lazy() == try_.to_lazy()


# Generated at 2022-06-14 03:07:33.481648
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(10).to_lazy() == Lazy(lambda: 10)


# Generated at 2022-06-14 03:08:16.689432
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.monoid import Sum

    assert Box(3).to_lazy() == Lazy(lambda: 3)
    assert Box(Sum(3)).to_lazy().fmap(lambda x: x.value + 1) == 4


# Generated at 2022-06-14 03:08:19.329531
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    box = Box(42)
    lazy = box.to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy.fold() == 42

# Generated at 2022-06-14 03:08:21.257203
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert(Box(1).to_lazy() == Lazy(lambda: 1))

# Generated at 2022-06-14 03:08:24.363928
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert Box(10).to_lazy() == Lazy(lambda: 10)



# Generated at 2022-06-14 03:08:25.652106
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(42).to_lazy().get() == 42

# Generated at 2022-06-14 03:08:29.972494
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(10).to_lazy().fold(lambda: 0) == 10
    assert Box(-10).to_lazy().fold(lambda: 0) == -10

# Generated at 2022-06-14 03:08:33.340005
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box("test").to_lazy() == Lazy("test")



# Generated at 2022-06-14 03:08:37.052533
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(10).to_lazy() == Lazy(lambda: 10)
    assert Box('abc').to_lazy() == Lazy(lambda: 'abc')
    assert Box(None).to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 03:08:37.819127
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy().value == 1

# Generated at 2022-06-14 03:08:39.489568
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:10:01.717341
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy, fold

    lazy = Box(42).to_lazy()
    assert lazy == Lazy(lambda: 42)
    assert fold(lazy) == 42



# Generated at 2022-06-14 03:10:05.822116
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:10:08.512767
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(10).to_lazy() == Lazy(lambda: 10)


# Generated at 2022-06-14 03:10:12.504187
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    # Given
    expected = Lazy(lambda: 1)
    actual = Box(1).to_lazy()

    # Then
    assert actual == expected


# Generated at 2022-06-14 03:10:24.318605
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Run test on Box.to_lazy method.

    :return: (None)
    """
    assert Box(5).to_lazy() == Box(5).to_lazy()

# Generated at 2022-06-14 03:10:25.772704
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert B

# Generated at 2022-06-14 03:10:29.986742
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert Box(1).to_lazy().fold()() == 1
    assert Box(2).to_lazy().map(lambda x: x + 1).fold()() == 3


# Generated at 2022-06-14 03:10:31.970191
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(5).to_lazy() == Lazy(lambda: 5)

# Generated at 2022-06-14 03:10:33.958156
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 10) == Box(10).to_lazy()

# Generated at 2022-06-14 03:10:36.170927
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy() == Lazy(lambda: 1)