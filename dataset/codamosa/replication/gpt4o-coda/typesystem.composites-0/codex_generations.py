

# Generated at 2024-06-04 19:26:42.993815
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():    if_clause = Field()

# Generated at 2024-06-04 19:26:44.650311
# Unit test for constructor of class NeverMatch
def test_NeverMatch():    field = NeverMatch()

# Generated at 2024-06-04 19:26:53.634549
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():    # Define some mock fields for testing
    class MockField(Field):
        def __init__(self, should_validate: bool, **kwargs: typing.Any) -> None:
            super().__init__(**kwargs)
            self.should_validate = should_validate

        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            if self.should_validate:
                return value
            raise self.validation_error("mock_error")

    # Test cases
    if_clause = MockField(should_validate=True)
    then_clause = MockField(should_validate=True)
    else_clause = MockField(should_validate=True)

    field = IfThenElse(if_clause=if_clause, then_clause=then_clause, else_clause=else_clause)
    assert field.validate("test") == "test"

    if_clause = MockField(should_validate=False)
    then_clause = MockField(should_validate=True)
    else_clause = MockField(should_validate=True)



# Generated at 2024-06-04 19:26:56.399189
# Unit test for method validate of class Not
def test_Not_validate():    field = Not(negated=NeverMatch())

# Generated at 2024-06-04 19:26:58.465639
# Unit test for method validate of class Not
def test_Not_validate():    field = Any()

# Generated at 2024-06-04 19:27:03.585402
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():    # Define some mock fields for testing
    class MockField(Field):
        def __init__(self, should_validate: bool, **kwargs: typing.Any) -> None:
            super().__init__(**kwargs)
            self.should_validate = should_validate

        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            if self.should_validate:
                return value
            raise self.validation_error("mock_error")

    # Test case where if_clause validates and then_clause is used
    if_clause = MockField(should_validate=True)
    then_clause = MockField(should_validate=True)
    else_clause = MockField(should_validate=False)
    field = IfThenElse(if_clause=if_clause, then_clause=then_clause, else_clause=else_clause)
    assert field.validate("test_value") == "test_value"

    # Test case where if_clause does not validate and else_clause is used
    if_clause = MockField

# Generated at 2024-06-04 19:27:05.974183
# Unit test for method validate of class Not
def test_Not_validate():    field = Not(negated=NeverMatch())

    # Test case where the value should pass validation

# Generated at 2024-06-04 19:27:08.799016
# Unit test for method validate of class Not
def test_Not_validate():    field = Not(negated=NeverMatch())

# Generated at 2024-06-04 19:27:11.904422
# Unit test for method validate of class OneOf
def test_OneOf_validate():    field1 = Any()

# Generated at 2024-06-04 19:27:12.855352
# Unit test for constructor of class NeverMatch
def test_NeverMatch():    field = NeverMatch()

# Generated at 2024-06-04 19:27:19.616988
# Unit test for constructor of class NeverMatch
def test_NeverMatch():    field = NeverMatch()

# Generated at 2024-06-04 19:27:24.870039
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():    if_clause = Field()

# Generated at 2024-06-04 19:27:28.052257
# Unit test for method validate of class Not
def test_Not_validate():    field = Not(negated=NeverMatch())

# Generated at 2024-06-04 19:27:29.631213
# Unit test for constructor of class Not
def test_Not():    field = Any()

# Generated at 2024-06-04 19:27:30.700960
# Unit test for constructor of class NeverMatch
def test_NeverMatch():    field = NeverMatch()

# Generated at 2024-06-04 19:27:32.027130
# Unit test for constructor of class Not
def test_Not():    field = Any()

# Generated at 2024-06-04 19:27:36.923366
# Unit test for method validate of class OneOf
def test_OneOf_validate():    field1 = Any()

# Generated at 2024-06-04 19:27:40.990347
# Unit test for method validate of class OneOf
def test_OneOf_validate():    field1 = Any()

# Generated at 2024-06-04 19:27:42.189629
# Unit test for constructor of class Not
def test_Not():    field = Any()

# Generated at 2024-06-04 19:27:43.213363
# Unit test for constructor of class NeverMatch
def test_NeverMatch():    field = NeverMatch()

# Generated at 2024-06-04 19:27:51.742412
# Unit test for method validate of class OneOf
def test_OneOf_validate():    field1 = Any()

# Generated at 2024-06-04 19:27:54.497877
# Unit test for method validate of class Not
def test_Not_validate():    field = Any()

# Generated at 2024-06-04 19:27:56.323297
# Unit test for method validate of class Not
def test_Not_validate():    field = Not(negated=NeverMatch())

    # Test case where the value should pass validation

# Generated at 2024-06-04 19:28:00.896185
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():    # Define some mock fields for testing
    class MockField(Field):
        def __init__(self, should_validate: bool, **kwargs: typing.Any) -> None:
            super().__init__(**kwargs)
            self.should_validate = should_validate

        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            if self.should_validate:
                return value
            raise self.validation_error("mock_error")

    # Test case where if_clause is True and then_clause is used
    if_clause = MockField(should_validate=True)
    then_clause = MockField(should_validate=True)
    else_clause = MockField(should_validate=False)
    field = IfThenElse(if_clause=if_clause, then_clause=then_clause, else_clause=else_clause)
    assert field.validate("test") == "test"

    # Test case where if_clause is False and else_clause is used

# Generated at 2024-06-04 19:28:05.482502
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():    # Define some mock fields for testing
    class MockField(Field):
        def __init__(self, should_validate: bool, **kwargs: typing.Any) -> None:
            super().__init__(**kwargs)
            self.should_validate = should_validate

        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            if self.should_validate:
                return value
            raise self.validation_error("mock_error")

    # Test case where if_clause validates and then_clause is used
    if_clause = MockField(should_validate=True)
    then_clause = MockField(should_validate=True)
    else_clause = MockField(should_validate=False)
    field = IfThenElse(if_clause=if_clause, then_clause=then_clause, else_clause=else_clause)
    assert field.validate("test") == "test"

    # Test case where if_clause does not validate and else_clause is used

# Generated at 2024-06-04 19:28:08.617520
# Unit test for method validate of class OneOf
def test_OneOf_validate():    field1 = Any()

# Generated at 2024-06-04 19:28:12.329303
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():    true_field = Field()

# Generated at 2024-06-04 19:28:13.820773
# Unit test for constructor of class Not
def test_Not():    field = Any()

# Generated at 2024-06-04 19:28:17.505204
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():    # Define some mock fields for testing
    class MockField(Field):
        def __init__(self, should_validate: bool, **kwargs: typing.Any) -> None:
            super().__init__(**kwargs)
            self.should_validate = should_validate

        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            if self.should_validate:
                return value
            raise self.validation_error("mock_error")

    # Test case where if_clause is True and then_clause is used
    if_clause = MockField(should_validate=True)
    then_clause = MockField(should_validate=True)
    else_clause = MockField(should_validate=False)
    field = IfThenElse(if_clause=if_clause, then_clause=then_clause, else_clause=else_clause)
    assert field.validate("test") == "test"

    # Test case where if_clause is False and else_clause is used

# Generated at 2024-06-04 19:28:23.030520
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():    # Define some mock fields for testing
    class MockField(Field):
        def __init__(self, should_validate: bool, **kwargs: typing.Any) -> None:
            super().__init__(**kwargs)
            self.should_validate = should_validate

        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            if self.should_validate:
                return value
            raise self.validation_error("mock_error")

    # Test cases
    if_clause = MockField(should_validate=True)
    then_clause = MockField(should_validate=True)
    else_clause = MockField(should_validate=True)

    field = IfThenElse(if_clause=if_clause, then_clause=then_clause, else_clause=else_clause)
    assert field.validate("test") == "test"

    if_clause = MockField(should_validate=False)
    then_clause = MockField(should_validate=True)
    else_clause = MockField(should_validate=True)



# Generated at 2024-06-04 19:28:31.424139
# Unit test for method validate of class OneOf
def test_OneOf_validate():    field1 = Any()

# Generated at 2024-06-04 19:28:36.081890
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():    true_field = Field()

# Generated at 2024-06-04 19:28:40.463834
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():    # Define some mock fields for testing
    class MockField(Field):
        def __init__(self, should_validate: bool, **kwargs: typing.Any) -> None:
            super().__init__(**kwargs)
            self.should_validate = should_validate

        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            if self.should_validate:
                return value
            raise self.validation_error("mock_error")

    # Test cases
    if_clause = MockField(should_validate=True)
    then_clause = MockField(should_validate=True)
    else_clause = MockField(should_validate=True)

    field = IfThenElse(if_clause=if_clause, then_clause=then_clause, else_clause=else_clause)

    # Case 1: if_clause validates, should return then_clause validation
    assert field.validate("test_value") == "test_value"

    # Case 2: if_clause does not validate, should return else

# Generated at 2024-06-04 19:28:44.022736
# Unit test for method validate of class OneOf
def test_OneOf_validate():    field1 = Any()

# Generated at 2024-06-04 19:28:45.151722
# Unit test for constructor of class NeverMatch
def test_NeverMatch():    field = NeverMatch()

# Generated at 2024-06-04 19:28:50.225345
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():    true_field = Field()

# Generated at 2024-06-04 19:28:52.080080
# Unit test for method validate of class Not
def test_Not_validate():    field = Not(negated=NeverMatch())

# Generated at 2024-06-04 19:28:56.094067
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():    # Define some mock fields for testing
    class MockField(Field):
        def __init__(self, should_validate: bool, **kwargs: typing.Any) -> None:
            super().__init__(**kwargs)
            self.should_validate = should_validate

        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            if self.should_validate:
                return value
            raise self.validation_error("mock_error")

    # Test cases
    if_clause = MockField(should_validate=True)
    then_clause = MockField(should_validate=True)
    else_clause = MockField(should_validate=True)

    field = IfThenElse(if_clause=if_clause, then_clause=then_clause, else_clause=else_clause)
    assert field.validate("test") == "test"

    if_clause = MockField(should_validate=False)
    then_clause = MockField(should_validate=True)
    else_clause = MockField(should_validate=True)



# Generated at 2024-06-04 19:29:00.315088
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():    # Define some mock fields for testing
    class MockField(Field):
        def __init__(self, should_validate: bool, **kwargs: typing.Any) -> None:
            super().__init__(**kwargs)
            self.should_validate = should_validate

        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            if self.should_validate:
                return value
            raise self.validation_error("mock_error")

    if_clause = MockField(should_validate=True)
    then_clause = MockField(should_validate=True)
    else_clause = MockField(should_validate=True)

    # Test case where if_clause validates
    field = IfThenElse(if_clause=if_clause, then_clause=then_clause, else_clause=else_clause)
    assert field.validate("test") == "test"

    # Test case where if_clause does not validate, but else_clause does
    if_clause = MockField(should_validate=False)
    field

# Generated at 2024-06-04 19:29:05.986754
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():    # Define some mock fields for testing
    class MockField(Field):
        def __init__(self, should_validate: bool, **kwargs: typing.Any) -> None:
            super().__init__(**kwargs)
            self.should_validate = should_validate

        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            if self.should_validate:
                return value
            raise self.validation_error("mock_error")

    # Test case where if_clause validates and then_clause is used
    if_clause = MockField(should_validate=True)
    then_clause = MockField(should_validate=True)
    else_clause = MockField(should_validate=False)
    field = IfThenElse(if_clause=if_clause, then_clause=then_clause, else_clause=else_clause)
    assert field.validate("test_value") == "test_value"

    # Test case where if_clause does not validate and else_clause is used
    if_clause = MockField

# Generated at 2024-06-04 19:29:12.084407
# Unit test for constructor of class NeverMatch
def test_NeverMatch():    field = NeverMatch()

# Generated at 2024-06-04 19:29:17.550341
# Unit test for method validate of class OneOf
def test_OneOf_validate():    field1 = Any()

# Generated at 2024-06-04 19:29:22.422187
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():    # Define some mock fields for testing
    class MockField(Field):
        def __init__(self, should_validate: bool, **kwargs: typing.Any) -> None:
            super().__init__(**kwargs)
            self.should_validate = should_validate

        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            if self.should_validate:
                return value
            raise self.validation_error("mock_error")

    # Test case where if_clause validates and then_clause is used
    if_clause = MockField(should_validate=True)
    then_clause = MockField(should_validate=True)
    else_clause = MockField(should_validate=False)
    field = IfThenElse(if_clause=if_clause, then_clause=then_clause, else_clause=else_clause)
    assert field.validate("test_value") == "test_value"

    # Test case where if_clause does not validate and else_clause is used
    if_clause = MockField

# Generated at 2024-06-04 19:29:25.918805
# Unit test for method validate of class OneOf
def test_OneOf_validate():    field1 = Any()

# Generated at 2024-06-04 19:29:29.814290
# Unit test for method validate of class Not
def test_Not_validate():    field = Not(negated=NeverMatch())

# Generated at 2024-06-04 19:29:33.831028
# Unit test for method validate of class Not
def test_Not_validate():    field = Not(negated=NeverMatch())

# Generated at 2024-06-04 19:29:38.016287
# Unit test for method validate of class OneOf
def test_OneOf_validate():    field1 = Any()

# Generated at 2024-06-04 19:29:41.386521
# Unit test for method validate of class OneOf
def test_OneOf_validate():    field1 = Any()

# Generated at 2024-06-04 19:29:44.710770
# Unit test for method validate of class OneOf
def test_OneOf_validate():    field1 = Any()

# Generated at 2024-06-04 19:29:50.264303
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():    # Define some mock fields for testing
    class MockField(Field):
        def __init__(self, should_validate: bool, **kwargs: typing.Any) -> None:
            super().__init__(**kwargs)
            self.should_validate = should_validate

        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            if self.should_validate:
                return value
            raise self.validation_error("mock_error")

    # Test cases
    if_clause = MockField(should_validate=True)
    then_clause = MockField(should_validate=True)
    else_clause = MockField(should_validate=True)

    field = IfThenElse(if_clause=if_clause, then_clause=then_clause, else_clause=else_clause)

    # Case 1: if_clause validates, should return then_clause validation
    assert field.validate("test") == "test"

    # Case 2: if_clause does not validate, should return else_clause validation

# Generated at 2024-06-04 19:29:57.773225
# Unit test for constructor of class NeverMatch
def test_NeverMatch():    field = NeverMatch()

# Generated at 2024-06-04 19:30:00.850932
# Unit test for method validate of class OneOf
def test_OneOf_validate():    field1 = Any()

# Generated at 2024-06-04 19:30:03.501274
# Unit test for method validate of class Not
def test_Not_validate():    field = Not(negated=NeverMatch())
    
    # Test case where the value should pass validation

# Generated at 2024-06-04 19:30:08.927417
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():    true_field = Field()

# Generated at 2024-06-04 19:30:14.228832
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():    # Define some mock fields for testing
    class MockField(Field):
        def __init__(self, should_validate: bool, **kwargs: typing.Any) -> None:
            super().__init__(**kwargs)
            self.should_validate = should_validate

        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            if self.should_validate:
                return value
            raise self.validation_error("mock_error")

    # Test cases
    if_clause = MockField(should_validate=True)
    then_clause = MockField(should_validate=True)
    else_clause = MockField(should_validate=True)

    field = IfThenElse(if_clause=if_clause, then_clause=then_clause, else_clause=else_clause)

    # Case 1: if_clause validates, should return then_clause validation
    assert field.validate("test") == "test"

    # Case 2: if_clause does not validate, should return else_clause validation

# Generated at 2024-06-04 19:30:17.805379
# Unit test for method validate of class OneOf
def test_OneOf_validate():    field1 = Any()

# Generated at 2024-06-04 19:30:21.413313
# Unit test for method validate of class Not
def test_Not_validate():    field = Any()

# Generated at 2024-06-04 19:30:25.889532
# Unit test for method validate of class OneOf
def test_OneOf_validate():    field1 = Any()

# Generated at 2024-06-04 19:30:31.790401
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():    # Define some mock fields for testing
    class MockField(Field):
        def __init__(self, should_validate: bool, **kwargs: typing.Any) -> None:
            super().__init__(**kwargs)
            self.should_validate = should_validate

        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            if self.should_validate:
                return value
            raise self.validation_error("mock_error")

    # Test case where if_clause is True and then_clause is used
    if_clause = MockField(should_validate=True)
    then_clause = MockField(should_validate=True)
    else_clause = MockField(should_validate=False)
    field = IfThenElse(if_clause=if_clause, then_clause=then_clause, else_clause=else_clause)
    assert field.validate("test") == "test"

    # Test case where if_clause is False and else_clause is used

# Generated at 2024-06-04 19:30:36.162837
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():    # Define some mock fields for testing
    class MockField(Field):
        def __init__(self, should_validate: bool, **kwargs: typing.Any) -> None:
            super().__init__(**kwargs)
            self.should_validate = should_validate

        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            if self.should_validate:
                return value
            raise self.validation_error("mock_error")

    # Test case where if_clause validates and then_clause is used
    if_clause = MockField(should_validate=True)
    then_clause = MockField(should_validate=True)
    else_clause = MockField(should_validate=False)
    field = IfThenElse(if_clause=if_clause, then_clause=then_clause, else_clause=else_clause)
    assert field.validate("test_value") == "test_value"

    # Test case where if_clause does not validate and else_clause is used
    if_clause = MockField

# Generated at 2024-06-04 19:30:47.059924
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():    # Define some mock fields for testing
    class MockField(Field):
        def __init__(self, should_validate: bool, **kwargs: typing.Any) -> None:
            super().__init__(**kwargs)
            self.should_validate = should_validate

        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            if self.should_validate:
                return value
            raise self.validation_error("mock_error")

    # Test case where if_clause is True and then_clause is used
    if_clause = MockField(should_validate=True)
    then_clause = MockField(should_validate=True)
    else_clause = MockField(should_validate=False)
    field = IfThenElse(if_clause=if_clause, then_clause=then_clause, else_clause=else_clause)
    assert field.validate("test") == "test"

    # Test case where if_clause is False and else_clause is used

# Generated at 2024-06-04 19:30:50.835085
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():    # Define some mock fields for testing
    class MockField(Field):
        def __init__(self, should_validate: bool, **kwargs: typing.Any) -> None:
            super().__init__(**kwargs)
            self.should_validate = should_validate

        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            if self.should_validate:
                return value
            raise self.validation_error("mock_error")

    if_clause = MockField(should_validate=True)
    then_clause = MockField(should_validate=True)
    else_clause = MockField(should_validate=True)

    # Test case where if_clause validates
    field = IfThenElse(if_clause=if_clause, then_clause=then_clause, else_clause=else_clause)
    assert field.validate("test") == "test"

    # Test case where if_clause does not validate, but else_clause does
    if_clause = MockField(should_validate=False)
    field

# Generated at 2024-06-04 19:30:52.049269
# Unit test for constructor of class Not
def test_Not():    field = Any()

# Generated at 2024-06-04 19:30:55.489511
# Unit test for method validate of class OneOf
def test_OneOf_validate():    field1 = Any()

# Generated at 2024-06-04 19:30:59.956546
# Unit test for method validate of class Not
def test_Not_validate():    field = Field()

# Generated at 2024-06-04 19:31:06.516606
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():    true_field = Field()

# Generated at 2024-06-04 19:31:12.045559
# Unit test for method validate of class OneOf
def test_OneOf_validate():    field1 = Any()

# Generated at 2024-06-04 19:31:15.734971
# Unit test for method validate of class OneOf
def test_OneOf_validate():    field1 = Any()

# Generated at 2024-06-04 19:31:21.583554
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():    true_field = Field()

# Generated at 2024-06-04 19:31:25.543426
# Unit test for method validate of class OneOf
def test_OneOf_validate():    field1 = Any()

# Generated at 2024-06-04 19:31:35.938841
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():    # Define some mock fields for testing
    class MockField(Field):
        def __init__(self, should_validate: bool, **kwargs: typing.Any) -> None:
            super().__init__(**kwargs)
            self.should_validate = should_validate

        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            if self.should_validate:
                return value
            raise self.validation_error("mock_error")

    if_clause = MockField(should_validate=True)
    then_clause = MockField(should_validate=True)
    else_clause = MockField(should_validate=True)
    field = IfThenElse(if_clause=if_clause, then_clause=then_clause, else_clause=else_clause)

    # Test case where if_clause validates
    assert field.validate("test_value") == "test_value"

    # Test case where if_clause does not validate, but else_clause does
    if_clause.should_validate = False
    assert field

# Generated at 2024-06-04 19:31:37.066072
# Unit test for constructor of class NeverMatch
def test_NeverMatch():    field = NeverMatch()

# Generated at 2024-06-04 19:31:40.683586
# Unit test for method validate of class Not
def test_Not_validate():    field = Not(negated=NeverMatch())

# Generated at 2024-06-04 19:31:42.340257
# Unit test for constructor of class Not
def test_Not():    field = Any()

# Generated at 2024-06-04 19:31:46.379203
# Unit test for method validate of class OneOf
def test_OneOf_validate():    field1 = Any()

# Generated at 2024-06-04 19:31:47.580218
# Unit test for constructor of class NeverMatch
def test_NeverMatch():    field = NeverMatch()

# Generated at 2024-06-04 19:31:51.193948
# Unit test for method validate of class Not
def test_Not_validate():    field = Not(negated=NeverMatch())

# Generated at 2024-06-04 19:31:56.180163
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():    # Define some mock fields for testing
    class MockField(Field):
        def __init__(self, should_validate: bool, **kwargs: typing.Any) -> None:
            super().__init__(**kwargs)
            self.should_validate = should_validate

        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            if self.should_validate:
                return value
            raise self.validation_error("mock_error")

    # Test case where if_clause is True and then_clause is used
    if_clause = MockField(should_validate=True)
    then_clause = MockField(should_validate=True)
    else_clause = MockField(should_validate=False)
    field = IfThenElse(if_clause=if_clause, then_clause=then_clause, else_clause=else_clause)
    assert field.validate("test") == "test"

    # Test case where if_clause is False and else_clause is used

# Generated at 2024-06-04 19:31:57.338262
# Unit test for constructor of class Not
def test_Not():    field = Any()

# Generated at 2024-06-04 19:32:01.122031
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():    # Define some mock fields for testing
    class MockField(Field):
        def __init__(self, should_validate: bool, **kwargs: typing.Any) -> None:
            super().__init__(**kwargs)
            self.should_validate = should_validate

        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            if self.should_validate:
                return value
            raise self.validation_error("mock_error")

    if_clause = MockField(should_validate=True)
    then_clause = MockField(should_validate=True)
    else_clause = MockField(should_validate=True)

    # Test case where if_clause validates
    field = IfThenElse(if_clause=if_clause, then_clause=then_clause, else_clause=else_clause)
    assert field.validate("test_value") == "test_value"

    # Test case where if_clause does not validate, but else_clause does
    if_clause = MockField(should_validate=False)


# Generated at 2024-06-04 19:32:10.388483
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():    true_field = Field()

# Generated at 2024-06-04 19:32:13.935630
# Unit test for method validate of class OneOf
def test_OneOf_validate():    field1 = Any()

# Generated at 2024-06-04 19:32:15.918495
# Unit test for method validate of class Not
def test_Not_validate():    field = Not(negated=NeverMatch())
    
    # Test case where the value should pass validation

# Generated at 2024-06-04 19:32:18.954188
# Unit test for method validate of class OneOf
def test_OneOf_validate():    field1 = Any()

# Generated at 2024-06-04 19:32:22.002925
# Unit test for method validate of class Not
def test_Not_validate():    field = Not(negated=NeverMatch())

# Generated at 2024-06-04 19:32:42.820309
# Unit test for constructor of class Not
def test_Not():    field = Any()

# Generated at 2024-06-04 19:32:47.049895
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():    # Define some mock fields for testing
    class MockField(Field):
        def __init__(self, should_validate: bool, **kwargs: typing.Any) -> None:
            super().__init__(**kwargs)
            self.should_validate = should_validate

        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            if self.should_validate:
                return value
            raise self.validation_error("mock_error")

    # Test case where if_clause is True and then_clause is used
    if_clause = MockField(should_validate=True)
    then_clause = MockField(should_validate=True)
    else_clause = MockField(should_validate=False)
    field = IfThenElse(if_clause=if_clause, then_clause=then_clause, else_clause=else_clause)
    assert field.validate("test") == "test"

    # Test case where if_clause is False and else_clause is used

# Generated at 2024-06-04 19:32:51.039432
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():    true_field = Field()

# Generated at 2024-06-04 19:32:54.445661
# Unit test for method validate of class Not
def test_Not_validate():    field = Any()

# Generated at 2024-06-04 19:32:58.348695
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():    # Define some mock fields for testing
    class MockField(Field):
        def __init__(self, should_validate: bool, **kwargs: typing.Any) -> None:
            super().__init__(**kwargs)
            self.should_validate = should_validate

        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            if self.should_validate:
                return value
            raise self.validation_error("mock_error")

    # Test case where if_clause is True and then_clause is used
    if_clause = MockField(should_validate=True)
    then_clause = MockField(should_validate=True)
    else_clause = MockField(should_validate=False)
    field = IfThenElse(if_clause=if_clause, then_clause=then_clause, else_clause=else_clause)
    assert field.validate("test") == "test"

    # Test case where if_clause is False and else_clause is used

# Generated at 2024-06-04 19:33:07.672247
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():    # Define some mock fields for testing
    class MockField(Field):
        def __init__(self, should_validate: bool, **kwargs: typing.Any) -> None:
            super().__init__(**kwargs)
            self.should_validate = should_validate

        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            if self.should_validate:
                return value
            raise self.validation_error("mock_error")

    # Test case where if_clause is True and then_clause is used
    if_clause = MockField(should_validate=True)
    then_clause = MockField(should_validate=True)
    else_clause = MockField(should_validate=False)
    field = IfThenElse(if_clause=if_clause, then_clause=then_clause, else_clause=else_clause)
    assert field.validate("test") == "test"

    # Test case where if_clause is False and else_clause is used

# Generated at 2024-06-04 19:33:10.794366
# Unit test for method validate of class OneOf
def test_OneOf_validate():    field1 = Any()

# Generated at 2024-06-04 19:33:14.597014
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():    # Define some mock fields for testing
    class MockField(Field):
        def __init__(self, should_validate: bool, **kwargs: typing.Any) -> None:
            super().__init__(**kwargs)
            self.should_validate = should_validate

        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            if self.should_validate:
                return value
            raise self.validation_error("mock_error")

    if_clause = MockField(should_validate=True)
    then_clause = MockField(should_validate=True)
    else_clause = MockField(should_validate=True)
    field = IfThenElse(if_clause=if_clause, then_clause=then_clause, else_clause=else_clause)

    # Test case where if_clause validates
    assert field.validate("test_value") == "test_value"

    # Test case where if_clause does not validate, but else_clause does
    if_clause.should_validate = False
    assert field

# Generated at 2024-06-04 19:33:17.770109
# Unit test for method validate of class OneOf
def test_OneOf_validate():    field1 = Any()

# Generated at 2024-06-04 19:33:21.322349
# Unit test for method validate of class OneOf
def test_OneOf_validate():    field1 = Any()

# Generated at 2024-06-04 19:33:23.253516
# Unit test for method validate of class Not
def test_Not_validate():    field = Not(negated=NeverMatch())

# Generated at 2024-06-04 19:33:27.075783
# Unit test for method validate of class OneOf
def test_OneOf_validate():    field1 = Any()

# Generated at 2024-06-04 19:33:29.859465
# Unit test for method validate of class Not
def test_Not_validate():    field = Field()

# Generated at 2024-06-04 19:33:32.927317
# Unit test for method validate of class OneOf
def test_OneOf_validate():    field1 = Any()

# Generated at 2024-06-04 19:33:35.795772
# Unit test for method validate of class OneOf
def test_OneOf_validate():    field1 = Any()

# Generated at 2024-06-04 19:33:44.848533
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():    # Define some mock fields for testing
    class MockField(Field):
        def __init__(self, should_validate: bool, **kwargs: typing.Any) -> None:
            super().__init__(**kwargs)
            self.should_validate = should_validate

        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            if self.should_validate:
                return value
            raise self.validation_error("mock_error")

    if_clause = MockField(should_validate=True)
    then_clause = MockField(should_validate=True)
    else_clause = MockField(should_validate=True)

    # Test case where if_clause validates
    field = IfThenElse(if_clause=if_clause, then_clause=then_clause, else_clause=else_clause)
    assert field.validate("test_value") == "test_value"

    # Test case where if_clause does not validate, but else_clause does
    if_clause = MockField(should_validate=False)


# Generated at 2024-06-04 19:33:50.288287
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():    # Define some mock fields for testing
    class MockField(Field):
        def __init__(self, should_validate: bool, **kwargs: typing.Any) -> None:
            super().__init__(**kwargs)
            self.should_validate = should_validate

        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            if self.should_validate:
                return value
            raise self.validation_error("mock_error")

    if_clause = MockField(should_validate=True)
    then_clause = MockField(should_validate=True)
    else_clause = MockField(should_validate=True)
    field = IfThenElse(if_clause=if_clause, then_clause=then_clause, else_clause=else_clause)

    # Test case where if_clause validates
    assert field.validate("test_value") == "test_value"

    # Test case where if_clause does not validate, but else_clause does
    if_clause.should_validate = False
    assert field

# Generated at 2024-06-04 19:33:53.276487
# Unit test for method validate of class OneOf
def test_OneOf_validate():    field1 = Any()

# Generated at 2024-06-04 19:33:57.685942
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():    # Define some mock fields for testing
    class MockField(Field):
        def __init__(self, should_validate: bool, **kwargs: typing.Any) -> None:
            super().__init__(**kwargs)
            self.should_validate = should_validate

        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            if self.should_validate:
                return value
            raise self.validation_error("mock_error")

    # Test case where if_clause validates and then_clause is used
    if_clause = MockField(should_validate=True)
    then_clause = MockField(should_validate=True)
    else_clause = MockField(should_validate=False)
    field = IfThenElse(if_clause=if_clause, then_clause=then_clause, else_clause=else_clause)
    assert field.validate("test") == "test"

    # Test case where if_clause does not validate and else_clause is used

# Generated at 2024-06-04 19:33:58.757876
# Unit test for constructor of class NeverMatch
def test_NeverMatch():    field = NeverMatch()

# Generated at 2024-06-04 19:34:11.369419
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():    # Define some mock fields for testing
    class MockField(Field):
        def __init__(self, should_validate: bool, **kwargs: typing.Any) -> None:
            super().__init__(**kwargs)
            self.should_validate = should_validate

        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            if self.should_validate:
                return value
            raise self.validation_error("mock_error")

    # Test case where if_clause is True and then_clause is used
    if_clause = MockField(should_validate=True)
    then_clause = MockField(should_validate=True)
    else_clause = MockField(should_validate=False)
    field = IfThenElse(if_clause=if_clause, then_clause=then_clause, else_clause=else_clause)
    assert field.validate("test") == "test"

    # Test case where if_clause is False and else_clause is used

# Generated at 2024-06-04 19:34:14.850156
# Unit test for method validate of class OneOf
def test_OneOf_validate():    field1 = Any()

# Generated at 2024-06-04 19:34:19.170419
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():    # Define some mock fields for testing
    class MockField(Field):
        def __init__(self, should_validate: bool, **kwargs: typing.Any) -> None:
            super().__init__(**kwargs)
            self.should_validate = should_validate

        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            if self.should_validate:
                return value
            raise self.validation_error("mock_error")

    if_clause = MockField(should_validate=True)
    then_clause = MockField(should_validate=True)
    else_clause = MockField(should_validate=True)

    # Test case where if_clause validates
    field = IfThenElse(if_clause=if_clause, then_clause=then_clause, else_clause=else_clause)
    assert field.validate("test") == "test"

    # Test case where if_clause does not validate, but else_clause does
    if_clause = MockField(should_validate=False)
    field

# Generated at 2024-06-04 19:34:23.273531
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():    # Define some mock fields for testing
    class MockField(Field):
        def __init__(self, should_validate: bool, **kwargs: typing.Any) -> None:
            super().__init__(**kwargs)
            self.should_validate = should_validate

        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            if self.should_validate:
                return value
            raise self.validation_error("mock_error")

    # Test case where if_clause is True and then_clause is used
    if_clause = MockField(should_validate=True)
    then_clause = MockField(should_validate=True)
    else_clause = MockField(should_validate=False)
    field = IfThenElse(if_clause=if_clause, then_clause=then_clause, else_clause=else_clause)
    assert field.validate("test") == "test"

    # Test case where if_clause is False and else_clause is used

# Generated at 2024-06-04 19:34:24.424278
# Unit test for constructor of class NeverMatch
def test_NeverMatch():    field = NeverMatch()

# Generated at 2024-06-04 19:34:32.028770
# Unit test for method validate of class Not
def test_Not_validate():    field = Not(negated=NeverMatch())
    
    # Test case where the value should pass validation

# Generated at 2024-06-04 19:34:35.072709
# Unit test for method validate of class OneOf
def test_OneOf_validate():    field1 = Any()

# Generated at 2024-06-04 19:34:38.166938
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():    if_clause = Field()

# Generated at 2024-06-04 19:34:41.607177
# Unit test for method validate of class OneOf
def test_OneOf_validate():    field1 = Any()

# Generated at 2024-06-04 19:34:44.484645
# Unit test for method validate of class Not
def test_Not_validate():    field = Not(negated=NeverMatch())

# Generated at 2024-06-04 19:34:49.080407
# Unit test for method validate of class OneOf
def test_OneOf_validate():    field1 = Any()

# Generated at 2024-06-04 19:34:53.660082
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():    # Define some mock fields for testing
    class MockField(Field):
        def __init__(self, should_validate: bool, **kwargs: typing.Any) -> None:
            super().__init__(**kwargs)
            self.should_validate = should_validate

        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            if self.should_validate:
                return value
            raise self.validation_error("mock_error")

    # Test cases
    if_clause = MockField(should_validate=True)
    then_clause = MockField(should_validate=True)
    else_clause = MockField(should_validate=True)

    field = IfThenElse(if_clause=if_clause, then_clause=then_clause, else_clause=else_clause)
    assert field.validate("test") == "test"

    if_clause = MockField(should_validate=False)
    then_clause = MockField(should_validate=True)
    else_clause = MockField(should_validate=True)



# Generated at 2024-06-04 19:34:59.358707
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():    # Define some mock fields for testing
    class MockField(Field):
        def __init__(self, should_validate: bool, **kwargs: typing.Any) -> None:
            super().__init__(**kwargs)
            self.should_validate = should_validate

        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            if self.should_validate:
                return value
            raise self.validation_error("mock_error")

    # Test cases
    if_clause = MockField(should_validate=True)
    then_clause = MockField(should_validate=True)
    else_clause = MockField(should_validate=True)

    field = IfThenElse(if_clause=if_clause, then_clause=then_clause, else_clause=else_clause)
    assert field.validate("test") == "test"

    if_clause = MockField(should_validate=False)
    then_clause = MockField(should_validate=True)
    else_clause = MockField(should_validate=True)



# Generated at 2024-06-04 19:35:03.827502
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():    # Define some mock fields for testing
    class MockField(Field):
        def __init__(self, should_validate: bool, **kwargs: typing.Any) -> None:
            super().__init__(**kwargs)
            self.should_validate = should_validate

        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            if self.should_validate:
                return value
            raise self.validation_error("mock_error")

    if_clause = MockField(should_validate=True)
    then_clause = MockField(should_validate=True)
    else_clause = MockField(should_validate=True)

    # Test case where if_clause validates
    field = IfThenElse(if_clause=if_clause, then_clause=then_clause, else_clause=else_clause)
    assert field.validate("test") == "test"

    # Test case where if_clause does not validate, but else_clause does
    if_clause = MockField(should_validate=False)
    field

# Generated at 2024-06-04 19:35:08.897803
# Unit test for method validate of class OneOf
def test_OneOf_validate():    field1 = Any()

# Generated at 2024-06-04 19:35:15.225184
# Unit test for constructor of class NeverMatch
def test_NeverMatch():    field = NeverMatch()

# Generated at 2024-06-04 19:35:19.328878
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():    # Define some mock fields for testing
    class MockField(Field):
        def __init__(self, should_validate: bool, **kwargs: typing.Any) -> None:
            super().__init__(**kwargs)
            self.should_validate = should_validate

        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            if self.should_validate:
                return value
            raise self.validation_error("mock_error")

    # Test case where if_clause validates and then_clause is used
    if_clause = MockField(should_validate=True)
    then_clause = MockField(should_validate=True)
    else_clause = MockField(should_validate=False)
    field = IfThenElse(if_clause=if_clause, then_clause=then_clause, else_clause=else_clause)
    assert field.validate("test") == "test"

    # Test case where if_clause does not validate and else_clause is used

# Generated at 2024-06-04 19:35:20.559164
# Unit test for constructor of class NeverMatch
def test_NeverMatch():    field = NeverMatch()

# Generated at 2024-06-04 19:35:23.475780
# Unit test for method validate of class OneOf
def test_OneOf_validate():    field1 = Any()

# Generated at 2024-06-04 19:35:32.580733
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():    # Define some mock fields for testing
    class MockField(Field):
        def __init__(self, should_validate: bool, **kwargs: typing.Any) -> None:
            super().__init__(**kwargs)
            self.should_validate = should_validate

        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            if self.should_validate:
                return value
            raise self.validation_error("mock_error")

    if_clause = MockField(should_validate=True)
    then_clause = MockField(should_validate=True)
    else_clause = MockField(should_validate=True)
    field = IfThenElse(if_clause=if_clause, then_clause=then_clause, else_clause=else_clause)

    # Test case where if_clause is True, should return then_clause validation
    assert field.validate("test_value") == "test_value"

    # Test case where if_clause is False, should return else_clause validation

# Generated at 2024-06-04 19:35:43.154494
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():    # Define some mock fields for testing
    class MockField(Field):
        def __init__(self, should_validate: bool, **kwargs: typing.Any) -> None:
            super().__init__(**kwargs)
            self.should_validate = should_validate

        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            if self.should_validate:
                return value
            raise self.validation_error("mock_error")

    # Test cases
    if_clause = MockField(should_validate=True)
    then_clause = MockField(should_validate=True)
    else_clause = MockField(should_validate=True)

    field = IfThenElse(if_clause=if_clause, then_clause=then_clause, else_clause=else_clause)
    assert field.validate("test") == "test"

    if_clause = MockField(should_validate=False)
    then_clause = MockField(should_validate=True)
    else_clause = MockField(should_validate=True)



# Generated at 2024-06-04 19:35:46.774609
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():    true_field = Field()

# Generated at 2024-06-04 19:35:51.283012
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():    # Define some mock fields for testing
    class MockField(Field):
        def __init__(self, should_validate: bool, **kwargs: typing.Any) -> None:
            super().__init__(**kwargs)
            self.should_validate = should_validate

        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            if self.should_validate:
                return value
            raise self.validation_error("mock_error")

    # Test cases
    if_clause = MockField(should_validate=True)
    then_clause = MockField(should_validate=True)
    else_clause = MockField(should_validate=True)

    field = IfThenElse(if_clause=if_clause, then_clause=then_clause, else_clause=else_clause)
    assert field.validate("test") == "test"

    if_clause = MockField(should_validate=False)
    then_clause = MockField(should_validate=True)
    else_clause = MockField(should_validate=True)



# Generated at 2024-06-04 19:35:55.836090
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():    # Define some mock fields for testing
    class MockField(Field):
        def __init__(self, should_validate: bool, **kwargs: typing.Any) -> None:
            super().__init__(**kwargs)
            self.should_validate = should_validate

        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            if self.should_validate:
                return value
            raise self.validation_error("mock_error")

    # Test case where if_clause is True and then_clause is used
    if_clause = MockField(should_validate=True)
    then_clause = MockField(should_validate=True)
    else_clause = MockField(should_validate=False)
    field = IfThenElse(if_clause=if_clause, then_clause=then_clause, else_clause=else_clause)
    assert field.validate("test") == "test"

    # Test case where if_clause is False and else_clause is used

# Generated at 2024-06-04 19:35:56.890130
# Unit test for constructor of class NeverMatch
def test_NeverMatch():    field = NeverMatch()

# Generated at 2024-06-04 19:36:07.956888
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():    # Define some mock fields for testing
    class MockField(Field):
        def __init__(self, should_validate: bool, **kwargs: typing.Any) -> None:
            super().__init__(**kwargs)
            self.should_validate = should_validate

        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            if self.should_validate:
                return value
            raise self.validation_error("mock_error")

    # Test case where if_clause is True and then_clause is used
    if_clause = MockField(should_validate=True)
    then_clause = MockField(should_validate=True)
    else_clause = MockField(should_validate=False)
    field = IfThenElse(if_clause=if_clause, then_clause=then_clause, else_clause=else_clause)
    assert field.validate("test") == "test"

    # Test case where if_clause is False and else_clause is used

# Generated at 2024-06-04 19:36:12.741611
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():    # Define some mock fields for testing
    class MockField(Field):
        def __init__(self, should_validate: bool, **kwargs: typing.Any) -> None:
            super().__init__(**kwargs)
            self.should_validate = should_validate

        def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
            if self.should_validate:
                return value
            raise self.validation_error("mock_error")

    # Test case where if_clause is True and then_clause is used
    if_clause = MockField(should_validate=True)
    then_clause = MockField(should_validate=True)
    else_clause = MockField(should_validate=False)
    field = IfThenElse(if_clause=if_clause, then_clause=then_clause, else_clause=else_clause)
    assert field.validate("test") == "test"

    # Test case where if_clause is False and else_clause is used

# Generated at 2024-06-04 19:36:13.883417
# Unit test for constructor of class Not
def test_Not():    field = Any()

# Generated at 2024-06-04 19:36:17.296620
# Unit test for method validate of class OneOf
def test_OneOf_validate():    field1 = Any()

# Generated at 2024-06-04 19:36:22.210353
# Unit test for method validate of class IfThenElse
def test_IfThenElse_validate():    true_field = Field()