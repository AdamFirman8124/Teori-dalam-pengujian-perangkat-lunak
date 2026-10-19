

# Generated at 2022-06-14 14:25:01.673920
# Unit test for method __or__ of class Field
def test_Field___or__():
    from typesystem.fields import (
        Boolean,
        Date,
        DateTime,
        Integer,
        String,
        Union,
    )

    field_A = Boolean()
    field_B = Integer()
    field_C = String()

    assert (field_A | field_B).any_of == [field_A, field_B]
    assert (field_A | (field_B | field_C)).any_of == [field_A, field_B, field_C]
    assert (field_A | Date()).any_of == [field_A, Date()]
    assert (field_A | DateTime()).any_of == [field_A, DateTime()]

# Generated at 2022-06-14 14:25:04.216025
# Unit test for method serialize of class String
def test_String_serialize():
    str_obj = String(format="date")
    assert str_obj.serialize(datetime.date(2020,4,4)) == "2020-04-04"

# Generated at 2022-06-14 14:25:13.553873
# Unit test for method validate of class Union
def test_Union_validate():
    def test_Union_validate_inner(value):
        a = Text()
        b = Integer()
        c = Union([a, b], required=True)
        return c.validate(value)
    params = {
        'value': [
            'hi',
            1,
            2.1,

        ]
    }
    answers = {
        'value': [
            'hi',
            1,
            None
        ]
    }
    assert all([test_Union_validate_inner(value) == answers['value'][i] for i,value in enumerate(params['value'])])



# Generated at 2022-06-14 14:25:15.368117
# Unit test for method serialize of class Array
def test_Array_serialize():
    A = Array(items=Integer)
    a = A.serialize([1, 'c']) 
    assert a == [1, None]

# Generated at 2022-06-14 14:25:19.804951
# Unit test for method validate of class String
def test_String_validate():
    assert(String(title="name", description="", format="date", allow_null=True).validate(None) == None)
    assert(String(title="name", description="", format="date", allow_null=True).validate(None, strict=False) == None)
    assert(String(title="name", description="", format="date", allow_null=True).validate(None, strict=True) == None)
    assert(String(title="name", description="", format="time", allow_null=False).validate(None) == None)
    assert(String(title="name", description="", format="time", allow_null=False).validate(None, strict=False) == None)

# Generated at 2022-06-14 14:25:23.866347
# Unit test for method serialize of class String
def test_String_serialize():
    test = String(format="date")
    assert test.serialize("2019-04-06") == "2019-04-06"
    assert test.serialize("2019-02-29") == "2019-02-29"
    assert test.serialize("asdf") == "asdf"


# Generated at 2022-06-14 14:25:28.963746
# Unit test for method validate of class Choice
def test_Choice_validate():
    field = Choice(
        choices=[("a", "A"), ("b", "B"), ("c", "C")]
    )
    value = "a"
    field.validate(value)
    assert value == "a"
    value = "x"
    with pytest.raises(ValidationError):
        field.validate(value)



# Generated at 2022-06-14 14:25:38.192743
# Unit test for method validate of class Object
def test_Object_validate():
    """
    Test validation method for instances of class Object.
    """
    import json
    import sys

    from json_schema_validator.utility import Message
    from json_schema_validator.utility import Uniqueness
    from json_schema_validator.utility import ValidationError

    # Validate validating:
    #   value = {'x': 'a'}
    #   properties = {'x': String()}
    to_validate = {'x': 'a'}
    my_Object = Object(properties={'x': String()})
    my_Object.validate(value=to_validate)

    # Validate validating:
    #   value = {'x': 'a'}
    #   properties = {'x': String(required=True)}

# Generated at 2022-06-14 14:25:44.093652
# Unit test for method validate of class Object
def test_Object_validate():
    from py_json_schema import field
    from py_json_schema import error
    from py_json_schema.field import Field
    from py_json_schema.field import Integer
    from py_json_schema.field import String
    from py_json_schema.field import List

    print("# Test Object: validate: case 1")
    # input

# Generated at 2022-06-14 14:25:55.826801
# Unit test for method validate of class Union
def test_Union_validate():
    v1 = String()
    v2 = Boolean()
    v3 = Integer()
    u = Union([v1, v2, v3])

    assert u.validate("test") == "test"
    assert u.validate(False) is False
    assert u.validate(4) == 4

    with pytest.raises(ValidationError) as exc_info:
        u.validate(5.5)
    assert exc_info.value.detail() == "Did not match any valid type."

    u2 = Union([v1, v2])
    with pytest.raises(ValidationError) as exc_info:
        u2.validate(3)
    assert exc_info.value.detail() == "Must be a string."



# Generated at 2022-06-14 14:26:35.269255
# Unit test for method validate of class Array
def test_Array_validate():
    # test 1
    schema = Array(Type(type_=int))
    data = [1, 2, 3]
    assert schema.validate(data) == data

    # test 2
    data = [1, "testing", 3]
    with pytest.raises(ValidationError) as error:
        schema.validate(data)
    assert error.value.messages()[0].text == "Must be an integer."

    # test 3
    data = {"1": 1, "2": 2, "3": 3}
    with pytest.raises(ValidationError) as error:
        schema.validate(data)
    assert error.value.messages()[0].text == "Must be an array."

    # test 4

# Generated at 2022-06-14 14:26:43.424879
# Unit test for constructor of class Choice
def test_Choice():
    try:
        choices = Choice(choices=[])
        assert False
    except:
        assert True

    choices = Choice(choices=['a', 'b', 'c'])
    assert choices.choices == [('a', 'a'), ('b', 'b'), ('c', 'c')]

    choices = Choice(choices=[('a', 'Aa'), ('b', 'Bb'), ('c', 'Cc')])
    assert choices.choices == [('a', 'Aa'), ('b', 'Bb'), ('c', 'Cc')]

    choices = Choice(choices=[('a', 'Aa')])
    assert choices.choices == [('a', 'Aa')]



# Generated at 2022-06-14 14:26:47.032843
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    global Field
    class DummyField(Field):
        def validate(self, value):
            return 'My validated value'
    field = DummyField()
    assert field.allow_null is False
    assert field.has_default() is False
    assert field.get_default_value() is None
    assert field.validate('raw value') == 'My validated value'


# Generated at 2022-06-14 14:26:59.418919
# Unit test for method validate of class Object
def test_Object_validate():
    #part1: for p in properties
    properties = {
                "number":Integer(minimum = 2,maximum = 8),
                "url":URL(allow_null=False),
            }
    #part2: for pp in pattern_properties
    pattern_properties = {
                ".*":String(max_length = 5),
            }
    #part3: for ap in additional_properties
    additional_properties = True
    min_properties = 2
    max_properties = 4
    required = ["number","url"]
    field = Object(allow_null=False,properties = properties,
                               pattern_properties=pattern_properties,
                               additional_properties=additional_properties,
                               min_properties=min_properties,
                               max_properties=max_properties,
                               required=required)

# Generated at 2022-06-14 14:27:03.748239
# Unit test for method validate of class Choice
def test_Choice_validate():
    choice = Choice()
    choice.choices = [("a","b")]
    assert choice.validate("a") == "a"
    
    

# Generated at 2022-06-14 14:27:09.189656
# Unit test for method validate of class Choice
def test_Choice_validate():
    testObj = Choice(choices=["a", "b", "c"])
    assert testObj.validate("a") == "a"
    assert testObj.validate("b") == "b"
    assert testObj.validate("c") == "c"
    assert testObj.validate(1) == "1"



# Generated at 2022-06-14 14:27:18.244251
# Unit test for method validate of class Array
def test_Array_validate():
    assert Array(items=Integer()).validate([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert Array(items=Integer()).validate(["1", "2"]) == [1, 2]
    assert Array(items=Integer()).validate(["1", "2", "3", "4"]) == [1, 2, 3, 4]
    assert Array(items=Integer()).validate([1, "2", 3, "4"]) == [1, 2, 3, 4]
    assert Array(items=Integer()).validate(["1.1", "2.2"]) == [1, 2]
    assert Array(items=Integer()).validate([1.1, 2.2]) == [1, 2]
    assert Array(items=Integer()).validate

# Generated at 2022-06-14 14:27:22.729885
# Unit test for constructor of class String
def test_String():
    # Test __init__
    string = String(allow_blank=True, trim_whitespace=True, max_length=None, min_length=None, pattern=None, format=None)

    # Test function validate
    isNotNull = string.validate("abc")
    NotNull = string.validate(None)
    isNull = string.validate("", strict=True)
    Null = string.validate(None, strict=True)
    value = string.validate("", strict=False)
    assert isNotNull == "abc"
    assert NotNull is None
    assert isNull == ""
    assert Null == ""
    assert value == "" 

    # Test function serialize
    value = string.serialize(None)
    assert value is None



# Generated at 2022-06-14 14:27:27.457534
# Unit test for constructor of class String
def test_String():
    try:
        String(
            allow_blank=False, trim_whitespace=True, max_length=2, min_length=1, pattern="", format="datetime"
        )
        assert True
    except AssertionError:
        assert False


# Generated at 2022-06-14 14:27:37.485020
# Unit test for method validate of class Object
def test_Object_validate():
    from decimal import Decimal
    from copy import deepcopy
    import uuid

# Generated at 2022-06-14 14:27:52.958074
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    class MyField(Field):
        pass
    f = MyField(default=5)
    assert f.get_default_value() == 5
    f = MyField()
    assert f.get_default_value() is None
    f = MyField(default=lambda : 5)
    assert f.get_default_value() == 5
    f = MyField(default=lambda : {2 : 3})
    assert f.get_default_value() == {2 : 3}

# Generated at 2022-06-14 14:27:54.612938
# Unit test for method serialize of class Array
def test_Array_serialize():
    field=Array(
        items=[String(min_length=5), Integer()],
    )
    result=field.serialize([1, 2])
    assert result == ['1', 2]



# Generated at 2022-06-14 14:27:56.214640
# Unit test for method __or__ of class Field
def test_Field___or__():
    assert (Field() | Field()) is not None
#



# Generated at 2022-06-14 14:28:05.427607
# Unit test for method validate of class Object
def test_Object_validate():
    price_schema = Field(type="number", minimum=0.00, exclusive_minimum=True)
    description_schema = Field(type="string")
    object_schema = Object(
        properties={"price": price_schema, "description": description_schema}
    )
    raw_value1 = {"price": 10, "description": "abc"}
    raw_value2 = {"price": -1, "description": "abc"}
    raw_value3 = {"price": 10, "description": "abc", "other": "other"}
    raw_value4 = {"price": 10, "description": "abc", "other": "other", "other2": "other2"}


# Generated at 2022-06-14 14:28:06.503559
# Unit test for method validate of class Choice
def test_Choice_validate():
    a=Choice()
    assert a.validate(1) == None


# Generated at 2022-06-14 14:28:08.027523
# Unit test for method validate of class Choice
def test_Choice_validate():
    string = "123"
    c = Choice(choices = (("123", "123"),("456","456")))
    assert c.validate(string) == string


# Generated at 2022-06-14 14:28:10.210716
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    field = Field(default="default value")
    assertField = field.get_default_value() == "default value"



# Generated at 2022-06-14 14:28:13.114218
# Unit test for constructor of class Const
def test_Const():
    is_const = Const(const=True)
    assert is_const.validate(value=True) == True
    assert is_const.validate(value=False) != False


# Generated at 2022-06-14 14:28:19.587212
# Unit test for method __or__ of class Field
def test_Field___or__():
    from unittest import TestCase, mock
    from typesystem.unittests.utils import assert_equal

    class Foo(Field):

        def get_default_value(self):
            return "foo"

    class Bar(Field):

        def get_default_value(self):
            return "bar"

    foo = Foo()
    bar = Bar()

    def test__or__():
        assert_equal(
            repr(foo | bar),
            """\
Union(
    any_of=[
        Foo(),
        Bar(),
    ],
)"""
        )
        assert_equal(
            repr(foo | bar | foo),
            """\
Union(
    any_of=[
        Foo(),
        Bar(),
        Foo(),
    ],
)"""
        )

        t = foo | bar
        assert_equal

# Generated at 2022-06-14 14:28:30.365115
# Unit test for method validate of class Number
def test_Number_validate():
    Numeric_value_test = Number()
    assert Numeric_value_test.validate(22.747) == 22.747
    assert Numeric_value_test.validate(22) == 22
    assert Numeric_value_test.validate(22.0) == 22
    assert Numeric_value_test.validate(-22.747) == -22.747
    assert Numeric_value_test.validate(-22) == -22
    assert Numeric_value_test.validate(-22.0) == -22
    assert Numeric_value_test.validate(inf) is None
    assert Numeric_value_test.validate(-inf) is None
    assert Numeric_value_test.validate(nan) is None
    assert Numeric_value_test.validate(20.1) != 20



# Generated at 2022-06-14 14:28:50.379099
# Unit test for method validate of class Choice
def test_Choice_validate():
    chc = Choice(choices=[("key","value")], allow_null=True)
    print(chc.validate("value"))
    print(chc.validate("key"))


# Generated at 2022-06-14 14:28:52.646920
# Unit test for constructor of class Const
def test_Const():
    constVal = 42
    c = Const(constVal)
    assert c.const == 42


# Generated at 2022-06-14 14:28:59.286218
# Unit test for method validate of class Choice
def test_Choice_validate():
    choice = Choice(required=False, allow_null=True)
    assert choice.validate(None) == None
    assert choice.validate('0') == '0'
    assert choice.validate('1') == '1'
    assert choice.validate('2') == '2'
    assert choice.validate('3') == '3'
    assert choice.validate('') == None


# Generated at 2022-06-14 14:29:02.622176
# Unit test for method validate of class Array
def test_Array_validate():
    data = {'a': [1,2,3], 'b': 4}
    array = Array(items=Integer(), unique_items=True)
    array.validate(data)



# Generated at 2022-06-14 14:29:05.647284
# Unit test for method validate of class Choice
def test_Choice_validate():
    try:
        Choice(choices=["male", "female"]).validate("")
    except ValidationError as e:
        assert e.code == "required"
    else:
        assert False



# Generated at 2022-06-14 14:29:15.873265
# Unit test for method validate of class Choice
def test_Choice_validate():
    # Test with empty list of choices
    empty_choice_field = Choice(name='empty_choice_field')
    assert empty_choice_field.validate('A') == 'A'
    assert empty_choice_field.validate('1') == '1'
    try:
        assert empty_choice_field.validate('') is None
    except ValidationError:
        assert True
    # Test with null value and allow_null is True
    Choice_allow_null_field = Choice(name='Choice_allow_null_field', allow_null=True)
    assert Choice_allow_null_field.validate('') is None
    assert Choice_allow_null_field.validate(None) is None
    assert Choice_allow_null_field.validate('A') == 'A'
    assert Choice_allow_null_

# Generated at 2022-06-14 14:29:19.975759
# Unit test for method validate of class Array
def test_Array_validate():
    # Initialization of the class
    array = Array(
        items = None,
        additional_items = False,
        min_items = 1,
        max_items = None,
        exact_items = None,
        unique_items = True
    )
    # Initialization of the value
    value = [1, 2, 3, 5, 4]
    # Validate the value
    validated_value = array.validate(value, strict=True)
    # Print the validated value
    print(validated_value)
# Call the function
test_Array_validate()

"""
Exception
    ValidationError
"""

# Generated at 2022-06-14 14:29:26.995459
# Unit test for method validate of class Choice
def test_Choice_validate():
    choices = [1,2,3]
    new_choice = type(str("ChoiceTest"), (Choice,), {"choices": choices})
    choice = new_choice()
    assert choice.validate(2) == 2
    assert choice.validate(None) == None
    with pytest.raises(ValidationError, match="This field is required."):
        choice.validate(None)
    with pytest.raises(ValidationError, match="Not a valid choice."):
        choice.validate(4)


# Generated at 2022-06-14 14:29:34.891579
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    class FieldInherited(Field):
        def validate(self, value, *, strict = False):
            pass

    field = FieldInherited()

    # case: field.default attr is a function
    # in this case the value returned will be a function
    default_function = lambda: "default function"
    field.default = default_function
    assert callable(field.get_default_value())

    # case: field.default attr is a simple value
    field.default = "simple value"
    assert not callable(field.get_default_value())
    assert field.get_default_value() == "simple value"

    # case: field.default attr is None
    field.default = None
    assert field.get_default_value() is None

    # case: field.default attr doesn't exists
   

# Generated at 2022-06-14 14:29:37.572185
# Unit test for constructor of class Const
def test_Const():
    test_schema = Const("test", description="Test")
    assert test_schema.const == "test"


# Generated at 2022-06-14 14:29:57.284059
# Unit test for method validate of class Object
def test_Object_validate():
    from gcdt_ramuda.util import set_logging, CRITICAL
    set_logging(logging.CRITICAL)
    
    properties = {"a": Boolean(), "b": Integer()}
    pattern_properties = {"c": Boolean()}
    additional_properties = False
    min_properties = None
    max_properties = None
    required = None
    value = {
        "a": True,
        "b": 3,
        "c": False,
        "d": False,
    }
    obj = Object(properties=properties, pattern_properties=pattern_properties, additional_properties=additional_properties, min_properties=min_properties, max_properties=max_properties, required=required)
    obj.validate(value, strict=False)


# Generated at 2022-06-14 14:30:04.781938
# Unit test for method validate of class Choice
def test_Choice_validate():
    field = Choice(choices=[('a', 'a'), ('b', 'b')])
    assert field.validate('a') == 'a'
    with pytest.raises(ValidationError):
        field.validate(1)
    with pytest.raises(ValidationError):
        field.validate('c')
    with pytest.raises(ValidationError):
        field.validate(None)


# Generated at 2022-06-14 14:30:13.566914
# Unit test for method validate of class Choice
def test_Choice_validate():
    #initializes a new instance of Choice
    choice = Choice(name='test')
    #initializes the variable value
    value = "choice1"
    #initializes choice's choices to contain two tuples
    choice.choices = [('choice1', 'Choice 1'), ('choice2', 'Choice 2')]
    #sets the variable value to choice's method validate(value)
    value = choice.validate(value=value)
    #assert that the value of value is equal to the value set
    assert value == "choice1"


# Generated at 2022-06-14 14:30:22.367121
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    str1 = 'str1'
    str2 = 'str2'
    num1 = 1
    num2 = 2
    f1 = Field(title=str1,description=str2,default=num1,allow_null=True)
    assert isinstance(f1.get_default_value(),int)
    assert f1.get_default_value() == num1
    f2 = Field(title=str1,description=str2,default=num2,allow_null=False)
    assert isinstance(f1.get_default_value(),int)
    assert f2.get_default_value() == num2
    f3 = Field(title=str1,description=str2,allow_null=True)
    assert f3.get_default_value() is None

# Generated at 2022-06-14 14:30:25.500984
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():

    class DummyField(Field):
        default = 'my default'

    field = DummyField()
    assert field.get_default_value() == 'my default'

# Generated at 2022-06-14 14:30:31.554148
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    """
    Test case to test method get_default_value of class Field
    """
    given_default_value=5
    given_default_type=int
    test_field=Field(default=given_default_value)
    assert test_field.get_default_value()==given_default_value
    assert isinstance(test_field.get_default_value(),given_default_type)
    assert test_field.has_default()==True

# Generated at 2022-06-14 14:30:42.636472
# Unit test for method validate of class Array
def test_Array_validate():

    def __init__(
        self,
        *,
        items: typing.Union[Field, typing.Sequence[Field]] = None,
        additional_items: typing.Union[Field, bool] = False,
        min_items: int = None,
        max_items: int = None,
        exact_items: int = None,
        unique_items: bool = False,
        **kwargs: typing.Any,
    ) -> None:
        super().__init__(**kwargs)

        items = list(items) if isinstance(items, (list, tuple)) else items

        assert (
            items is None
            or isinstance(items, Field)
            or (isinstance(items, list) and all(isinstance(i, Field) for i in items))
        )

# Generated at 2022-06-14 14:30:47.292302
# Unit test for constructor of class Choice
def test_Choice():
    # This unit test was written to test the constructor of class Choice
    choice = Choice(choices = ["1", "2", "3"])
    assert choice.allow_null == False
    assert choice.choices == [("1", "1"), ("2", "2"), ("3", "3")]
    assert choice.allow_blank == False
    assert choice.default == None


# Generated at 2022-06-14 14:30:50.662980
# Unit test for method validate of class Choice
def test_Choice_validate():
    a = Choice(choices = [("a","a"),("b","b")])
    assert a.validate("a") == "a"
    assert a.validate(None) == None
    assert a.validate("c") == "c"


# Generated at 2022-06-14 14:30:52.539397
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
  n_instance = Field()
  n_instance.default = 10
  assert n_instance.get_default_value() == 10


# Generated at 2022-06-14 14:31:11.773769
# Unit test for method validate of class String
def test_String_validate():
    st = String(max_length=4,min_length=2,pattern=r"^[A-Z]+$")
    assert st.validate("ISI")


# Generated at 2022-06-14 14:31:18.683884
# Unit test for method validate of class Object
def test_Object_validate():
    schema = Object(
            properties={
                "name": String(),
                "age": Integer(),
                "is_cool": Boolean(),
                "favorite_color": Choice(choices=["red", "green", "blue"]),
            },
            required=["name", "age"],
            additional_properties=False,
        )
    input_obj={"name": "John", "age": 3, "is_cool": True, "favorite_color": "blue"}
    output_obj=schema.validate(input_obj, strict=True)
    expected_obj={"name": "John", "age": 3, "is_cool": True, "favorite_color": "blue"}
    assert output_obj==expected_obj

test_Object_validate()


# Generated at 2022-06-14 14:31:21.569053
# Unit test for method validate of class Choice
def test_Choice_validate():
    test = Choice(choices=[("a","a"),("b","b"),("c","c")])
    assert test.validate("a") == "a"
    assert test.validate("b") == "b"
    assert test.validate("c") == "c"
    assert test.validate(None) == None
    try:
        test.validate("d")
    except ValidationError:
        pass


# Generated at 2022-06-14 14:31:27.385776
# Unit test for method validate of class Object
def test_Object_validate():
    field = Object()
    # value is None
    try:
        field.validate(None)
    except ValidationError as exc:
        assert str(exc) == "null"
    # value is int
    try:
        field.validate(0)
    except ValidationError as exc:
        assert str(exc) == "type"
    # value is dict
    assert field.validate({}) == dict()



# Generated at 2022-06-14 14:31:32.544682
# Unit test for method validate of class Choice
def test_Choice_validate():
    Choice(choices=["laptop","desktop"]).validate("laptop")
    Choice(choices=[("laptop", "laptop"),("desktop", "desktop")]).validate("laptop")
    #>>> Choice(choices=[("laptop", "laptop"),("desktop", "desktop")]).validate("laptop")
    #'laptop'
    with pytest.raises(ValidationError) as excinfo:
        Choice(choices=["laptop","desktop"]).validate("Cellphone")
    assert "Not a valid choice" in str(excinfo.value)



# Generated at 2022-06-14 14:31:38.810961
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    class TestField(Field):
        def __init__(self, addition: int = 0):
            self.addition = addition
        def get_default_value(self):
            default_value = Field.get_default_value(self)
            return default_value + self.addition
    testField = TestField(addition=5)
    testField.default = 2
    assert testField.get_default_value() == 7
## Unit tests for method __or__

# Generated at 2022-06-14 14:31:41.798117
# Unit test for method validate of class Array
def test_Array_validate():
    array = Array(items = Number, additional_items = False, min_items = 2, max_items = 4, unique_items = False)
    assert array.validate([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

# Generated at 2022-06-14 14:31:53.836782
# Unit test for method validate of class String
def test_String_validate():
    assert(String().validate("test")=="test")
    assert(String(allow_null=True).validate(None)==None)
    assert(String(allow_blank=True).validate("")=="")
    s = String(min_length=1)
    try:
        s.validate("")
    except ValidationError as error:
        assert(error.code=="min_length")
    try:
        s.validate(None)
    except ValidationError as error:
        assert(error.code=="type")
    assert(String(pattern="\d+").validate("123")=="123")
    try:
        s.validate("abc")
    except ValidationError as error:
        assert(error.code=="pattern")
    s = String(format="uuid")
   

# Generated at 2022-06-14 14:32:01.218306
# Unit test for method __or__ of class Field
def test_Field___or__():
    field_a, field_b, field_c, field_d = [typesystem.String() for _ in range(4)]
    assert repr(field_a | field_b) == repr(typesystem.Union([field_a, field_b]))
    assert repr(field_a | field_b | field_c) == repr(typesystem.Union([field_a, field_b, field_c]))
    assert repr(field_a | (field_b | field_c)) == repr(typesystem.Union([field_a, field_b, field_c]))
    assert repr(((field_a | field_b) | field_c) | field_d) == repr(typesystem.Union([field_a, field_b, field_c, field_d]))
# End unit test for method __or__ of class Field

# Generated at 2022-06-14 14:32:11.200363
# Unit test for method validate of class Choice
def test_Choice_validate():
    """
    Test method Choice.validate
    """
    from rapydscript.py2js.ast import JSVarDef
    from rapydscript.py2js.ast_util import node_to_js

    obj = Choice(choices=['0', '1', '2'])
    # Test with value=None
    value = None
    result = obj.validate(value)
    assert result == None

    value = '0'
    result = obj.validate(value)
    assert result == value

    value = '6'
    try:
        result = obj.validate(value)
    except ValidationError as error:
        assert True

    # Test with value=JSVarDef('var_name')
    value = JSVarDef('var_name')

# Generated at 2022-06-14 14:32:22.224173
# Unit test for constructor of class Const
def test_Const():
    schema = Const(3)
    try:
        schema.validate(3)
    except ValidationError:
        assert False, "validate() should succeed on 3"
    try:
        schema.validate(4)
        assert False, "validate() shoudn't succeed on 4"
    except ValidationError:
        pass

# Unit tests for validate of class Array

# Generated at 2022-06-14 14:32:29.034601
# Unit test for method validate of class Choice
def test_Choice_validate():
    emptyChoice = Choice(choices=[('a', 'b'), ('c', 'd')])
    emptyChoice.validate(value='a')
    emptyChoice.validate(value='c')
    with pytest.raises(ValidationError) as excinfo:
        emptyChoice.validate(value='d')
        
    assert excinfo.value.code == "choice"



# Generated at 2022-06-14 14:32:31.292199
# Unit test for method validate of class Choice
def test_Choice_validate():
    # case 1: input value is not none and is not in choice
    choice = Choice(choices=['ENUM1', 'ENUM2'])
    assert choice.validate('ENUM3') == None
    # case 2: input value is None and not allowed null
    choice = Choice(choices=['ENUM1', 'ENUM2'])
    assert choice.validate(None) == None



# Generated at 2022-06-14 14:32:39.840107
# Unit test for method validate of class Object
def test_Object_validate():
    test_schema = Object()
    result = test_schema.validate({'foo': 'bar'})
    assert result == {'foo': 'bar'}

    test_schema = Object()
    with pytest.raises(ValidationError):
        result = test_schema.validate({'foo': 'bar'}, strict=True)
    
    test_schema = Object(additional_properties=False)
    with pytest.raises(ValidationError):
        result = test_schema.validate({'foo': 'bar'})
    
    test_schema = Object(additional_properties=False)
    with pytest.raises(ValidationError):
        result = test_schema.validate({'foo': 'bar'}, strict=True)
    
    test_schema = Object

# Generated at 2022-06-14 14:32:44.004594
# Unit test for method validate of class Choice
def test_Choice_validate():
    choices = [('123', '123'), ('456', '456'), ('789', '789')]
    validate_obj = Choice(choices = choices)
    result = validate_obj.validate('123')
    assert result == '123'


# Generated at 2022-06-14 14:32:48.119002
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    from typesystem.fields import String
    Field().get_default_value() == None
    String(default="test").get_default_value().lower() == "test"
    String(default="test").get_default_value().lower() == "test"



# Generated at 2022-06-14 14:32:50.678483
# Unit test for method validate of class Array
def test_Array_validate():
    class Test(Array):
        pass
    test = Test(items=String())
    assert test.validate(['a', 'b']) == ['a', 'b']

# Generated at 2022-06-14 14:33:03.779557
# Unit test for constructor of class Array
def test_Array():
    a = Array()
    assert a.allow_null is False
    assert a.error_messages is None
    assert a.default is None
    assert a.description is None
    assert a.title is None

    items = Field()
    additional_items = Field()
    min_items = 1
    max_items = 10
    exact_items = 5
    unique_items = True
    a = Array(items=items,additional_items=additional_items,min_items=min_items,max_items=max_items,exact_items=exact_items,unique_items=unique_items)
    assert a.allow_null is False
    assert a.error_messages is None
    assert a.default is None
    assert a.description is None
    assert a.title is None
    assert a.items == items

# Generated at 2022-06-14 14:33:08.687499
# Unit test for method validate of class String
def test_String_validate():
    field = String()
    assert field.validate('') == ''
    field = String(allow_null=True)
    assert field.validate(None) == None
    field = String(allow_null=True, allow_blank=True)
    assert field.validate(None) == ''



# Generated at 2022-06-14 14:33:13.210549
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    # Test case data
    Field_data = [
        ('', '', True, None),
        ('field_1', '', False, 'field_1'),
        ('field_2', '', False, 'field_2')
    ]
    Field_results = []
    # Loop through the data
    for Field_test in Field_data:
        # Setup test
        field = Field(
            title = Field_test[0],
            description = Field_test[1],
            allow_null = Field_test[2])
        # Perform the test
        test_result = (field.get_default_value() == Field_test[3])
        Field_results.append(test_result)
    # Return the results
    return Field_results
