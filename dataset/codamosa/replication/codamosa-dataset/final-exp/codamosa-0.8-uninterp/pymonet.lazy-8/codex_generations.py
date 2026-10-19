

# Generated at 2022-06-14 03:31:25.699177
# Unit test for method map of class Lazy
def test_Lazy_map():
    assert Lazy(lambda x: x * 2).map(lambda y: y - 1).get(2) == 3



# Generated at 2022-06-14 03:31:31.895605
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    def f(x): return x + 2
    def g(x): return x ** 2
    def h(x): return x * x

    assert Lazy.of(4).ap(Lazy.of(f)).get() == 6
    assert Lazy.of(f).ap(Lazy.of(g)).get() == 100
    assert Lazy.of(f).ap(Lazy.of(h)).get() == 144

    assert Lazy.of(g).ap(Lazy.of(f)).get() == 6
    assert Lazy.of(g).ap(Lazy.of(g)).get() == 100
    assert Lazy.of(g).ap(Lazy.of(h)).get() == 144

# Generated at 2022-06-14 03:31:37.116228
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():  # pragma: no cover
    from pymonet.monad_try import Try

    def fn():
        pass

    assert Lazy(fn) == Lazy(fn)
    assert Lazy(fn) != Lazy(lambda: 5)
    assert Lazy(fn) != Try(fn)



# Generated at 2022-06-14 03:31:42.238427
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def add_one(x):
        def inner(a):
            return a + x
        return Lazy(inner)

    assert Lazy(lambda x: x * 2).bind(add_one(2)).bind(add_one(3)).get(4) == 14



# Generated at 2022-06-14 03:31:52.251529
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    # GIVEN
    fn1 = lambda: None
    lazy1 = Lazy.of(1)
    lazy2 = Lazy.of(2)
    lazy3 = Lazy(fn1)
    lazy4 = Lazy(fn1)
    lazy5 = lazy3.map(lambda x: x+1)
    lazy6 = lazy4.map(lambda x: x+1)
    lazy7 = Lazy(lambda a: a)

    # THEN
    assert lazy1 == lazy1
    assert not lazy1 == lazy2
    assert not lazy1 == lazy3
    assert lazy3 == lazy3
    assert lazy3 == lazy4
    assert not lazy3 == lazy5
    assert lazy5 == lazy5
    assert lazy5 == lazy6
    assert not lazy5 == lazy4
    assert lazy7(1) == 1

#

# Generated at 2022-06-14 03:32:02.023931
# Unit test for method get of class Lazy
def test_Lazy_get():
    """
    Test for method get of class Lazy.
    """
    def test_fn():
        """
        Simple function to test memoize behavior.
        """
        test_fn.count += 1

        return test_fn.count

    test_fn.count = 0

    assert Lazy(test_fn).get() == 1
    assert Lazy(test_fn).get() == 1
    assert test_fn.count == 1

    assert Lazy(test_fn).get() == 1
    assert Lazy(test_fn).get() == 1
    assert test_fn.count == 1



# Generated at 2022-06-14 03:32:05.204128
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    def fn(x):
        return lambda y: x+y

    fn_lazy = Lazy.of(fn)
    value_lazy = Lazy.of(1)

    assert fn_lazy.ap(value_lazy) == Lazy.of(2)



# Generated at 2022-06-14 03:32:17.188712
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.monoid import Sum
    from pymonet.box import Box

    def times3(a):
        return a * 3

    def times5(a):
        return a * 5

    def times7(a):
        return a * 7

    assert Lazy.of(5).ap(Lazy.of(times3)).get() == 15
    assert Lazy.of(5).ap(Lazy.of(times3)).ap(Lazy.of(times5)).get() == 75
    assert Lazy.of(5).ap(Lazy.of(times3)).ap(Lazy.of(times5)).ap(Lazy.of(times7)).get() == 525

    assert Lazy.of(Sum(10)).ap(Lazy.of(lambda m: m.fold())).get() == 10
    assert L

# Generated at 2022-06-14 03:32:23.506974
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    def f():
        return 1

    def g():
        return 2

    lazy_a1 = Lazy(f)
    lazy_a2 = Lazy(f)
    lazy_b1 = Lazy(g)

    assert lazy_a1 == lazy_a2
    assert lazy_a1 != lazy_b1


# Generated at 2022-06-14 03:32:27.364670
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    assert Lazy(lambda: 1) == Lazy(lambda: 1)
    assert Lazy(lambda: 1) != Lazy(lambda: 2)
    assert Lazy(lambda: 1) != Lazy(lambda: "one")
    assert Lazy(lambda: 1) != Lazy(lambda: None)


# Generated at 2022-06-14 03:32:34.440625
# Unit test for method map of class Lazy
def test_Lazy_map():
    assert Lazy(lambda: 1).map(lambda x: x + 1).get() == 2
    assert Lazy(lambda: 1).map(lambda x: x).get() == 1
    assert Lazy(lambda: 1).map(lambda x: None).get() is None


# Generated at 2022-06-14 03:32:42.683364
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.monad_either import Right, Left

    right = Lazy.of(1).map(lambda x: Right(x + 1))
    left = Lazy.of(1).map(lambda x: Left(x + 1))

    assert right.ap(right) == Lazy.of(3)
    assert right.ap(left) == Lazy.of(Left(2))
    assert left.ap(right) == Lazy.of(Left(2))
    assert left.ap(left) == Lazy.of(Left(2))

# Generated at 2022-06-14 03:32:50.392040
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.box import Box

    # when
    lazy_value = (
        Lazy.of(5)
        .bind(lambda x: Box(x + 5))
        .bind(lambda x: Lazy.of(x + 5))
        .bind(lambda x: Box(x + 5))
        .bind(lambda x: Lazy.of(x + 5))
    )

    # then
    assert(lazy_value.get() == 25)
    assert(not lazy_value.is_evaluated)

# Generated at 2022-06-14 03:32:51.139196
# Unit test for method get of class Lazy
def test_Lazy_get():
    def f(arg1):
        return arg1 + 1

    assert Lazy(f).get(1) == 2

# Generated at 2022-06-14 03:32:54.271082
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.maybe import Maybe

    assert Maybe.of(lambda x: x + 10).ap(Maybe.of(42)) == Maybe.of(52)



# Generated at 2022-06-14 03:32:58.358364
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    def mapper(lazy):
        return Lazy.of(lazy.get() + 1)

    assert Lazy.of(1).ap(Lazy.of(mapper)).get() == 2
    # Lazy has been evaluated
    assert Lazy.of(1).ap(Lazy.of(mapper)).get() == 2


# Generated at 2022-06-14 03:33:03.849599
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    lazy = Lazy(lambda x: x)

    assert lazy != 'value'

    assert Lazy.of(None) == Lazy.of(None)
    assert Lazy.of('value') != Lazy.of(None)

    assert lazy != Lazy(lambda x: x)

    lazy._compute_value(None)

    assert lazy == Lazy(lambda x: x)

    def generate_lazy() -> 'Lazy[T, U]':
        return lazy

    generated_lazy = generate_lazy()
    assert generated_lazy == generated_lazy

    generated_lazy._compute_value(None)
    assert generated_lazy == lazy

# Generated at 2022-06-14 03:33:12.414623
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():

    def checker_for_lazy_fn_eq(_, __):
        return True

    assert Lazy(checker_for_lazy_fn_eq) == Lazy(checker_for_lazy_fn_eq)

    def checker_for_lazy_fn(_, __):
        return False

    assert Lazy(checker_for_lazy_fn) != Lazy(checker_for_lazy_fn)
    assert Lazy(checker_for_lazy_fn) == Lazy(checker_for_lazy_fn)



# Generated at 2022-06-14 03:33:22.204224
# Unit test for method get of class Lazy
def test_Lazy_get():
    from pymonet.functor import Functor
    from pymonet.monoid import Monoid

    def f(*args) -> int:
        return sum(args)

    def mapper(arg: int) -> str:
        return '{arg}_mapped'.format(arg=str(arg))

    def folder(arg1: str, arg2: str) -> str:
        return '{arg1}_{arg2}'.format(arg1=arg1, arg2=arg2)

    l = Lazy.of(1).map(mapper).map(mapper)
    assert isinstance(l, Lazy)

    assert l.get() == '1_mapped_mapped'

    assert l.fold(folder) == '1_mapped_mapped'


# Generated at 2022-06-14 03:33:23.903003
# Unit test for method get of class Lazy
def test_Lazy_get():
    assert Lazy.of(5).get() == Lazy(lambda: 5).get() == 5



# Generated at 2022-06-14 03:33:31.046712
# Unit test for method get of class Lazy
def test_Lazy_get():  # pragma: no cover
    def fn(arg):  # pragma: no cover
        return [arg, 1]

    lazy = Lazy(fn)
    assert lazy.get(1) == [1, 1]



# Generated at 2022-06-14 03:33:40.881957
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():  # pragma: no cover
    from pymonet.box import Box
    from pymonet.either import Right, Left
    from pymonet.maybe import Maybe
    from pymonet.monad_try import Try
    from pymonet.validation import Validation

    def map_fn(x):
        return x * 2

    def ap_fn(x):
        return x * 4

    def bind_fn(x):
        return Lazy.of(x + 4)

    x = Lazy.of(2)
    y = Lazy.of(2)
    z = Lazy.of(4)

    assert x == y
    assert x != z

    x = Lazy.of(2)
    y = x.map(map_fn)

    assert x == Lazy.of(2)

# Generated at 2022-06-14 03:33:45.383696
# Unit test for method ap of class Lazy
def test_Lazy_ap():  # pragma: no cover
    class MyStruct:
        def __init__(self, value):
            self.value = value

        def __str__(self):
            return f"MyStruct({self.value})"

    fn = Lazy.of(MyStruct(1)).ap(Lazy.of(lambda x: x + 1))
    assert fn == Lazy(lambda: MyStruct(2))



# Generated at 2022-06-14 03:33:56.639961
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    # Define class to test
    class ClassToTest(object):
        def __init__(self, value):
            self.value = value

        def __eq__(self, other):
            return self.value == other.value

    def make_instance_of_ClassToTest(value):
        return Lazy(lambda x: ClassToTest(value))

    def class_to_test_constructor(value):
        return Lazy(lambda x: ClassToTest(value))

    # Make Lazy
    lazy = Lazy(class_to_test_constructor)

    # Make chained Lazy
    chained_lazy = lazy.bind(make_instance_of_ClassToTest)

    # Assert result of calling chained Lazy
    assert chained_lazy.get(2).to_box().value == ClassToTest(2)

# Generated at 2022-06-14 03:33:58.458868
# Unit test for method get of class Lazy
def test_Lazy_get():
    assert Lazy.of(123).get() == 123



# Generated at 2022-06-14 03:34:05.688386
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():  # pragma: no cover
    def constructor_fn():  # pragma: no cover
        return 5

    first_lazy = Lazy(constructor_fn)
    second_lazy = Lazy(constructor_fn)
    assert first_lazy == second_lazy

    first_lazy = Lazy(constructor_fn).get()
    second_lazy = Lazy(constructor_fn).get()
    assert first_lazy == second_lazy



# Generated at 2022-06-14 03:34:16.206509
# Unit test for method bind of class Lazy
def test_Lazy_bind():  # pragma: no cover
    from pymonet.monad_try import Try

    @Lazy
    def lazy(value) -> Try:
        return Try.of(lambda: value + 1)

    # test one level deep
    assert lazy.bind(lambda x: Try.of(lambda: x + 1)).get(2) == Try.of(lambda: 4)

    # test two levels deep
    assert lazy.bind(lambda x: Try.of(lambda: x + 1)).bind(lambda x: Try.of(lambda: x + 1)).get(2) == Try.of(lambda: 5)

    # test one level deep with errors
    assert lazy.bind(lambda x: Try.of(lambda: 1 / 0)).get(0) == Try.of(lambda: 1 / 0)


# Generated at 2022-06-14 03:34:18.563896
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    def fn_returning_10():
        return 10

    assert Lazy(fn_returning_10) == Lazy(fn_returning_10) is False
    assert Lazy.of(10) == Lazy.of(10) is True



# Generated at 2022-06-14 03:34:26.394146
# Unit test for method get of class Lazy
def test_Lazy_get():
    class A(object):
        class_value = 'class_value'

        def __init__(self, value, value_to_map) -> None:
            self.value = value
            self.value_to_map = value_to_map

        def __eq__(self, other):
            return isinstance(other, A) and self.value == other.value and self.value_to_map == other.value_to_map

    a = A('value', 'value_to_map')
    lazy = Lazy(lambda: a)

    assert lazy.get() == lazy.constructor_fn()
    assert lazy.get() == a
    assert not lazy.is_evaluated



# Generated at 2022-06-14 03:34:36.581346
# Unit test for method get of class Lazy
def test_Lazy_get():
    def fn_true():
        return True

    def fn_false():
        return False

    lazy_true = Lazy(fn_true)
    assert lazy_true.get() is True

    lazy_false = Lazy(fn_false)
    assert lazy_false.get() is False

    lazy_true_twice = Lazy(fn_true)
    assert lazy_true_twice.get() is True
    assert lazy_true_twice.get() is True

    lazy_false_twice = Lazy(fn_false)
    assert lazy_false_twice.get() is False
    assert lazy_false_twice.get() is False



# Generated at 2022-06-14 03:34:43.805213
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    def foo(arg):
        return arg + 1

    def bar(arg):
        return arg - 1

    lazy_foo = Lazy(foo)
    assert lazy_foo == lazy_foo
    assert lazy_foo != Lazy(bar)
    assert lazy_foo != Lazy(foo).map(bar)
    assert lazy_foo != Lazy(foo).ap(Lazy(lambda arg: arg - 1))

# Generated at 2022-06-14 03:34:49.215259
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    a = 5
    lazy_instance = Lazy(lambda *args: a)

    def binder(x):
        return Lazy(lambda *args: x + a)

    result = lazy_instance.bind(binder).get()
    assert result == 10, 'Lazy.bind work incorrectly'


# Generated at 2022-06-14 03:34:51.872297
# Unit test for method get of class Lazy
def test_Lazy_get():
    def foo():
        return 'foo'

    lazy = Lazy(foo)
    assert lazy.get() == 'foo'
    assert lazy.get() == 'foo'



# Generated at 2022-06-14 03:34:56.054417
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    lazy = Lazy(lambda x: x + 1) \
        .bind(lambda x: Lazy.of(x - 1)) \
        .bind(lambda x: Lazy.of(x / 2))

    assert lazy._compute_value(2) == 1


# Generated at 2022-06-14 03:35:04.114672
# Unit test for method map of class Lazy
def test_Lazy_map():
    def function_to_map(x):
        return x+1

    def function_to_lazy(x):
        return x-1

    lazy_instance = Lazy(function_to_lazy)
    mapped_lazy = lazy_instance.map(function_to_map)

    assert mapped_lazy.constructor_fn(1) == function_to_map(function_to_lazy(1))


# Generated at 2022-06-14 03:35:07.503047
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    fn = lambda n: n + 1
    lazy = Lazy(fn).bind(lambda n: Lazy(lambda: n*2))

    assert lazy.is_evaluated is False
    assert lazy.value is None
    assert lazy.constructor_fn(2) == 6

# Generated at 2022-06-14 03:35:10.960581
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def func(a):
        return Lazy(lambda: a)

    result = Lazy(lambda: "John").bind(func)
    assert result.get() == "John"

# Generated at 2022-06-14 03:35:19.671963
# Unit test for method map of class Lazy
def test_Lazy_map():
    assert Lazy.of(1).map(lambda x: x + 1).get() == 2
    assert Lazy(lambda x: x + 1).map(lambda x: x + 1).get(2) == 4
    assert Lazy(lambda x: x + 1).map(lambda x: x + 1) == Lazy(lambda x: x + 1).map(lambda x: x + 1)
    assert Lazy(lambda x: x + 1).map(lambda x: x + 1) != Lazy(lambda x: x + 2).map(lambda x: x + 2)


# Generated at 2022-06-14 03:35:22.834491
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.validation import Validation

    result = Validation.success(lambda x: x + 1).ap(Lazy(lambda: 1))
    assert result == Lazy.of(2)



# Generated at 2022-06-14 03:35:33.570309
# Unit test for method get of class Lazy
def test_Lazy_get():
    with module_and_class_name("Lazy.get") as (module, _):
        from pymonet.monad import Mapper
        from pymonet.validation import Validation

        def get():
            return 2

        def mapper(value):
            return value + 1

        lazy = Lazy(get)
        assert lazy.get(1) == 2

        add_one = Mapper.of(mapper)
        assert lazy.map(add_one).get(3) == 3

        lazy_four = Lazy.of(4)
        assert lazy_four.get(6) == 4

        assert lazy.map(add_one).ap(lazy_four).get(7) == 5


# Generated at 2022-06-14 03:35:39.630711
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    assert Lazy.of(1).bind(lambda x: Lazy.of(x + 1)).get() == 2

    assert Lazy(lambda: 1).bind(lambda x: Lazy.of(x + 1)).get() == 2

# Generated at 2022-06-14 03:35:44.125665
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def return_true_lazy():
        return Lazy(lambda: True)
    assert Lazy.of(True).bind(return_true_lazy) == Lazy.of(True)


# Generated at 2022-06-14 03:35:47.046310
# Unit test for method get of class Lazy
def test_Lazy_get():  # pragma: no cover
    def add_one(number):
        return number + 1

    lazy = Lazy(add_one)
    number = lazy.get(2)

    assert number == 3

# Generated at 2022-06-14 03:35:49.266982
# Unit test for method get of class Lazy
def test_Lazy_get():
    assert Lazy.of(123).get() == 123



# Generated at 2022-06-14 03:35:54.017869
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    # given
    lazy1 = Lazy(lambda x: x)
    lazy2 = Lazy(lambda x: x)

    # when
    result = lazy1 == lazy2

    # then
    assert result is True



# Generated at 2022-06-14 03:35:59.242826
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    lazy = Lazy(lambda x: x).ap(Lazy.of(5))
    assert lazy.get() == 5

    lazy = Lazy(lambda x: x ** 2).ap(Lazy(lambda x: x ** 3))
    assert lazy.get() == 125

# Generated at 2022-06-14 03:36:02.834978
# Unit test for method map of class Lazy
def test_Lazy_map():
    def plus1(x):
        return x + 1

    def plus2(x):
        return x + 2

    assert Lazy.of(1).map(plus1) == Lazy.of(2)
    assert Lazy.of(1).map(plus1).map(plus2) == Lazy.of(3)


# Generated at 2022-06-14 03:36:06.798614
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def fn(value):
        return Lazy(lambda x: value + x)

    derived = Lazy(lambda x: x + 1).bind(fn)
    derived_result = derived.get(5)

    assert derived_result == 6


# Generated at 2022-06-14 03:36:12.502059
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    """
    Unit test for method ap of class Lazy
    """
    from decimal import Decimal

    def sum(x: Decimal, y: Decimal) -> Decimal:
        return x + y

    assert Lazy(lambda a: sum(a, Decimal(1))).ap(Lazy(lambda b: Decimal(b))) == Lazy.of(
        Decimal(1)
    )



# Generated at 2022-06-14 03:36:24.024472
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    assert Lazy(lambda: 1) == Lazy(lambda: 1), 'Two Lazy are equals where both are evaluated both have the same value and constructor functions.'
    assert Lazy(lambda: 1) != Lazy(lambda: 2), 'Two Lazy are not equals where both are evaluated both not have the same value'
    assert Lazy(lambda: 1) != Lazy(lambda: 1).map(lambda x: x + 1), 'Two Lazy are not equals where both are evaluated both have the same value but different constructor functions'
    assert Lazy(lambda: 1) != Lazy(lambda: 1).bind(lambda x: Lazy(lambda: x)), 'Two Lazy are not equals where both are evaluated both have the same value but different constructor functions'

# Generated at 2022-06-14 03:36:34.305662
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def concat_two_strings(left_string: str, right_string: str) -> str:
        return left_string + right_string

    assert Lazy(lambda: "Hello ").bind(
        lambda left_string: Lazy(lambda: "World!").map(
            lambda right_string: concat_two_strings(left_string, right_string)
        )
    ).get() == "Hello World!"



# Generated at 2022-06-14 03:36:36.553625
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    assert Lazy.of(42).bind(lambda x: Lazy.of(x + 1)).get(12) == 43



# Generated at 2022-06-14 03:36:41.328847
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def test_fn(d: int) -> Lazy[int, int]:
        return Lazy.of(d * 2)

    assert Lazy.of(1).bind(test_fn) == Lazy(test_fn)

    empty_lazy = Lazy.of(1).bind(None)
    assert empty_lazy.is_evaluated
    assert empty_lazy.value is None

# Generated at 2022-06-14 03:36:44.848434
# Unit test for method map of class Lazy
def test_Lazy_map():
    def square(x): return x**2

    lazy = Lazy.of(3).map(lambda x: x + 1).map(square)

    assert lazy.get() == 16


# Generated at 2022-06-14 03:36:49.996248
# Unit test for method bind of class Lazy
def test_Lazy_bind():  # pragma: no cover
    print('Test Lazy bind')
    data = Lazy(lambda x: {'name': x})

    assert data.bind(lambda x: Lazy(lambda: str(x))).get(0) == "{'name': 0}"



# Generated at 2022-06-14 03:36:56.307330
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def add(a):
        return Lazy.of(a + 2)

    def mult(a):
        return Lazy.of(a * 4)

    lazy_multiply = Lazy.of(2).bind(add)
    assert lazy_multiply.get() == 4
    assert lazy_multiply.get() == 4

    lazy_multiply2 = Lazy.of(2).bind(add).bind(mult)
    assert lazy_multiply2.get() == 16


# Generated at 2022-06-14 03:37:03.755343
# Unit test for method map of class Lazy
def test_Lazy_map():
    from pymonet.monad_either import Right

    test_obj = Lazy.of(1)
    another_test_obj = test_obj.map(lambda x: x + 1)
    assert another_test_obj.get() == 2

    assert test_obj is not another_test_obj

    def lambda_fn(x):
        assert x == 1
        return Right(x + 1)
    assert test_obj.map(lambda_fn).get() == 2



# Generated at 2022-06-14 03:37:08.134597
# Unit test for method bind of class Lazy
def test_Lazy_bind():  # pragma: no cover
    def test_function(x: int) -> int:
        return x + 1

    lazy = Lazy.of(2).bind(lambda x: Lazy.of(test_function(x)))
    assert lazy.get() == test_function(2)



# Generated at 2022-06-14 03:37:17.319472
# Unit test for method map of class Lazy
def test_Lazy_map():
    """
    Function for testing method map of class Lazy
    """
    from pymonet.box import Box
    from pymonet.either import Right
    from pymonet.maybe import Maybe
    from pymonet.monad_try import Try
    from pymonet.validation import Validation


    def add_one(value):
        return value + 1

    def add_three(value):
        return value + 3

    def divide_by_zero(value):
        return 1/0

    def throw_err(value):
        raise ZeroDivisionError("Err")

    void_fn = lambda: None

# Generated at 2022-06-14 03:37:23.447335
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    """
    Evaluate function and memoize her output or return memoized value when function was evaluated.
    """
    def some_function(arg: int) -> int:
        return arg * 2

    some_lazy = Lazy(lambda: some_function(5)).bind(lambda result: Lazy(lambda: some_function(result) * 2))

    assert some_lazy.get() == 50



# Generated at 2022-06-14 03:37:28.208968
# Unit test for method map of class Lazy
def test_Lazy_map():
    def _constructor(value):
        return value

    assert Lazy(lambda: 42).map(_constructor) == Lazy(_constructor)
    assert Lazy(lambda: 42).map(lambda x: x + 1) == Lazy(lambda: 43)


# Generated at 2022-06-14 03:37:30.684480
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.box import Box

    assert Lazy.of(1).ap(Box(lambda x: x + 1)) == 2



# Generated at 2022-06-14 03:37:33.494792
# Unit test for method bind of class Lazy
def test_Lazy_bind():  # pragma: no cover
    def fn(value):
        return Lazy(lambda *args: value + 1)

    lazy = Lazy(lambda *args: 1)
    lazy = lazy.bind(fn)

    assert lazy.get() == 2

# Generated at 2022-06-14 03:37:36.786288
# Unit test for method map of class Lazy
def test_Lazy_map():
    """ Unit test for method map of class Lazy """
    assert Lazy(lambda name: name).map(lambda name: 'Hello {name}!'.format(name=name)).get('John') == 'Hello John!'



# Generated at 2022-06-14 03:37:43.931953
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def fn(x):
        if x > 5:
            return Lazy.of(x + 1)
        return Lazy.of(-1)

    assert Lazy(lambda x: x).bind(fn) == Lazy(lambda x: x).map(fn)
    assert Lazy(lambda x: x).bind(fn).get(1) == -1
    assert Lazy(lambda x: x).bind(fn).get(10) == 11


# Generated at 2022-06-14 03:37:50.761896
# Unit test for method bind of class Lazy
def test_Lazy_bind():  # pragma: no cover
    def test_fn():
        return Lazy.of(3)

    def mapper_fn(value):
        return value * 3

    lazy = Lazy(test_fn).bind(test_fn)
    assert lazy.get() == 9

    lazy = Lazy(test_fn).map(mapper_fn)
    assert lazy.get() == 9

    lazy = Lazy(test_fn).map(mapper_fn).bind(test_fn)
    assert lazy.get() == 27

    lazy = Lazy(test_fn).bind(test_fn).map(mapper_fn)
    assert lazy.get() == 27

# Generated at 2022-06-14 03:38:03.518651
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    assert Lazy(lambda: 1).bind(lambda x: Lazy(lambda: x + 1)).get() == 2
    assert Lazy(lambda: []).bind(lambda xs: Lazy(lambda: xs + [1])).get() == [1]
    assert Lazy(lambda: '').bind(lambda xs: Lazy(lambda: xs + '1')).get() == '1'
    assert Lazy(lambda: {}).bind(lambda xs: Lazy(lambda: {'a': xs}) if xs else Lazy(lambda: {'b': xs})).get() == {'b': {}}
    assert Lazy(lambda: {}).bind(lambda xs: Lazy(lambda: {'a': xs}) if xs else Lazy(lambda: {})).get() == {'a': {}}



# Generated at 2022-06-14 03:38:15.428237
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.monad_try import Try
    from pymonet.monad_try import Error

    def function_to_call(argument):
        return argument ** 2

    def function_to_call_with_error(argument):
        raise RuntimeError('Runtime error')

    def compose(val):
        return Try(lambda arg1: function_to_call(arg1 + val), val)

    assert Lazy(lambda val: val ** 2)\
        .bind(compose)\
        .bind(compose).get(2) == Try(function_to_call, 2)\
                                   .bind(compose)\
                                   .bind(compose).get()

    assert Lazy(lambda val: val ** 2)\
        .bind(compose)\
        .bind(compose).get(2) == 16

    assert Lazy

# Generated at 2022-06-14 03:38:18.985062
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    def f_of(value):
        return lambda x: value

    assert Lazy.of(1).ap(Lazy.of(f_of(2))) == Lazy.of(2)



# Generated at 2022-06-14 03:38:27.408511
# Unit test for method map of class Lazy
def test_Lazy_map():
    class A(object):
        def __init__(self, value):
            self.value = value

        def __eq__(self, other):
            return str(self.value) == str(other.value)

    assert Lazy(lambda: A(1)).map(lambda x: x.value + 1).get() == 2

    assert Lazy(lambda: 'abc').map(lambda x: x + 'd').get() == 'abcd'


# Generated at 2022-06-14 03:38:39.960154
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.functor import Functor

    from pymonet.box import Box
    from pymonet.validation import Validation

    def add_a_to_lazy(lazy: Lazy[int, int]):
        return lazy.map(lambda x: x + 1)

    add_one_to_lazy = Lazy(functools.partial(add_one_to_int))

    two_lazy = add_one_to_lazy.bind(add_a_to_lazy)

    assert two_lazy.get() == 2

    assert two_lazy.to_box().get() == 2
    assert two_lazy.to_validation().get_or_else([]) == 2

# Generated at 2022-06-14 03:38:46.795735
# Unit test for method map of class Lazy
def test_Lazy_map():
    def mapping_function(val):
        return val * val

    assert Lazy(lambda: 1).map(mapping_function) == Lazy(lambda: mapping_function(1))
    assert Lazy(lambda: 2).map(mapping_function) == Lazy(lambda: mapping_function(2))
    assert Lazy(lambda: 3).map(mapping_function) == Lazy(lambda: mapping_function(3))



# Generated at 2022-06-14 03:38:58.431372
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    assert Lazy.of("test") != None
    assert Lazy.of("test") != "test"
    assert Lazy.of("test") != Lazy.of("test2")

    assert Lazy.of("test2") == Lazy.of("test2")

    def fn():
        return "test"
    lazy1, lazy2 = Lazy(fn), Lazy(fn)
    assert lazy1 == lazy2

    def fn_with_argv(arg):
        return "test"
    lazy1, lazy2 = Lazy(fn_with_argv), Lazy(fn_with_argv)
    assert lazy1 == lazy2
    assert not Lazy(fn) == Lazy(fn_with_argv)

    lazy1._compute_value()
    lazy2._compute_value()
    assert lazy

# Generated at 2022-06-14 03:39:05.086922
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    def test(returned_value: int) -> Lazy[int, str]:
        def f(x: int) -> str:
            return str(x)
        return Lazy(lambda *args: f(returned_value))

    lazy_1 = Lazy.of(lambda x: x + 1)
    assert(lazy_1.ap(test(1)).get() == 2)
    assert(lazy_1.ap(Lazy.of(lambda x: x + 1)).get() == 2)


# Generated at 2022-06-14 03:39:08.533784
# Unit test for method map of class Lazy
def test_Lazy_map():  # pragma: no cover
    assert Lazy.of(10).map(lambda a: a * 2) == Lazy(lambda: 20)



# Generated at 2022-06-14 03:39:15.751375
# Unit test for method map of class Lazy
def test_Lazy_map():
    """
    Tests for Lazy.map method.
    """
    lazy_fn = lambda x: x + 5
    lazy_instance = Lazy(lazy_fn)

    mapped_fn = lambda x: x * 2
    mapped_lazy_instance = Lazy(mapped_fn)

    assert lazy_instance.map(mapped_fn) == mapped_lazy_instance


# Generated at 2022-06-14 03:39:20.758984
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    def fn_to_apply(x: int):
        return x * 2

    mapped_fn = Lazy.of(fn_to_apply).ap(Lazy.of(5))
    assert mapped_fn.get() == 10



# Generated at 2022-06-14 03:39:32.319209
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.monad_try import Try
    from pymonet.maybe import Maybe

    def divide(x, y):
        try:
            return Lazy.of(x/y)
        except ZeroDivisionError:
            return Try.raise_error(ValueError)

    assert Lazy.of(5).ap(Lazy.of(lambda x: x*6)) == Lazy.of(30)
    assert Lazy.of(5).ap(Lazy.of(lambda x: x*6)).to_maybe() == Maybe.just(30)
    assert not Lazy.of(5).ap(Lazy.of(lambda x: x*6)).to_maybe().is_empty
    assert Lazy.of(5).ap(Lazy.of(lambda x: x*6)).to_maybe().is_just
   

# Generated at 2022-06-14 03:39:42.116024
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.maybe import Maybe

    t = Lazy(lambda: 42)
    fn = lambda val: Lazy(lambda: val + 1)

    assert t.bind(fn) == Lazy(lambda: 43)

    def fn2(val):
        return Lazy(lambda: val + 1)

    assert Lazy.of(1).bind(fn2) == Lazy(lambda: 2)

    def fn_with_maybe(_):
        return Maybe.just(42)

    assert Lazy.of(1).map(lambda x: x + 1).bind(fn_with_maybe) == Maybe.just(43)

# Generated at 2022-06-14 03:39:47.542275
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    def double(x):
        return x * 2

    lazy = Lazy.of(double)
    fn = Lazy.of(3).ap(lazy)
    assert fn.get() == 6

    lazy = Lazy.of(lambda x: x * 2)
    fn = Lazy.of(3).ap(lazy)
    assert fn.get() == 6

    lazy = Lazy.of(lambda x, y: x * y)
    fn = lazy.ap(Lazy.of(3)).ap(Lazy.of(5)).get()
    assert fn == 15

# Generated at 2022-06-14 03:39:52.972998
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def add_one(arg):
        return Lazy(lambda _: arg + 1)

    lazy = Lazy(lambda: 1)
    assert lazy.bind(add_one).get() == 2

# Generated at 2022-06-14 03:39:55.180936
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    assert Lazy(lambda: 1).ap(Lazy(lambda x: x + 1)) == Lazy(lambda: 2)



# Generated at 2022-06-14 03:39:57.029334
# Unit test for method map of class Lazy
def test_Lazy_map():
    assert Lazy.of(1).map(lambda x: x + 2).get() == 3


# Generated at 2022-06-14 03:40:01.682806
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    def f(value):
        return value + 1

    from pymonet.box import Box

    lazy = Lazy.of(1)
    lazy_fn = Lazy.of(f)

    assert lazy.ap(lazy_fn).get() == Box(f).ap(Box.of(1)).get()


# Generated at 2022-06-14 03:40:07.307745
# Unit test for method map of class Lazy
def test_Lazy_map():  # type: ignore
    """
    Unit test for method map of class Lazy
    """
    assert Lazy(lambda x: x + 1).map(lambda x: x * 3).get(2) == 9



# Generated at 2022-06-14 03:40:18.643542
# Unit test for method ap of class Lazy
def test_Lazy_ap():  # pragma: no cover
    from pymonet.monad_try import Try
    from pymonet.box import Box
    from pymonet.lazy import Lazy

    assert Lazy.of(lambda x: x + 1).ap(Lazy.of(2)) == Lazy.of(3)
    assert Lazy.of(lambda x: x + 1).ap(Box(2)) == Lazy.of(3)
    assert Lazy.of(lambda x: x + 1).ap(Try(2)) == Lazy.of(3)
    assert Lazy.of(lambda x: x + 1).ap(Try(ValueError('Something went wrong'))) == Lazy.of(ValueError('Something went wrong'))


# Generated at 2022-06-14 03:40:29.408354
# Unit test for method bind of class Lazy

# Generated at 2022-06-14 03:40:39.679785
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    assert (
        Lazy(lambda value: value * 2)
        == Lazy(lambda value: value * 2)
    )
    assert (
        Lazy(lambda value: value * 2)
        != Lazy(lambda value: value * 4)
    )
    assert (
        Lazy(lambda value: value * 2)
        != Lazy(lambda value: value * 2).map(lambda value: value * 2)
    )
    assert (
        Lazy(lambda value: value * 2).map(lambda value: value * 2)
        == Lazy(lambda value: value * 2).map(lambda value: value * 2)
    )
    assert (
        Lazy(lambda value: value * 2).map(lambda value: value * 2)
        != Lazy(lambda value: value * 2)
    )

# Generated at 2022-06-14 03:40:48.245900
# Unit test for method map of class Lazy
def test_Lazy_map():
    def add_three(value):
        return value + 3

    def twice_add_three(value):
        return value * 2 + 3

    lazy = Lazy.of(2).map(add_three)

    assert lazy._compute_value() == add_three(2)

    lazy = Lazy.of(2).map(add_three).map(twice_add_three)

    assert lazy._compute_value() == twice_add_three(add_three(2))

    lazy = Lazy.of(2)
    lazy._compute_value()

    lazy_twice = lazy.map(twice_add_three)

    assert lazy_twice._compute_value() == twice_add_three(lazy.value)



# Generated at 2022-06-14 03:40:54.337460
# Unit test for method map of class Lazy
def test_Lazy_map():
    value = "VALUE"
    lazy = Lazy.of(value)

    assert lazy.is_evaluated is False
    new_lazy = lazy.map(lambda x: x + x)

    assert lazy.get() == value
    assert lazy.is_evaluated is True
    assert new_lazy.get() == value + value
    assert new_lazy.is_evaluated is True



# Generated at 2022-06-14 03:40:59.669188
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    assert Lazy.of(lambda x: x + 1).ap(Lazy.of(2)) == Lazy.of(3)
    assert Lazy.of(lambda x: x + 1).ap(Lazy.of(None)) == Lazy.of(lambda x: x + 1)

# Generated at 2022-06-14 03:41:04.554056
# Unit test for method map of class Lazy
def test_Lazy_map():
    """
    Test map function on Lazy monad
    """
    def increment(number: int) -> int:
        return number + 1

    lazy_number = Lazy.of(1).map(increment)

    assert lazy_number.get() == 2



# Generated at 2022-06-14 03:41:07.647214
# Unit test for method ap of class Lazy
def test_Lazy_ap():  # pragma: no cover
    def pair(x, y):
        return [x, y]

    assert Lazy.of(2).ap(Lazy.of(pair).ap(Lazy.of(10))).get() == [10, 2]

# Generated at 2022-06-14 03:41:17.979471
# Unit test for method map of class Lazy
def test_Lazy_map():
    def square(value):
        return value ** 2

    def mult(a, b):
        return a * b

    assert Lazy.of(2).map(square) == Lazy.of(4)
    assert Lazy.of(2).map(square).map(square) == Lazy.of(16)
    assert Lazy.of(2).map(square).map(square).constructor_fn(5) == 256
    assert Lazy.of(2).map(square).map(square).constructor_fn(3) == 256
    assert Lazy.of(2).map(square).map(mult).constructor_fn(3, 5) == 126



# Generated at 2022-06-14 03:41:29.523003
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.box import Box
    from pymonet.monad_try import Try
    from pymonet.validation import Validation

    assert (
        Lazy.of('value').bind(
            lambda x: Box.of(x),
        )
        == Box.of('value')
    )

    assert (
        Lazy.of(1+1)
        .bind(
            lambda x: Try.of(lambda: x ** 2)
        )
        == Try.of(lambda: 4)
    )

    assert (
        Lazy.of(None).bind(
            lambda x: Validation.fail(x),
        )
        == Validation.fail(None)
    )