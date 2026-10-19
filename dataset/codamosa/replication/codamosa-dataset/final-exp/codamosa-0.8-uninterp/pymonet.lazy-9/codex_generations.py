

# Generated at 2022-06-14 03:31:32.645069
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    from pymonet.box import Box
    from pymonet.either import Right
    from pymonet.maybe import Just
    from pymonet.monad_try import Success
    from pymonet.validation import Valid

    assert Lazy.of(1) == Lazy.of(1)
    assert Lazy.of(1) == Lazy(lambda: 1)
    assert Lazy(lambda: 1) == Lazy(lambda: 1)
    assert Lazy.of(1) == Box(1)
    assert Lazy.of(1) == Right(1)
    assert Lazy.of(1) == Just(1)
    assert Lazy.of(1) == Success(1)
    assert Lazy.of(1) == Valid(1)



# Generated at 2022-06-14 03:31:45.469592
# Unit test for method map of class Lazy
def test_Lazy_map():
    def add(x, y):
        return x + y

    l = Lazy(lambda: 2)
    assert l.map(lambda x: x + 3).get() == 5

    l = Lazy(lambda: 3)
    assert l.map(lambda x: x * 2).get() == 6

    l = Lazy(lambda: [1, 2, 3])
    assert l.map(lambda x: map(lambda y: y * 2, x)).get() == [2, 4, 6]

    l = Lazy(lambda: 'hello')
    assert l.map(lambda x: x + ' ').get() == 'hello '

    l = Lazy(lambda: {'x': 1})
    assert l.map(lambda x: x.get('x')).get() == 1

    l = Lazy(lambda: 3)

# Generated at 2022-06-14 03:31:54.105610
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    from pymonet.functor import Functor
    from pymonet.monoid import Monoid


    def func():
        return 5


    def func1(arg):
        return arg + 5


    def func2(arg):
        return arg - 5


    def func3(arg):
        return arg * 5


    def func4(arg):
        return arg / 5


    class MonoidImpl(Monoid):
        def __init__(self, value, func):
            self.value = value
            self.func = func

        @classmethod
        def zero(cls):
            return MonoidImpl(0, None)

        def __add__(self, other):
            return MonoidImpl(self.value + other.value, self.func)


# Generated at 2022-06-14 03:32:04.736595
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    def add(x):
        return x + 100

    lazy1 = Lazy(add)
    lazy2 = Lazy(add)

    assert lazy1.__eq__(lazy2)

    assert not lazy1.__eq__(Lazy(lambda x: x + 1))
    assert not lazy1.__eq__(Lazy(lambda x, y: x - y))
    assert not lazy1.__eq__(Lazy(lambda x, y, z: x * y * z))

    def add_and_multiply(x, y, z):
        return x + y * z

    lazy1 = Lazy(add_and_multiply)
    lazy2 = Lazy(add_and_multiply)

    assert lazy1.__eq__(lazy2)


# Generated at 2022-06-14 03:32:11.717600
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    # create some values
    def func(x):
        return x

    def other_func():
        return 0

    lazy = Lazy(func)
    lazy2 = Lazy(func)
    lazy3 = Lazy(other_func)

    # check equality, before fold call
    assert lazy == lazy
    assert lazy == lazy2
    assert lazy != lazy3

    # check equality, after fold call
    lazy.get(1)
    lazy2.get(1)
    lazy3.get(1)

    assert lazy == lazy
    assert lazy == lazy2
    assert lazy != lazy3



# Generated at 2022-06-14 03:32:13.033027
# Unit test for method get of class Lazy
def test_Lazy_get():  # pragma: no cover
    assert Lazy.of(2).get() == 2

# Generated at 2022-06-14 03:32:17.081511
# Unit test for method bind of class Lazy
def test_Lazy_bind():  # pragma: no cover
    def pi_plus(value):
        def pi_plus_lambda(pi):
            return pi + value

        return Lazy(pi_plus_lambda)

    assert Lazy.of(3.14).bind(pi_plus(1)).get() == 4.14


# Generated at 2022-06-14 03:32:19.151609
# Unit test for method map of class Lazy
def test_Lazy_map():
    assert Lazy.of(1).map(add(1)).get() == 2


# Generated at 2022-06-14 03:32:30.624799
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.box import Box
    from pymonet.either import Either
    from pymonet.maybe import Maybe
    from pymonet.monad_try import Try
    from pymonet.validation import Validation

    def add(a, b):
        return a + b

    value1 = Lazy(lambda: 1)
    value2 = Lazy(lambda: 2)

    assert value1.ap(value2).get() == 3
    assert value1.ap(value2).to_box().get() == 3
    assert value1.ap(value2).to_either().get() == 3
    assert value1.ap(value2).to_maybe().get() == 3
    assert value1.ap(value2).to_try().get() == 3


# Generated at 2022-06-14 03:32:41.191896
# Unit test for method get of class Lazy
def test_Lazy_get():  # pragma: no cover
    assert Lazy(lambda: 'a').get() == 'a'
    assert Lazy(lambda: 'a').get() == 'a'
    assert Lazy(lambda _arg: 'a').get('_arg') == 'a'
    assert Lazy(lambda _arg: 'a').get('_arg') == 'a'
    assert Lazy(lambda: 'a').get('_arg') == 'a'
    assert Lazy(lambda: 'a').get('_arg') == 'a'
    assert Lazy(lambda _arg: _arg).get('_arg') == '_arg'
    assert Lazy(lambda _arg: _arg).get('_arg') == '_arg'

# Generated at 2022-06-14 03:32:48.439433
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def mul_by_2(arg) -> Lazy[int, int]:
        def lambda_fn():
            return arg * 2

        return Lazy(lambda_fn)

    assert Lazy.of(1).bind(mul_by_2).get() == 2

# Generated at 2022-06-14 03:32:54.993344
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    value = 'value'
    value2 = 'value2'

    def function(value):
        return Lazy(lambda: value)

    def function2(value):
        return Lazy(lambda: value)

    assert Lazy.of(value).bind(function).get() == value
    assert Lazy.of(value).bind(function2).get() == value
    assert Lazy.of(value).bind(function).bind(function2).get() == value2

# Generated at 2022-06-14 03:33:00.449944
# Unit test for method get of class Lazy
def test_Lazy_get():
    """
    Testcase description:
        Tests that Lazy[A, B] call passed function and return constructed value.
    """
    result = Lazy(lambda x: '{}'.format(x)).get('lazy')
    assert 'lazy' == result


# Generated at 2022-06-14 03:33:05.250206
# Unit test for method get of class Lazy
def test_Lazy_get():
    assert Lazy(lambda x: x ** 2).get(2) == 4
    assert Lazy(lambda x: x ** 2).get(2) == Lazy(lambda x: x ** 2).get(2)


# Generated at 2022-06-14 03:33:15.927049
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    from pymonet.functor import Functor
    from pymonet.monad import Monad
    from pymonet.apply import Apply

    assert Monad.law_left_identity(Lazy, lambda fn: Lazy.bind(fn))
    assert Monad.law_right_identity(Lazy, lambda value: Lazy.of(value))

    assert Functor.law_identity(Lazy, lambda value: Lazy.of(value))
    assert Functor.law_composition(Lazy, lambda value, fn_1, fn_2: Lazy.of(value).map(fn_1).map(fn_2))


# Generated at 2022-06-14 03:33:17.360794
# Unit test for method get of class Lazy
def test_Lazy_get():
    assert Lazy.of(1).get() == 1



# Generated at 2022-06-14 03:33:23.121982
# Unit test for method bind of class Lazy
def test_Lazy_bind():  # pragma: no cover
    from pymonet import Maybe, MaybeError

    res = Maybe.just(12).fold(
        lambda: None,
        lambda x: x,
    )

    def maybe_transform(x):
        if x < 10:
            return Maybe.just(x + 10)
        else:
            return Maybe.just(x)

    lazy_calc = Maybe.just(12).bind(maybe_transform)

    assert lazy_calc.get() == res

# Generated at 2022-06-14 03:33:28.432301
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.monad_list import List

    add = lambda a, b: a + b
    lazy_value = Lazy.of(5)
    ap_lazy = Lazy.of(lambda a, b: add(a, b))  # function of adding 2 int
    lazy_sum = lazy_value.ap(ap_lazy)
    assert lazy_sum.get(10) == 15

    add_lazy = Lazy.of(lambda a: lambda b: a + b)  # function of adding 2 int
    ap_lazy = add_lazy.ap(Lazy.of(5))
    assert ap_lazy.get(10) == 15

    append_to_list = lambda lst, txt: lst + [txt]

# Generated at 2022-06-14 03:33:33.636913
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    _value = Lazy(lambda: 7).bind(lambda number: Lazy(lambda: number + 5))
    assert _value.is_evaluated == True
    assert _value.value == 12
    assert _value.get() == 12


# Generated at 2022-06-14 03:33:44.222217
# Unit test for method get of class Lazy
def test_Lazy_get():  # pragma: no cover
    def test_function():
        print('function called')
        return 5

    lazy_test = Lazy(test_function)

    assert lazy_test.is_evaluated is False
    assert lazy_test.value is None
    assert lazy_test.get() == 5
    assert lazy_test.is_evaluated is True
    assert lazy_test.value == 5

    lazy_test1 = Lazy(lambda x: x)
    assert lazy_test1.get(5) == 5

    lazy_test2 = Lazy(lambda x, y: x + y)
    assert lazy_test2.get(5, 6) == 11



# Generated at 2022-06-14 03:33:53.841878
# Unit test for method get of class Lazy
def test_Lazy_get():
    """
    Test for get method of Lazy
    """
    assert Lazy.of(1).get() == Lazy(lambda: 1).get() == 1
    assert Lazy(lambda x: x).get(1) == 1
    assert Lazy(lambda x, y: x + y).get(1, 2) == 3


# Generated at 2022-06-14 03:33:57.659558
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    lazy = Lazy(lambda x: x + 1).map(abs).bind(lambda x: Lazy(lambda y: x + y))
    assert lazy.get(1, 1) == 3



# Generated at 2022-06-14 03:33:59.804315
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    lazy1 = Lazy(lambda : 1)
    lazy2 = Lazy(lambda x: x + 1)
    assert lazy1.ap(lazy2).get() == 2



# Generated at 2022-06-14 03:34:02.121575
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    assert(Lazy.of("hello").bind(lambda x: Lazy.of("world")).get() == "world")


# Generated at 2022-06-14 03:34:12.858077
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def test_function(argument):
        return Lazy.of(argument)

    assert Lazy.of(42).bind(test_function).get() == 42
    assert Lazy.of('test').bind(test_function).get() == 'test'
    assert Lazy.of({'key': 'value'}).bind(test_function).get() == {'key': 'value'}
    assert Lazy.of([1, 2, 3, 4]).bind(test_function).get() == [1, 2, 3, 4]
    assert Lazy.of(range(0, 1)).bind(test_function).get() == range(0, 1)


# Generated at 2022-06-14 03:34:17.209609
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    class HasLazy(Generic[T, U]):
        def __init__(self, lazy_fn: Lazy[T, U]) -> None:
            self.lazy_fn = lazy_fn

    result = HasLazy(Lazy(lambda: 2)).lazy_fn.bind(lambda x: Lazy(lambda: x + 3))

    assert result.get() == 5

# Generated at 2022-06-14 03:34:20.454054
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    """
    Unit test for method bind of class Lazy.
    """

    def mapper(value):
        return Lazy.of(value)

    assert Lazy(lambda: 10).bind(mapper).constructor_fn() == Lazy(lambda: 10).get()



# Generated at 2022-06-14 03:34:23.924077
# Unit test for method get of class Lazy
def test_Lazy_get():  # pragma: no cover
    assert Lazy.of(5).get() == 5
    assert Lazy(lambda: 5).get() == 5



# Generated at 2022-06-14 03:34:28.449925
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    import pymonet

    l = Lazy(lambda *args: pymonet.Maybe(2))
    m = Lazy(lambda *args: pymonet.Maybe(lambda x: x + 1))

    v = l.ap(m)

    assert v.get() == pymonet.Maybe(3)



# Generated at 2022-06-14 03:34:39.769409
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.box import Box

    def function_1(a: int) -> int:
        return a * 2

    def function_2(b: int) -> int:
        return b * 3

    def function_3(c: int) -> int:
        return c + 5

    def function_4(d: int) -> Box[int]:
        return Box(d * 11)

    lazy_1 = Lazy.of(function_1)
    lazy_2 = Lazy.of(function_2)
    lazy_3 = Lazy.of(function_3)
    lazy_4 = Lazy.of(function_4)

    assert lazy_1.ap(lazy_2).ap(Lazy.of(3)) == Lazy.of(3).ap(lazy_2).ap(lazy_1)

# Generated at 2022-06-14 03:34:50.633201
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.functor import identity

    assert Lazy.of(1).bind(identity) == Lazy.of(1)

    assert Lazy(lambda: 1).bind(identity) == Lazy.of(1)

    assert Lazy(lambda: 1).bind(lambda x: Lazy.of(x + 1)) == Lazy.of(2)

    assert Lazy(lambda: 1).bind(lambda x: Lazy(lambda: x + 1)) == Lazy.of(2)

    assert Lazy(lambda: 1).map(lambda x: x + 1).bind(identity) == Lazy.of(2)

# Generated at 2022-06-14 03:34:54.803596
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    assert Lazy(lambda x: x).map(lambda x: 1).ap(Lazy.of(lambda x: 1)).__eq__(Lazy(lambda x: x).map(lambda x: 1).ap(Lazy.of(lambda x: 1))) is True


# Generated at 2022-06-14 03:35:07.019830
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    """
    Test that verify correctness of method __eq__ in class Lazy

    """
    class TestClass():
        def __init__(self):
            self.prop = 1

        def get_prop(self):
            self.prop += 1
            return self.prop

    assert Lazy(lambda x: x + 1) == Lazy(lambda x: x + 1)
    assert Lazy(lambda x: x + 1) != Lazy(lambda x: x)
    instance = TestClass()
    assert Lazy(instance.get_prop) != Lazy(instance.get_prop)
    assert Lazy(instance.get_prop).get(10) != Lazy(instance.get_prop).get(10)
    assert Lazy(instance.get_prop).get(10) == Lazy(instance.get_prop)
    assert L

# Generated at 2022-06-14 03:35:19.421923
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    """
    Check __eq__ method of Lazy.

    :returns: True when test passed else raise AssertionError exception
    :rtype: bool
    """
    fn_1 = lambda x: x
    fn_2 = lambda x: x + 1
    lazy_1 = Lazy(fn_1)
    lazy_2 = Lazy(fn_1)
    lazy_3 = Lazy(fn_2)
    assert lazy_1 != lazy_3
    assert lazy_1 == lazy_2
    assert not lazy_2.is_evaluated
    assert not lazy_3.is_evaluated
    assert lazy_1 != lazy_3
    assert lazy_2 == lazy_1
    assert lazy_1.get(1) == 1
    assert lazy_2.get(1) == 1
    assert lazy_3.get

# Generated at 2022-06-14 03:35:25.618258
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.maybe import Maybe

    assert Lazy.of(2).ap(Maybe.of(lambda x: x + 1)) == Maybe.of(3)
    assert Lazy.of(2).ap(Maybe.of(lambda x: None)) == Maybe.of(None)
    assert Lazy.of(2).ap(Maybe.to_nothing()) == Maybe.to_nothing()


# Generated at 2022-06-14 03:35:33.914194
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.box import Box
    from pymonet.validation import Validation

    def bind_fn(value: float) -> Lazy[float, float]:
        return Lazy.of(value ** 2)

    assert Lazy.of(2).bind(bind_fn) == Lazy.of(4)
    assert Lazy.of(3).bind(bind_fn) == Lazy.of(9)
    assert Lazy.of(1).bind(lambda value: Box.of(value)).bind(lambda box: Validation.success(box.get())) == Validation.success(1)


# Generated at 2022-06-14 03:35:36.037119
# Unit test for method get of class Lazy
def test_Lazy_get():
    l = Lazy(lambda x: x)
    l._compute_value(1)
    l._compute_value(2)
    assert l.get(1) == 1

# Generated at 2022-06-14 03:35:40.849546
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():  # pragma: no cover
    """
    Test of method __eq__ of class Lazy
    """
    assert Lazy(lambda x: x).__eq__(Lazy(lambda x: x)) is True
    assert Lazy(lambda x: x).__eq__('other') is False


# Generated at 2022-06-14 03:35:48.033705
# Unit test for method get of class Lazy
def test_Lazy_get():
    lazy = Lazy(lambda: 42)
    assert lazy.get() == 42
    lazy = Lazy(lambda: 'Hello, World!')
    assert lazy.get() == 'Hello, World!'
    lazy = Lazy(lambda x: x + 1)
    assert lazy.get(1) == 2
    lazy = Lazy(lambda x: x + ' Hello, World!')
    assert lazy.get('Hello, ') == 'Hello,  Hello, World!'



# Generated at 2022-06-14 03:35:56.547598
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    import pytest

    def test_equal_and_not_evaluated():
        assert Lazy.of(1) == Lazy.of(1)
        assert Lazy.of(1) != Lazy.of(2)

    def test_equal_and_evaluated():
        assert Lazy(lambda: 1).get() == Lazy(lambda: 1).get()
        assert Lazy(lambda: 1).get() != Lazy(lambda: 2).get()

    def test_unequal_and_not_evaluated():
        assert Lazy.of(1) != Lazy.of(2)

    def test_unequal_and_evaluated():
        assert Lazy(lambda: 1).get() != Lazy(lambda: 2).get()


# Generated at 2022-06-14 03:36:12.445033
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def twice(x):
        return Lazy(lambda: x + x)

    def add(x, y):
        return Lazy(lambda: x + y)

    assert str(Lazy.of(1).bind(twice).bind(add)) == 'Lazy[fn=<function Lazy.__init__.<locals>.<lambda> at 0x7f99a8796950>, value=None, is_evaluated=False]'

# Generated at 2022-06-14 03:36:16.941354
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    """
    Test for method Lazy.bind.
    This method return new Lazy depends from stored function.
    """
    def _constructor():
        return 'foo'

    def _mapper(_):
        return 'bar'

    lazy = Lazy(_constructor)

    lazy_mapped = lazy.bind(
        lambda arg: Lazy(_mapper)
    )

    assert _constructor() == 'foo'
    assert _mapper('foo') == 'bar'
    assert lazy_mapped.get() == 'bar'


# Generated at 2022-06-14 03:36:20.280183
# Unit test for method map of class Lazy
def test_Lazy_map():
    assert Lazy(lambda x: x * 2).map(lambda x: x + 2) == Lazy(lambda x: x * 2 + 2)



# Generated at 2022-06-14 03:36:25.690369
# Unit test for method map of class Lazy
def test_Lazy_map():
    assert (
        Lazy(lambda: 'value')
        .map(lambda v: v + '_mapped')
        .to_try()
        .map(lambda v: v.get())
        .get() == 'value_mapped'
    )



# Generated at 2022-06-14 03:36:29.883878
# Unit test for method ap of class Lazy
def test_Lazy_ap():  # pragma: no cover
    from pymonet.fun import add

    lazy = Lazy.of(2)
    applicative = Lazy.of(add)
    assert lazy.ap(applicative).get(3) == 5

# Generated at 2022-06-14 03:36:40.536706
# Unit test for method bind of class Lazy
def test_Lazy_bind():

    def fn(value):
        return Lazy.of(value + 1)

    lazy = Lazy.of(1)
    assert lazy.bind(fn).get() == 2

    def fn1(value):
        return Lazy.of(value)

    lazy = Lazy.of(1)
    assert lazy.bind(fn1).get() == 1

    def fn2(value):
        return Lazy.of(value + 1)

    def fn3(value):
        return Lazy.of(value + 2)

    lazy = Lazy.of(1)
    assert lazy.bind(fn2).bind(fn3).get() == 4

    def fn4(value):
        return Lazy.of(value + 1)

    def fn5(value):
        return Lazy.of(value)

    lazy = Lazy

# Generated at 2022-06-14 03:36:46.562910
# Unit test for method map of class Lazy
def test_Lazy_map():
    add_one = lambda a: a + 1
    add_1 = Lazy(add_one)

    add_two = lambda a: a + 2
    add_2 = add_1.map(add_two)

    assert add_2.get(0) == 2
    assert add_2.to_maybe(0) == Maybe.just(2)



# Generated at 2022-06-14 03:36:52.473403
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    input_1 = 5
    input_2 = 10
    lazy_with_function = Lazy(lambda x: x*x)
    sum_function = lambda x: Lazy(lambda y: x + y)
    result = lazy_with_function.bind(sum_function).get(input_1, input_2)
    assert result == 50, "result should be 25"



# Generated at 2022-06-14 03:36:59.166319
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    def add(a):
        def fn(x):
            return a + x
        return fn

    lazy_fn = Lazy(add)
    lazy_x = Lazy(lambda: 2)
    lazy_y = Lazy(lambda: 3)

    assert lazy_x.ap(lazy_fn).get() == 5
    assert lazy_fn.ap(lazy_x).get() == 2

    lazy_fn.ap(lazy_fn).ap(lazy_x).ap(lazy_y).get() == 7

    lazy_fn2 = Lazy(lambda: 100)
    assert lazy_fn.ap(lazy_fn2).get() == 100



# Generated at 2022-06-14 03:37:02.988035
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    result_lazy = Lazy.of(1).map(lambda x: x + 1).ap(Lazy.of(lambda x: x+1)).map(lambda x: x+1)
    assert result_lazy.get() == 5



# Generated at 2022-06-14 03:37:16.499546
# Unit test for method map of class Lazy
def test_Lazy_map():
    def square(number: int) -> int:
        return number ** 2

    assert Lazy(lambda x: square(x)).map(lambda x: x + 1).get(2) == 5
    assert Lazy(lambda x: square(x)).map(lambda x: x + 1).get(3) == 10
    assert Lazy(lambda x: square(x)).map(lambda x: x + 1).get(4) == 17



# Generated at 2022-06-14 03:37:17.012006
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    pass

# Generated at 2022-06-14 03:37:22.871695
# Unit test for method map of class Lazy
def test_Lazy_map():
    def add_one(x):
        return x + 1

    def double(x):
        return x * 2

    def triple(x):
        return x * 3

    lazy = Lazy.of(0)
    assert lazy.map(add_one).map(double).map(triple).get() == 6



# Generated at 2022-06-14 03:37:26.304985
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def concat(n, m):
        return Lazy(lambda *_: n + m)

    value = Lazy.of(5).bind(lambda n: concat(n, 3)).get()
    assert value == 8

# Generated at 2022-06-14 03:37:31.150560
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.monad_maybe import Maybe

    assert Lazy.of(5).bind(lambda x: Maybe.just(x + 10)) == Maybe.just(15)

    def lazy_f():
        raise ValueError("error")

    assert Lazy(lazy_f).bind(lambda x: Maybe.just(x + 10)) == Maybe.nothing()


# Generated at 2022-06-14 03:37:34.338165
# Unit test for method map of class Lazy
def test_Lazy_map():
    def fn(a):
        return a

    assert Lazy(fn).map(lambda a: a + 1).get(5) == 6

    assert Lazy(fn).map(lambda a: a + 1).constructor_fn(5) == 6



# Generated at 2022-06-14 03:37:39.669191
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    assert Lazy.of(5).bind(lambda x: Lazy.of(x * 10)) == Lazy.of(50)

    assert Lazy.of('five').bind(lambda x: Lazy.of(len(x))).bind(lambda x: Lazy.of(x * 10)) == Lazy.of(50)



# Generated at 2022-06-14 03:37:43.343321
# Unit test for method map of class Lazy
def test_Lazy_map():
    # pylint: disable=unused-variable, expression-not-assigned
    from pymonet.monad_list import List
    mapping_fn = lambda i: Lazy.of(str(i))
    mapped = List.of(1, 2, 3).map(mapping_fn)
    result = mapped.fold(lambda acc, e: acc + e.map(lambda i: i + ', ').get() if acc else e.get(), '')
    assert result == '1, 2, 3, '



# Generated at 2022-06-14 03:37:49.178292
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    assert Lazy.of(2).ap(Lazy.of(lambda x: x*2)) == Lazy(lambda: 4)
    assert Lazy.of(lambda x: x + 3).ap(Lazy.of(2)) == Lazy(lambda: 5)
    assert Lazy.of(lambda x: x*2).ap(Lazy.of(6)) == Lazy(lambda: 12)
    assert Lazy.of(2).ap(Lazy.of(3)) == Lazy(lambda: 3)



# Generated at 2022-06-14 03:37:52.583600
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    assert Lazy(lambda: [1, 2]).bind(lambda x: Lazy(lambda: x + [3])) == Lazy(lambda: [1, 2, 3])
    assert Lazy(lambda: [1, 2]).bind(lambda x: Lazy(lambda: x[::-1])) == Lazy(lambda: [2, 1])



# Generated at 2022-06-14 03:38:15.764944
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    def to_tuple(x): return (x, x)
    def add1(x): return x + 1
    def add2(x): return x + 2

    assert Lazy(add1).ap(Lazy(add2)).get(1) == 5
    assert Lazy(add1).map(add2).ap(Lazy(add2)).get(1) == 6
    assert Lazy(add1).ap(Lazy(add1).map(add2)).get(1) == 5
    assert Lazy(add1).map(to_tuple).ap(Lazy(add1).map(add2)).get(1) == (2, 3)


# Generated at 2022-06-14 03:38:25.207214
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    import unittest

    class TestLazyBind(unittest.TestCase):
        def test_it_should_return_result_of_piped_lambdas(self):
            def fn1(*args):
                return Lazy(lambda: args)

            def fn2(*args):
                return Lazy(lambda: args)

            self.assertEqual(Lazy.of(100).bind(fn1).bind(fn2).get(), (100,))

        def test_it_should_evalute_constructor_only_once_when_bind_to_once_piped_lambdas(self):
            constructor_fn = Lazy(lambda: 'test')

            def fn1(v):
                return v

            def fn2(*args):
                return Lazy(lambda: args)


# Generated at 2022-06-14 03:38:36.094180
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    import pymonet.either as E
    import pymonet.box as B

    def add_value(x):
        return Lazy.of(x + 1)

    lazy = Lazy.of(1).ap(E.Right(add_value))
    assert lazy.value == B.Box.of(2)

    lazy = Lazy.of(1).ap(E.Right(Lazy.of(add_value)))
    assert lazy.value is None

    lazy = Lazy.of(1).ap(E.Right(Lazy.of(lambda x: x + 1)))
    assert lazy.value == B.Box.of(2)

    lazy = Lazy.of(1).ap(E.Right(Lazy.of(lambda x: x + 1).ap(E.Right(add_value))))
    assert lazy.value

# Generated at 2022-06-14 03:38:38.425357
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def fn(x):
        return x * 2

    assert Lazy.of(2).bind(fn).get() == 4


# Generated at 2022-06-14 03:38:47.174574
# Unit test for method ap of class Lazy
def test_Lazy_ap():  # pragma: no cover
    from pymonet.list import List
    from pymonet.maybe import Maybe

    lazy_list=Lazy(lambda x: List([x]))
    lazy_maybe=Lazy(lambda x: Maybe.just(x))

    assert Lazy.of(lambda x: x+1).ap(lazy_list).get(1) == List([2])
    assert Lazy.of(lambda x: x+1).ap(lazy_maybe).get(1) == Maybe.just(2)


# Generated at 2022-06-14 03:38:52.746853
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    # given
    lazy = Lazy.of(1)
    lazy2 = Lazy.of(lambda value: value + 1)

    # when
    new_lazy = lazy.ap(lazy2)

    # then
    assert new_lazy.get() == 2


# Generated at 2022-06-14 03:39:01.409918
# Unit test for method ap of class Lazy
def test_Lazy_ap():  # pragma: no cover
    """
    Test method ap of class Lazy.
    """
    from pymonet.box import Box
    from pymonet.either import Right
    from pymonet.maybe import Maybe
    from pymonet.monad_try import Try
    from pymonet.validation import Validation

    assert Lazy.of(1).ap(Box.of(lambda x: x + 1)).get() == 2
    assert Lazy.of(1).ap(Right.of(lambda x: x + 1)).get() == 2
    assert Lazy.of(1).ap(Maybe.just(lambda x: x + 1)).get() == 2
    assert Lazy.of(1).ap(Try.of(lambda x: x + 1)).get() == 2

# Generated at 2022-06-14 03:39:06.370696
# Unit test for method map of class Lazy
def test_Lazy_map():
    def test_func(val):
        return val+1

    val = 5
    lazy_t = Lazy(lambda *args: val)
    mapped_lazy_t = lazy_t.map(test_func)

    assert mapped_lazy_t.get(None) == test_func(val)
    assert mapped_lazy_t != lazy_t


# Generated at 2022-06-14 03:39:14.209166
# Unit test for method map of class Lazy
def test_Lazy_map():
    from pymonet.validation import Validation

    assert Lazy.of(3).map(lambda x: x + 1).get() == 4
    assert Lazy.of(3).map(lambda x: Validation.success(x + 1)).get().get() == 4

    def _assert_only_one_call(*args):
        assert _assert_only_one_call.counter == 0, 'Function is called more then once'
        _assert_only_one_call.counter += 1
        return args[0]

    _assert_only_one_call.counter = 0

    assert isinstance(Lazy.of(3).map(lambda x: _assert_only_one_call(x)).get(), int)

# Generated at 2022-06-14 03:39:20.557826
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    def mapper(result):
        return result + 'world'

    lazy = Lazy.of('hello')
    assert isinstance(lazy.ap(Lazy.of(mapper)), Lazy)
    assert lazy.ap(Lazy.of(mapper)).get() == 'hello world'


# Generated at 2022-06-14 03:39:59.529105
# Unit test for method ap of class Lazy
def test_Lazy_ap():  # pragma: no cover
    def add(x: int, y: int) -> int:
        return x + y

    lazy = Lazy(lambda x: add).ap(Lazy(lambda y: y(1)))
    assert lazy.get(2) == 3



# Generated at 2022-06-14 03:40:02.660613
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    assert Lazy(lambda: 'A') == Lazy(lambda: 'A')
    assert Lazy(lambda: 'B') != Lazy(lambda: 'A')
    assert Lazy(lambda: 'A',) != 'A'



# Generated at 2022-06-14 03:40:08.789301
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.either import Left
    from pymonet.maybe import Nothing

    Lazy.of(1).ap(Lazy.of(lambda x: x + 2)).get() == 3
    Lazy.of(1).ap(Left(1)).get() == 1
    Lazy.of(1).ap(Nothing()).get() == 1

# Generated at 2022-06-14 03:40:15.349737
# Unit test for method bind of class Lazy
def test_Lazy_bind(): # pragma: no cover
    x = Lazy(lambda: 'hello')
    y = Lazy(lambda: 'world')

    def fn(x):
        def mapper(y):
            return x + y
        return y.map(mapper)

    assert x.bind(fn).get() == 'helloworld'

# Generated at 2022-06-14 03:40:27.992562
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    assert Lazy(lambda : 3).bind(lambda value: Lazy(lambda: value + 1)).get() == 4

    from pymonet.either import Left
    assert Lazy(lambda: Left(3)).bind(lambda either: Lazy(lambda: either.get_or_else(0) + 1)).get() == 4

    from pymonet.either import Right
    assert Lazy(lambda: Right(3)).bind(lambda either: Lazy(lambda: either.get() + 1)).get() == 4

    from pymonet.maybe import Maybe, Nothing
    assert Lazy(lambda: Maybe.just(3)).bind(lambda maybe: Lazy(lambda: maybe.get_or_else(0) + 1)).get() == 4

# Generated at 2022-06-14 03:40:32.019734
# Unit test for method map of class Lazy
def test_Lazy_map():
    def test_function(x: int) -> int:
        return x * x

    def test_function_mapper(x: int) -> str:
        return str(x)

    lazy = Lazy(test_function).map(test_function_mapper)
    assert lazy.get(4) == '16'


# Generated at 2022-06-14 03:40:35.533917
# Unit test for method map of class Lazy
def test_Lazy_map():
    lazy_a = Lazy(lambda x: x + 1)

    lazy_b = lazy_a.map(lambda x: x + 1)

    assert lazy_b.get(1) == 3


# Generated at 2022-06-14 03:40:38.719751
# Unit test for method ap of class Lazy
def test_Lazy_ap():  # pragma: no cover
    # WHEN
    result = Lazy.of(lambda x: x * x).ap(Lazy.of(5))

    # THEN
    assert result.get() == 25


# Generated at 2022-06-14 03:40:43.257076
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def contructor_fn(*args):
        print("In called value")
        return args

    container = Lazy(contructor_fn)
    result_container = container.bind(lambda result: Lazy.of("Mapped" + result))
    result = result_container.get("value")

    assert result == "Mappedvalue"

# Generated at 2022-06-14 03:40:54.485078
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    def return_two():  # pylint: disable=C0103
        return 2

    lazy_one = Lazy.of(1)
    lazy_two = Lazy(return_two)
    lazy_three = Lazy(return_two)
    lazy_four = Lazy(return_two)
    lazy_one.get()
    lazy_two.get()

    assert lazy_one != lazy_two
    assert lazy_two != lazy_three
    assert lazy_three == lazy_four
    assert lazy_four == lazy_four

    assert Lazy.of(1) == Lazy.of(1)
    assert Lazy.of(1) != Lazy.of(2)


# Unit tests for method map