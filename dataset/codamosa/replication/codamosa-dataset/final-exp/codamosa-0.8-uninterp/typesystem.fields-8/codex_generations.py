

# Generated at 2022-06-14 14:25:46.543682
# Unit test for constructor of class String
def test_String():
    a = String(allow_blank=False, trim_whitespace=True, max_length=20, min_length=2, pattern='^[a-z]$')
    assert a is not None


# Generated at 2022-06-14 14:25:49.821167
# Unit test for method validate of class Union
def test_Union_validate():
    def UnitTest(validator=None):
        u = Union([Integer(), String()])
        return u.validate(validator)
    assert UnitTest(1.0) == 1
    assert UnitTest("123") == "123"
    try:
        UnitTest(1.)
    except Exception as e:
        assert str(e) == "Did not match any valid type."
ClassName = typing.Union[BaseClass, OtherBaseClass]
ClassName_validator = Union([BaseClass_validator, OtherBaseClass_validator])


# Generated at 2022-06-14 14:25:52.179341
# Unit test for method validate_or_error of class Field
def test_Field_validate_or_error():
    type_field = Field(title='title', description='description')
    val = "123"
    res = type_field.validate_or_error(val)
    assert res.error
    assert isinstance(res.error, ValidationError)

# Generated at 2022-06-14 14:25:57.145989
# Unit test for method validate of class Array
def test_Array_validate():

    my_array = Array(items=[String()])
    my_array.validate([])
    my_array.validate([""], strict=True)
    with pytest.raises(ValidationError):
        my_array.validate([""])
    my_array.validate([""], strict=False)



# Generated at 2022-06-14 14:26:05.102486
# Unit test for method validate of class Array
def test_Array_validate():
    # Array defined with Type as Schema
    field = Array(items=Dict(properties={"name":String(max_length=3)}),required=True,null=True,default={"name":"fds"},description="Array")

    # Valid array
    value = field.serialize([{"name":"fds"},{"name":"fds1"},{"name":"fds2"},{"name":"fds3"},{"name":"fds4"}])
    expected_value = [{"name":"fds"},{"name":"fds"},{"name":"fds"},{"name":"fds"},{"name":"fds"}]
    assert value == expected_value
    value = field.validate(value)
    assert value == expected_value

    # Empty array
    value = field.serialize([])
    expected_value = []
    assert value == expected_value

# Generated at 2022-06-14 14:26:13.085787
# Unit test for method validate of class Choice
def test_Choice_validate():
    from unittest import TestCase
    from unittest.mock import patch

    class test_field_Choice_validate(TestCase):
        @patch("typing.List", spec=True)
        @patch("typing.Tuple", spec=True)
        @patch("typing.Sequence", spec=True)
        @patch("typing.Union", spec=True)
        def test_Choice_validate(self, mock_Union, mock_Sequence, mock_Tuple, mock_List):
            mock_Union.configure_mock(**{"__iter__.return_value": lambda: iter([])})
            mock_Sequence.configure_mock(**{"return_value": "mock_Sequence"})

# Generated at 2022-06-14 14:26:15.624532
# Unit test for method validate_or_error of class Field
def test_Field_validate_or_error():
    test_field = Field()
    test_result = test_field.validate_or_error("hello")
    assert test_result.value == "hello"
    assert not test_result.error

# Generated at 2022-06-14 14:26:22.672418
# Unit test for method validate of class Choice
def test_Choice_validate():
    assert Choice().validate(None, strict=False) is None
    assert Choice().validate(None, strict=True) is None
    assert Choice().validate("", strict=False) is None
    assert Choice().validate("", strict=True) is None
    assert Choice().validate(1, strict=False) is None
    assert Choice().validate(1, strict=True) is None
    

# Generated at 2022-06-14 14:26:33.065928
# Unit test for method serialize of class Array
def test_Array_serialize():
    
    # type
    obj = Array()
    a = obj.serialize(["a"])
    assert(a == ["a"])

    # number
    obj = Array()
    a = obj.serialize([1])
    assert(a == [1])

    # dict
    obj = Array()
    a = obj.serialize([{"a": "b"}])
    assert(a == [{"a": "b"}])

    # dict
    obj = Array(items=String())
    a = obj.serialize(["ab"])
    assert(a == ["ab"])
    
    # None
    obj = Array(items=String())
    a = obj.serialize(None)
    assert(a == None)

test_Array_serialize()


# Generated at 2022-06-14 14:26:36.797760
# Unit test for method __or__ of class Field
def test_Field___or__():
    from typesystem import Field, String, DateTime, Union
    assert (String() | DateTime()) == Union(any_of=[String(), DateTime()])
    assert (String() | Union(any_of=[DateTime()])) == Union(any_of=[String(), DateTime()])



# Generated at 2022-06-14 14:27:00.506764
# Unit test for method validate of class Object
def test_Object_validate():
    print("Unit test for method validate of class Object")

    # Case 1: add_property_schema = true, pattern_property = None
    schema1 = Object(
        properties = {"id": Integer(), "name": String()},
        additional_properties = True,
    )
    data1 = {"id": 10, "name": "John", "age": 20}
    print(schema1.validate(data1), end="\n\n")

    # Case 2: add_property_schema = false, pattern_property = None
    schema2 = Object(
        properties = {"id": Integer(), "name": String(max_length = 8)},
        additional_properties = False,
    )
    data2 = {"id": 10, "name": "John", "age": 20}

# Generated at 2022-06-14 14:27:10.343487
# Unit test for method serialize of class String
def test_String_serialize():
    assert String(format="date").serialize('2020-11-13') == '2020-11-13'
    assert String(format="time").serialize('00:00') == '00:00:00'
    assert String(format="datetime").serialize('2020-11-12T00:00') == '2020-11-12T00:00:00'
    assert String(format="uuid").serialize('77d07c24-4913-11ea-b77f-2e728ce88125') == '77d07c24-4913-11ea-b77f-2e728ce88125'



# Generated at 2022-06-14 14:27:15.071561
# Unit test for method serialize of class String
def test_String_serialize():
    error_msg ="You should call the super() method in your serialize method"
    test1 = True
    try:
        class MyString(String):
            pass
        ms = MyString()
        assert ms.serialize("my_string") == "my_string"
    except AssertionError:
        print(error_msg)
        test1 = False
    try:
        class MyString(String):
            def serialize(self, obj: typing.Any) -> typing.Any:
                pass
        ms = MyString()
        assert ms.serialize("my_string") == "my_string"
    except AssertionError:
        print(error_msg)
    test_cases = [True, test1]

# Generated at 2022-06-14 14:27:15.728277
# Unit test for method validate of class Number
def test_Number_validate():
    number = Number()
    value = 1
    assert number.validate(value) == 1

# Generated at 2022-06-14 14:27:20.786260
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    field = Field()
    assert field.get_default_value() == None
    field = Field(default = "null")
    assert field.get_default_value() == "null"
    field = Field(default = "1")
    assert field.get_default_value() == "1"
    func = lambda: 5
    field = Field(default = func)
    assert field.get_default_value() == 5


# Generated at 2022-06-14 14:27:30.125853
# Unit test for method validate of class Union
def test_Union_validate():
    if __debug__:
        class Foo(Field):
            def validate(self, value,strict=False):
                return value,None
        a=Foo()
        b=Union([a,a],allow_null=True)
        b.validate(None)
        if b.allow_null:
            print("allow null")
        if (b.any_of[0].allow_null ==True) and (b.any_of[1].allow_null==True):
            print("a allow_null and b allow null")
        print("validate null:",b.validate(None))

        print("not null:",b.validate(1))

# Generated at 2022-06-14 14:27:39.856652
# Unit test for method validate of class Union
def test_Union_validate():
    assert Union(any_of=[Boolean(), Float(multiple_of=1.0), Int()]).validate(1) == 1
    assert Union(any_of=[Boolean(), Float(multiple_of=1.0), Int()]).validate(1.0) == 1.0
    assert Union(any_of=[Boolean(), Float(multiple_of=1.0), Int()]).validate(False) == False

    # case: value is None and allow_null is False
    try:
        Union(any_of=[Boolean(), Float(multiple_of=1.0), Int()]).validate(None)
        assert False
    except ValidationError as error:
        assert error.messages() == [Message(text="May not be null.", code="null")]
    # case: value is None and allow_null is True
   

# Generated at 2022-06-14 14:27:48.882051
# Unit test for method validate of class Choice
def test_Choice_validate():
    from hypothesis import given
    from hypothesis.extra.datetime import datetimes
    from hypothesis.strategies import integers
    from datetime import datetime

    assert Choice(choices=[("choice 1", "choice 2")]).validate("choice 1") == "choice 1"
    assert Choice(choices=[("choice 1", "choice 2")]).validate("choice 2") == "choice 2"
    assert Choice(choices=[("1", "2")]).validate("1") == "1"
    assert Choice(choices=[("1", "2")]).validate("2") == "2"
    assert Choice(choices=[("1", "2")]).validate("") == "1"

    assert Choice().validate(None) == None
    assert Choice().validate(1) == 1
    assert Choice().validate(datetime.now())

# Generated at 2022-06-14 14:27:51.525529
# Unit test for method validate of class Choice
def test_Choice_validate():
    try:
        Choice().validate("")
        assert False, "should have thrown"
    except ValidationError:
        pass

# Generated at 2022-06-14 14:28:02.470285
# Unit test for method validate of class Object
def test_Object_validate():
    field = Object()
    field.properties = {
        "name": String(min_length=1, max_length=10),
        "age": Integer(minimum=1),
    }
    field.required = ["name", "age"]
    value = {"name": "Bob", "age": 28}
    assert field.validate(value) == value
    field.allow_null = True
    assert field.validate(None) == None

    # check object properties that are not required
    field = Object()
    field.properties = {
        "name": String(min_length=1, max_length=10),
        "age": Integer(minimum=1),
    }
    field.required = []
    value = {"name": "Bob", "age": 28}
    assert field.validate(value) == value

# Generated at 2022-06-14 14:28:24.592101
# Unit test for method validate of class Array
def test_Array_validate():
    schema = Array([])
    assert schema.validate([]) == []
    assert schema.validate([1]) == [1]
    try:
        schema.validate(None)
        assert 1==2
    except ValidationError as ex:
        assert 1==1

    schema = Array([], min_items=1)
    assert schema.validate([1]) == [1]
    try:
        schema.validate([])
        assert 1==2
    except ValidationError as ex:
        assert 1==1

    schema = Array([], max_items=1)
    assert schema.validate([1]) == [1]
    try:
        schema.validate([1,2])
        assert 1==2
    except ValidationError as ex:
        assert 1==1


# Generated at 2022-06-14 14:28:27.427265
# Unit test for method validate of class String
def test_String_validate():
    string = String()
    assert string.validate_or_error("test").is_valid == True
    
test_String_validate()


# Generated at 2022-06-14 14:28:32.572611
# Unit test for method validate of class Boolean
def test_Boolean_validate():
    bool_field = Boolean()
    bool_field.validate(True)
    bool_field = Boolean()
    bool_field.validate(1)
    bool_field = Boolean()
    bool_field.validate("true")


# Generated at 2022-06-14 14:28:42.305056
# Unit test for method validate of class Union
def test_Union_validate():
    # This is a method test, we do not test individual errors here
    errors = {
        "null": "May not be null.",
        "union": "Did not match any valid type.",
    }
    schema = Union([Array(), Number()])
    schema.allow_null = True
    assert schema.validate(None) is None
    assert schema.validate([1]) == [1]
    assert schema.validate(1) == 1
    assert schema.validate("string-should-fail") == ValidationError(messages=[
        Message(code="union", text=errors['union'])
    ])

test_Union_validate()


# Generated at 2022-06-14 14:28:54.417015
# Unit test for method validate of class Union
def test_Union_validate():
    u=Union([Number()])
    try:
        print(u.validate(None))
    except ValidationError as e:
        print(e)
        assert(str(e)=='null')
    try:
        print(u.validate(True))
    except ValidationError as e:
        print(e)
        assert(str(e)=='union')
    try:
        print(u.validate([1]))
    except ValidationError as e:
        print(e)
        assert(str(e)=='union')
    try:
        print(u.validate(1))
    except ValidationError as e:
        print(e)
        assert(str(e)=='union')

# Generated at 2022-06-14 14:28:58.043091
# Unit test for method validate of class Boolean
def test_Boolean_validate():
    a = Boolean(title="My title", description="My description")
    assert a.validate(False) == False
    assert a.validate(True) == True



# Generated at 2022-06-14 14:29:07.735948
# Unit test for method validate of class Union
def test_Union_validate():
    from fdk_rdf_parser.classes import Literal

    # Test that a subclass of Union will create an instance of Union with the
    # union of any_of and the any_of of the subclass
    expected_any_of = [Literal("a"), Literal("b")]
    expected_default = Literal("def")

    class MyUnion(Union):
        def __init__(self):
            super().__init__(
                any_of=expected_any_of,
                default=expected_default,
                allow_null=False,
            )

    instance = MyUnion()
    assert type(instance) is Union
    assert instance.any_of == expected_any_of
    assert instance.default == expected_default
    assert instance.allow_null is False

    # Verify that the method validate of class Union correctly validates

# Generated at 2022-06-14 14:29:15.381495
# Unit test for method validate of class Union
def test_Union_validate():
    field = Union([
        String(),
        Number()
    ], allow_null=False)
    value, error = field.validate_or_error(None)
    assert error
    assert error.messages()[0].text == "May not be null."
    value, error = field.validate_or_error(1)
    assert not error
    value, error = field.validate_or_error("1")
    assert not error
    value, error = field.validate_or_error([1, 2, 3])
    assert error
    assert len(error.messages()) == len([1, 2, 3])

# Generated at 2022-06-14 14:29:19.527800
# Unit test for method validate of class Choice
def test_Choice_validate():
    testObj = Choice(choices=["test", "test2"])
    assert testObj.validate("test") == "test"
    #assert testObj.validate("test2") == "test2"


# Generated at 2022-06-14 14:29:29.595370
# Unit test for method validate of class Union
def test_Union_validate():
    class FieldA(Field):
        errors = {"null": "May not be null.","type": "Must be of type {}."}

        def __init__(self, **kwargs: typing.Any) -> None:
            super().__init__(**kwargs)
        
        def validate(self, value: typing.Any, *, strict: bool = False) -> typing.Any:
            if value is None and self.allow_null:
                return None
            elif value is None:
                raise self.validation_error("null")
            elif not isinstance(value, int):
                raise self.validation_error("type", type=type(value))
            else:
                return value
    
    class FieldB(Field):
        errors = {"null": "May not be null.","type": "Must be of type {}."}



# Generated at 2022-06-14 14:29:42.896579
# Unit test for method validate of class Union
def test_Union_validate():
    obj = Union(any_of=[Number(), String(),])
    assert obj.validate(None) is None, "this is None and allow_null is True"
    assert obj.validate("foo") is "foo", "this is expected value foo of class str"
    assert obj.validate(123) is 123, "this is expected value 123 of class int"
    try:
        obj.validate(set())
    except ValidationError as e:
        assert '[union]' == str(e)
    else:
        assert False, "this is not None, but allow_null is False"

test_Union_validate()

# Generated at 2022-06-14 14:29:50.051246
# Unit test for method validate of class Union
def test_Union_validate():
    class TestError(Exception):
        pass
    class TestField(Field):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
        def validate(self, value, *, strict : bool = False)->typing.Any:
            if value == 5:
                raise self.validation_error("null")
            else:
                raise TestError()
    class TestField2(Field):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
        def validate(self, value, *, strict : bool = False)->typing.Any:
            if value == 'str':
                raise self.validation_error("null")
            else:
                raise TestError()
    testField = TestField

# Generated at 2022-06-14 14:29:58.872824
# Unit test for method validate of class Union
def test_Union_validate():
    class _ObjectID(Field):
        errors = {"type": "Must be an instance of bson.ObjectID."}

        def validate(self, value: typing.Any, *, strict: bool = False) -> typing.Any:
            if isinstance(value, bson.ObjectId):
                return value
            raise self.validation_error("type")

    def test_objectid_validation(value: typing.Any) -> None:
        schema = Union([_ObjectID(), Integer()]).validate(value)
        assert schema == bson.ObjectId(value)

    test_objectid_validation("5f5e2e5a9fdbde078f89e1cb")
    test_objectid_validation("5f5e2e5a9fdbde078f89e1cb")
    test_

# Generated at 2022-06-14 14:30:12.159709
# Unit test for method validate of class Union
def test_Union_validate():
    field_class = Union(any_of=[Boolean(), Number(minimum=1)])
    try:
        field_class.validate(None)
    except ValidationError as err:
        assert err.messages()[0] == Message(
            text="May not be null.", code="null", key="")
    else:
        assert False
    try:
        field_class.validate(0)
    except ValidationError as err:
        assert err.messages()[0] == Message(
            text="Must be at least 1.", code="minimum", key="")
    else:
        assert False

# Generated at 2022-06-14 14:30:16.501670
# Unit test for method validate of class Choice
def test_Choice_validate():
    class TestChoice(Choice):
        """testing for method validate"""
        def validate(self, value: typing.Any, *, strict: bool = True) -> typing.Any:
            if value is None and self.allow_null:
                return None
            elif value is None:
                raise self.validation_error("null")
            elif value not in Uniqueness([key for key, value in self.choices]):
                if value == "":
                    if self.allow_null and not strict:
                        return None
                    raise self.validation_error("required")
                raise self.validation_error("choice")
            return value
    # TestCase: value is None and this.allow_null is True

# Generated at 2022-06-14 14:30:25.347081
# Unit test for constructor of class Array
def test_Array():
    """ Tests the constructor of class Array """
    arr = Array()
    assert arr.items is None
    assert arr.additional_items is False
    assert arr.min_items is None
    assert arr.max_items is None
    assert arr.unique_items is False

    arr = Array(items=String())
    assert arr.items == String()
    assert arr.additional_items is False
    assert arr.min_items is None
    assert arr.max_items is None
    assert arr.unique_items is False


# Generated at 2022-06-14 14:30:27.802713
# Unit test for method validate of class Union
def test_Union_validate():
    new_instance_of_Union = Union([])
    new_instance_of_Union.validate(value=None, strict=False)


# Generated at 2022-06-14 14:30:31.362377
# Unit test for method __or__ of class Field
def test_Field___or__():
    # imports
    from typesystem.fields import String
    # test
    field = String() | String()
    assert isinstance(field, Union)
    assert field.any_of[0] == String()
    assert field.any_of[1] == String()



# Generated at 2022-06-14 14:30:37.481568
# Unit test for method validate of class Choice
def test_Choice_validate():
    c = Choice(choices=[('A','A'),('B','B')])
    print('choices = ',c.choices)
    try:
        result = c.validate('C')
    except ValidationError as e:
        print('ValidationError = ',e)



Choice(choices=[('A','A'),('B','B')])



# Generated at 2022-06-14 14:30:43.732591
# Unit test for method validate of class Choice
def test_Choice_validate():
    CHOICES = [("1", "one"), ("2", "two"), ("3", "three")]
    field = Choice(choices = CHOICES)
    try:
        field.validate("")
    except ValidationError as e:
        assert e.code == 'required'
    
    try:
        field.validate("4")
    except ValidationError as e:
        assert e.code == 'choice'

    assert field.validate("1") == "1"

# Generated at 2022-06-14 14:30:57.060669
# Unit test for method validate of class Array
def test_Array_validate():
    field = Array(items = None)
    try:
        value, error = field.validate_or_error(["test"])
        assert value == ["test"]
        assert error is None
    except ValidationError:
        assert False
    try:
        field.validate_or_error(None)
        assert False
    except ValidationError:
        pass
    try:
        field.validate_or_error(["test", None])
        assert False
    except ValidationError:
        pass
    field = Array(items = Str())
    try:
        value, error = field.validate_or_error(["test", None])
        assert value == ["test", None]
        assert error is None
    except ValidationError:
        assert False

# Generated at 2022-06-14 14:31:02.318484
# Unit test for method validate of class Union
def test_Union_validate():
    union = Union([Integer(), Float()])

    union.validate(1)
    union.validate(1.0)
    with pytest.raises(ValidationError):
        union.validate("1.0")
    union.validate(None, strict=False)



# Generated at 2022-06-14 14:31:10.981822
# Unit test for method validate of class Object
def test_Object_validate():
    obj = Object(properties={'x': Number(exclusive_minimum=-1, exclusive_maximum=1)}, required=['x'])
    with pytest.raises(ValidationError) as err:
        obj.validate_or_error({'x': 2})
            # assert it has error
    assert str(err.value) == 'Invalid value at [\'x\'], May not be less than -1.'

    with pytest.raises(ValidationError) as err:
        obj.validate_or_error({'x': -2})
            # assert it has error
    assert str(err.value) == 'Invalid value at [\'x\'], May not be greater than 1.'

    with pytest.raises(ValidationError) as err:
        obj.validate_or_error({'x': -1.0})


# Generated at 2022-06-14 14:31:18.232543
# Unit test for method validate of class Boolean
def test_Boolean_validate():
    # Boolean
    test_Boolean_validate_1 = Boolean()
    test_outcome_1 = test_Boolean_validate_1.validate(None)
    assert test_outcome_1 == None
    assert type(test_outcome_1) == type(None)
    test_outcome_2 = test_Boolean_validate_1.validate(False)
    assert test_outcome_2 == False
    assert type(test_outcome_2) == bool
    test_outcome_3 = test_Boolean_validate_1.validate(True)
    assert test_outcome_3 == True
    assert type(test_outcome_3) == bool
    # Allow Null
    test_Boolean_validate_2 = Boolean(allow_null=True)
    test_outcome_

# Generated at 2022-06-14 14:31:21.007926
# Unit test for method validate of class Boolean
def test_Boolean_validate():
    b=Boolean()
    try:
        b.validate(1)
        assert False
    except ValidationError:
        assert True

# Generated at 2022-06-14 14:31:25.408751
# Unit test for method validate of class Array
def test_Array_validate():
    data = [3, 4, 5]
    minimal = Array()
    assert minimal.validate(data) == data

    if 0:
        print("Array.validate succeed -- values are equal")
    else:
        print("Array.validate failed -- values are not equal")





# Generated at 2022-06-14 14:31:30.211774
# Unit test for constructor of class Choice
def test_Choice():
    # If there are no default values, they should be assigned values.
    choice_instance = Choice()
    assert choice_instance.choices == []

    # If there are default values, they should be ignored.
    choice_instance = Choice(choices=["apple", "orange", "grape"])
    assert choice_instance.choices == [("apple", "apple"), ("orange", "orange"), ("grape", "grape")]


# Generated at 2022-06-14 14:31:35.480048
# Unit test for method __or__ of class Field
def test_Field___or__():
    str_f = String()
    int_f = Integer()
    union = str_f | int_f
    assert (
        union.validate(3) == 3 and union.validate('3') == '3' and union.validate(None) == None and union.validate('') == None
    )

# Generated at 2022-06-14 14:31:41.045759
# Unit test for method validate of class Choice
def test_Choice_validate():
    sut = Choice(
        choices=[("1", "1"), ("2", "2"), ("3", "3")],
        allow_null=True,
    )
    assert sut.validate("1") == "1"
    assert sut.validate("2") == "2"
    assert sut.validate("3") == "3"
    assert sut.validate("") is None
    assert sut.validate(None) is None
    with pytest.raises(ValidationError):
        sut.validate("0")
    with pytest.raises(ValidationError):
        sut.validate(0)
    with pytest.raises(ValidationError):
        sut.validate(True)
    with pytest.raises(ValidationError):
        sut.validate

# Generated at 2022-06-14 14:31:46.658103
# Unit test for method validate of class Array
def test_Array_validate():
    test_Array = Array(items = [Str(),Str()],additional_items = False , min_items = 1,max_items = 2)
    test_validate = test_Array.validate(['a','b'])
    assert test_validate == ['a','b']
    
    

test_Array_validate()



# Generated at 2022-06-14 14:31:58.782096
# Unit test for method validate of class Choice
def test_Choice_validate():

    choice_field = Choice(allow_null=True, choices=['a', 'b'])
    assert choice_field.validate('a') == 'a'
    assert choice_field.validate(None) == None
    assert choice_field.validate('c') == None
    assert choice_field.validate(1) == None
    assert choice_field.validate('') == None


# Generated at 2022-06-14 14:32:09.880566
# Unit test for constructor of class String
def test_String():
    # case 1: normal input:
    try:
        S1 = String(default='')
        assert S1.has_default() == True
        assert S1.allow_blank == False
        assert S1.trim_whitespace == True
        assert S1.max_length == None
        assert S1.min_length == None
        assert S1.pattern == None
        assert S1.format == None
    except:
        assert False
    # case 2: abnormal input:
    try:
        S2 = String(max_length=0)
        assert False
    except:
        assert True
    try:
        S3 = String(min_length=-1)
        assert False
    except:
        assert True

# Generated at 2022-06-14 14:32:12.682062
# Unit test for method validate of class Choice
def test_Choice_validate():
    field=Choice(choices=["a", "b"])
    assert field.validate("a")=="a"
    assert field.validate("b")=="b"
    try:
       field.validate("c")
    except ValidationError:
       assert True
    else:
       assert False


# Generated at 2022-06-14 14:32:17.360224
# Unit test for method validate of class Choice
def test_Choice_validate():
    test1 = Choice(choices=[("f", "female"), ("m", "male")])
    assert test1.validate("f") == "f"
    assert test1.validate("female") == ("f", "female")
    assert test1.validate("m") == "m"
    assert test1.validate("male") == ("m", "male")
    assert test1.validate(None) == None
    assert test1.validate(0) == "f"
    assert test1.validate(1) == "m"
    assert test1.validate([]) == "f"
    assert test1.validate(["f", "m"]) == "f"
    assert test1.validate(["f", "m"], strict=True) == None


# Generated at 2022-06-14 14:32:20.207155
# Unit test for method validate of class String
def test_String_validate():
    input_value = '123'
    string = String(format = 'int')
    string_validate = string.validate(input_value)
    assert string_validate == 123

# Generated at 2022-06-14 14:32:29.480899
# Unit test for method validate of class Choice
def test_Choice_validate():
    test_field = Choice(choices=["one", "two"])
    try:
        test_field.validate(None)
        assert False
    except ValidationError:
        assert True
    assert test_field.validate("one") == "one"
    try:
        test_field.validate("three")
        assert False
    except ValidationError:
        assert True
    try:
        assert test_field.validate(None, strict=False) == None
    except ValidationError:
        assert False
    try:
        assert test_field.validate("") == None
    except ValidationError:
        assert False



# Generated at 2022-06-14 14:32:31.635082
# Unit test for method __or__ of class Field
def test_Field___or__():
    field = Field(title = "")
    union = field | field
    assert union.any_of == [field, field]



# Generated at 2022-06-14 14:32:38.186213
# Unit test for method validate of class Array
def test_Array_validate():
    array = Array(items = [String(),Number(),Integer()], min_items = 2, max_items = 2)
    validated = array.validate(['hello', 5.66, 90], strict = False)
    assert validated == ['hello', 5.66]
    with pytest.raises(ValidationError):
        array.validate([1,3,4])
    with pytest.raises(ValidationError):
        array.validate([])
    with pytest.raises(ValidationError):
        array.validate(5)

# Generated at 2022-06-14 14:32:43.531842
# Unit test for method validate of class Union
def test_Union_validate():
    class Car(Object):
        name = String()

    class Bike(Object):
        name = String()

    class Human(Object):
        name = String()

    class RollingStock(Union):
        any_of = [Car, Bike]

    schema = RollingStock()

    schema.validate(Car(name="Volvo"))


# Generated at 2022-06-14 14:32:44.345766
# Unit test for method validate of class String
def test_String_validate():
    pass

# Generated at 2022-06-14 14:33:04.207717
# Unit test for method validate of class Object
def test_Object_validate():
    field = Object(properties={
        'name': Text(required=True),
        'relation': Text(required=True),
        'age': Integer(required=True)
    })
    obj = field.validate({
        'name': 'User1',
        'age': 10,
        'relation': 'user'
    })
    assert obj == {
        'name': 'User1',
        'age': 10,
        'relation': 'user'
    }

    obj = field.validate({
        'name': '',
        'age': 10,
        'relation': 'user'
    })
    assert obj == {
        'name': '',
        'age': 10,
        'relation': 'user'
    }


# Generated at 2022-06-14 14:33:08.254353
# Unit test for method validate of class Number
def test_Number_validate():
    ans = Number().validate(2)
    assert ans == 2
    ans = Number().validate(3.3)
    assert ans == 3.3
    ans = Number().validate("3")
    assert ans == 3

# Generated at 2022-06-14 14:33:19.901159
# Unit test for method validate of class Boolean
def test_Boolean_validate():
    field = Boolean()
    assert(field.validate(True) == True)
    assert(field.validate(False) == False)
    assert(field.validate(None) == None)
    try:
        field.validate('')
    except ValidationError:
        pass
    else:
        assert(False and "ValidationError should be raised")

    field = Boolean(allow_null=True)
    assert(field.validate(None) == None)

    field = Boolean(allow_null=False)
    try:
        field.validate(None)
    except ValidationError:
        pass
    else:
        assert(False and "ValidationError should be raised")

    field = Boolean(allow_null=True)
    assert(field.validate(True) == True)