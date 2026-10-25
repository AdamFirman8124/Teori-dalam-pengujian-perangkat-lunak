

# Generated at 2026-10-24 02:00:56.796315
# Unit test for method is_right of class Right
def test_Right_is_right():
    from pymonet.either import Right, Left

    assert Right(42).is_right() is True
    assert Right(None).is_right() is True   # right-ness is independent of value
    assert Left("error").is_right() is False

# Generated at 2026-10-24 02:01:11.028941
# Unit test for method is_right of class Either
def test_Either_is_right():
    assert Left("error").is_right() is False
    assert Right("value").is_right() is True

    # result is independent of wrapped value:
    assert Left(None).is_right() is False
    assert Right(None).is_right() is True
    assert Left(0).is_right() is False
    assert Right(0).is_right() is True

    # base class default implementation returns None (pass):
    assert Either("value").is_right() is None

# Generated at 2026-10-24 02:01:31.815621
# Unit test for method map of class Left
def test_Left_map():
    mapper_called = False

    def mapper(x):
        nonlocal mapper_called
        mapper_called = True
        return x + 1

    result = Left(42).map(mapper)

    assert result == Left(42)
    assert result.value == 42
    assert result.is_left()
    assert not result.is_right()
    assert not mapper_called

# Generated at 2026-10-24 02:01:40.045019
# Unit test for method is_left of class Left
def test_Left_is_left():
    assert Left("error").is_left() is True
    assert Left(None).is_left() is True
    assert Left(0).is_left() is True

# Generated at 2026-10-24 02:02:34.087139
# Unit test for method to_maybe of class Left
def test_Left_to_maybe():
    from pymonet.maybe import Maybe

    assert Left(42).to_maybe() == Maybe.nothing()

# Generated at 2026-10-24 02:03:01.151200
# Unit test for method ap of class Either
def test_Either_ap():
    # Right: ap applies the function inside the applicative to the value
    assert Right(1).ap(Right(lambda value: value + 1)) == Right(2)

    # Right: ap works with a function taking the value
    assert Right('hello').ap(Right(lambda value: value.upper())) == Right('HELLO')

    # Left: ap short-circuits and returns a copy of Left with the same value
    assert Left('error').ap(Right(lambda value: value + 1)) == Left('error')

    # Left: ap ignores the applicative entirely
    assert Left('error').ap(Left('other')) == Left('error')

# Generated at 2026-10-24 02:03:09.198258
# Unit test for method to_maybe of class Right
def test_Right_to_maybe():
    assert Right(42).to_maybe() == Maybe.just(42)

# Generated at 2026-10-24 02:03:17.594914
# Unit test for method ap of class Left
def test_Left_ap():
    left = Left(42)

    # Left ignores the applicative, even when it holds a function
    result = left.ap(Right(lambda x: x + 1))
    assert result == Left(42)
    assert result is not left          # returns a copy, not self

    # Same result regardless of what is passed in
    assert Left(42).ap(Left(lambda x: x + 1)) == Left(42)
    assert Left('error').ap(Right(lambda x: x + 1)) == Left('error')

# Generated at 2026-10-24 02:03:18.922678
# Unit test for method ap of class Either
def test_Either_ap():
    # Right: ap applies the function inside the applicative to the value
    assert Right(1).ap(Right(lambda value: value + 1)) == Right(2)

    # Right: ap works with a function taking the value
    assert Right('hello').ap(Right(lambda value: value.upper())) == Right('HELLO')

    # Left: ap short-circuits and returns a copy of Left with the same value
    assert Left('error').ap(Right(lambda value: value + 1)) == Left('error')

    # Left: ap ignores the applicative entirely
    assert Left('error').ap(Left('other')) == Left('error')

# Generated at 2026-10-24 02:03:40.533649
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    right = Right(42)
    lazy_right = right.to_lazy()
    assert isinstance(lazy_right, Lazy)
    assert lazy_right.get() == 42

    left = Left('error')
    lazy_left = left.to_lazy()
    assert isinstance(lazy_left, Lazy)
    assert lazy_left.get() == 'error'

# Generated at 2026-10-24 02:04:08.807262
# Unit test for method to_box of class Either
def test_Either_to_box():
    right_box = Right(42).to_box()
    left_box = Left("error").to_box()

    assert isinstance(right_box, Box)
    assert right_box.value == 42

    assert isinstance(left_box, Box)
    assert left_box.value == "error"

# Generated at 2026-10-24 02:04:25.319146
# Unit test for method to_box of class Either
def test_Either_to_box():
    right_box = Right(42).to_box()
    left_box = Left("error").to_box()

    assert isinstance(right_box, Box)
    assert right_box.value == 42

    assert isinstance(left_box, Box)
    assert left_box.value == "error"

# Generated at 2026-10-24 02:04:26.716916
# Unit test for method ap of class Either
def test_Either_ap():
    # Right: ap applies the function inside the applicative to the value
    assert Right(1).ap(Right(lambda value: value + 1)) == Right(2)

    # Right: ap works with a function taking the value
    assert Right('hello').ap(Right(lambda value: value.upper())) == Right('HELLO')

    # Left: ap short-circuits and returns a copy of Left with the same value
    assert Left('error').ap(Right(lambda value: value + 1)) == Left('error')

    # Left: ap ignores the applicative entirely
    assert Left('error').ap(Left('other')) == Left('error')

# Generated at 2026-10-24 02:04:29.459063
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    right = Right(42)
    lazy_right = right.to_lazy()
    assert isinstance(lazy_right, Lazy)
    assert lazy_right.get() == 42

    left = Left('error')
    lazy_left = left.to_lazy()
    assert isinstance(lazy_left, Lazy)
    assert lazy_left.get() == 'error'

# Generated at 2026-10-24 02:04:30.931416
# Unit test for method to_maybe of class Right
def test_Right_to_maybe():
    assert Right(42).to_maybe() == Maybe.just(42)

# Generated at 2026-10-24 02:04:32.235831
# Unit test for method ap of class Left
def test_Left_ap():
    left = Left(42)

    # Left ignores the applicative, even when it holds a function
    result = left.ap(Right(lambda x: x + 1))
    assert result == Left(42)
    assert result is not left          # returns a copy, not self

    # Same result regardless of what is passed in
    assert Left(42).ap(Left(lambda x: x + 1)) == Left(42)
    assert Left('error').ap(Right(lambda x: x + 1)) == Left('error')

# Generated at 2026-10-24 02:05:04.504093
# Unit test for method case of class Either
def test_Either_case():
    # Right -> only `success` is called, with the Right value, and its result is returned
    success = Mock(return_value='success-result')
    error = Mock(return_value='error-result')
    right = Right(42)

    assert right.case(error, success) == 'success-result'
    success.assert_called_once_with(42)
    error.assert_not_called()

    # Left -> only `error` is called, with the Left value, and its result is returned
    success = Mock(return_value='success-result')
    error = Mock(return_value='error-result')
    left = Left('boom')

    assert left.case(error, success) == 'error-result'
    error.assert_called_once_with('boom')
    success.assert_not_called()

    # The handler's own return value (of any type) is passed through unchanged
    assert Right(1).case(lambda _: None, lambda v: v + 1) == 2
    assert Left(1).case(lambda v: v - 1, lambda _: None) == 0

# Generated at 2026-10-24 02:05:05.866094
# Unit test for method map of class Left
def test_Left_map():
    mapper_called = False

    def mapper(x):
        nonlocal mapper_called
        mapper_called = True
        return x + 1

    result = Left(42).map(mapper)

    assert result == Left(42)
    assert result.value == 42
    assert result.is_left()
    assert not result.is_right()
    assert not mapper_called

# Generated at 2026-10-24 02:05:14.104833
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:05:15.420090
# Unit test for method map of class Left
def test_Left_map():
    mapper_called = False

    def mapper(x):
        nonlocal mapper_called
        mapper_called = True
        return x + 1

    result = Left(42).map(mapper)

    assert result == Left(42)
    assert result.value == 42
    assert result.is_left()
    assert not result.is_right()
    assert not mapper_called

# Generated at 2026-10-24 02:05:16.731095
# Unit test for method case of class Either
def test_Either_case():
    # Right -> only `success` is called, with the Right value, and its result is returned
    success = Mock(return_value='success-result')
    error = Mock(return_value='error-result')
    right = Right(42)

    assert right.case(error, success) == 'success-result'
    success.assert_called_once_with(42)
    error.assert_not_called()

    # Left -> only `error` is called, with the Left value, and its result is returned
    success = Mock(return_value='success-result')
    error = Mock(return_value='error-result')
    left = Left('boom')

    assert left.case(error, success) == 'error-result'
    error.assert_called_once_with('boom')
    success.assert_not_called()

    # The handler's own return value (of any type) is passed through unchanged
    assert Right(1).case(lambda _: None, lambda v: v + 1) == 2
    assert Left(1).case(lambda v: v - 1, lambda _: None) == 0

# Generated at 2026-10-24 02:05:18.044810
# Unit test for method case of class Either
def test_Either_case():
    # Right -> only `success` is called, with the Right value, and its result is returned
    success = Mock(return_value='success-result')
    error = Mock(return_value='error-result')
    right = Right(42)

    assert right.case(error, success) == 'success-result'
    success.assert_called_once_with(42)
    error.assert_not_called()

    # Left -> only `error` is called, with the Left value, and its result is returned
    success = Mock(return_value='success-result')
    error = Mock(return_value='error-result')
    left = Left('boom')

    assert left.case(error, success) == 'error-result'
    error.assert_called_once_with('boom')
    success.assert_not_called()

    # The handler's own return value (of any type) is passed through unchanged
    assert Right(1).case(lambda _: None, lambda v: v + 1) == 2
    assert Left(1).case(lambda v: v - 1, lambda _: None) == 0

# Generated at 2026-10-24 02:05:25.699392
# Unit test for method to_validation of class Right
def test_Right_to_validation():import unittest

from pymonet.either import Right
from pymonet.validation import Validation


class TestRightToValidation(unittest.TestCase):

    def test_Right_to_validation(self):
        # returns a successful Validation holding the same value
        right = Right(42)
        validation = right.to_validation()

        self.assertIsInstance(validation, Validation)
        self.assertEqual(validation.value, 42)
        self.assertEqual(validation.errors, [])
        self.assertTrue(validation.is_success())

    def test_Right_to_validation_keeps_value_type(self):
        # works for non-int values too
        validation = Right({'key': 'value'}).to_validation()

        self.assertEqual(validation.value, {'key': 'value'})
        self.assertTrue(validation.is_success())

    def test_Right_to_validation_equivalent_to_validation_success(self):
        # consistent with calling Validation.success directly
        value = 'data'
        self.assertEqual(
            Right(value).to_validation().value,
            Validation.success(value).value
        )


if __name__ == '__main__':
    unittest.main()

# Generated at 2026-10-24 02:05:27.008502
# Unit test for method map of class Left
def test_Left_map():
    mapper_called = False

    def mapper(x):
        nonlocal mapper_called
        mapper_called = True
        return x + 1

    result = Left(42).map(mapper)

    assert result == Left(42)
    assert result.value == 42
    assert result.is_left()
    assert not result.is_right()
    assert not mapper_called

# Generated at 2026-10-24 02:05:28.335626
# Unit test for method to_validation of class Right
def test_Right_to_validation():import unittest

from pymonet.either import Right
from pymonet.validation import Validation


class TestRightToValidation(unittest.TestCase):

    def test_Right_to_validation(self):
        # returns a successful Validation holding the same value
        right = Right(42)
        validation = right.to_validation()

        self.assertIsInstance(validation, Validation)
        self.assertEqual(validation.value, 42)
        self.assertEqual(validation.errors, [])
        self.assertTrue(validation.is_success())

    def test_Right_to_validation_keeps_value_type(self):
        # works for non-int values too
        validation = Right({'key': 'value'}).to_validation()

        self.assertEqual(validation.value, {'key': 'value'})
        self.assertTrue(validation.is_success())

    def test_Right_to_validation_equivalent_to_validation_success(self):
        # consistent with calling Validation.success directly
        value = 'data'
        self.assertEqual(
            Right(value).to_validation().value,
            Validation.success(value).value
        )


if __name__ == '__main__':
    unittest.main()

# Generated at 2026-10-24 02:05:29.661120
# Unit test for method to_validation of class Right
def test_Right_to_validation():import unittest

from pymonet.either import Right
from pymonet.validation import Validation


class TestRightToValidation(unittest.TestCase):

    def test_Right_to_validation(self):
        # returns a successful Validation holding the same value
        right = Right(42)
        validation = right.to_validation()

        self.assertIsInstance(validation, Validation)
        self.assertEqual(validation.value, 42)
        self.assertEqual(validation.errors, [])
        self.assertTrue(validation.is_success())

    def test_Right_to_validation_keeps_value_type(self):
        # works for non-int values too
        validation = Right({'key': 'value'}).to_validation()

        self.assertEqual(validation.value, {'key': 'value'})
        self.assertTrue(validation.is_success())

    def test_Right_to_validation_equivalent_to_validation_success(self):
        # consistent with calling Validation.success directly
        value = 'data'
        self.assertEqual(
            Right(value).to_validation().value,
            Validation.success(value).value
        )


if __name__ == '__main__':
    unittest.main()

# Generated at 2026-10-24 02:05:30.965795
# Unit test for method map of class Left
def test_Left_map():
    mapper_called = False

    def mapper(x):
        nonlocal mapper_called
        mapper_called = True
        return x + 1

    result = Left(42).map(mapper)

    assert result == Left(42)
    assert result.value == 42
    assert result.is_left()
    assert not result.is_right()
    assert not mapper_called

# Generated at 2026-10-24 02:05:32.298335
# Unit test for method map of class Left
def test_Left_map():
    mapper_called = False

    def mapper(x):
        nonlocal mapper_called
        mapper_called = True
        return x + 1

    result = Left(42).map(mapper)

    assert result == Left(42)
    assert result.value == 42
    assert result.is_left()
    assert not result.is_right()
    assert not mapper_called

# Generated at 2026-10-24 02:05:33.616531
# Unit test for method to_validation of class Right
def test_Right_to_validation():import unittest

from pymonet.either import Right
from pymonet.validation import Validation


class TestRightToValidation(unittest.TestCase):

    def test_Right_to_validation(self):
        # returns a successful Validation holding the same value
        right = Right(42)
        validation = right.to_validation()

        self.assertIsInstance(validation, Validation)
        self.assertEqual(validation.value, 42)
        self.assertEqual(validation.errors, [])
        self.assertTrue(validation.is_success())

    def test_Right_to_validation_keeps_value_type(self):
        # works for non-int values too
        validation = Right({'key': 'value'}).to_validation()

        self.assertEqual(validation.value, {'key': 'value'})
        self.assertTrue(validation.is_success())

    def test_Right_to_validation_equivalent_to_validation_success(self):
        # consistent with calling Validation.success directly
        value = 'data'
        self.assertEqual(
            Right(value).to_validation().value,
            Validation.success(value).value
        )


if __name__ == '__main__':
    unittest.main()

# Generated at 2026-10-24 02:05:34.945198
# Unit test for method to_validation of class Right
def test_Right_to_validation():import unittest

from pymonet.either import Right
from pymonet.validation import Validation


class TestRightToValidation(unittest.TestCase):

    def test_Right_to_validation(self):
        # returns a successful Validation holding the same value
        right = Right(42)
        validation = right.to_validation()

        self.assertIsInstance(validation, Validation)
        self.assertEqual(validation.value, 42)
        self.assertEqual(validation.errors, [])
        self.assertTrue(validation.is_success())

    def test_Right_to_validation_keeps_value_type(self):
        # works for non-int values too
        validation = Right({'key': 'value'}).to_validation()

        self.assertEqual(validation.value, {'key': 'value'})
        self.assertTrue(validation.is_success())

    def test_Right_to_validation_equivalent_to_validation_success(self):
        # consistent with calling Validation.success directly
        value = 'data'
        self.assertEqual(
            Right(value).to_validation().value,
            Validation.success(value).value
        )


if __name__ == '__main__':
    unittest.main()

# Generated at 2026-10-24 02:05:37.654507
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    right = Right(42)
    lazy_right = right.to_lazy()
    assert isinstance(lazy_right, Lazy)
    assert lazy_right.get() == 42

    left = Left('error')
    lazy_left = left.to_lazy()
    assert isinstance(lazy_left, Lazy)
    assert lazy_left.get() == 'error'

# Generated at 2026-10-24 02:05:38.965336
# Unit test for method map of class Left
def test_Left_map():
    mapper_called = False

    def mapper(x):
        nonlocal mapper_called
        mapper_called = True
        return x + 1

    result = Left(42).map(mapper)

    assert result == Left(42)
    assert result.value == 42
    assert result.is_left()
    assert not result.is_right()
    assert not mapper_called

# Generated at 2026-10-24 02:05:40.272776
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:05:41.598221
# Unit test for method map of class Left
def test_Left_map():
    mapper_called = False

    def mapper(x):
        nonlocal mapper_called
        mapper_called = True
        return x + 1

    result = Left(42).map(mapper)

    assert result == Left(42)
    assert result.value == 42
    assert result.is_left()
    assert not result.is_right()
    assert not mapper_called

# Generated at 2026-10-24 02:05:42.916692
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:05:45.672504
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    right = Right(42)
    lazy_right = right.to_lazy()
    assert isinstance(lazy_right, Lazy)
    assert lazy_right.get() == 42

    left = Left('error')
    lazy_left = left.to_lazy()
    assert isinstance(lazy_left, Lazy)
    assert lazy_left.get() == 'error'

# Generated at 2026-10-24 02:05:48.541487
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    right = Right(42)
    lazy_right = right.to_lazy()
    assert isinstance(lazy_right, Lazy)
    assert lazy_right.get() == 42

    left = Left('error')
    lazy_left = left.to_lazy()
    assert isinstance(lazy_left, Lazy)
    assert lazy_left.get() == 'error'

# Generated at 2026-10-24 02:05:49.840895
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:05:51.150692
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:05:52.456185
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:05:55.193891
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    right = Right(42)
    lazy_right = right.to_lazy()
    assert isinstance(lazy_right, Lazy)
    assert lazy_right.get() == 42

    left = Left('error')
    lazy_left = left.to_lazy()
    assert isinstance(lazy_left, Lazy)
    assert lazy_left.get() == 'error'

# Generated at 2026-10-24 02:05:56.502830
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:05:57.842820
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:06:00.603553
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    right = Right(42)
    lazy_right = right.to_lazy()
    assert isinstance(lazy_right, Lazy)
    assert lazy_right.get() == 42

    left = Left('error')
    lazy_left = left.to_lazy()
    assert isinstance(lazy_left, Lazy)
    assert lazy_left.get() == 'error'

# Generated at 2026-10-24 02:06:02.052107
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:06:03.483443
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:06:04.785969
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:06:06.120853
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:06:07.431869
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:06:10.344138
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    right = Right(42)
    lazy_right = right.to_lazy()
    assert isinstance(lazy_right, Lazy)
    assert lazy_right.get() == 42

    left = Left('error')
    lazy_left = left.to_lazy()
    assert isinstance(lazy_left, Lazy)
    assert lazy_left.get() == 'error'

# Generated at 2026-10-24 02:06:13.014071
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    right = Right(42)
    lazy_right = right.to_lazy()
    assert isinstance(lazy_right, Lazy)
    assert lazy_right.get() == 42

    left = Left('error')
    lazy_left = left.to_lazy()
    assert isinstance(lazy_left, Lazy)
    assert lazy_left.get() == 'error'

# Generated at 2026-10-24 02:06:14.322096
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:06:15.635677
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:06:18.417197
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    right = Right(42)
    lazy_right = right.to_lazy()
    assert isinstance(lazy_right, Lazy)
    assert lazy_right.get() == 42

    left = Left('error')
    lazy_left = left.to_lazy()
    assert isinstance(lazy_left, Lazy)
    assert lazy_left.get() == 'error'

# Generated at 2026-10-24 02:06:19.867312
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:06:21.182319
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:06:23.939150
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    right = Right(42)
    lazy_right = right.to_lazy()
    assert isinstance(lazy_right, Lazy)
    assert lazy_right.get() == 42

    left = Left('error')
    lazy_left = left.to_lazy()
    assert isinstance(lazy_left, Lazy)
    assert lazy_left.get() == 'error'

# Generated at 2026-10-24 02:06:26.606088
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    right = Right(42)
    lazy_right = right.to_lazy()
    assert isinstance(lazy_right, Lazy)
    assert lazy_right.get() == 42

    left = Left('error')
    lazy_left = left.to_lazy()
    assert isinstance(lazy_left, Lazy)
    assert lazy_left.get() == 'error'

# Generated at 2026-10-24 02:06:29.699796
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    right = Right(42)
    lazy_right = right.to_lazy()
    assert isinstance(lazy_right, Lazy)
    assert lazy_right.get() == 42

    left = Left('error')
    lazy_left = left.to_lazy()
    assert isinstance(lazy_left, Lazy)
    assert lazy_left.get() == 'error'

# Generated at 2026-10-24 02:06:32.441718
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    right = Right(42)
    lazy_right = right.to_lazy()
    assert isinstance(lazy_right, Lazy)
    assert lazy_right.get() == 42

    left = Left('error')
    lazy_left = left.to_lazy()
    assert isinstance(lazy_left, Lazy)
    assert lazy_left.get() == 'error'

# Generated at 2026-10-24 02:06:34.103115
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:06:35.413525
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:06:38.300746
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    right = Right(42)
    lazy_right = right.to_lazy()
    assert isinstance(lazy_right, Lazy)
    assert lazy_right.get() == 42

    left = Left('error')
    lazy_left = left.to_lazy()
    assert isinstance(lazy_left, Lazy)
    assert lazy_left.get() == 'error'

# Generated at 2026-10-24 02:06:41.043465
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    right = Right(42)
    lazy_right = right.to_lazy()
    assert isinstance(lazy_right, Lazy)
    assert lazy_right.get() == 42

    left = Left('error')
    lazy_left = left.to_lazy()
    assert isinstance(lazy_left, Lazy)
    assert lazy_left.get() == 'error'

# Generated at 2026-10-24 02:06:42.434552
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:06:45.147035
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    right = Right(42)
    lazy_right = right.to_lazy()
    assert isinstance(lazy_right, Lazy)
    assert lazy_right.get() == 42

    left = Left('error')
    lazy_left = left.to_lazy()
    assert isinstance(lazy_left, Lazy)
    assert lazy_left.get() == 'error'

# Generated at 2026-10-24 02:06:46.458306
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:06:47.926236
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:06:50.998119
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    right = Right(42)
    lazy_right = right.to_lazy()
    assert isinstance(lazy_right, Lazy)
    assert lazy_right.get() == 42

    left = Left('error')
    lazy_left = left.to_lazy()
    assert isinstance(lazy_left, Lazy)
    assert lazy_left.get() == 'error'

# Generated at 2026-10-24 02:06:52.431937
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:06:53.759471
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:06:56.523311
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    right = Right(42)
    lazy_right = right.to_lazy()
    assert isinstance(lazy_right, Lazy)
    assert lazy_right.get() == 42

    left = Left('error')
    lazy_left = left.to_lazy()
    assert isinstance(lazy_left, Lazy)
    assert lazy_left.get() == 'error'

# Generated at 2026-10-24 02:06:57.832011
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:06:59.145224
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:07:00.485444
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:07:02.691409
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:07:05.622477
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    right = Right(42)
    lazy_right = right.to_lazy()
    assert isinstance(lazy_right, Lazy)
    assert lazy_right.get() == 42

    left = Left('error')
    lazy_left = left.to_lazy()
    assert isinstance(lazy_left, Lazy)
    assert lazy_left.get() == 'error'

# Generated at 2026-10-24 02:07:06.951678
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:07:08.538490
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:07:09.851433
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:07:11.160640
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:07:12.808403
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:07:14.118026
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:07:15.457870
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:07:18.544012
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    right = Right(42)
    lazy_right = right.to_lazy()
    assert isinstance(lazy_right, Lazy)
    assert lazy_right.get() == 42

    left = Left('error')
    lazy_left = left.to_lazy()
    assert isinstance(lazy_left, Lazy)
    assert lazy_left.get() == 'error'

# Generated at 2026-10-24 02:07:23.549223
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    right = Right(42)
    lazy_right = right.to_lazy()
    assert isinstance(lazy_right, Lazy)
    assert lazy_right.get() == 42

    left = Left('error')
    lazy_left = left.to_lazy()
    assert isinstance(lazy_left, Lazy)
    assert lazy_left.get() == 'error'

# Generated at 2026-10-24 02:07:24.994060
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:07:26.315566
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:07:29.087861
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    right = Right(42)
    lazy_right = right.to_lazy()
    assert isinstance(lazy_right, Lazy)
    assert lazy_right.get() == 42

    left = Left('error')
    lazy_left = left.to_lazy()
    assert isinstance(lazy_left, Lazy)
    assert lazy_left.get() == 'error'

# Generated at 2026-10-24 02:07:31.849396
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    right = Right(42)
    lazy_right = right.to_lazy()
    assert isinstance(lazy_right, Lazy)
    assert lazy_right.get() == 42

    left = Left('error')
    lazy_left = left.to_lazy()
    assert isinstance(lazy_left, Lazy)
    assert lazy_left.get() == 'error'

# Generated at 2026-10-24 02:07:33.170861
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:07:34.497826
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:07:36.156381
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:07:37.592283
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:07:39.063025
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:07:47.523239
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    right = Right(42)
    lazy_right = right.to_lazy()
    assert isinstance(lazy_right, Lazy)
    assert lazy_right.get() == 42

    left = Left('error')
    lazy_left = left.to_lazy()
    assert isinstance(lazy_left, Lazy)
    assert lazy_left.get() == 'error'

# Generated at 2026-10-24 02:07:48.957644
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:07:50.324207
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:07:51.723206
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:07:53.033135
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:07:54.335178
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:07:55.932686
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:07:57.244601
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:08:00.007318
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    right = Right(42)
    lazy_right = right.to_lazy()
    assert isinstance(lazy_right, Lazy)
    assert lazy_right.get() == 42

    left = Left('error')
    lazy_left = left.to_lazy()
    assert isinstance(lazy_left, Lazy)
    assert lazy_left.get() == 'error'

# Generated at 2026-10-24 02:08:01.330631
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:08:15.674625
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    right = Right(42)
    lazy_right = right.to_lazy()
    assert isinstance(lazy_right, Lazy)
    assert lazy_right.get() == 42

    left = Left('error')
    lazy_left = left.to_lazy()
    assert isinstance(lazy_left, Lazy)
    assert lazy_left.get() == 'error'

# Generated at 2026-10-24 02:08:16.988125
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:08:20.076151
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    right = Right(42)
    lazy_right = right.to_lazy()
    assert isinstance(lazy_right, Lazy)
    assert lazy_right.get() == 42

    left = Left('error')
    lazy_left = left.to_lazy()
    assert isinstance(lazy_left, Lazy)
    assert lazy_left.get() == 'error'

# Generated at 2026-10-24 02:08:21.382875
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:08:22.690261
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:08:23.992488
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:08:25.337835
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:08:26.730389
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:08:29.474317
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    right = Right(42)
    lazy_right = right.to_lazy()
    assert isinstance(lazy_right, Lazy)
    assert lazy_right.get() == 42

    left = Left('error')
    lazy_left = left.to_lazy()
    assert isinstance(lazy_left, Lazy)
    assert lazy_left.get() == 'error'

# Generated at 2026-10-24 02:08:30.772990
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:08:57.565836
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    right = Right(42)
    lazy_right = right.to_lazy()
    assert isinstance(lazy_right, Lazy)
    assert lazy_right.get() == 42

    left = Left('error')
    lazy_left = left.to_lazy()
    assert isinstance(lazy_left, Lazy)
    assert lazy_left.get() == 'error'

# Generated at 2026-10-24 02:09:00.310874
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    right = Right(42)
    lazy_right = right.to_lazy()
    assert isinstance(lazy_right, Lazy)
    assert lazy_right.get() == 42

    left = Left('error')
    lazy_left = left.to_lazy()
    assert isinstance(lazy_left, Lazy)
    assert lazy_left.get() == 'error'

# Generated at 2026-10-24 02:09:03.195689
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    right = Right(42)
    lazy_right = right.to_lazy()
    assert isinstance(lazy_right, Lazy)
    assert lazy_right.get() == 42

    left = Left('error')
    lazy_left = left.to_lazy()
    assert isinstance(lazy_left, Lazy)
    assert lazy_left.get() == 'error'

# Generated at 2026-10-24 02:09:05.965229
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    right = Right(42)
    lazy_right = right.to_lazy()
    assert isinstance(lazy_right, Lazy)
    assert lazy_right.get() == 42

    left = Left('error')
    lazy_left = left.to_lazy()
    assert isinstance(lazy_left, Lazy)
    assert lazy_left.get() == 'error'

# Generated at 2026-10-24 02:09:07.283130
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:09:10.055201
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    right = Right(42)
    lazy_right = right.to_lazy()
    assert isinstance(lazy_right, Lazy)
    assert lazy_right.get() == 42

    left = Left('error')
    lazy_left = left.to_lazy()
    assert isinstance(lazy_left, Lazy)
    assert lazy_left.get() == 'error'

# Generated at 2026-10-24 02:09:12.726411
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    right = Right(42)
    lazy_right = right.to_lazy()
    assert isinstance(lazy_right, Lazy)
    assert lazy_right.get() == 42

    left = Left('error')
    lazy_left = left.to_lazy()
    assert isinstance(lazy_left, Lazy)
    assert lazy_left.get() == 'error'

# Generated at 2026-10-24 02:09:14.359416
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:09:15.675389
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:09:16.990097
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:10:06.699354
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:10:08.119026
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:10:09.439185
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:10:12.202622
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    right = Right(42)
    lazy_right = right.to_lazy()
    assert isinstance(lazy_right, Lazy)
    assert lazy_right.get() == 42

    left = Left('error')
    lazy_left = left.to_lazy()
    assert isinstance(lazy_left, Lazy)
    assert lazy_left.get() == 'error'

# Generated at 2026-10-24 02:10:13.512439
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:10:15.186997
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:10:16.494471
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:10:17.796641
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:10:19.101591
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 02:10:20.408682
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)