

# Generated at 2022-06-13 19:09:43.496987
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    a = Exclude.ALWAYS(1)
    assert a == True


# Generated at 2022-06-13 19:09:50.874318
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None)
    assert Exclude.ALWAYS(True)
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS(1.0)
    assert Exclude.ALWAYS('str')
    assert Exclude.ALWAYS(())
    assert Exclude.ALWAYS(list())
    assert Exclude.ALWAYS(dict())

# Unit-test for method NEVER of class Exclude

# Generated at 2022-06-13 19:09:53.648034
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    eq_(True,Exclude.ALWAYS(1234))


# Generated at 2022-06-13 19:09:55.703228
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(5) == False


# Generated at 2022-06-13 19:09:57.628329
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1)


# Generated at 2022-06-13 19:10:00.037139
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(2) == True and Exclude.ALWAYS("str") == True and Exclude.ALWAYS(3.14) == True


# Generated at 2022-06-13 19:10:09.921226
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("1") == False
    assert Exclude.NEVER("2") == False


# Generated at 2022-06-13 19:10:11.759868
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("a string") == False



# Generated at 2022-06-13 19:10:14.175044
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False

if __name__ == "__main__":
    test_Exclude_NEVER()

# Generated at 2022-06-13 19:10:15.093948
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS('test')  == True


# Generated at 2022-06-13 19:10:19.488492
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(123) is True
    assert Exclude.ALWAYS('abc') is True
    assert Exclude.ALWAYS(True) is True

# Generated at 2022-06-13 19:10:21.246081
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    test_input = 'test'
    assert Exclude.NEVER(test_input) == False


# Generated at 2022-06-13 19:10:22.510262
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    print(Exclude.NEVER(1))


# Generated at 2022-06-13 19:10:23.683954
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS('dummy') == True


# Generated at 2022-06-13 19:10:25.067814
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True, "Exclude.ALWAYS has failed"


# Generated at 2022-06-13 19:10:26.284548
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(0) == True


# Generated at 2022-06-13 19:10:28.460576
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    dummy = 123
    assert Exclude.ALWAYS(dummy) == True

# Generated at 2022-06-13 19:10:30.033062
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("") == False


# Generated at 2022-06-13 19:10:30.967242
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(False) == True
    assert Exclude.ALWAYS(True) == True


# Generated at 2022-06-13 19:10:31.667019
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    x = Exclude.ALWAYS(6)
    assert x is True


# Generated at 2022-06-13 19:10:43.838596
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None)
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS(1.0)
    assert Exclude.ALWAYS('abc')
    assert Exclude.ALWAYS(True)
    assert Exclude.ALWAYS([])
    assert Exclude.ALWAYS(set())
    assert Exclude.ALWAYS(tuple())
    assert Exclude.ALWAYS(range(1))
    assert Exclude.ALWAYS(range(1, 2))
    assert Exclude.ALWAYS(range(1, 2, 3))
    assert Exclude.ALWAYS({})
    assert Exclude.ALWAYS({'abc': 1})
    assert Exclude.ALWAYS(Exclude)


# Generated at 2022-06-13 19:10:45.477216
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None) == True


# Generated at 2022-06-13 19:10:46.791613
# Unit test for function config
def test_config():
    pass

# Generated at 2022-06-13 19:10:53.093988
# Unit test for function config
def test_config():
    from dataclasses import dataclass

    @dataclass
    class A:
        def __init__(self):
            pass

    assert A.__annotations__ == {}
    assert A.__dataclass_fields__ == {
        'a': dataclasses.Field(init=False, repr=True, compare=True,
                               metadata={'dataclasses_json': {
                                   'undefined': Undefined.RAISE,
                                   'letter_case': 'snake'}})}

# Generated at 2022-06-13 19:10:54.155447
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    print(Exclude.ALWAYS)
    assert Exclude.ALWAYS(None) == True

# Generated at 2022-06-13 19:10:55.820719
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    test_value = 10
    
    if Exclude.NEVER(test_value):
        return True
    else:
        return False


# Generated at 2022-06-13 19:11:00.146257
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    '''
    If class Exclude's method ALWAYS is called, it should return True.
    '''
    assert Exclude.ALWAYS(0)


# Generated at 2022-06-13 19:11:04.362899
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    x = Exclude.ALWAYS
    assert(x(1) == True)
    assert(x(None) == True)
    assert(x(0) == True)


# Generated at 2022-06-13 19:11:06.544219
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    f = Exclude.ALWAYS

    assert f(1)
    assert f(True)
    assert f("")
    assert f(None)


# Generated at 2022-06-13 19:11:09.680280
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    print(Exclude.ALWAYS(True))
    print(Exclude.ALWAYS(False))

    print(Exclude.ALWAYS('1'))
    print(Exclude.ALWAYS(2))
    print(Exclude.ALWAYS(3.3))



# Generated at 2022-06-13 19:11:13.783509
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
  exclude = Exclude.NEVER
  assert exclude("test")


# Generated at 2022-06-13 19:11:21.939207
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS('a')
    assert Exclude.ALWAYS(True)
    assert Exclude.ALWAYS(False)
    assert Exclude.ALWAYS(()), 'empty tuple'
    assert Exclude.ALWAYS([]), 'empty list'
    assert Exclude.ALWAYS({}), 'empty dict'
    assert Exclude.ALWAYS(None)


# Generated at 2022-06-13 19:11:32.189080
# Unit test for function config
def test_config():
    from ..utils import FrozenOrderedDict
    from ..utils.utils import letter_case

    x = config(encoder=1, decoder=2, mm_field=3, field_name="abc",
               letter_case=letter_case.snake_case, undefined=Undefined.EXCLUDE)
    assert x == {"dataclasses_json":
                 {"encoder": 1, "decoder": 2, "mm_field": 3,
                  "letter_case": letter_case.snake_case,
                  "undefined": Undefined.EXCLUDE}}

    x = config(mm_field=3, letter_case=letter_case.snake_case,
               field_name="field1",
               exclude=lambda field, value: field == "field1")

# Generated at 2022-06-13 19:11:32.810751
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("")

# Generated at 2022-06-13 19:11:34.225357
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1)


# Generated at 2022-06-13 19:11:35.029468
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert config.Exclude.ALWAYS(2) == True


# Generated at 2022-06-13 19:11:36.387268
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True
    assert Exclude.ALWAYS('a') == True


# Generated at 2022-06-13 19:11:37.241941
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(True)


# Generated at 2022-06-13 19:11:37.929906
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(None) == False

# Generated at 2022-06-13 19:11:39.019375
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False

# Generated at 2022-06-13 19:11:45.314582
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    #Action
    callNEVER=Exclude.NEVER

    #Assert
    assert callNEVER(True)==False
    assert callNEVER(False)==False

# Generated at 2022-06-13 19:11:47.680990
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS("hi")
    assert Exclude.ALWAYS(Exclude.NEVER)
    assert Exclude.ALWAYS([1, 2, 3])


# Generated at 2022-06-13 19:11:49.268765
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False
    return True

# Generated at 2022-06-13 19:11:53.677764
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    c = config(exclude=Exclude.ALWAYS)

# Generated at 2022-06-13 19:11:54.974434
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS.__globals__['_']()

# Generated at 2022-06-13 19:11:56.449337
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None)



# Generated at 2022-06-13 19:11:57.987727
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1)==False


# Generated at 2022-06-13 19:11:59.396049
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(0) == True


# Generated at 2022-06-13 19:12:03.898356
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert (Exclude.NEVER(0) == True)
    assert (Exclude.NEVER(1) == True)
    assert (Exclude.NEVER(2) == True)
    assert (Exclude.NEVER(3) == True)
    assert (Exclude.NEVER(-1) == True)
    assert (Exclude.NEVER(3.14) == True)
    assert (Exclude.NEVER(3.1415) == True)
    assert (Exclude.NEVER('a') == True)
    assert (Exclude.NEVER('ab') == True)
    assert (Exclude.NEVER('') == True)
    assert (Exclude.NEVER(' ') == True)
    assert (Exclude.NEVER('123a') == True)

# Generated at 2022-06-13 19:12:05.188175
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("test") == True

test_Exclude_ALWAYS()


# Generated at 2022-06-13 19:12:15.093069
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
  assert Exclude.ALWAYS('a') == True


# Generated at 2022-06-13 19:12:16.911308
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS is not None
    assert Exclude.NEVER is not None

# Generated at 2022-06-13 19:12:18.166844
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) is False

# Generated at 2022-06-13 19:12:19.936383
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    result = Exclude.NEVER(1)
    expected = False
    assert result == expected
    

# Generated at 2022-06-13 19:12:21.317303
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(None) == False


# Generated at 2022-06-13 19:12:23.705473
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(5)
    assert Exclude.ALWAYS("Test")


# Generated at 2022-06-13 19:12:25.735129
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True
    assert Exclude.ALWAYS("a") == True


# Generated at 2022-06-13 19:12:33.444322
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(0)
    assert Exclude.NEVER(2)
    assert Exclude.NEVER(3)
    assert Exclude.NEVER(10)
    assert Exclude.NEVER(False)
    assert Exclude.NEVER(True)
    assert Exclude.NEVER(None)
    assert Exclude.NEVER("")
    assert Exclude.NEVER("Hello")
    assert Exclude.NEVER([""])
    assert Exclude.NEVER([])
    assert Exclude.NEVER([1])
    assert Exclude.NEVER({"a":1})



# Generated at 2022-06-13 19:12:35.859012
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None) == True
    assert Exclude.ALWAYS(not None) == True


# Generated at 2022-06-13 19:12:37.619720
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(True) == True


# Generated at 2022-06-13 19:12:58.485549
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert not Exclude.NEVER("anything")


# Generated at 2022-06-13 19:13:00.715457
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(0)

# Generated at 2022-06-13 19:13:13.478183
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    # Input
    test_input = "test"

    # Expected output
    exp_output = False

    # Actual output
    act_output = Exclude.NEVER(test_input)

    # Assertion
    assert exp_output == act_output

# Generated at 2022-06-13 19:13:16.286858
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER('1234')
    assert Exclude.NEVER(1234)
    assert Exclude.NEVER([1, 2, 3, 4])

# Generated at 2022-06-13 19:13:17.383095
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(None)

# Generated at 2022-06-13 19:13:21.514165
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    res1 = Exclude.ALWAYS(2)
    res2 = Exclude.ALWAYS(3)
    assert res1 == True and res2 == True


# Generated at 2022-06-13 19:13:24.478553
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS("a")
    assert Exclude.ALWAYS(None)



# Generated at 2022-06-13 19:13:27.219748
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    a = Exclude.NEVER
    assert a("test") == False

test_Exclude_NEVER()


# Generated at 2022-06-13 19:13:40.289369
# Unit test for function config
def test_config():
    from marshmallow import ValidationError

    from dataclasses import dataclass

    def encoder(obj: bytes) -> str:
        return obj.decode()

    def decoder(string: str) -> bytes:
        return string.encode()


# Generated at 2022-06-13 19:13:41.981003
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(True)
    assert Exclude.ALWAYS(False)
    assert Exclude.ALWAYS(None)


# Generated at 2022-06-13 19:14:17.299446
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    def func():
        return True
    assert Exclude.NEVER(func) == False
    assert Exclude.NEVER(func) is False


# Generated at 2022-06-13 19:14:23.753339
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None)
    # TODO: verify what happens when Exclude.ALWAYS(None)
    # assert Exclude.ALWAYS(0)
    # assert Exclude.ALWAYS(1)
    # assert Exclude.ALWAYS(True)
    # assert Exclude.ALWAYS(False)
    # assert Exclude.ALWAYS("")
    # assert Exclude.ALWAYS("abc")
    # assert Exclude.ALWAYS([])
    # assert Exclude.ALWAYS(['a'])
    # assert Exclude.ALWAYS((1, 2, 3))


# Generated at 2022-06-13 19:14:25.627972
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    # precondition: `Exclude.ALWAYS` is not null
    assert Exclude.ALWAYS is not None


# Generated at 2022-06-13 19:14:29.902635
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(str)
    assert Exclude.ALWAYS(int)
    assert Exclude.ALWAYS(float)
    assert Exclude.ALWAYS(list)
    assert Exclude.ALWAYS(set)
    assert Exclude.ALWAYS(dict)
    assert Exclude.ALWAYS(tuple)
    assert Exclude.ALWAYS(None)
    assert Exclude.ALWAYS('hello')
    assert Exclude.ALWAYS(object)


# Generated at 2022-06-13 19:14:30.898335
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(None) == False


# Generated at 2022-06-13 19:14:32.709854
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True
    assert Exclude.ALWAYS(list()) == True
    assert Exclude.ALWAYS("a") == True


# Generated at 2022-06-13 19:14:35.181913
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(2) == True
    assert Exclude.ALWAYS('a') == True
    assert Exclude.ALWAYS([1,2,3]) == True
    assert Exclude.ALWAYS({1:2,2:3}) == True
    return True



# Generated at 2022-06-13 19:14:36.269579
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    test = Exclude()
    assert test.ALWAYS(1) == True


# Generated at 2022-06-13 19:14:41.334602
# Unit test for function config
def test_config():
    from dataclasses import dataclass, field

    from marshmallow_dataclass import NewType
    from marshmallow_dataclass.config import get_marshmallow_config

    class Color(NewType):
        def __init__(self, color):
            self.value = color

    @dataclass
    class Person:
        name: str = field(metadata=config(
            encoder=lambda obj: {"name": obj.name},
            decoder=lambda dic: Person(dic['name']),
            mm_field=str,
            letter_case=lambda name: name.upper(),
            undefined=Undefined.RAISE,
            exclude=Exclude.ALWAYS,
        ))

# Generated at 2022-06-13 19:14:43.058365
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert(Exclude.ALWAYS(1) == True)


# Generated at 2022-06-13 19:16:06.422986
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(2)


# Generated at 2022-06-13 19:16:07.326330
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    e = Exclude.NEVER(1)
    assert e == False


# Generated at 2022-06-13 19:16:18.230831
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("abc")
    assert Exclude.NEVER("abcd")
    assert Exclude.NEVER("abcde")

# Generated at 2022-06-13 19:16:18.765089
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False

# Generated at 2022-06-13 19:16:21.050591
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("") == False
    assert Exclude.NEVER("1") == False



# Generated at 2022-06-13 19:16:26.838112
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS(0)
    assert Exclude.ALWAYS(True)
    assert Exclude.ALWAYS(False)
    assert Exclude.ALWAYS(None)
    assert Exclude.ALWAYS(Exclude.ALWAYS)
    assert Exclude.ALWAYS(Exclude.NEVER)
    assert Exclude.ALWAYS('hello')
    assert Exclude.ALWAYS('')


# Generated at 2022-06-13 19:16:28.291752
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    print("NEVER is {0}".format(Exclude.NEVER("Hello")))

# Generated at 2022-06-13 19:16:30.821415
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(0) == False
    assert Exclude.NEVER(1) == False
    assert Exclude.NEVER(99) == False


# Generated at 2022-06-13 19:16:42.796355
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert(Exclude.ALWAYS(0) == True)
    assert(Exclude.ALWAYS(1) == True)
    assert(Exclude.ALWAYS(12) == True)
    assert(Exclude.ALWAYS(9) == True)
    assert(Exclude.ALWAYS(-1) == True)
    assert(Exclude.ALWAYS(-123) == True)
    assert(Exclude.ALWAYS(0.0) == True)
    assert(Exclude.ALWAYS(1.0) == True)
    assert(Exclude.ALWAYS(12.1) == True)
    assert(Exclude.ALWAYS(-1.25) == True)
    assert(Exclude.ALWAYS(-123.123) == True)
    assert(Exclude.ALWAYS("") == True)

# Generated at 2022-06-13 19:16:44.833412
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(10) == True
    assert Exclude.ALWAYS(None) == True
    assert Exclude.ALWAYS('test') == True
