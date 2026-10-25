

# Generated at 2026-10-24 23:28:37.585703
# Unit test for method handle_from_dict of class _IgnoreUndefinedParameters

# Generated at 2026-10-24 23:28:40.184300
# Unit test for method handle_from_dict of class _IgnoreUndefinedParameters

# Generated at 2026-10-24 23:28:42.600457
# Unit test for method handle_from_dict of class _IgnoreUndefinedParameters

# Generated at 2026-10-24 23:28:45.019988
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 23:28:47.438286
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 23:28:49.852754
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 23:28:52.271307
# Unit test for method handle_from_dict of class _IgnoreUndefinedParameters

# Generated at 2026-10-24 23:28:54.689042
# Unit test for method handle_from_dict of class _IgnoreUndefinedParameters

# Generated at 2026-10-24 23:28:57.110009
# Unit test for method handle_from_dict of class _IgnoreUndefinedParameters

# Generated at 2026-10-24 23:28:59.528370
# Unit test for constructor of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:29:01.945133
# Unit test for constructor of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:29:04.363439
# Unit test for constructor of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:29:10.150303
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():obj = object()

# Generated at 2026-10-24 23:29:19.161699
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    @dataclasses.dataclass
    class Example:
        name: str
        extra: CatchAll = dataclasses.field(default_factory=dict)

    obj = Example(name="example", extra={"unknown_a": 1, "unknown_b": 2})
    values = {
        "name": obj.name,
        "extra": obj.extra,
    }

    result = _CatchAllUndefinedParameters.handle_to_dict(obj, values)

    assert result == {
        "name": "example",
        "unknown_a": 1,
        "unknown_b": 2,
    }
    assert "extra" not in result
    assert result is values  # The method mutates and returns the input dict.

# Generated at 2026-10-24 23:29:28.175653
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    assert getattr(
        _UndefinedParameterAction.handle_from_dict,
        "__isabstractmethod__",
        False,
    )

    with pytest.raises(TypeError, match=r"abstract method handle_from_dict"):
        _UndefinedParameterAction()

# Generated at 2026-10-24 23:29:29.508682
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

# Generated at 2026-10-24 23:29:30.855055
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

# Generated at 2026-10-24 23:29:32.185643
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

# Generated at 2026-10-24 23:29:40.973203
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    assert (
        _UndefinedParameterAction.handle_from_dict.__isabstractmethod__
        is True
    )
    assert "handle_from_dict" in _UndefinedParameterAction.__abstractmethods__

    with pytest.raises(TypeError, match="abstract method handle_from_dict"):
        _UndefinedParameterAction()

# Generated at 2026-10-24 23:29:42.422892
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

# Generated at 2026-10-24 23:29:47.323358
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    obj = object()
    kvs = {"name": "Alice", "age": 30}

    result = _UndefinedParameterAction.handle_to_dict(obj, kvs)

    assert result == {"name": "Alice", "age": 30}
    assert result is kvs

# Generated at 2026-10-24 23:29:49.740182
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 23:29:52.403408
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 23:29:54.820306
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 23:29:57.239981
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:29:59.659551
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:30:02.249374
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:30:04.669308
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 23:30:07.086288
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 23:30:09.506517
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 23:30:11.923375
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:30:14.339925
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:30:16.755949
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:30:19.178600
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 23:30:21.591712
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 23:30:24.012137
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 23:30:26.428454
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 23:30:28.842425
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 23:30:31.261209
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 23:30:33.681828
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-24 23:30:36.101379
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-24 23:30:38.516668
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-24 23:30:40.934208
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:30:43.351806
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:30:45.769599
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:30:48.186673
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:30:50.601603
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:30:53.020246
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:30:55.436877
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:30:57.853647
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:31:00.271516
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:31:02.684718
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 23:31:25.427009
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():message = "Received undefined initialization arguments {'x': 1}"

# Generated at 2026-10-24 23:31:26.824767
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

# Generated at 2026-10-24 23:31:33.818188
# Unit test for method handle_dump of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_dump():
    from dataclasses import dataclass, field
    from typing import Optional

    @dataclass
    class Example:
        defined_param: str
        undefined: Optional[CatchAllVar] = field(default_factory=dict)

    # Create instance with undefined parameters caught in catch-all field
    instance = Example.from_dict(
        {"defined_param": "value", "extra1": 1, "extra2": "two"},
        undefined_parameters=Undefined.INCLUDE
    )

    result = _CatchAllUndefinedParameters.handle_dump(instance)

    assert result == {"extra1": 1, "extra2": "two"}, \
        f"Expected {{'extra1': 1, 'extra2': 'two'}}, got {result}"

    # Empty catch-all when no undefined parameters were given
    instance_no_extras = Example.from_dict(
        {"defined_param": "value"},
        undefined_parameters=Undefined.INCLUDE
    )
    result_empty = _CatchAllUndefinedParameters.handle_dump(instance_no_extras)
    assert result_empty == {}, \
        f"Expected empty dict, got {result_empty}"

# Generated at 2026-10-24 23:31:42.114984
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    # The method defines an abstract interface and the base class must not be
    # instantiated directly.
    assert (
        _UndefinedParameterAction.handle_from_dict.__isabstractmethod__
        is True
    )
    assert "handle_from_dict" in _UndefinedParameterAction.__abstractmethods__

    with pytest.raises(TypeError):
        _UndefinedParameterAction()

# Generated at 2026-10-24 23:31:54.196443
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:31:56.618222
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:31:59.033602
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:32:01.450642
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 23:32:04.030735
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 23:32:06.450434
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 23:32:08.865276
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:32:11.280080
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:32:13.698674
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:32:16.114226
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:32:18.531709
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:32:27.800104
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():import dataclasses

# Generated at 2026-10-24 23:32:33.300150
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    obj = object()

    result = _UndefinedParameterAction.handle_dump(obj)

    assert result == {}

# Generated at 2026-10-24 23:32:49.595365
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    @dataclasses.dataclass
    class Example:
        identifier: int
        name: str
        extra: CatchAll = None

    wrapped_init = _CatchAllUndefinedParameters.create_init(Example)

    # Unknown keyword and surplus positional arguments are captured.
    instance = object.__new__(Example)
    wrapped_init(
        instance,
        1,
        "example",
        "surplus positional argument",
        unknown_key="unknown value",
    )

    assert instance.identifier == 1
    assert instance.name == "example"
    assert instance.extra == {
        "_UNKNOWN0": "surplus positional argument",
        "unknown_key": "unknown value",
    }

    # Unknown arguments are merged into an explicitly supplied catch-all dict.
    instance_with_existing_extra = object.__new__(Example)
    wrapped_init(
        instance_with_existing_extra,
        2,
        "another example",
        extra={"existing": "value"},
        another_unknown=42,
    )

    assert instance_with_existing_extra.identifier == 2
    assert instance_with_existing_extra.name == "another example"
    assert instance_with_existing_extra.extra == {
        "existing": "value",
        "another_unknown": 42,
    }

# Generated at 2026-10-24 23:33:06.683183
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:33:12.432729
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:33:14.960519
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:33:29.463272
# Unit test for method handle_dump of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:33:35.224507
# Unit test for method handle_dump of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_dump():TestClass = dataclasses.make_dataclass(
        "TestClass",
        [("extras", Optional[CatchAllVar], dataclasses.field(default_factory=dict))]
    )

# Generated at 2026-10-24 23:33:40.286740
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    obj = object()
    kvs = {"name": "Alice", "age": 30}

    result = _UndefinedParameterAction.handle_to_dict(obj, kvs)

    assert result is kvs
    assert result == {"name": "Alice", "age": 30}

# Generated at 2026-10-24 23:33:41.617842
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

# Generated at 2026-10-24 23:33:53.902532
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:33:59.943555
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:34:02.363669
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:34:04.883539
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 23:34:07.300246
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 23:34:09.716268
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 23:34:12.133549
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:34:14.549004
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:34:16.965015
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:34:19.381179
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 23:34:21.800341
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 23:34:35.066727
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():from dataclasses_json.undefined import _UndefinedParameterAction


# Generated at 2026-10-24 23:34:36.405264
# Unit test for method handle_dump of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_dump():
    from dataclasses import dataclass, field
    from typing import Optional

    @dataclass
    class Example:
        defined_param: str
        undefined: Optional[CatchAllVar] = field(default_factory=dict)

    # Create instance with undefined parameters caught in catch-all field
    instance = Example.from_dict(
        {"defined_param": "value", "extra1": 1, "extra2": "two"},
        undefined_parameters=Undefined.INCLUDE
    )

    result = _CatchAllUndefinedParameters.handle_dump(instance)

    assert result == {"extra1": 1, "extra2": "two"}, \
        f"Expected {{'extra1': 1, 'extra2': 'two'}}, got {result}"

    # Empty catch-all when no undefined parameters were given
    instance_no_extras = Example.from_dict(
        {"defined_param": "value"},
        undefined_parameters=Undefined.INCLUDE
    )
    result_empty = _CatchAllUndefinedParameters.handle_dump(instance_no_extras)
    assert result_empty == {}, \
        f"Expected empty dict, got {result_empty}"

# Generated at 2026-10-24 23:34:46.638136
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    @dataclasses.dataclass
    class Example:
        name: str
        extra: CatchAll = dataclasses.field(default_factory=dict)

    obj = Example(name="example", extra={"unknown": 42})
    kvs = {
        "name": "example",
        "extra": {
            "unknown": 42,
            "another_unknown": "value",
        },
    }

    result = _CatchAllUndefinedParameters.handle_to_dict(obj, kvs)

    assert result is kvs
    assert result == {
        "name": "example",
        "unknown": 42,
        "another_unknown": "value",
    }
    assert "extra" not in result

# Generated at 2026-10-24 23:34:47.968078
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

# Generated at 2026-10-24 23:34:57.804825
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    @dataclasses.dataclass
    class Example:
        required: int
        optional: str = "default"

    wrapped_init = _IgnoreUndefinedParameters.create_init(Example)

    # Unknown keyword arguments and excess positional arguments are ignored.
    instance = Example.__new__(Example)
    wrapped_init(
        instance,
        10,
        "provided",
        "extra positional",
        unknown_keyword="ignored",
    )

    assert instance.required == 10
    assert instance.optional == "provided"
    assert not hasattr(instance, "unknown_keyword")

    # Dataclass defaults are still applied.
    instance_with_defaults = Example.__new__(Example)
    wrapped_init(
        instance_with_defaults,
        required=20,
        another_unknown="ignored",
    )

    assert instance_with_defaults.required == 20
    assert instance_with_defaults.optional == "default"

# Generated at 2026-10-24 23:35:00.220260
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:35:02.634887
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:35:05.051386
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:35:07.468434
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:35:09.883936
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:35:12.301447
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:35:14.885249
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:35:17.307944
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:35:19.725465
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:35:22.144008
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 23:35:24.567233
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 23:35:26.980663
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 23:35:29.396538
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 23:35:31.815919
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 23:35:34.245419
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 23:35:36.665793
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 23:35:39.082866
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 23:35:41.499514
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 23:35:43.924745
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 23:35:46.343413
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 23:35:48.759322
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 23:35:51.179519
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 23:35:53.597527
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 23:35:56.011293
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 23:35:58.431395
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:36:00.844928
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:36:03.262792
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:36:05.680522
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 23:36:08.096515
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 23:36:10.523514
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 23:36:12.937075
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 23:36:15.358622
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 23:36:17.775349
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 23:36:20.190817
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 23:36:22.611631
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 23:36:25.029150
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 23:36:27.454983
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:36:29.876875
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:36:32.290056
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:36:34.706495
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 23:36:37.125621
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 23:36:39.541421
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 23:36:41.961108
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 23:36:44.377001
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 23:36:46.795189
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 23:36:49.211088
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:36:51.629886
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:36:54.047555
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:36:56.463459
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 23:36:58.880907
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 23:37:01.298031
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 23:37:03.715229
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 23:37:06.132796
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 23:37:08.549237
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 23:37:10.968352
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 23:37:13.382404
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 23:37:15.796430
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 23:37:18.212989
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 23:37:20.626867
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 23:37:23.047572
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 23:37:25.637874
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 23:37:28.055413
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 23:37:30.471078
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 23:37:32.894572
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 23:37:35.312793
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 23:37:37.727197
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 23:37:40.146611
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-24 23:37:42.562330
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-24 23:37:44.978437
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-24 23:37:47.395893
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:37:49.813860
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:37:52.230922
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:37:54.646741
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-24 23:37:57.066300
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-24 23:37:59.484322
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-24 23:38:01.899959
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 23:38:04.316784
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 23:38:06.733393
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 23:38:09.151423
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 23:38:11.568107
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 23:38:13.985584
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 23:38:16.401966
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 23:38:18.817838
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 23:38:21.234531
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 23:38:23.650514
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:38:26.067128
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:38:28.483494
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 23:38:30.899269
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 23:38:33.314704
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 23:38:35.732000
# Unit test for method create_init of class _UndefinedParameterAction