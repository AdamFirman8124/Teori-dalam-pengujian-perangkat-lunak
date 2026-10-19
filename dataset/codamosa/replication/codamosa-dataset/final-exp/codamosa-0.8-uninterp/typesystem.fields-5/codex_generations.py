

# Generated at 2022-06-14 14:25:51.518431
# Unit test for method __or__ of class Field
def test_Field___or__():
  assert (None or Field())  # Insert breakpoint here



# Generated at 2022-06-14 14:25:57.607764
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    field1 = Field(default=NO_DEFAULT)
    assert(field1.get_default_value() is None)
    field2 = Field(default = "hello")
    assert(field2.get_default_value() == "hello")
    def def_func():
        return "world"
    field3 = Field(default = def_func)
    assert(field3.get_default_value() == "world")



# Generated at 2022-06-14 14:26:03.657212
# Unit test for method validate of class Choice
def test_Choice_validate():
    obj1 = Choice(allow_null=True, choices=[("YES", "Yes"), ("NO", "No")])
    assert obj1.validate("YES") == "YES"
    assert obj1.validate("NO") == "NO"
    assert obj1.validate("") == None
    assert obj1.validate("NULL") == None
    assert obj1.validate("null") == None

test_Choice_validate()



# Generated at 2022-06-14 14:26:14.222950
# Unit test for method validate_or_error of class Field
def test_Field_validate_or_error():
    """
    Validates that the method validate_or_error of class Field
    returns a ValidationResult object containing the value and the error of a field.

    This test must return a class that inherits from Field for being able to recognize
    the function validate_or_error.
    """
    class FieldTest(Field):
        def __init__(self, *, value, error):
            self.value = value
            self.error = error
        def validate(self):
            return self.value

    field = FieldTest(value=5, error='error')
    assert isinstance(field.validate_or_error(field), ValidationResult)


# Generated at 2022-06-14 14:26:17.580850
# Unit test for method validate of class Array
def test_Array_validate():
    assert Array().validate([1, 2, 3]) == [1, 2, 3]
    assert Array().validate({'a': 1}) == {'a': 1}
    assert Array().validate(123) == 123
    assert Array().validate(None, strict=True) == None




# Generated at 2022-06-14 14:26:23.552559
# Unit test for method serialize of class Array
def test_Array_serialize():
    # Null
    assert Array().serialize(None) == None
    assert Array(allow_null=True).serialize(None) == None

    # List
    # Check when field is list
    my_list = ["A", "B"]
    assert Array(items = []).serialize(my_list) == my_list
    assert Array(items = [String()]).serialize(my_list) == my_list

    # Check when field is Field
    assert Array(items = String()).serialize(my_list) == ["A", "B"]
    assert Array(items = String(allow_null=True)).serialize(["A", None, "B"]) == ["A", None, "B"]

    # Check when field is None
    assert Array(items = None).serialize(my_list) == my_list

# Unit

# Generated at 2022-06-14 14:26:34.043143
# Unit test for method validate of class Array
def test_Array_validate():
    # create a field object
    array_field_object = Array()
    # the input arguments which will be used in the validate method
    args = [1,[1,3,3]]
    # the correct output value
    correct_output = [1, [1, 3, 3]]
    # test method
    try:
        # the function to be tested
        output = array_field_object.validate(args[0],strict=args[1])
    # Assertion error means the test is failed
    except AssertionError:
        print('TEST FAILED: validate() did not return the correct object')
        return False
    
    # the test is successed
    return True


# Generated at 2022-06-14 14:26:43.272374
# Unit test for method __or__ of class Field
def test_Field___or__():
    # Test Field.__or__ with non-Union, non-Union
    field1 = Field()
    field2 = Field()
    field = field1 | field2
    assert isinstance(field, Union)
    assert field.any_of == [field1, field2]
    # Test Field.__or__ with Union, non-Union
    field1 = Field()
    field2 = Field()
    field3 = Field()
    field4 = Union(any_of=[field1, field2])
    field = field4 | field3
    assert isinstance(field, Union)
    assert field.any_of == [field1, field2, field3]
    # Test Field.__or__ with non-Union, Union
    field1 = Field()
    field2 = Field()
    field3 = Field()

# Generated at 2022-06-14 14:26:48.497089
# Unit test for method validate of class Object
def test_Object_validate():
    property1 = {"age": Integer()}
    property2 = {"name": String()}
    properties = {**property1, **property2}
    schema = Object(properties = properties)

    assert schema.validate({'age': 0}) == {'age': 0}
    assert schema.validate({'name': 'Levin'}) == {'name': 'Levin'}
    assert schema.validate({'age': 0, 'name': 'Levin'}) == {'age': 0, 'name': 'Levin'}

test_Object_validate()



# Generated at 2022-06-14 14:27:00.546261
# Unit test for method validate of class Choice
def test_Choice_validate():
    assert Choice(choices=[("a","A"),("b","B")], allow_null=False, required=True).validate("a") == "a"
    assert Choice(choices=[("a","A"),("b","B")], allow_null=False, required=True).validate("b") == "b"
    assert Choice(choices=[("a","A"),("b","B")], allow_null=False, required=True).validate("c") == None
    assert Choice(choices=[("a","A"),("b","B")], allow_null=True, required=True).validate("a") == "a"
    assert Choice(choices=[("a","A"),("b","B")], allow_null=True, required=True).validate("b") == "b"

# Generated at 2022-06-14 14:27:17.267989
# Unit test for method validate of class Union
def test_Union_validate():
    union = Union([
        Text,
        Object({'a': Text})
    ])
    
    # value is not a string
    with pytest.raises(ValidationError):
        union.validate(1)
    # value is not an object
    with pytest.raises(ValidationError):
        union.validate("hello")
        
    # value is a string
    assert union.validate("hello") == "hello"
    # value is an object
    assert union.validate({'a': "hello"}) == {'a': "hello"}
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


# Generated at 2022-06-14 14:27:25.960618
# Unit test for method validate of class Array
def test_Array_validate():
    array = Array()
    assert array.validate([1, 2, 3]) == [1, 2, 3]
    assert array.validate([]) == []
    assert array.validate(None, strict=True) == None
    with pytest.raises(ValidationError):
        array.validate(None)
    with pytest.raises(ValidationError, match=r".*Must be an array.*"):
        array.validate("[]")
    with pytest.raises(ValidationError, match=r".*May not be null.*"):
        array.validate(None)
    with pytest.raises(ValidationError, match=r".*Items must be unique.*"):
        array = Array(unique_items=True)
        array.validate([])

# Generated at 2022-06-14 14:27:32.011708
# Unit test for method validate of class Object
def test_Object_validate():
    # Test case 1: when strict is False and the input is integers, output: valid (0)
    obj_field = Object()
    assert obj_field.validate(value=0, strict=False) == 0

    # Test case 2: when strict is True and the input is integers, output: invalid
    assert obj_field.validate(value=0, strict=True) == 0


# Generated at 2022-06-14 14:27:33.679198
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    f=Field()
    assert f.get_default_value() == None


# Generated at 2022-06-14 14:27:38.696340
# Unit test for method validate of class Choice
def test_Choice_validate():
    if Choice.validate('a') != 'a':
        print('test_Choice_validate_1_1 failed')
    if Choice.validate('') == '':
        print('test_Choice_validate_2_1 failed')
    if Choice.validate({'ba':'ba'}) == {'ba':'ba'}:
        print('test_Choice_validate_3_1 failed')

# Generated at 2022-06-14 14:27:47.278545
# Unit test for method validate of class Union
def test_Union_validate():
    class TestUnion(Union):
        def __init__(self, any_of: typing.List[Field], **kwargs: typing.Any):
            super().__init__(any_of=any_of, **kwargs)

    any_of = [String(), Integer(), Number()]
    union = TestUnion(any_of=any_of)
    union.validate('test_Union_validate()')
    union.validate(1)
    union.validate(2.0)
    try:
        union.validate(1.0)
    except ValidationError:
        pass
    try:
        union.validate({})
    except ValidationError:
        pass


# Generated at 2022-06-14 14:27:51.358946
# Unit test for method validate of class Number
def test_Number_validate():
    number_object = Number()
    try: 
        assert number_object.validate(1.1) == 1.1
    except:
        print("Unit test for method validate of class Number does not pass")



# Generated at 2022-06-14 14:28:02.391269
# Unit test for method validate of class Object
def test_Object_validate():
    schema = Object(properties={'a': Integer(required=True)})
    # test_null
    try:
        schema.validate(None)
        assert False
    except ValidationError as e:
        assert not e.messages()

    # test_a
    schema.validate({'a': 1})
    try:
        schema.validate({})
        assert False
    except ValidationError as e:
        assert e.messages()
    
    # test_int_value
    try:
        schema.validate(1)
        assert False
    except ValidationError as e:
        assert not e.messages()
    
    # test_required
    try:
        schema.validate({})
        assert False
    except ValidationError as e:
        assert not e.messages()
    


# Generated at 2022-06-14 14:28:10.337963
# Unit test for method validate of class Boolean
def test_Boolean_validate():
    b = Boolean()
    assert b.validate('1') == True
    assert b.validate(1) == True
    assert b.validate(0) == False
    assert b.validate('0') == False
    assert b.validate('true') == True
    assert b.validate('false') == False
    assert b.validate('on') == True
    assert b.validate('off') == False
    assert b.validate('') == False
    assert b.validate(None) == None



# Generated at 2022-06-14 14:28:15.196166
# Unit test for method serialize of class String
def test_String_serialize():
    test_string = [
        ("python", "python"),
        ("", "")
    ]
    for str_test, expect in test_string:
        result = String().serialize(str_test)
        assert result == expect

    str = "13.13.13.13"
    with pytest.raises(ValidationError):
        String(format="date").serialize(str)



# Generated at 2022-06-14 14:28:38.520682
# Unit test for method __or__ of class Field
def test_Field___or__():
    # Given
    f1 = Field()
    f2 = Field()

    # When
    u = f1 | f2

    # Then
    assert isinstance(u, Union)
    assert isinstance(u.any_of[0], Field)
    assert isinstance(u.any_of[1], Field)



# Generated at 2022-06-14 14:28:39.926418
# Unit test for method validate of class String
def test_String_validate():
    string = String()
    string.validate('jhango')


# Generated at 2022-06-14 14:28:52.178219
# Unit test for method validate of class Array
def test_Array_validate():
    input = {"a": 5}
    s = Object(properties={"a": Integer()})
    res, _ = s.validate_or_error(input)
    assert res == {"a": 5}
    input = {"a": "123"}
    res, error = s.validate_or_error(input)
    assert input == res
    assert error is not None
    assert len(error.messages()) == 1
    assert error.messages()[0].text == "Must be an integer."
    assert error.messages()[0].code == "type"
    assert error.messages()[0].index == ["a"]

    input = {"a": {"a": 123}}

# Generated at 2022-06-14 14:29:03.907533
# Unit test for method validate of class Object
def test_Object_validate():
    object1 = Object(allow_null = True, properties = {'name':String(max_length = 10, required = True), 'country':String(max_length = 7)}, pattern_properties = {'\d+':Integer(exclusive_maximum = 10)}, min_properties = 2, max_properties = 10)
    # Testing with valid data

# Generated at 2022-06-14 14:29:08.536443
# Unit test for method validate of class Union
def test_Union_validate():
    with pytest.raises(ValidationError):
        a = Union([Number(), Integer()])
        # pylint: disable=unused-variable
        b = a.validate("a")
        c = a.validate("0")
        # pylint: enable=unused-variable



# Generated at 2022-06-14 14:29:12.696194
# Unit test for method validate of class Array
def test_Array_validate():
    from bevy.schema import Array, Integer, ValidationError
    ArrayTest = Array(
        items = Integer(),
        additional_items = False,
        min_items = 2,
        max_items = None,
        exact_items = None,
        unique_items = False,
        allow_null = False,
    )
    with pytest.raises(ValidationError):
        ArrayTest.validate(None)


# Generated at 2022-06-14 14:29:21.796203
# Unit test for method validate of class Choice
def test_Choice_validate():
    choices_list = [('1', 'a'), ('2', 'b'), ('3', 'c')]
    choices = Choice(choices=choices_list)
    assert choices.validate('1') == '1'
    assert choices.validate('2') == '2'
    assert choices.validate('3') == '3'
    with pytest.raises(ValidationError):
        choices.validate('4')
    with pytest.raises(ValidationError):
        choices.validate('a')
    with pytest.raises(ValidationError):
        choices.validate('b')
    with pytest.raises(ValidationError):
        choices.validate('c')


# Generated at 2022-06-14 14:29:26.485290
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    from typesystem import Integer
    from typesystem.base import field

    @field("a", Integer)
    def a(*args, **kwargs):
        return Integer("a", *args, **kwargs)

    a2 = a(default=3)

    assert a2.get_default_value() == 3



# Generated at 2022-06-14 14:29:27.075875
# Unit test for method validate of class Number
def test_Number_validate():
    pass

# Generated at 2022-06-14 14:29:34.978462
# Unit test for method validate of class Object
def test_Object_validate():

    # Case 1: value is None and self.allow_null
    field = Object(allow_null=True)
    assert field.validate(value=None, strict=False) is None

    # Case 2: value is None and not self.allow_null
    field = Object(allow_null=False)
    try:
        field.validate(value=None, strict=False)
    except Exception as e:
        assert isinstance(e, ValidationError)

    # Case 3: value is not dict
    field = Object()
    try:
        field.validate(value=1, strict=False)
    except Exception as e:
        assert isinstance(e, ValidationError)

    # Case 4: value contains not str key
    field = Object()

# Generated at 2022-06-14 14:29:49.310410
# Unit test for method validate of class Choice
def test_Choice_validate():
    choice = Choice(choices=['male', 'female'])
    assert choice.validate('male')=='male'
    assert choice.validate('female')=='female'
    try:
        choice.validate('unknown')
        assert False, 'choice.validate("unknown") did not raise ValidationError'
    except ValidationError:
        pass
    # Allow null
    choice = Choice(choices=['male', 'female'], allow_null=True)
    assert choice.validate(None)==None
    assert choice.validate('')==None
    assert choice.validate('male')=='male'
    assert choice.validate('female')=='female'

# Generated at 2022-06-14 14:29:55.086225
# Unit test for constructor of class String
def test_String():
    frm = String(title = "First Name", description = "the first name of a person", default = "John", allow_null = False)
    assert isinstance(frm, Field)
    assert frm.title == "First Name"
    assert frm.description == "the first name of a person"
    assert frm.default == frm.default
    assert frm.allow_null == False


# Generated at 2022-06-14 14:30:00.738662
# Unit test for method validate of class Array
def test_Array_validate():
    # Arrange
    expected_list = [1, 2, 3]
    actual_list = [1,2,3]
    field = Array(min_items=3, max_items=4)

    # Act
    value, error = field.validate_or_error(actual_list)

    # Assert
    assert expected_list == value



# Generated at 2022-06-14 14:30:13.832788
# Unit test for method validate of class Array
def test_Array_validate():
    serializer = Array(
        items = [
            Integer(minimum=1, maximum=10),
            Integer(minimum=50, maximum=100)
        ],
        additional_items = Integer(minimum=1, maximum=10),
        min_items = 2,
        max_items = 4)
    serializer.validate([3, 4, 7, 8])
    serializer.validate([3, 4])
    with pytest.raises(ValidationError):
        serializer.validate([3])
    with pytest.raises(ValidationError):
        serializer.validate([3, 4, 7, 8, 5])
    with pytest.raises(ValidationError):
        serializer.validate([3, 4, 8, 8, 9])
    with pytest.raises(ValidationError):
        serial

# Generated at 2022-06-14 14:30:21.909278
# Unit test for method validate of class Object
def test_Object_validate():

    prop_dict ={'number':Integer()}
    obj = Object(properties=prop_dict)
    ft = {'number':5}
    obj.validate(ft)==ft
    try:
        ft['number']=-5
        obj.validate(ft)
        raise Exception('Should be failed')
    except ValidationError:
        pass
    ft = {'number':'5'}
    obj.validate(ft)=={'number':5}
    ft = {'number':None}
    try:
        obj.validate(ft)
        raise Exception('Should be failed')
    except ValidationError:
        pass


# Generated at 2022-06-14 14:30:32.484945
# Unit test for method validate of class Boolean
def test_Boolean_validate():
    """
    Test for method validate of Boolean
    """
    field = Boolean()
    print("Test 1: Test for method validate of class Boolean")
    print("Test Case 1: Boolean(False) validates as False")
    assert field.validate(False) == False, "Field does not validate as False"
    print("Test Case 2: Boolean(True) validates as True")
    assert field.validate(True) == True, "Field does not validate as True"
    print("Test Case 3: Boolean(1) validates as True")
    assert field.validate(1) == True, "Field does not validate as True"
    print("Test Case 4: Boolean(0) validates as False")
    assert field.validate(0) == False, "Field does not validate as False"

# Generated at 2022-06-14 14:30:43.422110
# Unit test for method validate of class Choice
def test_Choice_validate():
    choice = Choice()
    assert choice.validate('') == None
    assert choice.validate('value') == 'value'
    choice = Choice(choices=['value'])
    assert choice.validate('') == None
    assert choice.validate('value') == 'value'
    choice = Choice(choices=['value'],allow_null=False)
    assert choice.validate('') == None
    assert choice.validate('value') == 'value'
    choice.strict = True
    assert choice.validate('value') == 'value'
    choice = Choice(choices=['value'],allow_null=False,allow_blank=True)
    assert choice.validate('') is None
    assert choice.validate('value') == 'value'

# Generated at 2022-06-14 14:30:45.783554
# Unit test for method validate of class Object
def test_Object_validate():
    obj = Object()
    # For now only check that it runs without errors
    obj.validate({'a': '3', 'b': {'c': 4}})



# Generated at 2022-06-14 14:30:47.794222
# Unit test for constructor of class Const
def test_Const():
    c = Const(2)
    assert(c.const, 2)
    assert(c.allow_null, False)



# Generated at 2022-06-14 14:30:55.627089
# Unit test for method validate of class Object
def test_Object_validate():
    def test_properties(test_object):
        #Test for non-empty and non-null value
        test_object.validate(value={'a': 1, 'b': 2, 'c': 3})
 
        #Test for empty but not null value
        test_object.validate(value={})
 
        #Test for null value
        test_object.validate(value=None)
 
        #Test for non-null and non-object value
        with pytest.raises(ValidationError) as e:
            test_object.validate(value=1)
        assert len(e.value.messages) == 1
        assert e.value.messages[0].text == "Must be an object."
        assert e.value.messages[0].code == "type"
 
        #Test for null and

# Generated at 2022-06-14 14:31:14.334043
# Unit test for constructor of class String
def test_String():
    string = String(title="name",description="a string")
    assert string.title == "name"
    assert string.description == "a string"
    assert string.allow_blank == False
    assert string.trim_whitespace == True
    assert string.max_length == None
    assert string.min_length == None
    assert string.pattern == None
    assert string.format == None


# Generated at 2022-06-14 14:31:23.594100
# Unit test for method validate of class Array
def test_Array_validate():
    items = [String(min_length=2), Integer(), Decimal(precision=2)]
    schema = Array(items)
    data = ["foo", 12, 12.34, 24.56]
    message = schema.validate(data)
    if message == None:
        print("validate(self, value, *, strict=False) -> typing.Any PASSED")
    else:
        print("validate(self, value, *, strict=False) -> typing.Any FAILED")

# Generated at 2022-06-14 14:31:35.087009
# Unit test for method validate of class Object
def test_Object_validate():
    def test_None():
        # Test with None when allow_null is False.
        field = Object(title="test_test_method_test")
        try:
            field.validate(None)
        except ValidationError as e:
            assert e.messages()[0] == Message(text="May not be null.", code="null")
        # Test with None when allow_null is True.
        field = Object(title="test_test_method_test", allow_null=True)
        result = field.validate(None)
        assert result == None

    def test_str():
        # Test with a string.
        field = Object(title="test_test_method_test")
        try:
            field.validate("A string.")
        except ValidationError as e:
            assert e.messages()[0]

# Generated at 2022-06-14 14:31:37.216065
# Unit test for constructor of class Const
def test_Const():
    field = Const(const="hello")
    assert field.const == "hello"
    assert field.allow_null == None
    field = Const(const="hello", allow_null=True)
    assert field.allow_null == True


# Generated at 2022-06-14 14:31:39.227397
# Unit test for method validate of class Choice
def test_Choice_validate():
    chioce = Choice()
    chioce.allow_null = True
    chioce.choices = [('1', '1'), ('2', '2'), ('3', '3')]

    print(chioce.validate(None))


# Generated at 2022-06-14 14:31:45.569104
# Unit test for method __or__ of class Field
def test_Field___or__():
    from typesystem import Integer, String, Union
    from typesystem import Number, Float, Decimal
    from typesystem import Boolean, Object, Array
    
    field1 = Integer() | String()
    field2 = Array(items=(Number() | Float()))
    field3 = Array(items=(Boolean() | Object() | Integer() | Float()))
    assert isinstance(field1, Union)
    assert isinstance(field2, Array)
    assert isinstance(field3, Array)
    assert field2.items.any_of[0] is Number()
    assert field2.items.any_of[1] is Float()
    assert field3.items.any_of[0] is Boolean()
    assert field3.items.any_of[1] is Object()
    assert field3.items.any_of[2] is Integer

# Generated at 2022-06-14 14:31:50.351612
# Unit test for method validate of class Union
def test_Union_validate():
    value = [1, 2, 3]
    union = Union([
        Array(items=Integer(minimum=0)),
        Object(properties={
            "a": Integer(minimum=1)
        })
    ])
    union.validate(value)


# Generated at 2022-06-14 14:31:55.903004
# Unit test for method validate of class Choice
def test_Choice_validate():
    print("Test Choice validate:")
    choice=Choice(name="choice", choices=["a", "b"])
    try:
        choice.validate(1)
    except ValidationError as e:
        print("Value 1 is not a valid choice:", e)
    try:
        choice.validate(2)
    except ValidationError as e:
        print("Value 2 is not a valid choice:", e)
    try:
        choice.validate("c")
    except ValidationError as e:
        print("Value c is not a valid choice:", e)
    try:
        choice.validate("d")
    except ValidationError as e:
        print("Value d is not a valid choice:", e)

test_Choice_validate()
# End of unit test


# Generated at 2022-06-14 14:32:00.801619
# Unit test for method validate of class Choice
def test_Choice_validate():
    assert Choice(choices=[("1","one"),("2","two"),("3","three")]).validate("3",strict=False)=="3"
    assert Choice(choices=[("1","one"),("2","two"),("3","three")]).validate("4",strict=False)=="4"
    assert Choice(choices=[("1","one"),("2","two"),("3","three")]).validate("3",strict=True)=="3"
    assert Choice(choices=[("1","one"),("2","two"),("3","three")]).validate("4",strict=True)=="4"
    assert Choice(choices=[("1","one"),("2","two"),("3","three")]).validate("2",strict=False)=="2"

# Generated at 2022-06-14 14:32:01.859077
# Unit test for constructor of class Array
def test_Array():
    field = Array()


# Generated at 2022-06-14 14:32:11.939075
# Unit test for method validate of class Choice
def test_Choice_validate():
    field = Choice(required=True, choices=[
        ('Male', 'male'),
        ('Female', 'female'),
    ])
    assert field.validate('male') is None
    with pytest.raises(ValidationError) as ex:
        field.validate('girl')
    assert ex.value.code == 'choice'
    field.allow_null = True
    assert field.validate('') is None
    with pytest.raises(ValidationError) as ex:
        field.validate(None)
    assert ex.value.code == 'null'



# Generated at 2022-06-14 14:32:21.914076
# Unit test for constructor of class String
def test_String():
    string = String(title='title', description='description', allow_blank=True, trim_whitespace=True, max_length=None, min_length=None, pattern=None, format=None, allow_null=False)
    assert(string.title == 'title')
    assert(string.description == 'description')
    assert(string.allow_blank == True)
    assert(string.trim_whitespace == True)
    assert(string.max_length == None)
    assert(string.min_length == None)
    assert(string.pattern == None)
    assert(string.format == None)
    assert(string._creation_counter == 0)
    assert(string.allow_null == False)


# Generated at 2022-06-14 14:32:27.646460
# Unit test for method validate of class Choice
def test_Choice_validate():
    # Test case 1
    test_choice = Choice(choices=["a", "b", "c"])
    test_choice.allow_null = True
    val = test_choice.validate("a")
    assert val == "a"
    val = test_choice.validate("d")
    assert val is None


# Generated at 2022-06-14 14:32:30.559341
# Unit test for constructor of class Const
def test_Const():
    try:
        Const(const=None)
    except AssertionError as e:
        print(e)


# Generated at 2022-06-14 14:32:34.834619
# Unit test for method validate of class String
def test_String_validate():
    field = String()
    assert isinstance(field.validate('toto'),str)
    assert field.validate('toto') == 'toto'
    with pytest.raises(ValidationError):
        field.validate('')

#Unit test for method serialize of class String

# Generated at 2022-06-14 14:32:41.619799
# Unit test for method validate of class String
def test_String_validate():
    assert String(max_length=3).validate("s") == "s"
    assert String(min_length=3).validate("s") == "s"
    assert String(allow_blank=True).validate("") == ""
    assert String(allow_blank=False).validate("") == ""
    assert String(trim_whitespace=True).validate("  s  ") == "s"
    assert String(pattern="[a-z]+").validate("s") == "s"
    assert String(format="uuid").validate("13948ab4-4c4a-4c4a-89b4-13948ab4894b") == "13948ab4-4c4a-4c4a-89b4-13948ab4894b"
    assert String(format="date").validate

# Generated at 2022-06-14 14:32:46.954023
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    class FieldExample(Field):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.default = "Test"

    field_example = FieldExample()
    assert field_example.has_default()
    assert field_example.get_default_value() == "Test"



# Generated at 2022-06-14 14:32:55.677833
# Unit test for method validate of class Choice
def test_Choice_validate():
    # case 1: input null and allow_null = True
    choices = [("A", "1"), ("B", "2")]
    value = None
    allow_null = True
    strict = False
    result = None
    obj = Choice(choices = choices, allow_null = True)
    assert obj.validate(value, strict = strict) == result

    # case 2: input null and allow_null = False
    choices = [("A", "1"), ("B", "2")]
    value = None
    allow_null = False
    strict = True
    obj = Choice(choices = choices, allow_null = False)
    try:
        obj.validate(value, strict = strict)
    except ValidationError as result:
        assert result.text == "May not be null."

# Generated at 2022-06-14 14:32:58.303988
# Unit test for method __or__ of class Field
def test_Field___or__():
    field1 = String()
    param = field1
    field1 | field1 | field1
    param | param | param



# Generated at 2022-06-14 14:33:10.930413
# Unit test for method validate of class Union
def test_Union_validate():
    # set up
    def validate_or_error(self, value, *, strict = False):
        return value, None
    
    def has_default(self):
        return True
    
    def get_default_value(self):
        return "default"
    
    class Field:
        def __init__(self, allow_null = True):
            self.allow_null = allow_null
        def validation_error(self, code):
            return code
        def get_error_text(self, code):
            return code
        validate_or_error = validate_or_error
        has_default = has_default
        get_default_value = get_default_value
    
    def test_Union_validate_1():
        string = Field(allow_null = False)
        number = Field()