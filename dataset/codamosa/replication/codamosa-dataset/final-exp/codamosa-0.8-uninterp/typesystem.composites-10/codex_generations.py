

# Generated at 2022-06-14 14:12:40.443114
# Unit test for constructor of class Not
def test_Not():
    field = Not(negated='Integer')
    assert field.negated == 'Integer'


# Generated at 2022-06-14 14:12:44.943519
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    from typesystem.fields import String

    field = IfThenElse(
        String(), String(), String()
    )
    assert isinstance(field, IfThenElse)

    field.validate("hello")  # => "hello"



# Generated at 2022-06-14 14:12:53.340324
# Unit test for method validate of class Not
def test_Not_validate():
    current_path = os.path.dirname(os.path.abspath(__file__))
    parent_path = os.path.dirname(current_path)
    path = parent_path + "/test_files/test_Not.json"
    with open(path, 'r') as fd:
        test_Not = json.load(fd)
    for test_case in test_Not["cases"]:
        for test in test_case["tests"]:
            not_field = Not(String())
            if "value" in test:
                try:
                    not_field.validate(test["value"])
                    assert test["valid"]
                except Exception as e:
                    assert not test["valid"]


# Generated at 2022-06-14 14:12:55.610938
# Unit test for constructor of class AllOf
def test_AllOf():
    all_of = AllOf(None)
    assert all_of.all_of is None


# Generated at 2022-06-14 14:12:56.805683
# Unit test for constructor of class Not
def test_Not():
    assert 1 == 1

# Generated at 2022-06-14 14:12:58.479799
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
	assert isinstance(NeverMatch(), Field)


# Generated at 2022-06-14 14:12:59.505392
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    f = NeverMatch()



# Generated at 2022-06-14 14:13:04.981223
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    from typesystem import Schema, Number, String
    schema = Schema(
        title="IfThenElseTestSchema",
        enum=["A", "B", "C"],
    )

    assert len(schema.validate(IfThenElse(if_clause=String(), then_clause=Number()))) == 1

# Generated at 2022-06-14 14:13:14.653723
# Unit test for method validate of class Not
def test_Not_validate():
    import json

    class MyFieldNot(Not):
        def __init__(self, negated: Field, **kwargs: typing.Any) -> None:
            assert "allow_null" not in kwargs
            super().__init__(negated, **kwargs)

        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            _, error = self.negated.validate_or_error(value, strict=strict)
            if error:
                return value
            raise self.validation_error("negated")

    class MyFieldAllOf(AllOf):
        def __init__(self, all_of: typing.List[Field], **kwargs: typing.Any) -> None:
            assert "allow_null" not in kwargs

# Generated at 2022-06-14 14:13:18.414581
# Unit test for method validate of class Not
def test_Not_validate():
    # Initiate class Not with proper parameters
    not_field = Not(AllOf([String(format='date-time'), Int()]))
    # test the validate method
    assert not_field.validate(value = 12) is 12

# Generated at 2022-06-14 14:13:24.180578
# Unit test for method validate of class Not
def test_Not_validate():
    field = Not(String(), label="a")
    field.validate(object)
    field.validate(1)

# Generated at 2022-06-14 14:13:26.764097
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    instance = OneOf([Field()])
    assert instance.validate(1) == 1
    assert instance.validate(1) == 1



# Generated at 2022-06-14 14:13:35.626098
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    if_clause = Field(name='if_clause')
    then_clause = Field(name='then_clause')
    else_clause = Field(name='else_clause')

    s = IfThenElse(if_clause, then_clause, else_clause)
    assert s.if_clause == if_clause
    assert s.then_clause == then_clause
    assert s.else_clause == else_clause


# Generated at 2022-06-14 14:13:39.620781
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    from typesystem.fields import Boolean

    validator = IfThenElse(
        if_clause=Boolean(),
        then_clause=Boolean(),
        else_clause=Boolean()
    )
    assert validator.validate(True) == True
    assert validator.validate(False) == False
    assert validator.validate(True) == True



# Generated at 2022-06-14 14:13:49.995385
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


# Generated at 2022-06-14 14:13:51.999466
# Unit test for constructor of class Not
def test_Not():
    integerField = {"IntegerField": IntegerField()}
    not_field = Not(negated=integerField)
    assert not_field.negated == integerField

# Generated at 2022-06-14 14:13:53.720777
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    field = NeverMatch()
    assert field.error_messages == {'never': 'This never validates.'}


# Generated at 2022-06-14 14:13:54.617305
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    obj = NeverMatch()



# Generated at 2022-06-14 14:13:55.832180
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    test_NeverMatch = NeverMatch()
    assert test_NeverMatch


# Generated at 2022-06-14 14:14:05.007915
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    type = OneOf([Any()])
    assert type.validate(123) == 123
    try:
        type.validate("foo")
    except Exception as error:
        assert error.code == 'no_match'
        assert error.fields == ['one_of']

    type = OneOf([Any(), Any()])
    try:
        type.validate("foo")
    except Exception as error:
        assert error.code == 'multiple_matches'
        assert error.fields == ['one_of']



# Generated at 2022-06-14 14:14:14.424958
# Unit test for method validate of class Not
def test_Not_validate():
    from typesystem.types import String
    from typesystem.fields import Not
    s = String()
    n = Not(s)
    assert n.validate(1)==1
    assert n.validate('a')=='a'
    assert n.validate(True)==True
    assert n.validate(None)==None
    assert n.validate([])==[]
    assert n.validate({})=={}

# Generated at 2022-06-14 14:14:26.801584
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    obj_I = "abcd"
    obj_T = Field(type_class= str, choices=["abcd", "efgh"])
    obj_E = Field(type_class= str, choices=["1234", "5678"])
    obj_I_T_E = IfThenElse(if_clause=obj_I, then_clause=obj_T, else_clause=obj_E)
    print (obj_I_T_E.validate(value=obj_I))
    print (obj_I_T_E.validate(value="efgh"))
    print (obj_I_T_E.validate(value="1234"))
    print (obj_I_T_E.validate(value="5678"))

# Generated at 2022-06-14 14:14:29.735228
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
  if_clause = Field()
  then_clause = Field()
  else_clause = Field()
  return IfThenElse(if_clause, then_clause, else_clause)

# Generated at 2022-06-14 14:14:32.464766
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    f = IfThenElse(True, True, False)
    v, err = f.validate_or_error(True)
    assert v == True
    assert err == None


# Generated at 2022-06-14 14:14:34.398163
# Unit test for constructor of class OneOf
def test_OneOf():
    from typesystem.fields import String
    s = String()
    field = OneOf([s])
    field.validate("abc")


# Generated at 2022-06-14 14:14:38.815542
# Unit test for method validate of class Not
def test_Not_validate():
    import typesystem
    import json

    class MySchema(typesystem.Schema):
        result = typesystem.Not(typesystem.Boolean(default=True))

    schema = MySchema()
    try:
        schema.validate({"result": True})
    except ValueError as e:
        assert e.message == 'Expected {"result": boolean}. Got {"result": true}, which is invalid because Must not match.'
    else:
        assert False, 'Expected ValueError'



# Generated at 2022-06-14 14:14:40.950040
# Unit test for method validate of class Not
def test_Not_validate():
    n = Not(AnInteger()) 
    # Must not match the Integer Field
    assert n.validate(5) == 5

# Generated at 2022-06-14 14:14:50.456315
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    from typesystem.fields import String, Integer, Boolean

    field = IfThenElse(Boolean(), String(), Integer())
    assert field.validate(True) == "True"
    assert field.validate(False) == 0
    assert field.validate("") == 0
    assert field.validate(0) == 0
    assert field.validate(None) == 0
    assert field.validate(True, strict=True) == "True"
    assert field.validate(False, strict=True) == 0
    try:
        field.validate(0, strict=True)
        assert False
    except Exception:
        pass
    try:
        field.validate(None, strict=True)
        assert False
    except Exception:
        pass

# Generated at 2022-06-14 14:14:54.735724
# Unit test for method validate of class Not
def test_Not_validate():
    # arrange
    negated = Any()
    field = Not(negated)
    value = "anything"
    expected = value
    actual = None

    # act
    actual = field.validate(value)

    # assert
    assert expected == actual


# Generated at 2022-06-14 14:14:55.340226
# Unit test for constructor of class Not
def test_Not():
    pass

# Generated at 2022-06-14 14:15:02.778652
# Unit test for method validate of class Not
def test_Not_validate():
    field = Not(Any())
    assert field.validate(1) == 1
    with pytest.raises(ValidationError) as exc_info:
        field.validate(None)
    assert exc_info.value.code == "negated"



# Generated at 2022-06-14 14:15:12.208388
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    from typesystem.fields import String, Number
    field = IfThenElse(
        if_clause=String(validators=["max_length:2"], allow_null=True),
        then_clause=String(validators=["max_length:10"]),
        else_clause=Number(validators=["min_value:1"]),
    )
    # The if clause is not validated
    assert field.validate(1) == 1
    assert field.validate(100) == 100
    assert field.validate(None) == None
    assert field.validate('') == ''
    # The then clause is validated
    assert field.validate('a') == 'a'
    assert field.validate('aa') == 'aa'
    assert field.validate('aaa') == 'aaa'
    # The else clause

# Generated at 2022-06-14 14:15:17.683619
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    if_clause = Field()
    then_clause = Field()
    else_clause = Field()
    parent = IfThenElse(if_clause, then_clause, else_clause)
    assert parent.validate(value=1) == 1
    assert parent.validate(value=1, strict=True) == 1


# Generated at 2022-06-14 14:15:20.273018
# Unit test for constructor of class AllOf
def test_AllOf():
  all_of = AllOf("a", 'b')
  assert all_of.all_of == "a,b"


# Generated at 2022-06-14 14:15:28.748287
# Unit test for method validate of class Not
def test_Not_validate():
    class Test:
        def __init__(self):
            self.validated = False
            self.strict = False

        def validate(self, value, strict=False):
            self.value = value
            self.strict = strict
            self.validated = True

    test = Test()

    not_field = Not(test)

    value = {'message': 'test message', 'error': 'test err'}
    try:
        not_field.validate(value, strict=True)
    except:
        return

    assert test.validated
    assert test.value == value
    assert test.strict



# Generated at 2022-06-14 14:15:30.298414
# Unit test for constructor of class Not
def test_Not():
    assert Not(negated=Field(required=True)).negated == Field(required=True)

# Generated at 2022-06-14 14:15:30.868100
# Unit test for constructor of class Not
def test_Not():
    assert Not is not None

# Generated at 2022-06-14 14:15:35.371336
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    # Given
    if_clause = Field()
    then_clause = Field()
    else_clause = Field()
    kwargs = {"test1": 1, "test2": 2}

    # When
    IfThenElse(if_clause, then_clause, else_clause, **kwargs)

    # Then
    # No exception thrown

# Generated at 2022-06-14 14:15:39.105948
# Unit test for constructor of class OneOf
def test_OneOf():
    try:
        one_of_field=OneOf(one_of=[])
    except Exception as e:
        assert type(e) == AssertionError
    else:
        assert False



# Generated at 2022-06-14 14:15:40.450171
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    assert IfThenElse(0).validate(1) == 1
    assert IfThenElse('a', "b", "c").validate(3) == 3

# Generated at 2022-06-14 14:15:43.622755
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    assert 'NeverMatch' == NeverMatch.__name__


# Generated at 2022-06-14 14:15:45.787203
# Unit test for constructor of class OneOf
def test_OneOf():
    """
    Ensure that a oneOf type will not accept null.
    """
    assert OneOf([Any()]).schema_field

# Generated at 2022-06-14 14:15:47.868466
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    assert True



# Generated at 2022-06-14 14:15:57.729095
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    assert IfThenElse(if_clause=Any()).validate("hello") == "hello"
    with raises(FieldError) as err:
        IfThenElse(if_clause=NeverMatch()).validate("hello")
    assert "never" in str(err)
    assert IfThenElse(if_clause=NeverMatch(), then_clause=Any()).validate("hello") == "hello"
    with raises(FieldError) as err:
        IfThenElse(if_clause=NeverMatch(), then_clause=NeverMatch()).validate("hello")
    assert "never" in str(err)
    with raises(FieldError) as err:
        IfThenElse(if_clause=NeverMatch(), else_clause=NeverMatch()).validate("hello")
    assert "never" in str(err)

# Generated at 2022-06-14 14:16:00.139746
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    x = IfThenElse(Number(), Number(), Number())
    assert x.validate(10) == 10


# Generated at 2022-06-14 14:16:06.213554
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    from typesystem import Integer
    from typesystem.fields import IfThenElse
    class MyIfThenElse(IfThenElse):
        def __init__(self, **kwargs: typing.Any) -> None:
            assert "allow_null" not in kwargs
            super().__init__(if_clause=Integer(), **kwargs)
    assert MyIfThenElse(then_clause=Integer())

# Generated at 2022-06-14 14:16:10.496397
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    from typesystem.fields import Integer
    from typesystem.base import Schema

    if_clause = Integer()
    then_clause = Integer(minimum=10)
    else_clause = Integer(minimum=5)
    if_else_clause = IfThenElse(if_clause, then_clause, else_clause)
    schema = Schema(if_else_clause=if_else_clause)

    if_clause = Integer()
    then_clause = Integer(minimum=10)
    else_clause = Integer(minimum=5)
    if_else_clause = IfThenElse(if_clause, then_clause, else_clause)
    schema = Schema(if_else_clause=if_else_clause)


# Generated at 2022-06-14 14:16:16.434177
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    if_clause = NeverMatch(name="if_clause")
    then_clause = NeverMatch(name="then_clause")
    else_clause = NeverMatch(name="else_clause")
    ite = IfThenElse(if_clause=if_clause, then_clause=then_clause, else_clause=else_clause)
    assert ite.validate(1)

# Generated at 2022-06-14 14:16:17.385634
# Unit test for constructor of class OneOf
def test_OneOf():
    assert OneOf([Any(), Any()])

# Generated at 2022-06-14 14:16:24.341315
# Unit test for method validate of class Not
def test_Not_validate():
    from typesystem.types import String
    from typesystem.exceptions import ValidationError
    import pytest

    Not_not_string_in_strict = Not(String())

    # When
    with pytest.raises(ValidationError) as exception:
        Not_not_string_in_strict.validate(1)

    # Then
    assert "Must not match" in str(exception.value)

    # When
    with pytest.raises(ValidationError) as exception:
        Not_not_string_in_strict.validate(1, strict=True)

    # Then
    assert "Must not match" in str(exception.value)


# Generated at 2022-06-14 14:16:27.796243
# Unit test for method validate of class Not
def test_Not_validate():
    not_field = Not(Any())

    assert not_field.validate(False) == False


# Generated at 2022-06-14 14:16:29.073125
# Unit test for constructor of class Not
def test_Not():
  f = Field()
  t = Not(f)


# Generated at 2022-06-14 14:16:35.015404
# Unit test for method validate of class Not
def test_Not_validate():
    def test_negative():
        negated = Any()
        value = 'foobar'
        not_field = Not(negated)
        not_field.validate(value)

    def test_positive():
        negated = Any()
        value = 'foobar'
        not_field = Not(negated)
        try:
            not_field.validate(value)
        except ValidationError:
            pass
        else:
            assert False, 'supposed to be a validation error'

    test_negative()
    test_positive()



# Generated at 2022-06-14 14:16:37.706744
# Unit test for constructor of class OneOf
def test_OneOf():
    sub_item1 = Field()
    sub_item2 = Field()
    oneOf = OneOf([sub_item1, sub_item2])

# Generated at 2022-06-14 14:16:43.596687
# Unit test for method validate of class Not
def test_Not_validate():
    class NotExample(Not):
        def __init__(self):
            super().__init__(String())

    # String should be valid
    notObj = NotExample()
    assert notObj.validate("abc") is not None

    # Number should be invalid
    with pytest.raises(ValidationError):
        notObj.validate(123)


# Generated at 2022-06-14 14:16:47.131173
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    nm = NeverMatch(description="Check the class NeverMatch", some_field="some_value")
    assert nm.description == "Check the class NeverMatch"
    assert nm.some_field == "some_value"


# Generated at 2022-06-14 14:16:49.966311
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    class Id(Field):
        def __init__(self, **kwargs: typing.Any) -> None:
            super().__init__(**kwargs)

        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            return value
    _ = IfThenElse(Id(), Id(), Id())

# Generated at 2022-06-14 14:16:52.823980
# Unit test for method validate of class Not
def test_Not_validate():
    custom_field = Not(Any(), description="test")
    try:
        custom_field.validate("asdf")
    except Exception as e:
        assert isinstance(e, custom_field.validation_error)
        assert e.code == "negated"


# Generated at 2022-06-14 14:16:55.637568
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    f = OneOf(one_of=[Boolean()])
    assert f.validate(False) == False
    try:
        f.validate(2)
        assert False
    except FieldError as ex:
        assert ex.code == 'no_match'


# Generated at 2022-06-14 14:16:57.757384
# Unit test for constructor of class AllOf
def test_AllOf():
    from typesystem import Integer, String
    field = AllOf([Integer(), String()])



# Generated at 2022-06-14 14:17:00.917614
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    pass

# Generated at 2022-06-14 14:17:04.011404
# Unit test for method validate of class Not
def test_Not_validate():
    n = Not(negated=Any())
    value = 1
    strict = False
    error = n.validate(value, strict)
    assert error == value

# Generated at 2022-06-14 14:17:10.586990
# Unit test for method validate of class Not
def test_Not_validate():
    #assert Not(one_of=float).validate(23) == 23
    #assert Not(one_of=[int]).validate(23.3) == 23.3
    assert Not(negated=float).validate(23.0) == 23.0
    assert Not(negated=int).validate(23.3) == 23.3
    #assert Not(negated=int).validate(23) == 23


# Generated at 2022-06-14 14:17:14.515789
# Unit test for method validate of class Not
def test_Not_validate():
    negated = MockField()
    negated.validate_or_error = Mock(return_value=(None, None))
    n = Not(negated)
    ret_value = n.validate(None)
    assert ret_value == None


# Generated at 2022-06-14 14:17:27.766733
# Unit test for constructor of class OneOf
def test_OneOf():
    class Field(OneOf):
        def __init__(self, **kwargs: typing.Any) -> None:
            assert "allow_null" not in kwargs
            super().__init__(kwargs)
            self.kwargs = kwargs
        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            return value
    class Field2():
        def __init__(self, **kwargs: typing.Any) -> None:
            assert "allow_null" not in kwargs
            super().__init__(kwargs)
            self.kwargs = kwargs
        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            return value
    print(1)

# Generated at 2022-06-14 14:17:31.370572
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    if_clause = String(max_length=3)
    then_clause = String(min_length=3)
    else_clause = String(min_length=5)
    IfThenElse(if_clause, then_clause, else_clause)



# Generated at 2022-06-14 14:17:37.191142
# Unit test for constructor of class OneOf
def test_OneOf():
    # one_of = {"foo": "bar"}
    one_of = Field()
    # kwargs = {"foo": "bar"}
    kwargs = None
    # OneOf(one_of, **kwargs)
    oo = OneOf(one_of, **kwargs)
    assert oo is not None

# Generated at 2022-06-14 14:17:40.460305
# Unit test for constructor of class OneOf
def test_OneOf():
    string_field = String()
    integer_field = Integer()
    assert OneOf([string_field, integer_field]).one_of == [string_field, integer_field]
test_OneOf()


# Generated at 2022-06-14 14:17:42.357489
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    n = NeverMatch()
    assert (n.errors == {'never': 'This never validates.'})


# Generated at 2022-06-14 14:17:49.206499
# Unit test for constructor of class OneOf
def test_OneOf():
    f = OneOf([Any()], description='', allow_const=False)
    assert f.errors == {'no_match': 'Did not match any valid type.', 'multiple_matches': 'Matched more than one type.'}
    assert f.description == ''
    assert f.allow_const == False
    assert f.one_of == [Any()]

# Generated at 2022-06-14 14:17:54.494177
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    f = IfThenElse(if_clause=Field(), then_clause=Field(), else_clause=Field())
    assert isinstance(f.if_clause, Field)
    assert isinstance(f.then_clause, Field)
    assert isinstance(f.else_clause, Field)

# Generated at 2022-06-14 14:17:58.520040
# Unit test for constructor of class OneOf
def test_OneOf():
    from typesystem import Schema
    from typesystem.fields.string import String
    from typesystem.fields.number import Number

    schema = Schema(one_of=OneOf(one_of=[Number(), String()]))
    assert schema.validate(2) == 2
    assert schema.validate('a') == 'a'


# Generated at 2022-06-14 14:18:03.490638
# Unit test for method validate of class Not
def test_Not_validate():
    assert Not(String()).validate('abc') == 'abc'
    assert Not(String()).validate(123) == 123

    try:
        Not(String()).validate('')
    except:
        pass
    else:
        assert False



# Generated at 2022-06-14 14:18:04.143833
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    assert NeverMatch()

# Generated at 2022-06-14 14:18:05.453335
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    f_NeverMatch = NeverMatch()
    assert f_NeverMatch.errors == {'never': 'This never validates.'}


# Generated at 2022-06-14 14:18:15.420066
# Unit test for constructor of class OneOf
def test_OneOf():
    args = [
        {'one_of': ['type']},
        {'one_of': ['type'], 'description': 'description'},
        {'one_of': ['type'], 'name': 'name'},
        {'one_of': ['type'], 'allow_null': True},
        {'one_of': ['type'], 'error_messages': {'no_match': 'no_match message', 'multiple_matches': 'multiple_matches message'}},
        {'name': 'name', 'one_of': ['type'], 'error_messages': {'no_match': 'no_match message', 'multiple_matches': 'multiple_matches message'}},
    ]

# Generated at 2022-06-14 14:18:22.658420
# Unit test for method validate of class Not
def test_Not_validate():
    negated = Not(Any(), error_messages={'negated': 'Must not match.'})
    assert negated.validate(1) == 1
    try:
        negated.validate(None)
    except ValidationError as e:
        print(e.code)
        print(e.detail)
        print(e.meta)
        assert e.code == 'negated'
        assert e.detail == 'Must not match.'
        assert e.meta is None


# Generated at 2022-06-14 14:18:24.503086
# Unit test for constructor of class Not
def test_Not():
    field = Not(negated=Field())
    assert field.negated is not None


# Generated at 2022-06-14 14:18:30.126353
# Unit test for constructor of class OneOf
def test_OneOf():
    from typesystem import Integer, String

    integer = Integer()
    string = String()
    a = OneOf([integer, string], default="b")

    assert a.validate("a").value == "a"
    assert a.validate(1).value == 1
    assert a.validate(None).value == "b"
    # assert a.validate("c") == 'Value "c" is not a valid integer.'


# Generated at 2022-06-14 14:18:31.354591
# Unit test for constructor of class Not
def test_Not():
    assert Not.__init__

# Generated at 2022-06-14 14:18:39.972944
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    test = NeverMatch(description="Hello")
    assert test.description == "Hello"

# Unit tests for constructor of class OneOf

# Generated at 2022-06-14 14:18:41.365727
# Unit test for constructor of class Not
def test_Not():
    not_field = Not(Field)
    assert not_field != None

# Generated at 2022-06-14 14:18:50.000811
# Unit test for method validate of class Not
def test_Not_validate():
    input = {
        "if": {
            "description": "A simple boolean field",
            "type": "boolean"
        },
        "then": {
            "description": "A simple string field",
            "type": "string"
        },
        "else": {
            "description": "A simple number field",
            "type": "number"
        }
    }
    output = IfThenElse(**input)
    value = output.validate(True)
    value = output.validate(False)
    return output

# Generated at 2022-06-14 14:18:52.485869
# Unit test for method validate of class Not
def test_Not_validate():
    not_field = Not(AllOf([String(), Integer()]))
    not_field.validate(2)


# Generated at 2022-06-14 14:18:56.213744
# Unit test for method validate of class Not
def test_Not_validate():
    # Check that validation fails when validation of negated attribute is successful
    negated = NeverMatch()
    not_field = Not(negated)
    with pytest.raises(Exception, match="Must not match."):
        not_field.validate("value")



# Generated at 2022-06-14 14:19:00.080396
# Unit test for method validate of class Not
def test_Not_validate():
    # test_validate_itself
    assert Not(Any()).validate(None) == None
    # test_validate_negated
    assert Not(Any()).validate(False) == False
    # test_validate_negated_error
    with pytest.raises(ValidationError):
        Not(Any()).validate(True)


# Generated at 2022-06-14 14:19:04.289023
# Unit test for method validate of class Not
def test_Not_validate():
   x = Not(negated= IfThenElse(if_clause= Int(),then_clause=Int(),else_clause=Int()))
   assert x.validate(1) == 1

# Generated at 2022-06-14 14:19:04.850348
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    nm = NeverMatch()

# Generated at 2022-06-14 14:19:09.423588
# Unit test for constructor of class OneOf
def test_OneOf():
    obj = OneOf([])
    assert obj.one_of == []
    assert obj.errors == {'no_match': 'Did not match any valid type.', 'multiple_matches': 'Matched more than one type.'}
    assert obj.context == {}
    assert obj.path == []


# Generated at 2022-06-14 14:19:11.619341
# Unit test for constructor of class OneOf
def test_OneOf():
    oneof = OneOf(one_of=[])
    assert oneof.one_of == []


# Generated at 2022-06-14 14:19:20.102857
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
	n = NeverMatch()
	assert isinstance(n, NeverMatch)



# Generated at 2022-06-14 14:19:20.772848
# Unit test for constructor of class Not
def test_Not():
    assert Not(negated = None).negated is None

# Generated at 2022-06-14 14:19:23.400337
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    field = IfThenElse(Any(), Any(), Any())
    assert field.if_clause.allow_null is True
    assert field.then_clause.allow_null is True
    assert field.else_clause.allow_null is True

# Generated at 2022-06-14 14:19:26.354565
# Unit test for constructor of class OneOf
def test_OneOf():
    try:
        OneOf(one_of=['a', 'b'])  # Calling the constructor with a wrong argument
    except:
        assert True
    else:
        assert False


# Generated at 2022-06-14 14:19:28.590647
# Unit test for constructor of class Not
def test_Not():
    # Not(Field)
    not_obj = Not(Field())
    assert not_obj.negated == Field()


# Generated at 2022-06-14 14:19:31.566353
# Unit test for constructor of class OneOf
def test_OneOf():
    x = AllOf([
        Any(),
        Any()
    ])
    assert x.all_of[0].__class__.__name__ == 'Any'
    assert x.all_of[1].__class__.__name__ == 'Any'


# Generated at 2022-06-14 14:19:33.623845
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    f = IfThenElse(
        if_clause=Field(),
        then_clause=Field(),
        else_clause=Field()
    )

# Generated at 2022-06-14 14:19:38.408708
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    import typesystem
    import pytest
    schema = typesystem.OneOf([typesystem.Integer(), typesystem.String()])
    assert schema.validate(1) == 1
    assert schema.validate('abc') == 'abc'
    with pytest.raises(typesystem.Error):
        schema.validate('abc', strict=True)

# Generated at 2022-06-14 14:19:47.881172
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    print("Testing class IfThenElse")

    # construct a sequence of sub-items
    elements = [{'abc': 123}]
    then_clause = {'def': 456}
    else_clause = {'ghi': 789}

    # construct the field
    f = IfThenElse(if_clause=elements,
                   then_clause=then_clause,
                   else_clause=else_clause)
    assert f.if_clause == elements
    assert f.then_clause == then_clause
    assert f.else_clause == else_clause

    # demonstrate that 'elements' matches the if_clause, so the value is
    # then validated by the then_clause
    value = {'abc': 123, 'def': 456}
    validated = f.valid

# Generated at 2022-06-14 14:19:51.726787
# Unit test for constructor of class Not
def test_Not():
    schema = Not(negated=None)
    assert schema.errors == {"negated": "Must not match."}
    assert schema.negated == None
    assert schema.__name__ == "Not"


# Generated at 2022-06-14 14:20:09.790946
# Unit test for constructor of class OneOf
def test_OneOf():
    assert (OneOf(one_of=[Boolean(), String()]) is not None)

# Generated at 2022-06-14 14:20:11.805511
# Unit test for method validate of class OneOf
def test_OneOf_validate():

    oneOfField = OneOf([])
    assert oneOfField.validate("") == None


# Generated at 2022-06-14 14:20:15.857629
# Unit test for constructor of class OneOf
def test_OneOf():
    a = OneOf([Any()])
    b = OneOf([Any(), Any()])
    c = OneOf([Any(), Any(), Any()])
    d = OneOf([Any(), Any(), Any(), Any()])


# Generated at 2022-06-14 14:20:20.873911
# Unit test for constructor of class OneOf
def test_OneOf():
    from typesystem.fields import Integer

    one_of = OneOf([Integer(), Integer()])
    assert one_of.one_of[0].__class__.__name__ == "Integer"
    assert one_of.one_of[1].__class__.__name__ == "Integer"
    assert one_of.allow_null == False


# Generated at 2022-06-14 14:20:23.941489
# Unit test for constructor of class Not
def test_Not():
    """
    Test for Not class constructor
    """
    not_test = Not(1)
    assert not_test.negated == 1


# Generated at 2022-06-14 14:20:25.585236
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
	field = NeverMatch(name='test_NeverMatch')
	assert field.__class__ == NeverMatch


# Generated at 2022-06-14 14:20:27.161665
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
  nm = NeverMatch(description = "This never validates.")
  assert isinstance(nm, Field)


# Generated at 2022-06-14 14:20:30.740704
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    # Create a NeverMatch field
    field = NeverMatch()
    # Test that this field returns the expected error message
    validated, error = field.validate_or_error(5)
    assert error == "This never validates."
    assert validated is None


# Generated at 2022-06-14 14:20:41.579258
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    from typesystem import Schema, fields
    from typesystem import validation_error
    from typesystem.exceptions import ValidationError
    from typesystem import validators
    from typesystem.utils import ISO_8601_DATETIME_REGEX
    from datetime import datetime

    class OneOfSchema(Schema):
        date = fields.OneOf(
            [
                fields.DateTime(),
                fields.String(validators=[validators.Regex(ISO_8601_DATETIME_REGEX)]),
            ]
        )

    a = datetime(2019, 9, 12)  # type: datetime
    schema = OneOfSchema(strict=True)  # type: Schema


# Generated at 2022-06-14 14:20:44.202532
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    one_of = OneOf([Strings()], allow_null=False)

    result = one_of.validate('1')
    assert result == "1"