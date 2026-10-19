

# Generated at 2022-06-13 19:09:48.027929
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    print('test_Exclude_NEVER')
    params = ['a', 'b', 'c', 'd', 'e']
    for p in params:
        assert Exclude.NEVER(p)


# Generated at 2022-06-13 19:09:54.587990
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True
    assert Exclude.ALWAYS('a') == True
    assert Exclude.ALWAYS(3.4) == True
    assert Exclude.ALWAYS([1, 2]) == True
    assert Exclude.ALWAYS((1, 2)) == True
    assert Exclude.ALWAYS({1: 'a', 2: 'b'}) == True


# Generated at 2022-06-13 19:09:57.332044
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    # Test for nothing.
    assert Exclude.NEVER(None) == False


# Generated at 2022-06-13 19:09:59.052389
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    data = 2
    assert(Exclude.ALWAYS(data) == True)


# Generated at 2022-06-13 19:10:02.088916
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert(Exclude.ALWAYS(3) == True)
    assert(Exclude.ALWAYS(0) == True)
    assert(Exclude.ALWAYS(4) == True)
    assert(Exclude.ALWAYS(None) == True)
    assert(Exclude.ALWAYS("") == True)


# Generated at 2022-06-13 19:10:10.595737
# Unit test for function config
def test_config():
    from dataclasses import dataclass, field

    d = {'dataclasses_json': {}}

    @dataclass
    class A:
        f1: int
        f2: str = field(metadata=config(d))

    assert d == {'dataclasses_json': {
        'f2': {'exclude': 'always'}
    }}

    d = {'dataclasses_json': {}}

    @dataclass
    class A:
        f1: int
        f2: str = field(metadata=config(d, exclude=Exclude.NEVER))

    assert d ==  {'dataclasses_json': {
        'f2': {'exclude': 'never'}
    }}

    d = {'dataclasses_json': {}}


# Generated at 2022-06-13 19:10:12.705747
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("test") == False


# Generated at 2022-06-13 19:10:14.323974
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    # assert Exclude.NEVER(None) == False
    if Exclude.NEVER(None) == True:
        print("SUCCESS")

# Generated at 2022-06-13 19:10:15.249527
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(12) == True


# Generated at 2022-06-13 19:10:17.437677
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(10) == True


# Generated at 2022-06-13 19:10:20.460395
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(123) == True


# Generated at 2022-06-13 19:10:22.124044
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    if Exclude.ALWAYS is not True:
        return False
    else:
        return True


# Generated at 2022-06-13 19:10:23.330940
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS('blah')


# Generated at 2022-06-13 19:10:24.448071
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert callable(Exclude.ALWAYS)


# Generated at 2022-06-13 19:10:25.885763
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    expected = False
    result = Exclude.NEVER(3)
    assert result == expected
    

# Generated at 2022-06-13 19:10:29.662488
# Unit test for function config
def test_config():
    try:
        config(undefined='raise')
    except UndefinedParameterError:
        pass
    else:
        raise RuntimeError("config should have raised UndefinedParameterError!")

    try:
        config(undefined='Raise')
    except UndefinedParameterError:
        raise RuntimeError("config improperly raised UndefinedParameterError!")
    except AttributeError:
        pass

    _ = config(undefined=Undefined.RAISE)



# Generated at 2022-06-13 19:10:33.392054
# Unit test for function config
def test_config():
    """
    Test config function.
    """
    @dataclass
    class Test:
        d: int = config(field_name='e')

    assert Test(2).d == 2


# Generated at 2022-06-13 19:10:35.420824
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    test1 = True
    assert Exclude.ALWAYS(test1) == True



# Generated at 2022-06-13 19:10:36.873235
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("") == True


# Generated at 2022-06-13 19:10:48.454421
# Unit test for function config
def test_config():
    from dataclasses import dataclass, field
    from dataclasses_json import config
    from marshmallow import fields

    @dataclass
    class Data:
        value: int
        text: str = None

    class TextField(fields.Field):
        def _serialize(self, value, attr, obj, **kwargs):
            return {"text": value}

    @config(exclude=Exclude.NEVER, mm_field=TextField)
    @dataclass
    class Another:
        value: int
        text: str = None

    assert Data.__dataclass_json__ == {
        (None, 'value'): {},
        (None, 'text'):  {'exclude': Exclude.NEVER}
    }


# Generated at 2022-06-13 19:10:56.342068
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(True) == False
    assert Exclude.NEVER(False) == False
    assert Exclude.NEVER(3) == False
    assert Exclude.NEVER("test") == False
    assert Exclude.NEVER([1]) == False
    assert Exclude.NEVER((1)) == False
    assert Exclude.NEVER(None) == False
    assert Exclude.NEVER(Exclude.ALWAYS) == False
    assert Exclude.NEVER(Exclude.NEVER) == False
    assert Exclude.NEVER(Exclude.NEVER()) == False


# Generated at 2022-06-13 19:10:58.623203
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(5) == True


# Generated at 2022-06-13 19:11:00.884973
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS('test') == True



# Generated at 2022-06-13 19:11:02.460311
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    pass

test_Exclude_NEVER()

# Generated at 2022-06-13 19:11:06.711721
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(True) == False
    assert Exclude.NEVER(False) == False
    assert Exclude.NEVER(None) == False


# Generated at 2022-06-13 19:11:08.177135
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    input = "test"
    result = Exclude.ALWAYS(input)
    assert result == True


# Generated at 2022-06-13 19:11:12.161513
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(0) == False
    assert Exclude.NEVER(3) == False
    assert Exclude.NEVER('asdf') == False
    assert Exclude.NEVER(True) == False
    assert Exclude.NEVER(None) == False

test_Exclude_NEVER()


# Generated at 2022-06-13 19:11:15.427363
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(True) == True
    assert Exclude.ALWAYS(False) == True


# Generated at 2022-06-13 19:11:23.321108
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(object)

# Generated at 2022-06-13 19:11:25.480332
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert(Exclude.ALWAYS(5) == True)


# Generated at 2022-06-13 19:11:30.728841
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True


# Generated at 2022-06-13 19:11:41.119457
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None)
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS(1.0)
    assert Exclude.ALWAYS(True)
    assert Exclude.ALWAYS(False)
    assert Exclude.ALWAYS('a')
    assert Exclude.ALWAYS('abc')
    assert Exclude.ALWAYS([])
    assert Exclude.ALWAYS([1, 2, 3])
    assert Exclude.ALWAYS({})
    assert Exclude.ALWAYS({'k1': 1, 'k2': 2})



# Generated at 2022-06-13 19:11:44.389500
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    test_field = 'first_name'
    test_instance = 'John'
    a = Exclude.NEVER(test_field,test_instance)
    assert a is False


# Generated at 2022-06-13 19:11:47.698823
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    try:
        print(Exclude.NEVER(1))
    except TypeError:
        print("这里有一个TypeError异常，是因为test_Exclude_NEVER()函数接收了一个int参数")


# Generated at 2022-06-13 19:11:49.279198
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True


# Generated at 2022-06-13 19:11:51.512050
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
	assert Exclude.ALWAYS(3) == True


# Generated at 2022-06-13 19:11:52.555217
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1)

# Generated at 2022-06-13 19:11:54.160087
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(None) == False


# Generated at 2022-06-13 19:11:58.943156
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(True) == False
    assert Exclude.NEVER(False) == False
    assert Exclude.NEVER(None) == False
    assert Exclude.NEVER("True") == False
    assert Exclude.NEVER("False") == False
    assert Exclude.NEVER("True and False") == False


# Generated at 2022-06-13 19:12:00.210333
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None)


# Generated at 2022-06-13 19:12:07.841145
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1)==False

# Generated at 2022-06-13 19:12:10.067298
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None) is True
    assert Exclude.ALWAYS("") is True


# Generated at 2022-06-13 19:12:12.061966
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(0)
    assert not Exclude.NEVER(1)


# Generated at 2022-06-13 19:12:19.412013
# Unit test for function config
def test_config():
    from dataclasses import dataclass, field

    @dataclass
    @config(
        encoder=lambda o: o.__dict__,
        decoder=lambda d: d['name'])
    class Test:
        name: str = 'Default'

    assert Test().name == 'Default'

    t = Test('Bob')
    assert Test.from_json(t.to_json()) == Test('Bob')



# Generated at 2022-06-13 19:12:20.625088
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    a = Exclude.NEVER(2)
    assert a == False


# Generated at 2022-06-13 19:12:21.810138
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("hello") is True


# Generated at 2022-06-13 19:12:23.081858
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER('s')

# Generated at 2022-06-13 19:12:24.575445
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None)



# Generated at 2022-06-13 19:12:25.850915
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("abc") == False

# Generated at 2022-06-13 19:12:26.668455
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(2) == True
    assert Exclude.ALWAYS(3) == True


# Generated at 2022-06-13 19:12:42.639948
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    try:
       x = Exclude.NEVER(1)
    except:
       x = False
    assert x == False


# Generated at 2022-06-13 19:12:43.990713
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None)


# Generated at 2022-06-13 19:12:45.622692
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("a") == False

# Generated at 2022-06-13 19:12:54.464854
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) is False


# Generated at 2022-06-13 19:12:57.184954
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("") == False
    assert Exclude.NEVER(None) == False


# Generated at 2022-06-13 19:12:58.529872
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER('anything')


# Generated at 2022-06-13 19:13:01.368884
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(7) == False
    assert Exclude.NEVER('banana') == False
    assert Exclude.NEVER(True) == False


# Generated at 2022-06-13 19:13:10.680120
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS('test_data')


# Generated at 2022-06-13 19:13:20.567720
# Unit test for function config
def test_config():
    empty_metadata = {'dataclasses_json': {}}
    # Verify that config won't overwrite anything if no new information is passed
    assert empty_metadata == config(metadata=empty_metadata)
    encoder = lambda x: x
    decoder = lambda x: x
    mm_field = 'test'
    field_name = 'field_name'
    assert {'dataclasses_json': {'encoder': encoder}} == config(encoder=encoder)
    assert {'dataclasses_json': {'decoder': decoder}} == config(decoder=decoder)
    assert {'dataclasses_json': {'mm_field': mm_field}} == config(mm_field=mm_field)

# Generated at 2022-06-13 19:13:23.236846
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(5) == True
    assert Exclude.ALWAYS(-2) == True
    assert Exclude.ALWAYS(0) == True
    assert Exclude.ALWAYS("") == True
    assert Exclude.ALWAYS("hey") == True
    assert Exclude.ALWAYS(False) == True
    assert Exclude.ALWAYS(True) == True


# Generated at 2022-06-13 19:13:52.291093
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    obj = Exclude()
    result = obj.NEVER('a field')
    assert result == False


# Generated at 2022-06-13 19:13:53.327960
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("data") == False


# Generated at 2022-06-13 19:13:54.306330
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(2) == False


# Generated at 2022-06-13 19:13:55.237231
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(None) == False


# Generated at 2022-06-13 19:13:56.064713
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True
    return None


# Generated at 2022-06-13 19:13:57.290246
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
	if Exclude.ALWAYS(5):
		return True
	return False


# Generated at 2022-06-13 19:13:58.565460
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1)  # Check if field is excluded


# Generated at 2022-06-13 19:14:03.281144
# Unit test for function config
def test_config():
    from dataclasses import dataclass

    @dataclass
    class Config:
        _: int = config(decoder=int, encoder=str)
        __: int = config(mm_field=int)
        ___: int = config(undefined=str)
        ____: int = config(field_name='123')
        _____: int = config(exclude=int, undefined=str)


# vim: et:sw=4:syntax=python:ts=4:

# Generated at 2022-06-13 19:14:04.948394
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS is Exclude.ALWAYS


# Generated at 2022-06-13 19:14:11.227183
# Unit test for function config
def test_config():
    @config(undefined='exception')
    class Test:
        pass

    assert Test.__dataclasses_json__['undefined'] == Undefined.EXCEPTION

    try:
        @config(undefined='invalid')
        class Test:
            pass
        assert False, "Test should have raised an exception"
    except UndefinedParameterError:
        pass

    try:
        @config(undefined=42)
        class Test:
            pass
        assert False, "Test should have raised an exception"
    except UndefinedParameterError:
        pass

# Generated at 2022-06-13 19:15:18.501279
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    Exclude.ALWAYS("a")


# Generated at 2022-06-13 19:15:23.886446
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None)
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS(3.14)
    assert Exclude.ALWAYS(True)
    assert Exclude.ALWAYS(['a', 'b'])
    assert Exclude.ALWAYS(dict())


# Generated at 2022-06-13 19:15:32.061020
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(None) == False


# Generated at 2022-06-13 19:15:34.011944
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS('f') == True


# Generated at 2022-06-13 19:15:40.357864
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert(Exclude.ALWAYS[0] == True)
    assert(Exclude.ALWAYS[1] == True)
    assert(Exclude.ALWAYS["a"] == True)
    assert(Exclude.ALWAYS[None] == True)
    assert(Exclude.ALWAYS["abc"] == True)

# Generated at 2022-06-13 19:15:42.297834
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert(Exclude.NEVER(0) == False)


# Generated at 2022-06-13 19:15:44.010504
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False


# Generated at 2022-06-13 19:15:54.408639
# Unit test for function config
def test_config():
    import marshmallow as mm
    from marshmallow.fields import String
    import json

    @config(encoder=json.dumps, decoder=json.loads,
            mm_field=String(missing=None))
    @dataclass
    class Test:
        x: str
        y: str = field(metadata=config(exclude=Exclude.ALWAYS))
        z: str = field(metadata=config(exclude=Exclude.NEVER))

    assert global_config.encoders[str] == json.dumps
    assert global_config.decoders[str] == json.loads
    assert global_config.mm_fields[str] is String
    assert Test.__dataclasses_json__['encoder'] == json.dumps

# Generated at 2022-06-13 19:15:55.561909
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS('true')

# Generated at 2022-06-13 19:16:00.622875
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1)  == True
    assert Exclude.ALWAYS(0)  == True
    assert Exclude.ALWAYS(-1) == True
    assert Exclude.ALWAYS('') == True
    assert Exclude.ALWAYS('0') == True
    assert Exclude.ALWAYS('1') == True
    assert Exclude.ALWAYS('-1') == True
    assert Exclude.ALWAYS('a') == True


# Generated at 2022-06-13 19:18:31.469783
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(3)
    assert Exclude.ALWAYS('hello')
    assert Exclude.ALWAYS(Exclude.ALWAYS)


# Generated at 2022-06-13 19:18:32.772407
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    def _NEVER(foo):
        return False
    assert Exclude.NEVER == _NEVER


# Generated at 2022-06-13 19:18:33.722098
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(None)



# Generated at 2022-06-13 19:18:40.038457
# Unit test for function config
def test_config():
    from marshmallow import Schema, fields
    from dataclasses import dataclass
    from dataclasses_json import config
    from typing import Optional

    @dataclass
    class Foo:
        i: int

    @dataclass
    class Bar:
        foo: Foo

    class BarSchema(Schema):
        foo = fields.Nested('FooSchema')

    @dataclass
    class Spam:
        bar: Bar

    class SpamSchema(Schema):
        bar = fields.Nested('BarSchema')

    # encoder, decoder
    @config(encoder=lambda o: 1)
    class Foo:
        i: int

    assert Foo(i=2).encode() == '1'


# Generated at 2022-06-13 19:18:40.894775
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(True) is False
    assert Exclude.NEVER(False) is False

# Generated at 2022-06-13 19:18:42.020897
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS('string') is True


# Generated at 2022-06-13 19:18:44.299371
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    class Test:
        def __init__(self):
            self.num = 0
    t = Test()
    output = Exclude.NEVER(t)
    assert output == False


# Generated at 2022-06-13 19:18:45.634698
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(None) == False


# Generated at 2022-06-13 19:18:49.548509
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("") == False
    assert Exclude.NEVER(" ") == False
    assert Exclude.NEVER("1") == False


# Generated at 2022-06-13 19:18:54.045645
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(False)
    assert Exclude.NEVER(True)
    assert Exclude.NEVER(1)
    assert Exclude.NEVER(0)
    assert Exclude.NEVER([])
    assert Exclude.NEVER([1, 2, 3])
    assert Exclude.NEVER([0, 0, 0])
