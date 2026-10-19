

# Generated at 2022-06-13 19:09:43.784626
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS(None)
    assert Exclude.ALWAYS("a")


# Generated at 2022-06-13 19:09:48.924951
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    if Exclude.NEVER(False):
        print("Error here! NEVER should never return True")
    if Exclude.NEVER(0):
        print("Error here! NEVER should never return True")
    if Exclude.NEVER(''):
        print("Error here! NEVER should never return True")


# Generated at 2022-06-13 19:09:55.838791
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    # GIVEN: Pre-defined constant Exclude.NEVER
    # WHEN: Check the return value of Exclude.NEVER() with valid input
    # THEN: The False should be returned
    while True:
        name = input("Input your name or 'q' to quit: ")
        if name.lower() == 'q':
            break
        ret = Exclude.NEVER(name)
        print(ret)


# Generated at 2022-06-13 19:09:59.884256
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    import unittest
    class ExcludeTest( unittest.TestCase ):
        def test_Exclude_NEVER( self ):
            global Exclude
            self.assertTrue(Exclude.NEVER('SomeValue'))
    unittest.main()

# Generated at 2022-06-13 19:10:08.739745
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False

# Generated at 2022-06-13 19:10:10.450444
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("Should return False") == False

# Generated at 2022-06-13 19:10:16.533710
# Unit test for function config
def test_config():
    from marshmallow import fields
    @config(encoder=str, decoder=float, mm_field=fields.Integer)
    @dataclass
    class Point:
        x: int
        y: int

    assert Point(1, 2).to_json() == '{"x": "1", "y": "2"}'
    assert Point.from_json('{"x": 1.1, "y": 2.2}') == Point(1, 2)
    assert Point.Schema().fields['x'] is fields.Integer()

# Generated at 2022-06-13 19:10:17.707532
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(0) == False

# Generated at 2022-06-13 19:10:19.146641
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None)


# Generated at 2022-06-13 19:10:22.962804
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    def func(x: str) -> bool:
        return x == "0"

    assert Exclude.NEVER("1") is False
    assert Exclude.NEVER("") is False
    assert Exclude.NEVER(" ") is False
    assert Exclude.NEVER(func) is False



# Generated at 2022-06-13 19:10:25.938909
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS('instance') == True


# Generated at 2022-06-13 19:10:26.924053
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(123) == True

# Generated at 2022-06-13 19:10:28.789958
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("test") == True


# Generated at 2022-06-13 19:10:30.225814
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True


# Generated at 2022-06-13 19:10:35.001749
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(True)
    assert Exclude.ALWAYS('True')
    assert Exclude.ALWAYS(1.)
    assert Exclude.ALWAYS(False)
    assert Exclude.ALWAYS('False')
    assert Exclude.ALWAYS(0.)


# Generated at 2022-06-13 19:10:36.011631
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("Hello") == False

# Generated at 2022-06-13 19:10:37.759019
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False
    assert Exclude.NEVER("a") == False


# Generated at 2022-06-13 19:10:39.121191
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    x = Exclude.ALWAYS(1)
    assert x == True


# Generated at 2022-06-13 19:10:44.102351
# Unit test for function config
def test_config():
    class Foo:
        pass

    assert not hasattr(Foo, 'config')
    config(Foo)
    assert hasattr(Foo, 'config')
    assert callable(Foo.__dataclass_metadata__['dataclasses_json']['config'])



# Generated at 2022-06-13 19:10:45.677535
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS('test') is True


# Generated at 2022-06-13 19:10:48.632581
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    r = Exclude.NEVER(3)
    assert r == False


# Generated at 2022-06-13 19:10:50.363387
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None)
    assert Exclude.ALWAYS(Exclude())


# Generated at 2022-06-13 19:10:53.439489
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(True) == False
    assert Exclude.NEVER(False) == False
    assert Exclude.NEVER(5) == False
    assert Exclude.NEVER(None) == False


# Generated at 2022-06-13 19:10:54.495141
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(0) == Exclude.NEVER(1) == False

# Generated at 2022-06-13 19:10:56.941928
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(2) == False


# Generated at 2022-06-13 19:10:59.892539
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    e = Exclude()
    assert e.NEVER("anything") is False


# Generated at 2022-06-13 19:11:02.779864
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(object) == True
    assert Exclude.ALWAYS(str) == True

# Generated at 2022-06-13 19:11:05.031622
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("V") == True


# Generated at 2022-06-13 19:11:07.953850
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS("hello")


# Generated at 2022-06-13 19:11:15.640946
# Unit test for function config
def test_config():
    @dataclass
    class Panda():
        name: str

    @dataclass
    class Panda2():
        name: str

    @dataclass
    class Panda3():
        name: str

    @dataclass
    class Panda4():
        name: str

    @dataclass
    class Panda5():
        name: str

    @dataclass
    class Panda6():
        name: str

    @config_dict(pandas=config(mm_field=String(), encoder=lambda x: x, decoder=lambda x: x))
    class Parent():
        pandas: List[Panda]
        panda_: Optional[Panda]
        panda2: Panda2
        panda3: Panda3
        panda4: Panda4
        panda5: Panda5

# Generated at 2022-06-13 19:11:18.371313
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    class TestClass:
        TEST_CONSTANT=1

    assert Exclude.NEVER(TestClass.TEST_CONSTANT) == False
    

# Generated at 2022-06-13 19:11:19.452811
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(0) == False

# Generated at 2022-06-13 19:11:21.438310
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True


# Generated at 2022-06-13 19:11:22.470553
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False


# Generated at 2022-06-13 19:11:24.054211
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(5) == False

# Generated at 2022-06-13 19:11:33.626206
# Unit test for function config
def test_config():
    assert config() == {'dataclasses_json': {}}
    assert config(encoder=1.1) == {'dataclasses_json': {'encoder': 1.1}}
    assert config(decoder=1.1) == {'dataclasses_json': {'decoder': 1.1}}
    assert config(mm_field=1.1) == {'dataclasses_json': {'mm_field': 1.1}}
    assert config(field_name='x') == {
        'dataclasses_json': {'letter_case': lambda x: 'x'}}
    assert config(letter_case=lambda x: x.lower()) == {
        'dataclasses_json': {'letter_case': lambda x: x.lower()}}

# Generated at 2022-06-13 19:11:39.247602
# Unit test for function config
def test_config():
    from marshmallow.fields import Str

    @dataclass
    @config(
        encoder=lambda x: "test encoding",
        decoder=lambda x: "test decoding",
        mm_field=Str(),
        letter_case=lambda x: "test_letter_case",
        undefined=Undefined.EXCLUDE,
        field_name="test_field_name",
        exclude=Exclude.NEVER
    )
    class TestConfig:
        foo: str
        bar: int
        baz: float

    assert TestConfig.schema().get_field_names() == {'foo', 'bar', 'baz'}

# Generated at 2022-06-13 19:11:40.637946
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None)


# Generated at 2022-06-13 19:11:45.499787
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True
    assert Exclude.ALWAYS("test") == True
    assert Exclude.ALWAYS(1.2) == True
    assert Exclude.ALWAYS({"key" : "value"}) == True
    assert Exclude.ALWAYS([1,2,3]) == True


# Generated at 2022-06-13 19:11:46.261003
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False

test_Exclude_NEVER()

# Generated at 2022-06-13 19:11:59.476232
# Unit test for function config
def test_config():
    from dataclasses import dataclass

    from dataclasses_json import config as dataclass_config
    from marshmallow import Schema

    @dataclass
    class Schema1(Schema):
        pass

    @dataclass
    class Schema2(Schema):
        pass

    @dataclass
    class DataClass1:
        field1: str = dataclass_config(None, field_name='name')

        def __post_init__(self):
            self.field1 = 'default'

    @dataclass
    class DataClass2:
        field2: str = dataclass_config(None, field_name='name')

        def __post_init__(self):
            self.field1 = 'default'

    assert DataClass1().field1 == 'default'
    assert DataClass

# Generated at 2022-06-13 19:12:00.677859
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("hello") == True


# Generated at 2022-06-13 19:12:01.552022
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1)


# Generated at 2022-06-13 19:12:03.064972
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    cfg = config(exclude=Exclude.NEVER)

# Generated at 2022-06-13 19:12:06.580773
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    try:
        assert Exclude.NEVER(None) == False
    except TypeError:
        print("Type Error Occured!")
    else:
        print("No Type Error!")


# Generated at 2022-06-13 19:12:09.891758
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(0) == True
    assert Exclude.ALWAYS(1) == True
    assert Exclude.ALWAYS("a") == True
    assert Exclude.ALWAYS("b") == True


# Generated at 2022-06-13 19:12:14.059275
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(0)
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS(2)
    assert Exclude.ALWAYS(-1)
    assert Exclude.ALWAYS(-2)


# Generated at 2022-06-13 19:12:17.272023
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER('a') is False
    assert Exclude.NEVER('') is False
    assert Exclude.NEVER([]) is False


# Generated at 2022-06-13 19:12:17.942698
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None) == True


# Generated at 2022-06-13 19:12:20.424823
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1)==False
    assert Exclude.NEVER("a")==False
    assert Exclude.NEVER((1,2))==False


# Generated at 2022-06-13 19:12:27.678008
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(None) == False


# Generated at 2022-06-13 19:12:29.071034
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    a = Exclude.NEVER(4)
    assert a == False


# Generated at 2022-06-13 19:12:30.580056
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(5) == True


# Generated at 2022-06-13 19:12:35.437696
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    test = Exclude

# Generated at 2022-06-13 19:12:39.975534
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(5)
    assert Exclude.ALWAYS([1, 2, 3, 4])
    assert Exclude.ALWAYS((1, 2, 3, 4))
    assert Exclude.ALWAYS('abc')
    assert Exclude.ALWAYS(None)


# Generated at 2022-06-13 19:12:42.003638
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(5) == False


# Generated at 2022-06-13 19:12:44.039605
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    result = Exclude.ALWAYS(1)
    expected = True
    assert result == expected

test_Exclude_ALWAYS()


# Generated at 2022-06-13 19:12:46.077434
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1)


# Generated at 2022-06-13 19:12:58.164025
# Unit test for function config
def test_config():
    @dataclasses.dataclass
    class Entity:
        id: int = dataclasses.field(metadata=config(
            exclude=lambda f,v: False))

    entity = Entity()
    json_value = entity.to_json()
    assert 'id' in json_value



# Generated at 2022-06-13 19:12:59.907572
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS('x') == True


# Generated at 2022-06-13 19:13:18.243257
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(0)
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS(1.5)
    assert Exclude.ALWAYS('ab')



# Generated at 2022-06-13 19:13:20.103911
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("anything") is False


# Generated at 2022-06-13 19:13:23.564419
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    inp:bool=True
    out:bool=Exclude.ALWAYS(inp)
    assert out==True


# Generated at 2022-06-13 19:13:25.301399
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("any") == True



# Generated at 2022-06-13 19:13:35.068035
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    @dataclass_json
    @dataclass
    class C:
        n: int

    assert C.schema() == {'type': 'object', 'properties': {'n': {'type': 'number'}}}

    @dataclass_json
    @dataclass
    class C:
        n: int = config(exclude=Exclude.NEVER)

    assert C.schema() == {'type': 'object', 'properties': {'n': {'type': 'number'}}}

    @dataclass_json
    @dataclass
    class C:
        n: int = config(exclude=Exclude.NEVER)

    assert C.schema() == {'type': 'object', 'properties': {'n': {'type': 'number'}}}


# Generated at 2022-06-13 19:13:35.645500
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(5)

# Generated at 2022-06-13 19:13:39.372873
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None)
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS(1.0)
    assert Exclude.ALWAYS(True)
    assert Exclude.ALWAYS('')
    assert Exclude.ALWAYS([])
    assert Exclude.ALWAYS({})


# Generated at 2022-06-13 19:13:41.580186
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    l1 = Exclude.NEVER(False)
    assert l1 == False
    l2 = Exclude.NEVER(True)
    assert l2 == False


# Generated at 2022-06-13 19:13:47.018110
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert callable(Exclude.NEVER)
    assert Exclude.NEVER(0) == False
    assert Exclude.NEVER(1) == False
    assert Exclude.NEVER(True) == False


# Generated at 2022-06-13 19:13:48.271952
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    print(Exclude.NEVER(1))
    return Exclude.NEVER(1)


# Generated at 2022-06-13 19:14:37.071472
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    # Tests with different types of parameters
    class A:
        pass
    assert Exclude.ALWAYS(5)
    assert Exclude.ALWAYS("test")
    assert Exclude.ALWAYS([1, 2, 3, 4, 5])
    assert Exclude.ALWAYS(A)


# Generated at 2022-06-13 19:14:39.275807
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(0) == False
    assert Exclude.NEVER(1) == False


# Generated at 2022-06-13 19:14:40.528419
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1)


# Generated at 2022-06-13 19:14:42.405897
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS('anything')

# Generated at 2022-06-13 19:14:43.702002
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert(Exclude.NEVER(None))



# Generated at 2022-06-13 19:14:48.224552
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    nb_true = 0
    nb_false = 0

    for i in range(0,10):
        if Exclude.ALWAYS(i):
            nb_true+=1
        else:
            nb_false+=1
    assert nb_true == 10
    assert nb_false == 0


# Generated at 2022-06-13 19:14:53.250593
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    from dataclasses import dataclass

    @dataclass(frozen=True)
    class Example:
        a: int = 1
        b: int = 2

    example = Example()

    import marshmallow as mm
    class ExampleSchema(mm.Schema):
        a = mm.fields.Int()
        b = mm.fields.Int()

    es = ExampleSchema()
    es.dump(example)
    


# Generated at 2022-06-13 19:14:54.318627
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(0) == True



# Generated at 2022-06-13 19:14:55.377438
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS('test') == True


# Generated at 2022-06-13 19:14:56.442786
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS('field')


# Generated at 2022-06-13 19:16:26.029372
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    a = Exclude.NEVER(1)
    assert a == False

# Generated at 2022-06-13 19:16:28.600035
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    from dataclasses import dataclass
    @dataclass
    class Dummy:
        foo: str
    dummy = Dummy(foo="bar")
    assert Exclude.NEVER(dummy) == True


# Generated at 2022-06-13 19:16:29.722031
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(None)


# Generated at 2022-06-13 19:16:31.452061
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) is False
    assert Exclude.NEVER(None) is False



# Generated at 2022-06-13 19:16:34.161934
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    def test_func(x):
        return False

    assert Exclude.NEVER == test_func

# Generated at 2022-06-13 19:16:36.527003
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
        assert Exclude.NEVER(2) == True


# Generated at 2022-06-13 19:16:37.988986
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("test") == True


# Generated at 2022-06-13 19:16:46.292881
# Unit test for function config
def test_config():

    # use default value
    default_metadata: dict = {}
    default_metadata = config(default_metadata)
    assert default_metadata == {'dataclasses_json':{}}

    # use custom value
    encoder = "encoder"
    decoder = "decoder"
    mm_field = "mm_field"
    letter_case = "letter_case"
    undefined = "undefined"
    field_name = "field_name"
    exclude = "exclude"
    modified_metadata: dict = {}
    modified_metadata = config(
        modified_metadata, 
        encoder = encoder,
        decoder = decoder,
        mm_field = mm_field,
        letter_case = letter_case,
        undefined = undefined,
        field_name = field_name,
        exclude = exclude)


# Generated at 2022-06-13 19:16:49.622726
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    name = 'test'
    # This should return false, because right now exclude is set to never
    print(Exclude.NEVER(name))

# Generated at 2022-06-13 19:16:51.450413
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(3)
