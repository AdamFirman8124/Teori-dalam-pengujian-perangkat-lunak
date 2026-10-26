

# Generated at 2026-10-25 12:27:05.333334
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:27:44.434851
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:28:46.300828
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:28:49.372792
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:28:54.389873
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:29:24.700565
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:29:30.212746
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:29:33.715997
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:29:36.685205
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:30:33.733570
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:31:11.504107
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:31:38.539974
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:31:44.376963
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:32:32.724465
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:32:38.032772
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:32:43.767725
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:33:00.152282
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:33:33.229668
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:33:36.404065
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:33:54.628609
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:33:57.047878
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:33:59.464596
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:34:01.874822
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:34:04.288740
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:34:06.702514
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:34:09.116010
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:34:11.531222
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:34:13.947098
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:34:16.360182
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:34:26.574160
# Unit test for function tokenize_yaml
def test_tokenize_yaml():token = module_0.tokenize_yaml("name: alice\nage: 30\n")

# Generated at 2026-10-25 12:34:31.761364
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:34:48.699724
# Unit test for function validate_yaml
def test_validate_yaml():from typesystem import String, Integer


# Generated at 2026-10-25 12:34:51.112637
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:34:53.525571
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:34:55.973266
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:34:58.364889
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:35:00.777728
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:35:03.380253
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:35:05.794925
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:35:08.210739
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:35:10.623751
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:35:13.038175
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:35:15.453356
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:35:17.866790
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:35:20.278940
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:35:22.692161
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:35:25.109861
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:35:27.517879
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:35:29.932488
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:35:32.344036
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:35:35.014240
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:35:36.527233
# Unit test for function validate_yaml
def test_validate_yaml():from typesystem import String, Integer


# Generated at 2026-10-25 12:35:39.519710
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

# Generated at 2026-10-25 12:35:42.560834
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

# Generated at 2026-10-25 12:35:43.935139
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

# Generated at 2026-10-25 12:35:45.446120
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

# Generated at 2026-10-25 12:35:55.158692
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

# Generated at 2026-10-25 12:35:58.187551
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:36:00.792017
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:36:03.209634
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:36:05.889350
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:36:08.303497
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:36:10.745024
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:36:13.372915
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:36:15.786681
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:36:18.201340
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:36:20.615190
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:36:23.028499
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:36:25.441088
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:36:27.854022
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:36:30.266547
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:36:33.115336
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:36:35.527975
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:36:37.947003
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:36:40.357094
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:36:42.769831
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:36:45.182993
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:36:47.598088
# Unit test for function validate_yaml