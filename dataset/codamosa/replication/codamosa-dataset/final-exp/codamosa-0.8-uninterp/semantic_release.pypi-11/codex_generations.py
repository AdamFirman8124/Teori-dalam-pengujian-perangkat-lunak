

# Generated at 2022-06-14 05:12:52.166335
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    path = "dist"
    glob_patterns = ["*"]
    os.environ["PYPI_TOKEN"] = "pypi-sometoken"
    upload_to_pypi(path, glob_patterns=glob_patterns)

# Generated at 2022-06-14 05:12:52.848002
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
  pass

# Generated at 2022-06-14 05:12:59.354833
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    config.update({"repository": "test-repo"})
    os.environ["PYPI_USERNAME"] = "test_user"
    os.environ["PYPI_PASSWORD"] = "test_password"
    upload_to_pypi("dist_folder", skip_existing=True, glob_patterns=["pattern"])


# Generated at 2022-06-14 05:13:00.043262
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:13:00.731316
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:13:02.834866
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Tests function upload_to_pypi"""
    print('Testing upload_to_pypi')
    assert True

# Generated at 2022-06-14 05:13:03.694599
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()

# Generated at 2022-06-14 05:13:12.456349
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # pylint: disable=import-outside-toplevel
    from semantic_release import helpers
    from semantic_release.hvcs_helpers import mock

    pypi_token = "This would be a token"
    pypi_username = "username"
    pypi_password = "password"
    pypi_repository = "pypi-test"

    glob_patterns = ["*"]
    dist_package_1 = "dist/package1-1.0.0-py3-none-any.whl"
    dist_package_2 = "dist/package2-1.0.0-py3-none-any.whl"
    dist = f"{dist_package_1} {dist_package_2}"

# Generated at 2022-06-14 05:13:21.845230
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Arrange
    import glob
    import shutil

    os.environ["PYPI_USERNAME"] = "myusername"
    os.environ["PYPI_PASSWORD"] = "mypassword"

    path = "tests/test_upload_to_pypi"
    if os.path.isdir(path):
        shutil.rmtree(path)
    os.mkdir(path)
    open(os.path.join(path, "file1.txt"), "w").close()
    open(os.path.join(path, "file2.txt"), "w").close()

    # Act
    upload_to_pypi(path)

    # Assert
    assert len(glob.glob(path + "/*")) == 2

# Generated at 2022-06-14 05:13:24.781111
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(glob_patterns=["test"])

# Generated at 2022-06-14 05:13:30.777164
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert (upload_to_pypi("dist", True, ["*"]) == None)

# Generated at 2022-06-14 05:13:38.646313
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """
    Calling upload_to_pypi should execute twine command
    with correct parameters.
    """
    path = "dist"
    glob_patterns = ["*"]
    repository = "test-repository"
    username = "u"
    password = "p"
    token = "t"
    os.environ["PYPI_USERNAME"] = username
    os.environ["PYPI_PASSWORD"] = password
    os.environ["PYPI_TOKEN"] = token

    def side_effect(*args, **kwargs):
        command = kwargs.get("echo")
        assert command is not None

# Generated at 2022-06-14 05:13:41.593498
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()
    upload_to_pypi(path="~/dist", skip_existing=True, glob_patterns=["*", "**"])

# Generated at 2022-06-14 05:13:47.828562
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Ensure the upload_to_pypi function executes and returns without exceptions.
    """
    glob_patterns = ["*a*", "*b*"]
    assert not upload_to_pypi(glob_patterns=glob_patterns, skip_existing=True)
    assert not upload_to_pypi()
    assert not upload_to_pypi(skip_existing=True)

# Generated at 2022-06-14 05:13:52.038344
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    os.environ["PYPI_TOKEN"] = "pypi-token"
    try:
        upload_to_pypi(glob_patterns=["test.zip"])
    except:
        raise
    finally:
        os.environ.pop("PYPI_TOKEN")
    assert 1

# Generated at 2022-06-14 05:14:04.038083
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Test function upload_to_pypi
    """
    from semantic_release.utils import parse_version

    import semantic_release.hvcs as hvcs
    import semantic_release.settings as settings
    import semantic_release.history as history
    import semantic_release.vcs as vcs
    import semantic_release.packages as packages

    if "pypi" not in settings.config["ci"]:
        return

    with vcs.create() as repo:
        if not repo.working_dir_is_clean():
            repo.commit_all("Release commit")

        # Create a commit
        with open("test_file.txt", "w") as f:
            print(f"Dummy content", file=f)
        repo.add("test_file.txt")
        repo.commit("Change test file")
       

# Generated at 2022-06-14 05:14:10.371117
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    dist = "dist"
    glob_patterns = ["*"]
    username = "__token__"
    password = "pypi-adfasfadfasd"

    response = upload_to_pypi(dist=dist, glob_patterns=glob_patterns, skip_existing=True)

    assert response == f"twine upload -u '{username}' -p '{password}'  --skip-existing 'dist/*'"


# Generated at 2022-06-14 05:14:16.405527
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    delete_env("PYPI_TOKEN")
    assert not upload_to_pypi.__wrapped__()

    set_env("PYPI_TOKEN", "testing")
    assert not upload_to_pypi.__wrapped__()

    set_env("PYPI_TOKEN", "pypi-testing")
    assert not upload_to_pypi.__wrapped__()

# Generated at 2022-06-14 05:14:21.205490
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Create fake repository credentials
    os.environ["PYPI_USERNAME"] = "test_username"
    os.environ["PYPI_PASSWORD"] = "test_password"
    upload_to_pypi()
    del os.environ["PYPI_USERNAME"]
    del os.environ["PYPI_PASSWORD"]


# Generated at 2022-06-14 05:14:22.909743
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi()

# Generated at 2022-06-14 05:14:35.967701
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Test upload_to_pypi helper function.
    """
    upload_to_pypi()
    upload_to_pypi(path="dist", skip_existing=True, glob_patterns=["*"])
    upload_to_pypi(path="dist", skip_existing=False, glob_patterns=["*"])

# Generated at 2022-06-14 05:14:49.349571
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import tempfile
    from unittest.mock import patch

    from invoke import Context

    from .helpers import LoggedFunction

    with tempfile.TemporaryDirectory() as tmpdirname:
        testfile = "test.txt"
        testfolder = "testfolder"
        testpath = os.path.join(tmpdirname, testfolder, testfile)

        os.makedirs(tmpdirname + "/" + testfolder)
        with open(testpath, "w") as f:
            f.write("test")

        with patch("invoke.run") as run:
            with patch.dict("os.environ", {"PYPI_TOKEN": "pypi-testtoken"}, clear=True):
                upload_to_pypi(tmpdirname, True, ["testfolder/**"])
                run.assert_called_

# Generated at 2022-06-14 05:14:58.403254
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Arrange
    import tempfile
    from textwrap import dedent

    # Create setup.cfg with pypi section
    with tempfile.NamedTemporaryFile("w", delete=False) as f:
        f.write(
            dedent(
                """
            [distutils]
            index-servers=pypi
            """
            )
        )
    # Create ~/.pypirc with pypi username and password
    with open(os.path.expanduser("~/.pypirc"), "w") as f:
        f.write(
            dedent(
                """
            [distutils]
            index-servers=pypi
            """
            )
        )
    # Create tmp setup file that will be uploaded

# Generated at 2022-06-14 05:14:59.625292
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi("dist")

# Generated at 2022-06-14 05:15:10.462877
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from unittest.mock import patch, call
    from semantic_release.plugins.pypi_plugin import upload_to_pypi
    import os

    with patch("invoke.run") as mock_run:
        # Should 401 with no credentials
        upload_to_pypi()
        assert mock_run.call_count == 1
        assert mock_run.call_args[0][0] == "twine upload *"
        mock_run.reset_mock()

        # Should be fine with PYPI_TOKEN env var
        os.environ["PYPI_TOKEN"] = "pypi-example_token"
        upload_to_pypi()
        assert mock_run.call_count == 1

# Generated at 2022-06-14 05:15:12.653156
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi("dist", skip_existing=False, glob_patterns=["*"])

# Generated at 2022-06-14 05:15:17.583079
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # The function upload_to_pypi runs an invoke command, which will fail in unit testing.
    # Assumes a shell script run to test the script.
    # (Unit testing with invoke will be difficult unless ran in the same shell environment.)
    print(config.get('repository'))

# Generated at 2022-06-14 05:15:21.857658
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    os.environ['PYPI_TOKEN'] = 'pypi-token'
    os.environ['PYPI_USERNAME'] = 'pypi-username'
    os.environ['PYPI_PASSWORD'] = 'pypi-password'
    upload_to_pypi()

# Generated at 2022-06-14 05:15:35.252409
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    run_spy = run_spy = run
    run_spy.return_value = None
    dummy_path = "dummy_path"
    dummy_glob_patterns = ["*"]
    dummy_token = "dummy_token"
    dummy_username = "dummy_username"
    dummy_password = "dummy_password"
    dummy_repository = "dummy_repository"
    expected_token_call = "twine upload -u '__token__' -p 'dummy_token'"
    expected_username_password_call = "twine upload -u 'dummy_username' -p 'dummy_password'"

    # when no credentials are provided
    os.environ = {}

# Generated at 2022-06-14 05:15:35.771517
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert True

# Generated at 2022-06-14 05:15:54.285767
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(
        path="dist", skip_existing=False, glob_patterns=["*"]
    )

# Generated at 2022-06-14 05:15:56.526545
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    exit_status = upload_to_pypi()
    assert exit_status == 0

# Generated at 2022-06-14 05:16:09.182747
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Unit test for function upload_to_pypi."""
    # Import needed for unit test
    from invoke import MockContext

    # Local imports
    from semantic_release.uploaders import pypi
    from semantic_release.exceptions import UploadError

    mock_context = MockContext()

    # Test case where missing credentials
    os.environ["PYPI_TOKEN"] = ""
    os.environ["PYPI_USERNAME"] = ""
    os.environ["PYPI_PASSWORD"] = ""

    with mock_context:
        with mock_context.cd(os.path.expanduser("~")):
            with open("test_upload_to_pypi.txt", "w") as f:
                f.write("any content")


# Generated at 2022-06-14 05:16:12.356723
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    path = "dist_test"
    glob_patterns = ["*"]
    upload_to_pypi(path, glob_patterns)

# Generated at 2022-06-14 05:16:13.867237
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi("dist", True, ["*"])

# Generated at 2022-06-14 05:16:14.829759
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:16:28.374377
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Unit test for upload_to_pypi
    """
    # pylint: disable=missing-function-docstring, invalid-name
    try:
        upload_to_pypi()
    except ImproperConfigurationError as e:
        assert "Missing credentials" in str(e)

    with open(os.path.join(os.environ.get("HOME", ""), ".pypirc"), "w") as pypirc:
        pypirc.write("[distutils]\nindex-servers = pypi\n\n[pypi]\nrepository: https://upload.pypi.org/legacy/")
    upload_to_pypi(glob_patterns=["some-*.whl"])

# Generated at 2022-06-14 05:16:29.382451
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()

# Generated at 2022-06-14 05:16:43.416092
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """
    Unit testing for function upload_to_pypi
    """

    # Test when missing credentials
    try:
        upload_to_pypi()
        assert False
    except ImproperConfigurationError:
        assert True

    # Test when missing repo
    os.environ["PYPI_TOKEN"] = "pypi-abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    try:
        upload_to_pypi()
        assert False
    except TypeError:
        assert True

    # Test when bad repo
    config["repository"] = "https://upload.pypi_bad_repo.org"
    try:
        upload_to_pypi()
        assert False
    except TypeError:
        assert True

# Generated at 2022-06-14 05:16:47.175352
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Unit test for function upload_to_pypi"""
    upload_to_pypi(path="tests/fixtures", skip_existing=True, glob_patterns=["*"])

# Generated at 2022-06-14 05:17:28.468687
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # GIVEN
    glob_patterns = ["foo"]
    repository = "test-repository"
    dist = "dist"
    skip_existing = False

    config.set("repository", repository)

    def fake_run(cmd, hide=True, warn=True):
        assert cmd == (
            "twine upload -u '__token__' -p 'pypi-sometoken' -r 'test-repository' "
            '"dist/foo"'
        )

    # WHEN
    upload_to_pypi(dist, skip_existing, glob_patterns, fake_run)

    # THEN
    assert True



# Generated at 2022-06-14 05:17:37.328627
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    token = os.environ["PYPI_TOKEN"]
    file_name = 'semantic-release-1.5.1.tar.gz'
    folder_path = os.path.join('examples', 'pypi_setup')
    assert not upload_to_pypi(path=folder_path, glob_patterns=[])
    os.environ["PYPI_TOKEN"] = 'test-pypi'
    assert upload_to_pypi(path=folder_path, glob_patterns=[])
    assert not upload_to_pypi(path=folder_path, skip_existing=True)
    os.environ["PYPI_TOKEN"] = token

# Generated at 2022-06-14 05:17:40.613322
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi('dist', False, ['*'])

# Generated at 2022-06-14 05:17:43.349698
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Test upload_to_pypi function."""
    assert run('twine upload dist/* -u test -p test', warn=True).exited == 1

# Generated at 2022-06-14 05:17:46.604557
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    with mock.patch("invoke.run") as mock_run:
        upload_to_pypi()
        mock_run.assert_called_once_with(
            "twine upload  -u '__token__' -p 'pypi-notpretendingthisisavalidtoken' *"
        )



# Generated at 2022-06-14 05:17:50.368415
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(path="./tests/resources/dist", glob_patterns=["testpkg-0.0.1-py3-none-any.whl"])

# Generated at 2022-06-14 05:17:54.378131
# Unit test for function upload_to_pypi
def test_upload_to_pypi():

    try:
        upload_to_pypi()
    except ImproperConfigurationError as e:
        print(e)

if __name__ == "__main__":
    test_upload_to_pypi()

# Generated at 2022-06-14 05:18:00.863949
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from mlrun import new_function
    from mlrun.platforms.local import LocalRuntime

    fn = new_function(handler='upload_to_pypi')
    # Add local runtime handler
    fn.apply(LocalRuntime())
    result = fn.run()
    assert result.output == "No upload token or username/password found"

# Generated at 2022-06-14 05:18:11.516668
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import tempfile
    import shutil
    import random
    import string
    random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
    tmpdir = tempfile.mkdtemp()
    dist_dir = tempfile.mkdtemp(dir=tmpdir)
    with open(os.path.join(dist_dir, f"{random_string}.whl"), "w") as f:
        f.write(random_string)
    try:
        upload_to_pypi(path=dist_dir)
    finally:
        shutil.rmtree(tmpdir)

# Generated at 2022-06-14 05:18:19.396346
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import pytest
    #from semantic_release.plugins.pypi import upload_to_pypi
    with pytest.raises(ImproperConfigurationError):
        upload_to_pypi()

    os.environ['PYPI_USERNAME'] = 'username'
    os.environ['PYPI_PASSWORD'] = 'password'
    with pytest.raises(ImproperConfigurationError):
        upload_to_pypi()
    os.environ['PYPI_TOKEN'] = 'pypi-token'
    upload_to_pypi()

# Generated at 2022-06-14 05:19:41.938671
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .helpers import (
        LoggedFunctionTestCase,
        create_test_package,
        set_environ,
        remove_environ,
        captured_logging,
    )
    from .test_helpers import dummy_release
    import shutil
    import tempfile

    class UploadToPyPiTestCase(LoggedFunctionTestCase):
        def setUp(self):
            self.tempdir = tempfile.mkdtemp(prefix="semantic_release_test_")
            self.old_cwd = os.getcwd()
            self.cwd = os.path.join(self.tempdir, "repository")
            os.makedirs(self.cwd)
            os.chdir(self.cwd)

# Generated at 2022-06-14 05:19:42.848691
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()

# Generated at 2022-06-14 05:19:44.771156
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(path="dist", skip_existing=False, glob_patterns=None)

# Generated at 2022-06-14 05:19:48.301580
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Unit test for function upload_to_pypi."""
    upload_to_pypi('tests',True,['*'])

# Generated at 2022-06-14 05:19:49.416885
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()

# Generated at 2022-06-14 05:19:50.845579
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()

# Generated at 2022-06-14 05:19:51.691933
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert True

# Generated at 2022-06-14 05:20:04.054457
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi() == None
    assert upload_to_pypi('dist',True,["*"]) == None
    assert upload_to_pypi('dist',False,["*"]) == None
    assert upload_to_pypi('dist',True,["*"]) == None
    assert upload_to_pypi('dist',True,['*.py', '*.rst']) == None
    assert upload_to_pypi('dist',True,['*', '*.rst']) == None
    assert upload_to_pypi('dist',False,['*', '*.rst']) == None
    assert upload_to_pypi('dist',False,['*.py', '*.rst']) == None

# Generated at 2022-06-14 05:20:06.123152
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:20:18.428170
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from . import helpers
    from .helpers import LoggedFunction
    from .helpers import run_mock
    from unittest.mock import patch
    from pathlib import Path
    from tempfile import TemporaryDirectory

    test_repo = Path(__file__).parent.parent

    def test_case(
        username,
        password,
        token,
        repo,
        skip_existing,
        dist_file,
        expected_call,
        expected_cwd,
        expected_env,
    ):
        with TemporaryDirectory() as dist_dir:
            dist_dir = Path(dist_dir)
            dist_dir.joinpath("test.dist").touch()
            with patch("invoke.run", autospec=True, side_effect=run_mock) as run_mock:

                upload_to_pyp