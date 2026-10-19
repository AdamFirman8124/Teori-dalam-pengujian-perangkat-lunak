

# Generated at 2022-06-14 14:12:38.560590
# Unit test for method validate of class Not
def test_Not_validate():
    field = Not(String())
    assert field.validate("hello")
    try:
        field.validate("123")
        assert False, "Must not match."
    except ValidationError:
        assert True, "Must not match."


# Generated at 2022-06-14 14:12:44.269524
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    from typesystem import Integer

    field = IfThenElse(
        if_clause=Integer(), then_clause=Integer(), else_clause=Integer()
    )
    assert field.validate(1) == 1
    assert field.validate(1.0, strict=True) == 1
    assert field.validate(-1) == -1

# Generated at 2022-06-14 14:12:47.400189
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    i = IfThenElse(None,None,None)
    print(i.validate(1))
    print(i.validate(1))
    print(i.validate(1))
    print(i.validate(1))

# Generated at 2022-06-14 14:12:54.542887
# Unit test for constructor of class AllOf
def test_AllOf():
    from typesystem.fields import String
    from typesystem.types import Type

    str_field = String()
    str_type = Type(str_field)

    # test with a list of strings
    string_field_list = [String(), String()]
    allof_string = AllOf(string_field_list)
    assert allof_string.all_of == string_field_list

    # test with a list of types
    type_field_list = [str_type, str_type]
    allof_type = AllOf(type_field_list)
    assert allof_type.all_of == type_field_list

# Generated at 2022-06-14 14:12:56.852222
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    aField = IfThenElse(Field(),Field('b'))
    result = aField.validate(['a'])
    assert result == ['b']

# Generated at 2022-06-14 14:12:58.532077
# Unit test for method validate of class Not
def test_Not_validate():
    field = Not(String())
    assert field.validate(99) == 99

# Generated at 2022-06-14 14:13:01.519978
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    clause = IfThenElse(if_clause=Field(), then_clause=None, else_clause=None)
    assert clause.validate('') is None

# Generated at 2022-06-14 14:13:03.185427
# Unit test for method validate of class IfThenElse

# Generated at 2022-06-14 14:13:08.632391
# Unit test for method validate of class Not
def test_Not_validate():
    int_field = fields.Integer()
    not_field = Not(negated=int_field)

    assert not_field.validate("test") == "test"
    with pytest.raises(errors.ValidationError) as exc_info:
        not_field.validate(123)
    assert exc_info.value.code == "negated"

# Generated at 2022-06-14 14:13:13.227410
# Unit test for method validate of class Not
def test_Not_validate():
    from jsonschema import validate
    from jsonschema.exceptions import ValidationError

    class SchemaTest(typesystem.Schema):
        test = Not(typesystem.String())

    schema = SchemaTest(strict=True)

    with pytest.raises(ValidationError) as excinfo:
        schema.validate({"test":"test"})



# Generated at 2022-06-14 14:13:18.503293
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    assert OneOf(one_of=[String()]).validate("text") == "text"
    assert OneOf(one_of=[String()]).validate(5) == 5

# Generated at 2022-06-14 14:13:25.482949
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    import typesystem
    
    # Throws AssertionError
    try:
        class MySchema(typesystem.Schema):
          value = typesystem.OneOf(one_of=[])
    except AssertionError:
        pass

        # Throws AssertionError
try:
    class MySchema(typesystem.Schema):
        value = typesystem.OneOf(one_of=[1])
except AssertionError:
    pass


# Generated at 2022-06-14 14:13:29.444453
# Unit test for constructor of class Not
def test_Not():
    print("Unit test for constructor of class Not")
    # <Code>
    import typesystem
    
    schema = typesystem.Not(typesystem.String())
    # </Code>



# Generated at 2022-06-14 14:13:38.655021
# Unit test for method validate of class Not
def test_Not_validate():
    type = Not(None)
    # Test error on validate method using None as value
    try:
        type.validate(None)
        assert False
    except Exception as e:
        assert str(e) == 'must not be null'
    # Test error on validate method using a negative value
    try:
        type.validate(-1)
        assert False
    except Exception as e:
        assert str(e) == 'not a valid integer'
    # Test error on validate method using a positive value
    try:
        type.validate(1)
        assert True
    except Exception as e:
        assert False

# Generated at 2022-06-14 14:13:50.443264
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    assert IfThenElse(if_clause=Number(), then_clause=Str()).validate(1) == 1
    assert IfThenElse(if_clause=Number(), then_clause=Str()).validate("1") == "1"
    assert IfThenElse(if_clause=Number(), then_clause=Str()).validate(1.1) == 1.1
    assert IfThenElse(if_clause=Number(), then_clause=Str(), else_clause=Number()).validate(1) == 1
    assert IfThenElse(if_clause=Number(), then_clause=Str(), else_clause=Number()).validate("1") == 1

# Generated at 2022-06-14 14:13:53.343368
# Unit test for constructor of class AllOf
def test_AllOf():
    import typesystem

    field = typesystem.AllOf(
        [
            typesystem.String(max_length=10),
            typesystem.String(min_length=5),
        ]
    )


# Generated at 2022-06-14 14:13:54.665295
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    with pytest.raises(AssertionError):
        IfThenElse(Any(), allow_null=True)

# Generated at 2022-06-14 14:13:57.926638
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    never_match = NeverMatch()
    assert never_match is not None
    assert never_match.errors == {'never': 'This never validates.'}


# Generated at 2022-06-14 14:13:58.689816
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    assert NeverMatch()

# Generated at 2022-06-14 14:14:01.101313
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    nm = NeverMatch()
    assert nm.__class__.__name__ == "NeverMatch"

# Generated at 2022-06-14 14:14:15.677746
# Unit test for method validate of class OneOf
def test_OneOf_validate(): 
    field = OneOf([String(max_length=4), String(max_length=6)])
    assert field.validate("abcd") == "abcd"
    assert field.validate("abcde") == "abcde"
    try:
        field.validate("abcdef")
        assert False
    except FieldValidationError as error:
        assert error.messages == {"no_match": "Did not match any valid type."}
    try:
        field.validate("abcdefg")
        assert False
    except FieldValidationError as error:
        assert error.messages == {"no_match": "Did not match any valid type."}

# Generated at 2022-06-14 14:14:22.613173
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    try:
        one_of = OneOf([])
        print(one_of.validate(5.5))
    except ValidationError as e:
        errors = e.get_error_messages()
        assert errors["no_match"] == "Did not match any valid type.", 'expected exception and message should be -Did not match any valid type., but found {}'.format(errors["no_match"])



# Generated at 2022-06-14 14:14:31.158278
# Unit test for constructor of class OneOf
def test_OneOf():
    from typesystem.fields import Boolean, Number, String
    from typesystem import Schema, fields, validators
    from typesystem.base import Context
    class Person(Schema):
        name = fields.String(min_length=5)
        age = fields.Number()
        fav_number = fields.String()
    schema = Person(context={'fav_number': "3"})
    print(schema.validators)
    # o1 = OneOf([Boolean(), String()],
    #            error_messages={'no_match': 'Please choose one of them'})
    # print(o1.validate(False))
    # print(o1.validate(1))
    # print(o1.validate_or_error(1.1, strict=True))
    # print(o1.validate_

# Generated at 2022-06-14 14:14:36.005118
# Unit test for method validate of class Not

# Generated at 2022-06-14 14:14:42.371457
# Unit test for constructor of class AllOf
def test_AllOf():
    assert hasattr(AllOf, '__init__')
    AllOf.__init__(AllOf, ["test_all_of"], allow_null=False, description=None, name=None, parent=None)
    assert type(AllOf) == type

test_AllOf()


# Generated at 2022-06-14 14:14:50.671264
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    one_ofs = [
        Field(type=str, pattern="^[a-z]+$", name="one_ofs"),
        Field(type=int, minimum=0, maximum=4, name="one_ofs")
    ]
    assert Field(OneOf(one_ofs)).validate("abc") == "abc"
    assert Field(OneOf(one_ofs)).validate(3) == 3
    with pytest.raises(ValidationError):
        Field(OneOf(one_ofs)).validate(5)
    with pytest.raises(ValidationError):
        Field(OneOf(one_ofs)).validate("")



# Generated at 2022-06-14 14:14:53.211519
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    test_value = "test_value"
    neverMatch_value = NeverMatch(test_value)
    return neverMatch_value


# Generated at 2022-06-14 14:15:02.999748
# Unit test for method validate of class Not
def test_Not_validate():
    print('\n\nUnit test for method validate of class Not. \n')
    test_string = 'testing string'
    test_integer = 12345
    test_wrong_type = None

    test_not = Not(String())

    print('\nString field: ' + str(test_not.validate(test_string)))
    print('Integer field: ' + str(test_not.validate(test_integer)))
    print('Test wrong type:')
    try:
        print(test_not.validate(test_wrong_type))
    except TypeError as e:
        print('Exception raised, wrong type of data')


# Generated at 2022-06-14 14:15:06.900500
# Unit test for method validate of class Not
def test_Not_validate():
    field = Not(negated=String())
    result, error = field.validate_or_error("Hello")
    assert result is 'Hello'
    assert error == {'negated': 'Must not match.'}


# Generated at 2022-06-14 14:15:08.228857
# Unit test for method validate of class Not
def test_Not_validate():
    not_object = Not(Any())
    assert not_object.validate(None)

# Generated at 2022-06-14 14:15:16.452526
# Unit test for constructor of class AllOf
def test_AllOf():
    print ("Test 1: AllOf constructor")
    a1 = Field()
    a2 = Field()
    a3 = Field()
    allOf = AllOf([a1, a2, a3])
    assert [a1, a2, a3] == allOf.all_of
    assert {} == allOf.errors



# Generated at 2022-06-14 14:15:27.611984
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    # Test 1 - with valid input
    # Expected result = successful validation
    myField = OneOf([])
    try:
        myField.validate(1)
    except Exception as e:
        print("Test 1 - Fail")
        print("Raised exception: ", e)
    else:
        print("Test 1 - Success")

    # Test 2 - with invalid input
    # Expected result = unsuccessful validation
    myField = OneOf([])
    try:
        myField.validate({})
    except Exception as e:
        print("Test 2 - Success")
    else:
        print("Test 2 - Fail")

    # Test 3 - with strict mode
    # Expected result = unsuccessful validation
    myField = OneOf([])

# Generated at 2022-06-14 14:15:29.275592
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    val = NeverMatch(description = "Field must not match")
    assert (val.description == "Field must not match")


# Generated at 2022-06-14 14:15:31.405281
# Unit test for method validate of class Not
def test_Not_validate():
    print("test_Not_validate")
    n = Not(Field(), allow_null=False)
    with pytest.raises(ValidationError):
        n.validate({})

# Generated at 2022-06-14 14:15:34.223946
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    from typesystem.fields import String
    field = OneOf([String(max_length=10), String(max_length=5)])
    field.validate("12345")
    field.validate("123456")
    field.validate("12345678901")


# Generated at 2022-06-14 14:15:35.413614
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    field = NeverMatch(name='Null')
    assert isinstance(field, NeverMatch)

# Generated at 2022-06-14 14:15:38.623732
# Unit test for constructor of class OneOf
def test_OneOf():
    str_field = Field()
    int_field = Field()
    obj_field = Field()
    
    one_of_field = OneOf([str_field, int_field, obj_field])
    assert one_of_field.one_of == [str_field, int_field, obj_field]


# Unit tests for function validate() in class OneOf

# Generated at 2022-06-14 14:15:45.378050
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    class GreaterThanZero(Field):
        errors = {"invalid": "Value must be greater than zero."}
        def __init__(self, **kwargs: typing.Any) -> None:
            assert "allow_null" not in kwargs
            super().__init__(**kwargs)
        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            if value > 0:
                return value
            else:
                raise self.validation_error("invalid")

    class Integer(Field):
        errors = {"invalid": "Value must be an int."}

        def __init__(self, **kwargs: typing.Any) -> None:
            assert "allow_null" not in kwargs
            super().__init__(**kwargs)


# Generated at 2022-06-14 14:15:47.922893
# Unit test for constructor of class AllOf
def test_AllOf():
    f = AllOf([])
    assert f.all_of == []



# Generated at 2022-06-14 14:15:51.581235
# Unit test for constructor of class OneOf
def test_OneOf():
    """
    Create an instance of class OneOf
    """
    my_one_of = OneOf([1,2,3,4,5,6,7,8,9,10])
    assert my_one_of


# Generated at 2022-06-14 14:15:57.462604
# Unit test for method validate of class Not
def test_Not_validate():
    n = Not(negated=Number())
    assert n.validate(1) == 1
    assert n.validate(None) == None
    with pytest.raises(SchemaError) as e:
        n.validate(True)


# Generated at 2022-06-14 14:16:02.367610
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    a = Field()
    b = Field()
    x = Field()
    conditional = IfThenElse(a, then_clause=b)
    conditional.validate(1)
    conditional = IfThenElse(x, then_clause=b, else_clause=a)
    conditional.validate(1)

# Generated at 2022-06-14 14:16:05.984650
# Unit test for constructor of class AllOf
def test_AllOf():
    class Foo(Field):
        pass
    x = AllOf([Foo()])
    assert isinstance(x, Field)
    assert x.all_of[0].__class__ == Foo


# Generated at 2022-06-14 14:16:08.346472
# Unit test for constructor of class Not
def test_Not():
    not_=Not(negated=AllOf(all_of=[Field()]))
    assert not_.negated == AllOf(all_of=[Field()])


# Generated at 2022-06-14 14:16:16.148374
# Unit test for method validate of class Not
def test_Not_validate():
    """
    Test case for method validate of class Not
    Test type of self.negated
    test case: self.negated returns None
    """
    from typesystem.fields import String, Boolean
    from typesystem.base import Message
    from typesystem.exceptions import ValidationError

    # initialize field 'negated' with Boolean(required=True, default=False)
    negated = Boolean(required=True, default=False)
    field = Not(negated)
    value = ""
    assert field.validate(value) == ""



# Generated at 2022-06-14 14:16:26.636343
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    class A(Field):
        def validate(self, value, strict=False):
            return value == 1
    class B(Field):
        def validate(self, value, strict=False):
            return value == 3
    class C(Field):
        def validate(self, value, strict=False):
            return value == 4
    c1 = C()
    c2 = C()
    a = A()
    b = B()

    if_then_else_1 = IfThenElse(a, c1, c2)
    if_then_else_2 = IfThenElse(a, c1)
    if_then_else_3 = IfThenElse(a, else_clause=c2)
    if_then_else_4 = IfThenElse(a)


# Generated at 2022-06-14 14:16:35.078604
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():

    class Integer(Field):

        def validate_cast(self, value: typing.Any) -> typing.Any:
            return int(value)

        def to_primitive(self, value: typing.Any, context: typing.Any) -> typing.Any:
            return int(value)

    class Condition(Field):

        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            return value != 0

        def to_primitive(self, value: typing.Any, context: typing.Any) -> typing.Any:
            return str(value)

    class Condition2(Field):

        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            return value == 0


# Generated at 2022-06-14 14:16:40.476802
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    error_msg = None
    result = None
    try:
        result = NeverMatch()
    except Exception as e:
        error_msg = str(e)
    assert error_msg == None, "exception: " + str(error_msg)
    assert result != None, "result: " + str(result)


# Generated at 2022-06-14 14:16:44.095821
# Unit test for method validate of class Not
def test_Not_validate():
    n1 = Not(1)
    assert n1.validate(2) == 2
    with pytest.raises(ValidationError):
        n1.validate(1)



# Generated at 2022-06-14 14:16:54.116416
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    json_data = {
      "oneOf": [
        {
          "type": "object",
          "properties": {
            "name": {
              "type": "string"
            }
          },
          "required": [
            "name"
          ]
        },
        {
          "type": "object",
          "properties": {
            "age": {
              "type": "integer"
            }
          },
          "required": [
            "age"
          ]
        }
      ]
    }
    oneOf_obj = OneOf(json_data["oneOf"])
    assert(oneOf_obj.validate({"name": "lulu"}) == {"name": "lulu"})
    assert(oneOf_obj.validate({"age": 25}) == {"age": 25})
   

# Generated at 2022-06-14 14:17:08.647493
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    from typesystem import Integer
    from typesystem.fields import Union, Boolean, String

    class MyUnion(Union):
        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            super().validate(value, strict)
            # Add custom validation here
            if value == 'pippo':
                raise self.validation_error("no_match")

    # Case 1 before validation
    field = IfThenElse(
        if_clause=Boolean(true_values=("yes", ), false_values=("no", )),
        then_clause=MyUnion(Integer(), String()),
        else_clause=Integer()
    )
    field.validate("yes")
    field.validate("no")
    field.validate("pippo")
    assert field

    # Case

# Generated at 2022-06-14 14:17:12.870917
# Unit test for method validate of class Not
def test_Not_validate():
    #
    # Should NOT validate value which DOES match negated clause
    #
    def _test_Not_validate_x(self, value: typing.Any, strict: bool = False) -> typing.Any:
        _, error = self.negated.validate_or_error(value, strict=strict)
        if error:
            return value
        raise self.validation_error("negated")
    res = _test_Not_validate_x(self=Not(negated=Field(name="test")), value=123)
    assert res is not None
    #
    # Should validate value which does not match negated clause
    #
    def _test_Not_validate_y(self, value: typing.Any, strict: bool = False) -> typing.Any:
        _, error = self.negated.valid

# Generated at 2022-06-14 14:17:16.869179
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    if_clause = Field()
    if_clause_true = Field()
    if_clause_true.validate_or_error = MagicMock(return_value=(None, None))
    if_clause_false = Field()
    if_clause_false.validate_or_error = MagicMock(return_value=(None, ""))
    then_clause = Field()
    then_clause.validate = MagicMock()
    else_clause = Field()
    else_clause.validate = MagicMock()
    obj = IfThenElse(if_clause)
    obj.validate("")
    if_clause.validate_or_error.assert_called_once()
    then_clause.validate.assert_not_called()

# Generated at 2022-06-14 14:17:29.300807
# Unit test for constructor of class AllOf
def test_AllOf():
    from typesystem import String, Integer

    a = String()
    b = Integer()
    c = String()
    d = String()

    all_of = [a,b]
    not_of = [c,d]
    if_clause = a
    then_clause = b

    error_fields = [a,b,c,d]
    one_of = OneOf(all_of)
    all_of_field = AllOf(all_of)
    not_field = Not(all_of_field)
    if_then_else_field = IfThenElse(
        if_clause = if_clause,
        then_clause = then_clause
    )
    # test errors list is a list
    assert isinstance(one_of.errors, list)
    # test OneOf.__init

# Generated at 2022-06-14 14:17:33.031386
# Unit test for constructor of class OneOf
def test_OneOf():
    test = OneOf([])
    assert test.one_of == []
    assert test.errors == {"no_match": "Did not match any valid type.",
                           "multiple_matches": "Matched more than one type."
                           }


# Generated at 2022-06-14 14:17:35.942505
# Unit test for method validate of class Not
def test_Not_validate():
    value = 1
    strict = False
    field = Not(Int())

    assert field.validate(value, strict) == value

# Generated at 2022-06-14 14:17:45.490431
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    from typesystem.fields import String

    text = String()
    good_text = IfThenElse(
        if_clause=text,
        then_clause=String(min_length=5, max_length=10),
        else_clause=String(min_length=5, max_length=10),
    )
    good_text.validate("good text")
    good_text.validate("good text", strict=True)
    # TODO: change validation error message to "min_length" when all JS
    # implementations have been updated
    with pytest.raises(text.validation_error, match="minLength"):
        good_text.validate("bad")

# Generated at 2022-06-14 14:17:47.115590
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    assert isinstance(IfThenElse(AllOf([Integer()])), IfThenElse)

# Generated at 2022-06-14 14:17:53.931383
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    from typesystem.fields import String
    from typesystem.types import Schema
    class EmployeeSchema(Schema):
        full_name = IfThenElse(
            if_clause=String(max_length=50),
            then_clause=String(min_length=3),
            else_clause=String(max_length=50)
        )

    schema = EmployeeSchema(full_name='1234')
    schema.validate()

    schema = EmployeeSchema(full_name='12345678901')
    assert 'Invalid type' in schema.validate()

# Generated at 2022-06-14 14:17:56.256992
# Unit test for method validate of class Not
def test_Not_validate():
    not_field = Not(Boolean())
    print(not_field.validate(1))
    print(not_field.validate(None))
    print(not_field.validate(True))

# Generated at 2022-06-14 14:18:04.139833
# Unit test for constructor of class Not
def test_Not():
    int_field = typesystem.Integer()
    n = Not(int_field)
    print(type(n))
    print(type(n.negated))


# Generated at 2022-06-14 14:18:08.016524
# Unit test for method validate of class Not
def test_Not_validate():
    from typesystem.fields import Integer
    from typesystem.fields import Not
    from typesystem.fields import ValidationError

    field = Not(Integer())
    value = 5
    try:
        field.validate(value)
    except ValidationError:
        assert True
    else:
        assert False


# Generated at 2022-06-14 14:18:12.642414
# Unit test for method validate of class Not
def test_Not_validate():
    not_type = Not(Field())

    # successful validation returns the input value
    assert not_type.validate(1) == 1
    assert not_type.validate(None) is None
    assert not_type.validate("abc") == "abc"

    # failed validation raises an error
    with pytest.raises(ValidationError):
        not_type.validate(0)


# Generated at 2022-06-14 14:18:24.370799
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    one_of = [
        String(),
        Integer(),
    ]
    data_input_single = "test" #success
    data_input_multiple = 123 #fail
    data_input_none = True #fail

    field = OneOf(one_of)
    value, error = field.validate_or_error(data_input_single)
    assert value == data_input_single
    assert error is None

    field = OneOf(one_of)
    value, error = field.validate_or_error(data_input_multiple)
    assert value == data_input_multiple
    assert error is not None
    assert error.code == "multiple_matches"

    field = OneOf(one_of)
    value, error = field.validate_or_error(data_input_none)

# Generated at 2022-06-14 14:18:28.596154
# Unit test for constructor of class Not
def test_Not():
    one_of_list = [
        typesystem.String(),
    ]
    negated = typesystem.Not(
        typesystem.OneOf(
            one_of_list
        )
    )

    assert negated.negated.one_of == [
            typesystem.String(),
        ]

# Generated at 2022-06-14 14:18:31.907813
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    class TestField(Field):
        def validate(self, value, strict=False):
            return value

    assert IfThenElse(TestField()).validate(1) == 1
    with pytest.raises(FieldValidationError):
        IfThenElse(TestField(), TestField(required=True)).validate(1)

# Generated at 2022-06-14 14:18:34.151186
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
  testNeverMatch = NeverMatch()
  assert isinstance(testNeverMatch, NeverMatch)


# Generated at 2022-06-14 14:18:43.715076
# Unit test for constructor of class OneOf
def test_OneOf():
    def test_if_init():
        one_of = [Number(), String(format="email")]
        t = OneOf(one_of, format="email")
        assert t.format == "email"
        assert t.one_of == one_of
        assert t.errors == {
            "no_match": "Did not match any valid type.",
            "multiple_matches": "Matched more than one type."
        }
    test_if_init()

    def test_if_validate():
        one_of = [Number(), String(format="email")]
        t = OneOf(one_of, format="email")
        value, error = t.validate_or_error(10)
        assert value == 10
        assert error is None

# Generated at 2022-06-14 14:18:47.831210
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    data = 1
    if_clause = Any()
    then_clause = Any()
    field = IfThenElse(if_clause, then_clause)
    field.validate(data, True)

# Generated at 2022-06-14 14:18:51.484163
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    all_of = AllOf([Int(), Str()])
    assert all_of.validate(None, True) is None
    assert all_of.validate("1", True) == "1"
    assert all_of.validate(1, True) == 1
    with pytest.raises(ValidationError) as excinfo:
        Int().validate(None, True)
    assert str(excinfo.value) == "None is not of type 'number'"
    with pytest.raises(ValidationError) as excinfo:
        Int().validate("1", True)
    assert str(excinfo.value) == '"1" is not of type \'number\''

# Generated at 2022-06-14 14:19:02.508000
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    class SubType(Field):
        errors = {"mismatch": "Did not match any valid type."}

        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            if value != "subtype":
                raise self.validation_error("mismatch")
            return value

    if_clause = SubType()
    then_clause = SubType()
    else_clause = SubType()

    if_then_else = IfThenElse(if_clause, then_clause, else_clause)
    result = (if_then_else.validate(value="subtype"))
    assert result == "subtype"

    result = (if_then_else.validate(value="type"))
    assert result == "type"

# Generated at 2022-06-14 14:19:07.857635
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    #Test1: Type of value is not in one_of
    one_of = [Field(), Field()]
    oneOfField = OneOf(one_of, required=True)
    with pytest.raises(Exception):
        oneOfField.validate("foo")
    #Test2: Type of value is in one_of
    one_of = [Field(), String()]
    oneOfField = OneOf(one_of, required=True)
    oneOfField.validate("foo")


# Generated at 2022-06-14 14:19:11.354343
# Unit test for constructor of class Not
def test_Not():
    print("Test Not")
    str_field = typesystem.String(max_length=10)
    field = Not(str_field)
    print(field)

test_Not()


# Generated at 2022-06-14 14:19:13.418428
# Unit test for constructor of class Not
def test_Not():
    try:
        Not(None)
    except:
        return False
    return True


# Generated at 2022-06-14 14:19:15.553446
# Unit test for constructor of class OneOf
def test_OneOf():
    field = OneOf([typesystem.String()])
    assert field.one_of.__class__.__name__ == "List"
    assert field.one_of[0].__class__.__name__ == "String"


# Generated at 2022-06-14 14:19:21.997031
# Unit test for method validate of class Not
def test_Not_validate():
    notField = Not(String())
    assert notField.validate(0) is None
    assert notField.validate(1) is None
    assert notField.validate(1.0) is None
    assert notField.validate(True) is None
    assert notField.validate("") is None
    assert notField.validate("""{"spam": "eggs"}""") is None
    with pytest.raises(notField.validation_error):
        notField.validate("spam")


# Generated at 2022-06-14 14:19:30.645981
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    from typesystem import Integer, String
    s = OneOf([Integer, String], min_length=1, max_length=2)
    assert s.validate(1) == 1
    assert s.validate("12") == "12"
    error = s.validate("123")
    assert error.__class__.__name__ == "ValidationError"
    assert str(error) == "Ensure this value has at most 2 characters (it has 3)."
    error = s.validate("")
    assert error.__class__.__name__ == "ValidationError"
    assert str(error) == "Ensure this value has at least 1 characters (it has 0)."

# Generated at 2022-06-14 14:19:34.902016
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    type_list = []
    type_list.append(Integer())
    type_list.append(Float())
    type_list.append(String())
    item = OneOf(type_list)
    result = item.validate(5)
    assert result == 5
    try:
        result = item.validate(3.5)
        assert result == 3.5
    except ValidationError:
        assert False
    try:
        result = item.validate("5")
        assert result == "5"
    except ValidationError:
        assert False
    try:
        result = item.validate(None)
        assert False
    except ValidationError:
        assert True


# Generated at 2022-06-14 14:19:44.379813
# Unit test for constructor of class AllOf
def test_AllOf():
    my_all_of = AllOf(
        [Any(), Field()]
    )
    assert my_all_of == "AllOf"
    assert my_all_of.all_of == [Any(), Field()]
    assert my_all_of.check_types == True
    assert my_all_of.name == "AllOf"
    assert my_all_of.error_messages == {}
    assert my_all_of.description == ""
    assert my_all_of.example == None
    assert my_all_of.name == "AllOf"
    assert my_all_of.allow_coercion == True
    assert my_all_of.allow_reuse == True



# Generated at 2022-06-14 14:19:47.725857
# Unit test for constructor of class Not
def test_Not():
    from typesystem.types import Integer
    from typesystem import errors

    integer = Integer()
    not_integer = Not(integer)

    assert not_integer.validate(2)
    try:
        not_integer.validate(1)
    except errors.ValidationError:
        pass
    else:
        assert False

# Generated at 2022-06-14 14:20:03.811908
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    # simple test case
    I = IfThenElse(Int())
    assert I.validate(5) == 5

    # test if_clause
    I = IfThenElse(Int(),then_clause=Float())
    assert I.validate(5) == 5.0
    #test else_clause
    I = IfThenElse(Int(),Int(),Float())
    assert I.validate(5.0) == 5.0
    #test fail case
    I = IfThenElse(Int(),then_clause=Float(),else_clause=Int())
    assert I.validate(5.1) == 5


# Generated at 2022-06-14 14:20:07.847081
# Unit test for method validate of class Not
def test_Not_validate():
    from typesystem.error_wrappers import ValidationError

    field = Not(
        Field(name='not_pass_validation'),
    )
    try:
        field.validate('test')
    except ValidationError:
        pass
    except Exception as e:
        raise e
    else:
        assert False, 'Exception not raised'

# Generated at 2022-06-14 14:20:19.324609
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    class FieldStub(Field):
        def validate(self, value, strict=False):
            return "if"
        def validate_or_error(self, value, strict=False):
            return "if"
    class FieldStub1(Field):
        def validate(self, value, strict=False):
            return "then"
        def validate_or_error(self, value, strict=False):
            return "then"
    class FieldStub2(Field):
        def validate(self, value, strict=False):
            return "else"
        def validate_or_error(self, value, strict=False):
            return "else"
    field = FieldStub()
    field1 = FieldStub1()
    field2 = FieldStub2()

# Generated at 2022-06-14 14:20:22.544673
# Unit test for method validate of class Not
def test_Not_validate():
    x = Not(negated=Any())
    res = x.validate(1)
    assert res == 1
    res = x.validate(1, strict=True)
    assert res == 1

# Generated at 2022-06-14 14:20:31.167210
# Unit test for method validate of class Not
def test_Not_validate():
    from typesystem.typing import Optional
    from typesystem import Integer
    import pytest
    from app.models.typesystem_extension import Not

    # 1. Arrange
    schema: Not = Not(Integer())
    # 1.1. Prepare for validating
    # 1.1.1. Data type is right
    strict_data_type: int = 1
    # 1.1.2. Data type is wrong, but can auto convert
    not_strict_data_type: int = 2.1
    # 1.1.3. Data type isn't right and can't auto convert
    wrong_data_type: str = '0.1'

    # 2. Act
    # 2.1. Strict mode

# Generated at 2022-06-14 14:20:34.633263
# Unit test for constructor of class OneOf
def test_OneOf():
    expected = OneOf(OneOf)
    actual = OneOf(OneOf)
    assert expected == actual
    # Unit test for method 'validate' of class OneOf


# Generated at 2022-06-14 14:20:37.438741
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    field = NeverMatch()
    assert field.errors == {"never": "This never validates."}
    assert field.name == 'None'


# Generated at 2022-06-14 14:20:43.835944
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    # initialize and create a IfThenElse object
    if_clause = Field().validate
    then_clause = Field().validate
    else_clause = Field().validate
    if_then_else = IfThenElse(if_clause,then_clause, else_clause)
    value = "2019-01-10"
    strict = False
    # test if the function will return value of else_clause
    excepted = if_then_else.if_clause(value,strict)
    assert excepted == value



# Generated at 2022-06-14 14:20:51.369475
# Unit test for constructor of class OneOf
def test_OneOf():
    from typesystem.fields import Integer
    from typesystem.types import String
    from typesystem.fields import Union
    from typesystem.fields import Object
    from typesystem.fields import Array
    from typesystem.types import Boolean
    from typesystem.fields import Not
    from typesystem.fields import Null
    from typesystem.fields import Composite
    from typesystem.fields import Dict
    from typesystem.fields import Any
    from typesystem.fields import AllOf
    from typesystem.fields import OneOf
    from typesystem.fields import IfThenElse
    OneOf({})


# Generated at 2022-06-14 14:20:53.351958
# Unit test for method validate of class Not
def test_Not_validate():
    a = Not(None)
    assert a.validate("true") == "true"
    try:
        a.validate("false")
    except:
        assert True
    else:
        assert False

# Generated at 2022-06-14 14:21:24.916550
# Unit test for constructor of class AllOf
def test_AllOf():
    ao = AllOf(all_of=[])
    assert ao is not None
    assert ao.all_of is not None
    assert len(ao.all_of) == 0
    # Unit test for function validate of class AllOf
    def test_AllOf_validate(self):
        # Unit test for function validate of class AllOf
        def test_AllOf_validate_strict_false(self):
            class StringField(Field):
                errors = {"invalid": "Please enter a string."}
                def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
                    return value
            class NumberField(Field):
                errors = {"invalid": "Please enter a number."}

# Generated at 2022-06-14 14:21:27.933211
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    v1 = Any()
    v2 = Any()
    oo = OneOf([v1, v2])

    # 0 match
    with pytest.raises(oo.validation_error):
        oo.validate(None)
    # 1 match
    assert oo.v

# Generated at 2022-06-14 14:21:30.499714
# Unit test for method validate of class Not
def test_Not_validate():
    assert Not(negated=Any()).validate(1) == 1
    try:
        assert Not(negated=Any()).validate(None)
    except Exception as e:
        assert e.message == "Must not match."

# Generated at 2022-06-14 14:21:31.730130
# Unit test for constructor of class Not
def test_Not():
    not_field = Not(None)
    assert not_field.negated == None


# Generated at 2022-06-14 14:21:33.426637
# Unit test for constructor of class AllOf
def test_AllOf():
    all_of = [1]
    assert AllOf(all_of).all_of == all_of

# Generated at 2022-06-14 14:21:34.712735
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    assert NeverMatch(name='xxx').name == 'xxx'



# Generated at 2022-06-14 14:21:44.623287
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    one_of = OneOf([AlwaysMatch(), NeverMatch()])
    all_of = AllOf([AlwaysMatch(), NeverMatch()])
    not_ = Not(one_of)
    if_then_else = IfThenElse(one_of, AlwaysMatch(), AlwaysMatch())
    if_then_else1 = IfThenElse(one_of, then_clause=AlwaysMatch(), else_clause=AlwaysMatch())
    if_then_else2 = IfThenElse(one_of, then_clause=AlwaysMatch(), else_clause=Not(one_of))
    if_then_else3 = IfThenElse(one_of, then_clause=Not(one_of), else_clause=AlwaysMatch())

# Generated at 2022-06-14 14:21:51.283405
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    if_clause = Field(max_length=10)
    then_clause = Field(min_length=5)
    else_clause = Field(min_length=20)
    test = IfThenElse(if_clause,then_clause,else_clause)
    assert test.validate("123456789") == "123456789"
    assert test.validate("1234567890") == "1234567890"
    assert test.validate("12345678900") == "12345678900"
    

# Generated at 2022-06-14 14:21:52.600822
# Unit test for constructor of class Not
def test_Not():
    a = Not()
    print(a)


# Generated at 2022-06-14 14:21:57.938845
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    import typesystem
    schema = typesystem.Schema(
        fields={
            "one_of": OneOf(
                [typesystem.Integer(), typesystem.String()],
                description="Field 'one_of' must match exactly one of the sub-items.",
            )
        }
    )
    errors_dict = schema.validate({"one_of": 1})
    assert errors_dict == {}


# Generated at 2022-06-14 14:22:19.945120
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    from typesystem import Integer, Number, Schema

    class CustomSchema(Schema):
        x = IfThenElse(
            if_clause=Integer(minimum=5),
            then_clause=Integer(maximum=10),
            else_clause=Number(multiple_of=10),
        )

    try:
        CustomSchema({"x": 4})
    except:
        pass



# Generated at 2022-06-14 14:22:20.697335
# Unit test for constructor of class OneOf
def test_OneOf():
    assert OneOf([])


# Generated at 2022-06-14 14:22:23.371068
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    actual = IfThenElse(if_clause=Field(), then_clause=Field(), else_clause=Field()).validate({}, True)
    expected = {}
    assert actual == expected



# Generated at 2022-06-14 14:22:24.358879
# Unit test for constructor of class Not
def test_Not():
    # Should create a Not object
    assert Not(Any())


# Generated at 2022-06-14 14:22:25.898173
# Unit test for constructor of class AllOf
def test_AllOf():
    from typesystem.fields import Integer
    f1 = Integer()
    field = AllOf([f1])
    assert field.all_of == [f1]


# Generated at 2022-06-14 14:22:27.707538
# Unit test for constructor of class OneOf
def test_OneOf():
    assert OneOf([Any()]).one_of == [Any()]

# Generated at 2022-06-14 14:22:31.348339
# Unit test for constructor of class Not
def test_Not():
    with pytest.raises(AssertionError):
        f = Not(negated=True, allow_null=True) # type: ignore

    f = Not(negated=True)
    assert f.negated is True

# Unit tests for constructor of class IfThenElse

# Generated at 2022-06-14 14:22:34.178255
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    test = NeverMatch()
    assert test.label is None
    assert test.source is None
    assert test.metadata == {}
    assert test.errors == {"never": "This never validates."}
