

# Generated at 2022-06-14 08:08:26.417784
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # Should raise LoadFileException
    # cause of not defined environment variable ${some_env_var}.
    with pytest.raises(LoadFileException):
        load_module_from_file_location("/some/path/${some_env_var}")

    # Should load module without errors in a normal way.
    load_module_from_file_location("/some/path/to/module.py")

    # Should load module with environment variable substitution.
    os_environ["some_env_var"] = "some_path_value"
    load_module_from_file_location("/some/path/${some_env_var}/module.py")
    # Cleanup.
    del os_environ["some_env_var"]  # noqa

    # Should load module without errors even without .py extension.
    #

# Generated at 2022-06-14 08:08:39.242042
# Unit test for function str_to_bool
def test_str_to_bool():
    f1 = "y"
    f2 = "yes"
    f3 = "yep"
    f4 = "yup"
    f5 = "t"
    f6 = "true"
    f7 = "on"
    f8 = "enable"
    f9 = "enabled"
    f10 = "1"
    check1 = str_to_bool(f1)
    check2 = str_to_bool(f2)
    check3 = str_to_bool(f3)
    check4 = str_to_bool(f4)
    check5 = str_to_bool(f5)
    check6 = str_to_bool(f6)
    check7 = str_to_bool(f7)
    check8 = str_to_bool(f8)
    check9 = str

# Generated at 2022-06-14 08:08:51.489245
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    assert not load_module_from_file_location(b"boolean.py")
    assert load_module_from_file_location(b"boolean.py").BOOLEAN
    assert not load_module_from_file_location("./boolean.py")
    assert load_module_from_file_location("./boolean.py").BOOLEAN
    assert not load_module_from_file_location(__file__.encode())
    assert load_module_from_file_location(__file__.encode()).BOOLEAN
    assert not load_module_from_file_location(__file__)
    assert load_module_from_file_location(__file__).BOOLEAN
    assert not load_module_from_file_location(Path(__file__))
    assert load_

# Generated at 2022-06-14 08:09:00.198187
# Unit test for function str_to_bool
def test_str_to_bool():
    assert str_to_bool("no") == False
    assert str_to_bool("yes") == True
    assert str_to_bool("1") == True
    assert str_to_bool("0") == False
    assert str_to_bool("True") == True
    assert str_to_bool("false") == False
    assert str_to_bool("OFF") == False
    assert str_to_bool("ON") == True
    assert str_to_bool("no") == False
    assert str_to_bool("yes") == True
    assert str_to_bool("1") == True
    assert str_to_bool("0") == False
    assert str_to_bool("True") == True
    assert str_to_bool("false") == False
    assert str_to_bool("OFF") == False
    assert str_

# Generated at 2022-06-14 08:09:12.244889
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    from os import environ as os_environ
    from os import makedirs
    from os import mkdir
    from os import remove as os_remove
    from os import urandom
    from os import walk
    from shutil import rmtree

    from tempfile import gettempdir
    from tempfile import mktemp

    from types import ModuleType

    from pathlib import Path

    from importlib.util import module_from_spec
    from importlib.util import spec_from_file_location

    from hypothesis import given
    from hypothesis.strategies import binary
    from hypothesis.strategies import booleans
    from hypothesis.strategies import dictionaries
    from hypothesis.strategies import integers
    from hypothesis.strategies import lists
    from hypothesis.strategies import text


# Generated at 2022-06-14 08:09:23.988434
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import random
    import string

    # Test A (with pathlib.Path)
    path = "/tmp/" + "".join(
        random.choice(string.ascii_letters)
        for _ in range(random.randint(5, 10))
    )
    location = Path("/tmp/") / path
    location.write_text("some content")
    module = load_module_from_file_location(location)
    assert module.__file__ == str(location)
    location.unlink()

    # Test B (with non existing path)
    with pytest.raises(LoadFileException):
        load_module_from_file_location("/tmp/does_not_exists")

    # Test C (with os.environ var)

# Generated at 2022-06-14 08:09:31.925540
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    some_module = load_module_from_file_location(
        "some_module_name", "/some/path/${some_env_var}"
    )

    assert some_module.__name__ == "some_module_name"
    assert some_module.__file__ == "/some/path/${some_env_var}"

    assert str_to_bool("1") is True
    assert str_to_bool("0") is False
    assert str_to_bool("Y") is True
    assert str_to_bool("N") is False

    try:
        str_to_bool("qwerty")
    except ValueError:
        assert True

# Generated at 2022-06-14 08:09:41.677596
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    os_environ["some_env_var"] = "some_env_var_value"

    # A) Test location as string.
    assert load_module_from_file_location("tests/test_location")

    # B) Test location as string with some environment variables in it.
    assert (
        load_module_from_file_location("tests/${some_env_var}_location")
    )

    # C) Test location as path.
    assert load_module_from_file_location(Path("tests/test_location"))

    # D) Test location as path with some environment variables in it.
    assert (
        load_module_from_file_location(
            Path("tests/${some_env_var}_location")
        )
    )

    # E) Test location as bytes.
    assert load_module

# Generated at 2022-06-14 08:09:52.984976
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import os
    import tempfile
    from sanic.log import logger

    temp_dir = tempfile.gettempdir()
    logger.info(f"temp_dir: {temp_dir}")

    module_1 = load_module_from_file_location(Path(temp_dir, "__init__.py"))

    module_2 = load_module_from_file_location(
        Path(temp_dir, "__init__.py"), submodule_search_locations=temp_dir
    )

    module_3 = load_module_from_file_location(
        Path(temp_dir, "__init__.py").as_posix(),
        submodule_search_locations=[temp_dir],
    )


# Generated at 2022-06-14 08:09:59.999958
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    """ create file that returns a value """
    Path("test_load_module_from_file_location").touch()
    with open("test_load_module_from_file_location", "w") as file:
        file.write("a = 1")

    module = load_module_from_file_location(
        "test_load_module_from_file_location", "utf8"
    )

    """ assert that the value was returned from the file """
    assert module.a == 1



# Generated at 2022-06-14 08:10:15.438018
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    os_environ["SOME_ENV_VAR"] = "some_value"
    module = load_module_from_file_location("tests/mytest.py")
    assert module.name == "value"

    module = load_module_from_file_location("tests/${SOME_ENV_VAR}/mytest.py")
    assert module.name == "value"

    module = load_module_from_file_location("tests/mytest")
    assert module.name == "value"

    module = load_module_from_file_location("tests/${SOME_ENV_VAR}/mytest")
    assert module.name == "value"

    del os_environ["SOME_ENV_VAR"]
    with pytest.raises(LoadFileException):
        load_module_

# Generated at 2022-06-14 08:10:26.459305
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from unittest import TestCase
    from os import environ, remove
    from tempfile import NamedTemporaryFile as NTF
    import json

    class TestLoadModuleFromFileLocation(TestCase):
        def setUp(self):
            self.env_variables = dict(
                var_1="some_path/",
                var_2="some_module.py",
                var_3="some_module.json",
            )
            environ.update(self.env_variables)

        def tearDown(self):
            environ.clear()
            environ.update(self.env_variables)


# Generated at 2022-06-14 08:10:39.583342
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    os_environ["MODULE_PATH"] = "."

    # Check if we can load module provided as path
    # without any environment variables.
    module = load_module_from_file_location("sanic/config.py")
    assert module.TESTING

    # Check if we can load module provided as path
    # with environment variables in format ${some_env_var}
    # and these some_env_var are defined in os.environ.
    module = load_module_from_file_location("${MODULE_PATH}/config.py")
    assert module.TESTING

    # Check that LoadFileException is raised
    # when module provided as path contain
    # environment variables which are not defined in os.environ.

# Generated at 2022-06-14 08:10:51.207594
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # load_module_from_file_location(location) cases:
    # 1) We provide path to a py file
    assert not hasattr(
        load_module_from_file_location(
            Path(__file__).parent / "test_util_file.py"
        ),
        "sanic_config",
    )
    # 2) We provide path to non-py file
    assert not hasattr(
        load_module_from_file_location(
            Path(__file__).parent / "test_util_file.txt"
        ),
        "sanic_config",
    )
    # 3) We provide str path to non-py file

# Generated at 2022-06-14 08:11:02.032196
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from inspect import ismodule
    from sanic.log import logger

    logger.warning(
        "Function load_module_from_file_location is tested only"
        "in unittests_fly_test function."
    )

    def assert_load_module_from_file_location_returns_module(
        location, *args, **kwargs
    ):
        assert ismodule(
            load_module_from_file_location(location, *args, **kwargs)
        )

    assert_load_module_from_file_location_returns_module(
        "${PATH_TO_PYTHON_EXECUTABLE}/config/test_module.py"
    )


# Generated at 2022-06-14 08:11:15.046582
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from os import getcwd, makedirs, remove
    from os.path import dirname
    from tempfile import gettempdir

    from sanic.exceptions import PyFileError

    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )

    def create_test_file(content):
        return Path(
            gettempdir() + "/sanic_test_config.py"
        ).open(mode="w+").write(content)

    def remove_test_file():
        return Path(gettempdir() + "/sanic_test_config.py").unlink()

    def test(content=None, error=None):
        create_test_file(content)

# Generated at 2022-06-14 08:11:29.127611
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from os import environ
    from pathlib import Path
    from shutil import rmtree, copy2 as shutil_copy2, move as shutil_move
    from tempfile import mkdtemp

    # ----------------------
    # --- Test Parameters ---
    # ----------------------

    project_path = Path(__file__).parent.parent
    path_to_nonpy_file = project_path / "tests/files/nonpy_file"
    path_to_py_file = project_path / "tests/files/py_file.py"

    test_dir_path = Path(mkdtemp())
    test_dir_path.mkdir(exist_ok=True)

    environ["SOME_ENV_VAR"] = str(test_dir_path)

    test_nonpy_file_path = test_dir_path

# Generated at 2022-06-14 08:11:35.717646
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import os
    import tempfile
    from shutil import rmtree

    from sanic.exceptions import LoadFileException, PyFileError

    tmpdir_path = Path(tempfile.gettempdir()) / "sanic_test_config"
    if not tmpdir_path.is_dir():
        tmpdir_path.mkdir()

    some_config_file_path = tmpdir_path / "some_config.py"

    with some_config_file_path.open("w") as f:
        f.write("CONFIG = 'some_config'")


# Generated at 2022-06-14 08:11:46.586987
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import sys
    import os
    import tempfile
    import shutil
    import pytest
    import subprocess
    
    def create_file(path, content):
        if content is None:
            return
        with open(path, 'w') as f:
            f.write(content)

    def create_file_tree(contents):
        """
        Creates a file tree and returns the path to the root
        """
        tempdir = tempfile.TemporaryDirectory()
        path = Path(tempdir.name)
        for k,v in contents.items():
            if isinstance(v, str):
                create_file(path / k, v)
            else:
                create_file_tree(v)

        return path
    
    def test_file_tree(contents):
        root = create_file_

# Generated at 2022-06-14 08:12:00.323530
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    # Test 1: test with absolute path
    print("-" * 30)
    print("Test 1: Test with absolute path")
    some_module = load_module_from_file_location("/some/path/some_module.py")
    assert some_module.__name__ == "some_module"
    assert some_module.__file__ == "/some/path/some_module.py"

    # Test 2: test with relative path
    print("-" * 30)
    print("Test 2: Test with relative path")
    import os

    dirname = os.path.dirname(os.path.abspath(__file__))
    some_module = load_module_from_file_location(
        f"{dirname}/tests/some_module.py"
    )

# Generated at 2022-06-14 08:12:05.085213
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # TODO - these will require /tmp/ and environment variables

    pass

# Generated at 2022-06-14 08:12:18.407838
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import tempfile
    import os

    # A) Check if it works for simple cases
    tmp_file1 = tempfile.NamedTemporaryFile(mode="w+")
    tmp_file1.write("X = 'some_string'")
    tmp_file1.seek(0)
    tmp_file1_name = tmp_file1.name

    tmp_file2 = tempfile.NamedTemporaryFile(mode="w+")
    tmp_file2.write("X = 'some_other_string'")
    tmp_file2.seek(0)
    tmp_file2_name = tmp_file2.name

    module1 = load_module_from_file_location(tmp_file1_name)
    module2 = load_module_from_file_location(tmp_file2_name)

    assert module1

# Generated at 2022-06-14 08:12:29.838707
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    assert load_module_from_file_location("os", encoding="latin-1") is os
    assert load_module_from_file_location(b"os", encoding="latin-1") is os
    assert load_module_from_file_location(__file__, encoding="latin-1") is os
    assert load_module_from_file_location(Path(__file__), encoding="latin-1") is os

    # Setting environment variables
    os_environ["TEMP_ENV"] = "This is temporary environment variable"
    assert load_module_from_file_location(
        "os",
        "/tmp/${TEMP_ENV}",
    ) is os

    os_environ["TEMP_ENV"] = "This is temporary environment variable"
    assert load_module_from_file_location

# Generated at 2022-06-14 08:12:39.180828
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    import os

    import pytest

    from sanic.exceptions import PyFileError

    from sanic.helpers import load_module_from_file_location

    assert load_module_from_file_location("os.path") == os.path
    assert load_module_from_file_location("os").path == os.path
    assert load_module_from_file_location(
        __file__
    ) == load_module_from_file_location("__file__")

    with pytest.raises(ValueError):
        load_module_from_file_location("SanicIsTheBest")

    with pytest.raises(PyFileError):
        load_module_from_file_location(__file__ + "a")

    with pytest.raises(LoadFileException):
        load_module_from_file

# Generated at 2022-06-14 08:12:51.805977
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """
    Test cases:
        - Path object
        - str
        - bytes
        - module object
        - environment variables
        - exception
    """
    # Path object
    os_environ["some_env_var_path"] = "."
    # test function
    location = Path(".")
    module = load_module_from_file_location(location)
    assert "load_module" in module.__file__
    assert "switcher" in module.__file__
    del os_environ["some_env_var_path"]

    # str
    os_environ["some_env_var_str"] = "."
    # test function
    location = "${some_env_var_str}"
    module = load_module_from_file_location(location)

# Generated at 2022-06-14 08:13:02.327804
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Ensure that load_module_from_file_location returns the same result
    as importlib.util.module_from_spec.

    To test this function we have to mock _spec_from_file_location function
    as it is a private function in importlib.util.
    """

    def mocked_module_from_spec(
        _spec_from_file_location_mock: types.ModuleType
    ) -> types.ModuleType:
        """Mocked module_from_spec function."""
        _module_from_spec_mock = types.ModuleType("mocked_module_from_spec")
        _module_from_spec_mock.__class__ = _spec_from_file_location_mock
        return _module_from_spec_mock


# Generated at 2022-06-14 08:13:14.506123
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from os import rename, makedirs
    from shutil import rmtree, copy
    from tempfile import mkdtemp
    from random import Random
    from string import ascii_lowercase

    def random_string(length: int) -> str:
        return "".join(Random().choices(ascii_lowercase, k=length))

    tmp_dir_path = Path(mkdtemp())

# Generated at 2022-06-14 08:13:19.999911
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    location = Path(__file__).parent / "configs/app_config.py"
    app_config = load_module_from_file_location(location)
    assert "TEST_VAR_TO_BE_FOUND" in app_config.__dict__
    assert app_config.TEST_VAR_TO_BE_FOUND == "test"



# Generated at 2022-06-14 08:13:31.813468
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import baby.baby

    assert load_module_from_file_location("baby") == baby.baby
    import warnings

    warnings.simplefilter("error")
    with baby.baby as baby:
        assert baby == "baby"

    assert baby.baby.__file__ == "sanic/baby/baby.py"

    assert baby.baby.__package__ == "sanic.baby"
    import os

    os.environ["SANIC_TEST"] = "0"
    os.environ["SANIC_TEST_2"] = "0"
    with warnings.catch_warnings(record=True) as w:
        assert load_module_from_file_location(
            "sanic/baby/baby.py"
        ) == baby.baby

    assert len(w) == 0


# Generated at 2022-06-14 08:13:44.154526
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    correct_config = '''
import os

TEST_VARIABLE = 'true'
PATH_TO_TEST = os.environ.get('PATH')
'''

    incorrect_config = '''
NON_EXISTED_IMPORT = __import__('NON_EXISTED_IMPORT')
'''

    with tempfile.TemporaryDirectory() as temp_dir:
        correct_config_path = Path(temp_dir) / "correct_config.py"
        incorrect_config_path = Path(temp_dir) / "incorrect_config.py"

        with open(correct_config_path, "w") as fp:
            fp.write(correct_config)

        with open(incorrect_config_path, "w") as fp:
            fp.write(incorrect_config)

# Generated at 2022-06-14 08:14:03.686580
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from os import environ, makedirs
    from os.path import join
    from tempfile import gettempdir
    from unittest import TestCase
    from uuid import uuid4

    test_location = join(gettempdir(), f"{uuid4()}")
    makedirs(test_location, exist_ok=True)

    module_name = str(uuid4())
    with open(join(test_location, f"{module_name}.py"), "w") as f:
        f.write("some_value = 'Hello world!'")

    environ["SOME_ENV_VAR"] = test_location

    module_path = f"${{SOME_ENV_VAR}}/{module_name}.py"


# Generated at 2022-06-14 08:14:17.111969
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    def check_env_vars(location):
        try:
            load_module_from_file_location(location)
        except LoadFileException as e:
            assert "The following environment variables are not set: " in str(e)

    def load_from_file(location):
        return load_module_from_file_location(location)

    def load_from_bytes(location):
        return load_module_from_file_location(location.encode())

    def load_from_path(location):
        return load_module_from_file_location(Path(location))

    # Check if we can load module from a string.
    with open(__file__) as f:
        f_str = f.read()
    assert __name__ == load_from_file(__file__).__name__
    assert f_

# Generated at 2022-06-14 08:14:27.890568
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    os_environ["first_var"] = "my_var"
    os_environ["first_var2"] = "my_var"

    if not os.path.exists("test_dir"):
        os.makedirs("test_dir")

    test_file = open("test_dir/test_file.py", "w")
    test_file.write("test_data = 'test_data'")
    test_file.close()

    module = load_module_from_file_location(
        "test_dir/test_file.py", "/test/${first_var}", "test_file.py"
    )
    assert module.test_data == "test_data"


# Generated at 2022-06-14 08:14:36.205262
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    os_environ['SANIC_SETTING_B'] = "test"
    # For example You can:
    #  some_module = load_module_from_file_location(
    #      "some_module_name",
    #      "/some/path/${some_env_var}"
    #  )
    #
    #  some_module.some_attr
    some_module = load_module_from_file_location(
        "tests/example/settings.py",
        "tests/example/${SANIC_SETTING_B}_settings_${SANIC_SETTING_B}.py",
    )

    assert some_module.SANIC_SETTING_A == "test"
    assert some_module.SANIC_SETTING_B == "test"



# Generated at 2022-06-14 08:14:47.458848
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # A)
    # Set up os_environ.
    PATHS = {
        "/some/path/",
        "/some/path/file_name.py",
        ".",
        "file_name.py",
        "./",
        "/some/path/file_name",
        "file_name",
    }
    os_environ["some_env_var"] = "/some/env/path"
    os_environ["file_name_env_var"] = "file_name_env"


# Generated at 2022-06-14 08:14:58.417431
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    from configparser import ConfigParser
    from tempfile import TemporaryDirectory
    from os import environ, remove, path

    # Assert it can load multiline string.
    custom_str = """
    #multiline

    #comment
    CUSTOM = 'val'
    """
    config = load_module_from_file_location(custom_str)
    assert config.CUSTOM == "val"

    # Assert it can load bytes
    config = load_module_from_file_location(custom_str.encode("utf8"))
    assert config.CUSTOM == "val"

    # Assert it can load a pathlib.Path object
    custom_path = Path(__file__).absolute()
    config = load_module_from_file_location(
        custom_path
    )  #

# Generated at 2022-06-14 08:15:10.625215
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import os
    import tempfile

    # Check string location
    location = __file__
    file_content = dedent(
        """
        #define some_var
    """
    )
    config = load_module_from_file_location(location)
    assert config.some_var is None

    # Check bytes location
    with tempfile.TemporaryDirectory() as tmp_dir:
        file_path = os.path.join(tmp_dir, "config.py")
        with open(file_path, "w") as f:
            f.write(file_content)
        config = load_module_from_file_location(
            file_path.encode(encoding="utf-8")
        )
        assert config.some_var is None

    # Check Path location

# Generated at 2022-06-14 08:15:23.631913
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Unit test for function load_module_from_file_location."""
    # pylint: disable=import-outside-toplevel
    import os
    import random
    import string
    import tempfile
    import uuid

    test_string = "".join(
        random.choices(string.ascii_uppercase, k=10)
    )  # noqa: S311

    # 1 - Raise value error if location contains path
    location = "/some/path"
    try:
        load_module_from_file_location(location)
    except ValueError as e:
        print(f"Unit test 1: {e}")
    else:
        raise Exception

    # 2 - Raise load file exception if variable is not set
    location = "${some_var}"

# Generated at 2022-06-14 08:15:35.049669
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    import sys
    import os
    import re

    sys.path.append("some")

# Generated at 2022-06-14 08:15:45.305963
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from os import environ
    from pathlib import Path
    import tempfile
    from unittest.mock import patch

    with patch.dict("os.environ", {"first_var": "first_value"}):
        with tempfile.TemporaryDirectory() as dir:
            with tempfile.NamedTemporaryFile(dir=dir, suffix=".py") as f:
                f.write(
                    bytes(
                        """
                    from sanic import Sanic
                    import sys

                    app = Sanic("test")
                    __version__ = "testing"
                    __version_info__ = tuple(sys.version_info)
                """,
                        "utf8",
                    )
                )
                f.flush()
                # with no environment var

# Generated at 2022-06-14 08:16:03.437369
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    import tempfile
    from pathlib import Path

    with tempfile.TemporaryDirectory() as tmpdirname:
        test_mod_path = Path(tmpdirname) / "test_mod.py"
        with open(test_mod_path, "w") as test_mod_file:
            test_mod_file.write("test_var = 1")

        os_environ["TEST_ENV_VAR"] = str(test_mod_path.parent)

        test_mod = load_module_from_file_location(
            "test_mod", f"${TEST_ENV_VAR}/test_mod.py"
        )
        assert test_mod.test_var == 1
        assert test_mod.__file__ == str(test_mod_path)

# Generated at 2022-06-14 08:16:16.605253
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Tests load_module_from_file_location function.

    Tests all types of loading configurations provided by second parameter of
    load_module_from_file_location and load_module_from_file_location itself.
    """

    # Test A) loading module from path
    os_environ["SOME_ENV_VAR"] = "config.py"
    module_content = load_module_from_file_location(__file__)
    assert type(module_content) is types.ModuleType
    assert module_content.__file__ == __file__

    # Test B) loading module from pathlib.Path
    path_module_content = load_module_from_file_location(Path(__file__))
    assert type(path_module_content) is types.ModuleType
    assert path_module_content.__file__

# Generated at 2022-06-14 08:16:29.008649
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    import tempfile
    import shutil

    def create_temp_directory():
        return tempfile.mkdtemp()

    def create_temp_file_with_content(temp_dir, filename, content):
        path = Path(temp_dir, filename)
        path.write_text(content)
        return path

    # A) Test Path object
    # 1) Test basic usage
    temp_dir = create_temp_directory()
    config_path = create_temp_file_with_content(
        temp_dir, "config.py", "FOO = 3\nBAR = 4"
    )
    config = load_module_from_file_location(config_path)
    assert config.FOO == 3
    assert config.BAR == 4

    # 2) Test that path with environment variables is correctly resolved

# Generated at 2022-06-14 08:16:38.138993
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import pytest

    # Just for test.

    class AttrDict(dict):
        def __init__(self, *args, **kwargs):
            super(AttrDict, self).__init__(*args, **kwargs)
            self.__dict__ = self

    from tempfile import TemporaryDirectory as temp_dir

    tmp_dir = temp_dir()


# Generated at 2022-06-14 08:16:43.748062
# Unit test for function load_module_from_file_location

# Generated at 2022-06-14 08:16:50.888500
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    """Unit test for function load_module_from_file_location.

    """
    import tempfile
    from os import environ as os_environ
    from os.path import join

    tmp_dir_path = Path(tempfile.mkdtemp())

    # A) Generate some config file.

# Generated at 2022-06-14 08:16:56.752251
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import sys
    import unittest

    def load_config_from_py_path(path: str) -> types.ModuleType:
        return load_module_from_file_location(path)

    class LoadModuleFromFileLocationTestCase(unittest.TestCase):
        def test_cannot_load_from_non_str_or_path(self):
            with self.assertRaises(ValueError):
                load_config_from_py_path(1234)

        def test_loading_from_str_with_py_extension_should_return_module(self):
            module_from_py_extension = load_config_from_py_path("test.py")
            self.assertIsInstance(module_from_py_extension, types.ModuleType)


# Generated at 2022-06-14 08:17:03.186621
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import os
    import subprocess
    import tempfile

    # A) Create temporary module in the directory.
    file_path = os.path.join(tempfile.gettempdir(), "load_module_from_file_location_sample.py")


# Generated at 2022-06-14 08:17:12.013125
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import unittest
    from os import getcwd, remove
    from tempfile import mkstemp

    from sanic.helpers import load_module_from_file_location

    class TestLoadModuleFromFileLocation(unittest.TestCase):
        @classmethod
        def setUpClass(cls):
            # This temporary file will be removed in tearDownClass
            cls.config_file = None

        @classmethod
        def tearDownClass(cls):
            if cls.config_file is not None:
                remove(cls.config_file)

        def setUp(self):
            # Create temporary file that will be removed in tearDown
            _, self.config_file = mkstemp()

        def tearDown(self):
            remove(self.config_file)

        # Unit test for A)
       

# Generated at 2022-06-14 08:17:23.437307
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from pathlib import Path
    import os
    import sys
    import tempfile

    with tempfile.NamedTemporaryFile() as tf:
        test_file_path = Path(tf.name)
        test_file_path.write_text(
            "test_var = 'test_var_value'\n"
            "test_func = lambda input: input + '_test_func_value'\n"
        )
        module = load_module_from_file_location(test_file_path)
        assert module.test_var == 'test_var_value'
        assert module.test_func('some_input') == 'some_input_test_func_value'

        # Test that location can be also provided as a string.

# Generated at 2022-06-14 08:17:48.250507
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from tempfile import mkstemp
    from shutil import copyfileobj

    # Test 1:
    with open("tests/test_app.py", "rb") as f, open(".test_app.py", "wb") as g:
        copyfileobj(f, g)

    test_app = load_module_from_file_location(".test_app.py")
    assert test_app.__name__ == "test_app"

    # Test 2:
    with open("tests/test_app.py", "rb") as f, open(".test_app.py", "wb") as g:
        copyfileobj(f, g)

    test_app = load_module_from_file_location(f".{os.sep}.test_app.py")

# Generated at 2022-06-14 08:17:57.573200
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # A)
    # Set env variable to use it in tests.
    os_environ["SOME_ENV_VAR"] = "some_value"

    # B)
    # Check that ${SOME_ENV_VAR} and ${SOME_ENV_VAR2} will be resolved properly.
    # A ${SOME_ENV_VAR2} should not be resolved.
    location = (
        "${SOME_ENV_VAR}/some_path/${SOME_ENV_VAR2}/some_file.py"
    )

    # C)
    # Place an empty file there.
    with open(os_environ["SOME_ENV_VAR"] + "/some_path/some_file.py", "w"):
        pass

    # D)
    #

# Generated at 2022-06-14 08:18:08.727940
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from tempfile import TemporaryDirectory
    import os

    with TemporaryDirectory() as tmp_dir:
        os.environ["TEST_ENV_VAR"] = tmp_dir

        with open(os.path.join(tmp_dir, "blank_file.py"), "w") as f:
            f.write("")

        some_test_path_with_env_var_in_it = (
            "blablablablablabla/bla/" + "${TEST_ENV_VAR}" + "/blank_file.py"
        )


# Generated at 2022-06-14 08:18:21.823228
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # A) User provides a str type location and we do nothing.
    location = "path.to.file"
    assert (
        load_module_from_file_location(location)
        == import_string("path.to.file")
    )

    # B) User provides a bytes type location, so we decode it into a str type.
    location = b"path.to.file"
    assert (
        load_module_from_file_location(location)
        == import_string("path.to.file")
    )

    # C) User provides a Path type location and we convert it into a str type.
    location = Path("path.to.file")

    assert (
        load_module_from_file_location(location)
        == import_string("path.to.file")
    )

    # D) User