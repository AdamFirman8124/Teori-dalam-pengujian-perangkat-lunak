

# Generated at 2024-03-18 05:13:44.450034
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():    # Test encoding of various types using _ExtendedEncoder
    encoder = _ExtendedEncoder()

    # Test encoding of collection types
    assert encoder.default([1, 2, 3]) == [1, 2, 3]
    assert encoder.default({'key': 'value'}) == {'key': 'value'}

    # Test encoding of datetime
    dt = datetime(2021, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
    assert encoder.default(dt) == dt.timestamp()

    # Test encoding of UUID
    uuid_val = UUID('12345678123456781234567812345678')
    assert encoder.default(uuid_val) == str(uuid_val)

    # Test encoding of Enum
    class Color(Enum):
        RED = 1
        GREEN = 2
        BLUE = 3
    assert encoder.default(Color.RED) == Color.RED.value

    # Test encoding of Decimal
   

# Generated at 2024-03-18 05:13:50.283831
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():    # Test encoding of various types using _ExtendedEncoder
    encoder = _ExtendedEncoder()

    # Test encoding of collection types
    assert encoder.default([1, 2, 3]) == [1, 2, 3]
    assert encoder.default({'key': 'value'}) == {'key': 'value'}

    # Test encoding of datetime
    now = datetime.now(timezone.utc)
    assert encoder.default(now) == now.timestamp()

    # Test encoding of UUID
    uuid_obj = UUID('12345678123456781234567812345678')
    assert encoder.default(uuid_obj) == str(uuid_obj)

    # Test encoding of Enum
    class Color(Enum):
        RED = 1
        GREEN = 2
        BLUE = 3
    assert encoder.default(Color.RED) == Color.RED.value

    # Test encoding of Decimal
    decimal_obj = Decimal('10.5')

# Generated at 2024-03-18 05:13:55.559108
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():    # Test encoding of collections
    assert json.dumps([1, 2, 3], cls=_ExtendedEncoder) == '[1, 2, 3]'
    assert json.dumps({'a': 1, 'b': 2}, cls=_ExtendedEncoder) == '{"a": 1, "b": 2}'

    # Test encoding of datetime
    dt = datetime(2021, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
    assert json.dumps(dt, cls=_ExtendedEncoder) == str(dt.timestamp())

    # Test encoding of UUID
    uuid_obj = UUID('12345678123456781234567812345678')
    assert json.dumps(uuid_obj, cls=_ExtendedEncoder) == '"12345678-1234-5678-1234-567812345678"'

    # Test encoding of Enum
    class Color(Enum):
        RED = 1
        GREEN

# Generated at 2024-03-18 05:14:00.501493
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():    # Test encoding of various types using _ExtendedEncoder
    encoder = _ExtendedEncoder()

    # Test encoding of collection types
    assert encoder.default([1, 2, 3]) == [1, 2, 3]
    assert encoder.default({'key': 'value'}) == {'key': 'value'}

    # Test encoding of datetime
    dt = datetime(2021, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
    assert encoder.default(dt) == dt.timestamp()

    # Test encoding of UUID
    uuid_val = UUID('12345678123456781234567812345678')
    assert encoder.default(uuid_val) == str(uuid_val)

    # Test encoding of Enum
    class Color(Enum):
        RED = 1
        GREEN = 2
        BLUE = 3
    assert encoder.default(Color.RED) == Color.RED.value

    # Test encoding of Decimal
   

# Generated at 2024-03-18 05:14:07.539559
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():    # Test encoding of various types using _ExtendedEncoder
    encoder = _ExtendedEncoder()

    # Test encoding of a collection - list
    assert encoder.default([1, 2, 3]) == [1, 2, 3]

    # Test encoding of a collection - dict
    assert encoder.default({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}

    # Test encoding of a datetime object
    dt = datetime(2021, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
    assert encoder.default(dt) == dt.timestamp()

    # Test encoding of a UUID
    uuid_obj = UUID('12345678123456781234567812345678')
    assert encoder.default(uuid_obj) == str(uuid_obj)

    # Test encoding of an Enum
    class Color(Enum):
        RED = 1

# Generated at 2024-03-18 05:14:14.631140
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():    # Create an instance of the _ExtendedEncoder
    encoder = _ExtendedEncoder()

    # Test with a collection - list
    assert encoder.default([1, 2, 3]) == [1, 2, 3]

    # Test with a collection - dict
    assert encoder.default({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}

    # Test with a datetime object
    dt = datetime(2021, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
    assert encoder.default(dt) == dt.timestamp()

    # Test with a UUID
    uuid_obj = UUID('12345678123456781234567812345678')
    assert encoder.default(uuid_obj) == str(uuid_obj)

    # Test with an Enum
    class Color(Enum):
        RED = 1
        GREEN = 2

# Generated at 2024-03-18 05:14:21.816433
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():    # Test encoding of various types using _ExtendedEncoder
    encoder = _ExtendedEncoder()

    # Test encoding of collection types
    assert encoder.default([1, 2, 3]) == [1, 2, 3]
    assert encoder.default({'key': 'value'}) == {'key': 'value'}

    # Test encoding of datetime
    dt = datetime(2021, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
    assert encoder.default(dt) == dt.timestamp()

    # Test encoding of UUID
    uuid_obj = UUID('12345678123456781234567812345678')
    assert encoder.default(uuid_obj) == str(uuid_obj)

    # Test encoding of Enum
    class Color(Enum):
        RED = 1
        GREEN = 2
        BLUE = 3
    assert encoder.default(Color.RED) == Color.RED.value

    # Test encoding of Decimal
   

# Generated at 2024-03-18 05:14:28.842062
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():    # Test encoding of various types using _ExtendedEncoder
    encoder = _ExtendedEncoder()

    # Test encoding of collection types (list, set, dict)
    assert encoder.default([1, 2, 3]) == [1, 2, 3]
    assert encoder.default({1, 2, 3}) == [1, 2, 3]
    assert encoder.default({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}

    # Test encoding of datetime
    dt = datetime(2021, 1, 1, 12, 0, tzinfo=timezone.utc)
    assert encoder.default(dt) == dt.timestamp()

    # Test encoding of UUID
    uuid_obj = UUID('12345678123456781234567812345678')
    assert encoder.default(uuid_obj) == str(uuid_obj)

    # Test encoding of Enum

# Generated at 2024-03-18 05:14:34.276997
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():    encoder = _ExtendedEncoder()

    # Test encoding of collection types

# Generated at 2024-03-18 05:14:43.313108
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():    # Test encoding of various types using _ExtendedEncoder
    encoder = _ExtendedEncoder()

    # Test encoding of a collection - list
    assert encoder.default([1, 2, 3]) == [1, 2, 3]

    # Test encoding of a collection - dict
    assert encoder.default({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}

    # Test encoding of a datetime object
    dt = datetime(2021, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
    assert encoder.default(dt) == dt.timestamp()

    # Test encoding of a UUID
    uuid_obj = UUID('12345678123456781234567812345678')
    assert encoder.default(uuid_obj) == str(uuid_obj)

    # Test encoding of an Enum
    class Color(Enum):
        RED = 1
       

# Generated at 2024-03-18 05:15:15.359220
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():    # Test encoding of various types using _ExtendedEncoder
    encoder = _ExtendedEncoder()

    # Test encoding of a collection - list
    assert encoder.default([1, 2, 3]) == [1, 2, 3]

    # Test encoding of a collection - dict
    assert encoder.default({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}

    # Test encoding of a datetime object
    dt = datetime(2021, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
    assert encoder.default(dt) == dt.timestamp()

    # Test encoding of a UUID
    uuid_obj = UUID('12345678123456781234567812345678')
    assert encoder.default(uuid_obj) == str(uuid_obj)

    # Test encoding of an Enum
    class Color(Enum):
        RED = 1

# Generated at 2024-03-18 05:15:20.092981
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():    # Test encoding of various types using _ExtendedEncoder
    encoder = _ExtendedEncoder()

    # Test encoding of a collection - list
    assert encoder.default([1, 2, 3]) == [1, 2, 3]

    # Test encoding of a collection - dict
    assert encoder.default({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}

    # Test encoding of a datetime object
    dt = datetime(2021, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
    assert encoder.default(dt) == dt.timestamp()

    # Test encoding of a UUID
    uuid_obj = UUID('12345678123456781234567812345678')
    assert encoder.default(uuid_obj) == str(uuid_obj)

    # Test encoding of an Enum
    class Color(Enum):
        RED = 1

# Generated at 2024-03-18 05:15:25.680822
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():    # Test encoding of various data types using _ExtendedEncoder
    encoder = _ExtendedEncoder()

    # Test encoding of collection types (list and dict)
    assert encoder.default([1, 2, 3]) == [1, 2, 3]
    assert encoder.default({'key': 'value'}) == {'key': 'value'}

    # Test encoding of datetime
    dt = datetime(2021, 1, 1, 12, 0, tzinfo=timezone.utc)
    assert encoder.default(dt) == dt.timestamp()

    # Test encoding of UUID
    uuid_obj = UUID('12345678123456781234567812345678')
    assert encoder.default(uuid_obj) == str(uuid_obj)

    # Test encoding of Enum
    class Color(Enum):
        RED = 1
        GREEN = 2
        BLUE = 3
    assert encoder.default(Color.RED) == Color.RED.value

    # Test encoding of Decimal

# Generated at 2024-03-18 05:15:31.514413
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():    # Test encoding of various types using _ExtendedEncoder
    encoder = _ExtendedEncoder()

    # Test encoding of collection types (list, set, dict)
    assert encoder.default([1, 2, 3]) == [1, 2, 3]
    assert encoder.default({1, 2, 3}) == [1, 2, 3]
    assert encoder.default({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}

    # Test encoding of datetime
    dt = datetime(2023, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
    assert encoder.default(dt) == dt.timestamp()

    # Test encoding of UUID
    uuid_obj = UUID('12345678123456781234567812345678')
    assert encoder.default(uuid_obj) == str(uuid_obj)

    # Test encoding of Enum

# Generated at 2024-03-18 05:15:36.290118
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():    # Test encoding of various types using _ExtendedEncoder
    encoder = _ExtendedEncoder()

    # Test encoding of a collection - list
    assert encoder.default([1, 2, 3]) == [1, 2, 3]

    # Test encoding of a collection - dict
    assert encoder.default({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}

    # Test encoding of a datetime object
    dt = datetime(2021, 1, 1, 12, 0, tzinfo=timezone.utc)
    assert encoder.default(dt) == dt.timestamp()

    # Test encoding of a UUID
    uuid_obj = UUID('12345678123456781234567812345678')
    assert encoder.default(uuid_obj) == str(uuid_obj)

    # Test encoding of an Enum
    class Color(Enum):
        RED = 1
        GREEN = 2
       

# Generated at 2024-03-18 05:15:41.436496
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():    # Test encoding of collections
    assert json.dumps([1, 2, 3], cls=_ExtendedEncoder) == '[1, 2, 3]'
    assert json.dumps({'a': 1, 'b': 2}, cls=_ExtendedEncoder) == '{"a": 1, "b": 2}'

    # Test encoding of datetime
    dt = datetime(2021, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
    assert json.dumps(dt, cls=_ExtendedEncoder) == str(dt.timestamp())

    # Test encoding of UUID
    uuid_val = UUID('12345678123456781234567812345678')
    assert json.dumps(uuid_val, cls=_ExtendedEncoder) == '"12345678-1234-5678-1234-567812345678"'

    # Test encoding of Enum
    class Color(Enum):
        RED = 1
        GREEN

# Generated at 2024-03-18 05:15:48.960542
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():    # Test encoding of various types using _ExtendedEncoder
    encoder = _ExtendedEncoder()

    # Test encoding of a collection - list
    assert encoder.default([1, 2, 3]) == [1, 2, 3]

    # Test encoding of a collection - dict
    assert encoder.default({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}

    # Test encoding of a datetime object
    dt = datetime(2021, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
    assert encoder.default(dt) == dt.timestamp()

    # Test encoding of a UUID
    uuid_obj = UUID('12345678123456781234567812345678')
    assert encoder.default(uuid_obj) == str(uuid_obj)

    # Test encoding of an Enum
    class Color(Enum):
        RED = 1

# Generated at 2024-03-18 05:15:55.119395
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():    # Test encoding of various data types using _ExtendedEncoder
    encoder = _ExtendedEncoder()

    # Test encoding of collection types (list and dict)
    assert encoder.default([1, 2, 3]) == [1, 2, 3]
    assert encoder.default({'key': 'value'}) == {'key': 'value'}

    # Test encoding of datetime
    dt = datetime(2021, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
    assert encoder.default(dt) == dt.timestamp()

    # Test encoding of UUID
    uuid_obj = UUID('12345678123456781234567812345678')
    assert encoder.default(uuid_obj) == str(uuid_obj)

    # Test encoding of Enum
    class Color(Enum):
        RED = 1
        GREEN = 2
        BLUE = 3
    assert encoder.default(Color.RED) == Color.RED.value

    # Test

# Generated at 2024-03-18 05:16:01.845511
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():    # Test encoding of various types using _ExtendedEncoder
    encoder = _ExtendedEncoder()

    # Test encoding of collection types (list, set, dict)
    assert encoder.default([1, 2, 3]) == [1, 2, 3]
    assert encoder.default({1, 2, 3}) == [1, 2, 3]
    assert encoder.default({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}

    # Test encoding of datetime
    dt = datetime(2021, 1, 1, 12, 0, tzinfo=timezone.utc)
    assert encoder.default(dt) == dt.timestamp()

    # Test encoding of UUID
    uuid_obj = UUID('12345678123456781234567812345678')
    assert encoder.default(uuid_obj) == str(uuid_obj)

    # Test encoding of Enum

# Generated at 2024-03-18 05:16:07.603232
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():    # Test encoding of various types using _ExtendedEncoder
    encoder = _ExtendedEncoder()

    # Test encoding of a collection - list
    assert encoder.default([1, 2, 3]) == [1, 2, 3]

    # Test encoding of a collection - dict
    assert encoder.default({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}

    # Test encoding of a datetime object
    dt = datetime(2021, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
    assert encoder.default(dt) == dt.timestamp()

    # Test encoding of a UUID
    uuid_obj = UUID('12345678123456781234567812345678')
    assert encoder.default(uuid_obj) == str(uuid_obj)

    # Test encoding of an Enum
    class Color(Enum):
        RED = 1

# Generated at 2024-03-18 05:16:52.581325
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():    # Test encoding of various types using _ExtendedEncoder
    encoder = _ExtendedEncoder()

    # Test encoding of a collection - list
    assert encoder.default([1, 2, 3]) == [1, 2, 3]

    # Test encoding of a collection - dict
    assert encoder.default({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}

    # Test encoding of a datetime object
    dt = datetime(2021, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
    assert encoder.default(dt) == dt.timestamp()

    # Test encoding of a UUID
    uuid_obj = UUID('12345678123456781234567812345678')
    assert encoder.default(uuid_obj) == str(uuid_obj)

    # Test encoding of an Enum
    class Color(Enum):
        RED = 1
       

# Generated at 2024-03-18 05:17:00.293933
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():    # Test encoding of various types using _ExtendedEncoder
    encoder = _ExtendedEncoder()

    # Test encoding of collection types
    assert encoder.default([1, 2, 3]) == [1, 2, 3]
    assert encoder.default({'key': 'value'}) == {'key': 'value'}

    # Test encoding of datetime
    dt = datetime(2021, 1, 1, 12, 0, tzinfo=timezone.utc)
    assert encoder.default(dt) == dt.timestamp()

    # Test encoding of UUID
    uuid_obj = UUID('12345678123456781234567812345678')
    assert encoder.default(uuid_obj) == str(uuid_obj)

    # Test encoding of Enum
    class Color(Enum):
        RED = 1
        GREEN = 2
        BLUE = 3
    assert encoder.default(Color.RED) == Color.RED.value

    # Test encoding of Decimal

# Generated at 2024-03-18 05:17:05.987733
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():    # Test encoding of various types using _ExtendedEncoder
    encoder = _ExtendedEncoder()

    # Test encoding of a collection - list
    assert encoder.default([1, 2, 3]) == [1, 2, 3]

    # Test encoding of a collection - dict
    assert encoder.default({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}

    # Test encoding of a datetime object
    dt = datetime(2021, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
    assert encoder.default(dt) == dt.timestamp()

    # Test encoding of a UUID
    uuid_obj = UUID('12345678123456781234567812345678')
    assert encoder.default(uuid_obj) == str(uuid_obj)

    # Test encoding of an Enum
    class Color(Enum):
        RED = 1

# Generated at 2024-03-18 05:17:11.406876
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():    # Test encoding of various types using _ExtendedEncoder
    encoder = _ExtendedEncoder()

    # Test encoding of a collection - list
    assert encoder.default([1, 2, 3]) == [1, 2, 3]

    # Test encoding of a collection - dict
    assert encoder.default({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}

    # Test encoding of a datetime object
    dt = datetime(2021, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
    assert encoder.default(dt) == dt.timestamp()

    # Test encoding of a UUID
    uuid_obj = UUID('12345678123456781234567812345678')
    assert encoder.default(uuid_obj) == str(uuid_obj)

    # Test encoding of an Enum
    class Color(Enum):
        RED = 1

# Generated at 2024-03-18 05:17:16.309805
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():    # Create an instance of the _ExtendedEncoder
    encoder = _ExtendedEncoder()

    # Test encoding of various data types
    # Test encoding of a collection - list
    assert encoder.default([1, 2, 3]) == [1, 2, 3]
    # Test encoding of a collection - dict
    assert encoder.default({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}
    # Test encoding of a datetime object
    dt = datetime(2021, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
    assert encoder.default(dt) == dt.timestamp()
    # Test encoding of a UUID
    uuid_obj = UUID('12345678123456781234567812345678')
    assert encoder.default(uuid_obj) == str(uuid_obj)
    # Test encoding of an Enum
    class Color(Enum):
        RED

# Generated at 2024-03-18 05:17:21.563358
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():    # Test encoding of various types using _ExtendedEncoder
    encoder = _ExtendedEncoder()

    # Test encoding of a collection - list
    assert encoder.default([1, 2, 3]) == [1, 2, 3]

    # Test encoding of a collection - dict
    assert encoder.default({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}

    # Test encoding of a datetime object
    dt = datetime(2023, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
    assert encoder.default(dt) == dt.timestamp()

    # Test encoding of a UUID
    uuid_obj = UUID('12345678123456781234567812345678')
    assert encoder.default(uuid_obj) == str(uuid_obj)

    # Test encoding of an Enum
    class Color(Enum):
        RED = 1

# Generated at 2024-03-18 05:17:28.889425
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():    # Test encoding of various types using _ExtendedEncoder
    encoder = _ExtendedEncoder()

    # Test encoding of collection types
    assert encoder.default([1, 2, 3]) == [1, 2, 3]
    assert encoder.default({'key': 'value'}) == {'key': 'value'}

    # Test encoding of datetime
    dt = datetime(2021, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
    assert encoder.default(dt) == dt.timestamp()

    # Test encoding of UUID
    uuid_obj = UUID('12345678123456781234567812345678')
    assert encoder.default(uuid_obj) == str(uuid_obj)

    # Test encoding of Enum
    class Color(Enum):
        RED = 1
        GREEN = 2
        BLUE = 3
    assert encoder.default(Color.RED) == Color.RED.value

    # Test encoding of Decimal
   

# Generated at 2024-03-18 05:17:35.666446
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():    # Test encoding of various types using _ExtendedEncoder
    encoder = _ExtendedEncoder()

    # Test encoding of collection types
    assert encoder.default([1, 2, 3]) == [1, 2, 3]
    assert encoder.default({'key': 'value'}) == {'key': 'value'}

    # Test encoding of datetime
    dt = datetime(2021, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
    assert encoder.default(dt) == dt.timestamp()

    # Test encoding of UUID
    uuid_obj = UUID('12345678123456781234567812345678')
    assert encoder.default(uuid_obj) == str(uuid_obj)

    # Test encoding of Enum
    class Color(Enum):
        RED = 1
        GREEN = 2
        BLUE = 3
    assert encoder.default(Color.RED) == Color.RED.value

    # Test encoding of Decimal
   

# Generated at 2024-03-18 05:17:41.924554
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():    # Test encoding of various types using _ExtendedEncoder
    encoder = _ExtendedEncoder()

    # Test encoding of a collection - list
    assert encoder.default([1, 2, 3]) == [1, 2, 3]

    # Test encoding of a collection - dict
    assert encoder.default({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}

    # Test encoding of a datetime object
    dt = datetime(2021, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
    assert encoder.default(dt) == dt.timestamp()

    # Test encoding of a UUID
    uuid_obj = UUID('12345678123456781234567812345678')
    assert encoder.default(uuid_obj) == str(uuid_obj)

    # Test encoding of an Enum
    class Color(Enum):
        RED = 1

# Generated at 2024-03-18 05:17:48.208013
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():    # Test encoding of collections
    assert json.dumps([1, 2, 3], cls=_ExtendedEncoder) == '[1, 2, 3]'
    assert json.dumps({'a': 1, 'b': 2}, cls=_ExtendedEncoder) == '{"a": 1, "b": 2}'

    # Test encoding of datetime
    dt = datetime(2021, 1, 1, 12, 0, tzinfo=timezone.utc)
    assert json.dumps(dt, cls=_ExtendedEncoder) == str(dt.timestamp())

    # Test encoding of UUID
    uuid_val = UUID('12345678123456781234567812345678')
    assert json.dumps(uuid_val, cls=_ExtendedEncoder) == '"12345678-1234-5678-1234-567812345678"'

    # Test encoding of Enum
    class Color(Enum):
        RED = 1
        GREEN = 2

# Generated at 2024-03-18 05:19:09.005388
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():    # Test encoding of various types using _ExtendedEncoder
    encoder = _ExtendedEncoder()

    # Test encoding of a collection - list
    assert encoder.default([1, 2, 3]) == [1, 2, 3]

    # Test encoding of a collection - dict
    assert encoder.default({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}

    # Test encoding of a datetime object
    dt = datetime(2021, 1, 1, 12, 0, tzinfo=timezone.utc)
    assert encoder.default(dt) == dt.timestamp()

    # Test encoding of a UUID
    uuid_obj = UUID('12345678123456781234567812345678')
    assert encoder.default(uuid_obj) == str(uuid_obj)

    # Test encoding of an Enum
    class Color(Enum):
        RED = 1
        GREEN = 2
       

# Generated at 2024-03-18 05:19:17.222782
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():    encoder = _ExtendedEncoder()

    # Test encoding of collection types

# Generated at 2024-03-18 05:19:25.447517
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():    # Test encoding of various types using _ExtendedEncoder
    encoder = _ExtendedEncoder()

    # Test encoding of a collection (list)
    assert encoder.default([1, 2, 3]) == [1, 2, 3]

    # Test encoding of a mapping (dict)
    assert encoder.default({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}

    # Test encoding of a datetime object
    dt = datetime(2021, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
    assert encoder.default(dt) == dt.timestamp()

    # Test encoding of a UUID
    uuid_obj = UUID('12345678123456781234567812345678')
    assert encoder.default(uuid_obj) == str(uuid_obj)

    # Test encoding of an Enum
    class Color(Enum):
        RED = 1
       

# Generated at 2024-03-18 05:19:32.238770
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():    # Test encoding of various types using _ExtendedEncoder
    encoder = _ExtendedEncoder()

    # Test encoding of a collection - list
    assert encoder.default([1, 2, 3]) == [1, 2, 3]

    # Test encoding of a collection - dict
    assert encoder.default({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}

    # Test encoding of a datetime object
    dt = datetime(2021, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
    assert encoder.default(dt) == dt.timestamp()

    # Test encoding of a UUID
    uuid_obj = UUID('12345678123456781234567812345678')
    assert encoder.default(uuid_obj) == str(uuid_obj)

    # Test encoding of an Enum
    class Color(Enum):
        RED = 1

# Generated at 2024-03-18 05:19:38.691795
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():    encoder = _ExtendedEncoder()

    # Test encoding of collection types (list and dict)

# Generated at 2024-03-18 05:19:44.638772
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():    # Create an instance of the _ExtendedEncoder
    encoder = _ExtendedEncoder()

    # Test encoding of various data types
    # Test encoding of a collection - list
    assert encoder.default([1, 2, 3]) == [1, 2, 3]
    # Test encoding of a collection - dict
    assert encoder.default({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}
    # Test encoding of a datetime object
    dt = datetime(2021, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
    assert encoder.default(dt) == dt.timestamp()
    # Test encoding of a UUID
    uuid_obj = UUID('12345678123456781234567812345678')
    assert encoder.default(uuid_obj) == str(uuid_obj)
    # Test encoding of an Enum
    class Color(Enum):
        RED

# Generated at 2024-03-18 05:19:54.156316
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():    # Test encoding of various types using _ExtendedEncoder
    encoder = _ExtendedEncoder()

    # Test encoding of a collection - list
    assert encoder.default([1, 2, 3]) == [1, 2, 3]

    # Test encoding of a collection - dict
    assert encoder.default({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}

    # Test encoding of a datetime object
    dt = datetime(2021, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
    assert encoder.default(dt) == dt.timestamp()

    # Test encoding of a UUID
    uuid_obj = UUID('12345678123456781234567812345678')
    assert encoder.default(uuid_obj) == str(uuid_obj)

    # Test encoding of an Enum
    class Color(Enum):
        RED = 1
       

# Generated at 2024-03-18 05:20:02.257609
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():    # Test encoding of collections
    assert json.dumps([1, 2, 3], cls=_ExtendedEncoder) == '[1, 2, 3]'
    assert json.dumps({'a': 1, 'b': 2}, cls=_ExtendedEncoder) == '{"a": 1, "b": 2}'

    # Test encoding of datetime
    dt = datetime(2021, 1, 1, 12, 0, tzinfo=timezone.utc)
    assert json.dumps(dt, cls=_ExtendedEncoder) == str(dt.timestamp())

    # Test encoding of UUID
    uuid_val = UUID('12345678123456781234567812345678')
    assert json.dumps(uuid_val, cls=_ExtendedEncoder) == '"12345678-1234-5678-1234-567812345678"'

    # Test encoding of Enum
    class Color(Enum):
        RED = 1
        GREEN = 2

# Generated at 2024-03-18 05:20:10.771620
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():    # Test encoding of various types using _ExtendedEncoder
    encoder = _ExtendedEncoder()

    # Test encoding of a collection - list
    assert encoder.default([1, 2, 3]) == [1, 2, 3]

    # Test encoding of a collection - dict
    assert encoder.default({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}

    # Test encoding of a datetime object
    dt = datetime(2021, 1, 1, 12, 0, tzinfo=timezone.utc)
    assert encoder.default(dt) == dt.timestamp()

    # Test encoding of a UUID
    uuid_obj = UUID('12345678123456781234567812345678')
    assert encoder.default(uuid_obj) == str(uuid_obj)

    # Test encoding of an Enum
    class Color(Enum):
        RED = 1
        GREEN = 2
       

# Generated at 2024-03-18 05:20:17.466584
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():    # Test encoding of various types using _ExtendedEncoder
    encoder = _ExtendedEncoder()

    # Test encoding of a collection - list
    assert encoder.default([1, 2, 3]) == [1, 2, 3]

    # Test encoding of a collection - dict
    assert encoder.default({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}

    # Test encoding of a datetime object
    dt = datetime(2021, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
    assert encoder.default(dt) == dt.timestamp()

    # Test encoding of a UUID
    uuid_obj = UUID('12345678123456781234567812345678')
    assert encoder.default(uuid_obj) == str(uuid_obj)

    # Test encoding of an Enum
    class Color(Enum):
        RED = 1

# Generated at 2024-03-18 05:21:52.917034
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():    # Test encoding of various types using _ExtendedEncoder
    encoder = _ExtendedEncoder()

    # Test encoding of collection types
    assert encoder.default([1, 2, 3]) == [1, 2, 3]
    assert encoder.default({'key': 'value'}) == {'key': 'value'}

    # Test encoding of datetime
    dt = datetime(2021, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
    assert encoder.default(dt) == dt.timestamp()

    # Test encoding of UUID
    uuid_obj = UUID('12345678123456781234567812345678')
    assert encoder.default(uuid_obj) == str(uuid_obj)

    # Test encoding of Enum
    class Color(Enum):
        RED = 1
        GREEN = 2
        BLUE = 3
    assert encoder.default(Color.RED) == Color.RED.value

    # Test encoding of Decimal
   

# Generated at 2024-03-18 05:21:59.234120
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():    # Create an instance of the _ExtendedEncoder
    encoder = _ExtendedEncoder()

    # Test with a collection that is a mapping
    mapping = {'key1': 'value1', 'key2': 'value2'}
    assert encoder.default(mapping) == mapping

    # Test with a collection that is not a mapping
    collection = [1, 2, 3]
    assert encoder.default(collection) == collection

    # Test with a datetime object
    dt = datetime(2021, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
    assert encoder.default(dt) == dt.timestamp()

    # Test with a UUID object
    uuid_obj = UUID('12345678123456781234567812345678')
    assert encoder.default(uuid_obj) == str(uuid_obj)

    # Test with an Enum object
    class Color(Enum):
        RED = 1
        GREEN = 2


# Generated at 2024-03-18 05:22:06.364105
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():    # Test encoding of collections
    assert json.dumps([1, 2, 3], cls=_ExtendedEncoder) == '[1, 2, 3]'
    assert json.dumps({1: 'a', 2: 'b'}, cls=_ExtendedEncoder) == '{"1": "a", "2": "b"}'

    # Test encoding of datetime
    dt = datetime(2021, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
    assert json.dumps(dt, cls=_ExtendedEncoder) == str(dt.timestamp())

    # Test encoding of UUID
    uuid_obj = UUID('12345678123456781234567812345678')
    assert json.dumps(uuid_obj, cls=_ExtendedEncoder) == '"12345678-1234-5678-1234-567812345678"'

    # Test encoding of Enum
    class Color(Enum):
        RED = 1
        GREEN

# Generated at 2024-03-18 05:22:14.732273
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():    # Test encoding of various types using _ExtendedEncoder
    encoder = _ExtendedEncoder()

    # Test encoding of a collection (list)
    assert encoder.default([1, 2, 3]) == [1, 2, 3]

    # Test encoding of a mapping (dict)
    assert encoder.default({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}

    # Test encoding of a datetime object
    dt = datetime(2021, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
    assert encoder.default(dt) == dt.timestamp()

    # Test encoding of a UUID
    uuid_obj = UUID('12345678123456781234567812345678')
    assert encoder.default(uuid_obj) == str(uuid_obj)

    # Test encoding of an Enum
    class Color(Enum):
        RED = 1

# Generated at 2024-03-18 05:22:20.796636
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():    # Test encoding of various types using _ExtendedEncoder
    encoder = _ExtendedEncoder()

    # Test encoding of a collection - list
    assert encoder.default([1, 2, 3]) == [1, 2, 3]

    # Test encoding of a collection - dict
    assert encoder.default({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}

    # Test encoding of a datetime object
    dt = datetime(2021, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
    assert encoder.default(dt) == dt.timestamp()

    # Test encoding of a UUID
    uuid_obj = UUID('12345678123456781234567812345678')
    assert encoder.default(uuid_obj) == str(uuid_obj)

    # Test encoding of an Enum
    class Color(Enum):
        RED = 1
       

# Generated at 2024-03-18 05:22:34.381936
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():    # Test encoding of various types using _ExtendedEncoder
    encoder = _ExtendedEncoder()

    # Test encoding of a collection - list
    assert encoder.default([1, 2, 3]) == [1, 2, 3]

    # Test encoding of a collection - dict
    assert encoder.default({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}

    # Test encoding of a datetime object
    dt = datetime(2020, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
    assert encoder.default(dt) == 1577880000.0

    # Test encoding of a UUID
    uuid_obj = UUID('12345678123456781234567812345678')
    assert encoder.default(uuid_obj) == '12345678-1234-5678-1234-567812345678'

    # Test

# Generated at 2024-03-18 05:22:46.530803
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():    # Test encoding of various types using _ExtendedEncoder
    encoder = _ExtendedEncoder()

    # Test encoding of collection types (list, set, dict)
    assert encoder.default([1, 2, 3]) == [1, 2, 3]
    assert encoder.default({1, 2, 3}) == [1, 2, 3]
    assert encoder.default({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}

    # Test encoding of datetime
    dt = datetime(2021, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
    assert encoder.default(dt) == dt.timestamp()

    # Test encoding of UUID
    uuid_obj = UUID('12345678123456781234567812345678')
    assert encoder.default(uuid_obj) == str(uuid_obj)

    # Test encoding of Enum

# Generated at 2024-03-18 05:22:53.143904
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():    # Test encoding of various types using _ExtendedEncoder
    encoder = _ExtendedEncoder()

    # Test encoding of a collection - list
    assert encoder.default([1, 2, 3]) == [1, 2, 3]

    # Test encoding of a collection - dict
    assert encoder.default({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}

    # Test encoding of a datetime object
    dt = datetime(2021, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
    assert encoder.default(dt) == dt.timestamp()

    # Test encoding of a UUID
    uuid_obj = UUID('12345678123456781234567812345678')
    assert encoder.default(uuid_obj) == str(uuid_obj)

    # Test encoding of an Enum
    class Color(Enum):
        RED = 1

# Generated at 2024-03-18 05:23:00.036266
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():    # Test encoding of various types using _ExtendedEncoder
    encoder = _ExtendedEncoder()

    # Test encoding of a collection - list
    assert encoder.default([1, 2, 3]) == [1, 2, 3]

    # Test encoding of a collection - dict
    assert encoder.default({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}

    # Test encoding of a datetime object
    dt = datetime(2021, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
    assert encoder.default(dt) == dt.timestamp()

    # Test encoding of a UUID
    uuid_obj = UUID('12345678123456781234567812345678')
    assert encoder.default(uuid_obj) == str(uuid_obj)

    # Test encoding of an Enum
    class Color(Enum):
        RED = 1

# Generated at 2024-03-18 05:23:08.594099
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():    encoder = _ExtendedEncoder()

    # Test encoding of collection types