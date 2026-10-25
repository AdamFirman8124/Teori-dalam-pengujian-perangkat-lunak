

# Generated at 2026-10-24 11:57:28.766144
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

# Generated at 2026-10-24 11:57:44.437187
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

# Generated at 2026-10-24 11:57:57.243354
# Unit test for constructor of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters():
    @dataclasses.dataclass
    class Dummy:
        a: int
        b: str

    # 1. constructor: can instantiate concrete subclass
    instance = _RaiseUndefinedParameters()
    assert isinstance(instance, _RaiseUndefinedParameters)
    assert isinstance(instance, _UndefinedParameterAction)

    # base class is still abstract and cannot be instantiated directly
    with pytest.raises(TypeError):
        _UndefinedParameterAction()  # type: ignore

    # 2. only known params -> returned unchanged
    known = {"a": 1, "b": "x"}
    result = _RaiseUndefinedParameters.handle_from_dict(Dummy, dict(known))
    assert result == known

    # 3. empty input -> empty output, no error
    assert _RaiseUndefinedParameters.handle_from_dict(Dummy, {}) == {}

    # 4. unknown param -> raises UndefinedParameterError
    with pytest.raises(UndefinedParameterError) as exc_info:
        _RaiseUndefinedParameters.handle_from_dict(
            Dummy, {"a": 1, "b": "x", "c": 999}
        )
    assert "c" in str(exc_info.value)
    assert "Received undefined initialization arguments" in str(exc_info.value)

    # 5. only unknown params -> raises
    with pytest.raises(UndefinedParameterError):
        _RaiseUndefinedParameters.handle_from_dict(Dummy, {"unknown": 1})

    # 6. inherited default behavior is preserved
    kvs = {"a": 1}
    assert _RaiseUndefinedParameters.handle_to_dict(Dummy("a", "b"), kvs) == kvs
    assert _RaiseUndefinedParameters.handle_dump(Dummy("a", "b")) == {}
    assert _RaiseUndefinedParameters.create_init(Dummy) == Dummy.__init__

# Generated at 2026-10-24 11:58:28.863494
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 11:58:31.288404
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 11:59:06.318709
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():from dataclasses import dataclass

# Generated at 2026-10-24 11:59:41.689997
# Unit test for constructor of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters():
    # 1. constructor: no custom __init__, can be instantiated directly
    obj = _IgnoreUndefinedParameters()
    assert isinstance(obj, _IgnoreUndefinedParameters)
    assert isinstance(obj, _UndefinedParameterAction)

    # 2. handle_from_dict: keeps known, drops unknown
    @dataclass
    class Sample:
        a: int
        b: str

    kvs = {"a": 1, "b": "x", "unknown": 123}
    assert _IgnoreUndefinedParameters.handle_from_dict(Sample, kvs) == {
        "a": 1,
        "b": "x",
    }
    assert _IgnoreUndefinedParameters.handle_from_dict(Sample, {}) == {}

    # 3. create_init: generated __init__ ignores unknown kwargs/args
    @dataclass
    class Person:
        name: str
        age: int

    Person.__init__ = _IgnoreUndefinedParameters.create_init(Person)

    p1 = Person(name="Alice", age=30, extra="ignored", other=123)
    assert p1.name == "Alice"
    assert p1.age == 30
    assert not hasattr(p1, "extra")
    assert not hasattr(p1, "other")

    # positional + unknown kwarg mixed
    p2 = Person("Bob", 25, unknown_field="ignored")
    assert (p2.name, p2.age) == ("Bob", 25)

    # extra positional args are truncated, not raised
    p3 = Person("Carol", 40, "extra-positional")
    assert (p3.name, p3.age) == ("Carol", 40)

    # 4. inherited behavior unchanged
    d = {"a": 1, "b": 2}
    assert _IgnoreUndefinedParameters.handle_to_dict(p1, d) == d
    assert _IgnoreUndefinedParameters.handle_dump(p1) == {}

# Generated at 2026-10-24 11:59:58.085713
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

# Generated at 2026-10-24 12:00:12.188954
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

# Generated at 2026-10-24 12:00:37.577330
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

# Generated at 2026-10-24 12:01:14.816964
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 12:01:17.402427
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 12:01:19.819283
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 12:01:22.236569
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 12:01:24.661607
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 12:01:27.079166
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 12:01:29.494788
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 12:01:31.915131
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 12:01:34.334715
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 12:01:35.685659
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

# Generated at 2026-10-24 12:02:08.957696
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 12:02:11.525770
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 12:02:14.046019
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 12:02:16.468672
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 12:02:18.892549
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 12:02:21.459984
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 12:02:23.876962
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 12:02:26.299078
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 12:02:28.718390
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 12:02:31.136135
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 12:02:33.553218
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 12:02:35.975571
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 12:02:38.395291
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 12:02:40.814004
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 12:02:43.232196
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 12:02:45.848062
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 12:02:47.238874
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():from dataclasses import dataclass

# Generated at 2026-10-24 12:03:21.753127
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 12:03:23.076920
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():from dataclasses import dataclass

# Generated at 2026-10-24 12:03:41.947802
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

# Generated at 2026-10-24 12:03:44.374679
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 12:03:46.806762
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 12:03:49.225406
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 12:03:50.805508
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

# Generated at 2026-10-24 12:04:07.631086
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

# Generated at 2026-10-24 12:04:18.883199
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

# Generated at 2026-10-24 12:04:21.308033
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 12:04:23.727845
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 12:04:26.299162
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 12:04:28.947057
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 12:04:31.361115
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 12:04:33.780186
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 12:04:36.199591
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 12:04:38.618478
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 12:04:41.039001
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 12:04:43.455253
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 12:04:45.873186
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 12:04:48.290560
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 12:04:50.879852
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 12:04:52.452978
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():from dataclasses import dataclass

# Generated at 2026-10-24 12:05:01.168989
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 12:05:07.005086
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():from dataclasses import dataclass

@dataclasses.dataclass
class _Sample:
    x: int
    y: str = "default"

obj = _Sample(x=1)
result = _UndefinedParameterAction.handle_dump(obj)
assert result == {}

# Generated at 2026-10-24 12:05:08.653312
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

# Generated at 2026-10-24 12:05:20.222954
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

# Generated at 2026-10-24 12:05:21.553342
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

# Generated at 2026-10-24 12:05:38.345721
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

# Generated at 2026-10-24 12:05:40.774933
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 12:05:43.191317
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 12:05:45.608852
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-24 12:05:48.185665
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 12:05:50.605771
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 12:05:53.041792
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 12:06:09.169778
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():message = "Received undefined initialization arguments {'extra': 1}"

# Generated at 2026-10-24 12:06:26.983421
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 12:06:29.507092
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 12:06:31.928321
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 12:06:34.345621
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 12:06:36.761842
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 12:06:39.179222
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-24 12:06:41.594576
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 12:06:44.015170
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 12:06:46.435054
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 12:06:48.855811
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 12:06:51.272767
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 12:06:53.692102
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-24 12:06:56.110995
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 12:06:58.531217
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 12:07:00.949671
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-24 12:07:03.383795
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 12:07:05.803563
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-24 12:07:08.226265
# Unit test for constructor of class UndefinedParameterError