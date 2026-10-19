

# Generated at 2022-06-14 14:24:56.980456
# Unit test for method validate of class Array
def test_Array_validate():
    name = String()
    age = Integer()
    items = [name, age]
    field = Array(items=items)
    field.validate([])

if __name__=="__main__":
    test_Array_validate()

# Generated at 2022-06-14 14:25:01.281131
# Unit test for constructor of class Choice
def test_Choice():
    choices =[(1, 2), (3, 4), (5, 6)]
    choice = Choice(choices=choices)
    assert choice.allow_null == False
    assert choice.choices == [(1, 2), (3, 4), (5, 6)]


# Generated at 2022-06-14 14:25:06.200288
# Unit test for method validate of class Choice
def test_Choice_validate():
    q = Choice(
    choices=[1, 2, 3, 4, 5]
    )
    assert q.validate(2) == 2
    assert q.validate(10) == 10
    assert q.validate('') == ''
    assert q.validate(None) == None


# Generated at 2022-06-14 14:25:13.427130
# Unit test for method validate of class Choice
def test_Choice_validate():
    with pytest.raises(ValidationError):
        Choice(allow_null=False).validate(None)
    with pytest.raises(ValidationError):
        Choice().validate("foo")
    assert Choice().validate("") is None
    assert Choice(choices=[]).validate("") is None
    assert Choice(choices=[("1", "one"), None]).validate("1") == "1"
    assert Choice(choices=["1", "2"]).validate(1) == 1



# Generated at 2022-06-14 14:25:24.379816
# Unit test for method __or__ of class Field
def test_Field___or__():
    pass

    # some tests
    import typing
    import datetime
    from typesystem import Schema, fields, types

    # test_field_arity
    assert (fields.String() | fields.Integer())

    # test_field_multiple_inheritance
    class Address(fields.Schema):
        street = fields.String()
        number = fields.Integer()


    class Person(fields.Schema):
        name = fields.String()
        age = fields.Integer()
        address = fields.Schema(Address)


    class Employee(fields.Schema):
        code = fields.String()
        rating = fields.Integer()


    class PersonOrEmployee(fields.Schema):
        name = fields.String()
        age = fields.Integer()
        address = fields.Schema(Address)

# Generated at 2022-06-14 14:25:26.047817
# Unit test for method validate of class Array
def test_Array_validate():
    model = Array(items=List(items=Model(properties={})))
    model.validate(['[1,2,3,4]'])


# Generated at 2022-06-14 14:25:35.306166
# Unit test for method serialize of class Array
def test_Array_serialize():
    items = [
        Boolean(),
        String(max_length=3),
        String(max_length=4),
        String(max_length=5),
        String(max_length=6),
        String(max_length=7),
    ]
    schema = Array(items=items)

    input_obj = [True, "123", "1234", "12345", "123456", "1234567"]
    actual_value = schema.serialize(input_obj)

    assert actual_value == input_obj

    schema = Array(items=String)
    input_obj = ["1", "2", "3"]
    actual_value = schema.serialize(input_obj)

    assert actual_value == input_obj

# Generated at 2022-06-14 14:25:47.482152
# Unit test for method validate of class Array
def test_Array_validate():
    my_array = Array(items=Integer())
    # [5, 6, 13] passed
    print(my_array.validate([5, 6, 13]))
    # ['5', 6, 13] failed
    print(my_array.validate(['5', 6, 13]))
    # [5, 6, '13'] failed
    print(my_array.validate([5, 6, '13']))
    # [5, 6.0, 13] passed
    print(my_array.validate([5, 6.0, 13]))
    # [5, 6.3, 13] failed
    print(my_array.validate([5, 6.3, 13]))
    # [5, 6, 13, 14] passed

# Generated at 2022-06-14 14:25:58.978158
# Unit test for method validate of class Array
def test_Array_validate():
  DUNS_LIST = ["duns_number", "duns_number_4", "duns_number_2"]
  DUNS_TYPE_LIST = [String, String, String]
  DUNS = {k:v for k, v in zip(DUNS_LIST, DUNS_TYPE_LIST)}

# Generated at 2022-06-14 14:26:04.878571
# Unit test for method serialize of class Array
def test_Array_serialize():
    try:
        assert Array().serialize([1, 2, 3]) == [1, 2, 3]
        assert Array(items=Field()).serialize([1, 2, 3]) == [1, 2, 3]
        assert Array(items=[Field(), Field(), Field()]).serialize([1, 2, 3]) == [1, 2, 3]
        assert Array(items=Field()).serialize(None) is None
        assert Array(items=[Field(), Field(), Field()]).serialize(None) is None
    except Exception as error:
        print("test_Array_serialize():", error)

# Generated at 2022-06-14 14:26:30.267241
# Unit test for method validate of class Number
def test_Number_validate():
    field1 = Number(title= 'number', minimum=5, exclusive_minimum=5, maximum=10, exclusive_maximum=10, precision='1.1')
    assert field1.validate(value= 5.1, strict=False) == 5.1
    assert field1.validate(value= 5, strict=False) == 5
    assert field1.validate(value= '5.1', strict=False) == 5.1
    assert field1.validate(value= '5', strict=False) == 5
    assert field1.validate(value= 11.1, strict=False) != 11.1
    assert field1.validate(value= 11, strict=False) != 11
    assert field1.validate(value= '11.1', strict=False) != 11.1

# Generated at 2022-06-14 14:26:34.559238
# Unit test for method __or__ of class Field
def test_Field___or__():
    err = "All methods passed in must be Field objects"
    with pytest.raises(TypeError, match=err):
        Field().__or__(42)

    with pytest.raises(TypeError, match=err):
        Field().__or__(NotImplemented)

    with pytest.raises(TypeError, match=err):
        Field().__or__(None)

    with pytest.raises(TypeError, match=err):
        Field().__or__(object())

    with pytest.raises(TypeError, match=err):
        Field().__or__(lambda x: x)



# Generated at 2022-06-14 14:26:37.105333
# Unit test for method serialize of class String
def test_String_serialize():
    s = String(title="S", description="S is a test case for serialization.", default="")
    assert s.serialize(None) == ""


# Generated at 2022-06-14 14:26:39.625121
# Unit test for method serialize of class String
def test_String_serialize():
    print('test_String_serialize')
    s = String(format='date')
    print(s.serialize(datetime.datetime.now()))


# Generated at 2022-06-14 14:26:49.363810
# Unit test for method validate of class Union
def test_Union_validate():
    #test for method validate
    from pydantic import ValidationError, BaseModel
    from typing import Any

    class User(BaseModel):
        name: str
        age: int
        #cannot throw ValidationError for the constructor of Address,
        #so use schema_extra = False
        address: Any
        class Config:
            schema_extra = False
    class Address(BaseModel):
        city: str
        street: str


# Generated at 2022-06-14 14:26:53.341642
# Unit test for method serialize of class String
def test_String_serialize():
    s = String(format='date')
    if s.serialize('2018-01-01') != '2018-01-01':
        return False
    return True



# Generated at 2022-06-14 14:26:59.417168
# Unit test for method serialize of class String
def test_String_serialize():
    assert String(format='date').serialize(None) == None
    assert String(format='date').serialize('2019-09-05') == '2019-09-05'
    assert String(format='time').serialize('12:30:00') == '12:30:00'
    assert String(format='datetime').serialize('2019-09-05T12:30:00') == '2019-09-05T12:30:00'


# Generated at 2022-06-14 14:27:12.328567
# Unit test for method validate of class Boolean
def test_Boolean_validate():
    key = Boolean()
    assert key.validate(None) is None
    assert key.validate(True) is True
    assert key.validate(False) is False
    assert key.validate(1) is True
    assert key.validate(0) is False
    assert key.validate('true') is True
    assert key.validate('false') is False
    assert key.validate('on') is True
    assert key.validate('off') is False
    assert key.validate('') is False
    with pytest.raises(ValidationError) as e:
        key.validate('yes')
    assert e.value.code == 'type'
    assert e.value.text == "Must be a boolean."
    with pytest.raises(ValidationError) as e:
        key.validate

# Generated at 2022-06-14 14:27:13.334267
# Unit test for constructor of class Choice
def test_Choice():
    # nothing
    assert True



# Generated at 2022-06-14 14:27:15.918140
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    d = decimal.Decimal(17.5)
    class MyField(Field):
        default = d
    f = MyField()
    return f.get_default_value()


# Generated at 2022-06-14 14:27:38.656955
# Unit test for method validate of class Array
def test_Array_validate():
    src = [0, 1, 2, 3]
    schema = Array(items=Integer(), min_items=2, max_items=3)
    # Get the value that the method validate returns
    value = schema.validate(src)
    assert value == [0, 1, 2]
    with raises(ValidationError):
        schema.validate(src, strict=True)



# Generated at 2022-06-14 14:27:48.086509
# Unit test for method validate of class Array
def test_Array_validate():
    from typing import List, Union

    from marshmallow import fields

    from aiida_jsonforms import easy_schema

    int_field = easy_schema.Integer(minimum=0, maximum=10)
    str_field = easy_schema.String()

    class SomeClass(easy_schema.EasySchema):
        ints: List[int] = easy_schema.Array(items=int_field, min_items=1, max_items=3)
        strs: List[str] = easy_schema.Array(items=str_field, min_items=2, max_items=5)
        ints_and_strs: List[Union[int, str]] = easy_schema.Array(
            items=[int_field, str_field], min_items=2, max_items=5
        )

# Generated at 2022-06-14 14:27:54.219016
# Unit test for method validate of class Union
def test_Union_validate():
    e = Union([Int(), String()])
    assert e.validate(1) == 1
    assert e.validate("a") == "a"
    with pytest.raises(ValidationError):
        e.validate(True)
    with pytest.raises(ValidationError):
        e.validate(None)



# Generated at 2022-06-14 14:27:57.628221
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    f = Field(default = 5)
    assert f.get_default_value() == 5
    assert not f.has_default()
    assert f.validate_or_error(5).value == 5

# Generated at 2022-06-14 14:28:01.367989
# Unit test for method validate of class Object
def test_Object_validate():
    field1 = String(title = "TestName", description = "Test the name")
    field2 = Number(title = "TestNumber", description = "Test the number")
    assert type(field1) == String
    assert type(field2) == Number
    test_object = {
        "name": "Norman",
        "number": 12345678,
        "address": "TestAddress"
    }
    test_properties = {
        "name": field1,
        "number": field2
    }
    object_test = Object(properties = test_properties)
    object_test.validate(test_object)
    return True


# Generated at 2022-06-14 14:28:04.763328
# Unit test for method validate of class Choice
def test_Choice_validate():
    target = Choice(choices=[("a", "A"),("b", "B")])
    assert "null" == target.validate("null")

    target = Choice(choices=[("a", "A"),("b", "B"), ("c", "C")])
    assert "c" == target.validate("c")

    with pytest.raises(ValidationError) as e:
        target = Choice(choices=[("a", "A"),("b", "B"), ("c", "C")])
        target.validate("d")

# Generated at 2022-06-14 14:28:11.893958
# Unit test for method validate of class Object
def test_Object_validate():
    class MySchema(Schema):
        result = Boolean()

    obj = Object(properties={"result": MySchema()})
    obj.validate({"result": False, "invalid_key": "value"})
    try:
        obj.validate({"result": "value"})
    except ValidationError as e:
        assert e.messages()[0].text == "Must be a boolean."
        assert e.messages()[0].index == ["result"]
    try:
        obj.validate({"invalid_key": "value"})
    except ValidationError as e:
        assert "not in" in e.messages()[0].text
        assert e.messages()[0].index == ["invalid_key"]


# Generated at 2022-06-14 14:28:18.978836
# Unit test for method __or__ of class Field
def test_Field___or__():
    # Test case 1:
    integer = Integer()
    string = String()
    any_of = integer.__or__(string)
    try:
        assert isinstance(any_of, Union)
        assert any_of.any_of[0] == integer
        assert any_of.any_of[1] == string
        print("Test case 1 passed!")
    except Exception as e:
        print(e)
        print("Test case 1 failed!")
    # Test case 2:
    integer = Integer()
    any_of = integer.__or__(None)

# Generated at 2022-06-14 14:28:23.418440
# Unit test for method validate of class String
def test_String_validate():
    field1 = String()
    val1 = field1.validate("123")
    assert "123" == val1

    field2 = String(allow_blank=True)
    val2 = field2.validate("")
    assert "" == val2

# Generated at 2022-06-14 14:28:30.433165
# Unit test for method validate of class Object
def test_Object_validate():
    p1 = fields.String(requied=True)
    p2 = fields.String(requied=False)
    obj = Object(properties={"p1": p1, "p2": p2})
    print(obj.validate({'p1': 'a', 'p2': 'b'}))

test_Object_validate()

#changement de la valeur de p1 et p2 (dans properties) permet de passer la validation
# par exemple si properties={'p1':p2}


# Generated at 2022-06-14 14:28:59.232074
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    f = Field(default="Test")
    assert f.get_default_value() == "Test"
    f = Field()
    assert f.get_default_value() is None
    f = Field(default=None)
    assert f.get_default_value() is None
    f = Field(default=lambda: "Test")
    assert f.get_default_value() == "Test"
    f = Field(allow_null=True)
    assert f.get_default_value() is None

# Generated at 2022-06-14 14:29:05.035228
# Unit test for method validate of class Choice
def test_Choice_validate():
    assert Choice(choices=[("a","b")]).validate("a") == "a"
    assert Choice(choices=[("a","b")]).validate("b") == "b"
    with pytest.raises(ValidationError) as excinfo:
        Choice(choices=[("a","b")]).validate("c")
    assert excinfo.type == ValidationError
    assert "Not a valid choice." in excinfo.value.text



# Generated at 2022-06-14 14:29:15.199262
# Unit test for method validate of class String
def test_String_validate():
    assert String(allow_null=True, allow_blank=True, max_length=10, min_length=2).validate('') is None
    assert String(allow_null=True, allow_blank=True, max_length=10, min_length=2).validate('a') == 'a'
    assert String(allow_null=True, allow_blank=True, max_length=10, min_length=2).validate('ab') == 'ab'
    assert String(allow_null=True, allow_blank=True, max_length=10, min_length=2).validate('abc') == 'abc'
    assert String(allow_null=True, allow_blank=True, max_length=10, min_length=2).validate('abcdefghij') == 'abcdefghij'

# Generated at 2022-06-14 14:29:23.105923
# Unit test for method __or__ of class Field
def test_Field___or__():
    class field(Field):
        def __init__(self, value):
            self.value = value
        def serialize(self, obj):
            return self.value

    assert (field(value=1) | field(value=2)).serialize(value=None) == 1 or 2
test_Field___or__()


# Generated at 2022-06-14 14:29:32.280816
# Unit test for method validate of class Array
def test_Array_validate():
    from flambe import Field, Arr

    class X(Field):
        class Schema:
            prop = Field()

    class Y(Field):
        class Schema:
            prop = Field()

    y = Y(**{"prop": "hello"})
    xx = [X(), X(**{"prop": "foo"}), y, X()]

    field = Arr(items=[X(), Y()])
    value, error = field.validate_or_error(xx)

    assert error is None
    assert value == [X(), X(**{"prop": "foo"}), y, X()]

    field = Arr(items=[X(), Y()], unique_items=True)
    value, error = field.validate_or_error(xx)
    assert error is not None

# Generated at 2022-06-14 14:29:40.697224
# Unit test for method validate of class Object
def test_Object_validate():
    properties = {
        "foo": String(min_length=1),
        "bar": Integer(),
    }
    obj = Object(properties=properties, max_properties=2)
    test_obj = {"foo": "a", "bar": 2}
    assert obj.validate(test_obj) == {"foo": "a", "bar": 2}
    #test_obj = {"foo": "", "bar": 2}
    #try:
    #    obj.validate(test_obj)
    #    raise Exception("shouldn't return here")
    #except ValidationError:
    #    #print("test_obj =", test_obj)
    #    #print("obj.validate(test_obj)")
    #    pass

# Generated at 2022-06-14 14:29:43.018351
# Unit test for method validate of class Object
def test_Object_validate():
    field = Object(properties = {'key': Integer()})
    with pytest.raises(ValidationError):
        field.validate({'key': '1'})

# Generated at 2022-06-14 14:29:45.232213
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    field = Field()
    assert field.get_default_value() == None
    field = Field(default=3)
    assert field.get_default_value() == 3

# Generated at 2022-06-14 14:29:50.866405
# Unit test for method validate of class Choice
def test_Choice_validate():
    choices = [
        ('sweden', 'Sweden'),
        ('denmark', 'Denmark'),
        ('norway', 'Norway'),
        ('finland', 'Finland'),
        ('iceland', 'Iceland'),
    ]
    choice = Choice(choices=choices)
    value = choice.validate('sweden')
    assert value == 'sweden'
    value = choice.validate('denmark')
    assert value == 'denmark'
    value = choice.validate('norway')
    assert value == 'norway'
    value = choice.validate('finland')
    assert value == 'finland'
    value = choice.validate('iceland')
    assert value == 'iceland'
    
    value = choice.validate('greenland')
    assert value == 'greenland'
   

# Generated at 2022-06-14 14:29:57.492156
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    field = Field()
    field = Field(default=None)
    field = Field(default=True)
    field = Field(default=False)
    field = Field(default=1)
    field = Field(default=3.14)
    field = Field(default=decimal.Decimal(1.1))
    field = Field(default='default')
    field = Field(default=b'default')
    field = Field(default=())
    field = Field(default=[])
    field = Field(default={})



# Generated at 2022-06-14 14:30:08.195912
# Unit test for constructor of class Const
def test_Const():
    f = Const("foo")
    assert f.const == "foo"
    # TODO: there are more tests to be done

test_Const()



# Generated at 2022-06-14 14:30:14.802826
# Unit test for method validate of class Object
def test_Object_validate():
    properties = {
        "key1": "test",
    }
    pattern_properties = {
        "key2": "test",
    }
    additional_properties = "test"
    property_names = "test"
    min_properties = 1
    max_properties = 1
    required = []
    obj = Object(properties, pattern_properties, additional_properties, property_names, min_properties, max_properties, required)
    assert obj.validate("") == {}
    try:
        assert obj.validate(None)
    except ValidationError:
        pass
    try:
        assert obj.validate(True)
    except ValidationError:
        pass
    try:
        assert obj.validate(1)
    except ValidationError:
        pass

# Generated at 2022-06-14 14:30:17.021579
# Unit test for method validate of class Choice
def test_Choice_validate():
    c = Choice(choices=['c1', 'c2'])
    assert c.validate('c1') == 'c1'
    assert c.validate(None) == None
    assert c.validate('') == ''
    with pytest.raises(ValidationError):
        c.validate('c3')

# Generated at 2022-06-14 14:30:25.002939
# Unit test for constructor of class Array
def test_Array():
    items = Field()
    additional_items = False
    min_items = None
    max_items = None
    exact_items = None
    unique_items = False
    field1 = Array(items=items,
            additional_items=additional_items,
            min_items=min_items,
            max_items=max_items,
            exact_items=exact_items,
            unique_items=unique_items)
    assert field1.items == None
    assert field1.additional_items == True
    assert field1.min_items == 0
    assert field1.max_items == None
    assert field1.unique_items == False

    items = [Field(), Field()]
    additional_items = Field()
    min_items = 2
    max_items = None
    exact_items = None
    unique

# Generated at 2022-06-14 14:30:29.939957
# Unit test for method validate of class Choice
def test_Choice_validate():
    choice = Choice(choices=('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'))
    choice.validate('A')
    choice.validate('J')
    choice.validate('R')
    assert choice.validate('Z')=='Z'
    assert choice.validate('')==''



# Generated at 2022-06-14 14:30:41.214003
# Unit test for method validate of class Number
def test_Number_validate():
    float_field = Number()
    float_field.validate(1.2)
    float_field.validate(1)
    float_field.validate("2.2")
    float_field.validate(None)
    with pytest.raises(ValidationError):
        float_field.validate("")
    with pytest.raises(ValidationError):
        float_field.validate("abc")
    with pytest.raises(ValidationError):
        float_field.validate("NaN")
    with pytest.raises(ValidationError):
        float_field.validate("Inf")

    int_field = Number(numeric_type=int)
    int_field.validate(1.2)
    int_field.validate(1)

# Generated at 2022-06-14 14:30:45.425282
# Unit test for constructor of class Const
def test_Const():
    assert Const(42).validate(42) == 42
    assert Const(None).validate(None) == None
    assert Const(42, allow_null=True).validate(None) == None
    assert Const(None, allow_null=True).validate(None) == None

# Generated at 2022-06-14 14:30:51.690581
# Unit test for method __or__ of class Field
def test_Field___or__():
    # Verify that we get a Union object when we take a pipe of two fields
    field1 = Field()
    field2 = Field()
    union = field1 | field2
    assert isinstance(union, Union)
    assert union.any_of == [field1, field2]
    # Verify that we get a Union object when we take a pipe of a Union object
    # and a Field object
    field3 = Field()
    union = union | field3
    assert isinstance(union, Union)
    assert union.any_of == [field1, field2, field3]



# Generated at 2022-06-14 14:30:55.176288
# Unit test for method __or__ of class Field
def test_Field___or__():
    print('Unit test for method __or__ of class Field')
    any_of = [3, 4]
    obj1 = Field()
    obj2 = Field()
    obj3 = Union(any_of)
    obj4 = Union(any_of)
    obj1 | obj2 | obj3 | obj4
    return 0
test_Field___or__()


# Generated at 2022-06-14 14:30:57.741817
# Unit test for method validate of class Choice
def test_Choice_validate():
    choice = Choice(choices=[('1', 'a'), ('2', 'b')], allow_null=False)
    value = choice.validate('1')
    assert value == '1'
    value = choice.validate('2')
    assert value == '2'
    try:
        value = choice.validate('3')
    except ValidationError:
        assert True
    else:
        assert False



# Generated at 2022-06-14 14:31:18.346766
# Unit test for method validate of class Array
def test_Array_validate():
    kwargs = {
        "items": [
            Integer(required=True, allow_null=False),
            Integer(required=True, allow_null=False),
        ],
        "additional_items": Field(),
        "min_items": None,
        "max_items": None,
        "unique_items": False,
        "allow_null": False,
        "default": None,
    }
    fields = Array(**kwargs)
    value = []
    value2 = fields.validate(value)
    assert value == value2



# Generated at 2022-06-14 14:31:19.469808
# Unit test for method validate of class Choice
def test_Choice_validate():
    result = Choice(choices=["test"]).validate("test")
    assert result == "test"



# Generated at 2022-06-14 14:31:29.324588
# Unit test for method validate of class Array
def test_Array_validate():
    items = [
        String(required=False),
        Boolean(required=False),
        Number(required=False),
        Integer(required=False),
        Object(required=False),
    ]
    b=Boolean(required=False)
    list_items = [Number(), Integer(), String(min_length=5), Boolean(), Object()]
    schema = Array(items=list_items, additional_items=b)
    # case 1: value is None, allow_null = True
    obj="None"
    try:
        serialized = schema.serialize(obj)
        print(serialized)
    except ValidationError as e:
        print(e.messages)

    # case 2: value is None, allow_null = False

# Generated at 2022-06-14 14:31:39.778005
# Unit test for method __or__ of class Field
def test_Field___or__():
    assert (Decimal(max_value = 123) | Decimal(min_value = 123)).any_of == [Decimal(max_value = 123),Decimal(min_value = 123)]
    assert (Decimal(max_value = 123) | Float(min_value = 123.0)).any_of == [Decimal(max_value = 123),Float(min_value = 123.0)]
    assert (Float(max_value = 123.0) | Decimal(min_value = 123)).any_of == [Float(max_value = 123.0),Decimal(min_value = 123)]
    assert (Float(max_value = 123.0) | Float(min_value = 123.0)).any_of == [Float(max_value = 123.0),Float(min_value = 123.0)]


# Generated at 2022-06-14 14:31:41.325858
# Unit test for method validate of class String
def test_String_validate():
    string = String()
    assert string.validate("Hello world!") == "Hello world!"

# Generated at 2022-06-14 14:31:41.989915
# Unit test for method validate of class Choice
def test_Choice_validate():
    #Choice.validate(10, strict=True)
    pass



# Generated at 2022-06-14 14:31:43.920846
# Unit test for method validate of class Choice
def test_Choice_validate():
    c = Choice(allow_null=True,choices=[("a","a"),("b","b"),("c","c")])
    assert c.validate('a')=='a'
    assert c.validate(None)==None
    assert c.validate('')==None
    assert c.validate('d')=='d'



# Generated at 2022-06-14 14:31:45.964230
# Unit test for method validate of class Choice
def test_Choice_validate():
    field = Choice(allow_null=True, choices=[0, 1])
    assert field.validate(None) is None
    assert field.validate(0) == 0
    assert field.validate(1) == 1
    with raises(ValidationError):
        field.validate(2)
    with raises(ValidationError):
        field.validate("3")


# Generated at 2022-06-14 14:31:54.604883
# Unit test for method validate of class Array
def test_Array_validate():
    a = Array(min_items=5)
    assert a.validate([1,2,3,4,5]) == [1,2,3,4,5]
    # expected to fail since items are less than 5
    try:
      a.validate([1,2,3,4])
    except ValidationError:
      assert True
    except:
      assert False
    
    # expected to fail since item is not a list
    try:
      a.validate(1)
    except ValidationError:
      assert True
    except:
      assert False


# Test for method serialize of class Array

# Generated at 2022-06-14 14:31:59.867465
# Unit test for method validate of class Choice
def test_Choice_validate():
    fields=[{"name":"temperature","type":"choice", "null":False, "required":True, "choices":[{"value":15, "display_name":"cold"},{"value":18, "display_name":"mild"},{"value":22, "display_name":"warm"}]}, {"name":"humidity", "type":"choice", "null":True, "required":False, "choices": [{"value":30, "display_name":"very_humid"},{"value":55, "display_name":"some_humidity"},{"value":75, "display_name":"no_humidity"}]}]

# Generated at 2022-06-14 14:32:13.782763
# Unit test for method validate of class Object
def test_Object_validate():
    # test_Object_validate_null_values
    properties = {
        "foo": Integer(required=True),
        "bar": Integer(),
        "baz": Integer(),
    }
    schema = Object(properties=properties)
    assert schema.validate(None, strict=True) is None
    # test_Object_validate_required
    with pytest.raises(ValidationError):
        schema.validate({}, strict=True)
    # test_Object_validate_required_min_properties
    schema = Object(properties=properties, min_properties=1, max_properties=3)
    with pytest.raises(ValidationError):
        schema.validate({}, strict=True)
    # test_Object_validate_required_max_properties

# Generated at 2022-06-14 14:32:23.963957
# Unit test for method validate of class Array
def test_Array_validate():
    try:
        min_items = 1
        max_items = 2
        test_array = Array(Int(),min_items=min_items,max_items=max_items)
        assert test_array.validate([1,2.0]) == [1,2]
    except AssertionError:
        print("Failed test validate of class Array")
        raise AssertionError
    try:
        min_items = 1
        max_items = 2
        test_array = Array(Int(),min_items=min_items,max_items=max_items)
        assert test_array.validate([1,2,3]) == [1,2]
    except AssertionError:
        print("Failed test validate of class Array")
        raise AssertionError
    print("Passed test validate of class Array")



# Generated at 2022-06-14 14:32:36.014365
# Unit test for method validate of class Choice
def test_Choice_validate():
    def test1():
        field = Choice(choices=[
            ("Washington", "Washington"),
            ("Washington DC", "Washington DC"),
            ("Newyork", "Newyork"),
            ("New Jersey", "New Jersey")
        ])
        val = field.validate_or_error("Washington DC")
        assert val.value == "Washington DC"

    def test2():
        field = Choice(choices=[
            ("Washington", "Washington"),
            ("Washington DC", "Washington DC"),
            ("Newyork", "Newyork"),
            ("New Jersey", "New Jersey")
        ])
        val = field.validate_or_error("Newyork")
        assert val.value == "Newyork"


# Generated at 2022-06-14 14:32:44.340607
# Unit test for method validate of class Choice
def test_Choice_validate():
    choices = (("0", "0"), ("0.5", "0.5"), ("1", "1"))
    choice = Choice(choices=choices)
    assert choice.validate("0.5") == "0.5", "Should be '0.5'."
    assert choice.validate("1.0") == "1", "Should be '1'."
    assert choice.validate("-0.5") == "-0.5", "Should be '-0.5'"
    try:
        assert choice.validate("null") == "null", "Should be 'null'."
    except ValidationError:
        assert True



# Generated at 2022-06-14 14:32:47.363970
# Unit test for constructor of class Const
def test_Const():
    assert Const(5) is not None
    with pytest.raises(AssertionError):
        Const(5, allow_null=True)


# Generated at 2022-06-14 14:32:54.746047
# Unit test for constructor of class Const
def test_Const():
    # test for only null value
    a = Const(None)
    assert a.validate(None) == None
    try:
        a.validate(0)
    except ValidationError as e:
        assert e.code == 'only_null'
    
    # test for specific value
    b = Const(1)
    assert b.validate(1) == 1
    try:
        b.validate(0)
    except ValidationError as e:
        assert e.code == 'const'
        assert e.text == "Must be the value '1'."


# Generated at 2022-06-14 14:33:07.813972
# Unit test for method validate of class Choice
def test_Choice_validate():
    expected_choices = [("1", "1"), ("2", "2"), ("3", "3")]
    choice = Choice(choices=expected_choices)
    assert choice.validate(value="3") == "3"

    expected_choices = [("1", "1"), ("2", "2"), ("3", "3")]
    choice = Choice(choices=expected_choices, allow_null=True, )
    assert choice.validate(value=None,  strict=False) == None

    expected_choices = [("1", "1"), ("2", "2"), ("3", "3")]
    choice = Choice(allow_null=False,  choices=expected_choices)
    with pytest.raises(ValidationError):
        choice.validate(value="4")

    expected_cho

# Generated at 2022-06-14 14:33:19.553374
# Unit test for method validate of class Choice
def test_Choice_validate():
    a = Choice(choices=['banana', 'apple', 'orange'])
    assert a.validate('banana') == 'banana'
    assert a.validate('apple') == 'apple'
    assert a.validate('orange') == 'orange'
    with pytest.raises(ValidationError):
        a.validate('watermelon')
    with pytest.raises(ValidationError):
        a.validate('')
    b = Choice(choices=['banana', 'apple', 'orange'], allow_null=True)
    assert b.validate('banana') == 'banana'
    assert b.validate('apple') == 'apple'
    assert b.validate('orange') == 'orange'
    assert b.validate('') == None