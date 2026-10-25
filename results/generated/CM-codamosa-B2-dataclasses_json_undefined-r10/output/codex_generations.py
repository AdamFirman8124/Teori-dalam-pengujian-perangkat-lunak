

# Generated at 2026-10-24 04:02:20.854314
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    obj = object()

    result = _UndefinedParameterAction.handle_dump(obj)

    assert result == {}

# Generated at 2026-10-24 04:02:37.847869
# Unit test for method handle_dump of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_dump():
    @dataclass
    class WithCatchAll:
        name: str
        catch_all: CatchAll

    # 1. returns contents of catch-all field
    obj = WithCatchAll(name="a", catch_all={"extra1": 1, "extra2": "x"})
    assert _CatchAllUndefinedParameters.handle_dump(obj) == {
        "extra1": 1, "extra2": "x"
    }

    # 2. empty catch-all returns empty dict
    obj_empty = WithCatchAll(name="a", catch_all={})
    assert _CatchAllUndefinedParameters.handle_dump(obj_empty) == {}

    # 3. works with custom field name
    @dataclass
    class WithCustomName:
        name: str
        my_unknown: CatchAll

    obj_custom = WithCustomName(name="a", my_unknown={"foo": "bar"})
    assert _CatchAllUndefinedParameters.handle_dump(obj_custom) == {
        "foo": "bar"
    }

    # 4. no CatchAll field -> raises
    @dataclass
    class WithoutCatchAll:
        name: str

    with pytest.raises(UndefinedParameterError):
        _CatchAllUndefinedParameters.handle_dump(WithoutCatchAll(name="a"))

# Generated at 2026-10-24 04:02:53.616049
# Unit test for constructor of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters():
    @dataclasses.dataclass
    class Example:
        required: int
        optional: str = "default"

    Example.__init__ = _IgnoreUndefinedParameters.create_init(Example)

    # Unknown keyword and excess positional arguments should be ignored.
    instance = Example(
        1,
        "provided",
        "ignored positional argument",
        unknown="ignored keyword argument",
    )

    assert instance.required == 1
    assert instance.optional == "provided"
    assert not hasattr(instance, "unknown")

    # Defaults should still be applied.
    instance_with_default = Example(required=2, another_unknown=True)

    assert instance_with_default.required == 2
    assert instance_with_default.optional == "default"
    assert not hasattr(instance_with_default, "another_unknown")

# Generated at 2026-10-24 04:03:20.447077
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    @dataclasses.dataclass
    class Example:
        a: int
        b: str

    # 1. Defined parameters are returned untouched
    result = _RaiseUndefinedParameters.handle_from_dict(
        Example, {"a": 1, "b": "x"})
    assert result == {"a": 1, "b": "x"}

    # 2. Unknown parameters raise UndefinedParameterError
    with pytest.raises(UndefinedParameterError, match="undefined"):
        _RaiseUndefinedParameters.handle_from_dict(
            Example, {"a": 1, "b": "x", "c": 3})

    # 3. Unknown parameters are silently separated out (base separation logic)
    known, unknown = _UndefinedParameterAction._separate_defined_undefined_kvs(
        Example, {"a": 1, "c": 3})
    assert known == {"a": 1}
    assert unknown == {"c": 3}

    # 4. EXCLUDE drops unknown parameters
    result = _IgnoreUndefinedParameters.handle_from_dict(
        Example, {"a": 1, "c": 3})
    assert result == {"a": 1}

    # 5. INCLUDE collects unknown parameters into the CatchAll field
    @dataclasses.dataclass
    class WithCatchAll:
        a: int
        extra: CatchAll = None

    result = _CatchAllUndefinedParameters.handle_from_dict(
        WithCatchAll, {"a": 1, "c": 3, "d": 4})
    assert result == {"a": 1, "extra": {"c": 3, "d": 4}}

# Generated at 2026-10-24 04:03:22.085459
# Unit test for method handle_dump of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_dump():
    @dataclass
    class WithCatchAll:
        name: str
        catch_all: CatchAll

    # 1. returns contents of catch-all field
    obj = WithCatchAll(name="a", catch_all={"extra1": 1, "extra2": "x"})
    assert _CatchAllUndefinedParameters.handle_dump(obj) == {
        "extra1": 1, "extra2": "x"
    }

    # 2. empty catch-all returns empty dict
    obj_empty = WithCatchAll(name="a", catch_all={})
    assert _CatchAllUndefinedParameters.handle_dump(obj_empty) == {}

    # 3. works with custom field name
    @dataclass
    class WithCustomName:
        name: str
        my_unknown: CatchAll

    obj_custom = WithCustomName(name="a", my_unknown={"foo": "bar"})
    assert _CatchAllUndefinedParameters.handle_dump(obj_custom) == {
        "foo": "bar"
    }

    # 4. no CatchAll field -> raises
    @dataclass
    class WithoutCatchAll:
        name: str

    with pytest.raises(UndefinedParameterError):
        _CatchAllUndefinedParameters.handle_dump(WithoutCatchAll(name="a"))

# Generated at 2026-10-24 04:03:33.258160
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    # create_init on the base class must return the class's original
    # __init__ unmodified (identity check)
    @dataclasses.dataclass
    class Example:
        a: int
        b: str = "default"

    result = _UndefinedParameterAction.create_init(Example)
    assert result is Example.__init__

    # The returned init must still behave like the real one
    instance = Example.__new__(Example)
    result(instance, 42)
    assert instance.a == 42
    assert instance.b == "default"

    # Works with keyword arguments too
    instance2 = Example.__new__(Example)
    result(instance2, a=1, b="custom")
    assert instance2.a == 1
    assert instance2.b == "custom"

# Generated at 2026-10-24 04:03:42.154702
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    # Arrange
    dummy_obj = object()
    kvs = {"a": 1, "b": "two", "c": [3, 4]}

    # Act
    result = _UndefinedParameterAction.handle_to_dict(dummy_obj, kvs)

    # Assert
    assert result == {"a": 1, "b": "two", "c": [3, 4]}
    assert result is kvs  # base implementation returns the same dict unchanged

# Generated at 2026-10-24 04:03:47.785642
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    message = "Received an undefined parameter"

    error = UndefinedParameterError(message)

    assert isinstance(error, ValidationError)
    assert str(error) == message
    assert error.messages == [message]

# Generated at 2026-10-24 04:04:04.477054
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    @dataclasses.dataclass
    class Example:
        a: int
        b: str

    # 1. Defined parameters are returned untouched
    result = _RaiseUndefinedParameters.handle_from_dict(
        Example, {"a": 1, "b": "x"})
    assert result == {"a": 1, "b": "x"}

    # 2. Unknown parameters raise UndefinedParameterError
    with pytest.raises(UndefinedParameterError, match="undefined"):
        _RaiseUndefinedParameters.handle_from_dict(
            Example, {"a": 1, "b": "x", "c": 3})

    # 3. Unknown parameters are silently separated out (base separation logic)
    known, unknown = _UndefinedParameterAction._separate_defined_undefined_kvs(
        Example, {"a": 1, "c": 3})
    assert known == {"a": 1}
    assert unknown == {"c": 3}

    # 4. EXCLUDE drops unknown parameters
    result = _IgnoreUndefinedParameters.handle_from_dict(
        Example, {"a": 1, "c": 3})
    assert result == {"a": 1}

    # 5. INCLUDE collects unknown parameters into the CatchAll field
    @dataclasses.dataclass
    class WithCatchAll:
        a: int
        extra: CatchAll = None

    result = _CatchAllUndefinedParameters.handle_from_dict(
        WithCatchAll, {"a": 1, "c": 3, "d": 4})
    assert result == {"a": 1, "extra": {"c": 3, "d": 4}}

# Generated at 2026-10-24 04:04:35.115863
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    input_parameters = {"name": "Alice", "age": 30}

    # Abstract static methods can still be called directly on the class.
    result = _UndefinedParameterAction.handle_from_dict(
        cls=object,
        kvs=input_parameters,
    )

    # The base implementation contains only `pass`.
    assert result is None
    assert input_parameters == {"name": "Alice", "age": 30}

# Generated at 2026-10-24 04:04:52.712063
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    result = _UndefinedParameterAction.handle_dump(obj=None)

    assert result == {}

# Generated at 2026-10-24 04:04:55.727212
# Unit test for method handle_dump of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_dump():
    @dataclass
    class WithCatchAll:
        name: str
        catch_all: CatchAll

    # 1. returns contents of catch-all field
    obj = WithCatchAll(name="a", catch_all={"extra1": 1, "extra2": "x"})
    assert _CatchAllUndefinedParameters.handle_dump(obj) == {
        "extra1": 1, "extra2": "x"
    }

    # 2. empty catch-all returns empty dict
    obj_empty = WithCatchAll(name="a", catch_all={})
    assert _CatchAllUndefinedParameters.handle_dump(obj_empty) == {}

    # 3. works with custom field name
    @dataclass
    class WithCustomName:
        name: str
        my_unknown: CatchAll

    obj_custom = WithCustomName(name="a", my_unknown={"foo": "bar"})
    assert _CatchAllUndefinedParameters.handle_dump(obj_custom) == {
        "foo": "bar"
    }

    # 4. no CatchAll field -> raises
    @dataclass
    class WithoutCatchAll:
        name: str

    with pytest.raises(UndefinedParameterError):
        _CatchAllUndefinedParameters.handle_dump(WithoutCatchAll(name="a"))

# Generated at 2026-10-24 04:05:16.668745
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    obj = object()

    result = _UndefinedParameterAction.handle_dump(obj)

    assert result == {}

# Generated at 2026-10-24 04:05:41.245312
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    assert "handle_from_dict" in _UndefinedParameterAction.__abstractmethods__
    assert _UndefinedParameterAction.handle_from_dict.__isabstractmethod__

    with pytest.raises(TypeError, match="abstract class"):
        _UndefinedParameterAction()

# Generated at 2026-10-24 04:06:06.026484
# Unit test for method handle_dump of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:06:12.170661
# Unit test for method handle_dump of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:06:17.173353
# Unit test for method handle_dump of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:06:24.977076
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    @dataclasses.dataclass
    class TestClass:
        name: str
        age: int = 0

    # Defined parameters are returned unchanged.
    parameters = {"name": "Alice", "age": 30}
    assert _RaiseUndefinedParameters.handle_from_dict(
        TestClass, parameters
    ) == parameters

    # Undefined parameters raise UndefinedParameterError.
    with pytest.raises(
        UndefinedParameterError,
        match="Received undefined initialization arguments",
    ) as exc_info:
        _RaiseUndefinedParameters.handle_from_dict(
            TestClass,
            {"name": "Alice", "unknown": "value"},
        )

    assert exc_info.value.messages == (
        "Received undefined initialization arguments "
        "{'unknown': 'value'}"
    )

# Generated at 2026-10-24 04:06:26.505030
# Unit test for method handle_dump of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_dump():
    @dataclass
    class WithCatchAll:
        name: str
        catch_all: CatchAll

    # 1. returns contents of catch-all field
    obj = WithCatchAll(name="a", catch_all={"extra1": 1, "extra2": "x"})
    assert _CatchAllUndefinedParameters.handle_dump(obj) == {
        "extra1": 1, "extra2": "x"
    }

    # 2. empty catch-all returns empty dict
    obj_empty = WithCatchAll(name="a", catch_all={})
    assert _CatchAllUndefinedParameters.handle_dump(obj_empty) == {}

    # 3. works with custom field name
    @dataclass
    class WithCustomName:
        name: str
        my_unknown: CatchAll

    obj_custom = WithCustomName(name="a", my_unknown={"foo": "bar"})
    assert _CatchAllUndefinedParameters.handle_dump(obj_custom) == {
        "foo": "bar"
    }

    # 4. no CatchAll field -> raises
    @dataclass
    class WithoutCatchAll:
        name: str

    with pytest.raises(UndefinedParameterError):
        _CatchAllUndefinedParameters.handle_dump(WithoutCatchAll(name="a"))

# Generated at 2026-10-24 04:06:52.822564
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:07:07.981906
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:07:09.300995
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:07:38.495576
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:07:44.434016
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:07:50.474720
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:07:51.907871
# Unit test for method handle_dump of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_dump():
    @dataclass
    class WithCatchAll:
        name: str
        catch_all: CatchAll

    # 1. returns contents of catch-all field
    obj = WithCatchAll(name="a", catch_all={"extra1": 1, "extra2": "x"})
    assert _CatchAllUndefinedParameters.handle_dump(obj) == {
        "extra1": 1, "extra2": "x"
    }

    # 2. empty catch-all returns empty dict
    obj_empty = WithCatchAll(name="a", catch_all={})
    assert _CatchAllUndefinedParameters.handle_dump(obj_empty) == {}

    # 3. works with custom field name
    @dataclass
    class WithCustomName:
        name: str
        my_unknown: CatchAll

    obj_custom = WithCustomName(name="a", my_unknown={"foo": "bar"})
    assert _CatchAllUndefinedParameters.handle_dump(obj_custom) == {
        "foo": "bar"
    }

    # 4. no CatchAll field -> raises
    @dataclass
    class WithoutCatchAll:
        name: str

    with pytest.raises(UndefinedParameterError):
        _CatchAllUndefinedParameters.handle_dump(WithoutCatchAll(name="a"))

# Generated at 2026-10-24 04:07:53.242425
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    # create_init on the base class must return the class's original
    # __init__ unmodified (identity check)
    @dataclasses.dataclass
    class Example:
        a: int
        b: str = "default"

    result = _UndefinedParameterAction.create_init(Example)
    assert result is Example.__init__

    # The returned init must still behave like the real one
    instance = Example.__new__(Example)
    result(instance, 42)
    assert instance.a == 42
    assert instance.b == "default"

    # Works with keyword arguments too
    instance2 = Example.__new__(Example)
    result(instance2, a=1, b="custom")
    assert instance2.a == 1
    assert instance2.b == "custom"

# Generated at 2026-10-24 04:07:59.384079
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    @dataclasses.dataclass
    class Example:
        name: str
        age: int = 0

    parameters = {
        "name": "Alice",
        "age": 30,
    }

    result = _RaiseUndefinedParameters.handle_from_dict(Example, parameters)

    assert result == parameters

    parameters_with_unknown = {
        "name": "Alice",
        "age": 30,
        "unexpected": True,
    }

    with pytest.raises(UndefinedParameterError) as exc_info:
        _RaiseUndefinedParameters.handle_from_dict(
            Example, parameters_with_unknown
        )

    assert "Received undefined initialization arguments" in str(exc_info.value)
    assert "'unexpected': True" in str(exc_info.value)

# Generated at 2026-10-24 04:08:00.700915
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    # Arrange
    dummy_obj = object()
    kvs = {"a": 1, "b": "two", "c": [3, 4]}

    # Act
    result = _UndefinedParameterAction.handle_to_dict(dummy_obj, kvs)

    # Assert
    assert result == {"a": 1, "b": "two", "c": [3, 4]}
    assert result is kvs  # base implementation returns the same dict unchanged

# Generated at 2026-10-24 04:08:02.032806
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    # Arrange
    dummy_obj = object()
    kvs = {"a": 1, "b": "two", "c": [3, 4]}

    # Act
    result = _UndefinedParameterAction.handle_to_dict(dummy_obj, kvs)

    # Assert
    assert result == {"a": 1, "b": "two", "c": [3, 4]}
    assert result is kvs  # base implementation returns the same dict unchanged

# Generated at 2026-10-24 04:08:22.117041
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    obj = object()

    result = _UndefinedParameterAction.handle_dump(obj)

    assert result == {}
    assert isinstance(result, dict)

# Generated at 2026-10-24 04:08:24.639440
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 04:08:27.058577
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 04:08:29.476271
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 04:08:31.890125
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 04:08:34.322991
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 04:08:40.783621
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():result = _UndefinedParameterAction.handle_from_dict(int, {"x": 1})

# Generated at 2026-10-24 04:08:51.505054
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:08:52.817406
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:08:54.143473
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:09:07.275704
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:09:08.584695
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:09:09.897843
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:09:11.225085
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    # Arrange
    dummy_obj = object()
    kvs = {"a": 1, "b": "two", "c": [3, 4]}

    # Act
    result = _UndefinedParameterAction.handle_to_dict(dummy_obj, kvs)

    # Assert
    assert result == {"a": 1, "b": "two", "c": [3, 4]}
    assert result is kvs  # base implementation returns the same dict unchanged

# Generated at 2026-10-24 04:09:37.381656
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    class ConcreteUndefinedParameterAction(_UndefinedParameterAction):
        @staticmethod
        def module_0.handle_from_dict(cls, kvs: Dict[Any, Any]) -> Dict[str, Any]:
            return dict(kvs)

    input_parameters = {"name": "Alice", "age": 30}

    result = ConcreteUndefinedParameterAction.handle_from_dict(
        object(),
        input_parameters,
    )

    assert result == input_parameters
    assert result is not input_parameters
    assert "handle_from_dict" in _UndefinedParameterAction.__abstractmethods__

# Generated at 2026-10-24 04:09:54.383270
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 04:09:55.719263
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 04:10:26.533732
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    obj = Sample(a=5, b="y")

    # Base implementation returns an empty dict, ignoring the object.
    assert _UndefinedParameterAction.handle_dump(obj) == {}

    # Subclasses that don't override handle_dump inherit the same behavior.
    assert _RaiseUndefinedParameters.handle_dump(obj) == {}
    assert _IgnoreUndefinedParameters.handle_dump(obj) == {}

    # Works with any object (including None) since obj is unused.
    assert _UndefinedParameterAction.handle_dump(None) == {}

    # Must not mutate the passed object.
    assert dataclasses.asdict(obj) == {"a": 5, "b": "y"}

# Generated at 2026-10-24 04:10:40.360071
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:10:46.198086
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:10:52.952256
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:11:09.171016
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:11:15.069738
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:11:17.625088
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:11:20.094256
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:11:22.511131
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:11:24.922488
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:11:27.336797
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 04:11:29.757074
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 04:11:32.172253
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 04:11:34.587724
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-24 04:11:37.154512
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-24 04:11:39.572579
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-24 04:11:41.989674
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 04:11:44.407468
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 04:11:46.820562
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 04:11:49.236782
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:11:51.655099
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:11:54.073461
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:11:56.489280
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 04:12:06.065351
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():obj = object()

# Generated at 2026-10-24 04:12:07.416307
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    # create_init on the base class must return the class's original
    # __init__ unmodified (identity check)
    @dataclasses.dataclass
    class Example:
        a: int
        b: str = "default"

    result = _UndefinedParameterAction.create_init(Example)
    assert result is Example.__init__

    # The returned init must still behave like the real one
    instance = Example.__new__(Example)
    result(instance, 42)
    assert instance.a == 42
    assert instance.b == "default"

    # Works with keyword arguments too
    instance2 = Example.__new__(Example)
    result(instance2, a=1, b="custom")
    assert instance2.a == 1
    assert instance2.b == "custom"