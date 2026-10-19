

# Generated at 2022-06-14 03:31:29.579976
# Unit test for method get of class Lazy
def test_Lazy_get():
    def triple(x):
        return x*3

    def five():
        return 5

    assert Lazy(triple).get(2) == 6
    assert Lazy(five).get() == 5

    lazy = Lazy(triple).map(str)
    assert lazy.get(2) == "6"

    lazy_mapper = Lazy(triple).map(lambda x: x*2)
    assert lazy_mapper.get(2) == 12



# Generated at 2022-06-14 03:31:32.179832
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    assert Lazy.of(42).map(lambda x: x * 2) == Lazy.of(42).map(lambda x: x * 2)
    assert Lazy.of(42).map(lambda x: x * 2) != Lazy.of(43)



# Generated at 2022-06-14 03:31:38.834687
# Unit test for method map of class Lazy
def test_Lazy_map():  # pragma: no cover
    from .box import Box

    box = Box(2)
    lazy = Lazy.of(3).map(lambda x: x + 1)
    lazy2 = Lazy.of(4).map(box.map).map(lambda x: x + 1)

    assert lazy.get() == 4
    assert lazy2.get() == 7


# Generated at 2022-06-14 03:31:47.616729
# Unit test for method bind of class Lazy
def test_Lazy_bind():  # pragma: no cover
    assert Lazy.of(0).bind(lambda x: Lazy.of(x + 1)).get() == 1
    assert Lazy.of(0).bind(lambda x: Lazy.of(x + 1)).bind(lambda x: Lazy.of(x + 2)).get() == 3
    assert Lazy.of(0).bind(lambda x: Lazy.of(x + 1)).bind(lambda x: Lazy.of(x + 2)).bind(lambda x: Lazy.of(x + 4)).get(
    ) == 7



# Generated at 2022-06-14 03:31:57.174288
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    # GIVEN
    lazy1 = Lazy.of(2)
    lazy2 = Lazy.of(3)
    lazy3 = Lazy.of(3)

    # WHEN
    lazy1_eq_lazy1 = lazy1 == lazy1
    lazy1_eq_lazy2 = lazy1 == lazy2
    lazy2_eq_lazy3 = lazy2 == lazy3

    # THEN
    assert lazy1_eq_lazy1 is True
    assert lazy1_eq_lazy2 is False
    assert lazy2_eq_lazy3 is True



# Generated at 2022-06-14 03:32:08.508046
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    class DataLoader:
        def load_data(self, count):
            if count > 0:
                return Lazy.of(1)
            else:
                return Lazy.of(0)

    def do_something_with_data(data):
        return Lazy.of(data + 1)

    def do_something_with_error(error):
        return Lazy.of('error')

    counter = DataLoader()
    assert (
        Lazy.of(10)
        .map(lambda a: counter.load_data(a))  # returns Lazy(lambda: 1)
        .bind(do_something_with_data)  # lambda: 2
        .get() == 2
    )


# Generated at 2022-06-14 03:32:12.860478
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    assert Lazy(lambda x: x).map(lambda x: x + 5) == Lazy(lambda x: x).map(lambda x: x + 5)
    assert Lazy(lambda x: x).map(lambda x: x + 5) != Lazy(lambda x: x)
    assert Lazy(lambda x: x).map(lambda x: x + 5) != Lazy(lambda x: x + 5)


# Generated at 2022-06-14 03:32:19.470058
# Unit test for method bind of class Lazy
def test_Lazy_bind():  # pragma: no cover
    from random import choice
    from pymonet.box import Box
    from pymonet.maybe import Maybe

    def fn(value):
        if value % 2 == 0:
            return Box(value + 10)
        return Maybe.empty()

    def test_Lazy_bind(value):
        subject = Lazy.of(value)
        result = subject.bind(fn)
        return result.get()

    assert test_Lazy_bind(1) == 1
    assert test_Lazy_bind(2) == 12

# Generated at 2022-06-14 03:32:24.330899
# Unit test for method map of class Lazy
def test_Lazy_map():
    def test_function(*args):
        return 'test'
    def mapper(value):
        return value + '_mapper'
    assert (Lazy(test_function).map(mapper).get() == 'test_mapper')


# Generated at 2022-06-14 03:32:31.995351
# Unit test for method map of class Lazy
def test_Lazy_map():
    def add1(x: int) -> int:
        return x + 1

    class TestClass:
        @staticmethod
        def add1(x: int) -> int:
            return x + 1

    other = Lazy.of(2)

    assert Lazy.of(1).map(add1).map(str).get() == '2'
    assert Lazy.of(1).map(lambda x: x + 1).map(str).get() == '2'
    assert Lazy.of(1).map(TestClass.add1).map(str).get() == '2'
    assert Lazy.of(1).map(lambda x: x + other.get()).map(str).get() == '3'



# Generated at 2022-06-14 03:32:45.893463
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    assert Lazy.of(1) == Lazy.of(1) == Lazy.of(1).map(lambda x: x)
    assert Lazy.of(1) != Lazy.of(2)
    assert Lazy.of(1).map(lambda x: -x) != Lazy.of(1)
    assert Lazy.of(1).to_box() != Lazy.of(1)
    assert Lazy.of(1).to_box() == Lazy.of(1).to_box()
    assert Lazy.of(1).to_box() != Lazy.of(1).to_try()
    assert Lazy.of(1).to_try() == Lazy.of(1).to_try().map_err(lambda x: x)
    assert not Lazy.of(1).to_try

# Generated at 2022-06-14 03:32:50.821924
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    def constructor_fn(x):
        return x

    lazy1 = Lazy(constructor_fn)
    lazy2 = Lazy(constructor_fn)

    assert lazy1 == lazy2

    lazy2.get(3)

    assert lazy1 != lazy2


# Generated at 2022-06-14 03:33:00.754742
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    def return_a():
        return "a"

    # Test equality of Lazy with constructor_fn returning `a`
    assert Lazy(return_a) == Lazy(return_a)

    def return_b():
        return "b"

    def return_a_and_after_b():
        return "a"

    # Test unequality of Lazy with constructor_fn returning `a`
    # and Lazy with constructor_fn returning `b`
    assert Lazy(return_a) != Lazy(return_b)

    # Test unequality of Lazy before evaluation with constructor_fn
    # returning `a` and Lazy after evaluation with constructor_fn returning `a`

# Generated at 2022-06-14 03:33:12.491424
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    l1 = Lazy.of(1)
    l2 = Lazy.of(1)
    assert l1 == l2

    l3 = Lazy(lambda: True)
    l4 = Lazy(lambda: True)
    assert l3 == l4

    l5 = Lazy.of(1).map(lambda value: value + 1)
    l6 = Lazy.of(1).map(lambda value: value + 1)
    assert l5 == l6

    l7 = Lazy.of(1)
    l8 = Lazy.of(2)
    assert not l7 == l8

    l9 = Lazy.of(1)
    l10 = Lazy.of(2).map(lambda value: value - 1)
    assert not l9 == l10


# Generated at 2022-06-14 03:33:22.525888
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    def binary_fn(*args) -> int:
        return args[0] + args[1]

    assert Lazy(lambda: 2).ap(Lazy(lambda: 3)).get() == 5
    assert Lazy(binary_fn).ap(Lazy(lambda: 2)).ap(Lazy(lambda: 3)).get() == 5

    assert Lazy(lambda v: lambda x: v + x).ap(Lazy(2)).ap(Lazy(3)).get() == 5
    assert Lazy(binary_fn).ap(Lazy(2)).ap(Lazy(3)).get() == 5

    def compose(v, x) -> int:
        return v + x

    def compose2(v, x) -> int:
        return v + x


# Generated at 2022-06-14 03:33:29.050082
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():  # pragma: no cover
    def dl(fn):
        return fn

    def fn1(v):
        return 1

    def fn2(v):
        return 2

    def fn3(v):
        return 3

    def fn4(v):
        return 4

    a = Lazy(fn1)
    b = Lazy(fn4).bind(dl).map(fn1).map(fn4).map(fn3).map(fn2)
    c = Lazy(fn2).bind(dl).map(fn1).map(fn4).map(fn3).map(fn2)
    d = Lazy(fn4).bind(dl).map(fn1).map(fn4).map(fn3).map(fn1)
    assert a == a
    assert b == b
    assert c == c

# Generated at 2022-06-14 03:33:36.092516
# Unit test for method get of class Lazy
def test_Lazy_get():
    def square(a):
        return a * a

    assert Lazy(square).get(2) == 4

    def add(a, b):
        return a + b

    assert Lazy(add).get(2, 2) == 4

    assert Lazy.of(4).get() == 4
    assert Lazy.of(4).get(2) == 4
    assert Lazy.of(4).get(2, 2) == 4



# Generated at 2022-06-14 03:33:38.387558
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    assert Lazy.of(12) == Lazy.of(12)
    assert Lazy.of(12) != Lazy.of(42)



# Generated at 2022-06-14 03:33:41.652741
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    assert Lazy(lambda: 5) == Lazy(lambda: 5)

    assert Lazy(lambda: 5) != Lazy(lambda: 10)
    assert Lazy(lambda: 5) != 5



# Generated at 2022-06-14 03:33:47.424587
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.maybe import Maybe

    l: Lazy[None, Maybe[int]] = Lazy(lambda: Maybe.just(1))
    l1: Lazy[None, Maybe[int]] = Lazy(lambda: Maybe.empty())
    l2: Lazy[None, Maybe[int]] = Lazy(lambda: Maybe.just(2))

    def fn(m: Maybe[int]):
        return Lazy(lambda: m.map(lambda v: v + 2))

    assert l.bind(fn).get() == Maybe.just(3)
    assert l1.bind(fn).get() == Maybe.empty()
    assert l2.bind(fn).get() == Maybe.just(4)


# Generated at 2022-06-14 03:34:02.330879
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.either import Right, Left

    def fn(n: int) -> Lazy[int, Either[str, int]]:
        if n == 0:
            return Lazy.of(Right(n))
        elif n % 2 == 0:
            return Lazy.of(Right(n + 1))

        return Lazy.of(Left('{} is not even number'.format(n)))

    assert Right(1).fold(lambda: None, lambda v: v) == Lazy.of(1).bind(fn).fold(lambda: None, lambda v: v)
    assert Right(3).fold(lambda: None, lambda v: v) == Lazy.of(2).bind(fn).fold(lambda: None, lambda v: v)
    assert Right(5).fold(lambda: None, lambda v: v) == L

# Generated at 2022-06-14 03:34:14.758559
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    assert Lazy.of(10) == Lazy.of(10)
    assert Lazy.of('A') == Lazy.of('A')
    assert Lazy.of(False) == Lazy.of(False)
    assert Lazy.of([]) == Lazy.of([])

    assert Lazy.of(10) != Lazy.of(20)
    assert Lazy.of('A') != Lazy.of('B')
    assert Lazy.of(False) != Lazy.of(True)
    assert Lazy.of(1) != Lazy.of(True)
    assert Lazy.of([1]) != Lazy.of([])

    closure_value = 10
    closure = Lazy(lambda: closure_value)

    assert closure == Lazy(lambda: closure_value)
    assert closure != Lazy

# Generated at 2022-06-14 03:34:26.003966
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.monad_try import Try
    from pymonet.monad_list import List
    from pymonet.monad_option import Option
    from pymonet.monad_validation import Validation

    lazy_box = Lazy.of(Box(1))
    lazy_either = Lazy.of(Either.right(1))
    lazy_maybe = Lazy.of(Maybe.just(1))
    lazy_list = Lazy.of(List.of(1))
    lazy_try = Lazy.of(Try.of(lambda: 1))
    lazy_validation = Lazy.of(Validation.success(1))

    assert Lazy.of(2).ap(lazy_box).get() == Box(2)
    assert Lazy.of(2).ap(lazy_either).get

# Generated at 2022-06-14 03:34:27.351156
# Unit test for method map of class Lazy
def test_Lazy_map():
    assert Lazy.of(1).map(lambda a: a + 1).get() == 2

# Generated at 2022-06-14 03:34:34.317282
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    def test_suite():
        from pymonet.monad_maybe import Maybe
        from pymonet.monad_try import Try
        from pymonet.monad_validation import Validation

        def f(x): return x + 1
        def g(x): return x + 2

        # Test Lazy object with non-empty Maybe
        a = Lazy.of(2)
        b = Lazy.of(lambda x: x + 10)
        c = a.ap(b)
        assert c == Lazy(lambda *_: 12)
        assert c == Lazy(lambda *_: 12)

        # Test Lazy object with empty Maybe
        a = Lazy.of(None)
        b = Lazy.of(lambda x: x + 10)
        c = a.ap(b)

# Generated at 2022-06-14 03:34:44.047019
# Unit test for method bind of class Lazy
def test_Lazy_bind():  # pragma: no cover
    # type: () -> None
    def double(val):
        return val * 2

    # Lazy(fn=lambda: 5)
    double_lazy = Lazy(lambda: 5).bind(lambda val: Lazy.of(double(val)))
    assert double_lazy.get() == 10

    # Lazy(fn=lambda: lambda: 5)
    double_lazy = Lazy(lambda: lambda: 5).bind(lambda fn: fn()).bind(lambda val: Lazy.of(double(val)))
    assert double_lazy.get() == 10

    # Lazy(fn=lambda: lambda: lambda: 5)

# Generated at 2022-06-14 03:34:48.858929
# Unit test for method get of class Lazy
def test_Lazy_get():
    from pymonet.maybe import Maybe

    def my_fn():
        return Maybe(5).map(lambda x: x + 1).get()

    lazy_fn = Lazy.of(my_fn)
    assert lazy_fn.get() == 6


# Generated at 2022-06-14 03:34:54.078594
# Unit test for method ap of class Lazy
def test_Lazy_ap(): # pragma: no cover
    from pymonet.function import Function

    def validate_age(age):
        if age < 18:
            return 'To young'
        else:
            return 'Welcome'

    validate_fn = Function.of(validate_age)

    age = Lazy.of(17)
    result = age.ap(validate_fn)
    assert result.get() == 'To young'

    age = Lazy.of(20)
    result = age.ap(validate_fn)
    assert result.get() == 'Welcome'

    age = Lazy.of('17')
    result = age.ap(validate_fn)
    assert result.get() == 'To young'

    age = Lazy.of('20')
    result = age.ap(validate_fn)

# Generated at 2022-06-14 03:35:06.476182
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():  # pragma: no cover
    assert Lazy(lambda x: x) == Lazy(lambda x: x)
    assert Lazy(lambda x: x).map(lambda x: x + 1) == Lazy(lambda x: x).map(lambda x: x + 1)
    assert Lazy(lambda x: x) != Lazy.of(1)
    assert Lazy(lambda x: x) != Lazy(lambda x: x + 1)
    assert Lazy(lambda x: x) != Lazy(lambda x: x).map(lambda x: x + 1)
    assert Lazy(lambda x: x).map(lambda x: x + 1) != Lazy(lambda x: x).map(lambda x: x + 2)

# Generated at 2022-06-14 03:35:18.237158
# Unit test for method map of class Lazy
def test_Lazy_map():
    def f(x):
        return x + 1

    def g(x):
        return x + 2

    # Lazy with value 1
    la = Lazy.of(1)
    # Lazy with value 1 mapped by f
    lb = la.map(f)
    # Lazy with value 1 mapped by f and g
    lc = lb.map(g)

    assert lc.get() == 4

    la_new = Lazy.of(1)
    # Lazy with value 1 mapped by f
    lb_new = la_new.map(f)
    # Lazy with value 1 mapped by f and g
    lc_new = lb_new.map(g)

    # all created Lazy are equal because they have the same values and constructor functions
    assert la == la_new
    assert lb == lb_new

# Generated at 2022-06-14 03:35:24.811622
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    assert (
        Lazy(lambda x: x * 2)
        .bind(lambda x: Lazy(lambda y: x * y))
        .bind(lambda x: Lazy.of(x / 2))
        .get(10, 20) == 200
    )

# Generated at 2022-06-14 03:35:29.019599
# Unit test for method get of class Lazy
def test_Lazy_get():  # pragma: no cover
    def test_fn(*args):
        return args

    args = (1, 2)

    lazy = Lazy(test_fn)

    assert lazy.get(*args) == args
    assert lazy.is_evaluated is True



# Generated at 2022-06-14 03:35:37.858760
# Unit test for method map of class Lazy
def test_Lazy_map():
    from pymonet.validation import Validation
    from pymonet.either import Right
    from pymonet.maybe import Maybe
    from pymonet.box import Box
    from pymonet.monad_try import Try

    success_fn = lambda x: x * 2
    failure_fn = lambda x: 2 / x

    assert Lazy.of(10).map(success_fn).get() == 20
    assert Lazy.of(3).map(failure_fn).get() == 2 / 3
    assert Lazy.of(10).map(lambda x: Maybe.just(x)).get() == Maybe.just(10)
    assert Lazy.of(10).map(lambda x: Right(x)).get() == Right(10)

# Generated at 2022-06-14 03:35:47.059888
# Unit test for method bind of class Lazy
def test_Lazy_bind():  # pragma: no cover
    def add(a, b):
        return a + b

    def multiply(a, b):
        return a * b

    def sum_and_multiply(a, b, c):
        return add(multiply(a, b), c)

    def add_and_multiply(a, b, c):
        return add(a, multiply(b, c))

    assert Lazy(sum_and_multiply).bind(add_and_multiply).get(2, 3, 4) == 14
    assert Lazy(sum_and_multiply).bind(add_and_multiply).bind(add_and_multiply).get(1, 2, 3) == 21

# Generated at 2022-06-14 03:35:52.640334
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():  # pragma: no cover
    def add(a, b):
        return a + b

    lazy_a = Lazy(add)
    lazy_b = Lazy(add)
    assert lazy_a == lazy_b

    assert lazy_a.to_validation(1, 2) == lazy_b.to_validation(1, 2)

    lazy_b = Lazy(lambda: 1)
    assert lazy_a != lazy_b

    assert lazy_a.to_validation(1, 2) != lazy_b.to_validation(1, 2)

    lazy_a = Lazy(lambda: 1)
    assert lazy_a == lazy_b

    assert lazy_a.to_validation(1, 2) == lazy_b.to_validation(1, 2)



# Generated at 2022-06-14 03:35:57.796455
# Unit test for method map of class Lazy
def test_Lazy_map():
    def test_cases():
        num = Lazy(lambda: 9)
        fn = lambda x: x * 2
        mapped_num = num.map(fn)
        assert mapped_num.get() == fn(num.get())

    test_cases()


# Generated at 2022-06-14 03:36:06.919042
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    import pytest

    @pytest.fixture
    def x():
        return Lazy(lambda: "this is value")

    def test_return_true_if_both_lazy_evaluated_have_same_value_and_function(x):
        assert Lazy(lambda: "this is value") == x

    def test_return_false_if_lazy_not_evaluated_have_same_value_and_function(x):
        assert Lazy(lambda: "this is value") != x

    def test_return_false_if_one_lazy_evaluated_and_second_is_not_evaluated(x):
        assert Lazy(lambda: "this is value").get() == Lazy(lambda: "this is value")

# Generated at 2022-06-14 03:36:17.152806
# Unit test for method map of class Lazy
def test_Lazy_map():
    from pymonet.box import Box
    from pymonet.identity import Identity
    from pymonet.maybe import Maybe
    from pymonet.monad_try import Try
    from pymonet.validation import Validation

    def fn(x):
        return x + 2

    assert Lazy(lambda: fn).map(fn).get() == 4
    assert Lazy(lambda: 1).map(fn).get() == 3
    assert Lazy.of(1).map(fn).get() == 3

    monads = [Box(1), Identity(1), Maybe.just(1), Try(fn), Validation.success(1)]

    for monad in monads:
        assert Lazy(lambda: monad).map(fn).get().get() == 3



# Generated at 2022-06-14 03:36:25.727911
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    """
    Unit test for method __eq__ of class Lazy
    """
    from pymonet.functor import Functor
    from pymonet.monad import Monad, Applicative

    def assert_equals(expected: bool, actual: bool, message: str) -> None:
        if expected != actual:
            _message = 'Expected: {}, Actual: {}. {}'.format(expected, actual, message)
            raise AssertionError(_message)

    assert_equals(True, Functor.laws_identity(Lazy.of('value')), 'Test identity law')
    assert_equals(True, Functor.laws_composition(Lazy.of('value')), 'Test composition law')

# Generated at 2022-06-14 03:36:27.989110
# Unit test for method map of class Lazy
def test_Lazy_map():
    assert Lazy.of('a').map(lambda x: x + 'b') == Lazy(lambda *args: 'ab')
    assert Lazy(lambda x: x + 'a').map(lambda x: x + 'b').get('a') == 'ab'



# Generated at 2022-06-14 03:36:35.030251
# Unit test for method map of class Lazy
def test_Lazy_map():
    assert Lazy.of(4).map(lambda x: x + 1).get() == 5


# Generated at 2022-06-14 03:36:38.802923
# Unit test for method map of class Lazy
def test_Lazy_map():  # pragma: no cover
    @Lazy
    def lazy_fn(x):
        return x

    def mapper(x):
        return x + 1

    assert lazy_fn.map(mapper).constructor_fn(1) == 2



# Generated at 2022-06-14 03:36:46.342300
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():  # pragma: no cover
    def f(x):
        return x

    test = Lazy(f)
    for other in [1, 'str', [], {}, f]:
        assert not (test == other)

    for other in [Lazy(f), Lazy(lambda x: x + 1), Lazy(lambda x: x + 1), Lazy(f), Lazy(lambda x: x + 1)]:
        assert test != other

    assert test == test

# Generated at 2022-06-14 03:36:49.489756
# Unit test for method map of class Lazy
def test_Lazy_map():
    f = lambda x: x + 1
    g = lambda y: y * y
    assert Lazy(f).map(g).constructor_fn(1) == 4



# Generated at 2022-06-14 03:36:54.036994
# Unit test for method get of class Lazy
def test_Lazy_get():
    class TestClass:
        def __init__(self, value):
            self.value = value

    fn = lambda value: TestClass(value)

    lazy = Lazy(fn)
    assert lazy.get(1).value == 1
    assert lazy.get(2).value == 2


# Generated at 2022-06-14 03:36:56.269466
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    def multiply(value):
        return Lazy.of(lambda x: x * 4)

    assert Lazy.of(2).ap(multiply(12)).get() == 48

# Generated at 2022-06-14 03:37:02.987455
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    assert Lazy(lambda: 10).bind(lambda x: Lazy(lambda: x * 2)) == Lazy(lambda: 20)
    assert Lazy(lambda: 10).bind(lambda x: Lazy.of(x * 2)) == Lazy(lambda: 20)
    assert Lazy(lambda: 10 + 10).bind(Lazy.of(lambda x: x * 2)) == Lazy(lambda: 40)

# Generated at 2022-06-14 03:37:13.478013
# Unit test for method bind of class Lazy
def test_Lazy_bind():  # pragma: no cover
    lazy = Lazy(lambda x: x)
    new_lazy = Lazy(lambda x: x)
    lazy_with_two = lazy.bind(lambda x: new_lazy.map(lambda y: x + y))

    # Both folders must be not evaluated
    assert not lazy.is_evaluated
    assert not new_lazy.is_evaluated
    # Both folders must be not evaluated
    assert not lazy_with_two.is_evaluated

    assert lazy_with_two.get(1, 2) == 3
    # Lazy in lazy_with_two must be evaluated
    assert lazy.is_evaluated and new_lazy.is_evaluated
    # lazy_with_two must be evaluated
    assert lazy_with_two.is_evaluated

# Generated at 2022-06-14 03:37:15.670736
# Unit test for method get of class Lazy
def test_Lazy_get():
    lazy = Lazy(lambda x: x * 2)

    assert lazy.get(5) == 10



# Generated at 2022-06-14 03:37:19.586280
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.box import Box

    def stub_fun(arg):
        return Box(arg)

    assert Lazy.of('str').bind(stub_fun).get() == Box('str')

# Generated at 2022-06-14 03:37:27.040986
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    lazy = Lazy(lambda x: x)
    assert lazy.ap(Lazy.of(1)) == Lazy.of(1)
    assert lazy.ap(Lazy(lambda x: x)) == lazy

# Generated at 2022-06-14 03:37:28.103261
# Unit test for method get of class Lazy
def test_Lazy_get():
    assert Lazy.of(2).get() == 2



# Generated at 2022-06-14 03:37:30.888989
# Unit test for method get of class Lazy
def test_Lazy_get():
    lazy_comparable = Lazy.of(complex(0, 0))
    assert lazy_comparable.get() == complex(0, 0)



# Generated at 2022-06-14 03:37:39.476925
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.maybe import Maybe, just
    from pymonet.either import Right
    from pymonet.box import Box

    assert Lazy(lambda: Maybe.just(4)).ap(Maybe.just(lambda x: x+1)).get() == Maybe.just(5)
    assert Lazy(lambda: Maybe.just(4)).ap(Maybe.nothing()).get() == Maybe.nothing()

    assert Lazy(lambda: Right.success(4)).ap(Right.success(lambda x: x+1)).get() == Right.success(5)
    assert Lazy(lambda: Right.success(4)).ap(Right.failure('test')).get() == Right.failure('test')

    assert Lazy(lambda: Box(4)).ap(Box(lambda x: x+1)).get() == Box(5)

# Unit

# Generated at 2022-06-14 03:37:49.302583
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    from unittest import TestCase

    class __test_Lazy___eq__(TestCase):
        def test_should_return_true_for_two_lazy_with_same_is_evaluated_constructor_and_value(self):
            # given
            def fn():
                return 'test'
            lazy = Lazy(fn)
            lazy.is_evaluated = True
            lazy.value = fn()
            lazy2 = Lazy(fn)
            lazy2.is_evaluated = True
            lazy2.value = fn()

            # when
            result = lazy == lazy2

            # then
            self.assertTrue(result)


# Generated at 2022-06-14 03:37:54.665240
# Unit test for method map of class Lazy
def test_Lazy_map():
    assert Lazy(lambda: 'test') == Lazy(lambda: 'test')
    assert Lazy(lambda: 'test').map(lambda a: a) == Lazy(lambda: 'test')
    assert Lazy(lambda: 'test').map(lambda a: a).map(lambda a: a) == Lazy(lambda: 'test')
    assert Lazy(lambda: 'test').get() == 'test'

    assert Lazy(lambda: 'test').map(lambda a: a + ' b').get() == 'test b'
    assert Lazy(lambda: 'test').map(lambda a: a + ' b').bind(lambda b: Lazy(lambda: b + ' c')).get() == 'test b c'

# Generated at 2022-06-14 03:38:00.673661
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    from pymonet.maybe import Maybe

    assert Lazy(lambda a: a) == Lazy(lambda a: a)
    assert  Lazy(lambda a: a) != Lazy(lambda a: 1)
    assert Lazy(lambda a: a) != Maybe.nothing()


# Generated at 2022-06-14 03:38:07.145153
# Unit test for method bind of class Lazy
def test_Lazy_bind():  # pragma: no cover
    from pymonet.box import Box
    from pymonet.monad_try import Try

    def add(x):
        return Lazy.of(x + 1)

    lazy = Lazy.of(1).bind(add)
    assert lazy.get() == 2

    lazy = Lazy.of(1).bind(lambda x: Box.of(x + 1))
    assert lazy.get() == 2

    lazy = Lazy.of(1).bind(lambda x: Try.of(lambda: x + 1))
    assert lazy.get() == 2

    lazy = Lazy.of(1).bind(lambda x: Try.of(lambda: x/0))
    assert isinstance(lazy.get(), Exception)



# Generated at 2022-06-14 03:38:12.514401
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def plus1(a):
        return a+1

    def times2(a):
        return a*2

    assert Lazy.of(1).bind(lambda x: Lazy.of(plus1(x))).bind(lambda x: Lazy.of(times2(x))).get() == 4

test_Lazy_bind()

# Generated at 2022-06-14 03:38:16.242277
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    assert Lazy(lambda x: x + x).ap(Lazy.of(1)) == Lazy(lambda x: 1 + x).get()



# Generated at 2022-06-14 03:38:25.714782
# Unit test for method map of class Lazy
def test_Lazy_map():
    def f(x):
        return x + 10

    test_value = Lazy(lambda: 20)
    test_value = test_value.map(f)
    assert str(test_value) == 'Lazy[fn=<function test_Lazy_map.<locals>.f at 0x00000074D8ECF1E0>, value=None, ' \
                              'is_evaluated=False]'
    assert test_value.get() == 30



# Generated at 2022-06-14 03:38:29.691292
# Unit test for method get of class Lazy
def test_Lazy_get():
    def add(x, y):
        return x + y

    lazy_add = Lazy(lambda: add(3, 8))

    assert lazy_add.get() == 11



# Generated at 2022-06-14 03:38:36.302236
# Unit test for method get of class Lazy
def test_Lazy_get():
    first_value = 10
    second_value = 20
    def my_function(arg):
        return arg

    lazy = Lazy(my_function)
    assert lazy.get(10) == my_function(10)
    assert lazy.get(first_value) == my_function(first_value)
    assert lazy.get(first_value) == lazy.get(second_value)



# Generated at 2022-06-14 03:38:40.162526
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    def foo():
        return 0

    def bar():
        return 1

    assert Lazy(foo) == Lazy(foo)
    assert Lazy(foo) != Lazy(bar)
    assert Lazy(foo) != foo
    assert Lazy(foo) != 0


# Generated at 2022-06-14 03:38:42.709268
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():  # pragma: no cover
    assert Lazy.of(1) == Lazy.of(1)



# Generated at 2022-06-14 03:38:45.923476
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.monad_maybe import Maybe

    assert Lazy.of(lambda x: x).ap(
        Maybe.just(3)
    ) == Maybe.just(3)



# Generated at 2022-06-14 03:38:49.098166
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    def constructor_fn(*args):
        return args

    assert Lazy(constructor_fn) == Lazy(constructor_fn)

    lazy_obj = Lazy(constructor_fn)
    lazy_obj.get(1, 2, 3, 4, 5)
    assert lazy_obj == lazy_obj

    assert lazy_obj != Lazy(constructor_fn)



# Generated at 2022-06-14 03:39:00.005154
# Unit test for method map of class Lazy
def test_Lazy_map():  # pragma: no cover
    from pymonet.maybe import Maybe

    lazy = Lazy.of(1)
    incremented = lazy.map(lambda x: x + 2)

    assert callable(incremented.constructor_fn)
    assert not incremented.is_evaluated
    assert incremented.value is None
    assert incremented.constructor_fn() == 3
    assert incremented.is_evaluated
    assert incremented.value == 3
    assert lazy.get() == 1

    lazy = Lazy.of(1)
    incremented = lazy.map(lambda x: x)
    assert incremented == lazy
    assert incremented.constructor_fn() == 1
    assert incremented.is_evaluated
    assert incremented.value == 1


# Generated at 2022-06-14 03:39:04.251304
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def f(x: int) -> Lazy[int, int]:
        return Lazy(lambda: x + 1)

    lazy = Lazy(lambda: 1)
    result = lazy.bind(f)
    assert isinstance(result, Lazy[int, int])
    assert result.get() == 2

# Generated at 2022-06-14 03:39:13.825455
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    from pymonet.monad_try import Try
    from pymonet.validation import Validation

    def not_implemented(*args):
        raise NotImplementedError()

    # test for same type
    assert Lazy(not_implemented) == Lazy(not_implemented)

    # test for different type
    assert Lazy(not_implemented) != Try(not_implemented)
    assert Lazy(not_implemented) != Validation(not_implemented)

    # test for different constructor_fn
    assert Lazy(not_implemented) != Lazy(lambda: 0)
    assert Lazy(not_implemented) != Lazy(lambda: '0')
    assert Lazy(not_implemented) != Lazy(lambda: [])

# Generated at 2022-06-14 03:39:27.035581
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    def double(x):
        return Lazy.of(lambda arg: arg * 2)

    def add(x):
        return Lazy.of(lambda arg: arg + 2)

    result = Lazy.of(1).ap(double(1)).ap(add(1))
    expected = Lazy.of(6)
    assert result == expected

    result = Lazy.of(1).ap(double(1)).ap(Lazy.of(add(1)))
    expected = Lazy.of(6)
    assert result == expected

# Generated at 2022-06-14 03:39:27.813537
# Unit test for method map of class Lazy
def test_Lazy_map():
    assert Lazy


# Generated at 2022-06-14 03:39:30.673743
# Unit test for method map of class Lazy
def test_Lazy_map():
    function = lambda x: x
    assert Lazy.of(0).map(function) == Lazy(function)
    assert Lazy.of(0).map(function).get() == 0


# Generated at 2022-06-14 03:39:36.139493
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    """
    >>> test = Lazy.of(2)
    >>> test == Lazy.of(2)
    True
    >>> test == Lazy.of(3)
    False
    >>> test.get()
    2
    >>> test == Lazy.of(2)
    True
    >>> test == Lazy.of(3)
    False
    """



# Generated at 2022-06-14 03:39:46.321606
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    from pymonet.monad_try import Try

    class A:
        a = 1

    class B:
        a = 1

    assert Lazy.of(1) == Lazy.of(1)
    assert not Lazy.of(1) == Lazy.of(2)
    assert not Lazy.of(1) == 1
    assert not Lazy.of(Try.of(lambda: 1)) == Lazy.of(Try.of(lambda: 1))
    assert not Lazy.of(A()) == Lazy.of(A())
    assert not Lazy.of(A()) == Lazy.of(B())


test_Lazy___eq__()

# Generated at 2022-06-14 03:39:51.469310
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def function(arg: int) -> int:
        return arg + 1

    def second_function(arg: int) -> int:
        return arg + 10

    lazy = Lazy(function)
    second_lazy = lazy.bind(lambda x: Lazy(second_function))

    assert second_lazy.get() == 12

# Generated at 2022-06-14 03:39:59.008558
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    """
    Test correctness of method bind of class Lazy.
    """
    from pymonet.tests import _make_sum_tuple_fn, _make_str_fn1, _make_str_fn2

    x1 = Lazy.of(12).bind(_make_sum_tuple_fn)
    assert x1.get(1, 2) == (1, 2, 3)

    x2 = Lazy.of(24).bind(_make_sum_tuple_fn).map(_make_str_fn1).map(_make_str_fn2)
    assert x2.get(3, 4) == '21:23'



# Generated at 2022-06-14 03:40:01.384105
# Unit test for method map of class Lazy
def test_Lazy_map():
    """
    Test map method of Lazy class.
    """
    assert Lazy.of('foo').map(lambda x: 'bar' + x) == Lazy.of('barfoo')


# Generated at 2022-06-14 03:40:02.836618
# Unit test for method map of class Lazy
def test_Lazy_map():
    from pymonet.functor import test_map

    test_map(Lazy, *(1,))

# Generated at 2022-06-14 03:40:08.789894
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    lazy_success = Lazy(lambda: 1)
    lazy_failure = Lazy(lambda: Lazy.of(1)
                        .map(lambda arg: arg + 1)
                        .get())

    def bind_success(arg):  # pragma: no cover
        return lazy_success

    def bind_failure(arg):  # pragma: no cover
        return lazy_failure

    assert lazy_success.bind(bind_success).get() == 1
    assert lazy_failure.bind(bind_failure).get() == 2


# Generated at 2022-06-14 03:40:16.576567
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():  # pragma: no cover
    def fn(x):
        return x + 1

    assert Lazy(fn).__eq__(Lazy(fn))

# Generated at 2022-06-14 03:40:28.845594
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    """
    Unit test for method __eq__ of class Lazy
    """
    @patch('pymonet.lazy.Lazy.__init__', return_value=None)
    def test(constructor_fn, *args):
        # pylint: disable=unused-argument
        lazy = Lazy(lambda x: x)
        lazy.is_evaluated = False
        lazy.value = None
        lazy.constructor_fn = constructor_fn

        assert lazy.__eq__(lazy) == True
        lazy.is_evaluated = True
        assert lazy.__eq__(lazy) == True
        lazy.value = 4
        assert lazy.__eq__(lazy) == True
        lazy.constructor_fn = lambda x: x * 2
        assert lazy.__eq__(lazy) == True



# Generated at 2022-06-14 03:40:36.039350
# Unit test for method map of class Lazy
def test_Lazy_map():
    with mock.patch('random.getrandbits', return_value=1):
        multiplier = Lazy(lambda _: random.getrandbits(32))
        foo = multiplier.map(lambda x: x * 2).get(None)
        assert foo == 2

        foo = multiplier.map(lambda x: x * 4).get(None)
        assert foo == 4

        foo = multiplier.map(lambda x: x * 6).get(None)
        assert foo == 6

        foo = multiplier.map(lambda x: x * 8).get(None)
        assert foo == 8


# Generated at 2022-06-14 03:40:38.577406
# Unit test for method map of class Lazy
def test_Lazy_map():
    def f(x):
        return x + 1

    assert Lazy(f).map(f).get(3) == 5


# Generated at 2022-06-14 03:40:44.181455
# Unit test for method map of class Lazy
def test_Lazy_map():
    assert_that(Lazy(lambda: "abc").map(lambda x: x.upper()), equal_to(Lazy(lambda: "ABC")))
    assert_that(Lazy(lambda: "abc").map(lambda x: x + "1234").get(), equal_to("abc1234"))


# Generated at 2022-06-14 03:40:53.744332
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    def foo():
        pass

    def bar():
        pass

    lazy_foo = Lazy.of(foo)
    lazy_foo_copy = Lazy.of(foo)

    assert lazy_foo == lazy_foo_copy

    lazy_foo_evaluated = Lazy.of(foo).get()
    lazy_foo_evaluated_copy = Lazy.of(foo).get()

    assert lazy_foo_evaluated == lazy_foo_evaluated_copy

    lazy_bar = Lazy.of(bar)

    assert lazy_foo != lazy_bar

    assert lazy_foo != foo



# Generated at 2022-06-14 03:40:57.063072
# Unit test for method map of class Lazy
def test_Lazy_map():  # type: () -> None
    def inc(a):
        return a + 1

    def dec(a):
        return a - 1

    assert Lazy(inc).map(dec) == Lazy(lambda: dec(inc(None)))



# Generated at 2022-06-14 03:41:07.822418
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    @Lazy
    def get_1():
        return 1

    @Lazy
    def get_2():
        return 2

    assert get_1 == get_1
    assert get_1 != get_2
    assert get_2 != get_1
    assert get_2 == get_2

    @Lazy
    def lazy_1():
        return 1

    @Lazy
    def lazy_2():
        return 2

    assert Lazy.of(1) == Lazy.of(1)
    assert Lazy.of(1) != Lazy.of(2)
    assert Lazy.of(2) != Lazy.of(1)
    assert Lazy.of(2) == Lazy.of(2)

    assert lazy_1 == get_1
    assert lazy_1 != get_2
    assert lazy

# Generated at 2022-06-14 03:41:18.886813
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    from .monad_test_utils import function_with_no_arguments, function_with_one_argument, \
        function_with_two_arguments, function_with_three_arguments

    assert Lazy(function_with_no_arguments) == Lazy(function_with_no_arguments)
    assert Lazy(function_with_one_argument) == Lazy(function_with_one_argument)
    assert Lazy(function_with_two_arguments) == Lazy(function_with_two_arguments)
    assert Lazy(function_with_three_arguments) == Lazy(function_with_three_arguments)
    assert Lazy(function_with_no_arguments) != Lazy(function_with_one_argument)
    assert Lazy(function_with_no_arguments)

# Generated at 2022-06-14 03:41:23.142285
# Unit test for method get of class Lazy
def test_Lazy_get():  # pragma: no cover
    # Given
    def add_1(number: int) -> int:
        return number + 1

    assert Lazy(add_1).get(41) == 42
# End