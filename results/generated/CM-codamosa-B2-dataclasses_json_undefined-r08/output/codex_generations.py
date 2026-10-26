

# Generated at 2026-10-25 11:38:04.283770
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

# Generated at 2026-10-25 11:38:06.698872
# Unit test for constructor of class _UndefinedParameterAction

# Generated at 2026-10-25 11:38:09.116166
# Unit test for constructor of class _UndefinedParameterAction

# Generated at 2026-10-25 11:38:11.530976
# Unit test for constructor of class _UndefinedParameterAction

# Generated at 2026-10-25 11:38:13.944937
# Unit test for method handle_from_dict of class _IgnoreUndefinedParameters

# Generated at 2026-10-25 11:38:16.360292
# Unit test for method handle_from_dict of class _IgnoreUndefinedParameters

# Generated at 2026-10-25 11:38:18.771257
# Unit test for method handle_from_dict of class _IgnoreUndefinedParameters

# Generated at 2026-10-25 11:38:21.186365
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-25 11:38:23.600240
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-25 11:38:26.015527
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-25 11:38:28.430080
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 11:38:30.845721
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 11:38:33.260301
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 11:38:35.673243
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 11:38:38.090427
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 11:38:40.503332
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 11:38:42.917983
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-25 11:38:45.332483
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-25 11:38:47.746439
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-25 11:38:50.160992
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-25 11:38:52.573938
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-25 11:38:54.988374
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-25 11:38:57.406201
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-25 11:38:59.820893
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-25 11:39:02.234562
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-25 11:39:04.648104
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:39:07.062714
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:39:09.478885
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:39:11.893251
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-25 11:39:14.307829
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-25 11:39:16.723000
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-25 11:39:18.363214
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

# Generated at 2026-10-25 11:39:19.857064
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


# Generated at 2026-10-25 11:39:21.410423
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

# Generated at 2026-10-25 11:39:23.358240
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

# Generated at 2026-10-25 11:39:24.768896
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

# Generated at 2026-10-25 11:39:47.277454
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-25 11:39:49.737416
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-25 11:39:52.151396
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-25 11:39:54.567296
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 11:39:56.985689
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 11:39:59.395469
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 11:40:02.468168
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-25 11:40:04.857011
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-25 11:40:07.271539
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-25 11:40:09.685929
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 11:40:12.100034
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 11:40:14.515898
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 11:40:16.928444
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:40:19.343294
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:40:21.757001
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:40:24.185663
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 11:40:26.599617
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 11:40:29.013284
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 11:40:31.426108
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:40:33.839335
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:40:36.252818
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:40:38.666503
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 11:40:41.081166
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 11:40:43.499082
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 11:40:45.911903
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 11:40:48.322799
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 11:40:50.737873
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 11:40:53.153745
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-25 11:40:55.568272
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-25 11:40:58.005397
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-25 11:41:00.398838
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-25 11:41:02.814940
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-25 11:41:05.229964
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-25 11:41:07.643076
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-25 11:41:10.057858
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-25 11:41:12.470541
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-25 11:41:14.885572
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:41:17.300112
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:41:19.715236
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:41:22.127270
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:41:24.539835
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:41:26.953145
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:41:29.366055
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:41:31.781083
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:41:34.196238
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:41:36.609849
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:41:39.023378
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:41:41.438677
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:41:43.881624
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-25 11:41:46.294765
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-25 11:41:48.708937
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-25 11:41:51.122512
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-25 11:41:53.538418
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-25 11:41:55.951822
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-25 11:41:58.367244
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:42:00.783940
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:42:03.198408
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:42:05.616774
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-25 11:42:08.028230
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-25 11:42:10.441963
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-25 11:42:12.855405
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 11:42:15.268761
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 11:42:17.701649
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 11:42:20.113642
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-25 11:42:22.527949
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-25 11:42:24.943678
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-25 11:42:27.371337
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 11:42:29.783550
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 11:42:32.197537
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 11:42:34.611628
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:42:37.026139
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:42:39.441588
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:42:41.865272
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 11:42:44.276810
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 11:42:46.688769
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 11:42:49.135520
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-25 11:42:51.517675
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-25 11:42:53.945193
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-25 11:42:56.358318
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-25 11:42:58.771868
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-25 11:43:01.186021
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-25 11:43:03.600109
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:43:06.013093
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:43:08.425385
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:43:10.839122
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 11:43:13.253687
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 11:43:15.669149
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 11:43:18.126490
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 11:43:20.541997
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 11:43:22.952282
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 11:43:25.367191
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-25 11:43:27.780084
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-25 11:43:30.195767
# Unit test for constructor of class UndefinedParameterError

# Generated at 2026-10-25 11:43:32.609612
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:43:35.023309
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:43:37.439568
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:43:39.859174
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 11:43:42.271699
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 11:43:44.688495
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 11:43:47.100519
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:43:49.514972
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:43:51.929683
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:43:54.343915
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:43:56.758820
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:43:59.174163
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:44:01.589369
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-25 11:44:04.005065
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-25 11:44:06.418001
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-25 11:44:08.836049
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:44:11.252365
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:44:13.664756
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:44:16.079091
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-25 11:44:18.493039
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-25 11:44:20.907475
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-25 11:44:23.324811
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-25 11:44:25.742412
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-25 11:44:28.162191
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2026-10-25 11:44:31.137551
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 11:44:33.553382
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 11:44:35.966822
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 11:44:38.382430
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 11:44:40.798080
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 11:44:43.252094
# Unit test for method handle_to_dict of class _UndefinedParameterAction

# Generated at 2026-10-25 11:44:45.641733
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 11:44:48.075455
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 11:44:50.489758
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 11:44:52.904065
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:44:55.323299
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:44:57.739799
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:45:00.153580
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:45:02.567886
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:45:10.781520
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:45:44.368216
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    result = _UndefinedParameterAction.handle_dump(obj=None)

    assert result == {}
    assert isinstance(result, dict)

# Generated at 2026-10-25 11:46:13.658451
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:46:47.446725
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:46:49.863778
# Unit test for method create_init of class _CatchAllUndefinedParameters

# Generated at 2026-10-25 11:46:52.282354
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 11:46:54.696701
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 11:46:57.110660
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters

# Generated at 2026-10-25 11:46:59.524890
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-25 11:47:01.941569
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-25 11:47:04.354992
# Unit test for method handle_dump of class _UndefinedParameterAction

# Generated at 2026-10-25 11:47:15.325978
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    import dataclasses
    @dataclasses.dataclass
    class Dummy:
        a: int
        b: str = "default"
    assert _RaiseUndefinedParameters.handle_from_dict(Dummy, {"a": 1, "b": "x"}) == {"a": 1, "b": "x"}
    assert _RaiseUndefinedParameters.handle_from_dict(Dummy, {"a": 1}) == {"a": 1}
    assert _RaiseUndefinedParameters.handle_from_dict(Dummy, {}) == {}
    try:
        _RaiseUndefinedParameters.handle_from_dict(Dummy, {"a": 1, "c": 2})
        assert False, "expected UndefinedParameterError for {'c': 2}"
    except UndefinedParameterError as e:
        assert "c" in str(e)
    try:
        _RaiseUndefinedParameters.handle_from_dict(Dummy, {"unknown": 99})
        assert False, "expected UndefinedParameterError for all-unknown input"
    except UndefinedParameterError as e:
        assert "unknown" in str(e)
    result = _RaiseUndefinedParameters.handle_from_dict(Dummy, {"a": 1, "b": "y"})
    assert "a" in result and "b" in result and len(result) == 2

# Generated at 2026-10-25 11:47:19.320236
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

# Generated at 2026-10-25 11:47:21.987177
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

# Generated at 2026-10-25 11:47:24.121723
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

# Generated at 2026-10-25 11:48:01.510284
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-25 11:48:03.929717
# Unit test for method create_init of class _IgnoreUndefinedParameters

# Generated at 2026-10-25 11:48:06.899038
# Unit test for method create_init of class _IgnoreUndefinedParameters