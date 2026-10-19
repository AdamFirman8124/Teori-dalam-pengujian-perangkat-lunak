

# Generated at 2022-06-13 19:10:03.648409
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(UUID('f47ac10b-58cc-4372-a567-0e02b2c3d479')) == '"f47ac10b-58cc-4372-a567-0e02b2c3d479"'
    assert _ExtendedEncoder().encode(datetime.now()) == str(datetime.now().timestamp())
    assert _ExtendedEncoder().encode(datetime.now(timezone.utc)) == str(datetime.now(timezone.utc).timestamp())


# Generated at 2022-06-13 19:10:05.592851
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(Enum) == json.dumps(Enum)



# Generated at 2022-06-13 19:10:13.761374
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    import datetime
    from dataclasses import dataclass
    from enum import Enum
    from decimal import Decimal
    from uuid import UUID

# Generated at 2022-06-13 19:10:19.905153
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.default[datetime](datetime.now(timezone.utc))
    assert encoder.default[datetime](datetime.now())
    assert encoder.default[dict](dict(a=1))
    assert encoder.default[list]([1, 2, 3])
    assert encoder.default[UUID](UUID('0d3671e2-4b4e-4c8d-8a89-78c5cf5195f6'))
    assert encoder.default[Enum](Enum(int))
    assert encoder.default[str]('test')
    assert encoder.default[int](1)
    assert encoder.default[float](1.0)
    assert encoder.default[bool](True)

# Generated at 2022-06-13 19:10:23.289838
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    """ Unit Test: dataclasses_json._ExtendedEncoder """
    assert _ExtendedEncoder().encode(True) == 'true'

_default_encoder = _ExtendedEncoder(indent=True)
_default_decoder = json.JSONDecoder()



# Generated at 2022-06-13 19:10:30.209295
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    from unittest.mock import patch
    from datetime import datetime
    with patch('dataclasses_json.utils.json.JSONEncoder.default') as m_default:
        m_default.return_value = 'json.JSONEncoder.default'
        assert 'json.JSONEncoder.default' == m_default.return_value
        assert _ExtendedEncoder().default([1,2,3]) == [1,2,3]
        assert _ExtendedEncoder().default({1:2,3:4}) == {1:2,3:4}
        assert _ExtendedEncoder().default(datetime.now()) == int(datetime.now().timestamp())
        assert _ExtendedEncoder().default('1') == '1'
        assert _ExtendedEncoder().default(1) == 1

# Generated at 2022-06-13 19:10:34.494307
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.default((1,2,3)) == [1,2,3]
    assert encoder.default({1:2,3:4}) == {1:2,3:4}


# Generated at 2022-06-13 19:10:40.066823
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(
        {"name": datetime(2020, 6, 7, 10, 30, 30, tzinfo=timezone.utc),
         "uuid": UUID('a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11'),
         "enum": TestEnum.member1,
         "decimal": Decimal(0.1)
         }) == '{"name": 1591541430.0, "uuid": "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11", "enum": 1, "decimal": "0.1"}'


# Generated at 2022-06-13 19:10:51.521094
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode({'a': 1, 'b': 2}) == '{"a": 1, "b": 2}'
    assert _ExtendedEncoder().encode({'a': 1, 'b': [2, 3]}) == '{"a": 1, "b": [2, 3]}'
    assert _ExtendedEncoder().encode([1, 2, 3]) == '[1, 2, 3]'
    assert _ExtendedEncoder().encode(UUID('e590a97e-ee1f-4cf8-a63f-84bfaa94be53')) == '"e590a97e-ee1f-4cf8-a63f-84bfaa94be53"'

# Generated at 2022-06-13 19:10:58.107844
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    enc = _ExtendedEncoder()
    assert enc.default([1, 2, 3]) == [1, 2, 3]
    assert enc.default(['1', '2', '3']) == ['1', '2', '3']
    assert enc.default((1, 2, 3)) == (1, 2, 3)
    assert enc.default(('1', '2', '3')) == ('1', '2', '3')
    assert enc.default({'a': 'b', 'c': 'd'}) == {'a': 'b', 'c': 'd'}
    assert enc.default(datetime(2020, 1, 1)) == 1577836800.0

# Generated at 2022-06-13 19:11:25.960460
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(None) == "null"
    assert _ExtendedEncoder().encode(uuid.uuid4()) == "\"9274879d-bb68-405b-ad33-0cf223b7eae1\""
    assert _ExtendedEncoder().encode(True) == "true"
    assert _ExtendedEncoder().encode(False) == "false"
    assert _ExtendedEncoder().encode(1) == "1"
    assert _ExtendedEncoder().encode(1.0) == "1.0"
    assert _ExtendedEncoder().encode(1.0+0.0j) == "\"1.0+0.0j\""
    assert _ExtendedEncoder().encode("test") == "\"test\""
    assert _Ext

# Generated at 2022-06-13 19:11:27.762071
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert str(_ExtendedEncoder().encode(Enum)) == 'null'

# noinspection PyUnresolvedReferences

# Generated at 2022-06-13 19:11:35.983117
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    assert _ExtendedEncoder().default([1,2,3]) == [1,2,3]
    assert _ExtendedEncoder().default({'key': 'value'}) == {'key': 'value'}
    assert _ExtendedEncoder().default(datetime.now(timezone.utc)) == \
        datetime.now(timezone.utc).timestamp()
    assert _ExtendedEncoder().default(UUID('42a8353b-86f6-4b31-b238-a8f2b3811cac')) == \
        '42a8353b-86f6-4b31-b238-a8f2b3811cac'
    assert _ExtendedEncoder().default(Decimal('1.23')) == '1.23'
    class NewType:
        pass

# Generated at 2022-06-13 19:11:44.007561
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    _ExtendedEncoder().default(datetime.now().replace(tzinfo=timezone.utc).astimezone()) == datetime.now().timestamp()
    _ExtendedEncoder().default(datetime.now().replace(tzinfo=timezone.utc)) == datetime.now().timestamp()
    _ExtendedEncoder().default({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}
    _ExtendedEncoder().default([1, 2, 3]) == [1, 2, 3]

# Generated at 2022-06-13 19:11:49.640601
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    res = _ExtendedEncoder().encode([
        {}, [], "string", 10, 5.0, True, None, datetime.now(tz=timezone.utc),
        UUID("123e4567-e89b-12d3-a456-426655440000"),
        Decimal("1.414213"),
    ])
    # print("test__ExtendedEncoder res:", res)
    assert res.count("1.414213E+0") == 1  # the only float in str
    assert res.count("123e4567-e89b-12d3-a456-426655440000") == 1  # UUID



# Generated at 2022-06-13 19:11:52.507240
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.default(datetime.now(timezone.utc))



# Generated at 2022-06-13 19:12:01.694660
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default('abc') == 'abc'
    assert _ExtendedEncoder().default(123) == 123
    assert _ExtendedEncoder().default(123.4) == 123.4
    assert _ExtendedEncoder().default(True) == True
    assert _ExtendedEncoder().default(False) == False
    assert _ExtendedEncoder().default(None) == None
    assert _ExtendedEncoder().default(datetime(2019,12,1,8,0,0, tzinfo=timezone.utc)) == 1572636800.0

# Generated at 2022-06-13 19:12:06.244319
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(set()) == '[]'
    assert _ExtendedEncoder().encode(defaultdict(str)) == '{}'
    assert _ExtendedEncoder().encode(defaultdict(int)) == '{}'
    rid = datetime.now(tz=timezone.utc).replace(microsecond=0)
    assert _ExtendedEncoder().encode(rid)\
        == f'{datetime.timestamp(rid)}'
    assert json.loads(_ExtendedEncoder().encode(UUID('44444444-4444-4444-4444-444444444444'))) == '44444444-4444-4444-4444-444444444444'

# Generated at 2022-06-13 19:12:17.322564
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    o1 = {'a': 1, 'b': 2, 'c': 3}
    o2 = {'list': [1, 2, 3]}
    o3 = ('1', '2', '3')
    o4 = [1, 2, 3]
    o5 = datetime(2018, 11, 21, 23, 59, 59, 999999, timezone.utc)
    o6 = UUID("12345678-1234-5678-1234-567812345678")
    o7 = 'string'
    o8 = 6.28
    a = _ExtendedEncoder()
    dict1 = a.default(o1)
    dict2 = a.default(o2)
    dict3 = a.default(o3)
    dict4 = a.default(o4)

# Generated at 2022-06-13 19:12:24.757692
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert json.dumps([1, 2], cls=_ExtendedEncoder) == '[1, 2]'
    assert json.dumps(defaultdict(), cls=_ExtendedEncoder) == '{}'
    assert json.dumps(set(), cls=_ExtendedEncoder) == '[]'
    assert json.dumps(datetime.now(timezone.utc), cls=_ExtendedEncoder) == '0.0'
    assert json.dumps(UUID('c4b24098-4a6a-48e9-9c17-cf8e0bc6a089'), cls=_ExtendedEncoder) == '"c4b24098-4a6a-48e9-9c17-cf8e0bc6a089"'

# Generated at 2022-06-13 19:13:19.672133
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default([1,2]) == [1,2]
    assert _ExtendedEncoder().default('hoge') == 'hoge'
    assert _ExtendedEncoder().default(True) == True
    assert _ExtendedEncoder().default(None) == None
    assert _ExtendedEncoder().default(UUID('f47ac10b-58cc-4372-a567-0e02b2c3d479')) == 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
    import datetime
    assert _ExtendedEncoder().default(datetime.datetime(2020,1,1,0,0,0,0,datetime.timezone.utc)) == 1577836800.0

# Generated at 2022-06-13 19:13:32.656605
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default(datetime(2019, 2, 20)) == 1550198000.0
    assert _ExtendedEncoder().default([1, 2, 3]) == [1, 2, 3]
    assert _ExtendedEncoder().default([]) == []
    assert _ExtendedEncoder().default(()) == []
    assert _ExtendedEncoder().default(set()) == []
    assert _ExtendedEncoder().default({}) == {}
    assert _ExtendedEncoder().default({'1': 1}) == {'1': 1}
    assert _ExtendedEncoder().default(frozenset({'1', '2', '3'})) == ['1', '2', '3']

# Generated at 2022-06-13 19:13:39.212204
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    ext_enc = _ExtendedEncoder()
    assert ext_enc.default(list(range(5))) == list(range(5))
    assert ext_enc.default({'1': 2, '3': 4}) == {'1': 2, '3': 4}
    assert ext_enc.default(datetime(2010, 12, 12, 15, 0, tzinfo=timezone.utc)) == 1292233600.0



# Generated at 2022-06-13 19:13:47.232841
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    enc = _ExtendedEncoder()
    assert enc.default(1) == 1
    assert enc.default('a') == 'a'
    assert enc.default((1, 2)) == [1, 2]
    assert enc.default({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}
    assert enc.default(datetime.now()) == datetime.now().timestamp()
    assert enc.default(UUID('bb717b24-a8fc-11e9-bb65-784f4351712a')) == 'bb717b24-a8fc-11e9-bb65-784f4351712a'
    assert enc.default(Enum('Enum', ['a'])('a')) == 'a'

# Generated at 2022-06-13 19:13:54.531621
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    from datetime import timedelta

    encoder = _ExtendedEncoder()
    assert encoder.default([]) == []
    assert encoder.default({}) == {}

    timedelta(hours=1).total_seconds()
    assert encoder.default([datetime.now()]) == [datetime.now().timestamp()]
    assert encoder.default({'key1': datetime.now(), 'key2': datetime.now()}) == {
        'key1': datetime.now().timestamp(), 'key2': datetime.now().timestamp()}
    dt = datetime.now()
    assert encoder.default(dt) == dt.timestamp()

# Generated at 2022-06-13 19:14:01.655766
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.default(4) == 4
    assert encoder.default('str') == 'str'
    assert encoder.default({"k": "v"}) == {"k": "v"}
    assert encoder.default([1, 2, 3]) == [1, 2, 3]
    assert encoder.default(datetime(year=2019,
                                    month=9,
                                    day=28,
                                    hour=10,
                                    minute=30,
                                    second=15,
                                    tzinfo=timezone(
                                        timedelta(hours=3)))) == 1569682215

# Generated at 2022-06-13 19:14:09.693508
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    input = 3.2
    output = 3.2
    assert _ExtendedEncoder().default(input) == output

    input = datetime(2020, 7, 4, 10, 0, 0, tzinfo=timezone.utc)
    output = 1593998800.0
    assert _ExtendedEncoder().default(input) == output

    input = Decimal('3.2')
    output = '3.2'
    assert _ExtendedEncoder().default(input) == output



# Generated at 2022-06-13 19:14:16.430225
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    e = _ExtendedEncoder()
    assert e.default('hello') == 'hello'
    assert e.default(5) == 5
    assert e.default(5.5) == 5.5
    assert e.default(True) == True
    assert e.default(False) == False
    assert e.default(None) == None
    assert e.default(['hello', 'world']) == ['hello', 'world']
    assert e.default({'hello': 'world'}) == {'hello': 'world'}



# Generated at 2022-06-13 19:14:25.259024
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    import sys
    import json

    class SomeType:
        a: int

        def __init__(self) -> None:
            self.a = 1

        def __eq__(self, other: object) -> bool:
            return self.a == other.a

        def __repr__(self) -> str:
            return repr(self.a)

    # basic types
    assert _ExtendedEncoder().encode(1) == json.JSONEncoder().encode(1)
    assert _ExtendedEncoder().encode(True) == json.JSONEncoder().encode(True)
    assert _ExtendedEncoder().encode(None) == json.JSONEncoder().encode(None)
    assert _ExtendedEncoder().encode(1.0) == json.JSONEncoder().encode(1.0)


# Generated at 2022-06-13 19:14:28.320533
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    extended_encoder = _ExtendedEncoder()
    result = extended_encoder.default({'Dict': 1})
    assert result == {'Dict': 1}

    result = extended_encoder.default([1, 2, 3])
    assert result == [1, 2, 3]


# Generated at 2022-06-13 19:16:10.629360
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    e = _ExtendedEncoder()
    assert e.default([1, 2, 3]) == [1, 2, 3]
    assert e.default([]) == []
    assert e.default({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}
    assert e.default({}) == {}
    assert isinstance(e.default(datetime.now(tz=timezone.utc)), float)
    assert e.default(UUID('9c92395a-bcf4-4aa4-85c3-852853d9562d')) == '9c92395a-bcf4-4aa4-85c3-852853d9562d'
    assert e.default(cfg.enforce_string) is True

# Generated at 2022-06-13 19:16:12.224337
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    result = _ExtendedEncoder().encode([1, 2, 3])
    # noinspection PyUnresolvedReferences
    assert result == '[1, 2, 3]'



# Generated at 2022-06-13 19:16:14.689092
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.encode([]) == "[]"
    assert encoder.encode({}) == "{}"
    assert encoder.encode({1: 2}) == '{"1": 2}'
    assert encoder.encode([1, 2]) == "[1, 2]"



# Generated at 2022-06-13 19:16:16.716524
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    _ExtendedEncoder()
    


# Generated at 2022-06-13 19:16:27.701951
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    # type: () -> None
    e = _ExtendedEncoder()
    assert e.default([1, 2, 3]) == [1, 2, 3]
    assert e.default({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}
    myuuid = UUID("82d6747c-a63d-4bc0-b1a8-2c11e3e715fa")
    assert e.default(myuuid) == "82d6747c-a63d-4bc0-b1a8-2c11e3e715fa"

    class MyEnum(Enum):
        a = 'first'
        b = 'second'
    assert e.default(MyEnum(1)) == 'first'



# Generated at 2022-06-13 19:16:34.002275
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.default([]) == []
    assert encoder.default({}) == {}
    dt = datetime.now(timezone.utc)
    assert encoder.default(dt) == dt.timestamp()
    uuid = UUID('a2a0c26d-faf1-4d43-9e76-c22e4a0ca7e8')
    assert encoder.default(uuid) == 'a2a0c26d-faf1-4d43-9e76-c22e4a0ca7e8'
    assert encoder.default(Decimal('1.1')) == '1.1'



# Generated at 2022-06-13 19:16:37.746194
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    json_string = json.dumps(['a', 'b'], cls=_ExtendedEncoder)
    assert json_string == '["a", "b"]'



# Generated at 2022-06-13 19:16:46.117055
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    mj = _ExtendedEncoder()
    assert mj.default({1, 2, 3}) == [1, 2, 3]
    assert mj.default({"a": 1, "b": 2, "c": 3}) == {"a": 1, "b": 2, "c": 3}
    assert mj.default((1, 2, 3)) == [1, 2, 3]
    assert mj.default([1, 2, 3]) == [1, 2, 3]
    assert mj.default([1, 2, 3, {1, 2, 4}]) == [1, 2, 3, [1, 2, 4]]
    assert mj.default((1, 2, 3, {1, 2, 4})) == [1, 2, 3, [1, 2, 4]]


# Generated at 2022-06-13 19:16:49.923152
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    """
    Function to test constructor of class _ExtendedEncoder
    """

    x_json_encoder = _ExtendedEncoder()
    assert x_json_encoder


# Generated at 2022-06-13 19:16:51.091735
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    _ExtendedEncoder()
