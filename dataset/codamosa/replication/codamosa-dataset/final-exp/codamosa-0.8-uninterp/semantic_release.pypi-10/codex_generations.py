

# Generated at 2022-06-14 05:12:53.013802
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert not "Upload successfully" in upload_to_pypi()


# Generated at 2022-06-14 05:12:58.552280
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Unit test for function upload_to_pypi."""
    try:
        upload_to_pypi()
    except ImproperConfigurationError:
        upload_to_pypi(glob_patterns=["*.whl"])
    else:
        assert False, "ImproperConfigurationError was not raised"

# Generated at 2022-06-14 05:12:59.300616
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert True

# Generated at 2022-06-14 05:13:01.349872
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert(upload_to_pypi.__name__ == "upload_to_pypi")



# Generated at 2022-06-14 05:13:03.328137
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(path="dist", glob_patterns=["*.egg-info"], skip_existing=True)

# Generated at 2022-06-14 05:13:07.906394
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    os.environ['PYPI_TOKEN'] = 'pypi-token'
    path = "dist"
    glob_pattern = '*.whl'
    glob_patterns = [glob_pattern]
    upload_to_pypi('dist', skip_existing=False, glob_patterns=glob_patterns)

# Generated at 2022-06-14 05:13:14.854829
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    class Callback:
        """Saves mock run for testing.
        """
        def __init__(self):
            self.args = []

        def __call__(self, cmd):
            self.args.append(cmd)

    def mock_run(cmd):
        """Save command for testing.
        """
        callback.__call__(cmd)

    callback = Callback()
    # Ensure user has no PYPI_TOKEN or PYPI_USERNAME and PYPI_PASSWORD
    if "PYPI_TOKEN" in os.environ:
        del os.environ["PYPI_TOKEN"]
    if "PYPI_USERNAME" in os.environ:
        del os.environ["PYPI_USERNAME"]

# Generated at 2022-06-14 05:13:22.611227
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # pylint: disable=unused-argument
    def run(command):
        assert (
            command
            == "twine upload -u '__token__' -p 'pypi-XXXXXXXXXXXX-XXXXXXXXXXXX' "
            '"dist/foo"'
        )


# Generated at 2022-06-14 05:13:29.669640
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    
    def mock_run(command):
        print("Fake run")
        os.environ["PYPI_TOKEN"] = "pypi-faketoken"

    run_func = run
    try:
        run = mock_run
        upload_to_pypi("dist", skip_existing=False, glob_patterns=["*"])
    finally:
        run = run_func
        os.environ["PYPI_TOKEN"] = "pypi-realtoken"

# Generated at 2022-06-14 05:13:38.220852
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .helpers import capture_output
    from contextlib import contextmanager

    @contextmanager
    def mock_environ(**environ):
        original_environ = os.environ.copy()
        os.environ.update(environ)
        try:
            yield
        finally:
            os.environ.clear()
            os.environ.update(original_environ)

    with mock_environ(HOME="/home/user") as mocked_environ, capture_output(logger) as out:
        out.__enter__()
        upload_to_pypi()
        print(out.getvalue())
        assert (
            "Uploading packages to PyPI requires credentials" in out.getvalue()
        ), "credentials error message"


# Generated at 2022-06-14 05:13:48.944710
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from unittest.mock import patch
    from invoke.exceptions import UnexpectedExit
    with patch("invoke.run") as mock_run:
        upload_to_pypi("dist")
        mock_run.assert_called_once_with('twine upload "dist/*"')

        mock_run.reset_mock()
        upload_to_pypi("dist", skip_existing=True)
        mock_run.assert_called_once_with('twine upload --skip-existing "dist/*"')

        mock_run.reset_mock()
        upload_to_pypi("dist", glob_patterns=["*.whl", "*.exe"])
        mock_run.assert_called_once_with('twine upload "dist/*.whl" "dist/*.exe"')

        # Username and password

# Generated at 2022-06-14 05:13:50.109514
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi

# Generated at 2022-06-14 05:14:03.212471
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    glob_patterns = ["*"]
    path = "dist"
    skip_existing = False
    # pylint: disable=protected-access
    upload_to_pypi.logger.info = Mock(return_value=None)
    run = Mock(return_value=None)

    # test without token
    with patch("semantic_release.hvcs.git.os.environ", new_callable=dict):
        with raises(ImproperConfigurationError):
            upload_to_pypi(path=path, skip_existing=skip_existing, glob_patterns=glob_patterns)

    # test with token
    token = "pypi-hello"
    username = "__token__"
    password = token

# Generated at 2022-06-14 05:14:07.402395
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    path = "dist"
    skip_existing = False
    glob_patterns = ["test_*"]
    os.environ["PYPI_TOKEN"] = "test_token"
    upload_to_pypi(path, skip_existing, glob_patterns)

# Generated at 2022-06-14 05:14:18.215502
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .helpers import mock_run
    from .helpers import mock_logger
    import pytest

    fake_logger = mock_logger()

    os.environ["PYPI_USERNAME"] = "username"
    os.environ["PYPI_PASSWORD"] = "password"
    with mock_run() as mock_run_function:
        upload_to_pypi(
            path="fake_path", skip_existing=True, glob_patterns=["fake_glob_patterns"]
        )
        mock_run_function.assert_called_once_with(
            "twine upload -u 'username' -p 'password' --skip-existing 'fake_path/fake_glob_patterns'"
        )


# Generated at 2022-06-14 05:14:25.906795
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .helpers import get_semantic_release_command, get_semantic_release_version

    import shutil
    import sys
    import tempfile

    # use a patched version of the function to get real values
    upload_to_pypi_real = run_twine_upload

    dist_dir = tempfile.mkdtemp()
    version = get_semantic_release_version()
    package_name = "test_example"

    semantic_release_command = get_semantic_release_command()
    os.system(
        f"{semantic_release_command} --no-verify --yes major {package_name} --dist-dir {dist_dir}"
    )


# Generated at 2022-06-14 05:14:26.321334
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:14:38.162859
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import tempfile
    import shutil
    import os
    import os.path
    import glob

    # Create temp dir and a project in it
    tmpdir = tempfile.mkdtemp()
    tmp_project_dir = os.path.join(tmpdir, "tmp_project")
    os.mkdir(tmp_project_dir)
    with open(os.path.join(tmp_project_dir, "setup.py"), "wt") as f:
        f.writelines(
            [
                "from setuptools import setup\n",
                "setup(name='testproject')",
                "setup(version='0.0.1')",
            ]
        )

    # Test upload with a package

# Generated at 2022-06-14 05:14:50.474214
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Test upload_to_pypi.

    :raises AssertionError: If upload_to_pypi does not meet expectations.
    """
    from semantic_release.repository_plugin import get_repository_plugin
    from semantic_release import setup_logger
    from semantic_release.history.vcs import get_version_from_tag
    from semantic_release.history.vcs import get_commit_log
    from semantic_release.history.vcs import get_tags
    from semantic_release.history.reader import get_history
    from semantic_release.history.writer import update_changelog
    from semantic_release.__main__ import perform_release
    from unittest.mock import patch
    import re
    import os
    import tempfile
    import shutil
    import sys


# Generated at 2022-06-14 05:14:51.416849
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi

# Generated at 2022-06-14 05:15:00.824185
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()

# Generated at 2022-06-14 05:15:06.063337
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """
    Test for the function upload_to_pypi
    """
    path = "dist"
    skip_existing = False
    glob_patterns = ["*"]
    upload_to_pypi(path, skip_existing, glob_patterns)

# Generated at 2022-06-14 05:15:16.495521
# Unit test for function upload_to_pypi

# Generated at 2022-06-14 05:15:27.014857
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import pytest
    try:
        os.remove("test-repo/dist/example-1.0.0.tar.gz")
        os.remove("test-repo/dist/example-1.0.0-py2.py3-none-any.whl")
        os.remove("test-repo/dist/example-1.0.0-py27-none-any.whl")
    except FileNotFoundError:
        pass
    with pytest.raises(ImproperConfigurationError):
        upload_to_pypi(path="test-repo/dist")
    os.environ["PYPI_USERNAME"] = "pypiusername"
    os.environ["PYPI_PASSWORD"] = "pypipassword"

# Generated at 2022-06-14 05:15:38.768927
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from unittest.mock import patch

    from .helpers import LoggedFunctionTest

    test = LoggedFunctionTest(logger)
    patch("os.environ", {})
    test.assertRaises(
        ImproperConfigurationError,
        "Missing credentials for uploading to PyPI",
        upload_to_pypi,
    )
    patch("os.environ", {"PYPI_TOKEN": "foo"})
    test.assertRaises(
        ImproperConfigurationError,
        'PyPI token should begin with "pypi-"',
        upload_to_pypi,
    )

    patch("os.environ", {"PYPI_USERNAME": "foo", "PYPI_PASSWORD": "bar"})

# Generated at 2022-06-14 05:15:42.350366
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    flag = False
    try:
        upload_to_pypi()
    except:
        flag = True
    assert flag

# Generated at 2022-06-14 05:15:45.740069
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    try:
        upload_to_pypi(glob_patterns=['*test'])
        assert False
    except ImproperConfigurationError:
        assert True

# Generated at 2022-06-14 05:15:57.316224
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .helpers import mock_open, mock_isfile, mock_os

    tokens = ["pypi-", "pypi-irrelevant-token", "pypi-irrelevant-token", "pypi-token"]

    def _mock_open(*args, **kwargs):
        if args[0] == "PYPI_TOKEN":
            return mock_open(read_data=tokens.pop(0)).return_value
        return open(*args, **kwargs)

    mock_os = mock_os(["fakepypiusername", "fakepypipassword", "fakehomedir"], "environ")
    mock_isfile = mock_isfile(["true", "false"])


# Generated at 2022-06-14 05:16:09.124071
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """
    This is a unit test for the function upload_to_pypi.
    """
    # case 1:
    # check function when path is not given
    # assertion:
    with pytest.raises(invoke.exceptions.Exit) as excinfo:
        upload_to_pypi()
    assert 'Missing credentials for uploading to PyPI' in str(excinfo.value)
    # case 2:
    # check function when credentials is given
    # assertion:
    upload_to_pypi("path",skip_existing=False,glob_patterns=['*'])
    assert 'twine upload  --skip-existing "path/*"' == call(
        ["twine", "upload", "--skip-existing", "path/*"])

# Generated at 2022-06-14 05:16:10.259277
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(path="dist")

# Generated at 2022-06-14 05:16:27.553763
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi() == None

# Generated at 2022-06-14 05:16:29.821623
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # pylint: disable=import-error
    from semantic_release import upload_to_pypi

    upload_to_pypi()

# Generated at 2022-06-14 05:16:43.792666
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Unit test for function upload_to_pypi.
    """
    from unittest import mock
    from .helpers import get_mock_context
    from .environ import mock_environ

    context = get_mock_context()

    with mock.patch.object(run, "__call__", return_value=''), \
         mock.patch('os.environ', mock_environ):
        # Test upload with api token
        mock_environ["PYPI_TOKEN"] = "pypi-token"
        upload_to_pypi(glob_patterns=["*"])
        run.__call__.assert_called_with(
            'twine upload -u \'__token__\' -p \'pypi-token\' --skip-existing \'"dist/*"\''
        )

# Generated at 2022-06-14 05:16:54.325215
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    dist_dir = "my/path/to/dist"
    glob_patterns = ["*.egg", "dist/*.tar.gz"]
    expected_command = (
        "twine upload  -u '__token__' -p 'pypi-token' "
        '"my/path/to/dist/{}.egg" "my/path/to/dist/{}.tar.gz"'.format(
            glob_patterns[0], glob_patterns[1]
        )
    )
    os.environ["PYPI_TOKEN"] = "pypi-token"
    upload_to_pypi(dist_dir, glob_patterns=glob_patterns)
    assert run.calls == [
        (expected_command, {}, None, None, None, None)
    ]

# Generated at 2022-06-14 05:16:56.779418
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    try:
        return upload_to_pypi()
    except ImproperConfigurationError as e:
        raise e

# Generated at 2022-06-14 05:16:57.836317
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()

# Generated at 2022-06-14 05:17:03.267581
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    if not os.environ.get('PYPI_TOKEN'):
        os.environ['PYPI_TOKEN'] = "pypi-dummy_token"
    upload_to_pypi()
    assert os.environ['PYPI_TOKEN'] == "pypi-dummy_token"

# Generated at 2022-06-14 05:17:04.545549
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi is not None

# Generated at 2022-06-14 05:17:06.521038
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    raise NotImplementedError("Test not implemented yet")



# Generated at 2022-06-14 05:17:16.749191
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .helpers import patch_invoke
    from .helpers import patch_logger
    import pytest
    from shutil import copytree, rmtree
    from tempfile import mkdtemp
    from pathlib import Path

    from semantic_release import ImproperConfigurationError

    from .helpers import cd
    from .helpers import Context
    from .helpers import patch_logger

    ctx = Context()

    # Test : upload_to_pypi without source or env var, should raise ImproperConfigurationError
    with pytest.raises(ImproperConfigurationError):
        upload_to_pypi()

    # Test : upload_to_pypi, wrong token should raise ImproperConfigurationError
    with pytest.raises(ImproperConfigurationError):
        upload_to_pypi(token="wrong-token")

   

# Generated at 2022-06-14 05:17:57.232392
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .helpers import create_mock_config, create_mock_runner, MockRun

    path = "dist/wheel"
    glob_pattern = "*"
    mock_runner = create_mock_runner((MockRun.success,))
    create_mock_config()
    upload_to_pypi(path=path, glob_patterns=[glob_pattern], _run=mock_runner)
    last_run = mock_runner.last_run
    assert last_run.command.startswith("twine upload")
    assert last_run.kwargs["env"]["TWINE_REPOSITORY_URL"] == config["dev_pypi_url"]
    assert '"{}/{}"'.format(path, glob_pattern) in last_run.command

# Generated at 2022-06-14 05:18:00.917474
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """ Test if the upload_to_pypi function succesfully uploads to pypi"""

    upload_to_pypi()

# Generated at 2022-06-14 05:18:13.247760
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    import sys
    import config
    print("\n\nTesting function upload_to_pypi")

    # cases:
    # missing token or username/password: ImproperConfigurationError
    # missing pypi- prefix on token: ImproperConfigurationError
    # missing home dir: ImproperConfigurationError
    # missing .pypirc in home dir: ImproperConfigurationError
    # all files and glob patterns exist in DIST_DIR: no error, glob patterns are included in the upload


    config.repository = 'test_repository'
    config.username = 'test_username'
    config.password = 'test_password'
    config.path = os.path.join(os.getcwd(), 'test', 'data')
    config.skip_existing = False
    config.glob_patterns = ['*']

    #

# Generated at 2022-06-14 05:18:20.448818
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .helpers import mock
    from .helpers import set_environment

    set_environment(PYPI_TOKEN="pypi-12345")

    with mock.patch("invoke.run") as mock_run:
        upload_to_pypi()
        assert mock_run.called
        args,kwargs = mock_run.call_args
        args = ' '.join(args)
        assert f"twine upload -u '__token__' -p 'pypi-12345' '*'" == args


# Generated at 2022-06-14 05:18:24.032539
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """
    Unit test for function upload_to_pypi()
    """
    assert "Cannot find twine in path or in {}".format(os.environ["PATH"])

test_upload_to_pypi()

# Generated at 2022-06-14 05:18:26.864350
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi("dist", True, ["*"])

# Generated at 2022-06-14 05:18:28.109282
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi('dist') == None

# Generated at 2022-06-14 05:18:30.932362
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(path="dummy", skip_existing=False, glob_patterns=[])



# Generated at 2022-06-14 05:18:32.448323
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi("test/test_dist", True)

# Generated at 2022-06-14 05:18:42.386801
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .test_helpers import mockrun

    username = "testuser"
    password = "testpassword"
    path = "test/path"
    glob_patterns = [
        "*.whl",
        "*.zip",
    ]
    repository = "testpypi"
    expected_dist = '"test/path/foo.whl" "test/path/bar.zip"'

    with mockrun() as mocks:
        upload_to_pypi(
            path=path,
            skip_existing=False,
            glob_patterns=glob_patterns,
        )

# Generated at 2022-06-14 05:19:50.614465
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi("dist") is None

# Generated at 2022-06-14 05:20:03.565425
# Unit test for function upload_to_pypi
def test_upload_to_pypi():

    # Test empty glob pattern list
    try:
        upload_to_pypi(glob_patterns = None)
        print("Upload failed")
    except ImproperConfigurationError:
        print("Upload skipped")

    # Test empty glob pattern list, with skip_existing
    try:
        upload_to_pypi(glob_patterns = None, skip_existing = True)
        print("Upload failed")
    except ImproperConfigurationError:
        print("Upload skipped")

    # Test with glob patterns, with skip_existing
    try:
        upload_to_pypi(glob_patterns = ["*"], skip_existing = True)
        print("Upload failed")
    except ImproperConfigurationError:
        print("Upload skipped")

    # Test with glob patterns

# Generated at 2022-06-14 05:20:04.458736
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:20:15.088495
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .test_utils import reset_config, capture_stdout_and_stderr
    from unittest.mock import patch, call
    from semantic_release.plugins.vcs.git import get_remote_url
    import tempfile, shutil
    import logging
    import os

    root = tempfile.mkdtemp()
    print(root)
    os.chdir(root)
    logging.info("Running in ", root)
    rmtree = shutil.rmtree
    upload_to_pypi(path=".", glob_patterns=["*"])
    shutil.rmtree = rmtree

# Generated at 2022-06-14 05:20:22.566427
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from unittest import mock
    from contextlib import contextmanager
    from tempfile import TemporaryDirectory
    @contextmanager
    def mocked_env(env):
        with mock.patch.dict('os.environ', env):
            yield
    # Using ENV variables
    env_vars_1 = {"PYPI_TOKEN":"pypi-test-token", "PYPI_USERNAME": "username", "PYPI_PASSWORD":"password"}
    env_vars_2 = {"PYPI_TOKEN": "pypi-test-token", "PYPI_USERNAME": "username", "PYPI_PASSWORD": "password", "HOME": "/home"}


# Generated at 2022-06-14 05:20:24.109482
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:20:25.252309
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()

# Generated at 2022-06-14 05:20:37.016570
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    class MockRun:
        def __init__(self):
            self.args = None

        def __call__(self, args):
            # pylint: disable=attribute-defined-outside-init
            self.args = args

    mock_run = MockRun()

    # Attempt to get an API token from environment
    #
    # Passing an API token
    os.environ["PYPI_TOKEN"] = "pypi-token"
    upload_to_pypi("dist", glob_patterns=["hello*", "world*"])
    assert mock_run.args == "twine upload -u '__token__' -p 'pypi-token' 'dist/hello*' 'dist/world*'"
    #
    # Passing a *private* API token

# Generated at 2022-06-14 05:20:37.651084
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert True

# Generated at 2022-06-14 05:20:49.478211
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Make sure tokens are sanitized, but everything else is not
    secret = "abcabcabc"
    assert upload_to_pypi(path=secret, skip_existing=True, glob_patterns=[]) == f'twine upload -u "" -p "" --skip-existing "dist/*"'

    # Make sure repository can be properly set
    repository = "https://pypi.org/index.html"
    assert upload_to_pypi(path=secret, skip_existing=False, glob_patterns=[]) == f'twine upload -u "" -p "" -r "{repository}" "dist/*"'

    # Make sure a token is properly set