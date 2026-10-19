

# Generated at 2022-06-14 04:11:33.995834
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def lazy_function():
        return 5

    assert Validation.success(5).to_lazy() == Lazy(lazy_function)


# Generated at 2022-06-14 04:11:41.863405
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try
    from pymonet.box import Box

    def mapper(x): return x + 1

    assert Validation.success(Box(5)).to_lazy().map(mapper).to_try() == Lazy(lambda: mapper(Box(5))).to_try()
    assert Validation.success(Try(5)).to_lazy().map(mapper).to_try() == Lazy(lambda: mapper(Try(5))).to_try()


# Generated at 2022-06-14 04:11:46.221466
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    def returns_int():
        return 1

    validation = Validation.success(returns_int).to_lazy()
    assert isinstance(validation, Lazy)
    assert validation.value() == 1


# Generated at 2022-06-14 04:11:52.348040
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    # Given failed Validation
    val = Validation.fail(['Error 1'])

    # When Validation is transformed to Lazy
    lazy = val.to_lazy()

    # Then returned Lazy is Lazy with function returning None
    assert isinstance(lazy, Lazy)
    assert lazy.run() is None



# Generated at 2022-06-14 04:11:55.961439
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Check possibility to convert Validation to Lazy
    """
    from pymonet.lazy import Lazy

    assert (Validation.success(5).to_lazy() ==
            Lazy(lambda: 5))


# Generated at 2022-06-14 04:12:00.219438
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.maybe import Maybe
    from pymonet.box import Box
    from pymonet.lazy import Lazy

    assert(Validation.success(1).to_lazy() == Lazy(lambda: 1))
    assert(Validation.fail(['error']).to_lazy() == Lazy(lambda: None))

# Generated at 2022-06-14 04:12:04.927575
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Unit test for method to_lazy of class Validation.
    """
    from pymonet.lazy import Lazy

    def function_that_raises_an_exception():
        raise ValueError

    lazy = Validation.success(1).to_lazy()
    assert lazy == Lazy(lambda: 1)

    lazy = Validation.fail(['error']).to_lazy()
    assert lazy == Lazy(lambda: None)


# Generated at 2022-06-14 04:12:10.079175
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Validation to Lazy test.
    """
    from pymonet.monad_try import Try
    from pymonet.either import Left, Right
    from pymonet.lazy import Lazy

    validation = Validation.success(1)

    assert validation.to_lazy() == Lazy(lambda: 1)

    validation = Validation.fail(['Error'])

    assert validation.to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:12:14.418182
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Success
    from pymonet.box import Box

    assert Success(1).to_lazy().fmap(lambda x: Box(x)) == Success(Box(1))

# Generated at 2022-06-14 04:12:22.376496
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    # Validation.success[Hello]
    assert Lazy(lambda: 'Hello') == Validation.success('Hello').to_lazy()

    # Validation.fail[None, ['test1', 'test2']]
    assert Lazy(lambda: None) == Validation.fail(['test1', 'test2']).to_lazy()


# Generated at 2022-06-14 04:12:29.664743
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    lazy_val = Validation.success(10).to_lazy()
    assert lazy_val() == 10

    lazy_val = Validation.fail([10]).to_lazy()
    assert lazy_val() == None


# Generated at 2022-06-14 04:12:38.806572
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    validation = Validation.success("value")
    lazy_value = validation.to_lazy()

    assert lazy_value is not None
    assert isinstance(lazy_value, Lazy)
    assert lazy_value.get() == "value"

    validation = Validation.fail("error")
    lazy_value = validation.to_lazy()

    assert lazy_value is not None
    assert isinstance(lazy_value, Lazy)
    assert lazy_value.get() is None


# Generated at 2022-06-14 04:12:42.056955
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    lazy_value = Validation.success(lambda: 1).to_lazy()
    assert lazy_value.run() == 1


# Generated at 2022-06-14 04:12:45.966727
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    val = Validation.success(100)
    assert val.to_lazy() == Lazy(lambda: 100)

    val = Validation.fail('error')
    assert val.to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:12:49.664637
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Test unit for to_lazy method of class Validation
    """

    from pymonet.lazy import Lazy

    validation = Validation.success(3)
    assert validation.to_lazy() == Lazy(lambda: 3), 'Unit test for to_lazy method of class Validation'

# Generated at 2022-06-14 04:12:53.695290
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    def test(v):
        return v * 2

    v1 = Validation.success(5)
    assert v1.to_lazy().map(test).value() == 10

    v2 = Validation.fail([])
    assert v2.to_lazy().map(test).value() is None

# Generated at 2022-06-14 04:13:03.825095
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Test for method to_lazy().

    :returns: Nothing
    :raises: AssertionError when test failed
    """
    from pymonet.lazy import Lazy

    assert Validation.success(100).to_lazy() == Lazy(lambda: 100)
    assert Validation.success(100).to_lazy().value() == 100

    assert Validation.fail(['error']).to_lazy() == Lazy(lambda: None)
    assert Validation.fail(['error']).to_lazy().value() is None


# Generated at 2022-06-14 04:13:06.821108
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    valid = Validation.success(2)
    lazy = valid.to_lazy()

    assert Lazy(lambda: 2) == lazy


# Generated at 2022-06-14 04:13:11.204489
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    expected = Validation(1, []).to_lazy()

    assert Lazy(lambda: 1) == expected

    assert Try(1, is_success=True) == expected.get()

# Generated at 2022-06-14 04:13:15.716052
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def does_not_matter():
        pass

    def does_matter():
        return "some value"

    assert Lazy(does_not_matter) == Validation.fail().to_lazy()
    assert Lazy(does_matter) == Validation.success("some value").to_lazy()


# Generated at 2022-06-14 04:13:23.409136
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    def f():
        return 'this is value'

    result = Validation.success(f).to_lazy()

    assert result == Lazy(f)


# Generated at 2022-06-14 04:13:30.306094
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Validation.success(1).to_lazy().map(lambda x: x + 1).to_try() == Try(2)
    assert Validation.success(1).to_lazy().map(lambda x: Lazy(lambda: x + 1)).to_try() == Try(Lazy(lambda: 1+1))



# Generated at 2022-06-14 04:13:36.079444
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.success(1).to_lazy() != Lazy(lambda: 2)
    assert Validation.success(1).to_lazy() != Lazy(lambda: None)


# Generated at 2022-06-14 04:13:42.711803
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Unit test for method to_lazy of class Validation.
    """
    # Happy path
    # given
    validation = Validation.success('test string')
    # when
    lazy = validation.to_lazy()
    # then
    assert lazy.get() == 'test string'

    # Sad path
    # given
    validation = Validation.fail(['error 1', 'error 2'])
    # when
    lazy = validation.to_lazy()
    # then
    assert lazy.get() == None


# Generated at 2022-06-14 04:13:46.277482
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success('one').to_lazy() == Lazy(lambda: 'one')
    assert Validation.fail().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:13:49.607932
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(3).to_lazy() == Lazy(lambda: 3)
    assert Validation.fail(['error']).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:13:52.265119
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(1).to_lazy().get() == 1
    assert Validation.fail(['error']).to_lazy().get() is None


# Generated at 2022-06-14 04:13:57.172804
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    validation = Validation.success(1)
    assert validation.to_lazy() == Lazy(lambda: 1) and validation.value == 1

    validation = Validation.fail(['error1', 'error2'])
    assert validation.to_lazy() == Lazy(lambda: None) and validation.value is None


# Generated at 2022-06-14 04:14:00.817938
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    # given
    value = 'test'
    validation = Validation(value, [])
    # when
    result = validation.to_lazy()
    # then
    assert result._value() == value


# Generated at 2022-06-14 04:14:07.567754
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe

    success = Lazy(lambda: Validation.success(Maybe.just(1)))
    assert success.value() == Validation.success(Maybe.just(1))

    fail = Lazy(lambda: Validation.fail(['error']))
    assert fail.value() == Validation.fail(['error'])


# Generated at 2022-06-14 04:14:18.042611
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    validation = Validation.success(1)
    lazy = validation.to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy.get() == Try.success(1)

# Generated at 2022-06-14 04:14:23.451948
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    lazy = Lazy(lambda: Validation.success('value'))
    assert lazy == Lazy(lambda: Validation.success('value'))

    lazy = Lazy(lambda: Validation.fail('error'))
    assert lazy == Lazy(lambda: Validation.fail('error'))


# Generated at 2022-06-14 04:14:26.631089
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
        from pymonet.lazy import Lazy

        assert(Lazy(lambda: 5432) == Validation(5432, []).to_lazy())


# Generated at 2022-06-14 04:14:29.354798
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success('hello').to_lazy().get() == 'hello'
    assert Validation.fail(['bad']).to_lazy().get() is None



# Generated at 2022-06-14 04:14:37.159067
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    lazy_value = Lazy(lambda: 'value')
    assert Validation.success(lazy_value).to_lazy().value() == 'value'
    assert Validation.success(Try.success('value')).to_lazy().value == 'value'
    assert Validation.success(Try.fail(None)).to_lazy().value is None


# Generated at 2022-06-14 04:14:39.086762
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    try_ = Try(lambda: 5)
    lazy = try_.to_lazy()

    assert lazy == Lazy(lambda: 5)


# Generated at 2022-06-14 04:14:43.152497
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Unit test for method to_lazy of class Validation.
    """
    from pymonet.lazy import Lazy

    lazy = Lazy(lambda: 1)
    assert Validation.success(1).to_lazy() == lazy



# Generated at 2022-06-14 04:14:48.436677
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """Unit test for method to_lazy of class Validation."""

    lazy_success = Validation.success(1).to_lazy()
    lazy_fail = Validation.fail(["fail"]).to_lazy()

    assert(lazy_success.force() == 1)
    assert(lazy_fail.force() is None)


# Generated at 2022-06-14 04:14:55.813504
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    value = Validation.success(1)
    lazy = value.to_lazy()
    assert lazy.is_lazy()
    assert lazy == Lazy(lambda: 1)

    value = Validation.fail()
    lazy = value.to_lazy()
    assert lazy.is_lazy()
    assert lazy == Lazy(lambda: None)


# Generated at 2022-06-14 04:14:57.190881
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    result = Validation.success(10).to_lazy()
    assert result.get() == 10

    result = Validation.fail([1]).to_lazy()
    assert result.get() == None


# Generated at 2022-06-14 04:15:06.156911
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def func():
        return 'result'

    assert Validation.success(func).to_lazy() == Lazy(func)


# Generated at 2022-06-14 04:15:14.238747
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy


    def try_success(x):
        t = Try(x)
        return t

    def try_fail(x):
        t = Try(x, is_success=False)
        return t

    def try_map(f):
        def g(x):
            return try_success(f(x))
        return g

    def try_ap(f):
        def g(x):
            return try_map(f)(x).to_lazy()
        return g

    assert Validation.success(lambda x: x + 5).to_lazy() == Lazy(lambda: (lambda x: x + 5))

# Generated at 2022-06-14 04:15:21.990376
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Test for correct transformation Validation to Lazy monad.
    """
    from pymonet.lazy import Lazy
    lazy = Validation.success(1).to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.value == 1
    lazy = Validation.success().to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.value is None
    assert Validation.fail([1, 2, 3]).to_lazy() is None


# Generated at 2022-06-14 04:15:23.666133
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    result = Validation.success(5).to_lazy()

    assert result.value() == 5



# Generated at 2022-06-14 04:15:29.431094
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    It tests method to_lazy of class Validation.
    """
    from pymonet.lazy import Lazy

    lazy = Validation.success(1).to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.value() == 1
    assert lazy.value() == 1
    assert lazy.value() == 1
    assert lazy.value() == 1


# Generated at 2022-06-14 04:15:35.200082
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.functions import identity

    assert Validation.success(12).to_lazy() == Lazy(lambda: 12)
    assert Validation.success(12).to_lazy().map(identity) == Validation.success(12)
    assert Validation.fail(['error']).to_lazy() == Lazy(lambda: None)
    assert Validation.fail(['error']).to_lazy().map(identity) == Validation.fail(['error'])


# Generated at 2022-06-14 04:15:41.156057
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    # Box.to_lazy
    assert Validation.success(lambda: 5).to_lazy() == Lazy(lambda: lambda: 5).unit()
    assert Validation.fail(errors=['error']).to_lazy() == Lazy(lambda: None).unit()


# Generated at 2022-06-14 04:15:43.824273
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(1).to_lazy().eval() == 1
    assert Validation.fail([1]).to_lazy().eval() is None


# Generated at 2022-06-14 04:15:46.432995
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Test Validation.to_lazy method.
    """
    from pymonet.lazy import Lazy

    assert Validation.success(100).to_lazy() == Lazy(lambda: 100)
    assert Validation.fail(['error']).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:15:51.245178
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.maybe import Maybe
    from pymonet.either import Left, Right
    from pymonet.box import Box
    from pymonet.lazy import Lazy

    assert Validation.success('success').to_lazy() == Lazy(lambda: 'success')
    assert Validation.fail([]).to_lazy() == Lazy(lambda: None)
    assert Validation.success(Try.success('success')).to_lazy() == Lazy(lambda: 'success')
    assert Validation.success(Try.fail('')).to_lazy() == Lazy(lambda: None)
    assert Validation.success(Left(2)).to_lazy() == Lazy(lambda: None)
    assert Validation.success(Right(2)).to_l

# Generated at 2022-06-14 04:16:07.344755
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    v1 = Validation.success(1)
    assert v1.to_lazy() == Lazy(lambda: 1)
    assert v1.to_lazy().value() == 1

    v2 = Validation.fail([1, 'error'])
    assert v2.to_lazy() == Lazy(lambda: None)
    assert v2.to_lazy().value() is None


# Generated at 2022-06-14 04:16:08.655495
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 04:16:13.439881
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():

    from pymonet.lazy import Lazy

    lazy = Validation.success(1).to_lazy()
    assert lazy == Lazy(lambda: 1)
    assert lazy.value == 1


# Generated at 2022-06-14 04:16:19.016067
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """Test to_lazy method of Validation class"""
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    success_val = Validation(lambda: 2, [])
    assert success_val.to_lazy() == Lazy(lambda: 2)

    fail_val = Validation(None, [2])
    assert fail_val.to_lazy() == Lazy(None)


# Generated at 2022-06-14 04:16:24.539292
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    def square(x):
        return x * x
    assert Validation.success(4).to_lazy().fmap(square).eval() == 16
    assert Validation.success(4).to_lazy().fmap(lambda x: 2 * x).eval() == 8


# Generated at 2022-06-14 04:16:28.639557
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1) == Validation.success(1).to_lazy()
    assert Lazy(lambda: None) == Validation.fail([]).to_lazy()

# Generated at 2022-06-14 04:16:34.613136
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success('test').to_lazy() == Lazy(lambda: 'test')
    assert Validation.fail(['error']).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:16:38.285428
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    Lazy(lambda: Validation.success(10).value) == Validation.success(10).to_lazy()
    Lazy(lambda: Validation.fail(['error']).value) == Validation.fail(['error']).to_lazy()


# Generated at 2022-06-14 04:16:44.077655
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1) == Validation.success(1).to_lazy()
    assert Lazy(lambda: None) == Validation.fail([]).to_lazy()


# Generated at 2022-06-14 04:16:48.555830
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    assert Validation.success(5).to_lazy() == Lazy(lambda: 5)
    assert Validation.fail('error').to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:17:11.174677
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    val = Validation.success(2000)
    val_2 = Lazy(lambda: 2000)
    assert val.to_lazy() == val_2


# Generated at 2022-06-14 04:17:13.676036
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.success(1).to_lazy().eval() == 1



# Generated at 2022-06-14 04:17:18.090476
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    | Validation.success | should return Lazy with function returning Validation value (wrapped by Lazy)
    | Validation.fail | should return Lazy with function returning Validation value (wrapped by Lazy)
    """
    from pymonet.lazy import Lazy

    assert Lazy(lambda: "value") == Validation.success("value").to_lazy()
    assert Lazy(lambda: None) == Validation.fail().to_lazy()


# Generated at 2022-06-14 04:17:25.863508
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Tests Validation.to_lazy() method.
    """
    from pymonet.either import Right
    from pymonet.lazy import Lazy

    assert Validation(None, []).to_lazy() == Lazy(None)
    assert Validation(2, []).to_lazy() == Lazy(2)
    assert Validation(None, [1, 2, 3]).to_lazy() == Lazy(None)
    assert Validation(2, [1, 2, 3]).to_lazy() == Lazy(2)


# Generated at 2022-06-14 04:17:28.229581
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    def dummy_function():
        return 5

    validation = Validation.success(5)

    assert validation.to_lazy() == Lazy(dummy_function)


# Generated at 2022-06-14 04:17:37.856753
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try
    from pymonet.monad_try import _success_monad, _fail_monad

    original_val = 1
    wrapped_val = _success_monad(original_val)
    lazy_val = wrapped_val.to_lazy()  # Validation[A] -> Lazy[A]

    assert lazy_val.value() == original_val

    wrapped_val = _fail_monad(None)
    lazy_val = wrapped_val.to_lazy()  # Validation[A] -> Lazy[A]

    assert lazy_val.value() == wrapped_val.value  # Lazy[A] -> A


# Generated at 2022-06-14 04:17:44.332027
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    # Check if transform from Validation to Lazy works fine
    actual = Validation.success(1).to_lazy()
    expected = Lazy(lambda: 1)
    assert actual == expected

    # Check if transform from Validation to Lazy works fine
    actual = Validation.success(None).to_lazy()
    expected = Lazy(lambda: None)
    assert actual == expected

    # Check if transform from Validation to Lazy works fine
    actual = Validation.fail(errors=[]).to_lazy()
    expected = Lazy(lambda: None)
    assert actual == expected


# Generated at 2022-06-14 04:17:50.436654
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success().to_lazy() == Lazy(lambda: None)
    assert Validation.success(42).to_lazy() == Lazy(lambda: 42)
    assert Validation.fail([1, 2]).to_lazy() == Lazy(lambda: None)
    assert Validation.fail([1, 2]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:17:53.730425
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    result = Validation.success('test').to_lazy()

    assert isinstance(result, Lazy) and result.value() == 'test'

# Generated at 2022-06-14 04:17:56.765819
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail(['error']).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:18:22.834924
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Unit test for method to_lazy of class Validation
    """
    assert Validation.success(2).to_lazy() == Lazy(lambda: 2)
    assert Validation.fail([1]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:18:29.351429
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def test_value(value, errors):
        return Lazy(lambda: Validation(value, errors))

    assert test_value(None, []) == Lazy(lambda: Validation.success(None))
    assert test_value(1, []) == Lazy(lambda: Validation.success(1))
    assert test_value(None, ['1', '2']) == Lazy(lambda: Validation.fail(['1', '2']))



# Generated at 2022-06-14 04:18:35.490043
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Validation('lazy', []).to_lazy() == Lazy(lambda: 'lazy')

    assert Validation('lazy', [1, 2]).to_lazy() == Lazy(lambda: 'lazy')

    assert Validation([1, 2]).to_lazy() == Lazy(lambda: [1, 2])


# Generated at 2022-06-14 04:18:40.216816
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.validation import Validation
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe

    def test_success():
        x = Validation.success(1)
        assert x.to_lazy() == Lazy(lambda: 1)

    test_success()

# Generated at 2022-06-14 04:18:50.093608
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy
    from pymonet.monad import is_lazy

    success_Validation = Validation.success(10)
    fail_Validation = Validation.fail([1, 2, 3])

    assert is_lazy(success_Validation.to_lazy())
    assert success_Validation.to_lazy() == Lazy(lambda: 10)

    assert is_lazy(fail_Validation.to_lazy())
    assert fail_Validation.to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 04:18:54.845561
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_list import List
    from pymonet.either import Either
    from pymonet.lazy import Lazy

    def get_value():
        return 1

    validation = Validation.success(1)
    lazy = validation.to_lazy()
    assert lazy.value() == 1
    validation = Validation.fail([])
    lazy = validation.to_lazy()
    assert lazy.value() is None


# Generated at 2022-06-14 04:18:58.963206
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 'a') == Validation.success('a').to_lazy()

    assert Lazy(lambda: 1 / 0) == Validation.fail(errors=['Error-1']).to_lazy()



# Generated at 2022-06-14 04:19:03.263374
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.monad_try import Failure
    from pymonet.lazy import Lazy
    lazy = Validation.success(4).to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.value() == 4
    try_result = Validation.fail(['error']).to_lazy().value()
    assert isinstance(try_result, Try)
    assert try_result.is_failure() == True
    assert isinstance(try_result, Failure)


# Generated at 2022-06-14 04:19:08.639560
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.box import Box
    from pymonet.monad_try import Try
    from pymonet.either import Left, Right

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail([1, 2]).to_lazy() == Lazy(lambda: None)

# Generated at 2022-06-14 04:19:13.647596
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation(1, []).to_lazy() == Lazy(lambda: 1)
    assert Validation(1, []).to_lazy().force() == 1
    assert Validation(None, 'error').to_lazy().force() is None



# Generated at 2022-06-14 04:19:59.606621
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    validation = Validation.success(100)
    lazy = validation.to_lazy()
    assert lazy == Lazy(lambda: 100)


# Generated at 2022-06-14 04:20:07.106894
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Success

    lazy = Validation.success(10).to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.value() == 10

    lazy = Validation.fail([10]).to_lazy()
    assert isinstance(lazy.to_try(), Success)
    assert lazy.to_try().value is None


# Generated at 2022-06-14 04:20:11.633999
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    v = Validation(1, [])
    l = v.to_lazy()

    assert v.value == l.value()
    assert isinstance(l, Lazy)
    assert callable(l.value)
    assert l.value() == 1


# Generated at 2022-06-14 04:20:17.161416
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.enums import Status

    VALIDATION = Validation(10, [])
    LAZY = VALIDATION.to_lazy()

    assert isinstance(LAZY, Lazy)
    assert LAZY.value == 10
    assert LAZY.status == Status.COMPUTED



# Generated at 2022-06-14 04:20:21.271476
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    # Success Validation
    validation = Validation.success("hello")
    assert (Lazy(lambda: "hello") == validation.to_lazy())
    # Fail Validation
    validation = Validation.fail("hello")
    assert (Lazy(lambda: None) == validation.to_lazy())


# Generated at 2022-06-14 04:20:26.022210
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    def test_func():
        raise TypeError('Something wrong!')

    value = Validation.success(5)
    assert value.to_lazy() == Lazy(lambda: 5)

    value = Validation.fail('Something wrong!')
    assert value.to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:20:28.223044
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    assert Validation.success('ok').to_lazy() == Lazy(lambda: 'ok')


# Generated at 2022-06-14 04:20:33.783067
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    assert Validation.success(1).to_lazy() == Lazy(lambda : 1)
    assert Validation.success().to_lazy() == Lazy(lambda : None)



# Generated at 2022-06-14 04:20:37.758307
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    assert Try("hello").to_lazy() == Lazy(lambda: "hello")
    assert Try("hello", is_success=False).to_lazy() == Lazy(lambda: "hello")


# Generated at 2022-06-14 04:20:42.250756
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def lazy_test(result):
        assert result
        return True

    result = Validation.success('success').to_lazy().map(lazy_test).run()
    assert result
