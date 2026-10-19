

# Generated at 2022-06-14 05:12:54.321489
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi("path", True, ["*"])
    upload_to_pypi("path", False, ["*"])
    upload_to_pypi("path", True, ["*.whl"])

# Generated at 2022-06-14 05:13:05.807873
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # pylint: disable=unused-variable
    import os
    from semantic_release.hvcs.git import _git_root  # noqa: F401

    from .helpers import LoggedFunction

    # Create a patch to LoggedFunction that outputs directly to the command line
    @LoggedFunction(logger)
    def LoggedFunction(func):
        def inner(*args, **kwargs):
            print(args[0].name)
            args[0](*args[1:], **kwargs)

        return inner

    # Create the fake PyPI credentials file to read from
    home_dir = os.environ.get("HOME", "")
    os.environ["HOME"] = os.path.join(os.getcwd(), "pypi")

# Generated at 2022-06-14 05:13:13.643879
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    run = MockRun()
    pypi_username = "abc"
    pypi_password = "def"
    pypi_token = "pypi-ghi"
    repository = "alpha"
    skip_existing = True
    glob_patterns = ["*", ".*.whl", "*.exe"]
    os.environ["PYPI_USERNAME"] = pypi_username
    os.environ["PYPI_PASSWORD"] = pypi_password
    os.environ["PYPI_TOKEN"] = pypi_token

# Generated at 2022-06-14 05:13:22.178574
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from unittest.mock import patch

    from semantic_release.settings import config
    from semantic_release.settings import load_config
    from semantic_release.settings import override_config
    from semantic_release.version_service import VersionService
    from semantic_release.history import History
    from semantic_release.errors import UnknownCommitMessageStyleError
    from semantic_release.errors import NoPreviousVersionError
    from semantic_release.errors import NoValidFilesFoundError
    from semantic_release.errors import ConfigNotFoundError
    import os

    with patch("invoke.run") as run_mock, patch("os.environ") as os_environ:
        os_environ["PYPI_TOKEN"] = "pypi-testtoken"
        os_environ["USER"] = "testuser"
        load_config()
       

# Generated at 2022-06-14 05:13:25.582843
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi == UploadToPyPI.invoke

# Generated at 2022-06-14 05:13:27.276475
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi("tests/test_project/dist", False, ["1.0.0-0.*"])

# Generated at 2022-06-14 05:13:30.725070
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """
    Test function
    """
    upload_to_pypi(path='dist', skip_existing=True, glob_patterns=['*'])

# Generated at 2022-06-14 05:13:34.343512
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Test upload_to_pypi function"""
    path = "tests/pkg/dist"
    glob_patterns = ["example"]
    upload_to_pypi(path, glob_patterns=glob_patterns)

# Generated at 2022-06-14 05:13:47.565493
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Unit test for function upload_to_pypi
    """
    from .helpers import tempdir

    with tempdir(
        """{
            "repository": "https://pypi.org/pypi",
            "pypi_token": "pypi-abcd1234"
        }"""
    ) as (directory, settings_path):
        os.mkdir("dist")
        with open("dist/somefile", "w") as _:
            pass

        settings = config.load_config(settings_path)
        settings.config["pypi"]["repository"] = "https://pypi.org/pypi"
        settings.config["pypi"]["pypi_token"] = "pypi-abcd1234"

# Generated at 2022-06-14 05:13:49.369459
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()

# Generated at 2022-06-14 05:13:54.978493
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()

# Generated at 2022-06-14 05:14:04.430564
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .helpers import mock_pypi_repo, mock_file_upload

    with mock_pypi_repo() as repository, mock_file_upload() as request:
        upload_to_pypi(
            skip_existing=True, glob_patterns=["*-py3-none-any.whl", "*-py2-none-any.whl"]
        )

        assert request.call_count == 2
        assert request.call_args_list[0][1]["data"]["name"] == "semantic_release"
        assert request.call_args_list[1][1]["data"]["name"] == "semantic_release_2"

# Generated at 2022-06-14 05:14:06.657343
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi("dist", False, ["*"])
    upload_to_pypi("dist", True, ["*"])

# Generated at 2022-06-14 05:14:17.679801
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    with context('', config={'repository': 'test'}, env={'PYPI_TOKEN': 'pypi-test_token'}):
        upload_to_pypi(glob_patterns=['README.md'])
        run.assert_called_once_with("twine upload -u __token__ -p pypi-test_token -r 'test' \"README.md\"")

    with context('', config={'repository': 'test'}, env={'PYPI_USERNAME': 'test', 'PYPI_PASSWORD': 'test'}):
        upload_to_pypi(glob_patterns=['README.md'])

# Generated at 2022-06-14 05:14:18.728620
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi

# Generated at 2022-06-14 05:14:22.428655
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    run("python setup.py sdist bdist_wheel")
    assert(os.path.exists("dist/semantic_release-0.0.1.tar.gz"))
    assert(os.path.exists("dist/semantic_release-2.4.1-py2.py3-none-any.whl"))
    upload_to_pypi()

# Generated at 2022-06-14 05:14:29.794357
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    username = "dummy_username"
    password = "dummy_password"
    os.environ["PYPI_USERNAME"] = username
    os.environ["PYPI_PASSWORD"] = password
    run.return_value = "SUCCESS"
    upload_to_pypi()
    run.assert_called_once_with(f"twine upload -u '{username}' -p '{password}' 'dist/*'")

# Generated at 2022-06-14 05:14:34.570464
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """
    Create and upload wheel package with valid arguments.
    """
    from semantic_release.services.pypi import upload_to_pypi

    path = "dist"
    skip_existing = True
    glob_patterns = ["*"]

    upload_to_pypi(path, skip_existing, glob_patterns)



# Generated at 2022-06-14 05:14:35.145150
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:14:48.483631
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    case = {
        "path": "test/dist",
        "skip_existing": True,
        "glob_patterns": [
            "test/dist/*.whl"
        ]
    }
    token = os.environ.get("PYPI_TOKEN")
    username = os.environ.get("PYPI_USERNAME")
    password = os.environ.get("PYPI_PASSWORD")
    home_dir = os.environ.get("HOME", "")
    repository = config.get("repository", None)
    repository_arg = f" -r '{repository}'" if repository else ""

    username_password = (
        f"-u '{username}' -p '{password}'" if username and password else ""
    )


# Generated at 2022-06-14 05:15:03.365836
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Setup mock
    import os
    import tempfile
    from mock import patch

    # Create dist folder
    dist_folder = tempfile.TemporaryDirectory(suffix='dist')
    dist_path = os.path.join(dist_folder.name, 'dist')
    os.makedirs(dist_path)

    # Create wheel files
    wheel_names = ['wheel_1-0.0.0-py3-none-any.whl', 'wheel_2-0.0.0-py3-none-any.whl']
    for wheel_name in wheel_names:
        file_path = os.path.join(dist_path, wheel_name)
        with open(file_path, 'w') as wheel_file:
            wheel_file.write('test_wheel_file')

    # Run command
   

# Generated at 2022-06-14 05:15:05.732174
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """
    :return:
    """
    # TODO: Need to refactor this function, map to test_helpers.py
    pass

# Generated at 2022-06-14 05:15:07.510468
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # No test for this function, but this is used for coverage.
    pass

# Generated at 2022-06-14 05:15:15.559382
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Test w/o files in dist dir
    with pytest.raises(ImproperConfigurationError):
        upload_to_pypi()

    # Test with files in dist dir
    with mock.patch("semantic_release.backends.pypi.upload_to_pypi.run") as mock_run:
        mock_run.return_value = "some_file.whl"
        upload_to_pypi()
        mock_run.assert_called_once_with(
            "twine upload  \"dist/some_file.whl\""
        )

# Generated at 2022-06-14 05:15:26.003686
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # Missing credentials
    os.environ.clear()
    try:
        upload_to_pypi()
    except ImproperConfigurationError as e:
        assert "Missing credentials for uploading to PyPI" in str(e)
    else:
        assert False, "Should not have passed"

    # Just a token
    os.environ["PYPI_TOKEN"] = "pypi-abcdefghijklmnopqrstuvwxyz0123456789"
    try:
        upload_to_pypi()
    except ImproperConfigurationError as e:
        assert 'PyPI token should begin with "pypi-"' in str(e)
    else:
        assert False, "Should not have passed"

    # Username and password

# Generated at 2022-06-14 05:15:26.754277
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert True

# Generated at 2022-06-14 05:15:28.500256
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    dist = "dist"
    assert dist == test_upload_to_pypi.__defaults__[0]

# Generated at 2022-06-14 05:15:39.434266
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from tempfile import TemporaryDirectory
    from glob import glob

    new_dist_dir = "new_dist"
    with TemporaryDirectory() as temp_dir, TemporaryDirectory(dir=temp_dir) as dist_temp_dir:
        # Make some fake dist files
        os.makedirs(os.path.join(temp_dir, new_dist_dir))
        dist_files = ["test-1.2.3.tar.gz", "test-1.2.3-py2.py3-none-any.whl"]
        for file in dist_files:
            os.mknod(os.path.join(dist_temp_dir, file))
        assert len(glob(os.path.join(dist_temp_dir, "*"))) == 2


# Generated at 2022-06-14 05:15:42.980407
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert run("python setup.py sdist bdist_wheel").ok
    assert not run("which twine").failed
    assert upload_to_pypi() == 1

# Generated at 2022-06-14 05:15:46.850200
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    run("touch 'dist/a.b'")
    run("touch 'dist/b.c'")
    upload_to_pypi("dist")
    run("rm -r 'dist'")


# Generated at 2022-06-14 05:16:05.583872
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Test creating an in-memory TwineRepository object."""

# Generated at 2022-06-14 05:16:15.963876
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    class Test:
        pass

    test_object = Test()
    test_object.packages = ["package1", "package2"]
    test_object.username = 'test_user'
    test_object.password = 'password123'
    test_object.repository = 'test-repository'
    test_object.glob_patterns = ["*"]
    test_object.skip_existing = True

# Generated at 2022-06-14 05:16:16.480686
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:16:20.313252
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """
    Test of the helper upload_to_pypi.
    """
    try:
        # pylint: disable=unused-variable
        import twine

        # Unsetting values to test code branch with invalid pypi credentials
        os.environ["PYPI_USERNAME"] = ""
        os.environ["PYPI_PASSWORD"] = ""
        os.environ["PYPI_TOKEN"] = ""
        raise ImproperConfigurationError("Missing credentials for uploading to PyPI")
    except ModuleNotFoundError:
        pass

# Generated at 2022-06-14 05:16:30.091511
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .helpers import ContextManager as CM
    import shutil
    import sys
    import filecmp
    import tempfile

    # Create dummy uploaded file
    temp_path = tempfile.mkdtemp()

    uploaded_file = open(temp_path + '/dummy_file.whl', 'w+')
    uploaded_file.close()


# Generated at 2022-06-14 05:16:44.162147
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """Test upload_to_pypi for Incorrect Configuration"""

    # Test with no config
    try:
        upload_to_pypi()
    except ImproperConfigurationError:
        pass
    else:
        assert False

    # Test with pypi username and password
    os.environ["PYPI_USERNAME"] = "dummy_user"
    os.environ["PYPI_PASSWORD"] = "dummy_password"
    try:
        upload_to_pypi()
    except ImproperConfigurationError:
        pass
    else:
        assert False
    os.environ["PYPI_USERNAME"] = ""
    os.environ["PYPI_PASSWORD"] = ""

    os.environ["PYPI_TOKEN"] = "dummy_token"

# Generated at 2022-06-14 05:16:46.267411
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()

# Generated at 2022-06-14 05:16:59.481300
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    try:
        old_env = dict(os.environ)
        os.environ.pop("PYPI_TOKEN", None)
        os.environ.pop("PYPI_USERNAME", None)
        os.environ.pop("PYPI_PASSWORD", None)
        assert "PYPI_TOKEN" not in os.environ, "cleanup failed"
        assert "PYPI_USERNAME" not in os.environ, "cleanup failed"
        assert "PYPI_PASSWORD" not in os.environ, "cleanup failed"

        upload_to_pypi()
        assert False, "missing credentials should raise ImproperConfigurationError"
    except ImproperConfigurationError:
        pass


# Generated at 2022-06-14 05:17:01.397300
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi()

# Generated at 2022-06-14 05:17:02.414939
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    # run it
    upload_to_pypi()

# Generated at 2022-06-14 05:17:36.590899
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi("dist", False, ["*"]) == None

# Generated at 2022-06-14 05:17:46.902161
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .helpers import create_lore_ipsum_file
    from .helpers import create_dist

    release_info = {
        "current_version": "1.0.0",
        "next_version": "1.1.0",
        "previous_version": "0.8.0",
        "type": "minor",
    }

    with create_dist() as (path, file_name):
        with create_lore_ipsum_file(path, file_name, release_info) as file:
            upload_to_pypi(path)
            assert True

# Generated at 2022-06-14 05:17:51.082784
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert (
        upload_to_pypi.__name__
        == "upload_to_pypi"
    ), "function name is not equal to 'upload_to_pypi'"

# Generated at 2022-06-14 05:17:52.124753
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi("dist")

# Generated at 2022-06-14 05:17:52.845252
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    pass

# Generated at 2022-06-14 05:17:55.717124
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(path='dist', skip_existing=True, glob_patterns=['*'])

# Generated at 2022-06-14 05:17:56.463472
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    return



# Generated at 2022-06-14 05:17:57.594223
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    assert upload_to_pypi()

# Generated at 2022-06-14 05:18:03.849928
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """
    TODO: What to test here?
    1) Test that the command is issue properly.
    2) Test that the command is issue with all the parameters properly (i.e. user, token and repo).
    3) Test that the credentials are parsed properly from the env
    4) Test when credentials are not set (code should fail).
    """
    pass

# Generated at 2022-06-14 05:18:14.515352
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from unittest.mock import patch

    with patch('invoke.run') as mock_run:
        path = 'path'
        glob_patterns = ['*']
        token = 'pypi-some-token'
        username = '__token__'
        password = token
        repository = 'some-repository'
        repository_param = f" -r '{repository}'"
        username_password = f"-u '{username}' -p '{password}'"
        skip_existing = True
        skip_existing_param = " --skip-existing"
        dist = '"{}/{}"'.format(path, glob_patterns[0].strip())


# Generated at 2022-06-14 05:19:30.737033
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    try:
        os.mkdir("dist")
    except OSError:
        pass
    # built-in open() uses text mode by default, but make-believe twine uses binary.
    with open("dist/test.whl", "wb") as f:
        f.write(b"test")
    try:
        upload_to_pypi()
    except ImproperConfigurationError:
        pass
    finally:
        os.remove("dist/test.whl")

# Generated at 2022-06-14 05:19:33.144467
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    """
    Unit test for function upload_to_pypi
    """
    assert True

# Generated at 2022-06-14 05:19:34.913096
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi_test = upload_to_pypi()

# Generated at 2022-06-14 05:19:37.453437
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi(
        path="dist",
        skip_existing=False,
        glob_patterns=["*.whl"],
    )

# Generated at 2022-06-14 05:19:38.587056
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()

# Generated at 2022-06-14 05:19:47.327801
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    def test_upload_to_pypi_helper(specification):
        def test():
            mock_run = Mock()
            argspec = getargspec(upload_to_pypi)
            with patch(
                "semantic_release.hvcs.upload.pypi.run", mock_run
            ) as patched:
                path = specification.get('path', "dist")
                skip_existing = specification.get('skip_existing', False)
                glob_patterns = specification.get('glob_patterns', [])
                upload_to_pypi(path, skip_existing, glob_patterns=glob_patterns)
                expected_command = specification['expected_command']
                patched.assert_called_with(expected_command)
            # Check that we have the right number of args
            assert len

# Generated at 2022-06-14 05:20:01.469252
# Unit test for function upload_to_pypi
def test_upload_to_pypi():

    import os
    import subprocess
    import time

    from semantic_release import pypi as module

    prefix = str(time.time())

    # Generate a test file
    with open(f"dist/{prefix}.txt", "w") as file:
        file.write("test")

    # Run the function
    try:
        module.upload_to_pypi(path=f"dist/", skip_existing=False, glob_patterns=[f"{prefix}.txt"])
    except:
        pass

    # Ensure the file is now on test PyPI
    if prefix in [w for w in subprocess.getoutput("twine list").splitlines()]:
        assert True
    else:
        assert False

    # Cleanup
    os.system(f"rm dist/{prefix}.txt")

# Generated at 2022-06-14 05:20:03.146333
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    try:
        import twine
        assert True
    except ImportError:
        assert False

# Generated at 2022-06-14 05:20:04.384168
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    upload_to_pypi()

# Generated at 2022-06-14 05:20:15.087287
# Unit test for function upload_to_pypi
def test_upload_to_pypi():
    from .testing import mock_subprocess
    from .testing import make_local_repository
    from .testing import make_version_module
    from .testing import make_project_config

    def mock_subprocess_upload(cmd):
        assert cmd.startswith("twine")

    with make_local_repository("repo") as repo:
        with mock_subprocess(mock_subprocess_upload), make_project_config(
            "repo", version_module=make_version_module()
        ) as config:
            upload_to_pypi(skip_existing=False, glob_patterns=["*"])

