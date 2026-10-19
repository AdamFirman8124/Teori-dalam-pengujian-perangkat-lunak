

# Generated at 2022-06-14 14:12:50.571247
# Unit test for method validate of class Not
def test_Not_validate():
    # Case 1: Validation is impossible
    f1 = Not(String())
    value='abc'
    strict=True
    assert f1.validate(value, strict) == value

    # Case 2: Validation is impossible
    value = 'a'
    strict = False
    assert f1.validate(value, strict) == value

    # Case 3: Validation is OK
    value=1
    strict=True
    assert f1.validate(value, strict) == value

    # Case 4: Validation is OK
    value=1
    strict=False
    assert f1.validate(value, strict) == value


# Generated at 2022-06-14 14:13:01.184380
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    example = IfThenElse(True)
    assert example.validate(True) is True, "Error in validate of IfThenElse"
    example = IfThenElse(if_clause=True, then_clause=True, else_clause=False)
    assert example.validate(True) is True, "Error in validate of IfThenElse"
    assert example.validate(False) is False, "Error in validate of IfThenElse"
    example = IfThenElse(if_clause=False, then_clause=False)
    assert example.validate(True) is True, "Error in validate of IfThenElse"
    assert example.validate(False) is False, "Error in validate of IfThenElse"
    example = IfThenElse(False, False, True)

# Generated at 2022-06-14 14:13:06.296571
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    field_1 = Float()
    field_2 = Integer()
    field_3 = String()
    field_4 = OneOf([field_1, field_2, field_3])

    assert field_1.validate(3.14) == 3.14
    assert field_2.validate(3) == 3
    assert field_3.validate('I am a string') == 'I am a string'

    assert field_4.validate(3.14) == 3.14
    assert field_4.validate(3) == 3
    assert field_4.validate('I am a string') == 'I am a string'

    try:
        field_4.validate('true')
        assert False
    except ValueError as e:
        assert str(e) == 'String does not match expected format.'


# Generated at 2022-06-14 14:13:10.723724
# Unit test for method validate of class Not
def test_Not_validate():
    # arrange
    d = Not(negated=int, allow_null=True)
    # act
    e = d.validate(value="string", strict=True)
    # assert
    assert e == "string"
    assert d.validate(value="string", strict=True) == "string"

test_Not_validate()

# Generated at 2022-06-14 14:13:21.484601
# Unit test for method validate of class OneOf

# Generated at 2022-06-14 14:13:23.826194
# Unit test for constructor of class OneOf
def test_OneOf():
  subfields = [Field()]
  field = OneOf(subfields)
  assert field.one_of == subfields


# Generated at 2022-06-14 14:13:25.436658
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    field = NeverMatch()
    assert not field.validate(10)

# Generated at 2022-06-14 14:13:38.095773
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    # Test with if_clause
    test = IfThenElse(if_clause={"type": "integer"}, then_clause={"type": "string"})
    result = test.validate(1)
    assert result == "1"

    # Test without if_clause, but with else clause
    test = IfThenElse(then_clause={"type": "string"}, else_clause={"type": "integer"})
    result = test.validate(1)
    assert result == 1

    # Test with if_clause and else clause
    test = IfThenElse(if_clause={"type": "integer"}, then_clause={"type": "string"}, else_clause={"type": "integer"})
    result = test.validate(1)
    assert result == "1"

    # Test with all

# Generated at 2022-06-14 14:13:49.904692
# Unit test for method validate of class Not
def test_Not_validate():
    """
    Check if validate method returns passed value
    if nested field does not match.
    """

    # create a nested field that always validates
    class AlwaysMatch(Field):
        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            return value

    # create a root field with valid nested field
    root = Not(negated=AlwaysMatch())
    # validate anything
    valid, error = root.validate_or_error(1)
    # check if nested field validates
    assert valid == 1

    # create a root field with valid nested field
    root = Not(negated=AlwaysMatch())
    valid, error = root.validate_or_error(0)
    # check if nested field validates
    assert error is not None



# Generated at 2022-06-14 14:13:58.294882
# Unit test for method validate of class Not
def test_Not_validate():
    import typesystem
    import json
    # data = {'sales': 'good', 'revenue': 10000}
    schema = typesystem.Schema(
        properties={
            "sales": typesystem.String(choices=["good", "bad"]),
            "revenue": typesystem.Float(minimum=100),
        }
    )

    data = {'sales': 'good', 'revenue': 100}
    error = schema.validate(data)
    print(error)

    data = {'sales': 'bad', 'revenue': 100}
    error = schema.validate(data)
    print(error)

    data = {'sales': 'good', 'revenue': 10}
    error = schema.validate(data)
    print(error)


# Generated at 2022-06-14 14:14:12.399553
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    ItE = IfThenElse
    class C:
        def __init__(self, value): self.value = value
    c = C(value=2)
    assert ItE(if_clause=lambda x: x.value == 2, then_clause=lambda x: x.value == 2, else_clause=lambda x: x.value == 3).validate(c) == True
    assert ItE(if_clause=lambda x: x.value == 2, then_clause=lambda x: x.value == 2, else_clause=lambda x: x.value == 3).validate(c) == True

# Generated at 2022-06-14 14:14:14.010804
# Unit test for constructor of class AllOf
def test_AllOf():
    assert True # TODO: implement your test here


# Generated at 2022-06-14 14:14:21.067975
# Unit test for method validate of class Not
def test_Not_validate():
    from typesystem.fields import Boolean

    not_bool = Not(Boolean())
    validated_value, error = not_bool.validate_or_error(3)
    assert validated_value == 3
    assert error == None

    validated_value, error = not_bool.validate_or_error(True)
    assert error != None

# Generated at 2022-06-14 14:14:30.221242
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    valid_field_1 = Field()
    valid_field_1.validate = MagicMock(return_value=1)
    invalid_field_2 = Field()
    invalid_field_2.validate = MagicMock(side_effect=invalid_field_2.validation_error("error"))
    valid_field_3 = Field()
    valid_field_3.validate = MagicMock(return_value=2)

    test_object = OneOf([valid_field_1, invalid_field_2, valid_field_3])
    test_object.validate(1)

    valid_field_1.validate.assert_called_once_with(1)
    invalid_field_2.validate.assert_called_once_with(1)
    valid_field_3.validate.assert_called_

# Generated at 2022-06-14 14:14:31.129639
# Unit test for constructor of class AllOf
def test_AllOf():
    all_of = AllOf([])


# Generated at 2022-06-14 14:14:36.015179
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    class Test:
        def __init__(self, test_field : str):
            self.test_field = test_field
    test = Test("test")
    assert IfThenElse(Any(), None, None).validate(test) != []
    assert IfThenElse(Any(), None, None).validate(test) != {}
    assert IfThenElse(Any(), None, None).validate(test) != "test"



# Generated at 2022-06-14 14:14:40.345805
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    assert IfThenElse(if_clause=never_match(), then_clause=not_match(), else_clause=not_match()).validate("a") == "a"

# Generated at 2022-06-14 14:14:44.721170
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    assert IfThenElse(
        if_clause = String(),
        then_clause = String(),
        else_clause = String(min_length=3)
    ).validate('', False) == ""


# Generated at 2022-06-14 14:14:50.788918
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    field = IfThenElse(
        if_clause = AllOf(all_of = [Int(), Max(max = 10)]),
        then_clause = Min(min = 2),
        else_clause = Max(max = 16),
    )
    assert field.validate(4) == 4
    assert field.validate(20) == 20
    try:
        field.validate(1)
        assert False
    except ValidationError as error:
        assert str(error) == 'min'



# Generated at 2022-06-14 14:14:54.435108
# Unit test for method validate of class OneOf
def test_OneOf_validate():
  class UselessClass:
    def __init__(self, x: typing.Any = ""):
      self.x = x
  u = UselessClass("x")
  assert u.x == "x"

# Generated at 2022-06-14 14:15:07.634263
# Unit test for constructor of class OneOf
def test_OneOf():
    a = OneOf([])
    b = OneOf([OneOf([])])
    c = OneOf([Integer()])
    d = OneOf([Integer()], required=True)
    e = OneOf([Integer(), AllOf([Boolean()])])
    f = OneOf([Integer(), AllOf([Boolean()])], required=False)
    g = OneOf([Integer(), AllOf([Boolean()])], description="flarg")
    h = OneOf([Integer(), AllOf([Boolean()])], description="flarg", required=True)
    i = OneOf([Integer(), AllOf([Boolean()])], description="flarg", required=True, name="flarg")

# Generated at 2022-06-14 14:15:10.902711
# Unit test for constructor of class AllOf
def test_AllOf():
    string_field = String(max_length=10)
    number_field = Number(minimum=0)
    test_field = AllOf([string_field, number_field])
    assert test_field.all_of == [string_field, number_field]


# Generated at 2022-06-14 14:15:11.509201
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    X = NeverMatch()

# Generated at 2022-06-14 14:15:19.963175
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    assert IfThenElse(if_clause=Any(validators=[lambda x: x == 1]), then_clause=Any(validators=[lambda x: x == 2])).validate(1, strict=False) == 2
    assert IfThenElse(if_clause=Any(validators=[lambda x: x == 1]), then_clause=Any(validators=[lambda x: x == 1]), else_clause=Any(validators=[lambda x: x == 3])).validate(2, strict=False) == 3


# Generated at 2022-06-14 14:15:25.818009
# Unit test for method validate of class Not
def test_Not_validate():
    not_of_int = Not(Field(int))
    assert not_of_int.validate(0) == 0
    try:
        assert not_of_int.validate(1) == 1
    except Exception as e:
        assert str(e) == "{'negated': 'Must not match.'}"
    else:
        assert False



# Generated at 2022-06-14 14:15:30.914038
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    from typesystem import Integer, Object
    if_clause = Integer(minimum=10)
    then_clause = Integer(maximum=35)
    else_clause = Integer(minimum=35)
    field = IfThenElse(if_clause, then_clause, else_clause)
    obj = Object("test", {"x": field})
    obj.validate({"x": 11})
    obj.validate({"x": 34})
    obj.validate({"x": 40})

# Generated at 2022-06-14 14:15:39.591263
# Unit test for constructor of class AllOf
def test_AllOf():
    import sys
    import types
    import unittest
    import typesystem
    assert XFAIL, "buggy test skipped"
    class Test(unittest.TestCase):
        def test_AllOf_constructor_M_1(self):
            typesystem.fields.AllOf([None])
        def test_AllOf_constructor_M_2(self):
            typesystem.fields.AllOf([None]*2)
        def test_AllOf_constructor_M_3(self):
            typesystem.fields.AllOf([None, None])
        def test_AllOf_constructor_M_4(self):
            typesystem.fields.AllOf([None]*3)

# Generated at 2022-06-14 14:15:41.608672
# Unit test for method validate of class Not
def test_Not_validate():
    not_ = Not(Any())
    assert not_.validate(None) is None
    assert not_.validate(1) == 1
    assert not_.validate("string") == "string"

# Generated at 2022-06-14 14:15:53.096587
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    from typesystem.fields import Boolean
    from typesystem.fields import Integer
    from typesystem.fields import String

    if_clause = Boolean()
    then_clause = String()
    else_clause = Integer()
    testobj = IfThenElse(if_clause, then_clause, else_clause)
    testobj.validate(True, strict=False)
    try:
        testobj.validate("foo", strict=False)
        assert False, "string should not validate against then clause"
    except:
        pass
    testobj.validate(False, strict=False)
    try:
        testobj.validate("foo", strict=False)
        assert False, "string should not validate against else clause"
    except:
        pass

# Generated at 2022-06-14 14:15:54.794370
# Unit test for method validate of class Not
def test_Not_validate():
    attr = 'abc'
    assert_raises(TypeError, Not(attr).validate, attr)

# Generated at 2022-06-14 14:16:01.628010
# Unit test for method validate of class Not
def test_Not_validate():

    not_field = Not(negated=Any())
    not_field.validate(1)

    not_field = Not(negated=Boolean())
    not_field.validate(1)


# Generated at 2022-06-14 14:16:07.488577
# Unit test for constructor of class OneOf
def test_OneOf():
    import numpy as np
    from typesystem.fields.number import Number, Float

    ifThenElse = IfThenElse(Float())
    test_range = np.random.randint(0, 1000, (1, 1))
    for i in range(100):
        cur = test_range[np.random.randint(0, 100)]
        ifThenElse.validate(cur)



# Generated at 2022-06-14 14:16:14.542176
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    schema = OneOf(one_of={1,2,3})
    schema.validate(1)
    schema.validate(2)
    schema.validate(3)
    with pytest.raises(ValidationError):
        schema.validate(4)
    schema.validate(1, False)
    schema.validate(2, False)
    schema.validate(3, False)
    with pytest.raises(ValidationError):
        schema.validate(4, False)
    schema.validate(1, True)
    schema.validate(2, True)
    schema.validate(3, True)
    with pytest.raises(ValidationError):
        schema.validate(4, True)

# Generated at 2022-06-14 14:16:16.569738
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    field = NeverMatch()
    assert field.errors == {"never": "This never validates."}


# Generated at 2022-06-14 14:16:20.551949
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    from typesystem import Integer

    # Arrange
    then_clause = Integer()
    else_clause = Integer()
    value = 5

    # Act
    actual1 = IfThenElse(then_clause=then_clause, else_clause=else_clause)
    
    # Assert
    assert actual1.validate(value) == value


# Generated at 2022-06-14 14:16:24.797984
# Unit test for method validate of class Not
def test_Not_validate():
    field = Not(negated = Any())
    field.validate("test")
    try:
        field.validate(None)
        assert False == True
    except Exception:
        pass


# Generated at 2022-06-14 14:16:25.448851
# Unit test for method validate of class Not
def test_Not_validate():
    pass

# Generated at 2022-06-14 14:16:32.653071
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    field = IfThenElse(if_clause=1, then_clause=2, else_clause=3)
    assert field.validate(1) == 2
    assert field.validate(0) == 3
    field = IfThenElse(if_clause=1, then_clause=2)
    assert field.validate(1) == 2
    assert field.validate(0) is None
    field = IfThenElse(if_clause=1, else_clause=3)
    assert field.validate(1) is None
    assert field.validate(0) == 3

# Generated at 2022-06-14 14:16:34.595782
# Unit test for method validate of class Not
def test_Not_validate():
    value = 1
    strict = False
    test = Not(negated=value)

    assert test.validate(value=value, strict=strict) == value

# Generated at 2022-06-14 14:16:36.010661
# Unit test for method validate of class Not
def test_Not_validate():
    field = Not(Any())
    assert field.validate(None) == None

# Generated at 2022-06-14 14:16:40.314649
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    assert NeverMatch



# Generated at 2022-06-14 14:16:41.729463
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    assert NeverMatch()


# Generated at 2022-06-14 14:16:45.799548
# Unit test for constructor of class OneOf
def test_OneOf():
    """Test constructor"""
    o = OneOf()
    assert o.one_of == None
    o2 = OneOf(one_of = [1, 2, 3])
    assert o2.one_of == [1, 2, 3]


# Generated at 2022-06-14 14:16:47.993300
# Unit test for constructor of class Not
def test_Not():
    negated = Field()
    notField = Not(negated)
    assert(notField.negated is negated)


# Generated at 2022-06-14 14:16:49.939802
# Unit test for constructor of class Not
def test_Not():
    A = Field()
    B = Not(A)
    assert isinstance(B, Not)

# Generated at 2022-06-14 14:16:52.060468
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    pass
    # all_of = AllOf(one_of=[])
    # assert all_of.validate(2, 3) is None

# Generated at 2022-06-14 14:16:55.365383
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    field = OneOf(one_of=[Int(), Str()])

    assert field.validate(3) == 3
    assert field.validate("abc") == "abc"

    with pytest.raises(ValidationError):
        field.validate(None)
        field.validate(True)

# Generated at 2022-06-14 14:17:07.276521
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    # create a Field to use as if_clause
    f1 = Field("f1", required=True)

    # create a Field to use as then_clause
    f2 = Field("f2", required=True)

    # create a Field to use as else_clause
    f3 = Field("f3", required=True)

    # create a IfThenElse object
    ite = IfThenElse(f1, f2, f3)

    # test validate function of IfThenElse
    # f1, f2, f3 are all required
    assert ite.validate(1) == 1
    assert ite.validate("") == ""
    assert ite.validate([]) == []
    assert ite.validate({}) == {}
    assert ite.validate(True) == True

# Generated at 2022-06-14 14:17:11.697721
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    assert IfThenElse(
        String(),
        String(),
        String(),
    ).validate('a')=='a'
    assert IfThenElse(
        String(),
        String(),
        String(),
    ).validate(1)==1


# Generated at 2022-06-14 14:17:17.223443
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    if_clause = Field(required=True)
    then_clause = Field(required=True)
    else_clause = Field(required=True)
    if_then_else_field = IfThenElse(if_clause, then_clause, else_clause)

    # case 1
    assert if_then_else_field.validate(1) == 1
    # case 2
    assert if_then_else_field.validate(2) == 2

# Generated at 2022-06-14 14:17:31.089078
# Unit test for constructor of class IfThenElse

# Generated at 2022-06-14 14:17:35.942520
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    one_of = OneOf(one_of=[Field()])
    with pytest.raises(Field.validation_error):
        one_of.validate(12)
    assert one_of.validate(12) == 12


# Generated at 2022-06-14 14:17:38.473601
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    field = OneOf([Integer(),String()], name="testOneOf")
    field.validate(1)
    field.validate("2")


# Generated at 2022-06-14 14:17:39.629972
# Unit test for constructor of class AllOf
def test_AllOf():
    assert AllOf()


# Generated at 2022-06-14 14:17:46.731808
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    field = OneOf([])
    assert field.validate((0, 1)) == (0, 1)
    assert field.validate((0, 1)) == (0, 1)
    assert field.validate((0, 1)) == (0, 1)
    assert field.validate((0, 1)) == (0, 1)
    assert field.validate((0, 1)) == (0, 1)
    assert field.validate((0, 1)) == (0, 1)
    assert field.validate((0, 1)) == (0, 1)


if __name__ == "__main__":
    import sys
    import doctest

    doctest.testmod(verbose=True)
    sys.exit(0)

# Generated at 2022-06-14 14:17:50.072508
# Unit test for constructor of class Not
def test_Not():
    # Create argument
    negated = "Hello"

    # Create instance of class Not
    instance = Not(negated)

    # Check field values of instance are correct
    assert type(instance) == Not
    assert instance.negated == "Hello"

# Generated at 2022-06-14 14:17:52.401467
# Unit test for method validate of class Not
def test_Not_validate():
    not_ = Not(negated=Any(), label="not")
    actual = not_.validate(value="1")
    expected = "1"
    assert actual == expected

# Generated at 2022-06-14 14:17:52.975294
# Unit test for constructor of class AllOf
def test_AllOf():
    AllOf([], None, None)

# Generated at 2022-06-14 14:17:58.579956
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    if_clause = IfThenElse(field=1,type=int,source='a',validators=lambda value:True)
    then_clause = IfThenElse(field=2,type=int,source='a',validators=lambda value:True)
    else_clause = IfThenElse(field=3,type=int,source='a',validators=lambda value:True)
    field = IfThenElse(if_clause=if_clause,then_clause=then_clause,else_clause=else_clause)
    assert field.validate(4) == 3


# Generated at 2022-06-14 14:18:00.827068
# Unit test for constructor of class Not
def test_Not():
    not_field = Not(Field())
    assert not_field.negated == Field()

# Generated at 2022-06-14 14:18:08.627902
# Unit test for method validate of class Not
def test_Not_validate():
    """ Unit testing for method validate of class Not """
    field = Not(negated=Field())
    field.validate('345')


# Generated at 2022-06-14 14:18:10.394192
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    field = NeverMatch()
    error = field.validate(42)
    assert error == 'This never validates.'


# Generated at 2022-06-14 14:18:12.348787
# Unit test for constructor of class Not
def test_Not():
    not_field = Not(negated = Any())
    assert not_field.negated.__class__.__name__ == 'Any'

# Generated at 2022-06-14 14:18:19.135483
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    if_clause = Field()
    then_clause = Field()
    else_clause = Field()
    instance = IfThenElse(if_clause, then_clause, else_clause)
    assert instance.if_clause is if_clause
    assert instance.then_clause is then_clause
    assert instance.else_clause is else_clause
    assert instance.errors == {}



# Generated at 2022-06-14 14:18:20.197310
# Unit test for constructor of class OneOf
def test_OneOf():
    assert OneOf([])



# Generated at 2022-06-14 14:18:30.126661
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    oneof = OneOf(one_of=[Any()])
    validated_value = oneof.validate('somevalue')
    expected = 'somevalue'
    assert validated_value == expected, "It should equal to" + expected

    oneof = OneOf(one_of=[Any(), Any()])
    try:
        validated_value = oneof.validate('somevalue')
        expected = "This never validates."
        assert expected, "It should raise an error"
    except:
        pass

    oneof = OneOf(one_of=[NeverMatch()])
    try:
        validated_value = oneof.validate('somevalue')
        expected = "This never validates."
        assert expected, "It should raise an error"
    except:
        pass


# Generated at 2022-06-14 14:18:32.847765
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    try:
        NeverMatch()
    except AssertionError:
        assert False
    NeverMatch(description="test description")



# Generated at 2022-06-14 14:18:38.359383
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    oneOf_f1 = NeverMatch()
    oneOf_f2 = NeverMatch()

    # One of two NeverMatch fails to validate
    with pytest.raises(oneOf_f1.validation_error):
        o = OneOf([oneOf_f1, oneOf_f2])
        o.validate("nothing")


# Generated at 2022-06-14 14:18:42.949774
# Unit test for method validate of class Not
def test_Not_validate():
    # Setup
    if_clause = NeverMatch()
    then_clause = NeverMatch()
    else_clause = NeverMatch()
    n = IfThenElse(if_clause, then_clause, else_clause)
    # Exercise
    with pytest.raises(if_clause.validation_error):
        n.validate(None, strict=False)
    # Test

# Generated at 2022-06-14 14:18:55.229501
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    from typesystem import Schema

    people_schema = Schema(
        {
            "$schema": "http://json-schema.org/draft-04/schema#",
            "$id": "people_schema",
            "title": "People",
            "description": "A list of people",
            "type": "array",
            "items": {
                "type": "object",
                "title": "Person",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "The name of the person",
                    },
                    "age": {"type": "integer"},
                },
            },
        }
    )


# Generated at 2022-06-14 14:19:03.166196
# Unit test for constructor of class AllOf
def test_AllOf():
    a = AllOf()
    assert a is not None


# Generated at 2022-06-14 14:19:04.927719
# Unit test for constructor of class Not
def test_Not():
    not_field = Not(Field())
    assert not_field.negated == Field()



# Generated at 2022-06-14 14:19:08.533056
# Unit test for method validate of class Not
def test_Not_validate():
    f1 = Field()
    field_not = Not(f1)
    with pytest.raises(field_not.validation_error):
        field_not.validate("anything")
    field_not.validate(None)


# Generated at 2022-06-14 14:19:13.215692
# Unit test for constructor of class OneOf
def test_OneOf():
    a = OneOf([])
    assert isinstance(a,Field)
    assert a.errors == {'no_match': 'Did not match any valid type.', 'multiple_matches': 'Matched more than one type.'}
    assert a.one_of == []

# Generated at 2022-06-14 14:19:14.194352
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    field = NeverMatch()

# Generated at 2022-06-14 14:19:17.162033
# Unit test for constructor of class AllOf
def test_AllOf():
    a = Field(default="field1")
    b = Field(default="field2")
    all_ = AllOf([a, b])
    all_.validate("field3")


# Generated at 2022-06-14 14:19:25.311533
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    '''Define a small class for testing'''
    class Test:
        def __init__(self, val1 = None, val2 = None, val3 = None):
            self.val1 = val1
            self.val2 = val2
            self.val3 = val3
    
    '''Test only if_clause'''
    test1 = Test(1)
    schema = IfThenElse(Field(nullable = True, min_length=1))
    assert schema.validate(test1) == test1
    
    '''Test with then and else clause'''
    test2 = Test(1, 2, 3)

# Generated at 2022-06-14 14:19:26.233737
# Unit test for constructor of class Not
def test_Not():
    n = Not(negated=Any())
    assert n

# Generated at 2022-06-14 14:19:27.787934
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    if_clause = IfThenElse(
        Field(),
        Field(),
        Field(),
    )

# Generated at 2022-06-14 14:19:28.776221
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    f = NeverMatch()
    assert f.errors == {"never": "This never validates."}


# Generated at 2022-06-14 14:19:42.673018
# Unit test for constructor of class AllOf
def test_AllOf():
    list1 = [Any()]
    all_of = AllOf(list1)

    assert all_of.all_of == list1


# Generated at 2022-06-14 14:19:44.938973
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    # Arrange
    foo = NeverMatch()

    # Act
    bar = foo.validate(0)

    # Assert
    assert bar == None


# Generated at 2022-06-14 14:19:46.795469
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    never_match = NeverMatch()
    assert never_match.errors == {'never': 'This never validates.'}


# Generated at 2022-06-14 14:19:48.206605
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    assert NeverMatch()


# Generated at 2022-06-14 14:19:50.561035
# Unit test for constructor of class Not
def test_Not():
    not_field = Not("a")
    assert isinstance(not_field, Not)


# Generated at 2022-06-14 14:20:01.806623
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    f = NeverMatch()
    assert f.validate('a') == 'Unsupported Value'
    assert f.to_representation('a') == 'Unsupported Value'
    assert f.validate(0) == 'Unsupported Value'
    assert f.to_representation(0) == 'Unsupported Value'
    assert f.validate('0') == 'Unsupported Value'
    assert f.to_representation('0') == 'Unsupported Value'
    assert f.validate('') == 'Unsupported Value'
    assert f.to_representation('') == 'Unsupported Value'
    assert f.validate(True) == 'Unsupported Value'
    assert f.to_representation(True) == 'Unsupported Value'
    assert f.validate(None) == 'Unsupported Value'
    assert f.to_

# Generated at 2022-06-14 14:20:04.797238
# Unit test for constructor of class AllOf
def test_AllOf():
    from typesystem import String, Integer
    all_field = AllOf((String(), Integer()))
    try:
        all_field.validate('4')
        raise Exception
    except Exception:
        pass


# Generated at 2022-06-14 14:20:08.955765
# Unit test for constructor of class AllOf
def test_AllOf():
    a = AllOf([])
    assert a.all_of == []
    assert a.error_messages == {}
    assert a.allow_null == False
    assert a.default == None
    assert a.description == None
    assert a.id == None
    assert a.name == None
    assert a.title == None


# Generated at 2022-06-14 14:20:20.241799
# Unit test for method validate of class Not
def test_Not_validate():
    f1 = String()
    f2 = String()
    f3 = String()
    fields = [f1,f2,f3]
    def test1():
        assert f3.validate("ddd") == "ddd"
    def test2():
        assert f3.validate("ddd") == "ddd"

# Generated at 2022-06-14 14:20:21.489964
# Unit test for constructor of class OneOf
def test_OneOf():
    field = OneOf([])
    assert field.one_of == []


# Generated at 2022-06-14 14:20:45.011985
# Unit test for method validate of class Not
def test_Not_validate():
  field = Not(Any())
  field.validate("str")
  field.validate(None)

# Generated at 2022-06-14 14:20:45.599401
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
   assert NeverMatch()

# Generated at 2022-06-14 14:20:46.647699
# Unit test for constructor of class OneOf
def test_OneOf():
    assert OneOf(one_of = [Field()])

# Generated at 2022-06-14 14:20:48.802466
# Unit test for method validate of class Not
def test_Not_validate():
    # Null test
    not_field = Not(Any())
    assert not_field.validate(None) == None


# Generated at 2022-06-14 14:20:51.373434
# Unit test for constructor of class Not
def test_Not():
    print("Test: constructor of class Not")
    assert Not(1, label="Not") != None
    print("Success")


# Generated at 2022-06-14 14:20:52.596693
# Unit test for constructor of class Not
def test_Not():
    assert isinstance(Not(negated=Any()), Not)

# Generated at 2022-06-14 14:20:54.188323
# Unit test for method validate of class Not
def test_Not_validate():
    # Todo: Write a unit test for method validate of class Not
    raise NotImplementedError()


# Generated at 2022-06-14 14:20:56.773460
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    """Test IfThenElse"""
    field1 = Field()
    field2 = Field()
    field3 = Field()
    if_else1 = IfThenElse(field1,field2,field3)
    assert isinstance(if_else1,IfThenElse)

# Generated at 2022-06-14 14:21:02.887538
# Unit test for method validate of class Not
def test_Not_validate():
    field = Not(mock.Mock())
    field.negated.validate_or_error.return_value = (None, None)
    actual = field.validate(mock.sentinel.value)
    assert actual == mock.sentinel.value
    field.negated.validate_or_error.assert_called_once_with(
        mock.sentinel.value, strict=False
    )



# Generated at 2022-06-14 14:21:04.970692
# Unit test for constructor of class Not
def test_Not():
    plainField = Field()
    notField = Not(plainField)
    assert notField.negated is plainField



# Generated at 2022-06-14 14:21:52.455440
# Unit test for constructor of class AllOf
def test_AllOf():
    n = AllOf([])
    assert n.errors == {}
    assert n.all_of == []
    assert n.name == "all_of"


# Generated at 2022-06-14 14:21:53.426207
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    NeverMatch()

# Generated at 2022-06-14 14:21:55.104332
# Unit test for constructor of class Not
def test_Not():
    class Foo():
        pass
    foo = Foo()
    assert(foo.errors == None)


# Generated at 2022-06-14 14:21:56.444434
# Unit test for constructor of class AllOf
def test_AllOf():
    allOf = AllOf([])
    assert allOf.all_of is not None

# Generated at 2022-06-14 14:22:02.521495
# Unit test for method validate of class Not
def test_Not_validate():

    # 1. define the field
    negated = String()
    not_field = Not(negated)

    # 2. define the value to test
    # this value will fail because it is a String
    value = "hello"
    
    # 2.1 define the value to test
    # this value will pass because it is not a String
    #value = 1

    # 3. define expected value
    expected_value = value

    # 4. test
    result = not_field.validate(value)
    assert result == expected_value



# Generated at 2022-06-14 14:22:05.281133
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    """Test constructor of class NeverMatch"""

    # Test value of None for None set
    field = NeverMatch(allow_null=True)
    assert field.validate(None) == None
    # Test value of None for None unset
    field = NeverMatch()
    field.validate(None)


# Generated at 2022-06-14 14:22:08.108231
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    field = NeverMatch()
    assert(field.errors == {"never": "This never validates."})
    assert(field.allow_null == False)
    assert(field.default == None)


# Generated at 2022-06-14 14:22:11.754404
# Unit test for constructor of class AllOf
def test_AllOf():
    field = AllOf([String(), Integer()])
    assert field.all_of[0].__class__.__name__ == "String"
    assert field.all_of[1].__class__.__name__ == "Integer"


# Generated at 2022-06-14 14:22:12.658958
# Unit test for constructor of class OneOf
def test_OneOf():
    x = OneOf([])


# Generated at 2022-06-14 14:22:15.978519
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    never = NeverMatch()
    with pytest.raises(AssertionError) as excinfo:
        never = NeverMatch(allow_null=True)
    assert "allow_null" in str(excinfo)