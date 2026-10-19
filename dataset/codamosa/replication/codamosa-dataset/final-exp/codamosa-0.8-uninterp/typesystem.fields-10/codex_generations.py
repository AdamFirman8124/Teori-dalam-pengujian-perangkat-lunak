

# Generated at 2022-06-14 14:25:34.478951
# Unit test for method validate of class Choice
def test_Choice_validate():
    assert Choice(choices=["a", "b", "c"]).validate("b") == "b"
    assert Choice(choices=["a", "b", "c"]).validate("c") == "c"
    with pytest.raises(ValidationError):
        Choice(choices=["a", "b", "c"]).validate("d")
    assert Choice(choices=["a", "b", "c"], allow_null=True).validate(None) == None
    assert Choice(choices=["a", "b", "c"], allow_null=True).validate("") == None
    with pytest.raises(ValidationError):
        Choice(choices=["a", "b", "c"], allow_null=True).validate("")

# Generated at 2022-06-14 14:25:41.614504
# Unit test for method validate of class Array
def test_Array_validate():
    schema = Array(min_items=1, max_items=2)
    # case 1:
    expected_result = [1, 2]
    actual_result = Array().validate([1, 2])

    assert expected_result == actual_result
    # case 2:
    expected_result = [1,2,3]
    actual_result = Array(min_items=1, max_items=4).validate([1,2,3])

    assert expected_result == actual_result
    # case 3:
    expected_result = 1
    actual_result = Array().validate(1)

    assert expected_result == actual_result
    # case 4:
    expected_result = [1,2]
    actual_result = Array().validate([1,2])

    assert expected_result == actual_result
test_Array

# Generated at 2022-06-14 14:25:49.373833
# Unit test for method validate of class Union
def test_Union_validate():
    schema = Union([String(), String(max_length=10)])
    value, error = schema.validate_or_error("hello")
    assert value == "hello" and error is None

    value, error = schema.validate_or_error("hello world")
    assert error is None
    assert value == "hello world"

    value, error = schema.validate_or_error(123)
    assert value is None
    assert error.messages()[0].code == "union"


# Generated at 2022-06-14 14:25:52.173202
# Unit test for constructor of class Const
def test_Const():
    validator = Const(const="hello")
    assert validator.const == "hello"


# Generated at 2022-06-14 14:25:53.821741
# Unit test for constructor of class Const
def test_Const():
    try:
        schema = Const(const=None, required=True)
    except AssertionError:
        assert False


# Generated at 2022-06-14 14:26:03.128722
# Unit test for method serialize of class Array
def test_Array_serialize():
    test1 = Array(items=String(), min_items=0, max_items=2)
    assert test1.serialize(["a", "b"]) == ["a", "b"]
    assert test1.serialize(["a", "b", "c", "d"]) == ["a", "b"]
    assert test1.serialize([]) == []
    assert test1.serialize(None) == None

    test2 = Array(items=String(), min_items=2, max_items=2)
    assert test2.serialize(["a", "b"]) == ["a", "b"]
    assert test2.serialize(["a", "b", "c", "d"]) == ["a", "b"]
    assert test2.serialize([]) == None
    assert test2.serialize(None) == None

# Generated at 2022-06-14 14:26:08.536849
# Unit test for method validate of class Array
def test_Array_validate():
    validator = Array(items = [String(default=None),Number(default=None)], unique_items=True)
    validator.validate([])
    validator.validate(['a', 2])
    validator.validate(None)
    validator.validate([None, None])
    validator.validate(['a', None])
    validator.validate([None, 1])
    with raises(ValidationError):
        validator.validate(1)
    with raises(ValidationError):
        validator.validate([-1, 2])
    with raises(ValidationError):
        validator.validate(['a', 'b'])
    with raises(ValidationError):
        validator.validate(['b', None])
    with raises(ValidationError):
        validator.valid

# Generated at 2022-06-14 14:26:14.388087
# Unit test for method validate_or_error of class Field
def test_Field_validate_or_error():
    import typesystem
    from typesystem import types
    from typesystem.base import ValidationResult
    error = ""
    try:
        a = typesystem.String()
        b = ValidationResult(value="1",error=error)
        assert a.validate_or_error("1") == b
    except AssertionError:
        print("AssertionError")
    except Exception as e:
        print(e)


# Generated at 2022-06-14 14:26:26.113923
# Unit test for method validate_or_error of class Field
def test_Field_validate_or_error():
    from typesystem import ErrorDetails

    class MyField(Field):
        def validate(self, value: typing.Any, *, strict: bool = False) -> typing.Any:
            if value == "":
                raise ValidationError(code="error_code", text="error_message")

    field = MyField()

    assert isinstance(field.validate_or_error(value=""), ValidationResult)
    assert isinstance(field.validate_or_error(value="")[1], ValidationError)
    assert isinstance(field.validate_or_error(value="")[1].error_details, ErrorDetails)
    assert field.validate_or_error(value="")[1].error_details.code == "error_code"
    assert field.validate_or_error(value="")[1].error_details

# Generated at 2022-06-14 14:26:38.185107
# Unit test for method validate of class Choice
def test_Choice_validate():
    a = Choice(choices = [("aaa", "aaa")], allow_null = True)   
    assert a.validate("aaa") == "aaa"
    assert a.validate(None) == None
    assert a.validate("") == None
    assert a.validate("bbb") == "bbb"
    assert a.validate("xxx") == "xxx"

    b = Choice(choices = [("aaa", "aaa")], allow_null = False)   
    assert b.validate("aaa") == "aaa"
    assert b.validate(None) == None
    assert b.validate("") == None
    assert b.validate("bbb") == "bbb"
    assert b.validate("xxx") == "xxx"


# Generated at 2022-06-14 14:27:05.466420
# Unit test for method validate of class Object
def test_Object_validate():
    schema = Object()
    with pytest.raises(ValidationError):
        schema.validate(None)
    with pytest.raises(ValidationError):
        schema.validate("null")
    with pytest.raises(ValidationError):
        schema.validate("type")

    schema = Object(allow_null=True)
    assert schema.validate(None) is None
    assert schema.validate("type") == "type"
    with pytest.raises(ValidationError):
        schema.validate("null")



# Generated at 2022-06-14 14:27:08.060133
# Unit test for constructor of class String
def test_String():
    try:
        a = String()
    except:
        pass
    assert isinstance(a, String)


# Generated at 2022-06-14 14:27:12.193593
# Unit test for method validate of class Union
def test_Union_validate():
    # Arrange
    unionField = Union([Field(allow_null=True),Field(allow_null=False)],allow_null=True,default_value=3)

    # Act
    result = unionField.validate(None)
    # Assert
    assert result is None


# Generated at 2022-06-14 14:27:18.875025
# Unit test for method validate of class Union
def test_Union_validate():
    class Model:
        p1 = Integer()
        p2 = Integer()

    m1 = Model()
    m1.p1 = 100
    m2 = Model()
    m2.p2 = 200
    m2.p2 = 300

    def func1(m):
        # It will return 100
        return m.p1

    def func2(m):
        # It will return 200
        return m.p2

    m = Union([func1(m1), func2(m2)])
    # Unit test for function validate()
    assert m.validate([1, 2]) == [1, 2]


# Generated at 2022-06-14 14:27:20.249075
# Unit test for method validate of class Boolean
def test_Boolean_validate():
    field = Boolean()
    # value=1 should raise validation error
    with pytest.raises(ValidationError):
        field.validate(value=1)


# Generated at 2022-06-14 14:27:29.367846
# Unit test for method serialize of class String
def test_String_serialize():
    one = String(max_length = 10, format = "uuid")
    print(one)
    assert one.serialize("b5dafa89-7fef-4b74-8c66-dabfa531c9cf") == UUID("b5dafa89-7fef-4b74-8c66-dabfa531c9cf")
    assert one.serialize("") == ""
    assert one.serialize("b5dafa89-7fef-4b") == "b5dafa89-7fef-4b"
    #print(one.serialize("b5dafa89-7fef-4b74-8c66-dabfa531c9cf"))
    two = String(format = "time")
    print(two)
    #print(two.serialize

# Generated at 2022-06-14 14:27:39.186110
# Unit test for method validate of class Array
def test_Array_validate():
    import numpy as np
    import pandas as pd

    # test cases
    # test case 1:
    input_1 = np.arange(12).reshape(3, 4)
    expect_1 = "this field must be a list"

    # test case 2: 
    # test case 2.1:
    input_2_1 = [1, 2, 3, 4, 5]
    expect_2_1 = input_2_1
    # test case 2.2:
    input_2_2 = []
    expect_2_2 = "this field must not be empty"
    # test case 2.3:
    input_2_3 = [1, 2, 3, 4]
    expect_2_3 = "this field must have at least 5 items"
    # test case 2.4:
    input

# Generated at 2022-06-14 14:27:42.104748
# Unit test for method validate of class Number
def test_Number_validate():
    number_field = Number()
    assert number_field.validate(value=1)==1
    assert number_field.validate(value=None)==None

# Generated at 2022-06-14 14:27:44.943898
# Unit test for method validate of class Choice
def test_Choice_validate():
    c1 = Choice(choices=["A","B"], allow_null=True)
    print(c1.validate("A"))
    print(c1.validate(""))



# Generated at 2022-06-14 14:27:57.415891
# Unit test for method validate of class Choice
def test_Choice_validate():    
    choices = ["red", "blue", "green"]
    choice = Choice(choices=choices)
    assert choice.validate("red")=="red"
    assert choice.validate("red")!="blue"

    c1 = Choice(choices=choices, allow_null=True)
    assert c1.validate(None) == None
    assert c1.validate(None) != "blue"

    with pytest.raises(ValidationError):
        c2 = Choice(choices=choices)
        c2.validate(None)    

    with pytest.raises(ValidationError):
        c3 = Choice(choices=choices, allow_null=True, strict=False)
        c3.validate("")


# Generated at 2022-06-14 14:28:08.165462
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    field  = Field()
    assert field.get_default_value() == None
    field.default = 100
    assert field.get_default_value() == 100
    field.default = lambda : 200
    assert field.get_default_value() == 200

# Generated at 2022-06-14 14:28:11.087297
# Unit test for method validate of class Choice
def test_Choice_validate():
    field = Choice(choices=["foo", "bar"])
    assert field.validate("foo") == "foo"
    assert field.validate("bar") == "bar"
    with pytest.raises(ValidationError) as excinfo:
        field.validate("fizz")
    assert str(excinfo.value) == "Not a valid choice."



# Generated at 2022-06-14 14:28:16.657307
# Unit test for method __or__ of class Field
def test_Field___or__():
    fields = ['int()','string()','float()']
    main_field = Union(any_of=fields)
    assert(
        (main_field | fields[0]) ==
        Union(any_of=fields)
    )
    assert(
        (fields[0] | main_field) ==
        Union(any_of=fields)
    )
    assert(
        (fields[0] | fields[1]) ==
        Union(any_of=[fields[0],fields[1]])
    )


# Generated at 2022-06-14 14:28:29.133966
# Unit test for method validate of class Object
def test_Object_validate():
    class UserSchema(Schema):
        name = String(max_length=20)

    class CommentSchema(Schema):
        comment_id = Integer()
        user = Object(properties={"name": String()})

    schema = Object(
        properties={
            "id": Integer(),
            "comments": ListObject(CommentSchema),
            "users": ListObject(UserSchema),
        }
    )

    data = {
        "id": 123,
        "comments": [
            {"comment_id": 1, "user": {"name": "John Doe"}},
            {"comment_id": 2, "user": {"name": "Jane Doe"}},
        ],
        "users": [{"name": "John"}, {"name": "Jane"}, {"name": "Jack"}],
    }


# Generated at 2022-06-14 14:28:33.425657
# Unit test for method __or__ of class Field
def test_Field___or__():
    any_of = [typesystem.String(), typesystem.Number()]
    union_Field_Field = Union(any_of=any_of)
    assert (typesystem.String() | typesystem.Number()) == union_Field_Field



# Generated at 2022-06-14 14:28:36.709325
# Unit test for method validate of class Union
def test_Union_validate():
    obj = Union([
    String(nullable=False),
    Integer(nullable=False)
])
    assert obj.validate('True') == 'True'

# Generated at 2022-06-14 14:28:38.464614
# Unit test for method validate of class Object
def test_Object_validate():
    mapper_object = Object()
    assert not mapper_object.validate('test')

# Generated at 2022-06-14 14:28:50.381812
# Unit test for constructor of class String
def test_String():
  s = String(title="Name", format="uuid", allow_null=True, allow_blank=True)
  assert(s.__dict__["title"] == "Name")
  assert(s.__dict__["format"] == "uuid")
  assert(s.__dict__["allow_null"] == True)
  assert(s.__dict__["allow_blank"] == True)
  assert(s.__dict__["trim_whitespace"] == True)
  assert(s.__dict__["max_length"] == None)
  assert(s.__dict__["min_length"] == None)
  assert(s.__dict__["format"] == "uuid")
  assert(s.__dict__["pattern"] == None)
  assert(s.__dict__["pattern_regex"] == None)




# Generated at 2022-06-14 14:28:53.189839
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    f = Field(default=7)
    assert f.get_default_value() == 7

    f = Field(default=lambda: 7)
    assert f.get_default_value() == 7


# Generated at 2022-06-14 14:28:59.456474
# Unit test for method validate of class Choice
def test_Choice_validate():
    # Case 1: InvalidChoiceError
    test_choice = Choice()
    test_choice.choices = [("Ape", "Banana"),["E", "F"]]
    with pytest.raises(ValidationError):
        test_choice.validate("G", strict=False)
        test_choice.validate("", strict=True)


# Generated at 2022-06-14 14:29:16.507290
# Unit test for method validate of class Boolean
def test_Boolean_validate():
    # initialize
    field_Boolean = Boolean()
    # test several values for value and strict
    assert field_Boolean.validate("true", strict = False) == True
    assert field_Boolean.validate("false", strict = False) == False
    assert field_Boolean.validate("on", strict = False) == True
    assert field_Boolean.validate("off", strict = False) == False
    assert field_Boolean.validate("1", strict = False) == True
    assert field_Boolean.validate("0", strict = False) == False
    assert field_Boolean.validate("", strict = False) == False
    assert field_Boolean.validate(1, strict = False) == True
    assert field_Boolean.validate(0, strict = False) == False
    assert field_Boolean

# Generated at 2022-06-14 14:29:17.740348
# Unit test for constructor of class Const
def test_Const():
    field = Const(10)
    assert field.const == 10
    assert field.allow_null == False


# Generated at 2022-06-14 14:29:19.230229
# Unit test for constructor of class Const
def test_Const():
    assert Const(const = "Dog")

test_Const()



# Generated at 2022-06-14 14:29:29.555308
# Unit test for method validate of class Array
def test_Array_validate():
    # Test for invalidate value
    json_value = typeecdsa.Signature()
    json_validator = Array(unique_items=True, additional_items=False, max_items=None, min_items=None, items=None)
    try:
        json_validator.validate(json_value)
    except ValidationError as validationError:
        print(validationError.messages)

    # Test for invalidate value
    json_value = 'testing'
    json_validator = Array(unique_items=True, additional_items=False, max_items=None, min_items=None, items=None)
    try:
        json_validator.validate(json_value)
    except ValidationError as validationError:
        print(validationError.messages)

    # Test for invalidate value


# Generated at 2022-06-14 14:29:34.496262
# Unit test for method validate of class Choice
def test_Choice_validate():
    a = Choice(choices=[('delhi', 'Delhi'), ('mumbai', 'Mumbai'), ('pune', 'Pune')])
    a.validate('delhi')
    a.validate('delhi', strict=True)
    with raises(ValidationError):
        a.validate('goa')
    with raises(ValidationError):
        a.validate('goa', strict=True)
    with raises(ValidationError):
        a.validate('')



# Generated at 2022-06-14 14:29:44.366520
# Unit test for method validate of class Array
def test_Array_validate():
    schema = Array()
    assert schema.validate(None, strict=False) is None
    assert schema.validate([], strict=False) == []
    assert schema.validate(["a", 1, [2], {"b": 3}], strict=False) == [
        "a",
        1,
        [2],
        {"b": 3},
    ]
    assert schema.validate(1, strict=False) == [1]
    assert schema.validate("a", strict=False) == ["a"]

    schema = Array(min_items=2, max_items=4)
    assert schema.validate([1, 2], strict=False) == [1, 2]
    assert schema.validate([1], strict=False) == [1]
    assert schema.validate([], strict=False) == []
   

# Generated at 2022-06-14 14:29:50.949298
# Unit test for method __or__ of class Field
def test_Field___or__():
    class MyUnionField(Field):
        def __init__(self, **kwargs):
            kwargs['any_of'] = kwargs.get('any_of', [])
            kwargs['any_of'].append(String(enum=['hi','hello','hey']))
            super().__init__(**kwargs)
    assert (Integer() | String()).any_of[0] == Integer()
    assert (Integer() | String() | MyUnionField()).any_of[1] == String()
    assert (Integer() | String() | MyUnionField()).any_of[2].any_of[0] == String()
    assert (Integer() | String() | MyUnionField()).any_of[2].any_of[1] == 'hi'



# Generated at 2022-06-14 14:29:54.385139
# Unit test for method __or__ of class Field
def test_Field___or__():
    field1 = Text()
    field2 = Integer()
    field = field1 | field2
    assert isinstance(field, Union)
    assert len(field.any_of) == 2



# Generated at 2022-06-14 14:29:59.068837
# Unit test for method validate of class Object
def test_Object_validate():
    # Create an instance of Object
    Object_instance = Object()
    # Create a property key
    key = "description"
    # Create a property value
    value = "This is a description"
    # Get the validation of the Object instance
    validate_pass = Object_instance.validate(value)
    validate_fail = Object_instance.validate(value, strict=True)
    # Assert that the validation is as expected
    # assert validate_pass == {key: value}
    assert validate_fail is None

# Generated at 2022-06-14 14:30:12.317057
# Unit test for method validate of class Choice
def test_Choice_validate():
    choices = [("en", "English"), ("fr", "French")]
    result = Choice(choices=choices, allow_null=False).validate("en")
    assert result == "en"
    result = Choice(choices=choices, allow_null=True).validate("en")
    assert result == "en"
    with pytest.raises(ValidationError):
        Choice(choices=choices, allow_null=True).validate("it")
    result = Choice(choices=choices, allow_null=True).validate("")
    assert result is None
    # Test choice can be a list of choices
    with pytest.raises(ValidationError):
        Choice(choices=choices, allow_null=True).validate(["en", "fr", "it"])

# Generated at 2022-06-14 14:30:25.501298
# Unit test for method __or__ of class Field
def test_Field___or__():
    assert Field() | Field() | Field() | Field() == Union(any_of=[Field(), Field(), Field(), Field()])

# Generated at 2022-06-14 14:30:34.018513
# Unit test for method validate of class Number
def test_Number_validate():
  n = Number()
  try:
    n.validate(1)
  except Exception as x:
    print(str(x))
  n.validate(None)
  n.validate(1.1, strict=True)
  try:
    n.validate('1')
  except Exception as x:
    print(str(x))
  try:
    n.validate(True)
  except Exception as x:
    print(str(x))
  try:
    n.validate(float('inf'))
  except Exception as x:
    print(str(x))
  n = Number(maximum=0.1)
  try:
    n.validate(0.2)
  except Exception as x:
    print(str(x))

# Generated at 2022-06-14 14:30:38.942501
# Unit test for method __or__ of class Field
def test_Field___or__():
    assert str(Field() | Field()) == "<Union: (Field, Field)>"
    assert str(Field() | Field() | Field()) == "<Union: (Field, Field, Field)>"
    assert str(Field() | (Field() | Field())) == "<Union: (Field, Field, Field)>"



# Generated at 2022-06-14 14:30:43.690539
# Unit test for method validate of class Choice
def test_Choice_validate():
    choice = Choice(choices=["hello", "world"])
    assert isinstance(choice, Field), "choice is a field"
    assert choice.choices == [("hello", "hello"), ("world", "world")], "choices is valid"
    answer = choice.validate("hello")
    assert answer == "hello", "validate method is valid"



# Generated at 2022-06-14 14:30:52.458625
# Unit test for method __or__ of class Field

# Generated at 2022-06-14 14:31:03.643745
# Unit test for method validate of class String
def test_String_validate():
    obj3 = String()
    assert obj3.validate('123')=='123'
    assert obj3.validate('abc')=='abc'
    assert obj3.validate('123.0')=='123.0'
    assert obj3.validate('2003-02-12')=='2003-02-12'
    assert obj3.validate('2003-02-12T19:05:03.288Z')=='2003-02-12T19:05:03.288Z'
    assert obj3.validate('123.0')=='123.0'
    assert obj3.validate('1.23E2')=='1.23E2'
    assert obj3.validate('123')=='123'
    assert obj3.validate('3')=='3'
    assert obj3.validate

# Generated at 2022-06-14 14:31:12.286821
# Unit test for method validate of class Choice
def test_Choice_validate():
    unknown_value = "value"
    choice = Choice(choices=[("key", "value")])
    assert choice.validate(unknown_value) == unknown_value
    choice = Choice(choices=[("key", "value"), ("key1", "value1")])
    assert choice.validate(unknown_value) == unknown_value
    choice = Choice(choices=[("key", "value"), ("key1", "value1")])
    assert choice.validate(unknown_value) == unknown_value
    choice = Choice(choices=[("key", "value"), ("key1", "value1")])
    assert choice.validate(unknown_value) == unknown_value


# Generated at 2022-06-14 14:31:16.185359
# Unit test for method __or__ of class Field
def test_Field___or__():
    import typesystem
    field1 = typesystem.Field()
    field2 = typesystem.Field()
    field3 = typesystem.Field()
    union = (field1|field2)
    assert len(union.any_of) == 2
    union = union|field3
    assert len(union.any_of) == 3



# Generated at 2022-06-14 14:31:22.924279
# Unit test for method __or__ of class Field
def test_Field___or__():
    field1 = None  # type: Field
    field2 = None  # type: Field
    field3 = None  # type: Field
    field4 = None  # type: Field
    field5 = None  # type: Field
    any_of1 = None  # type: typing.List[Field]
    any_of2 = None  # type: typing.List[Field]
    union_field = None  # type: Union
    assert field1 or field2
    assert field3 or field4
    assert field5 or field3
    assert field5 or field4
    assert field1 or field2 or field3 or field4
    assert field1 or field2 or field3 or field4 or field5
    assert field1 or field2 or union_field



# Generated at 2022-06-14 14:31:31.383270
# Unit test for method validate of class String
def test_String_validate():
    # only text, no length or format
    t1 = String()
    assert t1.validate('this is a string') == 'this is a string'
    try:
        t1.validate('')
    except ValidationError as e:
        assert str(e) == 'Must not be blank.'
    try:
        t1.validate(' ')
    except ValidationError as e:
        assert str(e) == 'Must not be blank.'
    try:
        t1.validate(None)
    except ValidationError as e:
        assert str(e) == 'Must be a string.'
    # with length
    t2 = String(max_length=3, min_length=1)

# Generated at 2022-06-14 14:31:40.824971
# Unit test for constructor of class String
def test_String():
    str1 = String()
    assert str1.errors["type"] == "Must be a string."
    assert str1.errors["max_length"] == "Must have no more than {max_length} characters."
    assert str1.get_default_value() == None
    
    
    
    

# Generated at 2022-06-14 14:31:41.393822
# Unit test for constructor of class Const
def test_Const():
    Const(const=1)

# Generated at 2022-06-14 14:31:53.466871
# Unit test for method validate of class Object
def test_Object_validate():
    fields = {
        "name": String(required=True, min_length=1, max_length=10),
        "age": Integer(required=True, minimum=18, maximum=100),
        "address": Object(
            required=True,
            properties={
                "street": String(required=True, min_length=1, max_length=20),
                "city": String(required=True, min_length=1, max_length=20),
                "state": String(required=True, min_length=1, max_length=20),
            },
        ),
    }

# Generated at 2022-06-14 14:31:58.945072
# Unit test for method validate of class Choice
def test_Choice_validate():
    assert Choice().validate(None) == None
    assert Choice().validate("") == ""
    assert Choice().validate("1") == "1"
    assert Choice(choices=["1"]).validate("1") == "1"
    assert Choice(choices=["1", "2"]).validate("1") == "1"
    assert Choice(choices=("1", "2")).validate("1") == "1"
    assert Choice(choices=[("1", "2")]).validate("1") == "1"
    assert Choice(choices=[("1", "2"), ("3", "4")]).validate("3") == "3"

    with pytest.raises(ValidationError) as excinfo:
        Choice().validate(None)
    assert excinfo.value.code == "null"


# Generated at 2022-06-14 14:32:05.620062
# Unit test for method validate of class Object
def test_Object_validate():
    test_object = Object()
    test_dict = {'a':1, 'c':2}
    test_non_dict = 'd'
    assert test_object.validate(test_dict) == test_dict
    try:
        test_object.validate(test_non_dict)
    except ValidationError as e:
        assert e.messages[0].text == 'Must be an object.'


# Generated at 2022-06-14 14:32:13.510319
# Unit test for constructor of class String
def test_String():
    str_var = String(title="Name", max_length=10)
    assert isinstance(str_var, String)
    assert str_var.title == "Name"
    assert str_var.max_length == 10
    assert str_var.errors == String.errors
    str_default = String(title="Name", max_length=10, default="hello world")
    assert str_default.default == "hello world"
    assert str_default.allow_null == False
    str_null = String(title="Name", max_length=10, allow_null=True)
    assert str_null.allow_null == True
    assert str_null.default == None
    str_blank = String(title="Name", max_length=10, allow_blank=True)
    assert str_blank.default == ""


# Generated at 2022-06-14 14:32:23.786857
# Unit test for method validate of class Object
def test_Object_validate():
    class MultipleOfFoo(Field):
        def validate(self, value):
            if not (value * (1 / self.multiple_of)).is_integer():
                raise self.validation_error("multiple_of")
            return value

    field = Object(
        properties={
            "foo": Decimal(multiple_of=0.5),
            "bar": Decimal(multiple_of=0.3),
            "baz": Decimal(minimum=10),
            "qux": MultipleOfFoo(multiple_of=0.2),
        },
        additional_properties=Decimal(),
        require_all=True,
    )

# Generated at 2022-06-14 14:32:28.737123
# Unit test for method validate of class String
def test_String_validate():
    a = String(max_length=5)
    assert a.validate("123456") == None

    a = String(max_length=10)
    assert a.validate("123456") == "123456"


# Generated at 2022-06-14 14:32:32.208038
# Unit test for method validate of class Array
def test_Array_validate():
    Arr = Array(items=String(format="uuid"))
    print(Arr.validate(['test1','test2','test3','test4','test5']))

test_Array_validate()


# Generated at 2022-06-14 14:32:36.299826
# Unit test for method validate of class Choice
def test_Choice_validate():
    choices = [("a", "A"), ("b", "B")]
    choices_field = Choice(choices=choices)
    assert choices_field.validate("b") == "b"
    assert choices_field.validate("B") == "b"



# Generated at 2022-06-14 14:32:52.839876
# Unit test for method validate of class Union
def test_Union_validate():
    field = Union([Integer(), String()])
    assert field.validate(10) == 10 and field.validate("s") == "s" and \
        field.validate("") == "" and field.validate(" ") == " " and \
        field.validate("1") == "1" and field.validate("-") == "-" and \
        field.validate("@") == "@" and field.validate("a") == "a" and \
        field.validate("2") == "2" and field.validate("-1") == "-1" and \
        field.validate("-0") == "-0" and field.validate("0") == "0" and \
        field.validate("01") == "01" and field.validate("10") == "10" and \
        field.valid

# Generated at 2022-06-14 14:32:56.959754
# Unit test for constructor of class String
def test_String():
    s = String(title ="Hello",description="Hello")
    assert s.title == "Hello"
    assert s.description == "Hello"
    assert s.allow_blank == False
    assert s.trim_whitespace == True
    assert s.max_length == None
    assert s.min_length == None
    assert s.pattern == None
    assert s.format == None
    assert s._creation_counter == 0


# Generated at 2022-06-14 14:33:02.421685
# Unit test for method validate of class Union
def test_Union_validate():
    any_of = [String()]
    u = Union(any_of=any_of)
    value_1 = 'Hello World!'
    value_2 = 5
    print(u.validate(value_1))
    print(u.validate(value_2))
test_Union_validate()


# Generated at 2022-06-14 14:33:15.194993
# Unit test for method validate of class Union
def test_Union_validate():
    field = Union(any_of=[Boolean(), Number(), String()])
    assert field.validate(True) == True
    assert field.validate(10) == 10
    assert field.validate("String") == "String"
    assert field.validate(None) == None

    field = Union(any_of=[Boolean(), Number(), String()])
    field.allow_null = False
    try:
        field.validate(None)
    except ValidationError as e:
        assert e.messages == [Message(code="null", text="May not be null.")]
    else:
        assert False, "Expected ValidationError"

    field = Union(any_of=[Boolean(), Number(), String()])