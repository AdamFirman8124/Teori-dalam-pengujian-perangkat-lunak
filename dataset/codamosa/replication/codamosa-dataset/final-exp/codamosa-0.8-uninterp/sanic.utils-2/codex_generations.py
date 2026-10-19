

# Generated at 2022-06-14 08:08:27.470841
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    path = Path(__file__).parent # /home/username/anaconda3/lib/python3.8/site-packages/sanic
    config_filepath = path.joinpath("config_helpers.py")
    # config_filepath = "/home/username/anaconda3/lib/python3.8/site-packages/sanic/config_helpers.py"
    print(config_filepath)
    module = load_module_from_file_location(config_filepath)
    print(module.__spec__.origin)
    #print(module)

if __name__ == '__main__':
    test_load_module_from_file_location()

# Generated at 2022-06-14 08:08:39.963933
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    import inspect

    import nose.tools as nt

    # Check if it raises LoadFileException when
    # environment variable does not exist.
    path = "some_path/${some_env_var}"
    nt.assert_raises(
        LoadFileException, load_module_from_file_location, path
    )

    # Check if it loads from environment variable.
    os_environ["some_env_var"] = "some_path"
    nt.eq_(
        inspect.getfile(
            load_module_from_file_location(path)
        ),
        "some_path",
    )

    # Check if it uses module name when you give
    # path as argument to load_module_from_file_location.

# Generated at 2022-06-14 08:08:52.251513
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import os

    os.environ["some_env_var"] = "/some/env/variable"

    path_to_mod = "testing_module"
    try:
        os.remove(f"{path_to_mod}.py")
    except Exception:
        pass
    with open(f"{path_to_mod}.py", "w") as file_handler:
        file_handler.write("SOME_VAR = 0")
    module = load_module_from_file_location(path_to_mod)
    assert module.SOME_VAR == 0
    print("Unit test for load_module_from_file_location passed.")
    os.remove(f"{path_to_mod}.py")
    try:
        os.remove("some_env_var")
    except Exception:
        pass




# Generated at 2022-06-14 08:09:05.482405
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    os_environ["SANIC_LOAD_MODULE_TEST"] = "ok"
    module = load_module_from_file_location(
        "tests/test_application/test_config.py"
    )
    assert module.TEST_VAR == "ok"

    module = load_module_from_file_location(
        "tests/test_application/test_config.py",
        location=Path("tests/test_application/test_config.py"),
    )
    assert module.TEST_VAR == "ok"

    module = load_module_from_file_location(
        "tests/test_application/test_config.json"
    )
    assert module.TEST_VAR == "ok"


# Generated at 2022-06-14 08:09:11.369311
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # pylint: disable=protected-access
    from sanic.config import Config

    # Assume we have following variables defined in os.environ:
    os_environ["SOME_ENV_VAR"] = "some_env"

    # A) Using only environment variables.
    module = load_module_from_file_location(
        "sanic.config", "${SOME_ENV_VAR}/sanic/config.py"
    )
    assert module.__class__ == Config
    del os_environ["SOME_ENV_VAR"]

    # B) Using hardcoded path.
    module = load_module_from_file_location(
        "sanic.config", "./sanic/config.py"
    )
    assert module.__class__ == Config

# Generated at 2022-06-14 08:09:23.109409
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    dir_path = Path(__file__).parent / "dir"

    # Test exceptions
    with pytest.raises(LoadFileException):
        load_module_from_file_location(
            (dir_path / "some_module.py").as_posix(),
            "/some/path/${some_env_var}"
        )

    with pytest.raises(PyFileError):
        load_module_from_file_location(
            (dir_path / "invalid_some_module.py").as_posix()
        )

    # Test module loading
    module = load_module_from_file_location(
        (dir_path / "some_module.py").as_posix()
    )
    assert module.print_foo() == "Foo"

# Generated at 2022-06-14 08:09:32.691621
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    PATH = os.path.abspath(os.path.dirname(__file__))
    mod_simple = load_module_from_file_location(PATH + "/fixtures/simple_module.py")
    assert mod_simple.__name__ == "simple_module"
    assert mod_simple.simple_attribute == 42
    mod_package = load_module_from_file_location(PATH + "/fixtures/package/__init__.py")
    assert mod_package.__name__ == "package"
    assert mod_package.simple_attribute == 42
    mod_pkg_config = load_module_from_file_location(PATH + "/fixtures/package/config.py")
    assert mod_pkg_config.__name__ == "config"
    assert mod_pkg_config.simple_attribute == 42
    mod_simple

# Generated at 2022-06-14 08:09:42.041770
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Testing function load_module_from_file_location."""

    # Test 1. Checking if it raises LoadFileException when
    #         some ${some_env_var} is not set.
    os_environ["TEST_ENV_VAR_1"] = "test_env_var_1_value"

    try:
        load_module_from_file_location(
            "/tmp/some_file.txt",
            some_env_var="${TEST_ENV_VAR_1}",
            some_other_env_var="${TEST_ENV_VAR_2}",
        )
    except LoadFileException:
        pass

# Generated at 2022-06-14 08:09:53.155201
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    from os import environ as os_environ
    from os import remove as os_remove
    from os import path as os_path
    from tempfile import NamedTemporaryFile
    from configparser import ConfigParser
    from shutil import move as shutil_move

    # This code is needed for tests scenarios where
    # we use environment variables and it needs to be
    # set before we start creating tests.
    os_environ["TEST_ENV_VAR"] = "/tmp/test"
    os_environ["TEST_ENV_VAR_2"] = "/tmp/test"
    os_environ["TEST_ENV_VAR_3"] = "/tmp/test"

    # Some tests is going to use this file.

# Generated at 2022-06-14 08:10:02.290829
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # 1) File without environment variables
    conf_file_name = "config.py"
    conf_location = "tests/settings/" + conf_file_name
    _mod_spec = spec_from_file_location(conf_file_name, conf_location)
    module = module_from_spec(_mod_spec)
    _mod_spec.loader.exec_module(module)  # type: ignore

    assert module.DEBUG is False
    assert module.SECRET is None
    assert module.TESTING is False
    assert module.SETTINGS_LIST == ["test"]

    # 2) File with environment variables in path
    conf_file_name = "config_env_vars.py"
    conf_location = "${TEST_DIR}/${TEST_NAME}"
    os_environ["TEST_DIR"]

# Generated at 2022-06-14 08:10:17.134536
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    """
    This unit test has following steps:
    1) Create configuration file using tempfile.
    2) Check we can read configuration from file.
    3) Check we can read configuration from file in parent directory.
    4) Check we can read configuration from file in nested directory.
    5) Check we can read configuration from file using environment variables.
    6) Check we can read configuration from file from nested directory
       using environment variables in a path.
    7) Check that we can not read configuration from file
       using environment variables which are not set.
    8) Check that all of the above throws expected Exception.
    """

    import tempfile

    # 1) Check we can read configuration from file
    with tempfile.NamedTemporaryFile() as temp:
        temp.write(b"some_variable='some_value'")

# Generated at 2022-06-14 08:10:27.305799
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from os import environ
    from pathlib import Path

    # Positive

    # A) Loading module with local file
    #    (file name without .py extension)
    test_module_without_py_extension = load_module_from_file_location(
        "test_module_without_py_extension"
    )

    assert test_module_without_py_extension.__name__ == "test_module_without_py_extension"
    assert test_module_without_py_extension.KEYWORD == "value"

    # B) Loading module with local file
    #    (file name with .py extension)
    test_module_with_py_extension = load_module_from_file_location(
        "test_module_with_py_extension.py"
    )

    assert test_

# Generated at 2022-06-14 08:10:40.342307
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import os
    import sys
    import tempfile
    
    # We will use temporary file in a temporary directory
    # to emulate configuration file.
    # For that we create a temporary file and directory
    tfile = None
    tdir = None

# Generated at 2022-06-14 08:10:53.030510
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from os import path, system
    from inspect import isfunction

    my_conf = load_module_from_file_location(
        path.abspath(path.join(path.dirname(__file__), "my_conf.py"))
    )
    assert isfunction(my_conf.my_function)
    assert my_conf.my_function() == "my_function"

    my_conf = load_module_from_file_location(
        path.abspath(path.join(path.dirname(__file__), "my_conf.py")) + "c"
    )
    assert isfunction(my_conf.my_function)
    assert my_conf.my_function() == "my_function"

    # Test with environment variables,
    # to reduce noise, create temporary environment
    # variables in the testing

# Generated at 2022-06-14 08:11:05.039387
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    # --- Testing environment variable parsing
    # A) Json parsing
    os_environ["env_A"] = '"some data"'
    os_environ["env_B"] = "some_data"
    os_environ["env_C"] = "false"
    os_environ["env_D"] = "true"

    # B) Test that different environment variables are parsed correctly
    assert (
        load_module_from_file_location(
            "./test_load_module_from_file_location_test_data/test_case_B"
        ).__dict__
        == os_environ
    )

    # C) Test that environment variables are parsed correctly
    #    in location parameter which is of string type.

# Generated at 2022-06-14 08:11:17.476831
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    from sanic.config import TEST_LOAD_MODULE

    assert load_module_from_file_location(__file__).__name__ == "sanic.config"

    assert load_module_from_file_location(
        TEST_LOAD_MODULE, encoding="ascii"
    ).__name__ == "test_config"

    assert load_module_from_file_location(Path(TEST_LOAD_MODULE)).__name__ == (
        "test_config"
    )

    assert load_module_from_file_location(Path(__file__)).__name__ == "sanic.config"

    assert load_module_from_file_location(__package__).__name__ == "sanic"

# Generated at 2022-06-14 08:11:30.958828
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    def function_with_docstring():
        """ This is a docstring for function_with_docstring """
        return True

    class ClassWithDocstring:
        """ This is a docstring for ClassWithDocstring"""

    class_with_docstring = ClassWithDocstring()

    module_name = "unit_test_load_module_from_file_location"
    module_path = str(Path(__file__).parent / module_name)
    os.system(f"touch {module_path}.py")

    config = load_module_from_file_location(f"{module_path}.py")

    assert config.__name__ == module_name
    assert config.__file__ == f"{module_path}.py"
    assert config.__doc__ is None

    # Add a docstring to to module

# Generated at 2022-06-14 08:11:35.309747
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    with pytest.raises(ValueError):
        load_module_from_file_location('some_module_name', 'some/path')


# Generated at 2022-06-14 08:11:47.424254
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Tests load_module_from_file_location function."""

    # No fail pass
    load_module_from_file_location(__file__, globals=globals())

    # Fail with IOError
    with pytest.raises(IOError):
        load_module_from_file_location("non_existing_location")

    # Fail with PyFileError
    with pytest.raises(PyFileError):
        load_module_from_file_location(
            __file__, globals=globals()
        ).raise_example_py_file_error()

    # Check if it can handle location with environ variables
    some_env_var = "some_env_var_value"
    os_environ["some_env_var"] = some_env_var

# Generated at 2022-06-14 08:12:01.078940
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    from io import StringIO
    import sys
    import tempfile

    # A. Testing with corect parameters
    # A.1. With "location" as bytes.
    # A.1.1. And with additional arguments.
    path_to_temp_file = Path(
        tempfile.mkstemp(
            suffix=".py",
            prefix="load_module_from_file_location_test_",
            text=True,
            dir=os.getcwd(),
        )[1]
    )
    with open(path_to_temp_file, "w") as f:
        f.write("a=1\nb=2\n")

    # A.1.1.1. Without environment variables in location.

# Generated at 2022-06-14 08:12:17.786369
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # Case 1:
    # ---------
    # Try to load some module from file on disk.
    # It should raise in case of some error,
    # and load module if everything is OK.
    try:
        module = load_module_from_file_location(
            "sanic/exceptions.py", location="/abcdef"
        )
    except LoadFileException as e:
        assert e.args[0] == "Unable to load configuration file (e.strerror)"
    except Exception:
        raise
    else:
        raise Exception(
            "Case 1: load_module_from_file_location "
            "should raise LoadFileException in case of IOError."
        )


# Generated at 2022-06-14 08:12:24.069318
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import tempfile

    name = "config"
    a = "1"

    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as fp:
        fp.write(f"{name} = {a}")

    module = load_module_from_file_location(fp.name, name)

    assert hasattr(module, name)
    assert getattr(module, name) == a

    try:
        load_module_from_file_location(fp.name, "${invalid_env_var}")
    except LoadFileException as exc:
        assert "environment variables are not set: invalid_env_var" in exc.args[0]

    os_environ["valid_env_var"] = name

# Generated at 2022-06-14 08:12:36.462836
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    os_environ["SOME_ENV_VAR"] = "some_value"

    try:
        module = load_module_from_file_location(
            "some_module_name", "${SOME_ENV_VAR}"
        )
        assert (
            module.__name__ == "some_module_name"
        ), "module.__name__ is not the same as requested"
        assert (
            module.__file__.endswith("some_value")
        ), "module.__file__ does not contain requested value"
    finally:
        del os_environ["SOME_ENV_VAR"]


# Generated at 2022-06-14 08:12:47.413749
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import os

    from sanic.config import Config
    from sanic.exceptions import LiveReloadException

    try:
        config = Config.from_pyfile("config_test.py")
    except LiveReloadException:
        pass
    else:
        assert config.TESTING
        assert config.TESTING_WITH_DEFAULT
        assert config.TESTING_WITH_HELP
        assert config.TESTING_MULTIPLE
        assert config.TESTING_INT
        assert config.TESTING_BOOL
        assert config.TESTING_DICT

    os.environ["TESTING_BOOL"] = "Y"
    try:
        config = Config.from_envvar("TEST_CONFIG")
    except LiveReloadException:
        pass

# Generated at 2022-06-14 08:12:58.686265
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import tempfile
    import pytest
    with tempfile.NamedTemporaryFile("w", delete=False) as f:
        f.write("data = 1")

    assert load_module_from_file_location(f.name).data == 1
    os.unlink(f.name)

    with tempfile.TemporaryDirectory() as dname:
        full_path = os.path.join(dname, "data.py")
        with open(full_path, "w") as f:
            f.write("data = 2")

        assert load_module_from_file_location(full_path).data == 2

        full_path = os.path.join(dname, "d", "data.py")
        os.makedirs(os.path.dirname(full_path))

# Generated at 2022-06-14 08:13:08.984300
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from random import choice
    from string import ascii_letters

    import tempfile

    from os import environ

    # A.1) Should be able to load Python file.
    tmp_dir = tempfile.mkdtemp()
    tmp_config_file_name = "".join(choice(ascii_letters) for _ in range(10))
    tmp_config_file = f"{tmp_dir}/{tmp_config_file_name}.py"

# Generated at 2022-06-14 08:13:20.477297
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import os
    import sys
    import tempfile
    from os import environ as os_environ
    from shutil import rmtree
    from io import BytesIO

    # A) Test empty location
    try:
        module = load_module_from_file_location("")
        raise AssertionError("load_module_from_file_location() should raise ValueError for empty location")
    except ValueError:
        pass

    # B) Test .py files
    with tempfile.TemporaryDirectory() as tmpdirname:
        config_file_name = f"{tmpdirname}/config.py"
        with open(config_file_name, "w+") as config_file:
            config_file.write("true_var = True")

# Generated at 2022-06-14 08:13:32.374644
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from tempfile import NamedTemporaryFile

    tmp_file = NamedTemporaryFile(delete=False)
    tmp_file.write(b"A = 10\nB = 'hello'")
    tmp_file.seek(0)
    # Test load file
    module = load_module_from_file_location(tmp_file.name)
    assert module.A == 10
    assert module.B == "hello"
    tmp_file.close()

    # Test load file with path
    tmp_file = NamedTemporaryFile()
    tmp_file.write(b"A = 10\nB = 'hello'")
    tmp_file.seek(0)
    module = load_module_from_file_location(
        tmp_file.name, path=[Path(tmp_file.name).absolute().parent]
    )
    tmp

# Generated at 2022-06-14 08:13:45.093411
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # touch some_file_location.py
    some_file_location = Path(__file__).parent / "some_file_location.py"
    some_file_location.touch()
    with open(some_file_location, "w") as f:
        # some_function is used in load_module_from_file_location.py
        f.write("def some_function(): pass")

    # touch some_file_location2.py and add some var
    some_file_location2 = Path(__file__).parent / "some_file_location2.py"
    some_file_location2.touch()
    with open(some_file_location2, "w") as f:
        f.write("SOME_VAR = 'some_value'")

    # set some_env_var in environment
    os

# Generated at 2022-06-14 08:13:56.277752
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from os import environ
    from os.path import isfile
    from tempfile import NamedTemporaryFile

    from sanic.helpers import load_module_from_file_location

    with NamedTemporaryFile('w+', suffix='.py') as f:
        # Write config to temporary file and close it.
        f.write(
            'SERVER_NAME = "localhost:8000"'
            '\nSANIC_TEST_CONFIG_LOADED = True'
        )
        f.seek(0)

        res = load_module_from_file_location(
            f.name
        )

    assert hasattr(res, 'SERVER_NAME')
    assert getattr(res, 'SERVER_NAME') == "localhost:8000"

    # Expect SANIC_TEST_CONFIG_LOADED to be True
   

# Generated at 2022-06-14 08:14:13.076210
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # I. no environment variables
    location = "/some/path/../some/file_name.py"
    module = load_module_from_file_location(location)
    assert module.__name__ == "file_name"
    assert module.__file__ == "/some/path/../some/file_name.py"

    # II. environment variables
    os_environ["SANIC_CONFIG_ENV_VARIABLE"] = "value"
    location = "/some/path/${SANIC_CONFIG_ENV_VARIABLE}/../some/file_name.py"
    module = load_module_from_file_location(location)
    assert module.__name__ == "file_name"
    assert module.__file__ == "/some/path/value/../some/file_name.py"

# Generated at 2022-06-14 08:14:25.525453
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """
    This test creates file "test_config.py" in the current directory.
    Then it tries to:
    1. Load this file with function load_module_from_file_location
    2. Assert that the loaded module contains attribute 'a'.
    3. Assert that this attribute is equal to 100.
    4. Remove created file test_config.py
    """
    import tempfile

    # A) Create file "test_config.py" in the current directory
    F = tempfile.NamedTemporaryFile(
        delete=False,
        mode="w+",
        encoding="utf8",
        suffix=".py",
        prefix="test_load_module_from_file_location_",
    )
    test_name = F.name
    F.write("a = 100")
    F.close()
   

# Generated at 2022-06-14 08:14:27.725672
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    assert type(load_module_from_file_location(__file__)) == types.ModuleType

# Generated at 2022-06-14 08:14:37.681474
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    if os.path.exists("/tmp/test_load_module_from_file_location"):
        shutil.rmtree("/tmp/test_load_module_from_file_location")
    os.makedirs("/tmp/test_load_module_from_file_location/sanic/")
    os.makedirs("/tmp/test_load_module_from_file_location/sanic2/")

    os.environ["TEST_ENV_VAR"] = "/tmp/test_load_module_from_file_location/"

    # test for pathlib.Path

# Generated at 2022-06-14 08:14:48.389645
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import os

    os.environ[
        "SANIC_TEST_ENV_VAR"
    ] = "test this and that"  # Create enviroment variable
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # A) Try to get test module
    module = load_module_from_file_location(
        f"./{os.path.basename(__file__)}", current_dir
    )
    assert module.__name__ == "test_utils"

    # B) Try to load module from absolute path
    module_b = load_module_from_file_location(f"{current_dir}/test_utils.py")
    assert module_b.__name__ == "test_utils"

    # C) Try to load module from relative

# Generated at 2022-06-14 08:14:55.015604
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    import tempfile
    import random
    import tempfile
    import os
    import shutil

    def create_temp_dir() -> str:
        """Creates temp directory and returns its path."""
        return tempfile.mkdtemp()

    def create_temp_file() -> str:
        """Creates temp file and returns its path."""
        return tempfile.NamedTemporaryFile(delete=False).name

    def create_empty_module(location: str) -> None:
        """Creates empty module at location."""
        with open(location, "w") as f:
            f.write("")

    def create_module_with_assignment(location: str, assignment: str) -> None:
        with open(location, "w") as f:
            f.write(assignment)


# Generated at 2022-06-14 08:15:07.922602
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    test_module_path = Path(__file__).parent / "test_config_file"
    test_module = load_module_from_file_location(test_module_path)

    assert test_module.TEST_CONSTANT == 1
    assert test_module.TEST_CONSTANT1 == 1
    assert test_module.TEST_CONSTANT2 == 1
    assert test_module.TEST_CONSTANT3 == 1
    assert test_module.TEST_CONSTANT4 == 1
    assert test_module.TEST_CONSTANT5 == 1

    test_module_path = Path(__file__).parent / "test_config_file"

# Generated at 2022-06-14 08:15:18.645654
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa

    location = Path(__file__)
    assert location.is_file()
    module = load_module_from_file_location(location)
    assert module is not None
    assert hasattr(module, "str_to_bool")
    assert str_to_bool("y") is True
    assert str_to_bool("n") is False
    assert str_to_bool("0") is False
    assert str_to_bool("1") is True
    assert str_to_bool("x") is False

    location = "${HOME}/some_file.py"
    module = load_module_from_file_location(location)

    assert module is None

# Generated at 2022-06-14 08:15:27.777471
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    from os import path as os_path
    from tempfile import TemporaryDirectory
    from shutil import copy

    # Create temporary directory and add it to environment.
    with TemporaryDirectory(prefix="sanic_test") as tmp_dir:
        os_environ["SANIC_TEST_TEMP_DIR"] = tmp_dir
        os_environ["SANIC_TEST_TEMP_DIR_FOO"] = tmp_dir + "/foo"

        # Create temp file in directory.
        temp_file = tmp_dir + "/test.py"
        with open(temp_file, "w") as f:
            f.write("a = 1\n")
        # Load module from this temp file.
        module = load_module_from_file_location(temp_file)
        assert module.a == 1

        #

# Generated at 2022-06-14 08:15:41.072441
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    module = load_module_from_file_location(
        "tests/conf_for_testing.py", "/py_path"
    )
    config = module.config
    assert config["TEST_CONFIG"] == "1234567890"

    module = load_module_from_file_location(
        "tests/conf_for_testing.py", b"/py_path_bytes", encoding="utf-8"
    )
    config = module.config
    assert config["TEST_CONFIG"] == "1234567890"

    # Check that environment variable is properly resolved.
    some_env_var_value = os.urandom(10).hex()
    os.environ["SOME_ENV_VAR"] = some_env_var_value

# Generated at 2022-06-14 08:15:59.228278
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    module = load_module_from_file_location(
        "tests/settings.py"
    )
    assert module.TEST_VAR_FROM_FILE == "TEST_VALUE"

    module = load_module_from_file_location(
        Path(__file__).parent / "settings.py"
    )
    # Check that we can still import it by pathlib.Path
    assert module.TEST_VAR_FROM_FILE == "TEST_VALUE"

    module = load_module_from_file_location(
        "tests/settings.py",
        Path(__file__).parent / "config",
    )
    # Check that we can still import it by pathlib.Path
    assert module.TEST_VAR_FROM_FILE == "TEST_VALUE"

    module

# Generated at 2022-06-14 08:16:03.469481
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    assert load_module_from_file_location(
        "sanic.exceptions", "./sanic/exceptions.py"
    ).SanicException is pytest.approx(LoadFileException)
#



# Generated at 2022-06-14 08:16:09.950470
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    assert load_module_from_file_location("os").name == "os"

    assert (
        load_module_from_file_location(__file__).__name__
        == __name__.split(".")[-1]
    )

    os_environ["SOME_ENV_VAR"] = "some_env_value"

    assert (
        load_module_from_file_location("/${SOME_ENV_VAR}/test_config.py").key
        == "value"
    )
    del os_environ["SOME_ENV_VAR"]


# Generated at 2022-06-14 08:16:20.696357
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from tempfile import TemporaryDirectory
    from os import path
    from os import mkdir
    from os import environ
    from os import chmod
    from os import devnull
    from os import fdopen
    import shutil
    import stat

    with TemporaryDirectory() as tmp_dir:
        # Testing with executing file
        config_file = "tmp_conf.py"
        config_file_path = path.join(tmp_dir, config_file)
        with open(config_file_path, "w") as file:
            file.write("CONF_KEY = 10")
        chmod(config_file_path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
        config = load_module_from_file_location(config_file_path)
       

# Generated at 2022-06-14 08:16:30.897923
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from pathlib import Path
    from tempfile import NamedTemporaryFile

    from sanic.utils import test_load_module_from_file_location

    file = """
name = "TEST"
"""

    # Create a temporary file in the file system
    with NamedTemporaryFile("w") as temp_file:
        temp_file.write(file)
        temp_file.flush()

        # Try to load config file
        module = test_load_module_from_file_location(temp_file.name)
        assert module.name == "TEST"

    # --------------------------------------------------------------------------

    # Create a temporary file as a Path in the file system
    with NamedTemporaryFile("w") as temp_file:
        temp_file.write(file)
        temp_file.flush()

        # Try to load config file
        module = test

# Generated at 2022-06-14 08:16:34.109597
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    module = load_module_from_file_location(
        "tests.configs.sample_file.py"
    )
    assert module.ONE == 1
    assert module.foo == "bar"

# Generated at 2022-06-14 08:16:47.395538
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import tempfile
    import os

    # 0. Cleanup, delete temporary folder
    temp_path = tempfile.TemporaryDirectory()
    print("Temporary folder have been created: " + temp_path.name)

    # 1. Save test configuration to temporary folder.
    test_conf = """
    TEST_CONF = {
        "test": {
            "key1": "val1",
            "key2": 42
        }
    }
     """
    test_conf_file_name = "test_conf.py"
    test_conf_full_path = temp_path.name + "/" + test_conf_file_name
    file = open(test_conf_full_path, "w")
    file.write(test_conf)
    file.close()

    # 2. Load test configuration from temporary folder.


# Generated at 2022-06-14 08:16:55.508687
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    import random  # nosec
    import string  # nosec
    import os  # nosec

    # 1) Create config files with random config value and
    #    random environment variable.
    random_config_value = "".join(
        random.choice(string.ascii_letters) for i in range(0, 5)
    )
    env_var = "".join(random.choice(string.ascii_letters) for i in range(0, 2))
    os.environ[env_var] = env_var

    config_file = "config.py"
    with open(config_file, "w") as conf:
        conf.write('config = "' + random_config_value + '"')

    env_config_file = "${%s}/config.py" % env_var

# Generated at 2022-06-14 08:17:09.149502
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    # A) Test that environment variables can be used in file path.

    # A1) Test str path.
    # A1.1) Create test config file with an import keyword.
    #       This will ensure that file will be imported as a module,
    #       not just evaled.
    test_config_file_path = "./delete_me_A1.1.py"
    test_config_file = open(test_config_file_path, "w")
    test_config_file.write("import math")
    test_config_file.close()
    # A1.2) Check that env. var. can be used in it's path.
    os_environ["TEST_ENV_VAR_A1_2"] = "."
    test_module = load_module_from_file_location

# Generated at 2022-06-14 08:17:20.693545
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    """Unit test for function load_module_from_file_location"""
    # A) Test load_module_from_file_location with environment variables
    mod_name = "test_some_module.py"
    os_environ["LOAD_MODULE_FROM_FILE_LOCATION_TEST_1"] = "./"
    module = load_module_from_file_location(
        mod_name,
        "${LOAD_MODULE_FROM_FILE_LOCATION_TEST_1}",
        "module_name_1",
    )
    assert module.name == "module_name_1"

    # B) Test load_module_from_file_location without environment variables
    mod_name = "test_some_module.py"

# Generated at 2022-06-14 08:17:40.154452
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    import os
    import pytest
    import tempfile

    some_var = "some_value"

    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_file_name = "some_file"
        tmp_file_path = os.path.join(tmp_dir, tmp_file_name)
        with open(tmp_file_path, "w") as tmp_file:
            tmp_file.write(
                f"""
                some_str_var = "some_str_value"
                some_int_var = 1234
                some_bool_var = True
                """
            )

        # Test if file is loaded from absolute path
        some_loaded_module = load_module_from_file_location(
            tmp_file_path, encoding="utf8"
        )


# Generated at 2022-06-14 08:17:52.230196
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    """I don't know how to write unit tests for this function,
    but here is a template for that.
    You can run this test manually:

    $ nosetests -s -v file_loader.py:test_load_module_from_file_location
    """
    # TODO: write unit tests
    from os import environ
    from os.path import dirname, join, abspath

    def show(module):
        print("\nmodule:", module, "\n", dir(module), "\n")
        print("vars: ", vars(module), "\n")

    # environ["TEST_CONFIG"] = "config.py"
    # CONFIG_PATH = join(abspath(dirname(__file__)), environ["TEST_CONFIG"])
    # CONFIG_PATH = join(

# Generated at 2022-06-14 08:18:06.090140
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import_string = load_module_from_file_location
    assert import_string("string") is str
    assert import_string("datetime") is datetime
    assert import_string("datetime.datetime") is datetime
    assert import_string("datetime.datetime") is datetime.datetime
    assert import_string("datetime.datetime.now") is datetime.datetime.now
    assert import_string("datetime.datetime.now()") is datetime.datetime.now()
    assert import_string("datetime.datetime.utcnow()") is datetime.datetime.utcnow()
    assert import_string("datetime.datetime.utcnow") is datetime.datetime.utcnow

    assert import_string("os") is os

# Generated at 2022-06-14 08:18:11.645354
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    assert (
        load_module_from_file_location("tests.unit.server.utils.mock_module").test == 123
    )

    assert (
        load_module_from_file_location("./tests/unit/server/utils/mock_module.py")
        .test
        == 123
    )

    assert (
        load_module_from_file_location("./tests/unit/server/utils/mock_module.py.no")
        .test
        == 123
    )

    assert (
        load_module_from_file_location(
            "./tests/unit/server/utils/mock_module.py.${test_load_module_from_file_location_env_var}",
            encoding="base64",
        )
        .test
        == 123
    )

