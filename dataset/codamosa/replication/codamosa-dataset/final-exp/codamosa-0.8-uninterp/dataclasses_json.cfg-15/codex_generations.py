

# Generated at 2022-06-13 19:09:45.927217
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("test") == False


# Generated at 2022-06-13 19:09:50.492342
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    a = Exclude.ALWAYS(1)
    assert a == True
    b = Exclude.ALWAYS("1")
    assert b == True
    c = Exclude.ALWAYS(True)
    assert c == True


# Generated at 2022-06-13 19:09:52.497917
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    a = 'test'
    assert Exclude.NEVER(a) == False


# Generated at 2022-06-13 19:09:55.552225
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    """[Check] Exclusion of field"""
    assert Exclude.NEVER('dummy_param') == False


# Generated at 2022-06-13 19:09:57.493752
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True


# Generated at 2022-06-13 19:10:01.570157
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False
    assert Exclude.NEVER(0) == False
    assert Exclude.NEVER(None) == False
    assert Exclude.NEVER(True) == False
    assert Exclude.NEVER(False) == False
    assert Exclude.NEVER("") == False


# Generated at 2022-06-13 19:10:03.612242
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(4) == False
    assert Exclude.NEVER(0) == False
    assert Exclude.NEVER(11) == False


# Generated at 2022-06-13 19:10:05.015894
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
	assert Exclude.NEVER('a') == False


# Generated at 2022-06-13 19:10:06.403337
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    res = Exclude.ALWAYS(5)

    assert(res)


# Generated at 2022-06-13 19:10:09.991177
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(8)
    assert Exclude.ALWAYS([])


# Generated at 2022-06-13 19:10:19.014417
# Unit test for function config
def test_config():
    metadata = {}

    # Test default values
    default_config = {'letter_case': 'PASCAL'}
    assert config(metadata)['dataclasses_json'] == default_config
    assert metadata['dataclasses_json'] == default_config

    # Test override
    override_config = {'exclude': Exclude.ALWAYS}
    assert config(metadata, **override_config)['dataclasses_json'] == override_config
    expected_config = {
        'letter_case': 'PASCAL',
        'exclude': Exclude.ALWAYS
    }
    assert metadata['dataclasses_json'] == expected_config

    # Test explicit
    explicit_config = {'undefined': Undefined.STRICT}
    assert config(metadata, **explicit_config)['dataclasses_json'] == explicit

# Generated at 2022-06-13 19:10:20.367218
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1)


# Generated at 2022-06-13 19:10:22.005197
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True
    assert Exclude.ALWAYS(0) == True


# Generated at 2022-06-13 19:10:24.778159
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    always = Exclude.ALWAYS
    assert always(1)
    assert always({})
    assert always([])
    assert always(True)
    assert always(False)
    assert always(None)
    assert always("")


# Generated at 2022-06-13 19:10:26.048005
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(10) == False


# Generated at 2022-06-13 19:10:29.352204
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    test_class = Exclude()
    result = test_class.ALWAYS(True)
    assert result == True



# Generated at 2022-06-13 19:10:41.116567
# Unit test for function config
def test_config():
    import pytest
    from dataclasses_json import config

    @config(exclude=Exclude.NEVER)
    @dataclass
    class TestConf:
        pass

    @dataclass
    class TestConf:
        test: int = field(metadata=config(exclude=Exclude.NEVER))

    # Test if the metadata is propagating.
    assert dataclasses.asdict(TestConf()) == {'test': 0}

    @dataclass
    class TestConf:
        test: Optional[int] = field(metadata=config(undefined=Undefined.EXCLUDE))

    assert dataclasses.asdict(TestConf()) == {}

    # Test that Undefined.EXCLUDE does not have any effect here

# Generated at 2022-06-13 19:10:44.566801
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert(Exclude.NEVER(1))
    assert(Exclude.NEVER(None))
    assert(Exclude.NEVER("Hello"))
    assert(Exclude.NEVER(['a', 'b', 'c']))

# Generated at 2022-06-13 19:10:45.730782
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None) 


# Generated at 2022-06-13 19:10:48.219026
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    exclude = Exclude.NEVER
    test = True
    assert exclude(test) == False
    

# Generated at 2022-06-13 19:10:51.115178
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True
    assert Exclude.ALWAYS(2) == True


# Generated at 2022-06-13 19:10:52.231563
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    r = Exclude.ALWAYS(4)
    assert r == True


# Generated at 2022-06-13 19:10:53.054651
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1)

# Generated at 2022-06-13 19:10:54.393857
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1), "Exclude.ALWAYS() should always return True"


# Generated at 2022-06-13 19:10:56.941707
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("asd")
    

# Generated at 2022-06-13 19:10:59.217488
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False

# Generated at 2022-06-13 19:11:00.014010
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None) == True


# Generated at 2022-06-13 19:11:08.901446
# Unit test for function config
def test_config():
    import marshmallow

    from dataclasses_json.config import global_config
    from dataclasses_json.config import Exclude
    from dataclasses_json.undefined import Undefined as UNDEF

    assert global_config.encoders == {}
    assert global_config.decoders == {}
    assert global_config.mm_fields == {}

    # TODO: uncomment when implemented
    # assert global_config.json_module is json

    @config(encoder=lambda o: o + ' encoded')
    @dataclass
    class A:
        a: str

    assert global_config.encoders[A] == A.__annotations__['a'].__metadata__['dataclasses_json']['encoder']


# Generated at 2022-06-13 19:11:10.505512
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS is not None
    assert not Exclude.ALWAYS("")


# Generated at 2022-06-13 19:11:14.094923
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None) ==True
    assert Exclude.ALWAYS(1) ==True
    assert Exclude.ALWAYS('a') ==True


# Generated at 2022-06-13 19:11:18.224705
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    print(Exclude.NEVER(0))
    assert Exclude.NEVER(0) == False
    

# Generated at 2022-06-13 19:11:29.272847
# Unit test for function config
def test_config():
    # Test basic function
    config_metadata = config()
    assert config_metadata == {
        "dataclasses_json": {},
    }

    # Test config with undefined parameter
    config_metadata = config(undefined=Undefined.RAISE)
    assert config_metadata == {
        "dataclasses_json": {"undefined": Undefined.RAISE},
    }

    # Test config with undefined parameter that is a string
    config_metadata = config(undefined="skip")
    assert config_metadata == {
        "dataclasses_json": {"undefined": Undefined.SKIP},
    }

    # Test config with undefined parameter that is invalid
    with pytest.raises(UndefinedParameterError):
        config(undefined="this parameter is invalid")

    # Test config with exclude

# Generated at 2022-06-13 19:11:32.306816
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    never_result = Exclude.NEVER("a")
    
    assert never_result == False
    
test_Exclude_NEVER()

# Generated at 2022-06-13 19:11:34.225552
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True
    assert Exclude.ALWAYS('') == True


# Generated at 2022-06-13 19:11:38.246826
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert not Exclude.NEVER(1)
    assert not Exclude.NEVER([1, 2, 3])
    assert not Exclude.NEVER("Hello")
    assert not Exclude.NEVER(["Hello", "World"])
    assert not Exclude.NEVER({"key1": "value1"})
    assert not Exclude.NEVER({"key1": "value1", "key2": "value2"})


# Generated at 2022-06-13 19:11:42.845330
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False
    assert Exclude.NEVER(0) == False
    assert Exclude.NEVER([]) == False
    assert Exclude.NEVER([1]) == False
    assert Exclude.NEVER('hello') == False
    assert Exclude.NEVER('') == False
    assert Exclude.NEVER(None) == False


# Generated at 2022-06-13 19:11:46.258567
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS({}) == True
    assert Exclude.ALWAYS({'a': 1, 'b': 2}) == True
    assert Exclude.ALWAYS({'a': 1, 'b': 2}, {'a': 1, 'b': 2}) == True


# Generated at 2022-06-13 19:11:49.449326
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS(None)
    assert Exclude.ALWAYS("a")
    assert Exclude.ALWAYS(b"a")


# Generated at 2022-06-13 19:11:51.700872
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False

test_Exclude_NEVER()

# Generated at 2022-06-13 19:11:54.067036
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert isinstance(Exclude.NEVER(0),bool)
    assert Exclude.NEVER(0) == False


# Generated at 2022-06-13 19:11:58.069993
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(2)

# Generated at 2022-06-13 19:12:00.906581
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(0)
    assert Exclude.ALWAYS(False)
    assert Exclude.ALWAYS(True)
    assert Exclude.ALWAYS('')


# Generated at 2022-06-13 19:12:01.993183
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS('_') is True


# Generated at 2022-06-13 19:12:02.506519
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert NEVER(4) == False



# Generated at 2022-06-13 19:12:10.528656
# Unit test for function config
def test_config():
    from marshmallow import fields
    from dataclasses import dataclass, field

    @dataclass
    class Test:
        a: str = field(metadata=config(exclude=Exclude.ALWAYS))
        b: int = field(metadata=config(field_name='int'))
        c: float = field(metadata=config(field_name='float', letter_case=str.capitalize))
        d: int = field(metadata=config(undefined=Undefined.SKIP))
        e: str = field(metadata=config(encoder=lambda s: s.encode()))
        f: int = field(metadata=config(decoder=lambda i: int(i.decode())))
        g: str = field(metadata=config(mm_field=fields.String(validate=lambda v: int(v))))

   

# Generated at 2022-06-13 19:12:12.114014
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("hello")
    # PASS: returns True


# Generated at 2022-06-13 19:12:14.156671
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("value")


# Generated at 2022-06-13 19:12:16.959856
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    val = []
    expected = False
    result = Exclude.NEVER(val)
    assert (result == expected)


# Generated at 2022-06-13 19:12:19.808812
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    # Given
    func = Exclude.NEVER
    # When
    value = func(1)
    # Then
    assert value == False


# Generated at 2022-06-13 19:12:21.233602
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1)



# Generated at 2022-06-13 19:12:29.518286
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    import pytest
    myvalue = Exclude.ALWAYS(1)
    assert myvalue == True, "Exclude.ALWAYS(1) should return True"
    myvalue = Exclude.ALWAYS('abc')
    assert myvalue == True, "Exclude.ALWAYS('abc') should return True"

# Generated at 2022-06-13 19:12:30.887219
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    a = Exclude.NEVER("a")
    assert not a



# Generated at 2022-06-13 19:12:31.869047
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1)

# Generated at 2022-06-13 19:12:35.573570
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(None) == False
    assert Exclude.NEVER(1) == False
    assert Exclude.NEVER(True) == False
    assert Exclude.NEVER(False) == False


# Generated at 2022-06-13 19:12:37.485726
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
  assert Exclude.ALWAYS(2) == True
  

# Generated at 2022-06-13 19:12:38.718553
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("Hello")

# Generated at 2022-06-13 19:12:47.285654
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    from dataclasses import dataclass, field
    from dataclasses_json import config
    from dataclasses_json.undefined import Undefined

    @config(exclude=Exclude.NEVER)
    @dataclass
    class DataClass:
        value: float
        ones: list = field(default_factory=list, init=False)

        def __post_init__(self):
            self.ones = [1] * int(self.value)

    d = DataClass(5.5)
    assert d.ones == [1] * 5, f"Excluded field did not have the right value"

# Generated at 2022-06-13 19:12:56.182422
# Unit test for method ALWAYS of class Exclude

# Generated at 2022-06-13 19:13:00.263683
# Unit test for function config
def test_config():
    return config(
        encoder=lambda o: o,
        decoder=lambda o: o,
        mm_field='mm_field',
        letter_case='letter_case',
        undefined='omit'
    )



# Generated at 2022-06-13 19:13:09.911554
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert(Exclude.ALWAYS("any_string") == True)



# Generated at 2022-06-13 19:13:26.155229
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(['a','a','a','a','b','c','d','a','a']) == False


# Generated at 2022-06-13 19:13:28.311007
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    data_1 = 1
    data_2 = 2

    assert Exclude.NEVER(data_1) == False
    assert Exclude.NEVER(data_2) == False


# Generated at 2022-06-13 19:13:32.970026
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("")
    assert Exclude.ALWAYS("field")
    assert Exclude.ALWAYS("field", None)
    assert Exclude.ALWAYS("field", True)


# Generated at 2022-06-13 19:13:37.316103
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert True is Exclude.ALWAYS(1)
    assert True is Exclude.ALWAYS('a')
    assert True is Exclude.ALWAYS([1, 2])
    assert True is Exclude.ALWAYS({1: 2, 3: 4})

# Generated at 2022-06-13 19:13:38.194828
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(5)

# Generated at 2022-06-13 19:13:39.199853
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert NEVER("field") == False


# Generated at 2022-06-13 19:13:40.848182
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    test = Exclude()
    assert (test.ALWAYS("a") == True)


# Generated at 2022-06-13 19:13:41.893735
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("a") == True


# Generated at 2022-06-13 19:13:45.518971
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    if not Exclude.NEVER(6):
        return "Exclude.NEVER() works correctly"
    else:
        return "Exclude.NEVER() is broken"


# Generated at 2022-06-13 19:13:46.525605
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(5)


# Generated at 2022-06-13 19:14:19.828833
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(None) is False
    assert Exclude.NEVER('a') is False
    assert Exclude.NEVER('') is False
    assert Exclude.NEVER(0) is False
    assert Exclude.NEVER(1) is False
    assert Exclude.NEVER([]) is False
    assert Exclude.NEVER(()) is False


# Generated at 2022-06-13 19:14:21.791978
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
   assert Exclude.ALWAYS(1) == True


# Generated at 2022-06-13 19:14:23.819798
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    f = Exclude.ALWAYS
    assert f("a")
    assert f(True)
    assert f(1)
    assert f([])


# Generated at 2022-06-13 19:14:24.647456
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True


# Generated at 2022-06-13 19:14:25.491938
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER('z') == False



# Generated at 2022-06-13 19:14:26.328492
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False


# Generated at 2022-06-13 19:14:27.714848
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    obj = Exclude()
    assert obj.ALWAYS(1) == True


# Generated at 2022-06-13 19:14:33.241713
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    
    @dataclass
    class Person:
        name: str

    data = {"name": "Jhon"}
    assert Person.from_dict(data) == Person("Jhon")

    @config(exclude= Exclude.NEVER)
    @dataclass
    class Person:
        name: str

    data = {"name": "Jhon"}

    assert Person.from_dict(data) == Person("Jhon")

# Generated at 2022-06-13 19:14:35.353074
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("test") == False


# Generated at 2022-06-13 19:14:45.108400
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    # Creating a test function to verify the behavior of method NEVER of class Exclude
    def test_func(obj):
        # Return the object when object contains an attribute called 'value' and value of the object is equal to 'Michele'
        if hasattr(obj, 'value') and obj.value == 'Michele':
            return obj
        
    # Create an object
    obj = type('object', (object,), {'value': 'Michele'})

    # Create new function with the behavior described above
    new_func = Exclude.NEVER
    # Create new function with a constant behavior
    new_func2 = lambda x: False

    # Assert if the functions are equal
    assert new_func == new_func2

# Generated at 2022-06-13 19:16:06.463160
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    print(Exclude.ALWAYS('test'))
    assert Exclude.ALWAYS('test') == True


# Generated at 2022-06-13 19:16:12.908116
# Unit test for function config
def test_config():
    encoding = config(encoder='test_encoder')
    assert encoding['dataclasses_json']['encoder'] == 'test_encoder'
    decoding = config(decoder='test_decoder')
    assert decoding['dataclasses_json']['decoder'] == 'test_decoder'
    decoding = config(mm_field='test_mm_field')
    assert decoding['dataclasses_json']['mm_field'] == 'test_mm_field'
    decoding = config(field_name='test_field_name')
    assert decoding['dataclasses_json']['field_name'] == 'test_field_name'
    decoding = config(letter_case='test_letter_case')
    assert decoding['dataclasses_json']['letter_case'] == 'test_letter_case'

# Generated at 2022-06-13 19:16:13.700326
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False


# Generated at 2022-06-13 19:16:14.775397
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert(Exclude.NEVER([1, 2, 3]) == False)


# Generated at 2022-06-13 19:16:16.804216
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER('abc')

# Generated at 2022-06-13 19:16:17.674970
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert callable(Exclude.NEVER)
    assert Exclude.NEVER('abc') == False


# Generated at 2022-06-13 19:16:18.841654
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(0) == False
    assert Exclude.NEVER(1) == False
    assert Exclude.NEVER(2) == False


# Generated at 2022-06-13 19:16:20.696674
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(None) is True


# Generated at 2022-06-13 19:16:22.778708
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS('anything') is True


# Generated at 2022-06-13 19:16:24.116275
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None)


# Generated at 2022-06-13 19:18:44.265733
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    print("Testing of Exclude.NEVER")
    # Always returns False, so that should be included in json
    assert Exclude.NEVER('item') == False



# Generated at 2022-06-13 19:18:45.216298
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER('string') == False

# Generated at 2022-06-13 19:18:50.771456
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False
    assert Exclude.NEVER(2) == False
    assert Exclude.NEVER(3) == False
    assert Exclude.NEVER('a') == False
    assert Exclude.NEVER('b') == False
    assert Exclude.NEVER('c') == False


# Generated at 2022-06-13 19:18:52.804413
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER('a')


# Generated at 2022-06-13 19:18:54.527931
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    print(Exclude.ALWAYS(2))


# Generated at 2022-06-13 19:18:56.513563
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False
    assert Exclude.NEVER(None) == False


# Generated at 2022-06-13 19:19:02.806181
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    from datetime import datetime
    from dataclasses import dataclass
    import json
    @dataclass
    class A:
        p1:int=1
        p2:datetime=datetime.now()
        p3:str='p3'
    a=A()
    print(json.dumps(a.__dict__))
    print(a.__dict__)



# Generated at 2022-06-13 19:19:06.009117
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    NEVER = Exclude.NEVER
    assert NEVER("a") == False
    assert NEVER("b") == False
    assert NEVER("c") == False
    assert NEVER("d") == False
    assert NEVER("e") == False
    assert NEVER("f") == False

# Generated at 2022-06-13 19:19:07.354170
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert auto_config.Exclude.ALWAYS == (lambda _: True)


# Generated at 2022-06-13 19:19:08.731822
# Unit test for function config
def test_config():
    assert config(encoder='123') == {'dataclasses_json': {'encoder': '123'}}
    assert confi