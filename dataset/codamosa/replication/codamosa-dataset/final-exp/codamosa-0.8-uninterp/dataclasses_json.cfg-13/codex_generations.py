

# Generated at 2022-06-13 19:09:41.886319
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert NEVER(0) == False

# Generated at 2022-06-13 19:09:43.695486
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    class Test:
        def __init__(self, x):
            self.x = x

    test = Test(x = 10)
    result = Exclude.NEVER(test.x)
    print(result)


config()


# Generated at 2022-06-13 19:09:45.529387
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None) == True


# Generated at 2022-06-13 19:09:53.578920
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None)


# Generated at 2022-06-13 19:09:55.547702
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("abc") == True


# Generated at 2022-06-13 19:10:01.976213
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    EXC = Exclude()
    assert EXC.NEVER(3) == False
    assert EXC.NEVER(54) == False

# Generated at 2022-06-13 19:10:04.541714
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS(-2)
    assert Exclude.ALWAYS(100.0)
    assert Exclude.ALWAYS('Ala ma kota')


# Generated at 2022-06-13 19:10:07.238349
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    # Test for ALWAYS
    assert Exclude.ALWAYS(3) is True
    assert Exclude.ALWAYS(None) is True
    assert Exclude.ALWAYS('string') is True


# Generated at 2022-06-13 19:10:08.386873
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("dummy") == True


# Generated at 2022-06-13 19:10:09.841871
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    a = Exclude.NEVER('abc')
    assert(a == False)


# Generated at 2022-06-13 19:10:17.120469
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(True) == False
    assert Exclude.NEVER(False) == False
    print("test Exclude.NEVER passed")

test_Exclude_NEVER()



# Generated at 2022-06-13 19:10:20.729121
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(2)
    assert Exclude.ALWAYS(True)
    assert Exclude.ALWAYS(False)
    assert Exclude.ALWAYS('2')
    assert Exclude.ALWAYS('True')
    assert Exclude.ALWAYS('False')


# Generated at 2022-06-13 19:10:22.039211
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    print(Exclude.NEVER(4))



# Generated at 2022-06-13 19:10:23.249979
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("abc") == False


# Generated at 2022-06-13 19:10:25.905740
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None) is True
    assert Exclude.ALWAYS(1) is True
    assert Exclude.ALWAYS('a') is True
    assert Exclude.ALWAYS({'a': 1}) is True



# Generated at 2022-06-13 19:10:30.128935
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    # Arrange
    test_class = Exclude()
    expected = False
    # Act
    actual = test_class.NEVER("test")
    # Assert
    assert expected == actual


# Generated at 2022-06-13 19:10:34.380630
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    # Arrange
    arg1 = 1
    arg2 = 2

    # Act
    # Assert
    assert Exclude.NEVER(arg1) is True
    assert Exclude.NEVER(arg2) is True


# Generated at 2022-06-13 19:10:35.912746
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False


# Generated at 2022-06-13 19:10:41.914870
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    import unittest

    class TestExclude(unittest.TestCase):
        def test_Exclude_ALWAYS(self):
            A = Exclude.ALWAYS(10)
            self.assertEqual(A, True)

    suite = unittest.TestLoader().loadTestsFromModule(TestExclude())
    unittest.TextTestRunner().run(suite)


# Generated at 2022-06-13 19:10:43.337742
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1)



# Generated at 2022-06-13 19:10:48.312096
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    # Arrange
    t = Exclude()
    t1 = Exclude()
    # Act & Assert
    assert t.ALWAYS(t1) == True


# Generated at 2022-06-13 19:10:56.579685
# Unit test for function config
def test_config():
    from dataclasses import dataclass
    from typing import Optional

    @dataclass
    class A:
        prop: int = config(field_name="property")
        optional: Optional[str] = None

    assert A.__dataclass_fields__['prop'].metadata \
        == {'dataclasses_json': {'field_name': 'property'}}
    assert A.__dataclass_fields__['optional'].metadata \
        == {'dataclasses_json': {}}

    try:
        @dataclass
        class B:
            prop: int = config(undefined="Invalid")

    except UndefinedParameterError:
        assert True
    else:
        assert False


# Generated at 2022-06-13 19:11:06.212897
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.EVERYWHERE(1)
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS(True)
    assert Exclude.ALWAYS(False)
    assert Exclude.ALWAYS(None)
    assert Exclude.ALWAYS('1')
    assert Exclude.ALWAYS('')
    assert Exclude.ALWAYS([])
    assert Exclude.ALWAYS({})



# Generated at 2022-06-13 19:11:07.677003
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("some_value") == False


# Generated at 2022-06-13 19:11:09.684977
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True
    assert Exclude.ALWAYS(None) == True
    assert Exclude.ALWAYS("test") == True


# Generated at 2022-06-13 19:11:11.292854
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS('Test') == True


# Generated at 2022-06-13 19:11:12.325092
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False


# Generated at 2022-06-13 19:11:15.627138
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    obj = Exclude()
    assert obj.ALWAYS(1) == True


# Generated at 2022-06-13 19:11:25.260505
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("1")
    assert Exclude.ALWAYS("True")
    assert Exclude.ALWAYS("true")


# Generated at 2022-06-13 19:11:34.303062
# Unit test for function config
def test_config():
    from dataclasses import dataclass
    import marshmallow

    @dataclass
    @config(letter_case=str.lower)
    class A:
        name: str

    assert A.__dataclass_fields__["name"].metadata["dataclasses_json"]["letter_case"] == str.lower

    @dataclass
    @config(exclude=Exclude.ALWAYS)
    class B:
        name: str

    assert B.__dataclass_fields__["name"].metadata["dataclasses_json"]["exclude"] == Exclude.ALWAYS

    @dataclass
    @config(undefined=Undefined.EXCLUDE)
    class C:
        name: str


# Generated at 2022-06-13 19:11:36.912404
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("abcd") == True


# Generated at 2022-06-13 19:11:37.845943
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("ANYTHING")


# Generated at 2022-06-13 19:11:45.532123
# Unit test for function config
def test_config():
    from marshmallow import fields, Schema
    from dataclasses import dataclass
    from dataclasses_json import mm_schema

    @dataclass
    class TestData:
        test: int = config(
            encoder=lambda n: n + 1,
            decoder=lambda n: n - 1)

    assert TestData().test == 0
    assert TestData.__annotations__['test']['dataclasses_json']['encoder'](0) == 1
    assert TestData.__annotations__['test']['dataclasses_json']['decoder'](1) == 0

    @dataclass
    class TestData:
        test: int = config(
            mm_field=fields.Integer(validate=lambda n: n == 2))

    assert TestData().test == 0

# Generated at 2022-06-13 19:11:46.310194
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER('john') == False

# Generated at 2022-06-13 19:11:50.119861
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS('test')
    assert Exclude.ALWAYS({})
    assert Exclude.ALWAYS([])
    assert Exclude.ALWAYS(None)


# Generated at 2022-06-13 19:11:52.116947
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None) == True


# Generated at 2022-06-13 19:11:54.481313
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None)
    assert Exclude.ALWAYS("1")
    assert Exclude.ALWAYS(20)


# Generated at 2022-06-13 19:12:02.499978
# Unit test for function config
def test_config():
    class A:
        def __init__(self, a):
            self._a = a

        @property
        def a(self):
            return self._a

    class B:
        def __init__(self, b):
            self._b = b

        @property
        def b(self):
            return self._b

    encoder = lambda obj: dict(a=obj.a)
    decoder = lambda data: A(**data)

    @global_config.encoders.register
    @config(encoder=encoder)
    class D(A, B):
        pass

    @global_config.decoders.register
    @config(decoder=decoder)
    class E(D):
        pass


# Generated at 2022-06-13 19:12:04.220112
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("") == True
    assert Exclude.ALWAYS("hello") == True
    assert Exclude.ALWAYS(5) == True
    assert Exclude.ALWAYS(True) == True
    assert Exclude.ALWAYS(False) == True


# Generated at 2022-06-13 19:12:05.221315
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(0) == False


# Generated at 2022-06-13 19:12:10.670181
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False

# Unit test method ALWAYS of class Exclude

# Generated at 2022-06-13 19:12:13.233576
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    class A:
        pass
    
    a = A()
    
    assert Exclude.NEVER(a) == False
    

# Generated at 2022-06-13 19:12:15.361095
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
	a = 1
	assert Exclude.NEVER(a) == False


# Generated at 2022-06-13 19:12:19.460938
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True
    assert Exclude.ALWAYS('hello') == True
    assert Exclude.ALWAYS(True) == True
    assert Exclude.ALWAYS(tuple(['abc'])) == True


# Generated at 2022-06-13 19:12:21.959559
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("string")
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS(1.0)
    assert Exclude.ALWAYS(True)


# Generated at 2022-06-13 19:12:23.128610
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("a") == False

# Generated at 2022-06-13 19:12:27.781738
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    class test:
        def __init__(self, a, e=None):
            self.a = a
            self.e = e

    t = test(1, Exclude.ALWAYS)
    assert t.a==1
    assert t.e(2)

# Generated at 2022-06-13 19:12:29.212529
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("test")


# Generated at 2022-06-13 19:12:32.078150
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    import datetime

    date_with_time = datetime.datetime(2010, 10, 5, 23, 40, 30, 0)
    assert Exclude.NEVER(date_with_time)


# Generated at 2022-06-13 19:12:35.005786
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert(Exclude.ALWAYS(None))
    assert(Exclude.ALWAYS(1))
    assert(Exclude.ALWAYS("test"))


# Generated at 2022-06-13 19:12:43.059242
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(None)


# Generated at 2022-06-13 19:12:46.767541
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True
    assert Exclude.ALWAYS('a') == True
    assert Exclude.ALWAYS(True) == True
    assert Exclude.ALWAYS(False) == True


# Generated at 2022-06-13 19:12:47.935829
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    per = Exclude.NEVER("name")
    assert per == False

# Generated at 2022-06-13 19:12:56.688459
# Unit test for function config
def test_config():
    from marshmallow import fields
    from dataclasses import dataclass

    @dataclass
    class Test:
        a: int = None
        b: str = None
        c: int = None
        d: str = None

    # test is None
    assert config() == {'dataclasses_json': {}}

    # test is exist
    metadata = config(metadata = {'a': 1,},
                      encoder = {'b': 2},
                      decoder = {'c': 3},
                      mm_field = fields.Integer(5),
                      letter_case = lambda s: s,
                      undefined = 'ignore',
                      field_name = 'exclude')

# Generated at 2022-06-13 19:12:57.785303
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None) is True

# Generated at 2022-06-13 19:13:00.764280
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False
    assert Exclude.NEVER(2) == False
    assert Exclude.NEVER(3) == False


# Generated at 2022-06-13 19:13:16.553245
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    class TestData:
        def __init__(self, firstname, lastname, email, locid):
            self.firstname = firstname
            self.lastname = lastname
            self.email = email
            self.locid = locid

    test_data = TestData("Pratik", "Chetia", "pratik.chetia@mail.utoronto.ca", "1")

    assert Exclude.NEVER(test_data) == False



# Generated at 2022-06-13 19:13:18.173433
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
  assert Exclude.NEVER(True) == False
  assert Exclude.NEVER(False) == False


# Generated at 2022-06-13 19:13:20.017523
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1)



# Generated at 2022-06-13 19:13:22.228988
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True


# Generated at 2022-06-13 19:13:37.830627
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(2) == True


# Generated at 2022-06-13 19:13:39.801813
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    NEVER = Exclude.NEVER
    assert NEVER(True) == False
    assert NEVER(False) == False
    return True


# Generated at 2022-06-13 19:13:40.870174
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    print(Exclude.NEVER(2))



# Generated at 2022-06-13 19:13:44.232027
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("a") == False
    assert Exclude.NEVER(1) == False
    assert Exclude.NEVER([1, 2]) == False
    assert Exclude.NEVER((1, 2)) == False
    assert Exclude.NEVER({"a":2}) == False


# Generated at 2022-06-13 19:13:45.174221
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(True) == False
    assert Exclude.NEVER(False) == False


# Generated at 2022-06-13 19:13:45.660451
# Unit test for function config
def test_config():
    config()

# Generated at 2022-06-13 19:13:52.203340
# Unit test for function config
def test_config():
    # Setup
    from marshmallow import fields, Schema
    from marshmallow.fields import Field as MarshalField

    # Exercise

    class UserSchema(Schema):
        age = fields.Float()
        name = fields.String(attribute="userName")

    @config(mm_field=MarshalField(attribute='age'))
    class Age:
        pass

    config(
        encoder=int,
        decoder=float,
        mm_field=fields.Integer,
        letter_case=lambda s: s,
        undefined=Undefined.EXCLUDE,
        field_name="_field")


# Generated at 2022-06-13 19:13:53.092322
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    res = Exclude.NEVER(1)
    assert res is False


# Generated at 2022-06-13 19:13:54.340423
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(10)
    assert Exclude.ALWAYS('abc')


# Generated at 2022-06-13 19:13:55.013708
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("anything") == False

# Generated at 2022-06-13 19:14:26.974981
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(3) == False
    assert Exclude.NEVER("") == False
    assert Exclude.NEVER("abc") == False
    assert Exclude.NEVER("9!@&$*#") == False
    assert Exclude.NEVER("exclude") == False



# Generated at 2022-06-13 19:14:28.005075
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(None) == True


# Generated at 2022-06-13 19:14:28.992651
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    x = 1
    assert Exclude.NEVER(x) == False


# Generated at 2022-06-13 19:14:35.764200
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None) == True
    assert Exclude.ALWAYS(4) == True
    assert Exclude.ALWAYS("string") == True
    assert Exclude.ALWAYS(3.14) == True
    assert Exclude.ALWAYS(('a', 'b', 'c')) == True
    assert Exclude.ALWAYS([1, 2, 3]) == True
    assert Exclude.ALWAYS({'a':1, 'b':2, 'c':3}) == True


# Generated at 2022-06-13 19:14:37.205289
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1)



# Generated at 2022-06-13 19:14:38.634870
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(3) == True
    return



# Generated at 2022-06-13 19:14:40.246211
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    output = Exclude.ALWAYS(3)
    assert output == True


# Generated at 2022-06-13 19:14:42.847737
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    obj = Exclude()
    assert obj.ALWAYS(1) == True


# Generated at 2022-06-13 19:14:44.100522
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None) == True


# Generated at 2022-06-13 19:14:46.789117
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    def d():
        print("boom")

    assert_that(Exclude.NEVER(d), equal_to(False), message="Method NEVER should return false")



# Generated at 2022-06-13 19:16:04.498069
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    # When Exclude.NEVER is called with a value
    bool_value = Exclude.NEVER(3)
    # Then it should return False
    assert bool_value == False


# Generated at 2022-06-13 19:16:06.115187
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(["e", "f", "g"]) == False


# Generated at 2022-06-13 19:16:09.108442
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False
    assert Exclude.NEVER(-1) == False
    assert Exclude.NEVER(0) == False
    assert Exclude.NEVER(3.14) == False
    assert Exclude.NEVER('abc') == False
    assert Exclude.NEVER('') == False


# Generated at 2022-06-13 19:16:09.744062
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER('s') == False


# Generated at 2022-06-13 19:16:10.665698
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER('some field name') == False



# Generated at 2022-06-13 19:16:11.774489
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude().ALWAYS(True)
    assert Exclude().ALWAYS(False)


# Generated at 2022-06-13 19:16:13.386552
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(True)
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS('s')
    assert Exclude.ALWAYS('0')

# Generated at 2022-06-13 19:16:14.458191
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(0) == False
    assert Exclude.NEVER('a') == False


# Generated at 2022-06-13 19:16:17.189436
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(0)



# Generated at 2022-06-13 19:16:19.307639
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER('') == False


# Generated at 2022-06-13 19:18:51.529607
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) is False


# Generated at 2022-06-13 19:18:52.737272
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert(Exclude.NEVER(1) == False)

# Generated at 2022-06-13 19:18:54.489657
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(5)


# Generated at 2022-06-13 19:18:57.526215
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    # Arrange
    input = {"test":"test"}

    # Act
    output = Exclude.NEVER(input)

    # Assert
    assert output == False


# Generated at 2022-06-13 19:18:58.344269
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(0)

# Generated at 2022-06-13 19:19:00.227248
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert(Exclude.ALWAYS("abc") == True)


# Generated at 2022-06-13 19:19:02.062478
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER('abc') != False

# Generated at 2022-06-13 19:19:03.358931
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(True) == True


# Generated at 2022-06-13 19:19:04.574180
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False


# Generated at 2022-06-13 19:19:06.084380
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    def func():
        return False

    assert(Exclude.ALWAYS(func()) == True)
