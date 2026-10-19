

# Generated at 2022-06-14 05:12:51.832105
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(path = 'dist', skip_existing = False)
    assert True

# Generated at 2022-06-14 05:13:03.861687
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Unit test for function upload_to_pypi"""
    from .helpers import invoke_mocked_main, mock_run


# Generated at 2022-06-14 05:13:04.976775
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()

# Generated at 2022-06-14 05:13:05.553092
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:13:06.748064
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi("testing", True, ["*.tar.gz"])

# Generated at 2022-06-14 05:13:09.240870
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # TODO: Loop through each possible state of the environment
    # and ensure the proper errors are thrown.
    pass

# Generated at 2022-06-14 05:13:20.171776
# Unit test for function upload_to_pypi
def test_upload_to_pypi():

    dist = "unit_test_dist"
    skip_existing = True
    glob_patterns = ["example_*.whl"]
    os.environ["PYPI_USERNAME"] = "user"
    os.environ["PYPI_PASSWORD"] = "pw"
    os.environ["PYPI_REPOSITORY"] = "repo"

    try:
        upload_to_pypi(dist, skip_existing, glob_patterns)
    except:
        assert False

    os.environ["PYPI_TOKEN"] = "pypi-token"
    try:
        upload_to_pypi(dist, skip_existing, glob_patterns)
    except:
        assert False

    del os.environ["PYPI_TOKEN"]
    os.environ

# Generated at 2022-06-14 05:13:21.450170
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi("pipe", glob_patterns=["*.py"])

# Generated at 2022-06-14 05:13:30.643408
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import pytest
    from semantic_release.settings import config, load_config
    from semantic_release.config import setup_config
    from semantic_release import shell
    setup_config(shell)
    load_config()
    config.semantic_release.upload_to_pypi = True

    skip_existing = True
    path = "dist"
    glob_patterns = ["*"]

    with pytest.raises(ImproperConfigurationError):
        upload_to_pypi(
            path=path, skip_existing=skip_existing, glob_patterns=glob_patterns
        )

    os.environ["PYPI_TOKEN"] = "pypi-35a6129e7e15"
    os.environ["HOME"] = ""


# Generated at 2022-06-14 05:13:32.431375
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # TODO: write unit test for function upload_to_pypi
    pass

# Generated at 2022-06-14 05:13:39.048908
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Unit test for upload_to_pypi().
    """
    upload_to_pypi()

# Generated at 2022-06-14 05:13:49.948726
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .helpers import MockEnv

    env = MockEnv()
    env.set(
        "PYPI_TOKEN",
        "pypi-",
    )
    env.set(
        "PYPI_USERNAME",
        "__token__",
    )
    env.set(
        "PYPI_PASSWORD",
        "pypi-",
    )
    upload_to_pypi()
    env.set(
        "PYPI_TOKEN",
        "pypi-",
    )
    env.set(
        "PYPI_USERNAME",
        "__token__",
    )
    env.set(
        "PYPI_PASSWORD",
        "pypi-",
    )

# Generated at 2022-06-14 05:13:51.584309
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()

# Generated at 2022-06-14 05:13:56.980654
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from unittest.mock import patch

    with patch("invoke.run") as mock:
        upload_to_pypi(skip_existing=True)
        mock.assert_called_once_with(
            "twine upload  --skip-existing 'dist/*'"
        )

# Generated at 2022-06-14 05:14:00.356935
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """
    Upload to PyPI
    """
    # This might fail if the environment is not set up correctly.
    # In that case the unit test will fail.
    upload_to_pypi()

# Generated at 2022-06-14 05:14:03.576488
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    try:
        upload_to_pypi(path="dist", skip_existing=False, glob_patterns=None)
    except Exception as err:
        print(err)
        return False
    return True

# Generated at 2022-06-14 05:14:15.013048
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # pylint:disable=unused-argument
    def mock_run(cmd, hide=None):
        return cmd

    old_run = run
    run = mock_run

    # upload_to_pypi()
    path = "dist"
    skip_existing = False
    glob_patterns = ["*"]
    expected = 'twine upload  "dist/*"'
    assert upload_to_pypi(path, skip_existing, glob_patterns) == expected

    # upload_to_pypi(path='abc/def')
    path = "abc/def"
    skip_existing = False
    glob_patterns = ["*"]
    expected = 'twine upload  "abc/def/*"'
    assert upload_to_pypi(path, skip_existing, glob_patterns) == expected

   

# Generated at 2022-06-14 05:14:23.082702
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Replace the function by a mock to test it.
    """
    import unittest.mock
    from pathlib import Path
    from semantic_release.plugins.pypi.pypi import upload_to_pypi

    with unittest.mock.patch("invoke.run") as run_mock:
        upload_to_pypi("dist")
        assert run_mock.call_args == unittest.mock.call("twine upload 'dist/*'")

    with unittest.mock.patch("invoke.run") as run_mock:
        with unittest.mock.patch("os.environ", {
            "PYPI_TOKEN": "pypi-Token"
        }):
            upload_to_pypi("dist")
            assert run_mock

# Generated at 2022-06-14 05:14:23.777412
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:14:24.982186
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi

# Generated at 2022-06-14 05:14:34.844601
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi

# Generated at 2022-06-14 05:14:42.918196
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    
    # mock
    glob_patterns = ["dist/*"] # e.g. twine upload dist/example-0.0.1*
    mock_run = 'twine upload -u \'__token__\' -p \'pypi-token\' \'dist/example-0.0.1*\''
    assert upload_to_pypi(glob_patterns=glob_patterns) == mock_run

# Generated at 2022-06-14 05:14:53.335234
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Test the upload_to_pypi function
    """

    path1 = "dist"
    expected_output1 = "twine upload  'dist/semantic-release*'"
    assert upload_to_pypi(path1) == expected_output1, "The upload_to_pypi \
    function is not working properly"

    path2 = "dist"
    glob_patterns2 = ["*"]
    expected_output2 = "twine upload  'dist/semantic-release*'"
    assert upload_to_pypi(path2, glob_patterns2) == expected_output2, "The \
    upload_to_pypi function is not working properly"

    path3 = "dist"
    skip_existing3 = False
    glob_patterns3 = ["*"]
    expected_output3

# Generated at 2022-06-14 05:14:58.842750
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    with pytest.raises(ImproperConfigurationError):
        upload_to_pypi()

    assert upload_to_pypi.calls == 0
    os.environ["PYPI_TOKEN"] = "pypi-abc123"
    upload_to_pypi()
    assert upload_to_pypi.calls == 1
    assert upload_to_pypi.last_kwargs is not None
    assert upload_to_pypi.last_kwargs["glob_patterns"] == ["*"]

# Generated at 2022-06-14 05:15:10.076093
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    run_mock = MagicMock()

    with patch("semantic_release.upload_to_pypi.run", run_mock):

        with patch.dict(os.environ, {'PYPI_TOKEN': 'pypi-test_token'}):
            upload_to_pypi(path="test_path", skip_existing=True, glob_patterns=["test_pattern"])

        run_mock.assert_called_once_with(
            "twine upload -u '__token__' -p 'pypi-test_token'  --skip-existing \"test_path/test_pattern\""
        )

        run_mock.reset_mock()


# Generated at 2022-06-14 05:15:21.659852
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .helpers import mock, mock_run

    m_run = mock.patch("invoke.run", new_callable=mock_run)
    m_run.start()

    with m_run:
        upload_to_pypi(
            "test_dist",
            skip_existing=True,
            glob_patterns=["test_glob.whl", "test_glob2.whl"],
        )

        # Assert that three invocations were made

# Generated at 2022-06-14 05:15:25.334009
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # pylint: disable=unused-argument
    # Call the function with the given arguments
    upload_to_pypi("path", True, ["*"])

# Generated at 2022-06-14 05:15:26.567541
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert(upload_to_pypi)

# Generated at 2022-06-14 05:15:38.572101
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # pylint: disable=unused-argument
    def invoke_run(cmd: str):
        return None

    upload_to_pypi(
        path="dist", skip_existing=False, glob_patterns=["dist/*.whl"]
    )

    upload_to_pypi(
        path="dist", skip_existing=True, glob_patterns=["dist/*.whl"]
    )

    os.environ["PYPI_TOKEN"] = "pypi-__token"
    upload_to_pypi(path="dist", skip_existing=False, glob_patterns=["dist/*.whl"])

    config["repository"] = "my-repository"

# Generated at 2022-06-14 05:15:51.860738
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Tests for function upload_to_pypi.

    This will not test the actual upload, but only correct formatting of the command.
    """
    from invoke import Result
    
    from mock import patch
    
    # Set up some variables
    pypi_token = "pypi-sometoken"
    pypi_username = "someuser"
    pypi_password = "somepassword"
    my_repository = "somerepo"
    dist_path = "my/dist/path"
    
    # Set up environment variables
    os.environ["PYPI_TOKEN"] = pypi_token
    os.environ["PYPI_USERNAME"] = pypi_username
    os.environ["PYPI_PASSWORD"] = pypi_password

    # Test

# Generated at 2022-06-14 05:16:17.470257
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from semantic_release.hvcs import Git
    from semantic_release.settings import build_config

    cwd = os.getcwd()

# Generated at 2022-06-14 05:16:23.634265
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    args = ['/path/to/dist', True, ['*.whl']]
    run.assert_called_with(
        f"twine upload -u '__token__' -p 'pypi-some-token' --skip-existing '{args[0]}/{args[2][0].strip()}'"
    )

# Generated at 2022-06-14 05:16:31.081283
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Unit test
    """
    username = os.environ.get("PYPI_USERNAME")
    password = os.environ.get("PYPI_PASSWORD")
    if not (username or password):
        raise ImproperConfigurationError(
            "Missing credentials for uploading to PyPI"
        )

    repository = config.get("repository", None)
    repository_arg = f" -r '{repository}'" if repository else ""

    username_password = (
        f"-u '{username}' -p '{password}'" if username and password else ""
    )

    dist = " './*.tar.gz' './*.whl'"


# Generated at 2022-06-14 05:16:32.910677
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi()

# Generated at 2022-06-14 05:16:45.716445
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    def upload_with_token_error(token):
        os.environ["PYPI_TOKEN"] = token
        with pytest.raises(ImproperConfigurationError):
            upload_to_pypi()
        os.environ.pop("PYPI_TOKEN")

    # Test with token, username and password
    os.environ["PYPI_TOKEN"] = "pypi-abc123"
    with patch("invoke.run") as mock_run:
        upload_to_pypi()
        mock_run.assert_called_with(
            "twine upload -u '__token__' -p 'pypi-abc123' 'dist/*'"
        )
    os.environ.pop("PYPI_TOKEN")


# Generated at 2022-06-14 05:16:52.536556
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Unit test function to test this function"""
    username = os.environ["PYPI_USERNAME"]
    password = os.environ["PYPI_PASSWORD"]
    token = os.environ["PYPI_TOKEN"]
    assert username != "username"
    assert password != "password"
    assert token != "token"

# Generated at 2022-06-14 05:17:04.387996
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .helpers import MockContext, MockRun

    with MockContext(run, MockRun()) as r:
        upload_to_pypi(path="dist", skip_existing=False, glob_patterns=["*"])
        assert r.calls[0].args[0] == "twine upload  \"dist/*\""
        assert r.calls[0].kwargs == {}

        r.calls.clear()
        upload_to_pypi(
            path="dist",
            skip_existing=True,
            glob_patterns=["foo", "bar", "baz.whl", "qux.tar.gz"],
        )

# Generated at 2022-06-14 05:17:06.413874
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(path="dist", skip_existing=True, glob_patterns=["*"])

# Generated at 2022-06-14 05:17:07.640446
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()

# Generated at 2022-06-14 05:17:10.025675
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()
    upload_to_pypi(glob_patterns=["*",".*"])

# Generated at 2022-06-14 05:17:44.406560
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:17:48.967890
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import tempfile
    import zipfile

    with tempfile.TemporaryDirectory() as dist:
        archive = zipfile.ZipFile(os.path.join(dist, 'archive.zip'), 'w')
        archive.close()

        upload_to_pypi(dist, glob_patterns=['archive.zip'])

# Generated at 2022-06-14 05:17:49.961203
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert(upload_to_pypi())

# Generated at 2022-06-14 05:17:50.930150
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """

    :return:
    """

# Generated at 2022-06-14 05:18:04.201325
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Test for upload_to_pypi()."""
    username="testuser"
    password="testpassword"
    token="testtoken"
    repository = "test_pypi"
    dist_dir = 'dist'
    dist = "twine_test.whl"
    os.environ["PYPI_USERNAME"] = username
    os.environ["PYPI_PASSWORD"] = password
    os.environ["PYPI_TOKEN"] = token
    os.environ["TWINE_REPOSITORY"] = repository
    os.environ["TWINE_REPOSITORY_URL"] = "https://pypi.org/"
    os.environ["TWINE_USERNAME"] = username
    os.environ["TWINE_PASSWORD"] = password

# Generated at 2022-06-14 05:18:12.941333
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    path = "dist"
    skip_existing = False
    glob_patterns = ["*"]

    def mock_run(command):
        assert command == f"twine upload -u '__token__' -p 'pypi-token' --skip-existing \"dist/*\""

    run = mock_run
    os.environ['PYPI_TOKEN'] = 'pypi-token'

    upload_to_pypi(path, skip_existing, glob_patterns)

# Generated at 2022-06-14 05:18:22.894428
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    sample_token = "pypi-deadbeefdeadbeefdeadbeefdeadbeef"
    username = "username"
    password = "password"

    # No token, no username and password
    os.environ["PYPI_TOKEN"] = ""
    os.environ["PYPI_USERNAME"] = ""
    os.environ["PYPI_PASSWORD"] = ""
    os.environ["HOME"] = ""
    try:
        upload_to_pypi()
    except ImproperConfigurationError:
        pass

    # Valid token
    os.environ["PYPI_TOKEN"] = sample_token
    try:
        upload_to_pypi()
    except ImproperConfigurationError:
        pass

    # Invalid token
    os.environ["PYPI_TOKEN"]

# Generated at 2022-06-14 05:18:27.094161
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(path="tests/fixture/test_project/dist", skip_existing=True, glob_patterns=["mypackage*.whl"])

# Generated at 2022-06-14 05:18:38.513054
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    def mock_run(command, warn=False, hide=False, loglines=True):
        assert "twine upload" in command
        assert "some/path/dist/single.whl" in command
        assert "some/path/dist/multiple.whl" in command
        assert "some/path/dist/extra.whl" in command
        assert "__token__" in command
        assert "supersecuretoken" in command

    # Test with token
    logger.info("Testing upload_to_pypi with PYPI_TOKEN")
    os.environ["PYPI_TOKEN"] = "pypi-supersecuretoken"
    run = mock_run

# Generated at 2022-06-14 05:18:51.811324
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Tests whether the upload to PyPI works with a mocked environment
    """
    os.environ["PYPI_TOKEN"] = "pypi-1234567890abcdefghijklmnopqrstuvwxzy"
    # run = lambda cmd: None
    class Callable:
        def __init__(self):
            self.cmd = None
        def __call__(self, cmd):
            self.cmd = cmd

    r = Callable()
    globals()["run"] = r
    upload_to_pypi()
    cmd = r.cmd
    assert cmd == "twine upload -u '__token__' -p 'pypi-1234567890abcdefghijklmnopqrstuvwxzy' \"dist/*\""

# Generated at 2022-06-14 05:20:09.388103
# Unit test for function upload_to_pypi
def test_upload_to_pypi():

    # Assumes that the PyPI test credentials have been setup
    # https://packaging.python.org/tutorials/packaging-projects/#uploading-the-distribution-archives

    os.environ["PYPI_USERNAME"] = "pypitest"
    os.environ["PYPI_PASSWORD"] = "pypitest"
    expected_command = f"twine upload -u 'pypitest' -p 'pypitest' 'dist/test.tar.gz'"

    with LoggedFunction(logger):
        upload_to_pypi("dist", glob_patterns=["test.tar.gz"])

    assert expected_command == run.calls[0].command

# Generated at 2022-06-14 05:20:13.264932
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    try:
        os.environ["PYPI_TOKEN"] = "pypi-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    except:
        assert False, "Cannot setup env for PYPI_TOKEN"

# Generated at 2022-06-14 05:20:22.703863
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # given
    username = "test_user"
    password = "test_password"
    home_dir = "test_home_dir"
    path = "test_path"
    glob_patterns = ["test_pattern"]
    skip_existing = True

    class TestRun(object):
        def __init__(self, command):
            self.command = command

        def __call__(self, command):
            assert command == self.command

    # when
    test_run = TestRun(
        "twine upload -u '{}' -p '{}' --skip-existing '{}'".format(
            username, password, "test_path/test_pattern"
        )
    )
    os.environ["HOME"] = home_dir
    os.environ["PYPI_USERNAME"] = username

# Generated at 2022-06-14 05:20:28.085266
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(path="dist",
                   skip_existing=True,
                   glob_patterns=['*.whl','*.egg','*.zip','*.tar.gz','*.tar.bz','*.tar','*.tgz','*.tar.xz','*.tar.zst'])

# Generated at 2022-06-14 05:20:36.151817
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .mock_invoke import MockContext
    from .mock_invoke import MockRun
    c = MockContext()
    run = MockRun(c)
    c.config["repository"] = "test"
    with run:
        upload_to_pypi(path="", skip_existing=True, glob_patterns=["*"])
    assert run.commands[0] == "twine upload -u '__token__' -p 'pypi-TOKEN' -r 'test' --skip-existing \"/*\""

# Generated at 2022-06-14 05:20:46.798107
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .helpers import patch_run

    token_value = "pypi-x"

    patch_run(
        (
            "twine upload -u '__token__' -p 'pypi-x' "
            "-r 'my_custom_repo' --skip-existing "
            '"dist/foo.zip" "dist/bar.zip"'
        ),
        None,
    )

    upload_to_pypi(
        path="dist",
        skip_existing=True,
        glob_patterns=["foo.zip", "bar.zip"],
        repository="my_custom_repo",
    )

    os.environ["PYPI_TOKEN"] = token_value

# Generated at 2022-06-14 05:20:47.879430
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()

# Generated at 2022-06-14 05:20:49.698778
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """
    Test for uploading to pypi
    """
    upload_to_pypi(skip_existing=True)

# Generated at 2022-06-14 05:20:52.032914
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # TODO: write unit tests
    pass

# Generated at 2022-06-14 05:20:53.834136
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()