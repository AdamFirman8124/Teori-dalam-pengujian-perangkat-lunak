

# Generated at 2022-06-14 05:12:55.676954
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .helpers import _mock_subprocess_popen, MockPopen

    mock_popen: MockPopen
    with _mock_subprocess_popen() as (popen, _, _), MockPopen(popen) as mock_popen:
        upload_to_pypi()

# Generated at 2022-06-14 05:13:01.523619
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import os, tempfile
    from os import path
    from shutil import rmtree
    from invoke import run
    
    path = tempfile.mkdtemp()
    try:
        run("pip install twine")
        os.environ['TWINE_USERNAME'] = 'testuser' 
        os.environ['TWINE_PASSWORD'] = 'testpassword' 
        os.system("touch %s" % path + '/testpackage.tar.gz')
        upload_to_pypi(path)
    finally:
        rmtree(path)

# Generated at 2022-06-14 05:13:09.846832
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import os
    import sys
    import tempfile

    if 'PYPI_TOKEN' in os.environ:
        del os.environ['PYPI_TOKEN']

    if 'PYPI_USERNAME' in os.environ:
        del os.environ['PYPI_USERNAME']

    if 'PYPI_PASSWORD' in os.environ:
        del os.environ['PYPI_PASSWORD']

    # ImproperConfigurationError
    temp_dir = tempfile.mkdtemp()
    try:
        upload_to_pypi(temp_dir)
    except:  # noqa: E722 do-not-use-bare-except
        e = sys.exc_info()[0]

# Generated at 2022-06-14 05:13:10.324188
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:13:11.373956
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()

# Generated at 2022-06-14 05:13:22.066272
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """
    Test upload of wheels to PyPI
    """
    from semantic_release import get_version

    project_name = "semantic-release-testproject"
    version = get_version("0.1.0")
    version = version[:len(version)-1]
    destination = "dist"

    # Create dists and wheels
    run("python setup.py sdist bdist_wheel")
    path_to_dist = "dist/"+project_name+"-"+version

    glob_patterns = [project_name+"-"+version+".tar.gz"]
    upload_to_pypi(
        path=destination, skip_existing=False, glob_patterns=glob_patterns
    )

    # Check to see if the files were created

# Generated at 2022-06-14 05:13:31.355552
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Test the upload_to_pypi function."""

    # Test API Token credentials
    os.environ["PYPI_TOKEN"] = "pypi-xxx"

    # Test Username/Password credentials
    os.environ["PYPI_USERNAME"] = "XXX"
    os.environ["PYPI_PASSWORD"] = "xxx"

    upload_to_pypi("dist", False, ["*"])

# Generated at 2022-06-14 05:13:33.215029
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi != None, "Failed to check upload_to_pypi"

# Generated at 2022-06-14 05:13:46.544693
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import os
    import tempfile
    from pathlib import Path
    from unittest.mock import patch
    from unittest import mock
    from .helpers import LoggedFunction
    from .helpers import unittest_mock_method
    from .helpers import LoggingTestCase
    import semantic_release.hvcs
    import semantic_release.settings

    with tempfile.TemporaryDirectory() as temp_dir:
        temp_dir_path = Path(temp_dir).resolve()
        Path(temp_dir_path / "dist/package.whl").touch()

        repository = "pypi"


# Generated at 2022-06-14 05:13:50.169239
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    def mock_run(c, **kwargs):
        assert kwargs.get("echo")
        assert c == "twine upload -u 'username' -p 'password'  dist/*"

    upload_to_pypi(path="dist", glob_patterns=["*"], mock_run=mock_run)

# Generated at 2022-06-14 05:14:17.943208
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Test for function upload_to_pypi in pypi_upload module.
    """
    from unittest.mock import patch

    def mock_run(*args, **kwargs):
        """Mock for run func.
        """
        pass

    with patch("semantic_release.upload_to_pypi.run", side_effect=mock_run):
        upload_to_pypi()

    with patch("semantic_release.upload_to_pypi.run", side_effect=mock_run):
        with patch.dict("os.environ", {"PYPI_TOKEN": "pypi-token"}):
            upload_to_pypi()


# Generated at 2022-06-14 05:14:21.937581
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    with mock.patch("os.environ.get", return_value="twineuploadtest"):
        with mock.patch("invoke.run") as m_run:
            m_run.return_value.return_code = 0
            upload_to_pypi(
                path="path", skip_existing=True, glob_patterns=["*.whl", "*.tar.gz"]
            )



# Generated at 2022-06-14 05:14:23.197961
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Dummy for unit testing.
    """

# Generated at 2022-06-14 05:14:34.759483
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Test for no credentials
    try:
        upload_to_pypi("dist")
    except ImproperConfigurationError:
        pass
    else:
        raise AssertionError("Should have failed with no credentials")

    # Test for empty credentials
    try:
        upload_to_pypi("dist", username="", password="")
    except ImproperConfigurationError:
        pass
    else:
        raise AssertionError("Should have failed with empty credentials")

    # Test for invalid token
    try:
        upload_to_pypi("dist", token="test")
    except ImproperConfigurationError:
        pass
    else:
        raise AssertionError("Should have failed with invalid token")

    # Test for missing repository

# Generated at 2022-06-14 05:14:36.250297
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi("dist", True, ["*"])

# Generated at 2022-06-14 05:14:42.965668
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(path="dist")
    upload_to_pypi(path="dist", glob_patterns=["*"])
    upload_to_pypi(path="dist", skip_existing=True)
    upload_to_pypi(path="dist", skip_existing=True, glob_patterns=["*"])

# Generated at 2022-06-14 05:14:45.161998
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(path="dist", glob_patterns=["*.whl"])

# Generated at 2022-06-14 05:14:47.246283
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(path = "dist", skip_existing = False, glob_patterns = None)

# Generated at 2022-06-14 05:14:57.704712
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import subprocess
    import sys
    import os
    import requests
    import json

    username = os.environ.get("PYPI_USERNAME", "test123")
    password = os.environ.get("PYPI_PASSWORD", "test123")
    pip_username = os.environ.get("PIP_USERNAME", "test123")
    pip_password = os.environ.get("PIP_PASSWORD", "test123")

    # Get the latest version for simple
    package_url = "https://pypi.org/pypi/simple/json"
    r = requests.get(package_url)
    data = json.loads(r.text)
    latest_version = data['info']['version']

    # Create a new version

# Generated at 2022-06-14 05:15:03.448117
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """ Unit test to test the upload_to_pypi function """
    run("echo test > text.txt")
    run("zip test.zip text.txt")
    upload_to_pypi(path=".", glob_patterns=["test.zip"])
    run("rm text.txt")
    run("rm test.zip")

# Generated at 2022-06-14 05:15:24.051951
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """
    Here we test if the upload_to_pypi function,
    will pass the right flags with right credentials.
    """
    command = ""

    # Test all the cases where we do not have a repository
    config["repository"] = None
    os.environ["PYPI_TOKEN"] = ""
    upload_to_pypi(path="test")
    command_test_1 = command
    command = ""
    upload_to_pypi(path="test", skip_existing=True)
    command_test_2 = command
    command = ""
    upload_to_pypi(path="test", skip_existing=True, glob_patterns=["*"])
    command_test_3 = command
    command = ""

# Generated at 2022-06-14 05:15:25.206689
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi != None

# Generated at 2022-06-14 05:15:37.856811
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """
    Function to test that the upload_to_pypi function can be invoked without errs
    """

    token = 'pypi-123fake'
    username = '__token__'
    password = token
    dist = 'dist'

    repo_arg = f"-r '{config.get('repository', None)}'"

    username_password = (
        f"-u '{username}' -p '{password}'" if username and password else ""
    )

    dist = ""

    os.environ["TWINE_USERNAME"] = username
    os.environ["TWINE_PASSWORD"] = password

    run(f"twine upload {username_password}{repo_arg}{skip_existing_param} {dist}")

    del os.environ["TWINE_USERNAME"]
    del os.en

# Generated at 2022-06-14 05:15:38.303853
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:15:44.749982
# Unit test for function upload_to_pypi
def test_upload_to_pypi():

    def dummy_run(command):
        assert command == """twine upload -u '__token__' -p 'pypi-test_token' --skip-existing "dist/file-name-0.0.0-py2.py3-none-any.whl"""
        return 0

    os.environ["PYPI_TOKEN"] = "pypi-test_token"
    os.environ["HOME"] = "~"

    path = "dist"
    glob_patterns = ["file-name-0.0.0-py2.py3-none-any.whl"]

    old_run = run
    run = dummy_run
    upload_to_pypi(path, True, glob_patterns)
    run = old_run

    # Clean up test environment

# Generated at 2022-06-14 05:15:45.991375
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()

# Generated at 2022-06-14 05:15:57.524651
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    def test_for_missing_credentials():
        upload_to_pypi()
        assert result == 0

    # Missing credentials should raise an exception
    with pytest.raises(ImproperConfigurationError, match="upload to PyPI"):
        test_for_missing_credentials()

    os.environ["PYPI_USERNAME"] = ""
    os.environ["PYPI_PASSWORD"] = ""
    # Missing credentials should raise an exception
    with pytest.raises(ImproperConfigurationError, match="upload to PyPI"):
        test_for_missing_credentials()

    # Add a token
    os.environ["PYPI_TOKEN"] = "pypi-test-token"

    result = upload_to_pypi()
    assert result.ok

    # TOD

# Generated at 2022-06-14 05:15:58.308709
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:16:00.415095
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi.__name__ == "upload_to_pypi"

# Generated at 2022-06-14 05:16:01.511327
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:16:29.747350
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Test that upload_to_pypi uploads files and passes arguments correctly."""
    from invoke import Context
    from unittest.mock import patch
    from .helpers import LoggedFunction
    from semantic_release.functions.plugin_functions import get_plugin_function
    import semantic_release.settings as _settings
    import sys

    _settings.set_settings_location(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "fixtures")
    )

    pypi_username = "foo"
    pypi_password = "bar"
    pypi_repository = "baz"

    mock_run_context = Context()
    mock_run_context.config.run.echo = False

# Generated at 2022-06-14 05:16:37.794966
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    def mock_run(command: str, **kwargs: object) -> None:
        assert command == "twine upload -u '__token__' -p 'pypi-token' -r 'pypi' --skip-existing 'dist/*'"

    upload_to_pypi(
        path="dist", skip_existing=True, glob_patterns=["*"], run=mock_run
    )

# Generated at 2022-06-14 05:16:47.573469
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import subprocess
    import tempfile
    import shutil

    tmp_dir = tempfile.mkdtemp()
    try:
        os.chdir(tmp_dir)

        subprocess.call("echo hello > test.txt", shell=True)
        os.makedirs("subdir")
        subprocess.call("echo hello > subdir/test.txt", shell=True)

        upload_to_pypi(path=tmp_dir, glob_patterns=["*_wit.xlsx"])
        upload_to_pypi(path=tmp_dir, glob_patterns=["subdir/*_wit.xlsx"])

    finally:
        os.chdir("/")
        shutil.rmtree(tmp_dir)



# Generated at 2022-06-14 05:17:00.827783
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Test upload_to_pypi()"""
    import os
    import shutil
    import tempfile
    import subprocess
    import unittest
    import pytest
    from shlex import split
    from unittest import mock
    from semantic_release import version_utils

    from .helpers import LoggedFunction

    def create_file_structure():
        """Create a temporary file structure"""
        os.makedirs(os.path.join(temp_path, "dist"), exist_ok=True)
        os.makedirs(os.path.join(temp_path, "a", "b", "c"), exist_ok=True)

# Generated at 2022-06-14 05:17:02.095426
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:17:02.634048
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert True

# Generated at 2022-06-14 05:17:13.785183
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    def mock_run(command):
        return command
    run = mock_run
    assert upload_to_pypi(path="path") == "twine upload -u '__token__' -p 'pypi-token' '\"path/\"'"
    assert upload_to_pypi(path="path", repository="pypi") == "twine upload -u '__token__' -p 'pypi-token' -r 'pypi' '\"path/\"'"
    assert upload_to_pypi(path="path", skip_existing=True) == "twine upload -u '__token__' -p 'pypi-token'  --skip-existing '\"path/\"'"

# Generated at 2022-06-14 05:17:23.425784
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import tempfile
    import shutil
    try:
        os.environ['PYPI_USERNAME'] = 'TEST'
        os.environ['PYPI_PASSWORD'] = 'TEST'
        temp_dist = tempfile.mkdtemp()
        run = upload_to_pypi(temp_dist)
        expected = "twine upload -u 'TEST' -p 'TEST' '' --skip-existing '\"{}/{}\"'".format(temp_dist, "*")
        assert run.command == expected
    finally:
        if temp_dist:
            shutil.rmtree(temp_dist)

# Generated at 2022-06-14 05:17:33.782651
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import pathlib
    import shutil
    import tempfile

    temp_dir = tempfile.mkdtemp()
    old_cwd = os.getcwd()
    os.chdir(temp_dir)
    shutil.copyfile(str(pathlib.Path(__file__).parent.joinpath("example.whl")),
        f"{temp_dir}/example-1.0.0-py3-none-any.whl")
    os.environ['PYPI_TOKEN'] = 'pypi-123'
    upload_to_pypi()
    os.chdir(old_cwd)

# Generated at 2022-06-14 05:17:34.854479
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()

# Generated at 2022-06-14 05:18:12.497803
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(path='dist', skip_existing=True, glob_patterns=["lorem", "ipsum"])

# Generated at 2022-06-14 05:18:16.319527
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Ensure the function is callable
    upload_to_pypi()

    # Ensure correct parameters are set
    upload_to_pypi(
        path="dist", skip_existing=False, glob_patterns=["*"]
    )

# Generated at 2022-06-14 05:18:26.091540
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import os
    import pytest
    from tempfile import TemporaryDirectory

    # Create a temporary directory and file for testing
    tempdir = TemporaryDirectory()
    files = [
        os.path.join(tempdir.name, "filename1.txt"),
        os.path.join(tempdir.name, "filename2.txt"),
    ]
    for file in files:
        with open(file, "w") as f:
            f.write("Some content")

    # Check that files are uploaded when both username and password are given
    os.environ["PYPI_USERNAME"] = "username"
    os.environ["PYPI_PASSWORD"] = "password"
    upload_to_pypi(path=tempdir.name, glob_patterns=["*"])

    # Check that files are uploaded when neither username

# Generated at 2022-06-14 05:18:38.005032
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Uploading to PyPI
    with open(".pypirc", "w") as file:
        file.write("[distutils]\nindex-servers=pypi\n\n[pypi]\nusername=bob\npassword=hunter2")
    upload_to_pypi(skip_existing=True, glob_patterns=["*", "!*.whl"])  # Should not raise error
    os.remove(".pypirc")

    # Uploading to a different repository
    upload_to_pypi(repository="test")  # Should not raise error

    # Uploading using a PyPI token
    os.environ["PYPI_TOKEN"] = "pypi-some_api_key_that_is_not_saved_here"
    upload_to_pyp

# Generated at 2022-06-14 05:18:51.654654
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .helpers import LoggedFunctionTest

    def mocked_run(command):
        output = command.split()

        if output[1] == "upload":
            return True
        else:
            return False


# Generated at 2022-06-14 05:19:04.804592
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # If the token is missing, an exception is raise
    os.environ.pop("PYPI_TOKEN", None)
    os.environ.pop("PYPI_USERNAME", None)
    os.environ.pop("PYPI_PASSWORD", None)
    os.environ.pop("HOME", None)
    try:
        upload_to_pypi("/tmp", True, ["*"])
        assert False
    except ImproperConfigurationError:
        assert True
    # If the token is not prefixed with "pypi-", an exception is raise
    os.environ["PYPI_TOKEN"] = "123"
    try:
        upload_to_pypi("/tmp", True, ["*"])
        assert False
    except ImproperConfigurationError:
        assert True
   

# Generated at 2022-06-14 05:19:08.835499
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Given
    dist_path = "./test_dist"
    glob_pattern = "*.whl"

    # When
    upload_to_pypi(dist_path, True, [glob_pattern])

# Generated at 2022-06-14 05:19:16.338920
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    def mock_run(command):
        assert "twine upload" in command

    patch("invoke.run", mock_run).start()
    os.environ["PYPI_USERNAME"] = "username"
    os.environ["PYPI_PASSWORD"] = "password"
    upload_to_pypi("dist", skip_existing=True, glob_patterns=["*"])
    del os.environ["PYPI_USERNAME"]
    del os.environ["PYPI_PASSWORD"]
    upload_to_pypi("dist", skip_existing=True, glob_patterns=["*"])

# Generated at 2022-06-14 05:19:28.964738
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    username = "unit_test_user"
    password = "unit_test_password"
    token = "pypi-unit_test_token"
    repository = "test"
    glob_patterns = ["*"]
    path = "dist"
    skip_existing = True
    dist = " ".join(
        ['"{}/{}"'.format(path, glob_pattern.strip()) for glob_pattern in glob_patterns]
    )
    repository_arg = f" -r '{repository}'" if repository else ""
    username_password = (
        f"-u '{username}' -p '{password}'" if username and password else ""
    )
    skip_existing_param = " --skip-existing" if skip_existing else ""


# Generated at 2022-06-14 05:19:41.651306
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Successful upload of wheels
    assert not os.environ.get("PYPI_TOKEN")
    assert not os.environ.get("PYPI_USERNAME")
    assert not os.environ.get("PYPI_PASSWORD")
    assert upload_to_pypi(glob_patterns=["*"])

    # Successful upload of wheels
    os.environ["PYPI_TOKEN"] = "pypi-l2j2llad8j1"
    assert upload_to_pypi(glob_patterns=["*"])

    # Successful upload of wheels
    os.environ["PYPI_USERNAME"] = "user"
    os.environ["PYPI_PASSWORD"] = "password"

# Generated at 2022-06-14 05:20:52.210589
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi()

# Generated at 2022-06-14 05:21:05.726583
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import tempfile
    import textwrap
    import semantic_release

    with tempfile.TemporaryDirectory() as tmpdirname:
        with tempfile.NamedTemporaryFile(dir=tmpdirname, suffix=".whl") as zip_file:
            try:
                upload_to_pypi(zip_file.name)
            except SystemExit as e:
                assert e.code == 2
                assert e.args[0] == "Missing credentials for uploading to PyPI"

        with tempfile.NamedTemporaryFile(dir=tmpdirname, suffix=".whl") as zip_file:
            try:
                os.environ["PYPI_TOKEN"] = "test_token"
                upload_to_pypi(zip_file.name)
            except SystemExit as e:
                assert e.code == 1

# Generated at 2022-06-14 05:21:09.631041
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    path = "dist"
    skip_existing = False
    glob_patterns = ["*.whl"]
    upload_to_pypi(path, skip_existing, glob_patterns)

# Generated at 2022-06-14 05:21:13.728494
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(
        path="dist",
        skip_existing=False,
        glob_patterns=["*"],
    )

# Generated at 2022-06-14 05:21:18.954403
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    os.environ["PYPI_TOKEN"] = "pypi-1234"
    glob_patterns = ["*package1*", "*package2*"]
    upload_to_pypi(path = "dist", skip_existing = True, glob_patterns = glob_patterns)

# Generated at 2022-06-14 05:21:22.221684
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(path="dist", skip_existing=True, glob_patterns=["*"])

# Generated at 2022-06-14 05:21:22.927562
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert True

# Generated at 2022-06-14 05:21:32.531430
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    test_path = "dist"
    test_skip_existing = True
    test_glob_patterns = None
    test_repository = "test"
    test_token = "pypi-test"
    test_username = "test"
    test_password = "test"
    # Unit test upload_to_pypi with token
    config.set("repository", None)
    os.environ["PYPI_TOKEN"] = test_token
    with LoggedFunction(logger) as logger_mock:
        upload_to_pypi(test_path, test_skip_existing, test_glob_patterns)
        logger_mock.assert_any_call(
            "Sending files from dist to PyPI with Twine."
        )
        logger_mock.assert_any_

# Generated at 2022-06-14 05:21:37.466227
# Unit test for function upload_to_pypi
def test_upload_to_pypi():

    import io
    import json
    import unittest
    import unittest.mock
    
    from semantic_release import invoke

    from .helpers import LoggedFunction

    class TestUploadToPypi(unittest.TestCase):

        def setUp(self):
            self.cwd = os.getcwd()
            os.chdir(os.path.dirname(__file__))

        def tearDown(self):
            os.chdir(self.cwd)

        def invoke(self, string):
            # make sure we run the function in the same folder
            return invoke.run(
                string, echo=True, pty=False, warn=True, hide=False, encoding="utf-8"
            )


# Generated at 2022-06-14 05:21:47.424695
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .helpers import LoggedFunction, RunningInContainer

    def _setup_container():
        from semantic_release.settings import config
        from tqdm.auto import tqdm
        from invoke import run
        import docker

        image_tag = f"semantic-release-test:{config['current_version']}"
        client = docker.from_env()
        with tqdm(
            desc=f"Building CI/CD test container",
            total=1,
            unit="containers",
            leave=False,
        ) as pbar:
            try:
                client.images.pull(image_tag)
            except Exception:
                pass
            run(
                f"docker build -t {image_tag} "
                + "-f .semantic-release/test/Dockerfile-pypi-test ."
            )
