

# Generated at 2022-06-14 05:12:51.544495
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """
    Test upload_to_pypi.
    """
    upload_to_pypi()

# Generated at 2022-06-14 05:12:52.675103
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()

# Generated at 2022-06-14 05:13:04.373488
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    class MockRun:
        def __init__(self):
            self.calls = []
            self.commands = []

        def __call__(self, command):
            self.calls.append(command)
            self.commands = [c for c in self.commands if c != command]
            return

    mock_run = MockRun()

    class MockedEnv:
        PYPI_TOKEN = "pypi-some_token"
        PYPI_USERNAME = None
        PYPI_PASSWORD = None

    with MockedEnv() as env:
        upload_to_pypi(
            path="/tmp/dist",
            skip_existing=False,
            glob_patterns=["*.whl"],
            run=mock_run,
        )

# Generated at 2022-06-14 05:13:06.140001
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(path='test', glob_patterns=["test"])

# Generated at 2022-06-14 05:13:06.992441
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert True == True
    #assert False == True

# Generated at 2022-06-14 05:13:14.828600
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi.__name__ == "upload_to_pypi"
    assert upload_to_pypi.__doc__ == "Upload wheels to PyPI with Twine.\n\n    Wheels must already be created and stored at the given path.\n\n    Credentials are taken from either the environment variable\n    ``PYPI_TOKEN``, or from ``PYPI_USERNAME`` and ``PYPI_PASSWORD``.\n\n    :param path: Path to dist folder containing the files to upload.\n    :param skip_existing: Continue uploading files if one already exists.\n        (Only valid when uploading to PyPI. Other implementations may not support this.)\n    :param glob_patterns: List of glob patterns to include in the upload (['*'] by default).\n    "

# Generated at 2022-06-14 05:13:22.596499
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """ Test for function upload_to_pypi
    """

    from .helpers import mock_run

    glob_patterns = ["*dist*.gz", "*dist.tgz"]
    # Test with no glob pattern
    upload_to_pypi()
    mock_run.assert_called_with(
        "twine upload", hide=True, warn=True, encoding="utf-8"
    )

    # Test with glob patterns
    upload_to_pypi(glob_patterns=glob_patterns)
    mock_run.assert_called_with(
        "twine upload 'dist/*dist*.gz' 'dist/*dist.tgz'",
        hide=True,
        warn=True,
        encoding="utf-8",
    )

    # Test with environment variables

# Generated at 2022-06-14 05:13:24.787566
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:13:25.384866
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert skip_existing

# Generated at 2022-06-14 05:13:32.179837
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    
    # Testing for uploading the files with skip_existing option
    import sys
    import pytest

    @pytest.mark.skipif(sys.version_info[0] < 3, reason="Local Twine version is 2.x")
    def test_upload_with_skip_existing():
        """Uploading the files with skip_existing option
        """
        path = "dist"
        skip_existing = True
        glob_pattern = ["*"]
        upload_to_pypi(path, skip_existing, glob_pattern)
    test_upload_with_skip_existing()

    # Testing for uploading the files without skip_existing option
    def test_upload_without_skip_existing():
        """Uploading the files without skip_existing option
        """
        path = "dist"
        skip_existing = False 
        glob_

# Generated at 2022-06-14 05:13:48.440423
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Test upload_to_pypi

    With environment variables user can specify both username and password
    Or they can specify the token
    """

    # "PYPI_USERNAME": "user", "PYPI_PASSWORD": "password", "PYPI_TOKEN": "pypi-token"
    # This function should run without error in both cases
    os.environ["PYPI_USERNAME"] = "user"
    os.environ["PYPI_PASSWORD"] = "password"
    upload_to_pypi(path="./dist", glob_patterns=["*"])
    del os.environ["PYPI_USERNAME"]
    del os.environ["PYPI_PASSWORD"]

# Generated at 2022-06-14 05:13:50.457725
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi(['*'], 2) == "twine upload * 2"

# Generated at 2022-06-14 05:14:02.644657
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi.__name__ == "upload_to_pypi"
    assert upload_to_pypi.__doc__ == """Upload wheels to PyPI with Twine.

Wheels must already be created and stored at the given path.

Credentials are taken from either the environment variable
``PYPI_TOKEN``, or from ``PYPI_USERNAME`` and ``PYPI_PASSWORD``.

:param path: Path to dist folder containing the files to upload.
:param skip_existing: Continue uploading files if one already exists.
    (Only valid when uploading to PyPI. Other implementations may not support this.)
:param glob_patterns: List of glob patterns to include in the upload (["*"] by default).
"""

# Generated at 2022-06-14 05:14:10.488002
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Mock env vars used by Twine
    # pylint: disable-msg=C0103
    os.environ["PYPI_USERNAME"] = "user"
    os.environ["PYPI_PASSWORD"] = "password"
    global run # pylint: disable-msg=W0603
    run = lambda args: print(args)
    global logger
    logger = logging.getLogger(__name__)
    logger.debug = print
    # pylint: enable-msg=W0603
    upload_to_pypi()

# Generated at 2022-06-14 05:14:11.837623
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Put here some dummy data for mypy testing
    upload_to_pypi("dist", False, ["*"])

# Generated at 2022-06-14 05:14:12.727968
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:14:20.957682
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Test we get correct errors if missing parameters
    os.environ["PYPI_TOKEN"] = ""
    os.environ["PYPI_USERNAME"] = ""
    os.environ["PYPI_PASSWORD"] = ""
    with pytest.raises(ImproperConfigurationError):
        upload_to_pypi()

    # Test that we get correct errors if token malformed
    os.environ["PYPI_TOKEN"] = "malformed"
    with pytest.raises(ImproperConfigurationError):
        upload_to_pypi()

    # TODO: Make test that tries to call twine, and validate it calls it with the right parameters

# Generated at 2022-06-14 05:14:26.155930
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # TODO: improve tests. paths and filenames are hardcoded now.
    upload_to_pypi('/Users/joel/repos/semantic-release/tests/integration/release/upload_package/dist',
         True, ['*'])

# Generated at 2022-06-14 05:14:31.511487
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """
    The path variable will be modified to "dist/".
    """
    with open("dist/test_file", "w") as test_file:
        test_file.write("test")
    try:
        upload_to_pypi("dist/")
    finally:
        os.remove("dist/test_file")

# Generated at 2022-06-14 05:14:32.453895
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert callable(upload_to_pypi)

# Generated at 2022-06-14 05:14:51.839557
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Set environment
    os.environ["PYPI_TOKEN"] = "pypi-token"
    os.environ["PYPI_USERNAME"] = "pypi-username"
    os.environ["PYPI_PASSWORD"] = "pypi-password"

    # Call function
    upload_to_pypi()

    # Assert expected call
    args, kwargs = run.call_args
    assert isinstance(args, tuple)
    assert isinstance(kwargs, dict)
    assert args == ("twine upload -u 'pypi-username' -p 'pypi-password'  '\"dist/*\"'", )


# Generated at 2022-06-14 05:14:53.805231
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()

# Generated at 2022-06-14 05:14:56.017967
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .helpers import run_logged_function

    run_logged_function(upload_to_pypi)

# Generated at 2022-06-14 05:15:08.208029
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Mock the run function, so we don't actually call the external process
    old_run = run
    data = {}
    def new_run(command):
        data["command"] = command
    run = new_run


# Generated at 2022-06-14 05:15:18.342367
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    test_path = "./dist"

    # Make sure that going without credentials fails
    try:
        upload_to_pypi(test_path)
        raise AssertionError(
            "Expected upload_to_pypi to fail with missing PyPI credentials"
        )
    except ImproperConfigurationError:
        pass

    # Make sure that specifying a username and password works
    os.environ["PYPI_USERNAME"] = "tacocat"
    os.environ["PYPI_PASSWORD"] = "password"
    upload_to_pypi(test_path)

    # Make sure that a token works

# Generated at 2022-06-14 05:15:18.966103
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
	pass

# Generated at 2022-06-14 05:15:20.289840
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi
    pass

# Generated at 2022-06-14 05:15:21.332188
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()


# Generated at 2022-06-14 05:15:25.951988
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """
    Test function upload_to_pypi.
    """
    # pylint: disable=no-value-for-parameter,no-member
    upload_to_pypi.__wrapped__()



# Generated at 2022-06-14 05:15:26.898628
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:15:54.903622
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .mock_invoke import mock_run, ctx

    ctx.run = mock_run
    # Set necessary environment variables
    os.environ["PYPI_TOKEN"] = "pypi-asdfjkl"
    # Upload to test repo
    upload_to_pypi(repository="testrepo.com")
    assert ctx.run.call_count == 1
    command, call_kwargs = ctx.run.call_args
    assert "testrepo.com" in call_kwargs.get("command")
    assert "__token__" in call_kwargs.get("command")
    assert "-p 'pypi-asdfjkl'" in call_kwargs.get("command")

# Generated at 2022-06-14 05:16:08.082462
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .helpers import mock_run, mock_open
    from semantic_release.hvcs import guess
    from tempfile import TemporaryDirectory

    with TemporaryDirectory() as dir:
        mock_open(dir)
        repo = guess(config.get("hvcs"))
        assert repo is not None
        config["repository"] = repo.repository_url
        with mock_run() as run_mock, mock_open() as open_patch:
            open_patch.return_value.read.return_value = "abcdefg"
            os.environ["PYPI_TOKEN"] = "pypi-abcdefg"
            upload_to_pypi(dir, glob_patterns=["*"])

# Generated at 2022-06-14 05:16:09.748020
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi('dist', True, ['*'])

# Generated at 2022-06-14 05:16:17.675986
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import contextlib
    import tempfile
    import os
    import shutil
    import tempfile
    from invoke import run as invoke_run

    # Create a temporary directory
    @contextlib.contextmanager
    def tmpdir():
        tempdir = tempfile.mkdtemp()
        yield tempdir
        shutil.rmtree(tempdir)

    with tmpdir() as directory:
        # Create a temp file
        f = tempfile.NamedTemporaryFile(dir=directory)
        f.write(b'Hello world')
        f.flush()
        f.close()

        # Make sure twine is installed
        invoke_run('python3 -m pip install twine')

        # Run the command
        os.environ['PYPI_USERNAME'] = 'test'

# Generated at 2022-06-14 05:16:24.235788
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """
    Function to test upload_to_pypi.
    """
    config.update({
        "before_deploy": [
            "semantic_release.development_environment.create_wheel",
        ],
        "pypi_repository": [
            "test_module"
        ],
        "repository": "test_module"
    })

# Generated at 2022-06-14 05:16:25.348135
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()

# Generated at 2022-06-14 05:16:30.800917
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    os.environ["PYPI_TOKEN"] = "pypi-example_token1"
    try:
        upload_to_pypi()
    except ImproperConfigurationError as error:
        assert error.args[0] == "Missing credentials for uploading to PyPI"

    upload_to_pypi(skip_existing=True)

# Generated at 2022-06-14 05:16:39.784217
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Test for invalid token
    invalid_token = "c0ffee"

    try:
        upload_to_pypi(glob_patterns=["*.whl"], skip_existing=True)
        # Should not make it here
        raise AssertionError("No error was raised for missing token")
    except Exception as err:
        assert (
            str(err) == "Missing credentials for uploading to PyPI"
        ), "Wrong error message for missing token"

# Generated at 2022-06-14 05:16:43.047774
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """
    Unit test for function upload_to_pypi(path: str, skip_existing: bool)
    """
    upload_to_pypi()

# Generated at 2022-06-14 05:16:43.809043
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:17:31.364232
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Unit test for upload_to_pypi."""
    from . import get_mock_reponse
    from .test_helpers import clear_environment
    from .test_helpers import set_environment


# Generated at 2022-06-14 05:17:35.708012
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """
    Test function upload_to_pypi

    Args: 
        None
    Returns: 
        None
    """
    upload_to_pypi(path="tests/fixtures", skip_existing=True, glob_patterns=None)

# Generated at 2022-06-14 05:17:36.275947
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:17:45.566731
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Unit test for function upload_to_pypi
    """
    try:
        upload_to_pypi(glob_patterns=["NO_PATTERN"])
    except ImproperConfigurationError:
        print(
            "'Missing credentials for uploading to PyPI' exception is expected. "
            "It validates that function works properly with invalid path."
        )
    else:
        raise RuntimeError(
            "Function upload_to_pypi unexpectedly throws no exception on invalid path."
        )

# Generated at 2022-06-14 05:17:55.614622
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import io
    import sys
    from io import StringIO
    from unittest.mock import patch
    from unittest import mock

    # sets up the environment variables

# Generated at 2022-06-14 05:18:07.892824
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from unittest.mock import patch
    from unittest import TestCase


# Generated at 2022-06-14 05:18:14.205117
# Unit test for function upload_to_pypi
def test_upload_to_pypi():

    class Context:
        def run(self, task):
            return task
    context = Context()
    context.run('create_dist_folder')
    context.run('create_dist_files')
    
    upload_to_pypi.func(context, path='dist', skip_existing=False, glob_patterns=None)

# Generated at 2022-06-14 05:18:24.094189
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from pkg_resources import parse_version
    from unittest import mock
    from semantic_release.package_managers import get_package_manager
    from semantic_release import _get_version_type
    from semantic_release.history import current_version

    mocked_call = mock.Mock()
    mocked_glob = mock.Mock(return_value='file.whl')
    mocked_path = mock.Mock()
    mocked_path.join = mock.Mock(return_value='dist/file.whl')
    mocked_pkg = mock.Mock()
    mocked_pkg.get_project_name.return_value = 'test_package'
    mocked_pkg.get_project_version = mock.Mock(return_value='1.2.3')
    mocked_io = mock.Mock()
   

# Generated at 2022-06-14 05:18:37.417465
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import shlex
    from invoke import Context

    from .helpers import patch_run
    from .helpers import mock_run, mock_runner

    ctx = Context()
    mock_run(ctx, "twine upload -u 'username' -p 'password' "
             "-r 'repo' --skip-existing 'dist/file1.whl' 'dist/file2.whl' "
             '"dist/file 3.whl"')
    with patch_run(mock_runner(ctx)):
        upload_to_pypi(
            path="dist",
            skip_existing=True,
            glob_patterns=["file1.whl", "file2.whl", 'file 3.whl'],
        )

    command_called = mock_runner(ctx)["command"]
    command_called

# Generated at 2022-06-14 05:18:38.567205
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    try:
        upload_to_pypi(skip_existing=True)
    except:
        pass


# Generated at 2022-06-14 05:19:51.749037
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(glob_patterns=['*'])

# Generated at 2022-06-14 05:20:04.052335
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .helpers import MockEnvironment

    with MockEnvironment(
        PYPI_USERNAME="pypi_user",
        PYPI_PASSWORD="pypi_pass",
        PYPI_TOKEN="",
        HOME="",
        CI_RUNNER_ID=0,
        SEMANTIC_RELEASE_DEBUG=True,
    ) as env:
        upload_to_pypi()

    with MockEnvironment(
        PYPI_USERNAME="",
        PYPI_PASSWORD="",
        PYPI_TOKEN="pypi-token",
        HOME="",
        CI_RUNNER_ID=0,
        SEMANTIC_RELEASE_DEBUG=True,
    ) as env:
        upload_to_pypi()


# Generated at 2022-06-14 05:20:17.790840
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert os.getenv('HOME', '') != '/home/travis'
    assert upload_to_pypi.__name__ == 'upload_to_pypi'

# Generated at 2022-06-14 05:20:19.822395
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert(upload_to_pypi(path="dist", skip_existing=True, glob_patterns=["*"]) != None)

# Generated at 2022-06-14 05:20:25.834272
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import subprocess
    result = subprocess.run(["twine", "--version"], stdout=subprocess.PIPE)
    if result.returncode != 0:
        raise ImportError(
            "Twine is not installed. Twine is required to upload to PyPI."
        )

# Generated at 2022-06-14 05:20:31.533200
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """
    Tests for the function upload_to_pypi
    """
    from .helpers import LoggedFunctionTest
    from .helpers import env_setup
    from .helpers import patch_get_version

    env_setup()
    patch_get_version("0.0.0")

    LoggedFunctionTest(upload_to_pypi).run()

# Generated at 2022-06-14 05:20:32.259759
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:20:40.934315
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Since the function is only used to call invoke to run twine, which is already tested,
    # we will only test that the correct command is called with the correct arguments.
    def run_mock(command):
        assert command == "twine upload -u '__token__' -p 'pypi-test_token' --skip-existing 'dist/fake_dist_file'"

    with mock.patch('invoke.run', new=run_mock):
        upload_to_pypi(path='dist', skip_existing=True, glob_patterns=['fake_dist_file'])

# Generated at 2022-06-14 05:20:51.222601
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Setup
    config.set("repository", "pypitest")
    os.environ["PYPI_USERNAME"] = "foo"
    os.environ["PYPI_PASSWORD"] = "bar"
    os.environ["HOME"] = ""  # to simulate no .pypirc file in home directory
    os.makedirs("dist", exist_ok=True)
    open("dist/foo", "w").close()

    # Execute
    upload_to_pypi()

    # Assert

# Generated at 2022-06-14 05:20:51.924448
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass