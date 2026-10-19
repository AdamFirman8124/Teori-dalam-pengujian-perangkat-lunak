

# Generated at 2022-06-14 14:12:40.001445
# Unit test for method validate of class Not
def test_Not_validate():
    assert Not(Any()).validate(True)


# Generated at 2022-06-14 14:12:49.251595
# Unit test for method validate of class Not
def test_Not_validate():
    # validate is called when the schema is correct.
    negated = Field()
    field = Not(negated=negated)
    value = ''
    strict = False
    assert field.validate(value=value, strict=strict) == value

    # validate throw NotFieldError when the schema is incorrect.
    negated = Field()
    field = Not(negated=negated)
    value = ''
    strict = True
    error = None
    try:
        field.validate(value=value, strict=strict)
    except NotFieldError as e:
        error = e.errors

    assert error == {'negated': 'Must not match.'}


# Generated at 2022-06-14 14:12:51.277375
# Unit test for method validate of class Not
def test_Not_validate():
    not_=Not(AllOf([Negative(0)]))
    assert not_.validate(10)==10
    assert not_.validate(-10)==-10


# Generated at 2022-06-14 14:12:56.269622
# Unit test for method validate of class Not
def test_Not_validate():
    not_field = Not(AllOf([Any(), Any()]))
    assert not_field.validate(1) == 1
    assert not_field.validate(None) == None
    assert not_field.validate("a") == "a"

    not_field = Not(AllOf([Not(Any()), Not(Any())]))
    try:
        not_field.validate("a")
    except Exception:
        return
    raise AssertionError("test failed")
# test_Not_validate()


# Generated at 2022-06-14 14:13:02.403053
# Unit test for constructor of class OneOf
def test_OneOf():
    expected = '''{'errors': {'no_match': 'Did not match any valid type.', 'multiple_matches': 'Matched more than one type.'}, 'one_of': [Field(), Field()], '_required': False, '_default': None, 'name': '', 'description': ''}'''
    obj = OneOf([Field(), Field()])
    assert str(obj) == expected

# Generated at 2022-06-14 14:13:13.226803
# Unit test for method validate of class Not
def test_Not_validate():
    f = Not(Any())
    # first test
    # This will call Any().validate_or_error with value=1 and strict=False
    # So it will call the AbstractField.validate_or_error method which is not
    # implemented so it will return (None, "unknown_error")
    assert f.validate(1) == 1
    # second test
    # This will call Any().validate_or_error with value=1 and strict=True
    # So it will call the AbstractField.validate_or_error method which is not
    # implemented so it will return (None, "unknown_error")
    assert f.validate(1, strict=True) == 1
    # third test
    # This will call Any().validate_or_error with value=1 and strict=True
    # So it will call the Abstract

# Generated at 2022-06-14 14:13:23.305477
# Unit test for constructor of class OneOf
def test_OneOf():
    from typesystem import String, Integer, Float

    class MyField(OneOf):
        def __init__(self, **kwargs: typing.Any) -> None:
            super().__init__(
                [String(), Integer(), Float()], **kwargs)

    assert MyField().validate("foo") == "foo"
    assert MyField().validate(1) == 1
    assert MyField().validate(1.1) == 1.1

    with pytest.raises(MyField.validation_error):
        MyField().validate({})

    with pytest.raises(MyField.validation_error):
        MyField().validate(None)

# Generated at 2022-06-14 14:13:36.506069
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    from typesystem.fields import String, Integer
    from typesystem import Error


# Generated at 2022-06-14 14:13:39.202185
# Unit test for method validate of class Not
def test_Not_validate():
    field = Not(String())
    field.validate("hello")
    try:
        field.validate(1)
        assert False
    except ValidationError as e:
        assert e.error_code == "negated"

# Generated at 2022-06-14 14:13:47.522095
# Unit test for constructor of class OneOf
def test_OneOf():
    schema = OneOf([
        Int(),
        Float()
    ])

    assert schema.validate(1.0) == 1.0
    assert schema.validate(1) == 1
    assert schema.validate(2) == 2

    try:
        schema.validate("abc")
    except:
        pass
    else:
        raise Exception('should have failed')

    try:
        schema.validate(2.2)
    except:
        pass
    else:
        raise Exception('should have failed')


# Generated at 2022-06-14 14:13:59.088595
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    print("Testing OneOf.validate...", end="")
    f = OneOf([Field(label='f1'), Field(label='f2')])
    assert f.validate('a') == 'a'
    try:
        f.validate('b')
        assert False, "TypeError expected"
    except TypeError as e:
        assert isinstance(e, TypeError)
    except:
        assert False, "Wrong exception type"
    print("Passed.")


# Generated at 2022-06-14 14:14:10.571546
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    assert OneOf(one_of=[Any(), NeverMatch()], nullable=True).validate(None) == None
    assert OneOf(one_of=[Any(), NeverMatch()], nullable=True).validate(None, strict=True) == None
    assert OneOf(one_of=[NeverMatch(), Any()], nullable=True).validate(None) == None
    assert OneOf(one_of=[NeverMatch(), Any()], nullable=True).validate(None, strict=True) == None
    assert OneOf(one_of=[Any(), Any()], nullable=True).validate(None) == None
    assert OneOf(one_of=[Any(), Any()], nullable=True).validate(None, strict=True) == None


# Generated at 2022-06-14 14:14:13.018302
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    a = IfThenElse(Any(), Any(), Any())
    with pytest.raises(AssertionError):
        a.validate("test")

# Generated at 2022-06-14 14:14:18.734394
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    ite = IfThenElse(Any())
    if then_clause is Any():
        assert ite.validate(1) == 'true'
    else:
        assert ite.validate(1) == 'false'



# Generated at 2022-06-14 14:14:21.119683
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    f1 = OneOf([int, str])
    f1.validate(1)
    f1.validate('a')


# Generated at 2022-06-14 14:14:30.593366
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    import typesystem
    import pytest

    class Example(typesystem.Schema):
        class Meta:
            title = 'Example of IfThenElse'
            description = 'Example of IfThenElse'

        number = typesystem.Integer(allow_null=True)
        result = typesystem.IfThenElse(if_clause=number>10,
                                       then_clause=number+20,
                                       else_clause=number-20)

    example_schema = Example(strict=False)
    example_schema.validate({'number': 20})
    assert example_schema.validate({'number': 20})=={'number': 20, 'result': 40}
    example_schema.validate({'number': 5})

# Generated at 2022-06-14 14:14:31.888860
# Unit test for constructor of class OneOf
def test_OneOf():
    assert_instance(OneOf([]), Field)


# Generated at 2022-06-14 14:14:39.175493
# Unit test for constructor of class OneOf
def test_OneOf():   
    dict1 = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
    }
    dict2 = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
    }
    dict3 = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
    }
    dict4 = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
    }

# Generated at 2022-06-14 14:14:42.371798
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    a = 1
    b = 2
    assert IfThenElse(a, then_clause = b) == 2
    assert IfThenElse(b, then_clause = a) == 1

# Generated at 2022-06-14 14:14:45.565641
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    field = NeverMatch(name="NeverMatchTest")
    assert field.name == "NeverMatchTest"
    assert field.errors == {"never": "This never validates."}


# Generated at 2022-06-14 14:14:53.057499
# Unit test for constructor of class Not
def test_Not():
    from typesystem.types import String

    notstr = Not(String(), nullable=True)
    assert notstr.validate(0) == 0
    assert notstr.validate("Hello") == "Hello"
    assert notstr.validate("") == ""
    assert notstr.validate(None) == None


# Generated at 2022-06-14 14:14:57.609164
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    # It should return value when error is None
    assert IfThenElse(if_clause = Field()).validate(1) == 1
    # It should return value when error is not None
    assert IfThenElse(if_clause = Field()).validate(2) is None

# Generated at 2022-06-14 14:14:58.395160
# Unit test for constructor of class OneOf
def test_OneOf():
    pass

# Generated at 2022-06-14 14:15:03.333890
# Unit test for constructor of class Not
def test_Not():
    class Person:
        name = types.String(max_length=31)
    assert Person().validate(dict(name='John Doe')) == dict(name='John Doe')
    assert Person().validate(dict(name='John Doe and Jane Doe')) == {'name': ['Must have no more than 31 characters.']}

# Generated at 2022-06-14 14:15:12.523633
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    test_case = {
        "description": ["description", "description", "description"],
        "function_name": "function_name",
        "example": [
            {
                "input": [],
                "output": "output",
                "description": "description"
            },
            {
                "input": None,
                "output": "output",
                "description": "description"
            }
        ]
    }
    if_clause = Field(type_name="anyOf")
    then_clause = Field(type_name="anyOf")
    else_clause = Field(type_name="anyOf")
    test_object = IfThenElse(if_clause, then_clause, else_clause)
    validated = test_object.validate(test_case)

    assert validated == test_case

# Generated at 2022-06-14 14:15:15.405788
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    assert IfThenElse("if_clause", "then_clause").validate("if_clause", strict=False) \
            == "then_clause"

# Generated at 2022-06-14 14:15:26.974542
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    # Setup
    if_clause = Field()
    then_clause = Field()
    else_clause = Field()
    then_clause.validate = mock.Mock(return_value=1)
    else_clause.validate = mock.Mock(return_value=2)
    test_object = IfThenElse(if_clause, then_clause, else_clause)
    test_object.validate_or_error = mock.Mock()

    # Exercise
    test_object.validate(value=0, strict=True)

    # Verify
    then_clause.validate.assert_called_with(value=0, strict=True)

    # Exercise
    test_object.validate(value=0, strict=True)

    # Verify

# Generated at 2022-06-14 14:15:28.909643
# Unit test for constructor of class OneOf
def test_OneOf():
    from . import Number, Text
    field = OneOf(one_of=[Text(), Number()])
    assert field.one_of == [Text(), Number()]


# Generated at 2022-06-14 14:15:29.410501
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    pass

# Generated at 2022-06-14 14:15:32.145262
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    assert getattr(NeverMatch, 'errors')
    assert getattr(NeverMatch, '__init__')
    assert getattr(NeverMatch, 'validate')


# Generated at 2022-06-14 14:15:37.730799
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    field = NeverMatch()


# Generated at 2022-06-14 14:15:40.620632
# Unit test for constructor of class OneOf
def test_OneOf():
    test = OneOf(one_of=[])
    assert test.errors == {"no_match": "Did not match any valid type.", "multiple_matches": "Matched more than one type."}
    assert test.one_of == []

# Generated at 2022-06-14 14:15:46.373965
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    from typesystem.base import Error
    from typesystem import Integer
    from typesystem import String
    from typesystem import schema_validator

    schema = IfThenElse(
        # clause @if
        Integer(minimum=10),
        # clause @then
        String(min_length=5, max_length=5),
        # clause @else
        String(min_length=7, max_length=7)
    )

    # testing if then clause
    value, error = schema.validate_or_error('valid')
    assert value == 'valid'
    assert not isinstance(error, Error)
    value, error = schema.validate_or_error(11, strict=True)
    assert value == '11'
    assert not isinstance(error, Error)

    # testing else clause
    value, error = schema.valid

# Generated at 2022-06-14 14:15:52.185576
# Unit test for constructor of class AllOf
def test_AllOf():
    from tests.fields.test_field import TestField
    from typesystem.fields import Number

    m_all_of = [TestField(required=False), Number(max_value=5, required=False)]
    m_kwargs = {}

    AllOf(all_of=m_all_of, **m_kwargs)


# Generated at 2022-06-14 14:15:56.085694
# Unit test for constructor of class OneOf
def test_OneOf():
    list_field = [1, 2, 3]
    assert OneOf(one_of=list_field).one_of == list_field

    list_field = [1, 2, 3]
    assert OneOf(one_of=list_field, another_field=4).one_of == list_field


# Generated at 2022-06-14 14:15:58.809713
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
  print('Testing NeverMatch')
  m = NeverMatch()
  ok = True

  with pytest.raises(AssertionError):
    n = NeverMatch('useless')

  return ok


# Generated at 2022-06-14 14:16:06.170900
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    assert issubclass(NeverMatch, Field)
    assert NeverMatch.__name__ == 'NeverMatch'
    assert NeverMatch.__module__ == 'typesystem.json_schema'
    assert hasattr(NeverMatch, '__init__')
    assert hasattr(NeverMatch, 'validate')
    # __init__ should not allow any arguments
    try:
        NeverMatch(1)
    except TypeError:
        pass
    else:
        raise AssertionError


# Generated at 2022-06-14 14:16:14.184326
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    # Case 1: check if None is validated
    if_clause = Any()
    then_clause = Any()
    else_clause = Any()

    # Case 1: expected None is validated
    assert IfThenElse(if_clause, then_clause, else_clause).validate(None) is None

    # Case 2: check if None is validated when then is a StringField
    then_clause = String()

    # Case 2: expected None is not validated
    with pytest.raises(ValidationError):
        assert IfThenElse(if_clause, then_clause, else_clause).validate(None) is None

    # Case 3: check if None is validated when then is a StringField
    then_clause = String()
    else_clause = String()

    # Case 3: expected None is

# Generated at 2022-06-14 14:16:16.613078
# Unit test for constructor of class Not
def test_Not():
    not_field = Not(Field(max_length=10))
    assert not_field.negated.max_length == 10



# Generated at 2022-06-14 14:16:20.994431
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    from typesystem.fields import Integer

    ite = IfThenElse(if_clause=Integer(minimum=0, exclusiveMinimum=True),
    then_clause=Integer(minimum=1, exclusiveMinimum=True), else_clause=Integer(minimum=2, exclusiveMinimum=True))
    assert ite.validate(-1) == -1


# Generated at 2022-06-14 14:16:33.138244
# Unit test for constructor of class Not
def test_Not():
    # Create field
    field = Not(
        negated=Field("Hello"),
        errors={"negated":"Must not match"}
    )

    # Assertions
    assert field.negated == Field("Hello")
    assert field.errors == {"negated":"Must not match"}

# Generated at 2022-06-14 14:16:39.878225
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    field = IfThenElse(if_clause=Any(), then_clause=Any(), else_clause=Any())
    assert field.validate('value') == 'value'
    assert field.validate('') == ''
    assert field.validate(None) == None
    assert field.validate(1) == 1
    assert field.validate([]) == []
    assert field.validate({}) == {}



# Generated at 2022-06-14 14:16:43.146899
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    ite = IfThenElse(if_clause=Field(), then_clause=Field(), else_clause=Field())
    assert ite is not None


# Generated at 2022-06-14 14:16:45.064325
# Unit test for constructor of class AllOf
def test_AllOf():
    original_all_of = [Field()]
    AllOf(original_all_of)


# Generated at 2022-06-14 14:16:48.643537
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    field = IfThenElse(if_clause=Any(), then_clause=Any(), else_clause=Any())
    for value in [1, 'a', True]:
        field.validate(value)



# Generated at 2022-06-14 14:16:51.111339
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    assert IfThenElse(1, then_clause=2, else_clause=3).validate(2) == 2
    assert IfThenElse(1, then_clause=2, else_clause=3).validate(4) == 3

# Generated at 2022-06-14 14:16:52.500241
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    return NeverMatch(_description='never match')


# Generated at 2022-06-14 14:16:57.437475
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    fields = [
        {"type":"string", "maxLenght":20},
        {"type":"string", "maxLenght":10},
        {"type":"string", "maxLenght":10},
    ]
    if_then_else = IfThenElse(**fields[0],then_clause=fields[1],else_clause=fields[2],)
    assert if_then_else.then_clause == fields[1]
    assert if_then_else.else_clause == fields[2]
    assert if_then_else.if_clause == fields[0]


# Generated at 2022-06-14 14:16:59.401644
# Unit test for constructor of class OneOf
def test_OneOf():
    OneOf(one_of = [1, 2, 3])

# Generated at 2022-06-14 14:17:06.050248
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    from typesystem.fields import Boolean, Integer

    if_clause = Boolean()
    then_clause = Integer()
    else_clause = Integer()
    field = IfThenElse(if_clause, then_clause, else_clause)
    
    assert field.validate(True) == then_clause.validate(True)
    assert field.validate(False) == else_clause.validate(False)

# Generated at 2022-06-14 14:17:32.851850
# Unit test for constructor of class OneOf
def test_OneOf():
    from .enums import Enum
    from .structures import Integer, Object, String
    from .definitions import Definition, Definitions

    example_choices = [Integer, String, Object]
    example_field = OneOf(example_choices)
    example_definitions = Definitions(
        {"example": Definition(example_field)},
        Enum(
            fields={
                "example": Enum.Field(
                    type=example_field,
                    description="You could use this for validation.",
                )
            }
        ),
    )
    assert example_definitions.example.is_valid(42) == True
    assert example_definitions.example.is_valid("Test") == True
    assert example_definitions.example.is_valid({"Test": "42"}) == True

# Generated at 2022-06-14 14:17:33.861488
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    assert 1 == 1


# Generated at 2022-06-14 14:17:36.983920
# Unit test for constructor of class AllOf
def test_AllOf():
    a=AllOf(0)
    b=AllOf(1)
    c=AllOf(2)
    

# Generated at 2022-06-14 14:17:39.909916
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    obj = NeverMatch(label="Age")
    assert obj._field_name == "Age"
    assert obj.errors == {"never": "This never validates."}
    return


# Generated at 2022-06-14 14:17:45.890494
# Unit test for constructor of class AllOf
def test_AllOf():
    username = AllOf([
        Field(type=str, max_length=200),
        Field(type=str, regex="^[a-zA-Z0-9][a-zA-Z0-9@_\.-]*$"),
    ])
    assert username.validate("admin") == "admin"
    assert username.validate("admin123") == "admin123"

    try:
        username.validate("Admin")
    except:
        pass

    try:
        username.validate("Admin@")
    except:
        pass



# Generated at 2022-06-14 14:17:47.794599
# Unit test for constructor of class OneOf
def test_OneOf():
    field = OneOf([Field(name= "a"), Field()])
    assert field.one_of[0].name.value == "a"
    

# Generated at 2022-06-14 14:17:56.584424
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    from typesystem import Integer

    def test_fonction_IfThenElse(value, strict=False):
        if_clause=Integer()
        then_clause=Integer(minimum=10)
        else_clause=Integer(maximum=5)
        field=IfThenElse(if_clause,then_clause,else_clause)
        return field.validate(value,strict=strict)
       
    assert test_fonction_IfThenElse(2) == 2
    assert test_fonction_IfThenElse(15) == 15

    from typesystem import ValidationError
    from typesystem import String
    from typesystem.exceptions import ValidationError as ValidationError_typesystem
    from typing import Any
    import pytest

# Generated at 2022-06-14 14:17:59.871284
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    t = NeverMatch()
    assert t.label == "NeverMatch"
    assert t.identifier == "never_match"
    assert t.errors == {"never": "This never validates."}



# Generated at 2022-06-14 14:18:06.674288
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    from typesystem.fields import String
    if_clause = String(pattern=r"\d+")
    then_clause = String(pattern=r"a")
    else_clause = String(pattern=r"\d+")
    ifthenelse = IfThenElse(if_clause=if_clause, then_clause=then_clause, else_clause=else_clause)
    assert ifthenelse.validate("123") == "123"

# Generated at 2022-06-14 14:18:08.262627
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    a = IfThenElse(Field(), Field())
    assert a.validate(1) == 1

# Generated at 2022-06-14 14:18:51.521632
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    if_clause = Field()
    then_clause = Field()
    else_clause = Field()
    my_test = IfThenElse(if_clause, then_clause, else_clause)
    assert my_test.if_clause == if_clause
    assert my_test.then_clause == then_clause
    assert my_test.else_clause == else_clause

# Generated at 2022-06-14 14:18:53.400816
# Unit test for constructor of class OneOf
def test_OneOf():
    x = OneOf([1,2,3])
    x.validate(1)


# Generated at 2022-06-14 14:18:54.616427
# Unit test for constructor of class AllOf
def test_AllOf():
    fields = [Field(),Field()]
    try:
        AllOf(fields)
    except AssertionError:
        assert True


# Generated at 2022-06-14 14:19:02.125901
# Unit test for constructor of class AllOf
def test_AllOf():
    from typesystem.fields import Integer, String, Dict

    allof = AllOf([Integer(), String()])

    def f():
        return allof.validate('123')

    assert f() == '123'

    def g():
        return allof.validate({'a': 1})

    assert g() == {'a': 1}

    h = AllOf([Integer(), Dict({'a': Integer()})])

    def t():
        return h.validate({'a': 123})

    assert t() == {'a': 123}


# Generated at 2022-06-14 14:19:03.489311
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    field = NeverMatch()
    assert field.errors == {'never': 'This never validates.'}
    assert field.allow_null == False


# Generated at 2022-06-14 14:19:04.847892
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    assert isinstance(NeverMatch(), NeverMatch)


# Generated at 2022-06-14 14:19:06.060431
# Unit test for constructor of class OneOf
def test_OneOf():
    assert OneOf(one_of=[Any(), Any()]) != None


# Generated at 2022-06-14 14:19:10.104352
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    try:
        tmp = NeverMatch()
    except AttributeError as err:
        assert False, "constructor of NeverMatch raised AttributeError: " + str(err)
        return
    if False:
        tmp = NeverMatch()


# Generated at 2022-06-14 14:19:13.346670
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    field = IfThenElse(if_clause=Any(), then_clause=None, else_clause=None)
    field.validate('A valid value')
    return True

# Generated at 2022-06-14 14:19:15.170269
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    assert type(IfThenElse(Any(), Any())) is IfThenElse

# Generated at 2022-06-14 14:20:22.970401
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():

    class ThenClause(Field):
        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            return "then"

    class ElseClause(Field):
        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            return "else"

    class IfClause(Field):
        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            raise self.validation_error("no_match")

    then = ThenClause()
    else_ = ElseClause()
    if_ = IfClause()

    test_if_then_else = IfThenElse(if_,then,else_)
    assert test_if_then_else.validate(1) == "else"

# Generated at 2022-06-14 14:20:27.401104
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    my_else_clause = Any()
    my_then_clause = Any()
    my_if_clause = Any()
    my_ite = IfThenElse(my_if_clause, my_then_clause, my_else_clause)
    assert my_ite.validate(None) is None


# Generated at 2022-06-14 14:20:29.048421
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    """
    TestCase for constructor of class NeverMatch
    """
    pass


# Generated at 2022-06-14 14:20:40.145552
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    class X(Field):
        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            return value
    f = IfThenElse(X(), then_clause=X(), else_clause=X())
    validate_v_calls = []
    validate_c_calls = []
    class Y(Field):
        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            validate_v_calls.append(1)
            return value
    class Z(Field):
        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            validate_c_calls.append(1)
            return value
    f.if_clause = Y()
    f.then_clause = Z()
    f

# Generated at 2022-06-14 14:20:44.771568
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    cond = Field(min_length=3, max_length=5)
    then = Field(format="email")
    elze = Field(format="url")
    field = IfThenElse(cond, then, elze)
    value = "hey@dummy.com"
    try:
        field.validate(value)
        assert False
    except FieldValidationError as err:
        assert err.field == field
        assert err.code == "format_email"
        assert err.value == "hey@dummy.com"
    value = "https://heydummy.com"
    try:
        field.validate(value)
        assert False
    except FieldValidationError as err:
        assert err.field == field
        assert err.code == "min_length"

# Generated at 2022-06-14 14:20:54.300273
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    class Example:
        value = Field(str)

    class ExampleElse:
        value = Field(int)

    class ExampleElseElse:
        value = Field(float)

    test_data = [
        ('hello', Example, ExampleElse, ExampleElseElse),
        (5, ExampleElse, Example, ExampleElseElse),
        (5.5, ExampleElseElse, ExampleElse, Example),
    ]

    for item in test_data:
        if_value, if_class, then_class, else_class = item
        ite = IfThenElse(
            if_clause=if_class,
            then_clause=then_class,
            else_clause=else_class
        )
        assert if_value == ite.validate(if_value)


# Generated at 2022-06-14 14:21:03.766102
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():

    # check if validate function returns correct value for condition True
    if_clause = Field(type="number")
    then_clause = Field(type="number", min_value=3)
    else_clause = Field(type="number", max_value=2)

    assert IfThenElse(if_clause, then_clause, else_clause).validate(2) == 2
    assert IfThenElse(if_clause, then_clause, else_clause).validate(4) == 4

    # check if validate function returns correct value for condition False
    if_clause = Field(type="string")
    then_clause = Field(type="number", min_value=3)
    else_clause = Field(type="number", max_value=2)


# Generated at 2022-06-14 14:21:04.735601
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    f = NeverMatch()


# Generated at 2022-06-14 14:21:09.588174
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    if_clause = Field(required=True)
    then_clause = Field(required=True)
    else_clause = Field(required=True)
    field = IfThenElse(if_clause, then_clause, else_clause)
    assert field.validate(value=True, strict=True) == True
    assert field.validate(value=False, strict=True) == False

# Generated at 2022-06-14 14:21:10.526651
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    assert IfThenElse(field1).validate([0]) == [0]

