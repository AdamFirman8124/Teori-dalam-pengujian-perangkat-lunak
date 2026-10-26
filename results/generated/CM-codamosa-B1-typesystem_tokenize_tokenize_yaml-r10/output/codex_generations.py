

# Generated at 2026-10-25 11:48:48.798428
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

# Generated at 2026-10-25 11:48:51.994732
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

# Generated at 2026-10-25 11:48:55.431948
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

# Generated at 2026-10-25 11:48:56.927893
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

# Generated at 2026-10-25 11:48:58.366663
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

# Generated at 2026-10-25 11:49:01.066118
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 11:49:03.481278
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 11:49:05.895391
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 11:49:08.558000
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:49:10.977932
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:49:13.391826
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:49:15.804852
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 11:49:18.220906
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 11:49:20.640102
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 11:49:23.053239
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 11:49:25.468239
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 11:49:27.880406
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 11:49:30.296779
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 11:49:32.711001
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 11:49:35.125866
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 11:49:37.798522
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:49:40.212148
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:49:42.624731
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:49:45.730114
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

# Generated at 2026-10-25 11:49:47.366714
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

# Generated at 2026-10-25 11:50:08.566234
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

# Generated at 2026-10-25 11:50:10.507728
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

# Generated at 2026-10-25 11:50:11.944191
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

# Generated at 2026-10-25 11:50:13.581849
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

# Generated at 2026-10-25 11:50:15.053214
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

# Generated at 2026-10-25 11:50:41.516750
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:50:43.932050
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:50:46.346853
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:50:48.760821
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:50:50.241178
# Unit test for function validate_yaml
def test_validate_yaml():from typesystem import String, Integer


# Generated at 2026-10-25 11:51:12.666902
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

# Generated at 2026-10-25 11:51:14.186090
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

# Generated at 2026-10-25 11:51:16.030006
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

# Generated at 2026-10-25 11:51:20.231520
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

# Generated at 2026-10-25 11:51:23.315608
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

# Generated at 2026-10-25 11:51:24.851654
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

# Generated at 2026-10-25 11:51:27.741996
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:51:30.383123
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:51:32.799456
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:51:35.213932
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 11:51:37.628673
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 11:51:40.336229
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 11:51:42.752440
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:51:45.167309
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:51:47.613297
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:51:50.333463
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 11:51:52.749233
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 11:51:55.166481
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 11:51:57.771579
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 11:52:10.229817
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    content = "name: foo\nvalue: 42\n"
    token = module_0.tokenize_yaml(content)

    assert isinstance(token, DictToken)
    assert token.start_index == 0
    assert token.end_index == len(content) - 1

    key = list(token.keys())[0]
    assert isinstance(key, ScalarToken)
    assert key.value == "name"
    assert key.start_index == 0
    assert key.end_index == len("name") - 1

    value = token[key]
    assert isinstance(value, ScalarToken)
    assert value.value == "foo"

    second_key = list(token.keys())[1]
    second_value = token[second_key]
    assert second_value.value == 42
    assert isinstance(second_value.value, int)

    list_content = "items:\n  - 1\n  - 2\n"
    list_token = module_0.tokenize_yaml(list_content)
    assert isinstance(list_token, DictToken)
    items = list_token[list_key := list(list_token.keys())[0]]
    assert isinstance(items, ListToken)
    assert [item.value for item in items] == [1, 2]

# Generated at 2026-10-25 11:52:13.414102
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

# Generated at 2026-10-25 11:52:17.387655
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

# Generated at 2026-10-25 11:52:19.024697
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

# Generated at 2026-10-25 11:52:22.227738
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

# Generated at 2026-10-25 11:52:25.045593
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 11:52:27.490669
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 11:52:29.879271
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 11:52:32.289853
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:52:34.927658
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:52:37.341842
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:52:39.756699
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:52:42.170738
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:52:44.628339
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:52:47.016719
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 11:52:49.430198
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 11:52:51.844717
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 11:52:54.259102
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 11:52:56.672589
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 11:52:59.086923
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 11:53:01.503913
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:53:03.916474
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:53:06.331904
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:53:08.746829
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:53:11.161455
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:53:13.577893
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:53:15.990257
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:53:18.404660
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:53:20.819842
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:53:23.744232
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

# Generated at 2026-10-25 11:53:32.062304
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

# Generated at 2026-10-25 11:53:33.438314
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

# Generated at 2026-10-25 11:53:36.943372
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

# Generated at 2026-10-25 11:53:54.748942
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:53:57.168707
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:53:59.579836
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:54:01.995977
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:54:04.438415
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:54:07.046852
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:54:09.464494
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:54:11.884686
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:54:14.530667
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:54:16.940159
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:54:19.354680
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:54:21.831106
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:54:24.209443
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:54:26.625158
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:54:29.038400
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:54:31.454287
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:54:33.869522
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:54:36.281795
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:54:38.695091
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:54:41.111423
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:54:43.526406
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:54:45.939987
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 11:54:48.353058
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 11:54:50.772332
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 11:54:53.188881
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 11:54:55.603279
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 11:54:58.015623
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 11:55:00.430898
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 11:55:02.844502
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 11:55:05.257469
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 11:55:07.671744
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:55:10.085400
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:55:12.500738
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:55:14.913665
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:55:17.327309
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:55:19.740890
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:55:22.153207
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:55:24.565915
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:55:26.979290
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:55:29.394568
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:55:31.810599
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:55:34.225365
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:55:36.640016
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:55:39.054571
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:55:41.468522
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:55:43.882884
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:55:46.298005
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:55:48.711246
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:55:51.126583
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:55:53.542339
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:55:55.956670
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:55:58.370091
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:56:00.784460
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:56:03.200691
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:56:05.614021
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:56:08.028665
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:56:10.443518
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:56:12.858407
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 11:56:15.272065
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 11:56:17.688754
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 11:56:20.099910
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 11:56:22.513608
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 11:56:24.927051
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 11:56:27.340851
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:56:29.755319
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:56:32.170114
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:56:34.585767
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:56:36.999967
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:56:39.415946
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:56:41.830027
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:56:44.242996
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:56:46.659255
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:56:49.077176
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:56:51.488325
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:56:53.901974
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:56:56.316981
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:56:58.729039
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:57:01.142443
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:57:03.556641
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:57:05.971260
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:57:08.387046
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:57:10.801563
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 11:57:13.215900
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 11:57:15.628123
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 11:57:18.379046
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:57:20.791204
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:57:23.259373
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:57:25.659912
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:57:28.107023
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:57:30.489206
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:57:32.902145
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:57:35.316513
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:57:37.730236
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:57:40.147981
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:57:42.561446
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:57:44.975075
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:57:47.388984
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:57:49.804288
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:57:52.218110
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:57:54.632919
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:57:57.047987
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:57:59.493040
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:58:01.879371
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:58:04.291937
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:58:06.705529
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:58:09.121872
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:58:11.536125
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:58:13.949980
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:58:16.363673
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 11:58:18.779324
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 11:58:21.194639
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 11:58:23.606723
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:58:26.022922
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:58:28.436455
# Unit test for function validate_yaml

# Generated at 2026-10-25 11:58:49.569146
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