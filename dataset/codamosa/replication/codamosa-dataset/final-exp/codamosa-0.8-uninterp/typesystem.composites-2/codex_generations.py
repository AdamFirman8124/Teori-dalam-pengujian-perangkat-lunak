

# Generated at 2022-06-14 14:12:44.962046
# Unit test for constructor of class AllOf
def test_AllOf():
    pass



# Generated at 2022-06-14 14:12:47.311090
# Unit test for method validate of class Not
def test_Not_validate():
    notField = Not(negated=String(max_length=3))
    res = notField.validate('12345')
    assert res == '12345'



# Generated at 2022-06-14 14:12:55.677498
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    from typesystem import Integer, String
    from typesystem.base import ValidationError

    field = IfThenElse(Integer(), String())
    validate(field, 10)
    validate(field, "text")
    with raises(ValidationError) as error:
        field.validate(0.0)
    assert "'0.0' is not a valid string." in error.value.detail
    with raises(ValidationError) as error:
        field.validate("text")
    assert "'text' is not a valid integer." in error.value.detail
    field = IfThenElse(Integer(), String(), String())
    validate(field, "text")
    field = IfThenElse(Integer(), String(), String(), description="Field description")
    assert field.description == "Field description"
    assert field.if_clause.description is None

# Generated at 2022-06-14 14:13:07.471619
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    x = IfThenElse(
            if_clause = Bool(),
            then_clause = String(),
            else_clause = String()
        )
    assert x.validate(True) == True
    assert x.validate("Hello world!") == "Hello world!"
    assert x.validate("Hello world!") == "Hello world!"
    with pytest.raises(x.validation_error):
        assert x.validate(3.14)
    with pytest.raises(x.validation_error):
        assert x.validate(0)
    with pytest.raises(x.validation_error):
        x.validate({})
    with pytest.raises(x.validation_error):
        x.validate([])

# Generated at 2022-06-14 14:13:09.938018
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    import typesystem
    result = IfThenElse(if_clause=typesystem.Boolean(),then_clause=typesystem.DateTime())
    assert result != None


# Generated at 2022-06-14 14:13:11.619198
# Unit test for constructor of class AllOf
def test_AllOf():
    instance = AllOf(all_of=[])
    assert instance
    assert isinstance(instance, Field)


# Generated at 2022-06-14 14:13:14.055829
# Unit test for constructor of class AllOf
def test_AllOf():
    def vi(a):
        return a

    def vi2(a):
        print(a)
        return a

    field = AllOf([vi, vi2])


# Generated at 2022-06-14 14:13:16.635054
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    # TODO: Unit test validation for when all_of matches
    assert True


# Generated at 2022-06-14 14:13:22.369603
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    assert IfThenElse(
        Integer(), Integer(), String(), if_clause=Integer(), 
        then_clause=Integer(), else_clause=String()
    ).validate(10) == 10
    assert IfThenElse(
        Integer(), Integer(), String(), if_clause=Integer(), 
        then_clause=Integer(), else_clause=String()
    ).validate("not number") == "not number"

# Generated at 2022-06-14 14:13:35.679356
# Unit test for method validate of class IfThenElse

# Generated at 2022-06-14 14:13:49.950449
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    def test_body(if_clause, then_clause, else_clause):
        value = 42
        if_clause.validate = Mock()
        then_clause.validate = Mock()
        else_clause.validate = Mock()

        result = IfThenElse(if_clause=if_clause, then_clause=then_clause, else_clause=else_clause)
        result.validate(value)

        if_clause.validate.assert_called_once_with(42, strict=False)
        # Check that then_clause.validate() or else_clause.validate() is called once

# Generated at 2022-06-14 14:13:59.998464
# Unit test for method validate of class Not
def test_Not_validate():
    import typesystem

    class MismatchString(typesystem.String):
        def validate(self, value, strict=False):
            return "asdf"

    class MismatchInteger(typesystem.Integer):
        def validate(self, value, strict=False):
            return "asdf"

    class MismatchFloat(typesystem.Integer):
        def validate(self, value, strict=False):
            return "asdf"

    class MismatchBoolean(typesystem.Boolean):
        def validate(self, value, strict=False):
            return "asdf"

    class MismatchDatetime(typesystem.DateTime):
        def validate(self, value, strict=False):
            return "asdf"

    class TestNot(typesystem.Schema):
        name = typesystem.String()
        age = Not

# Generated at 2022-06-14 14:14:11.158573
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    class Test1(IfThenElse):
        def __init__(self):
            super().__init__(if_clause=Boolean(), then_clause=Integer())
            self.prob_if_clause_is_true = 50

    class Test2(IfThenElse):
        def __init__(self):
            super().__init__(if_clause=Boolean(), then_clause=Integer(min_value=10), else_clause=Integer(max_value=5))
            self.prob_if_clause_is_true = 50


# Generated at 2022-06-14 14:14:24.270212
# Unit test for constructor of class OneOf
def test_OneOf():
    import typesystem
    x = 'x'
    xo = typesystem.OneOf([typesystem.Integer, typesystem.String], x=x)
    assert xo.x == x
    assert xo.errors['no_match'] == 'Did not match any valid type.'
    assert xo.errors['multiple_matches'] == 'Matched more than one type.'
    assert xo.validate(1) is None
    assert xo.validate('a') is None
    assert xo.validate(True) == 'Did not match any valid type.'
    assert xo.validate(1.0) == 'Matched more than one type.'
    assert xo.validate(None, 'not_null') == 'Matched more than one type.'
    assert xo.validate(None) is None

# Unit test

# Generated at 2022-06-14 14:14:33.567469
# Unit test for method validate of class Not
def test_Not_validate():
    """
    Test if the validation method of class Not works as expected.
    """
    from typesystem.types import String
    from typesystem.base import ValidationError

    # Case 1: input value is not equal to the negated value.
    # Expected behaviour: return the input value
    n = Not(String(max_length=4))
    assert n.validate('Hello') == 'Hello'

    # Case 2: input value is equal to the negated value.
    # Expected behaviour: raise ValidationError with given message
    try:
        n.validate('HelloWorld')
    except ValidationError as e:
        assert e.message == 'Must not match.'

# Generated at 2022-06-14 14:14:35.439752
# Unit test for method validate of class Not
def test_Not_validate():
    value=1
    strict=True
    field=Not(value,strict)
    assert field.validate(value,strict)==value


# Generated at 2022-06-14 14:14:48.060364
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    import json
    from typesystem.validators import OneOf
    from typesystem.base import ValidationError


    class DataField(OneOf):
        def validate(self, value):
            if value == "ERROR":
                raise ValidationError("custom error")
            return super().validate(value)

    class DataField1(OneOf):
        def validate(self, value):
            if value == "ERROR":
                raise ValidationError("custom error")
            return super().validate(value)

    class DataField2(OneOf):
        def validate(self, value):
            if value == "ERROR":
                raise ValidationError("custom error")
            return super().validate(value)


# Generated at 2022-06-14 14:14:51.389232
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    field = IfThenElse(
        String(title="If"),
        String(title="Then"),
        String(title="Else"),
    )
    assert field.validate("else") == "else"

# Generated at 2022-06-14 14:15:03.445923
# Unit test for method validate of class Not
def test_Not_validate():
    import unittest
    import boolean

    class Not(Field):
        """
        Must match all of the sub-items.

        You should use custom validation instead.
        """

        errors = {"negated": "Must not match."}

        def __init__(self, negated: Field, **kwargs: typing.Any) -> None:
            assert "allow_null" not in kwargs
            super().__init__(**kwargs)
            self.negated = negated

        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            _, error = self.negated.validate_or_error(value, strict=strict)
            if error:
                return value
            raise self.validation_error("negated")



# Generated at 2022-06-14 14:15:04.051525
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    pass


# Generated at 2022-06-14 14:15:08.913974
# Unit test for constructor of class Not
def test_Not():
    not_ = Not(negated=Boolean(), description="a", nullable=True, name="b")
    assert not_.name == "b"
    assert not_.description == "a"
    assert not_.nullable == True

# Generated at 2022-06-14 14:15:11.836475
# Unit test for constructor of class Not
def test_Not():
    s = Not(Any())
    s.validate(None)
    with pytest.raises(schema.ValidationError):
        s.validate(False)

# Generated at 2022-06-14 14:15:21.921218
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    from typesystem.fields import String, Integer
    from typesystem import Field

    # Given
    string_field = String()
    integer_field = Integer()
    one_of_field = OneOf([string_field, integer_field], label="oneOf_field")

    # When
    string_input = "A string value"
    integer_input = 123
    bool_input = True
    string_output = one_of_field.validate(string_input)
    integer_output = one_of_field.validate(integer_input)

    # Then
    assert not isinstance(string_output, Field)
    assert isinstance(integer_output, Field)


# Generated at 2022-06-14 14:15:32.276812
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    import unittest

    class IfThenElseTests(unittest.TestCase):
        def test_IfThenElse(self):
            import json

            class Person(types.Type):
                name = types.String()
                age = types.Integer(min_value=15)
                is_child = types.Boolean()


# Generated at 2022-06-14 14:15:33.604233
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    assert Field(one_of=[Boolean()]).validate(True) == True

# Generated at 2022-06-14 14:15:36.620398
# Unit test for method validate of class Not
def test_Not_validate():
    not1 = Not(infer)
    assert not1.validate(None) == None


# Generated at 2022-06-14 14:15:38.681377
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
  field = typesystem.fields.NeverMatch()
  assert field is not None


# Generated at 2022-06-14 14:15:39.518658
# Unit test for constructor of class Not
def test_Not():
    assert Not(Any())

# Generated at 2022-06-14 14:15:40.660634
# Unit test for constructor of class OneOf
def test_OneOf():
    field = OneOf([])
    assert field



# Generated at 2022-06-14 14:15:43.049388
# Unit test for method validate of class Not
def test_Not_validate():
    field = Not(Any())
    value = None
    result = field.validate(value, strict=False)
    assert result == value


# Generated at 2022-06-14 14:15:51.351422
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    field = OneOf(one_of=[Any()], name="OneOf")
    field.validate(value=1)
    field.validate(value=2)
    field.validate(value=None)
    field.validate(value="")
    field.validate(value=False)
    field.validate(value=True)

# Generated at 2022-06-14 14:15:57.767923
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    # Test case 1:
    # constructor:
    # def __init__(self, one_of: typing.List[Field], **kwargs: typing.Any) -> None:
    field = OneOf([Int()], name="OneOf test")
    # validate:
    # def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
    field.validate(2)
    try:
        field.validate("invalid")
        assert False
    except:
        pass
    # unit test ends.


# Generated at 2022-06-14 14:16:09.032852
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    if_clause = fields.Dict({"a": fields.String()})
    then_clause = fields.Dict({"b": fields.String()})
    else_clause = fields.Dict({"c": fields.String()})
    ite_field = fields.IfThenElse(if_clause, then_clause, else_clause)
    input1 = {"a": "Test", "b": "Test2"}
    output1 = ite_field.validate(input1)
    assert output1["a"] == "Test"
    input2 = {"c": "Test"}
    output2 = ite_field.validate(input2)
    assert output2["c"] == "Test"
    input3 = {"d": "Test"}
    output3 = ite_field.validate(input3)

# Generated at 2022-06-14 14:16:15.492866
# Unit test for constructor of class NeverMatch
def test_NeverMatch():

    # Initialization of NeverMatch object
    never_match = NeverMatch()

    # The errors attribute must be a dictionary
    assert type(never_match.errors) == dict

    # The errors dictionary must have the key "never"
    assert 'never' in never_match.errors

    # The value associated with the key "never" must be "This never validates."
    assert never_match.errors['never'] == "This never validates."

# Generated at 2022-06-14 14:16:23.866647
# Unit test for method validate of class OneOf
def test_OneOf_validate():

    # == test field by field
    # oneOf_schema_1 = OneOf([{'type': 'integer'}, {'type': 'number'}])
    oneOf_schema_1 = OneOf([Field('integer'), Field('number')])
    try:
        oneOf_schema_1.validate(1)
    except:
        raise
    try:
        oneOf_schema_1.validate(1.1)
    except:
        raise
    try:
        oneOf_schema_1.validate(oneOf_schema_1)
    except Exception as e:
        print(e)
        pass

    # == test oneOf_schema_2
    # oneOf_schema_2 = OneOf([
    #     {'type': 'integer', 'minimum': 1, 'maximum

# Generated at 2022-06-14 14:16:26.999297
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    field = OneOf([Integer(name="one"), Integer(name="two")])
    assert 3 == field.validate(3)

    with pytest.raises(ValidationError):
        field.validate("oh")

# Generated at 2022-06-14 14:16:35.312592
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    """Test validate() of IfThenElse"""

    import typesystem
    from typesystem.errors import ValidationError

    class PositiveInt(typesystem.Integer):
        min_value = 0
    
    class NegativeInt(typesystem.Integer):
        max_value = 0
    
    class IfThenElseField(typesystem.IfThenElse):
        def __init__(self):
            super().__init__(
                if_clause = PositiveInt(),
                then_clause = typesystem.Float(),
                else_clause = NegativeInt()
            )
    
    if_then_else_field = IfThenElseField()

    assert if_then_else_field.validate(5) == 5.0
    assert if_then_else_field.validate(-5) == -5


# Generated at 2022-06-14 14:16:36.059160
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    pass

# Generated at 2022-06-14 14:16:37.220838
# Unit test for constructor of class Not
def test_Not():
    assert isinstance(Not(Any()), Field)

# Generated at 2022-06-14 14:16:40.372105
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    IfThenElse(
        if_clause = Any(),
        then_clause = Any(),
        else_clause = Any(),
    ).validate(value=1)


# Generated at 2022-06-14 14:16:51.725816
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    a = IfThenElse(if_clause=String(), then_clause=Any())
    assert a.validate(1) == 1
    a = IfThenElse(if_clause=String(), else_clause=Any())
    assert a.validate('1') == '1'
    a = IfThenElse(if_clause=String(), then_clause=Integer(), else_clause=Any())
    assert a.validate('1') == 1
    a = IfThenElse(if_clause=String(), then_clause=String(), else_clause=Any())
    assert a.validate(1) == 1

# Generated at 2022-06-14 14:16:58.055483
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    class Estudiante:
        def __init__(self, edad:int, numero_de_materias_aprobadas:int, numero_de_materias_reprobadas:int, promedio_de_calificaciones:float, estado:str="regular"):
            self.edad=edad
            self.numero_de_materias_aprobadas=numero_de_materias_aprobadas
            self.numero_de_materias_reprobadas=numero_de_materias_reprobadas
            self.promedio_de_calificaciones=promedio_de_calificaciones
            self.estado=estado
    Field.register_field(IfThenElse)

    estudiante_if

# Generated at 2022-06-14 14:17:01.017018
# Unit test for constructor of class Not
def test_Not():
    # Setup
    negated = "int"
    
    # Exercise
    target = Not(negated)

    # Verify
    assert target.negated == negated


# Generated at 2022-06-14 14:17:09.067308
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    if_clause = Field(name="if_clause")
    then_clause = Field(name="then_clause")
    else_clause = Field(name="else_clause")
    if_then_else = IfThenElse(if_clause, then_clause, else_clause)

    assert if_then_else.if_clause == if_clause
    assert if_then_else.then_clause == then_clause
    assert if_then_else.else_clause == else_clause

# Generated at 2022-06-14 14:17:18.223973
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    # Test for regular constructor
    if_clause = Field(name="test1")
    then_clause = Field(name="test2")
    else_clause = Field(name="test3")
    if_then_else = IfThenElse(if_clause, then_clause, else_clause, name="test")
    assert if_then_else.if_clause == if_clause
    assert if_then_else.then_clause == then_clause
    assert if_then_else.else_clause == else_clause

    # Test for constructor when then_clause is None
    if_clause = Field(name="test1")
    else_clause = Field(name="test3")

# Generated at 2022-06-14 14:17:20.846816
# Unit test for constructor of class AllOf
def test_AllOf():
    a = AllOf(all_of=[])
    assert a.all_of == []


# Generated at 2022-06-14 14:17:21.758650
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    field = NeverMatch()
    assert field.errors == {"never": "This never validates."}


# Generated at 2022-06-14 14:17:29.458504
# Unit test for method validate of class Not
def test_Not_validate():
    from typesystem.fields import Boolean
    from typesystem import ErrorMessage

    not_boolean = Not(Boolean())

    # test "if error:"
    value, error = not_boolean.validate_or_error("garbage")
    assert not error
    assert value == "garbage"

    # test "else:"
    value, error = not_boolean.validate_or_error(True)
    assert isinstance(error, ErrorMessage)
    assert error.code == "negated"
    assert value is None


# Generated at 2022-06-14 14:17:30.757410
# Unit test for method validate of class Not
def test_Not_validate():
    Not({}).validate(None)


# Generated at 2022-06-14 14:17:40.351090
# Unit test for constructor of class Not
def test_Not():
    def test_negated():
        not_bool = Not(allowed_types=bool)
        assert not_bool.validate(True) is None
        assert not_bool.validate(False) is None

    def test_none():
        not_none = Not(allow_none=True)
        assert not_none.validate(None)

    def test_disallow_none():
        not_none = Not(allow_none=False)
        assert not_none.validate(None) is None

    test_negated()
    test_none()
    test_disallow_none()


# Generated at 2022-06-14 14:17:46.750759
# Unit test for constructor of class Not
def test_Not():
    from typesystem.fields import String

    assert Not(String())

# Generated at 2022-06-14 14:17:54.484821
# Unit test for method validate of class Not
def test_Not_validate():
    not1 = Not(String())
    not2 = Not(Integer())
    
    with pytest.raises(Exception) as excinfo:
        not1.validate("123")
    assert excinfo.type == Exception
    assert excinfo.value.args[0] == "Must not match."
    
    with pytest.raises(Exception) as excinfo:
        not2.validate(123)
    assert excinfo.type == Exception
    assert excinfo.value.args[0] == "Must not match."
    
    not1.validate(123)
    not2.validate("123")


# Generated at 2022-06-14 14:17:55.708145
# Unit test for constructor of class AllOf
def test_AllOf():
    tp = AllOf(all_of=None)
    assert tp

# Generated at 2022-06-14 14:17:57.147334
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    ifThenElse = IfThenElse(AllOf([Field()]))
    assert ifThenElse


# Generated at 2022-06-14 14:18:00.680074
# Unit test for method validate of class Not
def test_Not_validate():
    class Type_1(Field):
        pass

    a=Type_1()
    b=Not(a)
    result=b.validate("hello")
    assert result=="hello"

# Generated at 2022-06-14 14:18:05.438112
# Unit test for method validate of class Not
def test_Not_validate():
    field1 = Field()
    field2 = Not(field1)

    # value is None
    error = field2.validate(None)
    assert error
    assert error.code == 'required'
    error = field1.validate(None)
    assert error
    assert error.code == 'required'



# Generated at 2022-06-14 14:18:10.523701
# Unit test for constructor of class OneOf
def test_OneOf():

    field = OneOf([Any(), Any()], description="test")
    assert field.description == "test"

    field = OneOf([Any(), Any()], allow_null=True)
    assert field.description == ""

    field = OneOf([Any(), Any()])
    assert field.description == ""

    for _ in range(5):
        field = OneOf([Any(), Any()], foo='test')
        assert field.foo == 'test'



# Generated at 2022-06-14 14:18:11.376829
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    assert NeverMatch()


# Generated at 2022-06-14 14:18:17.826440
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    def test_error():
        strict = False
        value = "value"
        if_clause = Field()
        then_clause = Field()
        else_clause = Field()
        with pytest.raises(Exception) as excinfo:
            IfThenElse(if_clause, then_clause, else_clause).validate(value, strict)
        assert str(excinfo.value) == "This field is required."


# Generated at 2022-06-14 14:18:24.909560
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    import typesystem
    class TestClass_IfThenElse_validate(typesystem.Schema):
        test_field = IfThenElse(if_clause=int, then_clause=int, else_clause=int)
    test_field = IfThenElse(if_clause=int, then_clause=int, else_clause=int)
    assert test_field.validate(1) == 1
    assert test_field.validate(1.0) == 1.0


# Generated at 2022-06-14 14:18:30.775844
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    ite=IfThenElse(1,1)
    assert ite.if_clause==1
    assert ite.then_clause==1
    assert ite.else_clause==Any()

# Generated at 2022-06-14 14:18:31.319904
# Unit test for constructor of class OneOf
def test_OneOf():
    pass

# Generated at 2022-06-14 14:18:42.256299
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    class Fruit(Field):
        pass
    orange = Fruit(name="orange")
    pear = Fruit(name="pear")
    banana = Fruit(name="banana")
    apple = Fruit(name="apple")
    fruit_tree = IfThenElse(
        if_clause=pear, then_clause=orange, else_clause=apple
    )
    orange.validate(pear.validate("orange")) # If-clause matches
    assert fruit_tree.validate("orange") == orange.validate("orange")
    assert fruit_tree.validate("apple") == apple.validate("apple")
    assert fruit_tree.validate("banana") == banana.validate("banana")
    assert fruit_tree.validate("apple") == Fruit(name="apple").validate("apple")
    assert fruit_

# Generated at 2022-06-14 14:18:53.401092
# Unit test for constructor of class OneOf
def test_OneOf():
    from typesystem.fields import String
    from typesystem.types import Error

    # Matches first type.
    validator = OneOf([String(), String()])
    assert validator.validate("test") == "test"

    # Raises if more than one matches.
    validator = OneOf([String(), String()])
    try:
        validator.validate("test")
    except Error as error:
        assert error.code == "multiple_matches"

    # Raises if no type matches.
    validator = OneOf([String(), String()])
    try:
        validator.validate(123)
    except Error as error:
        assert error.code == "no_match"



# Generated at 2022-06-14 14:18:54.372092
# Unit test for constructor of class AllOf
def test_AllOf():
    try:
        AllOf([1])
    except:
        pass
    else:
        assert False, "Should have raised an exception at this point"


# Generated at 2022-06-14 14:18:55.361875
# Unit test for constructor of class AllOf
def test_AllOf():
    test = AllOf("test")


# Generated at 2022-06-14 14:18:57.733463
# Unit test for constructor of class AllOf
def test_AllOf():
    f1 = AllOf(["a", "b"])
    assert f1.label == "AllOf"
    assert f1.help_text == ""
    assert f1.required is True
    assert f1.read_only is False


# Generated at 2022-06-14 14:19:01.260299
# Unit test for constructor of class OneOf
def test_OneOf():
    one = OneOf([Field()], name="OneOf")
    print(one)


# Generated at 2022-06-14 14:19:04.976572
# Unit test for method validate of class Not
def test_Not_validate():
    test_class = Not(negated=String())
    test_class.validate([])
    try:
        test_class.validate('')
    except:
        pass
    else:
        assert()

# Generated at 2022-06-14 14:19:05.897978
# Unit test for constructor of class AllOf
def test_AllOf():
    a = AllOf([])


# Generated at 2022-06-14 14:19:17.890015
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    # Arrange
    if_clause = String()
    then_clause = String()
    else_clause = String()

    # Act
    IfThenElse(if_clause, then_clause, else_clause)

# Generated at 2022-06-14 14:19:20.026346
# Unit test for method validate of class Not
def test_Not_validate():
    validate_expected = "Must not match."
    assert (Not(None).validate("", strict=False) == validate_expected)



# Generated at 2022-06-14 14:19:25.941054
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    from typesystem import Integer
    from typesystem.fields import String
    ite = IfThenElse(Integer(minimum=0, maximum=10), String(min_length=1, max_length=10))
    assert ite.if_clause.minimum == 0
    assert ite.if_clause.maximum == 10
    assert isinstance(ite.if_clause, Integer)
    assert ite.then_clause.min_length == 1
    assert ite.then_clause.max_length == 10
    assert isinstance(ite.then_clause, String)
    assert isinstance(ite.else_clause, Any)

# Generated at 2022-06-14 14:19:27.550064
# Unit test for constructor of class Not
def test_Not():
    not_required_field = Not(field=Integer(required=True))
    not_required_field.validate("a")

# Generated at 2022-06-14 14:19:29.054790
# Unit test for constructor of class OneOf
def test_OneOf():
    f = OneOf([str])
    f.validate('hello')


# Generated at 2022-06-14 14:19:33.134581
# Unit test for constructor of class OneOf
def test_OneOf():
    # None of the required subfields contain this string
    x = OneOf([Field(description='x'), Field(description='y')])
    # In this case an exception would be thrown because none of the subfields
    # contain this string
    # This field is optional, so it can be empty
    try:
        x.validate('')
    except Exception as e:
        assert type(e) != Exception

# Generated at 2022-06-14 14:19:39.537631
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    class TestIfThenElse(IfThenElse):
        def __init__(self, if_clause: Field=None, then_clause: Field=None, else_clause: Field=None):
            super().__init__(if_clause, then_clause, else_clause)

    assert TestIfThenElse(
        if_clause=Field(), then_clause=Field(), else_clause=Field()
    ).validate("test") == "test"

# Generated at 2022-06-14 14:19:40.367275
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    pass

# Generated at 2022-06-14 14:19:42.716767
# Unit test for constructor of class Not
def test_Not():
    from typesystem.fields import String

    notString = Not(String())
    assert notString.negated == String()


# Generated at 2022-06-14 14:19:44.661278
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    a = OneOf([StringField()])
    try:
        a.validate("123")
    except Exception:
        pass



# Generated at 2022-06-14 14:20:13.896135
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    from typesystem.base import List
    from typesystem.fields import Integer
    from typesystem.fields import String
    from typesystem.fields import Boolean
    # An integer field with a maximum value of 10
    sub_field_1 = Integer(maximum=10)
    # A Boolean field
    sub_field_2 = Boolean()
    # A field with sub_fields
  
    sub_list_1 = List(sub_field_1)
    sub_list_2 = List(sub_field_2)
    sub_list_3 = List(sub_field_2)
    # The field with one clause and the other clause with a default
    if_then_else = IfThenElse(sub_list_1, sub_list_2)
    # The field with two clauses

# Generated at 2022-06-14 14:20:14.619136
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    assert True

# Generated at 2022-06-14 14:20:25.364666
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    # trivial case
    if_clause = Any()
    then_clause = Any()
    else_clause = Any()
    if_else = IfThenElse(if_clause=if_clause,then_clause=then_clause,else_clause=else_clause)
    result = if_else.validate(1)
    assert result == 1
    # if-clause is ok
    if_clause = Any()
    then_clause = then_clause = Field() # no validate method
    else_clause = Any()
    if_else = IfThenElse(if_clause=if_clause,then_clause=then_clause,else_clause=else_clause)
    result = if_else.validate(1)
    assert result == 1
    # if-

# Generated at 2022-06-14 14:20:34.773660
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    class IfClause(Field):
        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            return value == 2
    class ThenClause(Field):
        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            return value == 4
    class ElseClause(Field):
        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            return value == 1
    
    assert IfThenElse(IfClause(), ThenClause(), ElseClause()).validate(2) == True
    assert IfThenElse(IfClause(), ThenClause(), ElseClause()).validate(1) == True
    assert IfThenElse(IfClause(), ThenClause(), ElseClause()).validate(3) == False

# Generated at 2022-06-14 14:20:38.271662
# Unit test for constructor of class OneOf
def test_OneOf():
    assert OneOf([],error_messages={'no_match': 'Did not match any valid type.', 'multiple_matches': 'Matched more than one type.'}) is not None   


# Generated at 2022-06-14 14:20:40.145963
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    n = NeverMatch()
    assert(n.errors_map == {"never": "This never validates."})


# Generated at 2022-06-14 14:20:42.122747
# Unit test for method validate of class Not
def test_Not_validate():
    schema = Not(Integer())
    assert schema.validate(10)
    try:
        schema.validate(1)
    except ValueError as e:
        assert str(e) == "Must not match."


# Generated at 2022-06-14 14:20:52.331415
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    def get_test_case_1():  
        """Not return value when error on if clause"""
        if_clause = Field()
        then_clause = Field()
        else_clause = Field()
        f = IfThenElse(if_clause, then_clause, else_clause)
        return f._validate(value = 0, strict = True)
    
    def get_test_case_2():  
        """Return value when error on if clause"""
        if_clause = Field()
        then_clause = Field()
        else_clause = Field()
        f = IfThenElse(if_clause, then_clause, else_clause)
        return f._validate(value = 0, strict = False)


    result_1 = get_test_case_1()
    result_

# Generated at 2022-06-14 14:20:54.296886
# Unit test for constructor of class Not
def test_Not():
    part = Not(
        negated=Boolean()
    )
    assert part.negated.validate(False) == False


# Generated at 2022-06-14 14:20:55.868350
# Unit test for constructor of class Not
def test_Not():
    from typesystem import Integer
    from typesystem.fields import Not
    assert Not(Integer(min_value=0))



# Generated at 2022-06-14 14:21:29.200641
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    # Check valid case
    testIfThenElse = IfThenElse(AllOf([Any()]))
    testIfThenElse.validate(1)
    # Check invalid case
    try:
        testIfThenElse.validate("a")
    except ValidationError:
        pass
    else:
        assert 0, "fail"

if __name__ == "__main__":
    test_IfThenElse_validate()

# Typedef for validator to be used for validation of integer fields
NumberValidator = typing.Union[
    int,
    float,
]


# Generated at 2022-06-14 14:21:31.769408
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    try:
        err = "This never validates."
        a = NeverMatch(errors = {"never": err})
        assert a.errors["never"] == err
    except Exception as e:
        print(e)
        assert False


# Generated at 2022-06-14 14:21:32.801346
# Unit test for constructor of class OneOf
def test_OneOf():
    assert OneOf


# Generated at 2022-06-14 14:21:35.754535
# Unit test for constructor of class AllOf
def test_AllOf():
    List = typing.List
    str = str
    all_of = [str]
    field = AllOf(all_of)
    assert field.all_of == [str]



# Generated at 2022-06-14 14:21:36.798615
# Unit test for constructor of class AllOf
def test_AllOf():
    AllOf([])


# Generated at 2022-06-14 14:21:38.668673
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    print("test_NeverMatch")
    f = NeverMatch()
    print(f)
    print(repr(f))


# Generated at 2022-06-14 14:21:39.484786
# Unit test for constructor of class AllOf
def test_AllOf():
    allof = AllOf([])


# Generated at 2022-06-14 14:21:43.937947
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    try:
        test = IfThenElse(1)
        assert False
    except AssertionError as e:
        pass

    try:
        test = IfThenElse(1, allow_null=1)
        assert False
    except AssertionError as e:
        pass
    assert True



# Generated at 2022-06-14 14:21:45.936442
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    bad_field = NeverMatch()
    assert bad_field.validate(5) == bad_field.validation_error("never")


# Generated at 2022-06-14 14:21:55.220301
# Unit test for constructor of class AllOf
def test_AllOf():
    fv = FieldValidator()
    fv.register_field_validator('AllOf', AllOf)
    with pytest.raises(TypeError) as excinfo:
        f = AllOf(all_of=[String()], allow_null=False, description="", label="", name="")
    assert 'AllOf() got an unexpected keyword argument' in str(excinfo.value)
    with pytest.raises(TypeError) as excinfo:
        f = AllOf(all_of=[String()], allow_empty=False, description="", label="", name="")
    assert 'AllOf() got an unexpected keyword argument' in str(excinfo.value)