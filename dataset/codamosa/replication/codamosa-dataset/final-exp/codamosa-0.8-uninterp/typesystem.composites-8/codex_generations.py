

# Generated at 2022-06-14 14:12:48.152547
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    ite = IfThenElse(Any(), String(), String())
    result = ite.validate(1)
    assert result == '1'
    result = ite.validate('1')
    assert result == '1'
    result = ite.validate(True)
    assert result == 'True'
    result = ite.validate(False)
    assert result == 'False'


# Generated at 2022-06-14 14:12:49.075073
# Unit test for constructor of class OneOf
def test_OneOf():
    OneOf()

# Generated at 2022-06-14 14:12:50.483727
# Unit test for constructor of class OneOf
def test_OneOf():
    one_of = OneOf([])
    assert one_of is not None

# Generated at 2022-06-14 14:12:55.480148
# Unit test for method validate of class Not
def test_Not_validate():
    field = Not(Negated=String())
    value = "test_Not_validate"
    field.validate(value)

    field2 = Not(Negated=Integer())
    try:
        field2.validate(value)
    except FieldValidationError as error:
        assert error.field == field2
        assert error.message == "Must not match."
        assert error.value == value



# Generated at 2022-06-14 14:13:07.615587
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    from typesystem.fields import Integer, Union

    # TODO: These tests are not exhaustive.


# Generated at 2022-06-14 14:13:08.583910
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    f = NeverMatch()
    assert isinstance(f, Field)

# Generated at 2022-06-14 14:13:11.046670
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    n = NeverMatch(title="Title", description="Description")
    assert n.errors == {"never": "This never validates."}

# Unit tests for constructor of class OneOf

# Generated at 2022-06-14 14:13:18.666800
# Unit test for method validate of class Not
def test_Not_validate():
    error_message = "Must not match."
    assert error_message == Not(Any()).validate_error(None)
    assert error_message == Not(Any()).validate_error(False)
    assert error_message == Not(Any()).validate_error(True)
    assert error_message == Not(Any()).validate_error(1)
    assert error_message == Not(Any()).validate_error(3.14)
    assert error_message == Not(Any()).validate_error("")
    assert error_message == Not(Any()).validate_error("string")
    assert error_message == Not(Any()).validate_error([])
    assert error_message == Not(Any()).validate_error({})

# Generated at 2022-06-14 14:13:20.794662
# Unit test for constructor of class Not
def test_Not():
    x  = Not(Any())
    assert x.negated.allow_null == True

# Generated at 2022-06-14 14:13:33.404883
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    #Test that the validation works as expected when exactly one of the sub-items match
    if_clause = Field()
    then_clause = Field()
    else_clause = Field()
    if_then_else = IfThenElse(if_clause, then_clause, else_clause)

    assert if_then_else.validate(2) == 2
    #Test that the validation works when more than one of the sub-items match
    if_clause = Field()
    then_clause = Field()
    else_clause = Field()
    if_then_else2 = IfThenElse(if_clause, then_clause, else_clause)

    assert if_then_else2.validate(2) == 2

    #Test that the validation works when none of the sub-items match
    if_cl

# Generated at 2022-06-14 14:13:42.582398
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    val = 4
    obj = IfThenElse(IfThenElse(Any(), Any()), Any())
    assert obj.validate(val, strict = True) == val
    # the else_clause of the outer if_then_else should be executed
    # given that the if_clause of the inner if_then_else is false
    val = ''
    obj = IfThenElse(IfThenElse(Any(), Any()), Any())
    assert obj.validate(val, strict = True) == val
    # the if_clause of the inner if_then_else should be executed
    # given that the if_clause of the outer if_then_else is true
    # and the if_clause of the inner if_then_else should be true
    val = 4

# Generated at 2022-06-14 14:13:44.864404
# Unit test for method validate of class Not
def test_Not_validate():
    testInstance = Not(Any())
    assert testInstance.validate(1) is None
    assert testInstance.validate(2) is None

# Generated at 2022-06-14 14:13:45.486820
# Unit test for method validate of class Not
def test_Not_validate():
    assert True

# Generated at 2022-06-14 14:13:48.559781
# Unit test for method validate of class Not
def test_Not_validate():
    value = [1,2,3]
    not_field = Not(negated=Array())
    assert not_field.validate(value) == value

# Generated at 2022-06-14 14:13:55.923864
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    from typesystem.fields import String

    if_clause = String(max_length=3)
    then_clause = String(min_length=10)
    else_clause = String(max_length=3)
    test_case = IfThenElse(if_clause, then_clause, else_clause)

    validation_error, error = test_case.validate_or_error("aa")
    assert error is None
    assert validation_error == "aa"

    validation_error, error = test_case.validate_or_error("aaaa")
    assert error is None
    assert validation_error == "aaaa"

    validation_error, error = test_case.validate_or_error("aaaaaaaaaa")
    assert error is None
    assert validation_error == "aaaaaaaaaa"

    validation_error,

# Generated at 2022-06-14 14:14:01.548152
# Unit test for method validate of class Not
def test_Not_validate():
    f = Not(Integer())
    v = f.validate(1)
    assert v == 1
    try:
        v = f.validate(1.1)
        assert True == False
    except ValidationError as e:
        v = f.validate(1)


# Generated at 2022-06-14 14:14:07.383958
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    field_1 = IfThenElse(Any(), Any())

    assert field_1.validate(1) == 1

    field_2 = IfThenElse(int, int)

    try:
        field_2.validate(1.0)
    except ValidationError as e:
        assert e.messages['if_clause'][0] == 'Must be an integer.'

# Generated at 2022-06-14 14:14:12.349785
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    field = OneOf([])
    with pytest.raises(FieldError) as excinfo:
        field.validate(None)
    assert excinfo.value.code == "no_match"

    field = OneOf([Integer()])
    value, error = field.validate_or_error(None)
    assert value == None
    assert error == None


# Generated at 2022-06-14 14:14:25.267659
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    #declaring field variables
    class Int(Field):
        errors = {"invalid": "Must be an integer."}
        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            try:
                return int(value)
            except ValueError:
                raise self.validation_error("invalid")
    #declaring field variables
    class Neg(Field):
        errors = {"invalid": "Must be an integer."}
        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            try:
                return bool(int(value) < 0)
            except ValueError:
                raise self.validation_error("invalid")

    #declaring field variables
    class Str(Field):
        errors = {"invalid": "Must be a string."}

# Generated at 2022-06-14 14:14:27.219377
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    nm = NeverMatch()
    assert nm


# Generated at 2022-06-14 14:14:34.131395
# Unit test for constructor of class OneOf
def test_OneOf():
    #This is a correct initialization
    a = OneOf([Field])
    assert a is not None
    assert type(a) is OneOf
    #The constructor should not work with invalid input
    try:
        a = OneOf([4,4])
    except AssertionError as e:
        assert str(e) == "The constructor of OneOf should take a list of fields as argument"


# Generated at 2022-06-14 14:14:35.906407
# Unit test for constructor of class Not
def test_Not():
    not_object = Not(negated=Field(type="integer"))

    assert not_object.negated.type == "integer"


# Generated at 2022-06-14 14:14:37.173697
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    assert NeverMatch(label="dont_use_this", description="because_it_never_matches")


# Generated at 2022-06-14 14:14:43.742239
# Unit test for constructor of class AllOf
def test_AllOf():
    from typesystem.fields import String
    expected_all_of = ["test_AllOf", "test_AllOf"]
    a = AllOf(all_of=[String(), String()])
    assert a.all_of == expected_all_of
    assert a.name == None



# Generated at 2022-06-14 14:14:50.237886
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    field_one_of = OneOf(
        one_of=[String(), String()],
        description="This description is not used.",
        title="This title is not used.",
        enum=["b", "a"],
        min_length=1,
        max_length=10,
    )
    assert field_one_of.validate("a") == "a"
    assert field_one_of.validate("b") == "b"
    assert field_one_of.validate("c") == None


# Generated at 2022-06-14 14:14:50.792054
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    pass

# Generated at 2022-06-14 14:14:54.435569
# Unit test for constructor of class AllOf
def test_AllOf():
    from typesystem.types import String
    test_value = 'test'
    test_object = AllOf([String()])
    assert test_object.validate(test_value) == 'test'

# Generated at 2022-06-14 14:14:55.041506
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    pass

# Generated at 2022-06-14 14:14:57.016078
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    obj = IfThenElse(if_clause = 'a')
    assert obj == None

# Generated at 2022-06-14 14:14:59.640148
# Unit test for constructor of class Not
def test_Not():
    negated = type("n", (Field,), {})()
    not_field = Not(negated)
    assert not_field.negated is negated

# Generated at 2022-06-14 14:15:07.136814
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    # setup
    field = OneOf([
        Field(type="number")
    ])

    # test and verify
    with pytest.raises(Exception):
        field.validate(1)



# Generated at 2022-06-14 14:15:12.638495
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    one_of = OneOf([Float(), Int()])
    assert(one_of.validate(1.0) == 1.0)
    assert(one_of.validate(1) == 1)
    try:
        one_of.validate("Not an Int or Float")
        assert(False)
    except ValidationError:
        assert(True)
    try:
        one_of.validate("Not an Int or Float", True)
        assert(False)
    except ValidationError:
        assert(True)
    

# Generated at 2022-06-14 14:15:14.739637
# Unit test for constructor of class OneOf
def test_OneOf():
    oneOf = OneOf(one_of=[Exact, Integer])
    print(oneOf)


# Generated at 2022-06-14 14:15:20.273026
# Unit test for method validate of class Not
def test_Not_validate():
    assert Not(negated=Any()).validate(0) == 0
    try:
        Not(negated=Any()).validate(None)
        assert False
    except:
        pass
    try:
        Not(negated=Any()).validate("bad_data")
        assert False
    except:
        pass


# Generated at 2022-06-14 14:15:22.742706
# Unit test for method validate of class Not
def test_Not_validate():
    not_parser = Not(Integer())
    not_parser.validate(2.0)

# Generated at 2022-06-14 14:15:24.757422
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    field = NeverMatch()
    assert field.__class__.__name__ == 'NeverMatch'


# Generated at 2022-06-14 14:15:30.492568
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    field = OneOf(one_of = [] )
    field.validate([])
    field = OneOf(one_of = [ 'str' ] )
    field.validate(['str'])
    field = OneOf(one_of = [ 'str', 'str' , 'str' ] )
    field.validate(['str', 'str' , 'str'])
    field.validate(None)


# Generated at 2022-06-14 14:15:34.874669
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    one_of = OneOf(one_of = [Field(default='f')])
    assert one_of.validate('f') == 'f'

    one_of = OneOf(one_of = [Field(default='f1'), Field(default='f2')])
    assert one_of.validate('f1') == 'f1'
    assert one_of.validate('f2') == 'f2'


# Generated at 2022-06-14 14:15:38.647415
# Unit test for method validate of class Not
def test_Not_validate():
    from typesystem.base import Message
    from typesystem.fields import Integer, String

    f = Not(String(min_length=4))
    value, error = f.validate_or_error(1)
    assert value == 1
    assert error is None

    value, error = f.validate_or_error("a")
    assert error == Message("negated")


# Generated at 2022-06-14 14:15:40.669970
# Unit test for constructor of class OneOf
def test_OneOf():
    a = OneOf([])
    assert isinstance(a, OneOf)

    b = OneOf([])
    assert b is not None


# Generated at 2022-06-14 14:15:56.261141
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    def test_OneOf_validate3_0_0(self, value, strict, validated, error):
        return True

    def test_OneOf_validate3_0_1(self, self, value, strict, validated, error):
        return True

    def test_OneOf_validate3_0_2(self, self, value, strict, validated, error):
        return True

    def test_OneOf_validate3_0_3(self, self, value, strict, validated, error):
        return True

    def test_OneOf_validate3_0_4(self, self, value, strict, validated, error):
        return True

    def test_OneOf_validate3_0_5(self, self, value, strict, validated, error):
        return True


# Generated at 2022-06-14 14:15:58.551548
# Unit test for constructor of class AllOf
def test_AllOf():
    from typesystem import Integer, String
    from typesystem.fields import AllOf

    assert AllOf([Integer(), String()]).all_of == [Integer(), String()]

# Generated at 2022-06-14 14:16:04.881610
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    value = 3
    if_clause = Field()
    then_clause = Field()
    else_clause = Field()
    test_IfThenElse = IfThenElse(if_clause, then_clause, else_clause)
    value_from_IfThenElse = test_IfThenElse.validate(value)
    assert value_from_IfThenElse == value


# Generated at 2022-06-14 14:16:06.263423
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    val = NeverMatch(description='description')


# Generated at 2022-06-14 14:16:14.240025
# Unit test for method validate of class OneOf

# Generated at 2022-06-14 14:16:19.836270
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    schema = IfThenElse(
        if_clause=int,
        then_clause=str,
        else_clause=int,
    )
    assert schema.validate(10) == "10"
    assert schema.validate(10.5) == 10.5
    assert schema.validate("10") == "10"
    assert schema.validate("10.5") == "10.5"

# Generated at 2022-06-14 14:16:22.941509
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    if_clause = NeverMatch()
    then_clause = NeverMatch()
    else_clause = NeverMatch()

    ite = IfThenElse(if_clause, then_clause, else_clause)
    ite.validate(1)
    ite.validate(1, True)

# Generated at 2022-06-14 14:16:25.972463
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    item = NeverMatch()
    if isinstance(item, Field):
        assert getattr(item, "allow_null", False) == False
        assert getattr(item, "errors", {}) == {"never":"This never validates."}
        assert getattr(item, "nullable", False) == False
    else:
        assert False, "item should be an instance of Field."

# Generated at 2022-06-14 14:16:26.998607
# Unit test for method validate of class Not
def test_Not_validate():
    raise NotImplementedError()


# Generated at 2022-06-14 14:16:29.744882
# Unit test for constructor of class Not
def test_Not():
    try:
        n = Not(negated=Field(allow_null=False))
        assert False, 'Constructor should have raised a TypeError exception'
    except TypeError as e:
        pass



# Generated at 2022-06-14 14:16:44.960930
# Unit test for method validate of class Not
def test_Not_validate():
    field = Not(None)
    field.validate(None, strict=True)
    # field = Not(None)
    # field.validate(None, strict=False)
    # field = Not(None)
    # field.validate(1, strict=True)
    # field = Not(None)
    # field.validate(1, strict=False)
    # field = Not(None)
    # field.validate("hello world!", strict=True)
    # field = Not(None)
    # field.validate("hello world!", strict=False)
    # field = Not(None)
    # field.validate(1.1, strict=True)
    # field = Not(None)
    # field.validate(1.1, strict=False)

# Generated at 2022-06-14 14:16:45.589767
# Unit test for constructor of class OneOf
def test_OneOf():
    pass

# Generated at 2022-06-14 14:16:50.753276
# Unit test for method validate of class Not
def test_Not_validate():
    result1 = Not(negated=NeverMatch()).validate("foo")
    result2 = Not(negated=NeverMatch()).validate("bar")
    result3 = Not(negated=NeverMatch()).validate("baz")
    
    assert(result1 == "foo")
    assert(result2 == "bar")
    assert(result3 == "baz")

# Generated at 2022-06-14 14:16:54.190514
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    if_clause = Field()
    then_clause = Field()
    else_clause = Field()
    test = IfThenElse(if_clause,then_clause,else_clause,name="name")
    print(test.name + "\n")


# Generated at 2022-06-14 14:17:06.259980
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    from typesystem import Integer, String

    class TestOneOf(OneOf):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

    # initialize valid parameters
    child1 = Integer()
    child2 = String()
    one_of = [child1, child2]
    name = "one_of"
    description = "This is a test."
    default = ""

    # initialize expected results
    expected1 = 10
    expected2 = "Test"

    # initialize instance of class to be tested
    test_OneOf = TestOneOf(one_of, name=name, description=description, default=default)
    # test validate method
    result1 = test_OneOf.validate(expected1)
    # assert results
    assert result1 == expected1
   

# Generated at 2022-06-14 14:17:16.651922
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    data_types = {
        'Array': typesystem.Array(child=typesystem.Integer()),
        'Boolean': typesystem.Boolean(),
        'Float': typesystem.Float(),
        'Integer': typesystem.Integer(),
        'String': typesystem.String(),
    }
    a = typesystem.Object(properties={'child1': OneOf(one_of=[data_types['Array'], data_types['Integer']])})
    data = {"child1": []}
    assert a.validate(data), "Valid data"
    data = {"child1": 1}
    assert a.validate(data), "Valid data"
    data = {"child1": {}}
    assert not a.validate(data), "Invalid data"
    data = {"child1": 1.1}
    assert not a.valid

# Generated at 2022-06-14 14:17:21.615827
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    class TestSchema(Schema):
        t = OneOf([String(), Dictionary({"hello": String()})])
    s = TestSchema()
    expected = "this should match"
    s.validate({"t": expected})


# Generated at 2022-06-14 14:17:24.126823
# Unit test for constructor of class Not
def test_Not():
    not_ = Not(None)

    assert not_.errors == {"negated": "Must not match."}
    assert not_.negated == None

# Generated at 2022-06-14 14:17:27.492599
# Unit test for method validate of class Not
def test_Not_validate():
    x = Not(Any())
    y = x.validate(123)
    assert y is None
    z = x.errors['negated']
    ez = "Must not match."
    assert z == ez

# Generated at 2022-06-14 14:17:32.060329
# Unit test for constructor of class AllOf
def test_AllOf():
    def test():
        f1 = Field(name="f1")
        f2 = Field(name="f2")
        all_of = AllOf([f1, f2])
        print(all_of.all_of == [f1, f2])
        return all_of.all_of == [f1, f2]
    assert test()


# Generated at 2022-06-14 14:17:45.639507
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    # No match case
    one_of = OneOf([])
    with pytest.raises(one_of.validation_error):
        one_of.validate(1)

    # Multiple matches
    one_of = OneOf([Any(), Any()])
    with pytest.raises(one_of.validation_error):
        one_of.validate(1)

    # One match
    one_of = OneOf([Any()])
    assert one_of.validate(1) == 1

    # Multiple matches, one error
    class FailField(Field):
        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            raise self.validation_error("foo")

    one_of = OneOf([Any(), FailField()])

# Generated at 2022-06-14 14:17:47.260366
# Unit test for constructor of class OneOf
def test_OneOf():
    assert OneOf(one_of=[Any()]).one_of == [Any()]

# Generated at 2022-06-14 14:17:49.530988
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    new_NeverMatch = NeverMatch()
    assert new_NeverMatch.errors == {'never': 'This never validates.'}


# Generated at 2022-06-14 14:17:57.649756
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    # Test validate() method, test with string
    one_of_field = OneOf([])
    value = "string"
    assert one_of_field.validate(value) == value

    # Test validate() method, test with int
    one_of_field = OneOf([])
    value = 1
    assert one_of_field.validate(value) == value

    # Test validate() method, test with double
    one_of_field = OneOf([])
    value = 1.1
    assert one_of_field.validate(value) == value

    # Test validate() method, test with boolean
    one_of_field = OneOf([])
    value = True
    assert one_of_field.validate(value) == value

    # Test validate() method, test without one_of attribute
    one_of_

# Generated at 2022-06-14 14:17:59.735056
# Unit test for constructor of class AllOf
def test_AllOf():
    typesystem.fields.compile_schema_class("AllOf")

# Generated at 2022-06-14 14:18:03.083628
# Unit test for constructor of class Not
def test_Not():
    test = Not(AllOf([Any()]))
    assert isinstance(test, Not)
    assert test.negated == AllOf([Any()])



# Generated at 2022-06-14 14:18:04.089653
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    n = NeverMatch()


# Generated at 2022-06-14 14:18:09.200588
# Unit test for constructor of class OneOf
def test_OneOf():
  name = 'OneOf'
  args = [
    {"type": "string"},
    {"type": "boolean"}
  ]
  kwargs = {}
  cmd = 'OneOf(one_of=args, **kwargs)'
  copied = eval(cmd)
  assert name in str(copied) and str(args) in str(copied) and str(kwargs) in str(copied)


# Generated at 2022-06-14 14:18:10.938144
# Unit test for constructor of class AllOf
def test_AllOf():
    from .fields import Integer

    subject = AllOf([Integer()])
    assert subject is not None

# Generated at 2022-06-14 14:18:12.165262
# Unit test for constructor of class OneOf
def test_OneOf():
    field = OneOf([Int()], name="test_OneOf")


# Generated at 2022-06-14 14:18:33.263550
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    a = 1
    b = 2
    c = 3
    if len(sys.argv) > 1:
        a = float(sys.argv[1])
    if len(sys.argv) > 2:
        b = float(sys.argv[2])
    if len(sys.argv) > 3:
        c = float(sys.argv[3])
    ofield = OneOf(a, b, c)
    print(ofield.validate(a))

# Generated at 2022-06-14 14:18:35.883472
# Unit test for constructor of class Not
def test_Not():
    field = Not(Any())
    assert field.negated is not None
    assert field.errors is not None

# Generated at 2022-06-14 14:18:44.369653
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    field = OneOf(one_of=[Number(), String()])
    assert field.validate("a") == "a"
    assert field.validate(2) == 2

    field = OneOf(one_of=[Number(), String()])
    with pytest.raises(ValidationError) as exc:
        field.validate(None)
    assert exc.value.code == "no_match"

    field = OneOf(one_of=[Number(), String()])
    with pytest.raises(ValidationError) as exc:
        field.validate(False)
    assert exc.value.code == "no_match"

    field = OneOf(one_of=[Number(), String()])
    with pytest.raises(ValidationError) as exc:
        field.validate(dict(a=1))

# Generated at 2022-06-14 14:18:48.263191
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    schema = NeverMatch()
    try:
        schema.validate(1)
    except Exception as err:
        assert str(err) == "This never validates."


# Generated at 2022-06-14 14:18:48.805444
# Unit test for constructor of class Not
def test_Not():
    field = Not(negated = None)

# Generated at 2022-06-14 14:18:50.258053
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    f = OneOf([])
    assert f.validate([]) == []

# Generated at 2022-06-14 14:18:51.949182
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    n = NeverMatch()
    assert n


# Generated at 2022-06-14 14:18:55.764063
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    f = OneOf(one_of=[])
    # we don't care about the return value
    f.validate(value=None, strict=False)
    # we don't care about the return value
    f.validate(value=None, strict=True)


# Generated at 2022-06-14 14:18:57.938890
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    val = 'a'
    validation_result = OneOf([Field1(), Field2(), Field3()], allow_null=False).validate(val)
    return validation_result

# Generated at 2022-06-14 14:18:59.695445
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    field = NeverMatch()
    assert field.errors == {"never": "This never validates."}
    assert field.allow_null == False


# Generated at 2022-06-14 14:19:19.526894
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    one_of = OneOf(one_of=[String(), Integer()], default='1')
    one_of.validate('1')
    try:
        one_of.validate('a')
        raise Exception('error')
    except:
        pass

# Generated at 2022-06-14 14:19:21.710054
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    assert OneOf([Any()]).validate(42) is None
    try:
        OneOf([NeverMatch()]).validate(42)
        assert False, 'should have failed'
    except:
        pass



# Generated at 2022-06-14 14:19:25.315803
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
  field = NeverMatch();
  print(NeverMatch.__name__);
  print(field.__class__.__name__);
  print(field.errors["never"]);


# Generated at 2022-06-14 14:19:29.524609
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    x = NeverMatch()
    print(x.allow_null)

    # Test for NoneType
    # TODO: Fix this test
    # try:
    #     assert x.validate(None) == "This never validates."
    # except AssertionError as e:
    #     print(e)


# Generated at 2022-06-14 14:19:30.645830
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    assert NeverMatch().errors['never'] == "This never validates."



# Generated at 2022-06-14 14:19:33.524963
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    from typesystem import String
    n = NeverMatch(
        description="Never matches.",
        required=False,
    )
    assert n.description == "Never matches."
    assert n.required == False
    assert n.errors == {"never": "This never validates."}


# Generated at 2022-06-14 14:19:38.312860
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    # Constructor test
    try:
        NeverMatch(allow_null=True)
        has_exception = False
    except AssertionError:
        has_exception = True
    assert has_exception

    value = NeverMatch()
    assert value.errors == {"never": "This never validates."}


# Generated at 2022-06-14 14:19:46.719773
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    assert OneOf([String()]).validate({"hello":"world"})
    assert OneOf([String(), String()]).validate({"hello":"world"})
    assert OneOf([String(), String(), OneOf([String(), Number()])]).validate({"hello":"world"})
    assert OneOf([String(), String(), OneOf([String(), Number()])]).validate([1,2,3])
    assert OneOf([String(), String(), OneOf([String(), Number(), List(items=String())])]).validate([1,2,3])
    assert OneOf([String(), String(), OneOf([String(), Number(), List(items=String())])]).validate([])



# Generated at 2022-06-14 14:19:59.188726
# Unit test for constructor of class AllOf
def test_AllOf():
    from typesystem.fields import String
    from typesystem.types import Type
    from typesystem.fields import Timeline

    schedule = String(empty=False, max_length=500, allow_null=True)
    empty = String()

    all_of = AllOf([schedule, empty])
    result = all_of.validate(dict(host_id=dummy, name=dummy, is_community=False, start_date=dummy, end_date=dummy, description=dummy, username=dummy, location=dummy, timeline=dummy, tags=dummy))

# Generated at 2022-06-14 14:20:00.709893
# Unit test for constructor of class AllOf
def test_AllOf():
    assert AllOf(all_of=[String(), Number(), Array(items=Integer())])

# Generated at 2022-06-14 14:20:19.948361
# Unit test for constructor of class AllOf
def test_AllOf():
    # assert isinstance(AllOf([]), Schema)
    assert isinstance(AllOf(all_of=[]), Field)
    # assert isinstance(AllOf([Any()], name=""), Field)
    # assert isinstance(AllOf([Any(), Any()], name=""), Field)
    # assert isinstance(AllOf([Any(), Any(), Any()], name=""), Field)


# Generated at 2022-06-14 14:20:26.554761
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    """
    Unit test for method validate of class OneOf
    """
    print("\nUnit test for method validate of class OneOf")
    print("\n-------------------------")
    print("Initializing - start")
    OneOf(one_of = [])
    print("Initializing - done")
    print("-------------------------")
    print("-------------------------")
    print("Testing - start")
    print("Testing - done")
    print("-------------------------")



# Generated at 2022-06-14 14:20:27.396002
# Unit test for constructor of class AllOf
def test_AllOf():
	typesystem.AllOf(["hello", "world"])

# Generated at 2022-06-14 14:20:29.306749
# Unit test for constructor of class AllOf
def test_AllOf():
    try:
        AllOf(1)
    except AssertionError:
        assert True
    else:
        assert False


# Generated at 2022-06-14 14:20:29.945517
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    a = NeverMatch()

# Generated at 2022-06-14 14:20:30.650980
# Unit test for constructor of class AllOf
def test_AllOf():
    AllOf()

# Generated at 2022-06-14 14:20:34.049522
# Unit test for constructor of class Not
def test_Not():
    not_test = Not(Field())
    assert isinstance(not_test, Not)
    assert isinstance(not_test.negated, Field)


# Generated at 2022-06-14 14:20:36.967373
# Unit test for constructor of class Not
def test_Not():
    with pytest.raises(Exception):
        Not(1)
    with pytest.raises(Exception):
        Not(None)

# Generated at 2022-06-14 14:20:38.515022
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    x = NeverMatch()
    assert x.errors == {"never": "This never validates."}


# Generated at 2022-06-14 14:20:39.375310
# Unit test for constructor of class Not
def test_Not():
    assert Not(negated=False) is not None

# Generated at 2022-06-14 14:21:08.931444
# Unit test for constructor of class Not
def test_Not():
    a = Field()
    b = Not(a)

# Generated at 2022-06-14 14:21:09.734773
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    nm = NeverMatch()



# Generated at 2022-06-14 14:21:10.517070
# Unit test for constructor of class Not
def test_Not():
    assert Not(negated=Any())

# Generated at 2022-06-14 14:21:11.690859
# Unit test for constructor of class Not
def test_Not():
    not_field = Not(
            negated=str
    )
    assert not_field.negated == str


# Generated at 2022-06-14 14:21:15.871855
# Unit test for constructor of class Not
def test_Not():
    from typesystem.fields import Boolean
    from typesystem.types import Schema
    s=Schema(properties={"n":Not(negated=Boolean()),
                         "b":Boolean()})
    s.validate({"n":True,
                "b":False})


# Generated at 2022-06-14 14:21:17.202526
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    # given
    field = NeverMatch()
    # then
    assert field == False

# Generated at 2022-06-14 14:21:19.086504
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    nm = NeverMatch()
    assert nm.errors == {"never": "This never validates."}


# Generated at 2022-06-14 14:21:26.812562
# Unit test for constructor of class Not
def test_Not():
    class Not(Field):
        def __init__(self, negated, **kwargs):
            assert "allow_null" not in kwargs
            super().__init__(**kwargs)
            self.negated = negated
    assert issubclass(Not, Field)
    # An error is raised if the assertion is True
    # We can not use try/except to test it
    # try:
    #     Not(negated="")
    # except AssertionError:
    #     assert True
    # else:
    #     assert False

# Generated at 2022-06-14 14:21:28.421526
# Unit test for constructor of class Not
def test_Not():
    try:
        Not(Field())
        assert False
    except AssertionError:
        pass

test_Not()

# Generated at 2022-06-14 14:21:31.253079
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    if_clause = Field()
    then_clause = Field()
    else_clause = Field()
    assert IfThenElse(
        if_clause, then_clause, else_clause
    ).if_clause.errors == if_clause.errors


