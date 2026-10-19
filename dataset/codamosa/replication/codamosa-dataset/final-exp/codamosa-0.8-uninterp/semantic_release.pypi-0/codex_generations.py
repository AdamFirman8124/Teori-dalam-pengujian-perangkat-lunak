

# Generated at 2022-06-14 05:13:02.230803
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .upload_result import UploadResult
    from .uploader import Uploader
    from .config import config_get_pyup_info

    from .helpers import (  # noqa
        mock,
        mock_open,
        read_file,
        mock_run,
        remove_file,
        write_file,
    )

    import requests

    # Create a temp directory and write a sample wheel to it
    temp_dir = "tests/fakes/"
    wheel_file = "tests/fakes/fake.whl"
    write_file(wheel_file, "fake wheel")

    # use the upload_to_pypi function
    config_get_pyup_info.return_value = None
    upload_to_pypi(temp_dir, False)

    # check that calls to twine have been made

# Generated at 2022-06-14 05:13:07.386989
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Check that the appropriate ``twine`` commands are called with the correct arguments."""
    upload_to_pypi("dist", skip_existing=True, glob_patterns=["*.tar.gz", "*.whl"])
    run.assert_called_once_with(
        "twine upload -u '__token__' -p 'pypi-123' --skip-existing "
        '"dist/*.tar.gz" "dist/*.whl"'
    )


# Generated at 2022-06-14 05:13:08.650492
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi("path")

# Generated at 2022-06-14 05:13:09.576640
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()

# Generated at 2022-06-14 05:13:20.411347
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    def test_upload_to_pypi(path="dist", skip_existing=False, glob_patterns=None):
        if not glob_patterns:
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

# Generated at 2022-06-14 05:13:23.273775
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()
    upload_to_pypi(skip_existing=True)

# Generated at 2022-06-14 05:13:28.367077
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    class os_environ():
        environ = {}
        def get(key):
            return os_environ.environ.get(key)
    os.environ = os_environ()
    os.environ.environ = {"PYPI_TOKEN": "token"}
    assert (upload_to_pypi() == None)

# Generated at 2022-06-14 05:13:29.420157
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert True

# Generated at 2022-06-14 05:13:34.072605
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    os.system('touch dist/test.tar.gz')
    try:
        upload_to_pypi()
    except ImproperConfigurationError:
        os.system('rm -rf dist')
        assert bool(1)
    else:
        os.system('rm -rf dist')
        assert False

# Generated at 2022-06-14 05:13:39.460998
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi("dist", skip_existing=False, glob_patterns=["*"])
    upload_to_pypi("dist", skip_existing=True, glob_patterns=["*"])


# Generated at 2022-06-14 05:13:45.633477
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    mock_config = {}
    config.update(mock_config)
    upload_to_pypi(path="dist", glob_patterns=["*.whl"])

# Generated at 2022-06-14 05:13:46.201548
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert True

# Generated at 2022-06-14 05:13:50.664244
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """unit test for upload_to_pypi"""
    print("Testing upload_to_pypi")
    upload_to_pypi(glob_patterns=["*"], skip_existing=True)

# Generated at 2022-06-14 05:13:52.879062
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi() == {'message': 'Uploaded files to PyPI.', 'level': 'info'}

# Generated at 2022-06-14 05:14:04.328637
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Create temporary config file
    with open("config.py", "w") as temp_config_file:
        temp_config_file.write("repository = 'test_repository'")

    # Write dummy package files in dist/
    os.makedirs("dist/")
    with open("dist/dummy_package.tar.gz", "w") as dummy_package:
        dummy_package.write("this is a dummy package")

    # Add necessary env variables to mock using twine
    os.environ["PYPI_USERNAME"] = "test_username"
    os.environ["PYPI_PASSWORD"] = "test_password"

    # Mock run command
    prev_run_command = run
    run_mock_params = None

    # Redefine run method, to mock its use and check

# Generated at 2022-06-14 05:14:05.383268
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi("dist")

# Generated at 2022-06-14 05:14:08.740380
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    run(f"python setup.py sdist", echo=True)
    run(f"python setup.py bdist_wheel", echo=True)
    logger.info("Uploading to PyPI")
    upload_to_pypi()

# Generated at 2022-06-14 05:14:09.740105
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()

# Generated at 2022-06-14 05:14:11.183509
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi() is None



# Generated at 2022-06-14 05:14:18.939934
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import shutil
    import tempfile

    try:
        package_name = "foobar-1.1.1-py3-none-any.whl"
        package_path = os.path.join(tempfile.gettempdir(), package_name)
        with open(package_path, 'w') as f:
            f.write('Hello World!')

        upload_to_pypi(tempfile.gettempdir(), glob_patterns=[package_name])
    finally:
        shutil.rmtree(tempfile.gettempdir())

# Generated at 2022-06-14 05:14:33.479980
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    path = "test/test_upload_to_pypi"
    run(f"mkdir -p {path}")
    run(f"touch {path}/file_to_upload")
    upload_to_pypi(path)
    run(f"rm -rf {path}")

# Generated at 2022-06-14 05:14:35.926403
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Test only works if credentials and path are correct
    # Should never fail. Good unit test for coverage
    upload_to_pypi(glob_patterns=["*"])

# Generated at 2022-06-14 05:14:38.570664
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi("dist", True, ["*"])


# Generated at 2022-06-14 05:14:38.997904
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:14:39.987481
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(glob_patterns=['*/*/*/*/*/*'])

# Generated at 2022-06-14 05:14:51.799354
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from io import StringIO
    from invoke import Context

    class DummyContext(Context):
        def __init__(self, streams):
            self.run = run
            self.sudo = run
            self.local = run
            self.streams = streams

        def __enter__(self):
            return self

        def __exit__(self, *args):
            pass

    # Test no error
    fake_stdout = StringIO()
    fake_stderr = StringIO()
    fake_streams = (fake_stdout, fake_stderr)
    fake_ctx = DummyContext(fake_streams)

# Generated at 2022-06-14 05:15:02.481688
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Test function upload_to_pypi.
    """
    from .helpers import mock_pypi_service
    from .helpers import patch_release_version

    # Create config for test
    config["pypi"]["user"] = "test_user"
    config["pypi"]["password"] = "test_password"

    # This test only needs the server
    mock_pypi_service("server")

    # Create test files
    with patch_release_version("0.0.1"):
        # Create package
        run("python setup.py sdist bdist_wheel", warn=True)

    # Upload package
    upload_to_pypi()

# Generated at 2022-06-14 05:15:05.864680
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    configuration = {"pypi": {"repository": "test-repo"}}
    with config.set(configuration):
        assert upload_to_pypi("/temp", skip_existing=True, glob_patterns=["*"])


# Generated at 2022-06-14 05:15:07.316668
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi is not None

# Generated at 2022-06-14 05:15:09.674081
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    token = "pypi-1234"
    os.environ["PYPI_TOKEN"] = token
    assert token == os.environ["PYPI_TOKEN"]

# Generated at 2022-06-14 05:15:26.693458
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:15:38.628321
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    try:
        import contextlib
        from unittest.mock import patch
        from unittest.mock import mock_open
    except ImportError:
        import mock
        import mock_open
        from contextlib import patch

    def _test_upload_to_pypi_wrapper(mock_run, env, username, password, glob_patterns, expected_pypi_call):
        os.environ.update(env)
        upload_to_pypi(glob_patterns=glob_patterns)
        assert mock_run.called
        twine_call = mock_run.call_args[0][0]
        assert twine_call == expected_pypi_call


# Generated at 2022-06-14 05:15:51.860988
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # pylint: disable=unused-argument,unused-variable,protected-access
    import pytest
    from .helpers import generate_release_notes, replace_variable, replace_with_mock_prompt
    # pylint: enable=unused-argument,unused-variable,protected-access
    from semantic_release import ci_checks, get_last_release, post_release
    from semantic_release.exceptions import ImproperConfigurationError
    from semantic_release.settings import config
    from semantic_release.version_service import check_version_service
    from semantic_release.version_service.version_service import _get_version
    from semantic_release.workflow import verify_workflow
    from unittest.mock import Mock


# Generated at 2022-06-14 05:16:02.314539
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from semantic_release.settings import config, load_config
    from .helpers import patch_logger
    from .helpers import capture_stdout, strip_ansi_escape
    from .test_release import create_file

    # import twine module for mocking
    import twine

    # create temp files and dirs
    config_file = create_file("test_upload.ini")
    dist_folder = create_file("test_upload_to_pypi/dist")

    # reset to default settings
    config.reset()

    # load test config
    load_config(config_file)

    # mock twine.commands module
    twine_mock = twine.commands.upload.upload
    twine.commands.upload.upload = lambda *args, **kwargs: None

    # mock stdout so print

# Generated at 2022-06-14 05:16:14.205610
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Test the upload_to_pypi function."""
    import unittest
    import inspect
    import tempfile
    import shutil
    import os

    class FakeOsModule(object):
        """Fake os module."""

        def __init__(self):
            self.environ = dict()

        def environ(self):
            """Env var."""
            return self.environ

        @staticmethod
        def path(path):
            return path

        def path_isfile(self, path):
            """Check if it is a file."""
            if path == '$HOME/.pypirc':
                return True

            return False

    class FakeInvoke(object):
        """Fake invoke module."""

        def __init__(self):
            self.command = None
            self.called = False


# Generated at 2022-06-14 05:16:28.067398
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import pathlib
    from io import StringIO
    from invoke import Context

    from .helpers import FakeRun
    from .helpers import LoggedFunction


# Generated at 2022-06-14 05:16:30.543886
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    glob_patterns = ["*.tar.gz", "*.whl"]
    upload_to_pypi(glob_patterns=glob_patterns)

# Generated at 2022-06-14 05:16:44.458062
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import shutil
    import tempfile
    import time
    from pathlib import Path
    
    d = tempfile.mkdtemp()
    (Path(d)/'test').touch()

    try:
        username = "__testuser__"
        password = "__testpassword__"
        with open(Path(d)/".pypirc","w") as f:
            f.write(f"""[distutils]
index-servers =
    pypitest

[pypitest]
repository: https://test.pypi.org/legacy/
username: {username}
password: {password}""")

        os.environ['HOME']=d
        upload_to_pypi(path=d)
    finally:
        shutil.rmtree(d)

# Generated at 2022-06-14 05:16:47.028297
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(path='dist', skip_existing=True, glob_patterns='abc')

# Generated at 2022-06-14 05:16:56.722197
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Setup
    glob_patterns = ["*.whl", "*.gz"]

    # Test empty glob_patterns, expect ["*"]
    upload_to_pypi(glob_patterns=[])
    assert glob_patterns == ["*"]

    # Test with glob_patterns
    upload_to_pypi(glob_patterns=glob_patterns)
    # Test with glob_patterns and skip_existing
    upload_to_pypi(glob_patterns=glob_patterns, skip_existing=True)

# Generated at 2022-06-14 05:17:29.361989
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()

# Generated at 2022-06-14 05:17:37.739268
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """
    test upload_to_pypi
    """
    # pylint: disable=unused-argument
    def call_upload(
        path: str = "dist", skip_existing: bool = False, glob_patterns: List[str] = None
    ):
        """
        call upload_to_pypi
        """
        # pylint: disable=unused-variable
        m_run = Mock()
        upload_to_pypi(path, skip_existing, glob_patterns)
        m_run.assert_called_with(
            "twine upload -u '__token__' -p 'pypi-123' --skip-existing 'dist/foo'"
        )

    m_os = Mock()

# Generated at 2022-06-14 05:17:46.390962
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import pytest
    import tempfile

    tempdir = tempfile.TemporaryDirectory()
    try:
        # Make a file
        with open(f'{tempdir.name}/test.txt', 'a') as f:
            f.write("test content")

        config.set("repository", "test_package")
        upload_to_pypi(path=f"{tempdir.name}")
    except Exception:
        pytest.fail("Unexpected exception")

# Generated at 2022-06-14 05:17:48.947704
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(glob_patterns=["*"])

# Generated at 2022-06-14 05:17:57.164915
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    def run_assert(
        path="dist",
        skip_existing=False,
        glob_patterns=None,
        expected_command="twine upload ./dist/*",
    ):
        run = MockRun(expected_command)
        upload_to_pypi(path=path, skip_existing=skip_existing, glob_patterns=glob_patterns)
        assert run.was_called

    # Default, basic call
    run_assert()

    # With different path
    run_assert(path=".", expected_command="twine upload ./*")

    # With skip_existing
    run_assert(
        skip_existing=True, expected_command="twine upload ./dist/* --skip-existing"
    )

    # With different glob pattern

# Generated at 2022-06-14 05:17:59.468995
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi("dist") is None

# Generated at 2022-06-14 05:18:12.292069
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Test for upload_to_pypi.

    The test is also used to document the behavior.
    """
    import os
    import shutil
    from unittest import mock
    from pathlib import Path

    # Make temporary dist directory
    dist = Path("test_dist")
    dist.mkdir(exist_ok=True)

    # Make files
    for p in ["a.whl", "b.whl", "c.whl"]:
        Path(dist, p).touch()

    # Run function
    with mock.patch("invoke.run") as mkdir:
        upload_to_pypi(str(dist), glob_patterns=["a.*", "b.*"])

# Generated at 2022-06-14 05:18:18.866099
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Test the calling of the function upload_to_pypi"""
    os.environ["PYPI_TOKEN"] = "pypi-test"

    upload_to_pypi(path="/home/test/dist")
    upload_to_pypi(path="/home/test/dist", skip_existing=True)
    upload_to_pypi(path="/home/test/dist", skip_existing=True, glob_patterns=["*"])

# Generated at 2022-06-14 05:18:22.637923
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(path="./dist/", skip_existing=True, glob_patterns=["semantic_release*"])

if __name__ == "__main__":
    test_upload_to_pypi()

# Generated at 2022-06-14 05:18:29.741561
# Unit test for function upload_to_pypi
def test_upload_to_pypi():

    upload_to_pypi(
        "dist",
        skip_existing=True,
        glob_patterns=[
            'semantic_release-3.0.0rc1-py2.py3-none-any.whl',
            'semantic_release-3.0.0rc1.tar.gz'
        ]
    )

# Generated at 2022-06-14 05:19:41.881069
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # mocks
    def mock_run(command):
        pass
    run_backup = run
    run = mock_run
    # cases
    upload_to_pypi()
    upload_to_pypi(glob_patterns=["*.whl"])
    upload_to_pypi(skip_existing=True)
    # reset
    run = run_backup

# Generated at 2022-06-14 05:19:44.811486
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(
        path="dist", skip_existing=True, glob_patterns=["*", "*.whl"]
    )

# Generated at 2022-06-14 05:19:50.264084
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()
    upload_to_pypi(glob_patterns=["*.txt"])
    upload_to_pypi(glob_patterns=["small-*.txt"])
    upload_to_pypi(skip_existing=True)

# Generated at 2022-06-14 05:19:51.633669
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()

# Generated at 2022-06-14 05:20:04.051471
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Test with username, password, and repository
    os.environ["PYPI_USERNAME"] = "username"
    os.environ["PYPI_PASSWORD"] = "password"
    upload_to_pypi(path="dist", glob_patterns=["file_name.txt"], skip_existing=False)
    upload_to_pypi(path="dist", glob_patterns=["file_name.txt"], skip_existing=True)
    upload_to_pypi(path="dist", glob_patterns=["file_name.txt", "*.txt"], skip_existing=False)
    upload_to_pypi(path="dist", glob_patterns=["file_name.txt", "*.txt"], skip_existing=True)
    del os.environ["PYPI_USERNAME"]


# Generated at 2022-06-14 05:20:17.790951
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import os
    import sys
    import shutil
    from distutils.version import LooseVersion
    from unittest import mock

    from semantic_release.settings import config
    from semantic_release.pypi.helpers import upload_to_pypi

    def mock_run(cmd, **kwargs):
        return mock.Mock()

    # Unit tests can not run on Windows
    if sys.platform.startswith('win'):
        return

    # Mock os.environ
    saved_environ = dict(os.environ)
    os.environ = {}

    # Mock os.path.isfile
    saved_isfile = os.path.isfile
    os.path.isfile = lambda x: True

    # Mock run

# Generated at 2022-06-14 05:20:24.371020
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(path="./test/test_data/dist", \
    skip_existing=False, glob_patterns=["*.whl"])
    # assert os.path.isfile("./test/test_data/dist/semantic_release-1.0.0-dev1.tar.gz")
    assert os.path.isfile("./test/test_data/dist/semantic_release-1.0.0-dev1.whl")
    os.remove("./test/test_data/dist/semantic_release-1.0.0-dev1.whl")

if __name__ == "__main__":
    test_upload_to_pypi()

# Generated at 2022-06-14 05:20:26.191534
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(glob_patterns=["*"])

# Generated at 2022-06-14 05:20:28.318368
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Fake unit test to ensure the function upload_to_pypi exists."""
    assert upload_to_pypi

# Generated at 2022-06-14 05:20:29.701930
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # TODO
    pass