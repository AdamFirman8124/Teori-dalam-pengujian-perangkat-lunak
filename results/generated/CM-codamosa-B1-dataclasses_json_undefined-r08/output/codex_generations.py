

# Generated at 2026-10-24 23:14:03.272606
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    @dataclasses.dataclass
    class TestClass:
        name: str
        extra: CatchAll = None

    obj = TestClass(
        name="example",
        extra={"unknown_field": 42, "another_field": "value"},
    )
    values = {
        "name": obj.name,
        "extra": obj.extra,
    }

    result = _CatchAllUndefinedParameters.handle_to_dict(obj, values)

    assert result == {
        "name": "example",
        "unknown_field": 42,
        "another_field": "value",
    }
    assert "extra" not in result

# Generated at 2026-10-24 23:14:19.257646
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    @dataclasses.dataclass
    class Example:
        name: str
        count: int = 10

    ignored_init = _IgnoreUndefinedParameters.create_init(Example)

    instance = Example.__new__(Example)
    ignored_init(
        instance,
        "kept",
        "ignored positional argument",
        count=3,
        unknown="ignored keyword argument",
    )

    assert instance.name == "kept"
    assert instance.count == 3
    assert not hasattr(instance, "unknown")

    # Defined defaults should still be applied.
    instance_with_default = Example.__new__(Example)
    ignored_init(instance_with_default, "defaulted", another_unknown=True)

    assert instance_with_default.name == "defaulted"
    assert instance_with_default.count == 10
    assert not hasattr(instance_with_default, "another_unknown")

# Generated at 2026-10-24 23:14:24.491762
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    obj = object()

    result = _UndefinedParameterAction.handle_dump(obj)

    assert result == {}

# Generated at 2026-10-24 23:14:31.358155
# Unit test for constructor of class _UndefinedParameterAction
def test__UndefinedParameterAction():
    with pytest.raises(
        TypeError,
        match=r"Can't instantiate abstract class .* with abstract method handle_from_dict",
    ):
        _UndefinedParameterAction()

# Generated at 2026-10-24 23:14:38.623038
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    from marshmallow import ValidationError

    # Constructor takes a message and stores it like ValidationError
    error = UndefinedParameterError("Received undefined initialization arguments {'foo': 1}")

    assert isinstance(error, UndefinedParameterError)
    assert isinstance(error, ValidationError)
    assert error.messages == ["Received undefined initialization arguments {'foo': 1}"]
    assert "foo" in str(error)

    # Empty message must also be constructible
    empty_error = UndefinedParameterError()
    assert isinstance(empty_error, ValidationError)


# Run directly: `python -m pytest this_file.py -k UndefinedParameterError`
if __name__ == "__main__":
    test_UndefinedParameterError()
    print("test_UndefinedParameterError passed")

# Generated at 2026-10-24 23:14:45.892472
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    # All parameters defined -> passed through unchanged
    kvs = {"name": "Alice", "age": 30}
    result = _RaiseUndefinedParameters.handle_from_dict(_SampleClass, kvs)
    assert result == {"name": "Alice", "age": 30}

    # One unknown parameter -> raises UndefinedParameterError
    kvs_with_unknown = {"name": "Alice", "age": 30, "unknown_param": "oops"}
    with pytest.raises(UndefinedParameterError) as exc_info:
        _RaiseUndefinedParameters.handle_from_dict(_SampleClass, kvs_with_unknown)
    assert "unknown_param" in str(exc_info.value)

    # Multiple unknown parameters -> all reported in the error
    kvs_multi_unknown = {"name": "Bob", "foo": 1, "bar": 2}
    with pytest.raises(UndefinedParameterError) as exc_info:
        _RaiseUndefinedParameters.handle_from_dict(_SampleClass, kvs_multi_unknown)
    assert "foo" in str(exc_info.value)
    assert "bar" in str(exc_info.value)

# Generated at 2026-10-24 23:14:47.635003
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    class Dummy:
        def __init__(self, x=1):
            self.x = x

    # base implementation must return original __init__ unwrapped
    assert _UndefinedParameterAction.create_init(Dummy) == Dummy.__init__

    # returned callable must still work as init
    obj = Dummy.__new__(Dummy)
    init = _UndefinedParameterAction.create_init(Dummy)
    assert callable(init)
    init(obj, x=42)
    assert obj.x == 42

# Generated at 2026-10-24 23:14:58.014143
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    @dataclasses.dataclass
    class Example:
        required: int
        optional: str = "default"

    Example.__init__ = _IgnoreUndefinedParameters.create_init(Example)

    # Unknown keyword and excess positional arguments are ignored.
    instance = Example(1, "provided", "ignored", unknown="ignored")

    assert instance.required == 1
    assert instance.optional == "provided"
    assert not hasattr(instance, "unknown")

    # Dataclass defaults are preserved when optional values are omitted.
    instance_with_default = Example(required=2, another_unknown=True)

    assert instance_with_default.required == 2
    assert instance_with_default.optional == "default"

# Generated at 2026-10-24 23:15:06.063856
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    @dataclasses.dataclass
    class Example:
        name: str
        extra: CatchAll = None

    obj = Example(name="Alice", extra={"age": 30, "active": True})
    values = {
        "name": "Alice",
        "extra": {"age": 30, "active": True},
    }

    result = _CatchAllUndefinedParameters.handle_to_dict(obj, values)

    assert result == {
        "name": "Alice",
        "age": 30,
        "active": True,
    }
    assert "extra" not in result
    assert result is values  # The method modifies and returns the input dict.

# Generated at 2026-10-24 23:15:07.497149
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    # All parameters defined -> passed through unchanged
    kvs = {"name": "Alice", "age": 30}
    result = _RaiseUndefinedParameters.handle_from_dict(_SampleClass, kvs)
    assert result == {"name": "Alice", "age": 30}

    # One unknown parameter -> raises UndefinedParameterError
    kvs_with_unknown = {"name": "Alice", "age": 30, "unknown_param": "oops"}
    with pytest.raises(UndefinedParameterError) as exc_info:
        _RaiseUndefinedParameters.handle_from_dict(_SampleClass, kvs_with_unknown)
    assert "unknown_param" in str(exc_info.value)

    # Multiple unknown parameters -> all reported in the error
    kvs_multi_unknown = {"name": "Bob", "foo": 1, "bar": 2}
    with pytest.raises(UndefinedParameterError) as exc_info:
        _RaiseUndefinedParameters.handle_from_dict(_SampleClass, kvs_multi_unknown)
    assert "foo" in str(exc_info.value)
    assert "bar" in str(exc_info.value)

# Generated at 2026-10-24 23:15:12.003434
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    obj = object()

    result = _UndefinedParameterAction.handle_dump(obj)

    assert result == {}

# Generated at 2026-10-24 23:15:21.475863
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    # The base implementation defines an abstract contract and cannot be
    # instantiated directly.
    assert _UndefinedParameterAction.handle_from_dict.__isabstractmethod__

    with pytest.raises(TypeError, match="abstract method handle_from_dict"):
        _UndefinedParameterAction()

    class ConcreteAction(_UndefinedParameterAction):
        @staticmethod
        def module_0.handle_from_dict(cls, kvs):
            return dict(kvs)

    input_values = {"name": "Alice", "age": 30}

    assert ConcreteAction.handle_from_dict(object, input_values) == input_values

# Generated at 2026-10-24 23:15:23.897318
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 23:15:26.318468
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 23:15:28.735295
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 23:15:44.357682
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    import dataclasses
    import inspect

    class Dummy:
        def __init__(self, x=1, y="hello"):
            self.x = x
            self.y = y

    result = _UndefinedParameterAction.create_init(Dummy)

    assert callable(result)
    assert result is Dummy.__init__
    assert inspect.signature(result) == inspect.signature(Dummy.__init__)

    instance = Dummy(5, "world")
    assert instance.x == 5
    assert instance.y == "world"

    instance2 = object.__new__(Dummy)
    result(instance2, 7, "again")
    assert instance2.x == 7
    assert instance2.y == "again"

    instance3 = object.__new__(Dummy)
    result(instance3)
    assert instance3.x == 1
    assert instance3.y == "hello"

    @dataclasses.dataclass
    class Point:
        x: int
        y: int = 2

    dataclass_result = _UndefinedParameterAction.create_init(Point)

    assert callable(dataclass_result)
    assert dataclass_result is Point.__init__

    point = Point(3)
    assert point.x == 3
    assert point.y == 2

    point2 = object.__new__(Point)
    dataclass_result(point2, 4, 5)
    assert point2.x == 4
    assert point2.y == 5

# Generated at 2026-10-24 23:15:49.276321
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    obj = object()

    result = _UndefinedParameterAction.handle_dump(obj)

    assert result == {}

# Generated at 2026-10-24 23:15:50.641709
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    class Dummy:
        def __init__(self, x=1):
            self.x = x

    # base implementation must return original __init__ unwrapped
    assert _UndefinedParameterAction.create_init(Dummy) == Dummy.__init__

    # returned callable must still work as init
    obj = Dummy.__new__(Dummy)
    init = _UndefinedParameterAction.create_init(Dummy)
    assert callable(init)
    init(obj, x=42)
    assert obj.x == 42

# Generated at 2026-10-24 23:15:55.989645
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    obj = object()
    kvs = {"name": "Alice", "age": 30}

    result = _UndefinedParameterAction.handle_to_dict(obj, kvs)

    assert result == {"name": "Alice", "age": 30}
    assert result is kvs

# Generated at 2026-10-24 23:16:01.053731
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    obj = object()
    kvs = {"known": 1, "unknown": 2}
    original_kvs = kvs.copy()

    result = _UndefinedParameterAction.handle_to_dict(obj, kvs)

    assert result is kvs
    assert result == original_kvs

# Generated at 2026-10-24 23:16:06.415188
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    obj = object()

    result = _UndefinedParameterAction.handle_dump(obj)

    assert result == {}

# Generated at 2026-10-24 23:16:08.836906
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 23:16:11.426804
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 23:16:13.843490
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 23:16:16.260736
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:16:18.678259
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:16:21.095094
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:16:23.517064
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 23:16:25.946927
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 23:16:28.363188
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 23:16:30.780637
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 23:16:33.198118
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 23:16:35.616457
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 23:16:38.034263
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:16:40.453893
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:16:42.873821
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:16:53.721223
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    import pytest
    from dataclasses import dataclass, field
    from typing import Optional

    @dataclass
    class _TestClass:
        defined_field: str = "value"
        undefined_parameters: Optional[CatchAllVar] = field(
            default_factory=dict, metadata={"dataclasses_json": {
                "undefined": True}})

    # Case 1: catch-all field contains undefined parameters -> merged into kvs
    obj = _TestClass(defined_field="a",
                     undefined_parameters={"extra1": 1, "extra2": 2})
    kvs = {"defined_field": "a", "undefined_parameters": {"extra1": 1,
                                                          "extra2": 2}}
    result = _CatchAllUndefinedParameters.handle_to_dict(obj, kvs)
    assert result == {"defined_field": "a", "extra1": 1, "extra2": 2}
    assert "undefined_parameters" not in result

    # Case 2: catch-all field is empty dict / None -> nothing merged
    obj = _TestClass(defined_field="a", undefined_parameters={})
    kvs = {"defined_field": "a", "undefined_parameters": {}}
    result = _CatchAllUndefinedParameters.handle_to_dict(obj, kvs)
    assert result == {"defined_field": "a"}
    assert "undefined_parameters" not in result

    obj = _TestClass(defined_field="a", undefined_parameters=None)
    kvs = {"defined_field": "a", "undefined_parameters": None}
    result = _CatchAllUndefinedParameters.handle_to_dict(obj, kvs)
    assert result == {"defined_field": "a"}
    assert "undefined_parameters" not in result

    # Case 3: original kvs dict is not mutated unexpectedly beyond the pop
    obj = _TestClass(defined_field="a",
                     undefined_parameters={"x": 1})
    kvs = {"defined_field": "a", "undefined_parameters": {"x": 1},
           "other": True}
    result = _CatchAllUndefinedParameters.handle_to_dict(obj, kvs)
    assert result == {"defined_field": "a", "x": 1, "other": True}

    # Case 4: missing catch-all field in class raises UndefinedParameterError
    @dataclass
    class _NoCatchAllClass:
        defined_field: str = "value"

    obj_no_catch_all = _NoCatchAllClass()
    with pytest.raises(UndefinedParameterError):
        _CatchAllUndefinedParameters.handle_to_dict(obj_no_catch_all,
                                                    {"defined_field": "a"})

    # Case 5: catch-all value that is not a dict is not merged
    obj = _TestClass(defined_field="a", undefined_parameters="not-a-dict")
    kvs = {"defined_field": "a", "undefined_parameters": "not-a-dict"}
    result = _CatchAllUndefinedParameters.handle_to_dict(obj, kvs)
    assert result == {"defined_field": "a"}
    assert "undefined_parameters" not in result

# Generated at 2026-10-24 23:17:11.571089
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    @dataclasses.dataclass
    class Sample:
        required: int
        optional: str = "default"

    Sample.__init__ = _IgnoreUndefinedParameters.create_init(Sample)

    # Unknown keyword arguments and excess positional arguments are ignored.
    instance = Sample(
        42,
        "ignored positional value",
        optional="explicit",
        unknown="ignored keyword value",
    )

    assert instance.required == 42
    assert instance.optional == "explicit"
    assert not hasattr(instance, "unknown")

    # Defaults are still applied when optional parameters are omitted.
    defaulted_instance = Sample(7, another_unknown=True)

    assert defaulted_instance.required == 7
    assert defaulted_instance.optional == "default"

# Generated at 2026-10-24 23:17:12.902106
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    from marshmallow import ValidationError

    # Constructor takes a message and stores it like ValidationError
    error = UndefinedParameterError("Received undefined initialization arguments {'foo': 1}")

    assert isinstance(error, UndefinedParameterError)
    assert isinstance(error, ValidationError)
    assert error.messages == ["Received undefined initialization arguments {'foo': 1}"]
    assert "foo" in str(error)

    # Empty message must also be constructible
    empty_error = UndefinedParameterError()
    assert isinstance(empty_error, ValidationError)


# Run directly: `python -m pytest this_file.py -k UndefinedParameterError`
if __name__ == "__main__":
    test_UndefinedParameterError()
    print("test_UndefinedParameterError passed")

# Generated at 2026-10-24 23:17:22.784740
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    @dataclasses.dataclass
    class Example:
        name: str
        value: int = 0
        extras: CatchAll = dataclasses.field(default_factory=dict)

    # Replace the generated dataclass initializer with the catch-all wrapper.
    Example.__init__ = _CatchAllUndefinedParameters.create_init(Example)

    obj = Example(
        "example",
        42,
        unknown_string="extra",
        unknown_number=123,
    )

    assert obj.name == "example"
    assert obj.value == 42
    assert obj.extras == {
        "unknown_string": "extra",
        "unknown_number": 123,
    }

    # An explicitly supplied catch-all dictionary is merged with unknown
    # keyword arguments.
    obj_with_existing_extras = Example(
        "another",
        extras={"existing": True},
        additional="value",
    )

    assert obj_with_existing_extras.name == "another"
    assert obj_with_existing_extras.value == 0
    assert obj_with_existing_extras.extras == {
        "existing": True,
        "additional": "value",
    }

    # Excess positional arguments are also retained.
    obj_with_excess_args = Example("positional", 10, "unexpected")

    assert obj_with_excess_args.extras == {
        "_UNKNOWN0": "unexpected",
    }

# Generated at 2026-10-24 23:17:25.204106
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 23:17:27.728787
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 23:17:30.147991
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 23:17:32.565465
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 23:17:34.982303
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 23:17:37.399840
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 23:17:39.816469
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:17:42.236308
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:17:44.651286
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:17:47.071337
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 23:17:49.494647
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 23:17:51.912095
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 23:17:54.329491
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:17:56.749625
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:17:59.166905
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:18:01.584947
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:18:04.007048
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:18:10.593811
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:18:19.603232
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    assert _UndefinedParameterAction.handle_from_dict.__isabstractmethod__

    with pytest.raises(TypeError, match=r"abstract method.*handle_from_dict"):
        _UndefinedParameterAction()

# Generated at 2026-10-24 23:18:24.311430
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    obj = object()

    result = _UndefinedParameterAction.handle_dump(obj)

    assert result == {}

# Generated at 2026-10-24 23:18:49.893194
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:18:52.442620
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:18:54.827425
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:18:57.245312
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 23:18:59.662583
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 23:19:02.078890
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 23:19:04.496447
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 23:19:06.912656
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 23:19:09.335283
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 23:19:11.755286
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 23:19:14.172069
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 23:19:16.590465
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 23:19:19.008079
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:19:21.424625
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:19:23.844848
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:19:26.263522
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:19:28.679953
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:19:31.099433
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:19:32.461113
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    from marshmallow import ValidationError

    # Constructor takes a message and stores it like ValidationError
    error = UndefinedParameterError("Received undefined initialization arguments {'foo': 1}")

    assert isinstance(error, UndefinedParameterError)
    assert isinstance(error, ValidationError)
    assert error.messages == ["Received undefined initialization arguments {'foo': 1}"]
    assert "foo" in str(error)

    # Empty message must also be constructible
    empty_error = UndefinedParameterError()
    assert isinstance(empty_error, ValidationError)


# Run directly: `python -m pytest this_file.py -k UndefinedParameterError`
if __name__ == "__main__":
    test_UndefinedParameterError()
    print("test_UndefinedParameterError passed")

# Generated at 2026-10-24 23:19:47.767865
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    @dataclasses.dataclass
    class Example:
        name: str
        value: int = 0
        extras: CatchAll = None

    Example.__init__ = _CatchAllUndefinedParameters.create_init(Example)

    instance = Example(
        "example",
        42,
        "extra positional argument",
        unknown_key="extra keyword argument",
    )

    assert instance.name == "example"
    assert instance.value == 42
    assert instance.extras == {
        "_UNKNOWN0": "extra positional argument",
        "unknown_key": "extra keyword argument",
    }

    # With no unknown parameters, the catch-all field is initialized to an
    # empty dictionary.
    instance_without_unknowns = Example("other")

    assert instance_without_unknowns.name == "other"
    assert instance_without_unknowns.value == 0
    assert instance_without_unknowns.extras == {}

# Generated at 2026-10-24 23:19:53.402079
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    obj = object()
    kvs = {"name": "Alice", 42: True}
    original_kvs = kvs.copy()

    result = _UndefinedParameterAction.handle_to_dict(obj, kvs)

    assert result is kvs
    assert result == original_kvs

# Generated at 2026-10-24 23:19:55.083245
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    class Dummy:
        def __init__(self, x=1):
            self.x = x

    # base implementation must return original __init__ unwrapped
    assert _UndefinedParameterAction.create_init(Dummy) == Dummy.__init__

    # returned callable must still work as init
    obj = Dummy.__new__(Dummy)
    init = _UndefinedParameterAction.create_init(Dummy)
    assert callable(init)
    init(obj, x=42)
    assert obj.x == 42

# Generated at 2026-10-24 23:20:00.933702
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    obj = object()
    kvs = {"name": "Alice", "age": 30}

    result = _UndefinedParameterAction.handle_to_dict(obj, kvs)

    assert result == {"name": "Alice", "age": 30}
    assert result is kvs

# Generated at 2026-10-24 23:20:05.278552
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    obj = object()

    result = _UndefinedParameterAction.handle_dump(obj)

    assert result == {}

# Generated at 2026-10-24 23:20:11.320187
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    obj = object()
    kvs = {"name": "Alice", "age": 30}
    original_kvs = kvs.copy()

    result = _UndefinedParameterAction.handle_to_dict(obj, kvs)

    assert result is kvs
    assert result == original_kvs

# Generated at 2026-10-24 23:20:13.738106
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:20:16.154497
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:20:18.570750
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:20:20.983745
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 23:20:23.401125
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 23:20:25.819619
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 23:20:28.242062
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:20:30.666273
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:20:33.079103
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:20:35.498300
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 23:20:41.527717
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():result = _UndefinedParameterAction.handle_from_dict(dict, {"key": "value"})

# Generated at 2026-10-24 23:20:46.340096
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    obj = object()

    result = _UndefinedParameterAction.handle_dump(obj)

    assert result == {}
    assert isinstance(result, dict)

# Generated at 2026-10-24 23:20:58.822353
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:21:03.954405
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:21:09.379764
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:21:15.012225
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    obj = object()
    kvs = {"name": "Alice", "age": 30}
    original_kvs = kvs.copy()

    result = _UndefinedParameterAction.handle_to_dict(obj, kvs)

    assert result == original_kvs
    assert result is kvs

# Generated at 2026-10-24 23:21:19.724906
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    obj = object()
    kvs = {"name": "Alice", "age": 30}

    result = _UndefinedParameterAction.handle_to_dict(obj, kvs)

    assert result == {"name": "Alice", "age": 30}
    assert result is kvs

# Generated at 2026-10-24 23:21:22.300830
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 23:21:24.927579
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 23:21:27.456579
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 23:21:29.873776
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:21:32.291103
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:21:34.706198
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:21:37.124631
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 23:21:39.540940
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 23:21:41.957058
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 23:21:50.135084
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():message = "Invalid undefined parameter"

# Generated at 2026-10-24 23:21:51.575018
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    class Dummy:
        def __init__(self, x=1):
            self.x = x

    # base implementation must return original __init__ unwrapped
    assert _UndefinedParameterAction.create_init(Dummy) == Dummy.__init__

    # returned callable must still work as init
    obj = Dummy.__new__(Dummy)
    init = _UndefinedParameterAction.create_init(Dummy)
    assert callable(init)
    init(obj, x=42)
    assert obj.x == 42

# Generated at 2026-10-24 23:22:10.276023
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    @dataclasses.dataclass
    class Example:
        name: str
        count: int = 0
        extra: CatchAll = dataclasses.field(default_factory=dict)

    original_init = Example.__init__
    Example.__init__ = _CatchAllUndefinedParameters.create_init(Example)

    # Unknown keyword and surplus positional arguments are captured.
    instance = Example("example", 3, "surplus", unknown="value")

    assert instance.name == "example"
    assert instance.count == 3
    assert instance.extra == {
        "_UNKNOWN0": "surplus",
        "unknown": "value",
    }

    # An explicitly supplied catch-all dictionary is preserved and extended.
    instance = Example(
        "another",
        count=5,
        extra={"existing": True},
        additional=42,
    )

    assert instance.name == "another"
    assert instance.count == 5
    assert instance.extra == {
        "existing": True,
        "additional": 42,
    }

    # functools.wraps preserves access to the original dataclass initializer.
    assert Example.__init__.__wrapped__ is original_init

# Generated at 2026-10-24 23:22:11.605689
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    # All parameters defined -> passed through unchanged
    kvs = {"name": "Alice", "age": 30}
    result = _RaiseUndefinedParameters.handle_from_dict(_SampleClass, kvs)
    assert result == {"name": "Alice", "age": 30}

    # One unknown parameter -> raises UndefinedParameterError
    kvs_with_unknown = {"name": "Alice", "age": 30, "unknown_param": "oops"}
    with pytest.raises(UndefinedParameterError) as exc_info:
        _RaiseUndefinedParameters.handle_from_dict(_SampleClass, kvs_with_unknown)
    assert "unknown_param" in str(exc_info.value)

    # Multiple unknown parameters -> all reported in the error
    kvs_multi_unknown = {"name": "Bob", "foo": 1, "bar": 2}
    with pytest.raises(UndefinedParameterError) as exc_info:
        _RaiseUndefinedParameters.handle_from_dict(_SampleClass, kvs_multi_unknown)
    assert "foo" in str(exc_info.value)
    assert "bar" in str(exc_info.value)

# Generated at 2026-10-24 23:22:16.769134
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    obj = object()

    result = _UndefinedParameterAction.handle_dump(obj)

    assert result == {}

# Generated at 2026-10-24 23:22:26.399493
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    assert (
        "handle_from_dict"
        in _UndefinedParameterAction.__abstractmethods__
    )

    class IncompleteAction(_UndefinedParameterAction):
        pass

    with pytest.raises(TypeError, match="handle_from_dict"):
        IncompleteAction()

# Generated at 2026-10-24 23:22:46.384965
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 23:22:47.710075
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 23:22:49.050690
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    # All parameters defined -> passed through unchanged
    kvs = {"name": "Alice", "age": 30}
    result = _RaiseUndefinedParameters.handle_from_dict(_SampleClass, kvs)
    assert result == {"name": "Alice", "age": 30}

    # One unknown parameter -> raises UndefinedParameterError
    kvs_with_unknown = {"name": "Alice", "age": 30, "unknown_param": "oops"}
    with pytest.raises(UndefinedParameterError) as exc_info:
        _RaiseUndefinedParameters.handle_from_dict(_SampleClass, kvs_with_unknown)
    assert "unknown_param" in str(exc_info.value)

    # Multiple unknown parameters -> all reported in the error
    kvs_multi_unknown = {"name": "Bob", "foo": 1, "bar": 2}
    with pytest.raises(UndefinedParameterError) as exc_info:
        _RaiseUndefinedParameters.handle_from_dict(_SampleClass, kvs_multi_unknown)
    assert "foo" in str(exc_info.value)
    assert "bar" in str(exc_info.value)

# Generated at 2026-10-24 23:22:57.413880
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    @dataclasses.dataclass
    class TestData:
        name: str
        extra: CatchAll = None

    obj = TestData(
        name="example",
        extra={"unknown_string": "value", "unknown_number": 42},
    )
    values = {
        "name": obj.name,
        "extra": obj.extra,
    }

    result = _CatchAllUndefinedParameters.handle_to_dict(obj, values)

    assert result is values
    assert result == {
        "name": "example",
        "unknown_string": "value",
        "unknown_number": 42,
    }
    assert "extra" not in result

# Generated at 2026-10-24 23:23:18.081751
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    @dataclasses.dataclass
    class Example:
        value: int
        extra: CatchAll = None

    original_init = Example.__init__
    Example.__init__ = _CatchAllUndefinedParameters.create_init(Example)

    # Unknown keyword and surplus positional arguments are captured.
    instance = Example(10, "surplus", unknown="value")

    assert instance.value == 10
    assert instance.extra == {
        "_UNKNOWN0": "surplus",
        "unknown": "value",
    }

    # Explicit catch-all values are preserved and merged with unknown kwargs.
    instance_with_existing_extra = Example(
        20,
        extra={"existing": True},
        another="value",
    )

    assert instance_with_existing_extra.value == 20
    assert instance_with_existing_extra.extra == {
        "existing": True,
        "another": "value",
    }

    # With no undefined parameters, the catch-all field is an empty dictionary.
    instance_without_extra = Example(30)

    assert instance_without_extra.value == 30
    assert instance_without_extra.extra == {}

    # functools.wraps should retain the wrapped initializer.
    assert Example.__init__.__wrapped__ is original_init

# Generated at 2026-10-24 23:23:19.436922
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    # All parameters defined -> passed through unchanged
    kvs = {"name": "Alice", "age": 30}
    result = _RaiseUndefinedParameters.handle_from_dict(_SampleClass, kvs)
    assert result == {"name": "Alice", "age": 30}

    # One unknown parameter -> raises UndefinedParameterError
    kvs_with_unknown = {"name": "Alice", "age": 30, "unknown_param": "oops"}
    with pytest.raises(UndefinedParameterError) as exc_info:
        _RaiseUndefinedParameters.handle_from_dict(_SampleClass, kvs_with_unknown)
    assert "unknown_param" in str(exc_info.value)

    # Multiple unknown parameters -> all reported in the error
    kvs_multi_unknown = {"name": "Bob", "foo": 1, "bar": 2}
    with pytest.raises(UndefinedParameterError) as exc_info:
        _RaiseUndefinedParameters.handle_from_dict(_SampleClass, kvs_multi_unknown)
    assert "foo" in str(exc_info.value)
    assert "bar" in str(exc_info.value)

# Generated at 2026-10-24 23:23:25.225623
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    obj = object()
    kvs = {"name": "Alice", "age": 30}

    result = _UndefinedParameterAction.handle_to_dict(obj, kvs)

    assert result == {"name": "Alice", "age": 30}
    assert result is kvs

# Generated at 2026-10-24 23:23:33.460582
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    @dataclasses.dataclass
    class Example:
        name: str
        extra: CatchAll = dataclasses.field(default_factory=dict)

    obj = Example(name="example", extra={"unknown": 42})
    values = {
        "name": "example",
        "extra": {
            "unknown": 42,
            "another": "value",
        },
    }

    result = _CatchAllUndefinedParameters.handle_to_dict(obj, values)

    assert result is values
    assert result == {
        "name": "example",
        "unknown": 42,
        "another": "value",
    }
    assert "extra" not in result

# Generated at 2026-10-24 23:23:35.882885
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 23:23:38.301525
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 23:23:40.823629
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 23:23:43.238698
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:23:45.656616
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:23:48.075859
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:23:50.493313
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 23:23:52.911651
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 23:23:55.329565
# Unit test for method create_init of class _UndefinedParameterAction