

# Generated at 2022-06-14 14:25:20.312244
# Unit test for method __or__ of class Field
def test_Field___or__():
    str_field = String()
    int_field = Integer()
    bool_field = Boolean()

    assert str_field.validate("a") == str_field | str_field
    assert str_field.validate("a") == str_field | str_field | str_field
    assert str_field.validate("a") == (str_field | int_field) | str_field
    assert int_field.validate(1) == (str_field | int_field) | int_field
    assert Field.validation_error("null_error").message == (str_field | bool_field).validate(None).error.message



# Generated at 2022-06-14 14:25:29.903097
# Unit test for method validate of class Boolean
def test_Boolean_validate():
    field = Boolean()
    assert field.validate(None) == None
    assert field.validate(True) == True
    assert field.validate(False) == False
    assert field.validate('true') == True
    assert field.validate('false') == False
    assert field.validate('on') == True
    assert field.validate('off') == False
    assert field.validate('1') == True
    assert field.validate('0') == False
    assert field.validate('-1') == False
    assert field.validate('5') == False
    assert field.validate(1) == True
    assert field.validate(0) == False
    assert field.validate(-1) == False
    assert field.validate(5) == False
    assert field.validate('none') == False



# Generated at 2022-06-14 14:25:35.954329
# Unit test for constructor of class Array
def test_Array():
    print(Array())
    print(Array(additional_items=False, items=[Boolean()]))
    print(Array(additional_items=Boolean(), items=Boolean()))
    print(Array(additional_items=True, unique_items=True))
    print(Array(additional_items=False, items=[Boolean(), String()], unique_items=True))
    print(Array(additional_items=Boolean(), items=String(), unique_items=True))



# Generated at 2022-06-14 14:25:45.415628
# Unit test for method validate of class Union
def test_Union_validate():
    assert_namedtuple_equal(
        Union([]).validate(3),
        Union([]).validate({}),
        Union([]).validate(None),
        Union([]).validate(''),
        Union([]).validate(b''),
        Union([]).validate([]),
        Union([]).validate(()),
    )
    assert_namedtuple_equal(
        Union([Any(), Any(), Any(), Any()]).validate('hello'),
        Union([Any()]).validate('hello'),
        Union([Any(), String()]).validate('hello'),
    )



# Generated at 2022-06-14 14:25:54.470869
# Unit test for method validate of class String
def test_String_validate():
    str1 = "abc"
    str2 = "a"
    str3 = ""
    str4 = "a"

    field1 = String(allow_blank=False, allow_null=False, max_length=100,min_length=1,pattern=None,format=None)
    assert field1.validate(str1) == "abc"
    assert field1.validate(str2) == "a"
    assert field1.validate(str3) == ""
    assert field1.validate(str4) == "a"



# Generated at 2022-06-14 14:26:00.184613
# Unit test for method serialize of class String
def test_String_serialize():
    string = String()
    assert string.serialize(None) == None
    assert string.serialize("") == ""
    assert string.serialize("test") == "test"
    assert string.serialize(123) == 123
    assert string.serialize(True) == True
    assert string.serialize(False) == False
    assert string.serialize([]) == []
    assert string.serialize({}) == {}



# Generated at 2022-06-14 14:26:06.833628
# Unit test for method validate of class Array
def test_Array_validate():
    field = Array()
    assert field.validate([1, 2]) == [1, 2]
    assert field.validate([1, 2, 3]) == [1, 2, 3]
    assert field.validate([]) == []

    assert field.validate(None) == None

    # In case of strict flag, the value must be a list
    with pytest.raises(ValidationError):
        field.validate(None, strict=True)

    with pytest.raises(ValidationError):
        field.validate({}, strict=True)

    with pytest.raises(ValidationError):
        field.validate(1, strict=True)

    with pytest.raises(ValidationError):
        field.validate("1", strict=True)

    # Items

# Generated at 2022-06-14 14:26:17.489138
# Unit test for method validate of class Choice
def test_Choice_validate():
    field = Choice(choices = [(1, '苹果'), (2, '香蕉')])
    assert field.validate(1) == 1
    assert field.validate('1') == 1
    assert field.validate(2) == 2
    assert field.validate('') == ''
    field = Choice(choices = [(1, '苹果'), (2, '香蕉')], validate_choices=True)
    assert field.validate(1) == 1
    assert field.validate('1') == 1
    assert field.validate(2) == 2
    try:
        field.validate(3)
    except ValidationError as err:
        assert err is not None

# Generated at 2022-06-14 14:26:23.867467
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    """
    Unit test for method get_default_value of class Field
    """
    f = Field(default = "abc")
    assert f.get_default_value() == "abc"
    f = Field(default = lambda: "xyz")
    assert f.get_default_value() == "xyz"


# Generated at 2022-06-14 14:26:28.157399
# Unit test for method validate of class Object
def test_Object_validate():
    from pydantic import BaseModel

    class City(BaseModel):
        name: str
        population: int
        area: int
        latitude: float
        longitude: float

    class State(BaseModel):
        name: str
        cities: typing.Dict[str, City]
        area: int

    State.schema()

    class Top(BaseModel):
        states: typing.Mapping[str, State]


# Generated at 2022-06-14 14:27:09.975353
# Unit test for method validate_or_error of class Field
def test_Field_validate_or_error():
    string = String()
    result = string.validate_or_error("123")
    assert result.value == "123"
    assert result.error is None



# Generated at 2022-06-14 14:27:12.912270
# Unit test for method serialize of class Array
def test_Array_serialize():
    schema = Array(items = Number())
    assert schema.serialize(obj = None) == None
    assert schema.serialize(obj = [1,3,5]) == [1,3,5]


# Generated at 2022-06-14 14:27:21.828721
# Unit test for constructor of class Const
def test_Const():
    json_schema = {
        'type': 'object',
        'properties': {
            'str_prop': {'type': 'string', 'const': 'const'},
            'bool_prop': {'type': 'boolean', 'const': False},
            'int_prop': {'type': 'integer', 'const': 42},
            'num_prop': {'type': 'number', 'const': 42.0},
            'null_prop': {'type': 'null', 'const': True},
            'union_prop': {
                'anyOf': [{
                    'type': 'string',
                    'const': 'str_val'
                }, {
                    'type': 'number',
                    'const': 42.0
                }]
            }
        }
    }
    str_schema = json.dumps

# Generated at 2022-06-14 14:27:26.096679
# Unit test for method validate of class Array
def test_Array_validate():
    schema = Array(min_items=1, items=Integer(minimum=0, maximum=10))
    assert schema.validate([1,2]) == [1,2]
    assert schema.validate([]) == None
    assert schema.validate('a') == None

# Generated at 2022-06-14 14:27:34.523366
# Unit test for method validate of class Union
def test_Union_validate():
    assert Union([String(allow_null=True)]).validate(None) is None # We can call this because self.allow_null is True

    field = Union([String(allow_null=True), Boolean()])
    assert field.validate("value") == "value" # Union returns the value if no error occurs
    assert field.validate(True) is True
    try:
        field.validate(None) 
    except Exception as e:
        assert isinstance(e, ValidationError)
        assert e.messages()[0].code == "union" # If no error, we raise an error: "union"


# Generated at 2022-06-14 14:27:43.039882
# Unit test for method validate of class Array

# Generated at 2022-06-14 14:27:46.033904
# Unit test for method validate_or_error of class Field
def test_Field_validate_or_error():
    assert Field().validate_or_error("Ying Tong") == ValidationResult(value=None, error=ValidationError('Field validation error', code='error'))

# Generated at 2022-06-14 14:27:58.325022
# Unit test for method validate of class String
def test_String_validate():
    # Case 1
    def validate(value, *, strict=False):
        return value
    f = Field(title="",description="",default=NO_DEFAULT,allow_null=True)
    f._creation_counter = 0
    s = String(allow_blank=False,trim_whitespace=True,max_length=5,min_length=5,pattern=None,format=None,title="",description="",default=NO_DEFAULT,allow_null=True)
    assert s.validate("bob") == "bob"
    assert s.validate("bob", strict=True) == "bob"
    assert s.validate("bob", strict=False) == "bob"
    assert s.validate("bob", strict="bob") == "bob"
    assert s.validate

# Generated at 2022-06-14 14:28:02.667689
# Unit test for method __or__ of class Field
def test_Field___or__():
    assert(
        (Field(title="test") | Field(title="testtest")).any_of
        == [Field(title="test"), Field(title="testtest")]
    )
    assert(Field(title="test") | Field(title="test")).any_of == [Field(title="test")]


# Generated at 2022-06-14 14:28:09.598104
# Unit test for method validate of class Object
def test_Object_validate():
    # Create field
    params={}
    params['properties']={'key1':Integer(),'key2':Float()}
    params['required']=[]
    params['allow_null']=True
    params['default']={'key1':1,'key2':2.5}
    params['additional_properties']=False
    params['min_properties']=1
    params['max_properties']=2
    params['property_names']=None
    params['pattern_properties']=None
    field = Object(**params)
    
    # Test validate with val=None, strict=False
    val = None
    strict = False
    expected = None
    observed = field.validate(val, strict = strict)
    assert observed == expected
    # Test validate with val=None, strict=True, should raise error

# Generated at 2022-06-14 14:28:26.146022
# Unit test for method validate of class String
def test_String_validate():
    # Tests for method validate of class String
    title = "test"
    assert String(title=title).validate("test") == "test"


# Generated at 2022-06-14 14:28:33.771756
# Unit test for method validate of class String
def test_String_validate():
    my_field = String(title='my_field', description='my_field', allow_blank=False,trim_whitespace=True, max_length=2, min_length=0, pattern=None, format="date")
    # Test case 1
    input_value = "2020-04-22"
    output_value_expected = datetime.date(2020, 4, 22)
    output_value = my_field.validate(input_value, strict=False)
    assert output_value == output_value_expected
    # Test case 2
    input_value = None
    output_value_expected = None
    output_value = my_field.validate(input_value, strict=False)
    assert output_value == output_value_expected
    # Test case 3
    input_value = "2020-04-00"

# Generated at 2022-06-14 14:28:41.805590
# Unit test for constructor of class Const
def test_Const():
    f = Const(
        const=5.5,
        title="const test",
        description="test description",
        example=5.5,
        constant=5.5,
    )

    # Test for constructor of class Const
    assert f.const == 5.5
    assert f.title == "const test"
    assert f.description == "test description"
    assert f.example == 5.5
    assert f.constant == 5.5

    # Test for method validate() of class Const
    assert f.validate(5.5) == 5.5


# Generated at 2022-06-14 14:28:53.885139
# Unit test for method validate of class Number
def test_Number_validate():
    fn = Number()
    value = fn.validate(1)
    assert value == 1
    value = fn.validate("-2")
    assert value == -2
    try:
        value = fn.validate("null")
    except ValidationError as err:
        assert err.code == "type"
    try:
        value = fn.validate("")
    except ValidationError as err:
        assert err.code == "type"
    try:
        value = fn.validate("-inf")
    except ValidationError as err:
        assert err.code == "type"
    try:
        value = fn.validate("nan")
    except ValidationError as err:
        assert err.code == "type"
    value = fn.validate("1.1")
    assert value == decimal.Decimal

# Generated at 2022-06-14 14:29:01.970900
# Unit test for method validate of class Array
def test_Array_validate():
    my_array = Array(
        items=[
            String(max_length=10, min_length=3),
            Integer(maximum=3, minimum=1),
        ],
        additional_items=Boolean(),
        unique_items=True,
    )
    value = [1, 2, 3, 4, True, False, True]
    expected = [1, 2, 3, True, False, True]
    assert my_array.validate(value=value) == expected



# Generated at 2022-06-14 14:29:10.152532
# Unit test for method validate of class Union
def test_Union_validate():
    field = Union([
        Integer(minimum=0),
        Array(min_items=3, unique_items=True, items=[
            Integer(minimum=0, maximum=999),
            Integer(minimum=0, maximum=999),
            Integer(minimum=0, maximum=999)])
    ])
    print(field.validate(5)) #return 5
    print(field.validate([1,2,3])) #return [1, 2, 3]
    print(field.validate([1,2,1])) #return [1, 2, 1]
    print(field.validate([1,2,1,4])) #return [1, 2, 1, 4]
    print(field.validate([1,2,1,4,5]))

# Generated at 2022-06-14 14:29:15.478800
# Unit test for method validate of class Union
def test_Union_validate():
    import ipdb
    ipdb.set_trace()
    # input value which can be of type string (hello) or int (100)
    value=100
    # Define the two types
    e1 = String() 
    e2 = Number() 
    # create an union of these two types
    u = Union([e1, e2]) 
    # Validate the input value
    result=u.validate(value)
    assert result==100
    # Define an input value of type string (hello)
    value="hello"
    # Validate the input value
    result=u.validate(value)
    assert result=="hello"


# Generated at 2022-06-14 14:29:18.071966
# Unit test for constructor of class String
def test_String():
    String(title='string', description='string', default='string', allow_null=True)


# Generated at 2022-06-14 14:29:23.306104
# Unit test for method validate of class Union
def test_Union_validate():
    # Setup
    u = Union([Boolean()], allow_null = False)
    # Assert
    assert u.validate(True) == True
    assert u.validate(1) == 1
    assert u.validate(False) == False
    assert u.validate(0) == 0
    assert u.validate(None) == None

# Generated at 2022-06-14 14:29:26.828438
# Unit test for constructor of class Const
def test_Const():
    try:
        print("Testing Const constructor...", end="")
        const = Const(True)
        assert(const.allow_null == False)
        print("Passed!")
    except Exception:
        print("Failed")


# Generated at 2022-06-14 14:29:44.009312
# Unit test for method validate of class Array
def test_Array_validate():
    a = [1, 2, 3, 4, 5]
    b = [1, 2, 3, 4, 5, 6] 
    c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    d, e = [], [1, 2, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    f, g = [], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2]
    h = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Generated at 2022-06-14 14:29:49.252364
# Unit test for method validate of class Choice
def test_Choice_validate():
    dic = [('A','A'),('B','B'),('C','C')]
    choice = Choice(choices = dic)
    assert choice.validate(value = 'A') == 'A'
    assert choice.validate(value = 'B') == 'B'
    assert choice.validate(value = 'C') == 'C'
    assert choice.validate(value = 'D') == 'D'
    assert choice.validate(value = None) == None
    assert choice.validate(value = '') == None
    try:
        choice.validate(value = '')
        assert None
    except ValidationError as error:
        assert error.code == 'required'


# Generated at 2022-06-14 14:29:52.823584
# Unit test for method validate of class Choice
def test_Choice_validate():
    c = Choice(choices=[("a", "A"), ("b", "B")], allow_null=True)
    c.validate("a")
    c.validate("b")
    try:
        c.validate("c")
        assert False, "Expected ValueError"
    except ValidationError:
        pass
    try:
        c.validate(None)
        assert False, "Expected ValueError"
    except ValidationError:
        pass



# Generated at 2022-06-14 14:29:55.946903
# Unit test for method validate of class Array
def test_Array_validate():
    items = [
        Integer(),
        Integer(),
    ]
    my_array= Array(items=items)
    my_array.validate([1, 2])
    my_array.validate([1, "2"])



# Generated at 2022-06-14 14:30:00.153399
# Unit test for constructor of class Const
def test_Const():
    c = Const(const=0)
    assert c.const == 0
    assert c.allow_null == False
    c = Const(const=0, allow_null=True)
    assert c.allow_null == True
# End unit test for constructor of class Const


# Generated at 2022-06-14 14:30:13.302720
# Unit test for method validate of class Choice
def test_Choice_validate():
    field_object = Choice(name='Test_Choice',choices=[('1','Val_1'),('2','Val_2'),('3','Val_3')])
    print('Test_1: Test input: ("1")')
    assert field_object.validate("1")=='1', "Test failed!"
    print('Test_1: Test output: Val_1')
    print('Test_2: Test input: (1)')
    assert field_object.validate(1)==1, "Test failed!"
    print('Test_2: Test output: Val_1')
    print('Test_3: Test input: ("4")')
    try:
        assert field_object.validate("4")==None, "Test failed!"
    except :
        print('Test_3: Test output: Not a valid choice')

test_

# Generated at 2022-06-14 14:30:17.553341
# Unit test for method __or__ of class Field
def test_Field___or__():
    class MyField(Field):
        pass
    class OtherField(Field):
        pass
    f1 = MyField()
    f2 = OtherField()
    f3 = f1 | f2
    print(type(f3))
    print(f3.any_of)


# Generated at 2022-06-14 14:30:21.035440
# Unit test for method validate of class String
def test_String_validate():
    test_obj = String(allow_blank=False, format="time")
    test_value = "03:15:55 PM"
    test_result = test_obj.validate(test_value)
    assert test_result == "15:15:55"

# Generated at 2022-06-14 14:30:26.181131
# Unit test for method validate of class String
def test_String_validate():
    string_one = String(title= "first name", description= "Student's first name",default= 'None', allow_null= False)
    assert string_one.validate("Uma") == "Uma"
    assert string_one.validate(None) == "None"


# Generated at 2022-06-14 14:30:26.935717
# Unit test for method validate of class Array
def test_Array_validate():
    pass

# Generated at 2022-06-14 14:30:48.121598
# Unit test for method __or__ of class Field
def test_Field___or__():
    assert Field() | Field() == Union([Field(), Field()])



# Generated at 2022-06-14 14:30:55.700849
# Unit test for method validate of class Array
def test_Array_validate():
    array1 = Array(items = String(), exact_items = 2)
    try:
        array1.validate(None)
    except ValidationError as e:
        assert e.messages()[0].code == "null"
        assert e.messages()[0].text == "May not be null."
    try:
        array1.validate(42)
    except ValidationError as e:
        assert e.messages()[0].code == "type"
        assert e.messages()[0].text == "Must be an array."
    try:
        array1.validate(['1', 2])
    except ValidationError as e:
        assert e.messages()[0].code == "type"
        assert e.messages()[0].text == "Must be a string."

# Generated at 2022-06-14 14:31:04.983478
# Unit test for method validate of class Number
def test_Number_validate():
    test1 = Number(minimum = 1,maximum = 10,multiple_of=2,precision='2')
    result1 = test1.validate(10)
    assert result1 == 10

    test2 = Number(minimum = 1,maximum = 10,multiple_of=2,precision='2')
    result2 = test2.validate(9)
    assert result2 == 10
# End of unit test for method validate of class Number
    def __repr__(self) -> str:
        return "Number()"

    def __str__(self) -> str:
        return "Number()"



# Generated at 2022-06-14 14:31:10.945268
# Unit test for method validate of class Union
def test_Union_validate():
    fields = []
    fields.append(Field(type="number"))
    fields.append(Field(type="integer"))

    schema = Union(fields)
    validated, error = schema.validate_or_error(1)
    assert validated == 1
    assert error is None
    validated, error = schema.validate_or_error(1.2)
    assert validated == 1.2
    assert error is None
    validated, error = schema.validate_or_error('1')
    assert error is not None
    assert error.messages()[0].code == 'type'

# Generated at 2022-06-14 14:31:12.661446
# Unit test for constructor of class Const
def test_Const():
    d = Const(None)
    assert d.const == None
    assert d.allow_null == True

# Generated at 2022-06-14 14:31:17.150503
# Unit test for constructor of class Const
def test_Const():
    const = Const(const="test")
    assert const.const == "test"
    assert const.allow_null == False
    try:
        const = Const(const="test", allow_null=True)
        assert False
    except AssertionError:
        assert True
    const2 = Const(const=None, allow_null=True)
    assert const2.const == None
    assert const2.allow_null == True

# Generated at 2022-06-14 14:31:27.795495
# Unit test for method validate of class Union
def test_Union_validate():
    number_field = Number() 
    string_field = String()
    fields = [number_field, string_field]
    union_field = Union(fields)
    assert union_field.validate(3.14) == 3.14
    assert union_field.validate("hello") == "hello"
    try:
        union_field.validate(True)
        assert(False)
    except ValidationError as error:
        assert error.code == "union"
 
    string_field.allow_null = True
    union_field = Union(fields)
    assert union_field.validate(None) is None
    assert union_field.validate("hello") == "hello"

# Generated at 2022-06-14 14:31:34.605886
# Unit test for method validate of class Array
def test_Array_validate():
    schema = Array(
        items = Array(
            items = Array(
                items = Integer()
            )
        )
    )

    obj = [
        [
            [1, 2, 3],
            [4, 5, 6]
        ],
        [
            [7, 8, 9]
        ]
    ]

    value, error = schema.validate_or_error(obj)
    assert value == obj
    assert error is None

# Generated at 2022-06-14 14:31:38.405744
# Unit test for method validate of class Array
def test_Array_validate():
    # Create a instance of Array class
    field = Array()
    # Method validate()  does not require argument
    assert field.validate() == ValidationError()
    # Method validate()  requires argument named 'value'
    assert field.validate(value=None) == None

# Generated at 2022-06-14 14:31:40.743461
# Unit test for method validate of class String
def test_String_validate():
    # Case: cast y to integer
    field = String(allow_blank=True)
    value = field.validate(None)
    assert value == ""


# Generated at 2022-06-14 14:31:52.643164
# Unit test for method validate of class Choice
def test_Choice_validate():
    #variables
    decision = 1
    #test of condition if
    if decision == 1:
        choices = ['a', 'b', 'c', 'd', 'e']
        value = 'a'
    #test of condition elif
    elif decision == 2:
        choices = ['a', 'b', 'c', 'd', 'e']
        value = 'f'
    #test of condition else
    else:
        choices = ['a', 'b', 'c', 'd', 'e']
        value = None
    #method init
    obj = Choice(choices=choices)
    obj.validate(value)

# Generated at 2022-06-14 14:31:59.396022
# Unit test for method __or__ of class Field
def test_Field___or__():
    f1 = Field()
    f2 = Field()
    f3 = Field()
    f4 = Field()
    u1 = f1 | f2
    u2 = f3 | f4
    u3 = u1 | u2
    u4 = u2 | u1
    assert u1.any_of == [f1, f2]
    assert u2.any_of == [f3, f4]
    assert u3.any_of == [f1, f2, f3, f4]
    assert u4.any_of == [f3, f4, f1, f2]

# Generated at 2022-06-14 14:32:03.982390
# Unit test for method validate of class Number
def test_Number_validate():
    test = Number()
    assert test.validate(0) == 0
    assert test.validate(1) == 1
    assert test.validate(float('inf')) == float('inf')
    assert test.validate(None) == None
    
test_Number_validate()



# Generated at 2022-06-14 14:32:09.174061
# Unit test for method validate of class String
def test_String_validate():
    field = String(max_length=2)
    assert field.validate('a') == 'a'
    assert field.validate('ab') == 'ab'
    with pytest.raises(ValidationError) as info:
        field.validate('abc')
    assert field.validation_error('max_length') == info.value


# Generated at 2022-06-14 14:32:11.699377
# Unit test for method validate of class Choice
def test_Choice_validate():
    field=Choice(choices=None,allow_null=True)
    assert field.validate("None",strict=True) == None
    assert field.validate("",strict=True) =="required"


# Generated at 2022-06-14 14:32:22.408110
# Unit test for method __or__ of class Field
def test_Field___or__():
    # case 1
    field_instance_1 = String(max_length=4)
    field_instance_2 = String(max_length=5)
    union_instance = Union([field_instance_1, field_instance_2])
    result = field_instance_1 | field_instance_2
    assert isinstance(result, Union)
    assert result.any_of == union_instance.any_of

    field_instance_1 = String(max_length=2)
    field_instance_2 = String(max_length=3)
    union_instance = Union([field_instance_1])
    result = field_instance_1 | field_instance_2
    assert isinstance(result, Union)
    assert union_instance.any_of[0] in result.any_of
    assert field_instance_2 in result.any

# Generated at 2022-06-14 14:32:25.959672
# Unit test for method __or__ of class Field
def test_Field___or__():
    """
    Test the __or__ method of Field class.
    :return:
    """
    a = Integer().__or__(String())
    print(type(a))

# Generated at 2022-06-14 14:32:31.007241
# Unit test for method validate of class Object
def test_Object_validate():
    property = Object(properties = {"name":String(), "id":Integer()})
    field = Object(properties = {"email":String(), "age":Integer(), "property": property})
    field.validate({"email": "test@test.com", "age": 23})
test_Object_validate()


# Generated at 2022-06-14 14:32:39.676491
# Unit test for constructor of class String
def test_String():
    # constructor has the following attribute
    title = "This is the title"
    description = "This is the description"
    default = "This is the default"
    allow_blank = True
    trim_whitespace = True
    max_length = 300
    min_length = 1
    pattern = "pattern"
    format = "format"

    s = String(title=title, description=description, default=default, allow_blank=allow_blank, trim_whitespace=trim_whitespace, max_length=max_length, min_length=min_length, pattern=pattern, format=format)
    assert s.title == title
    assert s.description == description
    assert s.default == default
    assert s.allow_blank == allow_blank
    assert s.trim_whitespace == trim_whitespace
   

# Generated at 2022-06-14 14:32:46.146572
# Unit test for method validate of class Choice
def test_Choice_validate():
    choice=Choice(choices=['1','2','3']);
    assert choice.validate(None)==None;
    assert choice.validate('')==None;
    assert choice.validate('1')=='1';
    try:
        choice.validate('4')
    except ValidationError as error:
        assert error.text=='Not a valid choice.';



# Generated at 2022-06-14 14:32:56.762690
# Unit test for constructor of class Const
def test_Const():
    s = Const(0)
    s.validate(0)
    try:
        s.validate(-1)
    except ValidationError:
        pass
    else:
        assert False


# Generated at 2022-06-14 14:33:01.709798
# Unit test for method validate of class Choice
def test_Choice_validate():
    def f(x):
            return x
    try:
        a = Choice(validators=[f])
        a.validate("")
    except ValidationError as e:
        assert (str(e) == "Must be a valid Choice.")


# Generated at 2022-06-14 14:33:02.550229
# Unit test for method validate of class Choice
def test_Choice_validate():
    pass

# Generated at 2022-06-14 14:33:06.740171
# Unit test for method validate of class Object
def test_Object_validate():
    # TODO
    # AssertError [1,2]
    # AssertError {'a':1,'b':2}
    # AssertError {1:2,}
    # AssertError {1:'a',}
    return True


# Generated at 2022-06-14 14:33:18.835856
# Unit test for method validate of class Array
def test_Array_validate():
    fmt="{0: <{width}} {1: <{width}} {2: <{width}} {3: <{width}}"
    width = 20
    result_list = []
    # default values
    obj = Array()
    try:
        result = obj.validate(None)
        result_list.append([fmt.format("obj = Array()", "obj.validate(None)", "None", "None"), True])
    except ValidationError:
        result_list.append([fmt.format("obj = Array()", "obj.validate(None)", "None", "None"), False])
