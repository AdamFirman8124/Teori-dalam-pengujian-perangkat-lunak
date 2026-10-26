

# Generated at 2026-10-25 10:56:11.473549
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    from dataclasses import dataclass, field
    from typing import Optional

    @dataclasses.dataclass
    class Example:
        defined: int
        extra: CatchAll = None

    obj = Example(defined=1, extra={"a": 1, "b": 2})

    # Case 1: catch-all value is a dict -> merged into kvs, key removed
    kvs = {"defined": 1, "extra": {"a": 1, "b": 2}}
    result = _CatchAllUndefinedParameters.handle_to_dict(obj, kvs)
    assert result == {"defined": 1, "a": 1, "b": 2}, result

    # Case 2: catch-all value is not a dict -> key removed, nothing merged
    kvs = {"defined": 1, "extra": None}
    result = _CatchAllUndefinedParameters.handle_to_dict(obj, kvs)
    assert result == {"defined": 1}, result

    # Case 3: catch-all value is an empty dict -> key removed, kvs unchanged
    kvs = {"defined": 1, "extra": {}}
    result = _CatchAllUndefinedParameters.handle_to_dict(obj, kvs)
    assert result == {"defined": 1}, result

    # Case 4: original kvs dict is mutated in place (pop semantics)
    kvs = {"defined": 1, "extra": {"x": 9}}
    _CatchAllUndefinedParameters.handle_to_dict(obj, kvs)
    assert "extra" not in kvs
    assert kvs == {"defined": 1, "x": 9}


test__CatchAllUndefinedParameters_handle_to_dict()
print("All handle_to_dict tests passed")

# Generated at 2026-10-25 10:56:29.862440
# Unit test for constructor of class _UndefinedParameterAction
def test__UndefinedParameterAction():
    # Abstract class: cannot be instantiated directly
    with pytest.raises(TypeError, match="abstract"):
        _UndefinedParameterAction()

    # Subclass without handle_from_dict: also cannot be instantiated
    class Incomplete(_UndefinedParameterAction):
        pass

    with pytest.raises(TypeError, match="abstract"):
        Incomplete()

    # Subclass implementing handle_from_dict: instantiation works
    class Concrete(_UndefinedParameterAction):
        @staticmethod
        def handle_from_dict(cls, kvs):
            return dict(kvs)

    obj = Concrete()

    assert isinstance(obj, _UndefinedParameterAction)
    assert Concrete.handle_from_dict(None, {"a": 1}) == {"a": 1}
    assert Concrete.handle_to_dict(obj, {"a": 1}) == {"a": 1}
    assert Concrete.handle_dump(obj) == {}

    class Dummy:
        pass

    dummy = Dummy()
    assert Concrete.create_init(dummy) == dummy.__init__

# Generated at 2026-10-25 10:56:43.113795
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    obj = object()

    result = _UndefinedParameterAction.handle_dump(obj)

    assert result == {}

# Generated at 2026-10-25 10:57:02.141524
# Unit test for constructor of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 10:57:04.555035
# Unit test for constructor of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 10:57:07.184251
# Unit test for constructor of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 10:57:09.603026
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-25 10:57:12.018605
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-25 10:57:21.207351
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-25 10:57:22.652647
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    # It should be a subclass of marshmallow's ValidationError
    assert issubclass(UndefinedParameterError, ValidationError)

    # Constructor must accept a message and store it
    exc = UndefinedParameterError("Received undefined initialization arguments {'foo': 1}")
    assert str(exc) == "Received undefined initialization arguments {'foo': 1}"

    # Constructor must work with no arguments
    exc_default = UndefinedParameterError()
    assert str(exc_default) == ""

    # Must be raisable and catchable as itself
    try:
        raise UndefinedParameterError("bad param")
    except UndefinedParameterError as e:
        assert "bad param" in str(e)

    # Must also be catchable as a ValidationError (parent class)
    try:
        raise UndefinedParameterError("bad param")
    except ValidationError as e:
        assert "bad param" in str(e)

# Generated at 2026-10-25 10:57:35.542961
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    obj = object()

    result = _UndefinedParameterAction.handle_dump(obj)

    assert result == {}

# Generated at 2026-10-25 10:57:36.977151
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():import dataclasses

import pytest

from dataclasses_json.undefined import _UndefinedParameterAction


@dataclasses.dataclass
class Sample:
    a: int
    b: int = 0


class DummyAction(_UndefinedParameterAction):
    @staticmethod
    def module_0.handle_from_dict(cls, kvs):
        known, _ = _UndefinedParameterAction._separate_defined_undefined_kvs(
            cls=cls, kvs=kvs
        )
        return known


def test_cannot_instantiate_abstract_base():
    with pytest.raises(TypeError, match="abstract"):
        _UndefinedParameterAction()


def test_subclass_without_handle_from_dict_cannot_instantiate():
    class Incomplete(_UndefinedParameterAction):
        pass

    with pytest.raises(TypeError, match="abstract"):
        Incomplete()


@pytest.mark.parametrize(
    "kvs,expected",
    [
        ({"a": 1, "b": 2}, {"a": 1, "b": 2}),
        ({"a": 1}, {"a": 1}),
        ({"a": 1, "extra": 9, "other": "x"}, {"a": 1}),
        ({"extra": 9}, {}),
        ({}, {}),
    ],
)
def test_handle_from_dict_returns_only_known_parameters(kvs, expected):
    assert DummyAction.handle_from_dict(Sample, kvs) == expected


def test_handle_from_dict_does_not_mutate_input():
    kvs = {"a": 1, "extra": 9}

    DummyAction.handle_from_dict(Sample, kvs)

    assert kvs == {"a": 1, "extra": 9}

# Generated at 2026-10-25 10:57:38.455921
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    from dataclasses import dataclass, field
    from typing import Optional

    @dataclasses.dataclass
    class Example:
        defined: int
        extra: CatchAll = None

    obj = Example(defined=1, extra={"a": 1, "b": 2})

    # Case 1: catch-all value is a dict -> merged into kvs, key removed
    kvs = {"defined": 1, "extra": {"a": 1, "b": 2}}
    result = _CatchAllUndefinedParameters.handle_to_dict(obj, kvs)
    assert result == {"defined": 1, "a": 1, "b": 2}, result

    # Case 2: catch-all value is not a dict -> key removed, nothing merged
    kvs = {"defined": 1, "extra": None}
    result = _CatchAllUndefinedParameters.handle_to_dict(obj, kvs)
    assert result == {"defined": 1}, result

    # Case 3: catch-all value is an empty dict -> key removed, kvs unchanged
    kvs = {"defined": 1, "extra": {}}
    result = _CatchAllUndefinedParameters.handle_to_dict(obj, kvs)
    assert result == {"defined": 1}, result

    # Case 4: original kvs dict is mutated in place (pop semantics)
    kvs = {"defined": 1, "extra": {"x": 9}}
    _CatchAllUndefinedParameters.handle_to_dict(obj, kvs)
    assert "extra" not in kvs
    assert kvs == {"defined": 1, "x": 9}


test__CatchAllUndefinedParameters_handle_to_dict()
print("All handle_to_dict tests passed")

# Generated at 2026-10-25 10:57:52.644639
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    obj = object()

    result = _UndefinedParameterAction.handle_dump(obj)

    assert result == {}

# Generated at 2026-10-25 10:57:55.136711
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 10:57:57.517945
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 10:58:00.531774
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 10:58:02.951177
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 10:58:05.364785
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 10:58:07.948385
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 10:58:10.363971
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 10:58:12.777148
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 10:58:15.190726
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 10:58:17.609315
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-25 10:58:20.025873
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-25 10:58:22.438392
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-25 10:58:43.742440
# Unit test for method handle_from_dict of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_handle_from_dict():
    @dataclasses.dataclass
    class ExampleClass:
        known_field: str
        another_known_field: int = 0

    # Undefined parameters should be silently dropped
    kvs = {
        "known_field": "value",
        "another_known_field": 42,
        "undefined_param": "some_value",
        "another_undefined": 123,
    }

    result = _IgnoreUndefinedParameters.handle_from_dict(ExampleClass, kvs)

    assert result == {
        "known_field": "value",
        "another_known_field": 42,
    }
    assert "undefined_param" not in result
    assert "another_undefined" not in result

    # Only known parameters should pass through unchanged
    kvs_known_only = {"known_field": "value", "another_known_field": 7}
    result_known_only = _IgnoreUndefinedParameters.handle_from_dict(
        ExampleClass, kvs_known_only)
    assert result_known_only == kvs_known_only

    # Only undefined parameters should result in an empty dict
    kvs_unknown_only = {"undefined_param": "some_value"}
    result_unknown_only = _IgnoreUndefinedParameters.handle_from_dict(
        ExampleClass, kvs_unknown_only)
    assert result_unknown_only == {}

    # Empty input should result in an empty dict
    assert _IgnoreUndefinedParameters.handle_from_dict(ExampleClass, {}) == {}

# Generated at 2026-10-25 10:58:45.082672
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    # 1. All parameters defined -> returned as-is
    result = _RaiseUndefinedParameters.handle_from_dict(
        cls=_Example, kvs={"a": 1, "b": "x"})
    assert result == {"a": 1, "b": "x"}

    # 2. Unknown parameter -> raises UndefinedParameterError
    with pytest.raises(UndefinedParameterError) as exc_info:
        _RaiseUndefinedParameters.handle_from_dict(
            cls=_Example, kvs={"a": 1, "unknown_param": 2})
    assert "unknown_param" in str(exc_info.value)

    # 3. Only defined subset is fine (missing optional field uses default)
    result = _RaiseUndefinedParameters.handle_from_dict(
        cls=_Example, kvs={"a": 5})
    assert result == {"a": 5}

# Generated at 2026-10-25 10:58:46.474065
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

# Generated at 2026-10-25 10:58:47.881915
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

# Generated at 2026-10-25 10:58:50.412827
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 10:58:52.956967
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 10:58:55.370496
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 10:58:57.788189
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 10:59:00.204931
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 10:59:02.621917
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 10:59:05.034350
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 10:59:07.476571
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 10:59:09.879666
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 10:59:12.296023
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 10:59:14.712070
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 10:59:17.137840
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 10:59:19.545692
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 10:59:21.959853
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 10:59:24.380525
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 10:59:25.972608
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    # base implementation is a pass-through: returns kvs unchanged
    obj = object()
    kvs = {"a": 1, "b": 2, "c": None}

    result = _UndefinedParameterAction.handle_to_dict(obj, kvs)

    assert result == {"a": 1, "b": 2, "c": None}
    assert result is kvs  # same object, not a copy


def test__UndefinedParameterAction_handle_to_dict_empty():
    obj = object()
    kvs = {}

    result = _UndefinedParameterAction.handle_to_dict(obj, kvs)

    assert result == {}
    assert result is kvs

# Generated at 2026-10-25 10:59:31.668772
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    # It should be a subclass of marshmallow's ValidationError
    assert issubclass(UndefinedParameterError, ValidationError)

    # Constructor must accept a message and store it
    exc = UndefinedParameterError("Received undefined initialization arguments {'foo': 1}")
    assert str(exc) == "Received undefined initialization arguments {'foo': 1}"

    # Constructor must work with no arguments
    exc_default = UndefinedParameterError()
    assert str(exc_default) == ""

    # Must be raisable and catchable as itself
    try:
        raise UndefinedParameterError("bad param")
    except UndefinedParameterError as e:
        assert "bad param" in str(e)

    # Must also be catchable as a ValidationError (parent class)
    try:
        raise UndefinedParameterError("bad param")
    except ValidationError as e:
        assert "bad param" in str(e)

# Generated at 2026-10-25 10:59:33.131478
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    # --- Fixtures -----------------------------------------------------------
    @dataclasses.dataclass
    class Person:
        name: str
        age: int
        extra: CatchAll = None

    @dataclasses.dataclass
    class WithFactory:
        name: str
        extra: CatchAll = dataclasses.field(default_factory=dict)

    @dataclasses.dataclass
    class NoCatchAll:
        name: str


# Generated at 2026-10-25 10:59:50.919272
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 10:59:53.335683
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 10:59:55.752472
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 10:59:58.167283
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 11:00:00.583469
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 11:00:02.996930
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 11:00:05.411595
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:00:07.826040
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:00:10.240690
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:00:12.656753
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-25 11:00:15.071862
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-25 11:00:17.485316
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-25 11:00:20.187426
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:00:23.585473
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:00:26.005878
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:00:28.427794
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-25 11:00:30.835756
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-25 11:00:33.253982
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-25 11:00:35.668715
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-25 11:00:38.084441
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-25 11:00:40.500257
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-25 11:00:42.917836
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-25 11:00:45.360079
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-25 11:00:47.746156
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-25 11:00:50.159106
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:00:52.578623
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:00:54.997262
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:00:57.411465
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:00:59.920268
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:01:02.317384
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:01:04.731134
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 11:01:07.146341
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 11:01:09.561483
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 11:01:11.975726
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 11:01:14.390739
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 11:01:16.804765
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 11:01:19.217514
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:01:21.636274
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:01:24.051791
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:01:26.464109
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 11:01:28.955150
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 11:01:31.369787
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 11:01:33.782796
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:01:36.196072
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:01:38.609481
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:01:41.021439
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:01:43.434773
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:01:45.848643
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:01:48.262405
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-25 11:01:50.676295
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-25 11:01:53.098762
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-25 11:01:55.508253
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-25 11:01:57.922979
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-25 11:02:00.336980
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-25 11:02:02.752356
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-25 11:02:05.166480
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-25 11:02:07.581947
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-25 11:02:10.508367
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-25 11:02:12.924627
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-25 11:02:15.338617
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-25 11:02:17.754579
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 11:02:20.171747
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 11:02:22.584015
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 11:02:24.998466
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:02:27.412714
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:02:29.829525
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:02:32.247284
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:02:34.661602
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:02:37.075474
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:02:39.490931
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 11:02:41.905460
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 11:02:44.322761
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 11:02:46.739860
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:02:49.152981
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:02:51.567419
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:02:53.982931
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-25 11:02:56.397454
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-25 11:02:58.814882
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-25 11:03:01.231925
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 11:03:03.644715
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 11:03:06.057761
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 11:03:08.473230
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:03:10.887310
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:03:13.304813
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:03:15.719811
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 11:03:18.133202
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 11:03:20.547690
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 11:03:25.909793
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-25 11:03:28.323591
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-25 11:03:30.737472
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-25 11:03:33.152930
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:03:35.569301
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:03:37.982806
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:03:40.398348
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-25 11:03:42.812371
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-25 11:03:45.226889
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-25 11:03:47.641108
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:03:50.055888
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:03:52.469599
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:03:54.884430
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 11:03:57.298098
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 11:03:59.713300
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 11:04:02.127116
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:04:04.541557
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:04:06.956276
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:04:09.370684
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 11:04:11.785517
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 11:04:14.199228
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 11:04:16.614378
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 11:04:19.028928
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 11:04:21.443604
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 11:04:23.859103
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-25 11:04:26.272771
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-25 11:04:28.686936
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-25 11:04:31.212431
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 11:04:33.534890
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 11:04:35.950744
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 11:05:12.352580
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    @dataclass
    class Example:
        x: int = 1

    # 1. Returns {} for any obj, including None / instance / class
    for obj in (None, object(), Example(), Example, "x", 42):
        result = _UndefinedParameterAction.handle_dump(obj)
        assert result == {}
        assert type(result) is dict

    # 2. Returns a new dict each call â mutation does not leak
    first = _UndefinedParameterAction.handle_dump(None)
    first["polluted"] = 1
    assert _UndefinedParameterAction.handle_dump(None) == {}

    # 3. Subclasses without an override inherit the same behavior
    assert _RaiseUndefinedParameters.handle_dump(Example()) == {}
    assert _IgnoreUndefinedParameters.handle_dump(Example()) == {}

# Generated at 2026-10-25 11:05:15.227023
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

# Generated at 2026-10-25 11:05:16.730603
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    # 1. All parameters defined -> returned as-is
    result = _RaiseUndefinedParameters.handle_from_dict(
        cls=_Example, kvs={"a": 1, "b": "x"})
    assert result == {"a": 1, "b": "x"}

    # 2. Unknown parameter -> raises UndefinedParameterError
    with pytest.raises(UndefinedParameterError) as exc_info:
        _RaiseUndefinedParameters.handle_from_dict(
            cls=_Example, kvs={"a": 1, "unknown_param": 2})
    assert "unknown_param" in str(exc_info.value)

    # 3. Only defined subset is fine (missing optional field uses default)
    result = _RaiseUndefinedParameters.handle_from_dict(
        cls=_Example, kvs={"a": 5})
    assert result == {"a": 5}

# Generated at 2026-10-25 11:05:19.522495
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:05:21.937861
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:05:24.625609
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:05:27.040757
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 11:05:29.455677
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 11:05:31.868580
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 11:05:34.438929
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 11:05:36.854708
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 11:05:39.270592
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 11:05:41.684762
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:05:44.098863
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:05:46.513353
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:05:48.927822
# Unit test for method handle_from_dict of class _UndefinedParameterAction