

# Generated at 2026-11-03 01:36:31.623473
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    class _Dummy:
        pass

    obj = _Dummy()
    result = _UndefinedParameterAction.handle_dump(obj)
    assert result == {}

# Generated at 2026-11-03 01:37:48.001218
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    class Dummy:
        a = 1
        b = "two"

    dummy = Dummy()
    result = _UndefinedParameterAction.handle_dump(dummy)
    assert result == {}

# Generated at 2026-11-03 01:40:31.336358
# Unit test for method handle_dump of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_dump():
    @dataclasses.dataclass
    class Person:
        name: str
        extra: CatchAll = dataclasses.field(default_factory=dict)

    # Object with parameters stored in the catch-all field
    person = Person(name="Alice")
    person.extra = {"age": 30, "city": "Berlin"}
    result = _CatchAllUndefinedParameters.handle_dump(person)
    assert result == {"age": 30, "city": "Berlin"}

    # Object with an empty catch-all field
    person2 = Person(name="Bob")
    result2 = _CatchAllUndefinedParameters.handle_dump(person2)
    assert result2 == {}

    # Object without a catch-all field should raise UndefinedParameterError
    @dataclasses.dataclass
    class NoCatchAll:
        name: str

    raised = False
    try:
        _CatchAllUndefinedParameters.handle_dump(NoCatchAll(name="Charlie"))
    except UndefinedParameterError:
        raised = True
    assert raised

# Generated at 2026-11-03 01:42:47.765845
# Unit test for constructor of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters():
    from dataclasses import dataclass

    @dataclass
    class A:
        one: int
        two: str = "default"

    # create_init returns a wrapped __init__ that ignores undefined parameters
    A.__init__ = _IgnoreUndefinedParameters.create_init(A)

    # Undefined keyword parameters are silently dropped
    obj = A(one=1, two="defined", undefined_parameter=2, another_unknown="x")
    assert obj.one == 1
    assert obj.two == "defined"
    assert not hasattr(obj, "undefined_parameter")
    assert not hasattr(obj, "another_unknown")

    # Defaults are applied for omitted parameters
    obj = A(one=3)
    assert obj.one == 3
    assert obj.two == "default"

    # Extra positional arguments beyond the accepted count are dropped
    obj = A(4, "five", 6, 7)
    assert obj.one == 4
    assert obj.two == "five"
    assert not hasattr(obj, "_UNKNOWN0")

    # handle_from_dict keeps only the known (defined) parameters
    known = _IgnoreUndefinedParameters.handle_from_dict(
        A, {"one": 1, "two": "2", "undefined": 3})
    assert known == {"one": 1, "two": "2"}

    # handle_to_dict passes kvs through unchanged
    obj = A(one=8)
    kvs = {"one": 8, "two": "default"}
    assert _IgnoreUndefinedParameters.handle_to_dict(obj, kvs) is kvs

    # handle_dump contributes nothing extra to the dump
    assert _IgnoreUndefinedParameters.handle_dump(obj) == {}

# Generated at 2026-11-03 01:43:49.272363
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    # _UndefinedParameterAction.handle_from_dict is abstract and has no
    # implementation (body is just `pass`), so invoking it directly
    # returns None regardless of the arguments passed.
    class _DummyClass:
        pass

    result = _UndefinedParameterAction.handle_from_dict(
        cls=_DummyClass, kvs={"a": 1, "b": "two"})
    assert result is None

    # Also verify with an empty kvs dict
    result = _UndefinedParameterAction.handle_from_dict(cls=_DummyClass, kvs={})
    assert result is None