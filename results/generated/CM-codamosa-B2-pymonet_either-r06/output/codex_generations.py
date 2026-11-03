

# Generated at 2026-11-02 17:11:19.509024
# Unit test for method to_maybe of class Right
def test_Right_to_maybe():
    from pymonet.maybe import Maybe

    right = Right(42)
    maybe = right.to_maybe()

    assert isinstance(maybe, Maybe)
    assert maybe.is_just is True
    assert maybe.value == 42

# Generated at 2026-11-02 17:11:32.909093
# Unit test for method to_validation of class Right
def test_Right_to_validation():
    right = Right(42)

    validation = right.to_validation()

    assert validation == Validation.success(42)
    assert validation.value == 42
    assert validation.errors == []
    assert validation.is_success() is True
    assert validation.is_fail() is False

# Generated at 2026-11-02 17:11:49.376875
# Unit test for method to_validation of class Right
def test_Right_to_validation():
    from pymonet.validation import Validation

    either = Right(42)
    validation = either.to_validation()

    assert validation == Validation.success(42)
    assert validation.value == 42
    assert validation.errors == []

# Generated at 2026-11-02 17:11:52.552255
# Unit test for constructor of class Right
def test_Right():
    right = Right(42)
    assert right.value == 42
    assert right.is_right() is True
    assert right.is_left() is False
    assert right == Right(42)
    assert right != Left(42)

# Generated at 2026-11-02 17:11:59.469808
# Unit test for method ap of class Left
def test_Left_ap():
    left = Left(42)
    result = left.ap(Right(lambda value: value + 1))

    # ap on Left ignores the applicative and returns a copy of self
    assert result == Left(42)
    assert result is not left
    assert result.is_left() is True
    assert result.is_right() is False

    # works regardless of the argument passed
    assert left.ap(Left(lambda value: value)) == Left(42)

# Generated at 2026-11-02 17:12:04.959509
# Unit test for method to_try of class Either
def test_Either_to_try():
    from pymonet.monad_try import Try

    # Right should transform into a successful Try with the same value
    right = Right(42)
    try_from_right = right.to_try()
    assert isinstance(try_from_right, Try)
    assert try_from_right.is_success() is True
    assert try_from_right.value == 42

    # Left should transform into a failed Try with the same value
    left = Left('error')
    try_from_left = left.to_try()
    assert isinstance(try_from_left, Try)
    assert try_from_left.is_success() is False
    assert try_from_left.value == 'error'

    # Right with a falsy value should still be a successful Try
    try_from_right_falsy = Right(0).to_try()
    assert try_from_right_falsy.is_success() is True
    assert try_from_right_falsy.value == 0

    # Left with a falsy value should still be a failed Try
    try_from_left_falsy = Left(None).to_try()
    assert try_from_left_falsy.is_success() is False
    assert try_from_left_falsy.value is None

# Generated at 2026-11-02 17:12:15.009372
# Unit test for method to_try of class Either
def test_Either_to_try():
    from pymonet.monad_try import Try
    from pymonet.either import Left, Right

    # Right should be transformed into successfully resolved Try
    right = Right(42)
    try_result = right.to_try()

    assert isinstance(try_result, Try)
    assert try_result.value == 42
    assert try_result.is_success is True
    assert try_result == Try(42, is_success=True)

    # Left should be transformed into failed Try
    left = Left('error')
    try_result = left.to_try()

    assert isinstance(try_result, Try)
    assert try_result.value == 'error'
    assert try_result.is_success is False
    assert try_result == Try('error', is_success=False)

    # Transformed Try should not be equal to Try with different success flag
    assert Right(1).to_try() != Left(1).to_try()

    # Value kept inside Try should be usable
    assert Right(10).to_try().map(lambda x: x * 2).value == 20

# Generated at 2026-11-02 17:12:19.991824
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    # Right Either should produce a Lazy returning its value
    right = Right(42)
    lazy = right.to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy() == 42

    # Left Either should produce a Lazy returning its value
    left = Left('error')
    lazy = left.to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy() == 'error'

# Generated at 2026-11-02 17:12:26.271582
# Unit test for method case of class Either
def test_Either_case():
    from unittest.mock import MagicMock

    from pymonet.either import Left, Right

    error_mock = MagicMock(return_value='error_result')
    success_mock = MagicMock(return_value='success_result')

    # Right should call the success handler with its value
    right = Right(42)
    result = right.case(error_mock, success_mock)

    assert result == 'success_result'
    success_mock.assert_called_once_with(42)
    error_mock.assert_not_called()

    error_mock.reset_mock()
    success_mock.reset_mock()

    # Left should call the error handler with its value
    left = Left('oops')
    result = left.case(error_mock, success_mock)

    assert result == 'error_result'
    error_mock.assert_called_once_with('oops')
    success_mock.assert_not_called()

# Generated at 2026-11-02 17:12:31.870646
# Unit test for method to_try of class Either
def test_Either_to_try():
    from pymonet.monad_try import Try

    # Right should be transformed into a successfully resolved Try
    right = Right(42)
    try_right = right.to_try()

    assert isinstance(try_right, Try)
    assert try_right.value == 42
    assert try_right.is_success is True
    assert try_right == Try(42, is_success=True)

    # Left should be transformed into a failed (not resolved) Try
    left = Left('error')
    try_left = left.to_try()

    assert isinstance(try_left, Try)
    assert try_left.value == 'error'
    assert try_left.is_success is False
    assert try_left == Try('error', is_success=False)

    # Both results should not be equal to each other
    assert try_right != try_left

# Generated at 2026-11-02 17:12:42.263878
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """Unit test for method to_lazy of class Either"""
    from pymonet.lazy import Lazy

    # Test with Right
    either = Right(42)
    lazy = either.to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy.get() == 42
    assert lazy.is_evaluated is True

    # Test with Left
    either = Left('error')
    lazy = either.to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy.get() == 'error'
    assert lazy.is_evaluated is True

    # Test laziness - value is not evaluated until get() is called
    lazy = Right(100).to_lazy()
    assert lazy.is_evaluated is False
    assert lazy.value is None
    assert lazy.get() == 100

    # Test with object identity preservation
    custom_value = object()
    lazy = Right(custom_value).to_lazy()
    assert lazy.get() is custom_value

    # Test fold over the lazy value
    lazy = Right(5).to_lazy()
    assert lazy.fold(lambda value: value + 1) == 6

# Generated at 2026-11-02 17:12:49.457428
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    # Either base class
    lazy = Either(42).to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.fold(lambda value: value) == 42

    # Left
    left_lazy = Left(42).to_lazy()
    assert isinstance(left_lazy, Lazy)
    assert left_lazy.fold(lambda value: value) == 42

    # Right
    right_lazy = Right(42).to_lazy()
    assert isinstance(right_lazy, Lazy)
    assert right_lazy.fold(lambda value: value) == 42

# Generated at 2026-11-02 17:12:58.450429
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """Unit test for method to_lazy of class Either."""
    from pymonet.lazy import Lazy

    # Right should be transformed into Lazy returning its value
    right = Right(42)
    lazy = right.to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.get() == 42

    # Left should be transformed into Lazy returning its value too
    left = Left('error')
    lazy_left = left.to_lazy()
    assert isinstance(lazy_left, Lazy)
    assert lazy_left.get() == 'error'

    # to_lazy should not be evaluated eagerly
    right_none = Right(None)
    lazy_none = right_none.to_lazy()
    assert isinstance(lazy_none, Lazy)
    assert lazy_none.get() is None

# Generated at 2026-11-02 17:13:02.938684
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # Left vs Left with equal values
    assert Left(1) == Left(1)
    assert Left('test') == Left('test')

    # Right vs Right with equal values
    assert Right(1) == Right(1)
    assert Right('test') == Right('test')

    # Left vs Right with equal values should not be equal
    assert not Left(1) == Right(1)
    assert not Right(1) == Left(1)

    # Different values should not be equal
    assert not Left(1) == Left(2)
    assert not Right(1) == Right(2)

    # Comparison with non-Either objects should be False
    assert not Left(1) == 1
    assert not Right(1) == 1
    assert not Left(1) == 'Left'
    assert not Right(1) == None
    assert not Left(1) == [1]

    # Inequality operator
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)
    assert not Left(1) != Left(1)
    assert not Right(1) != Right(1)

    # Comparison with other monad-like objects should be False
    from pymonet.box import Box
    assert not Left(1) == Box(1)
    assert not Right(1) == Box(1)

# Generated at 2026-11-02 17:13:08.436449
# Unit test for method to_try of class Either
def test_Either_to_try():
    from pymonet.monad_try import Try
    from pymonet.either import Left, Right

    # Right should be transformed into a successfully resolved Try
    right = Right(42)
    try_monad = right.to_try()

    assert isinstance(try_monad, Try)
    assert try_monad.is_success is True
    assert try_monad.value == 42

    # Left should be transformed into a non-resolved (failed) Try
    left = Left('error')
    try_monad = left.to_try()

    assert isinstance(try_monad, Try)
    assert try_monad.is_success is False
    assert try_monad.value == 'error'

# Generated at 2026-11-02 17:13:14.460852
# Unit test for method case of class Either
def test_Either_case():
    error_handler = lambda value: 'error: {}'.format(value)
    success_handler = lambda value: 'success: {}'.format(value)

    # Left should call the error handler with its value
    assert Left('left_value').case(error_handler, success_handler) == 'error: left_value'

    # Right should call the success handler with its value
    assert Right('right_value').case(error_handler, success_handler) == 'success: right_value'

    # Only one handler should be called per invocation
    called = []

    def tracking_error(value):
        called.append(('error', value))
        return 'error'

    def tracking_success(value):
        called.append(('success', value))
        return 'success'

    Left('l').case(tracking_error, tracking_success)
    assert called == [('error', 'l')]

    called = []
    Right('r').case(tracking_error, tracking_success)
    assert called == [('success', 'r')]

# Generated at 2026-11-02 17:13:22.404482
# Unit test for method case of class Either
def test_Either_case():
    from pymonet.either import Left, Right

    error_calls = []
    success_calls = []

    def error_handler(value):
        error_calls.append(value)
        return 'error: {}'.format(value)

    def success_handler(value):
        success_calls.append(value)
        return 'success: {}'.format(value)

    # Right should call only the success handler with its value
    right = Right(42)
    assert right.case(error_handler, success_handler) == 'success: 42'
    assert success_calls == [42]
    assert error_calls == []

    # Left should call only the error handler with its value
    left = Left('oops')
    assert left.case(error_handler, success_handler) == 'error: oops'
    assert error_calls == ['oops']
    assert success_calls == [42]

    # case should work with chained transformations as well
    assert Right(10).map(lambda x: x + 1).case(error_handler, success_handler) == 'success: 11'
    assert Left(10).map(lambda x: x + 1).case(error_handler, success_handler) == 'error: 10'

# Generated at 2026-11-02 17:13:41.189959
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    # Right either should transform into Lazy wrapping its value
    right = Right(42)
    lazy = right.to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.fn() == 42

    # Left either should transform into Lazy wrapping its value as well
    left = Left('error')
    lazy = left.to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.fn() == 'error'

# Generated at 2026-11-02 17:14:01.494441
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    # Right is transformed into Lazy which resolves to stored value
    either = Right(42)
    lazy = either.to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.get_value() == 42

    # Left is also transformed into Lazy which resolves to stored value
    either = Left('error')
    lazy = either.to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.get_value() == 'error'

# Generated at 2026-11-02 17:14:06.422029
# Unit test for method case of class Either
def test_Either_case():
    assert Left(42).case(lambda value: value + 1, lambda value: value + 2) == 43
    assert Right(42).case(lambda value: value + 1, lambda value: value + 2) == 44

# Generated at 2026-11-02 17:14:16.395034
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    # Test transformation from Right to Lazy
    right = Right(42)
    lazy = right.to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.fold(lambda value: value) == 42

    # Test transformation from Left to Lazy
    left = Left('error')
    lazy = left.to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.fold(lambda value: value) == 'error'

    # Test that Lazy holds the correct value for various types
    assert Right({'key': 'value'}).to_lazy().fold(lambda value: value) == {'key': 'value'}
    assert Left(None).to_lazy().fold(lambda value: value) is None

# Generated at 2026-11-02 17:14:23.384708
# Unit test for method case of class Either
def test_Either_case():
    error_handler_calls = []
    success_handler_calls = []

    def error_handler(value):
        error_handler_calls.append(value)
        return 'error: {}'.format(value)

    def success_handler(value):
        success_handler_calls.append(value)
        return 'success: {}'.format(value)

    # Right should call only the success handler with its value
    right = Right(42)
    assert right.case(error_handler, success_handler) == 'success: 42'
    assert error_handler_calls == []
    assert success_handler_calls == [42]

    # Left should call only the error handler with its value
    left = Left('oops')
    assert left.case(error_handler, success_handler) == 'error: oops'
    assert error_handler_calls == ['oops']
    assert success_handler_calls == [42]

    # Handlers can transform the wrapped value
    assert Right(10).case(lambda x: x + 1, lambda x: x * 2) == 20
    assert Left(10).case(lambda x: x + 1, lambda x: x * 2) == 11

# Generated at 2026-11-02 17:14:32.158391
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    # Right value transformed to Lazy
    either_right = Right(42)
    lazy = either_right.to_lazy()

    assert isinstance(lazy, Lazy)
    assert not lazy.is_evaluated()
    assert lazy.get() == 42
    assert lazy.is_evaluated()

    # Left value transformed to Lazy
    either_left = Left('error')
    lazy_left = either_left.to_lazy()

    assert isinstance(lazy_left, Lazy)
    assert not lazy_left.is_evaluated()
    assert lazy_left.get() == 'error'
    assert lazy_left.is_evaluated()

    # Equality check between lazies created from Either
    assert Right(1).to_lazy() == Right(1).to_lazy()

# Generated at 2026-11-02 17:14:39.605179
# Unit test for method case of class Either
def test_Either_case():
    from pymonet.either import Left, Right

    # Test Left: error function should be called with the value
    error_called = []
    success_called = []

    left = Left('error_value')
    result = left.case(
        lambda value: error_called.append(value) or 'error handled',
        lambda value: success_called.append(value) or 'success handled'
    )

    assert result == 'error handled'
    assert error_called == ['error_value']
    assert success_called == []

    # Test Right: success function should be called with the value
    error_called = []
    success_called = []

    right = Right('success_value')
    result = right.case(
        lambda value: error_called.append(value) or 'error handled',
        lambda value: success_called.append(value) or 'success handled'
    )

    assert result == 'success handled'
    assert error_called == []
    assert success_called == ['success_value']

    # Test that case returns the result of the applied function
    left = Left(10)
    right = Right(10)

    assert left.case(lambda x: x + 1, lambda x: x * 2) == 11
    assert right.case(lambda x: x + 1, lambda x: x * 2) == 20

# Generated at 2026-11-02 17:14:47.215451
# Unit test for method case of class Either
def test_Either_case():from pymonet.either import Left, Right


def test_Either_case_should_call_success_function_when_either_is_right():
    def success_mock(value):
        return 'success_called_with_{}'.format(value)

    def error_mock(value):
        return 'error_called_with_{}'.format(value)

    either = Right(42)

    assert either.case(error_mock, success_mock) == 'success_called_with_42'


def test_Either_case_should_call_error_function_when_either_is_left():
    def success_mock(value):
        return 'success_called_with_{}'.format(value)

    def error_mock(value):
        return 'error_called_with_{}'.format(value)

    either = Left(42)

    assert either.case(error_mock, success_mock) == 'error_called_with_42'


def test_Either_case_should_call_only_success_function_when_either_is_right():
    called = []

    def success_mock(value):
        called.append('success')

        return 'success'

    def error_mock(value):
        called.append('error')

        return 'error'

    either = Right(42)
    result = either.case(error_mock, success_mock)

    assert result == 'success'
    assert called == ['success']


def test_Either_case_should_call_only_error_function_when_either_is_left():
    called = []

    def success_mock(value):
        called.append('success')

        return 'success'

    def error_mock(value):
        called.append('error')

        return 'error'

    either = Left(42)
    result = either.case(error_mock, success_mock)

    assert result == 'error'
    assert called == ['error']

# Generated at 2026-11-02 17:15:21.375960
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """Unit test for method to_lazy of class Either"""
    from pymonet.lazy import Lazy

    right = Right(42)
    lazy = right.to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.force() == 42

    left = Left('error')
    lazy = left.to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.force() == 'error'

# Generated at 2026-11-02 17:15:29.444217
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    # Right case
    right_either = Right(42)
    lazy_from_right = right_either.to_lazy()
    assert isinstance(lazy_from_right, Lazy)
    assert lazy_from_right.is_evaluated is False
    assert lazy_from_right() == 42
    assert lazy_from_right.is_evaluated is True

    # Left case
    left_either = Left(42)
    lazy_from_left = left_either.to_lazy()
    assert isinstance(lazy_from_left, Lazy)
    assert lazy_from_left.is_evaluated is False
    assert lazy_from_left() == 42
    assert lazy_from_left.is_evaluated is True

    # Value is preserved exactly (including None)
    assert Right(None).to_lazy()() is None
    assert Left(None).to_lazy()() is None

    # Lazy returned wraps the original value, evaluated lazily each time
    lazy = Right(100).to_lazy()
    assert lazy() == 100
    assert lazy() == 100

# Generated at 2026-11-02 17:16:02.739864
# Unit test for method to_lazy of class Either

# Generated at 2026-11-02 17:16:16.846897
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():from pymonet.lazy import Lazy


# Generated at 2026-11-02 17:16:21.272661
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    # Left case
    left_either = Left('error_value')
    lazy_from_left = left_either.to_lazy()
    assert isinstance(lazy_from_left, Lazy)
    assert lazy_from_left.is_evaluated is False
    assert lazy_from_left() == 'error_value'
    assert lazy_from_left.is_evaluated is True

    # Right case
    right_either = Right('success_value')
    lazy_from_right = right_either.to_lazy()
    assert isinstance(lazy_from_right, Lazy)
    assert lazy_from_right.is_evaluated is False
    assert lazy_from_right() == 'success_value'
    assert lazy_from_right.is_evaluated is True

# Generated at 2026-11-02 17:16:32.296179
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.either import Left, Right

    # to_lazy on Right should produce a Lazy monad wrapping the value
    right_either = Right(42)
    lazy_from_right = right_either.to_lazy()
    assert isinstance(lazy_from_right, Lazy)
    assert lazy_from_right.fold() == 42

    # to_lazy on Left should also produce a Lazy monad wrapping the value
    left_either = Left('error')
    lazy_from_left = left_either.to_lazy()
    assert isinstance(lazy_from_left, Lazy)
    assert lazy_from_left.fold() == 'error'

    # Lazy should be evaluated lazily and cache the result
    lazy = Right(100).to_lazy()
    assert lazy.is_evaluated is False
    assert lazy.fold() == 100
    assert lazy.is_evaluated is True
    assert lazy.fold() == 100

# Generated at 2026-11-02 17:16:56.548431
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    right = Right(42)
    lazy = right.to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.get() == 42

    left = Left('error')
    lazy = left.to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.get() == 'error'

# Generated at 2026-11-02 17:17:07.970322
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    # to_lazy on Right should return a Lazy evaluating to the stored value
    right = Right(42)
    lazy = right.to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy.fold(lambda value: value) == 42

    # to_lazy on Left should return a Lazy evaluating to the stored value
    left = Left('error')
    lazy_left = left.to_lazy()

    assert isinstance(lazy_left, Lazy)
    assert lazy_left.fold(lambda value: value) == 'error'

# Generated at 2026-11-02 17:17:15.044277
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    # Right case: should return Lazy monad wrapping the value
    either_right = Right(42)
    lazy = either_right.to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy.get() == 42

    # Left case: should also return Lazy monad wrapping the value
    either_left = Left(0)
    lazy_left = either_left.to_lazy()

    assert isinstance(lazy_left, Lazy)
    assert lazy_left.get() == 0

# Generated at 2026-11-02 17:17:51.403514
# Unit test for method to_lazy of class Either

# Generated at 2026-11-02 17:17:59.627589
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():from pymonet.either import Left, Right

# Generated at 2026-11-02 17:19:05.834272
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    right_either = Right(42)
    right_lazy = right_either.to_lazy()
    assert isinstance(right_lazy, Lazy)
    assert right_lazy.get() == 42

    left_either = Left('error')
    left_lazy = left_either.to_lazy()
    assert isinstance(left_lazy, Lazy)
    assert left_lazy.get() == 'error'

# Generated at 2026-11-02 17:19:43.149160
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    '''Unit test for method Either.to_lazy'''
    from pymonet.either import Left, Right
    from pymonet.lazy import Lazy

    # Right instance transforms into a Lazy holding its value
    right = Right(42)
    lazy_right = right.to_lazy()
    assert isinstance(lazy_right, Lazy)
    assert lazy_right.get_value() == 42

    # Left instance transforms into a Lazy holding its value too
    left = Left('error')
    lazy_left = left.to_lazy()
    assert isinstance(lazy_left, Lazy)
    assert lazy_left.get_value() == 'error'

    # repeated evaluation returns the same (cached) value
    assert lazy_right.get_value() == 42
    assert lazy_left.get_value() == 'error'