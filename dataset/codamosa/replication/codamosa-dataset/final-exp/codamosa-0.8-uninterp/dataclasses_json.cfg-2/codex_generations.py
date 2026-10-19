

# Generated at 2022-06-13 19:09:48.532522
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(None) is False
    assert Exclude.NEVER("abc") is False
    assert Exclude.NEVER(1) is False
    assert Exclude.NEVER(1.0) is False
    assert Exclude.NEVER([]) is False


# Generated at 2022-06-13 19:09:50.577182
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    test = Exclude.NEVER
    assert test(10) is False

# Generated at 2022-06-13 19:09:52.160149
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False


# Generated at 2022-06-13 19:09:55.885560
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    @dataclass
    class Foo:
        foo: str
        bar: int

    foo = Foo("hello", 50)

    assert Exclude.NEVER("foo") is True
    assert Exclude.NEVER("bar") is True

# Generated at 2022-06-13 19:10:02.118598
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None) == True
    assert Exclude.ALWAYS(0) == True
    assert Exclude.ALWAYS(4) == True
    assert Exclude.ALWAYS("") == True
    assert Exclude.ALWAYS("any_string") == True
    assert Exclude.ALWAYS(True) == True
    assert Exclude.ALWAYS(False) == True
    assert Exclude.ALWAYS(1.0) == True
    assert Exclude.ALWAYS(10000.99) == True


# Generated at 2022-06-13 19:10:02.687485
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert 1 == 1


# Generated at 2022-06-13 19:10:05.312743
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(True)
    assert Exclude.NEVER(False)


# Generated at 2022-06-13 19:10:07.229642
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True


# Generated at 2022-06-13 19:10:13.791358
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("a")
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS(None)
    assert Exclude.ALWAYS("abc")
    assert Exclude.ALWAYS("abc"), "unit test for method Exclude.ALWAYS() failed"


# Generated at 2022-06-13 19:10:19.449182
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    # A list and that is not empty
    assert Exclude.NEVER(['test'])

    # A string
    assert Exclude.NEVER("test")

    # A number
    assert Exclude.NEVER(1)

    # A boolean
    assert Exclude.NEVER(True)

    # An object
    assert Exclude.NEVER(object())

# Generated at 2022-06-13 19:10:21.998768
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True

# Generated at 2022-06-13 19:10:24.771082
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    value1 = True 
    value2 = False
    assert (Exclude.NEVER(value1) == False)
    assert (Exclude.NEVER(value2) == False)

# Generated at 2022-06-13 19:10:26.831306
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    a = Exclude.ALWAYS(0)
    b = Exclude.NEVER(0)

    print(a)
    print(b)

test_Exclude_NEVER()

# Generated at 2022-06-13 19:10:28.790845
# Unit test for method NEVER of class Exclude

# Generated at 2022-06-13 19:10:29.690021
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(object()) == False


# Generated at 2022-06-13 19:10:36.599047
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(0) == True
    assert Exclude.ALWAYS(False) == True
    assert Exclude.ALWAYS(0.0) == True
    assert Exclude.ALWAYS(None) == True
    assert Exclude.ALWAYS("") == True
    assert Exclude.ALWAYS([]) == True
    assert Exclude.ALWAYS(()) == True
    assert Exclude.ALWAYS({}) == True


# Generated at 2022-06-13 19:10:37.852009
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    ex = Exclude()
    assert(ex.NEVER("anything") == False)

# Generated at 2022-06-13 19:10:49.631223
# Unit test for function config
def test_config():
    def test_config_impl(msg: str, cfg: dict):
        assert msg.replace('-', '_') in cfg
        assert cfg[msg.replace('-', '_')] == msg

    for key in ('mm_field', 'encoder', 'decoder', 'undefined'):
        msg = f'{key}-msg'
        expected = {'dataclasses_json': {key: msg}}
        cfg = config(metadata=None, **{key: msg})
        assert cfg == expected

    msg = 'exclude-msg'
    expected = {'dataclasses_json': {'exclude': msg}}
    cfg = config(metadata=None, exclude=msg)
    assert cfg == expected

    # Test overridden letter_case
    msg = 'field-name-msg'
   

# Generated at 2022-06-13 19:10:50.756830
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True


# Generated at 2022-06-13 19:10:53.026894
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    # Arrange
    x = Exclude.NEVER(15)
    expected_x = False

    # Act

    # Assert
    assert x == expected_x
    print('Exclude.NEVER works')


# Generated at 2022-06-13 19:10:56.279971
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("var") == False

# Generated at 2022-06-13 19:10:56.859106
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert(Exclude.NEVER(1) == False)

# Generated at 2022-06-13 19:11:03.127938
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS(True)
    assert Exclude.ALWAYS('a')
    assert Exclude.ALWAYS([1,2,3])
    assert Exclude.ALWAYS(None)


# Generated at 2022-06-13 19:11:08.309720
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    #Create a class
    class Person:
        #Initalization function
        def __init__(self, name):
            self.name = name
    #Create an instance for the class
    person = Person('John')
    #Call the method NEVER of the class Exclude and assign the returned value to the variable result
    result = Exclude.NEVER(person.name)
    #Assert to confirm the value returned by Exclude.NEVER() method
    assert result == False

# Generated at 2022-06-13 19:11:10.052393
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("blah")

if __name__ == "__main__":
    test_Exclude_NEVER()

# Generated at 2022-06-13 19:11:11.513023
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    result = Exclude.NEVER("test")
    assert result == False

# Generated at 2022-06-13 19:11:12.971772
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(False)
    assert Exclude.ALWAYS(True)
    assert Exclude.ALWAYS(None)

# Generated at 2022-06-13 19:11:15.689683
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("random_string")


# Generated at 2022-06-13 19:11:20.273347
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    class A:
        def __init__(self):
            self.attribute = True
        def __str__(self):
            return "A Object"
    a = A()
    assert Exclude.NEVER(a), 'Exclude.NEVER callable failed in config.py'


# Generated at 2022-06-13 19:11:22.601653
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    # Arrange
    # Act
    # Assert
    assert Exclude.NEVER('hello') == False


# Generated at 2022-06-13 19:11:27.287182
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False

# Generated at 2022-06-13 19:11:35.573191
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(0) == True
    assert Exclude.ALWAYS(1) == True
    assert Exclude.ALWAYS(2) == True
    assert Exclude.ALWAYS(3) == True
    assert Exclude.ALWAYS(4) == True
    assert Exclude.ALWAYS(5) == True
    assert Exclude.ALWAYS(6) == True
    assert Exclude.ALWAYS(7) == True
    assert Exclude.ALWAYS(8) == True
    assert Exclude.ALWAYS(9) == True
    assert Exclude.ALWAYS(10) == True
    assert Exclude.ALWAYS(11) == True
    assert Exclude.ALWAYS(12) == True
    assert Exclude.ALWAYS(13) == True
    assert Exclude.ALWAYS(14) == True
    assert Exclude

# Generated at 2022-06-13 19:11:36.869771
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True
    assert Exclude.ALWAYS("test") == True


# Generated at 2022-06-13 19:11:37.779465
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False


# Generated at 2022-06-13 19:11:42.628420
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    Ex = Exclude.NEVER
    assert Ex(1) == False
    assert Ex(0) == False
    assert Ex(True) == False
    assert Ex(False) == False
    assert Ex(None) == False



# Generated at 2022-06-13 19:11:44.871910
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
	ex = Exclude.ALWAYS
	if ex(5) != True:
		return False
	if ex(2.0) != True:
		return False
	if ex('hi') != True:
		return False
	return True	


# Generated at 2022-06-13 19:11:46.330739
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    field = "name"
    res = Exclude.NEVER(field)
    assert res == False


# Generated at 2022-06-13 19:11:48.664641
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    test_obj = Exclude()
    res = test_obj.NEVER(3)
    assert res == False


# Generated at 2022-06-13 19:11:50.013812
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS

# Generated at 2022-06-13 19:11:52.029799
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS({}) == True



# Generated at 2022-06-13 19:12:00.988980
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None)


# Generated at 2022-06-13 19:12:01.672548
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    x = Exclude.NEVER(1)
    assert x == False


# Generated at 2022-06-13 19:12:02.463901
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("T")

# Generated at 2022-06-13 19:12:08.879084
# Unit test for function config
def test_config():
    from marshmallow import Schema, fields

    # Function decorator
    @config(field_name='my_field',
            letter_case=lambda s: s.upper(),
            mm_field=fields.Integer(),
            undefined=Undefined.RAISE)
    @dataclass
    class MyClass:
        a: int

    field_entry = MyClass.__dataclass_fields__['a']
    assert field_entry['field_name'] == 'my_field'
    assert field_entry['letter_case']('') == 'MY_FIELD'
    assert isinstance(field_entry['mm_field'], fields.Integer)
    assert field_entry['undefined'] is Undefined.RAISE

    # Pre-defined constant

# Generated at 2022-06-13 19:12:10.804131
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None) == True, "Error on method ALWAYS of class Exclude"


# Generated at 2022-06-13 19:12:12.444108
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
	assert Exclude.NEVER(True) == False


# Generated at 2022-06-13 19:12:14.520679
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(0) == False


# Generated at 2022-06-13 19:12:16.117716
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    NEVER = Exclude.NEVER
    assert NEVER(2) == False



# Generated at 2022-06-13 19:12:18.116302
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    obj = {}
    assert Exclude.NEVER(obj) == False


# Generated at 2022-06-13 19:12:25.410640
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    from dataclasses import dataclass
    from typing import Callable
    @dataclass
    class Foo:
        bar: str

    @dataclass
    class Foo1:
        bar1:str

    @dataclass
    class Foo2:
        bar2:str

    @dataclass
    class Bar:
        foo: Foo
        foo1: Foo1
        foo2: Foo2

    assert not Exclude.NEVER(Bar,"foo")
    assert not Exclude.NEVER(Bar, "foo1")
    assert not Exclude.NEVER(Bar, "foo2")
    assert not Exclude.NEVER(Foo, "bar")
    assert not Exclude.NEVER(Foo1, "bar1")
    assert not Exclude.NEVER(Foo2, "bar2")

# Generated at 2022-06-13 19:12:57.444671
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS(None)
    assert Exclude.ALWAYS(True)
    assert Exclude.ALWAYS('')
    assert Exclude.ALWAYS('abc')


# Generated at 2022-06-13 19:12:59.451003
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
   assert Exclude.NEVER(True) == False
   assert Exclude.NEVER(False) == False


# Generated at 2022-06-13 19:13:01.187450
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    test_input = []
    assert Exclude.ALWAYS(test_input) == True


# Generated at 2022-06-13 19:13:19.670443
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None)
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS(2.3)
    assert Exclude.ALWAYS(True)
    assert Exclude.ALWAYS(False)
    assert Exclude.ALWAYS('foo')
    assert Exclude.ALWAYS(['foo', 'bar'])
    assert Exclude.ALWAYS({'foo': 1, 'bar': 2})
    assert Exclude.ALWAYS(set([1, 2]))
    assert Exclude.ALWAYS(frozenset([1, 2]))
    assert Exclude.ALWAYS({'foo': 1}.keys())
    assert Exclude.ALWAYS({'foo': 1}.items())
    assert Exclude.ALWAYS(range(1, 4))

# Generated at 2022-06-13 19:13:21.906716
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) is True


# Generated at 2022-06-13 19:13:23.864945
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True
    

# Generated at 2022-06-13 19:13:25.606509
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(3) == False


# Generated at 2022-06-13 19:13:32.879395
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(True) == False
    assert Exclude.NEVER("a") == False
    assert Exclude.NEVER(1) == False
    assert Exclude.NEVER(1.0) == False
    assert Exclude.NEVER(None) == False
    assert Exclude.NEVER(object()) == False
    assert Exclude.NEVER([1]) == False
    assert Exclude.NEVER(("a",)) == False


# Generated at 2022-06-13 19:13:33.648313
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(True)



# Generated at 2022-06-13 19:13:34.797206
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(Exclude.NEVER)

# Generated at 2022-06-13 19:14:18.992316
# Unit test for function config
def test_config():
    from dataclasses import dataclass, field
    from dataclasses_json import DataClassJsonMixin

    @dataclass
    class Foo(DataClassJsonMixin):
        a: int = field(metadata=config(exclude=Exclude.ALWAYS))

    assert not Foo(12345)._config.include('a')

# Generated at 2022-06-13 19:14:21.987529
# Unit test for function config
def test_config():
    config(undefined=Undefined.EXCLUDE)
    config(undefined="exclude")
    config(undefined="raise")

# Generated at 2022-06-13 19:14:23.716915
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    class TestClass:
        pass
    test_class = TestClass()
    assert(Exclude.NEVER(test_class))

# Generated at 2022-06-13 19:14:24.991502
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None) is True


# Generated at 2022-06-13 19:14:26.072046
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False


# Generated at 2022-06-13 19:14:27.097897
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(3) == True


# Generated at 2022-06-13 19:14:34.680295
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    object = Exclude()
    list_field_name = ['lenght', 'price', 'number_of_reads']
    
    # Test with two field names that are not excluded
    result = object.NEVER(list_field_name[0])
    assert result == False
    # Test with field name that is not exluded
    result = object.NEVER(list_field_name[1])
    assert result == False
    # Test with field name that is not exluded
    result = object.NEVER(list_field_name[2])
    assert result == False

# Generated at 2022-06-13 19:14:38.252043
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert (Exclude.ALWAYS(123) == True)
    assert (Exclude.ALWAYS(True) == True)
    assert (Exclude.ALWAYS(None) == True)
    assert (Exclude.ALWAYS("") == True)


# Generated at 2022-06-13 19:14:43.187950
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
  assert Exclude.NEVER('a')
  assert Exclude.NEVER(1)
  assert Exclude.NEVER(False)
  assert Exclude.NEVER(True)
  assert Exclude.NEVER(None)
  assert Exclude.NEVER('')


# Generated at 2022-06-13 19:14:45.548582
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(0) == True
    assert Exclude.ALWAYS(5) == True
    assert Exclude.ALWAYS('var') == True


# Generated at 2022-06-13 19:16:24.270055
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS(True)
    assert Exclude.ALWAYS(None)
    assert Exclude.ALWAYS(object)


# Generated at 2022-06-13 19:16:32.768041
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True



# Generated at 2022-06-13 19:16:36.475497
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    print("Unit test for method NEVER of class Exclude")
    assert(Exclude.NEVER(1) == False)
    print("Passed.")

# Generated at 2022-06-13 19:16:38.477527
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    test = Exclude.ALWAYS
    assert isinstance(test, Callable)



# Generated at 2022-06-13 19:16:40.646868
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(0) == False
    assert Exclude.NEVER(1) == False
    assert Exclude.NEVER(7) == False

# Generated at 2022-06-13 19:16:41.874465
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True


# Generated at 2022-06-13 19:16:45.619283
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(0) is True
    assert Exclude.ALWAYS(1) is True
    assert Exclude.ALWAYS(100) is True
    assert Exclude.ALWAYS("hello") is True
    assert Exclude.ALWAYS("") is True
    assert Exclude.ALWAYS(True) is True
    assert Exclude.ALWAYS(False) is True


# Generated at 2022-06-13 19:16:48.797726
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS(True)

# Generated at 2022-06-13 19:16:51.497517
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    instance = Exclude()
    assert instance.NEVER('') == False
    assert instance.NEVER(2) == False


# Generated at 2022-06-13 19:16:53.265773
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(None) == False  # True