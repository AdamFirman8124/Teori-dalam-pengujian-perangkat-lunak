

# Generated at 2022-06-13 19:10:06.051213
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.default(None) == None
    assert encoder.default(1) == 1
    assert encoder.default(1.9) == 1.9
    assert encoder.default(True) == True
    assert encoder.default(False) == False
    assert encoder.default(datetime.now(timezone.utc)) == datetime.now(timezone.utc).timestamp()
    assert encoder.default(b'abc') == 'abc'
    assert encoder.default(b'abc') != 'a'
    assert encoder.default(range(3)) == [0, 1, 2]
    assert encoder.default('abc') == 'abc'
    assert encoder.default(['abc', 'def']) == ['abc', 'def']

# Generated at 2022-06-13 19:10:14.090251
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    # given
    data = [
        {'dict': {'name': 'dummy'}},
        {'list': [2, 3]},
        {'str': 'test'},
        {'int': 1},
        {'float': 0.1},
        {'bool': True},
        {'none': None},
        {'date': datetime(2019, 1, 1)},
        {'uuid': UUID('8c0987dc-b76e-43ff-a5b8-7c8c75b1d9c2')},
        {'enum': cfg.LetterCase.CAMEL_CASE},
        {'decimal': Decimal('1.5')}
    ]

    # when
    result = json.dumps(data, cls=_ExtendedEncoder)



# Generated at 2022-06-13 19:10:23.723619
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    for o in [
            {'a': 'a', 'b': 1},
            [1, 2, 3],
            datetime(2020, 1, 1, 0, 0, 0, 0, tzinfo=timezone.utc),
            UUID('{12345678-1234-5678-1234-567812345678}')]:
        encoded = _ExtendedEncoder().default(o)
        assert encoded == json.dumps(o)
    for o in [datetime.now(), Enum('CustomizedEnum', [('HELLO', 0)])]:
        encoded = _ExtendedEncoder().default(o)
        assert encoded != json.dumps(o)

# Generated at 2022-06-13 19:10:30.241826
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    result = _ExtendedEncoder().default(datetime(2019, 12, 31, 1, 2, 3, 123456))
    assert result == datetime(2019, 12, 31, 1, 2, 3, 123456).timestamp()
    
    result = _ExtendedEncoder().default(UUID('a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11'))
    assert result == str(UUID('a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11'))

    class Test1(Enum):
        OPTION1 = 1
        OPTION2 = 2

    result = _ExtendedEncoder().default(Test1.OPTION1)
    assert result == 1


# Generated at 2022-06-13 19:10:42.053974
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode({}) == '{}'
    assert _ExtendedEncoder().encode([1, 2, 3]) == '[1, 2, 3]'
    assert _ExtendedEncoder().encode({"1": 2}) == '{"1": 2}'
    assert _ExtendedEncoder().encode("abc") == '"abc"'
    assert _ExtendedEncoder().encode(0) == '0'
    assert _ExtendedEncoder().encode(0.0) == '0.0'
    assert _ExtendedEncoder().encode(True) == 'true'
    assert _ExtendedEncoder().encode(False) == 'false'
    assert _ExtendedEncoder().encode(None) == 'null'

# Generated at 2022-06-13 19:10:45.731041
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    newEncoder = _ExtendedEncoder()
    testMe = [1, 2, 3, 4, 5]
    try:
        newEncoder.default(testMe)
        assert True
    except:
        assert False



# Generated at 2022-06-13 19:10:47.472287
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    enc = _ExtendedEncoder()



# Generated at 2022-06-13 19:10:56.130077
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    assert _ExtendedEncoder().default(set()) == []
    assert _ExtendedEncoder().default(frozenset()) == []
    assert _ExtendedEncoder().default(datetime.now()) == datetime.now().timestamp()
    assert _ExtendedEncoder().default(UUID('9f48a8b3-b7e5-47be-b3ad-8f023e3f0a67')) == '9f48a8b3-b7e5-47be-b3ad-8f023e3f0a67'

# Generated at 2022-06-13 19:11:05.032577
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default(set()) == []
    assert _ExtendedEncoder().default(frozenset()) == []
    assert _ExtendedEncoder().default(dict()) == {}
    assert _ExtendedEncoder().default(tuple()) == []
    assert _ExtendedEncoder().default(datetime.now(timezone.utc)) == 1526784317.836065



# Generated at 2022-06-13 19:11:12.973604
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.default(4) == 4
    assert encoder.default([4, 5]) == [4, 5]
    assert encoder.default(('4', 5)) == ['4', 5]
    assert encoder.default(('4', 5, {'a': 'b'})) == ['4', 5, {'a': 'b'}]
    assert encoder.default({'a': 'b'}) == {'a': 'b'}
    assert encoder.default("abc") == "abc"
    assert encoder.default("abc") != 'abc'
    assert encoder.default("abc") in ['abc', "abc"]


# noinspection PyProtectedMember

# Generated at 2022-06-13 19:11:33.894670
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    o = bytearray([1, 2, 3])
    assert _ExtendedEncoder().default(o) == [1, 2, 3]
    o = Decimal("5")
    assert _ExtendedEncoder().default(o) == '5'


# Generated at 2022-06-13 19:11:41.097687
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    assert list(json.loads(_ExtendedEncoder().encode([]))) == []
    assert list(json.loads(_ExtendedEncoder().encode((1, 2, 3)))) == [1, 2, 3]
    assert list(json.loads(_ExtendedEncoder().encode((1, 2, 3, (4, 5))))) == [1, 2, 3, [4, 5]]
    assert list(json.loads(_ExtendedEncoder().encode(set([1, 2, 3])))) == [1, 2, 3]
    assert list(json.loads(_ExtendedEncoder().encode({1: 2, 3: 4}))) == [{"1": 2, "3": 4}]

# Generated at 2022-06-13 19:11:49.119372
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    ee = _ExtendedEncoder()
    assert ee.default({}) == dict()
    assert ee.default([]) == list()
    assert ee.default(0.0) == 0.0
    assert ee.default(0) == 0
    assert ee.default(False) == False
    assert ee.default(True) == True
    assert ee.default(None) == None
    assert ee.default('a') == 'a'
    assert ee.default(UUID('0e2c1bbd-b841-4a87-b0fb-6172d9e60c7f')) == "0e2c1bbd-b841-4a87-b0fb-6172d9e60c7f"

# Generated at 2022-06-13 19:11:59.475913
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    encoder = _ExtendedEncoder()
    assert encoder.default({}) == {}
    assert encoder.default([]) == []
    assert encoder.default('aaa') == 'aaa'
    assert encoder.default(12345) == 12345
    assert encoder.default(True) == True
    assert encoder.default(()) == []
    assert encoder.default({'a': 1}) == {'a': 1}
    assert encoder.default([1, 2, 3]) == [1, 2, 3]
    assert encoder.default(UUID('0b0bb65b-a6e0-4c8e-b85e-516fca7b94f0')) == '0b0bb65b-a6e0-4c8e-b85e-516fca7b94f0'

# Generated at 2022-06-13 19:12:00.149387
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert isinstance(_ExtendedEncoder().encode(None), str)



# Generated at 2022-06-13 19:12:03.088455
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert json.dumps([UUID('6ccd780c-baba-1026-9564-0040f4311e29')], cls=_ExtendedEncoder) == '[null]'

_ext_en = _ExtendedEncoder()



# Generated at 2022-06-13 19:12:05.970774
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():  # pragma: no cover
    encoder = _ExtendedEncoder()
    s = '{"a":1}'
    data = {'a':1}
    assert encoder.encode(data) == s
    with pytest.raises(TypeError):
        encoder.encode(1)



# Generated at 2022-06-13 19:12:06.543492
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    _ExtendedEncoder().default(1)



# Generated at 2022-06-13 19:12:11.554066
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(dict(zip(range(2), [10,'a']))) == '{"0": 10, "1": "a"}'
    assert _ExtendedEncoder().encode(tuple(zip(range(2), [10,'a']))) == '[{"0": 10, "1": "a"}]'
    assert _ExtendedEncoder().encode(datetime(2018, 4, 23, 10, 10, 10, tzinfo=timezone.utc)) == '1524503010000.0'

# Generated at 2022-06-13 19:12:22.548601
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    from datetime import timedelta
    from decimal import Decimal
    from collections import deque

    encoder = _ExtendedEncoder()

    assert encoder.default(None) is None
    assert encoder.default(True) is True
    assert encoder.default(False) is False
    assert encoder.default(1) == 1
    assert encoder.default(1.1) == 1.1
    assert encoder.default((1, 2)) == [1, 2]
    assert encoder.default([1, 2]) == [1, 2]
    assert encoder.default({1: 2}) == {1: 2}
    assert encoder.default(deque((1, 2))) == [1, 2]
    assert encoder.default(datetime(2000, 1, 1)) == 946684800.0
    assert enc

# Generated at 2022-06-13 19:12:50.626529
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode([1, 2, 3]) == "[1, 2, 3]"
    assert _ExtendedEncoder().encode({"a": 1, "b": 2, "c": 3}) == '{"a": 1, "b": 2, "c": 3}'
    assert _ExtendedEncoder().encode(datetime(1970, 1, 1, 0, 0, 0)) == "0"
    assert _ExtendedEncoder().encode(UUID("332569e6-3079-4040-b43a-aa2a2f4c4f4e")) == '"332569e6-3079-4040-b43a-aa2a2f4c4f4e"'

# Generated at 2022-06-13 19:12:58.346801
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    encoder = _ExtendedEncoder()
    assert encoder.default(None) is None
    assert encoder.default(True) is True
    assert encoder.default(1) == 1
    assert encoder.default(1.0) == 1.0
    assert encoder.default('a') == 'a'
    assert encoder.default(['a', 1]) == ['a', 1]
    assert encoder.default({'a': 1}) == {'a': 1}
    assert encoder.default(datetime.now()) == pytest.approx(time.time())
    assert encoder.default(UUID('123e4567-e89b-12d3-a456-426655440000')) == '123e4567-e89b-12d3-a456-426655440000'
   

# Generated at 2022-06-13 19:13:01.754869
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default(cfg.MISSING) is cfg.MISSING
    assert _ExtendedEncoder().default(Decimal('0')) == '0'
    assert _ExtendedEncoder().default(Decimal('0.1')) == '0.1'
    assert _ExtendedEncoder().default(Decimal('1.0')) == '1.0'
    assert _ExtendedEncoder().default(Decimal('1')) == '1'




# Generated at 2022-06-13 19:13:10.874673
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    assert _ExtendedEncoder().default(None) is None
    assert _ExtendedEncoder().default(False) is False
    assert _ExtendedEncoder().default(10) == 10
    assert _ExtendedEncoder().default(10.0) == 10.0
    assert _ExtendedEncoder().default("string") == "string"
    assert _ExtendedEncoder().default([1, 2, 3]) == [1, 2, 3]
    assert _ExtendedEncoder().default(('a', 'b', 'c')) == ['a', 'b', 'c']
    assert _ExtendedEncoder().default({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}

# Generated at 2022-06-13 19:13:13.933594
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    ExtendedEncoder = _ExtendedEncoder()
    ExtendedEncoder.encode([1,2,3]) == [1,2,3]



# Generated at 2022-06-13 19:13:14.983581
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    _ExtendedEncoder()



# Generated at 2022-06-13 19:13:22.530001
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    j = json.JSONEncoder()
    assert j.encode(UUID("b4d68db9-3621-4a0c-9812-cfe4c4f4a099")) == '"b4d68db9-3621-4a0c-9812-cfe4c4f4a099"'
    assert j.encode(UUID("b4d68db9-3621-4a0c-9812-cfe4c4f4a099")) != '3785f5a5-5a58-4d5f-a45a-e1f52e09b714'
    assert j.encode(datetime.now()) != '"2017-09-24T09:43:55.719346"'

# Generated at 2022-06-13 19:13:34.241924
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder(): # type: ignore
    e = _ExtendedEncoder()
    assert e.default(1) == 1
    assert e.default(b'x') == b'x'
    assert e.default('1') == '1'
    assert e.default([1]) == [1]
    assert e.default({'a': 1}) == {'a': 1}
    now = datetime.now(timezone.utc)
    assert e.default(now) == now.timestamp()
    assert e.default(UUID('85d85798-72a2-4d5b-a5ba-da5f9c2fe6a5')) == '85d85798-72a2-4d5b-a5ba-da5f9c2fe6a5'

# Generated at 2022-06-13 19:13:42.804510
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(1) == "1"
    assert _ExtendedEncoder().encode([1, 2]) == "[1, 2]"
    assert _ExtendedEncoder().encode([1, {"a": [2, 3]}]) == "[1, {\"a\": [2, 3]}]"
    assert _ExtendedEncoder().encode({"a": 1, "b": 2}) == "{\"a\": 1, \"b\": 2}"
    assert _ExtendedEncoder().encode({"a": 1, "b": {"c": 2, "d": [3, 4]}}) == "{\"a\": 1, \"b\": {\"c\": 2, \"d\": [3, 4]}}"
    assert _ExtendedEncoder().encode(datetime.now(timezone.utc)) == "0"


# Generated at 2022-06-13 19:13:52.644109
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    # pylint: disable=unused-variable
    _dict = {'a': 1, 'b': 2}
    _list = [1, 2, 3]
    _timestamp = datetime.now(timezone.utc)
    _uuid = UUID('6ba7b810-9dad-11d1-80b4-00c04fd430c8')
    _enum = TestEnum.a
    _decimal = Decimal(0.5)
    encoder = _ExtendedEncoder()
    assert encoder.default(_dict) == _dict
    assert encoder.default(_list) == _list
    assert encoder.default(_timestamp) == _timestamp.timestamp()
    assert encoder.default(_uuid) == str(_uuid)
    assert encoder.default(_enum) == _

# Generated at 2022-06-13 19:14:35.900490
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    from decimal import Decimal as D
    from datetime import datetime as d
    import uuid
    from dataclasses_json.math_enum import MathEnum
    from dataclasses_json.extended_json import ExtendedJson, _ExtendedEncoder

    @ExtendedJson
    class TestExtendedEncoder:
        a: str = 'a'
        b: int = 1
        c: float = 1.1
        d: list = [1, 1.1, '1']
        e: tuple = (1, 1.1, '1')
        f: dict = {1: 1.1, '1': '1'}
        g: MathEnum = MathEnum.ADD
        h: d = d.now()
        i: uuid.UUID = uuid.uuid4()

# Generated at 2022-06-13 19:14:44.183271
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    o = _ExtendedEncoder()
    assert o.default({"a": 1}) == {"a": 1}
    assert o.default([1, 2]) == [1, 2]
    assert o.default(datetime.now()) == datetime.now().timestamp()
    assert o.default(UUID('ad9b9177-0f49-40e8-95b0-d06ace7a0c2f')) == 'ad9b9177-0f49-40e8-95b0-d06ace7a0c2f'



# Generated at 2022-06-13 19:14:47.450171
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    expected = 123
    json_encoder = _ExtendedEncoder(use_decimal=True)
    # noinspection PyTypeChecker
    result = json_encoder.default(Decimal(expected))
    assert result == expected



# Generated at 2022-06-13 19:14:50.644109
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default(Decimal()) == '0'
    # assert _ExtendedEncoder().default(decimal.Decimal()) == '0'

_extended_encoder = _ExtendedEncoder()

_SKIP = object()



# Generated at 2022-06-13 19:14:52.649824
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default(datetime.now()) == datetime.now().timestamp()



# Generated at 2022-06-13 19:14:59.642002
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.default(True) == True
    assert encoder.default(False) == False
    assert encoder.default(None) == None
    assert encoder.default(123) == 123
    assert encoder.default(123.456) == 123.456
    assert encoder.default('123') == '123'
    assert encoder.default(['a', 'b']) == ['a', 'b']
    assert encoder.default({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}
    assert encoder.default(bytes(3)) == bytes(3)
    assert encoder.default(set([1,2,3])) == [1,2,3]

# Generated at 2022-06-13 19:15:08.462879
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(['a']) == '["a"]'
    assert _ExtendedEncoder().encode(('a',)) == '["a"]'
    assert _ExtendedEncoder().encode({}) == '{}'
    assert _ExtendedEncoder().encode(set()) == '[]'
    assert _ExtendedEncoder().encode({'a': 1}) == '{"a": 1}'
    assert _ExtendedEncoder().encode(datetime(1970, 1, 1, 0, 0, 0, tzinfo=timezone.utc)) == '0.0'

# Generated at 2022-06-13 19:15:12.491018
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.default(1) == 1
    uuid = UUID("bfafc11f-e660-45b7-a71a-a0c9b56e2391")
    assert encoder.default(uuid) == "bfafc11f-e660-45b7-a71a-a0c9b56e2391"
    assert encoder.default(datetime.now()) != ""



# Generated at 2022-06-13 19:15:15.012234
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode({"foo": "bar"}) == '{"foo": "bar"}'


# Generated at 2022-06-13 19:15:17.565457
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoded = json.dumps(set(), cls=_ExtendedEncoder)
    assert encoded == '[]'


# Generated at 2022-06-13 19:16:16.801020
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.default([]) == []
    assert encoder.default((1, 2, 3)) == [1, 2, 3]
    assert encoder.default({'bad': 'dude'}) == {'bad': 'dude'}
    assert encoder.default(set([1, 2, 3])) == [1, 2, 3]
    assert encoder.default(9) == 9
    assert encoder.default(9.1) == 9.1
    assert encoder.default(True) is True
    assert encoder.default(False) is False
    assert encoder.default(None) is None
    assert encoder.default("abc") == "abc"
    assert encoder.default(Enum('one', 'ONE')) == 'ONE'

# Generated at 2022-06-13 19:16:17.657464
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    d = _ExtendedEncoder
    assert d(exclude_none=True) == d()


# Generated at 2022-06-13 19:16:21.488209
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default(set()) == list(set())
    assert _ExtendedEncoder().default(frozenset()) == list(frozenset())



# Generated at 2022-06-13 19:16:28.946158
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.default(datetime.now()) == datetime.now().timestamp()
    assert encoder.default(UUID('a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11')) == 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11'
    assert encoder.default(Decimal('1.2')) == '1.2'
    assert encoder.default(1) == 1
    assert encoder.default("string") == "string"
    assert encoder.default(True) == True




# Generated at 2022-06-13 19:16:31.080881
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.default(cfg.DataclassJsonMixin()) == {}



# Generated at 2022-06-13 19:16:42.284955
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    json_encoder = _ExtendedEncoder()
    assert json_encoder.default(dict()) == dict()
    assert json_encoder.default([1, 2, 3]) == [1, 2, 3]
    assert json_encoder.default(datetime.now()) == datetime.now().timestamp()
    assert json_encoder.default(UUID('2b1e7934-d07f-4429-a0fa-f7fa67d2e707')) == \
           str(UUID('2b1e7934-d07f-4429-a0fa-f7fa67d2e707'))
    assert json_encoder.default(Decimal('1.2')) == '1.2'



# Generated at 2022-06-13 19:16:48.659168
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    o = object()
    assert _ExtendedEncoder().default(o) == repr(o)
    assert _ExtendedEncoder().default(None) is None
    assert _ExtendedEncoder().default(1) == 1
    assert _ExtendedEncoder().default("str") == "str"
    assert _ExtendedEncoder().default(1.2) == 1.2
    assert _ExtendedEncoder().default({}) == {}
    assert _ExtendedEncoder().default([]) == []
    assert _ExtendedEncoder().default(UUID("12345678-1234-5678-1234-567812345678")) == "12345678-1234-5678-1234-567812345678"
    assert _ExtendedEncoder().default(datetime.utcnow()) == datetime.utcnow().timestamp

# Generated at 2022-06-13 19:16:57.447106
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    assert _ExtendedEncoder().default(['a', 1]) == ['a', 1]
    assert _ExtendedEncoder().default({'a': 1}) == {'a': 1}
    now = datetime.now(timezone.utc)
    assert _ExtendedEncoder().default(now) == now.timestamp()
    u = UUID('a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11')
    assert _ExtendedEncoder().default(u) == str(u)


# Generated at 2022-06-13 19:17:02.729685
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default(datetime.now(timezone.utc))
    assert _ExtendedEncoder().default(UUID('00000000-0000-0000-0000-000000000000'))
    assert _ExtendedEncoder().default({})
    assert _ExtendedEncoder().default([])
    assert _ExtendedEncoder().default(str())
    assert _ExtendedEncoder().default(int())
    assert _ExtendedEncoder().default(float())
    assert _ExtendedEncoder().default(False)
    assert _ExtendedEncoder().default(None)



# Generated at 2022-06-13 19:17:15.170379
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    """Test _ExtendedEncoder.default()"""
    e = _ExtendedEncoder()
    json_map = e.default({'a':1})
    assert(json_map == {'a':1})
    json_list = e.default([1, 2, 3])
    assert(json_list == [1, 2, 3])
    json_string = e.default('a')
    assert(json_string == 'a')
    json_number = e.default(1)
    assert(json_number == 1)
    json_float = e.default(2.0)
    assert(json_float == 2.0)
    json_bool = e.default(True)
    assert(json_bool == True)
    json_none = e.default(None)
    assert(json_none == None)
   

# Generated at 2022-06-13 19:19:27.162104
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    assert _ExtendedEncoder().default(datetime.now(timezone.utc)) == 1589933187.151135
    assert _ExtendedEncoder().default(Decimal('-42')) == '-42'
    assert _ExtendedEncoder().default(UUID('6e7c6a48-6a3c-49bc-b1fc-2a99db6a592c')) == '6e7c6a48-6a3c-49bc-b1fc-2a99db6a592c'
    assert _ExtendedEncoder().default(Mapping()) == {}
    assert _ExtendedEncoder().default(list()) == []
    assert _ExtendedEncoder().default(42) == 42
    assert _ExtendedEncoder().default(None) == None
    assert _ExtendedEncoder().default

# Generated at 2022-06-13 19:19:39.411055
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert json.dumps(UUID('7318ce68-8c4b-4177-bab4-b6a8a42a0eb6'), cls=_ExtendedEncoder) == '"7318ce68-8c4b-4177-bab4-b6a8a42a0eb6"'
    assert json.dumps(Decimal('1.0'), cls=_ExtendedEncoder) == '"1.0"'
    assert json.dumps(datetime(2020,1,1,tzinfo=timezone.utc), cls=_ExtendedEncoder) == '1577836800.0'
    assert json.dumps(['a', 'b', 'c'], cls=_ExtendedEncoder) == '["a", "b", "c"]'
    assert json.dumps

# Generated at 2022-06-13 19:19:53.352670
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    from dataclasses import dataclass
    from decimal import Decimal
    from uuid import UUID
    from datetime import timezone, datetime
    from enum import Enum

    @dataclass
    class Foo:
        pass

    class Bar(Enum):
        _value_ = 0

    def _test():
        assert _ExtendedEncoder().encode({}) == '{}'
        assert _ExtendedEncoder().encode([]) == '[]'
        assert _ExtendedEncoder().encode((1, 2, 3)) == '[1, 2, 3]'
        assert _ExtendedEncoder().encode(Foo) == '"Foo"'
        assert _ExtendedEncoder().encode(Bar) == '"Bar"'