

# Generated at 2026-10-24 04:15:11.802832
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:15:14.217708
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:15:16.636998
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:15:19.058373
# Unit test for constructor of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:15:21.469501
# Unit test for constructor of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:15:23.882636
# Unit test for constructor of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:15:26.292779
# Unit test for constructor of class _RaiseUndefinedParameters

# Generated at 2026-10-24 04:15:28.707236
# Unit test for constructor of class _RaiseUndefinedParameters

# Generated at 2026-10-24 04:15:31.124745
# Unit test for constructor of class _RaiseUndefinedParameters

# Generated at 2026-10-24 04:15:46.795791
# Unit test for method handle_dump of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:15:54.798113
# Unit test for method handle_dump of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:15:59.744555
# Unit test for method handle_dump of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:16:07.824977
# Unit test for constructor of class _UndefinedParameterAction
def test__UndefinedParameterAction():
    # 1. ABC has an abstract method -> direct instantiation must fail
    with pytest.raises(TypeError) as exc_info:
        _UndefinedParameterAction()
    assert "handle_from_dict" in str(exc_info.value)

    # 2. It is registered as abstract
    assert _UndefinedParameterAction.__abstractmethods__ == frozenset(
        {"handle_from_dict"}
    )

    # 3. A subclass implementing the abstract method is instantiable
    class _Concrete(_UndefinedParameterAction):
        @staticmethod
        def handle_from_dict(cls, kvs):
            return kvs

    assert _Concrete.__abstractmethods__ == frozenset()
    instance = _Concrete()
    assert isinstance(instance, _UndefinedParameterAction)

    # 4. Concrete (non-abstract) default implementations are inherited
    kvs = {"a": 1}
    assert _Concrete.handle_to_dict(object(), kvs) is kvs
    assert _Concrete.handle_dump(object()) == {}

    class _Obj:
        def __init__(self):
            pass

    assert _Concrete.create_init(_Obj) is _Obj.__init__

    # 5. _separate_defined_undefined_kvs splits on dataclass field names
    import dataclasses

    @dataclasses.dataclass
    class _Dc:
        a: int = 0

    known, unknown = _UndefinedParameterAction._separate_defined_undefined_kvs(
        cls=_Dc, kvs={"a": 1, "b": 2}
    )
    assert known == {"a": 1}
    assert unknown == {"b": 2}

# Generated at 2026-10-24 04:16:19.630567
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    @dataclasses.dataclass
    class Example:
        name: str
        count: int = 0
        extra: CatchAll = None

    # Replace the generated dataclass initializer with the catch-all wrapper.
    Example.__init__ = _CatchAllUndefinedParameters.create_init(Example)

    instance = Example(
        "example",
        3,
        "extra positional argument",
        unknown_key="unknown value",
    )

    assert instance.name == "example"
    assert instance.count == 3
    assert instance.extra == {
        "_UNKNOWN0": "extra positional argument",
        "unknown_key": "unknown value",
    }

    # An explicitly supplied catch-all dictionary is merged with unknown kwargs.
    supplied_extra = {"existing": "value"}
    instance = Example(
        name="another",
        extra=supplied_extra,
        additional=42,
    )

    assert instance.name == "another"
    assert instance.count == 0
    assert instance.extra == {
        "existing": "value",
        "additional": 42,
    }

# Generated at 2026-10-24 04:16:22.049557
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 04:16:24.552715
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 04:16:26.968000
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 04:16:29.384714
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 04:16:31.800037
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 04:16:38.864065
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 04:16:40.178656
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

# Generated at 2026-10-24 04:17:06.204449
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    assert inspect.isabstract(_UndefinedParameterAction)
    assert (
        _UndefinedParameterAction.handle_from_dict.__isabstractmethod__
        is True
    )

    try:
        _UndefinedParameterAction()
    except TypeError as exc:
        assert "abstract method handle_from_dict" in str(exc)
    else:
        raise AssertionError(
            "_UndefinedParameterAction should not be instantiable"
        )

# Generated at 2026-10-24 04:17:16.471662
# Unit test for method handle_from_dict of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_handle_from_dict():
    @dataclasses.dataclass
    class Example:
        name: str
        count: int = 0

    input_parameters = {
        "name": "example",
        "count": 3,
        "unknown": "ignored",
    }

    result = _IgnoreUndefinedParameters.handle_from_dict(
        Example, input_parameters
    )

    assert result == {
        "name": "example",
        "count": 3,
    }
    assert input_parameters == {
        "name": "example",
        "count": 3,
        "unknown": "ignored",
    }

# Generated at 2026-10-24 04:17:26.067421
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:17:28.485900
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:17:30.899799
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:17:33.326890
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 04:17:50.755930
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():import pytest


# Generated at 2026-10-24 04:18:02.019082
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    @dataclasses.dataclass
    class Example:
        required: int
        optional: str = "default"

    # Replace the generated dataclass initializer with the wrapped initializer.
    Example.__init__ = _IgnoreUndefinedParameters.create_init(Example)

    # Unknown keyword arguments and excess positional arguments are ignored.
    instance = Example(1, "provided", "ignored", unknown="ignored")

    assert instance.required == 1
    assert instance.optional == "provided"
    assert not hasattr(instance, "unknown")

    # Dataclass defaults are still applied.
    instance_with_default = Example(required=2, another_unknown=True)

    assert instance_with_default.required == 2
    assert instance_with_default.optional == "default"
    assert not hasattr(instance_with_default, "another_unknown")

# Generated at 2026-10-24 04:18:03.351845
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

# Generated at 2026-10-24 04:18:23.007644
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    @dataclasses.dataclass
    class Example:
        name: str
        extras: CatchAll = None

    Example.__init__ = _CatchAllUndefinedParameters.create_init(Example)

    # Unknown keyword and excess positional arguments are captured.
    instance = Example(
        "Alice",
        "first unknown positional",
        "second unknown positional",
        age=30,
    )

    assert instance.name == "Alice"
    assert instance.extras == {
        "_UNKNOWN0": "first unknown positional",
        "_UNKNOWN1": "second unknown positional",
        "age": 30,
    }

    # Explicit catch-all contents are preserved and merged with unknown values.
    instance = Example(
        "Bob",
        extras={"existing": "value"},
        active=True,
    )

    assert instance.name == "Bob"
    assert instance.extras == {
        "existing": "value",
        "active": True,
    }

    # The catch-all field is initialized to an empty dictionary when omitted.
    instance = Example("Charlie")

    assert instance.name == "Charlie"
    assert instance.extras == {}

# Generated at 2026-10-24 04:18:25.511135
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 04:18:27.930462
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 04:18:30.351169
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 04:18:32.761514
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 04:18:35.176530
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 04:18:37.599374
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 04:18:40.022001
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 04:18:42.615033
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():import pytest


# Generated at 2026-10-24 04:19:07.855648
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    class IncompleteAction(_UndefinedParameterAction):
        pass

    # The method is abstract and must be implemented by subclasses.
    with pytest.raises(TypeError):
        IncompleteAction()

    expected_cls = object()
    parameters = {"name": "Alice", "age": 30}

    class ConcreteAction(_UndefinedParameterAction):
        @staticmethod
        def module_0.handle_from_dict(cls, kvs):
            assert cls is expected_cls
            return dict(kvs)

    action = ConcreteAction()
    result = action.handle_from_dict(expected_cls, parameters)

    assert result == parameters
    assert result is not parameters

# Generated at 2026-10-24 04:19:17.138985
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:19:18.535872
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:19:19.871941
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:19:21.186648
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

# Generated at 2026-10-24 04:19:27.959569
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    @dataclasses.dataclass
    class Example:
        name: str
        age: int

    parameters = {"name": "Alice", "age": 30}

    result = _RaiseUndefinedParameters.handle_from_dict(Example, parameters)

    assert result == parameters

    with pytest.raises(UndefinedParameterError) as exc_info:
        _RaiseUndefinedParameters.handle_from_dict(
            Example,
            {"name": "Alice", "age": 30, "unknown": "value"},
        )

    assert "Received undefined initialization arguments" in str(exc_info.value)
    assert "'unknown': 'value'" in str(exc_info.value)

# Generated at 2026-10-24 04:19:29.275649
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

# Generated at 2026-10-24 04:19:49.677718
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    obj = object()

    result = _UndefinedParameterAction.handle_dump(obj)

    assert result == {}

# Generated at 2026-10-24 04:19:51.040144
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

# Generated at 2026-10-24 04:20:05.317854
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:20:11.248775
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:20:16.369136
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:20:30.148392
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    result = _UndefinedParameterAction.handle_dump(obj=object())

    assert result == {}

# Generated at 2026-10-24 04:20:31.739643
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

# Generated at 2026-10-24 04:20:34.159518
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 04:20:36.690432
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 04:20:39.182881
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 04:20:41.597343
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 04:20:46.875443
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 04:20:54.254608
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 04:21:09.084685
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    @dataclasses.dataclass
    class Example:
        name: str
        age: int = 0

    # Defined parameters are returned unchanged.
    parameters = {"name": "Alice", "age": 30}
    assert _RaiseUndefinedParameters.handle_from_dict(
        Example, parameters
    ) == parameters

    # Undefined parameters raise an error.
    with pytest.raises(UndefinedParameterError) as exc_info:
        _RaiseUndefinedParameters.handle_from_dict(
            Example,
            {"name": "Alice", "unknown": "value"},
        )

    assert "undefined initialization arguments" in str(exc_info.value)
    assert "'unknown': 'value'" in str(exc_info.value)

# Generated at 2026-10-24 04:21:29.482943
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:21:34.150039
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:21:36.653419
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:21:39.075366
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:21:41.482221
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:21:43.901286
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:21:46.313825
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 04:21:48.734629
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 04:21:50.104842
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():obj = object()

# Generated at 2026-10-24 04:21:51.559825
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

# Generated at 2026-10-24 04:22:12.583317
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    obj = object()

    result = _UndefinedParameterAction.handle_dump(obj)

    assert result == {}

# Generated at 2026-10-24 04:22:13.883725
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

# Generated at 2026-10-24 04:22:30.402496
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:22:35.666254
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:22:38.088737
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:22:40.593181
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 04:22:43.008805
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 04:22:45.570796
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 04:22:48.068178
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:22:50.482703
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:22:52.897160
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:23:14.741673
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:23:53.526804
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:23:55.941032
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:24:08.707825
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    obj = object()

    result = _UndefinedParameterAction.handle_dump(obj)

    assert result == {}

# Generated at 2026-10-24 04:24:20.177677
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:24:21.509863
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:24:22.829493
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 04:24:32.873648
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    @dataclasses.dataclass
    class Example:
        required: int
        optional: str = "default"

    Example.__init__ = _IgnoreUndefinedParameters.create_init(Example)

    # Unknown keyword arguments are ignored.
    instance = Example(1, optional="provided", unknown="ignored")
    assert instance.required == 1
    assert instance.optional == "provided"
    assert not hasattr(instance, "unknown")

    # Excess positional arguments are ignored.
    instance = Example(2, "value", "ignored")
    assert instance.required == 2
    assert instance.optional == "value"

    # Dataclass defaults are preserved.
    instance = Example(3, another_unknown=True)
    assert instance.required == 3
    assert instance.optional == "default"

# Generated at 2026-10-24 04:24:49.519566
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

# Generated at 2026-10-24 04:24:52.024280
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 04:24:54.444683
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 04:24:56.859174
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 04:24:58.217392
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

# Generated at 2026-10-24 04:25:05.334956
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    message = "Received an undefined parameter"

    error = UndefinedParameterError(message)

    assert isinstance(error, UndefinedParameterError)
    assert isinstance(error, ValidationError)
    assert error.messages == [message]
    assert str(error) == message

# Generated at 2026-10-24 04:25:13.731247
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    message = "Received an undefined parameter"

    error = UndefinedParameterError(message)

    assert isinstance(error, UndefinedParameterError)
    assert isinstance(error, ValidationError)
    assert error.messages == [message]
    assert str(error) == message