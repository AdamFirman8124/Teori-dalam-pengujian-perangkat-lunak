

# Generated at 2026-11-01 23:58:22.731437
# Unit test for method handle_from_dict of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_handle_from_dict():

    @dataclasses.dataclass
    class ExampleDataClass:
        field_a: str
        field_b: int

    # Unknown parameters should be ignored (dropped from the result)
    kvs = {"field_a": "value_a", "field_b": 42, "field_c": "unknown_value"}
    result = _IgnoreUndefinedParameters.handle_from_dict(ExampleDataClass, kvs)
    assert result == {"field_a": "value_a", "field_b": 42}

    # All defined parameters should be kept
    kvs = {"field_a": "value_a", "field_b": 42}
    result = _IgnoreUndefinedParameters.handle_from_dict(ExampleDataClass, kvs)
    assert result == {"field_a": "value_a", "field_b": 42}

    # Empty input dict should yield an empty result
    result = _IgnoreUndefinedParameters.handle_from_dict(ExampleDataClass, {})
    assert result == {}

# Generated at 2026-11-01 23:58:38.378085
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    class _Dummy:
        pass

    obj = _Dummy()

    # handle_dump is a static method and should return an empty dict
    result = _UndefinedParameterAction.handle_dump(obj)
    assert result == {}
    assert isinstance(result, dict)

# Generated at 2026-11-01 23:58:54.555346
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-11-01 23:59:03.648835
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-11-01 23:59:09.596746
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    class Dummy:
        def __init__(self, value=0):
            self.value = value

    # create_init should return the original __init__ of the object
    returned_init = _UndefinedParameterAction.create_init(Dummy)
    assert returned_init == Dummy.__init__

    # The returned init should be callable and behave like the original
    instance = Dummy.__new__(Dummy)
    returned_init(instance, value=42)
    assert instance.value == 42

# Generated at 2026-11-01 23:59:17.908394
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    # handle_to_dict is a pass-through: it must return the kvs unchanged
    class _Dummy:
        pass

    obj = _Dummy()

    # Non-empty dict of key-values
    kvs = {"a": 1, "b": "two", "c": [3, 4]}
    result = _UndefinedParameterAction.handle_to_dict(obj, kvs)
    assert result == kvs
    assert result is kvs  # returns the same dict object, not a copy

    # Empty dict
    empty_kvs: Dict[Any, Any] = {}
    result_empty = _UndefinedParameterAction.handle_to_dict(obj, empty_kvs)
    assert result_empty == {}

    # Nested structures are preserved as-is
    nested_kvs = {"outer": {"inner": 1}, "list": [{"x": 2}]}
    result_nested = _UndefinedParameterAction.handle_to_dict(obj, nested_kvs)
    assert result_nested == nested_kvs

# Generated at 2026-11-01 23:59:30.089192
# Unit test for constructor of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters():
    # The class implements all abstract methods, so it can be instantiated
    instance = _RaiseUndefinedParameters()
    assert isinstance(instance, _UndefinedParameterAction)
    assert isinstance(instance, _RaiseUndefinedParameters)

    # Verify static method behavior via the class
    @dataclasses.dataclass
    class Person:
        name: str
        age: int

    # Only known parameters: they are returned unchanged
    known_only = _RaiseUndefinedParameters.handle_from_dict(
        Person, {"name": "Alice", "age": 30})
    assert known_only == {"name": "Alice", "age": 30}

    # Unknown parameters present: UndefinedParameterError is raised
    try:
        _RaiseUndefinedParameters.handle_from_dict(
            Person, {"name": "Bob", "age": 40, "undefined_param": "oops"})
        raised = False
    except UndefinedParameterError as e:
        raised = True
        assert "undefined_param" in str(e)
    assert raised

# Generated at 2026-11-01 23:59:59.181763
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    class _Dummy:
        pass

    obj = _Dummy()
    kvs = {"a": 1, "b": "two", "c": [1, 2, 3]}
    result = _UndefinedParameterAction.handle_to_dict(obj, kvs)
    assert result == kvs
    assert result is kvs

    # Also works with an empty dict
    empty_result = _UndefinedParameterAction.handle_to_dict(obj, {})
    assert empty_result == {}

# Generated at 2026-11-02 00:00:22.626470
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    @dataclasses.dataclass
    class Example:
        a: int
        b: str = "default"

    # A callable wrapping the original __init__ is returned
    new_init = _IgnoreUndefinedParameters.create_init(Example)
    assert callable(new_init)
    assert new_init.__name__ == "__init__"

    # Undefined keyword arguments are ignored, defaults are applied
    instance = object.__new__(Example)
    new_init(instance, a=1, undefined_kwarg="should be ignored")
    assert instance.a == 1
    assert instance.b == "default"

    # Positional arguments still work alongside undefined kwargs
    instance2 = object.__new__(Example)
    new_init(instance2, 42, b="custom", another_unknown=True)
    assert instance2.a == 42
    assert instance2.b == "custom"

    # Behaviour matches the normal init when nothing is undefined
    instance3 = object.__new__(Example)
    new_init(instance3, a=7, b="explicit")
    assert instance3.a == 7
    assert instance3.b == "explicit"

# Generated at 2026-11-02 00:00:47.864556
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    # handle_to_dict is a static method that simply returns the given kvs
    obj = object()
    kvs = {"name": "Alice", "age": 30}
    result = _UndefinedParameterAction.handle_to_dict(obj, kvs)
    assert result == kvs
    assert result is kvs

    # Test with an empty dict
    empty_kvs: Dict[Any, Any] = {}
    result_empty = _UndefinedParameterAction.handle_to_dict(obj, empty_kvs)
    assert result_empty == {}

# Generated at 2026-11-02 00:01:24.574998
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    @dataclasses.dataclass
    class Person:
        name: str
        age: int

    person = Person(name="Alice", age=30)
    result = _UndefinedParameterAction.handle_dump(person)
    assert result == {}
    assert isinstance(result, dict)

    # Should also return an empty dict for arbitrary objects
    assert _UndefinedParameterAction.handle_dump(None) == {}
    assert _UndefinedParameterAction.handle_dump(object()) == {}

# Generated at 2026-11-02 00:01:47.615456
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    @dataclasses.dataclass
    class Example:
        name: str
        age: int

    # All parameters are known -> returns known parameters unchanged
    kvs = {"name": "Alice", "age": 30}
    result = _RaiseUndefinedParameters.handle_from_dict(Example, kvs)
    assert result == {"name": "Alice", "age": 30}

    # Empty input -> returns empty dict
    assert _RaiseUndefinedParameters.handle_from_dict(Example, {}) == {}

    # Unknown parameters -> raises UndefinedParameterError
    kvs_with_unknown = {"name": "Bob", "age": 25, "extra": "value"}
    try:
        _RaiseUndefinedParameters.handle_from_dict(Example, kvs_with_unknown)
        assert False, "Expected UndefinedParameterError to be raised"
    except UndefinedParameterError as e:
        assert "extra" in str(e)
        assert "undefined initialization arguments" in str(e)

# Generated at 2026-11-02 00:02:24.580455
# Unit test for method handle_from_dict of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_handle_from_dict():
    # Arrange
    @dataclasses.dataclass
    class TestClass:
        a: int
        b: str

    # Act: known and unknown parameters mixed
    result = _IgnoreUndefinedParameters.handle_from_dict(
        cls=TestClass, kvs={"a": 1, "b": "hello", "c": 42, "d": None})

    # Assert: only defined parameters are kept, undefined are ignored
    assert result == {"a": 1, "b": "hello"}

    # Act: only unknown parameters
    result = _IgnoreUndefinedParameters.handle_from_dict(
        cls=TestClass, kvs={"x": 1, "y": 2})

    # Assert: everything is dropped
    assert result == {}

    # Act: empty input
    result = _IgnoreUndefinedParameters.handle_from_dict(cls=TestClass, kvs={})

    # Assert: empty result
    assert result == {}

    # Act: only known parameters
    result = _IgnoreUndefinedParameters.handle_from_dict(
        cls=TestClass, kvs={"a": 5, "b": "world"})

    # Assert: all known parameters are preserved
    assert result == {"a": 5, "b": "world"}

# Generated at 2026-11-02 00:03:39.615449
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    @dataclass
    class Person:
        name: str
        age: int = 42
        city: str = "Unknown"

    original_init = Person.__init__
    new_init = _IgnoreUndefinedParameters.create_init(Person)

    # Returns a callable that wraps the original __init__
    assert callable(new_init)
    assert new_init.__name__ == "__init__"
    assert new_init.__wrapped__ is original_init

    # Install the new init
    Person.__init__ = new_init

    # Defined parameters are passed through to the original init
    person = Person(name="Alice", age=30, city="Berlin")
    assert person.name == "Alice"
    assert person.age == 30
    assert person.city == "Berlin"

    # Undefined keyword parameters are silently ignored
    person = Person(name="Bob", age=25, undefined_param="oops", another=1)
    assert person.name == "Bob"
    assert person.age == 25
    assert not hasattr(person, "undefined_param")
    assert not hasattr(person, "another")

    # Defaults are applied for parameters that were not provided
    person = Person(name="Charlie")
    assert person.age == 42
    assert person.city == "Unknown"

    # Positional arguments are supported and surplus ones are dropped
    person = Person("Dave", 30, "Berlin", "surplus")
    assert person.name == "Dave"
    assert person.age == 30
    assert person.city == "Berlin"

# Generated at 2026-11-02 00:04:12.654253
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    @dataclasses.dataclass
    class Person:
        name: str
        age: int
        city: str = "Unknown"

    # Replace the class __init__ with the wrapped init produced by create_init
    Person.__init__ = _IgnoreUndefinedParameters.create_init(Person)

    # Known parameters initialize the instance normally
    person = Person(name="Alice", age=30, city="Berlin")
    assert person.name == "Alice"
    assert person.age == 30
    assert person.city == "Berlin"

    # Undefined keyword parameters are silently ignored
    person_with_unknown = Person(name="Bob", age=25, undefined_param="ignored")
    assert person_with_unknown.name == "Bob"
    assert person_with_unknown.age == 25
    assert person_with_unknown.city == "Unknown"

    # Positional arguments still work
    person_positional = Person("Charlie", 40)
    assert person_positional.name == "Charlie"
    assert person_positional.age == 40
    assert person_positional.city == "Unknown"

    # Excess positional arguments are dropped
    person_extra = Person("Dave", 50, "ExtraCity", "dropped")
    assert person_extra.name == "Dave"
    assert person_extra.age == 50
    assert person_extra.city == "ExtraCity"

    # Mixing positional and keyword arguments with unknown kwargs
    person_mixed = Person("Eve", age=35, unknown="x")
    assert person_mixed.name == "Eve"
    assert person_mixed.age == 35
    assert person_mixed.city == "Unknown"

# Generated at 2026-11-02 00:04:40.772252
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    class DummyClass:
        def __init__(self, x, y=0):
            self.x = x
            self.y = y

    # create_init should simply return the original __init__ of the class
    result = _UndefinedParameterAction.create_init(DummyClass)
    assert result == DummyClass.__init__

    # The returned callable should behave exactly like the original __init__
    instance = DummyClass.__new__(DummyClass)
    result(instance, 42, y=7)
    assert instance.x == 42
    assert instance.y == 7

    # Default values should still apply when called through create_init
    instance2 = DummyClass.__new__(DummyClass)
    result(instance2, 1)
    assert instance2.x == 1
    assert instance2.y == 0

# Generated at 2026-11-02 00:05:32.181824
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    message = "Received undefined initialization arguments {'foo': 1}"

    # Constructor accepts a message and stores it
    error = UndefinedParameterError(message)
    assert isinstance(error, UndefinedParameterError)
    assert isinstance(error, ValidationError)
    assert error.args[0] == message
    assert str(error) == message

    # Constructor with no arguments
    error_no_args = UndefinedParameterError()
    assert isinstance(error_no_args, UndefinedParameterError)
    assert isinstance(error_no_args, ValidationError)

    # Error can be raised and caught as UndefinedParameterError
    try:
        raise UndefinedParameterError(message)
    except UndefinedParameterError as caught:
        assert str(caught) == message

    # Error can also be caught as ValidationError (parent class)
    try:
        raise UndefinedParameterError(message)
    except ValidationError as caught:
        assert str(caught) == message

# Generated at 2026-11-02 00:07:38.285091
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters