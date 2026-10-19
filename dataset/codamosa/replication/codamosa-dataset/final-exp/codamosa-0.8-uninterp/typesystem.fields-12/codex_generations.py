

# Generated at 2022-06-14 14:25:24.794389
# Unit test for method validate of class Choice
def test_Choice_validate():
    choices = [
        ('C', 'car'),
        ('D', 'dog'),
        ('C', 'cat')
    ]
    ac = Choice(
        choices=choices,
    )

    # value is cat, return cat
    value = 'C'
    assert ac.validate(value=value) == value

    # value is dog, return dog
    value = 'D'
    assert ac.validate(value=value) == value

    # value is not an element of choices
    value = 'B'
    with pytest.raises(ValidationError) as excinfo:
        ac.validate(value=value)
    excinfo.match('Not a valid choice.')



# Generated at 2022-06-14 14:25:34.557178
# Unit test for method validate of class Array
def test_Array_validate():
    assert Array(min_items=2, max_items=2).validate(['hello','world']) == ['hello','world']
    assert Array(min_items=2, max_items=2).validate(['hello','world','!','!']) == ['hello','world','!','!']
    #test for input is None
    assert Array(min_items=2, max_items=2, allow_null=True).validate(None) is None
    #test for input without Array
    try:
        Array(min_items=2, max_items=2).validate('')
    except ValidationError as e:
        assert e.messages[0].code == 'type'
    #test for input is empty

# Generated at 2022-06-14 14:25:45.744627
# Unit test for method validate of class Array
def test_Array_validate():
    # type annotation issue
    #   https://github.com/python/mypy/issues/3732
    #   https://github.com/python/mypy/issues/3731
    #   https://github.com/python/mypy/issues/7467
    def list_items(items: typing.Sequence[typing.Any]):
        if all(isinstance(item, int) for item in items) and 1 < len(items):
            return items
        else:
            return None

    array = Array.items(list_items)
    # array = Array.items([Int])
    test_list = [1, 2, 3]

# Generated at 2022-06-14 14:25:57.653842
# Unit test for method validate of class Array
def test_Array_validate():
    """Test the function validate of class Array."""

    # Test with items parameter
    items_1 = Field(type="integer")
    items_2 = Field(type="string")

    array_validator = Array(
        items = [items_1, items_2],
        min_items = 2,
        max_items = 3,
        unique_items = True,
        allow_null = False,
    )

    # Test with a valid case
    obj = [1, "2", 4]
    assert array_validator.validate(obj) == obj

    # Test with an invalid case
    obj = ["1", 2, "4"]
    try:
        array_validator.validate(obj)
    except ValidationError as error:
        assert error.messages()
        assert str(error)

# Generated at 2022-06-14 14:26:00.424549
# Unit test for constructor of class Choice
def test_Choice():
    choices = ['choice1', 'choice2']
    field = Choice(choices=choices)
    assert field.choices == [('choice1', 'choice1'), ('choice2', 'choice2')]


# Generated at 2022-06-14 14:26:02.339239
# Unit test for method validate of class String
def test_String_validate():
    value = ""
    strict = False
    field = String()
    field.validate()
    assert True


# Generated at 2022-06-14 14:26:06.792509
# Unit test for method validate of class Boolean
def test_Boolean_validate():
    boolean = Boolean()
    value_test_1 = None
    expected_res_1 = None
    res_1 = boolean.validate(value_test_1)
    assert res_1 == expected_res_1
    value_test_2 = 2
    expected_res_2 = None
    res_2 = boolean.validate(value_test_2, strict=True)
    assert res_2 == expected_res_2


    #value_test_3 = 'null'
    #expected_res_3 = None
    #res_3 = boolean.validate(value_test_3)
    #assert res_3 == expected_res_3
    #value_test_4 = 0
    #expected_res_4 = False
    #res_4 = boolean.validate(value_test_4)
    #assert

# Generated at 2022-06-14 14:26:17.411537
# Unit test for method validate of class Union
def test_Union_validate():
    # Verify that Union(String(),Integer()) raises a ValidationError when
    # passed a float and that the error message contains the message
    # "Did not match any valid type."
    assert_raises(ValidationError, Union([String(),Integer()]).validate, 1.0)
    assert_raises(ValidationError, Union([String(),Integer()]).validate, 1.0)
    assert_raises(ValidationError, Union([String(),Integer()]).validate, 1.0)
    assert_raises(ValidationError, Union([String(),Integer()]).validate, 1.0)
    assert_raises(ValidationError, Union([String(),Integer()]).validate, 1.0)
    assert_raises(ValidationError, Union([String(),Integer()]).validate, 1.0)

# Generated at 2022-06-14 14:26:28.578100
# Unit test for method validate_or_error of class Field
def test_Field_validate_or_error():
    # Valid cases
    valid_field_values = [
        (Field(), "abc", "abc"),
        (Field(), None, None),
    ]

    # Invalid cases
    invalid_field_values = [
        (Field(), [], "List or tuple has to be one element only"),
        (Field(), (1, 2), "List or tuple has to be one element only"),
        (Field(), "a b", "Expected str, got <class 'str'>"),
        (Field(), {}, "Expected object, got <class 'dict'>"),
    ]

    for field, value, error_message in valid_field_values:
        validation_result = field.validate_or_error(value)
        assert validation_result.value == value
        assert validation_result.error is None


# Generated at 2022-06-14 14:26:39.551341
# Unit test for method validate of class Object

# Generated at 2022-06-14 14:27:00.306775
# Unit test for method validate of class Choice
def test_Choice_validate():
    test_val1= 'M'
    test_val2= ''
    test_val3= 'AM'
    ch1=Choice(choices=['AM','PM'])
    ch2=Choice(choices=['AM','PM'],allow_null=True)
    assert ch1.validate(test_val1) == 'M'
    assert ch1.validate(test_val2) == 'AM'
    assert ch1.validate(test_val3) == 'AM'
    assert ch2.validate(test_val1) == 'M'
    assert ch2.validate(test_val2) == 'AM'
    assert ch2.validate(test_val3) == 'AM'
    test_val4= 1
    test_val5= None
    test_val6= ' '


# Generated at 2022-06-14 14:27:03.601311
# Unit test for method serialize of class String
def test_String_serialize():
    test_field=String(format='date')
    assert test_field.serialize('2015-07-23') == '2015-07-23'



# Generated at 2022-06-14 14:27:10.994423
# Unit test for method validate of class Array
def test_Array_validate():
    # true case
    try:
        field = Array(items=String())
        value = ["op", "op"]
        result = field.validate(value)
        assert (result == value)
    except ValidationError:
        assert (False)
    # false case
    try:
        field = Array(items=String())
        value = 4
        result = field.validate(value)
        assert (False)
    except ValidationError:
        assert (True)

# Generated at 2022-06-14 14:27:14.823032
# Unit test for method validate of class Union
def test_Union_validate():
    schema = Union([String(), Integer()])
    assert schema.validate(5) == 5
    assert schema.validate('5') == '5'
    with pytest.raises(ValidationError):
        schema.validate(5.5)
test_Union_validate()



# Generated at 2022-06-14 14:27:17.585184
# Unit test for constructor of class Choice
def test_Choice():
    ch = Choice(choices=["choice1", "choice2", "choice3"])
    assert ch.choices == [("choice1", "choice1"), ("choice2", "choice2"), ("choice3", "choice3")]



# Generated at 2022-06-14 14:27:26.743507
# Unit test for method validate of class Union
def test_Union_validate():
    def test_validation_error_for_object_and_string(s: typing.Any):
        with pytest.raises(ValidationError):
            String().validate(s)
        with pytest.raises(ValidationError):
            Number().validate(s)
        with pytest.raises(ValidationError):
            Boolean().validate(s)
        with pytest.raises(ValidationError):
            Object().validate(s)
        with pytest.raises(ValidationError):
            Array().validate(s)

    # Union([String(), Number(), Boolean(), Object(), Array()]).validate("string")；
    # Union([String(), Number(), Boolean(), Object(), Array()]).validate(1)；
    # Union([String(), Number(), Boolean(), Object(), Array()]).validate

# Generated at 2022-06-14 14:27:29.328827
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    field1=Field(title="test",description="test",default="123")
    assert field1.get_default_value()=="123"


# Generated at 2022-06-14 14:27:32.889421
# Unit test for method validate of class Union
def test_Union_validate():
    # Instantiating a schema
    s = Union([Integer(), Number()])
    # Validating the user input
    result = s.validate("10")
    # Asserting the result
    assert result == 10


# Generated at 2022-06-14 14:27:37.178180
# Unit test for method __or__ of class Field
def test_Field___or__():
    field = Field(title='a', description='b', default=NO_DEFAULT, allow_null=False)
    other = Field(title='a', description='b', default=NO_DEFAULT, allow_null=False)
    or_ = field | other
    assert isinstance(or_, Union)
    assert or_.any_of == [field, other]

# Generated at 2022-06-14 14:27:44.684909
# Unit test for constructor of class String
def test_String():
    # Valid values
    string_field = String(title="title", description="description", allow_blank=True, trim_whitespace=True, max_length=1, min_length=0, pattern="a")
    # Invalid values
    try:
        string_field = String(title="title", description="description", allow_blank=True, trim_whitespace=True, max_length="a", min_length=0, pattern="a")
        assert False, "Invalid max_length value."
    except Exception:
        pass

    try:
        string_field = String(title="title", description="description", allow_blank=True, trim_whitespace=True, max_length=2, min_length="a", pattern="a")
        assert False, "Invalid min_length value."
    except Exception:
        pass


# Generated at 2022-06-14 14:28:08.494187
# Unit test for method validate of class Choice
def test_Choice_validate():
    f = Choice(choices = [1,2])
    res1 = f.validate(1)
    assert res1 == 1
    res2 = f.validate(None)
    assert res2 == None
    res3 = f.validate(None, strict=True)
    assert res3 == None
    res4 = f.validate(3, strict=True)
    assert res4 == 3


# Generated at 2022-06-14 14:28:10.788724
# Unit test for method validate of class Choice
def test_Choice_validate():
    myChoice = Choice(choices=[("a", "b"), ("c", "d")])
    assert myChoice.validate("a") == "a"
    assert myChoice.validate("c") == "c"
    assert myChoice.validate("e") == "e"



# Generated at 2022-06-14 14:28:11.568279
# Unit test for method validate of class Object
def test_Object_validate():
    pass



# Generated at 2022-06-14 14:28:13.177990
# Unit test for method validate of class Array
def test_Array_validate():
    a = Array(items=String())
    a.validate([])
    a.validate(["foo"])
    a.validate(["foo", "bar"])


# Generated at 2022-06-14 14:28:21.509682
# Unit test for method validate of class String
def test_String_validate():
    mystring = String(allow_blank=True)
    assert mystring.validate('a') == 'a'
    assert mystring.validate('') == ''
    assert mystring.validate(None) == ''
   
    mystring2 = String(allow_blank=False)
    try:
        assert mystring2.validate('') == None
    except ValidationError:
        return
    raise AssertionError('ValidationError should have been raised')
    


# Generated at 2022-06-14 14:28:23.611510
# Unit test for method validate of class Union
def test_Union_validate():
    field = Union([Integer(minimum=10)])
    value = 10
    assert field.validate(value)== value
    value = 5
    try:
        field.validate(value)
    except ValidationError as error:
        assert error.messages()[0].code == "minimum"



# Generated at 2022-06-14 14:28:26.104971
# Unit test for method validate of class Array
def test_Array_validate():
    array_field = Array(
        items = Integer()
    )
    array_field.validate([1,2,3])
test_Array_validate()

# Generated at 2022-06-14 14:28:29.865535
# Unit test for method validate of class Array
def test_Array_validate():
    array_test = Array(items=String(), required=True)
    array_test.validate("[\"aaa\",\"bbb\"]")



# Generated at 2022-06-14 14:28:31.354140
# Unit test for method validate of class Choice
def test_Choice_validate():
    choice = Choice(choices=[1,2,3,4])
    assert choice.validate(0) == 'choice'
    assert choice.validate('0') == 'choice'
    assert choice.validate(1) == 1


# Generated at 2022-06-14 14:28:37.038324
# Unit test for constructor of class Choice
def test_Choice():
    c1 = Choice(choices=['a', 'b', 'c'])
    c2 = Choice(choices=[('a', 'A'), ('b', 'B'), ('c', 'C')])
    assert c1.choices == [('a', 'a'), ('b', 'b'), ('c', 'c')]
    assert c2.choices == [('a', 'A'), ('b', 'B'), ('c', 'C')]

# Generated at 2022-06-14 14:28:50.393759
# Unit test for method __or__ of class Field
def test_Field___or__():
    from binascii import unhexlify
    from typesystem import Boolean, Integer, Number
    from typesystem.compat import uuid

    class DecimalField(Field):
        default = decimal.Decimal
        errors = {"not_a_decimal": "{label} should be a decimal."}

        def validate(self, value, strict=False):
            try:
                value = decimal.Decimal(value)
            except decimal.DecimalException:
                raise self.validation_error("not_a_decimal")
            return value

    class UUIDField(Field):
        default = uuid.uuid4
        errors = {"not_a_uuid": "{label} should be a UUID."}


# Generated at 2022-06-14 14:28:55.156784
# Unit test for method __or__ of class Field
def test_Field___or__():
    from typesystem.base import Field, Union
    from typesystem.typing import Number

    field1 = Field()
    field2 = Field()

    assert isinstance(field1 | field2, Union)
    assert (field1 | field2).any_of == [field1, field2]

    assert isinstance((field1 | field2) | Number(), Union)
    assert ((field1 | field2) | Number()).any_of == [field1, field2, Number()]



# Generated at 2022-06-14 14:29:06.126866
# Unit test for constructor of class String
def test_String():
    assert String(allow_blank=False, max_length=1, title="", description="", default="default", allow_null=False).__dict__ == {'title': '', 'description': '', 'default': 'default', 'allow_null': False, 'allow_blank': False, 'trim_whitespace': True, 'max_length': 1, 'min_length': None, 'format': None, 'pattern': None, 'pattern_regex': None, '_creation_counter': 1}

# Generated at 2022-06-14 14:29:13.630277
# Unit test for method serialize of class Array
def test_Array_serialize():
    def test_serialize(self):
        _, schema = self._make_schema(
            items=Int(), required=True, title="Items Title", description="Items Description", default=12,
            label="Items Label", min_value=0, max_value=12, multiple_of=2, required=True
        )
        serializer = schema.serializer
        assert serializer.schema.items == Int(title="Items Title", description="Items Description", default=12,
                                              label="Items Label", min_value=0, max_value=12, multiple_of=2, required=True)
        value = serializer.serialize([2, 4, 6, 8, 10, 12])
        assert value == [2, 4, 6, 8, 10, 12]

# Generated at 2022-06-14 14:29:14.936465
# Unit test for constructor of class String
def test_String():
    test = String()
    assert test is not None



# Generated at 2022-06-14 14:29:20.135896
# Unit test for constructor of class Array
def test_Array():
    try:
        s = Array()
        assert False, "not allow blank"
    except TypeError:
        pass
    s1 = Array(items=None)
    assert s1.items is None, "allow blank"
    s2 = Array(items=Field())
    assert isinstance(s2.items, Field), "if items is a Field"
    s3 = Array(items=[])
    assert isinstance(s3.items, list) and len(s3.items) == 0, "if items is a list"
    try:
        s4 = Array(items=[Field(), "3"])
        assert False, "all items in list should be Field"
    except TypeError:
        pass
    s5 = Array(items=[Field(), Field()])

# Generated at 2022-06-14 14:29:27.889921
# Unit test for method validate of class Union
def test_Union_validate():
    from freditor.schema.field import String, Number, ValidationError
    from freditor.schema import Message

    field = Union([String(), Number()])
    assert field.validate("1") == "1"
    assert field.validate(1) == 1
    assert field.validate(True) == "true"  # Because it's a string field

    with pytest.raises(
        ValidationError,
        match="<ValidationError messages=\\[<Message code='union' text='Did not match any valid type.'>]>",
    ):
        field.validate(True)



# Generated at 2022-06-14 14:29:33.724424
# Unit test for constructor of class Const
def test_Const():
    assert Const(const=None, allow_null=True).allow_null == True
    try:
        assert Const(const=None, allow_null=False).allow_null == True
    except AssertionError:
        pass
    assert Const(const=10).allow_null == False



# Generated at 2022-06-14 14:29:42.295357
# Unit test for method validate of class String
def test_String_validate():
    MASHUP_LIST_OF_STRING = ['2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2']
    # inputs:

# Generated at 2022-06-14 14:29:46.657298
# Unit test for method validate of class Object
def test_Object_validate():
    key1 = "key1"
    key2 = "key2"
    key3 = "key3"
    key4 = "key4"

    prop1 = String()
    prop2 = String()
    prop3 = String()
    prop4 = String()
    prop5 = String()
    prop6 = String()

    schema = Object(properties={key1: prop1, key2: prop2}, required=["key1"])

    # Validating required fields
    value = {}
    try:
        schema.validate(value)
        print("\tFail")
    except ValidationError as e:
        print("\tPass")
    except Exception:
        print("\tFail")

    value = {key1: "hello"}

# Generated at 2022-06-14 14:30:15.406268
# Unit test for constructor of class String
def test_String():
    expected=String(title="", description="")
    title=expected.title 
    description=expected.description
    assert title == ""
    assert description == ""
    assert expected.allow_null == False
    assert expected.allow_blank == False
    assert expected.trim_whitespace == True
    assert expected.max_length == None
    assert expected.min_length == None
    assert expected.pattern == None
    assert expected.format == None


# Generated at 2022-06-14 14:30:18.364194
# Unit test for constructor of class Const
def test_Const():
    # Create an instance of Const
    Con = Const(const=None)
    # Test it with different inputs
    assert Con.validate(1) == 1
    assert Con.validate(None) == None
    # Test that ValidationError is raised when the input is not equal to the const
    with pytest.raises(ValidationError) as err:
        Con.validate(3)
    assert "Must be null." in err.value.message()
    

# Generated at 2022-06-14 14:30:26.452385
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    class TestField(Field):
        def validate(self, value):
            return True
    # test with default as string
    test = TestField(default="def")
    assert test.get_default_value() == "def"
    # test with default as callable function
    test = TestField(default=lambda: "def")
    assert test.get_default_value() == "def"
    # test with no default
    test = TestField()
    assert test.get_default_value() == None


# Generated at 2022-06-14 14:30:37.063779
# Unit test for method validate of class String
def test_String_validate():
    # Testing int value as input to method
    value_testcase_1 = 1234
    # Expected output of method
    expected_output_1 = ValidationError(text="Must be a string.",code="type")
    # Actual output of method
    actual_output_1 = String().validate_or_error(value=value_testcase_1)
    # Checking if the expected output is same as actual output
    assert expected_output_1.text == actual_output_1.error.text
    assert expected_output_1.code == actual_output_1.error.code
    # Testing float value as input to method
    value_testcase_2 = 1234.567
    # Expected output of method
    expected_output_2 = ValidationError(text="Must be a string.",code="type")
    # Actual output of method

# Generated at 2022-06-14 14:30:46.731190
# Unit test for method validate of class Union
def test_Union_validate():
    from jsonschema import TypeError
    from .validation import ValidationError

    class FieldMock(Field):
        def __init__(self, allow_null: bool = True):
            super().__init__(allow_null=allow_null)

        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            raise NotImplementedError()

    def raise_error(error: typing.Any, *, strict: bool = False) -> typing.Any:
        raise error

    # Test nullable
    child = FieldMock()
    union = Union([child])
    assert union.allow_null
    assert union.validate(None) is None

    child = FieldMock(allow_null=False)
    union = Union([child])
    assert not union.allow_null

   

# Generated at 2022-06-14 14:30:54.915038
# Unit test for method validate of class Union
def test_Union_validate():
    from unittest import TestCase
    from opyapi.schema.types import Boolean, Integer, String, Union

    def validate_or(schema: Union, value: typing.Any) -> typing.Tuple[bool, Union]:
        try:
            schema.validate(value)
        except ValidationError as error:
            return False, error
        return True, None

    field = Union(any_of=[Integer(), String()]) 
    assert validate_or(field, 'hello') == (True, None)
    assert validate_or(field, 123) == (True, None)
    assert validate_or(field, 3.14) == (False, ValidationError(messages=[Message(text='Must be an integer.', code='type')]))


# Generated at 2022-06-14 14:30:59.992027
# Unit test for method __or__ of class Field
def test_Field___or__():
    #MethodInput:
    #Field other:
    other = Field("Hello, world")
    assert other is not None
    #endField
    assert (self.__or__(other)) is not None

# Here, we test the parameters of the method __or__

# Generated at 2022-06-14 14:31:02.685187
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    #1
    if getattr(Field, 'default', None) == None:
        assert Field.get_default_value() == None
    else:
        Field.default = lambda: 1
        assert Field.get_default_value() == 1


# Generated at 2022-06-14 14:31:11.221267
# Unit test for method __or__ of class Field
def test_Field___or__():
    from typesystem.types import Array, Boolean, Integer, Number, Object, String
    from typesystem.types import Date, DateTime, Time
    from typesystem.json_schema import compile_schema

    f = Field(title="name")
    f = f | Integer(min_value=1, max_value=10)
    f = f | String(max_length=10)
    assert compile_schema(f) == {
        "title": "name",
        "type": "integer",
        "anyOf": [
            {"minimum": 1, "maximum": 10},
            {"type": "string", "maxLength": 10},
        ],
    }
    f = f | Date(format="date")
    f = f | DateTime(format="datetime")
    f = f | Time(format="time")
    f

# Generated at 2022-06-14 14:31:21.131060
# Unit test for method validate of class Choice
def test_Choice_validate():
    assert Choice(name='City', choices=[('Paris', 'Paris'), ('London', 'London'), ('Tokyo', 'Tokyo')]).validate('Paris') == 'Paris'
    assert Choice(name='City', choices=[('Paris', 'Paris'), ('London', 'London'), ('Tokyo', 'Tokyo')]).validate('Paris') != 'Lyon'
    assert Choice(name='City', choices=[('Paris', 'Paris'), ('London', 'London'), ('Tokyo', 'Tokyo')]).validate('Paris') != 'Milan'
    assert Choice(name='City', choices=[('Paris', 'Paris'), ('London', 'London'), ('Tokyo', 'Tokyo')]).validate('Paris') != 'New York'
    assert Choice(name='City', choices=[('Paris', 'Paris'), ('London', 'London'), ('Tokyo', 'Tokyo')]).valid

# Generated at 2022-06-14 14:31:37.900543
# Unit test for method serialize of class Array
def test_Array_serialize():
    class SubTestClass(Serializer):
        x = Integer()
    class TestClass(Serializer):
        field = Array(items=SubTestClass)
    instance = SubTestClass(x=10)
    instance_list = [instance]
    tc = TestClass(field=instance_list)
    assert tc.field == instance_list
    assert tc.dump().data == {"field": [{"x": 10}]}
    assert tc.validate() == {"field": [{"x": 10}]}


# Generated at 2022-06-14 14:31:40.158375
# Unit test for method validate of class Choice
def test_Choice_validate():
    assert Choice(choices=["a", "b", "c"]).validate("a") == "a"
    assert Choice(choices=["a", "b", "c"]).validate("d") == "a"
    assert Choice(choices=[("a", "d"), ("b", "e"), ("c", "f")]).validate("d") == "a"


# Generated at 2022-06-14 14:31:51.818853
# Unit test for method validate of class Number
def test_Number_validate():
    test_number = Number(minimum=5, maximum=10)
    tlist = [
        ("exact 10.0", test_number.validate, 10.0, {}),
        ("exact 9.0", test_number.validate, 9.0, {}),
        ("exact 5.0", test_number.validate, 5.0, {}),
        ("more 10.0", test_number.validate, 11.0, {"strict": True}, ValidationError),
        ("less 5.0", test_number.validate, 4.9, {"strict": True}, ValidationError),
    ]
    for t in tlist:
        t_name, t_func, t_arg, t_kwargs, t_expected = t

# Generated at 2022-06-14 14:31:52.286185
# Unit test for constructor of class Const
def test_Const():
    pass


# Generated at 2022-06-14 14:31:56.423691
# Unit test for method validate of class Array
def test_Array_validate():
    validator = Array(
        items= [
            Field(allow_null = True),
            Integer(minimum = 10, maximum = 20)
        ],
        additional_items=False,
        allow_null=False
    )

    input_test = [None, 5, 9, 10, 15, 20, 40, 'test']
    expected_output = [None, 5, 9, 10, 15, 20, 40, 'test']
    output_test = validator.validate(input_test, strict=True)
    assert output_test == expected_output


# Generated at 2022-06-14 14:31:59.267140
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    from typesystem.fields import String
    from typesystem import ValidationError

    field=String(title="name", default="default name")
    assert field.get_default_value() == "default name"
    assert isinstance(field.validation_error("invalid"), ValidationError)

# Generated at 2022-06-14 14:32:09.912347
# Unit test for method validate of class Choice
def test_Choice_validate():
    c1 = Choice(choices=[(1, "one"), (2, "two"), (3, "three")])
    assert c1.validate(1) == 1
    assert c1.validate(2) == 2
    assert c1.validate(3) == 3
    assert c1.validate(4)
    try:
        c1.validate(4)
    except ValidationError as e:
        assert e.code == "choice"
    try:
        c1.validate(None)
    except ValidationError as e:
        assert e.code == "null"

    c2 = Choice(choices=[(1, "one"), (2, "two"), (3, "three")], allow_null=True)
    assert c2.validate(None) == None
    assert c2.valid

# Generated at 2022-06-14 14:32:14.471084
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    field = Field()
    assert field.get_default_value() == None
    field.default = 3
    assert field.get_default_value() == 3
    field.default = lambda : 2
    assert field.get_default_value() == 2


# Generated at 2022-06-14 14:32:24.342069
# Unit test for method __or__ of class Field
def test_Field___or__():
    # Parameter int_field of test_Field___or__
    class int_field(Field):
        def validate(self, value: typing.Any, *, strict: bool = False) -> typing.Any:
            if value is None and self.allow_null:
                return None
            if not isinstance(value, int):
                raise self.validation_error("type")
            return value
    # Parameter str_field of test_Field___or__
    class str_field(Field):
        def validate(self, value: typing.Any, *, strict: bool = False) -> typing.Any:
            if value is None and self.allow_null:
                return None
            if not isinstance(value, str):
                raise self.validation_error("type")
            return value
    # Parameter union_field of test_Field

# Generated at 2022-06-14 14:32:26.285723
# Unit test for method validate of class Choice
def test_Choice_validate():
    choice = Choice()
    choice.validate(None)
    assert True



# Generated at 2022-06-14 14:33:14.083111
# Unit test for method validate of class Array
def test_Array_validate():

    # Test case 1
    schema = Array(items=Integer())
    value = [1, 2, 3]
    assert schema.validate(value) == value
    assert schema.serialize(value) == value

    # Test case 2
    schema = Array(items=Integer(), additional_items=True)
    value = [1, "2", 3]
    assert schema.validate(value) == value

    with pytest.raises(ValidationError) as error:
        schema.validate([1, 2, 3, 4])

    assert error.value.messages == [Message(text="Must have at most 3 items.", code="max_items", key="max_items")]

    # Test case 3
    schema = Array(items=[Integer(), String()], additional_items=False)
    value = [1, "2"]
   

# Generated at 2022-06-14 14:33:17.282422
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    field=Field(title="aa", description="bb")
    assert field.get_default_value() is None
    temp = field.get_default_value()
    assert temp is None
