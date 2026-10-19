

# Generated at 2022-06-14 14:12:53.462276
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    print("test_OneOf_validate")

    try:
        _, error = OneOf([String()], min_length=1).validate_or_error("")
        assert error == "min_length"
    except Exception:
        assert False

    try:
        _, error = OneOf([String(min_length=2)]).validate_or_error("1")
        assert error == "min_length"
    except Exception:
        assert False

    try:
        _, error = OneOf([String(min_length=2), Integer()]).validate_or_error("1")
        assert error == "no_match"
    except Exception:
        assert False


# Generated at 2022-06-14 14:13:05.825554
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    if_clause_field = String()
    then_clause_field = Integer()
    else_clause_field = Array()
    obj = {"foo": "a"}
    
    assert IfThenElse(if_clause=if_clause_field,then_clause=then_clause_field,else_clause=else_clause_field).validate(obj) == obj
    obj = {'foo': 1}
    with pytest.raises(ValidationError):
        IfThenElse(if_clause=if_clause_field,then_clause=then_clause_field,else_clause=else_clause_field).validate(obj)
    obj = {'bar': 1}

# Generated at 2022-06-14 14:13:13.492157
# Unit test for method validate of class Not
def test_Not_validate():
    f = Not(Integer())
    assert f.validate(-1) == -1
    assert f.validate(-12.3) == -12.3
    assert f.validate('aaa') == 'aaa'
    try:
        f.validate(123)
    except ErrorMessage as e:
        assert e.code == 'negated'
    try:
        f.validate(12.3)
    except ErrorMessage as e:
        assert e.code == 'negated'
    try:
        f.validate(None)
    except ErrorMessage as e:
        assert e.code == 'negated'
    try:
        f.validate('123')
    except ErrorMessage as e:
        assert e.code == 'negated'


# Generated at 2022-06-14 14:13:25.342703
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    from typesystem.fields import Integer
    from typesystem.schema import Schema
    from typesystem.types import Object
    from typesystem.validators import Equal

    if_clause = Object(properties={"a": Integer(validators=[Equal(1)])})
    then_clause = Object(properties={"b": Integer()})
    else_clause = Integer()

    schema = Schema({"a": IfThenElse(if_clause, then_clause, else_clause)})

    # correct cases
    assert schema.validate({"a": {"a": 1, "b": 3}}) == {"a": {"a": 1, "b": 3}}
    assert schema.validate({"a": 4}) == {"a": 4}

    # wrong cases

# Generated at 2022-06-14 14:13:32.384527
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    assert OneOf([Field()]).validate([Field()]) == [[Field()]]
    assert OneOf([Field(), Field()]).validate(Field()) == Field()
    from typesystem.exceptions import ValidationError
    try:
        OneOf([Field(), Field()]).validate(Field(required=False))
    except ValidationError:
        pass
    else:
        raise Exception("Test failed.")


# Generated at 2022-06-14 14:13:36.898441
# Unit test for method validate of class Not
def test_Not_validate():
    boolean = Boolean()
    not_boolean = Not(boolean)
    not_boolean.validate(0)
    try:
        not_boolean.validate(True)
        assert False
    except ValidationError:
        assert True

# Generated at 2022-06-14 14:13:41.244877
# Unit test for constructor of class AllOf
def test_AllOf():
    from typing import List
    from typesystem.fields import Integer

    field = AllOf([Integer()])
    assert isinstance(field, AllOf)
    assert isinstance(field.all_of, List)
    assert field.all_of[0].__class__.__name__ == "Integer"


# Generated at 2022-06-14 14:13:48.507448
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    assert OneOf(one_of=[str, int]).validate("1") == "1"
    assert OneOf(one_of=[int, str]).validate("1") == "1"
    assert OneOf(one_of=[int, str]).validate(1) == 1
    assert OneOf(one_of=[int, int]).validate("1") != "1"
    assert OneOf(one_of=[int, int]).validate("1") is not "1"


# Generated at 2022-06-14 14:13:50.710923
# Unit test for method validate of class Not
def test_Not_validate():
    assert Not(Any()).validate("Hello") == "Hello"
    assert Not(String()).validate("Hello") == "Hello"


# Generated at 2022-06-14 14:13:56.027636
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    # create dummy values of class Field
    if_clause = Field()
    then_clause = Field()
    else_clause = Field()
    # create IfThenElse Field with dummy values
    field = IfThenElse(if_clause, then_clause, else_clause)
    # create dummy input value
    value = None
    # call IfThenElse validate method
    result = field.validate(value)
    # assert result is None
    assert result == None

# Generated at 2022-06-14 14:14:07.149334
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    from typesystem.fields import Float, Integer
    ite = IfThenElse(if_clause=Integer(), then_clause=Integer(minimum=1), else_clause=Float())
    print(ite.validate(1))
    print(ite.validate(0))
    print(ite.validate(0.5))
    print(ite.validate("1"))
    print(ite.validate("0"))
    print(ite.validate("0.5"))

# Generated at 2022-06-14 14:14:08.486954
# Unit test for constructor of class OneOf
def test_OneOf():
    # Test if the constructor is not None
    assert OneOf is not None

# Generated at 2022-06-14 14:14:10.240287
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    never_match = NeverMatch(key="never")
    assert never_match.key == "never"


# Generated at 2022-06-14 14:14:20.262185
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    # No match
    oneOf1 = OneOf([])
    try:
        oneOf1.validate({})
        assert False, "OneOf validation error not raised"
    except:
        assert True
    # Multiple matches
    oneOf2 = OneOf([Any(), Any()])
    try:
        oneOf2.validate({})
        assert False, "OneOf validation error not raised"
    except:
        assert True
    # Single match
    oneOf3 = OneOf([Any()])
    assert oneOf3.validate({}) == {}


# Generated at 2022-06-14 14:14:23.081009
# Unit test for method validate of class Not
def test_Not_validate():
    notField = Not(Field())
    try:
        notField.validate(None)
    except ValueError:
        assert True
    else:
        assert False


# Generated at 2022-06-14 14:14:28.079853
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    #Create 2 fields to use in IfThenElse:
    field1 = IntegerField()
    field2 = NumberField()
    #Create a IfThenElse object
    IfElse = IfThenElse(if_clause = field1, then_clause = field2 , else_clause = field1)
    # assert that it works:
    value = 'a'
    IfElse.validate(value)

# Generated at 2022-06-14 14:14:35.152013
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    try:
        IfThenElse(Integer(max_value=2), String()).validate(2)
    except Exception as e:
        assert str(e) == 'Must be a string.'
    try:
        IfThenElse(Integer(max_value=2), String()).validate(3)
    except Exception as e:
        assert str(e) == 'Must be a string.'
    assert IfThenElse(Integer(max_value=2), String()).validate('Hello') == 'Hello'
    assert IfThenElse(Integer(max_value=2), String()).validate(1) == 1

# Generated at 2022-06-14 14:14:42.477491
# Unit test for method validate of class OneOf
def test_OneOf_validate():
    from typesystem import Schema, String

    class TestAllOf(Schema):
        types = OneOf([String(), String()])
        types1 = OneOf([String(), String()])
        types2 = OneOf([String(), String()])
        types3 = OneOf([String(), String()])
        types4 = OneOf([String(), String()])
        types5 = OneOf([String(), String()])


# Generated at 2022-06-14 14:14:42.917459
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    assert NeverMatch()

# Generated at 2022-06-14 14:14:46.538665
# Unit test for constructor of class AllOf
def test_AllOf():
    string_field = String()
    number_field = Number()
    all_of_field = AllOf([string_field, number_field])
    assert all_of_field.all_of == [string_field, number_field]



# Generated at 2022-06-14 14:14:52.108210
# Unit test for constructor of class OneOf
def test_OneOf():
    one_of_instance = OneOf([])
    assert isinstance(one_of_instance, OneOf)


# Generated at 2022-06-14 14:14:55.288968
# Unit test for constructor of class AllOf
def test_AllOf():
    msg = "All of the fields must be JSON-schema compatible."
    schema = AllOf([1,2,3])
    assert schema.all_of == [1,2,3]


# Generated at 2022-06-14 14:14:57.233332
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    assert IfThenElse.validate('val','val','val','val','val') == 1

# Generated at 2022-06-14 14:15:08.730285
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    field = IfThenElse(
        if_clause = Boolean(),
        then_clause = AllOf(
            [
                Integer(),
                Not(OneOf([
                    Boolean(),
                    Integer()
                ]))
            ]
        ),
        else_clause = AllOf(
            [
                Boolean(),
                Not(OneOf([
                    Boolean(),
                    Integer()
                ]))
            ]
        )
    )
    value = True
    validated_value = field.validate(value)
    assert validated_value == value
    value = False
    validated_value = field.validate(value)
    assert validated_value == value
    value = 1
    validated_value = field.validate(value)
    assert validated_value == value
    value = "not valid"

# Generated at 2022-06-14 14:15:13.023899
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    x = 1
    def f(x):
        if x==1:
            return False
        else:
            return True
    def g(x):
        if x==1:
            return True
        else:
            return False
    IfThenElse(f,g,x)

# Generated at 2022-06-14 14:15:17.626244
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    field = IfThenElse(if_clause=Any(), then_clause=None, else_clause=None)
    assert field.if_clause == Any()
    assert field.then_clause == Any()
    assert field.else_clause == Any()

# Generated at 2022-06-14 14:15:28.526913
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    class MyField1(Field):
        def validate(self, value, strict=False):
            if value == 1:
                raise self.validation_error("error_in_if")
            return value

    class MyField2(Field):
        def validate(self, value, strict=False):
            if value == 2:
                raise self.validation_error("error_in_then")
            return value

    class MyField3(Field):
        def validate(self, value, strict=False):
            if value == 3:
                raise self.validation_error("error_in_else")
            return value

    my_field1 = MyField1()
    my_field2 = MyField2()
    my_field3 = MyField3()


# Generated at 2022-06-14 14:15:30.022660
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    try:
        NeverMatch(allow_null=True)
    except AssertionError:
        pass


# Generated at 2022-06-14 14:15:31.390452
# Unit test for method validate of class Not
def test_Not_validate():
    field = Not(Field(label='Field'))
    field.validate('string')

# Generated at 2022-06-14 14:15:32.319768
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    # Add test here
    assert True

# Generated at 2022-06-14 14:15:40.428293
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    ifThenElse = IfThenElse(Any(name="if_clause"), Any(name="then_clause"))
    assert ifThenElse.validate(1) == 1


# Generated at 2022-06-14 14:15:43.402403
# Unit test for method validate of class Not
def test_Not_validate():
	not_test = Not(Any())
	not_test.errors = {"negated" : "test"}
	if not_test.validate(1) == 1 and not_test.validate(False) == False and len(not_test.errors) == 1:
		return
	assert False


# Generated at 2022-06-14 14:15:47.868786
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    validate_method = IfThenElse.validate
    value = "Hello world!"
    strict = False
    assert validate_method(value, strict) == value
    value = 25
    assert validate_method(value, strict) == value

# Generated at 2022-06-14 14:15:53.562257
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    # Test a IfThenElse with True in IF clause
    ite = IfThenElse(String(max_length=2), String())
    assert ite.validate("A") == "A"

    # Test a IfThenElse with False in IF clause
    ite = IfThenElse(String(max_length=1), String())
    assert ite.validate("A") == "A"


# Generated at 2022-06-14 14:15:56.666783
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    # Test that the function validate returns the correct value
    ifThenElse = IfThenElse(Any(), Any(), Any())
    assert ifThenElse.validate(1) == True
    assert ifThenElse.validate(0) == False

# Generated at 2022-06-14 14:15:58.092028
# Unit test for method validate of class Not
def test_Not_validate():
    fields = [Not(String())]
    is_valid(fields, "hello")


# Generated at 2022-06-14 14:16:03.705164
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    assert IfThenElse(
        if_clause=OneOf(one_of=[Any()]),
        then_clause=OneOf(one_of=[Any()]),
        else_clause=OneOf(one_of=[Any()]),
    ).validate(1) == 1



# Generated at 2022-06-14 14:16:12.562546
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():
    cls = IfThenElse
    # test cases:
    # if_clause = None -> error
    # then_clause = None -> error
    # else_clause = None -> error
    # value = None -> error
    # value = "hello" -> "hello"
    # value = 23 -> 23
    # value = "None" -> "None"
    if_clause = None
    then_clause = None
    else_clause = None
    value = None
    obj = cls(if_clause, then_clause, else_clause)
    try:
        res = obj.validate(value)
    except AssertionError as e:
        print("AssertionError:", e)
    else:
        print("No error")


# test for method __init__ of class IfThenElse

# Generated at 2022-06-14 14:16:16.197185
# Unit test for constructor of class AllOf
def test_AllOf():
    class A(AllOf):
        def __init__(self):
            AllOf.__init__(self, all_of=[1,2,3,4])
    assert A().all_of == [1,2,3,4]

# Generated at 2022-06-14 14:16:23.119485
# Unit test for constructor of class IfThenElse
def test_IfThenElse():
    field_1 = IfThenElse(
        if_clause = Any(),
        then_clause = Any(),
        else_clause = Any()
    )
    assert field_1.if_clause == Any()
    assert field_1.then_clause == Any()
    assert field_1.else_clause == Any()

    field_2 = IfThenElse(
        if_clause = Any(),
        then_clause = Any()
    )
    assert field_2.if_clause == Any()
    assert field_2.then_clause == Any()
    assert field_2.else_clause == Any()

# Generated at 2022-06-14 14:16:29.364837
# Unit test for constructor of class OneOf
def test_OneOf():
    a = OneOf(one_of=[])
    print(a)


# Generated at 2022-06-14 14:16:30.382091
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    x = NeverMatch()



# Generated at 2022-06-14 14:16:35.553083
# Unit test for method validate of class Not
def test_Not_validate():
    field = Not(Int())
    field.validate(4)
    try:
        field.validate(4.2)
    except Exception as exc:
        isinstance(exc, ValidationError)
        str(exc) == 'Must not match.'
        exc.error_code == 'negated'
    try:
        field.validate(None)
    except Exception as exc:
        isinstance(exc, ValidationError)
        str(exc) == 'Must not match.'
        exc.error_code == 'negated'


# Generated at 2022-06-14 14:16:38.650386
# Unit test for constructor of class OneOf
def test_OneOf():
    field1 = NeverMatch()
    field2 = NeverMatch()
    field3 = NeverMatch()
    oneOf = OneOf([field1, field2, field3])


# Generated at 2022-06-14 14:16:48.315051
# Unit test for method validate of class Not
def test_Not_validate():
    field = Not(negated=Any())
    assert field.validate(value=None) == None
    assert field.validate(value=1) == 1
    assert field.validate(value=1.1) == 1.1
    assert field.validate(value="foo") == "foo"
    assert field.validate(value=[1, 2]) == [1, 2]
    assert field.validate(value={"a": 1, "b": 2}) == {"a": 1, "b": 2}
    with pytest.raises(ValidationError, match="Must not match."):
        field.validate(value=True)


# Generated at 2022-06-14 14:16:49.357053
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    field=NeverMatch()
    assert field!=None

# Generated at 2022-06-14 14:16:54.301273
# Unit test for method validate of class Not
def test_Not_validate():
    not_field = Not(Number())
    assert not_field.validate(5.5) == 5.5
    assert not_field.validate('5.5') == '5.5'
    assert not_field.validate('5') == '5'
    assert not_field.validate(5) == 5
    assert not_field.validate(5.5) == 5.5

# Generated at 2022-06-14 14:17:06.369268
# Unit test for method validate of class Not
def test_Not_validate():
    class input:
        foo = "bar"
        validates = True
    inputNotValid = input 
    inputNotValid.foo = "bar2"
    inputNotValid.validates = False
    class output:
        foo = "bar"
        validates = True
    outputNotValid = output 
    outputNotValid.foo = "bar2"
    outputNotValid.validates = False
    class Not:
        def __init__(self, negated):
            self.negated = negated
        errors = {"negated": "Must not match."}
        def validate(self, value, strict=False):
            _, error = self.negated.validate_or_error(value, strict=strict)
            if error:
                return value
            raise self.validation_error("negated")

# Generated at 2022-06-14 14:17:09.386595
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    nevermatch = NeverMatch()
    with pytest.raises(AssertionError):
        nevermatch = NeverMatch(allow_null=True)


# Generated at 2022-06-14 14:17:15.026333
# Unit test for constructor of class AllOf
def test_AllOf():
    class MyClass:
        def __init__(self, all_of: typing.List[Field], **kwargs: typing.Any) -> None:
            assert "allow_null" not in kwargs
            self.all_of = all_of
    list2 = [1,2]
    list1 = [1]
    assert MyClass(list2).all_of == list2


# Generated at 2022-06-14 14:17:22.451407
# Unit test for constructor of class AllOf
def test_AllOf():
    assert AllOf(all_of=[]) is not None

# Generated at 2022-06-14 14:17:24.126559
# Unit test for constructor of class OneOf
def test_OneOf():
    assert issubclass(OneOf, Field)
OneOf()

# Generated at 2022-06-14 14:17:24.721054
# Unit test for constructor of class OneOf
def test_OneOf():
    assert OneOf({})

# Generated at 2022-06-14 14:17:27.665852
# Unit test for constructor of class AllOf
def test_AllOf():
    try:
        from typesystem.fields import Array, Integer
        assert AllOf(all_of = [Array(items=Integer)])
    except:
        assert False


# Generated at 2022-06-14 14:17:30.630866
# Unit test for method validate of class Not
def test_Not_validate():
    # declare instance of class Not
    test = Not(Any())

    # validate a list
    value = [1, 2]
    result = test.validate(value)
    assert result == value

# Generated at 2022-06-14 14:17:32.650110
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    nm = NeverMatch()
    assert nm



# Generated at 2022-06-14 14:17:34.489824
# Unit test for method validate of class Not
def test_Not_validate():
    field = Not(negated = String())
    value = "testing-value"
    field.validate(value)

# Generated at 2022-06-14 14:17:41.351481
# Unit test for method validate of class Not
def test_Not_validate():
    error_message = "Must not match."
    field = Not(Any(), error_messages={"negated": error_message})
    assert field.validate(1) == 1
    with pytest.raises(ValidationError) as excinfo:
        field.validate(None)
    assert excinfo.value.code == "negated"
    assert str(excinfo.value) == error_message


# Generated at 2022-06-14 14:17:44.885404
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    test = NeverMatch()
    assert test.errors == {"never": "This never validates."}

# Generated at 2022-06-14 14:17:49.304608
# Unit test for constructor of class OneOf
def test_OneOf():
    int_field = typing.cast(typing.Any, Field)()
    string_field = Field(str)
    u = typing.cast(typing.Any, OneOf)([int_field, string_field])
    assert u.one_of == [int_field, string_field]

# Generated at 2022-06-14 14:18:04.189291
# Unit test for method validate of class Not
def test_Not_validate():
    print("Testing validate of Not")
    neg_field = Not(negated=Any())
    assert(neg_field.validate(1)==1)

# Generated at 2022-06-14 14:18:05.295746
# Unit test for constructor of class AllOf
def test_AllOf():
    test = AllOf(all_of=[])
    assert test.all_of == []



# Generated at 2022-06-14 14:18:06.786332
# Unit test for method validate of class Not
def test_Not_validate():
    field = Not(NeverMatch())
    assert field.validate("a") == "a"

# Generated at 2022-06-14 14:18:13.371242
# Unit test for method validate of class Not
def test_Not_validate():
  test_cases=[]
  test_cases.append(
    [
      "Negative: Field negative",
      # Input
      {
        "negated": "10"
      },
      # Output
      {
        "negated_error": "This field must be a number."
      }
    ]
  )
  test_cases.append(
    [
      "Positive",
      # Input
      {
        "negated": 20
      },
      # Output
      {
        "negated": 20
      }
    ]
  )
  for test_case in test_cases:
    print("---")
    print("Description: " + str(test_case[0]))
    print("Input: " + str(test_case[1]))

# Generated at 2022-06-14 14:18:16.698268
# Unit test for constructor of class OneOf
def test_OneOf():
    with raises(AssertionError):
        oof = OneOf(one_of=[1,3,4], allow_null=True)


# Generated at 2022-06-14 14:18:19.078298
# Unit test for constructor of class AllOf
def test_AllOf():
    a = AllOf([1,2,3], name="type")
    assert a.all_of == [1,2,3]


# Generated at 2022-06-14 14:18:24.504076
# Unit test for constructor of class AllOf
def test_AllOf():
    """
    Ensure AllOf.__init__() is working.
    """
    from typesystem.fields import Number

    field_allOf = AllOf([Number()])
    assert isinstance(field_allOf, Field)
    assert field_allOf.all_of == [Number()]
    assert field_allOf.__class__.__name__ == "AllOf"



# Generated at 2022-06-14 14:18:26.654143
# Unit test for constructor of class AllOf
def test_AllOf():
    t = AllOf([], description="Test")
    assert t.all_of == []



# Generated at 2022-06-14 14:18:31.112390
# Unit test for method validate of class Not
def test_Not_validate():
    from typesystem.types import String
    
    someStr = "SomeString"
    myString = String(max_length=4)

    myNot = Not(myString)
    print(myNot)

    valid, error = myNot.validate_or_error(someStr)
    print(valid)
    print(error)

if __name__ == '__main__':
    test_Not_validate()

# Generated at 2022-06-14 14:18:32.803051
# Unit test for method validate of class Not
def test_Not_validate():
    field = Not(Field())
    field.validate("value")

# Generated at 2022-06-14 14:18:53.865112
# Unit test for constructor of class OneOf
def test_OneOf():
    from typesystem.types import String
    class MyOneOf(OneOf):
        def __init__(self, one_of: typing.List[Field], **kwargs: typing.Any) -> None:
            super().__init__(one_of, **kwargs)
    field = MyOneOf([String(), String()], name="name")
    assert field.name == "name"
    assert field.validate(1) == "1"
    assert field.deserialize(1) == "1"
    assert field.validate("") == ""
    assert field.deserialize("") == ""

# Generated at 2022-06-14 14:18:55.605895
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    try:
        NeverMatch()
    except AssertionError as e:
        print(e)


# Generated at 2022-06-14 14:18:59.396582
# Unit test for constructor of class AllOf
def test_AllOf():
    f1 = Field(name="test_field")
    f2 = Field(name="test_field")
    f3 = Field(name="test_field")
    test_field = AllOf([f1,f2,f3])
    assert test_field.all_of == [f1, f2, f3]


# Generated at 2022-06-14 14:19:02.354782
# Unit test for constructor of class OneOf
def test_OneOf():
  o = OneOf(one_of=[Boolean()])
  assert o

# Generated at 2022-06-14 14:19:04.766202
# Unit test for constructor of class AllOf
def test_AllOf():
    a = AllOf([])
    b = AllOf()
    c = AllOf([], meta = None)
    d = AllOf(meta = None)

# Generated at 2022-06-14 14:19:09.763569
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    name = 'test_NeverMatch'
    field = NeverMatch(name=name)
    assert field.name == name
    assert field.description == ''
    assert field.default is None
    assert field.required == None
    assert field.allow_null == False
    assert field.errors == {'never': 'This never validates.'}


# Generated at 2022-06-14 14:19:20.681924
# Unit test for constructor of class OneOf
def test_OneOf():
    from typesystem.fields import String
    oneOf = OneOf([String(max_length=5), String(min_length=3)])

    assert oneOf.validate("hello") == "hello"
    assert oneOf.validate("abc") == "abc"

    from typesystem.exceptions import ValidationError

    try:
        oneOf.validate("hello world")
    except ValidationError as exc:
        assert exc.errors() == [
            {
                "loc": [],
                "msg": "Did not match any valid type.",
                "type": "no_match",
            }
        ]


# Generated at 2022-06-14 14:19:21.678896
# Unit test for constructor of class OneOf
def test_OneOf():
    field = OneOf(one_of=[Field(), Field()])
    assert field is not None

# Generated at 2022-06-14 14:19:24.845131
# Unit test for constructor of class OneOf
def test_OneOf():
    f1 = Field(name="f1")
    f2 = Field(name="f2")
    assert OneOf(one_of=[f1, f2])

# Generated at 2022-06-14 14:19:25.862445
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    nm = NeverMatch()
    assert nm

# Generated at 2022-06-14 14:19:50.618555
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    a = NeverMatch()
    a.validate('Hello')


# Generated at 2022-06-14 14:19:52.631415
# Unit test for constructor of class OneOf
def test_OneOf():
    obj = OneOf(['field1', 'field2'])

# Generated at 2022-06-14 14:19:55.291923
# Unit test for constructor of class OneOf
def test_OneOf():
    assert isinstance(
        OneOf([Field(), Field(required=True)]),
        OneOf,
    )


# Generated at 2022-06-14 14:19:57.474406
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    field = NeverMatch()
    assert field.error == "This never validates."



# Generated at 2022-06-14 14:19:58.427928
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    pass #TODO


# Generated at 2022-06-14 14:20:00.273014
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    test = NeverMatch()
    assert test.errors == {"never": "This never validates."}


# Generated at 2022-06-14 14:20:01.631876
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    nm = NeverMatch()
    assert nm.label == 'NeverMatch'


# Generated at 2022-06-14 14:20:02.892386
# Unit test for constructor of class OneOf
def test_OneOf():
    assert OneOf



# Generated at 2022-06-14 14:20:11.792038
# Unit test for constructor of class NeverMatch
def test_NeverMatch():
    # Initialization
    nm = NeverMatch()
    assert nm

    # Type check
    assert isinstance(nm, NeverMatch)
    assert isinstance(nm, Field)

    # Field's attributes
    assert nm.name == 'nevermatch'
    assert nm.parent == None
    assert nm.errors == {'never': 'This never validates.'}

    # Field's functions
    assert nm.validate(1)
    assert nm.validate_or_error(1) == [None, {'never': 'This never validates.'}]
    assert Field.expect(nm, 1)
    assert nm.serialize() == {'type': 'nevermatch', 'errors': {'never': 'This never validates.'}}



# Generated at 2022-06-14 14:20:15.498536
# Unit test for constructor of class AllOf
def test_AllOf():
    field = AllOf([])
    assert field.errors == {}
    assert field.required is False
    assert field.description == ""
    assert field.example is None
    assert field.name is None
