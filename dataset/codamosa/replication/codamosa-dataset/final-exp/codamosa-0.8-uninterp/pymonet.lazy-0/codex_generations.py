

# Generated at 2022-06-14 03:31:32.080196
# Unit test for method map of class Lazy
def test_Lazy_map():
    assert Lazy(lambda: 2).map(lambda a: a + 1).map(lambda a: a + 1).map(lambda a: a + 1) == Lazy(lambda : 4)



# Generated at 2022-06-14 03:31:39.534105
# Unit test for method get of class Lazy
def test_Lazy_get():
    data = [
        (Lazy(lambda x: x + 1).get(1), 2),
        (Lazy(lambda x, y: x + y).get(1, 2), 3)
    ]
    for (result, expected) in data:
        assert result == expected, 'ERROR: Lazy get function return wrong value. \n \t Expected: {}, \n \t returned: {}'\
            .format(expected, result)



# Generated at 2022-06-14 03:31:44.587688
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    """Test ap method of Lazy class"""
    from pymonet.function import Function

    assert Lazy(lambda x: x + 3).ap(Lazy.of(Function.of(lambda x: x + 4))) == Lazy.of(7)


# Generated at 2022-06-14 03:31:46.848879
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.predicate import is_positive

    assert Lazy(lambda x: x + 1).bind(is_positive).get(1) is True

# Generated at 2022-06-14 03:31:50.826203
# Unit test for method bind of class Lazy
def test_Lazy_bind():  # pragma: no cover
    def fn(value):
        def new_lazy():
            return value + 1

        return Lazy(new_lazy)

    lazy = Lazy(lambda: 1)
    lazy = lazy.bind(fn)
    assert lazy.get() == 2



# Generated at 2022-06-14 03:32:02.913030
# Unit test for method map of class Lazy
def test_Lazy_map():
    def my_function(arg):
        return arg + 1

    assert Lazy(my_function).map(my_function) == Lazy(my_function).map(my_function)

    assert Lazy(my_function).map(my_function).map(my_function).map(my_function) == Lazy(my_function).map(lambda x: x + 3)

    assert Lazy(my_function).map(lambda x: x + 1).map(lambda x: x + 2).map(lambda x: x + 3).get(5) == 10

    assert Lazy(my_function).map(my_function).map(my_function).map(my_function).get(5) == 10



# Generated at 2022-06-14 03:32:05.208240
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    def constructor_fn():  # pragma: no cover
        pass

    def mapper():  # pragma: no cover
        pass

    lazy = Lazy(constructor_fn)
    lazy.map(mapper)

    lazy2 = lazy

    assert lazy == lazy2
    assert lazy != 1



# Generated at 2022-06-14 03:32:09.112532
# Unit test for method map of class Lazy
def test_Lazy_map():  # pragma: no cover
    import functools

    assert Lazy.of(5).map(lambda x: x + 10).get() == 15
    assert Lazy.of(5).map(lambda x: x + 10).get() == 15
    assert Lazy.of(5).map(lambda x: x + 10).get() == 15

    def add10(x):
        return x + 10

    assert Lazy.of(5).map(add10).get() == 15
    assert Lazy.of(3).map(functools.partial(add10, x=10)).get() == 23

    assert Lazy.of('a').map(lambda x: x + 'b').get() == 'ab'

# Generated at 2022-06-14 03:32:18.928403
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():

    assert Lazy.of(1).get() == Lazy.of(1).get()
    assert Lazy.of('a').get() == Lazy.of('a').get()
    assert Lazy.of([1, 2, 3]).get() == Lazy.of([1, 2, 3]).get()
    assert Lazy.of(1) != Lazy.of('a').get()
    assert Lazy.of(1) != Lazy.of([1, 2, 3]).get()
    assert Lazy.of(1) != Lazy.of([1, 2, 3])
    assert Lazy.of(1) != Lazy.of(1)

    def value_concat():
        return 'value'

    assert Lazy(value_concat) != Lazy(value_concat)

# Generated at 2022-06-14 03:32:24.881211
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    from pymonet.monad_try import Try

    assert Lazy(lambda x: x) == Lazy(lambda x: x)
    assert Lazy(lambda x: x) != Lazy(lambda y: y)
    assert Lazy(lambda x: x) != Try.of(lambda x: x)


# Generated at 2022-06-14 03:32:37.666925
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    assert Lazy.of(1) == Lazy.of(1)
    assert Lazy.of(1) != Lazy.of(2)
    assert Lazy.of(1) != Lazy.of(None)
    assert Lazy.of(None) != Lazy.of(1)

    assert Lazy(lambda: 1) != Lazy.of(1)
    assert Lazy(lambda: 1) != Lazy(lambda: 1)

    assert Lazy(lambda: 1).map(lambda v: v + 1) != Lazy.of(1).map(lambda v: v + 1)
    assert Lazy(lambda: 1).map(lambda v: v + 1) != Lazy(lambda: 1).map(lambda v: v + 1)


# Generated at 2022-06-14 03:32:43.522781
# Unit test for method map of class Lazy
def test_Lazy_map():
    def fn(*args):
        return tuple(args)

    assert Lazy(fn).map(lambda x: x).constructor_fn() == ()
    assert Lazy(fn).map(lambda x: x).constructor_fn(1, 2, 3) == (1, 2, 3)
    assert Lazy(fn).map(lambda x: x).constructor_fn(1) == (1,)
    assert Lazy(fn).map(lambda x: x).constructor_fn(1, 2, 3) == (1, 2, 3)



# Generated at 2022-06-14 03:32:55.346649
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():  # pragma: no cover
    """
    Test for Lazy class
    """
    assert Lazy.of(1) != Lazy.of(1)
    assert Lazy.of(1) == Lazy.of(1)
    assert Lazy.of(2) != Lazy.of(1)
    assert Lazy.of(lambda x: x + 1) != Lazy.of(lambda x: x)
    assert Lazy.of(lambda x: x) != Lazy.of(lambda x: x)
    assert Lazy.of(lambda x: x)(1) == Lazy.of(lambda x: x)(1)
    assert Lazy.of(lambda x: x + 1)(1) != Lazy.of(lambda x: x)(1)

    def fn1(x):
        return x


# Generated at 2022-06-14 03:33:03.759217
# Unit test for method bind of class Lazy
def test_Lazy_bind():  # pragma: no cover
    add_number = lambda x: x + 1
    double_number = lambda x: x * 2
    compare_number = lambda x: x == 2
    builder = Lazy(lambda: 1)
    assert builder.bind(add_number)\
                  .bind(double_number)\
                  .bind(compare_number)\
                  .get() == True

    builder = Lazy(lambda: 1)
    assert builder.bind(add_number)\
                  .bind(compare_number)\
                  .bind(double_number)\
                  .get() == False



# Generated at 2022-06-14 03:33:09.526194
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    """
    Test that if we bind function to Lazy it will be called with stored value during
    calling fold method, and result of folder will be stored in Lazy.
    """
    from pymonet.box import Box

    lazy = Lazy(lambda a: a + '0')
    lazy2 = lazy.bind(lambda a: Box(a + '1'))
    assert lazy2.get('3') == Box('30').put('1')


# Generated at 2022-06-14 03:33:20.202276
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():  # pragma: no cover
    assert Lazy.of(1).__eq__(Lazy.of(1))
    assert Lazy.of(1).__eq__(Lazy.of(1).get())
    assert not Lazy.of(1).__eq__(Lazy.of(2))
    assert not Lazy.of(1).__eq__(Lazy.of('a'))
    assert not Lazy.of(1).__eq__(None)
    assert not Lazy.of(1).__eq__('a')
    assert not Lazy.of(1).__eq__(1)
    assert not Lazy.of(1).__eq__(Lazy.of(1).to_box())
    assert not Lazy.of(1).__eq__(Lazy.of(1).to_either())


# Generated at 2022-06-14 03:33:26.419961
# Unit test for method map of class Lazy
def test_Lazy_map():
    def return_arg(arg):
        return arg

    def times_2(arg):
        return arg * 2

    lazy = Lazy.of(5)
    result_1 = lazy.map(return_arg)
    assert result_1.get() == 5

    result_2 = lazy.map(times_2)
    assert result_2.get() == 10

    result_3 = lazy.map(times_2).map(times_2).map(times_2)
    assert result_3.get() == 40

    fn = lambda x: x*2
    result_4 = lazy.map(fn).get()
    assert result_4 == 10



# Generated at 2022-06-14 03:33:29.751558
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    lazy = Lazy.of(2).bind(lambda a: Lazy.of(a+5))
    assert lazy.get() == 7

# Generated at 2022-06-14 03:33:40.188874
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    from pymonet.functor import Functor
    from pymonet.monad import Monad
    from pymonet.applicative import Applicative

    def lazy_eq(lazy1, lazy2, eq_fn):
        lazy1_monad = Monad.to_monad(lazy1)
        lazy2_monad = Monad.to_monad(lazy2)
        eq_monad = Monad.to_monad(eq_fn)
        lazy1_applicative_monad = Applicative.to_applicative(lazy1_monad)
        lazy2_applicative_monad = Applicative.to_applicative(lazy2_monad)
        eq_applicative_monad = Applicative.to_applicative(eq_monad)

        return lazy1

# Generated at 2022-06-14 03:33:41.742406
# Unit test for method get of class Lazy
def test_Lazy_get():
    assert Lazy.of(42).get() == 42



# Generated at 2022-06-14 03:33:48.316581
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def add(x):
        return x + 1

    def add_lazy(x):
        return Lazy(lambda *args: add(x))

    result = Lazy(lambda: 1).bind(add_lazy)
    expected = Lazy(lambda: 2)

    assert result == expected



# Generated at 2022-06-14 03:34:00.732125
# Unit test for method bind of class Lazy
def test_Lazy_bind():  # pragma: no cover
    def fn_lazy1(a):
        def fn_lazy2(b):
            return a + b

        return Lazy(fn_lazy2)

    lazy1 = Lazy(lambda a: a + 1)
    lazy2 = lazy1.bind(fn_lazy1)
    assert lazy2.get(1) == 3

    print(lazy2.get(1))
    assert lazy2.__eq__(lazy2.get(1))
    assert Lazy(fn_lazy1(1)).__eq__(lazy2.get(1))
    assert lazy2.get(2) == 5

    print(lazy1)  # Lazy[fn=<function <lambda> at 0x0000026E49B6B0D0>, value=None, is_evaluated

# Generated at 2022-06-14 03:34:10.575739
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    class A:
        a = 10

        def __eq__(self, other):
            return isinstance(other, A) and self.a == other.a

    f1 = lambda: A()
    lazy1 = Lazy(f1)
    lazy2 = Lazy(f1)
    assert lazy1 == lazy2

    lazy1.get()
    lazy2.get()
    assert lazy1 == lazy2

    f2 = lambda: A()
    lazy1 = Lazy(f2)
    lazy2 = Lazy(f2)
    assert lazy1 == lazy2

    lazy1.get()
    lazy2.get()
    assert lazy1 == lazy2

# Generated at 2022-06-14 03:34:21.483286
# Unit test for method map of class Lazy
def test_Lazy_map():  # type: () -> None
    """
    Unit test for method map of class Lazy
    """
    def add(x: int, y: int) -> int:
        return x + y

    def add_one(x: int) -> int:
        return x + 1

    lazy_function = Lazy(lambda: add(1, 1))
    result = lazy_function.map(add_one)
    assert result.get() == 3, 'result should be 3'

    lazy_function = Lazy(lambda: add(1, 1))
    result = lazy_function.map(add_one).map(add_one)
    assert result.get() == 4, 'result should be 4'

    lazy_function = Lazy(lambda: add(1, 1))
    result = lazy_function.map(add_one)
    result

# Generated at 2022-06-14 03:34:27.814913
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    assert Lazy.of(5) == Lazy.of(5)
    assert Lazy.of(5) != Lazy.of(6)
    assert Lazy(lambda x: x + 2) != Lazy.of(54)
    assert Lazy.of(None) != None
    assert Lazy.of(None) != Lazy.of(None)
    assert Lazy.of(None) == Lazy.of(None)


# Generated at 2022-06-14 03:34:31.564563
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.maybe import Maybe

    a = Lazy.of(Maybe.just(1))
    b = a.bind(lambda m: m.map(lambda x: x + 1))
    c = b.get()

    assert isinstance(c, Maybe)

    assert c.is_present
    assert c.get() == 2

# Generated at 2022-06-14 03:34:42.221890
# Unit test for method map of class Lazy
def test_Lazy_map():
    from pymonet.box import Box
    from pymonet.either import Left, Right
    from pymonet.maybe import Maybe
    from pymonet.monad_try import Failure
    from pymonet.validation import Invalid, Valid

    print('Test method map of class Lazy')

    fn = lambda x: '{}-{}'.format(x, x)
    assert Lazy(fn).map(lambda x: x.upper()).get('Mr') == 'MR-MR'

    assert Lazy(fn).map(lambda x: Box(x.upper())).get('Mr').get() == 'MR-MR'
    assert Lazy(fn).map(lambda x: Left(x.upper())).get('Mr') == Left('MR-MR')

# Generated at 2022-06-14 03:34:49.224901
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():  # pragma: no cover
    from nose.tools import assert_equal

    assert_equal(True, Lazy(lambda arg: arg) == Lazy(lambda arg: arg))
    assert_equal(False, Lazy(lambda arg: arg) == Lazy(lambda arg: arg + 1))
    assert_equal(False, Lazy(lambda arg: arg) == 42)



# Generated at 2022-06-14 03:34:54.302525
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():  # pragma: no cover
    from unittest import TestCase, main

    from pymonet.maybe import Maybe

    class _TestLazy(TestCase):
        def test_eq_empty_lazies(self):
            lazy_1 = Lazy(lambda: 1)
            lazy_2 = Lazy(lambda: 1)

            self.assertEqual(lazy_1, lazy_2)

        def test_eq_uncertain_lazies(self):
            lazy_1 = Lazy(lambda: 1)
            lazy_2 = Lazy(lambda: 1)

            lazy_1.get()
            lazy_2.get()

            self.assertEqual(lazy_1, lazy_2)


# Generated at 2022-06-14 03:34:59.561373
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def function_in_Lazy(*args):
        return "Lazy with function"

    l = Lazy(function_in_Lazy).bind(lambda x: Lazy.of("New value"))
    assert l.get() == "New value"



# Generated at 2022-06-14 03:35:06.389829
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():

    def first_fn(value):
        import random
        return value + random.randint(0, 100)

    def second_fn(value):
        import random
        return value + random.randint(0, 100)

    first_lazy = Lazy(first_fn)
    second_lazy = Lazy(second_fn)
    assert first_lazy == second_lazy
    assert first_lazy.get(5) != second_lazy.get(5)



# Generated at 2022-06-14 03:35:10.899185
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def constructor_fn():
        return 42

    lazy = Lazy(constructor_fn)

    def fn(x):
        return Lazy.of(x + 1)

    result = lazy.bind(fn)

    assert result.get() == 43


# Generated at 2022-06-14 03:35:13.767255
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    assert Lazy.of(lambda x: x + 1).ap(Lazy.of(2)) == Lazy(lambda *args: 3)

# Generated at 2022-06-14 03:35:21.747320
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def add_two(num: int) -> Lazy[int, int]:
        return Lazy.of(num + 2)

    def add_two_and_multiply(num: int) -> Lazy[int, int]:
        return Lazy.of(num + 2).map(lambda x: x * 2)

    assert Lazy.of(1).bind(add_two).get() == 3
    assert Lazy.of(1).bind(add_two).bind(add_two_and_multiply).get() == 10

# Generated at 2022-06-14 03:35:30.282051
# Unit test for method map of class Lazy
def test_Lazy_map():
    def square_and_add_1(x):
        return x * x + 1

    def add_1(x):
        return x + 1

    lazy_fn_one = Lazy(lambda: 1)
    assert lazy_fn_one.map(square_and_add_1).get() == 2
    assert lazy_fn_one.map(add_1).get() == 2

    lazy_add_1_5 = Lazy(lambda: 5)
    assert lazy_add_1_5.map(square_and_add_1).get() == 26
    assert lazy_add_1_5.map(add_1).get() == 6

    lazy_fn_two = Lazy(lambda: 2)
    assert lazy_fn_two.map(square_and_add_1).get() == 5
    assert lazy_fn

# Generated at 2022-06-14 03:35:32.866812
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.box import Box

    assert Lazy.of(5).bind(lambda n: Lazy.of(Box.of(n))).get() == Box.of(5)

# Generated at 2022-06-14 03:35:41.005783
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.monad_try import Try, Error
    from pymonet.validation import Validation, validation_passed, validation_failed
    from pymonet.monad_list import List

    def get_lazy(a):
        def fn(b):
            if a:
                return Lazy.of(b)
            raise ValueError('a is False')
        return fn

    def get_try(a):
        def fn(b):
            if a:
                return Try.of(lambda: b)
            else:
                return Try.error(Error('a is False'))
        return fn

    def get_validation(a):
        def fn(b):
            if a:
                return Validation.success(b)
            else:
                return Validation.error(b)
        return fn



# Generated at 2022-06-14 03:35:50.520930
# Unit test for method map of class Lazy
def test_Lazy_map():
    from pymonet.box import Box
    from pymonet.either import Right
    from pymonet.maybe import Just
    from pymonet.monad_try import Try
    from pymonet.validation import Validation

    def map_try(value):
        return Try(lambda: value + value)

    def map_maybe(value):
        return Just(value + value)

    def map_validation(value):
        return Validation.success(value)

    def map_right(value):
        return Right(value + value)

    def map_box(value):
        return Box(value + value)

    lazy = Lazy.of(2)
    assert lazy.map(lambda value: value + value).get() == 4
    assert lazy.map(lambda value: value + value).to_box().get() == 4

# Generated at 2022-06-14 03:36:02.242449
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.monad_try import Try

    def function_to_bind(n: int) -> Lazy:
        return Lazy(lambda: n)

    output = Lazy.of(2).bind(function_to_bind).to_maybe().bind(function_to_bind).bind(function_to_bind).get()
    assert output == 2

    output = Lazy.of(2).bind(function_to_bind).bind(function_to_bind).bind(function_to_bind).to_maybe().get()
    assert output == 2

    output = Lazy.of(2).bind(function_to_bind).to_maybe().bind(function_to_bind).bind(function_to_bind).get()
    assert output == 2


# Generated at 2022-06-14 03:36:05.207602
# Unit test for method get of class Lazy
def test_Lazy_get():
    import pytest

    lazy = Lazy(lambda *args: 'bar')
    assert(lazy.get() == 'bar')


# Generated at 2022-06-14 03:36:14.370999
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.maybe import Maybe

    lazy = Lazy.of(4)
    assert lazy.bind(lambda x: Lazy.of(x + 3)).get() == 7
    assert lazy.bind(lambda x: Maybe.nothing()).to_maybe().is_nothing()



# Generated at 2022-06-14 03:36:24.426429
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    assert Lazy.of(1).bind(lambda x: Lazy.of(x + 1)).get() == 2
    assert Lazy.of(1).bind(lambda x: Lazy.of(x + 1)).bind(lambda x: Lazy.of(x + 1)).get() == 3
    assert Lazy.of(1).bind(lambda x: Lazy.of(x + 1)).bind(lambda x: Lazy.of(x + 1)).bind(lambda x: Lazy.of(x + 1)).get() == 4
    assert Lazy.of(1).bind(lambda x: Lazy.of(x + 1)).map(lambda x: x * 3).get() == 6

# Generated at 2022-06-14 03:36:36.654062
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():

    class TestException(Exception):
        pass

    def test_fn_not_raises():
        return 'S'

    def test_fn_raises():
        raise TestException()

    test_fn_1 = lambda: test_fn_not_raises()
    test_fn_2 = lambda: test_fn_not_raises()
    test_fn_3 = lambda: test_fn_raises()

    lazy_1 = Lazy(test_fn_1)
    lazy_2 = Lazy(test_fn_2)
    lazy_3 = Lazy(test_fn_1)
    lazy_4 = Lazy(test_fn_3)
    lazy_5 = Lazy(test_fn_3)

    assert lazy_1 != lazy_2
    assert lazy_1 == lazy_1
    assert lazy_

# Generated at 2022-06-14 03:36:44.754912
# Unit test for method map of class Lazy
def test_Lazy_map():
    """
    Unit test suite for Lazy.map method
    """
    import pytest
    lazy = Lazy(lambda: 'abc')
    print(lazy)
    assert lazy.map(lambda a: a.capitalize()) == Lazy(lambda: 'Abc')

    # Check for lazy evaluation:
    def side_effect_function():
        side_effect_function.call_count += 1
        print('side effect')
        return 'side effect'
    side_effect_function.call_count = 0

    lazy = Lazy(side_effect_function)
    lazy.map(lambda a: a)
    assert side_effect_function.call_count == 0

    # Check for mapping not empty value:
    assert lazy.map(lambda a: a.capitalize()).get() == 'Side effect'
    assert side_effect

# Generated at 2022-06-14 03:36:55.416415
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.monad_maybe import Maybe

    @Lazy
    def add(a, b):
        return a + b

    @Lazy
    def _2(a):
        return a * 2

    assert (_2.bind(add).get(1, 1) == 4)
    assert (add.bind(_2).get(1, 1) == 4)
    assert (Maybe.just(5).bind(add).get(1, 1) == 6)
    assert (Maybe.nothing().bind(add).get(1, 1) is None)
    assert (Maybe.just(5).bind(_2).get(1, 1) == 10)
    assert (Maybe.nothing().bind(_2).get(1, 1) is None)

# Generated at 2022-06-14 03:37:01.775867
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    l1 = Lazy(lambda: 1)
    l2 = Lazy(lambda: 'a')
    assert l1.bind(lambda x: Lazy(lambda: x + 1)).get() == 2
    assert l2.bind(lambda x: Lazy(lambda: x + 2)).get() == 'a2'



# Generated at 2022-06-14 03:37:10.789695
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    assert (
        Lazy(lambda: 1).__eq__(Lazy(lambda: 1)) is True
    ), 'Lazy with same constructor_fn should be equals'
    assert (
        Lazy(lambda: 1).__eq__(Lazy(lambda: 2)) is False
    ), 'Lazy with different constructor_fn should not be equals'
    assert (
        Lazy(lambda: 1).__eq__(None) is False
    ), 'Lazy should not be equals with none'
    assert (
        Lazy(lambda: 1).__eq__(Lazy(lambda: 1).get()) is False
    ), 'Lazy should not be equals with its result'



# Generated at 2022-06-14 03:37:18.945781
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    assert Lazy.of(1).get() == 1
    assert Lazy.of(2).bind(lambda x: Lazy.of(x + 1)).get() == 3
    assert Lazy(lambda x: x + 3).map(lambda x: x * 2).get(2) == 8
    assert Lazy.of(2).bind(lambda x: Lazy.of(x + 1)).get() == 3
    assert Lazy.of(2).to_box().get() == 2
    assert Lazy.of(2).to_either().get() == 2
    assert Lazy.of(2).to_maybe().get() == 2
    assert Lazy.of(3).to_try().get() == 3
    assert Lazy.of(4).to_validation().get() == 4


# Generated at 2022-06-14 03:37:20.079871
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    assert Lazy.of(1).ap(Lazy.of(2)) == Lazy.of(2)


# Generated at 2022-06-14 03:37:29.004991
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.either import Left
    from pymonet.box import Box
    from pymonet.validation import Validation

    f = Lazy.of(1)
    g = Lazy.of(lambda x: x + 1)
    assert f.bind(lambda x: g.map(lambda fx: fx(x))).get() == 2
    assert g.ap(f).get() == 2
    assert f.to_maybe().ap(g).get() == 2
    assert f.to_box().ap(g).get() == 2
    assert f.to_try().to_maybe().ap(g).get() == 2

    # ensure Lazy[A, B] and Lazy[C, D] are compatible for ap

# Generated at 2022-06-14 03:37:39.852506
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    # given
    def fn1() -> int:
        return 1

    def fn2() -> int:
        return 2

    def fn3() -> int:
        return 3

    def fn4() -> int:
        return 4

    l1 = Lazy(fn1)
    l2 = Lazy(fn2)
    l3 = Lazy(fn3)
    l4 = Lazy(fn4)
    l5 = Lazy(fn1)

    # then
    assert l1 == Lazy(fn1)
    assert l1 != Lazy(fn2)

    assert l1 != Lazy(fn3)
    assert l1 != Lazy(fn4)

    assert Lazy(fn1) == l1
    assert Lazy(fn2) != l1

    assert Lazy(fn3) != l1


# Generated at 2022-06-14 03:37:43.761922
# Unit test for method map of class Lazy
def test_Lazy_map():
    assert Lazy(lambda x: x + 1).map(lambda x: x * 2).get(1) == 4
    assert Lazy(lambda: 2).map(lambda x: x * 2).get() == 4


# Generated at 2022-06-14 03:37:48.862522
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    # GIVEN
    generator = (i for i in range(5))
    lazy = Lazy((lambda gen: lambda: next(gen)))

    # WHEN
    lazy_value_generator = lazy.bind(lambda result: Lazy(lambda: result()))

    # THEN
    assert lazy_value_generator.get() == 0
    assert lazy_value_generator.get() == 1



# Generated at 2022-06-14 03:37:52.416168
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.box import Box

    def map_count(string):
        def fn(string):
            return string if len(string) % 2 == 0 else Box()

        return Lazy(fn).bind(Box.of)

    assert map_count('test') == Box()
    assert map_count('test13') == Box('test13')



# Generated at 2022-06-14 03:37:59.569068
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.validation import Validation

    value = Lazy(lambda: 0).ap(Lazy(lambda value: value + 1))
    assert value.get() == 1

    value = Lazy(lambda: Validation.success(0)).ap(Lazy(lambda value: value + 1))
    assert value.get() == Validation.success(1)



# Generated at 2022-06-14 03:38:07.453988
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)

    def fac(n):
        return Lazy(lambda: factorial(n))

    assert fac(5) == fac(5)
    assert fac(5).get(5) == fac(5).get(5)
    assert fac(6).bind(lambda x: Lazy(lambda: str(x))).get() == "720"
    assert fac(5).bind(lambda x: Lazy(lambda: str(x))).get() == "120"

# Generated at 2022-06-14 03:38:18.990172
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():  # pragma: no cover
    # Test for Lazy[int, int]
    assert Lazy(lambda: 1) == Lazy(lambda: 1)
    assert Lazy.of(1) == Lazy.of(1)

    assert Lazy.of(1) != Lazy(lambda: 2)
    assert Lazy(lambda: 1) != Lazy.of(2)

    # Test for Lazy[str, str]
    assert Lazy(lambda: '11') == Lazy(lambda: '11')
    assert Lazy.of('11') == Lazy.of('11')

    assert Lazy.of('1') != Lazy(lambda: '2')
    assert Lazy(lambda: '1') != Lazy.of('2')

    # Test for Lazy[Object, Object]

# Generated at 2022-06-14 03:38:23.310883
# Unit test for method map of class Lazy
def test_Lazy_map():  # pragma: no cover
    lazy = Lazy.of(3)

    def my_func(arg):
        return arg + 2

    assert lazy.map(my_func).get() == 5



# Generated at 2022-06-14 03:38:28.694141
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.monad_try import Try

    def try_constructor_fn(value):
        return Try(lambda: value)

    def mapper(value):
        return Try(lambda: value * 2)

    Lazy.of(2).bind(try_constructor_fn).bind(mapper).get()

# Generated at 2022-06-14 03:38:31.423696
# Unit test for method map of class Lazy
def test_Lazy_map():
    result = Lazy(lambda: 1).map(lambda a: a + 1).get()
    assert result == 2



# Generated at 2022-06-14 03:38:41.142539
# Unit test for method map of class Lazy
def test_Lazy_map():
    assert Lazy.of(1).map(lambda x: x + 1).get() == 2


# Generated at 2022-06-14 03:38:49.239828
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.maybe import Maybe
    from pymonet.either import Right

    assert Lazy.of(lambda x: x + 2).ap(Maybe.just(3)) == Lazy.of(5)
    assert Lazy.of(lambda x: x + 2).ap(Maybe.nothing()) == Lazy.of(lambda x: x + 2)
    assert Lazy.of(lambda x: x + 2).ap(Right(3)) == Lazy.of(5)
    assert Lazy.of(lambda x: x + 2).ap(Right(-1)) == Lazy.of(1)


# Generated at 2022-06-14 03:38:53.163386
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    double = lambda x: x * 2
    f = Lazy(double)
    g = Lazy.of(3)

    assert f.ap(g).get() == 6

# Generated at 2022-06-14 03:38:56.996187
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    lazy = Lazy(lambda x: x + 1)

    def fn(x):
        return Lazy(lambda y: x + y)

    result = lazy.bind(fn)

    assert result.get(2) == 5, 'Lazy bind failed'

# Generated at 2022-06-14 03:39:02.557204
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    constructor_fn = lambda x: x + 1
    first_lazy = Lazy(constructor_fn)
    adder = lambda x: x + 1
    second_lazy = Lazy.of(adder)
    assert first_lazy.ap(second_lazy) == Lazy(lambda x: x + 2)

# Generated at 2022-06-14 03:39:05.097893
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    assert Lazy(lambda _: 1).ap(Lazy.of(lambda x: x + 10)) == Lazy(lambda _: lambda x: x + 10)(1)

# Generated at 2022-06-14 03:39:12.162780
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    from pymonet.box import Box

    assert Lazy.of(Box(1)).map(lambda value: value.value) == Lazy.of(1)
    assert Lazy.of(Box(1)).map(lambda value: value.value) != Lazy.of(2)
    assert Lazy.of(Box(1)).map(lambda value: value.value) != Lazy(lambda *args: Box(1))
    assert Lazy.of(Box(1)).map(lambda value: value.value) != None

# Generated at 2022-06-14 03:39:17.307325
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    lazy_l = Lazy.of(lambda x: x * 2)
    lazy_r = Lazy.of(2)

    assert lazy_l.ap(lazy_r) == Lazy(lambda: 4)
    assert lazy_r.ap(lazy_l) == Lazy(lambda: 4)


# Generated at 2022-06-14 03:39:23.193888
# Unit test for method map of class Lazy
def test_Lazy_map():
    def f(a):
        return a ** 2

    def g(a):
        return a + 2

    lazy_f = Lazy(f)
    mapped_f_lazy = lazy_f.map(g)
    assert mapped_f_lazy.get(10) == 104



# Generated at 2022-06-14 03:39:28.505958
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    def constructor_fn():
        return 'test'

    lazy_1 = Lazy(constructor_fn)
    lazy_2 = Lazy(constructor_fn)
    lazy_3 = Lazy(lambda: 'test')
    assert lazy_1 == lazy_2
    assert lazy_1 != lazy_3
    assert lazy_2 == lazy_3


# Generated at 2022-06-14 03:39:48.682446
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from func_sig import _

    def square(x):
        return x * x

    square_lazy = Lazy.of(square)
    assert Lazy.of(5).ap(square_lazy) == Lazy.of(square(5))
    assert Lazy.of(2).ap(Lazy.of(_ + 3).ap(square_lazy)) == Lazy.of(square(2 + 3))



# Generated at 2022-06-14 03:39:55.486216
# Unit test for method map of class Lazy
def test_Lazy_map():
    from pymonet.bool import Bool

    lazy = Lazy(lambda: 1)
    assert lazy.map(lambda val: val + 2).get() == 3

    lazy = Lazy(lambda: Bool.TRUE)
    assert lazy.map(lambda val: val.is_true).get() is True

    lazy = Lazy(lambda: 1)
    assert lazy.map(lambda val: val + 2).map(lambda val: val + 20).get() == 23



# Generated at 2022-06-14 03:40:03.470186
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.monad_try import Try

    input_value = 10

    fn = (lambda x: 2 * x)

    def raise_error_fn(x):
        raise ValueError('Some error')

    cases = [
        (Lazy.of(fn), input_value, Lazy(lambda: 2 * input_value)),
        (Lazy.of(raise_error_fn), input_value, Lazy(lambda: Try.raise_error(ValueError('Some error')))),
    ]

    for case in cases:
        assert case[0].ap(Lazy.of(input_value)) == case[2]



# Generated at 2022-06-14 03:40:10.417093
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    """
    Another way to call function from Lazy is use bind method
    """
    from pymonet.box import Box

    def fn(a, b):
        return a + b

    a_lazy_f = Lazy.of(fn)
    # a_lazy_f.constructor_fn(2, 3) == 5
    assert a_lazy_f.bind(Box.of).fold(lambda func, a, b: func(a, b))(2, 3) == 5



# Generated at 2022-06-14 03:40:15.994824
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    a = Lazy(lambda x: x)
    b = Lazy(lambda x: x)

    assert a.ap(b) == b.ap(a)
    assert a.ap(b).to_box().value == b.get()



# Generated at 2022-06-14 03:40:26.964003
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    # Configuration
    test_data = {
        'input': {
            'constructor_fn': lambda: 10,
            'mapper_fn': lambda a: a * 2,
        },
        'expected': 20
    }

    # Test
    lazy = Lazy.of(test_data['input']['constructor_fn'])

    result = lazy.bind(
        lambda x: Lazy.of(test_data['input']['mapper_fn'](x))
    ).get()

    # Verify results
    assert test_data['expected'] == result, "expected={}, result={}".format(test_data['expected'], result)



# Generated at 2022-06-14 03:40:31.754941
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.maybe import Maybe

    def f(x):
        return Lazy.of(x + 5)

    v1 = Lazy.of(5).bind(f)
    assert v1.get() == 10

    v2 = Lazy.of(33)
    assert v2.bind(lambda x: Maybe.just(x)).bind(lambda x: Maybe.just(x)).get() == 33

# Generated at 2022-06-14 03:40:42.501824
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    # without any arguments
    assert Lazy.of(1).bind(lambda x: Lazy.of(x + 1)).get() == 2
    assert Lazy.of(1).bind(lambda x: Lazy.of(x.lower())).get() == '1'
    # with some arguments
    assert Lazy.of(1).bind(lambda x, y: Lazy.of(x + y)).get(1) == 2
    assert Lazy.of(1).bind(lambda x, y: Lazy.of(x.lower() + y)).get('acka') == '1acka'



# Generated at 2022-06-14 03:40:49.104467
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def function(num: int) -> Lazy[int, str]:
        """
        :param num: number to stroing in Lazy
        :type num: int
        :returns: Lazy with int number
        :rtype: Lazy[int, str]
        """
        return Lazy(lambda: str(num))

    assert Lazy(lambda: str(2)).bind(function).get() == "2"

# Generated at 2022-06-14 03:40:54.745297
# Unit test for method map of class Lazy
def test_Lazy_map():  # pragma: no cover
    def double(n):
        return n * 2

    def triple(n):
        return n * 3

    def test_lazy_double_triple(n):
        return Lazy.of(n).map(double).map(triple).get()

    assert test_lazy_double_triple(1) == 6

