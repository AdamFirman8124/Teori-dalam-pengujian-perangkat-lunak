

# Generated at 2022-06-14 08:08:24.979110
# Unit test for function str_to_bool
def test_str_to_bool():
    assert str_to_bool("y") == True
    assert str_to_bool("Y") == True
    assert str_to_bool("yes") == True
    assert str_to_bool("yep") == True
    assert str_to_bool("yup") == True
    assert str_to_bool("t") == True
    assert str_to_bool("T") == True
    assert str_to_bool("true") == True
    assert str_to_bool("on") == True
    assert str_to_bool("enable") == True
    assert str_to_bool("enabled") == True
    assert str_to_bool("1") == True
    assert str_to_bool("n") == False
    assert str_to_bool("N") == False
    assert str_to_bool("no") == False

# Generated at 2022-06-14 08:08:35.297127
# Unit test for function str_to_bool
def test_str_to_bool():
    test_values = [
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

    for string_value, expected_bool_value in test_values:
        assert str_to_bool(string_value) is expected_bool_value

# Generated at 2022-06-14 08:08:40.590711
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import types

    module_name_02 = "some_module_name"
    some_file_path = "/some/path/${some_env_var}"
    some_env_var = "some_env_var_value"
    os_environ["some_env_var"] = some_env_var

    module_02 = load_module_from_file_location(module_name_02, some_file_path)

    assert isinstance(module_02, types.ModuleType)
    assert module_02.__name__ == module_name_02
    assert module_02.__file__ == some_file_path.replace(
        "${some_env_var}", os_environ["some_env_var"]
    )

# Generated at 2022-06-14 08:08:49.093824
# Unit test for function str_to_bool
def test_str_to_bool():
    assert str_to_bool("t") == True
    assert str_to_bool("True") == True
    assert str_to_bool("yes") == True
    assert str_to_bool("y") == True
    assert str_to_bool("on") == True
    assert str_to_bool("f") == False
    assert str_to_bool("false") == False
    assert str_to_bool("no") == False
    assert str_to_bool("n") == False
    assert str_to_bool("off") == False

# Generated at 2022-06-14 08:08:59.410694
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import_module = load_module_from_file_location
    module_name = __name__
    module = import_module(module_name)

    # Test if function is able to import module by name
    assert module is not None
    assert module.__name__ == module_name

    # Test if function is able to import module by path
    file_path_to_module = import_module.__module__.__file__
    module = import_module(file_path_to_module)

    assert module is not None
    assert module.__name__ == module_name
    assert module.__file__ == file_path_to_module

    # Test if function is able to substitute environment variables
    os_environ["some_env_var"] = "some_value"

# Generated at 2022-06-14 08:09:11.614908
# Unit test for function str_to_bool
def test_str_to_bool():
    from pytest import raises
    assert str_to_bool("y") is True
    assert str_to_bool("yes") is True
    assert str_to_bool("t") is True
    assert str_to_bool("true") is True
    assert str_to_bool("on") is True
    assert str_to_bool("Enable") is True
    assert str_to_bool(" enabled") is True
    assert str_to_bool("1") is True
    assert str_to_bool("n") is False
    assert str_to_bool("NO") is False
    assert str_to_bool("f") is False
    assert str_to_bool("false") is False
    assert str_to_bool("oFF") is False
    assert str_to_bool("disable") is False

# Generated at 2022-06-14 08:09:23.669749
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import os
    import os.path

    import tempfile
    import unittest

    class TestLoadModuleFromFileLocation(unittest.TestCase):

        def test_happy_path(self):
            with tempfile.TemporaryDirectory() as tmp_dir:
                tmp_env = {"KEY": "VAL"}
                tmp_file = os.path.join(tmp_dir, "tmp.py")
                tmp_file_abs_path = os.path.abspath(tmp_file)
                tmp_file_rel_path = os.path.relpath(tmp_file)
                tmp_file_env_path = os.path.join(tmp_dir, f"{tmp_env['KEY']}.py")

                self.assertFalse(os.path.exists(tmp_file_abs_path))
                self.assertFalse

# Generated at 2022-06-14 08:09:33.140460
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    """Unit test for function load_module_from_file_location"""

    # ########################################
    # Test environment variables functionality
    # ########################################

    os_environ["TEST_ENV_VAR"] = "This_is_test_environment_variable"

    # 1.1) Test environment variables in format ${some_env_var}
    #      provided as a string.
    #
    # Note:
    #     When you pass Path("/") as a path parameter
    #     to the spec_from_file_location, you will get ImportError.
    #     Therefore we need to make sure that this will not happen,
    #     otherwise you will not be able to test for it.
    #
    #     This is why we pass "some/path/${TEST_ENV_VAR}" as

# Generated at 2022-06-14 08:09:42.082393
# Unit test for function str_to_bool
def test_str_to_bool():
    assert str_to_bool("yes") == True
    assert str_to_bool("yup") == True
    assert str_to_bool("true") == True
    assert str_to_bool("1") == True
    assert str_to_bool("YeS") == True
    assert str_to_bool("YUP") == True
    assert str_to_bool("tRuE") == True
    assert str_to_bool("1") == True
    assert str_to_bool("no") == False
    assert str_to_bool("False") == False
    assert str_to_bool("f") == False
    assert str_to_bool("0") == False
    assert str_to_bool("N") == False
    assert str_to_bool("FALSE") == False

# Generated at 2022-06-14 08:09:53.188411
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Unit test for function load_module_from_file_location."""

    # 1. Test with argument of a string type, without environment variables.
    assert (
        load_module_from_file_location("./tests/test_config.py")
        is not None
    )

    # 2. Test with argument of a string type, with environment variables.
    os_environ["SOME_ENV_VAR"] = "test_value"
    assert (
        load_module_from_file_location("./${SOME_ENV_VAR}/test_config.py")
        is not None
    )
    del os_environ["SOME_ENV_VAR"]

    # 3. Test with argument of a string type, but with environment variables
    #    provided in wrong format $some_env_var,

# Generated at 2022-06-14 08:10:08.891984
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Tests load_module_from_file_location function.

    Tests are divided into three parts:
    A) Test if function load_module_from_file_location raises
       LoadFileException if somewhere in location passed any
       environment variable in format ${some_env_var},
       where some_env_var is not defined in environment variables.
    B) Test if function load_module_from_file_location loads
       environment variables correctly.
    C) Test if function load_module_from_file_location works
       with various location formats and parameters.
    """

    # A) Test if function load_module_from_file_location raises
    #    LoadFileException if somewhere in location passed any
    #    environment variable in format ${some_env_var},
    #    where some_env_var is not defined in environment variables.

    os_

# Generated at 2022-06-14 08:10:18.658604
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    # A)
    # try to load module from file path
    # provided as environment variable
    os_environ["MY_MODULE_PATH"] = "/tmp/my_module.py"
    my_module = load_module_from_file_location("${MY_MODULE_PATH}")

    with open("/tmp/my_module.py", "w+") as my_module_file:
        my_module_file.write("my_var = True\n")

    # B)
    # check that my_var is True
    assert my_module.my_var is True

    # C)
    # try to load module from file path
    # provided as environment variable
    # and with filename in location

# Generated at 2022-06-14 08:10:25.255250
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    assert Path(__file__).is_file()
    test_object1 = load_module_from_file_location(__file__)
    test_object2 = load_module_from_file_location(__file__, "utf8")
    assert test_object1.__file__ == test_object2.__file__
    assert test_object1.__name__ == test_object2.__name__
    assert test_object1.__package__ == test_object2.__package__



# Generated at 2022-06-14 08:10:34.070963
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    assert str_to_bool("T") == True  # noqa
    assert str_to_bool("fAlSe") == False  # noqa
    assert str_to_bool("yes") == True  # noqa
    assert str_to_bool("n") == False  # noqa
    assert str_to_bool("1") == True  # noqa
    assert str_to_bool("0") == False  # noqa
    assert str_to_bool("wtf")


# Generated at 2022-06-14 08:10:43.176719
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from .temp_directory import get_temp_directory, delete_temp_directory

    config_template = \
        """
# encoding: utf-8

{}
    """

    import os

    with get_temp_directory(".") as temp_path:
        config_path = temp_path / "config.py"

        # A) Some object
        some_object = {"some_key": "some_value"}

        # B) Write it to config file
        with open(config_path, "w") as f:
            f.write(config_template.format(repr(some_object)))

        # C) Load it back.
        module = load_module_from_file_location(config_path)
        assert module.__dict__ == some_object

        # D) Load it from environment variable.
        os.en

# Generated at 2022-06-14 08:10:55.278279
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Test load_module_from_file_location function."""
    os_environ["TEST_ENV_VAR"] = "TEST_ENV_VAR"
    os_environ["TEST_ENV_VAR_WITH_SPECIAL_CHARS"] = r"$#*@_&%^"
    os_environ["TEST_ENV_VAR_WITH_PATH_TO_CONFIG_FILE"] = os.path.dirname(
        os.path.realpath(__file__)
    )

    conf_file_path = os.path.join(
        os.environ["TEST_ENV_VAR_WITH_PATH_TO_CONFIG_FILE"],
        "config_file_for_testing_env_vars.py",
    )

    # A)

# Generated at 2022-06-14 08:11:06.975371
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import pytest

    with pytest.raises(LoadFileException):
        assert load_module_from_file_location(
            "some_module_name", "/some/path/${"
            + "some_env_var"  # var that is missing in environment,
            + "}"
        )

    assert load_module_from_file_location(
        "some_module_name",
        "/some/path/${HOME}",
        os_environ["HOME"],
    ) == load_module_from_file_location(
        "some_module_name", "/some/path/%s" % os_environ["HOME"]
    )

    with pytest.raises(IOError):
        assert load_module_from_file_location("some_module_name", "/invalid_path")


# Generated at 2022-06-14 08:11:19.051459
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    env = dict(os_environ)
    os_environ.clear()
    os_environ.update(
        {
            "TEST_CASE_1": "path/to/some/file.py",
            "TEST_CASE_2": "path/to/some/file",
            "TEST_CASE_3": "path/to/some/file.yaml",
            "TEST_CASE_4": "ModuleWithDots.module",
        }
    )
    assert (
        load_module_from_file_location(
            "path/to/some/file.py",
            "/some/other${TEST_CASE_1}",
            "r",
            False,
            True,
        ).__name__
        == "file"
    )

# Generated at 2022-06-14 08:11:31.725317
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    from tempfile import NamedTemporaryFile
    from os import environ as os_environ
    from os import remove as os_remove
    from os import path as os_path

    content = "content"
    test_env_var = "test_env_var"


# Generated at 2022-06-14 08:11:44.511587
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Tests for function load_module_from_file_location
    """
    os_environ["SOME_TEST_ENV_VAR"] = "test_env_var"
    test_file_path = "./test_config.py"
    test_mod = load_module_from_file_location(test_file_path)
    assert test_mod.TEST_VARIABLE == "test_variable"
    test_mod = load_module_from_file_location(Path(test_file_path))
    assert test_mod.TEST_VARIABLE == "test_variable"
    test_mod = load_module_from_file_location("$SOME_TEST_ENV_VAR/test_config")

# Generated at 2022-06-14 08:12:01.279556
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Unit test for load_module_from_file_location function."""

    # Create temporary directory to put test files in.
    import tempfile
    import shutil
    temp_dir_path = tempfile.mkdtemp()

    # Create files.
    # File name is a key in test_cases dict.
    # File content is a value in test_cases dict.
    test_cases = {
        "file.py": "test_var = 2",
        "file.txt": "test_var = 2",
        "file_with_env_var.py": "test_var = ${TEST_ENV_VAR}",
        "file_with_wrong_env_var.py": "test_var = ${TEST_ENV_VAR_WRONG}",
    }

# Generated at 2022-06-14 08:12:14.493850
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    test_env = {"TEST_ENV_VAR_0": "TEST_ENV_VAR_0", "TEST_ENV_VAR_1": 1}
    os_environ.update(test_env)
    import_location_1 = "tests.utils.test_configs.test_config_1"
    import_location_2 = "tests/utils/test_configs/test_config_2.py"
    import_location_3 = "tests/utils/test_configs/test_config_3"
    import_location_4 = "${TEST_ENV_VAR_1}"
    import_location_5 = "./tests/utils/test_configs/test_config_4.py"

# Generated at 2022-06-14 08:12:22.887311
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    some_module = load_module_from_file_location(
        "some_module_name", "/some/path/${some_env_var}"
    )
    assert some_module.coroutine == True

    some_module2 = load_module_from_file_location(
        "some_module_name", "/some/path/${some_env_var}"
    )
    assert some_module == some_module2

    some_module3 = load_module_from_file_location(
        "some_module_name", "/some/path/\"${some_env_var}\""
    )
    assert some_module3.coroutine == True

    some_module4 = load_module_from_file_location(
        "some_module_name", "/some/path/${some_env_var}"
    )

# Generated at 2022-06-14 08:12:35.549687
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # Create temporary file.
    import tempfile
    from uuid import uuid4

    temp_dir = tempfile.mkdtemp()
    temp_file = tempfile.NamedTemporaryFile(
        mode="w+", dir=temp_dir, encoding="utf-8"
    )
    temp_file.write("a = 1\nb = 2")
    temp_file.flush()  # Save data to the file.

    # Run function under test.
    module = load_module_from_file_location(temp_file.name)

    # Check it's propertly loaded.
    assert module.a == 1
    assert module.b == 2

    # Check environment variables are expanded.
    os_environ["ENV_VAR_A"] = str(uuid4())

# Generated at 2022-06-14 08:12:46.968288
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    os_environ["some_env_var"] = "/some/path"

    # 1. We will test if function
    # load_module_from_file_location("test_module.py")
    # raises exception if test_module.py file does not exist.
    with pytest.raises(IOError):
        load_module_from_file_location("test_module.py")

    # 2. We will test load_module_from_file_location(Path).

    # 2.1 With Path instance.
    test_module = load_module_from_file_location(
        Path("test_module.py")
    )  # test_module.py file exists
    # Check if module is loaded properly.
    assert test_module.SOME_CONSTANT == "some_value"

    # 2.2 With path string

# Generated at 2022-06-14 08:12:55.510854
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    location = "${TEST_ENV_VAR}/some/path/some_file.py"

    # Case 1: Raises LoadFileException
    with pytest.raises(LoadFileException):
        load_module_from_file_location(location)

    # Case 2: Raises LoadFileException
    os_environ["TEST_ENV_VAR"] = "/fake/path"
    try:
        with pytest.raises(LoadFileException):
            load_module_from_file_location(location)
    finally:
        del os_environ["TEST_ENV_VAR"]

    # Case 3: Returns proper module
    os_environ["TEST_ENV_VAR"] = os.path.dirname(os.path.realpath(__file__))

# Generated at 2022-06-14 08:13:06.613140
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import tempfile

    test_tuple = (
        (
            "load_module_from_file_location('/wrong/path') with path"
            " to wrong location",
            "/wrong/path",
            "Unable to load configuration file",
        ),
        (
            "load_module_from_file_location('/wrong/path') with"
            " without path",
            "/wrong/path.py",
            "Unable to load configuration file",
        ),
        (
            "load_module_from_file_location('missing_module') with"
            " a module that doesn't exists",
            "missing_module",
            "No module named 'missing_module'",
        ),
    )


# Generated at 2022-06-14 08:13:17.800528
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Tests load_module_from_file_location function"""
    # Check if imports corretly when
    # location pointing to file on disk
    module = load_module_from_file_location(
        Path(__file__).parent / "test_data" / "config.py"
    )
    assert module.TEST_CONFIG_VARIABLE == "TEST_CONFIG_VALUE"
    # Check if raises error when
    # location pointing to missing file on disk
    with pytest.raises(IOError):
        load_module_from_file_location(
            Path(__file__).parent / "test_data" / "missing_file.py"
        )
    # Check if raises error when
    # location parameter is not of string or bytes type

# Generated at 2022-06-14 08:13:30.013164
# Unit test for function load_module_from_file_location

# Generated at 2022-06-14 08:13:40.103243
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    import tempfile

    temp_dir = tempfile.TemporaryDirectory()
    temp_dir.cleanup()
    env_var_name, env_var_value = "ENV_VAR_NAME", "ENV_VAR_VALUE"
    env_var_file_name = "env_var_file_name"

    # A) Without file location
    with pytest.raises(
        ValueError,
        match=(
            r"Could not detect a filename in '"
            r"<class 'bytes'>"
            r"' string. Please, use absolute path to the file."
        ),
    ):
        load_module_from_file_location(b"")

    # B) Without variables

    # B1) With existing module
    existing_module_name = "sanic.exceptions"
    module

# Generated at 2022-06-14 08:13:56.793087
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa: D202
    # Successful import module by file path
    res = load_module_from_file_location(
        "tests/test-utils/dummy_config.py"
    )
    assert res.__file__ == "tests/test-utils/dummy_config.py"

    # Successful import module by file path
    res = load_module_from_file_location(
        "tests/test-utils/dummy_config.py"
    )
    assert res.__file__ == "tests/test-utils/dummy_config.py"

    # Successful import module by Path
    res = load_module_from_file_location(
        Path("tests/test-utils/dummy_config.py")
    )

# Generated at 2022-06-14 08:14:10.123506
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Test load_module_from_file_location function from sanic.helpers."""

    import tempfile
    import shutil
    import random

    from pathlib import Path

    # 1) Create temporary directory that will contain module.
    temp_dir_path = Path(tempfile.mkdtemp())
    shutil.rmtree(temp_dir_path)  # remove temporary directory

    # 2) Create temporary file that will contain module.
    rand_num = random.randint(0, 10 ** 10)
    rand_name = "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=5))
    temp_mod_name = rand_name + ".py"
    temp_mod_path = Path(temp_dir_path / temp_mod_name)
    temp_mod_

# Generated at 2022-06-14 08:14:10.813154
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    pass



# Generated at 2022-06-14 08:14:21.734354
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    import sys

    # Basic load_module_from_file_location tests
    sys.modules["my_config"] = None
    assert isinstance(
        load_module_from_file_location(__file__), types.ModuleType
    )
    sys.modules["my_config"] = None
    test_config = Path(__file__).parent
    assert isinstance(
        load_module_from_file_location(__file__, str(test_config)),
        types.ModuleType,
    )

    # Test that function load_module_from_file_location
    # can read environment variables
    os_environ["AS_IS_TEST_ENV_VAR"] = "env_var"
    test_config = Path(__file__).parent.parent / "env_var_config"

# Generated at 2022-06-14 08:14:28.192541
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # Get the file name
    path = Path(__file__).parent / 'test_data/test_config.py'

    # Get the environment variable
    os_environ["TEST_ENV_VAR"] = str(path)

    # Try to load
    module = load_module_from_file_location(path)

    # Check if it has loaded
    assert module
    module.config_file_loaded

# Generated at 2022-06-14 08:14:38.176960
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # A) Test if returned object is a module
    if isinstance(load_module_from_file_location("config.py"), types.ModuleType):
        print("1")
    else:
        print("0")

    # B) Test if returned object is a module and check if it has a configs
    #    as a properties
    if (
        "configs" in load_module_from_file_location("config.py").__dict__
    ):  # noqa
        print("1")
    else:
        print("0")

    # C) Test if LoadFileException is raised when env var is not present in env
    try:
        load_module_from_file_location("/some/path/${SOME_ENV_VAR}")
    except LoadFileException:
        print("1")

# Generated at 2022-06-14 08:14:51.180761
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import sys

    sys.modules.pop("config", None)
    os_environ["APP_SETTINGS"] = "config.DevelopmentConfig"
    os_environ["FLASK_ENV"] = "development"
    os_environ["SANIC_ENV"] = "development"

    module = load_module_from_file_location("config.DevelopmentConfig")

    assert module.__name__ == "config"
    assert module.FLASK_ENV == "development"
    assert module.SANIC_ENV == "development"
    assert module.APP_SETTINGS == "config.DevelopmentConfig"

    module = load_module_from_file_location(b"config.DevelopmentConfig")

    assert module.__name__ == "config"
    assert module.FLASK_ENV == "development"
    assert module

# Generated at 2022-06-14 08:15:03.227262
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    os_environ["test_load_module_from_file_location"] = "test_load_module_from_file_location"
    assert (
        load_module_from_file_location(
            "test_load_module_from_file_location"
        ).__dict__
        == {}
    )
    os_environ["test_load_module_from_file_location"] = ""
    assert (
        load_module_from_file_location(
            "test_load_module_from_file_location"
        ).__dict__
        == {}
    )
    assert (
        load_module_from_file_location(
            "config.test_load_module_from_file_location"
        ).__dict__
        != {}
    )

# Generated at 2022-06-14 08:15:10.141217
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Unit tests for exposing load_module_from_file_location on external api"""

    test_module_path = "/tmp/sanic_test_module.py"
    with open(test_module_path, "w") as test_module_file:
        test_module_file.write('TEST = True')

    test_module = load_module_from_file_location(test_module_path)
    assert test_module.TEST == True


# Generated at 2022-06-14 08:15:21.408682
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # Test module path with environment variables.
    os_environ["TEST_ENV_VAR"] = "/root/my_project_folder"
    conf = load_module_from_file_location(
        "/root/${TEST_ENV_VAR}/config.py"
    )
    assert conf.__file__ == "/root/my_project_folder/config.py"

    # Test module path without environment variables.
    conf = load_module_from_file_location(
        "/root/my_project_folder/config.py"
    )
    assert conf.__file__ == "/root/my_project_folder/config.py"

    # Test module path with bytes.

# Generated at 2022-06-14 08:15:40.667074
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    # If you want to assert that method doesn't raise an exception then
    # you can use the context manager assert_no_exception
    with assert_no_exception():
        # A) Let's try to load a module by a path.
        module = load_module_from_file_location(
            location="/some/path/some_path.py"
        )

        assert module is not None
        assert module.__file__.endswith("some_path.py")

        # B) Now let's try to load a module by a path with environment
        #    variables in it.
        some_env_var = "some_env_var"
        os_environ[some_env_var] = "some_env_var_value"

# Generated at 2022-06-14 08:15:48.638486
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    # Setup env variables
    KEY = "SOME_KEY"
    VALUE = "some value"
    os_environ[KEY] = VALUE

    TEMP_FILE_NAME = "__temp_file_name__"
    TEMP_CONTENTS = """
    def some_func():
        return "some_val"
    """

    # A) Ensure that function works.
    print("Testing function load_module_from_file_location...")
    with open(TEMP_FILE_NAME, "w") as f:
        f.write(TEMP_CONTENTS)

    loaded_module = load_module_from_file_location(TEMP_FILE_NAME)
    assert loaded_module.some_func() == "some_val"

    # B) Ensure that function works with pathlib.

# Generated at 2022-06-14 08:16:01.700798
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # "{toxworkdir}/directory"
    # should be same as
    # "{toxworkdir}/directory/__init__.py"
    assert load_module_from_file_location(
        f"{os_environ['toxworkdir']}/directory"
    ).__name__ == "directory"

    # "{toxworkdir}/directory/__init__.py"
    assert load_module_from_file_location(
        f"{os_environ['toxworkdir']}/directory/__init__.py"
    ).__name__ == "directory"

    # "{toxworkdir}/directory/__init__.py"

# Generated at 2022-06-14 08:16:15.328034
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    from os import environ
    from random import randint
    import tempfile

    # Case 1:
    # Check if function can resolve environment variables.
    # to do this we will create temporary file
    # and put in him some random int.
    # Then we will save their path in environment variable
    # and check that function can load this file.
    config_path = Path(tempfile.mkdtemp()).resolve()

    config_file_name = "somefile.py"
    config_file_path = config_path / config_file_name

    config_file_name_without_extension = config_file_name.split(".")[0]


# Generated at 2022-06-14 08:16:19.974405
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """
    >>> assert load_module_from_file_location(
    ...    "some_module_name",
    ...    Path(__file__).parent / "res" / "test_load_module_from_path.py"
    ... ).test_result == 42
    """

    pass

# Generated at 2022-06-14 08:16:30.948939
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    import random
    import string

    # Prepare location string
    location = "/${" + "".join(  # noqa
        random.choices(
            string.ascii_uppercase + string.digits, k=10
        )
    ) + "}"
    assert "${" in location
    assert "}" in location

    # Set environment variable for location
    os_environ[location[2:-1]] = location[:-1] + "1"

    # Load module from file_location
    module = load_module_from_file_location(location)
    assert module.__file__ == location[:-1] + "1"

# Generated at 2022-06-14 08:16:41.786067
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Unit test for function load_module_from_file_location."""
    from pathlib import Path
    from tempfile import TemporaryDirectory
    from textwrap import dedent

    with TemporaryDirectory() as tmp_dir:
        # This test is using magic of python's pathlib, which automatically
        # creates any directories and files in path, even when the path is
        # absolute.
        tmp_dir = Path(tmp_dir)

        # Creating a test file.
        test_filename = tmp_dir / "test" / "test.py"

        with test_filename.open("w") as test_file:
            test_file.write(
                dedent(
                    """
                    TEST_CONSTANT_1 = "test"
                    TEST_CONSTANT_2 = 42
                    """
                )
            )

        test_mod = load

# Generated at 2022-06-14 08:16:50.628592
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from functools import partial

    from sanic.exceptions import LoadFileException

    from .test_config import test_module_location
    from .test_config import test_module_name

    # Test file does not exists.
    with pytest.raises(IOError):
        load_module_from_file_location("some_not_existing_file_on_my_disk")

    # Test basic functionality.
    some_module = load_module_from_file_location(test_module_name)

    assert some_module.__name__ == test_module_name
    assert some_module.__file__ == test_module_location

    some_module = load_module_from_file_location(test_module_location)

    assert some_module.__name__ == test_module_name
    assert some_module.__

# Generated at 2022-06-14 08:17:02.572742
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # pragma: no cover
    """Unit test to try to load modules with different paths:
    - Direct module name
    - Module with path
    - Module with path with environment variable
    - Module with bytes path
    - Module with bytes path with environment variable
    - Module with pathlib Path object
    """
    env_var = os_environ.get("ENV_VAR")
    if env_var is None:
        os_environ["ENV_VAR"] = "ENV_VAR_VALUE"


# Generated at 2022-06-14 08:17:07.626910
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import tempfile
    import os.path

    # Testing case when location is not kind of string/bytes/path
    try:
        load_module_from_file_location(1)
    except TypeError as e:
        assert "expected str, bytes" in str(e)

    # Testing case when location is of the bytes type
    tmp_file = "var_1=1\nvar_2='2'"
    tmp_file_path = os.path.join(
        tempfile.gettempdir(), "test_load_module_from_file_location.py"
    )
    with open(tmp_file_path, "wb") as f:
        f.write(tmp_file.encode("utf8"))

# Generated at 2022-06-14 08:17:28.362240
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import sys
    import pytest
    from os import environ, path
    from os.path import dirname

    some_script_dirpath = path.dirname(path.abspath(__file__))
    project_dirpath = path.dirname(some_script_dirpath)

    if f"{project_dirpath}/examples" not in sys.path:
        sys.path.append(f"{project_dirpath}/examples")


# Generated at 2022-06-14 08:17:40.037991
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    import os
    from os.path import exists
    from tempfile import TemporaryDirectory, NamedTemporaryFile
    from shutil import copyfile

    from pytest import raises

    # Create temporary directory and file.
    temp_dir = TemporaryDirectory()
    temp_file_name = NamedTemporaryFile("w", dir=temp_dir.name).name
    temp_file_path = Path(temp_file_name)

    # Create temporary configuration file in temp directory.
    config_var = "test_var"
    config_val = "test_val"
    copyfile(
        _file_path.parent / "test_resources" / "test_config_module.py", temp_file_path
    )

# Generated at 2022-06-14 08:17:52.200763
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from unittest.mock import patch, mock_open, ANY
    from io import StringIO

    test_location = "some_location"
    test_args = ("some_args",)
    test_kwargs = {"some_key": "some_value"}
    test_encoding = "some_encoding"

    with patch(
        "sanic.helpers.import_string", return_value="some_string"
    ) as import_string, patch(
        "sanic.helpers.module_from_spec"
    ) as module_from_spec, patch(
        "sanic.helpers.spec_from_file_location"
    ) as spec_from_file_location:

        module_from_spec.return_value = "some_module"

# Generated at 2022-06-14 08:18:06.089699
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    def get_test_config(test_config_name):
        current_path = Path(__file__).parent
        test_config_path = Path(current_path, test_config_name)
        test_config_path = str(test_config_path)
        return load_module_from_file_location(test_config_path)

    # testing config file without imports
    config = get_test_config("test_config_file")
    assert config.VAR_1 == "value_1"
    assert config.VAR_2 == "value_2"
    assert config.VAR_3["key_1"] == "value_1"
    assert config.VAR_3["key_2"] == "value_2"

# Generated at 2022-06-14 08:18:16.445915
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Unit test for function load_module_from_file_location."""

    from os import environ

    from pathlib import Path

    environ["SOME_ENV_VAR"] = "test2"

    some_module_name = "test_module"
    path_to_module = Path(__file__).parent.joinpath(some_module_name + ".py")

    def clean_module_from_sys_modules(module_name):
        if module_name in sys.modules:
            del sys.modules[module_name]

    clean_module_from_sys_modules(some_module_name)
    clean_module_from_sys_modules(path_to_module.absolute())

    def compare_modules(loaded_module):
        assert loaded_module.OK == True
        assert loaded_module.NOT_OK