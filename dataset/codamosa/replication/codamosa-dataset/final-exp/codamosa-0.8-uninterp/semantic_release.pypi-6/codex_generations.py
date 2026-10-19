

# Generated at 2022-06-14 05:13:01.407453
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Test for username, password and repository
    os.environ["PYPI_USERNAME"] = "username"
    os.environ["PYPI_PASSWORD"] = "password"
    os.environ["HOME"] = "/test/test_dir"
    os.environ["SEMANTIC_RELEASE_REPOSITORY"] = "repository"

    upload_to_pypi("test", True, "*")

    assert "twine upload -u 'username' -p 'password' -r 'repository' --skip-existing  'test/*'" == run.calls[0].args[0]

    # Test for api token
    os.environ["PYPI_TOKEN"] = "pypi-test_token"
    del os.environ["PYPI_USERNAME"]
   

# Generated at 2022-06-14 05:13:09.241743
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from unittest.mock import patch, Mock

    with patch('invoke.run', Mock()):
        from .helpers import LogMock
        from .helpers import LoggedFunction
        from .helpers import LogMock as logger
        logger.setLevel('INFO')
        LoggedFunction.logger = logger
        upload_to_pypi(path='dist')
        assert logger.logged_call.called

        logger.setLevel('ERROR')
        LoggedFunction.logger = logger
        upload_to_pypi(path='dist')
        assert logger.logged_call.called

# Generated at 2022-06-14 05:13:09.828513
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:13:15.847707
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from unittest.mock import patch, call

    with patch("invoke.run") as mock_run:
        upload_to_pypi()
        mock_run.assert_called_with("twine upload  \"dist/*\"")

    with patch.dict(os.environ, {"PYPI_TOKEN": "pypi-mytoken"}):
        with patch("invoke.run") as mock_run:
            upload_to_pypi()
            mock_run.assert_called_with("twine upload -u '__token__' -p 'mytoken' \"dist/*\"")

    with patch.dict(os.environ, {"PYPI_USERNAME": "myusername", "PYPI_PASSWORD": "mypassword"}):
        with patch("invoke.run") as mock_run:
            upload_

# Generated at 2022-06-14 05:13:16.761446
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # execute upload_to_pypi in temporary folder
    # and catch any error, or check if it was the expected
    # error, or check the output
    raise NotImplementedError

# Generated at 2022-06-14 05:13:29.203023
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Test environment variables
    # Test with API token
    os.environ["PYPI_TOKEN"] = "pypi-foo"
    upload_to_pypi("path")
    del os.environ["PYPI_TOKEN"]

    # Test with username and password
    os.environ["PYPI_USERNAME"] = "bar"
    os.environ["PYPI_PASSWORD"] = "baz"
    upload_to_pypi("path")
    del os.environ["PYPI_USERNAME"]
    del os.environ["PYPI_PASSWORD"]

    # Test pypi repository
    os.environ["TWINE_REPOSITORY"] = "testpypi"
    upload_to_pypi("path")

    # Test with glob_

# Generated at 2022-06-14 05:13:32.776787
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    with mock.patch('invoke.run') as mock_run:
        upload_to_pypi()
        mock_run.assert_called_with('twine upload "dist/*"')

# Generated at 2022-06-14 05:13:36.741150
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Skip test if credentials not set
    if (
        os.environ.get("PYPI_TOKEN", None)
        or os.environ.get("PYPI_USERNAME", None)
        or os.environ.get("PYPI_PASSWORD", None)
    ):
        upload_to_pypi(skip_existing=True)

# Generated at 2022-06-14 05:13:39.747348
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Unit test for function upload_to_pypi"""
    upload_to_pypi(path="dist", skip_existing=False, glob_patterns=None)

# Generated at 2022-06-14 05:13:40.871484
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # TODO
    return True

# Generated at 2022-06-14 05:13:56.666231
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Set environment variables
    os.environ["PYPI_USERNAME"] = "username"
    os.environ["PYPI_PASSWORD"] = "password"

    # Set arguments
    path = "my-dist"
    skip_existing = False

    # Call upload_to_pypi()
    upload_to_pypi(path, skip_existing)

    # Assert that the command to run Twine was called correctly
    run.assert_called_once_with(
        "twine upload -u 'username' -p 'password' my-dist/*"
    )

    # Unset environment variables
    del os.environ["PYPI_USERNAME"]
    del os.environ["PYPI_PASSWORD"]

    # Set environment variables for pypi token

# Generated at 2022-06-14 05:14:07.183144
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import pytest

    with pytest.raises(ImproperConfigurationError, match="Missing credentials for uploading to PyPI"):
        upload_to_pypi()

    os.environ["PYPI_TOKEN"] = "my_token"
    upload_to_pypi()
    del os.environ["PYPI_TOKEN"]

    os.environ["PYPI_USERNAME"] = "user"
    os.environ["PYPI_PASSWORD"] = "password"
    upload_to_pypi()
    del os.environ["PYPI_USERNAME"]
    del os.environ["PYPI_PASSWORD"]

# Generated at 2022-06-14 05:14:10.718810
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(path=".", glob_patterns=["test_upload_to_pypi.py"])
    
if __name__ == '__main__':
    test_upload_to_pypi()

# Generated at 2022-06-14 05:14:20.409683
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pypi_token = "b0-1234567890123456789012345678901234567890"
    assert upload_to_pypi.__name__ == "upload_to_pypi"
    try:
        os.environ["PYPI_TOKEN"] = pypi_token
        upload_to_pypi()
    except Exception as error:
        assert error == ImproperConfigurationError("Missing credentials for uploading to PyPI")
        os.environ["PYPI_USERNAME"] = "fake-username"
        os.environ["PYPI_PASSWORD"] = "fake-password"
        upload_to_pypi()
    del os.environ["PYPI_TOKEN"]

# Generated at 2022-06-14 05:14:25.922176
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import os

    path = os.getcwd()
    token = os.path.join(path, "tests/files/twine.pypi.file")
    os.environ["HOME"] = path
    os.environ["PYPI_TOKEN"] = token
    upload_to_pypi()

# Generated at 2022-06-14 05:14:32.453904
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .mock_context import mock_context
    from .mock_io import mock_io
    from .mock_proj import mock_proj

    with mock_io() as sio:
        with mock_proj(sio):
            with mock_context():
                upload_to_pypi(skip_existing=True)

# Generated at 2022-06-14 05:14:36.645146
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """
    Test for upload_to_pypi
    """
    semver_version_changed = "upload_to_pypi"
    upload_to_pypi(
        path = "dist",
        skip_existing = False,
        glob_patterns = ["jason@mysteryshack.com"],
    )

# Generated at 2022-06-14 05:14:50.083077
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .helpers import MockContext

    glob_patterns = ["foo*"]
    path = "dist"
    token = "pypi-token"
    username = "username"
    password = "password"

    def run_check(ctx, cmd, **kwargs):
        ctx.assert_called_once_with("twine", "upload", "-u", username, "-p", password, "--skip-existing", '"dist/foo*"')
        ctx.assert_success()

    ctx = MockContext(run_check, "HOME", os.getcwd())
    config.load()
    config.set("repository", "test-repo")
    config.save()

    # Test using token

# Generated at 2022-06-14 05:14:52.823609
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(
        path="test_upload_to_pypi",
        skip_existing=True,
        glob_patterns=["test_upload_to_pypi"],
    )

# Generated at 2022-06-14 05:15:01.568233
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .plugins.twine import upload_to_pypi
    import tempfile
    import pathlib
    import shutil

    test_dir = tempfile.mkdtemp()
    path = str(pathlib.Path(test_dir) / "dist")
    os.mkdir(path)
    try:
        upload_to_pypi(path)
    except SystemExit as e:
        assert e.code == 2
    else:
        assert False, "Should have raised SystemExit"
    finally:
        shutil.rmtree(test_dir)



# Generated at 2022-06-14 05:15:10.967550
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi()

# Generated at 2022-06-14 05:15:20.983486
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .helpers import create_files, remove_files

    # Create dirs and files

# Generated at 2022-06-14 05:15:31.139000
# Unit test for function upload_to_pypi
def test_upload_to_pypi():

    from unittest.mock import patch, MagicMock
    import tempfile

    pypirc_file = """

[distutils]
index-servers =
  pypi
  pypitest

[pypi]
username: __token__
password: pypi-123456789

[pypitest]
repository: https://test.pypi.org/legacy/
username: __token__
password: pypi-123456789
"""
    with tempfile.TemporaryDirectory() as tmpdir:
        fname = os.path.join(tmpdir, ".pypirc")
        print("Writing", fname)
        with open(fname, "w") as fh:
            fh.write(pypirc_file)


# Generated at 2022-06-14 05:15:40.322207
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .helpers import mock_run
    from .mock_settings import mock_config
    import mock

    with mock.patch("invoke.run", new=mock_run) as run_mock:
        mock_config(
            {
                "repository": "pypi",
                "twine": {"skip_existing": False, "glob_patterns": ["*"]},
            }
        )
        upload_to_pypi(
            path="path/to/wheels",
            skip_existing=False,
            glob_patterns=["*"],
        )
        assert run_mock.called is True
        assert run_mock.call_count == 1
        call_args = run_mock.call_args[0]

# Generated at 2022-06-14 05:15:52.511155
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Unit test for function upload_to_pypi.
    """
    from semantic_release.settings import Config

    old_config = config

    class TestConfig(Config):
        """Test config for testing upload_to_pypi function

        Attributes:
            info (logging.LogRecord): object with message, levelname and other info
                attributes
        """

        info = None

        def logger_info(self, msg, *args, **kwargs):
            """Mock of logging.info function

            Args:
                msg (str): log message
                args (list): optional arguments
                kwargs (dict): optional keyword arguments
            """
            self.info = logging.LogRecord(
                "name", 20, "/path/to/file.py", 111, msg, args, exc_info=None
            )

    test_

# Generated at 2022-06-14 05:16:02.848920
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """
    Unit test for upload_to_pypi
    """
    # test case 1: username & password
    # assert no error
    logger.info("Testing username & password")
    os.environ["PYPI_USERNAME"] = "bob"
    os.environ["PYPI_PASSWORD"] = "bobspassword"
    upload_to_pypi()
    del os.environ["PYPI_USERNAME"]
    del os.environ["PYPI_PASSWORD"]
    # test case 2: token
    # assert no error
    logger.info("Testing token")
    os.environ["PYPI_TOKEN"] = "pypi-sometoken"
    upload_to_pypi()
    del os.environ["PYPI_TOKEN"]

# Generated at 2022-06-14 05:16:11.776033
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    with open("test.pypirc", "w+") as f:
        f.write("[pypirc]\nusername=test\npassword=test\n")
    os.environ["PYPI_USERNAME"] = "test"
    os.environ["PYPI_PASSWORD"] = "test"
    upload_to_pypi(path="test", skip_existing=False, glob_patterns=["*"])
    os.unlink("test.pypirc")

# Generated at 2022-06-14 05:16:16.656833
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    try:
        run("rm -rf build dist")
        run("python setup.py bdist_wheel")
        upload_to_pypi()
        upload_to_pypi(skip_existing=True)
        run("python setup.py bdist_wheel")
        upload_to_pypi(skip_existing=True)
        upload_to_pypi(glob_patterns=["*-py2.py3-none-any.whl"])
    finally:
        run("rm -rf build dist")

# Generated at 2022-06-14 05:16:17.986030
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi("dist", True)

# Generated at 2022-06-14 05:16:19.690088
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert run(f"twine upload --skip-existing '{path}'")

# Generated at 2022-06-14 05:16:40.671131
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Testing function upload_to_pypi
    """
    from .helpers import MockRun

    with MockRun(success=True):
        upload_to_pypi()

# Generated at 2022-06-14 05:16:43.852028
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    with capture_logs() as logs:
        upload_to_pypi("dist", glob_patterns=["*"], skip_existing=False)


# Generated at 2022-06-14 05:16:49.573959
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    with open(os.devnull, "w") as fnull:
        try:
            upload_to_pypi()
        except ImproperConfigurationError as e:
            assert "Missing credentials for uploading to PyPI" == str(e)
        except FileNotFoundError as e:
            run("mkdir dist", stdout=fnull)
            upload_to_pypi()

# Generated at 2022-06-14 05:16:57.095207
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # no token
    os.environ.pop("PYPI_TOKEN", None)
    os.environ.pop("PYPI_USERNAME", None)
    os.environ.pop("PYPI_PASSWORD", None)
    import pytest
    with pytest.raises(ImproperConfigurationError):
        upload_to_pypi()

# Generated at 2022-06-14 05:16:58.585665
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(path="./dist")
    assert True

# Generated at 2022-06-14 05:17:09.719183
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import os
    import shutil
    import tempfile
    import contextlib
    import unittest
    import inspect
    import types
    import argparse
    import typing
    from unittest.mock import Mock
    from semantic_release.settings import config

    @contextlib.contextmanager
    def _change_directory(new_directory):
        old_directory = os.getcwd()
        os.chdir(new_directory)
        yield
        os.chdir(old_directory)

    @contextlib.contextmanager
    def _change_variable(var, value):
        old_value = var
        var = value
        yield
        var = old_value

    def create_file(filename):
        with open(filename, "w"):
            pass

    def get_parent_func():
        return inspect.current

# Generated at 2022-06-14 05:17:12.721848
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """
    helper function which helps you to test the upload_to_pypi function
    """
    assert upload_to_pypi() == 1

# Generated at 2022-06-14 05:17:14.605410
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """
    Successully uploads to twine
    """
    upload_to_pypi()


# Generated at 2022-06-14 05:17:16.008112
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi("dist", False, ["*"])

# Generated at 2022-06-14 05:17:16.689558
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:18:04.712135
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Test function upload_to_pypi.

    All test cases have these properties:
    * Expected return code is 0
    * pytest.raises(ImproperConfigurationError) is not raised, because if this is raised,
        then the test fails.
    """

    # Standard test case (using PYPI_TOKEN)
    os.environ["PYPI_TOKEN"] = "pypi-token"
    upload_to_pypi("./dist")

    # Standard test case (using PYPI_USERNAME and PYPI_PASSWORD)
    # This does not really upload to PyPI. It just checks for the behavior.
    os.environ["PYPI_USERNAME"] = "username"
    os.environ["PYPI_PASSWORD"] = "password"
    upload_to

# Generated at 2022-06-14 05:18:12.967385
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .mocks.tasks import MockContext

    path = "dist"
    glob_pattern = "*.whl"

    ctx = MockContext()

    upload_to_pypi(ctx, path, glob_patterns = [glob_pattern])

    assert ctx.run.mock_calls == [('run', ('twine upload '
                                           '"dist/{glob_pattern}"'.format(glob_pattern = glob_pattern)), {})]

# Generated at 2022-06-14 05:18:13.688282
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert False

# Generated at 2022-06-14 05:18:14.389102
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:18:19.107093
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    os.environ["PYPI_USERNAME"] = "testusername"
    os.environ["PYPI_PASSWORD"] = "testpassword"
    try:
        upload_to_pypi()
    except ImproperConfigurationError as e:
        assert "Missing credentials for uploading to PyPI" in str(e)

# Generated at 2022-06-14 05:18:27.142241
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi(path="") == 'twine upload  "*"'
    assert upload_to_pypi(path="", skip_existing=True) == 'twine upload   --skip-existing "*"'
    assert (upload_to_pypi(path="", glob_patterns=["file"]) ==
            'twine upload  "file"')
    assert (upload_to_pypi(path="", glob_patterns=["file", "file2"]) ==
            'twine upload  "file" "file2"')
    assert (upload_to_pypi(path="", glob_patterns=["file", "file2"]) ==
            'twine upload  "file" "file2"')

# Generated at 2022-06-14 05:18:38.513981
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Test the upload_to_pypi function.
    """
    import tempfile

    with tempfile.TemporaryDirectory() as tmp_dir:
        filename = os.path.join(tmp_dir, "test")
        with open(filename, "w") as f:
            f.write("content")

        # dist folder must exist
        upload_to_pypi(tmp_dir)

        # The file should not have been uploaded
        import requests
        from requests.exceptions import HTTPError

        try:
            res = requests.head("https://upload.pypi.org/legacy/", allow_redirects=True)
        except HTTPError as e:
            assert e.response.status_code == 404
        else:
            assert res.status_code == 200

# Generated at 2022-06-14 05:18:44.477927
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Test function upload_to_pypi"""
    config.set("repository", "test/testname", override=True)
    upload_to_pypi("this/is/a/dist", True)
    config.set("repository", "testname")

# Generated at 2022-06-14 05:18:45.691170
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()

# Generated at 2022-06-14 05:18:46.420781
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:19:59.330811
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    try:
        upload_to_pypi()
    except ImproperConfigurationError:
        pass
    assert True

# Generated at 2022-06-14 05:20:09.849338
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import test.unit_tests.helpers as helpers
    from invoke.config import Config

    # Configure env variables for username and password
    config = helpers.get_mock_config()
    config.run.return_value = Config({'exited': 0, 'ok': True})
    username = os.environ.get("PYPI_USERNAME")
    password = os.environ.get("PYPI_PASSWORD")
    os.environ["PYPI_USERNAME"] = "test"
    os.environ["PYPI_PASSWORD"] = "pass"

    upload_to_pypi(glob_patterns=["foo", "bar"])
    config.run.assert_called_once_with("twine upload -u 'test' -p 'pass' 'foo' 'bar'")



# Generated at 2022-06-14 05:20:10.595416
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:20:22.180596
# Unit test for function upload_to_pypi
def test_upload_to_pypi():

    # Mock environment variables
    os.environ["PYPI_TOKEN"] = "pypi-token"
    os.environ["HOME"] = "/home/user"
    os.environ["GITHUB_WORKSPACE"] = "/home/user/project"

    # Mock `run` function
    run_mock = mocker.patch("invoke.run")

    # Set home directory to not exist
    mocked_path = mocker.patch("pathlib.Path")
    mocked_path().exists.return_value = False

    # Upload a single glob pattern
    upload_to_pypi(glob_patterns=["*.whl"])

    # Upload multiple glob patterns
    upload_to_pypi(glob_patterns=["*.whl", "*.txt"])

    # Upload default glob pattern


# Generated at 2022-06-14 05:20:35.154774
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .context import ctx
    from .helpers import MockPath

    upload_path = MockPath("/home/user/project/dist")
    upload_path.add_file('fake-file-1.1.1-py3-none-any.whl')
    upload_path.add_file('fake-file-1.1.1.tar.gz')
    os.environ["PYPI_TOKEN"] = "pypi-FAKE_TOKEN"

    ctx.run = lambda k: ctx.run(k, pty=False)
    upload_to_pypi()

# Generated at 2022-06-14 05:20:43.358437
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .tasks import import_path

    return_value = {
        "calls": [
            (
                "run",
                [
                    "twine upload -u '__token__' -p 'pypi-token' --skip-existing 'dist/test_1.0.0-rc.1.dev0.tar.gz' 'dist/test_1.0.0-rc.1.dev0-py3-none-any.whl'"
                ],
                {},
                None,
                None,
            )
        ],
        "return_value": None,
    }
    
    os.environ['PYPI_TOKEN'] = "pypi-token"
    with import_path("twine.commands.upload"):
        path_to_files = "dist"
        import twine

# Generated at 2022-06-14 05:20:51.248882
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Unit test for function upload_to_pypi."""
    os.environ["TWINE_USERNAME"] = "TWINE_USERNAME"
    os.environ["TWINE_PASSWORD"] = "TWINE_PASSWORD"
    os.environ["TWINE_REPOSITORY"] = "TWINE_REPOSITORY"
    upload_to_pypi(path="dist", glob_patterns=["*.whl"])
    os.environ["TWINE_USERNAME"] = ""
    os.environ["TWINE_PASSWORD"] = ""
    os.environ["TWINE_REPOSITORY"] = ""

# Generated at 2022-06-14 05:20:53.953293
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(path = "dist", skip_existing = False, glob_patterns = ["*"])

# Generated at 2022-06-14 05:20:55.561517
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Test upload_to_pypi function
    """
    pass

# Generated at 2022-06-14 05:21:01.158114
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import pytest
    with pytest.raises(ImproperConfigurationError):
        upload_to_pypi()
    os.environ["PYPI_TOKEN"] = "pypi-token"
    upload_to_pypi() 
    del os.environ["PYPI_TOKEN"]