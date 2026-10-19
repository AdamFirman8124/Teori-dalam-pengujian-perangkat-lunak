

# Generated at 2022-06-14 04:11:32.915923
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    val = Validation(1, [])
    assert val.to_lazy() == Lazy(lambda: 1)

    val = Validation(None, [])
    assert val.to_lazy() == Lazy(lambda: None)

# Unit test method bind of class Validation

# Generated at 2022-06-14 04:11:38.988921
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Perform test for method to_lazy of class Validation.

    :return: None
    :rtype: None
    """
    from pymonet.lazy import Lazy

    assert (Lazy(lambda: 1) == Validation.success(1).to_lazy())
    assert (Lazy(lambda: None) == Validation.fail().to_lazy())


# Generated at 2022-06-14 04:11:42.522388
# Unit test for method __eq__ of class Validation
def test_Validation___eq__():
    assert Validation.success(1) == Validation.success(1)
    assert Validation.success(1) != Validation.success(2)
    assert Validation.success(1) != Validation.fail([])
    assert Validation.fail([1, 2, 3]) == Validation.fail([1, 2, 3])
    assert Validation.fail([1, 2, 3]) != Validation.fail([1, 2, 4])
    assert Validation.fail([1, 2, 3]) != Validation.success(None)
    assert Validation.success(None) != Validation.success(2)
    assert Validation.fail([]) == Validation.fail([])


# Generated at 2022-06-14 04:11:50.097375
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.box import Box

    # In case of success return Lazy with function returning Validation value
    validation = Validation.success(5)
    assert validation.to_lazy() == Lazy(lambda: Box(5))

    # In case of failure return Lazy with function returning Validation value
    validation = Validation.fail([5])
    assert validation.to_lazy() == Lazy(lambda: Box(None))


# Generated at 2022-06-14 04:11:54.397773
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    test_Validation_to_lazy
    """
    validation = Validation.success("value")

    assert validation.to_lazy().value() == "value"
    assert validation.to_lazy().value() == "value"


# Generated at 2022-06-14 04:11:59.263706
# Unit test for method __eq__ of class Validation
def test_Validation___eq__():
    assert Validation.success('a') == Validation.success('a')
    assert Validation.success('a') != Validation.success('b')
    assert Validation.fail('a') == Validation.fail('a')
    assert Validation.fail('a') != Validation.fail('b')


# Generated at 2022-06-14 04:12:08.926342
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    assert Validation.success(value=None).to_lazy() == Lazy(lambda: None)
    assert Validation.success(value=123).to_lazy() == Lazy(lambda: 123)
    assert Validation.success(value='test').to_lazy() == Lazy(lambda: 'test')
    assert Validation.success(value=[1, 2, 3]).to_lazy() == Lazy(lambda: [1, 2, 3])
    assert Validation.success(value={'key': 'value'}).to_lazy() == Lazy(lambda: {'key': 'value'})

# Generated at 2022-06-14 04:12:13.058762
# Unit test for method __eq__ of class Validation
def test_Validation___eq__():  # pragma: no cover
    assert Validation.success('a').__eq__(Validation.success('a'))
    assert not Validation.success('a').__eq__(Validation.success('b'))
    assert Validation.fail(['a']).__eq__(Validation.fail(['a']))
    assert not Validation.fail(['a']).__eq__(Validation.fail(['b']))
    assert not Validation.success('a').__eq__(Validation.fail(['a']))


# Generated at 2022-06-14 04:12:19.188837
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(10).to_lazy() == Lazy(lambda: 10)
    assert Validation.fail([1, 2, 3]).to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 04:12:28.082047
# Unit test for method __eq__ of class Validation
def test_Validation___eq__():
    """
    Unit test for method __eq__ of class Validation.
    """
    # Successful Validation
    successful_validation_1 = Validation.success(1)
    successful_validation_2 = Validation.success(1)
    assert successful_validation_1 == successful_validation_2

    # Failed Validation
    failed_validation_1 = Validation.fail([1, 2, 3])
    failed_validation_2 = Validation.fail([1, 2, 3])
    assert failed_validation_1 == failed_validation_2

    # Successful and failed Validations
    successful_validation = Validation.success(1)
    failed_validation = Validation.fail([2, 3])
    assert not successful_validation == failed_validation


# Generated at 2022-06-14 04:12:33.539949
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(3).to_lazy() == Lazy(lambda: 3)
    assert Validation.fail([1, 2, 3]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:12:37.392943
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 04:12:41.333911
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail([1, 2, 3]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:12:44.301548
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(10).to_lazy() == Lazy(lambda: 10)
    assert Validation.fail([1, 2]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:12:48.779804
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    # given
    validation = Validation.success(3)

    # when
    lazy = validation.to_lazy()

    # then
    assert isinstance(lazy, Lazy)
    assert lazy() == 3


# Generated at 2022-06-14 04:12:50.572653
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success('success').to_lazy().eval() == 'success'


# Generated at 2022-06-14 04:12:57.210924
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Unit test for to_lazy method
    """

    v1 = Validation.success(1)
    v2 = Validation.success(2)

    lazy1 = v1.to_lazy()
    lazy2 = v2.to_lazy()

    assert v1 == lazy1.value()
    assert v2 == lazy2.value()

    lazy3 = lazy1.map(lambda x: x + 1)
    assert v2 == lazy3.value()

    lazy4 = lazy1.ap(lambda x: Validation.success(x + 1))
    assert v2 == lazy4.value()

    lazy5 = lazy1.bind(lambda x: Validation.success(x + 1))
    assert v2 == lazy5.value()


# Generated at 2022-06-14 04:13:04.164662
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    def identity(value):
        return value

    assert Lazy(lambda: identity(Try(10))) == Validation.success(10).to_lazy()

    assert Lazy(lambda: identity(Try.fail())) == Validation.fail().to_lazy()

# Generated at 2022-06-14 04:13:13.317406
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.monad_try import Try

    def failing_function():
        raise RuntimeError('Failing function')

    assert Validation.fail().to_lazy() == Lazy(lambda: None)
    assert Validation.success(5).to_lazy() == Lazy(lambda: 5)
    assert Validation.fail([RuntimeError('Failing function')]) \
        .to_lazy().flat_map(lambda value: Try(failing_function)) == Try(failing_function, is_success=True)
    assert Validation.success(5) \
        .to_lazy().flat_map(lambda value: Try(failing_function)) == Try(failing_function, is_success=False)

# Generated at 2022-06-14 04:13:16.327224
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail([]).to_lazy() == Lazy(lambda: None)
    assert Validation.fail([1]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:13:23.588319
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    import pymonet.monad_try as Try
    assert Validation.success(10).to_lazy() == Lazy(lambda: 10)
    assert Validation.fail([10, 15]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:13:30.452976
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try
    from pymonet.either import Right, Left

    val = Validation.success(10)
    assert val.to_lazy() == Lazy(lambda: 10)

    val = Validation.fail([1,2,3])
    assert val.to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:13:35.381062
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    def f():
        return 7

    validation = Validation.success(f)
    lazy = validation.to_lazy()

    assert lazy == Lazy(f)


# Generated at 2022-06-14 04:13:37.864902
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    lazy = Validation.fail(['err1']).to_lazy()
    assert lazy.evaluate() is None


# Generated at 2022-06-14 04:13:45.339597
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.either import Right
    from pymonet.maybe import Maybe
    from pymonet.monad_try import Try
    from pymonet.box import Box
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    result = Validation.success('test').to_lazy()
    assert isinstance(result, Lazy), 'Validation.to_lazy() should return Lazy class'
    assert result.value() == 'test', 'Validation.to_lazy() should return Lazy value with Validation value'

    result = Validation.fail(['error']).to_lazy()
    assert isinstance(result, Lazy), 'Validation.to_lazy() should return Lazy class'

# Generated at 2022-06-14 04:13:49.522262
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    # Test for successful Validation
    def id(x):
        return x

    val = Lazy(lambda: 3)
    assert val.map(id) == Validation(4, []).to_lazy()

# Generated at 2022-06-14 04:13:54.528042
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    success = Validation.success(100)
    lazy = success.to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.force() == 100

    fail = Validation.fail(['Error1', 'Error2'])
    lazy = fail.to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.force() is None



# Generated at 2022-06-14 04:13:58.250132
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1).to_lazy().value() == 1
    assert Validation(1, []).to_lazy().value() == 1
    assert Validation(None, [1, 2]).to_lazy().value() is None



# Generated at 2022-06-14 04:14:02.461556
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def func():
        return 2

    lazy = Validation.success(func).to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy() == func()


# Generated at 2022-06-14 04:14:09.818491
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    validation = Validation.success(1)
    assert validation.to_lazy() == Lazy(lambda: 1)

    validation = Validation.fail()
    assert validation.to_lazy() == Lazy(lambda: None)
    assert validation.to_lazy().fmap(abs).to_try() == Try(None, is_success=False)


# Generated at 2022-06-14 04:14:18.231011
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail([1]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:14:23.992513
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Validation.success(42).to_lazy() == Lazy(lambda: 42)
    assert Validation.success(None).to_lazy() == Lazy(lambda: None)
    assert Validation.fail(['Error']).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:14:31.865010
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy
    from pymonet.box import Box

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.success(1).map(lambda x: x + 2).to_lazy() == Lazy(lambda: 3)
    assert Validation.fail(['Anything']).to_lazy() == Lazy(lambda: None)

# Generated at 2022-06-14 04:14:39.862319
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    validation = Lazy(lambda: Validation.fail(['failure']))
    value = validation.value()
    assert isinstance(value, Validation)
    assert value.value is None
    assert value.errors == ['failure']
    validation = Lazy(lambda: Validation.success('success'))
    value = validation.value()
    assert isinstance(value, Validation)
    assert value.value == 'success'
    assert value.errors == []


# Generated at 2022-06-14 04:14:43.486367
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    lazy_value = Lazy(lambda: 1)
    validation = Validation.success(1)

    assert validation.to_lazy() == lazy_value

# Generated at 2022-06-14 04:14:46.123522
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation(10, []).to_lazy() == Lazy(lambda: 10)



# Generated at 2022-06-14 04:14:51.122567
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Validation.success(123).to_lazy() == Lazy(lambda: 123)
    assert Validation.success(123).to_try() == Try(123, is_success=True)


# Generated at 2022-06-14 04:15:01.843603
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Testing to lazy conversion from Validation.
    """
    from pymonet.lazy import Lazy

    assert Validation(1, []).to_lazy()         == Lazy(lambda: 1)
    assert Validation('', []).to_lazy()        == Lazy(lambda: '')
    assert Validation(None, []).to_lazy()      == Lazy(lambda: None)
    assert Validation([], []).to_lazy()        == Lazy(lambda: [])
    assert Validation(False, []).to_lazy()     == Lazy(lambda: False)
    assert Validation({}, []).to_lazy()        == Lazy(lambda: {})
    assert Validation((), []).to_lazy()        == Lazy(lambda: ())


# Generated at 2022-06-14 04:15:07.624984
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    success_case = Validation.success(1)
    assert success_case.to_lazy() == Lazy(lambda: 1)

    fail_case = Validation.fail([2])
    assert fail_case.to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:15:15.104358
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.maybe import Maybe
    from pymonet.monad_try import Try
    import pymonet.lazy as lazy

    assert Validation.success([1, 2]).to_lazy() == Lazy(lambda: [1, 2])
    assert Validation.fail(["x>0"]).to_lazy() == Lazy(lambda: None)
    assert lazy.pure(Validation.fail(["x>0"])).bind(to_lazy) == Lazy(lambda: None)

    def get_list():  # pragma: no cover
        return []

    def get_element():  # pragma: no cover
        return 1

    def get_dict():  # pragma: no cover
        return {}

    def get_value():  # pragma: no cover
        return

# Generated at 2022-06-14 04:15:28.897307
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    # Successful Validation
    v = Validation.success(10)

    assert v.to_lazy() == Lazy(lambda: 10)

    # Failed Validation
    v = Validation.fail(['error1', 'error2'])

    assert v.to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 04:15:38.721400
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_maybe import Maybe
    from pymonet.monad_try import Try

    none = None
    errors = ['Error']
    errors_list = ['Error', 'Error']
    v_some = Validation(1, errors_list.copy())
    v_none = Validation(none, errors.copy())
    lazy_some = v_some.to_lazy()
    lazy_none = v_none.to_lazy()

    assert lazy_some == Lazy(lambda: v_some.value)
    assert lazy_none == Lazy(lambda: v_none.value)
    assert v_some == lazy_some.to_validation()
    assert v_none == lazy_none.to_validation()

# Generated at 2022-06-14 04:15:42.933670
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Test transform Validation to Lazy.
    """
    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail('error').to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:15:46.827937
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.success(None).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:15:48.505261
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    val = Validation.success(1)
    assert val.to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 04:15:52.757162
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    '''
    To test to_lazy method of class Validation.
    '''

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:15:55.175281
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    try:
        Validation.success('hello').to_lazy()
        assert False
    except TypeError:
        assert True


# Generated at 2022-06-14 04:16:06.140723
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():

    def run(value):

        from pymonet.monad_try import Try
        from pymonet.lazy import Lazy
        from pymonet.box import Box

        assert Validation(value, []).to_lazy() == Lazy(lambda: value)
        assert Validation(value, []).to_try() == Try(value, is_success=True)
        assert Validation(value, []).to_box() == Box(value)

    run(False)
    run(True)
    run(None)
    run(1)
    run(0)
    run(1.0)
    run(0.0)
    run('a')
    run('b')
    run([1,2,3])
    run((1,2,3))

# Generated at 2022-06-14 04:16:10.165359
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    It checks correctness of method Validation.to_lazy.

    :returns: None
    :rtype: None
    """

    from pymonet.lazy import Lazy

    def test_function():
        return 42

    validation = Validation.success(test_function())
    assert validation.to_lazy() == Lazy(test_function)

# Generated at 2022-06-14 04:16:13.773865
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    val = Validation(0).to_lazy()
    assert val == Lazy(lambda: 0)

# Generated at 2022-06-14 04:16:24.067061
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(2).to_lazy()._value() == 2


# Generated at 2022-06-14 04:16:27.816244
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    validation = Validation.success(123)
    assert validation.to_lazy().value() == 123

    validation = Validation.fail('abc')
    assert validation.to_lazy().value() is None


# Generated at 2022-06-14 04:16:30.648281
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)

    assert Validation.fail([1]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:16:35.921985
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    validation = Validation.success(10)

    result = validation.to_lazy()

    assert isinstance(result, Lazy)
    assert result.try_() == Try(10, is_success=True)


# Generated at 2022-06-14 04:16:38.948313
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def function():
        return True

    lazy = Validation.success(function).to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.value() is function


# Generated at 2022-06-14 04:16:45.401920
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    It tests `to_lazy` method of class `Validation`.
    """
    from pymonet.lazy import Lazy

    assert Validation.success(10).to_lazy() == Lazy(lambda: 10)
    assert Validation.fail().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:16:51.288118
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    val = Validation(5, [])
    try_lazy = val.to_lazy()
    assert try_lazy == Lazy(lambda: 5)
    assert NotImplemented == try_lazy.evaluate()


# Generated at 2022-06-14 04:16:55.887939
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def f(x):
        return x + 1

    assert Lazy(lambda: 1) == Validation.success(1).to_lazy()
    assert Lazy(lambda: f(2)) == Validation.success(2).to_lazy().map(f)


# Generated at 2022-06-14 04:16:59.667729
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail(["error-message"]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:17:09.845666
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try
    import pytest

    validation = Validation(1, [])
    assert isinstance(validation.to_lazy(), Lazy)
    assert validation.value == validation.to_lazy().force()

    validation = Validation(None, [])
    assert isinstance(validation.to_lazy(), Lazy)
    assert validation.value == validation.to_lazy().force()

    validation = Validation(1, [2])
    assert isinstance(validation.to_lazy(), Lazy)
    assert validation.value == validation.to_lazy().force()

    validation = Validation(None, [2])
    assert isinstance(validation.to_lazy(), Lazy)
    assert validation.value == validation

# Generated at 2022-06-14 04:17:25.060446
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Unit test for method to_lazy of class Validation
    """
    from pymonet.monad_try import Try

    monad = Validation.success(123)
    assert monad.value == 123
    assert monad.to_lazy().value().get() == 123

    monad = Validation.fail([])
    assert monad.value is None
    assert monad.to_lazy().value().get() is None


# Generated at 2022-06-14 04:17:27.828890
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    assert Validation.success(value=1).to_lazy().value == 1
    assert Validation.fail(errors=[1, 2]).to_lazy().value is None



# Generated at 2022-06-14 04:17:31.497320
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def _get_three():
        return 3

    test_lazy = Lazy(_get_three)

    assert Validation.success(2).to_lazy() == test_lazy


# Generated at 2022-06-14 04:17:33.944495
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(1).to_lazy().value() == 1
    assert Validation.fail(['error']).to_lazy().value() is None


# Generated at 2022-06-14 04:17:36.285324
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Success, Failure

    assert Success(1).to_lazy() == Lazy(lambda: 1)
    assert Failure(1, 2).to_lazy() == Lazy(lambda: 2)


# Generated at 2022-06-14 04:17:39.695933
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    lazy = Validation.success(1).to_lazy()
    assert isinstance(lazy, Lazy)
    assert callable(lazy.value)
    assert lazy.value() == 1


# Generated at 2022-06-14 04:17:43.804146
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    assert Validation.success(2).to_lazy() == Lazy(lambda: 2)
    assert Validation.success(2).to_lazy().force() == 2
    assert Validation.fail([]).to_lazy().force() == None



# Generated at 2022-06-14 04:17:50.392046
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.box import Box
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    lazy = Validation.success(Box('value')).to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy() == Box('value')
    assert lazy() is lazy().value
    assert lazy() is lazy().value
    assert lazy() is lazy().__dict__['value']


# Generated at 2022-06-14 04:17:57.482911
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def pick_letter(word):
        return Lazy(lambda: word[0])

    val = Validation.success("python")
    assert str(val.to_lazy()) == "Lazy[Function() -> 'python']"

    val = Validation.fail("error")
    assert str(val.to_lazy()) == "Lazy[Function() -> None]"

    val = Validation.success("python").bind(pick_letter)
    assert str(val.to_lazy()) == "Lazy[Function() -> 'p']"


# Generated at 2022-06-14 04:18:02.174309
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.success(1).to_lazy().get() == 1
    assert Validation.fail(['error 1', 'error 2']).to_lazy().get() is None


# Generated at 2022-06-14 04:18:17.149355
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation
    import unittest

    class ValidationToLazyTest(unittest.TestCase):
        def test_Validation_to_lazy(self):
            val = Validation(1, [])
            lazy_val = val.to_lazy()

            self.assertEqual(type(lazy_val), Lazy)
            self.assertEqual(lazy_val.value(), val.value)

    unittest.main()

# Generated at 2022-06-14 04:18:26.178830
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.monad_lazy import Lazy

    val = Validation.success().to_lazy()

    assert isinstance(val, Lazy)
    assert val.evaluate() is None

    val = Validation.fail(['a', 'b']).to_lazy()

    assert isinstance(val, Lazy)
    assert val.evaluate() is None

    val = Validation.success('a').to_lazy()

    assert isinstance(val, Lazy)
    assert val.evaluate() == 'a'



# Generated at 2022-06-14 04:18:29.855557
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.success(1).to_lazy().force() == Validation.success(1)


# Generated at 2022-06-14 04:18:33.126974
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1) == Validation.success(1).to_lazy()
    assert Lazy(lambda: None) == Validation.fail([1]).to_lazy()


# Generated at 2022-06-14 04:18:43.667705
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Test Validation to Lazy conversion.
    """
    v = Validation.success(1)
    l = v.to_lazy()
    assert v.value == l.value()
    assert l.success == v.is_success()

    v = Validation.success('text')
    l = v.to_lazy()
    assert v.value == l.value()
    assert l.success == v.is_success()

    v = Validation.fail(['error'])
    l = v.to_lazy()
    assert v.value == l.value()
    assert l.success == v.is_success()

    v = Validation.fail([1, 'error'])
    l = v.to_lazy()
    assert v.value == l.value()

# Generated at 2022-06-14 04:18:47.065360
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.validation import Validation
    from pymonet.lazy import Lazy

    # When: Lazy monad is created from valid Validation
    lazy_monad = Validation.success(2).to_lazy()

    # Then: Lazy monad has correct value
    assert lazy_monad == Lazy(lambda: 2)


# Generated at 2022-06-14 04:18:49.001772
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation(1, []).to_lazy().value() == 1


# Generated at 2022-06-14 04:18:52.178993
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy
    assert Lazy(lambda: 'a') == Validation.success('a').to_lazy()


# Generated at 2022-06-14 04:18:57.214956
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad import _monad_composition
    from pymonet.lazy import Lazy

    assert _monad_composition(Lazy.just(1), Validation.success,
                              Validation.fail, Validation.success,
                              Validation.fail, Validation.success) == Validation.success(Lazy.just(1))


# Generated at 2022-06-14 04:19:00.461339
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    validation = Validation.success(1)
    lazy = validation.to_lazy()
    assert lazy.value() == 1
    validation = Validation.fail(['error'])
    lazy = validation.to_lazy()
    assert lazy.value() is None


# Generated at 2022-06-14 04:19:25.294731
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.maybe import Maybe
    from pymonet.monad_try import Try
    from pymonet.monad_try import Unit
    from pymonet.box import Box

    assert(Try(42).to_lazy() == Lazy(Unit(42)))
    assert(Maybe(42).to_lazy() == Lazy(Unit(42)))
    assert(Box(42).to_lazy() == Lazy(Unit(42)))

# Generated at 2022-06-14 04:19:32.666483
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy(): # pragma: no cover
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail().to_lazy() == Lazy(lambda: None)
    assert Validation.success(1).to_try() == Try(1)
    assert Validation.fail([2]).to_try() == Try(None, is_success=False)


# Generated at 2022-06-14 04:19:35.440834
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    validation = Validation.success('X')
    assert validation.to_lazy() == Lazy(lambda: 'X')
    assert validation.to_lazy().get() == 'X'

    validation = Validation.fail()
    assert validation.to_lazy().get() is None

# Generated at 2022-06-14 04:19:42.186718
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Validation.success(5).to_lazy() == Lazy(lambda: 5)
    assert Validation.fail(['error']).to_lazy() == Lazy(lambda: None)
    assert Lazy(lambda: 5).to_validation() == Validation.success(5)
    assert Lazy(lambda: None).to_validation() == Validation.fail()


# Generated at 2022-06-14 04:19:44.614145
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    val = Validation.success('result')
    assert val.to_lazy() == Lazy(lambda: 'result')

# Generated at 2022-06-14 04:19:50.687717
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    print(Validation.success(5).to_lazy().map(lambda a: a * 2).force())
    print(Validation.fail(['error']).to_lazy().map(lambda a: a * 2).force())
    print(Validation.fail([]).to_lazy().map(lambda a: a * 2).force())


# Generated at 2022-06-14 04:19:57.916984
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.either import Left, Right
    from pymonet.lazy import Lazy

    val_success = Validation.success('result')
    assert val_success.to_lazy() == Lazy(lambda: 'result')

    val_fail = Validation.fail(['error 1', 'error 2'])
    assert val_fail.to_lazy() == Lazy(lambda: None)

# Generated at 2022-06-14 04:20:01.282023
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Unit test for method to_lazy of class Validation.
    """
    from pymonet.lazy import Lazy

    lazy = Validation.success(1).to_lazy()
    assert lazy.force() == 1, "Validation.to_lazy test failed"
    assert isinstance(lazy, Lazy), "Validation.to_lazy test failed"


# Generated at 2022-06-14 04:20:04.785595
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation
    v = Validation(5, [])
    assert v.to_lazy() == Lazy(lambda: 5)

# Generated at 2022-06-14 04:20:07.338135
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    lazy = Validation.success(1).to_lazy()
    assert lazy == Lazy(lambda: 1)


# Generated at 2022-06-14 04:20:50.648822
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy(): # pragma: no cover
    from pymonet.lazy import Lazy

    validation = Validation.success(lambda: 1)
    assert Lazy.from_function(lambda: 1) == validation.to_lazy()
    assert Lazy.from_function(lambda: None) == validation.to_lazy()
    assert Lazy.from_value(None) == validation.to_lazy()


# Generated at 2022-06-14 04:20:55.558812
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(42).to_lazy() == Lazy(lambda: 42)
    assert Validation.fail([1,2,3]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:21:00.307048
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    assert Validation.fail(1).to_lazy() == Lazy(None)
    assert Validation.success(1).to_lazy() == Lazy(1)


# Generated at 2022-06-14 04:21:04.379389
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    assert Validation(1, [2]).to_lazy() == Lazy(lambda: 1)
    assert Validation(None, [2]).to_lazy() == Lazy(lambda: None)

# Generated at 2022-06-14 04:21:07.080111
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(5).to_lazy() == Lazy(lambda: 5)



# Generated at 2022-06-14 04:21:09.141199
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(value=10).to_lazy().value() == 10
    assert Validation.fail(errors=[10, 20]).to_lazy().value() is None


# Generated at 2022-06-14 04:21:17.588116
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    def validate(value):
        try:
            int(value)
        except Exception as e:
            return Validation.fail([e])
        return Validation.success(value)

    value = Validation.success('1')
    value_ = validate(value.value)
    assert value.to_lazy() == value_.to_lazy()


if __name__ == '__main__':
    from pymonet.tools import run_doctest
    run_doctest()

# Generated at 2022-06-14 04:21:19.770129
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    def test():
        return Validation.success(9)
    lazy = Validation.success(test).to_lazy()
    assert lazy.take() == 9



# Generated at 2022-06-14 04:21:25.176012
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Test method to_lazy() of class Validation.

    :return: TEST_CASE_PASSED
    :rtype: String
    """
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    VALUE = 1
    is_success = True
    validation = Validation(VALUE, [])
    lazy = validation.to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy() == VALUE

    VALUE = None
    is_success = False
    validation = Validation(VALUE, [])
    lazy = validation.to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy() == VALUE

    return TEST_CASE_PASSED
