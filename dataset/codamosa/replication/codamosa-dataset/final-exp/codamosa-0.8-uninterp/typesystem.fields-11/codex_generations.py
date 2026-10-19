

# Generated at 2022-06-14 14:24:31.417897
# Unit test for method validate of class Array
def test_Array_validate():
    array = Array(items=String())
    assert array.validate([]) is True

# Generated at 2022-06-14 14:24:40.705182
# Unit test for method validate of class Choice
def test_Choice_validate():

    c = Choice(
        name="color",
        choices=[
            ("RED", "The color red."),
            ("GREEN", "The color green."),
            ("BLUE", "The color blue."),
        ],
        required=True,
    )
    assert c.get_error_text("required") == "This field is required."
    assert c.validate("RED") == "RED"
    assert c.validate("GREEN") == "GREEN"
    assert c.validate("BLUE") == "BLUE"
    with raises(ValidationError):
        c.validate("red")
    with raises(ValidationError):
        c.validate("")
    with raises(ValidationError):
        c.validate(None)


# Generated at 2022-06-14 14:24:47.533846
# Unit test for method serialize of class Array
def test_Array_serialize():
    array = Array(
        items=String(),
        additional_items=Boolean(),
        min_items=2,
        max_items=4,
    )
    obj = ['a', 'b', True, False, True]
    assert array.serialize(obj) == [
        'a', 'b', True, False, True
    ]

    pytest.raises(ValidationError, array.validate, [])
    pytest.raises(ValidationError, array.validate, obj[:3])
    pytest.raises(ValidationError, array.validate, obj[:5])
    array.validate(obj[:4])
    array.validate(['a', 'b', True, False])
    array.validate(obj)


# Generated at 2022-06-14 14:24:49.751193
# Unit test for method serialize of class String
def test_String_serialize():
    stringField = String(format = "time")
    output = stringField.serialize("12:56:00")
    assert output == "12:56:00"


# Generated at 2022-06-14 14:24:55.174158
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    field = Field(allow_null=True, description="Description", title="Field")
    field.default = "value"
    assert type(field) == Field
    assert field.has_default() == True
    assert field.get_default_value() == "value"
    assert field.validate("value") == "value"
    assert field.validate("") == "value"


# Generated at 2022-06-14 14:24:59.887258
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    class SubField(Field):
        def validate(self, value: typing.Any, *, strict: bool = False) -> typing.Any:
            return value
    f = SubField(default = 1)
    assert f.get_default_value() == 1

# Generated at 2022-06-14 14:25:08.543535
# Unit test for constructor of class Choice
def test_Choice():
    choice_list = [("one", "one"), ("two", "two"), ("three", "three")]
    choice = Choice(choices=choice_list)
    assert choice.validate("one") == "one"
    assert type(choice.validate("one")) == str
    assert choice.validate("two") == "two"
    assert type(choice.validate("two")) == str
    assert choice.validate("three") == "three"
    assert type(choice.validate("three")) == str
    try:
        choice.validate("four")
        assert False
    except ValidationError:
        pass
    assert choice.validate("") == None
    assert choice.validate("") == None



# Generated at 2022-06-14 14:25:11.121813
# Unit test for constructor of class Array
def test_Array():
    field = Array(items=String())
    assert field.items == String()
    assert field.allow_null is False
    assert field.default is None
    assert field.title is None
    assert field.description is None


# Generated at 2022-06-14 14:25:22.377423
# Unit test for method validate of class Choice
def test_Choice_validate():
    # Successfully call the validate method of class Choice
    choice_1 = Choice(choices=('A', 'B', 'C'))
    choice_2 = Choice(choices=[('A', 'a'), ('B', 'b'), ('C', 'c')])
    try:
        choice_1.validate('A')
        choice_2.validate('B')
        assert True
    except:
        assert False
    
    # Raises error in case of invalid choice value
    try:
        choice_1.validate('Z')
        choice_2.validate('z')
        assert False
    except:
        assert True

    # Raises error in case of invalid data type

# Generated at 2022-06-14 14:25:25.391311
# Unit test for method validate of class Union
def test_Union_validate():
    import json
    u=Union([Integer(default=5),Number(multiple_of=5)])
    unittest.TestCase().assertEqual( u.validate(5), 5)
    unittest.TestCase().assertEqual( u.validate(10), 10)
    unittest.TestCase().assertEqual( u.validate(15), 15)
    unittest.TestCase().assertEqual( u.validate(14), None)
    unittest.TestCase().assertEqual( str(u.validate(1)), '5')



# Generated at 2022-06-14 14:26:08.218788
# Unit test for method validate of class Array
def test_Array_validate():
    items = [Integer(),String()]
    items_class = type(items)

    # testing when items is not a list
    with pytest.raises(AssertionError):
        Array(items=items_class(items))

    # testing when additional_items is not a boolean or a Field
    with pytest.raises(AssertionError):
        Array(items = items, additional_items = items_class(items))

    # testing when min_items is not None or an integer
    with pytest.raises(AssertionError):
        Array(items = items, min_items = items_class(items))

    # testing when max_items is not None or an integer
    with pytest.raises(AssertionError):
        Array(items = items, max_items = items_class(items))

    # testing when

# Generated at 2022-06-14 14:26:13.084943
# Unit test for method __or__ of class Field
def test_Field___or__():
    a = Field(title="").validate(1)
    b = Field(title="").validate(2)
    assert isinstance((a | b), Union)
    assert (a | b).any_of == [a,b]
    c = Field(title="").validate(3)
    assert isinstance((a | (b | c)), Union)
    assert (a | (b | c)).any_of == [a,b,c]



# Generated at 2022-06-14 14:26:14.245034
# Unit test for constructor of class Const
def test_Const():
    with pytest.raises(TypeError):
        const = Const(const=0, allow_null=True)

## Field aliases



# Generated at 2022-06-14 14:26:25.459542
# Unit test for method validate of class Number
def test_Number_validate():
    n = Number()
    n.allow_null = True
    assert n.validate(None, strict=False) is None
    n1 = Number()
    n1.allow_null = False
    assert n1.validate(None, strict=False) is None
    n2 = Number()
    n2.allow_null = True
    assert n2.validate(None, strict=True) is None
    n3 = Number()
    n3.allow_null = True
    assert n3.validate(3, strict=True) == 3
    n4 = String()
    assert n4.validate("abc", strict=True) == "abc"
    n5 = Number()
    assert n5.validate(3, strict=True) == 3

# Generated at 2022-06-14 14:26:27.464277
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    test_field = Field()
    test_field.default = 1
    assert test_field.get_default_value() == 1

# Generated at 2022-06-14 14:26:31.600125
# Unit test for constructor of class Const
def test_Const():
    with pytest.raises(AssertionError):
        Const(const=1, allow_null=True)



# Generated at 2022-06-14 14:26:36.002846
# Unit test for constructor of class Array
def test_Array():
    Array(min_items=1)
    Array(['string'])
    Array([String()])
    Array(items=String(min_length=1))
    Array(items=[String(min_length=1)])
    Array(items=[String(min_length=1), String(min_length=2)])

# Generated at 2022-06-14 14:26:37.881384
# Unit test for method __or__ of class Field
def test_Field___or__():
    import typesystem
    assert not hasattr(typesystem.base.Field,'__or__')


# Generated at 2022-06-14 14:26:42.479052
# Unit test for constructor of class Const
def test_Const():
    from pytest import raises
    const1 = Const(5)
    assert const1.const == 5
    with raises(AssertionError):
        const1 = Const(5, allow_null=True)
    const2 = Const(10)
    assert const2.const == 10
    assert const1.const != const2.const

# Unit tests for method validate of class Const

# Generated at 2022-06-14 14:26:50.059275
# Unit test for constructor of class String
def test_String():
    with pytest.raises(AssertionError):
        String(title = {}, description = '', default = None, allow_null = False)

    with pytest.raises(AssertionError):
        String(title = '', description = [], default = None, allow_null = False)

    with pytest.raises(AssertionError):
        String(title = '', description = '', default = [], allow_null = False)

    with pytest.raises(AssertionError):
        String(title = '', description = '', default = None, allow_null = 'no_null')

    with pytest.raises(AssertionError):
        String(title = '', description = '', default = None, allow_null = False, allow_blank = 'not_blank')


# Generated at 2022-06-14 14:27:10.190437
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    field = Field(default=None)
    assert field.get_default_value() == None
    field = Field(default=False)
    assert field.get_default_value() == False
    field = Field(default=1)
    assert field.get_default_value() == 1
    field = Field(default="Hello")
    assert field.get_default_value() == "Hello"

test_Field_get_default_value()

# Generated at 2022-06-14 14:27:11.396941
# Unit test for method validate of class Choice
def test_Choice_validate():
    obj1=Choice()
    assert obj1.validate("a") == "a"
    assert obj1.validate("") == None



# Generated at 2022-06-14 14:27:20.669618
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    field = Field()
    assert getattr(field,'default',None) == None
    assert field.get_default_value() == None
    field = Field (default='test')
    assert getattr(field,'default','no default') == 'test'
    assert field.get_default_value() == 'test'
    field = Field (default=[1,2,3])
    assert getattr(field,'default',None) == [1,2,3]
    assert field.get_default_value() == [1,2,3]
    field = Field (default=3+3)
    assert getattr(field,'default',None) == 6
    assert field.get_default_value() == 6


# Generated at 2022-06-14 14:27:29.552129
# Unit test for method validate of class Array
def test_Array_validate():
    field = Array(items=Integer())
    value = None
    strict = False
    result = field.validate(value, strict=strict)
    assert result is None
    value = None
    strict = True
    with pytest.raises(ValidationError) as excinfo:
        field.validate(value, strict=strict)
    with pytest.raises(ValidationError) as excinfo:
        field.validate(3.14, strict=strict)
    result = field.validate([1, 2, 3])
    assert result == [1, 2, 3]
    result = field.validate(["1", "2", "3"])
    assert result == [1, 2, 3]
    result = field.validate([1, 2, "x"])

# Generated at 2022-06-14 14:27:31.524622
# Unit test for constructor of class String
def test_String():
    string = String(title="test")
    assert "test" == string.title


# Generated at 2022-06-14 14:27:41.514332
# Unit test for method validate of class Object
def test_Object_validate():
    field=Object(
        properties={
            "a":Number(allow_null=True),
            "b":String(allow_null=True),
            "c":Number(allow_null=True, required=True)
        },
        additional_properties=Number(allow_null=True),
        allow_null=True,
        required=True
    )
    print(field.validate({"b":"", "c":None}))
    print(field.validate({"d":1, "b":"", "c":None}))
    print(field.validate({"b":1, "c":None}))
    print(field.validate({"b":"", "c":1, "e":1}))
    print(field.validate(None))

test_Object_validate()


# Generated at 2022-06-14 14:27:49.624247
# Unit test for method validate of class Object
def test_Object_validate():
    obj = Object()

    # Test for null return
    assert obj.validate(None) == None

    # Test for null raise error
    obj = Object(allow_null = False)
    with pytest.raises(ValidationError):
        obj.validate(None)

    # Test for empty raise error
    obj = Object(allow_empty = False)
    with pytest.raises(ValidationError):
        obj.validate({})
    
    # Test for empty return
    obj = Object(allow_empty = True)
    assert obj.validate({}) == {}

    # Test for str raise error
    obj = Object()
    with pytest.raises(ValidationError):
        obj.validate("test")

    obj = Object()
    with pytest.raises(ValidationError):
        obj.valid

# Generated at 2022-06-14 14:27:53.991136
# Unit test for method __or__ of class Field
def test_Field___or__():
    # initialize test object
    func1 = Function(num_args=10)
    func2 = Function(num_args=10)
    # and test it
    assert (func1 | func2).any_of == [func1, func2]



# Generated at 2022-06-14 14:27:58.216929
# Unit test for method __or__ of class Field
def test_Field___or__():
    # TODO: Use unittest module
    field1 = String()
    field2 = Number()
    union_filed = field1 | field2
    assert Union.__name__ == field1.__or__(field2).__class__.__name__


# Generated at 2022-06-14 14:28:01.588375
# Unit test for method validate of class Choice
def test_Choice_validate():
    s = Choice(choices = [("foo", "bar")])
    assert s.validate("foo") == "foo"
    assert s.validate("bar") == "foo"
    assert s.validate("baz") == "foo"



# Generated at 2022-06-14 14:28:12.682028
# Unit test for method validate of class Union
def test_Union_validate():
    # test validate for a field with the only Union field
    field = Union([Date()], default="unknown")
    value = "2015-09-26"
    expected = "2015-09-26"
    assert field.validate(value) == expected

    # test validate for a field with the only Union field
    field = Union([Date()])
    value = "unknown"
    expected = ValidationError(
        messages=[Message(code='union', text='Did not match any valid type.', path=[])]
    )
    assert field.validate(value) == expected



# Generated at 2022-06-14 14:28:24.944640
# Unit test for method validate of class Choice
def test_Choice_validate():
    choice_field = Choice(choices = ['yes', 'no'], required=False)
    assert choice_field.validate("yes") == "yes"
    assert choice_field.validate("no") == "no"
    assert choice_field.validate("no yes") == "no yes"
    assert choice_field.validate("") == None
    assert choice_field.validate("True") == "True"
    assert choice_field.validate("no", strict=True) == "no"
    assert choice_field.validate("yes no") == "yes no"
    # Test with setting allow_null to True
    choice_field = Choice(choices = ['yes', 'no'], allow_null = True, required=False)
    assert choice_field.validate("yes") == "yes"
    assert choice_field

# Generated at 2022-06-14 14:28:37.027950
# Unit test for method validate of class Object
def test_Object_validate():
    from typing import Dict
    from simplevalidate import String, Object

    field = Object(properties={'last_name': String(required=True)})
    try:
        field.validate({'first_name': 'John', 'last_name': 'Smith'})
    except Exception as e:
        print(e)
        assert False

    try:
        field.validate({'first_name': 'John'})
    except Exception as e:
        print(e)
        assert True

    try:
        field.validate({'first_name': 'John', 'last_name': 12})
    except Exception as e:
        print(e)
        assert True

    # Ensure all property keys are strings.

# Generated at 2022-06-14 14:28:48.540454
# Unit test for method validate of class Object
def test_Object_validate():
    field = Object()
    value = {}
    strict = False
    # Nullable
    try:
        assert field.validate(None, strict=strict) is None
    except ValidationError as e:
        e.full_messages()
        print(e)
        assert False
    # Not nullable
    field = Object(allow_null=False)
    try:
        assert field.validate(None, strict=strict) is None
    except ValidationError as e:
        e.full_messages()
        assert True
    # Valid type
    value = {}
    try:
        field.validate(value, strict=strict)
        assert True
    except ValidationError as e:
        e.full_messages()
        assert False
    # Valid type
    value = {"a":1}


# Generated at 2022-06-14 14:28:54.362284
# Unit test for method validate of class Choice
def test_Choice_validate():
    choices=[('foo', 'foo'), ('bar', 'bar')]
    choicecast=Choice(choices=choices)
    assert choicecast.validate('foo') == 'foo'
    assert choicecast.validate('bar') == 'bar'
    with pytest.raises(ValidationError) as error:
        choicecast.validate('baz')



# Generated at 2022-06-14 14:29:01.072674
# Unit test for method validate of class Choice
def test_Choice_validate():
    choice = Choice(
        choices=[("red", "Red"), ("green", "Green")]
    )
    assert choice.validate("red") == "red"
    assert choice.validate("green") == "green"
    with pytest.raises(ValidationError):
        choice.validate("blue")
    with pytest.raises(ValidationError):
        choice.validate("")



# Generated at 2022-06-14 14:29:04.540368
# Unit test for method validate of class Object
def test_Object_validate():
    properties = {'name': Field(allow_null=True)}
    obj = Object(properties=properties, allow_null=True) 
    
    #Run the function to test
    obj.validate(None)


# Generated at 2022-06-14 14:29:06.096404
# Unit test for method __or__ of class Field
def test_Field___or__():
    assert isinstance(Field() | Field(), Union)


# Generated at 2022-06-14 14:29:08.044549
# Unit test for method validate of class Choice
def test_Choice_validate():
    field = Text()
    print ("Test Choice_validate")
    assert field.validate("")



# Generated at 2022-06-14 14:29:12.776933
# Unit test for method validate of class Choice
def test_Choice_validate():
    assert Choice(choices=[1,2,3]).validate(1) == 1
    assert Choice(choices=[1,2,3]).validate(4) == 4
    assert Choice(choices=[1,2,3], allow_null = True).validate(1) == 1
    assert Choice(choices=[1,2,3], allow_null = True).validate(None) == None
    assert Choice(choices=[1,2,3], allow_null = True).validate(5) == 5



# Generated at 2022-06-14 14:29:31.105796
# Unit test for method validate of class Choice
def test_Choice_validate():
    #test case 1
    choice = Choice(choices=['1','2'])
    value1 = choice.validate('1')
    value2 = choice.validate('2')
    assert value1 == '1'
    assert value2 == '2'
    # test case 2
    value3 = choice.validate('3')
    assert value3 == '3'
    # test case 3
    value4 = choice.validate('1',strict = True)
    assert value4 == '1'

# Generated at 2022-06-14 14:29:34.087371
# Unit test for method validate of class Boolean
def test_Boolean_validate():
	B = Boolean()
	assert B.validate('true') == True
	assert B.validate('1') == True
	assert B.validate('0') == False
	assert B.validate(1) == True
	assert B.validate(0) == False
	return True

# Generated at 2022-06-14 14:29:44.108088
# Unit test for method validate of class Union
def test_Union_validate():
    class C(Field): pass
    f1 = C(errors={"a" : "b"})
    f2 = C(errors={"c" : "d"})
    f3 = C(errors={"e" : "f"})
    g = Union([f1, f2, f3])

    # union: Did not match any valid type
    with pytest.raises(ValidationError) as excinfo:
        g.validate(4)
    assert len(excinfo.value.messages()) == 1
    assert excinfo.value.messages()[0].code == 'union'

    with pytest.raises(ValidationError) as excinfo:
        f1.validate_or_error(4)
    assert len(excinfo.value.messages()) == 1
    assert excinfo.value.mess

# Generated at 2022-06-14 14:29:56.516292
# Unit test for constructor of class String
def test_String(): 
    sample1 = String(title='sample',description='sample',default='sample')
    # assert sample1.title == 'sample'
    # assert sample1.description == 'sample'
    # assert sample1.default == 'sample'
    assert type(sample1.default) == str
    assert sample1.allow_null == False
    assert sample1.allow_blank == False
    assert sample1.trim_whitespace == True
    assert sample1.max_length == None
    assert sample1.min_length == None
    assert sample1.pattern == None
    assert sample1.format == None

# Generated at 2022-06-14 14:30:00.194445
# Unit test for method validate of class Object
def test_Object_validate():
    field = Object()
    assert field.validate(None) is None
    assert field.validate({'1': '1'}) == {'1': '1'}
    with pytest.raises(ValidationError):
        field.validate('')
    with pytest.raises(ValidationError):
        field.validate('1')
    with pytest.raises(ValidationError):
        field.validate([1])
    with pytest.raises(ValidationError):
        field.validate(1)
    with pytest.raises(ValidationError):
        field.validate(Object())


# Generated at 2022-06-14 14:30:04.782223
# Unit test for method __or__ of class Field
def test_Field___or__():
    assert Field() | Field() == Union(any_of = [Field(), Field()])
    assert Field() | Union(any_of = [Field()]) == Union(any_of = [Field(), Field()])


FINAL = Ellipsis

# Generated at 2022-06-14 14:30:13.992360
# Unit test for method validate of class Boolean
def test_Boolean_validate():
    assert True == Boolean().validate("true")
    assert True == Boolean().validate("1")
    assert False == Boolean().validate("False")
    assert False == Boolean().validate("0")
    assert False == Boolean().validate("")
    assert False == Boolean(allow_null=True).validate("")
    assert None == Boolean(allow_null=True).validate("")
    assert None == Boolean(allow_null=True).validate("null")
    assert "You must provide a value of true or false." == Boolean().validate("bad input")



# Generated at 2022-06-14 14:30:25.028893
# Unit test for method validate of class Array
def test_Array_validate():
    s = Array()
    f = s.validate
    with pytest.raises(ValidationError) as e_info:
        f([1, 2, 3, 4, 5], strict=True)
    with pytest.raises(ValidationError) as e_info:
        f([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], strict=True)
    with pytest.raises(ValidationError) as e_info:
        f(None, strict=True)
    assert f([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert f([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Generated at 2022-06-14 14:30:30.351442
# Unit test for method validate of class Choice
def test_Choice_validate():
    c=Choice(choices=["Europe","Asia","Africa","North America","South America","Australia","Antarctica"])
    assert c.validate("Europe")=="Europe"
    assert c.validate(["Europe","Asia","Africa","North America","South America","Australia","Antarctica"])=="Europe"
    assert c.validate([])=="Europe"
    assert c.validate(None) is None
    assert c.validate(1)=="Europe"

# Generated at 2022-06-14 14:30:36.915611
# Unit test for method __or__ of class Field
def test_Field___or__():
    assert (String() | Integer()) == (Integer() | String())
    assert (String() | Integer() | Float()) == (Integer() | Float() | String())
    assert (String() | Integer() | Float()) != (Integer() | String())
    assert (String() | Integer() | Float()) != (Integer() | Float())
    assert (String() | Integer() | Float()) != (Integer() | Float() | Decimal())


# Generated at 2022-06-14 14:30:56.738939
# Unit test for method validate of class Choice
def test_Choice_validate():
    field=Choice(choices=None, error_text_prefix="error_")
    assert field.validate(value=None, strict=False)==None

# Generated at 2022-06-14 14:31:07.625102
# Unit test for method validate of class Object
def test_Object_validate():
    my_object = {
        "key1": ["value1", "value2"],
        "key2": "value2"
    }

    my_schema = {
        "_schema": "object",
        "properties": {
            "key1": {
                "_schema": "array",
                "items": {
                    "_schema": "string"
                }
            },
            "key2": {
                "_schema": "string",
                "max_length": 100
            }
        },
        "additional_properties": False
    }

    r = json_schema(my_schema).validate(my_object)
    assert r == {
        "key1": ["value1", "value2"],
        "key2": "value2"
    }


# Generated at 2022-06-14 14:31:09.546558
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    with pytest.raises(TypeError):
        Field.get_default_value()

# Generated at 2022-06-14 14:31:16.965987
# Unit test for constructor of class Const
def test_Const():
    # test null case
    const_null = Const(None, description="this is a null value")
    try:
        const_null.validate(True)
    except ValidationError as error:
        assert error.code == "only_null"
        assert error.index == []

    # test non null case
    const_non_null = Const(False, description="this is a non null value")
    try:
        const_non_null.validate(True)
    except ValidationError as error:
        assert error.code == "const"
        assert error.index == []
        assert error.text == "Must be the value 'False'."


# Generated at 2022-06-14 14:31:21.811043
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    assert Field().get_default_value() == None
    assert Field(description="this is a description").description == "this is a description"
    assert Field(description="this is a description", default="default").get_default_value() == "default"
test_Field_get_default_value()


# Generated at 2022-06-14 14:31:28.791797
# Unit test for constructor of class String
def test_String():
    assert String()
    assert String(description="wow")
    assert String(title="wow")
    assert String(allow_blank=True)
    assert String(allow_null=True)
    assert String(trim_whitespace=False)
    assert String(max_length=5)
    assert String(min_length=5)
    assert String(pattern=r'\w+')
    assert String(format="date")
    assert String(format="time")
    assert String(format="datetime")
    assert String(format="uuid")


# Generated at 2022-06-14 14:31:30.813374
# Unit test for method validate of class String
def test_String_validate():
    field=String()
    assert field.validate("hello")=="hello"

# Generated at 2022-06-14 14:31:33.730477
# Unit test for method validate of class Choice
def test_Choice_validate():
    field = Choice(choices=["B", "C", "D"])
    assert field.validate("B") == "B"
    assert field.validate("C") == "C"
    assert field.validate("D") == "D"
    assert field.validate("A") == "A"
    assert field.validate("") == ""


# Generated at 2022-06-14 14:31:39.091016
# Unit test for method validate of class Choice
def test_Choice_validate():
    choice_field=Choice(choices=["a", "b"])
    valid=choice_field.validate("a")
    assert valid=="a"
    # test when value doesn't belong in choices
    with pytest.raises(ValidationError):
        choice_field.validate("c")
    # test when value is blank and this field is required
    with pytest.raises(ValidationError):
        choice_field.validate("")
    # test when value is blank and this field is not required
    choice_field=Choice(choices=["a", "b"], allow_null=True)
    valid=choice_field.validate("")
    assert valid is None


# Generated at 2022-06-14 14:31:45.518904
# Unit test for method validate of class String
def test_String_validate():
    # input for first test
    title1 = "dsf"
    description1 = "dsf"
    default1 = "dshjf"
    allow_blank1 = True
    trim_whitespace1 = True
    max_length1 = 4
    min_length1 = 1
    pattern1 = None
    format1 = None
    strict1 = False
    value1 = "hjf"
    # creating object
    obj = String(title = title1, description = description1, default = default1, allow_blank = allow_blank1, trim_whitespace = trim_whitespace1,
                 max_length = max_length1, min_length = min_length1, pattern = pattern1, format = format1)
    assert obj.validate(value1, strict = strict1) == value1
    # input for

# Generated at 2022-06-14 14:31:56.678769
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    assert Field(title="", description="", default=1, allow_null=False).get_default_value() == 1
    assert Field(title="", description="", allow_null=False).get_default_value() == NO_DEFAULT
    assert Field(title="", description="", allow_null=True).get_default_value() == None


# Generated at 2022-06-14 14:31:57.795473
# Unit test for constructor of class Const
def test_Const():
    assert Const(const=None, allow_null=True, strict=False).const == None


# Generated at 2022-06-14 14:32:04.927222
# Unit test for method validate of class Choice
def test_Choice_validate():
    #test to see if value is in choices--from unit test test_Choice_validate_no_error
    choice_valid_value= Choice(choices=[("name1","label1"), ("name2","label2")])
    assert choice_valid_value.validate('name1') == 'name1'
    #test to see if value is blank
    assert choice_valid_value.validate('') == None



# Generated at 2022-06-14 14:32:07.221063
# Unit test for method validate of class Choice
def test_Choice_validate():
    choice = Choice(choices=[('a','b')])
    assert choice.validate('b') == 'b'
    assert choice.validate('a') == 'b'
    assert choice.validate(1) == 'b'
    pytest.raises(ValidationError, choice.validate, None)
    pytest.raises(ValidationError, choice.validate, 'c')



# Generated at 2022-06-14 14:32:17.754714
# Unit test for method validate of class Number
def test_Number_validate():
    _test_Number_validate_type_0(197, True)

    _test_Number_validate_type_1(65, True)

    _test_Number_validate_type_2(160, True)

    _test_Number_validate_type_3(82, True)

    _test_Number_validate_type_4(128, True)

    _test_Number_validate_type_5(113, True)

    _test_Number_validate_type_6(95, True)

    _test_Number_validate_type_7(90.66, True)

    _test_Number_validate_type_8(106.63, True)

    _test_Number_validate_type_9(45.82, True)


# Generated at 2022-06-14 14:32:18.417472
# Unit test for method validate of class Object
def test_Object_validate():
    pass
    #todo




# Generated at 2022-06-14 14:32:28.679493
# Unit test for method validate of class Choice
def test_Choice_validate():
    # Test case 1: default case
    c1 = Choice(allow_null=True, choices=['yes', 'no'])
    ret1 = c1.validate('no')
    assert ret1 == 'no'
    # Test case 2: allow_null
    c2 = Choice(allow_null=True, choices=['yes', 'no'])
    ret2 = c2.validate(None)
    assert ret2 == None
    # Test case 3: not allow_null
    c3 = Choice(allow_null=False, choices=['yes', 'no'])
    with pytest.raises(ValidationError) as exc_info:
        c3.validate(None)
    ret3 = exc_info.value
    assert ret3.code == 'null'

# Generated at 2022-06-14 14:32:35.200268
# Unit test for method validate of class Choice
def test_Choice_validate():
    class Test:
        pass
    
    assert Choice(choices=None, label=None, default=None).validate("test") == "test"
    assert Choice(choices=None, label=None, default=None).validate("") == None
    assert Choice(choices=None, label=None, default=None).validate("not_in_choices") == None
    assert Choice(choices=None, label=None, default=None).validate(Test()) == None


# Generated at 2022-06-14 14:32:41.762182
# Unit test for constructor of class Const
def test_Const():
    Const(True)
    Const(const=True)
    Const(True, default=False)
    Const(const=True, default=False)
    Const(True, title="True value")
    Const(const=True, title="True value")
    Const(True, description="True description")
    Const(const=True, description="True description")
    Const(True, examples=[True])
    Const(const=True, examples=[True])


# Expose these classes in the top-level package namespace.

# Generated at 2022-06-14 14:32:43.378000
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    assert Field().get_default_value() == NO_DEFAULT


# Generated at 2022-06-14 14:32:51.132046
# Unit test for method validate of class Object
def test_Object_validate():
  object=Object()
  object.validate(a)
 


# Generated at 2022-06-14 14:33:04.405792
# Unit test for constructor of class Array
def test_Array():
    # Test case 1:
    field1 = Array()
    assert type(field1.items) is None
    assert type(field1.additional_items) is bool
    assert field1.additional_items == False
    assert type(field1.max_items) is None
    assert type(field1.min_items) is None
    assert type(field1.unique_items) is bool
    assert field1.unique_items == False
    assert field1.allow_null == True
    assert field1.has_default() == False

    # Test case 2
    field2 = Array(max_items = 3)
    assert type(field2.items) is None
    assert type(field2.additional_items) is bool
    assert field2.additional_items == False

# Generated at 2022-06-14 14:33:06.450655
# Unit test for method validate of class Number
def test_Number_validate():
    assert Number.validate(2) == 2
# end unit test for method validate of class Number


# Generated at 2022-06-14 14:33:18.489994
# Unit test for method validate of class Array
def test_Array_validate():
    items = [String(max_length=2), Number, Number]
    array = Array(items=items, min_items=3, max_items=3)
    
    value = [1, 2, 'abc', 'ab']
    array.validate(value)
    assert False, 'Expected to throw an exception because of extra elements in list'

# Generated at 2022-06-14 14:33:21.303238
# Unit test for method validate of class Choice
def test_Choice_validate():
    c=Choice(allow_null=True,choices=["1","2","3"])
    assert c.validate("1")=="1"
    assert c.validate("2")=="2"
    assert c.validate("3")=="3"
    with raises(ValidationError):
        assert c.validate("4")
    assert c.validate("")==None

