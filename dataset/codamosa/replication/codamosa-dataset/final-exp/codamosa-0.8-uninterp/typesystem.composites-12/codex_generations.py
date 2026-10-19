

# Generated at 2022-06-14 14:12:46.201252
# Unit test for constructor of class AllOf
def test_AllOf():
    field = AllOf([])



# Generated at 2022-06-14 14:12:53.800349
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    class Number(Field):
        """
        Represents a positive number.
        """

        errors = {"invalid": "Must be a number."}

        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            if isinstance(value, int):
                return value
            else:
                raise self.validation_error("invalid")

    assert IfThenElse(if_clause=Number(), then_clause=Number()).validate(1) == 1
    assert IfThenElse(
        if_clause=Number(), then_clause=Number(), else_clause=Number()
    ).validate(1) == 1



# Generated at 2022-06-14 14:12:56.704969
# Unit test for method validate of class Not
def test_Not_validate():
    b = Not(AllOf([String(), Integer()]))
    value = "hello"
    b.validate(value)
    assert True



# Generated at 2022-06-14 14:13:02.401938
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    from typesystem import Integer
    if_clause  = Integer(minimum=0)
    then_clause= Integer(maximum=5)
    else_clause= Integer(maximum=4)
    if_then_else = IfThenElse(if_clause, then_clause, else_clause)
    assert if_then_else.validate(2) == 2

# Generated at 2022-06-14 14:13:05.137358
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    field = NeverMatch()
    assert field.errors == {'never': 'This never validates.'}


# Generated at 2022-06-14 14:13:07.518900
# Unit test for method validate of class Not
def test_Not_validate():
    x = Not(AllOf)
    x.validate(1)
    assert x.validate(1) == 1


# Generated at 2022-06-14 14:13:11.336753
# Unit test for constructor of class AllOf
def test_AllOf():
    assert "all_of" not in dir(AllOf(all_of=[Any()]))
    assert "allow_null" not in dir(AllOf(all_of=[Any()]))
    assert "kwargs" not in dir(AllOf(all_of=[Any()]))


# Generated at 2022-06-14 14:13:15.918873
# Unit test for constructor of class AllOf
def test_AllOf():
    from typesystem import Object

    class Person(Object):
        name = String
        age = String

    # Create an Object with different types
    test_Object = AllOf([String, Integer])
    test_Person = AllOf([Person])
    test_Object2 = AllOf([String, Integer])
    test_Object3 = AllOf([String, Float])

    assert test_Object != test_Object2


# Generated at 2022-06-14 14:13:22.949751
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    # Define the test parameters
    value = 'value'
    strict = 0
    field = IfThenElse(if_clause=Any(), then_clause=Any(), else_clause=Any())

    # Define the expected results
    expected_result = value
    expected_error = None

    # Execute the test
    result, error = field.validate_or_error(value, strict)

    # Check the results
    assert result == expected_result
    assert error == expected_error
# End of method unit test

# Generated at 2022-06-14 14:13:26.707262
# Unit test for method validate of class Not
def test_Not_validate():
    some_int = 5
    not_int = Not(Integer())
    not_int.validate(some_int)
    some_str = "Hello World!"
    not_int.validate(some_str)


# Generated at 2022-06-14 14:13:36.552499
# Unit test for method validate of class Not
def test_Not_validate():
    n = Not(String())
    res, err = n.validate_or_error("A string")
    assert err

    res, err = n.validate_or_error(123)
    assert not err

    with pytest.raises(ErrorMessage) as excinfo:
        n.validate(123)

    assert "negated" in str(excinfo.value)


# Generated at 2022-06-14 14:13:40.714306
# Unit test for method validate of class Not
def test_Not_validate():
    # test with valid input
    n = Not(Integer(), min_value=1)
    n.validate(value=2)

    # test error
    with pytest.raises(ValidationError):
        n.validate(value=0)


# Generated at 2022-06-14 14:13:51.932307
# Unit test for method validate of class Not
def test_Not_validate():
    not_field = Not(String())
    assert not_field.validate(1) == 1
    not_field.validate(1)
    not_field.validate(1)
    assert not not_field.validate(1) is None
    not_field.validate(1)
    not_field.validate(1)
    assert not not_field.validate(1) is None
    assert not_field.validate(1) == 1
    not_field.validate(1)
    not_field.validate(1)
    assert not not_field.validate(1) is None
    assert not_field.validate(1) == 1
    not_field.validate(1)
    not_field.validate(1)
    assert not not_field.validate(1) is None

# Generated at 2022-06-14 14:13:59.653866
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    class A():
        def __init__(self, any: int):
            self.any = any
    class B():
        def __init__(self, any):
            self.any = any
    class C():
        def __init__(self, any):
            self.any = any
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
    class Employee(Person):
        def __init__(self, name, age, emp_id):
            Person.__init__(self, name, age)
            self.emp_id = emp_id
    class Bool(Field):
        def __init__(self, **kwargs: typing.Any) -> None:
            super().__init__(**kwargs)

# Generated at 2022-06-14 14:14:03.254706
# Unit test for method validate of class Not
def test_Not_validate():
#Input
    negated = Any()
#Expected Output
    expected = 1
#Computed Output
    result = Not(negated).validate(1)
#Check if expected and computed are same
    assert result == expected

# Generated at 2022-06-14 14:14:05.651233
# Unit test for method validate of class Not

# Generated at 2022-06-14 14:14:07.525058
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    f = NeverMatch()
    assert f.errors == {"never": "This never validates."}


# Generated at 2022-06-14 14:14:20.267618
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    # Test case where value is validated by then_clause
    field = IfThenElse(String(max_length=1), String(min_length=10))
    assert field.validate("X") == "X"
    # Test case where value is validated by else_clause, as if_clause fails
    field = IfThenElse(String(min_length=10),String(),String(max_length=1))
    assert field.validate("X") == "X"
    # Test case where value is not validated, ie. both if_clause and else_clause fail
    field = IfThenElse(String(min_length=10),String(),String(min_length=2))
    try:
        field.validate("X")
    except Exception as e:
        assert isinstance(e, ValidationError)

# Generated at 2022-06-14 14:14:25.809404
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    from typesystem.fields import Integer

    if_clause = Integer()
    then_clause = Integer()
    else_clause = Integer()
    myfield = IfThenElse(if_clause, then_clause, else_clause)

    assert myfield.validate(5) == 5
    assert myfield.validate(-9) == -9
    assert myfield.validate(-10) == -10

# Generated at 2022-06-14 14:14:29.961560
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    assert IfThenElse(String(), Number()).validate(1) == 1
    assert IfThenElse(Number(), String(), Number()).validate(1) == 1
    assert IfThenElse(Number(), String(), Number()).validate("1") == "1"



# Generated at 2022-06-14 14:14:39.888317
# Unit test for method validate of class Not
def test_Not_validate():
    not_a_number = Not(Number())

    # Test with a string
    try:
        not_a_number.validate("Drake")
    except ValidationError:
        pass
    else:
        raise Exception("Error not raised")
    
    # Test with an integer
    try:
        not_a_number.validate(5)
    except ValidationError:
        raise Exception("Should not have raised")



# Generated at 2022-06-14 14:14:45.186277
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    class Foo(Field):
        def validate(self, value, strict):
            return value
    
    obj = IfThenElse(Foo(), Foo())

    assert obj.validate(None) == None
    assert obj.validate(True) == None
    assert obj.validate("hello") == None

# Generated at 2022-06-14 14:14:50.600711
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    import typesystem
    class IfThenField(typesystem.IfThenElse):
        def if_clause(self, value):
            return value > 10
        def then_clause(self, value):
            return value + 10
        def else_clause(self, value):
            return value - 10
    it = IfThenField()
    assert it.validate(20) == 30
    assert it.validate(5) == -5
    assert it.validate(10) == 0

# Generated at 2022-06-14 14:14:52.747788
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    field = OneOf([Any(), Any()])
    assert field.validate("foo") == "foo"



# Generated at 2022-06-14 14:15:01.522263
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    class CheckEqual(Field):
        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            if value == '2':
                raise self.validation_error('any_error')
            return value

    if_clause = CheckEqual()
    then_clause = CheckEqual()
    else_clause = CheckEqual()

    conditional = IfThenElse(if_clause, then_clause, else_clause)

    assert '2' == conditional.validate('2')
    assert '3' == conditional.validate('3')

# Generated at 2022-06-14 14:15:05.461697
# Unit test for method validate of class Not
def test_Not_validate():
    result = Not(AllowNone(Any())).validate(1)
    assert(result == 1)
    try:
        Not(AllowNone(Any())).validate(None)
        assert(False)
    except:
        assert(True) # reached

# Generated at 2022-06-14 14:15:09.614300
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    assert IfThenElse(Number(minimum=0, multiple_of=2), Number(multiple_of=5)).validate(10) == 10
    with pytest.raises(typesystem.Error):
        IfThenElse(Number(minimum=0, multiple_of=2), Number(multiple_of=7)).validate(10)

# Generated at 2022-06-14 14:15:16.831730
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    from typesystem import Integer
    i1 = Integer(max_value=2)
    i2 = Integer(max_value=3)
    i3 = Integer(max_value=4)
    ite = IfThenElse(i1, i2, i3)
    print(ite.validate(1))
    print(ite.validate(2))
    print(ite.validate(3))
    print(ite.validate(4))
# test_IfThenElse_validate()

# Generated at 2022-06-14 14:15:23.764130
# Unit test for method validate of class Not
def test_Not_validate():
    # Arrange
    field = Not(negated=Integer(gte=0), description="Not positive integer")

    # Act
    # Assert
    assert field.validate(5) == 5
    field.validate(-10)
    # since the field only returns value, error cannot be caught
    # Thus we need to catch the error returned by validate_or_error()
    _, error = field.validate_or_error(-10)
    assert error != None


# Generated at 2022-06-14 14:15:27.251675
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    """
    Unit test method validate of class IfThenElse
    """
    int_field = Int()
    string_field = String()
    field = IfThenElse(int_field, then_clause = string_field)
    field.validate('abc')

# Generated at 2022-06-14 14:15:37.113725
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    class A(Field):

        def _cast(self, value: typing.Any) -> typing.Any:
            return value + "A"

    class B(Field):

        def _cast(self, value: typing.Any) -> typing.Any:
            return value + "B"


    f = OneOf([A(), B()])
    assert f.validate("A") == "AA"
    # If a value matches more than one type, an error will be raised
    with pytest.raises(OneOf.validation_error) as exc_info:
        f.validate("B")
    assert str(exc_info.value) == "Matched more than one type."
    with pytest.raises(OneOf.validation_error) as exc_info:
        f.validate("C")

# Generated at 2022-06-14 14:15:42.822822
# Unit test for constructor of class AllOf
def test_AllOf():
    # arrange
    Field1 = NeverMatch()
    Field2 = NeverMatch()
    listField = [Field1, Field2]

    # act
    allOf = AllOf(listField)
    # assert
    assert allOf.all_of == listField
    assert allOf.errors == {}
    assert allOf.description == None
    assert allOf.formats == []
    assert allOf.meta == {}
    assert allOf.default == None
    assert allOf.required == False
    assert allOf.name == None


# Generated at 2022-06-14 14:15:49.343993
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    Field.message_templates['invalid']= '{input} no es un {field}'
    i = IfThenElse(Integer(),String())
    i.validate(1)
    i.validate('1')
    try:
        i.validate('a')
    except Exception as e:
        assert str(e) == "'a' no es un IfThenElse"


# Generated at 2022-06-14 14:15:58.667086
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    # if_clause is valid
    if_clause = Field(allow_null=True)
    then_clause = Field(allow_null=True)
    else_clause = Field(allow_null=True)
    if_then_else = IfThenThenElse(if_clause=if_clause, then_clause=then_clause, else_clause=else_clause)

    if_clause.validate("foo")
    then_clause.validate("foo")
    else_clause.validate("foo")

    assert if_then_else.validate(None) == then_clause.validate(None)

    # if_clause raise error
    else_clause.validate("foo")

    assert if_then_else.validate("foo") == else_clause.valid

# Generated at 2022-06-14 14:15:59.779470
# Unit test for constructor of class AllOf
def test_AllOf():
    AllOf([])

# Generated at 2022-06-14 14:16:07.444440
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    from typesystem.fields import String
    from typesystem.exceptions import ValidationError
    from typesystem.fields import Integer
    from typesystem.fields import Boolean
    field1 = String()
    field2 = Integer()

    field3 = IfThenElse(field1, field2, Boolean())
    field3.validate('Hello')
    try:
        field3.validate(0)
    except ValidationError:
        assert True
    try:
        field3.validate(False)
    except ValidationError:
        assert True


# Generated at 2022-06-14 14:16:12.296991
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    if_clause = Field()
    then_clause = Field()
    else_clause = Field()
    if_then_else = IfThenElse(if_clause, then_clause, else_clause)
    assert if_then_else.if_clause == if_clause
    assert if_then_else.then_clause == then_clause
    assert if_then_else.else_clause == else_clause

# Generated at 2022-06-14 14:16:16.148100
# Unit test for method validate of class Not
def test_Not_validate():
    n = Not(String())
    assert n.validate("hello") == "hello"
    try:
        n.validate(5)
    except:
        assert True
    else:
        assert False


# Generated at 2022-06-14 14:16:16.709377
# Unit test for constructor of class AllOf
def test_AllOf():
    assert True

# Generated at 2022-06-14 14:16:20.057701
# Unit test for method validate of class Not
def test_Not_validate():
    n = Not(None)
    n.negated=Any()
    _, error = n.negated.validate_or_error(False, strict=False)
    if error is None:
        assert True
    else:
        assert False

# Generated at 2022-06-14 14:16:30.628662
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    # Create an object to test
    ite = IfThenElse(if_clause = 'StringField()', then_clause = 'StringField()', else_clause = 'StringField()')
    
    # For coverage
    # The variable is not used here, but the class will raise a coverage error when we try to call validate without passing the value argument
    # This could be done because we could have a custom logic in this function.    
    value = 'test_IfThenElse_validate'
    ite.validate(value, strict = False)
    


# Generated at 2022-06-14 14:16:35.499107
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    if_clause = Field("if clause", required=True)
    then_clause = Field("then clause", required=True)
    else_clause = Field("else clause", required=True)
    if_then_else = IfThenElse(if_clause=if_clause, then_clause=then_clause, else_clause=else_clause)
    value = None
    strict = False
    value = if_then_else.validate(value, strict)
    assert value == None

# Generated at 2022-06-14 14:16:37.080848
# Unit test for constructor of class AllOf
def test_AllOf():
    # Test with default value given
    assert AllOf(all_of=[])

# Generated at 2022-06-14 14:16:44.854184
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    "Unit test for method validate of class IfThenElse"
    if_clause = Field("a")
    then_clause = Field("b")
    else_clause = Field("c")
    ite = IfThenElse(if_clause, then_clause, else_clause)
    value = "a"
    try:
        ite.validate(value)
    except Exception as exc:
        assert False, "Unexpected exception for value=" + str(value) + ": " + str(exc)

# Generated at 2022-06-14 14:16:53.764726
# Unit test for method validate of class Not
def test_Not_validate():
    ErrorString = "Must not match."
    # The test case 
    testcase_list = [[{"a":1}, ErrorString],
                    [5, ErrorString],
                    ["This is a string", ErrorString]
                    ]

    # Initialize an AllOf object
    Not_instance = Not(Any())

    # Check if the test cases pass
    counter = 1
    for testcase in testcase_list:
        output= Not_instance.validate(testcase[0])
        testcase_result = "Pass" if output == testcase[1] else "fail"
        print("Test case " + str(counter) + " " + testcase_result)
        counter = counter + 1

test_Not_validate()

# Generated at 2022-06-14 14:16:56.616346
# Unit test for method validate of class Not
def test_Not_validate():
    Not(negated=Any()).validate("hello")
    assert (Not(negated=NeverMatch()).validate("hello")=="hello")


# Generated at 2022-06-14 14:17:03.619778
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    if_clause = Any()
    then_clause = Any()
    else_clause = Integer()

    result = IfThenElse(if_clause, then_clause, else_clause).validate("a")
    assert result == "a"

    # result = IfThenElse(if_clause, then_clause, else_clause).validate(1)
    # assert result == 1

test_IfThenElse_validate()

# Generated at 2022-06-14 14:17:07.809588
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    test_value = 7
    test_field = IfThenElse(
        if_clause = Field(),
        then_clause = Field(),
        else_clause = Field()
    )
    assert test_field.validate(test_value) == 7


# Generated at 2022-06-14 14:17:17.643451
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    class Test1(IfThenElse):
        def __init__(self, **kwargs: typing.Any) -> None:
            super().__init__(self, **kwargs)
    class Test2(IfThenElse):
        def __init__(self, **kwargs: typing.Any) -> None:
            super().__init__(self, **kwargs)
    # Test 1: If-then clause are valid.
    t1 = Test1(if_clause=Any(), then_clause=Any())
    t1.validate(True)
    # Test 2: If-then clause are invalid.
    t2 = Test2(if_clause=Any(), then_clause=Any())
    t2.validate(None)
    # Test 3: If-then clause are valid and else clause is valid

# Generated at 2022-06-14 14:17:19.471048
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    f1 = IfThenElse(if_clause=Field(), then_clause=Field())

# Generated at 2022-06-14 14:17:32.948497
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    if_clause = Field('if_clause', max_length=2)
    then_clause = Field('then_clause')
    else_clause = Field('else_clause', max_length=3)
    if_then_else = IfThenElse(if_clause, then_clause, else_clause)
    if_then_else.validate('if_clause')
    if_then_else.validate('el')

# Generated at 2022-06-14 14:17:33.571782
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    pass

# Generated at 2022-06-14 14:17:39.005617
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    field = IfThenElse('42')
    assert field.validate(4) == 4
    with pytest.raises(typesystem.exceptions.ValidationError) as e:
        field.validate(42)
    assert str(e) == '{"then": ["This field is required."]}'

# Generated at 2022-06-14 14:17:42.442762
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    field = IfThenElse(None, then_clause=1)
    assert field.validate(1) == 1
    field = IfThenElse(None, else_clause=2)
    assert field.validate(1) == 2

# Generated at 2022-06-14 14:17:54.093264
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    # Create instance of IfThenElse
    if_clause = String()
    then_clause = String()
    else_clause = String()
    if_then_else = IfThenElse(if_clause, then_clause, else_clause)
    # Test validate method
    def func1(value):
        return isinstance(value, str)
    def func2(value):
        return isinstance(value, str)
    def func3(value):
        return isinstance(value, str)
    if_clause.validate = func1
    then_clause.validate = func2
    else_clause.validate = func3
    assert if_clause.validate(10) == if_then_else.if_clause.validate(10)

# Generated at 2022-06-14 14:17:58.899390
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    if_clause = Field(type="number")
    then_clause = Field(type="string")
    else_clause = Field(type="string")
    field = IfThenElse(if_clause, then_clause, else_clause)
    assert field.validate(3) == "3"
    assert field.validate("a") == "a"
    assert field.validate(None) == None

# Generated at 2022-06-14 14:18:09.421008
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    class Color(Field):
        errors = {
            "not_red": "Value is not red.",
            "not_green": "Value is not green.",
        }

    red_color = Color(
        error_messages=Color.errors,
        validators=[lambda value: value == "red",],
    )
    green_color = Color(
        error_messages=Color.errors,
        validators=[lambda value: value == "green",],
    )
    blue_color = Color(
        error_messages=Color.errors,
        validators=[lambda value: value == "blue",],
    )
    yellow_color = Color(
        error_messages=Color.errors,
        validators=[lambda value: value == "yellow",],
    )


# Generated at 2022-06-14 14:18:16.397576
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    from typesystem.fields import Integer

    field = IfThenElse(
        if_clause=Integer(),
        then_clause=Integer(),
        else_clause=Integer(),
    )

    value = 1
    assert field.validate(value) == 1

    value = '1'
    assert field.validate(value) == 1

    value = 'a'
    assert field.validate(value) == 1

    value = 1
    assert field.validate(value) == 1



# Generated at 2022-06-14 14:18:25.162149
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    assert IfThenElse().validate(1) == 1
    assert IfThenElse().validate(1.2) == 1.2
    assert IfThenElse().validate(True) == True
    assert IfThenElse().validate(False) == False
    assert IfThenElse().validate('') == ''
    assert IfThenElse().validate('test') == 'test'
    assert IfThenElse().validate([]) == []
    assert IfThenElse().validate(['test']) == ['test']
    assert IfThenElse().validate({}) == {}
    assert IfThenElse().validate({'test': 1}) == {'test': 1}

# Generated at 2022-06-14 14:18:26.929451
# Unit test for constructor of class AllOf
def test_AllOf():
    field = AllOf(all_of = [Any(), Any()])


# Generated at 2022-06-14 14:18:36.530723
# Unit test for constructor of class AllOf
def test_AllOf():
    test = AllOf([])
    assert(test.all_of == [])


# Generated at 2022-06-14 14:18:38.313325
# Unit test for constructor of class AllOf
def test_AllOf():
    """
    Test the constructor of class AllOf
    """
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 14:18:41.150476
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    assert IfThenElse(1, 2, 3, default=5).validate(1) == 2
    assert IfThenElse(1, 2, 3, default=5).validate(2) == 5

# Generated at 2022-06-14 14:18:42.554122
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    assert IfThenElse(IfThenElse('true')).validate('true') == 'true'

# Generated at 2022-06-14 14:18:44.418025
# Unit test for constructor of class AllOf
def test_AllOf():
    x = AllOf(["bob", "fred"])
    assert x is not None

# Generated at 2022-06-14 14:18:48.264538
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    from typesystem.fields import String

    ite = IfThenElse(String())
    ite.validate("testing")

    # nothing is thrown, so the test passed
    assert True

# Generated at 2022-06-14 14:18:58.428427
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    expected = "expected"

    class ThenClause(Field):
        def validate(self, value: object, strict: bool = False) -> object:
            return expected

    class ElseClause(Field):
        def validate(self, value: object, strict: bool = False) -> object:
            return "unexpected"

    class IfClause(Field):
        def validate(self, value: object, strict: bool = False) -> object:
            raise AssertionError("should not have been called")

    assert expected == IfThenElse(if_clause=IfClause(), then_clause=ThenClause()).validate("anything")
    assert expected == IfThenElse(if_clause=IfClause(), else_clause=ElseClause()).validate("anything")

# Generated at 2022-06-14 14:19:06.003508
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    import typesystem
    class IfThenElse(typesystem.types.IfThenElse):
        def _validate_(self, value):
            pass
    obj = IfThenElse(
        if_clause = typesystem.types.Any(),
        then_clause = typesystem.types.Any(),
        else_clause = typesystem.types.Any()
    )
    obj.validate(None)


# Generated at 2022-06-14 14:19:17.807036
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    import unittest.mock as mock
    import typesystem
    with mock.patch('typesystem.fields.error_handler') as mocked_error_handler:
        mocked_error_handler.return_value = None
        x = typesystem.IfThenElse(typesystem.String(),then_clause=typesystem.String(min_length=3))
        res = x.validate("asd")
        assert res == "asd"
        x = typesystem.IfThenElse(typesystem.String(),then_clause=typesystem.String(min_length=3))
        res = x.validate("as")
        assert res == "as"
        x = typesystem.IfThenElse(typesystem.String(),then_clause=typesystem.String(min_length=3))
        res = x.validate(None)


# Generated at 2022-06-14 14:19:19.651723
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    IfThenElse(if_clause=None, then_clause=None, else_clause=None)
    assert True

# Generated at 2022-06-14 14:19:30.454069
# Unit test for constructor of class AllOf
def test_AllOf():
    all_of = AllOf(all_of=list())
    assert all_of


# Generated at 2022-06-14 14:19:31.892048
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    one_of = typing.List[Field]
    field = OneOf(one_of)
    value = 1
    strict = False
    assert field.validate(value, strict) == value


# Generated at 2022-06-14 14:19:37.989645
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    import unittest
    from typesystem.exceptions import ValidationError
    from typesystem.types import Integer, String

    class TestClass(unittest.TestCase):
         def test_val(self):
            obj = IfThenElse(if_clause=Integer(),then_clause=String())
            self.assertRaises(ValidationError, obj.validate, 12.6)
            self.assertRaises(ValidationError, obj.validate, "12")
            obj = IfThenElse(if_clause=String(),then_clause=Integer())
            self.assertRaises(ValidationError, obj.validate, 12)
            self.assertRaises(ValidationError, obj.validate, 12.6)
            obj = IfThenElse(if_clause=Integer(),then_clause=Integer())
           

# Generated at 2022-06-14 14:19:45.791196
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    from typesystem import ValidationError
    class MyField(Field):
        def to_python(self, value):
            return "Dirty"
    class MyField2(Field):
        def to_python(self, value):
            return "Dirty2"
    one_of = OneOf([MyField(), MyField2()])
    #test with valid value
    assert one_of.validate('Clean') == 'Dirty'
    #test with invalid value
    try:
        one_of.validate('Clean2')
    except ValidationError:
        assert True
    else:
        assert False


# Generated at 2022-06-14 14:19:50.970891
# Unit test for constructor of class AllOf
def test_AllOf():
    import typesystem
    int_field = typesystem.Integer()
    float_field = typesystem.Float()
    value = 1.0
    allof = typesystem.AllOf([int_field, float_field])
    allof.validate(1.0)
    allof.validate(1)
    assert allof.errors == {}


# Generated at 2022-06-14 14:19:56.251955
# Unit test for constructor of class AllOf
def test_AllOf():
    from typesystem.fields import String

    a = String()
    b = String()
    c = String()
    d = String()
    e = String()

    x=AllOf([a,b,c,d,e])
    d=x.validate("test")
    assert d=="test"



# Generated at 2022-06-14 14:20:02.451764
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    field = IfThenElse(
        String(max_length=10), String(min_length=5), String(min_length=2)
    )
    assert field.validate('a') == 'a'
    assert field.validate('ab') == 'ab'
    assert field.validate('abcde') == 'abcde'
    assert field.validate('abcdefghij') == 'abcdefghij'
    assert field.validate('abcdefghijk') == 'abcdefghijk'



# Generated at 2022-06-14 14:20:07.351072
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    assert OneOf(one_of=[Any()]).validate(True)
    try:
        OneOf(one_of=[NeverMatch()]).validate("abc")
        assert False
    except ValueError:
        pass
    try:
        OneOf(one_of=[NeverMatch(), NeverMatch()]).validate("abc")
        assert False
    except ValueError:
        pass


# Generated at 2022-06-14 14:20:10.346505
# Unit test for constructor of class AllOf
def test_AllOf():
    assert AllOf
    assert AllOf([])
    assert AllOf([], name='hogehoge')
    assert AllOf([], label='hogehoge')
    assert AllOf([], description='hogehoge')

# Generated at 2022-06-14 14:20:19.946825
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    class IfThen(Field):
        def __init__(self, if_clause: Field, then_clause: Field, **kwargs: typing.Any) -> None:
            super().__init__(**kwargs)
            self.if_clause = if_clause
            self.then_clause = then_clause 

        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            # cnd, err = self.if_clause.validate_or_error(value, strict = strict)
            # if err is None:
            return self.then_clause.validate(value, strict=strict)

# Generated at 2022-06-14 14:20:40.185832
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
        test_field = IfThenElse(Any(),then_clause=Any(),else_clause=Any())
        test_value = 5
        assert test_field.validate(test_value) == 5
        test_field = IfThenElse(NeverMatch(),then_clause=Any(),else_clause=Any())
        assert test_field.validate(test_value) == 5


# Generated at 2022-06-14 14:20:41.962446
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    value = 'test'
    field = IfThenElse(
        if_clause=Any(),
        then_clause=Any(),
        else_clause=Any()
    )
    field._validate(value)

# Generated at 2022-06-14 14:20:45.325839
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    a = IfThenElse(1, then_clause=2, else_clause=3)
    assert a.if_clause == 1
    assert a.then_clause == 2
    assert a.else_clause == 3



# Generated at 2022-06-14 14:20:48.019405
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    assert IfThenElse(String()).validate("x") is None
    assert IfThenElse(String()).validate(3) == 3 


# Generated at 2022-06-14 14:20:55.384903
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    def test_cases(test_input, test_output):
        if (len(test_input) == 2):
            assert IfThenElse(test_input[0], test_input[1], None).validate(test_output) == test_output
        else:
            assert IfThenElse(test_input[0], test_input[1], test_input[2]).validate(test_output) == test_output
    
    test_cases([String(), String()], "abc123")
    test_cases([Integer(), String()], "abc123")
    test_cases([Integer(), String(), String()], "abc123")


# Generated at 2022-06-14 14:21:04.084089
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    f = IfThenElse(if_clause=Any(), then_clause=Any())
    assert f.validate({"a": 1}) == {"a": 1}
    assert f.validate(1) == 1

    f = IfThenElse(if_clause=Any(), then_clause=Any(), else_clause=Any())
    assert f.validate({"a": 1}) == {"a": 1}
    assert f.validate(1) == 1

    f = IfThenElse(if_clause=Any(), else_clause=Any())
    assert f.validate({"a": 1}) == {"a": 1}
    assert f.validate(1) == 1

# Generated at 2022-06-14 14:21:10.265748
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    if_clause = Bool()
    then_clause = Int()
    else_clause = Str()
    if_then_else = IfThenElse(if_clause, then_clause, else_clause)
    assert if_then_else.validate(True) == 0
    assert if_then_else.validate(False) == ""
    assert if_then_else.validate(None) == None
    assert if_then_else.validate("") == None
    assert if_then_else.validate("hello") == None

# Generated at 2022-06-14 14:21:16.470797
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    if_clause = Field(type="string", pattern=r"^\w+\d+$")
    then_clause = Field(type="string", min_length=5)
    else_clause = Field(type="string", max_length=3)
    instance = IfThenElse(if_clause=if_clause, then_clause=then_clause, else_clause=else_clause)
    assert instance.validate("a1") == "a1"
    assert instance.validate("a") == "a"
    try:
        instance.validate(1)
        assert False
    except ValidationError:
        pass
    try:
        instance.validate("abcde")
        assert False
    except ValidationError:
        pass



# Generated at 2022-06-14 14:21:26.958485
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    if_clause = Field()
    if_clause.errors = {"if_clause": "If clause"}
    then_clause = Field()
    then_clause.errors = {"then_clause": "Then clause"}
    else_clause = Field()
    else_clause.errors = {"else_clause": "Else clause"}

    clause = IfThenElse(
        if_clause,
        then_clause=then_clause,
        else_clause=else_clause,
    )

    def get_error_message(e: typing.Any) -> str:
        return e.messages["IfThenElse"][0]

    # if branch
    _, error = if_clause.validate_or_error(1)
    assert get_error_message(error) == "If clause"

# Generated at 2022-06-14 14:21:35.674410
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    class Field1(Field):
        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            return True
    class Field2(Field):
        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            return value
    class Field3(Field):
        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            return value
    if_clause = Field1()
    then_clause = Field2()
    else_clause = Field3()
    field = IfThenElse(if_clause, then_clause, else_clause)
    value = 3
    assert field.validate(value) == value
    assert field.validate(value) != True

# Generated at 2022-06-14 14:21:49.239731
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    if_clause = String()
    then_clause = String()
    else_clause = String()
    ifThenElse = IfThenElse(if_clause,then_clause,else_clause)
    assert(ifThenElse.if_clause == if_clause)
    assert(ifThenElse.then_clause == then_clause)
    assert(ifThenElse.else_clause == else_clause)
    return


# Generated at 2022-06-14 14:21:57.492839
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    import json
    schema = json.load(open('tests/json_schema/if_then_else.json'))
    typesystem.parse_schema_to_types(schema, 'tests/json_schema/if_then_else.py')
    from tests.json_schema.if_then_else import IfThenElse1
    print(IfThenElse1(3).validate(3))
    from tests.json_schema.if_then_else import IfThenElse2
    print(IfThenElse2(2).validate(2))
    from tests.json_schema.if_then_else import IfThenElse3
    print(IfThenElse3(1).validate(1))

# Generated at 2022-06-14 14:21:59.134567
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    field = IfThenElse(String(max_length=5), String(max_length=10))
    field.validate("hello")

    field = IfThenElse(Dict(properties={"a": Integer()}), String(max_length=10))
    field.validate({"hello": "world"})

# Generated at 2022-06-14 14:22:04.783726
# Unit test for constructor of class IfThenElse
def test_IfThenElse():  # noqa
    if_clause = Field()
    then_clause = Field()
    else_clause = Field()
    
    condition = { 
        "if": if_clause,
        "then": then_clause,
        "else": else_clause
    }
    myinstance = IfThenElse(**condition) # noqa
    assert myinstance.if_clause == if_clause
    assert myinstance.then_clause == then_clause
    assert myinstance.else_clause == else_clause
    
    

# Generated at 2022-06-14 14:22:11.260451
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    from typesystem import Integer

    if_clause = Integer()
    then_clause = Integer()
    else_clause = Integer()

    conditional_field = IfThenElse(if_clause,
                                   then_clause,
                                   else_clause)
    assert conditional_field.if_clause == if_clause
    assert conditional_field.then_clause == then_clause
    assert conditional_field.else_clause == else_clause

# Generated at 2022-06-14 14:22:16.656769
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    assert IfThenElse(if_clause=Any(), then_clause=None, else_clause=None).if_clause == Any()
    assert IfThenElse(if_clause=Any(), then_clause=None, else_clause=None).then_clause == Any()
    assert IfThenElse(if_clause=Any(), then_clause=None, else_clause=None).else_clause == Any()

# Generated at 2022-06-14 14:22:17.679696
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    IfThenElse(Field(),Field())


# Generated at 2022-06-14 14:22:20.665965
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    f = IfThenElse(AllowNull(String()))
    f = IfThenElse(AllowNull(String()), AllowNull(String()))
    f = IfThenElse(AllowNull(String()), AllowNull(String()), AllowNull(String()))


# Generated at 2022-06-14 14:22:22.113694
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    f = IfThenElse(Any(), Any(), Any(), description='If-Then-Else')

# Generated at 2022-06-14 14:22:22.630695
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    pass