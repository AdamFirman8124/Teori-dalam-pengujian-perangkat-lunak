

# Generated at 2022-06-14 03:31:33.573270
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    def fn(a):
        return a - 5

    lazy_fn = Lazy.of(fn)
    lazy_a = Lazy.of(2)
    lazy_result = lazy_fn.ap(lazy_a)

    assert lazy_result.get() == -3



# Generated at 2022-06-14 03:31:35.069494
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    assert Lazy.of(1) == Lazy.of(1)



# Generated at 2022-06-14 03:31:38.838406
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    """
    Should returns new Lazy with result of Lazy constructor function applied to function in argument.
    """
    from pymonet.functors.functor import Functor
    from pymonet.monad_state import MonadState

    def add_one(x):
        return x + 1

    def multiply_two(x):
        return x * 2

    assert Lazy(add_one).ap(Lazy(multiply_two)).constructor_fn(42) == 84
    assert Lazy(2).ap(Lazy(4)).constructor_fn() == 8



# Generated at 2022-06-14 03:31:42.888716
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    # arrange
    lazy = Lazy(lambda: 1)
    fn = lambda arg: arg + 1
    seq1 = (2, 3, 4)
    seq2 = (1, 1, 1)

    # act & assert
    assert lazy.bind(fn).get() == 2
    assert lazy.get(*seq1) == 1
    assert lazy.get(*seq2) == 1
    assert lazy.bind(lambda arg: Lazy(lambda: arg)).bind(fn).get() == 2
    assert lazy.bind(lambda arg: Lazy(lambda: arg)).get(*seq1) == 1
    assert lazy.bind(lambda arg: Lazy(lambda: arg)).get(*seq2) == 1

# Generated at 2022-06-14 03:31:46.358606
# Unit test for method get of class Lazy
def test_Lazy_get():
    lazy = Lazy(lambda: 1+1)

    assert lazy.is_evaluated is False
    assert lazy.get() == 2
    assert lazy.is_evaluated is True


# Generated at 2022-06-14 03:31:50.272282
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    fn = lambda x: x
    assert Lazy(fn) == Lazy(fn)
    lazy = Lazy(fn)
    lazy.get(1)
    assert Lazy(fn) == lazy
    assert Lazy(fn) != Lazy(lambda x: x + 1)


# Generated at 2022-06-14 03:32:01.670162
# Unit test for method map of class Lazy
def test_Lazy_map():
    assert Lazy(lambda x: x).map(lambda x: x + 2)(2) == 4
    assert Lazy(lambda: 0).map(lambda x: x + 2)(2) == 2
    assert Lazy(lambda x: x).map(lambda x: x + 2).map(lambda x: x + 3)(2) == 9
    assert Lazy(lambda x: x).map(lambda x: x + 2).map(lambda x: x + 3).map(lambda x: x * 3)(2) == 27
    assert Lazy(lambda x: x + 2).map(lambda x: x * 2)(2) == 8
    assert Lazy(lambda x: x).map(lambda x: x + 2).map(lambda x: x + 3)(4) == 9

# Generated at 2022-06-14 03:32:07.587530
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    assert Lazy.of("abc").ap(Lazy.of(lambda s: s.upper())).get() == "ABC"
    assert Lazy.of("abc").ap(Lazy.of(lambda s: s.upper())).to_maybe(None) == Maybe.just("ABC")
    assert Lazy.of("abc").ap(Lazy.of(lambda s: s.upper())).to_try() == Try.of(lambda s: s.upper, "abc")
    assert Lazy.of("abc").ap(Lazy.of(lambda s: s.upper())).to_either() == Either.right("ABC")
    assert Lazy.of("abc").ap(Lazy.of(lambda s: s.upper())).to_validation() == Validation.success("ABC")

# Generated at 2022-06-14 03:32:17.943865
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.monad_try import Try

    assert Lazy.of(2).ap(Lazy.of(lambda x: x + 10)) == Lazy.of(12)

    assert Lazy.of(2).ap(Lazy.of(lambda x: x + 10)).ap(Lazy.of(lambda x: x - 1)) == Lazy.of(11)

    assert Lazy.of(2).ap(Lazy.of(lambda x: x + 10)).ap(Lazy.of(lambda x: x - 1)).ap(Lazy.of(lambda x: x * 2)) == \
           Lazy.of(22)

    def raz(x):
        return x / 0

    assert Lazy.of(2).ap(Lazy.of(raz)).to_try() == Try.of(raz, 2)

# Generated at 2022-06-14 03:32:25.830574
# Unit test for method get of class Lazy
def test_Lazy_get():
    assert Lazy.of(True).get() == True
    assert Lazy.of(1).get() == 1
    assert Lazy.of(1.5).get() == 1.5
    assert Lazy.of('aaa').get() == 'aaa'
    assert Lazy.of(['a']).get() == ['a']
    assert Lazy.of((1, '1')).get() == (1, '1')


# Generated at 2022-06-14 03:32:30.984538
# Unit test for method get of class Lazy
def test_Lazy_get():
    fn = lambda x: x + 2
    lazy = Lazy(fn)

    assert lazy.get(2) == 4



# Generated at 2022-06-14 03:32:34.214653
# Unit test for method map of class Lazy
def test_Lazy_map():
    assert Lazy(lambda x: [1, 2, 3]).map(lambda x: x + [4]).get(None) == [1, 2, 3, 4]


# Generated at 2022-06-14 03:32:45.580111
# Unit test for method get of class Lazy
def test_Lazy_get():  # pragma: no cover
    """
    Test method Lazy.get
    """
    # Test: Lazy return stored value if is evaluated
    assert Lazy.of(1).get() == 1

    # Test: Lazy return value of stored function if is evaluated
    assert Lazy(lambda: 1).get() == 1

    # Test: Lazy return value of stored function and memoize this value
    some = Lazy(lambda: 1)
    assert some.get() == 1
    assert some.is_evaluated is True
    assert some.value == 1

    # Test: Lazy return value of stored function with arguments and memoize this value
    some = Lazy(lambda x, y: x + y)
    assert some.get(1, 1) == 2
    assert some.is_evaluated is True
    assert some.value == 2

# Generated at 2022-06-14 03:32:51.546995
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__(): # pragma: no cover
    from pymonet.functor import Functor

    fn = lambda *args, **kwargs: 1
    lazy = Lazy(fn)
    functor = Functor.of(1)

    assert lazy == lazy
    assert lazy != functor
    assert lazy == Lazy(fn)
    assert lazy != Lazy(lambda: 1)



# Generated at 2022-06-14 03:32:55.082273
# Unit test for method map of class Lazy
def test_Lazy_map():
    lazy = Lazy(lambda x: x * 4)

    mapped = lazy.map(lambda x: x/2)

    assert mapped.constructor_fn(2) == 4


# Generated at 2022-06-14 03:32:59.897165
# Unit test for method bind of class Lazy
def test_Lazy_bind():  # pragma: no cover
    assert (
        Lazy.of(1)
        .bind(lambda x: Lazy.of(x + 2))
        .get()
    ) == 3



# Generated at 2022-06-14 03:33:07.273652
# Unit test for method map of class Lazy
def test_Lazy_map():  # pragma: no cover
    def compute_value() -> int:
        return 1

    lazy = Lazy(compute_value)

    assert lazy.map(lambda x: x + 1).get() == 2
    assert lazy.map(lambda x: x + 1).get() == 2
    assert lazy.map(lambda x: x + 1).get() == 2
    assert lazy.is_evaluated is True
    assert lazy.value == 1


# Generated at 2022-06-14 03:33:18.041161
# Unit test for method get of class Lazy
def test_Lazy_get():  # pragma: no cover
    from pymonet.box import Box
    from pymonet.maybe import Maybe
    from pymonet.either import Right
    from pymonet.monad_try import Try
    from pymonet.validation import Validation

    def sum_a_b_plus_one(a, b):
        return a + b + 1

    def divide_a_by_b(a, b):
        return a / b

    def raise_value_error(a, b):
        raise ValueError('Value error a, b = {}, {}'.format(a, b))

    box = Box(2)

    assert Lazy(sum_a_b_plus_one).get(1, 1) == 4
    assert Lazy(divide_a_by_b).get(1, 0) == 1
   

# Generated at 2022-06-14 03:33:22.033696
# Unit test for method get of class Lazy
def test_Lazy_get():
    def function():
        return 'Hello'

    lazy_hello = Lazy(function)

    assert lazy_hello.get() == 'Hello'
    assert lazy_hello.get() == 'Hello'


# Generated at 2022-06-14 03:33:28.846897
# Unit test for method bind of class Lazy
def test_Lazy_bind():  # pragma: no cover
    from pymonet.identity import Identity
    from pymonet.writer import Writer

    def double(x):
        return x * 2

    def add_num(x):
        return x + 10

    def double_add_num(x):
        return double(add_num(x))

    lazy = Lazy(double)
    assertion = Lazy(double).bind(lambda a: Lazy(add_num).map(lambda b: a + b))

    assert lazy.bind(lambda x: Lazy(add_num).map(lambda y: x + y)).get(2) == assertion.get(2)

    assert lazy.bind(lambda x: Lazy(add_num).map(lambda y: x + y)).get(2) == double_add_num(2)


# Generated at 2022-06-14 03:33:42.369188
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    # pylint: disable=W0142
    def f(a):
        return a

    def g(a):
        return a + 1

    def g1(a, *args):
        return a + 1

    def g2(a):
        return a + 1

    def g3(a):
        return a + 1

    def f1(a, b):
        return a

    def f2(a):
        return a

    def f3(a):
        return a

    def f4(a):
        return a

    def f5(a):
        return a

    def f6(a):
        return a

    def f7(a):
        return a

    def f8(a):
        return a

    def f9(a):
        return a


# Generated at 2022-06-14 03:33:47.967085
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    """
    Unit test for method bind.
    """
    assert Lazy(lambda x: x).bind(lambda x: Lazy(lambda: x)).get(1) == 1
    assert Lazy(lambda x: x).bind(lambda x: Lazy(lambda: x)).get(2) == 2
    assert Lazy(lambda x: x).bind(lambda x: Lazy(lambda: x)).get(3) == 3

# Generated at 2022-06-14 03:33:53.855599
# Unit test for method map of class Lazy
def test_Lazy_map():
    assert Lazy(lambda x: x - 1).map(lambda x: x * 2).get(1) == 0
    assert Lazy(lambda x: x - 1).map(lambda x: x * 2).get(2) == 2
    assert Lazy(lambda x: x - 1).map(lambda x: x * 2).get(3) == 4
    assert Lazy(lambda x: x - 1).map(lambda x: x * 2).get(4) == 6


# Generated at 2022-06-14 03:34:00.830516
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    double = lambda x: 2 * x
    add_10 = lambda x: 10 + x

    double_lazy = Lazy(double)

    new_lazy = double_lazy.bind(lambda x: Lazy(add_10(x)))
    assert new_lazy.get(8) == 26
    assert new_lazy.is_evaluated
    assert double_lazy.is_evaluated

# Generated at 2022-06-14 03:34:13.147049
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    assert Lazy(lambda x: x).__eq__(Lazy(lambda x: x)) is True
    assert Lazy(lambda x: x).__eq__(Lazy(lambda x: 1)) is False
    assert Lazy(lambda x: x).__eq__(Lazy(lambda x: x).map(lambda x: x)) is True
    assert Lazy(lambda x: x).__eq__(Lazy(lambda x: x).map(lambda x: 1)) is False
    assert Lazy(lambda x: x).map(lambda x: x).__eq__(Lazy(lambda x: x)) is False
    assert Lazy(lambda x: x).map(lambda x: x).__eq__(Lazy(lambda x: x).map(lambda x: x)) is True

# Generated at 2022-06-14 03:34:18.885995
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    fn0 = lambda: 'a'
    fn1 = lambda x: Lazy.of(x + 'b')
    fn2 = lambda x: Lazy.of(x + 'c')
    fn3 = lambda x: Lazy.of(x + 'd')

    lazy = Lazy(fn0).bind(fn1).bind(fn2).bind(fn3)
    assert lazy.constructor_fn() == 'abcd'



# Generated at 2022-06-14 03:34:29.748012
# Unit test for method __eq__ of class Lazy

# Generated at 2022-06-14 03:34:35.248691
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def fn_to_call(number: int) -> Lazy[int, str]:
        return Lazy(lambda: '{}'.format(number))

    lazy = Lazy(lambda: 5)

    assert lazy.bind(fn_to_call) == Lazy(lambda: '5')


# Generated at 2022-06-14 03:34:44.771742
# Unit test for method get of class Lazy
def test_Lazy_get():  # pragma: no cover
    def multiply(value):
        return value * 2

    def multiply_by_3(value):
        return value * 3

    lazy = Lazy(multiply_by_3)

    assert lazy.get(5) == 15
    assert lazy.get(5) == 15 # test memoization

    mapper = lambda value: value * 5
    lazy_1 = lazy.map(mapper)

    assert lazy_1.get(5) == lazy.get(5) * 5
    assert lazy_1.get(5) == lazy.get(5) * 5 # test memoization
    assert lazy_1.get(5) == lazy.get(5) * 5

    lazy_2 = lazy.bind(lambda value: Lazy(multiply).map(mapper))


# Generated at 2022-06-14 03:34:51.916925
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    from pymonet.immutable import Lazy

    # given
    value = 10
    lazy_one = Lazy(lambda: value)
    lazy_two = Lazy(lambda: value)
    lazy_three = Lazy(lambda: value * 2)

    # when
    lazy_one.get()
    lazy_two.get()
    lazy_three.get()

    # then
    assert lazy_one != lazy_three
    assert lazy_one == lazy_two

# Generated at 2022-06-14 03:35:09.278017
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    fn = Lazy.of(lambda x: x * 2)
    x = Lazy.of(3)
    assert x.ap(fn) == Lazy.of(6)

    fn = Lazy.of(lambda x: x * 2)
    x = Lazy.of(None)
    assert x.ap(fn) == Lazy.of(None)

    # for more details visit https://github.com/plippe/pymonet/issues/8
    fn = Lazy.of(lambda x: x * 2)
    x = Lazy.of(3)
    assert x.map(fn.get).to_maybe() == x.ap(fn).to_maybe()



# Generated at 2022-06-14 03:35:13.224304
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    add_number = lambda x: Lazy(lambda *args: x + 1)
    result = Lazy.of(1).bind(add_number).get()

    assert result == 2



# Generated at 2022-06-14 03:35:16.774583
# Unit test for method map of class Lazy
def test_Lazy_map():
    from pymonet.functoolz import identity

    lazy = Lazy(lambda x: x + 1)
    assert lazy.map(identity) == Lazy(lambda x: x + 1)


# Generated at 2022-06-14 03:35:26.601948
# Unit test for method map of class Lazy
def test_Lazy_map(): # pragma: no cover
    class A(object):
        def __init__(self, value):
            self.value = value

        def __str__(self):
            return 'LazyA[{}]'.format(self.value)

    class B(object):
        def __init__(self, value):
            self.value = value

        def __str__(self):
            return 'LazyB[{}]'.format(self.value)

    def mapper(a: A) -> B:
        return B(a.value + 1)

    def constructor_fn(*args):
        return A(args[0])

    assert Lazy(constructor_fn).map(mapper).get(2) == B(3)

# Generated at 2022-06-14 03:35:29.747702
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def add_one(x: int) -> int:
        return x + 1

    def multiply(x: int, y: int) -> int:
        return x * y

    assert Lazy(add_one).bind(lambda x: Lazy(lambda: multiply(x, 2))).get(1) == 4

# Generated at 2022-06-14 03:35:39.160250
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    @Lazy
    def id_Lazy(value):
        return value

    assert Lazy.of(1) == Lazy.of(1)
    assert id_Lazy(1) == id_Lazy(1)
    assert id_Lazy(1) == Lazy.of(1)
    assert id_Lazy(1).map(lambda x: x + 1) == Lazy.of(2)
    assert id_Lazy(1).map(lambda x: x + 1) != Lazy.of(1)



# Generated at 2022-06-14 03:35:43.343993
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    lazy = Lazy.of(2)

    mapper = lambda x: Lazy.of(x + 2)

    assert lazy.bind(mapper).get() == 4



# Generated at 2022-06-14 03:35:50.029807
# Unit test for method bind of class Lazy
def test_Lazy_bind():  # pragma: no cover
    def fn_1(a):
        def fn_2(b):
            return b + a

        return fn_2

    assert Lazy(fn_1).bind(lambda fn: Lazy(fn(3))).get(2) == 5
    assert Lazy(fn_1).map(lambda fn: fn(2)).get(3) == 4
    assert Lazy.of(4).get() == 4
    assert Lazy.of(5).map(lambda x: x + 1).get() == 6
    assert Lazy.of(3).ap(Lazy.of(lambda x: x + 3)).get() == 6

# Generated at 2022-06-14 03:35:57.315887
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    assert str(Lazy.of(1).bind(lambda x: Lazy.of(x + 2))) == 'Lazy[fn=function <lambda> at 0x106c6e510, value=None, is_evaluated=False]'
    assert Lazy.of(1).bind(lambda x: Lazy.of(x + 2)).get() == 3


# Generated at 2022-06-14 03:36:00.023092
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    assert Lazy.of('2').ap(Lazy.of(lambda x: int(x[0]) * int(x[0]))) == Lazy.of(4)



# Generated at 2022-06-14 03:36:17.424572
# Unit test for method map of class Lazy
def test_Lazy_map():
    def f(x: int): return x + 1
    def g(x: int): return x * 2

    lazy = Lazy(lambda x: x + 1)
    lazy_map = lazy.map(lambda x: x * 2)

    assert Lazy(g).bind(f) == lazy_map


# Generated at 2022-06-14 03:36:25.844735
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    def fn1(x: int) -> int:
        return x

    def fn2(x: int) -> int:
        return x + 1

    assert Lazy.of(0) != object()
    assert Lazy(fn1) != Lazy(fn1)
    assert Lazy(fn1) != Lazy(fn2)
    assert Lazy(fn1) != Lazy.of(0)
    assert Lazy.of(0) == Lazy(fn1).to_box(0)
    assert Lazy.of(0) == Lazy(fn1).to_either(0)
    assert Lazy.of(0) == Lazy(fn1).to_maybe(0)
    assert Lazy.of(0) != Lazy(fn1).to_try(0)
    assert Lazy.of(0)

# Generated at 2022-06-14 03:36:31.445815
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    # given
    my_lazy = Lazy(lambda: 1) \
        .map(lambda x: x + 1) \
        .bind(lambda x: Lazy(lambda: x + 2))

    # when
    result = my_lazy.get()

    # then
    assert result == 4, result



# Generated at 2022-06-14 03:36:35.390961
# Unit test for method map of class Lazy
def test_Lazy_map():
    from pymonet.box import Box

    assert Lazy(lambda: 4).map(lambda x: x + 2).get() == 6
    assert Lazy(lambda: Box(4)).map(lambda x: x + 2).get() == 6



# Generated at 2022-06-14 03:36:39.485961
# Unit test for method map of class Lazy
def test_Lazy_map():  # pragma: no cover
    def fn(val): return val + 1

    assert Lazy(fn).map(lambda val: val * 10).get(1) == 20
    assert Lazy(fn).map(lambda val: val * 10).map(lambda val: val * 5).get(1) == 100



# Generated at 2022-06-14 03:36:43.840492
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def fn(x: int) -> str:
        return str(x + 5)

    assert Lazy(lambda x: x + 5).bind(lambda y: Lazy(lambda x: fn(x))).get(5) == "10"

# Generated at 2022-06-14 03:36:50.097020
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    from pymonet.functions import id_
    from pymonet.monad import Identity

    assert Lazy(id_) == Lazy(id_)
    assert Lazy(id_) != Lazy(lambda x: x + 1)
    assert Lazy(id_) != 'foo'
    assert Lazy(id_) != Identity(4)



# Generated at 2022-06-14 03:36:58.786288
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.functor import Functor
    from pymonet.applicative import Applicative
    from pymonet.monad import Monad

    assert Functor.identity_law(Lazy.of(2), lambda x: x * 2)
    assert Functor.composition_law(Lazy.of(2), lambda x: x * 2, lambda x: x + 10)

    assert Applicative.identity_law(Lazy.of(2))
    assert Applicative.homomorphism_law(2, lambda x: x * 2)
    assert Applicative.interchange_law(Lazy.of(2), lambda x: x * 2)
    assert Applicative.composition_law(Lazy.of(lambda x: x * 2), Lazy.of(lambda x: x + 10), Lazy.of(2))

# Generated at 2022-06-14 03:37:07.984643
# Unit test for method map of class Lazy
def test_Lazy_map():
    """
    Unit test for method map of class Lazy.
    """
    lazy = Lazy.of(1).map(lambda x: x + 1)
    assert lazy.get() == 2

    lazy = Lazy.of(1).map(lambda x: x + 1).map(lambda x: x * 2)
    assert lazy.get() == 4

    assert Lazy.of(1).map(lambda x: x + 1).map(lambda x: x * 2) == Lazy.of(4)
    assert Lazy.of(None).map(lambda x: x + 1).map(lambda x: x * 2) == Lazy.of(None)



# Generated at 2022-06-14 03:37:15.478256
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    assert Lazy(lambda: 1) == Lazy(lambda: 1)
    assert Lazy(lambda: 1) != Lazy(lambda: 2)
    assert Lazy(lambda: 1) != 1
    assert Lazy(lambda: 1) != None
    assert Lazy(lambda: 1) != Lazy(lambda: 1).map(lambda _: _)
    assert Lazy(lambda: 1) != Lazy(lambda x: x).bind(lambda _: Lazy(lambda x: x))
    assert Lazy(lambda: 1) != Lazy(lambda: 1).ap(Lazy(lambda x: x))



# Generated at 2022-06-14 03:37:49.339039
# Unit test for method bind of class Lazy
def test_Lazy_bind():

    def assert_lazy_io_string(lazy_io_string, expected_value):
        actual_value = lazy_io_string.get()
        assert actual_value == expected_value
        assert actual_value.__class__.__name__ == 'IO'
        assert actual_value.get() == expected_value

    def assert_lazy_string(lazy_value, expected_value):
        actual_value = lazy_value.get()
        assert actual_value == expected_value
        assert actual_value.__class__.__name__ == 'str'

    def assert_lazy_int(lazy_value, expected_value):
        actual_value = lazy_value.get()
        assert actual_value == expected_value
        assert actual_value.__class__.__name__ == 'int'


# Generated at 2022-06-14 03:37:56.717957
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    def test_ap(test_input, expected):
        actual = test_input.get()
        assert actual == expected

    Lazy.of(1).ap(Lazy.of(lambda x: x + 1)).fold(test_ap)
    Lazy.of(1).ap(Lazy.of(lambda _x: "")).fold(test_ap)
    Lazy.of(lambda a: a + 1).ap(Lazy.of(1)).fold(test_ap)

# Generated at 2022-06-14 03:38:00.623807
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    assert Lazy.of(1) == Lazy.of(1)
    assert Lazy.of(1) != Lazy.of(2)


# Generated at 2022-06-14 03:38:07.306428
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    assert Lazy(lambda: 1).ap(Lazy.of(lambda ab: ab + 1)) == Lazy(lambda: 2)  # Lazy
    assert Lazy(lambda: 1).ap(2) == Lazy(lambda: 1)  # int
    assert Lazy(lambda: 1).ap("test") == Lazy(lambda: 1)  # str
    assert Lazy(lambda: 1).ap(dict(a=1, b=2)) == Lazy(lambda: 1)  # dict
    assert Lazy(lambda: 1).ap([1, 2, 3]) == Lazy(lambda: 1)  # list
    assert Lazy(lambda: 1).ap(("test", "test2")) == Lazy(lambda: 1)  # tuple

# Generated at 2022-06-14 03:38:12.259179
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    assert Lazy.of(lambda x: x + 1).ap(Lazy.of(1)) == Lazy(lambda x: 2)
    assert Lazy.of(lambda x: x + 1).map(lambda x: x + 2).ap(Lazy.of(1)) == Lazy(lambda x: 3)

# Generated at 2022-06-14 03:38:18.137133
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    # pylint: disable=C0103
    def fn(x):
        return Lazy.of(x)
    assert Lazy.of(4).bind(lambda x: Lazy.of(x + 1)).get() == 5
    assert Lazy.of(8).bind(fn).get() == 8

# Generated at 2022-06-14 03:38:21.982422
# Unit test for method map of class Lazy
def test_Lazy_map():
    def constructor(*args):
        return args

    lazy = Lazy(constructor)

    def mapper(value):
        return value * 2

    mapped = lazy.map(mapper)
    assert mapped.constructor_fn(2, 3) == lazy.constructor_fn(2, 3) * 2



# Generated at 2022-06-14 03:38:29.328007
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    assert (
        Lazy(lambda x: x).bind(lambda x: Lazy(lambda y: x + y)).constructor_fn(1)(2)
        ==
        3
    )

    assert (
        Lazy(lambda x: x).bind(lambda _: Lazy(lambda y: 2)).constructor_fn(1)(2)
        ==
        2
    )

    assert (
        Lazy(lambda x: x).bind(lambda _: Lazy(lambda y: 2)).constructor_fn(1)
        ==
        None
    )


# Generated at 2022-06-14 03:38:32.006814
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    def fn(x):
        return x + 2

    assert Lazy(fn).ap(Lazy(lambda: 2)).get() == 4



# Generated at 2022-06-14 03:38:35.722673
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def f(x: int) -> Lazy[int, int]:
        return Lazy.of(x*2)

    assert Lazy(lambda x: x).bind(f).get(1) == 2

# Generated at 2022-06-14 03:39:24.548533
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    result = Lazy(lambda x: x + 1).bind(
        lambda x: Lazy(lambda: x * 2))

    assert result.get(1) == 4

# Generated at 2022-06-14 03:39:32.259023
# Unit test for method bind of class Lazy
def test_Lazy_bind():  # pragma: no cover
    from pymonet.functor import Functor
    from pymonet.applicative import Applicative
    from pymonet.monad import Monad

    lazy = Lazy(lambda: 3)

    # test is Monad
    assert isinstance(lazy, Functor)
    assert isinstance(lazy, Applicative)
    assert isinstance(lazy, Monad)

    # test methods are not None
    assert lazy.map is not None
    assert lazy.ap is not None
    assert lazy.bind is not None

    # test bind
    add_one = lambda x: Lazy(lambda: x + 1)
    double = lambda x: Lazy(lambda: x * 2)

    assert lazy.bind(add_one) == Lazy(lambda: add_one(3).get())

# Generated at 2022-06-14 03:39:38.325617
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    assert Lazy.of(lambda x: x + 1).bind(lambda x: Lazy.of(x(1))).get() == 2
    assert Lazy.of(10).bind(lambda x: Lazy.of(x ** 2)).get() == 100
    assert Lazy.of(5).bind(lambda x: Lazy.of(x ** 2)).get() == 25



# Generated at 2022-06-14 03:39:49.320190
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.either import Right
    from pymonet.functor import Functor
    from pymonet.monad_try import Try

    def safe_reciprocal(a: float):
        return Try(lambda: 1 / a)

    def safe_root(a: float):
        return Try(lambda: a ** 0.5)

    def safe_root_reciprocal(a: float):
        return safe_root(a).bind(lambda x: safe_reciprocal(x))

    def safe_reciprocal_root(a: float):
        return safe_reciprocal(a).bind(lambda x: safe_root(x))

    def ap_validation(f, x):
        return Functor.of(f).ap(x)


# Generated at 2022-06-14 03:39:53.383129
# Unit test for method map of class Lazy
def test_Lazy_map():
    from pymonet.functors import test_functor

    f = lambda x: x ** 2
    g = lambda x: x + 1
    test_functor(Lazy, Lazy.of(f), f, g)


# Generated at 2022-06-14 03:40:02.059632
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():  # pragma: no cover
    def f1(a):
        print('f1', a)
        return a

    def f2(a):
        print('f2', a)
        return a

    assert Lazy(f1) != f1
    assert Lazy(f1) != Lazy(f1)
    assert Lazy(f1) != Lazy(f2)
    assert Lazy(f1) != Lazy(f1).map(lambda a: a + 'b')
    assert Lazy(f1) == Lazy(f1)



# Generated at 2022-06-14 03:40:06.489629
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    assert Lazy(lambda x: x + 10).bind(lambda x: Lazy(lambda: x + 1)).get(10) == 21

# Generated at 2022-06-14 03:40:11.286127
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.box import Box

    lazy_fn = Lazy(lambda x: x + 3)
    lazy_ap = lazy_fn.ap(lazy_fn)
    assert 6 == lazy_ap.get(3)

    box_lazy_fn = Box(lambda x: x + 3)
    lazy_ap2 = lazy_fn.ap(box_lazy_fn)
    assert 6 == lazy_ap2.get(3)



# Generated at 2022-06-14 03:40:20.342119
# Unit test for method bind of class Lazy
def test_Lazy_bind():

    from pymonet.monad_try import Try

    def sqrt(x: float) -> float:
        return x ** 2

    def try_sqrt(x: float) -> Lazy:
        return Lazy(lambda: Try.of(sqrt, x))

    assert Lazy.of(12.0).bind(try_sqrt) == Lazy.of(144.0)
    assert Lazy.of(0.0).bind(try_sqrt) == Lazy.of(0.0)

# Generated at 2022-06-14 03:40:24.590966
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    def plus_one(number):
        return number + 1

    def plus_two(number):
        return number + 2

    assert Lazy(plus_one) == Lazy(plus_one)
    assert Lazy(plus_one) != Lazy(plus_two)

