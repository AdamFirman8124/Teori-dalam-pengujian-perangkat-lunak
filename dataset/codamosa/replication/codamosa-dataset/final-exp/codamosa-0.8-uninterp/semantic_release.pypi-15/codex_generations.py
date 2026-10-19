

# Generated at 2022-06-14 05:13:02.892182
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    def get_call_args(run_mock):
        last_call_index = run_mock.call_count-1
        kwargs = run_mock.call_args_list[last_call_index][1]

        return kwargs["command"]

    with patch.object(invoke.run, "run") as run_mock:
        with patch.object(os, "environ", {"PYPI_TOKEN": "pypi-token"}):
            upload_to_pypi(
                path="/tmp",
                skip_existing=True,
                glob_patterns=["whl1", "whl2"],
            )
        
        command = get_call_args(run_mock)


# Generated at 2022-06-14 05:13:03.731905
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi("dist") == True

# Generated at 2022-06-14 05:13:12.457917
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """
    Test upload_to_pypi
    """
    from .helpers import WorkingDirectory

    # create a temporary directory
    with WorkingDirectory() as wd:
        # create file in temporary directory
        f = open("dev.txt", "w+")
        f.write("dev is a test")
        f.close()

        # create folder in temporary directory
        os.mkdir(os.path.join(wd, "dist"))

        # create file in temporary directory dist
        f = open(os.path.join(wd, "dist", "release.txt"), "w+")
        f.write("release is a test")
        f.close()

        # upload to pypi

# Generated at 2022-06-14 05:13:15.210011
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Unit test to verify the function upload_to_pypi"""
    upload_to_pypi()

    assert True

# Generated at 2022-06-14 05:13:19.433680
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .helpers import mocked_repository_config

    with mocked_repository_config({}):
        upload_to_pypi()

    with mocked_repository_config({"repository": "test_repo"}):
        upload_to_pypi()

# Generated at 2022-06-14 05:13:21.063416
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi is not None

# Generated at 2022-06-14 05:13:25.094612
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    exit_code = run("python setup.py -q sdist bdist_wheel", pty=True, hide=True, warn=True)
    assert exit_code.ok is True
    upload_to_pypi()

# Generated at 2022-06-14 05:13:27.238702
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(
        path="dist", skip_existing=False, glob_patterns=["*"]
    )

# Generated at 2022-06-14 05:13:37.470100
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """
    The function should try to get credentials from the environment,
    check that the arguments are valid and then call twine to upload.
    """
    import tempfile
    from contextlib import contextmanager
    from unittest.mock import patch
    from invoke.run import Result

    repo_name = "pypi_name"
    glob_patterns = ["wheel1.whl", "wheel2.whl"]
    repos = ["c", "d"]
    token = "pypi-xxxxxx"

    @contextmanager
    def mock_environ(**kwargs):
        """Temporarily changes os.environ."""
        original = os.environ.copy()
        try:
            os.environ.update(kwargs)
            yield
        finally:
            os.environ = original


# Generated at 2022-06-14 05:13:39.424628
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(path="dist", skip_existing=True, glob_patterns=["*"])

# Generated at 2022-06-14 05:13:49.511303
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .helpers import mocked_run, mocked_logger
    from .mock_project import Project

    def mock_run_failure(command, *args, **kwargs):
        if "twine upload" in command:
            return False
        return True

    def mock_run_success(command, *args, **kwargs):
        if "twine upload" in command:
            return True
        return True

    config.update({
        "repository": "pypi",
        "dry_run": False,
        "skip_existing": False
    })

    with mocked_logger(logger):

        with Project("project", {"__init__.py": None}):
            with mocked_run(mock_run_failure):
                assert upload_to_pypi() is False

# Generated at 2022-06-14 05:14:02.645320
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .context import cd, env_vars_set, env_vars_unset
    from .helpers import CapturingLoggingHandler
    from .mock_capture import capture_output
    import shutil
    import tempfile
    import invoke

    with capture_output() as (out, err):
        with env_vars_set(
            {"PYPI_USERNAME": "test_user", "PYPI_PASSWORD": "test_pass"}
        ):
            upload_to_pypi("dist", skip_existing=True, glob_patterns=("*",))

    assert out.getvalue().strip() == ""
    assert err.getvalue().strip() == ""


# Generated at 2022-06-14 05:14:13.478492
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .helpers import mock_run
    from .helpers import path_join

    from .helpers import get_temp_path
    base_path = get_temp_path()
    with mock_run(pypi_token="my_pypi_token"):
        upload_to_pypi(
            path=path_join(base_path, "dist"),
            skip_existing=True,
            glob_patterns=["test_upload_to_pypi1", "test_upload_to_pypi2",],
        )

    with mock_run(pypi_user="my_user", pypi_password="my_pass") as mock:
        upload_to_pypi(path=path_join(base_path, "dist"), skip_existing=True)


# Generated at 2022-06-14 05:14:19.185347
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    try:
        os.environ["PYPI_TOKEN"] = "token"
        upload_to_pypi(skip_existing=True)
        assert True
    except:
        assert False
    finally:
        if "PYPI_TOKEN" in os.environ:
            del os.environ["PYPI_TOKEN"]

# Generated at 2022-06-14 05:14:24.284853
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    token = "pypi-token"
    username = "username"
    password = "password"
    home_dir = os.environ.get("HOME", "")
    path = "dist"
    repository = "repository"
    skip_existing = True
    glob_patterns = ["one", "two"]

    os.environ.pop("PYPI_TOKEN", None)
    os.environ.pop("PYPI_USERNAME", None)
    os.environ.pop("PYPI_PASSWORD", None)
    os.environ["HOME"] = "/tmp"
    open(os.path.join(home_dir, ".pypirc"), "w+").close()


# Generated at 2022-06-14 05:14:35.355831
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .helpers import tempdir_context_manager, random_string

    with tempdir_context_manager() as tempdir:
        path = os.path.join(tempdir, "test")
        with open(os.path.join(path, "test.txt"), "w"):
            pass

        test_glob_patterns = ["*.txt", "*.temp"]
        env_vars = {
            "PYPI_TOKEN": "pypi-" + random_string(),
            "PYPI_USERNAME": "",
            "PYPI_PASSWORD": "",
            "PYPI_REPOSITORY": "",
        }


# Generated at 2022-06-14 05:14:38.397019
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi(path="mypath", skip_existing=True) == run("twine upload mypath")

# Generated at 2022-06-14 05:14:42.196930
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Unit test for function upload_to_pypi
    
    """
    upload_to_pypi(
        path = "dist", skip_existing = False, glob_patterns = None
    )

# Generated at 2022-06-14 05:14:43.372400
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi('dist') == None

# Generated at 2022-06-14 05:14:53.487706
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from typing import List, Optional

    upload_to_pypi(path = "dist", skip_existing = False, glob_patterns = None)
    upload_to_pypi(path = "dist", skip_existing = False, glob_patterns = "*.whl")
    upload_to_pypi(path = "dist", skip_existing = False, glob_patterns = "*.tar.gz")
    upload_to_pypi(path = "dist", skip_existing = False, glob_patterns = "*.whl *.tar.gz")
    upload_to_pypi(path = "dist", skip_existing = False, glob_patterns = ["*.whl", "*.tar.gz"])
    upload_to_pypi(path = "dist", skip_existing = False, glob_patterns = ())


# Generated at 2022-06-14 05:15:11.526490
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .helpers import UploadTestServer, MockRun

    import semantic_release.settings
    from semantic_release.vcs import Repo
    from semantic_release.history import get_commit_range
    from semantic_release.hvcs import get_vcs_client

# Generated at 2022-06-14 05:15:21.240820
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import os
    import shutil
    import tempfile
    import glob
    import pytest
    
    from .helpers import LoggedFunction, test_upload_to_pypi

    with LoggedFunction(logger):
        # Test valid token
        os.environ['PYPI_TOKEN'] = 'pypi-test_valid_token'
        with pytest.raises(ImproperConfigurationError):
            test_upload_to_pypi()
        
        # Test invalid token
        os.environ['PYPI_TOKEN'] = 'test_invalid_token'
        with pytest.raises(ImproperConfigurationError):
            test_upload_to_pypi()
            
        # Test invalid token
        os.environ['PYPI_TOKEN'] = 'test_invalid_token'


# Generated at 2022-06-14 05:15:25.893888
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(path = '/Users/anupchandrasekharan/Documents/Projects/2020/September/ReleaseIt/tests/example_project/dist', skip_existing = True, glob_patterns = ['*'])

# Generated at 2022-06-14 05:15:38.215716
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    test_upload_to_pypi.test = False
    os.environ["PYPI_TOKEN"] = ""
    upload_to_pypi()
    os.environ["PYPI_TOKEN"] = "pypi-123456789012345678901"
    upload_to_pypi()
    os.environ["PYPI_TOKEN"] = "abcdef"
    try:
        upload_to_pypi()
    except ImproperConfigurationError as e:
        assert str(e) == 'PyPI token should begin with "pypi-"'

    os.environ["PYPI_TOKEN"] = ""
    os.environ["PYPI_USERNAME"] = ""
    os.environ["PYPI_PASSWORD"] = ""
    upload_to

# Generated at 2022-06-14 05:15:42.745555
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert (
        upload_to_pypi("dist", glob_patterns=["*"])
        == "twine upload -u '__token__' -p 'pypi-test' 'dist/*'"
    )
    assert (
        upload_to_pypi("dist", skip_existing=True, glob_patterns=["*"])
        == "twine upload -u '__token__' -p 'pypi-test' --skip-existing 'dist/*'"
    )

# Generated at 2022-06-14 05:15:43.880640
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(path="./dist", glob_patterns=["*.whl", "*.tar.gz"])

# Generated at 2022-06-14 05:15:55.154650
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from semantic_release.hvcs import write_commit_message
    from .helpers import LoggedFunction

    def mocked_run(cmd):
        return cmd

    # Testing case with token
    token = "pypi-token-token"
    os.environ["PYPI_TOKEN"] = token
    run_ = LoggedFunction(logger)(mocked_run)
    assert upload_to_pypi(run_) == f"twine upload -u '__token__' -p '{token}' {os.path.join(write_commit_message.TEMPLATE_PATH, 'dist')}/*"
    os.environ.pop("PYPI_TOKEN", None)

    # Testing case with username and password
    username = "username"
    password = "password"

# Generated at 2022-06-14 05:16:08.369357
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Ensure that the upload_to_pypi() function works in all scenarios.

    This test is only invoked if the UPLOAD_TO_PYPI_TOKEN environment variable
    is set. This prevents people from accidentally running this test against
    PyPI.
    """
    # Import in function to avoid circular import
    from semantic_release.backends import upload_to_pypi as upload_function

    # Create an empty folder to do the upload to
    upload_dir = "/tmp/upload_to_pypi_tmp_dir"
    os.mkdir(upload_dir)

    # Create test files
    test_files = ["test1.tar.gz", "test2.tar.gz"]

# Generated at 2022-06-14 05:16:16.567060
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    with open('./tests/repo/.pypirc', 'w') as t_pypirc:
        t_pypirc.write(r"""
[distutils]
index-servers=
    pypi
    testpypi

[pypi]
repository: https://upload.pypi.org/legacy/
username: __token__
password: pypi-1234567890

[testpypi]
repository: https://test.pypi.org/legacy/
username: __token__
password: testpypi-1234567890""")

    assert upload_to_pypi() == False

# Generated at 2022-06-14 05:16:28.759188
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    try:
        import twine  # pylint: disable=import-outside-toplevel,unused-import

        run("twine help")
    except:
        raise ImportError("Can't test upload_to_pypi because Twine is not installed.")

    try:
        import keyring  # pylint: disable=import-outside-toplevel,unused-import
        import keyrings.alt  # pylint: disable=import-outside-toplevel,unused-import
    except ImportError:
        raise ImportError("Can't test upload_to_pypi because the package keyring is not installed.")

    try:
        upload_to_pypi()
    except:
        pass  # This is probably because the .pypirc file doesn't yet exist.

# Generated at 2022-06-14 05:16:54.652033
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Unit test for function upload_to_pypi"""
    import tempfile
    import shutil
    import os.path
    import tarfile

    # Prepare a dummy tarball
    tmp_dir = tempfile.mkdtemp()
    tarball = os.path.join(tmp_dir, "dummy.tar.gz")
    with tarfile.open(tarball, "w:gz") as tarball_file:
        content = "dummy".encode("utf-8")
        dummy_file = tarfile.TarInfo(name="dummy")
        dummy_file.size = len(content)
        tarball_file.addfile(dummy_file, io.BytesIO(content))

    # Test with skip_existing=False

# Generated at 2022-06-14 05:16:58.060950
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(skip_existing=True, path="dist")
    upload_to_pypi(skip_existing=False, path="dist", glob_patterns=["*"])

# Generated at 2022-06-14 05:16:58.708398
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:17:10.545742
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """
    Unit test for function upload_to_pypi
    """
    test_path = "test_path"
    test_token = "pypi-abcdefghijklmnopqrstuvwxyz1234567890"
    test_username = "test_username"
    test_password = "test_password"
    test_repo = "test_repo"
    test_glob_patterns = ["test_glob"]
    test_skip_existing = True
    test_dist = f'"{test_path}/{test_glob_patterns[0]}"'
    run_mock = None

    # Use the API token from environment variable PYPI_TOKEN
    run_mock = "token"
    os.environ["PYPI_TOKEN"] = test_token
   

# Generated at 2022-06-14 05:17:22.095198
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Unit test for upload_to_pypi.
    """

    import tempfile

    test_file_name = "test-file.txt"
    test_file_path = os.path.join(tempfile.gettempdir(), test_file_name)

    with open(test_file_path, "w") as test_file:
        test_file.write("Random file contents")

    def test_upload_to_pypi_with_directory(path):
        """Nested helper function for testing upload_to_pypi with some paths."""
        path_to_test_file = os.path.join(path, test_file_name)
        os.rename(test_file_path, path_to_test_file)
        upload_to_pypi(path)

# Generated at 2022-06-14 05:17:34.545809
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import unittest
    import unittest.mock

    # Customize logging level.
    unittest.mock.patch.object(
        logger, "warning",
        unittest.mock.patch.object(logger, "error"),
    )

    # Mock function run.
    run_mock = unittest.mock.Mock(name="run", return_value=None)
    unittest.mock.patch.object(
        upload_to_pypi, "run",
        run_mock,
    )

    # Creating a path with any value will be a valid path for the tests.
    upload_to_pypi_path = "path"

    # Creating a list with any value will be a valid glob_patterns for the tests.
    upload_to_pypi_gl

# Generated at 2022-06-14 05:17:47.465682
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .helpers import mock_run, mock_chdir, mock_os, mock_path_is_dir, mock_logger
    from .helpers import mock_open, mock_path_exists
    from .helpers import get_calls_to_run

    # Setup mocks
    mock_chdir.mock_clear()
    mock_run.mock_clear()
    mock_os.mock_clear()
    mock_path_is_dir.mock_clear()
    mock_path_exists.mock_clear()
    mock_os.environ = {}
    mock_logger.mock_clear()
    mock_open.mock_clear()

    # Test 1: Missing credentials
    #
    # Expected behavior:
    # 1. Raise ImproperConfigurationError
    # 2. Include

# Generated at 2022-06-14 05:17:55.809512
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    def mock_run(command):
        assert (
            command.strip() == 'twine upload -u \'__token__\' -p \'pypi-token\' --skip-existing "./dist/Sphinx-1.4.4-py3-none-any.whl"'
        )

    with mock.patch.object(invoke, 'run', side_effect=mock_run) as mock_run:
        upload_to_pypi(
            path="./dist",
            skip_existing=True,
            glob_patterns=["Sphinx-1.4.4-py3-none-any.whl"],
        )



# Generated at 2022-06-14 05:17:59.581443
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Testing upload_to_pypi"""
    upload_to_pypi(path="dist", skip_existing=False, glob_patterns=None)

# Generated at 2022-06-14 05:18:07.953461
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .helpers import MockConfig
    import tempfile
    import os
    from shutil import rmtree

    _test_folder = tempfile.mkdtemp()
    try:
        config.set_config(MockConfig())
        config["repository"] = "https://test.pypi.python.org/pypi"

        with open("{}/testfile.txt".format(_test_folder), "w") as testfile:
            testfile.write("Test")

        upload_to_pypi(_test_folder, glob_patterns=["*"])
    finally:
        rmtree(_test_folder)

# Generated at 2022-06-14 05:18:54.686504
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from semantic_release.settings import config
    config["repository"] = "https://test.pypi.org/legacy/"
    os.environ["PYPI_USERNAME"] = "test"
    os.environ["PYPI_PASSWORD"] = "test"
    try:
        upload_to_pypi(path="./semantic_release/tests/data")
    except ImproperConfigurationError:
        pass #If Twine is not installed, upload will not work, this is ok, we are just testing.
    del os.environ["PYPI_USERNAME"]
    del os.environ["PYPI_PASSWORD"]
    os.environ["PYPI_TOKEN"] = "test"

# Generated at 2022-06-14 05:19:08.309992
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import shutil
    from pathlib import Path

    from semantic_release.hvcs import git
    from semantic_release.settings import config
    from semantic_release.settings import first_config, Config

    config.load_dict(first_config)
    config.set_by_name("version_variable", "__version__")
    config.set_by_name("dry_run", True)

    source_repo = git.create_repo(path="test_git_repo")
    source_repo.create_file("repo-file", None, "add")
    source_repo.create_release("0.1.0", "release 0.1.0")
    shutil.copytree("test_git_repo", "test_git_repo_dest")

# Generated at 2022-06-14 05:19:09.909771
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    return


# Generated at 2022-06-14 05:19:18.051892
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from unittest.mock import patch, Mock
    from .helpers import dummy_run

    with patch("invoke.run", dummy_run):
        upload_to_pypi("dist", True, ["*.tar.gz", "*.whl"])

    args, kwargs = dummy_run.call_args
    # Argument order is not guaranteed in `twine upload` so testing args is not reliable
    assert (
        "twine upload  --skip-existing 'dist/*.tar.gz' 'dist/*.whl'"
        == kwargs["command"]
    )
    assert "semantic_release.download_helpers" in kwargs["hide"]
    assert "semantic_release.plugins.pypi" in kwargs["hide"]

# Generated at 2022-06-14 05:19:30.168434
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import glob
    import pathlib
    import tempfile

    with tempfile.TemporaryDirectory() as tmp:
        path = pathlib.Path(tmp)
        (path / "foobar").touch()

        # Test failure case: missing credentials
        with pytest.raises(ImproperConfigurationError) as e:
            upload_to_pypi(path=tmp)

        # Test success case
        os.environ["PYPI_TOKEN"] = "pypi-a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6"
        upload_to_pypi(path=tmp)

# Generated at 2022-06-14 05:19:30.850591
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:19:32.081856
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:19:32.845506
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:19:35.716352
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    try:
        args = vars()
        upload_to_pypi(**args)
    except ImproperConfigurationError:
        pass

# Generated at 2022-06-14 05:19:36.423422
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert True

# Generated at 2022-06-14 05:20:47.964553
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .helpers import temp_chdir

    with temp_chdir() as d:
        os.mkdir("dist")
        with open(os.path.join("dist", "test-0.1-py2.py3-none-any.whl"), "w"):
            pass
        upload_to_pypi()


__all__ = [
    "upload_to_pypi",
]

# Generated at 2022-06-14 05:20:53.355356
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import pytest

    # Can't use pytest's raises() context manager to verify the exact string
    with pytest.raises(ImproperConfigurationError):
        upload_to_pypi(skip_existing=False)

    with pytest.raises(ImproperConfigurationError):
        os.environ['PYPI_TOKEN'] = "something_that_does_not_start_with_pypi-"
        upload_to_pypi(skip_existing=False)

# Generated at 2022-06-14 05:20:57.373653
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    temp_dir = tempfile.TemporaryDirectory()
    wheel_file = "semantic-release-2.9.0.0-py3-none-any.whl"
    wheel_path = os.path.join(temp_dir.name, wheel_file)
    open(wheel_path, "a").close()
    upload_to_pypi(path=temp_dir.name, glob_patterns=[wheel_file])

# Generated at 2022-06-14 05:21:02.798330
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import tempfile
    import shutil
    import glob
    import os
    import pytest

    def run_twine(c, **kwargs):
        from invoke import UnexpectedExit
        try:
            run(c, **kwargs)
        except UnexpectedExit:
            pass

    # Create some files to upload
    with tempfile.TemporaryDirectory() as dist_dir:
        test_files = ["test_file1.txt", "test_file2.txt"]
        for test_file in test_files:
            with open(os.path.join(dist_dir, test_file), "w+") as fd:
                fd.write("Test")

        # Dry run a successful upload

# Generated at 2022-06-14 05:21:11.892140
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    os.environ["PYPI_USERNAME"] = "user"
    os.environ["PYPI_PASSWORD"] = "password"
    assert not upload_to_pypi.called
    upload_to_pypi()
    assert upload_to_pypi.called

    upload_to_pypi.reset_mock()
    os.environ["PYPI_TOKEN"] = "pypi-token"
    assert not upload_to_pypi.called
    upload_to_pypi()
    assert upload_to_pypi.called

# Generated at 2022-06-14 05:21:25.418297
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Check error for missing PYPI_TOKEN
    try:
        upload_to_pypi()
    except ImproperConfigurationError:
        pass

    # Check error for bad token
    try:
        os.environ["PYPI_TOKEN"] = "bAdtOkEn"
        upload_to_pypi()
    except ImproperConfigurationError:
        pass

    # Check error for missing PYPI_USERNAME
    os.environ["PYPI_TOKEN"] = None
    try:
        upload_to_pypi()
    except ImproperConfigurationError:
        pass

    # Check error for missing PYPI_PASSWORD
    os.environ["PYPI_USERNAME"] = "baduser"

# Generated at 2022-06-14 05:21:26.271529
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert False, "Test not implemented"

# Generated at 2022-06-14 05:21:38.010285
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import pytest
    from unittest.mock import patch
    from unittest.mock import mock_open
    import semantic_release

    with patch("invoke.run", return_value=None) as patch_run:
        semantic_release.upload_to_pypi()

    patch_run.assert_called_with(
        "twine upload -u '__token__' -p 'pypi-ABCDEFG' --skip-existing 'dist/*'"
    )
    assert patch_run.call_count == 1

    with patch("invoke.run", return_value=None) as patch_run:
        semantic_release.upload_to_pypi(
            path="dist/test", username="test", password="test", skip_existing=True
        )


# Generated at 2022-06-14 05:21:46.019584
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # No glob patterns
    os.environ["PYPI_USERNAME"] = "test"
    os.environ["PYPI_PASSWORD"] = "test"
    upload_to_pypi(glob_patterns=[])
    del os.environ["PYPI_USERNAME"]
    del os.environ["PYPI_PASSWORD"]
    # Glob patterns
    os.environ["PYPI_TOKEN"] = "test"
    upload_to_pypi(path="test", glob_patterns=["test"])
    del os.environ["PYPI_TOKEN"]

    # Skip existing
    os.environ["PYPI_USERNAME"] = "test"
    os.environ["PYPI_PASSWORD"] = "test"
    upload_to_

# Generated at 2022-06-14 05:21:46.746049
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass