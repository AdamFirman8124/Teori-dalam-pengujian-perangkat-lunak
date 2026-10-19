

# Generated at 2022-06-14 14:12:44.677189
# Unit test for constructor of class OneOf
def test_OneOf():
    def test_it():
        one_of = OneOf(one_of = [])
        assert one_of
    test_it()


# Generated at 2022-06-14 14:12:49.991876
# Unit test for constructor of class AllOf
def test_AllOf():
    # Happy path
    AllOf(all_of=[Any(), Any()])
    AllOf(all_of=[Any()])
    # Cannot be empty
    with pytest.raises(AssertionError):
        AllOf(all_of=[])
    # Must be a list of fields
    with pytest.raises(AssertionError):
        AllOf(all_of=[1,2,3])


# Generated at 2022-06-14 14:12:51.982011
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    field = NeverMatch()
    assert isinstance(field, Field)
    assert field.errors == {"never": "This never validates."}


# Generated at 2022-06-14 14:12:58.132248
# Unit test for method validate of class IfThenElse

# Generated at 2022-06-14 14:13:02.923545
# Unit test for method validate of class Not
def test_Not_validate():
    f = Not(nullable=True)
    # test 1
    assert f.validate(None) is None
    # test 2
    assert f.validate(1) == 1
    # test 3
    try:
        f.validate(0)
    except:
        assert False


# Generated at 2022-06-14 14:13:06.384593
# Unit test for method validate of class Not
def test_Not_validate():
    class TestNot(Not):
        def __init__(self):
            self.negated = Int()
    _not = TestNot()
    _not.validate(1)

# Generated at 2022-06-14 14:13:10.026590
# Unit test for method validate of class Not
def test_Not_validate():
    # Create Not object
    not_field = Not(negated=Not(negated=AllOf(all_of=[Any()])))
    # Test validate
    result = not_field.validate('abc')
    assert result == 'abc'


# Generated at 2022-06-14 14:13:15.483089
# Unit test for method validate of class Not
def test_Not_validate():
    # Test case 1
    print("Test case 1")
    field = String()
    neg = Not(negated=field)
    print("Should be True: " + str(neg.validate("a") == "a"))
    
    # Test case 2
    print("Test case 2")
    field = String()
    neg = Not(negated=field)
    print("Should be False: " + str(neg.validate("a") == "b"))



# Generated at 2022-06-14 14:13:18.458562
# Unit test for method validate of class Not
def test_Not_validate():
    field = Not(Any())
    assert field.validate(1) == 1
    with pytest.raises(ValidationError):
        field.validate(None)

# Unit tests for class AlwaysMatch

# Generated at 2022-06-14 14:13:21.880413
# Unit test for method validate of class Not
def test_Not_validate():
    not_field = Not(None)
    
    if type(Not(None).validate(None)) == type(None):
        print("PASSED")
    else:
        print("FAILED")


# Generated at 2022-06-14 14:13:37.242709
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    class ColorName(Field):
        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            return value

    class ColorHexCode(Field):
        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            return value

    class IfThenElse(Field):
        def __init__(
            self,
            if_clause: Field,
            then_clause: Field = None,
            else_clause: Field = None,
            **kwargs: typing.Any
        ) -> None:
            assert "allow_null" not in kwargs
            super().__init__(**kwargs)
            self.if_clause = if_clause
            self.then_clause = Any() if then_clause is None else then_cl

# Generated at 2022-06-14 14:13:48.350606
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    if_clause = Int(gt=0)
    then_clause = Float()
    else_clause = String()

    if_then_else = IfThenElse(if_clause=if_clause, then_clause=then_clause, else_clause=else_clause)

    try:
        if_then_else.validate(0.1)
    except ValidationError as e:
        assert e.messages == {'type': 'Value must be an integer.'}

    try:
        if_then_else.validate(0)
    except ValidationError as e:
        assert e.messages == {'gt': 'Value must be greater than 0.'}

    assert if_then_else.validate(1.0) == 1.0

# Generated at 2022-06-14 14:13:53.481962
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    class TestField(Field):
        def validate(self, value, strict=False):
            return value

    false_clause = IfThenElse(if_clause=TestField(), then_clause=TestField(), else_clause=TestField())
    true_clause = IfThenElse(
        if_clause=TestField(), then_clause=TestField(validators=[lambda val: len(val) > 3]), else_clause=TestField()
    )
    assert false_clause.validate("abc") == "abc"
    assert true_clause.validate("abc") == "abc"

# Generated at 2022-06-14 14:13:55.793149
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    validator = OneOf([Any(), Any()])
    value = 10
    expected = value
    actual = validator.validate(value)
    assert actual == expected


# Generated at 2022-06-14 14:14:08.213505
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    field = IfThenElse(if_clause=int, then_clause=str)
    assert field.validate(0) == 0

    field = IfThenElse(if_clause=int, then_clause=str)
    assert field.validate("not int") == "not int"

    field = IfThenElse(if_clause=int, else_clause=str)
    assert field.validate("not int") == "not int"

    field = IfThenElse(if_clause=int, else_clause=str)
    assert field.validate(0) == "0"

    field = IfThenElse(if_clause=int, then_clause=str, else_clause=Any())
    assert field.validate("not int") == "not int"


# Generated at 2022-06-14 14:14:18.441264
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    class CustomField(Field):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def validate(self, value):
            return value
    f1 = CustomField()
    f2 = CustomField()
    value = 1
    o = OneOf([f1, f2])
    o.validate(value, strict=True)
    assert o.validate(value, strict=False) == value
    o = OneOf([NeverMatch(), f2])
    o.validate(value, strict=True)
    assert o == 1


# Generated at 2022-06-14 14:14:24.075922
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    _if = IsType(int)
    _then = IsType(str)
    _else = IsType(bool)
    test_item = {'if': _if, 'then' : _then, 'else': _else}
    _if_then_else = IfThenElse(**test_item)
    assert isinstance(_if_then_else.if_clause, _if.__class__)
    assert isinstance(_if_then_else.then_clause, _then.__class__)
    assert isinstance(_if_then_else.else_clause, _else.__class__)

# Generated at 2022-06-14 14:14:32.197803
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    class String(Field):
        errors = {"not_a_string": "Must be a string."}
        def validate(self, value, *args, **kwargs):
            if not isinstance(value, str):
                raise self.validation_error("not_a_string")
            return value
    class Integer(Field):
        errors = {"not_an_integer": "Must be an integer."}
        def validate(self, value, *args, **kwargs):
            if not isinstance(value, int):
                raise self.validation_error("not_an_integer")
            return value
    if_clause = String()
    then_clause = Integer()
    else_clause = Any()
    field = IfThenElse(if_clause,then_clause,else_clause)
    # the clause is

# Generated at 2022-06-14 14:14:39.334960
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    assert IfThenElse(if_clause=Any()).validate("Test") is "Test"
    assert IfThenElse(if_clause=NeverMatch()).validate("Test") is None
    assert IfThenElse(if_clause=NeverMatch(), then_clause=Any()).validate("Test") is "Test"
    assert IfThenElse(if_clause=NeverMatch(), else_clause=Any()).validate("Test") is None
    assert IfThenElse(if_clause=NeverMatch(), then_clause=Any(), else_clause=NeverMatch()).validate("Test") is None
    assert IfThenElse(if_clause=NeverMatch(), then_clause=NeverMatch(), else_clause=Any()).validate("Test") is "Test"

# Generated at 2022-06-14 14:14:50.092275
# Unit test for constructor of class OneOf
def test_OneOf():
    import decimal
    import datetime
    import uuid

    class DecimalField(Any):
        def convert(self, value, path):
            assert DecimalField.is_decimal(value)
            return decimal.Decimal(value)

    class DateTimeField(Any):
        def convert(self, value, path):
            assert DateTimeField.is_datetime(value)
            return datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")

    class UUIDField(Any):
        def convert(self, value, path):
            assert UUIDField.is_uuid(value)
            return uuid.UUID(value)


# Generated at 2022-06-14 14:14:55.552550
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    field = NeverMatch()
    assert field.type_name == "never_match"
    assert field.errors == {"never": "This never validates."}
    assert field.name == "NeverMatch"


# Generated at 2022-06-14 14:15:01.195601
# Unit test for constructor of class OneOf
def test_OneOf():
    from typesystem import Integer

    # This is a contrived example, but for each test, it
    # should be possible to create a unique, generated example
    # to test the constructor.
    one_of = OneOf([Integer(minimum=1, maximum=100)] )

    assert not (one_of is None)


# Generated at 2022-06-14 14:15:11.375137
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    import torch
    import numpy as np
    import typesystem
    if_clause = typesystem.types.Dict({'a':typesystem.types.UnsignedInteger()})
    then_clause = typesystem.types.Dict({'b':typesystem.types.Float()})
    else_clause = typesystem.types.Dict({'c':typesystem.types.Float()})
    if_then_else = typesystem.types.IfThenElse(if_clause=if_clause, then_clause=then_clause, else_clause=else_clause)
    if_then_else.validate({'c': 2.0})
    with pytest.raises(typesystem.exceptions.ValidationError):
        if_then_else.validate({'a': 2})



# Generated at 2022-06-14 14:15:12.668980
# Unit test for constructor of class Not
def test_Not():
    assert Not


# Generated at 2022-06-14 14:15:16.005726
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    field_1 = NeverMatch(name="NeverMatch")
    assert field_1.name == "NeverMatch"
    assert field_1.errors == {"never": "This never validates."}


# Generated at 2022-06-14 14:15:19.749031
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    nm = NeverMatch()
    with pytest.raises(AssertionError):
        NeverMatch(allow_null=False)
    assert nm.errors == {"never": "This never validates."}


# Generated at 2022-06-14 14:15:20.380043
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    assert True

# Generated at 2022-06-14 14:15:27.744276
# Unit test for constructor of class IfThenElse
def test_IfThenElse():

    # There is no child class of Field that is callable (i.e. can be used as a function), so
    # using the built-in function type here.
    def test_if_clause(x):
        return True
    def test_then_clause(x):
        return True
    def test_else_clause(x):
        return True

    f = IfThenElse(test_if_clause, test_then_clause, test_else_clause)
    assert(f.validate(1) == True)



# Generated at 2022-06-14 14:15:29.393865
# Unit test for constructor of class AllOf
def test_AllOf():
    all_of=[256]
    Field.validate(all_of, strict=False)
    


# Generated at 2022-06-14 14:15:30.492358
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    field = NeverMatch()
    assert field


# Generated at 2022-06-14 14:15:38.492285
# Unit test for constructor of class OneOf
def test_OneOf():
    all1 = Field()
    assert OneOf([all1]).validate(3) == 3

# Generated at 2022-06-14 14:15:39.963145
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    try:
        IfThenElse(None, None, None)
    except:
        assert False
    assert True

# Generated at 2022-06-14 14:15:46.060385
# Unit test for constructor of class OneOf
def test_OneOf():
    # Test type error for bad arg type
    with pytest.raises(TypeError) as error_info1:
        OneOf("hi")
    assert str(error_info1.value).startswith("one_of is not a List")
    # Test type error for empty list
    with pytest.raises(TypeError) as error_info2:
        OneOf([])
    assert str(error_info2.value).startswith("Empty list")
    # Test type error for non-Field list item
    with pytest.raises(TypeError) as error_info3:
        OneOf([1])
    assert str(error_info3.value).startswith("Wrong item")
    # Test type error for list items of different Field subtypes

# Generated at 2022-06-14 14:15:51.475888
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    from typesystem.fields import Boolean, Integer, String

    a = IfThenElse(
        if_clause=Boolean(),
        then_clause=Integer(),
        else_clause=String(),
    )
    assert a.validate(True) == 0
    assert a.validate(False) == ""

# Generated at 2022-06-14 14:15:52.597176
# Unit test for constructor of class AllOf
def test_AllOf():
    x: Field = AllOf([])


# Generated at 2022-06-14 14:15:56.787236
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    assert isinstance(IfThenElse(Field(),Field()), IfThenElse)
    assert isinstance(IfThenElse(Field(),else_clause=Field()), IfThenElse)
    assert isinstance(IfThenElse(Field(),then_clause=Field()), IfThenElse)
    assert isinstance(IfThenElse(Field()), IfThenElse)


# Generated at 2022-06-14 14:15:58.553517
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    with pytest.raises(AssertionError):
        NeverMatch(allow_null=True)


# Generated at 2022-06-14 14:16:01.487969
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    a=IfThenElse(1,2,3)
    print(a.__dict__)

test_IfThenElse()

# Generated at 2022-06-14 14:16:04.343059
# Unit test for constructor of class AllOf
def test_AllOf():
    all_of = AllOf([Field()], description='foo')
    assert isinstance(all_of, Field)


# Generated at 2022-06-14 14:16:07.927119
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
   field = IfThenElse(if_clause=1, then_clause=2, else_clause=3)
   assert field.if_clause == 1
   assert field.then_clause == 2
   assert field.else_clause == 3


# Generated at 2022-06-14 14:16:12.904113
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    NeverMatch()


# Generated at 2022-06-14 14:16:16.049631
# Unit test for constructor of class AllOf
def test_AllOf():
    all_of: typing.List[Field] = [Any(), Any()]
    field: AllOf = AllOf(all_of)
    assert field.all_of is all_of


# Generated at 2022-06-14 14:16:17.345620
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    my_field = NeverMatch()
    


# Generated at 2022-06-14 14:16:18.264403
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    NeverMatch()


# Generated at 2022-06-14 14:16:20.434338
# Unit test for constructor of class OneOf
def test_OneOf():
    field = OneOf([Field(name='test')])
    assert field.one_of == [Field(name='test')]


# Generated at 2022-06-14 14:16:22.460987
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    assert NeverMatch()


# Generated at 2022-06-14 14:16:23.350616
# Unit test for constructor of class AllOf
def test_AllOf():
    pass

# Generated at 2022-06-14 14:16:25.493733
# Unit test for constructor of class OneOf
def test_OneOf():
    one_of_test = OneOf(one_of = [Field(name='test')])
    assert not one_of_test.name


# Generated at 2022-06-14 14:16:29.571847
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    # Default arguments
    nevermatch = NeverMatch()
    # Assertions
    assert (nevermatch.errors == {"never": "This never validates."})
    assert (nevermatch.name == "nevermatch")
    assert (nevermatch.description == "")
    assert (nevermatch.nullable == True)


# Generated at 2022-06-14 14:16:31.939517
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    field = IfThenElse(Any(), None, None)
    assert field.if_clause
    assert field.then_clause
    assert field.else_clause

# Generated at 2022-06-14 14:16:41.088642
# Unit test for constructor of class OneOf
def test_OneOf():
    y = OneOf(one_of=[Field(),Field()], description=None)
    assert "one_of" in y.__dict__


# Generated at 2022-06-14 14:16:45.892277
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    f = IfThenElse(
        if_clause=Field(),
        then_clause=String(),
        else_clause=Number(),
    )
    return f.if_clause is not None and f.then_clause is not None and f.else_clause is not None

# Generated at 2022-06-14 14:16:48.642389
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    field = NeverMatch()
    # test if the instance of the class is of the same type
    assert isinstance(field, NeverMatch) == True


# Generated at 2022-06-14 14:16:49.630992
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    field = IfThenElse(1)

# Generated at 2022-06-14 14:16:55.782289
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    field = NeverMatch(name="NeverMatch_test")
    field = NeverMatch(name="NeverMatch_test", description="NeverMatch_test")
    field = NeverMatch(
        name="NeverMatch_test",
        description="NeverMatch_test",
    )
    field = NeverMatch(
        name="NeverMatch_test",
        description="NeverMatch_test",

    )
    field = NeverMatch(
        name="NeverMatch_test",
        description="NeverMatch_test",
        errors={
            "never": "never_test"
        }
    )

# Generated at 2022-06-14 14:17:00.965413
# Unit test for constructor of class OneOf
def test_OneOf():
    a_list = [Field(),Field()]
    t = OneOf(a_list)
    assert t.one_of == a_list
    assert t.errors == {'no_match': 'Did not match any valid type.', 'multiple_matches': 'Matched more than one type.'}


# Generated at 2022-06-14 14:17:05.418729
# Unit test for constructor of class OneOf
def test_OneOf():
    def __init__(self, one_of: typing.List[Field], **kwargs: typing.Any) -> None:
        assert "allow_null" not in kwargs
        super().__init__(**kwargs)
        self.one_of = one_of

# Generated at 2022-06-14 14:17:09.284990
# Unit test for constructor of class OneOf
def test_OneOf():
    oo = OneOf([])
    assert oo.one_of == []
    assert oo.errors['no_match'] == 'Did not match any valid type.'
    assert oo.errors['multiple_matches'] == 'Matched more than one type.'

# Generated at 2022-06-14 14:17:11.745236
# Unit test for constructor of class OneOf
def test_OneOf():
    type_ = OneOf([])
    assert type_.one_of == []
    assert type_.required == False


# Generated at 2022-06-14 14:17:16.949057
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    if_clause = int
    then_clause = float
    else_clause = str
    x = IfThenElse(if_clause, then_clause, else_clause)
    assert isinstance(x, IfThenElse)
    assert x.if_clause == if_clause
    assert x.then_clause == then_clause
    assert x.else_clause == else_clause

# Generated at 2022-06-14 14:17:31.168956
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    # Arrange
    field = IfThenElse(None, None, None)

    # Act

    # Assert
    assert field

# Generated at 2022-06-14 14:17:33.664755
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    a = NeverMatch()
    assert issubclass(type(a), Field)


# Generated at 2022-06-14 14:17:36.772999
# Unit test for constructor of class OneOf
def test_OneOf():
    one_of = [Field()]
    assert(str(OneOf(one_of)) == "OneOf(<typesystem.fields.Field>)")

# Generated at 2022-06-14 14:17:45.865365
# Unit test for constructor of class AllOf
def test_AllOf():
    from typesystem import (
        Array,
        Boolean,
        Integer,
        Number,
        Object,
        Schema,
        String,
    )
    from typesystem.middleware import JSONSchemaMiddleware, ValidationMiddleware

    class TestSchema(Schema):
        array_of_json = Array(items=AllOf([Boolean(), Integer(), Number()]))
        simple_object = Object(properties={"key": String()})
        complex_object = Object(properties={"key": AllOf([Boolean(), Integer(), Number()])})

        class Meta:
            middleware = [ValidationMiddleware(), JSONSchemaMiddleware()]

    schema = TestSchema()

# Generated at 2022-06-14 14:17:46.952438
# Unit test for constructor of class OneOf
def test_OneOf():
  # assert o.one_of == one_of
  pass

# Generated at 2022-06-14 14:17:49.941242
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    n = NeverMatch()
    value_to_test, error = n.validate_or_error(1)
    assert error == {'never': 'This never validates.'}


# Generated at 2022-06-14 14:17:52.275899
# Unit test for constructor of class OneOf
def test_OneOf():
    c = OneOf(one_of=[])
    c = OneOf(one_of=[Any()])
    c = OneOf(one_of=[Any(), Any()])

# Generated at 2022-06-14 14:17:53.847729
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    nm = NeverMatch(name='NeverMatch')
    #nm.validate('test')
    assert nm is not None

# Generated at 2022-06-14 14:17:55.488827
# Unit test for constructor of class AllOf
def test_AllOf():
    
    assert isinstance(AllOf, object)



# Generated at 2022-06-14 14:17:56.663916
# Unit test for constructor of class AllOf
def test_AllOf():
    assert "allow_null" not in AllOf([]).kwargs

# Generated at 2022-06-14 14:18:24.062518
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    nm = NeverMatch()
    assert nm.errors["never"] == "This never validates."


# Generated at 2022-06-14 14:18:24.994734
# Unit test for constructor of class OneOf
def test_OneOf():
    assert OneOf is not None


# Generated at 2022-06-14 14:18:26.242679
# Unit test for constructor of class AllOf
def test_AllOf():
    assert AllOf



# Generated at 2022-06-14 14:18:28.288898
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    test = IfThenElse(String(max_length = 5), Integer())
    assert test.if_clause.max_length == 5
    assert isinstance(test.then_clause, Integer)

# Generated at 2022-06-14 14:18:30.851006
# Unit test for constructor of class OneOf
def test_OneOf():
    field = OneOf([])
    assert field.errors == {'multiple_matches': 'Matched more than one type.', 'no_match': 'Did not match any valid type.'}



# Generated at 2022-06-14 14:18:36.579738
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    f = IfThenElse(String(), String(), String())
    # Test for if_clause
    assert f.if_clause.__class__ is String
    # Test for then_clause
    assert f.then_clause.__class__ is String
    # Test for else_clause
    assert f.else_clause.__class__ is String

# Generated at 2022-06-14 14:18:37.975253
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    assert NeverMatch(), "Creating a NeverMatch object should not raise an exception"


# Generated at 2022-06-14 14:18:40.856793
# Unit test for constructor of class OneOf
def test_OneOf():
    x = [] # Declare x as a list
    kwargs = {} # Declare kwargs as an empty dict
    assert x.__init__(**kwargs) == x


# Generated at 2022-06-14 14:18:44.418651
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    x = IfThenElse(Any('x'), Any('y'))
    assert x.if_clause is not None
    assert x.then_clause is not None
    assert x.else_clause is not None

# Generated at 2022-06-14 14:18:47.103267
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    with pytest.raises(AssertionError):
        NeverMatch(allow_null=False)

