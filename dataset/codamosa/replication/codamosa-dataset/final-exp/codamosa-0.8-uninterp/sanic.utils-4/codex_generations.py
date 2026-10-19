

# Generated at 2022-06-14 08:08:27.507532
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    if __name__ == "__main__":
        from tempfile import TemporaryDirectory
        from os import environ

        TEMP_DIR = Path(TemporaryDirectory().name)
        CONFIG_PATH = TEMP_DIR / "config_test.py"

        with open(CONFIG_PATH, "w") as f:
            f.writelines(["TEST = 'test'"])

        config_module_1 = load_module_from_file_location(CONFIG_PATH)
        assert "TEST" in config_module_1.__dict__
        assert config_module_1.__name__ == "config_test"
        # clean up
        if CONFIG_PATH.exists():
            CONFIG_PATH.unlink()

        environ["TEST_ENV"] = "1"
        config_module_2

# Generated at 2022-06-14 08:08:40.012715
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # A) Check if function fails gracefully
    #    when environment variable is not set.
    try:
        load_module_from_file_location(
            "${UNDEFINED_ENVVAR}", "some", "args", "and", "kwargs"
        )
    except LoadFileException as e:
        assert "UNDEFINED_ENVVAR" in str(e)
    else:
        raise AssertionError("UNDEFINED_ENVVAR not found in exception")

    # B) Check if function properly
    #    resolves environment variables.

# Generated at 2022-06-14 08:08:52.252252
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    import os
    import tempfile

    # Test 0: simple load file
    actual = load_module_from_file_location(__file__)
    assert actual.__file__ == __file__

    # Test 1: simple load file with Path
    actual = load_module_from_file_location(Path(__file__))
    assert actual.__file__ == __file__

    # Test 2: simple load unicode file with bytes
    #         using utf-8 by default
    actual = load_module_from_file_location(
        Path(__file__).parent / "test_script_utf8_bom.py",
        encoding="utf-8",
    )
    assert actual.__name__ == "test_script_utf8_bom"
    assert hasattr(actual, "s")
   

# Generated at 2022-06-14 08:09:05.431769
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    import pytest

    # 0) Basic test
    os_environ["test_0"] = "test_0"
    module = load_module_from_file_location(
        "${test_0}",
        parent="/tmp",
        loader=None,
        target="test_0",
        submodule_search_locations=None,
        is_package=False,
        has_location=True,
    )
    assert module.__name__ == "test_0"
    assert module.__file__ == "/tmp/test_0"

    # 1) Basic test with Path parameter
    os_environ["test_1"] = "/tmp/test_1"

# Generated at 2022-06-14 08:09:12.334214
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # TODO: Add new unit tests
    # Existing tests needs to be refactored
    # to use separate location for tests
    # and to be more clear and readable.
    location = "tests/test_load_module_from_file_location.py"

    # module = load_module_from_file_location(location)
    module = load_module_from_file_location("asd")
    print("module:", module)

# Generated at 2022-06-14 08:09:21.871523
# Unit test for function load_module_from_file_location

# Generated at 2022-06-14 08:09:31.466224
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import_str = '__import__("load_module_from_file_location")'
    location = environ.get(
        "TEST_PATH",
        str(Path(__file__).resolve().parent / "test_config.py"),
    )  # type: ignore
    os_environ["TEST_PATH"] = location

    module = load_module_from_file_location(location)
    module2 = load_module_from_file_location(
        "$$$!" + import_str + ".test_config"
    )
    assert module.key == module2.key
    assert module.key2 == module2.key2

    module3 = load_module_from_file_location(
        "$$$!" + import_str + ".test_config"
    )
    assert module2.key == module

# Generated at 2022-06-14 08:09:41.461124
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Unit test for function load_module_from_file_location."""

    test_value_0 = load_module_from_file_location("/", "/")
    assert isinstance(test_value_0, types.ModuleType)
    assert test_value_0.__file__ == "/"

    assert str_to_bool("y") is True
    assert str_to_bool("yes") is True
    assert str_to_bool("yep") is True
    assert str_to_bool("yup") is True
    assert str_to_bool("t") is True
    assert str_to_bool("true") is True
    assert str_to_bool("on") is True
    assert str_to_bool("enable") is True
    assert str_to_bool("enabled") is True

# Generated at 2022-06-14 08:09:52.838923
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # A) Check if it returns normal module loaded
    #    with importlib.util.spec_from_file_location
    #    if given path does not contain any environment variables.
    some_normal_path = "/some/normal/path.py"
    module = load_module_from_file_location(some_normal_path)
    assert isinstance(
        module, types.ModuleType
    ), "Loaded module is not a module type"
    assert module.__file__ == some_normal_path, "__file__ property is wrong"

    # B) Check if it can load module from path containing
    #    environment variables in format ${some_env_var}.
    # B.1)
    #    Check if raises LoadFileException if there is a non-defined
    #    environment variable in path.

# Generated at 2022-06-14 08:10:02.153965
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    Path("/tmp/test.py").write_text(  # nosec
        'SANIC_1 = 1\nSANIC_2 = "2"\nSANIC_3 = ["3", "32"]'
    )

    os_environ["SANIC_NUM"] = "42"

    module = load_module_from_file_location(
        "/tmp/${SANIC_NUM}", encoding="utf-8"
    )

    os_environ.pop("SANIC_NUM")

    assert module.SANIC_1 == 1
    assert module.SANIC_2 == "2"
    assert module.SANIC_3 == ["3", "32"]

    module = load_module_from_file_location("/tmp/test.py")
    assert module.SANIC_1 == 1
    assert module.SANIC_

# Generated at 2022-06-14 08:10:17.009234
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    config = load_module_from_file_location("tests/test_config.py")
    config2 = load_module_from_file_location(Path("tests/test_config.py"))
    assert config.TEST_KEY is config2.TEST_KEY

    config3 = load_module_from_file_location(
        Path("$PWD") / "tests" / "test_config.py"
    )
    assert config.TEST_KEY is config3.TEST_KEY

    os_environ["TEST_ENV_VAR_FOR_TESTS"] = "variable"
    config4 = load_module_from_file_location(
        Path("$TEST_ENV_VAR_FOR_TESTS") / "tests" / "test_config.py"
    )
    assert not has

# Generated at 2022-06-14 08:10:27.249989
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    import sys
    import tempfile
    import pytest

    location = tempfile.mktemp()
    with open(location, "w") as fp:
        fp.write("foo = 2")

    module = load_module_from_file_location(location)

    # make sure the new module is imported
    assert module.foo == 2
    assert location in sys.modules

    # make sure you can get it from import_string
    module = import_string(location)
    assert module.foo == 2
    assert location in sys.modules

    # make sure you can pass in a pathlib.Path
    module = load_module_from_file_location(Path(location))
    assert module.foo == 2
    assert location in sys.modules

    # try to load a file that doesn't exist

# Generated at 2022-06-14 08:10:31.793932
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import json
    import os
    import tempfile

    test_dir = tempfile.TemporaryDirectory(prefix="test_sanic_")
    test_dir_path = Path(test_dir.name)
    test_file_name = "test_sanic_module.py"

    import_module_name = "test_pymodule"

    os_environ["TEST_DIR_PATH"] = str(test_dir_path)


# Generated at 2022-06-14 08:10:42.505408
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    test_file_path = Path(__file__).resolve().parent / "test.py"

    fake_env_var_name = "fake_env_var"
    fake_env_var_value = "fake_env_var_value"
    os_environ[fake_env_var_name] = fake_env_var_value

    test_file_path_with_env_var = (
        str(test_file_path).replace(".py", "")
        + f"${fake_env_var_name}"
        + ".py"
    )

    module_with_str_path = load_module_from_file_location(
        str(test_file_path)
    )
    assert module_with_str_path.test_variable == 42

    module_with_path = load_module_from

# Generated at 2022-06-14 08:10:54.302036
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # Test for file path
    msg = "The following environment variables are not set: a, b, c"
    try:
        load_module_from_file_location("/some/path/${a}/${b}/${c}")
    except LoadFileException as e:
        err = e
    assert err.args[0] == msg

    # Test for import_string
    msg = (
        "Unable to import 'import_string' "
        "from 'sanic.helpers.import_string', "
        "Please make sure that it is installed properly"
    )
    try:
        load_module_from_file_location("import_string")
    except ValueError as e:
        err = e
    assert err.args[0] == msg

# Generated at 2022-06-14 08:11:06.312046
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import tempfile
    import os
    import argparse
    import shutil
    import pathlib
    import sys

    parser = argparse.ArgumentParser(
        description="Unit test load_module_from_file_location function"
    )
    parser.add_argument(
        "--file_name",
        type=str,
        help="Name of file that will be created and used in tests.",
    )
    parser.add_argument(
        "--file_name2",
        type=str,
        help="Name of file that will be created and used in tests.",
    )
    parser.add_argument(
        "--silent",
        type=str_to_bool,
        help="If True print only OKs: True/False",
        default=True,
    )

# Generated at 2022-06-14 08:11:18.732410
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    tests = [
        ("${TEST_ENV_VAR}", "FALSE", {"TEST_ENV_VAR" : "FALSE"}),
        ("${TEST_ENV_VAR}", "FALSE", {"TEST_ENV_VAR" : "TRUE"}),
        ("test.conf", "TRUE", {}),
        ("test.conf", "TRUE", {"TEST_ENV_VAR" : "FALSE"}),
        ("test.conf", "FALSE", {"TEST_ENV_VAR" : "TRUE"}),
    ]


# Generated at 2022-06-14 08:11:31.502818
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # pylint: disable=unused-variable
    import os
    import tempfile

    # 1) Test it with a module name and path to file.
    tmp_1_path = os.path.join(
        tempfile.gettempdir(), "tmp_1.py"
    )  # Path to temporary file.
    tmp_1 = open(tmp_1_path, "w")
    tmp_1.write("TEST_VAR_1 = 1")  # Write something to it.
    tmp_1.close()
    tmp_1_module = load_module_from_file_location(
        "tmp_1", path=tmp_1_path
    )  # Load module from it.
    assert tmp_1_module.TEST_VAR_1 == 1
    os.remove(tmp_1_path)

# Generated at 2022-06-14 08:11:44.313494
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    some_test_env_var = "SOME_TEST_ENV_VAR"
    os_environ[some_test_env_var] = "/test/env/var"


# Generated at 2022-06-14 08:11:51.831920
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from sanic.exceptions import LoadFileException, PyFileError
    from tempfile import NamedTemporaryFile

    # A) Check if function raises LoadFileException
    # if some environment variables are not set.
    os_environ["test"] = "test_string"
    with NamedTemporaryFile(mode="w", delete=False) as f:
        f.write("test_string")

    with pytest.raises(LoadFileException):
        load_module_from_file_location(
            location="${test}", raising=True
        )

    # B) Check if function loads module as expected.
    test_module = load_module_from_file_location(
        Path(f.name), raising=True
    )

    assert test_module.__file__ == f.name

    # C) Check that function raises TypeError

# Generated at 2022-06-14 08:12:06.126048
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    test_dir = Path(__file__).parent
    module_name_1 = "config"
    module_name_2 = "module_not_exist"
    module_name_3 = "module_without_py_extension"
    file_name_1 = "config.py"
    file_name_2 = "module_without_py_extension"
    file_path_1 = Path(test_dir, file_name_1)
    file_path_2 = Path(test_dir, file_name_2)
    location_1 = str(file_path_1)
    location_2 = str(file_path_2)

    # Test location parameter.
    # Should accept string.
    assert load_module_from_file_location(location_1).__name__ == module_name_1

    # Should

# Generated at 2022-06-14 08:12:13.889267
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    import pytest

    test_path = Path("./tests/test_load_module_from_file_location.py")

    assert getattr(
        load_module_from_file_location(test_path),
        "some_test_string",
    ) == "some_string"
    assert getattr(
        load_module_from_file_location(test_path),
        "some_test_integer",
    ) == 42

    test_path = Path("./tests/nested/test_load_module_from_file_location.py")

    assert getattr(
        load_module_from_file_location(test_path),
        "some_test_string",
    ) == "some_string"

# Generated at 2022-06-14 08:12:24.097155
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import os
    import inspect
    import re

    current_script_path = os.path.dirname(inspect.getsourcefile(test_load_module_from_file_location))
    test_file_name = os.path.join(current_script_path, "test_module_loader.py")

    # The test
    module = load_module_from_file_location(test_file_name)

    assert module.is_loaded, "The test file was not loaded as expected"

    # This little part will explain how to resolve environment variables
    os.environ["SANIC"] = "SANIC"

    module = load_module_from_file_location(
        "This is an example, how to resolve environment "
        "${SANIC} variable in ${SANIC} location of the file"
    )

# Generated at 2022-06-14 08:12:33.582201
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    # 1) Check if it raises LoadFileException if given env var
    #    is not defined. This env var is not defined, so
    #    it should raise LoadFileException.
    os_environ.clear()
    try:
        load_module_from_file_location(
            "${THIS_ENV_VAR_IS_NOT_DEFINED}/some.py"
        )
        assert False, "Exception should be raised"
    except LoadFileException:
        pass

    # 2) Check if it raises LoadFileException if given env var
    #    is not defined. This env var is defined, so
    #    it should NOT raise LoadFileException.
    os_environ["THIS_ENV_VAR_IS_DEFINED"] = "some value"

# Generated at 2022-06-14 08:12:45.407067
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # pragma: no cover
    # Set some environment var.
    os_environ["e1"] = "<<_e1_>>"
    os_environ["e2"] = "<<_e2_>>"


# Generated at 2022-06-14 08:12:54.901354
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    os_environ.update({"ENV_VAR": "env_var_value"})

    test_module = load_module_from_file_location(
        "tests/fixtures/configs/some_file_name.py"
    )
    assert test_module.another_var == 8

    test_module = load_module_from_file_location(
        "/tests/fixtures/configs/some_file_name.py"
    )
    assert test_module.some_var == 7

    test_module = load_module_from_file_location(
        "/tests/fixtures/configs/${ENV_VAR}/some_file_name.py"
    )
    assert test_module.another_var == 8


# Generated at 2022-06-14 08:13:06.106383
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    from os import getcwd, environ

    # 0. Setting up.
    environ["temp_env_var"] = str(Path(getcwd()) / "temp_env_var")
    environ["temp_env_var_2"] = "some_value"
    config_some_path = Path(getcwd()) / "config_some_path"
    config_some_path.mkdir()
    some_config_file = config_some_path / "some_config_file.py"
    some_config_file.write_text("some_var = 'some_value'")

    # 1. Testing of config name with "." and ":"
    config_name = "some_config_file"

# Generated at 2022-06-14 08:13:17.303735
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    def test_load_module():
        # If you want to test this function without side effects to your
        # filesystem.
        # You have to create custom FakeOpen object
        # http://stackoverflow.com/a/10916431/1927243
        class FakeOpen:
            text = "test_var = 1\ntest_list = [1, 2, 3]"

            def __init__(self, path):
                self.path = path
                self.name = path.split("/")[-1]

            def read(self):
                return self.text

        fake_open_object = FakeOpen("/some/path/")


# Generated at 2022-06-14 08:13:27.307167
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    def helper(location, expected):
        module = load_module_from_file_location(location)
        assert module.var == expected

    helper(os.path.join(os.path.dirname(__file__), "mock_module.py"), "some_value")
    helper(os.path.join(os.path.dirname(__file__), "mock_config.json"), "some_other_value")
    helper(b"\xe3\x81\x82\xe3\x81\x84\xe3\x81\x86\xe3\x81\x88\xe3\x81\x8a.py", "romaji")

# Generated at 2022-06-14 08:13:35.369543
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from tempfile import mktemp
    from datetime import date
    from textwrap import dedent

    #
    # A) Assert loading module from file with only .py extension.
    #

    file_path = mktemp(suffix=".py")
    file_name = file_path.split("/")[-1].split(".")[0]

    with open(file_path, "wt") as f:
        f.write(
            dedent(
                f"""
        PI = 3.14

        def square(x):
            return x*x


        if __name__ == "__main__":
            print(PI)
            print(square(PI))
            """
            )
        )

    # Mock module_from_spec and spec_from_file_location.

# Generated at 2022-06-14 08:13:48.600890
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import json

    import pytest

    with open("./test_files/test_location.json", "rt") as file:
        test_locations = json.loads(file.read())

    with pytest.raises(LoadFileException):
        load_module_from_file_location(test_locations["error_location"])

    load_module_from_file_location(test_locations["correct_location"])

# Generated at 2022-06-14 08:13:57.755734
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    # Create a file with module in it.
    import os
    import tempfile
    from os.path import join
    from textwrap import dedent

    module_file_content = dedent(
        """
        spam = 'spam'

        def func():
            return spam
    """
    )
    test_module_file = tempfile.NamedTemporaryFile(delete=False)
    test_module_file.write(module_file_content.encode())
    test_module_file.close()

    # Save file location to env var.
    os.environ["TEST_MODULE"] = join(
        os.getcwd(), test_module_file.name
    )

    # Creation of test module using its location from env var.

# Generated at 2022-06-14 08:14:11.097034
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    location_with_env_var = "/some/path/${SOME_ENV}"

    # A) Check if parameter is Path object.
    Path(location_with_env_var).exists = lambda x: True
    assert load_module_from_file_location(
        Path(location_with_env_var)
    ) is not None

    # B) Check if parameter is of a bytes type.
    assert load_module_from_file_location(
        b"/some/path/${SOME_ENV}"
    ) is not None

    # C) Check if parameter should be resolved as environment variable.
    #    Check if such environment variable is set.

    # Check if environment variable is not set.

# Generated at 2022-06-14 08:14:24.053000
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    print("In test_load_module_from_file_location")
    expected = "1"
    a = load_module_from_file_location("./tests/configs/conf.py")
    assert a.a == expected, "Expected %s but got %s" % (expected, a)
    a = load_module_from_file_location("./tests/configs/conf.json")
    assert a.a == expected, "Expected %s but got %s" % (expected, a)
    a = load_module_from_file_location("./tests/configs/conf.yml")
    assert a.a == expected, "Expected %s but got %s" % (expected, a)

# Generated at 2022-06-14 08:14:34.518884
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    os_environ["DUMMY_ENV_VAR"] = "/dummy"
    os_environ["DUMMY_ENV_VAR_2"] = "tmp"

    current_dir = Path(__file__).parent.absolute()
    dummy_py_path = current_dir / "dummy.py"

    module = load_module_from_file_location(
        dummy_py_path, encoding="utf8"
    )
    assert module.dummy_path == dummy_py_path.absolute()
    module = load_module_from_file_location(
        "/tmp/${DUMMY_ENV_VAR_2}/dummy.py", encoding="utf8"
    )
    assert module.dummy_path == "/tmp/tmp/dummy.py"
    module = load_module

# Generated at 2022-06-14 08:14:45.298999
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    os_environ["some_env_var"] = "some_value"

    with tempfile.NamedTemporaryFile() as f:
        f.write(b"foo = 42\nbar = 'baz'\n")
        f.flush()
        module = load_module_from_file_location(f.name)

    assert module.foo == 42
    assert module.bar == "baz"

    with tempfile.NamedTemporaryFile() as f:
        f.write(b"foo = 42\n")
        f.flush()
        module = load_module_from_file_location(
            f.name,
            "/some/path/${some_env_var}"
        )

    assert module.foo == 42

# Generated at 2022-06-14 08:14:52.758512
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
  
    import os
    import tempfile
    from os import environ
    from pathlib import Path

    # test for syntax errors
    try:
        load_module_from_file_location("tests/test.py")
    except PyFileError:
        pass
    else:
        assert False

    # test for non-exist location
    try:
        load_module_from_file_location("tests/test2.py")
    except IOError:
        pass
    else:
        assert False

    # test for environment variables
    env_var_name = "CONFIG_FOR_TEST"
    assert env_var_name not in os.environ

    with tempfile.TemporaryDirectory() as temp_dirname:
        os.environ[env_var_name] = temp_dirname
        config_path = Path

# Generated at 2022-06-14 08:15:04.129729
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from tempfile import NamedTemporaryFile
    from pathlib import Path

    # A) Test with str location parameter
    with NamedTemporaryFile(prefix="sanic_config_") as _file:
        _file.write("""
            TEST_VARIABLE_1 = "Some variable value"
        """.encode("utf8"))
        _file.flush()

        module = load_module_from_file_location(
            _file.name, encoding="utf8", mode="r"
        )
        assert hasattr(module, "TEST_VARIABLE_1")
        assert getattr(module, "TEST_VARIABLE_1") == "Some variable value"

    # B) Test with bytes location parameter

# Generated at 2022-06-14 08:15:12.745935
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import tempfile
    import shutil

    import pytest

    # Prepare some module configuration:
    test_config = {"some_configuration_option": "some_value"}

    # Create test module that contains some configuration:
    with tempfile.TemporaryDirectory() as tmp_dir_path:
        tmp_dir_path = Path(tmp_dir_path)
        test_conf_path = tmp_dir_path / "test_conf.py"
        with open(test_conf_path, "w") as test_conf:
            test_conf.write(
                """from pathlib import Path
test_config = {setup_conf}
test_module_path = Path(__file__).parent.absolute()
"""
                .format(
                    setup_conf=str(test_config)
                )  # nosec
            )

       

# Generated at 2022-06-14 08:15:25.324468
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    os_environ["some_env_var"] = "testing_env_var"

    location = "./tests/data/config.cfg"
    module = load_module_from_file_location(location)
    assert module
    assert module.__name__ == "config"
    assert module.__file__.endswith("/config.cfg")
    assert module.TESTING == True
    assert module.TESTING_WITH_VALUE == "testing value with environment "
    "variables"

    location = "./tests/data/config.cfg"
    module = load_module_from_file_location(location)
    assert module
    assert module.__name__ == "config"
    assert module.__file__.endswith("/config.cfg")
    assert module.TESTING == True


# Generated at 2022-06-14 08:15:42.465368
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from tempfile import NamedTemporaryFile

    module = None
    temp_file_name = ""
    with NamedTemporaryFile(mode="w+") as temp_file:
        module_name = "test_module"
        path = temp_file.name
        temp_file_name = path
        temp_file.write(f"test_variable = 'abc'")
        temp_file.seek(0)
        try:
            module = load_module_from_file_location(module_name, path)
        except Exception as e:
            raise e

    assert module is not None
    assert module.test_variable == "abc"

    assert module.__file__ == temp_file_name
    assert "test_module" in module.__name__



# Generated at 2022-06-14 08:15:55.237403
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """ Tests function load_module_from_file_location()
        by testing imports from valid and invalid locations.
    """

    location = "sanic/helpers.py"
    import sanic

    path = Path(sanic.__file__).parent / "helpers.py"

    path_str = str(path)
    bytes_path = bytes(path)

    # A) Tests imports from valid locations

    # 1) Import from path as a string
    module_path_string = load_module_from_file_location(path_str)
    assert_module_path_string(module_path_string, path_str)

    # 2) Import from path as a bytes
    module_path_bytes = load_module_from_file_location(bytes_path, "utf8")

# Generated at 2022-06-14 08:16:06.286805
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from os import environ as os_environ
    from os import pathsep as os_pathsep
    from os import putenv as os_putenv
    from tempfile import TemporaryDirectory
    from textwrap import dedent
    from unittest import TestCase

    from sanic.helpers import load_module_from_file_location

    class LoadModuleFromFileLocationTestCase(TestCase):
        def setUp(self):
            self.temp_path = TemporaryDirectory()
            os_putenv("ENV_VAR_1", self.temp_path.name)
            os_putenv(
                "PYTHONPATH",
                os_environ["PYTHONPATH"] + os_pathsep + self.temp_path.name,
            )


# Generated at 2022-06-14 08:16:15.697288
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import tempfile

    location = tempfile.mkstemp(suffix=".py", prefix="some_config_")
    with open(location[1], "w+") as config:
        config.write(
            """
    SOME_CONST = 123
    SOME_OTHER_CONST = "some other const"
    """
        )
    module = load_module_from_file_location(location[1])
    assert module.SOME_CONST == 123
    assert module.SOME_OTHER_CONST == "some other const"



# Generated at 2022-06-14 08:16:26.762855
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    a = load_module_from_file_location("./test.py")
    assert a.__name__ == "test"
    assert a.__file__ == "./test.py"

    # A) Check if location contains any environment variables
    #    in format ${some_env_var}.
    a = load_module_from_file_location("./${HOME}/test.py")
    assert a.__name__ == "test"
    assert a.__file__ == os.environ["HOME"] + "/test.py"
    os.putenv("HOME", "/")

    # B) Check these variables exists in environment.
    with pytest.raises(LoadFileException, match="MyHouse"):
        load_module_from_file_location("./${MyHouse}/test.py")

    # C)

# Generated at 2022-06-14 08:16:33.284410
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import tempfile
    from pytest import raises

    # Test 1
    # load_module_from_file_location
    # Test if it loads .py file from path
    # and returns it's content.
    with tempfile.NamedTemporaryFile(mode="w+") as f:
        f.write("module_content = 'test'")
        f.seek(0)
        assert (
            load_module_from_file_location(f.name).module_content == "test"
        )

    # Test 2
    # load_module_from_file_location
    # Test if it raises LoadFileException
    # while trying to load path with non existing
    # environment variable.
    with tempfile.NamedTemporaryFile(mode="w+") as f:
        f.write("module_content = 'test'")

# Generated at 2022-06-14 08:16:46.401787
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Test function load_module_from_file_location"""
    import tempfile
    import os

    # Prepare testing module

# Generated at 2022-06-14 08:16:55.094292
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from .test_app import assert_app_config

    # Load from string of a python file

# Generated at 2022-06-14 08:17:01.169346
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    os_environ["SOME_ENV_VAR"] = "some_text"
    module_location = "/tmp/${SOME_ENV_VAR}/some_module.py"
    module = load_module_from_file_location(module_location)
    assert module.__file__ == module_location
    os_environ.pop("SOME_ENV_VAR")

# Generated at 2022-06-14 08:17:11.412760
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from unittest.mock import patch

    test_path = "configtest/test_file"

    with patch(
        "sanic.config.import_string",
        side_effect=ValueError("import failure"),
    ):
        try:
            load_module_from_file_location("test_location")
        except IOError:
            pass
        else:
            assert False, "IOError was not raised"

    with patch("sanic.config.import_string"):
        assert isinstance(
            load_module_from_file_location("test_location"), types.ModuleType
        )


# Generated at 2022-06-14 08:17:26.987292
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # pragma: no cover

    # Load module from path
    try:
        module_from_path = load_module_from_file_location(
            "../../sanic/helpers.py"
        )
        assert module_from_path.__name__ == "sanic.helpers"
    except Exception:
        pass

    # Load module from path using relative path
    try:
        module_from_path = load_module_from_file_location(
            "helpers.py", "../../sanic/"
        )
        assert module_from_path.__name__ == "sanic.helpers"
    except Exception:
        pass

    # Load package from path

# Generated at 2022-06-14 08:17:33.966343
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    os_environ["TEST_ENV_VAR"] = "/home/some_user/some_directory"
    module = load_module_from_file_location(
        "/some/path/${TEST_ENV_VAR}/some_module_name.py"
    )
    print(module)
    del os_environ["TEST_ENV_VAR"]



# Generated at 2022-06-14 08:17:39.217095
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    path_to_config = Path(__file__).parent / "configuration_files"
    test_config = path_to_config / "test_config.py"

    # A) Simple case.
    module = load_module_from_file_location(test_config)
    assert module.variable_in_python_file == "test_value"

    # B) Trying to pass environment variable ${PWD} in the path.
    module = load_module_from_file_location(
        test_config.parent.parent
        / "${PWD}"
        / path_to_config.name
        / test_config.name
    )
    assert module.variable_in_python_file == "test_value"

    # C) Check for exception.

# Generated at 2022-06-14 08:17:51.788875
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import os
    import sys
    import json
    import pytest
    import tempfile
    import importlib.util

    # If there is no environment variable TEMP_ENV_VAR
    # set in your OS environ, please create one
    # and set it to some value.
    # For example:
    # > export TEMP_ENV_VAR="/some/path"
    test_script_filename = "test.py"

    test_script_content = """
        bla = "foo"
        CONFIG_TEST_VAR = "test_value"
        TEST_CONFIG_VAR = [
            "item_1",
            "item_2",
            "item_3"
        ]

        class MyClass:
            pass
    """

    test_json_filename = "test.json"

   

# Generated at 2022-06-14 08:18:05.685005
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import tempfile

    def create_test_module_content(path, content):
        temp_folder = tempfile.gettempdir()
        mod_path = Path(temp_folder) / path
        mod_path.parent.mkdir(parents=True, exist_ok=True)
        with mod_path.open(mode="w") as f:
            f.write(content)
        return mod_path

    mod_path = create_test_module_content(
        path="sanic/utils/load_module_from_file_location.py",
        content="""
            def test_func():
                return "sub_module"
        """,
    )

# Generated at 2022-06-14 08:18:16.176107
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # Test if location is bytes and encoding is not set
    try:
        load_module_from_file_location(b"/a/b/c.py", "")
    except TypeError:
        pass

    # Test if location is bytes and encoding is set
    module = load_module_from_file_location(b"/a/b/c.py", "utf8")
    assert isinstance(module, types.ModuleType)

    # Test if location is Path or str and does not contain environment
    # variables and .py extension.
    module = load_module_from_file_location("/a/b/c.py", "utf8")
    assert isinstance(module, types.ModuleType)

    # Test if location is Path or str and does not contain environment
    # variables and does not contain .py extension.