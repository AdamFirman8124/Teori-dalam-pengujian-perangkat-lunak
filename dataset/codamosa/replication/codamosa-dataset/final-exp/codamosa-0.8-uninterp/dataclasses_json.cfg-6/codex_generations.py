

# Generated at 2022-06-13 19:09:43.544763
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    print(Exclude.NEVER('a'))

# Generated at 2022-06-13 19:09:54.102061
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    import dataclasses
    from typing import List
    from dataclasses_json.config import config, Exclude

    @config(exclude=Exclude.NEVER)
    @dataclasses.dataclass
    class Test:
        name: str
        age: int

    obj = Test("test_name", 100)
    # obj.name = "test_name"
    # obj.age = 100
    # from dataclasses_json import dump, load
    # data_json = dump(obj)
    # print("data_json = ", data_json)
    # data = load(data_json, Test)
    # print("data = ", data)


# Generated at 2022-06-13 19:09:57.693514
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(Exclude.ALWAYS)
    assert Exclude.ALWAYS(Exclude.NEVER)
    assert Exclude.ALWAYS(True)
    assert Exclude.ALWAYS(False)


# Generated at 2022-06-13 19:10:00.369875
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS(2)
    assert Exclude.ALWAYS(None)
    assert Exclude.ALWAYS('a')


# Generated at 2022-06-13 19:10:02.751339
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    x = Exclude()
    print(x.NEVER)
    print(Exclude.NEVER)


# Generated at 2022-06-13 19:10:05.737863
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("")
    assert Exclude.ALWAYS("a")
    assert Exclude.ALWAYS("xy")
    assert Exclude.ALWAYS("012")


# Generated at 2022-06-13 19:10:06.861676
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("") == False


# Generated at 2022-06-13 19:10:09.470873
# Unit test for method ALWAYS of class Exclude

# Generated at 2022-06-13 19:10:16.408900
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    from src.dataclasses_json_utils import config
    from dataclasses import dataclass

    @dataclass
    class A:
        x: int = 3

    @config(exclude=Exclude.NEVER)
    class A:
        x: int = 3

    assert A(3).x == 3



# Generated at 2022-06-13 19:10:17.625880
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1)

# Generated at 2022-06-13 19:10:21.041639
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None) == True


# Generated at 2022-06-13 19:10:28.377044
# Unit test for function config
def test_config():
    from marshmallow import fields

    # Use new function
    @config(exclude=Exclude.ALWAYS)  # type: ignore
    class CustomConfig:
        pass

    assert CustomConfig.__dataclasses_json__ == {
        'dataclasses_json': {
            'exclude': Exclude.ALWAYS
        }
    }

    # Use legacy method
    @config(mm_field=fields.String)  # type: ignore
    class LegacyConfig:
        pass

    assert LegacyConfig.__dataclasses_json__ == {
        'dataclasses_json': {
            'mm_field': fields.String
        }
    }

# Generated at 2022-06-13 19:10:29.985021
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("a string") == False


# Generated at 2022-06-13 19:10:34.228369
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(0)
    assert Exclude.ALWAYS('hello')
    assert Exclude.ALWAYS([1, 2, 3])
    assert Exclude.ALWAYS(('a', 'b', 'c'))


# Generated at 2022-06-13 19:10:35.762945
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    obj = object()
    assert Exclude.ALWAYS(obj)



# Generated at 2022-06-13 19:10:37.549808
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    include = False
    assert(Exclude.NEVER(include) == False)


# Generated at 2022-06-13 19:10:38.890965
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None) is True


# Generated at 2022-06-13 19:10:41.067205
# Unit test for method ALWAYS of class Exclude

# Generated at 2022-06-13 19:10:47.745855
# Unit test for function config
def test_config():
    from dataclasses import dataclass, field
    from dataclasses_json import config
    @dataclass
    class User:
        name: str = field(metadata={config(field_name="name")})
        gender: str = field(metadata={config(letter_case="upper")})
    gender = "male"
    user = User(gender)
    assert user.gender == "MALE"
    assert user.name == "name"

# Generated at 2022-06-13 19:10:50.322868
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True
    assert Exclude.ALWAYS('abc') == True
    assert Exclude.ALWAYS(['a']) == True


# Generated at 2022-06-13 19:10:53.931864
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    e1 = Exclude()
    assert e1.NEVER('') == False


# Unit test method ALWAYS of class Exclude

# Generated at 2022-06-13 19:10:54.794626
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False and Exclude.NEVER(0) == False

# Generated at 2022-06-13 19:11:08.612323
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(True) is True
    assert Exclude.ALWAYS(False) is True
    assert Exclude.ALWAYS(None) is True
    assert Exclude.ALWAYS(1) is True
    assert Exclude.ALWAYS(0) is True
    assert Exclude.ALWAYS(-1) is True
    assert Exclude.ALWAYS(object()) is True
    assert Exclude.ALWAYS("") is True
    assert Exclude.ALWAYS("a") is True
    assert Exclude.ALWAYS(()) is True
    assert Exclude.ALWAYS([]) is True
    assert Exclude.ALWAYS({}) is True


# Generated at 2022-06-13 19:11:09.789378
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    obj=Exclude
    assert obj.NEVER('1') == False


# Generated at 2022-06-13 19:11:11.658295
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    def f(_):
        return True
    assert Exclude.ALWAYS == f


# Generated at 2022-06-13 19:11:13.280514
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS is not None

# Generated at 2022-06-13 19:11:15.862558
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None) == True


# Generated at 2022-06-13 19:11:22.484554
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(True) is False
    assert Exclude.NEVER(False) is False
    assert Exclude.NEVER(1) is False
    assert Exclude.NEVER(0) is False
    assert Exclude.NEVER(1.5) is False
    assert Exclude.NEVER(0.0) is False
    assert Exclude.NEVER("foo") is False
    assert Exclude.NEVER("") is False
    assert Exclude.NEVER("bar") is False
    assert Exclude.NEVER("0") is False
    assert Exclude.NEVER("1") is False


# Generated at 2022-06-13 19:11:28.316553
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(4) == True
    assert Exclude.ALWAYS("4") == True
    assert Exclude.ALWAYS(4.0) == True
    assert Exclude.ALWAYS(["1","2","3"]) == True
    assert Exclude.ALWAYS({"a":1,"b":2}) == True


# Generated at 2022-06-13 19:11:29.634650
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    exclude = Exclude()
    assert exclude.ALWAYS('a') == True
    return True


# Generated at 2022-06-13 19:11:34.970476
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert(Exclude.NEVER('abc') == False)


# Generated at 2022-06-13 19:11:35.754947
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(0)

# Generated at 2022-06-13 19:11:36.490793
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("") == False


# Generated at 2022-06-13 19:11:37.494163
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("foo") is True


# Generated at 2022-06-13 19:11:41.313110
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("foo")
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS(True)
    assert Exclude.ALWAYS(None)
    assert Exclude.ALWAYS(object)
    assert Exclude.ALWAYS(())


# Generated at 2022-06-13 19:11:43.477770
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None) == True
    print("Exclude_ALWAYS test passed!")


# Generated at 2022-06-13 19:11:44.804315
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None) == True


# Generated at 2022-06-13 19:11:46.139381
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
        field='marshmellow'
        return Exclude.NEVER(field)
# Case 1
print(test_Exclude_NEVER())


# Generated at 2022-06-13 19:11:49.811331
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    obj = Exclude()
    assert obj.NEVER(1) == False
    assert obj.NEVER('a') == False
    assert obj.NEVER([1,2]) == False
    assert obj.NEVER(['a','b']) == False

# Generated at 2022-06-13 19:11:51.844201
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(True) == False


# Generated at 2022-06-13 19:12:11.702720
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(2)
    assert Exclude.ALWAYS(0)
    assert Exclude.ALWAYS(-2)
    assert Exclude.ALWAYS(1.1)
    assert Exclude.ALWAYS(-1.1)
    assert Exclude.ALWAYS(0.0)
    assert Exclude.ALWAYS(-0.0)
    assert Exclude.ALWAYS(False)
    assert Exclude.ALWAYS(True)
    assert Exclude.ALWAYS("")
    assert Exclude.ALWAYS("test-string")
    assert Exclude.ALWAYS(["test"])
    assert Exclude.ALWAYS((0, 1))
    assert Exclude.ALWAYS({"test": 2})
    assert Exclude.ALWAYS(None)
    assert Exclude.ALWAYS(object())


# Generated at 2022-06-13 19:12:13.284739
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(None)


# Generated at 2022-06-13 19:12:15.415560
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(3) == True


# Generated at 2022-06-13 19:12:20.821214
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    print("Testing method ALWAYS of class Exclude")
    my_exclude=Exclude()
    if(my_exclude.ALWAYS("hello")):
        print("Test passed")
    else:
        print("Test failed")
    if(not my_exclude.ALWAYS("world")):
        print("Test passed")
    else:
        print("Test failed")


# Generated at 2022-06-13 19:12:29.325413
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    # Arrange    
    from dataclasses import dataclass, field

    @dataclass
    class Person:
        name: str = field(metadata=config(exclude=Exclude.NEVER))
        age: int = field(metadata=config(exclude=Exclude.NEVER))
        weight: float = field(metadata=config(exclude=Exclude.NEVER))
    
    # Act
    person = Person('Foo', 20, 80.0)
    # Assert
    assert is_dataclass(person)



# Generated at 2022-06-13 19:12:30.776198
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True


# Generated at 2022-06-13 19:12:31.997984
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert callable(Exclude.NEVER)
    assert Exclude.NEVER("")

# Generated at 2022-06-13 19:12:33.508510
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER('hi') == False


# Generated at 2022-06-13 19:12:39.152927
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS('a')
    assert Exclude.ALWAYS(True)
    assert Exclude.ALWAYS([1, 2, 3])
    assert Exclude.ALWAYS({1, 2, 3})
    assert Exclude.ALWAYS(())
    assert Exclude.ALWAYS({})


# Generated at 2022-06-13 19:12:39.939861
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("asdf")


# Generated at 2022-06-13 19:13:01.111099
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    # Arrange
    test_var = 1
    expected = False
    
    # Act
    result = Exclude.NEVER(test_var)

    # Assert
    assert result == expected


# Generated at 2022-06-13 19:13:12.480824
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False
    print('Done')

if __name__ == '__main__':
    test_Exclude_NEVER()

# Generated at 2022-06-13 19:13:19.788546
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True
    assert Exclude.ALWAYS(0.01) == True
    assert Exclude.ALWAYS("Alfa Bravo Charlie") == True
    assert Exclude.ALWAYS("") == True
    assert Exclude.ALWAYS([]) == True
    assert Exclude.ALWAYS([1,2,3]) == True
    assert Exclude.ALWAYS((1,2,3)) == True
    assert Exclude.ALWAYS({}) == True
    assert Exclude.ALWAYS({"Alfa":1,"Bravo":2,"Charlie":3}) == True


# Generated at 2022-06-13 19:13:20.915667
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("a") == False


# Generated at 2022-06-13 19:13:22.998249
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert not Exclude.NEVER(None)


# Generated at 2022-06-13 19:13:26.722995
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    # Given
    instance = Exclude.ALWAYS
    parameter = "any"

    # When
    result = instance(parameter)

    # Then
    assert result is True


# Generated at 2022-06-13 19:13:28.423906
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER('a') == False


# Generated at 2022-06-13 19:13:32.558170
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert(Exclude.ALWAYS(0))
    assert(Exclude.ALWAYS(3.14))
    assert(Exclude.ALWAYS("any string"))


# Generated at 2022-06-13 19:13:35.149264
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS('')
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS(True)


# Generated at 2022-06-13 19:13:35.915908
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER('a') == False


# Generated at 2022-06-13 19:14:15.214684
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("a") == False


# Generated at 2022-06-13 19:14:17.152926
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(0) == True



# Generated at 2022-06-13 19:14:18.633215
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None) == True


# Generated at 2022-06-13 19:14:22.024825
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS([])
    assert Exclude.ALWAYS('test')
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS(print)
    assert Exclude.ALWAYS(Exclude.ALWAYS)
    assert Exclude.ALWAYS(Exclude.NEVER)


# Generated at 2022-06-13 19:14:22.987005
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None)

test_Exclude_ALWAYS()

# Generated at 2022-06-13 19:14:23.827626
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    a=Exclude().NEVER
    assert a(0)

# Generated at 2022-06-13 19:14:30.087071
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(0)
    assert Exclude.ALWAYS(None)
    assert Exclude.ALWAYS(1.0)
    assert Exclude.ALWAYS(True)
    assert Exclude.ALWAYS(False)
    assert Exclude.ALWAYS("abc")
    assert Exclude.ALWAYS(Exclude.ALWAYS)
    assert Exclude.ALWAYS(Exclude.NEVER)
    assert Exclude.ALWAYS([1, 2, 3])
    assert Exclude.ALWAYS(())
    assert Exclude.ALWAYS({1, 2, 3})
    assert Exclude.ALWAYS({})
    assert Exclude.ALWAYS({1: 2})


# Generated at 2022-06-13 19:14:30.831331
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True

# Generated at 2022-06-13 19:14:31.867262
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER((1, 2, 3)) == False

# Generated at 2022-06-13 19:14:32.838453
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
	assert Exclude.ALWAYS(_) == True


# Generated at 2022-06-13 19:16:10.144031
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():          
    assert(Exclude.ALWAYS(4))

# Generated at 2022-06-13 19:16:11.017535
# Unit test for method ALWAYS of class Exclude

# Generated at 2022-06-13 19:16:12.113303
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    """
    Test that always returns true
    """
    assert Exclude.ALWAYS(1) == True


# Generated at 2022-06-13 19:16:13.404640
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert functools.reduce(lambda x, y: x or y, map(Exclude.NEVER, range(100))) == False


# Generated at 2022-06-13 19:16:14.514720
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS('')


# Generated at 2022-06-13 19:16:17.270896
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False


# Generated at 2022-06-13 19:16:27.920859
# Unit test for function config
def test_config():
    from dataclasses import dataclass

    @config()
    @dataclass
    class DefaultConfig:
        foo: str = 'bar'
        baz: str = 'boo'

    assert isinstance(DefaultConfig.__dataclasses_json__, dict)
    assert len(DefaultConfig.__dataclasses_json__) == 0

    @config(encoder=str)
    @dataclass
    class StringEncoder:
        foo: str = 'bar'
        baz: str = 'boo'

    assert isinstance(StringEncoder.__dataclasses_json__, dict)
    assert StringEncoder.__dataclasses_json__['encoder'] == str


# Generated at 2022-06-13 19:16:30.996105
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(Exclude) == False
    assert Exclude.NEVER("") == False
    assert Exclude.NEVER("_") == False
    assert Exclude.NEVER("function") == False


# Generated at 2022-06-13 19:16:33.070919
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    answer = Exclude.ALWAYS(0)
    assert answer == True


# Generated at 2022-06-13 19:16:35.084686
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None)
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS(True)
    assert Exclude.ALWAYS('abc')
