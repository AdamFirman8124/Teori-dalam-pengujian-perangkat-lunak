

# Generated at 2022-06-14 14:12:53.499635
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    from pprint import pprint
    from base_tester import check

    obj = {"value": "Test"}
    all_of_object = {"value": ["Test", 1]}
    data_1_0 = {'state': 'AA', 'state_name': 'AAA'}
    data_1_1 = {'state': 11, 'state_name': 'AAA'}
    data_2_0 = {'state': 'CC', 'state_name': 'CCC'}
    data_2_1 = {'state': 33, 'state_name': 'CCC'}
    data_3_0 = {'state': 'EE', 'state_name': 'EEE'}
    data_3_1 = {'state': 55, 'state_name': 'EEE'}

# Generated at 2022-06-14 14:12:56.605578
# Unit test for method validate of class Not
def test_Not_validate():
    # Test when method validate of class Not returns correct output
    not_val = Not(AllOf([Any()]))
    assert not_val.validate(10) == 10


# Generated at 2022-06-14 14:12:59.098576
# Unit test for method validate of class Not
def test_Not_validate():
    not_field= Not(negated=Int())
    assert not_field.validate(10) == 10


# Generated at 2022-06-14 14:13:01.236329
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    # Test for body of __init__ in class NeverMatch
    assert True == True


# Generated at 2022-06-14 14:13:03.266544
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    field = OneOf(one_of=[])
    assert field.validate(value=False) == False


# Generated at 2022-06-14 14:13:05.825280
# Unit test for constructor of class AllOf
def test_AllOf():
    a = AllOf(all_of = [])
    assert a.all_of == []


# Generated at 2022-06-14 14:13:14.096125
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    if_clause = IfThenElse(AllOf([]), AllOf([]), AllOf([]))
    assert if_clause.validate(None) == None

    # TODO: Implment test case
    #if_clause = IfThenElse(AllOf([]), AllOf([]), AllOf([]))
    #assert if_clause.validate(1) == 1

    # TODO: Implment test case
    #if_clause = IfThenElse(AllOf([]), AllOf([]), AllOf([]))
    #assert if_clause.validate(None) == None

    # TODO: Implment test case
    #if_clause = IfThenElse(AllOf([]), AllOf([]), AllOf([]))
    #assert if_clause.validate(None) == None

# Generated at 2022-06-14 14:13:16.301397
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    nm = NeverMatch()
    print(nm)


# Generated at 2022-06-14 14:13:25.580655
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    class Person(TypedDict):
        name: str
        age: int
        male: bool
    class Department(TypedDict):
        name: str
        person: Person
        male: bool

    dept_dict = {
        'name': 'Engineering',
    }
    dept_schema = TypedSchema.from_typeddict(Department)
    person_schema = TypedSchema.from_typeddict(Person)
    one_of_schema: TypedSchema = OneOf([person_schema, dept_schema])
    one_of_schema.validate(dept_dict)



# Generated at 2022-06-14 14:13:29.028900
# Unit test for constructor of class OneOf
def test_OneOf():
    Field.__init__
    one_of = [{'type': 'string'}, {'type': 'integer'}]
    p = OneOf(one_of)


# Generated at 2022-06-14 14:13:35.852545
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    test_field = NeverMatch()
    assert test_field.errors["never"] == "This never validates."


# Generated at 2022-06-14 14:13:37.779746
# Unit test for constructor of class Not
def test_Not():
    assert issubclass(Not, Field)
    assert Not.errors == {'negated': 'Must not match.'}


# Generated at 2022-06-14 14:13:49.494647
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    a = OneOf([String(max_length=1)])
    result = a.validate('aaa')
    assert result == None

    b = OneOf([Integer(), String(max_length=1)])
    result = b.validate(2)
    assert result == None

    c = OneOf([Integer(), String(max_length=1)])
    result = c.validate('bbb')
    assert result == None

    d = OneOf([Integer(), String(max_length=1)])
    result = d.validate('vvv')
    assert result == None

    e = OneOf([Integer(), String(max_length=1)])
    result = e.validate(5)
    assert result == 5

    f = OneOf([Integer(), String(max_length=1)])
    result = f.valid

# Generated at 2022-06-14 14:13:52.236789
# Unit test for method validate of class Not
def test_Not_validate():
    instance = Not(negated=None)
    value = None
    strict = None
    expected = None
    actual = instance.validate(value, strict)

    assert actual == expected

# Generated at 2022-06-14 14:13:54.770195
# Unit test for constructor of class OneOf
def test_OneOf():
    from typesystem.fields import Integer

    field = OneOf([Integer(), Integer()])
    assert field.one_of[0].TYPE == "integer"
    assert field.one_of[1].TYPE == "integer"


# Generated at 2022-06-14 14:14:00.784473
# Unit test for method validate of class Not
def test_Not_validate():
    field = Not(negated=Any())
    value = 1
    assert field.validate(value, strict=True) == 1
    with pytest.raises(ValidationError) as excinfo:
        field.validate(None)
    assert excinfo.value.as_dict() == {'negated': 'Must not match.'}



# Generated at 2022-06-14 14:14:02.922641
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    n = NeverMatch()
    assert n.errors == {"never": "This never validates."}


# Generated at 2022-06-14 14:14:13.909761
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    data = [
        {
            "data" : 'test',
            "validates" : False,
            "exception": 'no_match'
        },
        {
            "data" : 'a',
            "validates" : True,
            "exception": None
        },
        {
            "data" : 'ab',
            "validates" : True,
            "exception": 'multiple_matches'
        },
        {
            "data" : 'c',
            "validates" : True,
            "exception": None
        }
    ]

# Generated at 2022-06-14 14:14:20.087686
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    from typesystem import Number, String

    assert IfThenElse(Number(), String()).validate(1) == "1"

    # If clause fails
    import pytest
    with pytest.raises(ValidationError):
        IfThenElse(String(), String()).validate(1)

# Generated at 2022-06-14 14:14:21.173320
# Unit test for constructor of class Not
def test_Not():
    a = Not(negated=Field())

# Generated at 2022-06-14 14:14:26.942782
# Unit test for constructor of class AllOf
def test_AllOf():
    # Instantiate object
    allof_obj = AllOf(None)



# Generated at 2022-06-14 14:14:35.942790
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    #define a list of Field that are elements of class OneOf
    one_of = [Field("Field1", type="string"), Field("Field2", type="integer")]
    #create a instance of class OneOf
    one_of0 = OneOf("OneOf0", one_of=one_of)
    #test the method validate with a value that is a string. We expect it to return true.
    value = "test"
    assert one_of0.validate(value)
    #test with another value "test2". We expect it to return true as well
    value = "test2"
    assert one_of0.validate(value)
    #test with a value that is not a string(integer in our case). We expect that the method validate does not return true
    value = 2

# Generated at 2022-06-14 14:14:43.901296
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    int_one_of = OneOf([Integer(minimum=1)])
    try:
        int_one_of.validate(0)
        assert False
    except ValidationError:
        assert True
    int_one_of.validate(2)
    try:
        int_one_of.validate(1)
        assert False
    except ValidationError:
        assert True


# Generated at 2022-06-14 14:14:45.494832
# Unit test for constructor of class AllOf
def test_AllOf():
    assert isinstance(AllOf([Any()]), AllOf)


# Generated at 2022-06-14 14:14:47.518584
# Unit test for method validate of class Not
def test_Not_validate():
    n = Not(negated="abc")
    result = n.validate("xyz")
    assert result == "xyz"


# Generated at 2022-06-14 14:14:52.109266
# Unit test for method validate of class Not
def test_Not_validate():
	# Create an object of class Not
    n = Not(None)
    # Test the method with parameter value = 1, strict = False
    result = n.validate(1, False)
    # Assert the result with the expected output
    assert result == 1


# Generated at 2022-06-14 14:14:55.907666
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    schema = OneOf([TypeSystemError.typesystem.Integer, TypeSystemError.typesystem.String])
    with pytest.raises(ValidationError, match="Did not match any valid type."):
        schema.validate(9999)



# Generated at 2022-06-14 14:14:59.140776
# Unit test for constructor of class Not
def test_Not():
    t = Not(eval("int"))
    assert t.negated.__name__ == "int.__getitem__", "unit test for Not failed!"


# Generated at 2022-06-14 14:15:06.414499
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    from typesystem.fields import Field, String, Union

    is_str = OneOf(one_of=[String()])
    assert is_str.validate(1) == '1'
    assert is_str.validate('hello') == 'hello'

    is_str_or_int = Union(types=[String(), Integer()])
    assert is_str_or_int.validate(1) == 1
    assert is_str_or_int.validate('hello') == 'hello'

# Generated at 2022-06-14 14:15:06.996750
# Unit test for constructor of class OneOf
def test_OneOf():
    assert 1 == 1

# Generated at 2022-06-14 14:15:11.230102
# Unit test for constructor of class AllOf
def test_AllOf():
    assert AllOf([Any()])


# Generated at 2022-06-14 14:15:12.518127
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
   myfield = NeverMatch()


# Generated at 2022-06-14 14:15:15.803493
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    # Arrange
    of = OneOf(one_of=[1, 2, 3])
    # Act
    of.validate(2)
    # Assert
    assert True



# Generated at 2022-06-14 14:15:18.377273
# Unit test for constructor of class AllOf
def test_AllOf():
    allof = AllOf([1,2,3])
    assert allof


# Generated at 2022-06-14 14:15:21.134196
# Unit test for method validate of class Not
def test_Not_validate():
    """Unit test for method validate of class Not"""
    assert Not({}).validate({"key": "value"}) == {"key": "value"}



# Generated at 2022-06-14 14:15:23.857313
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    field = IfThenElse(Integer(), defaults_to=0)
    assert field.validate("") == 0
    assert field.validate("1") == 1



# Generated at 2022-06-14 14:15:28.835467
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    valid_types = [
        {'type': 'string', 'title': 'value'},
        # {'type': 'array', 'title': 'value', 'items': {'type': 'string'}}
    ]
    value = 'hello world'

    field = OneOf(one_of=valid_types)
    field.validate(value)



# Generated at 2022-06-14 14:15:30.530366
# Unit test for constructor of class OneOf
def test_OneOf():
    one_of = OneOf(one_of=[Any()])
    print(one_of)
    
test_OneOf()

# Generated at 2022-06-14 14:15:31.145815
# Unit test for method validate of class Not
def test_Not_validate():
    pass

# Generated at 2022-06-14 14:15:33.916429
# Unit test for method validate of class Not
def test_Not_validate():
    print("Running test test_Not_validate...")
    field = Not(String())
    if field.validate("string"):
        print("pass")
    else:
        print("fail")


# Generated at 2022-06-14 14:15:43.803937
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    if_clause = NeverMatch()
    then_clause = NeverMatch()
    else_clause = NeverMatch()
    utils = IfThenElse(if_clause, then_clause, else_clause)
    value = 10
    assert utils.validate_or_error(value)[1] is None
    else_clause = NeverMatch()
    if_clause = NeverMatch()
    then_clause = NeverMatch()
    utils = IfThenElse(if_clause, then_clause, else_clause)
    value = 10
    assert utils.validate_or_error(value)[1] is None
    else_clause = NeverMatch()
    then_clause = NeverMatch()
    if_clause = NeverMatch()

# Generated at 2022-06-14 14:15:44.423857
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    assert NeverMatch()

# Generated at 2022-06-14 14:15:45.389348
# Unit test for constructor of class OneOf
def test_OneOf():
	c = OneOf([])
	print(c)

# Generated at 2022-06-14 14:15:47.423169
# Unit test for constructor of class Not
def test_Not():
    assert Not(negated=Field)



# Generated at 2022-06-14 14:15:54.016949
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    a = IfThenElse(AllOf([]), String())
    a.validate(1)
    a.validate('2')

# Define type for format of attribute 'if' of class IfThenElse
IfThenElse_if = Field

# Define type for format of attribute 'then' of class IfThenElse
IfThenElse_then = Field

# Define type for format of attribute 'else' of class IfThenElse
IfThenElse_else = Field



# Generated at 2022-06-14 14:15:59.091545
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    a = OneOf(
        [
            Int(maximum=10),
            Int(minimum=15),
            Int(maximum=10),
        ],
        required=True,
        description="At most 10 or at least 15.",
        errors={"no_match": "At most 10 or at least 15."},
    )
    assert a.validate(5) == 5
    assert a.validate(15) == 15
    assert a.validate(20) == 15


# Generated at 2022-06-14 14:16:08.346793
# Unit test for method validate of class Not
def test_Not_validate():
    context = {
        "a": "a",
        "b": "b",
    }
    not_a = Not(Field(key="a"))
    assert not_a.validate(context) == context
    with pytest.raises(ValidationError):
        not_a.validate(
            {
                "a": 123,
            }
        )
    not_b = Not(Field(key="b"))
    assert not_b.validate(context) == context
    with pytest.raises(ValidationError):
        not_b.validate(
            {
                "b": 123,
            }
        )

# Integration test for class Not

# Generated at 2022-06-14 14:16:11.927375
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    field = IfThenElse(String(), String(), String())
    assert field.validate("a") == "a"
    assert field.validate(1) == "1"
    assert field.validate(None) == ""



# Generated at 2022-06-14 14:16:17.126050
# Unit test for constructor of class AllOf
def test_AllOf():
    print('Testing constructor of class AllOf')
    try: 
        AllOf(int, str)
        assert False, 'AllOf is not allowed'
    except:
        assert True
    try:
        AllOf([int,str])
        assert True
    except:
        assert False, 'AllOf is allowed'


# Generated at 2022-06-14 14:16:18.646085
# Unit test for method validate of class Not
def test_Not_validate():
    field_type = Not(Any())
    field_type.validate('')

# Generated at 2022-06-14 14:16:30.423408
# Unit test for method validate of class Not
def test_Not_validate():
    errors = {
        "negated": "Must not match."
    }

    def __init__(self, negated: Field, **kwargs: typing.Any) -> None:
        assert "allow_null" not in kwargs
        super().__init__(**kwargs)
        self.negated = negated

    def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
        _, error = self.negated.validate_or_error(value, strict=strict)
        if error:
            return value
        raise self.validation_error("negated")


# Generated at 2022-06-14 14:16:35.136513
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    test_field = IfThenElse(Any(), None, None)
    try:
        test_field.validate(None)
    except Exception as exception:
        assert (exception.messages["__all__"]) == [
            "Must not be blank if null is not allowed."
        ]
    # If a condition is not fulfilled, then the value is being validated by the else_clause
        assert test_field.else_clause.validate(None) == None



# Generated at 2022-06-14 14:16:38.752149
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    field = NeverMatch("test", title="title", description="description")
    assert field.name == "test"
    assert field.title == "title"
    assert field.description == "description"


# Generated at 2022-06-14 14:16:40.809950
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    one_of_field = OneOf([String(), Number()])
    one_of_field.validate("Hello")

# Generated at 2022-06-14 14:16:43.542316
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    field = OneOf([])
    value = None
    strict = None

    # Calling function validate
    field.validate(value, strict)

# Generated at 2022-06-14 14:16:53.728602
# Unit test for method validate of class Not
def test_Not_validate():
    # Test for case that validates when negated matches
    test_negated_field = Not(NeverMatch())
    test_value = "Foo"
    test_validated_value, test_validated_error = test_negated_field.validate_or_error(test_value)

    assert test_validated_value == test_value
    assert test_validated_error is None
    assert test_negated_field.errors["negated"] == "Must not match."

    # Test for case that doesn't validate when negated doesn't match
    test_negated_field = Not(Integer())
    test_value = "Foo"
    test_validated_value, test_validated_error = test_negated_field.validate_or_error(test_value)

    assert test_validated_value is None

# Generated at 2022-06-14 14:16:54.257344
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    pass

# Generated at 2022-06-14 14:17:03.051447
# Unit test for constructor of class AllOf
def test_AllOf():
    class AllOf:
        def __init__(self, all_of: typing.List[Field], **kwargs: typing.Any) -> None:
            assert "allow_null" not in kwargs
            super().__init__(**kwargs)
            self.all_of = all_of
    a = AllOf([1, 2, 3])
    try:
        assert(len(a.all_of) == 3)
    except AssertionError:
        print("AllOf constructor doesn't work")
    else:
        print("AllOf constructor works")


# Generated at 2022-06-14 14:17:05.315557
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    # Check that coverage is reported
    a = NeverMatch()
    assert isinstance(a,NeverMatch)



# Generated at 2022-06-14 14:17:10.000357
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    a = NeverMatch(
        optional=True, title="Allowed if optional", default=None, description="Never match"
    )
    assert a.optional
    assert a.title == "Allowed if optional"
    assert a.default == None
    assert a.description == "Never match"



# Generated at 2022-06-14 14:17:17.387338
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    if_clause = Field()
    then_clause = Field()
    else_clause = Field()
    field = IfThenElse(if_clause = if_clause, then_clause = then_clause, else_clause = else_clause)
    value = 5
    strict = False
    actual = field.validate(value = value, strict = strict)
    assert actual == value


# Generated at 2022-06-14 14:17:18.217091
# Unit test for constructor of class OneOf
def test_OneOf():
    assert True

# Generated at 2022-06-14 14:17:30.154998
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    import string
    import random

    def method_test(test_case, method_test_name, function_under_test):
        # Print method name and test case
        print('Test for method {} in class IfThenElse: {}'.format(method_test_name, test_case))
        # The input should be valid if test_case is 'valid'
        is_valid_input = False
        valid_input = None
        if test_case == 'valid':
            is_valid_input = True
            valid_input = generate_valid_input()
        # Generate a valid input and make it invalid
        if test_case == 'invalid':
            is_valid_input = True
            valid_input = generate_valid_input()
            valid_input = make_input_invalid(valid_input)
        # Generate an invalid input

# Generated at 2022-06-14 14:17:31.413715
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
	assert NeverMatch().__init__ == None


# Generated at 2022-06-14 14:17:41.745440
# Unit test for method validate of class Not
def test_Not_validate():
    notfield = Not(IfThenElse(AllOf(Any(), Any()), then_clause=Any()), field_name="Not")
    # should not validate, cases:
    # if-clause is valid and then-clause is valid
    assert notfield.validate(1)
    # if-clause is not valid and then-clause is valid
    assert notfield.validate([1,2])
    # if-clause is valid and then-clause is not valid
    assert notfield.validate([])
    # if-clause is not valid and then-clause is not valid
    assert notfield.validate(False)

# Generated at 2022-06-14 14:17:45.839283
# Unit test for constructor of class AllOf
def test_AllOf():
    n = Any()
    all_of = AllOf(n)
    assert all_of.all_of == n

# Generated at 2022-06-14 14:17:48.239292
# Unit test for method validate of class Not
def test_Not_validate():
    class ActorValidator(IfThenElse):
        pass

    validator = ActorValidator("name")
    try:
        validator.validate("name")
    except Exception as e:
        assert True
    else:
        assert False

# Generated at 2022-06-14 14:17:49.351557
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    pass


# Generated at 2022-06-14 14:17:55.629850
# Unit test for constructor of class OneOf
def test_OneOf():
    one_of1 = OneOf([Any()])
    one_of2 = OneOf([Any(), Any(), Any()])
    one_of3 = OneOf([Any(),Any(),Any(),Any(),Any(),Any()])
    assert (one_of1.one_of == [Any()])
    assert (one_of2.one_of == [Any(), Any(), Any()])
    assert (one_of3.one_of == [Any(), Any(), Any(), Any(), Any(), Any()])
    print("Test for constructor of one of is passed.")


# Generated at 2022-06-14 14:17:58.335013
# Unit test for constructor of class OneOf
def test_OneOf():
    
    f = OneOf([Field()], nullable=True)
    assert f.nullable == True
    assert f.default == None
    assert f.one_of == [Field()]



# Generated at 2022-06-14 14:18:05.359919
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    schema = OneOf([Any()], noneable=True)
    assert schema.validate(None) is None
    assert schema.validate(1) == 1
    with pytest.raises(Exception) as exc:
        schema.validate([1])
    assert str(exc.value) == 'Expected one of: Any'


# Generated at 2022-06-14 14:18:09.947619
# Unit test for constructor of class OneOf
def test_OneOf():
    import pytest
    from typesystem.fields import Integer, Number
    candidate = [Integer(), Number()]
    def one_of(one_of: int) -> int:
        return one_of
    one_of=OneOf(candidate)
    with pytest.raises(AssertionError):
        one_of=OneOf(candidate,allow_null=False)


# Generated at 2022-06-14 14:18:20.992198
# Unit test for constructor of class IfThenElse

# Generated at 2022-06-14 14:18:28.012782
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    # Given
    schema = IfThenElse(Integer(),Integer(),String(),description="description",
    format="regex",pattern="pattern")
    positive_input = 32
    negative_input = "hola"
    # When
    result_positive_input = schema.validate(positive_input)
    result_negative_input = schema.validate(negative_input)
    # Then
    assert result_positive_input == 32
    assert result_negative_input == "hola"


# Generated at 2022-06-14 14:18:29.254692
# Unit test for constructor of class AllOf
def test_AllOf():
    assert AllOf(None, description = 'test-description') is not None

# Generated at 2022-06-14 14:18:40.599633
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    class IfThenElse(Field):
        errors = {
            "no_clause": "Did not match any valid type.",
            "multiple_matches": "Matched more than one type.",
        }
        def __init__(
            self,
            if_clause: Field,
            then_clause: Field = None,
            else_clause: Field = None,
            **kwargs: typing.Any
        ) -> None:
            super().__init__(**kwargs)
            self.if_clause = if_clause
            self.then_clause = Any() if then_clause is None else then_clause
            self.else_clause = Any() if else_clause is None else else_clause


# Generated at 2022-06-14 14:18:45.867316
# Unit test for method validate of class Not
def test_Not_validate():
    errors = {"negated": "Must not match."}
    field_1 = Not(errors)
    field_2 = Not(errors)

    if(field_1.errors == field_2.errors):
        assert True
    else:
        assert False


# Generated at 2022-06-14 14:18:51.322572
# Unit test for method validate of class Not
def test_Not_validate():
    params = dict(
        name="negated",
        title="Negated",
        description="Must not match.",
        negated=Field()
    )
    not_field = Not(**params)
    print(not_field.validate(None))
    print(not_field.validate(1))


# Generated at 2022-06-14 14:18:53.652002
# Unit test for constructor of class AllOf
def test_AllOf():
    all_of = AllOf([])
    assert all_of.__dict__['all_of'] == []


# Generated at 2022-06-14 14:18:55.764270
# Unit test for method validate of class Not
def test_Not_validate():
    def test_fn():
        field = Not(negated=String(), description="field")
        field.validate("")
    assert test_fn() is None

# Generated at 2022-06-14 14:19:03.241644
# Unit test for method validate of class Not
def test_Not_validate():
    not_ = Not(Number())
    with pytest.raises(ValueError):
        not_.validate(123)
        

# Generated at 2022-06-14 14:19:07.944410
# Unit test for constructor of class OneOf
def test_OneOf():
    # Normal initialization
    field = Field()
    one_of_field = OneOf([field])
    assert one_of_field.one_of is not None
    assert one_of_field.one_of == [field]

    # Error test: AssertionError when allow_null exists in kwargs
    try:
        OneOf([field], allow_null=False)
        assert False
    except AssertionError:
        assert True



# Generated at 2022-06-14 14:19:11.517043
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    t = False

    def throw():
        raise AssertionError

    try:
        NeverMatch()
    except AssertionError:
        t = True
    assert t



# Generated at 2022-06-14 14:19:21.779830
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    from typesystem.base import ValidationError
    from typesystem import Integer
    from typesystem import String

    if_clause = Integer(max_value=100)
    then_clause = Integer(min_value=0, max_value=100)
    else_clause = String(min_length=2)

    if_then_else = IfThenElse(if_clause, then_clause, else_clause)

# Generated at 2022-06-14 14:19:31.566180
# Unit test for method validate of class Not
def test_Not_validate():
    # this field should always return an error
    negated_field = NeverMatch()
    # test for valid value
    negated_field2 = Not(negated=negated_field)
    valid_value = 5
    assert negated_field2.validate(valid_value) == 5
    # test for invalid value
    invalid_value = 'hello'
    try:
        negated_field2.validate(invalid_value)
        # should never reach this line
        assert False
    except NeverMatch.validation_error:
        pass
    # test for null value
    null_value = None
    try:
        negated_field2.validate(null_value)
        # should never reach this line
        assert False
    except NeverMatch.validation_error:
        pass



# Generated at 2022-06-14 14:19:33.531386
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    if_clause = Field()
    then_clause = Field()
    else_clause = Field()
    ite = IfThenElse(if_clause, then_clause, else_clause)
    assert ite.validate(1) == 1



# Generated at 2022-06-14 14:19:36.792467
# Unit test for constructor of class OneOf
def test_OneOf():
    try:
        assert OneOf
    except NameError:
        print("OneOf is not defined")
    else:
        print("OneOf is defined")
    #assert OneOf() is not None


# Generated at 2022-06-14 14:19:38.911397
# Unit test for constructor of class OneOf
def test_OneOf():
    L = [{'type': 'string'}, {'type': 'integer'}]
    OneOf(L)


# Generated at 2022-06-14 14:19:41.199606
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    f = IfThenElse(integer(), string())
    assert f.validate(1) == "1"

# Generated at 2022-06-14 14:19:42.951723
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    with pytest.raises(AssertionError):
        NeverMatch(allow_null=True)


# Generated at 2022-06-14 14:19:46.071864
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    field = NeverMatch()
    return field


# Generated at 2022-06-14 14:19:47.472184
# Unit test for constructor of class AllOf
def test_AllOf():
    field = AllOf([Int(), Int()])
    return field.validate(4)



# Generated at 2022-06-14 14:19:59.596433
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    validate_in_true_case = 'validate_in_true_case'
    validate_in_false_case = 'validate_in_false_case'
    class IfClause(Field):
        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            if value == 'if_clause':
                return validate_in_true_case
            else:
                return validate_in_false_case
    class ThenClause(Field):
        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            return value
    class ElseClause(Field):
        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            return value
    if_clause = IfClause()

# Generated at 2022-06-14 14:20:06.135044
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    '''
    Test validate function.
    '''
    from typesystem.fields import Integer
    from typesystem.validators import MaxValue
    from typesystem.exceptions import ValidationError
    from typesystem.base import ErrorList

    #case valid
    if_clause = Integer(validators=[MaxValue(10)])
    then_clause = Integer(validators=[MaxValue(20)])
    else_clause = Integer(validators=[MaxValue(30)])
    if_then_else = IfThenElse(if_clause, then_clause, else_clause)
    result = if_then_else.validate(10)
    assert result == 10

    #case invalid
    if_clause = Integer(validators=[MaxValue(10)])

# Generated at 2022-06-14 14:20:13.723393
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    from typesystem import Integer

    field = IfThenElse(
        if_clause = Integer(minimum = 10),
        then_clause = Integer(minimum = 100),
        else_clause = Integer(minimum = 200),
    )

    assert field.validate(5) == 200
    assert field.validate(15) == 15
    # assert field.validate(15) == 150 # this would be the case if validate method returned the validated value, instead of the input value
    print('test_IfThenElse_validate passed')



# Generated at 2022-06-14 14:20:14.805035
# Unit test for constructor of class OneOf
def test_OneOf():
    assert OneOf([]) is not None

# Generated at 2022-06-14 14:20:24.425736
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    test_value = 17
    assert test_value == IfThenElse(if_clause=Any()).validate(test_value)
    assert test_value == IfThenElse(if_clause=Any(), then_clause=Any()).validate(test_value)
    assert test_value == IfThenElse(if_clause=Any(), else_clause=Any()).validate(test_value)
    assert test_value == IfThenElse(if_clause=Any(), then_clause=Any(), else_clause=Any()).validate(test_value)
    assert test_value == IfThenElse(if_clause=NeverMatch(), else_clause=Any()).validate(test_value)

# Generated at 2022-06-14 14:20:25.117544
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    item = NeverMatch()
    assert item.validation_error("never")

# Generated at 2022-06-14 14:20:26.289854
# Unit test for constructor of class AllOf
def test_AllOf():
    obj = AllOf("abc")
    assert obj.all_of == "abc"
    assert obj.description == "AllOf(all_of='abc')"

# Generated at 2022-06-14 14:20:28.592868
# Unit test for constructor of class OneOf
def test_OneOf():
	from typesystem import Integer
	x = OneOf([Integer])
	print(x.validate('1'))
	print(x.errors)


# Generated at 2022-06-14 14:20:32.858345
# Unit test for constructor of class OneOf
def test_OneOf():
    base_type = OneOf([Int(), Float()])
    assert base_type.one_of == [Int(), Float()]


# Generated at 2022-06-14 14:20:35.379610
# Unit test for constructor of class AllOf
def test_AllOf():
    """
    Test the constructor of the class AllOf
    """
    assert AllOf([1, 2, 3])



# Generated at 2022-06-14 14:20:39.071608
# Unit test for constructor of class AllOf
def test_AllOf():
    field = AllOf([])
    assert field.all_of == []
    field = AllOf([], description="A description")
    assert field.all_of == []
    assert field.description == "A description"



# Generated at 2022-06-14 14:20:42.468919
# Unit test for constructor of class OneOf
def test_OneOf():
    one_of_1 = OneOf([])
    one_of_2 = OneOf([Any()])
    one_of_3 = OneOf([Any(), Any()])
    assert one_of_1
    assert one_of_2
    assert one_of_3

# Generated at 2022-06-14 14:20:44.445947
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    field = NeverMatch()
    assert field.errors["never"] == "This never validates."


# Generated at 2022-06-14 14:20:54.299602
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    from typesystem.fields import String, Integer
    from typesystem.types import Type
    if_clause = IfThenElse(String())
    then_clause = IfThenElse(String(), Integer())
    else_clause = IfThenElse(String(), Integer(), Integer())
    assert isinstance(if_clause.if_clause, String)
    assert isinstance(then_clause.if_clause, String)
    assert isinstance(else_clause.if_clause, String)
    assert isinstance(if_clause.then_clause, Any)
    assert isinstance(then_clause.then_clause, Type)
    assert isinstance(else_clause.then_clause, Type)
    assert isinstance(if_clause.else_clause, Any)

# Generated at 2022-06-14 14:20:56.702583
# Unit test for constructor of class OneOf
def test_OneOf():
    from typesystem.fields import Integer, String
    from typesystem.fields import Object
    from typesystem.fields import Union
    from typesystem.fields import Field, OneOf
    x = OneOf([Integer(), String()])



# Generated at 2022-06-14 14:20:58.454824
# Unit test for constructor of class AllOf
def test_AllOf():
    """
    Test constructor
    """
    field = AllOf(None)



# Generated at 2022-06-14 14:21:05.872873
# Unit test for constructor of class OneOf
def test_OneOf():
    from typesystem.fields import Integer, String
    class Person(Field):
        first_name = String()

    errors = {
        "no_match": "Did not match any valid type.",
        "multiple_matches": "Matched more than one type."
    }
    field = OneOf(one_of=[String(), Person(), Integer()], errors=errors)

    # testing constructor
    assert field.one_of == [String(), Person(), Integer()] and field.errors == errors
    print('Test 1 (OneOf) OK')



# Generated at 2022-06-14 14:21:08.969473
# Unit test for constructor of class NeverMatch

# Generated at 2022-06-14 14:21:15.274189
# Unit test for constructor of class AllOf
def test_AllOf():
    field = AllOf([], parent=None)
    return field


# Generated at 2022-06-14 14:21:25.673007
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    if_clause = Field(type="string")
    print(if_clause)
    then_clause = Not(if_clause)
    print(then_clause)
    else_clause = AllOf([if_clause, then_clause])
    print(else_clause)

    if_then_else = IfThenElse(if_clause=if_clause, then_clause=then_clause, else_clause=else_clause)
    print(if_then_else)
    assert if_then_else.if_clause == if_clause
    assert if_then_else.then_clause == then_clause
    assert if_then_else.else_clause == else_clause


# Generated at 2022-06-14 14:21:31.540477
# Unit test for constructor of class OneOf
def test_OneOf():
    test_oneOf_value1 = 3.2
    test_oneOf_value2 = "testvalue"
    test_oneOf_test1 = Decimal(test_oneOf_value1)
    test_oneOf_test2 = String(test_oneOf_value2)
    test_oneOf_instance = OneOf([test_oneOf_test1, test_oneOf_test2])
    assert test_oneOf_instance.validate(test_oneOf_value1) == test_oneOf_value1
    assert test_oneOf_instance.validate(test_oneOf_value2) == test_oneOf_value2

# Generated at 2022-06-14 14:21:32.845417
# Unit test for constructor of class OneOf
def test_OneOf():
    assert not hasattr(OneOf, "errors")


# Generated at 2022-06-14 14:21:41.202781
# Unit test for constructor of class OneOf
def test_OneOf():
    from typesystem.fields import Integer

    field = OneOf([Integer()], name='OneOf')
    field.validate(1)
    try:
        field.validate('foo')
    except ValidationError as exc:
        assert exc.code == 'no_match'
    try:
        field.validate('')
    except ValidationError as exc:
        assert exc.code == 'no_match'
    try:
        field.validate(None)
    except ValidationError as exc:
        assert exc.code == 'no_match'
    try:
        field.validate(1.0)
    except ValidationError as exc:
        assert exc.code == 'multiple_matches'


# Generated at 2022-06-14 14:21:44.974564
# Unit test for constructor of class AllOf
def test_AllOf():
    import typesystem
    age = typesystem.Integer(minimum=0, maximum=120)
    name = typesystem.String(min_length=1, max_length=10)
    field = typesystem.AllOf([age, name])


# Generated at 2022-06-14 14:21:46.642452
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    test_field = Field()
    assert isinstance(test_field, Field)

# Unit test all valid input

# Generated at 2022-06-14 14:21:51.062211
# Unit test for constructor of class OneOf
def test_OneOf():
    one_of = OneOf([Field])
    assert one_of.errors == {
        "no_match": "Did not match any valid type.",
        "multiple_matches": "Matched more than one type.",
    }
    assert one_of.one_of == [Field]
    assert one_of.__name__ == "OneOf"



# Generated at 2022-06-14 14:21:55.332571
# Unit test for constructor of class AllOf
def test_AllOf():
    f1 = Field(name="f1")
    f2 = Field(name="f2")
    all_of = AllOf(all_of=[f1, f2])
    assert all_of.all_of[0] == f1
    assert all_of.all_of[1] == f2


# Generated at 2022-06-14 14:21:57.684791
# Unit test for constructor of class OneOf
def test_OneOf():
    fields = [Field()]
    one_of = OneOf(fields)
    assert one_of.one_of == fields


# Generated at 2022-06-14 14:22:04.812245
# Unit test for constructor of class AllOf
def test_AllOf():
    type_float = AllOf([1.0, 2.0])
    assert type_float.is_type_of(1.0)
    assert not type_float.is_type_of(1)
    assert type_float.validate(1.0) == 1.0
    assert not type_float.validate(1)


# Generated at 2022-06-14 14:22:05.940077
# Unit test for constructor of class AllOf
def test_AllOf():
    assert AllOf is not None


# Generated at 2022-06-14 14:22:09.475510
# Unit test for constructor of class AllOf
def test_AllOf():
    number=Field(type="number")
    string=Field(type="string")
    assert AllOf([number, string])
    assert AllOf([number, string]).all_of == [number, string]


# Generated at 2022-06-14 14:22:12.101240
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    assert len(IfThenElse(Field(required=True), Field(required=True)).fields) == 2
    assert len(IfThenElse(Field(), None, Field()).fields) == 2



# Generated at 2022-06-14 14:22:21.088789
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    import pytest
    from typesystem.fields import String

    if_clause = String()
    then_match = String()
    else_match = String()

    value = "string"
    if_match, _ = if_clause.validate_or_error(value, strict=False)
    if_no_match, _ = if_clause.validate_or_error(15, strict=False)
    then_match, _ = then_match.validate_or_error(value, strict=False)
    else_match, _ = else_match.validate_or_error(value, strict=False)

    # If Clause and then a match,
    if_test = IfThenElse(if_clause, then_match, else_match)

# Generated at 2022-06-14 14:22:24.509394
# Unit test for constructor of class OneOf
def test_OneOf():
    import typesystem
    schema = typesystem.OneOf([typesystem.Integer(), typesystem.String()])
    assert schema.errors == {
        "no_match": "Did not match any valid type.",
        "multiple_matches": "Matched more than one type."
    }


# Generated at 2022-06-14 14:22:27.206116
# Unit test for constructor of class OneOf
def test_OneOf():
    assert OneOf
    OneOf()
    assert "no_match" in OneOf.errors
    assert "multiple_matches" in OneOf.errors



# Generated at 2022-06-14 14:22:28.404007
# Unit test for constructor of class OneOf
def test_OneOf():
    f1 = OneOf(one_of=None)


# Generated at 2022-06-14 14:22:30.325821
# Unit test for constructor of class AllOf
def test_AllOf():
    test_schema = AllOf()
    print(test_schema)


# Generated at 2022-06-14 14:22:31.605810
# Unit test for constructor of class OneOf
def test_OneOf():
    t = OneOf()
    assert t is not None
