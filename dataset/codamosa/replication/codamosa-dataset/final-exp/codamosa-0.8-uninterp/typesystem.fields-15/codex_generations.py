

# Generated at 2022-06-14 14:25:05.664679
# Unit test for method validate of class Union
def test_Union_validate():
    class MyUnion(Union):
        def __init__(self):
            super().__init__(any_of=[Text(), Integer()])
    valid = MyUnion()
    try:
        assert valid.validate("hello") == "hello"
    except:
        print("test_Union_validate: valid.validate('hello') == 'hello' failed")

    try:
        assert valid.validate(25) == 25
    except:
        print("test_Union_validate: valid.validate(25) == 25 failed")

    try:
        valid.validate(None)
    except:
        pass
    else:
        print("test_Union_validate: valid.validate(None) should have raised an exception")

    try:
        valid.validate(True)
    except:
        pass

# Generated at 2022-06-14 14:25:13.890464
# Unit test for method validate of class Union
def test_Union_validate():
    class Foo(Field):
        pass
    class Bar(Field):
        pass
    class Baz(Field):
        pass
    u = Union(
        any_of=[Foo(name='f1'), Bar(name='b1'), Baz(name='b2')]
    )
    f = Foo(
        name = 'f2'
    )
    b = Bar(
        name = 'b3'
    )
    b2 = Baz(
        name = 'b4'
    )
    u.validate(f)
    u.validate(b)
    u.validate(b2)


# Generated at 2022-06-14 14:25:14.471556
# Unit test for method __or__ of class Field
def test_Field___or__():
    pass



# Generated at 2022-06-14 14:25:17.430228
# Unit test for method validate of class Array
def test_Array_validate():
    f = "type"
    class t(Array):
        @property
        def _validate_code(self):
            return f
    a = t()
    try:
        a.validate(1)
    except Exception as e:
        b = e
        assert b.messages[0].text == a.get_error_text(f)


# Generated at 2022-06-14 14:25:21.571328
# Unit test for method validate of class Union
def test_Union_validate():
    class OtherField(Field):
        errors = {'null': 'May not be null.'}

    class TestField(Field):
        errors = {'null': 'May not be null.', 'type': "Must be type 'bool'."}

    class TestNone(Field):
        allow_null = None
        errors = {'null': 'May not be null.', 'type': "Must be type 'bool'."}

    class TestFalse(Field):
        allow_null = False
        errors = {'null': 'May not be null.', 'type': "Must be type 'bool'."}

    class TestTrue(Field):
        allow_null = True
        errors = {'null': 'May not be null.', 'type': "Must be type 'bool'."}

    test = TestField()
    none = TestNone()
    false = TestFalse

# Generated at 2022-06-14 14:25:23.321559
# Unit test for method serialize of class String
def test_String_serialize():
    str1 = String()
    assert str1.serialize(45) == 45

# Generated at 2022-06-14 14:25:25.801728
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    f1 = Field(default=lambda: 10)
    f2 = Field(default=10)
    assert f1.get_default_value() == 10
    assert f2.get_default_value() == 10



# Generated at 2022-06-14 14:25:27.818192
# Unit test for method serialize of class String
def test_String_serialize():
    a = String()
    assert a.serialize("00:00:01") == "00:00:01"


# Generated at 2022-06-14 14:25:34.068063
# Unit test for method serialize of class Array
def test_Array_serialize():

    class MyArray(Array):        
        def __init__(self, *, items: Field = None, **kwargs: typing.Any) -> None:
            super().__init__(items=items, **kwargs)
    # Unit test mock item field
    class MockField():
        pass


    obj = MockField()
    serializer = MyArray(items=Simple(allow_null=True, default=None))
    assert serializer.serialize(obj) == obj


# Generated at 2022-06-14 14:25:39.227943
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    assert (Field(default=5).get_default_value() == 5)
    assert (Field(default=None).get_default_value() is None)
    assert (Field(default=None, allow_null=True).get_default_value() is None)
    assert (Field().get_default_value() is None)
    #
    # closure
    def gen_value():
        return 10
    assert (Field(default=gen_value).get_default_value() == 10)


# Generated at 2022-06-14 14:26:00.983882
# Unit test for method validate of class Choice
def test_Choice_validate():
    f = Choice(choices=['1','2','3'])

    test_dict = {
        'input': ['1', '2', '3', '4'],
        'output': [True, True, True, False]
      }

    for i in range(len(test_dict['input'])):
        assert(f.validate(test_dict['input'][i]) == True) == test_dict['output'][i]
# Test for method validate_or_error of class Choice

# Generated at 2022-06-14 14:26:04.878431
# Unit test for method validate of class Union
def test_Union_validate():
    validator = Union(any_of = [String(), Number()])
    assert validator.validate('Hello World!') == 'Hello World!'
    assert validator.validate(2.718) == 2.718
    with pytest.raises(ValidationError) as excinfo:
        validator.validate(True)
    assert excinfo.value.code == 'union'

# Generated at 2022-06-14 14:26:14.004911
# Unit test for method serialize of class Array
def test_Array_serialize():
    items = [Integer(),Integer()]
    additional_items = Integer()
    unique_items = True
    min_items = 2
    max_items = 3
    arr = Array(items = items, additional_items = additional_items, unique_items = unique_items, min_items = min_items, max_items = max_items)
    value = [1,2,3,4]
    result = [1,2,3,4]
    assert arr.serialize(value) == result

# Generated at 2022-06-14 14:26:20.966988
# Unit test for method validate of class Array

# Generated at 2022-06-14 14:26:29.791843
# Unit test for method validate of class Choice
def test_Choice_validate():
    my_choice = Choice(choices=[
        ("foo", "bar"),
        ("baz", "boo"),
    ], required=True)
    assert my_choice.validate("foo") is True
    assert my_choice.validate("baz") is True
    assert my_choice.validate("ban") is False
    assert my_choice.validate("") is False
    assert my_choice.validate(None) is False
    assert my_choice.validate("") is False
    my_choice = Choice(choices=[
        ("foo", "bar"),
        ("baz", "boo"),
    ], required=True, allow_null=True)
    assert my_choice.validate(None) is True
    assert my_choice.validate("") is True


# Generated at 2022-06-14 14:26:33.263444
# Unit test for method validate of class Union
def test_Union_validate():
    f = Union([Integer(minimum=10, maximum=20), Integer(minimum=30, maximum=40)])
    assert f.validate(25) == 25
    assert f.validate(35) == 35
    try:
        f.validate(7)
        raise Exception("Int should fail with value 7")
    except ValidationError:
        pass
    try:
        f.validate(43)
        raise Exception("Int should fail with value 43")
    except ValidationError:
        pass
    

test_Union_validate()



# Generated at 2022-06-14 14:26:36.830997
# Unit test for method validate of class Number
def test_Number_validate():
    test_field = Number(minimum=0, maximum=10, precision=".1")
    try:
        assert test_field.validate(11) == ValidationResult(value=None, error="Must be less than or equal to 10.")
    except AssertionError:
        assert test_field.validate(11) == ValidationResult(value=None, error="Must be less than or equal to 10. (Got 11)")


# Generated at 2022-06-14 14:26:46.159235
# Unit test for method validate of class Choice
def test_Choice_validate():
    data = [
        {"in": 1, "out": {"value": 1, "error": None}},
        {"in": None, "out": {"value": None, "error": None}},
        {"in": "", "out": {"value": None, "error": None}},
        {"in": "2", "out": {"value": None, "error": "Not a valid choice."}},
    ]
    for case in data:
        field = Choice()
        result = field.validate_or_error(case["in"])
        assert result.value == case["out"]["value"]
        assert result.error == case["out"]["error"]



# Generated at 2022-06-14 14:26:50.237465
# Unit test for constructor of class Choice
def test_Choice():
    choices = [
        ("choice1", "choice1"),
        ("choice2", "choice2"),
    ]
    field = Choice(choices=choices)
    if field.choices != choices:
        raise Exception("constructor of class Choice is failed")


# Generated at 2022-06-14 14:27:01.422200
# Unit test for method validate of class Union
def test_Union_validate():
    def assert_validation(data, field):
        validator = Field()
        try:
            value, errors = field.validate_or_error(data)
        except ValidationError as e:
            errors = e.messages()
        validator.validate(errors)
    def assert_valid_data(data, field):
        try:
            value, errors = field.validate_or_error(data)
        except ValidationError as e:
            errors = e.messages()
        if errors:
            raise AssertionError(f"{data} should be valid for {field}")
        return value

# Generated at 2022-06-14 14:27:49.369814
# Unit test for method validate of class Union
def test_Union_validate():
    any_of = [Boolean(name="foobar"), Number(name="barfoo")]
    obj = Union(any_of=any_of, allow_null=True, default=False)
    assert obj.validate(True) == True
    assert obj.validate(False) == False
    assert obj.validate(None) == None

    obj = Union(any_of=any_of, allow_null=False, default=False)
    assert obj.validate(True) == True
    assert obj.validate(False) == False
    try:
        obj.validate(None)
        assert False
    except:
        assert True

    try:
        obj.validate("foo")
        assert False
    except Exception as e:
        assert "union" in str(e)


# Generated at 2022-06-14 14:27:53.713165
# Unit test for method serialize of class String
def test_String_serialize():
    myfield = String(format="time")
    assert myfield.serialize("12:34:56") == "12:34:56"
    assert myfield.serialize(None) == None
# End of unit test



# Generated at 2022-06-14 14:27:58.005710
# Unit test for method validate of class Union
def test_Union_validate():
    data = 2
    u = Union([Int(), String()])
    _, error = u.validate_or_error(data)
    print(error)

    assert(error.messages()[0].code == "union")

test_Union_validate()


# Generated at 2022-06-14 14:28:02.430531
# Unit test for method validate of class String
def test_String_validate():
    string=String()
    a=string.validate('sadfas')
    assert a=='sadfas'
    try:
        string.validate(1)
        raise Exception("error should be made! but not")
    except ValidationError:
        assert True
    test_String_validate()


# Generated at 2022-06-14 14:28:07.137391
# Unit test for method validate of class Boolean
def test_Boolean_validate():
    f = Boolean()
    assert f.validate(False) == False
    assert f.validate(True) == True
    try:
        assert f.validate(3) == False
    except ValidationError:
        return True
    assert False



# Generated at 2022-06-14 14:28:12.111910
# Unit test for method __or__ of class Field
def test_Field___or__():
    class StringField(Field):
        pass
    sf1 = StringField()
    class IntField(Field):
        pass
    if1 = IntField()
    sf1 or if1
    class Union(Field):
        pass
    u1 = Union()
    sf2 = StringField()
    u1 | sf2
    u1 | if1



# Generated at 2022-06-14 14:28:13.772164
# Unit test for method __or__ of class Field
def test_Field___or__():
    #assert (1 or 2) == 1
    assert (False or True) == True

# Generated at 2022-06-14 14:28:26.445834
# Unit test for method validate of class Choice
def test_Choice_validate():
    # If a choice is valid, it should return the value.
    field = Choice(choices=[("a", "A"), ("b", "B")], allow_null=True)
    assert field.validate("a") == "a"
    assert field.validate("b") == "b"

    # If a choice is null and allow_null, it should return None.
    assert field.validate("") == None
    assert field.validate(None) == None

    # If a choice is blank and not allow_null, it should raise ValidationError("required").
    with pytest.raises(ValidationError) as exc:
        field.validate("", strict=True)
    assert exc.value.code == "required"

    # If a choice is not valid, it should raise ValidationError("choice").

# Generated at 2022-06-14 14:28:37.757470
# Unit test for method __or__ of class Field
def test_Field___or__():
    class Field1(Field):
        pass
    class Field2(Field):
        pass
    class Field3(Field):
        pass

    field1 = Field1()
    field2 = Field2()
    field3 = Field3()
    field12 = field1 | field2
    field13 = field1 | field3

    assert isinstance(field12, Union)
    assert isinstance(field13, Union)

    assert len(field12.any_of) == 2
    assert len(field13.any_of) == 2

    assert field1 in field12.any_of
    assert field2 in field12.any_of

    assert field1 in field13.any_of
    assert field3 in field13.any_of



# Generated at 2022-06-14 14:28:45.676632
# Unit test for method validate of class Choice
def test_Choice_validate():
    import unittest
    from jsonobject import Choice
    from jsonobject.exceptions import ValidationError
    class Test(Choice):
        choices = [("Item1", "Item1"),("Item2", "Item2")]
    class TestCase(unittest.TestCase):

        def test_choice_validate(self):
            test = Test()
            test.validate("Item1")
            with self.assertRaises(ValidationError):
                test.validate("item1")
    unittest.main()


# Generated at 2022-06-14 14:29:00.847868
# Unit test for method validate of class Object
def test_Object_validate():
    assert Object(properties={'abc': String()}, additional_properties=False)\
        .validate({'abc': 'test'}) == {'abc': 'test'}



# Generated at 2022-06-14 14:29:11.430693
# Unit test for method validate of class String
def test_String_validate():
    # Case 1: generic string is valid
    value1 = "any string you want"
    field = String()
    assert field.validate(value1) == value1
    # Case 2: null string is invalid
    field = String()
    assert field.validate_or_error(None).error.code == "null"
    # Case 3: when trim_whitespace is true whitespaces are removed
    field = String(trim_whitespace=True)
    value2 = "    any string you want    "
    assert field.validate(value2) == value1
    # Case 4: when max_length of string is set to a number and
    # value is longer, then string is invalid
    field = String(max_length=5)
    value3 = "123456789"
    assert field.validate_or_

# Generated at 2022-06-14 14:29:15.613927
# Unit test for method validate of class Union
def test_Union_validate():
    def test(field, value, expected):
        actual = field.validate(value)
        assert actual == expected
        print(f"PASS: field={field}, value={value}")

    # test(..., ..., ...)
    # TODO: Write a test for this method.



# Generated at 2022-06-14 14:29:17.100618
# Unit test for constructor of class Const
def test_Const():
    f = Const(const = 5)
    assert f.config['allow_null'] == False
    assert f.const == 5


# Generated at 2022-06-14 14:29:20.034384
# Unit test for constructor of class Const
def test_Const():
    obj = Const('one',const='one')
    obj.validate('one')
    try:
        obj.validate('not one')
    except ValidationError as err:
        print(err)

# Generated at 2022-06-14 14:29:25.593536
# Unit test for method validate of class Object
def test_Object_validate():
    '''
    Function to test the validate method of class Object
    '''
    data = {
      "properties": {
        "prop1": String(max_length=20),
        "prop2": Integer()
      }
    }
    obj = Object(**data)
    value = {"prop1":"testing", "prop2":12}
    assert obj.validate(value) == value


# Generated at 2022-06-14 14:29:32.243813
# Unit test for method validate of class String
def test_String_validate():
    string = String(title='String', description='String Test')
    valid_str_list = ["valid_str", "valid_str1", "valid_str2"]
    invalid_str_list = [None, 1, 0]
    for str in valid_str_list:
        try:
            string.validate(str, strict=True)
        except ValidationError:
            assert False
            return
    for str in invalid_str_list:
        try:
            string.validate(str, strict=True)
            assert False
        except ValidationError:
            assert True
    return



# Generated at 2022-06-14 14:29:39.136605
# Unit test for method __or__ of class Field
def test_Field___or__():
    field_1 = Field(title='field_1')
    field_2 = Field(title='field_2')
    field_3 = Field(title='field_3')
    union = field_1 | field_2 | field_3
    assert isinstance(union, Union)
    assert isinstance(union.any_of[0], Field)
    assert isinstance(union.any_of[1], Field)
    assert isinstance(union.any_of[2], Field)



# Generated at 2022-06-14 14:29:42.057952
# Unit test for method validate of class Number
def test_Number_validate():
    assert 1 == Number(minimum=1).validate(1)
    assert 1 == Number(maximum=1).validate(1)
    assert 1 == Number(minimum=1).validate(1)
    assert 1 == Number().validate(1)



# Generated at 2022-06-14 14:29:47.040673
# Unit test for method validate of class Choice
def test_Choice_validate():
    c = Choice(choices = [("foo","foo"),("bar","bar")],allow_null=True)
    assert c.validate("false") == c.validate("foo") == c.validate("bar") == c.validate("foo") == c.validate("bar") 
    assert c.validate("") == c.validate(None) # For class Choice, '' and None are equivalent
    assert c.validate("baz") == "baz" # value not in choices


# Generated at 2022-06-14 14:30:16.863502
# Unit test for method validate of class Choice
def test_Choice_validate():
    class CustomChoice(Choice):
        errors = {
            "null": "May not be null.",
            "required": "This field is required.",
            "choice": "Not a valid choice.",
        }

        def __init__(
            self, 
            *, 
            choices: typing.Sequence[typing.Union[str, typing.Tuple[str, str]]] = None, 
            **kwargs: typing.Any
        ):
            super().__init__(**kwargs)
            self.choices = [
                (choice if isinstance(choice, (tuple, list)) else (choice, choice)) for choice in choices or []
            ]
            assert all(len(choice) == 2 for choice in self.choices)


# Generated at 2022-06-14 14:30:24.971460
# Unit test for method validate of class Choice
def test_Choice_validate():
  choice1 = Choice(name = 'Choice1' ,choices = [('0','zero'),('1','one'),('2','two')],allow_null = False)

  result = choice1.validate('0', strict = False)
  assert result == '0'

  with pytest.raises(ValidationError):
    choice1.validate('3', strict = True)
  
  with pytest.raises(ValidationError):
    choice1.validate('', strict = True)

  choice2 = Choice(name = 'Choice2', choices = [('0','zero'),('1','one'),('2','two')],allow_null = False,allow_blank = True)

  result = choice2.validate('', strict = False)
  assert result == None


# Generated at 2022-06-14 14:30:28.641142
# Unit test for method validate of class Choice
def test_Choice_validate():
    newChoice = Choice(choices = [('hello', 'hello'), ('hello2', 'hello2')])
    newChoice.validate('hello')
    newChoice.validate(None)
    newChoice.validate('')
    try:
         newChoice.validate('hello3')
         assert False
    except ValidationError:
        assert True



# Generated at 2022-06-14 14:30:36.442809
# Unit test for method validate of class Choice
def test_Choice_validate():
    choice = Choice(choices=[])
    assert choice.validate(value=None, strict=False) is None
    assert choice.validate(value='', strict=False) == ''
    try:
        choice.validate(value=None, strict=True)
    except ValidationError:
        assert True
    else:
        assert False
    try:
        choice.validate(value='', strict=True)
    except ValidationError:
        assert True
    else:
        assert False



# Generated at 2022-06-14 14:30:46.248898
# Unit test for method validate of class Union
def test_Union_validate():
    assert Union(
                any_of=[Integer(default=0, allow_null=True),
                Integer(default=0, allow_null=True),
                Integer(default=0, allow_null=True)]
            ).validate(None) == None
    assert Union(
                any_of=[String(default="null", allow_null=True),
                String(default="null", allow_null=True),
                String(default="null", allow_null=True)]
            ).validate(None) == None
    assert Union(
                any_of=[Integer(default=0, allow_null=True),
                Integer(default=0, allow_null=True),
                String(default="null", allow_null=True)]
            ).validate(None) == None
    
    

# Generated at 2022-06-14 14:30:47.545142
# Unit test for method __or__ of class Field
def test_Field___or__():
    assert String() | String() == String() | String()

# Generated at 2022-06-14 14:30:55.289287
# Unit test for method validate of class Union
def test_Union_validate():
    test_obj = Union(any_of = [AnyType()])
    value = "test"
    try:
        test_obj.validate(value)
    except Exception as e:
        trace_back = sys.exc_info()
        error = trace_back[1].__str__()
        assert error == "May not be null."
    else:
        assert False
    value = 1
    try:
        test_obj.validate(value)
    except Exception as e:
        trace_back = sys.exc_info()
        error = trace_back[1].__str__()
        assert error == "May not be null."
    else:
        assert False
    value = None
    try:
        test_obj.validate(value)
    except Exception as e:
        trace_back = sys.exc_

# Generated at 2022-06-14 14:31:03.407811
# Unit test for method __or__ of class Field
def test_Field___or__():
    import typesystem
    d = {'any_of': []}
    assert d.update({'any_of': []}) == None
    N = type('N', (object,), {'any_of': []})
    class NN(object):
        any_of = []
    assert isinstance(typesystem.field.Union(**d), (N, NN)) == True
    assert typesystem.field.Union(**d) != typesystem.field.Union(**d)


# Generated at 2022-06-14 14:31:09.370699
# Unit test for method validate of class Choice
def test_Choice_validate():
    print("Testing method validate of class Choice")
    choice = Choice(choices=[("A", "Apple",), ("B", "Banana",)])
    assert choice.validate("A") == "A"
    assert choice.validate("B") == "B"
    try:
        choice.validate("")
    except ValueError as value_error:
        assert value_error.args[0] == "Must not be blank."
    except:
        assert False


# Generated at 2022-06-14 14:31:16.542279
# Unit test for constructor of class Array
def test_Array():
    my_array = Array(
        required = True,
        description = "This is an array.",
        max_items = 5,
        min_items = 1,
        items = [
            String(),
            String(max_length = 10),
            String(min_length = 5)
        ],
        additional_items = String()
    )
    assert my_array.required is True
    assert my_array.description == "This is an array."
    assert my_array.max_items == 5
    assert my_array.min_items == 1
    assert len(my_array.items) == 3


# Generated at 2022-06-14 14:31:31.542903
# Unit test for method validate of class Array
def test_Array_validate():
    schema = Array(items=String())

    # Check that the length of the array is valid
    # Arrange
    value = []
    # Act
    result, error = schema.validate_or_error(value)
    # Assert
    assert error == ValidationError(
        messages=[
            Message(
                code="empty",
                message="Must not be empty.",
                index=None,
            )
        ]
    )

    # Check that the length of the array is valid
    # Arrange
    value = ["", ""]
    # Act
    result, error = schema.validate_or_error(value)
    # Assert

# Generated at 2022-06-14 14:31:41.560450
# Unit test for method validate of class Array
def test_Array_validate():
    def instance_of(cls):
        return cls()
    with pytest.raises(AssertionError):
        Array(min_items='a')
    with pytest.raises(AssertionError):
        Array(max_items='a')
    with pytest.raises(AssertionError):
        Array(exact_items='a')
    with pytest.raises(AssertionError):
        Array(items='a')
    with pytest.raises(AssertionError):
        Array(items=[1])
    with pytest.raises(AssertionError):
        Array(additional_items='a')
    with pytest.raises(AssertionError):
        Array(unique_items='a')

# Generated at 2022-06-14 14:31:50.352248
# Unit test for method validate of class String
def test_String_validate():
    str1 = String(
        title="str1",
        description="str1",
        default="str1",
        allow_blank=True,
        trim_whitespace=True,
        max_length=None,
        min_length=None,
        pattern=None,
        format=None,
        allow_null=False
    )
    assert str1.validate("str1") == "str1"
    assert str1.validate(None) == None
    assert str1.validate("") == ""


# Generated at 2022-06-14 14:31:55.931663
# Unit test for method validate of class Choice
def test_Choice_validate():
    field = Choice(choices=[("a", "b"), ("c", "d")])
    # Test first choice
    assert field.validate("a") == "a"
    # Test second choice
    assert field.validate("c") == "c"
    # Test not a valid choice
    try:
        field.validate("e")
    except ValidationError:
        pass
    # Test null
    assert field.validate(None) == None
    # Test allow null true
    field = Choice(choices=[("a", "b"), ("c", "d")], allow_null=True)
    assert field.validate(None) == None
    # Test allow null false
    field = Choice(choices=[("a", "b"), ("c", "d")], allow_null=False)

# Generated at 2022-06-14 14:31:59.665918
# Unit test for method __or__ of class Field
def test_Field___or__():
    from unittest import TestCase
    from typesystem.field import String, Integer

    class A(TestCase):
        def test_String_is_combined_with_Integer(self):
            items_field = String() | String()
            Integer() | String() | items_field

            A.assertIsInstance(items_field, Union)
    A()



# Generated at 2022-06-14 14:32:10.136912
# Unit test for method validate of class Choice
def test_Choice_validate():
    choice = Choice(choices = [("choice1", "choice1"), ("choice2", "choice2")])
    
    # Correctly identify choice
    assert(choice.validate("choice1") == "choice1")
    assert(choice.validate("choice2") == "choice2")

    # Currectly identify null as a choice if null is allowed
    choice = Choice(choices = [("choice1", "choice1"), ("choice2", "choice2")], allow_null = True)
    assert(choice.validate(None) == None)

    # Raise an exception if choice is missing and null is not allowed
    choice = Choice(choices = [("choice1", "choice1"), ("choice2", "choice2")])
    with pytest.raises(ValidationError):
        choice.validate(None)

    # Recogn

# Generated at 2022-06-14 14:32:19.385100
# Unit test for method validate of class String
def test_String_validate():
    string_field = String(title = '', description = '', default = NO_DEFAULT, allow_null = False, allow_blank = False, trim_whitespace = True, max_length = None, min_length = None, pattern = re.compile('^[0-9]+$'), format = None)
    # Case 1
    assert string_field.validate_or_error(2, strict=False).error.text == 'Must be a string.'
    # Case 2
    assert string_field.validate_or_error("1234", strict=False).value == '1234'


# Generated at 2022-06-14 14:32:30.417089
# Unit test for method validate of class String

# Generated at 2022-06-14 14:32:32.205399
# Unit test for method validate of class Choice
def test_Choice_validate():
    obj = Choice()
    result = obj.validate("")
    assert result == None


# Generated at 2022-06-14 14:32:33.663804
# Unit test for method validate of class Object
def test_Object_validate():
    field=Object()
    value=[]
    field.validate(value)


# Generated at 2022-06-14 14:32:56.119200
# Unit test for method validate of class Number
def test_Number_validate():
    test_number = Number()
    test_number.validate("123")
    test_number.validate(123)
    test_number.validate("123.123")
    test_number.validate(123.123)
    value = test_number.validate("a")
    print(value)
    # inf = float("inf")
    # test_number.validate(inf)
    # nan = float("nan")
    # test_number.validate(nan)

test_Number_validate()


# Generated at 2022-06-14 14:32:58.738171
# Unit test for method validate of class Number
def test_Number_validate():
    obj = Number(minimum=0, maximum=10, multiple_of=2)
    obj.validate(12)


# Generated at 2022-06-14 14:33:01.303345
# Unit test for method validate of class String
def test_String_validate():
    f = String()
    res = f.validate('123')
    assert res == '123'


# Generated at 2022-06-14 14:33:07.586859
# Unit test for method validate of class Array
def test_Array_validate():
    obj = Array(
        items=None,
        additional_items=True,
        min_items=None,
        max_items=None,
        unique_items=False,
        allow_null=False,
        required=False)
    assert obj.validate([]) == []
    assert obj.validate([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]

    obj = Array(
        items=None,
        additional_items=False,
        min_items=None,
        max_items=None,
        unique_items=False,
        allow_null=False,
        required=False)
    assert obj.validate([]) == []

# Generated at 2022-06-14 14:33:08.745506
# Unit test for constructor of class Const
def test_Const():
    Const(const=None)


# Generated at 2022-06-14 14:33:11.389656
# Unit test for method validate of class Choice
def test_Choice_validate():
  a=Choice(choices=[ ('1', 'banana'), ('2', 'apple') ])
  print(a.validate(2))

# Generated at 2022-06-14 14:33:13.106317
# Unit test for method validate of class Choice
def test_Choice_validate():
    cl = Choice(choices=[("1", "one")])
    print(cl.validate("1"))
    #assert cl.validate("1") == "one"

test_Choice_validate()
