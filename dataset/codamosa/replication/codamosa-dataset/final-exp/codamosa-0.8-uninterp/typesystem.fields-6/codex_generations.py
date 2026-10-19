

# Generated at 2022-06-14 14:25:36.959010
# Unit test for method validate of class Array
def test_Array_validate():
    messages = []
    for item in [2, 3]:
        validator = Array(items=Number())
        _, error = validator.validate_or_error(item)
        if error is not None:
            messages += error.messages()
    assert len(messages) == 2

# Generated at 2022-06-14 14:25:41.569869
# Unit test for method serialize of class String
def test_String_serialize():
    field = String(format="date")
    assert field.format == "date"
    assert field.serialize(datetime.datetime.now()) == datetime.datetime.now().strftime("%Y-%m-%d")
# end of unit test



# Generated at 2022-06-14 14:25:47.913785
# Unit test for method serialize of class String
def test_String_serialize():
    x = String()
    assert x.serialize("2020-04-13") == "2020-04-13"
    assert x.serialize("") == ""
    assert x.serialize(" ") == " "
    assert x.serialize("  ") == "  "
    assert x.serialize("123") == "123"
    assert x.serialize("abc") == "abc"

# Generated at 2022-06-14 14:25:55.436235
# Unit test for method serialize of class String
def test_String_serialize():
    field = String(format="datetime")
    date = datetime.datetime(2020, 1, 2, 12, 0, 0)
    assert field.serialize(date) == "2020-01-02T12:00:00"
    field.format = "date"
    assert field.serialize(date) == "2020-01-02"
    field.format = "time"
    assert field.serialize(date) == "12:00:00"


# Generated at 2022-06-14 14:26:01.833163
# Unit test for method validate of class Union
def test_Union_validate():
    test_any_of = [Field(type="integer"),Field(type="array")]
    test_field = Union(any_of = test_any_of)
    assert test_field.validate(["a","b"]) ==  ["a","b"]
    assert test_field.validate(1) ==  1
    try:
        test_field.validate(None)
    except ValidationError:
        pass
    try:
        test_field.validate(False)
    except ValidationError:
        pass


# Generated at 2022-06-14 14:26:07.741954
# Unit test for method __or__ of class Field
def test_Field___or__():
    from .fields import String
    from .fields import Integer
    from .fields import Boolean
    from .fields import Float
    from .fields import Decimal
    from .fields import List
    from .fields import Union

    assert (String() | Integer()).any_of[0] == String()
    assert (String() | Integer()).any_of[1] == Integer()
    assert (String() | String()).any_of[0] == String()
    assert (String() | String()).any_of[1] == String()
    assert (String() | Integer() | List(Integer())).any_of[0] == String()
    assert (String() | Integer() | List(Integer())).any_of[1] == Integer()
    assert (String() | Integer() | List(Integer())).any_of[2] == List(Integer())

# Generated at 2022-06-14 14:26:09.474740
# Unit test for method serialize of class String
def test_String_serialize():
    obj = String(format = "date")
    assert obj.serialize(ts) == "2015-01-01"


# Generated at 2022-06-14 14:26:11.703971
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    field = Field(title="year", description="input year")
    print(field.get_default_value())

test_Field_get_default_value()


# Generated at 2022-06-14 14:26:14.222409
# Unit test for method validate of class Array
def test_Array_validate():
    arr = Array()
    obj = [1,2,3]
    assert arr.validate(obj) == obj
    obj = {"1":"2"}
    assert arr.validate(obj) == obj
    obj = None
    assert arr.validate(obj) == obj
    obj = ""
    assert arr.validate(obj) == obj
test_Array_validate()


# Generated at 2022-06-14 14:26:16.017640
# Unit test for method serialize of class String
def test_String_serialize():
    result = String().serialize("2020-10-13")
    assert result == "2020-10-13"



# Generated at 2022-06-14 14:26:34.660759
# Unit test for method validate of class Choice
def test_Choice_validate():
  from unittest import TestCase
  from field_validation import Choice
  choice = Choice(choices=[('a', 'a')])
  try:
    choice.validate('b')
  except ValidationError as e:
    assert True
  else:
    assert False    


# Generated at 2022-06-14 14:26:38.785162
# Unit test for method validate of class Union
def test_Union_validate():
    class MockField:
        def __init__(self):
            self.allow_null = True
    child1 = MockField()
    child2 = MockField()
    child3 = MockField()
    child4 = MockField()
    child5 = MockField()
    child6 = MockField()
    child7 = MockField()
    child8 = MockField()
    child9 = MockField()
    field = Union([None, child1, child2, child3, child4, child5, child6, child7, child8, child9])

    # Test case 1
    try:
        result = field.validate(None)
    except ValidationError as e:
        result = e.messages()
    assert result == []

    # Test case 2

# Generated at 2022-06-14 14:26:48.922238
# Unit test for method __or__ of class Field
def test_Field___or__():
    class Field1(Field):
        pass
    class Field2(Field):
        pass
    class Field3(Field):
        pass
    f1 = Field1()
    f2 = Field2()
    f3 = Field3()
    f4 = Field1()
    f5 = Field2()
    f6 = Field3()
    assert Union(any_of=[f1, f2, f3]).any_of == [f1, f2, f3]
    assert (f1 | f2 | f3).any_of == [f1, f2, f3]
    assert (f1 | (f2 | f3)).any_of == [f1, f2, f3]

# Generated at 2022-06-14 14:26:55.892284
# Unit test for method validate of class Object
def test_Object_validate():
    assert Object().validate({"a":1}) == {"a":1}
    assert Object(name="a").validate({"a":1}) == {"a":1}
    assert Object(properties={"a":Boolean()}).validate({"a":True}) == {"a":True}
    assert Object(properties={"a":Boolean()}).validate({"a":False}) == {"a":False}


# Generated at 2022-06-14 14:26:59.120479
# Unit test for method serialize of class Array
def test_Array_serialize():
    # Define data
    data = [0, 10, 20]
    # Define schema
    schema = Array(items=Integer())
    # Verify the result
    assert schema.serialize(data) == data


# Generated at 2022-06-14 14:27:06.275377
# Unit test for method validate of class Choice
def test_Choice_validate():
    choice = Choice(choices=[('1','1'),('2','2'),('3','3')])
    assert choice.validate('1') =='1'
    assert choice.validate(None) is None
    assert choice.validate('') == ''
    assert choice.validate(1) == '1'
    with pytest.raises(ValidationError) as exc_info:
        choice.validate(4)
    assert repr(exc_info.value) == "ValidationError(code='choice', text='Not a valid choice.')"
    with pytest.raises(ValidationError) as exc_info:
        choice.validate('4')
    assert repr(exc_info.value) == "ValidationError(code='choice', text='Not a valid choice.')"



# Generated at 2022-06-14 14:27:16.252322
# Unit test for constructor of class String
def test_String():
    S = String(title="", description="")
    assert S.errors == {
        "type": "Must be a string.",
        "null": "May not be null.",
        "blank": "Must not be blank.",
        "max_length": "Must have no more than {max_length} characters.",
        "min_length": "Must have at least {min_length} characters.",
        "pattern": "Must match the pattern /{pattern}/.",
        "format": "Must be a valid {format}.",
    }
    assert S.allow_blank == False
    assert S.trim_whitespace == True
    assert S.max_length == None
    assert S.min_length == None
    assert S.format == None
    assert S.pattern == None
    assert S.pattern_regex == None

# Unit test

# Generated at 2022-06-14 14:27:18.544143
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    class MyField(Field):
        def __init__(self):
            self.default = 1
    assert MyField().get_default_value() == 1

# Generated at 2022-06-14 14:27:23.192732
# Unit test for method validate of class Array
def test_Array_validate():
    schema = Array(
        property_names=String(read_only=True),
        min_items=2,
        max_items=20,
        additional_items=Boolean(read_only=True),
    )
    # test for correct value
    sample1 = [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
    ]
    assert schema.validate(sample1) == sample1
    # test for wrong value

# Generated at 2022-06-14 14:27:34.397068
# Unit test for method validate of class Array
def test_Array_validate():
    from jsonschema_dev_toolkit.validators import OneOf
    from jsonschema_dev_toolkit.validators import String
    from jsonschema_dev_toolkit.validators import ValidationError
    from jsonschema_dev_toolkit.validators import Array
    
    field = Array(items=[String(), String()], min_items=2, max_items=2)
    field.validate(['a', 'b'])
    field.validate(['a', 'b', 'c'])
    try:
        field.validate(['a'])
    except ValidationError as e:
        assert e.code == 'min_items'
    
    field = Array(items=String(), min_items=2)

# Generated at 2022-06-14 14:27:59.000028
# Unit test for method __or__ of class Field
def test_Field___or__():
    # Testing when the self type is Union
    union1 = Union(any_of=[String()])
    string1 = String()
    union2 = union1 | string1
    assert union2.any_of == [String(), String()]

    # Testing when the self type is not Union
    string1 = String()
    string2 = String()
    union1 = string1 | string2
    assert union1.any_of == [String(), String()]


# Generated at 2022-06-14 14:28:06.854470
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    class TestField(Field):
        def validate(self, value: typing.Any, *, strict: bool = False) -> typing.Any:
            raise NotImplementedError()  # pragma: no cover
        def serialize(self, obj: typing.Any) -> typing.Any:
            raise NotImplementedError()  # pragma: no cover

    f = TestField()
    assert f.has_default() == False
    assert f.get_default_value() == None

    f.default = 5
    assert f.has_default() == True
    assert f.get_default_value() == 5

    f.default = lambda : 6
    assert f.has_default() == True
    assert f.get_default_value() == 6



# Generated at 2022-06-14 14:28:12.520931
# Unit test for method validate of class Array
def test_Array_validate():
    array = Array(
        items=String(),
        additional_items=False,
        min_items=2,
        max_items=3,
        allow_null=True,
        null_choice="",
    )
    value, error = array.validate_or_error(None)
    assert value is None
    assert error is None

    value, error = array.validate_or_error([1])
    assert value is None
    assert error is not None

    value, error = array.validate_or_error(["", "", ""])
    assert value == ["", "", ""]
    assert error is None

    value, error = array.validate_or_error(["", "", "", ""])
    assert value is None
    assert error is not None



# Generated at 2022-06-14 14:28:20.124964
# Unit test for method validate of class Union
def test_Union_validate():
    class TestSchema(Schema):
        a = Union(any_of=[Int()])
        b = Union(any_of=[Int()])

    assert TestSchema().deserialize({"a": "1", "b": "1"}) == {"a": 1, "b": 1}
    try:
        TestSchema().deserialize({"a": [1, 1], "b": 1})
    except ValidationError:
        pass
    else:
        assert False



# Generated at 2022-06-14 14:28:26.255674
# Unit test for method validate of class Union
def test_Union_validate():
    any_of = [String(), Int()]
    union = Union(any_of)
    assert union.validate("anyString") == "anyString"
    assert union.validate(666) == 666
    with pytest.raises(ValidationError):
        union.validate(1.23)
    with pytest.raises(ValidationError):
        union.validate({})

# Generated at 2022-06-14 14:28:28.177727
# Unit test for method __or__ of class Field
def test_Field___or__():
    from typesystem import String
    from typesystem import Boolean

    assert (String() | Boolean())



# Generated at 2022-06-14 14:28:35.442179
# Unit test for method __or__ of class Field
def test_Field___or__():
    from typesystem import Str, Number, Union
    number = Number()
    string = Str()

    # field | field
    assert (number | string).any_of == [number, string]
    # field | union
    assert (number | (string | number)).any_of == [number, string, number]
    # union | field
    assert ((number | string) | number).any_of == [number, string, number]



# Generated at 2022-06-14 14:28:38.808948
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
  # Arrange
  f = Field(title="", description="", default=NO_DEFAULT, allow_null=False)
  # Act 
  actual = f.get_default_value()
  # Assert
  assert actual == NO_DEFAULT

# Generated at 2022-06-14 14:28:45.202042
# Unit test for method __or__ of class Field
def test_Field___or__():
    from .any_of import any_of
    from .union import Union
    from .field import Field
    from .field import field

    actual = Field() | Field()
    assert type(actual) == Union

    actual = Field() | Field() | Field()
    assert type(actual) == Union

    actual = Field() | Field() | Field() | Field()
    assert type(actual) == Union



# Generated at 2022-06-14 14:28:57.500289
# Unit test for method validate of class Array
def test_Array_validate():
    S = Array(items=Integer())
    S.validate([])
    S.validate([1])
    S.validate([1, 2])
    S.validate([1, 2, 3])
    S.validate([1, 2, 3, 4])
    S.validate([1, None, 3, 4])
    S.validate([1, None, 3, 4], strict=True)
    S.validate([1, 2, None, 4])
    S.validate([1, 2, 3, None])

    S = Array(items=Integer(allow_null=True))
    S.validate([])
    S.validate([1])
    S.validate([1, 2])
    S.validate([1, 2, 3])

# Generated at 2022-06-14 14:29:12.504414
# Unit test for method serialize of class Array
def test_Array_serialize():
    from datetime import datetime, date, time
    from decimal import Decimal

    field = Array(items=String())
    assert field.serialize(["123", "345"]) == ["123", "345"]
    field = Array(items=Integer())
    assert field.serialize([1, 23]) == [1, 23]
    field = Array(items=Float())
    assert field.serialize([1.2, 3.45]) == [1.2, 3.45]
    field = Array(items=Boolean())
    assert field.serialize([True, False]) == [True, False]
    field = Array(items=Date())
    assert field.serialize([datetime(1999, 12, 31).date()]) == ["1999-12-31"]
    field = Array(items=Time())

# Generated at 2022-06-14 14:29:13.949749
# Unit test for method __or__ of class Field
def test_Field___or__():
    # Test for method __or__
    # TODO
    assert True == True


# Generated at 2022-06-14 14:29:20.550812
# Unit test for method validate of class Choice
def test_Choice_validate():
    choice = Choice(choices=["cat","dog"])
    assert(choice.validate("cat") == "cat")
    assert(choice.validate("dog") == "dog")
    assert(choice.validate(None) == None)
    # assert(choice.validate("") == None)
    try:
        choice.validate("fish") == "fish"
    except ValidationError as e:
        assert(e.code == "choice")


# Generated at 2022-06-14 14:29:25.029195
# Unit test for method validate of class Object
def test_Object_validate():
    obj_field = Object(required=["name", "age"])
    d = {"name": "Bob", "age": 20}
    assert obj_field.validate(d) is not None
    assert obj_field.validate(d) == {"name": "Bob", "age": 20}


# Generated at 2022-06-14 14:29:28.941000
# Unit test for method validate of class Choice
def test_Choice_validate():
    assert Choice().validate(None)==None
    assert Choice().validate(1)==1
    assert Choice().validate('a')=='a'
    assert Choice().validate('a','b','c')=='a'
    assert Choice().validate(1,'a','b','c')==1



# Generated at 2022-06-14 14:29:31.449979
# Unit test for constructor of class Choice
def test_Choice():
    choices = ["a","b"]
    assert (choices == Choice(choices = choices).choices)
    assert (choices == Choice(choices = tuple(choices)).choices)
    

# Generated at 2022-06-14 14:29:42.647914
# Unit test for method validate of class Array
def test_Array_validate():
    # test case 1:
    print("test case 1: array with min_items, max_items and allow_null")
    field = Array(
        min_items=1, max_items=2, allow_null=True,
        items=String(max_length=3)
    )
    value = ['hello', 'world']
    try:
        field.validate(value)
        assert True, 'pass test case 1'
    except ValidationError as e:
        assert False, 'fail test case 1'
    # test case 2:
    print("test case 2: array with min_items, max_items and allow_null")
    field = Array(
        min_items=1, max_items=2, allow_null=True,
        items=String(max_length=3)
    )

# Generated at 2022-06-14 14:29:49.546238
# Unit test for constructor of class String
def test_String():
    test_string = String(
        title="Test",
        description="Test",
        default = "",
        allow_null = False,
        allow_blank = False,
        trim_whitespace = True,
        max_length = None,
        min_length = None,
        pattern = None,
        format = None
    )
    return test_string


# Generated at 2022-06-14 14:29:54.307764
# Unit test for method validate of class Union
def test_Union_validate():
    obj = Union(any_of=[Integer(), Number()])
    print(obj.validate(4))
    print(obj.validate(0.4))
    print(obj.validate(5.6))
if __name__ == "__main__":
    test_Union_validate()


# Generated at 2022-06-14 14:30:06.727548
# Unit test for method validate of class Choice
def test_Choice_validate():
    field = Choice(choices=[
    ("a", "A"),
    ("b", "B"),
    ("c", "C ")
  ])
    assert field.validate(None) == None
    assert field.validate(None, strict = True) == None
    assert field.validate("a") == "a"
    assert field.validate("b") == "b"
    assert field.validate("c") == "c"
    assert field.validate("A") == "A"
    assert field.validate("B") == "B"
    assert field.validate("C") == "C"


# Generated at 2022-06-14 14:30:16.774313
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    default_returned = Field(default = "Hello World!").get_default_value()
    assert default_returned == "Hello World!"
    assert callable(Field(default = lambda: "Function returned succesfully").get_default_value())


# Generated at 2022-06-14 14:30:28.796370
# Unit test for method validate of class Object
def test_Object_validate():
    schema = Object(
        properties = {
            'name': Text(max_length = 10),
            'year': Integer(minimum = 2000, maximum = 2020),
            'active': Boolean(),
        },
        required = ['name', 'year', 'active'],
        additional_properties = False,
    )

    # test success
    data = {
        'name': 'test',
        'year': 2002,
        'active': True,
    }
    result, error = schema.validate_or_error(data)
    assert result == {'name': 'test', 'year': 2002, 'active': True}
    assert error is None

    # test failure
    data = {
        'name': 'test',
        'year': 2002,
        'active': True,
        'extra': True,
    }
    result,

# Generated at 2022-06-14 14:30:38.895074
# Unit test for method __or__ of class Field
def test_Field___or__():
    from typesystem.types import String, Number
    # Test for a Union type with only 1 field
    field1 = Field()
    field2 = Field()
    field3 = Field()
    union1 = (field1 | field2)
    assert isinstance(union1, Union)
    assert union1.any_of == [field1, field2]
    # Test for a Union type with more than 1 field
    union2 = (field1 | union1 | field3)
    assert isinstance(union2, Union)
    assert union2.any_of == [field1, field2, field3]
    # Test if the __or__ method works on different types of fields
    assert isinstance(String() | Number(), Union)



# Generated at 2022-06-14 14:30:43.232482
# Unit test for method __or__ of class Field
def test_Field___or__():
    import typesystem

    # method 1
    unions = typesystem.String() | typesystem.Integer()
    assert isinstance(unions, typesystem.Union)

    # method 2
    unions = typesystem.Union(any_of=[typesystem.String()]) | typesystem.Integer()
    assert isinstance(unions, typesystem.Union)



# Generated at 2022-06-14 14:30:45.848960
# Unit test for constructor of class Const
def test_Const():
    c = Const("foo")
    c.validate("foo")
    with pytest.raises(ValidationError):
        c.validate("bar")



# Generated at 2022-06-14 14:30:54.273253
# Unit test for method validate of class Choice
def test_Choice_validate():
    t1 = [
        ("a", "a"),
        ("b", "b"),
        ("c", "c"),
        ("d", "d"),
        ("e", "e"),
        ("f", "f"),
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
    ]
    choices = Choice(choices = t1)

# Generated at 2022-06-14 14:30:55.157245
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    Field()
    # raise Exception

# Generated at 2022-06-14 14:31:06.673149
# Unit test for method validate of class Array
def test_Array_validate():
    # If the below values are changed, all the test cases will fail
    items = [String(), String()]
    additional_items = False
    min_items = 2
    max_items = 2
    unique_items = False
    # If the above values are changed, all the test cases will fail
    array = Array(items=items, additional_items=additional_items, min_items=min_items, max_items=max_items, unique_items=unique_items)
    # test case: validate: value not list
    try:
        array.validate({})
    except ValidationError as error:
        assert error.messages[0].text == "Must be an array."
    # test case: validate: value is None
    try:
        array.validate(None)
    except ValidationError as error:
        assert error

# Generated at 2022-06-14 14:31:11.173416
# Unit test for method validate of class Choice
def test_Choice_validate():
    c = Choice(choices=[(0, "Male"), (1, "Female")])
    x = c.validate(0)
    x = c.validate(1)
    assert x is None
    assert c.validate("") != None
    assert c.validate(2) != None


# Generated at 2022-06-14 14:31:19.100473
# Unit test for method validate of class String

# Generated at 2022-06-14 14:31:41.047452
# Unit test for method validate of class Array
def test_Array_validate():

    # Test validity of array of validators on
    # exact number of items
    number_exact = Array(exact_items=2)
    num_lst = [2, 3]
    assert number_exact.validate(num_lst) == num_lst
    # Test validity of array of validators on
    # any number of items
    number_addit = Array()
    assert number_addit.validate(num_lst) == num_lst
    # Test validity of array of validators on
    # min and max number of items
    num_min = Array(min_items=1)
    num_max = Array(max_items=2)
    assert num_min.validate(num_lst) == num_lst
    assert num_max.validate(num_lst) == num

# Generated at 2022-06-14 14:31:53.032603
# Unit test for method validate of class Array
def test_Array_validate():

    # Create an instance of class Array
    array_field = Array()

    # Validate a array value
    valid_value = [1, 2, 3]
    invalid_value = 1
    try:
        array_field.validate(invalid_value)
    except ValidationError as e:
        assert(e.messages[0].text == "Must be an array.")

    # Validate a array value with a property key
    try:
        array_field.validate(invalid_value, strict=True)
    except ValidationError as e:
        assert(e.messages[0].text == "Must be an array.")
    
    # Validate a array value
    try:
        array_field.validate(valid_value, strict=True)
    except ValidationError as e:
        assert(False)


# Generated at 2022-06-14 14:31:56.836727
# Unit test for method serialize of class Array
def test_Array_serialize():
    schema = Array(items=String(min_length=5))
    assert schema.serialize(["abc", "abcde"]) == ["abc", "abcde"]
    assert schema.serialize(["abc", "abcde", "abcd"]) == ["abc", "abcde"]


# Generated at 2022-06-14 14:32:08.793504
# Unit test for method validate of class Union
def test_Union_validate():
    # Create a list of subclasses to be tested (Field)
    any_of_List = [
        Integer(minimum=10, maximum=20, required=True, allow_null=False),
        Integer(minimum=30, maximum=40, required=True, allow_null=False)
    ]

    # Test is_required
    assert Union(any_of=any_of_List, allow_null=False, required=True).is_required() == True

    # Test validate with matching data type
    union_One = Union(any_of=any_of_List, allow_null=False, required=True)
    assert union_One.validate(15) == 15
    assert union_One.validate(35) == 35

    # Test validate with non-matching data type

# Generated at 2022-06-14 14:32:15.019036
# Unit test for method validate of class Choice
def test_Choice_validate():
    # test case 1
    class TestChoice(Choice):
        def __init__(
            self,
            *,
            choices: typing.Sequence[typing.Union[str, typing.Tuple[str, str]]] = None,
            **kwargs: typing.Any,
        ) -> None:
            super().__init__(**kwargs)
            self.choices = [
                (choice if isinstance(choice, (tuple, list)) else (choice, choice))
                for choice in choices or []
            ]
            assert all(len(choice) == 2 for choice in self.choices)
    test_choices = TestChoice(choices = [("A", "a")])
    assert test_choices.validate("A") == "A"
    #test case 2

# Generated at 2022-06-14 14:32:24.599306
# Unit test for method validate of class Array
def test_Array_validate():
    # Test: method validate
    field = Array()
    value = []
    assert field.validate(value) == []

    field = Array(allow_null=False)
    with pytest.raises(ValidationError):
        field.validate(None)

    field = Array(null=False)
    with pytest.raises(ValidationError):
        field.validate(None)

    field = Array(allow_null=False, min_items=1)
    with pytest.raises(ValidationError):
        field.validate(None)

    field = Array(allow_null=True, min_items=1)
    with pytest.raises(ValidationError):
        field.validate([])

    field = Array(allow_null=False, exact_items=3)

# Generated at 2022-06-14 14:32:36.135162
# Unit test for method validate of class Boolean
def test_Boolean_validate():
    booleanTranslation = {
        True: "true",
        False: "false",
        "true": True,
        "false": False,
        "1": True,
        "0": False,
    }

    boolean = Boolean()
    assert booleanTranslation[boolean.validate(True, strict=False)] == "true"
    assert booleanTranslation[boolean.validate(False, strict=False)] == "false"
    assert booleanTranslation[boolean.validate("1", strict=False)] == "true"
    assert booleanTranslation[boolean.validate("0", strict=False)] == "false"
    assert booleanTranslation[boolean.validate("true", strict=False)] == "true"
    assert booleanTranslation[boolean.validate("false", strict=False)] == "false"

# Generated at 2022-06-14 14:32:37.872011
# Unit test for method validate of class Boolean
def test_Boolean_validate():
    value = ""
    strict = False
    field = Boolean()

    assert field.validate(value, strict=strict) == False


# Generated at 2022-06-14 14:32:49.027624
# Unit test for method validate of class String
def test_String_validate():
    string_field = String()
    assert isinstance(string_field.validate("hello"), str)
    assert string_field.validate("hello") == "hello"

    assert isinstance(string_field.validate("你好"), str)
    assert string_field.validate("你好") == "你好"

    assert string_field.validate("") == ""

    string_field.allow_blank = True
    assert string_field.validate("") == ""

    string_field.allow_null = True
    assert string_field.validate(None) == None

    string_field.allow_blank = False
    string_field.allow_null = True
    assert string_field.validate(None) == None

    string_field.allow_blank = True
    assert string_field.valid

# Generated at 2022-06-14 14:32:56.987878
# Unit test for method validate of class Choice
def test_Choice_validate():
    assert Choice(choices=[(1,1), (2,2), (3,3)]).validate(1) == 1
    assert Choice(choices=[(1,1), (2,2), (3,4)]).validate(3) == 3
    assert Choice(choices=[(1,1), (2,2), (3,3)]).validate(5) == 5
    assert Choice(choices=[(1,1), (2,2), (3,3)]).validate("") == ""
    assert Choice(choices=[(1,1), (2,2), (3,3)]).validate(None) == None
    assert Choice(choices=[(1,1), (2,2), (3,4)]).validate(None) == None

# Generated at 2022-06-14 14:33:14.288857
# Unit test for method validate of class Choice
def test_Choice_validate():
    obj = Choice(allow_null=True, choices=[("a", "b")])
    assert obj.validate("a") == "a"
    with pytest.raises(ValidationError) as exc_info:
        obj.validate("c")
    assert exc_info.value.text == "Not a valid choice."

