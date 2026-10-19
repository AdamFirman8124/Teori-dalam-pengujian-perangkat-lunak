

# Generated at 2022-06-14 14:24:27.310736
# Unit test for method serialize of class String
def test_String_serialize():
    g=String(title='Name',description='Email',allow_blank=True)
    assert g.serialize(1)==1
    g=String(title='Name',description='Email',format='datetime')
    assert g.serialize('2020-06-13T16:00:00Z')== datetime.datetime(2020, 6, 13, 16, 0, tzinfo=datetime.timezone.utc)


# Generated at 2022-06-14 14:24:37.755368
# Unit test for method validate of class Union
def test_Union_validate():
    assert Union([
        Integer(),
        String()
    ]).validate(123) == 123
    assert Union([
        Integer(),
        String()
    ]).validate("123") == "123"

    # error if value is null
    with pytest.raises(ValidationError, match="null"):
        Union([
            Integer(),
            String()
        ]).validate(None)

    # error if value is of wrong type
    with pytest.raises(ValidationError, match="union"):
        Union([
            Integer(),
            String()
        ]).validate(1.23)


# Generated at 2022-06-14 14:24:42.299344
# Unit test for method serialize of class String
def test_String_serialize():
    str_object = String(min_length=5, max_length=20)
    # Expected result
    string_result = "test"
    # Actual result
    string_result_serialize = str_object.serialize("test")
    # Test result
    assert string_result_serialize == string_result



# Generated at 2022-06-14 14:24:51.716431
# Unit test for constructor of class Array
def test_Array():
    a = Array()

    # min_items + max_items
    a = Array(min_items=1)
    assert a.min_items == 1
    a = Array(max_items=1)
    assert a.max_items == 1
    a = Array(min_items=1, max_items=1)
    assert a.min_items == 1
    assert a.max_items == 1
    assert a.exact_items is None

    # exact_items
    a = Array(exact_items=1)
    assert a.exact_items == 1
    assert a.min_items == 1
    assert a.max_items == 1

    # additional_items
    a = Array(additional_items=True)
    assert a.additional_items is True

# Generated at 2022-06-14 14:24:59.988292
# Unit test for method serialize of class Array
def test_Array_serialize():
    field = Array(items=Integer())
    assert field.serialize([1, 2, 3]) == [1, 2, 3]
    assert field.serialize([]) == []
    assert field.serialize(None) == None

    field = Array(items=Integer())
    assert field.serialize([1, 2, 3]) == [1, 2, 3]
    assert field.serialize([]) == []
    assert field.serialize(None) == None

A = typing.TypeVar("A")



# Generated at 2022-06-14 14:25:10.988367
# Unit test for method validate of class Number
def test_Number_validate():
    class TestNumber(Number):
        numeric_type = int
    num_str = '123'
    num_str_error='abc'
    num_int = 123
    num_int_error = 123.123
    num_float = 123.123
    num_float_error = '123.123'
    testNum = TestNumber()
    try:
        parse_num_int = testNum.validate(num_int)
        assert parse_num_int == num_int
    except ValidationError:
        assert False
    try:
        parse_num_int_error = testNum.validate(num_int_error)
        print(parse_num_int_error)
        assert False
    except ValidationError:
        assert True

# Generated at 2022-06-14 14:25:17.225373
# Unit test for constructor of class Array
def test_Array():
    a = Array(items=[String(), Integer()], max_items=2, min_items=1, unique_items=True, strict=False)
    b = Array(items=[String(), Integer()], max_items=2, min_items=1, unique_items=True, strict=True)
    c = Array(items=String(), max_items=2, min_items=1, unique_items=True, strict=False)
    d = Array(items=String(), max_items=2, min_items=1, unique_items=True, strict=True)

    assert isinstance(a, Array)
    assert a.items[0] == String()
    assert a.items[1] == Integer()
    assert a.max_items == 2
    assert a.min_items == 1
    assert a.unique_items == True
   

# Generated at 2022-06-14 14:25:22.430603
# Unit test for constructor of class Integer
def test_Integer():
    i = Integer(minimum=10, maximum=15, exclusive_minimum=20, exclusive_maximum=25, multiple_of=5)
    assert i.minimum == 10
    assert i.maximum == 15
    assert i.exclusive_minimum == 20
    assert i.exclusive_maximum == 25
    assert i.multiple_of == 5
    assert i.numeric_type == int

    # test validation
    value = 8
    with pytest.raises(ValidationError) as err:
        i.validate(value)
    assert "Must be greater than or equal to 10." == str(err.value)


# Generated at 2022-06-14 14:25:32.614712
# Unit test for method validate of class Object
def test_Object_validate():
    properties = {
        "name": String(required = True),
        "age": Integer(maximum = 10),
        "job": String(required = True)
    }
    Object = Object(
        properties = properties, min_properties = 2, max_properties = 4, additional_properties = False, required = ["name", "age"]
    )
    assert Object.validate({
            "name": "a",
            "age": 1,
            "b": "c"
        }) == {
            "name": "a",
            "age": 1
        }
    try:
        Object.validate({"name": "a"})
    except:
        assert True
    try:
        Object.validate({"name": "a", "age": 11})
    except:
        assert True

# Generated at 2022-06-14 14:25:34.847973
# Unit test for method validate of class String
def test_String_validate():
    test1 = String(max_length=5)
    result1 = test1.validate("abcd")
    assert result1 == "abcd"


# Generated at 2022-06-14 14:26:01.513510
# Unit test for method validate of class Array
def test_Array_validate():
    schema = Array(
        items=[
            Integer(
                required=True,
                minimum=0,
            ),
            String(
                required=True,
                max_length=5,
            ),
        ],
        additional_items=String(max_length=5),
        min_items=0,
        max_items=5,
        unique_items=True,
        allow_null=False,
    )
    # Given the following value to be validated by the schema above
    given = [1, "a", "b", "c", "d", "e", "f", "g"]
    # We expect to obtain the following validated value
    expected = [1, "a", "b", "c", "d", "e"]
    # When we call method validate of class Array
    actual = schema.validate(given)


# Generated at 2022-06-14 14:26:05.309122
# Unit test for method validate of class Choice
def test_Choice_validate():
    err = "Not a valid choice."
    choices = [
        (1, "1"),
        (2, "2"),
        "'3'",
        True,
    ]
    _ = Choice(choices=choices)
    assert(Choice._validate(True,strict=False) is True)
    assert(Choice._validate(1,strict=False) is 1)
    assert(Choice._validate(2,strict=False) is 2)
    assert(Choice._validate("'3'",strict=False) is "'3'")
    assert(Choice._validate("5",strict=False) == err)
    assert(Choice._validate(5,strict=False) == err)



# Generated at 2022-06-14 14:26:16.706669
# Unit test for method validate of class Array
def test_Array_validate():
    # 1
    field_arr = Array()
    value = []
    assert field_arr.validate(value) == value

    # 2
    value = None
    assert field_arr.validate(value) == value

    # 3
    field_arr = Array(allow_null=False)
    value = None
    with pytest.raises(ValidationError) as error:
        field_arr.validate(value)
    assert 'May not be null.' in error.value.error().messages()[0].text

    # 4
    field_arr = Array(allow_null=False)
    value = []
    with pytest.raises(ValidationError) as error:
        field_arr.validate(value)
    assert 'Must not be empty.' in error.value.error().messages()[0].text

# Generated at 2022-06-14 14:26:22.934433
# Unit test for method validate of class Array
def test_Array_validate():
    # WHEN
    validate = Array(
        items=Integer(maximum=100, minimum=1),
        additional_items=Field(),
        min_items=3,
        max_items=5,
        unique_items=False,
        allow_null=False,
        default=None,
        title=None,
        description=None,
    ).validate

    # THEN
    assert validate([1,2,3]) == [1,2,3]
    try:
        validate([1,2,3,4,5,4])
    except ValidationError:
        assert True
    try:
        validate([1,2,3,4,5,6])
    except ValidationError:
        assert True
    try:
        validate([1])
    except ValidationError:
        assert True

# Generated at 2022-06-14 14:26:25.989354
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    f = Field()
    f.default = 5
    assert f.get_default_value() == 5
    f.default = lambda: 10
    assert f.get_default_value() == 10



# Generated at 2022-06-14 14:26:35.607156
# Unit test for method validate of class Choice
def test_Choice_validate():
    test = Choice(choices=(
        ("河北", "河北"),
        ("河南", "河南"),
        ("山西", "山西"),
        ("山东", "山东"),
    ), name='province', source='province')
    assert test.validate("河北") == "河北"
    assert test.validate("内蒙古") == "内蒙古"



# Generated at 2022-06-14 14:26:44.576518
# Unit test for method validate of class Choice
def test_Choice_validate():
    # Case 1 : a simple case
    fname = Choice(
        name="name",
        label="Name",
        required=True,
        choices=[("A", "Alan"), ("B", "Bob"), ("C", "Carl")],
    )
    value = "A"
    assert fname.validate(value = value) == "A"
    # Case 2 : the value is not in the choices
    value = "X"
    with pytest.raises(ValidationError):
        fname.validate(value = value)
    # Case 3 : value is None (and allow_null is not set)
    value = None
    with pytest.raises(ValidationError):
        fname.validate(value = value)
    # Case 4 : value is None (and allow_null is set)
    fname.allow

# Generated at 2022-06-14 14:26:45.761238
# Unit test for constructor of class Const
def test_Const():
    assert Const(True).validate(True) == True
    assert Const(True).validate(False) == False
    assert Const(True).validate(None) == None

# Generated at 2022-06-14 14:26:51.786521
# Unit test for method serialize of class Array
def test_Array_serialize():
    assert Array(items=None).serialize("a") == "a"
    assert Array(items=None).serialize("hello") == "hello"
    assert Array(items=None).serialize(1) == 1
    assert Array(items=None).serialize(3.14) == 3.14

    assert Array(items=Integer()).serialize([1]) == [1]
    assert Array(items=Integer()).serialize([1,2,3]) == [1,2,3]
    assert Array(items=Integer()).serialize([5,6.7]) == [5,6]
    assert Array(items=Integer()).serialize([9.9,8]) == [9,8]

    assert Array(items=Integer()).serialize(["1"]) == [1]
    assert Array(items=Integer()).serial

# Generated at 2022-06-14 14:26:54.321257
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    field = Field(title='title', description='description', allow_null=False, default=None)
    assert field.get_default_value() == None
    field.default = 1
    assert field.get_default_value() == 1

# Generated at 2022-06-14 14:27:39.671789
# Unit test for method validate of class Choice
def test_Choice_validate():
    try:
        choice_field=Choice(choices=[1,3,4], allow_null=True, description="test case")
        choice_field.validate(1)
    except ValidationError as ve:
        print('ValidationError',ve.text)
    try:
        choice_field=Choice(choices=[1,3,4], allow_null=False, description="test case")
        choice_field.validate('')
    except ValidationError as ve:
        print('ValidationError',ve.text)
    try:
        choice_field=Choice(choices=[1,3,4], allow_null=False, description="test case")
        choice_field.validate(5)
    except ValidationError as ve:
        print('ValidationError',ve.text)

        
test_Choice_valid

# Generated at 2022-06-14 14:27:41.257542
# Unit test for method validate of class Array
def test_Array_validate():
    # unit tests for Array method validate
    # TODO: write unit tests for Array method validate
    pass



# Generated at 2022-06-14 14:27:49.458374
# Unit test for method validate of class Choice
def test_Choice_validate():
    choice = Choice(allow_null=True)
    assert choice.validate(None, strict=False) == None
    try:
        choice.validate(None, strict=True)
    except Exception as error:
        assert isinstance(error,ValidationError)
        assert error.text == "May not be null."
        assert error.code == "null"
    try:
        choice.validate(None)
    except Exception as error:
        assert isinstance(error,ValidationError)
        assert error.text == "May not be null."
        assert error.code == "null"
    try:
        choice.validate("", strict=False)
    except Exception as error:
        assert isinstance(error,ValidationError)
        assert error.text == "This field is required."
        assert error.code == "required"

# Generated at 2022-06-14 14:28:01.046277
# Unit test for method validate of class String
def test_String_validate():
    # Case 1 - Normal Case
    value = "1234567890"
    result = String().validate(value)
    assert result == value
    
    # Case 2 - Normal Case
    value = "abcdefgh"
    result = String(max_length = 10).validate(value)
    assert result == value
    
    # Case 3 - Normal Case
    value = "abcdefghij"
    result = String(min_length = 10).validate(value)
    assert result == "abcdefghij"
    
    # Case 4 - Normal Case
    value = "1234567890"
    result = String(pattern = "^[a-zA-Z0-9_-]{3,20}$").validate(value)
    assert result == "1234567890"
    
    # Case 5 - Normal Case

# Generated at 2022-06-14 14:28:06.019021
# Unit test for method validate of class Union
def test_Union_validate():
    class Foo(Field):
        def validate(self, value, *, strict = False):
            if len(value) == 2:
                return value
            raise self.validation_error('type')
    class Bar(Field):
        def validate(self, value, *, strict = False):
            if len(value) == 3:
                return value
            raise self.validation_error('type')
    class Baz(Field):
        def validate(self, value, *, strict = False):
            if len(value) == 4:
                return value
            raise self.validation_error('type')
    class Qux(Field):
        def validate(self, value, *, strict = False):
            if len(value) == 5:
                return value
            raise self.validation_error('type')


# Generated at 2022-06-14 14:28:07.756724
# Unit test for method validate of class Union
def test_Union_validate():
    new_field = Union([String(), Integer()])
    assert new_field.validate("test") == "test"
    assert new_field.validate(3) == 3




# Generated at 2022-06-14 14:28:10.651974
# Unit test for method validate of class Choice
def test_Choice_validate():
    choice_field = Choice(choices = [ ( "1", "one" ), ( "2", "two" ) ])
    assert choice_field.validate(1) == 1
    assert choice_field.validate("2") == "2"
    assert choice_field.validate() == None
    assert choice_field.validate(3) == None


# Generated at 2022-06-14 14:28:11.523774
# Unit test for method validate of class Array
def test_Array_validate():
    test_instance = Array()
    test_instance.validate([])


# Generated at 2022-06-14 14:28:22.705681
# Unit test for method validate of class Choice
def test_Choice_validate():
    assert Choice(choices=[""]).validate(value="") == ""
    assert Choice(choices=[""]).validate(value=None) == None
    assert Choice(choices=[""]).validate(value="random string") == "random string"
    assert Choice(choices=[""], allow_null=True).validate(value="") == ""
    assert Choice(choices=[""], allow_null=True).validate(value=None) == None
    assert Choice(choices=[""], allow_null=True).validate(value="random string") == "random string"
    assert Choice(choices=[""]).validate(value="", strict=True) == ""
    assert Choice(choices=[""]).validate(value=None, strict=True) == None
    assert Choice(choices=[""]).valid

# Generated at 2022-06-14 14:28:26.592225
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    field = Field(title = "", description = "", default = "")
    val = field.get_default_value()
    print("expected: " + "")
    print("actual: " + val)
    assert val == ""


# Generated at 2022-06-14 14:28:43.976951
# Unit test for method validate of class Choice
def test_Choice_validate():
    assert Choice(choices=[("test", "test")]).validate("test")
    assert Choice(choices=[("test", "test")]).validate("test") == "test"
    assert Choice(choices=[("test", "test")]).validate("test") != None
    assert Choice(choices=[("test", "test")]).validate("test") == "test"
    assert Choice(choices=[("test", "test")]).validate("abc") != "abc"
    assert Choice(choices=[("test", "test")]).validate(None) == None
    assert Choice(choices=[("test", "test")]).validate(None) != "abc"



# Generated at 2022-06-14 14:28:51.323820
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    # assert
    assert Field().get_default_value() == None
    assert Field(default=1).get_default_value() == 1
    assert Field(default="a").get_default_value() == "a"
    assert Field(default="a").__dict__ == {'title': '', 'description': '', 'allow_null': False, 'default': 'a', '_creation_counter': 0}

###################################################################################################

# Generated at 2022-06-14 14:28:55.471690
# Unit test for method validate of class Number
def test_Number_validate():
    t = Number()
    assert(t.validate(3) == 3)
    assert(t.validate(3.4) == 3.4)
    assert(t.validate(True) == True)
    assert(t.validate("77") == 77)


# Generated at 2022-06-14 14:29:06.404411
# Unit test for constructor of class Array
def test_Array():
    field1 = Array(items=String(min_length=2))
    assert field1.items.min_length == 2
    field2 = Array(items=Integer())
    assert field2.items.__class__.__name__ == "Integer"
    field3 = Array(items=Null())
    assert field3.items.__class__.__name__ == "Null"
    field4 = Array(items=[String(), Null()])
    assert field4.items[0].__class__.__name__ == "String"
    assert field4.items[1].__class__.__name__ == "Null"
    field5 = Array(items=String(min_length=2), min_items = 2)
    assert field5.min_items == 2

# Generated at 2022-06-14 14:29:16.996529
# Unit test for method validate of class String
def test_String_validate():
    # Test case 1
    title = "test 1"
    field = String(title=title, default="", allow_null=True, format="date")
    assert field.validate("2020-06-01") == datetime.datetime(2020, 6, 1)
    # Test case 2
    title = "test 2"
    field = String(title=title, default="", allow_null=True, format="date")
    assert field.validate("2020-06-01") == datetime.datetime(2020, 6, 1)
    # Test case 3
    title = "test 3"
    field = String(title=title, default="", allow_null=False, format="date")
    assert field.validate("2020-06-01") == datetime.datetime(2020, 6, 1)
    # Test case 4
   

# Generated at 2022-06-14 14:29:26.650195
# Unit test for method validate of class Union
def test_Union_validate():
    _map_type_to_class = {
        "integer": Integer,
        "number": Number,
        "string": String,
        "boolean": Boolean,
    }
    sample_json_schema = [
        {
        "anyOf": [
            {
                "type": "integer"
            },
            {
                "type": "number"
            }
        ]
    },
    {
        "anyOf": [
            {
                "type": "string"
            },
            {
                "type": "boolean"
            }
        ]
    }
]

    schema = {
        "anyOf": [
            {
                "type": "integer"
            },
            {
                "type": "number"
            }
        ]
    }

# Generated at 2022-06-14 14:29:28.226080
# Unit test for method validate of class Object
def test_Object_validate():
    o = Object()
    o.validate({"abc": "abc"})
    
    

# Generated at 2022-06-14 14:29:37.306721
# Unit test for method validate of class Choice
def test_Choice_validate(): 
    field = Choice(choices = ["one", "two", "three"])
    assert field.validate("one") == "one"
    assert field.validate("two") == "two"
    assert field.validate("three") == "three" 
    assert field.validate("") == "" 
    assert field.validate(5) == "" 
    assert field.validate(None) == "null"
    assert field.validate("four") == "not a valid choice"



# Generated at 2022-06-14 14:29:42.256650
# Unit test for method validate of class Union
def test_Union_validate():
    field = Union([String(), Number()])
    field.validate(0)
    field.validate("string")
    try:
        field.validate(True)
    except ValidationError as e:
        assert len(e.messages()) == 1
        assert e.messages()[0].code == "union"
        assert e.messages()[0].index == []
    else:
        assert 1 == 0



# Generated at 2022-06-14 14:29:49.630012
# Unit test for method validate of class Object
def test_Object_validate():
    schema = Object(properties={"number": Integer()})
    out, err = schema.validate_or_error({"number": 1})
    assert out == {"number": 1}

    out, err = schema.validate_or_error({"number": 1.0})
    assert out == {"number": 1}
    print(err.messages())
    assert any(message.code == "type" for message in err.messages())

    out, err = schema.validate_or_error({"number": 1, "extra": 2})
    assert out == {"number": 1, "extra": 2}

    schema_2 = Object(properties={"number": Integer()}, additional_properties=False)
    out, err = schema_2.validate_or_error({"number": 1, "extra": 2})

# Generated at 2022-06-14 14:30:06.021926
# Unit test for method validate of class Choice
def test_Choice_validate():
    c = Choice()
    assert c.validate("a") == "a"
    assert c.validate("b") == "b"
    assert c.validate("c") == "c"
    assert c.validate("d") == "d"
    #Raise error when value is not in the list of choices
    with pytest.raises(ValidationError):
        assert c.validate("k")
    #Raise error when value of an attribute is not a str
    with pytest.raises(ValidationError):
        assert c.validate(1)


# Generated at 2022-06-14 14:30:10.153805
# Unit test for method __or__ of class Field
def test_Field___or__():
    class TestField(Field):
        pass
    assert TestField() | TestField() == TestField() | TestField()
    assert TestField() | TestField() | TestField() == TestField() | TestField() | TestField()



# Generated at 2022-06-14 14:30:13.678283
# Unit test for method __or__ of class Field
def test_Field___or__():
    from typesystem.union import Union
    from typesystem.string import String
    from typesystem.integer import Integer
    s = String()
    i = Integer()
    assert s | i == Union([s, i])


# Generated at 2022-06-14 14:30:21.371928
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    class Field_get_default_value_schema(Schema):
        class Meta:
            fields = ["field2"]

        field1 = Field1()
        field2 = Field2()

    class Field_get_default_value_schema_obj(object):
        pass
    a = Field_get_default_value_schema(data=Field_get_default_value_schema_obj)

    assert a.field1.get_default_value() == "default_value"
    assert a.field2.get_default_value() == "default_value"
    print("get_default_value of class Field: passed")



# Generated at 2022-06-14 14:30:32.155920
# Unit test for method __or__ of class Field
def test_Field___or__():
    # Test or operator for class Field
    assert Field(title="Title") | Field(title="Other title") == Union(any_of=[Field(title="Title"),
                      Field(title="Other title")])
    assert Field(title="Other title") | Field(title="Title") == Union(any_of=[Field(title="Other title"),
                      Field(title="Title")])
    assert Field(title="Other title") | Field(title="Other title") == Union(any_of=[Field(title="Other title"),
                      Field(title="Other title")])
    assert Field(title="Title") | Field(title="Title") == Union(any_of=[Field(title="Title"),
                      Field(title="Title")])

# Generated at 2022-06-14 14:30:35.570261
# Unit test for method validate of class Choice
def test_Choice_validate():
    choice=Choice()
    choice.validate(None)
    choice.validate(1)
    choice.validate(2)



# Generated at 2022-06-14 14:30:41.439639
# Unit test for method validate of class Union
def test_Union_validate():

    schema= Union([Enum(["A", "B"])])
    assert schema.validate(None) == None

    schema= Union([Enum(["A", "B"])])
    try:
        assert schema.validate(1)
    except ValidationError as error:
        assert error.messages() == [Message(code="type", text="Must be one of: 'A', 'B'.", path=[])]


# Generated at 2022-06-14 14:30:50.996929
# Unit test for method validate of class Object
def test_Object_validate():
    schema = Object(properties={'a': String()})
    # Validating an dictionary.
    assert(schema.validate({'a': 'abc'}) == {'a': 'abc'})
    # Validating non-dictionary object
    with pytest.raises(ValidationError):
        schema.validate(['a', 'b', 'c'])
    # Validating non-dictionary object with strict as True
    with pytest.raises(ValidationError):
        schema.validate(['a', 'b', 'c'], strict=True)
    # Validating empty dictionary object.
    assert(schema.validate({}) is not None)
    # Validating string
    with pytest.raises(ValidationError):
        schema.validate('a')
    # Validating string with strict as True
   

# Generated at 2022-06-14 14:30:57.318601
# Unit test for method validate of class Union
def test_Union_validate():
    raise NotImplementedError

    # self.assertIsNone(value)
    # self.assertEqual(tuple(value), ())
    # self.assertEqual(type(value), tuple)
    # self.assertEqual(len(value), 0)
    # self.assertEqual(len(value), 1)
    # self.assertEqual(value, False)
    # self.assertEqual(value, True)
    # self.assertEqual(value, 0)
    # self.assertEqual(value, 0.0)
    # self.assertEqual(value, '')
    # self.assertEqual(len(value), 1)
    # self.assertEqual(value, True)
    # self.assertEqual(value, 0)
    # self.assertEqual(value, '')

# Generated at 2022-06-14 14:30:59.405173
# Unit test for method __or__ of class Field
def test_Field___or__():
    try:
        Field() or Field()
    except Exception as e:
        print(e)
    else:
        raise Exception("no error")



# Generated at 2022-06-14 14:31:13.611113
# Unit test for method validate of class Array
def test_Array_validate():
    a = Array(items=String(), additional_items=String())
    try:
        a.validate(3)
    except ValidationError as e:
        assert e.error_messages[0].text == "Must be an array."
        assert e.error_messages[0].code == "type"
    else:
        raise Exception("Should raise an exception")
        
    try:
        a.validate([3])
    except ValidationError as e:
        assert e.error_messages[0].text == "Must be a string."
        assert e.error_messages[0].code == "type"
    else:
        raise Exception("Should raise an exception")
        
    try:
        a.validate([1, 2, 3])
    except ValidationError as e:
        assert e.error_mess

# Generated at 2022-06-14 14:31:25.171384
# Unit test for method validate of class Array
def test_Array_validate():
    array_of_strings = Array(items=String())

    with pytest.raises(ValidationError) as e:
        array_of_strings.validate(123)
    assert [m.text for m in e.value.messages] == ["Must be an array."]

    with pytest.raises(ValidationError) as e:
        array_of_strings.validate(["foo", "bar", 123])
    assert [m.text for m in e.value.messages] == ["Must be a string."]

    assert array_of_strings.validate(["foo", "bar"]) == ["foo", "bar"]


array_of_strings = Array(items=String())


# Generated at 2022-06-14 14:31:33.443625
# Unit test for method validate of class Union
def test_Union_validate():
    assert Union([Integer(), Float()]).validate(1.45) == 1.45
    assert Union([Integer(), Float()]).validate(1) == 1
    assert Union([Integer(), Float()]).validate(None) == None
    assert Union([Integer(), Float()]).validate([1,2,3]) == None
    assert Union([Integer(), Float()]).validate(1.45) != [1,2,3]
    assert Union([Integer(), Float()]).validate(1.45) != "hello"


# Generated at 2022-06-14 14:31:39.478256
# Unit test for method validate of class Object
def test_Object_validate():
    
    # case 1.
    properties = {"x": Integer()}
    object = Object(properties=properties)
    res = object.validate({"x": 1})
    
    print(res)
    
    # case 2.
    properties = {"x": Integer(allow_null=True)}
    object = Object(properties=properties)
    res = object.validate({"x": None})
    
    print(res)

    # case 3.
    properties = {"x": Integer()}
    object = Object(properties=properties)
    try:
        object.validate({"x": "1"})
    except ValidationError as ex:
        print(ex)

    # case 4.
    properties = {"x": Integer()}
    object = Object(properties=properties)

# Generated at 2022-06-14 14:31:40.893899
# Unit test for method validate of class Choice
def test_Choice_validate():
    text = "field"
    choices = ['city', 'state', 'country']
    result = Choice(text, choices)
    assert choices,result.choices


# Generated at 2022-06-14 14:31:52.847186
# Unit test for method validate of class Union
def test_Union_validate():
    import datetime
    from apistar import test
    from apistar.validators import validate
    from apistar.types import Type, String, Integer, Boolean, Number

    class Person(Type):
        name: String
        age: Integer

    class Vehicle(Type):
        name: String
        price: Number

    class Event(Type):
        name: String
        date_time: datetime.datetime
        capacity: Integer

    class Booking(Type):
        person: Person
        vehicle: Vehicle
        event: Union[Event, Vehicle]


# Generated at 2022-06-14 14:31:58.472773
# Unit test for method __or__ of class Field
def test_Field___or__():
    class LeftField(Field):
        def __init__(self):
            super().__init__(title='', description='', default= NO_DEFAULT, allow_null= True)

    class RightField(Field):
        def __init__(self):
            super().__init__(title='', description='',  default= NO_DEFAULT, allow_null= True)

    left = LeftField()
    right = RightField()
    union = left | right
    assert isinstance(union, Union)




# Generated at 2022-06-14 14:32:09.797605
# Unit test for method validate of class Array
def test_Array_validate():
    example = [1, 2, 3, 4]

# Generated at 2022-06-14 14:32:21.216533
# Unit test for method validate of class Boolean
def test_Boolean_validate():

    boolean_object = Boolean()

    # Test when input value is a strict boolean and allow_null is set to False
    # Expected result: value
    assert boolean_object.validate(value=True) == True
    assert boolean_object.validate(value=False) == False

    # Test when input value is a non-strict boolean
    # Expected result: value
    assert boolean_object.validate(value="True", strict=False) == True
    assert boolean_object.validate(value=None, strict=False) == None
    assert boolean_object.validate(value="", strict=False) == False

    # Test when input value is not a boolean and allow_null is set to True
    # Expected result: None
    boolean_object.allow_null = True
    assert boolean_object.validate(value=None)

# Generated at 2022-06-14 14:32:28.737576
# Unit test for method __or__ of class Field
def test_Field___or__():
    string_field = String(
        title="title", description="description", default="default"
    )
    number_field = Number(
        title="title", description="description", default=42
    )
    union_field = string_field | number_field
    assert isinstance(union_field, Union)
    any_of = union_field.any_of
    assert any_of[0] == string_field
    assert any_of[1] == number_field



# Generated at 2022-06-14 14:32:40.559020
# Unit test for constructor of class String
def test_String():
    # title, description and trim_whitespace should be right after construction
    a = String("title", "description", True )
    assert a.title == "title"
    assert a.description == "description"
    assert a.trim_whitespace == True

    # allow_blank, max_length should be right after construction
    b = String("title", "description", False, True, 10 )
    assert b.title == "title"
    assert b.description == "description"
    assert b.allow_blank == False
    assert b.max_length == 10


# test for function validate of class String

# Generated at 2022-06-14 14:32:51.431289
# Unit test for constructor of class Array
def test_Array():
    field = Array()
    assert field.items is None
    assert field.additional_items is False
    assert field.min_items is None
    assert field.max_items is None
    assert field.unique_items is False

    field = Array(items=String)
    assert field.items == String
    assert field.additional_items is False
    assert field.min_items is None
    assert field.max_items is None
    assert field.unique_items is False

    field = Array(items=[String, Boolean])
    assert field.items == [String, Boolean]
    assert field.additional_items is False
    assert field.min_items is None
    assert field.max_items is None
    assert field.unique_items is False

    field = Array(additional_items=True)
    assert field.items is None

# Generated at 2022-06-14 14:32:52.805064
# Unit test for method validate of class Choice
def test_Choice_validate():
    choice = Choice()
    print(choice.validate(None))


# Generated at 2022-06-14 14:33:06.141681
# Unit test for constructor of class Const
def test_Const():
    c = Const(const=7)
    assert c.const == 7
    assert c.validate(7) == 7
    assert c.get_error_text("const") == "Must be the value '7'."
    # Test that value is compared to const using '!='
    raises(ValidationError, c.validate, value=8)
    raises(ValidationError, c.validate, value=None)
    raises(ValidationError, c.validate, value="7")
    raises(ValidationError, c.validate, value=True)
    raises(ValidationError, c.validate, value=False)

    c = Const(const="7")
    assert c.const == "7"
    assert c.validate("7") == "7"

# Generated at 2022-06-14 14:33:07.976230
# Unit test for method validate of class Number
def test_Number_validate():
    n = Number(minimum=0)
    n.validate(0)

# Generated at 2022-06-14 14:33:19.651639
# Unit test for method validate of class Number
def test_Number_validate():
    num = Number()
    assert num.validate(2.3) == 2.3
    assert num.validate(2) == 2
    assert num.validate("2.3") == decimal.Decimal("2.3")
    assert num.validate("2") == 2
    assert num.validate(2.3) == 2.3
    assert num.validate("-2.3") == decimal.Decimal("-2.3")
    assert num.validate("-2") == -2
    assert num.validate("2.3a") == 2.3
    assert num.validate("a 2.3") == None
    assert num.validate(True) == None
    assert num.validate(False) == None
    assert num.validate(None) == None

