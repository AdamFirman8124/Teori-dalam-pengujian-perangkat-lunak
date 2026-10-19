

# Generated at 2022-06-14 08:08:18.670546
# Unit test for function str_to_bool
def test_str_to_bool():
    # Test truthy values
    assert str_to_bool("y")
    assert str_to_bool("t")
    assert str_to_bool("Y")
    assert str_to_bool("1")

    # Test falsy values
    assert not str_to_bool("n")
    assert not str_to_bool("f")
    assert not str_to_bool("0")

    # Test invalid values
    with pytest.raises(ValueError):
        str_to_bool("")
    with pytest.raises(ValueError):
        str_to_bool("no")


# Generated at 2022-06-14 08:08:29.251731
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    module = load_module_from_file_location("importlib.util")
    assert module.module_from_spec is not None
    module = load_module_from_file_location("sys")
    assert module.version is not None
    module = load_module_from_file_location("tests.test_helpers")
    assert module.test_load_module_from_file_location is not None
    try:
        module = load_module_from_file_location("somemodule")
        assert False, "that's an error"
    except ImportError as e:
        e.name == "somemodule"

# Generated at 2022-06-14 08:08:35.181475
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    os_environ["test_env_variable"] = "test_env_variable_value"

    # A) Check if raised exception when some environment variables
    #    are not set.
    caught_exception = False
    try:
        load_module_from_file_location(
            "some_module_name",
            "some/path/${some_not_defined_env_variable}",
        )
    except LoadFileException:
        caught_exception = True

    assert caught_exception

    # B) Resolve environment variables in file location.
    load_module_from_file_location(
        "some_module_name", "some/path/${test_env_variable}"
    )
    assert True

# Generated at 2022-06-14 08:08:44.403158
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from pathlib import Path
    from tempfile import TemporaryDirectory

    with TemporaryDirectory() as tempdir_name:

        tempdir = Path(tempdir_name)

        # A) Create file with some python code
        fname = tempdir / "test_fname.py"
        with fname.open("w") as f:
            f.write(
                """\
"""
            )

        # B) Check that this file
        #    is successfully loaded as module.
        module = load_module_from_file_location(fname)
        assert module.__file__ == str(fname)

        # C) Create file with some python code
        fname = tempdir / "test_fname2.py"

# Generated at 2022-06-14 08:08:57.715878
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    from os import environ as os_environ


# Generated at 2022-06-14 08:09:08.415683
# Unit test for function str_to_bool
def test_str_to_bool(): # noqa
    assert str_to_bool("yes")
    assert str_to_bool("y")
    assert str_to_bool("Yep")
    assert str_to_bool("TRUE")
    assert str_to_bool("on")
    assert str_to_bool("1")
    assert str_to_bool("NO")
    assert not str_to_bool("OFF")
    assert not str_to_bool("disabled")
    assert not str_to_bool("FALSE")
    assert not str_to_bool("0")
    with pytest.raises(ValueError):
        str_to_bool("")
    with pytest.raises(ValueError):
        str_to_bool(" ")
    with pytest.raises(ValueError):
        str_to_bool("noo")

# Generated at 2022-06-14 08:09:21.778821
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Unit test for function load_module_from_file_location."""

    # A) Check right work of function.
    os_environ["TEST_ENV_VAR"] = "some_env_var"
    location = "/some/path/${TEST_ENV_VAR}"
    module = load_module_from_file_location(location)
    assert module.__file__ == location
    del os.environ["TEST_ENV_VAR"]

    # B) Check ValueError on empty argument.
    location = ""
    with pytest.raises(ValueError) as excinfo:
        load_module_from_file_location(location)
    assert (
        "Unable to load configuration file ()" in str(excinfo.value)
    )

    # C) Check ValueError on non exist file

# Generated at 2022-06-14 08:09:22.305451
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    pass

# Generated at 2022-06-14 08:09:31.926115
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    import pytest
    import tempfile
    import shutil

    example_config = """\
    SOME_CONSTANT = "example"
    SOME_OTHER_CONSTANT = 5
    """

    # 1) Test if it works with bytes and string path parameters
    with tempfile.NamedTemporaryFile() as temp_file:
        temp_file.write(example_config.encode("utf8"))
        temp_file.flush()
        module = load_module_from_file_location(temp_file.name)
        assert hasattr(module, "SOME_CONSTANT")
        assert hasattr(module, "SOME_OTHER_CONSTANT")
        del module


# Generated at 2022-06-14 08:09:41.677654
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import pytest

    def _test(
        location,
        encoding="utf8",
        isinstance_module=types.ModuleType,
        module_atr=None,
        exception=None,
    ):
        assert (
            isinstance(load_module_from_file_location(location, encoding), isinstance_module)  # noqa
            or (module_atr is not None and hasattr(module_atr, "__file__"))
            or exception == ValueError
        )

    # Test 1
    _test("sanic.exceptions")
    # Test 2
    _test("/Users/mahmoud/github/libraries/sanic/sanic/exceptions.py")
    # Test 3

# Generated at 2022-06-14 08:09:57.521224
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # XXX: This is not a real unit testing, but you know - should be good enough
    import os
    import sys

    import pytest

    # First, save the current environment vars and change the values
    # of SANIC_CONFIG_ENV1 and SANIC_CONFIG_ENV2.
    old_env_vars = os.environ.copy()
    os.environ["SANIC_CONFIG_ENV1"] = "env1"
    os.environ["SANIC_CONFIG_ENV2"] = "env2"

    # Test for the case, when location is of a type bytes and encoding != 'utf8'.
    # For example: location = b"/home/sanic/config1${SANIC_CONFIG_ENV1}.json${"
    #                          b"SANIC_CONFIG_

# Generated at 2022-06-14 08:10:09.362732
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    from tempfile import TemporaryDirectory

    with TemporaryDirectory() as tmp_dir:
        # Test if it can load config from file
        tmp_dir_path = Path(tmp_dir)
        conf_file = tmp_dir_path / "config.py"
        conf_file.write_text(
            text="some_var = 'some_val'",
            encoding="utf8"
        )
        config_module = load_module_from_file_location(
            location=conf_file
        )
        assert config_module.some_var == "some_val"
        # Test if it can load config from folder
        conf_file = tmp_dir_path / "config.py"

# Generated at 2022-06-14 08:10:18.795963
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Checks if function load_module_from_file_location works correctly."""
    from tempfile import mkstemp
    from sanic import Sanic

    app = Sanic("test_load_module_from_file_location")

    # B) Check if it works for correct file.
    __, test_file = mkstemp()
    with open(test_file, "w") as test_file:
        test_file.write(
            "key = 'value'\n"
            "port = 123\n"
            "debug = True\n"
            "host = '0.0.0.0'\n"
        )
    loaded_config = load_module_from_file_location(test_file)

    assert loaded_config.key == "value"
    assert loaded_config.port == 123

# Generated at 2022-06-14 08:10:28.344789
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    # case 1
    location = "${HOME}/config/config.py"
    # Fake os.environ['HOME']
    os_environ["HOME"] = "/home/testuser"
    expected_module = types.ModuleType("config")
    expected_module.__file__ = "/home/testuser/config/config.py"
    assert load_module_from_file_location(location) == expected_module
    # Clean up
    del os_environ["HOME"]

    # case 2
    location = "${HOME}/config/config.py"
    # Do not define os.environ['HOME']
    # Environment variable from location
    # will not be resolved.
    assert load_module_from_file_location(location) == None

    # case 3
    location = "./config.py"
    expected_

# Generated at 2022-06-14 08:10:40.869220
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    some_module = load_module_from_file_location(
        "tests.some_module",
        "./tests/some_module.py",
        origin="some_module.py",
    )

    assert some_module.some_var == 1
    assert some_module.some_other_var == 2

    some_module = load_module_from_file_location(
        "tests.some_module",
        "./tests/some_module.py",
        "./tests/some_module.pyc",
        "./tests/some_module.pyo",
        origin="some_module.py",
        is_package=True,
    )

    assert some_module.some_var == 1
    assert some_module.some_other_var == 2

    some_module = load_module_from_file_

# Generated at 2022-06-14 08:10:53.694341
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # test relative path
    os_environ["test_reletive_path"] = "/some/path/"
    assert (
        load_module_from_file_location(
            "test_relative_path", "some_module_name.py"
        )
        is not None
    )

    # test absolute path
    assert (
        load_module_from_file_location(
            "/some/path/some_module_name.py"
        ) is not None
    )

    # test enviroment variable
    assert (
        load_module_from_file_location(
            "${test_reletive_path}some_module_name.py"
        ) is not None
    )

    # test with pathlib.Path

# Generated at 2022-06-14 08:11:05.776341
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    import os
    import pytest
    import tempfile

    def create_temporary_file_with_content(file_content: bytes) -> Path:
        """Create temporary file with content and return a path
        to this temporary file."""

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_dir_path = Path(temp_dir)

            some_file_path = temp_dir_path / "some_file.py"

            with some_file_path.open("wb") as some_file:
                some_file.write(file_content)

            return some_file_path

    def create_temporary_directory_containing_file(
        file_name: str, file_content: bytes
    ) -> Path:
        """Create temporary directory containing file with content and return
        a path to this temporary directory."""

# Generated at 2022-06-14 08:11:18.555196
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    class Module:
        pass

    module = Module()
    module.test = "it works!"
    module.test_lambda = lambda: "it works!"
    sys.modules["test_load_module_from_file_location"] = module

    some_module = load_module_from_file_location(
        "test_load_module_from_file_location"
    )
    assert some_module.test == "it works!"
    assert some_module.test_lambda() == "it works!"

    Path("testing.py").touch()
    some_module = load_module_from_file_location("testing.py")
    assert some_module.__name__ == "testing"

    Path("testing-bytes.py").touch()

# Generated at 2022-06-14 08:11:31.311270
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    from random import random
    from tempfile import NamedTemporaryFile

    file_name = "some_file_name.py"
    file_with_env_var_in_the_name = "some_file_name_${RANDOM}.py"
    module_name = "module_name"
    module_var1 = "module_var1"
    module_var2 = "module_var2"
    module_var1_val = random()
    module_var2_val = random()
    env_var = "RANDOM"
    env_var_val = random()


# Generated at 2022-06-14 08:11:44.132360
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import pytest
    from tempfile import NamedTemporaryFile
    from pathlib import Path
    from os import environ as os_environ
    environ = os_environ.copy()
    some_env_var = "some_env_var"
    some_env_val = "some_env_val"

    def _exec(script, m, name=None):
        if not name:
            name = m.__name__
        exec(script, m.__dict__, m.__dict__)
        if name != "__main__":
            return getattr(m, name)

    with NamedTemporaryFile(mode="w+", suffix=".py") as f:
        f.write("{some_env_var} = {some_env_val}")
        f.seek(0)

# Generated at 2022-06-14 08:12:00.423443
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    import sanic.config

    valid_config = {
        "some_key": "a",
        "some_other_key": 1,
        "yet_another_key": [1, "a", True],
    }
    valid_config_str = f"some_key = {valid_config['some_key']}\n" \
                        f"some_other_key = {valid_config['some_other_key']}\n" \
                        f"yet_another_key = {valid_config['yet_another_key']}\n"

    env_var_name = "SANIC_TEST_ENV_VAR"
    env_var_value = "some_value"
    os_environ[env_var_name] = env_var_value


# Generated at 2022-06-14 08:12:02.980301
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    assert (
        load_module_from_file_location(Path(__file__))
        == load_module_from_file_location(__file__)
    )

# Generated at 2022-06-14 08:12:16.662810
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # Case 1: Env_var in location
    os_environ["MODULE"] = "module"
    module = load_module_from_file_location(
        "test_utils.test_load_module_from_file_location.module"
    )
    assert module.__file__ == "module"
    assert module.a == "config_a"
    assert module.b == "config_b"
    assert module.c == "config_c"
    module = load_module_from_file_location(
        f"${MODULE}",
        "tests/utils/data/config.py",
        submodule_search_locations=["/some/other/path"],
    )
    assert module.a == "config_a"
    assert module.b == "config_b"

# Generated at 2022-06-14 08:12:23.699912
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    _module_name = "tests.test_helpers.some_module"

    # 1. Test with module name
    module = load_module_from_file_location(_module_name)
    assert module.some_variable == "some_value"

    # 2. Test with module path
    module = load_module_from_file_location(
        Path(__file__).parent / "some_module.py"
    )
    assert module.some_variable == "some_value"

    # 3. Test with string module path
    module = load_module_from_file_location(
        str(Path(__file__).parent / "some_module.py")
    )
    assert module.some_variable == "some_value"

    # 4. Test with some bytes path with different encoding

# Generated at 2022-06-14 08:12:36.194109
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    # A) Check if ${some_env_var} is not set

    # 1. Set some_env_var environment variable
    #    and save its original value.
    import os
    some_env_var_original_value = os.environ.setdefault(
        "some_env_var", "some_env_var_value"
    )

    # 2. Delete some_env_var environment variable.
    os.environ.pop("some_env_var")

    # 3. Clear some_env_var environment variable.
    os.environ["some_env_var"] = ""

    # 4. Try to load module with ${some_env_var} in location.

# Generated at 2022-06-14 08:12:41.251910
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from _pytest.tmpdir import TempdirFactory
    from pathlib import Path
    from tempfile import gettempdir

    # We need to do this because tests run in another process,
    # so $TMP env var will not be the same.
    os_environ["TMP"] = str(gettempdir())

    # A) Create temporary files and dirs.
    tmpdir_factory = TempdirFactory()
    root = tmpdir_factory.mktemp(
        "load_module_from_file_location_test", numbered=False
    )

    config_file = root.join("config.py")
    config_file.write(r"my_var = 2")
    # Remove config.py and try to load it.
    os.remove(str(config_file))

# Generated at 2022-06-14 08:12:53.033311
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import tempfile
    import os

    location = tempfile.NamedTemporaryFile(mode="w")

    # 1) Test if we can load module provided as a file location.
    sample_module_content = """
        test_value = "sample_value"
        class SampleClass:
            def __init__(self):
                return
            def sample_method(self):
                return
    """
    location.write(sample_module_content)
    location.flush()

    loaded_module = load_module_from_file_location(location.name)

    # A) Check if module is loaded properly.
    assert loaded_module.test_value.lower() == "sample_value"
    assert isinstance(loaded_module.SampleClass(), loaded_module.SampleClass)

# Generated at 2022-06-14 08:13:05.650523
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from os import environ
    from os import makedirs
    from pathlib import Path

    from sanic import Sanic
    from tempfile import mkdtemp


# Generated at 2022-06-14 08:13:12.592360
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa: D102
    mod = load_module_from_file_location(
        "sanic.test.test_utils.test_load_module_from_file_location"
    )
    assert mod.test_string == "Test string"
    assert mod.test_int == 123
    assert mod.test_float == 12.3
    assert mod.test_function.__name__ == "test_function"
    assert mod.test_path == Path.cwd()

# Generated at 2022-06-14 08:13:23.368930
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    location = "tests/test_configs/test_config_1.py"  # exists
    module = load_module_from_file_location(location)

    assert module.config_1_1 == 1
    assert module.config_1_2 == "string"

    location = "tests/test_configs/test_config_2.py"  # doesn't exist
    with pytest.raises(PyFileError):
        load_module_from_file_location(location)

    location = "tests/test_configs/test_config_3.py"  # exists
    module = load_module_from_file_location(location)
    assert module.config_3_1 == 1
    assert module.config_3_2 == "string"


# Generated at 2022-06-14 08:13:38.561569
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # 1. Loading file with path.
    path_to_file = Path(__file__).parent / "test.cfg"
    assert load_module_from_file_location(path_to_file).variable == "Value"

    # 2. Loading file from str path.
    path_to_file = str(path_to_file)
    assert load_module_from_file_location(path_to_file).variable == "Value"

    # 3. Loading file from bytes path.
    path_to_file = bytes(path_to_file, encoding="utf8")
    assert load_module_from_file_location(path_to_file).variable == "Value"

    # 4. Loading file with environment variable.
    path_to_file = "${SANIC_CFG_PATH}/test.cfg"
    os_

# Generated at 2022-06-14 08:13:51.849832
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    module = load_module_from_file_location("./tests/fixtures/load_module_file.py")
    assert module.DUMMY_MODULE_CONSTANT == "OK"
    module = load_module_from_file_location(
        "./tests/fixtures/load_module_file.py"
    )
    assert module.DUMMY_MODULE_CONSTANT == "OK"
    module = load_module_from_file_location(
        "./tests/fixtures/load_module_file.py",
        follow_symlinks=True,
    )
    assert module.DUMMY_MODULE_CONSTANT == "OK"

# Generated at 2022-06-14 08:14:04.440825
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import tempfile
    location = tempfile.mktemp()
    f = open(location, "w")
    f.write("test_value = 111")
    f.close()
    config = load_module_from_file_location(location)
    assert config.test_value == 111

    config2 = load_module_from_file_location(Path(location))
    assert config2.test_value == 111

    config3 = load_module_from_file_location(bytes(location, "utf-8"))
    assert config3.test_value == 111

    import os

    os.environ["TEST_ENV"] = location
    config4 = load_module_from_file_location(
        "${TEST_ENV}", encoding="utf-8"  # type: ignore
    )

# Generated at 2022-06-14 08:14:17.450518
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from sanic.config import CONFIG_DEFAULTS

    os_environ["SANIC_TEST_LOAD_MODULE_CONFIG_FILE"] = __file__
    # Load config file.
    config_module = load_module_from_file_location(
        "SANIC_TEST_LOAD_MODULE_CONFIG_FILE"
    )

    # Compare loaded module with default config.
    assert config_module == CONFIG_DEFAULTS

    # Compare loaded module with given config.
    config_module = load_module_from_file_location(
        "sanic.config", "LICENSE", *((), ()),
    )
    assert config_module.__copyright__ == "Copyright 2018 - present, the contributors"
    assert config_module.__license__ == "MIT License"



# Generated at 2022-06-14 08:14:25.426927
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # Create temp directory and place inside some configuration file.
    with tempfile.TemporaryDirectory() as tmp_dir:
        with open(str(Path(tmp_dir).joinpath("config.py")), "w") as f:
            f.writelines( (
                "import os\n",
                f"ENV_VAR = '{os.environ.get('TEST_ENV_VAR')}'\n",
                f"ENV_VAR_IN_PATH = '{os.environ.get('TEST_ENV_VAR_IN_PATH')}'\n",
                "CONSTANT = 'some_constant'\n",
            ) )

        # Test 1: Check for empty environment variable.
        del os.environ['TEST_ENV_VAR']

# Generated at 2022-06-14 08:14:27.070161
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    assert load_module_from_file_location("__builtin__") is builtins

# Generated at 2022-06-14 08:14:37.002441
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    # Mocks.
    import sys
    import inspect

    # A) Check that everything is OK when we have no environment variables
    #    in the file path.
    os_environ_backup = os_environ.copy()
    os_environ.clear()
    try:
        mod = load_module_from_file_location(__file__)
        assert mod.__file__ == __file__
        assert (
            inspect.getsource(
                mod
            ).strip()
            == inspect.getsource(
                sys.modules[this_module_name]
            ).strip()
        )
    finally:
        os_environ.clear()
        os_environ.update(os_environ_backup)

    # B) Check that load_module_from_file_location raises LoadFileException
    #   

# Generated at 2022-06-14 08:14:42.638068
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    os_environ["SOME_VAR"] = "/some/path/to"

# Generated at 2022-06-14 08:14:47.130582
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    assert (
        load_module_from_file_location(
            "samples/configs/config.py",
            Path(__file__).parent.joinpath("samples").joinpath("configs"),
        )
        .FOO
        == "bar"
    )



# Generated at 2022-06-14 08:14:58.135113
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    from os import environ as os_environ
    from os import mkdir
    from os.path import join as path_join
    from shutil import rmtree
    from tempfile import mkdtemp
    from textwrap import dedent

    # A) Create temporary directory.
    tmp_dir = mkdtemp()

    # B) Create some configuration there.
    some_config = dedent(
        r"""
        config_var_1 = 1
        config_var_2 = "Hello"
    """
    )
    config_file_name = "some_config.py"
    config_file_path = path_join(tmp_dir, config_file_name)
    with open(config_file_path, "w") as config_file:
        config_file.write(some_config)

# Generated at 2022-06-14 08:15:08.456904
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    module = load_module_from_file_location(
        "sanic.tests.test_utils.test_conf_module"  # type: ignore
    )
    assert module.SQLALCHEMY_DATABASE_URI == "sqlite://"
    assert module.DEBUG is True
    assert module.TESTING is False
    assert module.SECRET_KEY is ""



# Generated at 2022-06-14 08:15:11.722711
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    os_environ["some_env_var"] = "some_value"

    # If args is of a bytes type, encoding will be used to decode bytes.

# Generated at 2022-06-14 08:15:24.630878
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """Basic test of load_module_from_file_location function."""
    location_a = "some_module_name"
    location_b = "/some/path/to/module/file"
    location_c = "C:\some\windows\path\to\module\file"
    location_d = "C:\some\windows\path\to\module\file.py"

    with pytest.raises(
        ImportError, match="No module named 'some_module_name'"
    ):
        load_module_from_file_location(location_a)
    with pytest.raises(
        IOError, match="Unable to load configuration file"
    ):
        load_module_from_file_location(location_b)

# Generated at 2022-06-14 08:15:35.575583
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import tempfile, os

    location = tempfile.mkdtemp()
    file_path = os.path.join(location, "config.py")
    with open(file_path, "w") as f:
        f.write(
            """CHILDREN_WORKER_CONNECTIONS = 10
DEFAULT_HANDLER_CLASS = "sanic.request.Request"
"""
        )

    module = load_module_from_file_location(file_path)
    assert module.CHILDREN_WORKER_CONNECTIONS == 10
    assert module.DEFAULT_HANDLER_CLASS == "sanic.request.Request"
    assert module.__file__ == file_path

    module = load_module_from_file_location(location + "/config.py")
    assert module.CHILDREN_WORKER

# Generated at 2022-06-14 08:15:45.996411
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    from tempfile import TemporaryDirectory

    with TemporaryDirectory() as temp_dir:
        path = Path(temp_dir)
        config_file_path = path / "config.py"
        config_file_path.touch()

        module = load_module_from_file_location(config_file_path)
        assert isinstance(module, types.ModuleType)
        assert module.__file__ == str(config_file_path)

        with config_file_path.open() as file_:
            file_.write("ENV = 'dev'")
        module = load_module_from_file_location(config_file_path)
        assert module.ENV == "dev"

        module = load_module_from_file_location(
            ("config.py",), path.as_posix()
        )


# Generated at 2022-06-14 08:15:53.147514
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():  # noqa
    """Unit test for function load_module_from_file_location."""

    class LoadFileExceptionSubclass(LoadFileException):
        pass

    class PyFileErrorSubclass(PyFileError):
        pass

    # 1) Test for files with .py extension.

    # 1.1) Test if function returns expected module.
    #      If load_module_from_file_location returns expected module.
    #
    #      For example if we have file some_module_name.py
    #      in folder /some/path/ with following code inside:
    #
    #          variable = "some_variable"
    #
    #      then:
    #
    #          some_module = load_module_from_file_location(
    #              "some_module_name",
    #              "/some/path/some

# Generated at 2022-06-14 08:16:05.155015
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    from unittest.mock import patch

    def get_path(path):
        import os.path
        return os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            path
        )

    def test_config_file():
        """Returns contents of tests/config_for_testing_load_module_from_file_location.py
        file as string."""
        path = get_path(
            "config_for_testing_load_module_from_file_location.py"
        )
        with open(path, "r") as config_file:
            return config_file.read()


# Generated at 2022-06-14 08:16:17.329093
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # Validator
    def _validate_result_module(module):
        assert "CONFIG_VAR" in module.__dict__.keys()
        assert module.CONFIG_VAR == "config var"

    # Case 1: load from string
    result_module = load_module_from_file_location(
        "tests/test_configs/config.py"
    )
    _validate_result_module(result_module)

    # Case 2: load from bytes
    result_module = load_module_from_file_location(
        b"tests/test_configs/config.py"
    )
    _validate_result_module(result_module)

    # Case 3: load from Path

# Generated at 2022-06-14 08:16:30.095793
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    import random

    # We can't use here pytest.tmpdir because it is run in separated process.
    import tempfile

    random_string = str(random.getrandbits(256))

    # Set some_env_var to random_string
    os_environ["some_env_var"] = random_string

    with tempfile.TemporaryDirectory() as tmpdir_name:
        tmpdir = Path(tmpdir_name)

        # Prepare some_module.py
        some_module_file = tmpdir / "some_module.py"
        with some_module_file.open("wb") as f:
            f.write(
                b"some_var = '"
                + some_module_file.as_posix().encode("utf8")
                + b"'"
            )

        # Prepare some_var_

# Generated at 2022-06-14 08:16:41.680736
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    assert isinstance(
        load_module_from_file_location(__file__), types.ModuleType
    )
    assert isinstance(
        load_module_from_file_location(b".", encoding="utf8"),
        types.ModuleType,
    )
    assert isinstance(
        load_module_from_file_location("./sanic/", encoding="utf8"),
        types.ModuleType,
    )
    assert isinstance(
        load_module_from_file_location("./test/test_helpers.py"),
        types.ModuleType,
    )
    assert isinstance(
        load_module_from_file_location("./test/test_helpers.py", b"utf8"),
        types.ModuleType,
    )

# Generated at 2022-06-14 08:16:55.170504
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # A) Check if location contains any environment variables
    #    in format ${some_env_var}.
    location = "some/path"
    assert len(re_findall(r"\${(.+?)}", location)) == 0

    # B) Check these variables exists in environment.
    location = "some/path/${TEST_ENV_VAR}"
    assert len(set(re_findall(r"\${(.+?)}", location)).difference(os_environ.keys()))

    # C) Substitute them in location.
    location = "some/path/${TEST_ENV_VAR}"
    os_environ["TEST_ENV_VAR"] = "test"

# Generated at 2022-06-14 08:17:04.985923
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    """
    Tests load_module_from_file_location function functionality.

    Config file test/load_config_test.py contains:
        some_var = "some_var_value"
        some_dict = {"some_key": "some_dict_value"}
        some_list = [1, 2, 3]
    """

    # Config file path is given as a string.
    # 1) When the file name contains .py extension.
    module = load_module_from_file_location(
        "test/load_config_test.py"
    )
    assert module.some_var == "some_var_value"
    assert module.some_dict == {"some_key": "some_dict_value"}
    assert module.some_list == [1, 2, 3]

    # 2) When the file name doesn't

# Generated at 2022-06-14 08:17:17.943023
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    os_environ["LOCAL_ENV_VAR_EXAMPLE"] = "testing"
    os_environ["SECRET_ENV_VAR_EXAMPLE"] = "testing"

    def testing_module():
        return 1

    assert (
        load_module_from_file_location(
            "/some/path/${LOCAL_ENV_VAR_EXAMPLE}/testing_module.py"
        ).testing_module()
        == testing_module()
    )
    assert (
        load_module_from_file_location(
            "/some/path/${SECRET_ENV_VAR_EXAMPLE}/testing_module.py"
        ).testing_module()
        == testing_module()
    )

# Generated at 2022-06-14 08:17:27.742202
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # Without any environment variables
    conf_file = str(Path(__file__).parent / "conf_file_for_test")
    module = load_module_from_file_location(conf_file)
    assert module.foo == "bar"
    assert module.bar == {"baz": True, "quz": False}
    assert module.deeply_nested_dict == {"a": {"b": {"c": {"d": 42}}}}
    assert module.nested_list == ["foo", "bar", ["baz", ["quz", [42]]]]

# Generated at 2022-06-14 08:17:39.384284
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # Test A
    location = "some_module_name"
    assert load_module_from_file_location(location) == import_string(location)

    # Test B
    location = "/some/path/${some_env_var}"
    env_var = "SOME_ENV_VAR"
    os_environ[env_var] = ""
    with pytest.raises(
        LoadFileException, match=f"The following environment variables are"
    ):
        load_module_from_file_location(location)
    os_environ[env_var] = "test_path"
    spec_location = location.replace("${" + env_var + "}", os_environ[env_var])
    spec_name = spec_location.split("/")[-1]

# Generated at 2022-06-14 08:17:48.600001
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    # Given
    location = "tests/config_for_tests.py"
    os_environ["VAR_FROM_ENV"] = "from environment"
    os_environ["VAR_FROM_ENV_NOT_USED"] = "not used"

    # When
    imported_module = load_module_from_file_location(location)

    # Then
    assert imported_module.VAR_FROM_MODULE == "from module"
    assert imported_module.VAR_FROM_ENV == "from environment"



# Generated at 2022-06-14 08:17:57.729378
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():

    from unittest import mock
    from unittest.mock import patch

    from os import environ as os_environ

    from pathlib import PosixPath

    os_environ["MY_TEST_ENV_VAR"] = "my_test_env_value"

    with patch("os.remove") as mocked_os_remove:
        with patch("tempfile.mkstemp") as mocked_tempfile_mkstemp:
            with patch("sanic.helpers.import_string") as mocked_import_string:

                mocked_tempfile_mkstemp.return_value = 0, PosixPath(
                    "/tmp/test_file_name.py"
                )

                result = load_module_from_file_location(
                    "test_file_name", "/tmp"
                )

                mocked_import_

# Generated at 2022-06-14 08:18:08.805043
# Unit test for function load_module_from_file_location
def test_load_module_from_file_location():
    test_env_var = "TEST_ENV_VAR"
    test_env_val = "TEST_ENV_VAL"
    os_environ[test_env_var] = test_env_val

    path = Path(
        __file__
    ).parent  # sanic.config -> tests/test_config.py -> tests/ -> root/ ...

    # Regular file load use case.
    assert (
        __file__
        == load_module_from_file_location(__file__).__file__
    )  # check if module file path (__file) is the same
    assert (
        __file__
        == load_module_from_file_location(__file__).__file__
    )  # check if module file name (__name) is the same

    # Environment variable substitution use case.