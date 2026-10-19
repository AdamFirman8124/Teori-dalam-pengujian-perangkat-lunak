

# Generated at 2022-06-14 14:25:11.792218
# Unit test for method validate of class Array
def test_Array_validate():
    array = Array(
        items = String(allow_empty=False),
        unique_items = True
    )

    list_value = [1,2,3,4]
    validated_list_value = array.validate(list_value)
    assert validated_list_value == list_value
    
    list_value = [1,"2","3",4]
    try:
        array.validate(list_value)
    except ValidationError as e:
        assert len(e.messages) == 2
        assert e.messages[0].instruction == "unique_items"
        assert e.messages[1].instruction == "type"
        
test_Array_validate()


# Generated at 2022-06-14 14:25:17.819668
# Unit test for constructor of class Array
def test_Array():
    items = [String(), Number()]
    additional_items = Number()
    min_items = 0
    max_items = 10
    unique_items = True
    inf = initf = Field()
    arr = Array(items, additional_items, min_items, max_items, unique_items)
    # test __init__
    assert inf == initf
    assert arr.items == items
    assert arr.additional_items == additional_items
    assert arr.min_items == min_items
    assert arr.max_items == max_items
    assert arr.unique_items == unique_items
    # test validate
    assert arr.validate([]) == []
    assert arr.validate(["1"]) == ["1"]
    assert arr.validate(["1", 1]) == ["1", 1]
    assert arr.valid

# Generated at 2022-06-14 14:25:24.922823
# Unit test for method validate of class Array
def test_Array_validate():
   arr1=Parameter.objects.get(id=1)
   arr2=Parameter.objects.get(id=2)
   arr3=Parameter.objects.get(id=3)
   arr_field=Array(items=arr1,additional_items=True,required=True)
   arr_field1=Array(items=arr2,additional_items=True,required=True)
   arr_field2=Array(items=arr3,additional_items=True,required=True)
   arr=[1,2,3]
   arr_field.validate(arr)
   arr_field1.validate(arr)
   arr_field2.validate(arr)

# Generated at 2022-06-14 14:25:32.786702
# Unit test for method validate of class Array
def test_Array_validate():
    type_ = Array(items = String())
    assert type_.validate(["1","2",3]) == ["1","2",3]
    assert type_.validate([1,2,3]) == [1,2,3]
    try:
        type_.validate([1,2,"3"])
    except ValidationError:
        error = ValidationError()
        assert len(error.messages) == 3
        assert error.messages[0].code == "type"
        assert error.messages[1].code == "type"
        assert error.messages[2].code == "type"


# Generated at 2022-06-14 14:25:40.519736
# Unit test for method validate of class String
def test_String_validate():
    from typesystem.exceptions import ValidationError as E
    from typesystem.fields import String
    import pytest
    for _ in range(1000):
        assert String(min_length=1, max_length=1, pattern='[0-9]').validate('1') == '1'
        assert String(format="date").validate("2000-01-01")
        assert String(format="time").validate("12:34:56")
        assert String(format="datetime").validate("2000-01-01T12:34:56")
    with pytest.raises(E) as excinfo:
        String(min_length=2, max_length=2, pattern='[0-9]').validate('1')
    assert "Must have at least" in str(excinfo.value)

# Generated at 2022-06-14 14:25:48.409361
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    class Bool(Field):
        def validate(self, value, **kwargs):
            if value not in [True, False]:
                raise ValidationError("Not a boolean")
            return value
    b = Bool(default=True)
    assert b.get_default_value() == True
    b.default = False
    assert b.get_default_value() == False
    f = lambda: "foo"
    b.default = f
    assert b.get_default_value() == f()



# Generated at 2022-06-14 14:25:59.414195
# Unit test for method validate of class Array
def test_Array_validate():
    items = [Integer(minimum=1)]
    array = Array(items=items)

    # value = None
    with pytest.raises(ValidationError, match=r'^.*May not be null.*$'):
        array.validate(None)

    # value = "abc"
    with pytest.raises(ValidationError, match=r'^.*Must be an array.*$'):
        array.validate('abc')

    # value = [0]
    with pytest.raises(ValidationError, match=r'^.*Must be greater than or equal to 1.*$'):
        array.validate([0])

    # value = [1]
    result = array.validate([1])
    assert result == [1]


# Generated at 2022-06-14 14:26:03.919122
# Unit test for method validate of class Array
def test_Array_validate():
    items = [Field(required=True),Field(required=True)] #list(items)
    arr = Array(items=items) #(self, items: typing.Union[Field, typing.Sequence[Field]] = None, ...
    value = [2,2] #array of value
    error = None
    #returns nothing
    #arr.validate(value)
    assert arr.validate(value) is None


# Generated at 2022-06-14 14:26:07.855227
# Unit test for method validate of class Choice
def test_Choice_validate():
    choices = [("1","one"),("2","two")]
    choice = Choice(choices=choices)
    assert choice.validate("1") == "1"
    assert choice.validate("2") == "2"
    assert choice.validate("") == ""
    assert choice.validate("3") == "3"
    assert (choice.validate("") is None) == True

# Generated at 2022-06-14 14:26:12.150774
# Unit test for method validate of class Array
def test_Array_validate():
    obj = Array(
        items=Field(
            type="string",
        ),
    )
    assert obj.validate([]) == []
    assert obj.validate(["abc", "def", "ghi"]) == ["abc", "def", "ghi"]
    assert obj.validate([1, 2, 3]) == ["1", "2", "3"]

    obj = Array(
        items=Field(
            type="string",
        ),
        min_items=1
    )
    assert obj.validate([]) == []  # this should raise a validation error
    assert obj.validate(["abc", "def", "ghi"]) == ["abc", "def", "ghi"]
    assert obj.validate([1, 2, 3]) == ["1", "2", "3"]


# Generated at 2022-06-14 14:26:25.196043
# Unit test for method serialize of class String
def test_String_serialize():
    objString = String(title="test")
    assert objString.serialize("this is a test string") == "this is a test string"


# Generated at 2022-06-14 14:26:28.131622
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    field = Field(default = 1)
    assert field.get_default_value() == 1
    def default():
        return 2
    field = Field(default = default())
    assert field.get_default_value() == 2


# Generated at 2022-06-14 14:26:31.334420
# Unit test for constructor of class Const
def test_Const():
    value = True
    j = Const(value)
    assert j.to_primitive() == value


# Generated at 2022-06-14 14:26:37.859094
# Unit test for method validate of class Object
def test_Object_validate():
    # Instantiate an object to test
    testobj = Object()
    input_value = {
        "key1": "value1",
        "key2": "value2",
    }
    testobj.validate(input_value)

    # Instantiate an object to test
    testobj = Object()
    input_value = {
        "key1": "value1",
        "key2": "value2",
    }
    assert isinstance(input_value, (dict, typing.Mapping))


# Generated at 2022-06-14 14:26:43.780922
# Unit test for method validate of class Choice
def test_Choice_validate():
    # input = ("", ["a", "b", "c"])
    # output = ("", ["a", "b", "c"])
    # assert Choice.validate(input) == output
    assert Choice.validate(["a", "b", "c"]) == ["a", "b", "c"]



# Generated at 2022-06-14 14:26:44.856991
# Unit test for method __or__ of class Field
def test_Field___or__():
    field = Field()
    field.__or__(Field())
    # TODO: Implement unit test
    pass



# Generated at 2022-06-14 14:26:55.813010
# Unit test for method validate of class Choice
def test_Choice_validate():
    if __name__ == "__main__":
        # test_Choice_validate()
        c = Choice(choices=[('paper', 'Paper'), ('plastic', 'Plastic')], required=True, allow_null=False)
        try:
            print(c.validate(None))
        except ValidationError as e:
            print(e.text)
        try:
            print(c.validate(''))
        except ValidationError as e:
            print(e.text)
        try:
            print(c.validate('metal'))
        except ValidationError as e:
            print(e.text)
        try:
            print(c.validate('paper'))
        except ValidationError as e:
            print(e.text)

# Generated at 2022-06-14 14:27:00.506529
# Unit test for method validate of class Union
def test_Union_validate():
    # Create a new Context
    context = Context()

    # Create a new Union object
    a = Union([Any()], None)

    # Call method validate of Union object a
    try:
        a.validate(None, strict = False)
    except ValidationError as e:
        assert e.code() == "null"



# Generated at 2022-06-14 14:27:05.781555
# Unit test for method validate of class Union
def test_Union_validate():
    item_schema1=String
    item_schema2=Integer
    item_schema3=Union([item_schema1,item_schema2])
    item = item_schema3.validate(10)
    assert item == 10


# Generated at 2022-06-14 14:27:15.945862
# Unit test for method validate of class Union
def test_Union_validate():
    # Test the validate method of class Union
    my_string = String()  # create an instance of class String
    my_union = Union([my_string])  # create an instance of class Union with child string
    assert my_union.validate("test_string") == "test_string"  # validate
    my_integer = Integer()  # create an instance of class Integer
    my_union = Union([my_string, my_integer])  # create an instance of class Union with child string and integer
    assert my_union.validate(2) == 2  # validate
    my_boolean = Boolean()  # create an instance of class Boolean
    my_union = Union([my_string, my_integer, my_boolean])  # create an instance of class Union with child string, integer and boolean

# Generated at 2022-06-14 14:27:32.011677
# Unit test for method validate of class Union
def test_Union_validate():

    test1 = Field()
    test2 = Field()
    test3 = Union([test1, test2])
    validated = test3.validate([1])
    assert validated == True
    print('Test of method validate of class Union passed')

test_Union_validate()


# Generated at 2022-06-14 14:27:33.937549
# Unit test for method validate of class Union
def test_Union_validate():
    # Create an instance of class Union
    union_instance = Union([], allow_null = False)

    # Create a variable of type bool and assign it to result
    result = union_instance.validate(None, strict = False)

    # Check that the result of calling function validate is not None
    assert result is not None



# Generated at 2022-06-14 14:27:41.380911
# Unit test for method validate of class Union
def test_Union_validate():
    data = {"type": "object", "properties": {"a": {"type": "string"}}}
    s = Object(properties={"a": String()})
    s2 = String()
    union = Union([s, s2])
    value, error = union.validate_or_error('foo')
    assert value == 'foo'
    assert error is None
    
    value, error = union.validate_or_error(data)
    assert value == data
    assert error is None
    
    # TODO: error handling
test_Union_validate()



# Generated at 2022-06-14 14:27:45.982071
# Unit test for method validate of class Array
def test_Array_validate():
    obj = Array(
        min_items=None,
        max_items=None,
        items=None,
        additional_items=False,
        unique_items=False,
        allow_null=False,
        min_length=None,
        max_length=None,
    )
    assert obj.validate(["hello"]) == ["hello"]


# Generated at 2022-06-14 14:27:51.759488
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    f1 = Field(default="hi")
    assert f1.get_default_value() == "hi"
    f2 = Field(default=None)
    assert f2.get_default_value() == None
    f3 = Field(default=lambda: "hi")
    assert f3.get_default_value() == "hi"

# Generated at 2022-06-14 14:27:55.355833
# Unit test for method __or__ of class Field
def test_Field___or__():
    field1 = Field()
    field2 = Field()
    field3 = Field()
    union = field1 | field2 | field3
    assert union.any_of == [field1, field2, field3]



# Generated at 2022-06-14 14:27:56.231279
# Unit test for method validate of class Array
def test_Array_validate():
    a = Array()
    print(a.validate([1, 2, 3, 4]))



# Generated at 2022-06-14 14:28:03.952796
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    a = Field(_is_readonly=False, _is_required=False, _is_nullable=True, allow_null=False
)
    assert a.get_default_value() is None
    a = Field(_is_readonly=False, _is_required=False, _is_nullable=False, allow_null=True
)
    assert type(a.get_default_value()) is not None
    a = Field(_is_readonly=False, _is_required=False, _is_nullable=False, allow_null=True
)
    assert a.get_default_value() is None



# Generated at 2022-06-14 14:28:10.846139
# Unit test for method validate of class Union
def test_Union_validate():
    from . import String, Integer, Bool, Null

    class TestUnionField(Union):
        def __init__(self, **kwargs) -> None:
            super().__init__(
                any_of=[
                    Bool(**kwargs),
                    String(**kwargs),
                    Integer(**kwargs),
                    Null(**kwargs),
                ],
                **kwargs,
            )

    field = TestUnionField()
    value = 'test'
    error = field.validate_or_error('test')
    assert error[1] == None and error[0] == 'test', 'test 1 failed'
    
    value = False
    error = field.validate_or_error(False)
    assert error[1] == None and error[0] == False, 'test 2 failed'

    value = 7


# Generated at 2022-06-14 14:28:14.174466
# Unit test for constructor of class Array
def test_Array():
    items = int()
    additional_items = bool()
    min_items = 3
    max_items = 3
    unique_items = True
    test_array = Array(items=items, additional_items=additional_items, min_items=min_items, max_items=max_items, unique_items=unique_items)
    assert test_array.items is not None
    assert test_array.additional_items is not None
    assert test_array.min_items is not None
    assert test_array.max_items is not None
    assert test_array.unique_items is not False


# Generated at 2022-06-14 14:28:33.951894
# Unit test for method validate of class Array
def test_Array_validate():
    validator = Array(items=[Integer(), Integer()])
    value = validator.validate([1, 2])
    print(value)
    
test_Array_validate()


# Generated at 2022-06-14 14:28:41.963436
# Unit test for method validate of class String
def test_String_validate():
    assert String(title = '', description = '', allow_blank = False, trim_whitespace = True, max_length = None, min_length = None, pattern = None, format = None).validate('a') == 'a'
    assert String(title = '', description = '', allow_blank = False, trim_whitespace = True, max_length = None, min_length = None, pattern = None, format = None).validate('', strict=True) == None

    s1 = String(title = '', description = '', allow_blank = False, trim_whitespace = True, max_length = 3, min_length = 2, pattern = None, format = None)
    assert s1.validate('a') == None
    assert s1.validate('abc') == 'abc'

# Generated at 2022-06-14 14:28:47.600456
# Unit test for method validate of class Choice
def test_Choice_validate():
    number_choices = Choice(
        name="number_choices",
        choices=[("1", 1), ("2", 2), ("3", 3)],
        allow_null=True,
        allow_blank=False,
    )

    value_validate = number_choices.validate(1)
    assert value_validate == 1



# Generated at 2022-06-14 14:28:59.839520
# Unit test for method validate of class Object

# Generated at 2022-06-14 14:29:07.735571
# Unit test for method validate of class Choice
def test_Choice_validate():
    field = Choice(allow_null=True, choices = [("A", "a"),("B", "b"),("C", "c")])
    assert field.validate("A") == "A"
    assert field.validate("B") == "B"
    assert field.validate("C") == "C"
    assert field.validate("a") == "A"
    assert field.validate("b") == "B"
    assert field.validate("c") == "C"
    assert field.validate("d") == "choice"
    assert field.validate("") == "required"
    assert field.validate("null") == "null"



# Generated at 2022-06-14 14:29:18.540136
# Unit test for method validate of class Union
def test_Union_validate():
    # Test case 1
    def test_case_1():
        print("Begin test case 1")
        # Test 1
        schema = Union(
        [
            Integer(min_value=0, max_value=100, exclusive_max=True),
            Boolean()
        ]
        )
        try:
            schema.validate(100)
        except ValidationError as e:
            print(e.messages())
            assert e.messages() == [{'index': [], 'code': 'max_value', 'text': 'Must have a value less than 100.'}]
        print("End test case 1")
    # Test case 2
    def test_case_2():
        print("Begin test case 2")
        # Test 1

# Generated at 2022-06-14 14:29:21.744533
# Unit test for constructor of class Const
def test_Const():
    try:
        Const(1.0)
    except AssertionError:
        pass
    else:
        raise AssertionError("Did not raise AssertionError")


# Generated at 2022-06-14 14:29:31.259924
# Unit test for method validate of class Number
def test_Number_validate():
    result1 = Number().validate(2)
    result2 = Number().validate("2")
    result3 = Number().validate(None)
    result4 = Number().validate(float(2))
    result5 = Number().validate(2.0)
    result6 = Number().validate(float(2.0))
    result7 = Number().validate(2.02)
    result8 = Number().validate(float(2.02))
    result9 = Number().validate(27)
    result10 = Number().validate(27.0)
    result11 = Number().validate(float(27))
    result12 = Number().validate(float(27.0))
    result13 = Number().validate(27.27)
    result14 = Number().validate(float(27.27))
    result15

# Generated at 2022-06-14 14:29:38.294520
# Unit test for method validate of class Choice
def test_Choice_validate():
  choice = Choice(allow_null = True, allow_blank = True)
  assert choice.validate(None) == None
  assert choice.validate("text") == "text"
  try:
    choice.validate(None)
  except:
    assert True
  else:
    assert False
  try:
    choice.validate(None)
  except:
    assert True
  else:
    assert False


# Generated at 2022-06-14 14:29:46.444799
# Unit test for method validate of class Object
def test_Object_validate():
    # for additional_properties: True
    # for additional_properties: False
    # for additional_properties not None, False and True
    from pydantic import Field, Object, ValidationError
    from pydantic.fields import StringField
    from pydantic.error_wrappers import ValidationError
    
    class Model1(Object):
        properties = {'key1': StringField()}
        additional_properties = True
        
    assert Model1({'key1':'value1'}).key1 == 'value1'
    
    class Model2(Object):
        properties = {'key2': StringField()}
        additional_properties = False

    assert Model2({'key2':'value2'}).key2 == 'value2'
    

# Generated at 2022-06-14 14:30:07.267359
# Unit test for method validate of class String
def test_String_validate():
    a=String(title="abc")
    try:
        assert a.validate(None) == None
    except:
        print("Error:\nmethod validate of class String")


# Generated at 2022-06-14 14:30:12.848255
# Unit test for constructor of class String
def test_String():
    st = String(title="String",
                description="A string",
                default="abcd",
                allow_blank=True,
                trim_whitespace=True,
                min_length=2,
                max_length=10,
                pattern=r"^[a-zA-z0-9_.]+$")
    


# Generated at 2022-06-14 14:30:22.238038
# Unit test for method validate of class Array
def test_Array_validate():
    obj = Array(items=None, additional_items=False, min_items=None, max_items=None, unique_items=False)
    assert obj.validate([]) == [], 'assert #1 has failed'
    assert obj.validate([1,2,3]) == [1,2,3], 'assert #2 has failed'
    assert obj.validate([{'i': 1}, {'j': 2}, {'k': 3}]) == [{'i': 1}, {'j': 2}, {'k': 3}], 'assert #3 has failed'
    assert obj.validate([{'i': 1}, {'j': 2, 'k': 3}]) == [{'i': 1}, {'j': 2, 'k': 3}], 'assert #4 has failed'

test_Array_validate()



# Generated at 2022-06-14 14:30:24.872298
# Unit test for method validate of class Choice
def test_Choice_validate():
    obj1 = Choice(choices=['toto'])
    assert obj1.validate('toto') == 'toto', "setting choices failed"
    obj2 = Choice()
    with pytest.raises(ValidationError):
        obj2.validate('toto')



# Generated at 2022-06-14 14:30:34.063248
# Unit test for method validate of class Choice
def test_Choice_validate():
    ch = Choice(choices=["a", "b"])
    assert ch.validate(value="a") == "a"
    assert ch.validate(value="b") == "b"
    assert ch.validate(value=None) == None
    assert ch.validate(value="") == ""
    try:
        ch.validate(value="c", strict=False)
        assert False
    except ValidationError:
        assert True
    try:
        ch.validate(value="c", strict=True)
        assert False
    except ValidationError:
        assert True
    try:
        ch = Choice(choices=None, allow_null=False)
        ch.validate(value=None)
        assert True
    except ValidationError:
        assert False




# Generated at 2022-06-14 14:30:37.791290
# Unit test for constructor of class Const
def test_Const():
    Const(const="one")
    Const(const=1)
    Const(const=1.0)
    Const(const=None)
    Const(const=[])
    Const(const={})

# Generated at 2022-06-14 14:30:44.481757
# Unit test for method validate of class Choice
def test_Choice_validate():
    assert Choice(choices=[("name1","name1_value")]).validate("name1_value") == "name1_value"
    assert Choice(choices=[("name1","name1_value")]).validate("name1") == "name1"


# Generated at 2022-06-14 14:30:49.625773
# Unit test for method validate of class Choice
def test_Choice_validate():
    x = Choice(choices = [('A', 'A'), ('B', 'B')])
    # case 1
    assert x.validate('A') == 'A'
    # case 2
    assert x.validate('B') == 'B'
    # case 3
    assert x.validate('abcd') == 'abcd'
    # case 4
    assert x.validate('') == ''
    


# Generated at 2022-06-14 14:30:54.517621
# Unit test for method validate of class Choice
def test_Choice_validate():
    field = Choice(choices=[('s', '1'), ('s2', '2'), ('s3', '3')])
    assert field.validate('s') == 's'
    assert field.validate('s2') == 's2'
    assert field.validate('s3') == 's3'
    assert field.validate('') == None
    assert field.validate(None) == None

test_Choice_validate()



# Generated at 2022-06-14 14:31:00.784124
# Unit test for method validate of class String
def test_String_validate():
    a_test = String(default=None)
    assert a_test.validate(None)    == None
    assert a_test.validate('')      == ''
    assert a_test.validate('testing') == 'testing'
    try:
        a_test.validate(3)
        assert False
    except Exception:
        pass


# Generated at 2022-06-14 14:31:11.681355
# Unit test for method validate of class Number
def test_Number_validate():
    number = Number(minimum = 2,maximum = 9)
    print(number.validate(8))
    # try:
    #     number.validate(8)
    # except ValidationError as e:
    #     print(e.code)
    #     print(e.text)



# Generated at 2022-06-14 14:31:19.419182
# Unit test for method validate of class Union
def test_Union_validate():
    # Test the base case of the Union class (correct value)
    schema = Union([Integer, Number, String], allow_null=False)
    value = 5
    output, error = schema.validate_or_error(value)
    print(output)
    # Test the base case of the Union class (error, null)
    schema = Union([Integer, Number, String], allow_null=False)
    value = None
    output, error = schema.validate_or_error(value)
    print(error)
    # Test the base case of the Union class (error, union)
    schema = Union([Integer, Number, String], allow_null=False)
    value = "a"
    output, error = schema.validate_or_error(value)
    print(error)


# Generated at 2022-06-14 14:31:29.250782
# Unit test for method validate of class Number
def test_Number_validate():
    a = Number(allow_null=False)
    b = Number(allow_null=True)
    c = Number(allow_null=True,allow_blank=True)

    # test case 1: null value and not allow null
    try:
        a.validate(None)
    except ValidationError as e:
        print(e.text)
    # output: May not be null.

    # test case 2: null value and allow null
    print(
        b.validate(None) 
    )  # output: None

    # test case 3: empty string and allow null
    try:
        print(
            b.validate("")
        ) # output: Must be a number.
    except ValidationError as e:
        print(e.text)

    # test case 4: empty string and allow null and allow blank

# Generated at 2022-06-14 14:31:35.533121
# Unit test for constructor of class Const
def test_Const():
    const_1 = Const(const="hh")
    const_2 = Const(const=["hello"])
    const_3 = Const(const=None)
    const_4 = Const(const=1)

    # test when value not equal to const, then the validation error
    #  is raised and thus, the error message is returned
    assert const_1.validate("hh") == "hh"
    assert const_2.validate(["hello"]) == ["hello"]
    assert const_3.validate(None) is None
    assert const_4.validate(1) == 1
    try:
        assert const_1.validate("hello")
    except ValidationError as error:
        assert error.messages()[0].code == "const"


# Generated at 2022-06-14 14:31:37.118414
# Unit test for method validate of class Choice
def test_Choice_validate():
        assert Choice(choices=[
        "a",
        ("b", "B"),
        {"c": "C"},
        ("d", {"d": "D"}),
    ]).validate("a") == "a"



# Generated at 2022-06-14 14:31:43.190976
# Unit test for method validate of class Array
def test_Array_validate():
    error_messages = [{'code': 'unique_items', 'key': 0, 'text': 'Items must be unique.'},
     {'code': 'unique_items', 'key': 1, 'text': 'Items must be unique.'}]
    passed = True
    test_array = Array(unique_items=True)
    try:
        test_array.validate([1, 1])
    except ValidationError as e:
        if (e.messages() != error_messages):
            passed = False
    assert passed

test_Array_validate()

# Generated at 2022-06-14 14:31:54.955814
# Unit test for method validate of class Array
def test_Array_validate():
    from pydantic.error_wrappers import ValidationError
    from pydantic import BaseModel
    from ._array import Array
    from ._field import Field
    from ._message import Message
    from ._object import Object
    from ._validator import Validator

# Generated at 2022-06-14 14:32:01.874391
# Unit test for method validate of class Union
def test_Union_validate():
    # Case 1: match of the value is successful
    schema = Union([String(max_length=5),Integer()],allow_null=True)

    value = 5
    child, error = schema.validate_or_error(value)

    assert child==5
    assert error==None

    # Case 2: match of the value is unsuccessful and so the error is raised again
    schema = Union([String(max_length=5),Integer(minimum=10)],allow_null=True)

    value = 5
    with pytest.raises(ValidationError) as e:
        schema.validate(value)

    assert str(e.value.messages[0]) == "Must be at least 10."

    # Case 3: match of the value is unsuccessful and no error is raised
    # hence new error is raised


# Generated at 2022-06-14 14:32:07.435605
# Unit test for method validate of class Choice
def test_Choice_validate():
    choice = Choice()
    assert choice.validate(None) == None
    choice2 = Choice(choices=[(2,"good"),(3,"bad")])
    assert choice2.validate(2) == 2
    assert choice2.validate(3) == 3
    assert choice2.validate(5) == "5 not in Uniqueness([2, 3])"



# Generated at 2022-06-14 14:32:09.950820
# Unit test for constructor of class String
def test_String():
    field = String()
    assert field.validate(1) == None
    assert field.validate(None) == None
    assert field.validate('') == None
    assert field.validate('hello') == 'hello'



# Generated at 2022-06-14 14:32:17.397124
# Unit test for method validate of class Choice
def test_Choice_validate():
    assert Choice(choices=["1","2"], allow_null=False).validate("1") == "1"



# Generated at 2022-06-14 14:32:25.286567
# Unit test for method validate of class Choice
def test_Choice_validate():
    choice1 = Choice(choices=["yes", "no"])
    try: 
        choice1.validate("y")
        assert(False)
    except ValidationError :
        assert(True)

    choice2 = Choice(choices=["yes", "no"])
    try: 
        choice2.validate(1)
        assert(False)
    except ValidationError:
        assert(True)

    choice3 = Choice(choices=["yes", "no"])
    try:
        choice3.validate(None)
        assert(False)
    except ValidationError:
        assert(True)

    choice4 = Choice(choices=["yes", "no"])
    assert(choice4.validate("yes") == "yes")



# Generated at 2022-06-14 14:32:36.503288
# Unit test for method validate of class Object

# Generated at 2022-06-14 14:32:47.364033
# Unit test for method validate of class Array
def test_Array_validate():
    err_messages = []
    def err_message_handler(message: Message) -> None:
        err_messages.append(message)
    string = String(min_length=1, max_length=10, error_handler=err_message_handler)
    a = Array(items=string, max_items=1)
    assert a.validate(["Rachit"]) == ["Rachit"]
    assert a.validate(["Rachit", "Gupta"]) == ["Rachit"]
    assert err_messages[0].text == "Must have no more than 1 items."
    assert err_messages[0].index == [1]
    assert err_messages[0].code == "max_items"

# Generated at 2022-06-14 14:32:52.018391
# Unit test for method validate of class String
def test_String_validate():
    value = String(default="test")
    try:
        number = 1
        value.validate(number)
    except ValidationError:
        print("An expected validation error has occurred")
    except Exception:
        print("An unexpected error has occurred")
    finally:
        value.validate("test")
        print("\ttest_String_validate successed")


# Generated at 2022-06-14 14:32:57.056250
# Unit test for method validate of class Choice
def test_Choice_validate():
    c = Choice(choices=["true", "false"])
    c.validate("true") == "true"
    c.validate("false") == "false"
    c.validate("T") == "choice"
    c.validate("F") == "choice"



# Generated at 2022-06-14 14:33:09.724467
# Unit test for method validate of class Object
def test_Object_validate():
    # 1. normal use case
    test_data = {
        "key1": "value1",
        "key2": "value2"
    }
    res = Object(properties={
        "key1": String(),
        "key2": String()
    }).validate(test_data)
    assert res['key1'] == 'value1'
    assert res['key2'] == 'value2'

    # 2. null case
    res = Object(properties={
        "key1": String(),
        "key2": String()
    },allow_null=True).validate(None)
    assert res == None
    
    # 3. empty object
    res = Object(properties={
        "key1": String(),
        "key2": String()
    },allow_null=False,min_properties='1').validate

# Generated at 2022-06-14 14:33:14.236570
# Unit test for method validate of class String
def test_String_validate():
    string = String(title = "String", description = "String Description")
    print(string.validate("Sample String"))
    #pprint(string.__dict__)
    
test_String_validate()
