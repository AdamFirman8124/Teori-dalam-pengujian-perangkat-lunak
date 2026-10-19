

# Generated at 2022-06-14 14:25:06.202915
# Unit test for method validate of class Choice
def test_Choice_validate():
    clazz = Choice(
        choices=[("a", "A"), ("b", "B"), ("c", "C"), ("d", "D")],
    )
    assert clazz.validate("a") == "a"
    assert clazz.validate("b") == "b"
    assert clazz.validate("c") == "c"
    assert clazz.validate("d") == "d"


# Generated at 2022-06-14 14:25:17.938345
# Unit test for method validate of class Object
def test_Object_validate():
    expected_errors = {
        "null": "May not be null.",
        "type": "Must be an object.",
        "invalid_key": "All object keys must be strings.",
        "required": "This field is required.",
        "invalid_property": "Invalid property name.",
        "empty": "Must not be empty.",
        "max_properties": "Must have no more than {max_properties} properties.",
        "min_properties": "Must have at least {min_properties} properties.",
    }
    data = Object(properties = {
        'foo': String()
    }, required = ['foo'])
    # test code: a valid value
    value = {'foo': 'bar'}
    assert data.validate(value) == value

    # test code: a valid value

# Generated at 2022-06-14 14:25:24.709134
# Unit test for method validate_or_error of class Field
def test_Field_validate_or_error():
    class TT(Field):
        def validate(self, value: typing.Any, *, strict: bool = False) -> typing.Any:
            if value == 1:
                raise Exception('throw an error')
            return value

    tt = TT()
    value1 = tt.validate_or_error(1)
    assert value1.value is None
    assert value1.error.code == 'type_error'
    assert value1.error.text == 'type error'

    value2 = tt.validate_or_error(2)
    assert value2.value == 2
    assert value2.error is None
    return TT
TT = test_Field_validate_or_error()



# Generated at 2022-06-14 14:25:27.432951
# Unit test for method validate of class Object
def test_Object_validate():
    get_errors = Object(properties={'test':Boolean()}).validate({'test':'test'})
    assert get_errors == 'Boolean'

# Generated at 2022-06-14 14:25:32.693528
# Unit test for method validate of class Union
def test_Union_validate():
    assert (Union([Integer()]).validate(10) == 10)
    try:
        Union([Integer()]).validate(None)
        raise AssertionError("Must be raised an error")
    except ValidationError:
        pass
    try:
        Union([Integer()]).validate("10")
        raise AssertionError("Must be raised an error")
    except ValidationError:
        pass

TypeChecker.verify_subclass(Union, Field)



# Generated at 2022-06-14 14:25:38.338510
# Unit test for method validate of class Union
def test_Union_validate():
    field = Union([
        Object(properties={'name': Text(default='tom')}),
        Object(properties={'name': Text(default='peter')})
    ])
    assert field.validate({'name': 'tom'}) == {'name': 'tom'}
    assert field.validate({'name': 'peter'}) == {'name': 'peter'}
    with pytest.raises(ValidationError):
        field.validate({'name': 'susan'})
    assert field.validate({'name': 'tom'}) == field.serialize({'name': 'tom'})



# Generated at 2022-06-14 14:25:47.537300
# Unit test for method serialize of class String
def test_String_serialize():
    import datetime
    date = datetime.datetime(2011, 11, 22)
    date_string = date.strftime('%Y-%m-%dT%H:%M:%S')
    assert date_string == '2011-11-22T00:00:00'

    t = String(format='datetime')
    assert t.serialize(date) == date_string

    #input is datetime type, but format is not datetime
    t = String(format='time')
    assert t.serialize(date) == '00:00:00'



# Generated at 2022-06-14 14:25:49.628809
# Unit test for method validate of class Choice
def test_Choice_validate():
    choice = Choice(choices = ["red","blue"])
    assert choice.validate("red") == "red"
    assert choice.validate(None) == None
    assert choice.validate("") == None
    assert choice.validate(1) == None
    assert choice.validate(0) == None


# Generated at 2022-06-14 14:25:53.502115
# Unit test for method validate of class Choice
def test_Choice_validate():
    ch = Choice(choices=[1, 2, 3, 'string'])
    assert ch.validate(1) == 1
    assert ch.validate(4) == None


# Generated at 2022-06-14 14:26:02.889445
# Unit test for method serialize of class String
def test_String_serialize():
    obj = String()
    assert obj.serialize('bbb') == 'bbb'
    obj.format = 'date'
    assert obj.serialize('bbb') == 'bbb'
    assert obj.serialize('2018-01-01') == '2018-01-01'
    obj.format = 'datetime'
    assert obj.serialize('bbb') == 'bbb'
    assert obj.serialize('2018-01-01T00:00:00Z') == '2018-01-01T00:00:00Z'
    obj.format = 'uuid'
    assert obj.serialize('bbb') == 'bbb'

# Generated at 2022-06-14 14:26:22.405541
# Unit test for method validate of class Array
def test_Array_validate():
    array = Array(items=Integer())
    input_array =[1,2,3]
    output_array = [1,2,3]
    assert array.validate(input_array) == output_array, 'validation failed'
    input_array =[1,'2',3]
    output_array = [1,2,3]
    assert array.validate(input_array) == output_array, 'validation failed'
    input_array =[1.0, 2.0,3.0]
    output_array = [1,2,3]
    assert array.validate(input_array) == output_array, 'validation failed'
    input_array =[1, 2,3,4]
    output_array = [1,2,3,4]

# Generated at 2022-06-14 14:26:27.502835
# Unit test for method __or__ of class Field
def test_Field___or__():
    instance1 = Field(title='', description='', default=NO_DEFAULT, allow_null=False)
    instance2 = Field(title='', description='', default=NO_DEFAULT, allow_null=False)
    field = instance1 | instance2
    assert isinstance(field, Union)
    assert field.any_of[0] == instance1
    assert field.any_of[1] == instance2



# Generated at 2022-06-14 14:26:35.758083
# Unit test for method validate of class Choice
def test_Choice_validate():
    value_test_list = ["null", "none", "" , 1, [1], {'a': 2}]
    for value in value_test_list:
        try:
            test = Choice()
            test.validate(value)
            assert False
        except ValidationError:
            pass
    value = str()
    try:
        test = Choice()
        test.validate(value)
        assert False
    except ValidationError:
        pass


# Generated at 2022-06-14 14:26:44.732532
# Unit test for method validate of class Array
def test_Array_validate():
    myField2 = Array(allow_null=True, items=Integer())
    with pytest.raises(ValidationError) as exception_info:
        myField2.validate('my string')
    assert str(exception_info.value) == 'Encountered the following error(s):\n - Must be an array. (code=type)'

    myField3 = Array(allow_null=True, items=Integer(), min_items=1)
    valid, error = myField3.validate_or_error([1, 2, 3])
    assert valid == [1, 2, 3]
    assert error is None
    with pytest.raises(ValidationError) as exception_info:
        myField3.validate([])

# Generated at 2022-06-14 14:26:47.348196
# Unit test for method validate of class Array
def test_Array_validate():
    class TestArray(Array):
        def validate(self, obj, *, strict=False):
            return super().validate(obj, strict=strict)
    arr = TestArray(items=Field(type="string"))
    arr.validate(["string"])
    with pytest.raises(ValidationError) as exc:
        arr.validate(["not_string"])
    exc.value.messages[0].text == 'Must be a string.'


# Generated at 2022-06-14 14:26:53.582079
# Unit test for method validate of class Array

# Generated at 2022-06-14 14:27:01.054017
# Unit test for method serialize of class Array
def test_Array_serialize():
  arrayItems = [Str(), Int()]
  inputValue = ["a", 1]
  obj = Array(items=arrayItems)
  arrayOutput = obj.serialize(inputValue)
  validate.non_empty_array(arrayOutput)
  validate.length(2, arrayOutput)
  validate.array_elements_of_type(str, arrayOutput)
  # TODO: Validate all elments of the array are serialized, as per the Array's items
  # arrayOutput = [i.serialize(x) for i, x in zip(arrayItems, inputValue)]



# Generated at 2022-06-14 14:27:04.930440
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    # init a Field obj
    field = Field()
    # test if method get_default_value returns the expected value
    assert field.get_default_value() is None


# Generated at 2022-06-14 14:27:10.190881
# Unit test for method validate of class String
def test_String_validate():
    s = String(max_length=4)
    assert s.validate('abc') == 'abc'
    assert s.validate('abcde') == None
    assert s.validate(None) == None
    assert s.validate(1.0) == None
    assert s.validate('') == None


# Generated at 2022-06-14 14:27:11.659663
# Unit test for method validate of class Array
def test_Array_validate():
    f = Array(items=field.Integer(), unique_items=True)
    assert f.validate([1, 2]) == [1, 2]
    assert f.validate([1, 1])

test_Array_validate()



# Generated at 2022-06-14 14:27:30.552316
# Unit test for method serialize of class Array
def test_Array_serialize():
    # test with an Array of simple objects
    class Person(Object):
        first_name = String()
        last_name = String()
        age = Integer()
    class A(Array):
        items = Person()
    person1=Person(first_name="Bob", last_name="Smith", age=24)
    person2=Person(first_name="Alice", last_name="Smith", age=25)
    person3=Person(first_name="Charlie", last_name="Smith", age=26)
    assert A(person1,person2,person3)==A(person1,person2,person3).serialize(A(person1,person2,person3))

    # test with an Array of arrays
    class B(Array):
        items = Integer()
    class C(Array):
        items = B()
    assert C

# Generated at 2022-06-14 14:27:34.882074
# Unit test for method validate of class Array
def test_Array_validate():
    array = Array()
    assert array.validate(None) is None

    test_value = [1, 2, 3]
    assert array.validate(test_value) == test_value
    assert array.validate([]) == []

    # error = array.validate(None)
    # print(error)



# Generated at 2022-06-14 14:27:37.703568
# Unit test for method serialize of class Array
def test_Array_serialize():
    array_obj =  ['test-value']
    sut = Array()
    actual = sut.serialize(array_obj)
    assert actual == ['test-value']


# Generated at 2022-06-14 14:27:43.336470
# Unit test for method validate of class Number
def test_Number_validate():
    valid = [20, 20.2, "20.2"]
    invalid = ["20.2.2", "", None, "a"]
    num = Number(minimum = 10, maximum = 20)
    for i in valid:
        assert num.validate(i) == i
    for i in invalid:
        with pytest.raises(ValidationError):
            num.validate(i)



# Generated at 2022-06-14 14:27:50.354745
# Unit test for method validate of class String
def test_String_validate():
    # Case 1: If the input string is too long 
    try:
        s = String(max_length=4)
        s.validate('12345')
    except ValidationError as e:
        assert e.code == 'max_length'
    # Case 2: If the input string is too short
    try:
        s = String(min_length=5)
        s.validate('1234')
    except ValidationError as e:
        assert e.code == 'min_length'
    # Case 3: If the input string has illegal character
    try:
        s = String(pattern='^[0-9]\d*$')
        s.validate('12abc')
    except ValidationError as e:
        assert e.code == 'pattern'


# Generated at 2022-06-14 14:28:01.678812
# Unit test for method validate of class Choice
def test_Choice_validate():
  ch = Choice(choices=[('1', 'a'), ('2', 'b')], required=False, allow_null=False)
  assert ch.validate(1) == 1
  assert ch.validate('1') == '1'
  try:
    ch.validate('3')
    assert False
  except:
    assert True
  try:
    ch.validate(None)
    assert False
  except:
    assert True

test_Choice_validate()


# Generated at 2022-06-14 14:28:06.129598
# Unit test for method __or__ of class Field
def test_Field___or__():
    a = String()
    b = String()
    u = a | b
    assert a and b in u.any_of
# End unit test for method __or__ of class Field


# Generated at 2022-06-14 14:28:08.287541
# Unit test for method validate of class Choice
def test_Choice_validate():
    c = Choice(choices=[(1,2),(3,4)], allow_null=False)
    assert c.validate(1) == 1
    assert c.validate(4) == 4
    assert c.validate(5) == 'Not a valid choice.'

# Generated at 2022-06-14 14:28:17.050203
# Unit test for method validate of class Number
def test_Number_validate():
    def test_type(value, numeric_type, allow_null, strict, **kwargs):
        numeric_type = numeric_type or float
        try:
            numeric_type(value)
            expected = numeric_type(value)
        except (ValueError, TypeError):
            expected = ValidationError('Must be a number.')

        result = Number(
            allow_null=allow_null,
            numeric_type=numeric_type,
            **kwargs
        ).validate_or_error(value, strict=strict)
        assert result.value == expected or result.error != expected

    def test_finite(value, numeric_type, allow_null, strict, **kwargs):
        numeric_type = numeric_type or float

# Generated at 2022-06-14 14:28:22.658004
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    # When an object of class Field is created
    f=Field(title='f1',description='desc1')
    # When we call method get_default_value
    v=f.get_default_value()
    # Then it returns None
    assert v is None
    

# Generated at 2022-06-14 14:28:39.368650
# Unit test for constructor of class Array
def test_Array():
    f = Array(items=Integer(), additional_items=None, min_items=1, max_items=1, unique_items=False)
    assert f.items == [Integer()]
    assert f.additional_items is None
    assert f.min_items == 1
    assert f.max_items == 1
    assert f.unique_items == False

    with pytest.raises(AssertionError):
        Array(items=Integer(), additional_items=None, min_items=1, max_items=1, unique_items=1)


# Generated at 2022-06-14 14:28:40.670764
# Unit test for method validate of class Array
def test_Array_validate():
    pass


# Generated at 2022-06-14 14:28:46.024031
# Unit test for method validate of class Choice
def test_Choice_validate():
    list_of_tuples = [('1', 'one'),('2', 'two'),('3', 'three'),]
    assert Choice(choices=list_of_tuples).validate(value='1') == '1'
    assert Choice(choices=list_of_tuples).validate(value='4') == ValueError()



# Generated at 2022-06-14 14:28:58.447084
# Unit test for method validate of class Array
def test_Array_validate():
    a = Array(
        min_items=5, max_items=5, items=Field()
    )
    b = Array(
        min_items=5, max_items=5, items=Field()
    )
    assert a.validate(x) == b.validate(x) and a.validate(x) == c
    #Edge case
    x = []
    c = []
    with pytest.raises(ValidationError):
        a.validate(x)
    x = [1,2,3]
    with pytest.raises(ValidationError):
        a.validate(x)
    x = [1,2,3,4,5,6]
    with pytest.raises(ValidationError):
        a.validate(x)



# Generated at 2022-06-14 14:29:04.791509
# Unit test for method validate of class Choice
def test_Choice_validate():
    assert Choice(choices=["Python", "Java", "C++"], allow_null=True).validate("Java") == "Java"
    # test_fails_on_parsing_invalid_characters
    with pytest.raises(ValidationError) as err:
        Choice(choices=["Python", "Java", "C++"], allow_null=False).validate("Scala")
    assert "choice" == err.value.code



# Generated at 2022-06-14 14:29:14.670581
# Unit test for method validate of class Choice
def test_Choice_validate():
    field1 = Choice(choices=["a", "b"])
    field2 = Choice(choices=["c", "d"])
    assert field1.validate("a") == "a"
    assert field1.validate("b") == "b"
    assert field2.validate("c") == "c"
    assert field2.validate("d") == "d"
    assert field1.validate("e") == field1.validation_error("choice")
    assert field1.validate(None) == field1.validation_error("null")
    assert field2.validate("e") == field2.validation_error("choice")
    assert field2.validate(None) == field2.validation_error("null")


# Generated at 2022-06-14 14:29:24.756942
# Unit test for method validate of class Choice
def test_Choice_validate():
    # Test with blank value
    choice = Choice(choices=[("a", "A"), ("b", "B")], allow_null=True)
    try:
        value = choice.validate("", strict=True)
        assert False
    except ValidationError:
        assert True
    
    # Test with empty value
    try:
        value = choice.validate("", strict=False)
        assert value is None and True
    except ValidationError:
        assert False
    
    # Test with null value
    try:
        value = choice.validate(None, strict=False)
        assert value is None and True
    except ValidationError:
        assert False
    
    # Test with not existing value

# Generated at 2022-06-14 14:29:29.029810
# Unit test for constructor of class String
def test_String():
    x = String()
    assert x.allow_blank == False
    assert x.allow_null == False
    assert x.trim_whitespace == True
    assert x.max_length == None
    assert x.min_length == None
    assert x.pattern_regex == None
    assert x.format == None


# Generated at 2022-06-14 14:29:41.891388
# Unit test for method validate of class Choice
def test_Choice_validate():
    import unittest
    import io
    import sys

    class TestChoice(unittest.TestCase):
        def test_Choice_validate(self):
            # Test use of class
            choice = Choice(choices=["apple", "banana"])
            self.assertEqual(choice.validate("apple"), "apple")
            try:
                choice.validate("not a real fruit")
                # If the program reaches this line, then it did not error, so the test failed
                self.assertTrue(False)
            except ValidationError:
                self.assertTrue(True)
            choice2 = Choice(choices=[("apple", "APPLE"), ("banana", "BANANA")])
            self.assertEqual(choice2.validate("BANANA"), "BANANA")

# Generated at 2022-06-14 14:29:49.337173
# Unit test for method validate of class String
def test_String_validate():
    import unittest.mock as mock
    # Setup test objects
    mock_field: mock.MagicMock()
    mock_field.has_default.return_value = False
    mock_field.allow_null = False
    mock_field.allow_blank = False
    mock_field.trim_whitespace = True
    mock_field.max_length = None
    mock_field.min_length = None
    mock_field.pattern = None
    mock_field.pattern_regex = None
    mock_field.format = None
    mock_field.validation_error.side_effect = ValidationError(text="Must be a string.", code="type")

# Generated at 2022-06-14 14:30:00.512488
# Unit test for method serialize of class Array
def test_Array_serialize():
    class Foo(Struct):
            bar=String(serialize_as="BAR")

    field = Array(items=Foo)
    result = field.serialize([{"bar": "foo"}])
    assert isinstance(result, list)
    assert result == [{"BAR": "foo"}]



# Generated at 2022-06-14 14:30:08.351815
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    """ For Field class, method get_default_value unit test"""
    class Field_test(Field):
        def validate(self, value: typing.Any, *, strict: bool = False) -> typing.Any:
            return value

        def serialize(self, obj: typing.Any) -> typing.Any:
            return obj
    # Usingassert
    field = Field_test()
    assert field.get_default_value() == None

# Generated at 2022-06-14 14:30:10.572560
# Unit test for constructor of class Const
def test_Const():
    with pytest.raises(AssertionError):
        Const(**{'allow_null': True})

# Generated at 2022-06-14 14:30:16.053313
# Unit test for method validate of class Union
def test_Union_validate():

    Union_instance = Union(any_of=[Integer(), Boolean()])
    try:
        Union_instance.validate(value=1)
    except ValidationError as exception:
        raise ValueError(exception)

    try:
        Union_instance.validate(value=1)
    except ValidationError as exception:
        raise ValueError(exception)



# Generated at 2022-06-14 14:30:22.679428
# Unit test for method validate of class Union
def test_Union_validate():
    obj = Union(any_of=[String(), Integer()])
    assert obj.validate("string") == "string"
    assert obj.validate(10) == 10
   

    # Test for error code 'union'
    try:
        obj.validate(1.0)
        assert False, "Did not raise ValidationError."
    except ValidationError as e:
        assert e.code == "union"



# Generated at 2022-06-14 14:30:29.569598
# Unit test for constructor of class Array
def test_Array():
    schema = Array(
        items=String(),
        additional_items=True,
        min_items=2,
        max_items=5,
        unique_items=False,
        allow_null=False,
        validators=[]
    )
    assert schema.items == String()
    assert schema.additional_items == True
    assert schema.min_items == 2
    assert schema.max_items == 5
    assert schema.unique_items == False


# Generated at 2022-06-14 14:30:35.559073
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    class FieldOne(Field):
        def __init__(self, **kwargs):
            super(FieldOne, self).__init__(**kwargs)
            self.default = "default"
    field_one = FieldOne()
    assert field_one.get_default_value() == "default"
test_Field_get_default_value()


# Generated at 2022-06-14 14:30:40.658427
# Unit test for method validate of class Choice
def test_Choice_validate():
    field = Choice(choices=[(1, 2), (3, 4), (5, 6)])
    assert field.validate(1) == 1
    assert field.validate(3) == 3
    assert field.validate(5) == 5
    try:
        field.validate(7)
        assert False
    except ValidationError:
        assert True



# Generated at 2022-06-14 14:30:42.410950
# Unit test for method __or__ of class Field
def test_Field___or__():
    import pytest
    msg = "Schema.__or__() method not implemented"    
    with pytest.raises(NotImplementedError, match=msg):
        Field().__or__(Field())


# Generated at 2022-06-14 14:30:44.986897
# Unit test for method validate of class Choice
def test_Choice_validate():
    assert Choice(choices=["a"]).validate("a") == "a"
    assert Choice(choices=["a"]).validate("b") == "b"


# Generated at 2022-06-14 14:31:05.852399
# Unit test for method validate of class Array
def test_Array_validate():
    print('Testing method validate of class Array...', end='')
    assert(Array().validate([]) == [])
    assert(Array(allow_null=True).validate(None) == None)
    assert(Array(allow_null=True).validate([]) == [])

    assert(Array().validate_or_error(None) == (None, ValidationError(messages=[Message(text=Array.errors['null'], code='null')])))
    assert(Array().validate_or_error([]) == ([], None))
    assert(Array().validate_or_error('s') == ('s', ValidationError(messages=[Message(text=Array.errors['type'], code='type')])))

# Generated at 2022-06-14 14:31:13.090171
# Unit test for method validate of class Choice
def test_Choice_validate():
    from datetime import timedelta
    field=Choice(name='Choice',choices=[(timedelta(days=1), '1 Day'), (timedelta(days=7), '1 Week')],allow_null=True,default=timedelta(days=1))
    assert field.validate(timedelta(days=7))==timedelta(days=7)
    try:
        field.validate(timedelta(days=2))
        assert False
    except ValidationError as e:
        assert e.code=='choice'


# Generated at 2022-06-14 14:31:16.994003
# Unit test for method __or__ of class Field
def test_Field___or__():
    # [TODO] How to test this?
    field = Field()
    other = Field()
    assert isinstance(field.__or__(other), Union)



# Generated at 2022-06-14 14:31:19.664891
# Unit test for method validate of class Boolean
def test_Boolean_validate():
    # Given
    value = "True"
    is_value_false = value.lower()
    # Then
    assert value is True



# Generated at 2022-06-14 14:31:25.029215
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    a=Field()
    b=Field(default=[1,2,3])
    c=Field(default=NO_DEFAULT)
    assert a.has_default()==False
    assert b.has_default()==True
    assert b.get_default_value()==[1,2,3]
    assert c.get_default_value()==None



# Generated at 2022-06-14 14:31:26.783457
# Unit test for method validate of class Choice
def test_Choice_validate():
    temp = Choice()
    assert temp.validate("a")
    assert temp.validate("")


# Generated at 2022-06-14 14:31:33.657343
# Unit test for method validate of class Choice
def test_Choice_validate():
    val = Choice()
    print("validate(value=None, *, strict=False) = " + str(val.validate(value=None, strict=False)))
    print("validate(value=None, *, strict=True) = " + str(val.validate(value=None, strict=True)))

    val = Choice(choices=["choice1", "choice2"])
    print("validate(value=None, *, strict=False) = " + str(val.validate(value=None, strict=False)))
    print("validate(value=None, *, strict=True) = " + str(val.validate(value=None, strict=True)))
    print("validate(value='', *, strict=False) = " + str(val.validate(value="", strict=False)))
    print

# Generated at 2022-06-14 14:31:39.283304
# Unit test for method validate of class Choice
def test_Choice_validate():
    
        choice = Choice()
        choice1 = Choice(choices = ["one","two"])
        choice2 = Choice(choices = ["one","two"])
        choice3 = Choice(choices = [1,2])
        choice4 = Choice(choices = ["1","2"])
    
        assert choice.validate("one") == "one"
        assert choice1.validate("one") == "one"
        assert choice2.validate("one", strict=True) == "one"
        assert choice3.validate(1) == 1
        assert choice4.validate("1", strict=True) == "1"

        with pytest.raises(ValidationError):
            choice.validate("one", strict=True)



# Generated at 2022-06-14 14:31:50.730527
# Unit test for method validate of class Array
def test_Array_validate():
    # This is an array of one type
    property1 = properties.String()
    property2 = properties.Integer()
    property3 = properties.Number()
   
    array = properties.Array(items = [property1, property2, property3])
    assert array.validate(['1', 2, 3]) == ['1', 2, 3]
    assert array.serialize(['1', 2, 3]) == ['1', 2, 3]
    assert array.get_default_value() == []
    assert array.has_default() == True
    assert array.allow_null() == False

# Generated at 2022-06-14 14:31:56.247091
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    @dataclass(frozen=True)
    class TestField(Field):
        title: str
        description: str
        default: typing.Any

    field = TestField(title='', description='', default='foo')
    assert field.get_default_value() == 'foo'

    field = TestField(title='', description='', default='foo')
    assert field.get_default_value() == 'foo'

# Generated at 2022-06-14 14:32:17.197964
# Unit test for method validate of class Number
def test_Number_validate():
    assert Number().validate(0.6) == 0.6
    assert Number().validate(-0.6) == -0.6
    assert Number().validate(0) == 0
    assert Number().validate(-0) == 0
    assert Number().validate(3) == 3
    assert Number().validate(-3) == -3
    assert Number().validate(3.0) == 3.0
    assert Number().validate(-3.0) == -3.0

    assert Integer().validate(3.0) == 3

    assert Number(minimum=0).validate(0) == 0
    assert Number(minimum=-0.1).validate(0) == 0
    assert Number(minimum=-0.1).validate(0.1) == 0.1

# Generated at 2022-06-14 14:32:23.286823
# Unit test for method validate of class Array
def test_Array_validate():
    import pytest
    from inspect import signature

    with pytest.raises(TypeError):
        Array.validate()

    field = Array(
        items=[String(), Number()], max_items=2, min_items=1, exact_items=2
    )

    with pytest.raises(ValidationError):
        field.validate([1, 2, 3])

    with pytest.raises(ValidationError):
        field.validate([1])

    with pytest.raises(ValidationError):
        field.validate([[''], [1]])

    assert field.validate([1.0, 2.0]) == [1.0, 2.0]


# Generated at 2022-06-14 14:32:35.552673
# Unit test for method validate of class Choice
def test_Choice_validate():
    ch = Choice(choices=["a", "b", "c"])
    assert ch.validate("a") == "a"
    assert ch.validate("b") == "b"
    assert ch.validate("c") == "c"
    assert ch.validate(None) is None
    try:
        ch.validate("d")
        assert False
    except ValidationError:
        pass
    try:
        ch.validate(0)
        assert False
    except ValidationError:
        pass
    assert ch.validate("") is None
    ch = Choice(choices=[("a", "A"), ("b", "B"), ("c", "C")])
    assert ch.validate("a") == "a"
    assert ch.validate("b") == "b"
    assert ch.valid

# Generated at 2022-06-14 14:32:46.002942
# Unit test for method __or__ of class Field
def test_Field___or__():
    print("test_Field___or__")
    int1 = Integer()
    int2 = Integer()
    union_int1_and_int2 = Union(any_of=[int1, int2])
    union_int1_and_int2_ = int1 | int2
    assert union_int1_and_int2.any_of[0] == union_int1_and_int2_.any_of[0]
    assert union_int1_and_int2.any_of[1] == union_int1_and_int2_.any_of[1]
    str1 = String()
    str2 = String()
    union_str1_and_str2 = Union(any_of=[str1, str2])
    union_str1_and_str2_ = str1 | str2
    assert union_

# Generated at 2022-06-14 14:32:55.073660
# Unit test for method validate of class Array
def test_Array_validate():
    from tortoise.contrib.pydantic import PyDanticValidationMixin

    class Task(PyDanticValidationMixin):
        id: int
        name: str

    class Team(PyDanticValidationMixin):
        name: str
        members: List[Task]

        class Config:
            orm_mode = True
            fields = {"name": "team_name"}

    class TeamSchema(PyDanticValidationMixin):
        name: str
        members: Array(items=Task)

    obj = Team.get(name="Spider Team")
    obj.members.append(Task(id=1, name="Hulk"))
    obj.members.append(Task(id=2, name="Deadpool"))


# Generated at 2022-06-14 14:32:56.471320
# Unit test for method __or__ of class Field
def test_Field___or__():
    assert (Field() | Field())



# Generated at 2022-06-14 14:32:57.602169
# Unit test for method validate of class Choice
def test_Choice_validate():
    assert 1 == 1



# Generated at 2022-06-14 14:33:10.274670
# Unit test for method validate of class Boolean
def test_Boolean_validate():
    assert_equal(Boolean().validate(True), True)
    assert_equal(Boolean().validate(False), False)

    assert_equal(Boolean().validate("true"), True)
    assert_equal(Boolean().validate("false"), False)

    assert_equal(Boolean().validate("1"), True)
    assert_equal(Boolean().validate("0"), False)

    assert_equal(Boolean().validate(1), True)
    assert_equal(Boolean().validate(0), False)

    assert_equal(Boolean(allow_null=True).validate(None), None)
    assert_equal(Boolean(allow_null=True).validate("null"), None)
    assert_equal(Boolean(allow_null=True).validate(""), None)


# Generated at 2022-06-14 14:33:15.041362
# Unit test for method validate of class Array
def test_Array_validate():
    assert Array(min_items=2).validate(["a"]) == ["a"]
    assert Array(max_items=1).validate(["a", "b"]) == ["a"]
test_Array_validate()