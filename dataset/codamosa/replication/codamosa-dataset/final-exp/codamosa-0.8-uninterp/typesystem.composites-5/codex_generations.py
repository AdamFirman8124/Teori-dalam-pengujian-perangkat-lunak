

# Generated at 2022-06-14 14:12:45.110491
# Unit test for method validate of class Not
def test_Not_validate():
    foo = Not(String())
    # should pass
    foo.validate(False, strict=False)



# Generated at 2022-06-14 14:12:45.432585
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    pass

# Generated at 2022-06-14 14:12:51.397725
# Unit test for method validate of class Not
def test_Not_validate():
    a = Not(AllOf([Any(), Any()]))
    b, c = a.validate_or_error([1, 2, 3], strict=False)
    print (b)
    print (c)
    a = Not(AllOf([Any(), Any()]), error_messages={'negated': 'did not negated'})
    b, c = a.validate_or_error([1, 2], strict=False)
    print (b)
    print (c)


# Generated at 2022-06-14 14:13:02.819749
# Unit test for method validate of class Not
def test_Not_validate():
    notfld = Not(negated=Any())
    result1, error1 = notfld.validate_or_error('')
    if error1 is not None:
        print('Error found: {}'.format(error1))
    print('Result: {}'.format(result1))
    assert(error1 is None)
    result2, error2 = notfld.validate_or_error('ABC')
    if error2 is not None:
        print('Error found: {}'.format(error2))
    print('Result: {}'.format(result2))
    assert(error2 is None)

    notfld = Not(negated=OneOf([Any(), Any()]))
    result3, error3 = notfld.validate_or_error('')

# Generated at 2022-06-14 14:13:04.009642
# Unit test for constructor of class AllOf
def test_AllOf():
    from typesystem.fields import Array
    from typesystem import String

    all_of = AllOf([Array(items=String()), Array(max_items=1)])

# Generated at 2022-06-14 14:13:08.260233
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    assert IfThenElse(if_clause=1, then_clause=2, else_clause=3).validate(1) == 2
    assert IfThenElse(if_clause=1, then_clause=2, else_clause=3).validate(4) == 3

# Generated at 2022-06-14 14:13:10.722813
# Unit test for method validate of class Not
def test_Not_validate():
    field = Not(Any())
    valid, error = field.validate_or_error(None)
    assert valid == None 
    assert error == None


# Generated at 2022-06-14 14:13:16.592503
# Unit test for method validate of class Not
def test_Not_validate():
    not_field = Not(negated=Any())
    assert not_field.validate(None) == None
    assert not_field.validate(1) == 1
    assert not_field.validate(True) == True
    assert not_field.validate(3.14) == 3.14
    assert not_field.validate('abcd') == 'abcd'
    assert not_field.validate([1]) == [1]
    assert not_field.validate({1:1}) == {1:1}


# Generated at 2022-06-14 14:13:27.586839
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    from typesystem.fields import Integer
    from typing import Type
    class field(Field):
        errors = {
            "wrong": "this is wrong."
        }
    class field2():
        def validate(self, value, strict):
            return ["1", "2"]
    class field3(Field):
        errors = {
            "wrong2": "this is wrong2."
        }
    a_cls: Type[Field] = IfThenElse
    a = a_cls(field(), field2(), field3())
    a.validate(2)
    b = a_cls(field(), Integer())
    b.validate(3)
    c = a_cls(field(), else_clause=Integer())
    c.validate(3)

# Generated at 2022-06-14 14:13:35.108296
# Unit test for method validate of class Not
def test_Not_validate():
    field = Not(String(max_length=10))
    assert field.validate(None) == None
    assert field.validate(1234) == 1234

    field = Not(String(max_length=10))
    assert field.validate('a') == 'a'
    with pytest.raises(Invalid) as excinfo:
        field.validate('abc')

# Generated at 2022-06-14 14:13:43.474563
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    field = IfThenElse(Integer(10), strict=True)
    assert field.validate(9) == 9
    assert field.validate(10) == 10
    assert field.validate(11) == 11



# Generated at 2022-06-14 14:13:54.191373
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    class MyInteger(Field):
        errors = {"invalid": "Must be an integer."}
        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            if not isinstance(value, int):
                raise self.validation_error("invalid")
            return value
            
    s = IfThenElse(MyInteger(), MyInteger(), MyInteger())
        
    s.validate(-1)
    try:
        s.validate(1.1)
        assert False, "s.validate(1.1) should raise an exception"
    except ValidationError as e:
        assert str(e) == "'1.1' is not a valid integer."
        
    s.validate(None)
    s = IfThenElse(MyInteger(), MyInteger())

# Generated at 2022-06-14 14:13:56.062916
# Unit test for constructor of class OneOf
def test_OneOf():
    one_of = [Any()]
    one_of_field = OneOf(one_of)
    assert one_of_field


# Generated at 2022-06-14 14:13:57.622545
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    x = NeverMatch()


# Generated at 2022-06-14 14:14:00.506887
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    oneOf = OneOf(one_of=[
        'test',
        'test2'
    ])
    oneOf.validate('test')

# Generated at 2022-06-14 14:14:02.561078
# Unit test for constructor of class Not
def test_Not():
    assert isinstance(Not(negated=Boolean()), Not) == True


# Generated at 2022-06-14 14:14:10.954635
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    if_clause = AllOf([String(), AllowNone()])
    then_clause = String()
    else_clause = Integer()
    test_field = IfThenElse(if_clause, then_clause, else_clause)
    assert test_field.validate("yes") == "yes"
    assert test_field.validate(None) == None
    assert test_field.validate(42) == 42
    import pytest
    with pytest.raises(test_field.validation_error):
        test_field.validate(42.0)

test_IfThenElse_validate()

# Generated at 2022-06-14 14:14:12.445139
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    ite = IfThenElse(Any(), Any(), Any())



# Generated at 2022-06-14 14:14:20.855586
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    class OneOfTest(Field):
        def validate(self, value, strict=False):
            return "a"
    from typesystem.fields import Boolean
    field = OneOf([Boolean()], error_messages={"no_match": "error_message1"})
    value = True
    strict = False
    expected = "a"
    result = field.validate(value, strict)
    assert result == expected


# Generated at 2022-06-14 14:14:21.901275
# Unit test for method validate of class Not
def test_Not_validate():
    not_type = Not(Boolean())

# Generated at 2022-06-14 14:14:32.867427
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    if_clause = Field()
    else_clause = Field()
    then_clause = Field()
    field = IfThenElse(if_clause, then_clause, else_clause)
    field.validate("")


# Generated at 2022-06-14 14:14:34.284257
# Unit test for constructor of class OneOf
def test_OneOf():
    obj = OneOf()
    assert obj is not None

# Generated at 2022-06-14 14:14:35.281382
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    field = NeverMatch()
    assert field.validate("foo") == "foo"

# Generated at 2022-06-14 14:14:45.598171
# Unit test for method validate of class Not
def test_Not_validate():
    from typesystem import Schema, Boolean, Integer

    def some_predicate(x):
        return x in [0, 2]

    class MySchema(Schema):
        choices = Not(Integer(minimum=0, maximum=9))

    schema = MySchema()
    schema.validate(choices=0)
    schema.validate(choices=9)
    schema.validate(choices=0)
    schema.validate(choices=2)
    try:
        schema.validate(choices=3)
    except:
        pass
    else:
        assert False


# Generated at 2022-06-14 14:14:47.610033
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    from typesystem.types import String
    from typesystem.fields import IfThenElse, Integer
    

# Generated at 2022-06-14 14:14:54.435037
# Unit test for constructor of class Not
def test_Not():
    all_values = [
        {"name": "Alice", "salary": 10},
        {"name": "Bob", "salary": 20},
        {"name": "Charlie", "salary": 30},
    ]
    assert all(Not(MinLength(3)).validate_many(all_values) == [])

    # Unit test for constructor of class IfThenElse
    def test_IfThenElse():
        all_values = [
            {"name": "Alice", "salary": 10},
            {"name": "Bob", "salary": 20},
            {"name": "Charlie", "salary": 30},
        ]
        assert len(
            IfThenElse(MaxLength(1)).validate_many(all_values)
        ) == len(
            all_values
        )

    # Unit test for constructor of class OneOf


# Generated at 2022-06-14 14:14:58.162840
# Unit test for constructor of class OneOf
def test_OneOf():
    class Point:
        pass

    field = OneOf([Point(x=1), Point(y=2)], description="test OneOf")
    # field.validate()
    print(field)

# Generated at 2022-06-14 14:15:05.410390
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    oo = OneOf([str])
    assert oo.validate('my_string')
    assert not oo.validate(1)
    assert not oo.validate(True)
    assert not oo.validate(None)
    assert not oo.validate([1, 'hello'])
    assert not oo.validate({'a': 1, 'b': 2})
    assert not oo.validate((1, 'hello'))



# Generated at 2022-06-14 14:15:10.825768
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():

    from typesystem.fields import String
    from typesystem.composite import IfThenElse

    text = String()
    if_clause = IfThenElse(text, String(min_length=5))
    value_true = 'This will work'
    value_false = 'This will not'
    print(if_clause.validate(value_true))
    print(if_clause.validate(value_false))



# Generated at 2022-06-14 14:15:11.888879
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    NeverMatch(name="name")

# Generated at 2022-06-14 14:15:28.250960
# Unit test for constructor of class AllOf
def test_AllOf():
    test_object = AllOf([Integer()], name="AllOf")
    assert test_object.__class__.__name__ == "AllOf"
    assert test_object.all_of == [Integer()]
    assert test_object.name == "AllOf"
    assert test_object.errors == {}



# Generated at 2022-06-14 14:15:33.520669
# Unit test for method validate of class Not
def test_Not_validate():
    field = Not(Any())
    assert field.validate(1) == 1
    field = Not(Any(min_value=100))
    assert field.validate(1) == 1
    field = Not(Any(min_value=100))
    try:
        field.validate(1000)
        assert False
    except Exception as e:
        assert str(e) == 'Must not match.'


# Generated at 2022-06-14 14:15:35.414147
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    ifthenelse = IfThenElse(if_clause=IntegerField())
    assert ifthenelse.validate(2) == 2

# Generated at 2022-06-14 14:15:37.811629
# Unit test for constructor of class Not
def test_Not():
    class A(Field):
        pass
    a = A()
    b = Not(a)
    assert b.negated is a
    assert b.allow_null is None


# Generated at 2022-06-14 14:15:44.171935
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():

    # Create an instance of class IfThenElse
    if_clause = True
    then_clause = True
    else_clause = False
    then_if = IfThenElse(if_clause, then_clause, else_clause)

    # Create an instance of class IfThenElse
    if_clause = True
    then_clause = True
    else_clause = False
    else_if = IfThenElse(if_clause, then_clause, else_clause)

    # Assert that the value returned by method validate of class IfThenElse is correct
    assert then_if.validate(True) and else_if.validate(False)

# Generated at 2022-06-14 14:15:50.522785
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    assert OneOf([]).validate(1) is None
    assert OneOf([2]).validate(2) is None
    assert OneOf([2, 3]).validate(3) is None
    assert OneOf([2, 3]).validate(4) is None
    assert OneOf([2, 3]).validate(3, strict=True) is None


# Generated at 2022-06-14 14:15:59.436152
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    # Expect no_match error
    f = OneOf([
        String(),
        String(),
        String(),
        String(),
        String(),
        String(),
        String(),
        String(),
        String(),
        String(),
        String(),
        String(),
        String(),
        String(),
        String(),
        String(),
        String(),
        String(),
        String(),
        String(),
        String(),
        String(),
        String(),
        String(),
        String(),
        String(),
        String(),
    ])
    f.validate_or_error(20)

    # Expect multiple_matches error
    f2 = OneOf([String(), List()])
    f2.validate_or_error([None])

    # Expect No error
    f3 = OneOf([String(), Any()])
    f3.valid

# Generated at 2022-06-14 14:16:01.895800
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    from typesystem.fields import String, Integer
    assert isinstance(IfThenElse(if_clause=1), IfThenElse)


# Generated at 2022-06-14 14:16:07.399564
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():

    if_clause = Field("test if_clause field")
    then_clause = Field("test then_clause field")
    else_clause = Field("test else_clause field")
    if_then_else = IfThenElse(if_clause, then_clause, else_clause)
    assert if_then_else.validate("test") == "test"

# Generated at 2022-06-14 14:16:07.971389
# Unit test for constructor of class AllOf
def test_AllOf():
    assert 0

# Generated at 2022-06-14 14:16:36.542212
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    one_of = OneOf([Int(), Str(), "abc"])
    assert(one_of.validate(1) == 1)
    assert(one_of.validate("abc") == "abc")
    assert(one_of.validate("a") == "a")
    assert(one_of.validate("b") == "b")
    assert(one_of.validate("c") == "c")

    # test_OneOf_validate_with_strict
    one_of = OneOf([Int(), Str(), "abc"])
    assert(one_of.validate("abc", True) == "abc")
    try:
        one_of.validate("1.1", True)
    except Exception as e:
        assert(e.args[0] == "Must be a string.")

# Unit test

# Generated at 2022-06-14 14:16:44.907162
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    from typesystem.fields import String
    ite = IfThenElse(String(max_length=5), "Hello")
    result = ite.validate("Hello")
    assert result == "Hello"
    result = ite.validate("Hello world")
    """
    Because the IfThenElse field cannot distinguish between if_clause and else_clause,
    when the input is valid in the if_clause and invalid in the then_clause, it will report the error of the if_clause.
    """
    assert result == "Hello"

# Generated at 2022-06-14 14:16:54.687530
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    from typesystem import Integer

    # test for then_clause
    def function1(a, b):
        return a+b
    a = 1
    b = 2
    result = function1(a, b)
    assert result == 3
    a = ["a", "b", "c"]
    b = ["d"]
    result = function1(a, b)
    assert result == ['a', 'b', 'c', 'd']
    a = ["a", "b", "c", "d"]
    b = 1
    try:
        result = function1(a, b)
    except TypeError:
        print("Apples and oranges can't be added")

    # test for else_clause
    def function2(a, b):
        return a * b + 2 * max(a, b)

# Generated at 2022-06-14 14:16:55.409362
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    assert True

# Generated at 2022-06-14 14:16:58.737968
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    then = Any()
    else_ = Any()
    ifThenElse = IfThenElse(then=then, else_=else_)
    assert ifThenElse.validate(None) is None

# Generated at 2022-06-14 14:17:01.655603
# Unit test for method validate of class Not
def test_Not_validate():
    actual = Not(
        negated=Integer(minimum=2)
    ).validate(1)
    expected = 1
    assert actual == expected


# Generated at 2022-06-14 14:17:13.275637
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    test_type = IfThenElse(Boolean(), Boolean())
    assert test_type.validate(True) == True
    assert test_type.validate(False) == False

    test_type = IfThenElse(Boolean(), None, Boolean())
    assert test_type.validate(False) == False

    test_type = IfThenElse(Boolean(), Boolean(), Boolean())
    assert test_type.validate(True) == True
    assert test_type.validate(False) == True

    test_type = IfThenElse(Boolean(), Integer(), Integer())
    assert test_type.validate(True) == 1
    assert test_type.validate(False) == 1

    test_type = IfThenElse(Boolean(), None, Integer())
    assert test_type.validate(False) == 1

    test_type

# Generated at 2022-06-14 14:17:19.503100
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    from typesystem.fields import String
    assert OneOf([String()]).validate("hello") == "hello"
    assert OneOf([String(), String()]).validate("hello") == "hello"
    assert OneOf([String()]).validate("hello") == "hello"
    # AllOf consists of two String fields
    assert AllOf([String(), String(min_length=4),String()]).validate("hello") == "hello"
    # Field(IfThenElse) determines the error message of the If-clause and the then-clause
    assert IfThenElse(String(),String()).validate("hello") == "hello"
#Unit test for method validate of class AllOf

# Generated at 2022-06-14 14:17:29.595298
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    error_message = "This never validates."
    assert NeverMatch().errors.get('never','None') == error_message
    fields = [NeverMatch(),NeverMatch()]
    assert OneOf(fields).errors.get('multiple_matches','None') == "Matched more than one type."
    assert AllOf(fields).errors == {}
    assert Not(NeverMatch()).errors.get('negated','None') == "Must not match."
    if_clause = NeverMatch()
    then_clause = NeverMatch()
    else_clause = NeverMatch()
    assert IfThenElse(if_clause,then_clause,else_clause).errors == {}


# Generated at 2022-06-14 14:17:36.932149
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    if_clause = IfThenElse(
        if_clause='"hello"',
        then_clause='"hello"',
        else_clause='"hello2"',
    )

    if_clause.validate('"hello"') == '"hello"'
    if_clause.validate('"hello2"') == '"hello2"'
    if_clause.validate('"hello3"') == '"hello2"'



# Generated at 2022-06-14 14:17:56.725411
# Unit test for method validate of class Not
def test_Not_validate():
    class Int(Field):
        """
        Converts an argument to `int`.
        """

        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            try:
                return int(value)
            except ValueError:
                raise self.validation_error("invalid")

    negated = Not(Int(), description="Negated int")
    value = 2
    _, error = negated.validate_or_error(value)
    assert error["code"] == "negated"

# Generated at 2022-06-14 14:17:57.508206
# Unit test for constructor of class AllOf
def test_AllOf():
    pass # TODO


# Generated at 2022-06-14 14:18:08.591880
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    class A:
        pass

    a = A()
    a.x = "foo"
    a.y = "bar"

    if_clause = A()
    if_clause.x = String(min_length=3)
    if_clause.y = String(max_length=3)

    then_clause = A()
    then_clause.x = String(min_length=4)

    else_clause = A()
    else_clause.x = String(min_length=2)
    else_clause.y = String(max_length=4)

    if_then_else = IfThenElse(if_clause, then_clause, else_clause)

    assert if_then_else.validate(a) == a

    a.x = "fo"

# Generated at 2022-06-14 14:18:10.040347
# Unit test for constructor of class OneOf
def test_OneOf():
    test_field = OneOf(one_of=[Boolean()])
    assert test_field


# Generated at 2022-06-14 14:18:11.094441
# Unit test for method validate of class OneOf
def test_OneOf_validate():
  a = OneOf([1,2,3])

# Generated at 2022-06-14 14:18:22.359407
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    class ValidateProtocol:
        def validate(self, value_to_be_validated, strict=False):
            return value_to_be_validated

    class ZeroField:
        def validate(self, value_to_be_validated, strict=False):
            if value_to_be_validated==0:
                return value_to_be_validated
            else:
                raise Exception("The value is bigger than 0")
    class NegativeField:
        def validate(self, value_to_be_validated, strict=False):
            if value_to_be_validated<0:
                return value_to_be_validated
            else:
                raise Exception("The value is not negative")

# Generated at 2022-06-14 14:18:24.958459
# Unit test for constructor of class Not
def test_Not():
    class test(Not):
        def __init__(self,negated):
            super().__init__(negated)
    a = Not(1)
    b = test(1)

# Generated at 2022-06-14 14:18:28.769763
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    """
        Test if the method validate of class IfThenElse validates its inputs as expected
    """
    sweet = IfThenElse(if_clause=Any(description='if clause'), then_clause=Any(description='then clause'), else_clause=Any(description='else clause'),description='description')
    sweet.validate(1)
    sweet.validate(True)
    sweet.validate([1,2,3])
    sweet.validate('hello')
    sweet.validate(0.2)
    sweet.validate({"a":1})

# Generated at 2022-06-14 14:18:29.721722
# Unit test for constructor of class AllOf
def test_AllOf():
    assert AllOf([])


# Generated at 2022-06-14 14:18:34.369140
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    one_of = OneOf([], required=False)
    with pytest.raises(FieldValidationError):
        one_of.validate(None)

    # no_match
    with pytest.raises(FieldValidationError):
        one_of.validate(None)

# Generated at 2022-06-14 14:19:04.759253
# Unit test for constructor of class AllOf
def test_AllOf():
    from typesystem.fields import String
    field1 = String()
    field2 = String()
    field_all = AllOf(all_of=[field1, field2])
    field_all.validate("foo")
    # This will raise an error (or at least it should), because foo is not a parsed JSON dict
    field_all.validate("foo", strict=True)

# Generated at 2022-06-14 14:19:16.345986
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    from typesystem.fields import String
    from typesystem.types import Type
    from typesystem.validators import MaxLength
    from typesystem.validators import MinLength

    def test_IfThenElse_validate_succes(value):
        myType = String(name='myType', validators=[IfThenElse(else_clause=MaxLength(5), if_clause=MinLength(5), then_clause=MaxLength(5))])
        myType.validate(value)
    
    def test_IfThenElse_validate_failure(value):
        myType = String(name='myType', validators=[IfThenElse(else_clause=MaxLength(5), if_clause=MinLength(5), then_clause=MaxLength(5))])

# Generated at 2022-06-14 14:19:16.950961
# Unit test for constructor of class OneOf
def test_OneOf():
    pass

# Generated at 2022-06-14 14:19:19.725042
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    """
    This is a test for the method validate of class IfThenElse
    """
    dic = {'if': {'const': True}, 'then': {'const': 1}}
    f = IfThenElse(**dic)
    assert f._validate() == {'if': {'const': True}, 'then': {'const': 1}}

# Generated at 2022-06-14 14:19:24.953170
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    from typesystem import Integer
    from typesystem import String
    class MyIfThenElse(IfThenElse):
        def __init__(self):
            super().__init__(
                if_clause=Integer(),
                then_clause=String(),
                else_clause=Integer()
            )
    my_ifthenelse = MyIfThenElse()
    result = my_ifthenelse.validate("3")
    assert result == "3"
    result = my_ifthenelse.validate(3)
    assert result == 3

# Generated at 2022-06-14 14:19:31.636642
# Unit test for method validate of class OneOf
def test_OneOf_validate():
	# initialization
	oneOf = OneOf([String(),Number()])
	
	# OneOf should throw error for value that doesn't match any fields in list of fields
	with pytest.raises(Exception):
		res = oneOf.validate("string")

	# OneOf should throw error for value that match multiple fields in list of fields
	with pytest.raises(Exception):
		res = oneOf.validate("string")

	# OneOf should pass for value that matches exactly one field in list of fields
	res = oneOf.validate("string")
	assert res == "string"


# Generated at 2022-06-14 14:19:33.602520
# Unit test for constructor of class Not
def test_Not():
    from typesystem.fields import Integer

    allowed = Not(Integer())
    not_allowed = Not(allowed)
    allowed.validate(123)
    with pytest.raises(Not.ValidationError):
        not_allowed.validate(123)


# Generated at 2022-06-14 14:19:38.021970
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    if_clause=Not(negated = Any())
    then_clause=Not(negated = Any())
    else_clause=Not(negated = Any())
    IfThenElse(if_clause,then_clause,else_clause).validate(value=1)



# Generated at 2022-06-14 14:19:44.126722
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    from typesystem.fields import Integer

    x = Integer(min_value=1)
    y = Integer(max_value=0)
    v = IfThenElse(x, then_clause=y)

    assert v.validate(1) == 1

    try:
        v.validate(2)
        assert False
    except Exception as e:
        assert e.args[0] == 'Max value is 0, got 2.'

# Generated at 2022-06-14 14:19:48.709462
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    test_schema = {'if': {'type': 'string'}, 'then': {'type': 'integer'}, 'else': {'type': 'number'}}
    field = IfThenElse(if_clause=test_schema['if'], then_clause=test_schema['then'], else_clause=test_schema['else'])
    assert field.validate('string test') == 0
    assert field.validate(21) == 21.0

# Generated at 2022-06-14 14:20:02.512689
# Unit test for constructor of class OneOf
def test_OneOf():
    n = OneOf([])
    assert n.one_of == []


# Generated at 2022-06-14 14:20:11.392281
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    # Array Schema with oneOf
    oneOf = [
        {"number": 12},
        {"string": "hi"},
        {"boolean": True}
    ]
    # int type
    assert OneOf(oneOf).validate(12) == 12
    # string type
    assert OneOf(oneOf).validate("hi") == "hi"
    # boolean type
    assert OneOf(oneOf).validate(True) == True
    # error
    try:
        OneOf(oneOf).validate(-0.1)
        assert False
    except Exception as e:
        assert True
    try:
        OneOf(oneOf).validate(False)
        assert False
    except Exception as e:
        assert True



# Generated at 2022-06-14 14:20:13.584931
# Unit test for constructor of class Not
def test_Not():
    test = Not(Any())
    assert(test.negated == Any())

# Generated at 2022-06-14 14:20:22.489289
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    f0 = NeverMatch()
    f1 = NeverMatch()
    f2 = NeverMatch()
    field = OneOf(one_of=[f0, f1, f2])

    with pytest.raises(NeverMatch.validation_error) as e:
        field.validate(None)
    assert e.value.code == "no_match"

    field = OneOf(one_of=[Any()])

    assert field.validate(None) == None

    with pytest.raises(NeverMatch.validation_error) as e:
        field.validate([1, 2, 3])
    assert e.value.code == "multiple_matches"

# Generated at 2022-06-14 14:20:23.904235
# Unit test for constructor of class OneOf
def test_OneOf():
    assert OneOf([Any()])


# Generated at 2022-06-14 14:20:26.642147
# Unit test for constructor of class OneOf
def test_OneOf():
    expected_result = {'one_of': ['a', 'b']}
    actual_result = str(OneOf(['a','b']))
    assert expected_result == actual_result

# Generated at 2022-06-14 14:20:28.109850
# Unit test for constructor of class AllOf
def test_AllOf():
    all_of = AllOf([Any()])
    assert all_of is not None

# Generated at 2022-06-14 14:20:30.596340
# Unit test for constructor of class OneOf
def test_OneOf():
    OneOf([])
    OneOf([Any()])
    OneOf([Any(), Any()])
    OneOf([Any(), Any(), Any()])


# Generated at 2022-06-14 14:20:34.811094
# Unit test for constructor of class OneOf
def test_OneOf():
    # Create an instance of class OneOf
    one_of_field = OneOf([1,2,3])

    assert type(one_of_field) == OneOf
    assert one_of_field is not None


# Generated at 2022-06-14 14:20:35.379699
# Unit test for constructor of class OneOf
def test_OneOf():
	assert OneOf([])

# Generated at 2022-06-14 14:21:02.545797
# Unit test for constructor of class OneOf
def test_OneOf():
    assert OneOf.__doc__


# Generated at 2022-06-14 14:21:03.576690
# Unit test for constructor of class OneOf
def test_OneOf():
    pass


# Generated at 2022-06-14 14:21:11.055997
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    from typesystem.fields import String
    from typesystem.types import Type
    f = IfThenElse(
        if_clause=Type(String(max_length=3), strict=True),
        then_clause=Type(String(max_length=6), strict=True),
        else_clause=Type(String(max_length=9), strict=True),
    )
    f.validate((1, 2, 3, 4, 5, 6), strict=True)
    f.validate((1, 2, 3), strict=True)
    f.validate((1, 2, 3, 4, 5, 6, 7, 8, 9, 0), strict=True)

# Generated at 2022-06-14 14:21:14.619602
# Unit test for constructor of class OneOf
def test_OneOf():
    value_validator = OneOf([], min_length=1, max_length=1)
    assert value_validator.one_of == []
    assert value_validator.min_length == 1
    assert value_validator.max_length == 1


# Generated at 2022-06-14 14:21:22.588665
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    S = IfThenElse
    S('if_clause', 'then_clause', 'else_clause')
    S('if_clause', then_clause = 'then_clause', else_clause = 'else_clause')
    S('if_clause', then_clause = 'then_clause')
    S('if_clause', else_clause = 'else_clause')
    #S('if_clause', 'then_clause', else_clause = 'else_clause')
    #S('if_clause', then_clause = 'then_clause', 'else_clause')

# Generated at 2022-06-14 14:21:25.400873
# Unit test for constructor of class Not
def test_Not():
    not_obj = Not(Any(), description="description")
    assert(not_obj.description == "description")
    assert(not_obj.negated == Any())


# Generated at 2022-06-14 14:21:27.117440
# Unit test for constructor of class OneOf
def test_OneOf():
    test_field = OneOf([Field()])
    assert test_field.one_of == [Field()]


# Generated at 2022-06-14 14:21:28.383137
# Unit test for constructor of class AllOf
def test_AllOf():
    pass # nothing to test, just checking existence and that init is not broken


# Generated at 2022-06-14 14:21:34.712852
# Unit test for constructor of class AllOf
def test_AllOf():
    import sys
    from typesystem.fields import Integer, String
    allFields = [Integer(), String()]
    allFields2 = [Integer(), Integer()]
    allFields3 = [Integer(), String(), Integer()]
    myAllOf = AllOf(allFields)
    myAllOf2 = AllOf(allFields2)
    myAllOf3 = AllOf(allFields3)
    myAllOf.validate(allFields)
    myAllOf2.validate(allFields2)
    myAllOf3.validate(allFields3)

test_AllOf()

# Generated at 2022-06-14 14:21:37.115442
# Unit test for constructor of class OneOf
def test_OneOf():
    assert str(OneOf(one_of = [str])) == "OneOf(one_of=[<class 'str'>])"