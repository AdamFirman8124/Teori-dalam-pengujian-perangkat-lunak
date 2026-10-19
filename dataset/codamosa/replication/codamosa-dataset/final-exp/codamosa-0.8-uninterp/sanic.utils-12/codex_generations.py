

# Generated at 2022-06-14 08:08:24.080634
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location(): # pragma: no cover
    some_file = Path(__file__).parent / "some_file.py"
    with some_file.open("w") as f:
        f.write('a = "some_val"')

    # A) Check if path to module is in string format
    assert load_module_from_file_location(
        str(some_file)).a == "some_val"

    # B) Check if path to module is in bytes format
    assert load_module_from_file_location(
        str(some_file).encode()).a == "some_val"

    # C) Check if path to module is in Path format
    assert load_module_from_file_location(some_file).a == "some_val"

    # D) Check if path contains environment variable.

# Generated at 2022-06-14 08:08:29.250937
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from sanic.config import Config  # noqa
    from pathlib import Path

    ConfigPath = Path("../tests/config.py")
    Config = load_module_from_file_location(ConfigPath)
    assert Config.TEST_KEY == "test_value"

    Config = load_module_from_file_location("sanic.config")

    assert issubclass(Config, object)
    assert ConfigPath.resolve().as_posix() == Config.__file__

# Generated at 2022-06-14 08:08:36.931109
# Unit test for function str_to_bool
def test_str_to_bool():
    for string_true in (
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
    ):
        assert str_to_bool(string_true)
    for string_false in (
        "n",
        "no",
        "f",
        "false",
        "off",
        "disable",
        "disabled",
        "0",
    ):
        assert not str_to_bool(string_false)
    with pytest.raises(ValueError):
        str_to_bool("maybe")

# Generated at 2022-06-14 08:08:49.514233
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    import unittest
    import tempfile

    class TestLoadModuleFromFileLocationMethods(unittest.TestCase):
        def test_load_module_from_file_location_test1(self):
            with tempfile.NamedTemporaryFile() as f:
                f.write(b'TEST1 = True\n')
                f.flush()
                module = load_module_from_file_location(f.name)
                self.assertEqual(module.TEST1, True)

        def test_load_module_from_file_location_test2(self):
            with tempfile.NamedTemporaryFile() as f:
                f.write(b'TEST2 = True\n')
                f.flush()
                module = load_module_from_file_location(f.name)


# Generated at 2022-06-14 08:08:58.276300
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Unit test for function load_module_from_file_location."""
    from os import environ as os_environ
    from os import path

    os_environ["test_sanic_helpers"] = "test_sanic_helpers"
    module = load_module_from_file_location(
        "test_sanic_helpers",
        path.join(path.dirname(__file__), "config_for_test.py"),
    )

    assert module.some_var == "some_value"
    assert module.CONFIG_FILE_ENV == "test_sanic_helpers"

# Generated at 2022-06-14 08:09:10.462949
# Unit test for function str_to_bool
def test_str_to_bool():
    assert str_to_bool("t") == True
    assert str_to_bool("true") == True
    assert str_to_bool("True") == True
    assert str_to_bool("y") == True
    assert str_to_bool("yes") == True
    assert str_to_bool("Yes") == True
    assert str_to_bool("ON") == True
    assert str_to_bool("oN") == True
    assert str_to_bool("1") == True
    assert str_to_bool("Y") == True

    assert str_to_bool("f") == False
    assert str_to_bool("false") == False
    assert str_to_bool("False") == False
    assert str_to_bool("n") == False
    assert str_to_bool("No") == False
    assert str

# Generated at 2022-06-14 08:09:21.669212
# Unit test for function str_to_bool
def test_str_to_bool():
    assert (
        str_to_bool("y")
        == str_to_bool("yes")
        == str_to_bool("yup")
        == str_to_bool("on")
        == str_to_bool("True")
        == str_to_bool("1")
        == True
    )

    assert (
        str_to_bool("n")
        == str_to_bool("no")
        == str_to_bool("nop")
        == str_to_bool("off")
        == str_to_bool("False")
        == str_to_bool("0")
        == False
    )

    assert str_to_bool("atata") == ValueError

# Generated at 2022-06-14 08:09:26.089119
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # TODO: add more testing, especially for cases when file doesn't exist
    # TODO: or when location parameter is of a bytes type
    test_file_path = Path(__file__).resolve().parent / "test.py"
    test_module = load_module_from_file_location(test_file_path)
    assert test_module.test_variable == "TEST"

# Generated at 2022-06-14 08:09:34.624223
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

# Generated at 2022-06-14 08:09:42.732444
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # Test loading file with short path
    module = load_module_from_file_location("tests/app.py")
    assert module.app.config == {"TESTING": True, "SERVER_NAME": None}

    # Test loading file with full path
    module = load_module_from_file_location(Path(__file__).parent / "app.py")
    assert module.app.config == {"TESTING": True, "SERVER_NAME": None}

    # Test loading file with environment variables in path
    os_environ["test_test_test"] = "test"
    module = load_module_from_file_location(
        "tests/${test_test_test}/app.py"
    )
    assert module.app.config == {"TESTING": True, "SERVER_NAME": None}

# Generated at 2022-06-14 08:09:57.851900
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    assert hasattr(load_module_from_file_location("./"), "__file__")

    os_environ["test_load_module_from_file_location"] = "test"
    assert hasattr(load_module_from_file_location("./${test_load_module_from_file_location}"), "__file__")

    os_environ["test_load_module_from_file_location2"] = "test2"
    assert hasattr(load_module_from_file_location("./${test_load_module_from_file_location}/${test_load_module_from_file_location2}"), "__file__")

    assert hasattr(load_module_from_file_location("./tests/test_utils.py"), "__file__")

# Generated at 2022-06-14 08:10:04.320783
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import sys
    import os

    def module_path(module):
        """
        Generates path to module in format
        <module_dir>/<module_name>.py.
        """
        return f"{os.path.dirname(module.__file__)}/{module.__name__}.py"

    demo_module = sys.modules["demo"]
    module_path_with_env_var = module_path(
        demo_module
    )  # ${DEMO_ENV_VAR} was not expanded, so will be found in result
    assert (
        load_module_from_file_location(module_path(demo_module))
        is demo_module
    )  # module can be loaded from its path in sys.modules

# Generated at 2022-06-14 08:10:16.828147
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # pylint: disable=import-outside-toplevel
    from unittest.mock import patch

    def _assert_env_vars_in_location(env_var: str, location: str):
        with patch.dict("os.environ", {env_var: "ThisIsVarName"}):
            module = load_module_from_file_location(
                location=location, loader="loader"
            )
            assert module == "ThisIsVarName"

    _assert_env_vars_in_location("some_env_var", "/some/path/${some_env_var}")
    _assert_env_vars_in_location("some_env_var", "/some/path/${some_env_var}/")

# Generated at 2022-06-14 08:10:27.132673
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Unit test for function load_module_from_file_location.

    Test loads test_module_file.py and test_module_file_2.py file into local
    memory space, checks if they were loaded as a modules, after that checks
    if they have attributes that were defined in files and if they have
    attributes as a Path instances.
    """

    # A) Get path to directory where this test file is located.
    test_dir = Path(__file__).resolve().parent

    # B) Get relative path to test_module_file.py and test_module_file_2.py files.
    test_file = Path("test_module_file.py")
    test_file_2 = Path("test_module_file_2.py")

    # C) Load test_file and test_file_2 modules.
    test

# Generated at 2022-06-14 08:10:40.261166
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import inspect
    import os
    import random
    import string

    random_module_name = "".join(
        random.choice(string.ascii_letters + string.digits)
        for _ in range(10)
    )
    random_child_module_name = "".join(
        random.choice(string.ascii_letters + string.digits)
        for _ in range(10)
    )
    os.environ["SOME_ENV_VAR"] = random_child_module_name


# Generated at 2022-06-14 08:10:51.804600
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import os

    os.environ["ENV_VARIABLE"] = "env_variable"
    os.environ["ENV_VARIABLE2"] = "env_variable2"

    # Case 1: Load module from file location
    module_config = load_module_from_file_location(
        "some_module_name",
        Path(__file__).parent / "data" / "module_config.py",
    )

    assert module_config.VARIABLE == "value"
    assert module_config.VARIABLE2 == "value2"

    # Case 2: Load module from env variable

# Generated at 2022-06-14 08:11:02.729458
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # Setup
    os_environ["ENV_VAR_VALUE"] = "env_var_value"
    file_path = Path(__file__).parent.joinpath("config_files/config_01.py")
    location_with_env_var = str(file_path).replace(
        "__init__", "${ENV_VAR_VALUE}"
    )

    locations_to_test = [
        file_path,
        location_with_env_var,
        str(file_path),
        location_with_env_var.encode(),
    ]

    # Execute
    results = [
        load_module_from_file_location(location) for location in locations_to_test
    ]
    expected_result = type("Config", (), {"CONFIG_VALUE": "config_01"})()

# Generated at 2022-06-14 08:11:04.266776
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    assert load_module_from_file_location(__file__)

# Generated at 2022-06-14 08:11:04.988325
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    pass

# Generated at 2022-06-14 08:11:13.903789
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    def test_load_simple_file():
        simple_config = load_module_from_file_location(
            "tests/test_configs/simple_config.py"
        )
        assert simple_config.some_var == "some_value"

    def test_load_file_with_env_vars():
        os_environ["some_valid_env_var"] = "some_value"
        try:
            simple_config = load_module_from_file_location(
                "/tests/test_configs/${some_valid_env_var}_config.py"
            )
            assert simple_config.some_var == "some_value"
        finally:
            os_environ.pop("some_valid_env_var")


# Generated at 2022-06-14 08:11:27.960830
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # type: ignore
    assert load_module_from_file_location(
        "sys"
    ).version_info == sys.version_info  # type: ignore
    assert load_module_from_file_location(__file__).__file__ == __file__
    assert load_module_from_file_location(
        Path(__file__)
    ).__file__ == __file__  # type: ignore

    with pytest.raises(LoadFileException):
        load_module_from_file_location(
            "/some/path/${some_env_var_that_doesnt_exist}"
        )



# Generated at 2022-06-14 08:11:35.275323
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Unit test for function load_module_from_file_location."""
    from pathlib import Path
    from os import pathsep, environ, getenv, setenv
    from tempfile import gettempdir
    import sys

    from pytest import raises

    from sanic.config import load_module_from_file_location

    # check if function was initialized correctly
    # if not raises AttributeError
    if sys.implementation.name != "cpython":
        assert hasattr(load_module_from_file_location, "__wrapped__")
    assert (
        sys.gettrace() is None
        if hasattr(load_module_from_file_location, "__wrapped__")
        else True
    )


    # various wrong inputs
    with raises(TypeError):
        load_module_from_file_

# Generated at 2022-06-14 08:11:46.451559
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import tempfile

    fd, path = tempfile.mkstemp(suffix=".py", prefix="config_")
    with open(path, "w") as f:
        f.write(
            """
CONFIG_VAR = 100
            """
        )

    module = load_module_from_file_location(path)
    assert CONFIG_VAR == 100

    # Try with non-existing file
    try:
        load_module_from_file_location("/non-existing-file")
    except LoadFileException:
        assert True
    else:
        assert False, "Raise exception when file is missing"

    # Try with existing file without .py extension
    load_module_from_file_location(path, mode="r")
    assert CONFIG_VAR == 100

    # Try with environment variables in path


# Generated at 2022-06-14 08:12:00.218641
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Test function load_module_from_file_location
    """
    try:
        import tempfile
    except:
        # In case that tempfile doesn't exist in the system,
        # skip the test.
        return

    with tempfile.TemporaryDirectory(suffix="sanic_test") as tempdir:
        # Testing loading module from absolute path.
        tmp_path = Path(tempdir, "config.py")
        with open(tmp_path, "w") as f:
            f.write("foo=1")
        tmp_mod = load_module_from_file_location(tmp_path)
        assert tmp_mod.foo == 1

        # Testing loading module from relative path.
        tmp_path = Path(tempdir, "config2.py")

# Generated at 2022-06-14 08:12:09.825927
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import random
    import string
    import sys
    import os

    # Generate random non-existent file name
    os.system(
        "touch "
        + "".join(
            random.choice(string.ascii_uppercase + string.digits)
            for _ in range(8)
        )
        + ".py"
    )

    def load_non_existent_file_exception():
        load_module_from_file_location(
            "".join(
                random.choice(string.ascii_uppercase + string.digits)
                for _ in range(8)
            )
            + ".py"
        )


# Generated at 2022-06-14 08:12:16.079037
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # Set environment variable that will be used in following tests
    os_environ["SOME_ENV_VAR"] = "some_env_value"

    # Cases where function should raise LoadFileException
    assert_raises(
        LoadFileException,
        load_module_from_file_location,
        "some/${SOME_MISSING_ENV_VAR}/path/module.py",
    )

    # Cases where function should raise PyFileError
    assert_raises(
        PyFileError,
        load_module_from_file_location,
        "/some/path/file.py",
        "some_module_name",
    )

    # Cases where function should raise IOError
    assert_raises(IOError, load_module_from_file_location, "some_module_name")

   

# Generated at 2022-06-14 08:12:23.491197
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    os_environ["TEST_ENV_VAR"] = "test"
    with tempfile.NamedTemporaryFile(mode="w", suffix=".py") as tf:
        t = f"""

var1 = 1
var2 = "test"
"""
        tf.write(t)
        tf.flush()
        module1 = load_module_from_file_location(tf.name)
        module2 = load_module_from_file_location(
            Path(tf.name), encoding="utf8"
        )
        module3 = load_module_from_file_location(
            Path(tf.name).as_uri(), encoding="utf8"
        )

# Generated at 2022-06-14 08:12:33.380327
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    os_environ["SOME_ENV_VAR"] = "/some/path"
    module = load_module_from_file_location(
        "tests/config_test_file.py", "/some/path/${SOME_ENV_VAR}"
    )
    assert module.TEST_PARAMETER == 1

    module = load_module_from_file_location(
        "tests/config_test_file.py", "/some/path/${SOME_ENV_VAR}/"
    )
    assert module.TEST_PARAMETER == 1

# Generated at 2022-06-14 08:12:45.194830
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    # Create temporary config file.
    tmp_config_file = Path(__file__).parent / "tmp_config_file.py"
    tmp_config_file.touch()
    with tmp_config_file.open(mode="w") as f:
        f.write(
            """
import os
PROJECT_DIR = os.path.dirname(__file__)
"""
        )

    # Set environment variables.
    os.environ["TEST_ENV_VAR1"] = "my_file.txt"
    os.environ["TEST_ENV_VAR2"] = str(tmp_config_file)


# Generated at 2022-06-14 08:12:54.824428
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import shutil
    from tempfile import mkdtemp
    from random import choice, randint

    from .test_helpers import TEST_DIR

    # A) Create a config file in temp dir.
    tmpdir = mkdtemp()

    # Create a random file name.
    file_name = "".join(
        [choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-.") for i in range(randint(6, 20))]  # noqa
    ) + ".py"

    tmpfile_path = Path(tmpdir) / file_name
    with open(tmpfile_path, "w") as tmpfile:
        tmpfile.write("FOO=42")

    # B) Check if module was properly loaded.
    module = load_module

# Generated at 2022-06-14 08:13:04.767007
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    # if location parameter is a string path to some file
    # and this file is python script which defines some variable called
    # SOME_VARIABLES, then the module returned by function
    # load_module_from_file_location should expose this variable
    # in its own namespace

    # We have test_file.py next to this test_load_module_from_file_location file
    # This file defines SOME_VARIABLES = some_value

    location = Path(__file__).parent / "test_file.py"

    mod = load_module_from_file_location(location)
    assert mod.__file__ == str(location)
    assert mod.__name__ == "test_file"
    assert mod.SOME_VARIABLES == "some_value"

    # If location is instead of path to

# Generated at 2022-06-14 08:13:16.496761
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    os_environ["SANIC_TEST_ENV_VAR"] = "env_var"
    os_environ["SANIC_TEST_ENV_VAR_NOT_SET_UP"] = "env_var_not_set_up"

    # Test if it can load module from .py file
    module_from_py_file = load_module_from_file_location(
        "some_module_name",
        "${SANIC_TEST_ENV_VAR}/path/to/module.py",
    )
    assert hasattr(module_from_py_file, "__name__")
    assert hasattr(module_from_py_file, "__file__")
    assert module_from_py_file.__name__ == "some_module_name"
    assert module_from_py

# Generated at 2022-06-14 08:13:23.922066
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa: F601
    os_environ["var1"] = "val1"
    try:
        os_environ["var2"] = "val2"
        load_module_from_file_location(
            "/some/path/${var1}/${var2}/location/${var3}.py"  # noqa: F821
        )
    except LoadFileException as e:
        assert re.search(
            r"The following environment variables are not set:\s+var3", str(e)
        )  # noqa: F821
    else:
        assert False

# Generated at 2022-06-14 08:13:36.722983
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """
    Unit test for module load_module_from_file_location
    """
    tester_file_1 = Path("test_load_module_from_file_location_file_1")
    tester_file_2 = Path("test_load_module_from_file_location_file_2")
    tester_file_3 = Path("test_load_module_from_file_location_file_3")
    tester_file_4 = Path("test_load_module_from_file_location_file_4")

    assert not tester_file_1.is_file()
    assert not tester_file_2.is_file()
    assert not tester_file_3.is_file()
    assert not tester_file_4.is_file()

    tester_file_1.write_

# Generated at 2022-06-14 08:13:47.427001
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from pathlib import Path
    from random import randint
    from unittest.mock import patch
    import tempfile

    # 1. Test for ValueError on trying to resolve not set environment variable.
    with tempfile.TemporaryDirectory() as dirpath:

        # A) Create fake environment variable.
        fake_env_var = "FAKE_ENV_VAR_%s" % randint(1, 1000)
        assert fake_env_var not in os.environ, (
            "This test assumes that there is no such environment variable "
            "as %s in environment. But it is defined. "
            "Please update test in test_load_module_from_file_location() "
            "function in utils.py file." % fake_env_var
        )

        # B) Create file with fake environment variable.
       

# Generated at 2022-06-14 08:13:50.810387
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    location = "${PWD}/docker/docker-compose.yml"
    module = load_module_from_file_location(location)
    assert module.__file__ == location

# Generated at 2022-06-14 08:14:03.918461
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    import sys
    import types
    import pytest

    sys.path.insert(0, "tests/sample_configs")

    # We need to reload config file from sample_configs
    # to reset module.
    # In other case, they will always have
    # module.__file__ attribute.
    del sys.modules["tests.sample_configs.config_1"]
    del sys.modules["tests.sample_configs.config_2"]

    # A) Check that load_module_from_file_location returns
    #    module loaded provided path.
    # B) Check that it rewrites module.__file__ attribute.

# Generated at 2022-06-14 08:14:17.110433
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    # Setup environment variables.
    os_environ["TEST_ENV_VAR"] = "test_env_var"

    # Create config file to load.
    config_file_path = Path("fake_config.py")
    config_file_path.write_text("a = 1\nb = 2")

    # A) Test whether it loads regular module.

    loaded_module = load_module_from_file_location("time")

    assert loaded_module.__name__ == "time"

    # B) Test whether it loads config file.

    loaded_module = load_module_from_file_location(config_file_path)

    assert loaded_module.__name__ == "fake_config"
    assert loaded_module.a == 1
    assert loaded_module.b == 2

    # Empty config file.

    config

# Generated at 2022-06-14 08:14:25.229835
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import unittest

    class TestLoadModuleFromFileLocationFun(unittest.TestCase):
        def test_load_python_file(self):
            import os

            from sanic_toolkit.utils import load_module_from_file_location

            os.environ["SANIC_TOOLKIT_TEST_ENV_1"] = "env_var_1_val"
            os.environ["SANIC_TOOLKIT_TEST_ENV_2"] = "env_var_2_val"
            os.environ["SANIC_TOOLKIT_TEST_ENV_3"] = "env_var_3_val"
            os.environ["SANIC_TOOLKIT_TEST_ENV_4"] = "env_var_4_val"

# Generated at 2022-06-14 08:14:35.122394
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    # Case 1:
    # The location parameter is of a string type and
    # we look for a file without .py extension.
    module = load_module_from_file_location(
        location="sanic/examples/config_example.json",
        encoding="utf8",
        is_package=False,
    )
    assert module == types.ModuleType("config")
    assert module.__file__ == "sanic/examples/config_example.json"
    assert module.config_example_json_param == "config_example_json_param"

    # Case 3:
    # The location parameter is of a string type and
    # we look for a file with .py extension.

# Generated at 2022-06-14 08:14:45.180431
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import tempfile

    name = "test_file.py"
    with tempfile.TemporaryDirectory() as tmp_dir:
        file = tmp_dir + "/" + name
        with open(file, "w") as file:
            file.write("test_var = 4")
        module = load_module_from_file_location(file)
        assert module.test_var == 4

# Generated at 2022-06-14 08:14:52.624814
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from os import environ

    environ["some_env_var"] = "some_value"
    some_module = load_module_from_file_location(
        "some_module_name",
        "/some/path/${some_env_var}",
        True,  # package
        False,  # is_namespace
    )
    assert some_module.__name__ == "some_module_name"
    assert some_module.__file__ == "/some/path/some_value"
    assert getattr(some_module, "__package__", None)


# Generated at 2022-06-14 08:14:59.538463
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    os_environ["TEST_ENV"] = "test"
    location = load_module_from_file_location("tests.unit.test_config")
    assert location.test_value == 42
    location = load_module_from_file_location(
        "/test/test_config", "/some/path/${TEST_ENV}"
    )
    assert location.test_value == 24



# Generated at 2022-06-14 08:15:10.971843
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import tempfile

    temp_path = Path(
        tempfile.mkdtemp(
            prefix="test_load_module_from_file_location", suffix="/",
        )
    )
    module_name = "module_name"
    module_file_name = "module_file.py"
    module_file_path = Path(temp_path, module_file_name)
    module_file_path_without_ext = Path(
        temp_path, module_file_path.stem
    )
    module_file_content = (
        "CONSTANT = 42\n"
        "class MyClass:\n"
        "    @staticmethod\n"
        "    def do_something():\n"
        '        return "something"'
    )

# Generated at 2022-06-14 08:15:24.046119
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Tests load_module_from_file_location function.
    """
    os_environ["TEST_ENV"] = Path("tests").resolve().absolute()

    import pytest  # isort:skip

    pytest.importorskip("importlib_metadata")
    from importlib_metadata import version  # isort:skip  # noqa  # pylint: disable=wrong-import-order

    module = load_module_from_file_location(
        "tests/test_configurations/module1.py"
    )
    module = load_module_from_file_location(
        "tests/test_configurations/module2.py"
    )
    module = load_module_from_file_location(
        "tests/test_configurations/module3.py"
    )


# Generated at 2022-06-14 08:15:35.191867
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """
    Test that load_module_from_file_location works
    The test files are located in the same folder as this test file
    """
    # Try loading a file with no environment variable
    module = load_module_from_file_location("../tests/test_files/test_config_no_env.py")
    assert module.TEST_CONFIG_VAR["test_key_1"] == "test_value_1"

    # Try loading a file with environment variable
    module = load_module_from_file_location("../tests/test_files/${TEST_CONFIG_FILE}")
    assert module.TEST_CONFIG_VAR["test_key_2"] == "test_value_2"

    # Try loading a file in a folder with environment variable
    module = load_module_from_file_location

# Generated at 2022-06-14 08:15:45.450233
# Unit test for function load_module_from_file_location

# Generated at 2022-06-14 08:15:52.955226
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """
    Test function load_module_from_file_location.
    """
    os_environ["SOME_VAR_MOCK"] = "some_var_mock_value"

    # Test for location as a string.
    location = '/some/path/${SOME_VAR_MOCK}/config.py'
    module = load_module_from_file_location(location)
    assert 'some_var_mock_value' in module.__file__
    assert module.some_var_mock_value == 'some_var_mock_value'

    # Test for location as a pathlib.Path.
    location = Path('/some/path/${SOME_VAR_MOCK}/config.py')
    module = load_module_from_file_location(location)

# Generated at 2022-06-14 08:16:05.057970
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Test for function load_module_from_file_location"""

    sample_conf_module = Path(__file__).parent.parent / "sample_conf.py"
    loaded_module = load_module_from_file_location(sample_conf_module)
    assert loaded_module.FOO == True

    # location can be of a bytes type
    loaded_module = load_module_from_file_location(
        sample_conf_module.encode("utf-8")
    )
    assert loaded_module.FOO == True

    # location can contain an environment variables
    loaded_module = load_module_from_file_location(
        sample_conf_module.parent / "${HOME}/sample_conf.py"
    )
    assert loaded_module.FOO == True

    # when location is of a bytes type,

# Generated at 2022-06-14 08:16:18.154118
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    assert load_module_from_file_location("__main__")  # type: ignore

    with pytest.raises(PyFileError) as exc_info:
        load_module_from_file_location(__file__)

    assert __file__ in str(exc_info.value)

    with pytest.raises(IOError) as exc_info:
        load_module_from_file_location(__file__ + "emm-some-random-file-name")

    assert "Unable to load configuration file" in str(exc_info.value)

    location = Path(__file__).parent.joinpath("config.py")

    with pytest.warns(UserWarning) as record:
        module = load_module_from_file_location(location)


# Generated at 2022-06-14 08:16:29.202211
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # Test with non-existing path
    try:
        load_module_from_file_location("")
        assert False
    except LoadFileException:
        pass

    # Test with non-existing environment variable
    try:
        load_module_from_file_location("${not_existing_env_var}")
        assert False
    except LoadFileException:
        pass

    # Test with non-existing environment variable
    try:
        load_module_from_file_location("${not_existing_env_var}")
        assert False
    except LoadFileException:
        pass

# Generated at 2022-06-14 08:16:38.290010
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location(): # noqa
    # A) Check that we can resolve an environment variable.
    importlib.reload(importlib)
    os_environ["TEST_ENV_VAR"] = "test_env_value"
    spec = importlib.util.spec_from_file_location(
        "test_module",
        "/some/path/${TEST_ENV_VAR}/test_module.py"
    )
    assert spec.origin == "/some/path/test_env_value/test_module.py"

    # B) Check that we get a reasonable error if environment variable not set.
    del os_environ["TEST_ENV_VAR"]

# Generated at 2022-06-14 08:16:49.442078
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import sys, re, os

    # A) Test invalid location parameter.
    try:
        load_module_from_file_location(42)
    except LoadFileException as e:
        assert str(e) == "Invalid location parameter type: <class 'int'>"
    except Exception as e:
        raise

    # B) Test invalid location type parameter.
    try:
        load_module_from_file_location("config.py", 42)
    except LoadFileException as e:
        assert str(e) == "Invalid location type parameter: <class 'int'>"
    except Exception as e:
        raise

    # C) Run test after invalid location type parameter
    #    (e.g. location type is module).

# Generated at 2022-06-14 08:16:58.619257
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    import shutil

    # A)
    # Create tmp dir which will be used here.
    tmp_dir = Path(__file__).resolve().parent.joinpath("tmp")
    tmp_dir.mkdir(exist_ok=True)
    # Create test_module.py
    # test_module.py will be used by load_module_from_file_location func.
    test_module_path = tmp_dir.joinpath("test_module.py")

# Generated at 2022-06-14 08:17:10.169245
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import shutil
    import tempfile
    import os

    # Create two temporary directories for saving some file
    temp_dir_1 = tempfile.mkdtemp()
    temp_dir_2 = tempfile.mkdtemp()
    
    # Create test files
    _conf_str = '''
    OK_VARIABLE = True

    def ok_func():
        return True
    '''
    with open(temp_dir_1 + '/test_directories_file.py', 'w') as test_file:
        test_file.write(_conf_str)

    _conf_str = '''
    BAD_VARIABLE = True
    '''

# Generated at 2022-06-14 08:17:21.949384
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import tempfile
    import json

    # Checking that if location is a string, it can be loaded.
    tmp = tempfile.NamedTemporaryFile(mode="wt")
    tmp.write("foo = 'bar'")
    tmp.flush()

    loaded_module = load_module_from_file_location(tmp.name)

    assert loaded_module.foo == "bar"

    # Checking that if location is a bytes, it can be loaded.
    assert "foo" not in json.loads(
        load_module_from_file_location(json.dumps({"foo": "bar"}).encode()).__dict__
    )

    # Checking that if location is a bytes, it can be loaded even with encoding provided.

# Generated at 2022-06-14 08:17:29.447219
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # file path
    os_environ["env_var"] = "env_var_value"
    location = load_module_from_file_location(
        b"pathlib_testing.py", encoding="utf8"
    )
    assert location.__file__ == "pathlib_testing.py"
    assert location.some_var == "some_value"

    # file path with environment variable
    location = load_module_from_file_location(
        "${env_var}/pathlib_testing.py"
    )
    assert location.__file__ == "env_var_value/pathlib_testing.py"
    assert location.some_var == "some_value"

    # file path with missing environment variable

# Generated at 2022-06-14 08:17:40.699618
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    import lib.sanic_envconfig.config

    # Test loading from file
    some_module = load_module_from_file_location(
        Path(__file__).parent / "tests" / "helpers" / "some_module.py"
    )

    assert some_module.SOME_INT_VARIABLE == 1
    assert some_module.SOME_STR_VARIABLE == "some_string"

    # Test loading from file as string
    some_module = load_module_from_file_location(
        str(Path(__file__).parent / "tests" / "helpers" / "some_module.py")
    )
    assert some_module.SOME_INT_VARIABLE == 1
    assert some_module.SOME_STR_VARIABLE == "some_string"

# Generated at 2022-06-14 08:17:52.419803
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Some simple checks, that function will return proper values
    with proper arguments and raise proper exceptions with improper ones.

    Run with:
        python -m sanic.config.functions_for_vine_config test_load_module_from_file_location

    """
    abs_path = os.path.dirname(os.path.abspath(__file__))
    os.environ["test_env_var"] = str(abs_path)

    def _assert_module_dicts_equal(*modules):
        for k, v in modules[0].__dict__.items():
            for module in modules:
                assert module.__dict__[k] == v

    module_path = os.path.join(abs_path, "test.py")
    module_path_bytes = bytes(module_path, "utf8")


# Generated at 2022-06-14 08:18:06.278185
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import tempfile

    cfg_file = tempfile.NamedTemporaryFile(prefix="sanic_config_", suffix=".py")
    cfg_file.write(b"TEST_VALUE = 123")
    cfg_file.seek(0)
    cfg_file_name = cfg_file.name
    cfg_file.close()

    def test_with_location_as_name_and_path():
        assert load_module_from_file_location(
            "sanic_config", cfg_file_name
        ).TEST_VALUE == 123

    def test_with_location_as_name_and_path_without_ext():
        assert load_module_from_file_location(
            "sanic_config", cfg_file_name.replace(".py", "")
        ).T