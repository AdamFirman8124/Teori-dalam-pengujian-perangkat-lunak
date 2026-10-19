

# Generated at 2022-06-14 05:12:56.070128
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Example of how to test the upload_to_pypi function using pytest."""
    import pytest
    from semantic_release.errors import UnknownCommandError

    try:
        upload_to_pypi()
    except ImproperConfigurationError as e:
        assert "Missing credentials for uploading to PyPI" in str(e)
    except UnknownCommandError as e:
        assert "twine" in str(e)
    else:
        pytest.fail()

# Generated at 2022-06-14 05:13:06.712826
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .helpers import mock_subprocess

    with mock_subprocess(None) as run_function:

        # Default config
        upload_to_pypi()
        run_function.assert_called_once_with(
            "twine upload -u '__token__' -p 'pypi-fake-token' '' --skip-existing 'dist/*'"
        )
        run_function.reset_mock()

        # Custom path
        upload_to_pypi(path="my/custom/path")
        run_function.assert_called_once_with(
            "twine upload -u '__token__' -p 'pypi-fake-token' '' --skip-existing 'my/custom/path/*'"
        )
        run_function.reset_mock()

        # Custom path, custom repository
       

# Generated at 2022-06-14 05:13:09.222177
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi("dist", True, ["*"])
    return True

# Generated at 2022-06-14 05:13:20.175522
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Test with token
    os.environ["PYPI_TOKEN"] = "pypi-abcdefghijklmnopqrstuvwxyz"
    upload_to_pypi(path="tests", glob_patterns=["*"])

    # Test with username and password
    os.environ["PYPI_USERNAME"] = "username"
    os.environ["PYPI_PASSWORD"] = "password"
    upload_to_pypi(path="tests", glob_patterns=["*"])

    # Test with unknown credentials
    os.environ["PYPI_TOKEN"] = ""
    os.environ["PYPI_USERNAME"] = ""

# Generated at 2022-06-14 05:13:29.964195
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from unittest.mock import patch

    with patch(
        "semantic_release.hvcs.pypi.helpers.run", autospec=True,
    ) as mocked_run:
        upload_to_pypi(
            path="twine_uploads", skip_existing=True,
        )
        mocked_run.assert_called_once_with(
            "twine upload  --skip-existing 'twine_uploads/*'"
        )

        mocked_run.reset_mock()
        upload_to_pypi(path="wheel_folder")
        mocked_run.assert_called_once_with("twine upload  'wheel_folder/*'")

        mocked_run.reset_mock()
        upload_to_pypi(skip_existing=True)
        mocked_run.assert_

# Generated at 2022-06-14 05:13:30.825460
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:13:34.772524
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """upload_to_pypi dummy test.

    No assertions since it's hard to check if this function can generate
    a successful twine request, and we don't want to impose the hardcoding
    of credentials.
    """
    upload_to_pypi()

# Generated at 2022-06-14 05:13:38.311273
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(path = "dist", skip_existing = False, glob_patterns = None)

# Generated at 2022-06-14 05:13:49.610631
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import shutil
    from semantic_release.plugins.pypi import upload_to_pypi

    try:
        import twine  # noqa: F401
    except ImportError:
        return


# Generated at 2022-06-14 05:14:00.131020
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    path = "dist"
    glob_patterns = ["*"]
    skip_existing = False
    repository = None
    token = "pypi-szpyxbfxyaigwuyhqmjemslydzmaynnf"
    
    # set environment variables
    os.environ["PYPI_TOKEN"] = token
    
    # function call
    upload_to_pypi(path = path, skip_existing = skip_existing, glob_patterns = glob_patterns)
    
    # remove environment variables
    os.environ.pop("PYPI_TOKEN")

# Generated at 2022-06-14 05:14:08.561839
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(path="mydist", glob_patterns=["file1", "file2"])
    upload_to_pypi(
        path="mydist",
        skip_existing=True,
        glob_patterns=["file1", "file2"],
        repository="test",
    )

# Generated at 2022-06-14 05:14:12.117779
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Set up variables
    skip_existing = True
    glob_patterns = ["dist/*"]
    path = os.path.dirname(__file__)
    
    # Run the upload_to_pypi function
    upload_to_pypi(path, skip_existing, glob_patterns)

# Generated at 2022-06-14 05:14:13.335343
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()

# Generated at 2022-06-14 05:14:21.775305
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # The following dictionary can be updated as required for testing purposes
    test_case_1 = {
        "path": "dist",
        "skip_existing": False,
        "glob_patterns": ["*"],
        "expected": "twine upload  *",
    }

    parameters = ["path", "skip_existing", "glob_patterns"]
    # The follow test_cases dictionary can be updated as required for testing purposes.
    test_cases = [test_case_1]
    for test_case in test_cases:
        result = upload_to_pypi(**test_case)
        assert result == test_case["expected"]


if __name__ == "__main__":
    test_upload_to_pypi()

# Generated at 2022-06-14 05:14:31.951535
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    repo = "test-repo"
    glob_patterns = ["dist/file1", "dist/file2"]

    default_config = config.copy()
    default_config["repository"] = "test-repo"
    config.update(default_config)

    with patch('builtins.input', MagicMock(return_value='yes')), patch('invoke.run', MagicMock()) as mock:
        upload_to_pypi(glob_patterns=glob_patterns)
        assert mock.call_args_list[0][0][0] == 'twine upload  "dist/file1" "dist/file2"'
    config.update(default_config)

# Generated at 2022-06-14 05:14:34.198547
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Unit test for function upload_to_pypi"""
    upload_to_pypi("dist")


# Generated at 2022-06-14 05:14:35.760496
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(path = "dist", skip_existing = False, glob_patterns = ["*"])

# Generated at 2022-06-14 05:14:42.850792
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(path="path/to/repo")
    upload_to_pypi(path="path/to/repo", skip_existing=True)
    upload_to_pypi(
        path="path/to/repo",
        skip_existing=True,
        glob_patterns=["package1", "package2"],
    )

# Generated at 2022-06-14 05:14:53.314756
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    def setup_patch(monkeypatch):
        monkeypatch.setenv("PYPI_USERNAME", "unittest_username")
        monkeypatch.setenv("PYPI_PASSWORD", "unittest_password")

    def test_username_password_combination_works(capsys, monkeypatch):
        setup_patch(monkeypatch)
        upload_to_pypi(glob_patterns=["*.whl"])
        captured = capsys.readouterr()
        assert (
            captured.out
            == "\nUploading files to PyPI with Twine.\n"
            "        twine upload -u 'unittest_username' -p 'unittest_password'  "
            "'dist/*.whl'\n"
        )


# Generated at 2022-06-14 05:15:01.445184
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    with patch("twine.run") as mock_run:
        upload_to_pypi(path="path")
        mock_run.assert_called_once_with("twine upload --skip-existing 'path/*'")

    with patch("twine.run") as mock_run:
        upload_to_pypi(path="path", glob_patterns=["foo", "bar/*"])
        mock_run.assert_called_once_with("twine upload --skip-existing 'path/foo' 'path/bar/*'")


# Generated at 2022-06-14 05:15:20.668577
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    username = "pypi-username"
    password = "pypi-password"
    token = "pypi-token"
    repo = "test_repo"
    glob_patterns = ["glob-pattern-1", "glob-pattern-2"]
    dist_path = "./dist/"
    skip_existing = True
    expected_dist = '"{}/{}" "{}/{}"'.format(
        dist_path, glob_patterns[0], dist_path, glob_patterns[1]
    )
    command = (
        "twine upload -u '{username}' -p '{password}' -r '{repo}' --skip-existing {dist}"
    )

    os.environ["PYPI_USERNAME"] = username

# Generated at 2022-06-14 05:15:30.962155
# Unit test for function upload_to_pypi
def test_upload_to_pypi():

    def return_false(*args, **kwargs):
        return False

    class stubbed_run:
        def __call__(self, *args, **kwargs):
            pass

    original_run = run
    run = stubbed_run()

    os.environ["HOME"] = ""
    # Test missing .pypirc file with no credentials
    try:
        upload_to_pypi()
        assert False
    except ImproperConfigurationError:
        assert True

    os.environ["HOME"] = "fake_home"
    # patch isfile to return True
    os.path.isfile = return_false
    # Test missing .pypirc file with no credentials
    try:
        upload_to_pypi()
        assert False
    except ImproperConfigurationError:
        assert True


# Generated at 2022-06-14 05:15:33.110706
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(path="dist", skip_existing=True, glob_patterns=["*.whl"])

# Generated at 2022-06-14 05:15:34.363816
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi is not None

# Generated at 2022-06-14 05:15:41.880026
# Unit test for function upload_to_pypi
def test_upload_to_pypi():

    def mock_run(command):
        return command

    class MockedConfig:
        @staticmethod
        def get(key, default=None):
            return default

    global_config = config
    global_run = run


# Generated at 2022-06-14 05:15:53.841776
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from . import (
        pypi_username,
        pypi_password,
        pypi_token,
        upload_to_pypi,
        get_pypi_config_import_error,
        get_pypi_config_login_error,
    )

    with upload_to_pypi.mock(), pypi_username.mock(None), pypi_password.mock(None), pypi_token.mock(None):
        exc = get_pypi_config_import_error()
        assert str(exc) == "Missing credentials for uploading to PyPI"
        assert issubclass(exc.__class__, ImproperConfigurationError)


# Generated at 2022-06-14 05:16:03.815481
# Unit test for function upload_to_pypi
def test_upload_to_pypi():

    """
    Verify that the upload_to_pypi function returns correct value for
    correct arguments and raises ImproperConfigurationError for invalid arguments.
    """

    assert upload_to_pypi("dist")

    token = "pypi-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

    assert upload_to_pypi("dist", skip_existing=True)

    assert upload_to_pypi("dist", glob_patterns=["*"])

    assert upload_to_pypi("dist", token=token)

    assert upload_to_pypi("dist", username="user", password="password")

    try:
        upload_to_pypi("dist", token=1)

    except ImproperConfigurationError:
        assert True


# Generated at 2022-06-14 05:16:11.049316
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pypi_token = "pypi-my-token"
    pypi_username = "username"
    pypi_password = "password"

    pypi_repository = "testpypi"

    logger.info("Missing credentials")
    os.environ["HOME"] = "/home/user"
    try:
        upload_to_pypi()
    except:
        pass
    else:
        assert False, "Missing credentials should raise ImproperConfigurationError"

    logger.info("No env variable, but .pypirc exists")
    # Write .pypirc
    with open(os.path.join(os.environ["HOME"], ".pypirc"), "w") as file:
        file.write("[pypi]\n")

# Generated at 2022-06-14 05:16:17.562003
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """
    Tests upload_to_pypi with a mock repository url, username, and password.
    """
    try:
        repository_url = "test_repository"
        username = "test_user"
        password = "test_password"
        upload_to_pypi(path="dist", skip_existing=False, glob_patterns=["*"])
        assert False
    except ImproperConfigurationError:
        assert True
    else:
        assert False

    os.environ["PYPI_USERNAME"] = username
    os.environ["PYPI_PASSWORD"] = password

    upload_to_pypi(path="dist", skip_existing=False, glob_patterns=["*"])

# Generated at 2022-06-14 05:16:29.162917
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Set up pytest environment - we need the function under test and the glob module
    import sys
    import pathlib
    my_path = pathlib.Path(__file__).parent.absolute()
    sys.path.insert(0, str(my_path))
    import glob
    # Import the function under test
    from helpers.upload_to_pypi import upload_to_pypi

    # Files to upload
    test_files = [
        'this_is_a_test_file.txt',
        'this_is_also_a_test_file.txt',
        'this_is_another_test_file.txt',
    ]

    # Create the test files

# Generated at 2022-06-14 05:16:47.831354
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi("/path/to/dist", True)
    upload_to_pypi("/path/to/dist", True, ["foo", "bar"])

# Generated at 2022-06-14 05:16:54.126392
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Create a fake dist folder
    run("mkdir dist")
    f = open("dist/test_file", "w+")
    f.close()

    # Upload to PYPI
    upload_to_pypi()
    run("rm -r dist")

# Generated at 2022-06-14 05:17:04.540182
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    path = "dist"
    with patch('invoke.run') as mock_run:
        upload_to_pypi()
        mock_run.assert_called_once_with(
            'twine upload * -u \'\' -p \'\' "dist/*"', hide=True, warn=True)
    with patch('invoke.run') as mock_run:
        upload_to_pypi(path, skip_existing=True)
        mock_run.assert_called_once_with(
            'twine upload * -u \'\' -p \'\' --skip-existing "dist/*"', hide=True, warn=True)
    glob_patterns = ["*", "*.tar.gz"]

# Generated at 2022-06-14 05:17:05.204866
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:17:12.075734
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    os.environ["PYPI_TOKEN"] = "pypi-token"
    os.environ["PYPI_USERNAME"] = "pypi-username"
    os.environ["PYPI_PASSWORD"] = "pypi-password"
    os.environ["HOME"] = "~"

    config["repository"] = "repository"

    upload_to_pypi()
    upload_to_pypi(skip_existing=True)
    upload_to_pypi(glob_patterns=["*"])



# Generated at 2022-06-14 05:17:12.964724
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi() == None

# Generated at 2022-06-14 05:17:14.401731
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi("dist", False)

# Generated at 2022-06-14 05:17:17.426703
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    run(f"twine upload {username_password}{repository_arg}{skip_existing_param} {dist}")

# Generated at 2022-06-14 05:17:20.497228
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(glob_patterns=["*.whl"])

# Generated at 2022-06-14 05:17:21.215423
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass # TODO

# Generated at 2022-06-14 05:17:54.993696
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert not upload_to_pypi()

# Generated at 2022-06-14 05:18:07.469928
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from unittest.mock import patch

    from semantic_release import get_version
    from .helpers import get_version_from_logs

    with patch("invoke.run") as invoke_run:
        upload_to_pypi("sample/dist", False)
        c = invoke_run.call_args_list[0][0][0]
        assert "twine upload" in c
        assert '"sample/dist/*"' in c

    with patch("invoke.run") as invoke_run:
        upload_to_pypi("sample/dist", False, ["*", "*"])
        c = invoke_run.call_args_list[0][0][0]
        assert "twine upload" in c
        assert '"sample/dist/*"' in c


# Generated at 2022-06-14 05:18:08.138214
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
  assert True

# Generated at 2022-06-14 05:18:11.199453
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(path="path", skip_existing=False, glob_patterns=[""])

# Generated at 2022-06-14 05:18:21.611693
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import pytest
    from semantic_release.settings import config

    with pytest.raises(ImproperConfigurationError) as err:
        upload_to_pypi()
    assert "Missing credentials" in str(err.value)

    os.environ['PYPI_TOKEN'] = 'pypi-test'
    config['repository'] = 'test'
    upload_to_pypi()
    assert "twine upload -u '__token__' -p 'pypi-test' -r 'test'" in LoggedFunction.printed_text
    del os.environ['PYPI_TOKEN']

    os.environ['PYPI_USERNAME'] = 'username'
    os.environ['PYPI_PASSWORD'] = 'password'
    upload_to_pypi()

# Generated at 2022-06-14 05:18:25.348234
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(
        path="dist",
        repository="pypi",
        skip_existing=False,
        glob_patterns=["dist/*.whl"],
    )

# Generated at 2022-06-14 05:18:37.845583
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """
    Test the upload_to_pypi function by mocking the Invoke's run function.
    This method checks if the function upload_to_pypi runs correctly.
    :return: bool
    """

    def _run(command, dry_run=False):
        """
        Mock for invoke's run method.
        :param command:
        :param dry_run:
        :return: bool
        """
        return command


    from semantic_release.hvcs import upload
    import os
    import shutil
    if os.path.exists('dist'):
        shutil.rmtree('dist')
    os.makedirs('dist')

    with open('dist/dummy.whl', 'w') as f:
        f.write('')
    glob_pattern = "*"
    glob_

# Generated at 2022-06-14 05:18:48.108508
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """
    Test if upload is done using twine and if arguments are passed correctly
    """
    result = upload_to_pypi(path='dist', skip_existing=True, glob_patterns=['*.whl', '*.tar.gz'])
    assert result == invoke.run.assert_called_with(
        f"twine upload -u '__token__' -p 'pypi-token' --skip-existing "
        f'"dist/{glob_patterns[0].strip()}" "dist/{glob_patterns[1].strip()}"'
    )

# Generated at 2022-06-14 05:18:57.729157
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    username = "test_username"
    password = "test_password"
    token = "test_token"

    # Check an ImproperConfigurationError is raised when no token or username+password are provided
    os.environ["HOME"] = ""
    try:
        upload_to_pypi()
        assert False
    except ImproperConfigurationError:
        pass

    # Check an ImproperConfigurationError is raised when no token or username+password are provided
    del os.environ["HOME"]
    try:
        upload_to_pypi()
        assert False
    except ImproperConfigurationError:
        pass

    # Check an ImproperConfigurationError is raised when token does not begin with pypi-
    os.environ["PYPI_TOKEN"] = "test_token"

# Generated at 2022-06-14 05:19:11.414407
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    def mockerun(command):
        if command.startswith("twine1 upload"):
            return "1"
        elif command.startswith("twine2 upload"):
            return "2"
        elif command.startswith("twine3 upload"):
            return "3"
        elif command.startswith("twine4 upload"):
            return "4"
        elif command.startswith("twine5 upload"):
            return "5"
        else:
            return ""

    upload_to_pypi(path="path", skip_existing=True, glob_patterns=["*"])
    assert run.call_count == 1
    assert run.call_args.kwargs["command"] == "twine -v upload --skip-existing 'path/*'"

    upload_to_

# Generated at 2022-06-14 05:20:23.436429
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Testing the upload_to_pypi function by mocking the run function.
    """
    def run_wrapper(cmd):
        """Wraps the function to allow testing of the command.
        """
        assert cmd == expected_cmd

    global run
    global os
    run_backup = run
    os_backup = os
    run = run_wrapper
    os = MagicMock()
    os.environ.get.side_effect = ("pypi-aSdA6d", None, None)
    expected_cmd = "twine upload -u '__token__' -p 'pypi-aSdA6d' 'dist/test*'"
    upload_to_pypi(
        "dist", False, ["test*"]
    )

# Generated at 2022-06-14 05:20:27.323920
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    path = os.environ.get("TEST_PATH", "")
    print(config)
    return upload_to_pypi(path, glob_patterns=["*.tar.gz"])

# Generated at 2022-06-14 05:20:39.449531
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Unit test for function upload_to_pypi
    """
    import shutil
    import os
    
    path = 'test_dist'
    if not os.path.exists(path):
        os.makedirs(path)
        
    # Generate Packages to upload
    packages = ['dummy-package-1.0.0-py3-none-any.whl',
                'dummy-package-1.0.0.tar.gz']
    for package in packages:
        with open(os.path.join(path, package), 'w+') as f:
            f.write('Test content')

    upload_to_pypi(
        path=path,
        glob_patterns=['*.whl', '*gz'],
        skip_existing=True)
    
    shutil

# Generated at 2022-06-14 05:20:45.600606
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # If you run this test, then you need to set the environment variable TWINE_USERNAME, TWINE_PASSWORD and TWINE_REPOSITORY_URL
    # You also need to configure .pypirc (see https://docs.python.org/2/distutils/packageindex.html#pypirc)
    # You also need to have a test-package in dist folder
    upload_to_pypi("dist")

# Generated at 2022-06-14 05:20:53.107633
# Unit test for function upload_to_pypi
def test_upload_to_pypi():

    from unittest.mock import patch
    import tempfile

    with patch("semantic_release.hvcs.pypi.upload_to_pypi") as mock_upload_to_pypi:

        # Create a temp folder to use as a dist folder
        with tempfile.TemporaryDirectory() as tempdir:

            # Default configuration
            os.environ["PYPI_TOKEN"] = "pypi-XXXXXX"
            mock_upload_to_pypi(tempdir)
            cmd = mock_upload_to_pypi.mock_calls[0].args[0]
            expected_cmd = "twine upload -u '__token__' -p 'pypi-XXXXXX' '{}/*'".format(
                tempdir
            )
            assert cmd == expected_cmd



# Generated at 2022-06-14 05:21:06.568151
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Mock the run method, because we don't actually want to run the command :)
    global run
    run = lambda *args, **kwargs: None
    # Mock the environment variables
    os.environ["HOME"] = ""
    os.environ["PYPI_TOKEN"] = ""

    # Upload to PyPI
    upload_to_pypi()

    # Upload to Test PyPI
    upload_to_pypi(repository="testpypi")

    # Upload to Test PyPI with an API token
    os.environ["PYPI_TOKEN"] = "pypi-abcdefg"
    upload_to_pypi(repository="testpypi")

    # Upload to Test PyPI with an API token and skip existing

# Generated at 2022-06-14 05:21:14.980031
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    c = {"repository": "pypitest"}
    upload_to_pypi(skip_existing=True)
    upload_to_pypi(skip_existing=True, path="foo")
    upload_to_pypi(skip_existing=True, glob_patterns=["*"])
    upload_to_pypi(skip_existing=True, glob_patterns=["foo", "bar"])
    upload_to_pypi(skip_existing=True, glob_patterns=["foo", "bar"], path="foo")
    upload_to_pypi(skip_existing=True, glob_patterns=["foo", "bar"], path="foo")
    upload_to_pypi(skip_existing=True, glob_patterns=["foo", "bar"], path="foo")
    upload

# Generated at 2022-06-14 05:21:23.547919
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    os.environ['PYPI_TOKEN'] = "pypi-abcd"
    import sys
    sys.argv = ['','','','','','','','','','','','']
    sys.modules['twine'] = 'twine'
    sys.modules['invoke'] = 'invoke'
    sys.modules['invoke.run'] = 'run'
    assert upload_to_pypi(glob_patterns=['test'])

# Generated at 2022-06-14 05:21:32.790174
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Unit test for function upload_to_pypi"""
    from .helpers import mock_run
    from .decorators import logger_disabled

    # Verify that when missing username and password, ImproperConfigurationError is raised
    with logger_disabled(True):
        with mock_run(AttributeError('result.stdout')):
            from semantic_release.upload_to_pypi import upload_to_pypi
            from semantic_release import ImproperConfigurationError
            with pytest.raises(ImproperConfigurationError):
                upload_to_pypi.__wrapped__()

    # Verify that when an incomplete PyPI token is present, ImproperConfigurationError is raised

# Generated at 2022-06-14 05:21:34.013571
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi("dist") == "twine upload -u '__token__' -p 'pypi-123' 'dist/*'"