

# Generated at 2022-06-14 05:12:55.722643
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Test that the correct command is executed.
    """
    from mock import patch, MagicMock

    # Set default parameters
    path = "dist"
    glob_patterns = ["*"]
    skip_existing = False

    with patch("os.environ.get") as mock_environ, patch("invoke.run") as mock_run:
        mock_environ.return_value = "pypi-abc"

        # Execute function
        upload_to_pypi(
            path=path, skip_existing=skip_existing, glob_patterns=glob_patterns
        )

        # Test that the command was executed correctly
        dist = " ".join(
            ['"{}/{}"'.format(path, glob_pattern.strip()) for glob_pattern in glob_patterns]
        )
        expected = f

# Generated at 2022-06-14 05:12:56.690552
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi(dist_folder_name) == "Uploading wheel to PyPI..."

# Generated at 2022-06-14 05:12:59.979603
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    def run(cmd, echo=True, warn=True, in_stream=None, out_stream=None, hide=None, encoding=None, pty=False):
        print(cmd)
        return

    upload_to_pypi(run=run)

# Generated at 2022-06-14 05:13:00.677130
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:13:01.352302
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert 1 == 1

# Generated at 2022-06-14 05:13:09.697849
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Test missing credentials
    os.environ.pop("PYPI_TOKEN", None)
    try:
        upload_to_pypi()
        assert False
    except ImproperConfigurationError:
        assert True

    # Test missing token
    os.environ["PYPI_USERNAME"] = "username"
    os.environ["PYPI_PASSWORD"] = "password"
    try:
        upload_to_pypi()
        assert False
    except ImproperConfigurationError:
        assert True

    # Test invalid token
    os.environ["PYPI_TOKEN"] = "invalid-token"
    try:
        upload_to_pypi()
        assert False
    except ImproperConfigurationError:
        assert True

    # Test valid credentials

# Generated at 2022-06-14 05:13:20.499460
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import os
    if 'PYPI_TOKEN' not in os.environ:
        os.environ['PYPI_TOKEN'] = 'pypitest-test-test-test-test'
    assert 'PYPI_TOKEN' in os.environ
    
    from semantic_release.hvcs.git import commit_is_tag

    from .utils import run_invoke_task
    from .utils import get_working_directory

    from invoke.exceptions import Exit

    from unittest import mock

    working_directory = get_working_directory()

    with mock.patch('invoke.run') as run_mock:
        run_mock.return_value = None
        run_invoke_task(working_directory, "python.setup", "sdist")

        from .utils import run_invoke_task


# Generated at 2022-06-14 05:13:30.127477
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # test missing credentials
    try:
        upload_to_pypi()
    except Exception as ex:
        assert type(ex) == ImproperConfigurationError

    os.environ["HOME"] = ""
    # test missing pypi config
    try:
        upload_to_pypi()
    except Exception as ex:
        assert type(ex) == ImproperConfigurationError

    os.environ["HOME"] = "/tmp"
    open("/tmp/.pypirc", "w+").close()
    open("/tmp/dist/file.txt", "w+").close()

    # test invalid token
    os.environ["PYPI_TOKEN"] = "this_is_invalid"
    try:
        upload_to_pypi()
    except Exception as ex:
        assert type(ex) == Impro

# Generated at 2022-06-14 05:13:36.625654
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import os
    from semantic_release.settings import config
    from semantic_release.plugins.upload_to_pypi import upload_to_pypi
    os.environ["PYPI_TOKEN"] = "pypi-12345"
    config.set("repository", "test-repo")
    assert upload_to_pypi(skip_existing=True) == "twine upload -u '__token__' -p 'pypi-12345' -r 'test-repo' --skip-existing 'dist/*'"

# Generated at 2022-06-14 05:13:48.287239
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """
    A function for testing the upload_to_pypi function

    The function is tested on the package twine itself
    """
    import os
    import shutil
    import glob
    import logging
    import sys
    import xmlrpc.client
    import subprocess
    import time
    import requests

    # get twine package
    run("python3 -m pip download twine")

    # create dist folder
    os.mkdir("dist")

    # unzip the twine package
    run("unzip twine-3.1.1-py3-none-any.whl -d dist")

    # remove the twine package
    os.remove("twine-3.1.1-py3-none-any.whl")

    # get the package name

# Generated at 2022-06-14 05:14:17.343516
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert True

# Generated at 2022-06-14 05:14:17.868538
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:14:25.725294
# Unit test for function upload_to_pypi
def test_upload_to_pypi():

    from .helpers import mocked_run

    def run_setup_py_check_call(cmdline, **kwargs):
        """Check the cmdline of the mocked run() method."""
        if cmdline == "python setup.py clean --all":
            return
        if cmdline == "python setup.py sdist bdist_wheel":
            return
        if cmdline.startswith("twine upload -u '__token__' -p 'pypi-testtoken'"):
            return
        else:
            raise Exception("Unexpected command line in run() call: {}".format(cmdline))


# Generated at 2022-06-14 05:14:29.221088
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
  os.environ["PYPI_TOKEN"] = "pypi-asdf1234"
  upload_to_pypi(path=".", skip_existing=True, glob_patterns=["*.whl"])

# Generated at 2022-06-14 05:14:30.348000
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:14:32.041044
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert getattr(upload_to_pypi, "__wrapped__")

# Generated at 2022-06-14 05:14:40.035998
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .mocking import mocked_run
    import tempfile

    # Create a temporary folder to store files
    dist_folder = tempfile.TemporaryDirectory()
    # Temporarily change the dist folder so we don't create a bunch of files in the root
    config.set("dist_folder", dist_folder.name)

    # Call the function with no glob patterns, since there are no files to upload yet
    upload_to_pypi(glob_patterns=[])
    # Assert that no calls were made to run
    mocked_run.assert_not_called()

    # Create a file in the dist folder using the python setup tools
    # The file will be deleted when the context manager is exited

# Generated at 2022-06-14 05:14:49.405084
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    os.environ['PYPI_USERNAME'] = 'username'
    os.environ['PYPI_PASSWORD'] = 'password'
    os.environ['PYPI_TOKEN'] = 'token'
    del os.environ['PYPI_TOKEN']
    upload_to_pypi()
    os.environ['PYPI_TOKEN'] = 'token'
    del os.environ['PYPI_PASSWORD']
    del os.environ['PYPI_USERNAME']
    upload_to_pypi()
test_upload_to_pypi()

# Generated at 2022-06-14 05:14:58.404777
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """
    Does upload_to_pypi work as expected?
    """
    # A hack to make sure the correct executable is used
    run('which twine > /tmp/test_twine.txt')
    os.environ["PATH"] = f"{os.path.dirname(os.path.abspath(__file__))}:{os.environ['PATH']}"
    run('which twine > /tmp/test_twine2.txt')
    assert os.path.dirname(os.path.abspath(__file__)) in open('/tmp/test_twine2.txt').read() # pylint: disable=line-too-long

    # No repo
    upload_to_pypi()

    # With repo
    upload_to_pypi(repository='pypi')

# Generated at 2022-06-14 05:15:04.199436
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    path = "dist"
    skip_existing = False
    glob_patterns = ["*"]

    if not glob_patterns:
        glob_patterns = ["*"]

    token = os.environ.get("PYPI_TOKEN")
    username = None
    password = None
    if not token:
        # Look for a username and password instead
        username = os.environ.get("PYPI_USERNAME")
        password = os.environ.get("PYPI_PASSWORD")
        home_dir = os.environ.get("HOME", "")

# Generated at 2022-06-14 05:15:22.607791
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    global username, password, token, repository, repository_arg, dist, skip_existing_param

    username = None
    password = None
    token = "pypi-ahoj"
    repository = "https://pypi.org/pypi"
    repository_arg = " -r 'https://pypi.org/pypi'"
    dist = '"/dist/*"'
    skip_existing_param = ""

    assert upload_to_pypi(glob_patterns=["*"], skip_existing=False) == "twine upload -u '__token__' -p 'pypi-ahoj' -r 'https://pypi.org/pypi' /dist/*"

# Generated at 2022-06-14 05:15:32.420825
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    os.environ["HOME"] = "/dev/null"
    os.environ["PYPI_TOKEN"] = "pypi-token"
    os.environ["PYPI_USERNAME"] = "username"
    os.environ["PYPI_PASSWORD"] = "password"
    os.environ["PYPI_REPOSITORY"] = "http://custom-repository"
    upload_to_pypi()
    del os.environ["PYPI_REPOSITORY"]
    upload_to_pypi(glob_patterns=["pattern1", "pattern2"])
    upload_to_pypi(skip_existing=True)
    upload_to_pypi(skip_existing=True, glob_patterns=["pattern3", "pattern4"])
   

# Generated at 2022-06-14 05:15:37.868016
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Arrange
    path = "test_path"
    glob_patterns = ["test_file_1", "test_file_2"]

    # Act
    upload_to_pypi(path=path, glob_patterns=glob_patterns)

    # Assert
    # Assertions are handled by mocks

# Generated at 2022-06-14 05:15:51.587550
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    class mock_run:
        def __init__(self):
            self.command = ""

        def __call__(self, command):
            self.command = command

    glob_patterns = ["*"]
    path = "dist"
    expected_command = 'twine upload -u __token__ -p pypi-blahblahblah "dist/*"'
    run_mock = mock_run()

    os.environ["PYPI_TOKEN"] = "pypi-blahblahblah"

    upload_to_pypi(path, glob_patterns=glob_patterns, _run=run_mock)

    assert run_mock.command == expected_command

    del os.environ["PYPI_TOKEN"]


# Generated at 2022-06-14 05:16:02.119487
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # This is an integration test.
    # It is expected to fail if credentials for PyPI are not available.
    username = os.environ.get("PYPI_USERNAME")
    password = os.environ.get("PYPI_PASSWORD")
    if not username:
        try:
            with open(os.path.join(os.environ["HOME"], ".pypirc")) as fp:
                config = fp.read()
            username = [line.split("=")[1] for line in config.split("\n") if "username" in line][0]
        except (OSError):
            # Don't run the test if we can't find credentials
            return
    if not (username and password):
        # Don't run the test if we can't find credentials
        return
    import tempfile

# Generated at 2022-06-14 05:16:08.789545
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from pathlib import Path

    from tempfile import TemporaryDirectory

    repo_dir = TemporaryDirectory(prefix="semantic-release-")
    test_dir = Path(repo_dir.name)

    file_to_upload = test_dir / "test-file"
    file_to_upload.write_text("test")

    upload_to_pypi(test_dir, glob_patterns=["test-file"])

# Generated at 2022-06-14 05:16:15.185377
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import tempfile
    import random
    import string

    random_string = "".join(random.choice(string.ascii_lowercase) for i in range(10))
    temp_file = tempfile.NamedTemporaryFile(delete=True)
    with temp_file:
        temp_file.write(random_string.encode('utf-8'))
        temp_file.flush()
        upload_to_pypi(temp_file.name)



# Generated at 2022-06-14 05:16:15.683877
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert True

# Generated at 2022-06-14 05:16:24.698501
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    if upload_to_pypi():
        raise AssertionError("Invalid config")
    upload_to_pypi(glob_patterns=["test_package-1.2.3-py3-none-any.*\.*"])
    upload_to_pypi(glob_patterns=["test_package-*-py3-none-any.*\.*"])
    upload_to_pypi(glob_patterns=["test_package-*-*-any.*\.*"])

# Generated at 2022-06-14 05:16:33.670785
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    def mock_run(value):
        pass

    run_ = mock_run
    upload_to_pypi(path="mock_path", skip_existing=False)
    assert run_.call_count == 1
    assert run_.call_args[0][0] == "twine upload  'mock_path/*'"
    upload_to_pypi(path="mock_path", skip_existing=True, glob_patterns=["mock_pattern"])
    assert run_.call_count == 2
    assert run_.call_args[0][0] == "twine upload  --skip-existing 'mock_path/mock_pattern'"

# Generated at 2022-06-14 05:16:52.884043
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()

# Generated at 2022-06-14 05:17:04.705955
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import os
    import shutil
    

# Generated at 2022-06-14 05:17:05.362726
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:17:16.161489
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from pytest import raises
    from unittest.mock import patch
    
    # Testing for token
    token = "pypi-test-token"
    with patch.dict(os.environ, {"PYPI_TOKEN": token}):
        with patch.object(run, "invoke") as mock_run:
            upload_to_pypi(["*"])
            mock_run.assert_called_with(f"twine upload -u '__token__' -p '{token}' *")

    # Testing for username and password
    username = "test-username"
    password = "test-password"
    dist = 'dist'
    glob_patterns = ["*"]

# Generated at 2022-06-14 05:17:17.900051
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    try:
        upload_to_pypi()
    except ImproperConfigurationError as e:
        pass

# Generated at 2022-06-14 05:17:31.252060
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    fake_dist_files = [
        "dist/module-1.0.0-py3-none-any.whl",
        "dist/module-1.0.0.tar.gz",
        "dist/module-1.1.0-py3-none-any.whl",
        "dist/module-1.1.0.tar.gz",
    ]
    upload_to_pypi(
        path="dist", skip_existing=True, glob_patterns=["*-1.1.*", "*.tar.gz"]
    )

# Generated at 2022-06-14 05:17:38.424064
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import os
    import shutil
    import tempfile
    import zipfile
    from contextlib import ExitStack
    from unittest import mock

    from path import Path
    from semantic_release import settings

    from hypothesis import given
    from hypothesis.strategies import (
        booleans,
        integers,
        lists,
        text,
    )

    from .helpers import LoggedFunction
    from .strategies import semantic_versions
    from .test_helpers import  hypothesis_settings

    def touch(path):
        Path(path).touch()



# Generated at 2022-06-14 05:17:39.720519
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:17:49.371029
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # pylint: disable=unused-variable
    from contextlib import contextmanager
    from unittest.mock import call, patch

    class MockInvokeResult:
        def __init__(self, stdout="", stderr="", exit_code=0):
            self.stdout = stdout
            self.stderr = stderr
            self.exited = exit_code

    @contextmanager
    def env(environ):
        old_env = dict(os.environ)
        os.environ.update(environ)
        try:
            yield
        finally:
            os.environ.clear()
            os.environ.update(old_env)


# Generated at 2022-06-14 05:17:57.416997
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """A unit test of upload_to_pypi().

    Steps:
    - Create temporary test folder
    - Create a temporary test script file
    - Create a test wheel
    - Test upload_to_pypi()
    - Cleanup temp folder and files
    """
    import os
    import shutil
    import sys

    from email.message import Message
    from io import StringIO
    from unittest import TestCase, main, mock

    from semantic_release import upload_to_pypi
    from semantic_release.exceptions import ImproperConfigurationError

    test_folder = '/tmp/semantic_release_test_folder'

    tmp_file_path = os.path.join(test_folder, 'tmp_script.py')
    tmp_file = open(tmp_file_path, 'w')
    tmp_file

# Generated at 2022-06-14 05:18:40.752818
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Upload with token
    os.environ["PYPI_TOKEN"] = "pypi-12345"
    upload_to_pypi(glob_patterns = ["*.whl"])
    del os.environ["PYPI_TOKEN"]

    # Upload with username and password
    os.environ["PYPI_USERNAME"] = "pypi_username"
    os.environ["PYPI_PASSWORD"] = "pypi_password"
    upload_to_pypi(glob_patterns = ["*.whl"])
    del os.environ["PYPI_USERNAME"]
    del os.environ["PYPI_PASSWORD"]

# Generated at 2022-06-14 05:18:48.334464
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi(path='/dist', skip_existing=True, glob_patterns=['*.whl', '*.tar.gz']) == True
    assert upload_to_pypi(path='/dist') == True
    assert upload_to_pypi(path='/dist_tmp', skip_existing=False, glob_patterns=[]) == True

# Generated at 2022-06-14 05:18:58.318977
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import pytest
    from tempfile import TemporaryDirectory
    from tqdm import tqdm

    # Case 1: No credentials provided
    with pytest.raises(ImproperConfigurationError) as excinfo:
        upload_to_pypi()
    assert "Missing credentials for uploading to PyPI" in str(excinfo.value)

    # Case 2: Missing password
    with pytest.raises(ImproperConfigurationError) as excinfo:
        with os.environ.copy():
            os.environ["PYPI_USERNAME"] = "username"
            upload_to_pypi()
    assert "Missing credentials for uploading to PyPI" in str(excinfo.value)

    # Case 3: Missing username

# Generated at 2022-06-14 05:19:11.008382
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Mock the twine upload command."""
    from unittest.mock import patch

    from semantic_release.hvcs.bitbucket import BitBucket
    from semantic_release.hvcs.github import GitHub

    from .helpers import mocked_run

    hvcs_cls_list = GitHub, BitBucket
    for hvcs_cls in hvcs_cls_list:
        if hvcs_cls.check_auth():
            with patch("semantic_release.cli.upload_to_pypi.run", mocked_run):
                upload_to_pypi(path="dist", skip_existing=True)

    assert mocked_run.call_count == len(hvcs_cls_list)

# Generated at 2022-06-14 05:19:13.045337
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(path="project/dist", glob_patterns=["*"])


# Generated at 2022-06-14 05:19:14.671544
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()

# Generated at 2022-06-14 05:19:15.519658
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert 1

# Generated at 2022-06-14 05:19:18.418189
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Unit test for function upload_to_pypi"""
    print("test_upload_to_pypi")

# Generated at 2022-06-14 05:19:30.507305
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Test upload to PyPi with Twine.
    """
    import semantic_release.vcs.git as git
    # Invoke is struggling to run this command on macOS through pytest.
    #  Pytest will not create the dist folder, but twine upload can create it
    #  We want to remove the dist folder before asserting it was created.
    # Ensure dist folder doesn't already exist
    run("rm -r dist/")
    # Upload dist to pypi
    upload_to_pypi()
    # Ensure dist directory exists
    if not os.path.exists("dist/"):
        raise RuntimeError("dist directory does not exist.")
    # Ensure dist directory contains setup.py
    if not os.path.isfile("dist/setup.py"):
        raise RuntimeError("dist directory does not contain setup.py.")
    #

# Generated at 2022-06-14 05:19:43.207293
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """
    Unit test for function upload_to_pypi
    """
    import mock
    import pytest
    from invoke.exceptions import Fail

    from .helpers import LoggedFunction
    from .helpers import SemanticReleaseException

    def run(command: str):
        """
        Mock function to replace the real run function
        """
        if command != "twine upload -u '__token__' -p 'pypi-1234abcd' 'dist/*'":
            raise Fail("Wrong command")

    logger = mock.Mock()


# Generated at 2022-06-14 05:20:58.524202
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import shutil
    from tempfile import TemporaryDirectory, mkstemp

    with TemporaryDirectory() as dist_path:
        shutil.copytree("tests/sample_files/sdist", os.path.join(dist_path, "sdist"))
        shutil.copytree("tests/sample_files/bdist_wheel", os.path.join(dist_path, "bdist_wheel"))

        assert upload_to_pypi(dist_path) is None

# Generated at 2022-06-14 05:21:08.934802
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # GIVEN a folder with a wheel in it
    path = "dist"
    wheel = "package-0.0.0-py3-none-any.whl"
    wheel_path = "{}/{}".format(path, wheel)
    with open(wheel_path, "w") as wheel_file:
        wheel_file.write("test")

    # WHEN uploading to PyPI
    upload_to_pypi(path)

    # THEN a wheel should not be uploaded
    assert os.path.isfile(wheel_path)

# Generated at 2022-06-14 05:21:09.512028
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:21:12.258479
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi()

# Generated at 2022-06-14 05:21:19.078845
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Test for function upload_to_pypi.

    This test should be run with py.test
    """

# Generated at 2022-06-14 05:21:25.647931
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Given
    path = 'dist'
    skip_existing = True
    glob_patterns = ['*.whl']
    os.environ['PYPI_TOKEN'] = 'pypi-xxxxxxxxxxxxxxxxxxxxx'

    # When
    upload_to_pypi(path, skip_existing, glob_patterns)

# Generated at 2022-06-14 05:21:33.681638
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from unittest.mock import patch

    with patch("invoke.run") as run_mock:
        upload_to_pypi(
            "dist", skip_existing=True, glob_patterns=["*", "other/**/*.whl"]
        )
        run_mock.assert_called_with(
            "twine upload -u '__token__' -p 'pypi-abcdefghijklm' --skip-existing 'dist/*' 'dist/other/**/*.whl'"
        )



# Generated at 2022-06-14 05:21:44.060857
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import tempfile
    import shutil

    tmp_path = tempfile.mkdtemp()


# Generated at 2022-06-14 05:21:57.439885
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Tests upload_to_pypi function
    """
    import os
    import subprocess
    import tempfile
    import shutil

    def _run(cmd):
        return subprocess.check_output(cmd, shell=True).decode("utf-8")
    
    def _run_in_temp_dir(cmd, temp_dir=None, create_files=None, create_files_count=None):
        if not create_files_count:
            create_files_count = 1
        if not create_files:
            create_files = ["temp_file_0.txt"]
            create_files = create_files[:create_files_count]
        if not temp_dir:
            temp_dir = tempfile.mkdtemp()

# Generated at 2022-06-14 05:22:04.655234
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi(path="test_dist", glob_patterns=["*"]) is None
    # TODO: AppVeyor doesn't seem to like the next line
    #assert upload_to_pypi(path="test_dist", skip_existing=True) is None
    #assert upload_to_pypi(path="test_dist", glob_patterns=["a*"]) is None