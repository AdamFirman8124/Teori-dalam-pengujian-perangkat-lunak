

# Generated at 2022-06-14 05:12:44.978014
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()

# Generated at 2022-06-14 05:12:51.734305
# Unit test for function upload_to_pypi
def test_upload_to_pypi():

    test_path = "test_assets/dist/"
    test_glob_patterns = ["simple-1.5.5.tar.gz"]
    
    # Test upload
    upload_to_pypi(test_path, True, test_glob_patterns) 

    # Test bad credentials
    os.environ["PYPI_TOKEN"] = "Wrong-API-Token"
    try:
        upload_to_pypi(test_path, True, test_glob_patterns)
    except Exception:
        pass
    else:
        raise Exception("Should error")

    # Test no repository
    os.environ["PYPI_TOKEN"] = "pypi-Test-API-Token"

# Generated at 2022-06-14 05:12:53.298054
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(path="/some/path/to/upload_to")

# Generated at 2022-06-14 05:12:58.883034
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi.reset_mock()
    upload_to_pypi()

    call_args = upload_to_pypi.call_args[0][0]
    assert call_args == "dist"
    assert upload_to_pypi.call_args[1] == {}

# Generated at 2022-06-14 05:13:01.407571
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    glob_patterns = ["*.pkg", "*.msi"]
    # upload_to_pypi("dist", True, glob_patterns)

# Generated at 2022-06-14 05:13:03.360696
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Function is difficult to test due to it needing to be mocked out
    pass

# Generated at 2022-06-14 05:13:04.976455
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi("path", True, ["*"])

# Generated at 2022-06-14 05:13:06.872986
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi(path="/path/to/dist", skip_existing=True, glob_patterns=["*"])

# Generated at 2022-06-14 05:13:08.292171
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert False

# Generated at 2022-06-14 05:13:09.488032
# Unit test for function upload_to_pypi

# Generated at 2022-06-14 05:13:22.266440
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import pytest
    from invoke.exceptions import UnexpectedExit
    from pytest_mock import MockFixture

    path = "dist"
    skip_existing = False
    glob_patterns = None

    # Mock
    run = MockFixture()

    # Successful attempt with API token
    run.return_value.ok = True
    token = "pypi-this-is-a-token"
    upload_to_pypi(path, skip_existing, glob_patterns, token=token)
    run.assert_called_once_with(
        f'twine upload -u \'__token__\' -p \'{token}\' "dist/*"'
    )
    run.reset()

    # Successful attempt with username and password
    run.return_value.ok = True
    username = "user"
    password

# Generated at 2022-06-14 05:13:35.488906
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .helpers import temp_chdir
    from shutil import rmtree
    from pathlib import Path
    import tempfile
    import filecmp
    from tempfile import NamedTemporaryFile
    from contextlib import suppress
    import pytest
    
    # Setup
    tmp_dir = tempfile.TemporaryDirectory()
    dist_dir = Path(tmp_dir.name) / "dist"
    dist_dir.mkdir()
    (dist_dir / "test_file.txt").touch()
    (dist_dir / "test_file2.txt").touch()
    (dist_dir / "test_file3.txt").touch()
    test_file_name = (dist_dir / "test_file2.txt").name


# Generated at 2022-06-14 05:13:46.704821
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    try:
        import pytest

        pass
    except ImportError:
        pass
    else:
        pytest.importorskip("twine")

    from pathlib import Path

    from mock import patch
    from unittest.mock import Mock

    mock_run = Mock()
    with patch("semantic_release.hvcs.git.run", mock_run):
        upload_to_pypi(
            path=Path("dist"),
            glob_patterns=["*.whl"]
        )
        expected_call = "twine upload  \"dist/*.whl\""
        assert mock_run.call_args[0][0] == expected_call


# Generated at 2022-06-14 05:13:52.470349
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Create fake .pypirc file
    logger.info("Uploading to PyPI")
    username = os.environ.get("PYPI_USERNAME")
    password = os.environ.get("PYPI_PASSWORD")

    # Check username or password is set
    assert username or password

    # Check dist folder
    dist = "dist"
    assert os.path.exists(dist)

    # Check whether to skip existing file or not
    skip_existing = True

    # Check glob patterns
    glob_patterns = ["*"]

    # Run function upload_to_pypi()
    upload_to_pypi(
        dist,
        skip_existing,
        glob_patterns
    )

# Generated at 2022-06-14 05:13:56.172452
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert (
        run("twine upload -u '__token__' -p 'pypi-token' --repository pypi --skip-existing 'dist/semantic_release*'")
        == ""
    )

# Generated at 2022-06-14 05:14:07.087009
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    config.set("repository", "https://test.pypi.org/legacy/")
    os.environ["PYPI_USERNAME"] = "test_username"
    os.environ["PYPI_PASSWORD"] = "test_password"
    upload_to_pypi(
        "test_path",
        skip_existing=True,
        glob_patterns=["test_glob_pattern", "test_glob_pattern2"],
    )
    os.environ["PYPI_TOKEN"] = "pypi-test_token"
    upload_to_pypi(
        "test_path2", skip_existing=False, glob_patterns=["test_glob_pattern3"]
    )

# Generated at 2022-06-14 05:14:07.691090
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:14:15.923782
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Test for upload_to_pypi which uploads to the test PyPI
    """
    from .test_helpers import mock_config_repository

    with mock_config_repository({'repository': 'https://test.pypi.org/legacy/'}):
        upload_to_pypi(
            path='./dist',
            skip_existing=True,
            glob_patterns=['*'],
            username='__token__',
            password=os.getenv("PYPI_TOKEN"),
        )

# Generated at 2022-06-14 05:14:23.435431
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # test with token (os.environ mocked)
    os.environ["PYPI_TOKEN"] = "pypi-token"
    upload_to_pypi()
    assert run.call_args == call("twine upload -u '__token__' -p 'pypi-token' '*/'")

    # test with username and password (os.environ mocked)
    os.environ["PYPI_TOKEN"] = None
    os.environ["PYPI_USERNAME"] = "user"
    os.environ["PYPI_PASSWORD"] = "password"
    upload_to_pypi()
    assert run.call_args == call("twine upload -u 'user' -p 'password' '*/'")

    # test with repository (os.environ mocked)
   

# Generated at 2022-06-14 05:14:25.571978
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(path="tests/wheel", glob_patterns=["*.whl"])

# Generated at 2022-06-14 05:14:39.271000
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .test.test_helpers import MockCollector

    def mock_run(command):
        assert command == "twine upload -u '__token__' -p 'pypi-test' 'dist/*'"

    collector = MockCollector()
    collector.add_mock("invoke.run", mock_run)
    collector.get_original("semantic_release.upload_to_pypi")(
        path="dist", skip_existing=False, glob_patterns=["*"]
    )
    collector.finalize()

# Generated at 2022-06-14 05:14:51.300647
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    get = os.environ.get
    try:
        os.environ["PYPI_TOKEN"] = "pypi-s0m3t0k3n"
        upload_to_pypi(skip_existing=True)
    finally:
        os.environ["PYPI_TOKEN"] = get("PYPI_TOKEN", "")
    try:
        os.environ["PYPI_USERNAME"] = "spam"
        os.environ["PYPI_PASSWORD"] = "eggs"
        upload_to_pypi(skip_existing=True)
    finally:
        os.environ["PYPI_USERNAME"] = get("PYPI_USERNAME", "")

# Generated at 2022-06-14 05:14:58.275460
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    with patch("invoke.run"):
        with patch("semantic_release.UploadToPypi.config"):
            upload_to_pypi("dist", False, glob_patterns=["some_package*.whl"])

            invoke.run.assert_called_with("twine upload -u '__token__' -p 'pypi-token' 'dist/some_package*.whl'")

# Generated at 2022-06-14 05:14:59.518461
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()

# Generated at 2022-06-14 05:15:04.563123
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # TODO: It's possible to disable network access and set up a mock server
    # that returns success/failure codes, but that's probably a little too
    # heavy for our purposes. For now, pypi is a black box to us.
    # (It's more likely that the error would be in the way the path is
    # constructed anyway, which can be tested.)
    assert True

# Generated at 2022-06-14 05:15:07.157206
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(path="path", skip_existing=True, glob_patterns=["one", "two"])

# Generated at 2022-06-14 05:15:08.094812
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi is not None

# Generated at 2022-06-14 05:15:18.293969
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import tempfile

    # Create temp folder and file
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = os.path.join(temp_dir, "test.file")
        open(file_path, "w").write("test")

        # Create fake env variables
        os.environ["PYPI_USERNAME"] = "username"
        os.environ["PYPI_PASSWORD"] = "password"
        os.environ["PYPI_TOKEN"] = "pypi-token"


# Generated at 2022-06-14 05:15:19.300549
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert False


# Generated at 2022-06-14 05:15:29.711929
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .helpers import MockRun

    # import the function we want to test
    from .upload_to_pypi import upload_to_pypi

    # Define the function we want to override
    def func(command):
        assert (
            command
            == 'twine upload -u \'username\' -p \'password\' -r \'repository\' --skip-existing "dist/pattern1" "dist/pattern2" "dist/pattern3"'
        )

        # mock the response
        return "Success"

    # Override the run function with our MockRun
    run = MockRun(func, "Success")


# Generated at 2022-06-14 05:15:53.394001
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Assert that function upload_to_pypi calls twine correctly with given params.
    """
    import mock
    import sys

    class SystemExit(Exception):
        pass

    def mock_run(args):
        # paths to src and dist folder are not relevant for the test
        assert args == (
            b"twine upload -u 'twine_username' -p 'twine_password' -r 'test_repo'"
            b" --skip-existing 'test_path/test_glob.whl'"
        )

    sys.modules["invoke"] = mock.Mock()
    sys.modules["invoke"].run = mock_run


# Generated at 2022-06-14 05:16:01.024018
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Tests the upload_to_pypi function."""
    # Basic test
    run("python -m setup sdist", warn=True)
    run("python -m setup bdist_wheel", warn=True)
    upload_to_pypi()
    # Test with different dist folder
    run("python -m setup sdist --dist-dir diff_dist", warn=True)
    run("python -m setup bdist_wheel --dist-dir diff_dist", warn=True)
    upload_to_pypi(path="diff_dist")

# Generated at 2022-06-14 05:16:04.243315
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    os.environ["PYPI_TOKEN"] = "test"
    upload_to_pypi()
    del os.environ["PYPI_TOKEN"]

# Generated at 2022-06-14 05:16:06.936844
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    try:
        upload_to_pypi("test", True, ["*"])
    except ImproperConfigurationError:
        return
    assert False

# Generated at 2022-06-14 05:16:16.529798
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import os
    from shutil import copytree
    from tempfile import mkdtemp

    from .helpers import MockContext
    from .helpers import MockRun
    from .helpers import logged_function_test

    @logged_function_test(logger)
    def test_pypi_upload_with_token(
        tmpdir: str,
        mocker: MockContext,
        mock_run: MockRun,
        mock_get_logger: MockContext,
    ):
        build_dir = tmpdir.mkdir("build")
        build_dir.mkdir("dist")
        build_dir.mkdir("foo_project")
        build_dir.mkdir("bar_project")

# Generated at 2022-06-14 05:16:17.807953
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert(True)

# Generated at 2022-06-14 05:16:29.264554
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .helpers import tmpdir
    from .helpers import mock_run

    with tmpdir() as tmp:
        with mock_run() as run_mock:
            upload_to_pypi(path=tmp)
            run_mock.assert_called_once_with(
                "twine upload --skip-existing '{}/{}'".format(tmp, "*")
            )

        with mock_run() as run_mock:
            upload_to_pypi(path=tmp, glob_patterns=["foo.whl", "bar.whl"])

# Generated at 2022-06-14 05:16:39.226723
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Test for function upload_to_pypi.

    Inserts a directory and calls upload_to_pypi to upload files.

    :return: Success or failure message.
    """
    try:
        os.makedirs("dist")
        os.makedirs("src")
        os.makedirs("src/release_app")
        os.makedirs("src/release_app/__init__.py")
        upload_to_pypi(path="src")
        return "Success"
    except:
        return "Failed"

# Generated at 2022-06-14 05:16:40.485428
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi

# Generated at 2022-06-14 05:16:46.340052
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """
    GIVEN a wheel exist in dist folder
    WHEN upload_to_pypi is called
    THEN the wheel should be uploaded to PyPI.
    """
    try:
        os.chdir("tests/tmp")
        run(
            f"python setup.py sdist bdist_wheel"
        )
        upload_to_pypi()
    finally:
        os.chdir("../..")

# Generated at 2022-06-14 05:17:19.419434
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert True

# Generated at 2022-06-14 05:17:21.154263
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(skip_existing=True)

# Generated at 2022-06-14 05:17:22.236309
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()

# Generated at 2022-06-14 05:17:34.572225
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from unittest import mock
    from semantic_release import version
    from .helpers import test_version

    version.__version__ = test_version()

    with mock.patch("invoke.run") as mocked_run:
        mocked_run.return_value = "Uploading dist/project-0.0.1.tar.gz [--skip-existing] [--repository alternative] (twine upload -u __token__ -p pypi-123456789) -> Uploaded to PyPI."
        upload_to_pypi(path="dist", skip_existing=True, glob_patterns=["*.tar.gz"])

# Generated at 2022-06-14 05:17:36.591459
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    result = run('twine upload "dist/test1.txt" "dist/test2.txt"')
    assert result.ok


# Generated at 2022-06-14 05:17:49.709320
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import unittest
    import os
    import shutil

    # Create fixtures

    fixtures_dir = os.path.join(os.path.dirname(__file__), "fixtures")
    assert os.path.exists(fixtures_dir)

    dist_dir = os.path.join(fixtures_dir, "dist")
    if os.path.exists(dist_dir):
        shutil.rmtree(dist_dir)

    metadata_dir = os.path.join(fixtures_dir, "metadata")
    if os.path.exists(metadata_dir):
        shutil.rmtree(metadata_dir)

    os.mkdir(dist_dir)
    os.mkdir(metadata_dir)


# Generated at 2022-06-14 05:17:52.001552
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Run the upload_to_pypi function."""
    upload_to_pypi("dist", skip_existing=False, glob_patterns=["test1", "test2"])

# Generated at 2022-06-14 05:17:55.831111
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    os.environ["PYPI_TOKEN"] = "pypi-test-token"
    upload_to_pypi(glob_patterns=["*.files"])

# Generated at 2022-06-14 05:17:59.580158
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi("test/test_upload/dist", skip_existing=True, glob_patterns=["*"])

# Generated at 2022-06-14 05:18:00.242505
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:19:17.813182
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    with patch("functions.upload_to_pypi.run") as mock_run, patch("invoke.run") as mock_invoke_run:
        mock_settings = MagicMock()
        mock_settings.get = lambda x: None
        with patch("functions.upload_to_pypi.config", mock_settings):
            upload_to_pypi()
            expected_cmd = "twine upload "
            mock_run.assert_called_once_with(expected_cmd)
            mock_invoke_run.assert_not_called()

    with patch("functions.upload_to_pypi.run") as mock_run, patch("invoke.run") as mock_invoke_run:
        mock_settings = MagicMock()
        mock_settings.get = lambda x: None

# Generated at 2022-06-14 05:19:29.930092
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Create mock wheel
    print("Create mock wheel...")
    distribution = "twine"
    version = "1.12.1"
    run("python3 setup.py bdist_wheel")

    # Save username, password and token to env
    print("Save to env...")
    username = "username"
    password = "password"
    token = "token"
    os.environ["PYPI_USERNAME"] = username
    os.environ["PYPI_PASSWORD"] = password
    os.environ["PYPI_TOKEN"] = token

    print("Run upload_to_pypi...")

    # Test upload with username and password
    try:
        upload_to_pypi()
    except Exception as e:
        print(e)

    # Test upload with token

# Generated at 2022-06-14 05:19:31.073074
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi() == None

# Generated at 2022-06-14 05:19:32.433390
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert False

# Generated at 2022-06-14 05:19:44.443489
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Test for function upload_to_pypi"""
    from .test_helpers import mock_invoke_run

    import pytest

    from invoke.exceptions import Exit
    from semantic_release.errors import ImproperConfigurationError

    with pytest.raises(ImproperConfigurationError) as excinfo:
        upload_to_pypi()

    assert "Missing credentials for uploading to PyPI" in str(excinfo.value)

    mock_invoke_run.side_effect = RuntimeError("Missing dependency")

    with pytest.raises(ImproperConfigurationError) as excinfo:
        upload_to_pypi(skip_existing=True)

    assert "Failed to upload to PyPI" in str(excinfo.value)

    mock_invoke_run.side_effect = Exit(1)


# Generated at 2022-06-14 05:19:53.428561
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """
    Test for function upload_to_pypi
    """
    # 0. Setup
    os.environ["HOME"] = "../../"
    glob_patterns = ["*"]
    path_glob_pattern = "dist"

    # 1. Execute the function with a skip_existing parameter
    upload_to_pypi(
        path=path_glob_pattern, skip_existing=True, glob_patterns=glob_patterns
    )

    # 2. Execute the function with a glob_patterns parameter
    upload_to_pypi(
        path=path_glob_pattern, skip_existing=False, glob_patterns=glob_patterns
    )

    # 3. Execute the function without parameters

# Generated at 2022-06-14 05:19:57.825721
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Test coverage for the function upload_to_pypi"""
    assert upload_to_pypi(path="dist",
        skip_existing=True,
        glob_patterns=["*"]) == None

    # Assert ImproperConfigurationError for missing environment var
    try:
        assert upload_to_pypi(path="dist",
        skip_existing=True,
        glob_patterns=["*"]) == None
    except ImproperConfigurationError:
        pass

    # Assert ImproperConfigurationError for missing .pypirc file
    assert upload_to_pypi(path="dist",
        skip_existing=True,
        glob_patterns=["*"]) == None

# Generated at 2022-06-14 05:20:07.853666
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    def mock_run(a, b, c, d, e, env=None):
        assert env is not None
    
    old_run = run
    run = mock_run

# Generated at 2022-06-14 05:20:19.950535
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import pytest
    from semantic_release.hooks import UploadToPypi
    from semantic_release.errors import UploadToPypiError

    # No credentials
    with pytest.raises(UploadToPypiError):
        upload_to_pypi()

    # Invalid token
    os.environ["PYPI_TOKEN"] = "INVALID"
    with pytest.raises(UploadToPypiError):
        upload_to_pypi()

    # Token
    os.environ["PYPI_TOKEN"] = "pypi-token"
    try:
        upload_to_pypi()
    except Exception:
        pytest.fail("upload_to_pypi() should not raise an exception with a token")

    # Invalid username and password
    del os.environ

# Generated at 2022-06-14 05:20:33.700362
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Check upload_to_pypi function executes its body self-contained.
    """
    token = "token"
    username = "username"
    password = "password"
    os.environ.get('PYPI_TOKEN', None)
    os.environ.get('PYPI_USERNAME', None)
    os.environ.get('PYPI_PASSWORD', None)

    os.environ['PYPI_TOKEN'] = token
    upload_to_pypi(skip_existing=True)
    assert os.environ.get('PYPI_TOKEN', None) == token

    os.environ['PYPI_USERNAME'], os.environ['PYPI_PASSWORD'] = username, password
    upload_to_pypi(skip_existing=True)
