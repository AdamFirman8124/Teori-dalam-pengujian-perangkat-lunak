

# Generated at 2022-06-14 08:08:26.294047
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from os import environ
    from tempfile import NamedTemporaryFile

    with NamedTemporaryFile(mode="w", delete=False, suffix=".py") as f:
        f.write(
            '"""This temporary test file should be deleted after test is done."""\n'
        )
        f.write("TEST_VAR_FROM_MODULE_1 = 1\n")

    environ["TEST_ENVIRONMENT_VARIABLE"] = "should_be_env_variable"


# Generated at 2022-06-14 08:08:39.240935
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from test import test_module_for_config_loader

    test_module = load_module_from_file_location(
        "test.test_module_for_config_loader"
    )

    assert test_module.thing == test_module_for_config_loader.thing

    test_module = load_module_from_file_location(
        Path(__file__).parent.joinpath("test_module_for_config_loader.py")
    )

    assert test_module.thing == test_module_for_config_loader.thing

    # Test when we pass absolute path.
    test_module = load_module_from_file_location(
        Path(__file__).parent.parent.joinpath("test_module_for_config_loader.py")
    )

    assert test_module.thing == test_module

# Generated at 2022-06-14 08:08:47.103736
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    # Test case 1: Should load file with ";" in file name.
    assert load_module_from_file_location("sanic/examples/test;;;.py").test == ";test;"

    # Test case 2: Should load file with "${some_env_var}" in file name.
    os_environ["foo"] = "examples"
    assert load_module_from_file_location("sanic/${foo}/test.py").test == "test"
    del os_environ["foo"]

    # Test case 3: Should load file with "${some_env_var}" which is not in os_environ.
    # Note: In this case we don't use os.path.join because it converts ";" to ":" in Unix.

# Generated at 2022-06-14 08:08:53.497071
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    os_environ["TEST_ENV_VAR"] = "test_env_value"
    module = load_module_from_file_location(
        "test_module_name",
        "/some/path/${TEST_ENV_VAR}",
        submodule_search_locations="test_module_name.test_submodule_search_locations",
    )
    assert (
        module.CONFIG_VALUE
        == "test_module_name.test_submodule_search_locations"
    )
    assert module.__name__ == "test_module_name"
    assert module.__file__ == "/some/path/test_env_value"
    assert module.TEST_CONSTANT == "test_module_name"
    assert hasattr(module, "__package__") is False


# Generated at 2022-06-14 08:09:05.842248
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # Test if function throw error if environment variable is not defined.
    try:
        load_module_from_file_location("some_module_name", "/some/path/${some_env_var}")  # noqa
    except LoadFileException:
        pass
    else:
        raise AssertionError("Function didn't raise LoadFileException")

    # Test if function finds environment variable in location.
    os_environ["some_env_var"] = "some_value"
    assert "some_value" in load_module_from_file_location(
        "some_module_name", "/some/path/${some_env_var}"
    ).__file__

    # Test if function finds environment variable in location.
    os_environ["some_env_var"] = "some_value"
    assert "some_value"

# Generated at 2022-06-14 08:09:11.501617
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # Test with Path
    module_content = "test_value = 42"
    with TemporaryDirectory() as _temp_dir:
        location = "temp_file.py"
        temp_file_path = Path(_temp_dir, location)
        with open(temp_file_path, "w") as temp_file:
            temp_file.write(module_content)
        module = load_module_from_file_location(temp_file_path)
    assert module.test_value == 42

    # Test with bytes
    location = bytes("/some/test/file/location.py", "utf8")

# Generated at 2022-06-14 08:09:23.576262
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # pylint: disable=R0914
    """Test load module from file location.

    This function tests all possible way to load file from file location
    as well with or without environment variables.
    """

    # A) Test loading python file without enviroment variables
    # B) Test loading python file with enviroment variables
    # C) Test loading python file with undefined environment variables
    # D) Test loading python file with ${some_env_var} in path
    # E) Test loading python file with ${some_env_var} in path and env vars
    # F) Test loading python file with ${some_env_var} in path and not defined
    #    env vars
    # G) Test loading also files without .py extension
    # H) Test loading file with .py extension but without .py extension
    #    in file location arg

# Generated at 2022-06-14 08:09:33.078317
# Unit test for function str_to_bool
def test_str_to_bool():
    from datadog import api

    assert str_to_bool("true") == True
    assert str_to_bool("false") == False
    assert str_to_bool("TRUE") == True
    assert str_to_bool("FALSE") == False
    assert str_to_bool("True") == True
    assert str_to_bool("False") == False
    assert str_to_bool("trUe") == True
    assert str_to_bool("fAlSe") == False
    assert str_to_bool("1") == True
    assert str_to_bool("0") == False
    assert str_to_bool("on") == True
    assert str_to_bool("off") == False
    assert str_to_bool("ON") == True
    assert str_to_bool("OFF") == False
    assert str

# Generated at 2022-06-14 08:09:42.070938
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from io import StringIO
    from pathlib import Path

    # Create test config in string
    file_string = """
default_val = "some"
str_var = "some_str"
int_var = 10
float_var = 10.5
bool_var = True
list_var = ["list", "of", "strings"]
tuple_var = ("tuple", "of", "strings")
dict_var = {"name": "value"}
nested_var = {
    "some": "other",
    "some2": "other2",
    "some3": {
        "some": "other"
    }
}
"""

    # Create test config file
    with open("test.py", "w") as f:
        f.write(file_string)

    # Try to load
    module = load_module

# Generated at 2022-06-14 08:09:53.189186
# Unit test for function str_to_bool
def test_str_to_bool():
    assert str_to_bool("true")
    assert str_to_bool("True")
    assert str_to_bool("YES")
    assert str_to_bool("1")
    assert str_to_bool("on")
    assert str_to_bool("On")
    assert str_to_bool("yepp")
    assert str_to_bool("yep")

    assert not str_to_bool("false")
    assert not str_to_bool("False")
    assert not str_to_bool("NO")
    assert not str_to_bool("0")
    assert not str_to_bool("off")
    assert not str_to_bool("Off")
    assert not str_to_bool("nope")
    assert not str_to_bool("nop")


# Generated at 2022-06-14 08:10:08.338253
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # os.path.isfile could be used instead of os.path.exists for more strict
    # check, but it's a test function and i don't want to create this file
    # just for the test.
    assert not load_module_from_file_location(
        "/some/random/nonexistent/path/to/some_file.py"
    )
    assert load_module_from_file_location(
        "unittest_tools", Path(__file__).parent
    )
    assert load_module_from_file_location(
        "unittest_tools", Path(__file__).parent / "unittest_tools.py"
    )


# Generated at 2022-06-14 08:10:20.744643
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Test for function load_module_from_file_location.

    For proper functioning of this test,
    there should exist file location.py in the same directory with .env file.
    For example location.py should have:
        # In location.py
        app_name = "location.py"
    And should exist location.env that
    should contain environment variable "DEV_ENV_VAR"
    and BUILD_ENV_VAR:
        # In location.env
        DEV_ENV_VAR = "correct"
        BUILD_ENV_VAR = "/tmp/correct"
    """

    # For this test, we need to put location.py
    # in the same directory as location.env
    location_file = Path().absolute().parent.joinpath("location.py")
    location_file_path = str

# Generated at 2022-06-14 08:10:29.395896
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """
    This function tests load_module_from_file_location.
    """
    from tempfile import NamedTemporaryFile

    # A) Test with a string location
    with NamedTemporaryFile(mode="w", suffix=".py") as temp_file:
        temp_file.write("var1 = 'foo'")
        temp_file.flush()
        module = load_module_from_file_location(temp_file.name)
        assert module.var1 == "foo"

    # B) Test with a Path location
    with NamedTemporaryFile(mode="w", suffix=".py") as temp_file:
        temp_file.write("var2 = 'bar'")
        temp_file.flush()
        module = load_module_from_file_location(Path(temp_file.name))
        assert module.var

# Generated at 2022-06-14 08:10:41.416263
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    os_environ["SOME_PATH"] = "/some/"
    os_environ["ENV_FILE"] = "env_file.py"

    # A) Check if location contains any environment variables
    #    in format ${some_env_var}.
    try:
        load_module_from_file_location("${env_file}")
    except LoadFileException:
        pass

    try:
        load_module_from_file_location("/some/path/${env_file}")
    except LoadFileException:
        pass

    try:
        load_module_from_file_location("/some/path/${env_file}")
    except LoadFileException:
        pass

    # B) Check these variables exists in environment.

# Generated at 2022-06-14 08:10:54.301889
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    os_environ["TEST_ENV_VAR"] = "/some/path/"
    location = "test_file"
    test_location = "${TEST_ENV_VAR}/some/path/${TEST_ENV_VAR}${TEST_ENV_VAR}"
    test_location += location

    test_file = (
        "\"\"\"Docstring.\"\"\"\n"
        "import os\n"
        "path = os.getcwd() + \"/\"\n"
        "TEST_MODULE_ATTRIBUTE = path + '/'.join(__file__.split('/')[:-1])"
    )

    with open(test_location, "w") as f:
        f.write(test_file)

    module = load_module_from_file

# Generated at 2022-06-14 08:11:06.312185
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from tempfile import NamedTemporaryFile

    def test_config_factory(value) -> types.ModuleType:
        with NamedTemporaryFile(mode="w") as temp:
            temp.write(
                "CONFIG_VALUE = '%s'\n" % value
            )  # write config example

            temp.flush()
            config = load_module_from_file_location(temp.name)

        return config

    # A) Checking if environment variable substitution works fine.
    some_env_var = "some_env_var"
    os_environ[some_env_var] = "some_value"
    with NamedTemporaryFile(mode="w") as temp:
        temp.write(
            "SOME_MODULE_CONFIG = '${%s}'" % some_env_var
        )  # write

# Generated at 2022-06-14 08:11:18.731852
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import tempfile

    # Check that load_module_from_file_location() is working properly
    module = load_module_from_file_location(
        "some_module_name", __file__, "r", False, False
    )
    assert module.__name__ == "some_module_name"

    # Check that load_module_from_file_location() raise LoadFileException
    # if provided environment variable not exists.
    try:
        load_module_from_file_location(
            "some_module_name",
            "/some/path/${SOME_NOT_EXISTS_ENV_VAR}",
        )
    except LoadFileException:
        assert True

    # Check that load_module_from_file_location() is working properly
    # with environment variables.

# Generated at 2022-06-14 08:11:31.203674
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    def _check_if_module_is_loaded():
        if hasattr(module, "foo"):
            return True
        else:
            return False

    module = load_module_from_file_location(
        "/tmp/test_load_module_from_file_location.py",
        textwrap.dedent(
            """\
            foo = 1"""
        ),
    )
    assert module
    assert _check_if_module_is_loaded()
    assert module.foo == 1

    module = load_module_from_file_location(
        "/tmp/test_load_module_from_file_location.py", b"foo = 1",
    )
    assert module
    assert _check_if_module_is_loaded()
    assert module.foo == 1

# Generated at 2022-06-14 08:11:44.011969
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa: D202
    # 1. Check that it handles import strings properly
    assert load_module_from_file_location("math") == math

    # 2. Check that it handles import strings with error properly
    try:
        load_module_from_file_location("a_module_that_does_not_exist")
    except ImportError:
        pass
    else:
        raise  # this should not happen

    # 3. Check that it handles import strings with file locations
    #    properly
    assert (
        load_module_from_file_location("tests.configs.basic_config")
        == tests.configs.basic_config
    )

    # 4. Check that it handles import strings with file locations
    #    with errors properly

# Generated at 2022-06-14 08:11:51.691418
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import pytest
    from os import environ
    from pathlib import Path

    some_module = Path(
        "/some/path/to/${some_env_var}/${some_other_env_var}/some_module.py"
    )

    other_module = Path(
        "/some/path/to/${some_env_var}/${some_other_env_var}/other_module.py"
    )

    environ["some_env_var"] = "some_env_var_value"
    environ["some_other_env_var"] = "some_other_env_var_value"


# Generated at 2022-06-14 08:12:04.210006
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    import ast
    import os
    import pytest
    import tempfile
    from pathlib import Path
    from sanic.exceptions import LoadFileException, PyFileError

    test_cases = [
        (
            "sanic.__init__",
            pytest.raises(LoadFileException),
        ),
        (
            "tests.test_config.settings_module",
            pytest.raises(LoadFileException),
        ),
        (
            "tests.test_config.settings_module_with_error",
            pytest.raises(PyFileError),
        ),
        ("tests.test_config.settings_module_with_env_vars", None),
    ]

    for case, expected_exception in test_cases:
        with expected_exception:
            module = load_module_from_file

# Generated at 2022-06-14 08:12:17.849929
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import tempfile

    from pytest import raises

    # 1. Load file sucessfully.
    location_correctly = tempfile.NamedTemporaryFile(suffix=".py").name
    loaded_module = load_module_from_file_location(location_correctly)
    assert isinstance(loaded_module, types.ModuleType)

    # 2. Fail to load file with non-existing environment variable.
    non_existing_env_var = "non_existing_env_var"
    location_incorrectly = Path(location_correctly).parent / f"${{{non_existing_env_var}}}"
    with raises(LoadFileException) as e:
        load_module_from_file_location(location_incorrectly)
    assert f"The following environment variables are not set: {non_existing_env_var}"

# Generated at 2022-06-14 08:12:23.270690
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import tempfile

    with tempfile.NamedTemporaryFile() as temp_f:
        temp_f.write(b'SOME_SOME = "OK"')
        temp_f.seek(0)
        module = load_module_from_file_location(temp_f.name)

    assert module.SOME_SOME == "OK"

# Generated at 2022-06-14 08:12:35.918741
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    os_environ["TEST_ENV_VAR"] = "test_env_var"

    # without environment variables
    # --------------------------------------------------------
    location = os.path.join(os.path.abspath(__file__ + "/../../.."), "setup.py")

    module = load_module_from_file_location(location)

    assert module.__name__ == "setup"

    # with environment variables
    # --------------------------------------------------------
    module = load_module_from_file_location(
        "config",  # happens that there is a file config.py in the root directory
        "${TEST_ENV_VAR}${TEST_ENV_VAR}${TEST_ENV_VAR}${TEST_ENV_VAR}",
    )

    assert module.__name__ == "config"



# Generated at 2022-06-14 08:12:47.095529
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    import sys
    import uuid

    path = Path(__file__).parent / "test_config.py"
    # Dummy environment variables.
    env_var_1, env_var_2 = str(uuid.uuid4()), str(uuid.uuid4())

    # Check that it loads from Path.
    assert load_module_from_file_location(path)

    # Check that it can resolve environment variables
    assert (
        load_module_from_file_location(f"${env_var_1}/{env_var_2}/{path}")
        == load_module_from_file_location(path)
    )

    # Check that it can load from bytes location.

# Generated at 2022-06-14 08:12:55.583436
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import unittest

    class TestCase(unittest.TestCase):
        def test_load_module_from_file_location_finds_env_vars(self):
            os_environ["some_env_var"] = "some_value"

# Generated at 2022-06-14 08:13:06.657293
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from unittest.mock import patch
    delete_env_var = False
    if "env_var" not in os_environ:
        os_environ["env_var"] = "./tests/config"
        delete_env_var = True
    location = "${env_var}/config.py"

    with patch.object(importlib.util, "spec_from_file_location") as mspec:
        with patch.object(importlib.util, "module_from_spec") as mmod:
            load_module_from_file_location(location)
            mspec.assert_called_with(
                "config",
                "./tests/config/config.py",
                origin="${env_var}/config.py",
            )

# Generated at 2022-06-14 08:13:17.854108
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    cwd = Path.cwd()
    # A) Test ok.
    os_environ["SANIC_TEST_ENV_VAR"] = "environ"
    test_config_module = load_module_from_file_location(
        cwd / "tests/sanic/config_for_testing.py"
    )
    os_environ.pop("SANIC_TEST_ENV_VAR")
    assert test_config_module.TEST_CONFIG == "environ"

    # B) Test ok.
    test_config_module = load_module_from_file_location(
        cwd / "tests/sanic/config_for_testing.py"
    )
    assert test_config_module.TEST_CONFIG == "config_for_testing.py"

    # C) Test

# Generated at 2022-06-14 08:13:30.116927
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import os
    import shutil
    import tempfile
    import unittest
    import warnings

    import yaml

    try:
        with warnings.catch_warnings():  # to suppress pyyaml warning
            warnings.simplefilter("ignore")
            YAML_CONFIG = yaml.load(
                """
                base:
                    string_key: "string_value"
                    boolean_key: true
                """
            )
    except ImportError:
        YAML_CONFIG = None

    class TestLoadModuleFromFileLocation(unittest.TestCase):
        def setUp(self):
            self.dir = tempfile.mkdtemp()
            self.file_name = os.path.join(self.dir, "test_config.py")

        def tearDown(self):
            shutil.rmtree

# Generated at 2022-06-14 08:13:40.159704
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # checking bytes
    bytes_var = b"bytes.py"
    module = load_module_from_file_location(bytes_var)
    assert hasattr(module, "__file__")
    assert module.__file__ == bytes_var.decode("utf8")

    # checking str_to_bool
    assert str_to_bool("yes") is True
    assert str_to_bool("y") is True
    assert str_to_bool("t") is True
    assert str_to_bool("true") is True
    assert str_to_bool("on") is True
    assert str_to_bool("enable") is True
    assert str_to_bool("enabled") is True
    assert str_to_bool("1") is True

    assert str_to_bool("no") is False
    assert str_to_

# Generated at 2022-06-14 08:13:55.725837
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    """
    ./tests/test_utils/test_load_module_from_file_location/test_module.py:
        import sys
        import os

        __file__ = sys.argv[1]
        PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        TESTS_ROOT = os.path.dirname(__file__)

        config = {
            'some_config': {
                'some_value': 42
            }
        }

    """
    # The fastest and most foolproof way to test this function is to test
    # it against a real python module.
    # The Test environment:
    # - Test directory
    #    ├── test_load_module_from_file_location                                                                                                

# Generated at 2022-06-14 08:14:08.883698
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from tempfile import mkdtemp
    from os import environ
    from shutil import rmtree

    import pytest

    some_env_var_value = "some/value/"
    environ["SOME_ENV_VAR"] = some_env_var_value

    test_module_location = (
        "tests/test_module.py"  # Location in this repo relative to main.py
    )
    # test_module_location = os.path.abspath(test_module_location)

    tmpdir = mkdtemp()

    test_module_copy_location = Path(tmpdir) / f"{Path(test_module_location).name}"


# Generated at 2022-06-14 08:14:15.709913
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import pytest

    def _compare_loaded_and_expected(
        loaded,
        file_path,
        encoding="utf8",
        suffix=".py",
        final_dot=False,
        is_package=False,
    ):
        assert isinstance(loaded, types.ModuleType)
        assert loaded.__file__.endswith(file_path)
        assert loaded.__name__.endswith(f"{file_path.name}{'.' if final_dot else ''}")
        assert loaded.__name__.startswith(
            f"{file_path.parent.name}.{file_path.name}"
        ) if is_package else True

# Generated at 2022-06-14 08:14:26.872790
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    assert (
        "some_module_name"
        == load_module_from_file_location(
            "/home/some_name/some_module_name.py"
        ).__name__
    )
    assert ("some_module_name" == load_module_from_file_location("$HOME/some_module_name.py").__name__)
    assert (
        "some_module_name"
        == load_module_from_file_location(Path("/home/some_name/some_module_name.py"))
        .__name__
    )
    assert ("some_module_name" == load_module_from_file_location("/home/some_name/some_module_name.txt").__name__)

# Generated at 2022-06-14 08:14:36.028446
# Unit test for function load_module_from_file_location

# Generated at 2022-06-14 08:14:47.310537
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import os

    location = "tests/test_config.py"
    module = load_module_from_file_location(location)
    assert module.TEST_VAR is True

    location = "tests/test_config.py"
    module = load_module_from_file_location(location)
    assert module.TEST_VAR is True

    location = os.path.abspath("tests/test_config.py")
    module = load_module_from_file_location(location)
    assert module.TEST_VAR is True

    location = "$PWD/tests/test_config.py"
    module = load_module_from_file_location(location)
    assert module.TEST_VAR is True

    location = "tests/test_config.ini"
    module = load_module_from

# Generated at 2022-06-14 08:14:58.306500
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Check if load_module_from_file_location works correctly or not.

    Tests:
    - load_module_from_file_location raises LoadFileException
      if the location contains some not set environment variables.
    - load_module_from_file_location substatutes environment variables
      in the location provided by user.
    - load_module_from_file_location returns module which has module.__file__
      attribute equal to the location provided by user.
    - load_module_from_file_location raises IOError if module cannot
      be found under that location.
    - load_module_from_file_location raises LoadFileException if
      module cannot be loaded and location contains environment variables.
    - load_module_from_file_location raises PyFileError if
      module cannot be loaded and location contains python file.
    """

# Generated at 2022-06-14 08:15:10.565566
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    valid_module_location = "./test_module/test_module_name.py"
    valid_module_name = "test_module.test_module_name"

    # Test valid module location
    loaded_module = load_module_from_file_location(valid_module_location)
    assert loaded_module.__name__ == valid_module_name

    # Test valid module name
    loaded_module = load_module_from_file_location(valid_module_name)
    assert loaded_module.__name__ == valid_module_name

    # Test valid module location with environment variable
    os_environ["TEST_VAR"] = "test_module"
    loaded_module = load_module_from_file_location(
        f"./${TEST_VAR}/test_module_name.py"
    )

# Generated at 2022-06-14 08:15:23.527437
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    import os
    import pytest
    # New empty module
    module = types.ModuleType("module")
    module.__file__ = "/tmp/module.py"
    # Save some data in this module
    module.some_data = "Hello world!"
    # Save module to file
    with open(module.__file__, "w") as module_file:
        module_file.write("some_data = 'Hello world!'")
    # Try to load this module
    loaded_module = load_module_from_file_location(module.__file__)
    # Check that module has been loaded
    assert loaded_module == module
    # Check that some data in this module has been loaded
    assert loaded_module.some_data == "Hello world!"
    # Check that path to module has been loaded
    assert loaded_

# Generated at 2022-06-14 08:15:35.048144
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Tests for function load_module_from_file_location."""
    from sanic import Sanic

    # Check if function will raise error when invalid environment variable
    # is set.
    os_environ["invalid_environ_var"] = ""
    with pytest.raises(LoadFileException):
        load_module_from_file_location(
            "./some_invalid_path/${invalid_environ_var}/file.py"
        )
    del os_environ["invalid_environ_var"]

    # Check if function will raise error when invalid file location is set.
    with pytest.raises(IOError):
        load_module_from_file_location("./some_invalid_path/file.py")

    # Check if function will raise error when invalid file location is set.

# Generated at 2022-06-14 08:15:46.421254
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from os import remove, environ
    from tempfile import mkstemp

    fd, name = mkstemp(suffix=".py")
    with open(name, "w") as temp:
        temp.write("a = 'b'")
    env_key, env_val = "SANIC_TEST_ENV_VAR", "foo/bar"
    environ[env_key] = env_val
    path = "${" + env_key + "}" + name
    loaded_module = load_module_from_file_location(path)
    assert loaded_module.a == "b"
    remove(name)

# Generated at 2022-06-14 08:15:58.944484
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # A) Test loading file with import path
    assert (
        load_module_from_file_location("sanic.config").__name__
        == "sanic.config"
    )

    # B) Test loading file from absolute path
    assert (
        load_module_from_file_location(
            "/home/user/.config/Sanic/config.py"
        ).__name__
        == "config"
    )

    # C) Test loading file with environment variables in path
    os_environ.update(
        {
            "some_env_var": "test",
            "some_other_env_var": "test2",
        }
    )


# Generated at 2022-06-14 08:16:08.037505
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Unit test for function load_module_from_file_location()."""

    import pytest

    # A) Test if function loads a module from python path if it is
    #    in a python path.
    py_path_module = load_module_from_file_location(
        "tests.load_module_from_file_location_module"
    )
    assert py_path_module.__name__ == "tests.load_module_from_file_location_module"

    # B) Test if function loads a module from path if this path is provided.
    file_path = Path(__file__).parent / "load_module_from_file_location_module.py"
    file_path_module = load_module_from_file_location(file_path)

# Generated at 2022-06-14 08:16:18.446537
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    os_environ["SANIC_TEST_ENV_VAR"] = "test_value"
    test_module = load_module_from_file_location(
        "tests/apps/module.py"
    )
    assert test_module.correct_config == "test_value"
    os_environ.pop("SANIC_TEST_ENV_VAR")

    location_with_env_var = (
        Path(__file__).parent / "apps/module.py"
    ).as_posix()  # /some/path/${SANIC_TEST_ENV_VAR}
    os_environ["SANIC_TEST_ENV_VAR"] = "test_value"

# Generated at 2022-06-14 08:16:31.783408
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location(): # noqa
    import os
    import pytest
    import tempfile

    os.environ["TEMP_DIR"] = tempfile.gettempdir()

    def create_config_file(
        content: str, file_name: str, file_path: str
    ) -> None:
        """Create module config file."""
        with open(os.path.join(file_path, file_name), "w") as f:
            f.write(content)

    def check_if_loaded(expected_content, module):
        """Check if module is loaded corectly."""
        assert module.test == expected_content
        assert module.test_env == os.environ["TMP"]

    def check_if_exec_error_correct(error_type):
        """Check if error is raised corectly."""

# Generated at 2022-06-14 08:16:42.511106
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import os
    import tempfile
    import tempfile
    import unittest

    class LoadModuleFromFileLocationTestCase(unittest.TestCase):
        def test_load_module(self):
            test_module = """
            x = 'abc'
            y = {'abc': 1}
            """
            _, temp_path = tempfile.mkstemp()
            with open(temp_path, "w") as temp_file:
                temp_file.write(test_module)

            module = load_module_from_file_location(temp_path)
            self.assertEqual(module.x, "abc")
            self.assertDictEqual(module.y, {"abc": 1})
            os.remove(temp_path)

            # Also test here that the path can be of the Path object type
           

# Generated at 2022-06-14 08:16:53.596601
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    os_environ["TEST_CONFIG_ENV_VAR"] = "test_config_env_var"

    # Test when config is loaded by name.
    test_module = load_module_from_file_location("test_config")
    assert test_module.test_env_var == os_environ["TEST_CONFIG_ENV_VAR"]

    # Test when config is loaded by file.
    test_module = load_module_from_file_location("test_config.py")
    assert test_module.test_env_var == os_environ["TEST_CONFIG_ENV_VAR"]

    # Test when config is loaded by file with path.
    test_module = load_module_from_file_location("test_configs/test_config.py")

# Generated at 2022-06-14 08:16:57.606983
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    PATH_TO_TEST = Path(__file__).parent / "load_module_from_file_location.py"
    module = load_module_from_file_location(PATH_TO_TEST)
    assert module.TEST == 123

# Generated at 2022-06-14 08:17:08.848432
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Unit test for function load_module_from_file_location"""
    assert load_module_from_file_location("sanic.app") is sanic.app
    assert load_module_from_file_location(
        "builtins.dict", encoding="ascii"
    ) is dict
    assert load_module_from_file_location(b"builtins.dict") is dict

    my_file = Path(__file__).parent / "test_file.py"
    assert load_module_from_file_location(my_file)

    my_file = Path(__file__).parent / "test_file.txt"
    assert load_module_from_file_location(my_file)


# Generated at 2022-06-14 08:17:20.481401
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    location = "tests/fixtures/conf/config.py"
    config = load_module_from_file_location(location)
    assert config.TESTING

    try:
        load_module_from_file_location("./test/test")
        assert False
    except LoadFileException as e:
        assert "Cannot locate configuration file" in e.args[0]

    try:
        load_module_from_file_location(
            "/home/${TESTING_HOMEDIR}/test/test"
        )
        assert False
    except LoadFileException as e:
        assert "The following environment variables are not set" in e.args[0]

    os_environ["TESTING_HOMEDIR"] = "test"

# Generated at 2022-06-14 08:17:24.930878
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    assert load_module_from_file_location("tests.test_helpers")

# Generated at 2022-06-14 08:17:37.841364
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # 1. Test using file path as module name.
    location = Path(__file__).parent / "config" / "test_config.py"
    module_name = location.stem
    assert (
        module_name
        == load_module_from_file_location(location).__name__
    )

    # 2. Test using string as module name.
    module_name = "test"
    assert module_name == load_module_from_file_location(
        location, module_name
    ).__name__

    # 3. Test using file path not ending with .py as module name.
    location = Path(__file__).parent / "config" / "not_end_with_py"
    assert load_module_from_file_location(location).__file__ == str(
        location
    )

    # 4

# Generated at 2022-06-14 08:17:50.851041
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # A) Check string (env vars will not be resolved)
    assert (
        load_module_from_file_location("$env_var_that_doesn_exist")
        is None
    )  # this location does not exist.

    # B) Check bytes (env vars will not be resolved)
    assert (
        load_module_from_file_location(b"$env_var_that_doesn_exist")
        is None
    )  # this location does not exist.

    # C) Check Path (env vars will not be resolved)
    assert (
        load_module_from_file_location(Path("$env_var_that_doesn_exist"))
        is None
    )  # this location does not exist.

    # D) Check string with resolved env vars
    # I) Create file
    tmp

# Generated at 2022-06-14 08:17:58.614763
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from os import environ
    from os import getcwd
    from os import path
    from os.path import exists
    from tempfile import mkdtemp
    from glob import glob

    # A) Preparation.
    #    Create environment variables
    environ["ENV_VAR_1"] = "env_var_1_val"
    environ["ENV_VAR_2"] = "env_var_2_val"

    #    Create configuration file in tmp dir and
    #    include in it some environment variables.
    actual_temp_dir = mkdtemp()
    temp_file_name = "test_config.py"
    expected_temp_file_path = path.join(actual_temp_dir, temp_file_name)

# Generated at 2022-06-14 08:18:10.912516
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Make sure that function works as intended."""
    location = "tests/utils_test/load_module_from_file_location_test"
    test_module = load_module_from_file_location(location)

    assert isinstance(test_module, types.ModuleType)
    assert test_module.__name__ == "load_module_from_file_location_test"
    assert test_module.__file__ == location
    assert test_module.TEST_CONST == 42
    assert test_module.TEST_FUNC(42) == 42

    location = "tests/utils_test/load_module_from_file_location_test.py"
    test_module = load_module_from_file_location(location)

    assert isinstance(test_module, types.ModuleType)