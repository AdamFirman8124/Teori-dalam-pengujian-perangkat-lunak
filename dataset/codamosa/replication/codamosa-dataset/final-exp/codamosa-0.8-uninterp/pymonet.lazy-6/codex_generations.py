

# Generated at 2022-06-14 03:31:34.405267
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.validation import Validation

    def fn(a):
        def lambda_fn(a_1, a_2):
            return a + a_1 + a_2
        return Lazy(lambda_fn)

    assert Lazy.of(1).ap(Lazy.of((2, 3))).get() == 6

    assert Lazy.of(1).ap(Lazy.of((2, 3))).to_validation() == Validation.success(3)



# Generated at 2022-06-14 03:31:44.151168
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    def fn_add(x):
        return x + 1

    def fn_mul(x):
        return x * 2

    assert Lazy(fn_add) == Lazy(fn_add)
    assert Lazy(fn_add).map(fn_mul) == Lazy(fn_add).map(fn_mul)
    assert Lazy(fn_add) != Lazy(fn_mul)
    assert Lazy(fn_add).map(fn_mul) != Lazy(fn_mul).map(fn_add)



# Generated at 2022-06-14 03:31:46.995792
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    lazy = Lazy(lambda x: x)
    identity = lambda x: Lazy.of(x)

    assert lazy.bind(identity) == lazy.map(identity)

# Generated at 2022-06-14 03:31:50.952719
# Unit test for method bind of class Lazy
def test_Lazy_bind():  # pragma: no cover
    def fn_with_side_effects():
        print('function called')
        return 5

    lazy = Lazy(fn_with_side_effects).bind(lambda a: Lazy(lambda: a + 1))
    assert lazy.get() == 6


# Generated at 2022-06-14 03:32:00.898096
# Unit test for method ap of class Lazy
def test_Lazy_ap():  # pragma: no cover
    from pymonet.monad_functions import identity, square

    assert Lazy(identity).ap(Lazy.of(2)) == Lazy.of(2)
    assert Lazy(square).ap(Lazy.of(2)) == Lazy.of(4)
    assert Lazy(identity).ap(Lazy.of(2)).is_evaluated
    assert Lazy(square).ap(Lazy.of(2)).is_evaluated


# Generated at 2022-06-14 03:32:06.993859
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():  # pragma: no cover
    def fn(x):
        return x

    l1 = Lazy(fn)
    l2 = Lazy(fn)
    l3 = Lazy(fn)
    l4 = Lazy(fn)
    l5 = Lazy(lambda x: x + 1)

    l1.get(1)
    l2.get(1)
    l3.get(1)
    l4.get(2)
    l5.get(1)

    assert l1 == l2
    assert not (l1 == l3)
    assert not (l1 == l4)
    assert not (l1 == l5)



# Generated at 2022-06-14 03:32:13.771588
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():  # pragma: no cover
    def func_1():
        return 5

    def func_2():
        return 7

    lazy_1 = Lazy(func_1)
    lazy_1_copy = Lazy(func_1)
    lazy_2 = Lazy(func_2)

    assert lazy_1 == lazy_1_copy
    assert lazy_1 != lazy_2
    assert lazy_2 != lazy_1_copy

# Generated at 2022-06-14 03:32:24.330986
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    """Unit test for method bind of class Lazy"""

    lazy = Lazy.of(10)
    fn_1 = lambda arg: Lazy.of(arg * 2)
    fn_2 = lambda arg: Lazy.of(arg * 3)
    lazy_result_1 = lazy.bind(fn_1).bind(fn_2)
    assert lazy_result_1.get() == 60
    assert lazy_result_1.is_evaluated

    lazy_result_2 = lazy_result_1.bind(fn_2)
    assert lazy_result_2.get() == 180
    assert lazy_result_2.is_evaluated

    assert lazy_result_1 is lazy_result_2



# Generated at 2022-06-14 03:32:26.039789
# Unit test for method map of class Lazy
def test_Lazy_map():
    assert Lazy.of(1).map(lambda x: x + 1).get() == 2
    assert Lazy.of(1).map(lambda x: x + 1).to_maybe().get() == 2



# Generated at 2022-06-14 03:32:36.999998
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    from pymonet.monad_maybe import Maybe
    from pymonet.monad_try import Try
    from pymonet.monad_validation import Validation

    def foo():
        return 1

    def bar():
        return 'str'

    def baz():
        raise Exception('Exception')

    def qux():
        return None

    assert Lazy(foo) == Lazy(foo)
    assert Lazy(foo) != Lazy(bar)

    assert Lazy(foo) != Try.of(foo)
    assert Lazy(foo) != Maybe.just(1)
    assert Lazy(foo) != Validation.success(1)

    assert Lazy(bar) != Try.of(foo)
    assert Lazy(bar) != Maybe.just(1)

# Generated at 2022-06-14 03:32:43.451421
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    first_lazy = Lazy(lambda: 1)
    second_lazy = Lazy(lambda: 1)
    assert first_lazy == second_lazy
    first_lazy.get()
    assert first_lazy == second_lazy

# Generated at 2022-06-14 03:32:49.445961
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    """
    Unit test for __eq__ method of class Lazy.
    """
    fn = lambda x: x
    assert Lazy(fn) == Lazy(fn)

    assert not Lazy(fn) == Lazy(lambda *x: None)
    assert not Lazy(fn) == Lazy(fn).get(None)



# Generated at 2022-06-14 03:32:59.209465
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    import copy

    def div(a, b):
        return a / b

    def id_(val):
        return val

    f1 = Lazy(div).map(lambda x: x + 1)
    f2 = Lazy(id_).map(lambda x: x + 1)
    f3 = Lazy(div).map(lambda x: x + 1)
    f4 = f1

    assert f1 == f3
    assert f1 == f4
    assert f1 != f2
    assert f2 != f3
    assert f2 != f4
    assert f3 == f4

    assert f1.map(lambda x: x + 1) != f3
    assert f1.map(lambda x: x + 1) != f4

    f1 = f2 = f3 = f4 = None
    f1 = L

# Generated at 2022-06-14 03:33:10.693245
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    def compute_lazy_value():
        return UUID(1)

    def compute_mapped_value():
        return UUID(2)

    lambda_fn = Lazy(compute_lazy_value)
    lambda_fn_mapped = lambda_fn.map(lambda *args: compute_mapped_value())

    assert not lambda_fn == None
    assert not lambda_fn == 1
    assert not lambda_fn == lambda_fn_mapped
    assert lambda_fn == Lazy(compute_lazy_value)

    lambda_fn.get()
    lambda_fn_mapped.get()

    assert not lambda_fn == None
    assert not lambda_fn == 1
    assert not lambda_fn == lambda_fn_mapped
    assert lambda_fn == Lazy(compute_lazy_value)




# Generated at 2022-06-14 03:33:14.490730
# Unit test for method get of class Lazy
def test_Lazy_get():
    def square(x: int) -> int:
        return x ** 2

    assert Lazy.of(1).get() == 1
    assert Lazy.of(square).get()(2) == 4

# Generated at 2022-06-14 03:33:23.634039
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():

    def function(*args):
        return args

    def another_function(*args):
        return args

    def mapper(*args):
        return args

    def mapper_two(*args):
        return args

    lazy = Lazy(function)
    another_lazy = Lazy(another_function)

    assert lazy != another_lazy

    lazy = lazy.map(mapper)
    another_lazy = another_lazy.map(mapper_two)

    assert lazy != another_lazy

    assert lazy != '123'

    assert Lazy.of(1) == Lazy.of(1)
    assert Lazy.of(1) != Lazy.of('1')
    assert Lazy.of(1).map(lambda v: 1) == Lazy.of('1').map(lambda v: 1)


#

# Generated at 2022-06-14 03:33:26.323070
# Unit test for method map of class Lazy
def test_Lazy_map():
    def inp_fn() -> str:
        return 'input'

    def mapper_fn(value: str) -> str:
        return value + ' mapped'

    lazy = Lazy(inp_fn)
    assert lazy.map(mapper_fn).get() == 'input mapped'



# Generated at 2022-06-14 03:33:30.385968
# Unit test for method map of class Lazy
def test_Lazy_map():
    def fn():
        return 1

    assert Lazy(fn).map(lambda x: x + 1).get() == 2
    assert Lazy(fn).get() == 1


# Generated at 2022-06-14 03:33:35.101785
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from unittest import TestCase

    from pymonet.maybe import Maybe

    lazy = Lazy(lambda: Maybe.just(lambda x: x + 1))
    result = lazy.ap(Lazy.of(1))
    assert(result.get() == 2)

# Generated at 2022-06-14 03:33:38.985808
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    assert Lazy.of(1) == Lazy.of(1)
    assert Lazy.of(1) != Lazy.of(None)
    assert Lazy.of(1) != Lazy.of(2)
    assert Lazy.of(None) != Lazy.of(2)



# Generated at 2022-06-14 03:33:50.210229
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    f = Lazy(lambda x: x+1)
    assert f.bind(lambda x: Lazy(lambda: x)).get(1) == 2
    assert f.bind(lambda x: Lazy(lambda: x+x)).get(1) == 4
    assert f.bind(lambda x: Lazy(lambda: x+x)).get(2) == 5


# Generated at 2022-06-14 03:33:58.458876
# Unit test for method bind of class Lazy
def test_Lazy_bind():  # pragma: no cover
    def square(number):
        return number * number

    def empty_Lazy():
        return Lazy.of(None)

    def positive_Lazy(value):
        return Lazy.of(value)

    assert empty_Lazy().bind(square).constructor_fn() == None
    assert positive_Lazy(2).bind(square).constructor_fn() == 4
    assert positive_Lazy(2).bind(square).bind(square).constructor_fn() == 16

# Generated at 2022-06-14 03:34:07.191600
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():  # pragma: no cover
    assert Lazy(lambda x: x).__eq__(Lazy(lambda x: x))
    assert Lazy.of(1).__eq__(Lazy.of(1))
    assert not Lazy.of(1).__eq__(Lazy.of(2))
    assert not Lazy.of('a').__eq__(Lazy.of('b'))
    assert not Lazy(lambda x: x).__eq__(None)
    assert not Lazy.of(1).__eq__(None)


# Generated at 2022-06-14 03:34:18.944774
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from functools import reduce
    # Test bind with flatmapping
    def flatmapping_result(x, y):
        return x + y

    def flatmapping_function(x):
        return Lazy(lambda *args: x + 1)

    assert Lazy(lambda: 10).bind(flatmapping_function).get() == 11
    assert Lazy(lambda: 10).bind(flatmapping_function).bind(flatmapping_function).get() == 12
    assert type(Lazy(lambda: 10).bind(flatmapping_function).bind(flatmapping_function).bind(flatmapping_function)) == Lazy


# Generated at 2022-06-14 03:34:23.772217
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    # Given
    def fun_hello(x):
        return Lazy.of("Hello {}".format(x))

    # When
    # Then
    assert Lazy.of("World").bind(fun_hello).get() == "Hello World"



# Generated at 2022-06-14 03:34:32.652568
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    """
    :return: None
    """
    from pymonet.monad import Monad

    Monad.is_monad(Lazy)

    assert Lazy(lambda: 1).bind(lambda x: Lazy(lambda: x * 3)).get() == 3
    assert Lazy(lambda: 1).bind(lambda x: Lazy(lambda: x * 3)).get() == 3
    assert Lazy(lambda: 1).bind(lambda x: Lazy(lambda: x * 3)).get() == 3

    assert Lazy.of(1).bind(lambda x: Lazy(lambda: x * 3)).get() == 3
    assert Lazy.of(1).bind(lambda x: Lazy(lambda: x * 3)).get() == 3

# Generated at 2022-06-14 03:34:42.619816
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from typing import Any

    from pymonet.box import Box
    from pymonet.either import Left, Right
    from pymonet.maybe import Maybe
    from pymonet.monad_try import Failure

    def first(value: Any) -> Box[int]:
        return Box.of(value + 10)

    def second(value: Any) -> Box[int]:
        return Box.of(value - 10)

    def third(value):
        if value > 10:
            return Right(value)
        else:
            return Left(value)

    def fourth(value):
        if value > 5:
            return Maybe.just(value)
        return Maybe.empty()

    def fifth(value) -> Lazy[int, str]:
        return Lazy.of(lambda: str(value))


# Generated at 2022-06-14 03:34:54.144210
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def testee_function(arg1: int, arg2: str) -> str:
        return '{} {}'.format(arg1, arg2)

    lazy = Lazy(testee_function)
    bound_lazy = lazy.bind(lambda result: Lazy.of(result + '!!!'))

    assert bound_lazy.get(1, 'asda') == '1 asda!!!'

    def get_value_of_lazy(lazy: Lazy):
        return lazy.get(1, 'asda')

    lazy_evaluated_bound_lazy = Lazy.of(bound_lazy)

    assert get_value_of_lazy(lazy_evaluated_bound_lazy) == '1 asda!!!'



# Generated at 2022-06-14 03:35:00.920614
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():  # pragma: no cover
    def lazy_1():
        return 'lazy_1'

    def lazy_2():
        return 'lazy_2'

    assert Lazy(lazy_1) == Lazy(lazy_1)
    assert Lazy(lazy_1) != Lazy(lazy_2)

test_Lazy___eq__()

# Generated at 2022-06-14 03:35:06.881864
# Unit test for method map of class Lazy
def test_Lazy_map():
    from pymonet.functions import partial1
    from pymonet.box import Box
    from pymonet.either import Right

    def add(x):
        def inner_add(y):
            return x + y

        return inner_add

    def get_value(x):
        def get_value_fn(y):
            return y.get()

        return get_value_fn

    v = Lazy(partial1(add, 2))
    assert v.map(partial1(add, 3)).map(get_value(Box)) == Box(5)
    assert v.map(partial1(add, 3)).map(get_value(Right)) == Right(5)



# Generated at 2022-06-14 03:35:18.629649
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    def test_fn(*args):
        return args

    is_true_1 = Lazy(test_fn) == Lazy(test_fn)
    is_true_2 = Lazy(test_fn)(1, 2, 3) == Lazy(test_fn)(1, 2, 3)
    is_true_3 = Lazy(test_fn)(1, 2, 3) == Lazy(test_fn)(1, 2, 3)
    is_false = Lazy(test_fn) == Lazy(test_fn)(1, 2, 3)

    assert is_true_1
    assert is_true_2
    assert is_true_3
    assert not is_false

# Generated at 2022-06-14 03:35:29.982951
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.maybetype import Maybe

    def create_dict_from_long_key_name(key: str) -> dict:
        """
        :param key: key to find in dict
        :type key: String
        :return: dict with key as key
        :rtype: dict
        """
        return {key: 'value'}

    def get_value_from_dict(key: str, dict):
        """
        :param key: key to find in dict
        :type key: String
        :param dict: dict where to find key
        :type dict: dict
        :return: value from dict
        :rtype: Any
        """
        return dict[key]


# Generated at 2022-06-14 03:35:36.824410
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def build_lazy(value):
        return Lazy(lambda: value)
    assert build_lazy(1).bind(lambda x: build_lazy(x)) == build_lazy(1)
    assert build_lazy(1).bind(lambda x: build_lazy(x + 1)) == build_lazy(2)

# Generated at 2022-06-14 03:35:39.578684
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    assert (
        Lazy.of(lambda x: x + 1).ap(Lazy.of(2)) ==
        Lazy.of(3)
    )



# Generated at 2022-06-14 03:35:45.276217
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.validation import Validation

    lazy1 = Lazy(lambda a, b, c: a + b + c)
    lazy2 = Lazy(lambda a: a * 2)

    assert lazy1.ap(lazy2).get(1, 2, 3) == 12



# Generated at 2022-06-14 03:35:49.152672
# Unit test for method map of class Lazy
def test_Lazy_map():  # pragma: no cover
    import pytest

    assert Lazy(lambda: 1).map(lambda x: x + 3).get() == 4
    assert Lazy(lambda: None).map(lambda x: x + 3).get() is None
    with pytest.raises(TypeError):
        Lazy(lambda: None).map()


# Generated at 2022-06-14 03:36:01.529406
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    """Tests for bind method of Lazy class"""
    from pymonet.box import Box
    from pymonet.maybe import Maybe
    from pymonet.monad_try import Try

    def make_list(x):
        return Lazy(lambda: [x])

    assert Maybe.just(1).bind(make_list).bind(lambda x: Maybe.just(x[0])) == Maybe.just(1)

    assert Maybe.just(1).bind(make_list).bind(lambda x: Maybe.nothing()) == Maybe.nothing()

    assert Maybe.nothing().bind(make_list).bind(lambda x: Maybe.just(x[0])) == Maybe.nothing()

    assert Box(1).bind(make_list).bind(lambda x: Box(x[0])) == Box(1)


# Generated at 2022-06-14 03:36:11.877643
# Unit test for method ap of class Lazy
def test_Lazy_ap(): # pragma: no cover
    def plus(value):
        return lambda x: x + value

    plus_1 = Lazy.of(plus(1)).ap(Lazy.of(1))
    assert plus_1.get() == 2

    plus_100 = Lazy.of(plus(100)).ap(Lazy.of(23))
    assert plus_100.get() == 123

    plus_minus_1 = Lazy.of(plus(1)).ap(plus(100).ap(Lazy.of(22)))
    assert plus_minus_1.get() == 123

    assert Lazy.of(plus(100)).ap(Lazy.of(100)).get() == 200
    assert Lazy.of(plus(100)).ap(Lazy.of(100)).get() == 200



# Generated at 2022-06-14 03:36:19.228129
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    value = 'hello'

    def fn(value):
        return Lazy(lambda *args: value[::-1])

    def mapper(value):
        return value * 2

    assert Lazy.of(value).bind(fn).get() == 'olleh'
    assert Lazy.of(value).bind(fn).map(mapper).get() == 'olleholleh'


# Generated at 2022-06-14 03:36:25.678011
# Unit test for method map of class Lazy
def test_Lazy_map():
    """
    Test for map method of Lazy class
    """

    def f1(value):
        return value + 10

    # compute value with map method
    lazy_obj = Lazy(f1)
    lazy_obj_mapped = lazy_obj.map(lambda v: v + 10)
    assert lazy_obj_mapped.is_evaluated is False
    assert lazy_obj_mapped == Lazy(lambda v: f1(v) + 10)
    assert lazy_obj_mapped.get(10) == 30

    # check map function for correct work
    assert lazy_obj_mapped == lazy_obj.map(lambda v: v + 10)



# Generated at 2022-06-14 03:36:35.134097
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    def double(x):
        return Lazy.of(2.0 * x)

    assert Lazy.of(1.0).ap(double) == Lazy.of(2.0)
    assert Lazy.of(3.0).ap(double) == Lazy.of(6.0)
    assert Lazy.of(10.0).ap(double) == Lazy.of(20.0)


# Generated at 2022-06-14 03:36:43.774499
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.functor import Functor
    from pymonet.monad import Monad
    from pymonet.box import Box
    from pymonet.maybe import Maybe
    from pymonet.validation import Validation

    assert Functor[Lazy].map(Lazy.of(10).to_box(), lambda x: x, lambda x: Box.of(x)) == Box.of(10)
    assert Functor[Lazy].map(Lazy.of(10).to_maybe(), lambda x: x, lambda x: Maybe.just(x)) == Maybe.just(10)
    assert Functor[Lazy].map(Lazy.of(10).to_validation(), lambda x: x, lambda x: Validation.failure(x)) == Validation.failure(10)

    assert Monad[Lazy].bind

# Generated at 2022-06-14 03:36:45.738425
# Unit test for method map of class Lazy
def test_Lazy_map():
    assert Lazy.of(42).map(lambda x: x + 5).get() == 47



# Generated at 2022-06-14 03:36:56.675873
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.monad_try import Try
    from pymonet.list_like import List
    from pymonet.validation import Validation

    assert Lazy.of(5).ap(Lazy.of(lambda x: x + 1)).get() == 6
    assert Lazy.of(5).ap(Lazy.of(lambda x: x + 1)).ap(Lazy.of(lambda x: x * 2)).get() == 12
    assert Lazy.of(Try.of(lambda x: x + 1)).ap(Lazy.of(5)).get() == Try.of(6)
    assert Lazy.of(5).ap(Lazy.of(Try.of(lambda x: x + 1))).get() == Try.of(6)

# Generated at 2022-06-14 03:36:59.194584
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    # Lazy[Function([]) -> 5]
    lazy = Lazy(lambda: 5)
    # Lazy[Function(5) -> 5 * 2]
    result = lazy.bind(lambda x: Lazy(lambda: x * 2))

    assert result.get() == 10



# Generated at 2022-06-14 03:37:01.825681
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    assert Lazy.of(2).bind(lambda i: Lazy.of(i + 2)) == Lazy.of(4)

# Generated at 2022-06-14 03:37:12.378645
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.monad import fail, success
    from pymonet.monad_try import monad_try_sequence

    mock_error_handler = Lazy.of(lambda *args: 'handler')
    mock_value = Lazy.of('mock_value')

    mock_fn_arguments = (1, 2)

    def test_mock_right_fn(value):
        def mock_right_fn(*args):
            return success(value)

        return Lazy.of(mock_right_fn)

    def test_mock_left_fn(value):
        def mock_left_fn(*args):
            return fail(value)

        return Lazy.of(mock_left_fn)

    mock_lazy_right_fn = Lazy.of(test_mock_right_fn)

# Generated at 2022-06-14 03:37:19.770336
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.box import Box
    from pymonet.either import Left, Right
    from pymonet.maybe import Maybe
    from pymonet.monad_try import Try
    from pymonet.validation import Validation

    def fn1(*args):
        return Lazy.of(1)(*args)

    def fn2(*args):
        return Lazy.of(Right(1))(*args)

    def fn3(*args):
        return Lazy.of(1)

    assert Lazy.of(fn1).bind(fn1).get() == Lazy.of(1).get()
    assert Lazy.of(fn1).bind(fn2).get() == Box.of(1).get()
    assert Lazy.of(fn1).bind(fn3).get() == 1

# Generated at 2022-06-14 03:37:23.382102
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    assert Lazy(lambda a: a).bind(lambda a: Lazy.of(a + 1)).get(1) == 2
    assert Lazy(lambda a, b: a).bind(lambda a: Lazy.of(a + 1)).get(1, 2) == 2



# Generated at 2022-06-14 03:37:25.477600
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    assert Lazy(lambda: 3).bind(lambda x: Lazy(lambda: x + 5)).get() == 8
    assert Lazy(lambda: 3).bind(lambda x: Lazy(lambda: x + 5)).get() == 8
    assert Lazy(lambda: 3).bind(lambda x: Lazy(lambda: x + 5)).get() == 8



# Generated at 2022-06-14 03:37:33.601282
# Unit test for method map of class Lazy
def test_Lazy_map():
    lazy = Lazy(lambda: 1)

    assert lazy.map(lambda x: x + 1).get() == 2



# Generated at 2022-06-14 03:37:44.994406
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def f1(x):
        return Lazy(lambda n: n)

    def f2(x):
        return Lazy(lambda n: n*2)

    def f3(x):
        return Lazy(lambda n: n*3)

    lazy = Lazy(lambda: 1)
    assert lazy.bind(f1).bind(f2).bind(f3).get() == 6
    assert lazy.bind(f1).bind(f2).bind(f3).get() == 6
    assert lazy.bind(f1).bind(f2).bind(f3).get() == 6
    assert lazy.bind(f1).bind(f2).bind(f3).get() == 6
    assert lazy.bind(f1).bind(f2).bind(f3).get() == 6

# Generated at 2022-06-14 03:37:50.457714
# Unit test for method bind of class Lazy
def test_Lazy_bind():  # pragma: no cover
    def add(a):
        return Lazy(lambda b: a+b)

    lazy_1 = Lazy.of(1)
    lazy_2 = lazy_1.bind(add)
    assert lazy_2.get(2) == 3

    # bind is the only way to get Lazy value
    # its impossible to call fn in constructor
    assert lazy_1.get(2) == 1



# Generated at 2022-06-14 03:37:55.170289
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.validation import Validation

    def mapper(value):
        return Lazy.of(value * 2)

    def mapper_ap(value):
        return Lazy.of(value * 5)

    result = Lazy.of(2).ap(Lazy.of(mapper_ap))

    assert result == Lazy.of(20)

    result1 = Lazy.of(2).map(lambda x: x * 2).ap(Lazy.of(lambda x: x * 5))

    assert result1 == Lazy.of(20)

    result2 = Lazy.of(mapper).ap(Lazy.of(4))

    assert result2 == Lazy.of(8)

    result3 = Lazy.of(lambda x: x * 2).ap(Lazy.of(4))

   

# Generated at 2022-06-14 03:38:05.353006
# Unit test for method map of class Lazy
def test_Lazy_map():
    # Given
    x = Lazy(lambda: 1)
    y = Lazy(lambda: x)
    z = Lazy(lambda: 2)

    # Then
    assert x.map(lambda x: x + 1).get() == 2
    assert x.map(lambda x: z).get() == z
    assert x.map(lambda x: y).get() == Lazy(lambda: Lazy(lambda: 1))
    assert x.map(lambda x: x + 1).map(
        lambda n: n * n
    ).get() == 4

    assert y.map(lambda x: x + 1).get() == Lazy(lambda: 2)
    assert y.map(lambda x: z).get() == Lazy(lambda: z)

    assert z.map(lambda x: x + 1).get() == 3

# Generated at 2022-06-14 03:38:08.262624
# Unit test for method map of class Lazy
def test_Lazy_map():
    @Lazy
    def _sum(a, b):
        return a + b

    lazy_sum = _sum.map(lambda x: x + 1)
    assert lazy_sum.get(1, 2) == 4



# Generated at 2022-06-14 03:38:14.702245
# Unit test for method map of class Lazy
def test_Lazy_map():
    def divide_by_two(x: int) -> float:
        return x / 2

    def add_one(x: int) -> int:
        return x + 1

    lazy = Lazy.of(1)
    lazy_map = lazy.map(add_one).map(divide_by_two)

    assert lazy_map.get() == divide_by_two(add_one(lazy.get()))



# Generated at 2022-06-14 03:38:24.413996
# Unit test for method map of class Lazy
def test_Lazy_map():
    from hypothesis import given
    from hypothesis import strategies as st
    from pymonet.box import Box
    from pymonet.maybe import Maybe
    from pymonet.monad_try import Try
    from pymonet.either import Either
    from pymonet.validation import Validation

    @given(st.integers(), st.integers())
    def test_Lazy_map_Box(val1, val2):
        assert Lazy(lambda x: val1).map(lambda x: x + val2).get() == Box(val1).map(lambda x: x + val2).get()
        assert Lazy(lambda x: val1).map(lambda x: x + val2).to_box() == Box(val1).map(lambda x: x + val2)


# Generated at 2022-06-14 03:38:28.263047
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.maybe import Maybe

    def add(a, b):
        return Maybe.just(a + b)

    def mult(a, b):
        return Maybe.just(a * b)

    add_lazy = Lazy(add)
    mult_lazy = Lazy(mult)

    assert mult_lazy.ap(add_lazy.ap(Lazy.of(2).ap(Lazy.of(3)))).get() == 8

# Generated at 2022-06-14 03:38:39.919481
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    def identity(x):
        return x

    def double(x):
        return 2 * x

    def triple(x):
        return 3 * x

    def add(x, y):
        return x + y

    def add_two_arg(x, y):
        return (x + y, x + y, x + y)

    def add_three_arg(x, y, z):
        return (x + y + z, x + y + z, x + y + z)

    def some_function():
        return 'value'

    def some_function_with_argument(arg):
        return arg

    def some_function_with_multi_arguments(arg1, arg2, arg3):
        return (arg1, arg2, arg3)

    assert Lazy(identity) == Lazy(identity)

# Generated at 2022-06-14 03:38:54.671877
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    x = 2
    y = 3
    z = 5
    lazy_z = Lazy(lambda: z)
    assert lazy_z.bind(lambda z: Lazy(lambda: x + y + z)).get() == 10
    assert lazy_z.bind(lambda z: Lazy(lambda: x + y + z)).is_evaluated is True



# Generated at 2022-06-14 03:39:01.731388
# Unit test for method map of class Lazy
def test_Lazy_map():
    from pymonet.box import Box

    def add_one(x):
        return x + 1

    def get_box_value(box):
        return box.get()

    lazy_box = Lazy(lambda: Box(1))
    assert lazy_box.map(get_box_value).constructor_fn() == 1
    assert lazy_box.map(get_box_value).map(add_one).constructor_fn() == 2
    assert lazy_box.map(add_one).constructor_fn() == Box(2)
    assert lazy_box.map(get_box_value).constructor_fn() == Box(1)

# Unit test method ap of class Lazy

# Generated at 2022-06-14 03:39:10.797013
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    def double(x):
        return x * 2

    double_lazy = Lazy(double)
    double_lazy_value = Lazy(double)
    double_lazy.get(1)
    double_lazy_value.get(1)

    triple_lazy = Lazy(lambda x: x * 3)
    triple_lazy_value = Lazy(lambda x: x * 3)
    triple_lazy.get(1)
    triple_lazy_value.get(1)

    assert double_lazy == double_lazy
    assert double_lazy != triple_lazy
    assert double_lazy == double_lazy_value
    assert double_lazy != triple_lazy_value
    assert triple_lazy == triple_lazy
    assert triple_lazy != double_lazy


# Generated at 2022-06-14 03:39:24.183763
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    def f(): pass

    def g(): pass

    def h(): pass

    def i(): pass

    def j(): pass

    lazy = Lazy(f)
    lazy1 = Lazy(g)
    lazy2 = Lazy(h)
    lazy3 = Lazy(i)
    lazy4 = Lazy(j)

    lazy.get()
    lazy1.get()
    lazy2.get()

    assert lazy.__eq__(lazy1) == False
    assert lazy.__eq__(lazy2) == False
    assert lazy1.__eq__(lazy2) == False
    assert lazy2.__eq__(lazy3) == False
    assert lazy3.__eq__(lazy4) == False

    lazy1.constructor_fn = f

# Generated at 2022-06-14 03:39:28.712169
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    def add(a):
        return a + 5

    def add_10(a):
        return a + 10

    lazy_add = Lazy(add)
    lazy_add_10 = Lazy(add_10)
    assert lazy_add_10.ap(lazy_add).get(5) == 20

# Generated at 2022-06-14 03:39:30.233257
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    assert Lazy.of(3) == Lazy.of(3)



# Generated at 2022-06-14 03:39:37.717431
# Unit test for method bind of class Lazy
def test_Lazy_bind():  # pragma: no cover
    def test_lazy_fn(a):
        return a

    def test_mapper(a):
        return Lazy(lambda b: b * 2)

    test_lazy = Lazy(test_lazy_fn)
    lazy = test_lazy.bind(test_mapper)
    assert lazy.get(1) == 2
    assert lazy.get(2) == 4
    assert lazy.get(3) == 6
    assert lazy.get(2) == 4
    assert lazy.get(3) == 6

# Generated at 2022-06-14 03:39:40.635058
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    # Lazy[int, int]
    result = Lazy.of(3).ap(Lazy.of(lambda x: x + 1))
    assert result.get() == 4



# Generated at 2022-06-14 03:39:44.420119
# Unit test for method map of class Lazy
def test_Lazy_map():
    # Arrange
    from pymonet.maybe import Maybe

    # Act
    result = Lazy.of(1).map(Maybe.just)

    # Assert
    assert(result.get() == Maybe.just(1))



# Generated at 2022-06-14 03:39:55.402853
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    def square(value):
        return value * value

    def wrapped_square(value):
        return Lazy.of(square(value))

    fn = Lazy.of(lambda x, y: x * 2 + y)
    ap = fn.ap(Lazy.of(5))

    assert assert_that(ap.get(3)).is_equal_to(13)
    assert assert_that(ap.get(3)).is_equal_to(13)
    assert assert_that(ap.get(4)).is_equal_to(14)
    assert assert_that(ap.get(4)).is_equal_to(14)
    assert assert_that(ap.map(square).get(4)).is_equal_to(196)
    assert assert_that(ap.map(square).get(4)).is_equal_to

# Generated at 2022-06-14 03:40:17.748304
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    assert Lazy.of(1).ap(Lazy.of(lambda x: x + 1)) == Lazy.of(2)

    def test_fn(x):
        return Lazy.of(x + 1)

    assert Lazy.of(1).ap(Lazy.of(test_fn)) == Lazy.of(2)



# Generated at 2022-06-14 03:40:23.209910
# Unit test for method bind of class Lazy
def test_Lazy_bind():  # pragma: no cover
    from pymonet.validation import Validation

    lazy_fn = Lazy.of(5)

    def lazy_mapper(i):
        return Lazy.of(i + 1)

    assert lazy_fn.bind(lazy_mapper).get() == 6

# Generated at 2022-06-14 03:40:31.025295
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.either import Right
    from pymonet.monad_try import Try
    from pymonet.validation import Validation

    assert Lazy.of(1).ap(Lazy.of(lambda a: a + 2)).get() == 3
    assert Lazy.of(1).ap(Lazy.of(lambda: 2)).get() == 2
    assert Lazy.of(1).ap(Right.of(lambda a: a + 2)).get() == 3
    assert Lazy.of(1).ap(Try.of(lambda a: a + 2)).get() == 3
    assert Lazy.of(1).ap(Validation.success(lambda a: a + 2)).get() == 3



# Generated at 2022-06-14 03:40:35.513765
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def add(x: int) -> Lazy[int, int]:
        return Lazy(lambda y: x + y)

    lazy_x = Lazy(lambda: 1)

    assert lazy_x.bind(add).get(2) == 3

# Generated at 2022-06-14 03:40:39.861575
# Unit test for method map of class Lazy
def test_Lazy_map():
    def test_function(value):
        return value

    result = Lazy(test_function).map(lambda x: x.upper()).get('a')
    assert result == 'A'



# Generated at 2022-06-14 03:40:47.602388
# Unit test for method map of class Lazy
def test_Lazy_map():
    from pymonet.box import Box
    from pymonet.maybe import Maybe

    def is_even(n: int) -> bool:
        return n % 2 == 0

    def add_one(n: int) -> int:
        return n + 1

    lazy_box_even = Lazy.of(2).to_box() \
        .map(lambda n: n + 1) \
        .map(lambda n: n * 2) \
        .map(lambda n: n / 2) \
        .map(is_even) \
        .map(lambda is_even: 'even' if is_even else 'odd')
    assert lazy_box_even.get() == 'even'


# Generated at 2022-06-14 03:40:53.296449
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    """
    Test for method bind of class Lazy
    """
    assert Lazy(lambda x: x + 1).bind(lambda x: Lazy(lambda: x * 2)).get(3) == 8
    assert Lazy(lambda x: x + 1).bind(lambda x: Lazy(lambda: x * 2)).constructor_fn == (lambda x: 8)


# Generated at 2022-06-14 03:41:04.411228
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.maybe import Maybe
    from pymonet.box import Box
    from pymonet.f import F

    assert Lazy.of('def').ap(Maybe.just(F.add('abc'))) == Lazy.of('abcdef')
    assert Lazy.of(None).ap(Maybe.just(F.add('abc'))) == Lazy.of(None)
    assert Box(Box(Box(Lazy.of(F.add(1))).get()).get()).get() == Box(Box(Box(Lazy.of(F.add(1))).get()).get()).get()

# Generated at 2022-06-14 03:41:11.005573
# Unit test for method bind of class Lazy
def test_Lazy_bind():  # pragma: no cover
    lazy1 = Lazy(lambda n: n + 1)
    lazy2 = Lazy(lambda n: n * 2)

    assert lazy1.bind(
        lambda n: lazy2.map(
            lambda m: n + m
        )
    ).get(10) == 22

    # Test if mapper is called only during calling fold method
    lazy_mapper = Lazy(lambda n: n + 3)

    def lazy_mapper_get(*args):
        return lazy_mapper.get(*args)

    x = lazy2.bind(
        lambda n: lazy1.map(
            lazy_mapper_get
        )
    )
    assert lazy_mapper.is_evaluated is False
    assert x.get(10) == 26
    assert lazy_mapper.is_evaluated

# Generated at 2022-06-14 03:41:19.756935
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    assert Lazy.of(lambda x: x * 2).ap(Lazy.of(3)) == Lazy.of(6)
    assert Lazy.of(lambda x: x * 2).ap(Lazy.of(None)) == Lazy.of(None)
    assert Lazy.of(lambda x, y: x * y).ap(Lazy.of(4)).ap(Lazy.of(5)) == Lazy.of(20)
    assert Lazy.of(lambda x, y, z: x * y * z).ap(Lazy.of(4)).ap(Lazy.of(5)).ap(Lazy.of(8)) == Lazy.of(160)
    assert Lazy.of(lambda x, y: x * y).ap(Lazy.of(4)).ap(Lazy.of(None)) == L