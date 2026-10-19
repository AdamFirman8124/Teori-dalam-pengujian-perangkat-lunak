

# Generated at 2022-06-14 03:01:37.616710
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet import Lazy

    assert Lazy(lambda: Box(5).value) == Box(5).to_lazy()



# Generated at 2022-06-14 03:01:40.850145
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    lazy: Lazy[Callable[[], int]] = Box(5).to_lazy()
    assert lazy.get() == Box(5).value
    assert lazy.get() == 5


# Generated at 2022-06-14 03:01:42.172135
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(5) == Box(5)



# Generated at 2022-06-14 03:01:46.041160
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    sut = Box(5).to_lazy()
    assert sut.fold(lambda x: x + 1) == 6
    assert sut.fold(lambda x: x) == 5
    assert sut.fold(lambda x: x) == 5



# Generated at 2022-06-14 03:01:49.772463
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(1) == Box(1)
    assert Box(1) != Box(2)
    assert Box(1) != "asd"
    assert Box(1) != None

# Generated at 2022-06-14 03:01:52.552099
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    # given
    given_value = 1
    # and
    box = Box(given_value)
    # and
    from pymonet.lazy import Lazy

    expected = Lazy(lambda: given_value)
    # when
    result = box.to_lazy()
    # then
    assert result == expected
    # when
    result = result.get()
    # then
    assert result == expected.get()

# Generated at 2022-06-14 03:01:59.318007
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(1) == Box(1)
    assert Box('a') == Box('a')
    assert Box((1, 2)) == Box((1, 2))
    assert Box('a') != Box('b')
    assert Box(1) != Box(2)
    assert Box((1, 2)) != Box((2, 3))


# Generated at 2022-06-14 03:02:03.099350
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(1) == Box(1)
    assert Box(1) != Box(2)
    assert Box(1) != 'Box(1)'



# Generated at 2022-06-14 03:02:05.340208
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(5) == Box(5)
    assert Box(5) != Box(6)
    assert Box(5) != 1



# Generated at 2022-06-14 03:02:09.695749
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.lazy import lazy

    box = Box(lambda: 42)
    assert box.to_lazy() == Lazy(lambda: 42)
    assert box.to_lazy().force() == 42
    assert lazy(box.to_lazy()).force() == 42



# Generated at 2022-06-14 03:02:13.250812
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test transformation into Lazy
    """
    assert Box(5).to_lazy().value() == 5

# Generated at 2022-06-14 03:02:15.548421
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(1) == Box(1)
    assert Box(list(range(100))) == Box(list(range(100)))



# Generated at 2022-06-14 03:02:18.517694
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(1) == Box(1)
    assert Box(1) != Box(2)
    assert Box(1) != 1
    assert Box(1) != None


# Generated at 2022-06-14 03:02:21.079926
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Check correctness of to_lazy of class Box.
    """
    from pymonet.lazy import Lazy

    assert Box(5).to_lazy().value() == Lazy(lambda: 5).value()

# Generated at 2022-06-14 03:02:25.357432
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    """
    Unit test for method __eq__ of class Box
    """

    box1 = Box('value')
    box2 = Box('value')
    box3 = Box('another value')

    assert box1 == box2
    assert box2 == box1
    assert box1 != box3
    assert box3 != box1



# Generated at 2022-06-14 03:02:29.508044
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert(Box(42).to_lazy() == Lazy(lambda: 42))


# Generated at 2022-06-14 03:02:33.020445
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    box = Box(1)
    lazy = box.to_lazy()
    assert type(lazy) is Lazy and lazy.f() == 1

# Generated at 2022-06-14 03:02:38.201622
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box("test") == Box("test")
    assert Box("test") != Box("not test")

    assert Box("test") == "test"
    assert Box("test") != "not test"

    assert Box("test") == None
    assert Box("not test") != None



# Generated at 2022-06-14 03:02:46.138157
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.monoids import Sum

    box = Box(Sum(1))
    boxed_lazy = box.to_lazy()
    assert boxed_lazy.is_folded is False
    assert boxed_lazy.fold() == box
    assert boxed_lazy.is_folded is True
    # Checking that lazy is not evaluating second time
    assert boxed_lazy.fold() == box
    assert boxed_lazy.is_folded is True

# Generated at 2022-06-14 03:02:50.309555
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(1) != Box(1)
    assert Box(1) == Box(1)
    assert Box(1) != Box(2)
    assert Box(1) != Box((1,))



# Generated at 2022-06-14 03:02:54.830344
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    assert Box(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:02:57.223109
# Unit test for method __eq__ of class Box
def test_Box___eq__():  # pragma: no cover
    assert Box(1) == Box(1)
    assert Box(1) != Box(2)
    assert Box(1) != 1



# Generated at 2022-06-14 03:02:59.119207
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert Lazy(lambda: 10).value() == Box(10).to_lazy().value()

# Generated at 2022-06-14 03:03:01.389753
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert Box("abc").to_lazy().value() == 'abc'

# Generated at 2022-06-14 03:03:06.260427
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    box = Box(5)  # type: Box[int]
    lazy = box.to_lazy()
    assert lazy == Lazy(lambda: 5)



# Generated at 2022-06-14 03:03:09.126876
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(1) == Box(1)
    assert not Box(1) == Box(2)
    assert not Box(1) == '1'



# Generated at 2022-06-14 03:03:14.325981
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Box('eins').to_lazy() == Lazy(lambda: 'eins')
    assert Box(2).to_lazy() == Lazy(lambda: 2)
    assert Box(None).to_lazy() == Lazy(lambda: None)
    assert Box(True).to_lazy() == Lazy(lambda: True)


# Generated at 2022-06-14 03:03:16.685373
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Lazy(lambda: 1) == Box(1).to_lazy()



# Generated at 2022-06-14 03:03:23.769950
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    def demo_func():
        return 'abc'

    abc = Box(demo_func).to_lazy()

    assert isinstance(abc, Lazy)
    assert abc.get()() == 'abc'
    assert Box(demo_func).to_lazy().get()() == 'abc'

    assert Box(None).to_lazy() == Lazy(lambda: None)

    real = Try(demo_func)
    assert real.to_lazy() is Lazy(real.get)

# Generated at 2022-06-14 03:03:28.150924
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test to_lazy method of Box class

    :returns: Nothing
    :rtype: Nothing
    """
    from pymonet.functor import Functor

    value = 1
    monad = Box(value)

    monad_lazy = monad.to_lazy()
    assert(monad_lazy.value() == value)
    assert(Functor.fmap(lambda x: x + 1, monad_lazy).value() == monad_lazy.value() + 1)

# Generated at 2022-06-14 03:03:35.158001
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(5).to_lazy().foldr(lambda x: x) == 5
    assert Box([1, 2, 3]).to_lazy().foldr(lambda x: x) == [1, 2, 3]
    assert Box(None).to_lazy().foldr(lambda x: x) is None
    assert Box(True).to_lazy().foldr(lambda x: x) is True



# Generated at 2022-06-14 03:03:37.416740
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box
    """
    assert Lazy(lambda: 5) == Box(5).to_lazy()


# Generated at 2022-06-14 03:03:40.188187
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 2) == Box(2).to_lazy()



# Generated at 2022-06-14 03:03:50.528200
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert Box(2).to_lazy() == Lazy(lambda: 2)
    assert Box(2).to_lazy().value() == 2
    assert Box(3.14).to_lazy() == Lazy(lambda: 3.14)
    assert Box(3.14).to_lazy().value() == 3.14
    assert Box("hello").to_lazy() == Lazy(lambda: "hello")
    assert Box("hello").to_lazy().value() == "hello"
    assert Box([1, 2, 3, 4]).to_lazy() == Lazy(lambda: [1, 2, 3, 4])
    assert Box([1, 2, 3, 4]).to_lazy().value() == [1, 2, 3, 4]


# Generated at 2022-06-14 03:03:55.121861
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    import pymonet.lazy
    def a():
        return 'b'
    x = Box('a')
    b = x.to_lazy()
    print(b)
    assert b.get() == 'a'
    assert b.fold(a) == 'a'
    assert b != x


# Generated at 2022-06-14 03:03:56.934879
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy() == Lazy(lambda: 1)
    assert Box(1).to_lazy().run() == 1

# Generated at 2022-06-14 03:03:59.065114
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:04:00.727461
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:04:04.936442
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    >>> test_Box_to_lazy()
    (1, 1)
    """
    lazy = Box(1).to_lazy()
    assert lazy.fold() == 1
    assert lazy.fold() == 1

# Generated at 2022-06-14 03:04:07.196381
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:04:11.456368
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    value = 42
    box = Box(value)
    assert box.to_lazy().value == value

# Generated at 2022-06-14 03:04:14.391628
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Box(5).to_lazy() == Lazy(lambda: 5)

# Generated at 2022-06-14 03:04:18.524799
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for to_lazy method of class Box.
    """
    box = Box('value')
    lazy = box.to_lazy()

    assert lazy == Lazy(lambda: 'value')

# Generated at 2022-06-14 03:04:20.606599
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(4).to_lazy().evaluate() == 4



# Generated at 2022-06-14 03:04:23.127782
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    def func():
        return 1

    assert Box(1).to_lazy() == Lazy(func)

# Generated at 2022-06-14 03:04:26.655839
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(True).to_lazy() == Lazy(lambda: True)



# Generated at 2022-06-14 03:04:31.003855
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """Unit test for method to_lazy of class Box"""
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:04:35.341490
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test Box.to_lazy method.
    """

    # given
    some_value = [1, 2, 3]
    box = Box(some_value)

    # when
    lazy = box.to_lazy()

    # then
    assert lazy.is_folded() is False
    assert lazy.value() == some_value


# Generated at 2022-06-14 03:04:37.809409
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy() == Box(1).bind(lambda x: Lazy(lambda: x))

# Generated at 2022-06-14 03:04:39.815748
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:04:52.530316
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.functor import Functor

    def test_map(value):
        return value - 1

    box = Box(5)
    maybe = box.to_lazy()

    assert isinstance(maybe, Lazy)
    assert isinstance(maybe, Functor)
    assert callable(maybe.value)
    assert maybe.value() == 5

    mapped_box = maybe.map(test_map)
    assert callable(mapped_box.value)
    assert mapped_box.value() == 4

# Generated at 2022-06-14 03:04:54.170082
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    def five():
        return 5

    assert Box(five).to_lazy().unwrap() == 5

# Generated at 2022-06-14 03:04:55.743738
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    box = Box(1)

    lazy = box.to_lazy()

    assert lazy.value() == 1

# Generated at 2022-06-14 03:04:57.733988
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    def f():  # pragma: no cover
        pass
    lazy = Box(f).to_lazy()

    assert lazy == Lazy(f)



# Generated at 2022-06-14 03:05:02.306294
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    box = Box(5)
    lazy_box = box.to_lazy()

    assert isinstance(lazy_box, Lazy)
    assert lazy_box.fold() == 5



# Generated at 2022-06-14 03:05:05.245396
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box('test').to_lazy().is_lazy()
    assert not Box('test').to_lazy().is_folded()
    assert Box('test').to_lazy().value() == 'test'

# Generated at 2022-06-14 03:05:13.114436
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box
    """

    test_input_1: Box[int] = Box(1)
    actual_result_1: Box[int] = test_input_1.to_lazy().force()

    assert actual_result_1 == Box(1)

    test_input_2: Box[int] = Box(2)
    actual_result_2: Box[int] = test_input_2.to_lazy().force()

    assert actual_result_2 == Box(2)

# Generated at 2022-06-14 03:05:15.239851
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(3).to_lazy() == Lazy(lambda: 3)



# Generated at 2022-06-14 03:05:16.939995
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:05:18.272585
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert Box(10).to_lazy() == Lazy(lambda: 10)

# Generated at 2022-06-14 03:05:37.453662
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box

    :return: None
    """

    def _test_function(arg1: int, arg2: int) -> int:
        return arg1 + arg2

    lazy_function = _test_function.__call__
    lazy_function_reference = _test_function

    # Call to_lazy method and save result in lazy_value_1
    lazy_value_1 = Box(lazy_function).to_lazy()

    # Call to_lazy method and save result in lazy_value_2
    lazy_value_2 = Box(lazy_function_reference).to_lazy()

    # Call to_lazy method and save result in lazy_value_3
    lazy_value_3 = Box(_test_function).to_lazy()

    assert lazy_

# Generated at 2022-06-14 03:05:39.766222
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:05:41.845332
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    result = Box(10).to_lazy()

    assert isinstance(result, Lazy)
    assert result.fold() == 10


# Generated at 2022-06-14 03:05:44.265052
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy
    assert Box('value').to_lazy() == Lazy(lambda: 'value')

# Generated at 2022-06-14 03:05:46.093393
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    @Box
    def fn():
        return 10

    assert fn.to_lazy() == Lazy(lambda: 10)



# Generated at 2022-06-14 03:05:48.321027
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy() == Box(2).to_lazy()
    assert Box(1).to_lazy() != Box(1).to_lazy()


# Generated at 2022-06-14 03:05:51.159042
# Unit test for method to_lazy of class Box
def test_Box_to_lazy(): # pragma: no cover
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1) == Box[int](1).to_lazy()

# Generated at 2022-06-14 03:05:54.776908
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    # GIVEN any Box monad
    box = Box(1)

    # WHEN to_lazy method will called
    lazy = box.to_lazy()

    # THEN Lazy with return box monad value function should returned
    assert lazy.fold() == 1

# Generated at 2022-06-14 03:05:57.825437
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    lazy = Box(10).to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.is_eager() is False
    assert lazy.is_empty() is False
    assert lazy.force() == 10


# Generated at 2022-06-14 03:06:00.499416
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    lazy_value = Lazy(lambda: 1)

    assert Box(1).to_lazy() == lazy_value

# Generated at 2022-06-14 03:06:13.927046
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Tests converting of Box to lazy.

    :return: None
    """
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1) == Box(1).to_lazy()

# Generated at 2022-06-14 03:06:16.999112
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(5).to_lazy() == Lazy(lambda: 5)
    assert Box(6).to_lazy().value() == 6
    assert Box(7).to_lazy().map(lambda v: v * v).value() == 49


# Generated at 2022-06-14 03:06:21.003921
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 10).value == Box(10).to_lazy().value()


# Generated at 2022-06-14 03:06:24.570468
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:06:26.944403
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 10) == Box(10).to_lazy()


# Generated at 2022-06-14 03:06:28.440016
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box
    """
    assert Box(1).to_lazy().eval() == 1



# Generated at 2022-06-14 03:06:30.194051
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    x = Box(3)
    assert x.to_lazy() == Lazy(lambda: 3)


# Generated at 2022-06-14 03:06:33.974160
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(5).to_lazy() == Lazy(lambda: 5)



# Generated at 2022-06-14 03:06:45.860471
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Return correct Lazy monad on Box.to_lazy method.

    :return: none
    :rtype: None
    """
    from pymonet.bell import bell
    from pymonet.lazy import Lazy
    from pymonet.logger import logger
    from pymonet.monad_try import Try, is_success

    value = bell()

    lazy = Box(value).to_lazy()

    assert isinstance(lazy, Lazy)

    logger.info('Value: {}'.format(value))
    logger.info('Box: {}'.format(Box(value)))
    logger.info('Lazy: {}'.format(lazy))
    logger.info('Lazy.value: {}'.format(lazy.value()))


# Generated at 2022-06-14 03:06:47.322232
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box('test').to_lazy().value() == 'test'


# Generated at 2022-06-14 03:07:09.469806
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy().value() == 1



# Generated at 2022-06-14 03:07:14.564328
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)
    assert Box("Test").to_lazy() == Lazy(lambda: "Test")
    assert Box("").to_lazy() == Lazy(lambda: "")
    assert Box(1.0).to_lazy() == Lazy(lambda: 1.0)
    assert Box(50).to_lazy() == Lazy(lambda: 50)


# Generated at 2022-06-14 03:07:17.747957
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box
    """
    assert Box(5).to_lazy().value() == 5


# Generated at 2022-06-14 03:07:20.494061
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    def test():
        x = Box(3)
        y = x.to_lazy()
        return y.fold(lambda: 0, lambda num: num)

    assert test() == 3

# Generated at 2022-06-14 03:07:24.641301
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """Unit test for method to_lazy of class Box"""

    from pymonet.lazy import Lazy

    a = Box(Lazy(lambda: 1)).to_lazy()

    assert a.force() == Lazy(lambda: 1).force()

# Generated at 2022-06-14 03:07:27.227383
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    actual = Box(4).to_lazy()
    expected = [4]
    assert actual.values == expected

# Generated at 2022-06-14 03:07:29.306885
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 10).fold() == Box(10).to_lazy().fold()

# Generated at 2022-06-14 03:07:31.590235
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    # given
    value = 2
    box = Box(value)
    # when
    lazy = box.to_lazy()
    # then
    assert lazy.force() == value


# Generated at 2022-06-14 03:07:33.998210
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    import pytest

    assert Box(1).to_lazy().value() == 1
    with pytest.raises(TypeError):
        Box(1).to_lazy().value()(1)


# Generated at 2022-06-14 03:07:37.633138
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    # Test for empty Box
    assert Box(None).to_lazy().fold() is None

    # Test for Box with not None value
    assert Box(1).to_lazy().fold() == 1



# Generated at 2022-06-14 03:08:31.153791
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert Box(42).to_lazy() == Box(42).to_lazy()
    assert Box(42).to_lazy().map(lambda x: x * 2) == Box(84).to_lazy()
    assert Box(42).to_lazy().map(lambda x: x * 2).value() == 84
    assert Box(lambda a, b: a + b).to_lazy().apply(Box(2), Box(3)).value() == 5
    assert Box(42).to_lazy().map(lambda x: x * 2).value() == 84
    assert Box(42).to_lazy().bind(lambda x: Box(x * 2)).value() == 84

# Generated at 2022-06-14 03:08:33.077360
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:08:38.775108
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    def _test_to_lazy(box: Box) -> bool:
        from pymonet.lazy import Lazy

        return Lazy(lambda: 1) == box.to_lazy()

    assert _test_to_lazy(Box(1))


# Generated at 2022-06-14 03:08:41.883842
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test to_lazy method of class Box.

    :return: Nothing
    """
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 100) == Box(100).to_lazy()



# Generated at 2022-06-14 03:08:45.764791
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box
    """
    actual = Box(1).to_lazy()
    expected = Lazy(lambda: 1)

    assert actual == expected


# Generated at 2022-06-14 03:08:47.365688
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(3).to_lazy().eval() == 3



# Generated at 2022-06-14 03:08:48.752520
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy().value() == 1



# Generated at 2022-06-14 03:08:52.701920
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert type(Box(5).to_lazy()) is Lazy
    assert Box(5).to_lazy().eval() == 5

# Generated at 2022-06-14 03:08:56.688273
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    value = 'value'
    lazy = Box(value).to_lazy()
    assert lazy.is_folded() is False
    assert lazy.fold() == value
    assert isinstance(lazy, Lazy)


# Generated at 2022-06-14 03:09:07.504648
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.monad_validation import Validation
    from pymonet.monad_try import Error

    number_box = Box(1)
    assert number_box.to_lazy().value() == 1

    string_box = Box('Hello World')
    assert string_box.to_lazy().value() == 'Hello World'

    def some_function() -> int:
        return 42

    function_box = Box(some_function)
    assert function_box.to_lazy().value() == 42

    try_box = Box(Try(1, is_success=True))
    assert try_box.to_lazy().value().value == 1

    validation_box = Box(Validation.success(1))
    assert validation_box.to_lazy

# Generated at 2022-06-14 03:10:47.768511
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box.
    """
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:10:58.281963
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    def get_value():
        return 'value'

    assert Box(get_value).value() == 'value'

# Generated at 2022-06-14 03:11:01.949273
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:11:05.915445
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for to_lazy method of class Box.
    """
    assert isinstance(Box(1).to_lazy(), 'pymonet.lazy.Lazy')

# Generated at 2022-06-14 03:11:08.291202
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(2).to_lazy().evaluate() == Lazy(lambda: 2).evaluate()

# Generated at 2022-06-14 03:11:18.084262
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box('test').to_lazy() is Lazy(lambda: 'test')

# Generated at 2022-06-14 03:11:22.687452
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for Box.to_lazy method
    """
    from pymonet.lazy import Lazy

    assert Box(2).to_lazy() == Lazy(lambda: 2)

# Generated at 2022-06-14 03:11:24.789120
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy() == Box(1).value

# Generated at 2022-06-14 03:11:36.982223
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.either import Right

    lazy = Right(10).to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.fold() == 10
