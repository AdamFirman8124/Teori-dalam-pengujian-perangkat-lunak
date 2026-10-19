

# Generated at 2022-06-13 19:09:44.101930
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS('test')

# Generated at 2022-06-13 19:09:46.734343
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    test_value = False
    result = Exclude.NEVER(test_value)
    assert result == False


# Generated at 2022-06-13 19:09:51.658637
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) is True
    assert Exclude.ALWAYS('a') is True
    assert Exclude.ALWAYS('') is True
    assert Exclude.ALWAYS(0) is True
    assert Exclude.ALWAYS(None) is True

# Generated at 2022-06-13 19:09:53.221268
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None) is True


# Generated at 2022-06-13 19:09:55.245544
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    result = Exclude.NEVER("string")
    assert result == False


# Generated at 2022-06-13 19:09:59.596001
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(0)
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS(100)
    assert Exclude.ALWAYS('a')
    assert Exclude.ALWAYS('abc')
    assert Exclude.ALWAYS('')


# Generated at 2022-06-13 19:10:00.973200
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    value = Exclude.ALWAYS("some_value")
    assert value == True


# Generated at 2022-06-13 19:10:02.817950
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False


# Generated at 2022-06-13 19:10:10.300923
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(False) == False
    assert Exclude.NEVER(True) == False
    assert Exclude.NEVER(1) == False
    assert Exclude.NEVER(0) == False
    assert Exclude.NEVER("") == False
    assert Exclude.NEVER("abc") == False
    assert Exclude.NEVER(None) == False


# Generated at 2022-06-13 19:10:13.549405
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None) is True
    assert Exclude.ALWAYS(1) is True
    assert Exclude.ALWAYS(object()) is True



# Generated at 2022-06-13 19:10:18.459463
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS("s")
    assert Exclude.ALWAYS(1.0)


# Generated at 2022-06-13 19:10:19.846853
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    a = Exclude.ALWAYS(1)
    assert a == True


# Generated at 2022-06-13 19:10:27.827518
# Unit test for function config
def test_config():
    # type: () -> None
    try:
        # type: ignore
        @dataclass
        class Obj:
            i: int = field(metadata=config(undefined="strict"))
    except UndefinedParameterError:
        pass
    else:
        assert False, "Should raise error when undefined parameters are not valid"

    # type: ignore
    @dataclass
    class Obj2:
        i: int = field(metadata=config(undefined=Undefined.EXCLUDE))

    # type: ignore
    @dataclass
    class Obj3:
        i: int = field(metadata=config(undefined="exclude"))

    # type: ignore

# Generated at 2022-06-13 19:10:28.792994
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert not Exclude.NEVER(None)


# Generated at 2022-06-13 19:10:32.069806
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False
    assert Exclude.NEVER(2) == False
    assert Exclude.NEVER(9) == False


# Generated at 2022-06-13 19:10:32.925084
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    a = {}
    assert Exclude.NEVER(a)
    assert not a


# Generated at 2022-06-13 19:10:35.080365
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    class ClassTest:
        def methodTest(self):
            return False

    # We test that it returns always True
    assert Exclude.ALWAYS(ClassTest) == True
    assert Exclude.ALWAYS(ClassTest()) == True
    assert Exclude.ALWAYS(ClassTest().methodTest) == True
    assert Exclude.ALWAYS(ClassTest().methodTest()) == True


# Generated at 2022-06-13 19:10:40.417297
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False
    assert Exclude.NEVER(0) == False
    assert Exclude.NEVER(-1) == False
    assert Exclude.NEVER(1.0) == False
    assert Exclude.NEVER(-1.0) == False
    assert Exclude.NEVER(0.0) == False


# Generated at 2022-06-13 19:10:51.807591
# Unit test for function config
def test_config():
    from dataclasses import dataclass, fields
    from marshmallow.fields import Int as MarshmallowInt

    @dataclass
    class TestStruct:
        a: int
        b: int = 3

        class Config:
            encoder = str
            decoder = int
            mm_field = int
            letter_case = str.upper
            exclude = Exclude.NEVER

    test_obj = TestStruct(10)
    assert 9 == len(fields(test_obj))

    for field in fields(test_obj):
        field_metadata = field.metadata.get('dataclasses_json')
        if field.metadata.get('dataclasses_json') is not None:
            assert global_config.encoders[field.type] == field_metadata['encoder']

# Generated at 2022-06-13 19:10:52.756308
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("string") == False


# Generated at 2022-06-13 19:11:00.965505
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    test_value = Exclude.NEVER
    assert test_value(0) == False
    assert test_value(1) == False
    assert test_value(2) == False
    assert test_value(3) == False
    assert test_value(4) == False


# Generated at 2022-06-13 19:11:11.611802
# Unit test for function config
def test_config():
    from dataclasses import dataclass, field

    @dataclass
    class Foo:
        foo: str = ''
        bar: str = field(metadata=config(field_name='BAR'))

    assert Foo().to_dict() == {'foo': '', 'BAR': ''}

    # Both fields have the same name
    @dataclass
    class Foo:
        foo: str = field(metadata=config(field_name='FOO'))
        bar: str = field(metadata=config(field_name='FOO'))

    assert Foo().to_dict() == {'bar': '', 'FOO': ''}

# Generated at 2022-06-13 19:11:13.285604
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    # Arrange
    value = 5

    # Act
    result = Exclude.NEVER(value)

    # Assert
    assert result is False


# Generated at 2022-06-13 19:11:20.232923
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    @dataclass
    class ExcludeTest:
        a: int
        b: int

        @config(exclude=Exclude.ALWAYS)
        def c(self):
            return self.a + self.b

    excl = ExcludeTest(a=1, b=1)
    d = dataclasses_json.dump(excl)
    assert d == '{"a": 1, "b": 1}'

# Generated at 2022-06-13 19:11:23.497032
# Unit test for function config
def test_config():
    import inspect
    config()
    config(exclude=lambda field_name, field: True)
    assert len(inspect.signature(config).parameters) == 18
    assert len(inspect.signature(config).parameters) == len(inspect.signature(config).parameters)

# Generated at 2022-06-13 19:11:25.096347
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER



# Generated at 2022-06-13 19:11:26.460126
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(10) is True

# Generated at 2022-06-13 19:11:27.479086
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    print(Exclude.ALWAYS)


# Generated at 2022-06-13 19:11:29.325248
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    print(Exclude.NEVER.__name__)
    assert Exclude.NEVER.__name__ == '<lambda>'


# Generated at 2022-06-13 19:11:30.623781
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    # c = Exclude.ALWAYS
    assert Exclude.ALWAYS(1) is True


# Generated at 2022-06-13 19:11:35.832802
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS(Exclude.ALWAYS)
    assert Exclude.ALWAYS(Exclude.NEVER)
    assert Exclude.ALWAYS(Exclude)


# Generated at 2022-06-13 19:11:37.817513
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True



# Generated at 2022-06-13 19:11:40.516376
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True
    assert Exclude.ALWAYS('s') == True
    assert Exclude.ALWAYS(Exclude) == True

# Generated at 2022-06-13 19:11:42.413357
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(3) == False


# Generated at 2022-06-13 19:11:43.703569
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(True)
    assert Exclude.ALWAYS(False)


# Generated at 2022-06-13 19:11:45.021909
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    data = "test"
    assert Exclude.NEVER(data) == False

# Generated at 2022-06-13 19:11:46.191302
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    result = Exclude.ALWAYS(True)
    assert result is True


# Generated at 2022-06-13 19:11:48.806025
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS('') == True
    assert Exclude.ALWAYS(1) == True
    assert Exclude.ALWAYS([]) == True



# Generated at 2022-06-13 19:11:52.695533
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False
    assert Exclude.NEVER('Hello, World!') == False
    assert Exclude.NEVER(True) == False
    assert Exclude.NEVER(False) == False

# Generated at 2022-06-13 19:11:57.625889
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
  # create an instance of class Exclude
  exc = Exclude()

  print("\nExample of method NEVER of class Exclude:")
  print(exc.NEVER(True))
  print(exc.NEVER(False))

if __name__ == "__main__":
  # execute only if run as a script
  test_Exclude_NEVER()
  print("\nTest was performed successfully.")

# Generated at 2022-06-13 19:12:04.984732
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None) == True


# Generated at 2022-06-13 19:12:06.214612
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) is True
    assert Exclude.ALWAYS('x') is True



# Generated at 2022-06-13 19:12:06.990274
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER('a') == False


# Generated at 2022-06-13 19:12:19.070847
# Unit test for function config
def test_config():
    import marshmallow
    class Foo:
        pass

    @dataclass
    class Bar:
        foo: Foo
        bar: str

    class MyField(marshmallow.fields.Field):
        pass

    MyFieldType = type(MyField)

    def encode(foo: Foo):
        return f'<{foo}>'

    def decode(s: str):
        return Foo()

    @functools.cached_property
    def to_upper(cls):
        return str.upper


# Generated at 2022-06-13 19:12:21.299759
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(2) == True
    assert Exclude.ALWAYS(None) == True
    assert Exclude.ALWAYS(-1) == True


# Generated at 2022-06-13 19:12:22.889041
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS('test')


# Generated at 2022-06-13 19:12:26.178188
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS('')
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS(False)
    assert Exclude.ALWAYS([])


# Generated at 2022-06-13 19:12:28.124730
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(None) == False



# Generated at 2022-06-13 19:12:35.170543
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    from marshmallow import Schema, fields
    from marshmallow.exceptions import ValidationError
    from typing import Any

    @config(metadata={"dataclasses_json": {"exclude": Exclude.NEVER}})
    @dataclass
    class Test:
        name: str = "haha"

    class TestSchema(Schema):
        name = fields.Str()

    test = Test()

    print(test)
    serialized_result = TestSchema().dumps(test)
    print(serialized_result)

    deserialized_result = TestSchema().loads(serialized_result)
    print(deserialized_result)


# Generated at 2022-06-13 19:12:37.851839
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    # Given
    obj = object()

    # When
    result = Exclude.NEVER(obj)

    # Then
    assert result == False

# Generated at 2022-06-13 19:12:53.145615
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    for x in [1, 0, '', 'a', True, False, {}, {'key': 'value'}]:
        assert Exclude.ALWAYS(x) == True


# Generated at 2022-06-13 19:12:56.825613
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    '''
    Checking if Exclude.NEVER() is returning False.
    '''
    assert Exclude.NEVER(0) == False

# Generated at 2022-06-13 19:12:57.953411
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None)
    assert Exclude.ALWAYS(False)



# Generated at 2022-06-13 19:12:59.429265
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(7)
    assert Exclude.ALWAYS("hello world")
    assert Exclude.ALWAYS(Exclude.ALWAYS)



# Generated at 2022-06-13 19:12:59.998486
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(True)


# Generated at 2022-06-13 19:13:02.134777
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
  from dataclasses import dataclass
  from dataclasses_json import dataclass_json
  @dataclass_json
  @dataclass
  class User:
    id: str
    name: str
    age: int = config(exclude=Exclude.NEVER)




# Generated at 2022-06-13 19:13:02.814088
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    result=Exclude.ALWAYS(1)
    assert result == True

# Generated at 2022-06-13 19:13:03.495309
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert(Exclude.ALWAYS(10) == True)


# Generated at 2022-06-13 19:13:04.622900
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER('a') == False

# Generated at 2022-06-13 19:13:05.708305
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    Exclude.NEVER(None)

# Generated at 2022-06-13 19:14:02.058291
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None) == True


# Generated at 2022-06-13 19:14:04.501926
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("test")


# Generated at 2022-06-13 19:14:05.921527
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(None) == False


# Generated at 2022-06-13 19:14:16.548602
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    print(Exclude.NEVER(1))
    print(Exclude.NEVER(""))
    print(Exclude.NEVER({}))


# Generated at 2022-06-13 19:14:18.273326
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(True) == True


# Generated at 2022-06-13 19:14:19.428884
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS('abc') is True


# Generated at 2022-06-13 19:14:21.046099
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    ret = Exclude.NEVER(True)
    assert ret == False



# Generated at 2022-06-13 19:14:23.049920
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    print(Exclude.ALWAYS)
    print(Exclude.NEVER)
    return True
# Run tests
test_Exclude_ALWAYS()

# Generated at 2022-06-13 19:14:24.228431
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(3) is True


# Generated at 2022-06-13 19:14:32.364093
# Unit test for function config
def test_config():
    assert config(
        field_name='lower_case',
        letter_case=str.lower
    ) == {
        'dataclasses_json': {
            'letter_case': str.lower
        }
    }

    assert config(
        field_name='lower_case',
        letter_case=str.lower,
        undefined='exception'
    ) == {
        'dataclasses_json': {
            'letter_case': str.lower,
            'undefined': Undefined.EXCEPTION
        }
    }

    with pytest.raises(UndefinedParameterError):
        assert config(undefined='invalid')


# Generated at 2022-06-13 19:16:03.615440
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False


# Generated at 2022-06-13 19:16:04.972096
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("test") == True

# Generated at 2022-06-13 19:16:07.086847
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS({})
    assert Exclude.ALWAYS({"asdf": 0})
    assert Exclude.ALWAYS({"asdf": 1})


# Generated at 2022-06-13 19:16:07.979595
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
  assert Exclude.NEVER(True)==False


# Generated at 2022-06-13 19:16:09.098888
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS('a')


# Generated at 2022-06-13 19:16:11.575984
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    # Setup
    expected = True

    # Exercise
    actual = Exclude.ALWAYS(True)

    # Verify
    assert actual == expected, f"actual = {actual}, expected = {expected}"


if __name__ == '__main__':
    test_Exclude_ALWAYS()

# Generated at 2022-06-13 19:16:12.540502
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(True) == False
    

# Generated at 2022-06-13 19:16:17.471095
# Unit test for function config
def test_config():
    def converter(val):
        return val if val else "foo"

    class MyClass:
        class_var = 0

    @dataclass
    class MyDataClass:
        my_class: MyClass
        my_str: str
        my_int: int = field(default=1)

        @config(exclude=Exclude.ALWAYS)
        def hidden_var(self):
            return 'hidden'

        @config(field_name='new_name')
        def renamed_var(self):
            return 'renamed'

        @config(encoder=converter)
        def encoded_var(self):
            return None

    def test_encoder(val):
        return val

    MyDataClass = config(
        decoder=test_encoder
    )(MyDataClass)

    # verify that the

# Generated at 2022-06-13 19:16:19.584171
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1)


# Generated at 2022-06-13 19:16:20.850557
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert NEVER(1) == False


# Generated at 2022-06-13 19:19:19.681886
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS(0)
    assert Exclude.ALWAYS('a')
    assert Exclude.ALWAYS('')
    assert Exclude.ALWAYS(None)


# Generated at 2022-06-13 19:19:20.911912
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS('geek')
    

# Generated at 2022-06-13 19:19:23.790778
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS(None)
    assert Exclude.ALWAYS('abc')


# Generated at 2022-06-13 19:19:25.194822
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(2) == True
    assert Exclude.ALWAYS("string") == True


# Generated at 2022-06-13 19:19:26.260061
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(0)



# Generated at 2022-06-13 19:19:34.308827
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(2) == False
    assert Exclude.NEVER(3) == False
    assert Exclude.NEVER(4) == False
    assert Exclude.NEVER('hi') == False
    assert Exclude.NEVER(['1','2','3']) == False
    assert Exclude.NEVER(['a','b','c']) == False
    assert Exclude.NEVER(('a','b','c')) == False
    assert Exclude.NEVER((1,2,3)) == False
    assert Exclude.NEVER({'a': 1, 'b': 2, 'c': 3}) == False
    assert Exclude.NEVER({1:'a', 2:'b', 3:'c'}) == False

test_Exclude_NEVER()


# Generated at 2022-06-13 19:19:35.882743
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    try:
        if (Exclude.ALWAYS(None) != True):
            return False
    except:
        return False
    return True



# Generated at 2022-06-13 19:19:38.409562
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert _GlobalConfig.__init__()
    obj = Exclude.NEVER
    assert obj(2) == False


# Generated at 2022-06-13 19:19:40.008124
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(5)
    assert Exclude.ALWAYS("Ola")


# Generated at 2022-06-13 19:19:41.816770
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("Hello") is True
