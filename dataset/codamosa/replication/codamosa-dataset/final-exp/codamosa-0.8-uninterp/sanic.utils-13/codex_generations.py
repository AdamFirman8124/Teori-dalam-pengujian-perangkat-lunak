

# Generated at 2022-06-14 08:08:25.166713
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import os

    env_vars = {
        "some_env_var": "some_env_val",
        "some_env_var_with_nested_env_var": "${some_env_var}",
    }
    for key, value in env_vars.items():
        os.environ[key] = value

    # A) Test module loading
    location = "sanic/config.py"
    module = load_module_from_file_location(location)

    assert "sanic.config" in repr(module)

    # B) Test using environment variable in module path
    os.environ["some_env_var"] = "sanic"
    os.environ["some_env_var_with_nested_env_var"] = "sanic"

# Generated at 2022-06-14 08:08:36.041833
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import tempfile
    import os

    location = "test_test.py"
    with tempfile.TemporaryDirectory() as tmp:
        tmp_location = os.path.join(tmp, location)

        with open(tmp_location, "w") as f:
            test_code = """
                test_string = "hello world"
                test_list = [1, 2, 3]
            """
            f.write(test_code)

        module = load_module_from_file_location(tmp_location)
        assert module.test_string == 'hello world'
        assert module.test_list == [1, 2, 3]

        # Test module loading from bytes path
        module = load_module_from_file_location(
            Path(tmp_location).read_bytes()
        )
        assert module.test_string

# Generated at 2022-06-14 08:08:49.302085
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    os_environ["TEST_ENV_VAR"] = "env_var_value"
    os_environ["TEST_ENV_VAR2"] = "env_var_value2"
    os_environ["TEST_ENV_VAR3"] = "env_var_value3"

    module = load_module_from_file_location("sanic.config.DEFAULTS")
    assert isinstance(module, types.ModuleType)
    assert module.REQUEST_MAX_SIZE == 100000000

    module = load_module_from_file_location(
        "/sanic/config/${TEST_ENV_VAR}", "sanic.config"
    )
    assert isinstance(module, types.ModuleType)

# Generated at 2022-06-14 08:08:59.511446
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # 1. Test situation when you have to load file with .py extension.
    expected_result = {}
    expected_result["TEST_VAR_1"] = 1
    expected_result["TEST_VAR_2"] = "some text"
    expected_result["TEST_VAR_3"] = False

    result = load_module_from_file_location(__file__).__dict__
    assert result == expected_result

    # 2. Test situation when file name does not have .py extension.
    expected_result = {}
    expected_result["TEST_VAR_1"] = 1
    expected_result["TEST_VAR_2"] = "some text"
    expected_result["TEST_VAR_3"] = False


# Generated at 2022-06-14 08:09:11.212737
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    os_environ["some_env_var"] = "some_value_for_env_var"
    os_environ["some_bool_env_var"] = "true"
    os_environ["some_int_env_var"] = str(1)
    path = Path("tests/components/test_config.py")

    module = load_module_from_file_location(path)
    assert module.some_config == "some_value"
    assert module.some_env_config == "some_value_for_env_var"
    assert module.some_bool_config is True
    assert module.some_int_config == 1
    assert module.some_bool_env_config is True
    assert module.some_int_env_config == 1



# Generated at 2022-06-14 08:09:23.341614
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    assert import_string("os.path") == os.path
    assert str_to_bool("t") is True
    assert str_to_bool("y") is True
    assert str_to_bool("yes") is True
    assert str_to_bool("yup") is True
    assert str_to_bool("n") is False
    assert str_to_bool("no") is False
    assert str_to_bool("f") is False
    assert str_to_bool("false") is False
    assert str_to_bool("0") is False
    assert str_to_bool("1") is True

    assert str_to_bool("not_a_bool") is False

# Generated at 2022-06-14 08:09:32.914087
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Tests functions load_module_from_file_location."""

    # A) Test for correct behaviour of load_module_from_file_location with
    #    environment variables.
    # A.1) Set environment variables:
    vars_set = {
        "env_var_in_dir": "env_var_value_in_dir",
        "env_var_in_file": "env_var_value_in_file",
    }
    for key, val in vars_set.items():
        os_environ[key] = val

    # A.2) Create some test files and directories.
    root_dir = Path(__file__) / "../../../tmp/test_load_module"
    root_dir.mkdir(exist_ok=True, parents=True)

# Generated at 2022-06-14 08:09:42.041619
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    from os import environ as os_environ
    from pathlib import Path
    from tempfile import TemporaryDirectory
    from unittest import TestCase

    from sanic.utils import load_module_from_file_location

    class LoadModuleFromFileLocationTests(TestCase):
        def setUp(self):
            # Create temporary directory.
            self.temp_dir = TemporaryDirectory()

        def tearDown(self):
            # Close temporary directory.
            self.temp_dir.cleanup()

        def test_with_env_vars(self):

            TEST_CONFIG_FILE_CONTENT = """
            OPTION = "Option"

            class Option:
                value = "Value"

            # This is comment
            def option(self):
                return "Option"

            """
            # Create test file with test content.
           

# Generated at 2022-06-14 08:09:47.288657
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import os
    import sys
    import tempfile
    import unittest


    class TestLoadModuleFromFileLocation(unittest.TestCase):

        def setUp(self) -> None:
            self.env_var = "SANIC_TEST_ENV_VAR"
            self.env_var_value = "Some test value"
            os.environ[self.env_var] = self.env_var_value

        def test_resolve_env_var(self):
            path = "${" + self.env_var + "}/test"
            module = load_module_from_file_location(path)
            self.assertEqual(module.__file__, self.env_var_value + "/test")

        def test_bytes_location(self):
            tmp_file, tmp_path = temp

# Generated at 2022-06-14 08:09:59.608343
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import sys
    import tempfile

    location = "tests/config_for_unit_testing.py"
    module = load_module_from_file_location(location)

    assert module.function_defined_in_config() == "function_defined_in_config"

    with tempfile.NamedTemporaryFile() as file:
        file.write(b'CONSTANT = "constant_defined_in_file"')
        file.flush()

        module = load_module_from_file_location(file.name)
        assert module.CONSTANT == "constant_defined_in_file"

    assert "tests/config_for_unit_testing.py" in sys.modules

    os_environ["some_env_var"] = "some_path"


# Generated at 2022-06-14 08:10:14.942433
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import os
    import tempfile

    # create temp file
    test_file_content = "a = 5"
    file_name = "test_file"
    tmp_file_name = f"{file_name}.py"
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)

        # write content to the file
        tmp_file_path = (tmp_path / tmp_file_name).resolve()
        with open(tmp_file_path, "w+") as f:
            f.write(test_file_content)

        # load module from file
        os.environ["test_env_var"] = tmp_dir
        module = load_module_from_file_location(f"${test_env_var}/{tmp_file_name}")


# Generated at 2022-06-14 08:10:26.196296
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    try:
        import example_configs.config1
    except ImportError:
        pass

    # Check if module was loaded successful.
    some_module = load_module_from_file_location(
        "example_configs.config1"
    )

    # Test if modules equals
    assert example_configs.config1 == some_module
    # Test if attributes are equal.
    assert (
        example_configs.config1.somelist
        == some_module.somelist
    )

    # Check if file was loaded and substituted.
    some_module2 = load_module_from_file_location(
        "${example_config_path}",
        "${example_config_path}/config1.py"
    )
    assert example_configs.config1 == some_module2



# Generated at 2022-06-14 08:10:39.365363
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    def test_env_variable_expansion():
        import tempfile

        with tempfile.TemporaryDirectory() as temp_dir_1, tempfile.TemporaryDirectory() as temp_dir_2:
            config_file_path = Path(temp_dir_1) / "config.py"
            config_file_path.write_text("CONFIG_VAR = 1")

            os_environ["TEMP_DIR"] = temp_dir_2

            config = load_module_from_file_location(
                "${TEMP_DIR}/config.py", config_file_path
            )

            assert config.CONFIG_VAR == 1

    def test_load_string():
        config = load_module_from_file_location("sanic.app")

        assert hasattr(config, "Sanic")


# Generated at 2022-06-14 08:10:51.021377
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import os
    import inspect
    import traceback
    from . import test_module_name
    from . import test_module_name_with_env_var

    assert all(
        [
            inspect.ismodule(test_module_name),
            # test_module_name.__name__.endswith(".test_module_name"),
            test_module_name.some_config_parameter == 5,
            test_module_name.some_config_parameter2 == "some_config_parameter2",  # noqa
        ]
    ), traceback.format_exc()


# Generated at 2022-06-14 08:10:56.366679
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    tmpdir = Path(__file__).parent.parent / "examples" / "tmpdir"
    if not tmpdir.exists():
        tmpdir.mkdir()

    name = "some_module_name"
    filename = "some_file_name.py"
    module_file_path = tmpdir / filename

# Generated at 2022-06-14 08:11:08.632342
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # A) file path string
    some_module = load_module_from_file_location(
        "tests/sanic/config_example.py"
    )
    assert hasattr(some_module, "CONFIG")
    assert some_module.CONFIG["TEST_KEY"] == "TEST_VALUE"

    # B) bytes of file path string
    some_module = load_module_from_file_location(
        "tests/sanic/config_example.py".encode()
    )

    assert hasattr(some_module, "CONFIG")
    assert some_module.CONFIG["TEST_KEY"] == "TEST_VALUE"

    # C) pathlib Path object

# Generated at 2022-06-14 08:11:19.822560
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """
    Validate that load_module_from_file_location works properly with:
    - file paths with environment variables
    - with bytes type locations
    - with ascii encoded bytes type locations
    """
    import os

    # Arbitrary environment variable to be tested.
    # Make sure that it doesn't exist in environment.
    os_environ_key = "TEST_KEY"
    assert os_environ_key not in os.environ.keys()

    # Add the environment variable to the environment
    os.environ[os_environ_key] = "/tmp"

    # Correct call with environment variable
    assert "/tmp" == load_module_from_file_location("${%s}/test.py" % os_environ_key).__file__  # noqa

    # Invalid call with environment variable

# Generated at 2022-06-14 08:11:26.954393
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    cur_path = Path(__file__).resolve().parent.joinpath("data")
    config_file_name = "config_example.py"
    config_file_path = cur_path.joinpath(config_file_name).as_posix()
    assert "config_example" in load_module_from_file_location(config_file_path)

# Generated at 2022-06-14 08:11:34.886329
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import sys
    from unittest.mock import patch
    from unittest.mock import MagicMock

    if sys.version_info >= (3, 7):
        from importlib.metadata import PathMetadata
        from importlib.resources import read_text
        from importlib.resources import _finders as finders

        class _Loader:
            def __init__(self, module_name, metadata):
                self.metadata = metadata
                self.module_name = module_name

            def create_module(self, spec):
                return self.module

            def exec_module(self, module):
                module.__file__ = self.metadata.path
                exec(read_text(self.metadata, "config.py"), module.__dict__)

        #------------------------------
        # Pre-test environment mockings

# Generated at 2022-06-14 08:11:46.206572
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    import tempfile

    # 1) Use to create test config file with environment variable
    #    in format ${some_env_var} in location parameter.
    def use_env_var_in_location(location):
        # A) Create test config file.
        test_config_file = tempfile.NamedTemporaryFile(delete=False)
        test_config_file.write(b"TEST_KEY = 1")
        test_config_file.close()

        # B) Define ${some_env_var} in environment.
        some_env_var = "SOME_ENV_VAR"
        os_environ[some_env_var] = str(Path(test_config_file.name).parent)

        # C) Call location parameter with ${some_env_var}
        #    and test

# Generated at 2022-06-14 08:12:02.041952
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import os

    def clean_up():
        del os.environ["D_FOO"]
        os.remove("d.py")

    try:
        os.environ["D_FOO"] = "d.py"
        with open("d.py", "w") as d_module:
            d_module.write("FOO = 'FOO'")
        assert (
            load_module_from_file_location("${D_FOO}").FOO == "FOO"
        ), "Environment variables not resolved in location"
    finally:
        clean_up()

# Generated at 2022-06-14 08:12:15.694707
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    try:
        import configparser
    except ImportError:
        from backports import configparser

    from os import environ, path

    from sanic.config import Config

    location = "tests/fixtures/py_config/basic.py"
    assert isinstance(
        load_module_from_file_location(location), types.ModuleType
    )

    location = "tests/fixtures/py_config/basic_with_env_var.py"
    environ["some_env_var"] = "some_val"
    assert isinstance(
        load_module_from_file_location(location), types.ModuleType
    )
    del environ["some_env_var"]

    location = "some_broken_module_name"

# Generated at 2022-06-14 08:12:23.344222
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    def create_file_with_content(content, tmp_path):
        path = tmp_path / "blah.py"
        path.write_text(content)
        return str(path)

    def check_module_loaded_correctly(file_content, module_name, tmp_path):
        location = create_file_with_content(file_content, tmp_path)
        loaded_module = load_module_from_file_location(location)
        assert module_name in sys.modules

        assert loaded_module.test_value == 42

    def test_module_finally_deleted(module_name):
        del sys.modules[module_name]

    def check_module_exception(file_content, tmp_path):
        location = create_file_with_content(file_content, tmp_path)
       

# Generated at 2022-06-14 08:12:36.028866
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa

    import logging
    import tempfile

    config_str = """
    LOGGING_LEVEL = logging.CRITICAL
    USERNAME = "user"
    LOGGING_LEVEL_FALLBACK = logging.CRITICAL
    PASSWORD = "password"
    """

    logging_level = logging.CRITICAL
    logging_level_fallback = logging.CRITICAL

    def _check_module_attrs(module):

        assert module.LOGGING_LEVEL == logging_level
        assert module.LOGGING_LEVEL_FALLBACK == logging_level_fallback
        if hasattr(module, "PASSWORD"):
            assert module.PASSWORD == "password"
        if hasattr(module, "USERNAME"):
            assert module.USERNAME == "user"

   

# Generated at 2022-06-14 08:12:39.810133
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Make sure that configuration from a file is loaded properly"""
    from tempfile import NamedTemporaryFile

    with NamedTemporaryFile("w", prefix="sanic_", suffix=".py") as f:
        f.write("SOME_CONSTANT = 'SOME_CONSTANT_VALUE'")
        f.flush()
        module = load_module_from_file_location(f.name)
    assert module.SOME_CONSTANT == "SOME_CONSTANT_VALUE"

# Generated at 2022-06-14 08:12:52.273015
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    os_environ["SANIC_TEST_VAR_1"] = "some_val_1"
    os_environ["SANIC_TEST_VAR_2"] = "some_val_2"

    class SomeClass:
        def __init__(self):
            self.some_attr = None

    # A) Get module path
    curr_path = Path(__file__)
    parent_path = curr_path.parent.resolve()
    module_path = parent_path / "test_file.py"

    # B) Load module from module path (where the file contains `some_var = 1`)
    loaded_module = load_module_from_file_location(module_path)

    # C) Assert it is the same module we imported by importlib.
    assert loaded_module is test_

# Generated at 2022-06-14 08:13:02.539703
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    import tempfile


# Generated at 2022-06-14 08:13:14.934837
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    # A) Check if location contains any environment variables
    #    in format ${some_env_var}.
    assert "some_env_var" in re_findall(r"\${(.+?)}", "${some_env_var}")

    # B) Check these variables exists in environment.
    assert set(["SOME_ENV_VAR"]).difference(os_environ.keys()) == set()

    assert str_to_bool("Yes")
    assert str_to_bool("True")
    assert not str_to_bool("false")

    # C) Substitute them in location.

# Generated at 2022-06-14 08:13:26.503596
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # Test A)
    location = Path("/some/path/to/some_module/some_module_name.py")
    assert load_module_from_file_location(location)
    assert load_module_from_file_location(str(location))

    # Test B)
    location = "/some/path/to/another_module/another_module_name"
    assert load_module_from_file_location(location)
    assert load_module_from_file_location(str(location))

    # Test C)
    location = b"/some/path/to/another_module/another_module_name"
    assert load_module_from_file_location(location, encoding="utf8")
    assert load_module_from_file_location(
        location, encoding="utf8"
    )  # Test for

# Generated at 2022-06-14 08:13:38.716772
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    def a_func():
        pass

    def a_class():
        pass

    module = load_module_from_file_location(__file__)
    assert module.a_func is a_func
    assert module.a_class is a_class

    module = load_module_from_file_location(__file__.encode("utf8"))
    assert module.a_func is a_func
    assert module.a_class is a_class

    module = load_module_from_file_location(Path(__file__))
    assert module.a_func is a_func
    assert module.a_class is a_class

    module = load_module_from_file_location("./test_helpers")
    assert module.test_load_module_from_file_location is test_load_

# Generated at 2022-06-14 08:13:54.988155
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from .constants import TEST_DIR
    from .utils import get_test_config_path

    # assert
    # 1) load module from path/to/file.py

    module = load_module_from_file_location(get_test_config_path())
    assert set(dir(module)).issuperset({"TEST_CONFIG_KEY", "TEST_CONFIG_VALUE"})

    # 2) load module from directory

    module = load_module_from_file_location(TEST_DIR)
    assert set(dir(module)).issuperset({"TEST_CONFIG_KEY", "TEST_CONFIG_VALUE"})

    # 3) load module from non existing file/dir
    #    and catch the errors

    from datetime import datetime

    from sanic.exceptions import LoadFileError



# Generated at 2022-06-14 08:14:08.135339
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import shutil
    import os
    module_name = "test_module_name"
    file_name = "test_file_name"
    os_environ["test_env_var"] = "test_env_var_value"
    with tempfile.TemporaryDirectory() as tmp_dir:
        module_path = os.path.join(tmp_dir, file_name)
        with open(module_path + ".py", "w") as module:
            module.write("name = '{}'".format(module_name))
        module = load_module_from_file_location(module_path)
        assert module.name == module_name

        module_path = os.path.join(tmp_dir, file_name)
        with open(module_path + ".pyc", "wb") as module:
            module

# Generated at 2022-06-14 08:14:15.340670
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Test if function load_module_from_file_location will succesfully
    handle:

    1) file given as a path
    2) file given as a bytes
    3) file given as a string
    4) file given as a string with environment variables
    5) file extension is not .py
    6) file contains unicode literals
    7) file contains keyword arguments
    8) file contains non-keyword arguments
    9) file contains syntax error
    10) file does not exists
    """
    import sys
    import tempfile
    import os


# Generated at 2022-06-14 08:14:21.279953
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    os_environ["some_env_var"] = "some/path"
    some_module = load_module_from_file_location(
        "some_module_name",
        "/some/path/${some_env_var}",
        submodule_search_locations=[],
    )
    assert some_module.__name__ == "some_module_name"

# Generated at 2022-06-14 08:14:27.833082
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    import_path = "random_module.my_name"
    location = f"/tmp/{import_path.replace('.', '/')}.py"

    # A) Create folder structure and file
    Path(location).parent.mkdir(parents=True, exist_ok=True)

# Generated at 2022-06-14 08:14:37.775939
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    assert load_module_from_file_location("os").__name__ == "os"  # dynamic import
    assert load_module_from_file_location(
        "os"
    ).__file__ == "os"  # dynamic import with file-like syntax

    # Load dynamic import with file-like syntax
    assert load_module_from_file_location("os/$PATH").__name__ == "os"

    assert (  # Load dynamic import with file-like syntax
        load_module_from_file_location("os/$PATH").__file__ == "os"
    )

    assert load_module_from_file_location(Path("os")).__name__ == "os"  # dynamic import

    assert (
        load_module_from_file_location(Path("os")).__file__ == "os"
    )  #

# Generated at 2022-06-14 08:14:48.442405
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import tempfile
    import os
    import shutil
    import pytest

    config_path = os.path.abspath(
        os.path.dirname(os.path.realpath(__file__)) + "/../../examples/handler"
    )
    tmp_folder = tempfile.gettempdir()

    # A) Check if function loads module from path
    assert load_module_from_file_location(
        config_path + "/helloworld.py"
    ).__name__ == "helloworld"

    # B) Check if function loads module from path containing
    #    env variable which is not set.
    with pytest.raises(LoadFileException):
        load_module_from_file_location(config_path + "/env_vars/${SOME_VAR}/app")

    #

# Generated at 2022-06-14 08:14:55.461951
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    os_environ["CONFIG_DIR"] = str(Path(__file__).parent.absolute())
    os_environ["CONFIG_FILE"] = "config_for_testing.py"
    config = load_module_from_file_location(
        "${CONFIG_DIR}/${CONFIG_FILE}",
        str(Path(__file__).parent.absolute()),
    )
    assert config.TEST == "test"



# Generated at 2022-06-14 08:15:07.975469
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    import tempfile

    # A) Test a simple file which is brought with
    #    library in 'tests/config' directory.

    # A.1) getting module without extension
    module = load_module_from_file_location("tests.config", "config")
    assert getattr(module, "test_attr") == "test_attr_value"

    # A.2) getting module with extension
    module = load_module_from_file_location("tests.config", "config.py")
    assert getattr(module, "test_attr") == "test_attr_value"

    # B) Test a file in arbitrary directory

    # B.1) Create an arbitrary directory
    tmp_dir_location = tempfile.mkdtemp()

    # B.2) Create a temp file with config.
    #      Note that I can use Path

# Generated at 2022-06-14 08:15:20.507330
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    from os import environ, path
    from unittest import mock

    from tempfile import NamedTemporaryFile

    from .server import Sanic
    from .config import Config
    from .settings import (
        LOGO,
        LOGO_SANIC_LABEL,
        LOGO_TITLE_START,
        LOGO_TITLE_END,
        LOGO_FORMAT,
    )

    # A) Test for string as location parameter.

    # A.1) Without environment variable in location path.

    # A.1.1) With ".py" in location path.
    app = Sanic(
        "test_with_load_module_from_file_location_str_A1_1"
    )  # type: Sanic


# Generated at 2022-06-14 08:15:39.355345
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    TEST_MODULE_FILE_NAME = "module_for_module_loading_test.py"
    TEST_MODULE_FILE_PATH = Path(__file__).parent / TEST_MODULE_FILE_NAME

    loaded_module = load_module_from_file_location(TEST_MODULE_FILE_PATH)
    assert loaded_module.TEST_VARIABLE is True

    loaded_module = load_module_from_file_location(str(TEST_MODULE_FILE_PATH))
    assert loaded_module.TEST_VARIABLE is True

    loaded_module = load_module_from_file_location(bytes(TEST_MODULE_FILE_PATH))
    assert loaded_module.TEST_VARIABLE is True

# Generated at 2022-06-14 08:15:48.862167
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # Check that we can load from path and from location
    assert (
        load_module_from_file_location(
            os.path.dirname(__file__) + "/test_settings.py"
        ).TEST_KEY
        == "test_value"
    )
    assert (
        load_module_from_file_location("test_settings")
        .TEST_KEY == "test_value"
    )
    # Check that load module from location after we change folder
    current_dir = os.getcwd()
    os.chdir(os.path.dirname(__file__))
    assert (
        load_module_from_file_location("test_settings")
        .TEST_KEY == "test_value"
    )
    os.chdir(current_dir)



# Generated at 2022-06-14 08:16:02.213178
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import pytest
    from pathlib import Path
    import os

    def _assert_config_loaded(
        location: Union[bytes, str, Path],
        expected_config: types.ModuleType,
        *args,
        **kwargs,
    ):
        config = load_module_from_file_location(
            location, *args, **kwargs
        )
        assert config.__dict__ == expected_config.__dict__

    EXPECTED_CONFIG = types.ModuleType("config")
    EXPECTED_CONFIG.CONFIG_VAR1 = 1
    EXPECTED_CONFIG.CONFIG_VAR2 = "string"

    # UNIT TESTS

    # A) STRING TYPE
    # 1.1) load file by name
    config_file_name = Path(__file__).parent

# Generated at 2022-06-14 08:16:15.750663
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Test for the helpers.load_module_from_file_location function."""
    from os import environ as os_environ
    from os import remove as os_remove
    from os import mkdir as os_mkdir
    from shutil import rmtree as shutil_rmtree

    from pathlib import Path as pathlib_Path

    from tempfile import NamedTemporaryFile as tempfile_NamedTemporaryFile
    from tempfile import TemporaryDirectory as tempfile_TemporaryDirectory

    import pytest

    # A) Byte compatible:

    # Good path:
    location_byte_str = b"location_byte_str"
    with tempfile_TemporaryDirectory() as tmp_dir:
        location_byte_str_path = pathlib_Path(tmp_dir) / location_byte_str
        location_byte_str_path

# Generated at 2022-06-14 08:16:26.866463
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # Test if function loads module provided as a path.
    assert load_module_from_file_location(
        Path(__file__).parent / "test_loader.py"
    ).TEST_VARIABLE == "test_value"

    # Test if function loads module provided as a string.
    assert load_module_from_file_location(
        str(Path(__file__).parent / "test_loader.py")
    ).TEST_VARIABLE == "test_value"

    # Test if function loads module provided as a bytes.
    assert load_module_from_file_location(
        str(Path(__file__).parent / "test_loader.py").encode("utf8")
    ).TEST_VARIABLE == "test_value"

    # Test if function is capable of using environment variables.

# Generated at 2022-06-14 08:16:33.340456
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from os import environ

    environ["TEST_ENVIRONMENT_VARIABLE"] = "test"
    test_module = load_module_from_file_location(
        "config.test_module", "tests/test_config/test_module.py"
    )
    assert test_module.MODULE_VARIABLE == "test"
    del environ["TEST_ENVIRONMENT_VARIABLE"]
    assert load_module_from_file_location.__name__ == "load_module_from_file_location"
    assert load_module_from_file_location.__doc__
    assert test_module.__file__
    assert test_module.__name__ == "config.test_module"

# Generated at 2022-06-14 08:16:46.518113
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # pylint: disable=import-outside-toplevel
    import tempfile

    # Test 1:
    tmp_dir = tempfile.TemporaryDirectory(prefix="sanic-test-")
    tmp_dir_path = Path(tmp_dir.name)
    tmp_file_path = Path(tmp_dir_path, "test_load_module_from_file_location")
    tmp_file_path.write_text(
        "DUMMY_CONST = 'dummy value'"
    )

    test_module = load_module_from_file_location(tmp_file_path)
    assert test_module.DUMMY_CONST == 'dummy value'

    # Test 2:
    os_environ["DUMMY_ENV_VAR_NAME"] = str(tmp_file_path)
   

# Generated at 2022-06-14 08:16:59.328358
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import shutil
    import tempfile
    from os import environ, path

    # A) Check if function raises LoadFileException in case:
    #    1) Any of the environment variables passed in location argument
    #       is not defined in environment.
    #    2) Location is not Path or path like string or string with $
    #       notations.
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)

        # 1) Any of the environment variables passed in location argument
        #    is not defined in environment.
        os_environ["sanic_env_variable"] = "some_value"
        location = str(tmpdir / "some_file")
        open(location, "w").close()

        with pytest.raises(LoadFileException):
            load_module_from_file_

# Generated at 2022-06-14 08:17:10.522388
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    import pytest
    import os
    import tempfile

    try:
        some_env_var = os.environ["some_env_var"]
        del os.environ["some_env_var"]
        assert "some_env_var" not in os.environ.keys()
    except KeyError:
        some_env_var = None
        pass

    with tempfile.NamedTemporaryFile("w", suffix=".py") as temp_file:
        temp_file.write("a = {'a': 1}")
        temp_file.seek(0)
        module = load_module_from_file_location(temp_file.name)
        assert hasattr(module, "a")


# Generated at 2022-06-14 08:17:22.199916
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # Check if module loaded as expected.
    mod = load_module_from_file_location("fixtures/sanic/configs/tst_cfg.py")
    assert mod.foo == "bar"

    # Check if function raise error for invalid configuration.
    with pytest.raises(PyFileError):
        load_module_from_file_location("fixtures/sanic/configs/invalid.py")

    # Check if function raise error for file not found.
    with pytest.raises(LoadFileException):
        load_module_from_file_location("some_invalid_file_name.py")

    # Check if function raise error for environment variable not set.
    with pytest.raises(LoadFileException):
        load_module_from_file_location("${invalid}")

    # Check if function

# Generated at 2022-06-14 08:17:40.006526
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # A) Check if location contains any environment variables
    #    in format ${some_env_var}.
    os_environ["some_env_var"] = "some_val"

    # B) Check these variables exists in environment.
    # C) Substitute them in location.
    result = load_module_from_file_location(
        "${some_env_var}"
    )
    assert type(result).__name__ == "str"
    assert result == "some_val"

    # A) Check if location contains any environment variables
    #    in format ${some_env_var}.
    # B) Check these variables exists in environment.
    # C) Substitute them in location.
    result = load_module_from_file_location(
        "bytes(${some_env_var}, 'utf8')"
    )

# Generated at 2022-06-14 08:17:52.200762
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    """Check if function load_module_from_file_location works correctly."""
    import pytest
    from os import environ, pathsep
    from pathlib import Path
    import tempfile

    # 1. Check simple case - load_module_from_file_location(
    #    'some_module_name', '/some/path/to/some_module.py'
    # ).
    test_module_location = Path(
        __file__
    ).parent / "test_module_for_load_module_from_file_location.py"
    test_module = load_module_from_file_location(test_module_location)
    assert test_module.__version__ == "1.0"
    assert test_module.config_key == "config value"

    # 2. Check if load_module

# Generated at 2022-06-14 08:18:06.090050
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # 1.
    test_module_path = Path(__file__).parent / "test_utils.py"
    test_module = load_module_from_file_location(test_module_path)
    assert test_module.__name__ == "test_utils"
    assert test_module.__file__ == str(test_module_path)
    # 2.
    test_module = load_module_from_file_location(str(test_module_path))
    assert test_module.__name__ == "test_utils"
    assert test_module.__file__ == str(test_module_path)
    # 3.
    test_module = load_module_from_file_location(bytes(test_module_path))
    assert test_module.__name__ == "test_utils"
    assert test_module