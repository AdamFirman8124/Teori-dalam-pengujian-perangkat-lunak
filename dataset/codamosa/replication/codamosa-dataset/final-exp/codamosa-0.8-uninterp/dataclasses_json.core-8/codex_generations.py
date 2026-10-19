

# Generated at 2022-06-13 19:09:58.685190
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode({"a": 1}) == '{"a": 1}'



# Generated at 2022-06-13 19:10:07.345968
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    """
    Unit test for method default of class _ExtendedEncoder
    """
    obj_to_test = _ExtendedEncoder()
    json_str = obj_to_test.encode([datetime.now()])
    assert isinstance(json_str, str)
    json_str = obj_to_test.encode([{'foo': ('bar',)}])
    assert isinstance(json_str, str)
    json_str = obj_to_test.encode([Enum('TestEnum', {'FOO': 'foo'})])
    assert isinstance(json_str, str)
    json_str = obj_to_test.encode([Decimal(1)])
    assert isinstance(json_str, str)

# Generated at 2022-06-13 19:10:17.561196
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    from unittest.mock import patch

    assert _ExtendedEncoder().default(MISSING) is None

    with patch('dataclasses_json.converter._ExtendedEncoder.default') as mock_encoder_default_func:
        encoder = _ExtendedEncoder()
        decoder = json.JSONDecoder()

        assert encoder.default(None) == decoder.decode(encoder.encode(None))
        assert encoder.default(True) == decoder.decode(encoder.encode(True))
        assert encoder.default(1) == decoder.decode(encoder.encode(1))
        assert encoder.default(1.0) == decoder.decode(encoder.encode(1.0))

# Generated at 2022-06-13 19:10:22.911248
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode({1, 2, 3}) == '{1, 2, 3}'
    assert _ExtendedEncoder().encode({1: 1, 2: 2, 3: 3}) == '{"1": 1, "2": 2, "3": 3}'
    assert _ExtendedEncoder().encode(datetime.now(tz=timezone.utc)) == '{}'
    



# Generated at 2022-06-13 19:10:29.978884
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    from datetime import date
    assert _ExtendedEncoder().encode(
        {'a': 1, 'b': [3, 4], 'c': {'d': 5, 'e': {'f': 6}}}) == json.dumps(
        {'a': 1, 'b': [3, 4], 'c': {'d': 5, 'e': {'f': 6}}})

# Generated at 2022-06-13 19:10:34.431503
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    from decimal import Decimal
    from enum import Enum
    from uuid import UUID
    from dataclasses_json._utils import _isinstance_safe
    from dataclasses import dataclass

    class Color(Enum):
        WHITE = '#ffffff'
        BLACK = '#000000'
        YELLOW = '#ffff00'

    @dataclass
    class DictData:
        l: list
        t: tuple
        d: dict

    @dataclass
    class Foo:
        uuid: UUID
        dt: datetime
        dec: Decimal
        color: Color
        dd: DictData

    @dataclass
    class Bar:
        foo: Foo


# Generated at 2022-06-13 19:10:38.402490
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    o = UUID('3d3f2fc1-460b-49f9-9bbd-0a0b945eb89e')
    j = json.dumps(o, cls=_ExtendedEncoder)
    assert '3d3f2fc1-460b-49f9-9bbd-0a0b945eb89e' == j

ENCODER = _ExtendedEncoder()



# Generated at 2022-06-13 19:10:50.167494
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    def _test(obj, expected, **kwargs) -> None:
        encoder = _ExtendedEncoder(**kwargs)
        assert encoder.default(obj) == expected

    _test(datetime.utcnow(), json.dumps(datetime.utcnow().timestamp()), sort_keys=True)
    _test([1, 2], [1, 2])
    _test(set([1, 2]), [1, 2])
    _test({"a": 1}, {"a": 1})
    _test({1, 1}, [1])
    _test((1, 2), [1, 2])
    dt = datetime.fromtimestamp(100, timezone.utc)
    _test(dt, json.dumps(100))

# Generated at 2022-06-13 19:10:57.129773
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    assert _ExtendedEncoder().encode({'a':1, 'b':2}) == '{"a": 1, "b": 2}'
    assert _ExtendedEncoder().encode(set([1,2,3])) == '[1, 2, 3]'
    assert _ExtendedEncoder().encode([1,2,3]) == '[1, 2, 3]'
    assert _ExtendedEncoder().encode(True) == 'true'
    assert _ExtendedEncoder().encode(1) == '1'
    assert _ExtendedEncoder().encode(Decimal('33.5')) == '"33.5"'
    assert _ExtendedEncoder().encode(datetime.now(timezone.utc)) == 'null'


# Generated at 2022-06-13 19:11:11.440868
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default([1, 2, 3]) == [1, 2, 3]
    assert _ExtendedEncoder().default(tuple([1, 2, 3])) == [1, 2, 3]
    assert _ExtendedEncoder().default(set([1, 2, 3])) == [1, 2, 3]
    assert _ExtendedEncoder().default({'a': 1, 'b': 2, 'c': 3}) == {'a': 1, 'b': 2, 'c': 3}
    assert _ExtendedEncoder().default(datetime.now(tz=timezone.utc)) == 1474147994

# Generated at 2022-06-13 19:11:43.349456
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    encoder = _ExtendedEncoder()
    assert encoder.default(3) == 3
    assert encoder.default(3.8) == 3.8
    assert encoder.default('test') == 'test'
    assert encoder.default(None) == None
    assert encoder.default([1, 2, 3]) == [1, 2, 3]
    assert encoder.default(dict(foo='bar')) == dict(foo='bar')
    assert encoder.default(set([1, 2, 3])) == [1, 2, 3]
    assert encoder.default(datetime(2018, 3, 8, 14, 17, 3)) == 1520505823.0

# Generated at 2022-06-13 19:11:50.013169
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(set()) == "[]"
    assert _ExtendedEncoder().encode({}) == "{}"
    assert _ExtendedEncoder().encode([1, 2]) == "[1, 2]"
    assert _ExtendedEncoder().encode(['a', 'b']) == '["a", "b"]'
    assert _ExtendedEncoder().encode({"a": 1, "b": 2}) == '{"a": 1, "b": 2}'
    assert _ExtendedEncoder().encode(1) == '1'
    assert _ExtendedEncoder().encode(True) == 'true'
    assert _ExtendedEncoder().encode(False) == 'false'
    assert _ExtendedEncoder().encode(None) == 'null'
    assert _ExtendedEncoder().en

# Generated at 2022-06-13 19:12:00.173257
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    e = _ExtendedEncoder()
    assert e.encode({'a': [1, 2, 3]}) == '{"a": [1, 2, 3]}'
    assert e.encode(set([1, 2, 3])) == '[1, 2, 3]'
    assert e.encode([1, 2, 3]) == '[1, 2, 3]'
    assert e.encode({1, 2, 3}) == '[1, 2, 3]'
    assert e.encode(list({1, 2, 3})) == '[1, 2, 3]'
    assert e.encode(dict({'a': 1, 'b': 2, 'c': 3})) == '{"a": 1, "c": 3, "b": 2}'
    assert e.encode(dict(zip('abc', range(1, 4))))

# Generated at 2022-06-13 19:12:07.955784
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    # type: () -> None
    """
    :return:
    """
    assert _ExtendedEncoder().default(1.2) == 1.2
    assert _ExtendedEncoder().default("s") == "s"
    assert _ExtendedEncoder().default(True) == True
    assert _ExtendedEncoder().default(False) == False
    assert _ExtendedEncoder().default(None) == None

    assert _ExtendedEncoder().default([]) == []
    assert _ExtendedEncoder().default(tuple()) == []
    assert _ExtendedEncoder().default(range(0)) == []
    assert _ExtendedEncoder().default(range(3)) == [0, 1, 2]
    assert _ExtendedEncoder().default({"a": 1}) == {"a": 1}
    assert _ExtendedEncoder

# Generated at 2022-06-13 19:12:11.844998
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(datetime.now().replace(tzinfo=timezone.utc)) == json.JSONEncoder().encode(datetime.now().replace(tzinfo=timezone.utc).timestamp())


# Generated at 2022-06-13 19:12:14.814060
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    # test constructor of class _ExtendedEncoder
    json.JSONEncoder()
    _ExtendedEncoder()


# Generated at 2022-06-13 19:12:23.782786
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.default(datetime.now()) == datetime.now().timestamp()
    assert encoder.default(datetime.now(timezone.utc)) == datetime.now(timezone.utc).timestamp()
    assert encoder.default(UUID('2f7ccd9a-2e7a-4b28-8b63-aabd0c7e3b3a')) == '2f7ccd9a-2e7a-4b28-8b63-aabd0c7e3b3a'
    # Unit test for class Enum. This is just a sample
    class Color(Enum):
        RED = 1
        GREEN = 2
        BLUE = 3
    assert encoder.default(Color.RED) == 1

# Generated at 2022-06-13 19:12:33.907295
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    a = [1, 2, 3, [4, 5], 6]
    result = json.dumps(a, cls=_ExtendedEncoder)
    assert result == json.dumps(a)

    a = {1: [2, 3, 4], 5: [6, 7, 8]}
    result = json.dumps(a, cls=_ExtendedEncoder)
    assert result == json.dumps(a)

    a = datetime.fromtimestamp(100, timezone.utc)
    result = json.dumps(a, cls=_ExtendedEncoder)
    assert result == json.dumps(a.timestamp())

    a = UUID('00000000-0000-0000-0000-000000000001')
    result = json.dumps(a, cls=_ExtendedEncoder)

# Generated at 2022-06-13 19:12:42.825701
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    json_encoder = _ExtendedEncoder()
    assert(json_encoder.default({"a":1}) == {"a":1})
    assert(json_encoder.default([1,2,4]) == [1,2,4])
    assert(json_encoder.default({1,2,4}) == [1,2,4])
    assert(json_encoder.default(datetime.now(tz=timezone.utc)) == datetime.now(tz=timezone.utc).timestamp())
    assert(json_encoder.default(UUID('002d2725-6bb1-46fe-b6c0-96db2b6f33c6')) == '002d2725-6bb1-46fe-b6c0-96db2b6f33c6')

# Generated at 2022-06-13 19:12:52.424354
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert '"Foo"' == json.dumps('Foo', cls=_ExtendedEncoder)
    assert '3.3' == json.dumps(3.3, cls=_ExtendedEncoder)
    assert '123' == json.dumps(123, cls=_ExtendedEncoder)
    assert '123' == json.dumps(123.0, cls=_ExtendedEncoder)
    assert 'true' == json.dumps(True, cls=_ExtendedEncoder)
    assert 'false' == json.dumps(False, cls=_ExtendedEncoder)
    assert 'null' == json.dumps(None, cls=_ExtendedEncoder)


# Generated at 2022-06-13 19:13:20.013331
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    encoder = _ExtendedEncoder()
    assert '[1, 2, 3]' == json.dumps([1, 2, 3], cls=encoder)
    assert '{"a": 1, "b": 2}' == json.dumps({'a': 1, 'b': 2}, cls=encoder)
    assert '"2020-01-01T00:00:00+00:00"' == json.dumps(datetime(2020, 1, 1), cls=encoder)
    assert '"deadbeef-dead-dead-beef-deaddeadbeef"' == json.dumps(UUID('deadbeef-dead-dead-beef-deaddeadbeef'), cls=encoder)
# end test__ExtendedEncoder_default



# Generated at 2022-06-13 19:13:23.433954
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():  # type: ignore
    _ExtendedEncoder().default(datetime.now())

_extended_encoder = _ExtendedEncoder()



# Generated at 2022-06-13 19:13:34.504082
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default(10) == 10
    assert _ExtendedEncoder().default(None) is None
    assert _ExtendedEncoder().default(True) is True
    assert _ExtendedEncoder().default(False) is False
    assert _ExtendedEncoder().default({}) == {}
    assert _ExtendedEncoder().default([]) == []
    assert _ExtendedEncoder().default(datetime.now()) == 1558361602
    assert _ExtendedEncoder().default(UUID('05c1db45-a0ca-4c06-a420-55a8cf6b9bec')) == '05c1db45-a0ca-4c06-a420-55a8cf6b9bec'

# Generated at 2022-06-13 19:13:42.865287
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    import uuid
    from datetime import datetime
    from decimal import Decimal
    from enum import Enum
    class TestEnum(Enum):
        A = 0
    assert _ExtendedEncoder().encode(dict(a=1)) == '{"a": 1}'
    assert _ExtendedEncoder().encode(list(range(5))) == '[0, 1, 2, 3, 4]'
    assert _ExtendedEncoder().encode(uuid.uuid4()) == str(uuid.uuid4())
    assert _ExtendedEncoder().encode(TestEnum.A) == '0'
    assert _ExtendedEncoder().encode(datetime(2020, 1, 1, tzinfo=timezone.utc)) == '1577836800.0'
    assert _ExtendedEncoder().encode

# Generated at 2022-06-13 19:13:49.103696
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(UUID('6e8bc430-9c3a-11d9-9669-0800200c9a66')) == '"6e8bc430-9c3a-11d9-9669-0800200c9a66"'
    assert _ExtendedEncoder().encode(datetime(2020, 7, 4, 12, 34, 56, tzinfo=timezone.utc)) == '1593992896.0'
    assert _ExtendedEncoder().encode({'a': 'b', 'c': 'd'}) == '{"a": "b", "c": "d"}'



# Generated at 2022-06-13 19:13:53.493518
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    encoder = _ExtendedEncoder()
    assert encoder.default(set([1])) == [1]
    assert encoder.default({1: 2}) == {1: 2}
    assert encoder.default(datetime(2020, 1, 1)) == 1577836800.0
    assert encoder.default(UUID('f47ac10b-58cc-4372-a567-0e02b2c3d479')) == 'f47ac10b-58cc-4372-a567-0e02b2c3d479'



# Generated at 2022-06-13 19:13:59.225747
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode([1, 2, 3]) == "[1, 2, 3]"
    assert _ExtendedEncoder().encode({'a': 1, 'b': 2}) == '{"a": 1, "b": 2}'
    assert _ExtendedEncoder().encode({1, 2, 2}) == '[1, 2]'
    assert _ExtendedEncoder().encode(datetime(2019, 1, 1,
                                              tzinfo=timezone.utc)) == '1546300800.0'
    assert _ExtendedEncoder().encode(UUID('c18b1534-f196-4f96-a79a-e2b6982485af')) == '"c18b1534-f196-4f96-a79a-e2b6982485af"'
   

# Generated at 2022-06-13 19:14:08.108671
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    extended_encoder = _ExtendedEncoder()
    result = extended_encoder.default(["a", "list"])
    assert result == ["a", "list"]

    result = extended_encoder.default({"a": "dict"})
    assert result == {"a": "dict"}

    result = extended_encoder.default(datetime.now())
    assert result is not None

    result = extended_encoder.default(UUID("8c9897e5-23d5-4e7b-8789-4516d3b77090"))
    assert result == "8c9897e5-23d5-4e7b-8789-4516d3b77090"

    result = extended_encoder.default(Decimal("1.1"))
    assert result == "1.1"

#T

# Generated at 2022-06-13 19:14:14.068048
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default([]) == []
    assert _ExtendedEncoder().default({}) == {}
    assert _ExtendedEncoder().default(0.0) == 0.0
    assert _ExtendedEncoder().default(1.0) == 1.0
    assert _ExtendedEncoder().default('hi') == 'hi'
    assert _ExtendedEncoder().default(True) == True
    assert _ExtendedEncoder().default(False) == False
    assert _ExtendedEncoder().default(None) == None
    assert _ExtendedEncoder().default(UUID('d15a5133-c539-4d86-a668-c2b486499f71')) == 'd15a5133-c539-4d86-a668-c2b486499f71'

# Generated at 2022-06-13 19:14:16.019620
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    result = _ExtendedEncoder().default(datetime.now())
    assert result is not None


# Generated at 2022-06-13 19:14:45.242688
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    extended_encoder = _ExtendedEncoder()
    test_dict = extended_encoder.default({'a': 1, 'b': 2})
    assert test_dict == {'a': 1, 'b': 2}
    test_list = extended_encoder.default([1, 2, 3, 4, 5])
    assert test_list == [1, 2, 3, 4, 5]
    test_str = extended_encoder.default('abc')
    assert test_str == 'abc'
    test_int = extended_encoder.default(123)
    assert test_int == 123
    test_float = extended_encoder.default(1.234)
    assert test_float == 1.234
    test_bool = extended_encoder.default(True)
    assert test_bool is True
    test_none = extended

# Generated at 2022-06-13 19:14:54.283010
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    from datetime import date
    from decimal import Decimal
    from uuid import uuid4
    from enum import Enum

    class MyEnum(Enum):
        A = 'a'
        B = 'b'


# Generated at 2022-06-13 19:15:01.026483
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    extended_encoder = _ExtendedEncoder()

    assert extended_encoder.default([1, 2, 3]) == [1, 2, 3]
    assert extended_encoder.default({'a': 1}) == {'a': 1}
    assert extended_encoder.default({'a': {'b': 1}}) == {'a': {'b': 1}}

    dt = datetime(2018, 11, 10, tzinfo=timezone.utc)
    assert extended_encoder.default(dt) == 1541824400.0

    uuid = UUID('bff87670-aa20-413c-9f11-4888a8f3a0f3')

# Generated at 2022-06-13 19:15:02.737382
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode({"a": datetime.now()})



# Generated at 2022-06-13 19:15:10.524724
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    e = _ExtendedEncoder()
    assert e.default([1, 2]) == [1, 2]
    assert e.default({"a": 1, "b": 2}) == {"a": 1, "b": 2}
    assert e.default("abcd") == "abcd"
    assert e.default(4) == 4
    assert e.default(4.0) == 4.0
    assert e.default(True) == True
    assert e.default(None) == None
    d = datetime.fromtimestamp(1546410714)
    assert e.default(d) == 1546410714
    assert e.default(UUID("12345678123456781234567812345678")) == "12345678-1234-5678-1234-567812345678"

# Generated at 2022-06-13 19:15:15.167265
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.default(True) == True
    assert encoder.default(False) == False
    assert encoder.default(None) == None
    assert encoder.default(1) == 1
    assert encoder.default(1.234) == 1.234
    assert encoder.default(1 + 1j) == '1+1j'
    assert encoder.default('string') == 'string'
    assert encoder.default([1, 2, '3']) == [1, 2, '3']
    assert encoder.default({'1':1, '2':2}) == {'1':1, '2':2}
    assert encoder.default(datetime.now(timezone.utc)) == datetime.now(timezone.utc).timestamp()
   

# Generated at 2022-06-13 19:15:26.758886
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode([1, 2]) == '[1, 2]'
    assert _ExtendedEncoder().encode({'a': 1}) == '{"a": 1}'
    assert _ExtendedEncoder().encode([1, 2]) == '[1, 2]'
    assert _ExtendedEncoder().encode(set([1, 2])) == '[1, 2]'
    assert _ExtendedEncoder().encode(frozenset([1, 2])) == '[1, 2]'
    assert _ExtendedEncoder().encode(tuple([1, 2])) == '[1, 2]'
    assert _ExtendedEncoder().encode(datetime.now()) == '1578465984.8730142'

# Generated at 2022-06-13 19:15:31.854769
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    assert _ExtendedEncoder().default(dict()) == {}
    assert _ExtendedEncoder().default(set()) == []
    assert _ExtendedEncoder().default(set([1])) == [1]
    assert _ExtendedEncoder().default(datetime(2020, 4, 7, 19, 12, 58, 782000, timezone.utc)) == 1586280378.782001
    assert _ExtendedEncoder().default(UUID('{12345678-1234-1234-1234-123456789012}')) == '12345678-1234-1234-1234-123456789012'
    assert _ExtendedEncoder().default(Decimal('0.123456789')) == '0.123456789'

# Generated at 2022-06-13 19:15:38.575517
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    result: Json = _ExtendedEncoder().default(MappingProxyType({'a': 'b'}))
    assert result == {'a': 'b'}
    result = _ExtendedEncoder().default(OrderedDict([('a', 'b')]))
    assert result == {'a': 'b'}
    result = _ExtendedEncoder().default(datetime.now(timezone.utc))
    assert isinstance(result, float)
    result = _ExtendedEncoder().default(UUID('4e7668fe-b4aa-4f8b-8138-ff238829be24'))
    assert result == '4e7668fe-b4aa-4f8b-8138-ff238829be24'

# Generated at 2022-06-13 19:15:47.238044
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode({'test': {'a': 1, 'b': 2}, 'test1': [1, 2, 3], 'test2': set([3, 2, 1])}) == '{"test": {"a": 1, "b": 2}, "test1": [1, 2, 3], "test2": [3, 2, 1]}'
    assert _ExtendedEncoder().encode(['a', 'b']) == '["a", "b"]'
    assert _ExtendedEncoder().encode({'a': 1, 'b': 2}) == '{"a": 1, "b": 2}'
    assert _ExtendedEncoder().encode(set([1, 2, 3])) == '[1, 2, 3]'

# Generated at 2022-06-13 19:16:32.614718
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    _ExtendedEncoder()



# Generated at 2022-06-13 19:16:33.611353
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    _ExtendedEncoder()


# Generated at 2022-06-13 19:16:38.769222
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode({{'a': [1, 2, True]}}) == '{"a": [1, 2, true]}'
    assert json.loads(_ExtendedEncoder().encode({{'a': datetime.now()}})) == '{"a": %f}' % int(datetime.now().timestamp())
    assert json.loads(_ExtendedEncoder().encode({{'a': Decimal('1.1')}})) == '{"a": "1.1"}'

# Generated at 2022-06-13 19:16:46.687377
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode([{'b': 2, 'a': 1}, {'b': 2, 'a': 1}]) == '[{"b": 2, "a": 1}, {"b": 2, "a": 1}]'
    assert _ExtendedEncoder().encode(['a', 'b']) == '["a", "b"]'
    assert _ExtendedEncoder().encode({'b': 2, 'a': 1}) == '{"b": 2, "a": 1}'
    assert _ExtendedEncoder().encode(1) == '1'
    assert _ExtendedEncoder().encode(2.2) == '2.2'
    assert _ExtendedEncoder().encode(True) == 'true'
    assert _ExtendedEncoder().encode(False) == 'false'

# Generated at 2022-06-13 19:16:59.855287
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(set([1, 2, 3])) == "[1, 2, 3]"
    assert _ExtendedEncoder().encode(tuple([1, 2, 3])) == "[1, 2, 3]"
    assert _ExtendedEncoder().encode(range(3)) == "[0, 1, 2]"
    assert _ExtendedEncoder().encode({1: 2, 3: 4}) == '{"1": 2, "3": 4}'
    assert _ExtendedEncoder().encode(timezone.utc) == '"UTC"'
    assert _ExtendedEncoder().encode(datetime.now(timezone.utc)) == str(datetime.now(timezone.utc).timestamp())

# Generated at 2022-06-13 19:17:02.750932
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode([1, 2, 3]) == "[1, 2, 3]"
    assert _ExtendedEncoder().encode({1: 'one', 2: 'two'}) == "{\"1\": \"one\", \"2\": \"two\"}"



# Generated at 2022-06-13 19:17:08.768849
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    from datetime import timedelta
    from dataclasses import dataclass
    from enum import IntEnum, unique

    @dataclass
    class ClassA:
        name: str
        value: int
        flag: bool
    class ClassB:
        def __init__(self, name: str, value: int, flag: bool) -> None:
            self.name = name
            self.value = value
            self.flag = flag
    class ClassC:
        def __init__(self, name: str, value: int) -> None:
            self.name = name
            self.value = value
        def __eq__(self, other):
            return self.name == other.name and self.value == other.value
        def __hash__(self):
            return hash(self.name) ^ hash(self.value)

# Generated at 2022-06-13 19:17:15.300347
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.default(True) == True
    assert encoder.default(1) == 1
    assert encoder.default(1.0) == 1.0
    assert encoder.default('a') == 'a'
    assert encoder.default(
        datetime(year=2019, month=5, day=1, hour=5, minute=0, second=0, tzinfo=timezone.utc)) == 1556759600.0
    assert encoder.default(UUID('f47ac10b-58cc-4372-a567-0e02b2c3d479')) == 'f47ac10b-58cc-4372-a567-0e02b2c3d479'



# Generated at 2022-06-13 19:17:27.547109
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    # test collection
    assert _ExtendedEncoder().default(tuple(range(3))) == [0,1,2]
    assert _ExtendedEncoder().default(set(range(3))) == [0, 1, 2]
    assert _ExtendedEncoder().default(range(3)) == [0, 1, 2]

    # test mapping
    assert _ExtendedEncoder().default({k: k + 1 for k in range(3)}) == {
        "0": 1,
        "1": 2,
        "2": 3
    }

    # test datetime
    assert _ExtendedEncoder().default(
        datetime(1970, 1, 1, 0, 0, 0, tzinfo=timezone.utc)) == 0.0

# Generated at 2022-06-13 19:17:33.601306
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.default(True) == True
    assert encoder.default(100) == 100
    assert encoder.default(100.0) == 100.0
    assert encoder.default('abc') == 'abc'
    assert encoder.default('中文') == '中文'
    assert encoder.default(None) == None
    assert encoder.default([1, 2, 3]) == [1, 2, 3]
    assert encoder.default((1, 2, 3)) == [1, 2, 3]
    assert encoder.default({'abc': 123}) == {'abc': 123}
    assert encoder.default({'abc': 123}) == {'abc': 123}
    now = datetime.now(timezone.utc)

# Generated at 2022-06-13 19:18:45.491950
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    e = _ExtendedEncoder()
    assert e.default([1, '2']) == [1, '2']
    assert e.default({'a': 1}) == {'a': 1}
    assert abs(e.default(datetime.now()) - datetime.now().timestamp()) < 1
    assert e.default(UUID('8c7f1a57-ea01-54d6-b572-83d698a0a3f3')) == '8c7f1a57-ea01-54d6-b572-83d698a0a3f3'
    class X(Enum):
        a = 1
    assert e.default(X.a) == 1
    assert e.default(Decimal('1.23456')) == '1.23456'

# Generated at 2022-06-13 19:18:55.359543
# Unit test for constructor of class _ExtendedEncoder

# Generated at 2022-06-13 19:19:04.308174
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    json_encoder = _ExtendedEncoder(check_circular=False, indent=2, separators=(',', ': '))
    obj = {
        'a': [1, 2, 3],
        'b': {
            'c': ['d', 'e', 'f', True, False, None, Decimal('1.2'), datetime.now(timezone.utc), UUID(int=0)]
        }
    }
    assert json_encoder.encode(obj) == json.dumps(obj, check_circular=False, indent=2, separators=(',', ': '))



# Generated at 2022-06-13 19:19:09.981846
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.default([1, 2]) == [1, 2]
    assert encoder.default(datetime.now()) == datetime.now().timestamp()
    assert encoder.default(UUID('8e3116b3-c1ed-4a45-b8db-75f9a24a6823')) == str(UUID('8e3116b3-c1ed-4a45-b8db-75f9a24a6823'))
    assert encoder.default(Decimal(1.1)) == str(Decimal(1.1))



# Generated at 2022-06-13 19:19:15.801698
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode({1, 2, 3}) == '{1, 2, 3}'
    assert _ExtendedEncoder().encode(set()) == '[]'
    assert _ExtendedEncoder().encode({1: 2, 3: 4}) == '{"1": 2, "3": 4}'
    assert _ExtendedEncoder().encode(datetime(2002, 10, 27, 12, 0, 0, 0,
                                              timezone.utc)) == '1036053200.0'
    assert _ExtendedEncoder().encode(
        UUID('123e4567-e89b-12d3-a456-426655440000')) == \
               '"123e4567-e89b-12d3-a456-426655440000"'
    assert _Ext

# Generated at 2022-06-13 19:19:23.429995
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.default('dataclasses') == 'dataclasses'
    assert encoder.default([]) == []
    assert encoder.default((1, 2, 3)) == [1, 2, 3]
    assert encoder.default({}) == {}
    assert encoder.default(set()) == []
    assert encoder.default(()) == []
    assert encoder.default(frozenset({1, 2, 3})) == [1, 2, 3]
    assert encoder.default(frozenset([1, 2, 3])) == [1, 2, 3]
    assert encoder.default({'dataclasses': 1}) == {'dataclasses': 1}

# Generated at 2022-06-13 19:19:30.425262
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(1) == '1'
    assert _ExtendedEncoder().encode(True) == 'true'
    assert _ExtendedEncoder().encode(False) == 'false'
    assert _ExtendedEncoder().encode(None) == 'null'
    assert _ExtendedEncoder().encode({1: 2, 3: 4}) == '{"1": 2, "3": 4}'
    assert _ExtendedEncoder().encode([1, 2, 3, 4]) == '[1, 2, 3, 4]'
    assert _ExtendedEncoder().encode("1234") == '"1234"'
    assert _ExtendedEncoder().encode(datetime(2018, 12, 1, 12, 0, 0, tzinfo=timezone.utc)) == '1543632000'

# Generated at 2022-06-13 19:19:41.976671
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert json.dumps(UUID('01234567-89ab-cdef-0123-456789abcdef'),
                      cls=_ExtendedEncoder) == '"01234567-89ab-cdef-0123-456789abcdef"'
    assert json.dumps([UUID('01234567-89ab-cdef-0123-456789abcdef'), UUID('01234567-89ab-cdef-0123-456789abcdef')
], cls=_ExtendedEncoder) == '["01234567-89ab-cdef-0123-456789abcdef", "01234567-89ab-cdef-0123-456789abcdef"]'