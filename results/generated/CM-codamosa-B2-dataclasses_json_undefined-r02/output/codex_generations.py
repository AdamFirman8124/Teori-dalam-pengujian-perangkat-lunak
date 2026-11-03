

# Generated at 2026-11-01 22:01:49.339554
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    @dataclasses.dataclass
    class Sample:
        a: int
        b: str = "default_b"

    # The base-class implementation is an abstract stub: calling it directly
    # performs no processing and returns None.
    assert _UndefinedParameterAction.handle_from_dict(Sample, {"a": 1}) is None

    # RAISE strategy: known parameters are passed through unchanged...
    assert _RaiseUndefinedParameters.handle_from_dict(
        Sample, {"a": 1, "b": "value"}) == {"a": 1, "b": "value"}

    # ...and any undefined parameter triggers UndefinedParameterError.
    try:
        _RaiseUndefinedParameters.handle_from_dict(Sample, {"a": 1, "c": 3})
        raised = False
    except UndefinedParameterError:
        raised = True
    assert raised, "Expected UndefinedParameterError for unknown parameter 'c'"

    # EXCLUDE strategy: undefined parameters are silently dropped.
    assert _IgnoreUndefinedParameters.handle_from_dict(
        Sample, {"a": 1, "c": 3, "d": 4}) == {"a": 1}

    # INCLUDE strategy requires a catch-all field to collect unknowns.
    @dataclasses.dataclass
    class WithCatchAll:
        a: int
        rest: CatchAll = None

    # Unknown parameters end up inside the catch-all field.
    assert _CatchAllUndefinedParameters.handle_from_dict(
        WithCatchAll, {"a": 1, "c": 3}) == {"a": 1, "rest": {"c": 3}}

    # No undefined parameters yields an empty catch-all dictionary.
    assert _CatchAllUndefinedParameters.handle_from_dict(
        WithCatchAll, {"a": 1}) == {"a": 1, "rest": {}}

    # Multiple unknown parameters are all collected.
    assert _CatchAllUndefinedParameters.handle_from_dict(
        WithCatchAll, {"a": 1, "x": 10, "y": 20}) == {
        "a": 1, "rest": {"x": 10, "y": 20}}

    # Explicitly supplying the catch-all field with its default value while
    # unknown parameters are present fills it with the unknown parameters.
    assert _CatchAllUndefinedParameters.handle_from_dict(
        WithCatchAll, {"a": 1, "rest": None, "z": 5}) == {
        "a": 1, "rest": {"z": 5}}

# Generated at 2026-11-01 22:02:42.382637
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    # Test that UndefinedParameterError can be constructed with a message
    message = "Received undefined initialization arguments {'foo': 1}"
    error = UndefinedParameterError(message)

    # Verify the error is an instance of UndefinedParameterError
    assert isinstance(error, UndefinedParameterError)

    # Verify it is also a ValidationError (inherits from marshmallow)
    assert isinstance(error, ValidationError)

    # Verify the message is stored correctly
    assert str(error) == message

    # Verify it can be raised and caught
    try:
        raise UndefinedParameterError("test error")
    except UndefinedParameterError as e:
        assert str(e) == "test error"
    except ValidationError:
        assert False, "Should have been caught as UndefinedParameterError"

    # Verify it can be caught as a ValidationError
    try:
        raise UndefinedParameterError("another test")
    except ValidationError as e:
        assert str(e) == "another test"

    # Verify construction with no arguments
    error_no_args = UndefinedParameterError()
    assert isinstance(error_no_args, UndefinedParameterError)

# Generated at 2026-11-01 22:03:02.103517
# Unit test for constructor of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters():
    instance = _RaiseUndefinedParameters()
    assert instance is not None
    assert isinstance(instance, _RaiseUndefinedParameters)
    assert isinstance(instance, _UndefinedParameterAction)
    # Static methods should be accessible on the instance
    assert callable(instance.handle_from_dict)
    assert callable(instance.handle_to_dict)
    assert callable(instance.handle_dump)
    assert callable(instance.create_init)

# Generated at 2026-11-01 22:03:29.220119
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    # Test 1: no unknown parameters, catch-all field not provided
    @dataclasses.dataclass
    class ObjectWithCatchAll1:
        a: int
        catch_all: CatchAll = None

    kvs = {'a': 1}
    result = _CatchAllUndefinedParameters.handle_from_dict(ObjectWithCatchAll1, kvs)
    assert result == {'a': 1, 'catch_all': {}}

    # Test 2: catch-all field received with its default value, no unknown parameters
    kvs = {'a': 1, 'catch_all': None}
    result = _CatchAllUndefinedParameters.handle_from_dict(ObjectWithCatchAll1, kvs)
    assert result == {'a': 1, 'catch_all': None}

    # Test 3: catch-all field received with its default value, unknown parameters present
    kvs = {'a': 1, 'catch_all': None, 'b': 'unknown'}
    result = _CatchAllUndefinedParameters.handle_from_dict(ObjectWithCatchAll1, kvs)
    assert result == {'a': 1, 'catch_all': {'b': 'unknown'}}

    # Test 4: catch-all field already parsed as dict, unknown parameters are merged
    kvs = {'a': 1, 'catch_all': {'x': 1}, 'b': 'unknown'}
    result = _CatchAllUndefinedParameters.handle_from_dict(ObjectWithCatchAll1, kvs)
    assert result == {'a': 1, 'catch_all': {'x': 1, 'b': 'unknown'}}

    # Test 5: catch-all field already parsed as dict, no unknown parameters
    kvs = {'a': 1, 'catch_all': {'x': 1}}
    result = _CatchAllUndefinedParameters.handle_from_dict(ObjectWithCatchAll1, kvs)
    assert result == {'a': 1, 'catch_all': {'x': 1}}

    # Test 6: input field with same name as catch-all but not a dict raises error
    kvs = {'a': 1, 'catch_all': 'not-a-dict'}
    with pytest.raises(UndefinedParameterError):
        _CatchAllUndefinedParameters.handle_from_dict(ObjectWithCatchAll1, kvs)

    # Test 7: catch-all field with default_factory
    @dataclasses.dataclass
    class ObjectWithCatchAllFactory:
        a: int
        catch_all: CatchAll = dataclasses.field(default_factory=dict)

    kvs = {'a': 1, 'catch_all': {}}
    result = _CatchAllUndefinedParameters.handle_from_dict(ObjectWithCatchAllFactory, kvs)
    assert result == {'a': 1, 'catch_all': {}}

    kvs = {'a': 1, 'catch_all': {}, 'b': 'unknown'}
    result = _CatchAllUndefinedParameters.handle_from_dict(ObjectWithCatchAllFactory, kvs)
    assert result == {'a': 1, 'catch_all': {'b': 'unknown'}}

    # Test 8: class without a catch-all field raises error
    @dataclasses.dataclass
    class ObjectWithoutCatchAll:
        a: int

    with pytest.raises(UndefinedParameterError):
        _CatchAllUndefinedParameters.handle_from_dict(ObjectWithoutCatchAll, {'a': 1, 'b': 2})

# Generated at 2026-11-01 22:03:48.530468
# Unit test for constructor of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters():
    @dataclasses.dataclass
    class DataClass:
        id: int
        name: str = "default"

    # handle_from_dict keeps only known parameters, silently dropping unknown ones
    result = _IgnoreUndefinedParameters.handle_from_dict(
        DataClass, {"id": 1, "name": "Alice", "unexpected_key": "value"})
    assert result == {"id": 1, "name": "Alice"}

    # Input consisting solely of unknown parameters yields an empty mapping
    result = _IgnoreUndefinedParameters.handle_from_dict(DataClass, {"foo": 1})
    assert result == {}

    # Wrapped __init__ accepts and discards unknown keyword arguments
    wrapped_init = _IgnoreUndefinedParameters.create_init(DataClass)
    instance = object.__new__(DataClass)
    wrapped_init(instance, id=5, name="Bob", unknown_kwarg=123)
    assert instance.id == 5
    assert instance.name == "Bob"

    # Extra positional arguments are truncated to the number of takeable fields
    instance2 = object.__new__(DataClass)
    wrapped_init(instance2, 7, "Carol", "surplus_positional")
    assert instance2.id == 7
    assert instance2.name == "Carol"

    # Defaults are applied for parameters that were not provided
    instance3 = object.__new__(DataClass)
    wrapped_init(instance3, 8)
    assert instance3.id == 8
    assert instance3.name == "default"

    # handle_to_dict passes the kvs through unchanged
    kvs = {"id": 1, "name": "Alice"}
    assert _IgnoreUndefinedParameters.handle_to_dict(None, kvs) == kvs

    # handle_dump contributes no additional parameters
    assert _IgnoreUndefinedParameters.handle_dump(None) == {}

# Generated at 2026-11-01 22:04:00.312179
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    # Constructor accepts a message string and preserves it
    message = "Received undefined initialization arguments {'unknown_param': 42}"
    error = UndefinedParameterError(message)

    # It is an instance of both the custom error and marshmallow's ValidationError
    assert isinstance(error, UndefinedParameterError)
    assert isinstance(error, ValidationError)

    # The message should be stored and retrievable
    assert error.messages == message
    assert message in str(error)

    # Constructor also accepts a list of messages
    list_error = UndefinedParameterError(["first error", "second error"])
    assert isinstance(list_error, UndefinedParameterError)
    assert isinstance(list_error, ValidationError)
    assert list_error.messages == ["first error", "second error"]

    # It can be raised and caught as UndefinedParameterError
    try:
        raise UndefinedParameterError("test raise message")
    except UndefinedParameterError as caught:
        assert "test raise message" in str(caught)
    except ValidationError:
        # Should never reach here: UndefinedParameterError is caught first
        assert False, "UndefinedParameterError was not caught as its own type"

# Generated at 2026-11-01 22:05:12.506163
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-11-01 22:05:51.158293
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    # nonce:da65f232
    @dataclasses.dataclass
    class _Record:
        id: int
        name: str
        extras: CatchAll = None

    custom_init = _CatchAllUndefinedParameters.create_init(_Record)

    record = object.__new__(_Record)
    custom_init(record, 1, "widget", color="red", size="XL")

    assert record.id == 1
    assert record.name == "widget"
    assert record.extras == {"color": "red", "size": "XL"}

    # With no undefined parameters the catch-all field ends up as an empty dict
    plain = object.__new__(_Record)
    custom_init(plain, id=2, name="gadget")

    assert plain.id == 2
    assert plain.name == "gadget"
    assert plain.extras == {}

# Generated at 2026-11-01 22:06:24.693964
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    @dataclasses.dataclass
    class TestClass:
        known_field: int
        extras: CatchAll = None

    # Case 1: catch-all value is a dict -> popped and merged into kvs
    obj = TestClass(known_field=1, extras={"undefined_a": 1, "undefined_b": "x"})
    kvs = {"known_field": 1, "extras": {"undefined_a": 1, "undefined_b": "x"}}
    result = _CatchAllUndefinedParameters.handle_to_dict(obj, kvs)
    assert result == {"known_field": 1, "undefined_a": 1, "undefined_b": "x"}
    assert "extras" not in result

    # Case 2: catch-all value is not a dict -> only popped, not merged
    obj = TestClass(known_field=2, extras=None)
    kvs = {"known_field": 2, "extras": None}
    result = _CatchAllUndefinedParameters.handle_to_dict(obj, kvs)
    assert result == {"known_field": 2}

    # Case 3: empty dict catch-all -> nothing extra merged
    obj = TestClass(known_field=3, extras={})
    kvs = {"known_field": 3, "extras": {}}
    result = _CatchAllUndefinedParameters.handle_to_dict(obj, kvs)
    assert result == {"known_field": 3}

# Generated at 2026-11-01 22:06:44.761628
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    # handle_dump is the base implementation that always returns an empty
    # dict, regardless of the object passed in.

    class _Dummy:
        pass

    obj = _Dummy()

    result = _UndefinedParameterAction.handle_dump(obj)

    assert result == {}
    assert isinstance(result, dict)

# Generated at 2026-11-01 22:07:03.154552
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-11-01 22:07:06.536616
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-11-01 22:08:02.898737
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    import pytest
    from dataclasses import dataclass, field

    @dataclass
    class Example:
        first_name: str
        last_name: str
        catch_all: CatchAll = field(default_factory=dict)

    # Unknown parameters are collected into the catch-all field
    result = _CatchAllUndefinedParameters.handle_from_dict(
        Example, {"first_name": "John", "last_name": "Doe",
                  "age": 30, "city": "Berlin"})
    assert result == {"first_name": "John", "last_name": "Doe",
                      "catch_all": {"age": 30, "city": "Berlin"}}

    # No unknown parameters -> catch-all becomes the (empty) default
    result = _CatchAllUndefinedParameters.handle_from_dict(
        Example, {"first_name": "John", "last_name": "Doe"})
    assert result == {"first_name": "John", "last_name": "Doe",
                      "catch_all": {}}

    # Explicitly provided (already parsed) catch-all dict is preserved
    result = _CatchAllUndefinedParameters.handle_from_dict(
        Example, {"first_name": "John", "last_name": "Doe",
                  "catch_all": {"a": 1}})
    assert result == {"first_name": "John", "last_name": "Doe",
                      "catch_all": {"a": 1}}

    # Already parsed catch-all dict is merged with new unknown parameters
    result = _CatchAllUndefinedParameters.handle_from_dict(
        Example, {"first_name": "John", "last_name": "Doe",
                  "catch_all": {"a": 1}, "b": 2})
    assert result == {"first_name": "John", "last_name": "Doe",
                      "catch_all": {"a": 1, "b": 2}}

    # A non-dict value for the catch-all field raises an error
    with pytest.raises(UndefinedParameterError):
        _CatchAllUndefinedParameters.handle_from_dict(
            Example, {"first_name": "John", "last_name": "Doe",
                      "catch_all": "invalid"})

# Generated at 2026-11-01 22:08:14.772436
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    """
    Test the base implementation of _UndefinedParameterAction.handle_dump,
    which should always return an empty dict regardless of the object passed.
    """
    class DummyClass:
        def __init__(self):
            self.attr = "value"

    # With a regular object instance
    dummy_instance = DummyClass()
    result = _UndefinedParameterAction.handle_dump(dummy_instance)
    assert result == {}
    assert isinstance(result, dict)

    # With None as the argument
    assert _UndefinedParameterAction.handle_dump(None) == {}

    # With a plain string argument
    assert _UndefinedParameterAction.handle_dump("some_string") == {}

# Generated at 2026-11-01 22:08:36.073051
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    @dataclasses.dataclass
    class Person:
        first_name: str
        last_name: str
        misc: CatchAll = None

    # Case 1: catch-all field contains a dict -> entries merged into kvs
    person = Person(first_name="John", last_name="Doe",
                    misc={"age": 42, "city": "Berlin"})
    kvs = {"first_name": "John", "last_name": "Doe",
           "misc": {"age": 42, "city": "Berlin"}}
    expected = {"first_name": "John", "last_name": "Doe",
                "age": 42, "city": "Berlin"}
    result = _CatchAllUndefinedParameters.handle_to_dict(person, kvs)
    assert result == expected
    assert "misc" not in result

    # Case 2: catch-all field is None (not a dict) -> key simply removed
    person = Person(first_name="Jane", last_name="Roe", misc=None)
    kvs = {"first_name": "Jane", "last_name": "Roe", "misc": None}
    expected = {"first_name": "Jane", "last_name": "Roe"}
    result = _CatchAllUndefinedParameters.handle_to_dict(person, kvs)
    assert result == expected

    # Case 3: catch-all field is an empty dict -> nothing merged
    person = Person(first_name="A", last_name="B", misc={})
    kvs = {"first_name": "A", "last_name": "B", "misc": {}}
    expected = {"first_name": "A", "last_name": "B"}
    result = _CatchAllUndefinedParameters.handle_to_dict(person, kvs)
    assert result == expected

# Generated at 2026-11-01 22:08:43.137843
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    # nonce:18fa0a00
    class Dummy:
        def __init__(self, a=0, b=None):
            self.a = a
            self.b = b

    # create_init should simply return the original __init__ of the object
    result = _UndefinedParameterAction.create_init(Dummy)
    assert result == Dummy.__init__

    # The returned callable should behave like the original __init__
    instance = Dummy.__new__(Dummy)
    result(instance, a=5, b="x")
    assert instance.a == 5
    assert instance.b == "x"

    # Works with default arguments too
    instance2 = Dummy.__new__(Dummy)
    result(instance2)
    assert instance2.a == 0
    assert instance2.b is None

# Generated at 2026-11-01 22:08:47.542495
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    class DummyObj:
        pass

    obj = DummyObj()

    # Non-empty mapping should be returned unchanged
    kvs = {"a": 1, "b": "value", "c": [1, 2, 3]}
    result = _UndefinedParameterAction.handle_to_dict(obj, kvs)
    assert result == {"a": 1, "b": "value", "c": [1, 2, 3]}
    assert result is kvs  # identity: base implementation returns same dict

    # Empty mapping should also be returned unchanged
    empty_kvs = {}
    result_empty = _UndefinedParameterAction.handle_to_dict(obj, empty_kvs)
    assert result_empty == {}

# Generated at 2026-11-01 22:09:25.027762
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-11-01 22:09:41.926276
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-11-01 22:10:00.143482
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-11-01 22:10:07.311167
# Unit test for method handle_from_dict of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_handle_from_dict():
    @dataclasses.dataclass
    class _ExampleClass:
        known_field: str
        another_known_field: int = 0

    # Case: mix of known and unknown parameters -> unknown are dropped
    kvs = {
        "known_field": "value",
        "another_known_field": 42,
        "undefined_param": "should be ignored",
        "another_undefined": 123,
    }
    result = _IgnoreUndefinedParameters.handle_from_dict(
        cls=_ExampleClass, kvs=kvs)
    assert result == {"known_field": "value", "another_known_field": 42}

    # Case: only known parameters -> returned unchanged
    kvs = {"known_field": "value", "another_known_field": 7}
    result = _IgnoreUndefinedParameters.handle_from_dict(
        cls=_ExampleClass, kvs=kvs)
    assert result == {"known_field": "value", "another_known_field": 7}

    # Case: only unknown parameters -> empty dict returned
    kvs = {"undefined_param": "ignored", "another_undefined": 1}
    result = _IgnoreUndefinedParameters.handle_from_dict(
        cls=_ExampleClass, kvs=kvs)
    assert result == {}

    # Case: empty input -> empty dict returned
    result = _IgnoreUndefinedParameters.handle_from_dict(
        cls=_ExampleClass, kvs={})
    assert result == {}

# Generated at 2026-11-01 22:10:20.736958
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    @dataclasses.dataclass
    class Employee:
        name: str
        age: int = 42
        city: str = "Berlin"

    original_init = Employee.__init__

    # Patch the class initializer with the wrapped one
    Employee.__init__ = _IgnoreUndefinedParameters.create_init(Employee)

    # The wrapper keeps a reference to the original init via functools.wraps
    assert Employee.__init__.__wrapped__ is original_init

    # 1. All defined parameters are passed through unchanged
    emp = Employee(name="Alice", age=30, city="Paris")
    assert emp.name == "Alice"
    assert emp.age == 30
    assert emp.city == "Paris"

    # 2. Missing parameters fall back to their declared defaults
    emp_default = Employee(name="Bob")
    assert emp_default.name == "Bob"
    assert emp_default.age == 42
    assert emp_default.city == "Berlin"

    # 3. Undefined keyword parameters are silently ignored (no error raised)
    emp_unknown = Employee(name="Carol", salary=5000, department="IT")
    assert emp_unknown.name == "Carol"
    assert emp_unknown.age == 42
    assert emp_unknown.city == "Berlin"

    # 4. Mixing positional and keyword arguments works
    emp_mixed = Employee("Dave", 50, city="London")
    assert emp_mixed.name == "Dave"
    assert emp_mixed.age == 50
    assert emp_mixed.city == "London"

    # 5. Excess positional arguments are truncated away
    emp_extra = Employee("Eve", 33, "Oslo", "extra1", "extra2")
    assert emp_extra.name == "Eve"
    assert emp_extra.age == 33
    assert emp_extra.city == "Oslo"

    # 6. A missing required argument still results in a TypeError
    raised = False
    try:
        Employee()
    except TypeError:
        raised = True
    assert raised

# Generated at 2026-11-01 22:10:36.126461
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    """Unit test for method handle_from_dict of class _UndefinedParameterAction"""

    # Concrete implementation of the abstract handler used for testing
    class _ConcreteHandler(_UndefinedParameterAction):
        @staticmethod
        def module_0.handle_from_dict(cls, kvs):
            known, _ = _UndefinedParameterAction._separate_defined_undefined_kvs(
                cls=cls, kvs=kvs)
            return known

    @dataclasses.dataclass
    class Example:
        name: str
        age: int

    # Known parameters are kept, unknown ones are filtered out
    kvs = {"name": "Alice", "age": 30, "extra": "ignored"}
    result = _ConcreteHandler.handle_from_dict(Example, kvs)
    assert result == {"name": "Alice", "age": 30}

    # Only unknown parameters results in an empty dict
    result = _ConcreteHandler.handle_from_dict(Example, {"unknown": 42})
    assert result == {}

    # Empty input yields an empty dict
    result = _ConcreteHandler.handle_from_dict(Example, {})
    assert result == {}

    # The abstract base implementation itself performs no processing
    assert _UndefinedParameterAction.handle_from_dict(Example, kvs) is None

    # The RAISE strategy rejects unknown parameters
    with pytest.raises(UndefinedParameterError):
        _RaiseUndefinedParameters.handle_from_dict(Example, kvs)

    # The RAISE strategy accepts known parameters only
    result = _RaiseUndefinedParameters.handle_from_dict(
        Example, {"name": "Bob", "age": 25})
    assert result == {"name": "Bob", "age": 25}

    # The EXCLUDE strategy silently drops unknown parameters
    result = _IgnoreUndefinedParameters.handle_from_dict(Example, kvs)
    assert result == {"name": "Alice", "age": 30}

# Generated at 2026-11-01 22:10:40.694970
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    # Test basic construction with a message
    message = "Received undefined initialization arguments {'foo': 1}"
    error = UndefinedParameterError(message)
    assert error is not None
    assert str(error) == message
    assert error.args == (message,)

    # It should be a subclass of ValidationError and Exception
    assert isinstance(error, UndefinedParameterError)
    assert isinstance(error, ValidationError)
    assert isinstance(error, Exception)

    # It should be raisable and catchable as UndefinedParameterError
    try:
        raise UndefinedParameterError("some error")
    except UndefinedParameterError as caught:
        assert str(caught) == "some error"

    # It should also be catchable as a ValidationError
    try:
        raise UndefinedParameterError("validation failure")
    except ValidationError as caught:
        assert isinstance(caught, UndefinedParameterError)
        assert str(caught) == "validation failure"

    # Construction with no arguments should also work
    empty_error = UndefinedParameterError()
    assert isinstance(empty_error, UndefinedParameterError)
    assert str(empty_error) == ""

    # Construction with multiple args is preserved like a normal Exception
    multi_error = UndefinedParameterError("msg", {"key": "value"})
    assert multi_error.args == ("msg", {"key": "value"})

# Generated at 2026-11-01 22:10:58.718163
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    import pytest

    @dataclasses.dataclass
    class ObjectWithCatchAll:
        id: str
        undefined_parameters: CatchAll = None

    # undefined parameters stored in the catch-all field are merged
    # into the output dict and the catch-all key is removed
    obj = ObjectWithCatchAll(id='123',
                             undefined_parameters={'unknown': 'unknown'})
    kvs = {'id': '123',
           'undefined_parameters': {'unknown': 'unknown'}}
    result = _CatchAllUndefinedParameters.handle_to_dict(obj, kvs)
    assert result == {'id': '123', 'unknown': 'unknown'}

    # a non-dict catch-all value is simply removed from the dict
    obj = ObjectWithCatchAll(id='123', undefined_parameters=None)
    kvs = {'id': '123', 'undefined_parameters': None}
    result = _CatchAllUndefinedParameters.handle_to_dict(obj, kvs)
    assert result == {'id': '123'}

    # a class without a catch-all field raises UndefinedParameterError
    @dataclasses.dataclass
    class ObjectWithoutCatchAll:
        id: str

    with pytest.raises(UndefinedParameterError):
        _CatchAllUndefinedParameters.handle_to_dict(
            ObjectWithoutCatchAll(id='123'), {'id': '123'})