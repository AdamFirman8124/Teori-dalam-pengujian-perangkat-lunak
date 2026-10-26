

# Generated at 2026-10-25 07:14:24.313758
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 07:14:26.730474
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 07:14:29.146400
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 07:14:31.563285
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:14:33.977674
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:14:36.392153
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:14:38.809787
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:14:40.223372
# Unit test for function validate_yaml
def test_validate_yaml():from typesystem import String, Integer


# Generated at 2026-10-25 07:14:56.782482
# Unit test for function tokenize_yaml
def test_tokenize_yaml():import pytest

from typesystem.base import ParseError, Position
from typesystem.tokenize.tokens import DictToken, ListToken, ScalarToken

# Import the module under test (adjust path to your layout)
from typesystem.tokenize.yaml import tokenize_yaml


def test_tokenize_yaml_mapping():
    token = module_0.tokenize_yaml("key: value")
    assert isinstance(token, DictToken)
    assert token.content == "key: value"
    assert token.value == {"key": "value"}


def test_tokenize_yaml_nested():
    content = "parent:\n  child: 1\n"
    token = module_0.tokenize_yaml(content)
    assert isinstance(token, DictToken)
    assert token.value == {"parent": {"child": 1}}

    child = token.find(["parent"])
    assert isinstance(child, DictToken)
    assert child.value == {"child": 1}

    scalar = token.find(["parent", "child"])
    assert isinstance(scalar, ScalarToken)
    assert scalar.value == 1
    # Position of the scalar "1": line 2, column 9
    assert scalar.start == content.index("1")
    assert scalar.get_position() == Position(line_no=2, column_no=9, char_index=scalar.start)


def test_tokenize_yaml_sequence():
    token = module_0.tokenize_yaml("- a\n- b\n")
    assert isinstance(token, ListToken)
    assert token.value == ["a", "b"]


def test_tokenize_yaml_scalar_types():
    token = module_0.tokenize_yaml("int: 123\nfloat: 1.5\nbool: true\nnull: null\n")
    assert token.find(["int"]).value == 123
    assert token.find(["float"]).value == 1.5
    assert token.find(["bool"]).value is True
    assert token.find(["null"]).value is None


def test_tokenize_yaml_multidocument_takes_first():
    # yaml.load with a SafeLoader parses a single document â
    # multiple documents raise a ComposerError, which is NOT caught.
    with pytest.raises(Exception):
        module_0.tokenize_yaml("---\na: 1\n---\nb: 2\n")


def test_tokenize_yaml_bytes_input():
    token = module_0.tokenize_yaml(b"key: value\n")
    assert token.value == {"key": "value"}
    # positions must index into the decoded string, not the bytes
    assert token.content == "key: value\n"


def test_tokenize_yaml_empty_string():
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_yaml("")
    error = exc_info.value
    assert error.text == "No content."
    assert error.code == "no_content"
    assert error.position == Position(column_no=1, line_no=1, char_index=0)


def test_tokenize_yaml_whitespace_only():
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_yaml("   \n  \n")
    assert exc_info.value.code == "no_content"


def test_tokenize_yaml_parse_error():
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_yaml("key: [unclosed")
    error = exc_info.value
    assert error.code == "parse_error"
    assert error.text.endswith(".")
    assert error.position.line_no == 1
    assert error.position.char_index >= 0


def test_tokenize_yaml_parse_error_line_number():
    content = "a: 1\nb: [oops\n"
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_yaml(content)
    assert exc_info.value.position.line_no == 2


def test_tokenize_yaml_requires_pyyaml(monkeypatch):
    from typesystem.tokenize import yaml as yaml_module

    monkeypatch.setattr(yaml_module, "yaml", None)
    with pytest.raises(AssertionError, match="'pyyaml' must be installed."):
        yaml_module.tokenize_yaml("key: value")

# Generated at 2026-10-25 07:15:13.287984
# Unit test for function tokenize_yaml
def test_tokenize_yaml():import pytest

from typesystem.base import ParseError, Position
from typesystem.tokenize.tokens import DictToken, ListToken, ScalarToken

# Import the module under test (adjust path to your layout)
from typesystem.tokenize.yaml import tokenize_yaml


def test_tokenize_yaml_mapping():
    token = module_0.tokenize_yaml("key: value")
    assert isinstance(token, DictToken)
    assert token.content == "key: value"
    assert token.value == {"key": "value"}


def test_tokenize_yaml_nested():
    content = "parent:\n  child: 1\n"
    token = module_0.tokenize_yaml(content)
    assert isinstance(token, DictToken)
    assert token.value == {"parent": {"child": 1}}

    child = token.find(["parent"])
    assert isinstance(child, DictToken)
    assert child.value == {"child": 1}

    scalar = token.find(["parent", "child"])
    assert isinstance(scalar, ScalarToken)
    assert scalar.value == 1
    # Position of the scalar "1": line 2, column 9
    assert scalar.start == content.index("1")
    assert scalar.get_position() == Position(line_no=2, column_no=9, char_index=scalar.start)


def test_tokenize_yaml_sequence():
    token = module_0.tokenize_yaml("- a\n- b\n")
    assert isinstance(token, ListToken)
    assert token.value == ["a", "b"]


def test_tokenize_yaml_scalar_types():
    token = module_0.tokenize_yaml("int: 123\nfloat: 1.5\nbool: true\nnull: null\n")
    assert token.find(["int"]).value == 123
    assert token.find(["float"]).value == 1.5
    assert token.find(["bool"]).value is True
    assert token.find(["null"]).value is None


def test_tokenize_yaml_multidocument_takes_first():
    # yaml.load with a SafeLoader parses a single document â
    # multiple documents raise a ComposerError, which is NOT caught.
    with pytest.raises(Exception):
        module_0.tokenize_yaml("---\na: 1\n---\nb: 2\n")


def test_tokenize_yaml_bytes_input():
    token = module_0.tokenize_yaml(b"key: value\n")
    assert token.value == {"key": "value"}
    # positions must index into the decoded string, not the bytes
    assert token.content == "key: value\n"


def test_tokenize_yaml_empty_string():
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_yaml("")
    error = exc_info.value
    assert error.text == "No content."
    assert error.code == "no_content"
    assert error.position == Position(column_no=1, line_no=1, char_index=0)


def test_tokenize_yaml_whitespace_only():
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_yaml("   \n  \n")
    assert exc_info.value.code == "no_content"


def test_tokenize_yaml_parse_error():
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_yaml("key: [unclosed")
    error = exc_info.value
    assert error.code == "parse_error"
    assert error.text.endswith(".")
    assert error.position.line_no == 1
    assert error.position.char_index >= 0


def test_tokenize_yaml_parse_error_line_number():
    content = "a: 1\nb: [oops\n"
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_yaml(content)
    assert exc_info.value.position.line_no == 2


def test_tokenize_yaml_requires_pyyaml(monkeypatch):
    from typesystem.tokenize import yaml as yaml_module

    monkeypatch.setattr(yaml_module, "yaml", None)
    with pytest.raises(AssertionError, match="'pyyaml' must be installed."):
        yaml_module.tokenize_yaml("key: value")

# Generated at 2026-10-25 07:15:16.001672
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 07:15:18.418885
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 07:15:20.836699
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 07:15:23.453306
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:15:25.866851
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:15:28.283303
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:15:30.877282
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:15:33.296561
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:15:35.708940
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:15:38.376446
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:15:40.797304
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:15:43.209217
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:15:45.625621
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:15:48.041108
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:15:50.456370
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:15:52.871982
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:16:08.970556
# Unit test for function validate_yaml
def test_validate_yaml():from typesystem.fields import Field

# Generated at 2026-10-25 07:16:25.460483
# Unit test for function validate_yaml
def test_validate_yaml():
    import pytest

    from typesystem.base import ParseError, ValidationError
    from typesystem.fields import Integer, String

    if yaml is None:
        pytest.skip("pyyaml is not installed.")

    class Person(Schema):
        name = String()
        age = Integer()

    # 1. Valid YAML string validates and returns the parsed value.
    value = module_0.validate_yaml("name: Alice\nage: 30\n", Person)
    assert value == {"name": "Alice", "age": 30}

    # 2. Bytes input is decoded and validated the same way.
    value = module_0.validate_yaml(b"name: Bob\nage: 25\n", Person)
    assert value == {"name": "Bob", "age": 25}

    # 3. Missing required field raises ValidationError with position info.
    with pytest.raises(ValidationError) as exc_info:
        module_0.validate_yaml("age: 30\n", Person)
    assert len(exc_info.value.messages) == 1
    message = exc_info.value.messages[0]
    assert message.code == "required"
    assert message.start_position is not None
    assert message.start_position.line_no == 1

    # 4. Wrong scalar type raises ValidationError pointing at the value.
    with pytest.raises(ValidationError) as exc_info:
        module_0.validate_yaml("name: Alice\nage: not_a_number\n", Person)
    message = exc_info.value.messages[0]
    assert message.code in ("parse", "invalid")
    assert message.start_position.line_no == 2

    # 5. Malformed YAML raises ParseError with a nonzero position.
    with pytest.raises(ParseError) as exc_info:
        module_0.validate_yaml("name: [unclosed\n", Person)
    assert exc_info.value.code == "parse_error"
    assert exc_info.value.position.line_no >= 1

    # 6. Empty content raises ParseError with code "no_content".
    with pytest.raises(ParseError) as exc_info:
        module_0.validate_yaml("   \n", Person)
    assert exc_info.value.code == "no_content"
    assert exc_info.value.position.line_no == 1
    assert exc_info.value.position.column_no == 1

# Generated at 2026-10-25 07:16:28.429466
# Unit test for function validate_yaml
def test_validate_yaml():
    import pytest

    from typesystem.base import ParseError, ValidationError
    from typesystem.fields import Integer, String

    if yaml is None:
        pytest.skip("pyyaml is not installed.")

    class Person(Schema):
        name = String()
        age = Integer()

    # 1. Valid YAML string validates and returns the parsed value.
    value = module_0.validate_yaml("name: Alice\nage: 30\n", Person)
    assert value == {"name": "Alice", "age": 30}

    # 2. Bytes input is decoded and validated the same way.
    value = module_0.validate_yaml(b"name: Bob\nage: 25\n", Person)
    assert value == {"name": "Bob", "age": 25}

    # 3. Missing required field raises ValidationError with position info.
    with pytest.raises(ValidationError) as exc_info:
        module_0.validate_yaml("age: 30\n", Person)
    assert len(exc_info.value.messages) == 1
    message = exc_info.value.messages[0]
    assert message.code == "required"
    assert message.start_position is not None
    assert message.start_position.line_no == 1

    # 4. Wrong scalar type raises ValidationError pointing at the value.
    with pytest.raises(ValidationError) as exc_info:
        module_0.validate_yaml("name: Alice\nage: not_a_number\n", Person)
    message = exc_info.value.messages[0]
    assert message.code in ("parse", "invalid")
    assert message.start_position.line_no == 2

    # 5. Malformed YAML raises ParseError with a nonzero position.
    with pytest.raises(ParseError) as exc_info:
        module_0.validate_yaml("name: [unclosed\n", Person)
    assert exc_info.value.code == "parse_error"
    assert exc_info.value.position.line_no >= 1

    # 6. Empty content raises ParseError with code "no_content".
    with pytest.raises(ParseError) as exc_info:
        module_0.validate_yaml("   \n", Person)
    assert exc_info.value.code == "no_content"
    assert exc_info.value.position.line_no == 1
    assert exc_info.value.position.column_no == 1

# Generated at 2026-10-25 07:16:31.289906
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 07:16:33.703435
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 07:16:36.123340
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 07:16:38.664347
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 07:16:41.079650
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 07:16:43.495569
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 07:16:45.999521
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 07:16:48.355368
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 07:16:50.770414
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 07:16:53.185835
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:16:55.924443
# Unit test for function validate_yaml
def test_validate_yaml():from typesystem.fields import Field

# Generated at 2026-10-25 07:16:58.642199
# Unit test for function validate_yaml
def test_validate_yaml():
    import pytest

    from typesystem.base import ParseError, ValidationError
    from typesystem.fields import Integer, String

    if yaml is None:
        pytest.skip("pyyaml is not installed.")

    class Person(Schema):
        name = String()
        age = Integer()

    # 1. Valid YAML string validates and returns the parsed value.
    value = module_0.validate_yaml("name: Alice\nage: 30\n", Person)
    assert value == {"name": "Alice", "age": 30}

    # 2. Bytes input is decoded and validated the same way.
    value = module_0.validate_yaml(b"name: Bob\nage: 25\n", Person)
    assert value == {"name": "Bob", "age": 25}

    # 3. Missing required field raises ValidationError with position info.
    with pytest.raises(ValidationError) as exc_info:
        module_0.validate_yaml("age: 30\n", Person)
    assert len(exc_info.value.messages) == 1
    message = exc_info.value.messages[0]
    assert message.code == "required"
    assert message.start_position is not None
    assert message.start_position.line_no == 1

    # 4. Wrong scalar type raises ValidationError pointing at the value.
    with pytest.raises(ValidationError) as exc_info:
        module_0.validate_yaml("name: Alice\nage: not_a_number\n", Person)
    message = exc_info.value.messages[0]
    assert message.code in ("parse", "invalid")
    assert message.start_position.line_no == 2

    # 5. Malformed YAML raises ParseError with a nonzero position.
    with pytest.raises(ParseError) as exc_info:
        module_0.validate_yaml("name: [unclosed\n", Person)
    assert exc_info.value.code == "parse_error"
    assert exc_info.value.position.line_no >= 1

    # 6. Empty content raises ParseError with code "no_content".
    with pytest.raises(ParseError) as exc_info:
        module_0.validate_yaml("   \n", Person)
    assert exc_info.value.code == "no_content"
    assert exc_info.value.position.line_no == 1
    assert exc_info.value.position.column_no == 1

# Generated at 2026-10-25 07:17:01.330211
# Unit test for function validate_yaml
def test_validate_yaml():
    import pytest

    from typesystem.base import ParseError, ValidationError
    from typesystem.fields import Integer, String

    if yaml is None:
        pytest.skip("pyyaml is not installed.")

    class Person(Schema):
        name = String()
        age = Integer()

    # 1. Valid YAML string validates and returns the parsed value.
    value = module_0.validate_yaml("name: Alice\nage: 30\n", Person)
    assert value == {"name": "Alice", "age": 30}

    # 2. Bytes input is decoded and validated the same way.
    value = module_0.validate_yaml(b"name: Bob\nage: 25\n", Person)
    assert value == {"name": "Bob", "age": 25}

    # 3. Missing required field raises ValidationError with position info.
    with pytest.raises(ValidationError) as exc_info:
        module_0.validate_yaml("age: 30\n", Person)
    assert len(exc_info.value.messages) == 1
    message = exc_info.value.messages[0]
    assert message.code == "required"
    assert message.start_position is not None
    assert message.start_position.line_no == 1

    # 4. Wrong scalar type raises ValidationError pointing at the value.
    with pytest.raises(ValidationError) as exc_info:
        module_0.validate_yaml("name: Alice\nage: not_a_number\n", Person)
    message = exc_info.value.messages[0]
    assert message.code in ("parse", "invalid")
    assert message.start_position.line_no == 2

    # 5. Malformed YAML raises ParseError with a nonzero position.
    with pytest.raises(ParseError) as exc_info:
        module_0.validate_yaml("name: [unclosed\n", Person)
    assert exc_info.value.code == "parse_error"
    assert exc_info.value.position.line_no >= 1

    # 6. Empty content raises ParseError with code "no_content".
    with pytest.raises(ParseError) as exc_info:
        module_0.validate_yaml("   \n", Person)
    assert exc_info.value.code == "no_content"
    assert exc_info.value.position.line_no == 1
    assert exc_info.value.position.column_no == 1

# Generated at 2026-10-25 07:17:04.055601
# Unit test for function validate_yaml
def test_validate_yaml():
    import pytest

    from typesystem.base import ParseError, ValidationError
    from typesystem.fields import Integer, String

    if yaml is None:
        pytest.skip("pyyaml is not installed.")

    class Person(Schema):
        name = String()
        age = Integer()

    # 1. Valid YAML string validates and returns the parsed value.
    value = module_0.validate_yaml("name: Alice\nage: 30\n", Person)
    assert value == {"name": "Alice", "age": 30}

    # 2. Bytes input is decoded and validated the same way.
    value = module_0.validate_yaml(b"name: Bob\nage: 25\n", Person)
    assert value == {"name": "Bob", "age": 25}

    # 3. Missing required field raises ValidationError with position info.
    with pytest.raises(ValidationError) as exc_info:
        module_0.validate_yaml("age: 30\n", Person)
    assert len(exc_info.value.messages) == 1
    message = exc_info.value.messages[0]
    assert message.code == "required"
    assert message.start_position is not None
    assert message.start_position.line_no == 1

    # 4. Wrong scalar type raises ValidationError pointing at the value.
    with pytest.raises(ValidationError) as exc_info:
        module_0.validate_yaml("name: Alice\nage: not_a_number\n", Person)
    message = exc_info.value.messages[0]
    assert message.code in ("parse", "invalid")
    assert message.start_position.line_no == 2

    # 5. Malformed YAML raises ParseError with a nonzero position.
    with pytest.raises(ParseError) as exc_info:
        module_0.validate_yaml("name: [unclosed\n", Person)
    assert exc_info.value.code == "parse_error"
    assert exc_info.value.position.line_no >= 1

    # 6. Empty content raises ParseError with code "no_content".
    with pytest.raises(ParseError) as exc_info:
        module_0.validate_yaml("   \n", Person)
    assert exc_info.value.code == "no_content"
    assert exc_info.value.position.line_no == 1
    assert exc_info.value.position.column_no == 1

# Generated at 2026-10-25 07:17:07.144448
# Unit test for function validate_yaml
def test_validate_yaml():
    import pytest

    from typesystem.base import ParseError, ValidationError
    from typesystem.fields import Integer, String

    if yaml is None:
        pytest.skip("pyyaml is not installed.")

    class Person(Schema):
        name = String()
        age = Integer()

    # 1. Valid YAML string validates and returns the parsed value.
    value = module_0.validate_yaml("name: Alice\nage: 30\n", Person)
    assert value == {"name": "Alice", "age": 30}

    # 2. Bytes input is decoded and validated the same way.
    value = module_0.validate_yaml(b"name: Bob\nage: 25\n", Person)
    assert value == {"name": "Bob", "age": 25}

    # 3. Missing required field raises ValidationError with position info.
    with pytest.raises(ValidationError) as exc_info:
        module_0.validate_yaml("age: 30\n", Person)
    assert len(exc_info.value.messages) == 1
    message = exc_info.value.messages[0]
    assert message.code == "required"
    assert message.start_position is not None
    assert message.start_position.line_no == 1

    # 4. Wrong scalar type raises ValidationError pointing at the value.
    with pytest.raises(ValidationError) as exc_info:
        module_0.validate_yaml("name: Alice\nage: not_a_number\n", Person)
    message = exc_info.value.messages[0]
    assert message.code in ("parse", "invalid")
    assert message.start_position.line_no == 2

    # 5. Malformed YAML raises ParseError with a nonzero position.
    with pytest.raises(ParseError) as exc_info:
        module_0.validate_yaml("name: [unclosed\n", Person)
    assert exc_info.value.code == "parse_error"
    assert exc_info.value.position.line_no >= 1

    # 6. Empty content raises ParseError with code "no_content".
    with pytest.raises(ParseError) as exc_info:
        module_0.validate_yaml("   \n", Person)
    assert exc_info.value.code == "no_content"
    assert exc_info.value.position.line_no == 1
    assert exc_info.value.position.column_no == 1

# Generated at 2026-10-25 07:17:09.827408
# Unit test for function validate_yaml
def test_validate_yaml():
    import pytest

    from typesystem.base import ParseError, ValidationError
    from typesystem.fields import Integer, String

    if yaml is None:
        pytest.skip("pyyaml is not installed.")

    class Person(Schema):
        name = String()
        age = Integer()

    # 1. Valid YAML string validates and returns the parsed value.
    value = module_0.validate_yaml("name: Alice\nage: 30\n", Person)
    assert value == {"name": "Alice", "age": 30}

    # 2. Bytes input is decoded and validated the same way.
    value = module_0.validate_yaml(b"name: Bob\nage: 25\n", Person)
    assert value == {"name": "Bob", "age": 25}

    # 3. Missing required field raises ValidationError with position info.
    with pytest.raises(ValidationError) as exc_info:
        module_0.validate_yaml("age: 30\n", Person)
    assert len(exc_info.value.messages) == 1
    message = exc_info.value.messages[0]
    assert message.code == "required"
    assert message.start_position is not None
    assert message.start_position.line_no == 1

    # 4. Wrong scalar type raises ValidationError pointing at the value.
    with pytest.raises(ValidationError) as exc_info:
        module_0.validate_yaml("name: Alice\nage: not_a_number\n", Person)
    message = exc_info.value.messages[0]
    assert message.code in ("parse", "invalid")
    assert message.start_position.line_no == 2

    # 5. Malformed YAML raises ParseError with a nonzero position.
    with pytest.raises(ParseError) as exc_info:
        module_0.validate_yaml("name: [unclosed\n", Person)
    assert exc_info.value.code == "parse_error"
    assert exc_info.value.position.line_no >= 1

    # 6. Empty content raises ParseError with code "no_content".
    with pytest.raises(ParseError) as exc_info:
        module_0.validate_yaml("   \n", Person)
    assert exc_info.value.code == "no_content"
    assert exc_info.value.position.line_no == 1
    assert exc_info.value.position.column_no == 1

# Generated at 2026-10-25 07:17:12.831201
# Unit test for function validate_yaml
def test_validate_yaml():
    import pytest

    from typesystem.base import ParseError, ValidationError
    from typesystem.fields import Integer, String

    if yaml is None:
        pytest.skip("pyyaml is not installed.")

    class Person(Schema):
        name = String()
        age = Integer()

    # 1. Valid YAML string validates and returns the parsed value.
    value = module_0.validate_yaml("name: Alice\nage: 30\n", Person)
    assert value == {"name": "Alice", "age": 30}

    # 2. Bytes input is decoded and validated the same way.
    value = module_0.validate_yaml(b"name: Bob\nage: 25\n", Person)
    assert value == {"name": "Bob", "age": 25}

    # 3. Missing required field raises ValidationError with position info.
    with pytest.raises(ValidationError) as exc_info:
        module_0.validate_yaml("age: 30\n", Person)
    assert len(exc_info.value.messages) == 1
    message = exc_info.value.messages[0]
    assert message.code == "required"
    assert message.start_position is not None
    assert message.start_position.line_no == 1

    # 4. Wrong scalar type raises ValidationError pointing at the value.
    with pytest.raises(ValidationError) as exc_info:
        module_0.validate_yaml("name: Alice\nage: not_a_number\n", Person)
    message = exc_info.value.messages[0]
    assert message.code in ("parse", "invalid")
    assert message.start_position.line_no == 2

    # 5. Malformed YAML raises ParseError with a nonzero position.
    with pytest.raises(ParseError) as exc_info:
        module_0.validate_yaml("name: [unclosed\n", Person)
    assert exc_info.value.code == "parse_error"
    assert exc_info.value.position.line_no >= 1

    # 6. Empty content raises ParseError with code "no_content".
    with pytest.raises(ParseError) as exc_info:
        module_0.validate_yaml("   \n", Person)
    assert exc_info.value.code == "no_content"
    assert exc_info.value.position.line_no == 1
    assert exc_info.value.position.column_no == 1

# Generated at 2026-10-25 07:17:15.744443
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 07:17:18.390998
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 07:17:20.804419
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 07:17:23.225054
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:17:25.651231
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:17:28.067503
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:17:30.485035
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:17:32.901249
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:17:35.522020
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:17:37.938178
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:17:40.352847
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:17:42.771854
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:17:45.183118
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:17:47.600965
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:17:50.014037
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:17:52.432508
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 07:17:54.848265
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 07:17:57.262043
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 07:17:59.681702
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:18:02.098351
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:18:04.513598
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:18:06.930953
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 07:18:09.347029
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 07:18:11.760729
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 07:18:14.178301
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:18:16.596410
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:18:19.017467
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:18:21.429055
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:18:23.848447
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:18:26.263967
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:18:28.729692
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:18:31.124258
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:18:33.541861
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:18:35.955093
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:18:38.372463
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:18:40.789675
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:18:43.203748
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:18:45.626405
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:18:48.043042
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:18:50.455881
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:18:52.872074
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:18:55.287639
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:18:57.703990
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 07:19:00.155430
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 07:19:02.568497
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 07:19:04.980665
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:19:07.395930
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:19:09.816785
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:19:12.234545
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:19:14.650163
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:19:17.066825
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:19:19.484917
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:19:21.899950
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:19:24.317422
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:19:26.734906
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:19:29.149936
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:19:31.565353
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:19:33.984576
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 07:19:36.402458
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 07:19:38.814195
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 07:19:41.230360
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:19:43.647288
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:19:46.062768
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:19:48.481678
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:19:50.901176
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:19:53.313291
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:19:55.729969
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:19:58.144515
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:20:00.560457
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:20:02.974869
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:20:05.393494
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:20:07.808442
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:20:10.220388
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:20:12.635948
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:20:15.052449
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:20:17.593861
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:20:20.010465
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:20:22.423608
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:20:24.838725
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 07:20:27.255143
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 07:20:29.672571
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 07:20:32.086943
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 07:20:34.501668
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 07:20:36.919642
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 07:20:39.337397
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:20:41.751342
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:20:44.170148
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:20:46.586781
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:20:49.006247
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:20:51.423910
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:20:53.842070
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 07:20:56.255578
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 07:20:58.673351
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 07:21:01.091066
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:21:03.505463
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:21:05.920759
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:21:10.131710
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:21:12.550608
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:21:14.969662
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:21:17.384760
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:21:19.799862
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:21:22.256310
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:21:24.673350
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 07:21:27.087682
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 07:21:29.494740
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 07:21:31.913305
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:21:34.332265
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:21:36.749641
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:21:39.164332
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:21:41.577474
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:21:43.992385
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:21:46.406054
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:21:48.821212
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:21:51.235133
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:21:53.648883
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:21:56.064977
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:21:58.478948
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:22:01.217094
# Unit test for function validate_yaml
def test_validate_yaml():
    import pytest

    from typesystem.base import ParseError, ValidationError
    from typesystem.fields import Integer, String

    if yaml is None:
        pytest.skip("pyyaml is not installed.")

    class Person(Schema):
        name = String()
        age = Integer()

    # 1. Valid YAML string validates and returns the parsed value.
    value = module_0.validate_yaml("name: Alice\nage: 30\n", Person)
    assert value == {"name": "Alice", "age": 30}

    # 2. Bytes input is decoded and validated the same way.
    value = module_0.validate_yaml(b"name: Bob\nage: 25\n", Person)
    assert value == {"name": "Bob", "age": 25}

    # 3. Missing required field raises ValidationError with position info.
    with pytest.raises(ValidationError) as exc_info:
        module_0.validate_yaml("age: 30\n", Person)
    assert len(exc_info.value.messages) == 1
    message = exc_info.value.messages[0]
    assert message.code == "required"
    assert message.start_position is not None
    assert message.start_position.line_no == 1

    # 4. Wrong scalar type raises ValidationError pointing at the value.
    with pytest.raises(ValidationError) as exc_info:
        module_0.validate_yaml("name: Alice\nage: not_a_number\n", Person)
    message = exc_info.value.messages[0]
    assert message.code in ("parse", "invalid")
    assert message.start_position.line_no == 2

    # 5. Malformed YAML raises ParseError with a nonzero position.
    with pytest.raises(ParseError) as exc_info:
        module_0.validate_yaml("name: [unclosed\n", Person)
    assert exc_info.value.code == "parse_error"
    assert exc_info.value.position.line_no >= 1

    # 6. Empty content raises ParseError with code "no_content".
    with pytest.raises(ParseError) as exc_info:
        module_0.validate_yaml("   \n", Person)
    assert exc_info.value.code == "no_content"
    assert exc_info.value.position.line_no == 1
    assert exc_info.value.position.column_no == 1

# Generated at 2026-10-25 07:22:04.006411
# Unit test for function validate_yaml
def test_validate_yaml():
    import pytest

    from typesystem.base import ParseError, ValidationError
    from typesystem.fields import Integer, String

    if yaml is None:
        pytest.skip("pyyaml is not installed.")

    class Person(Schema):
        name = String()
        age = Integer()

    # 1. Valid YAML string validates and returns the parsed value.
    value = module_0.validate_yaml("name: Alice\nage: 30\n", Person)
    assert value == {"name": "Alice", "age": 30}

    # 2. Bytes input is decoded and validated the same way.
    value = module_0.validate_yaml(b"name: Bob\nage: 25\n", Person)
    assert value == {"name": "Bob", "age": 25}

    # 3. Missing required field raises ValidationError with position info.
    with pytest.raises(ValidationError) as exc_info:
        module_0.validate_yaml("age: 30\n", Person)
    assert len(exc_info.value.messages) == 1
    message = exc_info.value.messages[0]
    assert message.code == "required"
    assert message.start_position is not None
    assert message.start_position.line_no == 1

    # 4. Wrong scalar type raises ValidationError pointing at the value.
    with pytest.raises(ValidationError) as exc_info:
        module_0.validate_yaml("name: Alice\nage: not_a_number\n", Person)
    message = exc_info.value.messages[0]
    assert message.code in ("parse", "invalid")
    assert message.start_position.line_no == 2

    # 5. Malformed YAML raises ParseError with a nonzero position.
    with pytest.raises(ParseError) as exc_info:
        module_0.validate_yaml("name: [unclosed\n", Person)
    assert exc_info.value.code == "parse_error"
    assert exc_info.value.position.line_no >= 1

    # 6. Empty content raises ParseError with code "no_content".
    with pytest.raises(ParseError) as exc_info:
        module_0.validate_yaml("   \n", Person)
    assert exc_info.value.code == "no_content"
    assert exc_info.value.position.line_no == 1
    assert exc_info.value.position.column_no == 1

# Generated at 2026-10-25 07:22:06.967469
# Unit test for function validate_yaml
def test_validate_yaml():
    import pytest

    from typesystem.base import ParseError, ValidationError
    from typesystem.fields import Integer, String

    if yaml is None:
        pytest.skip("pyyaml is not installed.")

    class Person(Schema):
        name = String()
        age = Integer()

    # 1. Valid YAML string validates and returns the parsed value.
    value = module_0.validate_yaml("name: Alice\nage: 30\n", Person)
    assert value == {"name": "Alice", "age": 30}

    # 2. Bytes input is decoded and validated the same way.
    value = module_0.validate_yaml(b"name: Bob\nage: 25\n", Person)
    assert value == {"name": "Bob", "age": 25}

    # 3. Missing required field raises ValidationError with position info.
    with pytest.raises(ValidationError) as exc_info:
        module_0.validate_yaml("age: 30\n", Person)
    assert len(exc_info.value.messages) == 1
    message = exc_info.value.messages[0]
    assert message.code == "required"
    assert message.start_position is not None
    assert message.start_position.line_no == 1

    # 4. Wrong scalar type raises ValidationError pointing at the value.
    with pytest.raises(ValidationError) as exc_info:
        module_0.validate_yaml("name: Alice\nage: not_a_number\n", Person)
    message = exc_info.value.messages[0]
    assert message.code in ("parse", "invalid")
    assert message.start_position.line_no == 2

    # 5. Malformed YAML raises ParseError with a nonzero position.
    with pytest.raises(ParseError) as exc_info:
        module_0.validate_yaml("name: [unclosed\n", Person)
    assert exc_info.value.code == "parse_error"
    assert exc_info.value.position.line_no >= 1

    # 6. Empty content raises ParseError with code "no_content".
    with pytest.raises(ParseError) as exc_info:
        module_0.validate_yaml("   \n", Person)
    assert exc_info.value.code == "no_content"
    assert exc_info.value.position.line_no == 1
    assert exc_info.value.position.column_no == 1

# Generated at 2026-10-25 07:22:13.316108
# Unit test for function validate_yaml
def test_validate_yaml():
    import pytest

    from typesystem.base import ParseError, ValidationError
    from typesystem.fields import Integer, String

    if yaml is None:
        pytest.skip("pyyaml is not installed.")

    class Person(Schema):
        name = String()
        age = Integer()

    # 1. Valid YAML string validates and returns the parsed value.
    value = module_0.validate_yaml("name: Alice\nage: 30\n", Person)
    assert value == {"name": "Alice", "age": 30}

    # 2. Bytes input is decoded and validated the same way.
    value = module_0.validate_yaml(b"name: Bob\nage: 25\n", Person)
    assert value == {"name": "Bob", "age": 25}

    # 3. Missing required field raises ValidationError with position info.
    with pytest.raises(ValidationError) as exc_info:
        module_0.validate_yaml("age: 30\n", Person)
    assert len(exc_info.value.messages) == 1
    message = exc_info.value.messages[0]
    assert message.code == "required"
    assert message.start_position is not None
    assert message.start_position.line_no == 1

    # 4. Wrong scalar type raises ValidationError pointing at the value.
    with pytest.raises(ValidationError) as exc_info:
        module_0.validate_yaml("name: Alice\nage: not_a_number\n", Person)
    message = exc_info.value.messages[0]
    assert message.code in ("parse", "invalid")
    assert message.start_position.line_no == 2

    # 5. Malformed YAML raises ParseError with a nonzero position.
    with pytest.raises(ParseError) as exc_info:
        module_0.validate_yaml("name: [unclosed\n", Person)
    assert exc_info.value.code == "parse_error"
    assert exc_info.value.position.line_no >= 1

    # 6. Empty content raises ParseError with code "no_content".
    with pytest.raises(ParseError) as exc_info:
        module_0.validate_yaml("   \n", Person)
    assert exc_info.value.code == "no_content"
    assert exc_info.value.position.line_no == 1
    assert exc_info.value.position.column_no == 1

# Generated at 2026-10-25 07:22:29.802289
# Unit test for function tokenize_yaml
def test_tokenize_yaml():import pytest

from typesystem.base import ParseError, Position
from typesystem.tokenize.tokens import DictToken, ListToken, ScalarToken

# Import the module under test (adjust path to your layout)
from typesystem.tokenize.yaml import tokenize_yaml


def test_tokenize_yaml_mapping():
    token = module_0.tokenize_yaml("key: value")
    assert isinstance(token, DictToken)
    assert token.content == "key: value"
    assert token.value == {"key": "value"}


def test_tokenize_yaml_nested():
    content = "parent:\n  child: 1\n"
    token = module_0.tokenize_yaml(content)
    assert isinstance(token, DictToken)
    assert token.value == {"parent": {"child": 1}}

    child = token.find(["parent"])
    assert isinstance(child, DictToken)
    assert child.value == {"child": 1}

    scalar = token.find(["parent", "child"])
    assert isinstance(scalar, ScalarToken)
    assert scalar.value == 1
    # Position of the scalar "1": line 2, column 9
    assert scalar.start == content.index("1")
    assert scalar.get_position() == Position(line_no=2, column_no=9, char_index=scalar.start)


def test_tokenize_yaml_sequence():
    token = module_0.tokenize_yaml("- a\n- b\n")
    assert isinstance(token, ListToken)
    assert token.value == ["a", "b"]


def test_tokenize_yaml_scalar_types():
    token = module_0.tokenize_yaml("int: 123\nfloat: 1.5\nbool: true\nnull: null\n")
    assert token.find(["int"]).value == 123
    assert token.find(["float"]).value == 1.5
    assert token.find(["bool"]).value is True
    assert token.find(["null"]).value is None


def test_tokenize_yaml_multidocument_takes_first():
    # yaml.load with a SafeLoader parses a single document â
    # multiple documents raise a ComposerError, which is NOT caught.
    with pytest.raises(Exception):
        module_0.tokenize_yaml("---\na: 1\n---\nb: 2\n")


def test_tokenize_yaml_bytes_input():
    token = module_0.tokenize_yaml(b"key: value\n")
    assert token.value == {"key": "value"}
    # positions must index into the decoded string, not the bytes
    assert token.content == "key: value\n"


def test_tokenize_yaml_empty_string():
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_yaml("")
    error = exc_info.value
    assert error.text == "No content."
    assert error.code == "no_content"
    assert error.position == Position(column_no=1, line_no=1, char_index=0)


def test_tokenize_yaml_whitespace_only():
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_yaml("   \n  \n")
    assert exc_info.value.code == "no_content"


def test_tokenize_yaml_parse_error():
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_yaml("key: [unclosed")
    error = exc_info.value
    assert error.code == "parse_error"
    assert error.text.endswith(".")
    assert error.position.line_no == 1
    assert error.position.char_index >= 0


def test_tokenize_yaml_parse_error_line_number():
    content = "a: 1\nb: [oops\n"
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_yaml(content)
    assert exc_info.value.position.line_no == 2


def test_tokenize_yaml_requires_pyyaml(monkeypatch):
    from typesystem.tokenize import yaml as yaml_module

    monkeypatch.setattr(yaml_module, "yaml", None)
    with pytest.raises(AssertionError, match="'pyyaml' must be installed."):
        yaml_module.tokenize_yaml("key: value")

# Generated at 2026-10-25 07:22:32.224621
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:22:34.639789
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:22:37.054353
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:22:39.469428
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:22:41.883841
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:22:44.298741
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:22:47.006438
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 07:22:49.422914
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 07:22:51.836228
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 07:22:54.250518
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:22:56.668708
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:22:59.080442
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:23:01.496072
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 07:23:03.910957
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 07:23:06.327946
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 07:23:08.746398
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:23:11.163493
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:23:13.576298
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:23:15.994185
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:23:18.411664
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:23:20.824307
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:23:23.238006
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:23:25.651936
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:23:28.068040
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:23:42.591867
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:23:45.006239
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:23:47.421121
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:23:49.838757
# Unit test for function validate_yaml

# Generated at 2026-10-25 07:23:51.427238
# Unit test for function validate_yaml
def test_validate_yaml():from typesystem import String, Integer


# Generated at 2026-10-25 07:23:54.327613
# Unit test for function validate_yaml
def test_validate_yaml():
    import pytest

    from typesystem.base import ParseError, ValidationError
    from typesystem.fields import Integer, String

    if yaml is None:
        pytest.skip("pyyaml is not installed.")

    class Person(Schema):
        name = String()
        age = Integer()

    # 1. Valid YAML string validates and returns the parsed value.
    value = module_0.validate_yaml("name: Alice\nage: 30\n", Person)
    assert value == {"name": "Alice", "age": 30}

    # 2. Bytes input is decoded and validated the same way.
    value = module_0.validate_yaml(b"name: Bob\nage: 25\n", Person)
    assert value == {"name": "Bob", "age": 25}

    # 3. Missing required field raises ValidationError with position info.
    with pytest.raises(ValidationError) as exc_info:
        module_0.validate_yaml("age: 30\n", Person)
    assert len(exc_info.value.messages) == 1
    message = exc_info.value.messages[0]
    assert message.code == "required"
    assert message.start_position is not None
    assert message.start_position.line_no == 1

    # 4. Wrong scalar type raises ValidationError pointing at the value.
    with pytest.raises(ValidationError) as exc_info:
        module_0.validate_yaml("name: Alice\nage: not_a_number\n", Person)
    message = exc_info.value.messages[0]
    assert message.code in ("parse", "invalid")
    assert message.start_position.line_no == 2

    # 5. Malformed YAML raises ParseError with a nonzero position.
    with pytest.raises(ParseError) as exc_info:
        module_0.validate_yaml("name: [unclosed\n", Person)
    assert exc_info.value.code == "parse_error"
    assert exc_info.value.position.line_no >= 1

    # 6. Empty content raises ParseError with code "no_content".
    with pytest.raises(ParseError) as exc_info:
        module_0.validate_yaml("   \n", Person)
    assert exc_info.value.code == "no_content"
    assert exc_info.value.position.line_no == 1
    assert exc_info.value.position.column_no == 1

# Generated at 2026-10-25 07:23:57.027165
# Unit test for function validate_yaml
def test_validate_yaml():
    import pytest

    from typesystem.base import ParseError, ValidationError
    from typesystem.fields import Integer, String

    if yaml is None:
        pytest.skip("pyyaml is not installed.")

    class Person(Schema):
        name = String()
        age = Integer()

    # 1. Valid YAML string validates and returns the parsed value.
    value = module_0.validate_yaml("name: Alice\nage: 30\n", Person)
    assert value == {"name": "Alice", "age": 30}

    # 2. Bytes input is decoded and validated the same way.
    value = module_0.validate_yaml(b"name: Bob\nage: 25\n", Person)
    assert value == {"name": "Bob", "age": 25}

    # 3. Missing required field raises ValidationError with position info.
    with pytest.raises(ValidationError) as exc_info:
        module_0.validate_yaml("age: 30\n", Person)
    assert len(exc_info.value.messages) == 1
    message = exc_info.value.messages[0]
    assert message.code == "required"
    assert message.start_position is not None
    assert message.start_position.line_no == 1

    # 4. Wrong scalar type raises ValidationError pointing at the value.
    with pytest.raises(ValidationError) as exc_info:
        module_0.validate_yaml("name: Alice\nage: not_a_number\n", Person)
    message = exc_info.value.messages[0]
    assert message.code in ("parse", "invalid")
    assert message.start_position.line_no == 2

    # 5. Malformed YAML raises ParseError with a nonzero position.
    with pytest.raises(ParseError) as exc_info:
        module_0.validate_yaml("name: [unclosed\n", Person)
    assert exc_info.value.code == "parse_error"
    assert exc_info.value.position.line_no >= 1

    # 6. Empty content raises ParseError with code "no_content".
    with pytest.raises(ParseError) as exc_info:
        module_0.validate_yaml("   \n", Person)
    assert exc_info.value.code == "no_content"
    assert exc_info.value.position.line_no == 1
    assert exc_info.value.position.column_no == 1