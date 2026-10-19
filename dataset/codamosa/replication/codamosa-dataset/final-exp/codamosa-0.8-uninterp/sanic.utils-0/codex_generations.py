

# Generated at 2022-06-14 08:08:26.406318
# Unit test for function str_to_bool
def test_str_to_bool():
    assert str_to_bool("true") is True
    assert str_to_bool("TRUE") is True
    assert str_to_bool("yes") is True
    assert str_to_bool("yEs") is True
    assert str_to_bool("y") is True
    assert str_to_bool("Y") is True
    assert str_to_bool("on") is True
    assert str_to_bool("ON") is True
    assert str_to_bool("1") is True
    assert str_to_bool("false") is False
    assert str_to_bool("FALSE") is False
    assert str_to_bool("no") is False
    assert str_to_bool("nO") is False
    assert str_to_bool("n") is False
    assert str_to_bool("N") is False


# Generated at 2022-06-14 08:08:39.252033
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import sanic

    # Testing 1) when location is a bytes parameter.
    module = load_module_from_file_location(bytes(__file__, encoding="utf8"))
    assert module.__name__ == "sanic.helpers"
    # Testing 2) when location is a str parameter.
    module = load_module_from_file_location(str(__file__))
    assert module.__name__ == "sanic.helpers"
    # Testing 3) when location is a Path parameter.
    module = load_module_from_file_location(Path(__file__))
    assert module.__name__ == "sanic.helpers"
    # Testing 4) when location is a str parameter with environment variables.
    os_environ["test"] = "helpers"
    module = load_module_from_file_location

# Generated at 2022-06-14 08:08:47.103966
# Unit test for function str_to_bool
def test_str_to_bool():
    """Unit test for function str_to_bool."""

# Generated at 2022-06-14 08:08:53.496976
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import tempfile
    import pytest
    import inspect
    import os

    content = "a = 5\nb = 'mama'"
    content_as_bytes = content.encode()

    # The following 2 lines could probably be refactored,
    # but as they are not as important as functionality,
    # I leave them like that.
    path_to_file = tempfile.NamedTemporaryFile(mode="w+", suffix=".tmp").name
    path_to_file_as_bytes = path_to_file.encode()

    with open(path_to_file, "w+") as file:
        file.write(content)

    # Load module from file using location in bytes format.
    # The loaded module has name tmp_1 (file name without extension).
    module = load_module_from_file_location

# Generated at 2022-06-14 08:09:05.851968
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Unit test for function load_module_from_file_location"""

    # A) Check if location contains any environment variables
    #    in format ${some_env_var}.
    # B) Check these variables exists in environment.
    # C) Substitute them in location.

    # A)
    location = "/some_file.py"
    env_vars_in_location = set(re_findall(r"\${(.+?)}", location))
    assert not env_vars_in_location

    # B)
    not_defined_env_vars = env_vars_in_location.difference(os_environ.keys())
    assert not not_defined_env_vars

    # C)
    for env_var in env_vars_in_location:
        new_location = location.replace

# Generated at 2022-06-14 08:09:13.600617
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # A) Tests with environment variables inside location
    os_environ["some_env_var"] = "some_var"
    assert (
        load_module_from_file_location(
            "some_module_name", "/some/path/${some_env_var}"
        ).__name__
        == "some_module_name"
    )

    # B) Tests with .py inside location
    assert (
        load_module_from_file_location(
            "some_module_name", "/some/path/some_file.py"
        ).__name__
        == "some_module_name"
    )

    # C) Tests with .yaml inside location

# Generated at 2022-06-14 08:09:25.142351
# Unit test for function str_to_bool
def test_str_to_bool():

    assert str_to_bool("y")
    assert str_to_bool("yes")
    assert str_to_bool("yep")
    assert str_to_bool("yup")
    assert str_to_bool("t")
    assert str_to_bool("true")
    assert str_to_bool("on")
    assert str_to_bool("enable")
    assert str_to_bool("enabled")
    assert str_to_bool("1")

    assert not str_to_bool("n")
    assert not str_to_bool("no")
    assert not str_to_bool("f")
    assert not str_to_bool("false")
    assert not str_to_bool("off")
    assert not str_to_bool("disable")
    assert not str_to_bool("disabled")

# Generated at 2022-06-14 08:09:29.507310
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    with open("test_load.py", "w") as file:
        file.write("test_this = 'TEST'\n")
    module = load_module_from_file_location("test_load")
    assert module.test_this == "TEST"
    os.remove("test_load.py")

# Generated at 2022-06-14 08:09:36.401492
# Unit test for function str_to_bool
def test_str_to_bool():
    assert str_to_bool("y") is True
    assert str_to_bool("t") is True
    assert str_to_bool("1") is True
    assert str_to_bool("YeS") is True
    assert str_to_bool("Yes") is True
    assert str_to_bool("Y") is True
    assert str_to_bool("yes") is True
    assert str_to_bool("Yes") is True
    assert str_to_bool("YEP") is True
    assert str_to_bool("Yep") is True
    assert str_to_bool("Yup") is True
    assert str_to_bool("yup") is True
    assert str_to_bool("True") is True
    assert str_to_bool("true") is True
    assert str_to_bool("On") is True


# Generated at 2022-06-14 08:09:49.524762
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    # Test function with a string as a parameter
    some_module = load_module_from_file_location(
        "some_module_name", "some/path/some_module.py"
    )
    assert some_module.true_function()

    # Test function with a Path as a parameter
    path = Path(__file__).parent / "test_module.py"
    some_module = load_module_from_file_location("some_module_name", path)
    assert some_module.true_function()

    # Test that function has environment variable substitution.
    os_environ["some_env_var"] = "some/path"
    some_module = load_module_from_file_location(
        "some_module_name", "${some_env_var}/some_module.py"
    )


# Generated at 2022-06-14 08:10:02.040329
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Tests load_module_from_file_location function."""

    # A) Testing working with bytes object.
    #    Testing with environment vars in location.

    # Create test config file temporarily.
    temp_config_file = Path("tests/tmp_config.py")
    with open(temp_config_file, "w") as f:
        f.write("")

    # Set environment variables.
    os_environ["TMP_VAR_1"] = "var1"
    os_environ["TMP_VAR_2"] = "var2"

    # Prepare location for testing.

# Generated at 2022-06-14 08:10:14.951433
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # A) Check if str_to_bool works
    assert str_to_bool("y") == True
    assert str_to_bool("yes") == True
    assert str_to_bool("Y") == True
    assert str_to_bool("YES") == True
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

# Generated at 2022-06-14 08:10:26.245309
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import sys
    import tempfile
    import contextlib

    @contextlib.contextmanager
    def py_files_open(file_content, exec_=False, **file_kwargs):
        with tempfile.NamedTemporaryFile(
            suffix=".py", mode="w+", delete=False, **file_kwargs
        ) as f:
            f.write(file_content)
            f.seek(0)
            if exec_:
                exec(compile(f.read(), f.name, "exec"))
            yield f


# Generated at 2022-06-14 08:10:39.363367
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    _mod_spec = spec_from_file_location(
        "test_module", "/tmp/test_config.py", submodule_search_locations=[]
    )
    module = module_from_spec(_mod_spec)
    _mod_spec.loader.exec_module(module)  # type: ignore

    assert module.TOKEN == "chouette"
    assert module.__file__ == "/tmp/test_config.py"

    location = "/tmp/test_config2.py"
    module = load_module_from_file_location(location)
    assert module.TOKEN == "chouette2"

    module = load_module_from_file_location("/tmp/test_config3.py")
    assert module.k == 1

# Generated at 2022-06-14 08:10:44.983688
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa: D103
    import pytest  # noqa: F401

    location = "tests/data/sanic_app.py"
    module = load_module_from_file_location(location)
    assert module.__name__ == "sanic_app"
    assert module.__file__ == location
    assert module.__package__ is None



# Generated at 2022-06-14 08:10:56.454874
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Test for load_module_from_file_location function."""

    test_module_file_path = "tests/test_helper_functions.py"
    test_module_name = test_module_file_path.split("/")[-1].split(".")[0]

    # Test load_module_from_file_location function using file path.
    # Check if loaded module has expected name.
    assert (
        load_module_from_file_location(test_module_file_path).__name__
        == test_module_name
    )
    # Check if loaded module has expected __file__ attribute.
    assert (
        load_module_from_file_location(test_module_file_path).__file__
        == test_module_file_path
    )

    # Test load_module_from

# Generated at 2022-06-14 08:11:08.747475
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from os import environ as os_environ

    tmp_path_1 = "/tmp/test/"
    tmp_path_2 = "/tmp/test/2/"
    os_environ["SANIC_ENV_VAR_1"] = tmp_path_1
    os_environ["SANIC_ENV_VAR_2"] = tmp_path_2

    assert (
        load_module_from_file_location(
            "/opt/test/${SANIC_ENV_VAR_1}test.py"
        ).__file__
        == tmp_path_1 + "test.py"
    )

# Generated at 2022-06-14 08:11:19.880756
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    assert str_to_bool("on") is True
    assert str_to_bool("off") is False

    assert str_to_bool("yes") is True
    assert str_to_bool("false") is False
    try:
        str_to_bool("some_invalid_bool_string")
        assert False, "str_to_bool did not catch invalid bool string"
    except ValueError:
        pass

    location = Path(__file__).parent / "test_data"

    assert (
        load_module_from_file_location(location / "some_module.py").some_value
        == "some_value"
    )
    assert (
        load_module_from_file_location(location / "some_module.py").some_func()
        == "some_func"
    )

    assert load

# Generated at 2022-06-14 08:11:32.172160
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    import tempfile
    import os
    import sys

    test_env_var = "SANIC_TEST_ENV_FILE"

# Generated at 2022-06-14 08:11:36.875352
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    module = load_module_from_file_location("tests/config.py")
    assert module.TEST_CONFIG == "Test"
    assert module.TEST_CONFIG_2 == 2
# End unit test for function load_module_from_file_location



# Generated at 2022-06-14 08:11:49.754101
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    location = os.path.join(os.path.dirname(__file__), "tests/data/configuration.py")
    # Test importing using path
    _configuration = load_module_from_file_location(location)
    assert _configuration.HELLO == "world"
    # Test importing using string
    _configuration = load_module_from_file_location(str(location))
    assert _configuration.HELLO == "world"
    # Test importing using Path
    _configuration = load_module_from_file_location(Path(location))
    assert _configuration.HELLO == "world"
    # Test importing using bytes
    _configuration = load_module_from_file_location(bytes(location, "utf-8"))
    assert _configuration.HELLO == "world"
   

# Generated at 2022-06-14 08:12:02.186288
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    class Person:
        """
        This is my custom class.
        """
        pass  # noqa

    with open(
        f"{Path(__file__).parent}/tests/configs/load_module_from_file_location.py",
        "w",
    ) as f:
        f.write(
            """FOUR = 4\n"I am string"\n"I am \\n string"\n'I am \\' string'\n"I am \\\\n string"\n\nSmile = "\u263A"\nPerson = "sanic.exceptions.LoadFileException.Person"\n\n"""  # noqa
        )  # write data to a file


# Generated at 2022-06-14 08:12:07.890707
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    os_environ["SOME_ENV_VAR"] = "/test/test_app"
    module = load_module_from_file_location(
        "test_app",
        "/some/path/${SOME_ENV_VAR}/test.py"
    )
    assert module

# Generated at 2022-06-14 08:12:20.219713
# Unit test for function load_module_from_file_location

# Generated at 2022-06-14 08:12:31.263134
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    try:
        # A) Test trying to load configuration with invalid environment
        #    variables in format ${some_undefined_env_var}.
        some_module = load_module_from_file_location(
            "some_module_name", "/some/path/${some_undefined_env_var}"
        )
    except LoadFileException as e:
        assert (
            "The following environment variables are not set: some_undefined_env_var"
            in e.args
        )
    else:
        raise AssertionError(
            "In case of trying to load configuration with invalid "
            "environment variables LoadFileException should be raised."
        )


# Generated at 2022-06-14 08:12:33.322787
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """[summary]
    """
    assert load_module_from_file_location("sanic.log")

# Generated at 2022-06-14 08:12:41.661744
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    os_environ["env_var"] = "some_random_value"

    location = "${env_var}/module_name.py"
    with pytest.raises(LoadFileException):
        load_module_from_file_location(location)

    location = f"{Path.cwd()}/module_name.py"

    module = load_module_from_file_location(location)
    assert module.SETTINGS1 == "Loaded from file"
    assert module.SETTINGS2 == "Loaded from file too"

# Generated at 2022-06-14 08:12:53.239851
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Unit test for function load_module_from_file_location"""


# Generated at 2022-06-14 08:13:02.958051
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # A) The module and the file is located in the root directory.
    #    Then we can try to load it as:
    res = load_module_from_file_location("__main__")
    assert res.__name__ == "__main__"

    # B) There is no file.
    #    Then we should get importlib.util.ModuleSpec error.
    from importlib.util import ModuleSpec

    with pytest.raises(ModuleSpec.ModuleNotFoundError):
        load_module_from_file_location("qwertyuiop")

    # C) There is a file, but there are problems with it.
    #    Then we should get `sanic.exceptions.PyFileError`.
    #    Case 1. There are syntax errors.
    with pytest.raises(PyFileError):
        load_module

# Generated at 2022-06-14 08:13:15.206964
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from tempfile import TemporaryDirectory

    with TemporaryDirectory() as tmpdirname:
        tmpdirname = Path(tmpdirname)
        tmp_module = tmpdirname / "tmp_module.py"
        tmp_module.touch()

        tmp_content = {
            "key1": "value1",
            "key2": "value2",
            "key3": "value3",
        }
        with open(tmp_module, "w") as module:
            module.write(
                "from typing import Any\n\n"
                "var1: Any = {}\n\n"
                "var2: Any = {}".format(
                    repr(tmp_content["key1"]), repr(tmp_content["key2"])
                )
            )


# Generated at 2022-06-14 08:13:27.307692
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    os_environ["SANIC_ENV_VARIABLE"] = "test"
    assert (
        load_module_from_file_location(
            "tests.unit.helpers_test_module",
            "${SANIC_ENV_VARIABLE}/unit/helpers_test_module.py",
        ).__name__
        == "tests.unit.helpers_test_module"
    )

# Generated at 2022-06-14 08:13:35.369722
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """
    When You set environment variable for PYTHONPATH, it can happen that
    You will have import error in the line with import_string.
    Therefore You should run tests from the root directory of a project like:
    python -m tests.helpers.test_load_module_from_file_location
    """

    import sanic

    CURR_DIR = Path(sanic.__file__).resolve().parent
    TEST_DIR = Path(__file__).resolve().parent

    class TestModule(object):
        def __init__(self):
            self.test_value = None
            self.test_value2 = None

    test_fname = "test_module_file.py"
    test_fname_other = "test_module_file_other.py"

# Generated at 2022-06-14 08:13:43.969504
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    test_file = Path(__file__).parent / "test_file.txt"
    test_python_file = Path(__file__).parent / "test_file.py"
    assert load_module_from_file_location(test_file) == "test content"
    test_config_module = load_module_from_file_location(test_python_file)
    assert test_config_module.test_config_var == "test"
    assert test_config_module.test_function() == "test function"

# Generated at 2022-06-14 08:13:56.038750
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    def _test_resolving_env_vars_in_location(
        env_vars_in_location: set,
        os_environ_entries: dict,
        location: str,
        expected_location: str,
    ):

        # A) Check if location contains any environment variables
        #    in format ${some_env_var}.
        assert set(re_findall(r"\${(.+?)}", location)) == env_vars_in_location
        # B) Check these variables exists in environment.
        assert env_vars_in_location.difference(
            os_environ.keys()
        ) == set()  # or os_environ_entries.keys()

        # C) Substitute them in location.

# Generated at 2022-06-14 08:14:09.134151
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    def test_location(location):
        """
        Function for testing load_module_from_file_location
        """
        module = load_module_from_file_location(location)
        assert module.FOO == 1
        assert module.BAR == 2

    # 1. Test load_module_from_file_location with string.
    path = "/tmp/file.py"
    with open(path, "w+") as f:
        f.write("FOO = 1\nBAR = 2\n")
    test_location(path)

    # 2. Test load_module_from_file_location with Path.
    path = Path("/tmp/file.py")
    with open(path, "w+") as f:
        f.write("FOO = 1\nBAR = 2\n")
    test

# Generated at 2022-06-14 08:14:15.829484
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Simple test for load_module_from_file_location function."""
    import pytest
    from tempfile import TemporaryDirectory
    from textwrap import dedent

    with TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        os_environ["TEST_ENV_VAR"] = str(tmpdir)
        os_environ["TEST_ENV_VAR2"] = str(tmpdir)

        # Check that when no environment variables are present,
        # then everything is just works.
        tmp_config_file = tmpdir / "config.py"
        tmp_config_file.write_text(dedent("""
        TESTVAR = 42
        """).strip())
        module = load_module_from_file_location(tmp_config_file)

# Generated at 2022-06-14 08:14:24.565562
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import os
    import pytest

    # 1. Check if function raises error for the following:
    # a. Non existing location
    with pytest.raises(LoadFileException):
        load_module_from_file_location("./non-existing-path/file.py")

    # b. Location of not a .py file
    with pytest.raises(LoadFileException):
        load_module_from_file_location("./test-data/textfile")

    # c. Location is of a bytes type, but not in utf-8 encoding

# Generated at 2022-06-14 08:14:30.050257
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    assert load_module_from_file_location("types") == types
    assert load_module_from_file_location(__file__) == sys.modules[__name__]
    assert (
        load_module_from_file_location(__file__.replace(".py", ".txt"))
        == sys.modules[__name__]
    )

# Generated at 2022-06-14 08:14:42.292026
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from pathlib import Path
    from copy import copy

    # A) Test location as str.
    config = load_module_from_file_location(
        "tests.fixtures.test_config",
    )
    assert config.test_config["test"] == "test"

    # B) Test location as absolut_path.
    absolut_path_to_test_config = Path(
        "tests/fixtures/test_config.py"
    ).resolve()
    config = load_module_from_file_location(
        absolut_path_to_test_config,
    )
    assert config.test_config["test"] == "test"

    # C) Test location as environment_var

# Generated at 2022-06-14 08:14:48.213396
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    # GIVEN
    location = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../../examples/simple_get.py")
    )

    # WHEN
    _module = load_module_from_file_location(location)

    # THEN
    assert _module is not None



# Generated at 2022-06-14 08:15:04.614587
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    import unittest
    import unittest.mock
    import sys

    class TestCase(unittest.TestCase):

        def setUp(self):
            self.mock_import_module_simple = unittest.mock.patch(
                "sanic.helpers.load_module_from_file_location."
                "import_string",
                return_value="some_module_simple",
            )
            self.mock_import_module_simple.start()

            self.mock_import_module_and_func = unittest.mock.patch(
                "sanic.helpers.load_module_from_file_location."
                "import_string",
                return_value="some_module_and_func",
            )
            self.mock_import_module_

# Generated at 2022-06-14 08:15:17.521247
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import os

    file_location = "test_load_module_from_file_location"
    file_path = os.path.dirname(os.path.abspath(__file__)) + '/' + file_location

    # Testing that it is possible to import module when it is not in path.
    module = load_module_from_file_location(file_location)
    assert module

    # Testing that it is possible to import module with path.
    module = load_module_from_file_location(file_path)
    assert module

    # Testing that it is possible to use environment variables in path.
    env_var_name = "SANIC_CUSTOM_CONFIG_PATH"
    env_var_value = file_path
    os.environ[env_var_name] = env_var_value
    module

# Generated at 2022-06-14 08:15:27.418091
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    def test_my_config_py_func():
        assert "test_file_content" == os_environ["TEST_VAR"]

    def test_my_config_py():
        assert test_my_config_py_func.__name__ in __main__.config.__dict__

    from tempfile import TemporaryDirectory

    import tempfile

    with TemporaryDirectory() as tmp_dir:
        config_file = tempfile.NamedTemporaryFile(mode="w", dir=tmp_dir)
        config_file.write("test_file_content")
        config_file.flush()
        os_environ["TEST_VAR"] = config_file.name

# Generated at 2022-06-14 08:15:40.719945
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from tempfile import mkdtemp
    from os import environ
    from os.path import join

    tmp_dir_path = mkdtemp(prefix="tmp_sanic_config")
    config_path = join(tmp_dir_path, "config.py")
    environ_var = "SANIC_CONFIG_TEMP_DIR"

    with open(config_path, "w") as f:
        f.write(
            f"test_var = 'some_word'\n"
            f"test_var2 = 'some_word2'\n"
        )

    config = load_module_from_file_location(config_path)


# Generated at 2022-06-14 08:15:48.638575
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import os
    import sys

    # Prepare
    test_module_path = os.path.dirname(__file__)
    os_environ["SANIC_TEST_ENV_VAR"] = test_module_path

    # Test for invalid parameters
    try:
        load_module_from_file_location(1)
    except ValueError as e:
        assert str(e) == "location parameter has to be either string, bytes or pathlib.Path object"  # noqa
    else:
        assert False

    try:
        load_module_from_file_location(
            b"config.py", encoding="non_exists_encoding"
        )
    except LookupError as e:
        assert str(e) == "unknown encoding: non_exists_encoding"  # noqa

# Generated at 2022-06-14 08:16:01.700782
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    import importlib
    import sys
    # Create temporary file.
    with open("/tmp/tmp_file.txt", "w+") as f:
        f.write("x=1")
    module = load_module_from_file_location("/tmp/tmp_file.txt")
    assert module.x == 1
    # Remove temporary file.
    importlib.reload(os)
    os.remove("/tmp/tmp_file.txt")
    # Create temporary file.
    with open("/tmp/tmp_file.txt", "wb+") as f:
        f.write(b"x=1")
    module = load_module_from_file_location("/tmp/tmp_file.txt")
    assert module.x == 1
    # Remove temporary file.

# Generated at 2022-06-14 08:16:03.210637
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    os_environ["A_ENV_VAR"] = "1"
    from . import config1

    mod = load_module_from_file_location(Path(__file__).parent / "config1.py")
    assert mod.CONFIG1_KEY == config1.CONFIG1_KEY

# Generated at 2022-06-14 08:16:16.515798
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # 1. Some very normal import
    # test1.py file must be somewhere in sys.path
    sys_path = sys.path[:]
    for sys_path_item in sys_path:
        try:
            load_module_from_file_location("test1")
            break
        except ImportError:
            continue
    else:
        raise Exception("Unit test failed. Should never happen")

    # 2. Import from file.
    # Set location of test2.py from file.
    test2_file = Path(sys_path[-1]) / "test2.py"
    load_module_from_file_location(test2_file)

    # 3. Import ${PWD}/test3.py
    test3_file = Path("test3.py")

# Generated at 2022-06-14 08:16:28.878692
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    os_environ["SOME_ENV_VAR"] = "test/test_app"
    os_environ["SOME_ENV_VAR_2"] = "test/test_app/config_test_2.py"
    os_environ["SOME_ENV_VAR_3"] = "test/test_app/config_test_3.py"
    os_environ["SOME_ENV_VAR_4"] = "test/test_app/config_test_4.py"

    # Test loading with location as pathlib.Path
    module = load_module_from_file_location(
        Path(os_environ["SOME_ENV_VAR"]) / "config_test_1.py"
    )

# Generated at 2022-06-14 08:16:37.817838
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    import unittest

    import tempfile

    from pathlib import Path

    from os import environ

    class TestLoadModuleFromFileLocation(unittest.TestCase):

        def setUp(self):
            # Create temporary file to test if
            # load_module_from_file_location can import it.

            with tempfile.NamedTemporaryFile() as temp:
                temp.write(b"sample_var = 'sample_data'")
                temp.seek(0)
                self.tmp_file = temp.name

        def tearDown(self):
            pass

        def test_file_path_and_result(self):
            location = self.tmp_file
            module = load_module_from_file_location(location)
            self.assertEqual(module.sample_var, "sample_data")


# Generated at 2022-06-14 08:17:02.241297
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import tempfile
    import shutil

    test_module_name = "test"
    test_module_content = "test_variable = 42"
    test_env_var_name = "SANIC_TEST_ENV_VAR"
    test_env_var_value = "42"

    # A) Setting environment variable needed for this test
    os_environ[test_env_var_name] = test_env_var_value

    # B) Create temp directory for tests.
    #    We need to manually clean it, but after tests will be finished.
    temp_test_dir = tempfile.mkdtemp()
    temp_test_dir = Path(temp_test_dir)


# Generated at 2022-06-14 08:17:07.511308
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import tempfile

    # 1. Check that value error is raised if location parameter is not of
    #  type string or bytes.
    location = {"something": "some_value"}
    with pytest.raises(ValueError):
        _mod = load_module_from_file_location(location)

    # 2. Check that load file exception is raised if env_var is not defined
    #  in the environment where you execute code.
    with tempfile.TemporaryDirectory() as tmp_dir:
        location = Path(tmp_dir) / "my_conf.py"
        with open(location, "w") as my_conf:
            my_conf.write(
                "CONFIG_VALUE = 'value'\n"
                "IMPORTED = '${ENV_VAR}'\n"
            )

# Generated at 2022-06-14 08:17:19.505006
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """
    Testing load_module_from_file_location()
    """
    import sys
    import subprocess
    import os
    import tempfile
    import shutil

    # We are testing module loaded by path.
    # So let's make temp directory.
    temp_dir = tempfile.mkdtemp()
    temp_path = Path(temp_dir)
    file_name = "test.py"
    file_path = temp_path / file_name

    # Testing return value when file does not exists.
    def test_return_value_if_file_does_not_exist():
        with pytest.raises(FileNotFoundError):
            load_module_from_file_location(file_path)

    # Testing return value when file does exists, but does not contain any
    # python code.

# Generated at 2022-06-14 08:17:28.361964
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import os
    import tempfile
    import textwrap
    import pathlib

    FEW_ENV_VARS = [
        ("var1", "1"),
        ("var2", "2"),
        ("var3", "3"),
    ]

    def assert_loaded_module_same_as_fixture(
        loaded_module,
        fixture,
    ):
        assert loaded_module.__name__ == fixture.__name__
        assert loaded_module.__file__ == fixture.__file__
        for attr in dir(fixture):
            if not attr.startswith("__"):
                assert attr in dir(loaded_module)
                assert getattr(loaded_module, attr) == getattr(fixture, attr)


# Generated at 2022-06-14 08:17:33.299672
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import os
    import sys

    import pytest

    s = "some_module_name"
    f = "/some/path/file_name.py"
    os.environ["some_env_var"] = "env_var_value"
    os.environ["another_env_var"] = "another_value"

    sys.modules[s] = None
    with pytest.raises(
        LoadFileException,
        match="The following environment variables are not set: "
        "not_defined_env_var",
    ):
        _ = load_module_from_file_location(
            "some_module_name",
            "/some/path/${some_env_var}/${not_defined_env_var}/file_name.py",
        )

    _ = load_module_from_file_

# Generated at 2022-06-14 08:17:43.679548
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    assert load_module_from_file_location("types").__name__ == "types"
    assert load_module_from_file_location("re").__name__ == "re"

    import random, string  # noqa


# Generated at 2022-06-14 08:17:52.437069
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    some_module = load_module_from_file_location(
        "sanic.exceptions", "./sanic/exceptions.py"
    )
    assert some_module is exceptions

    os_environ["SANIC_EXCEPTIONS"] = "./sanic/exceptions.py"
    some_module = load_module_from_file_location(
        "sanic.exceptions", "${SANIC_EXCEPTIONS}"
    )
    assert some_module is exceptions



# Generated at 2022-06-14 08:18:06.329899
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    assert load_module_from_file_location(
        os.getcwd() + "/tests/files/configs/yaml.yml"
    ).PROP_1 == "bar"
    assert load_module_from_file_location(
        os.getcwd() + "/tests/files/configs/json.json"
    ).PROP_1 == "bar"
    assert load_module_from_file_location(
        os.getcwd() + "/tests/files/configs/env.env"
    ).env_1 == "foo"
    try:
        load_module_from_file_location(
            os.getcwd() + "/tests/files/configs/python.py"
        )
    except PyFileError:
        pass

# Generated at 2022-06-14 08:18:11.755680
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    # A) First lets define location and some environment variables
    location = "${PWD}/tests/test_loader.py"
    # lets assume this exists in environment
    os_environ["PWD"] = "/home/some_user/some_project/sanic"

    # B) Now let's see that when we would just inject one environment variable
    #    into a location.
    module_from_env_var = load_module_from_file_location(location)
    assert module_from_env_var.__name__ == "test_loader"
    assert "TEST_VAR_A" in module_from_env_var.__dict__
    assert module_from_env_var.TEST_VAR_A == 1

    # C) Now let's see that when we would inject two environment variables
    #    into a