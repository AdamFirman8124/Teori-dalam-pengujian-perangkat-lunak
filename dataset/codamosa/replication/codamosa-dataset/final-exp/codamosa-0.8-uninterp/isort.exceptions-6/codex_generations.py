

# Generated at 2022-06-13 23:00:27.469978
# Unit test for constructor of class LiteralParsingFailure
def test_LiteralParsingFailure():
    try:
        raise LiteralParsingFailure("add", "")
    except Exception as e:
        assert str(e) == (
            "isort failed to parse the given literal add. "
            "It's important to note that isort literal sorting only supports "
            "simple literals parsable by ast.literal_eval which gave the "
            "exception of ."
        )

# Generated at 2022-06-13 23:00:29.977252
# Unit test for constructor of class InvalidSettingsPath
def test_InvalidSettingsPath():
    InvalidSettingsPath(settings_path="test_InvalidSettingsPath")

# Generated at 2022-06-13 23:00:33.620039
# Unit test for constructor of class UnsupportedSettings
def test_UnsupportedSettings():
    errors = {
        "one": {"value": 1, "source": "unit test"},
        "two": {"value": True, "source": "unit test"},
    }
    ex = UnsupportedSettings(errors)
    assert ex.unsupported_settings == errors
    assert "one" in str(ex)
    assert "two" in str(ex)

# Generated at 2022-06-13 23:00:35.342406
# Unit test for constructor of class FileSkipped
def test_FileSkipped():
    with pytest.raises(FileSkipped, match = r".* does not exist."):
        raise FileSkipped('Invalid path', 'Invalid path')

# Generated at 2022-06-13 23:00:38.217203
# Unit test for constructor of class UnsupportedSettings
def test_UnsupportedSettings():
    test_dict = {'option1': {'value': 0, 'source': 'test'}}
    test_UnsupportedSettings = UnsupportedSettings(test_dict)
    assert test_UnsupportedSettings.unsupported_settings == test_dict

# Generated at 2022-06-13 23:00:48.344999
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    try:
        raise LiteralSortTypeMismatch(int, str)
    except LiteralSortTypeMismatch as e:
        assert e.kind == int
        assert e.expected_kind == str
        assert e.args == (
            "isort was told to sort a literal of type <class 'str'> but was given "
            "a literal of type <class 'int'>.",)


# Generated at 2022-06-13 23:00:56.427443
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():
    try:
        raise ProfileDoesNotExist('some_profile')
    except ProfileDoesNotExist as e:
        assert e.profile == 'some_profile'
        assert str(e) == "Specified profile of some_profile does not exist. Available profiles: black,pep8,google,pycharm,jupyterlab,jupyter_full,jedi,pycharm_full,ipython_full,mypy,pycharm_django,flake8,atom,spyder,vscode,vim,sublime,intellij_full,unreal,vscode_full,yapf."

# Generated at 2022-06-13 23:00:57.784930
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    s = LiteralSortTypeMismatch
    assert isinstance(s, object) == True

# Generated at 2022-06-13 23:01:00.681174
# Unit test for constructor of class InvalidSettingsPath
def test_InvalidSettingsPath():
    try:
        raise InvalidSettingsPath("/settings_path")
    except InvalidSettingsPath as e:
        assert e.settings_path == "/settings_path"


# Generated at 2022-06-13 23:01:24.068263
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    LiteralSortTypeMismatch(type(""), type(""))
    LiteralSortTypeMismatch(str, int)
    LiteralSortTypeMismatch(str, list)
    LiteralSortTypeMismatch(bool, str)
    LiteralSortTypeMismatch(dict, list)
