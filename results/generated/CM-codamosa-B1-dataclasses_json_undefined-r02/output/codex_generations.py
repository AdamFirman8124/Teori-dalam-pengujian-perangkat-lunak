

# Generated at 2026-10-24 14:20:24.501768
# Unit test for constructor of class _UndefinedParameterAction
def test__UndefinedParameterAction():
    # _UndefinedParameterAction is an abstract base class:
    # it has an abstract static method (handle_from_dict),
    # so instantiating it directly must raise TypeError.
    with pytest.raises(TypeError):
        _UndefinedParameterAction()

    # Non-abstract static methods should still be usable via the class.
    # _separate_defined_undefined_kvs splits kvs into known / unknown.
    class _Dummy:
        pass

    import dataclasses as dc

    @dc.dataclasses_dataclass if False else dc.dataclass
    class _Dummy:
        known_field: int = 0

    known, unknown = _UndefinedParameterAction._separate_defined_undefined_kvs(
        _Dummy, {"known_field": 1, "extra": 2})
    assert known == {"known_field": 1}
    assert unknown == {"extra": 2}

# Generated at 2026-10-24 14:20:26.925285
# Unit test for method handle_from_dict of class _IgnoreUndefinedParameters

# Generated at 2026-10-24 14:20:29.344302
# Unit test for method handle_from_dict of class _IgnoreUndefinedParameters

# Generated at 2026-10-24 14:20:31.758592
# Unit test for method handle_from_dict of class _IgnoreUndefinedParameters

# Generated at 2026-10-24 14:20:34.370639
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 14:20:36.786394
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 14:20:39.200381
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 14:20:41.730888
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

# Generated at 2026-10-24 14:20:43.047661
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 14:20:44.425770
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():from dataclasses import dataclass

@dataclasses.dataclass
class _Sample:
    x: int
    y: str = "default"

obj = _Sample(x=1)
result = _UndefinedParameterAction.handle_dump(obj)
assert result == {}

# Generated at 2026-10-24 14:20:45.735782
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

# Generated at 2026-10-24 14:20:47.074209
# Unit test for method handle_dump of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_dump():
    @dataclasses.dataclass
    class Example:
        x: int
        catch_all: CatchAll = dataclasses.field(default_factory=dict)

    obj = Example(x=1, catch_all={"extra": 42, "other": "value"})

    result = _CatchAllUndefinedParameters.handle_dump(obj)

    assert result == {"extra": 42, "other": "value"}
    assert _CatchAllUndefinedParameters.handle_dump(Example(x=1)) == {}

# Generated at 2026-10-24 14:20:48.382793
# Unit test for method handle_dump of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_dump():
    @dataclasses.dataclass
    class Example:
        x: int
        catch_all: CatchAll = dataclasses.field(default_factory=dict)

    obj = Example(x=1, catch_all={"extra": 42, "other": "value"})

    result = _CatchAllUndefinedParameters.handle_dump(obj)

    assert result == {"extra": 42, "other": "value"}
    assert _CatchAllUndefinedParameters.handle_dump(Example(x=1)) == {}

# Generated at 2026-10-24 14:20:49.713124
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 14:20:51.040217
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():from dataclasses import dataclass

@dataclasses.dataclass
class _Sample:
    x: int
    y: str = "default"

obj = _Sample(x=1)
result = _UndefinedParameterAction.handle_dump(obj)
assert result == {}

# Generated at 2026-10-24 14:20:52.367262
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

# Generated at 2026-10-24 14:20:53.703974
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

# Generated at 2026-10-24 14:20:56.246309
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:20:58.661595
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:21:01.073904
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:21:03.595871
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 14:21:06.015473
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 14:21:08.429216
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 14:21:10.842794
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:21:13.258558
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:21:15.678585
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:21:18.093438
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-24 14:21:20.507727
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-24 14:21:22.921113
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-24 14:21:25.335988
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:21:27.765263
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:21:30.183651
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:21:32.598716
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 14:21:35.027342
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 14:21:37.443725
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 14:21:39.860239
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 14:21:42.275177
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 14:21:44.690066
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 14:21:47.104723
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 14:21:49.519961
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 14:21:51.937768
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 14:21:54.358121
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 14:21:56.779158
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 14:21:59.194996
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 14:22:01.609860
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 14:22:04.023377
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 14:22:06.439936
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 14:22:08.855625
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:22:11.271004
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:22:13.685598
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:22:16.101443
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 14:22:18.516042
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 14:22:20.931552
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 14:22:23.348599
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:22:25.763096
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:22:34.297968
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:22:35.615416
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

# Generated at 2026-10-24 14:22:52.266502
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    dummy_obj = object()

    # empty dict
    kvs = {}
    result = _UndefinedParameterAction.handle_to_dict(dummy_obj, kvs)
    assert result == {}
    assert result is kvs

    # normal defined parameters
    kvs = {"a": 1, "b": "x"}
    result = _UndefinedParameterAction.handle_to_dict(dummy_obj, kvs)
    assert result == {"a": 1, "b": "x"}
    assert result is kvs

    # Any keys / values are passed through unchanged
    kvs = {1: "one", None: object(), "nested": {"k": [1, 2, 3]}}
    result = _UndefinedParameterAction.handle_to_dict(dummy_obj, kvs)
    assert result == kvs
    assert result is kvs

    # obj argument is ignored
    kvs = {"x": 1}
    assert _UndefinedParameterAction.handle_to_dict(None, kvs) is kvs
    assert _UndefinedParameterAction.handle_to_dict("anything", kvs) is kvs

# Generated at 2026-10-24 14:23:08.699317
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():import unittest
from dataclasses import dataclass, field
from typing import Optional

from dataclasses_json.undefined import (
    _RaiseUndefinedParameters,
    _IgnoreUndefinedParameters,
    _CatchAllUndefinedParameters,
    UndefinedParameterError,
)


@dataclass
class Person:
    name: str
    age: int


@dataclass
class PersonWithCatchAll:
    name: str
    misc: Optional[CatchAllVar] = None


from dataclasses_json.utils import CatchAllVar  # noqa: E402  (needs CatchAllVar at annotation time)


class TestHandleFromDict(unittest.TestCase):

    # --- _RaiseUndefinedParameters: known params only ---
    def test_raise_with_known_params(self):
        result = _RaiseUndefinedParameters.handle_from_dict(
            Person, {"name": "Alice", "age": 30})
        self.assertEqual(result, {"name": "Alice", "age": 30})

    # --- _RaiseUndefinedParameters: unknown param raises ---
    def test_raise_with_unknown_param(self):
        with self.assertRaises(UndefinedParameterError) as ctx:
            _RaiseUndefinedParameters.handle_from_dict(
                Person, {"name": "Alice", "age": 30, "city": "Berlin"})
        self.assertIn("city", str(ctx.exception))

    # --- _IgnoreUndefinedParameters: unknown params are dropped ---
    def test_ignore_drops_unknown_params(self):
        result = _IgnoreUndefinedParameters.handle_from_dict(
            Person, {"name": "Alice", "age": 30, "city": "Berlin"})
        self.assertEqual(result, {"name": "Alice", "age": 30})

    # --- _CatchAllUndefinedParameters: unknown params go into catch-all field ---
    def test_catch_all_collects_unknown(self):
        result = _CatchAllUndefinedParameters.handle_from_dict(
            PersonWithCatchAll, {"name": "Alice", "city": "Berlin"})
        self.assertEqual(result, {"name": "Alice", "misc": {"city": "Berlin"}})

    # --- _CatchAllUndefinedParameters: no unknowns -> empty dict ---
    def test_catch_all_empty_when_no_unknowns(self):
        result = _CatchAllUndefinedParameters.handle_from_dict(
            PersonWithCatchAll, {"name": "Alice"})
        self.assertEqual(result, {"name": "Alice", "misc": {}})

    # --- _CatchAllUndefinedParameters: merges into pre-filled catch-all ---
    def test_catch_all_merges_prefilled(self):
        result = _CatchAllUndefinedParameters.handle_from_dict(
            PersonWithCatchAll,
            {"name": "Alice", "misc": {"country": "DE"}, "city": "Berlin"})
        self.assertEqual(result, {
            "name": "Alice",
            "misc": {"country": "DE", "city": "Berlin"}})

    # --- _CatchAllUndefinedParameters: non-dict value for catch-all field errors ---
    def test_catch_all_rejects_non_dict_conflict(self):
        with self.assertRaises(UndefinedParameterError):
            _CatchAllUndefinedParameters.handle_from_dict(
                PersonWithCatchAll, {"name": "Alice", "misc": "oops"})

# Generated at 2026-10-24 14:23:11.116859
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:23:13.534467
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:23:15.946615
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:23:18.361375
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 14:23:20.775694
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 14:23:23.190606
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 14:23:25.605641
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 14:23:28.022323
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 14:23:30.439767
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 14:23:32.852668
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:23:35.269287
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:23:58.725353
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:24:00.129529
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

# Generated at 2026-10-24 14:24:01.460733
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

# Generated at 2026-10-24 14:24:04.029587
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 14:24:06.615421
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 14:24:09.031336
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 14:24:11.630610
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 14:24:14.045967
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 14:24:16.461842
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 14:24:19.135605
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 14:24:21.549774
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 14:24:23.965989
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 14:24:26.529685
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 14:24:28.948627
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 14:24:31.367115
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 14:24:33.793511
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 14:24:36.204353
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 14:24:38.621216
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 14:24:41.037472
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 14:24:43.451558
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 14:24:45.868353
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 14:24:48.285065
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 14:24:50.699597
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 14:24:53.112947
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 14:24:55.529988
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:24:57.944155
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:25:00.361095
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:25:02.777698
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 14:25:05.194286
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 14:25:07.610289
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 14:25:10.026940
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 14:25:12.441950
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 14:25:14.861685
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 14:25:17.276687
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 14:25:19.692417
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 14:25:22.105784
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 14:25:24.520533
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 14:25:26.935957
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 14:25:37.744301
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 14:25:40.063584
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

# Generated at 2026-10-24 14:25:41.381952
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

# Generated at 2026-10-24 14:25:42.706877
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

# Generated at 2026-10-24 14:25:44.029524
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

# Generated at 2026-10-24 14:25:45.344094
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

# Generated at 2026-10-24 14:25:46.659105
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

# Generated at 2026-10-24 14:25:48.091437
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

# Generated at 2026-10-24 14:25:49.520504
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

# Generated at 2026-10-24 14:25:52.327343
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:25:53.721930
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():from dataclasses import dataclass

# Generated at 2026-10-24 14:25:56.141511
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-24 14:25:58.556950
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-24 14:26:00.971467
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-24 14:26:06.633218
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 14:26:09.048267
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 14:26:11.462875
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 14:26:14.039960
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 14:26:16.448907
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 14:26:18.863853
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 14:26:21.281947
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 14:26:23.694992
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 14:26:26.107841
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 14:26:28.520568
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:26:30.934923
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:26:33.347886
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:26:35.760725
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 14:26:38.174753
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 14:26:43.749046
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():kvs = {"name": "Alice", "age": 30}

# Generated at 2026-10-24 14:26:45.076572
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

# Generated at 2026-10-24 14:27:10.448860
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    # The method defines an abstract contract and prevents direct
    # instantiation of the base action.
    assert (
        "handle_from_dict"
        in _UndefinedParameterAction.__abstractmethods__
    )
    assert getattr(
        _UndefinedParameterAction.handle_from_dict,
        "__isabstractmethod__",
        False,
    )

    with pytest.raises(TypeError):
        _UndefinedParameterAction()

# Generated at 2026-10-24 14:27:12.864886
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 14:27:15.278032
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 14:27:17.692155
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 14:27:20.104366
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:27:22.517809
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:27:24.935416
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:27:27.344054
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:27:29.758333
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:27:32.172295
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:27:39.530629
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:27:41.947119
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:27:44.360438
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:28:03.052400
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 14:28:10.938880
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    @dataclasses.dataclass
    class Sample:
        a: int
        b: str = "default"

    # The base implementation is abstract and its body is `pass`,
    # so it must return None for any concrete input.
    known_and_unknown = {"a": 1, "b": "override", "c": 3}
    result = _UndefinedParameterAction.handle_from_dict(Sample, known_and_unknown)
    assert result is None

    # Same for the empty input case.
    assert _UndefinedParameterAction.handle_from_dict(Sample, {}) is None

    # Input must not be mutated by the base implementation.
    assert known_and_unknown == {"a": 1, "b": "override", "c": 3}

    # The method is declared abstract, so the base class cannot be instantiated.
    assert getattr(
        _UndefinedParameterAction.handle_from_dict, "__isabstractmethod__", False
    ) is True

    try:
        _UndefinedParameterAction()
    except TypeError as exc:
        assert "abstract" in str(exc).lower()
    else:
        raise AssertionError("_UndefinedParameterAction should not be instantiable")

# Generated at 2026-10-24 14:28:12.340418
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

# Generated at 2026-10-24 14:28:13.708002
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

# Generated at 2026-10-24 14:28:16.590464
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-24 14:28:19.005800
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-24 14:28:21.417505
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-24 14:28:23.831225
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:28:26.244933
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:28:28.658324
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:28:31.071615
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-24 14:28:33.642509
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-24 14:28:36.055732
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-24 14:28:38.468708
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 14:28:40.881459
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 14:28:43.294429
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 14:28:45.707527
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 14:28:48.120416
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 14:28:50.532754
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 14:28:52.945564
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:28:55.363477
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:28:57.774008
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:29:13.855161
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 14:29:16.268474
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 14:29:18.681475
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 14:29:21.095829
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 14:29:23.507583
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 14:29:25.920648
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 14:29:28.333241
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 14:29:30.746416
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 14:29:33.159409
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 14:29:35.572879
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:29:37.985666
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:29:40.404232
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 14:29:42.821127
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 14:29:45.234715
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 14:29:47.646233
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 14:30:03.794630
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 14:30:05.214531
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():from dataclasses import dataclass

@dataclasses.dataclass
class _Sample:
    x: int
    y: str = "default"

obj = _Sample(x=1)
result = _UndefinedParameterAction.handle_dump(obj)
assert result == {}

# Generated at 2026-10-24 14:30:06.610661
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

# Generated at 2026-10-24 14:30:23.238390
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