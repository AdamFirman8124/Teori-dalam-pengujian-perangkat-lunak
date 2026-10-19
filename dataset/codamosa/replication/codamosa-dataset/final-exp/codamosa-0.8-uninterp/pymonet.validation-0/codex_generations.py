

# Generated at 2022-06-14 04:11:37.589230
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """Unit test for method to_lazy of class Validation"""
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    res = Validation.success(10).to_lazy()
    assert res.value() == 10
    assert res == Lazy(lambda: 10)
    assert res.map(lambda v: v + 1).value() == 11

    res = Validation.fail([2]).to_lazy()
    assert res.value() is None
    assert res == Lazy(lambda: None)
    assert res.map(lambda v: v + 1).value() is None


# Generated at 2022-06-14 04:11:44.096108
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.box import Box
    from pymonet.either import Left, Right
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try, Failure
    from pymonet.validation import Validation

    # Success
    validation = Validation.success('Hello!')
    assert Lazy(lambda: 'Hello!') == validation.to_lazy()

    validation = Validation.fail(['fail'])
    assert Lazy(lambda: None) == validation.to_lazy()

# Generated at 2022-06-14 04:11:49.662659
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.success(1).to_lazy().eval() == 1
    assert Validation.fail(['error']).to_lazy() == Lazy(lambda: None)
    assert Validation.fail(['error']).to_lazy().eval() is None


# Generated at 2022-06-14 04:11:58.771534
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try

    def calculate_sum(a, b):
        return a + b

    assert Validation.success('Hello').to_lazy() == Lazy(lambda: 'Hello')
    assert Validation.fail(['The number is to big']).to_lazy() == Lazy(lambda: None)
    assert Validation.success(42).to_lazy().map(lambda x: x + 2) == Lazy(lambda: 44)
    assert Validation.success(42).to_lazy().ap(Try(calculate_sum, is_success=True)) == Lazy(lambda: 84)
    assert Validation.success(42).to_lazy().bind(lambda x: Try(x + 2)) == Try(44)

# Generated at 2022-06-14 04:12:06.956280
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    success = Validation.success(2)
    lazy = success.to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy() == 2

    fail = Validation.fail(['error1', 'error2'])
    lazy = fail.to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.eval() == None

    assert success.to_lazy() == Lazy(lambda: success.value)
    assert fail.to_lazy() == Lazy(lambda: fail.value)



# Generated at 2022-06-14 04:12:08.319848
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail([1]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:12:09.758203
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    validation = Validation.success(10)

    assert validation.to_lazy() == Lazy(lambda: 10)

# Generated at 2022-06-14 04:12:13.942568
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    # Given
    validation = Validation.success('a')

    # When
    result = validation.to_lazy()

    # Then
    assert result.value() == 'a'


# Generated at 2022-06-14 04:12:21.828852
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    def fn():  # pragma: no cover
        return 'lazy value'

    validation = Validation.success(fn)
    lazy = validation.to_lazy()
    assert type(lazy) == Lazy
    assert lazy() == 'lazy value'


# Generated at 2022-06-14 04:12:26.166015
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    validation = Validation.success('success')
    lazy = validation.to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy.force() == 'success'



# Generated at 2022-06-14 04:12:31.236292
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def fn():
        return 'value'

    assert Validation.success(fn).to_lazy() == Lazy(fn)

# Generated at 2022-06-14 04:12:33.231143
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 2) == Validation.success(2).to_lazy()


# Generated at 2022-06-14 04:12:39.660800
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy(): # pragma: no cover
    from pymonet.lazy import Lazy

    lazy = Validation(123, []).to_lazy()

    assert isinstance(lazy, Lazy)
    assert isinstance(lazy.force(), int)
    assert lazy.force() == 123


# Generated at 2022-06-14 04:12:45.818000
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:12:50.212841
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def get_lazy_value(value):
        return Lazy(lambda: value)

    assert Validation.success(1).to_lazy() == get_lazy_value(1)
    assert Validation.fail(['error']).to_lazy() == get_lazy_value(None)


# Generated at 2022-06-14 04:12:52.540836
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    lazy = Validation.success(1).to_lazy()
    assert lazy.is_a(Lazy)
    assert lazy.value() == 1


# Generated at 2022-06-14 04:13:05.656055
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    def check():
        """
        Check that method returns Lazy monad.
        """
        assert_lazy = Lazy(lambda: Validation.success(123))
        assert isinstance(assert_lazy, Lazy)

    def check_evaluation():
        """
        Check that method returns Lazy monad and this monad has not been evaluated.
        """
        assert_lazy = Lazy(lambda: Validation.success(123))
        assert assert_lazy.is_evaluated() == False

    def check_monad_is_lazy():  # pragma: no cover
        """
        Check that method returns Lazy monad itself.
        """
        assert_lazy = Lazy(lambda: Validation.success(123))
       

# Generated at 2022-06-14 04:13:12.172681
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.validation import Validation

    lazy_validation = Validation.success('success').to_lazy()
    assert callable(lazy_validation.value)
    assert (lazy_validation.evaluate() == 'success')

    lazy_validation = Validation.fail(['fail']).to_lazy()
    assert callable(lazy_validation.value)
    assert (lazy_validation.evaluate() is None)


# Generated at 2022-06-14 04:13:15.548667
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Validation.success(2).to_lazy() == Lazy(lambda: 2)
    assert Validation.fail(['error']).to_lazy() == Lazy(lambda: None)

# Generated at 2022-06-14 04:13:21.839819
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    def f():
        return Try(10)

    lazy = f().to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.to_try() == Try(10)


# Generated at 2022-06-14 04:13:28.005461
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    def test():
        return 'test value'

    assert Validation.success(test).to_lazy().value() == 'test value'
    assert Validation.fail().to_lazy().value() is None


# Generated at 2022-06-14 04:13:33.012379
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Test method to_lazy of class Validation.
    """

    success_validation = Validation.success(1)
    result = success_validation.to_lazy().eval()
    assert result == 1

    failed_validation = Validation.fail([1])
    result = failed_validation.to_lazy().eval()
    assert result is None


# Generated at 2022-06-14 04:13:36.544673
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.valiadtion import Validation

    assert Validation(1, []).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 04:13:39.571930
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    assert Validation(1, ['error']).to_lazy() == Lazy(lambda: 1)
    assert Validation('1', []).to_lazy() == Lazy(lambda: '1')
    assert isinstance(Validation('1', []).to_lazy().f, Lazy)


# Generated at 2022-06-14 04:13:43.474905
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(2).to_lazy() == Lazy(lambda: 2)
    assert Validation.fail('error').to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 04:13:48.168739
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    assert Validation.success(2).to_lazy() == Lazy(lambda: 2)
    assert Validation.fail([]).to_lazy() == Lazy(lambda: None)

# Generated at 2022-06-14 04:13:51.253063
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    val = Validation.success(True).to_lazy()
    assert isinstance(val, Lazy)
    assert val.call()


# Generated at 2022-06-14 04:13:55.785780
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Test for method to_lazy of class Validation.
    """
    from pymonet.maybe import Maybe
    from pymonet.box import Box
    from pymonet.lazy import Lazy

    assert Validation.success('foo').to_lazy() == Lazy(lambda: 'foo')
    assert Validation.fail().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:13:59.061578
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    validation = Validation('test', [])
    lazy = validation.to_lazy()
    assertLazy(lazy, 'test')
    validation = Validation(None, ['error 1', 'error 2'])
    lazy = validation.to_lazy()
    assertLazy(lazy, None)


# Generated at 2022-06-14 04:14:06.651480
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """ Tests to_lazy method of Validation class. """
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    assert Validation.success('Test').to_lazy() == Lazy(lambda: 'Test')
    assert Validation.fail(['Error']).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:14:15.783609
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """Unit test for to_lazy method of Validation monad"""
    from pymonet.lazy import Lazy
    import pytest

    def test_with_success():
        """Unit test with successful validation"""
        validation = Validation.success(1)
        res = validation.to_lazy()
        assert isinstance(res, Lazy)
        assert res.thunk == validation.value

    def test_with_fail():
        """Unit test with failed validation"""
        validation = Validation.fail(['fail'])
        res = validation.to_lazy()
        assert isinstance(res, Lazy)
        assert res.thunk == validation.value

    test_with_success()
    test_with_fail()


# Generated at 2022-06-14 04:14:19.548826
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def fun():
        return 'DATA'

    lazy = Validation.success(fun).to_lazy()
    assert lazy == Lazy(fun)



# Generated at 2022-06-14 04:14:25.465007
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def lazy(value):
        def func():
            return value
        return Lazy(func)

    assert Validation.success('A').to_lazy() == lazy('A')
    assert Validation.fail(['A']).to_lazy() == lazy(None)


# Generated at 2022-06-14 04:14:29.663865
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def foo():
        return 'bar'

    assert Validation.success('bar').to_lazy().get() == foo()
    assert Validation.success('bar').to_lazy() == Lazy(foo)


# Generated at 2022-06-14 04:14:37.903900
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """Unit test for Validation.to_lazy()."""

    # pylint: disable=line-too-long
    import pytest
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail([]).to_lazy() == Lazy(lambda: None)
    assert Validation.fail([1]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:14:42.393823
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    validation = Validation.success(1)
    assert validation.to_lazy() == Lazy(lambda: 1)

    validation = Validation.fail()
    assert validation.to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:14:50.244609
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Run tests for method to_lazy of class Validation
    """
    from pymonet.lazy import Lazy, Operator
    from pymonet.either import Left, Right
    from pymonet.monad_try import Try

    val_success = Validation.success(4)
    val_fail = Validation.fail(['not valid'])
    assert val_success.to_lazy() == Lazy(lambda: 4)
    assert val_fail.to_lazy() == Lazy(lambda: None)
    assert Operator.bind(val_fail.to_lazy(), lambda x: Lazy(lambda: x*x)) == Lazy(lambda: None)
    assert Operator.bind(val_success.to_lazy(), lambda x: Lazy(lambda: x*x)) == Lazy(lambda: 16)

# Generated at 2022-06-14 04:14:54.934826
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    assert Validation.success(5).to_lazy() == Lazy(lambda: 5)
    assert Validation.fail([]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:14:58.462581
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    validation = Validation.success(42)
    lazy = validation.to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy.call() == 42


# Generated at 2022-06-14 04:15:02.398428
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def stub(x):
        return 'B'

    v = Validation(stub, [1, 2, 3])
    lazy = v.to_lazy()
    assert lazy == Lazy(stub)


# Generated at 2022-06-14 04:15:12.829856
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Unit test for method to_lazy of class Validation

    :returns: True when unit test is successful
    :rtype: Boolean
    """
    value = 1
    validation = Validation.success(value)

    lazy = validation.to_lazy()

    return lazy.value() == value


# Generated at 2022-06-14 04:15:16.486642
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    lazy_f = lambda: 1
    lazy = Validation.success().to_lazy()

    assert lazy.f == lazy_f

# Generated at 2022-06-14 04:15:22.925939
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    validation = Validation.success(5).to_lazy()
    assert isinstance(validation, Lazy)
    assert validation.get() == 5
    assert validation.get() == 5

    validation = Validation.fail([1, 2, 3]).to_lazy()
    assert isinstance(validation, Lazy)
    assert validation.get() is None
    assert validation.get() is None


# Generated at 2022-06-14 04:15:26.716248
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    assert Validation(42, []).to_lazy() == Lazy(lambda: 42)
    assert Validation(None, [1, 2, 3]).to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 04:15:31.968684
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Test Validation.to_lazy method.
    """
    from pymonet.maybe import Maybe
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy
    assert Validation.success(Maybe.just(1)).to_lazy() == Lazy(lambda: Maybe.just(1))
    assert Validation.fail(Try.failure(1)).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:15:34.661101
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    def f():
        return 3 + 3

    assert Validation.success(f).to_lazy().get() == f()
    assert Validation.fail().to_lazy().get() is None

# Generated at 2022-06-14 04:15:35.740875
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(3).to_lazy() == Lazy(lambda: 3)


# Generated at 2022-06-14 04:15:40.911857
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def create_lazy_val_with_value(val):
        return Lazy(lambda: val)

    val = Validation.success(1)
    val_lazy = val.to_lazy()

    assert val_lazy == create_lazy_val_with_value(1)


# Generated at 2022-06-14 04:15:43.639950
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    def fn():
        return 'success'

    validation = Validation.success().to_lazy().map(fn).value()

    assert validation == 'success'


# Generated at 2022-06-14 04:15:48.459147
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    print('Unit test for method to_lazy of class Validation')
    from pymonet.lazy import Lazy

    validation = Validation(1, [])
    lazy_monad = validation.to_lazy()
    assert(isinstance(lazy_monad, Lazy))
    assert(1 == lazy_monad.value())
    print('... ok')


# Generated at 2022-06-14 04:16:09.220032
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Test method to_lazy of class Validation.
    """
    from pymonet.lazy import Lazy

    # Test for successful Validation
    val = Validation.success(2)
    assert isinstance(val.to_lazy(), Lazy)
    assert val.to_lazy() == Lazy(lambda: 2)

    # Test for failed Validation
    val = Validation.fail(['Error'])
    assert isinstance(val.to_lazy(), Lazy)
    assert val.to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:16:13.917410
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail([1]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:16:17.306286
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    lazy = Lazy(lambda: 'test')
    validation = Validation(lazy, [])

    assert validation.to_lazy() == lazy

# Generated at 2022-06-14 04:16:19.647164
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 04:16:24.593421
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    validation = Validation.success(1)
    assert isinstance(validation.to_lazy(), Lazy)
    assert validation.to_lazy().get() == 1


# Generated at 2022-06-14 04:16:33.570476
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Unit test for method to_lazy of class Validation.
    """
    from pymonet.box import Box
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    validation = Validation.success(23)
    lazy_monad = Lazy(lambda: 23)
    try_monad = Try(23, is_success=True)
    box_monad = Box(23)

    # Test with successful Validation
    assert validation.to_lazy() == Lazy(lambda: 23)
    assert validation.to_lazy() == lazy_monad
    assert validation.to_lazy() == try_monad
    assert validation.to_lazy() == box_monad

    # Test with failed Validation

# Generated at 2022-06-14 04:16:42.284547
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from unittest import TestCase, main

    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    class TestValidationToLazy(TestCase):

        def test_success_Validation_to_lazy(self):
            validation = Validation.success('value')
            lazy = validation.to_lazy()
            self.assertEqual(
                Lazy(lambda: 'value'),
                lazy
            )

        def test_fail_Validation_to_lazy(self):
            validation = Validation.fail(['error'])
            lazy = validation.to_lazy()
            self.assertEqual(
                Lazy(lambda: None),
                lazy
            )

    main()


# Generated at 2022-06-14 04:16:46.328326
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """Unit test for method to_lazy of class Validation"""

    from pymonet.lazy import Lazy

    lazy = Validation.success(1).to_lazy()
    assert lazy.value() == 1
    assert isinstance(lazy, Lazy)


# Generated at 2022-06-14 04:16:55.355242
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    success_lazy = Lazy(lambda: 'success')
    fail_lazy = Lazy(lambda: 'fail')

    # when Validation is successful
    validation = Validation.success(success_lazy)
    # then lazy is transformed to Maybe
    assert validation.to_lazy() == success_lazy

    # when Validation is failed
    validation = Validation.fail(fail_lazy)
    # then lazy is transformed to Maybe
    assert validation.to_lazy() == fail_lazy


# Generated at 2022-06-14 04:17:01.721275
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.box import Box
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe
    from pymonet.monad_try import Try

    val_1 = Validation.success('Some value')
    val_2 = Validation.fail(['Some error'])

    assert val_1.to_lazy() == Lazy(lambda: 'Some value')
    assert val_2.to_lazy() == Lazy(lambda: None)

# Generated at 2022-06-14 04:17:35.352777
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """Unit test for method to_lazy of class Validation"""
    from pymonet.lazy import Lazy
    lazy_instance = Lazy(lambda: "hello")
    assert Validation.success('hello').to_lazy() == lazy_instance
    assert Validation.fail('some error').to_lazy() == lazy_instance


# Generated at 2022-06-14 04:17:42.479003
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Unit test for method to_lazy of class Validation
    """
    from pymonet.lazy import Lazy

    def validator(value):
        if value.startswith('a'):
            return Validation.success(value.upper())
        return Validation.fail(['Value must start from letter a!'])

    assert Lazy(lambda: 'abc').bind(lambda x: validator(x).to_lazy()).force() == Validation.success('ABC')
    assert Lazy(lambda: '123').bind(lambda x: validator(x).to_lazy()).force() == Validation.fail(['Value must start from letter a!'])

# Generated at 2022-06-14 04:17:44.653015
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def func():
        return 42

    assert Validation.success(func).to_lazy() == Lazy(func)
    assert Validation.success(42).to_lazy() == Lazy(lambda: 42)


# Generated at 2022-06-14 04:17:47.546070
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success('Hello').to_lazy() == Lazy(lambda: 'Hello')
    assert Validation.fail(['World']).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:17:49.881234
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 04:17:52.062910
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success("A").to_lazy() == Lazy("A")


# Generated at 2022-06-14 04:17:54.972922
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    It check that method to_lazy returns correct monad.
    """
    from pymonet.lazy import Lazy

    assert Validation.success('a').to_lazy() == Lazy(lambda: 'a')


# Generated at 2022-06-14 04:17:57.032468
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    validation = Validation.success(42)
    lazy = validation.to_lazy()
    assert lazy.__class__.__name__ == 'Lazy' and lazy.func() == 42

# Generated at 2022-06-14 04:17:59.891266
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation(10, []).to_lazy() == Lazy(lambda: 10)
    assert Validation(None, []).to_lazy() == Lazy(lambda: None)
    assert Validation('error', ['aaa']).to_lazy() == Lazy(lambda: 'error')

# Generated at 2022-06-14 04:18:03.630274
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    validation = Validation.success(1)

    result = validation.to_lazy()
    assert isinstance(result, Lazy)
    assert result.value() == 1


# Generated at 2022-06-14 04:19:05.864153
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    def my_func(a):
        return a

    validation = Validation.success(2)
    assert validation.to_lazy().__call__(callback=my_func) == 2



# Generated at 2022-06-14 04:19:10.223409
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    assert Validation.success(3).to_lazy() == Lazy(lambda: 3)
    assert Validation.fail([1, 2]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:19:17.465591
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    val_success = Validation.success(10)
    val_fail = Validation.fail([10, 20])
    assert val_success.to_lazy() == Lazy(lambda: 10)
    assert val_fail.to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:19:20.006368
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success('anything').to_lazy().get() == 'anything'
    assert Validation.fail(['anything']).to_lazy() is None


# Generated at 2022-06-14 04:19:23.841893
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:19:27.172623
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def test_success_lazy_value_is_validation_value():
        unit = Validation.success(1)
        success_lazy_value = unit.to_lazy().get()
        assert success_lazy_value == unit.value


# Generated at 2022-06-14 04:19:31.220031
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1) == Validation.success(1).to_lazy()
    assert Lazy(lambda: None) == Validation.fail([1]).to_lazy()


# Generated at 2022-06-14 04:19:38.466008
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    def test_mapper(value):
        return value

    lazy = Validation.success(5).to_lazy()
    assert lazy.map(test_mapper) == Lazy(lambda: 5)

    lazy = Validation.fail([1, 2, 3]).to_lazy()
    assert lazy.map(test_mapper) == Lazy(lambda: None)


# Generated at 2022-06-14 04:19:41.650374
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation(10, []).to_lazy() == Lazy(lambda: 10)

    def f():
        return None

    assert Validation(None, [1]).to_lazy() == Lazy(f)

# Generated at 2022-06-14 04:19:47.926033
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail(errors=[1, 2]).to_lazy() == Lazy(lambda: None)
