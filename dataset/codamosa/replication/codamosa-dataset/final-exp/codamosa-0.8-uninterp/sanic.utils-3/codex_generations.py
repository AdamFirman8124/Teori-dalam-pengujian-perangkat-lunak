

# Generated at 2022-06-14 08:08:18.464899
# Unit test for function str_to_bool
def test_str_to_bool():
    assert str_to_bool("1") is True
    assert str_to_bool("Yes") is True
    assert str_to_bool("y") is True
    assert str_to_bool("n") is False
    assert str_to_bool("") is False

# Generated at 2022-06-14 08:08:29.168881
# Unit test for function str_to_bool
def test_str_to_bool():
    assert str_to_bool("y") == True
    assert str_to_bool("Y") == True
    assert str_to_bool("yes") == True
    assert str_to_bool("YES") == True
    assert str_to_bool("yeP") == True
    assert str_to_bool("yEs") == True
    assert str_to_bool("yes") == True
    assert str_to_bool("t") == True
    assert str_to_bool("T") == True
    assert str_to_bool("true") == True
    assert str_to_bool("TRUE") == True
    assert str_to_bool("True") == True
    assert str_to_bool("on") == True
    assert str_to_bool("ON") == True
    assert str_to_bool("On") == True
   

# Generated at 2022-06-14 08:08:41.398622
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import os
    import tempfile
    import shutil
    some_env_var = "some/path/to/config"
    os.environ["some_env_var"] = some_env_var
    temp_dir = tempfile.mkdtemp()

# Generated at 2022-06-14 08:08:52.814080
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import tempfile
    import uuid
    import os


# Generated at 2022-06-14 08:09:05.587554
# Unit test for function str_to_bool
def test_str_to_bool():
    assert str_to_bool("t")
    assert str_to_bool("yes")
    assert str_to_bool("yup")
    assert str_to_bool("T")
    assert str_to_bool("00")
    assert str_to_bool("1")
    assert str_to_bool("enabled")
    assert not str_to_bool("no")
    assert not str_to_bool("nope")
    assert not str_to_bool("n")
    assert not str_to_bool("False")
    assert not str_to_bool("FALSE")
    assert not str_to_bool("0")
    assert not str_to_bool("disabled")
    assert str_to_bool("T")
    with pytest.raises(ValueError):
        str_to_bool("not a valid string")

# Generated at 2022-06-14 08:09:11.613241
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import pytest
    import random
    import string
    import tempfile

    from os import environ
    from pathlib import Path
    from unittest.mock import patch

    from sanic.config import Config
    from sanic.log import LOGGING_CONFIG_DEFAULTS

    from .config_manager import _validate_not_a_dict
    from .core import Sanic

    def gen_random_file_path(num_of_letters=10):
        return "/some/random/path/random_name." + "".join(
            random.choice(string.ascii_lowercase) for _ in range(num_of_letters)
        )


# Generated at 2022-06-14 08:09:23.670419
# Unit test for function str_to_bool
def test_str_to_bool():
    assert str_to_bool("1") is True
    assert str_to_bool("true") is True
    assert str_to_bool("on") is True
    assert str_to_bool("yes") is True
    assert str_to_bool("y") is True
    assert str_to_bool("t") is True

    assert str_to_bool("0") is False
    assert str_to_bool("false") is False
    assert str_to_bool("off") is False
    assert str_to_bool("no") is False
    assert str_to_bool("n") is False
    assert str_to_bool("f") is False

    with pytest.raises(ValueError) as e:
        str_to_bool("10")
    assert "Invalid truth value 10" in str(e.value)

# Generated at 2022-06-14 08:09:33.170470
# Unit test for function str_to_bool
def test_str_to_bool():
    assert str_to_bool("true") is True
    assert str_to_bool("True") is True
    assert str_to_bool("TRUE") is True
    assert str_to_bool("TrUe") is True

    assert str_to_bool("false") is False
    assert str_to_bool("False") is False
    assert str_to_bool("FALSE") is False
    assert str_to_bool("fAlSe") is False

    assert str_to_bool("y") is True
    assert str_to_bool("Y") is True
    assert str_to_bool("yes") is True
    assert str_to_bool("yep") is True
    assert str_to_bool("yup") is True
    assert str_to_bool("YES") is True

# Generated at 2022-06-14 08:09:42.097611
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Unit test for function load_module_from_file_location. """
    import tempfile
    from os import environ
    import os

    # try to load file that is not exist
    try:
        module = load_module_from_file_location("not_existing_file.py")
    except LoadFileException as e:
        pass

    # try to load file that is not a python source file
    try:
        module = load_module_from_file_location("not_a_file.py")
    except PyFileError as e:
        pass

    # try to load file that is not a python source file
    try:
        module = load_module_from_file_location("not_a_file")
    except PyFileError as e:
        pass

    # try to load file with unresolved environment variable

# Generated at 2022-06-14 08:09:47.336554
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    from tempfile import TemporaryDirectory

    from pathlib import Path

    def assert_module_equal(a, b):
        for attr in dir(b):
            if not attr.startswith("_"):
                assert getattr(a, attr) == getattr(b, attr)

    with TemporaryDirectory() as tmp:
        # Test that module is well loaded when location is a bytes string.
        module_bytes = load_module_from_file_location(
            Path(__file__).read_bytes(), "utf8"
        )
        module_str = load_module_from_file_location(__file__)
        assert_module_equal(module_str, module_bytes)

        # Test that module is well loaded when location is a path.
        module_path = load_module_from_file

# Generated at 2022-06-14 08:09:55.833771
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Unit test for function load_module_from_file_location."""
    assert (
        load_module_from_file_location(
            "tests.unit.common.test_load_module.tests_file"
        ).TEST_VARIABLE
        == "unittest"
    )



# Generated at 2022-06-14 08:10:08.703246
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # Given
    from os.path import dirname, join
    from tempfile import NamedTemporaryFile

    from sanic import Sanic
    from sanic.config import ConfigError

    here = dirname(__file__)
    static_file = join(here, "static/css/style.css")
    python_file = join(here, "app.py")

    # When
    loaded_module_static_file = load_module_from_file_location(static_file)
    # Then
    assert isinstance(loaded_module_static_file, types.ModuleType)
    assert loaded_module_static_file.__file__ == static_file

    # When
    loaded_module_python_file = load_module_from_file_location(python_file)
    # Then

# Generated at 2022-06-14 08:10:18.563279
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    def load_module(location):
        """Helper function to load a module from a file location"""
        _mod_spec = importlib.util.spec_from_file_location(
            "config", location
        )
        module = importlib.util.module_from_spec(_mod_spec)
        _mod_spec.loader.exec_module(module)  # type: ignore
        return module

    def prepare_config_file(config_lines):
        """Helper function to create a config file with some content"""
        with tempfile.TemporaryDirectory() as tmpdir:
            filepath = os.path.join(tmpdir, "config.py")
            with open(filepath, "w") as config_file:
                config_file.write("\n".join(config_lines) + "\n")
            return file

# Generated at 2022-06-14 08:10:27.962668
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    os_environ["test"] = "test_location"
    os_environ["foo"] = "foo_location"
    os_environ["bar"] = "bar_location"

    test_location = os_environ["test"]
    foo_location = os_environ["foo"]
    bar_location = os_environ["bar"]

    def test(location, args, kwargs):
        module = load_module_from_file_location(location, *args, **kwargs)
        assert module.__file__ == location
        assert module.foo == "foo"
        assert module.bar == "bar"
        assert module.option1 == "option1"
        assert module.option2 == "option2"
        assert module.option3 == "option3"

    # Test for:
    # 1. With Path inputs

# Generated at 2022-06-14 08:10:40.688894
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import shutil
    import tempfile
    import os

    def test_env_var_in_location_parameter():
        # A) Create some dummy environment variables
        os_environ.update(
            {
                "SOME_ENV_VAR_FILE_LOCATION": "some_env_var_file_location",
                "SOME_ENV_VAR_FILE_NAME": "some_env_var_file_name",
                "SOME_ENV_VAR_FILE_CONTENT": "some_env_var_file_content",
            }
        )

        # B) Create temp directory.
        temp_dir = tempfile.mkdtemp()

        # C) Create file in this temp directory.

# Generated at 2022-06-14 08:10:53.441707
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from os import environ, makedirs
    from os.path import join
    from shutil import rmtree
    from tempfile import mkdtemp
    from uuid import uuid4

    from pytest import raises

    from sanic.helpers import load_module_from_file_location

    # A. Testing errors
    expected_exception_message = "Unable to load configuration file"

    # A1. Environment variables in format ${some_env_var}
    # A1.1 No such environment variables
    temp_dir = mkdtemp()
    with open(join(temp_dir, str(uuid4()) + ".py"), "w") as f:
        f.write("")

    location = join(temp_dir, "1.py")
    with raises(LoadFileException) as exception:
        load_module_

# Generated at 2022-06-14 08:11:05.497493
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    os_environ["SOME_ENV_VAR"] = "some_env_var"
    os_environ["OTHER_ENV_VAR"] = "other_env_var"

    with patch("sanic.utils.os.environ") as os_environ_mock:
        os_environ_mock.copy.return_value = {
            "SOME_ENV_VAR": "some_env_var",
            "OTHER_ENV_VAR": "other_env_var",
        }

        os_environ_mock.keys.return_value = ["SOME_ENV_VAR", "OTHER_ENV_VAR"]


# Generated at 2022-06-14 08:11:18.376858
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Unit test for function load_module_from_file_location.

    This is an integration test as it ties three different functions together:
        1. load_module_from_file_location
        2. get_group_in_config
        3. update_setting_with_env_var

    """
    from .config import Config

    config_file_name = "conf_error.py"
    env_var_name = "NEW_ENV_VAR"

    cur_dir = Path(__file__).parent
    config_file_path = str(
        (cur_dir / "configuration_files").resolve() / config_file_name
    )

    # GET AND SET ENVIRONMENT VARIABLE
    env_var_name_env = "CONF_ENV_VAR"
    env_var_

# Generated at 2022-06-14 08:11:31.127261
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    # T1: Check if location is not string or Path object.
    with pytest.raises(LoadFileException):
        load_module_from_file_location(128)

    # T2: Check if location is a string.
    #     Check if location contains undefined environment variable.
    os_environ["env_var"] = "value"
    with pytest.raises(LoadFileException):
        load_module_from_file_location("${env_var_2}")
    del os_environ["env_var"]

    # T3: Check if location is a string.
    #     It contains environment variable in format ${some_env_var}.
    os_environ["env_var"] = "value"
    location = load_module_from_file_location("${env_var}")

# Generated at 2022-06-14 08:11:43.875220
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    environ = os.environ
    example_environ = {
        "ENABLE": "yes",
        "SIMPLE_VAR_1": "test",
        "SIMPLE_VAR_2": "test",
        "RESTART_PATH": "test",
        "SOME_VAR_3": "test",
        "HOST": "test",
        "PORT": "test",
    }
    os.environ = example_environ

# Generated at 2022-06-14 08:12:03.212818
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """ Unit test for function load_module_from_file_location. """

    import sys
    import shutil
    import os
    import pathlib

    import pytest

    # Set test data directory
    test_data_dir = "tests/sanic/helpers/test_data"

    # Exceptions to check
    # 1) No file in path.
    with pytest.raises(LoadFileException) as excinfo:
        load_module_from_file_location("some_nonexistent_file")

    # 2) File exists and is a directory.
    with pytest.raises(LoadFileException) as excinfo:
        load_module_from_file_location(".")

    # 3) Valid .py file, but module name is invalid.

# Generated at 2022-06-14 08:12:16.926432
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Test load_module_from_file_location function."""
    import inspect

    # We load fixture config file
    fixture_module = load_module_from_file_location(
        "/configs/fixtures/fixture_module.py"
    )

    assert (
        inspect.getfile(fixture_module) == "/configs/fixtures/fixture_module.py"
    )
    assert fixture_module.__name__ == "fixture_module"
    assert fixture_module.text == "some text"
    assert fixture_module.a == "a"
    assert fixture_module.b == "b"
    assert fixture_module.c == "c"
    assert fixture_module.foo == {"bar": "baz", "bam": "boom"}
    assert fixture_module.num == 25

# Generated at 2022-06-14 08:12:28.008395
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Unit test for function load_module_from_file_location."""
    # A) If location is absolute path, returns module.

    assert isinstance(
        load_module_from_file_location(
            "${PWD}".encode("utf8"),
            "${PWD}/sanic/examples/simple_server.py",
        ),
        types.ModuleType,
    )

    assert isinstance(
        load_module_from_file_location(
            "${PWD}/sanic/examples/simple_server.py".encode("utf8")
        ),
        types.ModuleType,
    )

    # B) If location contains environment variables substitution, returns module


# Generated at 2022-06-14 08:12:38.448294
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    import json
    import os
    import os.path
    import tempfile

    import pytest

    # 0.
    some_module = load_module_from_file_location(
        "sanic.config", *("__package__",)
    )
    assert some_module.__package__ == "sanic"

    # 1.
    some_module = load_module_from_file_location(
        "sanic.config", *("__package__",), raise_errors=True
    )
    assert some_module.__package__ == "sanic"

    # 2.
    with pytest.raises(ImportError):
        load_module_from_file_location(
            "sanic.conf", *("__package__",), raise_errors=True
        )

    # 3.
   

# Generated at 2022-06-14 08:12:48.374001
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    name = "some_file"
    file_content = "structure=True"
    file_path = f"/some/path/{name}.py"
    os_environ["some_env_var"] = file_path

    with open(file_path, "w") as f:
        f.write(file_content)

    module = load_module_from_file_location(f"$some_env_var")

    assert module.structure is True
    assert module.__file__ == file_path

    del os_environ["some_env_var"]

# Generated at 2022-06-14 08:12:59.697449
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    import tempfile

    from os import environ as os_environ

    from pathlib import Path

    from sanic import Sanic

    from sanic.config import Config

    from sanic.constants import CONFIG_DEFAULTS

    from sanic.exceptions import LoadFileException

    from sanic.helpers import get_function_name_from_path
    from sanic.helpers import load_module_from_file_location as lmffl

    CONFIG_DEFAULT_TYPE_BOOL = CONFIG_DEFAULTS[get_function_name_from_path(
        Sanic, "bool_or_dotted_path"
    )]

    config_dict = {"KEY": "VALUE"}

# Generated at 2022-06-14 08:13:05.553753
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    # A) Tests for good cases.

    # A1) Test for module import from file.
    loaded_module = load_module_from_file_location(
        __file__.replace("tests/", "sanic/")
    )
    assert hasattr(loaded_module, "str_to_bool")

    # A2) Test for module imported from file and then from a string.
    loaded_module = load_module_from_file_location(
        __file__.replace("tests/", "sanic/"),
        "sanic.utils.functions",
    )
    assert hasattr(loaded_module, "str_to_bool")

    # B) Tests for bad cases.

    # B1) Tests for wrong file path.

# Generated at 2022-06-14 08:13:16.901309
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import sys
    import os
    import shutil

    def clean_up(file_path: Union[str, Path]) -> None:
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
            if os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception:
            if os.path.isfile(file_path):
                shutil.rmtree(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)

    # Create temporary file
    tmp_file_path = Path("tmp_file")
    tmp_file_path.touch()


# Generated at 2022-06-14 08:13:28.827229
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    from os import environ as os_environ
    import tempfile

    # A) testing values to try
    true_values = [
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
    ]
    false_values = [
        "n",
        "no",
        "f",
        "false",
        "off",
        "disable",
        "disabled",
        "0",
    ]

    # B) testing environment variables

# Generated at 2022-06-14 08:13:36.155560
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import os
    from os import environ as os_environ
    from tempfile import TemporaryDirectory
    from textwrap import dedent

    from sanic.log import error, logger

    # Create temporary directory.
    with TemporaryDirectory() as tmp_path:
        tmp_path = Path(tmp_path)

        # Create configuration file with empty content.
        config_file_name = "config.py"
        config_file = tmp_path / config_file_name
        config_file.touch()

        # Create configuration file for env vars with content:
        #   TEST = True
        #   TEST_STR = "some string"
        #   TEST_INT = 123
        env_vars_file_name = "config_env_vars.py"
        env_vars_file = tmp_path / env_vars_file

# Generated at 2022-06-14 08:13:54.363321
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Unit test for load_module_from_file_location function."""

    # Usecase 1:
    # Check if function works ok with location provided as a Path object.
    # Mark that this location contains an environment variable
    # in format ${some_env_var}.
    fake_some_env_var = "some_env_var"
    fake_location = Path("/some/path/${some_env_var}")
    fake_module_name = "module_name"
    fake_module = types.ModuleType(fake_module_name)
    fake_module.__file__ = str(fake_location)
    fake_spec = spec_from_file_location(
        fake_module_name, str(fake_location), is_package=False
    )

# Generated at 2022-06-14 08:14:05.073240
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from io import StringIO
    import sys
    from tempfile import NamedTemporaryFile

    path = "some/path/${some_env_var}"
    assert load_module_from_file_location(
        location="${some_env_var}",
    ) == path

    assert load_module_from_file_location(
        location="./file.py",
    ).__file__ == "./file.py"

    # A) Check if it raises correct exception
    #    If location contains environment variables which are
    #    not defined.
    not_defined_var = "not_defined_var"
    with pytest.raises(LoadFileException) as excinfo:
        load_module_from_file_location(
            location="${not_defined_var}",
        )


# Generated at 2022-06-14 08:14:17.941292
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    file_location = Path.cwd() / "tests" / "test_config_file.py"

    # A) Run like: python -m pytest tests/test_load_module_from_file_location.py
    #    to check that config file is loaded
    module = load_module_from_file_location(file_location)
    assert module.TEST_VARIABLE == 3

    # B) Run like: python -m pytest
    #    to check that environment variable is loaded
    environment_variable = "TEST_VARIABLE"
    os_environ[environment_variable] = str(file_location)
    module = load_module_from_file_location(
        "${" + environment_variable + "}"
    )
    assert module.TEST_VARIABLE == 3



# Generated at 2022-06-14 08:14:25.617686
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # A) Test if it loads *.py files from full paths
    some_module = load_module_from_file_location(
        "some_module_name", "/some/path/to/some_module.py"
    )
    assert some_module.__name__ == "some_module_name"
    assert some_module.__file__ == "/some/path/to/some_module.py"

    # B) Test if it loads configuration files from full paths
    some_module = load_module_from_file_location(
        "some_module_name", "/some/path/to/configuration.some_file_extension"
    )
    assert some_module.__name__ == "config"
    assert some_module.__file__ == "/some/path/to/configuration.some_file_extension"



# Generated at 2022-06-14 08:14:31.198207
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    os_environ["SOME_ENV_VAR"] = "some_env_val"
    assert hasattr(
        load_module_from_file_location(
            "some_module_name", "/some/path/${some_env_var}"
        ),
        "some_module_name",
    )



# Generated at 2022-06-14 08:14:42.771752
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # pylint: disable=protected-access
    os_environ["some_env_var"] = "some_env_var_value"

    # Note: The following statements my seem wired but their purpose is
    # to test all available arguments of load_module_from_file_location
    # function in order to cover all code paths and raise all possible
    # exceptions in case of invalid input.

    # A) Test with file location with environment variable in format ${env_var}.
    # User provides location as string and file is a python module.

# Generated at 2022-06-14 08:14:44.605522
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    assert hasattr(
        load_module_from_file_location(
            os.path.join(os.path.dirname(__file__), "data/custom_loader.py")
        ),
        "__config_dict__",
    )

# Generated at 2022-06-14 08:14:51.616947
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # Test load_module_from_file_location for Path type
    config = load_module_from_file_location(
        Path(__file__).parent / "configs/test.py"
    )
    assert config.test == "ok"

    # Test load_module_from_file_location for string type
    config = load_module_from_file_location(
        str(Path(__file__).parent / "configs/test.py")
    )
    assert config.test == "ok"

    # Test load_module_from_file_location for bytes type
    # Also this test checks if path with bytes type is still
    # properly resolved.

# Generated at 2022-06-14 08:15:02.464712
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    os_environ["some_env_var"] = "some_path"

    assert load_module_from_file_location(
        "some_module_name", "/some/path/some_module.py"
    )
    assert load_module_from_file_location(
        "some_module_name",
        "/some/path/${some_env_var}/some_module.py",
    )
    with pytest.raises(LoadFileException):
        load_module_from_file_location(
            "some_module_name",
            "/some/path/${some_env_var_which_does_not_exist}/some_module.py",
        )



# Generated at 2022-06-14 08:15:10.294066
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import tempfile
    import os

    with tempfile.TemporaryDirectory() as tmpdirname:
        file_path = os.path.join(tmpdirname, "test.py")
        tmp_file = open(file_path, "w")
        tmp_file.write("GLOBAL_TEST_VARIABLE = 5")
        tmp_file.close()
        imported_module = load_module_from_file_location(file_path)

        assert imported_module.GLOBAL_TEST_VARIABLE == 5



# Generated at 2022-06-14 08:15:26.625645
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    # A) Check if file is read with encoding
    test_string = "test_string"
    test_string_bytes = test_string.encode("latin-1")
    assert (
        load_module_from_file_location(test_string_bytes, encoding="latin-1")
        == test_string
    )

    # B) Check if bytes are not decoded as utf-8
    test_string_bytes = test_string.encode("utf-8")
    assert (
        load_module_from_file_location(test_string_bytes, encoding="latin-1")
        != test_string
    )

    # C) Check if environment variable is resolved
    os_environ["test_env_var"] = test_string

# Generated at 2022-06-14 08:15:40.396638
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import sys
    from os import environ
    from pathlib import Path
    from tempfile import NamedTemporaryFile

    # 1.
    # A) Write content to a temp file.
    with NamedTemporaryFile(mode="w", dir=None, delete=False) as f:
        f.file.write("name = 'some_name'")

    # B) Load module from file using function.
    mod = load_module_from_file_location(f.name)

    # C) Make assertions.
    assert mod.name == "some_name"

    # 2.
    # A) Use temp dir.
    temp_dir = Path(f.name).parent

    # B) Copy the content of the file into this dir.
    filename = temp_dir / "some_name.py"

# Generated at 2022-06-14 08:15:49.238701
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    # A) Check if some file is able to be loaded as module.
    #    If not, raise an exception.
    from . import test_module
    assert load_module_from_file_location(
        __file__.replace("utils.py", "test_module.py")
    ) == test_module

    # B) The function must throw an exception if given
    #    env_var is not defined in an environment.

# Generated at 2022-06-14 08:16:02.420852
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import os

    # A) Check if location contains any environment variables
    #    in format ${some_env_var}.
    os.environ["some_env_var"] = "some/path"
    os.environ["some_other_env_var"] = "some/other/path"

    # 1. We can provide path to a file as a string.
    try:
        import_string(
            f"${os.environ['some_env_var']}/config.py"
        )  # Should raise LoadFileException.
    except LoadFileException:
        pass
    else:
        raise Exception(
            "Should raises a LoadFileException when environment "
            "variable is not set."
        )
    # Reset environment variable.
    os.environ.pop("some_env_var")

    # 2. We

# Generated at 2022-06-14 08:16:15.909620
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    assert load_module_from_file_location("os").__name__ == "os"

    with open("file_without_extension", "w") as f:
        f.write("variable = 5")

    module = load_module_from_file_location("file_without_extension")
    assert module.__file__ == "file_without_extension"
    assert module.variable == 5

    with open("file_with_extension.py", "w") as f:
        f.write("variable = 5")

    module = load_module_from_file_location("file_with_extension.py")
    assert module.variable == 5

    with open("file_with_extension_in_path.py", "w") as f:
        f.write("variable = 5")

    module = load_module_from

# Generated at 2022-06-14 08:16:26.851431
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # 1.1 Well-behaviour
    # 1.1.1 When location is Path object
    from sanic.server import HttpProtocol  # noqa: F401; pylint: disable=import-outside-toplevel

    load_module_from_file_location(
        location=Path(__file__),
        target="http_protocol_test",
    )
    assert HttpProtocol.http_protocol_test

    # 1.1.2 When location is str object and has no any environment variables
    load_module_from_file_location(
        location=__file__,
        target="http_protocol_test",
    )
    assert HttpProtocol.http_protocol_test

    # 1.1.3 When location is str object and has environment variables
    #       - Environment variables are set


# Generated at 2022-06-14 08:16:31.155936
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    os_environ["SOME_ENV_VAR"] = "some_env_var"
    try:
        module = load_module_from_file_location(
            "/some/path/${SOME_ENV_VAR}/some.py"
        )
        assert module.__name__ == "some"
    finally:
        del os_environ["SOME_ENV_VAR"]

# Generated at 2022-06-14 08:16:41.893944
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # A) We want to be sure than exceptions are raised
    #    if env vars are incorrectly used.
    # 1) Define environment variable.
    TEST_ENV = "TEST_ENV"
    TEST_ENV_VALUE = "TEST_ENV_VALUE"
    os_environ[TEST_ENV] = TEST_ENV_VALUE

    # 2) Create file with environment variables defined in it.
    with open("sanic_settings.py", "w") as f:
        f.write(f'TEST_ENV_RESOLVED = "${{{TEST_ENV}}}"')

    # 3) Load it, to test if variables are correctly resolved.
    env_resolv1 = load_module_from_file_location("sanic_settings.py")

    # 4) See if Test

# Generated at 2022-06-14 08:16:50.673873
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    os.environ["__TEST_CONFIG_ENV_VAR_FIVE"] = "five"
    os.environ["__TEST_CONFIG_ENV_VAR_SIX"] = "six"

    # Does nothing
    load_module_from_file_location("./config.py", "ascii")

    # Does nothing
    load_module_from_file_location("./config.py", "utf8")

    # Does nothing
    load_module_from_file_location("./config.py", "utf-8")

    # Does nothing
    load_module_from_file_location(b"./config.py", "utf8")

    # Does nothing
    load_module_from_file_location(b"./config.py", "utf-8")

    # Does nothing


# Generated at 2022-06-14 08:17:02.625696
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    # A) Check if environment variables in location parameter are correctly
    #    resolved.
    path_to_some_file = os.path.dirname(os.path.abspath(__file__))
    env_var_name = "SOME_ENV_VAR"
    some_env_var = "some_env_var_value"
    # A.1) Check that module is loaded if environment variable is passed.
    os.environ[env_var_name] = some_env_var
    some_module = load_module_from_file_location(
        "some_module_name",
        os.path.join(path_to_some_file, "${" + env_var_name + "}"),
    )
    assert some_module.some_var == "some_value"
    #

# Generated at 2022-06-14 08:17:18.752966
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    # A) Check "some_module" is loaded from the file path provided.
    os_environ["TEST_ENV"] = "test"
    some_module = load_module_from_file_location(
        # B) Check environment variables like ${TEST_ENV} in the path
        #    are resolved.
        "some_module_name",
        "/some/path/${TEST_ENV}",
    )
    assert some_module.__name__ == "some_module_name"
    assert some_module.__file__ == "/some/path/test"
    assert some_module.file_path == "/some/path/test"
    del os_environ["TEST_ENV"]

# Generated at 2022-06-14 08:17:28.054070
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Test function load_module_from_file_location"""

    # A) Check if location contains any environment variables
    #    in format ${some_env_var}.
    os_environ["some_env_var"] = "some/path"
    location = "some/path/${some_env_var}"
    env_vars_in_location = set(re_findall(r"\${(.+?)}", location))

    # B) Check these variables exists in environment.
    not_defined_env_vars = env_vars_in_location.difference(os_environ.keys())

    assert not not_defined_env_vars

    # C) Substitute them in location.

# Generated at 2022-06-14 08:17:39.821493
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from sanic import Sanic
    from sanic.config import Config

    app = Sanic()
    app.config = Config()

    config_location = Path(__file__).parent.joinpath(
        "config", "test_load_module_from_file_location.py"
    )
    config = load_module_from_file_location(config_location)

    assert (
        config.TEST_TEST_LOAD_MODULE_FROM_FILE_LOCATION_TEST_CONFIG_VARIABLE
        is True
    )

    config_location = Path(__file__).parent.joinpath(
        "config", "test_load_module_from_file_location"
    )
    config = load_module_from_file_location(config_location)


# Generated at 2022-06-14 08:17:52.109160
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import os
    import tempfile

    abs_path = tempfile.mkdtemp()


# Generated at 2022-06-14 08:18:05.987371
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa

    import pytest

    # Testing parameter location is of a string or bytes type.

    with pytest.raises(
        TypeError,
        match="load_module_from_file_location() argument 1 must be of a str or bytes type",
    ):
        load_module_from_file_location(123, "/some/path/${some_env_var}")

    # Testing environment variables
    # in format ${some_env_var}.

    # A) location contains environment variables
    #    in format ${some_env_var}, but some of them is not defined.

    os_environ["some_env_var"] = "/some/path"
    os_environ["some_env_var_not_defined"] = "/some/path/not/defined"


# Generated at 2022-06-14 08:18:06.713765
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    pass

# Generated at 2022-06-14 08:18:16.819169
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from tests.test_helper import config, is_module

    assert is_module(
        config, load_module_from_file_location("./tests/test_config.py")
    )

    assert is_module(
        config,
        load_module_from_file_location("./tests/test_config", "utf8"),
    )

    assert is_module(
        config,
        load_module_from_file_location("./tests/test_config.py", "utf8"),
    )

    assert is_module(
        config,
        load_module_from_file_location("./tests/test_config.py", "utf8", "True"),
    )
