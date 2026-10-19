

# Generated at 2022-06-14 03:01:37.176270
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(1) == Box(1)
    assert Box(None) == Box(None)



# Generated at 2022-06-14 03:01:41.146223
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(1) == Box(1)
    assert Box(1) != Box(2)
    assert Box('abc') == Box('abc')
    assert Box('abc') != Box('def')
    assert Box(1) != 'abc'
    assert Box('abc') != 1



# Generated at 2022-06-14 03:01:44.474997
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(1) == Box(1)
    assert Box(1) != Box(2)
    assert Box(1) != Box('1')
    assert Box(1) != None
    assert Box(1) != 1



# Generated at 2022-06-14 03:01:46.310959
# Unit test for method __eq__ of class Box
def test_Box___eq__():  # pragma: no cover
    assert Box(1) == Box(1)
    assert not (Box(1) == Box(2))
    assert not (Box(1) == 1)


# Generated at 2022-06-14 03:01:49.053996
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert Lazy(lambda: 'a') == Box('a').to_lazy()

# Generated at 2022-06-14 03:01:56.742494
# Unit test for method __eq__ of class Box
def test_Box___eq__():

    # Box and Box are equal with same type and value
    assert Box.__eq__(Box(1), Box(1)) is True

    # Box and Box are not equal with same type and different values
    assert Box.__eq__(Box(1), Box(2)) is False

    # Box and Box are not equal with different types
    assert Box.__eq__(Box(1), Box('1')) is False

    # Box and other object are not equal
    assert Box.__eq__(Box(1), object()) is False



# Generated at 2022-06-14 03:01:59.039477
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(1) == Box(1)



# Generated at 2022-06-14 03:01:59.952480
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(15).to_lazy().get_value() == 15



# Generated at 2022-06-14 03:02:08.993677
# Unit test for method __eq__ of class Box
def test_Box___eq__():  # pragma: no cover
    assert Box(0) == Box(0)
    assert Box(1) == Box(1)
    assert Box('test') == Box('test')
    assert Box([1, 2, 3]) == Box([1, 2, 3])

    assert Box(0) != Box(1)
    assert Box(1) != Box(0)
    assert Box('test') != Box('qwerty')
    assert Box('qwerty') != Box('test')
    assert Box([1, 2, 3]) != Box([2, 3, 4])
    assert Box([2, 3, 4]) != Box([1, 2, 3])


# Generated at 2022-06-14 03:02:14.712411
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    # when
    result = Box(3).to_lazy()
    result2 = Box(Try(3, is_success=True)).to_lazy().fmap(lambda x: x.value).fetch()

    # then
    assert result.fetch() == 3
    assert isinstance(result, Lazy)
    assert result2 == 3
    assert isinstance(result2, int)

# Generated at 2022-06-14 03:02:18.283532
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(12).to_lazy() == Lazy(lambda: 12)

# Generated at 2022-06-14 03:02:20.496562
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    a = Box(1)
    assert a.to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:02:29.739432
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.functor import Functor

    b1 = Box(1)
    b2 = Box(2)

    assert b1.map(lambda x: x + 1) == b2, 'Box map method'

    f = Functor.of(b1)
    assert isinstance(f, Functor), 'Box functor instance'
    assert f.map(lambda x: x + 1) == b2, 'Box map via functor'

    l1 = b1.to_lazy()
    l2 = Lazy(lambda: 3)
    l3 = Lazy(lambda: 1 + 2)
    l4 = Lazy(lambda: 1 + 5)
    l5 = Lazy(lambda: 1)


# Generated at 2022-06-14 03:02:32.100843
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(5).to_lazy().get() == 5

# Generated at 2022-06-14 03:02:40.390060
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy
    from pymonet.functor import is_functor
    from pymonet.applicative import is_applicative

    box = Box(3)
    assert is_functor(box.to_lazy())
    assert isinstance(box.to_lazy(), Lazy)
    assert box.to_lazy() == Lazy(lambda: 3)
    assert is_applicative(box.to_lazy())



# Generated at 2022-06-14 03:02:45.479911
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    a = Box(1)

    assert str(a.to_lazy()) == 'Lazy[value=1]'
    assert a.to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:02:48.622848
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy().map(lambda x: x()) == Lazy(lambda: 1)



# Generated at 2022-06-14 03:02:52.656435
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(lambda: 1).to_lazy() == Lazy(lambda: 1)
    assert Box(lambda: Box(1)).to_lazy() == Lazy(lambda: Box(1))

# Generated at 2022-06-14 03:02:55.562665
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box('hello').to_lazy() == Lazy(lambda: 'hello')

# Generated at 2022-06-14 03:02:59.145360
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe

    assert Box(5).to_lazy() == Lazy(lambda: 5)


# Generated at 2022-06-14 03:03:04.713899
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    lazy = Box(1).to_lazy()
    assert lazy.value(0) == 1
    assert lazy.fold(lambda _: 0, lambda _: 1) == 1

# Generated at 2022-06-14 03:03:07.975729
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    def add_one(value):
        return value + 1

    assert Box(2).to_lazy().map(add_one).map(add_one).force() == 4

# Generated at 2022-06-14 03:03:10.938277
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Tests whether method to_lazy return correct value or not.
    """
    assert Box(42).to_lazy() == Lazy(lambda: 42)


# Generated at 2022-06-14 03:03:12.439926
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    import pytest

    assert Box(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:03:13.920314
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy().bind(lambda x: Lazy(lambda: x + 1)).force() == 2

# Generated at 2022-06-14 03:03:16.232439
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    result = Box(1).to_lazy()
    assert(result.get() == 1)

# Generated at 2022-06-14 03:03:17.912130
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    assert Box(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:03:18.944269
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:03:21.815880
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    lazy = Box(3).to_lazy()
    assert lazy.value() == 3
    assert lazy.is_folded == False

# Generated at 2022-06-14 03:03:27.525173
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet import _do

    @_do(Box[str])
    def run_lazy_box():
        first: str = yield Box('first')
        second: str = yield Box('second')
        last: str = yield Box('last')

        return first + second + last

    assert str(run_lazy_box()) == "Box[value=firstsecondlast]"

# Generated at 2022-06-14 03:03:32.941912
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    def to_lazy_test():
        return Box(3).to_lazy().value() == 3
    assert to_lazy_test() is True



# Generated at 2022-06-14 03:03:34.345364
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    result = Box(10).to_lazy()

    assert result() == 10

# Generated at 2022-06-14 03:03:43.495121
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    result = Box(1).to_lazy()
    assert result == Lazy(lambda: 1)

    result = Box(1).to_lazy().map(lambda x: x + 1)
    assert result == Lazy(lambda: 2)

    result = Box(1).to_lazy().flat_map(lambda x: Lazy(lambda: x + 1))
    assert result == Lazy(lambda: 2)

    result = Box(1).to_lazy().flat_map(lambda x: Try(x + 1))
    assert result == Try(2, is_success=True)



# Generated at 2022-06-14 03:03:51.601512
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    """
    Test for method to_lazy of class Box.
    """
    from pymonet.lazy import Lazy

    assert Box(13).to_lazy() == Lazy(lambda: 13)
    assert Box('string').to_lazy() == Lazy(lambda: 'string')
    assert Box({'key': 'value'}).to_lazy() == Lazy(lambda: {'key': 'value'})
    assert Box(True).to_lazy() == Lazy(lambda: True)
    assert Box(None).to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 03:03:53.665341
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(5).to_lazy() == Lazy(lambda: 5)



# Generated at 2022-06-14 03:03:55.539630
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(42).to_lazy() == Lazy(lambda: 42)

# Generated at 2022-06-14 03:03:57.009930
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:03:58.740479
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    val = Box(42).to_lazy().eval()
    assert val == 42



# Generated at 2022-06-14 03:04:00.727258
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    box = Box(lambda a: a + 1)
    lazy = box.to_lazy()
    assert lazy.get()(1) == 2

# Generated at 2022-06-14 03:04:05.690492
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    inc = lambda x: x + 1
    box = Box(2)
    lazy = box.to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy.value() == 2
    assert lazy.map(inc).value() == 3

# Generated at 2022-06-14 03:04:16.340760
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    box = Box(10)

    lazy = box.to_lazy()
    assert lazy.value() == 10

# Generated at 2022-06-14 03:04:20.189761
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy() == (lambda: 1)
    assert Box('str').to_lazy() == (lambda: 'str')
    assert Box([1, 2]).to_lazy() == (lambda: [1, 2])
    assert Box({1, 2}).to_lazy() == (lambda: {1, 2})
    assert Box({'key': 'value'}).to_lazy() == (lambda: {'key': 'value'})
    assert Box(True).to_lazy() == (lambda: True)



# Generated at 2022-06-14 03:04:32.924822
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    try_monad = Try(10, is_success=True)
    lazy_monad = Lazy(lambda: 10)
    box_monad = Box(10)

    assert lazy_monad.get_or_else(0) == box_monad.to_lazy().get_or_else(0)
    assert try_monad.get_or_else(0) == box_monad.to_lazy().get_or_else(0)

# Generated at 2022-06-14 03:04:35.090331
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    def func():
        return 1

    assert Box(1).to_lazy() == Lazy(func)


# Generated at 2022-06-14 03:04:37.014827
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy().fold() == 1

# Generated at 2022-06-14 03:04:39.247471
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert Box(3).to_lazy().fold() == 3


# Generated at 2022-06-14 03:04:43.731237
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    box_try = Try(5, is_success=True)
    lazy_from_box_try = box_try.to_lazy()

    assert isinstance(lazy_from_box_try, Lazy)
    assert lazy_from_box_try.value() == 5



# Generated at 2022-06-14 03:04:46.013254
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:04:48.380164
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(10).to_lazy().is_evaluated()



# Generated at 2022-06-14 03:04:52.614767
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    box = Box(100)
    lazy_box = box.to_lazy()
    assert isinstance(lazy_box, Lazy)
    assert lazy_box.is_folded() is False
    assert lazy_box.get_value() == 100



# Generated at 2022-06-14 03:05:01.945297
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(2).to_lazy() == Lazy(lambda: 2)



# Generated at 2022-06-14 03:05:05.813090
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert isinstance(Box(10).to_lazy(), Lazy)

    assert Lazy(lambda: Box(10)).bind(lambda value: value).value.value == Box(Box(10)).value.value
    assert Lazy(lambda: Box(10)).bind(lambda value: value.value).value == Box(Box(10)).value.value
    assert Lazy(lambda: Box(10)).bind(lambda value: value.value * 2.0).value == Box(20.0).value


# Generated at 2022-06-14 03:05:07.012356
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(42).to_lazy().get_value() == 42



# Generated at 2022-06-14 03:05:07.990153
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(2).to_lazy() == Lazy(lambda: 2)



# Generated at 2022-06-14 03:05:11.829941
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert Box(10).to_lazy().fold(lambda: 30) == 10
    assert Box('str').to_lazy().fold(lambda: 30) == 'str'

# Generated at 2022-06-14 03:05:14.773764
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    a = Box(1)
    b = Lazy(lambda: 1)

    assert a.to_lazy() == b


# Generated at 2022-06-14 03:05:15.948038
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert isinstance(Box(1).to_lazy(), Lazy)


# Generated at 2022-06-14 03:05:17.371404
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert isinstance(Box(5).to_lazy(), Lazy)

# Generated at 2022-06-14 03:05:19.491281
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy() == Box(1).to_lazy().flat_map(lambda x: Box(x))
    assert isinstance(Box(1).to_lazy(), Box)


# Generated at 2022-06-14 03:05:21.694857
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(11).to_lazy() == Lazy.unit(11)

# Generated at 2022-06-14 03:05:47.735712
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    """
    Make unit test for function to_lazy of class Box
    """
    from pymonet.monad_try import Try

    assert Box(1).to_lazy() == Lazy(lambda: 1)
    assert Box(Try(1, is_success=True)).to_lazy() == Lazy(lambda: Try(1, is_success=True))
    assert Box('Ivan').to_lazy() == Lazy(lambda: 'Ivan')
    assert Box(1.01).to_lazy() == Lazy(lambda: 1.01)
    assert Box(True).to_lazy() == Lazy(lambda: True)
    assert Box([1, 2, 3, 1]).to_lazy() == Lazy(lambda: [1, 2, 3, 1])
    assert Box

# Generated at 2022-06-14 03:05:50.211989
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(Box('value')) == Lazy(lambda: 'value')

# Generated at 2022-06-14 03:05:55.154000
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for Box to_lazy method.
    """
    from pymonet.lazy import Lazy
    from pymonet.test_utils import chunk_test

    result = Box('foo').to_lazy()

    assert isinstance(result, Lazy) is True
    assert result.is_folded is False
    assert chunk_test(result.value) == 'foo'



# Generated at 2022-06-14 03:05:57.175856
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.monad_lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:06:00.268316
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1) == Box(1).to_lazy()

# Generated at 2022-06-14 03:06:03.327112
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    lazy = Lazy(lambda: 1)

    assert Box(1).to_lazy() == lazy


# Generated at 2022-06-14 03:06:06.557170
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test that Box converted to Lazy returns the same value as contained in Box

    :returns: Nothing
    :rtype: None
    """
    assert 1 == Box("test").to_lazy().call()


# Generated at 2022-06-14 03:06:13.181438
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test Box.to_lazy method.
    """
    from pymonet.lazy import Lazy

    b = Box("Some value")
    l = b.to_lazy()

    assert isinstance(l, Lazy)
    assert l.get() == b.value



# Generated at 2022-06-14 03:06:17.688700
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe

    # Arrange
    box = Box(value=5)

    # Act
    lazy = box.to_lazy()
    maybe = lazy.map(lambda x: x * 2)

    # Assert
    assert isinstance(lazy, Lazy)
    assert lazy.value() == 5
    assert isinstance(maybe, Maybe)
    assert isinstance(maybe.value, int)
    assert maybe.value == 10

# Generated at 2022-06-14 03:06:31.609366
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad import Monad
    from pymonet.monad_try import Try

    # type: Callable[[object], bool]
    def is_lazy(value: object) -> bool:
        return isinstance(value, Lazy)

    assert Monad.is_monad(Box('test').to_lazy())
    assert is_lazy(Box('test').to_lazy())
    assert is_lazy(Box(1).to_lazy())
    assert is_lazy(Box(Try(1)).to_lazy())
    assert is_lazy(Box(Try.success(1)).to_lazy())
    assert is_lazy(Box(Try(0, is_success=False)).to_lazy())


# Generated at 2022-06-14 03:07:17.094733
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test that to_lazy transform box into non folded lazy with function returning previous value.
    """
    from pymonet.lazy import Lazy

    box = Box(10)
    lazy = box.to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy.is_folded is False
    assert lazy.value() == 10


# Generated at 2022-06-14 03:07:19.434526
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    box = Box('test_Box')
    lazy = box.to_lazy()
    assert lazy.get() == 'test_Box'

# Generated at 2022-06-14 03:07:22.793285
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    box = Box("*")
    lazy = box.to_lazy()
    assert lazy.fold() == "*"



# Generated at 2022-06-14 03:07:31.099223
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    import unittest

    from pymonet.lazy import Lazy

    class TestCase(unittest.TestCase):

        def test_returns_not_folded_Lazy_with_function_returning_previous_value(self):
            box = Box(10)

            self.assertIsInstance(box.to_lazy(), Lazy)
            self.assertFalse(box.to_lazy().is_folded)
            self.assertEqual(box.to_lazy().eval(), 10)

    unittest.main()


# Generated at 2022-06-14 03:07:33.389633
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(12).to_lazy().__repr__() == 'Lazy[evaluated=False]'

# Generated at 2022-06-14 03:07:37.271961
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1).__eq__(Box(1).to_lazy())

# Generated at 2022-06-14 03:07:41.095004
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    new_lazy = Box(1).to_lazy()
    assert isinstance(new_lazy, Lazy)
    assert new_lazy.computed() == False
    assert new_lazy.get()() == 1
    assert new_lazy.computed() == True

# Generated at 2022-06-14 03:07:42.095658
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert Box(10).to_lazy().fold() == 10

# Generated at 2022-06-14 03:07:43.036407
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box('x').to_lazy().value() == 'x'



# Generated at 2022-06-14 03:07:45.061154
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    box = Box(1)

    assert box.to_lazy().fold() == 1

# Generated at 2022-06-14 03:09:16.853153
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    f = lambda x: x + 1
    box = Box(1)
    lazy_monad = box.to_lazy()
    assert isinstance(lazy_monad, Lazy)
    assert lazy_monad.unfold() == 1
    assert lazy_monad.map(f).unfold() == 2



# Generated at 2022-06-14 03:09:18.017476
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    """
    Test to_lazy method of Box class.
    """
    assert Box(5).to_lazy().evaluate() == 5



# Generated at 2022-06-14 03:09:21.754263
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box.
    """
    assert Box(1).to_lazy().get() == 1


# Generated at 2022-06-14 03:09:27.361849
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box('hello').to_lazy() == Lazy(lambda: 'hello')
    assert Box(1).to_lazy() == Lazy(lambda: 1)
    assert Box([1, 2, 3]).to_lazy() == Lazy(lambda: [1, 2, 3])

# Generated at 2022-06-14 03:09:29.842391
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    lazy = Box(1).to_lazy()
    assert(lazy.unwrap() == 1)



# Generated at 2022-06-14 03:09:32.342184
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:09:35.476197
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1) == Box(1).to_lazy()


# Generated at 2022-06-14 03:09:41.486517
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.monad_try import Try
    from pymonet.monad_maybe import Maybe

    assert (
        Box(None).to_lazy()
        == Maybe.just(None).to_lazy()
        == Try(None).to_lazy()
    )

# Generated at 2022-06-14 03:09:46.075062
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_maybe import Maybe

    maybe = Maybe.just(2)
    box = maybe.value

    print(str(box))
    print(str(box.to_lazy()))
    assert str(box.to_lazy()) == str(Lazy(lambda: box.value))


# Generated at 2022-06-14 03:09:51.552178
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    test_value = 123
    test_box = Box(test_value)
    test_lazy = test_box.to_lazy()
    assert isinstance(test_lazy, Lazy)
    assert test_lazy.value() == test_value
    assert test_lazy.is_folded() is True
    assert test_lazy.has_error() is False
    assert test_lazy.is_success() is True



# Generated at 2022-06-14 03:11:35.337745
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(4).to_lazy() == Lazy(lambda: 4)

