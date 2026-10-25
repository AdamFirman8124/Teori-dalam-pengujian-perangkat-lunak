

# Generated at 2026-10-24 14:15:02.991287
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 14:15:05.408517
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 14:15:08.089162
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 14:15:10.504603
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 14:15:12.919255
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 14:15:15.338421
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 14:15:17.759090
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:15:20.178143
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:15:22.596918
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:15:42.441397
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:16:20.684856
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:16:23.101564
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:16:25.516121
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:16:28.369361
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:16:31.518491
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:16:49.442552
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 14:17:08.714138
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 14:17:11.125045
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 14:17:13.537791
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 14:17:16.110379
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 14:17:18.524095
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 14:17:20.938303
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:17:23.486825
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:17:25.910115
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:17:28.337244
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:17:30.748564
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:17:33.162501
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:17:35.585906
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:17:37.992233
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:17:40.404191
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:17:42.816339
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 14:17:45.232156
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 14:17:47.648276
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 14:17:50.065209
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:17:52.481682
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:17:54.902790
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:17:57.318817
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 14:17:59.743583
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 14:18:02.159604
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 14:18:04.581563
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 14:18:07.000612
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 14:18:09.424617
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 14:18:11.839707
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 14:18:14.251552
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 14:18:16.665238
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 14:18:19.077886
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:18:21.490151
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:18:23.911267
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:18:26.325498
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:18:29.239105
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:18:32.063971
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:18:43.843402
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

# Generated at 2026-10-24 14:18:45.176038
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

# Generated at 2026-10-24 14:18:46.569352
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

# Generated at 2026-10-24 14:19:06.004469
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:19:08.419880
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:19:11.003518
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:19:13.420396
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:19:16.047796
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:19:18.453365
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:19:20.870149
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:19:23.286710
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:19:25.702233
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:19:28.114358
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:19:30.529462
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:19:32.940960
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:19:35.353862
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 14:19:37.781734
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 14:20:10.270826
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 14:20:11.899930
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

# Generated at 2026-10-24 14:20:13.218706
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

# Generated at 2026-10-24 14:20:14.592487
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

# Generated at 2026-10-24 14:20:17.436626
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:20:19.965684
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:20:22.384481
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:20:24.927754
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:20:27.347852
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:20:29.761706
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:20:32.180897
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 14:20:34.594575
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 14:20:37.009352
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 14:20:39.423631
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:20:42.421915
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:20:45.289399
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:20:46.619387
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

# Generated at 2026-10-24 14:20:47.930854
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

# Generated at 2026-10-24 14:20:50.597780
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:20:53.510989
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:20:56.081526
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:20:58.497203
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 14:21:00.908954
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 14:21:03.323405
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 14:21:05.735377
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:21:08.148661
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:21:10.561702
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:21:13.175866
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:21:15.593796
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:21:18.007812
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:21:20.420408
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:21:22.836350
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:21:25.250029
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:21:27.664234
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:21:30.084731
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:21:32.499033
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:21:34.912573
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:21:37.344289
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:21:39.761362
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:21:42.179370
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:21:44.590724
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:21:47.005181
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:21:49.419565
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:21:51.835475
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:21:54.277919
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:21:56.717042
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 14:21:59.133887
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 14:22:01.548116
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 14:22:03.962544
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 14:22:06.389505
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 14:22:08.805280
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 14:22:11.222224
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:22:13.636556
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:22:16.051796
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:22:18.468402
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:22:20.883550
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:22:23.299448
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:22:25.713704
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:22:28.128191
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:22:30.966561
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:22:32.505355
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

# Generated at 2026-10-24 14:22:35.160582
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:22:38.030906
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:22:40.898487
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:22:43.765996
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:22:46.531626
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:22:49.398632
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:22:52.270412
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:22:55.171464
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:22:57.681889
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:23:00.096365
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 14:23:02.515391
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 14:23:05.169753
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 14:23:07.585779
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:23:10.148918
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:23:12.567543
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:23:14.980541
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:23:17.394444
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:23:19.808414
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:23:22.243133
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:23:24.659149
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:23:27.080018
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:23:29.494635
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 14:23:31.908984
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 14:23:34.328066
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 14:23:36.741838
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:23:39.544999
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:23:42.327854
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:24:00.366196
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:24:02.964350
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:24:05.376045
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:24:07.973226
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:24:10.498007
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:24:12.914026
# Unit test for function validate_yaml

# Generated at 2026-10-24 14:24:15.329590
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 14:24:17.745171
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 14:24:20.159440
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 14:24:22.573371
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 14:24:25.188116
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 14:24:27.601911
# Unit test for function tokenize_yaml