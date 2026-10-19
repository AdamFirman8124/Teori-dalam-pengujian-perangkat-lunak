

# Generated at 2022-06-14 08:08:26.808591
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    os_environ["SANIC_ENV_VAR"] = "dummy_value"
    # A) Will load module with name: somemodule.py
    #    And will put it in some/other/path
    os_environ["SANIC_ENV_VAR_2"] = "some/other/path"
    some_module = load_module_from_file_location(
        "somemodule.py", "/some/path/${SANIC_ENV_VAR_2}"
    )
    assert some_module.__name__ == "somemodule"
    assert some_module.__file__ == "/some/other/path/somemodule.py"

# Generated at 2022-06-14 08:08:39.403472
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Test for function load_module_from_file_location."""

    import_string = load_module_from_file_location
    assert import_string("json") is not None

    import_string = load_module_from_file_location
    assert import_string("os") is not None

    import_string = load_module_from_file_location
    assert import_string("os.path") is not None

    import_string = load_module_from_file_location
    assert import_string("os.path.join") is not None

    import_string = load_module_from_file_location
    assert import_string("os.path") is not None

    import_string = load_module_from_file_location
    assert import_string("os.path") is not None

    import_string = load_module_from

# Generated at 2022-06-14 08:08:47.104722
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    if "TEST_LOCATION" in os_environ.keys():
        test_location = os_environ["TEST_LOCATION"]
    else:
        test_location = os.path.dirname(__file__)

    test_config_name = "test_config"
    test_config_file_path = os.path.join(test_location, test_config_name + ".py")
    test_config_data = "TEST_CONFIG_DATA = True"

    with open(test_config_file_path, "w") as f:
        f.write(test_config_data)

    test_config = import_string("test_config.test_config")
    test_config_actual = load_module_from_file_location(test_location + "/test_config")


# Generated at 2022-06-14 08:08:53.456872
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # pylint: disable=missing-function-docstring

    # Check if function can load module from pathlib.Path
    location = Path(__file__)
    module = load_module_from_file_location(location)
    assert module is not None

    # Check if function can load module from os.PathLike
    try:
        from os import PathLike  # pylint: disable=no-name-in-module
    except ImportError:
        PathLike = None
    if PathLike:
        location = PathLike(__file__)
        module = load_module_from_file_location(location)
        assert module is not None

    # Check if function can load module from bytes
    module = load_module_from_file_location(
        location.encode(), encoding=location.suffix[1:]
    )
   

# Generated at 2022-06-14 08:09:05.841385
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    os_environ["SOME_ENV_VAR"] = f"{Path(__file__).parent.parent}/examples"
    config = load_module_from_file_location(
        "config",
        "${SOME_ENV_VAR}/app_with_config/config.py",
    )
    assert config.CONFIG == "config"
    del os_environ["SOME_ENV_VAR"]

    config = load_module_from_file_location(
        "config", "${NOT_DEF_ENV_VAR}/config.py"
    )
    assert config is None

    config = load_module_from_file_location(
        "config", f"{Path(__file__).parent.parent}/examples/config.py"
    )
    assert config

# Generated at 2022-06-14 08:09:11.706765
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Test the function load_module_from_file_location."""
    location = "test/test_utils/test_config.py"
    module = load_module_from_file_location(location)
    assert module.NAME == "test_config"
    assert module.CONFIG_1 == "value_1"
    assert module.CONFIG_2 == "value_2"
    assert module.CONFIG_3 == "value_3"
    location = "test/test_utils/test_config2.py"
    module = load_module_from_file_location(location)
    assert module.NAME == "test_config2"
    location = Path("test/test_utils/test_config2.py")
    module = load_module_from_file_location(location)

# Generated at 2022-06-14 08:09:18.681909
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    from tempfile import NamedTemporaryFile

    with NamedTemporaryFile(mode="w") as fp:
        fp.write("blank_module")
        fp.flush()
        module = load_module_from_file_location(fp.name)

        assert module.__name__ == "config"

    with NamedTemporaryFile(mode="w", suffix=".py") as fp:
        fp.write("blank_module")
        fp.flush()
        module = load_module_from_file_location(fp.name)

        assert module.__name__ == "blank_module"

# Generated at 2022-06-14 08:09:28.849743
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import tempfile
    import os

    path = os.path.join(tempfile.gettempdir(), "temp_module.py")
    os.environ["TEMP_MODULE_PATH"] = tempfile.gettempdir()
    with open(path, "w") as temp_module:
        temp_module.write("some_variable = 'temp'")

    assert "some_variable" in dir(
        load_module_from_file_location("temp_module", path)
    )
    assert "some_variable" in dir(
        load_module_from_file_location("temp_module", "${TEMP_MODULE_PATH}")
    )
    assert load_module_from_file_location("temp_module", path).some_variable == "temp"


# Generated at 2022-06-14 08:09:36.936021
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import_string = load_module_from_file_location

    # Import default module
    module1 = import_string("__main__")
    assert type(module1) is types.ModuleType
    assert module1.__name__ == "__main__"
    assert module1.__file__ == "<string>"

    # Import global module when path contains environment variables
    os_environ["ENV_VAR"] = "environ"
    module2 = import_string("fixtures/global_module_with_env_var.py")
    assert type(module2) is types.ModuleType
    assert module2.__name__ == "module2"
    assert module2.__file__ == "fixtures/environ/module2.py"

    # Import global module when path is provided as Path

# Generated at 2022-06-14 08:09:49.819381
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    #############################################################
    # Part A) test to pass a Path type location variable
    #############################################################
    module_location = Path(__file__).parent / 'test_load_module_from_file_location.py' # noqa
    module = load_module_from_file_location(module_location)
    assert module.__name__ == "test_load_module_from_file_location"
    assert module.__package__ == "app_with_project"

    #############################################################
    # Part B) test to pass a string type location variable
    #############################################################
    module = load_module_from_file_location(str(module_location))
    assert module.__name__ == "test_load_module_from_file_location"

# Generated at 2022-06-14 08:10:01.894517
# Unit test for function load_module_from_file_location

# Generated at 2022-06-14 08:10:06.922720
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """We need to create temporary directory with simple
    configuration file, load it and check if everything is alright.
    """
    import os
    import tempfile


# Generated at 2022-06-14 08:10:18.096487
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    os_environ["SANIC_TEST_ENV_VAR"] = "some_value"

    os_environ["SANIC_TEST_ENV_VAR_2"] = "test"

    # 1. Tests for case when location is of string type.
    #    A) Tests for exception LoadFileException with
    #       message: The following environment variables are not set:
    #       ${some_env_var}.
    with pytest.raises(LoadFileException) as exc_info:
        load_module_from_file_location(
            "some_module_name", "/some/path/${some_env_var}"
        )

    exception_message = exc_info.value.args[0]

# Generated at 2022-06-14 08:10:27.761952
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    os_environ["config_path"] = os.getcwd()
    file = os.path.join(os_environ["config_path"], "tests", "test_config.py")
    module = load_module_from_file_location(None, file)
    assert module.TEST.test1.test2.test3.test4 == "sanic"
    module = load_module_from_file_location(None, file, module_name="test")
    assert module.TEST.test1.test2.test3.test4 == "sanic"
    module = load_module_from_file_location(None, "tests.test_config")
    assert module.TEST.test1.test2.test3.test4 == "sanic"

# Generated at 2022-06-14 08:10:40.590562
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    from os import environ

    with pytest.raises(LoadFileException) as exc:
        load_module_from_file_location("${nonexistent_env_var}")
    assert (
        str(exc.value)
        == "The following environment variables are not set: nonexistent_env_var"
    )

    # Every of these tests considering environment variable
    # environ["existing_env_var"] is set.
    environ["existing_env_var"] = "existing_env_var_value"

    module = load_module_from_file_location("${existing_env_var}")
    assert module.__spec__.name == "existing_env_var_value"
    assert module.__file__ == "existing_env_var_value"


# Generated at 2022-06-14 08:10:53.340601
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """ Just a function to test load_module_from_file_location """
    import sanic.config

    module = load_module_from_file_location(sanic.config.__file__)
    assert module.__name__ == "config"

    module = load_module_from_file_location(sanic.config.__file__, "utf8")
    assert module.__name__ == "config"
    assert module.LOGO == "Sanic"

    module = load_module_from_file_location(
        Path(sanic.config.__file__)
    )  # type: ignore
    assert module.__name__ == "config"
    assert module.LOGO == "Sanic"

    with os_environ.temp(some_env_var="42"):
        module = load_module_from_file

# Generated at 2022-06-14 08:11:05.382595
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from os import environ as os_environ
    os_environ["SOME_VAR"] = "some value"
    os_environ["OTHER_VAR"] = "other value"
    valid_location = "location/without/env/vars/some_file.py"
    module = load_module_from_file_location(valid_location)
    assert module.__name__ == "some_file"

    valid_location = "/root/path/to/some_file_with_env_vars.py"
    module = load_module_from_file_location(
        valid_location, "/root/path/${SOME_VAR}/${OTHER_VAR}/some_file_with_env_vars.py"
    )

# Generated at 2022-06-14 08:11:18.340336
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    import os
    import tempfile

    def touch(path):
        Path(path).touch()

    def dump_file(path, content):
        Path(path).write_text(content)

    with tempfile.TemporaryDirectory() as tmpdir:
        # check empty module
        touch(Path(tmpdir) / "empty.py")
        empty_module = load_module_from_file_location(
            Path(tmpdir) / "empty.py"
        )
        assert empty_module.__file__ == (Path(tmpdir) / "empty.py")

        # check test module
        # test_module.py:
        #     VAR = 1
        #     TEST_VAR = VAR + 2

# Generated at 2022-06-14 08:11:31.100179
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    import pytest
    from os import environ
    from os import path

    # location is str
    dir_path = path.dirname(path.realpath(__file__))
    location = path.join(dir_path, "test_load_module_from_file_location.py")
    # assert that function returns module.
    assert (
        isinstance(
            load_module_from_file_location(location), types.ModuleType
        )
        is True
    )

    # location has env. var in format ${ENV_VAR_NAME}
    location = "test_load_module_from_file_location.py"
    # assert that function raises LoadFileException
    # if env. var not defined.
    with pytest.raises(LoadFileException):
        load_module_from_

# Generated at 2022-06-14 08:11:43.820831
# Unit test for function load_module_from_file_location

# Generated at 2022-06-14 08:12:00.372694
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # Test 1
    test_func = load_module_from_file_location(
        "tests.utils.loaders.config", encoding="utf8"
    )
    assert test_func.test_load == "OK"
    # Test 2
    test_func = load_module_from_file_location(
        b"tests.utils.loaders.config", encoding="utf8"
    )
    assert test_func.test_load == "OK"
    # Test 3
    test_func = load_module_from_file_location(
        b"tests.utils.loaders.config", encoding="utf8"
    )
    assert test_func.test_load == "OK"
    # Test 4

# Generated at 2022-06-14 08:12:04.966228
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    os_environ["TESTING_ENV"] = "./"
    test_config = load_module_from_file_location("./tests/test_config.py")
    assert test_config.TESTING is True
    assert test_config.TESTING_ENV is "./"
    del os_environ["TESTING_ENV"]



# Generated at 2022-06-14 08:12:13.229302
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Test load_module_from_file_location function.

    1) Load module from local file.
    2) Try to import module with non-existing environment variables in path.
    3) Try to import module with an existing environment variable in path.
    4) Try to import module with non existing file.
    5) Try to import non-python module.
    6) Try to import non-existing module.

    """
    # A) Test load module from local file.
    #
    #    1) Load module from local file.
    #    2) Check if loaded module file path is correct.
    #    3) Check if loaded module has correct name.
    #
    import os
    import tempfile
    from sys import version_info

    # 1) Load module from local file.

# Generated at 2022-06-14 08:12:23.272054
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from tempfile import TemporaryDirectory

    with TemporaryDirectory() as temp_dir:
        path_to_test_file = Path(temp_dir) / "test.py"
        contents = (
            "#!/usr/bin/env python3.6\n"
            "test_field = 'test_value'\n"
            "test_field_two = 'test_value_two'\n"
        )

        path_to_test_file.touch()
        with open(path_to_test_file, "w") as f:
            f.write(contents)

        # load from path
        res = load_module_from_file_location(path_to_test_file)
        assert res.test_field == "test_value"
        assert res.test_field_two == "test_value_two"



# Generated at 2022-06-14 08:12:35.973030
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from os.path import join, dirname
    from pathlib import Path
    from pytest import raises
    from re import compile as re_compile

    # A) Check if location contains any environment variables
    #    in format ${some_env_var}.
    os_environ["SOME_ENV_VAR"] = "env_var_value"
    location = "${SOME_ENV_VAR}"

    env_vars_in_location = set(re_findall(r"\${(.+?)}", location))
    assert env_vars_in_location == {"SOME_ENV_VAR"}

    # B) Check these variables exists in environment.
    not_defined_env_vars = env_vars_in_location.difference(os_environ.keys())
    assert not not_

# Generated at 2022-06-14 08:12:39.605017
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    some_module = load_module_from_file_location(
        "tests/module.py", "/some/path/${some_env_var}"
    )
    # Check if we have some_module.some_module_function
    assert hasattr(some_module, "some_module_function")
    # Check if we have some_module.some_module_function
    assert hasattr(some_module, "property_inside_module")

# Generated at 2022-06-14 08:12:47.923101
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa: D102
    os_environ["some_env_var"] = "some_value"
    module = load_module_from_file_location(
        "path/to/file/${some_env_var}/some_file.py"
    )
    del os_environ["some_env_var"]

    assert module.__name__ == "some_file"
    assert module.__file__.endswith("some_file.py")



# Generated at 2022-06-14 08:12:59.247887
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    assert load_module_from_file_location("tests.test_helpers.module_under_test")
    assert load_module_from_file_location("tests/test_helpers.py")

    os_environ["TEST_ENV_VAR"] = "some_value"
    assert load_module_from_file_location("tests/test_helpers.py")
    assert load_module_from_file_location("tests/${TEST_ENV_VAR}/test_helpers.py")
    del os_environ["TEST_ENV_VAR"]

    try:
        load_module_from_file_location("tests/test_helpers.py", "utf42")
    except LookupError:
        assert True
    else:
        assert False


# Generated at 2022-06-14 08:13:05.403342
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from tempfile import TemporaryDirectory
    from textwrap import dedent

    from .test_utils import TemporaryEnvironmentVariable

    # test_load_module_from_file_location_can_not_load_file_without_full_path
    module = load_module_from_file_location("file.py")
    assert module == None  # type: ignore

    # test_load_module_from_file_location_can_load_file_with_full_path
    with TemporaryDirectory() as tmp_dir_name:
        test_file_name = Path(tmp_dir_name, "file.py")
        test_file_name.touch()
        module = load_module_from_file_location(test_file_name)
        assert module.__name__ == "file"

    # test_load_module_from_file_location

# Generated at 2022-06-14 08:13:16.900869
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # pylint: disable=protected-access, import-outside-toplevel
    import tempfile
    import shutil
    import os

    # Test if I can load file with path with env vars.
    # Test if I can load py file.
    # Test if I can load yaml file.
    test_dir = Path(tempfile.mkdtemp())

    # Test load without env variable
    path_to_py_module = Path(test_dir / "test_file.py")
    path_to_yaml_module = Path(test_dir / "test_file.yaml")

    # Test load with env variable
    os.environ["TEST_PATH_ENV"] = str(test_dir)

# Generated at 2022-06-14 08:13:26.017038
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # A) Check if location contains any environment variables
    #    in format ${some_env_var}.
    env_var = "SANIC_TEST_VAR"
    val = "test var"
    # Create environment variable.
    os_environ[env_var] = val
    # Create location with this env var in format ${some_env_var}.
    location = "path/${" + env_var + "}/some_file"
    # Check if module was imported.
    assert load_module_from_file_location(location)
    # Delete this environment variable.
    del os_environ[env_var]

    # B) Check these variables exists in environment.
    #    Because it was delted in previous test.
    with pytest.raises(LoadFileException):
        # Try to import module.
        load

# Generated at 2022-06-14 08:13:34.990168
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location(): # noqa
    """Unit test for function load_module_from_file_location"""
    import os
    import tempfile


# Generated at 2022-06-14 08:13:43.644513
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from .test_files.test_configs import utils_test_config

    utils_test_config_loaded = load_module_from_file_location(
        "utils_test_config", __file__
    )

    assert utils_test_config.SOME_CONFIG == utils_test_config_loaded.SOME_CONFIG
    assert utils_test_config.SOME_OTHER_CONFIG == (
        utils_test_config_loaded.SOME_OTHER_CONFIG
    )

# Generated at 2022-06-14 08:13:55.855278
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Unit test for function load_module_from_file_location."""

    # Load some valid module
    my_module = load_module_from_file_location("test_module")
    assert my_module.MY_CONSTANT == "some_value"

    # Trying to load module with environment variable in path.
    os_environ["MY_ENV_VAR"] = "test_env_var"
    my_module = load_module_from_file_location("test_module_${MY_ENV_VAR}")
    assert my_module.MY_CONSTANT == "some_value"
    del os_environ["MY_ENV_VAR"]

    # Trying to load module with undefined environment variable in path.

# Generated at 2022-06-14 08:14:08.986930
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from tempfile import TemporaryDirectory

    with TemporaryDirectory() as temp_dir:
        temp_dir = Path(temp_dir)
        os_environ["TEST_ENV_VAR_1"] = temp_dir.as_posix()
        test_module_content = "a = 1"

        test_module_path = temp_dir / "test_module.py"
        with open(test_module_path, "w") as test_module:
            test_module.write(test_module_content)

        test_module_name = test_module_path.parts[-1].split(".")[0]
        module = load_module_from_file_location(
            test_module_name, test_module_path
        )

        assert module.a == 1

        module = load_module_from_file_location

# Generated at 2022-06-14 08:14:15.758948
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    import sys
    import tempfile
    from os import remove, rmdir
    from os.path import dirname
    from pathlib import Path
    from shutil import rmtree
    from shutil import move as move_file
    from unittest.mock import patch

    import pytest

    class TestCase:
        # pylint: disable=no-self-use

        def test_load_module_from_file_location_with_str(self):
            """Test load_module_from_file_location with string."""
            temp_dir = tempfile.TemporaryDirectory()
            old_sys_modules = sys.modules.copy()

            temp_file = Path(temp_dir.name) / "some_var.py"


# Generated at 2022-06-14 08:14:24.562909
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    configs_path = Path(__file__).parent / "configs"
    os_environ["SANIC_ENV"] = "testing"
    os_environ["SANIC_TESTING"] = "true"

    config1 = load_module_from_file_location(configs_path / "config1.py")
    config2 = load_module_from_file_location(configs_path / "config2.py")
    config3 = load_module_from_file_location(configs_path / "config3.py")
    config4 = load_module_from_file_location(configs_path / "config4.py")
    config5 = load_module_from_file_location(configs_path / "config5.py")

# Generated at 2022-06-14 08:14:34.787400
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    os_environ["TEST_ENV_VAR"] = "test_env_var_value"

    # 1) Check if it's ok when you provide a full path as an argument.
    try:
        load_module_from_file_location(
            "/some/path/${TEST_ENV_VAR}/file_name.py"
        )
    except Exception:
        assert False

    # 2) Check if it's ok when you provide a file name as an argument.
    try:
        load_module_from_file_location("file_name.py")
    except Exception:
        assert False

    # 3) Check if it's ok when you provide an environment variable as an
    #    argument.

# Generated at 2022-06-14 08:14:40.361106
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    os_environ["some_env_var"] = "some_env_var_value"

    module = load_module_from_file_location("_test_module")
    assert module is not None
    assert module.__name__ == "_test_module"
    assert module.test_var == "test_var_value"

    module = load_modul

# Generated at 2022-06-14 08:14:52.120110
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # A) Test:
    #       - arguments are valid and function works properly
    #       - function raises LoadFileException
    #       - function raises IOError
    #       - function raises PyFileError
    #

    # A.1) Test:
    #       - arguments are valid and function works properly
    #
    some_module = load_module_from_file_location(
        "some_module_name", "tests/fixtures/some_path/some_module.py"
    )
    assert "some_module" == some_module.name
    assert "some_module.py" == some_module.__file__

    # A.2) Test:
    #       - function raises LoadFileException
    #

# Generated at 2022-06-14 08:15:07.974318
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import tempfile

    with tempfile.TemporaryDirectory() as tmpdir:
        location = Path(tmpdir) / "some_file.py"

        wrong_location = location / "some_file.py"  # wrong path

        # Test file loading with location as path.
        location.write_text("some_var = 'some_val'")
        module = load_module_from_file_location(location)
        assert module.some_var == "some_val"

        # Test file loading with location as str.
        location.write_text("some_var = 'some_val'")
        module = load_module_from_file_location(str(location))
        assert module.some_var == "some_val"

        # Test environment variable resolving.

# Generated at 2022-06-14 08:15:15.734247
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    import pytest
    from os import environ as os_environ, remove
    from pathlib import Path
    from textwrap import dedent

    from sanic.exceptions import LoadFileException, PyFileError

    # Create temporary file.
    file_location = Path("test_load_module_from_file_location.py")
    file_location.write_text(dedent("""\
        x = 1
        y = 2
    """))

    # Unit test load_module_from_file_location
    assert load_module_from_file_location(file_location) == load_module_from_file_location(file_location.__str__()) == load_module_from_file_location(file_location.__bytes__())

    # Unit test what happens if file does not exist.

# Generated at 2022-06-14 08:15:26.732555
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # A)
    test_module_name = "test_load_module_from_file_location_module"
    test_location = "test_load_module_from_file_location_location"

    # 0) Tests module import from string.
    class SomeClass(object):
        pass

    some_object = SomeClass()
    some_object.attribute = "test_attribute"

    some_module = types.ModuleType(test_module_name)
    some_module.some_object = some_object
    some_module.__file__ = "test_file"

    assert load_module_from_file_location(test_module_name) is some_module

    # 1) Testing module import from string with no path and .py extension.
    some_module = types.ModuleType(test_location)

# Generated at 2022-06-14 08:15:40.504386
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # pragma: no cover
    import pytest

    location = "sanic.config.module_from_file_location_test_location"
    os_environ[location] = "./sanic/tests/data"
    module = load_module_from_file_location(
        "${" + location + "}/module_from_file_location.py"
    )
    assert module.a == 1
    assert module.b == 2
    os_environ.pop(location)

    location = "sanic.config.module_from_file_location_test_location"
    os_environ[location] = "/sanic/tests/data"
    module = load_module_from_file_location(
        "./${" + location + "}/module_from_file_location.py"
    )
    assert module

# Generated at 2022-06-14 08:15:49.276582
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import sys
    import pathlib
    import random

    # A) File name only
    #    A.1) Some random file name
    test_module_name = "__test_module_" + str(random.randint(0, 1e9))
    #    A.2) Searching path for the file name with this file name.
    test_module_path = None
    for path in sys.path:
        if (
            pathlib.Path(path).exists()
            and (
                pathlib.Path(path)
                / test_module_name
                / (test_module_name + ".py")
            ).exists()
        ):
            test_module_path = pathlib.Path(
                path
            ) / test_module_name / (test_module_name + ".py")


# Generated at 2022-06-14 08:16:02.475515
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import io
    import sys
    import tempfile

    # A) Check that location with path works.
    with tempfile.TemporaryDirectory() as tmpdirname:
        tmpdirname = Path(tmpdirname)
        module1_dir = tmpdirname / "module1_dir"
        module1_dir.mkdir()
        with (module1_dir / "__init__.py").open("w"):
            pass
        with (module1_dir / "module1.py").open("w") as f:
            f.write("module1_var=1")

        module2_dir = tmpdirname / "module2_dir"
        module2_dir.mkdir()
        with (module2_dir / "module2.py").open("w") as f:
            f.write("module2_var=2")

# Generated at 2022-06-14 08:16:15.958926
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    location = "/home/user/app/config.py"
    module = load_module_from_file_location(location)
    assert module.__file__ == location
    assert module.name == "config"

    location = "/home/user/app/config"
    module = load_module_from_file_location(location)
    assert module.__file__ == location

    location = "../some_other_module.py"
    module = load_module_from_file_location(location)
    assert module.__file__.endswith(location)

    location = "some_other_module"
    module = load_module_from_file_location(location)
    assert module.__file__.endswith(".py")

    location = "some_other_module.py"
    module = load_module_from

# Generated at 2022-06-14 08:16:26.851406
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """
    Tests import string from file location.
    """
    from tempfile import NamedTemporaryFile
    from unittest.mock import patch

    with NamedTemporaryFile() as temp:
        temp.write(b"FOO = True")
        temp.flush()
        path = Path(temp.name)
        module = load_module_from_file_location(path)
        assert module.FOO is True

    with NamedTemporaryFile() as temp:
        temp.write(b'FOO = "FOO"')
        temp.flush()
        module = load_module_from_file_location(temp.name)
        assert module.FOO == "FOO"


# Generated at 2022-06-14 08:16:36.335088
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    # 0. Set up a location for test config.
    test_config_location = Path(__file__).parent / "test_config.py"

    # 1. Test load_module_from_file_location with string as location.
    test_config_string_location = f"{test_config_location}"
    loaded_config = load_module_from_file_location(
        test_config_string_location
    )
    assert (
        loaded_config.TEST_CONFIG_VAR == "test_config"
    ), "Unable to load config from test_config.py"

    # 2. Test load_module_from_file_location with Path as location.
    test_config_path_location = Path(test_config_string_location)
    loaded_config = load_module_from_file

# Generated at 2022-06-14 08:16:48.818242
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import os
    from tempfile import TemporaryDirectory
    from os.path import join as path_join
    from importlib import reload

    ##############################
    # Test load module from file #
    ##############################
    with TemporaryDirectory() as temp_dir:
        test_file_name = path_join(temp_dir, "somefile.py")
        with open(test_file_name, "w", encoding="utf8") as f:
            f.write(
                """some_value = 'SOME_VALUE'\nother_value = 'OTHER_VALUE'"""
            )
        some_module = load_module_from_file_location(test_file_name)
        assert some_module.some_value == "SOME_VALUE"
        assert some_module.other_value == "OTHER_VALUE"
       

# Generated at 2022-06-14 08:17:03.545806
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # When:
    #   Load file with location which is not a file path,
    #   is not bytes type, but is a env var, which is not set,
    #   and it is of a string type.
    # Then:
    #   LoadFileException should be thrown.
    with pytest.raises(LoadFileException):
        load_module_from_file_location("${UNSET_ENV_VARIABLE}")

    # Given:
    #   Directory for testing with config.py file.
    directory = Path("tests/config")
    # When:
    #   Load file with location which is actually a file path but is of a bytes
    #   type.
    # Then:
    #   No exception should be thrown.

# Generated at 2022-06-14 08:17:12.112854
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # Check if function works with saving file name
    import_me = b"src/sanic_cors/extension.py"
    assert load_module_from_file_location(
        import_me
    ).__name__ == "extension"  # type: ignore

    # Check if function works with absolute path
    import_me = b"/src/sanic_cors/extension.py"
    assert load_module_from_file_location(
        import_me
    ).__name__ == "extension"  # type: ignore

    # Check if we can import module with custom name
    import_me = b"src/sanic_cors/extension.py"

# Generated at 2022-06-14 08:17:23.480950
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    import os.path

    test_module_name = "test_module"
    test_module_file = (
        os.path.dirname(os.path.realpath(__file__)) + "/test_module.py"
    )

    test_module = load_module_from_file_location(test_module_file)
    assert test_module.__name__ == test_module_name

    test_module = load_module_from_file_location(
        test_module_file, "some_nonexistent_package_name"
    )
    assert test_module.__name__ == test_module_name

    test_module_name = "test_module_with_non_ascii_path"

# Generated at 2022-06-14 08:17:33.800690
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # A) When location is of a string type
    # A.1) When location is a valid python file path.
    location = "tests/test_fixtures/configuration_files/valid_python_file.py"
    module = load_module_from_file_location(location)
    assert type(module) == types.ModuleType
    assert module.__file__ == location
    # A.2) When location is an invalid python file path.
    location = "tests/test_fixtures/configuration_files/invalid_python_file.py"
    with pytest.raises(PyFileError):
        load_module_from_file_location(location)
    # A.3) When location is a valid config file path.

# Generated at 2022-06-14 08:17:37.122684
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    assert (
        load_module_from_file_location(
            "tests/test_file_location", "./tests/test_file_location"
        )
        == "Hello world!"
    )



# Generated at 2022-06-14 08:17:50.158702
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # 1) Test if function load_module_from_file_location loads module
    #    provided as Path object.
    # 2) Test if function load_module_from_file_location loads module
    #    provided as string that looks like path.
    # 3) Test if function load_module_from_file_location loads module
    #    provided as string that looks like import path.
    # 4) Test if function load_module_from_file_location raises exception
    #    when loading wrong module.
    # 5) Test if function load_module_from_file_location raises exception
    #    when location string contains not defined environment variables.

    from importlib import util as importlib_util

    from tempfile import TemporaryDirectory

    from os import environ as os_environ
    from random import choice, random

    from pathlib import Path

   

# Generated at 2022-06-14 08:17:58.366895
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    test_module_contents1 = """
some_var1 = 1
some_var2 = 2
"""
    test_module_contents2 = """
some_var3 = 3
some_var4 = 4
"""
    test_module_contents3 = """
some_var5 = 5
some_var6 = 6
"""
    test_module_contents4 = """
some_var7 = 7
some_var8 = 8
"""
    test_module_contents5 = """
some_var9 = 9
some_var10 = 10
"""
    test_module_contents6 = """
some_var11 = 11
some_var12 = 12
"""


# Generated at 2022-06-14 08:18:04.200875
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    os_environ["TEST_ENV_VAR"] = "some_value"
    load_module_from_file_location(
        "tests/test_utils/config.py",
        "/some/path/${TEST_ENV_VAR}/${TEST_ENV_VAR}/test.py",
    )

# Generated at 2022-06-14 08:18:15.244685
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import sys
    import os
    import tempfile
    import pytest

    test_dir = tempfile.gettempdir()

    with open(os.path.join(test_dir, "module1.py"), "w") as f:
        f.write("a = 1")
    with open(os.path.join(test_dir, "module2.py"), "w") as f:
        f.write("b = 2")

    sys.path.insert(0, test_dir)

    # Load module from .py file
    mod1 = load_module_from_file_location("module1")
    assert mod1.a == 1
    assert mod1.__file__ == os.path.join(test_dir, "module1.py")

    # Load module from the same file
    mod1 = load_module_from