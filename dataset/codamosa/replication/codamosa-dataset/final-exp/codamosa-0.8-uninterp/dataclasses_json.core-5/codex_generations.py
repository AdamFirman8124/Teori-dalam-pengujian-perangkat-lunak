

# Generated at 2022-06-13 19:10:02.118301
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode([1,2,3]) == "[1, 2, 3]"
    assert _ExtendedEncoder().encode({'a': 1, 'b': 2}) == '{"a": 1, "b": 2}'
    assert _ExtendedEncoder().encode(datetime.now(timezone.utc)) == '0.0'


# Generated at 2022-06-13 19:10:05.993306
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default(datetime.now()) == datetime.now().timestamp()
    assert _ExtendedEncoder().default(1.0) == 1.0
    assert _ExtendedEncoder().default(1) == 1
    assert _ExtendedEncoder().default(True) == True
    assert _ExtendedEncoder().default('qwer') == 'qwer'
    assert _ExtendedEncoder().default(UUID('70622f26-2a9e-4790-8e7f-6b2cf6b14001')).lower() == '70622f26-2a9e-4790-8e7f-6b2cf6b14001'
    assert _ExtendedEncoder().default(None) == None
    assert _ExtendedEncoder().default([]) == []
    assert _Ext

# Generated at 2022-06-13 19:10:14.064223
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default(datetime.now()) is not None
    assert _ExtendedEncoder().default(UUID('0704de9a-bf6c-4746-8cdc-f08dfeef0ad3')) is not None
    assert _ExtendedEncoder().default(Decimal('10.0')) is not None
    assert _ExtendedEncoder().default(MappingProxyType(dict(x=1))) is not None
    assert _ExtendedEncoder().default(range(10)) is not None
    assert _ExtendedEncoder().default(tuple(range(10))) is not None
    assert _ExtendedEncoder().default(frozenset(range(10))) is not None
    assert _ExtendedEncoder().default(set(range(10))) is not None
    assert _ExtendedEncoder

# Generated at 2022-06-13 19:10:23.643532
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.default(None) == None
    assert encoder.default(False) == False
    assert encoder.default(True) == True
    assert encoder.default(1) == 1
    assert encoder.default(1.0) == 1.0
    assert encoder.default("cat") == "cat"
    assert encoder.default(datetime.now(timezone.utc)) == datetime.now(timezone.utc).timestamp()
    assert encoder.default(Decimal('0.1')) == "0.1"
    assert encoder.default([1, 2]) == [1, 2]
    assert encoder.default((1, 2)) == [1, 2]
    assert encoder.default(set()) == []
    assert encoder.default

# Generated at 2022-06-13 19:10:29.116248
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(datetime(2015, 10, 16, 22, 5, 50, tzinfo=timezone.utc)) == '1445095550.0'
    assert _ExtendedEncoder().encode(UUID('d5edd010-5dfa-4444-bac7-8875d0d7ad73')) == '"d5edd010-5dfa-4444-bac7-8875d0d7ad73"'
    assert _ExtendedEncoder().encode(Decimal('123.45')) == '"123.45"'



# Generated at 2022-06-13 19:10:37.852719
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    json.dumps([1, 2, 3], cls=encoder)
    json.dumps(datetime.now(timezone.utc), cls=encoder)
    json.dumps({'name': 'John Doe'}, cls=encoder)
    json.dumps(UUID('e4ccd4f6-5b5f-4a23-ab6e-7b96db9ddcb5'), cls=encoder)
    json.dumps(Decimal('3.14'), cls=encoder)



# Generated at 2022-06-13 19:10:49.629749
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(UUID('cdc10109-a0d6-4e8e-b1c2-b937cd9bea8b')) == "\"cdc10109-a0d6-4e8e-b1c2-b937cd9bea8b\""
    assert _ExtendedEncoder().encode(datetime.fromtimestamp(1000, timezone.utc)) == "1000.0"
    assert _ExtendedEncoder().encode(Decimal("1.1")) == "\"1.1\""
    assert _ExtendedEncoder().encode(cfg.settings.MISSING_ERRORS) == '"missing"'
    assert _ExtendedEncoder().encode({'a': 1}) == "{\"a\": 1}"
    assert _ExtendedEncoder

# Generated at 2022-06-13 19:10:54.289699
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder(sort_keys=True, indent=4).encode({"a": [1, 2]}) == '{\n    "a": [\n        1,\n        2\n    ]\n}'


# Generated at 2022-06-13 19:11:10.501608
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default([1, 2]) == [1, 2]
    assert _ExtendedEncoder().default({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}
    assert json.loads(_ExtendedEncoder().encode(datetime.now(timezone.utc))) == {
        '__dataclass_json__datetime': True,
        'timestamp': datetime.now(timezone.utc).timestamp()
    }

# Generated at 2022-06-13 19:11:19.090011
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder().encode
    assert encoder([1, 2, 3]) == "[1, 2, 3]"
    assert encoder({"a": [1, 2, 3]}) == '{"a": [1, 2, 3]}'
    assert encoder({"a": [1, 2, 3]}) == '{"a": [1, 2, 3]}'
    assert encoder(set([1, 2, 3])) == "[1, 2, 3]"


# Generated at 2022-06-13 19:12:01.027499
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    assert _ExtendedEncoder().default([1, 2]) == [1, 2]
    assert _ExtendedEncoder().default((1, 2)) == [1, 2]
    assert _ExtendedEncoder().default({1: 2}) == {1: 2}
    assert _ExtendedEncoder().default(set([1, 2])) == [1, 2]
    assert _ExtendedEncoder().default(frozenset([1, 2])) == [1, 2]
    assert _ExtendedEncoder().default(bytearray([1, 2])) == [1, 2]
    assert _ExtendedEncoder().default(memoryview(b'12')) == [49, 50]
    assert _ExtendedEncoder().default(datetime(2017, 2, 3, 4, 5, 6, 7)) == 1486141906

# Generated at 2022-06-13 19:12:05.665971
# Unit test for method default of class _ExtendedEncoder

# Generated at 2022-06-13 19:12:10.764647
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    result = _ExtendedEncoder().encode(list(range(10)))
    assert result == '[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]'

    result = _ExtendedEncoder().encode(tuple(range(10)))
    assert result == '[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]'

    result = _ExtendedEncoder().encode(dict(zip(range(10), range(10))))
    assert result == '{"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}'

    result = _ExtendedEncoder().encode(set(range(10)))

# Generated at 2022-06-13 19:12:22.142477
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    json.dumps(dict(a=1), cls=_ExtendedEncoder)
    json.dumps([1], cls=_ExtendedEncoder)
    json.dumps("a", cls=_ExtendedEncoder)
    json.dumps(1, cls=_ExtendedEncoder)
    json.dumps(1e3, cls=_ExtendedEncoder)
    json.dumps(True, cls=_ExtendedEncoder)
    json.dumps(None, cls=_ExtendedEncoder)
    json.dumps(datetime(2020, 1, 1, 12, 12, 12, tzinfo=timezone.utc), cls=_ExtendedEncoder)

# Generated at 2022-06-13 19:12:32.892524
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    encoder = _ExtendedEncoder()
    assert encoder.default(1) == 1
    assert encoder.default(1.0) == 1.0
    assert encoder.default(True) == True
    assert encoder.default(False) == False
    assert encoder.default(None) == None
    assert encoder.default([]) == []
    assert encoder.default({}) == {}
    assert encoder.default({"a": 1}) == {"a": 1}
    assert encoder.default({"a": 1, "b": 2}) == {"a": 1, "b": 2}
    assert encoder.default(["a", "b", "c"]) == ["a", "b", "c"]
    assert encoder.default({"a": "b"}) == {"a": "b"}
    assert encoder

# Generated at 2022-06-13 19:12:42.370782
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.default({1: 2}) == {1: 2}
    assert encoder.default([1, 2]) == [1, 2]
    assert encoder.default(datetime.now(timezone.utc)) == datetime.now(timezone.utc).timestamp()
    assert encoder.default(UUID('f47ac10b-58cc-4372-a567-0e02b2c3d479')) == 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
    enum = cfg.LetterCase()
    assert encoder.default(enum.KEBAB) == 'kebab'
    assert encoder.default(Decimal('12.456')) == '12.456'


# Generated at 2022-06-13 19:12:46.239426
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    extendedEncoder = _ExtendedEncoder()
    assert extendedEncoder.default(Decimal('4.0')) == '4.0'
    assert extendedEncoder.default([1, 2]) == [1, 2]



# Generated at 2022-06-13 19:13:04.472767
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert json.dumps(dict(a=1), cls=_ExtendedEncoder) == '{"a": 1}'
    assert json.dumps(list(range(10)), cls=_ExtendedEncoder) == '[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]'
    assert json.dumps(datetime(2019, 1, 2, 3, 4, 5, tzinfo=timezone.utc), cls=_ExtendedEncoder) == '1546751045.0'
    assert json.dumps(datetime(2019, 1, 2, 3, 4, 5), cls=_ExtendedEncoder) == '"2019-01-02 03:04:05"'

# Generated at 2022-06-13 19:13:12.223804
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert json.dumps([1, 2, 3], cls=_ExtendedEncoder) == '[1, 2, 3]'
    assert json.dumps([[1], 23, '3'], cls=_ExtendedEncoder) == '[[1], 23, "3"]'
    assert json.dumps({'a': 1, 'b': 2, 'c': 3}, cls=_ExtendedEncoder) == '{"a": 1, "b": 2, "c": 3}'
    assert json.dumps([{'a': 1}, {'b': 2, 'c': 3}], cls=_ExtendedEncoder) == '[{"a": 1}, {"b": 2, "c": 3}]'

# Generated at 2022-06-13 19:13:16.241470
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    with warnings.catch_warnings(record=True) as w:
        result = _ExtendedEncoder()
        assert len(w) == 0
        assert result
        assert _isinstance_safe(result, _ExtendedEncoder)



# Generated at 2022-06-13 19:13:51.870404
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(dict(a=1)) == '{"a": 1}'
    assert _ExtendedEncoder().encode(list(1, 2, 3)) == '[1, 2, 3]'
    assert _ExtendedEncoder().encode(datetime(year=2020, month=8, day=11,
                                              tzinfo=timezone.utc)) == '1597190400.0'
    assert _ExtendedEncoder().encode(UUID('ef2d2bf2-d5d7-4b5c-b3f5-c44ba9d9a1e4')) == '"ef2d2bf2-d5d7-4b5c-b3f5-c44ba9d9a1e4"'
    assert _ExtendedEncoder().en

# Generated at 2022-06-13 19:13:58.093189
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    from datetime import date
    
    class OptionalTestSubclassTest(Enum):
        b = 'a'
        
    @dataclass
    class Dummy:
        a: datetime = field(default_factory=lambda: datetime(2020, 1, 1))
        b: OptionalTestSubclassTest = OptionalTestSubclassTest.b
    

    class OptionalTestSubclass(Enum):
        b = 'a'
        
    @dataclass
    class OptionalTest:
        b: OptionalTestSubclass = OptionalTestSubclass.b
        c: UUID = UUID('{12345678-1234-5678-1234-567812345678}')
        d: Decimal = Decimal(1)
        e: Collection = field(default_factory=lambda: tuple())

# Generated at 2022-06-13 19:14:03.310744
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode({}) == '{}'
    assert _ExtendedEncoder().encode([1]) == '[1]'
    assert _ExtendedEncoder().encode(datetime.now()) == '{}'
    assert _ExtendedEncoder().encode(datetime.now(timezone.utc)) == '{}'
    assert _ExtendedEncoder().encode(UUID(int=1)) == '"00000000-0000-0000-0000-000000000001"'

# Unit test:
# test if name of class _ExtendedEncoder is "ExtendedEncoder"
test__ExtendedEncoder.__name__ == "_ExtendedEncoder"


# Generated at 2022-06-13 19:14:07.130310
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    assert json.dumps(set([1, 2]), cls=_ExtendedEncoder) == '[1, 2]'
    assert json.dumps({1: 2}, cls=_ExtendedEncoder) == '{"1": 2}'



# Generated at 2022-06-13 19:14:13.836189
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    class MyClass():
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __eq__(self, o: object) -> bool:
            if not isinstance(o, MyClass):
                return False
            return self.x == o.x and self.y == o.y

    class MyClass2(MyClass):
        pass

    class MyClass3(MyClass):
        def __str__(self):
            return 'x={0}, y={1}'.format(self.x, self.y)

    class ABC(Enum):
        ALPHA = 1,
        BETA  = 2,

    class ABC1(MyClass):
        pass

    class ABC2(Enum):
        ALPHA = MyClass1(1, 2)
        BETA 

# Generated at 2022-06-13 19:14:23.140330
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    example1 = (
        _ExtendedEncoder(indent=2).encode({"a": {"b": [1, 2, 3], "c": 4}},
                                          bytearray) ==
        b'{\n  "a": {\n    "b": [\n      1,\n      2,\n      3\n    ],\n '
        b'"c": 4\n  }\n}'
    )
    example2 = (
        _ExtendedEncoder(indent=2).encode({"a": {"b": [1, 2, 3], "c": 4}},
                                          bytearray)[:4] ==
        b'{\n  '
    )

# Generated at 2022-06-13 19:14:30.561730
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    import json
    import datetime
    import uuid
    import enum
    import decimal
    sut = _ExtendedEncoder()
    # No type checking
    assert isinstance(sut.default([]), list)
    assert isinstance(sut.default({}), dict)
    assert isinstance(sut.default(None), type(None))
    assert isinstance(sut.default(True), bool)
    assert isinstance(sut.default(1), int)
    assert isinstance(sut.default(1.1), float)
    assert isinstance(sut.default('a'), str)
    assert isinstance(sut.default(datetime.datetime.now()), float)
    assert isinstance(sut.default(datetime.datetime.now(timezone.utc)), float)

# Generated at 2022-06-13 19:14:36.989665
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(dict(a=1)) == '{"a": 1}'
    assert _ExtendedEncoder().encode([1]) == '[1]'
    dt = datetime.now(timezone.utc)
    assert _ExtendedEncoder().encode(dt) == str(dt.timestamp())
    assert _ExtendedEncoder().encode(UUID('7d9afaf8-a7b0-4739-9e27-a11b0d6cbf23')) == '7d9afaf8-a7b0-4739-9e27-a11b0d6cbf23'
    assert _ExtendedEncoder().encode(Decimal('1.1')) == '1.1'

# Generated at 2022-06-13 19:14:43.016306
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder.default != json.JSONEncoder.default
    o = json.dumps({"a": 1, "b": 2.0, "c": None, "d": True},
                cls=_ExtendedEncoder)
    assert o == '{"a": 1, "b": 2.0, "c": null, "d": true}'


# Generated at 2022-06-13 19:14:48.226216
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode([datetime.now()])
    assert _ExtendedEncoder().encode(["1", "2"])
    assert _ExtendedEncoder().encode({"1": "2"})
    assert _ExtendedEncoder().encode(EnumMember("1"))
    assert _ExtendedEncoder().encode(Decimal("123.456"))


# Generated at 2022-06-13 19:15:46.357776
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(None) == 'null'
    assert _ExtendedEncoder().encode(True) == 'true'
    assert _ExtendedEncoder().encode(False) == 'false'
    assert _ExtendedEncoder().encode(1) == '1'
    assert _ExtendedEncoder().encode(1.0) == '1.0'
    assert _ExtendedEncoder().encode('string') == '"string"'
    assert _ExtendedEncoder().encode([1, 2, 3]) == '[1, 2, 3]'
    assert _ExtendedEncoder().encode({'a': 1, 'b': 2}) == '{"a": 1, "b": 2}'


# Generated at 2022-06-13 19:15:48.363561
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(datetime.now())



# Generated at 2022-06-13 19:15:55.910493
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert json.dumps(dict(a=1, b=2), cls=_ExtendedEncoder) == '{"a": 1, "b": 2}'
    assert json.dumps([1, 2], cls=_ExtendedEncoder) == '[1, 2]'
    assert json.dumps(1, cls=_ExtendedEncoder) == '1'
    assert json.dumps('a', cls=_ExtendedEncoder) == '"a"'
    assert json.dumps(1.2, cls=_ExtendedEncoder) == '1.2'
    assert json.dumps(None, cls=_ExtendedEncoder) == 'null'
    assert json.dumps(True, cls=_ExtendedEncoder) == 'true'


# Generated at 2022-06-13 19:15:57.303657
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert isinstance(_ExtendedEncoder(), json.JSONEncoder)



# Generated at 2022-06-13 19:16:00.150961
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert isinstance(_ExtendedEncoder(), json.JSONEncoder)
    assert _ExtendedEncoder().encode({"a":1}) == '{"a": 1}'

# Test for decorator funciton 'dec_encode_with'

# Generated at 2022-06-13 19:16:06.752865
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    e = _ExtendedEncoder()
    assert e.default({1: 2}) == {1: 2}
    assert e.default(set([1])) == [1]
    assert e.default([1, 2]) == [1, 2]
    # TODO: test datetime
    # TODO: test UUID
    # TODO: test Enum
    # TODO: test Decimal



# Generated at 2022-06-13 19:16:11.374176
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    # Extended encoder should handle decimal type
    assert encoder.encode(Decimal('1.0')) == '"1.0"'
    # Extended encoder should not handle uuid type
    try:
        encoder.encode(UUID('be93c9f0-6d2c-4686-a73a-a2af7de10d2a'))
        assert False, 'Error: above line should have thrown an exception.'
    except TypeError:
        pass



# Generated at 2022-06-13 19:16:16.735241
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(1) == '1'
    assert _ExtendedEncoder().encode({'a': 'b'}) == '{"a": "b"}'
    assert _ExtendedEncoder().encode([1, 2, {3: '3'}]) == '[1, 2, {"3": "3"}]'
    assert _ExtendedEncoder().encode(['1', '2']) == '["1", "2"]'
    assert _ExtendedEncoder().encode(True) == 'true'
    assert _ExtendedEncoder().encode(False) == 'false'
    assert _ExtendedEncoder().encode(None) == 'null'
    assert _ExtendedEncoder().encode(5.5) == '5.5'

# Generated at 2022-06-13 19:16:18.722076
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder(indent=2)
    result = encoder.default(UUID('123e4567-e89b-12d3-a456-426655440000'))
    assert result == '123e4567-e89b-12d3-a456-426655440000'



# Generated at 2022-06-13 19:16:20.647764
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    # noinspection PyStatementEffect
    ExtendedEncoder = _ExtendedEncoder


# Generated at 2022-06-13 19:17:04.217879
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    # create dummy objects
    dummy_obj = object()
    dummy_set = {1, 2, 3}
    dummy_list = [4, 5, 6]
    dummy_mapping = {
        'a' : 7,
        'b' : 8,
        'c' : 9
    }
    dummy_datetime = datetime(2020, 11, 15, tzinfo = timezone.utc)
    dummy_uuid = UUID(hex = '0b6a9f0d435d4cb5a5e5e499287a085f')
    dummy_enum = cfg.LetterCase.CAPITALIZED
    dummy_decimal = Decimal(3.14)
    # test for dummy_obj
    encoder = _ExtendedEncoder()

# Generated at 2022-06-13 19:17:11.169718
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default(MISSING) is MISSING
    assert _ExtendedEncoder().default(None) is None
    assert _ExtendedEncoder().default(True) is True
    assert _ExtendedEncoder().default(False) is False
    assert _ExtendedEncoder().default(float('nan')) is None
    assert _ExtendedEncoder().default(float('inf')) is None



# Generated at 2022-06-13 19:17:24.838400
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    assert _ExtendedEncoder().default(True) == True
    assert _ExtendedEncoder().default(False) == False
    assert _ExtendedEncoder().default(1) == 1
    assert _ExtendedEncoder().default(1.23) == 1.23
    assert _ExtendedEncoder().default(None) == None
    assert _ExtendedEncoder().default("abc") == "abc"
    assert _ExtendedEncoder().default([1, 2, 3]) == [1, 2, 3]
    assert _ExtendedEncoder().default({1, 2, 3}) == [1, 2, 3]
    assert _ExtendedEncoder().default({"a": 1, "b": 2}) == {"a": 1, "b": 2}

# Generated at 2022-06-13 19:17:26.226084
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(Decimal('3.14')) == '"3.14"'


# Generated at 2022-06-13 19:17:37.673353
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.default(list(range(10))) == list(range(10))
    assert encoder.default({"foo": "bar", 1: [1, 2, 3]}) == {"foo": "bar", '1': [1, 2, 3]}
    assert encoder.default(datetime.now(timezone.utc)) == datetime.now(timezone.utc).timestamp()
    assert encoder.default(UUID('1acbacf6-2c6c-11e9-939b-a95d0bf6fb5e')) == '1acbacf6-2c6c-11e9-939b-a95d0bf6fb5e'

# Generated at 2022-06-13 19:17:41.416979
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert json.dumps(b'foo', cls=_ExtendedEncoder) == '"foo"'
    assert json.dumps(datetime.now(timezone.utc), cls=_ExtendedEncoder) != '"foo"'
    assert json.dumps(Enum('MyEnum', 'foo'), cls=_ExtendedEncoder) == '"foo"'


# Generated at 2022-06-13 19:17:53.702996
# Unit test for constructor of class _ExtendedEncoder

# Generated at 2022-06-13 19:17:58.930109
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default([1,2]) == [1,2]
    assert _ExtendedEncoder().default({"a":1, "b":2}) == {"a":1, "b":2}
    assert _ExtendedEncoder().default(UUID('12345678123456781234567812345678')) == '12345678-1234-5678-1234-567812345678'
    assert _ExtendedEncoder().default(datetime(1970, 1, 1, 0, 0, 0, tzinfo=timezone.utc)) == 0
    assert _ExtendedEncoder().default(Enum('test', 'a b c')) == 'a'
    assert _ExtendedEncoder().default(Decimal('0.1')) == '0.1'


# Generated at 2022-06-13 19:18:05.949414
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert json.dumps({datetime(2020, 1, 1): 123}, cls=_ExtendedEncoder) == '{"2020-01-01T00:00:00": 123}'
    assert json.dumps({UUID('id'*8): 123}, cls=_ExtendedEncoder) == '{"11111111-1111-1111-1111-111111111111": 123}'
    assert json.dumps({Decimal(1): 123}, cls=_ExtendedEncoder) == '{"1": 123}'
    assert json.dumps({"Hello": "World"}, cls=_ExtendedEncoder) == '{"Hello": "World"}'


# Generated at 2022-06-13 19:18:12.364066
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    my_datetime = datetime(1952, 3, 11, 2, 15, 0, 0, tzinfo=timezone.utc)
    my_uuid = UUID(
        '{148fecbf-b6c7-4e0b-9b1d-136007c56ccd}')
    my_decimal = Decimal('12.34')
    class my_enum(Enum):
        one = 'ONE'
    my_col = [my_datetime, my_uuid, my_enum.one, my_decimal]
    encoder = _ExtendedEncoder()
    res = encoder.default(my_col)