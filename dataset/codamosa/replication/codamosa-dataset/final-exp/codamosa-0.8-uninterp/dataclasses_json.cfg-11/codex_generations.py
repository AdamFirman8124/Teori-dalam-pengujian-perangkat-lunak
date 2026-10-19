

# Generated at 2022-06-13 19:09:42.092038
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("hi") == False


# Generated at 2022-06-13 19:09:42.699257
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(None)

# Generated at 2022-06-13 19:09:51.066662
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(0)
    assert Exclude.ALWAYS(False)
    assert Exclude.ALWAYS(1.0)
    assert Exclude.ALWAYS(True)
    assert Exclude.ALWAYS('')
    assert Exclude.ALWAYS('a')
    assert Exclude.ALWAYS(())
    assert Exclude.ALWAYS((1,2))
    assert Exclude.ALWAYS([])
    assert Exclude.ALWAYS([1,2])
    assert Exclude.ALWAYS({})
    assert Exclude.ALWAYS({'a':1})


# Generated at 2022-06-13 19:09:53.992870
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    def f1(_):
        return False
    def f2(_):
        return True
    assert f1 == Exclude.NEVER
    assert f1 != f2



# Generated at 2022-06-13 19:09:56.893070
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    res = Exclude.NEVER(1)
    expected = False
    assert (res == expected)



# Generated at 2022-06-13 19:09:59.998249
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    # Arrange
    condition = 1
    e = Exclude.ALWAYS

    # Act
    result = e(condition)

    # Assert
    assert result, "condition is true therefore the result should be true"


# Generated at 2022-06-13 19:10:17.454849
# Unit test for function config
def test_config():
    from hypothesis import given, infer, strategies as st
    from dataclasses import dataclass, field

    from dataclasses_json import DataClassJsonMixin
    from dataclasses_json.config import config, Exclude

    @dataclass
    class TestClass(DataClassJsonMixin):
        a: int
        b: Optional[str] = None

    @given(st.dictionaries(st.text(), st.booleans()))
    def test_exclude(exclude_bin):
        @dataclass
        class TestClassExclude(DataClassJsonMixin):
            a: int = config(exclude=lambda __, k: exclude_bin.get(k, False))
            b: float = config(exclude=lambda __, k: exclude_bin.get(k, False))

        exclude_

# Generated at 2022-06-13 19:10:19.569288
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(4) == True, "Exclude.ALWAYS(4) should return True"



# Generated at 2022-06-13 19:10:22.671485
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(0)
    assert Exclude.ALWAYS(None)
    assert Exclude.ALWAYS(object())
    assert Exclude.ALWAYS([])
    assert Exclude.ALWAYS({})


# Generated at 2022-06-13 19:10:23.841782
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1)


# Generated at 2022-06-13 19:10:33.112981
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER('')
    assert Exclude.NEVER(None)
    assert Exclude.NEVER(True)
    assert Exclude.NEVER(False)
    assert Exclude.NEVER(1)
    assert Exclude.NEVER(1.0)
    assert Exclude.NEVER([])
    assert Exclude.NEVER(())
    assert Exclude.NEVER({})



# Generated at 2022-06-13 19:10:34.777521
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(True)



# Generated at 2022-06-13 19:10:35.865627
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(None) is True

# Generated at 2022-06-13 19:10:37.634126
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS("str")


# Generated at 2022-06-13 19:10:38.984141
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False


# Generated at 2022-06-13 19:10:41.965563
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1==0) == False
    assert Exclude.NEVER(3==3) == False


# Generated at 2022-06-13 19:10:46.743841
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    def ALWAYS() -> bool:
        return True

    def NEVER() -> bool:
        return True

    d = dict()
    d['test'] = 'test'
    assert Exclude.NEVER(d) == NEVER()

    assert Exclude.NEVER(d) == NEVER()

# Generated at 2022-06-13 19:10:49.727971
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(0)
    assert Exclude.ALWAYS(False)
    assert Exclude.ALWAYS('')
    assert not Exclude.ALWAYS(True)


# Generated at 2022-06-13 19:10:52.938719
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS('') is True
    assert Exclude.ALWAYS(1) is True
    assert Exclude.ALWAYS(0) is True
    assert Exclude.ALWAYS(None) is True
    assert Exclude.ALWAYS([]) is True
    assert Exclude.ALWAYS({}) is True


# Generated at 2022-06-13 19:10:53.864629
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False


# Generated at 2022-06-13 19:11:11.555498
# Unit test for function config
def test_config():
    # doc = inspect.getdoc(config)
    # assert doc

    def my_encoder(o):
        return {"my_encoder_called": True, "value": o}

    def my_decoder(d):
        return d["value"]

    class MyMMField(MarshmallowField):
        pass

    @dataclass
    @config(exclude=Exclude.ALWAYS,
            encoder=my_encoder,
            decoder=my_decoder,
            mm_field=MyMMField,
            field_name="another_name",
            undefined=Undefined.RAISE)
    class Example:
        a: int
        b: int = 0
        c: int = dataclasses_json.config(exclude=Exclude.NEVER,
                                         field_name="C")
        d: int

# Generated at 2022-06-13 19:11:13.227689
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None)
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS([])
    assert Exclude.ALWAYS({})

# Generated at 2022-06-13 19:11:15.806916
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
  assert Exclude.NEVER(1) == False


# Generated at 2022-06-13 19:11:20.892851
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(0)
    assert Exclude.NEVER(1)
    assert Exclude.NEVER(None)
    assert Exclude.NEVER(True)
    assert Exclude.NEVER(False)
    assert Exclude.NEVER('')
    assert Exclude.NEVER('abc')
    assert Exclude.NEVER(str)



# Generated at 2022-06-13 19:11:21.999708
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("test")

# Generated at 2022-06-13 19:11:24.129630
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1)


# Generated at 2022-06-13 19:11:27.852463
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    #create an Exclude object
    exclude_to_test = Exclude()
    #call method NEVER and check the result
    assert(exclude_to_test.NEVER("test") == False)

# Generated at 2022-06-13 19:11:36.051902
# Unit test for function config
def test_config():
    from marshmallow import fields as mm_fields
    from dataclasses import dataclass

    @dataclass
    class SomeClass:
        a: int = 1
        b: int = 1

    @dataclass
    class SomeClassWithArgs:
        a: int = 1
        b: int = 1

        @config(field_name='some_class_with_args')
        def __post_init__(self, a: int, b: int):
            self.a = a
            self.b = b

    # TODO: add more tests
    #       test the actual behavior of the properties

    # Test encoder
    @config(encoder=lambda x: {"a": x.a, "c": x.b})
    class SomeClassWithEncoder(SomeClass):
        pass

    assert global_config.encod

# Generated at 2022-06-13 19:11:36.913131
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False


# Generated at 2022-06-13 19:11:39.809487
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    example_field = field(Exclude.NEVER)
    assert example_field.metadata['dataclasses_json']['exclude'](field(Exclude.NEVER),
                                                                 Exclude.NEVER) == True

# Generated at 2022-06-13 19:11:48.099484
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False


# Generated at 2022-06-13 19:11:49.320947
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    Exclude.NEVER("a")


# Generated at 2022-06-13 19:11:51.938381
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None)
    assert Exclude.ALWAYS("Toto")


# Generated at 2022-06-13 19:11:53.582685
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True


# Generated at 2022-06-13 19:11:54.855681
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("abc")



# Generated at 2022-06-13 19:11:56.389903
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(3) == False


# Generated at 2022-06-13 19:11:58.589774
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    # GIVEN
    a = Exclude()

    # WHEN
    res = a.NEVER(5)

    # THEN
    assert res == False



# Generated at 2022-06-13 19:12:00.055262
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(0) == False


# Generated at 2022-06-13 19:12:02.427820
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("") == False
    assert Exclude.NEVER("ab") == False
    assert Exclude.NEVER(1) == False
    assert Exclude.NEVER(None) == False

# Generated at 2022-06-13 19:12:08.853792
# Unit test for function config
def test_config():
    '''
    Ensure that the config function behaves as expected
    
    '''
    import dataclasses
    import marshmallow
    import dataclasses_json
    import pprint
    import json
    from dataclasses_json.config import Undefined, config

    
    
    
    
    
    @dataclasses.dataclass
    class MyClass:
        name: str
    
        class Meta:
            encoder = json.dumps
            decoder = json.loads
            mm_field = marshmallow.fields.Field()
            letter_case = lambda x: x.lower()
            undefined = Undefined.RAISE
            exclude = lambda field_name, obj: field_name == 'name'
    
    
    
    
    
    
    
    
    
    
    
    
    
    


# Generated at 2022-06-13 19:12:29.372623
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True
    assert Exclude.ALWAYS(0) == True
    assert Exclude.ALWAYS(-1) == True
    assert Exclude.ALWAYS(None) == True
    assert Exclude.ALWAYS('Lucas') == True
    assert Exclude.ALWAYS([1, 2]) == True
    assert Exclude.ALWAYS((1, 2)) == True


# Generated at 2022-06-13 19:12:40.083655
# Unit test for function config
def test_config():
    import dataclasses
    import marshmallow

    @dataclasses.dataclass
    class Test:
        foo: int

        @config(encoder=int, decoder=float)
        def bar(self):
            return self.foo

        @config(mm_field=marshmallow.fields.Float())
        def baz(self):
            return self.foo

        @config(field_name='qux')
        @config(letter_case=str.upper)
        def quux(self):
            return self.foo

        @config(undefined=Undefined.RAISE)
        def quuux(self):
            return self.foo

        @config(exclude=Exclude.NEVER)
        def quuuux(self):
            return self.foo

    fields = dataclasses.fields(Test)



# Generated at 2022-06-13 19:12:42.135639
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS(): 
    assert Exclude.ALWAYS(10) == True
    

# Generated at 2022-06-13 19:12:43.407736
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1)



# Generated at 2022-06-13 19:12:45.481609
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None) == True



# Generated at 2022-06-13 19:12:55.084153
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False

test_Exclude_NEVER()


# Generated at 2022-06-13 19:12:58.995067
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER('a') is False
    assert Exclude.NEVER(1) is False
    assert Exclude.NEVER(None) is False
    assert Exclude.NEVER(False) is False


# Generated at 2022-06-13 19:13:00.450126
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False

# Generated at 2022-06-13 19:13:12.598328
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    test_value1 = 123
    test_value2 = 456
    assert Exclude.NEVER(test_value1) is True
    assert Exclude.NEVER(test_value2) is True


# Generated at 2022-06-13 19:13:14.681821
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False
    assert Exclude.NEVER('a') == False


# Generated at 2022-06-13 19:13:46.357381
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(None)

# Generated at 2022-06-13 19:13:47.363961
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert(Exclude.ALWAYS(1) == True)


# Generated at 2022-06-13 19:13:48.362717
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert callable(Exclude.ALWAYS)


# Generated at 2022-06-13 19:13:49.357325
# Unit test for method ALWAYS of class Exclude

# Generated at 2022-06-13 19:13:58.764700
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(42) == False


# Generated at 2022-06-13 19:14:07.952862
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    from dataclasses import dataclass

    @dataclass
    class A:
        a: int

    @dataclass
    class B:
        a: int


# Generated at 2022-06-13 19:14:09.836747
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("field") == False
    assert Exclude.NEVER("value") == False
    assert Exclude.NEVER("extra") == False

# Generated at 2022-06-13 19:14:11.030721
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS('str')

# Generated at 2022-06-13 19:14:12.340759
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False

# Generated at 2022-06-13 19:14:17.202850
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True
    assert Exclude.ALWAYS("1") == True
    assert Exclude.ALWAYS(False) == True
    assert Exclude.ALWAYS(True) == True

# Generated at 2022-06-13 19:15:54.351858
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(5) == True
    assert Exclude.ALWAYS("67") == True
    assert Exclude.ALWAYS(7.1) == True
    assert Exclude.ALWAYS(b"a") == True
    assert Exclude.ALWAYS(None) == True


# Generated at 2022-06-13 19:15:55.849821
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    res = Exclude.NEVER(5)
    assert res is False

# Generated at 2022-06-13 19:15:57.576403
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    a = Exclude()
    assert a.ALWAYS("anything") == True


# Generated at 2022-06-13 19:16:03.370074
# Unit test for function config
def test_config():

    # Check that everything can be set either with metadata or by direct invocation
    import marshmallow as mm
    class Class:
        pass
    typed_class = TypeVar('typed_class',bound=Class)
    import json
    # TODO: currently, dataclasses_json.config can only add information to an existing metadata
    # Why?
    def encoder(obj, recurse):
        return True
    def decoder(obj, schema):
        return True
    def mmfield():
        return True
    def lettercase(str):
        return True

    json.loads = lambda str: True
    json.dumps = lambda obj: True

    # TODO: Warnings
    # global_config.json_module = json
    # assert global_config.json_module is json
    # global_config.json_module = json

   

# Generated at 2022-06-13 19:16:05.201950
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("test") == False


# Generated at 2022-06-13 19:16:07.437010
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) is False
    assert Exclude.NEVER(2) is False
    assert Exclude.NEVER(3) is False
    assert Exclude.NEVER(5) is False

# Generated at 2022-06-13 19:16:16.961088
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("value") == True


# Generated at 2022-06-13 19:16:21.441103
# Unit test for function config
def test_config():
    metadata = {'dataclasses_json': {'exclude': 'hello'}}
    config(metadata=metadata, exclude='world')
    assert {'dataclasses_json': {'exclude': 'world'}} == metadata

# Generated at 2022-06-13 19:16:23.950609
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(0) is False
    assert Exclude.NEVER(1) is False
    assert Exclude.NEVER('a') is False

# Generated at 2022-06-13 19:16:42.687087
# Unit test for function config
def test_config():
    import unittest.mock as mock
    from marshmallow.fields import Str

    class MockField(Str):
        pass

    class MockCallable:
        pass

    mock_encoder = mock.Mock()
    mock_encoder.__func__.return_value = 'encoder'
    mock_decoder = mock.Mock()
    mock_decoder.__func__.return_value = 'decoder'
    mock_field = mock.Mock()
    mock_field.__class__.__name__ = 'mock_field'
    mock_callable = mock.Mock()
    mock_callable.__func__.return_value = 'callable'