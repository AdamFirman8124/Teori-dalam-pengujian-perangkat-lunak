

# Generated at 2026-11-02 20:27:53.308921
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    # _UndefinedParameterAction.create_init is a static method that simply
    # returns the original __init__ of the given class.

    @dataclasses.dataclass
    class Example:
        a: int
        b: str = "default"

    original_init = Example.__init__
    returned_init = _UndefinedParameterAction.create_init(Example)

    # The returned callable must be the class' original __init__
    assert returned_init is original_init

    # The returned callable must behave like the original __init__
    instance = Example.__new__(Example)
    returned_init(instance, a=1)
    assert instance.a == 1
    assert instance.b == "default"

    # Also works for a plain (non-dataclass) class
    class Plain:
        def __init__(self, x):
            self.x = x

    plain_init = _UndefinedParameterAction.create_init(Plain)
    assert plain_init is Plain.__init__

    plain_instance = Plain.__new__(Plain)
    plain_init(plain_instance, 42)
    assert plain_instance.x == 42

# Generated at 2026-11-02 20:29:21.941090
# Unit test for method handle_dump of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_dump():
    import pytest
    from dataclasses import dataclass
    from dataclasses_json.utils import CatchAllVar

    @dataclass
    class Person:
        name: str
        catch_all: Optional[CatchAllVar] = None

    # Returns the value stored in the catch-all field
    person = Person(name="Alice", catch_all={"age": 30, "city": "Berlin"})
    result = _CatchAllUndefinedParameters.handle_dump(person)
    assert result == {"age": 30, "city": "Berlin"}

    # Returns None when the catch-all field holds no data
    person_without_extra = Person(name="Bob")
    result = _CatchAllUndefinedParameters.handle_dump(person_without_extra)
    assert result is None

    # Raises UndefinedParameterError when the class has no catch-all field
    @dataclass
    class NoCatchAll:
        name: str

    with pytest.raises(UndefinedParameterError):
        _CatchAllUndefinedParameters.handle_dump(NoCatchAll(name="Carol"))

# Generated at 2026-11-02 20:35:03.597537
# Unit test for constructor of class _CatchAllUndefinedParameters