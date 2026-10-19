

# Generated at 2022-06-14 14:25:30.065531
# Unit test for method __or__ of class Field
def test_Field___or__():
    field1 = Field()
    field2 = Field()
    field3 = Field()
    field4 = Field()
    field5 = Field()
    field6 = Field()
    field7 = Field()
    field8 = Field()
    field9 = Field()
    field10 = Field()
    field11 = Field()
    field12 = Field()
    field13 = Field()
    field14 = Field()
    field15 = Field()
    field16 = Field()
    field17 = Field()
    field18 = Field()
    field19 = Field()
    field20 = Field()
    field21 = Field()
    field22 = Field()
    field23 = Field()
    field24 = Field()
    field25 = Field()
    field26 = Field()
    field27 = Field()
    field28 = Field()
    field29

# Generated at 2022-06-14 14:25:36.488185
# Unit test for method validate of class Choice
def test_Choice_validate():
    choice = Choice(choices=[
        ("r", "russian"),
        ("e", "english"),
        ("g", "german")
    ])
    for lang in ["r", "e", "g"]:
        assert choice.validate(lang) == lang
    for lang in ["ru", "en", "ge"]:
        with pytest.raises(ValidationError) as err:
            choice.validate(lang)
        assert err.value.code == "choice"
    assert choice.validate("") == None
    assert choice.validate(None) == None
    assert choice.validate(1) == "1"



# Generated at 2022-06-14 14:25:40.285826
# Unit test for method serialize of class Array
def test_Array_serialize():
    obj = [1, 2, 3]
    items = [Number(multiple_of=1)]
    array = Array(items=items)
    assert array.serialize(obj) == obj


# Generated at 2022-06-14 14:25:44.912188
# Unit test for method validate_or_error of class Field
def test_Field_validate_or_error():
    a=Field()
    a1=a.validate_or_error('aj', strict=True)
    a2=ValidationResult(value=None, error=ValidationError(text='Not implement', code='NOT_IMPLEMENT'))
    assert a1==a2

# Generated at 2022-06-14 14:25:57.055517
# Unit test for method validate of class Union
def test_Union_validate():
    field_1 = String(name="String field")
    field_2 = Integer(name="Integer field")
    other_fields = [String(name="String field"),
            Integer(name="Integer field"),
            Number(name="Number field"),
            Boolean(name="Boolean field"),
            Null(name="Null field"),
            Any(name="Any field")]
    valid_string_candidates = ["String type", "Number type", "Boolean type", "Null type",
            "Any type", None]
    valid_number_candidates = [7, True, False, None]
    valid_boolean_candidates = [True, False, None]
    valid_null_candidates = [None]
    valid_any_candidates = ["String type", 7, True, False, None]


# Generated at 2022-06-14 14:26:02.299467
# Unit test for method validate of class Number
def test_Number_validate():
    test_number = Number()
    assert test_number.validate("10") == 10
    assert test_number.validate(10) == 10
    assert test_number.validate("10.0") == 10
    assert test_number.validate(10.0) == 10



# Generated at 2022-06-14 14:26:03.918315
# Unit test for method serialize of class String
def test_String_serialize():
    v1=String(format="uuid")
    assert v1.serialize==Formats.Formats.uuid.serialize



# Generated at 2022-06-14 14:26:10.728353
# Unit test for method validate of class Number
def test_Number_validate():
    value1 = Number(minimum=0, maximum=10)
    value2 = Number(minimum=0, maximum=10, multiple_of=2)
    value3 = Number(minimum=0, maximum=10, multiple_of=0.5)
    # test 1
    assert value1.validate(5) == 5 and value1.validate(9) == 9 and value1.validate(-5) == -5
    # test 2
    assert value2.validate(4) == 4 and value2.validate(8) == 8
    # test 3
    assert value3.validate(1.5) == 1.5 and value3.validate(4.5) == 4.5




# Generated at 2022-06-14 14:26:15.225551
# Unit test for method validate of class Array
def test_Array_validate():
    v1 = {"a": 1, "b": 2, "c": 3, "d": 4}
    v2 = [("a", 1), ("b", 2), ("c", 3), ("d", 4)]
    v3 = [("a", 1), ("b", 2), ("d", 4), ("c", 3)]
    v4 = {("a", 1), ("b", 2), ("d", 4), ("c", 3)}

    print(len(v1)==len(v2)==len(v3)==len(v4))
    print(sorted(v1.items())==sorted(v2))
    print(sorted(v2)==sorted(v3))
    print(set(v2)==set(v4))
    print(len(set(v2))==len(set(v4)))

# Generated at 2022-06-14 14:26:21.821575
# Unit test for method serialize of class Array
def test_Array_serialize():

    class Schema(BaseSchema):
        a = Array(items=Integer())
        b = Array(items=String())

    schema = Schema(strict=True)
    assert schema.dump({"a": [1, 2, 3], "b": ["a"]}) == {"a": [1, 2, 3], "b": ["a"]}
    schema = Schema(strict=False)
    assert schema.dump({"a": [1, 2, 3], "b": ["a"]}) == {"a": [1, 2, 3], "b": ["a"]}
    assert schema.dump({"a": ["1", 2, 3], "b": ["a"]}) == {"a": [1, 2, 3], "b": ["a"]}

# Generated at 2022-06-14 14:26:35.759215
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    def test_func():
        return 'test'
    f = Field()
    f.default = test_func 
    assert f.get_default_value() == 'test'       
    f.default = 'default_value'
    assert f.get_default_value() == 'default_value'
    f.default = None
    assert f.get_default_value() == None



# Generated at 2022-06-14 14:26:44.806444
# Unit test for constructor of class Const
def test_Const():
    import pandas as pd
    from typing import NamedTuple
    from datetime import datetime

    class User(NamedTuple):
        name: str
        age: int
        birthday: datetime

    UserSchema = Object(
        {
            "name": Text(allow_null=False),
            "age": Number(allow_null=False),
            "birthday": DateTime(allow_null=False)
        }
    )
    user = [dict(name="Alice", age=23, birthday=datetime(1995, 2, 23))]
    data = pd.DataFrame(user)
    data.birthday = data.birthday.astype(str)
    user_schema = UserSchema.serialize(data.to_dict("records"))

# Generated at 2022-06-14 14:26:47.389384
# Unit test for method validate of class Union
def test_Union_validate():

    validator = Union([
        String(required=True, empty=False, min_length=1),
        Integer(required=True, min_number=1)
    ])
    validated, error = validator.validate_or_error('test')
    assert (error is None)

# Generated at 2022-06-14 14:26:56.412034
# Unit test for method validate of class Union
def test_Union_validate():
    t1 = Any()
    t2 = Integer()
    t3 = String()
    u = Union([t1, t2, t3])
    assert u.validate(1) == 1
    assert u.validate("1") == "1"
    assert u.validate(1.0) == 1.0
    assert u.validate(False) == False
    try:
        assert u.validate({}) == {}
    except ValidationError:
        pass
    else:
        raise Exception("Not pass")

# Generated at 2022-06-14 14:27:03.390045
# Unit test for method __or__ of class Field
def test_Field___or__():
    class TestField(Field):
        pass
    testField = TestField()
    testField2 = TestField()
    assert (testField | testField2).any_of == [testField, testField2]

    class TestFieldUnion(Union):
        any_of = [testField, testField2]

    assert (testField | TestFieldUnion()).any_of == [testField, testField2]



# Generated at 2022-06-14 14:27:14.383442
# Unit test for method validate of class Object
def test_Object_validate():
    # 测试基本信息
    properties = {"name": Field(validators=[validate.Length(max=5)]), 
                  "age": Integer(required=True)}
    schema = Object(properties=properties)
    data = {"name": "mike", "age": 23}
    result = schema.validate(data)
    assert result == {'name': 'mike', 'age': 23}

    # 测试pattern_properties
    properties = {"name": Field(validators=[validate.Length(max=5)])}
    pattern_properties = {"^s(.+)": Field(validators=[validate.Length(max=5)])}
    schema = Object(properties=properties, pattern_properties=pattern_properties)

# Generated at 2022-06-14 14:27:16.696563
# Unit test for method validate of class Array
def test_Array_validate():
    field = Array(items=[Number(),Number()])
    result = field.validate([1,2])
    assert result == [1,2]


# Generated at 2022-06-14 14:27:24.569881
# Unit test for method validate of class Choice
def test_Choice_validate():
    def check(value, expected_output):
        out = Choice().validate(value)
        assert out == expected_output

    def error(value):
        with pytest.raises(validation.ValidationError):
            Choice().validate(value)

    check(None, None)
    error("")
    error("a")

    check("a", "a")
    check("b", "b")
    error("c")

    check("a", "a")
    check("b", "b")
    error("c")

    check("a", "a")
    check("b", "b")
    error("c")

    check("a", "a")
    check("b", "b")
    error("c")

    check("a", "a")
    check("b", "b")

# Generated at 2022-06-14 14:27:32.059282
# Unit test for method validate of class Choice
def test_Choice_validate():
    
    import sys
    import pytest
    import inspect

    test_choice = Choice(choices=["test_choice", "test_choice2"])

    assert test_choice.validate("test_choice")== "test_choice"

    assert test_choice.validate("test_choice2")== "test_choice2"
    
    with pytest.raises(ValidationError):
        test_choice.validate("test_choice3")



# Generated at 2022-06-14 14:27:41.451862
# Unit test for method validate of class String
def test_String_validate():
    value="1"
    assert value == String(title="",description="",default="",allow_null=False).validate(value,strict=False)
    assert value == String(title="",description="",default="",allow_null=False).validate(value,strict=True)
    value=None
    assert value == String(title="",description="",default="",allow_null=True).validate(value,strict=False)
    value=None
    assert value == String(title="",description="",default="",allow_null=True,allow_blank=True).validate(value,strict=False)
    value=" "
    assert value == String(title="",description="",default="",allow_null=True,allow_blank=True).validate(value,strict=False)
    value="  "


# Generated at 2022-06-14 14:28:27.375380
# Unit test for method validate of class Choice
def test_Choice_validate():
    # Create sample object of Choice
    choices_field = Choice(choices=["a", "b", "c"])
    # Make assertion
    assert choices_field.validate("b") == "b"
    # Make assertion
    assert choices_field.validate(None) == None
    # Make assertion
    with pytest.raises(ValidationError):
        choices_field.validate("a")
    # Make assertion
    with pytest.raises(ValidationError):
        choices_field.validate("b")
    # Make assertion
    with pytest.raises(ValidationError):
        choices_field.validate("c")



# Generated at 2022-06-14 14:28:30.530097
# Unit test for method validate of class String
def test_String_validate():
    obj = String()
    result = obj.validate("hello")
    assert result=='hello'

# Generated at 2022-06-14 14:28:40.194139
# Unit test for method validate of class String
def test_String_validate():
    # test for not allowed null value
    test_validate_value = String()
    try:
        test_validate_value.validate(None)
    except ValidationError as e:
        assert e.code == 'null'
        assert e.text == 'Must not be null.'
    # test for not allowed blank value
    test_validate_value = String(allow_null=True)
    try:
        test_validate_value.validate('', strict=True)
    except ValidationError as e:
        assert e.code == 'blank'
        assert e.text == 'Must not be blank.'
    # test for allowed blank value
    assert test_validate_value.validate('', strict=False) == ''
    # test for not allowed blank value, but allowed null value

# Generated at 2022-06-14 14:28:42.200245
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    field = Field() 
    assert field.get_default_value() == None


# Generated at 2022-06-14 14:28:46.436990
# Unit test for constructor of class String
def test_String():
    s = String(title="A String", description="A string", default="Default string")
    assert s.title == "A String"
    assert s.description == "A string"
    assert s.default == "Default string"


# Generated at 2022-06-14 14:28:52.474021
# Unit test for constructor of class String
def test_String():
    field = String()

    assert(field.has_default() == False)
    assert(field.allow_null == False)
    assert(field.title == "")
    assert(field.description == "")
    assert(field.allow_blank == False)
    assert(field.trim_whitespace == True)
    assert(field.max_length == None)
    assert(field.min_length == None)
    assert(field.pattern == None)
    assert(field.pattern_regex == None)
    assert(field.format == None)
    assert(field.has_default() == False)


# Generated at 2022-06-14 14:28:54.415584
# Unit test for method validate of class String
def test_String_validate():
    singleStringField = String()
    assert singleStringField.validate("str") == "str"

# Generated at 2022-06-14 14:28:55.975355
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    field = Field()
    assert field.get_default_value() == None

# Generated at 2022-06-14 14:29:03.090496
# Unit test for method validate of class Choice
def test_Choice_validate():
    choices = [
        ("1", "1"),
        ("2", "2"),
        ("3", "3")
    ]
    c = Choice(choices=choices)
    c.validate("2")
    c.validate("1")
    c.validate("3")
    try:
        c.validate("5")
    except ValueError as e:
        assert str(e) == "Not a valid choice."


# Generated at 2022-06-14 14:29:10.851178
# Unit test for constructor of class Array
def test_Array():
    class Document(DocumentSchema):
        items = Array()

    assert len(Document.__fields__) == 1
    assert 'items' in Document.__fields__
    assert isinstance(Document.__fields__['items'], Array)
    assert Document.__fields__['items'].name == 'items'
    assert Document.__fields__['items'].items is None
    assert Document.__fields__['items'].additional_items is False
    assert Document.__fields__['items'].min_items is None
    assert Document.__fields__['items'].max_items is None
    assert Document.__fields__['items'].unique_items is False
    assert Document.__fields__['items'].allow_null is True
    assert Document.__fields__['items'].required is False


# Generated at 2022-06-14 14:29:22.306337
# Unit test for method validate of class Choice
def test_Choice_validate():
    ch = Choice(choices=[('A', 'B'), ('C', 'D')])
    assert ch.validate('A') == 'A'
    assert ch.validate('B') == 'A'
    assert ch.validate('C') == 'C'
    assert ch.validate('D') == 'C'
    assert ch.validate('', strict=False) == None
    assert ch.validate('', strict=True) == ''


# Generated at 2022-06-14 14:29:31.709914
# Unit test for method validate of class Array
def test_Array_validate():
    """
    Unit test for method validate of class Array
    """
    field = Array(items=Integer(min_value=10,max_value=30))
    assert field.validate([]) == []
    assert field.validate([20]) == [20]
    assert field.validate([20,30,10]) == [20,30,10]
    try:
        field.validate([20,30,10,0])
    except ValidationError as error:
        assert error.messages() == [Message(text='Must have no more than 3 items.', code="max_items", index=[3])]
    field = Array(items=Integer(min_value=10,max_value=30),min_items=2,max_items=5)
    assert field.validate([20,30]) == [20,30]


# Generated at 2022-06-14 14:29:42.683977
# Unit test for method validate of class String
def test_String_validate():
    title = "string example"
    description = "description example"
    default = "default example"
    allow_blank = False
    trim_whitespace = True
    max_length = 20
    min_length = 5
    pattern = r"\w+"
    format = "format example"
    allow_null = False
    field_string = String(title=title, description=description, default=default, allow_blank=allow_blank, trim_whitespace=trim_whitespace, max_length=max_length, min_length=min_length, pattern=pattern, format=format, allow_null=allow_null)

    assert field_string.validate("quyen") is not None
    assert field_string.validate("quyen") is not ValidationError

# Generated at 2022-06-14 14:29:44.783548
# Unit test for method validate of class Choice
def test_Choice_validate():
    choice = Choice(choices=["one", "two", "three"])
    assert choice.validate("one") == "one"
    assert choice.validate("two") == "two"
    assert choice.validate("three") == "three"

    with pytest.raises(ValidationError):
        choice.validate("four")



# Generated at 2022-06-14 14:29:46.086777
# Unit test for constructor of class Const
def test_Const():
    simpleExample = Const(1)
    assert str(simpleExample) == "Const(1)"


# Generated at 2022-06-14 14:29:48.378271
# Unit test for method __or__ of class Field
def test_Field___or__():
    pass

# Generated at 2022-06-14 14:29:57.776511
# Unit test for method validate of class String
def test_String_validate():
    #initialize the field
    string_field = String(min_length = 2, max_length = 3, format = "uuid" )
    #test different cases
    try:
        assert string_field.validate(None, strict=True)
    except:
        print("case1: validation error")
    try:
        assert string_field.validate("")
        print("case2: no validation error")
    except:
        print("case2: validation error")
    try:
        assert string_field.validate("12345")
    except:
        print("case3: no validation error")
    try:
        assert string_field.validate("12345", strict = True)
    except:
        print("case4: no validation error")

# Generated at 2022-06-14 14:30:04.454064
# Unit test for method __or__ of class Field
def test_Field___or__():
    import typesystem
    def fn1(x):
        print("fn1", x)
        return x
    def fn2(x):
        print("fn2", x)
        return x
    typesystem.Integer()
    typesystem.Integer()
    Field.__or__(fn1(typesystem.Integer()), fn2(typesystem.Integer()))



# Generated at 2022-06-14 14:30:15.684255
# Unit test for method serialize of class String
def test_String_serialize():
    assert String(format='date').serialize(time.strptime("1/1/2020", '%d/%m/%Y')) == datetime.date(2020, 1, 1)
    assert String(format='time').serialize(time.strptime("1/1/2020", '%d/%m/%Y')) == None
    assert String(format='datetime').serialize(time.strptime("1/1/2020", '%d/%m/%Y')) == datetime.datetime(2020, 1, 1, 0, 0)
    assert String(format='uuid').serialize("dcd98b7102dd2f0e8b11d0f600bfb0c093") == None



# Generated at 2022-06-14 14:30:20.116231
# Unit test for method validate of class Choice
def test_Choice_validate():
    string_test_cases = [
        ('test', 'test'), ('test', ('test', 'test')), ('test', ('test', 'test1')), ('test', ('test1', 'test2'))
    ]
    choice_lst_test_cases = [
        (('test', 'test'), Choice(choices=[('test', 'test')])),
        (('test', 'test1'), Choice(choices=[('test', 'test')])),
        (('test', 'test2'), Choice(choices=[('test', 'test')])),
        (('test1', 'test2'), Choice(choices=[('test', 'test')]))
    ]

# Generated at 2022-06-14 14:30:43.426025
# Unit test for method validate of class Union
def test_Union_validate():
    # Create a dictionary and a Union object.
    dic = {'b': 6, 'a': 5}
    u= Union([Dictionary(), Dictionary()])
    test = {'key':'value'}
    # Check if the u object is a Field.
    assert isinstance(u, Field)==True
    # Check if the u object is a Union.
    assert isinstance(u, Union)==True
    # Check if the value inserted is a dictionary.
    assert isinstance(test, dict) == True
    assert isinstance(dic, dict) == True
    # Check if the method validate returns the correct value.
    assert u.validate(dic) == dic
    # Check if the method validate can handle incorrect input data.
    assert u.validate(test) == dic
    #Check if the method validate raises the

# Generated at 2022-06-14 14:30:50.392160
# Unit test for method validate of class Choice
def test_Choice_validate():
    choice_object = Choice(choices=['4', '3', '2', '1'])
    if choice_object.validate('4') != '4':
        raise AssertionError()
    if choice_object.validate('5') != '5':
        raise AssertionError()
    if choice_object.validate('5') == '5':
        raise AssertionError()
    if choice_object.validate(None) != None:
        raise AssertionError()
    if choice_object.validate(None) == None:
        raise AssertionError()


# Generated at 2022-06-14 14:30:57.237366
# Unit test for method validate of class Union
def test_Union_validate():
    assert Union([Integer(), Number()]).validate(4) == 4
    assert Union([Integer(), Number()]).validate(3.1) == 3.1
    error = Union([Integer(), Number()]).validate_or_error("hi")[1]
    assert error.messages()[0].text == "Must be a number."

    error = Union([Integer(), Number()]).validate_or_error("hi")[1]
    assert error.messages()[0].text == "Must be a number."

    error = Union([Integer(), String()]).validate_or_error(True)[1]
    assert error.messages()[0].text == "Must be an integer."

    error = Union([Boolean(), String()]).validate_or_error(4)[1]

# Generated at 2022-06-14 14:31:02.470118
# Unit test for constructor of class Array
def test_Array():
    items = Array(items = [
        String(),
        Integer()
    ], unique_items = True, min_items = 2, max_items = 4)
    assert (items.items[0].__class__.__name__ == "String")
    assert (items.items[1].__class__.__name__ == "Integer")
    assert (items.unique_items == True)
    assert (items.min_items == 2)
    assert (items.max_items == 4)


# Generated at 2022-06-14 14:31:11.725246
# Unit test for method validate of class Choice
def test_Choice_validate():
    assert Choice(choices=[("key1","value1")]).validate("key1") == "key1"
    assert Choice(choices=[("key1","value1")]).validate("value1") == "key1"
    assert Choice(choices=[("key1","value1")]).validate("key2") == "key2"
    assert Choice(choices=[("key1","value1")]).validate("value2") == "key1"
    assert Choice(allow_null=True,choices=[("key1","value1")]).validate("key1") == "key1"
    assert Choice(allow_null=True,choices=[("key1","value1")]).validate("value1") == "key1"

# Generated at 2022-06-14 14:31:15.507097
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    title = "name"
    description = "name"
    default = "name"
    allow_null = False
    field = Field(title=title,
                description=description,
                default=default,
                allow_null=allow_null)
    assert field.has_default() is True
    assert field.get_default_value()  == "name"



# Generated at 2022-06-14 14:31:18.609770
# Unit test for method validate of class Choice
def test_Choice_validate():
    a = Choice(required=True, choices=[(1, 'A'), (2, 'B')])
    a.validate(1)
    try:
        a.validate(3)
    except ValidationError as e:
        print("The content of ValidationError is {}".format(e.text))

# Generated at 2022-06-14 14:31:28.792427
# Unit test for method validate of class Object
def test_Object_validate():
    """
    Test method validate of class Object
    """
    d = {}
    d["Object"] = Object()
    d["test"] = {}
    d["test"]["test"] = "test"
    d["test"]["test2"] = ""
    assert d["Object"].validate(d["test"]) == d["test"]
    assert d["Object"].validate(d["test"]) == d["test"]
    d["test"]["test"] = 2
    try:
        d["Object"].validate(d["test"])
    except errors.ValidationError:
        pass
    try:
        d["Object"].validate(d["test"])
    except errors.ValidationError:
        pass
    d["test"]["test"] = "test"

# Generated at 2022-06-14 14:31:36.574707
# Unit test for method validate of class Union
def test_Union_validate():
    # unit test for method validate of class Union 
    # Test for Union.validate
    class Test(Serializer):
        a=Integer(default=1)
        b=Integer(default=2)
    test_union=Union(any_of=[Test(a=1,b=2),Test(a=3,b=4)],default=2)
    assert test_union.validate(Test(a=1,b=2))==1

test_Union_validate()
       
test_Union_validate()

# Generated at 2022-06-14 14:31:44.414805
# Unit test for method validate of class String
def test_String_validate():
    string1_field = String(min_length=4)
    string2_field = String(max_length=4)
    string3_field = String(pattern="^ABC.*")

    assert string1_field.validate("ABCD") == "ABCD"
    assert string1_field.validate("ABC") == "ABC"
    assert string1_field.validate("") == ""
    assert string1_field.validate(None) == ""
    assert string1_field.validate("ABC\0") == "ABC"
    assert string1_field.validate("ABC\0DEF") == "ABCDEF"
    assert string1_field.validate(" ABCD") == "ABCD"
    assert string1_field.validate("ABCD ") == "ABCD"

# Generated at 2022-06-14 14:31:53.123805
# Unit test for constructor of class String
def test_String():
    field = String(title = "test_title", description = "test_description", default = "test_default")
    assert field.title == "test_title"
    assert field.description == "test_description"
    assert field.default == "test_default"


# Generated at 2022-06-14 14:32:02.693048
# Unit test for method validate of class Array
def test_Array_validate():
    """
    Unit test for method validate of class Array
    """
    class TestClass(object):
        def __init__(self, a: int) -> None:
            self.a = a
        def __eq__(self, other) -> bool:
            return isinstance(other, TestClass) and other.a == self.a

    # case 1: items is None, additional_items is False
    num_list = NumberList(min_items = 2, max_items = 3)
    str_list = StringList(min_items = 2, max_items = 3)
    obj_list = ObjectList(min_items = 2, max_items = 3)
    arr_list = ArrayList(min_items = 2, max_items = 3)

    value = [1., 2., 3.]
    expected = value
    result = num

# Generated at 2022-06-14 14:32:06.632336
# Unit test for method validate of class Choice
def test_Choice_validate():
    """
    This unit test is for method validate of class Choice
    """
    field1 = Choice(choices=["As", "Bs", "Cs", "Ds"])
    field = field1.validate('As',strict=0)
    assert field=='As'


# Generated at 2022-06-14 14:32:14.144841
# Unit test for method validate of class Object
def test_Object_validate():
    from typing import List, Dict, Any
    from jsonvalidator.validators import Object, Choice, Number
    from jsonvalidator.fields import Field

    class _TestField(Field):
        def __init__(self, *args: Any, **kwargs: Any) -> None:
            self.errors= {
                "type": "Must be an object.",
                "null": "May not be null.",
                "invalid_key": "All object keys must be strings.",
                "required": "This field is required.",
                "invalid_property": "Invalid property name.",
                "empty": "Must not be empty.",
                "max_properties": "Must have no more than {max_properties} properties.",
                "min_properties": "Must have at least {min_properties} properties.",
            }

# Generated at 2022-06-14 14:32:23.016624
# Unit test for method validate of class Object
def test_Object_validate():
    class A(Object):
        required = ["a", "b"]
        properties = {"a": Integer, "b": Float}

    a = A()
    print(a.validate({"a": 1, "b": 2.0}))
    print(a.validate({"a": 1, "b": 2.0, "c": 3.0}))
    print(a.validate({"a": 1, "b": 2.0, "c": 3.0, "d": "e"}))
    a.validate({"a": 1, "b": 2.0, "c": 3.0, "d": "e"}, strict = True)



# Generated at 2022-06-14 14:32:27.649249
# Unit test for method validate of class Choice
def test_Choice_validate():
    choice = Choice(choices = [["b", "b"], ["c", "c"]])
    try:
        choice.validate('a')
    except ValidationError:
        assert True
    else:
        assert False


# Generated at 2022-06-14 14:32:34.168773
# Unit test for method __or__ of class Field
def test_Field___or__():
    string = String()
    number = Number()
    union = string | number
    assert union.any_of == [string, number]
    union2 = string | number | union
    assert union2.any_of == [string, number, union]
# Test for method __or__ of class Field ends here.

    def __and__(self, other: "Field") -> "Intersection":
        return Intersection(items=[self, other])

# Generated at 2022-06-14 14:32:36.463197
# Unit test for method get_default_value of class Field
def test_Field_get_default_value():
    default = 5
    f = Field(default = default)
    assert f.get_default_value() == default
    

# Generated at 2022-06-14 14:32:41.855057
# Unit test for method __or__ of class Field
def test_Field___or__():
    from .. import Union

    field1 = Field()
    field2 = Field()
    u1 = Union([field1, field2])
    u2 = field1 | field2
    assert u1.any_of == u2.any_of

    field3 = Field()
    u3 = field1 | field2 | field3
    assert len(u3.any_of) == 3



# Generated at 2022-06-14 14:32:48.350776
# Unit test for method validate of class Union
def test_Union_validate():
    assert Union(any_of=[Dict(), Array()]).validate([])
    assert Union(any_of=[Dict(), Array()]).validate({})
    with pytest.raises(ValidationError):
        Union(any_of=[Dict(), Array()]).validate(None)
    with pytest.raises(ValidationError):
        Union(any_of=[Dict(), Array()]).validate('test')


# Generated at 2022-06-14 14:33:08.153072
# Unit test for method validate of class Choice
def test_Choice_validate():
    input_json = {
        "data": {
            "type": "nodes",
            "attributes": {
                "id": 1,
                "name": "name1",
                "type": "type1"
            }
        }
    }
    class Choice(Field):
        errors = {
            "null": "May not be null.",
            "required": "This field is required.",
            "choice": "Not a valid choice.",
        }
        def __init__(self, *, choices: typing.Sequence[typing.Union[str, typing.Tuple[str, str]]] = None, **kwargs: typing.Any):
            super().__init__(**kwargs)

# Generated at 2022-06-14 14:33:12.068082
# Unit test for method validate of class Object
def test_Object_validate():
    # Test the correctness of Object.validate of empty string
    with pytest.raises(ValidationError):
        value = ''
        strict = False
        o1 = Object()
        o1.validate(value)


# Generated at 2022-06-14 14:33:19.078934
# Unit test for constructor of class Array
def test_Array():
    arr = Array(
        items = Integer(min_inclusive=0, max_inclusive=100),
        min_items = 1,
        max_items = 10,
        unique_items = True
    )
    assert arr.items == Integer(min_inclusive=0, max_inclusive=100)
    assert arr.min_items == 1
    assert arr.max_items == 10
    assert arr.unique_items == True
