

# Generated at 2026-10-24 14:52:23.693101
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    # handle_to_dict is a pass-through on the base class:
    # it must return the input dict unchanged.

    obj = object()  # obj is unused by the base implementation
    kvs = {"a": 1, "b": "two", "c": None}

    result = _UndefinedParameterAction.handle_to_dict(obj, kvs)

    assert result == {"a": 1, "b": "two", "c": None}
    assert result is kvs  # base class returns the same dict, not a copy

    # Empty dict stays empty
    assert _UndefinedParameterAction.handle_to_dict(obj, {}) == {}

# Generated at 2026-10-24 14:52:25.125572
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    # 1. String message â how it's raised in undefined.py
    err = UndefinedParameterError("Received undefined initialization arguments {'x': 1}")
    assert isinstance(err, ValidationError)
    assert isinstance(err, Exception)
    assert err.messages == ["Received undefined initialization arguments {'x': 1}"]
    assert err.data is None
    assert err.valid_data is None

    # 2. Explicit constructor arguments are stored unchanged
    err = UndefinedParameterError(
        {"x": ["Invalid value."]},
        field_name="x",
        data={"x": 1},
        valid_data={},
    )
    assert err.messages == {"x": ["Invalid value."]}
    assert err.field_name == "x"
    assert err.data == {"x": 1}
    assert err.valid_data == {}

    # 3. List message is preserved
    assert UndefinedParameterError(["a", "b"]).messages == ["a", "b"]

    # 4. Raisable / catchable as both types
    with pytest.raises(UndefinedParameterError, match="bad input"):
        raise UndefinedParameterError("bad input")
    with pytest.raises(ValidationError):
        raise UndefinedParameterError("bad input")

# Generated at 2026-10-24 14:52:26.559475
# Unit test for constructor of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters():
    # Constructor: class is concrete (handle_from_dict implemented)
    # and takes no arguments.
    action = _RaiseUndefinedParameters()
    assert isinstance(action, _RaiseUndefinedParameters)
    assert isinstance(action, _UndefinedParameterAction)

    # Fixture class whose fields define "known" parameters.
    @dataclasses.dataclass
    class _Dummy:
        a: int
        b: str = "x"

    # handle_from_dict: only defined fields are passed through.
    assert _RaiseUndefinedParameters.handle_from_dict(
        _Dummy, {"a": 1, "b": "y"}) == {"a": 1, "b": "y"}

    # handle_from_dict: undefined parameters raise UndefinedParameterError.
    with pytest.raises(UndefinedParameterError) as exc_info:
        _RaiseUndefinedParameters.handle_from_dict(_Dummy, {"a": 1, "c": 2})
    assert "undefined initialization arguments" in str(exc_info.value)
    assert "c" in str(exc_info.value)

    # Empty input is valid â returns empty dict, no error.
    assert _RaiseUndefinedParameters.handle_from_dict(_Dummy, {}) == {}

# Generated at 2026-10-24 14:52:28.099654
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    @dataclass
    class Person:
        name: str
        age: int

    # 1. only known params -> returned as-is
    kvs = {"name": "Alice", "age": 30}
    assert _RaiseUndefinedParameters.handle_from_dict(Person, kvs) == kvs

    # 2. empty input -> empty output, no error
    assert _RaiseUndefinedParameters.handle_from_dict(Person, {}) == {}

    # 3. subset of known params -> returned as-is, no error
    assert _RaiseUndefinedParameters.handle_from_dict(
        Person, {"name": "Bob"}
    ) == {"name": "Bob"}

    # 4. only unknown params -> raises
    with pytest.raises(UndefinedParameterError) as exc_info:
        _RaiseUndefinedParameters.handle_from_dict(
            Person, {"unknown": 1}
        )
    assert "'unknown': 1" in str(exc_info.value)

    # 5. mix of known + unknown -> raises, does not silently drop
    with pytest.raises(UndefinedParameterError) as exc_info:
        _RaiseUndefinedParameters.handle_from_dict(
            Person, {"name": "Alice", "age": 30, "extra": "boom"}
        )
    assert "'extra': 'boom'" in str(exc_info.value)

# Generated at 2026-10-24 14:52:29.633893
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    # 1. String message â how it's raised in undefined.py
    err = UndefinedParameterError("Received undefined initialization arguments {'x': 1}")
    assert isinstance(err, ValidationError)
    assert isinstance(err, Exception)
    assert err.messages == ["Received undefined initialization arguments {'x': 1}"]
    assert err.data is None
    assert err.valid_data is None

    # 2. Explicit constructor arguments are stored unchanged
    err = UndefinedParameterError(
        {"x": ["Invalid value."]},
        field_name="x",
        data={"x": 1},
        valid_data={},
    )
    assert err.messages == {"x": ["Invalid value."]}
    assert err.field_name == "x"
    assert err.data == {"x": 1}
    assert err.valid_data == {}

    # 3. List message is preserved
    assert UndefinedParameterError(["a", "b"]).messages == ["a", "b"]

    # 4. Raisable / catchable as both types
    with pytest.raises(UndefinedParameterError, match="bad input"):
        raise UndefinedParameterError("bad input")
    with pytest.raises(ValidationError):
        raise UndefinedParameterError("bad input")

# Generated at 2026-10-24 14:52:32.213395
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:52:34.624727
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:52:37.037676
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:52:39.596343
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:52:42.011733
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:52:44.424654
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:52:46.839246
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 14:52:49.252126
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 14:52:51.666585
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 14:52:54.081493
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:52:56.496051
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:52:58.908650
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:53:01.321660
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:53:03.735061
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:53:06.146952
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:53:22.696453
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    # handle_to_dict is a pass-through on the base class:
    # it must return the input dict unchanged.

    obj = object()  # obj is unused by the base implementation
    kvs = {"a": 1, "b": "two", "c": None}

    result = _UndefinedParameterAction.handle_to_dict(obj, kvs)

    assert result == {"a": 1, "b": "two", "c": None}
    assert result is kvs  # base class returns the same dict, not a copy

    # Empty dict stays empty
    assert _UndefinedParameterAction.handle_to_dict(obj, {}) == {}

# Generated at 2026-10-24 14:53:40.372425
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:53:42.881303
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:53:45.300223
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:53:47.711059
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:53:50.123703
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:53:52.730014
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:53:55.144449
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:53:57.556684
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:53:59.977842
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:54:02.390228
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:54:04.801930
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:54:07.214884
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:54:09.627519
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 14:54:12.042123
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 14:54:25.160094
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():error = UndefinedParameterError("invalid parameter")
assert isinstance(error, ValidationError)
assert str(error) == "invalid parameter"

# Generated at 2026-10-24 14:54:26.480484
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    from dataclasses import dataclass, field

    @dataclass
    class A:
        x: int
        rest: CatchAll = field(default_factory=dict)

    A.__init__ = _CatchAllUndefinedParameters.create_init(A)

    # 1. No extra parameters -> catch-all is empty dict
    obj = A(1)
    assert obj.x == 1
    assert obj.rest == {}

    # 2. Unknown keyword parameters are collected into the catch-all field
    obj = A(1, unknown=5, other="hi")
    assert obj.x == 1
    assert obj.rest == {"unknown": 5, "other": "hi"}

    # 3. Extra positional parameters are collected under _UNKNOWN{i} keys
    obj = A(1, 2, 3)
    assert obj.x == 1
    assert obj.rest == {"_UNKNOWN0": 2, "_UNKNOWN1": 3}

    # 4. Explicitly passing the catch-all field passes through unchanged
    obj = A(1, rest={"a": 1})
    assert obj.x == 1
    assert obj.rest == {"a": 1}

    # 5. Non-dict value for the catch-all field raises UndefinedParameterError
    try:
        A(1, rest=5)
        assert False, "Expected UndefinedParameterError"
    except UndefinedParameterError:
        pass

# Generated at 2026-10-24 14:54:27.812062
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():import unittest
from dataclasses import dataclass

from dataclasses_json import CatchAll
from dataclasses_json.undefined import _CatchAllUndefinedParameters


@dataclass
class _Example:
    field_a: str
    extra_data: CatchAll = None


class TestCatchAllUndefinedParametersHandleToDict(unittest.TestCase):

    def test_merges_catch_all_dict_into_kvs(self):
        # arrange
        obj = _Example(field_a="value")
        kvs = {"field_a": "value", "extra_data": {"b": 2, "c": "three"}}

        # act
        result = _CatchAllUndefinedParameters.handle_to_dict(obj, kvs)

        # assert â catch-all contents are hoisted to top level
        self.assertEqual(result, {"field_a": "value", "b": 2, "c": "three"})

    def test_catch_all_key_is_removed(self):
        # arrange
        obj = _Example(field_a="value")
        kvs = {"field_a": "value", "extra_data": {"b": 2}}

        # act
        result = _CatchAllUndefinedParameters.handle_to_dict(obj, kvs)

        # assert â the catch-all field name itself no longer appears
        self.assertNotIn("extra_data", result)

    def test_empty_catch_all_dict(self):
        # arrange
        obj = _Example(field_a="value", extra_data={})
        kvs = {"field_a": "value", "extra_data": {}}

        # act
        result = _CatchAllUndefinedParameters.handle_to_dict(obj, kvs)

        # assert
        self.assertEqual(result, {"field_a": "value"})

    def test_non_dict_catch_all_is_dropped(self):
        # arrange
        obj = _Example(field_a="value", extra_data="not-a-dict")
        kvs = {"field_a": "value", "extra_data": "not-a-dict"}

        # act
        result = _CatchAllUndefinedParameters.handle_to_dict(obj, kvs)

        # assert â popped unconditionally, only merged if dict
        self.assertEqual(result, {"field_a": "value"})

    def test_mutates_kvs_in_place_and_returns_it(self):
        # arrange
        obj = _Example(field_a="value")
        kvs = {"field_a": "value", "extra_data": {"x": 1}}

        # act
        result = _CatchAllUndefinedParameters.handle_to_dict(obj, kvs)

        # assert â implementation pops/updates on the same dict
        self.assertIs(result, kvs)


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-10-24 14:54:29.441019
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

# Generated at 2026-10-24 14:54:30.834011
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 14:54:32.194342
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():from dataclasses import dataclass

@dataclasses.dataclass
class _Sample:
    x: int
    y: str = "default"

obj = _Sample(x=1)
result = _UndefinedParameterAction.handle_dump(obj)
assert result == {}

# Generated at 2026-10-24 14:54:48.691680
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    # handle_to_dict is a pass-through on the base class:
    # it must return the input dict unchanged.

    obj = object()  # obj is unused by the base implementation
    kvs = {"a": 1, "b": "two", "c": None}

    result = _UndefinedParameterAction.handle_to_dict(obj, kvs)

    assert result == {"a": 1, "b": "two", "c": None}
    assert result is kvs  # base class returns the same dict, not a copy

    # Empty dict stays empty
    assert _UndefinedParameterAction.handle_to_dict(obj, {}) == {}

# Generated at 2026-10-24 14:54:51.107121
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 14:54:53.523392
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 14:54:55.941234
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 14:54:58.350845
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 14:55:00.956429
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 14:55:03.369569
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 14:55:05.782290
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:55:08.195253
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:55:10.607948
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:55:13.019944
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 14:55:15.437434
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 14:55:17.845981
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 14:55:20.259130
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:55:22.833553
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():from dataclasses import dataclass

# Generated at 2026-10-24 14:55:24.217336
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    # handle_to_dict is a pass-through on the base class:
    # it must return the input dict unchanged.

    obj = object()  # obj is unused by the base implementation
    kvs = {"a": 1, "b": "two", "c": None}

    result = _UndefinedParameterAction.handle_to_dict(obj, kvs)

    assert result == {"a": 1, "b": "two", "c": None}
    assert result is kvs  # base class returns the same dict, not a copy

    # Empty dict stays empty
    assert _UndefinedParameterAction.handle_to_dict(obj, {}) == {}

# Generated at 2026-10-24 14:55:25.635708
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

# Generated at 2026-10-24 14:55:26.989709
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 14:55:28.307576
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():from dataclasses import dataclass

@dataclasses.dataclass
class _Sample:
    x: int
    y: str = "default"

obj = _Sample(x=1)
result = _UndefinedParameterAction.handle_dump(obj)
assert result == {}

# Generated at 2026-10-24 14:55:31.277251
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:55:32.724284
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():from dataclasses import dataclass

# Generated at 2026-10-24 14:55:35.554691
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    @dataclasses.dataclass
    class Example:
        a: int
        b: str = "default_b"
        c: Optional[int] = None

    original_init = Example.__init__
    try:
        Example.__init__ = _IgnoreUndefinedParameters.create_init(Example)

        # Defined keyword parameters pass through unchanged
        obj = Example(a=1, b="hello", c=2)
        assert obj.a == 1
        assert obj.b == "hello"
        assert obj.c == 2

        # Undefined keyword parameters are silently dropped
        obj = Example(a=2, undefined_param="dropped", another_undefined=42)
        assert obj.a == 2
        assert obj.b == "default_b"
        assert obj.c is None

        # Positional arguments are truncated at the number of takeable
        # parameters; extras are treated as undefined and dropped
        obj = Example(3, "positional", 5, "extra_unknown_arg")
        assert obj.a == 3
        assert obj.b == "positional"
        assert obj.c == 5

        # Defaults are applied when parameters are omitted
        obj = Example(a=4)
        assert obj.a == 4
        assert obj.b == "default_b"
        assert obj.c is None

        # Mixed positional and known keyword arguments
        obj = Example(5, c=7, unknown_kw="ignored")
        assert obj.a == 5
        assert obj.b == "default_b"
        assert obj.c == 7
    finally:
        # Restore the original __init__ so other tests are unaffected
        Example.__init__ = original_init

# Generated at 2026-10-24 14:55:36.922933
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():import unittest
from dataclasses import dataclass

from dataclasses_json import CatchAll
from dataclasses_json.undefined import _CatchAllUndefinedParameters


@dataclass
class _Example:
    field_a: str
    extra_data: CatchAll = None


class TestCatchAllUndefinedParametersHandleToDict(unittest.TestCase):

    def test_merges_catch_all_dict_into_kvs(self):
        # arrange
        obj = _Example(field_a="value")
        kvs = {"field_a": "value", "extra_data": {"b": 2, "c": "three"}}

        # act
        result = _CatchAllUndefinedParameters.handle_to_dict(obj, kvs)

        # assert â catch-all contents are hoisted to top level
        self.assertEqual(result, {"field_a": "value", "b": 2, "c": "three"})

    def test_catch_all_key_is_removed(self):
        # arrange
        obj = _Example(field_a="value")
        kvs = {"field_a": "value", "extra_data": {"b": 2}}

        # act
        result = _CatchAllUndefinedParameters.handle_to_dict(obj, kvs)

        # assert â the catch-all field name itself no longer appears
        self.assertNotIn("extra_data", result)

    def test_empty_catch_all_dict(self):
        # arrange
        obj = _Example(field_a="value", extra_data={})
        kvs = {"field_a": "value", "extra_data": {}}

        # act
        result = _CatchAllUndefinedParameters.handle_to_dict(obj, kvs)

        # assert
        self.assertEqual(result, {"field_a": "value"})

    def test_non_dict_catch_all_is_dropped(self):
        # arrange
        obj = _Example(field_a="value", extra_data="not-a-dict")
        kvs = {"field_a": "value", "extra_data": "not-a-dict"}

        # act
        result = _CatchAllUndefinedParameters.handle_to_dict(obj, kvs)

        # assert â popped unconditionally, only merged if dict
        self.assertEqual(result, {"field_a": "value"})

    def test_mutates_kvs_in_place_and_returns_it(self):
        # arrange
        obj = _Example(field_a="value")
        kvs = {"field_a": "value", "extra_data": {"x": 1}}

        # act
        result = _CatchAllUndefinedParameters.handle_to_dict(obj, kvs)

        # assert â implementation pops/updates on the same dict
        self.assertIs(result, kvs)


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-10-24 14:55:39.561642
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 14:55:41.973974
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 14:55:44.386366
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 14:55:46.799607
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 14:55:49.213526
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 14:55:51.625630
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 14:55:54.176141
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 14:55:56.593207
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 14:55:59.005198
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 14:56:01.417892
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 14:56:03.829759
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 14:56:06.243224
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 14:56:08.656962
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:56:11.070474
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:56:13.482125
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:56:15.897162
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:56:18.310348
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:56:20.723509
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:56:23.141455
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 14:56:25.557572
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 14:56:27.971155
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 14:56:30.387577
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 14:56:32.795853
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 14:56:35.210614
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 14:56:37.622266
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 14:56:40.037376
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 14:56:42.448659
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 14:56:44.862562
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 14:56:47.276210
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 14:56:49.689254
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 14:56:52.101640
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:56:54.514925
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:56:56.932458
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:56:59.341901
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 14:57:01.753643
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 14:57:04.168000
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 14:57:06.579954
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 14:57:08.992401
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 14:57:11.405960
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 14:57:14.048019
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:57:15.364799
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():from dataclasses import dataclass

# Generated at 2026-10-24 14:57:16.702318
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    from dataclasses import dataclass, field

    @dataclass
    class A:
        x: int
        rest: CatchAll = field(default_factory=dict)

    A.__init__ = _CatchAllUndefinedParameters.create_init(A)

    # 1. No extra parameters -> catch-all is empty dict
    obj = A(1)
    assert obj.x == 1
    assert obj.rest == {}

    # 2. Unknown keyword parameters are collected into the catch-all field
    obj = A(1, unknown=5, other="hi")
    assert obj.x == 1
    assert obj.rest == {"unknown": 5, "other": "hi"}

    # 3. Extra positional parameters are collected under _UNKNOWN{i} keys
    obj = A(1, 2, 3)
    assert obj.x == 1
    assert obj.rest == {"_UNKNOWN0": 2, "_UNKNOWN1": 3}

    # 4. Explicitly passing the catch-all field passes through unchanged
    obj = A(1, rest={"a": 1})
    assert obj.x == 1
    assert obj.rest == {"a": 1}

    # 5. Non-dict value for the catch-all field raises UndefinedParameterError
    try:
        A(1, rest=5)
        assert False, "Expected UndefinedParameterError"
    except UndefinedParameterError:
        pass

# Generated at 2026-10-24 14:57:18.112064
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

# Generated at 2026-10-24 14:57:19.446546
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    from dataclasses import dataclass, field

    @dataclass
    class A:
        x: int
        rest: CatchAll = field(default_factory=dict)

    A.__init__ = _CatchAllUndefinedParameters.create_init(A)

    # 1. No extra parameters -> catch-all is empty dict
    obj = A(1)
    assert obj.x == 1
    assert obj.rest == {}

    # 2. Unknown keyword parameters are collected into the catch-all field
    obj = A(1, unknown=5, other="hi")
    assert obj.x == 1
    assert obj.rest == {"unknown": 5, "other": "hi"}

    # 3. Extra positional parameters are collected under _UNKNOWN{i} keys
    obj = A(1, 2, 3)
    assert obj.x == 1
    assert obj.rest == {"_UNKNOWN0": 2, "_UNKNOWN1": 3}

    # 4. Explicitly passing the catch-all field passes through unchanged
    obj = A(1, rest={"a": 1})
    assert obj.x == 1
    assert obj.rest == {"a": 1}

    # 5. Non-dict value for the catch-all field raises UndefinedParameterError
    try:
        A(1, rest=5)
        assert False, "Expected UndefinedParameterError"
    except UndefinedParameterError:
        pass

# Generated at 2026-10-24 14:57:20.868757
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    # 1. String message â how it's raised in undefined.py
    err = UndefinedParameterError("Received undefined initialization arguments {'x': 1}")
    assert isinstance(err, ValidationError)
    assert isinstance(err, Exception)
    assert err.messages == ["Received undefined initialization arguments {'x': 1}"]
    assert err.data is None
    assert err.valid_data is None

    # 2. Explicit constructor arguments are stored unchanged
    err = UndefinedParameterError(
        {"x": ["Invalid value."]},
        field_name="x",
        data={"x": 1},
        valid_data={},
    )
    assert err.messages == {"x": ["Invalid value."]}
    assert err.field_name == "x"
    assert err.data == {"x": 1}
    assert err.valid_data == {}

    # 3. List message is preserved
    assert UndefinedParameterError(["a", "b"]).messages == ["a", "b"]

    # 4. Raisable / catchable as both types
    with pytest.raises(UndefinedParameterError, match="bad input"):
        raise UndefinedParameterError("bad input")
    with pytest.raises(ValidationError):
        raise UndefinedParameterError("bad input")

# Generated at 2026-10-24 14:57:22.292306
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

# Generated at 2026-10-24 14:57:23.930531
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 14:57:25.268777
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():from dataclasses import dataclass

@dataclasses.dataclass
class _Sample:
    x: int
    y: str = "default"

obj = _Sample(x=1)
result = _UndefinedParameterAction.handle_dump(obj)
assert result == {}

# Generated at 2026-10-24 14:57:26.603587
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():import unittest
from dataclasses import dataclass

from dataclasses_json import CatchAll
from dataclasses_json.undefined import _CatchAllUndefinedParameters


@dataclass
class _Example:
    field_a: str
    extra_data: CatchAll = None


class TestCatchAllUndefinedParametersHandleToDict(unittest.TestCase):

    def test_merges_catch_all_dict_into_kvs(self):
        # arrange
        obj = _Example(field_a="value")
        kvs = {"field_a": "value", "extra_data": {"b": 2, "c": "three"}}

        # act
        result = _CatchAllUndefinedParameters.handle_to_dict(obj, kvs)

        # assert â catch-all contents are hoisted to top level
        self.assertEqual(result, {"field_a": "value", "b": 2, "c": "three"})

    def test_catch_all_key_is_removed(self):
        # arrange
        obj = _Example(field_a="value")
        kvs = {"field_a": "value", "extra_data": {"b": 2}}

        # act
        result = _CatchAllUndefinedParameters.handle_to_dict(obj, kvs)

        # assert â the catch-all field name itself no longer appears
        self.assertNotIn("extra_data", result)

    def test_empty_catch_all_dict(self):
        # arrange
        obj = _Example(field_a="value", extra_data={})
        kvs = {"field_a": "value", "extra_data": {}}

        # act
        result = _CatchAllUndefinedParameters.handle_to_dict(obj, kvs)

        # assert
        self.assertEqual(result, {"field_a": "value"})

    def test_non_dict_catch_all_is_dropped(self):
        # arrange
        obj = _Example(field_a="value", extra_data="not-a-dict")
        kvs = {"field_a": "value", "extra_data": "not-a-dict"}

        # act
        result = _CatchAllUndefinedParameters.handle_to_dict(obj, kvs)

        # assert â popped unconditionally, only merged if dict
        self.assertEqual(result, {"field_a": "value"})

    def test_mutates_kvs_in_place_and_returns_it(self):
        # arrange
        obj = _Example(field_a="value")
        kvs = {"field_a": "value", "extra_data": {"x": 1}}

        # act
        result = _CatchAllUndefinedParameters.handle_to_dict(obj, kvs)

        # assert â implementation pops/updates on the same dict
        self.assertIs(result, kvs)


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-10-24 14:57:44.494430
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:57:46.908509
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:57:49.322339
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:57:51.735207
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 14:57:54.148236
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 14:57:56.560166
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 14:57:59.496048
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:58:01.909074
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:58:04.322214
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:58:06.734318
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 14:58:09.146786
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 14:58:11.560781
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 14:58:13.974103
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:58:16.387202
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:58:18.799110
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:58:21.211464
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:58:23.624738
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:58:26.038195
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:58:28.456567
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:58:30.870324
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:58:33.283424
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:58:35.697071
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:58:38.112270
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:58:40.524402
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:58:42.936783
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 14:58:45.350079
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 14:58:47.762711
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 14:58:50.176034
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 14:58:52.587928
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 14:58:55.001750
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 14:58:57.414257
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:58:58.819518
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():from dataclasses import dataclass

# Generated at 2026-10-24 14:59:21.180949
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    @dataclasses.dataclass
    class Example:
        value: int

    original_init = Example.__init__
    created_init = _UndefinedParameterAction.create_init(Example)

    assert created_init is original_init

    instance = Example.__new__(Example)
    created_init(instance, value=42)

    assert instance.value == 42

# Generated at 2026-10-24 14:59:26.735825
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:59:28.151090
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():from dataclasses import dataclass

# Generated at 2026-10-24 14:59:44.835073
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    # handle_to_dict is a pass-through on the base class:
    # it must return the input dict unchanged.

    obj = object()  # obj is unused by the base implementation
    kvs = {"a": 1, "b": "two", "c": None}

    result = _UndefinedParameterAction.handle_to_dict(obj, kvs)

    assert result == {"a": 1, "b": "two", "c": None}
    assert result is kvs  # base class returns the same dict, not a copy

    # Empty dict stays empty
    assert _UndefinedParameterAction.handle_to_dict(obj, {}) == {}

# Generated at 2026-10-24 14:59:47.254616
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 14:59:49.765910
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 14:59:52.313650
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 14:59:54.727894
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:59:57.141645
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:59:59.554234
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 15:00:01.968993
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 15:00:04.383645
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 15:00:06.793956
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 15:00:32.142708
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    obj = object()
    kvs = {"a": 1, "b": "x", 3: [1, 2]}
    result = _UndefinedParameterAction.handle_to_dict(obj, kvs)
    assert result == {"a": 1, "b": "x", 3: [1, 2]}
    assert result is kvs
    empty = {}
    empty_result = _UndefinedParameterAction.handle_to_dict(obj, empty)
    assert empty_result == {}
    assert empty_result is empty
    other = {"nested": {"k": "v"}}
    assert _UndefinedParameterAction.handle_to_dict(None, other) is other
    assert _UndefinedParameterAction.handle_to_dict(obj, other) == {"nested": {"k": "v"}}

# Generated at 2026-10-24 15:00:33.986886
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

# Generated at 2026-10-24 15:00:35.374222
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    # 1. String message â how it's raised in undefined.py
    err = UndefinedParameterError("Received undefined initialization arguments {'x': 1}")
    assert isinstance(err, ValidationError)
    assert isinstance(err, Exception)
    assert err.messages == ["Received undefined initialization arguments {'x': 1}"]
    assert err.data is None
    assert err.valid_data is None

    # 2. Explicit constructor arguments are stored unchanged
    err = UndefinedParameterError(
        {"x": ["Invalid value."]},
        field_name="x",
        data={"x": 1},
        valid_data={},
    )
    assert err.messages == {"x": ["Invalid value."]}
    assert err.field_name == "x"
    assert err.data == {"x": 1}
    assert err.valid_data == {}

    # 3. List message is preserved
    assert UndefinedParameterError(["a", "b"]).messages == ["a", "b"]

    # 4. Raisable / catchable as both types
    with pytest.raises(UndefinedParameterError, match="bad input"):
        raise UndefinedParameterError("bad input")
    with pytest.raises(ValidationError):
        raise UndefinedParameterError("bad input")

# Generated at 2026-10-24 15:00:37.793542
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 15:00:40.221473
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 15:00:42.627371
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 15:00:45.042046
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 15:00:47.500510
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 15:00:49.913394
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 15:00:59.219179
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 15:01:01.631020
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 15:01:04.043860
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 15:01:06.456980
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 15:01:08.870462
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 15:01:11.283753
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 15:01:13.696989
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 15:01:16.111315
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 15:01:18.524355
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 15:01:20.939731
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 15:01:23.352334
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 15:01:25.766332
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 15:01:28.179313
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 15:01:30.593526
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 15:01:33.004544
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 15:01:35.417341
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 15:01:37.829252
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 15:01:40.243101
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 15:01:42.655949
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 15:01:45.071089
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 15:01:47.484082
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 15:01:49.898144
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 15:01:52.311767
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 15:01:54.727936
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 15:01:57.140695
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 15:01:59.553626
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 15:02:01.967427
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 15:02:04.551043
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 15:02:05.941640
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():from dataclasses import dataclass

@dataclasses.dataclass
class _Sample:
    x: int
    y: str = "default"

obj = _Sample(x=1)
result = _UndefinedParameterAction.handle_dump(obj)
assert result == {}