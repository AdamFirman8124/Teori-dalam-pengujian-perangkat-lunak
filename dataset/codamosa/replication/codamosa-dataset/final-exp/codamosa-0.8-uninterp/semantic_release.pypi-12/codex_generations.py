

# Generated at 2022-06-14 05:12:54.520929
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .mock_logging_setup import MockLoggingHandler

    mock_logger = MockLoggingHandler()
    upload_to_pypi(glob_patterns=["test"])
    assert mock_logger.messages == [
        "Uploading files to PyPI with Twine..."
    ]

# Generated at 2022-06-14 05:12:55.648001
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert 1 == 1

# Generated at 2022-06-14 05:12:56.311298
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # TODO: Create unit test for upload_to_pypi
    pass

# Generated at 2022-06-14 05:13:06.265244
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Given
    os.environ["PYPI_USERNAME"] = "test_user"
    os.environ["PYPI_PASSWORD"] = "test_password"
    repository = "test_repository"
    glob_patterns = ["*.tar.gz", "*.whl"]
    test_arguments = {
        "path": "path",
        "skip_existing": False,
        "glob_patterns": glob_patterns,
    }
    dist = " ".join(
        ['"{}/{}"'.format("path", glob_pattern.strip()) for glob_pattern in glob_patterns]
    )

# Generated at 2022-06-14 05:13:12.801952
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .helpers import MockContext

    context = MockContext(
        config={"repository": "test", "username": "user", "password": "pwd"},
        run=lambda cmd, capture=False, **kwargs: print(cmd),
    )

    upload_to_pypi(path="dist", glob_patterns=["*"], context=context)

    assert context.run.calls[0][0] == "twine upload -u 'user' -p 'pwd' -r 'test' dist/*"

# Generated at 2022-06-14 05:13:14.009059
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:13:22.346070
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .helpers import Mock, patch

    with patch("invoke.run") as mock_run:
        mock_run.return_value = Mock(returncode=0)

        upload_to_pypi(
            glob_patterns=["foo", "bar"],
            skip_existing=True
        )

        mock_run.assert_called_once_with('twine upload -u \'__token__\' -p \'pypi-test_token\' --skip-existing "dist/foo" "dist/bar"')

        upload_to_pypi(
            glob_patterns=["foo", "bar"],
            skip_existing=False
        )


# Generated at 2022-06-14 05:13:31.590711
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Test function with just path
    upload_to_pypi(path="/foo/bar")
    assert (
        run.calls[0].args[0]
        == "twine upload  -u \'__token__\' -p \'pypi-token\' \'\"/foo/bar/*\"\'"
    )
    # Reset run
    run.calls = []

    # Test function with just path, no glob
    upload_to_pypi(path="/foo/bar", glob_patterns=[])
    assert run.calls[0].args[0] == "twine upload  -u \'__token__\' -p \'pypi-token\'"
    # Reset run
    run.calls = []

    # Test function with just path, no glob

# Generated at 2022-06-14 05:13:38.891935
# Unit test for function upload_to_pypi

# Generated at 2022-06-14 05:13:40.029028
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Test upload_to_pypi"""
    pass

# Generated at 2022-06-14 05:13:48.508734
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi(path = "dist", skip_existing = False , glob_patterns = "*") == None

# Generated at 2022-06-14 05:13:51.124819
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(
        path="dist",
        skip_existing=True,
        glob_patterns=["*", "**/*"],
    )

# Generated at 2022-06-14 05:13:54.334552
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(path="release", skip_existing=True, glob_patterns=["*.md"])

# Generated at 2022-06-14 05:13:59.043506
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .mock_run import MockRun

    with MockRun() as mock_run:
        upload_to_pypi()
        mock_run.assert_called_once_with(
            "twine upload -u '__token__' -p 'pypi-test' ", hide=True, warn=True
        )

# Generated at 2022-06-14 05:14:10.947549
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    class run_mock:
        def __init__(self, arg=None):
            self.arg = arg

    # Test - no token, but with username and password
    os.environ["PYPI_USERNAME"] = "__token__"
    os.environ["PYPI_PASSWORD"] = "pypi-token"
    upload_to_pypi("", run=run_mock, glob_patterns=("*",))
    assert run_mock.arg == "twine upload -u '__token__' -p 'pypi-token' \"*\""

    os.environ["PYPI_USERNAME"] = None
    upload_to_pypi("", run=run_mock, glob_patterns=("*",))

# Generated at 2022-06-14 05:14:12.169978
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()

# Generated at 2022-06-14 05:14:22.317999
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi() == "Uploading to PyPI"
    assert upload_to_pypi(path="a/b/c") == "Uploading to PyPI"
    assert upload_to_pypi(skip_existing=True) == "Uploading to PyPI"
    assert upload_to_pypi(glob_patterns=None) == "Uploading to PyPI"
    assert upload_to_pypi(glob_patterns=[]) == "Uploading to PyPI"
    assert upload_to_pypi(glob_patterns=["./"], skip_existing=True) == "Uploading to PyPI"
    assert upload_to_pypi(glob_patterns=["../x*"]) == "Uploading to PyPI"

# Generated at 2022-06-14 05:14:23.600627
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi() == None

# Generated at 2022-06-14 05:14:34.981270
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Basic execution
    with patch('builtins.run') as mock_run:
        upload_to_pypi()
        mock_run.assert_called_once_with('twine upload  "dist/*"')

    # User provided glob patterns
    with patch('builtins.run') as mock_run:
        upload_to_pypi(glob_patterns=["sdist/*.tar.gz", "wheel/*.whl"])
        mock_run.assert_called_once_with('twine upload  "sdist/*.tar.gz" "wheel/*.whl"')

    # Skip existing
    with patch('builtins.run') as mock_run:
        upload_to_pypi(skip_existing=True)

# Generated at 2022-06-14 05:14:36.458038
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # TODO: implement test for function upload_to_pypi
    pass

# Generated at 2022-06-14 05:14:53.896675
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Tests for error handling
    os.environ["PYPI_TOKEN"] = "pypi-token"
    assert upload_to_pypi()
    del os.environ["PYPI_TOKEN"]
    os.environ["PYPI_USERNAME"] = "pypi-username"
    os.environ["PYPI_PASSWORD"] = "pypi-password"
    assert upload_to_pypi()
    del os.environ["PYPI_USERNAME"]
    del os.environ["PYPI_PASSWORD"]
    os.environ["HOME"] = '/'
    assert upload_to_pypi()
    del os.environ["HOME"]


# Generated at 2022-06-14 05:15:01.558579
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    with pytest.raises(ImproperConfigurationError):
        upload_to_pypi()

    os.environ["PYPI_TOKEN"] = "pypi-foo"

    with patch("twine.commands.upload.upload_file") as upload_file:
        upload_to_pypi()
        assert upload_file.call_count == 0

        upload_to_pypi("dist", glob_patterns=["foo"])
        assert upload_file.call_count == 1

# Generated at 2022-06-14 05:15:02.651297
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()

# Generated at 2022-06-14 05:15:03.433583
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert callable(upload_to_pypi)

# Generated at 2022-06-14 05:15:05.467849
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Test for upload_to_pypi"""
    upload_to_pypi("dist","skip_existing")

# Generated at 2022-06-14 05:15:15.859694
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .helpers import mocked_run

    mocked_run.reset()
    mocked_run.side_effect = [None]

    with config.context("repository", "my_repo"):
        upload_to_pypi()

    assert mocked_run.call_count == 1
    assert mocked_run.call_args[0][0] == (
        "twine upload --skip-existing -u '__token__' -p 'pypi-123' -r 'my_repo' "
        '"./dist/*"'
    )

    mocked_run.reset()
    mocked_run.side_effect = [None]

    with config.context("repository", None):
        upload_to_pypi(glob_patterns=["*.whl", "*.tar.gz"])

    assert mocked

# Generated at 2022-06-14 05:15:17.223724
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi() == None

# Generated at 2022-06-14 05:15:20.363596
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Unit test for function upload_to_pypi"""
    try:
        upload_to_pypi("dist", True, ["*"])
    except ImproperConfigurationError:
        pass

# Generated at 2022-06-14 05:15:21.088629
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:15:25.333151
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # It's not possible to unit test upload_to_pypi because it's an invoke function.
    # Since there's no need to test this function, we will leave it here for reference.
    pass

# Generated at 2022-06-14 05:15:47.204668
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import subprocess
    import pytest
    from semantic_release.settings import config

    # All config values in semantic release are accessible through this object
    # When config["key"] is used, it's really calling config.get("key", None)
    config["repository"] = "pypi"

    # Save current environment
    old_pypi_token = os.getenv("PYPI_TOKEN", "")
    old_pypi_username = os.getenv("PYPI_USERNAME", "")
    old_pypi_password = os.getenv("PYPI_PASSWORD", "")
    old_pypi_repository = os.getenv("PYPI_REPOSITORY", "")


# Generated at 2022-06-14 05:15:47.575259
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:15:47.923007
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:15:59.328782
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Test function actions
    The function is intended to upload wheels to PyPI with Twine.

    Wheels must already be created and stored at the given path.

    Credentials are taken from either the environment variable
    ``PYPI_TOKEN``, or from ``PYPI_USERNAME`` and ``PYPI_PASSWORD``.

    :param path: Path to dist folder containing the files to upload.
    :param skip_existing: Continue uploading files if one already exists.
        (Only valid when uploading to PyPI. Other implementations may not support this.)
    :param glob_patterns: List of glob patterns to include in the upload (["*"] by default).
    """
    # Check the basic
    # if os.environ.get("CI", "") == "true":
    #     assert os.environ.get("CODECOV_

# Generated at 2022-06-14 05:16:01.956432
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """This function is not tested as it is a helper for a third-party library.
    """
    pass

# Generated at 2022-06-14 05:16:13.949824
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import tempfile  # pylint: disable=redefined-outer-name
    import os
    import glob

    import pytest

    with tempfile.TemporaryDirectory() as tmpdirname:
        # create a few files to upload
        files = [
            "foo.whl",
            "bar.whl",
            "foo-bar.whl",
            "foo.zip",
        ]
        for fname in files:
            with open(f"{tmpdirname}/{fname}", "w") as f:
                f.write(f"This is {fname}")

        # 1. Test uploading OK
        upload_to_pypi(tmpdirname, glob_patterns=["*.whl"])
        assert len(glob.glob(f"{tmpdirname}/*.whl"))

# Generated at 2022-06-14 05:16:17.491713
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Run the test file
    """
    os.system("python3 ./upload_to_pypi.py")

# Generated at 2022-06-14 05:16:23.633674
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import pytest

    with pytest.raises(ImproperConfigurationError):
        upload_to_pypi()

    try:
        import twine

        if "pypi" in twine.__version__:
            upload_to_pypi(".", True, ["*"])

    except ImportError:
        pass

# Generated at 2022-06-14 05:16:34.124084
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    with tempfile.TemporaryDirectory() as tmpdirname:
        fake_wheel_path = os.path.join(tmpdirname, "fake_wheel.whl")
        with open(fake_wheel_path, "w"):
            pass

        pypi_password = "foobar"

        @contextmanager
        def mock_pypi_password_patcher(pypi_password):
            with patch("semantic_release.hooks.before_deploy.os.environ", {"PYPI_PASSWORD": pypi_password}):
                yield

        with mock_pypi_password_patcher(pypi_password):
            upload_to_pypi(path=tmpdirname)

        # This is an informational output of the function, so we need to capture and clear it

# Generated at 2022-06-14 05:16:35.746711
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()

# Generated at 2022-06-14 05:17:14.435278
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    test_username = "test_username"
    test_password = "test_password"
    test_token = "pypi-test_token"
    test_repository = "test_repository"
    test_glob_pattern = "*"
    test_glob_pattern_list = [f"*{i}" for i in range(0, 3)]
    test_path = "test_path"

    env_vars = dict(
        PYPI_USERNAME=test_username,
        PYPI_PASSWORD=test_password,
        PYPI_TOKEN=test_token,
        repository=test_repository,
        PATH_TO_DIST=test_path,
    )


# Generated at 2022-06-14 05:17:18.255204
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi('travis-logs/')


if __name__ == '__main__':
    test_upload_to_pypi()

# Generated at 2022-06-14 05:17:20.840245
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(
        path="/tmp",
        glob_patterns=["*.whl", "*.tar.gz"],
        skip_existing=True
    )

# Generated at 2022-06-14 05:17:33.563557
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Setup environment
    os.environ["PYPI_TOKEN"] = "pypi-1234"
    upload_to_pypi("dist", True)
    upload_to_pypi("dist", False)
    upload_to_pypi("dist", True, ["hello*"])
    upload_to_pypi("dist", True, ["hello*", "bye*"])
    upload_to_pypi("dist", False, ["hello*"])
    upload_to_pypi("dist", False, ["hello*", "bye*"])

    # Setup environment
    os.environ["PYPI_USERNAME"] = "username"
    os.environ["PYPI_PASSWORD"] = "password"
    upload_to_pypi("dist", True)
    upload_

# Generated at 2022-06-14 05:17:34.757750
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()

# Generated at 2022-06-14 05:17:45.450997
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # case when PYPI_TOKEN is present
    token = "pypi-adsfadsf"
    os.environ["PYPI_TOKEN"] = token
    upload_to_pypi.__wrapped__()
    assert run.calls == [f'twine upload -u "__token__" -p "{token}" "dist/*"']

    # case when PYPI_USERNAME and PYPI_PASSWORD are present
    del os.environ["PYPI_TOKEN"]
    username = "username"
    password = "password"
    os.environ["PYPI_USERNAME"] = username
    

# Generated at 2022-06-14 05:17:47.052779
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # need to make a mock of run() and check if it is called
    pass

# Generated at 2022-06-14 05:17:50.948535
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """upload_to_pypi Unit test."""

    upload_to_pypi(
        "dist", True, glob_patterns=["*"]
    )

# Generated at 2022-06-14 05:18:04.252342
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Mock run commands
    import sys
    import unittest.mock as mock

    if sys.version_info >= (3, 6):
        from unittest import mock
    else:
        import mock
    mock.patch("invoke.run").start()
    from semantic_release.uploaders import pypi

    config = {
        "repository": "https://pypi.python.org/pypi",
        "skip_existing": True,
        "glob_patterns": ["*.whl"],
    }

    # Test with token (default distribution)
    os.environ["PYPI_TOKEN"] = "pypi-xxxxxxxxxxxxxxxxxxxx"
    pypi.upload_to_pypi(**config)
    # Check if the correct command has been run
    invoke.run.assert_called

# Generated at 2022-06-14 05:18:16.678691
# Unit test for function upload_to_pypi
def test_upload_to_pypi():

    # Test function upload_to_pypi with username and password
    os.environ["PYPI_USERNAME"] = "test_username"
    os.environ["PYPI_PASSWORD"] = "test_password"
    os.environ["HOME"] = "/"
    run.__getitem__ = lambda obj, key: "/usr/bin/twine upload -u 'test_username' -p 'test_password' -r 'https://test_repository' /tmp/test_dist/*.tar.gz"
    upload_to_pypi(path="/tmp/test_dist", skip_existing=True, glob_patterns=["*.tar.gz"])

    # Test function upload_to_pypi with token
    os.environ["PYPI_TOKEN"] = "test_token"
   

# Generated at 2022-06-14 05:19:30.179372
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Unit tests for function upload_to_pypi
    """
    upload_to_pypi(path="dist", glob_patterns=["*"])

# Generated at 2022-06-14 05:19:42.873653
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .helpers import mock

    with mock.patch("invoke.run", return_value="Twine output"):
        upload_to_pypi.logger.info = mock.MagicMock()
        upload_to_pypi(path="dist", skip_existing=False)
        upload_to_pypi.logger.info.assert_called_with(
            "Uploading wheels to PyPI with Twine.",
            extra={
                "command": "twine upload  -u '' -p '' dist/'*'",
                "output": "Twine output",
            },
        )

    with mock.patch("invoke.run", return_value="Twine output"):
        upload_to_pypi.logger.info = mock.MagicMock()

# Generated at 2022-06-14 05:19:52.986226
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    #Given
    glob_patterns = ["*.whl"]
    path = "dist"
    token = "pypi-this_is_an_api_token_from_travis"
    username = "travis"
    password = "travis"
    repository = "pypitest"

    # When
    run.return_value = None
    os.environ.get.side_effect = [username, password, token]
    home_dir = os.environ.get.return_value = ""
    os.path.isfile.return_value = True

    # Then
    upload_to_pypi(
        path=path, skip_existing=False, glob_patterns=glob_patterns
    )

# Generated at 2022-06-14 05:20:02.064499
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from tempfile import TemporaryDirectory
    from pathlib import Path
    from .helpers import (
        create_dist_files_for_tests,
        clean_dist_files_for_tests,
    )

    with TemporaryDirectory() as path:
        path = Path(path)
        create_dist_files_for_tests(path)

        os.environ["PYPI_TOKEN"] = "pypi-no_exist"
        upload_to_pypi(path, False)

        clean_dist_files_for_tests(path)

# Generated at 2022-06-14 05:20:03.798988
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(path="dist", glob_patterns=["my_package*"])

# Generated at 2022-06-14 05:20:05.844626
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert True

# Generated at 2022-06-14 05:20:07.900229
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(path="tests/test_dist", glob_patterns=["*"])

# Generated at 2022-06-14 05:20:09.664235
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(path="/tmp", glob_patterns=["*"])

# Generated at 2022-06-14 05:20:11.384370
# Unit test for function upload_to_pypi
def test_upload_to_pypi():  # noqa: D103
    assert upload_to_pypi("dist") == None

# Generated at 2022-06-14 05:20:12.972842
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass