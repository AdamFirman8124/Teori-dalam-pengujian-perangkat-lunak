

# Generated at 2022-06-14 03:31:39.337206
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.box import Box
    from pymonet.monad import Monad

    def box_mapper(value):
        return Box(value + 1)
    def lazy_mapper(value):
        return Lazy.of(value + 1)

    wrapper_box = lambda value: Box(value)
    wrapper_lazy = lambda value: Lazy.of(value)

    for monad in [Box, Lazy]:
        for wrapper in [wrapper_box, wrapper_lazy]:
            for mapper in [box_mapper, lazy_mapper]:
                assert monad(2).ap(wrapper(mapper)) == wrapper(mapper)(2)



# Generated at 2022-06-14 03:31:49.448985
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():  # pragma: no cover
    assert Lazy.of(1) == Lazy.of(1)
    assert Lazy.of('test') == Lazy.of('test')
    assert Lazy.of(None) == Lazy.of(None)

    assert Lazy.of(1) != Lazy.of('test')
    assert Lazy.of('test') != Lazy.of(1)
    assert Lazy.of(1) != Lazy.of(None)
    assert Lazy.of(None) != Lazy.of(1)
    assert Lazy.of(None) != Lazy.of('test')
    assert Lazy.of('test') != Lazy.of(None)



# Generated at 2022-06-14 03:31:54.130007
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.box import Box

    def test_fn(value):
        return Box(value * 2)

    assert Lazy(lambda x: x).bind(test_fn).get(4) == Box(8)

# Generated at 2022-06-14 03:31:59.990922
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    l1 = Lazy.of(1)
    l2 = Lazy.of(1)
    assert l1 == l2
    l2.get()
    assert l1 == l2
    l2 = Lazy.of(2)
    assert l1 != l2
    l1.get()
    assert l1 != l2
    l2 = Lazy.of(1)
    assert l1 != l2

# Generated at 2022-06-14 03:32:08.088391
# Unit test for method bind of class Lazy
def test_Lazy_bind():

    # empty Lazy
    value = Lazy.of(0)
    value_extra_arg = 'extra arg'
    value_result = 1
    value_args = (1, )

    # mapper
    def mapper(result: int, extra_arg: str) -> int:
        return value_result

    value_mapper_result = value.bind(
        lambda *args: Lazy(
            lambda *args: mapper(value_result, value_extra_arg)
        )
    ).get(*value_args)
    assert value_mapper_result == value_result

# Generated at 2022-06-14 03:32:11.901101
# Unit test for method get of class Lazy
def test_Lazy_get():
    """
    >>> test_Lazy_get()
    True
    """
    def test_fn(x):
        return x + 2

    test_lazy_fn = Lazy(test_fn)
    return test_lazy_fn.get(2) == 4



# Generated at 2022-06-14 03:32:20.622039
# Unit test for method bind of class Lazy
def test_Lazy_bind():  # pylint: disable=redefined-outer-name
    from pymonet.either import Right, Left
    from pymonet.monad_maybe import Maybe

    # pylint: disable=too-many-locals
    def foo(number):
        if number > 2:
            return Lazy(lambda: Right(number + 1))
        return Lazy(lambda: Left('Error'))

    def bar(other_number):
        if other_number > 4:
            return Lazy(lambda: Maybe.just(other_number + 2))
        return Lazy(lambda: Maybe.empty())

    def baz(maybe_value: Maybe):
        return Lazy(lambda: Right(maybe_value))

    def fold(number):
        return Lazy(lambda: foo(number)).bind(bar).bind(baz).get()



# Generated at 2022-06-14 03:32:31.061545
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    assert Lazy.of(lambda x: x + 1).ap(Lazy.of(2)) == Lazy.of(3)
    assert Lazy.of(lambda x: x + 1).ap(Lazy.of(lambda y: y + 1)).ap(Lazy.of(2)) == Lazy.of(4)

    assert Lazy.of(lambda x, y: x + y).ap(Lazy.of(1)).ap(Lazy.of(2)) == Lazy.of(3)
    assert Lazy.of(lambda x, y: x + y).ap(Lazy.of(lambda x: x + 1)).ap(Lazy.of(2)) == Lazy.of(4)

# Generated at 2022-06-14 03:32:43.148287
# Unit test for method get of class Lazy
def test_Lazy_get():  # pragma: no cover
    from pymonet.box import Box
    from pymonet.either import Right
    from pymonet.maybe import Just
    from pymonet.monad_try import Success
    from pymonet.validation import SuccessValidation

    def test_case():
        def fn(a):
            return a + 3

        def fn2(a):
            return a + 4

        def fn3(a):
            return a + 5

        assert (Lazy.of(5).get()
                == 5)

        assert (Lazy(fn).get(2)
                == 5)

        assert (Lazy(fn3).map(fn2).map(fn).map(fn).get(1)
                == 16)


# Generated at 2022-06-14 03:32:45.697969
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    assert Lazy(lambda: 1) == Lazy(lambda: 1)
    assert Lazy(lambda: 1) != Lazy(lambda: 2)



# Generated at 2022-06-14 03:32:50.391759
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    f = Lazy.of(10)
    g = Lazy.of(10)

    assert f == g, "Two not empty Lazy should be equal"



# Generated at 2022-06-14 03:32:54.404356
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def builder(val):
        return Lazy(lambda: val)

    assert Lazy(lambda: "Hello") \
        .bind(lambda a: builder(a + ", world")) \
        .get() == "Hello, world"

    assert Lazy(lambda: "Hello") \
        .bind(lambda a: builder(a + ", world")) \
        .bind(lambda a: builder(a + '!')) \
        .get() == "Hello, world!"

    assert Lazy(lambda: "Hello") \
        .bind(lambda a: builder(a + ", world")) \
        .bind(lambda a: builder(a + '!')) \
        .bind(lambda a: builder(a + '!')) \
        .get() == "Hello, world!!!"


# Generated at 2022-06-14 03:32:59.897213
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    def plus(a: int) -> int:
        return a + 1

    plus_lazy = Lazy(plus)
    two_lazy = Lazy(lambda *args: 2)

    assert plus_lazy.ap(two_lazy).constructor_fn(None) == 3

    # Ensure we don't evaluate function
    assert two_lazy.is_evaluated is False
    assert plus_lazy.is_evaluated is False

# Generated at 2022-06-14 03:33:03.603719
# Unit test for method get of class Lazy
def test_Lazy_get():
    """
    Testing Lazy get method
    """
    assert Lazy.of(2).get() == 2



# Generated at 2022-06-14 03:33:07.460006
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def sum(x):
        def sum_impl(y):
            return Lazy.of(x + y)
        return sum_impl

    l = Lazy.of(1)
    assert l.bind(sum(2)).get() == 3



# Generated at 2022-06-14 03:33:11.153259
# Unit test for method map of class Lazy
def test_Lazy_map():
    def square(x: int) -> int:
        return x * x

    double = Lazy(lambda x: x + x)
    map_double = double.map(square)

    assert square(double.get(1)) == map_double.get(1)



# Generated at 2022-06-14 03:33:16.007195
# Unit test for method get of class Lazy
def test_Lazy_get():
    def f(arg1, arg2):
        return arg1 + arg2

    lazy = Lazy(f)

    assert lazy.get(5, 2) == 7
    assert lazy.is_evaluated

    assert lazy.get(5, 2) == 7
    assert lazy.is_evaluated


# Generated at 2022-06-14 03:33:22.067335
# Unit test for method get of class Lazy
def test_Lazy_get():
    def f(x):
        return x + 1

    lazy = Lazy(f)
    lazy2 = Lazy(f)
    lazy3 = Lazy(f)
    assert lazy.get(1) == 2
    assert lazy.get(1) == 2
    assert lazy.is_evaluated
    assert lazy2.get(2) == 3
    assert lazy2.is_evaluated
    assert lazy3.is_evaluated is False
    assert lazy3.get(3) == 4



# Generated at 2022-06-14 03:33:23.445896
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    from pymonet.box import Box

    lazy = Lazy.of(Box(2))
    assert lazy == Lazy(lambda *args: Box(2))



# Generated at 2022-06-14 03:33:27.128313
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    def test_Lazy___eq__():
        fn = lambda: 1
        lazy = Lazy(fn)

        assert lazy == lazy
        assert lazy == Lazy(fn)
        assert lazy == Lazy.of(1)
        assert lazy != Lazy.of(2)
        assert lazy == Lazy(lambda: 1).to_try()


# Generated at 2022-06-14 03:33:31.100190
# Unit test for method get of class Lazy
def test_Lazy_get():
    assert Lazy.of(1).get(None) == 1

# Generated at 2022-06-14 03:33:33.178543
# Unit test for method get of class Lazy
def test_Lazy_get():
    assert Lazy.of(1).get() == 1


# Generated at 2022-06-14 03:33:42.506730
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.box import Box
    from pymonet.either import Right
    from pymonet.maybe import Maybe
    from pymonet.monad_try import Try
    from pymonet.validation import Validation

    assert Lazy.of(4).bind(lambda x: Lazy.of(x + 2)) == Lazy.of(6)
    assert Lazy.of(4).bind(lambda x: Box(x + 2)) == Box(6)
    assert Lazy.of(4).bind(lambda x: Right(x + 2)) == Right(6)
    assert Lazy.of(4).bind(lambda x: Maybe.just(x + 2)) == Maybe.just(6)

# Generated at 2022-06-14 03:33:45.156359
# Unit test for method get of class Lazy
def test_Lazy_get():
    def lazy_fun():
        return 'some'

    lazy = Lazy(lazy_fun)

    assert lazy.get() == 'some'



# Generated at 2022-06-14 03:33:51.740781
# Unit test for method get of class Lazy
def test_Lazy_get():  # pragma: no cover
    assert Lazy.of(7).get() == 7
    assert Lazy.of(lambda x: x+1).map(lambda x: x(5)).get() == 6
    assert Lazy.of(lambda x: x).ap(Lazy.of('a')).get() == 'a'
    assert Lazy.of(lambda x: x).bind(lambda x: Lazy.of(x+1)).get() == 2



# Generated at 2022-06-14 03:33:57.488010
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    assert Lazy(lambda x: x).bind(lambda x: Lazy(lambda x: x * 2)).get(4) == 8
    assert Lazy(lambda x: x).bind(lambda x: Lazy(lambda x: x * 2)).bind(lambda x: Lazy(lambda x: x * 3)).get(4) == 24


# Generated at 2022-06-14 03:33:58.233086
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    pass



# Generated at 2022-06-14 03:34:05.472519
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    from pymonet.box import Box

    def fn() -> Box[int]:
        return Box.empty()

    lazy1: Lazy[None, Box[int]] = Lazy(fn)
    lazy2: Lazy[None, Box[int]] = Lazy(fn)

    assert lazy1 == lazy2

    answer1: Box[int] = lazy1.constructor_fn()
    lazy1.is_evaluated = True
    lazy1.value = answer1

    answer2: Box[int] = lazy2.constructor_fn()
    lazy2.is_evaluated = True
    lazy2.value = answer2

    assert lazy1 == lazy2


# Generated at 2022-06-14 03:34:12.296463
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    # pylint: disable=unused-argument
    from pymonet.either import Left

    def fn(x):
        return Lazy(lambda *args: x + 1)

    assert Lazy(lambda *args: 1).bind(fn).get() == 2

    def error(x):
        return Lazy(lambda *args: Left('error'))

    assert Lazy(lambda *args: 1).bind(error).get() == Left('error')



# Generated at 2022-06-14 03:34:18.214098
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    def fn(x: int) -> int: return x + 1

    def fx(x: int) -> int: return x * 2

    lazy = Lazy(lambda: 10)
    lazy_fn = Lazy(lambda: fn)

    assert lazy.ap(lazy_fn) == Lazy(lambda: fn(10))
    assert lazy.to_maybe().ap(Maybe.just(fn)) == Maybe.just(fn(10))

# Generated at 2022-06-14 03:34:30.656826
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    """

    """
    from pymonet.monad_try import Try
    from pymonet.validation import Validation

    try_or_logging = lambda x: Try.of(int, x) | Try.of(lambda x: logging.info(x), x)

    x = Lazy.of(lambda x: x + 1)
    y = Lazy.of(lambda x: x + 1)
    z = x.bind(y.bind)
    assert z.get(1) == 3

    x = Lazy.of(lambda x: x + 1)
    y = Lazy.of(lambda x: x + 1)
    z = x.bind(lambda x: y.bind(lambda y: Lazy.of(x + y)))
    assert z.get(1) == 3

    x = Lazy.of

# Generated at 2022-06-14 03:34:38.550378
# Unit test for method map of class Lazy
def test_Lazy_map():
    # Testing map method on not evaluated Lazy
    result = Lazy(lambda: 3) \
        .map(lambda x: x + 1) \
        .map(lambda x: x + 1) \
        .fold(lambda: 4)

    assert 3 == result

    # Testing map method on evaluated Lazy
    result = Lazy(lambda: 3) \
        .fold(lambda: 4) \
        .map(lambda x: x + 1) \
        .map(lambda x: x + 1)

    assert 5 == result


# Generated at 2022-06-14 03:34:44.725588
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    assert Lazy.of(1) == Lazy.of(1)
    assert Lazy.of(1) != Lazy.of(2)
    assert Lazy.of(1) != Lazy.of(2.0)
    assert Lazy.of(1) != Lazy.of("1")
    assert Lazy.of(1) != Lazy.of("foo")
    assert Lazy.of(1) != Lazy.of("foo").map(lambda _: 1)



# Generated at 2022-06-14 03:34:49.432259
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    """Test that two Lazy are equals where both are evaluated both have the same value and
    constructor functions.
    """
    lam = Lazy(lambda: 1)
    lam2 = Lazy(lambda: 1)
    lam3 = Lazy(lambda: 2)
    assert lam == lam

# Generated at 2022-06-14 03:34:56.580591
# Unit test for method bind of class Lazy
def test_Lazy_bind():

    def error_generator():
        raise Exception('raise exception')

    error = Lazy(error_generator).bind(lambda x: Lazy.of(x * 7)).get()
    assert error == None

    random_lazy_value = Lazy.of(3).bind(lambda x: Lazy.of(x * 7)).get()
    assert random_lazy_value == 21

    def large_number_generator():
        return 79

    assert Lazy.of(large_number_generator).bind(lambda x: Lazy.of(x())).get() == 79



# Generated at 2022-06-14 03:35:04.556605
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    def func_1():
        return 1

    def func_2():
        return 2

    lazy_1 = Lazy(func_1)
    assert not (lazy_1 == Lazy(func_2))
    assert lazy_1 == Lazy(func_1)

    lazy_1._compute_value()
    assert not (lazy_1 == Lazy(func_1))
    assert lazy_1 == Lazy.of(1)



# Generated at 2022-06-14 03:35:09.990868
# Unit test for method map of class Lazy
def test_Lazy_map():
    class TestClass:
        def __init__(self, id):
            self.id = id
            self.generated_id = 0

        def generate_id(self):
            self.generated_id = self.id
            self.id = self.id + 1
            return self.generated_id

    def test_fn(n):
        return TestClass(n)

    lazy_fn = Lazy(test_fn)
    lazy_with_map = lazy_fn.map(lambda c: c.id)

    assert lazy_with_map.get(1) == 1



# Generated at 2022-06-14 03:35:13.830186
# Unit test for method get of class Lazy
def test_Lazy_get():
    def user_by_id(id):
        return 'John Doe'

    lazy = Lazy(user_by_id)

    assert lazy.get(1) == 'John Doe'

# Generated at 2022-06-14 03:35:20.553600
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def merge_two_values(a: int, b: int) -> int:
        return a + b

    def get_b_value(a: int) -> int:
        return 5

    lazy_fn = Lazy(lambda a: merge_two_values(a, get_b_value(a)))

    result = lazy_fn.bind(lambda res: Lazy.of(res)).get(1)

    assert result == 6

# Generated at 2022-06-14 03:35:24.371043
# Unit test for method get of class Lazy
def test_Lazy_get():
    def fn():
        return 5

    lazy = Lazy(fn)

    assert lazy.get() == 5
    assert lazy.is_evaluated
    assert lazy.value == 5



# Generated at 2022-06-14 03:35:31.493127
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    """
    Unit test for method bind of class Lazy
    """
    def func_sum(x, y):
        return x + y

    def func_mul(x, y):
        return x * y

    lazy = Lazy(func_sum).bind(lambda x: Lazy(func_mul).map(lambda y: y * x))
    assert lazy.get(1, 1) == 2



# Generated at 2022-06-14 03:35:40.544137
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():  # pragma: no cover
    lazy_1 = Lazy.of(1)
    lazy_2 = Lazy.of(1)

    assert lazy_1 == lazy_2

    lazy_1 = Lazy.of('test')
    lazy_2 = Lazy.of('test')

    assert lazy_1 == lazy_2

    lazy_1 = Lazy.of([1, 2, 3])
    lazy_2 = Lazy.of([1, 2, 3])

    assert lazy_1 == lazy_2



# Generated at 2022-06-14 03:35:50.345097
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    import pymonet.maybe

    def inc(value):
        return value + 1

    def is_even(number):
        return number % 2 == 0

    def multiply_by_2(number):
        return number * 2

    def divide_by_2(number):
        return number / 2

    lazy = Lazy.of(10).bind(
        lambda value: Lazy.of(inc(value)).bind(
            is_even
        )
    ).bind(
        multiply_by_2
    ).bind(
        divide_by_2
    )
    assert lazy.get() == 10


# Generated at 2022-06-14 03:36:02.145232
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    """
    Check Lazy.ap method with notempty Lazy
    """
    from pymonet.either import Right

    def add_2(x):
        return x + 2

    result = Lazy.of(2).ap(Lazy.of(add_2))
    assert result.get() == 4

    # check if Lazy with constructor returning Either
    def add_3(x):
        return Right(x + 3)

    result = Lazy.of(2).ap(Lazy.of(add_3))
    assert result.get() == Right(5)

    # check if Lazy with constructor returning Lazy
    def add_4(x):
        return Lazy.of(x + 4)

    result = Lazy.of(2).ap(Lazy.of(add_4))
    assert result.get()

# Generated at 2022-06-14 03:36:12.080138
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.box import Box
    from pymonet.monad_try import Try

    try_double_value = Try(lambda n: n * 2)
    try_inc_value = Try(lambda n: n + 1)
    lazy_value = Lazy(lambda n: n * 3)
    box_value = Box(4)

    assert lazy_value.ap(try_double_value).get(1) == 6
    assert lazy_value.ap(try_inc_value).get(1) == 4
    assert lazy_value.ap(box_value) == lazy_value.map(lambda n: n * 4)
    assert lazy_value.ap(try_double_value) != lazy_value.map(lambda n: n * 4)
    assert lazy_value.ap(try_double_value) == lazy_value

# Generated at 2022-06-14 03:36:22.861109
# Unit test for method get of class Lazy
def test_Lazy_get():
    """
    Test Lazy get method.
    """
    # pylint: disable=protected-access
    result = Lazy(lambda arg: arg + arg).get(5)
    assert result == 10
    assert Lazy(lambda arg: arg + arg).value is None
    assert Lazy(lambda arg: arg + arg).is_evaluated is False
    result = Lazy(lambda arg: arg + arg).get(5)
    assert result == 10
    assert Lazy(lambda arg: arg + arg).value == 10
    assert Lazy(lambda arg: arg + arg).is_evaluated is True
    # pylint: enable=protected-access

# Unit tests for methods of, map and bind of class Lazy

# Generated at 2022-06-14 03:36:33.725828
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    lazy_one_to_one = Lazy(lambda *args: 1)
    lazy_one_to_one_copy = Lazy(lambda *args: 1)
    lazy_zero_to_zero = Lazy(lambda *args: 0)
    lazy_one_to_zero = Lazy(lambda *args: 0)

    assert lazy_one_to_one == lazy_one_to_one
    assert lazy_one_to_one == lazy_one_to_one_copy
    assert lazy_one_to_one != lazy_zero_to_zero
    assert lazy_one_to_one != lazy_one_to_zero

# Generated at 2022-06-14 03:36:42.797946
# Unit test for method get of class Lazy
def test_Lazy_get():  # pragma: no cover
    from pymonet.box import Box
    from pymonet.validation import Validation

    def test_fn():
        return 1

    lazy_obj1 = Lazy(test_fn)
    assert lazy_obj1.get() == 1

    lazy_obj2 = Lazy.of(1)
    assert lazy_obj2.get() == 1

    lazy_obj3 = lazy_obj2.map(lambda x: x + 1)
    assert lazy_obj3.get() == 2

    lazy_obj4 = lazy_obj2.ap(Lazy.of(lambda x: x + 1))
    assert lazy_obj4.get() == 2

    lazy_obj5 = lazy_obj2.bind(lambda x: Lazy.of(x + 1))

# Generated at 2022-06-14 03:36:54.374350
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def fn(a):
        return Lazy.of(a + ' world!')

    assert Lazy.of('hello').bind(fn).get() == 'hello world!'
    assert Lazy.of('hello').bind(fn).constructor_fn() == 'hello world!'
    assert Lazy.of('hello').bind(fn).to_box().get() == 'hello world!'
    assert Lazy.of('hello').bind(fn).to_either().get() == 'hello world!'
    assert Lazy.of('hello').bind(fn).to_maybe().get() == 'hello world!'
    assert Lazy.of('hello').bind(fn).to_try().get() == 'hello world!'
    assert Lazy.of('hello').bind(fn).to_validation().get() == 'hello world!'


# Generated at 2022-06-14 03:37:04.454997
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    def func(*args):
        return args

    assert Lazy(func) == Lazy(func)
    assert Lazy.of(1) == Lazy.of(1)
    assert not Lazy.of(1) == Lazy.of(2)
    assert not Lazy.of(1) == Lazy.of(None)
    assert not Lazy.of(None) == Lazy.of(1)

    def func1(*args):
        return args

    def func2(*args):
        return args

    assert Lazy(func1) == Lazy(func1)
    assert not Lazy(func1) == Lazy(func2)


# Generated at 2022-06-14 03:37:16.276667
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    def func(*args):
        return 1

    assert Lazy(func) == Lazy(func)
    assert Lazy.of(10) == Lazy.of(10)
    assert not Lazy(func) == Lazy.of(10)
    assert not Lazy(func) == None


# Generated at 2022-06-14 03:37:23.380189
# Unit test for method ap of class Lazy
def test_Lazy_ap():  # pragma: no cover
    from pymonet.validation import Validation
    from pymonet.utils.compare import compare
    import pymonet.implementations as impl

    mapper = Lazy(lambda x: x + 1)
    fn = Lazy(lambda x: x + 2)
    applicative = mapper.ap(fn)

    assert compare(impl.compute(applicative.get(1)),impl.compute(Validation.success(4)))

# Generated at 2022-06-14 03:37:32.933234
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    from pymonet.either import Right
    from pymonet.box import Box
    from pymonet.maybe import Maybe

    assert Lazy.of(Right(Right(1))) == Lazy.of(Right(Right(1)))
    assert (Lazy.of(Right(Right(1))) == Lazy.of(Right(Right(1))) == Lazy.of(Right(Right(1))))
    assert Lazy.of(Box(Right(Right(1)))) == Lazy.of(Box(Right(Right(1))))
    assert Lazy.of(Maybe.empty()) == Lazy.of(Maybe.empty())
    assert Lazy.of(Right(Right(1))) != Lazy.of(Right(Right(2)))

# Generated at 2022-06-14 03:37:44.172019
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from tests.conftest import assert_that

    def return_1():
        return 1

    def return_2():
        return 2

    def return_3():
        return 3

    lazy_1 = Lazy.of(return_1)

    assert_that(
        lazy_1.bind(lambda x: Lazy.of(lambda: x + return_2())),
        Lazy.of(lambda: return_3())
    )

    assert_that(
        lazy_1.bind(lambda x: Lazy.of(lambda: x))
        .bind(lambda x: Lazy.of(lambda: x + return_2()))
        .bind(lambda x: Lazy.of(lambda: x + return_3())),
        Lazy.of(lambda: return_6())
    )



# Generated at 2022-06-14 03:37:48.862525
# Unit test for method get of class Lazy
def test_Lazy_get():
    assert Lazy.of(1).get() == 1

    passed = False
    def raise_exception():
        raise Exception()
        return
    lazy_with_exception = Lazy(raise_exception)

    try:
        lazy_with_exception.get()
    except Exception:
        passed = True

    assert passed


# Generated at 2022-06-14 03:37:51.868492
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    lazy = Lazy.of(1)
    lazy_copy = lazy
    lazy_same = Lazy.of(1)
    lazy_not_equal = Lazy.of(2)

    assert lazy == lazy_copy
    assert lazy == lazy_same
    assert lazy_not_equal != lazy


# Generated at 2022-06-14 03:37:58.626982
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    from pymonet.functor import Functor

    fn = lambda x: x + 1
    lazy = Lazy(fn)
    lazy1 = Lazy(fn)
    lazy2 = Lazy(lambda x: x + 2)

    assert lazy == lazy1
    assert lazy != lazy2
    assert lazy != object()
    assert lazy != Functor(fn)

# Generated at 2022-06-14 03:38:05.210546
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():  # pragma: no cover
    def identity(x):
        return x

    def inc(x):
        return x + 1

    def dec(x):
        return x - 1

    lazy = Lazy(identity)
    assert lazy == Lazy(identity)
    assert lazy == Lazy.of(1)
    assert Lazy(inc).map(dec) == Lazy(dec).map(inc)
    assert lazy != Lazy(1), "Lazy can't be equal to non Lazy objects"
    assert lazy != Lazy(inc)
    assert lazy != Lazy(inc).map(inc)



# Generated at 2022-06-14 03:38:13.334555
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def add_5(x):
        return x + 5

    def mult_2(x):
        return x * 2

    assert Lazy.of(1).bind(lambda x: Lazy.of(x + 1)).get() == 2
    assert Lazy.of(2).bind(lambda x: Lazy.of(mult_2(add_5(x)))).get() == 14

    assert Lazy.of(1).bind(lambda _: Lazy.of(1)).bind(lambda _: Lazy.of(1)).bind(lambda _: Lazy.of(2)).get() == 2

    assert Lazy.of(1).bind(lambda x: Lazy.of(mult_2(x))).get() == 2

# Generated at 2022-06-14 03:38:24.679538
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    from pymonet.functor import Functor
    from pymonet.applicative import Applicative
    from pymonet.monad import Monad

    @Functor.instance(Lazy)
    def functor_factory():
        return Lazy

    assert functor_factory(Lazy(lambda x: x)).fmap(lambda x: x).equals(Lazy(lambda x: x))

    @Applicative.instance(Lazy)
    def applicative_factory():
        return Lazy

    assert applicative_factory(Lazy(lambda x: x)).ap(Lazy(lambda x: x)).equals(Lazy(lambda x: x))

# Generated at 2022-06-14 03:38:49.965647
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    lazy_fn = Lazy.of(lambda x: x + 1)
    assert Lazy.of(1).ap(lazy_fn) == Lazy.of(2)

    lazy_fn = Lazy.of(lambda x: x + 1)
    assert Lazy.of(1).ap(lazy_fn) == Lazy.of(2)

    lazy_fn = Lazy.of(lambda x, y: x + y)
    assert Lazy.of(lambda x: x + 1).ap(lazy_fn) == Lazy.of(3)

    lazy_fn = Lazy.of(lambda x: Lazy.of(lambda y: x + y))
    assert Lazy.of(1).ap(lazy_fn) == Lazy.of(2)



# Generated at 2022-06-14 03:38:56.782377
# Unit test for method get of class Lazy
def test_Lazy_get():  # pragma: no cover
    assert Lazy(lambda x: x + 1).get(2) == 3
    assert Lazy(lambda x: x - 1).get(2) == 1
    assert Lazy(lambda x: x * 3).get(2) == 6
    assert Lazy(lambda x: x / 3).get(2) == 2 / 3


# Generated at 2022-06-14 03:38:58.613284
# Unit test for method map of class Lazy
def test_Lazy_map():
    assert Lazy.of(2).map(lambda x: x * 3) == Lazy.of(6)



# Generated at 2022-06-14 03:39:01.709370
# Unit test for method map of class Lazy
def test_Lazy_map():
    assert Lazy(lambda x: x).map(lambda x: x + 1).get(0) == 1
# It's end of unit tests



# Generated at 2022-06-14 03:39:10.758531
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    assert (Lazy(lambda x: x) == Lazy(lambda: 0)) is False
    assert (Lazy(lambda x: x) == Lazy(lambda x: x)) is True
    assert (Lazy(lambda x: x).map(lambda x: x + 1) == Lazy(lambda x: x * 2)) is False
    assert (Lazy(lambda x: x).map(lambda x: x + 1) == Lazy(lambda x: x + 1)) is True
    assert (Lazy(lambda x: x).map(lambda x: x + 1).ap(Lazy(lambda x: x - 1)).get(5) == 5)

# Generated at 2022-06-14 03:39:16.226367
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    """Unit test for method __eq__ of class Lazy."""
    assert Lazy(lambda *args: args) != ""
    assert Lazy(lambda *args: args) == Lazy(lambda *args: args)
    assert Lazy(lambda *args: args) != Lazy(lambda *args: (args))



# Generated at 2022-06-14 03:39:28.630999
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    def value_factory():
        return 'value'

    assert Lazy(value_factory) == Lazy(value_factory)
    assert not Lazy(value_factory).get() == Lazy(value_factory)
    assert Lazy(value_factory) == Lazy(value_factory).get()
    assert Lazy(value_factory).get() == Lazy(value_factory).get()
    assert not Lazy(value_factory) == Lazy(value_factory).get()
    assert not Lazy(value_factory).get() == Lazy(value_factory)
    assert not Lazy(value_factory) == Lazy(lambda: 'new value')
    assert not Lazy(value_factory).get() == Lazy(lambda: 'new value').get()

# Generated at 2022-06-14 03:39:33.002139
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def fn(v):
        def inner_fn():
            return v + 2
        return Lazy(inner_fn)

    assert Lazy(lambda: 3).bind(fn) == Lazy.of(5)  # type: ignore



# Generated at 2022-06-14 03:39:38.694903
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    lazy_str = Lazy(lambda a, b: '{} {}'.format(a, b))

    fn = lambda string: Lazy(lambda: len(string))
    result = lazy_str.bind(fn)

    assert result.get('hello', 'world') == len('hello world')



# Generated at 2022-06-14 03:39:49.568123
# Unit test for method map of class Lazy
def test_Lazy_map():
    class Child:
        def __init__(self, name):
            self.name = name

    class Parent:
        def __init__(self, children):
            self.children = children

    def lazy_child_name() -> Lazy[None, str]:
        return Lazy(lambda: Child('Adam').name)

    def lazy_children_names():
        """
        Make Lazy with list of children names with mapper.
        """
        return lazy_child_name().map(lambda name: 'Hello {}'.format(name))

    def lazy_parent_names():
        """
        Make Lazy with list of children names.
        """
        return lazy_children_names().map(lambda name: 'Mr {}'.format(name))


# Generated at 2022-06-14 03:40:42.422466
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    lazy_function = Lazy(lambda x: x * 2)
    value = 3

    assert lazy_function.ap(Lazy.of(value)).get() == 6

    lazy_function = Lazy(lambda x: x + 2)
    value = 3

    assert lazy_function.ap(Lazy.of(value)).get() == 5

# Generated at 2022-06-14 03:40:54.437887
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.validation import Validation

    assert Lazy(lambda: 1).ap(Lazy(lambda x: x + 1)).get() == 2
    assert Lazy(lambda: 1).to_validation().ap(Validation.success(lambda x: x + 1)).get() == 2
    assert Lazy(lambda: 1).ap(Validation.success(lambda x: x + 1)).to_validation().get() == 2
    assert Lazy(lambda: 1).ap(Validation.success(lambda x: x + 1)).bind(lambda x: Lazy(lambda: x + 2)).get() == 3
    assert Lazy(lambda: 1).ap(Validation.success(lambda x: x + 1)).to_box().bind(
        lambda x: Lazy(lambda: x + 2)).get() == 3



# Generated at 2022-06-14 03:40:57.135705
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def f(x):
        return Lazy(lambda *args: x + 5)

    lazy_value = Lazy(lambda: 7)
    lazy_result = lazy_value.bind(f)
    assert lazy_result.get() == 12


# Generated at 2022-06-14 03:41:03.930692
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    func = Lazy(lambda x: x + 1)
    result = func.ap(Lazy(lambda x: x + 1))
    assert result.get() == 2

    assert Lazy(lambda: 1).map(lambda v: v + 1).ap(Lazy(lambda v: v + 1)).get() == 3
    assert Lazy(lambda: 1).ap(Lazy(lambda v: v + 1)).get() == 2



# Generated at 2022-06-14 03:41:10.508206
# Unit test for method map of class Lazy
def test_Lazy_map():
    """
    Test for method map of Lazy class.
    """
    class TestClass:
        def __init__(self, value: int) -> None:
            self.value = value

    def fn(x: int) -> TestClass:
        return TestClass(x)

    assert Lazy.of(2).map(fn) == Lazy(lambda *args: fn(2))

    class FailClass:
        def __init__(self, value: int) -> None:
            self.value = value

    def fail_fn(x: int) -> FailClass:
        return FailClass(x)

    assert Lazy.of(2).map(fail_fn) != Lazy(lambda *args: fail_fn(2))


# Generated at 2022-06-14 03:41:15.349517
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def function(arg):
        return Lazy.of(arg)

    lazy = Lazy.of('lazy_value')
    assert lazy.bind(function).get() == 'lazy_value'

# Generated at 2022-06-14 03:41:22.998186
# Unit test for method map of class Lazy
def test_Lazy_map():  # pragma: no cover
    def add(x: int, y: int) -> int:
        return x + y

    assert Lazy(lambda: add(1, 2)).map(lambda x: x*x).get() == 9
    assert Lazy(lambda: add(1, 2)).map(lambda x: x*2).get() == 6


# Generated at 2022-06-14 03:41:31.587919
# Unit test for method map of class Lazy
def test_Lazy_map():  # pragma: no cover
    from pymonet.box import Box
    from pymonet.monad_try import Try

    def add_x(x: int) -> int:
        return x + 2

    b = Box(2)
    lazy = Lazy.of(1)
    assert lazy.map(add_x).get() == add_x(1)

    lazy_f_monkey = lazy.map(add_x).map(add_x).map(add_x).map(add_x).map(add_x).map(add_x).map(add_x).map(add_x).map(
        add_x).map(add_x)
    assert lazy_f_monkey.get() == 1024

    def add_two_params(a: int, b: int) -> int:
        return a + b