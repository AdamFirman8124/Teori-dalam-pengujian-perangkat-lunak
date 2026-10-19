

# Generated at 2022-06-14 03:31:34.613905
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    lazy = Lazy.of(5)
    assert lazy.get() == 5
    assert lazy.bind(lambda x: Lazy.of(x + 3)).get() == 8
    assert lazy.bind(lambda x: Lazy.of(x - 3)).get() == 2
    assert lazy.bind(lambda x: Lazy.of(x + 3)).get() == 8
    assert lazy.bind(lambda x: Lazy.of(x + 3)).bind(lambda x: Lazy.of(x + 3)).get() == 11
    assert lazy.bind(lambda x: Lazy.of(x + 3)).bind(lambda x: Lazy.of(x + 3)).bind(lambda x: Lazy.of(x - 5)).get() == 6



# Generated at 2022-06-14 03:31:41.547996
# Unit test for method ap of class Lazy
def test_Lazy_ap():

    def fn(x):
        return Lazy.of(x)

    def fn2(x, y):
        return Lazy.of(x + y)

    assert Lazy(fn).ap(Lazy(fn2)).get(1, 2) == 3
    assert Lazy(lambda x: fn2(x, 1)).ap(Lazy(fn)).get(1) == 2



# Generated at 2022-06-14 03:31:51.906469
# Unit test for method get of class Lazy
def test_Lazy_get():
    def func(a): return a

    assert_that(Lazy(func).get('1234'), equal_to('1234'))
    assert_that(Lazy(func).get('1234'), equal_to('1234'))
    assert_that(Lazy(func).get('1234'), equal_to('1234'))
    assert_that(Lazy(func).get(1234), equal_to(1234))
    assert_that(Lazy(func).get(1234), equal_to(1234))
    assert_that(Lazy(func).get(1234), equal_to(1234))
    assert_that(Lazy(func).get(None), equal_to(None))
    assert_that(Lazy(func).get(None), equal_to(None))

# Generated at 2022-06-14 03:31:57.401784
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def f(x):
        return Lazy(lambda: x + 3)

    r = Lazy(lambda: 2).bind(f)
    assert r.get() == 5



# Generated at 2022-06-14 03:31:58.961106
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def f(a):
        return Lazy.of(a + 1)

    x = Lazy.of(5)
    assert x.bind(f).get() == 6



# Generated at 2022-06-14 03:32:10.331671
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():  # pragma: no cover
    assert Lazy(lambda x: x) != Lazy(lambda y: y)

    def add(x):
        return x + x

    assert Lazy(add) == Lazy(add)
    assert Lazy(lambda x: x).map(add) == Lazy(lambda x: x).map(add)

    def multiply(x):
        return x * x

    assert Lazy(lambda x: x).map(add) != Lazy(lambda x: x).map(multiply)

    assert Lazy(add).ap(Lazy(add)) == Lazy(add).ap(Lazy(add))
    assert Lazy(add).ap(Lazy(add)) != Lazy(multiply).ap(Lazy(add))


# Generated at 2022-06-14 03:32:18.525053
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    assert Lazy(lambda x: x).ap(Lazy(lambda x: str(x))) == Lazy(lambda x: str(x))
    assert Lazy(lambda x: x).ap(Lazy(lambda x: str(x * 2))) == Lazy(lambda x: str(x * 2))
    assert Lazy(lambda x: x * 2).ap(Lazy(lambda x: str(x))) == Lazy(lambda x: str(x * 2))
    assert Lazy(lambda x: str(x * 2)).ap(Lazy(lambda x: x * 2)) == Lazy(lambda x: str(x * 4))


# Generated at 2022-06-14 03:32:30.228294
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.box import Box
    from pymonet.maybe import Maybe

    def add(a):
        return Maybe.just(a + 1)

    def not_add(a):
        return Maybe.empty()

    assert Lazy(lambda: Maybe.just(2)).ap(Lazy(lambda: Maybe.just(add))) == Maybe.just(3)
    assert Lazy(lambda: Maybe.empty()).ap(Lazy(lambda: Maybe.just(add))) == Maybe.empty()
    assert Lazy(lambda: Maybe.just(2)).ap(Lazy(lambda: Maybe.empty())) == Maybe.empty()
    assert Lazy(lambda: Maybe.just(2)).ap(Lazy(lambda: Maybe.just(not_add))) == Maybe.empty()


# Generated at 2022-06-14 03:32:40.617234
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    from pymonet.functor import Functor
    from pymonet.monad import Monad
    from pymonet.applicative import Applicative

    assert Lazy.of(1) == Lazy.of(1)
    assert Lazy.of(1) != Lazy.of(2)
    assert Lazy.of(1) != Lazy.of(2).map(lambda x: x)

    assert Lazy.of(1) != 1
    assert Lazy.of(1) != None
    assert Lazy.of(1) != Functor
    assert Lazy.of(1) != Monad
    assert Lazy.of(1) != Applicative



# Generated at 2022-06-14 03:32:52.332326
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():  # pragma: no cover
    """
    test_Lazy___eq__ - test method __eq__ in class Lazy returns False when one Lazy not equals other
    """
    def test(first_fn, second_fn):
        first_lazy = Lazy(first_fn)
        second_lazy = Lazy(second_fn)
        first_lazy.get()
        second_lazy.get()

        return first_lazy == second_lazy

    assert not test(lambda: 'a', lambda: 'b')
    assert test(lambda: 'a', lambda: 'a')
    assert not test(lambda: 'a', lambda: 1)
    assert test(lambda: (1, 'a'), lambda: (1, 'a'))

# Generated at 2022-06-14 03:32:58.536916
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    assert Lazy.of(1).bind(lambda x: Lazy.of(x+1)).get() == 2

# Generated at 2022-06-14 03:33:08.939829
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.maybe import Maybe

    class ClassWithMethod(object):
        @staticmethod
        def method(value):
            return 'method({})'.format(value)

    assert Lazy.of(1).bind(lambda x: Lazy.of(x + 1)).get() == 2
    assert Lazy.of(1).bind(lambda x: Lazy.of(x + 1)).to_maybe().get() == 2

    assert Lazy.of(1).bind(lambda x: Lazy.of(x + 1)).bind(lambda x: Lazy.of(x * 2)).get() == 4
    assert Lazy.of(1).bind(lambda x: Lazy.of(x + 1)).bind(lambda x: Lazy.of(x * 2)).to_maybe().get() == 4


# Generated at 2022-06-14 03:33:15.715805
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.maybe import Maybe
    from pymonet.monad_try import Try

    def fn(x):
        return x

    assert Lazy(fn).ap(Lazy(lambda x: x)).get(1) == 1
    assert Lazy(fn).ap(Maybe.just(1)).get() == 1
    assert Lazy(fn).ap(Maybe.nothing()).get() is Lazy(fn).get()
    assert Lazy(fn).ap(Try.of(lambda x: x, 1)).get() == 1


# Generated at 2022-06-14 03:33:24.665145
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.maybe import Maybe
    from pymonet.validation import Validation

    def get_maybe() -> 'Maybe[int]':
        return Lazy.of(123).to_maybe()

    # Without fold
    value = Lazy.of(lambda: get_maybe).bind(lambda x: Lazy.of(x))

    # With fold
    value = Lazy.of(lambda: get_maybe).ap(Lazy.of(lambda x: x)).get()
    assert value == Maybe.just(123)

    def get_validation() -> 'Validation[int, str]':
        return Lazy.of(123).to_validation()

    value = Lazy.of(lambda: get_validation).bind(lambda x: Lazy.of(x)).get()

# Generated at 2022-06-14 03:33:36.425459
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.box import Box

    def assert_lazy(lazy, expected_value):
        result = lazy.get()
        assert result == expected_value

    lazy = Lazy.of(1).map(lambda value: value + 2)
    assert_lazy(lazy.ap(Box(lambda value: value * 3)), 9)
    assert_lazy(lazy.ap(Box(lambda value: value * 4)), 12)
    assert_lazy(lazy.ap(Box(lambda value: value * 5)), 15)

    assert_lazy(Lazy.of(lambda value: value * 5).ap(lazy), 15)
    assert_lazy(Lazy.of(lambda value: value * 6).ap(lazy), 18)



# Generated at 2022-06-14 03:33:39.116905
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    from pymonet.utils import custom_test_equality
    custom_test_equality(Lazy(lambda: 'spam'), Lazy(lambda: 'spam'))



# Generated at 2022-06-14 03:33:47.092697
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    check.equal(Lazy(lambda x: x + 1), Lazy(lambda x: x + 1))
    check.equal(Lazy(lambda x: x + 1).map(lambda x: x + 1), Lazy(lambda x: x + 1).map(lambda x: x + 1))
    check.not_equal(Lazy(lambda x: x + 1), Lazy(lambda x: x + 2))
    check.not_equal(Lazy(lambda x: x + 1).map(lambda x: x + 1), Lazy(lambda x: x + 2).map(lambda x: x + 1))



# Generated at 2022-06-14 03:33:54.570691
# Unit test for method bind of class Lazy
def test_Lazy_bind():  # pragma: no cover
    assert Lazy.of(1).bind(lambda v: Lazy.of(v + 10)) == Lazy.of(11)
    assert Lazy.of(1).bind(lambda v: Lazy.of(v + 1)).bind(lambda v: Lazy.of(v + 10)) == Lazy.of(12)
    assert Lazy.of(25).bind(lambda v: Lazy.of(v + 1)).bind(lambda v: Lazy.of(v + 10)).bind(lambda v: Lazy.of(v * v)) == Lazy.of(676)

# Generated at 2022-06-14 03:34:04.868194
# Unit test for method get of class Lazy
def test_Lazy_get():
    from pymonet.testing import assert_that, are_equal

    assert_that(Lazy.of(None).get(), are_equal(None))
    assert_that(Lazy.of(1).get(), are_equal(1))
    assert_that(Lazy.of(1.1).get(), are_equal(1.1))
    assert_that(Lazy.of('1').get(), are_equal('1'))
    assert_that(Lazy.of([1]).get(), are_equal([1]))
    assert_that(Lazy.of((1,)).get(), are_equal((1,)))
    assert_that(Lazy.of({1}).get(), are_equal({1}))
    assert_that(Lazy.of({1: 1}).get(), are_equal({1: 1}))

# Generated at 2022-06-14 03:34:12.006675
# Unit test for method map of class Lazy
def test_Lazy_map():
    assert Lazy.of('a').map(lambda s: s.upper()) == Lazy.of('A')
    assert Lazy.of('a').map(lambda s: s.upper()).constructor_fn() == Lazy.of('A').constructor_fn()
    assert Lazy.of('a').map(lambda s: Lazy.of(s.upper())).constructor_fn() == Lazy.of('A').constructor_fn()


# Generated at 2022-06-14 03:34:21.286528
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    assert (
        Lazy.of(2).bind(lambda x: Lazy.of(x * 3)).get()
        ==
        Lazy.of(2).bind(lambda x: Lazy.of(x * 3)).constructor_fn()
    )



# Generated at 2022-06-14 03:34:24.982868
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    def equals(fn: Callable[[T], U]) -> None:
        assert Lazy(fn) == Lazy(fn), 'Lazy with same functions should be equals'

    yield equals, lambda x: 1



# Generated at 2022-06-14 03:34:30.041002
# Unit test for method get of class Lazy
def test_Lazy_get():
    from pymonet.box import Box

    value = Lazy.of(5).get()
    assert Box(value).equals(Box(5)) == True

    value = Lazy(lambda: 5).get()
    assert Box(value).equals(Box(5)) == True

    value = Lazy(lambda: 5).get(1)
    assert Box(value).equals(Box(5)) == True

    value = Lazy(lambda x: x).get(5)
    assert Box(value).equals(Box(5)) == True



# Generated at 2022-06-14 03:34:33.834780
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def constructor(*args):
        return 1

    assert Lazy(constructor).bind(lambda x: Lazy.of(x * 2)).get() == 2


# Generated at 2022-06-14 03:34:37.942520
# Unit test for method map of class Lazy
def test_Lazy_map():
    @Lazy
    def fn():
        return 10

    assert fn.map(lambda x: x * 2).get() == 20
    assert fn.map(lambda x: x / 2).get() == 5
    assert fn.map(lambda x: '{}'.format(x)).get() == '10'



# Generated at 2022-06-14 03:34:46.921296
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    fn = lambda: 'test'
    lazy1 = Lazy(fn)
    lazy2 = Lazy(fn)
    lazy3 = Lazy(lambda: 'test2')
    lazy4 = Lazy(lambda: 'test')
    lazy5 = Lazy(lambda: 'test')
    lazy6 = Lazy(lambda: 'test')
    lazy7 = Lazy(lambda: 'test')

    lazy1._compute_value(1)
    lazy4._compute_value(1)
    lazy5._compute_value(1)
    lazy6._compute_value(1)
    lazy7._compute_value(1)

    assert lazy1 == lazy1
    assert lazy1 == lazy5
    assert lazy1 == lazy6
    assert lazy1 == lazy7

    assert lazy1 != lazy2
    assert lazy1

# Generated at 2022-06-14 03:34:53.581219
# Unit test for method get of class Lazy
def test_Lazy_get():
    fn = lambda: Lazy.of(1).get()
    assert fn() == 1

    def double():
        return Lazy.of(2).map(lambda x: x * 2).get()

    assert double() == 4

    def reverse_and_upper(s):
        return Lazy.of(s).map(lambda x: x[::-1].upper()).get()

    assert reverse_and_upper('monad') == 'DANOM'



# Generated at 2022-06-14 03:35:05.989326
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    test_get_2_value = 2

    def add_2(value):
        assert test_get_2_value == value
        assert not add_2.is_called
        add_2.is_called = True

        return Lazy.of(value + test_add_2_value + test_mul_2_value)

    add_2.is_called = False
    test_add_2_value = 2
    test_mul_2_value = 3

    result_add_2 = Lazy(add_2).bind(lambda value: Lazy(lambda *args: value * test_mul_2_value))

    test_result_add_2_value = test_get_2_value * test_mul_2_value + test_add_2_value + test_mul_2_value
   

# Generated at 2022-06-14 03:35:10.311758
# Unit test for method get of class Lazy
def test_Lazy_get():
    def test_function(x):
        return x + 1
    lazy = Lazy(test_function)
    # Test that lazy has not right value
    assert lazy.is_evaluated is False
    assert lazy.value is None
    # Test that lazy can call constructor function
    assert lazy.get(1) == test_function(1)
    # Test that lazy store constructor function results
    assert lazy.is_evaluated is True
    assert lazy.value == test_function(1)


# Generated at 2022-06-14 03:35:21.071853
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.validation import Validation

    # Successful Validation with Lazy
    validation = Validation.success(Lazy(lambda x: x + 'a'))

    # Lazy(Lambda(x: x + 'b')).ap(validation)
    # is the same as
    # Lazy(Lambda(x: Lazy(Lambda(y: x + y)).ap(Success(a)))).ap(Success(b))
    # is the same as
    # Lazy(validation.get().constructor_fn(validation.get()))
    assert validation.ap(Lazy(lambda x: Lazy(lambda y: x + y))).get(None) == 'ab'

# Generated at 2022-06-14 03:35:32.819998
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    def double(x):
        return x + x

    def add(a, b):
        return a + b

    def add_to_double(a):
        return add(a, double(a))

    reference_value = add_to_double(1)

    lazy_value = Lazy(double).ap(Lazy(add).ap(Lazy(lambda x: x + 1)).ap(Lazy(lambda x: x + 1)))

    assert lazy_value.get() == reference_value

# Generated at 2022-06-14 03:35:45.674907
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.validation import Validation
    from pymonet.box import Box

    def mapper(x):
        global counter
        counter += 1
        return Box(x)

    def mapper2(x):
        global counter
        counter += 1
        return Validation.success(x)

    lazy = Lazy(lambda: 1)
    lazy2 = Lazy(lambda: 1)
    counter = 0
    assert lazy.bind(mapper).get() == Box(1)
    assert counter == 1
    assert lazy.bind(mapper) == lazy.bind(mapper)
    assert lazy.bind(mapper) == lazy2.bind(mapper)
    assert lazy2.bind(mapper) == lazy.bind(mapper)

# Generated at 2022-06-14 03:35:49.095707
# Unit test for method map of class Lazy
def test_Lazy_map():
    assert Lazy.of(5).map(lambda x: x + 10) == Lazy(lambda x: 15)



# Generated at 2022-06-14 03:35:57.148015
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.box import Box
    from pymonet.validation import Errors, Validation

    lazy = Lazy.of(2)

    assert lazy.bind(lambda x: Box(x*2)).get() == Box(4)
    assert lazy.bind(lambda x: Box(x*2)).get() == lazy.get()
    assert lazy.bind(lambda x: Box(x*2)).get() == 4

    try:
        lazy.bind(lambda x: Validation.failure(Errors([x])))
    except ValueError as e:
        assert str(e) == 'Lazy.get() must not raise an error'

    assert lazy.bind(lambda x: Validation.failure(Errors([x]))).to_validation() == Validation.failure(Errors([2]))

# Generated at 2022-06-14 03:35:59.550400
# Unit test for method get of class Lazy
def test_Lazy_get():
    def return_one() -> int:
        return 1

    assert return_one() == Lazy(return_one).get()



# Generated at 2022-06-14 03:36:11.044868
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    assert Lazy.of(ValueError).map(lambda e: str(e)).__eq__(Lazy.of(ValueError).map(lambda e: str(e)))
    assert Lazy.of(ValueError).map(lambda e: str(e)).__eq__(Lazy.of(ValueError).map(lambda e: e.__str__()))
    assert not Lazy.of(ValueError).map(lambda e: str(e)).__eq__(Lazy.of(ValueError))
    assert not Lazy.of(ValueError).map(lambda e: str(e)).__eq__(Lazy.of(ValueError).map(lambda e: str(e) * 2))

# Generated at 2022-06-14 03:36:17.696006
# Unit test for method __eq__ of class Lazy

# Generated at 2022-06-14 03:36:20.060181
# Unit test for method get of class Lazy
def test_Lazy_get():
    test = Lazy(lambda: 1)

    assert test.get() == 1



# Generated at 2022-06-14 03:36:22.532902
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from .box_test import test_Box_bind

    test_Box_bind(Lazy)



# Generated at 2022-06-14 03:36:28.339149
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    constructor = Lazy(lambda *args: 1)
    assert constructor != None  # noqa
    assert constructor != object()
    assert constructor != Lazy(lambda *args: 2)
    assert constructor != Lazy(lambda *args: 1)
    assert constructor == Lazy(lambda *args: 1)


# Generated at 2022-06-14 03:36:40.841309
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    """
    >>> def fn(value):
    ...     return Lazy.of(value + 1)
    ...
    >>> Lazy.of(2).bind(fn).get()
    3
    >>> Lazy.of(2).bind(fn).get()
    3
    >>> Lazy.of(2).bind(fn).map(lambda x: x + 1).get()
    4
    >>> def fn2(value):
    ...     return Lazy.of(value + 2)
    ...
    >>> Lazy.of(2).bind(fn).bind(fn2).get()
    5
    """
    pass

# Generated at 2022-06-14 03:36:44.645512
# Unit test for method get of class Lazy
def test_Lazy_get():
    def test_get(value, expected):
        def f(x):
            assert x == value
            return 5

        assert Lazy(f).get(value) == expected

    test_get(1, 5)
    test_get(2, 5)

# Generated at 2022-06-14 03:36:49.566595
# Unit test for method get of class Lazy
def test_Lazy_get():
    assert Lazy.of(5).get() == 5
    assert Lazy.of(5).map(lambda x: x + 2).get() == 7
    assert Lazy.of(5).bind(lambda x: Lazy.of(x + 2)).get() == 7

# Generated at 2022-06-14 03:36:54.827991
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():  # pragma: no cover
    def fn(*args):
        return 2

    def fn2(*args):
        return 3

    lazy_fn = Lazy(fn)
    lazy_fn2 = Lazy(fn2)

    assert lazy_fn == lazy_fn
    assert lazy_fn == lazy_fn2

    assert lazy_fn != None
    assert lazy_fn != 1

# Generated at 2022-06-14 03:36:58.166750
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    assert (
        Lazy.of(3).bind(lambda x: Lazy.of(x * 4)).get(1)
    ), 12

# Generated at 2022-06-14 03:37:02.606840
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def fn(arg1):
        return Lazy(lambda arg2: arg1 + arg2)

    def fn2(arg1):
        return arg1 * 3

    assert Lazy(lambda arg: fn2(arg)).bind(fn).get(1) == 4



# Generated at 2022-06-14 03:37:09.986915
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    def f(x):
        return Lazy.of(lambda y: x + y)

    assert Lazy(lambda x : x + 1).ap(f(10)) == Lazy(lambda x : 11 + x)
    assert Lazy(lambda x : x + 1).ap(Lazy.of(10)) == Lazy(lambda x : 10 + x)
    assert Lazy(lambda x : x + 1).ap(Lazy.of(10)).ap(f(2)) == Lazy(lambda x : 13 + x)


# Generated at 2022-06-14 03:37:13.605440
# Unit test for method map of class Lazy
def test_Lazy_map():
    def init_fn(a):
        return a + 1

    result = Lazy(init_fn).map(lambda a: a * 2).map(lambda a: a * 3).get(10)

    assert result == init_fn(10) * 2 * 3



# Generated at 2022-06-14 03:37:18.847875
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():  # pragma: no cover
    from utils import identity

    lazy_identity = Lazy(identity)
    assert lazy_identity == lazy_identity
    assert lazy_identity == lazy_identity.map(identity)

    assert Lazy(identity) == Lazy(identity)
    assert Lazy(identity) != Lazy(
        lambda x: x + 1)

    assert lazy_identity == Lazy(identity)
    assert lazy_identity != Lazy(lambda x: x + 1)


# Generated at 2022-06-14 03:37:26.296320
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    from pymonet.validation import Validation
    from pymonet.box import Box

    assert Lazy(lambda: 0) == Lazy(lambda: 0)
    assert Lazy(lambda: 0) == Lazy.of(0)
    assert Lazy(lambda: Box(0)) == Lazy.of(Box(0))
    assert Lazy(lambda: [0]) == Lazy.of([0])
    assert Lazy(lambda: 0) != Lazy(lambda: 1)
    assert Lazy(lambda: 0) != Validation.success(0)


# Generated at 2022-06-14 03:37:47.391223
# Unit test for method map of class Lazy
def test_Lazy_map():  # pragma: no cover
    from pymonet.box import Box
    from pymonet.monad_try import Try
    from pymonet.validation import Validation

    lazy = Lazy.of(2).map(lambda x: x ** 2)

    assert lazy.get() == 4

    lazy = Lazy.of(2).map(lambda x: Box(x ** 2))
    assert isinstance(lazy.get(), Box)
    assert lazy.get().get() == 4

    lazy = Lazy.of(2).map(lambda x: Try.of(lambda: x ** 2)).map(lambda x: x.get())
    assert isinstance(lazy.get(), Try)
    assert lazy.get().get() == 4


# Generated at 2022-06-14 03:37:53.977492
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    from pymonet.monad_try import Try
    from pymonet.maybe import Maybe

    assert Lazy(lambda: 1) == Lazy(lambda: 1)
    assert Lazy(lambda: 1).to_maybe() == Lazy(lambda: 1).to_maybe()
    assert Lazy(lambda: 1).to_try() == Lazy(lambda: 1).to_try()
    assert Try.of(lambda: 1) == Lazy(lambda: 1).to_try()
    assert Lazy(lambda: 1) == Try.of(lambda: 1)
    assert Lazy(lambda: 1).to_maybe() == Maybe.just(1)
    assert Lazy(lambda: 1) == Maybe.just(1)
    assert Try.of(lambda: 1) == Maybe.just(1)
    assert Maybe.just(1)

# Generated at 2022-06-14 03:37:59.504598
# Unit test for method map of class Lazy
def test_Lazy_map():
    fold_fn = lambda x: x

    def mapper_fn(x: str) -> float:
        return float(x)

    assert Lazy(fold_fn).map(mapper_fn).get('1.1') == 1.1


# Generated at 2022-06-14 03:38:04.453366
# Unit test for method get of class Lazy
def test_Lazy_get():  # pragma: no cover
    def test_fn():
        test_val = 1
        return test_val

    assert Lazy.of(1).get() == 1
    assert Lazy.of(test_fn).get() == test_fn()
    assert Lazy.of(test_fn).get(1, 2) == test_fn(1, 2)


# Generated at 2022-06-14 03:38:09.290313
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def f(a):
        return Lazy(lambda *args: a + 1)

    def g(a):
        return Lazy(lambda *args: a + 2)

    def h(a):
        return Lazy(lambda *args: a + 3)

    # 7 = ((1+2) + 3) + 4
    assert Lazy.of(1).bind(f).bind(g).bind(h).get() == 7

# Generated at 2022-06-14 03:38:12.551900
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():  # pragma: no cover
    assert Lazy(lambda *args: Error(args[0])) != Lazy(lambda *args: Error(args[0]))
    assert not Lazy(lambda *args: Error(args[0])) == Lazy(lambda *args: Error(args[0]))

# Generated at 2022-06-14 03:38:17.325711
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():  # pragma: no cover
    lazy1 = Lazy(lambda x: x)
    lazy2 = Lazy(lambda y: y)
    assert lazy1 == lazy2

    lazy3 = Lazy(lambda z: z)
    lazy3._compute_value(42)
    assert lazy3 != lazy1


# Generated at 2022-06-14 03:38:25.945984
# Unit test for method get of class Lazy
def test_Lazy_get():  # pragma: no cover
    from pymonet.box import Box
    from pymonet.either import Right
    from pymonet.maybe import Maybe

    def add1(x):
        return x + 1

    def multiply(x, y):
        return x * y

    assert Lazy(lambda: 1).get() == 1
    assert Lazy(lambda: 1).map(add1).get() == 2
    assert Lazy(lambda: 1).map(lambda x: 2).map(add1).get() == 3
    assert Lazy(lambda x: 2).bind(lambda x: Lazy(lambda: x + 1)).get(1) == 3
    assert Lazy(lambda: 1).bind(lambda x: Lazy(lambda: x + 1)).get() == 2

# Generated at 2022-06-14 03:38:31.328992
# Unit test for method get of class Lazy
def test_Lazy_get():  # pragma: no cover
    from random import random
    from decimal import Decimal

    assert Lazy.of(Decimal(0)).get() == Decimal(0)

    assert (
        Lazy.of(Decimal(0))
        .map(lambda val: val + Decimal(1))
        .map(lambda val: val - Decimal(1))
        .map(lambda val: val * Decimal(2))
        .get()
        == Decimal(0)
    )


# Generated at 2022-06-14 03:38:39.998788
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    def _test(a, b):
        return a + b

    lazy_1 = Lazy.of(lambda x: x * 2)
    lazy_2 = Lazy.of(lambda x: x + 2)

    test_2 = lazy_1.ap(lazy_2)

    assert test_2.constructor_fn(3) == 10

    def _test_3(x):
        return x + 3

    lazy_3 = Lazy.of(_test_3)

    test_3 = lazy_1.ap(lazy_3)

    assert test_3.constructor_fn(2) == 7

# Generated at 2022-06-14 03:38:54.170176
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    # when
    result = Lazy.of(1).bind(lambda x: Lazy.of(x + 2))

    # then
    assert Lazy.of(3) == result

# Generated at 2022-06-14 03:38:59.994839
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.box import Box

    def sum(x, y):
        return x + y

    lazy_sum = Lazy(lambda _: sum(2, 3))

    assert lazy_sum.bind(lambda _: Lazy.of(Box.of(10))) == Lazy(lambda _: Box.of(10))

    assert lazy_sum.bind(lambda result: Lazy.of(Box.of(10 + result))) == Lazy(lambda _: Box.of(15))



# Generated at 2022-06-14 03:39:03.584159
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    assert Lazy(lambda: 1).bind(lambda x: Lazy(lambda: x + 1)).constructor_fn() == 2
    assert Lazy(lambda: 1).bind(lambda x: Lazy(lambda: x)).get() == 1



# Generated at 2022-06-14 03:39:13.737864
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def inc(x):
        return x + 1

    def sum(a, b):
        return a + b

    # Given
    inc_lazy = Lazy(inc)
    sum_lazy = Lazy(sum)
    lazy = Lazy.of(0)
    one = Lazy.of(1)

    # When
    result = one.bind(inc_lazy).bind(inc_lazy).bind(inc_lazy)
    result_2 = lazy.bind(inc_lazy).bind(inc_lazy).bind(inc_lazy)
    result_3 = lazy.bind(inc_lazy).bind(inc_lazy).bind(inc_lazy).bind(inc_lazy).bind(inc_lazy).bind(inc_lazy)

# Generated at 2022-06-14 03:39:16.583682
# Unit test for method map of class Lazy
def test_Lazy_map():
    LazyValue = Lazy(lambda x: x * x)

    assert LazyValue.map(lambda x: x + 1).get(2) == 5



# Generated at 2022-06-14 03:39:19.672037
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    assert Lazy.of(2).ap(Lazy.of(lambda x: x+2)) == Lazy.of(4)



# Generated at 2022-06-14 03:39:27.081721
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.monad_list import List

    simple_fn = lambda x: x
    assert Lazy.of(1).bind(Lazy.of).bind(simple_fn).get() == 1

    assert Lazy.of(1).bind(
        lambda x: Lazy.of(2).bind(
            lambda y: List([x, y]).bind(
                lambda z: Lazy.of(z)
            )
        )
    ).get() == [1, 2]

# Generated at 2022-06-14 03:39:35.787536
# Unit test for method map of class Lazy
def test_Lazy_map():
    from pymonet.maybe import Maybe
    from pymonet.box import Box
    from pymonet.validation import Validation

    lazy = Lazy(lambda: 10)

    assert lazy.map(lambda x: x + 5).get() == 15
    assert lazy.map(lambda x: x * 2).get() == 20

    assert isinstance(lazy.map(lambda x: Maybe.just(x + 5)), Lazy)
    assert lazy.map(lambda x: Box(x + 5)).get().get_value() == 15
    assert lazy.map(lambda x: Validation.success(x + 5)).get().get_value() == 15


# Generated at 2022-06-14 03:39:38.694403
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    assert Lazy.of(1).bind(lambda x: Lazy.of(x + 1)).get() == 2

# Generated at 2022-06-14 03:39:46.954017
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    """
    Unit test for method __eq__ of class Lazy.
    """
    assert Lazy.of(lambda x: x + 2) == Lazy.of(lambda y: y + 2)

    assert Lazy.of(lambda x: x + 2) != Lazy.of(lambda y: y + 3)

    assert Lazy.of(lambda x: x + 2) != "Lazy.of(lambda x: x + 2)"

    assert Lazy.of(lambda x: x + 2).bind(lambda x: Lazy.of(x + 2)) == Lazy.of(lambda x: x + 2).bind(lambda x: Lazy.of(x + 2))


# Generated at 2022-06-14 03:40:12.029878
# Unit test for method get of class Lazy
def test_Lazy_get():
    """
    Unit test for method get of class Lazy
    """
    assert Lazy.of('1').get() == '1'
    assert Lazy.of(1).get() == 1
    assert Lazy.of(None).get() is None



# Generated at 2022-06-14 03:40:21.111339
# Unit test for method get of class Lazy
def test_Lazy_get():
    def t_with_args(x):
        return x+1

    assert Lazy.of(0).get() == 0
    assert Lazy.of(1).get() == 1
    assert Lazy(lambda: 1).get() == 1
    assert Lazy(lambda: 0).get() == 0
    assert Lazy(lambda x: x).get(1) == 1
    assert Lazy(lambda x, y, z: x+y+z).get(1,2,3) == 6
    assert Lazy(t_with_args).get(1) == 2


# Generated at 2022-06-14 03:40:26.063525
# Unit test for method bind of class Lazy
def test_Lazy_bind():

    def fn(x):
        print(x + 2)
        return Lazy.of(x + 2)

    def fn2(x):
        print(x * 2)
        return Lazy.of(x * 2)

    assert Lazy.of(1).bind(fn).bind(fn2).get() == 6


# Generated at 2022-06-14 03:40:28.800055
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def fn1(arg):
        return arg

    def fn2(arg):
        return Lazy(lambda *args: fn1(arg))

    assert Lazy(fn1).bind(fn2).get() == fn1(None)



# Generated at 2022-06-14 03:40:34.043635
# Unit test for method bind of class Lazy
def test_Lazy_bind():  # pragma: no cover
    def f(x):
        return Lazy(lambda: x ** 2)

    def g(x):
        return Lazy(lambda: x ** 3)

    assert Lazy(lambda: 10).bind(f).bind(g).get() == 1000
    assert Lazy(lambda: 10).bind(g).bind(f).get() == 10000

# Generated at 2022-06-14 03:40:35.889663
# Unit test for method get of class Lazy
def test_Lazy_get():
    """
    Method get of class Lazy
    """
    assert Lazy.of('a').get() == 'a'



# Generated at 2022-06-14 03:40:39.110231
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    assert Lazy.of(1).bind(
        lambda x: Lazy.of(x + 2)
    ).get() == 3



# Generated at 2022-06-14 03:40:45.582718
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    assert Lazy.of(5) == Lazy.of(5)
    assert Lazy(lambda: 5) == Lazy(lambda: 5)
    assert not Lazy(lambda: 5) == Lazy(lambda: 7)
    assert not Lazy.of(5) == Lazy.of(7)
    assert Lazy(lambda: 5) != Lazy(lambda: 7)
    assert Lazy.of(5) != Lazy.of(7)
    assert not Lazy.of(5) == Lazy(lambda: 5)



# Generated at 2022-06-14 03:40:47.369397
# Unit test for method get of class Lazy
def test_Lazy_get():
    assert Lazy(lambda x: x).get(42) == 42



# Generated at 2022-06-14 03:40:58.178616
# Unit test for method map of class Lazy
def test_Lazy_map():
    def simple_fn(x):
        return x * 2

    def nested_fn(x):
        def inner_fn(y):
            return y * 2

        return Lazy.of(inner_fn(x))

    assert repr(Lazy.of(1).map(simple_fn)) == 'Lazy[fn=<function Lazy.__init__.<locals>.<lambda> at 0x7f5f5d7f5158>, value=None, is_evaluated=False]'
    assert repr(Lazy.of(1).map(nested_fn)) == 'Lazy[fn=<function Lazy.__init__.<locals>.<lambda> at 0x7f5f5d4ef488>, value=None, is_evaluated=False]'

    assert Lazy.of(1).map(simple_fn).get