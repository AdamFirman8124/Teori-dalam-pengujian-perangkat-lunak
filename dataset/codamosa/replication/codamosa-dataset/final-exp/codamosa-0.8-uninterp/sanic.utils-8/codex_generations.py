

# Generated at 2022-06-14 08:08:26.417002
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import os
    import sys

    # Let's create a temporary file that we can copy
    temp_file = "temp_file.py"
    with open(temp_file, "w+") as file:
        file.write("DEBUG = True")
    sys.path.insert(0, os.path.abspath(os.getcwd()))  # to avoid ValueError

    module_from_file_location = load_module_from_file_location(temp_file)

    assert module_from_file_location.DEBUG is True

    os.remove(temp_file)

    os.environ["temp_module_env"] = "temp_module_env"
    temp_file = "${temp_module_env}/temp_file.py"

    module_from_file_location = load_module_from_file_location

# Generated at 2022-06-14 08:08:39.252548
# Unit test for function str_to_bool
def test_str_to_bool():
    conf = [
        ("y", True),
        ("yes", True),
        ("YES", True),
        ("yep", True),
        ("yup", True),
        ("t", True),
        ("true", True),
        ("on", True),
        ("enable", True),
        ("enabled", True),
        ("1", True),
        ("n", False),
        ("no", False),
        ("f", False),
        ("false", False),
        ("off", False),
        ("disable", False),
        ("disabled", False),
        ("0", False),
    ]
    for k, v in conf:
        assert str_to_bool(k) == v

# Generated at 2022-06-14 08:08:51.547577
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Tests load_module_from_file_location()'s functionalities"""

    location = os.path.abspath(os.path.join(__file__, "..", "module1.py"))
    module = load_module_from_file_location(location)

    # A) Test if module is loaded and imported properly
    assert module is not None
    assert module.CONFIG_VAR == "config value"
    # Test if module file is loaded properly
    assert module.__file__ == location

    # B) Test if location can be a path.Path instance
    module = load_module_from_file_location(Path(location))
    assert module is not None

    # C) Test if location can be a bytes instance
    location_bytes = location.encode()

# Generated at 2022-06-14 08:09:00.218286
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """
    Tests the load_module_from_file_location function
    """
    # config = load_module_from_file_location("tests/test_config.py")
    os_environ["TEST_CONFIG_FILE_LOCATION"] = str(Path("tests/test_config.py"))

    config = load_module_from_file_location(
        "${TEST_CONFIG_FILE_LOCATION}",
    )

    assert hasattr(config, "TEST_PORT")
    assert config.TEST_PORT == 8000
    assert hasattr(config, "TEST_HOST")
    assert config.TEST_HOST == "127.0.0.1"
    assert hasattr(config, "TEST_BOOLEAN")
    assert config.TEST_BOOLEAN

    del os

# Generated at 2022-06-14 08:09:09.366152
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import pytest
    import tempfile
    import unittest
    import sys
    from os import environ

    def mocked_file_loader(
        mocked__mod_spec: types.ModuleType,
        mocked__file_location: str,
        *args,
        **kwargs
    ):
        """Mock for importlib.util.module_from_spec.

        It should mock the importlib.util.module_from_spec
        behaviour, but we don't want to mock the rest of
        behaviour of the module_from_spec.
        """
        mocked__mod_spec.loader.exec_module(
            mocked__mod_spec
        )  # type: ignore

    mocked_file_loader.__name__ = "module_from_spec"

# Generated at 2022-06-14 08:09:22.727228
# Unit test for function str_to_bool
def test_str_to_bool():
    assert str_to_bool("1")
    assert str_to_bool("yes")
    assert str_to_bool("t")
    assert str_to_bool("true")
    assert str_to_bool("on")
    assert str_to_bool("enable")
    assert str_to_bool("enabled")
    assert str_to_bool("y")
    assert str_to_bool("yep")
    assert str_to_bool("yup")
    assert not str_to_bool("0")
    assert not str_to_bool("no")
    assert not str_to_bool("false")
    assert not str_to_bool("off")
    assert not str_to_bool("disable")
    assert not str_to_bool("disabled")
    assert not str_to_bool("f")

# Generated at 2022-06-14 08:09:32.373868
# Unit test for function str_to_bool
def test_str_to_bool():
    for true_string in {
        "y",
        "yes",
        "yep",
        "yup",
        "t",
        "true",
        "on",
        "enable",
        "enabled",
        "1",
    }:
        assert str_to_bool(true_string) == True

    for false_string in {
        "n",
        "no",
        "f",
        "false",
        "off",
        "disable",
        "disabled",
        "0",
    }:
        assert str_to_bool(false_string) == False

    try:
        str_to_bool("")
    except ValueError:
        assert True
    else:
        assert False


# Generated at 2022-06-14 08:09:41.884428
# Unit test for function str_to_bool
def test_str_to_bool():  # noqa
    try:
        str_to_bool(1)
    except TypeError:
        pass
    assert str_to_bool("true") is True
    assert str_to_bool("TRUE") is True
    assert str_to_bool("yes") is True
    assert str_to_bool("YeS") is True
    assert str_to_bool("on") is True
    assert str_to_bool("ON") is True
    assert str_to_bool("yep") is True
    assert str_to_bool("YEP") is True
    assert str_to_bool("yup") is True
    assert str_to_bool("YUP") is True
    assert str_to_bool("t") is True
    assert str_to_bool("T") is True
    assert str_to_bool("1")

# Generated at 2022-06-14 08:09:53.087367
# Unit test for function str_to_bool
def test_str_to_bool():
    assert str_to_bool("y") is True
    assert str_to_bool("yes") is True
    assert str_to_bool("yep") is True
    assert str_to_bool("yup") is True
    assert str_to_bool("t") is True
    assert str_to_bool("true") is True
    assert str_to_bool("on") is True
    assert str_to_bool("enable") is True
    assert str_to_bool("enabled") is True
    assert str_to_bool("1") is True

    assert str_to_bool("n") is False
    assert str_to_bool("no") is False
    assert str_to_bool("f") is False
    assert str_to_bool("false") is False
    assert str_to_bool("off") is False

# Generated at 2022-06-14 08:10:02.264936
# Unit test for function str_to_bool
def test_str_to_bool():
    assert str_to_bool("y")
    assert str_to_bool("Y")
    assert str_to_bool("yes")
    assert str_to_bool("Yes")
    assert str_to_bool("t")
    assert str_to_bool("T")
    assert str_to_bool("true")
    assert str_to_bool("True")
    assert str_to_bool("on")
    assert str_to_bool("On")
    assert str_to_bool("1")
    assert not str_to_bool("1a")
    assert not str_to_bool("a")
    assert not str_to_bool("2")
    assert not str_to_bool("0000")
    assert not str_to_bool("100")
    assert not str_to_bool("n")
    assert not str_

# Generated at 2022-06-14 08:10:17.165371
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    test_cases = [
        (
            "sanic.config",
            "/some/path/${does_not_exist}",
            None,
        ),
        (
            "sanic.config",
            "/some/path/${does_not_exist}",
            {"does_not_exist": "this_does_exist"},
        ),
        (
            "sanic.config",
            "/some/path/${PWD}",
            {"PWD": "this_does_exist"},
        ),
        (
            "sanic.config",
            (b"/some/path/${PWD}".decode("ascii"), "utf8"),
            {"PWD": "this_does_exist"},
        ),
    ]

    for test_case in test_cases:
        args, location, kwargs

# Generated at 2022-06-14 08:10:27.338202
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from .util import temporary_file, temporary_directory
    from .exceptions import SanicConfigNotFound
    # A) Test, when location contains environment variables
    os_environ["some_env_var"] = "some_value"
    with temporary_file() as config_file:
        conf_file_name = config_file.name
        location = f"/some/path/{conf_file_name}"
        # 1) Create file with some configuration
        config_file.write(
            b"""
            url = "http://www.example.com"
            port = 80
            """
        )
        config_file.seek(0)

        module = load_module_from_file_location(
            "${some_env_var}" + location,
        )

# Generated at 2022-06-14 08:10:36.675104
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    test_module = load_module_from_file_location(
        "/home/leonardo/PycharmProjects/sanic-toolkit/sanic_toolkit/tools/config_examples/test.py"
    )
    assert test_module.Foo == "foo_value"
    assert test_module.BAR == "bar value"
    assert test_module.Spam == "spam value"
    assert test_module.HAM == "ham value"
    assert test_module.EGGS == "eggs value"


# Generated at 2022-06-14 08:10:48.707380
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from types import ModuleType
    from pathlib import Path

    file_location_1 = Path(__file__)
    loaded_module_1 = load_module_from_file_location(file_location_1)
    assert isinstance(loaded_module_1, ModuleType)

    file_location_2 = Path(__file__).parent / "test_utils.py"
    loaded_module_2 = load_module_from_file_location(file_location_2)
    assert isinstance(loaded_module_2, ModuleType)

    # Test with environment variable
    file_location_3 = (
        Path(__file__).parent / "${HOME}" / "test_utils.py"
    )
    loaded_module_3 = load_module_from_file_location(file_location_3)

# Generated at 2022-06-14 08:10:55.143915
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # Create a module with a variable in it, then load it and check it
    location = "/tmp/some_module.py"
    base_module = """\
module_variable = 1
"""
    with open(location, "w") as module:
        module.write(base_module)

    module = load_module_from_file_location(location)

    assert module.module_variable == 1


# Generated at 2022-06-14 08:11:06.922982
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import os

    # A) Check exception when environment variable is not defined.
    try:
        load_module_from_file_location(
            "some_module_name",
            "/some/path/${not_defined_env_var}",
        )
    except LoadFileException as e:
        assert (
            str(e)
            == "The following environment variables are not set: not_defined_env_var"
        )

    # B) Check if substitution occures.

# Generated at 2022-06-14 08:11:15.467360
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa: D103

    class SomeException(Exception):
        pass

    location = "tests/test_configs/config_with_env_vars.py"
    os_environ.update({"TEST_VARIABLE": "universe"})
    try:
        module = load_module_from_file_location(location)
    except LoadFileException as e:
        raise SomeException(e) from e
    assert module.SOME_VARIABLE == "universe"



# Generated at 2022-06-14 08:11:29.550136
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    os_environ["SOME_ENV"] = "SOME_ENV_VALUE"

    module = load_module_from_file_location(
        "test_load_module_from_file_location_test_module",
        __file__
        [
            :-
            len(
                "tests/unit/utils/test_load_module_from_file_location.py"
            )
        ]
        + "tests/unit/utils/test_load_module_from_file_location_test_module.py",
    )
    assert module.some_env == "SOME_ENV_VALUE"


# Generated at 2022-06-14 08:11:35.848616
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    def first_test():
        # 1. Test when location is in string format,
        #    has dots, slashes and file with .py extension.
        #    No environment variables in location.

        location = "some/path/to/some_module.py"
        name = location.split("/")[-1].split(".")[0]
        _mod_spec = spec_from_file_location(name, location)
        module = module_from_spec(_mod_spec)
        _mod_spec.loader.exec_module(module)  # type: ignore

        assert load_module_from_file_location(location) == module


# Generated at 2022-06-14 08:11:46.636392
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import tempfile
    import random

    name_chars = "abcdefghijklmnoprstuvwxyzABCDEFGHIJKLMNOPRSTUVWXYZ"


# Generated at 2022-06-14 08:12:01.746349
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import os

    open("config.py", "w").write(
        "a = 'config.py = ' + __file__ + ' = ' + os.environ.get('TAG', 'NoEnvVar')\n"
    )

    m1 = load_module_from_file_location("config")
    assert m1.a == "config.py = config.py = NoEnvVar"

    # Test passing Path
    m2 = load_module_from_file_location(Path("config.py"))
    assert m2.a == "config.py = config.py = NoEnvVar"

    # Test passing bytes parameter
    m3 = load_module_from_file_location(b"config.py")
    assert m3.a == "config.py = config.py = NoEnvVar"

    # Test

# Generated at 2022-06-14 08:12:08.914861
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import tempfile

    # Create a temporary file
    fd, config_path = tempfile.mkstemp(".py")
    os.close(fd)


# Generated at 2022-06-14 08:12:20.644921
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """
    Test for load_module_from_file_location.

    Works only if one of following environment variables is set:
        TEST_LOAD_MODULE_FROM_FILE_LOCATION_OK
        TEST_LOAD_MODULE_FROM_FILE_LOCATION_DOES_NOT_EXIST
    """
    NOT_SET_VALUE = "NOT_SET_VALUE"  # some not set value

    # A) Test that if module is not provided as full path and has only
    #    filename without extension will raise IOError.
    with pytest.raises(IOError):
        load_module_from_file_location("some_non_existing_module_name")

    # B) Test that if module is provided as full path and does not exists,
    #    raises IOError.

# Generated at 2022-06-14 08:12:33.657610
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import tempfile

    config_file_content = "SOME_VAR = 'SOME_VALUE'"
    temp_config_file = tempfile.NamedTemporaryFile()
    temp_config_file.write(config_file_content.encode())
    temp_config_file.flush()

    module = load_module_from_file_location(temp_config_file.name)
    assert module.SOME_VAR == "SOME_VALUE"

    # Deletes temporary file
    temp_config_file.close()

    import os
    import re

    os.environ["SOME_ENV_VAR"] = "SOME_VALUE"
    config_file_content = "SOME_VAR = '${SOME_ENV_VAR}'"
    temp_config_file = tempfile.NamedTem

# Generated at 2022-06-14 08:12:45.455635
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    assert load_module_from_file_location("./tests/test_utils/test_config.py")
    assert load_module_from_file_location(Path(__file__).parent / "test_config.py")
    assert load_module_from_file_location("tests/test_utils/test_config.py")

    # Test enviroment variable resolving
    os_environ["TEST_LOAD_MODULE_FROM_FILE_LOCATION"] = Path(__file__).parent
    assert (
        load_module_from_file_location(
            "${TEST_LOAD_MODULE_FROM_FILE_LOCATION}/test_config.py"
        )
        is not None
    )
    del os_environ["TEST_LOAD_MODULE_FROM_FILE_LOCATION"]

# Generated at 2022-06-14 08:12:50.723791
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    os.environ["some_env_var"] = "some_value"
    location = "/some/path/${some_env_var}/some_file.py"
    module = load_module_from_file_location(location)
    assert module.__file__ == "/some/path/some_value/some_file.py"



# Generated at 2022-06-14 08:13:01.674771
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    # A) Location is string
    # B) Env var in location
    #       1) Env var exists
    #       2) Env var does not exist
    # C) Location contains .py extension
    #       1) Location is absolute.
    #       2) Location is relative.
    # D) Location does not contain .py extension
    #       1) Location is absolute.
    #       2) Location is relative.

    class SomeClass:
        pass

    # A) Location is string

    def test_string(location):

        module = load_module_from_file_location(location)

        assert module.__name__ == "some_class"
        assert module.__file__ == location
        assert module.SomeClass == SomeClass

    test_string("some_class")
    test_string("some_class.py")

# Generated at 2022-06-14 08:13:13.919491
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from copy import deepcopy
    from io import StringIO
    from unittest import TestCase
    from unittest.mock import patch, mock_open

    from sanic import __version__ as sanic_version
    from sanic.helpers import load_module_from_file_location

    def get_test_configuration(
        configuration_name: str, configuration_str: str
    ):
        """Generates configuration file content
        and passes it as parameter in function load_module_from_file_location
        and returns loaded module.
        """

        # Make sure that we don't have any configuration with this name.
        if configuration_name in os_environ:
            os_environ.pop(configuration_name)


# Generated at 2022-06-14 08:13:24.004655
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from temporary.directory import TemporaryDirectory
    from os import environ as os_environ, pathsep

    # A) Test environment variable resolving.
    with TemporaryDirectory() as temp_dir:
        module_name = "test_load_module_from_file_location"
        test_env_var_name = "TEST_ENV_VAR_FOR_TEST_LOAD_MODULE_FROM_FILE_LOCATION"
        test_env_var_val = "test_env_var_val"
        os_environ[test_env_var_name] = test_env_var_val

        # 1) Test environment variable resolving from environment variables.
        module_path = f"{test_env_var_name}{pathsep}{temp_dir}/{module_name}.py"
        module = load_module_from

# Generated at 2022-06-14 08:13:36.825046
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    cwd = Path.cwd()
    try:
        # A) Check if location contains any environment variables
        #    in format ${some_env_var}.
        # B) Check these variables exists in environment.
        # C) Substitute them in location.
        os_environ["some_env_var"] = str(cwd)
        some_module = load_module_from_file_location(
            "some_module_name", "${some_env_var}/conftest.py"
        )
        assert some_module.__name__ == "some_module_name"
    finally:
        del os_environ["some_env_var"]

    # 1) Works good with Path objects.

# Generated at 2022-06-14 08:13:51.849611
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    config_path = Path(__file__).parent.joinpath("tests", "config.py")
    module = load_module_from_file_location(config_path)
    assert module.TEST == "1"
    module = load_module_from_file_location(config_path)
    assert module.TEST == "1"
    module = load_module_from_file_location(config_path)
    assert module.TEST == "1"



# Generated at 2022-06-14 08:14:04.245886
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    test_module_path = os.path.dirname(os.path.dirname(
        os.path.realpath(__file__))) + "/tests/unittests/conf_file.py"

    test_module = load_module_from_file_location(test_module_path)
    assert test_module.TEST_VAR == 'OK'

    test_module = load_module_from_file_location(Path(test_module_path))
    assert test_module.TEST_VAR == 'OK'

    os_environ['TEST_VAR'] = test_module_path
    test_module = load_module_from_file_location('${TEST_VAR}')
    assert test_module.TEST_VAR == 'OK'

# Generated at 2022-06-14 08:14:17.222022
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    # A) If location contains environment variables, they should be resolved.
    #    Also it should be possible to use Path() object as location, as well
    #    as string. Also location shouldn't be a python module, as it would be
    #    treated as a loading module by name.
    os_environ['some_env_var'] = '/path/to/some/file'

    m_1 = load_module_from_file_location(Path(__file__).parents[0] / "__init__.py") # noqa
    m_2 = load_module_from_file_location(os_environ['some_env_var'])
    assert m_1 is m_2

    # B) If location doesn't point to existing file, then IOError should be raised

# Generated at 2022-06-14 08:14:27.985417
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import tempfile

    # It should be able to load module with correct file path.
    with tempfile.NamedTemporaryFile(suffix=".py", mode="w+") as f:
        f.write("test_variable = 0")
        f.flush()
        assert load_module_from_file_location(f.name).test_variable == 0

    # It should throw LoadFileException if file does not exist.
    with pytest.raises(LoadFileException):
        load_module_from_file_location("som_file_that_does_not_exist")

    # It should throw IOError if file is not python file.

# Generated at 2022-06-14 08:14:36.395158
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import os
    import tempfile
    import shutil
    import pytest

    def _prepare_test_file(test_file_content):
        # Prepare temporary directory for testing.
        temp_dir = tempfile.TemporaryDirectory()
        os.mkdir(os.path.join(temp_dir.name, "test_folder"), mode=0o777)
        os.mkdir(os.path.join(temp_dir.name, "test_folder", "test_subfolder"), mode=0o777)
        # Write configuration file.
        temp_conf_file_path = os.path.join(
            temp_dir.name, "test_folder", "test_subfolder", "some_conf.py")
        with open(temp_conf_file_path, 'w') as temp_conf_file:
            temp_

# Generated at 2022-06-14 08:14:44.743344
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # A) Test for case when environment variable is in the beginnig.
    location = "${HOME}/some_file"
    assert load_module_from_file_location(location) is not None

    # B) Test for case when environment variable is in the middle.
    location = "/some/path/file/${HOME}"
    assert load_module_from_file_location(location) is not None

    # C) Test for case when environment variable is in the end.
    location = "/some/path/file/"
    assert load_module_from_file_location(location) is not None

# Generated at 2022-06-14 08:14:51.750038
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from os import environ as os_environ

    test_config_file_path = Path(
        os_environ["BASE_DIR"] + "/tests/test_utilities/test_config_file.py"
    )
    loaded_module = load_module_from_file_location(
        test_config_file_path,
        "/some/path/${TEST_INVALID_ENV_VAR}"
        if "TEST_INVALID_ENV_VAR" in os_environ
        else test_config_file_path,
    )

    assert loaded_module
    assert loaded_module.__name__ == "test_config_file"
    assert loaded_module.SOME_TEST_CONFIG_VAR == "Test config variable value"

# Generated at 2022-06-14 08:15:03.607048
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import tempfile
    import os

    test_fw_folder = os.path.dirname(os.path.realpath(__file__))
    test_fw_folder = os.path.join(test_fw_folder, "")
    test_file_path = test_fw_folder + "test_load_module_from_file_location.py"

    # Create file and write it for test:
    with open(test_file_path, "w") as f:
        f.write("test = True")

    # Test if file is created:
    assert os.path.exists(test_file_path) is True
    # Load file and assert:
    test_file_loaded = load_module_from_file_location(test_file_path)

# Generated at 2022-06-14 08:15:16.867196
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """
    The test is not really very good, because for it can pass
    and not be able to load the file.
    """
    # For testing we need to use the file that will definitely be created.
    # It is better to create it in the same directory, where it is the test.
    current_file_path = Path(__file__).parent.absolute()
    test_file_path = current_file_path / "load_module_from_file_location.py"

    # Add some environment variables for testing.
    os_environ["SOME_ENV_VAR_1"] = "some_env_var_1_value"
    os_environ["SOME_ENV_VAR_2"] = "some_env_var_2_value"

    # Add some content to the file and save it.
    file

# Generated at 2022-06-14 08:15:27.160614
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from os import environ
    from os.path import join, expanduser

    from pathlib import Path

    from pytest import raises

    tmp_path = Path(expanduser("~/tmp/test_load_module_from_file_location"))
    if not tmp_path.exists():
        tmp_path.mkdir()

    def create_module(content, encoding = "utf8"):
        """
        Create test module with given content.
        Returns path to created module.
        """

        test_module_path = tmp_path / str(uuid.uuid4())
        with test_module_path.open("wb") as test_module:
            test_module.write(content.encode(encoding))

        return test_module_path

    # Testing that load_module_from_file_location raises when can't

# Generated at 2022-06-14 08:15:44.490749
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from pathlib import Path
    from .config import test_config as expected
    from .config.test_config import a, b, c, e, f, g

    # Test with byte path
    module = load_module_from_file_location(b"test_config", "config", encoding="utf8")
    assert module
    assert isinstance(module.__file__, str)
    assert module.__file__.endswith("test_config.py")
    assert module.a == a and module.b == b and module.c == c and module.e == e

    # Test with byte path
    module = load_module_from_file_location(Path("test_config"), "config")
    assert module
    assert isinstance(module.__file__, str)

# Generated at 2022-06-14 08:15:57.451882
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    original_cwd = os.getcwd()
    os.chdir(os.path.dirname(__file__))

    # A) Check if location contains any environment variables
    #    in format ${some_env_var}.
    os.environ["some_env_var"] = "some_env_var"
    assert (
        load_module_from_file_location(
            f"${os.environ['some_env_var']}"
        ).__file__
        == os.path.basename(__file__)
    )

    # B) Check these variables exists in environment.
    with pytest.raises(LoadFileException):
        load_module_from_file_location("${some_env_var}_not_set")

    # C) Substitute them in location.

# Generated at 2022-06-14 08:16:07.386837
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import pathlib
    import os
    import shutil
    import tempfile
    import types as test_types

    temp_dir_path = os.path.join(tempfile.gettempdir(), "config_loader_test_")
    temp_dir = tempfile.TemporaryDirectory(temp_dir_path)

    # A) Testing when you give the location with existing file
    #    but without .py extension
    # A1) Testing when you give the location with existing file
    #     but without .py extension and without environment variables in it.
    path = pathlib.Path(temp_dir.name).joinpath("example.conf")
    path.touch()
    module = load_module_from_file_location(path)

    assert isinstance(module, test_types.ModuleType)

# Generated at 2022-06-14 08:16:18.232440
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from os import environ
    from tempfile import TemporaryDirectory, NamedTemporaryFile
    from pathlib import Path
    from shutil import copyfile

    # ==========================
    # | Preparation test data  |
    # ==========================

    # A) Prepare some environment variables required by tests.
    environ["PATHS_ENV_VAR"] = "/path/to/module"
    environ["PATHS_ENV_VAR2"] = "/path/to/"
    environ["PATHS_ENV_VAR3"] = "/"

    # B) Create object which represents configuration file.
    #    We'll copy it to temporary location later.
    CONFIG_FILE = "config.py"
    with open(CONFIG_FILE, "w") as file:
        file.write("some_config = True")

   

# Generated at 2022-06-14 08:16:31.472881
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    ROOT_PATH = Path(__file__).resolve().parent

    # A) Check loading from just a file name (expect raising LoadFileException)
    file_name = "empty_file.py"
    with pytest.raises(LoadFileException):
        load_module_from_file_location(file_name)

    # B) Check loading from just a path (expect raising LoadFileException)
    path = str(ROOT_PATH / "tests")
    with pytest.raises(LoadFileException):
        load_module_from_file_location(path)

    # C) Check loading from file with absolute path, without extension
    file_path = str(ROOT_PATH / "tests" / "file_for_import.py")
    module = load_module_from_file_location(file_path)
   

# Generated at 2022-06-14 08:16:42.208492
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import os
    import sys
    import tempfile

    # A) Test that loading module from file works.

    with tempfile.NamedTemporaryFile(
        mode="w", encoding="utf8", delete=False
    ) as test_module_bytes_file:
        module_name = "test_module_bytes"
        test_module_bytes_file.write(
            f'{module_name} = types.SimpleNamespace()\n'
            f'{module_name}.x = 1\n'
        )

    test_module_bytes_path = Path(test_module_bytes_file.name)

    # Load module from bytes file.
    test_module_bytes = load_module_from_file_location(
        test_module_bytes_path.read_bytes()
    )
    assert test_module_bytes

# Generated at 2022-06-14 08:16:50.784492
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from os import environ, makedirs, remove
    from os.path import join

    from tempfile import TemporaryDirectory

    from unittest.mock import patch

    from .test_configs import some_dict_module as some_module
    from .test_configs import EmptyModule


# Generated at 2022-06-14 08:17:02.723684
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from .test_config import load_module_from_file_location_test as load_module

    module = load_module(__file__, encoding="utf-8")
    assert module.__name__ == "sanic.config"

    module_byte_file = load_module(__file__.encode("utf-8"))
    assert module_byte_file.__name__ == "sanic.config"

    module_path = load_module(Path(__file__))
    assert module_path.__name__ == "sanic.config"

    os_environ["test_env_vart_var"] = __file__
    module_env_var = load_module("/test/${test_env_vart_var}")
    assert module_env_var.__name__ == "sanic.config"
    del os

# Generated at 2022-06-14 08:17:07.638269
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import tempfile
    import os

    def create_config_file(var_name, var_value):
        with tempfile.TemporaryDirectory() as tmpdirname:
            os.environ[var_name] = tmpdirname
            file_name = f"{tmpdirname}/test.py"

            with open(file_name, "w") as file:
                config_string = f"CONFIG='{var_value}'"
                file.write(config_string)

            return file_name

    def del_env_var(var_name):
        if var_name in os.environ:
            del os.environ[var_name]


# Generated at 2022-06-14 08:17:19.612970
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import os

    from unittest import TestCase, mock

    from sanic.helpers import load_module_from_file_location

    # A) Initialize some env variables
    os.environ["blah"] = "blah"
    os.environ["foo"] = "foo"
    os.environ["foobar"] = "foobar"


# Generated at 2022-06-14 08:17:30.661988
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    module = load_module_from_file_location(
        "${SANIC_TESTING_PATH}/fixtures/test_load_module_from_file_location.py"
    )
    assert module.test == 1

# Generated at 2022-06-14 08:17:41.475913
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    module_a = load_module_from_file_location(Path("module_a.py"), "tests/")
    assert module_a.a == 1
    module_b = load_module_from_file_location(Path("module_b.py"), "tests/")
    assert module_b.b == 1

    try:
        module_c = load_module_from_file_location(
            "module_a_with_syntax_error.py", "tests/"
        )
        assert False
    except BaseException:
        module_c = None

    assert module_c is None

    module_a_with_env_var = load_module_from_file_location(
        "${APP_CONFIG_DIR}/module_a.py"
    )
    assert module_a == module_a_with_env

# Generated at 2022-06-14 08:17:52.684509
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Tests load_module_from_file_location function."""
    import tempfile

    with tempfile.NamedTemporaryFile() as tmp:

        # Test valid case
        temp_file_name = tmp.name
        name = temp_file_name.split("/")[-1].split(".")[
            0
        ]  # get just the file name without path and .py extension
        tmp.write(b"some_value = 1; some_not_imported_value = 1\n")
        tmp.flush()
        module = load_module_from_file_location(tmp.name)
        assert module.some_value == 1
        assert module.__name__ == name

        # Test invalid case
        tmp.write(b"some_value=syntax_error\n")
        tmp.flush()

# Generated at 2022-06-14 08:17:59.934681
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    location = "/some/path/to/${PWD}/module.py"

    assert load_module_from_file_location(location).FOO == "bar"

    location = "/some/path/to/module.py"

    assert load_module_from_file_location(location).FOO == "bar"

    locat

# Generated at 2022-06-14 08:18:10.560803
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Test for :load_module_from_file_location"""
    from os.path import dirname, join

    curdir = dirname(__file__)
    test_file = join(curdir, "fixtures", "test_config.py")

    with open(test_file) as fp:
        mod = load_module_from_file_location(test_file)
        assert mod.TEST_KEY == 10

        mod = load_module_from_file_location(fp)
        assert mod.TEST_KEY == 10

        mod = load_module_from_file_location(test_file.encode())
        assert mod.TEST_KEY == 10