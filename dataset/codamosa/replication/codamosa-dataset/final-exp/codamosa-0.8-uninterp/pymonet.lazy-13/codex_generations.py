

# Generated at 2022-06-14 03:31:28.407317
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    lazy = Lazy.of(1)
    lazy2 = Lazy.of(1)
    lazy3 = Lazy.of(2)
    assert lazy == lazy2
    assert lazy != lazy3
    assert lazy != None



# Generated at 2022-06-14 03:31:38.528051
# Unit test for method get of class Lazy
def test_Lazy_get():
    assert Lazy.of(1).get() == 1
    assert Lazy.of(2).get('hello') == 2
    assert Lazy.of(1).get() == 1 == Lazy.of(1).get()
    assert Lazy.of(2).get('hello') == 2 == Lazy.of(2).get('hello')
    assert Lazy.of(1).get(1) == 1 == Lazy.of(1).get(1)
    assert Lazy.of(1).get(1, 2) == 1 == Lazy.of(1).get(1, 2)


# Generated at 2022-06-14 03:31:40.741555
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def add(x):
        return Lazy(lambda y: x + y)

    assert Lazy.of(2).bind(add).get(3) == 5
    assert Lazy.of(2).bind(add).get(5) == 7
    assert Lazy.of(5).bind(add).get(5) == 10


# Generated at 2022-06-14 03:31:45.737429
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    assert Lazy.of(2).bind(lambda x: Lazy.of(x + 3)) == Lazy.of(5)
    assert Lazy.of(5).bind(lambda x: Lazy.of(x + 5)) != Lazy(lambda x: x + 5)  # type: ignore


# Generated at 2022-06-14 03:31:49.962771
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    fn = Lazy(lambda x, y: x + y)
    result = Lazy.of(1).ap(fn).get(2)

    assert result == 3

    result2 = Lazy.of(1).ap(Lazy.of(lambda x, y: x + y)).get(2)

    assert result2 == 3



# Generated at 2022-06-14 03:31:56.300532
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def f(x):
        return x * x

    def s(x):
        return x + x

    lazy_f = Lazy.of(f)
    lazy_s = Lazy.of(s)

    assert lazy_f.bind(lambda f: lazy_s.bind(lambda s: Lazy.of(f(3) + s(3)))).get() == 18

# Generated at 2022-06-14 03:32:02.113986
# Unit test for method map of class Lazy
def test_Lazy_map():  # pragma: no cover
    def function_to_map(*args):
        return args[1] + 1

    def function_to_call(*args):
        return args[0]

    lazy_instance = Lazy(function_to_call)
    result = lazy_instance.map(function_to_map)

    assert result.get(5) == 6

# Generated at 2022-06-14 03:32:06.098959
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    assert Lazy(lambda a: a.upper()).ap(Lazy('foo')).get() == 'FOO'



# Generated at 2022-06-14 03:32:10.942499
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    def fn(a):
        return a

    assert Lazy(fn).__eq__(Lazy(fn))
    assert not Lazy(fn).__eq__(Lazy(lambda x: x+1))
    assert not Lazy(fn).__eq__(fn)


# Generated at 2022-06-14 03:32:20.150067
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.monad_try import Try
    from pymonet.either import Right

    def one_to_two():
        return Try.of(lambda: 2)

    def one_to_two_with_try():
        return Lazy(one_to_two)

    result = one_to_two_with_try().bind(lambda x: Lazy(lambda: x + 2))
    result_evaluated = result.constructor_fn()
    assert isinstance(result_evaluated, Try)
    assert result_evaluated == Try.of(lambda: 4)

    assert Lazy(lambda: 2).bind(lambda x: Lazy(lambda: x + 2)).constructor_fn() == 4

# Generated at 2022-06-14 03:32:23.304753
# Unit test for method get of class Lazy
def test_Lazy_get():
    # GIVEN
    def func(val): return val * 2

    lazy = Lazy(func)

    # WHEN
    result = l

# Generated at 2022-06-14 03:32:27.254527
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():  # pragma: no cover
    def identity(x):
        return x

    fn = lambda v: v

    assert Lazy(fn).__eq__(Lazy(fn))
    assert not Lazy(fn).__eq__(identity)

# Generated at 2022-06-14 03:32:32.635695
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():  # pragma: no cover
    def div(x, y):
        return x / y

    assert Lazy.of(2) == Lazy.of(2)
    assert Lazy(div).map(lambda x: x * 2) == Lazy(lambda: div(5, 0)).map(lambda x: x * 2)



# Generated at 2022-06-14 03:32:37.551365
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    def add(x: int) -> int:
        return x + 1

    def add2(x: int) -> int:
        return x + 2

    assert Lazy.of(add).ap(Lazy.of(1)).get() == add(1)
    assert Lazy.of(add2).ap(Lazy.of(1)).get() == add2(1)



# Generated at 2022-06-14 03:32:41.475788
# Unit test for method get of class Lazy
def test_Lazy_get():
    def square(x):
        return x*x

    lz = Lazy(square)

    assert lz.get(5) == 25
    assert lz.is_evaluated
    assert lz.value == 25


# Generated at 2022-06-14 03:32:49.932830
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    # - eq:
    #   - Lazy with eq values
    #   - Lazy with eq constructors
    #   - Lazy with both eq constructors and eq values
    # - not eq:
    #   - Lazy with eq constructors but different values
    #   - Lazy with eq values but different constructors
    #   - Lazy with different constructors and different values

    add_two = lambda x: x + 2
    double = lambda x: x * 2

    assert Lazy.of(2) == Lazy.of(2)
    assert Lazy(add_two) == Lazy(add_two)
    assert Lazy(add_two).get() == Lazy(add_two).get()
    assert not Lazy(add_two) == Lazy.of(2)

# Generated at 2022-06-14 03:32:54.186099
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():  # pragma: no cover
    from pymonet.monad_try import Try

    def _return_one():
        return 1

    def _return_two():
        return 2

    fn_with_one = lambda: Try.of(_return_one)
    fn_with_two = lambda: Try.of(_return_two)
    assert Lazy.of(fn_with_one) == Lazy.of(fn_with_one)
    assert Lazy.of(fn_with_one) != Lazy.of(fn_with_two)
    assert Lazy.of(fn_with_one) != Lazy.of(fn_with_one).map(lambda x: x + 1)

# Generated at 2022-06-14 03:33:02.408060
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    from pymonet.box import Box

    assert Lazy(lambda: 2).__eq__(Lazy(lambda: 2))
    assert Lazy(lambda a: a).__eq__(Lazy(lambda a: a))
    assert Lazy(lambda a, b: a + b).__eq__(Lazy(lambda a, b: a + b))
    assert not Lazy(lambda a, b: a + b).__eq__(Lazy(lambda a, b: a * b))
    assert not Lazy(lambda a, b: a * b).__eq__(Lazy(lambda a, b: a + b))
    assert not Lazy(lambda a, b: a * b).__eq__(Lazy(lambda a: a))

# Generated at 2022-06-14 03:33:06.981451
# Unit test for method get of class Lazy
def test_Lazy_get():
    """
    Test Lazy get method

    :returns: None
    :rtype: None
    """
    fn = lambda x: x
    lazy = Lazy(fn)

    assert lazy.get(42) == 42
    assert lazy.is_evaluated
    assert lazy.get(43) == 42

# Generated at 2022-06-14 03:33:09.479874
# Unit test for method map of class Lazy
def test_Lazy_map():
    value = Lazy.of(3).map(lambda x: x + 1).map(lambda x: x * x)
    assert value == Lazy.of(16)


# Generated at 2022-06-14 03:33:25.714370
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():  # pragma: no cover
    def call_fn_1(*_):
        return 1

    def call_fn_2(*_):
        return 2

    def call_fn_3(*_):
        return 3

    def call_fn_4(*_):
        return 4

    assert Lazy(call_fn_1) == Lazy(call_fn_1)
    assert Lazy(call_fn_2) == Lazy(call_fn_2)

    assert Lazy(call_fn_1) != Lazy(call_fn_2)
    assert Lazy(call_fn_2) != Lazy(call_fn_3)
    assert Lazy(call_fn_3) != Lazy(call_fn_4)

    assert Lazy(call_fn_3) != Lazy(call_fn_2)


# Generated at 2022-06-14 03:33:32.008732
# Unit test for method ap of class Lazy
def test_Lazy_ap():  # pragma: no cover
    lazier_than_lazy = Lazy.of(Lazy.of(lambda x: x))
    result = lazier_than_lazy.ap(Lazy.of(lambda x: x + x)).get(4)
    assert result == 8



# Generated at 2022-06-14 03:33:36.607052
# Unit test for method map of class Lazy
def test_Lazy_map():
    # given
    lazy = Lazy(lambda x, y: x + y)
    mapper = lambda x: x * 2

    # when
    result = lazy.map(mapper)

    # then
    assert result == Lazy(lambda x, y: mapper(lazy.constructor_fn(x, y)))


# Generated at 2022-06-14 03:33:41.576948
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def fn(value):
        return Lazy(lambda: value + 1)

    fn_2 = Lazy(lambda: lambda x: x * 2)

    result = Lazy(lambda: 1).bind(fn).bind(fn).bind(fn).bind(fn_2).constructor_fn()
    assert result == 10


# Generated at 2022-06-14 03:33:50.348317
# Unit test for method ap of class Lazy
def test_Lazy_ap():  # pragma: no cover
    from pymonet.functor import identity
    from pymonet.monad import MonadZero

    lazy = Lazy.of(1)
    mapper = Lazy.of(identity)
    assert mapper.ap(lazy) == Lazy.of(1)
    assert mapper.ap(MonadZero.empty()) == MonadZero.empty()
    assert Lazy.of(identity).ap(MonadZero.empty()) == MonadZero.empty()
    assert Lazy.of(identity).ap(Lazy.of(1)) == Lazy.of(1)


# Generated at 2022-06-14 03:33:53.937613
# Unit test for method map of class Lazy
def test_Lazy_map():
    def f(x):
        return x * 2

    def g(x):
        return x + 1

    assert Lazy(f).map(g).get(3) == 8


# Generated at 2022-06-14 03:34:03.237461
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    """
    Lazy[Function() -> Int].bind(function) -> Lazy[Function() -> Int2].

    Which is equivalent to:

    Lazy[Function() -> Int](function).bind(function) -> Lazy[Function() -> Int2].

    :returns: True when test passed, otherwise throws AssertionError exception
    :rtype: bool
    """
    value = Lazy.of(lambda: 10).bind(lambda x: Lazy.of(lambda: '%s, World' % (x + 1)))
    assert isinstance(value, Lazy)

    assert 10 == value.constructor_fn()

    return True


# Generated at 2022-06-14 03:34:15.243636
# Unit test for method map of class Lazy
def test_Lazy_map():
    """
    Check if map return another object of class Lazy with mapped constructor_fn.
    Check if constructor_fn are not executed after calling map method.
    """
    lazy = Lazy(lambda x: x)

    # Check if Lazy change constructor_fn after calling map
    mapped_lazy = lazy.map(lambda x: x * 2)
    assert mapped_lazy.constructor_fn(10) == 20

    # Check if Lazy constructor_fn are not evaluated after calling map
    lazy.constructor_fn = Mock()
    mapped_lazy = lazy.map(lambda x: x * 2)
    assert lazy.constructor_fn.call_count == 0

    # Check if Lazy constructor_fn are not evaluated after calling map
    lazy.constructor_fn = lambda x: x

# Generated at 2022-06-14 03:34:26.428984
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.monad_try import Try
    from pymonet.either import Right
    from pymonet.box import Box

    def f(x):
        return Lazy(lambda: x + 1)

    def g(x):
        return Lazy(lambda: x + 's')

    def h(x):
        return Lazy(lambda: x + 's')

    # examples: Lazy(1).map(f).bind(g).bind(h).get() == '1sss'
    assert Lazy(lambda: 1).bind(f).bind(g).bind(h).get() == '1sss'

    # examples: Lazy(Lazy(1)).map((lambda x: x.get())).
    #                            bind(lambda x: Lazy(lambda: x + 1)).
    #                            bind

# Generated at 2022-06-14 03:34:35.545866
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def const_1():
        return 1
    def const_2(x):
        return x + 1
    def const_3(x):
        return x + 2

    def_lazy_1 = Lazy(const_1)
    def_lazy_2 = Lazy(const_2)
    def_lazy_3 = Lazy(const_3)

    actual = def_lazy_1.bind(lambda x: def_lazy_2).bind(lambda x: def_lazy_3)
    assert actual._compute_value() == 4



# Generated at 2022-06-14 03:34:46.885005
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.validation import Validation, ValidationError

    Lazy.of(1).bind(lambda x: Lazy.of(x + 2)).bind(lambda x: Lazy.of(x + 3)).get() == (1 + 2 + 3)
    Lazy.of(2).bind(lambda x: Lazy.of(x * 2)).bind(lambda x: Lazy.of(x * 3)).get() == (2 * 2 * 3)
    Lazy.of(2).bind(lambda x: Validation.success(x * 2)).bind(lambda x: Validation.success(x * 3)).get() == (2 * 2 * 3)

# Generated at 2022-06-14 03:34:55.239147
# Unit test for method map of class Lazy
def test_Lazy_map():
    """
    >>> test_Lazy_map()
    True
    """
    def func_a(a):
        return a

    lazy_a = Lazy(func_a)
    lazy_b = lazy_a.map(lambda a: a + 1)
    lazy_c = lazy_a.map(lambda a: a + 1).map(lambda a: a + 1)

    return (
        lazy_b.get(1) == 2
        and lazy_c.get(1) == 3
        and lazy_b.is_evaluated == False
        and lazy_c.is_evaluated == False
    )


# Generated at 2022-06-14 03:35:07.348373
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    # we will show how to use Lazy with bind method
    # we will use example of Pipeline with preprocessing module
    # lets suppose that we have input data with different properties
    input_data1 = ['cat', 'dog', 'rabbit']  # type: T
    input_data2 = [1, 2, 3]  # type: T
    input_data3 = {'cow', 'sheep', 'horse'}  # type: T

    # and we want to preprocess each of this data with two methods
    def preprocessor1(input_data):  # type: (T) -> U
        return [input_data[i] * 2 for i in range(len(input_data))]


# Generated at 2022-06-14 03:35:10.691422
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    def fn(x):
        return x * 2

    assert Lazy.of(1).ap(Lazy.of(fn)).get() == 2



# Generated at 2022-06-14 03:35:22.432598
# Unit test for method ap of class Lazy
def test_Lazy_ap():  # pragma: no cover
    from pymonet.validation import Validation
    from pymonet.lazy import Lazy

    def create_l(val):
        def create(value):
            return value

        return Lazy(lambda: val).map(create)

    def add(trace, next_val):
        def add_fn(prev):
            return prev + next_val

        lazy = Lazy.of(trace)
        return lazy.ap(create_l(add_fn)).get()

    assert Validation.success(10).ap(Lazy(lambda: 10)) == Validation.success(10)
    assert Validation.success(5).ap(Lazy(lambda: 10)) == Validation.success(15)

# Generated at 2022-06-14 03:35:29.430843
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    import pymonet.functor as functor
    import pymonet.box as box

    def fn_2_lazy_box(param):
        return Lazy(lambda: box.Box(param+1))

    # Test with non-empty Lazy
    result = Lazy.of(5).bind(fn_2_lazy_box)
    assert result.get() == box.Box(6)

    # Test with empty Lazy
    result = Lazy.of(None).bind(fn_2_lazy_box)
    assert result.get() == box.Box(None)



# Generated at 2022-06-14 03:35:35.262724
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    test_fn = lambda x: 2 * x
    lazy = Lazy.of(test_fn)
    applicative = Lazy.of(40)

    actual = lazy.ap(applicative)
    expected = Lazy.of(80)

    assert expected == actual

# Generated at 2022-06-14 03:35:45.664746
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    def f(x): return x
    assert Lazy(f) != Lazy(f)
    assert Lazy(f).map(f) != Lazy(f).map(f)
    assert Lazy(f) != Lazy(lambda x: x+1)
    assert Lazy(f).map(f) != Lazy(f)
    assert Lazy(f).map(f)._compute_value(1) == Lazy(f).map(f)._compute_value(1)
    assert Lazy(f).map(f) != Lazy(f).map(lambda x: x+1)



# Generated at 2022-06-14 03:35:55.404619
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    def function():
        return 0

    assert Lazy.of(0) == Lazy(function) == Lazy.of(0)
    assert Lazy.of(0) != Lazy(lambda: 1)
    assert Lazy(lambda: 0) != Lazy(lambda: 1)
    assert Lazy(lambda: 0) != Lazy(lambda: 0)
    assert Lazy.of(0) != Lazy.of(1)
    assert Lazy.of(0) != Lazy(lambda: None)
    assert Lazy.of(0) != None  # noqa: E711
    assert Lazy.of(0) != 0  # noqa: E711
    assert Lazy.of(0) != 'string'
    assert Lazy.of(0) != [0]



# Generated at 2022-06-14 03:36:02.956182
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    """
    Unit test for method __eq__ of class Lazy
    """
    import pytest
    from pymonet.maybe import Maybe

    def func(*args):  # pylint: disable=unused-variable
        return 3

    # test Lazy with another class
    assert Lazy.of(7) != 7

    # test Lazy with evaluated and not evaluated lazy
    assert Lazy.of(7).get() == Lazy.of(7)
    assert Lazy.of(7).get() != Lazy.of(3)

    # test Lazy with mapper
    assert Lazy.of(7).map(lambda x: x == 7) != Lazy.of(7).map(lambda x: x == 3)

# Generated at 2022-06-14 03:36:12.645797
# Unit test for method bind of class Lazy
def test_Lazy_bind():  # pragma: no cover
    def add(a):
        return a + 5

    def divide_by_2(a):
        return a / 2

    lazy = Lazy(lambda: 12)
    assert lazy.get() == 12

    lazy = lazy.map(add)
    assert lazy.get() == 17

    lazy = lazy.map(divide_by_2)
    assert lazy.get() == 8.5



# Generated at 2022-06-14 03:36:23.078763
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.box import Box
    from pymonet.either import Right
    from pymonet.monad_try import Try

    assert Lazy(lambda: 1).bind(lambda x: Box(x*2)).to_box() == Box(2)
    assert Lazy(lambda: 1).bind(lambda x: Right(x*2)).to_either() == Right(2)
    assert Lazy(lambda: 1).bind(lambda x: Try.of(lambda: x*2)).to_try() == Try.of(lambda: 2)
    assert Lazy(lambda: 1).bind(lambda x: Lazy(lambda: x*2)).get() == 2



# Generated at 2022-06-14 03:36:31.281052
# Unit test for method map of class Lazy
def test_Lazy_map():
    def square(x):
        return x * x

    def add(x):
        return x + x

    lazy_value = Lazy.of(1)
    multiplied_by_2 = lazy_value.map(square)
    multiplied_by_4 = multiplied_by_2.map(add)

    assert lazy_value.get() == 1
    assert multiplied_by_2.get() == 2
    assert multiplied_by_4.get() == 4


# Generated at 2022-06-14 03:36:41.403839
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.box import Box
    from pymonet.either import Right
    from pymonet.maybe import Maybe
    from pymonet.monad_try import Try
    from pymonet.validation import Validation

    def f(value):
        return value * 2

    def g(value):
        return value + 1
    # with Box
    lazy_ap_box = Lazy.of(f).ap(Box(g))
    assert lazy_ap_box.get(1) == 4

    # with Either
    lazy_ap_either = Lazy.of(f).ap(Right(g))
    assert lazy_ap_either.get(1) == 4

    # with Maybe
    lazy_ap_maybe_just = Lazy.of(f).ap(Maybe.just(g))
    assert lazy_ap_

# Generated at 2022-06-14 03:36:51.488930
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.monad_maybe import Maybe
    from pymonet.monad_try import Try

    def double_value(value):
        return value * 2

    assert Lazy.of(double_value).ap(Lazy.of(2)) == Lazy.of(4)
    assert Lazy.of(double_value).ap(Maybe.just(2)) == Maybe.just(4)
    assert Lazy.of(double_value).ap(Try.of(lambda: 2)) == Try.of(lambda: 4)
    assert Lazy.of(double_value).ap(double_value) == 4



# Generated at 2022-06-14 03:36:54.385529
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def add1(x: int) -> Lazy[int, int]:
        return Lazy.of(x + 1)

    def double(x: int) -> Lazy[int, int]:
        return Lazy.of(x * 2)

    assert Lazy.of(1).bind(add1).bind(double).get() == 4

# Generated at 2022-06-14 03:37:01.376525
# Unit test for method bind of class Lazy
def test_Lazy_bind():  # pragma: no cover
    def create_lazy(number):
        def getter():
            return number

        return Lazy(getter)

    lazy = Lazy.of(5)
    assert lazy.bind(create_lazy).get() == 5

    lazy = Lazy.of(5)
    assert lazy.bind(lambda n: create_lazy(n + 5)).get() == 10


# Generated at 2022-06-14 03:37:03.550725
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    assert Lazy.of(4).bind(
        lambda x: Lazy.of(x + 5)).get(3) == 4 + 5



# Generated at 2022-06-14 03:37:07.067862
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    """
     Test for method ap of class Lazy
     """
    lazy_fn = Lazy(lambda x: x)
    assert lazy_fn.ap(Lazy.of(0)) == lazy_fn.map(lambda x: x)


# Generated at 2022-06-14 03:37:15.126568
# Unit test for method map of class Lazy
def test_Lazy_map():
    """ Unit test for method map of class Lazy. """
    add_two_fn = lambda x: x + 2
    add_three_fn = lambda x: x + 3
    lazy_value = Lazy(add_two_fn)

    assert Lazy(add_three_fn) == lazy_value.map(add_three_fn)
    assert Lazy(add_two_fn) == lazy_value.map(lambda x: x)  # evaluating function inside Lazy
    assert Lazy(add_three_fn) == lazy_value.map(lambda x: x + 1).map(lambda x: x + 2)



# Generated at 2022-06-14 03:37:23.999739
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    def fn(*args):
        return sum(args)

    def mapper(x):
        return x+1

    assert Lazy(fn).ap(Lazy(mapper))(1, 2, 3) == Lazy(fn).map(mapper)(1, 2, 3) == sum((1, 2, 3))+1



# Generated at 2022-06-14 03:37:28.539107
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.either import Right, Left

    def fn(v):  # type: ignore
        if v == 1:
            return Lazy.of(Right(1))
        return Lazy.of(Left("not 1"))

    assert Lazy.of(1).bind(fn).get() == Right(1)
    assert Lazy.of(2).bind(fn).get() == Left("not 1")



# Generated at 2022-06-14 03:37:36.779747
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():  # pragma: no cover
    import pytest

    # [Given]
    def test_function():
        return 1

    def test_function_2():
        return 2

    lazy = Lazy(test_function)
    lazy_2 = Lazy(test_function)
    lazy_3 = Lazy(test_function_2)
    lazy_4 = Lazy(test_function)
    lazy_4._compute_value()

    # [When/Then]
    assert not (lazy == 1)
    assert lazy == lazy_2
    assert lazy != lazy_3
    assert lazy != lazy_4



# Generated at 2022-06-14 03:37:45.038151
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def test_function(n):
        return n
    lazy_test_function = Lazy(test_function)
    assert lazy_test_function.bind(test_function) == Lazy(test_function)

    def test_function2(n):
        return n*2
    lazy_test_function2 = Lazy(test_function2)
    assert lazy_test_function.bind(test_function2) == Lazy(test_function2)
    assert lazy_test_function.bind(lazy_test_function) == Lazy(test_function)



# Generated at 2022-06-14 03:37:47.986236
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    from pymonet.validation import Validation
    from pymonet.box import Box

    function = lambda : 1
    lazy1 = Lazy(function)
    lazy2 = Lazy(function)

    assert lazy1 == lazy2



# Generated at 2022-06-14 03:37:49.737675
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    assert Lazy.of(lambda x: x + 10).ap(Lazy.of(2)) == Lazy.of(12)



# Generated at 2022-06-14 03:37:52.739836
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def fn(value):
        def lambda_fn(*args):
            def func(*args):
                return 'hello {}'.format(value)
            return func

        return Lazy(lambda_fn)

    assert Lazy(lambda *_: 'world').bind(fn)(1) == Lazy(lambda *_: 'hello world')(1)

# Generated at 2022-06-14 03:38:01.495468
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    # type: () -> None
    def add_one(v):
        # type: (int) -> Lazy[int, int]
        return Lazy.of(v + 1)

    def add_two(v):
        # type: (int) -> Lazy[int, int]
        return Lazy.of(v + 2)

    computed_lazy = Lazy.of(0).bind(add_one).bind(add_two)
    assert computed_lazy.get() == 3


# Generated at 2022-06-14 03:38:08.583550
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def constructor(s):
        return (s + 'f')

    def mapper(s):
        return (s + 'm')

    def folder(result):
        return (result + 'f')

    def mapper_folder(result):
        return (result + 'm')

    lazy = Lazy(constructor).map(mapper).bind(Lazy.of)
    assert lazy.get('t') == 'tm'

    lazy_folded = lazy.get('t')
    assert lazy_folded == 'tm'
    assert lazy.is_evaluated

    lazy.is_evaluated = False
    assert lazy.get('t') == 'tm'



# Generated at 2022-06-14 03:38:14.487381
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    from pymonet.functor import Functor

    def constructor(x):  # pragma: no cover
        return x * 2

    def mapper(x):  # pragma: no cover
        return x + 1

    lazy = Lazy(constructor)
    lazy_copy = Lazy(constructor)
    lazy_mapped = lazy.map(mapper)
    lazy_mapped_copy = lazy.map(mapper).map(mapper)
    assert lazy == lazy_copy
    assert lazy_mapped == lazy_mapped_copy
    assert lazy != lazy_mapped



# Generated at 2022-06-14 03:38:26.914743
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.maybe import Maybe
    from pymonet.functional import compose

    def function_1(x):
        return x + 5

    def function_2(x):
        return x / 2

    def function_3(x):
        return x * 6

    lazy_function_1 = Lazy(function_1)
    lazy_function_2 = Lazy(function_2)
    lazy_function_3 = Lazy(function_3)

    composed_function_1 = compose(function_2, function_1)
    composed_function_2 = compose(function_3, function_2)

    lazy_composed_function_1 = composed_function_1 >> function_2
    lazy_composed_function_2 = composed_function_2 >> function_1

    input_value = 1
    expected_output_value

# Generated at 2022-06-14 03:38:31.662231
# Unit test for method map of class Lazy
def test_Lazy_map():
    """
    Lambda expression to multiply passed value on 2
    """
    doubler = lambda x: x * 2

    # Create structure with lambda expression
    lazy = Lazy.of(5).map(doubler)

    assert lazy.get() == 10



# Generated at 2022-06-14 03:38:37.255524
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.box import Box

    def function_to_call(argument):
        return argument

    # When
    lazy_result = Lazy(lambda: 1).ap(Box(function_to_call))
    lazy_value = lazy_result.get()

    # Then
    assert lazy_value == 1



# Generated at 2022-06-14 03:38:45.888906
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.functor import Functor
    from pymonet.applicative import Applicative
    from pymonet.applicative import ApplicativeOps
    from pymonet.monad import Monad
    from pymonet.monad import MonadOps

    assert isinstance(Lazy, Functor)
    assert isinstance(Lazy, Applicative)
    assert isinstance(Lazy, Monad)

    # Test Functor
    assert Functor.lift(lambda x: x + 1, Lazy.of(1)) == Lazy.of(2)

    # Test Applicative
    assert Applicative.of(2) == Lazy.of(2)

    assert ApplicativeOps.ap(Lazy.of(lambda x: x + 1), Lazy.of(1)) == Lazy.of(2)
    assert Applic

# Generated at 2022-06-14 03:38:53.065392
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.either import Right

    lazy_fn = Lazy.of(lambda x: x + 1)
    lazy_arg = Lazy.of(5)

    assert lazy_fn.ap(lazy_arg) == Lazy(lambda *args: Right(6))

    lazy_fn_1 = Lazy.of(lambda x, y: [x, y])
    lazy_arg_1 = Lazy.of([1, 2])
    assert lazy_fn_1.ap(lazy_arg_1) == Lazy(lambda *args: Right([1, 2]))

    lazy_fn_2 = Lazy.of(lambda x, y, z: [x, y, z])
    lazy_arg_2 = Lazy.of([1, 2])

# Generated at 2022-06-14 03:39:01.634631
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    def _eq(lazy1, lazy2, is_eq):
        assert (lazy1 == lazy2) == is_eq, '{} == {}'.format(lazy1, lazy2)

    _eq(Lazy.of(1), Lazy.of(1), True)
    _eq(Lazy(lambda: 's'), Lazy(lambda: 's'), True)
    _eq(Lazy(lambda: 's'), Lazy(lambda: 's2'), False)
    _eq(Lazy(lambda: 's'), Lazy.of('s'), True)
    _eq(Lazy(lambda: 's').map(lambda x: x), Lazy(lambda: 's'), True)
    _eq(Lazy(lambda: 's').map(lambda x: x + 1), Lazy(lambda: 's'), False)

# Generated at 2022-06-14 03:39:10.680768
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    from pymonet.either import Right, Left
    from pymonet.validation import Validation, Success, Failure


# Generated at 2022-06-14 03:39:13.491784
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    assert Lazy(lambda: 's').bind(lambda s: Lazy(lambda: s.upper())).get() == 'S'



# Generated at 2022-06-14 03:39:22.714477
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.box import Box
    from pymonet.either import Right
    from pymonet.maybe import Maybe
    from pymonet import Lazy

    def mapper(value):
        return 2 * value

    def add(x, y):
        return x + y

    assert Lazy.of(1).map(mapper).ap(Lazy.of(2)).get() == 4
    assert Lazy.of(1).map(mapper).ap(Box(2)).get() == 4
    assert Lazy.of(1).map(mapper).ap(Right(2)).get() == 4
    assert Lazy.of(1).map(mapper).ap(Maybe.just(2)).get() == 4


# Generated at 2022-06-14 03:39:28.484409
# Unit test for method bind of class Lazy
def test_Lazy_bind():  # pragma: no cover
    from pymonet.maybe import Maybe
    from pymonet.monad_try import Try

    def divide(a, b):
        return Try(lambda: a / b)

    division = Lazy(lambda a: Lazy(lambda b: divide(a, b)))
    division2 = division.bind(lambda division: division.bind(lambda division: division.map(lambda division: division)))
    division3 = division.bind(lambda division: division.bind(lambda division: division.map(lambda division: division ** 2)))
    division2 = division2.map(lambda division: division.to_maybe())

    assert division.constructor_fn == division2.constructor_fn
    assert division.constructor_fn == division3.constructor_fn


# Generated at 2022-06-14 03:39:47.927712
# Unit test for method map of class Lazy
def test_Lazy_map():
    def square(value):
        return value * value

    def add_one(value):
        return value + 1

    def add_five(value):
        return value + 5

    assert Lazy(square).map(add_one) == Lazy(lambda x: add_one(x*x))
    assert Lazy(square).map(add_one).map(add_five) == Lazy(lambda x: add_five(add_one(x*x)))
    assert Lazy(lambda: 2).map(add_one).map(add_five).fold() == 8
    assert Lazy(lambda: 2).map(add_one).map(add_five).map(square).fold() == 64


# Generated at 2022-06-14 03:39:57.147729
# Unit test for method bind of class Lazy
def test_Lazy_bind():

    def fn1(param) -> Lazy[str, int]:
        def constructor() -> int:
            return int(param)

        return Lazy(constructor)

    def fn2(param) -> Lazy[int, bool]:
        def constructor() -> bool:
            return bool(param)

        return Lazy(constructor)

    lazy = Lazy(lambda param: param).bind(fn1).bind(fn2)

    assert lazy.get('123') is True
    assert lazy.get('0') is False

    lazy2 = Lazy(lambda: 123)
    assert lazy2.get() == 123

# Generated at 2022-06-14 03:40:01.732097
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.list import List
    from pymonet.monad_try import Try

    def test_function(number):
        return number / 10

    def function_returning_lazy(number):
        return Lazy(lambda: Try.of(test_function, number))

    assert Lazy.of(1).ap(Lazy.of(function_returning_lazy)).get() == Try.of(test_function, 1)
    assert Lazy.of(10).ap(Lazy.of(function_returning_lazy)).get() == Try.of(test_function, 10)
    assert Lazy.of(0).ap(Lazy.of(function_returning_lazy)).get() == Try.of(test_function, 0)


# Generated at 2022-06-14 03:40:10.307466
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    def add_one(x):
        return Lazy.of(x + 1)

    def double(x):
        return Lazy.of(x * 2)

    assert Lazy.of(1).ap(Lazy.of(add_one)).get() == 2
    assert Lazy.of(add_one).ap(Lazy.of(1)).get() == 2
    assert Lazy.of(double).ap(Lazy.of(add_one)).ap(Lazy.of(4)).get() == 10

# Generated at 2022-06-14 03:40:18.974576
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    """
    `Lazy.bind` method
    Use `bind` method to execute function stored in Lazy.
    This is only way to execute constructor function (and all mappers)
    """
    print('#' * 10 + ' test_Lazy_bind ' + '#' * 10)

    def do_something(value: int) -> int:
        return value ** 2

    Lazy(do_something).bind(print).bind(type).bind(print)



# Generated at 2022-06-14 03:40:26.345644
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():  # pragma: no cover
    def test():  # pragma: no cover
        a = Lazy.of(True)
        b = Lazy.of(False)

        assert a is not b

        c = Lazy.of(True)

        assert c is not a

        assert a != b
        assert a == c

        d = Lazy(lambda *args: None)
        assert d != a
        d.get()
        assert d == a

    test()
    test()



# Generated at 2022-06-14 03:40:28.644397
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    assert (
        Lazy.of(1).bind(
            lambda x: Lazy.of(x + 1)
        ).get() == 2
    )



# Generated at 2022-06-14 03:40:35.152524
# Unit test for method map of class Lazy
def test_Lazy_map():
    assert_equal(
        Lazy(lambda x: x ** 2).map(lambda x: x + 1).get(),
        Lazy(lambda x: x ** 2).get() + 1,
        'Lazy map with lambda function'
    )
    assert_equal(
        Lazy(lambda x: x ** 2).map(lambda x: x + 1).get(),
        Lazy(lambda x: x ** 2).get() + 1,
        'Lazy map with lambda function 2'
    )



# Generated at 2022-06-14 03:40:42.941788
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def fn1(x):
        return x * 2

    def fn2(x):
        return Lazy(lambda _: x * 2)

    lazy_lazy = Lazy(fn1).bind(fn2)
    assert lazy_lazy.get(2) == 8

    lazy_lazy = Lazy(fn1).bind(fn2).bind(fn2)
    assert lazy_lazy.get(2) == 16

    lazy = Lazy(fn1).map(fn2).bind(fn2)
    assert lazy.get(2) == 8



# Generated at 2022-06-14 03:40:54.649658
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.monad_try import Try
    from pymonet.either import Right

    def test_func_failing(val):
        if val > 1:
            return Try.fail('test_error')
        return Try.of(val + 1)

    def test_func_ok(val):
        if val > 1:
            return Right(val + 1)
        return Right(val + 2)

    assert Lazy.of(1).bind(test_func_failing).get() == Try.fail('test_error')
    assert Lazy.of(1).bind(test_func_ok).get() == Right(2)
    assert Lazy.of(2).bind(test_func_ok).get() == Right(3)



# Generated at 2022-06-14 03:41:24.891996
# Unit test for method map of class Lazy
def test_Lazy_map():  # pragma: no cover
    """
    This is unit test for Lazy.map method.
    """
    from pymonet.box import test_Box_map

    def mapper(x):
        return x + 1

    def constructor_fn(x):
        return 0

    lazy = Lazy.of(constructor_fn).map(mapper)
    new_lazy = lazy.map(mapper)

    test_Box_map(lambda x: x + 1, new_lazy)

