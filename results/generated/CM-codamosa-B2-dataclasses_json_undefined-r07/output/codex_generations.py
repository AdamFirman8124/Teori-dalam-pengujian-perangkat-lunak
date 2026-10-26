

# Generated at 2026-10-25 09:03:18.615254
# Unit test for method handle_from_dict of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_handle_from_dict():
    from dataclasses import dataclass

    @dataclass
    class Sample:
        name: str
        age: int

    # 1. only known parameters -> returned unchanged
    kvs = {"name": "Alice", "age": 30}
    assert _IgnoreUndefinedParameters.handle_from_dict(Sample, kvs) == kvs

    # 2. mix of known + unknown -> unknown are excluded
    assert _IgnoreUndefinedParameters.handle_from_dict(
        Sample,
        {"name": "Alice", "age": 30, "extra": "ignored", "other": 123}
    ) == {"name": "Alice", "age": 30}

    # 3. only unknown parameters -> empty dict
    assert _IgnoreUndefinedParameters.handle_from_dict(
        Sample, {"foo": 1, "bar": 2}
    ) == {}

    # 4. empty input -> empty output
    assert _IgnoreUndefinedParameters.handle_from_dict(Sample, {}) == {}

    # 5. partial known parameters -> returned as-is, no error
    assert _IgnoreUndefinedParameters.handle_from_dict(
        Sample, {"name": "Bob", "unknown": "x"}
    ) == {"name": "Bob"}

    # 6. values preserved, input not mutated
    @dataclass
    class Complex:
        a: int
        b: str = "default"

    input_kvs = {"a": 1, "b": None, "c": [1, 2], "d": {"k": "v"}}
    result = _IgnoreUndefinedParameters.handle_from_dict(Complex, input_kvs)
    assert result == {"a": 1, "b": None}
    assert input_kvs == {"a": 1, "b": None, "c": [1, 2], "d": {"k": "v"}}

# Generated at 2026-10-25 09:03:36.008492
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    obj = object()

    result = _UndefinedParameterAction.handle_dump(obj)

    assert result == {}

# Generated at 2026-10-25 09:03:38.446396
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 09:03:40.863106
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 09:03:43.277339
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 09:03:56.291447
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    class Sample:
        def __init__(self, val):
            self.val = val
    result = _UndefinedParameterAction.create_init(Sample)
    assert result is Sample.__init__
    assert callable(result)
    inst = Sample.__new__(Sample)
    result(inst, 123)
    assert inst.val == 123
    class Plain:
        pass
    assert _UndefinedParameterAction.create_init(Plain) is Plain.__init__
    assert not hasattr(_UndefinedParameterAction.create_init(Sample), "__wrapped__")

# Generated at 2026-10-25 09:04:22.987525
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 09:04:25.412338
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 09:04:27.830836
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 09:04:30.282624
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 09:04:32.699648
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 09:04:35.318540
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 09:04:37.735250
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-25 09:04:40.151328
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-25 09:04:42.567334
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-25 09:04:44.984941
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 09:04:47.405444
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 09:04:49.821720
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 09:04:52.237378
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 09:04:54.655707
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 09:04:57.076077
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 09:04:59.493523
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-25 09:05:01.908920
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-25 09:05:04.325870
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-25 09:05:06.744573
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 09:05:09.162864
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 09:05:11.579422
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 09:05:13.994988
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-25 09:05:16.412499
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-25 09:05:18.831464
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-25 09:05:21.247922
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 09:05:23.664383
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 09:05:26.080228
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 09:05:28.496119
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 09:05:30.918583
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 09:05:33.339935
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 09:05:35.756824
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 09:05:38.174944
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 09:05:40.593867
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 09:05:43.009617
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 09:05:45.426026
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 09:05:47.843956
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 09:05:50.262158
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-25 09:05:52.680015
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-25 09:05:55.095557
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-25 09:05:57.511415
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 09:05:59.931341
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 09:06:02.346676
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 09:06:04.765655
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-25 09:06:07.269492
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-25 09:06:09.686940
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-25 09:06:12.102231
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 09:06:14.520867
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 09:06:16.937329
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 09:06:19.354024
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 09:06:21.773424
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 09:06:24.188700
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 09:06:26.606582
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 09:06:29.021743
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 09:06:31.439395
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 09:06:33.856705
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-25 09:06:36.273322
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-25 09:06:38.694986
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-25 09:06:41.107596
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 09:06:43.527568
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 09:06:45.947249
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 09:06:48.363694
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 09:06:50.783167
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 09:06:53.201458
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 09:06:56.573979
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 09:06:58.994323
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 09:07:01.411928
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 09:07:03.828279
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 09:07:06.296647
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 09:07:08.809350
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 09:07:11.206547
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 09:07:13.622532
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 09:07:16.039391
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 09:07:18.569099
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 09:07:20.918885
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 09:07:23.385073
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 09:07:25.800854
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-25 09:07:28.218327
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-25 09:07:30.638495
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-25 09:07:33.054988
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 09:07:35.474863
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 09:07:37.892396
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 09:07:40.307612
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-25 09:07:42.797161
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-25 09:07:56.003454
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-25 09:08:17.207180
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


# Generated at 2026-10-25 09:08:26.931024
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

# Generated at 2026-10-25 09:08:29.465616
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 09:08:31.886205
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 09:08:34.510388
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 09:08:36.928793
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 09:08:39.346624
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 09:08:41.760274
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 09:08:44.180497
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-25 09:08:46.599352
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-25 09:08:49.016354
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-25 09:08:51.434074
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 09:08:53.870846
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 09:08:56.284116
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 09:08:58.709134
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 09:09:01.119421
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 09:09:03.536259
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 09:09:05.954991
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 09:09:08.370881
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 09:09:10.787794
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 09:09:13.204639
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 09:09:30.832453
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 09:10:01.343686
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 09:10:17.167211
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

# Generated at 2026-10-25 09:10:18.649297
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

# Generated at 2026-10-25 09:10:46.168993
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    @dataclass
    class Sample:
        name: str
        age: int

    # 1. all keys known -> returned as-is
    kvs = {"name": "Alice", "age": 30}
    result = _RaiseUndefinedParameters.handle_from_dict(Sample, kvs)
    assert result == {"name": "Alice", "age": 30}

    # 2. empty input -> empty output, no error
    assert _RaiseUndefinedParameters.handle_from_dict(Sample, {}) == {}

    # 3. subset of known fields -> returned, no error
    assert _RaiseUndefinedParameters.handle_from_dict(
        Sample, {"name": "Bob"}) == {"name": "Bob"}

    # 4. only unknown keys -> raises
    with pytest.raises(UndefinedParameterError):
        _RaiseUndefinedParameters.handle_from_dict(
            Sample, {"unknown": 123})

    # 5. mix of known + unknown -> raises, does not return known part
    with pytest.raises(UndefinedParameterError) as exc_info:
        _RaiseUndefinedParameters.handle_from_dict(
            Sample, {"name": "Alice", "age": 30, "extra": "boom"})
    assert "extra" in str(exc_info.value)
    assert "boom" in str(exc_info.value)

    # 6. it is a ValidationError (marshmallow) subclass
    with pytest.raises(ValidationError):
        _RaiseUndefinedParameters.handle_from_dict(Sample, {"bad": True})

    # 7. input dict is not mutated
    original = {"name": "Alice", "age": 30}
    _RaiseUndefinedParameters.handle_from_dict(Sample, original)
    assert original == {"name": "Alice", "age": 30}

# Generated at 2026-10-25 09:10:55.106825
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

# Generated at 2026-10-25 09:11:01.758227
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

# Generated at 2026-10-25 09:11:49.768602
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    # base implementation always returns empty dict, regardless of obj
    for obj in [object(), None, "string", 123, {"a": 1}]:
        result = _UndefinedParameterAction.handle_dump(obj)
        assert result == {}
        assert isinstance(result, dict)

    # each call returns a new dict instance
    assert _UndefinedParameterAction.handle_dump(object()) is not \
           _UndefinedParameterAction.handle_dump(object())

    # subclasses that don't override must inherit same behaviour
    assert _RaiseUndefinedParameters.handle_dump(object()) == {}
    assert _IgnoreUndefinedParameters.handle_dump(object()) == {}

# Generated at 2026-10-25 09:11:51.141953
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

# Generated at 2026-10-25 09:11:53.760178
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-25 09:11:56.440048
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-25 09:12:02.277931
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-25 09:12:03.813369
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

# Generated at 2026-10-25 09:12:05.247608
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

# Generated at 2026-10-25 09:12:12.005256
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

# Generated at 2026-10-25 09:12:32.653878
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 09:12:35.064057
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 09:12:37.487330
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 09:12:39.901733
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 09:12:42.318583
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 09:12:44.735808
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 09:12:47.153406
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 09:12:49.734264
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 09:12:52.149561
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 09:12:56.166394
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-25 09:12:58.583335
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-25 09:13:01.000168
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-25 09:13:03.419274
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-25 09:13:05.834675
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-25 09:13:08.251584
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-25 09:13:10.745782
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 09:13:13.162978
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 09:13:15.579758
# Unit test for method handle_from_dict of class _UndefinedParameterAction