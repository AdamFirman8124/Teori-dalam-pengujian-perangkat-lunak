

# Generated at 2026-10-25 09:11:02.375449
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

# Generated at 2026-10-25 09:11:03.809440
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

# Generated at 2026-10-25 09:11:06.779197
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

# Generated at 2026-10-25 09:11:44.972633
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

# Generated at 2026-10-25 09:11:49.477882
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

# Generated at 2026-10-25 09:11:52.358860
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:11:54.774619
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:11:56.159758
# Unit test for function validate_yaml
def test_validate_yaml():from typesystem import String, Integer


# Generated at 2026-10-25 09:12:12.712723
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

# Generated at 2026-10-25 09:12:15.557313
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

# Generated at 2026-10-25 09:12:17.011058
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

# Generated at 2026-10-25 09:12:18.560773
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

# Generated at 2026-10-25 09:12:21.631369
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

# Generated at 2026-10-25 09:12:24.712657
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

# Generated at 2026-10-25 09:12:27.570618
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

# Generated at 2026-10-25 09:12:30.339733
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:12:32.969176
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:12:35.646737
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:12:38.061733
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:12:40.480742
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:12:43.060147
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:12:45.478466
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:12:47.897318
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:12:50.312713
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:12:53.012184
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 09:12:55.429816
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 09:12:57.851338
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 09:13:00.269024
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 09:13:02.686222
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 09:13:05.106346
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 09:13:07.526360
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 09:13:09.950031
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 09:13:12.365680
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 09:13:14.783109
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:13:17.202523
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:13:19.619337
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:13:22.236608
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:13:24.653064
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:13:27.070266
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:13:29.486459
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:13:31.906296
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:13:34.323842
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:13:36.739975
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:13:39.154391
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:13:41.570171
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:13:43.989835
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:13:46.408663
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:13:48.821150
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:13:51.236546
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 09:13:53.653564
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 09:13:56.070338
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 09:13:58.598873
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:14:01.018097
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:14:03.430861
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:14:05.847543
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:14:08.263596
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:14:10.679667
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:14:13.096668
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 09:14:15.516260
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 09:14:17.928941
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 09:14:20.347488
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 09:14:22.774018
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 09:14:25.180486
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 09:14:27.598203
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:14:30.016554
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:14:32.431751
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:14:34.848680
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:14:37.265000
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:14:39.681973
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:14:42.100935
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:14:44.517353
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:14:46.931751
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:14:49.349549
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:14:51.763212
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:14:54.181802
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:14:56.599548
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:14:59.017024
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:15:01.798658
# Unit test for function validate_yaml
def test_validate_yaml():from typesystem.fields import Field

# Generated at 2026-10-25 09:15:05.063020
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

# Generated at 2026-10-25 09:15:08.134248
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

# Generated at 2026-10-25 09:15:11.208815
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

# Generated at 2026-10-25 09:15:29.152910
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 09:15:31.577373
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 09:15:33.990252
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 09:15:36.403605
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:15:38.816787
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:15:41.242026
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:15:43.649731
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 09:15:46.066133
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 09:15:48.484793
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 09:15:50.903276
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 09:15:53.360735
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 09:15:55.741598
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 09:15:58.159739
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:16:00.578872
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:16:02.990373
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:16:25.037643
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

# Generated at 2026-10-25 09:16:28.006057
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

# Generated at 2026-10-25 09:16:32.545659
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

# Generated at 2026-10-25 09:16:35.315215
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

# Generated at 2026-10-25 09:16:38.207381
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

# Generated at 2026-10-25 09:16:41.079659
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

# Generated at 2026-10-25 09:16:42.533676
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

# Generated at 2026-10-25 09:16:45.073767
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:16:47.540881
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:16:50.212129
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:16:52.631179
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:16:55.044464
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:16:57.461035
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:17:00.183727
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:17:02.601510
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:17:05.020417
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:17:07.746032
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

# Generated at 2026-10-25 09:17:14.087381
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

# Generated at 2026-10-25 09:17:16.961572
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

# Generated at 2026-10-25 09:17:22.007724
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

# Generated at 2026-10-25 09:17:30.679881
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

# Generated at 2026-10-25 09:17:33.756297
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:17:36.483112
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:17:38.900033
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:17:41.313654
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:17:43.730606
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:17:46.537033
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:17:48.957019
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:17:51.371746
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:17:53.787730
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:17:56.202215
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:17:58.620157
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:18:01.037279
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:18:03.739427
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:18:06.154453
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:18:08.570833
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:18:10.988138
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:18:13.402692
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:18:15.817488
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:18:18.231874
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:18:20.650409
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:18:23.066414
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:18:25.484580
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:18:27.903533
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:18:30.320384
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:18:34.883412
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:18:37.299707
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:18:39.716596
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:18:42.130986
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:18:44.543811
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:18:46.958542
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:18:49.375114
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:18:51.792479
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:18:54.207086
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:18:56.622428
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:18:59.036559
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:19:01.450457
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:19:03.864947
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:19:06.280433
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:19:07.853048
# Unit test for function validate_yaml
def test_validate_yaml():from typesystem import String, Integer


# Generated at 2026-10-25 09:19:12.257178
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

# Generated at 2026-10-25 09:19:15.232188
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

# Generated at 2026-10-25 09:19:18.505632
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

# Generated at 2026-10-25 09:19:22.207659
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

# Generated at 2026-10-25 09:19:23.839139
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

# Generated at 2026-10-25 09:19:33.036916
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:19:35.450544
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:19:37.864780
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:19:40.457133
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 09:19:43.098665
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 09:19:45.515570
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 09:19:47.927410
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:19:50.524205
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:19:52.945065
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:19:55.355796
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:19:57.772910
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:20:00.187043
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:20:02.600590
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:20:05.014502
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:20:07.429709
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:20:09.845291
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:20:12.258602
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:20:14.671271
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:20:17.086449
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:20:19.502972
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:20:21.918139
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:20:24.662477
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

# Generated at 2026-10-25 09:20:28.648123
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

# Generated at 2026-10-25 09:20:31.518080
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

# Generated at 2026-10-25 09:20:48.718071
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 09:20:51.132956
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 09:20:53.547708
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 09:20:55.964673
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:20:58.375798
# Unit test for function validate_yaml

# Generated at 2026-10-25 09:21:01.000251
# Unit test for function validate_yaml