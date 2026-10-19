

# Generated at 2022-06-14 08:08:26.616592
# Unit test for function str_to_bool
def test_str_to_bool():
    assert str_to_bool("true")
    assert str_to_bool("t")
    assert str_to_bool("yes")
    assert str_to_bool("y")
    assert str_to_bool("1")
    assert str_to_bool("enabled")
    assert str_to_bool("enable")
    assert str_to_bool("on")
    assert str_to_bool("yep")
    assert str_to_bool("yup")
    assert str_to_bool("TRUE")
    assert str_to_bool("T")
    assert str_to_bool("YES")
    assert str_to_bool("Y")
    assert str_to_bool("1")
    assert str_to_bool("ENABLED")
    assert str_to_bool("ENABLE")
    assert str_to_

# Generated at 2022-06-14 08:08:39.301280
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import tempfile
    pyfile = tempfile.NamedTemporaryFile(prefix="test_", suffix=".py")
    pyfile.write(b"some_var = 1")
    pyfile.flush()
    module = load_module_from_file_location(pyfile.name)
    assert module.some_var == 1

    import os
    import shutil
    # Create directory `testdir`
    tmpdir = tempfile.mkdtemp(prefix="test_")
    testdir = Path(tmpdir) / "testdir"
    os.mkdir(testdir)
    os.environ["MYVAR"] = str(testdir)

    # Create file `testdir/testfile.py`
    testfile = testdir / "testfile.py"

# Generated at 2022-06-14 08:08:47.103825
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # A) Check if location contains any environment variables
    #    in format ${some_env_var}.
    env_vars_in_location = set(re_findall(r"\${(.+?)}", '''test/${some_env_var}'''))

    # B) Check these variables exists in environment.
    not_defined_env_vars = env_vars_in_location.difference(os_environ.keys())
    if not_defined_env_vars:
        print(
            "The following environment variables are not set: "
            f"{', '.join(not_defined_env_vars)}"
        )
    
    # C) Substitute them in location.

# Generated at 2022-06-14 08:08:58.598155
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Checks if load_module_from_file_location function works correctly."""

    import pytest

    # A) If the location parameter is bytes, then it should be decoded with
    #    the provided encoding.
    module = load_module_from_file_location(
        b"\xc2\xabSome location\xc2\xbb",
        "/some/system/path",
        encoding="utf8",
    )
    assert "location" in dir(module)

    # B) If the location parameter is a string, then it should be loaded as
    #    path.
    module = load_module_from_file_location(
        b"Some location", "/some/system/path"
    )
    assert "location" in dir(module)

    # C) If the location parameter is a path, then it should be loaded

# Generated at 2022-06-14 08:09:10.765620
# Unit test for function str_to_bool
def test_str_to_bool():
    assert str_to_bool("true") is True
    assert str_to_bool("True") is True
    assert str_to_bool("t") is True
    assert str_to_bool("on") is True
    assert str_to_bool("yes") is True
    assert str_to_bool("y") is True
    assert str_to_bool("yep") is True
    assert str_to_bool("YEP") is True
    assert str_to_bool("yup") is True
    assert str_to_bool("ON") is True

    assert str_to_bool("false") is False
    assert str_to_bool("1") is False
    assert str_to_bool("FALSE") is False
    assert str_to_bool("f") is False
    assert str_to_bool("off") is False


# Generated at 2022-06-14 08:09:23.109943
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    import logging
    from importlib import reload
    from pathlib import Path
    from tempfile import TemporaryDirectory
    from unittest.mock import patch

    from sanic import Sanic

    TEMPORARY_DIRECTORY = TemporaryDirectory()
    TEMPORARY_DIRECTORY_PATH = Path(TEMPORARY_DIRECTORY.name)
    TEMPORARY_DIRECTORY_PATH_ABS = TEMPORARY_DIRECTORY_PATH.absolute()
    TEST_FILE_PATH = TEMPORARY_DIRECTORY_PATH / "test_file.py"

    # For the test we use a small app.
    app = Sanic("test_load_module_from_file_location")

    # Prepare test_file.py with a variable TEST_VAR set to "TEST_VAR_

# Generated at 2022-06-14 08:09:29.987001
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    import tempfile

    with tempfile.TemporaryDirectory() as tmpdirname:
        name = "MYCONFIG"
        fpath = tmpdirname + "/" + name + ".py"
        with open(fpath, "w") as fo:
            fo.write("FOO=1\n")
            fo.write("bar=2\n")
        mymodule = load_module_from_file_location(fpath)
        os.remove(fpath)
        assert mymodule.FOO == 1
        assert mymodule.bar == 2



# Generated at 2022-06-14 08:09:37.388851
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Test for function that loads module from file location"""
    import json

    test_str_with_env_vars = "${test_env_var}/test.py"

    # test if environment variable is properly substitute in location
    os_environ["test_env_var"] = "test_env_var"
    assert (
        load_module_from_file_location(test_str_with_env_vars).__file__
        == "test_env_var/test.py"
    )

    # test if exception is raised when environment variable is not set
    del os_environ["test_env_var"]

# Generated at 2022-06-14 08:09:50.249430
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from sanic.config import Config
    from types import ModuleType
    from tempfile import NamedTemporaryFile
    from typing import Type
    from uuid import uuid4

    def create_config_file(content: str) -> ModuleType:
        with NamedTemporaryFile(delete=False) as config_file:
            config_file.write(content.encode("utf-8"))

        return load_module_from_file_location(config_file.name)

    # A) Test if empty config file works.
    assert repr(create_config_file("")) == "config"

    # B) Test if load_module_from_file_location can load module from
    #    environment variable.

    # a) Create random variable name for environment variable.

# Generated at 2022-06-14 08:10:00.960142
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import tempfile
    import shutil

    # Create temporary directory
    temp_dir = tempfile.mkdtemp()


# Generated at 2022-06-14 08:10:16.455136
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    # All these tests will be run only if you run them by hands
    # with command `pytest tests/test_helpers.py`
    # because they are not the nosetests.

    # Run tests in directory where this file is.
    path_to_caller = Path(__file__).parent

    # 1. A) Prepare folder with config.py
    assert not Path(path_to_caller, "config").exists()
    assert not Path(path_to_caller, "config", "config.py").exists()
    config_folder = Path(path_to_caller, "config")
    config_folder.mkdir()
    config_py = Path(config_folder, "config.py")
    config_py.touch()

    # 1. B) Let's write some content in config.py
    example

# Generated at 2022-06-14 08:10:26.041815
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    module = load_module_from_file_location(
        "sanic.helpers.test_functions", "test.py"
    )
    assert module.__name__ == "sanic.helpers.test_functions"

    module = load_module_from_file_location(
        "helpers.test_functions", "test.py"
    )
    assert module.__name__ == "helpers.test_functions"

    module = load_module_from_file_location("test", "test.py")
    assert module.__name__ == "test"

    module = load_module_from_file_location("test.py")
    assert module.__name__ == "test"

# Generated at 2022-06-14 08:10:38.727349
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Test to make sure that load_module_from_file_location
    returns correct object.
    """
    # create a test file
    test_file = "/tmp/test_sanic_config.py"
    with open(test_file, "w") as f:
        f.write("TEST = 'TEST'")

    # load it with load_module_from_file_location
    mod = load_module_from_file_location(test_file)

    # compare it with types.ModuleType
    assert isinstance(mod, types.ModuleType)

    # test its values
    assert mod.TEST == "TEST"
    assert mod.__file__ == test_file

    # delete the test file
    os.remove(test_file)



# Generated at 2022-06-14 08:10:50.708767
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    from tempfile import mkstemp
    from os import close, unlink
    from os.path import exists

    # A) Just check if it is able to load module from .py file.
    mod_path = Path("/tmp/test_module.py")
    mod_path.write_text(
        'some_var = "Some value"'
    )  # write some content to file
    mod = load_module_from_file_location(mod_path)
    assert mod.some_var == "Some value"
    mod_path.unlink()  # remove file

    # B) Check if it is able to load env vars from file.
    os_environ["TEST_ENV_VAR"] = "testing env var"
    mod_path = Path("/tmp/test_module.py")
   

# Generated at 2022-06-14 08:10:54.447463
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    module = load_module_from_file_location(__file__)
    assert isinstance(module, types.ModuleType)


if __name__ == "__main__":
    test_load_module_from_file_location()

# Generated at 2022-06-14 08:10:59.644885
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    location = (
        Path(__file__).parent
        / "data"
        / "load_module_from_file_location"
        / "simple_module.py"
    )
    mod = load_module_from_file_location(location)
    assert mod.a == 1
    assert mod.b == 2

# Generated at 2022-06-14 08:11:10.685822
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    this_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(this_dir)

    module = load_module_from_file_location(
        Path(this_dir) / "test_config.py"
    )

    module = load_module_from_file_location(
        Path(this_dir) / "test_config.py", "utf8"
    )

    module = load_module_from_file_location(
        "test_config.py", this_dir, "utf8"
    )

    module = load_module_from_file_location(
        "test_config.py", this_dir, "utf8"
    )


# Generated at 2022-06-14 08:11:20.542735
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    # A. Check error handling
    try:
        some_module = load_module_from_file_location(
            "some_module_name", "/some/path/${some_env_var}"
        )
        # If no error here, then something went wrong.
        assert False
    except Exception as e:
        assert isinstance(e, LoadFileException)

    # B. Check if function returns correct module type.
    # It should return an object of the module type.
    some_module = load_module_from_file_location(
        "sanic.app", "/home/kirill/src/Sanic/sanic/app.py"
    )
    assert isinstance(some_module, types.ModuleType)

    # C. Check if function can load module without .py extension.
    some_module = load_module

# Generated at 2022-06-14 08:11:32.572986
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import tempfile

    # A) Create temporary file with some content
    # and assign relative file path to location
    some_content = "some_var = 100"
    location = Path(tempfile.NamedTemporaryFile(mode="w").name)
    with open(location, "w") as fp:
        fp.write(some_content)
    # B) Check that we get module with some_var
    # coresponding to some_content
    module = load_module_from_file_location(location)
    assert module.some_var == 100

    # A) Create temporary file with some content
    # and assign absolute file path to location
    some_content = "some_var_abs = 101"
    location_abs = Path(tempfile.NamedTemporaryFile(mode="w").name).absolute()

# Generated at 2022-06-14 08:11:45.117785
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    assert load_module_from_file_location(__file__)

    import json
    import pickle
    import tempfile

    import pytest

    json_content = {"some_json_key": "some_json_val"}
    pickle_content = {"some_pickle_key": "some_pickle_val"}

    with tempfile.NamedTemporaryFile("w") as json_file:
        json_file_path = Path(json_file.name)
        json.dump(json_content, json_file)
        json_file.flush()
        loaded_json_module = load_module_from_file_location(
            json_file_path, encoding="utf8"
        )

    with tempfile.NamedTemporaryFile("wb") as pickle_file:
        pickle_file_path = Path

# Generated at 2022-06-14 08:11:58.514171
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # Import sanic just for the sake of test
    from sanic import Sanic

    # Put module Sanic in the same directory where this test is located.
    # It's just for the sake of test.
    file = Path(__file__).parent / "Sanic.py"

# Generated at 2022-06-14 08:12:09.424079
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    # 1. Test importing .py file
    import tempfile
    import shutil
    from sanic.config import TEST_FILES_FOLDER
    from sanic import Sanic

    with tempfile.TemporaryDirectory() as temp_dir:

        temp_dir_path = Path(temp_dir) / "sanic_test_project"
        shutil.copytree(TEST_FILES_FOLDER, temp_dir_path)

        module = load_module_from_file_location(
            temp_dir_path / "config.py"
        )

        assert "CONFIG_FILE" in module.__dict__.keys()
        assert module.CONFIG_FILE == "config.py"

        assert "SERVER_NAME" in module.__dict__.keys()
        assert module.SERVER_NAME == "localhost"

# Generated at 2022-06-14 08:12:20.830210
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import json
    import os
    import tempfile

    # A) Same location, fails for no reason
    try:
        load_module_from_file_location("a/b/c/d/e")
    except LoadFileException as error:
        assert (
            "The following environment variables are not set: some_env_var"
            in error.message
        )
    else:
        assert False, "unexpected success"

    # B) Same location but with environment variables
    os.environ["some_env_var"] = "123"
    try:
        load_module_from_file_location("a/b/c/d/e")
    except LoadFileException as error:
        assert (
            "The following environment variables are not set: ${some_env_var}"
            in error.message
        )
   

# Generated at 2022-06-14 08:12:31.463326
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    # For more info sees:
    # https://stackoverflow.com/questions/20483633/python-3-3-1-cannot-import-name-main
    if __name__ == "__main__":
        from .test_helpers import load_module_from_file_location_unittest
        import os

        os.environ["SANIC_TEST_VAR"] = "t"
        os.environ["SANIC_TEST_NOT_DEFINED_VAR"] = "q"
        load_module_from_file_location_unittest(os.environ["SANIC_TEST_VAR"])

# Generated at 2022-06-14 08:12:39.821820
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Unit test for function load_module_from_file_location."""
    this_dir = Path(__file__).absolute().parent
    module_as_file = this_dir / "module_as_file.py"

# Generated at 2022-06-14 08:12:52.269306
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # A) Check if module can be loaded
    #    with just a plain string.
    module_a = load_module_from_file_location(
        "sanic.server"
    )  # type: ignore # noqa
    assert module_a.__file__ == "sanic/server.py"

    # B) Check if module can be loaded with
    #    a string containing environment variables.
    os_environ["DIR_NAME"] = __file__.split("/")[-2]
    module_b = load_module_from_file_location(
        "sanic.server",
        "/some/${DIR_NAME}",
    )  # type: ignore # noqa
    assert module_b.__file__ == "sanic/server.py"

    # C) Check if module can be loaded with a


# Generated at 2022-06-14 08:13:02.539336
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import tempfile

    # Create temporary directory
    with tempfile.TemporaryDirectory(prefix="unitest_") as temp_dir:

        # Put in environment some variable
        s = "some_env_var"
        os_environ[s] = temp_dir

        # Create file
        path = Path(temp_dir) / "some_file.py"
        path.write_text("some_value = 'hello'")

        # Load file from location
        module = load_module_from_file_location(path)

        # Check value
        assert module.some_value == "hello"

        # Fail on unexisting env variable
        path.write_text("some_value = '${FAIL}'")

# Generated at 2022-06-14 08:13:14.881675
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from tempfile import TemporaryDirectory

    # ----------------------------
    # Test module loading from location
    # ----------------------------
    with TemporaryDirectory() as module_path:
        module_name = "test_module"
        module_file_name = module_name + ".py"

        # Create test module
        module_path_file = Path(module_path) / module_file_name

        module_path_file.write_text(
            '''# Test module for load_module_from_file_location
            TEST_VAR = "Test variable"
        '''
        )

        assert not hasattr(sys.modules, module_name)

        # Load module from its location
        test_module = load_module_from_file_location(
            str(module_path_file), module_path
        )

# Generated at 2022-06-14 08:13:24.412896
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    import pytest

    # A) Test if calling function with Path as a first parameter
    #    coresponds to calling it with str as a first parameter
    assert (
        load_module_from_file_location("./path")
        == load_module_from_file_location(Path("./path"))
    )

    # B) Test if calling function with Path as a first parameter
    #    coresponds to calling it with str as a first parameter
    assert (
        load_module_from_file_location(b"./path")
        == load_module_from_file_location(Path("./path"))
    )

    # C) Test if calling function with Path as a first parameter
    #    coresponds to calling it with str as a first parameter

# Generated at 2022-06-14 08:13:32.290801
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    os_environ["some_env_var"] = "some_env_var_value"
    module = load_module_from_file_location(
        "test_load_module_from_file_location",
        "tests/test_module.py"
    )
    assert module.some_var == 'test_load_module_from_file_location'
    del os_environ["some_env_var"]

# Generated at 2022-06-14 08:13:46.785901
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from tempfile import TemporaryDirectory

    # Testing regular .py configuration file.
    with TemporaryDirectory() as tempdir:
        with open(Path(tempdir) / "config.py", "w") as f:
            f.write(
                """
                test_var = "test_value"
                TEST_INT_VAR = 42
                """
            )

        test_module = load_module_from_file_location(
            Path(tempdir) / "config.py"
        )
        assert test_module.test_var == "test_value"
        assert test_module.TEST_INT_VAR == 42

    # Testing regular key=value configuration file.

# Generated at 2022-06-14 08:13:56.982443
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    try:
        import configparser
    except ImportError:
        # ConfigParser is not available in python 3.9,
        # but we use it here only to create some config file.
        # Hence here is a pure python implementation.
        import io
        import sys

        class RawConfigParser:
            STORE_TYPES = {str: "str"}

            def __init__(self):
                self.vars = {}

            def read(self, _):
                return []

            def raw_items(self, _):
                return self.vars.items()

            def set(self, section, var, value):
                self.vars[(section, var)] = value

            def write(self, file_object):
                for (section, var), value in self.vars.items():
                    store_type = self.ST

# Generated at 2022-06-14 08:14:10.330626
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    from tempfile import mkdtemp
    from os import environ as os_environ
    from shutil import rmtree
    from random import choice as choice_from

    # create a temporary directory
    tmp_dir = mkdtemp()
    # create test configuration file
    test_config_file_path = Path(tmp_dir, "test_config.py")
    with test_config_file_path.open("w") as f:
        f.write(
            """
            version = 1
            name = "test_config"
            """
        )

    # create test environment variables
    some_env_vars = {
        "key1": "value1",
        "key2": "value2",
        "key3": "value3",
    }

# Generated at 2022-06-14 08:14:21.455527
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    os_environ["some_env_var"] = "/some/env/var/value"

    module = load_module_from_file_location(
        "test_utils",
        "./sanic/tests/unit/test_server/test_utils.py",
    )

    assert module.__name__ == "test_utils"
    assert module.SOME_TEST_CONFIG_PARAM == "test"
    assert module.SOME_OTHER_TEST_CONFIG_PARAM == "test2"

    module = load_module_from_file_location(
        "/some/path/${some_env_var}/test_utils.py"
    )

    assert module.__name__ == "test_utils"
    assert module.SOME_TEST_CONFIG_PARAM == "test"

# Generated at 2022-06-14 08:14:33.342144
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """
    Tests cases when path to the module contains environment variables.
    """
    import sys
    import pytest
    from tempfile import mkstemp, TemporaryDirectory
    from os import close, environ as os_environ
    from shutil import copyfile

    test_environ_var = "TEST_ENV_VAR"
    test_environ_var_name = "TEST_ENV_VAR_NAME"
    test_environ_var_val = "TEST_ENV_VAR_VAL"
    test_environ_var_name_val = f"{test_environ_var_name}={test_environ_var_val}"

    # Prepare an object that emulates function mkstemp, but returns
    # also a file content

# Generated at 2022-06-14 08:14:41.273948
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import tempfile
    import os
    import shutil
    pathlib = Path(__file__).parent
    temp_dir_path = tempfile.mkdtemp()

# Generated at 2022-06-14 08:14:52.863259
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from io import StringIO
    from tempfile import TemporaryDirectory

    config_str = """\
    SERVER = "some_server_name"
    URL = "https://" + SERVER
    """

    with TemporaryDirectory() as tmpdirname:

        # 1) Test that function works with bytes variables.
        loc_bytes = Path(tmpdirname, "config_bytes.py").encode()
        with open(loc_bytes, "wb") as config_bytes_file:
            config_bytes_file.write(config_str.encode())
        module_bytes = load_module_from_file_location(loc_bytes, encoding="utf8")
        assert module_bytes.SERVER == "some_server_name"
        assert module_bytes.URL == "https://some_server_name"

        # 2) Test that function works

# Generated at 2022-06-14 08:15:04.127968
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import json

    config_vals = {
        "val1": "some_val",
        "val2": "other_val",
        "val3": 2,
    }

    fpath = "some/path/to/config.json"
    with open(fpath, "w") as f:
        json.dump(config_vals, f)

    config = load_module_from_file_location(fpath)

    assert hasattr(config, "val1")
    assert hasattr(config, "val2")
    assert hasattr(config, "val3")

    assert getattr(config, "val1") == config_vals["val1"]
    assert getattr(config, "val2") == config_vals["val2"]
    assert getattr(config, "val3") == config_vals["val3"]



# Generated at 2022-06-14 08:15:12.745824
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from tempfile import NamedTemporaryFile
    from types import ModuleType

    # A) Without any environment variables.
    assertion_message = (
        "Expected module type is ModuleType, but got "
        f"{type(load_module_from_file_location(__file__))}"
    )
    assert isinstance(
        load_module_from_file_location(__file__), ModuleType
    ), assertion_message

    # B) With environment variables.
    with NamedTemporaryFile(suffix=".py") as tmp_file:
        os_environ["file_path_for_load_module_from_file_location_test"] = str(
            tmp_file.name
        )

        # 1. Not existing environment variable.

# Generated at 2022-06-14 08:15:25.324683
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from tempfile import NamedTemporaryFile

    import_name = "test_config_name"
    content = "CONFIG_VALUE = 3"
    with NamedTemporaryFile("w", suffix=".py", delete=False) as test_config:
        test_config.write(content)
        test_config_name = test_config.name

        try:
            config_module = load_module_from_file_location(
                test_config_name
            )
            assert config_module.CONFIG_VALUE == 3
        finally:
            os.remove(test_config_name)

    with NamedTemporaryFile("w", suffix=".py", delete=False) as test_config:
        test_config.write(content)
        test_config_name = test_config.name


# Generated at 2022-06-14 08:15:42.572757
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from ctypes import CDLL, c_char_p
    from os import environ

    from sanic.config import Config

    from .test_config import config_from_file_path

    # A) Check that function correctly handles exceptions.

    # A-1) Check if it correctly raises PyFileError if given module is not valid
    #      Python module.

    path_to_invalid_py_module = config_from_file_path("invalid_py_module")
    try:
        load_module_from_file_location(path_to_invalid_py_module)
    except (PyFileError, LoadFileException):
        pass

# Generated at 2022-06-14 08:15:55.354269
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Tests functions load_module_from_file_location."""

    # A) Test that load_module_from_file_location
    #    returns the same module as python built-in `import`
    #    for normal import.
    import os

    os_module_with_import = os
    os_module_with_load_module_from_file_location = load_module_from_file_location(
        "os"
    )

    assert os_module_with_import is os_module_with_load_module_from_file_location

    # B) Test that load_module_from_file_location
    #    returns module with the same attributes
    #    as the module imported with built-in `import`.

# Generated at 2022-06-14 08:16:00.871715
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """
    Loads example_config.py and checks if contains key "key"
    with value "value".
    """
    example_config_dir = Path(__file__).parent / "example_config.py"
    assert load_module_from_file_location(example_config_dir).key == "value"



# Generated at 2022-06-14 08:16:14.482999
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # Load from file location string
    from .test_config import test_conf_file

    module = load_module_from_file_location(
        test_conf_file, "config_from_file_location"
    )
    assert module.SOME_ENV_VAR == "env_val_placeholder"
    assert module.SOME_SETTING == "some_placeholder"

    # Load from file location string with Path
    from .test_config import test_conf_file_path

    module = load_module_from_file_location(
        test_conf_file_path, "config_from_file_location_path"
    )
    assert module.SOME_ENV_VAR == "env_val_placeholder"
    assert module.SOME_SETTING == "some_placeholder"

    # Load

# Generated at 2022-06-14 08:16:22.167677
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    os_environ["HARVEST_ENV"] = "dev"
    os_environ["BASE_DIR"] = "./my_project"

    test_module = load_module_from_file_location(
        f"${BASE_DIR}/app/config/{HARVEST_ENV}.py"
    )
    assert test_module.__file__ == "./my_project/app/config/dev.py"
    assert test_module.SERVER_HOST == "localhost"
    assert test_module.SERVER_PORT == 8000

    test_module = load_module_from_file_location(Path("test.py"))
    assert test_module.__file__ == "test.py"


# Generated at 2022-06-14 08:16:31.763381
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Test input parameters of function load_module_from_file_location"""
    from .utils import IS_WINDOWS

    from pathlib import Path
    from tempfile import NamedTemporaryFile
    from textwrap import dedent

    tmp_file = NamedTemporaryFile(delete=False, mode="w+")
    tmp_file.write(
        dedent(
            """
        from os import environ as os_environ
        from pathlib import Path

        some_param = 1

        some_complex_param = Path("some_complex_param")

        some_path_param = Path("some_path_param")

        some_path_param_from_env = Path(f"some_path_param_from_env_{
            some_param
        }")
        """
        )
    )
    tmp_file.close()

   

# Generated at 2022-06-14 08:16:42.510776
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import re

    # ---- Tests for case with just one string
    # A) Test that function does not import unexisting module
    #    and raises IOError.
    try:
        load_module_from_file_location("unexisting_module")
        assert False
    except IOError:
        pass

    # B) Test that function imports existing module properly.
    assert load_module_from_file_location("re") == re

    # ---- Tests for case with file path
    # A) Test that function does not import unexisting file
    #    and raises IOError.
    try:
        load_module_from_file_location("unexisting_file.py")
        assert False
    except IOError:
        pass

    # B) Test that function imports existing file properly.

# Generated at 2022-06-14 08:16:50.880114
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # See the docstring for tests in this cases.
    def test_a():
        location = "some_module/${HOME}/example.py"
        (os_environ["HOME"])
        load_module_from_file_location(location=location)

    def test_b():
        location = "some_module/${HOME}/example.py"
        try:
            load_module_from_file_location(location=location)
        except LoadFileException as e:
            assert "HOME" in str(e)
        finally:
            del os_environ["HOME"]

    def test_c():
        location = "some_module/${HOME}/example.py"
        os_environ["HOME"] = "should be replaced"

# Generated at 2022-06-14 08:17:01.891320
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    assert (
        load_module_from_file_location(
            location="tests/test_helper/test_config_module.py"
        )
        .test_setting_a
        == "some string"
    )

    assert (
        load_module_from_file_location(
            bytes(
                "tests/test_helper/test_config_module.py", encoding="utf-8"
            )
        )
        .test_setting_a
        == "some string"
    )

    assert (
        load_module_from_file_location(
            location=Path("tests/test_helper/test_config_module.py")
        )
        .test_setting_a
        == "some string"
    )

# Generated at 2022-06-14 08:17:11.709578
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    file_path = Path(__file__).parent / "load_module_from_file_location"
    file_path_ = str(file_path.resolve())

    # Check if file_path ends with some_module_name.py
    assert file_path_.endswith("some_module_name.py")

    # Import some_module_name.py as some_module_name via importlib.
    some_module_name_path = Path("some_module_name.py")
    abs_some_module_name_path = file_path / some_module_name_path
    some_module_name = load_module_from_file_location(abs_some_module_name_path)

    # Check if some_module_name.py was imported correctly.

# Generated at 2022-06-14 08:17:26.611076
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # Arrange
    location = "some_module_name"
    os_environ["some_env_var"] = "some_value"
    spec = spec_from_file_location(
        location,
        "some_module_name",
        "/some/path/${some_env_var}"
    )
    module = module_from_spec(spec)
    module.__file__ = "/some/path/some_value"
    spec.loader.exec_module(module)

    # Act
    loaded_module = load_module_from_file_location(
        location,
        "/some/path/${some_env_var}"
    )

    # Assert
    assert loaded_module == module

# Generated at 2022-06-14 08:17:38.894577
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """
    Here is located unit test for function
    load_module_from_file_location.
    """
    test_config_1 = """
    SERVER_NAME = "server1"
    """

    test_config_2 = """
    SERVER_NAME = "server2"
    """

    test_config_3 = """
    SERVER_NAME = "server3"
    """

    test_path = Path(tempfile.mkdtemp())
    test_config_1_path = Path(
        test_path / "test_config_1.py"
    )
    test_config_1_path.write_text(test_config_1)
    test_config_2_path = Path(
        test_path / "test_config_2.py"
    )
    test_config_2_path

# Generated at 2022-06-14 08:17:50.799715
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # type: ignore
    """Test load_module_from_file_location function."""
    # A) Check that location is of a bytes type and location has
    #    environment variables in it.

    # 1) Set environment variables and check that they are set.
    os_environ["TEST_VAR_1"] = "TEST_VAR_1_VALUE"
    os_environ["TEST_VAR_2"] = "TEST_VAR_2_VALUE"
    os_environ["TEST_VAR_3"] = "TEST_VAR_3_VALUE"
    assert os.getenv("TEST_VAR_1") == "TEST_VAR_1_VALUE"
    assert os.getenv("TEST_VAR_2") == "TEST_VAR_2_VALUE"
   

# Generated at 2022-06-14 08:17:58.591858
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from functools import partial

    from copy import copy

    from numpy.random import randint
    from numpy.testing import assert_array_equal, assert_equal

    from pytest import raises

    from sys import modules

    from types import ModuleType

    # Creation of a random module name
    rand_mod_name = "".join(chr(randint(2 ** 8)) for _ in range(randint(100)))

    # Creation of a random location
    rand_location = Path(
        "".join(chr(randint(2 ** 8)) for _ in range(randint(100)))
    )

    # Creation of a random module object
    rand_mod = ModuleType(rand_mod_name)
    setattr(rand_mod, "__file__", str(rand_location))


# Generated at 2022-06-14 08:18:10.877074
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from os import environ as os_environ
    from pathlib import Path
    from tempfile import TemporaryFile, TemporaryDirectory
    from unittest.mock import patch

    with patch.dict(os_environ, {"TEST_ENV_VAR": "TEST"}):
        assert os_environ["TEST_ENV_VAR"] == "TEST"
        with TemporaryDirectory() as tempdir:
            with TemporaryFile(mode="a+") as file:
                # Should load config files
                file.write("test = 1")
                file.seek(0)
                assert load_module_from_file_location(
                    file.name
                ).test == 1
                # Should load python files