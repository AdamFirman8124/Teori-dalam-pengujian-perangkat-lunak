

# Generated at 2022-06-14 04:11:39.262218
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    lazy_1 = Validation.success('success').to_lazy()
    assert lazy_1 == Lazy(lambda: 'success')

    lazy_2 = Validation.success().to_lazy()
    assert lazy_2 == Lazy(lambda: None)

    lazy_3 = Validation.fail(['errors']).to_lazy()
    assert lazy_3 == Lazy(lambda: None)



# Generated at 2022-06-14 04:11:44.525145
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """Unit test for method to_lazy of class Validation"""

    # Test to_lazy with success Validation
    val = Validation.success('content')
    assert val.to_lazy() == Lazy(lambda: 'content')

    # Test to_lazy with fail Validation
    val = Validation.fail(['error'])
    assert val.to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 04:11:49.369398
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    def test_success():
        assert Validation.success(2).to_lazy() == Lazy(lambda: 2)

    def test_fail():
        assert Validation.fail([2]).to_lazy() == Lazy(lambda: None)

    test_success()
    test_fail()



# Generated at 2022-06-14 04:11:51.375511
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    assert Validation.success('abc').to_lazy() == Lazy(lambda: 'abc')

# Generated at 2022-06-14 04:11:57.135133
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(5).to_lazy() == Lazy(lambda: 5)
    assert Validation.fail([1]).to_lazy() == Lazy(lambda: None)
    assert Validation.success(True).to_lazy() == Lazy(lambda: True)
    assert Validation.fail([1, 2, 3]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:12:02.517645
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Unit test for method to_lazy of class Validation.
    """
    from pymonet.lazy import Lazy

    assert Validation(True, []).to_lazy() == Lazy(lambda: True)
    assert Validation(3.14, []).to_lazy() == Lazy(lambda: 3.14)
    assert Validation("test", []).to_lazy() == Lazy(lambda: "test")


# Generated at 2022-06-14 04:12:07.449273
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.success(EqualityTestClass(2)).to_lazy() == Lazy(lambda: EqualityTestClass(2))
    assert Validation.fail([TypeError('abc')]).to_lazy() == Lazy(lambda: ValueError('abc'))

# Generated at 2022-06-14 04:12:10.079511
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1) == Validation.success(1).to_lazy()
    assert Lazy(lambda: None) == Validation.fail([]).to_lazy()


# Generated at 2022-06-14 04:12:13.468339
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    def test_Function():
        return 1

    assert Validation.success(1).to_lazy().value() == test_Function()


# Generated at 2022-06-14 04:12:15.616933
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    return Validation(4, []).to_lazy().eval() == 4


# Generated at 2022-06-14 04:12:22.379007
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    validation = Validation.success('spam')
    assert validation.to_lazy() == Lazy(lambda: 'spam')


# Generated at 2022-06-14 04:12:25.731420
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def some_fun():
        return 1

    lazy = Validation.success(some_fun).to_lazy()

    assert lazy == Lazy(some_fun)


# Generated at 2022-06-14 04:12:28.082313
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(5).to_lazy() == Lazy(lambda: 5)

# Unit tests for method to_try of class Validation

# Generated at 2022-06-14 04:12:32.921338
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """Unit test for method to_lazy of class Validation."""
    assert Validation.success(1).to_lazy().lazy_func() == 1
    assert Validation.success(1).to_lazy().is_lazy_empty() is False


# Generated at 2022-06-14 04:12:37.059713
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    def test_func():
        return 1

    lazy_monad = Validation.success(test_func).to_lazy()
    assert lazy_monad.value() == 1

# Generated at 2022-06-14 04:12:42.229652
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try, Success, Failure
    from pymonet.validation import Validation
    assert Validation.success(100).to_lazy() == Lazy(lambda: 100)
    assert Validation.fail(100).to_lazy() == Lazy(lambda: None)

# Generated at 2022-06-14 04:12:48.473903
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Transformation to Lazy monad works correctly.
    """
    from pymonet.lazy import Lazy

    def get_value(value):
        return Validation(value, [])

    lazy_validation = Lazy(lambda: Validation('Success', []))

    assert lazy_validation.value() == Validation('Success', [])
    assert lazy_validation.map(lambda x: x.value).value() == 'Success'
    assert get_value('Success').to_lazy().value() == 'Success'


# Generated at 2022-06-14 04:12:50.672443
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 04:12:57.411725
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.functions import maybe
    from pymonet.functions import unit
    from pymonet.func_to_monad import to_lazy
    from pymonet.lazy import Lazy

    def lazy_function():
        return True

    def fullfilled_function(value):
        return value

    def empty_function():
        return []

    assert Validation.success(True).ap(to_lazy(lazy_function)).ap(to_lazy(fullfilled_function)) == Validation.success(True)
    assert Validation.success('value').ap(to_lazy(empty_function)).ap(to_lazy(fullfilled_function)) == Validation.fail([])

# Generated at 2022-06-14 04:13:01.402963
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    validation = Validation.success(1)
    assert validation.to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 04:13:07.376222
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    validation = Validation.success(42)
    assert validation.to_lazy() == Lazy(lambda: 42)

    validation = Validation.fail([1, 2, 3])
    assert validation.to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:13:15.253448
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.either import Right
    from pymonet.monad_try import Success

    assert Validation(Right(Lazy(lambda: 'x')), []).to_lazy() == Lazy(lambda: Right(Lazy(lambda: 'x')))
    assert Validation.fail([]).to_lazy() == Lazy(lambda: None)
    assert Validation(Success('x'), []).to_lazy() == Lazy(lambda: Success('x'))
    assert Validation.fail(['x']).to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 04:13:20.432408
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """Unit test for method to_lazy of class Validation."""
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 04:13:28.971475
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Test method to_lazy of class Validation.
    """
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    # Case 1: successful validation
    result = Validation.success(True)
    assert result.to_lazy() == Lazy(lambda: True)

    # Case 2: failed validation
    result = Validation.fail()
    assert result.to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:13:30.745637
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.box import Box

    assert Validation.success('test').to_lazy() == Lazy(lambda: Box('test'))


# Generated at 2022-06-14 04:13:38.010473
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Unit test for method to_lazy of class Validation

    :returns: None
    """
    def test_function():
        return 'Hello world!'

    validation = Validation.success(test_function)

    assert validation.is_success()
    assert validation.value == test_function
    assert validation.errors == []
    assert validation.to_lazy() == Lazy(test_function)


# Generated at 2022-06-14 04:13:42.488455
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():

    @lazy
    def lazy_val(): return Validation.success(1)
    assert lazy_val.get() == Validation.success(1)

    @lazy
    def lazy_val2(): return Validation.fail([1])
    assert lazy_val2.get() == Validation.fail([1])
    assert lazy_val2.is_success() is False


# Generated at 2022-06-14 04:13:46.417475
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.fail('not empty').to_lazy() == Lazy(lambda: None)
    assert Validation.success('empty').to_lazy() == Lazy(lambda: 'empty')



# Generated at 2022-06-14 04:13:51.055926
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    success = Validation.success(7)
    try:
        result = success.to_lazy()
        assert result.eval() == 7
    except Exception as e:
        print('Error: {}'.format(e))
        assert False
    finally:
        print('test_Validation_to_lazy OK!')


# Generated at 2022-06-14 04:13:56.243029
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    lazy_success = Validation.success(3).to_lazy()
    lazy_fail = Validation.fail([Error()]).to_lazy()

    assert isinstance(lazy_success, Lazy)
    assert isinstance(lazy_fail, Lazy)
    assert lazy_success.run() == 3
    assert lazy_fail.run() is None


# Generated at 2022-06-14 04:14:03.769838
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Unit test for method to_lazy of class Validation.
    """
    from pymonet.monad_try import Try

    assert Validation.success('success').to_lazy() == Lazy(lambda: 'success')
    assert Validation.fail().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:14:10.839342
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.box import Box
    from pymonet.monad_validation import Validation
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    lazy = Validation.success(Box(42)).to_lazy()

    assert isinstance(lazy, Lazy)
    assert isinstance(lazy.value(), Try)
    assert lazy.value().is_success
    assert lazy.value().value == Box(42)

# Generated at 2022-06-14 04:14:14.796413
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    validation = Validation.success(1)
    lazy = validation.to_lazy()
    assert lazy.value() == validation.value
    assert lazy.with_default(0) == validation.value
    assert lazy.with_default(0) == validation.value

    validation = Validation.fail([1])
    lazy = validation.to_lazy()
    assert lazy.value() == validation.value
    assert lazy.with_default(0) == 0
    assert lazy.with_default(0) == 0


# Generated at 2022-06-14 04:14:24.983235
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Test that to_lazy method of Validation transform Validation to Lazy.
    """
    from pymonet.lazy import Lazy

    # Successful validation
    successful_validation = Validation.success(10)
    lazy = successful_validation.to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy.__value__() == 10

    # Failed validation
    failed_validation = Validation.fail([])
    lazy = failed_validation.to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy.__value__() is None

# Generated at 2022-06-14 04:14:31.474183
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    """Unit test for method to_lazy of class Validation"""
    success_value = Validation.success(1)
    lazy_success = success_value.to_lazy()
    assert lazy_success.get() == 1

    fail_value = Validation.fail([])
    lazy_fail = fail_value.to_lazy()
    assert lazy_fail.get() is None

# Generated at 2022-06-14 04:14:35.920856
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Unit test for method to_lazy of class Validation
    """
    from pymonet.lazy import Lazy

    lazy = Lazy(lambda: 5)
    assert Validation.success(5).to_lazy() == lazy


# Generated at 2022-06-14 04:14:41.096423
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    def inc(x):
        return x + 1

    x = Validation.success(1)
    y = Validation.fail([1, 2])
    assert x.to_lazy().map(inc) == Lazy(lambda: 2)
    assert y.to_lazy().map(inc) == Lazy(lambda: None)


# Generated at 2022-06-14 04:14:52.175270
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.functions import compose

    # given
    val_str = Validation.success('123')
    val_int = Validation.success(123)

    # when
    result1 = val_str.to_lazy().map(lambda x: x + '123').get()
    result2 = val_str.to_lazy().map(len).get()
    result3 = val_int.to_lazy().map(lambda x: x + 123).get()
    result4 = val_int.to_lazy().bind(lambda x: Validation.success(x + 123)).get()
    result5 = compose(
        val_int.to_lazy(),
        lambda x: x + 123,
        lambda y: y + y,
        lambda z: z - 1,
    ).get()

    # then

# Generated at 2022-06-14 04:14:58.932013
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """It tests to_lazy method of Validation class"""

    from pymonet.lazy import Lazy

    success_validation = Validation.success(1)
    fail_validation = Validation.fail(['error'])

    #
    # to_lazy method
    #

    assert success_validation.to_lazy() == Lazy(lambda: 1)
    assert fail_validation.to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:15:00.789216
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy(): # pragma: no cover
    from pymonet.lazy import Lazy

    valid = Validation.success(2)
    lazy = valid.to_lazy()

    assert lazy == Lazy(lambda: 2)
    assert lazy.force() == 2


# Generated at 2022-06-14 04:15:05.071163
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    When: call to_lazy method on Validation
    Then: returns Lazy monad with function returning Validation value
    """

    # Given
    validation = Validation('Validation', [])

    # When
    result = validation.to_lazy()

    # Then
    assert isinstance(result, Lazy)
    assert result.value() == 'Validation'


# Generated at 2022-06-14 04:15:12.864426
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.box import Box
    from pymonet.lazy import Lazy

    def add_two(a):
        return a + 2

    def multiply_two(a):
        return a * 2

    def divide_two(a):
        return a / 2

    def return_lazy_value(a):
        return Lazy(lambda: a)

    v1 = Validation.success(10)

    result = v1.map(add_two).\
        map(multiply_two).\
        map(divide_two).\
        map(return_lazy_value)

    assert result.value() == Box(10)


# Generated at 2022-06-14 04:15:21.716257
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    import pymonet.lazy
    import pymonet.lazy
    from pymonet.validation import Validation

    def function(a):
        return a*2

    def other_function():
        return Validation.success(function(2))

    assert Validation.success(2).to_lazy() == pymonet.lazy.Lazy(function)(2)
    assert Validation.success(2).to_lazy().flat_map(pymonet.lazy.Lazy(other_function)) == pymonet.lazy.Lazy(Validation.success)(4)


# Generated at 2022-06-14 04:15:27.741412
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    It is used to test to_lazy method of Validation class.
    """
    from pymonet.lazy import Lazy

    def fn():
        return 'Hello World!'

    validation_success = Validation.success(fn())
    validation_fail = Validation.fail()

    lazy_success = validation_success.to_lazy()
    lazy_fail = validation_fail.to_lazy()

    assert isinstance(lazy_success, Lazy)
    assert isinstance(lazy_fail, Lazy)
    assert lazy_success() == lazy_success.value
    assert lazy_fail() is None
    assert lazy_success() == fn()
    assert lazy_success.value == 'Hello World!'
    assert lazy_fail.value is None


# Generated at 2022-06-14 04:15:29.432249
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 04:15:33.444999
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    validation = Validation.success(2)
    assert validation.to_lazy() == Lazy(lambda: 2)

    validation = Validation.fail()
    assert validation.to_lazy() == Lazy(lambda: None)

# Generated at 2022-06-14 04:15:39.260426
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.box import Box
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail([1, 2, 3]).to_lazy() == Lazy(lambda: None)
    assert Validation.success(Box(1)).to_lazy() == Lazy(Box(1))


# Generated at 2022-06-14 04:15:42.553511
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    validation = Validation.success(42)

    lazy = validation.to_lazy()

    assert lazy == Lazy(lambda: 42)


# Generated at 2022-06-14 04:15:46.058437
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    validation = Validation.success(1)
    assert validation.to_lazy() == Lazy(lambda: 1)

    validation = Validation.fail()
    assert validation.to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:15:48.929188
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    lazy = Validation.success(10).to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.get() == 10

    lazy = Validation.fail([0, 1]).to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.get() is None



# Generated at 2022-06-14 04:15:54.641353
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    # Setup
    def calc():
        return 5

    # Exercise
    result = Validation.success(5).to_lazy()

    # Verify
    assert result.value() == Validation.success(5).value


# Generated at 2022-06-14 04:15:57.035244
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(1).to_lazy().get() == 1
    assert Validation.fail().to_lazy().get() == None


# Generated at 2022-06-14 04:16:03.535708
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    It take 2 validations and transform them to Lazy monads.
    Running lazy monads return value of validations.
    """
    from pymonet.lazy import Lazy

    assert Validation.success('value').to_lazy() == Lazy(lambda: 'value')
    assert Validation.fail(['error']).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:16:07.885880
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    def result():
        return 'result'

    assert Validation.success('result').to_lazy() == Lazy(result)
    assert Validation.fail(['sad']).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:16:10.260919
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """Test successful case."""
    validation = Validation.success(1)
    assert validation.to_lazy().get() == 1


# Generated at 2022-06-14 04:16:13.874762
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert_that(
        Validation.success('data').to_lazy(),
        equal_to(Lazy(lambda: 'data'))
    )

# Generated at 2022-06-14 04:16:20.233789
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def test_method(self, expected_result):
        self.assertEqual(Lazy(lambda: 30), expected_result)
        self.assertEqual(Lazy(lambda: None), expected_result)

    Validation.test_to_lazy = test_method
    Validation.test_to_lazy(Validation.success(30), Lazy(lambda: 30))
    Validation.test_to_lazy(Validation.fail(30), Lazy(lambda: None))

# Generated at 2022-06-14 04:16:23.488922
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(2).to_lazy() == Lazy(lambda: 2)


# Generated at 2022-06-14 04:16:27.235067
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Lazy(lambda: "a") == Validation.success("a").to_lazy()


# Generated at 2022-06-14 04:16:30.240466
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    val = Validation.success(1)
    v = val.to_lazy()
    assert v.value()

    val = Validation.fail()
    v = val.to_lazy()
    assert v.value() is None


# Generated at 2022-06-14 04:16:37.497272
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Unit test for method to_lazy of class Validation.
    """
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.success(None).to_lazy() == Lazy(lambda: None)
    assert Validation.fail([1, 2]).to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 04:16:44.236152
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail([1, 2]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:16:50.331251
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.box import Box
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    unit = lambda x: x
    assert Lazy(unit).fmap(lambda x: x + 10).value() == 10
    assert Lazy(unit).fmap(lambda x: Box(x + 10)).fmap(lambda x: x.value()).value() == 10
    assert Lazy(unit).fmap(lambda x: Box(Try(lambda: x + 10))).bind(lambda box: box.value()).value() == 10

# Generated at 2022-06-14 04:16:53.540122
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Validation(1, []).to_lazy() == Lazy(lambda: 1)
    try:
        assert Validation(1, [2]).to_lazy() == Lazy(lambda: 1)
    except Exception:
        pass


# Generated at 2022-06-14 04:16:57.756849
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    lazy = Validation(1, []).to_lazy()

    assert isinstance(lazy, Lazy)

    assert lazy() == 1



# Generated at 2022-06-14 04:17:03.159111
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.box import Box
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    validation = Validation.fail(['error'])
    assert validation.is_fail()
    assert validation.to_lazy() == Lazy()

    validation = Validation.success('value')
    assert validation.is_success()
    assert validation.to_lazy() == Lazy(lambda: 'value')


# Generated at 2022-06-14 04:17:07.783565
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def sum_one(x):
        return x + 1

    lazy_value = Validation.success(0).to_lazy()
    assert lazy_value.map(sum_one) == Lazy(sum_one)(0)



# Generated at 2022-06-14 04:17:14.137480
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.box import Box
    from pymonet.monad_try import Try

    assert Validation.success().to_lazy() == Lazy(lambda : None)
    assert Validation.success('Successful value').to_lazy() == Lazy(lambda : 'Successful value')
    assert Validation.fail().to_lazy() == Lazy(lambda : None)
    assert Validation.fail().to_lazy() == Lazy(lambda : None)


# Generated at 2022-06-14 04:17:20.615253
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Test method to_lazy of class Validation.
    """
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    lazy = Validation.success(42).to_lazy()
    assert lazy == Lazy(lambda: 42)
    assert lazy.force() == Try(42, is_success=True)



# Generated at 2022-06-14 04:17:24.500525
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    expected = Lazy(lambda: 'test')
    actual = Validation.success('test').to_lazy()
    assert(expected == actual)


# Generated at 2022-06-14 04:17:30.814806
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    validation = Validation.success(12)
    lazy = validation.to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy.get() == 12

    validation = Validation.fail([1, 2])
    lazy = validation.to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy.get() is None



# Generated at 2022-06-14 04:17:33.687931
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.fail(['error']).to_lazy() == Lazy(lambda: None)
    assert Validation.success('test').to_lazy() == Lazy(lambda: 'test')


# Generated at 2022-06-14 04:17:37.272950
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 10) == Validation.success(10).to_lazy()
    assert Lazy(lambda: None) == Validation.fail().to_lazy()

# Generated at 2022-06-14 04:17:40.247020
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail().to_lazy() == Lazy(lambda: None)

# Generated at 2022-06-14 04:17:46.161724
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy
    from pymonet.box import Box
    from pymonet.monad_list import List

    assert Validation.success('Test').to_lazy() == Lazy(lambda: 'Test')
    assert Validation.fail().to_lazy() == Lazy(lambda: None)
    assert Validation.success(Lazy(lambda: 3)).to_lazy() == Lazy(lambda: 3)
    assert Validation.success(Box(3)).to_lazy() == Lazy(lambda: 3)
    assert Validation.success(Try(3)).to_lazy() == Lazy(lambda: 3)
    assert Validation.success(List('Test')).to_lazy() == Lazy(lambda: 'Test')



# Generated at 2022-06-14 04:17:52.502820
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Test: Validation.to_lazy
    Given: Validation with value="x" and empty errors
    When: call to_lazy on Validation
    Then: should return Lazy with function returning "x"
    """
    actual = Validation.success('x').to_lazy()
    assert isinstance(actual, Lazy)
    assert actual.unbox() == 'x'


# Generated at 2022-06-14 04:17:56.292402
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():

    def test_function():
        return 2

    # If Validation has no errors
    assert Validation.success(test_function()).to_lazy().get_value() == 2

    # If Validation has errors
    assert Validation.fail(["Error 1", "Error 2"]).to_lazy().get_value() == None


# Generated at 2022-06-14 04:18:01.034108
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """Test it should return Lazy with Validation value"""
    from pymonet.lazy import Lazy

    # Given
    validation = Validation(1, [])

    # When
    lazy = validation.to_lazy()

    # Then
    assert Lazy(lambda: 1) == lazy


# Generated at 2022-06-14 04:18:05.361816
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail(errors=[1, 2, 3]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:18:10.340065
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    def times3(a):
        return a * 3

    def times5(a):
        return a * 5

    assert Validation.success(10).to_lazy().map(times3).map(times5).get() == 150
    assert Validation.success(10).to_lazy() == Lazy(lambda: 10)



# Generated at 2022-06-14 04:18:26.754141
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.maybe import Maybe
    from pymonet.box import Box
    from pymonet.either import Either
    from pymonet.monad_try import Try

    validation = Validation.success('test')
    assert validation == validation.to_lazy().eval()

    validation = Validation.success(None)
    assert validation == validation.to_lazy().eval()

    validation = Validation.fail(['error'])
    assert validation == validation.to_lazy().eval()

    assert Maybe.just(None) == Maybe.from_value(validation.to_lazy().eval())
    assert Maybe.from_value(validation.to_lazy().eval()) == Maybe.from_value(validation.to_lazy().eval())

    assert validation.to_lazy().eval() == Box.from_value

# Generated at 2022-06-14 04:18:33.466257
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    def _test_to_lazy_method(validation, expected_value):
        lazy_value = validation.to_lazy().get_value()
        assert lazy_value == expected_value

    _test_to_lazy_method(Validation.success(10), 10)
    _test_to_lazy_method(Validation.success([1, 2, 3]), [1, 2, 3])
    _test_to_lazy_method(Validation.fail([10, 20, 30]), None)


# Generated at 2022-06-14 04:18:39.709350
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    lazy = Validation.success('abc').to_lazy()
    assert isinstance(lazy, Lazy) and lazy() == 'abc'

    lazy = Validation.fail(['error1', 'error2']).to_lazy()
    assert isinstance(lazy, Lazy) and lazy() == None



# Generated at 2022-06-14 04:18:43.546370
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    try_success = Try(1)
    lazy = Lazy(lambda: try_success)
    assert lazy == Validation.success(1).to_lazy()
    assert lazy != Validation.fail([1]).to_lazy()

# Generated at 2022-06-14 04:18:50.844356
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try
    from pymonet.validation import Validation

    # Success Validation
    assert Validation.success('value').to_lazy() == Lazy(lambda: 'value')

    # Failed Validation
    assert Validation.fail().to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 04:18:53.413766
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    fn = lambda: 'a'
    assert Validation.success(fn()).to_lazy() == Lazy(fn)


# Generated at 2022-06-14 04:18:57.567496
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(10).to_lazy() == Lazy(lambda: 10)
    assert Validation.fail().to_lazy() == Lazy(lambda: None)
    assert Validation.fail([1]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:19:00.183351
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Python function is callable and can be stored in monads.
    """
    validation = Validation.success(lambda: 'Hello')
    assert validation.to_lazy().eval()() == 'Hello'

# Generated at 2022-06-14 04:19:05.325796
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.validation import Validation
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1) == Validation.success(1).to_lazy()  # success case
    assert Lazy(lambda: None) == Validation.fail([1, 2]).to_lazy()  # fail case


# Generated at 2022-06-14 04:19:09.289032
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Writing unit test of method to_lazy of class Validation
    """

    assert Validation.success(5).to_lazy().evaluate() == 5
    assert Validation.success(5).to_lazy().evaluate() == 5


# Generated at 2022-06-14 04:19:23.300633
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Unit test for method to_lazy of class Validation
    """
    assert Validation.success('test').to_lazy().value() == 'test'
    assert Validation.fail('test').to_lazy().value() is None


# Generated at 2022-06-14 04:19:27.857841
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.either import Left
    from pymonet.monad_try import Try

    assert Validation.success(Lazy(lambda: Try.success(Left(1)))).to_lazy() == Lazy(lambda: Try.success(Left(1)))
    assert Validation.fail([1, 2]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:19:29.144123
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success('hello').to_lazy().get_val()() == 'hello'

# Generated at 2022-06-14 04:19:31.268236
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    validation = Validation.success(7)
    lazy = validation.to_lazy()

    assert lazy.eval() == 7


# Generated at 2022-06-14 04:19:39.829617
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    value = 123

    validation_success = Validation.success(value)
    assert isinstance(validation_success.to_lazy(), Lazy)
    assert validation_success.to_lazy().eval() == value

    errors = [1, 2, 3]

    validation_fail = Validation.fail(errors)
    assert isinstance(validation_fail.to_lazy(), Lazy)
    assert validation_fail.to_lazy().eval() is None



# Generated at 2022-06-14 04:19:42.391897
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success('abc').to_lazy() == Lazy(lambda: 'abc')


# Generated at 2022-06-14 04:19:48.123817
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Validation(1, []).to_lazy() == Lazy(lambda: 1)
    assert Validation(1, []).to_lazy().eval() == Try(1, is_success=True)



# Generated at 2022-06-14 04:19:52.098722
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():

    # Given
    from pymonet.lazy import Lazy
    v1 = Validation.success('Lazy')

    # When
    v2 = v1.to_lazy()

    # Then
    assert v2.value() == 'Lazy'
    assert isinstance(v2, Lazy)


# Generated at 2022-06-14 04:19:55.910730
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    lazy = Validation.success(120).to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.call() == 120


# Generated at 2022-06-14 04:19:59.625159
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Unit test for method to_lazy of class Validation.
    """
    value = 1
    validation = Validation.success(value)

    assert validation.to_lazy().value() == value


# Generated at 2022-06-14 04:20:10.633889
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    result = Validation.success(42).to_lazy()
    expected = Lazy(lambda: 42)
    assert result == expected


# Generated at 2022-06-14 04:20:14.500156
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 11) == Validation.success(11).to_lazy()
    assert Lazy(lambda: None) == Validation.fail([]).to_lazy()


# Generated at 2022-06-14 04:20:22.733860
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    Validation.success(1).to_lazy()
    assert Lazy.unit(1) == Validation.success(1).to_lazy()
    assert Lazy.unit(1).to_box() == Validation.success(1).to_lazy().to_box()
    assert Lazy.unit(1).to_maybe() == Validation.success(1).to_lazy().to_maybe()
    assert Lazy.unit(1).to_try() == Validation.success(1).to_lazy().to_try()


# Generated at 2022-06-14 04:20:27.355857
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail([]).to_lazy() == Lazy(None)


# Generated at 2022-06-14 04:20:30.271658
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Validation.fail().to_lazy() == Lazy(lambda: None)
    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 04:20:35.658065
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def test():
        return True
    def test2():
        return False

    functions = Lazy(test) | Validation.to_lazy() | Validation.to_lazy() | Validation.to_lazy()
    assert isinstance(functions.value, Lazy) is True

# Generated at 2022-06-14 04:20:41.992451
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy
    from pymonet.functor import Functor

    v = Validation.fail(['error'])
    assert v.to_lazy() == Lazy(Functor(lambda: None))

    v = Validation.success(1)
    assert v.to_lazy() == Lazy(Functor(lambda: 1))

# Generated at 2022-06-14 04:20:46.921374
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    validation = Validation(1, [])
    assert validation.to_lazy() == Lazy(lambda: 1)

    validation = Validation(None, [])
    assert validation.to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:20:50.720536
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Assert that Validation.to_lazy() return a new Lazy object containing lambda as expression
    """
    from pymonet.lazy import Lazy

    assert Validation.success(3).to_lazy() == Lazy(lambda: 3)


# Generated at 2022-06-14 04:20:57.210096
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_lazy import Lazy

    lazy_val1 = Lazy(lambda: 9)
    validation1 = Validation.success(9)
    assert validation1.to_lazy() == lazy_val1
    lazy_val2 = Lazy(lambda: None)
    validation2 = Validation.fail()
    assert validation2.to_lazy() == lazy_val2

# Generated at 2022-06-14 04:21:19.730364
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(10).to_lazy().get() == Validation.success(10).value
    assert Validation.fail('error').to_lazy().get() == Validation.fail('error').value


# Generated at 2022-06-14 04:21:21.919016
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    def lazy_func():
        return 1

    validation = Validation.success(1)
    assert validation.to_lazy().get == lazy_func


# Generated at 2022-06-14 04:21:24.204332
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    x_lazy = Validation.success("Lazy").to_lazy()
    assert x_lazy().value == "Lazy"


# Generated at 2022-06-14 04:21:30.225810
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    import pymonet.lazy

    v = Validation.success(1)
    assert v.to_lazy() == pymonet.lazy.Lazy(lambda: 1)

    v = Validation.fail([])
    assert v.to_lazy() == pymonet.lazy.Lazy(lambda: None)

