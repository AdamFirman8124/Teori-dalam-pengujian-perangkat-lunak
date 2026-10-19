

# Generated at 2022-06-14 08:08:25.787364
# Unit test for function str_to_bool
def test_str_to_bool():
    data = [
        ("y", True),
        ("yes", True),
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

    for val, expected in data:
        try:
            assert str_to_bool(val) == expected
        except ValueError:
            raise ValueError("Invalid truth value %s" % val)

# Generated at 2022-06-14 08:08:39.029966
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    from io import BytesIO
    from configparser import ConfigParser

    from os import environ as os_environ
    from random import random
    from string import ascii_lowercase, digits

    from pytest import raises

    # For python 3.8 and newer we can use module_from_spec(...).__name__
    # to get module name, but for older python versions we have to
    # receive a module name from user.
    def get_module_name(module):
        for name, val in module.__dict__.items():
            if val is module:
                return name

    # Random string will be used in testing some env variables.
    rand_str = "".join(
        ascii_lowercase[int(random() * 26)] for i in range(6)
    )

    # A)

# Generated at 2022-06-14 08:08:47.104702
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import sys
    import tempfile

    tmp_dir = tempfile.TemporaryDirectory()
    tmp_dir_name = tmp_dir.name

    # A) Save config file
    config = """
        SECRET = "this is secret"
        DEBUG = True
    """
    with tempfile.NamedTemporaryFile(mode="w", suffix=".py", dir=tmp_dir_name) as f:
        f.write(config)
        f.flush()
        config_file_name = f.name

    # B) Try to load saved config file
    config = load_module_from_file_location(config_file_name)

    # C) Make sure that config has variables SECRET and DEBUG
    assert config.SECRET == "this is secret"
    assert config.DEBUG == True


    # A) Save config file


# Generated at 2022-06-14 08:08:50.661744
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    with tempfile.TemporaryDirectory() as tmpdirname:
        file_name = "tmp_file"
        file_path = Path(tmpdirname) / file_name
        file_path.write_text("some content")

        module  = load_module_from_file_location(file_path)
        assert module.__name__ == file_name

        module = load_module_from_file_location(file_path / "some/invalid/path")
        assert not module
        assert not module.__name__


# Generated at 2022-06-14 08:08:59.219362
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    from os import environ, pathsep, path as os_path
    from tempfile import NamedTemporaryFile, TemporaryDirectory
    from unittest import mock

    import pytest

    from sanic.config import load_module_from_file_location, str_to_bool

    from sanic import Sanic

    # Case 1.
    with pytest.raises(IOError):
        load_module_from_file_location("")

    # Case 2.
    with pytest.raises(IOError):
        load_module_from_file_location(1)

    # Case 3.
    with pytest.raises(IOError):
        load_module_from_file_location(True)

    # Case 4.
    with pytest.raises(IOError):
        load_module_from_file

# Generated at 2022-06-14 08:09:11.392640
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Test function load_module_from_file_location."""
    import pytest
    from sanic.exceptions import LoadFileException, PyFileError

    # Test for raising LoadFileException because specified file does not exist.
    with pytest.raises(LoadFileException):
        load_module_from_file_location("not_existing_file.py")
    # Test for raising exception when env_var_in_path is not set.
    with pytest.raises(LoadFileException):
        load_module_from_file_location(
            "some_module_name", "/some/path/${some_env_var}"
        )

    # Test for raising PyFileError.
    # Set path to file with invalid syntax and try
    # to load this file.
    # It should raise PyFileError.

# Generated at 2022-06-14 08:09:22.721968
# Unit test for function str_to_bool
def test_str_to_bool():
    assert str_to_bool("y") is True
    assert str_to_bool("t") is True
    assert str_to_bool("1") is True
    assert str_to_bool("yes") is True
    assert str_to_bool("yup") is True
    assert str_to_bool("Y") is True

    assert str_to_bool("n") is False
    assert str_to_bool("f") is False
    assert str_to_bool("0") is False
    assert str_to_bool("no") is False
    assert str_to_bool("off") is False
    assert str_to_bool("n") is False

    with pytest.raises(ValueError):
        str_to_bool("not")

# Generated at 2022-06-14 08:09:32.373563
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    assert hasattr(
        load_module_from_file_location(__file__), "test_load_module_from_file_location"
    )
    assert hasattr(
        load_module_from_file_location(__file__), "test_load_module_from_file_location"
    )
    assert hasattr(
        load_module_from_file_location(
            "./tests/test_helpers.py"
        ),
        "test_load_module_from_file_location",
    )
    assert hasattr(
        load_module_from_file_location(
            "./tests/test_helpers.py"
        ),
        "test_load_module_from_file_location",
    )

# Generated at 2022-06-14 08:09:41.884067
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from tempfile import NamedTemporaryFile

    config_data = {
        "string_data_entry": "string",
        "int_data_entry": 1234,
        "float_data_entry": 12.34,
        "list_data_entry": [1, 2, 3, 4],
        "dict_data_entry": {"a": 1, "b": 2},
        "bool_data_entry": False,
    }

    with NamedTemporaryFile("r+") as config_file:
        config_content = []

# Generated at 2022-06-14 08:09:53.088322
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import tempfile
    import shutil


# Generated at 2022-06-14 08:10:08.021927
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    import tempfile
    import shutil
    import os

    # Create temporary directory.
    tmp_dir = tempfile.mkdtemp()

    # Create a dummy test configuration file
    # in temporary directory.
    with open(os.path.join(tmp_dir, "test_config.py"), "w") as f:
        f.write(
            """
from sanic import Sanic
import uvloop
sanic_app = Sanic('testapp')
sanic_app.config.TEST_CONFIG_KEY = 'some_value'
"""
        )

    # Check if function works with pathlib.Path.
    module = load_module_from_file_location(
        Path(os.path.join(tmp_dir, "test_config.py"))
    )

# Generated at 2022-06-14 08:10:20.526898
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import tempfile

    valid_test_cases = [
        # A) Check if location contains any environment variables
        #    in format ${some_env_var}.
        # B) Check these variables exists in environment.
        # C) Substitute them in location.
        tempfile.TemporaryDirectory(prefix="some_dir_prefix"),
    ]

    valid_path = None

# Generated at 2022-06-14 08:10:29.290300
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Test load_module_from_file_location function

    1) Test with valid file path
    2) Test with file that exists with non-valid file path
    3) Test with non-existing file
    """
    from os import remove
    from pathlib import Path
    from tempfile import NamedTemporaryFile

    import pytest

    # 1) Test with valid file path
    for file_path in [
        "tests/settings/settings.json",
        Path("tests/settings/settings.json"),
        b"tests/settings/settings.json",
    ]:
        config = load_module_from_file_location(file_path)
        assert isinstance(config.SETTINGS, dict)

    # 2) Test with file that exists with non-valid file path

# Generated at 2022-06-14 08:10:41.329016
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location(): # noqa

    import os
    import tempfile

    # 1a) Test passing Path objects.
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.close()
    temp_file_path = Path(temp_file.name)
    os.remove(temp_file_path)
    with tempfile.TemporaryDirectory() as tempdir:
        tempdir_path = Path(tempdir)
        assert (
            load_module_from_file_location(tempdir_path)
            is import_string(tempdir_path.as_posix())
        )
        tempfile_path = tempdir_path.joinpath("temp_file.py")
        with open(tempfile_path, "w") as temp_file:
            temp_file.write("def test(): pass")

# Generated at 2022-06-14 08:10:54.201992
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    # Tests for loading module from file name
    curdir = Path(__file__).resolve().parent

    # 1. Test for correct file name:
    module1 = load_module_from_file_location(
        str(curdir / "../scripts/config.py")
    )
    assert module1.SECRET_KEY == "wert19g8"
    assert module1.PROXIES is None

    # 2. Test for file location, which doesn't exists:
    try:
        load_module_from_file_location(str(curdir / "some_non_existing_file.py"))
        assert False
    except IOError as e:
        assert "Unable to load configuration" in str(e)

    # 3. Test for file location without extension:
    module3 = load_module_from_file_location

# Generated at 2022-06-14 08:11:06.203893
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    def test_load_file():
        """Test load module from file."""
        module = load_module_from_file_location("tests/assets/config.py")
        assert module.CONFIG_FILE == "config.py"
        assert module.CONFIG_PATH == Path("tests/assets/config.py").absolute()

        module = load_module_from_file_location("tests/assets/config")
        assert module.CONFIG_FILE == "config"
        assert module.CONFIG_PATH == Path("tests/assets/config").absolute()

        module = load_module_from_file_location("tests/assets/config.conf")
        assert module.CONFIG_FILE == "config.conf"
        assert module.CONFIG_PATH == Path("tests/assets/config.conf").absolute()


# Generated at 2022-06-14 08:11:12.756484
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Test load_module_from_file_location using a test.py file"""
    _dir = Path(__file__).parent
    try:
        _mod = load_module_from_file_location(
            Path(_dir, "test.py"), "utf8", "r"
        )
        assert _mod.foo == "bar"
        assert _mod.baz["bar"] == "baz"
    except Exception as e:
        pass
    else:
        assert False

# Generated at 2022-06-14 08:11:22.954116
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # pylint: disable=missing-function-docstring
    from tempfile import NamedTemporaryFile

    temp_file = NamedTemporaryFile(mode="w+")
    temp_file.write("l = 'Loaded!'")
    temp_file.flush()

    os_environ["some_env_var"] = temp_file.name

    module = load_module_from_file_location(
        f"${'some_env_var'}", temp_file.name
    )

    assert module.l == "Loaded!"

    temp_file.close()



# Generated at 2022-06-14 08:11:31.289918
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    test_location = "/home/sanic/some/path/${TEST_LOCATION}"
    os_environ["TEST_LOCATION"] = test_location
    expected = load_module_from_file_location(
        test_location, "/home/sanic/some/path/${TEST_LOCATION}"
    )
    assert expected == load_module_from_file_location(
        test_location, "/home/sanic/some/path/${TEST_LOCATION}"
    )



# Generated at 2022-06-14 08:11:44.132220
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import os
    import tempfile

    # A) Create temporary file with some config.
    os.environ["some_env_var"] = "some_env_var_value"
    config_file_content = """
        class TempClass:
            pass
        temp_var = "temp_var_value"
    """

    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".py", dir="/tmp/", delete=False
    ) as f:
        f.write(config_file_content)
        f.close()
        # B) Load this temporary file as module
        temp_module = load_module_from_file_location(
            "some_name", "/tmp/${some_env_var}/" + f.name
        )

        # C) Check if the module import has been done correctly.

# Generated at 2022-06-14 08:11:52.509197
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """For simplicity I used os.environ.get instead of environment variables
    substitution, because I don't want to mess up my environment variables.
    """
    import os
    from os import environ as os_environ
    from pathlib import Path
    from random import choice

    from sanic.helpers import load_module_from_file_location

    from .utils import get_random_string

    # A) Create random module in temporary file.
    file_name = get_random_string()
    file_path = Path(os.environ.get("TEST_TEMP_DIR", os.environ.get("TEMP")))

# Generated at 2022-06-14 08:12:03.496508
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # Test load_module_from_file_location() with
    # environment variable in location parameter.
    os_environ["test_env_var"] = "test/test_config/"
    test_conf = load_module_from_file_location(
        # Assert correct path is made from variables.
        "${test_env_var}test_conf.py",
        # Assert correct name of module is generated.
        *{
            "name": "test_conf",
            # Assert coresponding module is loaded.
            "cached": False,
            "path": "${test_env_var}test_conf.py",
        }.values(),
    )
    assert test_conf.LOREM == "ipsum"

    # Test load_module_from_file_location() with
    # file path as location

# Generated at 2022-06-14 08:12:06.068728
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """
    Write unit test for function load_module_from_file_location
    """
    pass

# Generated at 2022-06-14 08:12:19.171414
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # 0. Test if it raises an exception when passed a string
    #    without '.' or '/' and without '.py' at the end.
    with pytest.raises(
        IOError,
        match=r"Unable to load configuration.*",
    ):
        load_module_from_file_location("test")

    # 1. Create a test file
    with open("test.py", "w") as test_file:
        test_file.write("TEST = 'test'")

    # 2. Try to load a file from current directory
    test_module = load_module_from_file_location("test.py")

    assert test_module.TEST == "test"

    # 3. Try to load a file from current directory

# Generated at 2022-06-14 08:12:30.498414
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import sys
    import io
    import tempfile
    import textwrap
    import unittest
    import os

    import_message = "Hello, I'm imported module"
    import_code = textwrap.dedent(
        f"""
    print("{import_message}")
    var_1 = "test string"
    """
    )

    def load_module(
        module: str,
        code: str,
        temp_dir: tempfile.TemporaryDirectory,
        sys_path: list,
        **kwargs: Any
    ) -> types.ModuleType:
        """Function that creates config.py file, writes some code to it,
        add its path to sys.path and returns this module."""
        file_name = Path(module + ".py")

# Generated at 2022-06-14 08:12:42.134774
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    os_environ["SANIC_CONFIG_FILE_ENV_TEST"] = "True"
    try:
        module = load_module_from_file_location(
            "sanic/tests/config_files/test_config_file.py",
            location="sanic/tests/config_files/${SANIC_CONFIG_FILE_ENV_TEST}.py"
        )
        assert module.USER == "John", "User name should be John."
        assert module.PASSWORD == "Swordfish", "Password should be Swordfish."

    except:
        # Something is broken, failing test
        os_environ.pop("SANIC_CONFIG_FILE_ENV_TEST")
        assert False
    os_environ.pop("SANIC_CONFIG_FILE_ENV_TEST")
    assert True

# Generated at 2022-06-14 08:12:43.993094
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    assert load_module_from_file_location("asyncio") == asyncio

# Generated at 2022-06-14 08:12:54.331435
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    import tempfile

    def create_config_file(content: str, file_path: str = None) -> str:
        if file_path is None:
            with tempfile.NamedTemporaryFile(mode="w+") as tf:
                f = tf.file
                f.write(content)
                f.flush()

                file_path = tf.name

        else:
            with open(file_path, "w") as f:
                f.write(content)
                f.flush()

        return file_path


# Generated at 2022-06-14 08:13:06.010749
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    os_environ["file"] = "file.py"
    os_environ["absolute_path"] = os.path.abspath("file.py")

    test_file = os.path.abspath("file.py")
    test_module = load_module_from_file_location("file.py")
    assert test_module.__file__ == test_file

    test_file = os.path.abspath("file.py")
    test_module = load_module_from_file_location("file")
    assert test_module.__file__ == test_file

    test_file = os.path.abspath("file.py")
    test_module = load_module_from_file_location("test/file.py")
    assert test_module.__file__ == test_file

    test_file

# Generated at 2022-06-14 08:13:17.175396
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # Set some environment variables to check resolving environment variables
    # in file location.
    os_environ["some_env_var"] = "some_value"

    # Check loading valid module.
    some_module = load_module_from_file_location(
        "importlib_test_module.py",
        # Use environment variable in file location
        "${some_env_var}/importlib_test_module.py",
    )
    assert hasattr(some_module, "TEST_CONSTANT")
    assert some_module.TEST_CONSTANT == True  # noqa

    # Check loading of invalid module.

# Generated at 2022-06-14 08:13:30.618908
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # No errors will be raised
    # if requirements are OK.
    assert load_module_from_file_location(
        "sanic", "../sanic/__init__.py"
    )
    assert load_module_from_file_location(
        "test_config", "./test_config.py"
    )
    assert load_module_from_file_location(
        "/home/alice/test_config.py", "./test_config.py"
    )

    assert load_module_from_file_location(
        "test_config", b"./test_config.py"
    )
    assert load_module_from_file_location(
        "test_config",
        b"./test_config.py",
        encoding="utf8",
    )

    assert load_module_from_

# Generated at 2022-06-14 08:13:40.381590
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    # 1) test load module from string path.
    assert {"foo": "bar"} == load_module_from_file_location(
        "config", __file__
    ).__dict__

    # 2) test load module from bytes path.
    assert {"foo": "bar"} == load_module_from_file_location(
        b"config", __file__.encode("utf-8")
    ).__dict__

    # 3) test load module from Path object.
    assert {"foo": "bar"} == load_module_from_file_location(
        Path(__file__), "config"
    ).__dict__

    # 4) Test if module is loaded with $ENV parameters.
    os_environ["some_env_var"] = "some_value"

# Generated at 2022-06-14 08:13:53.721608
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # Case with just file name
    module = load_module_from_file_location(
        "test_load_module_from_file_location.py"
    )
    assert module.__file__ == Path(
        "test_load_module_from_file_location.py"
    ).resolve()

    # Case with path
    module = load_module_from_file_location(
        "tests/test_load_module_from_file_location.py"
    )
    assert module.__file__ == Path(
        "tests/test_load_module_from_file_location.py"
    ).resolve()

    # Case with bytes
    module = load_module_from_file_location(
        Path(__file__).resolve().encode()
    )

# Generated at 2022-06-14 08:14:05.013250
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from shutil import rmtree

    base_path = Path("/tmp/some-dir/some-file.py")
    some_config = bytes("config_var = 'some-val'", "utf8")

    os_environ["some_env_var"] = "some-dir"

    # A) Path doesn't exist
    try:
        load_module_from_file_location(base_path)
    except IOError as e:
        assert e.strerror == "Unable to load configuration file (e.strerror)"
    else:
        assert False, "Should throw an exception"

    # B) Path exists but it isn't a file or directory
    (base_path.parent / "some-file.py").write_text("")


# Generated at 2022-06-14 08:14:17.941324
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    module = load_module_from_file_location(
        "sanic.config.test_app_configs.empty_module"
    )
    assert module.empty_module_var == "empty_module_var"

    module = load_module_from_file_location(
        "sanic.config.test_app_configs.module_with_imports"
    )
    assert module.test_var == "Hello, World!"

    import sanic.config.test_app_configs.empty_module
    module = load_module_from_file_location(
        "sanic.config.test_app_configs.empty_module"
    )
    assert sanic.config.test_app_configs.empty_module == module


# Generated at 2022-06-14 08:14:22.699705
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    location = "tests/config/config.py"
    module = load_module_from_file_location(location)
    assert module.TEST_CONFIG_KEY == "sanic_config"

    location = "tests/config/conf"
    module = load_module_from_file_location(location)
    a

# Generated at 2022-06-14 08:14:33.810238
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Unit test for function load_module_from_file_location."""
    os_environ['ENV_VAR'] = 'some_value'

    module_1 = load_module_from_file_location(__file__)
    assert module_1.__name__ == __name__
    assert module_1.__file__ == __file__

    module_2 = load_module_from_file_location(Path(__file__))
    assert module_2.__name__ == __name__
    assert module_2.__file__ == __file__

    module_3 = load_module_from_file_location('test_load_module_from_file_location', __file__)  # noqa
    assert module_3.__name__ == __name__
    assert module_3.__file__ == __file__



# Generated at 2022-06-14 08:14:38.280019
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    path = Path(__file__)
    testing_config = load_module_from_file_location(path)
    assert testing_config.TEST is True
    assert testing_config.TEST_DICT == {"a": 1, "b": 2}

# Generated at 2022-06-14 08:14:51.374500
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from random import randint
    from time import time
    from tempfile import NamedTemporaryFile

    import_string_original = import_string.__original__
    test_module_name = "test_module_" + str(int(time()))
    test_module: types.ModuleType = types.ModuleType(test_module_name)
    # We are monkey patching import_string to return our module
    import_string = lambda _: test_module  # type: ignore

    # Test with module name
    tested_module = load_module_from_file_location(test_module_name)
    assert tested_module == test_module

    # Test with module name and .py extension
    tested_module = load_module_from_file_location(test_module_name + ".py")
    assert tested_module == test_module



# Generated at 2022-06-14 08:14:53.659536
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import doctest

    doctest.testmod(optionflags=doctest.ELLIPSIS)

# Generated at 2022-06-14 08:15:08.931219
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    # Test exception:
    # if not isinstance(location, Path) or "/" in location or "$" in location:
    with pytest.raises(LoadFileException):
        load_module_from_file_location(
            "module_name",
            Path("/some/path/${some_env_var}"),
            encoding="utf8",
        )

        load_module_from_file_location(
            b"module_name",
            b"/some/path/${some_env_var}",
            encoding="utf8",
        )

        load_module_from_file_location(
            "module_name",
            "/some/path/${some_env_var}",
            encoding="utf8",
        )

    with pytest.raises(LoadFileException):
        load_module_from_

# Generated at 2022-06-14 08:15:20.928751
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    file_path = "/path/to/conf/file.py"

    # 1. Test a normal use case
    location = file_path
    module = load_module_from_file_location(location)
    assert module.__name__ == "file"

    # 2. Test a case when we provide environment variable
    location = "/path/to/${HOME}/conf/file.py"
    module = load_module_from_file_location(location)
    assert module.__name__ == "file"

    # 3. Test a case when we provide not defined environment variable
    location = "/path/to/${UNDEFINED}/conf/file.py"
    with pytest.raises(LoadFileException):
        load_module_from_file_location(location)

    # 4. Test a case when we provide file that is

# Generated at 2022-06-14 08:15:33.556152
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # A) Check if we can load the file with the given path and
    #    the path is of type str.
    from random import randint
    from string import ascii_letters
    from tempfile import NamedTemporaryFile

    with NamedTemporaryFile(suffix=".py", delete=False) as temp_file:
        file_name = temp_file.name
        temp_file.writelines('foo = "bar"')
    loaded_module = load_module_from_file_location(file_name)
    assert hasattr(loaded_module, "foo") and loaded_module.foo == "bar"
    # B) Check if we can load the file with the given path and
    #    the path is of type Path.
    temp_path = Path(file_name)
    loaded_module = load_module_from_file

# Generated at 2022-06-14 08:15:44.284321
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # test with normal string file path
    assert load_module_from_file_location(__file__).__name__ == "sanic.config"
    # test with bytes file path
    assert load_module_from_file_location(
        __file__.encode()
    ).__name__ == "sanic.config"
    # test with environment variables in file path
    assert load_module_from_file_location(
        "${SANIC_TEST_FILE_LOCATION}"
    ).__name__ == "sanic.config"
    # test with Path object file path
    assert load_module_from_file_location(Path(__file__)).__name__ == "sanic.config"
    # test with Path object file path

# Generated at 2022-06-14 08:15:57.353645
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import tempfile
    import os

    # A) Testing location with environment variables in format ${ENV_VAR}:

    os.environ["ENV_VAR_TEST_BASIC"] = "VALUE_BASIC"
    os.environ["ENV_VAR_TEST_MORE"] = "VALUE_MORE"
    os.environ["ENV_VAR_TEST_EVERY_WHERE"] = "VALUE_EVERY_WHERE"


# Generated at 2022-06-14 08:16:07.329853
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # noqa
    import tempfile
    from copy import copy
    from os import environ, path

    def _write_file(filename, s):
        with open(filename, "w") as f:
            f.write(s)

    def _write_py(filename, s):
        _write_file(filename, "import sys\n" + s)

    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = path.realpath(tmpdir)
        test_env_var = "TEST_ENV_VAR"
        environ[test_env_var] = tmpdir
        test_env_var_path = path.join(tmpdir, "test_env_var")
        content_path = path.join(tmpdir, "test_config")

# Generated at 2022-06-14 08:16:18.230958
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # Check that all imports work as expected
    import os
    import re
    import time
    import builtins as __builtin__
    import types as __types
    import typing as __typing

    assert os is not None
    assert re is not None
    assert time is not None
    assert __builtin__ is not None
    assert __types is not None
    assert __typing is not None

    # Check that exceptions are correctly raised
    import pytest

    with pytest.raises(Exception):
        raise Exception("Test")

    # Check that exceptions are correctly raised
    with pytest.raises(PyFileError):
        raise PyFileError("Test")

    # Check that load_module_from_file_location function works as expected
    from sanic.config import load_module_from_file_location
    import os

# Generated at 2022-06-14 08:16:31.536154
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    def test_no_environ_vars(location):
        with open(location) as f:
            content = f.read()
        assert load_module_from_file_location(location).__file__ == location
        assert load_module_from_file_location(location).content == content
        assert import_string(location).__file__ == location
        assert import_string(location).content == content

    def test_with_environ_vars(location, environ_var1, environ_var2):
        with open(location) as f:
            content = f.read()
        os_environ[environ_var1] = environ_var1
        os_environ[environ_var2] = environ_var2
        assert load_module_from_file_location(location).__file__ == location

# Generated at 2022-06-14 08:16:42.257596
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import sys

    # Some fake environment variables
    os_environ["test_env_var_1"] = "test_env"
    os_environ["test_env_var_2"] = "test_env"

    # Create some fake module
    test_module_file_name = "test_module_name"
    test_module_file_location = "/tmp/" + test_module_file_name + ".py"
    with open(test_module_file_location, "w") as f:
        f.write(
            "test_var_1 = 'test_value_1'\r\ntest_var_2 = 'test_value_2'"
        )
    module = load_module_from_file_location(
        test_module_file_location,
    )

    # Check if it works
    sys

# Generated at 2022-06-14 08:16:53.459311
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    path_to_example_config_fixtures_dir = (
        Path(__file__).absolute().parent
        / "example_config_fixtures"
    )

    # Case 1) Check if function can handle file path
    #         as a string type.
    path_to_example_config_fixtures_dir = str(
        path_to_example_config_fixtures_dir
    )
    module_config_string = load_module_from_file_location(
        path_to_example_config_fixtures_dir
        + "/example_config_string.py"
    )
    assert module_config_string.EXAMPLE_STRING == "string"

    # Case 2) Check if function can handle file path
    #         as a bytes type.

# Generated at 2022-06-14 08:17:02.090805
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # Unit test for function load_module_from_file_location
    module = load_module_from_file_location(
        """test_module_name""", f"""{Path(__file__).parent}/test_utils.py""",
    )
    assert module.test_utils_variable == "some_value"

# Generated at 2022-06-14 08:17:11.747131
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import tempfile
    from shutil import rmtree
    from tempfile import TemporaryDirectory

    def create_mock_module(module_name: str, module_content: dict) -> Path:

        with tempfile.TemporaryDirectory() as temp_dir_name:
            module_location = Path(temp_dir_name) / (module_name + ".py")

            with open(module_location, "w") as target:
                target.write("\n".join([f"{key} = {value}" for key, value in module_content.items()]))

            return module_location

    # A) Test load_module_from_file_location with real python file.
    module_content = {"a": 1, "b": 2}

# Generated at 2022-06-14 08:17:17.887072
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from tempfile import NamedTemporaryFile

    with NamedTemporaryFile(mode="w", delete=False) as tmp_py_file:
        tmp_py_file.write("some_var = True")

    try:
        module = load_module_from_file_location(tmp_py_file.name)
        assert module.some_var
    finally:
        os.remove(tmp_py_file.name)

# Generated at 2022-06-14 08:17:27.710743
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from test.test_utils.random_generator import string_generator

    some_location = "some_location"

    config_module = load_module_from_file_location(some_location)

    assert config_module.__name__ == "config"
    assert config_module.__file__ == some_location
    assert config_module.__package__ is None

    random_env_var_value = string_generator()

    os_environ["TEST_UTILS_TEST_ENV_VAR_RANDOM"] = random_env_var_value

    config_module = load_module_from_file_location(
        f"{some_location}/${{TEST_UTILS_TEST_ENV_VAR_RANDOM}}"
    )


# Generated at 2022-06-14 08:17:39.331616
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # A) Check error case:
    #    pass to function some_var which is not loadable.
    some_var = 1
    try:
        load_module_from_file_location(some_var)
    except LoadFileException as e:
        # Add assert if you want to check that exception is raised here.
        pass

    # B) Check error case:
    #    pass to function environment variable which does not exist.
    try:
        load_module_from_file_location(
            "/some/path/${some_environment_variable_which_does_not_exist}"
        )
    except LoadFileException as e:
        # Add assert if you want to check that exception is raised here.
        pass

    # C) Check normal case:
    #    pass to function module from file.
    #    This file should contain

# Generated at 2022-06-14 08:17:47.604081
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # pragma: no cover
    location = os.path.dirname(__file__) + "/test_load_module_from_file_location"
    module = load_module_from_file_location(location)
    assert isinstance(module, types.ModuleType)
    assert module.__name__ == "test_load_module_from_file_location"
    assert module.a == "a"
    assert module.b == "b"
    return True



# Generated at 2022-06-14 08:17:57.258491
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    assert load_module_from_file_location("sys") == sys
    with open("temp_file", "w") as tf:
        tf.write("hello = 'world'\n")

    assert load_module_from_file_location("temp_file").hello == "world"

    # In the next line . Path objects with the same path are compared.
    # The problem is that in python3.5 and python3.6 __fspath__ does not
    # exist and Path object is not recognized as a string, so == operator
    # return always False. In python3.7 and above __fspath__ exist, so
    # == operator again works as expected.
    #
    # Thus to make this unit test work in any version of python,
    # Path objects are converted to str before comparing.
    #
    # It is also possible to

# Generated at 2022-06-14 08:18:06.329542
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    path = os.path.abspath("test/test_test_config.json")
    module = load_module_from_file_location(path)
    assert module.TEST == "test"
    assert module.FALSE_TEST == False
    assert module.TRUE_TEST == True

    os_environ["test_variable"] = "test/test_test_config.json"
    module = load_module_from_file_location(
        "/${test_variable}", encoding="utf8"
    )
    assert module.TEST == "test"

# Generated at 2022-06-14 08:18:16.597857
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    """Test if load_module_from_file_location works properly."""
    import tempfile
    import os

    # Test for normal functionality
    # 1) Test for normal functionality
    content = "some_type = 3"
    handle, tmp_file_path = tempfile.mkstemp(suffix=".py")
    with open(tmp_file_path, "w") as tmp_file:
        tmp_file.write(content)

    module = load_module_from_file_location(tmp_file_path)
    assert module.some_type == 3
    os.remove(tmp_file_path)

    # Test for normal functionality
    # 2) Test with str_to_bool
    content = "some_type = 'on'"