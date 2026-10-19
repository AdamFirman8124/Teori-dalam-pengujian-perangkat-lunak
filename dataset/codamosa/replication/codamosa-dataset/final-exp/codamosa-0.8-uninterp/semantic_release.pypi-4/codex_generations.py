

# Generated at 2022-06-14 05:12:49.637100
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(glob_patterns=["*.whl"])

# Generated at 2022-06-14 05:13:02.610044
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import pathlib
    from .helpers import TemporaryDirectory

    def list_files(path):
        return [os.path.relpath(str(f), path) for f in pathlib.Path(path).rglob("**/*")]

    with TemporaryDirectory() as tmpdir:
        with open(os.path.join(tmpdir, "foo.txt"), "w") as f:
            f.write("foo")
        os.makedirs(os.path.join(tmpdir, "bar"))
        with open(os.path.join(tmpdir, "bar", "baz.txt"), "w") as f:
            f.write("bar/baz")

# Generated at 2022-06-14 05:13:11.641674
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .helpers import patch_run

    pypi_url = "https://upload.pypi.org/legacy/"
    password = "hunter2"
    username = "secret"
    token = "pypi-hunter2"
    repository = "pypi"
    dist = '/path/to/dist/*'

    with patch_run() as mock_run:
        upload_to_pypi(path=dist)

    assert mock_run.call_count == 1
    mock_run.assert_called_with(
        f"twine upload --repository-url '{pypi_url}' "
        f"{dist}"
    )

    with patch_run() as mock_run:
        os.environ["PYPI_USERNAME"] = username
        upload_to_pypi

# Generated at 2022-06-14 05:13:22.043676
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # setup test
    try:
        # test missing credentials
        upload_to_pypi()
        assert False, "Should have failed with missing credentials."
    except ImproperConfigurationError as e:
        assert "Missing credentials" in str(e)

    # test missing password
    os.environ["PYPI_USERNAME"] = "test_user"
    try:
        upload_to_pypi()
        assert False, "Should have failed with missing password."
    except ImproperConfigurationError as e:
        assert "Missing credentials" in str(e)

    # test missing username
    os.environ["PYPI_USERNAME"] = ""
    os.environ["PYPI_PASSWORD"] = "test_password"

# Generated at 2022-06-14 05:13:24.626210
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi()

# Generated at 2022-06-14 05:13:29.756598
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Test that upload_to_pypi raises an error when a PYPI_TOKEN is not provided"""
    try:
        upload_to_pypi()
        assert False
    except ImproperConfigurationError:
        assert True

# Generated at 2022-06-14 05:13:33.313666
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    args = ['dist/test_package-0.1.0-py3-none-any.whl']
    upload_to_pypi(path="dist", skip_existing=False, glob_patterns=args)

# Generated at 2022-06-14 05:13:34.622032
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Just an example
    pass

# Generated at 2022-06-14 05:13:47.724894
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import shutil
    import tempfile
    import io
    import sys
    import unittest
    from unittest.mock import patch
    from .testutils import disable_logging

    class UploadToPyPiTestCase(unittest.TestCase):

        """Unit test for function upload_to_pypi"""

        @classmethod
        def setUpClass(cls):
            cls.repository = os.environ.get("TEST_REPOSITORY", "pypi")
            cls.token = os.environ.get("TEST_PYPI_TOKEN", "")
            cls.username = os.environ.get("TEST_PYPI_USERNAME", "")

# Generated at 2022-06-14 05:13:58.433504
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import json
    import tempfile
    import unittest
    import unittest.mock
    import pathlib
    import twine
    import requests

    class MockResponse:
        @staticmethod
        def json():
            return {"releases": {"0.0.1": [{"url": "url"}]}}

        @staticmethod
        def raise_for_status():
            pass

    class MockedSession:
        def request(self, method, url, auth, **kwargs):
            return MockResponse()


# Generated at 2022-06-14 05:14:13.546176
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Test when there is no environment variable
    try:
        upload_to_pypi()
    except ImproperConfigurationError:
        pass
    else:
        assert False
    # Test when there is a token
    os.environ["PYPI_TOKEN"] = "pypi-fake"
    try:
        upload_to_pypi()
    except Exception as e:
        assert "Missing credentials for uploading to PyPI" in str(e)
    else:
        assert False

    os.environ["PYPI_TOKEN_PYPI"] = "pypi-fake"
    try:
        upload_to_pypi()
    except Exception as e:
        assert "Missing credentials for uploading to PyPI" in str(e)
    else:
        assert False


# Generated at 2022-06-14 05:14:14.632550
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:14:22.985799
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    token = os.environ.get("PYPI_TOKEN")
    username = os.environ.get("PYPI_USERNAME")
    password = os.environ.get("PYPI_PASSWORD")
    home_dir = os.environ.get("HOME", "")

    if username and password:
        os.environ["PYPI_USERNAME"] = username
        os.environ["PYPI_PASSWORD"] = password

    if token:
        os.environ["PYPI_TOKEN"] = token

    if home_dir and os.path.isfile(os.path.join(home_dir, ".pypirc")):
        os.environ["HOME"] = home_dir


# Generated at 2022-06-14 05:14:26.971242
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from distutils.dir_util import remove_tree

    try:
        upload_to_pypi(path="tests/fixtures/files_to_upload")
    finally:
        remove_tree("tests/fixtures/files_to_upload")

# Generated at 2022-06-14 05:14:38.776165
# Unit test for function upload_to_pypi

# Generated at 2022-06-14 05:14:46.071726
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import os

    pypi_test_path = os.path.join(os.getcwd(), "pypi_test")
    os.makedirs(pypi_test_path)
    test_file_1 = os.path.join(pypi_test_path, "test_file_1")
    test_file_2 = os.path.join(pypi_test_path, "test_file_2.py")

    open(test_file_1, "w").close()
    open(test_file_2, "w").close()

    # No glob pattern should be empty
    no_glob_pattern = []
    assert upload_to_pypi(pypi_test_path, glob_patterns=no_glob_pattern) == [""]

# Generated at 2022-06-14 05:14:46.788089
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert True

# Generated at 2022-06-14 05:14:54.436156
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Unit test for function upload_to_pypi

    This test ensures that the upload_to_pypi function works as expected, with the
    correct arguments being passed to the Twine tool.
    """

    from unittest.mock import patch, call
    from .helpers import LoggedFunction

    # Mock the configuration variable
    with patch("semantic_release.settings.config.get", return_value='foo'):
        # Mock the run function
        with patch('invoke.run') as runmock:
            # Call the function
            upload_to_pypi(path='dist',
                skip_existing=True,
                glob_patterns=["*"])

            # Check that run was called with the correct parameters

# Generated at 2022-06-14 05:14:55.107287
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:15:07.754712
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from unittest.mock import patch
    from .helpers import LoggedFunction
    import os
    import tempfile
    
    # Create temp directory
    temp_dir = tempfile.mkdtemp(prefix='semantic-release-tmp-dist')
    os.environ["HOME"] = temp_dir
    
    # Mock invoke.run() to intercept the command call
    with patch('invoke.run') as mock_run:
        # Prepare expected twine command
        expected_twine_command = 'twine upload -u \'__token__\' -p \'pypi-12345678910\' \"{}/{}\"'.format(temp_dir, '*')
        # Call the target function
        upload_to_pypi(path=temp_dir)
        # Verify that this module invoked the twine command correctly
        mock

# Generated at 2022-06-14 05:15:17.020223
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert True

# Generated at 2022-06-14 05:15:18.273108
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi()==None

# Generated at 2022-06-14 05:15:24.241892
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .helpers import get_logger_output, LoggedFunction
    from .contexts import temp_chdir, environment

    # Test errors
    assert get_logger_output(
        "ERROR",
        lambda: upload_to_pypi()
    ) == ["Missing credentials for uploading to PyPI"]
    assert get_logger_output(
        "ERROR",
        lambda: upload_to_pypi(),
        environment(PYPI_PASSWORD="xxx", PYPI_USERNAME="yyy")
    ) == []
    assert get_logger_output(
        "ERROR",
        lambda: upload_to_pypi(glob_patterns=[]),
        environment(PYPI_TOKEN="pypi-xxx")
    ) == []

# Generated at 2022-06-14 05:15:25.454890
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi()

# Generated at 2022-06-14 05:15:38.005912
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Tokens have an "pypi-" prefix
    assert upload_to_pypi.__name__ == "upload_to_pypi"
    assert upload_to_pypi.__qualname__ == "upload.upload_to_pypi"

# Generated at 2022-06-14 05:15:42.139060
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .mocks import MockRun

    upload_to_pypi()  # pylint: disable=no-value-for-parameter

# Generated at 2022-06-14 05:15:43.904024
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pytest_helper.invoke('upload_to_pypi')
    assert pytest_helper.invoked == ['twine upload -u \'__token__\' -p \'pypi-********\' "dist/*"']


# Generated at 2022-06-14 05:15:55.268932
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """
    Test upload_to_pypi
    Note: This function uses python's invoke.run which we are not able to mock
    """
    from unittest.mock import patch, Mock, call

    with patch("os.environ.get") as mock_get_env, patch("invoke.run") as mock_run:
        mock_get_env.side_effect = [None, "badtoken", "pypi-good_token", "testuser", "testpw",
                                    None, "testuser", "testpw"]

        upload_to_pypi(path="test_path", skip_existing=False, glob_patterns=["a", "b"])

# Generated at 2022-06-14 05:16:08.430003
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from semantic_release.hvcs import Commit
    from semantic_release.logging_dict import LoggingDict
    from semantic_release.settings import get_default_config
    from semantic_release.history.utils import create_changelog_entry

    new_version = "1.2.0"
    current_version = "1.1.0"
    custom_next_version = "1.2.1"

    commit_msg = "feat(xxx): some stuff"
    commit_body = commit_msg
    commit_hash = "123"
    commit_author = "John Doe <john@doe.com>"
    commit = Commit(hash=commit_hash, body=commit_body, author=commit_author)
    next_version = create_changelog_entry(new_version, current_version, commit)

   

# Generated at 2022-06-14 05:16:10.034737
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass
    # TODO Find a way to unit test this function

# Generated at 2022-06-14 05:16:30.757843
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Test upload_to_pypi function.
    """
    path="path"
    skip_existing=True
    glob_patterns=["test*","*test"]
    upload_to_pypi(path,skip_existing,glob_patterns)

# Generated at 2022-06-14 05:16:33.471157
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Unit test upload_to_pypi function."""
    pass

# Generated at 2022-06-14 05:16:46.012837
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    run = MagicMock()
    upload_to_pypi(path='dist', skip_existing=False, glob_patterns=['dist/*'], run=run)
    assert 'twine upload -u \'__token__\' -p \'pypi-TEST_TOKEN\' "dist/*"' in run.call_args[0][0]

    run.reset_mock()

    upload_to_pypi(path='dist', skip_existing=True, glob_patterns=['dist/*'], run=run)
    assert 'twine upload -u \'__token__\' -p \'pypi-TEST_TOKEN\' --skip-existing "dist/*"' in run.call_args[0][0]

    run.reset_mock()


# Generated at 2022-06-14 05:16:56.120342
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Test function upload_to_pypi.
    """
    path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.pardir, "tests/wheelhouse")
    )

    try:
        glob_patterns = ["*.whl"]
        skip = False
        upload_to_pypi(path, skip_existing=skip, glob_patterns=glob_patterns)
    except Exception:
        logging.error("Upload of wheel to PyPI failed")
        raise

    assert True

# Generated at 2022-06-14 05:16:59.810790
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(path="tests/fixtures/dist", skip_existing=False, glob_patterns=["*"])

if __name__ == "__main__":
    test_upload_to_pypi()

# Generated at 2022-06-14 05:17:01.397697
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    run_result = run("")

# Generated at 2022-06-14 05:17:07.441117
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """
    The test_upload_to_pypi function is used to test the upload_to_pypi function
    """
    glob_patterns = ["*"]
    token = "pypi-1234567890"
    os.environ["PYPI_TOKEN"] = token

    upload_to_pypi(glob_patterns = glob_patterns)

    os.environ.pop("PYPI_TOKEN")

# Generated at 2022-06-14 05:17:18.167859
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(path="./tests/test_data/pypi_test_folder", skip_existing=True, glob_patterns=["*.zip"])
    upload_to_pypi(path="./tests/test_data/pypi_test_folder", skip_existing=True, glob_patterns=["*.tgz"])
    upload_to_pypi(path="./tests/test_data/pypi_test_folder", skip_existing=True, glob_patterns=["*.whl"])
    upload_to_pypi(path="./tests/test_data/pypi_test_folder", skip_existing=True, glob_patterns=["*.egg"])



# Generated at 2022-06-14 05:17:28.221041
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Arrange
    pypi_token = "pypi-supersecret"
    pypi_username = "anyuser"
    pypi_password = "supersecret"

    # Act

# Generated at 2022-06-14 05:17:30.391634
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(path = "dist", skip_existing=False, glob_patterns=None)

# Generated at 2022-06-14 05:18:06.688602
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi("dist", glob_patterns=["*.whl", "*.egg"])

# Generated at 2022-06-14 05:18:10.606460
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi("/Users/huangtiandou/testing-python-semantic-release/tests/fixtures/semantic-release/dist")

# Generated at 2022-06-14 05:18:12.444220
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """
    Unit test for function upload_to_pypi
    """
    return

# Generated at 2022-06-14 05:18:13.107791
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:18:13.804663
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert True

# Generated at 2022-06-14 05:18:19.010491
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from invoke.exceptions import UnexpectedExit

    try:
        upload_to_pypi(None, None, None)
    except UnexpectedExit as e:
        assert hasattr(e, "result"), "The error message is expected"
        assert "missing credentials" in e.result.stderr.lower(), "The error message is expected"


# Generated at 2022-06-14 05:18:25.496591
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi.__name__ == 'upload_to_pypi'

    mock_run = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))) + '\\mock_run'

    upload_to_pypi(path=mock_run, skip_existing=False, glob_patterns=['*'])
    upload_to_pypi(path=mock_run, skip_existing=True, glob_patterns=['*'])

# Generated at 2022-06-14 05:18:26.533998
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:18:38.219723
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    with open('test_pypi_username', 'w') as f:
        f.write('pypi_username')
    with open('test_pypi_password', 'w') as f:
        f.write('pypi_password')
    # PyPI token should begin with "pypi-"
    try:
        upload_to_pypi(skip_existing=False, glob_patterns=['CHANGELOG.rst'])
    except ImproperConfigurationError:
        pass

    os.environ["PYPI_TOKEN"] = 'pypi-c2a5594f7eed3e9cdbf51ffb8291d68b'
    upload_to_pypi(skip_existing=False, glob_patterns=['CHANGELOG.rst'])
    upload_

# Generated at 2022-06-14 05:18:39.879962
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(path=".", glob_patterns="*.yml")

# Generated at 2022-06-14 05:20:01.469715
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import os
    from unittest.mock import patch
    from semantic_release.hooks.pypi import upload_to_pypi
    from semantic_release.settings import config

    # Test with username, password and repository
    os.environ["PYPI_USERNAME"] = "username"
    os.environ["PYPI_PASSWORD"] = "password"
    config.set("repository", "test")

    with patch("invoke.run", return_value="") as mock_run:
        upload_to_pypi(path="path", skip_existing=False, glob_patterns=["*"])
        assert mock_run.call_count == 1

# Generated at 2022-06-14 05:20:02.800207
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()

# Generated at 2022-06-14 05:20:03.842635
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()

# Generated at 2022-06-14 05:20:09.903054
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    with open("tests/test_data/twine-1.11.0.tar.gz", "rb") as file:
        data = file.read()
        assert data == upload_to_pypi("twine-1.11.0.tar.gz")

# Generated at 2022-06-14 05:20:20.881708
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    dist = "dist"
    glob_patterns = ["*"]
    token = "pypi-askdjiasjdiaosdjsaodj"
    os.environ["PYPI_TOKEN"] = token
    
    # Test with token
    upload_to_pypi(dist, glob_patterns=glob_patterns)
    assert run.calls[0] == f"twine upload -u '__token__' -p '{token}' '{dist}/*'"

    del os.environ["PYPI_TOKEN"]
    os.environ["PYPI_USERNAME"] = "user"
    os.environ["PYPI_PASSWORD"] = "password"

    # Test with password and username

# Generated at 2022-06-14 05:20:32.961974
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    test_upload_to_pypi.called = False
    def mock_run(command):
        test_upload_to_pypi.called = True
    original_run = run
    run = mock_run
    os.environ["PYPI_USERNAME"] = "foo"
    os.environ["PYPI_PASSWORD"] = "bar"
    try:
        upload_to_pypi()
        assert test_upload_to_pypi.called
    finally:
        run = original_run
        del os.environ["PYPI_USERNAME"]
        del os.environ["PYPI_PASSWORD"]

# Generated at 2022-06-14 05:20:34.693100
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:20:38.068994
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """
    Runs the function for the purpose of testing.
    """
    upload_to_pypi(
        path="dist", skip_existing=False, glob_patterns=["*"]
        )

# Generated at 2022-06-14 05:20:39.819269
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()

# Generated at 2022-06-14 05:20:42.498773
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Test with no repository
    upload_to_pypi()
    # Test with repository
    upload_to_pypi(repository="test")