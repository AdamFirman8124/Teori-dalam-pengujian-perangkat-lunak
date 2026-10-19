

# Generated at 2022-06-14 14:12:53.536442
# Unit test for method validate of class Not
def test_Not_validate():
    class MyNot(Not):
        base_error_message = "not_validate_test"
    negated = NeverMatch(required=True)
    my_not = MyNot(negated)
    my_not.validate(True)
    my_not.validate(True, required=True)
    with pytest.raises(ValidationError, match="not_validate_test"):
        my_not.validate(True, strict=True)
    with pytest.raises(ValidationError, match="not_validate_test"):
        my_not.validate(True, strict=True, required=True)



# Generated at 2022-06-14 14:13:05.825767
# Unit test for method validate of class OneOf

# Generated at 2022-06-14 14:13:08.489297
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    x = IfThenElse(if_clause=None, then_clause=None, else_clause=None)
    assert x.if_clause == None

# Generated at 2022-06-14 14:13:19.103035
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    f = IfThenElse(if_clause= OneOf(one_of=[Field()]), then_clause=Field())
    assert f.validate(1, strict=True) == Field().validate(1, strict=True)
    f = IfThenElse(if_clause= OneOf(one_of=[Field()]), then_clause=Field())
    assert f.validate(None, strict=True) == Field().validate(None, strict=True)
    f = IfThenElse(if_clause= OneOf(one_of=[Field(), NeverMatch()]), then_clause=Field())
    assert f.validate(1, strict=True) == Field().validate(1, strict=True)
    f = IfThenElse(if_clause= NeverMatch(), else_clause= Field())
    assert f.valid

# Generated at 2022-06-14 14:13:23.354359
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    oneof = OneOf([Field(), Field()])
    # should fail
    try:
        oneof.validate(1)
        assert False
    except ValidationError:
        pass
    # should pass
    oneof.validate(1, strict=True)

# Generated at 2022-06-14 14:13:28.611575
# Unit test for constructor of class OneOf
def test_OneOf():
    field = OneOf([], label="OneOf_label")
    assert field.label == "OneOf_label"
    assert field.errors == {
        "no_match": "Did not match any valid type.",
        "multiple_matches": "Matched more than one type.",
    }


# Generated at 2022-06-14 14:13:39.716070
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    class Number(Field):
        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            return value
    class Integer(Number):
        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            return value
    class String(Field):
        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            return value


    integer = Integer()
    string = String()
    if_clause = integer
    then_clause = string
    else_clause = string
    ite = IfThenElse(if_clause, then_clause, else_clause)
    assert ite.validate(0) == 0
    assert ite.validate('hello') == 'hello'




# Unit test

# Generated at 2022-06-14 14:13:48.454961
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    from typesystem.fields import Integer
    if_clause = Integer(minimum=1, maximum=10)
    then_clause = Integer(minimum=4, maximum=10)
    else_clause = Integer(minimum=10, maximum=20)
    field = IfThenElse(if_clause, then_clause, else_clause)
    assert field.validate(5) == 5
    assert field.validate(11) == 11
    assert field.validate(3, strict=True) == 4
    assert field.validate(21, strict=True) == 20

# Generated at 2022-06-14 14:13:57.367500
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    """
    If the result of if_clause validation is None, if_clause is valid.
    Else, else_clause is valid.
    """
    class NumberField(Field):
        errors = {"invalid": "Number is invalid."}
        def validate(self, value, strict=False):
            try:
                return int(value)
            except ValueError:
                raise self.validation_error("invalid")

    class ExpectedField(Field):
        def validate(self, value, strict=False):
            return value
    expected = ExpectedField()

    # If the value matches if_clause, then_clause is expected
    assert expected == IfThenElse(NumberField(), expected, Any())
    assert expected != IfThenElse(NumberField(), Any(), expected)

# Generated at 2022-06-14 14:13:58.635010
# Unit test for constructor of class AllOf
def test_AllOf():
    assert AllOf



# Generated at 2022-06-14 14:14:04.068262
# Unit test for constructor of class OneOf
def test_OneOf():
    try:
        b1 = OneOf([])
    except Exception as e:
        b1 = None
    assert b1 == None


# Generated at 2022-06-14 14:14:05.980113
# Unit test for method validate of class Not
def test_Not_validate():
    field = Not(Any())
    assert field.validate(1) == 1

# Generated at 2022-06-14 14:14:08.289769
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    # object to be tested
    object = IfThenElse(if_clause=0, then_clause=0, else_clause=0)

    # actual result
    result = object.validate(value=0, strict=0)

    # expected result
    expected = None

    # assert
    assert result == expected


# Generated at 2022-06-14 14:14:10.430760
# Unit test for constructor of class Not
def test_Not():
    value = "test"
    assert Not(Not(Any()), nullable=False).validate(value) == value


# Generated at 2022-06-14 14:14:11.930980
# Unit test for method validate of class Not
def test_Not_validate():
    negative = Not(String())
    negative.validate("test string")

# Generated at 2022-06-14 14:14:13.502419
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    f = NeverMatch()
    assert f


# Generated at 2022-06-14 14:14:18.792777
# Unit test for constructor of class OneOf
def test_OneOf():
    o1 = NeverMatch()
    o2 = NeverMatch()
    o3 = NeverMatch()
    o = OneOf([o1, o2, o3])
    assert o is not None


# Generated at 2022-06-14 14:14:28.668922
# Unit test for method validate of class Not
def test_Not_validate():
    # Creation of a Not object
    negated = AlwaysMatch()
    a = Not(negated)

    # Match: value = 1
    value = 1
    strict = False
    object_returned = a.validate(value, strict)
    assert object_returned == value
    assert object_returned == 1

    # No match: value = 0
    value = 0
    strict = False
    with pytest.raises(ValidationError) as e_info:
        a.validate(value, strict)
    assert str(e_info.value) == "Must not match."

    # No match: value = 2.5
    value = 2.5
    strict = False
    with pytest.raises(ValidationError) as e_info:
        a.validate(value, strict)

# Generated at 2022-06-14 14:14:33.399930
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    from typesystem import string_field, integer_field

    assert IfThenElse(
        if_clause=string_field(),
        then_clause=integer_field()).validate("5") == 5
    assert IfThenElse(
        if_clause=string_field(),
        then_clause=integer_field()).validate(5) == 5


# Generated at 2022-06-14 14:14:36.952539
# Unit test for method validate of class Not
def test_Not_validate():
    field = Not(negated=AllOf(all_of=[Any()]))
    assert field.validate(1) == 1
    try:
        field.validate(1)
    except ValidationError as e:
        assert e.code == "negated"
    else:
        raise AssertionError("Test failed!")



# Generated at 2022-06-14 14:14:41.001620
# Unit test for constructor of class Not
def test_Not():
    assert (Not(negated=bool()).negated == bool())

# Generated at 2022-06-14 14:14:44.814904
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    import typesystem

    nm = typesystem.NeverMatch()
    assert nm.name == "NeverMatch"
    assert nm.__class__.__name__ == "NeverMatch"



# Generated at 2022-06-14 14:14:52.268271
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    if_clause = String(min_length=5)
    then_clause = String(max_length=5)
    else_clause = String(min_length=5)
    field = IfThenElse(if_clause, then_clause, else_clause)
    # test case 1: if_clause matches
    value = '123456'
    result = field.validate(value)
    assert result == value
    # test case 2: if_clause does not match
    value = '12345'
    result = field.validate(value)
    assert result == value



# Generated at 2022-06-14 14:14:54.217341
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    fields = NeverMatch()
    assert fields.errors == {'never': 'This never validates.'}


# Generated at 2022-06-14 14:15:03.116460
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    schema = OneOf([
        Integer(min_value=1, max_value=10),
        Integer(min_value=10, max_value=20),
        Integer(min_value=20, max_value=30)
    ])
    validate_schema(schema, [{"value": 15, "errors": None},
                             {"value": 40, "errors": {'no_match': 'Did not match any valid type.'}},
                             {"value": 5, "errors": {'multiple_matches': 'Matched more than one type.'}}])


# Generated at 2022-06-14 14:15:08.864272
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    obj = OneOf(one_of=[Int(), Bool()], name="a")
    assert obj.validate(1) == 1
    with pytest.raises(ValidationError):
        obj.validate(1.0)
    with pytest.raises(ValidationError):
        obj.validate(None)
    assert obj.validate(True) is True



# Generated at 2022-06-14 14:15:18.708457
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    from typesystem import fields
    from typesystem.types import String
    from typesystem.exceptions import ValidationError
    from unittest import TestCase
    from typesystem.fields import IfThenElse

    class MyTestCase(TestCase):

        def test_IfThenElse_validate(self):
            field = IfThenElse(if_clause=Integer(), then_clause=String())
            with self.assertRaises(ValidationError):
                field.validate(1)
            self.assertEqual(field.validate(2), "2")

    MyTestCase().test_IfThenElse_validate()

# Generated at 2022-06-14 14:15:21.454788
# Unit test for constructor of class Not
def test_Not():
	a = Not(True, allow_none=False)
	assert a.allow_none == False
	assert a.errors == {'negated':'Must not match.'}


# Generated at 2022-06-14 14:15:31.922451
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    from typesystem import Integer

    # Unit test for method validate of class IfThenElse where if_clause is true
    value = 10
    strict = False
    expected_return_value = value
    if_clause = Integer(minimum=10)
    then_clause = Integer(maximum=10)
    else_clause = Integer(maximum=5)
    if_then_else = IfThenElse(
        if_clause=if_clause, then_clause=then_clause, else_clause=else_clause
    )
    return_value = if_then_else.validate(value, strict=strict)
    assert return_value == expected_return_value

    # Unit test for method validate of class IfThenElse where if_clause is false
    value = 10
    strict = False
    expected_return

# Generated at 2022-06-14 14:15:33.278547
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    field = IfThenElse(Any(), Any())
    field.validate(1)



# Generated at 2022-06-14 14:15:39.825190
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    field = OneOf(
        one_of=[
            String(),
            Number(),
            String(pattern=r"^test\d+$")
        ]
    )
    assert field.validate("test1") == "test1"
    assert field.validate(2) == 2
    try:
        field.validate("test")
        assert False
    except ValidationError:
        pass
    try:
        field.validate("3")
        assert False
    except ValidationError:
        pass


# Generated at 2022-06-14 14:15:50.931130
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    def validate_if_then_else(i, t, e, value):
        if_clause = Field()
        if_clause.validate_method = i
        then_clause = Field()
        then_clause.validate_method = t
        else_clause = Field()
        else_clause.validate_method = e
        return IfThenElse(if_clause, then_clause, else_clause).validate(value, strict=True)


# Generated at 2022-06-14 14:15:59.650644
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    from typesystem.exceptions import ValidationError
    from typesystem.fields import String, Integer

    field = OneOf([Integer(), String()])

    try:
        field.validate('Okey')
    except ValidationError:
        assert False
    
    try:
        field.validate(1234)
    except ValidationError:
        assert False
    
    try:
        field.validate(True)
        assert False
    except ValidationError:
        assert True
    
    try:
        field.validate('Okey', strict=True)
        assert False
    except ValidationError:
        assert True
    
    try:
        field.validate(1234, strict=True)
        assert False
    except ValidationError:
        assert True


# Generated at 2022-06-14 14:16:10.137372
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
        #test 1
        test = IfThenElse(if_clause=String(), then_clause=Int())
        result = test.validate(5)
        assert result == 5

        #test 2
        test = IfThenElse(if_clause=String(), then_clause=Int())
        result = test.validate("5")
        assert result == "5"

        #test 3
        test = IfThenElse(if_clause=String(), then_clause=Int(), else_clause=Int())
        result = test.validate("5")
        assert result == "5"

        #test 4
        test = IfThenElse(if_clause=String(), then_clause=Int(), else_clause=Int())
        result = test.validate(5)
        assert result == 5

        #test 5


# Generated at 2022-06-14 14:16:15.081468
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    print("test_OneOf_validate\n")
    field = OneOf([Int(), Bool()])
    print("1")
    print(field.validate(1))
    print("True")
    print(field.validate(True))
    print("'1'")
    print(field.validate("1"))




# Generated at 2022-06-14 14:16:18.044282
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    # test case 1
    input_value = 1
    expected_result = 1
    actual_result = OneOf([Any()]).validate(input_value)
    assert expected_result == actual_result


# Generated at 2022-06-14 14:16:20.010558
# Unit test for constructor of class Not
def test_Not():
    not_field = Not(negated=None)
    assert not_field.negated == None

# Generated at 2022-06-14 14:16:31.197202
# Unit test for method validate of class OneOf
def test_OneOf_validate():

    dog = {
        "name": "Scooby",
        "breed": "Dane",
        "age": 50,
        "personality": ["friendly", "gentle", "shy"],
        "family": [
            {"name": "Fred", "age": 15},
            {"name": "Velma", "age": 20, "favorite_dessert": "cheesecake"},
            {"name": "Daphne", "age": 18},
            {"name": "Shaggy", "age": 19},
        ],
    }

    s = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "age": {"type": "integer"},
            "location": {"type": "string", "default": "Mystery Mansion"},
        },
    }
    schema = One

# Generated at 2022-06-14 14:16:34.331415
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    one_of = [{'type': 'number'}, {'type': 'string'}]
    field = OneOf(one_of)
    assert field.validate(1) == 1
    assert field.validate('1') == '1'

# Generated at 2022-06-14 14:16:35.711729
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    f = NeverMatch()

    assert isinstance(f, NeverMatch)



# Generated at 2022-06-14 14:16:43.442600
# Unit test for constructor of class AllOf
def test_AllOf():
    import typesystem
    schema = typesystem.Schema(
        properties = {'title': {'type': 'string'}, 'description': {'type': 'string'}},
        required = ['description', 'title']
    )
    AllOf(schema)


# Generated at 2022-06-14 14:16:45.743283
# Unit test for constructor of class Not
def test_Not():
    negated = Not(then_clause="test")
    assert negated.then_clause == "test"


# Generated at 2022-06-14 14:16:50.889275
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    with pytest.raises(AssertionError):
        IfThenElse(if_clause=Number(allow_null=False), then_clause=Any(allow_null=False), else_clause=String(allow_null=False), allow_null=True)
        # All of the arguments are not allowed to be True but the argument allow_null is True



# Generated at 2022-06-14 14:16:52.268506
# Unit test for constructor of class Not
def test_Not():
    assert Not(None).negated == None


# Generated at 2022-06-14 14:16:54.479634
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    """
    Test the method validate of class IfThenElse
    """
    _field = IfThenElse(None)
    assert _field.validate('a') == 'a'

# Generated at 2022-06-14 14:17:04.391402
# Unit test for constructor of class OneOf
def test_OneOf():
    class OneOf(Field):
        def __init__(self, one_of: typing.List[Field], **kwargs: typing.Any) -> None:
            super().__init__(**kwargs)
            self.one_of = one_of
    print('\n## Unit test for constructor of class OneOf')
    print('\tObjective: to check the correctness of constructor. ') 
    one_of = OneOf(['hello', 1, 'world'])
    assert one_of.one_of == ['hello', 1, 'world']
    print('\tSuccess: OneOf constructor test passed.')
    
test_OneOf()

# Generated at 2022-06-14 14:17:15.319519
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    class IfThenElseTest(Field):
        def __init__(self, if_clause: Field, then_clause: Field = None, else_clause: Field = None, **kwargs: typing.Any) -> None:
            super().__init__(**kwargs)
            self.if_clause = if_clause
            self.then_clause = Any() if then_clause is None else then_clause
            self.else_clause = Any() if else_clause is None else else_clause

        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            _, error = self.if_clause.validate_or_error(value, strict=strict)

# Generated at 2022-06-14 14:17:19.204669
# Unit test for constructor of class AllOf
def test_AllOf():
   class Name(Field):
      pass

   assert AllOf(all_of=[]).validate(23) == Name().validate(23)



# Generated at 2022-06-14 14:17:26.616889
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    # Test case data
    one_of_1 = [Number(), String()]
    kwargs_1 = {}
    value_1 = 2

    # Perform the test
    try:
        OneOf(one_of_1, **kwargs_1).validate(value_1)
    except Exception as e:
        print(f"Exception raised when performing test_OneOf_validate:\n{str(e)}")
        raise



# Generated at 2022-06-14 14:17:28.700622
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    assert IfThenElse(if_clause=Boolean(), then_clause=String()).validate(5)
test_IfThenElse_validate()

# Generated at 2022-06-14 14:17:35.730088
# Unit test for constructor of class OneOf
def test_OneOf():
    assert type(OneOf(one_of=[Any()])) == OneOf

# Generated at 2022-06-14 14:17:37.343756
# Unit test for constructor of class AllOf
def test_AllOf():
  x = AllOf(all_of = [])


# Generated at 2022-06-14 14:17:42.008203
# Unit test for constructor of class OneOf
def test_OneOf():
  one_of = OneOf(one_of=[Field(name='a', required=True, nullable=False), Field(name='b', required=True, nullable=False)])
  assert one_of.one_of[0].name == 'a'
  assert one_of.nullable == False


# Generated at 2022-06-14 14:17:46.315245
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    assert (NeverMatch(name="NeverMatch").__class__.__name__) == "NeverMatch"



# Generated at 2022-06-14 14:17:49.304924
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    from typesystem.fields import String, Integer

    schema = IfThenElse(Integer(), Integer(), String())
    assert schema.validate(1) == 1
    assert schema.validate("hello") == "hello"

# Generated at 2022-06-14 14:17:51.282273
# Unit test for constructor of class Not
def test_Not():
    not_field = Not(
        String()
    )
    assert not_field.__class__.__name__ == "Not"

# Generated at 2022-06-14 14:17:52.918167
# Unit test for constructor of class AllOf
def test_AllOf():
    A = AllOf(all_of=[])
    assert A is not None


# Generated at 2022-06-14 14:17:59.757588
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    if_clause = None
    then_clause = None
    else_clause = None
    if_clause = Field('if_clause')
    then_clause = Field('then_clause')
    else_clause = Field('else_clause')
    IfThenElse(if_clause, then_clause, else_clause)

    if_clause = Field('if_clause')
    then_clause = Field('then_clause')
    else_clause = Field('else_clause')
    IfThenElse(if_clause, None, else_clause)

    if_clause = Field('if_clause')
    then_clause = Field('then_clause')
    else_clause = Field('else_clause')

# Generated at 2022-06-14 14:18:09.816326
# Unit test for constructor of class OneOf
def test_OneOf():
    field = OneOf([
        {'type': 'string'},
        {'type': 'integer'},
        {'type': 'number'}
    ])
    assert field.name == 'one_of'
    assert field.one_of[0].name == 'string'
    assert field.one_of[1].name == 'integer'
    assert field.one_of[2].name == 'number'
    assert field.errors == {'no_match': 'Did not match any valid type.', 'multiple_matches': 'Matched more than one type.'}
    # Check that the new field is a valid field
    test_data = 'test'
    expected_result = 'test'
    assert field.validate(test_data) == expected_result, 'OneOf() field constructor failed'


# Generated at 2022-06-14 14:18:10.858862
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    assert NeverMatch().validate(5) == 5

# Generated at 2022-06-14 14:18:17.500820
# Unit test for constructor of class Not
def test_Not():
  not_ = Not(None)
  assert isinstance(not_, Field)


# Generated at 2022-06-14 14:18:20.267462
# Unit test for constructor of class AllOf
def test_AllOf():
    import typing
    from typesystem.fields import Integer, List, Field
    f = AllOf([List(items=Integer())])
    assert isinstance(f, Field)

# Generated at 2022-06-14 14:18:21.548973
# Unit test for constructor of class Not
def test_Not():
    # do nothing
    pass

# Generated at 2022-06-14 14:18:24.236613
# Unit test for constructor of class Not
def test_Not():
    '''Testing constructor of class Not'''
    negated = Any()
    not_field = Not(negated)
    assert not_field.negated == negated


# Generated at 2022-06-14 14:18:25.162633
# Unit test for constructor of class AllOf
def test_AllOf():
    assert AllOf != None


# Generated at 2022-06-14 14:18:29.679930
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    # Arrange
    if_clause = Field()
    then_clause = Field()
    else_clause = Field()
    field = IfThenElse(if_clause, then_clause, else_clause)

    # Act
    value = field.validate(object())

    # Assert
    assert value is not None


# Generated at 2022-06-14 14:18:30.813217
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    IfThenElse(Field,Field,Field).validate(value=None)

# Generated at 2022-06-14 14:18:32.239391
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    assert(not IfThenElse(1).validate(2))

# Generated at 2022-06-14 14:18:33.740094
# Unit test for constructor of class OneOf
def test_OneOf():
    assert one_of is not None


# Generated at 2022-06-14 14:18:36.579214
# Unit test for constructor of class Not
def test_Not():
    not_field = Not(None)
    if isinstance(not_field, Not):
        print("Yes, it is a Not")


# Generated at 2022-06-14 14:18:56.425532
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    import typesystem
    type_int_strict = typesystem.Integer()
    type_int_lenient = typesystem.Integer(strict=False)
    type_str_strict = typesystem.String()
    type_str_lenient = typesystem.String(strict=False)
    is_if_then_else_valid = IfThenElse(if_clause=type_int_strict, then_clause=type_str_strict, else_clause=type_str_lenient)
    print(is_if_then_else_valid.validate(1)) # should print '1'
    print(is_if_then_else_valid.validate(1.1)) # should print '1.1'
    print(is_if_then_else_valid.validate('1')) # should raise

# Generated at 2022-06-14 14:18:58.045150
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    try:
        NeverMatch()
    except TypeError:
        assert True

if __name__ == "__main__":
    test_NeverMatch()

# Generated at 2022-06-14 14:18:59.230620
# Unit test for constructor of class AllOf
def test_AllOf():
    field = AllOf([Field])
    assert field != None


# Generated at 2022-06-14 14:19:04.192173
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    test_field = NeverMatch()
    assert test_field.errors == {"never": "This never validates."}

# Unit tests for method validate of class NeverMatch
# 1. test if the field never validates the value

# Generated at 2022-06-14 14:19:06.220272
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    assert "hi" == IfThenElse(
        if_clause=Any(),
        else_clause=Any(),
        then_clause=Any(),
    ).validate("hi")

# Generated at 2022-06-14 14:19:07.659872
# Unit test for constructor of class Not
def test_Not():
    assert Not(None)


# Generated at 2022-06-14 14:19:18.792899
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    base_schema = types.Schema({
        'movie': types.Object({
            'name': types.String(),
            'year': types.Integer(),
            'date': types.Date(),
            'won': types.Boolean()
        }, allow_extra_attributes=False)})

    base_schema_2 = types.Schema({
        'movie': types.Object({
            'name': types.String(),
            'year': types.Integer(),
            'date': types.Date(),
            'won': types.Boolean()
        }, allow_extra_attributes=False)})


# Generated at 2022-06-14 14:19:20.249818
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    assert NeverMatch(name='NeverMatch') is not None


# Generated at 2022-06-14 14:19:27.199036
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    class Validator(IfThenElse):
        def __init__(self, if_clause: Field, then_clause: Field = None, else_clause: Field = None, **kwargs: typing.Any) -> None:
            assert "allow_null" not in kwargs
            super().__init__(if_clause, then_clause, else_clause, **kwargs)

    class Int(Field):
        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            try:
                value = int(value)
            except (TypeError, ValueError):
                raise self.validation_error("invalid_type")
            if self.minimum is not None and value < self.minimum:
                raise self.validation_error("too_small")

# Generated at 2022-06-14 14:19:29.015581
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    x = NeverMatch()
    assert x.errors == {"never": "This never validates."}


# Generated at 2022-06-14 14:19:58.982969
# Unit test for constructor of class Not
def test_Not():
    field = Not(negated=1)
    assert field.negated == 1

# Generated at 2022-06-14 14:20:02.575442
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    class test_NeverMatch(object):
        def __init__(self, **kwargs: typing.Any) -> None:
            assert "allow_null" not in kwargs
            super().__init__(**kwargs)
    x = test_NeverMatch(**kwargs)
    assert x

# Generated at 2022-06-14 14:20:03.841185
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    assert(NeverMatch().errors["never"] == "This never validates.")


# Generated at 2022-06-14 14:20:04.692377
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
  assert NeverMatch() is not None


# Generated at 2022-06-14 14:20:07.427494
# Unit test for constructor of class Not
def test_Not():
    assert (
        Not(negated=None).validate(None)
        is None  # type: ignore[name-defined,no-any-return,attr-defined]
    )

# Generated at 2022-06-14 14:20:08.552962
# Unit test for constructor of class OneOf
def test_OneOf():
    assert isinstance(OneOf({}), Field)


# Generated at 2022-06-14 14:20:09.790602
# Unit test for constructor of class AllOf
def test_AllOf():
    a = AllOf([String()])


# Generated at 2022-06-14 14:20:11.283174
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    with pytest.raises(Exception):
        NeverMatch()


# Generated at 2022-06-14 14:20:15.138592
# Unit test for constructor of class OneOf
def test_OneOf():
    field = OneOf([], **{})

    assert field.errors == {
        "no_match": "Did not match any valid type.",
        "multiple_matches": "Matched more than one type.",
    }

# Generated at 2022-06-14 14:20:25.499897
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    from typesystem import Integer
    from typesystem.fields import Any

    field = IfThenElse(
        if_clause=Integer(),
        then_clause=Integer(),
    )
    assert field.validate(12) == 12
    assert field.validate(12.0) == 12.0

    field = IfThenElse(
        if_clause=Integer(),
        then_clause=Integer(),
        else_clause=Any(),
    )
    assert field.validate(12) == 12
    assert field.validate(12.0) == 12.0

    field = IfThenElse(
        if_clause=Integer(),
        else_clause=Integer(),
    )
    assert field.validate(12.0) == 12.0

# Generated at 2022-06-14 14:21:06.020346
# Unit test for constructor of class AllOf
def test_AllOf():
    field = AllOf(
        all_of = [
            String(),
            String(),
            String(),
        ]
    )
    assert field.all_of[0].__class__.__name__ == 'String'
    assert field.all_of[1].__class__.__name__ == 'String'
    assert field.all_of[2].__class__.__name__ == 'String'

    field = AllOf(
        all_of = [
            String(),
            String(),
            String(),
        ],
        allow_null = True
    )
    assert field.allow_null == True

    field = AllOf(
        all_of = [
            String(),
            String(),
            String(),
        ],
        description = 'string description'
    )
    assert field.description == 'string description'



# Generated at 2022-06-14 14:21:13.518535
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    field1 = Integer(minimum=0)
    field2 = List(items=Integer(minimum=0))
    field3 = Boolean()
    field4 = List(items=Integer(maximum=0))
    field5 = Integer(maximum=0)
    field6 = Boolean()
    field = IfThenElse(if_clause=field3, then_clause=field2, else_clause=field4)
    value = [0, 1, 2]
    assert field.validate(value, strict=False) == value
    value = [1, 2, 3]
    field = IfThenElse(if_clause=field6, then_clause=field1, else_clause=field5)
    assert field.validate(value, strict=False) == value

# Generated at 2022-06-14 14:21:15.407763
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    c = NeverMatch()
    assert c.errors == {"never": "This never validates."}


# Generated at 2022-06-14 14:21:17.507797
# Unit test for constructor of class OneOf
def test_OneOf():
    from . import Int


# Generated at 2022-06-14 14:21:18.360378
# Unit test for constructor of class AllOf
def test_AllOf():
    AllOf(1)

# Generated at 2022-06-14 14:21:28.534621
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    import pytest
    from typesystem import AnyOf, Boolean, Integer, String
    from typesystem.exceptions import ValidationError
    from typesystem.error_wrappers import ErrorList

    schema = IfThenElse(Boolean(enum=[True]), String(), Integer())

    assert schema.validate(True) == True
    assert schema.validate(False) == 0

    with pytest.raises(ValidationError) as exc_info:
        schema.validate(123)

    errors = exc_info.value.errors

    assert len(errors) == 1
    assert errors[0]["error"] == "invalid_type"
    assert errors[0]["expected_type"] == "string"
    assert errors[0]["expected_subtypes"] == []
    assert errors[0]["actual_type"] == "integer"
   

# Generated at 2022-06-14 14:21:30.269384
# Unit test for constructor of class AllOf
def test_AllOf():
    from typesystem.fields import String
    all_of = AllOf( [ String(min_length=1) ] )
    assert all_of!=None

# Generated at 2022-06-14 14:21:36.142482
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    field = IfThenElse(if_clause=IfThenElse(if_clause=Boolean(), then_clause=String(), else_clause=Number()),
                       then_clause=Integer(),
                       else_clause=Array(items=String()))
    assert field.validate("true") == "true"
    assert field.validate("false") == 0.0
    assert field.validate("true") == 1
    assert field.validate("false") == ["false"]



# Generated at 2022-06-14 14:21:37.953518
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    # Test with empty constructor
    assert NeverMatch().validate("AnyValue") == "AnyValue"

# Generated at 2022-06-14 14:21:47.671497
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    import typesystem
    import numbers

    # Test method validate of class IfThenElse
    class Number(typesystem.Integer):
        """
        A type for numbers
        """

        def __init__(self, **kwargs: typing.Any) -> None:
            """
            Initialize a Number object
            """
            super().__init__(**kwargs)

        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            """
            Assert value is a number and return it if it is
            """
            if isinstance(value, numbers.Number) is False:
                raise self.validation_error("Value is not a number")
            return value


    # Test method validate of class IfThenElse
    class Code(typesystem.Integer):
        """
        A code
        """

       