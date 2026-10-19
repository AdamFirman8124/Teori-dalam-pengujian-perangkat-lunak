

# Generated at 2022-06-14 08:08:27.211669
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    if not os_environ.get("CI"):
        location = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), "fixtures", "app_name.py"
        )
        assert load_module_from_file_location(location).app_name == "Sanic"
        app_name = load_module_from_file_location(location).app_name

        assert app_name == "Sanic"

    location = Path(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), "fixtures")
    )
    assert load_module_from_file_location(location).app_name == "Sanic"
    app_name = load_module_from_file_location(location).app_name

# Generated at 2022-06-14 08:08:39.391466
# Unit test for function str_to_bool
def test_str_to_bool():
    # test case 1
    msg = "test case 1 failed"
    assert str_to_bool("Yes") is True, msg

    # test case 2
    msg = "test case 2 failed"
    assert str_to_bool("no") is False, msg

    # test case 3
    msg = "test case 3 failed"
    assert str_to_bool("1") is True, msg

    # test case 4
    msg = "test case 4 failed"
    assert str_to_bool("0") is False, msg

    # test case 5
    msg = "test case 5 failed"
    assert str_to_bool("true") is True, msg

    # test case 6
    msg = "test case 6 failed"
    assert str_to_bool("false") is False, msg

# Generated at 2022-06-14 08:08:46.684968
# Unit test for function str_to_bool
def test_str_to_bool():
    """Checks example values for str_to_bool."""
    for val in {
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
        assert str_to_bool(val)

    for val in {"n", "no", "f", "false", "off", "disable", "disabled", "0"}:
        assert not str_to_bool(val)

    try:
        str_to_bool("somestring")
    except ValueError:
        pass
    else:
        raise Exception("Should raise ValueError for 'somestring'")

# Generated at 2022-06-14 08:08:58.508916
# Unit test for function str_to_bool
def test_str_to_bool():
    assert str_to_bool("y") == True
    assert str_to_bool("yes") == True
    assert str_to_bool("yep") == True
    assert str_to_bool("yup") == True
    assert str_to_bool("t") == True
    assert str_to_bool("true") == True
    assert str_to_bool("on") == True
    assert str_to_bool("enable") == True
    assert str_to_bool("enabled") == True
    assert str_to_bool("1") == True
    assert str_to_bool("n") == False
    assert str_to_bool("no") == False
    assert str_to_bool("f") == False
    assert str_to_bool("false") == False
    assert str_to_bool("off") == False

# Generated at 2022-06-14 08:09:10.705241
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    def raise_load_file_exception(
        location,
        enconding,
        *args,
        **kwargs
    ):
        with pytest.raises(LoadFileException):
            load_module_from_file_location(
                location,
                enconding,
                *args,
                **kwargs
            )

    #  1. Test if error is raised with wrong file path
    raise_load_file_exception("/some/wrong/file/path", "utf8")

    #  2. Test if error is raised with wrong module name
    raise_load_file_exception("some_wrong_module_name", "utf8")

    #  3. Test if error is raised with wrong module name, which contains
    #     invalid characters for Python module names

# Generated at 2022-06-14 08:09:23.061475
# Unit test for function str_to_bool
def test_str_to_bool():
    assert str_to_bool("n") is False
    assert str_to_bool("0") is False
    assert str_to_bool("no") is False
    assert str_to_bool("f") is False
    assert str_to_bool("false") is False
    assert str_to_bool("off") is False
    assert str_to_bool("disable") is False
    assert str_to_bool("disabled") is False

    assert str_to_bool("y") is True
    assert str_to_bool("1") is True
    assert str_to_bool("yes") is True
    assert str_to_bool("yep") is True
    assert str_to_bool("yup") is True
    assert str_to_bool("t") is True
    assert str_to_bool("true") is True

# Generated at 2022-06-14 08:09:32.658272
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import sys
    import types

    from unittest import TestCase

    class TestLoadModuleFromFileLocation(TestCase):
        def test_without_args(self):
            # Test A) Environment variables substitution in loading path.
            os_environ["env_var1"] = "env_var_value1"
            os_environ["env_var2"] = "env_var_value2"
            os_environ["env_var3"] = "env_var_value3"
            path = "${env_var1}/some_name.py"
            module = load_module_from_file_location(path)
            self.assertEqual(module.__name__, "some_name")
            self.assertEqual(module.__file__, path)

# Generated at 2022-06-14 08:09:42.041617
# Unit test for function str_to_bool
def test_str_to_bool():
    # Check that it raises ValueError on wrong input
    wrong_values = [
        "",
        "1",
        "yes but no",
        "true but false",
        "on and off",
        "maybe",
        "True but False",
        "0 but 1",
        "Y but N",
        "T and F",
        "T, F",
        "y, n",
        "1, 0",
        "Yes, No",
    ]
    for val in wrong_values:
        assert_raises(ValueError, str_to_bool, val)

    # Check that it converts
    # all possible combinations of words to True and False

# Generated at 2022-06-14 08:09:47.577606
# Unit test for function str_to_bool
def test_str_to_bool():
    assert str_to_bool("y")
    assert str_to_bool("yes")
    assert str_to_bool("Y")
    assert str_to_bool("YES")
    assert not str_to_bool("n")
    assert not str_to_bool("false")
    assert not str_to_bool("FALSE")

# Generated at 2022-06-14 08:09:59.772800
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    assert load_module_from_file_location(
        "sanic.helpers"
    ) == import_string("sanic.helpers")

    assert load_module_from_file_location(
        "sanic.helpers", "sanic/"
    ) == import_string("sanic.helpers")

    assert load_module_from_file_location(
        "sanic.helpers", "sanic", "helpers"
    ) == import_string("sanic.helpers")

    assert load_module_from_file_location(
        b"sanic.helpers", b"sanic\helpers.py"
    ) == import_string("sanic.helpers")


# Generated at 2022-06-14 08:10:10.487780
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import sys
    import os
    import re

    # Create test module.
    test_module_file_name = "test_module.py"
    with open(test_module_file_name, "w") as test_module_file:
        test_module_file.write('test_module_var = "test_module_var_value"')
    if not sys.path:
        sys.path.append("")
    # Get path to test module.
    test_module_path = sys.path[0]
    if not test_module_path:
        test_module_path = "."
    test_module = load_module_from_file_location(
        os.path.join(test_module_path, test_module_file_name)
    )

# Generated at 2022-06-14 08:10:22.717402
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    os_environ["SANIC_TEST_ENV_VAR1"] = "some_value1"
    os_environ["SANIC_TEST_ENV_VAR2"] = "some_value2"
    os_environ["SANIC_TEST_ENV_VAR3"] = ""

    # A
    assert load_module_from_file_location("${SANIC_TEST_ENV_VAR1}") is None
    assert load_module_from_file_location("${SANIC_TEST_ENV_VAR2}") is None
    assert load_module_from_file_location("${SANIC_TEST_ENV_VAR3}") is None

# Generated at 2022-06-14 08:10:30.312146
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Function load_module_from_file_location should pass all these tests"""
    from sanic.config import Config
    from os import path
    from tempfile import TemporaryDirectory
    from contextlib import contextmanager

    # Create temporary directory
    @contextmanager
    def temp_path():
        with TemporaryDirectory() as temp_dir:
            yield Path(temp_dir)

    # Tests
    # A) Test that this function can read json config
    with temp_path() as temp_dir:
        # create json config
        json_config_path = path.join(temp_dir, "config.json")

# Generated at 2022-06-14 08:10:43.234152
# Unit test for function load_module_from_file_location

# Generated at 2022-06-14 08:10:55.325506
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    import tempfile

    def simple_conf(file_name):
        with open(file_name, "w") as f:
            f.write("VAR = 12")

    # Test loading module from file location.
    with tempfile.NamedTemporaryFile() as temp_file:
        file_name = temp_file.name
        simple_conf(file_name)
        module = load_module_from_file_location(file_name)
        assert module.VAR == 12

    # Test loading module when location contains environment variables.
    with tempfile.NamedTemporaryFile() as temp_file:
        file_name = temp_file.name

        # A) Simulate environment variables.
        SOME_ENV_VAR = file_name
        os_environ["SOME_ENV_VAR"] = SOME_EN

# Generated at 2022-06-14 08:11:06.975716
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # Test when location is in a string format.
    # pylint: disable=fixme
    # FIXME: try to remove this setup step
    #        and do it in the test itself.
    location = "tests/test_config.py"
    if not os.path.exists(location):
        location = "app/tests/test_config.py"

    test_module = load_module_from_file_location(location)
    assert hasattr(test_module, "TEST_VARIABLE")
    assert test_module.TEST_VARIABLE == 1
    assert hasattr(test_module, "VARIABLE_DICT")
    assert hasattr(test_module.VARIABLE_DICT, "foo")

# Generated at 2022-06-14 08:11:18.222785
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    location = "tests.configs.test_config"
    module = load_module_from_file_location(location)
    assert module.option == "value"
    assert module.list_option == ["val1", "val2"]

    os_environ["SOME_ENV_VAR"] = "unittest"
    location = "/some/path/${SOME_ENV_VAR}/tests/configs/test_config.py"
    module = load_module_from_file_location(location)
    assert module.option == "value"
    assert module.list_option == ["val1", "val2"]
    del os_environ["SOME_ENV_VAR"]

# Generated at 2022-06-14 08:11:31.279225
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """
    Test will check if load_module_from_file_location works correctly
    in different situations.
    """
    # test normal import
    load_module_from_file_location("os.path")

    # test import from path
    load_module_from_file_location("test/test_helpers.py")

    # test import from path with environment variable
    os_environ["SOME_ENV_VAR"] = "test"
    load_module_from_file_location("${SOME_ENV_VAR}/test_helpers.py")
    del os_environ["SOME_ENV_VAR"]

    # test import from path with wrong file
    with pytest.raises(IOError):
        load_module_from_file_location("test/some_wrong_file.py")

# Generated at 2022-06-14 08:11:44.131615
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from importlib import reload
    from contextlib import contextmanager
    from unittest.mock import patch

    @contextmanager
    def mock_import_string(string: str, module):
        with patch.object(  # type: ignore
            module_to_patch, "import_string", return_value=module
        ):
            yield

    some_module_name = "some_module_name"
    some_module_location = "/home/${HOME}/some_module_name.py"
    some_env_var_value = "mock_home_value"

    module_to_patch = __import__(
        "sanic.helpers.strings", fromlist=["import_string"]
    )
    some_module = object()


# Generated at 2022-06-14 08:11:51.718383
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    os_environ["cool_env_var"] = "cool_env_var_value"

    res = load_module_from_file_location(
        location="tests/fixtures/config/project.config",
        name="project.config",
        package=None
    )
    assert hasattr(res, "DATABASE_URI")
    assert res.DATABASE_URI == "sqlite:///:memory:"

    res = load_module_from_file_location(
        location="tests/fixtures/config/${cool_env_var}/project.config",
        name="project.config",
        package=None
    )
    assert hasattr(res, "DATABASE_URI")
    assert res.DATABASE_URI == "sqlite:///:memory:"

    del os_environ

# Generated at 2022-06-14 08:12:03.733766
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    """Unit tests for function load_module_from_file_location"""
    import sys

    sys_path_before = set(sys.path)

    config_values = {
        "TEST_BOOL": True,
        "TEST_STRING": "some_string_value",
        "TEST_INT": 123,
    }

    # Create temporary file with TEST_BOOL = True.
    # We will treat this file like a config file.
    with open("test_config.py", "w") as config_file:
        for key, val in config_values.items():
            config_file.write(f"{key} = {val}\n")

    test_module = load_module_from_file_location("test_config.py")


# Generated at 2022-06-14 08:12:17.400051
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import os
    import tempfile
    import pathlib

    # Test file
    config_path = pathlib.Path(tempfile.gettempdir()) / 'tmp.py'
    config_path.touch()
    config_path.write_text(
        '''
        class Cl(): pass
        ''')

    # Test env var
    os.environ["TEST_ENV_VAR"] = config_path.parent.as_posix()

    mod = load_module_from_file_location(config_path)
    assert hasattr(mod, 'Cl') == True

    mod = load_module_from_file_location(config_path.as_posix())
    assert hasattr(mod, 'Cl') == True


# Generated at 2022-06-14 08:12:23.947321
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    import jinja2
    from tempfile import TemporaryDirectory

    # All tests are done in temporary folder.
    with TemporaryDirectory() as tmpdir:

        # There is no test.py file in folder.
        with pytest.raises(PyFileError):
            load_module_from_file_location(
                "test", str(Path(tmpdir).resolve())
            )

        # Create simple config file test.py with content:
        #
        #     test_value = 10
        #
        # and set some environment variable.
        test_path = Path(tmpdir) / "test.py"
        with open(test_path, "w") as f:
            f.write("test_value = 10")

        os_environ["TEST_VAL"] = "test.py"

        # Check if we can load this

# Generated at 2022-06-14 08:12:31.403585
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    assert load_module_from_file_location("__main__")
    assert load_module_from_file_location("sanic.app")
    assert load_module_from_file_location("__future__")
    assert load_module_from_file_location("sys")
    assert load_module_from_file_location("set")
    assert load_module_from_file_location("os")



# Generated at 2022-06-14 08:12:39.788627
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import tempfile
    import shutil
    import sys

    config = """
    A_VALUE = "%s"
    B_VALUE = "%s"
    """

    tmp_path = Path(tempfile.mkdtemp())
    tmp_path.joinpath("config.py").write_text(config.replace("%s", "True"))
    tmp_path.joinpath("config.ini").write_text(config.replace("%s", "False"))

    expected_result = type(
        "Config", (), {"A_VALUE": True, "B_VALUE": False}
    )()

    assert (
        load_module_from_file_location(
            tmp_path.joinpath("config.py")
        )
        == expected_result
    )


# Generated at 2022-06-14 08:12:51.420622
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    test_module_name = "in_memory_module"
    test_module_content = """
        some_string = "some_value"
        some_int = 1
        some_list = [
            "some",
            "values"
        ]
    """
    test_module = types.ModuleType(test_module_name)
    exec(compile(test_module_content, "in_memory_content", "exec"), test_module.__dict__)

    assert isinstance(
        load_module_from_file_location(test_module), types.ModuleType
    )

    assert (
        load_module_from_file_location(test_module).some_string
        == "some_value"
    )

# Generated at 2022-06-14 08:12:53.854184
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    assert (
        load_module_from_file_location("sanic.config").Config
        == sanic.config.Config
    )



# Generated at 2022-06-14 08:13:05.959524
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    sys.modules.pop("test_module_load", None)
    test_module = types.ModuleType("test_module_load")
    test_module.__file__ = "test_module_load.py"
    sys.modules["test_module_load"] = test_module

    # A) Test with module object
    assert (
        load_module_from_file_location("test_module_load")
        is test_module
    )

    # B) Test with path
    sys.modules.pop("test_module_load", None)

    test_module_path = Path("./example/config.py")
    test_module = load_module_from_file_location(test_module_path)
    assert test_module.SOME_ENVIRONMENT == "test"

    # Test with env var in path

# Generated at 2022-06-14 08:13:17.133475
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # Test import from file path
    os_environ["some_env_var"] = "some_dir"
    path = "tests/data/module_from_file/some_module"
    module = load_module_from_file_location(path, "utf8")
    assert module.some_attr == "some_val"

    # Test import from environment variable in file path
    path = "tests/data/${some_env_var}/some_module"
    module = load_module_from_file_location(path, "utf8")
    assert module.some_attr == "some_val"

    # Test import from Path object
    path = Path("tests/data/module_from_file/some_module")
    module = load_module_from_file_location(path, "utf8")
    assert module.some

# Generated at 2022-06-14 08:13:29.081395
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """
    We test this function in two steps:
        1) With location provided as string.
        2) With location provided as Path object.
    """

    # Step 1:
    # --------------------------------------------------------
    # 1.1) Test location with relative and absolute paths.
    location = "test_file.py"
    module = load_module_from_file_location(location)
    assert module

    location = Path(__file__).parent / "test_file.py"
    assert isinstance(location, Path)
    module = load_module_from_file_location(location)
    assert module

    # 1.2) Test location with environment variables.
    location = "test_file.py"
    os_environ["SANIC_TESTING_ENV_VARIABLE"] = "test_file.py"
    module

# Generated at 2022-06-14 08:13:40.410290
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    from sanic.utils import is_binary_file
    import os

    test_dict = {
        "int": 1,
        "float": 1.0,
        "bool": True,
        "string": "string",
        "list": [1],
        "dict": {"a": "b"},
        "tuple": (1, 2),
        "list_of_list": [[1, 2], [3, 4]],
    }

    for key, value in test_dict.items():
        # A. Create test file
        tmp_dir = os.path.dirname(os.path.abspath(__file__))
        tmp_file = os.path.join(tmp_dir, "temp.py")
        with open(tmp_file, "w+") as f:
            f.write

# Generated at 2022-06-14 08:13:53.710785
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from sanic.config import TEST_SCRIPT, TEST_SCRIPT_BAD
    from sanic.exceptions import LoadFileException

    # Test location as a pathlib.Path object
    module = load_module_from_file_location(Path(TEST_SCRIPT))
    assert module.TEST_VARIABLE == "t"

    # Test location as a string
    module = load_module_from_file_location(TEST_SCRIPT)
    assert module.TEST_VARIABLE == "t"

    # Test location as a bytes object
    module = load_module_from_file_location(b"test_script")
    assert module.TEST_VARIABLE == "t"

    # Test location as a bytes object

# Generated at 2022-06-14 08:14:05.013399
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from .test_module1 import test_module1
    from .test_module2 import test_module2
    from .test_module3 import test_module3

    os_environ["test_env_var"] = "test_env_var_value"

    assert load_module_from_file_location(
        "test_module1", __file__.replace("__init__.py", "test_module1.py")
    ) == test_module1

    assert load_module_from_file_location(
        "test_module2", __file__.replace("__init__.py", "test_module2.py")
    ) == test_module2


# Generated at 2022-06-14 08:14:12.154154
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # Notice $variable below is not resolved as environment variable.
    # It is a "part of the file path"
    some_module = load_module_from_file_location(
        "some_module_name", "/some/path/$variable"
    )
    assert some_module.__name__ == "some_module_name"
    assert some_module.__file__ == "/some/path/$variable"



# Generated at 2022-06-14 08:14:25.124988
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # test normal work with file_location
    try:
        module = load_module_from_file_location(
            "tests/some_config.py"
        )
        assert module.TEST == "test_sting"
        assert module.TEST_INT == 10
    except:
        assert False

    # test normal work with Path
    try:
        from pathlib import Path
        module = load_module_from_file_location(
            Path(__file__).parent.absolute() / "some_config.py"
        )
        assert module.TEST == "test_sting"
        assert module.TEST_INT == 10
    except:
        assert False

    # Test with environment variables.
    # Test with environment variables.
    import os

# Generated at 2022-06-14 08:14:35.067970
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import pytest
    import tempfile

    # Test that invalid location is handled properly.
    with pytest.raises(IOError):
        load_module_from_file_location("")

    # Test that invalid location is handled properly.
    with pytest.raises(IOError):
        load_module_from_file_location("", "/${invalid_env_var}")

    # Test that invalid location is handled properly.
    with pytest.raises(IOError):
        load_module_from_file_location("", "invalid_module_name")

    # Test that valid path will be loaded as module.
    valid_module_name = "valid_module_name"
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)

# Generated at 2022-06-14 08:14:46.604265
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    importpath = "import_module.test_module"
    module = load_module_from_file_location(importpath)
    assert module.test_getme == "I am here"

    filepath = "tests/test_module.py"
    module = load_module_from_file_location(filepath)
    assert module.test_getme == "I am here"

    filepath = Path(__file__).parent / "test_module.py"
    module = load_module_from_file_location(filepath)
    assert module.test_getme == "I am here"

    filepath = Path(__file__).parent / "test_module.py"
    module = load_module_from_file_location(filepath)
    assert module.test_getme == "I am here"

    filepath

# Generated at 2022-06-14 08:14:57.670189
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    """Unit test for function load_module_from_file_location."""

    from os import chdir, environ

    from pathlib import Path

    from tempfile import TemporaryDirectory

    # 1. Test with providing python file that is a module.

    # 1.1. Test with correct python file.
    with TemporaryDirectory() as temp_dir:

        # 1.1.1. Create module file.
        module_file_path = Path(temp_dir, "test_module_file.py")
        with open(module_file_path, "w") as module_file:
            module_file.write("a = 5")

        # 1.1.2. Change directory to  temp_dir and load module.
        chdir(temp_dir)

# Generated at 2022-06-14 08:15:09.938011
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    os_environ["TEST_VAR"] = "TEST_VAR"
    assert load_module_from_file_location(
        "tests/test_helpers/config.py"
    ).TEST_VAR == "TEST_VAL"
    assert load_module_from_file_location(
        "tests/test_helpers/config.py"
    ).load_module_from_file_location.__name__ == "load_module_from_file_location"
    assert load_module_from_file_location(
        "tests/test_helpers/config.py"
    ).str_to_bool.__name__ == "str_to_bool"

# Generated at 2022-06-14 08:15:17.058943
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    import os
    import pathlib
    import tempfile
    import pytest
    import sanic.exceptions

    # if no / in location then import_string will be used
    sanic.helpers.load_module_from_file_location("pathlib.Path") == pathlib.Path
    sanic.helpers.load_module_from_file_location("os.environ") == os.environ

    # if / in location then:
    #   1) If location does not exist raise IOError
    with pytest.raises(IOError):
        sanic.helpers.load_module_from_file_location("/tmp/does_not_exist.py")

    #   2) if location exists and is a file and has .py extension
    #      in location then load a module from it.
    _

# Generated at 2022-06-14 08:15:28.155694
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    """Tests load_module_from_file_location function"""

    # Case 0) Import module from string
    import logging
    import_string("logging")
    assert logging.__name__ == "logging"

    # Case 1) Import a module from existing string path.
    module = load_module_from_file_location(
        "tests/app_examples/app_error_handler/app.py"
    )
    assert module.app.name == "app.app"

    # Case 2) Import a module from existing bytes path.
    module = load_module_from_file_location(
        b"tests/app_examples/app_error_handler/app.py"
    )
    assert module.app.name == "app.app"

    # Case 3) Import a module from existing pathlib

# Generated at 2022-06-14 08:15:41.230545
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    module = load_module_from_file_location(
        "sanic.config.test_module.test_load_module_from_file_location_mod",
        __file__,
        package=__package__,
    )
    assert module.PATH == __file__
    assert module.TEST_ENV_VAR == "TEST_VALUE"

    with os.environ.copy() as env:
        del env["TEST_ENV_VAR"]
        with pytest.raises(LoadFileException, match="The following environment variables are not set: TEST_ENV_VAR"):
            load_module_from_file_location("sanic.config.test_module.test_load_module_from_file_location_mod", __file__, package=__package__)

    assert load_module_from_

# Generated at 2022-06-14 08:15:53.815525
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location(): # noqa

    import pytest
    from pathlib import Path

    from sanic.exceptions import LoadFileException
    from sanic.utils import load_module_from_file_location as load_file

    from .conftest import (
        TESTS_PATH,
        VALID_CONFIG_PATH,
        INVALID_CONFIG_PATH,
        TESTS_PATH_STR,
        VALID_CONFIG_PATH_STR,
    )

    # Try to use load_module_from_file_location with location parameter
    # as bytes
    def test_with_location_param_as_bytes():
        with pytest.raises(IOError):
            load_file(b"some_name", b"${some_env_var}/some_path")

# Generated at 2022-06-14 08:16:05.540215
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from .test_utils import get_test_config, get_test_config_factory

    from ..app import Sanic

    import types

    import os

    # 1. Get path to test config.
    config_path = get_test_config()

    # 2. Check if it's loaded properly.

    assert isinstance(load_module_from_file_location(config_path), types.ModuleType)

    # 3. Set environment variable.
    os.environ["ENV_VAR"] = config_path

    # 4. Check if config was loaded properly with environment variable.
    assert isinstance(
        load_module_from_file_location("/some/path/${ENV_VAR}"), types.ModuleType
    )

    # 5. Check if "ENV_VAR_NOT_SET" is not a valid environment

# Generated at 2022-06-14 08:16:14.855115
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Unit test for function load_module_from_file_location"""
    # Requires that you have a file located at
    #  tests/files/dev_config/dev_config.py
    # with content "TEST = True".
    module = load_module_from_file_location(
        "tests/files/dev_config/dev_config.py"
    )
    assert module.TEST
    assert module.__file__.endswith(
        "/tests/files/dev_config/dev_config.py"
    )

# Generated at 2022-06-14 08:16:26.631677
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    """Tests load_module_from_file_location function."""
    from os import environ as os_environ
    from pathlib import Path
    from types import ModuleType
    from tempfile import mkdtemp

    tmppath = Path(mkdtemp())
    tmppath.joinpath("tmpfile").write_text(
        "a=1\nb=2\n"
    )  # Creates temporary file with some config

    os_environ["test_env_var"] = str(tmppath)  # Adding env var to the environment

    # Now let's try some importings.

    # Loading from file path - should raise error.

# Generated at 2022-06-14 08:16:37.040672
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # pylint: disable=redefined-outer-name

    from tempfile import mkdtemp
    from shutil import rmtree
    from pathlib import Path

    from sanic.config import Config
    from sanic.helpers import load_module_from_file_location

    # Variables
    cfg = Config()

    # Functions

    def create_config(name, content="", temp_dir=None):
        """Creates temporary file and returns its path."""
        if temp_dir is None:
            temp_dir = cfg.TEMPLATE_CONFIG_DIR
        path = Path(temp_dir) / f"{name}.py"
        with path.open("w") as file:
            file.write(content)
        return path

    # Tests

# Generated at 2022-06-14 08:16:49.169113
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Unit test for function load_module_from_file_location."""

    # A) Check working with bytes for different encodings.
    assert (
        load_module_from_file_location(b"utf_8", location=b"bytes").location
        == "bytes"
    )
    assert (
        load_module_from_file_location(b"utf_16_le", location=b"bytes").location
        == "bytes"
    )
    assert (
        load_module_from_file_location(b"utf_16_be", location=b"bytes").location
        == "bytes"
    )
    assert (
        load_module_from_file_location(b"utf_32_le", location=b"bytes").location
        == "bytes"
    )

# Generated at 2022-06-14 08:17:01.530496
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    tests = {
        'nested_attr': "tests.fixtures.conf_test.nested_attr",
        '_nested_attr': "_nested_attr",
        'simple_attr': "tests.fixtures.conf_test.simple_attr",
        'test_attr': "tests.fixtures.conf_test.test_attr",
        'not_existing_attr': "tests.fixtures.conf_test.not_existing_attr",
    }
    configuration_module = load_module_from_file_location("tests/fixtures/conf_test.py")

    assert tests['nested_attr'] == configuration_module.nested_attr.value
    assert tests['_nested_attr'] == configuration_module._nested_attr
    assert tests['simple_attr'] == configuration_module.simple_attr
   

# Generated at 2022-06-14 08:17:11.557025
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    from pathlib import Path
    from os import environ
    from tempfile import NamedTemporaryFile, TemporaryDirectory

    # Prepare test files that can be imported.
    with NamedTemporaryFile(mode="w") as f:
        f.write(
            '''
            import types

            class SomeClass():

                def some_method():
                    pass
            '''
        )
        f.flush()
        some_module = load_module_from_file_location(f.name)

    with TemporaryDirectory() as tempdir_name:
        some_module = load_module_from_file_location(Path(tempdir_name))

    # Check if it imports modules correctly.
    assert hasattr(some_module, "SomeClass")

    # Check if it imports classes correctly.
    assert some_module.SomeClass().__

# Generated at 2022-06-14 08:17:26.712746
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # On string location.
    assert load_module_from_file_location(
        'import sys\nprint("test")\nx = "y"'
    ).x == "y"

    # On bytes location.
    assert load_module_from_file_location(
        b'import sys\nprint("test")\nx = "y"'
    ).x == "y"

    # On Path location.
    assert load_module_from_file_location(
        Path(__file__).parent / "../tests/config.py"
    ).DB_USER == "app_user"

    # On Path location containing environment variable.
    os_environ["some_env_var"] = "some_value"

# Generated at 2022-06-14 08:17:38.895464
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import os
    import pytest
    import tempfile
    from pathlib import Path
    from sanic.config import load_module_from_file_location

    # Set some environment variables
    os.environ["test_env_var_1"] = "test_env_var_1_value"
    os.environ["test_env_var_2"] = "test_env_var_2_value"

    # Create temporary module file
    with tempfile.TemporaryDirectory() as temp_dir:
        some_temp_module_file = Path(temp_dir) / "some_temp_module.py"

# Generated at 2022-06-14 08:17:51.619273
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    from pathlib import Path

    from sanic.config import (
        load_module_from_file_location,
        LoadFileException,
    )

    from sanic.exceptions import PyFileError

    # some tests for location that is not a Path instance
    for location in [
        "some_module_name",
        "some_module_name.py",
        "/some/path/to/some_module_name.py",
    ]:
        if "." not in location:
            # test with extension
            load_module_from_file_location(location + ".py")
        else:
            # test without extension
            load_module_from_file_location(location)

    # some tests for location that is a Path instance and with extension

# Generated at 2022-06-14 08:18:05.527374
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # pragma: no cover
    """Unit test for method load_module_from_file_location."""
    from tempfile import NamedTemporaryFile
    import os.path as os_path
    import sys
    import time

    # Test if it can load regular file
    with NamedTemporaryFile() as file:
        module_name = "some_module{}".format(time.time())
        module_location = file.name
        module_definition = "some_var = 1"
        file.write(module_definition.encode())
        file.flush()
        module = load_module_from_file_location(module_name, module_location)
        assert getattr(module, "some_var") == 1

    # Test if it can load file with absolute path.
    with NamedTemporaryFile() as file:
        module_name

# Generated at 2022-06-14 08:18:16.057303
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # This function is tested on Linux system with bash.

    # If You run this unit test, the "./temp" will be created in Your
    # directory You run this unit test.

    assert os_environ.get("UNIT_TEST") is not None

    module_you_want_to_import = "sanic.config"
    path_without_env_vars = "./temp/test_env.py"
    path_with_env_vars = f"./temp/test_env${UNIT_TEST}.py"
    path_with_env_vars_without_leading_dot = (
        f"/temp/test_env${UNIT_TEST}.py"
    )