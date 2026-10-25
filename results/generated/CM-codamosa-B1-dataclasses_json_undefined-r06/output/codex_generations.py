

# Generated at 2026-10-24 12:20:58.213118
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

# Generated at 2026-10-24 12:20:59.532469
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 12:21:00.866452
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():from dataclasses import dataclass

@dataclasses.dataclass
class _Sample:
    x: int
    y: str = "default"

obj = _Sample(x=1)
result = _UndefinedParameterAction.handle_dump(obj)
assert result == {}

# Generated at 2026-10-24 12:21:02.306155
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

# Generated at 2026-10-24 12:21:12.360934
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

# Generated at 2026-10-24 12:21:13.751866
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

# Generated at 2026-10-24 12:22:25.151298
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

# Generated at 2026-10-24 12:22:27.662063
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-24 12:22:30.084293
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-24 12:22:32.500369
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-24 12:22:35.078481
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 12:22:37.607977
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 12:22:40.035667
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 12:22:42.546533
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-24 12:22:44.962525
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-24 12:22:47.383157
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-24 12:22:58.660357
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():from dataclasses import dataclass

# Generated at 2026-10-24 12:23:00.023818
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

# Generated at 2026-10-24 12:23:23.111944
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

# Generated at 2026-10-24 12:23:25.784965
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 12:23:28.314218
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 12:23:30.735930
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 12:23:33.151926
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 12:23:35.566047
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 12:23:37.982993
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 12:23:40.396766
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 12:23:42.809743
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 12:23:45.226216
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 12:23:47.792496
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-24 12:23:50.205888
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-24 12:23:52.618900
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-24 12:23:55.032141
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-24 12:24:10.625535
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-24 12:24:11.960184
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-24 12:24:13.303102
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 12:24:14.629620
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():from dataclasses import dataclass

@dataclasses.dataclass
class _Sample:
    x: int
    y: str = "default"

obj = _Sample(x=1)
result = _UndefinedParameterAction.handle_dump(obj)
assert result == {}

# Generated at 2026-10-24 12:24:37.944167
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 12:24:40.500796
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 12:24:42.913928
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 12:24:45.328409
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 12:24:47.743058
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 12:24:50.156390
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 12:24:52.570329
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 12:24:54.984283
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 12:24:57.401373
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 12:24:59.811008
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 12:25:02.225004
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 12:25:19.911454
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    message = "Received undefined initialization arguments {'x': 1}"
    error = UndefinedParameterError(message)

    assert isinstance(error, ValidationError)
    assert isinstance(error, UndefinedParameterError)
    assert error.messages == [message]
    assert str(error) == message
    assert error.args == (message,)

    field_error = UndefinedParameterError("bad value", field_name="age")
    assert field_error.messages == ["bad value"]
    assert field_error.field_name == "age"

# Generated at 2026-10-24 12:25:21.252643
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

# Generated at 2026-10-24 12:25:24.458095
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

# Generated at 2026-10-24 12:25:25.782777
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 12:25:27.197349
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():from dataclasses import dataclass

@dataclasses.dataclass
class _Sample:
    x: int
    y: str = "default"

obj = _Sample(x=1)
result = _UndefinedParameterAction.handle_dump(obj)
assert result == {}

# Generated at 2026-10-24 12:25:28.545360
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

# Generated at 2026-10-24 12:25:29.962388
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

# Generated at 2026-10-24 12:25:32.687495
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

# Generated at 2026-10-24 12:25:34.019873
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 12:25:35.492955
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():from dataclasses import dataclass

@dataclasses.dataclass
class _Sample:
    x: int
    y: str = "default"

obj = _Sample(x=1)
result = _UndefinedParameterAction.handle_dump(obj)
assert result == {}

# Generated at 2026-10-24 12:25:38.040821
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 12:25:40.838184
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 12:25:43.254824
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 12:25:45.785920
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 12:25:48.199891
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 12:25:50.614036
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 12:25:53.036728
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 12:25:55.444597
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 12:25:57.858588
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 12:26:00.277932
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 12:26:02.691726
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 12:26:13.614807
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():obj = object()

# Generated at 2026-10-24 12:26:14.949456
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

# Generated at 2026-10-24 12:26:16.289465
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

# Generated at 2026-10-24 12:26:17.605686
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

# Generated at 2026-10-24 12:26:18.936830
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 12:26:20.292736
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():from dataclasses import dataclass

@dataclasses.dataclass
class _Sample:
    x: int
    y: str = "default"

obj = _Sample(x=1)
result = _UndefinedParameterAction.handle_dump(obj)
assert result == {}

# Generated at 2026-10-24 12:26:21.709015
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

# Generated at 2026-10-24 12:26:23.057815
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

# Generated at 2026-10-24 12:26:24.464132
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

# Generated at 2026-10-24 12:26:41.156873
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

# Generated at 2026-10-24 12:26:43.563597
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 12:26:45.978620
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 12:26:48.604499
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 12:26:51.017691
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 12:26:53.441360
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 12:26:55.854460
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 12:26:58.268182
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 12:27:00.779871
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 12:27:03.192919
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 12:27:05.605692
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 12:27:08.126052
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    message = "Received undefined initialization arguments {'x': 1}"
    error = UndefinedParameterError(message)

    assert isinstance(error, ValidationError)
    assert isinstance(error, UndefinedParameterError)
    assert error.messages == [message]
    assert str(error) == message
    assert error.args == (message,)

    field_error = UndefinedParameterError("bad value", field_name="age")
    assert field_error.messages == ["bad value"]
    assert field_error.field_name == "age"

# Generated at 2026-10-24 12:27:25.285697
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

# Generated at 2026-10-24 12:27:26.725548
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 12:27:28.110653
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():from dataclasses import dataclass

@dataclasses.dataclass
class _Sample:
    x: int
    y: str = "default"

obj = _Sample(x=1)
result = _UndefinedParameterAction.handle_dump(obj)
assert result == {}

# Generated at 2026-10-24 12:27:29.492768
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

# Generated at 2026-10-24 12:27:30.890463
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

# Generated at 2026-10-24 12:27:32.234078
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

# Generated at 2026-10-24 12:27:33.629440
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

# Generated at 2026-10-24 12:27:36.220124
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 12:27:38.819574
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 12:27:41.229629
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 12:27:43.882445
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 12:27:46.290850
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 12:27:48.703707
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 12:27:51.117950
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 12:27:53.947585
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 12:27:56.361807
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 12:27:58.779302
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 12:28:01.191399
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 12:28:03.608512
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 12:28:09.689425
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-24 12:28:12.103634
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-24 12:28:14.516893
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-24 12:28:16.929555
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 12:28:19.343394
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 12:28:21.754548
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 12:28:24.169184
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 12:28:26.579467
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 12:28:28.993032
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 12:28:31.406763
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 12:28:33.819825
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 12:28:36.233800
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 12:28:38.646822
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-24 12:28:41.059868
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-24 12:28:43.474057
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-24 12:28:45.887361
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 12:28:48.304792
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 12:28:50.715642
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 12:28:53.128876
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 12:28:55.554282
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 12:28:57.966565
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 12:29:00.378367
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 12:29:02.794175
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 12:29:05.204333
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 12:29:07.616511
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 12:29:10.030124
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 12:29:12.443033
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 12:29:14.863578
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 12:29:17.283283
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 12:29:19.699159
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 12:29:28.593705
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 12:29:31.007882
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 12:29:33.422301
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 12:29:35.834179
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 12:29:38.247349
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 12:29:40.659623
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 12:29:43.072731
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 12:29:45.486590
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 12:29:47.900719
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 12:29:50.313650
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 12:29:52.727269
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 12:29:55.141115
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 12:29:57.555142
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 12:29:59.968170
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 12:30:13.739871
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():assert _UndefinedParameterAction.handle_dump(object()) == {}

# Generated at 2026-10-24 12:30:15.164587
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

# Generated at 2026-10-24 12:30:16.599929
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

# Generated at 2026-10-24 12:30:17.954911
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 12:30:19.271902
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():from dataclasses import dataclass

@dataclasses.dataclass
class _Sample:
    x: int
    y: str = "default"

obj = _Sample(x=1)
result = _UndefinedParameterAction.handle_dump(obj)
assert result == {}

# Generated at 2026-10-24 12:30:22.005120
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

# Generated at 2026-10-24 12:30:40.548301
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 12:30:42.961811
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 12:30:45.376949
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters