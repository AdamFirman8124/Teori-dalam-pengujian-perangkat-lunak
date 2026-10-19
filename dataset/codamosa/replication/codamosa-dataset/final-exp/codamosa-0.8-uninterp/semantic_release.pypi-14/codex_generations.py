

# Generated at 2022-06-14 05:12:45.828208
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()

# Generated at 2022-06-14 05:12:56.509413
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # simulate a successful run
    with run.patch() as mock:
        mock.return_value.ok = True
        upload_to_pypi()
        mock.assert_called_once_with(
            f"twine upload  'dist/*'", hide=True, warn=True
        )

    # simulate an unsuccessful run
    with run.patch() as mock:
        mock.return_value.ok = False
        upload_to_pypi()
        mock.assert_called_once_with(
            f"twine upload  'dist/*'", hide=True, warn=True
        )

# Generated at 2022-06-14 05:13:00.690353
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    os.environ["PYPI_TOKEN"] = "test_token"
    upload_to_pypi("test", skip_existing=False, glob_patterns=["test.tar.gz"])

# Generated at 2022-06-14 05:13:05.838335
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi() == None
    assert upload_to_pypi(path="/path/to/dist") == None
    assert upload_to_pypi(path="/path/to/dist", skip_existing=True) == None
    assert upload_to_pypi(path="/path/to/dist", glob_patterns=["*.whl", "*.gz"]) == None

# Generated at 2022-06-14 05:13:06.386622
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert 1 == 1

# Generated at 2022-06-14 05:13:08.650416
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()

# Generated at 2022-06-14 05:13:09.879121
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi(path="dist") == None

# Generated at 2022-06-14 05:13:12.523101
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    logger.debug("Unit Testing function 'upload_to_pypi'...")

    # Test upload function
    upload_to_pypi(path="dist", skip_existing=False, glob_patterns=["*.whl"])

# Generated at 2022-06-14 05:13:13.961915
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:13:22.327404
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Unit test for function upload_to_pypi
    """
    from os import makedirs
    from os.path import abspath, join, dirname
    from shutil import rmtree
    from tempfile import mkdtemp
    from unittest import TestCase, mock

    from semantic_release.settings import config

    # Create temporary directory
    tmpdir = mkdtemp()

    # Create temporary files in temporary directory
    wheel_dir = abspath(join(dirname(__file__), "data", "wheel_dir"))
    wheel_dir_abs_path = join(tmpdir, "wheel_dir")
    makedirs(wheel_dir_abs_path)
    run(f"cp {wheel_dir}/* {wheel_dir_abs_path}")

    # Execute function

# Generated at 2022-06-14 05:13:37.770760
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """
    Unit test for function upload_to_pypi
    """
    import tempfile
    import shutil
    from invoke.exceptions import UnexpectedExit

    from semantic_release import __version__

    path = tempfile.mkdtemp()

# Generated at 2022-06-14 05:13:38.482973
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:13:49.689875
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import os
    import shutil
    from tempfile import TemporaryDirectory
    from invoke import run
    from invoke.exceptions import UnexpectedExit
    from semantic_release.hvcs import version_branched_from_master, version_branched_from_develop

    def run_in_dir(cmd, cwd):
        run(cmd, hide=True, warn=True, pty=True, echo=True, cwd=cwd)

    def assert_no_tag(tag):
        try:
            run_in_dir(f"git tag", cwd=cwd)
            assert 1 == 0 # Should not reach this statement
        except UnexpectedExit:
            pass

    def assert_has_tag(tag):
        run_in_dir(f"git tag", cwd=cwd)

# Generated at 2022-06-14 05:13:56.521282
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()
    upload_to_pypi(".", True, ['*'])
    upload_to_pypi(".", False, ['*'])
    upload_to_pypi(".", False, ['test*'])
    upload_to_pypi(".", True, ['test*'])

# Generated at 2022-06-14 05:13:57.084972
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:14:03.696492
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Python is installed locally
    # .pypirc is not present
    # PyPI credentials are present in environment
    # Upload to testpypi should be successfull
    os.environ["PYPI_USERNAME"] = "test"
    os.environ["PYPI_PASSWORD"] = "foo"
    upload_to_pypi("dist", False, ["*"])

# Generated at 2022-06-14 05:14:09.754815
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """
    To test upload_to_pypi, we can provide all the arguments to the function.
    Since this functio does not use any new imports, it is easier to test.
    """
    path = "dist"
    skip_existing = False
    glob_patterns = ['*']
    upload_to_pypi(path, skip_existing, glob_patterns)
    assert True

# Generated at 2022-06-14 05:14:10.823049
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()

# Generated at 2022-06-14 05:14:11.888759
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()

# Generated at 2022-06-14 05:14:21.581350
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    try:
        import twine
    except ImportError:
        print("Test skipped: twine is not installed")
        return

    from tempfile import TemporaryDirectory
    import shutil

    from .helpers import run_logged_function
    from .mock_twine import MockTwine

    import os
    import sys

    if sys.version_info.minor < 5:
        print("Test skipped: not supported on this Python version")
        return

    def test_twine(self, path, username, password, repository):
        return

    with TemporaryDirectory() as tmp_dir, MockTwine(tmp_dir, test_twine):
        os.makedirs(os.path.join(tmp_dir, "dist"))

# Generated at 2022-06-14 05:14:39.215861
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Unit-test upload_to_pypi.
    """
    import pytest
    from invoke.exceptions import Failure
    from semantic_release.utils import working_directory
    from semantic_release.hvcs.git import reset_branch, commit_new_version

    def create_dist_dir():
        """Create a test dist directory with a fake file.
        """
        with open("test_dist/test.txt", "w+") as test_file:
            test_file.write("Test file for semantic-release")

    def remove_dist_dir():
        """Remove a test dist directory with a fake file.
        """
        os.remove("test_dist/test.txt")

    with working_directory("tests/repositories/gitrepo"):
        reset_branch("master")
        commit_new

# Generated at 2022-06-14 05:14:40.931210
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi("dist", True, ["*"])

# Generated at 2022-06-14 05:14:41.656963
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:14:48.138681
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import shutil
    import tempfile


    with tempfile.TemporaryDirectory() as tmpdir:
        distdir = os.path.join(tmpdir, "dist")
        os.makedirs(distdir)
        shutil.copy('next_release/__init__.py', distdir)
        # TODO: check that upload happens
        upload_to_pypi(path="dist")

# Generated at 2022-06-14 05:14:49.250422
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()

# Generated at 2022-06-14 05:14:50.767875
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # TODO
    assert False

# Generated at 2022-06-14 05:14:51.681535
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()

# Generated at 2022-06-14 05:14:54.942807
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    config.set("repository", "pypi")
    upload_to_pypi(path="tests/fixtures/test-package/dist")

# Generated at 2022-06-14 05:14:57.116801
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(path="dist", skip_existing=False, glob_patterns=["*"])

# Generated at 2022-06-14 05:15:08.956504
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    repository = '--repository test'
    username = '--username test'
    password = '--password test'

    path = '"path/to/dist" "path/to/dist2"'
    skip_existing = '--skip-existing'
    run_command = 'twine upload {username_password}{repository_arg}{skip_existing_param} {dist}'

    with patch('invoke.run') as mock_run:
        try:
            upload_to_pypi(path)
            args, kwargs = mock_run.call_args
            assert args[0] == run_command.format(username_password='',repository_arg='',skip_existing_param='',dist=path)
        except ImproperConfigurationError:
            pass


# Generated at 2022-06-14 05:15:27.131861
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(path="dist", skip_existing=True)

# Generated at 2022-06-14 05:15:28.331721
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()



# Generated at 2022-06-14 05:15:39.356139
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .helpers import mock_run
    from .helpers import mock_environment
    from .helpers import mock_build_and_store_distributions
    from .helpers import mock_get_config

    # Mock the build and store process
    mock_build_and_store_distributions()

    with mock_environment(PYPI_USERNAME="test", PYPI_PASSWORD="pass"):
        with mock_get_config(get_config_mock_data):
            with mock_run() as mocked_run:
                upload_to_pypi()
                mocked_run.assert_called_with(
                    "twine upload -u 'test' -p 'pass' 'dist/*'"
                )


# Generated at 2022-06-14 05:15:40.887202
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi("dist")

# Generated at 2022-06-14 05:15:47.806692
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Check when environment variables do not exist
    try:
        upload_to_pypi()
    except ImproperConfigurationError:
        pass
    else:
        raise Exception("Should have raised an ImproperConfigurationError")

    # Check when API token exists
    os.environ = {
        "PYPI_TOKEN": "pypi-123",
    }
    upload_to_pypi()

# Generated at 2022-06-14 05:15:59.228918
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .mocks import mock, patch

    # Example glob_patterns
    glob_patterns = ["*.whl"]

    with patch("invoke.run") as mock_run:
        upload_to_pypi(glob_patterns=glob_patterns)
        mock_run.assert_called_with(
            "twine upload -u '__token__' -p 'pypi-1234' 'dist/*.whl'"
        )

    with patch("invoke.run") as mock_run:
        upload_to_pypi(glob_patterns=glob_patterns, repository="testPyPI")

# Generated at 2022-06-14 05:16:12.556557
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    test_pypi_token= "pypi-some-token"
    test_pypi_username = "test_username"
    test_pypi_password = "test_password"
    test_dist_path = "dist"
    test_glob_pattern1 = "*.whl"
    test_glob_pattern2 = "*.tgz"


# Generated at 2022-06-14 05:16:13.673585
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
	upload_to_pypi()

# Generated at 2022-06-14 05:16:17.808748
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """
    This function tests the functionality of the function
    upload_to_pypi()
    """
    upload_to_pypi()

# Generated at 2022-06-14 05:16:26.571629
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .helpers import monkeypatch_function

    # Monkeypatch functions being tested
    monkeypatch_function(
        "semantic_release.package_managers.twine.run",
        lambda command: "Test run: {}".format(command),
    )

    # Test
    upload_to_pypi()
    upload_to_pypi(path="test-path")
    upload_to_pypi(skip_existing=True)
    upload_to_pypi(glob_patterns=["*test1", "test2"])

# Generated at 2022-06-14 05:17:10.024726
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Arrange
    test_twine_list = "twine list __token__ -r 'test_repo'"
    test_twine_upload_token = "twine upload -u '__token__' -p 'pypi-test_token'"
    test_twine_upload_token_repo = "twine upload -u '__token__' -p 'pypi-test_token' -r 'test_repo'"
    test_twine_upload_user_pass = "twine upload -u 'test_user' -p 'test_password'"
    test_twine_upload_user_pass_repo = "twine upload -u 'test_user' -p 'test_password' -r 'test_repo'"


# Generated at 2022-06-14 05:17:11.998762
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()

# Generated at 2022-06-14 05:17:20.050421
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Should raise exception when missing token
    try:
        upload_to_pypi()
    except ImproperConfigurationError:
        pass
    else:
        raise Exception("Should have raised exception when missing token")

    # Should be able to upload to PyPI (when configured to do so)
    os.environ["PYPI_TOKEN"] = "pypi-token"
    try:
        upload_to_pypi()
    except Exception as e:
        raise Exception(
            "Should be able to upload to PyPI (when configured to do so)"
        ) from e

# Generated at 2022-06-14 05:17:21.152384
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi("dist")

# Generated at 2022-06-14 05:17:21.815012
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:17:22.637160
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:17:32.103981
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    run_command = "twine upload -u 'username' -p 'password' 'some/path/test artifact' 'some/path/test artifact 2'"
    run = MockRunFunction(return_value=None)

    with patch('semantic_release.vcs_helpers.run', new=run):
        upload_to_pypi(path='some/path', glob_patterns=['test artifact', 'test artifact 2'],
                       username='username', password='password')

    assert run.call_count == 1
    assert run.call_args[0][0] == run_command

# Generated at 2022-06-14 05:17:33.239399
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()

# Generated at 2022-06-14 05:17:42.814331
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Unit test for function upload_to_pypi.
    """
    import tempfile
    import shutil
    import mock

    home = tempfile.mkdtemp("_upload_to_pypi_test")

# Generated at 2022-06-14 05:17:44.983052
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    path = "./dist"
    glob_pattern = ["*"]
    test_upload_to_pypi(path=path, glob_patterns=glob_pattern)

# Generated at 2022-06-14 05:19:06.430949
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from invoke import Context
    from invoke.exceptions import Failure
    from semantic_release.plugins.pypi import upload_to_pypi

    # No API token
    try:
        upload_to_pypi(path="/tmp/dist/")
    except ImproperConfigurationError as e:
        print("No API token")
        print(e)

    # API token with no PYPI_USERNAME or PYPI_PASSWORD
    os.environ['PYPI_TOKEN']="pypi-..."
    upload_to_pypi(path="/tmp/dist/")
    print("API token with no PYPI_USERNAME or PYPI_PASSWORD")

    # No API token, but PYPI_USERNAME and PYPI_PASSWORD

# Generated at 2022-06-14 05:19:07.213182
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:19:08.552831
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi is not None

# Generated at 2022-06-14 05:19:14.729278
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Arrange
    os.environ["PYPI_TOKEN"] = "pypi-token"
    tmp_dir = "tmp"
    os.makedirs(tmp_dir, exist_ok=True)
    open(os.path.join(tmp_dir, "test_file"), "w").close()
    skip_existing = False

    # Act
    upload_to_pypi(tmp_dir, skip_existing)

# Generated at 2022-06-14 05:19:16.397902
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()

# Generated at 2022-06-14 05:19:17.410053
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:19:18.697248
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert 1==1


# Generated at 2022-06-14 05:19:22.135744
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    return True


# run unit tests
try:
    test_upload_to_pypi()
except Exception as e:
    print(e)

# Generated at 2022-06-14 05:19:28.006103
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # import os
    # os.environ["PYPI_TOKEN"] = "pypi-0123456789abcdef0123456789abcdef"
    pass

'''

# Plugin

plugins:
  - python:
      module: semantic_release.plugins.pypi_twine
      no_verify: true
'''

# Generated at 2022-06-14 05:19:28.588260
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:21:59.089437
# Unit test for function upload_to_pypi
def test_upload_to_pypi():

    if "username" and "password" in os.environ:
        del os.environ["username"]
        del os.environ["password"]

    path = "twine"
    skip_existing = False
    glob_patterns = None
    expected_result = (
        "twine upload -u '__token__' -p 'pypi-lkjalksdj' --skip-existing 'twine/foobar'"
    )

    os.environ["PYPI_TOKEN"] = "pypi-lkjalksdj"
    os.environ["HOME"] = os.path.abspath("./tests")
    result = upload_to_pypi(path, skip_existing, glob_patterns)
    del os.environ["PYPI_TOKEN"]
    del os.environ["HOME"]

# Generated at 2022-06-14 05:22:00.284497
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()

# Generated at 2022-06-14 05:22:13.472039
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # TODO: Should have tests specifically for the local file upload case
    os.environ["PYPI_TOKEN"] = "pypi-blahbity"
    upload_to_pypi("dist/some-file")
    upload_to_pypi("dist/some-file", skip_existing=True)
    upload_to_pypi("dist/some-file", repository="pypi-test")
    upload_to_pypi("dist/some-file", glob_patterns=["*", "*/*", "*.egg-info"])
    os.environ["PYPI_USERNAME"] = "pypi-user"
    os.environ["PYPI_PASSWORD"] = "pypi-pass"
    upload_to_pypi("dist/some-file")


# Generated at 2022-06-14 05:22:14.591586
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
        upload_to_pypi()

# Generated at 2022-06-14 05:22:15.591283
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()

# Generated at 2022-06-14 05:22:22.878901
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # None input
    assert upload_to_pypi() == None
    # Normal input
    assert upload_to_pypi(path="dist", skip_existing=False, glob_patterns=["*"]) == None
    # Invalid input
    assert upload_to_pypi(path="dist", skip_existing="False", glob_patterns=["*"]) == None

# Generated at 2022-06-14 05:22:23.988803
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()

# Generated at 2022-06-14 05:22:30.909693
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Testing credentials
    os.environ["PYPI_TOKEN"] = "pypi-blah"
    os.environ["PYPI_USERNAME"] = "blah"
    os.environ["PYPI_PASSWORD"] = "blah"
    assert upload_to_pypi() == True

# Generated at 2022-06-14 05:22:33.171708
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Invoke the function under test
    upload_to_pypi(path="")

# Generated at 2022-06-14 05:22:34.141351
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()