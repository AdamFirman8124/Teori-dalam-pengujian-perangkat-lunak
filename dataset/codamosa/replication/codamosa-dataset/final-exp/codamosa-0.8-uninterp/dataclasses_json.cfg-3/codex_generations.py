

# Generated at 2022-06-13 19:09:40.994027
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1)


# Unit testing for method ALWAYS of class Exclude

# Generated at 2022-06-13 19:09:42.752359
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    x = Exclude.NEVER(3)
    assert x == False
    y = Exclude.NEVER("hello")
    assert y == False


# Generated at 2022-06-13 19:09:43.598672
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("Dummy") == True


# Generated at 2022-06-13 19:09:53.773514
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True
    assert Exclude.ALWAYS(3.14) == True
    assert Exclude.ALWAYS(1 + 3.14j) == True
    assert Exclude.ALWAYS(True) == True
    assert Exclude.ALWAYS(None) == True
    assert Exclude.ALWAYS(1 == 1) == True
    assert Exclude.ALWAYS(float('inf')) == True
    assert Exclude.ALWAYS(float('nan')) == True
    assert Exclude.ALWAYS('a') == True
    assert Exclude.ALWAYS(b'a') == True


# Generated at 2022-06-13 19:10:01.364844
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
	assert Exclude.ALWAYS(1)  == True
	assert Exclude.ALWAYS(2) == True
	assert Exclude.ALWAYS(1.0) == True
	assert Exclude.ALWAYS(True) == True
	assert Exclude.ALWAYS(False) == True
	assert Exclude.ALWAYS([]) == True
	assert Exclude.ALWAYS({}) == True
	assert Exclude.ALWAYS(()) == True
	assert Exclude.ALWAYS('') == True
	assert Exclude.ALWAYS(None) == True


# Generated at 2022-06-13 19:10:02.424513
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    result = Exclude.NEVER(1)
    assert result == False


# Generated at 2022-06-13 19:10:03.648558
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("something")



# Generated at 2022-06-13 19:10:05.056953
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert not Exclude.ALWAYS(None)


# Generated at 2022-06-13 19:10:07.629434
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None)
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS(True)
    assert Exclude.ALWAYS("Hello")


# Generated at 2022-06-13 19:10:11.434180
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert(Exclude.ALWAYS(None) == True)
    assert(Exclude.ALWAYS(1) == True)
    assert(Exclude.ALWAYS('aa') == True)

# Generated at 2022-06-13 19:10:19.738206
# Unit test for function config
def test_config():
    """Simple test of config function"""

    data = {
        'encoder': 1,
        'decoder': 2,
        'mm_field': 3,
        'letter_case': 4,
        'undefined': 5,
        'exclude': 6,
    }

    # If there are no existing settings, defaults to empty dict
    assert config() == {}

    # If config() is called with a pre-existing dict, it modifies it
    assert config(data) == {'dataclasses_json': data}
    data['foo'] = 'bar'
    assert config(data) == {'foo': 'bar', 'dataclasses_json': data}
    data['dataclasses_json']['foo'] = 'baz'
    assert config(data) == data

    # Optional parameters modify the relevant part of the dict


# Generated at 2022-06-13 19:10:20.580959
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True


test_Exclude_ALWAYS()


# Generated at 2022-06-13 19:10:21.871270
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(None) == False


# Generated at 2022-06-13 19:10:25.272275
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():

    def func1(x):
        return True

    def func2(y):
        return True

    assert func1(1) == True
    assert func2("hello") == True

    assert Exclude.ALWAYS(1) == func1(1)
    assert Exclude.ALWAYS("hello") == func2("hello")

# Generated at 2022-06-13 19:10:26.330096
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert callable(Exclude.NEVER)


# Generated at 2022-06-13 19:10:28.986581
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(True) == True
    assert Exclude.ALWAYS(False) == True

# Generated at 2022-06-13 19:10:40.516746
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    from dataclasses import dataclass
    from dataclasses_json import config
    from dataclasses_json.undefined import Undefined


    # Define a dataclass
    @dataclass
    class X:
        a: int = 5
        b: int = 10
        c: int = 15

    # JSON without excluding any fields
    json_str = """{
            "a": 6,
            "b": 7,
            "c": 8
        }"""

    x1 = X.from_json(json_str)
    x2 = X.from_json(json_str, config=config(exclude=Exclude.NEVER))
    assert x1 == x2

    # Define a dataclass with a function
    @dataclass
    class Y:
        a: int = 5
        b

# Generated at 2022-06-13 19:10:45.195429
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():  # pylint: disable=invalid-name
    @dataclasses.dataclass
    class Test:
        a: int = 1
        b: int = 2
    assert Exclude.NEVER('a')
    assert Exclude.NEVER('b')
    assert not Exclude.NEVER('c')

# Generated at 2022-06-13 19:10:47.328046
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    bob = Exclude.ALWAYS("Bob")
    assert bob == True


# Generated at 2022-06-13 19:10:48.070052
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("") == True


# Generated at 2022-06-13 19:10:51.603330
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(2) 


# Generated at 2022-06-13 19:10:52.537864
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(True)
    assert Exclude.ALWAYS(False)


# Generated at 2022-06-13 19:10:54.255025
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER.__name__ == '<lambda>'
    assert not Exclude.NEVER(True)

# Generated at 2022-06-13 19:10:56.775663
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    never = Exclude.NEVER
    assert never(True) == False

# Generated at 2022-06-13 19:10:59.047353
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(12)


# Generated at 2022-06-13 19:11:05.956045
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("")
    assert Exclude.NEVER(" ")
    assert Exclude.NEVER("vlaue")
    assert Exclude.NEVER("1")
    assert Exclude.NEVER("tr")
    assert Exclude.NEVER("tR")


# Generated at 2022-06-13 19:11:13.152919
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(100) == False
    assert Exclude.NEVER(200) == False
    assert Exclude.NEVER(300) == False
    assert Exclude.NEVER(0) == False
    assert Exclude.NEVER(-1) == False
    assert Exclude.NEVER(-0.0) == False
    assert Exclude.NEVER(0.0) == False
    assert Exclude.NEVER('foo') == False
    assert Exclude.NEVER('') == False
    assert Exclude.NEVER([]) == False
    assert Exclude.NEVER(()) == False
    assert Exclude.NEVER({}) == False


# Generated at 2022-06-13 19:11:15.750866
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(0) == True


# Generated at 2022-06-13 19:11:17.305871
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER('a') == False



# Generated at 2022-06-13 19:11:19.689569
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    testdict = {'a':'b', 'c':'d'}
    assert NEVER(testdict) == False


# Generated at 2022-06-13 19:11:22.601383
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(Exclude.NEVER)

# Generated at 2022-06-13 19:11:32.649583
# Unit test for function config
def test_config():
    from marshmallow import fields as mm_fields
    from dataclasses import dataclass

    @dataclass
    @config(encoder=None)
    class MyClass:
        pass
    
    my_class = MyClass()
    
    assert my_class.__dataclass_metadata__['dataclasses_json']['encoder'] is None
    
    @dataclass
    @config(decoder=None)
    class MyClass:
        pass
    
    my_class = MyClass()
    
    assert my_class.__dataclass_metadata__['dataclasses_json']['decoder'] is None
    
    @dataclass
    @config(mm_field=mm_fields.Int)
    class MyClass:
        pass
    
    my_class = MyClass()
    

# Generated at 2022-06-13 19:11:33.738633
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    config(exclude=Exclude.NEVER)

# Generated at 2022-06-13 19:11:36.190879
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) is False
    assert Exclude.NEVER("1") is False



# Generated at 2022-06-13 19:11:41.622012
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    class Person:
      def __init__(self,name,age):
        self.name = name
        self.age = age

    def isPerson(obj):
        return type(obj) is Person

    assert Exclude.NEVER(Person("Johnny",21))


# Generated at 2022-06-13 19:11:47.581035
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True
    assert Exclude.ALWAYS(None) == True
    assert Exclude.ALWAYS("hello") == True
    assert Exclude.ALWAYS(False) == True
    assert Exclude.ALWAYS(True) == True
    assert Exclude.ALWAYS([1,2,3]) == True
    assert Exclude.ALWAYS({"a": 1}) == True


# Generated at 2022-06-13 19:11:49.499138
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    value = 'value'
    result = Exclude.ALWAYS(value)
    assert result


# Generated at 2022-06-13 19:11:51.700666
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    a = Exclude.ALWAYS(None)
    assert a



# Generated at 2022-06-13 19:11:56.034322
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True
    assert Exclude.ALWAYS(0) == True
    assert Exclude.ALWAYS([1,2,3]) == True
    assert Exclude.ALWAYS((1,2,3)) == True
    assert Exclude.ALWAYS({'a':1,'b':2}) == True


# Generated at 2022-06-13 19:11:59.934515
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    class Exclude_Test:
        def __init__(self):
            pass

        def foo(self):
            return 1
        def bar(self):
            return 2

    et = Exclude_Test()

    assert Exclude.NEVER(et.foo)
    assert Exclude.NEVER(et.bar)

# Generated at 2022-06-13 19:12:03.533859
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("abc")
    assert Exclude.ALWAYS("def")
    assert Exclude.ALWAYS("1")


# Generated at 2022-06-13 19:12:11.282706
# Unit test for function config
def test_config():
    from dataclasses import dataclass
    from marshmallow import fields
    import pytest
    from .compat import json

    @config(encoder=int, field_name='aField')
    @dataclass
    class DummyClass:
        """Class for testing configuration."""
        a_field: int

    def test_field(a_field: DummyClass) -> DummyClass:
        """Function for testing configuration."""
        return a_field

    @config(decoder=float)
    @dataclass
    class AnotherDummyClass:
        """Class for testing configuration."""
        a_field: int

    @config()
    @dataclass
    class UndefinedClass:
        """Class for testing undefined parameters."""
        a_field: int


# Generated at 2022-06-13 19:12:12.839748
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert not Exclude.NEVER('1')


# Generated at 2022-06-13 19:12:23.184728
# Unit test for function config
def test_config():
    from marshmallow import fields

    @config(encoder=str, decoder=int, letter_case=str.lower)
    class Foo:
        pass

    assert Foo.__dataclasses_json__ == {
        "encoder": str,
        "decoder": int,
        "letter_case": str.lower,
    }

    # Ensure the function is actually callable, and not just a boolean
    assert callable(Foo.__dataclasses_json__["letter_case"])

    @config(undefined=Undefined.EXCLUDE)
    class Bar:
        pass

    assert Bar.__dataclasses_json__["undefined"] == Undefined.EXCLUDE

    @config(undefined="EXCLUDE")
    class Baz:
        pass

    assert Bar.__dataclasses_json

# Generated at 2022-06-13 19:12:31.764631
# Unit test for function config
def test_config():
    import marshmallow as mm
    class Example:
        pass

    config(encoder=lambda x: '')
    config(decoder=lambda x: x)
    config(mm_field=mm.Integer())
    config(letter_case=lambda x: '')
    config(undefined=Undefined.RAISE)
    config(field_name='name')
    config(exclude=lambda _, instance: False)

    with pytest.raises(UndefinedParameterError):
        config(undefined='invalid')

    # Test if the base class is checked by the decoder
    assert config(decoder=Example)

# Generated at 2022-06-13 19:12:33.352088
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(True) == False



# Generated at 2022-06-13 19:12:35.331769
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    test_data = ['a', 'b', 'c']
    assert Exclude.NEVER(test_data) == False

# Generated at 2022-06-13 19:12:37.248330
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert(Exclude.ALWAYS("Hola") == True)


# Generated at 2022-06-13 19:12:38.810333
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("abc") == False


# Generated at 2022-06-13 19:12:46.416655
# Unit test for function config
def test_config():
    """Unit test for function config"""
    import pytest
    from dataclasses_json.undefined import UNDEFINED, EXCLUDE, SKIP

    with pytest.raises(UndefinedParameterError):
        config(undefined="invalid")
    config(undefined=UNDEFINED)
    config(undefined=EXCLUDE)
    config(undefined=SKIP)
    config(undefined="undefined")
    config(undefined="EXCLUDE")
    config(undefined="skip")

# Generated at 2022-06-13 19:12:50.703287
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    x = Exclude.ALWAYS
    assert x(3) == True


# Generated at 2022-06-13 19:12:51.914335
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(None) is False


# Generated at 2022-06-13 19:12:53.777950
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER('a')
    assert Exclude.NEVER(1)
    assert Exclude.NEVER(None)



# Generated at 2022-06-13 19:12:58.793539
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True
    assert Exclude.ALWAYS("str") == True
    assert Exclude.ALWAYS([1,2,3]) == True
    assert Exclude.ALWAYS((1,2,3)) == True


# Generated at 2022-06-13 19:13:08.247500
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert(Exclude.ALWAYS('') == True)
    assert(Exclude.ALWAYS('Param') == True)
    assert(Exclude.ALWAYS(None) == True)
    assert(Exclude.ALWAYS(0) == True)
    assert(Exclude.ALWAYS(42) == True)
    assert(Exclude.ALWAYS({}) == True)
    assert(Exclude.ALWAYS({'Param'}) == True)
    assert(Exclude.ALWAYS([]) == True)
    assert(Exclude.ALWAYS(['Param']) == True)
    assert(Exclude.ALWAYS({'Param': 42}) == True)
    assert(Exclude.ALWAYS({42: 'Param'}) == True)


# Generated at 2022-06-13 19:13:12.538971
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True
    assert Exclude.ALWAYS("s") == True
    assert Exclude.ALWAYS(int) == True


# Generated at 2022-06-13 19:13:14.254158
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("test")==False


# Generated at 2022-06-13 19:13:17.270045
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    # Create an instance of Exclude
    exclude = Exclude()

    # Run method NEVER on the instance and check if it returns false
    assert not exclude.NEVER(2)


# Generated at 2022-06-13 19:13:19.955417
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    obj = Exclude()
    assert obj.NEVER(1) == False
    

# Generated at 2022-06-13 19:13:23.375449
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    # given
    E = Exclude
    # when
    x = E.NEVER
    # then
    assert x('a') == False

# Generated at 2022-06-13 19:13:29.134528
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    # Setup
    obj = [1, 2, 3]
    expected = False

    # Exercise
    actual = Exclude.NEVER(obj)

    # Verify
    assert expected == actual



# Generated at 2022-06-13 19:13:32.126823
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    class TestExclude():
        def test(self):
            assert Exclude.ALWAYS(None)


# Generated at 2022-06-13 19:13:33.790482
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1)
    assert Exclude.NEVER("")
    assert Exclude.NEVER(True)
    assert Exclude.NEVER(False)


# Generated at 2022-06-13 19:13:36.769541
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    # Given
    x = 5
    # When
    result = Exclude.NEVER(x)
    # Then
    assert result == False


# Generated at 2022-06-13 19:13:39.341100
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS(None)
    assert Exclude.ALWAYS("")

test_Exclude_ALWAYS()


# Generated at 2022-06-13 19:13:41.295406
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    #assert Exclude.NEVER(1) == False
    assert Exclude.NEVER(1) != True


# Generated at 2022-06-13 19:13:43.510802
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    obj = Exclude()
    assert obj.ALWAYS(1) == True

# Generated at 2022-06-13 19:13:49.264781
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("test") == True
    assert Exclude.ALWAYS("") == True
    assert Exclude.ALWAYS(1) == True
    assert Exclude.ALWAYS(1.1) == True
    assert Exclude.ALWAYS({}) == True
    assert Exclude.ALWAYS([]) == True
    assert Exclude.ALWAYS(()) == True



# Generated at 2022-06-13 19:13:50.914439
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    test_list = ["a", "b", "c"]
    assert not any(i in test_list for i in test_list)


# Generated at 2022-06-13 19:13:57.680710
# Unit test for function config
def test_config():
    pass

# Generated at 2022-06-13 19:14:01.740616
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("Failed!") == False


# Generated at 2022-06-13 19:14:04.417079
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    return Exclude.ALWAYS(5)


# Generated at 2022-06-13 19:14:06.724126
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    class SomeClass:
        def __str__(self):
            return "SomeClass"
    assert Exclude.NEVER(SomeClass()) is False

# Generated at 2022-06-13 19:14:08.863943
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(True)
    assert Exclude.ALWAYS(False)


# Generated at 2022-06-13 19:14:10.384460
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) is True
    return True


# Generated at 2022-06-13 19:14:14.903747
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(0)
    assert Exclude.NEVER(False)
    assert Exclude.NEVER(None)
    assert Exclude.NEVER('')
    assert Exclude.NEVER([])
    assert Exclude.NEVER({})
    assert not Exclude.NEVER('a')


# Generated at 2022-06-13 19:14:16.337274
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert(Exclude.ALWAYS("a string") == True)

    assert(Exclude.ALWAYS(42) == True)

    assert(Exclude.ALWAYS(None) == True)


# Generated at 2022-06-13 19:14:18.473138
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    # pylint: disable=expression-not-assigned
    Exclude.ALWAYS("foo")


# Generated at 2022-06-13 19:14:26.542591
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("") == False
    assert Exclude.NEVER("") != True
    assert Exclude.NEVER("B") == False
    assert Exclude.NEVER("B") != True
    assert Exclude.NEVER("C") == False
    assert Exclude.NEVER("C") != True
    assert Exclude.NEVER("D") == False
    assert Exclude.NEVER("D") != True
    assert Exclude.NEVER("E") == False
    assert Exclude.NEVER("E") != True
    assert Exclude.NEVER("F") == False
    assert Exclude.NEVER("F") != True
    assert Exclude.NEVER("G") == False
    assert Exclude.NEVER("G") != True
    assert Exclude.NEVER("H") == False
    assert Exclude.NE

# Generated at 2022-06-13 19:14:28.440561
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    class DummyClass:
        pass
    dummy_obj = DummyClass()
    assert not Exclude.NEVER(dummy_obj)

# Generated at 2022-06-13 19:14:44.789892
# Unit test for function config
def test_config():
    test_metadata = config(
        metadata={},
        encoder=str,
        decoder=int,
        mm_field=MarshmallowField(load_only=True),
        letter_case=str.lower,
        undefined=Undefined.EXCLUDE_IF_MISSING,
        exclude=Exclude.ALWAYS,
    )
    assert test_metadata['dataclasses_json'] == {
        'encoder': str,
        'decoder': int,
        'mm_field': MarshmallowField(load_only=True),
        'letter_case': str.lower,
        'undefined': Undefined.EXCLUDE_IF_MISSING,
        'exclude': Exclude.ALWAYS,
    }


# Generated at 2022-06-13 19:14:46.665742
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(0) is False
    assert Exclude.NEVER(1) is False


# Generated at 2022-06-13 19:14:47.483453
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(0) == False

# Generated at 2022-06-13 19:14:50.020412
# Unit test for function config
def test_config():

    @dataclass
    class A:
        a: str = field()
        b: int = field(metadata=config(field_name="B"))
        c: float = field(metadata=config(exclude=Exclude.ALWAYS))

    result = encode_class(A(a="a", b=1, c=2.0))
    assert result['B'] == 1

    A2 = dataclass(A, frozen=True)

    assert not hasattr(A2(), "c")



# Generated at 2022-06-13 19:14:51.340031
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(0)
    assert Exclude.ALWAYS(1)



# Generated at 2022-06-13 19:14:53.394469
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(True)
    assert Exclude.NEVER(False)


# Generated at 2022-06-13 19:14:58.785524
# Unit test for function config
def test_config():
    import pytest
    with pytest.raises(UndefinedParameterError):
        _ = config(undefined='unhandled')
    assert config(undefined=Undefined.RAISE) == {
        'dataclasses_json': {
            'undefined': Undefined.RAISE
        }
    }

# Generated at 2022-06-13 19:15:07.993612
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(False) is True
    assert Exclude.NEVER(True) is True
    assert Exclude.NEVER(None) is True
    assert Exclude.NEVER("") is True
    assert Exclude.NEVER("aa") is True
    assert Exclude.NEVER(1) is True
    assert Exclude.NEVER(2.2) is True
    assert Exclude.NEVER([]) is True
    assert Exclude.NEVER([1, 2]) is True
    assert Exclude.NEVER(()) is True
    assert Exclude.NEVER((1, 2)) is True
    assert Exclude.NEVER({}) is True
    assert Exclude.NEVER({1, 2}) is True
    assert Exclude.NEVER({1: 2}) is True

# Generated at 2022-06-13 19:15:08.926394
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None) == True



# Generated at 2022-06-13 19:15:10.206092
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False
    assert Exclude.NEVER("test") == False


# Generated at 2022-06-13 19:15:24.580145
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    pass
    assert Exclude.ALWAYS("") == True
    assert Exclude.ALWAYS("abc") == True
    assert Exclude.ALWAYS("abc123._-") == True
    assert Exclude.ALWAYS("*") == True


# Generated at 2022-06-13 19:15:31.459590
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(object)

# Generated at 2022-06-13 19:15:35.246965
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    e1 = Exclude.ALWAYS
    assert e1(1) == True
    assert e1(0.5) == True
    assert e1('a') == True
    assert e1(Exclude) == True


# Generated at 2022-06-13 19:15:38.823426
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None) == True
    assert Exclude.ALWAYS("") == True
    assert Exclude.ALWAYS("a") == True


# Generated at 2022-06-13 19:15:40.357062
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS('input') == True

# Generated at 2022-06-13 19:15:41.843331
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
	assert Exclude.NEVER("test") == False

# Generated at 2022-06-13 19:15:42.908066
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER('a') == False


# Generated at 2022-06-13 19:15:47.982547
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():

    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS(0)
    assert Exclude.ALWAYS('True')
    assert Exclude.ALWAYS(True)
    assert Exclude.ALWAYS({'a': 1, 'b': 2})
    assert Exclude.ALWAYS(
        ('this', 'is', 'list'))
    assert Exclude.ALWAYS([1, 2, 3])
    assert Exclude.ALWAYS({'foo': 'bar'})
    assert Exclude.ALWAYS(['foo', 'bar'])
    assert Exclude.ALWAYS(('foo', 'bar'))
    assert Exclude.ALWAYS({1, 2, 3})
    assert Exclude.ALWAYS(None)
    assert Exclude.ALWAYS(
        ['this', 'is', 'tuple'])
    assert Exclude

# Generated at 2022-06-13 19:15:54.323346
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(True), "Always false"
    assert Exclude.NEVER(False), "Always false"
    assert Exclude.NEVER(2), "Always false"
    assert Exclude.NEVER(""), "Always false"
    assert Exclude.NEVER("foo"), "Always false"
    assert Exclude.NEVER([]), "Always false"
    assert Exclude.NEVER([1,2]), "Always false"
    assert Exclude.NEVER(()), "Always false"
    assert Exclude.NEVER((1,2)), "Always false"


# Generated at 2022-06-13 19:16:00.236078
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(0) == True
    assert Exclude.ALWAYS(1) == True
    assert Exclude.ALWAYS(1.0) == True
    assert Exclude.ALWAYS(-1) == True
    assert Exclude.ALWAYS(-1.0) == True
    assert Exclude.ALWAYS('hello') == True
    assert Exclude.ALWAYS('') == True
    assert Exclude.ALWAYS((0,)) == True
    assert Exclude.ALWAYS([0]) == True


# Generated at 2022-06-13 19:16:23.994759
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    test_class = Exclude()
    result = test_class.NEVER(123)
    if result == False:
        print("test method NEVER of class Exclude succeed!")
    else:
        print("test method NEVER of class Exclude failed!")

# Generated at 2022-06-13 19:16:36.673787
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert NEVER(1) == False
    assert NEVER('') == False
    assert NEVER('a') == False
    assert NEVER(0) == False
    assert NEVER(True) == False
    assert NEVER(False) == False
    assert NEVER(None) == False



# Generated at 2022-06-13 19:16:38.117459
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True



# Generated at 2022-06-13 19:16:41.364689
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True
    assert Exclude.ALWAYS(False) == True
    assert Exclude.ALWAYS(True) == True
    assert Exclude.ALWAYS("") == True


# Generated at 2022-06-13 19:16:42.212696
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("")


# Generated at 2022-06-13 19:16:43.637230
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS({})
    assert Exclude.ALWAYS("")


# Generated at 2022-06-13 19:16:45.554697
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    always= False
    never = True
    if always:
        return True
    if never:
        return False
    else:
        return False


# Generated at 2022-06-13 19:16:47.499119
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(True) is False


# Generated at 2022-06-13 19:16:50.146878
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS('test')


# Generated at 2022-06-13 19:16:52.515896
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True


# Generated at 2022-06-13 19:17:34.857860
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    """
    this function test that Exclude.ALWAYS is a function
    """
    res = Exclude.ALWAYS((1,2))
    assert res is True
    assert callable(Exclude.ALWAYS)


# Generated at 2022-06-13 19:17:43.285798
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER('hi') == False

# Generated at 2022-06-13 19:17:46.783920
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    obj = Exclude()
    assert obj.ALWAYS(1) == True
    assert obj.ALWAYS('abc') == True


# Generated at 2022-06-13 19:17:47.531962
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True


# Generated at 2022-06-13 19:17:48.988473
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("foo") == True


# Generated at 2022-06-13 19:17:50.216965
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(None) == False


# Generated at 2022-06-13 19:17:52.542634
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    for i in range(0, 5):
        assert NEVER(i) == False

test_Exclude_NEVER()

# Generated at 2022-06-13 19:17:53.962930
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("abc") == False


# Generated at 2022-06-13 19:17:57.026669
# Unit test for function config
def test_config():
    dct = {'dataclasses_json': {}}
    dc = lambda s: s[0].upper() + s[1:]

    config(dct,
           letter_case=dc,
           exclude='always',
           )
    assert dct == {'dataclasses_json': {
        'letter_case': dc,
        'exclude': Exclude.ALWAYS,
        'undefined': Undefined.EXCLUDE,
        }}

# Generated at 2022-06-13 19:17:58.662533
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    result = Exclude.NEVER("test")
    assert result == False


# Generated at 2022-06-13 19:19:30.209231
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None) == True


# Generated at 2022-06-13 19:19:31.968284
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER


# Generated at 2022-06-13 19:19:33.118800
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(True)
    assert not Exclude.ALWAYS(False)


# Generated at 2022-06-13 19:19:35.115451
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    call_result = Exclude.NEVER(5)
    assert call_result == False
    

# Generated at 2022-06-13 19:19:39.696530
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS(2)
    assert Exclude.ALWAYS(1.2)
    assert Exclude.ALWAYS(3.3)
    assert Exclude.ALWAYS(0)
    assert Exclude.ALWAYS(0.1)
