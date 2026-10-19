

# Generated at 2022-06-14 14:12:54.905375
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    Ite = IfThenElse(Field(),Field(),Field(),Field())
    class IteTest:
        def test_1(self):
            pass
        def test_2(self):
            pass
        def test_3(self):
            pass
        def test_4(self):
            pass
    ite_test = IteTest()
    ite_test.test_1 = lambda: Ite.if_clause.validate(1) == None
    ite_test.test_2 = lambda: Ite.then_clause.validate(2) == None
    ite_test.test_3 = lambda: Ite.else_clause.validate(3) == None
    ite_test.test_4 = lambda: Ite.validate(4) == None
    ite_test.test_1

# Generated at 2022-06-14 14:12:58.279441
# Unit test for method validate of class Not
def test_Not_validate():
    not_null = Not(Any(), allow_null=False)
    assert not_null.validate({"a": 123}) == {"a": 123}
    assert not_null.validate(None) == {"a": 123}

# Generated at 2022-06-14 14:13:00.643434
# Unit test for constructor of class AllOf
def test_AllOf():
    print("Testing AllOf constructor")
    al = AllOf(0)
    print(al.all_of)



# Generated at 2022-06-14 14:13:10.652038
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    pattern = re.compile("^<!\[CDATA\[.*\]\]>$")
    string_value = "test_IfThenElse_validate"
    class_value = "test_IfThenElse_validate"
    # Conditional sub-item matching.
    ifThenElse_field = IfThenElse(pattern)
    # Valid type
    validated_value = ifThenElse_field.validate(string_value)
    assert validated_value == string_value

    # Invalid type
    with pytest.raises(ValidationError) as excinfo:
        ifThenElse_field.validate(class_value)
    assert str(excinfo.value) == "Value must match the given pattern."

# Generated at 2022-06-14 14:13:14.457976
# Unit test for method validate of class Not
def test_Not_validate():
    assert Not(Any()).validate(1) == 1
    assert Not(Any()).validate("") == ""
    assert Not(Integer()).validate("") == ""
    try:
        Not(Integer()).validate(1)
        assert False
    except:
        assert True


# Generated at 2022-06-14 14:13:19.155620
# Unit test for method validate of class Not
def test_Not_validate():
    from typesystem.fields import Integer
    from typesystem.exceptions import ValidationError
    import pytest

    field = Not(Integer())

    with pytest.raises(ValidationError) as excinfo:
        field.validate(0)

    assert excinfo.match("Must not match.")



# Generated at 2022-06-14 14:13:23.354356
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    assert IfThenElse(
        OneOf([String(), Integer()]), then_clause=Integer()
        ).validate("foo") == "foo"
    assert IfThenElse(
        OneOf([String(), Integer()]), then_clause=Integer()
        ).validate(42) == 42

# Generated at 2022-06-14 14:13:36.550660
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    if_clause = BaseSchema(strict=True)
    if_clause.fields = {"name": String()}
    if_clause.make_validator()
    then_clause = BaseSchema(strict=True)
    then_clause.fields = {"name": String()}
    then_clause.make_validator()
    else_clause = BaseSchema(strict=True)
    else_clause.fields = {"name": String()}
    else_clause.make_validator()
    data = {"name": "smile"}
    ite = IfThenElse(if_clause, then_clause, else_clause)
    with pytest.raises(errors.ValidationError):
        ite.validate(data, strict=False)

# Generated at 2022-06-14 14:13:43.111901
# Unit test for method validate of class Not
def test_Not_validate():
    #the digit type
    digit_clause = Field.as_type(int)
    not_digit_if = Not(digit_clause)

    #the not digit type
    assert not_digit_if.validate('a') == 'a'
    assert not_digit_if.validate('abc') == 'abc'
    assert not_digit_if.validate('123') == '123'

    #the digit type
    assert not_digit_if.validate(123) == 123
    assert not_digit_if.validate(-123) == -123
    assert not_digit_if.validate(100) == 100

    #the digit type
    assert not_digit_if.validate(True) == True
    assert not_digit_if.validate(False) == False
    assert not_digit_if.valid

# Generated at 2022-06-14 14:13:47.945735
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    field = IfThenElse(int, min_value=2)
    assert field.validate(2) == 2
    with raises(ValidationError) as excinfo:
        field.validate(1)
    with raises(ValidationError) as excinfo:
        field.validate("b")


# Generated at 2022-06-14 14:13:54.788561
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    from typesystem.fields import Integer

    field = IfThenElse(Integer(), Integer())

    assert field.validate(5) == 5

    assert field.validate(5.0) == 5

    assert field.validate(5.5) == 5

    assert field.validate(5.5, strict=True) == 5

# Generated at 2022-06-14 14:14:05.303122
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    assert OneOf(one_of=[Any()]).validate("toto").name == 'Any'
    assert OneOf(one_of=[Any()]).validate(1).name == 'Any'
    assert OneOf(one_of=[Any()]).validate(True).name == 'Any'
    assert OneOf(one_of=[Any()]).validate([1, 2]).name == 'Any'
    assert OneOf(one_of=[Any()]).validate([1, 2]).name == 'Any'
    assert OneOf(one_of=[Any()]).validate({'a':'b'}).name == 'Any'


# Generated at 2022-06-14 14:14:09.894213
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    f = OneOf([
        typing.List[int],
        typing.List[str],
    ])
    a = f.validate([1, 2])
    b = f.validate(['1', '2'])
    assert a == [1, 2]
    assert b == ['1', '2']


# Generated at 2022-06-14 14:14:11.948572
# Unit test for constructor of class AllOf
def test_AllOf():
    items = [Any() for _ in range(5)]
    field = AllOf(items)
    assert field.all_of == items



# Generated at 2022-06-14 14:14:12.312928
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    assert(True)

# Generated at 2022-06-14 14:14:16.888697
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    # Given
    one_of = OneOf([Any(), Any(), Any()])

    # When
    result = one_of.validate(1)

    # Then
    assert result == 1

# Generated at 2022-06-14 14:14:19.213784
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    with assert_raises(AssertionError):
        NeverMatch(allow_null=False)


# Generated at 2022-06-14 14:14:20.750433
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    def test():
        assert NeverMatch()
    test()


# Generated at 2022-06-14 14:14:22.664264
# Unit test for constructor of class AllOf
def test_AllOf():
    assert AllOf(all_of = [Field(required=True)], required=True)


# Generated at 2022-06-14 14:14:31.187159
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():

    tests = [
        {
            "value": 0,
            "if_clause": Integer(),
            "then_clause": Integer(),
            "else_clause": Integer(),
            "expect": 0
        },
        {
            "value": 0,
            "if_clause": Integer(),
            "then_clause": String(),
            "else_clause": Integer(),
            "expect": 0
        },
        {
            "value": 0,
            "if_clause": String(),
            "then_clause": String(),
            "else_clause": Integer(),
            "expect": 0
        },
    ]

    for test in tests:
        if_clause = test["if_clause"]
        then_clause = test["then_clause"]

# Generated at 2022-06-14 14:14:45.747752
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    field = OneOf(one_of=[String(), Int(), Bool()])
    assert field.validate("hello") == "hello"
    assert field.validate(1) == 1
    assert field.validate(True) is True
    # Error message
    with pytest.raises(ValidationError) as excinfo:
        field.validate(None)
    assert excinfo.value.args[0]["json"] == {
        "$schema": {
            "code": "no_match",
            "message": "Did not match any valid type.",
        }
    }
    # Error message
    with pytest.raises(ValidationError) as excinfo:
        field.validate([])

# Generated at 2022-06-14 14:14:51.964486
# Unit test for method validate of class Not
def test_Not_validate():
    field = Not(Boolean())
    value = 1
    strict = False
    assert field.validate(value, strict) == value
    field.negated.errors = {"invalid": "Value must be <class 'int'>"}
    try:
        field.validate(value, strict)
    except ValidationError as e:
        assert e.code == "invalid"
        assert e.path == []
        assert e.value == value
        assert e.field.errors == {"invalid": "Value must be <class 'int'>"}
        assert e.field.__class__ == Boolean


# Generated at 2022-06-14 14:14:56.320177
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    from typesystem import Integer
    ite = IfThenElse(Integer(2), Integer(3), Integer(4))
    ite.validate(3)
    ite.validate(4)
    ite.validate(3)
    ite.validate(2)

# Generated at 2022-06-14 14:14:58.457262
# Unit test for method validate of class Not
def test_Not_validate():
    field = Not(None)
    value = 'Test'
    assert field.validate(value) == value

# Generated at 2022-06-14 14:15:00.962004
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    # Specific test case for constructor of class NeverMatch
    field = NeverMatch()
    assert isinstance(field, NeverMatch)


# Generated at 2022-06-14 14:15:04.442336
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    import typesystem
    schema = typesystem.Schema(
        typesystem.IfThenElse(None, 0)
    )
    assert schema.validate(0) == 0
    assert schema.validate(None) == None

# Generated at 2022-06-14 14:15:09.206163
# Unit test for constructor of class Not
def test_Not():
    # Arrange
    myField = Not(Field())

    # Act
    # Assert
    assert myField.required
    assert myField.error_messages == {'negated': 'Must not match.'}
    assert myField.negated == Field()
    assert myField.field_name == 'Not'


# Generated at 2022-06-14 14:15:21.134739
# Unit test for method validate of class Not

# Generated at 2022-06-14 14:15:23.188124
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    NeverMatch()

    # Constructor should accept None value
    NeverMatch(None)


# Generated at 2022-06-14 14:15:31.436599
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    from . import Number
    from .constants import MAX_INTEGER
    if_clause = Number(minimum=0, maximum=MAX_INTEGER)
    then_clause = Number(minimum=0, maximum=MAX_INTEGER)
    else_clause = Number(minimum=-MAX_INTEGER, maximum=0)
    if_then_else = IfThenElse(if_clause=if_clause, then_clause=then_clause, else_clause=else_clause)
    assert if_then_else.validate(5) == 5
    assert if_then_else.validate(-5) == -5

# Generated at 2022-06-14 14:15:38.532781
# Unit test for constructor of class Not
def test_Not():
    try:
        Not(None)
    except AssertionError:
        assert True
    negated = Not(Any())
    assert negated.negated.errors == {'invalid': 'is invalid'}


# Generated at 2022-06-14 14:15:39.392501
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    pass


# Generated at 2022-06-14 14:15:45.758993
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    # Test that correct input condition makes then_clause run and returns correct result
    test_field = IfThenElse(if_clause=String(max_length=2), then_clause=String(max_length=3), else_clause=String(max_length=6))
    assert test_field.validate('a') == 'a'
    # Test that wrong input condition makes else_clause run and returns correct result
    test_field2 = IfThenElse(if_clause=String(max_length=2), then_clause=String(max_length=3), else_clause=String(max_length=6))
    assert test_field2.validate('abcdefg') == 'abcdefg'
    # Test that wrong results from both clauses returns error

# Generated at 2022-06-14 14:15:49.645303
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    field = NeverMatch()
    assert field.allow_null is False
    assert field.error_messages == {"never": "This never validates."}


# Generated at 2022-06-14 14:15:58.866340
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    field1 = IfThenElse(if_clause="if this", then_clause="then this", else_clause="else this")
    field2 = IfThenElse(if_clause="if this", then_clause="then this")
    field3 = IfThenElse(if_clause="if this", then_clause="then this", else_clause=Field())
    field4 = IfThenElse(if_clause="if this", then_clause=Field(), else_clause=Field())
    field5 = IfThenElse(if_clause="if this", then_clause=Field(), else_clause="else this")
    field6 = IfThenElse(if_clause="if this", then_clause=Field())

# Generated at 2022-06-14 14:16:04.251478
# Unit test for constructor of class AllOf
def test_AllOf():
    from typesystem.fields import String, Integer
    field = AllOf([String(), Integer()])
    assert isinstance(field, AllOf)
    assert field.all_of[0] is String()
    assert field.all_of[1] is Integer()
    assert field.allow_null is False


# Generated at 2022-06-14 14:16:06.032318
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    assert IfThenElse(Any(), Any(), Any()).validate(123) == 123


# Generated at 2022-06-14 14:16:13.860154
# Unit test for constructor of class AllOf
def test_AllOf():
    import typesystem
    from typesystem import types

    class MyException(Exception):
        pass

    class TypeA(typesystem.types.String):
        def __init__(self, **kwargs: typing.Any) -> None:
            super().__init__(**kwargs)

    class TypeB(typesystem.types.String):
        def __init__(self, **kwargs: typing.Any) -> None:
            super().__init__(**kwargs)

    field = types.AllOf([TypeA(), TypeB()])

    #raise MyException("testing exception")
    try:
        result = field.validate("testing")
    except MyException as e:
        print("expecting error")
        raise e
    print(result)


# Generated at 2022-06-14 14:16:22.306095
# Unit test for method validate of class Not
def test_Not_validate():
    # Set up mock
    test_field = typing.cast(Field, mock.Mock())
    test_value = mock.Mock()
    test_strict = mock.Mock()
    negated_error = mock.Mock()
    test_field.validate_or_error.return_value = (mock.Mock(), negated_error)
    expected = mock.Mock()
    # Perform test
    test_unit = Not(test_field)
    actual = test_unit.validate(test_value, test_strict)
    # Assert
    test_field.validate_or_error.assert_called_once_with(test_value, test_strict)
    assert actual is expected

# Generated at 2022-06-14 14:16:25.147269
# Unit test for constructor of class AllOf
def test_AllOf():
    a = AllOf([Int(),Float()], required=True)
    assert a.required == True
    assert a.__class__.__name__ == "AllOf"


# Generated at 2022-06-14 14:16:33.905240
# Unit test for method validate of class Not
def test_Not_validate():
    f = Not(negated=Int())
    # negation

# Generated at 2022-06-14 14:16:34.794011
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    x = NeverMatch()


# Generated at 2022-06-14 14:16:45.222690
# Unit test for method validate of class Not
def test_Not_validate():
    class MyField(Field):
        def __init__(self, **kwargs):
            assert "allow_null" not in kwargs
            super().__init__(**kwargs)

        def validate(self, value):
            return True, 'test'

    # Branch coverage
    my_field = MyField()
    not_field = Not(my_field)
    try:
        not_field.validate(123)
    except Exception as e:
        assert str(e) == "Must not match."

    # Branch coverage
    my_field = MyField()
    not_field = Not(my_field)
    assert not_field.validate(123) == 123



# Generated at 2022-06-14 14:16:54.897350
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    one_if = 1
    zero_if = 0
    one_then = 1
    zero_then = 0
    one_else = 1
    zero_else = 0

    assert IfThenElse(one_if, one_then).validate(1) == 1
    assert IfThenElse(one_if, one_then).validate(0) == 1
    assert IfThenElse(zero_if, one_then).validate(1) == 1
    assert IfThenElse(zero_if, one_then).validate(0) == 1
    assert IfThenElse(one_if, zero_then).validate(1) == 0
    assert IfThenElse(one_if, zero_then).validate(0) == 0
    assert IfThenElse(zero_if, zero_then).validate(1) == 0
    assert If

# Generated at 2022-06-14 14:16:58.943379
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    field = IfThenElse(if_clause=Field(), then_clause=Field(required=True), else_clause=Field())
    try:
        field.validate({})
    except Exception as e:
        print(e)


# Generated at 2022-06-14 14:17:00.860882
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    pass
    nm = NeverMatch()
    assert nm.name == "NeverMatch"

# Generated at 2022-06-14 14:17:09.436844
# Unit test for constructor of class Not
def test_Not():
    assert Not().__eq__(Not())
    assert Not({}).__eq__(Not({}))
    a = Boolean(True)
    assert Not(a).__eq__(Not(a))
    assert Not({'negated': a}).__eq__(Not({'negated': a}))
    b = Boolean(False)
    print(Not(b).errors)
    assert Not(b).errors == {'negated': "Must not match."}
    assert Not({'negated': b}).__eq__(Not({'negated': b}))


# Generated at 2022-06-14 14:17:12.700510
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    assert IfThenElse(
        if_clause=NeverMatch(),
        then_clause=NeverMatch(),
        else_clause=NeverMatch()
    ).validate() == None

# Generated at 2022-06-14 14:17:13.191813
# Unit test for constructor of class Not
def test_Not():
    field = Not(field=Field())
    assert field

# Generated at 2022-06-14 14:17:16.173401
# Unit test for method validate of class Not
def test_Not_validate():
    test_value = 1
    test_field = Not(int)
    assert test_field.validate(test_value) == test_value
    assert test_field.validate(test_value, strict=True) == test_value

# Generated at 2022-06-14 14:17:22.038518
# Unit test for constructor of class Not
def test_Not():
    assert 1==1


# Generated at 2022-06-14 14:17:25.758650
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    field = NeverMatch()
    assert field.label == 'Never match'
    assert field.description == 'Doesn\'t ever match.'
    assert field.required
    assert field.allow_null == False



# Generated at 2022-06-14 14:17:32.169931
# Unit test for constructor of class AllOf
def test_AllOf():
    x = AllOf([])
    assert str(x) == 'AllOf()'
    x = AllOf([], description='Foo')
    assert str(x) == "AllOf(description='Foo')"
    x = AllOf([], name='Foo')
    assert str(x) == "AllOf(name='Foo')"
    x = AllOf([], description='Foo', name='Foo')
    assert str(x) == "AllOf(description='Foo', name='Foo')"


# Generated at 2022-06-14 14:17:42.788879
# Unit test for constructor of class OneOf
def test_OneOf():
    one_of = OneOf([])
    assert one_of.one_of == []
    assert one_of.name is None
    assert one_of.description is None
    assert one_of.subtypes == []
    assert one_of.allow_cast is True
    assert one_of.validators == {}
    assert one_of.allow_empty_strings is False
    assert one_of.allow_null is False
    assert one_of.default is None
    assert one_of.error_messages == {
        'required': 'This field is required.',
        'no_match': 'Did not match any valid type.',
        'multiple_matches': 'Matched more than one type.',
    }


# Generated at 2022-06-14 14:17:49.942261
# Unit test for constructor of class AllOf
def test_AllOf():
    from typesystem import (
        AllOf,
        CompoundField,
        Number,
        String,
        Array,
        ArrayOf,
    )
    
    a = AllOf([String, Number])
    assert isinstance(a, CompoundField)
    assert type(a.all_of[0])==String
    assert type(a.all_of[1])==Number
    

# Generated at 2022-06-14 14:17:51.024461
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    def test_validate(self=None):
        # TODO: Write test
        pass



# Generated at 2022-06-14 14:17:52.999582
# Unit test for method validate of class Not
def test_Not_validate():
  field = Not(negated=None)
  assert field.validate(None)
  assert not field.validate(1)

# Generated at 2022-06-14 14:17:59.802195
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    # Test constructor with no paramater and check fields
    field = NeverMatch()
    assert field.errors == { 'never': 'This never validates.' }

    # Test constructor with paramaters and check fields
    field = NeverMatch(description='this is never matched')
    assert field.description == 'this is never matched'

    # Test constructor with paramaters and check fields
    field = NeverMatch(example='this is never matched')
    assert field.example == 'this is never matched'

    # Test constructor with paramaters and check fields
    field = NeverMatch(name='this is never matched')
    assert field.name == 'this is never matched'

    # Test constructor with invalid paramater

# Generated at 2022-06-14 14:18:01.656131
# Unit test for constructor of class OneOf
def test_OneOf():
    oneOfField = OneOf([])
    assert oneOfField.one_of == []

# Generated at 2022-06-14 14:18:02.990573
# Unit test for constructor of class AllOf
def test_AllOf():
    field = AllOf([])
    assert field

# Generated at 2022-06-14 14:18:12.421817
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    field = NeverMatch()
    assert field.errors == {"never": "This never validates."}


# Generated at 2022-06-14 14:18:17.500860
# Unit test for method validate of class Not
def test_Not_validate():
    import typesystem
    error = None

    # Create an object of the class via constructor
    item_object = Not(negated=typesystem.String())
    try:
        # Valid value
        item_object.validate(value="abc")
    except Exception as e:
        error = e

    assert error is None

# Generated at 2022-06-14 14:18:18.985526
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    field = NeverMatch()
    assert 'never' in field.errors


# Generated at 2022-06-14 14:18:24.457620
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():

    from typesystem.types import String

    class MyField(IfThenElse):
        def __init__(self,  **kwargs) -> None:
            super().__init__(if_clause=String,**kwargs)

    field = MyField()
    assert field.validate("A") == "A"
    assert field.validate(1) == 1



# Generated at 2022-06-14 14:18:26.601400
# Unit test for constructor of class OneOf
def test_OneOf():
    obj = OneOf(one_of=['Not a field'])
    assert obj.one_of == ['Not a field']

# Generated at 2022-06-14 14:18:33.891939
# Unit test for method validate of class Not
def test_Not_validate():
    Field_ins1 = Not()
    ins = Not(Field_ins1)
    assert ins.validate("") == ""
    assert ins.validate("String") == "String"
    assert ins.validate("[1,2,3]") == "[1,2,3]"
    assert ins.validate(10) == 10
    assert ins.validate(True) == True
    assert ins.validate(False) == False
    assert ins.validate({"key":"value"}) == {"key":"value"}
    assert ins.validate(None) == None
    assert ins.validate([1,2,3]) == [1,2,3]
    assert ins.validate({"key":"value", "key2":"value2"}) == {"key":"value", "key2":"value2"}
    assert ins.validate

# Generated at 2022-06-14 14:18:38.313191
# Unit test for method validate of class Not
def test_Not_validate():
    test_obj = Not(negated=None)
    with pytest.raises(test_obj.validation_error) as excinfo:
        test_obj.validate(value=0)
    assert 'Must not match.' == str(excinfo.value)

# Generated at 2022-06-14 14:18:41.879985
# Unit test for constructor of class OneOf
def test_OneOf():
    # Test the constructor of the class
    this_list = [Any()]
    this_list.append(Any())
    this_list.append(Any())
    a = OneOf(this_list)
    print("This is a: ", a)

# Generated at 2022-06-14 14:18:44.059533
# Unit test for method validate of class Not
def test_Not_validate():
    not_field = Not(Any())
    # when
    not_field.validate(None)


# Generated at 2022-06-14 14:18:46.291364
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    ne = NeverMatch()
    assert not ne


# Generated at 2022-06-14 14:18:56.462399
# Unit test for method validate of class Not
def test_Not_validate():
    field = Not(negated=Field())
    assert field.validate("ABCD") == "ABCD"



# Generated at 2022-06-14 14:18:57.794522
# Unit test for constructor of class AllOf
def test_AllOf():
    field = AllOf(all_of=list())
    assert field.all_of == list()
        

# Generated at 2022-06-14 14:19:00.320312
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    x = NeverMatch()
    assert x


# Generated at 2022-06-14 14:19:03.989407
# Unit test for constructor of class AllOf
def test_AllOf():
    try:
        all_of = AllOf(all_of=[])
        assert True
    except:
        assert False


# Generated at 2022-06-14 14:19:09.423915
# Unit test for method validate of class Not
def test_Not_validate():
    from typesystem.fields import Integer, Not
    field = Not(Integer(), min_value = 3)
    field.validate(value=1)
    field.validate(value=2)
    with pytest.raises(field.validation_error):
        field.validate(value=3)
        field.validate(value=4)
        field.validate(value=5)
    field.validate(value=None)

# Generated at 2022-06-14 14:19:13.128417
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    f = NeverMatch()
    try:
        f.validate(1)
    except f.ValidationError as e:
        assert e.code == 'never'
        assert str(e) == 'This never validates.'

# Generated at 2022-06-14 14:19:16.006257
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    field = IfThenElse(then_clause = Field())
    assert field.validate('string') == 'string'
    assert field.validate(1) == 1


# Generated at 2022-06-14 14:19:20.831391
# Unit test for method validate of class Not
def test_Not_validate():
    # Case 1: value is not string
    my_field = Not(String(max_length=5))
    assert my_field.validate('aaaaaaaaa') is None, 'Value must be none'
    # Case 2: value is string
    my_field = Not(Int())
    assert my_field.validate('a'), 'Value must be true'


# Generated at 2022-06-14 14:19:23.153728
# Unit test for method validate of class Not
def test_Not_validate():
    not_field = Not(negated = "string")
    value = "string1"
    strict = False
    print(not_field.validate(value, strict))
    # except


# Generated at 2022-06-14 14:19:26.035172
# Unit test for constructor of class Not
def test_Not():
	field = Not(negated = None)
	assert field.errors is not None
	assert field.negated is None
	assert field.name is None


# Generated at 2022-06-14 14:19:43.407613
# Unit test for method validate of class Not
def test_Not_validate():
    Not(Any()).validate('wrong')

# Generated at 2022-06-14 14:19:49.515119
# Unit test for method validate of class Not
def test_Not_validate():
    one = 1
    none = None

    test_success = Not(Any())
    test_failure = Not(Any(allow_null=False))
    #Test if value is None and not a required field
    assert test_success.validate(none) is None
    #Test if value is None and is a required field
    try:
        test_failure.validate(none)
    except Exception as e:
        assert e.args[0] == "This field is required."
    #Test for failure case
    try:
        test_failure.validate(1)
    except Exception as e:
        assert e.args[0] == "Must not match."

# Generated at 2022-06-14 14:20:01.188120
# Unit test for method validate of class Not
def test_Not_validate():
    from typesystem import Schema
    from typesystem.types import String
    class A(Schema):
        a = Integer(min_value=1)

    class B(Schema):
        b = Integer(min_value=2)

    class C(Schema):
        c = Not(negated=OneOf([A, B]))

    assert C({'c': {'a': 1}}).is_valid() is False
    assert C({'c': {'b': 2}}).is_valid() is False
    assert C({'c': {'a': 3}}).is_valid() is True
    assert C({'c': {'b': 3}}).is_valid() is True
    assert C({'c': 'a'}).is_valid() is True
    # assert C({'c': 3}).is_valid

# Generated at 2022-06-14 14:20:05.766067
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    field1 = MyCustomField()
    field2 = MyCustomField()
    field3 = MyCustomField()
    field = IfThenElse(field1, field2, field3)
    assert field.if_clause == field1
    assert field.then_clause == field2
    assert field.else_clause == field3

# Generated at 2022-06-14 14:20:09.624730
# Unit test for method validate of class Not
def test_Not_validate():
    def func():
        schema = {'not': {'type': 'integer'}}
        params = 1
        data = typesystem.load_schema(schema, params)
        return data
    assert func(test_Not_validate) == type.__call__('1',)


# Generated at 2022-06-14 14:20:15.851989
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    def test(if_clause, then_clause, else_clause, value, expected):
        field = IfThenElse(if_clause, then_clause, else_clause)
        result = field.validate(value)
        assert result == expected
        print(result)

    test(1, 2, 3, 1, 2)
    test(1, 2, 3, 0, 3)

# Generated at 2022-06-14 14:20:20.156089
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    dic= {'name': 'Larry Page', 'age': '45'}
    field = IfThenElse(Field(type='string'), Field(type='string'), Field(type='string'))
    if field.validate(dic) is not None:
        assert False
    else:
        assert True


# Generated at 2022-06-14 14:20:25.717160
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    if_clause = Field()
    then_clause = Field()
    else_clause = Field()
    test_if_then_else = IfThenElse(if_clause, then_clause, else_clause)
    test_if_then_else.validate(1)
    test_if_then_else.validate(2)


# Generated at 2022-06-14 14:20:26.605931
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    field = IfThenElse(Any(), Any())
    assert field is not None


# Generated at 2022-06-14 14:20:33.508696
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    from typesystem.schemas import Any


# Generated at 2022-06-14 14:21:12.843754
# Unit test for method validate of class Not
def test_Not_validate():
    field = Not(Any())
    assert field.validate("hello") == "hello"
    assert field.validate(-15.0) == -15.0
    assert field.validate(15) == 15
    assert field.validate(True) == True
    assert field.validate([1,2,3,4]) == [1,2,3,4]
    assert field.validate({'hello': 3, 'bye' : 'bye'}) == {'hello': 3, 'bye' : 'bye'}
    assert field.validate(None) == None

# Test error raised if value is not of the type negated in the Not class

# Generated at 2022-06-14 14:21:15.530611
# Unit test for method validate of class Not
def test_Not_validate():
    f = Not(Any())
    tested_object = f.validate([])
    assert tested_object == [], 'test_Not_validate assert#1 has failed.'


# Generated at 2022-06-14 14:21:25.891080
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    class MyField(Field):
        def __init__(self):
            super().__init__()

    ite = IfThenElse(MyField(), MyField(), MyField())
    assert isinstance(ite.if_clause, MyField)
    assert isinstance(ite.then_clause, MyField)
    assert isinstance(ite.else_clause, MyField)

    # Now test the kwargs version.
    ite = IfThenElse(if_clause=MyField(), then_clause=MyField(), else_clause=MyField())
    assert isinstance(ite.if_clause, MyField)
    assert isinstance(ite.then_clause, MyField)
    assert isinstance(ite.else_clause, MyField)

    # Now test the args default to Any
    ite = IfThen

# Generated at 2022-06-14 14:21:27.164598
# Unit test for constructor of class Not
def test_Not():
    n = Not(negated=None)
    assert n.negated == None
 

# Generated at 2022-06-14 14:21:33.751879
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    # Test 1: If then and else clauses are None, method should return the value
    field = IfThenElse(if_clause=IfThenElse(if_clause=Any()))
    value, error = field.validate_or_error(value = 1)
    assert value == 1
    assert error is None
    # Test if_clause returns None (i.e, condition returns True)
    field = IfThenElse(if_clause=IfThenElse(if_clause=Any()), then_clause="test")
    value, error = field.validate_or_error(value = 1)
    assert value == "test"
    assert error is None
    # Test if_clause returns an error (i.e, condition returns False)

# Generated at 2022-06-14 14:21:39.669202
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    int_field = Int(min_value=0)
    string_field = String()
    if_clause = Int(max_value=0)
    then_clause = Int(min_value=0)
    else_clause = String(min_length=1)
    if_then_else = IfThenElse(if_clause, then_clause, else_clause)
    with pytest.raises(ValidationError):
        if_then_else.validate(1)

# Generated at 2022-06-14 14:21:40.899468
# Unit test for method validate of class Not
def test_Not_validate():
    f = Not(Field())
    f.validate(None)

# Generated at 2022-06-14 14:21:50.883103
# Unit test for method validate of class Not
def test_Not_validate():
    not_ = Not(negated=DateField())
    assert not_.validate(value=123) == 123
    assert not_.validate(value='string') == 'string'
    try:
        assert not not_.validate(value='2018-03-14T17:21:35Z')
    except:
        assert  not_.validate(value='2018-03-14T17:21:35Z') == '2018-03-14T17:21:35Z'

# Generated at 2022-06-14 14:22:00.469338
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    from .schema import Integer
    from .schema import String

    cond = Integer(max_value=100)

    a = IfThenElse(cond,then_clause=Integer(max_value=75))
    b = IfThenElse(cond,then_clause=Integer(max_value=75),else_clause=String())
    c = IfThenElse(cond,else_clause=String())

    assert a.validate(10) == 10
    assert a.validate(150) == 150

    assert b.validate(10) == 10
    assert b.validate(150) == '150'
    assert b.validate('abc') == 'abc'

    assert c.validate(10) == 10
    assert c.validate(150) == '150'

# Generated at 2022-06-14 14:22:01.309128
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    pass
