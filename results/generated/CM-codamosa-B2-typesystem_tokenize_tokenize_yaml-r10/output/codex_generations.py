

# Generated at 2026-10-24 19:23:22.975228
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:23:25.396359
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:23:27.816429
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:23:30.233314
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:23:32.650435
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:23:35.066302
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:23:37.485149
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:23:39.900054
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:23:42.318578
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:23:44.734790
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:23:47.152740
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:23:49.737275
# Unit test for function tokenize_yaml
def test_tokenize_yaml():token = module_0.tokenize_yaml("name: tom\nage: 30\n")

# Generated at 2026-10-24 19:23:52.404886
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:23:59.923168
# Unit test for function validate_yaml
def test_validate_yaml():from typesystem import Schema, String, Integer

class Person(Schema):
    name = String()
    age = Integer()

# Valid input: returns validated value, no errors
value, errors = module_0.validate_yaml("name: Jane\nage: 30\n", Person)
assert value == {"name": "Jane", "age": 30}
assert errors == []

# Invalid input: value is None, one error with position info
value, errors = module_0.validate_yaml("name: Jane\nage: notanumber\n", Person)
assert value is None
assert len(errors) == 1
assert errors[0].message() == "Must be a number."

# Error position points at the offending scalar value
assert errors[0].start_position.line_no == 2
assert errors[0].start_position.column_no == 6

# Bytes input works the same as str
value, errors = module_0.validate_yaml(b"name: Bob\nage: 42\n", Person)
assert value == {"name": "Bob", "age": 42}
assert errors == []

# Parse error: malformed YAML
value, errors = module_0.validate_yaml("name: [Jane\nage: 30\n", Person)
assert value is None
assert len(errors) == 1
assert errors[0].message() == "expected ',' or ']', but found ''.\n"

# Empty content: explicit no_content parse error
value, errors = module_0.validate_yaml("   \n", Person)
assert value is None
assert len(errors) == 1
assert errors[0].message() == "No content."

# Field validator (not just Schema) is supported
value, errors = module_0.validate_yaml("hello\n", String())
assert value == "hello"
assert errors == []

# Generated at 2026-10-24 19:24:02.575680
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:24:05.325745
# Unit test for function validate_yaml
def test_validate_yaml():from typesystem import Schema, String, Integer

class Person(Schema):
    name = String()
    age = Integer()

# Valid input: returns validated value, no errors
value, errors = module_0.validate_yaml("name: Jane\nage: 30\n", Person)
assert value == {"name": "Jane", "age": 30}
assert errors == []

# Invalid input: value is None, one error with position info
value, errors = module_0.validate_yaml("name: Jane\nage: notanumber\n", Person)
assert value is None
assert len(errors) == 1
assert errors[0].message() == "Must be a number."

# Error position points at the offending scalar value
assert errors[0].start_position.line_no == 2
assert errors[0].start_position.column_no == 6

# Bytes input works the same as str
value, errors = module_0.validate_yaml(b"name: Bob\nage: 42\n", Person)
assert value == {"name": "Bob", "age": 42}
assert errors == []

# Parse error: malformed YAML
value, errors = module_0.validate_yaml("name: [Jane\nage: 30\n", Person)
assert value is None
assert len(errors) == 1
assert errors[0].message() == "expected ',' or ']', but found ''.\n"

# Empty content: explicit no_content parse error
value, errors = module_0.validate_yaml("   \n", Person)
assert value is None
assert len(errors) == 1
assert errors[0].message() == "No content."

# Field validator (not just Schema) is supported
value, errors = module_0.validate_yaml("hello\n", String())
assert value == "hello"
assert errors == []

# Generated at 2026-10-24 19:24:08.106676
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:24:10.865892
# Unit test for function validate_yaml
def test_validate_yaml():from typesystem import Schema, String, Integer

class Person(Schema):
    name = String()
    age = Integer()

# Valid input: returns validated value, no errors
value, errors = module_0.validate_yaml("name: Jane\nage: 30\n", Person)
assert value == {"name": "Jane", "age": 30}
assert errors == []

# Invalid input: value is None, one error with position info
value, errors = module_0.validate_yaml("name: Jane\nage: notanumber\n", Person)
assert value is None
assert len(errors) == 1
assert errors[0].message() == "Must be a number."

# Error position points at the offending scalar value
assert errors[0].start_position.line_no == 2
assert errors[0].start_position.column_no == 6

# Bytes input works the same as str
value, errors = module_0.validate_yaml(b"name: Bob\nage: 42\n", Person)
assert value == {"name": "Bob", "age": 42}
assert errors == []

# Parse error: malformed YAML
value, errors = module_0.validate_yaml("name: [Jane\nage: 30\n", Person)
assert value is None
assert len(errors) == 1
assert errors[0].message() == "expected ',' or ']', but found ''.\n"

# Empty content: explicit no_content parse error
value, errors = module_0.validate_yaml("   \n", Person)
assert value is None
assert len(errors) == 1
assert errors[0].message() == "No content."

# Field validator (not just Schema) is supported
value, errors = module_0.validate_yaml("hello\n", String())
assert value == "hello"
assert errors == []

# Generated at 2026-10-24 19:24:13.555373
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:24:16.082652
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:24:18.599378
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:24:21.018305
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:24:23.438418
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:24:25.862391
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:24:28.301807
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:24:30.884108
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:24:33.299046
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:24:35.715928
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:24:38.304097
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:24:40.724293
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:24:43.143056
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:24:45.560097
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:24:47.975374
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:24:50.391099
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:24:52.805657
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:24:55.223379
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:24:57.644777
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:25:00.125723
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:25:02.477350
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:25:04.895387
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:25:07.313207
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:25:09.731393
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:25:12.149477
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:25:14.568878
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:25:16.984811
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:25:19.403730
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:25:21.824356
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:25:24.239673
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:25:26.659106
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:25:29.074621
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:25:31.497098
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:25:33.913347
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:25:36.327735
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:25:38.748357
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:25:41.167125
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:25:43.923093
# Unit test for function tokenize_yaml
def test_tokenize_yaml():token = module_0.tokenize_yaml("name: tom\nage: 30\n")

# Generated at 2026-10-24 19:25:45.274204
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

# Generated at 2026-10-24 19:25:46.601759
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

# Generated at 2026-10-24 19:25:49.246059
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:25:52.059012
# Unit test for function validate_yaml
def test_validate_yaml():from typesystem import Schema, String, Integer

class Person(Schema):
    name = String()
    age = Integer()

# Valid input: returns validated value, no errors
value, errors = module_0.validate_yaml("name: Jane\nage: 30\n", Person)
assert value == {"name": "Jane", "age": 30}
assert errors == []

# Invalid input: value is None, one error with position info
value, errors = module_0.validate_yaml("name: Jane\nage: notanumber\n", Person)
assert value is None
assert len(errors) == 1
assert errors[0].message() == "Must be a number."

# Error position points at the offending scalar value
assert errors[0].start_position.line_no == 2
assert errors[0].start_position.column_no == 6

# Bytes input works the same as str
value, errors = module_0.validate_yaml(b"name: Bob\nage: 42\n", Person)
assert value == {"name": "Bob", "age": 42}
assert errors == []

# Parse error: malformed YAML
value, errors = module_0.validate_yaml("name: [Jane\nage: 30\n", Person)
assert value is None
assert len(errors) == 1
assert errors[0].message() == "expected ',' or ']', but found ''.\n"

# Empty content: explicit no_content parse error
value, errors = module_0.validate_yaml("   \n", Person)
assert value is None
assert len(errors) == 1
assert errors[0].message() == "No content."

# Field validator (not just Schema) is supported
value, errors = module_0.validate_yaml("hello\n", String())
assert value == "hello"
assert errors == []

# Generated at 2026-10-24 19:25:54.699678
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:25:57.403057
# Unit test for function validate_yaml
def test_validate_yaml():from typesystem import Schema, String, Integer

class Person(Schema):
    name = String()
    age = Integer()

# Valid input: returns validated value, no errors
value, errors = module_0.validate_yaml("name: Jane\nage: 30\n", Person)
assert value == {"name": "Jane", "age": 30}
assert errors == []

# Invalid input: value is None, one error with position info
value, errors = module_0.validate_yaml("name: Jane\nage: notanumber\n", Person)
assert value is None
assert len(errors) == 1
assert errors[0].message() == "Must be a number."

# Error position points at the offending scalar value
assert errors[0].start_position.line_no == 2
assert errors[0].start_position.column_no == 6

# Bytes input works the same as str
value, errors = module_0.validate_yaml(b"name: Bob\nage: 42\n", Person)
assert value == {"name": "Bob", "age": 42}
assert errors == []

# Parse error: malformed YAML
value, errors = module_0.validate_yaml("name: [Jane\nage: 30\n", Person)
assert value is None
assert len(errors) == 1
assert errors[0].message() == "expected ',' or ']', but found ''.\n"

# Empty content: explicit no_content parse error
value, errors = module_0.validate_yaml("   \n", Person)
assert value is None
assert len(errors) == 1
assert errors[0].message() == "No content."

# Field validator (not just Schema) is supported
value, errors = module_0.validate_yaml("hello\n", String())
assert value == "hello"
assert errors == []

# Generated at 2026-10-24 19:25:58.726961
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

# Generated at 2026-10-24 19:26:01.454594
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:26:04.322164
# Unit test for function validate_yaml
def test_validate_yaml():from typesystem import Schema, String, Integer

class Person(Schema):
    name = String()
    age = Integer()

# Valid input: returns validated value, no errors
value, errors = module_0.validate_yaml("name: Jane\nage: 30\n", Person)
assert value == {"name": "Jane", "age": 30}
assert errors == []

# Invalid input: value is None, one error with position info
value, errors = module_0.validate_yaml("name: Jane\nage: notanumber\n", Person)
assert value is None
assert len(errors) == 1
assert errors[0].message() == "Must be a number."

# Error position points at the offending scalar value
assert errors[0].start_position.line_no == 2
assert errors[0].start_position.column_no == 6

# Bytes input works the same as str
value, errors = module_0.validate_yaml(b"name: Bob\nage: 42\n", Person)
assert value == {"name": "Bob", "age": 42}
assert errors == []

# Parse error: malformed YAML
value, errors = module_0.validate_yaml("name: [Jane\nage: 30\n", Person)
assert value is None
assert len(errors) == 1
assert errors[0].message() == "expected ',' or ']', but found ''.\n"

# Empty content: explicit no_content parse error
value, errors = module_0.validate_yaml("   \n", Person)
assert value is None
assert len(errors) == 1
assert errors[0].message() == "No content."

# Field validator (not just Schema) is supported
value, errors = module_0.validate_yaml("hello\n", String())
assert value == "hello"
assert errors == []

# Generated at 2026-10-24 19:26:06.743076
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:26:09.158205
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:26:11.574961
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:26:14.157817
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:26:16.576249
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:26:18.992131
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:26:21.408500
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:26:23.841204
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:26:26.256708
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:26:28.672540
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:26:31.088366
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:26:33.502598
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:26:35.918081
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:26:38.336318
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:26:40.753224
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:26:43.171086
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:26:45.589167
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:26:48.001669
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:26:50.419593
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:26:52.840151
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:26:55.259918
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:26:57.674213
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:27:00.088819
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:27:02.506307
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:27:04.921835
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:27:07.337785
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:27:09.752799
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:27:12.168426
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:27:14.900496
# Unit test for function validate_yaml
def test_validate_yaml():from typesystem import Schema, String, Integer

class Person(Schema):
    name = String()
    age = Integer()

# Valid input: returns validated value, no errors
value, errors = module_0.validate_yaml("name: Jane\nage: 30\n", Person)
assert value == {"name": "Jane", "age": 30}
assert errors == []

# Invalid input: value is None, one error with position info
value, errors = module_0.validate_yaml("name: Jane\nage: notanumber\n", Person)
assert value is None
assert len(errors) == 1
assert errors[0].message() == "Must be a number."

# Error position points at the offending scalar value
assert errors[0].start_position.line_no == 2
assert errors[0].start_position.column_no == 6

# Bytes input works the same as str
value, errors = module_0.validate_yaml(b"name: Bob\nage: 42\n", Person)
assert value == {"name": "Bob", "age": 42}
assert errors == []

# Parse error: malformed YAML
value, errors = module_0.validate_yaml("name: [Jane\nage: 30\n", Person)
assert value is None
assert len(errors) == 1
assert errors[0].message() == "expected ',' or ']', but found ''.\n"

# Empty content: explicit no_content parse error
value, errors = module_0.validate_yaml("   \n", Person)
assert value is None
assert len(errors) == 1
assert errors[0].message() == "No content."

# Field validator (not just Schema) is supported
value, errors = module_0.validate_yaml("hello\n", String())
assert value == "hello"
assert errors == []

# Generated at 2026-10-24 19:27:17.541588
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:27:20.314075
# Unit test for function validate_yaml
def test_validate_yaml():from typesystem import Schema, String, Integer

class Person(Schema):
    name = String()
    age = Integer()

# Valid input: returns validated value, no errors
value, errors = module_0.validate_yaml("name: Jane\nage: 30\n", Person)
assert value == {"name": "Jane", "age": 30}
assert errors == []

# Invalid input: value is None, one error with position info
value, errors = module_0.validate_yaml("name: Jane\nage: notanumber\n", Person)
assert value is None
assert len(errors) == 1
assert errors[0].message() == "Must be a number."

# Error position points at the offending scalar value
assert errors[0].start_position.line_no == 2
assert errors[0].start_position.column_no == 6

# Bytes input works the same as str
value, errors = module_0.validate_yaml(b"name: Bob\nage: 42\n", Person)
assert value == {"name": "Bob", "age": 42}
assert errors == []

# Parse error: malformed YAML
value, errors = module_0.validate_yaml("name: [Jane\nage: 30\n", Person)
assert value is None
assert len(errors) == 1
assert errors[0].message() == "expected ',' or ']', but found ''.\n"

# Empty content: explicit no_content parse error
value, errors = module_0.validate_yaml("   \n", Person)
assert value is None
assert len(errors) == 1
assert errors[0].message() == "No content."

# Field validator (not just Schema) is supported
value, errors = module_0.validate_yaml("hello\n", String())
assert value == "hello"
assert errors == []

# Generated at 2026-10-24 19:27:22.969250
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:27:25.702165
# Unit test for function validate_yaml
def test_validate_yaml():from typesystem import Schema, String, Integer

class Person(Schema):
    name = String()
    age = Integer()

# Valid input: returns validated value, no errors
value, errors = module_0.validate_yaml("name: Jane\nage: 30\n", Person)
assert value == {"name": "Jane", "age": 30}
assert errors == []

# Invalid input: value is None, one error with position info
value, errors = module_0.validate_yaml("name: Jane\nage: notanumber\n", Person)
assert value is None
assert len(errors) == 1
assert errors[0].message() == "Must be a number."

# Error position points at the offending scalar value
assert errors[0].start_position.line_no == 2
assert errors[0].start_position.column_no == 6

# Bytes input works the same as str
value, errors = module_0.validate_yaml(b"name: Bob\nage: 42\n", Person)
assert value == {"name": "Bob", "age": 42}
assert errors == []

# Parse error: malformed YAML
value, errors = module_0.validate_yaml("name: [Jane\nage: 30\n", Person)
assert value is None
assert len(errors) == 1
assert errors[0].message() == "expected ',' or ']', but found ''.\n"

# Empty content: explicit no_content parse error
value, errors = module_0.validate_yaml("   \n", Person)
assert value is None
assert len(errors) == 1
assert errors[0].message() == "No content."

# Field validator (not just Schema) is supported
value, errors = module_0.validate_yaml("hello\n", String())
assert value == "hello"
assert errors == []

# Generated at 2026-10-24 19:27:28.355150
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:27:31.118058
# Unit test for function validate_yaml
def test_validate_yaml():from typesystem import Schema, String, Integer

class Person(Schema):
    name = String()
    age = Integer()

# Valid input: returns validated value, no errors
value, errors = module_0.validate_yaml("name: Jane\nage: 30\n", Person)
assert value == {"name": "Jane", "age": 30}
assert errors == []

# Invalid input: value is None, one error with position info
value, errors = module_0.validate_yaml("name: Jane\nage: notanumber\n", Person)
assert value is None
assert len(errors) == 1
assert errors[0].message() == "Must be a number."

# Error position points at the offending scalar value
assert errors[0].start_position.line_no == 2
assert errors[0].start_position.column_no == 6

# Bytes input works the same as str
value, errors = module_0.validate_yaml(b"name: Bob\nage: 42\n", Person)
assert value == {"name": "Bob", "age": 42}
assert errors == []

# Parse error: malformed YAML
value, errors = module_0.validate_yaml("name: [Jane\nage: 30\n", Person)
assert value is None
assert len(errors) == 1
assert errors[0].message() == "expected ',' or ']', but found ''.\n"

# Empty content: explicit no_content parse error
value, errors = module_0.validate_yaml("   \n", Person)
assert value is None
assert len(errors) == 1
assert errors[0].message() == "No content."

# Field validator (not just Schema) is supported
value, errors = module_0.validate_yaml("hello\n", String())
assert value == "hello"
assert errors == []

# Generated at 2026-10-24 19:27:33.790062
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:27:36.481408
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:27:38.891304
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:27:41.414819
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:27:43.835344
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:27:46.251435
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:27:48.669793
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:27:51.084514
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:27:53.663822
# Unit test for function tokenize_yaml
def test_tokenize_yaml():token = module_0.tokenize_yaml("name: tom\nage: 30\n")

# Generated at 2026-10-24 19:27:56.320924
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:27:59.021239
# Unit test for function validate_yaml
def test_validate_yaml():from typesystem import Schema, String, Integer

class Person(Schema):
    name = String()
    age = Integer()

# Valid input: returns validated value, no errors
value, errors = module_0.validate_yaml("name: Jane\nage: 30\n", Person)
assert value == {"name": "Jane", "age": 30}
assert errors == []

# Invalid input: value is None, one error with position info
value, errors = module_0.validate_yaml("name: Jane\nage: notanumber\n", Person)
assert value is None
assert len(errors) == 1
assert errors[0].message() == "Must be a number."

# Error position points at the offending scalar value
assert errors[0].start_position.line_no == 2
assert errors[0].start_position.column_no == 6

# Bytes input works the same as str
value, errors = module_0.validate_yaml(b"name: Bob\nage: 42\n", Person)
assert value == {"name": "Bob", "age": 42}
assert errors == []

# Parse error: malformed YAML
value, errors = module_0.validate_yaml("name: [Jane\nage: 30\n", Person)
assert value is None
assert len(errors) == 1
assert errors[0].message() == "expected ',' or ']', but found ''.\n"

# Empty content: explicit no_content parse error
value, errors = module_0.validate_yaml("   \n", Person)
assert value is None
assert len(errors) == 1
assert errors[0].message() == "No content."

# Field validator (not just Schema) is supported
value, errors = module_0.validate_yaml("hello\n", String())
assert value == "hello"
assert errors == []

# Generated at 2026-10-24 19:28:01.770837
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:28:06.096911
# Unit test for function validate_yaml
def test_validate_yaml():from typesystem import Schema, String, Integer

class Person(Schema):
    name = String()
    age = Integer()

# Valid input: returns validated value, no errors
value, errors = module_0.validate_yaml("name: Jane\nage: 30\n", Person)
assert value == {"name": "Jane", "age": 30}
assert errors == []

# Invalid input: value is None, one error with position info
value, errors = module_0.validate_yaml("name: Jane\nage: notanumber\n", Person)
assert value is None
assert len(errors) == 1
assert errors[0].message() == "Must be a number."

# Error position points at the offending scalar value
assert errors[0].start_position.line_no == 2
assert errors[0].start_position.column_no == 6

# Bytes input works the same as str
value, errors = module_0.validate_yaml(b"name: Bob\nage: 42\n", Person)
assert value == {"name": "Bob", "age": 42}
assert errors == []

# Parse error: malformed YAML
value, errors = module_0.validate_yaml("name: [Jane\nage: 30\n", Person)
assert value is None
assert len(errors) == 1
assert errors[0].message() == "expected ',' or ']', but found ''.\n"

# Empty content: explicit no_content parse error
value, errors = module_0.validate_yaml("   \n", Person)
assert value is None
assert len(errors) == 1
assert errors[0].message() == "No content."

# Field validator (not just Schema) is supported
value, errors = module_0.validate_yaml("hello\n", String())
assert value == "hello"
assert errors == []

# Generated at 2026-10-24 19:28:07.524848
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

# Generated at 2026-10-24 19:28:10.183438
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:28:12.858792
# Unit test for function validate_yaml
def test_validate_yaml():from typesystem import Schema, String, Integer

class Person(Schema):
    name = String()
    age = Integer()

# Valid input: returns validated value, no errors
value, errors = module_0.validate_yaml("name: Jane\nage: 30\n", Person)
assert value == {"name": "Jane", "age": 30}
assert errors == []

# Invalid input: value is None, one error with position info
value, errors = module_0.validate_yaml("name: Jane\nage: notanumber\n", Person)
assert value is None
assert len(errors) == 1
assert errors[0].message() == "Must be a number."

# Error position points at the offending scalar value
assert errors[0].start_position.line_no == 2
assert errors[0].start_position.column_no == 6

# Bytes input works the same as str
value, errors = module_0.validate_yaml(b"name: Bob\nage: 42\n", Person)
assert value == {"name": "Bob", "age": 42}
assert errors == []

# Parse error: malformed YAML
value, errors = module_0.validate_yaml("name: [Jane\nage: 30\n", Person)
assert value is None
assert len(errors) == 1
assert errors[0].message() == "expected ',' or ']', but found ''.\n"

# Empty content: explicit no_content parse error
value, errors = module_0.validate_yaml("   \n", Person)
assert value is None
assert len(errors) == 1
assert errors[0].message() == "No content."

# Field validator (not just Schema) is supported
value, errors = module_0.validate_yaml("hello\n", String())
assert value == "hello"
assert errors == []

# Generated at 2026-10-24 19:28:15.390927
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:28:17.806635
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:28:20.347676
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:28:22.766395
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:28:25.185862
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:28:27.700189
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:28:30.117999
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:28:32.538251
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:28:34.958034
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:28:37.380104
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:28:39.808788
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:28:42.370785
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:28:44.790179
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:28:47.209059
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:28:49.621591
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:28:52.040408
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:28:54.456789
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:28:56.874529
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:28:59.290110
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:29:01.707648
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:29:04.123863
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:29:06.537669
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:29:08.962953
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:29:11.380221
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:29:13.798904
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:29:16.215260
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:29:18.631581
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:29:21.046832
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:29:23.464360
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:29:25.880888
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:29:28.295672
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:29:30.715055
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:29:33.135551
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:29:35.553122
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:29:37.969234
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:29:40.384832
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:29:42.802142
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:29:45.217689
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:29:47.637718
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:29:50.055023
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:29:52.470768
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:29:54.888476
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:29:57.304043
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:29:59.719392
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:30:02.135420
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:30:04.554657
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:30:06.967715
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:30:09.384422
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:30:11.800671
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:30:14.216592
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:30:16.634456
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:30:19.052349
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:30:21.470975
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:30:23.885611
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:30:26.303197
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:30:28.723595
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:30:31.139855
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:30:35.402467
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:30:37.815613
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:30:40.230231
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:30:42.645057
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:30:45.062361
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:30:47.476645
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:30:49.895725
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:30:52.314309
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:30:54.737525
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:30:57.154588
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:30:59.566637
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:31:01.983369
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:31:04.401818
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:31:06.819554
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:31:09.237768
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:31:11.652925
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:31:14.070139
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:31:16.484854
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:31:18.901598
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:31:21.315546
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:31:23.756654
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:31:26.150974
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:31:28.566773
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:31:30.982286
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:31:33.398644
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:31:35.818529
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:31:38.235934
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:31:40.655919
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:31:43.072542
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:31:45.485720
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:31:49.078859
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:31:51.497293
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:31:53.915716
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:31:56.332872
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:31:58.752469
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:32:01.168533
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:32:03.586007
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:32:06.027689
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:32:08.421057
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:32:10.839772
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:32:13.257735
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:32:15.672957
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:32:18.093684
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:32:20.511638
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:32:22.928477
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:32:25.344830
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:32:27.768865
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:32:30.183860
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:32:32.598894
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:32:35.018020
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:32:37.435498
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:32:39.849010
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:32:42.267807
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:32:44.684024
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 19:32:47.100769
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:32:49.517096
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:32:51.932180
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:32:54.357507
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:32:56.773486
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:32:59.567896
# Unit test for function validate_yaml
def test_validate_yaml():from typesystem import Schema, String, Integer

class Person(Schema):
    name = String()
    age = Integer()

# Valid input: returns validated value, no errors
value, errors = module_0.validate_yaml("name: Jane\nage: 30\n", Person)
assert value == {"name": "Jane", "age": 30}
assert errors == []

# Invalid input: value is None, one error with position info
value, errors = module_0.validate_yaml("name: Jane\nage: notanumber\n", Person)
assert value is None
assert len(errors) == 1
assert errors[0].message() == "Must be a number."

# Error position points at the offending scalar value
assert errors[0].start_position.line_no == 2
assert errors[0].start_position.column_no == 6

# Bytes input works the same as str
value, errors = module_0.validate_yaml(b"name: Bob\nage: 42\n", Person)
assert value == {"name": "Bob", "age": 42}
assert errors == []

# Parse error: malformed YAML
value, errors = module_0.validate_yaml("name: [Jane\nage: 30\n", Person)
assert value is None
assert len(errors) == 1
assert errors[0].message() == "expected ',' or ']', but found ''.\n"

# Empty content: explicit no_content parse error
value, errors = module_0.validate_yaml("   \n", Person)
assert value is None
assert len(errors) == 1
assert errors[0].message() == "No content."

# Field validator (not just Schema) is supported
value, errors = module_0.validate_yaml("hello\n", String())
assert value == "hello"
assert errors == []

# Generated at 2026-10-24 19:33:03.869488
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:33:06.735330
# Unit test for function validate_yaml
def test_validate_yaml():from typesystem import Schema, String, Integer

class Person(Schema):
    name = String()
    age = Integer()

# Valid input: returns validated value, no errors
value, errors = module_0.validate_yaml("name: Jane\nage: 30\n", Person)
assert value == {"name": "Jane", "age": 30}
assert errors == []

# Invalid input: value is None, one error with position info
value, errors = module_0.validate_yaml("name: Jane\nage: notanumber\n", Person)
assert value is None
assert len(errors) == 1
assert errors[0].message() == "Must be a number."

# Error position points at the offending scalar value
assert errors[0].start_position.line_no == 2
assert errors[0].start_position.column_no == 6

# Bytes input works the same as str
value, errors = module_0.validate_yaml(b"name: Bob\nage: 42\n", Person)
assert value == {"name": "Bob", "age": 42}
assert errors == []

# Parse error: malformed YAML
value, errors = module_0.validate_yaml("name: [Jane\nage: 30\n", Person)
assert value is None
assert len(errors) == 1
assert errors[0].message() == "expected ',' or ']', but found ''.\n"

# Empty content: explicit no_content parse error
value, errors = module_0.validate_yaml("   \n", Person)
assert value is None
assert len(errors) == 1
assert errors[0].message() == "No content."

# Field validator (not just Schema) is supported
value, errors = module_0.validate_yaml("hello\n", String())
assert value == "hello"
assert errors == []

# Generated at 2026-10-24 19:33:09.397016
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:33:12.155760
# Unit test for function validate_yaml
def test_validate_yaml():from typesystem import Schema, String, Integer

class Person(Schema):
    name = String()
    age = Integer()

# Valid input: returns validated value, no errors
value, errors = module_0.validate_yaml("name: Jane\nage: 30\n", Person)
assert value == {"name": "Jane", "age": 30}
assert errors == []

# Invalid input: value is None, one error with position info
value, errors = module_0.validate_yaml("name: Jane\nage: notanumber\n", Person)
assert value is None
assert len(errors) == 1
assert errors[0].message() == "Must be a number."

# Error position points at the offending scalar value
assert errors[0].start_position.line_no == 2
assert errors[0].start_position.column_no == 6

# Bytes input works the same as str
value, errors = module_0.validate_yaml(b"name: Bob\nage: 42\n", Person)
assert value == {"name": "Bob", "age": 42}
assert errors == []

# Parse error: malformed YAML
value, errors = module_0.validate_yaml("name: [Jane\nage: 30\n", Person)
assert value is None
assert len(errors) == 1
assert errors[0].message() == "expected ',' or ']', but found ''.\n"

# Empty content: explicit no_content parse error
value, errors = module_0.validate_yaml("   \n", Person)
assert value is None
assert len(errors) == 1
assert errors[0].message() == "No content."

# Field validator (not just Schema) is supported
value, errors = module_0.validate_yaml("hello\n", String())
assert value == "hello"
assert errors == []

# Generated at 2026-10-24 19:33:14.803486
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:33:17.493549
# Unit test for function validate_yaml
def test_validate_yaml():from typesystem import Schema, String, Integer

class Person(Schema):
    name = String()
    age = Integer()

# Valid input: returns validated value, no errors
value, errors = module_0.validate_yaml("name: Jane\nage: 30\n", Person)
assert value == {"name": "Jane", "age": 30}
assert errors == []

# Invalid input: value is None, one error with position info
value, errors = module_0.validate_yaml("name: Jane\nage: notanumber\n", Person)
assert value is None
assert len(errors) == 1
assert errors[0].message() == "Must be a number."

# Error position points at the offending scalar value
assert errors[0].start_position.line_no == 2
assert errors[0].start_position.column_no == 6

# Bytes input works the same as str
value, errors = module_0.validate_yaml(b"name: Bob\nage: 42\n", Person)
assert value == {"name": "Bob", "age": 42}
assert errors == []

# Parse error: malformed YAML
value, errors = module_0.validate_yaml("name: [Jane\nage: 30\n", Person)
assert value is None
assert len(errors) == 1
assert errors[0].message() == "expected ',' or ']', but found ''.\n"

# Empty content: explicit no_content parse error
value, errors = module_0.validate_yaml("   \n", Person)
assert value is None
assert len(errors) == 1
assert errors[0].message() == "No content."

# Field validator (not just Schema) is supported
value, errors = module_0.validate_yaml("hello\n", String())
assert value == "hello"
assert errors == []

# Generated at 2026-10-24 19:33:20.009838
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:33:22.426460
# Unit test for function validate_yaml

# Generated at 2026-10-24 19:33:24.847794
# Unit test for function validate_yaml