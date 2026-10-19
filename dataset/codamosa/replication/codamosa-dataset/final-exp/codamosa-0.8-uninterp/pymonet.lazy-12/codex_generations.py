

# Generated at 2022-06-14 03:31:29.550195
# Unit test for method map of class Lazy
def test_Lazy_map():
    from pymonet.maybe import Maybe

    assert Maybe.of(5).map(lambda x: x + 3) == Maybe.of(8)
    assert Maybe.of(4).map(lambda x: x + 3) == Maybe.of(7)



# Generated at 2022-06-14 03:31:33.625031
# Unit test for method get of class Lazy
def test_Lazy_get():
    from pymonet.assertions import assert_that

    def stub(x: int) -> int:
        return 4

    lazy = Lazy(stub)
    assert_that(lazy.get(1)).is_equal_to(4)



# Generated at 2022-06-14 03:31:46.405680
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    """
    Unit test for method __eq__ of class Lazy
    """
    from pymonet.validation import Validation

    assert Lazy.of(1) == Lazy.of(1)
    assert Lazy.of(1) == Lazy(lambda: 1)
    assert Lazy(lambda: 1).map(lambda x: x * 2) == Lazy(lambda: 2)

    assert (
        Lazy.of(1)
        .map(lambda x: x * 2)
        .bind(lambda x: Lazy.of(x * 3)) == Lazy.of(2).bind(lambda x: Lazy.of(x * 3))
    )

    assert Lazy.of(1).ap(Lazy.of(lambda x: x * 2)) == Lazy(lambda: 2)

    assert Lazy.of

# Generated at 2022-06-14 03:31:48.618165
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    assert Lazy.of(10) == Lazy.of(10)
    assert Lazy.of(10) != Lazy.of(11)

# Generated at 2022-06-14 03:31:55.344822
# Unit test for method bind of class Lazy
def test_Lazy_bind():  # pragma: no cover
    def add_5(x):
        return Lazy(lambda arg: arg + add_5(arg).get(5) + 5)

    lazy = Lazy.of(5)

    assert lazy.bind(add_5).constructor_fn(0) == 5
    assert lazy.bind(add_5).get(5) == 120

# Generated at 2022-06-14 03:32:00.336049
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def test_fn(x):
        return Lazy(lambda: x * 3)

    assert Lazy(lambda: 2).bind(test_fn).get() == 6



# Generated at 2022-06-14 03:32:08.033977
# Unit test for method bind of class Lazy
def test_Lazy_bind():  # pragma: no cover
    def sum_two(value):
        return value + 2

    class TestLazy(Lazy[int, int]):
        def __init__(self, constructor_fn: Callable[[int], int]) -> None:
            super().__init__(constructor_fn)

    def test_constructor_fn(x):
        return x + 2

    lazy = TestLazy(test_constructor_fn)
    result = lazy.bind(sum_two).get(2)
    assert result == 6

# Generated at 2022-06-14 03:32:18.887399
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    """
    Test methods of Lazy that return new Lazy.
    """
    def test_Lazy_bind_inner(a):
        return Lazy(lambda *args: a * a)

    lazy = Lazy(lambda *args: 1)
    lazy_bind = lazy.bind(test_Lazy_bind_inner)

    assert lazy_bind._compute_value() == 1
    assert lazy_bind._compute_value() == 1
    assert lazy_bind._compute_value() == 1
    assert lazy_bind._compute_value() == 1

    lazy_bind_result = lazy_bind.get()

    assert lazy_bind_result == 1
    assert lazy_bind_result == 1
    assert lazy_bind_result == 1
    assert lazy_bind_result == 1


# Generated at 2022-06-14 03:32:30.421738
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():  # pragma: no cover
    from pymonet.functor import Functor

    def construct_with_1_returns_1(x):
        return 1

    def construct_with_0_returns_1(x):
        return 1

    assert Lazy(lambda t: 1).__eq__(Lazy(construct_with_1_returns_1))
    assert Lazy(lambda t: 1).__eq__(Lazy(construct_with_1_returns_1))
    assert not Lazy(lambda t: 0).__eq__(Lazy(construct_with_1_returns_1))
    assert not Lazy(lambda t: 1).__eq__(Lazy(construct_with_0_returns_1))


# Generated at 2022-06-14 03:32:37.412836
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    def identity(x):
        return x

    assert Lazy(identity) == Lazy(identity)
    assert Lazy(identity).map(identity) == Lazy(identity).map(identity)
    assert Lazy(identity).map(identity).map(identity) == Lazy(identity).map(identity)
    assert Lazy(identity).map(identity) != Lazy(identity)



# Generated at 2022-06-14 03:32:51.412857
# Unit test for method map of class Lazy
def test_Lazy_map():  # pragma: no cover
    from pymonet.box import Box
    from pymonet.either import Left, Right
    from pymonet.maybe import Nothing, Maybe
    from pymonet.monad_try import Try
    from pymonet.validation import Validation
    from pymonet.writer import Writer


    def add2(a):
        return a + 2

    def div3(a):
        return a / 3

    def is_gt(a):
        return a > 10

    def power2(a):
        return a ** 2

    def compose2(a):
        return compose(add2, power2)(a)

    def error_div_fn(a):
        return a / 0

    def div_fn(a):
        return a / 7


# Generated at 2022-06-14 03:33:00.161977
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    """
    >>> incr = lambda x: x + 1
    >>> add_n_times = lambda n: lambda x: x + n
    >>> x = Lazy.of(1)
    >>> y = Lazy.of(2)
    >>> z = Lazy.of(3)
    >>> r = x.bind(lambda xv: y.bind(lambda yv: z.bind(lambda zv: Lazy.of(xv + yv + zv))))
    >>> r.get()
    6
    >>> x.bind(incr).get()
    2
    >>> x.bind(add_n_times(4)).get()
    5
    """

# Generated at 2022-06-14 03:33:06.380018
# Unit test for method map of class Lazy
def test_Lazy_map():
    # pylint: disable=unused-argument
    def test_function(*args):
        return 'test'

    lazy_value = Lazy(test_function)
    mapped_lazy = lazy_value.map(lambda val: val + '1')
    assert mapped_lazy.get() == 'test1'


# Generated at 2022-06-14 03:33:08.901298
# Unit test for method get of class Lazy
def test_Lazy_get():
    assert Lazy.of(1).get() == 1
    assert Lazy.of(2).get() == 2
    assert Lazy(lambda : 3).get() == 3


# Generated at 2022-06-14 03:33:14.590783
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    assert Lazy.of(1) == Lazy.of(1)
    assert Lazy.of(1) != Lazy.of(2)

    assert Lazy.of(1) != 2
    assert Lazy.of(1) != Lazy.of(lambda: 1)
    assert Lazy.of(lambda: 1) != Lazy.of(lambda: 1)



# Generated at 2022-06-14 03:33:19.486998
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    lazy1 = Lazy(lambda: 3)
    lazy2 = Lazy(lambda: 5)
    lazy3 = lazy1.bind(lambda n: lazy2)
    assert lazy3._compute_value() == lazy2._compute_value()
    assert lazy3.value == lazy2.value
    assert lazy3.is_evaluated == lazy2.is_evaluated



# Generated at 2022-06-14 03:33:27.795777
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():  # pragma: no cover
    assert Lazy(lambda x: x).__eq__(Lazy(lambda x: x))
    assert not Lazy(lambda x: x).__eq__(Lazy(lambda x: x + 1))
    assert not Lazy(lambda x: x).__eq__(Lazy(lambda x, y: x))
    assert not Lazy(lambda x: x).__eq__(Lazy(lambda y: y))
    assert not Lazy(lambda x: x).__eq__(Lazy(lambda y: y))
    assert not Lazy(lambda x: x).__eq__(Lazy(lambda y: y))
    assert not Lazy(lambda x: x).__eq__(2)
    assert not Lazy(lambda x: x).__eq__(None)



# Generated at 2022-06-14 03:33:39.305080
# Unit test for method get of class Lazy
def test_Lazy_get():
    def constructor_fn_1(first_arg, *args):
        return first_arg

    def constructor_fn_2(first_arg, *args):
        return ''.join(args)

    assert str(Lazy.of('1')) == 'Lazy[fn=<function Lazy.<locals>.<lambda> at 0x10bc35378>, value=1, is_evaluated=True]'
    assert Lazy.of('1').get() == '1'

    assert str(Lazy(constructor_fn_1).map(lambda value: value + '2')) == 'Lazy[fn=<function Lazy.map.<locals>.<lambda> at 0x10bc35c18>, value=None, is_evaluated=False]'  # noqa

# Generated at 2022-06-14 03:33:42.539561
# Unit test for method get of class Lazy
def test_Lazy_get():
    # function returning any value
    def func():
        return 1

    # create Lazy with this function
    lazy = Lazy(func)

    assert lazy.get() == 1



# Generated at 2022-06-14 03:33:49.173379
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    from pymonet.functor import id

    lazy_1 = Lazy.of(1)
    lazy_2 = Lazy.of(1)
    lazy_3 = Lazy.of(3).bind(lambda x: lazy_2)
    lazy_4 = Lazy.of(1).bind(lambda x: lazy_2)

    assert lazy_1 == lazy_1
    assert lazy_1 == lazy_2
    assert lazy_1 != lazy_3
    assert lazy_3 == lazy_4



# Generated at 2022-06-14 03:33:59.730490
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    """
    Testing method ap of class Lazy.
    """
    # given
    source1 = Lazy(lambda _: lambda x: x + 1)
    source2 = Lazy(lambda: 1)

    # when
    result = source1.ap(source2)

    # then
    assert result.get() == 2


# Generated at 2022-06-14 03:34:04.412148
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    def add(a, b):
        return a + b

    lazy_add = Lazy.of(add)
    lazy_1 = Lazy.of(1)
    lazy_2 = Lazy.of(2)

    assert lazy_1.ap(lazy_add) == Lazy.of(3)
    assert lazy_2.ap(lazy_add) == Lazy.of(3)

# Generated at 2022-06-14 03:34:08.973611
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    assert Lazy.of(1).bind(lambda v: Lazy.of(v + 1)) == Lazy.of(2)
    assert Lazy.of(1).bind(lambda v: Lazy.of(v + 1)).get() == 2



# Generated at 2022-06-14 03:34:12.711887
# Unit test for method map of class Lazy
def test_Lazy_map():
    lazy = Lazy(lambda: 10)
    lazy2 = lazy.map(lambda x: x + 1)

    assert lazy2.get() == 11



# Generated at 2022-06-14 03:34:23.877644
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.box import Box
    from pymonet.either import Right
    from pymonet.maybe import Maybe
    from pymonet.monad_try import Try
    from pymonet.validation import Validation

    def identity_fn(x):
        return x

    def fn(x):
        return Lazy.of(x)

    def fn1(x):
        return Box(x + 1)

    def fn2(x: Right):
        return x.map(lambda val: val * 2)

    def fn3(x: Maybe):
        return x.map(lambda val: val * 3)

    def fn4(x: Try):
        return x.map(lambda val: val * 4)

    def fn5(x: Validation):
        return x.map(lambda val: val * 5)



# Generated at 2022-06-14 03:34:32.721234
# Unit test for method map of class Lazy
def test_Lazy_map():
    def plus_two(x):
        return x + 2

    def multiply_by_two(x):
        return x * 2

    assert Lazy(plus_two) == Lazy(plus_two)

    assert Lazy(plus_two).map(multiply_by_two) == Lazy(lambda: (plus_two(0) * 2))
    assert Lazy(plus_two).map(multiply_by_two).get(10) == (plus_two(10) * 2)

    assert Lazy(plus_two).fold(lambda x: x) == Lazy(plus_two).map(lambda x: x).fold(lambda x: x)
    assert Lazy(plus_two).fold(lambda x: x) == Lazy(plus_two).map(lambda x: x).fold(lambda x: x)


# Generated at 2022-06-14 03:34:40.465468
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def initial_function(x):
        return x * 10

    def double_function(x):
        return x * 2

    lazy = Lazy(initial_function)
    assert lazy.get(10) == 100

    lazy = lazy.bind(lambda x: Lazy(double_function)).map(lambda x: x + 1)
    assert lazy.get(10) == 201

    # test memoization
    assert lazy.get(10) == 201

    # test __str__ method
    assert str(lazy) == 'Lazy[fn=<lambda>, value=201, is_evaluated=True]'


# Generated at 2022-06-14 03:34:43.680338
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    """
    Test ``Lazy`` class `ap` method
    """
    def function():
        return 2

    assert Lazy(function).ap(Lazy.of(lambda a: a * 2)).get() == 4


# Generated at 2022-06-14 03:34:49.063207
# Unit test for method map of class Lazy
def test_Lazy_map():
    def lazy_int_adder(arg):
        return Lazy.of(lambda x: x + arg)

    lazy_adder = Lazy(lazy_int_adder)
    lazy_result = lazy_adder.map(lambda x: x(5))
    assert lazy_result.get() == 10



# Generated at 2022-06-14 03:34:58.098793
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    """
    Test for method bind of class Lazy
    """
    from pymonet.box import Box
    import pytest

    def divide(a, b):
        if b == 0:
            raise ValueError('Division by zero is undefined')

        return a / b

    def get_result(lazy_fn):
        return lazy_fn(5, 2).to_box()

    lazy_result = Lazy.of(lambda a, b: Lazy.of(divide(a, b)))

    assert get_result(lazy_result).get() == 2.5

    lazy_result = Lazy.of(lambda a, b: Lazy.of(divide(a, b / 2)))

    assert get_result(lazy_result).get() == 5


# Generated at 2022-06-14 03:35:18.591376
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():  # pragma: no cover
    assert Lazy(lambda: 1) == Lazy(lambda: 1)
    assert Lazy(lambda: "str") == Lazy(lambda: "str")
    assert Lazy(lambda: 1) != Lazy(lambda: 2)
    assert Lazy(lambda: "str1") != Lazy(lambda: "str2")
    assert (
        Lazy(lambda: [1, 2]) == Lazy(lambda: [1, 2])
        and Lazy(lambda: [1, 2]) != Lazy(lambda: [2, 1])
    )

# Generated at 2022-06-14 03:35:29.929200
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.validation import Validation

    smart_lazy = Lazy(lambda: Validation.success('1'))
    smart_lazy = smart_lazy.ap(Lazy(lambda: 1))
    smart_lazy = smart_lazy.ap(Lazy(lambda: 1.1))
    smart_lazy = smart_lazy.ap(Lazy(lambda: 2))
    smart_lazy = smart_lazy.ap(Lazy(lambda: []))
    smart_lazy = smart_lazy.ap(Lazy(lambda: {'a': 1}))
    smart_lazy = smart_lazy.ap(Lazy(lambda: {'b': 2}))
    smart_lazy = smart_lazy.ap(Lazy(lambda: ['a', 'b']))
    smart_

# Generated at 2022-06-14 03:35:34.290525
# Unit test for method map of class Lazy
def test_Lazy_map():  # pragma: no cover

    def function(x):
        return x + 3

    result = Lazy.of(1).map(function).get()
    assert result == 1 + 3

    result = Lazy.of(1).map(function).map(function).get()
    assert result == 1 + 3 + 3



# Generated at 2022-06-14 03:35:43.343900
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def test_fn(value):
        return Lazy.of(value + 8)

    assert Lazy.of(4).bind(test_fn).get() == 12
    assert Lazy.of(7).map(test_fn).bind(test_fn).get() == 23
    assert Lazy.of(7).bind(test_fn).bind(test_fn).get() == 23
    assert Lazy.of(7).map(test_fn).map(test_fn).get() == 23



# Generated at 2022-06-14 03:35:50.721630
# Unit test for method map of class Lazy
def test_Lazy_map():  # pragma: no cover
    def add_one(n: int) -> int:
        return n + 1

    x1 = Lazy(lambda: add_one(10)).map(lambda x: x * 2).get()
    assert x1 == 22

    def concat(a: str, b: str) -> str:
        return a + b

    x2 = Lazy(lambda: concat('Hello', ' World!')).map(lambda x: x + ' ').get()
    assert x2 == 'Hello World! '



# Generated at 2022-06-14 03:35:53.157706
# Unit test for method map of class Lazy
def test_Lazy_map():
    assert Lazy.of(2).map(lambda x: x + 1).get() == 3



# Generated at 2022-06-14 03:36:03.474851
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    assert (Lazy.of(1).bind(lambda x: Lazy.of(x + 1)).get() == 2)
    assert (Lazy.of(1).bind(lambda x: Lazy.of(x + 1)).to_box().get() == 2)
    assert (Lazy.of(1).bind(lambda x: Lazy.of(x + 1)).to_maybe().get() == 2)
    assert (Lazy.of(1).bind(lambda x: Lazy.of(x + 1)).to_try().get() == 2)
    assert (Lazy.of(1).bind(lambda x: Lazy.of(x + 1)).to_validation().get() == 2)

# Generated at 2022-06-14 03:36:10.087632
# Unit test for method map of class Lazy
def test_Lazy_map():
    from pymonet.chain import Chain, ChainItem

    test_value = 1
    test_lazy_map = Lazy.of(test_value)

    test_transformed_lazy = test_lazy_map.map(lambda x: x + 1)
    assert test_lazy_map != test_transformed_lazy

    test_transformed_value = test_transformed_lazy.get(test_value)
    assert test_transformed_value == test_value + 1


# Generated at 2022-06-14 03:36:16.684551
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    assert Lazy(lambda _: 0) == Lazy(lambda _: 0)
    assert Lazy(lambda _: 0).bind(lambda x: Lazy(lambda _: x + 1)) == Lazy(lambda _: 0).bind(lambda x: Lazy(lambda _: x + 1))
    assert Lazy(lambda _: 0).map(lambda x: x + 1) == Lazy(lambda _: 0).map(lambda x: x + 1)
    assert Lazy(lambda _: 0).ap(Lazy(lambda _: lambda x: x + 1)) == Lazy(lambda _: 0).ap(Lazy(lambda _: lambda x: x + 1))
    assert Lazy(lambda _: 0) != 0

# Generated at 2022-06-14 03:36:25.522210
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def inc(a):
        return a + 1

    def dec(a):
        return a - 1

    def bind_fn(value):
        return Lazy.of(value).map(inc)

    def f(a):
        return dec(a)

    # Lazy(f).bind(g) = Lazy(f(g))
    # Lazy(f).bind(Lazy.of) = Lazy(f(Lazy.of)) = Lazy(f)
    assert Lazy(f).bind(bind_fn) == Lazy(f).map(inc)
    assert Lazy(f).bind(Lazy.of) == Lazy(f)

    def f(a):
        return dec(a)

    def g(a):
        return inc(a)


# Generated at 2022-06-14 03:36:52.010399
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    assert Lazy.of(0).bind(lambda x: Lazy.of(x + 1)).bind(lambda x: Lazy.of(x * x)) == Lazy.of(1).bind(lambda x: Lazy.of(x * x))

# Generated at 2022-06-14 03:36:54.133972
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    assert Lazy(lambda x: x + 1).bind(lambda x: Lazy(lambda: x + 2)).get(1) == 4

# Generated at 2022-06-14 03:37:04.942210
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    """ Unit test of Lazy.__eq__ method """
    def fn(arg: int) -> str:
        return str(arg)

    lazy1 = Lazy(fn).map(lambda x: 'Lazy: {}'.format(x)).bind(lambda x: Lazy(lambda arg: '{}!'.format(x)))
    lazy2 = Lazy(fn).map(lambda x: 'Lazy: {}'.format(x)).bind(lambda x: Lazy(lambda arg: '{}!'.format(x)))
    lazy3 = Lazy(fn).map(lambda x: 'Lazy: {}'.format(x)).bind(lambda x: Lazy(lambda arg: '{}'.format(x)))

    assert lazy1 == lazy2
    assert lazy1 != lazy3

# Generated at 2022-06-14 03:37:15.167216
# Unit test for method map of class Lazy
def test_Lazy_map():
    from pymonet.box import Box
    from pymonet.either import Right
    from pymonet.maybe import Maybe
    from pymonet.monad_try import Try
    from pymonet.validation import Validation

    assert Lazy.of(1).map(lambda x: x * 2) == Lazy(lambda: 1 * 2)
    assert Lazy.of(1).map(lambda x: x + 2) == Lazy(lambda: 1 + 2)
    assert Lazy.of(1).map(lambda x: x ** 2) == Lazy(lambda: 1 ** 2)
    assert Lazy.of(1).map(lambda x: x / 2) == Lazy(lambda: 1 / 2)
    assert Lazy.of(1).map(lambda x: x - 2) == Lazy(lambda: 1 - 2)

# Generated at 2022-06-14 03:37:23.310972
# Unit test for method map of class Lazy
def test_Lazy_map():  # pragma: no cover
    def mul(*args):
        return args[0] * args[1]

    lazy_mul = Lazy.of(mul)
    lazy_result = lazy_mul.map(lambda x: x(2, 3))

    assert lazy_result.get() == 6

    lazy_mul_2 = Lazy.of(mul)
    lazy_result_2 = lazy_mul_2.map(lambda x: x(2, 3))

    # check memoization
    assert lazy_result_2.get() == 6

# Generated at 2022-06-14 03:37:34.070433
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.numbers import Number

    def ap_test(a, b):
        return a + b

    assert (Number(1) | Lazy.of | Lazy.of).ap(Lazy.of(ap_test)) == Lazy.of(ap_test(1, 1))
    assert (Number(1) | Lazy.of | Lazy.of).ap(Lazy.of(ap_test)).get() == ap_test(1, 1)
    assert (Number(1) | Lazy.of | Lazy.of).ap(Number(1) | Lazy.of).get() == ap_test(1, 1)
    assert (Number(1) | Lazy.of | Lazy.of).ap(Number(1) | Lazy.of).get() == ap_test(1, 1)

#

# Generated at 2022-06-14 03:37:40.267980
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def divide_by(n):
        def divide_by_n(x):  # pragma: no cover
            return x / n

        return divide_by_n

    if Lazy.of(10).bind(divide_by(2)).get() != 5 or Lazy.of(10).bind(divide_by(0)).get() != 0:
        raise AssertionError('test_Lazy_bind')

# Generated at 2022-06-14 03:37:47.545358
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def add2(x):
        return Lazy(lambda x: x + 2)

    assert Lazy(lambda x: x).bind(add2).get(2) == 4
    assert Lazy(lambda x: x).bind(add2).get(2) == 4
    assert Lazy(lambda x: x).bind(add2).get(2) == 4
    assert Lazy(lambda x: x).bind(add2).get(2) == 4
    assert Lazy(lambda x: x).bind(add2).get(2) == 4


# Generated at 2022-06-14 03:37:49.338770
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    assert Lazy.of(1).bind(lambda x: Lazy.of(x + 2)).constructor_fn() == 3



# Generated at 2022-06-14 03:37:52.125584
# Unit test for method map of class Lazy
def test_Lazy_map():
    def test_method(x):
        return x % 2 == 0

    lazy_input = Lazy(test_method)
    lazy_result = lazy_input.map(lambda x: x * 3)
    assert lazy_result(6) == True



# Generated at 2022-06-14 03:38:23.564272
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    fn = Lazy(lambda x: x + 1)
    assert fn.ap(Lazy.of(5)) == Lazy.of(6)

    fn = Lazy(lambda x: x + 1)
    assert fn.ap(Lazy.of(5)) == Lazy(lambda: 6)

    fn = Lazy(lambda x: x + 1)
    assert str(fn.ap(Lazy.of(5))) == 'Lazy[fn=<function Lazy.<locals>.lambda_fn at 0x7f5d6c5c6e18>, value=None, is_evaluated=False]'  # noqa


# Generated at 2022-06-14 03:38:26.263664
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    value = Lazy.of(1)
    value2 = value.bind(lambda x: Lazy.of(x + 1)).bind(lambda x: Lazy.of(x + 2))
    assert value2.get(2) == 4

# Generated at 2022-06-14 03:38:31.434874
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    def f(x):
        return x + 1

    def g(x):
        return x - 1

    assert Lazy(f).ap(Lazy(g)).get(10) == 10
    assert Lazy(f).ap(Lazy(f)).ap(Lazy(g)).get(10) == 11

# Generated at 2022-06-14 03:38:42.260757
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.multimethod import multimethod
    from pymonet.monad_maybe import Maybe, NoneType

    @multimethod
    def foo(): return None

    def fn(x): return x + 10

    assert Lazy.of(2).ap(Lazy.of(fn)) == Lazy.of(12)

    assert Lazy.of(2).ap(Maybe.just(fn)) == Lazy.of(12)

    assert Lazy.of(2).ap(Maybe.none()) == Lazy.of(None)

    assert Lazy.of(None).ap(Maybe.just(fn)) == Lazy.of(None)

    assert Lazy.of(None).ap(Maybe.none()) == Lazy.of(None)

    assert Lazy.of(None).ap(Lazy.of(fn))

# Generated at 2022-06-14 03:38:44.162643
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def add_one(value):
        return Lazy.of(value + 1)

    def divide_by_two(value):
        return Lazy.of(value / 2)

    subject = Lazy.of(10)
    result = subject.bind(add_one).bind(divide_by_two)

    assert result.get() == 6, 'Should return 6'

# Generated at 2022-06-14 03:38:47.696318
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.either import Right, Left

    def add(a):
        return a + 5

    assert (Lazy(lambda: 1).to_either().ap(Lazy(lambda: add)) == Right(6))



# Generated at 2022-06-14 03:38:56.616822
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    # GIVEN
    a = Lazy.of(5)
    add_5 = Lazy.of(lambda x: x + 5)

    # WHEN
    b = Lazy.of(None).ap(add_5)

    # THEN
    assert b.constructor_fn() == 10
    assert b.is_evaluated is False

    # WHEN
    b2 = a.ap(add_5)

    # THEN
    assert b2.constructor_fn() == 10
    assert b2.is_evaluated is False

# Generated at 2022-06-14 03:39:01.805071
# Unit test for method map of class Lazy
def test_Lazy_map():
    inc = lambda x: x + 1
    double = lambda x: x * 2

    assert Lazy(lambda x: x + 1).map(double).get(3) == 8
    assert Lazy(inc).map(double).get(3) == 8

    assert Lazy(inc).map(double) == Lazy(inc).map(double)
    assert Lazy(inc).map(double) != Lazy(inc).map(lambda x: x * 2 + 1)
    assert Lazy(inc).map(double) != Lazy(lambda x: x + 1)



# Generated at 2022-06-14 03:39:06.805803
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def lazy_fn(value):
        return value + 1
    def pure_fn(value):
        return Lazy.of(value)
    lazy = Lazy.of(10)
    assert lazy.bind(lazy_fn).constructor_fn(None) == 11
    assert lazy.bind(pure_fn).constructor_fn(None) == 10


# Generated at 2022-06-14 03:39:14.050662
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():  # pragma: no cover
    assert Lazy.of(1) == Lazy.of(1)
    assert Lazy.of(1) != Lazy.of(2)
    assert Lazy.of(1) != Lazy.of("1")
    assert Lazy.of(1) != 1
    assert Lazy.of(1) != None

# Generated at 2022-06-14 03:40:12.106725
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.box import Box
    from pymonet.either import Right
    from pymonet.maybe import Maybe
    from pymonet.monad_try import Try
    from pymonet.validation import Validation

    lazy_successful = Lazy(lambda v: True)
    assert lazy_successful.bind(lambda value: Box(value)).to_box()
    assert lazy_successful.bind(lambda _: None).to_box()
    assert lazy_successful.bind(lambda value: Right(value)).to_either()
    assert lazy_successful.bind(lambda _: None).to_either()
    assert lazy_successful.bind(lambda value: Maybe.just(value)).to_maybe()
    assert lazy_successful.bind(lambda _: None).to_maybe()

# Generated at 2022-06-14 03:40:14.869506
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    assert Lazy(lambda: 123).bind(lambda x: Lazy(lambda: x * x)).get() == 123 * 123

# Generated at 2022-06-14 03:40:17.225075
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from tests.monad_tests.test_either import test_Either_return_method

    def inner(x):
        return test_Either_return_method(x + 5)

    def outer(x):
        return Lazy.return_(x).bind(inner)

    assert outer(5).get() == 10
    assert outer(42).to_maybe().get_or_else(0) == 47
    assert outer(42).to_box().get() == 47
    assert outer(42).to_validation().get() == 47

# Generated at 2022-06-14 03:40:21.641806
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    import pymonet.reader_writer as Lazy

    assert Lazy.of(1).ap(Lazy.of(lambda v: v + 1)).to_box(0) == Lazy.of(2).to_box(0)



# Generated at 2022-06-14 03:40:25.345300
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.identity import Identity

    def inc(value: int) -> int: return value + 1

    assert Lazy.of(1).ap(Identity(inc)) == Lazy.of(2)


# Generated at 2022-06-14 03:40:31.168789
# Unit test for method map of class Lazy
def test_Lazy_map():
    def lazy_fn(value: str) -> str:
        return value

    def upper_fn(value: str) -> str:
        return value.upper()

    lazy = Lazy(lazy_fn)
    lazy_mapped = lazy.map(upper_fn)

    assert len(lazy_mapped.to_try().get_errors()) > 0

    assert lazy_mapped.get('value') == upper_fn(lazy_fn('value'))
    assert lazy_mapped.get('value') == 'VALUE'


# Generated at 2022-06-14 03:40:35.325875
# Unit test for method map of class Lazy
def test_Lazy_map():
    # GIVEN
    fn = lambda x: x + 1
    lazy = Lazy(fn)

    # WHEN
    mapped_lazy = lazy.map(fn)

    # THEN
    assert mapped_lazy._compute_value(10) == 21


# Generated at 2022-06-14 03:40:39.298269
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    assert Lazy.of(lambda x: x + 1).ap(Lazy.of(1)) == Lazy.of(2)
    assert Lazy.of(lambda x: x + 1).ap(Lazy.of(None)) == Lazy.of(None)


# Generated at 2022-06-14 03:40:45.709729
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.box import Box
    from pymonet.either import Right

    identity = lambda x: Lazy.of(x)
    assert Lazy(lambda x: x * 2).bind(identity).get(1) == Lazy(lambda x: x * 2).get(1)
    assert Lazy(lambda x: x * 2).bind(Box.of).get(1) == Box(Lazy(lambda x: x * 2).get(1))
    assert Lazy(lambda x: x * 2).bind(Right.of).get(1) == Right(Lazy(lambda x: x * 2).get(1))

# Generated at 2022-06-14 03:40:52.032752
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from nose.tools import assert_equal

    def fn(value: int) -> Lazy:
        return Lazy(lambda *args: Lazy(lambda *args: value + 1))

    lazy = Lazy(lambda *args: 10)
    result = lazy.bind(fn)
    result.get()
    assert_equal(result, Lazy(lambda *args: Lazy(lambda *args: 11)))

