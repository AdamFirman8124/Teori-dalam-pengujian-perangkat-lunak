

# Generated at 2022-06-14 03:31:32.032086
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    """
    Test for Lazy.__eq__
    """
    def fn(x):
        return x

    assert Lazy(fn) == Lazy(fn)
    assert Lazy(fn) != Lazy(lambda x: x + 1)
    assert Lazy(fn) != 1
    assert Lazy(fn) != fn



# Generated at 2022-06-14 03:31:36.540903
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    import pytest

    def add_one(x):
        return Lazy.of(x + 1)

    lazy_add_one = Lazy(add_one)

    assert lazy_add_one.bind(add_one).bind(add_one).get(2) == 4

# Generated at 2022-06-14 03:31:45.790299
# Unit test for method get of class Lazy
def test_Lazy_get():
    def _f(a):
        return a

    # test for not evaluated Lazy
    assert Lazy(_f).get(2) == 2

    # test for evaluated Lazy
    lazy = Lazy(_f)
    lazy.get(2)
    assert lazy.value == 2

    # test for Lazy which should run only once no matter how many times called get
    def _f(a):
        return a

    lazy = Lazy(_f)
    lazy.get(2)
    assert lazy.value == 2


# Generated at 2022-06-14 03:31:51.909797
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():

    def plus(digit: int) -> Lazy[int, int]:
        return Lazy(lambda arg: arg + digit)

    lazy = Lazy.of(5)
    assert Lazy.of(5) == lazy
    assert Lazy.of(5) == Lazy.of(5)
    lazy = lazy.bind(plus(5))
    assert lazy == lazy.bind(plus(5))
    assert lazy != Lazy.of(5)
    assert Lazy.of(5) != lazy



# Generated at 2022-06-14 03:31:57.252830
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    """
    It's just a simple code to check how bind method of Lazy works.

    It's not a unit test
    """  # pragma: no cover
    def increment(value):
        return value + 1

    def square(value):
        return value * value

    lazy = Lazy(lambda: 1)

    lazy_sqrt = lazy.bind(lambda x: Lazy.of(increment(x)).map(square))

    assert lazy_sqrt.get() == 4

# Generated at 2022-06-14 03:32:02.101688
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    test1 = lambda x: x + 1
    test2 = lambda x: x + 1

    lazy1 = Lazy(test1)
    lazy2 = Lazy(test2)

    assert lazy1 == lazy2
    assert lazy1 == Lazy(test1)
    assert Lazy(test1) == lazy1


# Generated at 2022-06-14 03:32:11.894419
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():  # pragma: no cover
    def _add5(a):
        return a + 5

    assert Lazy(_add5).map(lambda a: a + 1) == Lazy(_add5).map(lambda a: a + 1)
    assert not Lazy(_add5).map(lambda a: a + 1) == Lazy(_add5).map(lambda a: a + 2)
    assert not Lazy(_add5).map(lambda a: a + 1) == Lazy(_add5)
    assert Lazy(_add5) == Lazy(_add5)

# Generated at 2022-06-14 03:32:16.858353
# Unit test for method get of class Lazy
def test_Lazy_get():
    counter = 0
    def fn():
        nonlocal counter
        counter += 1
        return 1

    lazy = Lazy(fn)
    counter = 0
    assert lazy.get() == 1
    assert counter == 1
    assert lazy.get() == 1
    assert counter == 1


# Generated at 2022-06-14 03:32:26.362790
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    """
    Unit test for method bind of class Lazy
    """
    def _return(value: T) -> Lazy[T, T]:
        return Lazy.of(value)

    def _zero(value: T) -> Lazy[T, T]:
        return Lazy(lambda: 0)

    # Create new Lazy with function returning 1
    one = Lazy(lambda: 1)

    # fold function and return result
    assert one.bind(_return) == 1

    # takes value and returns 0
    assert one.bind(_zero) == 0

# Generated at 2022-06-14 03:32:29.917717
# Unit test for method get of class Lazy
def test_Lazy_get():
    def test_mapper(a):
        return a + 1

    def constructor_fn(a):
        return a

    lazy_instance = Lazy(constructor_fn)
    assert lazy_instance.get(1) == 1
    assert lazy_instance.is_evaluated



# Generated at 2022-06-14 03:32:44.350391
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():

    assert Lazy.of(3).__eq__(Lazy.of(3))
    assert not Lazy.of(3).__eq__(Lazy.of(2))

    assert Lazy.of(3).map(lambda x: x + 5).__eq__(Lazy.of(3).map(lambda x: x + 5))
    assert not Lazy.of(3).map(lambda x: x + 5).__eq__(Lazy.of(3).map(lambda x: x + 4))

    assert not Lazy.of(3).__eq__(Lazy.of(3).map(lambda x: x + 5))
    assert not Lazy.of(3).__eq__(Lazy.of(4))

# Generated at 2022-06-14 03:32:50.908278
# Unit test for method map of class Lazy
def test_Lazy_map():
    from pymonet.box import Box

    def id(x):
        return x

    assert Lazy(lambda: 1).map(id).get() == Box(1).map(lambda x: Box(id(x))).get()
    assert Lazy(lambda: 1).map(lambda y: y * y).get() == Box(1).map(lambda x: Box(x * x)).get()


# Generated at 2022-06-14 03:32:52.618513
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    assert Lazy(lambda n: n).ap(Lazy(lambda n: n + 1)).map(lambda n: n * 2) == Lazy(lambda n: n).ap(Lazy(lambda n: n + 1)).map(lambda n: n * 2)



# Generated at 2022-06-14 03:32:57.725389
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    lazy_evaluator = Lazy(lambda x: x ** 2)
    lazy_evaluator_2 = Lazy(lambda x: x ** 3)

    assert lazy_evaluator.bind(lambda x: lazy_evaluator_2) == Lazy(lambda x: lazy_evaluator_2.constructor_fn(x**2))



# Generated at 2022-06-14 03:33:04.258768
# Unit test for method get of class Lazy
def test_Lazy_get():
    assert Lazy.of(2).get() == 2
    assert Lazy.of(3).get(1) == 3
    assert Lazy.of(4).get(1, 2) == 4
    assert Lazy.of(5).get(1, 2, 3) == 5
    assert Lazy.of(6).get(1, 2, 3, 4) == 6
    assert Lazy.of(7).get(1, 2, 3, 4, 5) == 7
    assert Lazy.of(8).get(1, 2, 3, 4, 5, 6) == 8
    assert Lazy.of(9).get(1, 2, 3, 4, 5, 6, 7) == 9
    assert Lazy.of(10).get(1, 2, 3, 4, 5, 6, 7, 8) == 10
   

# Generated at 2022-06-14 03:33:11.148931
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def f(x):
        return Lazy.of(x + 1)

    def g(x):
        return Lazy.of(x + 2)

    def h(x):
        return Lazy.of(x + 3)

    result = (Lazy.of(1)
              .bind(f)
              .bind(g)
              .bind(h))
    assert result.get() == 7



# Generated at 2022-06-14 03:33:15.258729
# Unit test for method get of class Lazy
def test_Lazy_get():
    def foo() -> int:
        return 5 + 10

    lazy = Lazy(foo)
    assert lazy.get() == 15

    lazy = Lazy(func=lambda: 5 + 10)
    assert lazy.get() == 15



# Generated at 2022-06-14 03:33:22.067363
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():  # pylint: disable=invalid-name
    assert Lazy(lambda: None).__eq__(Lazy(lambda: None)) is True
    assert Lazy(lambda: None).__eq__(Lazy(lambda x: None)) is False
    assert Lazy(lambda x: None).__eq__(Lazy(lambda: None)) is False
    assert Lazy(lambda x: x).__eq__(Lazy(lambda x: None)) is False
    assert Lazy(lambda x: None).__eq__(Lazy(lambda x: x)) is False



# Generated at 2022-06-14 03:33:27.986400
# Unit test for method map of class Lazy
def test_Lazy_map():
    """
    Unit test for method map of class Lazy
    """
    def add(x: int, y: int) -> int:
        """
        :param x: int
        :param y: int
        :returns: sum of arguments
        :rtype: int
        """
        return x + y

    assert Lazy(add).map(add).map(add).get(2, 3) == Lazy(add).map(lambda x: add(add(x), add(x))).get(2, 3)
    assert Lazy(add).map(add).map(add).get(3, 3) == Lazy(add).map(lambda x: add(add(x), add(x))).get(3, 3)
    assert Lazy(add).map(add).map(add).get(10, 10) == Lazy

# Generated at 2022-06-14 03:33:34.871180
# Unit test for method get of class Lazy
def test_Lazy_get():
    assert Lazy(lambda: 100).get() == 100
    assert Lazy(lambda: 13).get() == 13
    assert Lazy(lambda: 2).get() == 2
    assert Lazy(lambda: '').get() == ''
    assert Lazy(lambda: 'test').get() == 'test'
    assert Lazy(lambda: True).get() == True


# Generated at 2022-06-14 03:33:44.596879
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.utils import curry
    from pymonet.box import Box

    def result(*args):
        return args[0]

    fn = curry(result).partial(Box(6)).partial(Box(4))

    assert Lazy.of(fn).bind(lambda f: f()).get() == Box(4)
    assert Lazy.of(fn).bind(lambda f: Lazy(lambda: f())).get() == Box(4)



# Generated at 2022-06-14 03:33:46.331716
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    assert Lazy(lambda x: x+1).ap(Lazy.of(1)) == Lazy.of(2)

# Generated at 2022-06-14 03:33:49.140983
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    assert Lazy.of("value").bind(lambda value: Lazy.of("value" + " 2")).get() == "value 2"


# Generated at 2022-06-14 03:33:51.992555
# Unit test for method get of class Lazy
def test_Lazy_get():
    # given
    lazy = Lazy(lambda *args: 1)

    # then
    assert lazy.get() == 1
    assert lazy.get(None, None) == 1


# Generated at 2022-06-14 03:34:01.025740
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    def add(a):
        def fn(b):
            return a + b
        return fn

    def my_fn(a):
        return a ** 2

    add_x_fn = Lazy.of(5).ap(Lazy.of(add))
    assert add_x_fn.get()(10) == 15

    my_fn_x_add = Lazy.of(my_fn).ap(Lazy.of(add))
    assert my_fn_x_add.get()(10) == 100


# Generated at 2022-06-14 03:34:06.020384
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    lazy = Lazy(lambda: 2)
    lazy_fn = Lazy(lambda x: x + 2)

    assert lazy.ap(lazy_fn).get() == 4  # test success
    assert lazy.ap(Lazy.of(None)).get() == 2  # test empty

# Generated at 2022-06-14 03:34:16.676109
# Unit test for method get of class Lazy
def test_Lazy_get():
    assert Lazy.of(5).get() == 5

    assert Lazy(lambda: 5).get() == 5
    assert Lazy(lambda: 'aaa').get() == 'aaa'
    assert Lazy(lambda: 2 ** 10).get() == 1024
    assert Lazy(lambda: 2 ** 10).map(lambda x: x / 2).get() == 512

    assert Lazy.of(5).get(1, 2, 3, 4, 5) == 5
    assert Lazy(lambda a: a).get(1) == 1
    assert Lazy(lambda a, b: a + b).get(1, 2) == 3
    assert Lazy(lambda a, b, c, d, e: a + b + c + d + e).get(1, 2, 3, 4, 5) == 15

    # test memoization
    counter

# Generated at 2022-06-14 03:34:19.146728
# Unit test for method get of class Lazy
def test_Lazy_get():
    def fn():
        return 1

    lazy = Lazy(fn)
    assert lazy.get() == 1
    assert lazy.is_evaluated is True



# Generated at 2022-06-14 03:34:29.907362
# Unit test for method map of class Lazy
def test_Lazy_map():  # pragma: no cover
    from pymonet.functor import Functor
    from pymonet.utils import BaseTestCase

    class TestMapperFunctor(Functor):
        __test__ = False

        def map(self, mapper):
            return Lazy.of(mapper(self.value))

    class LazyMapTests(BaseTestCase):

        def test_should_map(self):
            a = Lazy.of(1).map(lambda x: x + 1)
            b = Lazy.of(2)
            self.assertEqual(a, b)

        def test_should_map_for_functor(self):
            a = TestMapperFunctor(1).fmap(lambda x: x + 1)
            b = Lazy.of(2)

# Generated at 2022-06-14 03:34:38.029779
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    lazy_1 = Lazy(lambda: 1)
    lazy_2 = Lazy(lambda: 2)
    lazy_3 = Lazy(lambda: 3)
    lazy_4 = Lazy(lambda: 4)
    lazy_5 = Lazy(lambda: 5)

    def compute_lazy(x):
        def add(y):
            return Lazy(lambda: x + y)
        return lazy_1.bind(add)

    assert lazy_5.get() == compute_lazy(lazy_2.get()).get()

# Generated at 2022-06-14 03:34:47.830008
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    lazy_value = Lazy.of(5)
    lazy_fn = Lazy.of(lambda x: x + 2)
    assert lazy_value.ap(lazy_fn).get() == 7


# Generated at 2022-06-14 03:34:49.876726
# Unit test for method get of class Lazy
def test_Lazy_get():
    lazy = Lazy(lambda x: x * 2)
    assert lazy.get(2) == 4



# Generated at 2022-06-14 03:34:54.480045
# Unit test for method bind of class Lazy
def test_Lazy_bind():  # pragma: no cover
    def get_lazy_data(x):
        def compute_data(number):
            return number + 10

        return Lazy.of(x).map(compute_data)

    assert get_lazy_data(5).bind(get_lazy_data) == Lazy.of(25)


# Generated at 2022-06-14 03:35:01.642466
# Unit test for method map of class Lazy
def test_Lazy_map():
    def add_1(x): return x + 1
    def mul_2(x): return x * 2
    def pow_3(x): return x ** 3

    lazy_add_3 = Lazy.of(3).map(add_1).map(mul_2).map(pow_3)

    assert lazy_add_3.get() == 216



# Generated at 2022-06-14 03:35:09.939455
# Unit test for method map of class Lazy
def test_Lazy_map():
    """
    Test map method of class Lazy.
    """
    assert Lazy(lambda: 1).map(lambda x: x + 2).get() == 3
    assert Lazy(lambda: 1).map(lambda x: x + 2).to_box().get() == 3
    assert Lazy(lambda: 1).map(lambda x: x + 2).to_either().get().get_right() == 3
    assert Lazy(lambda: 1).map(lambda x: x + 2).to_maybe().get().get() == 3
    assert Lazy(lambda: 1).map(lambda x: x + 2).to_try().get().get_right() == 3
    assert Lazy(lambda: 1).map(lambda x: x + 2).to_validation().get().get_right() == 3


# Generated at 2022-06-14 03:35:15.012298
# Unit test for method map of class Lazy
def test_Lazy_map():
    def fn(x):
        return x

    def mapper(x):
        return x + 1

    l = Lazy(fn)

    assert l.map(mapper) == Lazy(lambda: fn(0) + 1)


# Unit tests for method ap of class Lazy

# Generated at 2022-06-14 03:35:21.084025
# Unit test for method get of class Lazy
def test_Lazy_get():
    counter = 0

    def counter_fn(*args):
        nonlocal counter
        counter += 1

        return counter

    lazy = Lazy(counter_fn)
    assert lazy.get() == 1
    assert lazy.get() == 1
    assert lazy.get() == 1
    assert lazy.get() == 1
    assert lazy.get() == 1
    assert lazy.get() == 1


# Generated at 2022-06-14 03:35:26.110232
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def add(a: int, b: int, c: int) -> int:
        return a + b + c

    lazy = Lazy.of(add).bind(lambda fn: Lazy.of(fn(1, 2, 3)))
    assert lazy.get() == add(1, 2, 3)
    assert lazy.get() == add(1, 2, 3)



# Generated at 2022-06-14 03:35:29.541650
# Unit test for method get of class Lazy
def test_Lazy_get():
    assert Lazy.of(42).get() == 42
    assert Lazy.of(42).get(1) == 42
    assert Lazy.of(42).get(1, 2) == 42


# Generated at 2022-06-14 03:35:35.112107
# Unit test for method get of class Lazy
def test_Lazy_get():
    def test_Lazy_with_empty_method(*args):  # pylint: disable=unused-argument
        return 'value'

    assert Lazy.of('value').get() == 'value'
    assert Lazy(test_Lazy_with_empty_method).get() == 'value'
    assert Lazy(test_Lazy_with_empty_method).get(1, 2, 3) == 'value'



# Generated at 2022-06-14 03:35:49.238281
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.monad_list import List
    from pymonet.monad_tuple import Tuple

    def f(x):
        return Tuple(x, 'a')

    def g(x):
        return List(x, 'a')

    lazy = Lazy.of(1)
    assert lazy.bind(f).constructor_fn(None) == f(1)
    assert lazy.bind(f).bind(g).constructor_fn(None) == f(1).bind(g)
    assert lazy.bind(f).bind(g).constructor_fn(None) == g(1)

# Generated at 2022-06-14 03:35:57.262728
# Unit test for method get of class Lazy
def test_Lazy_get():
    def constructor_fn(arg):
        return arg

    def mapper(value):
        return value + 10

    def mapper2(value):
        return value * 10

    def sum_values(value):
        return value + 10

    lazy = Lazy(constructor_fn)
    assert lazy.get(10) == 10
    assert lazy.get(10) == 10
    assert lazy.is_evaluated

    lazy2 = Lazy(constructor_fn)
    assert lazy2.get(100) == 100

    mapper_lazy = lazy.map(mapper)
    assert mapper_lazy.get(10) == 20
    assert mapper_lazy.get(10) == 20
    assert mapper_lazy.is_evaluated


# Generated at 2022-06-14 03:36:04.773945
# Unit test for method get of class Lazy
def test_Lazy_get():
    lazy = Lazy.of(1)
    assert lazy.get() == 1

    lazy = Lazy(lambda: 2)
    assert lazy.get() == 2

    lazy = Lazy(lambda x: x + 1)
    assert lazy.get(1) == 2

    lazy = Lazy(lambda x, y: x + y)
    assert lazy.get(1, 2) == 3



# Generated at 2022-06-14 03:36:06.913059
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    fn = Lazy(lambda x: x + 1)
    value = Lazy(lambda: 1)

    assert fn.ap(value).get() == 2

# Generated at 2022-06-14 03:36:15.822642
# Unit test for method map of class Lazy
def test_Lazy_map():
    def double(x):
        return x * 2

    def add3(x):
        return x + 3

    def add1(x):
        return x + 1

    def single(x):
        return x

    def add2(x):
        return x + 2

    lazy_starting = Lazy.of(10)

    # map
    assert Lazy.of(10).map(double).get() == 20
    assert Lazy.of(10).map(double).map(add3).get() == 23
    assert Lazy.of(10).map(double).map(add3).map(add1).get() == 24
    assert Lazy.of(10).map(double).map(add3).map(add1).map(single).get() == 24

    # compose

# Generated at 2022-06-14 03:36:20.439596
# Unit test for method get of class Lazy
def test_Lazy_get():
    def func(*args):
        return "This is value"

    lazy = Lazy(func)
    assert lazy.get() == "This is value"
    assert lazy.get() == "This is value"
    assert lazy.get() == "This is value"


# Generated at 2022-06-14 03:36:26.691106
# Unit test for method map of class Lazy
def test_Lazy_map():  # pragma: no cover
    def fn(input_value):
        return input_value

    def mapper(input_value):
        return input_value + '_mapped'

    lazy = Lazy(fn)
    mapped = lazy.map(mapper)

    assert mapped.get('value') == 'value_mapped'



# Generated at 2022-06-14 03:36:28.432415
# Unit test for method map of class Lazy
def test_Lazy_map():
    """
    >>> assert Lazy.of(1).map(lambda x: x + 2) == Lazy(lambda x: 3)
    """


# Generated at 2022-06-14 03:36:30.140548
# Unit test for method get of class Lazy
def test_Lazy_get():
    assert Lazy.of(1).get() == 1



# Generated at 2022-06-14 03:36:39.400878
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():  # pragma: no cover
    def fn(*args):
        return args

    lazy_1 = Lazy(fn)
    lazy_2 = Lazy(fn)

    assert lazy_1 == lazy_2

    lazy_1._compute_value(1)
    assert lazy_1 == lazy_2

    lazy_2._compute_value(1)
    assert lazy_1 == lazy_2

    lazy_1._compute_value(2)
    assert lazy_1 != lazy_2

    lazy_1._compute_value(1)
    lazy_2 = Lazy(lambda: 2)
    assert lazy_1 != lazy_2


# Generated at 2022-06-14 03:36:54.146065
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    def ap_test(a, b, c):
        assert a + b == c

    lazy_func = Lazy.of(lambda a: lambda b: a + b)
    lazy_func.ap(Lazy.of(1)).ap(Lazy.of(2)).map(lambda c: Lazy.of(ap_test(1, 2, c))).get()
    lazy_func.ap(Lazy.of(1)).ap(Lazy.of(3)).map(lambda c: Lazy.of(ap_test(1, 3, c))).get()


# Generated at 2022-06-14 03:37:04.553211
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def first_fn(A):
        return A + 1

    def second_fn(A):
        return A + 2

    def third_fn(A):
        return A + 3

    lazy_one = Lazy.of(1)
    lazy_two = lazy_one.bind(lambda A: Lazy.of(first_fn(A)))
    assert lazy_two.get() == 2

    lazy_three = lazy_two.bind(lambda A: Lazy.of(second_fn(A)))
    assert lazy_three.get() == 4

    lazy_four = lazy_three.bind(lambda A: Lazy.of(third_fn(A)))
    assert lazy_four.get() == 7


# Generated at 2022-06-14 03:37:12.379304
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.box import Box
    from pymonet.maybe import Maybe
    from pymonet.validation import Validation

    assert Lazy.of(lambda x: x + 1).ap(Box(4)) == Lazy.of(5)
    assert Lazy.of(lambda x: x + 1).ap(Maybe.just(4)) == Lazy.of(5)
    assert Lazy.of(lambda x: x + 1).ap(Validation.success(4))._compute_value() == Lazy.of(5)._compute_value()


# Generated at 2022-06-14 03:37:14.245182
# Unit test for method get of class Lazy
def test_Lazy_get():
    def fn(x):
        return x

    assert Lazy(fn).get(42) == 42



# Generated at 2022-06-14 03:37:18.004756
# Unit test for method get of class Lazy
def test_Lazy_get():
    """Test for method get of class Lazy."""
    from pymonet.validation import Validation

    test_arg = 1

    def test_function(arg):
        return arg * 2

    lazy_validation = Lazy(test_function).to_validation(test_arg)

    assert lazy_validation.get() == test_arg * 2


# Generated at 2022-06-14 03:37:23.870257
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.maybe import Maybe

    def fn(x):
        return Maybe.just(lambda y: y + x)

    def identity(x):
        return x

    assert Lazy.of(1).ap(Lazy.of(identity)).get() == 1

    assert Lazy.of(1).ap(Lazy.of(fn).ap(Lazy.of(1))).get() == 2

# Generated at 2022-06-14 03:37:26.742095
# Unit test for method get of class Lazy
def test_Lazy_get():
    def return_str():
        return 'Test str'

    lazy = Lazy(return_str)
    assert lazy.get() == 'Test str'
    assert lazy.is_evaluated is True


# Generated at 2022-06-14 03:37:30.768962
# Unit test for method ap of class Lazy
def test_Lazy_ap(): # pragma: no cover
    """
    >>> Lazy.of(lambda x: x + 1).ap(Lazy.of(1))
    Lazy[fn=<function test_Lazy_ap.<locals>.<lambda> at 0x7f072c454bf8>, value=2, is_evaluated=True]
    >>> Lazy.of(lambda x: x + 1).ap(Lazy.of(1)).value
    2
    >>> Lazy.of(lambda x: x + 1).ap(Lazy.of(1)).get()
    2
    """
    pass


# Generated at 2022-06-14 03:37:37.150443
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    a = Lazy(lambda: 1)
    assert a != 1
    assert a == Lazy(lambda: 1)

    assert Lazy(lambda: 1).map(lambda x: x + 1) != Lazy(lambda: 1)
    assert Lazy(lambda: 1).map(lambda x: x + 1) != Lazy(lambda: 2)
    assert Lazy(lambda: 1).map(lambda x: x + 1) == Lazy(lambda: 1).map(lambda x: x + 1)


# Generated at 2022-06-14 03:37:39.213706
# Unit test for method map of class Lazy
def test_Lazy_map():
    assert Lazy.of(1).map(lambda x: x + 1).get() == 2



# Generated at 2022-06-14 03:37:53.254935
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    get_mock_value = lambda x: Lazy(lambda: x)

    class MockException(Exception):
        pass

    try_1 = Lazy(lambda: 2).bind(get_mock_value)
    try_2 = Lazy(lambda: 2).bind(lambda x: Lazy(lambda: x).bind(get_mock_value))
    try_3 = Lazy(lambda: 2).bind(lambda x: Lazy(lambda: x).bind(lambda y: Lazy(lambda: y).bind(get_mock_value)))
    try_4 = Lazy(lambda: 2).bind(lambda x: Lazy(lambda: x).bind(lambda y: Lazy(lambda: y).bind(lambda z: Lazy(lambda: z).bind(get_mock_value))))

# Generated at 2022-06-14 03:37:58.765983
# Unit test for method get of class Lazy
def test_Lazy_get():
    test_Lazy = Lazy.of('abc')
    assert test_Lazy.get(1, 2, 3) == 'abc'
    assert test_Lazy.is_evaluated
    assert test_Lazy.get(1, 2, 3) == 'abc'



# Generated at 2022-06-14 03:38:06.528171
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.monad_try import Try

    def divide(value):
        """
        Divide value by 2

        :param value: value to divide by 2
        :type value: number
        :returns: successfully division result
        :rtype: number | MonadTry[Error]
        """
        return Try(lambda: value / 2)

    computed_value = Lazy.of(100)
    computed_value = computed_value.bind(divide)

    assert computed_value.get() == 50

    def divide_by_zero(value):
        """
        Divide value by 0

        :param value: value to divide by 0
        :type value: int
        :returns: division result
        :rtype: number | MonadTry[Error]
        """
        return Try(lambda: value / 0)

    computed

# Generated at 2022-06-14 03:38:09.428201
# Unit test for method get of class Lazy
def test_Lazy_get():  # pragma: no cover
    from nose.tools import assert_equals

    lazy = Lazy(lambda: 'aaa')
    assert_equals('aaa', lazy.get())
    assert_equals('aaa', lazy.get())


# Generated at 2022-06-14 03:38:12.365334
# Unit test for method get of class Lazy
def test_Lazy_get():
    """
    Call constructor function of Lazy and return it's value.
    """
    called = False

    def fn(arg):
        nonlocal called
        called = True
        return arg

    assert Lazy(fn).get('test') == 'test'
    assert called is True

# Generated at 2022-06-14 03:38:24.277619
# Unit test for method bind of class Lazy
def test_Lazy_bind():  # pragma: no cover
    from pymonet.maybe import Maybe
    from pymonet.monad_try import Try

    assert str(Lazy(lambda: Maybe.of(5)).bind(lambda x: Lazy(lambda: Maybe.just(x + 5)))) == 'Lazy[fn=<function test_Lazy_bind.<locals>.<lambda>.lambda_fn at 0x7f3f3d5e5ae8>, value=None, is_evaluated=False]'

# Generated at 2022-06-14 03:38:36.869568
# Unit test for method get of class Lazy
def test_Lazy_get():
    from pymonet.box import Box
    from pymonet.either import Right
    from pymonet.maybe import Maybe
    from pymonet.monad_try import Try
    from pymonet.validation import Validation

    def add_and_multiply_by_2(x):
        return 2 * x + 2

    def throw_error_on_2(x: int) -> int:
        if x == 2:
            raise ValueError("x has wrong value")
        return x

    def error_can_not_be_0(x: int) -> Validation[int, str]:
        if x == 0:
            return Validation.fail('Error')
        return Validation.success(x)

    # Test for function
    f_lazy = Lazy(add_and_multiply_by_2)

# Generated at 2022-06-14 03:38:40.285871
# Unit test for method ap of class Lazy
def test_Lazy_ap():  # pragma: no cover
    def sum(x):
        return x + 10

    a = Lazy.of(1)
    b = Lazy.of(sum)

    assert a.ap(b) == Lazy.of(11)

# Generated at 2022-06-14 03:38:43.183245
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    def add(x: int, y: int) -> int:
        return x + y

    assert Lazy.of(add).ap(Lazy.of(1)).ap(Lazy.of(2)) == Lazy.of(3)



# Generated at 2022-06-14 03:38:45.557048
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def fn(value):
        def lambda_fn(*args):
            return value

        return Lazy(lambda_fn)

    lazy = Lazy(lambda: 1)
    assert lazy.bind(fn) == fn(1)

# Generated at 2022-06-14 03:39:01.062551
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    def value_mapper(a: int, b: str) -> str:
        return f'{a}{b}'

    def lazy_mapper(a: int) -> Lazy[int, str]:
        return Lazy.of(str(a))

    value_lazy = Lazy.of(value_mapper)
    lazy_lazy = Lazy.of(lazy_mapper)

    assert value_lazy.ap(lazy_lazy).get(2) == '2'

    def lazy_mapper_empty(a: int) -> Lazy[int, str]:
        return Lazy.of(None)

    value_lazy_empty = Lazy.of(value_mapper)
    lazy_lazy_empty = Lazy.of(lazy_mapper_empty)

    assert value_l

# Generated at 2022-06-14 03:39:04.896336
# Unit test for method map of class Lazy
def test_Lazy_map():
    def identity(x):
        return x
    v = Lazy.of('The value I want to pass to the function')
    assert v.map(identity) == Lazy(identity)

    assert v.map(identity).get() == 'The value I want to pass to the function'



# Generated at 2022-06-14 03:39:10.957533
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    # Given
    def double(value):
        return value * 2

    lazy_double = Lazy(double)

    def add(a, b):
        return a + b

    lazy_add = Lazy(add)

    # When
    result = lazy_double.ap(lazy_add)

    # Then
    assert result.get(1, 2) == 6

# Generated at 2022-06-14 03:39:13.164202
# Unit test for method map of class Lazy
def test_Lazy_map():
    assert Lazy.of(1).map(lambda x: x * 2).get() == 2



# Generated at 2022-06-14 03:39:17.354922
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def print_value(x):
        print('Bind: {}'.format(x))
        return Lazy.of(x)

    lazy = Lazy(lambda: 'Test')
    lazy = lazy.bind(print_value)
    assert lazy.get() == 'Test'

# Generated at 2022-06-14 03:39:26.106067
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():  # pragma: no cover
    """
    Unit test for method __eq__ of class Lazy
    """
    assert Lazy.of(2) == Lazy.of(2)
    assert Lazy.of(2) != Lazy.of(3)

    assert Lazy(lambda: 2) != Lazy.of(2)
    assert (
        Lazy(lambda: 2) !=
        Lazy(lambda: 3)
    )
    assert Lazy(lambda: 2) != Lazy(lambda: 2)


# Generated at 2022-06-14 03:39:32.838120
# Unit test for method get of class Lazy
def test_Lazy_get():
    """
    Unit test for method get of class Lazy
    """
    from pymonet.box import Box
    from pymonet.either import Right
    from pymonet.maybe import Maybe
    from pymonet.monad_try import Try

    function = lambda x: 1 if x else 0
    lazy = Lazy(function)
    assert lazy.get(False) == 0  # Should be not evaluated and false
    assert lazy.is_evaluated is False  # Should be not evaluated and false
    assert lazy.get(False) == 0  # Should be evaluated and false
    assert lazy.is_evaluated is True  # Should be evaluated and false
    assert lazy.get(1) == 1  # Should be evaluated and false
    assert lazy.is_evaluated is True  # Should be evaluated and false

# Generated at 2022-06-14 03:39:45.025374
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.box import Box
    from pymonet.maybe import Maybe

    add_one = lambda x: x + 1
    mul_by_3 = lambda x: x * 3

    right_box = Box(add_one).map(mul_by_3)
    right_maybe = Maybe(add_one).map(mul_by_3)
    left_box = Box(mul_by_3)
    left_maybe = Maybe(mul_by_3)
    left_lazy = Lazy(mul_by_3)
    right_lazy = Lazy.of(add_one).map(mul_by_3)

    assert left_lazy.ap(right_lazy).get() == 9
    assert left_box.ap(right_lazy).get() == 9

# Generated at 2022-06-14 03:39:46.520109
# Unit test for method get of class Lazy
def test_Lazy_get():
    assert Lazy(lambda: 'foo').get() == 'foo'



# Generated at 2022-06-14 03:39:58.260551
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.validation import Validation

    def test_fn(a):
        def inner(b):
            return a + b

        return inner

    lazy_fn = Lazy(test_fn)
    lazy_value = Lazy.of(10)
    validation = Validation.of(True)
    empty_validation = Validation.of(False)

    assert lazy_fn.ap(lazy_value).get() == 20
    assert lazy_fn.ap(validation).to_box().get() == validation.to_box().get()
    assert lazy_fn.ap(empty_validation) == empty_validation

    # Test for empty lazy
    lazy_fn_empty = Lazy.of(test_fn)

# Generated at 2022-06-14 03:40:07.687424
# Unit test for method get of class Lazy
def test_Lazy_get():
    lazy_lazy = Lazy.of(lambda: 'lazy value')
    assert lazy_lazy.get() == 'lazy value'



# Generated at 2022-06-14 03:40:16.252830
# Unit test for method map of class Lazy
def test_Lazy_map():  # pragma: no cover
    # GIVEN class Lazy with any function
    lazy = Lazy(lambda x: x + 1)
    # AND function returning argument multiplied by 2
    fn = lambda x: x * 2
    # WHEN try to map lazy constructor_fn by given function
    new_lazy = lazy.map(fn)
    # THEN new Lazy have function calling constructor_fn with 2 as argument
    assert Lazy(lambda: fn(lazy.constructor_fn(2))) == new_lazy


# Generated at 2022-06-14 03:40:17.581997
# Unit test for method map of class Lazy
def test_Lazy_map():  # pragma: no cover
    assert Lazy(lambda: 1).map(lambda x: x + 1).get() == 2



# Generated at 2022-06-14 03:40:23.261136
# Unit test for method map of class Lazy
def test_Lazy_map():
    assert Lazy.of(1).map(str) == Lazy.of('1')
    assert Lazy.of(1).map(str).map(int) == Lazy.of(1)
    assert Lazy.of(1).map(lambda x: int(x) / 0) == Lazy.of(0)



# Generated at 2022-06-14 03:40:29.186748
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    def add(a):
        return a + 10

    def mul(a):
        return a * 3

    def add_mul(a):
        return add(mul(a))

    lazy = Lazy(mul).map(add)
    lazy1 = Lazy(add).ap(lazy)
    assert lazy1.get(5) == add_mul(5)



# Generated at 2022-06-14 03:40:42.437715
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.monad_maybe import Maybe

    constructor_fn = lambda *args: args

    assert Maybe.just(lambda x: x)\
        .ap(Lazy(constructor_fn)) == Maybe.just(constructor_fn(None))
    assert Lazy(constructor_fn)\
        .ap(Maybe.just(lambda x: x)) == Maybe.just(constructor_fn(None))

    assert Maybe.just(lambda x, y: x+y)\
        .ap(Lazy(constructor_fn)) == Maybe.just(constructor_fn(None, None))
    assert Lazy(constructor_fn)\
        .ap(Maybe.just(lambda x, y: x+y)) == Maybe.just(constructor_fn(None, None))


# Generated at 2022-06-14 03:40:44.935692
# Unit test for method get of class Lazy
def test_Lazy_get():
    assert Lazy.of(1).get() == 1
    assert Lazy.of((lambda x: x * 2)).get(2) == 4



# Generated at 2022-06-14 03:40:49.159708
# Unit test for method get of class Lazy
def test_Lazy_get():
    def function1(value: str) -> int:
        return len(value)

    lazy = Lazy(function1)
    assert lazy.get('test') == 4
    assert lazy.is_evaluated
    assert lazy.value == 4



# Generated at 2022-06-14 03:40:57.064128
# Unit test for method bind of class Lazy
def test_Lazy_bind():  # pragma: no cover
    def add1(x):
        return x + 1

    def concat(acc, x):
        return acc + str(x)

    def trace(x):
        return Lazy(lambda: print(x))

    lazy_function = Lazy.of(1).map(add1).bind(trace).map(add1).bind(trace).map(add1).bind(trace).map(add1).fold(concat, "")
    print(lazy_function)

    assert(lazy_function == "1234")



# Generated at 2022-06-14 03:41:03.515365
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    assert Lazy(lambda: 'mock_data').bind(lambda data: Lazy(lambda: data.upper())).get() == 'MOCK_DATA'
    assert Lazy(lambda: 1).bind(lambda value: Lazy(lambda: value + 1)).get() == 2
    assert Lazy(lambda: {1: 'test'}).bind(lambda data: Lazy(lambda: data[1])).get() == 'test'
    assert Lazy(lambda: (1, 2, 3)).bind(lambda data: Lazy(lambda: data[0] + data[1])).get() == 3


# Generated at 2022-06-14 03:41:19.709156
# Unit test for method map of class Lazy
def test_Lazy_map():
    """
    Test for Lazy.map method.
    """
    from pymonet.box import Box
    from pymonet.either import Right
    from pymonet.maybe import Maybe
    from pymonet.validation import Validation

    def fn3(a):
        return a ** 2

    def fn2(a):
        return a + 2

    def fn1(a):
        return a ** 3

    assert Lazy(fn1).map(fn2).map(fn3).get(2) == 512
    assert Lazy(fn1).bind(lambda a: Lazy(fn2).map(fn3)).get(2) == 512
    assert Box(3).map(fn1).map(fn2).map(fn3).get() == 512
    assert Right(3).map(fn1).map(fn2).map

# Generated at 2022-06-14 03:41:30.391402
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.monad_try import Success, Failure
    from pymonet.validation import Validation

    def actual_fn(a: int) -> int:
        return a + 5

    def expect_fn(a: int) -> Lazy[int, int]:
        return Lazy.of(a + 5)

    assert Lazy.of(5).ap(Lazy.of(actual_fn)) == expect_fn(5)
    assert Lazy.of(Success(10)).ap(Lazy.of(actual_fn)) == expect_fn(Success(10))
    assert Lazy.of(Failure(RuntimeError('exception'))).ap(Lazy.of(actual_fn)) == expect_fn(Failure(RuntimeError('exception')))