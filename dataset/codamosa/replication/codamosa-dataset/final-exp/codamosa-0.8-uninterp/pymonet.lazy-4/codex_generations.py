

# Generated at 2022-06-14 03:31:31.470555
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    # Python 3.4
    assert Lazy.of(lambda num: num * 2).ap(Lazy.of(4)) == Lazy.of(8)



# Generated at 2022-06-14 03:31:34.903119
# Unit test for method map of class Lazy
def test_Lazy_map():
    lazy = Lazy(lambda x: x + 1)
    mapped_lazy = lazy.map(lambda x: x ** 2)

    assert mapped_lazy.get(1) == 4



# Generated at 2022-06-14 03:31:46.848160
# Unit test for method get of class Lazy
def test_Lazy_get():  # pragma: no cover
    assert Lazy.of(1).get() == 1

    assert Lazy(lambda a: a + 1).get(1) == 2

    assert Lazy(lambda a: a + 1).map(lambda a: a * 2).get(2) == 6

    assert Lazy(lambda a: a + 1).bind(
        lambda a:
            Lazy(lambda b: b * 2).bind(
                lambda b:
                    Lazy(lambda c: c + 3)
            )
    ).bind(
        lambda a:
            Lazy(lambda b: b * 2).bind(
                lambda b:
                    Lazy(lambda c: c + 3)
            )
    ).get(3) == 12



# Generated at 2022-06-14 03:31:52.033603
# Unit test for method get of class Lazy
def test_Lazy_get():
    # noinspection PyMissingOrEmptyDocstring
    def _test_empty():
        lazy_instance = Lazy(lambda: 3)
        assert lazy_instance.get() == 3

    def _test_not_empty():
        lazy_instance = Lazy(lambda: 4)
        lazy_instance.get()
        assert lazy_instance.get() == 4

    _test_empty()
    _test_not_empty()


# Generated at 2022-06-14 03:32:02.548065
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    # pylint: disable=W0612
    from pymonet.maybe import Maybe

    def fn(x):
        return Lazy(lambda *args: x * 3)

    def fn2(x):
        return Lazy(lambda *args: x * 2)

    assert Lazy.of(5).ap(fn(5)) == Lazy.of(5 * 3)
    assert Lazy(lambda *args: Maybe.of(5)).ap(fn(5)).get() == Maybe.of(5 * 3)
    assert Lazy(lambda *args: Maybe.of(5)).ap(fn2(5)).get() == Maybe.of(5 * 2)



# Generated at 2022-06-14 03:32:08.468961
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    assert Lazy.of(42) == Lazy.of(42)
    assert Lazy.of(42) != Lazy.of(24)
    assert Lazy.of(42) != [1, 2, 3]

# Generated at 2022-06-14 03:32:12.198373
# Unit test for method get of class Lazy
def test_Lazy_get():  # pragma: no cover
    # Given
    def no_param_function():
        return 'lazy value'

    lazy_object = Lazy(no_param_function)

    # When
    evaluation = lazy_object.get()

    # Then
    assert evaluation == 'lazy value'



# Generated at 2022-06-14 03:32:14.025720
# Unit test for method get of class Lazy
def test_Lazy_get():
    assert Lazy(lambda: 0).get() == 0



# Generated at 2022-06-14 03:32:20.514896
# Unit test for method map of class Lazy
def test_Lazy_map():
    from unittest import TestCase

    from pymonet.functor import Functor

    class TestLazy(TestCase):

        def test_map(self):
            lazy = Lazy(lambda: 5)
            result = lazy.map(lambda x: x + 1)
            self.assertEqual(6, result.get())

        def test_map_with_lambda(self):
            lazy = Lazy(lambda: 5)
            result = lazy.map(lambda x: x + 1)
            self.assertEqual(6, result.get())

    Suites.add_suite(TestLazy, 'test_map')



# Generated at 2022-06-14 03:32:24.159968
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    a = Lazy(lambda x: x)
    b = Lazy(lambda x: x)

    assert a == a
    assert b == b
    assert a != b

# Generated at 2022-06-14 03:32:31.573745
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    lazy_list = Lazy.of(lambda a: [a])
    lazy_value = Lazy.of(2)
    assert lazy_value.ap(lazy_list) == lazy_list.map(lambda x: x(2))

# Generated at 2022-06-14 03:32:34.429111
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    lazy = Lazy.of(5)
    assert lazy.bind(lambda x: Lazy.of(x + 1)).get() == 6



# Generated at 2022-06-14 03:32:41.686060
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def plus(x: int) -> int:
        return x + 1

    lazy = Lazy(lambda: 1).bind(plus)
    assert lazy.get() == 2

    lazy = Lazy(lambda: 1).bind(lambda x: Lazy(lambda: x + 1))
    assert lazy.get() == 2

    lazy = Lazy(lambda: 1).bind(lambda x: Lazy(lambda: x + 1)).map(lambda x: x * 2)
    assert lazy.get() == 4

# Generated at 2022-06-14 03:32:45.276763
# Unit test for method get of class Lazy
def test_Lazy_get():

    def testing_function(a: int, b: int) -> int:
        return a + b

    assert Lazy(testing_function).get(1, 2) == 3




# Generated at 2022-06-14 03:32:55.917809
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    from pymonet.function import compose

    p = Lazy.of(lambda x: x + 1).map(lambda x: x * 2).map(lambda x: x ** 3)

    q = Lazy.of(lambda x: x).map(compose(lambda x: x ** 3, lambda x: x * 2, lambda x: x + 1))

    assert p == q

    n = Lazy.of(lambda x: x + 1).map(lambda x: x * 2).map(lambda x: x ** 3)

    m = Lazy.of(lambda x: x + 1).map(lambda x: x ** 3).map(lambda x: x * 2)

    assert not n == m



# Generated at 2022-06-14 03:33:02.937648
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    # given
    def construct_fn1(*args):
        return 1

    def construct_fn2(*args):
        return 2

    # when
    l1 = Lazy(construct_fn1)
    l2 = Lazy(construct_fn2)
    l3 = Lazy(construct_fn1)

    # then
    assert l1 == l1
    assert l1 != l2
    assert l3 == l3



# Generated at 2022-06-14 03:33:07.645533
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def add(x):
        return x + 1

    def to_lazy(x):
        return Lazy(lambda *args: add(x))

    assert Lazy(lambda *args: 4).bind(to_lazy).constructor_fn() == 5



# Generated at 2022-06-14 03:33:17.267611
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():  # pragma: no cover
    from tests.test_lazy import NUMBER

    # two Lazy are equal when both are evaluated and constructor function return the same value
    assert Lazy.of(NUMBER) == Lazy.of(NUMBER)
    assert Lazy.of(NUMBER).map(lambda number: number + 1) == Lazy.of(NUMBER).map(lambda number: number + 1)

    # two Lazy are not equal when both are evaluated and constructor function return the different value
    assert Lazy.of(NUMBER) != Lazy.of(NUMBER + 1)
    assert Lazy.of(NUMBER).map(lambda number: number + 1) != Lazy.of(NUMBER)

    # two Lazy are not equal when one from them is evaluated and second is not

# Generated at 2022-06-14 03:33:24.919028
# Unit test for method map of class Lazy
def test_Lazy_map():
    from pymonet.box import Box

    assert Lazy.of('hello').map(str.upper).get() == 'HELLO'
    assert Lazy.of(Box.of('hello')).map(str.upper).get() == Box('HELLO')
    assert Lazy.of((lambda x: x.upper())).map(str.upper).get() == (lambda x: x.upper().upper())
    assert Lazy.of(('hello')).map(lambda x: Lazy.of(x)).get() == 'hello'
    assert Lazy.of((lambda x: Lazy.of('hello'))).map(lambda x: x.get()).get() == 'hello'


# Generated at 2022-06-14 03:33:36.351380
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    test_lazy_one = Lazy.of(lambda: None)
    test_lazy_two = Lazy.of(lambda: None)
    assert test_lazy_one == test_lazy_two
    assert test_lazy_one == test_lazy_one

    test_lazy_one = Lazy.of(lambda: 1)
    test_lazy_two = Lazy.of(lambda: 1)
    assert test_lazy_one == test_lazy_two

    test_lazy_one = Lazy.of(lambda: 1)
    test_lazy_two = Lazy.of(lambda: 2)
    assert test_lazy_one != test_lazy_two



# Generated at 2022-06-14 03:33:44.504297
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    assert Lazy(lambda: 0) == Lazy(lambda: 0)
    assert Lazy(lambda: 0) == Lazy.of(0)
    assert Lazy(lambda: 0) != Lazy(lambda: 1)
    assert Lazy(lambda: 0) != Lazy.of(1)
    assert Lazy(lambda: 0) != None



# Generated at 2022-06-14 03:33:52.845436
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    from .func import identity
    from .func import compose
    from .func import constant

    assert Lazy.of(1) == Lazy.of(1)
    assert Lazy.of(5) == Lazy.of(5)
    assert Lazy(identity) == Lazy(identity)

    assert Lazy.of(1) != Lazy.of(2)
    assert Lazy.of(5) != Lazy.of(6)
    assert Lazy(identity) != Lazy(compose(identity, identity))
    assert Lazy(compose(identity, identity)) != Lazy(constant)



# Generated at 2022-06-14 03:33:58.069160
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    def constructor_fn():
        return 'foo'

    def mapper(x):
        return x

    lazy1 = Lazy(constructor_fn)
    lazy2 = Lazy(constructor_fn)
    lazy1.map(mapper)
    lazy2.map(mapper)
    assert lazy1 == lazy2

# Generated at 2022-06-14 03:34:02.613946
# Unit test for method get of class Lazy
def test_Lazy_get():
    """
    Test Lazy's get method with not empty constructor_fn
    """
    def fn(x):
        return x + 1

    lazy = Lazy.of(2).map(fn)
    assert lazy.get() == fn(2)
    assert lazy.is_evaluated



# Generated at 2022-06-14 03:34:14.951805
# Unit test for method get of class Lazy
def test_Lazy_get():
    from pymonet.box import Box
    from pymonet.tuple import Tuple

    one = Lazy.of(1)
    two = Lazy.of(2)

    assert one.get() == 1
    assert one.get() == 1
    assert two.get() == 2
    assert one.get() == 1

    sum_one_and_two = one.bind(lambda x: two.map(lambda y: Tuple.of(x, y)))
    assert sum_one_and_two.get() == Tuple.of(1, 2)

# Generated at 2022-06-14 03:34:26.268629
# Unit test for method ap of class Lazy
def test_Lazy_ap():  # pragma: no cover
    def _map(x):
        return x + 1

    def _map2(x):
        return x * 2

    def _map3(x):
        raise RuntimeError('error')

    def _map4(x):
        return Lazy(lambda: _map(x))

    assert Lazy(_map).ap(Lazy(_map2)).get(10) == 22
    assert Lazy(_map).ap(Lazy(_map3)).to_try().is_failure
    assert Lazy(_map).ap(Lazy(_map4)).get(10) == 20
    assert Lazy(_map3).ap(Lazy(_map3)).to_try().is_failure
    assert Lazy(lambda: 10).ap(Lazy(_map)).get() == 11
    assert Lazy(lambda: 10).ap

# Generated at 2022-06-14 03:34:29.958114
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def inc(el):
        return Lazy.of(el + 1)

    assert Lazy.of(1).bind(inc).get() == 2
    assert Lazy.of(1).bind(inc).bind(inc).get() == 3

# Generated at 2022-06-14 03:34:36.280520
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def test_fn(text):
        return Lazy.of(str(text))

    lazy = Lazy.of(123)
    result = lazy.bind(test_fn)
    assert result.get() == '123'

    lazy = Lazy.of(None)
    result = lazy.bind(test_fn)
    assert result.get() is None


# Generated at 2022-06-14 03:34:41.867329
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    """
    Tests ap method for class Lazy.
    """
    def add_one(x: int) -> int:
        """
        Return x + 1
        """
        return x + 1

    lazy_add_one = Lazy.of(add_one)
    lazy_one = Lazy.of(1)

    result = lazy_add_one.ap(lazy_one)
    assert result.get() == 2


# Generated at 2022-06-14 03:34:46.399098
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():  # pragma: no cover
    def func(value):
        return value

    assert Lazy(func) == Lazy(func)
    assert Lazy(func) != Lazy(lambda x: x)



# Generated at 2022-06-14 03:34:52.901816
# Unit test for method get of class Lazy
def test_Lazy_get():  # pragma: no cover
    assert Lazy(lambda x: x).get(1) == 1
    assert Lazy(lambda x, y: x + y).get(1, 2) == 3

    lazy = Lazy(lambda x: x)
    assert lazy.get(1) == 1
    assert lazy.get(1) == 1


# Generated at 2022-06-14 03:34:58.591737
# Unit test for method get of class Lazy
def test_Lazy_get():
    def func(a: int, b: int) -> int:
        return a + b

    lazy = Lazy(func)
    assert lazy.get(2, 3) == 5
    assert lazy.get(1, 1) == 2
    assert lazy.get(2, 3) == 5


# Generated at 2022-06-14 03:35:02.997270
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def setup_fn(x):
        return Lazy.of(x + 1)

    lazy_result = Lazy(lambda: 1).bind(setup_fn)
    assert lazy_result == Lazy.of(2)


# Generated at 2022-06-14 03:35:09.360355
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def fn_lazy_of_some(x: bool) -> Lazy[bool, bool]:
        def fn_lazy_of_true(y: bool) -> Lazy[bool, bool]:
            return Lazy.of(True)

        return Lazy.of(x).bind(fn_lazy_of_true)

    assert Lazy.of(True).bind(fn_lazy_of_some) == Lazy(lambda *args: True)

    assert Lazy.of(False).bind(fn_lazy_of_some) == Lazy(lambda *args: False)



# Generated at 2022-06-14 03:35:18.706408
# Unit test for method bind of class Lazy
def test_Lazy_bind():  # pragma: no cover
    def f(something):
        return something.upper()

    def mock(arg):
        return Lazy(lambda a: a + (arg,))


    lazy = Lazy(lambda a, b: a + b).bind(mock)
    result = lazy.get(1, 2)
    assert result == (1, 2)

    lazy = Lazy(lambda a: f(a)).bind(Lazy.of)
    assert lazy.get("something") == "SOMETHING"

    lazy = Lazy(lambda a: a + 1)
    assert lazy.get(5) == 6



# Generated at 2022-06-14 03:35:21.020360
# Unit test for method get of class Lazy
def test_Lazy_get():
    assert Lazy(lambda: 1).get() == 1



# Generated at 2022-06-14 03:35:31.838509
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.box import Box
    from pymonet.maybe import Maybe

    f = lambda x: x + 2
    v = Lazy.of(2)
    g = Lazy.of(f)
    h = Lazy.of(3)
    b = Lazy.of(Box(3))

    assert(Lazy.of(5)) == v.ap(g)
    assert(g.ap(v) == Lazy.of(f(2)))
    assert(v.ap(h) == Lazy.of(2))
    assert(v.ap(b) == Lazy.of(Box(2)))
    assert(Lazy.of(Maybe(3))) == v.ap(Lazy.of(Maybe))

# Generated at 2022-06-14 03:35:39.478898
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    assert Lazy(lambda *args: True) == Lazy(lambda *args: True)
    assert Lazy(lambda *args: True).map(lambda x: x) == Lazy(lambda *args: True).map(lambda x: x)

    assert not Lazy(lambda *args: True) == Lazy(lambda *args: False)
    assert not Lazy(lambda *args: True) == Lazy(lambda *args: None)



# Generated at 2022-06-14 03:35:48.977519
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    import pytest

    # Should ap both Lazy
    result = (Lazy.of(lambda x: x + 1).ap(Lazy.of(2))).get()
    assert result == 3

    # Should return Lazy(lambda x: x + 1)
    result = (Lazy.of(lambda x: x + 1).ap(Lazy.of(lambda x: x))).get(2)
    assert result == 3

    # Should raise TypeError when function in Lazy not takes exactly one argument
    fn = lambda: "any"
    with pytest.raises(TypeError):
        Lazy.of(fn).ap(Lazy.of(1)).get()

# Generated at 2022-06-14 03:36:01.038865
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    """
    test __eq__ method
    """
    # Case: two are equals
    Lazy1 = Lazy(lambda x: x)
    Lazy2 = Lazy(lambda x: x)
    assert Lazy1 == Lazy2
    # Case: first is evaluated, but second is not
    Lazy1._compute_value(1)
    assert Lazy1 != Lazy2
    # Case: all is same, but function is not
    Lazy2.constructor_fn = lambda x: x + 1
    assert Lazy1 != Lazy2
    # Case: all is same, but value is not
    Lazy2.constructor_fn = lambda x: x
    Lazy2._compute_value(1)
    assert Lazy1 != Lazy2



# Generated at 2022-06-14 03:36:09.365643
# Unit test for method bind of class Lazy
def test_Lazy_bind():  # pragma: no cover
    """
    Test of Lazy.bind method
    """
    from pymonet.box import Box

    lazy = Lazy.of(1).bind(lambda x: Box.of(x + 1))
    assert lazy.get() == 2

    lazy = Lazy.of(1).bind(lambda x: Lazy.of(x + 1))
    assert lazy.get() == 2

    lazy = Lazy.of(1).bind(lambda x: x + 1)
    assert lazy.get() == 2


# Generated at 2022-06-14 03:36:13.593622
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    assert Lazy.of(1).ap(Lazy.of(lambda a: a + 2)).get() == 3
    assert Lazy.of(lambda a: a + 2).ap(Lazy.of(3)).get() == 5
    assert Lazy.of(1).ap(Lazy.of(2)).get() == 2


# Generated at 2022-06-14 03:36:21.262992
# Unit test for method bind of class Lazy
def test_Lazy_bind():  # pragma: no cover
    from pymonet import Lazy

    def with_one(value):
        return Lazy.of(value + 1)

    def mult_3(value):
        return Lazy.of(value * 3)

    assert Lazy.of(10).bind(with_one).bind(mult_3).get() == 33
    assert Lazy.of(10).bind(with_one).map(lambda v: v - 5).get() == 6

# Generated at 2022-06-14 03:36:30.955957
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.maybe import Maybe

    def increment(x):
        return x + 1

    def double(x):
        return x * 2

    def triple(x):
        return x * 3

    assert Lazy.of(increment).ap(Maybe.just(1)) == Maybe.just(2)
    assert Lazy.of(double).ap(Maybe.just(1)) == Maybe.just(2)
    assert Lazy.of(triple).ap(Maybe.just(1)) == Maybe.just(3)



# Generated at 2022-06-14 03:36:41.180678
# Unit test for method get of class Lazy
def test_Lazy_get():
    def func_one():
        return 1

    def func_two(a):
        return a + 2

    def func_three(a):
        return a * 3

    assert Lazy.of(1).get() == func_one()
    assert Lazy.of(func_one).map(func_two).map(func_three).get() == func_three(func_two(func_one()))
    assert Lazy.of(func_one).bind(lambda x: Lazy.of(func_two(x))).bind(lambda x: Lazy.of(func_three(x))).get() ==\
        func_three(func_two(func_one()))
    assert Lazy.of(func_one).to_box().get() == func_one()
    assert Lazy.of(func_one).to_

# Generated at 2022-06-14 03:36:47.428312
# Unit test for method bind of class Lazy
def test_Lazy_bind():  # pragma: no cover
    def fn(i):
        return Lazy(lambda: i)

    def fn2(i):
        return i + 10

    assert Lazy.of(5).bind(fn).get() == 5
    assert Lazy.of(5).bind(fn).bind(lambda i: Lazy.of(fn2(i))).get() == 15

# Generated at 2022-06-14 03:36:50.644486
# Unit test for method get of class Lazy
def test_Lazy_get():
    assert Lazy(lambda: 1).get() == 1
    assert Lazy(lambda: 1).get(2, 3) == 1

# Testing of methods



# Generated at 2022-06-14 03:36:54.468813
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    assert Lazy(lambda: 1).bind(lambda x: Lazy.of(x + 1)).get() == 2
    assert Lazy(lambda: 'abc').bind(lambda x: Lazy(lambda: str(x))).get() == 'abc'


# Generated at 2022-06-14 03:37:00.334502
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    lazy_1 = Lazy.of(1)
    lazy_2 = Lazy.of(1)
    lazy_3 = Lazy.of(3)
    lazy_4 = Lazy(lambda x: x + 1)

    assert lazy_1 == lazy_2
    assert lazy_1 != lazy_3
    assert lazy_1 != lazy_4

# Generated at 2022-06-14 03:37:07.597581
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    def test1():
        """
        Returns function that remember that she was called.
        :returns: function that remember that she was called.
        :rtype: Function()
        """
        test1.is_called = True
        return 1

    def test2():
        """
        Returns function that remember that she was called.
        :returns: function that remember that she was called.
        :rtype: Function()
        """
        test2.is_called = True
        return 1

    assert Lazy(test1) == Lazy(test1)
    assert Lazy(test2) == Lazy(test2)
    assert not Lazy(test1) == Lazy(test2)
    assert not Lazy(test1) == 2
    assert not Lazy(test1) == Lazy.of(2)

#

# Generated at 2022-06-14 03:37:13.384123
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def func1(value):
        return Lazy.of(value + 1)

    lazy_lazy = Lazy(lambda: 0).bind(func1)

    assert lazy_lazy.get() == func1(0).get()



# Generated at 2022-06-14 03:37:24.376528
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    def foo():
        return 1

    def bar():
        return 2

    assert Lazy(foo) == Lazy(foo), 'Lazy are equals when both are evaluated, have the same value and constructor functions'
    assert Lazy(foo) != Lazy(bar), 'Lazy are not equals when both are evaluated, have the same value and constructor functions'

    # in python3.7 is_evaluated and value are None when object is created with __init__
    assert Lazy(foo) == Lazy(bar), 'Lazy are equals when both are not evaluated and have the same constructor functions'

    lazy_foo = Lazy(foo)
    lazy_foo._compute_value()
    assert Lazy(foo) == Lazy(foo), 'Lazy are equals when both are evaluated, have the same value and constructor functions'
    assert Lazy(foo)

# Generated at 2022-06-14 03:37:34.776389
# Unit test for method get of class Lazy
def test_Lazy_get():
    from pymonet.monad_try import Try
    from pymonet.maybe import Maybe
    from pymonet.box import Box

    def foo():
        return 'foo'

    def bar(foo):
        return 'bar ' + foo

    def baz(foo):
        return 'baz ' + foo

    def qux(foo):
        return 'qux ' + foo

    test = Lazy(foo).bind(lambda foo: Lazy(bar(foo))).bind(lambda foo: Lazy(baz(foo))).bind(lambda foo: Lazy(qux(foo)))

    # Memoized value
    assert Lazy(foo).get() == Lazy(foo).get()
    assert Lazy(foo).get() == 'foo'

    # Convience method get()

# Generated at 2022-06-14 03:37:40.209368
# Unit test for method get of class Lazy
def test_Lazy_get():
    def func_a() -> int:
        return 1

    def func_b() -> int:
        return 2

    lazy_a = Lazy(func_a)
    lazy_b = Lazy(func_b)

    assert lazy_a.get() == 1
    assert lazy_b.get() == 2


# Generated at 2022-06-14 03:37:43.559810
# Unit test for method get of class Lazy
def test_Lazy_get():
    # given
    value = 'Value'
    lazy = Lazy.of(value)

    # when
    result = lazy.get()

    # then
    assert value == result



# Generated at 2022-06-14 03:37:48.064442
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def f(x):
        return Lazy.of(x + 1)

    def f2(x):
        return Lazy.of(x + 2)

    def f3(x):
        return Lazy.of(x + 3)

    assert Lazy.of(5).bind(f).bind(f2).bind(f3).get() == 11


# Generated at 2022-06-14 03:37:51.017121
# Unit test for method get of class Lazy
def test_Lazy_get():
    called = False

    def fn():
        nonlocal called
        called = True
        return 123

    lazy = Lazy(fn)
    assert lazy.get() == 123
    assert called
    assert lazy.get() == 123
    assert called



# Generated at 2022-06-14 03:38:01.724362
# Unit test for method bind of class Lazy
def test_Lazy_bind():  # pragma: no cover
    def square(x): return x * x

    def add_one(x): return 1 + x

    def add_a_lazy(x):
        return Lazy.of(add_one(x))

    lazy_of_function = Lazy(lambda x: square(x))

    assert lazy_of_function.bind(lambda x: Lazy.of(x)) == Lazy.of(lambda x: square(x))
    assert lazy_of_function.bind(add_a_lazy) == Lazy(lambda x: square(x) + 1)



# Generated at 2022-06-14 03:38:06.379088
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    assert Lazy(lambda *args: None) == Lazy(lambda *args: None)
    assert Lazy(lambda *args: 'test') != Lazy(lambda *args: 'test2')
    assert Lazy(lambda *args: 'test') != None
    assert Lazy(lambda *args: 'test') != 0
    assert Lazy(lambda *args: 'test') != ()
    assert Lazy(lambda *args: 'test') != {}
    assert Lazy(lambda *args: 'test') != ['test']



# Generated at 2022-06-14 03:38:09.920678
# Unit test for method get of class Lazy

# Generated at 2022-06-14 03:38:17.693956
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def fn_lazy(x):
        return Lazy(lambda y: x+y)

    eval_fn = Lazy(lambda: 100).bind(fn_lazy)

    actual_value = eval_fn(1)

    assert actual_value == 101

# Generated at 2022-06-14 03:38:26.985521
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.either import Right
    from pymonet.monad_try import Success

    assert Lazy.of(lambda x: x + 1).bind(lambda x: Lazy.of(lambda y: x(y) + 2)).bind(lambda x: Lazy.of(x(7))) == Lazy.of(10)

    assert Lazy.of(lambda x: Right(x + 1)).bind(lambda x: Lazy.of(x(10))).get().is_right
    assert Lazy.of(lambda x: Success(x + 1)).bind(lambda x: Lazy.of(x(10))).get().is_success


# Generated at 2022-06-14 03:38:32.158833
# Unit test for method bind of class Lazy
def test_Lazy_bind():  # pragma: no cover
    assert Lazy.of(1).bind(lambda x: Lazy.of(x+1)).get() == 2
    assert Lazy.of(1).bind(lambda x: Lazy.of(x+1)).map(lambda y: y+1).get() == 3

# Generated at 2022-06-14 03:38:36.354574
# Unit test for method get of class Lazy
def test_Lazy_get():
    def decorated(x):
        return x + 1

    lazy = Lazy(decorated).map(lambda x: x + 2)

    assert lazy.get(1) == 4
    assert lazy.get(1) == 4



# Generated at 2022-06-14 03:38:38.708103
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    assert Lazy.of(1).bind(lambda v: Lazy.of(v + 1)).get() == 2



# Generated at 2022-06-14 03:38:49.721327
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    # 4 + 5, applied
    val = Lazy.of(4).ap(Lazy.of(5))
    assert val.get() == 9
    assert val == Lazy(lambda: 9)

    # 3 + 2 + 1 += 6, applied
    val = Lazy.of(3).ap(Lazy.of(2)).ap(Lazy.of(1))
    assert val.get() == 6
    assert val == Lazy(lambda: 6)

    # 3 + 2 + 1 += 6, applied in different order
    val = Lazy.of(3).ap(Lazy.of(2))
    val = val.ap(Lazy.of(1))
    assert val.get() == 6
    assert val == Lazy(lambda: 6)

    # 3 + 2 + 1 += 6, applied in different order
    val

# Generated at 2022-06-14 03:39:00.393345
# Unit test for method ap of class Lazy
def test_Lazy_ap():  # pragma: no cover
    from pymonet.monad_try import Try

    def fn1(x):
        return x + 1

    def fn2(x):
        return x / 2

    def fn3(x):
        return x * x

    fn4 = Lazy.of(lambda x: x + 1)

    fn5 = fn4.map(fn3).ap(Lazy.of(3))

    fn5.get()

    # Lazy(fn=<function fn2 at 0x7f1bbc11b400>, value=None, is_evaluated=False)
    # Lazy(fn=<function fn2 at 0x7f1bbc11b400>, value=None, is_evaluated=False)
    # Lazy(fn=<function fn3 at 0x7f1bbc11b

# Generated at 2022-06-14 03:39:04.980249
# Unit test for method get of class Lazy
def test_Lazy_get():
    def add(a):
        return a + 1

    def div(a, b):
        return a / b

    assert Lazy(add).get(1) == add(1)
    assert Lazy(div).get(1, 2) == div(1, 2)
    assert Lazy(div).get(1, 0) == div(1, 0)



# Generated at 2022-06-14 03:39:13.175116
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def set_state(value: int) -> Lazy[int, int]:
        def return_value_plus_1(_: int) -> Lazy[int, int]:
            return Lazy.of(value + 1)

        return Lazy.of(value).bind(return_value_plus_1)

    assert Lazy.of(1).bind(lambda value: Lazy.of(value + 1)).get() == 2
    assert Lazy.of(1).bind(lambda value: Lazy.of(value - 1)).get() == 0
    assert set_state(1).get() == 2
    assert set_state(3).get() == 4


# Generated at 2022-06-14 03:39:17.360313
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.monad_try import Try
    from pymonet.box import Box

    def square(x):
        return Try(lambda: x ** 2)

    result = Lazy(lambda: 3).bind(square)
    assert result.get() == Box(9)

# Generated at 2022-06-14 03:39:41.000950
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def add(x):
        return Lazy(lambda y: x + y)

    def mult(x):
        return Lazy(lambda y: x * y)

    l1 = Lazy(lambda x: x).bind(add(1)).bind(mult(2))
    assert l1.constructor_fn(2) == (2 + 1) * 2

    l2 = Lazy(lambda x: x).bind(add(1)).bind(mult(2)).bind(add(3))
    assert l2.constructor_fn(2) == ((2 + 1) * 2) + 3

    l3 = Lazy(lambda x: x).bind(add(1)).bind(add(3))
    assert l3.constructor_fn(2) == (2 + 1) + 3



# Generated at 2022-06-14 03:39:49.702011
# Unit test for method bind of class Lazy
def test_Lazy_bind():  # pragma: no cover
    def add(a, b):
        return a + b

    assert Lazy.of(2).bind(lambda a: Lazy.of(add(a, 3))).get() == 5
    assert Lazy.of(2).bind(Lazy.of).get() == 2
    assert Lazy.of(2).bind(lambda a: Lazy.of(a)).get() == 2
    assert Lazy.of(2).bind(lambda a: Lazy.of(add(a, 1))).bind(lambda a: Lazy.of(add(a, 3))).get() == 6


# Generated at 2022-06-14 03:39:53.024848
# Unit test for method get of class Lazy
def test_Lazy_get():
    lazy_lst = Lazy(lambda: [1, 2, 3])
    assert lazy_lst.get() == [1, 2, 3]



# Generated at 2022-06-14 03:39:55.878944
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    lazy_magic = Lazy(lambda: 100)
    lazy_plus = lazy_magic.bind(lambda value: Lazy.of(value + 100))
    assert lazy_plus.get() == 200



# Generated at 2022-06-14 03:40:04.639993
# Unit test for method bind of class Lazy
def test_Lazy_bind():  # pragma: no cover
    from pymonet.monad_maybe import Maybe

    def fn(value):
        return Maybe.just(value * 2)

    def fn2(value):
        return Maybe.just(value * 4)

    def fn3(value):
        return Maybe.just(value * 8)

    assert Lazy.of(1).bind(lambda value: Lazy.of(value * 2)).get() == (1 * 2)
    assert Lazy.of(1).bind(lambda value: Lazy.of(value * 2)).bind(lambda value: Lazy.of(value * 4)).get() == 1 * 2 * 4
    assert Lazy.of(1).bind(fn).bind(fn2).bind(fn3).get() == 1 * 2 * 4 * 8

# Generated at 2022-06-14 03:40:09.997016
# Unit test for method get of class Lazy
def test_Lazy_get():
    from pymonet.functor import Functor

    def some_fn1(x: int, y: int) -> int:
        return x + y

    assert Lazy(some_fn1).get(1, 3) == 4
    assert Lazy(some_fn1).get(1, 3) == 4  # check memoize
    assert Lazy(lambda: Functor(1)).get() == 1


# Generated at 2022-06-14 03:40:23.859696
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    assert Lazy.of(1).__eq__(Lazy.of(1))
    assert Lazy.of(1).__eq__(Lazy(lambda: 1))

    assert Lazy.of(1).__eq__(Lazy.of(2)) is False
    assert Lazy.of(1).__eq__(Lazy(lambda: 2)) is False
    assert Lazy.of(1).__eq__(Lazy(lambda: 1).map(lambda x: x + 1)) is False
    assert Lazy.of(1).__eq__(Lazy(lambda: 1).map(lambda x: x + 1)) is False
    assert Lazy.of(1).__eq__(Lazy(lambda: 1).ap(Lazy.of(lambda i: i + 1))) is False
    assert Lazy.of(1).__

# Generated at 2022-06-14 03:40:27.250848
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    lazy = Lazy(lambda x: x+1)
    result = lazy.bind(lambda x: Lazy(lambda y: x+2)).get(1)
    assert result == 4


# Generated at 2022-06-14 03:40:29.270100
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    assert Lazy.of(lambda a: a + 10).ap(Lazy.of(1)) == Lazy.of(11)


# Generated at 2022-06-14 03:40:32.136017
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def get_vector():
        return [1, 2, 3, 4]

    def sum_vector(vector):
        return sum(vector)

    assert Lazy.of(get_vector).bind(sum_vector).get() == 10

# Generated at 2022-06-14 03:40:48.945602
# Unit test for method get of class Lazy
def test_Lazy_get():
    lazy = Lazy(lambda x: x * 2)

    assert lazy.get(5) == 10
    assert lazy.get(5) == 10
    assert lazy.is_evaluated
    assert lazy.value == 10



# Generated at 2022-06-14 03:40:54.598723
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    assert Lazy(lambda x: x + 1).ap(Lazy(lambda y: y / 8)) == Lazy(lambda x: (x + 1) / 8)
    assert Lazy(lambda x, y: x + y).ap(Lazy(lambda y: y / 8)) == Lazy(lambda x, y: (x + y) / 8)


# Generated at 2022-06-14 03:40:57.461590
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    def func_a(): return 1
    def func_b(): return 2

    assert Lazy(func_a) == Lazy(func_a)
    assert Lazy(func_a) != Lazy(func_b)
    assert Lazy(func_a) == Lazy(func_a).get()


# Generated at 2022-06-14 03:41:07.575746
# Unit test for method bind of class Lazy
def test_Lazy_bind():  # pragma: no cover
    from pymonet.monad_try import Try
    from pymonet.validation import Validation

    def f1(a):
        if a == 1:
            return Try.failure(TypeError('a cannot be 1'))
        return Try.success(a + 1)

    def f2(a):
        return Validation.success(a + 2)

    assert Lazy.of(2).bind(f1).get() == 3
    assert Lazy.of(1).bind(f1).get() == 1
    assert Lazy.of(2).bind(f1).bind(f2).get() == 5
    assert Lazy.of(1).bind(f1).bind(f2).get() == 1

# Generated at 2022-06-14 03:41:17.727060
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    assert Lazy.of('a') == Lazy.of('a')
    assert Lazy.of('a') != Lazy.of('b')
    assert Lazy.of('a') != Lazy(lambda: 'a')
    assert Lazy(lambda: 'a') != Lazy(lambda: 'a')
    assert Lazy(lambda: 'a') == Lazy(lambda: 'a')
    assert Lazy(lambda: 'a')._compute_value() == 'a'
    assert Lazy(lambda: 'a') == Lazy(lambda: Lazy(lambda: 'a')._compute_value())



# Generated at 2022-06-14 03:41:22.257387
# Unit test for method map of class Lazy
def test_Lazy_map():
    def add(x):
        return x + 1

    def double(x):
        return x * 2

    def foo(x):
        return x

    assert Lazy(foo).map(add).map(double).get() == 4



# Generated at 2022-06-14 03:41:30.529205
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    assert Lazy(lambda: 2).ap(Lazy.of(lambda x: x * x)) == Lazy(lambda: 4)
    assert Lazy(lambda: 2).ap(Lazy(lambda: lambda x: x * x)) == Lazy(lambda: 4)
    assert Lazy(lambda: 2).ap(Lazy(lambda: lambda x: x * x).map(lambda x: lambda y: x(y))) == Lazy(lambda: 4)
