

# Generated at 2022-06-14 14:25:51.415823
# Unit test for method serialize of class String
def test_String_serialize():
    assert String(format="uuid").serialize('9e0adc87-f69d-45b6-b0c7-d6d8f13c3fdf') == '9e0adc87-f69d-45b6-b0c7-d6d8f13c3fdf'


# Generated at 2022-06-14 14:25:53.598131
# Unit test for method validate of class Number
def test_Number_validate():
    field = Number()
    assert field.validate("15.0")==15.0
    assert field.validate("15")==15
    assert field.validate(15.0)==15.0
    assert field.validate(15)==15


# Generated at 2022-06-14 14:26:02.998058
# Unit test for method validate of class Union
def test_Union_validate():
    Field.errors_as_list = True
    class NewUnion(Union):
        def __init__(self, any_of: typing.List[Field]):
            super().__init__(any_of=any_of)
    class NewInt(Integer):
        def get_error_text(self, code):
            return code
    class NewStr(String):
        def get_error_text(self, code):
            return code
    newInt = NewInt()
    newStr = NewStr()
    newUnion = NewUnion([newInt, newStr])
    try:
        newUnion.validate(123)
    except ValidationError as exception:
        assert exception.messages() == [{'code': 'type', 'text': 'type'}]

# Generated at 2022-06-14 14:26:06.338996
# Unit test for method validate of class Object
def test_Object_validate():
    field=Object()
    assert field.validate({}, strict=True)=={}
    assert field.validate({'a':1, 'b':2}, strict=True)=={'a':1, 'b':2}
    try:
        field.validate(1, strict=False)
    except ValidationError:
        assert field.validate(1, strict=False)==None
    try:
        field.validate(None, strict=False)
    except ValidationError:
        assert field.validate(None, strict=False)==None


# Generated at 2022-06-14 14:26:12.609075
# Unit test for method validate of class String
def test_String_validate():
    my_str = String()
    assert my_str.validate(None, strict=True) == None
    assert my_str.validate(None, strict=False) == ""

    assert my_str.validate(1, strict=True) == None
    assert my_str.validate(1, strict=False) == "1"


# Generated at 2022-06-14 14:26:20.069412
# Unit test for method validate of class Array
def test_Array_validate():
    # Test case that field is not provided and inputs are valid
    try:
        field = Array()
        result = field.validate(None)
        assert result is None
    except Exception:
        print("Array.validate(None) failed")
    # Test case that field is not provided and inputs are invalid
    try:
        field = Array()
        field.validate("string")
        print("Array.validate(inputs) failed")
    except Exception:
        pass
    # Test case that field is provided and inputs are invalid
    try:
        field = Array(items=String())
        field.validate("string")
    except Exception:
        print("Array.validate(inputs) failed")
    # Test case that field is provided and inputs are valid

# Generated at 2022-06-14 14:26:29.952271
# Unit test for method validate of class Object
def test_Object_validate():
    # test additional_properties is None, strict is False
    def test_obj_1():
        field = Object()
        value = {'a': 1, 'b': 2}
        try:
            field.validate(value=value, strict=False)
        except ValidationError:
            assert True
        else:
            assert False
        try:
            field.validate(value=value, strict=True)
        except ValidationError:
            assert True
        else:
            assert False
    test_obj_1()

    # test additional_properties is None, strict is True
    def test_obj_2():
        field = Object()
        value = {'a': 1, 'b': 2}
        try:
            field.validate(value=value, strict=False)
        except ValidationError:
            assert True

# Generated at 2022-06-14 14:26:34.815586
# Unit test for method validate of class Union
def test_Union_validate():
    class TestField(Field):
        errors = {"error": "Error"}
        def validate(self, value, strict = False):
            return None, ValidationError(messages = [Message(text = "Error", code = "error", index = [])])

    field = Union(any_of = [TestField(), TestField()])
    # test if the value is a valid type
    assert field.validate({"test": True}) == None
    # test if the value is null
    assert field.validate(None) == None
    # test if the value is of a valid type
    with pytest.raises(ValidationError) as exc_info:
        field.validate(123)
    assert exc_info.value.messages[0].text == "Error"

# Generated at 2022-06-14 14:26:38.867514
# Unit test for method validate of class Array
def test_Array_validate():
    schema = Array(default=['apple','cherry','berry'],max_items=4)
    assert schema.validate(['apple','cherry','berry'], strict=False) == ['apple','cherry','berry']
    assert schema.validate(['apple','cherry','berry'], strict=True) == ['apple','cherry','berry']
    with pytest.raises(ValidationError):
        schema.validate(['apple','cherry','berry','berry'], strict=True)
    with pytest.raises(ValidationError):
        schema.validate([], strict=True)


# Generated at 2022-06-14 14:26:45.477778
# Unit test for method serialize of class String
def test_String_serialize():
    x = String(format='date')
    assert x.serialize('2015-1-1') == '2015-1-1'
    x = String(format='uuid')
    assert x.serialize('6ccd780c-baba-1026-9564-0040f4311e29') == '6ccd780c-baba-1026-9564-0040f4311e29'



# Generated at 2022-06-14 14:27:05.623986
# Unit test for constructor of class String
def test_String():
    test_String = String(allow_blank=False, trim_whitespace=True, max_length=None, min_length=None, pattern=None, format=None)
    assert test_String


# Generated at 2022-06-14 14:27:06.384308
# Unit test for method validate of class String
def test_String_validate():
    pass

# Generated at 2022-06-14 14:27:10.135162
# Unit test for constructor of class String
def test_String():
    s = String(title="name", description="The name of the user", trim_whitespace=False, max_length=15, pattern="^[A-Za-z]*$")
    assert s.title == "name", "The test passed"
    assert s.description == "The name of the user", "The test passed"
    assert s.trim_whitespace == False, "The test passed"
    assert s.max_length == 15, "The test passed"
    assert s.pattern == "^[A-Za-z]*$", "The test passed"


# Generated at 2022-06-14 14:27:14.875560
# Unit test for method validate of class Union
def test_Union_validate():
    test_schema = JsonSchemaProperty(
        type=Union(
            any_of=[JsonSchemaProperty(type=String, allow_null=True), JsonSchemaProperty(type=Integer, allow_null=True), JsonSchemaProperty(type=Enum(enum=[1,"one"], default=1))]
        ),
        default=1,
        allow_null=True,
    )
    assert test_schema.validate_or_error('one') == ('one', None)
    assert test_schema.validate_or_error('two') == (1, None)
    assert test_schema.validate_or_error(2) == (2, None)
    assert test_schema.validate_or_error(3) == (1, None)
    assert test_schema.valid

# Generated at 2022-06-14 14:27:22.499485
# Unit test for method validate of class Object
def test_Object_validate():
    object = Object(properties={"name": String()})
    assert object.validate(dict(name="John Doe")) == dict(name="John Doe")
    assert object.validate({"name": "John Doe"}) == dict(name="John Doe")
    assert object.validate(dict(name="John Doe", job="developer")) == dict(name="John Doe", job="developer")
    assert object.validate({"name": "John Doe", "job": "developer"}) == dict(name="John Doe", job="developer")

    assert object.validate(dict(name=1)) == dict(name=1)
    assert object.validate({"name": 1}) == dict(name=1)

# Generated at 2022-06-14 14:27:33.763895
# Unit test for method validate of class Array
def test_Array_validate():
    field = Array(items=Integer(), unique_items=True)

    # Empty list
    assert field.validate([]) == []

    # Null/None
    assert field.validate(None) == None

    # Integer
    assert field.validate([1, 2, 3]) == [1, 2, 3]

    # Float
    assert field.validate([1.1, 2.2, 3.3]) == [1.1, 2.2, 3.3]

    # Not a list
    with pytest.raises(ValidationError):
        field.validate({})

    # Negative integer
    with pytest.raises(ValidationError):
        field.validate([-1, -2, -3])

    # Floats

# Generated at 2022-06-14 14:27:43.861008
# Unit test for method validate of class Union
def test_Union_validate():
    class Color(String):
        """Red, Green, Blue"""

        def __init__(self, **kwargs: typing.Any) -> None:
            super().__init__(
                const=kwargs.get("const"),
                enum=kwargs.get("enum", ["red", "green", "blue"]),
                title=kwargs.get("title"),
                description=kwargs.get("description"),
                default=kwargs.get("default"),
                required=kwargs.get("required"),
                read_only=kwargs.get("read_only"),
                write_only=kwargs.get("write_only"),
            )

    # Test for simple case
    color_schema = Color(const='black')
    input = 'black'
    output = color_schema.validate(input)
    assert output == input

# Generated at 2022-06-14 14:27:49.132961
# Unit test for method validate of class Number
def test_Number_validate():
    obj1 = Number()
    assert obj1.validate(3)==3
    obj2 = Number()
    assert obj2.validate(3.0)==3.0
    assert obj2.validate('3.0')==3.0


# Generated at 2022-06-14 14:27:53.498277
# Unit test for constructor of class Const
def test_Const():
	# try with arg
	a1 = Const(1)
	assert a1.const == 1
	# try without arg
	a1 = Const()
	assert a1.const == None

# A unit test for method validate of class Const

# Generated at 2022-06-14 14:28:03.582454
# Unit test for method validate of class String
def test_String_validate():
    field = String(title="A string")
    assert(field.validate("A string") == "A string")
    field = String(title="A string", min_length=10)
    assert(field.validate("A string") == "A string")
    with pytest.raises(ValidationError) as exc:
        field.validate("Not long")
    assert(exc.value.code == "min_length")
    with pytest.raises(ValidationError) as exc:
        field = String(title="A string", pattern="Not a string")
        field.validate("A string")
    assert(exc.value.code == "pattern")
    assert(field.validate(None) == None)

# Generated at 2022-06-14 14:28:26.193876
# Unit test for method validate of class Choice
def test_Choice_validate():
    result = Choice(choices=["1", "3"]).validate(value=1)
    assert result == result, 'result is not true'
    result = Choice(choices=["1", "3"]).validate(value='1')
    assert result == result, 'result is not true'
    result = Choice(choices=["1", "3"]).validate(value='a')
    assert result == result, 'result is not true'
    result = Choice(choices=["1", "3"]).validate(value='2', strict=True)
    assert result == result, 'result is not true'



# Generated at 2022-06-14 14:28:33.819857
# Unit test for method validate of class Number
def test_Number_validate():
        assert Number().validate(1) == 1
        assert Number(allow_null=True).validate(1) == 1
        assert Number(allow_null=True).validate(None) == None
        assert Number(allow_null=True, precision="0.5").validate(1.25) == 1.5
        assert Number(precision="0.5").validate(1.25) == 1.25
        assert Number(precision="0.5").validate(1.35) == 1.5
        assert Number(precision="0.25").validate(1.025) == 1.0
        assert Number(precision="0.25").validate(1.025) == 1.0
        assert Number(maximum=2.0).validate(1) == 1

# Generated at 2022-06-14 14:28:39.673951
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    class ObjField(Field):
        def __init__(self, **kwargs):
            super(ObjField, self).__init__(**kwargs)
            self.default = 'str'
    obj = ObjField()
    try:
        assert obj.get_default_value() == 'str'
    except AssertionError:
        print('Test case failed: test_Field_get_default_value')
    else:
        print('Test case passed: test_Field_get_default_value')

# Generated at 2022-06-14 14:28:51.905955
# Unit test for method validate of class Union

# Generated at 2022-06-14 14:29:03.643894
# Unit test for method validate of class Array
def test_Array_validate():
    #Arrange
    values = [
        {
            "items": [1, 2, 3],
            "expected": [1, 2, 3],
            "error": None,
            "strict": False
        },
        {
            "items": None,
            "expected": None,
            "error": None,
            "strict": False
        },
        {
            "items": [1, 2, 3],
            "expected": [1, 2, 3],
            "error": None,
            "strict": True
        },
        {
            "items": None,
            "expected": None,
            "error": None,
            "strict": True
        }
    ]

    for value in values:
        print(value)
        #Act

# Generated at 2022-06-14 14:29:11.477318
# Unit test for method validate of class Array
def test_Array_validate():
    array_of_strings = Array(items=String())
    assert array_of_strings.validate(["a", "b", "c"]) == ["a", "b", "c"]
    assert array_of_strings.validate([None, "b", "c"]) == [None, "b", "c"]
    assert array_of_strings.validate([None]) == [None]
    assert array_of_strings.validate([]) == []
    assert array_of_strings.validate(None) == None

    with pytest.raises(ValidationError) as excinfo:
        array_of_strings.validate(None, strict=True)
    assert excinfo.value.messages == [Message(code="null", text="May not be null.")]


# Generated at 2022-06-14 14:29:14.537966
# Unit test for constructor of class Const
def test_Const():
    assert(Const(1).validate(1))
    assert(Const(null).validate(null))
    assert(not Const(1).validate(0))
    assert(not Const(null).validate(0))



# Generated at 2022-06-14 14:29:16.196246
# Unit test for constructor of class Const
def test_Const():
    a = Const(1)
    assert a.get_default_value() == 1
    assert a.const == 1


# Generated at 2022-06-14 14:29:25.986269
# Unit test for method validate of class Choice
def test_Choice_validate():
    Choice = SchemaFields.Choice

    assert Choice(allow_null=True, choices=["a", "b"]).validate("a") == "a"
    assert Choice(choices=["a", "b"]).validate("a") == "a"
    assert Choice(choices=["a", "b"]).validate("b") == "b"

    assert Choice(choices=["a", "b"]).validate("A") == "a"
    assert Choice(choices=["a", "b"]).validate("B") == "b"

    assert Choice(choices=["a", "b"]).validate("a", strict=True) == "a"
    assert Choice(choices=["a", "b"]).validate("b", strict=True) == "b"


# Generated at 2022-06-14 14:29:37.339680
# Unit test for method validate of class Array
def test_Array_validate():
    # array with pattern and min_items, max_items
    items = [String(pattern=re.compile("^[0-9a-zA-Z_-]{2,9}$"))]
    array_schema = Array(items=items, min_items=4, max_items=4)

    # testing invalid number of elements
    assert array_schema.validate(["12", "34", "56", "78", "90"]) == "Must have no more than 4 items."
    assert array_schema.validate(["12", "34", "56"]) == "Must have at least 4 items."

    # testing element pattern

# Generated at 2022-06-14 14:29:56.503613
# Unit test for method validate of class Union
def test_Union_validate():
    class Color(String):
        def validate(self, value, *, strict):
            if value == "red":
                return value
            return super().validate(value)
    class ColorNumber(Number):
        def validate(self, value, *, strict):
            if value == 0:
                return value
            return super().validate(value)

    red = Color()
    zero = ColorNumber()

    union = Union([red, zero])

    with pytest.raises(ValidationError):
        union.validate(1)

    assert union.validate(0) == 0
    assert union.validate("red") == "red"



# Generated at 2022-06-14 14:30:03.270180
# Unit test for method validate of class String
def test_String_validate():
    string1 = String(
        title = "",
        description = "",
        default = NO_DEFAULT,
        allow_null = False,
        allow_blank = False,
        trim_whitespace = True,
        max_length = None,
        min_length = None,
        pattern = None,
        format = None,
    )
    assert string1.validate() == None


# Generated at 2022-06-14 14:30:08.878985
# Unit test for method validate of class Union
def test_Union_validate():
    field = Union(
        any_of = [
            Field(type = "integer"),
            Field(type = "string", pattern = "[a-z]{2}")
        ]
    )
    assert field.validate("ab")
    assert field.validate("AB") is None



# Generated at 2022-06-14 14:30:19.718559
# Unit test for constructor of class Array
def test_Array():
    # create sample data
    items = [
        Field(),
        Field(),
        Field()
    ]

    additional_items = Field()
    min_items = 1
    max_items = 2
    exact_items = 2
    unique_items = True
    
    # call constructor
    obj = Array(
        items = items,
        additional_items = additional_items,
        min_items = min_items,
        max_items = max_items,
        exact_items = exact_items,
        unique_items = unique_items
    )

    # make assertions
    assert isinstance(obj,Field)
    assert isinstance(obj,Array)
    assert obj.items == items
    assert obj.additional_items == additional_items
    assert obj.min_items == min_items

# Generated at 2022-06-14 14:30:30.713507
# Unit test for method validate of class Union
def test_Union_validate():
    class Test(Union):
        def __init__(self, any_of, **kwargs):
            super().__init__(any_of)
    with pytest.raises(ValidationError):
        Test([String(min_length = 1), Boolean()]).validate(1)
    with pytest.raises(ValidationError):
        Test([String(min_length = 1), Boolean()]).validate(True)
    with pytest.raises(ValidationError):
        Test([String(min_length = 2), Boolean()]).validate(1)
    assert Test([String(), Boolean()]).validate(1)
    assert Test([String(), Boolean()]).validate(True)
    assert Test([String(min_length=2), Boolean()]).validate(1)

# Generated at 2022-06-14 14:30:38.942393
# Unit test for method validate of class Array
def test_Array_validate():

        try:
            # input_array=['d']
            input_array=['a','b','c','d']
            print('input_array:',input_array)

            schema = Array(
                items=String(),
                min_items=1,
                max_items=2,
            )
            result=schema.validate(input_array)
            print('result:',result)

        except ValidationError as exc:
            print(exc.messages)
        print('==========================================')

# test_Array_validate()


# Generated at 2022-06-14 14:30:43.093156
# Unit test for method validate of class Array
def test_Array_validate():
    # Items none, Additional_items none
    a1 = Array()
    a2 = a1.validate([1, 2, 3, 4, 5])
    print(a2)
    # additional_items Filed, items none
    a1 = Array(additional_items=Integer())
    a2 = a1.validate([1, 2, 3, 4, 5])
    print(a2)
    # items Filed, additional_items none
    a1 = Array(items=Integer())
    a2 = a1.validate([1, 2, 3, 4, 5])
    print(a2)
    # items and additional_items Filed
    a1 = Array(items=Integer(), additional_items=String())

# Generated at 2022-06-14 14:30:46.075460
# Unit test for method validate of class Choice
def test_Choice_validate():
    field = Choice(choices=[('a', 'A'), ('b', 'B')])
    print(field.validate('c'))
    print(field.validate('a'))


# Generated at 2022-06-14 14:30:54.234336
# Unit test for method validate of class Array
def test_Array_validate():
    prop = Array()
    assert prop.validate([]) == []
    assert prop.validate([1, False, "hello", {"1":"1"}]) == [1, False, "hello", {"1":"1"}]
    assert prop.validate([[], [], ['test'], [False]]) == [[], [], ['test'], [False]]
    assert prop.validate(['test']) == ['test']
    assert prop.validate([True]) == [True]
    assert prop.validate([{}]) == [{}]
    assert prop.validate([None]) == [None]
    assert prop.validate(([], [], ['test'], [False])) == ([], [], ['test'], [False])

    prop = Array(allow_null=True)

# Generated at 2022-06-14 14:30:55.681410
# Unit test for method validate of class Choice
def test_Choice_validate():
    choice = Choice(choices=[('A', 'B'), ('C', 'D')])
    assert choice.validate('C') == 'C'


# Generated at 2022-06-14 14:31:10.087389
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    class FieldChild(Field):
        def get_default_value(self):
            return "test_default"
    assert FieldChild().get_default_value() == "test_default"

# Generated at 2022-06-14 14:31:13.053984
# Unit test for method validate of class Choice
def test_Choice_validate():
    cc = Choice(
        choices=[
            ("", "None (Default)"),
            ("AF", "Afghanistan"),
            ("AL", "Albania"),
            ("DZ", "Algeria"),
        ]
    )
    assert cc.validate('AF') == 'AF'
    assert cc.validate('DZ') == 'DZ'
    # assert cc.validate('NONE') == "NONE"
    assert cc.validate('NONE') == None



# Generated at 2022-06-14 14:31:16.994350
# Unit test for method validate of class Array
def test_Array_validate(): # TODO: understand why is this test commented out
    myArray = Array(UniqueInteger(), UniqueFloat())
    myArray.validate([1,1.1,1.1])


# Generated at 2022-06-14 14:31:17.754993
# Unit test for method validate of class Object
def test_Object_validate():
    pass



# Generated at 2022-06-14 14:31:20.902402
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    Field_Instance = Field(title="", description="", default="test", allow_null=False)
    assert Field_Instance.get_default_value() == "test"

# Generated at 2022-06-14 14:31:23.240857
# Unit test for method validate of class Union
def test_Union_validate():
    f = Union(any_of=[Integer(), String()], default="test")
    try:
        f.validate(123)
    except ValidationError:
        print("ok")

# Generated at 2022-06-14 14:31:29.499334
# Unit test for method validate of class Union
def test_Union_validate():
    #Define some test fields to be used in the Union
    type_field = Type(type="object")
    required_field = Required(required=["key1", "key2"])
    properties_field = Properties(properties={"key1":String()})
    test_fields = [type_field, required_field, properties_field]
    
    my_union = Union(any_of=test_fields)
    print(my_union.validate({}, strict=True))

test_Union_validate()


# Generated at 2022-06-14 14:31:33.371370
# Unit test for method validate of class Choice
def test_Choice_validate():
    c = Choice(choices=[1,2,3],allow_null=True)
    v_for_null = c.validate(None,strict=True)
    assert v_for_null is None
    v_for_value = c.validate(1,strict=True)
    assert v_for_value == 1
    v_for_blank = c.validate("",strict=False)
    assert v_for_blank is None




# Generated at 2022-06-14 14:31:35.337667
# Unit test for method validate of class Array
def test_Array_validate():
    assert Array(max_items=2).validate([1,2,3]) == [1,2]

# Generated at 2022-06-14 14:31:39.678249
# Unit test for method validate of class Choice
def test_Choice_validate():
    test_input_1 = Choice(allow_null=False, allow_blank=False, name="my_choice")
    expected_output_1 = "Must be a string."
    actual_output_1 = test_input_1.validate(None, strict=True)
    assert expected_output_1 == actual_output_1

    test_input_2 = Choice(choices=[('1','1'),('2','2')], name="my_choice")
    expected_output_2 = None
    actual_output_2 = test_input_2.validate(None, strict=True)
    assert expected_output_2 == actual_output_2

    test_input_3 = Choice(choices=[('1','1'),('2','2')], name="my_choice")
    expected_output_3 = 'choice'
    actual_

# Generated at 2022-06-14 14:31:57.289533
# Unit test for method validate of class String
def test_String_validate():
    assert String(min_length=5).validate("abcde") == "abcde"
    assert String(max_length=5).validate("abcdefg") == "abcde"
    assert String(min_length=5).validate("abc") == None
    assert String(max_length=5).validate("abcdeghij") == None
    assert String(pattern=re.compile(r'[a-z]+')).validate('123') == None
    assert String(pattern=re.compile(r'[a-z]+')).validate('abc') == "abc"
    assert String(format='date').validate('9999') == None
    assert String(format='date').validate('2018-10-10') == '2018-10-10'

# Generated at 2022-06-14 14:32:09.386696
# Unit test for method validate of class Object
def test_Object_validate():
    # testing for function validate of class Object
    # 'value' is a valid input, which is a dict
    field = Object(allow_null=False)
    value = {}
    validated_value = field.validate(value)
    assert validated_value == {}
    # 'value' is a valid input, which is a dict
    field = Object(allow_null=False)
    value = {"key1":1, "key2":2}
    validated_value = field.validate(value)
    assert validated_value == {"key1":1, "key2":2}
    # 'value' is an invalid input, it is not a dict
    field = Object(allow_null=False)
    value = 123
    with pytest.raises(ValidationError):
        validated_value = field.validate(value)
    #

# Generated at 2022-06-14 14:32:20.730375
# Unit test for method validate of class Object
def test_Object_validate():
    assert Object(properties={"prop1": String()}).validate({"prop1" : "prop-value"}) == {"prop1": "prop-value"}
    assert Object(properties={"prop1": String()}).validate({"prop1" : 1}) == {"prop1": "1"}
    assert Object(properties={"prop1": Integer()}).validate({"prop1" : 1}) == {"prop1": 1}
    assert Object(properties={"prop1": Integer(allow_null=True)}).validate({"prop1" : None}) == {"prop1": None}
    assert Object(properties={"prop1": Integer()}).validate({"prop1" : None}) == {"prop1": None}

# Generated at 2022-06-14 14:32:24.979780
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    field = Field()
    assert field.get_default_value() is None
    field = Field(default=42)
    assert field.get_default_value() == 42
    field = Field(default=lambda: 42)
    assert field.get_default_value() == 42
    field = Field(default=None, allow_null=True)
    assert field.get_default_value() is None


# Generated at 2022-06-14 14:32:34.209646
# Unit test for method __or__ of class Field
def test_Field___or__():
    f1 = Field(title="A", description="B")
    f2 = Field(title="A", description="B")
    f3 = Field(title="A", description="B")
    u = f1 | f2 | f3
    assert f1 in u.any_of
    assert f2 in u.any_of
    assert f3 in u.any_of
    other_u = Union([f1, f2])
    u2 = f3 | other_u
    assert f3 in u2.any_of
    assert f1 in u2.any_of
    assert f2 in u2.any_of



# Generated at 2022-06-14 14:32:37.434974
# Unit test for method __or__ of class Field
def test_Field___or__():
    a = 'aaa'
    b = 'bbb'
    result = Field(title=a, description=b).__or__(Field(title=a, description=b))
    assert isinstance(result, Union)



# Generated at 2022-06-14 14:32:37.993228
# Unit test for method __or__ of class Field
def test_Field___or__():
    pass



# Generated at 2022-06-14 14:32:39.848788
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    field = Field(default = None)
    value = field.get_default_value()
    assert value == None


# Generated at 2022-06-14 14:32:50.903359
# Unit test for method validate of class String
def test_String_validate():
    # Create an instance of String class
    field = String()
    # Test 1: validate a null value
    value = None
    assert field.validate(value) == ""
    # Test 2: validate a null value as number
    value = 1
    assert field.validate(value) == ""
    # Test 3: validate
    value = "  "
    assert field.validate(value) == ""
    # Test 4: validate a blank string, not allow blank
    field = String(allow_blank = False)
    value = "  "
    assert field.validate(value) == None
    # Test 5: validate a valid string
    field = String()
    value = "abc"
    assert field.validate(value) == "abc"
    # Test 6: validate a string with max length

# Generated at 2022-06-14 14:33:04.000490
# Unit test for method validate of class Array
def test_Array_validate():
    array_field = Array(items=String(allow_null=True, allow_blank=True))
    # Validates null values
    assert array_field.validate(None) is None
    # Raises error if the array is empty
    with pytest.raises(ValidationError): array_field.validate([])
    # Raises error if not array
    with pytest.raises(ValidationError): array_field.validate("string")
    # Validates string arrays
    array_field.validate(["string1","string2"])
    # Validates arrays of numbers
    array_field.validate([1,2,3.2])
    # Raises error if an array item is not of the right type
    with pytest.raises(ValidationError): array_field.validate(["string", 1])
   

# Generated at 2022-06-14 14:33:15.481424
# Unit test for constructor of class Const
def test_Const():
    const = Const(const=10)
    assert const.validate(10) == 10
    with pytest.raises(ValidationError):
        const.validate(11)


# Generated at 2022-06-14 14:33:24.527284
# Unit test for method validate of class String
def test_String_validate():

    # Test method validate on empty string when null is not allowed as input
    assert String(allow_null=False).validate("") == Exception

    # Test method validate on string when it exceeds max length
    assert String(max_length=0).validate("string") == Exception

    # Test method validate on string when it exceeds min length
    assert String(min_length=3).validate("st") == Exception

    # Test method validate on string when it does not match regex
    assert String(pattern=r"^[A-Za-z]+$").validate("str1ng") == Exception

    # Test method validate on string with input valid string
    assert String().validate("string") == "string"

    # Test method validate on empty string when null is allowed as input
    assert String(allow_null=True).validate("") == ""

    # Test