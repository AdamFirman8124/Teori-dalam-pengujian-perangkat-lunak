

# Generated at 2022-06-14 03:31:32.028554
# Unit test for method bind of class Lazy
def test_Lazy_bind():  # pragma: no cover
    from pymonet.maybe import Maybe

    def fn(value):
        def lazy_fn():
            return Maybe.just(value)
        return Lazy(lazy_fn)

    lazy = Lazy.of(2)

    result = lazy.bind(lambda value: fn(value + 2))

    assert result.get() == 4

# Generated at 2022-06-14 03:31:38.680448
# Unit test for method get of class Lazy
def test_Lazy_get():
    def f():
        return 1

    def g():
        return '1'

    lazy_f = Lazy.of(f)

    assert lazy_f.get() == 1
    assert lazy_f.get() == 1

    lazy_g = Lazy.of(g)

    assert lazy_g.get() == '1'
    assert lazy_g.get() == '1'

# Generated at 2022-06-14 03:31:43.347718
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    # Test not equal objects
    assert Lazy.of(1) == Lazy.of(1)
    assert not Lazy.of(2) == Lazy.of(1)
    assert not Lazy.of(1) == Lazy.of(2)
    assert not Lazy.of(1).map(lambda el: el * 2) == Lazy.of(2)
    assert not Lazy.of(1).map(lambda el: el * 2) == Lazy.of(2).map(lambda el: el * 2)

    def f1(el):
        return el + 1

    def f2(el):
        return el + 2

    assert Lazy.of(1).map(f1).bind(Lazy.of) == Lazy.of(1).map(f1).bind(Lazy.of)
   

# Generated at 2022-06-14 03:31:52.834722
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    """
    Test method __eq__ of class Lazy
    """
    assert Lazy(lambda a: a).__eq__(Lazy(lambda a: a)) == True, '__eq__ of Lazy should return True in compare with same Lazy instance'
    assert Lazy(lambda a: a).__eq__(Lazy(lambda b: b)) == False, '__eq__ of Lazy should return False in compare with different Lazy instance'
    assert Lazy(lambda a: a).__eq__(None) == False, '__eq__ of Lazy should return False in compare with None'
    assert Lazy(lambda a: a).__eq__(True) == False, '__eq__ of Lazy should return False in compare with bool'

# Generated at 2022-06-14 03:31:59.287571
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    from pymonet.functor import identity

    mapper = lambda x: x + 1
    lazy_a = Lazy.of(0).map(mapper)
    lazy_b = Lazy.of(0).map(mapper)
    lazy_c = Lazy(lambda x: x + 1)
    assert lazy_a == lazy_b
    assert lazy_a != lazy_c
    assert lazy_a == lazy_a



# Generated at 2022-06-14 03:32:06.065390
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def constructor(a):
        return a * 2

    def mapper(a):
        def inner(b):
            return b * 2 + a
        return inner

    lazy = Lazy(constructor)
    lazy2 = lazy.map(mapper)
    lazy3 = lazy2.bind(lambda a: Lazy(lambda b: a(b) + '!!!'))

    ret = lazy3.get(7)

    assert ret == '28!!!'



# Generated at 2022-06-14 03:32:10.595965
# Unit test for method map of class Lazy
def test_Lazy_map():  # pragma: no cover
    """
    test Lazy map method
    """
    def add_one(x):
        return x + 1

    assert Lazy(lambda: 1).map(add_one).get() == 2


# Generated at 2022-06-14 03:32:19.910551
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    """
    Test for bind method of Lazy
    """

    def lazy_fn(*args):
        assert args[0] == 5
        assert args[1] == 10
        return 20

    def outer_addition(x):  # pylint: disable=unused-variable
        return Lazy(lambda y: x + y)

    # Lazy[function(x) -> x + y]
    lazy = Lazy(lazy_fn)

    # Lazy[function(y) -> x + y]
    lazy = lazy.bind(outer_addition)

    # Function returning x + y
    function = lazy.constructor_fn

    returned_value = function(5, 10)

    assert returned_value == 25
    assert lazy.is_evaluated is True
    assert lazy.value == 20

# Generated at 2022-06-14 03:32:27.345663
# Unit test for method get of class Lazy
def test_Lazy_get():  # pragma: no cover
    assert Lazy.of(5).get() == 5
    assert Lazy.of(5).map(lambda x: x + 1).get() == 6
    assert Lazy.of(5).map(lambda x: x + 1).get() == 6
    assert Lazy.of(5).map(lambda x: x + 1).map(lambda x: x * 4).get() == 24



# Generated at 2022-06-14 03:32:32.371184
# Unit test for method map of class Lazy
def test_Lazy_map():
    assert Lazy(lambda *_: 5).map(lambda x: x + 1).get() == 6
    assert Lazy(lambda *_: 5).map(lambda x: x + 1).get() == Lazy(lambda *_: 5).map(lambda x: x + 1).get()



# Generated at 2022-06-14 03:32:45.362056
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.box import Box

    x = Lazy.of(2).map(lambda n: n + 1)
    y = Lazy.of(lambda n: n - 1)
    result = x.ap(y).get()
    assert result == Box(1)

    x = Lazy.of(lambda n: n + 1).ap(Lazy.of(3))
    result = x.get()
    assert result == Box(4)

    x = Lazy.of(lambda n: n + 1).ap(Lazy.of(lambda n: n - 1))
    result = x.get()
    assert result == Box(0)



# Generated at 2022-06-14 03:32:50.992603
# Unit test for method map of class Lazy
def test_Lazy_map():
    def f(x):
        return x + 1

    def g(x):
        return x * 2

    def h(x):
        return x * 5

    assert Lazy.of(1).map(f).map(g).map(h) == Lazy(lambda: f(g(h(1))))


# Generated at 2022-06-14 03:33:00.887549
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.validation import Validation

    def func(x, y):
        return x + y

    def func2(x, y, z):
        return x + y + z

    # Create pair of lazy objects
    lazy_validation_ap = Lazy.of(func)
    lazy_validation_with_args = Lazy.of((1, 2))

    assert lazy_validation_ap.ap(lazy_validation_with_args).get() == 3
    assert lazy_validation_with_args.ap(lazy_validation_ap).get() == 3
    assert lazy_validation_ap.ap(Lazy.of((1, 2))).get() == 3

    lazy_validation_ap = Lazy(func2)

# Generated at 2022-06-14 03:33:04.956952
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def fn(x):
        def get_result():
            return x + x

        return Lazy(get_result)

    assert Lazy(lambda: 1).bind(fn).get() == 2

# Generated at 2022-06-14 03:33:09.094128
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    def f():
        pass

    def g():
        pass

    lazy = Lazy(f)

    assert lazy == lazy
    assert lazy != Lazy(g)
    assert lazy != g
    assert lazy != None
    assert lazy != Lazy(f).get()
    assert lazy == Lazy.of(None)

# Generated at 2022-06-14 03:33:15.966505
# Unit test for method map of class Lazy
def test_Lazy_map():
    assert Lazy.of(1).map(lambda x: x + 1) == Lazy.of(2)
    assert Lazy.of(1).map(lambda x: x + 1).map(lambda x: x + 5) == Lazy.of(8)
    assert Lazy.of(1).map(lambda x: x + 1).map(lambda x: x + 5).map(lambda x: x * 10) == Lazy.of(80)



# Generated at 2022-06-14 03:33:20.364486
# Unit test for method bind of class Lazy
def test_Lazy_bind():  # pragma: no cover
    def f(x):
        return Lazy(lambda: x + 1)

    def g(x):
        return Lazy(lambda: x * 3)

    assert Lazy(lambda: 1).bind(f).bind(g) == Lazy(lambda: (1 + 1) * 3)



# Generated at 2022-06-14 03:33:27.212667
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    """
    Lazy comparison test.

    Two Lazy are equals where both are evaluated both have the same value and constructor functions.
    """
    from pymonet.insertion_sort import insertion_sort

    def insertion_sort_1(arg):
        return insertion_sort(arg, lambda x, y: x < y)

    def insertion_sort_2(arg):
        return insertion_sort(arg, lambda x, y: x < y)

    lazy_1 = Lazy(insertion_sort_1)
    lazy_1_with_mapped_value = lazy_1.map(lambda x: x[0])

    assert lazy_1_with_mapped_value == Lazy(insertion_sort_1).map(lambda x: x[0])
    assert lazy_1.map(lambda x: x[0]) is not L

# Generated at 2022-06-14 03:33:38.793581
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    assert Lazy(lambda: 1).bind(lambda v: Lazy(lambda: v + 1)).get() == 2
    assert Lazy(lambda: 1).bind(lambda v: Lazy(lambda: v + 1)).to_box().fold(lambda: 0, lambda v: v) == 2
    assert Lazy(lambda: 1).bind(lambda v: Lazy(lambda: v + 1)).to_maybe().get_or_else(lambda: 0) == 2
    assert Lazy(lambda: 1).bind(lambda v: Lazy(lambda: v + 1)).to_try().get() == 2
    assert Lazy(lambda: 1).bind(lambda v: Lazy(lambda: v + 1)).to_validation().fold(lambda: 0, lambda v: v) == 2

# Generated at 2022-06-14 03:33:42.549376
# Unit test for method bind of class Lazy
def test_Lazy_bind():  # pragma: no cover
    def some_number() -> int:
        return 10

    lazy_number = Lazy(some_number)
    assert lazy_number.bind(lambda n: Lazy.of(n)).get() == 10

# Generated at 2022-06-14 03:33:54.777515
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def constructor_fn():
        return 1

    def mapper(value):
         return value + 1

    def bad_mapper(value):
        raise Exception('Simple exception')

    def error_mapper(value):
        from pymonet.error import Error
        return Error('Error', value)

    lazy_value = Lazy(constructor_fn)

    assert lazy_value.bind(lambda value: Lazy(lambda: mapper(value))).get() == 2
    assert lazy_value.bind(lambda value: Lazy(lambda: mapper(value))).get() == 2

    try:
        lazy_value.bind(lambda value: Lazy(lambda: bad_mapper(value))).get()
    except Exception as e:
        assert str(e) == 'Simple exception'
        assert isinstance(e, Exception)



# Generated at 2022-06-14 03:34:04.763919
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    """
    Unit test for method bind of class Lazy
    """
    from pymonet.functor import Functor

    from pymonet.cont import Cont

    from pymonet.reader import Reader

    from pymonet.state import State

    test_list = [
        ([Functor.of, lambda _: Lazy.of('X')], 'X'),
        ([Cont.of, lambda _: Lazy.of('X')], 'X'),
        ([Reader.of, lambda _: Lazy.of('X')], 'X'),
        ([State.of, lambda _: Lazy.of('X')], 'X'),
    ]

    for data, expected in test_list:
        assert data[0](data[1]).bind(data[1]).constructor_fn() == expected

# Generated at 2022-06-14 03:34:08.478388
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    """
    >>> Lazy(lambda x: x+1).bind(lambda x: Lazy(lambda y: x+y)).get(2, 3)
    6
    """



# Generated at 2022-06-14 03:34:19.943516
# Unit test for method bind of class Lazy
def test_Lazy_bind():  # pragma: no cover
    from pymonet.maybe import Maybe

    def add_five(value: int) -> Lazy[int, int]:
        return Lazy(lambda *args: value + args[0])

    value: Lazy[int, int] = Lazy.of(1).bind(lambda x: Lazy.of(x + 5))
    assert value.get(5) == 11

    def get_name(person: dict) -> Lazy[dict, Maybe[str]]:
        return Lazy(lambda *args: person.get(args[0], Maybe.nothing()))


    person = {"name": "Joe", "age": 17}
    name: Lazy[dict, Maybe[str]] = get_name(person)
    assert name.get("name").get_or_else("No name") == "Joe"

# Generated at 2022-06-14 03:34:26.741724
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.monad_try import Try

    def succ(x):
        return Lazy.of(x)

    def err(x):
        return Lazy.of(Try.failure(ZeroDivisionError('Division by zero')))

    assert Lazy.of(0).bind(succ).get() == 0
    assert Lazy.of(0).bind(err).get().is_failure() == True



# Generated at 2022-06-14 03:34:33.963692
# Unit test for method map of class Lazy
def test_Lazy_map():
    assert Lazy.of(1).map(lambda x: x + 1) == Lazy(lambda: 2)
    assert Lazy.of(1).map(lambda x: x + 1).map(float) == Lazy(lambda: 2.0)
    assert Lazy.of(1).map(lambda x: x + 1).map(float).map(lambda x: x * 2) == Lazy(lambda: 4.0)


# Generated at 2022-06-14 03:34:36.227491
# Unit test for method map of class Lazy
def test_Lazy_map():
    """
    Testing method map of Lazy
    """
    assert Lazy.of(10).map(lambda x: x + 1).get() == 11

# Generated at 2022-06-14 03:34:42.179382
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    assert (
        Lazy(lambda x: x) ==
        Lazy(lambda x: x)
    )

    assert (
        Lazy(lambda x: x) ==
        Lazy(lambda x: x)
    )

    assert (
        Lazy(lambda x: x) ==
        Lazy(lambda x: x)
    )

    assert (
        Lazy(lambda x: x) ==
        Lazy(lambda x: x)
    )



# Generated at 2022-06-14 03:34:53.295575
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    assert Lazy.of(2).__eq__(Lazy.of(2))
    assert not Lazy.of(2).__eq__(Lazy.of(3))

    assert Lazy.of('a').__eq__(Lazy.of('a'))
    assert not Lazy.of('a').__eq__(Lazy.of('b'))

    assert not Lazy.of('a').__eq__(Lazy.of(3))
    assert not Lazy.of(3).__eq__(Lazy.of('a'))
    assert not Lazy.of(3).__eq__('a')

    assert not Lazy.of(3).__eq__(None)



# Generated at 2022-06-14 03:34:58.669454
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    """
    Test only method `ap` of Lazy class.
    """
    from pymonet.box import Box

    def constructor_fn(x):
        return x + 1

    def mapper(x):
        return x + 2

    assert Box(constructor_fn).ap(Box(mapper)).get() == Box(constructor_fn(mapper(None))).get()
    assert Lazy(constructor_fn).ap(Lazy(mapper)).get() == Lazy(constructor_fn(mapper(None))).get()

# Generated at 2022-06-14 03:35:05.317314
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    assert (
        Lazy.of(lambda x: x + 1).ap(Lazy.of(1)) == Lazy(lambda x: x + 1).ap(Lazy(lambda x: x))
    )

    assert (
        Lazy.of(lambda x: x + 2).ap(Lazy.of(1)) == Lazy.of(3)
    )



# Generated at 2022-06-14 03:35:10.840296
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    """
    Creates Lazy[int, int] then create Lazy[int, int -> int] by map method.
    The constant function can be seen as Lazy[int, int -> int]
    """
    lazy = Lazy.of(1)
    constant_lazy = Lazy.of(lambda x: 1)
    assert lazy.ap(constant_lazy).constructor_fn() == 1

# Generated at 2022-06-14 03:35:14.162254
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def lazy_fn():
        return Lazy.of(1)

    assert Lazy.of(1).bind(lambda x: Lazy.of(x + 1)).get() == 2

# Generated at 2022-06-14 03:35:20.906468
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.either import Right
    from pymonet.monad_try import Try

    def fn(x):
        return x + 2

    lz_fn = Lazy(fn)
    lz_int = Lazy.of(2)

    assert lz_fn.ap(lz_int) == Lazy(lambda *args: lz_fn.get(*args)(lz_int.get(*args)))


# Generated at 2022-06-14 03:35:26.568644
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    assert Lazy(lambda x: x).bind(lambda x: Lazy(lambda y: x + y)).get(2, 3) == 5
    assert Lazy(lambda x: x + 2).bind(lambda x: Lazy(lambda y: x * y)).get(2, 3) == 12
    assert Lazy(lambda x: x).bind(lambda x: Lazy(lambda y: x + y)).get(2, 3) == 5


# Generated at 2022-06-14 03:35:30.598592
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def test_fn(x):
        return x

    def test_bind_fn(x):
        return Lazy(lambda: x)

    def test_bind_type_mismatch(x):
        return x

    assert Lazy.of(1).bind(test_bind_fn).get() == 1
    raises(TypeError, lambda: Lazy.of(1).bind(test_bind_type_mismatch))



# Generated at 2022-06-14 03:35:38.819875
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    import pymonet.monad_option as option

    one_fn = Lazy(lambda: 1)
    assert one_fn.ap(Lazy(lambda x: x + x)) == Lazy(lambda: 2)
    assert one_fn.ap(Lazy(lambda x: x + x)).ap(Lazy(lambda x: x + x)) == Lazy(lambda: 4)

    assert Lazy(lambda _: option.Maybe.just(20)).ap(one_fn.to_maybe()) == Lazy(lambda: option.Maybe.just(20))
    assert Lazy(lambda _: option.Maybe.nothing()).ap(one_fn.to_maybe()) == Lazy(lambda: option.Maybe.nothing())


# Generated at 2022-06-14 03:35:44.902254
# Unit test for method bind of class Lazy
def test_Lazy_bind():  # type: ignore
    def test_method(callable):  # type: ignore
        if callable.is_evaluated:
            assert callable.value == 4
            assert callable.constructor_fn == test_method
            return callable.constructor_fn
        else:
            callable.is_evaluated = True
            callable.value = 4
            return callable.constructor_fn

    assert test_method(Lazy(lambda: 1).bind(lambda x: Lazy(lambda: x + 3)))() == 4

# Generated at 2022-06-14 03:35:47.658788
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():  # pragma: no cover
    a = lambda x: x
    b = lambda x: x
    assert Lazy(a) == Lazy(a)
    assert Lazy(a) != Lazy(b)

# Generated at 2022-06-14 03:35:55.678296
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    test_instance = Lazy(lambda x: x if x >= 5 else None)
    binded_instance = test_instance.bind(lambda x: Lazy(lambda y: x + y))

    assert binded_instance.get(1, 0) is None
    assert binded_instance.get(None, 0) is None
    assert binded_instance.get(None, None) is None
    assert binded_instance.get(None, 100) is None
    assert binded_instance.get(None, -100) is None
    assert binded_instance.get(5, 0) == 5
    assert binded_instance.get(5, -7) == -2
    assert binded_instance.get(5, 7) == 12

# Generated at 2022-06-14 03:36:07.169999
# Unit test for method map of class Lazy
def test_Lazy_map():
    """
    Test map method of class Lazy.

    Running it with pytest
    """
    def test_fn(arg1, arg2):
        return arg1 + arg2

    lazy = Lazy(test_fn)
    assert lazy.get(1, 2) == 3

    new_lazy = lazy.map(lambda x: x * 2)
    assert new_lazy.get(1, 2) == 6

    new_lazy = lazy.map(lambda x: x * 2).map(lambda x: x + 1)
    assert new_lazy.get(1, 2) == 7

    new_lazy = Lazy(lambda a, b: a + b).map(lambda x: x * 2).map(lambda x: x + 1)
    assert new_lazy.get(1, 2) == 7



# Generated at 2022-06-14 03:36:15.986674
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from .lazy import Lazy
    from .util import is_eager

    def mapper(value):
        return value * 2

    def eager_mapper(value):
        eager_mapper.called = True
        return value * 2
    eager_mapper.called = False

    def function(value):
        return lambda result: result + 1

    def eager_function(value):
        eager_function.called = True
        return lambda result: result + 1
    eager_function.called = False

    assert Lazy(mapper).ap(Lazy(function)(1)).get() == Lazy(mapper).map(eager_mapper).map(eager_function)(1)
    assert eager_mapper.called and eager_function.called

# Generated at 2022-06-14 03:36:21.002226
# Unit test for method map of class Lazy
def test_Lazy_map():
    assert Lazy.of(1).map(lambda x: x + 1).get() == 2
    assert Lazy.of(2).map(lambda x: x + 2).get() == 4
    assert Lazy.of(3).map(lambda x: x + 3).get() == 6


# Generated at 2022-06-14 03:36:27.522019
# Unit test for method bind of class Lazy
def test_Lazy_bind():  # pragma: no cover
    # given
    def add(x):
        return x + 1
    thunk = Lazy.of(1)

    # when
    mapped_thunk = thunk.bind(lambda x: Lazy.of(add(x)))

    # then
    assert mapped_thunk.get() == 2



# Generated at 2022-06-14 03:36:31.226446
# Unit test for method map of class Lazy
def test_Lazy_map():
    from decimal import Decimal
    lazy = Lazy(lambda x: x * 2)
    assert lazy.map(lambda v: Decimal(v) / 2) == Lazy(lambda x: x)

# Generated at 2022-06-14 03:36:36.800915
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.applicative import Applicative

    f = Lazy.of(lambda arg: arg + 1)
    g = Lazy.of(1)
    assert isinstance(f, Applicative)
    assert isinstance(g, Applicative)

    result = f.ap(g)
    assert isinstance(result, Lazy)
    assert result.get() == 2

# Generated at 2022-06-14 03:36:40.298495
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def f(a):
        def fn(b):
            return a * b

        return Lazy(fn)

    assert Lazy(lambda: 4).bind(f)(1) == 4
    assert Lazy(lambda: 5).bind(f)(1) == 5


# Generated at 2022-06-14 03:36:43.333798
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def multiplication(number):
        return Lazy(lambda x: x * number)

    assert Lazy.of(4).bind(multiplication).get(2) == 8



# Generated at 2022-06-14 03:36:46.470228
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    assert Lazy(lambda: 1).bind(lambda x: Lazy.of(x + 1)).get(1) == 2  # type: ignore


# Generated at 2022-06-14 03:36:49.130848
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    assert Lazy.of(lambda x: x + 1).ap(Lazy.of(1)) == Lazy.of(2)


# Generated at 2022-06-14 03:36:56.651928
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.either import Right

    lazy = Lazy(lambda *_: Right(1))
    lazy_new = lazy.bind(lambda a: Right(a + 1))
    assert lazy_new.get() == Right(2)


# Generated at 2022-06-14 03:37:00.825605
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    import pymonet.maybe as maybe

    my_lazy = Lazy.of(lambda x, y: x + y)
    result = my_lazy.ap(maybe.Maybe.just(1)).ap(maybe.Maybe.just(2))
    assert result.to_maybe() == maybe.Maybe.just(3)

    # Example from Maybe monad
    m = maybe.Maybe.just(lambda x: x * y).ap(maybe.Maybe.just(x))
    assert m.to_maybe() == maybe.Maybe.just(-10)

# Generated at 2022-06-14 03:37:07.964893
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    import pytest

    assert Lazy(lambda x: x * 3).ap(Lazy(lambda y: y + 5)).get(1) == 18
    assert Lazy(lambda x: x * 3).ap(Lazy(lambda y: y + 5)).get(10) == 45
    assert Lazy(lambda x: x * 3).ap(Lazy(lambda y: y + 5)).get(100) == 305

    assert Lazy(lambda x: x * 3).ap(Lazy(lambda y: y + 5)).to_box(1) == Lazy(lambda x: x * 3).ap(Lazy(lambda y: y + 5)).get(1)

# Generated at 2022-06-14 03:37:12.425616
# Unit test for method bind of class Lazy
def test_Lazy_bind():  # pragma: no cover
    def add_func(a):
        return Lazy(lambda b: a + b)

    # Lazy is callable function so we need call him
    lazy = Lazy(lambda a: a * 2)

    assert lazy.bind(add_func)(10).get() == 20

# Generated at 2022-06-14 03:37:17.108802
# Unit test for method ap of class Lazy
def test_Lazy_ap():  # pragma: no cover
    def get_foo() -> str:
        return 'foo'

    def add_foo_to_start(value: str) -> str:
        return 'foo' + value

    lazy = Lazy(get_foo)
    add_foo_lazy = Lazy(add_foo_to_start)

    assert lazy.ap(add_foo_lazy).get() == 'foofoo'



# Generated at 2022-06-14 03:37:22.597973
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def mapper(name):
        return Lazy(lambda x: x)

    assert Lazy.of('test').bind(mapper) == Lazy(lambda x: 'test')
    assert Lazy.of('test').bind(mapper).bind(mapper) == Lazy(lambda x: 'test')


# Generated at 2022-06-14 03:37:28.310178
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def add_two_to_lazy_int(x: Lazy[int, int]) -> Lazy[int, int]:
        return x.map(lambda a: a + 2)

    destination = Lazy.of(1)
    destination = destination.bind(add_two_to_lazy_int)
    result = destination.get()
    assert result == 3
    assert destination.is_evaluated == True


# Generated at 2022-06-14 03:37:32.696126
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    lazy = Lazy.of(5).ap(Lazy.of(lambda x: x * 2))
    assert lazy.get() == 10

    lazy = Lazy.of(5).ap(Lazy.of(lambda x: x * 2)).ap(Lazy.of(lambda x: x * x))
    assert lazy.get() == 100



# Generated at 2022-06-14 03:37:43.932388
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    """
    Unit test for method bind of class Lazy.
    """
    from pymonet.either import Right
    from pymonet.maybe import Maybe

    def plus(value1, value2):
        """
        Function add two values and wrap it in any monad.
        """
        return (value1 + value2).to_maybe()

    def multiply(value1, value2):
        """
        Function multiply two values and wrap it in any monad.
        """
        return (value1 * value2).to_maybe()

    def subtract(value1, value2):
        """
        Function subtract two values and wrap it in any monad.
        """
        return (value1 - value2).to_maybe()


# Generated at 2022-06-14 03:37:49.140971
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    assert Lazy.of(lambda x: x+20).ap(Lazy.of(30)) == Lazy.of(50), "Test Lazy.ap failed"
    assert Lazy.of(lambda x: x+20).ap(Lazy.of(30)).ap(Lazy.of(20)) == Lazy.of(20).ap(Lazy.of(lambda x: x+30)), "Test Lazy.ap failed"

# Generated at 2022-06-14 03:38:06.187186
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.monad_try import Try

    def io_safe_read_book(path: str) -> Try[str]:
        from io import open

        try:
            with open(path, encoding='utf-8') as f:
                return Try.of(lambda: f.read())
        except IOError as e:
            return Try.error(e)

    def process_book_content(content: str) -> Lazy[str, int]:
        return Lazy(lambda: len(content))

    def process_book(path: str) -> Lazy[str, int]:
        return Lazy(lambda: io_safe_read_book(path)).bind(process_book_content)

    assert process_book('data/book.txt').get() == 34
    assert process_book('data/book2.txt').get()

# Generated at 2022-06-14 03:38:14.184090
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    def add(x):
        return Lazy.of(x + 3)

    def mult(x):
        return Lazy.of(x * 2)

    assert Lazy.of(3) \
        .ap(add(1)) \
        .ap(mult(7)) \
        .get() == 27

    assert (Lazy.of(3)
            .ap(add(1))
            .ap(mult(7))
            .map(lambda x: x + 1)
            .get() == 28)

    assert (Lazy.of(3)
            .ap(add(1))
            .ap(mult(7))
            .map(lambda x: x + 1)
            .bind(add)
            .get() == 30)


# Generated at 2022-06-14 03:38:24.535240
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    class Foo:
        def __init__(self, foo: int) -> None:
            self.foo = foo

        def __eq__(self, other: object) -> bool: # pragma: no cover
            return self.foo == other.foo

        def __repr__(self) -> str: # pragma: no cover
            return '[foo = {}]'.format(self.foo)

    def bar(foo: Foo) -> Foo:
        return Foo(2 * foo.foo)

    def baz(foo: Foo) -> Foo:
        return Foo(3 * foo.foo)

    lazy = Lazy.of(Foo(1))
    assert (lazy.bind(bar).bind(baz).get()) == Foo(6)

# Generated at 2022-06-14 03:38:29.256986
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def some_function(x):
        import random
        return random.randint(3, 3)

    def some_other_function(x):
        import random
        return Lazy(lambda: random.randint(4, 4))

    lazy_some_function = Lazy(some_function)

    first_test = lazy_some_function.bind(some_other_function)
    second_test = lazy_some_function.bind(some_other_function)

    assert first_test.get() == 4
    assert second_test.get() == 4
    assert first_test == second_test


# Generated at 2022-06-14 03:38:35.865575
# Unit test for method bind of class Lazy
def test_Lazy_bind():  # pragma: no cover
    def fn1(x):
        return Lazy.of(2)

    def fn2(x):
        return Lazy.of(x)

    def fn3(x):
        return Lazy.of(x)

    composed_fn = Lazy(fn1).bind(fn2).bind(fn3)

    assert composed_fn.get(1) == 2

# Generated at 2022-06-14 03:38:39.877625
# Unit test for method bind of class Lazy
def test_Lazy_bind():  # pragma: no cover
    lazy = Lazy(lambda x: str(x)).bind(lambda x: Lazy(lambda: x))

    assert lazy.get(3) == '3'
    assert lazy.get(4) == lazy.get(4)



# Generated at 2022-06-14 03:38:43.401897
# Unit test for method map of class Lazy
def test_Lazy_map():
    def add_one(val):
        return val + 1

    lazy = Lazy.of(1)
    lazy_mapped = lazy.map(add_one)

    assert Lazy(add_one).map(add_one).get() == lazy_mapped.get()


# Generated at 2022-06-14 03:38:45.374886
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    lazy_list = Lazy.of(lambda a: [a, a])
    lazy_val = Lazy.of(2)
    result_lazy_ap = lazy_list.ap(lazy_val)

    assert result_lazy_ap == Lazy(lambda: [2, 2])



# Generated at 2022-06-14 03:38:48.347500
# Unit test for method map of class Lazy
def test_Lazy_map():
    """
    Test method map of class Lazy
    """
    lazy = Lazy.of(lambda x: x * 2)
    assert lazy.map(lambda x: x + 3).get(2) == (2 * 2) + 3



# Generated at 2022-06-14 03:38:50.805765
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    assert Lazy.of(lambda x: x + 1).ap(Lazy.of(1)) == Lazy.of(2)


# Generated at 2022-06-14 03:39:15.485625
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    a = Lazy(lambda: 2)
    b = a.bind(lambda x: Lazy(lambda: x + 2))
    c = a.bind(lambda x: Lazy(lambda: x + 3))
    assert b._compute_value() == 4
    assert c._compute_value() == 5


# Generated at 2022-06-14 03:39:22.143467
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.functor import Functor

    assert Lazy.of(lambda x: x + 5).ap(Lazy.of(4)) == Lazy.of(9)
    assert Lazy.of(lambda x: x + 5).ap(Functor.of(4)) == Lazy.of(9)



# Generated at 2022-06-14 03:39:25.258388
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    assert Lazy.of(lambda x, y: x + y).ap(Lazy.of(1)).ap(Lazy.of(2)).get() == 3
    assert Lazy.of(lambda x, y: x + y).ap(Lazy.of(1)).ap(Lazy.of(2)).to_box().get() == 3


# Generated at 2022-06-14 03:39:28.772284
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.either import Right
    from pymonet.monad_try import Try

    counter = 0

    lazy_result = Lazy(lambda: counter)
    lazy_result = lazy_result.bind(lambda c: Right(Lazy(lambda: c * 4)))
    lazy_result = lazy_result.bind(lambda c: Try(lambda: c * 2))

    counter = 2
    # Try[8]
    assert lazy_result.get() == Try.success(8)

# Generated at 2022-06-14 03:39:37.903733
# Unit test for method bind of class Lazy
def test_Lazy_bind():

    lazy = Lazy(lambda x: x)
    assert lazy.bind(lambda x: Lazy(lambda y: x + y)).constructor_fn(2)(3) == 5

    lazy = Lazy(lambda x: x)
    assert (
        lazy.map(lambda x: x + 1).bind(
            lambda x: Lazy(lambda y: x * y)
        ).constructor_fn(2, 4) == 10
    )
    assert (
        lazy.map(lambda x: x + 1).bind(
            lambda x: Lazy(lambda y: x * y)
        ).constructor_fn(2, 4) == 10
    )



# Generated at 2022-06-14 03:39:43.520707
# Unit test for method map of class Lazy
def test_Lazy_map():
    from pymonet.box import Box
    from pymonet.lazy import Lazy

    def mapper(value):
        return Lazy.of(Box(value))

    assert Lazy.of(1).map(mapper).get() == Box(1)
    assert Lazy.of(2).map(mapper).get() == Box(2)



# Generated at 2022-06-14 03:39:54.627508
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    def identity(one):
        return one

    def twice(one):
        return one * 2

    def string_two():
        return 'two'

    def string_four():
        return 'four'

    assert Lazy(identity).ap(Lazy(twice)) == Lazy(identity).ap(Lazy(twice))

    assert Lazy(identity).map(twice).map(twice) == Lazy(identity).map(twice).map(twice)

    assert Lazy(twice).map(twice).bind(Lazy.of) == Lazy(twice).map(twice).bind(Lazy.of)

    assert Lazy(string_two).bind(lambda it: Lazy(twice).map(twice).bind(Lazy.of)) == Lazy(string_two).bind

# Generated at 2022-06-14 03:40:04.497759
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__(): # pragma: no cover
    from pymonet.function import identity
    from pymonet.function import compose

    from pymonet.box import Box

    def add_one(value):
        return Lazy.of(value + 1)

    function_64_pass_64 = lambda: 64
    function_64_pass_128 = lambda: 128

    assert Lazy(function_64_pass_64) == Lazy(function_64_pass_64)
    assert not Lazy(function_64_pass_64) == Lazy(function_64_pass_128)

    result = compose(add_one, Lazy(function_64_pass_64))

    assert result == Lazy(function_64_pass_64).map(add_one)


# Generated at 2022-06-14 03:40:07.207305
# Unit test for method map of class Lazy
def test_Lazy_map():
    def fn(x: int) -> int:
        return x + 1

    assert Lazy.of(1).map(fn).get() == 2

# Generated at 2022-06-14 03:40:17.011118
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    """
    Tests Lazy monad with bind method usage.
    """
    def get_value():
        return 'value'

    def external_mapper(value):
        assert value == 'value'
        return 'mapped_value'

    @Lazy
    def get_lazy_value():
        return get_value()

    @Lazy
    def get_mapped_value():
        return external_mapper(get_lazy_value.get())

    result = get_mapped_value.get()
    expected_result = 'mapped_value'
    assert result == expected_result



# Generated at 2022-06-14 03:41:01.089290
# Unit test for method ap of class Lazy
def test_Lazy_ap():  # pragma: no cover
    from pymonet.functor import Functor
    def add(x):
        return x + 1
    def times(x):
        return x * 3

    class A(Functor):
        def map(self, f):
            return f(1)

    a = A()
    b = Lazy.of(add).map(lambda n: n(1))
    l = b.ap(a)
    assert l._compute_value() == 2

    c = Lazy.of(times)
    d = Lazy.of(add)
    l2 = c.ap(d)
    assert l2._compute_value(1) == 4



# Generated at 2022-06-14 03:41:04.068962
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def fn(x):
        return Lazy(lambda: x + 1)

    assert Lazy(lambda: 1).bind(fn).get() == 2



# Generated at 2022-06-14 03:41:06.861651
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.list import List

    def fn(value):
        def inner_fn(v):
            return List.of(v ** 2)

        return value.bind(inner_fn)

    Lazy(lambda: List.of(1, 2, 3)).bind(fn).get() == [1, 4, 9]



# Generated at 2022-06-14 03:41:13.172155
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.box import Box
    from pymonet.either import Right
    from pymonet.maybe import Maybe
    from pymonet.monad_try import Try
    from pymonet.validation import Validation
    from hypothesis import given
    from hypothesis.strategies import integers, lists, booleans

    @given(integers(), integers())
    def div_test_fn(value, divider):
        if divider == 0:
            raise ValueError("Not zero!")
        return value / divider

    def create_success_validation(value):
        return Validation.success(value)

    def create_fail_validation(_):
        return Validation.fail("division by zero")


# Generated at 2022-06-14 03:41:20.346875
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.validation import Validation
    from pymonet.box import Box
    from pymonet.maybe import Maybe
    from pymonet.monad_try import Try

    assert Lazy.of(1).ap(Lazy.of(lambda x: x + 1)).get() == 2
    assert Lazy.of(1).ap(Lazy.of(Box(lambda x: x + 1))).get() == 2
    assert Lazy.of(1).ap(Lazy.of(Maybe.just(lambda x: x + 1))).get() == 2
    assert Lazy.of(1).ap(Lazy.of(Try.of(lambda x: x + 1))).get() == 2

# Generated at 2022-06-14 03:41:30.648956
# Unit test for method ap of class Lazy
def test_Lazy_ap():  # pragma: no cover
    from pymonet.box import Box

    def fn_to_map(x):  # pragma: no cover
        return x + 4

    assert Lazy.of(1).ap(Lazy.of(fn_to_map)).get() == 5
    assert Lazy.of(2).ap(Lazy.of(fn_to_map)).get() == 6
    assert Lazy.of(3).ap(Lazy.of(fn_to_map)).get() == 7
    assert Lazy.of(1).ap(Box(fn_to_map)).get() == 5
    assert Lazy.of(2).ap(Box(fn_to_map)).get() == 6
    assert Lazy.of(3).ap(Box(fn_to_map)).get() == 7

