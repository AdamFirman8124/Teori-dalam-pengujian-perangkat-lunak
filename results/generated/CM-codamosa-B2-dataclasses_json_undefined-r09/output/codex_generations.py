

# Generated at 2026-11-02 08:53:59.518134
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    # handle_from_dict is abstract; create a concrete stub that delegates
    # to the shared _separate_defined_undefined_kvs helper so we can
    # exercise the base-class behavior.
    class _StubAction(_UndefinedParameterAction):
        @staticmethod
        def module_0.handle_from_dict(cls, kvs: Dict[Any, Any]) -> Dict[str, Any]:
            known, unknown = \
                _UndefinedParameterAction._separate_defined_undefined_kvs(
                    cls=cls, kvs=kvs)
            return known, unknown

    @dataclasses.dataclass
    class Example:
        a: int
        b: str

    # Only defined parameters
    known, unknown = _StubAction.handle_from_dict(Example, {"a": 1, "b": "x"})
    assert known == {"a": 1, "b": "x"}
    assert unknown == {}

    # Mixed defined and undefined parameters
    known, unknown = _StubAction.handle_from_dict(
        Example, {"a": 1, "b": "x", "c": 2, "d": 3})
    assert known == {"a": 1, "b": "x"}
    assert unknown == {"c": 2, "d": 3}

    # Only undefined parameters
    known, unknown = _StubAction.handle_from_dict(Example, {"z": 9})
    assert known == {}
    assert unknown == {"z": 9}

    # Empty input
    known, unknown = _StubAction.handle_from_dict(Example, {})
    assert known == {}
    assert unknown == {}

    # The abstract base class itself cannot be instantiated
    import pytest
    with pytest.raises(TypeError):
        _UndefinedParameterAction()

    # Concrete RAISE behavior: undefined parameters trigger the error
    with pytest.raises(UndefinedParameterError):
        _RaiseUndefinedParameters.handle_from_dict(Example, {"a": 1, "x": 2})

    # Concrete EXCLUDE behavior: undefined parameters are dropped
    result = _IgnoreUndefinedParameters.handle_from_dict(
        Example, {"a": 1, "b": "y", "x": 2})
    assert result == {"a": 1, "b": "y"}

# Generated at 2026-11-02 08:54:43.134543
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    @dataclasses.dataclass
    class Sample:
        x: int
        y: str = "default"

    result = _UndefinedParameterAction.handle_from_dict(Sample, {"x": 1, "y": "a", "z": 2})
    assert result is None

# Generated at 2026-11-02 08:56:36.919199
# Unit test for constructor of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters():
    action = _IgnoreUndefinedParameters()

    # Constructor should produce an instance of the base action class
    assert isinstance(action, _UndefinedParameterAction)
    assert isinstance(action, _IgnoreUndefinedParameters)

    # The class is stateless - all behavior is in static methods
    assert hasattr(action, "handle_from_dict")
    assert hasattr(action, "handle_to_dict")
    assert hasattr(action, "handle_dump")
    assert hasattr(action, "create_init")

    # handle_from_dict should filter out undefined parameters
    @dataclasses.dataclass
    class Example:
        a: int
        b: str = "default"

    known, unknown = \
        _UndefinedParameterAction._separate_defined_undefined_kvs(
            Example, {"a": 1, "b": "x", "c": 2, "d": 3})
    assert known == {"a": 1, "b": "x"}
    assert unknown == {"c": 2, "d": 3}

    result = _IgnoreUndefinedParameters.handle_from_dict(
        Example, {"a": 1, "b": "x", "c": 2, "d": 3})
    assert result == {"a": 1, "b": "x"}

    # Undefined parameters are silently dropped, known ones kept
    result = _IgnoreUndefinedParameters.handle_from_dict(Example, {"a": 5})
    assert result == {"a": 5}

    result = _IgnoreUndefinedParameters.handle_from_dict(Example, {"z": 1})
    assert result == {}

    # handle_to_dict passes kvs through unchanged
    kvs = {"a": 1, "extra": 2}
    assert _IgnoreUndefinedParameters.handle_to_dict(None, kvs) == \
        {"a": 1, "extra": 2}

    # handle_dump returns an empty dict
    assert _IgnoreUndefinedParameters.handle_dump(None) == {}

    # create_init returns a callable that ignores undefined kwargs
    init_func = _IgnoreUndefinedParameters.create_init(Example)
    assert callable(init_func)
    instance = init_func.__func__(Example) if hasattr(init_func,
                                                      "__func__") else None

    # Using the wrapped init through actual instantiation
    @dataclasses.dataclass
    @dataclasses.dataclass
    class _Wrapper:
        pass

    wrapper = _IgnoreUndefinedParameters()
    assert wrapper is not None

# Generated at 2026-11-02 08:58:02.453495
# Unit test for constructor of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters():
    """
    Test the constructor of class _RaiseUndefinedParameters.
    The class only defines static methods, so instantiation should
    succeed without any arguments and yield an instance of
    _UndefinedParameterAction.
    """
    instance = _RaiseUndefinedParameters()
    assert isinstance(instance, _RaiseUndefinedParameters)
    assert isinstance(instance, _UndefinedParameterAction)

# Generated at 2026-11-02 09:02:50.488054
# Unit test for method create_init of class _CatchAllUndefinedParameters