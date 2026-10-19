

# Generated at 2022-06-14 14:12:41.026195
# Unit test for method validate of class Not
def test_Not_validate():
    field = Not(
        String(),
        description="test",
    )

    assert field.validate("123") == "123"


# Generated at 2022-06-14 14:12:51.052169
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    from typesystem import Integer, String

    if_clause = Integer(minimum=0)
    then_clause = String()
    else_clause = Integer()

    test_ifthenelse1 = IfThenElse(if_clause, then_clause, else_clause)
    result1, error1 = IfThenElse.validate_or_error(test_ifthenelse1, 1)
    result2, error2 = IfThenElse.validate_or_error(test_ifthenelse1, "test")
    result3, error3 = IfThenElse.validate_or_error(test_ifthenelse1, -1)

    assert result1 == 1
    assert result2 == "test"
    assert result3 == -1

# Generated at 2022-06-14 14:12:52.035055
# Unit test for constructor of class AllOf
def test_AllOf():
    f = AllOf([])
    assert f.all_of == []


# Generated at 2022-06-14 14:12:56.403022
# Unit test for constructor of class OneOf
def test_OneOf():
    with pytest.raises(AssertionError):
        OneOf(1, allow_null=True)
        OneOf("a", allow_null=False)
    assert OneOf("b", allow_null=True).allow_null == True


# Generated at 2022-06-14 14:12:57.544299
# Unit test for constructor of class AllOf
def test_AllOf():
    AllOf()


# Generated at 2022-06-14 14:13:02.296044
# Unit test for constructor of class AllOf
def test_AllOf():
    # Test for initialization of class AllOf
    item1 = AllOf(['a'])
    # Test for ValueError raised by mismatched types in AllOf
    try:
        item2 = AllOf(3)
    except ValueError as e:
        assert type(e) == ValueError


# Generated at 2022-06-14 14:13:06.750016
# Unit test for constructor of class Not
def test_Not():
    import pytest
    from typesystem.fields import String

    field = Not(String())
    assert field.negated == String()

    with pytest.raises(AssertionError):
        Not(String(), allow_null=False)



# Generated at 2022-06-14 14:13:16.543090
# Unit test for method validate of class Not
def test_Not_validate():
    """
    unit test for method validate of class Not
    """
    from typesystem.fields import Integer

    field = Not(Integer())
    # Testing without error
    field.validate(0)
    field.validate("0")
    field.validate(1)
    field.validate("1")
    field.validate(10)
    field.validate("10")
    field.validate(100)
    field.validate("100")
    # Testing with error
    try:
        field.validate("")
    except Exception as e:
        assert type(e) is field.validation_error
    try:
        field.validate("a")
    except Exception as e:
        assert type(e) is field.validation_error

# Generated at 2022-06-14 14:13:19.056562
# Unit test for method validate of class Not
def test_Not_validate():
    # Given
    field = Not(Any())

    # When
    result = field.validate(None)

    # Then
    assert result == None



# Generated at 2022-06-14 14:13:26.916379
# Unit test for method validate of class Not
def test_Not_validate():
    data = {"must_be_null": None, "must_be_int": 1, "must_be_str": "hello"}
    field = Not(IsInt)
    result = field.validate(data["must_be_null"])
    assert result == data["must_be_null"]
    result = field.validate(data["must_be_int"])
    assert result == data["must_be_int"]
    result = field.validate(data["must_be_str"])
    assert result == data["must_be_str"]

# Generated at 2022-06-14 14:13:36.050304
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    one_of = OneOf([Int(), Str()])
    s = "a"
    try:
        one_of.validate(1)
        one_of.validate([1])
        one_of.validate(s)
    except Exception as e:
        print(e)
        assert False


# Generated at 2022-06-14 14:13:38.285528
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    print ("test OneOf.validate")
    value = 'Hello'
    field = OneOf([String()])
    field.validate(value)


# Generated at 2022-06-14 14:13:42.300147
# Unit test for method validate of class Not
def test_Not_validate():
    not_test = Not(String())
    assert not_test.validate(1) == 1, "Invalid input test failed"
    assert not_test.validate("Hello") == "Hello", "Invalid input test failed"



# Generated at 2022-06-14 14:13:53.238948
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    def test_if(value):
        return value == 'condition'

    def test_then(value):
        if value != 'then':
            raise Exception()

    def test_else(value):
        if value != 'else':
            raise Exception()

    field = IfThenElse(Field(validate=test_if), Field(validate=test_then))
    field.validate('condition')

    field = IfThenElse(Field(validate=test_if), else_clause=Field(validate=test_else))
    field.validate('else')

    field = IfThenElse(Field(validate=test_if), Field(validate=test_then), Field(validate=test_else))
    field.validate('else')


# Generated at 2022-06-14 14:14:00.421797
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    test = Field(name = "test")
    assert str(test) == "test"
    assert repr(test) == "test"
    assert type(test) is Field
    assert test.name == "test"
    assert test.label is None
    assert test.description is None
    assert test.default is None
    assert test.required is True
    assert test.strict is False
    
    test = Field(name = "test", label = "Test")
    assert str(test) == "test"
    assert repr(test) == "test"
    assert type(test) is Field
    assert test.name == "test"
    assert test.label == "Test"
    assert test.description is None
    assert test.default is None
    assert test.required is True
    assert test.strict is False
    
    test

# Generated at 2022-06-14 14:14:07.287296
# Unit test for constructor of class OneOf
def test_OneOf():
    class MyClass:
        def __init__(self, b: typing.Any, c: typing.Any, d: typing.Any) -> None:
            super().__init__()
            self.a = None
            self.b = b
            self.c = c
            self.d = d


    f = Field()

    one_of = OneOf(one_of=[f, ])
    assert one_of


# Generated at 2022-06-14 14:14:11.766758
# Unit test for method validate of class Not
def test_Not_validate():
    from typesystem.exceptions import ValidationError
    from typesystem.integer import Integer
    n = Not(Integer())
    n.validate(2)
    try:
        n.validate(3)
        raise Exception("ValidationError")
    except ValidationError as e:
        assert e.code == "negated"


# Generated at 2022-06-14 14:14:19.717241
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    a = String(max_length=50)
    b = String(max_length=50)
    c = String(max_length=50)
    ifThenElse = IfThenElse(a, b, c)
    assert ifThenElse.if_clause == a
    assert ifThenElse.then_clause == b
    assert ifThenElse.else_clause == c


# Generated at 2022-06-14 14:14:22.504559
# Unit test for constructor of class OneOf
def test_OneOf():
    from typesystem.fields import Boolean, Integer
    field = OneOf([Integer(), Boolean()])
    assert field.one_of == [Integer(), Boolean()]


# Generated at 2022-06-14 14:14:23.966073
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    obj = NeverMatch()
    assert obj is not None


# Generated at 2022-06-14 14:14:32.424497
# Unit test for method validate of class Not
def test_Not_validate():
  errors = None
  prop_to_check = None
  n = Not(String(max_length=3), allow_null=True)
  res, errors = n.validate_or_error("123")
  assert res == "123"

  res, errors = n.validate_or_error(123)
  assert res == ""
  assert errors == [{'code': 'negated', 'message': 'Must not match.', 'path': ''}]


# Generated at 2022-06-14 14:14:34.674278
# Unit test for constructor of class Not
def test_Not():
    a = Not(Float())
    b = Not(Integer())
    c = Not(Float())

    assert a != b
    assert a == c



# Generated at 2022-06-14 14:14:36.655073
# Unit test for method validate of class Not
def test_Not_validate():
    negated = Not(Any())
    candidate = 'candidate'
    error = negated.validate(candidate)
    assert error == candidate


# Generated at 2022-06-14 14:14:41.000903
# Unit test for constructor of class OneOf
def test_OneOf():
    success = False
    try:
        x = OneOf(one_of=['x'])
    except AssertionError:
        success = True
    assert success


# Generated at 2022-06-14 14:14:41.801396
# Unit test for constructor of class Not
def test_Not():
    assert Not

# Generated at 2022-06-14 14:14:49.719144
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    from typesystem import Integer, String, Boolean
    from typesystem import Invalid
    f = IfThenElse(
        if_clause = Boolean(),
        then_clause = Integer(),
        else_clause = String()
    )
    assert f.validate(True) == 0
    assert f.validate(False) == ''
    try:
        f.validate(0)
    except Invalid as e:
        assert str(e) == 'if_clause: Was not True or False.'
    else:
        raise AssertionError
test_IfThenElse_validate()


# Generated at 2022-06-14 14:14:50.305520
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    pass

# Generated at 2022-06-14 14:14:59.486885
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    from typesystem.exceptions import ValidationError
    import typesystem
    import pytest

    a: typesystem.Field = typesystem.Field(name="a")
    b: typesystem.Field = typesystem.Field(name="b")
    c: typesystem.Field = typesystem.Field(name="c")
    ifThenElse = IfThenElse(if_clause=a, then_clause=b, else_clause=c)
    assert ifThenElse.validate(0) == 0
    with pytest.raises(ValidationError):
        ifThenElse.validate("error")

# Generated at 2022-06-14 14:15:06.298757
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    if_clause = Any()
    then_clause = Any()
    else_clause = Any()
    number_clause = Any()
    x = 2
    y = 4
    z = 4
    object1 = IfThenElse(if_clause, then_clause, else_clause)
    object1.validate(x)
    object1.validate(y)
    object1.validate(z)


# Generated at 2022-06-14 14:15:10.402867
# Unit test for constructor of class AllOf
def test_AllOf():
    all_of = [Field(), Field()]
    all_of_obj = AllOf(all_of)
    assert all_of_obj.all_of == all_of
    assert all_of_obj.required == False
    assert all_of_obj.allow_null == False
    assert 'all_of' in all_of_obj.__dict__

# Generated at 2022-06-14 14:15:15.252562
# Unit test for method validate of class Not
def test_Not_validate():
    my_not_field = Not(String())
    not_result = my_not_field.validate("invalid")
    assert not_result is not None

# Generated at 2022-06-14 14:15:18.012400
# Unit test for constructor of class OneOf
def test_OneOf():
    one_of = OneOf([Field()])
    assert one_of.one_of == [Field()]


# Generated at 2022-06-14 14:15:24.605248
# Unit test for method validate of class Not
def test_Not_validate():
    class A(Field):
        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            return None

    a = Not(A())

    value1 = 1
    value2 = None
    strict = False
    result1 = a.validate(value1, strict)
    result2 = a.validate(value2, strict)

    assert result1 == value1
    assert result2 == value2



# Generated at 2022-06-14 14:15:27.567612
# Unit test for constructor of class Not
def test_Not():
    not_test = Not(None)
    assert not_test.negated == None
    assert not_test.errors == {"negated": "Must not match."}
    
    

# Generated at 2022-06-14 14:15:29.238278
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    test = OneOf([Field(type=bool),Field(type=int)])
    assert test.validate(1) == 1


# Generated at 2022-06-14 14:15:33.169387
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    # Test case 1
    # Testing two cases: there is one match, and multiple matches
    items = [Integer(min_value=4), String()]
    one = OneOf(items)
    if isinstance(6, int):
        assert one.validate(6) == 6
    try:
        one.validate("cat")
    except Exception:
        assert True

# Generated at 2022-06-14 14:15:34.751368
# Unit test for constructor of class OneOf
def test_OneOf():
    with pytest.raises(AssertionError):
        field = OneOf(String(), allow_null=True)

# Generated at 2022-06-14 14:15:38.683671
# Unit test for method validate of class Not
def test_Not_validate():
    field = Not(negated=Field())
    result, error = field.validate_or_error(None)
    assert result is not None
    assert error is None


# Generated at 2022-06-14 14:15:43.925384
# Unit test for method validate of class Not
def test_Not_validate():
    my_object = Not(
        OneOf([
            Integer(min_value=1),
            String(min_length=1),
        ])
    )

    for value in [1, 1.1, True, False, "str", "", None]:
        try:
            my_object.validate(value, strict=True)
            raise Exception("Should have raised")
        except ValidationError as error:
            assert error.messages == {"negated": "Must not match."}

    for value in [2, True, False, "abc", None]:
        assert my_object.validate(value, strict=True) == value



# Generated at 2022-06-14 14:15:51.586767
# Unit test for constructor of class OneOf
def test_OneOf():
    assert OneOf(one_of = [int, float]).validate(1) == 1
    assert OneOf(one_of = [int, float]).validate(1.0) == 1.0
    assert OneOf(one_of = [int, float]).errors['no_match'] == "Did not match any valid type."
    assert OneOf(one_of = [int, float]).errors['multiple_matches'] == "Matched more than one type."


# Generated at 2022-06-14 14:15:55.965416
# Unit test for constructor of class OneOf
def test_OneOf():
    from . import fields

    d = fields.OneOf([fields.Integer(), fields.String()])
    assert d.one_of == [fields.Integer(), fields.String()]

# Generated at 2022-06-14 14:16:02.759634
# Unit test for constructor of class OneOf
def test_OneOf():
	# Test 1: nominal case
	test1 = OneOf([Field()])

	# Test 2: one_of must be a list
	try:
		test2 = OneOf(Field())
	except:
		pass
	else:
		print("Fail: Test 2")

	# Test 3: Test with string
	try:
		test3 = OneOf("")
	except:
		pass
	else:
		print("Fail: Test 3")

	# Test 4: Test with integer
	try:
		test4 = OneOf(0)
	except:
		pass
	else:
		print("Fail: Test 4")

	# Test 5: Test with dictionary
	try:
		test5 = OneOf({})
	except:
		pass

# Generated at 2022-06-14 14:16:12.364167
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    import pytest

    assert "test_IfThenElse_validate"


# Generated at 2022-06-14 14:16:13.829387
# Unit test for method validate of class Not
def test_Not_validate():
    field = Not(Float())
    value = "1"
    field.validate(value)
    return True



# Generated at 2022-06-14 14:16:23.005840
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    class Int(Field):
        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            return int(value)
    class Str(Field):
        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            return str(value)
    if_clause = Int()
    then_clause = Str()
    else_clause = Str()
    ite = IfThenElse(if_clause, then_clause, else_clause)
    assert ite.validate("1") == 1
    assert ite.validate("a") == "a"
    assert ite.validate("1") == 1
    assert ite.validate("a") == "a"
    assert ite.validate(1) == 1
    assert it

# Generated at 2022-06-14 14:16:24.585989
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    from typesystem import String

    schema = OneOf([String(""), String("")])
    assert schema.validate("") == ""


test_OneOf_validate()

# Generated at 2022-06-14 14:16:29.491247
# Unit test for method validate of class Not
def test_Not_validate():
    # Test with a negative value
    child = Not(Any())

    result = child.validate(None)
    assert result is None

    # Test with a positive value
    child = Not(Any())
    with pytest.raises(child.validation_error) as excinfo:
        child.validate(1)
    assert 'Must not match' in str(excinfo.value)

# Generated at 2022-06-14 14:16:34.261733
# Unit test for constructor of class AllOf
def test_AllOf():
    # Arrange
    ALLOF_CLASS = AllOf
    class_name = 'TestClass'
    class_doc = 'Test Class'
    
    # Act
    all_of = ALLOF_CLASS([class_doc])
    all_of.name = class_name

    # Assert
    assert all_of.name == class_name
    assert all_of.all_of[0] == class_doc


# Generated at 2022-06-14 14:16:36.400273
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    list_ = ['as',3]
    number_ = 3
    assert OneOf(list_).validate(3) == 3


# Generated at 2022-06-14 14:16:37.871621
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    assert OneOf(None).validate(None) == None

# Generated at 2022-06-14 14:16:45.482767
# Unit test for method validate of class Not
def test_Not_validate():
    field = Not(Integer())
    field.validate(1)
    try:
        field.validate(3.14)
        assert False
    except Exception:
        assert True


# Generated at 2022-06-14 14:16:46.524051
# Unit test for constructor of class OneOf
def test_OneOf():
    assert OneOf(one_of = "String")

# Generated at 2022-06-14 14:16:55.668574
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    from typesystem import Schema, Array
    from typesystem.errors import ValidationError

    class Person(Schema):
        name = Array(items=["Petya", "Vasya", "Dima"])

    p = Person()

    try:
        p.validate({"name": ["Vasya", "Dima"]})
    except ValidationError as e:
        assert str(e) == "Must be 1 item(s), not 2."

    try:
        p.validate({"name": ["Petya", "Dima"]})
    except ValidationError as e:
        assert str(e) == "Must be 1 item(s), not 2."

    try:
        p.validate({"name": ["Vasya", "Petya"]})
    except ValidationError as e:
        assert str

# Generated at 2022-06-14 14:17:07.656799
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    # case
    one_of_data = [
        "not_match",
        "match",
        "also_not_match",
    ]
    one_of_type = [
        String(),
        String(),
        String(),
    ]
    oof = OneOf(one_of_type)
    oof.validate(one_of_data[0])

    # case
    try:
        one_of_data = [
            "not_match",
            "match",
            "match",
        ]
        one_of_type = [
            String(),
            String(),
            String(),
        ]
        oof = OneOf(one_of_type)
        oof.validate(one_of_data[0])
    except:
        assert True
    else:
        assert False

   

# Generated at 2022-06-14 14:17:17.579113
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    value, error = OneOf([
        Field(key="a"),
        Field(key="b"),
    ]).validate_or_error({"a": "A"})
    assert error is None
    assert value == {"a": "A"}

    value, error = OneOf([
        Field(key="a"),
        Field(key="b"),
    ]).validate_or_error({"a": "A", "b": "B"})
    assert error == {"type": "multiple_matches"}
    assert value == {"a": "A", "b": "B"}

    value, error = OneOf([
        Field(key="a"),
        Field(key="b"),
    ]).validate_or_error({"c": "A", "d": "B"})

# Generated at 2022-06-14 14:17:27.035603
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    assert OneOf(one_of=[String()]).validate("foo") == "foo"
    with pytest.raises(FieldValidationError) as excinfo:
        OneOf(one_of=[String()]).validate(123)
    assert str(excinfo.value) == "Did not match any valid type."
    with pytest.raises(FieldValidationError) as excinfo:
        OneOf(one_of=[String(min_length=10), String()]).validate("foo")
    assert str(excinfo.value) == "Matched more than one type."


# Generated at 2022-06-14 14:17:33.080714
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    from typesystem.field import String
    from typesystem.field import Integer
    from typesystem.errors import ValidationError
    from typesystem.validators import one_of
    from typesystem.utils import filter_empty_value

    field = OneOf([String(), Integer()])

    assert field.validate(1) == 1

    assert field.validate(1.1) == 1.1

    assert field.validate('a') == 'a'

    error = None

# Generated at 2022-06-14 14:17:36.613319
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    test_field = NeverMatch()
    assert test_field.__dict__ == {'errors': {'never': 'This never validates.'}, 'required': False}


# Generated at 2022-06-14 14:17:39.182541
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    field = OneOf([String(),Number()])
    assert field.validate(123) == 123
    assert field.validate("123") == "123"

# Generated at 2022-06-14 14:17:41.913900
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    field = IfThenElse(if_clause='', then_clause='', else_clause='')
    assert field.validate(value='') == None

# Generated at 2022-06-14 14:17:52.882355
# Unit test for method validate of class Not
def test_Not_validate():
    schema = Not(String())
    schema.validate('test')
    try:
        schema.validate('hello')
        assert False, 'Negation operator failed!'
    except:
        pass


# Generated at 2022-06-14 14:17:59.734252
# Unit test for method validate of class OneOf
def test_OneOf_validate():

    # variable to store the count of tests
    test_number = 0

    # test if the array of fields is empty
    schema = OneOf(fields=[])
    error = None
    result = None
    
    try:
        result = schema.validate(12)
    except Exception as err:
        error = err
    test_number += 1
    assert result == None
    assert error.args[0] == "No fields were specified."

    # test if all the fields match the value
    schema = OneOf(fields=[Integer(), Float()])
    error = None
    result = None
    
    try:
        result = schema.validate(12.0)
    except Exception as err:
        error = err

    test_number += 1
    assert result == 12.0
    assert error == None

    # test if no field

# Generated at 2022-06-14 14:18:09.784812
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    # arrange
    if_clause = Field()
    # return_value, error
    if_clause.validate_or_error = mock.MagicMock(return_value=(1, 2))
    then_clause = Field()
    then_clause.validate = mock.MagicMock(return_value=9)
    else_clause = Field()
    else_clause.validate = mock.MagicMock(return_value=10)
    sut = IfThenElse(if_clause, then_clause, else_clause)
    # act
    result = sut.validate(3)
    # assert
    if_clause.validate_or_error.assert_called_once_with(3)
    then_clause.validate.assert_called_once_with(3)


# Generated at 2022-06-14 14:18:17.351086
# Unit test for method validate of class Not
def test_Not_validate():
    then_clause = Any()
    assert then_clause.validate(1) == 1
    assert then_clause.validate(True) == True
    assert then_clause.validate(None) == None
    assert then_clause.validate('aa') == 'aa'
    assert then_clause.validate('True') == 'True'
    obj = Not(then_clause)
    _, error = obj.validate_or_error(None)
    assert error == None
    print ("validate ok")


# Generated at 2022-06-14 14:18:28.131503
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    # Test for OneOf with invalid value
    number_field = Field()

    string_field = Field()
    string_field.validators = [str]

    one_of_field = OneOf([number_field, string_field], name='OneOf')
    one_of_field.validate({'hello': 'ewr'})
    assert one_of_field.validation_error('no_match') == 'Did not match any valid type.'
    # Test for OneOf with valid value
    try:
        one_of_field.validate(1)
    except Exception:
        assert False
    assert not one_of_field.validation_error('no_match')
    # Test for OneOf with multiple value
    invalid_string_field = Field()


# Generated at 2022-06-14 14:18:32.111616
# Unit test for constructor of class OneOf
def test_OneOf():
    foo1 = OneOf([Any()])
    assert foo1
    foo2 = OneOf([])
    assert not foo2
    dou = Field()

    foo3 = OneOf([Any(), dou])
    assert foo3
    foo4 = OneOf([dou, dou])
    assert foo4
    foo5 = OneOf([dou, Any()])
    
test_OneOf()

# Generated at 2022-06-14 14:18:35.156332
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    pass
    # You can write test for method validate of class OneOf here
    OneOf([])
    # Some code here



# Generated at 2022-06-14 14:18:37.565172
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    field = IfThenElse(if_clause=NeverMatch())
    assert field.validate(123) == 123


# Generated at 2022-06-14 14:18:39.430463
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    # check class constructor
    instance = NeverMatch()
    assert instance is None


# Generated at 2022-06-14 14:18:41.815132
# Unit test for constructor of class Not
def test_Not():
    not_field = Not(negated=Field())
    assert not_field.negated == Field()
    assert not_field.errors == {}


# Generated at 2022-06-14 14:18:51.587868
# Unit test for constructor of class Not
def test_Not():
    f = Not(String())
    assert f.negated == String()

# Generated at 2022-06-14 14:18:52.192880
# Unit test for constructor of class OneOf
def test_OneOf():
    pass

# Generated at 2022-06-14 14:18:55.229307
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    field = OneOf([Boolean(), Integer()], name=None, required=False)
    assert field.validate(None, False) == None
    assert field.validate(False, False) == False

# Generated at 2022-06-14 14:18:58.614653
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    from typesystem import Object, String

    schema = Object(properties={"foo": OneOf([String(), Boolean()])})
    assert schema.validate({"foo": True}) == {"foo": True}
    assert schema.validate({"foo": "bar"}) == {"foo": "bar"}

# Generated at 2022-06-14 14:19:08.940102
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    # Define a list of fields containing all types of fields
    one_of = [Field(), Null(Field()), Str(), Null(Str()), Union(Field(), Str()), Null(Union(Field(), Str()))]
    # Check that validate raises a ValidationError with "no_match" as message when value doesn't match any of the
    # sub-items
    f = OneOf(one_of)
    with pytest.raises(Field.ValidationError) as err:
        f.validate(1)
        assert err.value.message == "no_match"
    # Check that validate raises a ValidationError with "multiple_matches" as message when value matches more than one
    # sub-items
    f = OneOf(one_of)

# Generated at 2022-06-14 14:19:10.155680
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    a = NeverMatch()
    assert a


# Generated at 2022-06-14 14:19:16.946995
# Unit test for constructor of class OneOf
def test_OneOf():
    # test null/empty params in constructor
    try:
        OneOf()
    except Exception as e:
        assert type(e) == TypeError
    
    #test invalid type in param
    try:
        OneOf(one_of='all')
    except Exception as e:
        assert type(e) == TypeError

    # test correct param
    assert OneOf(one_of=['all']).one_of == ['all']

# Generated at 2022-06-14 14:19:18.260518
# Unit test for constructor of class AllOf
def test_AllOf():
    field = AllOf([])
    assert field.all_of == []


# Generated at 2022-06-14 14:19:19.734467
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    # method is private, no test
    pass


# Generated at 2022-06-14 14:19:23.911855
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    import pytest
    from typesystem.fields import Integer

    field = IfThenElse(Integer(min_value=0))
    assert field.validate(1) == 1
    with pytest.raises(field.validation_error):
        field.validate(0)
    assert field.validate(None) == None



# Generated at 2022-06-14 14:19:43.644825
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    from typesystem.fields import Boolean

    field = OneOf([Boolean(), Boolean()])
    assert field.validate(True) is True
    assert field.validate(False) is False
    try:
        field.validate(1)
    except Exception as ex:
        assert str(ex) == 'Did not match any valid type.'


# Generated at 2022-06-14 14:19:46.561453
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    a = NeverMatch()
    val, err = a.validate_or_error(True)
    assert err != None
    assert err == {'never': 'This never validates.'}
    assert val == undefined


# Generated at 2022-06-14 14:19:47.830096
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    data = NeverMatch()


# Generated at 2022-06-14 14:19:49.974250
# Unit test for constructor of class OneOf
def test_OneOf():
    assert OneOf(one_of = [1,2,3]) is not None


# Generated at 2022-06-14 14:19:52.630251
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    Foo = OneOf([OneOf([])])
    Foo = Foo()
    Foo.validate(1)

# Generated at 2022-06-14 14:19:54.606291
# Unit test for method validate of class Not
def test_Not_validate():
    c = Not(negated=None)
    assert c.validate(None) is None
    try:
        c.validate("str")
    except Exception as e:
        assert e.args[0] == "Must not match."
        return
    assert False



# Generated at 2022-06-14 14:19:56.051398
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    ne = NeverMatch()
    assert ne


# Generated at 2022-06-14 14:20:02.844566
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    from typesystem.exceptions import ValidationError
    from typesystem import String

    one_of_validate = OneOf(one_of=[String(max_length=1), String(max_length=3)])

    # Success case
    assert one_of_validate.validate("my_string", strict=False) == "my_string"
    
    try:
        # Failure case
        one_of_validate.validate("my_string", strict=False)
    except ValidationError as e:
        assert e.code == "multiple_matches"


# Generated at 2022-06-14 14:20:06.340989
# Unit test for method validate of class Not
def test_Not_validate():
    # should pass
    field = Not(Any())
    assert field.validate(None) == None

    # should raise error
    field = Not(Number())
    try:
        field.validate(None)
        assert False
    except FieldValidationError as e:
        assert True

# Generated at 2022-06-14 14:20:06.863763
# Unit test for constructor of class Not
def test_Not():
    assert True

# Generated at 2022-06-14 14:20:22.124124
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    from typesystem.fields import NeverMatch
    NeverMatch(description="test")



# Generated at 2022-06-14 14:20:26.182171
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    f = NeverMatch(error_messages={"never": "This {} never validates."})
    assert isinstance(f, NeverMatch)
    assert f.errors['never'] == "This {} never validates."
    assert f.repr_value() == "never"


# Generated at 2022-06-14 14:20:30.594960
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    class A:
        pass
    a = A()
    a.validate_or_error = lambda a, b: (True, None)
    b = A()
    b.validate_or_error = lambda a, b: (False, 'a')
    o = OneOf(one_of=[a, b])
    o.validate(1)
    raise Exception('Test failed')

# Generated at 2022-06-14 14:20:41.349277
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    # test object instantiation of class OneOf
    f1 = Field()
    list_f = [f1]
    instance = OneOf(list_f)
    assert instance.one_of == list_f
    # test error raise in case of wrong key
    f2 = Field()
    value_f2 = "test_string"
    with pytest.raises(ValidationError) as v_error:
        instance.validate(f2, value_f2, False)
    assert v_error.value.code == "never" and v_error.value.message == "This never validates."
    # test error raise in case of wrong key and multiple matches
    f2 = Field()
    value_f2 = "test_string"
    list_f = [f1,f2]

# Generated at 2022-06-14 14:20:42.340520
# Unit test for constructor of class OneOf
def test_OneOf():
    obj = OneOf([])

# Generated at 2022-06-14 14:20:47.499931
# Unit test for constructor of class OneOf
def test_OneOf():
    field = OneOf([])
    assert field.errors == {
        "no_match": "Did not match any valid type.",
        "multiple_matches": "Matched more than one type.",
    }

    field = OneOf([String()])
    assert field.validate("hello") == "hello"
    assert field.validate(None) == "None"


# Generated at 2022-06-14 14:20:49.096379
# Unit test for constructor of class OneOf
def test_OneOf():
    t = OneOf(one_of=[str])
    t.validate("aa")


# Generated at 2022-06-14 14:20:51.332939
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    with pytest.raises(AssertionError):
        NeverMatch(allow_null=False)


# Generated at 2022-06-14 14:20:53.352353
# Unit test for constructor of class AllOf
def test_AllOf():
    f = AllOf([Field(name="name",required=True),Field(name="age",required=False)])
    assert f.name == None
    assert f.required == False



# Generated at 2022-06-14 14:20:54.918130
# Unit test for method validate of class Not
def test_Not_validate():
    print("Test for Not method validate")
    field = Not(negated=Field.const(5))
    assert field.validate(5) == 5
    assert field.validate(1) == 1



# Generated at 2022-06-14 14:21:10.844423
# Unit test for method validate of class Not
def test_Not_validate():
    not1 = Not(number)
    not1.validate(1.0)
    # 'number' is the smallest valid float data type
    assert number.validate(1.0) == 1.0, 'validate(1.0) is failed'

# Generated at 2022-06-14 14:21:11.717015
# Unit test for constructor of class AllOf
def test_AllOf():
    AllOf(all_of=[int])



# Generated at 2022-06-14 14:21:14.544322
# Unit test for constructor of class OneOf
def test_OneOf():
    one_of = OneOf([int, str, typing.List[int]])
    one_of.validate([0, 1, 2])


# Generated at 2022-06-14 14:21:15.709235
# Unit test for constructor of class AllOf
def test_AllOf():
    foo = AllOf([])
    assert foo is not None


# Generated at 2022-06-14 14:21:19.047322
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    ite = IfThenElse(if_clause=String(), then_clause=Integer())
    assert ite.if_clause != None
    assert ite.then_clause != None
    assert ite.else_clause != None

# Generated at 2022-06-14 14:21:20.536064
# Unit test for constructor of class OneOf
def test_OneOf():
    instance = OneOf(one_of=[Field])


# Generated at 2022-06-14 14:21:24.151233
# Unit test for method validate of class Not
def test_Not_validate():
    f = Not(negated=String())
    assert f.validate('abc') == 'abc'

    try:
        f.validate('')
    except Exception as e:
        assert e.validation_errors == {'negated': 'Must not match.'}


# Generated at 2022-06-14 14:21:25.994769
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    nm = NeverMatch()
    return nm


# Generated at 2022-06-14 14:21:26.612690
# Unit test for method validate of class Not
def test_Not_validate():
  pass

# Generated at 2022-06-14 14:21:30.410018
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    try:
        x = NeverMatch()
        print("Constructed a NeverMatch")
    except AssertionError:
        pass
    try: 
        x = NeverMatch(allow_null=True)
        print("Constructed a NeverMatch")
    except AssertionError:
        print("Failed to construct a NeverMatch")


# Generated at 2022-06-14 14:22:04.665489
# Unit test for method validate of class OneOf

# Generated at 2022-06-14 14:22:11.117450
# Unit test for constructor of class Not
def test_Not():
    from typesystem import Schema
    from typesystem.fields import String
    assert Not(String()).negated == String()
    assert Not(OneOf([String()])).negated == OneOf([String()])
    assert Not(Not(String())).negated == String()
    assert Not(Not(String()), description="Test").description == "Test"
    assert Not(Schema({"name": String()})).negated == Schema({"name": String()})

# Generated at 2022-06-14 14:22:12.447796
# Unit test for constructor of class OneOf
def test_OneOf():
    assert isinstance(OneOf(one_of=[Any()]), OneOf)

# Generated at 2022-06-14 14:22:14.253182
# Unit test for constructor of class Not
def test_Not():
    """
    To test constructor of class Not
    """
    assert Not(Field())



# Generated at 2022-06-14 14:22:16.580545
# Unit test for method validate of class Not
def test_Not_validate():
    # Create a new object of class Not
    t = Not(Any())
    # Test if it is valid
    assert t.validate("hello") is "hello"


# Generated at 2022-06-14 14:22:24.813717
# Unit test for constructor of class OneOf
def test_OneOf():
    tester = ['bar']
    instance = OneOf(tester)
    assert instance.one_of == tester
    assert instance.errors == {'no_match': 'Did not match any valid type.',
                               'multiple_matches': 'Matched more than one type.'}
    error = "'NeverMatch' object has no attribute '_build_schema'"
    try:
        instance.build_schema()
    except AttributeError:
        assert str(AttributeError) == error
    error = "'NeverMatch' object has no attribute '_validate'"
    try:
        instance.validate('foo', strict=True)
    except AttributeError:
        assert str(AttributeError) == error
    error = "'NeverMatch' object has no attribute 'validation_error'"

# Generated at 2022-06-14 14:22:34.664057
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    print("test_OneOf_validate")
    #test case A:
    field1 = Field(required=False, nullable=False)
    field2 = Field(required=True, nullable=False)
    field3 = Field(required=False, nullable=True)
    field_list = [field1,field2,field3]
    field_list2 = [field2,field1]
    field_list3 = [field1,field3]
    field4 = OneOf(field_list)
    value4 = "hello"
    field4.validate(value4)
    value5 = "hello"
    field5 = OneOf(field_list2)
    field5.validate(value5)
    value6 = "hello"
    field6 = OneOf(field_list3)