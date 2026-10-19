

# Generated at 2022-06-13 19:09:40.419546
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(None)

# Generated at 2022-06-13 19:09:41.494592
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True
    assert Exclude.ALWAYS(0) == True
    assert Exclude.ALWAYS(-1) == True


# Generated at 2022-06-13 19:09:43.901488
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(0) == True
    assert Exclude.ALWAYS(1) == True
    assert Exclude.ALWAYS(5) == True
    assert Exclude.ALWAYS('string') == True
    assert Exclude.ALWAYS(None) == True
    assert Exclude.ALWAYS(object()) == True


# Generated at 2022-06-13 19:09:46.039563
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    class Example():
        pass
    a = Exclude.NEVER(Example)
    assert a == False


# Generated at 2022-06-13 19:09:48.758208
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert(not Exclude.NEVER(1))
    assert(not Exclude.NEVER('1'))


# Generated at 2022-06-13 19:09:50.818058
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    exclude = Exclude.NEVER
    assert exclude("A") == False


# Generated at 2022-06-13 19:09:53.277106
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(3)
    assert Exclude.ALWAYS(None)
    assert Exclude.ALWAYS("TEST")


# Generated at 2022-06-13 19:09:55.119536
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    a = Exclude.NEVER(2)
    assert a == False


# Generated at 2022-06-13 19:09:59.142041
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None) == True
    assert Exclude.ALWAYS(False) == True
    assert Exclude.ALWAYS(1234567890) == True
    assert Exclude.ALWAYS('foo') == True


# Generated at 2022-06-13 19:10:02.254785
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS("Hello")
    assert Exclude.ALWAYS(False)
    assert Exclude.ALWAYS(Exclude)
    assert Exclude.ALWAYS(Exclude.ALWAYS)


# Generated at 2022-06-13 19:10:06.560703
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS('1')
    assert Exclude.ALWAYS(False)
    assert Exclude.ALWAYS(True)


# Generated at 2022-06-13 19:10:09.470848
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(0) == False


# Generated at 2022-06-13 19:10:11.434693
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("a") == True



# Generated at 2022-06-13 19:10:14.769054
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    class DataClass:
        field = "field"

    assert Exclude.NEVER(DataClass.field)



# Generated at 2022-06-13 19:10:17.161322
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(5)
    assert Exclude.ALWAYS('string')


# Generated at 2022-06-13 19:10:25.976103
# Unit test for function config
def test_config():
    import marshmallow as ma
    @dataclass
    class Test:
        x: int = config(
            encoder=int, decoder=int, field_name="y",
            letter_case=lambda x: x.upper(),
            undefined=Undefined.RAISE,
            exclude=Exclude.NEVER)

    test = Test(0)

# Generated at 2022-06-13 19:10:28.279378
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER('abc') == False


# Generated at 2022-06-13 19:10:30.133143
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert (Exclude.ALWAYS(1) == True)
    assert (Exclude.ALWAYS(0) == True)
    assert (Exclude.ALWAYS(-1) == True)


# Generated at 2022-06-13 19:10:32.164825
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    result = Exclude.ALWAYS("test")
    assert result == True


# Generated at 2022-06-13 19:10:33.236285
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(None) == False

# Generated at 2022-06-13 19:10:35.663755
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True

# Generated at 2022-06-13 19:10:37.808752
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    def _local_func(x: str) -> bool:
        return False

    assert Exclude.NEVER == _local_func


# Generated at 2022-06-13 19:10:40.023877
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False
    assert Exclude.NEVER('a') == False


# Generated at 2022-06-13 19:10:41.718543
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(5)


# Generated at 2022-06-13 19:10:43.587464
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) is True
    assert Exclude.ALWAYS(None) is True


# Generated at 2022-06-13 19:10:45.196319
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("never")


# Generated at 2022-06-13 19:10:46.934523
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(None) == False

# Generated at 2022-06-13 19:10:49.053178
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(None)


if __name__ == "__main__":
    test_Exclude_NEVER()

# Generated at 2022-06-13 19:10:56.960152
# Unit test for function config
def test_config():
    from marshmallow.fields import UUID, Email
    from marshmallow.validate import Email

    @config(metadata={'some_key': 'some_value'},
            encoder=email_encoder,
            decoder=email_decoder,
            mm_field=Email(validate=Email()),
            letter_case=lambda s: s.title(),
            undefined=Undefined.EXCLUDE,
            field_name="my_custom_name",
            exclude=Exclude.ALWAYS,
            )
    class Person:
        ...

# Generated at 2022-06-13 19:10:57.716656
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("True") == True


# Generated at 2022-06-13 19:11:00.035341
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    is_always = Exclude.ALWAYS('test')
    assert is_always == True


# Generated at 2022-06-13 19:11:02.999916
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1)
    assert Exclude.NEVER(None)
    assert Exclude.NEVER(True)
    assert Exclude.NEVER([])


# Generated at 2022-06-13 19:11:04.339372
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    bool_value = Exclude.ALWAYS(None)
    assert bool_value == True


# Generated at 2022-06-13 19:11:10.653677
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS('any')
    assert Exclude.ALWAYS('')
    assert Exclude.ALWAYS(None)
    assert Exclude.ALWAYS({})
    assert Exclude.ALWAYS([])
    assert Exclude.ALWAYS((1,))
    assert Exclude.ALWAYS((1, 2))


# Generated at 2022-06-13 19:11:14.513551
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    # Given: pre-defined constant Exclude.NEVER
    # When: adding the constant to a class
    @dataclass
    class Test:
        i: int = field(metadata={'dataclasses_json': {'exclude': Exclude.NEVER}})
    result = Test()
    # Expect: the constant affects the value of the field
    assert result.i == 0


# Generated at 2022-06-13 19:11:16.458444
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS('a')


# Generated at 2022-06-13 19:11:21.294232
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    Exclude.NEVER = lambda _: False
    assert Exclude.NEVER(2) == False
    assert Exclude.NEVER("Hello") == False
    assert Exclude.NEVER(['a', 'b']) == False

# Generated at 2022-06-13 19:11:22.388268
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(3) == True


# Generated at 2022-06-13 19:11:24.558452
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS('a') == True


# Generated at 2022-06-13 19:11:26.917316
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    result = Exclude.NEVER(8)
    expected = False
    assert result == expected


# Generated at 2022-06-13 19:11:31.691572
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False

# Generated at 2022-06-13 19:11:33.633424
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    param = 1
    assert Exclude.NEVER(param) == False

# Generated at 2022-06-13 19:11:35.718200
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) is True
    assert Exclude.ALWAYS('') is True
    assert Exclude.ALWAYS(None) is True


# Generated at 2022-06-13 19:11:36.736612
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True


# Generated at 2022-06-13 19:11:38.192378
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    def always_true(_):
        return True
    assert Exclude.ALWAYS (1) == always_true(1)


# Generated at 2022-06-13 19:11:41.387050
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    x = Exclude.NEVER
    print(x)
    assert x(1) == True, "Test Failed"


# Generated at 2022-06-13 19:11:44.631045
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert(Exclude.ALWAYS(2) == True)
    assert(Exclude.ALWAYS(0) == True)
    assert(Exclude.ALWAYS(-2) == True)


# Generated at 2022-06-13 19:11:46.842921
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    import dataclasses
    @dataclasses.dataclass
    class Example:
        a: str = dataclasses.field(metadata={'dataclasses_json': {'exclude': Exclude.NEVER}})

    assert Example.__annotations__["a"] == "str"

# Generated at 2022-06-13 19:11:49.965307
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert(Exclude.ALWAYS(None) == True)
    assert(Exclude.ALWAYS("Hello") == True)
    assert(Exclude.ALWAYS(1) == True)


# Generated at 2022-06-13 19:11:53.772465
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False
    assert Exclude.NEVER("a") == False
    assert Exclude.NEVER("") == False
    assert Exclude.NEVER("1") == False

# Generated at 2022-06-13 19:12:00.333124
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(7) == False


# Generated at 2022-06-13 19:12:01.802795
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    e = Exclude()
    x = e.ALWAYS(3)
    return x


# Generated at 2022-06-13 19:12:02.841303
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert not Exclude.NEVER(object())


# Generated at 2022-06-13 19:12:06.146600
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    # Arrange
    obj = Exclude()
    # Act
    res = obj.NEVER
    # Assert

# Generated at 2022-06-13 19:12:07.977089
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert(Exclude.ALWAYS(1))
    assert(Exclude.ALWAYS(True))
    assert(Exclude.ALWAYS("Hi"))
    assert(Exclude.ALWAYS(None))


# Generated at 2022-06-13 19:12:09.135576
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert not Exclude.NEVER(1)

# Generated at 2022-06-13 19:12:11.038605
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(0) == False, "NEVER must return False"



# Generated at 2022-06-13 19:12:12.611455
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    foo = Exclude.ALWAYS("bar")
    return foo

# Generated at 2022-06-13 19:12:15.203486
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) is True
    assert Exclude.ALWAYS('a') is True


# Generated at 2022-06-13 19:12:21.959572
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    c = Exclude
    assert c.NEVER(1) == False
    assert c.NEVER("String") == False
    assert c.NEVER([1, 2, 3]) == False
    assert c.NEVER((1, 2, 3)) == False
    assert c.NEVER({"a": 1, "b": 2, "c": 3}) == False
    assert c.NEVER({"a": "1", "b": "2", "c": "3"}) == False


# Generated at 2022-06-13 19:12:33.303626
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    pass

# Generated at 2022-06-13 19:12:34.899987
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert(Exclude.ALWAYS(True) == True)


# Generated at 2022-06-13 19:12:36.708470
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    exclude = Exclude.NEVER
    result = exclude("test")
    assert result == False

# Generated at 2022-06-13 19:12:37.578919
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER('anything') == False

# Generated at 2022-06-13 19:12:41.109082
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    from dataclasses import dataclass
    @dataclass
    class Example:
        included: str
        excluded: str = config(exclude=Exclude.NEVER)
    example = Example(included='included', excluded='excluded')
    assert example.excluded == 'excluded'

# Generated at 2022-06-13 19:12:43.531544
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    # Arrange
    obj = None

    # Act
    result = Exclude.ALWAYS(obj)

    # Assert
    assert result == True



# Generated at 2022-06-13 19:12:45.998050
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True
    assert Exclude.ALWAYS(None) == True


# Generated at 2022-06-13 19:12:57.785297
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    data = {"name":"John","age":30,"cars":{"car1" : "Ford","car2" : "BMW","car3" : "Fiat"}}
    #print(Exclude.ALWAYS(data))
    assert Exclude.ALWAYS(data) == True


# Generated at 2022-06-13 19:12:58.399672
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(None)

# Generated at 2022-06-13 19:13:01.544943
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(3)
    assert Exclude.ALWAYS('3')
    assert Exclude.ALWAYS(None)
    assert Exclude.ALWAYS([3, 4])


# Generated at 2022-06-13 19:13:33.154512
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("a") == True


# Generated at 2022-06-13 19:13:35.265528
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    e_obj = Exclude()
    assert(e_obj.ALWAYS("something") == True)


# Generated at 2022-06-13 19:13:36.039931
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True


# Generated at 2022-06-13 19:13:37.047056
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    result = Exclude.ALWAYS(1)
    assert result == True


# Generated at 2022-06-13 19:13:38.563997
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("") == True



# Generated at 2022-06-13 19:13:40.072489
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) is False


# Generated at 2022-06-13 19:13:43.672778
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert(Exclude.NEVER(1) == False)
    assert(Exclude.NEVER(0) == False)
    assert(Exclude.NEVER(None) == False)
    assert(Exclude.NEVER('') == False)
    assert(Exclude.NEVER('a string') == False)


# Generated at 2022-06-13 19:13:47.193971
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(2) is True
    assert Exclude.ALWAYS(0) is True
    assert Exclude.ALWAYS(5) is True
    assert Exclude.ALWAYS(67) is True
    assert Exclude.ALWAYS(-4) is True
    assert Exclude.ALWAYS(-7) is True


# Generated at 2022-06-13 19:13:48.198749
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("") == True


# Generated at 2022-06-13 19:13:54.207779
# Unit test for function config
def test_config():
    from marshmallow.fields import Boolean
    from dataclasses import dataclass, field
    import copy
    
    @dataclass
    class Person:
        name: str
        age: int
        human: bool = True

        @config(encoder=lambda arg: arg.lower())
        def get_name(self):
            return self.name

    p = Person('Nate', 35)
    res = as_dict(p)
    
    assert res == {
        'name': 'nate',
        'age': 35,
        'human': True
    }
    
    p = Person('Nate', 35, human=False)
    res = as_dict(p)

    assert res == {
        'name': 'nate',
        'age': 35,
        'human': False
    }


# Generated at 2022-06-13 19:15:27.618081
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    print(Exclude.NEVER(1))

# Generated at 2022-06-13 19:15:28.974121
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("test") == False


# Generated at 2022-06-13 19:15:40.536785
# Unit test for function config
def test_config():
    from dataclasses import dataclass as dataclass_no_config, field as _field
    from dataclasses_json import dataclass
    from dataclasses_json.undefined import UNDEFINED

    # Test for a dataclass with no config
    @dataclass_no_config
    class Instance:
        a: str

    assert not hasattr(dataclasses.fields(Instance)[0], "metadata")
    assert Instance.__config__() is None

    # Test for a dataclass with default config
    @dataclass
    class Instance:
        a: str

    assert not hasattr(dataclasses.fields(Instance)[0], "metadata")
    assert Instance.__config__() == {"dataclasses_json": {}}

    # Test for a dataclass with customized configs
   

# Generated at 2022-06-13 19:15:45.265593
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("") == False
    assert Exclude.NEVER(" ") == False
    assert Exclude.NEVER("test") == False
    assert Exclude.NEVER(" test") == False
    assert Exclude.NEVER("test ") == False
    assert Exclude.NEVER(" test ") == False


# Generated at 2022-06-13 19:15:48.410090
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None)
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS("test")


# Generated at 2022-06-13 19:15:50.680332
# Unit test for method ALWAYS of class Exclude

# Generated at 2022-06-13 19:15:51.585506
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER('abc') is False

# Generated at 2022-06-13 19:15:52.634290
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    print(Exclude.ALWAYS('test'))



# Generated at 2022-06-13 19:16:08.970124
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    @dataclass
    class TestClass:
        pass

    @dataclass_json
    @dataclass
    class TestClass2:
        attr: TestClass

    assert TestClass2(TestClass()).to_dict() == {'attr': {}}

    @dataclass_json(exclude=Exclude.NEVER)
    @dataclass
    class TestClass2:
        attr: TestClass

    assert TestClass2(TestClass()).to_dict() == {'attr': {}}

    @dataclass_json(exclude=Exclude.ALWAYS)
    @dataclass
    class TestClass2:
        attr: TestClass

    assert TestClass2(TestClass()).to_dict() == {}



# Generated at 2022-06-13 19:16:10.055623
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("") == True


# Generated at 2022-06-13 19:19:22.309185
# Unit test for function config
def test_config():
    from dataclasses import dataclass, field
    from dataclasses_json import config
    @dataclass
    class foo:
        """
        Test class
        """
        __metadata__ = config(exclude=Exclude.NEVER,
                              letter_case=lambda s: s.upper(),
                              undefined=Undefined.RAISE,
                              field_name="bar")
        bar: int

    assert foo.__metadata__["dataclasses_json"]["exclude"] == Exclude.NEVER
    assert foo.__metadata__["dataclasses_json"]["letter_case"]("bar") == "BAR"
    assert foo.__metadata__["dataclasses_json"]["undefined"] == Undefined.RAISE

# Generated at 2022-06-13 19:19:24.151033
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("A") == True


# Generated at 2022-06-13 19:19:26.068045
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None)



# Generated at 2022-06-13 19:19:29.840323
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    field = config(exclude=Exclude.ALWAYS)
    assert field['dataclasses_json']['exclude'](None,None)


# Generated at 2022-06-13 19:19:37.571234
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    func = Exclude.NEVER
    assert func(0) == False, "Something is wrong in Exclude.NEVER"
    assert func(1) == False, "Something is wrong in Exclude.NEVER"
    assert func(1000) == False, "Something is wrong in Exclude.NEVER"
    assert func(-1) == False, "Something is wrong in Exclude.NEVER"
