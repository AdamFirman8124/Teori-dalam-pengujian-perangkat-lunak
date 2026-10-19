

# Generated at 2022-06-13 19:09:40.263703
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER([])
    assert Exclude.NEVER({})
    assert Exclude.NEVER(Exclude.NEVER)


# Generated at 2022-06-13 19:09:42.288000
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(True) == True


# Generated at 2022-06-13 19:09:45.698136
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(None)
    assert Exclude.NEVER(0)
    assert Exclude.NEVER([])
    assert Exclude.NEVER({})
    assert Exclude.NEVER("")


# Generated at 2022-06-13 19:09:54.687337
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    @dataclass
    class TestClass:
        a: str
        b: str = field(metadata=config(exclude=Exclude.ALWAYS))
        c: str = field(metadata=config(exclude=Exclude.ALWAYS))

    assert not TestClass.__dataclass_fields__['b'].metadata['dataclasses_json']['exclude']('b', dict())
    assert not TestClass.__dataclass_fields__['c'].metadata['dataclasses_json']['exclude']('c', dict())


# Generated at 2022-06-13 19:10:04.535626
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    # pylint: disable=too-many-statements
    from uuid import UUID
    from datetime import datetime
    from dataclasses import dataclass
    from dataclasses_json import dataclass_json
    from dataclasses_json import DataClassJsonMixin

    @dataclass_json
    @dataclass
    class MyTestClass(DataClassJsonMixin):
        """
        MyTestClass
        """
        pk: UUID
        timestamp: datetime

    test_data = MyTestClass(pk=UUID('10000000-0000-0000-0000-000000000002'),
                            timestamp=datetime(2019, 6, 29, 14, 15, 16))

    json_data = test_data.to_json()
    # print(json_data)

# Generated at 2022-06-13 19:10:06.324559
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(True), Exclude.NEVER(True)


# Generated at 2022-06-13 19:10:09.397556
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS('a') == True


# Generated at 2022-06-13 19:10:13.051614
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(False) == True
    assert Exclude.ALWAYS(True) == True
    assert Exclude.ALWAYS(None) == True


# Generated at 2022-06-13 19:10:15.185210
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(3) == True
    assert Exclude.ALWAYS(2.5) == True
    assert Exclude.ALWAYS('Hola') == True


# Generated at 2022-06-13 19:10:16.854864
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS('')

# Generated at 2022-06-13 19:10:21.133658
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
  # arrange
  x = 5
  expected = False
  # act
  actual = Exclude.NEVER(x)
  # assert
  assert actual == expected


# Generated at 2022-06-13 19:10:24.521139
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(True)
    assert Exclude.ALWAYS(False)
    assert not Exclude.NEVER(True)
    assert not Exclude.NEVER(False)

# Generated at 2022-06-13 19:10:26.381532
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    class TestClass0:
        def __init__(self):
            pass

    assert Exclude.ALWAYS(TestClass0())



# Generated at 2022-06-13 19:10:38.295202
# Unit test for function config
def test_config():
    from datetime import date

    @dataclass
    @config(encoder=lambda obj: f'{obj.year}-{obj.day}-{obj.month}', decoder=str)
    class Date(date):
        pass

    assert Date.__dataclass_fields__['year'].metadata == {}
    assert Date.__dataclass_fields__['day'].metadata == {}
    assert Date.__dataclass_fields__['month'].metadata == {}
    assert Date.__dataclass_fields__['year'].type == int
    assert Date.__dataclass_fields__['day'].type == int
    assert Date.__dataclass_fields__['month'].type == int

# Generated at 2022-06-13 19:10:42.413653
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True
    assert Exclude.ALWAYS(2) == True
    assert Exclude.ALWAYS(3) == True
    assert Exclude.ALWAYS(4) == True


# Generated at 2022-06-13 19:10:43.888009
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS('True')==True


# Generated at 2022-06-13 19:10:47.375178
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS("Hello")
    assert Exclude.ALWAYS([1, 2, 3])


# Generated at 2022-06-13 19:10:49.524629
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    always = Exclude.NEVER
    always_none = always(None)
    assert always_none == False


# Generated at 2022-06-13 19:10:54.150482
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    import unittest
    class TestExcludeNever(unittest.TestCase):
        def test(self):
            assert Exclude.NEVER("a") == False
    t = TestExcludeNever()
    t.test()

# Generated at 2022-06-13 19:10:55.789633
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    if Exclude.ALWAYS(3):
        print('ok')
    else:
        print('error')


# Generated at 2022-06-13 19:11:01.232405
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(0)
    assert Exclude.ALWAYS('a')
    assert Exclude.ALWAYS(None)


# Generated at 2022-06-13 19:11:03.448016
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("a")


# Generated at 2022-06-13 19:11:05.696771
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True


# Generated at 2022-06-13 19:11:07.954414
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False


# Generated at 2022-06-13 19:11:09.051576
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(10) == False


# Generated at 2022-06-13 19:11:10.648000
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    result = Exclude.ALWAYS(T)
    assert result, 'Should return True value'


# Generated at 2022-06-13 19:11:11.956504
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(True) == False


# Generated at 2022-06-13 19:11:19.688828
# Unit test for function config
def test_config():
    data = config(field_name='abc')
    assert data['dataclasses_json']['letter_case']('X') == 'abc'

    assert isinstance(config(undefined='ignore')['dataclasses_json']['undefined'], Undefined.IGNORE)
    assert isinstance(config(undefined=Undefined.RAISE)['dataclasses_json']['undefined'], Undefined.RAISE)

# Generated at 2022-06-13 19:11:20.892255
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("abc") is False


# Generated at 2022-06-13 19:11:29.095246
# Unit test for function config
def test_config():
    import dataclasses
    import json

    @config(encoder=lambda v: f"encoded:{v}", decoder=lambda v: f"decoded:{v}")
    @dataclasses.dataclass
    class Simple:
        val: int

    @config(encoder=lambda v: json.dumps(v), decoder=lambda v: json.loads(v))
    @dataclasses.dataclass
    class Complex:
        val: Dict[str, int]

    print(Simple(val=4))
    print(Complex(val={"a": 4}))

# Generated at 2022-06-13 19:11:34.823071
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None) == True
    # assert Exclude.ALWAYS("test") == True


# Generated at 2022-06-13 19:11:35.905087
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert isinstance(Exclude.NEVER, Callable)


# Generated at 2022-06-13 19:11:43.647813
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False
    assert Exclude.NEVER(2) == False
    assert Exclude.NEVER(3) == False
    assert Exclude.NEVER('1') == False
    assert Exclude.NEVER('2') == False
    assert Exclude.NEVER('3') == False


# Generated at 2022-06-13 19:11:44.630084
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False

# Generated at 2022-06-13 19:11:45.498962
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None)

# Generated at 2022-06-13 19:11:50.915447
# Unit test for function config
def test_config():
    """
    Test the config function
    """
    from marshmallow import fields
    from dataclasses import dataclass
    from dataclasses_json.compat import BytesIO

    @dataclass
    class Foo:
        a: int

    def to_string(foo: Foo) -> str:
        return str(foo.a)

    def from_string(string: str) -> Foo:
        return Foo(int(string))

    @config(encoder=to_string, decoder=from_string)
    @dataclass
    class Bar:
        a: int

    assert Bar(1).to_repr() == '1'
    assert Bar(1) == Bar.from_repr('1')


# Generated at 2022-06-13 19:11:52.462963
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("Anything")


# Generated at 2022-06-13 19:11:55.669930
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(0) == True
    assert Exclude.ALWAYS(None) == True
    assert Exclude.ALWAYS('') == True
    assert Exclude.ALWAYS(False) == True


# Generated at 2022-06-13 19:11:57.939463
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    e = Exclude.NEVER(True)
    print(e)
    f = Exclude.NEVER(False)
    print(f)


# Generated at 2022-06-13 19:11:59.355594
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(3) == False


# Generated at 2022-06-13 19:12:07.419762
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    testField = Exclude.NEVER(object)
    assert testField == False

# Generated at 2022-06-13 19:12:09.050595
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(5) == False


# Generated at 2022-06-13 19:12:11.514892
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(True) == False
    assert Exclude.NEVER(False) == False
    assert Exclude.NEVER(None) == False

# Generated at 2022-06-13 19:12:13.064415
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None)


# Generated at 2022-06-13 19:12:15.203483
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
	assert Exclude.NEVER(Exclude.NEVER)


# Generated at 2022-06-13 19:12:17.015113
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None) == True
    return


# Generated at 2022-06-13 19:12:18.693091
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("hello") == False

# Generated at 2022-06-13 19:12:21.023785
# Unit test for method NEVER of class Exclude

# Generated at 2022-06-13 19:12:23.079739
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER({}) == False



# Generated at 2022-06-13 19:12:26.373165
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) is False
    assert Exclude.NEVER(-1) is False
    assert Exclude.NEVER(.1) is False
    assert Exclude.NEVER(-.1) is False

# Generated at 2022-06-13 19:12:41.824747
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False

# Generated at 2022-06-13 19:12:44.223454
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    class MyClass:
        pass

    my_object = MyClass()

    # Check if the method NEVER returns false for a given object
    assert not Exclude.NEVER(my_object)

# Generated at 2022-06-13 19:12:46.201478
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(True) == True


# Generated at 2022-06-13 19:12:54.465678
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert not Exclude.NEVER(1)


# Generated at 2022-06-13 19:12:57.133550
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(True) == False
    assert Exclude.NEVER(False) == False


# Generated at 2022-06-13 19:12:58.032600
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(42) == False


# Generated at 2022-06-13 19:13:01.545024
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    # If a field is set to be "excluded always", then it always should be excluded
    assert Exclude.ALWAYS('foo')
    assert Exclude.ALWAYS(123)
    assert Exclude.ALWAYS((1, 2, 3))


# Generated at 2022-06-13 19:13:10.060148
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False

# Generated at 2022-06-13 19:13:12.182447
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("foo")


# Generated at 2022-06-13 19:13:13.977154
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER('foo') == False


# Generated at 2022-06-13 19:13:44.859481
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("") is False

# Generated at 2022-06-13 19:13:45.911325
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS('any string') == True


# Generated at 2022-06-13 19:13:46.891492
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(3) == False


# Generated at 2022-06-13 19:13:52.818297
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    # Create a data class with only one field
    @dataclass
    class Test_Exclude_NEVER_class:
        field_1: int = config(exclude=Exclude.NEVER)
    # Create an object of the data class
    Test_Exclude_NEVER_object = Test_Exclude_NEVER_class(1)
    # Test if the __dict__ of the object contains the field we expect
    Test_Exclude_NEVER_dict = Test_Exclude_NEVER_object.__dict__
    Test_Exclude_NEVER_dict_keys = list(Test_Exclude_NEVER_dict.keys())
    assert ('field_1' in Test_Exclude_NEVER_dict_keys) == True


# Generated at 2022-06-13 19:13:56.868177
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(False) == False
    assert Exclude.NEVER(True) == False
    assert Exclude.NEVER(None) == False
    assert Exclude.NEVER(0) == False
    assert Exclude.NEVER(1) == False
    assert Exclude.NEVER(2) == False
    assert Exclude.NEVER('a') == False
    assert Exclude.NEVER(1.1) == False
    assert Exclude.NEVER('b') == False


# Generated at 2022-06-13 19:13:59.127721
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(None) is False


# Generated at 2022-06-13 19:14:04.386565
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS('a')
    assert Exclude.ALWAYS(True)
    assert Exclude.ALWAYS(1.5)
    assert Exclude.ALWAYS(3j)
    assert Exclude.ALWAYS({"a":1})


# Generated at 2022-06-13 19:14:07.479786
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    f = Exclude.NEVER
    assert f(1) == False
    assert f(1.1) == False
    assert f("str") == False
    assert f(True) == False


# Generated at 2022-06-13 19:14:09.173544
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(None)



# Generated at 2022-06-13 19:14:10.556858
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    res = Exclude.NEVER("abc")
    assert res == False


# Generated at 2022-06-13 19:15:20.722540
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS    # TODO: What does this do?


# Generated at 2022-06-13 19:15:24.840490
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("str") is True
    assert Exclude.ALWAYS(None) is True
    assert Exclude.ALWAYS(1) is True
    assert Exclude.ALWAYS(1.0) is True


# Generated at 2022-06-13 19:15:25.867915
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None)


# Generated at 2022-06-13 19:15:29.382968
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(0) is True
    assert Exclude.ALWAYS('any_string') is True
    assert Exclude.ALWAYS(5.0) is True
    assert Exclude.ALWAYS([]) is True
    assert Exclude.ALWAYS({}) is True
    assert Exclude.ALWAYS(None) is True
    assert Exclude.ALWAYS(stop_iteration()) is True


# Generated at 2022-06-13 19:15:31.633055
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert(Exclude.ALWAYS(True))


# Generated at 2022-06-13 19:15:38.517969
# Unit test for function config
def test_config():
    assert config(undefined='ignore') == {
        'dataclasses_json': {
            'undefined': Undefined.IGNORE,
        },
    }

    assert config(undefined=Undefined.RAISE) == {
        'dataclasses_json': {
            'undefined': Undefined.RAISE,
        },
    }

    with pytest.raises(UndefinedParameterError):
        assert config(undefined='should fail')

    assert config(letter_case=str.upper) == {
        'dataclasses_json': {
            'letter_case': str.upper,
        },
    }

    assert config(field_name='foo') == {
        'dataclasses_json': {
            'letter_case': 'foo',
        },
    }


# Generated at 2022-06-13 19:15:45.833480
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(None) == False


# Generated at 2022-06-13 19:15:47.739387
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("abc") is True


# Generated at 2022-06-13 19:15:49.524703
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(0) == True


# Generated at 2022-06-13 19:15:52.761995
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    # Arrange
    data = Exclude.NEVER
    a = 0
    b = 10

    # Act
    output = data(a)
    output2 = data(b)

    # Assert
    assert output == False
    assert output2 == False


# Generated at 2022-06-13 19:18:35.146593
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None) == True


# Generated at 2022-06-13 19:18:36.079694
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1)



# Generated at 2022-06-13 19:18:40.116695
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    """test_Exclude_ALWAYS()
    """ 
    assert Exclude.ALWAYS(True) == True
    assert Exclude.ALWAYS(False) == True
    assert Exclude.ALWAYS(None) == True
    assert Exclude.ALWAYS(1) == True
    assert Exclude.ALWAYS(0.0) == True
    assert Exclude.ALWAYS('1') == True
    assert Exclude.ALWAYS('a') == True
    assert Exclude.ALWAYS('z') == True

# Generated at 2022-06-13 19:18:40.922991
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None) == True



# Generated at 2022-06-13 19:18:43.391214
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(5) == True
    assert Exclude.ALWAYS("hello") == True
    assert Exclude.ALWAYS(True) == True
    assert Exclude.ALWAYS(False) == True
    assert Exclude.ALWAYS("a") == True
    assert Exclude.ALWAYS("") == True

# Generated at 2022-06-13 19:18:44.424530
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("TEST") == True


# Generated at 2022-06-13 19:18:45.708700
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
  assert Exclude.ALWAYS('x') == True


# Generated at 2022-06-13 19:18:48.639809
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("") == True


# Generated at 2022-06-13 19:18:50.164260
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    """class Exclude method ALWAYS should return True"""
    assert Exclude.ALWAYS(0)



# Generated at 2022-06-13 19:18:56.618201
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    obj1 = 1
    obj2 = [1,2,3]
    obj3 = "abc"
    obj4 = {'a': 'a'}
    obj5 = (1,2)
    if Exclude.NEVER(obj1):
        pass
    else:
        print("Success")

    if Exclude.NEVER(obj2):
        pass
    else:
        print("Success")

    if Exclude.NEVER(obj3):
        pass
    else:
        print("Success")

    if Exclude.NEVER(obj4):
        pass
    else:
        print("Success")

    if Exclude.NEVER(obj5):
        pass
    else:
        print("Success")

test_Exclude_NEVER()