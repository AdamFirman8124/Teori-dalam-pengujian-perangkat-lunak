

# Generated at 2022-06-14 03:16:50.849359
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    from pymonet.functor import Functor

    assert not Either(1).__eq__(1)
    assert Either(1).__eq__(Functor(1))
    assert not Either(1).__eq__(Functor(2))
    assert not Either(1).__eq__(Functor(2))
    assert not Either(1).__eq__(Either(2))
    assert Either(1).__eq__(Either(1))
    assert Left(1).__eq__(Left(1))
    assert not Left(1).__eq__(Left(2))
    assert not Left(1).__eq__(Right(2))
    assert not Left(1).__eq__(Either(1))
    assert not Left(1).__eq__(Either(2))

# Generated at 2022-06-14 03:16:54.374851
# Unit test for method case of class Either
def test_Either_case():
    assert Either(True).case(lambda _: 'value', lambda _: 'message') == 'message'
    assert Either(1).case(lambda _: 'value', lambda _: 'message') == 'value'



# Generated at 2022-06-14 03:17:00.516158
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Right(1) == Right(1)
    assert Left(Exception("Error!")) == Left(Exception("Error!"))
    assert Left(Exception("Error!")) != Left(Exception("Another Error!"))
    assert Right(1) != Left(1)
    assert Right("var") != Right("var2")


# Generated at 2022-06-14 03:17:04.181311
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Left(1) == Left(1)
    assert Left(1) != Left(2)
    assert Right(1) == Right(1)
    assert Right(1) != Right(2)
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)


# Generated at 2022-06-14 03:17:13.221306
# Unit test for method case of class Either
def test_Either_case():
    def error_handler(error: str) -> str:
        return "E " + error

    def success_handler(success: str) -> str:
        return "S " + success

    assert Left("Error Text").case(error_handler, success_handler) == "E Error Text"
    assert Right("Success Text").case(error_handler, success_handler) == "S Success Text"



# Generated at 2022-06-14 03:17:20.849974
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Either(5) == Either(5)
    assert Either(5) != Either(6)
    assert Either(5) != 5
    assert Either(6) == Either(6)
    assert Either(6) != Either(5)
    assert Either(6) != 5


# Generated at 2022-06-14 03:17:23.676002
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Right('data').to_lazy() == Lazy(lambda: 'data')
    assert Left(ValueError('data')).to_lazy() == Lazy(lambda: ValueError('data'))



# Generated at 2022-06-14 03:17:32.080034
# Unit test for method case of class Either
def test_Either_case():

    l = Left("Monad is not functor")
    r = Right("Monad is functor")

    assert l.case(error=lambda x: x, success=lambda x: x) == "Monad is not functor"
    assert r.case(error=lambda x: x, success=lambda x: x) == "Monad is functor"



# Generated at 2022-06-14 03:17:35.352995
# Unit test for method case of class Either
def test_Either_case():
    assert Left(42).case(error=lambda n: n + 1, success=lambda n: n - 1) == 43
    assert Right(42).case(error=lambda n: n + 1, success=lambda n: n - 1) == 41

# Generated at 2022-06-14 03:17:39.527308
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)
    assert Left(1) != None


# Generated at 2022-06-14 03:17:44.494270
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Either.to_lazy(Right(5)) == Lazy(lambda: 5)



# Generated at 2022-06-14 03:17:48.564683
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.either import Left, Right

    assert Left(1).to_lazy() == Lazy(Left(1))
    assert Right(1).to_lazy() == Lazy(Right(1))

# Generated at 2022-06-14 03:17:50.549601
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(1).to_lazy().value() == 1
    assert Right(1).to_lazy().value() == 1

# Generated at 2022-06-14 03:17:58.060449
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Unit test for method to_lazy of class Either.

    :returns: Nothing
    :rtype: None
    """
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 10) == Left(10).to_lazy()
    assert Lazy(lambda: 10) == Right(10).to_lazy()


# Generated at 2022-06-14 03:18:09.022562
# Unit test for method to_lazy of class Either
def test_Either_to_lazy(): # pylint: disable=invalid-name
    """A code example of method to_lazy"""
    try:
        from pymonet.lazy import Lazy # pylint: disable=import-error

        def test():
            """Test function"""
            return Lazy(lambda: 1)

        assert test() == 1 # pylint: disable=no-value-for-parameter
        assert test() == 1
        assert test() == 1
        assert test() == 1
        return 0
    except AssertionError:
        print("A code example of method to_lazy")
        return 1



# Generated at 2022-06-14 03:18:13.090829
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    value = 10
    assert Lazy(lambda: value) == Either(value).to_lazy()


# Generated at 2022-06-14 03:18:16.537876
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    assert Right(1).to_lazy() == Lazy(lambda: 1)
    assert Left(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:18:18.870086
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    import operator

    assert Either(1).to_lazy().pure(operator.add, 5) == Lazy(lambda: 6)

# Generated at 2022-06-14 03:18:23.191396
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    # Given
    either = Either
    # When
    lazy_either = either.to_lazy()
    # Then
    assert isinstance(lazy_either, Either)
    assert lazy_either is either


# Generated at 2022-06-14 03:18:24.224868
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    # GIVEN/WHEN
    e = Right(lambda x: x+5)

    # THEN
    assert e.to_lazy().value()(0) == 5

# Generated at 2022-06-14 03:18:31.154638
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """Unit test for method to_lazy of class Either"""
    # given
    either_right = Right(123)
    either_left = Left(123)

    # when
    result_right = either_right.to_lazy()
    result_left = either_left.to_lazy()

    # then
    assert result_right() == 123
    assert result_left() == 123



# Generated at 2022-06-14 03:18:40.380894
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    import unittest

    from pymonet.lazy import Lazy

    class EitherToLazyTest(unittest.TestCase):
        def test_Right_to_lazy_should_return_Lazy_that_returns_previous_value(self):
            assert Right(1).to_lazy() == Lazy(lambda: 1)

        def test_Left_to_lazy_should_return_Lazy_that_returns_previous_value(self):
            assert Left(1).to_lazy() == Lazy(lambda: 1)

    unittest.main()



# Generated at 2022-06-14 03:18:42.559354
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(2).to_lazy().run() == 2



# Generated at 2022-06-14 03:18:46.241729
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Right(5).to_lazy() == Lazy(lambda: 5)
    assert Left(5).to_lazy() == Lazy(lambda: 5)


# Generated at 2022-06-14 03:18:48.300847
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert isinstance(Left('error').to_lazy(), Lazy)
    assert isinstance(Right('value').to_lazy(), Lazy)


# Generated at 2022-06-14 03:18:51.034142
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    assert Either(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:18:52.217765
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Either.right(10).to_lazy() == Lazy(lambda: 10)
    assert Either.left(10).to_lazy() == Lazy(lambda: 10)


# Generated at 2022-06-14 03:19:00.163174
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.box import Box
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(1).to_lazy() == Lazy(lambda: 1)
    assert Left(Box(1)).to_lazy() == Lazy(lambda: Box(1))
    assert Right(Box(1)).to_lazy() == Lazy(lambda: Box(1))
    assert Left(Try(1, is_success=False)).to_lazy() == Lazy(lambda: Try(1, is_success=False))
    assert Right(Try(1, is_success=True)).to_lazy() == Lazy(lambda: Try(1, is_success=True))

# Generated at 2022-06-14 03:19:07.929615
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_maybe import Maybe
    from pymonet.box import Box

    assert Lazy(lambda: 1) == Left(1).to_lazy()
    assert Lazy(lambda: 2) == Right(2).to_lazy()
    assert Lazy(lambda: 3).value() == 3


# Generated at 2022-06-14 03:19:22.513410
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe

    assert Either.Left(1).to_lazy() == Lazy(lambda: 1)
    assert Either.Right(1).to_lazy() == Lazy(lambda: 1)
    assert Maybe.just(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:19:31.580045
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """Test Either to_lazy method"""
    # pylint: disable=C0103
    assert Left("abc").to_lazy().force() == "abc"
    assert Right("abc").to_lazy().force() == "abc"


# Generated at 2022-06-14 03:19:40.763308
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    # Test with Right
    assert Right(42).to_lazy() == Lazy(lambda: 42)
    assert Right(42).to_lazy().get() == 42
    # Test with Left
    assert Left(42).to_lazy() == Lazy(lambda: 42)
    assert Left(42).to_lazy().get() == 42


# Generated at 2022-06-14 03:19:44.925977
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(2).to_lazy() == Lazy(lambda: 2)


# Generated at 2022-06-14 03:19:47.522309
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Either(5).to_lazy() == Lazy(5)


# Generated at 2022-06-14 03:19:50.053394
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left.unit(5).to_lazy().value() == 5
    assert Right.unit(5).to_lazy().value() == 5



# Generated at 2022-06-14 03:19:53.793434
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    either_right = Right(5)
    lazy_right = either_right.to_lazy()
    assert lazy_right.evaluate() == 5

# Generated at 2022-06-14 03:20:03.927801
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.box import Box
    from pymonet.monad_list import List

    assert Either.to_lazy(Right(2)).get() == 2
    assert Either.to_lazy(Left(2)).get() == 2
    assert Either.to_lazy(Try(2)).get() == 2
    assert Either.to_lazy(Box(2)).get() == 2
    l = List.from_iterable([2, 3, 4])
    assert Either.to_lazy(l).get() == [2, 3, 4]


# Generated at 2022-06-14 03:20:06.312053
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right('42').to_lazy().force() == '42'
    assert Left('42').to_lazy().force() == '42'



# Generated at 2022-06-14 03:20:11.541822
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    from pymonet.test_utils import assert_equals

    assert_equals((lambda: 5).to_box().to_lazy(), Lazy(lambda: 5))
    assert_equals((lambda: 'test').to_box().to_lazy(), Lazy(lambda: 'test'))
    assert_equals((lambda: 5.5).to_box().to_lazy(), Lazy(lambda: 5.5))



# Generated at 2022-06-14 03:20:15.006799
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.either import Right

    def add_two(value):
        return value + 2

    def add_three(value):
        return value + 3

    assert Lazy(lambda: 5) == Right(5).to_lazy()
    assert Lazy(lambda: 7) == Right(5).to_lazy().map(add_two)
    assert Lazy(lambda: 10) == Right(5).to_lazy().map(add_two).map(add_three)


# Generated at 2022-06-14 03:20:30.087603
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Either(4).to_lazy() == Lazy(lambda: 4)



# Generated at 2022-06-14 03:20:36.580785
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    To lazy should convert either to lazy.

    :returns: Nothing

    >>> from pymonet.monad_either import Either, Right, Left
    >>> from pymonet.lazy import Lazy
    >>> def test(): return 10
    >>> lazy = Lazy(test)
    >>> (Right(10) == Right(10)).to_lazy()
    Lazy(True)
    >>> (Right(10) == Left(10)).to_lazy()
    Lazy(False)
    >>> (Left(10) == Left(10)).to_lazy()
    Lazy(True)

    """
    pass


# Generated at 2022-06-14 03:20:41.006702
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    # When value is right
    right_value = Right(3)  # type: Either[int]
    assert right_value.to_lazy() == Lazy(lambda: 3)

    # When value is left
    left_value = Left("error")  # type: Either[str]
    assert right_value.to_lazy() == Lazy(lambda: "error")



# Generated at 2022-06-14 03:20:46.040578
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """Unit test for method to_lazy of class Either"""
    assert str(Right(1).to_lazy().value()) == str(Lazy(lambda: 1).value())
    assert str(Left(1).to_lazy().value()) == str(Lazy(lambda: 1).value())



# Generated at 2022-06-14 03:20:50.785131
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left('test').to_lazy() == Lazy(lambda: 'test')
    assert Right(42).to_lazy() == Lazy(lambda: 42)


# Generated at 2022-06-14 03:20:54.783373
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Right(5).to_lazy() == Lazy(lambda: 5)
    assert Left(5).to_lazy() == Lazy(lambda: 5)



# Generated at 2022-06-14 03:21:04.921543
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Either.to_lazy(Left('abc')) == Either.to_lazy(Left('abc'))
    assert Either.to_lazy(Left('abc')) is not Either.to_lazy(Left('abcd'))

    assert Either.to_lazy(Right('abc')) == Either.to_lazy(Right('abc'))
    assert Either.to_lazy(Right('abc')) is not Either.to_lazy(Right('abcd'))

    f = lambda x: x ** 2
    assert Either.to_lazy(Right(2)).map(f).value() == Either.to_lazy(Right(2)).map(f).value()
    assert Either.to_lazy(Right(2)).map(f) is not Either.to_lazy(Right(3)).map(f)

# Generated at 2022-06-14 03:21:09.599672
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left(None).to_lazy() == Lazy(lambda: None)
    assert Right(None).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:21:12.163962
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """Unit test for method to_lazy of class Either"""

    assert Right(2).to_lazy().value() == 2
    assert Left(2).to_lazy().value() == 2



# Generated at 2022-06-14 03:21:14.869748
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(3).to_lazy() == Lazy(lambda: 3)
    assert Left(3).to_lazy() == Lazy(lambda: 3)


# Generated at 2022-06-14 03:21:22.569721
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(1).to_lazy() == Lazy(lambda: 1)
    assert Left(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:21:25.689064
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 'test') == Either('test').to_lazy()

# Generated at 2022-06-14 03:21:28.933818
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    import pymonet.lazy
    def test_func():
        return 1
    assert pymonet.lazy.Lazy(test_func) == Right(42).to_lazy()


# Generated at 2022-06-14 03:21:33.388244
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    def is_equal(lazy: Lazy, expected):
        assert lazy.evaluate() == expected

    assert Right(1).to_lazy() == Lazy(lambda: 1)
    assert Left(2).to_lazy() == Lazy(lambda: 2)


# Generated at 2022-06-14 03:21:35.071438
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Right(12).to_lazy() == Lazy(lambda: 12)
    assert Left(12).to_lazy() == Lazy(lambda: 12)


if __name__ == '__main__':
    test_Either_to_lazy()

# Generated at 2022-06-14 03:21:36.628002
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(42).to_lazy() == Lazy(lambda: 42)
    assert Left(42).to_lazy() == Lazy(lambda: 42)



# Generated at 2022-06-14 03:21:42.056027
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    def actually_monad(value):
        return '{}!'.format(value)

    monad = Right(2)
    assert monad.to_lazy().bind(actually_monad).value == '2!'
    assert monad.bind(lambda x: Left(x)).to_lazy().bind(actually_monad).value == 2


# Generated at 2022-06-14 03:21:45.146727
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.box import Box

    assert Left('error').to_lazy() == Lazy(lambda: 'error')
    assert Right('value').to_lazy() == Lazy(lambda: 'value')


# Generated at 2022-06-14 03:21:48.891291
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(1).to_lazy().value() == 1
    assert Left("Error").to_lazy().value() == "Error"


# Generated at 2022-06-14 03:21:55.531421
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """Unit test for method to_lazy of class Either"""
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1) == Left(1).to_lazy()
    assert Lazy(lambda: 1) == Right(1).to_lazy()


# Generated at 2022-06-14 03:22:12.314452
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    # given
    either_right = Right(1)
    either_left = Left(1)

    # when
    lazy_right = either_right.to_lazy()
    lazy_left = either_left.to_lazy()

    # then
    assert lazy_right.value() == 1
    assert lazy_left.value() == 1



# Generated at 2022-06-14 03:22:14.184200
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(None).to_lazy().resolve() == None
    assert Right(None).to_lazy().resolve() == None


# Generated at 2022-06-14 03:22:24.940153
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(2).to_lazy() == Lazy(lambda: 2)
    assert Left(2).to_lazy() == Lazy(lambda: 2)


# Generated at 2022-06-14 03:22:31.953573
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    def l1(x):
        return x + 1

    def l2(x):
        return x + 2

    assert l2(l1(1)) == 4
    assert Left(1).to_lazy().bind(l1).bind(l2).value() == 4
    assert Right(1).to_lazy().bind(l1).bind(l2).value() == 4



# Generated at 2022-06-14 03:22:34.186845
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Either(42).to_lazy() == Lazy(lambda : 42)


# Generated at 2022-06-14 03:22:40.114082
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    import pymonet.lazy as lazy

    # Given
    right = Right(1)
    left = Left(1)

    # Then
    assert right.to_lazy().get_value() == 1
    assert left.to_lazy().get_value() == 1
    assert isinstance(right.to_lazy(), lazy.Lazy)
    assert isinstance(left.to_lazy(), lazy.Lazy)



# Generated at 2022-06-14 03:22:46.684373
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Right(5).to_lazy() == Left(5).to_lazy()
    assert Right(5).to_lazy().force() == Left(5).to_lazy().force()
    assert type(Right(5).to_lazy()) == Lazy == type(Left(5).to_lazy())

test_Either_to_lazy()


# Generated at 2022-06-14 03:22:49.814092
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    def fn():
        return 3
    assert Left(3).to_lazy() == Lazy(fn)
    assert Right(3).to_lazy() == Lazy(fn)


# Generated at 2022-06-14 03:22:52.708492
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    print(Right(42).to_lazy() == Lazy(lambda: 42), 'test_Either_to_lazy')



# Generated at 2022-06-14 03:22:55.884945
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    # GIVEN
    left = Left(3)
    right = Right('test')
    # WHEN
    value_left = left.to_lazy()
    value_right = right.to_lazy()
    # THEN
    assert value_left.value() == left
    assert value_right.value() == right


# Generated at 2022-06-14 03:23:15.058159
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Either(1).to_lazy() == Lazy(lambda: 1)
    assert Either(-1).to_lazy() == Lazy(lambda: -1)
    assert Either('test').to_lazy() == Lazy(lambda: 'test')
    assert Either('   test   ').to_lazy() == Lazy(lambda: '   test   ')
    assert Either(None).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:23:17.695060
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Test to_lazy method of class Either.
    """
    lazy = Right(23).to_lazy()
    assert lazy.value() == 23

# Generated at 2022-06-14 03:23:24.778537
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    # given
    monad = Right(5)

    # when
    val = monad.to_lazy().force()

    # then
    assert val == 5

    # given
    monad = Left(5)

    # when
    val = monad.to_lazy().force()

    # then
    assert val == 5

# Generated at 2022-06-14 03:23:35.511057
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Either(2).to_lazy() == Lazy(lambda: 2)


# Generated at 2022-06-14 03:23:38.884004
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Lazy(lambda: 1) == Either(1).to_lazy()
    assert Lazy(lambda: 1) == Right(1).to_lazy()
    assert Lazy(lambda: RuntimeError(1)) == Left(RuntimeError(1)).to_lazy()
    assert Lazy(lambda: Try(1)) == Right(Try(1)).to_lazy()



# Generated at 2022-06-14 03:23:49.682686
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """Ensure that Either can be transformed to Lazy."""
    from pymonet.maybe import Maybe
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try
    from pymonet.validation import Validation
    from pymonet.box import Box

    # Lazy
    assert Right(1).to_lazy() == Lazy(lambda: 1)
    assert Right(1).to_lazy().value() == 1

    # Maybe
    assert Right(1).to_lazy() == Lazy(lambda: Maybe.just(1))
    assert Right(1).to_lazy().value() == Maybe.just(1)

    # Try
    assert Right(1).to_lazy() == Lazy(lambda: Try(1, is_success=True))

# Generated at 2022-06-14 03:23:53.923485
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Either(10).to_lazy().value() == 10
    assert Either(None).to_lazy().value() is None


# Generated at 2022-06-14 03:23:57.958401
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(None).to_lazy() == Lazy(lambda: None)
    assert Right(None).to_lazy() == Lazy(lambda: None)

# Generated at 2022-06-14 03:24:01.534249
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left(2).to_lazy() == Lazy(None)
    assert Right(2).to_lazy() == Lazy(2)



# Generated at 2022-06-14 03:24:06.627354
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    def square_lazy(x):
        return x ** 2

    right_lazy = Right(10).to_lazy().map(square_lazy)
    assert isinstance(right_lazy, Lazy)
    assert right_lazy() == 100

    left_lazy = Left(10).to_lazy()
    assert isinstance(left_lazy, Lazy)
    assert left_lazy() == 10



# Generated at 2022-06-14 03:24:47.076381
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    assert Validation.success(0).to_lazy() == Lazy(lambda: 0)
    assert Validation.fail([None]).to_lazy() == Lazy(lambda: None)
    assert Validation.success(None).to_lazy() == Lazy(lambda: None)
    assert Validation.success(Right(None)).to_lazy() == Lazy(lambda: Right(None))
    assert Validation.fail([Right(None)]).to_lazy() == Lazy(lambda: Right(None))
    assert Validation.success(Left(None)).to_lazy() == Lazy(lambda: Left(None))

# Generated at 2022-06-14 03:24:50.284794
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Test to_lazy method of Either class.
    """

    # execute test
    result = Right(1).to_lazy()

    # assert
    assert 1 == result.value()



# Generated at 2022-06-14 03:25:00.109757
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet import LazyEvaluationError
    lazy = Either(True).to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.call() is True
    lazy = Either(False).to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.call() is False
    lazy = Either(Lazy(lambda: True)).to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.call() is True
    lazy = Either(Lazy(lambda: False)).to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.call() is False
    lazy = Either(Lazy(lambda: Lazy(lambda: True))).to_lazy()
    assert isinstance

# Generated at 2022-06-14 03:25:04.267052
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """Test either to_lazy method"""
    left = Left(1)
    assert left.to_lazy().value() is 1

    right = Right(1)
    assert right.to_lazy().value() is 1

# Generated at 2022-06-14 03:25:07.151834
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    import pymonet.lazy

    # test Left value
    data = Left(1)
    assert data.to_lazy().get() == data.value

    # test Right value
    data = Right(1)
    assert data.to_lazy().get() == data.value



# Generated at 2022-06-14 03:25:10.555038
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:25:17.414650
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """Test to_lazy method of class Either."""
    assert Left([1, 2, 3]).to_lazy().value() == [1, 2, 3]
    assert Right([1, 2, 3]).to_lazy().value() == [1, 2, 3]

# Generated at 2022-06-14 03:25:21.518927
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert isinstance(Left(Exception('fail')).to_lazy(), Lazy)
    assert isinstance(Right(1).to_lazy(), Lazy)

    assert Left(Exception('fail')).to_lazy().value() == Left(Exception('fail'))
    assert Right(1).to_lazy().value() == 1


# Generated at 2022-06-14 03:25:24.237090
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(2).to_lazy().get() == 2
    assert Left(2).to_lazy().get() == 2


# Generated at 2022-06-14 03:25:26.277243
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:26:41.990786
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.box import Box

    assert Either(Box(1)).to_lazy() == Either(Box(1)).value