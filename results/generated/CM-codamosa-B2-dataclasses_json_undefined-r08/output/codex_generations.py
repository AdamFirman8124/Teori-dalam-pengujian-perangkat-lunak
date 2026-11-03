

# Generated at 2026-11-01 20:14:17.463625
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    """
    Test that the base implementation of handle_dump returns an empty dict
    regardless of the object passed in.
    """

    class DummyClass:
        def __init__(self):
            self.some_attr = "value"

    dummy_instance = DummyClass()

    result = _UndefinedParameterAction.handle_dump(dummy_instance)

    assert result == {}
    assert isinstance(result, dict)

# Generated at 2026-11-01 20:14:55.455397
# Unit test for constructor of class _UndefinedParameterAction
def test__UndefinedParameterAction():
    # _UndefinedParameterAction is abstract (has abstractmethod handle_from_dict),
    # so it must not be possible to instantiate it directly.
    try:
        _UndefinedParameterAction()
        instantiated = True
    except TypeError:
        instantiated = False
    assert not instantiated, \
        "_UndefinedParameterAction should be abstract and not instantiable"

    # Prepare a concrete dataclass to exercise the static helper methods
    @dataclasses.dataclass
    class Example:
        a: int
        b: str = "default"

    instance = Example(a=1)

    # _separate_defined_undefined_kvs splits known vs unknown parameters
    known, unknown = _UndefinedParameterAction._separate_defined_undefined_kvs(
        Example, {"a": 1, "b": "hello", "c": 42})
    assert known == {"a": 1, "b": "hello"}
    assert unknown == {"c": 42}

    # All-known kvs yield empty unknown dict
    known, unknown = _UndefinedParameterAction._separate_defined_undefined_kvs(
        Example, {"a": 5})
    assert known == {"a": 5}
    assert unknown == {}

    # handle_to_dict passes kvs through unchanged
    kvs = {"a": 1, "extra": 2}
    assert _UndefinedParameterAction.handle_to_dict(instance, kvs) == \
        {"a": 1, "extra": 2}

    # handle_dump contributes no extra parameters by default
    assert _UndefinedParameterAction.handle_dump(instance) == {}

    # create_init returns the original __init__ untouched
    assert _UndefinedParameterAction.create_init(Example) == Example.__init__

# Generated at 2026-11-01 20:15:41.638988
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():

    @dataclasses.dataclass
    class Dummy:
        a: int
        b: str = "default"

    # The abstract base implementation simply passes, so it returns None
    # regardless of the input mapping.
    result = _UndefinedParameterAction.handle_from_dict(Dummy, {"a": 1, "b": "x"})
    assert result is None

    result_empty = _UndefinedParameterAction.handle_from_dict(Dummy, {})
    assert result_empty is None

# Generated at 2026-11-01 20:16:05.831314
# Unit test for method handle_from_dict of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_handle_from_dict():
    @dataclasses.dataclass
    class Example:
        name: str
        age: int

    # Known and unknown parameters together: unknown should be dropped
    kvs = {"name": "Alice", "age": 30, "unknown_param": "value",
           "another_unknown": 123}
    result = _IgnoreUndefinedParameters.handle_from_dict(cls=Example, kvs=kvs)
    assert result == {"name": "Alice", "age": 30}

    # Only known parameters
    kvs = {"name": "Bob", "age": 25}
    result = _IgnoreUndefinedParameters.handle_from_dict(cls=Example, kvs=kvs)
    assert result == {"name": "Bob", "age": 25}

    # Empty input
    result = _IgnoreUndefinedParameters.handle_from_dict(cls=Example, kvs={})
    assert result == {}

# Generated at 2026-11-01 20:16:43.486986
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-11-01 20:17:17.179330
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-11-01 20:18:00.084661
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-11-01 20:18:50.975978
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    class Dummy:
        pass

    dummy = Dummy()
    result = _UndefinedParameterAction.handle_dump(dummy)
    assert result == {}
    assert isinstance(result, dict)

# Generated at 2026-11-01 20:19:39.023958
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    @dataclasses.dataclass
    class Sample:
        x: int = 1
        y: str = "hello"

    obj = Sample(x=5, y="world")
    result = _UndefinedParameterAction.handle_dump(obj)
    assert result == {}
    assert isinstance(result, dict)

# Generated at 2026-11-01 20:21:49.880894
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    @dataclasses.dataclass
    class Example:
        name: str
        value: int
        extras: Optional[CatchAllVar] = dataclasses.field(default_factory=dict)

    # create_init must return a callable wrapper around the original __init__
    new_init = _CatchAllUndefinedParameters.create_init(Example)
    assert callable(new_init)

    # Unknown keyword arguments are collected into the catch-all field
    instance = object.__new__(Example)
    new_init(instance, name="alice", value=1, unknown_key="x", another=2)
    assert instance.name == "alice"
    assert instance.value == 1
    assert instance.extras == {"unknown_key": "x", "another": 2}

    # No undefined parameters yields an empty catch-all dict
    instance2 = object.__new__(Example)
    new_init(instance2, name="bob", value=2)
    assert instance2.name == "bob"
    assert instance2.value == 2
    assert instance2.extras == {}

    # Excess positional arguments are routed into the catch-all field
    instance3 = object.__new__(Example)
    new_init(instance3, "carol", 3, 99, "extra")
    assert instance3.name == "carol"
    assert instance3.value == 3
    assert instance3.extras == {"_UNKNOWN0": 99, "_UNKNOWN1": "extra"}

    # Mix of normal positional args and unknown keyword args
    instance4 = object.__new__(Example)
    new_init(instance4, "dave", 4, key="val")
    assert instance4.name == "dave"
    assert instance4.value == 4
    assert instance4.extras == {"key": "val"}

    # functools.wraps preserves the wrapped __init__ metadata
    assert new_init.__name__ == "__init__"

    # Installing the wrapper on the class behaves like the decorated pipeline
    original_init = Example.__init__
    Example.__init__ = new_init
    try:
        eve = Example("eve", 5, zip_code="12345")
        assert eve.name == "eve"
        assert eve.value == 5
        assert eve.extras == {"zip_code": "12345"}
    finally:
        Example.__init__ = original_init

    # A class without a catch-all field raises UndefinedParameterError
    # when the created initializer receives unknown parameters
    @dataclasses.dataclass
    class NoCatchAll:
        a: int

    plain_init = _CatchAllUndefinedParameters.create_init(NoCatchAll)
    bad = object.__new__(NoCatchAll)
    raised = False
    try:
        plain_init(bad, a=1, b=2)
    except UndefinedParameterError:
        raised = True
    assert raised

# Generated at 2026-11-01 20:22:39.433672
# Unit test for method handle_dump of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_dump():
    @dataclasses.dataclass
    class Person:
        name: str
        age: int
        extra: CatchAll = dataclasses.field(default_factory=dict)

    Person.__init__ = _CatchAllUndefinedParameters.create_init(Person)

    # Instance created with undefined parameters: they should land in 'extra'
    person = Person("Alice", 30, city="Berlin", hobby="reading")
    result = _CatchAllUndefinedParameters.handle_dump(person)
    assert result == {"city": "Berlin", "hobby": "reading"}

    # Instance created without undefined parameters: catch-all stays empty
    plain_person = Person("Bob", 25)
    result = _CatchAllUndefinedParameters.handle_dump(plain_person)
    assert result == {}

    # Explicitly provided catch-all content should also be returned as-is
    explicit_person = Person("Carol", 40, extra={"country": "France"})
    result = _CatchAllUndefinedParameters.handle_dump(explicit_person)
    assert result == {"country": "France"}

# Generated at 2026-11-01 20:23:16.605500
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():# handle_from_dict is abstract, so create a concrete subclass whose
    # implementation delegates to the shared helper methods.
    class _ConcreteAction(_UndefinedParameterAction):
        @staticmethod
        def module_0.handle_from_dict(cls, kvs: Dict[Any, Any]) -> Dict[str, Any]:
            known, _ = _UndefinedParameterAction._separate_defined_undefined_kvs(
                cls=cls, kvs=kvs)
            return known

    @dataclasses.dataclass
    class Person:
        name: str
        age: int

    # Defined fields are kept, undefined ones are separated out
    kvs = {"name": "Alice", "age": 30, "city": "Berlin", "extra": [1, 2]}
    result = _ConcreteAction.handle_from_dict(Person, kvs)
    assert result == {"name": "Alice", "age": 30}, \
        f"Expected only known fields, got {result}"

    # Original input dict must not be mutated
    assert kvs == {"name": "Alice", "age": 30, "city": "Berlin", "extra": [1, 2]}

    # Empty input yields empty dict
    assert _ConcreteAction.handle_from_dict(Person, {}) == {}

    # Default values: fields with defaults may be absent from the input
    @dataclasses.dataclass
    class WithDefault:
        required: int
        optional: str = "fallback"

    result = _ConcreteAction.handle_from_dict(
        WithDefault, {"required": 1, "optional": "given", "junk": True})
    assert result == {"required": 1, "optional": "given"}

    # Non-dataclass input would fail, ensure fields lookup is used on the class
    try:
        _ConcreteAction.handle_from_dict(Person, None)
        raised = False
    except Exception:
        raised = True
    assert raised, "Passing invalid kvs should raise"

# Generated at 2026-11-01 20:23:52.354990
# Unit test for method handle_from_dict of class _UndefinedParameterAction