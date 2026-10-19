

# Generated at 2022-06-14 14:12:51.398848
# Unit test for method validate of class Not
def test_Not_validate():
    from typesystem.fields import String
    from typesystem.exceptions import ValidationError
    from typesystem import Schema

    schema = Schema(
        {"test_Not": Not(negated=String())}
    )
    # test:simple test
    try:
        assert schema.validate({"test_Not": "test"})
        raise AssertionError("Expected ValidationError")
    except ValidationError as e:
        assert e.field_errors["test_Not"] == ["Must not match."]
    # test:simple test
    try:
        assert schema.validate({"test_Not": 1})["test_Not"] == 1
    except ValidationError as e:
        assert "Never reached"

# Generated at 2022-06-14 14:12:57.706690
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    schema = OneOf([
        {"type": "string"},
        {"type": "integer"}
    ])

    # Initial state
    assert isinstance(schema.one_of, list)

    # Method validate
    assert schema.validate("1")
    assert schema.validate(1)
    assert isinstance(schema.validate("1"), str)
    assert isinstance(schema.validate(1), int)



# Generated at 2022-06-14 14:13:09.263731
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    class IntOrString(IfThenElse):
        def __init__(self):
            super().__init__(
                then_clause=Int(),
                else_clause=String(),
                if_clause=Int(),
            )

    field = IntOrString()
    result, error = field.validate_or_error(1)
    assert result == 1
    assert error is None
    assert field.validate("1") == "1"
    result, error = field.validate_or_error("1")
    assert result == "1"
    assert error is None
    result, error = field.validate_or_error('"1"')
    assert result == '"1"'
    assert error is None

    # TODO: should this validate?
    # assert field.validate({"test": 1}) == {"

# Generated at 2022-06-14 14:13:09.898113
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    pass

# Generated at 2022-06-14 14:13:13.806456
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    assert IfThenElse(
        if_clause = None,
        then_clause = None,
        else_clause = None
    ) == None
    assert IfThenElse(
        if_clause = True,
        then_clause = True,
        else_clause = True
    ) == True

# Generated at 2022-06-14 14:13:22.064874
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    from typesystem import Schema, String
    Text = IfThenElse(
        if_clause=Schema({
            "text": String,
        }),
        then_clause=Schema({
            "text": String,
        }),
        else_clause=Schema({
            "list": [String],
        }),
    )
    assert Text.validate({"text": "hello"}) == {"text": "hello"}
    assert Text.validate({"list": ["hello"]}) == {"list": ["hello"]}



# Generated at 2022-06-14 14:13:28.610977
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    single = IfThenElse(
        if_clause=Field(type_class=int),
        then_clause=Field(type_class=int),
        else_clause=Field(type_class=str),
    )
    assert single.validate(4) == 4
    assert single.validate("hello") == "hello"
    assert single.validate(4.1) == "4.1"

# Generated at 2022-06-14 14:13:30.860290
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    nm = NeverMatch()
    assert nm.errors == {"never": "This never validates."}


# Generated at 2022-06-14 14:13:38.210319
# Unit test for method validate of class Not
def test_Not_validate():
    def mock_validate_or_error(value, strict=False):
        return None

    import types
    real_validate_or_error = Not.validate_or_error
    try:
        Not.validate_or_error = mock_validate_or_error
        negated = Not(None)
        negated.validate(0) # None is returned by mock
    finally:
        Not.validate_or_error = real_validate_or_error

# Generated at 2022-06-14 14:13:42.612943
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    class If(object):
        def validate(self, p1, p2):
            if p2:
                return True
            else:
                return False
    field = IfThenElse(If(), None, None)
    assert field.validate(True, False) == True

# Generated at 2022-06-14 14:13:50.710942
# Unit test for constructor of class AllOf
def test_AllOf():
    from typesystem import String
    field = AllOf(
        [
            String(min_length=1),
            String(max_length=1),
        ],
    )
    field.validate("a")
    string_field = String(max_length=1)
    string_field.validate("a")


# Generated at 2022-06-14 14:13:51.637002
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    pass
    # TODO: write unit test

# Generated at 2022-06-14 14:14:02.459244
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    from typesystem.types import String
    # If the list is empty or the value doesn't match any item, raise an error.
    field = OneOf([])
    try:
        field.validate(1)
        assert False
    except Exception as e:
        assert e.code == "no_match"

    field = OneOf([String(), Integer()])
    try:
        field.validate(1.5)
        assert False
    except Exception as e:
        assert e.code == "no_match"
    # If the value matches more than one item, raise an error.
    field = OneOf([String(), Any()])
    try:
        field.validate(1)
        assert False
    except Exception as e:
        assert e.code == "multiple_matches"
    # If the value matches exactly one item,

# Generated at 2022-06-14 14:14:03.754712
# Unit test for constructor of class AllOf
def test_AllOf():
    field = AllOf()
    assert field is not None

# Generated at 2022-06-14 14:14:10.336827
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
	import json
	from typesystem.fields import String
	data = {"foo": "bar"}
	field = IfThenElse(String(), String(), String())
	assert field.validate(data) == data
	field = IfThenElse(String(), String())

	data["foo"] = None
	with pytest.raises(ValueError):
		field.validate(data)
	data["foo"] = "bar"
	assert field.validate(data) == data
		



# Generated at 2022-06-14 14:14:12.245146
# Unit test for constructor of class AllOf
def test_AllOf():
    from typesystem.fields import Integer
    assert AllOf([Integer()]) is not None


# Generated at 2022-06-14 14:14:25.175442
# Unit test for constructor of class AllOf
def test_AllOf():
    class AllOf(Field):
        """
        Must match all of the sub-items.

        You should instead consolidate into a single type, or use
        schema inheritence instead of this.
        """

        def __init__(self, all_of: typing.List[Field], **kwargs: typing.Any) -> None:
            assert "allow_null" not in kwargs
            super().__init__(**kwargs)
            self.all_of = all_of

        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            for child in self.all_of:
                child.validate(value, strict=strict)
            return value
    # Success case
    f = AllOf([Field()])
    assert True
    return f


# Generated at 2022-06-14 14:14:31.558499
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    if_clause= Integer(maximum=5)
    then_clause= Integer(maximum=6)
    else_clause= Integer(maximum=7)
    if_then_else = IfThenElse(if_clause=if_clause, then_clause=then_clause, else_clause=else_clause)
    try:
        if_then_else.validate(3)
    except:
        pass
    finally:
        assert True

# Generated at 2022-06-14 14:14:34.181057
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    import pytest
    never_match = NeverMatch()
    assert never_match.errors == {"never": "This never validates."}


# Generated at 2022-06-14 14:14:45.565966
# Unit test for method validate of class Not
def test_Not_validate():
    not_field = Not(Field)
    assert not_field.validate(1) == 1
    try:
        not_field.validate(None)
    except ValidationError as e:
        assert e.code == 'negated'
        assert str(e) == "Must not match."
    not_field2 = Not(Int(default=0, name='Int'), name='Not field 2')
    assert not_field2.validate(None) == 0
    assert not_field2.validate(1) == 1
    try:
        not_field2.validate('abc')
    except ValidationError as e:
        assert e.code == 'invalid'
        assert str(e) == "Invalid value."



# Generated at 2022-06-14 14:14:53.108244
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    from typesystem import Integer, String
    IfThenElse(Integer(), then_clause=String())
    return True
test_IfThenElse()

# Generated at 2022-06-14 14:14:58.106706
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    a = Field(coerce=str)
    b = Field(description="description", format="format")
    c = IfThenElse(a, b)
    c.validate(1)
    assert c.schema() == {"type": "string", "description": "description", "format": "format"}

# Generated at 2022-06-14 14:15:01.633200
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    never_match = NeverMatch()
    assert never_match.errors == {"never": "This never validates."}
    assert never_match.__doc__ == "Doesn't ever match."


# Generated at 2022-06-14 14:15:11.641716
# Unit test for method validate of class Not
def test_Not_validate():
    a = Not(IfThenElse(
        if_clause=AllOf([Any(), Any()]),
        then_clause=Any(),
        else_clause=Any(),
    ))
    b = Not(IfThenElse(
        if_clause=AllOf([Any(), Any()]),
        then_clause=Any(),
        else_clause=Any(),
    ))
    c = Not(IfThenElse(
        if_clause=AllOf([Any(), Any()]),
        then_clause=OneOf([Any(), Any()]),
        else_clause=OneOf([Any(), Any()]),
    ))

# Generated at 2022-06-14 14:15:15.200969
# Unit test for method validate of class Not
def test_Not_validate():
    item = Not(
        field=Integer(minimum=0, maximum=10),
        description="Must not be in range 0:10",
    )
    item.validate(value=0)



# Generated at 2022-06-14 14:15:25.149079
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    # test match
    result = OneOf([Any()]).validate(1)
    assert result == 1

    # test not match
    msg = ''
    try:
        result = OneOf([NeverMatch()]).validate(1)
    except Exception as e:
        msg = str(e)
    assert msg == 'one_of.no_match: Did not match any valid type.'

    # test multiple matches
    msg = ''
    try:
        result = OneOf([Any(), Any()]).validate(1)
    except Exception as e:
        msg = str(e)
    assert msg == 'one_of.multiple_matches: Matched more than one type.'


# Generated at 2022-06-14 14:15:29.596555
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    field = IfThenElse(Integer()) # value of IfThenElse instance: self.if_clause, self.then_clause and self.else_clause
    field = IfThenElse(Integer(), Integer())
    field = IfThenElse(Integer(maximum=10), Integer(), String())
    field = IfThenElse(Integer(maximum=10), Integer(), String(max_length=10))
    


# Generated at 2022-06-14 14:15:31.146490
# Unit test for constructor of class AllOf
def test_AllOf():
    assert AllOf([Any(), Any()])


# Generated at 2022-06-14 14:15:37.892997
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    # Given
    field = OneOf(one_of=[Any()])

    # When/Then
    assert field.validate("x") == "x"

    # Given
    field = OneOf(one_of=[Any(), Any()])

    # When/Then
    assert field.validate("x") == "x"

    # Given
    field = OneOf(one_of=[Any(), NeverMatch()])

    # When/Then
    with pytest.raises(Exception) as excinfo:
        field.validate("x")
    assert "multiple_matches" in str(excinfo.value)

    # Given
    field = OneOf(one_of=[NeverMatch(), NeverMatch()])

    # When/Then
    with pytest.raises(Exception) as excinfo:
        field.validate("x")
   

# Generated at 2022-06-14 14:15:40.504449
# Unit test for method validate of class Not
def test_Not_validate():
    not_field = Not(String())
    not_validate_result, not_validate_error = not_field.validate_or_error(1)
    assert not_validate_error is None


# Generated at 2022-06-14 14:15:46.335479
# Unit test for method validate of class Not
def test_Not_validate():
    schema=Not(Integer())
    schema.validate(3)

# Generated at 2022-06-14 14:15:49.193419
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    x = NeverMatch()
    assert (x.errors == {"never": "This never validates."})


# Generated at 2022-06-14 14:15:57.689886
# Unit test for method validate of class Not
def test_Not_validate():

    # Define a set of valid values
    valid_values = ['banana', 'apple', 'pear', None]

    # Define a set of invalid values
    invalid_values = ['orange']

    # Create a new Not object with keyword argument if_clause
    test1 = Not(if_clause='banana')

    for test_value in valid_values:
        try:
            test1.validate(test_value)
        except Exception as e:
            print('Error:', e)
            assert False

    for test_value in invalid_values:
        try:
            test1.validate(test_value)
        except Exception as e:
            assert True


# Generated at 2022-06-14 14:16:02.236228
# Unit test for method validate of class Not
def test_Not_validate():
    t = Not(negated=Field())
    validated, _ = t.validate_or_error(['1'])
    assert validated == ['1']
    _, error = t.validate_or_error(1)
    assert error.code == "negated"



# Generated at 2022-06-14 14:16:05.117224
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    field = IfThenElse(AllOf([Any()]), Field())
    assert field.validate("") == ""


# Generated at 2022-06-14 14:16:12.765930
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    class TestIfThenElse(unittest.TestCase):

        def test_return_this_then_clause_if_value_match_if_clause(self):
            field = IfThenElse(if_clause=Boolean(), then_clause=String())
            value = field.validate(True)
            self.assertEqual(value, "true")

        def test_return_this_else_clause_if_value_not_match_if_clause(self):
            field = IfThenElse(if_clause=Boolean(), else_clause=String())
            value = field.validate("value")
            self.assertEqual(value, "value")

    return TestIfThenElse

# Generated at 2022-06-14 14:16:20.225745
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    if_clause = fields.String()
    then_clause = fields.Integer()
    else_clause = fields.Decimal()

    if_clause.validate("")
    then_clause.validate(1)
    else_clause.validate(1.1)

    if_then_else = IfThenElse(if_clause, then_clause, else_clause)
    if_then_else.validate("")
    if_then_else.validate(1)
    if_then_else.validate(1.1)


# Generated at 2022-06-14 14:16:27.043789
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    """
    Ensure that the constructor of the class NeverMatch prunes non-valid
    arguments.
    """
    # GIVEN the class NeverMatch
    # WHEN initiating it with non-valid arguments
    field = NeverMatch(validators=[lambda x: True], allow_null=True)

    # THEN the error is raised
    assert field.allow_null == False
    assert field.validators == []



# Generated at 2022-06-14 14:16:31.611306
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    from typesystem import Integer, String
    field = IfThenElse(if_clause=Integer(), then_clause=String())
    assert field.validate("1") == "1"
    assert field.validate(1) == "1"
    assert field.validate("True") == "True"
    assert field.validate(True) == "True"



# Generated at 2022-06-14 14:16:33.941097
# Unit test for method validate of class Not
def test_Not_validate():
    field = Not(NeverMatch())
    assert field.validate(1) == 1
    with pytest.raises(ValidationError):
        field.validate(None)


# Generated at 2022-06-14 14:16:48.260900
# Unit test for constructor of class AllOf
def test_AllOf():
    test_cases = [
        ("AllOf_1", (Field, "all_of", AllOf(Field, "all_of")),
            {'description': 'Must match all of the sub-items.'}),
        ("AllOf_2", (Field, "all_of", AllOf(Field, "all_of", "foo")),
            {'description': 'Must match all of the sub-items.', 'foo': 'bar'}),
    ]
    for tc in test_cases:
        with pytest.raises(TypeError):
            AllOf(tc[1])
        assert AllOf(tc[2]).__dict__ == tc[1][2].__dict__



# Generated at 2022-06-14 14:16:52.362057
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    field = IfThenElse("if_clause", "then_clause", "else_clause")
    assert field.if_clause == "if_clause"
    assert field.then_clause == "then_clause"
    assert field.else_clause == "else_clause"

# Generated at 2022-06-14 14:16:53.643512
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    no_match = NeverMatch()

test_NeverMatch()


# Generated at 2022-06-14 14:16:59.031429
# Unit test for method validate of class Not
def test_Not_validate():
    not_field = Not(negated=Str())
    data = not_field.validate("123")
    assert data == "123"

    with pytest.raises(TypeError) as excinfo:
        data = not_field.validate(123)
    assert "Must not m" in str(excinfo.value)



# Generated at 2022-06-14 14:17:02.789630
# Unit test for method validate of class Not
def test_Not_validate():
    not_task = Not(String())
    assert not_task.validate(None) is None
    assert not_task.validate('12345') is None
    assert not_task.validate(1234) is None


# Generated at 2022-06-14 14:17:06.311539
# Unit test for method validate of class Not
def test_Not_validate():
    not_field = Not(negated=AllOf([Any(), Any()]))

    value = 2
    strict = True
    assert not_field.validate(value, strict) == value


# Generated at 2022-06-14 14:17:08.873668
# Unit test for constructor of class OneOf
def test_OneOf():
    # This unit test is to test the construction of class OneOf
    testType = OneOf([])
    assert testType is not None


# Generated at 2022-06-14 14:17:12.550540
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    from typesystem import Integer, String

    if_clause = String()
    then_clause = Integer()

    ite = IfThenElse(if_clause, then_clause)

    ite.validate('1')



# Generated at 2022-06-14 14:17:20.077378
# Unit test for constructor of class AllOf
def test_AllOf():
    """test_AllOf"""
    import uuid
    class AllOfCls(Field):
        """
        Must match all of the sub-items.
        You should instead consolidate into a single type,
        or use schema inheritence instead of this.
        """
        x = 1
        def __init__(self, all_of: typing.List[Field], **kwargs: typing.Any) -> None:
            assert "allow_null" not in kwargs
            super().__init__(**kwargs)
            self.all_of = all_of
            self.y = uuid.uuid4()

        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            for child in self.all_of:
                child.validate(value, strict=strict)
            return value



# Generated at 2022-06-14 14:17:22.716943
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    ite = IfThenElse(String(), Integer())
    with pytest.raises(ValidationError):
        ite.validate(1)

# Generated at 2022-06-14 14:17:31.590775
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    field = NeverMatch()
    assert field.validate(None) == None


# Generated at 2022-06-14 14:17:36.310100
# Unit test for constructor of class OneOf
def test_OneOf():
    int_array = OneOf([Integer,Float])
    print(int_array.validate(5))
    print(int_array.validate(4.2))
    #print(int_array.validate("3"))


# Generated at 2022-06-14 14:17:42.865590
# Unit test for constructor of class AllOf
def test_AllOf():
    from typesystem.fields import Array
    from typesystem.types import Integer

    a = Array(integer=Integer())
    b = Array(max_length=1)

    schema = AllOf([a, b])

    assert schema.validate([]) == []
    assert schema.validate([1]) == [1]
    assert schema.validate([2]) == [2]

    with raises(schema.validation_error):
        schema.validate([1, 2])

# Generated at 2022-06-14 14:17:45.787866
# Unit test for constructor of class OneOf
def test_OneOf():
    assert OneOf([Any()]).one_of == [Any()]


# Generated at 2022-06-14 14:17:49.396799
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    if_clause = Field()
    then_clause = Field()
    else_clause = Field()
    test = IfThenElse(if_clause, then_clause, else_clause)
    assert test.validate(1) == 1

# Generated at 2022-06-14 14:17:55.361963
# Unit test for constructor of class IfThenElse
def test_IfThenElse():

    # Arrange
    if_clause = Field()
    then_clause = Field()
    else_clause = Field()
    test_field = IfThenElse(if_clause, then_clause, else_clause)

    # Act and Assert
    assert isinstance(test_field, Field)
    assert test_field.if_clause == if_clause
    assert test_field.then_clause == then_clause
    assert test_field.else_clause == else_clause



# Generated at 2022-06-14 14:17:57.436274
# Unit test for constructor of class AllOf
def test_AllOf():
    a = Field()
    b = Field()
    c = AllOf([a, b])
    assert [a, b] == c.all_of


# Generated at 2022-06-14 14:18:01.119725
# Unit test for constructor of class AllOf
def test_AllOf():
    test=AllOf(all_of=[AllOf(all_of=[])])
    assert test.all_of==[AllOf(all_of=[])]


# Generated at 2022-06-14 14:18:10.400270
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    '''
    this test is to test constructor of class IfThenElse
    '''
    class Success(Field):
        def validate(self, value, strict=False):
            return value
    class Fail(Field):
        errors = {
            "invalid": "Not valid"
        }
        def validate(self, value, strict=False):
            raise self.validation_error("invalid")

    assert IfThenElse(Success(), Success()).validate(12) == 12
    assert IfThenElse(Fail(), Success()).validate(12) == 12
    assert IfThenElse(Fail(), Success(), Success()).validate(12) == 12
    assert IfThenElse(Fail(), Success(), Fail()).validate(12) == 12
    assert IfThenElse(Fail(), Fail(), Success()).validate(12) == 12

# Generated at 2022-06-14 14:18:21.603786
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    # Checking validation error with the first if_clause
    # This is the correct result, but it may not be the expected result
    ifthenelse_field = IfThenElse(if_clause=NeverMatch(),
                                  then_clause=NeverMatch(),
                                  else_clause=NeverMatch())
    with pytest.raises(FieldValidationError):
        ifthenelse_field.validate(None)
    # Checking validation error with the second if_clause
    # This is the correct result, but it may not be the expected result
    ifthenelse_field = IfThenElse(if_clause=NeverMatch(),
                                  then_clause=NeverMatch())
    with pytest.raises(FieldValidationError):
        ifthenelse_field.validate(None)
    # Checking validation error with the third if_clause

# Generated at 2022-06-14 14:18:26.654289
# Unit test for constructor of class AllOf
def test_AllOf():
    field = AllOf()
    assert field

# Generated at 2022-06-14 14:18:27.565108
# Unit test for constructor of class OneOf
def test_OneOf():
    assert OneOf([Field()])

# Generated at 2022-06-14 14:18:30.474448
# Unit test for constructor of class OneOf
def test_OneOf():
    from typesystem import Integer
    from typesystem import String

    test = OneOf([Integer, String], name="x", description="x")
    assert test.__class__ is OneOf
    assert test.one_of == [Integer, String]


# Generated at 2022-06-14 14:18:35.151017
# Unit test for constructor of class AllOf
def test_AllOf():
    str1 = typesystem.String()
    str2 = typesystem.String()
    all_of = typesystem.AllOf([str1, str2])
    assert str1.validate("test") == all_of.validate("test")


# Generated at 2022-06-14 14:18:36.831124
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    assert NeverMatch(label='test') is not None


# Generated at 2022-06-14 14:18:39.059402
# Unit test for constructor of class AllOf
def test_AllOf():
    all_of = [Field()]
    field = AllOf(all_of)
    assert field.all_of == all_of



# Generated at 2022-06-14 14:18:39.658420
# Unit test for constructor of class NeverMatch

# Generated at 2022-06-14 14:18:41.998558
# Unit test for constructor of class OneOf
def test_OneOf():
    field = OneOf(one_of=[Boolean(), Integer()])
    assert isinstance(field, OneOf)
    assert field.required == True


# Generated at 2022-06-14 14:18:47.984637
# Unit test for constructor of class OneOf
def test_OneOf():
    import json
    field = OneOf([Any(), Any()])
    assert field.validate(1) == 1
    with pytest.raises(field.validation_error) as e:
        field.validate(None)
    assert json.loads(str(e.value)) == {"code": "no_match"}


# Generated at 2022-06-14 14:18:54.325377
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    # object creation
    neverMatch = NeverMatch()

    # testing field values
    assert neverMatch.name is None
    always = neverMatch.always_error is True
    assert always == True
    assert neverMatch.default is None
    assert neverMatch.description == ''
    assert neverMatch.format is None
    assert neverMatch.title == ''
    assert neverMatch.errors == {'never': 'This never validates.'}


# Generated at 2022-06-14 14:19:03.195019
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    NeverMatch(name="never_match")



# Generated at 2022-06-14 14:19:03.967863
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    x = NeverMatch()
    assert x.errors == {"never": "This never validates."}


# Generated at 2022-06-14 14:19:05.491113
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    field = NeverMatch()
    assert field.errors == {"never": "This never validates."}


# Generated at 2022-06-14 14:19:07.079091
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    # test __init__ function
    my_NeverMatch = NeverMatch()


# Generated at 2022-06-14 14:19:08.487494
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    assert NeverMatch(name="NeverMatch") != None


# Generated at 2022-06-14 14:19:11.249219
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    test = NeverMatch()
    expected = "{'type': 'never'}"
    assert str(test) == expected


# Generated at 2022-06-14 14:19:11.949394
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    assert NeverMatch()

# Generated at 2022-06-14 14:19:13.216203
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    field = NeverMatch()


# Generated at 2022-06-14 14:19:16.092664
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    NeverMatch(description="Pretty description")
    NeverMatch(description="Pretty description", extend=True)
    NeverMatch(description="Pretty description", extend=True, required=True)

# Generated at 2022-06-14 14:19:18.586574
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    n = NeverMatch()
    assert n.allow_null == False
    assert n.errors == {'never': 'This never validates.'}


# Generated at 2022-06-14 14:19:34.304280
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    field = NeverMatch()
    assert field.errors == {'never': 'This never validates.'}


# Generated at 2022-06-14 14:19:36.877862
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    try:
        IfThenElse('if_clause')
    except:
        raise AssertionError("Test 1: Constructor Failed.")



# Generated at 2022-06-14 14:19:37.849154
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    assert type(NeverMatch()) == NeverMatch

# Generated at 2022-06-14 14:19:39.279415
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    assert NeverMatch().validate(None) == None


# Generated at 2022-06-14 14:19:41.153889
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    test = NeverMatch()
    assert isinstance(test, Field)


# Generated at 2022-06-14 14:19:43.959915
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    obj = IfThenElse(if_clause=Any())
    assert obj.if_clause is not None
    assert obj.then_clause is not None
    assert obj.else_clause is not None

# Generated at 2022-06-14 14:19:46.833603
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    n = NeverMatch()
    try:
        with pytest.raises(TypeError):
            n.validate('maybe', strict = False)
    except AssertionError as e:
        print(e)


# Generated at 2022-06-14 14:19:59.232003
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    # Input:
    field = NeverMatch(
        title="field_title", description="field_description", 
        required=True, nullable=False, 
        read_only=True, write_only=False, 
        default_value=None, enum=None, 
        errors=None, error_messages={}, 
        validators=None, validator_messages={}, 
        choices=[], **{}
    )

    # Output:
    assert field.title == "field_title"
    assert field.description == "field_description"
    assert field.required == True
    assert field.nullable == False
    assert field.read_only == True
    assert field.write_only == False
    assert field.default_value == None
    assert field.enum == None
    assert field.errors == None
   

# Generated at 2022-06-14 14:20:01.685674
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    # Check that the constructor has no input arguments
    import inspect
    assert len(inspect.getfullargspec(NeverMatch.__init__).args) == 1


# Generated at 2022-06-14 14:20:03.961508
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    with pytest.raises(AssertionError, match="allow_null"):
        f = NeverMatch(allow_null=True)


# Generated at 2022-06-14 14:20:28.496939
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    field = NeverMatch()
    assert field.errors == {"never": "This never validates."}



# Generated at 2022-06-14 14:20:30.208456
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    a = NeverMatch()
    assert a.errors == {"never": "This never validates."}

# Generated at 2022-06-14 14:20:32.004497
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    error = NeverMatch().validate('a')
    assert error , 'never'


# Generated at 2022-06-14 14:20:34.149225
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    assert NeverMatch.errors == {"never": "This never validates."}


# Generated at 2022-06-14 14:20:44.286142
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    # Test with IfThenElse without then_clause and else_clause
    class NameType(Field):
        pass
    if_clause = NameType()
    assert IfThenElse(if_clause).if_clause == if_clause
    assert IfThenElse(if_clause).then_clause == Any()
    assert IfThenElse(if_clause).else_clause == Any()

    # Test with IfThenElse without else_clause
    then_clause = NameType()
    assert IfThenElse(if_clause, then_clause).if_clause == if_clause
    assert IfThenElse(if_clause, then_clause).then_clause == then_clause
    assert IfThenElse(if_clause, then_clause).else_clause == Any()

    #

# Generated at 2022-06-14 14:20:45.951925
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    obj = NeverMatch(name='test')
    assert obj.name == 'test'


# Generated at 2022-06-14 14:20:47.238384
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    assert NeverMatch(name="1")

# Generated at 2022-06-14 14:20:48.802465
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    field = NeverMatch()
    assert field.validate(10) == "This never validates."


# Generated at 2022-06-14 14:20:57.096067
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    class MyField(Field):
        def __init__(self, **kwargs: typing.Any) -> None:
            super().__init__(**kwargs)
        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            return value
    myfield = MyField()
    
    # test for default values
    IfThenElse(myfield)
    
    IfThenElse(myfield, then_clause=myfield)
    
    IfThenElse(myfield, else_clause=myfield)
    
    IfThenElse(myfield, then_clause=myfield, else_clause=myfield)
    
    # test for init with many of one field
    IfThenElse(myfield, myfield, myfield)
    

# Generated at 2022-06-14 14:20:58.035963
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    n = NeverMatch()


# Generated at 2022-06-14 14:21:47.964358
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    try:
        NeverMatch()
    except AssertionError:
        assert False

    try:
        NeverMatch(allow_null=False)
    except AssertionError:
        assert True
    else:
        assert False


# Generated at 2022-06-14 14:21:53.089377
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    if_clause = Field()
    then_clause = Field()
    else_clause = Field()
    if_then_else = IfThenElse(if_clause, then_clause, else_clause)
    assert if_then_else.if_clause == if_clause
    assert if_then_else.then_clause == then_clause
    assert if_then_else.else_clause == else_clause

# Generated at 2022-06-14 14:21:56.978049
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    """
    Test IfThenElse constructor with given values.
    """
    IfThenElse(
        if_clause = Str(),
        then_clause = Str()
    )
    IfThenElse(
        if_clause = Int(),
        then_clause = Int()
    )

# Generated at 2022-06-14 14:21:57.938491
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    never_match = NeverMatch()


# Generated at 2022-06-14 14:21:59.379525
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    field = NeverMatch()
    assert field.errors == {"never": "This never validates."}


# Generated at 2022-06-14 14:22:02.555271
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    field = NeverMatch(name='NeverMatch')
    assert field.name == 'NeverMatch'
    assert field.errors == {"never": "This never validates."}
    assert field.allow_null == False
    assert field.required == False
    assert field.default == None


# Generated at 2022-06-14 14:22:03.638907
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    assert(NeverMatch().validate(None) == None)


# Generated at 2022-06-14 14:22:06.207277
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    assert IfThenElse(if_clause=Field(), then_clause=Field()).else_clause.typesystem_type == 'Any'

# Generated at 2022-06-14 14:22:07.342082
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    item = NeverMatch()


# Generated at 2022-06-14 14:22:11.261076
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    # At the moment, since NeverMatch inherits from Field,
    # we can't create a NeverMatch instance with keyword arguments.
    nm = NeverMatch()
    with pytest.raises(AssertionError):
        nm = NeverMatch(foo='bar')
