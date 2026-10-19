

# Generated at 2022-06-14 08:08:27.436201
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # test passing location as string (with environment variable in it)
    os_environ["some_env_var"] = "from-environment"
    mod = load_module_from_file_location(
        "sanic.conf.${some_env_var}.settings",
        "/sanic/conf/from-environment/",
    )
    assert mod.SOME_SETTING == "some_setting_value"
    del os_environ["some_env_var"]

    # test passing location as path (without environment variable)
    mod = load_module_from_file_location(
        Path("/sanic/conf/from-file-system/settings.py")
    )
    assert mod.SOME_SETTING == "some_setting_value"

    # test passing location as bytes(with environment variable in it)
    os_

# Generated at 2022-06-14 08:08:36.095099
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from .test_helpers import TempDirectory

    with TempDirectory() as tmp:
        with open(f"{tmp}/file.py", "w") as f:
            f.write("x = 123")

        assert load_module_from_file_location(f"{tmp}/file.py")
        assert load_module_from_file_location(f"{tmp}/file.py")
        assert load_module_from_file_location(f"{tmp}/file.py")



# Generated at 2022-06-14 08:08:49.357012
# Unit test for function load_module_from_file_location

# Generated at 2022-06-14 08:08:59.546750
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import os
    import pytest

    # Test load module using path to file as a string
    module = load_module_from_file_location(
        location=os.path.join(os.path.dirname(__file__), "application_factory.py")  # noqa
    )
    assert hasattr(module, "create_app") is True
    assert callable(getattr(module, "create_app", None)) is True

    # Test load module using pathlib.Path
    module = load_module_from_file_location(
        location=Path(os.path.dirname(__file__), "application_factory.py")
    )
    assert hasattr(module, "create_app") is True
    assert callable(getattr(module, "create_app", None)) is True

    # Test load

# Generated at 2022-06-14 08:09:11.721595
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    import sys
    import os
    import os.path as path

    def raise_if_not_equal(left, right, error_msg):
        assert left == right, error_msg

    # 1. Test function raises correct error
    # if path doesn't exist
    try:
        load_module_from_file_location(
            "test/test_configs.py",
            "test/this/path/does/not/exist/test_configs.py",
        )
        assert False, "Should raise LoadFileException"
    except LoadFileException as e:
        raise_if_not_equal(
            str(e),
            "Unable to load configuration file (No such file or directory)",
            "Should contain correct error message.",
        )

    # 2. Test function raises correct error
    # if environment

# Generated at 2022-06-14 08:09:23.769788
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    # ==========
    # A) Check if location contains any environment variables
    #    in format ${some_env_var}.
    # B) Check these variables exists in environment.
    # C) Substitute them in location.
    # ==========
    # A) Check if location contains any environment variables
    #    in format ${some_env_var}.
    # ==========
    os_environ["SOME_ENV_VAR"] = "SOME_VALUE"
    location = "${SOME_ENV_VAR}/path/${SOME_ENV_VAR}.py"
    env_vars_in_location = set(re_findall(r"\${(.+?)}", location))

    # B) Check these variables exists in environment.
    not_defined_env_vars

# Generated at 2022-06-14 08:09:33.231196
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    try:
        import test_module
        test_module.name = "test_module"
    except ImportError:
        test_file = open("test_module.py", "w")
        test_file.write('name = "test_module"')
        test_file.close()
        import test_module

    # A
    location = "${PWD}/test_module.py"
    module = load_module_from_file_location(location)
    assert module.name == "test_module"
    assert module.__file__ == location

    # B
    location = Path("test_module.py")
    module = load_module_from_file_location(location)
    assert module.name == "test_module"
    assert module.__file__ == str(location)

    # C

# Generated at 2022-06-14 08:09:42.125442
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import sys

    def wotest():
        sys.path.append("/some/path")

        found_correct_module = False


# Generated at 2022-06-14 08:09:50.884678
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # pylint: disable=W0612
    import tempfile
    import shutil
    import unittest
    from unittest.mock import patch
    from pathlib import Path

    # get a `tempfile.TemporaryDirectory` instance
    with tempfile.TemporaryDirectory() as temp_dir:

        # use the `Path` class for better portability
        path = Path(temp_dir)

        # create a `test.py` file
        test_file = path / "test.py"

# Generated at 2022-06-14 08:10:01.259179
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """This function tests `load_module_from_file_location` method

    You can change the test config_yml file to update the test.
    """
    os_environ["TEST_CONFIG_LIST_VALUE"] = "['test_list_value']"
    os_environ["TEST_CONFIG_BOOL_VALUE"] = "on"
    os_environ["TEST_CONFIG_INT_VALUE"] = "123"
    os_environ["TEST_CONFIG_STR_VALUE"] = "test_str_value"
    os_environ["TEST_CONFIG_FLOAT_VALUE"] = "1234.567"
    os_environ["TEST_CONFIG_NESTED"] = '{"nested_key": "nested_value"}'

# Generated at 2022-06-14 08:10:15.754620
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa

    import os
    from pathlib import Path
    from unittest import TestCase

    from sanic.exceptions import LoadFileException

    from .helpers import create_file

    class TestLoadModuleFromFileLocation(TestCase):
        """Tests load_module_from_file_location function."""

        def setUp(self):
            # If some of this environment variables are set
            # before test starts, then save their values.
            if "some_env_var" in os.environ:
                self.__some_env_var = os.environ["some_env_var"]
                del os.environ["some_env_var"]


# Generated at 2022-06-14 08:10:26.494372
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    os_environ["test_var"] = "test"

    # Load a module.
    module = load_module_from_file_location(
        location="./tests/test_application.py",
        package=None,
    )

    # Test if the module is really loaded.
    assert module.test_answer == 42

    # Test loading module with environment variables.
    module_with_env_var = load_module_from_file_location(
        location="./tests/${test_var}_application.py",
        package=None,
    )

    assert module_with_env_var.test_answer == 42

    # Test loading module with multiple environment variables.
    multiple_env_vars = "./tests/${test_var}_${test_var}_application.py"
    module_with_multiple

# Generated at 2022-06-14 08:10:39.639325
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa

    # Check if functions raises ValueError when
    # location exists in environment but has no value
    os_environ["mock_env_var"] = ""
    try:
        load_module_from_file_location("${mock_env_var}")
    except LoadFileException as e:
        e = str(e)
        assert e == "The following environment variables are not set: mock_env_var"
    del os_environ["mock_env_var"]

    # Check if function can load module from path
    mock_dict = {"mock_module_key": "mock_module_value"}
    os_environ["mock_env_var"] = "$SOME_TEST_PATH/some_python_module.py"

# Generated at 2022-06-14 08:10:46.383439
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Unit test for function load_module_from_file_location."""
    import pytest

    def test_error(location):
        with pytest.raises(LoadFileException):
            load_module_from_file_location(location)

    test_error("unknown-variable")
    test_error("/some/path/unknown-variable")
    test_error("${unknown_variable}")
    test_error("/some/path/${unknown_variable}")

# Generated at 2022-06-14 08:10:57.524908
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # A) Check if location contains environment variable in format ${some_env_var}
    def test_env_vars():
        try:
            load_module_from_file_location("/some/path/${some_env_var}")
            raise ValueError("Test not passed")
        except LoadFileException:
            pass

    # B) Check for non existing file (Unable to load configuration file)
    def test_not_existing_file():
        try:
            load_module_from_file_location("/some/non_existing_file.py")
            raise ValueError("Test not passed")
        except PyFileError:
            pass

    # C) Check for empty file

# Generated at 2022-06-14 08:11:10.243591
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import os
    import tempfile
    import importlib

    with open("tests/sample_config/config.py") as file_handler:
        file_data = file_handler.read()

    # 1.)  Load module from file name of string type
    #      with/without .py extension.
    #      Check basic data inside of loaded module and
    #      if module was cached in sys.modules.
    for file_name in ["config.py", "config"]:
        module = load_module_from_file_location(
            "tests/sample_config/{}".format(file_name)
        )


# Generated at 2022-06-14 08:11:18.261490
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from tempfile import NamedTemporaryFile

    with NamedTemporaryFile() as config_file:
        config_file.write(
            b"""
some_val = "some_val"
some_var = "some_var"
"""
        )
        config_file.flush()

        loaded_module = load_module_from_file_location(config_file.name)

    assert loaded_module.some_val == "some_val"
    assert loaded_module.some_var == "some_var"

# Generated at 2022-06-14 08:11:31.051373
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    path = Path(__file__).parent / "sanic_motor.py"
    # A) load_module_from_file_location:
    #    - not set any parameters
    #    - just import module provided as a path.
    from . import sanic_motor

    sanic_motor_1 = load_module_from_file_location(path)
    assert sanic_motor_1 is sanic_motor

    # B) load_module_from_file_location
    #    - not set any parameters
    #    - import module provided as a string.
    sanic_motor_2 = load_module_from_file_location(str(path))
    assert sanic_motor_2 is sanic_motor

    # C) load_module_from_file_location
    #    -

# Generated at 2022-06-14 08:11:37.442164
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    location = (
        "tests/test_utils/test_load_module_from_file_location"
        "/test_module_from_file_location.py"
    )
    assert isinstance(
        load_module_from_file_location(location), types.ModuleType
    )

# Generated at 2022-06-14 08:11:43.182985
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa

    PATH = Path.cwd()
    os_environ["CUR_DIR"] = str(PATH)
    TEST_FILE_NAME = "test_load_module_from_file_location.py"

# Generated at 2022-06-14 08:11:52.274992
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa: F811
    # A) Check if location parameter is of a bytes type
    assert load_module_from_file_location(bytes("./", "utf8")).__file__ == (
        Path().absolute().joinpath("./").__str__()
    )

    # B) Check if it works without passing any extra args
    assert not load_module_from_file_location("./config.py").DEBUG

    # C) Check if it works with args
    assert load_module_from_file_location("./config.py", True).DEBUG

    # D) Check if location parameter is of a Path type
    assert load_module_from_file_location(
        Path("./config.py"), False
    ).DEBUG is False

    # E) Check if location parameter can contains environment variables
    #    in format

# Generated at 2022-06-14 08:12:03.395165
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from os import system
    from tempfile import NamedTemporaryFile
    from textwrap import dedent
    from uuid import uuid4
    from unittest import TestCase

    class LoadModuleFromFileLocationTestCase(TestCase):
        def setUp(self):
            self.file_content = dedent(
                """
            variable_1 = "test variable value"
            variable_2 = 123
            variable_3 = ['a', 'b', 'c']
            variable_4 = {'first': '1', 'second': '2', 'third': '3'}
            variable_5 = ('a', 'b', ['1', '2', '3'], {'first': '1', 'second': '2'})
            """
            )
            self.tmp_file = NamedTemporaryFile(delete=False)

# Generated at 2022-06-14 08:12:17.055316
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Function to test load_module_from_file_location"""

    from os import environ
    from os.path import join
    from tempfile import mkdtemp
    from shutil import rmtree
    from pathlib import Path

    try:
        from unittest.mock import patch
        from unittest.mock import MagicMock
    except ImportError:
        from unittest.mock import patch
        from unittest.mock import MagicMock

    def _check_returned_module(module):
        """Checks if module is loaded properly"""
        assert "some_attr" in dir(module)
        assert module.some_attr == "some_attr_value"
        assert "some_function" in dir(module)
        assert module.some_function() == "some_function_return_value"



# Generated at 2022-06-14 08:12:23.837175
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    id_ = id(load_module_from_file_location("os"))
    new_id = id(load_module_from_file_location("os"))
    assert id_ == new_id

    id_ = id(load_module_from_file_location("os.path"))
    new_id = id(load_module_from_file_location("os.path"))
    assert id_ == new_id

    id_ = id(load_module_from_file_location("os.path.abspath"))
    new_id = id(load_module_from_file_location("os.path.abspath"))
    assert id_ == new_id

    id_ = id(
        load_module_from_file_location(
            Path("tests/test_helpers.py").absolute()
        )
    )

# Generated at 2022-06-14 08:12:36.300953
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from os import remove
    from os.path import exists

    # Get current path
    current_path = Path(__file__).parent

    # 1. Test with module file
    # 1.1. Basic configuration
    os_environ["ENV_VAR_BASIC_CONFIG_FILE"] = str(current_path)
    module = load_module_from_file_location(
        "test_module.py",
        "${ENV_VAR_BASIC_CONFIG_FILE}/test_module.py",
    )
    assert module.CONF_VAR == "conf_var"

    # 1.2. Nonexistent file
    nonexistent_file_name = "nonexistent_file.py"

# Generated at 2022-06-14 08:12:47.264015
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    def test_module_from_file_location(module):
        assert module.test_variable == "success"

    # check if module located on fs is imported properly
    test_module_from_file_location(
        load_module_from_file_location(
            __file__[:-len("test_utils.py")] + "helpers/test_module.py"
        )
    )
    # check if module located on fs is imported properly in case
    # environment variable is used in path to this file
    test_module_from_file_location(
        load_module_from_file_location(
            __file__[:-len("test_utils.py")]
            + "${"
            + "TEST_MODULE_FILE_PATH_ENV_VAR"
            + "}"
        )
    )

# Generated at 2022-06-14 08:12:58.500569
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Unit test for function load_module_from_file_location."""
    from os.path import dirname as os_path_dirname
    from os.path import join as os_path_join
    from os import environ as os_environ
    import random
    import string

    # A) Test case load_module_from_file_location.
    #    Test some random location.
    #    Create some Python file with random name.
    #    Create random variables in this Python file.
    #    Create random variables in environment.
    #    Check if we can load this Python file and if it has variables
    #    equal to random environment variables.

# Generated at 2022-06-14 08:13:08.847331
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    def testable_load_module_from_file_location(
        location: Union[bytes, str, Path], encoding: str = "utf8"
    ):
        return load_module_from_file_location(
            location, encoding, packages=["sanic_jinja2_tests"]
        )

    assert "test_module" == (
        testable_load_module_from_file_location(
            Path(__file__).parent.parent
            / "sanic_jinja2_tests"
            / "modules"
            / "test_module.py"
        ).__name__
    )


# Generated at 2022-06-14 08:13:20.312273
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Unit test for function load_module_from_file_location."""
    # A) Positive tests
    os_environ["some_env_var"] = "some_value"

# Generated at 2022-06-14 08:13:32.268099
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    os_environ["TEST_ENV_VAR"] = "test_env_var_value"
    test_dir_path = Path(__file__).parent / "test_dir"
    test_dir_path.mkdir(parents=True, exist_ok=True)

    test_module_path = test_dir_path / "test_module.py"
    with open(test_module_path, "w") as test_module_file:
        test_module_file.write("test_var = 7")

    test_module_string_path = test_dir_path / "test_module_string.py"
    with open(test_module_string_path, "w") as test_module_string_file:
        test_module_string_file.write('test_var = "module_string"')

   

# Generated at 2022-06-14 08:13:44.809392
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    location = "test_location"
    os_environ["some_env_var"] = "some_env_value"
    env_var = "${some_env_var}"

    for location in [
        "test_location",
        location.encode(),
        Path(location),
        os_environ["some_env_var"],
        "${some_env_var}",
        location + env_var,
        Path(location + env_var),
    ]:
        assert load_module_from_file_location(location)

# Generated at 2022-06-14 08:13:56.189578
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from unittest.mock import patch


# Generated at 2022-06-14 08:14:09.326789
# Unit test for function load_module_from_file_location

# Generated at 2022-06-14 08:14:15.898498
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from .config import load_module_from_file_location as t
    import os, tempfile
    env_var_content = "a_var"
    os.environ["SOME_ENV_VAR"] = env_var_content
    with tempfile.NamedTemporaryFile(mode="w+") as temp_file:
        temp_file.write(f"some_var = 42")
        temp_file.flush()
        module = t(temp_file.name)
        assert module.some_var == 42
    module = t(Path(temp_file.name))
    assert module.some_var == 42
    # Test with environment variable
    module = t(Path(f"{temp_file.name}_with_env_var/${{SOME_ENV_VAR}}"))
    assert module.some_

# Generated at 2022-06-14 08:14:24.623419
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Test if we correctly import configuration module.

    We are testing this in two ways.
    First:
        By importing a configuration module from current dir with
        importlib.util.spec_from_file_location.
    Second:
        By importing a configuration module from current dir using
        the import_string function which is used in the original
        get_config function"""

    # A) Check if importing configuration module with
    #    importlib.util.spec_from_file_location works.
    config_module = load_module_from_file_location(__file__)

    assert hasattr(config_module, "CONFIG_MODULE_ATTRIBUTE") == True
    assert config_module.CONFIG_MODULE_ATTRIBUTE == "ATTRIBUTE_IN_CONFIG_MODULE"

    # B) Check if importing configuration

# Generated at 2022-06-14 08:14:33.945956
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import os

    os.environ["some_env_var"] = "some_path/"
    from_str = load_module_from_file_location(
        "some_module_name", "some_path/${some_env_var}"
    )
    from_bytes = load_module_from_file_location(
        b"some_module_name", b"some_path/${some_env_var}"
    )
    from_path = load_module_from_file_location(
        Path("some_module_name"), Path("some_path/${some_env_var}")
    )

    assert from_str == from_bytes == from_path



# Generated at 2022-06-14 08:14:45.662503
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # 1.
    module = load_module_from_file_location(
        "/Users/user/sanic/config.py"
    )  # str type
    assert module.__name__ == "config"

    # 2.
    module = load_module_from_file_location(
        b"/Users/user/sanic/config.py"
    )  # bytes type
    assert module.__name__ == "config"

    # 3.
    module = load_module_from_file_location(
        Path("/Users/user/sanic/config.py")
    )  # pathlib.Path type
    assert module.__name__ == "config"

    # 4.

# Generated at 2022-06-14 08:14:46.529215
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """UnitTests for function load_module_from_file_location."""
    pass

# Generated at 2022-06-14 08:14:57.622119
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    test_mod = "tests.helpers_tests.test_config"
    test_mod_without_py = "tests.helpers_tests.test_config_without_py"

    assert load_module_from_file_location(test_mod,).content == "test_config"

    assert load_module_from_file_location(
        test_mod_without_py,
    ).content == "test_config_without_py"

    assert load_module_from_file_location(
        test_mod_without_py,
    ).__name__ == "test_config_without_py"

    assert load_module_from_file_location(
        test_mod_without_py,
    ).__file__ == "without_py"

    # Test custom loader

# Generated at 2022-06-14 08:15:09.887739
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from os import pathsep, environ as os_environ
    from shutil import copyfile
    from tempfile import TemporaryDirectory
    from testing_config import config

    def create_env(**kwargs):
        for key, val in kwargs.items():
            os_environ[key] = val

    def create_py_file(file_name, content):
        with open(file_name, "w") as file:
            file.write(content)

    # Test 1.
    with TemporaryDirectory() as tmp_dir:
        file_name = tmp_dir + "/some_module.py"
        copyfile("testing_config/config.py", file_name)
        location = file_name
        # A.
        loaded_module = load_module_from_file_location(location, "utf8")
       

# Generated at 2022-06-14 08:15:26.402470
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    import sys
    import os

    assert "test_load_module_from_file_location.py" in sys.argv[0]
    test_config_file = Path(sys.argv[0]).parent / "test_config_file.py"

    # A) Test that it reads from .py file.
    config = load_module_from_file_location(test_config_file)
    assert all(
        [
            getattr(config, attr)
            for attr in config.__dict__.keys()
            if not attr.startswith("_")
        ]
    )

# Generated at 2022-06-14 08:15:36.891743
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import pytest
    import pathlib

    # A)
    # When in location string
    # there are no environment variables in format ${some_env_var}
    # this should not cause any errors
    location = "valid/path/to/some/file"
    assert load_module_from_file_location(location) is not None

    # B)
    # When in location string we use environment variables in format ${some_env_var},
    # verify that:
    # - They have to be defined/set in environment.
    # - That they will be successfully resolved and it will not cause any errors
    not_defined_env_var = "some_not_set_env_var_abc"
    location = f"valid/path/to/some/${{{not_defined_env_var}}}/file"


# Generated at 2022-06-14 08:15:44.867965
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import tempfile

    name = "test_load_module_from_file_location"
    expected_list = [1, 2, 3]

    with tempfile.NamedTemporaryFile(delete=False) as f:
        f.write(bytes(f"""{name} = {expected_list}""", "utf8"))
        f.flush()
        f.close()

        test_module = load_module_from_file_location(f.name)

    os.remove(f.name)

    retured_list = test_module.__dict__[name]
    assert expected_list == retured_list

# Generated at 2022-06-14 08:15:57.740838
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import tempfile
    import os

    config_data = """
    DEBUG = True

    class App:
        pass
    """

    with tempfile.NamedTemporaryFile(suffix=".py", delete=True) as config_file:
        config_file.write(config_data.encode())
        config_file.flush()

        # A) Path object
        configuration = load_module_from_file_location(Path(config_file.name))
        assert configuration.DEBUG is True

        # B) bytes
        configuration = load_module_from_file_location(config_file.name.encode())
        assert configuration.DEBUG is True

        # C) string containing environment variable
        os.environ["MY_ENV_VAR"] = config_file.name

# Generated at 2022-06-14 08:16:04.367156
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    assert load_module_from_file_location("pathlib")
    assert load_module_from_file_location("os.path") is os.path
    assert (
        load_module_from_file_location("tests.aio.test_utils.fake_module")
        is fake_module
    )

    assert load_module_from_file_location("fake_path")
    os.remove("fake_path")

# Generated at 2022-06-14 08:16:16.979317
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    import tempfile

    def create_temp_module(file_name, content):
        with tempfile.NamedTemporaryFile(mode="w", suffix=file_name + ".py") as f:
            f.write(content)
            f.flush()
            return load_module_from_file_location(f.name)

    def create_temp_text_module(file_name, content):
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=file_name + ".txt"
        ) as f:
            f.write(content)
            f.flush()
            return load_module_from_file_location(f.name)


# Generated at 2022-06-14 08:16:29.587606
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from tempfile import NamedTemporaryFile
    import pytest

    BASE_PATH = Path(__file__).parent / "test_helpers"

    def check_module(location, expected_result, env_vars_to_be_added=None):
        if env_vars_to_be_added is not None:
            for var, val in env_vars_to_be_added.items():
                os_environ[var] = val

        assert load_module_from_file_location(location) == expected_result

        if env_vars_to_be_added is not None:
            for var in env_vars_to_be_added.keys():
                del os_environ[var]

    # Test with environment variables

# Generated at 2022-06-14 08:16:38.443817
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import pytest

    from tempfile import TemporaryDirectory

    file_with_env_vars = """
# Example with environment variables in file location

some_env_var = ${SOME_ENV_VAR}
some_env_var_2 = ${SOME_ENV_VAR_2}
"""

    file_without_env_vars = """
# Example without environment variables in file location
some_env_var = "some_value"
some_env_var_2 = "some_value_2"
"""

    def test_load_module_from_file_location_without_env_vars(tmp_path):

        tmp_file = tmp_path / "test_file.py"
        tmp_file.write_text(file_without_env_vars)

        module = load_module_from_file_

# Generated at 2022-06-14 08:16:46.676396
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """
    GIVEN provided file path,
    WHEN load_module_from_file_location is called,
    THEN ensure module is loaded correctly.
    """
    expected_module = import_string("os")

    path = Path(__file__).parent.joinpath("os.py")

    # Check if module loaded is the module we expect to.
    assert (
        load_module_from_file_location(path) == expected_module
    ), "Module loaded should be the same as expected."


# Generated at 2022-06-14 08:16:59.317308
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from tempfile import NamedTemporaryFile
    import os
    import sys

    assert os.environ.get("TEST_SECRET") is None
    os.environ["TEST_SECRET"] = "this is a secret"

    with NamedTemporaryFile(mode="w+") as f:
        f.write('print("loading config file")\n' "SECRET='${TEST_SECRET}'")
        f.flush()
        sys.path.insert(0, f.name[:-3])
        mod = load_module_from_file_location(f.name)
    assert mod.SECRET == "this is a secret"

    with NamedTemporaryFile(mode="w+") as f:
        f.write(
            'raise Exception("something is wrong with this config file")'
        )
        f.flush

# Generated at 2022-06-14 08:17:21.850572
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # Test get module from location
    some_module = load_module_from_file_location(__name__)
    assert some_module is not None
    assert hasattr(some_module, "load_module_from_file_location")

    # Test that when location is given by name of existing module,
    # then the same module is returned.
    load_module_from_file_location(__name__) == some_module

    # Test module from non existing path
    with pytest.raises(LoadFileException):
        load_module_from_file_location("/not/existing/path")

    # Test when location contains environment variables in format
    # ${some_env_var}.

    # A) Test that if some of them is not defined in environmnet,
    #    then error is raised.

# Generated at 2022-06-14 08:17:27.696008
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    os_environ["some_env_var"] = "some/path/to/some/config.py"
    some_module = load_module_from_file_location(os_environ["some_env_var"])
    assert hasattr(some_module, "CONFIG_VAR")
    assert some_module.CONFIG_VAR == "some_val"
    del os_environ["some_env_var"]

# Generated at 2022-06-14 08:17:39.621743
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import tempfile
    from os.path import dirname as os_path_dirname
    from warnings import catch_warnings, filterwarnings
    from sanic.log import logger
    logger.setLevel("ERROR")
    with catch_warnings():
        filterwarnings("ignore", category=DeprecationWarning)

        # Create a temporary directory.
        tmp_dir = tempfile.mkdtemp()
        test_config_file = f"{tmp_dir}/test_config.py"
        test_config_file_wrong_path = f"{tmp_dir}/wrong_path/test_config.py"

        # Create a temporary file.
        with open(test_config_file, "w") as f:
            f.write("CONFIG_VARIABLE = 'Example configuration string'")

        # Test that the file

# Generated at 2022-06-14 08:17:52.015478
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # A) Successful import
    if config.DEBUG:
        _mod = load_module_from_file_location(
            Path("tests/test_config.py"), Path("tests")
        )
        assert _mod.test_conf["test_key"] == "test_value"
        assert _mod.test_conf["test_key_2"] == 43
        # If imported module is in
        # sys.modules, then remove it
        # for further tests.
        if "tests.test_config" in sys.modules:
            del sys.modules["tests.test_config"]

    # B) Import module from PATH
    if config.DEBUG:
        _mod = load_module_from_file_location("tests/test_config")
        assert _mod.test_conf["test_key"] == "test_value"

# Generated at 2022-06-14 08:18:05.883624
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from unittest import TestCase

    from os import environ
    from pathlib import Path

    from sanic.exceptions import LoadFileException, PyFileError

    from sanic_envconfig.main import (
        load_module_from_file_location,
        str_to_bool,
    )

    # Create test files
    # Strings
    with open("test.py", "w") as f:
        f.write('var = "string"')
    # Lists
    with open("test1.py", "w") as f:
        f.write("var = [1, 2, 3]")
    # Booleans
    with open("test2.py", "w") as f:
        f.write("var = False")
    # Ints

# Generated at 2022-06-14 08:18:16.292503
# Unit test for function load_module_from_file_location