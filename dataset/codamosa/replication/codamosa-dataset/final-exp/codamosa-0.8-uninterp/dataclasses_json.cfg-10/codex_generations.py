

# Generated at 2022-06-13 19:09:43.493142
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None)


# Generated at 2022-06-13 19:09:49.794686
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None) == True
    assert Exclude.ALWAYS(True) == True
    assert Exclude.ALWAYS(False) == True
    assert Exclude.ALWAYS(1) == True
    assert Exclude.ALWAYS({}) == True
    assert Exclude.ALWAYS([]) == True
    assert Exclude.ALWAYS("") == True

# Generated at 2022-06-13 19:09:51.549670
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert(Exclude.ALWAYS('1'))



# Generated at 2022-06-13 19:09:53.715990
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(0) == False


# Generated at 2022-06-13 19:09:57.332746
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER('') == False
    assert Exclude.NEVER(False) == False
    assert Exclude.NEVER(None) == False
    assert Exclude.NEVER(True) == False



# Generated at 2022-06-13 19:09:58.685181
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
   assert(Exclude.ALWAYS(None) == True)


# Generated at 2022-06-13 19:09:59.377938
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(3)


# Generated at 2022-06-13 19:10:00.518917
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(None) == False


# Generated at 2022-06-13 19:10:01.798126
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False


# Generated at 2022-06-13 19:10:02.549755
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS('foo') is True


# Generated at 2022-06-13 19:10:05.852399
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():

    assert Exclude.ALWAYS is not None


# Generated at 2022-06-13 19:10:08.678856
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True
    assert Exclude.ALWAYS("s") == True
    assert Exclude.ALWAYS(1.0) == True
    assert Exclude.ALWAYS(False) == True


# Generated at 2022-06-13 19:10:14.337793
# Unit test for function config
def test_config():
    from marshmallow import fields as mm_fields
    from dataclasses import dataclass

    @dataclass
    @config(encoder=None,
            decoder=None,
            mm_field=None,
            letter_case=None,
            undefined=None,
            exclude=None)
    class Data:
        a: str



# Generated at 2022-06-13 19:10:17.242025
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    e = Exclude()
    if e.ALWAYS(5):
        print("true")
    if e.ALWAYS(0):
        print("can't be true")


# Generated at 2022-06-13 19:10:19.340803
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    exp_result = False
    result = Exclude.NEVER(False)
    assert result == exp_result



# Generated at 2022-06-13 19:10:22.467938
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("I hope this passes")
    assert Exclude.ALWAYS("I hope this passes")
    assert Exclude.ALWAYS("I hope this passes")
    assert Exclude.ALWAYS("I hope this passes")


# Generated at 2022-06-13 19:10:24.265930
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS([1, 2, 3])
    assert Exclude.ALWAYS(1234)


# Generated at 2022-06-13 19:10:25.535287
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(2) == False


# Generated at 2022-06-13 19:10:32.262065
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(True) is False
    assert Exclude.NEVER(False) is False
    assert Exclude.NEVER(1) is False
    assert Exclude.NEVER(0) is False
    assert Exclude.NEVER("") is False
    assert Exclude.NEVER("hello") is False


# Generated at 2022-06-13 19:10:36.016799
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(None) == False
    assert Exclude.NEVER(1) == False
    assert Exclude.NEVER('') == False
    assert Exclude.NEVER('1') == False


# Generated at 2022-06-13 19:10:39.169459
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1)



# Generated at 2022-06-13 19:10:40.926907
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None) == True

# Generated at 2022-06-13 19:10:42.330036
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None) == True


# Generated at 2022-06-13 19:10:43.790045
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True


# Generated at 2022-06-13 19:10:50.949668
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
  assert Exclude.ALWAYS(1)
  assert Exclude.ALWAYS(False)
  assert Exclude.ALWAYS(0.0)
  assert Exclude.ALWAYS(None)
  assert Exclude.ALWAYS('')
  assert Exclude.ALWAYS(())
  assert Exclude.ALWAYS([])
  assert Exclude.ALWAYS({})
  assert Exclude.ALWAYS(set())
  assert Exclude.ALWAYS(frozenset())


# Generated at 2022-06-13 19:10:52.225198
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(2) == True


# Generated at 2022-06-13 19:10:56.268729
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    data = [0, -1, 0.0, 1.1, "0", "a", True, [], [1], [0], [0.0], [1.1], ["0"],
            {}, {1: 1}, {0: 0}, {0.0: 0.0}, {1.1: 1.1}, {"0": "0"}, None]
    for d in data:
        assert Exclude.NEVER(d) == False


# Generated at 2022-06-13 19:10:58.539246
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    print(Exclude.NEVER(1))



# Generated at 2022-06-13 19:11:04.113300
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS('a')
    assert Exclude.ALWAYS(True)
    assert Exclude.ALWAYS(None)
    assert Exclude.ALWAYS(Exclude())


# Generated at 2022-06-13 19:11:04.938474
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(None)

# Generated at 2022-06-13 19:11:09.790934
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS('_')


# Generated at 2022-06-13 19:11:11.019934
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert not Exclude.NEVER("a")

# Generated at 2022-06-13 19:11:15.572531
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True
    assert Exclude.ALWAYS('') == True
    assert Exclude.ALWAYS(0) == True
    assert Exclude.ALWAYS(0.0) == True
    assert Exclude.ALWAYS(False) == True
    assert Exclude.ALWAYS(None) == True
    assert Exclude.ALWAYS(()) == True
    assert Exclude.ALWAYS({}) == True
    assert Exclude.ALWAYS([]) == True


# Generated at 2022-06-13 19:11:31.836835
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(True) == True
    assert Exclude.ALWAYS(False) == True
    assert Exclude.ALWAYS(1) == True
    assert Exclude.ALWAYS(0) == True
    assert Exclude.ALWAYS("not empty") == True
    assert Exclude.ALWAYS("") == True
    assert Exclude.ALWAYS('a') == True
    assert Exclude.ALWAYS(None) == True
    assert Exclude.ALWAYS(5.5) == True
    assert Exclude.ALWAYS(0.0) == True
    assert Exclude.ALWAYS(.5) == True
    assert Exclude.ALWAYS(['list', 'of', 'things']) == True
    assert Exclude.ALWAYS(['list']) == True


# Generated at 2022-06-13 19:11:33.396200
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS("a")
    assert Exclude.ALWAYS(1.0)


# Generated at 2022-06-13 19:11:35.237340
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    func = Exclude.ALWAYS
    assert func(object()) is True, "Alwasy should return true"



# Generated at 2022-06-13 19:11:36.968984
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    test_Exclude_value = Exclude.ALWAYS(1)
    expected_Exclude_value = True

    assert test_Exclude_value == expected_Exclude_value


# Generated at 2022-06-13 19:11:42.509781
# Unit test for function config
def test_config():
    _config = config()
    assert _config.get('dataclasses_json', {}) == {'undefined': Undefined.EXCLUDE}

    _config = config(metadata={'Object': {'name': 'Object', 'type': 'Class'}},
                     encoder={'name': 'encoder'},
                     decoder={'name': 'decoder'},
                     mm_field={'name': 'mm_field'},
                     letter_case={'name': 'letter_case'},
                     undefined='RAISE',
                     exclude={'name': 'exclude'})
    assert _config == {
        'dataclasses_json': {'undefined': Undefined.RAISE},
        'Object': {'name': 'Object', 'type': 'Class'}
    }
    assert _config['dataclasses_json']

# Generated at 2022-06-13 19:11:44.051292
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS('hello') is True


# Generated at 2022-06-13 19:11:47.003323
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    test_t = Exclude.ALWAYS(tuple)
    assert test_t, "method ALWAYS of class Exclude doesn't return True"


# Generated at 2022-06-13 19:11:53.074083
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    # WHEN ALWAYS is called
    result = Exclude.ALWAYS('dummy')
    # THEN the result is True
    assert True == result



# Generated at 2022-06-13 19:11:55.753174
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("") is False
    assert Exclude.NEVER(5) is False
    assert Exclude.NEVER(True) is False
    assert Exclude.NEVER([]) is False


# Generated at 2022-06-13 19:11:57.051145
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False


# Generated at 2022-06-13 19:11:58.684250
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    print(Exclude.NEVER)
    assert Exclude.NEVER('hello') == False

# Generated at 2022-06-13 19:12:01.657943
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(10)
    assert Exclude.NEVER(None)
    assert Exclude.NEVER(object())  # object is a not-callable type
    assert Exclude.NEVER(lambda: False)


# Generated at 2022-06-13 19:12:02.785308
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(None)

# Generated at 2022-06-13 19:12:08.718170
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(5) == False
    assert Exclude.NEVER(0) == False
    assert Exclude.NEVER(-1) == False
    assert Exclude.NEVER(0.0) == False
    assert Exclude.NEVER(-1.0) == False
    assert Exclude.NEVER(False) == False
    assert Exclude.NEVER(True) == False
    assert Exclude.NEVER("Hi") == False
    assert Exclude.NEVER([]) == False
    assert Exclude.NEVER(()) == False
    assert Exclude.NEVER({}) == False
    assert Exclude.NEVER(None) == False
    assert Exclude.NEVER(Exclude.NEVER) == False


# Generated at 2022-06-13 19:12:20.670242
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert('NEVER_test' in globals())
    del globals()['NEVER_test']

    @dataclass_json
    @dataclass
    class TestClass:
        field1: int = 1
        field2: str = 'NEVER_test'

    TestClass_dict = dict(
        # field1:int = 1
        field2='NEVER_test'
    )
    # print("TestClass_dict: ", TestClass_dict)

    test_obj = TestClass.from_json(TestClass_dict)
    # print("test_obj: ", test_obj)
    assert(test_obj.field2 == 'NEVER_test')

    assert('NEVER_test' in globals())
    del globals()['NEVER_test']


# Generated at 2022-06-13 19:12:22.894342
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(True)
    assert Exclude.ALWAYS(False)
    assert Exclude.ALWAYS(None)
    assert Exclude.ALWAYS(42)


# Generated at 2022-06-13 19:12:24.303678
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    a = Exclude.ALWAYS(1)
    assert a == True


# Generated at 2022-06-13 19:12:36.716701
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    @dataclass
    class Employee:
        id: int
        name: str

    json_str = '''{
        "id": 12345,
        "name": "Jenny"
    }'''

    @dataclass_json.config(exclude=Exclude.NEVER, mm_skip=True)
    class Emp:
        id: int
        name: str

    assert Exclude.NEVER(Emp)

    emp = dataclass_json.loads(json_str, Emp)
    assert emp.id == 12345
    assert emp.name == "Jenny"


# Generated at 2022-06-13 19:12:39.456956
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None) == True
    assert Exclude.ALWAYS(1) == True
    assert Exclude.ALWAYS('hello') == True
    return True


# Generated at 2022-06-13 19:12:43.100682
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER({})
    assert Exclude.NEVER({'name': 'first'})
    assert Exclude.NEVER({'name': 'new', 'age': 8})


# Generated at 2022-06-13 19:12:46.816414
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    from dataclasses import dataclass

    @dataclass
    class Test_Exclude_NEVER:
        x: int

    assert Exclude.NEVER(Test_Exclude_NEVER.x) == False


# Generated at 2022-06-13 19:12:49.721825
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(object()) is True
    assert Exclude.ALWAYS("") is True
    assert Exclude.ALWAYS(None) is True
    assert Exclude.ALWAYS(42) is True


# Generated at 2022-06-13 19:12:51.047270
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None) == True


# Generated at 2022-06-13 19:12:52.230757
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None) is True


# Generated at 2022-06-13 19:12:54.699446
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(3) == False



# Generated at 2022-06-13 19:12:56.829503
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS() == True


# Generated at 2022-06-13 19:12:58.206942
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert(True == Exclude.ALWAYS(None))


# Generated at 2022-06-13 19:13:13.269275
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(True) is True
    assert Exclude.ALWAYS(False) is True

# Generated at 2022-06-13 19:13:15.083702
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True
    assert Exclude.ALWAYS(0) == True

# Generated at 2022-06-13 19:13:18.138179
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("") == False, "Failed test on Exclude.NEVER"
    assert Exclude.NEVER("abc") == False, "Failed test on Exclude.NEVER"


# Generated at 2022-06-13 19:13:20.016446
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(5) == False


# Generated at 2022-06-13 19:13:22.229281
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("test") == True


# Generated at 2022-06-13 19:13:34.177273
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER is not None
    assert Exclude.NEVER(1) == False
    assert Exclude.NEVER(0) == False
    assert Exclude.NEVER(0.0) == False
    assert Exclude.NEVER('') == False
    assert Exclude.NEVER(' ') == False
    assert Exclude.NEVER('test') == False
    assert Exclude.NEVER('field_name') == False
    assert Exclude.NEVER([]) == False
    assert Exclude.NEVER(['field_name']) == False
    assert Exclude.NEVER(['field_name', 'field_name_2']) == False
    assert Exclude.NEVER({'field': 'name'}) == False
    assert Exclude.NEVER(complex(0)) == False
    assert Exclude.NEVER

# Generated at 2022-06-13 19:13:43.953279
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    x = Exclude()
    assert x.ALWAYS(1) == True


# Generated at 2022-06-13 19:13:48.253362
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS(None)
    assert Exclude.ALWAYS(-1)
    assert Exclude.ALWAYS(True)
    assert Exclude.ALWAYS(False)


# Generated at 2022-06-13 19:13:49.260365
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1)


# Generated at 2022-06-13 19:13:51.136976
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    '''
    This function tests whether the Exclude class' method ALWAYS works or not
    :return: True or False
    '''
    assert Exclude.ALWAYS(0) == True


# Generated at 2022-06-13 19:14:21.992836
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    """
    Unit test for method ALWAYS of class Exclude
    """
    r = Exclude.ALWAYS(True)
    assert r == True
    r = Exclude.ALWAYS(False)
    assert r == True
    r = Exclude.ALWAYS(1)
    assert r == True


# Generated at 2022-06-13 19:14:23.107030
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    global_config.exclude = Exclude.ALWAYS



# Generated at 2022-06-13 19:14:25.340229
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    def test(obj):
        return False

    assert test(Exclude.NEVER), "NEVER's method test(obj) should always return False"


# Generated at 2022-06-13 19:14:27.278618
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True
    assert Exclude.ALWAYS(0) == True
    assert Exclude.ALWAYS(-1) == True


# Generated at 2022-06-13 19:14:28.042056
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None)

# Generated at 2022-06-13 19:14:29.288791
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False
    assert Exclude.NEVER(2) == False

# Generated at 2022-06-13 19:14:35.804145
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True
    assert Exclude.ALWAYS(1.0) == True
    assert Exclude.ALWAYS("string") == True
    assert Exclude.ALWAYS((1,2,3)) == True
    assert Exclude.ALWAYS([1,2,3]) == True
    assert Exclude.ALWAYS({"key": "value"}) == True
    assert Exclude.ALWAYS(None) == True
    return True


# Generated at 2022-06-13 19:14:46.910003
# Unit test for function config
def test_config():
    metadata = {}
    lib_metadata = metadata.setdefault('dataclasses_json', {})
    assert 'encoder' not in lib_metadata
    assert 'decoder' not in lib_metadata
    assert 'mm_field' not in lib_metadata
    assert 'letter_case' not in lib_metadata
    assert 'undefined' not in lib_metadata
    assert 'field_name' not in lib_metadata
    assert 'exclude' not in lib_metadata
    
    def func():
        pass
    
    metadata = config(encoder=func, decoder=func, mm_field=func, letter_case=func, undefined=func, exclude=func)
    assert 'encoder' in lib_metadata
    assert 'decoder' in lib_metadata
    assert 'mm_field' in lib_metadata

# Generated at 2022-06-13 19:14:47.909604
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("abc") == False

# Generated at 2022-06-13 19:14:49.153868
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    r = Exclude.NEVER(1)
    assert r == False


# Generated at 2022-06-13 19:15:59.894348
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert(Exclude.NEVER(1) == False )
    assert(Exclude.NEVER('test') == False )
    assert(Exclude.NEVER([1,2,3]) == False )


# Generated at 2022-06-13 19:16:04.579540
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(2)
    assert Exclude.ALWAYS(Exclude)
    assert Exclude.ALWAYS("test")
    assert Exclude.ALWAYS(True)


# Generated at 2022-06-13 19:16:05.854986
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False



# Generated at 2022-06-13 19:16:07.230827
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    some_object = Exclude()
    assert some_object.ALWAYS(True)


# Generated at 2022-06-13 19:16:18.230231
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS(True)
    assert Exclude.ALWAYS('abc')


# Generated at 2022-06-13 19:16:20.191045
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    result = Exclude.ALWAYS(42)
    assert result == True

# Generated at 2022-06-13 19:16:22.358301
# Unit test for method ALWAYS of class Exclude

# Generated at 2022-06-13 19:16:23.769306
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True


# Generated at 2022-06-13 19:16:24.873473
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER('value') == False


# Generated at 2022-06-13 19:16:32.644528
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    from dataclasses import dataclass

    @dataclass
    class Person:
        first_name: str
        last_name: str = 'Doe'
        middle_name: str = 'Undefined'
        def __init__(self, first_name: str, last_name: Optional[str]=None, middle_name: Optional[str]=None) -> None:
            self.first_name = first_name
            if last_name is not None:
                self.last_name = last_name
            if middle_name is not None:
                self.middle_name = middle_name

    person = Person(first_name='John')
    assert isinstance(person, Person)
    assert person.first_name == 'John'
    assert person.last_name == 'Doe'

# Generated at 2022-06-13 19:18:58.308021
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER({}) == False
    assert Exclude.NEVER(0) == False
    assert Exclude.NEVER(1) == False
    assert Exclude.NEVER('a') == False


# Generated at 2022-06-13 19:19:00.188625
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert(Exclude.ALWAYS(1) == True)


# Generated at 2022-06-13 19:19:02.023899
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None) == True


# Generated at 2022-06-13 19:19:05.383812
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    test_data = (2, 3.0, "hello", [1, 2], (1, 2), {"k": "v"}, {}, None, True)
    is_included = Exclude.ALWAYS(test_data)
    print(is_included)


# Generated at 2022-06-13 19:19:09.279998
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    # Copy class Exclude
    class ExcludeTest:
        NEVER: Callable[[T], bool] = Exclude.NEVER

    exclude = ExcludeTest()
    # Test 1
    assert exclude.NEVER(int)

    # Test 2
    assert exclude.NEVER(str)



# Generated at 2022-06-13 19:19:12.760885
# Unit test for function config
def test_config():
    import dataclasses
    import dataclasses_json
    @dataclasses_json.config
    def test_func(a, b=2, *, c=3, **kwargs):
        return a * b * c * len(kwargs)
    # test function call:
    @dataclasses.dataclass
    class Test:
        a: int = 1

    assert test_func(**Test().dict()) == 6

# Generated at 2022-06-13 19:19:14.737481
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert(Exclude.NEVER(3) == False)

# Generated at 2022-06-13 19:19:15.760892
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("")



# Generated at 2022-06-13 19:19:17.004734
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(None) == False


# Generated at 2022-06-13 19:19:23.703750
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
  assert(Exclude.NEVER(False) == False)
  assert(Exclude.NEVER(True) == False)
  assert(Exclude.NEVER(None) == False)
  assert(Exclude.NEVER(1) == False)
  assert(Exclude.NEVER(1.1) == False)
  assert(Exclude.NEVER("a") == False)
  assert(Exclude.NEVER([1]) == False)
  assert(Exclude.NEVER({'a': 1}) == False)
  assert(Exclude.NEVER('abc') == False)
  assert(Exclude.NEVER(b'abc') == False)
  assert(Exclude.NEVER(set()) == False)
