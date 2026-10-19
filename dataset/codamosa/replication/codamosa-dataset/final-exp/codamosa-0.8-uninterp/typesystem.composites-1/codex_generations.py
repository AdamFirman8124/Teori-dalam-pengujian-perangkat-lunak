

# Generated at 2022-06-14 14:12:44.534857
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    o = OneOf([Any()])
    o.validate(1, strict=True)

# Generated at 2022-06-14 14:12:49.389540
# Unit test for constructor of class Not
def test_Not():
    data = 123
    n = Not(Integer())
    # should not raise an exception
    n.validate(data)
    # should raise an exception
    data = '123'
    with pytest.raises(ValidationError):
        n.validate(data)
    # should raise an exception
    data = 'test'
    with pytest.raises(ValidationError):
        n.validate(data)

# Generated at 2022-06-14 14:12:51.525646
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    """Test for method validate"""
    field_type = IfThenElse(Integer(), String())
    value = 5
    field_type.validate(value)

# Generated at 2022-06-14 14:12:59.200527
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    ## Test that if none of the fields match the given input, an error is returned
    # Create an instance of `AllOf`
    all_of = AllOf([])
    value = 'J'
    strict = False
    # Retrieve the method to be tested
    cls = OneOf
    validate_func = getattr(cls, 'validate')
    # Execute the method to be tested
    method_output = validate_func(all_of, value, strict)
    # Compare the output to the expected
    assert method_output == None


# Generated at 2022-06-14 14:13:00.283610
# Unit test for constructor of class OneOf
def test_OneOf():
    assert OneOf([]) is not None

# Generated at 2022-06-14 14:13:07.058840
# Unit test for method validate of class Not
def test_Not_validate():
    from typesystem import Schema

    class MySchema(Schema):
        field = Not(schema={
            "type": "number"
        })

    with raises(TypeError):
        MySchema({"field": "something else"})

    s = MySchema({"field": "something else"})
    assert s.is_valid(value={"field": "something else"}) == True

# Generated at 2022-06-14 14:13:11.829967
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    field = OneOf([
        Any(),
        Any(),
        Any(),
    ])

    # Test 1: test with no errors
    value, error = field.validate_or_error('hello')
    assert error is None
    assert value == 'hello'

    # Test 2: test with multiple errors
    value, error = field.validate_or_error({})
    assert error
    assert value is None

# Generated at 2022-06-14 14:13:16.623490
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    user_type = {
        "type": "object",
        "properties": {
            "firstname": {"type": "string"},
            "lastname": {"type": "string"}
        }
    }
    type_schema = TypeSchema(user_type)
    user = {
        "firstname": "John",
        "lastname": "Doe"
    }
    assert type_schema.validate(user) == user



# Generated at 2022-06-14 14:13:19.889339
# Unit test for method validate of class Not
def test_Not_validate():
    from typesystem import String
    not_string = Not(String())
    result, error = not_string.validate_or_error(123)
    assert error is None
    assert result == 123

# Generated at 2022-06-14 14:13:26.609902
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    int_field = Integer()
    str_field = String()
    one_of = OneOf([int_field, str_field])
    # First one matches
    assert one_of.validate("123") == 123
    # Second one matches
    assert one_of.validate("321") == "321"
    # No match
    try:
        one_of.validate("hello")
        assert False
    except FieldError as err:
        assert err.code == "no_match"

# Generated at 2022-06-14 14:13:37.284367
# Unit test for method validate of class Not
def test_Not_validate():
    s: Field = String(max_length=10)
    n: Field = Not(s)
    assert n.validate("valid_value") is None
    try:
        n.validate("invalid_value")
        raise AssertionError("Should have raised validation error")
    except ValidationError as e:
        assert e.code == "negated"
    assert n.to_json_schema() == {
        "title": "String",
        "type": "string"
    }

# Generated at 2022-06-14 14:13:48.821322
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    from typesystem.fields import String

    class Movie(metaclass=IfThenElse(String(max_length=3), String(min_length=3))):
        pass
    class Person(metaclass=IfThenElse(String(max_length=3), String(min_length=3))):
        pass
    movie = Movie(name="bat")
    person = Person(name="bat")
    print(movie.validate())
    print(person.validate())


test_IfThenElse_validate()


# Generated at 2022-06-14 14:13:57.628329
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    class A:
        pass
    a = A()
    # test the function with no arguments has no error
    result1 = IfThenElse(if_clause=Any()).validate(a)
    assert(result1 == a)
    result2 = IfThenElse(if_clause=Any(), then_clause=Any()).validate(a)
    assert(result2 == a)
    result3 = IfThenElse(if_clause=Any(), else_clause=Any()).validate(a)
    assert(result3 == a)
    result4 = IfThenElse(if_clause=Any(), then_clause=Any(), else_clause=Any()).validate(a)
    assert(result4 == a)
    # test the function with if_clause argument has error
    result5 = IfThenElse

# Generated at 2022-06-14 14:14:09.471068
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    """
    if_clause is a Field
    then_clause is a Field
    else_clause is a Field
    """
    # test if_clause not None
    if_clause = Field.get_instance({"type": str})
    test_if_clause = IfThenElse(if_clause)
    assert test_if_clause.if_clause.match("abc")
    assert not test_if_clause.if_clause.match(1)

    # test then_clause not None, else_clause None
    then_clause = Field.get_instance({"type": int})
    test_then_clause = IfThenElse(
        if_clause,
        then_clause=then_clause)
    assert test_then_clause.then_clause.match

# Generated at 2022-06-14 14:14:10.106624
# Unit test for method validate of class Not
def test_Not_validate():
    assert True==False

# Generated at 2022-06-14 14:14:23.134365
# Unit test for method validate of class Not
def test_Not_validate():
    import typesystem
    from typesystem.fields import Integer
    from typesystem.primitives import String
    from typesystem.exceptions import ValidationError

    # In this unit test, a dummy integer field is inserted into the field 'negated'
    # of Not.
    negated = Integer()
    base = typesystem.SimpleType()
    field = Not(negated, **base.get_init_kwargs())
    # Test the invalid values.
    for value in ('blah', 1.2, '1.2'):
        try:
            field.validate(value)
        except ValidationError:
            pass
        else:
            assert False, "Did not catch ValidationError when input value '{}' is not valid as an integer".format(value)
    # Test the valid value.

# Generated at 2022-06-14 14:14:28.333811
# Unit test for method validate of class Not
def test_Not_validate():
    assert 1==1
    not_obj = Not(negated=None)
    try:
        not_obj.validate("test")
    except Exception as e:
        assert e.code == "negated"
    try:
        not_obj.validate("")
    except Exception as e:
        assert e.code == "negated"



# Generated at 2022-06-14 14:14:30.957813
# Unit test for constructor of class OneOf
def test_OneOf():
    try:
        all_field = AllOf([])
    except AssertionError:
        pass
    else:
        raise AssertionError("failed to detect error")

# Generated at 2022-06-14 14:14:33.651119
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    testObject = NeverMatch(description="this is a description", title="title")
    assert testObject.description == "this is a description"
    assert testObject.title == "title"


# Generated at 2022-06-14 14:14:40.099232
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    if_field = Field()
    then_field = Field()
    else_field = Field()
    if_then_else_field = IfThenElse(
        if_field, then_field, else_field, error_messages={"required": "Test error"}
    )
    # Test non-matching if_field
    _, error = if_field.validate_or_error(123)
    assert error is None
    _, error = then_field.validate_or_error(123)
    assert error is not None
    _, error = else_field.validate_or_error(123)
    assert error is None
    validated = if_then_else_field.validate(123)
    assert validated == 123
    # Test matching if_field
    _, error = if_field.validate_or_

# Generated at 2022-06-14 14:14:48.757889
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    # These values are chosen as (1) can get it to happen, 
    # and (2) easy to check the answer
    # assert is the keyword used to verify something
    assert(IfThenElse(IfThenElse(Any(), Any()), Any()).validate(1))
    assert(IfThenElse(IfThenElse(Any(), Any()), Any(), Any()).validate(1))



# Generated at 2022-06-14 14:14:52.377225
# Unit test for method validate of class Not
def test_Not_validate():
    a = Field()
    n = Not(a)
    n.validate('not a')
    try:
        n.validate(a)
        assert False
    except ValidationError:
        assert True

# Generated at 2022-06-14 14:15:04.335731
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    import typesystem

    class Schema(typesystem.Schema):
        if_clause = typesystem.Boolean(default=False)
        then_clause = typesystem.String()
        else_clause = typesystem.Number()

        class Meta:
            fields = ['a', 'b', 'c']
            extra = typesystem.EXTRA_REMOVE

    schema = Schema()
    data = {'a': 1, 'b': 2, 'c': 3}
    assert schema.validate(data) == {'a': 1, 'b': 2, 'c': 3}

    schema = Schema(fields=['if_clause', 'then_clause', 'else_clause'])

# Generated at 2022-06-14 14:15:05.877386
# Unit test for constructor of class AllOf
def test_AllOf():
    data = []
    assert AllOf(data).all_of == data


# Generated at 2022-06-14 14:15:07.814616
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    result = IfThenElse.validate_IfThenElse(IfThenElse(), 4)
    assert result == 4

# Generated at 2022-06-14 14:15:14.698427
# Unit test for method validate of class Not
def test_Not_validate():
    # Initialize the field:
    negated = Any()
    not_field = Not(negated)

    # Tests with valid values:
    assert not_field.validate(None) == None
    assert not_field.validate(True) == True
    assert not_field.validate(False) == False
    assert not_field.validate(1) == 1
    assert not_field.validate(1.0) == 1.0
    assert not_field.validate(1j) == 1j
    assert not_field.validate('') == ''
    assert not_field.validate('asd') == 'asd'
    assert not_field.validate([]) == []
    assert not_field.validate([1, 2]) == [1, 2]
    assert not_field.validate({})

# Generated at 2022-06-14 14:15:22.900789
# Unit test for constructor of class OneOf
def test_OneOf():
    # Unit test for method validate of class OneOf
    class Field1(OneOf):
        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            return 1, None
    class Field2(OneOf):
        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            return 2, None
    Field = OneOf([Field1(), Field2()])
    assert Field.validate(1) == 1
    assert Field.validate(2) == 2


# Generated at 2022-06-14 14:15:28.389106
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    field = IfThenElse(
        if_clause = String(max_length = 4),
        then_clause = String(min_length = 2),
        else_clause = String(min_length = 5)
    )
    assert field.validate("abcd") == "abcd"
    assert field.validate("abcdefg") == "abcdefg"
    assert field.validate("a") is None

# Generated at 2022-06-14 14:15:29.584760
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    assert IfThenElse(Any(), Any()).validate('Hello') == 'Hello'


# Generated at 2022-06-14 14:15:31.090087
# Unit test for constructor of class AllOf
def test_AllOf():
    f = AllOf([])
    assert f is not None

# Generated at 2022-06-14 14:15:34.665296
# Unit test for constructor of class OneOf
def test_OneOf():
    assert isinstance(OneOf([Field]), OneOf)

# Generated at 2022-06-14 14:15:38.681982
# Unit test for method validate of class Not
def test_Not_validate():
	f = Not(Field(name="string"))
	x = "string"
	assert f.validate(x, strict=False)== x


# Generated at 2022-06-14 14:15:39.818216
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    assert NeverMatch()


# Generated at 2022-06-14 14:15:42.414386
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    # Nothing to test, since we never actually use this, and it doesn't get
    # called.
    print("NeverMatch constructor")
    print("Passed")
    print("")


# Generated at 2022-06-14 14:15:47.756268
# Unit test for method validate of class Not
def test_Not_validate():
    boolean_value = Not(Boolean())
    # Test correct input value
    assert boolean_value.validate(False) == False
    # Test incorrect input value
    with pytest.raises(ValidationError):
        boolean_value.validate("False")

# Below is the testing code

# Generated at 2022-06-14 14:15:49.749384
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    r = NeverMatch()
    assert r.errors == {"never": "This never validates."}

# Generated at 2022-06-14 14:15:58.384120
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    """
    TESTS :: Unit test for method IfThenElse of class IfThenElse
    """
    class IfThenElseTest(Field):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.if_clause = IfThenElse(Field(),Field("Hello"),Field("Bye"))
            self.then_clause = Field("World")

    if_clause = IfThenElse(Field("if"),Field("then"),Field("else"))
    result = if_clause.validate("if")
    assert result == "then"
    if_clause_test = IfThenElseTest()
    result = if_clause_test.validate("if")
    assert result == "if"

# Generated at 2022-06-14 14:15:59.464164
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    pass

# Generated at 2022-06-14 14:16:03.755666
# Unit test for method validate of class Not
def test_Not_validate():
    not_field = Not(String())
    not_field.validate("")
    with raises(ValidationError) as error:
        not_field.validate("A")
    assert error.value.field == "__root__"

# Generated at 2022-06-14 14:16:05.887105
# Unit test for constructor of class AllOf
def test_AllOf():
    """ Assert the constructor accepts two arguments and returns a Field object. """
    assert type(AllOf(Field(),Field())) == AllOf



# Generated at 2022-06-14 14:16:10.431753
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    f = NeverMatch()
    assert f.errors["never"] == "This never validates."


# Generated at 2022-06-14 14:16:12.996681
# Unit test for constructor of class Not
def test_Not():
    assert Not(Field()) == Not(Field())
    assert Not(Field()) != Not(Any())
    assert Not(Field()) != Not(Not(Field()))

# Generated at 2022-06-14 14:16:20.438225
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    if_clause = Integer()
    then_clause = Float()
    else_clause = String()
    m = IfThenElse(if_clause=if_clause, then_clause=then_clause, else_clause=else_clause)

    # test the default values of then_clause and else_clause
    m = IfThenElse(if_clause=if_clause)

    # test the default values of else_clause
    m = IfThenElse(if_clause=if_clause, then_clause=then_clause)



# Generated at 2022-06-14 14:16:25.103625
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    #Arrange
    values=['a','b','c']
    field = IfThenElse('a','c')
    #Act
    contact = (field.validate(values))
    #Assert
    assert contact == 'c'

# Generated at 2022-06-14 14:16:26.362876
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    field = NeverMatch()
    assert field

# Generated at 2022-06-14 14:16:27.804737
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    try:
        IfThenElse(1, 2, 3)
    except AssertionError as e:
        assert type(e) == AssertionError


# Generated at 2022-06-14 14:16:29.960284
# Unit test for constructor of class OneOf
def test_OneOf():
    with pytest.raises(AssertionError):
        o = OneOf([
            String(),
        ], allow_null=True)



# Generated at 2022-06-14 14:16:33.689078
# Unit test for constructor of class Not
def test_Not():
    assert(Not(None).negated == None)
    assert(Not(negated = None).negated == None)
    assert(Not(negated = None, errors=None).negated == None)
    #assert(Not(negated = None, errors={"errors": "nice try"}).negated == None)


# Generated at 2022-06-14 14:16:34.711745
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
  nm = NeverMatch()


# Generated at 2022-06-14 14:16:37.082230
# Unit test for constructor of class OneOf
def test_OneOf():
	__args__ = []
	print("Test_OneOf")
	test = OneOf(*__args__)
	assert test is not None

# Generated at 2022-06-14 14:16:43.389255
# Unit test for constructor of class Not
def test_Not():
    assert type(Not({})) == Not

# Generated at 2022-06-14 14:16:45.281395
# Unit test for constructor of class Not
def test_Not():
    # Given
    a = Not(None)
    # Then
    assert a.negated == None


# Generated at 2022-06-14 14:16:50.076225
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    # Create an instance of class IfThenElse
    if_then_else = IfThenElse(if_clause=String(max_length=5), then_clause=String(max_length=4), else_clause=String(max_length=3))
    assert if_then_else.validate(value="hello") == "hell"


# Generated at 2022-06-14 14:16:54.826238
# Unit test for method validate of class Not
def test_Not_validate():
    assert Not(negated = int).validate(2) == 2
    assert Not(negated = str).validate(2) == 2
    raises(FieldValidationError)(Not(negated = int).validate)(2.0)
    raises(FieldValidationError)(Not(negated = str).validate)('2')
    assert Not(negated = int).validate(None) == None


# Generated at 2022-06-14 14:16:58.891594
# Unit test for method validate of class Not
def test_Not_validate():
    # Setup
    not_ = Not(Any())
    value = ""
    strict = False

    # Exercise
    not_result = not_.validate(value, strict)

    # Verify
    assert not_result is value



# Generated at 2022-06-14 14:17:03.742643
# Unit test for method validate of class Not
def test_Not_validate():
    a = Not(String())
    assert a.validate('abc') is not None, 'Value must be not null'
    assert a.validate(0) is not None, 'Value must be not null'
    assert a.validate(None) is not None, 'Value must be not null'


# Generated at 2022-06-14 14:17:06.205687
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    res = IfThenElse(if_clause=Any(), then_clause=Any(), else_clause=Any())
    assert res is not None

# Generated at 2022-06-14 14:17:10.053016
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    field = IfThenElse(if_clause=Any(), then_clause=Any())

    assert field.validate(0) == 0
    assert field.validate(True) == True
    assert field.validate(None) == None

# Generated at 2022-06-14 14:17:12.408357
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    n = NeverMatch()
    assert n.errors == {"never": "This never validates."}
    return None


# Generated at 2022-06-14 14:17:15.714990
# Unit test for constructor of class OneOf
def test_OneOf():
    schema1 = OneOf([Integer(max_length=2)])
    assert schema1.errors == {'no_match': 'Did not match any valid type.', 'multiple_matches': 'Matched more than one type.'}


# Generated at 2022-06-14 14:17:22.612829
# Unit test for constructor of class OneOf
def test_OneOf():
    OptInt = OneOf([Int, None])
    OptInt([5])
    OptInt([None])


# Generated at 2022-06-14 14:17:24.671164
# Unit test for constructor of class Not
def test_Not():
    field = Not(negated=Any())
    assert field.negated is not None


# Generated at 2022-06-14 14:17:30.714116
# Unit test for constructor of class OneOf
def test_OneOf():
    one_of = OneOf()
    assert one_of.errors == {"no_match": "Did not match any valid type.", "multiple_matches": "Matched more than one type."}


if __name__ == "__main__":
    one_of = OneOf()
    assert one_of.errors == {"no_match": "Did not match any valid type.", "multiple_matches": "Matched more than one type."}

# Generated at 2022-06-14 14:17:33.129365
# Unit test for method validate of class Not
def test_Not_validate():
    a = Not(Child())
    a.validate({"name": "test", "age": 12})


# Generated at 2022-06-14 14:17:44.095382
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    from typesystem import Integer
    from typesystem import Schema
    from typesystem.exceptions import ValidationError
    
    s = Schema(
        type="object",
        properties={
            "x": IfThenElse(
                if_clause=Integer(minimum=10),
                then_clause=Integer(minimum=100),
                else_clause=Integer(minimum=0)
            )
        }
    )
    assert s.validate({"x": 10})
    assert s.validate({"x": 111})
    assert s.validate({"x": 1})
    assert s.validate({"x": -10})
    assert not s.validate({"x": 9})
    assert not s.validate({"x": 0})
    assert not s.validate({"x": -1})

# Generated at 2022-06-14 14:17:54.410298
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    """
    test the method validate of class IfThenElse
    """
    # Define a IfThenElse field
    if_value = Field()
    if_value.label = "if_value"
    then_value = Field()
    then_value.label = "then_value"
    else_value = Field()
    else_value.label = "else_value"
    if_then_else = IfThenElse(if_clause = if_value, then_clause = then_value, else_clause = else_value)
    if_then_else.label = "if_then_else"

    # Case with valid value for the if clause and for then clause
    input_value = 5
    expected_output_value = 5

# Generated at 2022-06-14 14:17:56.586376
# Unit test for constructor of class OneOf
def test_OneOf():
    a = typing.List[Field]
    # assert True # TODO: implement your test here
    assert True # TODO: implement your test here


# Generated at 2022-06-14 14:18:07.143663
# Unit test for constructor of class Not
def test_Not():
    name = Not("name", min_length=2, max_length=100)
    assert name.name == "name"
    assert name.min_length == 2
    assert name.max_length == 100
    assert name.description is None
    assert name.allow_null == False
    assert name.null_message == "This field may not be null."
    assert name.negated == "name"
    assert name.negated.min_length == 2
    assert name.negated.max_length == 100
    assert name.negated.description is None
    assert name.negated.allow_null == False
    assert name.negated.null_message == "This field may not be null."
    assert name.errors == {'negated': 'Must not match.'}

# Generated at 2022-06-14 14:18:10.399726
# Unit test for constructor of class Not
def test_Not():
    class Dummy:
        pass
    dummy = Dummy()
    dummy.errors = {"negated": "Must not match."}
    not_ = Not(dummy)
    assert not_.negated == dummy
    assert not_.errors == {"negated": "Must not match."}


# Generated at 2022-06-14 14:18:12.937591
# Unit test for method validate of class Not

# Generated at 2022-06-14 14:18:28.667168
# Unit test for method validate of class Not
def test_Not_validate():
    method = Method.objects.get(id=59)
    assert method.name == "Not.validate"
    parameters = [
        Parameter.objects.get(id=60),
        Parameter.objects.get(id=61),
    ]
    assert method.parameters.count() == len(parameters)
    for i, parameter in enumerate(parameters):
        assert parameter == method.parameters.all()[i]

    assert method.enclosing_type == Type.objects.get(id=58)
    assert method.enclosing_is_class is True
    assert not method.enclosing_is_function
    assert method.enclosing_is_method
    assert method.enclosing_is_property
    assert not method.enclosing_is_staticmethod
    assert not method.enclosing

# Generated at 2022-06-14 14:18:31.976923
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    foo = Any()
    bar = Any()
    if_then_else = IfThenElse(foo, bar)
    assert foo == if_then_else.if_clause
    assert bar == if_then_else.then_clause
    assert type(if_then_else.else_clause) == Any

# Generated at 2022-06-14 14:18:33.151510
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    test = NeverMatch()
    assert test

# Generated at 2022-06-14 14:18:37.433493
# Unit test for method validate of class Not
def test_Not_validate():
    not_field = Not(negated=String())
    assert not_field.validate('212321') == '212321'
    # assert not_field.validate(2) == 2
    return

test_Not_validate()

# Generated at 2022-06-14 14:18:41.194172
# Unit test for method validate of class Not
def test_Not_validate():
    
    not_validate_test_1 = Not(negated=None)
    #validate_or_error_test_1
    #not_validate_test_1.validate(None)

    #not_validate_test_1.validate_or_error(None)

# Generated at 2022-06-14 14:18:42.189170
# Unit test for constructor of class OneOf
def test_OneOf():
    
    assert OneOf


# Generated at 2022-06-14 14:18:45.064952
# Unit test for constructor of class AllOf
def test_AllOf():
    AllOf([Any()], name="name1")
    AllOf([Any(), Any()], name="name2")


# Generated at 2022-06-14 14:18:48.589388
# Unit test for method validate of class Not
def test_Not_validate():
    f = Not({})
    try:
        f.validate(None)
    except Exception as e:
        assert str(e) == "Must not match."


# Generated at 2022-06-14 14:18:55.140912
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    f1 = IfThenElse(Any())
    value = 3
    f1.validate(value)


    f2 = IfThenElse(None, Integer())
    value = 3
    f2.validate(value)


    f3 = IfThenElse(None, None, Integer())
    value = 3
    f3.validate(value)


    f4 = IfThenElse(None, Integer(), Integer())
    value = 3
    f4.validate(value)

# Generated at 2022-06-14 14:18:56.781219
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    # To check that the constructor runs without error
    NeverMatch()
    return True


# Generated at 2022-06-14 14:19:09.473116
# Unit test for method validate of class Not
def test_Not_validate():
    field = Not(Any())
    with pytest.raises(ValidationError):
        field.validate(1)
    field.validate(None)



# Generated at 2022-06-14 14:19:20.466204
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    import typesystem
    class Color(typesystem.Enum):
        choices = ["red", "green", "blue"]
    class Schema(typesystem.Schema):
        color = Color()
        color_is_red = typesystem.fields.IfThenElse(
            if_clause=typesystem.fields.Equals("blue"),
            then_clause=Color())
        color_is_blue = typesystem.fields.IfThenElse(
            if_clause=typesystem.fields.Equals("blue"),
            then_clause=typesystem.fields.Boolean(),
            else_clause=typesystem.fields.String())
    # test case "color_is_red"
    schema = Schema({
        "color": "red",
        "color_is_red": "red"
    })

# Generated at 2022-06-14 14:19:22.223854
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    nm = NeverMatch()
    assert nm.attributes == {"format": "NeverMatch", "type": "null"}



# Generated at 2022-06-14 14:19:28.419191
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    from typesystem.fields import String
    from typesystem.fields import Integer 
    from typesystem.fields import Number
    from typesystem.fields import Boolean

    if_ = String()

    then_ = String()

    else_ = String()

    s = IfThenElse(if_, then_, else_)

    s.validate(23)

    # assert isinstance(s.validate(23), str)

# Generated at 2022-06-14 14:19:35.895792
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    from typesystem.fields import Integer, String
    field = IfThenElse(if_clause=Integer(), then_clause=String())
    ret = field.validate(123)
    assert isinstance(ret, str)
    ret = field.validate("abc")
    assert isinstance(ret, str)
    ret = field.validate(123, True)
    assert isinstance(ret, str)
    ret = field.validate("abc", True)
    assert isinstance(ret, str)
    ret = field.validate(123, False)
    assert isinstance(ret, str)
    ret = field.validate("abc", False)
    assert isinstance(ret, str)


# Generated at 2022-06-14 14:19:37.480739
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    field = NeverMatch()
    assert field.name == None


# Generated at 2022-06-14 14:19:38.799787
# Unit test for constructor of class OneOf
def test_OneOf():
    x = OneOf([int])
    assert x



# Generated at 2022-06-14 14:19:41.950316
# Unit test for method validate of class Not
def test_Not_validate():
    field = Not(Field())
    try:
        value = field.validate("")
    except:
        value = None
    assert value is None


# Generated at 2022-06-14 14:19:42.954673
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    assert NeverMatch()


# Generated at 2022-06-14 14:19:44.214102
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    field = NeverMatch()
    assert field.allow_null == False

# Generated at 2022-06-14 14:20:18.966606
# Unit test for method validate of class Not
def test_Not_validate():
    from typesystem.fields import String

    a = Not(String())
    # Validating with a String value
    assert a.validate("abc") == "abc"
    # Validating with an int value
    try:
        a.validate(123)
    except Exception as e:
        assert e.code == "negated"

# Generated at 2022-06-14 14:20:23.765489
# Unit test for method validate of class Not
def test_Not_validate():
    not1 = Not(negated=NeverMatch())
    try:
        not1.validate("test")
    except Exception as e:
        assert e.errors == {"negated": ["Must not match."]}
    assert not1.validate("test", strict=True) == "test"



# Generated at 2022-06-14 14:20:29.274417
# Unit test for method validate of class Not
def test_Not_validate():
    from typesystem import String

    from .schemas import Person

    class NotPerson(Not):
        def __init__(self, **kwargs):
            super().__init__(Person(**kwargs))

    # case 1:
    person = Person()
    valid_value = {"name": "James"}
    assert person.validate(valid_value) == valid_value

    not_person = NotPerson()
    assert not_person.validate(valid_value) == valid_value


# Generated at 2022-06-14 14:20:33.176442
# Unit test for constructor of class OneOf
def test_OneOf():
    field1 = Field()
    field2 = Field()
    field3 = Field()
    one_of = OneOf([field1, field2, field3])
    assert one_of.one_of == [field1, field2, field3]

# Generated at 2022-06-14 14:20:36.286590
# Unit test for method validate of class Not
def test_Not_validate():
    field = Not(Field())
    assert field.validate(NotImplemented) == (NotImplemented)


# Generated at 2022-06-14 14:20:42.982011
# Unit test for method validate of class Not
def test_Not_validate():
    not_field = Not(Any())
    class_name = not_field.__class__.__name__
    function_name = sys._getframe().f_code.co_name
    try:
        not_field.validate(None)
        print('[{} - {}] Should have raised an error!'.format(class_name, function_name))
        assert False
    except FieldValidationError as e:
        print('[{} - {}] Correctly raised an error!'.format(class_name, function_name))
        assert True


# Generated at 2022-06-14 14:20:45.191203
# Unit test for constructor of class Not
def test_Not():
    class n(Not):
        pass
    assert n.errors ==  {"negated": "Must not match."}


# Generated at 2022-06-14 14:20:51.931152
# Unit test for constructor of class OneOf
def test_OneOf():
    """
    Test for constructor of class OneOf
    """
    # GIVEN
    input_value = {
        "name": "testOneOf",
        "one_of": [Any()],
        "allow_null": True
    }

    # WHEN
    result = OneOf(**input_value)

    # THEN
    assert result.name == 'testOneOf'
    assert result.one_of == [Any()]
    assert result.allow_null == True


# Generated at 2022-06-14 14:20:56.040678
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    if_clause = Field(label="if", description="if_clause")
    then_clause = Field(label="then", description="then_clause")
    else_clause = Field(label="else", description="else_clause")
    name = IfThenElse(if_clause, then_clause, else_clause)
    assert name.validate(123) == 123


# Generated at 2022-06-14 14:20:58.616904
# Unit test for method validate of class Not
def test_Not_validate():
    field = Not(Any())
    assert field.validate('a') == 'a'
    try:
        field.validate(0)
        assert False
    except FieldValidationError:
        assert True

# Generated at 2022-06-14 14:21:22.860894
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    from typesystem.base import ValidationError
    from typesystem.fields import String
    field = IfThenElse(if_clause=String(), then_clause=String(), strict=True)
    field.validate("abc")
    try:
        field.validate(1)
    except ValidationError:
        pass
    else:
        assert False, "Should fail for int"
    field = IfThenElse(if_clause=String(), else_clause=String(), strict=True)
    field.validate(1)
    try:
        field.validate("abc")
    except ValidationError:
        pass
    else:
        assert False, "Should fail for str"

# Generated at 2022-06-14 14:21:26.202328
# Unit test for constructor of class Not
def test_Not():
    # Test field
    some_field = Field()
    # Test constructor for class Not
    some_field = Not(some_field)
    # Test empty constructor for class Not
    some_field = Not()


# Generated at 2022-06-14 14:21:27.943280
# Unit test for constructor of class Not
def test_Not():
    test = Not(Field(name="test", required=True))
    print(test.__dict__)



# Generated at 2022-06-14 14:21:28.760644
# Unit test for constructor of class AllOf
def test_AllOf():
    pass


# Generated at 2022-06-14 14:21:31.289583
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    assert value, "default value" == IfThenElse(
        IntegerField(minimum=2),
        StringField(max_length=2),
        StringField(min_length=2)
    ).validate(1)



# Generated at 2022-06-14 14:21:36.059937
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    instance = IfThenElse(if_clause=Any(), then_clause=Any(), else_clause=Any())
    assert instance.validate({'a': 'b'}) == {'a': 'b'}
    assert instance.validate({}) == {}
    assert instance.validate(1) == 1
    assert instance.validate('string') == 'string'

# Generated at 2022-06-14 14:21:45.652773
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    # Test that this method returns an error, if the value matches if_clause, but not then_clause
    field_1 = String()
    field_2 = Integer()
    field_3 = Float()
    field_4 = IfThenElse(field_1, field_3)
    value_1 = 123
    with pytest.raises(Exception) as exception_1:
        field_4.validate(value_1)
    assert exception_1.value.args[0] == 'Field "if_clause" on IfThenElse field is invalid.'

    # Test that this method returns an error, if the value matches if_clause and then_clause, but not else_clause
    field_5 = IfThenElse(field_3, field_3, field_2)
    value_2 = 3.14

# Generated at 2022-06-14 14:21:52.735292
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    if_clause = IfThenElse(Any(), Any(), Any())
    then_clause = IfThenElse(Any(), Any(), Any())
    else_clause = IfThenElse(Any(), Any(), Any())
    a = IfThenElse(if_clause, then_clause, else_clause)
    assert a.validate('a', strict = False) == 'a'
    assert a.validate(1, strict = False) == 1
    assert a.validate(True, strict = False) == True
    assert a.validate(1.0, strict = False) == 1.0

# Generated at 2022-06-14 14:21:53.430882
# Unit test for constructor of class AllOf
def test_AllOf():
    assert True

# Generated at 2022-06-14 14:21:55.514749
# Unit test for constructor of class Not
def test_Not():
    try:
        Not(None)
    except AssertionError:
        assert True
    except:
        assert False
    else:
        assert False

# Generated at 2022-06-14 14:22:30.290420
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
	from typesystem.fields import Integer
	field = IfThenElse(Integer(minimum=0), Integer(maximum=1), Integer(minimum=10), name='test')
	field.validate(9) # then clause is validated
	field.validate(0) # else clause is validated

# Generated at 2022-06-14 14:22:34.218019
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    test_schema = IfThenElse(
        if_clause=Integer(),
        then_clause=Integer(),
        else_clause=String(),
    )
    assert test_schema.validate("5") == "5"
    assert test_schema.validate(5) == 5



# Generated at 2022-06-14 14:22:42.442801
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    assert IfThenElse(field_1, field_2).validate(value) == value
    assert IfThenElse(field_1, field_2, field_3).validate(value) == value
    assert IfThenElse(field_1, field_2, field_3, field_4).validate(value) == value
    assert IfThenElse(field_1, field_2, field_3, field_4, field_5).validate(value) == value
    assert IfThenElse(field_1, field_2, field_3, field_4, field_5, field_6).validate(value) == value
    assert IfThenElse(field_1, field_2, field_3, field_4, field_5, field_6, field_7).validate(value) == value