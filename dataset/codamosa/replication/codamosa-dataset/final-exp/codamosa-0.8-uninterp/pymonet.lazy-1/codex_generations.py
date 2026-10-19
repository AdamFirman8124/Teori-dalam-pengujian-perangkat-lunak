

# Generated at 2022-06-14 03:31:30.871023
# Unit test for method get of class Lazy
def test_Lazy_get():
    lazy = Lazy(lambda x: x + 1)

    assert lazy.get(1) == 2


# Generated at 2022-06-14 03:31:34.588609
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    from pymonet.function import compose

    # GIVEN
    # WHEN
    lazy1 = Lazy(compose(lambda x: x * 2, lambda x: x + 1))
    lazy2 = Lazy(compose(lambda x: x * 2, lambda x: x + 1))
    lazy3 = Lazy(compose(lambda x: x * 12, lambda x: x + 1))

    # THEN
    assert lazy1 == lazy2
    assert lazy1 != lazy3



# Generated at 2022-06-14 03:31:39.688315
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.monad_maybe import Maybe

    assert Lazy(lambda x: x + 1).ap(
        Maybe.just(lambda x: x + 2)
    ).get(2) == 5


# Unit tests for method bind of class Lazy

# Generated at 2022-06-14 03:31:47.947692
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    from pymonet.function import compose

    just_5_lazy = Lazy.of(5)
    just_5_lazy_2 = Lazy.of(5)
    just_5_lazy_3 = just_5_lazy_2.map(lambda x: x)

    assert just_5_lazy == just_5_lazy
    assert just_5_lazy_3 == just_5_lazy
    assert just_5_lazy != just_5_lazy_2



# Generated at 2022-06-14 03:31:54.029329
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    assert (
        Lazy(lambda arg: arg[0] ** arg[1]).ap(Lazy(lambda arg: arg[0] + arg[1]))
    ) == Lazy(lambda arg: (arg[0] + arg[1]) ** (arg[0] + arg[1]))



# Generated at 2022-06-14 03:32:04.851277
# Unit test for method get of class Lazy
def test_Lazy_get():
    from pymonet.box import Box
    from pymonet.maybe import Maybe
    from pymonet.monad_try import Try
    from pymonet.validation import Validation

    def throwing_lazy_fn(arg):
        raise Exception('Error')

    def throwing_lazy_fn2(arg):
        raise Exception('Error')

    lazy_fn = Lazy(lambda x: 'test')
    lazy_throwing_fn = Lazy(throwing_lazy_fn)
    lazy_throwing_fn2 = Lazy(throwing_lazy_fn2)
    assert lazy_fn.get() == 'test'
    assert lazy_fn.to_box().get() == Box('test')
    assert lazy_fn.to_either().get() == 'test'

# Generated at 2022-06-14 03:32:11.894369
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.box import Box
    from pymonet.validation import Validation

    lazy_result = Lazy.of(lambda x: x + 1)
    box_result = Box(1)
    validation_result = Validation.success(1)

    assert lazy_result.ap(box_result) == Lazy.of(2)
    assert lazy_result.ap(validation_result) == Lazy.of(2)


# Generated at 2022-06-14 03:32:16.858820
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    def test_fn(x):
        pass

    lazy = Lazy(test_fn)
    assert lazy == Lazy(test_fn)

    lazy.get('')
    lazy2 = Lazy(test_fn)
    lazy2.get('')

    assert lazy == lazy2


# Generated at 2022-06-14 03:32:28.866597
# Unit test for method map of class Lazy
def test_Lazy_map():
    """
    Test method map of class Lazy
    """
    def test_function(n):
        return n ** 2 + n

    test_lazy = Lazy(lambda n: n ** 2 + n)
    mapped_lazy = test_lazy.map(lambda n: n * 3 + 1)

    assert type(test_lazy) == Lazy
    assert type(mapped_lazy) == Lazy
    assert test_lazy.get(2) == test_function(2)
    assert mapped_lazy.get(2) == test_function(2) * 3 + 1
    assert test_lazy.get(3) == test_function(3)
    assert mapped_lazy.get(3) == test_function(3) * 3 + 1


# Generated at 2022-06-14 03:32:34.801930
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    assert (
        Lazy(lambda x: x)
        .bind(lambda x: Lazy(lambda y: x + y))
        .get(1, 2)
    ) == 3
    assert (
        Lazy(lambda x: x)
        .bind(lambda x: Lazy('{} seconds'.format(x)))
        .get(1)
    ) == '1 seconds'

# Generated at 2022-06-14 03:32:41.904084
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.identity import Identity

    assert Lazy.of(1).bind(lambda x: Lazy.of(x + 1)) == Lazy.of(2)
    assert Lazy.of(1).bind(lambda x: Identity(x + 1)).fold() == 2



# Generated at 2022-06-14 03:32:45.318523
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    lazy = Lazy(lambda x: x+1)
    lazy2 = Lazy(lambda x: x+1)
    assert lazy == lazy2

    lazy3 = Lazy(lambda x: x+3)
    assert lazy != lazy3


# Generated at 2022-06-14 03:32:50.265931
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    @Lazy
    def test_Lazy(*args):
        return "test lazy value"

    @Lazy
    def test_Lazy_1(*args):
        return "test lazy value"

    assert test_Lazy == test_Lazy_1



# Generated at 2022-06-14 03:32:58.321165
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    def fn():
        return 1

    assert not Lazy(fn) == Lazy(fn)
    assert Lazy(fn) == Lazy(fn)
    assert not Lazy(fn) == 1
    assert not Lazy(fn) == 1.0
    assert not Lazy(fn) == "Lazy(fn)"
    assert not Lazy(fn) == tuple()
    assert not Lazy(fn) == dict()
    assert not Lazy(fn) == list()
    assert not Lazy(fn) == set()
    assert not Lazy(fn) == frozenset()
    assert not Lazy(fn) == object()


# Generated at 2022-06-14 03:33:02.579195
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():  # pragma: no cover
    def a():
        return 'a'

    def b():
        return 'b'

    Lazy(a) == Lazy(a)
    Lazy(a).map(b) == Lazy(a).map(b)
    Lazy(a) != Lazy(b)
    Lazy(a).map(b) != Lazy(a).map(a)


# Unit tests for method of of class Lazy

# Generated at 2022-06-14 03:33:07.507519
# Unit test for method get of class Lazy
def test_Lazy_get():
    assert Lazy(lambda: 5).get() == 5
    assert Lazy(lambda: 7).get() == 7
    assert Lazy(lambda: 'asf').get() == 'asf'
    assert Lazy(lambda: True).get() is True
    assert Lazy(lambda: None).get() is None


# Generated at 2022-06-14 03:33:18.282494
# Unit test for method map of class Lazy
def test_Lazy_map():
    def test_function_to_map(p: int) -> int:
        return p + 4

    lazy_obj = Lazy.of(2)  # constructor_fn = lambda: 2
    mapped_lazy = lazy_obj.map(test_function_to_map)  # constructor_fn = lambda: test_function_to_map(lazy_obj.constructor_fn())
    assert mapped_lazy.get() == 6

    def test_function_to_map(p: str) -> str:
        return p + "2"

    lazy_obj = Lazy.of("2")  # constructor_fn = lambda: 2
    mapped_lazy = lazy_obj.map(test_function_to_map)  # constructor_fn = lambda: test_function_to_map(lazy_obj.constructor_fn())

# Generated at 2022-06-14 03:33:22.355307
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def constructor_fn(arg):
        return arg

    def mapper(arg):
        return Lazy(lambda *args: arg)

    assert Lazy(constructor_fn).bind(mapper).get(1) == 1

# Generated at 2022-06-14 03:33:28.970775
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.box import Box
    from pymonet.either import Left
    from pymonet.maybe import Maybe
    from pymonet.monad_try import Try
    from pymonet.validation import Validation, Success, Failure

    pf = lambda i: Lazy(lambda x: Box(x * i))
    assert Lazy(lambda x: x).bind(pf).get(4) == 16

    pf = lambda i: Lazy(lambda x: Left(x * i))
    assert Lazy(lambda x: x).bind(pf).get(4) == Left(16)

    pf = lambda i: Lazy(lambda x: Maybe.just(x * i))
    assert Lazy(lambda x: x).bind(pf).get(4) == Maybe.just(16)


# Generated at 2022-06-14 03:33:33.922991
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    """Unit test for method bind of class Lazy"""
    _lazy = Lazy(lambda value, x: value * x).bind(lambda value: Lazy(lambda x: value * x))
    assert _lazy.get(2, 3) == 12

# Generated at 2022-06-14 03:33:41.368444
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    def double(x):
        return x * 2

    assert Lazy(double) == Lazy(double)

    def triple(x):
        return x * 3

    assert not Lazy(double) == Lazy(triple)

    assert not Lazy(double) == Lazy.of(4)

    assert not Lazy(double) == "4"



# Generated at 2022-06-14 03:33:46.378858
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    class Record:
        str_value = 'default'

    def constructor_fn():
        return Record()

    def mapper(record):
        return record.str_value

    def setter(record):
        record.str_value = 'test'
        return record

    assert Lazy(constructor_fn).bind(setter).bind(mapper).get() == 'test'

# Generated at 2022-06-14 03:33:55.243316
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    """
    Unit test for method __eq__ of class Lazy
    """
    import datetime

    from pymonet.monad_try import Try
    from pymonet.validation import Validation

    now = datetime.datetime.now()

    my_lazy = Lazy.of(now)
    assert (my_lazy.to_box() == Box.of(now))
    assert (my_lazy.to_either() == Either.of(now))
    assert (my_lazy.to_maybe() == Maybe.of(now))
    assert (my_lazy.to_try() == Try.of(lambda: now))
    assert (my_lazy.to_validation() == Validation.success(now))



# Generated at 2022-06-14 03:34:03.568929
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    # pylint: disable=unused-argument,unnecessary-lambda,pointless-string-statement,invalid-name
    def f(x: int) -> Lazy[int, int]:
        return Lazy(lambda _x: _x + 5)

    assert Lazy(lambda: 10).bind(f).get() == 15
    assert Lazy(lambda: 1).bind(lambda x: Lazy(lambda: 2 * x)).get() == 2
    assert Lazy(lambda: 2).bind(lambda x: Lazy(lambda: 2 * x)).get() == 4



# Generated at 2022-06-14 03:34:08.026983
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def fn(a):
        return Lazy.of(a ** 2)

    lazy = Lazy.of(10)
    assert lazy.bind(fn).get() == 100
    assert lazy.bind(fn) == Lazy.of(100)

# Generated at 2022-06-14 03:34:14.697864
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():  # pragma: no cover
    assert Lazy.of(lambda: 2) == Lazy.of(lambda: 2)
    assert not Lazy.of(lambda: 2) == Lazy.of(3)
    assert not Lazy.of(lambda: 2) == Lazy.of(lambda: 3)
    assert not Lazy.of(lambda: 2) == None

# Generated at 2022-06-14 03:34:25.093551
# Unit test for method get of class Lazy
def test_Lazy_get():
    from pymonet.monad_maybe import Maybe

    def mapper(x):
        return x + 1

    def fold_fn(*args):
        return Lazy(lambda: 2)

    test_fn = lambda: 1

    lazy_1 = Lazy(test_fn)
    lazy_2 = Lazy(test_fn).map(mapper)
    lazy_3 = Lazy(test_fn).bind(fold_fn)
    lazy_4 = Lazy(lambda: Maybe.just(1)).bind(lambda x: x.map(mapper))

    assert lazy_1.get() == 1
    assert lazy_2.get() == 2
    assert lazy_3.get() == 2
    assert lazy_4.to_maybe().get() == 2

# Generated at 2022-06-14 03:34:31.789699
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    # given
    fn1 = lambda x: x + 1
    fn2 = lambda x: x * 3
    lazy1 = Lazy(fn1)
    lazy2 = Lazy(fn1)
    lazy3 = Lazy(fn2)

    # then
    assert lazy1 == lazy2
    assert lazy1 != lazy3

    # given
    lazy1._compute_value(1)
    lazy2._compute_value(1)
    lazy3._compute_value(1)

    # then
    assert lazy1 == lazy2
    assert lazy1 != lazy3


# Generated at 2022-06-14 03:34:41.915905
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    def add(x):
        return x + 1

    def add2(x):
        return x + 2

    def add3(x):
        return x + 3

    lazy = Lazy.of(add)

    add1 = lazy.ap(Lazy.of(1)).get()
    add2 = lazy.ap(Lazy.of(1)).ap(Lazy.of(1)).get()
    add3 = lazy.ap(Lazy.of(1)).ap(Lazy.of(2)).get()

    assert add1 == 2, 'Lazy ap with 1 argument should return 2'
    assert add2 == 3, 'Lazy ap with 2 arguments should return 3'
    assert add3 == 4, 'Lazy ap with 3 arguments should return 4'



# Generated at 2022-06-14 03:34:50.349607
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    def add(a, b):
        return a + b

    def increment(x):
        return x + 1

    assert Lazy.of(add).ap(Lazy.of(1)).ap(Lazy.of(2)).get() == add(1, 2)
    assert Lazy.of(add).ap(Lazy.of(increment).ap(Lazy.of(1))).ap(Lazy.of(2)).get() == add(2, 2)



# Generated at 2022-06-14 03:34:55.522002
# Unit test for method get of class Lazy
def test_Lazy_get():
    assert Lazy.of(1).get() == Lazy(lambda: 1).get() == 1
    assert Lazy.of().get() == Lazy(lambda: None).get() is None


# Generated at 2022-06-14 03:35:07.538434
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    def f1(a):
        return a

    def f2(a):
        return -a

    def f3(a):
        return a

    def f4(a):
        return a

    notEqual1 = Lazy(f1)
    notEqual2 = Lazy(f1)
    notEqual3 = Lazy(f2)
    notEqual4 = Lazy(f1)
    notEqual4._compute_value(1)
    notEqual4._compute_value(1)
    equal1 = Lazy(f3)
    equal2 = Lazy(f3)
    equal3 = Lazy(f4)
    equal3._compute_value(1)
    equal3._compute_value(1)
    assert notEqual1 != notEqual2
   

# Generated at 2022-06-14 03:35:13.595086
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():  # pragma: no cover
    def positive_fn(op):
        return op > 0

    def negative_fn(op):
        return op < 0

    assert Lazy(positive_fn).__eq__(Lazy(positive_fn))
    assert Lazy(positive_fn).__eq__(Lazy(negative_fn)) is False



# Generated at 2022-06-14 03:35:18.035120
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    assert Lazy(lambda x: x) == Lazy(lambda x: x)
    assert Lazy(lambda x: x) != Lazy(lambda x: x + 1)
    assert Lazy(lambda x: x).map(lambda x: x + 1) != Lazy(lambda x: x).map(lambda x: x)

# Generated at 2022-06-14 03:35:22.371892
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():  # pragma: no cover
    def construct_fn(*args):
        return 'value'

    lazy = Lazy(construct_fn)

    assert lazy == Lazy.of('value')

    lazy.get()

    assert lazy == Lazy.of('value')



# Generated at 2022-06-14 03:35:32.445730
# Unit test for method map of class Lazy
def test_Lazy_map():
    from pymonet.maybe import Maybe
    from pymonet.box import Box

    def test_Lazy(x: int) -> Lazy[int, int]:
        return Lazy(lambda: x)

    assert test_Lazy(5).map(lambda x: x + 1).get() == 6
    assert test_Lazy(5).map(Box.of).get().get() == 5
    assert test_Lazy(5).map(lambda _: 'test').get() == 'test'
    assert test_Lazy(5).map(Maybe.just).get() == Maybe.just(5)
    assert test_Lazy(5).map(Lazy.of).get() == Lazy.of(5)



# Generated at 2022-06-14 03:35:37.459746
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():  # pragma: no cover
    a = Lazy.of(0)
    b = Lazy.of(0)
    c = Lazy.of(1)

    assert a == b
    assert a != c
    assert id(a) != id(b)



# Generated at 2022-06-14 03:35:45.375585
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    # GIVEN
    lazy1 = Lazy(lambda: 'lazy1')
    lazy2 = Lazy(lambda: 'lazy2')

    # WHEN
    result1 = lazy1 == lazy1
    result2 = lazy1 == lazy2
    result3 = lazy1 == Lazy(lambda: 'lazy1')
    result4 = lazy1 == 1
    result5 = Lazy(lambda: 1) == Lazy(lambda: 1)
    result6 = Lazy(lambda: 1) == Lazy(lambda: 2)

    # THEN
    assert result1 is True
    assert result2 is False
    assert result3 is True
    assert result4 is False
    assert result5 is True
    assert result6 is False



# Generated at 2022-06-14 03:35:51.113502
# Unit test for method map of class Lazy
def test_Lazy_map():
    # GIVEN
    lazy_data = Lazy(lambda x: x + 1)
    mapper = lambda x: x * 2
    result = Lazy(lambda x: 2 * (x + 1))

    # WHEN
    lazy_mapper = lazy_data.map(mapper)

    # THEN
    assert lazy_mapper(1) == result(1)


# Generated at 2022-06-14 03:35:57.934767
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    def func1():  # pragma: no cover
        return 1

    def func2(x):  # pragma: no cover
        return x

    assert Lazy(func1) == Lazy(func1)
    assert Lazy(func2) == Lazy(func2)
    assert Lazy(func1) != Lazy(func2)



# Generated at 2022-06-14 03:36:02.577693
# Unit test for method get of class Lazy
def test_Lazy_get():  # pragma: no cover
    assert Lazy.of(1).get() == 1

# Generated at 2022-06-14 03:36:06.637210
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def invert_number(number):
        return Lazy.of(number - 1)

    lazy = Lazy(lambda: 1)
    result = lazy.bind(invert_number)
    assert result.get() == 0



# Generated at 2022-06-14 03:36:15.679048
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    """
    Unit test for method ap of class Lazy
    """
    assert Lazy.of(lambda x: x * 3).ap(Lazy.of(2)) == Lazy.of(6)
    assert Lazy.of(lambda x: x * 3).ap(Lazy.of(0)) == Lazy.of(0)

    assert Lazy.of(lambda x: x * 3).ap(Lazy.of()) == Lazy.of(None)
    assert Lazy.of().ap(Lazy.of(2)) == Lazy.of(None)

    assert Lazy.of(lambda x, y: x * y).ap(Lazy.of(2)).ap(Lazy.of(3)) == Lazy.of(6)

# Generated at 2022-06-14 03:36:25.019907
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    import pytest

    # Test case data
    lazy = Lazy(lambda: 2)

    def double(value):
        return Lazy(lambda: value * 2)

    def triple(value):
        return Lazy(lambda: value * 3)

    # Test case
    assert lazy.bind(double).bind(triple).get() == 12
    assert lazy.bind(double).bind(triple) == Lazy(lambda: 12)
    assert lazy.bind(double).bind(triple).is_evaluated is True
    assert lazy.bind(double).bind(triple).value == 12

    assert lazy.bind(double).get() == 4
    assert lazy.bind(double).is_evaluated is True
    assert lazy.bind(double).value == 4

    assert lazy.bind(triple).get() == 6
    assert lazy

# Generated at 2022-06-14 03:36:31.228019
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    assert Lazy.of(lambda x: x + 1)\
        .ap(Lazy.of(1)) == Lazy.of(2)

    assert Lazy.of(lambda x, y: x * y)\
        .ap(Lazy.of(2))\
        .ap(Lazy.of(3)) == Lazy.of(6)



# Generated at 2022-06-14 03:36:35.438048
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    def add(a, b):
        return a + b
    def sub(a, b):
        return a - b

    lazy_add = Lazy(add)
    lazy_sub = Lazy(sub)
    lazy_add_copy = Lazy(add)

    assert lazy_add == Lazy.of(lazy_add.get(1, 2))
    assert lazy_add == lazy_add_copy
    assert lazy_add != lazy_sub



# Generated at 2022-06-14 03:36:39.528198
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    def test_function(x):
        return x ** 2

    def apply_function(a):
        return test_function(a)

    lazy = Lazy.of(apply_function)
    result_lazy = lazy.ap(Lazy.of(2))
    assert result_lazy.get() == 4

# Generated at 2022-06-14 03:36:52.149971
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    from pymonet.functor import Functor
    from pymonet.monad_try import Try
    unit_value1: Lazy[int, str] = Lazy.of('')
    unit_value2: Lazy[int, str] = Lazy.of('')
    empty_value: Lazy[None, None] = Lazy.of(None)
    failure: Lazy[None, None] = Lazy(lambda: Try.raise_exception())
    mapped_value1: Lazy[Lazy[int, str], str] = Functor.fmap(lambda x: x.upper(), unit_value1)
    mapped_value2: Lazy[Lazy[int, str], str] = Functor.fmap(lambda x: x.upper(), unit_value2)

    assert unit_value1 == unit_

# Generated at 2022-06-14 03:36:59.829515
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.box import Box

    def add(x):
        return Lazy(lambda y: x + y)

    def mul(x):
        return Lazy(lambda y: x * y)

    # ap
    assert Lazy.of(1).ap(Lazy.of(2)) == Lazy.of(2)
    assert Lazy.of(1).map(lambda x: x + 1).ap(Lazy.of(1)) == Lazy.of(2)
    assert Lazy.of(2).ap(Lazy.of( 1).map(lambda x: x + 1)) == Lazy.of(3)

    # Applicative laws

# Generated at 2022-06-14 03:37:01.625410
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    assert Lazy.of(1) == Lazy.of(1)



# Generated at 2022-06-14 03:37:08.902540
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.box import Box

    def constructor_fn(a, b, c):  # pylint: disable=unused-argument
        return Box(4)

    lazy = Lazy(constructor_fn)

    def fn(value):
        return Lazy(lambda: value ** 2)
    assert lazy.bind(fn).get() == 16

# Generated at 2022-06-14 03:37:12.329470
# Unit test for method bind of class Lazy
def test_Lazy_bind():  # pragma: no cover
    assert (
        Lazy.of(lambda a, b: a + b)
        .bind(lambda x: Lazy.of(x(1, 2)))
        .get() == 3
    )

# Generated at 2022-06-14 03:37:14.885945
# Unit test for method map of class Lazy
def test_Lazy_map():
    func = Lazy(lambda x: x + 1)
    new_func = func.map(lambda x: x * 2)
    assert new_func.get(1) == 4



# Generated at 2022-06-14 03:37:19.812347
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    """
    Test for method __eq__ of class Lazy.
    """
    def sum(a, b):
        return a + b

    lazy1 = Lazy(sum)
    lazy2 = Lazy(lambda a, b: a + b)

    assert lazy1 == lazy2

# Generated at 2022-06-14 03:37:21.950444
# Unit test for method map of class Lazy
def test_Lazy_map():
    def func_1(arg):
        return arg * 5

    def func_2(arg):
        return arg * 2

    lazy = Lazy(func_1).map(func_2)

    assert lazy.get(2) == 20



# Generated at 2022-06-14 03:37:25.884590
# Unit test for method get of class Lazy
def test_Lazy_get():
    def add_one(x):
        return x + 1

    result = Lazy(add_one).map(lambda x: x + 1).get(1)

    assert result == 3



# Generated at 2022-06-14 03:37:35.769670
# Unit test for method bind of class Lazy
def test_Lazy_bind():  # pragma: no cover
    """
    Given:  Call Lazy constructor with function returning number and bind with function, which double it.
    When:   bind function is called
    Then:   Bounding function should be called and it's output injected into Lazy constructor
    """

    def _fn(x: int) -> int:
        return x ** 2

    assert (
        Lazy(lambda: 1).bind(lambda x: Lazy(_fn(x))).constructor_fn()  # pylint: disable=no-value-for-parameter
        == _fn(1)
    )
    assert (
        Lazy(lambda: 2).bind(lambda x: Lazy(_fn(x))).constructor_fn()  # pylint: disable=no-value-for-parameter
        == _fn(2)
    )

# Generated at 2022-06-14 03:37:38.405008
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    result = Lazy.of(2).ap(Lazy.of(lambda x: x * 3))
    assert result.get() == 6



# Generated at 2022-06-14 03:37:48.502293
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.box import Box
    import pytest
    add = lambda x: lambda y: x + y
    double = lambda x: 2 * x
    half = lambda x: x / 2
    increment = lambda x: x + 1

    lazy = Lazy.of(1)
    assert lazy.bind(add(1)).bind(half) == Lazy.of(1).bind(lambda x: add(1)(x)).bind(half)
    assert lazy.bind(double).bind(increment) == Lazy.of(1).bind(double).bind(increment)
    assert lazy.bind(double).get() == Lazy.of(1).bind(double).get()
    assert lazy.bind(add(3)).bind(double).get() == Lazy.of(1).bind(lambda x: add(3)(x)).bind

# Generated at 2022-06-14 03:37:52.755954
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():  # pragma: no cover
    import pymonet.functions as F

    assert Lazy.of('1') == Lazy.of('1')
    assert Lazy.of('1') != Lazy.of(2)
    assert Lazy.of(1) != Lazy.of('1')

    assert Lazy(F.identity) != Lazy(F.identity)
    assert Lazy(F.identity) != Lazy(F.addition)


# Generated at 2022-06-14 03:38:05.325341
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.monad_try import Try
    from pymonet.monoid import Sum
    from pymonet.validation import Validation, ValidationError

    method_used = False

    def method(x: Sum) -> Lazy:
        nonlocal method_used
        method_used = method_used or True
        return Lazy.of(x.value)

    # Call bind without calling method
    Lazy.of(Sum(2)).bind(method)
    assert not method_used

    # Call bind with function raising exception
    def raising_fn(x):
        raise Exception
    new_value = Lazy.of(Sum(2)).bind(raising_fn)
    assert isinstance(new_value, Try)
    assert isinstance(new_value.value, Exception)

    # Call bind with function instead of Lazy

# Generated at 2022-06-14 03:38:10.502493
# Unit test for method map of class Lazy
def test_Lazy_map():
    def concat_a_to_b(a, b):
        return a + b

    result = Lazy(concat_a_to_b).map(lambda a: a + '!')

    assert isinstance(result, Lazy)

    assert result.constructor_fn(1, 2) == '12!'
    assert result.constructor_fn(5, 6) == '56!'
    assert result.constructor_fn(8, 9) == '89!'



# Generated at 2022-06-14 03:38:13.921954
# Unit test for method get of class Lazy
def test_Lazy_get():

    def foo(a):
        return a

    x = Lazy(foo)
    assert x.get() is None

# Generated at 2022-06-14 03:38:25.189724
# Unit test for method map of class Lazy
def test_Lazy_map():
    assert (
        Lazy.of(10).map(lambda x: x * 10) == Lazy.of(100)
    )  # Lazy maps function to empty Lazy
    assert (
        Lazy.of(10).map(lambda x: x * 10).map(lambda x: x + 1) == Lazy.of(101)
    )  # Lazy maps function to empty Lazy
    assert (
        Lazy.of(10).map(lambda x: Lazy.of(x * 10)).map(lambda x: x + 1) == Lazy.of(101)
    )  # Lazy maps function to empty Lazy
    assert (
        Lazy.of(10).map(lambda x: Lazy.of(x * 10).get()) == Lazy.of(100)
    )  # Lazy maps function to empty

# Generated at 2022-06-14 03:38:27.765256
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def function(a):
        return Lazy.of(a)

    assert Lazy.of(1).bind(function).get() == 1
    assert Lazy.of(2).bind(function).get() == 2
    assert Lazy.of(3).bind(function).get() == 3



# Generated at 2022-06-14 03:38:31.910729
# Unit test for method map of class Lazy
def test_Lazy_map():
    assert Lazy(lambda x: x).map(lambda x: x * 2).get(2) == 4
    assert Lazy(lambda x, y: x + y).map(lambda x: x * 2).get(1, 2) == 6


# Generated at 2022-06-14 03:38:33.886845
# Unit test for method get of class Lazy
def test_Lazy_get():
    def fn() -> int:
        return 42

    assert Lazy(fn).get() == 42



# Generated at 2022-06-14 03:38:41.178402
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def apply_if_not_zero(value):
        def is_zero():
            return value == 0

        def apply():
            return value ** 3

        if is_zero():
            return Lazy.of(value)
        else:
            return Lazy.of(apply)

    assert Lazy.of(0).bind(apply_if_not_zero) == Lazy.of(0)
    assert Lazy.of(1).bind(apply_if_not_zero) == Lazy.of(1)

# Generated at 2022-06-14 03:38:44.886442
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    assert Lazy(lambda x: x + 1).map(lambda x: str(x)).__eq__(Lazy(lambda x: x + 1).map(lambda x: str(x)))



# Generated at 2022-06-14 03:38:48.216703
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    assert Lazy.of(1).bind(lambda x: Lazy.of(x+1)).get() == 2
    assert Lazy.of(2).bind(lambda x: Lazy.of(x+1)).get() == 3


# Generated at 2022-06-14 03:39:00.734945
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.box import Box
    from pymonet.either import Left, Right

    add = lambda x, y: x + y

    sum_with_one_branch = lambda x: Lazy.of(x).bind(lambda x: add(x, 1))
    sum_with_two_branch = lambda x: Lazy.of(x).bind(lambda x: add(x, 2))

    assert sum_with_one_branch(10).constructor_fn() == 11
    assert sum_with_one_branch(-1).constructor_fn() == 0
    assert sum_with_two_branch(10).constructor_fn() == 12
    assert sum_with_two_branch(-1).constructor_fn() == 1


# Generated at 2022-06-14 03:39:06.726527
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.list import List

    def list_transform(lst: List[int]) -> List[int]:
        """
        Transform List<Int> int List<Int>.

        :param lst: list to transform
        :type lst: List<Int>
        :returns: transformed List<Int>
        :rtype: List<Int>
        """
        return lst.map(lambda x: x + 1)

    assert Lazy.of(List.of(1, 2, 3, 4, 5)).bind(list_transform) == Lazy.of(List.of(2, 3, 4, 5, 6))



# Generated at 2022-06-14 03:39:11.970872
# Unit test for method get of class Lazy
def test_Lazy_get():
    function_called = False

    def function():
        nonlocal function_called
        function_called = True
        return 200

    lazy = Lazy(function)

    assert lazy.get() == 200
    assert function_called is True



# Generated at 2022-06-14 03:39:14.625913
# Unit test for method map of class Lazy
def test_Lazy_map():
    def f(x):
        return x * 2

    x = Lazy(f).map(f)(2)
    assert 8 == x



# Generated at 2022-06-14 03:39:23.172278
# Unit test for method get of class Lazy
def test_Lazy_get():
    counter = {'counter': 0}

    def increment_counter(counter):
        counter['counter'] += 1

    def inc():
        counter['counter'] += 1
        return 1

    def test_template(value):
        """
        We use list as mutable object to pass mutable counter to lazy functions,
        because only mutable objects passed to constructor of Lazy will be the same.
        """
        assert value is True
        assert counter['counter'] == 1

    lazy_true = Lazy(lambda: True)
    lazy_false = Lazy(lambda: False)
    assert lazy_true.get() is True
    assert lazy_false.get() is False
    assert lazy_true.get_or(False) is True
    assert lazy_false.get_or(True) is True
    assert lazy_true.get_or_call

# Generated at 2022-06-14 03:39:27.241109
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def some_fn(arg) -> 'Lazy[T, int]':
        return Lazy(lambda: arg)

    fn = Lazy(lambda: some_fn(1).get()).bind(some_fn)

    assert fn.constructor_fn() == 1



# Generated at 2022-06-14 03:39:28.631804
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.either import Right

    assert Lazy.of(lambda x: x + 1).ap(Right.of(2)).get() == 3

# Generated at 2022-06-14 03:39:30.646290
# Unit test for method get of class Lazy
def test_Lazy_get():
    def double(value):
        return value * 2

    lazy = Lazy(double)

    assert lazy.get(2) == 4
    assert lazy.get(2) == 4



# Generated at 2022-06-14 03:39:36.140112
# Unit test for method map of class Lazy
def test_Lazy_map():
    lazy_fn = lambda x: 2
    lazy = Lazy(lazy_fn)
    lazy2 = lazy.map(lambda x: x * 2)
    assert lazy2.constructor_fn() == 4

    lazy3 = Lazy(lambda x: 2).map(lambda x: x * 2)
    assert lazy3.constructor_fn() == 4


# Generated at 2022-06-14 03:39:39.316362
# Unit test for method get of class Lazy
def test_Lazy_get():
    lazy_value = 2

    lazy = Lazy.of(lazy_value)
    assert lazy.get() == lazy_value

# Generated at 2022-06-14 03:39:45.730409
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    from pymonet.box import Box
    from pymonet.custom_types import CustomType

    from pymonet.either import Right

    from pymonet.maybe import Maybe

    from pymonet.monad_try import Try

    from pymonet.validation import Validation

    lazy = Lazy(lambda: 666)

    assert lazy == lazy
    assert lazy == Lazy(lambda: 666)
    assert lazy != Lazy(lambda: 101)

    assert lazy != Box(666)
    assert lazy != CustomType('test')
    assert lazy != Right(666)
    assert lazy != Maybe.just(666)
    assert lazy != Try.of(lambda: 666)
    assert lazy != Validation.success(666)


# Generated at 2022-06-14 03:39:46.952656
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.validation import Validation
    validation = Validation.success(lambda a, b: a + b)
    assert Lazy.of(1).ap(validation).get(1) == 2

# Generated at 2022-06-14 03:39:51.348136
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def fn1(x):
        def inner(y):
            return x + y
        return Lazy(inner)

    lazy = Lazy(lambda x: x*2)
    result = lazy.bind(fn1)
    assert result.get(12) == 48

# Generated at 2022-06-14 03:39:54.862962
# Unit test for method bind of class Lazy
def test_Lazy_bind():  # pragma: no cover
    def add2(x):
        return Lazy.of(x + 2)

    lazy_result = Lazy.of(1).bind(add2)
    assert lazy_result.get() == 3



# Generated at 2022-06-14 03:39:58.717092
# Unit test for method get of class Lazy
def test_Lazy_get():
    def f(arg):
        return arg * 2

    l = Lazy(lambda arg: arg * 2)
    assert l.get(2) == 4
    assert l.get(2) == 4



# Generated at 2022-06-14 03:40:00.952890
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    assert Lazy.of(lambda x: x + 1).ap(Lazy.of(1)) == Lazy.of(2)


# Generated at 2022-06-14 03:40:04.063773
# Unit test for method get of class Lazy
def test_Lazy_get():
    def function(name):
        return name + ' lazy!'

    assert Lazy.of('lazy').get() == 'lazy'
    assert Lazy(function).get('hello') == 'hello lazy!'
    assert Lazy(function).get('hello') == 'hello lazy!'  # calling twice


# Generated at 2022-06-14 03:40:10.797058
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def add_100(x):
        return x + 100

    def mul_100(x):
        return x * 100

    lazy = Lazy(lambda: 100)
    assert isinstance(lazy.bind(lambda x: Lazy(lambda: x + 100)), Lazy)
    assert lazy.bind(lambda x: Lazy(lambda: x + 100)).get() == add_100(100)
    assert lazy.bind(lambda x: Lazy(lambda: x * 100)).get() == mul_100(100)



# Generated at 2022-06-14 03:40:14.174282
# Unit test for method get of class Lazy
def test_Lazy_get():
    def function(value):
        return value

    lazy = Lazy(function)

    assert lazy.get(0) == 0


# Generated at 2022-06-14 03:40:24.400783
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    lazy_int = Lazy(lambda x: x)
    lazy_str = Lazy(lambda x: str(x))

    assert lazy_int.ap(lazy_int) == lazy_int
    assert lazy_str.ap(lazy_str) == lazy_str

    lazy_str.ap(lazy_int).fold(
        lambda x: False,
        lambda x: True
    )

    assert lazy_str.ap(lazy_int).get(3) == lazy_str

    lazy_str.ap(lazy_int).get(3) == 3
    lazy_str.map(lambda x: x + '4').ap(lazy_int).get(3) == lazy_str

# Generated at 2022-06-14 03:40:34.620064
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    # pylint: disable=W0613
    def fn_A():
        return 1

    def fn_B():
        return 2

    lazy_a = Lazy(fn_A)
    lazy_b = Lazy(fn_B)

    assert lazy_a != lazy_b

    lazy_a.get()
    lazy_b.get()

    assert lazy_a == lazy_b

    assert Lazy(fn_A).get() == 1

# Generated at 2022-06-14 03:40:37.017282
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    assert (
           Lazy(lambda: 'girl').bind(lambda name: Lazy.of('Hello, ' + name))
           == Lazy.of('Hello, girl')
    )

# Generated at 2022-06-14 03:40:40.301219
# Unit test for method map of class Lazy
def test_Lazy_map():
    def constructor(x):
        return x

    def mapper(x):
        return x * 2

    assert Lazy(constructor).map(mapper).get(1) == 2



# Generated at 2022-06-14 03:40:42.666142
# Unit test for method get of class Lazy
def test_Lazy_get():
    """
    In this method we're testing fold computation
    """
    assert Lazy(lambda: True).get() is True

# Generated at 2022-06-14 03:40:45.923049
# Unit test for method get of class Lazy
def test_Lazy_get():  # pragma: no cover
    def fn(x):
        return x + 2

    f = Lazy(fn)
    assert f.get(2) == 4



# Generated at 2022-06-14 03:40:57.158336
# Unit test for method map of class Lazy
def test_Lazy_map():
    from pymonet.functor import Functor

    def test_function(x):
        return x + 1

    def mapper(x):
        return x + 2

    def another_mapper(x):
        return x + 3

    lazy = Lazy(test_function)
    lazy_functor = Functor(lazy)
    mapped_functor = lazy_functor.map(mapper)

    assert mapped_functor.get(20) == mapper(test_function(20))
    assert mapped_functor.get(20) == 25

    double_mapped_functor = mapped_functor.map(another_mapper)
    assert double_mapped_functor.get(20) == another_mapper(mapper(test_function(20)))

# Generated at 2022-06-14 03:41:00.577894
# Unit test for method map of class Lazy
def test_Lazy_map():
    assert Lazy.of(1).map(lambda x: x).get() == 1
    assert Lazy.of(2).map(lambda x: x + 2).get() == 4



# Generated at 2022-06-14 03:41:07.753550
# Unit test for method get of class Lazy
def test_Lazy_get():
    # given
    person_fn = lambda first_name, last_name: {"first_name": first_name, "last_name": last_name}

    lazy_person = Lazy(person_fn)

    # when
    # then
    assert lazy_person.get("John", "Doe") == {"first_name": "John", "last_name": "Doe"}
    assert lazy_person.is_evaluated is True
    assert lazy_person.value == {"first_name": "John", "last_name": "Doe"}



# Generated at 2022-06-14 03:41:13.529563
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def fn(x):
        return Lazy.of(x)

    test_fn = lambda x: Lazy.of(x)

    assert Lazy.of(1).bind(fn) == test_fn(1)



# Generated at 2022-06-14 03:41:20.459216
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.monad_try import Try

    def division(dividend, divisor):
        return Try.of(lambda: dividend / divisor)

    division_lazy = Lazy(division)
    division_lazy_mapper = division_lazy.map(lambda x: x * 3)

    division_lazy_mapper.ap(Lazy.of(1)).ap(Lazy.of(2)) == division_lazy_mapper.ap(Lazy.of(2)).ap(Lazy.of(1))
    assert division_lazy_mapper.ap(Lazy.of(1)).ap(Lazy.of(2)).get() == Try.of(lambda: 3 / 2)

# Generated at 2022-06-14 03:41:27.501914
# Unit test for method map of class Lazy
def test_Lazy_map():
    def fn(x):
        return x + 1

    lazy = Lazy.of(1)
    assert lazy == lazy.map(fn).map(lambda x: x + 1)

