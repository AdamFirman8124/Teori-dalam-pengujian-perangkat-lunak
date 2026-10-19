

# Generated at 2022-06-14 14:25:36.614591
# Unit test for method serialize of class Array
def test_Array_serialize():
    # Arrange
    class IntegerField(Field):
        def validate(self,value,strict=False):
            return int(value)
    class StringField(Field):
        def validate(self,value,strict=False):
            return str(value)

    a=Array(StringField)
    b=Array(items=IntegerField)
    # Act
    a_serialize = a.serialize(['1','2','3'])
    b_serialize = b.serialize([1,2,3])
    # Assert
    assert a_serialize == ['1','2','3']
    assert b_serialize == [1,2,3]


# Generated at 2022-06-14 14:25:41.880301
# Unit test for method serialize of class String
def test_String_serialize():
    test_string = String(format="datetime")
    test_datetime = datetime.datetime(year=1991, month=2, day=11, hour=1,minute=1,second=1)
    assert test_string.serialize(test_datetime) == test_datetime.isoformat()

# Generated at 2022-06-14 14:25:54.094018
# Unit test for method validate of class Union
def test_Union_validate():
    # if value is None and self.allow_null:
    class field_a(Field):
        def __init__(self, allow_null = True, **kwargs):
            super().__init__(**kwargs)
            self.allow_null = allow_null

    field_1 = field_a()
    union_field = Union(any_of = [field_1], allow_null=True)
    try:
        union_field.validate(value = None)
        assert True
    except:
        assert False

    # elif value is None:
    class field_b(Field):
        def __init__(self, allow_null = False, **kwargs):
            super().__init__(**kwargs)
            self.allow_null = allow_null

    field_2 = field_b()
    union

# Generated at 2022-06-14 14:25:58.795687
# Unit test for constructor of class Array
def test_Array():
    array = Array()
    assert array.items is None
    assert array.additional_items is False
    assert array.min_items is None
    assert array.max_items is None
    assert array.unique_items is False

    array = Array(items=[Integer(), String()])
    assert array.items is not None


# Generated at 2022-06-14 14:26:06.936782
# Unit test for method __or__ of class Field
def test_Field___or__():
    from typesystem import Array
    from typesystem.fields import Boolean
    from typesystem.fields import Integer
    from typesystem.fields import Number
    from typesystem.fields import Text
    from typesystem.fields import Union
    from typesystem.fields import Value
    from typesystem.fields import values
    
    
    
    
    
    
    
    
    
    
    from typesystem import Array
    from typesystem.fields import Boolean
    from typesystem.fields import Integer
    from typesystem.fields import Number
    from typesystem.fields import Text
    from typesystem.fields import Union
    from typesystem.fields import Value
    from typesystem.fields import values
    import typing
    import decimal
    isinstance(Boolean(), Field)
    isinstance(Text(), Field)
    isinstance(Integer(), Field)
    isinstance

# Generated at 2022-06-14 14:26:17.487924
# Unit test for method validate of class Array
def test_Array_validate():
    class TestArray(Array):
        def validate(self, value: typing.Any, *, strict: bool = False) -> typing.Any:
            value = super().validate(value, strict=strict)
            return value
    print(TestArray(max_items=3).validate([1,2,3]))
    print(TestArray(max_items=3).validate([1,2,3,4]))
    print(TestArray(max_items=3).validate([1,2,3,4,5]))
    print(TestArray().validate([1,2,3,4,5]))
    print(TestArray(additional_items=True).validate([1,2,3,4,5]))

# Generated at 2022-06-14 14:26:23.866953
# Unit test for method validate of class Choice
def test_Choice_validate():
    choice_field = Choice(choices=[("1", "1"), ("2", "2")], allow_null=True)
    print(choice_field.validate("1"))
    print(choice_field.validate("2"))
    print(choice_field.validate("3"))
    print(choice_field.validate(""))


# Generated at 2022-06-14 14:26:34.420212
# Unit test for method validate of class Choice
def test_Choice_validate():
    class testField(Field):
        def __init__(self, **kwargs: typing.Any):
            super().__init__(**kwargs)
               
        def validate(self,value: typing.Any, *, strict: bool = False):
            if value is None and self.allow_null:
                return None
            elif value is None:
                raise self.validation_error("null")
            elif value not in Uniqueness([key for key, value in self.choices]):
                if value == "":
                    if self.allow_null and not strict:
                        return None
                    raise self.validation_error("required")
                raise self.validation_error("choice")
            return value


# Generated at 2022-06-14 14:26:39.557493
# Unit test for method validate of class Array
def test_Array_validate():
    class ObjectField(Field):
        def serialize(self, obj: typing.Any) -> typing.Any:
            if obj is None:
                return None
            return {"value": obj}

    t = Array(ObjectField())
    assert t.validate("not an array") == "not an array"
    assert t.validate([1, 2]) == [
        {"value": 1},
        {"value": 2},
    ]

# Generated at 2022-06-14 14:26:43.565228
# Unit test for constructor of class Const
def test_Const():
    # Constructor
    # First argument must not be None
    try:
        Const(None)
    except:
        return
    raise Exception('test_Const failed')


# Generated at 2022-06-14 14:26:53.550068
# Unit test for method serialize of class Array
def test_Array_serialize():
    schema = Array()
    serialized = schema.serialize([1, 2, 3])
    assert serialized == [1, 2, 3]



# Generated at 2022-06-14 14:26:57.499855
# Unit test for method validate of class Choice
def test_Choice_validate():
    choice = Choice(name='test')
    assert choice.validate('20', strict=False) == '20'
    assert choice.validate(None, strict=False) == None
    assert choice.validate('', strict=False) == 'required'



# Generated at 2022-06-14 14:27:05.188819
# Unit test for method validate of class Object
def test_Object_validate():
    """Case to test validation of the method Object.validate"""
    test_schema = Object(
        properties = {
                    "id": Integer(),
                    "name": String(min_length=0, max_length=255)
                },
        additional_properties = False,
        required = ["id"],
        allow_null = True
            )
    response = test_schema.validate({"id": 0, "name": "abc"})
    assert response == {"id": 0, "name": "abc"}
    response = test_schema.validate({"name": "abc"})
    assert response == {"name": "abc"}
    response = test_schema.validate({"id": 0})
    assert response == {"id": 0}
    response = test_schema.validate(None)
    assert response == None

# Generated at 2022-06-14 14:27:13.507774
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    field = Field(default=None)
    assert field.get_default_value() == None
    field = Field(default=1)
    assert field.get_default_value() == 1
    field = Field(default=[])
    field.default.append(1)
    assert field.get_default_value() == []
    assert field.get_default_value() == [1]
    field = Field(default=[])
    assert field.get_default_value() == []
    field = Field(default=lambda: 1)
    assert field.get_default_value() == 1

# Generated at 2022-06-14 14:27:16.141760
# Unit test for method validate of class Array
def test_Array_validate():
    a = Field()
    data = [1,2,3]
    a = Array(items=a, min_items=2, max_items=4)
    a.validate(data)

# Generated at 2022-06-14 14:27:22.349684
# Unit test for method validate_or_error of class Field
def test_Field_validate_or_error():
    from typesystem import Integer, String
    from typesystem.base import ValidationResult
    from typesystem.error_messages import ErrorMessages
    from typesystem.fields import Field
    from typesystem.message import Message

    class dummy_field(Field):
        errors = ErrorMessages()

        def validate(self, value, *, strict):
            return value
        
    f = dummy_field()
    assert f.validate_or_error("test") == ValidationResult(
        value="test", error=None
    )
    assert f.validate_or_error(2, strict=True) == ValidationResult(
        value=2, error=None
    )

# Generated at 2022-06-14 14:27:33.551673
# Unit test for method validate of class Union
def test_Union_validate():
    int1 = Integer(maximum=5, minimum=1)
    int2 = Integer(maximum=10, minimum=6)
    str1 = String(min_length=5, max_length=10)
    obj1 = Object(properties={'name': String(), 'age': Integer()})
    obj2 = Object(properties={'name': String(), 'lastname': String()})


# Generated at 2022-06-14 14:27:34.587162
# Unit test for method __or__ of class Field
def test_Field___or__():
    assert False


# Generated at 2022-06-14 14:27:42.163760
# Unit test for method __or__ of class Field
def test_Field___or__():
    """Test method __or__ of class Field"""
    assert Field() | Field() is not None
    assert Field(description='description', title='title') | Field(description='description', title='title') is not None
    assert Field(description='description', title='title') | Field(allow_null=True, description='description', title='title') is not None
    assert Field(title='title') | Field(title='title', allow_null=True) is not None
    assert Field(title='title', allow_null=True) | Field(allow_null=True, title='title') is not None
    assert Field(allow_null=True, title='title') | Field(title='title', default='union') is not None


# Generated at 2022-06-14 14:27:44.121799
# Unit test for method serialize of class Array
def test_Array_serialize():
    items = [Integer(), String(),Float()]
    obj = [1,2,3,4,5,6,7]
    print(Array(items=items).serialize(obj))



# Generated at 2022-06-14 14:28:02.125511
# Unit test for method validate of class Choice
def test_Choice_validate():
    c1 = Choice(choices=[("a", "A")])
    s = 'c'
    assert c1.validate(s) == "c"


# Generated at 2022-06-14 14:28:04.665433
# Unit test for constructor of class String
def test_String():
    field = String(format="date")
    return field


# Generated at 2022-06-14 14:28:10.210300
# Unit test for method validate of class Array
def test_Array_validate():
    # Check invalid type must be an array
    # Error message must be the same
    with pytest.raises(ValidationError) as error:
        data = {}
        Array(strict=True).validate(data)
    assert error.value.messages()[0].code == "type"

    # Check allow null
    # Error message must be different, besides not have message
    assert Array(allow_null=True).validate(None) is None

    # Check null not allowed, then raise error
    # Error message must be the same
    with pytest.raises(ValidationError) as error:
        data = None
        Array(allow_null=False, strict=True).validate(data)
    assert error.value.messages()[0].code == "null"

    # Check max item
    # Error message must be

# Generated at 2022-06-14 14:28:13.445893
# Unit test for method validate of class Choice
def test_Choice_validate():
    a = Choice(choices=[("Dog", "Dog"), ("Cat", "Cat"), ("Bear", "Bear")])
    print(a.validate("Dog"))
    print(a.validate("Cat"))
    print(a.validate("Bear"))
    print(a.validate("Wolf"))



# Generated at 2022-06-14 14:28:21.077040
# Unit test for method validate of class Choice
def test_Choice_validate():
    field = Choice(choices=[
        ('a','a'),
        ('b','b')
    ])
    field.validate('','','','')
    field.validate(None) #test for allow_null
    field.validate('Test') #test for type error
    field.validate(2) #test for value error
    field.validate(1) #test for type error
    
test_Choice_validate()


# Generated at 2022-06-14 14:28:31.195449
# Unit test for method __or__ of class Field
def test_Field___or__():
  from datetime import date
  from typesystem.fields import String, Date
  from typesystem.unions import Union
  
  union = String() | Date()
  
  assert union.__class__ == Union
  assert len(union.any_of) == 2
  assert isinstance(union.any_of[0], String)
  assert isinstance(union.any_of[1], Date)
  
  assert union.validate(None).value == None
  assert union.validate(None, strict=True).error.code == 'required'
  assert union.validate('').error.code == 'invalid_type'
  assert union.validate('', strict=True).value == ''
  assert union.validate(date.today()).error.code == 'invalid_type'

# Generated at 2022-06-14 14:28:32.462346
# Unit test for method validate of class Union
def test_Union_validate():
    schema = Union(any_of=[Text(), Boolean()])
    schema.validate(True)



# Generated at 2022-06-14 14:28:34.091947
# Unit test for method __or__ of class Field
def test_Field___or__():
    from typesystem import Integer

    assert isinstance(Field() | Field(), Union)
    assert isinstance(Field() | Integer(), Union)
    assert isinstance(Integer() | Field(), Union)



# Generated at 2022-06-14 14:28:35.901780
# Unit test for constructor of class Const
def test_Const():
    assert Const(3).validate(3) == 3


# Generated at 2022-06-14 14:28:43.071346
# Unit test for method validate of class Array
def test_Array_validate():
    class MyString(Str):
        def __init__(self):
            super().__init__(allow_empty=False, allow_whitespace=False)
    schema = Array(
        items = [MyString(), MyString(), MyString()],
        min_items = 1,
        max_items = 4,
        unique_items = True)
    test_list1 = ["a", "b", "c"]
    test_list2 = []
    test_list3 = ["a", "b", "c", "d"]
    test_list4 = ["a", "a", "b", "c"]
    test_list5 = "hello"
    test_list6 = ["a", "b", "c", "d", "e"]
    test_list7 = ["a", "b", 1]

# Generated at 2022-06-14 14:29:08.427975
# Unit test for method validate of class String
def test_String_validate():
    obj = String()
    obj.title = "title"
    obj.description = "description"
    obj.allow_blank = True
    obj.trim_whitespace = True
    obj.max_length = 100
    obj.min_length = 10
    obj.pattern = "test"
    obj.format = "datetime"
    assert obj.validate("test string") == "test string", "Wrong value returned"
    assert obj.validate("test string") != "wrong value", "Wrong value returned"

# Generated at 2022-06-14 14:29:19.035889
# Unit test for method validate of class Choice
def test_Choice_validate():
    choice = Choice(choices = ['apple','banana','lemon','orange'])
    assert choice.validate('lemon') == 'lemon'
    assert choice.validate('orange') == 'orange'
    assert choice.validate('apple') == 'apple'
    assert choice.validate('apple') == 'apple'
    assert choice.validate('apple') == 'apple'
    assert choice.validate('apple') == 'apple'
    assert choice.validate('apple') == 'apple'
    assert choice.validate('apple') == 'apple'
    assert choice.validate('apple') == 'apple'
    assert choice.validate('apple') == 'apple'
    assert choice.validate('apple') == 'apple'
    assert choice.validate('apple') == 'apple'

# Generated at 2022-06-14 14:29:29.353437
# Unit test for method validate of class Choice
def test_Choice_validate():
    choice = Choice()
    assert choice.validate(None, strict=False) is None
    assert choice.validate(None, strict=True) is None
    #
    with pytest.raises(ValidationError):
        choice.validate(None, strict=True)
    #
    choice = Choice(allow_null=False)
    assert choice.validate(None, strict=True) is None
    #
    choice = Choice(allow_null=False)
    assert choice.validate(None, strict=False) is None
    #
    choice = Choice(allow_null=True)
    assert choice.validate(None, strict=True) is None
    #
    choice = Choice(allow_null=None)

# Generated at 2022-06-14 14:29:37.340597
# Unit test for method validate of class Choice
def test_Choice_validate():
    field = Choice(choices=["red", "blue"])
    result = field.validate("red")
    assert result == "red"

    field = Choice(choices=[("red", "Red"), ("blue", "Blue")])
    result = field.validate("red")
    assert result == "red"
    result = field.validate("blue")
    assert result == "blue"



# Generated at 2022-06-14 14:29:43.018441
# Unit test for method validate of class Choice
def test_Choice_validate():
    # Testing Choice's method validate with a value that already exists among the list of choices
    field = Choice(choices = [('red', 'red'),('blue', 'blue'),('black', 'black')])
    field.validate(value = 'blue')
    # Testing Choice's method validate with a value that does not exist among the list of choices
    field = Choice(choices = [('red', 'red'),('blue', 'blue'),('black', 'black')])
    field.validate(value = 'green')



# Generated at 2022-06-14 14:29:53.981785
# Unit test for constructor of class Array
def test_Array():
    field = Array()
    assert field.items is None
    assert field.additional_items is False
    assert field.min_items is None
    assert field.max_items is None
    assert field.unique_items is False

    field = Array(
        items=Field(),
        additional_items=Field(),
        min_items=3,
        max_items=5,
        unique_items=True,
    )
    assert isinstance(field.items, Field)
    assert isinstance(field.additional_items, Field)
    assert field.min_items == 3
    assert field.max_items == 5
    assert field.unique_items is True



# Generated at 2022-06-14 14:29:57.423282
# Unit test for method __or__ of class Field
def test_Field___or__():
    f1 = String(max_length=3)
    f2 = String(max_length=5)
    f3 = f1 | f2
    assert isinstance(f3, Union)
    assert len(f3.any_of) == 2
    assert f1 in f3.any_of

# Generated at 2022-06-14 14:30:06.784063
# Unit test for constructor of class String
def test_String():
    # Test constructor.
    newString = String()
    assert newString.allow_null == False
    assert newString.title == ""
    assert newString.description == ""
    assert newString._creation_counter == 0
    assert len(newString.errors) == 5
    assert newString.allow_blank == False
    assert newString.trim_whitespace == True
    assert newString.max_length == None
    assert newString.min_length == None
    assert newString.pattern == None
    assert newString.format == None


# Generated at 2022-06-14 14:30:13.199351
# Unit test for method validate of class Object

# Generated at 2022-06-14 14:30:20.407144
# Unit test for constructor of class String
def test_String():
    str1 = String(allow_blank = True, trim_whitespace = True, max_length = None, min_length = None, pattern = None, format = None, title="", description="")
    assert str1.allow_blank == True
    assert str1.trim_whitespace == True
    assert str1.max_length == None
    assert str1.min_length == None
    assert str1.pattern == None
    assert str1.format == None
    assert str1.title == ""
    assert str1.description == ""

# Unit tests for String validation

# Generated at 2022-06-14 14:30:40.185914
# Unit test for method validate of class Number
def test_Number_validate():
    s = Number()
    try:
        assert (s.validate("1")) == 1
    except ValidationError:
        assert False
    try:
        s.validate("a") == 1
    except ValidationError:
        assert True
    try:
        assert (s.validate("1.01")) == 1.01
    except ValidationError:
        assert False
    else:
        assert False
    try:
        assert (s.validate("0")) == 0
    except ValidationError:
        assert False
    try:
        assert (s.validate("999999")) == 999999
    except ValidationError:
        assert False
    try:
        assert (s.validate("-999999")) == -999999
    except ValidationError:
        assert False
test_Number_validate()



# Generated at 2022-06-14 14:30:50.370494
# Unit test for method __or__ of class Field
def test_Field___or__():
    Field.errors["not_a_field"] = "Invalid Type"
    Field.errors["not_a_field2"] = "Invalid Type"

    field = Field(title="Field")
    field2 = Field(title="Field2")

    union = field | field2
    assert len(union.any_of) == 2
    assert union.any_of[0].title == "Field"
    assert union.any_of[1].title == "Field2"

    field3 = Field(title="Field3")
    union2 = union | field3
    assert len(union2.any_of) == 3
    assert union2.any_of[0].title == "Field"
    assert union2.any_of[1].title == "Field2"
    assert union2.any_of[2].title == "Field3"



# Generated at 2022-06-14 14:30:57.210734
# Unit test for method validate of class String
def test_String_validate():
    assert String(title="Name").validate("Jonas") == "Jonas"
    assert String(title="Name").validate("") == ""
    assert String(title="Name").validate(None) == None
    assert String(title="Name", allow_null=True).validate(None) == None
    assert String(title="Name", allow_blank=True).validate("") == ""
    assert String(title="Name", allow_null=True, allow_blank=True).validate(None) == None
    assert String(title="Name", max_length=5).validate("Jonas") == "Jonas"
    assert String(title="Name", min_length=5).validate("Jonas") == "Jonas"

# Generated at 2022-06-14 14:31:01.469913
# Unit test for method validate of class String
def test_String_validate():
    f = String(format="uuid")
    a = f.validate("d1d9ad9e-3f40-4065-beb2-7b2cae5b249e")
    assert isinstance(a, str)
    assert a == "d1d9ad9e-3f40-4065-beb2-7b2cae5b249e"


# Test for method serialize of class String

# Generated at 2022-06-14 14:31:04.528476
# Unit test for method validate of class Array
def test_Array_validate():
    arr = [1, 2, 3]
    array = Array(min_items=1, max_items=5)
    assert array.validate(arr)
    assert array.validate(arr) == [1, 2, 3]
    arr[-1] = 5
    assert array.validate(arr)


# Generated at 2022-06-14 14:31:12.617917
# Unit test for method validate of class Number
def test_Number_validate():
    number = Number()
    try:
        number.validate(True)
        assert False, "No exception is raised"
    except ValidationError as e:
        assert e.code == "type"
        assert e.text == "Must be a number."

    try:
        number.validate(None)
        assert False, "No exception is raised"
    except ValidationError as e:
        assert e.code == "null"
        assert e.text == "May not be null."

    try:
        number.validate(float('inf'))
        assert False, "No exception is raised"
    except ValidationError as e:
        assert e.code == "finite"
        assert e.text == "Must be finite."


# Generated at 2022-06-14 14:31:16.145119
# Unit test for method __or__ of class Field
def test_Field___or__():
    class Field1(Field):
        pass
    class Field2(Field):
        pass
    union = Field1() | Field2()
    assert isinstance(union.any_of[0], Field1)
    assert isinstance(union.any_of[1], Field2)


# Generated at 2022-06-14 14:31:23.490300
# Unit test for method validate of class Object
def test_Object_validate():
    field = Field()
    field2 = Field()
    field3 = Field(allow_null=True)
    field4 = Field()
    field5 = Field()
    field6 = Field()
    field7 = Field()

    properties = {"name": field, "age": field2, "phone": field3, "mail": field4}
    keys = properties.keys()

    def additional_properties(value):
        if value not in keys:
            raise field5.validation_error("invalid_property")

    additional_properties = Field(validate=additional_properties)

    def property_names(value):
        if value not in ["name", "age", "phone", "mail", "add"]:
            raise field6.validation_error("invalid_property")

    property_names = Field(validate=property_names)

# Generated at 2022-06-14 14:31:24.786015
# Unit test for constructor of class Const
def test_Const():
    schema = Const(2)
    schema.validate(2)
    with pytest.raises(ValidationError):
        schema.validate(3)


# Generated at 2022-06-14 14:31:36.620987
# Unit test for method validate of class Array
def test_Array_validate():
    a = Array()
    assert a.validate([]) == []
    assert a.validate([None]) == [None]
    assert a.validate([1,2,3]) == [1,2,3]
    assert a.validate([1,2.0,3]) == [1,2.0,3]
    assert a.validate(["a","b","c"]) == ["a","b","c"]
    assert a.validate([{1:2}]) == [{1:2}]
    assert a.validate([[]]) == [[]]
    assert a.validate([{}]) == [{}]

    try:
        a.validate(None)
        assert False
    except ValidationError as e:
        assert e.messages()[0].text == "May not be null."

# Generated at 2022-06-14 14:31:56.922297
# Unit test for method validate of class String
def test_String_validate():
    myString = String(allow_null=True)
    try:
        myString.validate(None)
    except Exception as e:
        assert False #Shouldn't have exception
    try:
        myString.validate(5)
        assert False #Should have thrown exception
    except Exception as e:
        assert isinstance(e, ValidationError)
    try:
        myString.validate("")
        assert False #Should have thrown exception
    except Exception as e:
        assert isinstance(e, ValidationError)
    try:
        myString.validate("Hello")
    except Exception as e:
        assert False #Should not have thrown exception


# Generated at 2022-06-14 14:32:08.874451
# Unit test for method validate of class Array
def test_Array_validate():
    from marshmallow_polyfield import PolyField
    from marshmallow_polyfield.fields import Int

    array = Array()
    for value in (1, "1", True, None):
        with pytest.raises(ValidationError):
            array.validate(value)

    array = Array(min_items=3, max_items=3)
    with pytest.raises(ValidationError):
        array.validate([])
    with pytest.raises(ValidationError):
        array.validate([1, 2])
    with pytest.raises(ValidationError):
        array.validate([1, 2, 3, 4, 5])

    array = Array(items=Int())

# Generated at 2022-06-14 14:32:09.542782
# Unit test for method __or__ of class Field
def test_Field___or__():

    pass



# Generated at 2022-06-14 14:32:20.908869
# Unit test for method validate of class Array
def test_Array_validate():
  a = Array(items=String())
  b = a.validate(["hey", "now", "brown", "cow"])
  assert b == ["hey", "now", "brown", "cow"]
  a = Array(items=String())
  b = a.validate([1, 2, 3])
  assert b == [1, 2, 3]
  # if only one error happens, the first error gets raised
  try:
    a = Array(items=String())
    b = a.validate(["hey", "now", 2, "cow"])
    assert False
  except ValidationError as e:
    assert e.messages()[0].text == "Must be a string."
  # if there are multiple errors, they all get added to the ValidationError object

# Generated at 2022-06-14 14:32:32.251755
# Unit test for method __or__ of class Field
def test_Field___or__():
    field1 = Field()
    field2 = Field(allow_null=True)
    field3 = Field()

    union_of_1_and_2 = field1 | field2
    assert isinstance(union_of_1_and_2, Union)
    assert union_of_1_and_2.any_of == [field1, field2]
    assert not union_of_1_and_2.fields
    assert not union_of_1_and_2.allow_null

    union_of_2_and_3 = field2 | field3
    assert isinstance(union_of_2_and_3, Union)
    assert union_of_2_and_3.any_of == [field2, field3]

    union_of_1_and_2_and_3 = union_of_1_and

# Generated at 2022-06-14 14:32:40.104380
# Unit test for method validate of class Choice
def test_Choice_validate():
    f = Choice(choices=[("first", "1"), ("second", "2")])
    assert f.validate("first") == "first"
    try:
        f.validate("3")
    except ValidationError as error:
        assert error.code == "choice"
    try:
        f.validate("")
        raise Exception()
    except ValidationError as error:
        assert error.code == "required"
    #
    f = Choice(choices=[("first", "1"), ("second", "2")], allow_null=True)
    assert f.validate("first") == "first"
    assert f.validate("3") == "3"
    try:
        f.validate("")
    except ValidationError as error:
        assert error.code == "required"

# Generated at 2022-06-14 14:32:51.081980
# Unit test for method validate of class Array
def test_Array_validate():
    test_Array = Array(
        items=None,
        additional_items=False,
        min_items=None,
        max_items=None,
        exact_items=None,
        unique_items=False,
        **{}
    )
    test_Array.validate([])
    test_Array.validate(["hello", "world"])
    test_Array.validate(["lesson1", "lesson2", "lesson3", "lesson4", "lesson5"])
    test_Array.validate(["one", "two", "three", "four", "five", "six", "seven"])


# Generated at 2022-06-14 14:32:54.052823
# Unit test for method validate of class Choice
def test_Choice_validate():
    c1 = Choice(choices=['a', 'b'])
    assert c1.validate('a') == 'a'


# Generated at 2022-06-14 14:33:06.848879
# Unit test for method validate of class Array
def test_Array_validate():
    test_object = Array(items=Integer())
    assert test_object.validate(None) == None
    assert test_object.validate([]) == []
    assert test_object.validate([1]) == [1]
    assert test_object.validate([1.0]) == [1]
    assert test_object.validate([1, 2, 3]) == [1, 2, 3]
    assert test_object.validate([1, 2, 3.0]) == [1, 2, 3]
    assert test_object.validate([1, 2, "3"]) == [1, 2, 3]
    assert test_object.validate(["1", "2", "3"]) == [1, 2, 3]

# Generated at 2022-06-14 14:33:12.167120
# Unit test for method validate of class Choice
def test_Choice_validate():
    Choice(choices=["a"]).validate("a", strict=True)
    assert Choice(choices=["a"]).validate("a", strict=False) == "a"
    assert Choice(choices=["a"]).validate("a", strict=False) in [("a", "a")]
