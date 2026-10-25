

# Generated at 2026-10-24 13:16:35.954398
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

# Generated at 2026-10-24 13:16:52.334266
# Unit test for constructor of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters():
    # 1. Constructor: instantiable (abstract handle_from_dict is implemented)
    assert isinstance(_IgnoreUndefinedParameters(), _UndefinedParameterAction)

    # 2. handle_from_dict: keeps only defined fields
    @dataclasses.dataclass
    class Example:
        a: int = 1
        b: str = "x"

    assert _IgnoreUndefinedParameters.handle_from_dict(
        Example, {"a": 2, "b": "y", "unknown": 99, "extra": None}
    ) == {"a": 2, "b": "y"}
    assert _IgnoreUndefinedParameters.handle_from_dict(Example, {}) == {}

    # 3. create_init (the constructor wrapper): unknown kwargs ignored
    Example.__init__ = _IgnoreUndefinedParameters.create_init(Example)

    assert Example() == Example(a=1, b="x")                      # defaults kept
    assert Example(2, "y") == Example(a=2, b="y")                # positional kept
    assert Example(2, "y", unknown=99) == Example(a=2, b="y")    # unknown kwarg dropped
    assert Example(b="z", junk=[1, 2]) == Example(a=1, b="z")    # known kwarg kept
    assert not hasattr(Example(unknown=99), "unknown")

    # 4. create_init: excess positional args ignored
    assert Example(2, "y", 999, "overflow") == Example(a=2, b="y")
    assert Example(2, b="y", extra=1) == Example(a=2, b="y")

# Generated at 2026-10-24 13:16:53.772026
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

# Generated at 2026-10-24 13:17:13.439187
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

# Generated at 2026-10-24 13:17:20.041987
# Unit test for constructor of class _UndefinedParameterAction
def test__UndefinedParameterAction():
    with pytest.raises(TypeError, match="abstract"):
        _UndefinedParameterAction()

# Generated at 2026-10-24 13:17:22.457026
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 13:17:24.870966
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 13:17:27.284642
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 13:17:29.800927
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 13:17:32.215023
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 13:17:34.628241
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 13:17:37.043227
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 13:17:39.457096
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 13:17:41.871730
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 13:17:44.466896
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 13:17:46.880194
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 13:17:49.295714
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 13:17:51.712203
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 13:17:54.131305
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 13:17:56.547605
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 13:17:58.962828
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 13:18:01.377365
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 13:18:03.792561
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 13:18:26.183788
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    @dataclasses.dataclass
    class Example:
        name: str
        extra: CatchAll = dataclasses.field(default_factory=dict)

    result = _CatchAllUndefinedParameters.handle_from_dict(
        Example,
        {
            "name": "Alice",
            "age": 30,
            "active": True,
        },
    )

    assert result == {
        "name": "Alice",
        "extra": {
            "age": 30,
            "active": True,
        },
    }

# Generated at 2026-10-24 13:18:27.539636
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

# Generated at 2026-10-24 13:18:28.872367
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

# Generated at 2026-10-24 13:18:30.224924
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

# Generated at 2026-10-24 13:18:31.618482
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

# Generated at 2026-10-24 13:18:32.951517
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

# Generated at 2026-10-24 13:18:35.501757
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 13:18:38.061532
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 13:18:40.479519
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 13:18:42.897209
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 13:18:45.413643
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 13:18:47.827014
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 13:18:50.243100
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 13:18:52.661268
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 13:18:55.078661
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 13:18:57.497187
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 13:18:59.926238
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 13:19:02.339729
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 13:19:04.927198
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-24 13:19:07.338567
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-24 13:19:09.762858
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-24 13:19:12.166579
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 13:19:14.580727
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 13:19:16.996518
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 13:19:19.410399
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 13:19:21.825714
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 13:19:24.239306
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 13:19:26.653044
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 13:19:29.067425
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 13:19:31.480929
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 13:19:33.894551
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 13:19:36.308963
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 13:19:38.723819
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 13:19:41.137964
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 13:19:43.551835
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 13:19:45.965521
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 13:19:48.379020
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 13:19:50.793242
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 13:19:53.206891
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 13:19:55.620843
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 13:19:58.034147
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 13:20:00.447851
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 13:20:02.860661
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 13:20:05.273549
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 13:20:07.688546
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 13:20:10.100843
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 13:20:12.516240
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 13:20:14.928278
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 13:20:17.341650
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 13:20:19.755368
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 13:20:22.167666
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 13:20:24.581868
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 13:20:26.995417
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 13:20:29.408855
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 13:20:31.822922
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 13:20:34.236463
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 13:20:36.648782
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 13:20:39.066045
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 13:20:41.475299
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 13:20:43.888341
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 13:20:46.300349
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 13:20:48.714483
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 13:20:51.128321
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 13:20:53.542163
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 13:20:55.955618
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 13:20:58.369962
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 13:21:00.783801
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 13:21:03.196650
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 13:21:05.610895
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 13:21:08.024707
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 13:21:10.442155
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 13:21:12.853509
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 13:21:15.267952
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 13:21:17.682501
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 13:21:20.094879
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 13:21:22.507963
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 13:21:24.920905
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 13:21:27.334258
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 13:21:29.748298
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 13:21:32.162654
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 13:21:34.581883
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 13:21:36.998289
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 13:21:39.416068
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 13:21:41.834953
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 13:21:44.247724
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 13:21:46.663897
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 13:21:49.085048
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 13:21:51.499518
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 13:21:53.919980
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 13:21:56.334283
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 13:22:00.678800
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 13:22:03.092814
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 13:22:05.502611
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 13:22:07.914217
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 13:22:10.330401
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 13:22:12.739447
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 13:22:15.151950
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 13:22:17.566525
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 13:22:19.983119
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 13:22:22.393421
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 13:22:24.806130
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 13:22:27.220097
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 13:22:29.632400
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 13:22:32.055273
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 13:22:34.480380
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 13:22:36.894234
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 13:22:39.307422
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 13:22:41.721573
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 13:22:44.134309
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 13:22:46.547939
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 13:22:48.962354
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 13:22:51.376136
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 13:22:53.788380
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 13:22:56.203044
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 13:22:58.616085
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 13:23:01.029573
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 13:23:03.444888
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 13:23:05.864121
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 13:23:08.281122
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 13:23:10.696157
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 13:23:17.470441
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 13:23:19.888173
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 13:23:31.425615
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 13:23:34.119871
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 13:23:35.599591
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():from dataclasses import dataclass

# Generated at 2026-10-24 13:23:37.025704
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

# Generated at 2026-10-24 13:23:44.706789
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    class Example:
        def __init__(self, a: int, b: str = "default"):
            self.a = a
            self.b = b

    original_init = Example.__init__
    result = _UndefinedParameterAction.create_init(Example)

    # Base action is a no-op: it must return the class's __init__ unchanged
    assert result is original_init

    # The returned callable still initializes instances correctly
    instance = result(Example(), a=1, b="x")
    assert instance.a == 1
    assert instance.b == "x"

    # Default values still apply
    instance_default = result(Example(), a=2)
    assert instance_default.b == "default"

# Generated at 2026-10-24 13:23:46.030925
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    class Example:
        def __init__(self, a: int, b: str = "default"):
            self.a = a
            self.b = b

    original_init = Example.__init__
    result = _UndefinedParameterAction.create_init(Example)

    # Base action is a no-op: it must return the class's __init__ unchanged
    assert result is original_init

    # The returned callable still initializes instances correctly
    instance = result(Example(), a=1, b="x")
    assert instance.a == 1
    assert instance.b == "x"

    # Default values still apply
    instance_default = result(Example(), a=2)
    assert instance_default.b == "default"

# Generated at 2026-10-24 13:24:02.522107
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

# Generated at 2026-10-24 13:24:20.226563
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 13:24:29.502486
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():from dataclasses import dataclass

# Generated at 2026-10-24 13:24:32.445911
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 13:24:34.162631
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():from dataclasses import dataclass

# Generated at 2026-10-24 13:24:35.473603
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

# Generated at 2026-10-24 13:24:36.929372
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

# Generated at 2026-10-24 13:24:49.924942
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

# Generated at 2026-10-24 13:24:51.252294
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

# Generated at 2026-10-24 13:24:54.139258
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

# Generated at 2026-10-24 13:24:55.522930
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

# Generated at 2026-10-24 13:24:56.999132
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

# Generated at 2026-10-24 13:24:58.375287
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

# Generated at 2026-10-24 13:24:59.707972
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

# Generated at 2026-10-24 13:25:02.525667
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-24 13:25:04.940904
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-24 13:25:07.358724
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-24 13:25:09.933640
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 13:25:12.347388
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 13:25:14.923604
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 13:25:17.767530
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 13:25:20.188752
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 13:25:22.602338
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-24 13:25:46.256025
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 13:25:47.995882
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():from dataclasses import dataclass

# Generated at 2026-10-24 13:25:49.315945
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

# Generated at 2026-10-24 13:25:50.761268
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

# Generated at 2026-10-24 13:25:52.288023
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

# Generated at 2026-10-24 13:25:53.831410
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

# Generated at 2026-10-24 13:25:55.264782
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

# Generated at 2026-10-24 13:25:56.580292
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 13:25:57.924534
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():from dataclasses import dataclass

@dataclasses.dataclass
class _Sample:
    x: int
    y: str = "default"

obj = _Sample(x=1)
result = _UndefinedParameterAction.handle_dump(obj)
assert result == {}

# Generated at 2026-10-24 13:25:59.667787
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

# Generated at 2026-10-24 13:26:01.209171
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

# Generated at 2026-10-24 13:26:02.642707
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 13:26:04.075148
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():from dataclasses import dataclass

@dataclasses.dataclass
class _Sample:
    x: int
    y: str = "default"

obj = _Sample(x=1)
result = _UndefinedParameterAction.handle_dump(obj)
assert result == {}