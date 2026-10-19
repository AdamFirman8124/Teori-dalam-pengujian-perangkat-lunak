

# Generated at 2022-06-14 03:01:33.097265
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method `to_lazy` of class `Box`.
    """
    assert Box(5).to_lazy() == Box(5).to_lazy()

    assert Box(5).to_lazy().fold() == 5


# Generated at 2022-06-14 03:01:35.330011
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    f = lambda: 3
    assert Box(3).to_lazy() == Lazy(f)

# Generated at 2022-06-14 03:01:37.048191
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert (Box(1) == Box(1)).value == True



# Generated at 2022-06-14 03:01:39.530115
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box('abc').to_lazy() == Lazy(lambda: 'abc')

# Generated at 2022-06-14 03:01:41.310977
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    assert Box(1).to_lazy() == Lazy(lambda: Box(1).value)

# Generated at 2022-06-14 03:01:44.178758
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    x = Box(42)
    y = Box(42)
    assert x == y

    x.value = 'foo'
    assert not x == y


# Generated at 2022-06-14 03:01:45.845522
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(1) == Box(1)
    assert Box(1) != Box(2)
    assert Box(1) != (1)



# Generated at 2022-06-14 03:01:48.913728
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(1) != Box(2)
    assert Box(1) == Box(1)



# Generated at 2022-06-14 03:01:52.982567
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(1) == 1
    assert Box(1) == Box(1)
    assert Box(1) != Box('1')
    assert Box(1) != 1
    assert Box(1) != None
    assert Box(1) != Box(2)



# Generated at 2022-06-14 03:01:56.889967
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(1) == Box(1)
    assert Box(1) != Box(2)
    assert Box('test value') == Box('test value')
    assert Box('test value') != Box('test value2')



# Generated at 2022-06-14 03:02:04.058221
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    # Execution
    result = Box(10).to_lazy()

    # Verification
    assert isinstance(result, Lazy)
    assert result.fold(lambda x: x + 20) == 30
    assert result.fold(lambda x: Try.just(x - 10)) == Try.just(0)



# Generated at 2022-06-14 03:02:05.947994
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert Box(1).to_lazy().get() == 1



# Generated at 2022-06-14 03:02:13.993299
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy, is_lazy_value
    from pymonet.monad_try import Try, is_try_value
    def asd():
        return 'asd'

    res = is_lazy_value(Box(asd).to_lazy())
    assert(res)

    res = Box(asd).to_lazy().force()
    assert(res == 'asd')

    res = Box(asd).to_lazy().map(lambda value: value()).force()
    assert(res == 'asd')

    res = Box(asd()).to_lazy().map(lambda value: value()).force()
    assert(res == 'asd')


# Generated at 2022-06-14 03:02:16.402535
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    def f():
        return 5

    assert Box(2).to_lazy() == Lazy(f)

# Generated at 2022-06-14 03:02:19.680558
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(10).to_lazy().eval() == 10
    assert Box(10).to_lazy().eval() == 10
    assert Box(10).to_lazy().map(lambda v: v + 10).eval() == 20



# Generated at 2022-06-14 03:02:23.660287
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    lazy = Box(10).to_lazy()
    result = lazy.fold(lambda: 'Ok')
    assert Lazy(lambda: 10) == lazy
    assert 'Ok' == result

# Generated at 2022-06-14 03:02:27.962626
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Box(123).to_lazy() == Lazy(lambda: 123)
    assert Box('qwerty').to_lazy() == Lazy(lambda: 'qwerty')

# Generated at 2022-06-14 03:02:29.656998
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(123).to_lazy() == Lazy(lambda: 123)


# Generated at 2022-06-14 03:02:32.022434
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Lazy(lambda: 1) == Box(1).to_lazy()

# Generated at 2022-06-14 03:02:37.125862
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    def lazy_evaluator():
        return 5

    box = Box(lazy_evaluator).to_lazy()
    assert type(box) == Lazy
    assert box.value() == 5

# Generated at 2022-06-14 03:02:40.339728
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Box(10).to_lazy() == Lazy(lambda: 10)

# Generated at 2022-06-14 03:02:53.193406
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method `to_lazy` of class `Box`

    :return: nothing
    :rtype: None
    """
    from pymonet.identity import Identity
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe
    from pymonet.identity import Identity

    assert Box(Identity(Identity(Identity("a")))).to_lazy().fold() == Identity("a")
    assert Box(Identity("a")).to_lazy().fold() == Identity("a")
    assert Box("a").to_lazy().fold() == "a"
    assert Box(Maybe.just("a")).to_lazy().fold() == Maybe.just("a")
    assert Box(Maybe.nothing()).to_lazy().fold() == Maybe.nothing()


# Generated at 2022-06-14 03:02:55.589655
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:02:59.207809
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.monad_test import add1

    assert Box(4).to_lazy().fmap(add1).fold() == 5


# Generated at 2022-06-14 03:03:04.053979
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box

    :returns: Nothing
    :rtype: None
    """
    assert Box(1).to_lazy().value() == 1
    assert Box(2).to_lazy().value() == 2
    assert Box(3).to_lazy().value() == 3

# Generated at 2022-06-14 03:03:07.205229
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    value = 1
    box = Box(value)
    lazy_value = box.to_lazy().value.invoke()
    assert lazy_value == value

# Generated at 2022-06-14 03:03:12.754745
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Box(12).to_lazy() == Lazy(lambda: 12)
    assert Box('asdf').to_lazy() == Lazy(lambda: 'asdf')
    assert Box(12).to_lazy().force() == 12
    assert Box(Lazy(lambda: 12)).to_lazy().force().force() == 12

# Generated at 2022-06-14 03:03:14.488602
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    box = Box(5)
    assert box.to_lazy().force() == box.value

# Generated at 2022-06-14 03:03:16.436801
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(42).to_lazy().value() == 42

# Generated at 2022-06-14 03:03:17.521517
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(3).to_lazy().value() == 3

# Generated at 2022-06-14 03:03:19.768612
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    value = 123
    box = Box(value)
    lazy = box.to_lazy()

    assert lazy.is_folded() is False
    assert lazy.value() == value

# Generated at 2022-06-14 03:03:22.540656
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Box(10).to_lazy() == Lazy(lambda: 10)



# Generated at 2022-06-14 03:03:26.092897
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    box = Box(5)
    lazy_box = box.to_lazy()
    assert lazy_box == Lazy(lambda: 5)



# Generated at 2022-06-14 03:03:32.648474
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pytest import raises

    # test for correct value
    assert Box(1).to_lazy() == Lazy(lambda: 1)

    # test for incorrect type of input value
    with raises(TypeError):
        Box('wrong type').to_lazy()

# Generated at 2022-06-14 03:03:38.924370
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert Box(1).to_lazy() == Lazy(lambda: 1)
    assert Box(True).to_lazy() == Lazy(lambda: True)
    assert Box(None).to_lazy() == Lazy(lambda: None)
    assert Box([]).to_lazy() == Lazy(lambda: [])
    assert Box({1: 'one', 2: 'two'}).to_lazy() == Lazy(lambda: {1: 'one', 2: 'two'})



# Generated at 2022-06-14 03:03:40.284046
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(0).to_lazy() == Lazy(lambda: 0)

# Generated at 2022-06-14 03:03:48.666872
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test behaviour of to_lazy method of Box class.

    :returns: nothing
    :rtype: None
    """
    from pymonet.lazy import Lazy
    value = 5
    # create box with value and transform it into Lazy
    lazy = Box(value).to_lazy()
    # checks lazy instance type
    assert isinstance(lazy, Lazy), 'Box.to_lazy() result must be instance of Lazy'
    # checks lazy instance value
    assert lazy.to_value() == value, 'Box.to_lazy() must return Lazy with same value as Box'



# Generated at 2022-06-14 03:03:50.818159
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:03:53.566591
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(5).to_lazy() == Lazy(lambda: 5)


# Generated at 2022-06-14 03:03:56.430813
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe

    result = Lazy(lambda: Maybe.just(5))

    assert Box(Maybe.just(5)).to_lazy() == result



# Generated at 2022-06-14 03:04:04.843128
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test for method to_lazy for class Box.
    """

    # Test for converting Box to Lazy with previous value
    box_1 = Box(1)
    assert box_1.to_lazy().value() == 1, 'Box should be converted to Lazy with previous value'

    # Test for converting empty Box to Lazy with previous value
    box_2 = Box(0)
    assert box_2.to_lazy().value() == 0, 'Box should be converted to Lazy with previous value'



# Generated at 2022-06-14 03:04:08.897094
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    box = Box(1)
    assert box.map(lambda x: x + 1) == Box(2)
    assert box.to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:04:12.638733
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    This test case for testing method to_lazy for Box monad

    :returns: AssertionError if test failed
    """

    from pymonet.lazy import Lazy

    assert Box(3).to_lazy() == Lazy(lambda : 3)



# Generated at 2022-06-14 03:04:16.883283
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe

    assert Box(Lazy.unit(5)).to_lazy().f == 5
    assert Box(Maybe.just(5)).to_lazy().f == 5



# Generated at 2022-06-14 03:04:22.013271
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    def value_retrieving_function():
        return 'test'

    assert Box(value_retrieving_function).to_lazy() == Lazy(value_retrieving_function)


# Generated at 2022-06-14 03:04:24.164689
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(5).to_lazy().unwrap() == 5

# Generated at 2022-06-14 03:04:27.788936
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert isinstance(Box(1).to_lazy(), Lazy)



# Generated at 2022-06-14 03:04:30.103295
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(12).to_lazy() == Lazy(lambda: 12)

# Generated at 2022-06-14 03:04:34.108608
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.syntax import lazy

    assert lazy(Lazy(lambda: 2).value) == lazy(Box(2).to_lazy().value)

# Generated at 2022-06-14 03:04:35.740805
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert Box(5).to_lazy().f() == 5


# Generated at 2022-06-14 03:04:40.063844
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    box = Box(10)
    assert box.to_lazy() == Lazy(lambda: 10)

# Generated at 2022-06-14 03:04:41.217346
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(2).to_lazy() == Lazy(lambda: 2)



# Generated at 2022-06-14 03:04:47.877175
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for to_lazy method of class Box

    :returns: Nothing
    :rtype: None
    """
    from pymonet.lazy import Lazy

    assert Box(10).to_lazy() == Lazy(lambda: 10)

# Generated at 2022-06-14 03:04:57.547924
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test Box.to_lazy method
    """
    from pymonet.lazy import Lazy

    # GIVEN
    box = Box(100)

    # WHEN
    lazy = box.to_lazy()

    # THEN
    if not isinstance(lazy, Lazy):
        raise TypeError('Box.to_lazy returned {}, but expected Lazy instance!'.format(type(lazy)))

    from pymonet.monad import bind
    result = bind(lazy, lambda v: v - 2)
    if result.value != 98:
        raise ValueError('Lazy.value returned {}, but expected 98!'.format(result.value))


# Generated at 2022-06-14 03:05:01.529967
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box
    """
    from pymonet.lazy import Lazy
    assert Lazy(lambda: 100) == Box(100).to_lazy()

# Generated at 2022-06-14 03:05:03.262235
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert Box(1).to_lazy().fold_lazy(lambda: 2) == 1

# Generated at 2022-06-14 03:05:04.937824
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    box = Box(lambda a: a * 10)
    assert box.to_lazy() == Lazy(box.value)



# Generated at 2022-06-14 03:05:07.906171
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Lazy(lambda: 10) == Box(10).to_lazy()

    # method is lazy
    assert Lazy(lambda: 'lazy') == Lazy(lambda: Box('lazy').to_lazy())



# Generated at 2022-06-14 03:05:09.471821
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    box = Box(1)
    assert box.to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:05:13.617245
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from nose.tools import assert_equal

    assert_equal(Box(1).to_lazy(), Lazy(lambda: 1))



# Generated at 2022-06-14 03:05:19.993442
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box
    """
    from pymonet.lazy import Lazy

    lazy = Box(1).to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy.eval() == 1

# Generated at 2022-06-14 03:05:22.039425
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy
    assert Box(5).to_lazy() == Lazy(lambda: 5)

# Generated at 2022-06-14 03:05:27.317457
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe

    assert Box(10).to_lazy() == Lazy(lambda: 10)
    assert Box(Maybe.just(10)).to_lazy() == Lazy(lambda: Maybe.just(10))



# Generated at 2022-06-14 03:05:29.636078
# Unit test for method to_lazy of class Box
def test_Box_to_lazy(): # pragma: no cover
    from pymonet.lazy import Lazy

    assert Box(42).to_lazy() == Lazy(lambda: 42)

# Generated at 2022-06-14 03:05:33.065565
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    box = Box('string')

    lazy = box.to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy.unbox() == 'string'


# Generated at 2022-06-14 03:05:36.532794
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test of 'to_lazy' method in Box.
    """
    from pymonet.lazy import Lazy
    assert Box(5).to_lazy() == Lazy(lambda: 5)



# Generated at 2022-06-14 03:05:37.952499
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(10).to_lazy() == Lazy(lambda: 10)

# Generated at 2022-06-14 03:05:42.516352
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Lazy(lambda: 4) == Box(4).to_lazy()
    assert Lazy(lambda: Try(4, is_success=True)) == Box(Try(4, is_success=True)).to_lazy()



# Generated at 2022-06-14 03:05:46.890460
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    """
    Unit test for method to_lazy of class Box.
    """
    from pymonet.lazy import Lazy

    assert Box(True).to_lazy() == Lazy(lambda: True)
    assert Box(2).to_lazy() == Lazy(lambda: 2)
    assert Box('hello').to_lazy() == Lazy(lambda: 'hello')



# Generated at 2022-06-14 03:05:50.509560
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box
    """
    from pymonet.lazy import Lazy

    lazy_value = Lazy(lambda: 'test')

    assert Box('test').to_lazy() == lazy_value



# Generated at 2022-06-14 03:06:03.115889
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    box = Box(42)
    lazy = box.to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy() == box.value

# Generated at 2022-06-14 03:06:05.713006
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    # given
    value = 3
    box = Box(value)
    # when
    result = box.to_lazy()
    # then
    assert result.value() == value

# Generated at 2022-06-14 03:06:11.497210
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy().value() == 1
    assert Box(True).to_lazy().value() == True
    assert Box(None).to_lazy().value() == None
    assert Box('test').to_lazy().value() == 'test'



# Generated at 2022-06-14 03:06:14.125527
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    result = Box(1).to_lazy()
    assert isinstance(result, Lazy)
    assert result.value() == 1


# Generated at 2022-06-14 03:06:16.084367
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    assert Box(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:06:18.501039
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(2).to_lazy().value() == 2

# Generated at 2022-06-14 03:06:24.000911
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box.
    """
    from pymonet.lazy import Lazy
    assert(Lazy(lambda: 5) == Box(5).to_lazy())

# Generated at 2022-06-14 03:06:31.483484
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    import unittest
    from pymonet.lazy import Lazy

    # Simple test with number value
    assert Box(123).to_lazy() == Lazy(lambda: 123)

    class Test(unittest.TestCase):
        def test(self):
            # Simple test with list value
            self.assertEqual(Box([123, 456]).to_lazy(), Lazy(lambda: [123, 456]))

    unittest.main()


# Generated at 2022-06-14 03:06:35.639065
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box
    """
    assert Box(42).to_lazy().is_val(42)



# Generated at 2022-06-14 03:06:38.657060
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    assert Box(123).to_lazy() == Lazy(lambda: 123)

# Generated at 2022-06-14 03:07:01.109857
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert str(Box(1).to_lazy()) == "Lazy[value=<function Box.to_lazy.<locals>.<lambda> at 0x{}>]".format(hex(id(Box(1).to_lazy().value)))
    assert Box(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:07:03.302193
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert Box(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:07:05.319899
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test lazification method of Box monad.
    """
    assert Lazy(lambda: 42) == Box(42).to_lazy()


# Generated at 2022-06-14 03:07:08.092563
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    test_value = 42
    lazy = Box(test_value).to_lazy()

    assert lazy == Lazy(lambda: test_value)

# Generated at 2022-06-14 03:07:11.462842
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    value = 2
    box = Box(value)

    assert isinstance(box.to_lazy(), Lazy)
    assert box.to_lazy().force() == value



# Generated at 2022-06-14 03:07:13.536327
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    def return_value(value):
        return value

    assert Box(4).to_lazy().value() == return_value(4)

# Generated at 2022-06-14 03:07:17.308143
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    box = Box(1)
    assert box.to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:07:24.851900
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    a = Box(12)
    lazy = a.to_lazy()
    assert lazy.get_value() == 12
    assert repr(lazy) == 'Lazy[function=<function Box_to_lazy.<locals>.<lambda> at 0x10c9eabf8>]'
    assert str(lazy) == 'Lazy[function=<function Box_to_lazy.<locals>.<lambda> at 0x10c9eabf8>]'


# Generated at 2022-06-14 03:07:30.451672
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.monoid import Sum
    from pymonet.lazy import Lazy

    lazy_value = Lazy.unit(Sum(10))
    lazy_value = lazy_value.map(lambda x: x.value + 100)

    assert lazy_value.value() == 110
    assert lazy_value.value() == 110

# Generated at 2022-06-14 03:07:33.368538
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test of transformation of Box into not folded Lazy.

    :returns: None
    :rtype: None
    """
    assert Box(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:08:19.284835
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    # Test case 1
    value = 'hello'
    my_box = Box(value)
    assert my_box.to_lazy() == Lazy(lambda: 'hello')

    # Test case 2
    value = lambda x: 2 * x
    my_box = Box(value)
    assert my_box.to_lazy() == Lazy(lambda: lambda x: 2 * x)


# Generated at 2022-06-14 03:08:25.686793
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1) == Box(1).to_lazy()
    assert Lazy(lambda: '2') == Box('2').to_lazy()
    assert Lazy(lambda: '3') == Box('3').to_lazy()



# Generated at 2022-06-14 03:08:28.011688
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    import pymonet.lazy as lazy
    assert lazy.Lazy(lambda: '1') == Box('1').to_lazy(), 'Should return not folded Lazy monad with function returning previous value'

# Generated at 2022-06-14 03:08:31.527881
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert isinstance(Box(1).to_lazy(), Lazy)



# Generated at 2022-06-14 03:08:35.231159
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    """
    Unit test for method to_lazy for class Box.

    """
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    assert Box(12).to_lazy() == Lazy(lambda: 12)



# Generated at 2022-06-14 03:08:37.354478
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Lazy(lambda: 5) == Box(5).to_lazy()

# Generated at 2022-06-14 03:08:39.409456
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():

    assert Box(3).to_lazy().map(lambda x: x**2).force() == 9


# Generated at 2022-06-14 03:08:50.544954
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box
    """
    from pymonet.lazy import Lazy
    from pymonet.test.test_validation import _test_validation_to_lazy
    from pymonet.test.test_either import _test_either_to_lazy
    from pymonet.test.test_try import _test_try_to_lazy
    from pymonet.test.test_maybe import _test_maybe_to_lazy
    from pymonet.test.test_lazy import _test_lazy_to_lazy


# Generated at 2022-06-14 03:08:54.566580
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box.
    """

    a_box = Box(5)

    lazy_box = a_box.to_lazy()

    assert lazy_box == Lazy(lambda: 5)

# Generated at 2022-06-14 03:08:58.185227
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)
    assert Box(1).to_lazy().fold() == 1


# Generated at 2022-06-14 03:09:44.154630
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box
    """

    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)

# unit test for method to_validation of class Box

# Generated at 2022-06-14 03:09:46.638451
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(3).to_lazy() == Lazy(lambda: 3)


# Generated at 2022-06-14 03:09:47.634087
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert Box(1).to_lazy().force() == 1
    assert Box("").to_lazy().force() == ""

# Generated at 2022-06-14 03:09:48.838099
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(5).to_lazy().evaluate() == 5

# Generated at 2022-06-14 03:09:49.914248
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy().force() == 1



# Generated at 2022-06-14 03:09:50.990914
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(5).to_lazy().force() == 5

# Generated at 2022-06-14 03:09:52.039433
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(42).to_lazy() == Lazy(lambda: 42)

# Generated at 2022-06-14 03:09:53.371953
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert Box(10).to_lazy() == Lazy(lambda: 10)



# Generated at 2022-06-14 03:09:56.608774
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """ Unit test for method `to_lazy` of class `Box` """

    from pymonet.lazy import Lazy

    assert isinstance(Box(123).to_lazy(), Lazy)



# Generated at 2022-06-14 03:09:59.580553
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    input = Box(1)
    result = input.to_lazy()
    assert isinstance(result, Lazy)
    assert result.fold(lambda: None) == 1


# Generated at 2022-06-14 03:11:29.681007
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    def foo(x):
        return x * 2

    assert Box(1).to_lazy() == Lazy(lambda: 1)
    assert foo(Box(1).to_lazy().value()) == 2
    assert Box(1).to_lazy().map(lambda x: x + 1).value() == 2