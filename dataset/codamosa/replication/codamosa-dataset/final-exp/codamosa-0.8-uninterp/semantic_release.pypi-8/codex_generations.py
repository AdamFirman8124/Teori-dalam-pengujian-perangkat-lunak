

# Generated at 2022-06-14 05:13:01.518477
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import os
    import shutil
    import tempfile

    # GIVEN
    # A local temporary folder
    tempdir = tempfile.mkdtemp()
    # That temporary folder contains a temp copy of the setup file
    setupfile = os.path.join(tempdir, "setup.py")

    with open(setupfile, "w") as setup_file:
        setup_file.write("""from setuptools import setup

setup(
    name="Project X",
    packages=["src"],
)""")


    # WHEN
    # The dist folder is created and setup.py is run
    distdir = os.path.join(tempdir, "dist")
    os.mkdir(distdir)


# Generated at 2022-06-14 05:13:02.232697
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:13:03.253124
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # TODO: Test is not fully implemented
    pass

# Generated at 2022-06-14 05:13:04.242474
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi("dist")

# Generated at 2022-06-14 05:13:12.555626
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .helpers import _get_changed_files
    from .version import get_version

    version = get_version(
        path=config["files"]["version_source"],
        version_variable=config["files"]["version_variable"],
    )
    changed_files = _get_changed_files(base_url=config["repository"]["base_url"])
    if changed_files:

        # Push tag
        tag_message = "Version " + version
        upload_to_pypi(
            path="dist",
            skip_existing=False,
            glob_patterns=config["upload"].get("glob_patterns", [""]),
        )


test_upload_to_pypi()

# Generated at 2022-06-14 05:13:20.785870
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .test_helpers import get_temp_file_name, MockContext
    temp_path = get_temp_file_name()
    c = MockContext()
    upload_to_pypi(
        path=temp_path,
        glob_patterns=[
            "test.txt",
            "a*b",
        ],
        skip_existing=True,
    )
    c.run.assert_called_once_with(
        "twine upload -u '__token__' -p 'pypi-xxx' --skip-existing 'test.txt' 'a*b'"
    )

# Generated at 2022-06-14 05:13:30.328642
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Test that the twine upload command is being called correctly.
    """
    from mock import patch
    from .helpers import Command

    with patch.object(Command, "run") as run_mock:
        home_dir = os.environ.get("HOME", "")
        os.environ["HOME"] = "fake/home"
        with open(os.path.join(os.environ.get("HOME", ""), ".pypirc"), "w") as f:
            f.write("[distutils]\n")
            f.write("index-servers=pypi")
            f.write("\n")
            f.write("[pypi]\n")
            f.write("repository = https://pypi.org/legacy/\n")

# Generated at 2022-06-14 05:13:30.925019
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert False

# Generated at 2022-06-14 05:13:38.696304
# Unit test for function upload_to_pypi

# Generated at 2022-06-14 05:13:39.403277
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:13:45.717094
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """This function is not tested in integration tests, but
    is tested in the unit tests.  Prefix with "test_" any
    function that you want to be tested automatically by
    the unit tests.
    """
    assert False

# Generated at 2022-06-14 05:13:48.201311
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(path="tests/fixtures/wheel")

# Generated at 2022-06-14 05:13:55.232600
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Create a distribution file
    path = "twine_test"
    os.makedirs(path)
    distribution_file_path = os.path.join(path, "index.html")
    with open(distribution_file_path, 'w') as f:
        f.write("A simple index page.")

    upload_to_pypi(path)

    # Remove distribution file
    os.remove(distribution_file_path)
    os.rmdir(path)


# Generated at 2022-06-14 05:14:06.167443
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import tempfile
    import shutil
    from invocations.testing import test
    from semantic_release.contrib.pypi import upload_to_pypi
    target = tempfile.mkdtemp()
    tempdir = tempfile.mkdtemp()
    open('{}/foo.whl'.format(tempdir), 'a').close()
    os.mkdir('{}/bar'.format(tempdir))
    open('{}/bar/baz.whl'.format(tempdir), 'a').close()

# Generated at 2022-06-14 05:14:17.176610
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi("test_path") == \
        "twine upload -u 'pypi_token' -p 'pypi-test' --skip-existing 'test_path/*'"
    assert upload_to_pypi("test_path", skip_existing=True) == \
        "twine upload -u 'pypi_token' -p 'pypi-test' --skip-existing 'test_path/*'"
    assert upload_to_pypi("test_path", glob_patterns=["*", "*.*"]) == \
        "twine upload -u 'pypi_token' -p 'pypi-test' --skip-existing 'test_path/*' 'test_path/*.*'"

# Generated at 2022-06-14 05:14:24.356443
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    cred_dir = os.path.dirname(os.path.abspath(__file__)) + "/credentials"
    token_file = cred_dir + "/pypi"
    credentials = open(token_file).read().split()
    token = credentials[0]
    username = credentials[1].split("=")[1]

    os.environ["PYPI_TOKEN"] = token
    os.environ["PYPI_USERNAME"] = username
    upload_to_pypi(path="test", skip_existing=True, glob_patterns=["*"])
    del os.environ["PYPI_TOKEN"]
    del os.environ["PYPI_USERNAME"]

# Generated at 2022-06-14 05:14:25.571813
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()

# Generated at 2022-06-14 05:14:27.663042
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(path="tests/test_files/dist", skip_existing=True)

# Generated at 2022-06-14 05:14:34.181328
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    os.environ["PYPI_TOKEN"] = "pypi-abcdefghijk"

    upload_to_pypi(skip_existing=True)
    command = run.calls[-1].args[0]

    assert command.startswith("twine upload -u '__token__' -p 'pypi-abcdefghijk' --skip-existing")
    assert '"dist/pytest_plugin.py"' in command

# Generated at 2022-06-14 05:14:36.049298
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi("dist")
    upload_to_pypi("dist", skip_existing=True)

# Generated at 2022-06-14 05:14:52.639547
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Mock environment variables
    os.environ["PYPI_TOKEN"] = "pypi-123"

    # Mock run.run
    def mock_run(command: str, **kwargs):
        assert command.startswith("twine upload")
        assert command.find("__token__") != -1
        assert command.find("pypi-123") != -1
        assert command.find("dist/file") != -1
    run.run = mock_run

    # Execute
    upload_to_pypi(path="dist", glob_patterns=["file"])

# Generated at 2022-06-14 05:14:53.636981
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:14:55.844735
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(path="dist", skip_existing=True, glob_patterns=["*"])

# Generated at 2022-06-14 05:14:59.232036
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()
    upload_to_pypi(glob_patterns=["test"])

if __name__ == '__main__':
    test_upload_to_pypi()

# Generated at 2022-06-14 05:15:00.359322
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()

# Generated at 2022-06-14 05:15:06.934998
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    token = "foo"
    repository = "test"
    username = "user"
    password = "pass"
    expected_upload_to_pypi_token = (
        f'twine upload -u "__token__" -p "{token}" -r "{repository}" "*"'
    )

# Generated at 2022-06-14 05:15:17.524470
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .helpers import set_env_vars

    set_env_vars(PYPI_USERNAME="test-username", PYPI_PASSWORD="test-password")
    assert upload_to_pypi() == "twine upload -u 'test-username' -p 'test-password' 'dist/'", "Failed to upload to PyPI."

    set_env_vars(PYPI_TOKEN="pypi-test-token")
    assert upload_to_pypi() == "twine upload -u '__token__' -p 'pypi-test-token' 'dist/'", "Failed to upload to PyPI."

    set_env_vars(repository="test-repository")

# Generated at 2022-06-14 05:15:19.910012
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(path="path/to/dist", skip_existing=True, glob_patterns=["*"])

# Generated at 2022-06-14 05:15:21.331734
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    result = run("twine upload --help")
    assert result.ok is True

# Generated at 2022-06-14 05:15:23.552391
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi('dist', True, ['mock_distribution'])

# Generated at 2022-06-14 05:15:51.918401
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Token or username and password required
    try:
        upload_to_pypi()
    except ImproperConfigurationError as e:
        assert str(e) == "Missing credentials for uploading to PyPI"
    else:
        assert False

    # Token should start with "pypi-"
    try:
        upload_to_pypi(token="PYPI_TOKEN")
    except ImproperConfigurationError as e:
        assert str(e) == 'PyPI token should begin with "pypi-"'
    else:
        assert False

    # Repository should be passed to twine
    upload_to_pypi(
        token="pypi-1k5r5d5l5r5", username="PYPI_USERNAME", password="PYPI_PASSWORD"
    )
    os.en

# Generated at 2022-06-14 05:16:02.392619
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Test assertions for `upload_to_pypi`."""

    from .helpers import MockRun

    run = MockRun(fail=False)

    upload_to_pypi(path="path", skip_existing=True, glob_patterns=["glob"])

    assert run.invoked_once_with(
        "twine upload -u '__token__' -p 'secret' --skip-existing "
        '"path/glob"'
    )

    run = MockRun(fail=False)

    upload_to_pypi(path="path", skip_existing=False, glob_patterns=["glob"])

    assert run.invoked_once_with(
        "twine upload -u '__token__' -p 'secret' " '"path/glob"'
    )


# Generated at 2022-06-14 05:16:03.651064
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi() == 0

# Generated at 2022-06-14 05:16:04.608148
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert True

# Generated at 2022-06-14 05:16:05.342142
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert True == True

# Generated at 2022-06-14 05:16:14.598886
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from unittest.mock import patch, Mock

    mock_run = Mock()

    with patch("semantic_release.hvcs.git.upload_to_pypi.run", mock_run):
        upload_to_pypi(path="path", glob_patterns=["glob_patterns"])

    assert mock_run.call_count == 1
    call_args, _ = mock_run.call_args
    assert call_args[0] == 'twine upload -u \'__token__\' -p \'pypi-token\' ' \
                           '\'"path/glob_patterns"\''

# Generated at 2022-06-14 05:16:16.941317
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()

# Generated at 2022-06-14 05:16:26.731252
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .helpers import patch_run
    from .helpers import patch_get

    patch_get("username", "username")
    patch_get("password", "password")
    patch_get("repository", "test_repository")
    patch_run("$1")

    upload_to_pypi("path", True, ["*", "?.txt"])

    assert (
        run.call_args[0][0]
        == "twine upload -u 'username' -p 'password' -r 'test_repository' --skip-existing 'path/*' 'path/?.txt'"
    )

# Generated at 2022-06-14 05:16:29.193351
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi(path = "dist", skip_existing = False, glob_patterns = ["*"])


# Generated at 2022-06-14 05:16:32.442255
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert run("python -m unittest discover -v -s tests/plugins/test_upload_to_pypi.py").ok

# Generated at 2022-06-14 05:17:09.298320
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    os.environ["PYPI_USERNAME"] = "PYPI_USERNAME"
    os.environ["PYPI_PASSWORD"] = "PYPI_PASSWORD"
    upload_to_pypi()
    assert(True)

# Generated at 2022-06-14 05:17:11.913310
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi.__name__ == "upload_to_pypi"

# Generated at 2022-06-14 05:17:17.330038
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    try:
        run(f"rm -rf dist")
        run(f"mkdir -p dist")
        run(f"cp test/test_artifact.txt dist")
        upload_to_pypi(glob_patterns=["test_artifact.txt"])
    finally:
        run(f"rm -rf dist")

# Generated at 2022-06-14 05:17:31.197802
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .helpers import mock_git_info, run_failing_tests

    with run_failing_tests():
        sys_args = ['upload_to_pypi']

        with mock_git_info():
            with pytest.raises(ImproperConfigurationError):
                argv = sys.argv
                sys.argv = sys_args
                upload_to_pypi()
                sys.argv = argv

        with set_env(
            {
                "PYPI_TOKEN": "pypi-this",
                "PYPI_USERNAME": "user",
                "PYPI_PASSWORD": "pass",
            },
            mock_git_info,
        ):
            sys_args = ['upload_to_pypi']
            argv = sys.argv
            sys

# Generated at 2022-06-14 05:17:34.123141
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Test for missing username and password
    with pytest.raises(ImproperConfigurationError):
        upload_to_pypi()

# Generated at 2022-06-14 05:17:47.001861
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    glob_patterns = ["*"]

    # Attempt to get an API token from environment
    token = os.environ.get("PYPI_TOKEN")
    username = None
    password = None
    if not token:
        # Look for a username and password instead
        username = os.environ.get("PYPI_USERNAME")
        password = os.environ.get("PYPI_PASSWORD")
        home_dir = os.environ.get("HOME", "")
        if not (username or password) and (
            not home_dir or not os.path.isfile(os.path.join(home_dir, ".pypirc"))
        ):
            raise ImproperConfigurationError(
                "Missing credentials for uploading to PyPI"
            )

# Generated at 2022-06-14 05:17:55.948468
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Test that upload_to_pypi uses the correct arguments"""
    upload_to_pypi(
        path="dist",
        skip_existing=False,
        glob_patterns=['semantic_release-*'],
    )
    assert ' '.join(run.calls[0][1][0].split(' ')[3:]).strip() == "semantic_release-*"
    upload_to_pypi(
        path="dist",
        skip_existing=True,
        glob_patterns=['twine-*'],
    )
    assert ' '.join(run.calls[1][1][0].split(' ')[3:]).strip() == "twine-*"

# Generated at 2022-06-14 05:18:08.116878
# Unit test for function upload_to_pypi
def test_upload_to_pypi():

    from .helpers import LoggedFunction

    call_count = 0

    def mock_run(command):
        nonlocal call_count
        assert command == expected_command
        call_count += 1

    # Test 1
    call_count = 0
    # Set the environment variables
    os.environ["PYPI_TOKEN"] = "pypi-a1b2cd3d-abcd-1234-5678-a9a8a7a6a5a4"
    path = "dist"
    dist = '"{}/test_fake_pypi_wheel-1.0.0-py3-none-any.whl"'.format(path)
    repository_arg = ""

# Generated at 2022-06-14 05:18:20.073856
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """
    Unit test for function upload_to_pypi
    """
    import subprocess
    import pytest

    dist_path = 'tests/fixtures/dist'

    class SubprocessMock(object):
        def __init__(self, returncode, output):
            self.returncode = returncode
            self.output = output

        def check_output(self, *args):
            return self.output

        def run(self, *args):
            return self


# Generated at 2022-06-14 05:18:21.590878
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()

# Generated at 2022-06-14 05:19:29.716911
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(path="dist", skip_existing=False, glob_patterns=["*"])

# Generated at 2022-06-14 05:19:42.428771
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Test upload_to_pypi.
    """
    from contextlib import contextmanager
    from tempfile import TemporaryDirectory
    from unittest import mock

    from semantic_release.hvcs.git import Git

    @contextmanager
    def mock_env(token=None, username=None, password=None):
        token_env = {}
        username_password_env = {}
        old_env = os.environ.copy()

        if token:
            token_env = {"PYPI_TOKEN": token}
            username_password_env = {"PYPI_USERNAME": "__token__", "PYPI_PASSWORD": token}

        if username and password:
            username_password_env = {"PYPI_USERNAME": username, "PYPI_PASSWORD": password}


# Generated at 2022-06-14 05:19:52.553367
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from os import path

    from semantic_release.settings import config
    from semantic_release.util import get_version
    from tempfile import mkdtemp

    # Ensure that the config is empty
    config.clear()

    # Create a temp directory to store the package files
    temp_dist = mkdtemp()
    assert path.isdir(temp_dist)

    # Set the credentials to something invalid so we don't accidentally upload anything
    os.environ['PYPI_USERNAME'] = "temp_user"
    os.environ['PYPI_PASSWORD'] = "temp_password"

    # Upload to pypi and ensure that the files are uploaded
    upload_to_pypi(path=temp_dist, skip_existing=True, glob_patterns=["*"])

# Generated at 2022-06-14 05:20:04.224547
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .helpers import mock_subprocess_check_output, reset_subprocess_check_output

    def mock_subprocess_check_output_cert(command):
        assert command[0] == "twine"
        assert command[1] == "upload"
        assert command[2] == "-u"
        assert command[3] == "__token__"
        assert command[4] == "-p"
        assert command[5] == "pypi-foobar"
        assert command[6] == "--skip-existing"
        assert command[7] == '"dist/wheel-*.whl"'
        assert len(command) == 8


# Generated at 2022-06-14 05:20:05.556072
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi("path")

# Generated at 2022-06-14 05:20:08.914316
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert isinstance(upload_to_pypi(
        path="dist",
        skip_existing=False,
        glob_patterns=["*"]
    ), None)

# Generated at 2022-06-14 05:20:12.002585
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(path="./examples/__fake_dist_package/dist",skip_existing=True,glob_patterns=["*"])

# Generated at 2022-06-14 05:20:19.297394
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Unit testing for function upload_to_pypi
    """
    from .helpers import to_ordered_dict

    try:
        run("pip install twine")
    except:
        pass

    result = upload_to_pypi.func(
        path="/tmp/dist",
        skip_existing=True,
        glob_patterns=["*"],
    )

    assert result is None

    result = to_ordered_dict(result)

    assert result == {}

# Generated at 2022-06-14 05:20:25.813344
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from unittest.mock import patch
    
    from .helpers import ContextMock
    

# Generated at 2022-06-14 05:20:27.909805
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """
    Unit test for function upload_to_pypi
    """
    upload_to_pypi()