

# Generated at 2024-03-18 08:41:48.094416
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():    # Setup fields for the test
    if_clause = NeverMatch()
    then_clause = Field()
    else_clause = Field()

    # Create an instance of IfThenElse with the setup fields
    conditional_field = IfThenElse(if_clause=if_clause, then_clause=then_clause, else_clause=else_clause)

    # Test the 'else' branch by passing a value that will not satisfy the 'if_clause'
    value = "test_value"
    result = conditional_field.validate(value)
    assert result == value, "The 'else' clause did not return the original value when 'if_clause' is not satisfied."

    # Now, let's test the 'then' branch by making sure the 'if_clause' is satisfied
    # For this, we need to replace the 'if_clause' with a Field that always validates
    conditional_field.if_clause = Field()

    # Test the 'then' branch by passing a value that will satisfy the

# Generated at 2024-03-18 08:41:55.565627
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():    # Setup fields for the test
    if_clause = Any()
    then_clause = Any()
    else_clause = NeverMatch()

    # Create an instance of IfThenElse with the setup fields
    conditional_field = IfThenElse(if_clause=if_clause, then_clause=then_clause, else_clause=else_clause)

    # Test the 'then' branch
    value = "test value"
    assert conditional_field.validate(value) == value, "The 'then' clause did not validate as expected."

    # Test the 'else' branch
    conditional_field.if_clause = NeverMatch()  # Change the if_clause to always fail
    try:
        conditional_field.validate(value)
        assert False, "The 'else' clause should have raised a validation error."
    except conditional_field.validation_error as exc:
        assert exc.code == "never", "The 'else' clause did not raise the expected validation error."


# Generated at 2024-03-18 08:42:05.814893
# Unit test for constructor of class AllOf
def test_AllOf():    # Test that the constructor correctly assigns the `all_of` parameter
    field1 = Field()
    field2 = Field()
    all_of_field = AllOf([field1, field2])
    assert all_of_field.all_of == [field1, field2], "Constructor must assign the `all_of` parameter"

    # Test that the constructor raises an AssertionError if `allow_null` is passed in kwargs
    try:
        AllOf([field1, field2], allow_null=True)
        assert False, "Constructor should not accept `allow_null` in kwargs"
    except AssertionError:
        assert True

    # Test that the constructor does not raise an error for additional kwargs
    try:
        AllOf([field1, field2], example_kwarg="example")
        assert True, "Constructor should accept additional kwargs"
    except Exception as e:
        assert False, f"Constructor should not raise an error for additional kwargs: {e}"


# Generated at 2024-03-18 08:42:09.484326
# Unit test for constructor of class NeverMatch
def test_NeverMatch():    # Test that the constructor raises an AssertionError if 'allow_null' is in kwargs
    try:
        field = NeverMatch(allow_null=True)
        assert False, "AssertionError not raised"
    except AssertionError:
        pass

    # Test that the constructor does not raise an error if 'allow_null' is not in kwargs
    try:
        field = NeverMatch()
    except AssertionError:
        assert False, "AssertionError raised unexpectedly"


# Generated at 2024-03-18 08:42:19.559936
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():    # Setup fields for the test
    if_clause = NeverMatch()
    then_clause = Field()
    else_clause = Field()

    # Create an instance of IfThenElse with the setup fields
    conditional_field = IfThenElse(if_clause=if_clause, then_clause=then_clause, else_clause=else_clause)

    # Test the 'if' clause failing and 'else' clause succeeding
    value = "test_value"
    result = conditional_field.validate(value)
    assert result == value, "The 'else' clause should validate when the 'if' clause fails."

    # Test the 'if' clause succeeding and 'then' clause succeeding
    if_clause = Field()
    conditional_field = IfThenElse(if_clause=if_clause, then_clause=then_clause)
    result = conditional_field.validate(value)
    assert result == value, "The 'then' clause should validate when the 'if' clause succeeds."

    # Test the 'if'

# Generated at 2024-03-18 08:42:20.120258
# Unit test for constructor of class Not

# Generated at 2024-03-18 08:42:24.486455
# Unit test for constructor of class Not
def test_Not():    # Test that the constructor correctly initializes the 'negated' field
    field = Any()
    not_field = Not(negated=field)
    assert not_field.negated == field, "Constructor must initialize 'negated' field"

    # Test that the constructor raises an AssertionError if 'allow_null' is in kwargs
    try:
        Not(negated=field, allow_null=True)
        assert False, "Constructor should not accept 'allow_null' kwarg"
    except AssertionError:
        assert True


# Generated at 2024-03-18 08:42:30.065484
# Unit test for constructor of class Not
def test_Not():    # Test that the constructor correctly initializes the `negated` field
    negated_field = Any()
    not_field = Not(negated=negated_field)
    assert not_field.negated == negated_field, "Constructor failed to initialize `negated` field"

    # Test that the constructor raises an AssertionError if `allow_null` is passed in kwargs
    try:
        Not(negated=negated_field, allow_null=True)
        assert False, "Constructor should not accept `allow_null` kwarg"
    except AssertionError:
        assert True


# Generated at 2024-03-18 08:42:34.382765
# Unit test for constructor of class OneOf
def test_OneOf():    # Test that the constructor correctly assigns the 'one_of' attribute
    field1 = Any()
    field2 = Any()
    one_of_field = OneOf([field1, field2])
    assert one_of_field.one_of == [field1, field2], "Constructor failed to assign 'one_of' attribute"

    # Test that the constructor raises an AssertionError if 'allow_null' is in kwargs
    try:
        OneOf([field1, field2], allow_null=True)
        assert False, "Constructor should not accept 'allow_null' kwarg"
    except AssertionError:
        assert True


# Generated at 2024-03-18 08:42:42.193616
# Unit test for method validate of class Not
def test_Not_validate():    # Create a field that always fails validation
    always_fail = NeverMatch()

    # Create a Not field with the always_fail field
    not_field = Not(always_fail)

    # Test that the Not field validates correctly
    assert not_field.validate("any value") == "any value", "Should validate since the inner field always fails"

    # Create a field that always passes validation
    always_pass = Field()

    # Create a Not field with the always_pass field
    not_field_with_pass = Not(always_pass)

    # Test that the Not field raises a validation error
    try:
        not_field_with_pass.validate("any value")
        assert False, "Should raise a validation error since the inner field always passes"
    except not_field_with_pass.validation_error as exc:
        assert exc.code == "negated", "Should raise a 'negated' validation error"


# Generated at 2024-03-18 08:42:52.608852
# Unit test for method validate of class Not
def test_Not_validate():    # Create a field that always validates
    always_valid_field = Any()

    # Create a field that never validates
    never_valid_field = NeverMatch()

    # Test that Not with a field that always validates raises a validation error
    not_always_valid = Not(always_valid_field)
    try:
        not_always_valid.validate("any value")
        assert False, "Should have raised a validation error"
    except not_always_valid.validation_error as exc:
        assert exc.code == "negated", "Error code should be 'negated'"

    # Test that Not with a field that never validates passes
    not_never_valid = Not(never_valid_field)
    try:
        result = not_never_valid.validate("any value")
        assert result == "any value", "Should have returned the input value"
    except not_never_valid.validation_error:
        assert False, "Should not have raised a validation error"


# Generated at 2024-03-18 08:42:59.256277
# Unit test for method validate of class OneOf
def test_OneOf_validate():    # Create instances of Field that will be used for testing
    always_valid = Any()
    never_valid = NeverMatch()
    integer_field = Field(types=int)

    # Test case where no sub-item matches
    one_of_no_match = OneOf([never_valid, never_valid])
    try:
        one_of_no_match.validate("test")
        assert False, "Should have raised a validation error for no matches."
    except one_of_no_match.validation_error as exc:
        assert exc.code == "no_match", "Error code should be 'no_match'."

    # Test case where exactly one sub-item matches
    one_of_single_match = OneOf([never_valid, always_valid])
    assert one_of_single_match.validate("test") == "test", "Should have validated as it matches the 'always_valid' field."

    # Test case where more than one sub-item matches
    one_of_multiple_matches = OneOf([always_valid, integer_field])


# Generated at 2024-03-18 08:43:08.953120
# Unit test for method validate of class OneOf
def test_OneOf_validate():    string_field = typesystem.fields.String()

# Generated at 2024-03-18 08:43:09.961960
# Unit test for constructor of class Not

# Generated at 2024-03-18 08:43:23.946020
# Unit test for constructor of class OneOf
def test_OneOf():    # Test that the constructor correctly assigns the `one_of` parameter
    field1 = Field()
    field2 = Field()
    one_of_field = OneOf(one_of=[field1, field2])
    assert one_of_field.one_of == [field1, field2], "Constructor must assign `one_of` parameter"

    # Test that the constructor raises an AssertionError if `allow_null` is passed in kwargs
    try:
        OneOf(one_of=[field1, field2], allow_null=True)
        assert False, "Constructor should not accept `allow_null` in kwargs"
    except AssertionError:
        assert True

    # Test that the constructor does not raise an error for other kwargs
    try:
        OneOf(one_of=[field1, field2], example="example")
        assert True
    except AssertionError:
        assert False, "Constructor should accept other kwargs"


# Generated at 2024-03-18 08:43:32.320587
# Unit test for method validate of class OneOf
def test_OneOf_validate():    # Create instances of Field that will be used for testing
    always_valid = Any()
    never_valid = NeverMatch()

    # Create a OneOf instance with fields that will always and never validate
    one_of_field = OneOf([always_valid, never_valid])

    # Test case where the value should validate against exactly one field
    assert one_of_field.validate("test value") == "test value", "Should match the always valid field"

    # Test case where the value should not validate against any field
    try:
        one_of_field.validate(None)
    except one_of_field.validation_error as exc:
        assert exc.code == "no_match", "Should not match any field"

    # Create a OneOf instance with fields that will always validate
    one_of_always_valid = OneOf([always_valid, Any()])

    # Test case where the value should validate against multiple fields

# Generated at 2024-03-18 08:43:32.873727
# Unit test for constructor of class AllOf

# Generated at 2024-03-18 08:43:54.224409
# Unit test for method validate of class Not
def test_Not_validate():    # Create a field that always fails validation
    always_fail = NeverMatch()

    # Create a Not field with the always_fail field as the negated field
    not_field = Not(always_fail)

    # Test that the Not field validates successfully since the negated field fails
    assert not_field.validate("any value") == "any value", "Should validate since the negated field always fails"

    # Create a field that always passes validation
    always_pass = Field()

    # Create a Not field with the always_pass field as the negated field
    not_field_with_pass = Not(always_pass)

    # Test that the Not field raises a validation error since the negated field passes

# Generated at 2024-03-18 08:43:59.472543
# Unit test for constructor of class IfThenElse
def test_IfThenElse():    if_clause = NeverMatch()

# Generated at 2024-03-18 08:44:04.836051
# Unit test for constructor of class Not
def test_Not():    # Test that the constructor correctly initializes the 'negated' field
    field = Field()
    not_field = Not(negated=field)
    assert not_field.negated == field, "Constructor must initialize 'negated' field"

    # Test that the constructor raises an AssertionError if 'allow_null' is in kwargs
    try:
        Not(negated=field, allow_null=True)
        assert False, "Constructor should not accept 'allow_null' kwarg"
    except AssertionError:
        pass


# Generated at 2024-03-18 08:44:10.108227
# Unit test for constructor of class Not

# Generated at 2024-03-18 08:44:14.218236
# Unit test for constructor of class AllOf
def test_AllOf():    # Test that the constructor correctly assigns the `all_of` parameter
    field1 = Field()
    field2 = Field()
    all_of_field = AllOf([field1, field2])
    assert all_of_field.all_of == [field1, field2], "Constructor must assign the `all_of` parameter"

    # Test that the constructor raises an AssertionError if `allow_null` is passed in kwargs
    try:
        AllOf([field1, field2], allow_null=True)
        assert False, "Constructor should not accept `allow_null` as a kwarg"
    except AssertionError:
        pass


# Generated at 2024-03-18 08:44:24.393121
# Unit test for constructor of class IfThenElse
def test_IfThenElse():    if_clause = NeverMatch()

# Generated at 2024-03-18 08:44:26.824202
# Unit test for constructor of class Not
def test_Not():    # Test that the constructor correctly initializes the `negated` field
    field = Any()
    not_field = Not(negated=field)
    assert not_field.negated == field, "The `negated` field should be initialized with the provided field"


# Generated at 2024-03-18 08:44:32.593169
# Unit test for constructor of class NeverMatch
def test_NeverMatch():    # Test that the constructor raises an AssertionError if 'allow_null' is in kwargs
    try:
        field = NeverMatch(allow_null=True)
        assert False, "AssertionError not raised"
    except AssertionError:
        pass

    # Test that the constructor does not raise an error when 'allow_null' is not in kwargs
    try:
        field = NeverMatch()
        assert True
    except AssertionError:
        assert False, "AssertionError raised unexpectedly"


# Generated at 2024-03-18 08:44:37.263149
# Unit test for constructor of class AllOf
def test_AllOf():    # Test that the constructor correctly assigns the `all_of` parameter
    field1 = Field()
    field2 = Field()
    all_of_field = AllOf([field1, field2])
    assert all_of_field.all_of == [field1, field2], "Constructor must assign the `all_of` parameter"

    # Test that the constructor raises an AssertionError if `allow_null` is in kwargs
    try:
        AllOf([field1, field2], allow_null=True)
        assert False, "Constructor should not accept `allow_null` in kwargs"
    except AssertionError:
        assert True


# Generated at 2024-03-18 08:44:45.042176
# Unit test for constructor of class OneOf
def test_OneOf():    # Test that the constructor correctly assigns the 'one_of' parameter
    field1 = Any()
    field2 = NeverMatch()
    one_of_field = OneOf([field1, field2])
    assert one_of_field.one_of == [field1, field2], "Constructor did not assign 'one_of' correctly"

    # Test that the constructor raises an AssertionError if 'allow_null' is passed in kwargs
    try:
        OneOf([field1, field2], allow_null=True)
        assert False, "Constructor should not accept 'allow_null' as a kwarg"
    except AssertionError:
        assert True, "Constructor correctly raised an AssertionError for 'allow_null' kwarg"


# Generated at 2024-03-18 08:44:50.835990
# Unit test for constructor of class Not
def test_Not():    # Test that the constructor correctly initializes the `negated` field
    field = Any()
    not_field = Not(negated=field)
    assert not_field.negated == field, "The `negated` field should be initialized with the passed argument."

    # Test that the constructor raises an AssertionError if 'allow_null' is in kwargs
    try:
        Not(negated=field, allow_null=True)
        assert False, "AssertionError should be raised when 'allow_null' is in kwargs"
    except AssertionError:
        pass


# Generated at 2024-03-18 08:44:59.179424
# Unit test for constructor of class AllOf
def test_AllOf():    # Test that the constructor correctly initializes the `all_of` attribute
    field1 = Field()
    field2 = Field()
    all_of_field = AllOf([field1, field2])
    assert all_of_field.all_of == [field1, field2], "Constructor must initialize the `all_of` attribute with the provided fields"

    # Test that the constructor raises an AssertionError if `allow_null` is passed in kwargs
    try:
        AllOf([field1, field2], allow_null=True)
        assert False, "Constructor should not accept `allow_null` as a kwarg"
    except AssertionError:
        assert True

    # Test that the constructor does not raise an error for other kwargs
    try:
        AllOf([field1, field2], example="example")
        assert True, "Constructor should accept other kwargs"
    except Exception as e:
        assert False, f"Constructor raised an unexpected exception: {e}"


# Generated at 2024-03-18 08:45:07.778298
# Unit test for constructor of class AllOf
def test_AllOf():    # Test that the constructor correctly assigns the `all_of` parameter
    field1 = Field()
    field2 = Field()
    all_of_field = AllOf([field1, field2])
    assert all_of_field.all_of == [field1, field2], "Constructor must assign the `all_of` parameter"

    # Test that the constructor raises an AssertionError if `allow_null` is in kwargs
    try:
        AllOf([field1, field2], allow_null=True)
        assert False, "Constructor should not accept `allow_null` in kwargs"
    except AssertionError:
        pass


# Generated at 2024-03-18 08:45:19.884429
# Unit test for constructor of class IfThenElse
def test_IfThenElse():    if_clause = NeverMatch()

# Generated at 2024-03-18 08:45:22.685461
# Unit test for constructor of class Not
def test_Not():    # Test that the constructor correctly initializes the 'negated' field
    field = Any()
    not_field = Not(negated=field)
    assert not_field.negated == field, "The 'negated' field should be initialized with the provided field"


# Generated at 2024-03-18 08:45:31.720837
# Unit test for constructor of class IfThenElse
def test_IfThenElse():    if_clause = NeverMatch()

# Generated at 2024-03-18 08:45:38.835984
# Unit test for constructor of class OneOf
def test_OneOf():    # Test that the constructor correctly assigns the 'one_of' parameter
    field1 = Any()
    field2 = Any()
    one_of_field = OneOf([field1, field2])
    assert one_of_field.one_of == [field1, field2], "Constructor failed to assign 'one_of' parameter correctly"

    # Test that the constructor raises an AssertionError if 'allow_null' is passed in kwargs
    try:
        OneOf([field1, field2], allow_null=True)
        assert False, "Constructor should not accept 'allow_null' as a kwarg"
    except AssertionError:
        assert True, "Constructor correctly raised an AssertionError for 'allow_null' kwarg"


# Generated at 2024-03-18 08:45:39.391571
# Unit test for constructor of class Not

# Generated at 2024-03-18 08:45:46.746212
# Unit test for constructor of class OneOf
def test_OneOf():    # Test that the constructor correctly assigns the `one_of` parameter
    field1 = Field()
    field2 = Field()
    one_of_field = OneOf(one_of=[field1, field2])
    assert one_of_field.one_of == [field1, field2], "Constructor must assign `one_of` parameter"

    # Test that the constructor raises an AssertionError if `allow_null` is passed in kwargs
    try:
        OneOf(one_of=[field1, field2], allow_null=True)
        assert False, "Constructor should not accept `allow_null` in kwargs"
    except AssertionError:
        assert True

    # Test that the constructor does not raise an error for other kwargs

# Generated at 2024-03-18 08:45:48.919707
# Unit test for constructor of class Not
def test_Not():    negated_field = Any()

# Generated at 2024-03-18 08:45:52.707578
# Unit test for constructor of class Not
def test_Not():    # Test that the constructor correctly initializes the 'negated' field
    negated_field = Any()
    not_field = Not(negated=negated_field)
    assert not_field.negated == negated_field, "Constructor failed to initialize 'negated' field"


# Generated at 2024-03-18 08:45:54.905729
# Unit test for constructor of class Not
def test_Not():    # Test that the constructor correctly initializes the 'negated' field
    field = Any()
    not_field = Not(negated=field)
    assert not_field.negated == field, "The 'negated' field should be initialized with the provided field"


# Generated at 2024-03-18 08:45:57.722950
# Unit test for constructor of class Not
def test_Not():    # Test that the constructor correctly initializes the `negated` field
    field = Any()
    not_field = Not(negated=field)
    assert not_field.negated == field, "The `negated` field should be initialized with the passed argument"


# Generated at 2024-03-18 08:46:09.702755
# Unit test for constructor of class OneOf
def test_OneOf():    # Test that the constructor correctly assigns the 'one_of' parameter
    field1 = Field()
    field2 = Field()
    one_of_field = OneOf(one_of=[field1, field2])
    assert one_of_field.one_of == [field1, field2], "Constructor failed to assign 'one_of' parameter correctly"

    # Test that the constructor raises an AssertionError if 'allow_null' is passed in kwargs
    try:
        OneOf(one_of=[field1, field2], allow_null=True)
        assert False, "Constructor should not accept 'allow_null' as a kwarg"
    except AssertionError:
        assert True


# Generated at 2024-03-18 08:46:20.863035
# Unit test for constructor of class OneOf
def test_OneOf():    # Test that the constructor correctly assigns the `one_of` parameter
    field1 = Field()
    field2 = Field()
    one_of_field = OneOf(one_of=[field1, field2])
    assert one_of_field.one_of == [field1, field2], "Constructor failed to assign one_of"

    # Test that the constructor raises an AssertionError if 'allow_null' is in kwargs
    try:
        OneOf(one_of=[field1, field2], allow_null=True)
        assert False, "Constructor should not accept 'allow_null' as a kwarg"
    except AssertionError:
        assert True

    # Test that the constructor correctly passes other kwargs to the parent class
    example_kwarg = "example_value"
    one_of_field_with_kwargs = OneOf(one_of=[field1, field2], example_kwarg=example_kwarg)

# Generated at 2024-03-18 08:46:28.896557
# Unit test for constructor of class OneOf
def test_OneOf():    # Test that the constructor correctly assigns the 'one_of' parameter
    field1 = Field()
    field2 = Field()
    one_of_field = OneOf(one_of=[field1, field2])
    assert one_of_field.one_of == [field1, field2], "Constructor failed to assign 'one_of' parameter correctly"

    # Test that the constructor raises an AssertionError if 'allow_null' is passed in kwargs
    try:
        OneOf(one_of=[field1, field2], allow_null=True)
        assert False, "Constructor should not accept 'allow_null' as a kwarg"
    except AssertionError:
        assert True

    # Test that the constructor correctly passes other kwargs to the parent class
    one_of_field_with_kwargs = OneOf(one_of=[field1, field2], title="Test Title", description="Test Description")

# Generated at 2024-03-18 08:46:31.345883
# Unit test for constructor of class Not
def test_Not():    # Test that the constructor correctly initializes the `negated` field
    field = Field()
    not_field = Not(negated=field)
    assert not_field.negated == field, "The `negated` field should be initialized with the provided field"


# Generated at 2024-03-18 08:46:36.540856
# Unit test for constructor of class IfThenElse
def test_IfThenElse():    if_clause = NeverMatch()

# Generated at 2024-03-18 08:46:44.462184
# Unit test for constructor of class IfThenElse
def test_IfThenElse():    if_clause = NeverMatch()

# Generated at 2024-03-18 08:46:53.977532
# Unit test for constructor of class IfThenElse
def test_IfThenElse():    if_clause = NeverMatch()

# Generated at 2024-03-18 08:46:54.938313
# Unit test for constructor of class Not

# Generated at 2024-03-18 08:46:59.767390
# Unit test for constructor of class OneOf
def test_OneOf():    # Test that the constructor correctly assigns the 'one_of' attribute
    field1 = Field()
    field2 = Field()
    one_of_field = OneOf([field1, field2])
    assert one_of_field.one_of == [field1, field2], "Constructor failed to assign 'one_of' attribute correctly"

    # Test that the constructor raises an AssertionError if 'allow_null' is in kwargs
    try:
        OneOf([field1, field2], allow_null=True)
        assert False, "Constructor should not accept 'allow_null' kwarg"
    except AssertionError:
        assert True


# Generated at 2024-03-18 08:47:09.390776
# Unit test for constructor of class OneOf
def test_OneOf():    # Test that the constructor correctly assigns the 'one_of' attribute
    field1 = Field()
    field2 = Field()
    one_of_field = OneOf([field1, field2])
    assert one_of_field.one_of == [field1, field2], "Constructor must assign 'one_of' attribute"

    # Test that the constructor raises an AssertionError if 'allow_null' is in kwargs
    try:
        OneOf([field1, field2], allow_null=True)
        assert False, "'allow_null' should not be accepted by the constructor"
    except AssertionError:
        assert True

    # Test that the constructor does not raise an error for other kwargs
    try:
        OneOf([field1, field2], example="example")
        assert True, "Constructor should accept other kwargs"
    except AssertionError:
        assert False, "Constructor should not raise an error for other kwargs"


# Generated at 2024-03-18 08:47:33.447194
# Unit test for constructor of class IfThenElse
def test_IfThenElse():    if_clause = NeverMatch()

# Generated at 2024-03-18 08:47:39.233167
# Unit test for constructor of class IfThenElse
def test_IfThenElse():    if_clause = NeverMatch()

# Generated at 2024-03-18 08:47:46.511595
# Unit test for constructor of class OneOf
def test_OneOf():    # Test that the constructor correctly assigns the `one_of` parameter
    field1 = Field()
    field2 = Field()
    one_of_field = OneOf(one_of=[field1, field2])
    assert one_of_field.one_of == [field1, field2], "Constructor must assign `one_of` parameter"

    # Test that the constructor raises an AssertionError if `allow_null` is passed in kwargs
    try:
        OneOf(one_of=[field1, field2], allow_null=True)
        assert False, "Constructor should not accept `allow_null` in kwargs"
    except AssertionError:
        assert True

    # Test that the constructor correctly passes other kwargs to the parent class
    example_kwargs = {'example_key': 'example_value'}
    one_of_field_with_kwargs = OneOf(one_of=[field1, field2], **example_kwargs)

# Generated at 2024-03-18 08:47:53.010951
# Unit test for constructor of class Not
def test_Not():    # Test that the constructor correctly initializes the `negated` field
    field = Any()
    not_field = Not(negated=field)
    assert not_field.negated == field, "The `negated` field should be initialized with the passed argument."

    # Test that the constructor raises an AssertionError if 'allow_null' is in kwargs
    try:
        Not(negated=field, allow_null=True)
        assert False, "AssertionError should be raised when 'allow_null' is in kwargs"
    except AssertionError:
        assert True, "AssertionError was raised as expected"


# Generated at 2024-03-18 08:47:59.290460
# Unit test for constructor of class IfThenElse
def test_IfThenElse():    if_clause = NeverMatch()

# Generated at 2024-03-18 08:48:03.821055
# Unit test for constructor of class IfThenElse
def test_IfThenElse():    if_clause = NeverMatch()

# Generated at 2024-03-18 08:48:08.366647
# Unit test for constructor of class OneOf
def test_OneOf():    # Test that the constructor correctly assigns the 'one_of' attribute
    field1 = Field()
    field2 = Field()
    one_of_field = OneOf([field1, field2])
    assert one_of_field.one_of == [field1, field2], "Constructor failed to assign 'one_of' attribute correctly"

    # Test that the constructor raises an AssertionError if 'allow_null' is in kwargs
    try:
        OneOf([field1, field2], allow_null=True)
        assert False, "Constructor should not accept 'allow_null' as a keyword argument"
    except AssertionError:
        assert True


# Generated at 2024-03-18 08:48:20.105000
# Unit test for constructor of class Not
def test_Not():    # Test that the constructor correctly initializes the 'negated' field
    negated_field = Any()
    not_field = Not(negated=negated_field)
    assert not_field.negated == negated_field, "Constructor failed to initialize 'negated' field"

    # Test that the constructor raises an AssertionError if 'allow_null' is passed in kwargs
    try:
        Not(negated=negated_field, allow_null=True)
        assert False, "Constructor should not accept 'allow_null' kwarg"
    except AssertionError:
        pass


# Generated at 2024-03-18 08:48:20.837444
# Unit test for constructor of class Not

# Generated at 2024-03-18 08:48:27.722213
# Unit test for constructor of class OneOf
def test_OneOf():    # Test that the constructor correctly assigns the 'one_of' attribute
    field1 = Field()
    field2 = Field()
    one_of_field = OneOf([field1, field2])
    assert one_of_field.one_of == [field1, field2], "Constructor must assign 'one_of' attribute"

    # Test that the constructor raises an assertion error if 'allow_null' is in kwargs
    try:
        OneOf([field1, field2], allow_null=True)
        assert False, "'allow_null' should not be accepted by the OneOf constructor"
    except AssertionError:
        assert True

    # Test that the constructor does not raise an error for other kwargs
    try:
        OneOf([field1, field2], example="example")
        assert True, "Constructor should accept other kwargs"
    except AssertionError:
        assert False, "Constructor should not raise an error for other kwargs"


# Generated at 2024-03-18 08:49:07.265648
# Unit test for constructor of class Not
def test_Not():    # Test that the constructor correctly initializes the 'negated' field
    field = Any()
    not_field = Not(negated=field)
    assert not_field.negated == field, "The 'negated' field should be initialized with the provided field"


# Generated at 2024-03-18 08:49:15.957535
# Unit test for constructor of class IfThenElse
def test_IfThenElse():    if_clause = NeverMatch()

# Generated at 2024-03-18 08:49:17.124016
# Unit test for constructor of class Not

# Generated at 2024-03-18 08:49:19.715619
# Unit test for constructor of class Not
def test_Not():    negated_field = Any()

# Generated at 2024-03-18 08:49:24.818718
# Unit test for constructor of class Not
def test_Not():    # Test that the constructor correctly initializes the 'negated' field
    negated_field = Any()
    not_field = Not(negated=negated_field)
    assert not_field.negated == negated_field, "Constructor failed to initialize 'negated' field"

    # Test that the constructor raises an AssertionError if 'allow_null' is passed in kwargs
    try:
        Not(negated=negated_field, allow_null=True)
        assert False, "Constructor should not accept 'allow_null' kwarg"
    except AssertionError:
        assert True


# Generated at 2024-03-18 08:49:27.044978
# Unit test for constructor of class Not
def test_Not():    # Test that the constructor correctly initializes the 'negated' field
    field = Any()
    not_field = Not(negated=field)
    assert not_field.negated == field, "The 'negated' field should be initialized with the provided field"


# Generated at 2024-03-18 08:49:35.160170
# Unit test for constructor of class OneOf
def test_OneOf():    # Test that the constructor correctly assigns the `one_of` parameter
    field1 = Field()
    field2 = Field()
    one_of_field = OneOf(one_of=[field1, field2])
    assert one_of_field.one_of == [field1, field2], "Constructor must assign `one_of` parameter"

    # Test that the constructor raises an AssertionError if `allow_null` is passed in kwargs
    try:
        OneOf(one_of=[field1, field2], allow_null=True)
        assert False, "Constructor should not accept `allow_null` in kwargs"
    except AssertionError:
        assert True

    # Test that the constructor correctly passes other kwargs to the parent class
    title = "Test Title"
    description = "Test Description"
    one_of_field_with_kwargs = OneOf(one_of=[field1, field2], title=title, description=description)

# Generated at 2024-03-18 08:49:35.789141
# Unit test for constructor of class Not

# Generated at 2024-03-18 08:49:46.259362
# Unit test for constructor of class OneOf
def test_OneOf():    # Test that the constructor correctly assigns the 'one_of' parameter
    field1 = Any()
    field2 = Any()
    one_of_field = OneOf([field1, field2])
    assert one_of_field.one_of == [field1, field2], "Constructor must assign 'one_of' parameter"

    # Test that the constructor raises an AssertionError if 'allow_null' is in kwargs
    try:
        OneOf([field1, field2], allow_null=True)
        assert False, "Constructor should not accept 'allow_null' in kwargs"
    except AssertionError:
        assert True

    # Test that the constructor correctly passes other kwargs to the parent class
    example_kwargs = {'example_key': 'example_value'}
    one_of_field_with_kwargs = OneOf([field1, field2], **example_kwargs)
    assert one_of_field_with_kwargs.example_key == 'example_value', "Constructor must pass kwargs to parent class"


# Generated at 2024-03-18 08:49:51.748238
# Unit test for constructor of class OneOf
def test_OneOf():    # Test that the constructor correctly assigns the `one_of` parameter
    string_field = typesystem.fields.String()
    integer_field = typesystem.fields.Integer()
    one_of_field = OneOf([string_field, integer_field])
    assert one_of_field.one_of == [string_field, integer_field], "Constructor failed to assign `one_of`"

    # Test that the constructor raises an AssertionError if `allow_null` is passed in kwargs
    try:
        one_of_field_with_null = OneOf([string_field, integer_field], allow_null=True)
    except AssertionError:
        pass
    else:
        assert False, "Constructor should not accept `allow_null` as a kwarg"
