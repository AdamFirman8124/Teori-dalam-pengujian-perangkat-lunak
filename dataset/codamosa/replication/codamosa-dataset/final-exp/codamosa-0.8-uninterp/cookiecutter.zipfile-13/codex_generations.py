

# Generated at 2022-06-13 18:50:07.228399
# Unit test for function unzip
def test_unzip():
    import shutil
    import tempfile
    import zipfile

    def create_test_zipfile(archive_name, file_list):
        with zipfile.ZipFile(archive_name, 'w', zipfile.ZIP_DEFLATED) as zf:
            for fname in file_list:
                zf.write(fname)
        return archive_name

    # Construct a temporary directory, to be used as a cookiecutter repo
    temp_cookiecutter_repo = tempfile.mkdtemp()

    # Construct a test zipfile
    test_directory = os.path.join(temp_cookiecutter_repo, 'test_directory')
    os.mkdir(test_directory)
    test_file = os.path.join(test_directory, 'file.txt')

# Generated at 2022-06-13 18:50:14.001276
# Unit test for function unzip
def test_unzip():
    # Test extracting a protected repository
    passwd = os.environ.get('TEST_REPO_ZIP_PASSWORD')
    if passwd is not None:
        # TODO
        pass
    else:
        # Test extracting an unprotected repository
        unzip_path = unzip(
            'https://codeload.github.com/Audreyr/cookiecutter-pypackage/zip/master',
            True,
            clone_to_dir='tmp'
        )
        import shutil
        shutil.rmtree(unzip_path)

# Generated at 2022-06-13 18:50:23.880030
# Unit test for function unzip
def test_unzip():
    """
    Test whether the unzip function works correctly with a valid zip
    Curretnly not working as in pycharm the unzip function mounts permission denied.
    :return:
    """

    # expected
    expected_path = None
    expected_error_message = None

    # temporary file
    fp = tempfile.TemporaryFile()
    fp.write(b"test")
    fp.seek(0)

    # create zip file
    zip_obj = ZipFile('test_zip.zip', 'w')
    zip_obj.writestr('test_dir/', fp.read())
    zip_obj.close()

    # test

# Generated at 2022-06-13 18:50:35.769298
# Unit test for function unzip
def test_unzip():
    # TODO(waldenburg): Why are these tests not in tests.py?
    import shutil
    import requests_mock

    def mock_requests(uri, content=None):
        if content is not None:
            assert isinstance(content, bytes)

        def request_callback(request, context):
            context.status_code = 200
            return content

        with requests_mock.Mocker() as mock:
            mock.get(uri, text=request_callback)
            return mock

    # Local zip file with unprotected files
    # i.e. repo.zip file from cookiecutter-pypackage.
    repo_zip = os.path.join(
        os.getcwd(), 'tests/fixtures/repo-unprotected.zip'
    )
    # Local zip file with password-protected files
    #

# Generated at 2022-06-13 18:50:42.793953
# Unit test for function unzip
def test_unzip():
    import pytest
    import os
    import shutil
    from cookiecutter.utils import which
    from tempfile import mkdtemp
    from tests.test_cookiecutter import clean_empty_dir

    def _test_unzip_helper(is_url, filepath, no_input=False):
        unzip_dir = unzip(filepath, is_url=is_url, no_input=no_input)
        assert os.path.isdir(unzip_dir)

        # Assert some files we expect to see
        for fname in ('README.rst', 'hooks', '{{cookiecutter.repo_name}}'):
            assert os.path.exists(os.path.join(unzip_dir, fname))

        shutil.rmtree(unzip_dir)


# Generated at 2022-06-13 18:50:50.817834
# Unit test for function unzip
def test_unzip():
    import shutil
    import stat
    import sys
    import zlib

    def create_zipfile(filepath):
        zipfd = open(filepath, 'wb')
        zip = ZipFile(zipfd, 'w')
        zip.writestr('package/__init__.py', '# package')
        zip.writestr('package/file1.py', '# file1 in package')
        zip.writestr('package/file2.py', '# file2 in package')
        zip.close()
        zipfd.close()

    def create_protected_zipfile(filepath, passwd):
        zipfd = open(filepath, 'wb')
        zip = ZipFile(zipfd, 'w')
        zip.writestr('package/__init__.py', '# package')
        zip.writest

# Generated at 2022-06-13 18:50:53.558296
# Unit test for function unzip
def test_unzip():
    os.system("touch file.zip")
    unzip("file.zip", is_url=False)
    os.system("rm file.zip")

# Generated at 2022-06-13 18:51:00.348466
# Unit test for function unzip
def test_unzip():
    # os.chdir('/Users/yekx/Works/CookieCutter/CookieCutter')
    unzip_path = unzip('../tests/test-repo-pre/', is_url=False)
    assert os.path.isdir(unzip_path)
    # os.chdir('/Users/yekx/Works/CookieCutter/CookieCutter')

# Generated at 2022-06-13 18:51:01.037319
# Unit test for function unzip
def test_unzip():
    pass


# Generated at 2022-06-13 18:51:06.478091
# Unit test for function unzip
def test_unzip():
    import shutil
    import zipfile
    import tempfile
    from unittest.mock import patch


    repo_zip_path = os.path.join(
        os.path.dirname(__file__), '..', '..',
        'tests', 'test-repo-tmpl', 'test-repo.zip'
    )

    repo_zip_prot_path = os.path.join(
        os.path.dirname(__file__), '..', '..',
        'tests', 'test-repo-tmpl', 'test-repo-prot.zip'
    )

    def unzip_url(url):
        temp = tempfile.mkdtemp()
        unzip = unzip(url, True, temp)
        shutil.rmtree(temp)
        return unzip

   

# Generated at 2022-06-13 18:51:21.455633
# Unit test for function unzip
def test_unzip():
    """
    Test for cookiecutter.utils.unzip
    """
    import os
    import shutil
    import tempfile
    import zipfile

    import pytest

    @pytest.fixture(params=[True, False])
    def temp_zip_path(request):
        zip_file_name = 'foo.zip'
        temp_path = tempfile.mkdtemp()
        zip_path = os.path.join(temp_path, zip_file_name)
        zip_file = zipfile.ZipFile(zip_path, mode='w')

        if request.param:
            zip_file.writestr('foo.txt', b'foo')
        else:
            zip_file.writestr('bar/bar.txt', b'bar')

        zip_file.close()

        yield zip_path



# Generated at 2022-06-13 18:51:31.383960
# Unit test for function unzip
def test_unzip():
    """Unit test for function unzip"""
    import zipfile
    import sys
    import time

    # create a zip file
    test_zip = tempfile.NamedTemporaryFile(suffix='.zip')
    zip_file = zipfile.ZipFile(test_zip, 'w')
    zip_file.writestr(
        'doesnotexist/doesnotexist',
        'test file text',
        zipfile.ZIP_DEFLATED,
    )
    zip_file.close()

    # test unzip
    test_unzip = unzip(test_zip.name, False)
    assert test_unzip == tempfile.gettempdir() + '/doesnotexist'

    # remove unzipped file
    os.remove(tempfile.gettempdir() + '/doesnotexist/doesnotexist')
    os

# Generated at 2022-06-13 18:51:35.838561
# Unit test for function unzip
def test_unzip():
    """Unit test for function unzip.

    Return:
        str: The path to the extracted repo.
    """
    expected_repo_name = 'cookiecutter-pypackage'
    assert unzip('./tests/test-repos/' + expected_repo_name + '.zip', is_url=False).endswith(expected_repo_name)

# Generated at 2022-06-13 18:51:36.760050
# Unit test for function unzip
def test_unzip():
    pass

# Generated at 2022-06-13 18:51:37.585628
# Unit test for function unzip
def test_unzip():
    pass

# Generated at 2022-06-13 18:51:43.011185
# Unit test for function unzip
def test_unzip():
    try:
        unzip('/tmp/test/cookiecutter-pypackage/tests/fixtures/dummy/',
                False, '/tmp/haha', no_input=True, password=None)
    except Exception as e:
        pass
    assert True

# Generated at 2022-06-13 18:51:53.521837
# Unit test for function unzip
def test_unzip():
    """
    unzip() should raise a InvalidZipRepository Exception if:
        * Zipfile is empty
        * Zipfile does not include a top-level directory
        * Zipfile is not a valid zip archive
    """
    try:
        unzip('tests/test-repos/empty_dir.zip', True, no_input=True)
    except InvalidZipRepository:
        pass
    else:
        assert False

    try:
        unzip('tests/test-repos/bad_top_level.zip', True, no_input=True)
    except InvalidZipRepository:
        pass
    else:
        assert False

    try:
        unzip('tests/test-repos/not_a_zipfile.zip', True, no_input=True)
    except InvalidZipRepository:
        pass

# Generated at 2022-06-13 18:52:06.020061
# Unit test for function unzip
def test_unzip():
    """
    Check the function unzip
    """
    import urllib
    import os
    import shutil
    import sys
    import unittest

    class Test_Unzip(unittest.TestCase):
        """
        Test the method unzip
        """
        # Test valid path
        def test_valid_path(self):
            """test_valid_path"""
            zip_uri = os.path.join(
                os.path.dirname(__file__),
                'test_files',
                'test_archive.zip'
            )

            unzip_path = unzip(
                zip_uri=zip_uri,
                is_url=False,
                clone_to_dir='.',
                no_input=False,
                password=None
            )
            unzip_path = unzip_

# Generated at 2022-06-13 18:52:15.739203
# Unit test for function unzip
def test_unzip():
    """Test unzip function."""
    # TODO: Make this test more robust
    test_folder = os.path.dirname(__file__)
    options = {
        'no-input': True,
        'extra_context': {},
        'checkout': None,
        'replay': False,
        'overwrite_if_exists': False,
        'skip_if_file_exists': False,
        'output_dir': None,
        'config_file': None
    }

    test_zip_uri = os.path.join(test_folder, 'test_cookiecutter')
    unzip_path = unzip(test_zip_uri, False, 'cookie', **options)
    assert os.path.isdir(unzip_path)



# Generated at 2022-06-13 18:52:26.738646
# Unit test for function unzip
def test_unzip():
    import os
    import shutil

    test_dir = os.path.dirname(os.path.abspath(__file__))
    out_dir = os.path.join(test_dir, 'test_unzip_output')
    if os.path.exists(out_dir):
        shutil.rmtree(out_dir)

    # Passing normal zip file
    zip_uri = os.path.join(test_dir, 'files', 'simple_repo.zip')
    unzip(zip_uri, False, out_dir)

    # Check for empty zip file
    zip_uri = os.path.join(test_dir, 'files', 'empty.zip')
    unzip(zip_uri, False, out_dir)

    # Check for file without top level directory
    zip_uri = os.path

# Generated at 2022-06-13 18:52:48.200830
# Unit test for function unzip
def test_unzip():
    archive_dir = os.path.dirname(os.path.dirname(__file__))
    test_zip = os.path.join(archive_dir, 'tests', 'test-repo-tmpl', 'cookiecutter-tests.zip')
    unzip_path = unzip(zip_uri=test_zip, is_url=False)
    assert os.path.exists(unzip_path) is True
    assert os.path.exists(os.path.join(unzip_path, 'README.rst')) is True

# Generated at 2022-06-13 18:52:54.697394
# Unit test for function unzip
def test_unzip():
    import unzip_setuptools
    from .test_identify_repo import GIT_REPO_ZIP
    from .test_repository import cookiecutter_json
    unzip(GIT_REPO_ZIP, True, '.', True)
    assert cookiecutter_json == 'test.json'

# Generated at 2022-06-13 18:52:57.983453
# Unit test for function unzip
def test_unzip():
    filename = 'tests/fake-repo-tmpl/fake-repo-master.zip'

    unzip_path = unzip(filename, False)
    assert os.path.exists(unzip_path)

    os.remove(unzip_path)

# Generated at 2022-06-13 18:53:07.103232
# Unit test for function unzip
def test_unzip():
    """Test for the unzip function.
    """
    # Check file download
    # This needs to pull data from the internet to test.
    # It is enabled for when needed.
    if False:
        zip_uri = "https://github.com/audreyr/cookiecutter-pypackage/archive/master.zip"
        is_url = True
        clone_to_dir = '/tmp'
        no_input = False
        password = None
        unzip(zip_uri, is_url, clone_to_dir, no_input, password)

    # Check file download and extraction
    zip_uri = "http://bit.ly/cookiecutter-pypackage"
    is_url = True
    clone_to_dir = '/tmp'
    no_input = False
    password = None

# Generated at 2022-06-13 18:53:07.765061
# Unit test for function unzip
def test_unzip():
    pass

# Generated at 2022-06-13 18:53:13.696589
# Unit test for function unzip
def test_unzip():
    """Test that function doesnt crash. -- no real unit test yet.
    """

    # TODO: This test is not atomic. The unzipped file might be left on the FS if the test fails.
    path = unzip('https://github.com/audreyr/cookiecutter-pypackage/archive/master.zip',
                 is_url=True)
    assert path.startswith('/tmp/')

# Generated at 2022-06-13 18:53:15.902156
# Unit test for function unzip
def test_unzip():
    assert unzip('cookiecutter-pypackage', False) == 'cookiecutter-pypackage'


# Generated at 2022-06-13 18:53:16.675197
# Unit test for function unzip
def test_unzip():
    assert True == True

# Generated at 2022-06-13 18:53:25.946961
# Unit test for function unzip
def test_unzip():
    import filecmp
    import shutil
    import os.path
    
    base_src = 'https://github.com/daviddonnelly/cookiecutter-testing-unzip/archive'
    zip_uri = base_src + '/master.zip'
    local_zip_uri = 'tests/test_unzip/master.zip'
    local_unzip_path = 'tests/test_unzip/master'
    unzip_path = unzip(zip_uri, True, clone_to_dir='tests/test_unzip', no_input=True)
    
    assert(os.path.exists(unzip_path))
    assert(filecmp.cmp(unzip_path, local_unzip_path))
    
    # test with local zip file

# Generated at 2022-06-13 18:53:26.603083
# Unit test for function unzip
def test_unzip():
    pass

# Generated at 2022-06-13 18:53:58.628353
# Unit test for function unzip
def test_unzip():

    try:
        import StringIO
    except ImportError:
        from io import StringIO

    from zipfile import ZIP_DEFLATED
    from zipfile import ZipFile

    import tempfile
    import os

    with tempfile.NamedTemporaryFile() as arch:
        arch.write('nothing')
        arch.flush()

        try:
            unzip(arch.name, False)
        except InvalidZipRepository:
            pass
        else:
            assert False

    with tempfile.NamedTemporaryFile() as arch:
        zf = ZipFile(arch, 'w')
        zf.writestr('topdir/', '', ZIP_DEFLATED)
        zf.writestr('topdir/firstdir/', '', ZIP_DEFLATED)

# Generated at 2022-06-13 18:53:59.415118
# Unit test for function unzip
def test_unzip():
    pass

# Generated at 2022-06-13 18:54:10.932739
# Unit test for function unzip
def test_unzip():
    from cookiecutter.utils import generate_files
    from nose.tools import assert_raises

    class Arg(object):

        def __init__(self, **kwargs):
            for key, value in kwargs.items():
                setattr(self, key, value)
    import shutil
    tmp_dir = generate_files()

    actual_dir = os.path.abspath(tmp_dir)

    zip_file_path = os.path.join(actual_dir, 'cookiecutter_tmp.zip')

    try:
        import zipfile
        with zipfile.ZipFile(zip_file_path, 'w') as myzip:
            myzip.write(actual_dir, 'cookiecutter_tmp')
    except Exception as e:
        raise e

    # test the function
    tmp_unzip_

# Generated at 2022-06-13 18:54:13.980788
# Unit test for function unzip
def test_unzip():
    """Simple unit test for function unzip."""
    assert unzip('zipfile.zip', False) is None
    assert unzip('https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/archive/master.zip', True) is None

# Generated at 2022-06-13 18:54:23.833390
# Unit test for function unzip
def test_unzip():
    from zipfile import ZIP_DEFLATED
    import requests
    import time
    import shutil

    # create a temp dir and set it as the working directory
    import tempfile
    temp_dir = tempfile.mkdtemp()
    os.chdir(temp_dir)
    
    # create some files and a subfolder to create a repo
    os.mkdir(os.path.join(temp_dir, 'tests_unzip'))
    with open(os.path.join(temp_dir, 'tests_unzip', 'test_file1'), 'w+') as f:
        f.write('test')
    with open(os.path.join(temp_dir, 'tests_unzip', 'test_file2'), 'w+') as f:
        f.write('test')

# Generated at 2022-06-13 18:54:31.663588
# Unit test for function unzip
def test_unzip():
    import shutil
    import zipfile


# Generated at 2022-06-13 18:54:38.646782
# Unit test for function unzip
def test_unzip():
    project_name = "python-xyz"
    unzip_path = unzip(zip_uri="https://api.github.com/repos/audreyr/cookiecutter-pypackage/zipball",
                       is_url=True, clone_to_dir=".", no_input=True)
    unzip_dirs = os.listdir(unzip_path)

    assert len(unzip_dirs) == 1
    assert unzip_dirs[0] == project_name

    # TODO: Add tests once we can invoke the function with a password

# TODO: Add more unit tests, instructions on how to use a password etc.

# Generated at 2022-06-13 18:54:50.790995
# Unit test for function unzip
def test_unzip():
    import shutil
    import zipfile
    import io
    from testfixtures import tempdir, log_capture
    from cookiecutter.utils import rmtree, rmdir

    # Prepare zip file
    temp_directory = tempdir()
    source_dir = temp_directory.makedir('source_dir')
    archive_name = os.path.join('source_dir', 'test.zip')

    # Create archive and add files
    with zipfile.ZipFile(archive_name, 'w') as archive:
        archive.writestr('first_file', 'Test content')
        archive.writestr('folder/second_file', 'Second test content')

    # Run function unzip
    # First without password
    # Then with password
    password = ''
    # Without password

# Generated at 2022-06-13 18:55:01.212824
# Unit test for function unzip
def test_unzip():
    import os
    from zipfile import ZipFile
    from shutil import rmtree
    from pathlib import Path
    from pytest import raises
    from cookiecutter.utils import normalize, rmtree_tempdir

    cur_path = Path(__file__).parent.resolve()

    def remove_files_in_dir(path):
        for f in os.listdir(path):
            os.unlink(os.path.join(path, f))

    assert cur_path.is_dir()

    # Create temporary directory
    tempdir = os.path.join(cur_path, 'test_unzip')
    make_sure_path_exists(tempdir)

    assert os.path.isdir(tempdir)
    assert not os.listdir(tempdir)

    # Negative test for function unzip, expect

# Generated at 2022-06-13 18:55:11.101531
# Unit test for function unzip
def test_unzip():
    """Test unzipping a valid file and an invalid file"""
    import requests_mock
    from contextlib import contextmanager
    from cookiecutter.utils import rmtree

    @contextmanager
    def mock_url(url, content):
        with requests_mock.Mocker() as m:
            m.get(
                url,
                content=content,
                headers={
                    'Content-Type': 'application/zip',
                    'Content-Disposition': 'attachment; filename=repo.zip',
                },
            )
            yield m

    def mkzip(paths):
        """Create a test zip file"""
        import io
        import zipfile

        f = io.BytesIO()
        with zipfile.ZipFile(f, 'w') as z:
            for p in paths:
                z.writestr

# Generated at 2022-06-13 18:56:14.643729
# Unit test for function unzip
def test_unzip():
    import os
    import zipfile
    import shutil
    import requests
    import glob
    import json
    import subprocess
    import filecmp
    import getpass
    import time
    import sys
    import tarfile

    # Create a temp directory
    tempdir = tempfile.mkdtemp()

    # Clone the test repo
    subprocess.check_call(['git', 'clone', 'https://github.com/audreyr/cookiecutter-pypackage.git'], cwd=tempdir)

    # Make it a package
    subprocess.check_call(['python', 'setup.py', 'sdist'], cwd=os.path.join(tempdir, 'cookiecutter-pypackage'))

    # Grab the resulting package

# Generated at 2022-06-13 18:56:24.706402
# Unit test for function unzip
def test_unzip():
    # Local zip
    #   cookiecutter.json in the root
    #   cookiecutter.json in subdir
    #   empty directory
    local_zip = os.path.join(os.path.dirname(__file__), 'repo-tmpl.zip')
    unzip_path = unzip(local_zip, False)
    assert os.path.isfile(os.path.join(unzip_path, 'cookiecutter.json'))
    assert os.path.isfile(os.path.join(unzip_path, 'simple', 'cookiecutter.json'))
    assert os.path.isdir(os.path.join(unzip_path, 'empty_dir'))
    os.rmdir(os.path.join(unzip_path, 'empty_dir'))

# Generated at 2022-06-13 18:56:27.701229
# Unit test for function unzip
def test_unzip():
    try:
        assert unzip(
            zip_uri='https://github.com/audreyr/cookiecutter-pypackage/archive/master.zip',
            is_url=True,
            clone_to_dir='.',
            no_input=False,
            password=None
        )
    except RuntimeError:
        pass

# Generated at 2022-06-13 18:56:39.213970
# Unit test for function unzip
def test_unzip():
    from unittest import TestCase
    from mock import patch
    from requests.exceptions import RequestException
    from requests.models import Response

    class unzipTest(TestCase):
        def setUp(self):
            self.zip_uri = 'https://bitbucket.org/pokoli/cookiecutter-pylons/get/tip.zip'
            self.zip_uri_file_path = os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                'zip_repository.zip'
            )
            self.clone_to_dir = tempfile.mkdtemp()
            self.patch('requests.get', side_effect=RequestException)


# Generated at 2022-06-13 18:56:48.556165
# Unit test for function unzip
def test_unzip():
    import shutil

    dir_name = "test/test_zip"
    shutil.rmtree(dir_name, ignore_errors=True)
    os.mkdir(dir_name)
    os.mkdir(os.path.join(dir_name, "tests"))
    os.mkdir(os.path.join(dir_name, "tests", "bar"))
    file_path = os.path.join(dir_name, "tests", "bar", "foo.txt")
    with open(file_path, "w") as f:
        f.write("hello")

    zip_file_name = os.path.join(dir_name, "test_zip.zip")
    os.chdir(os.path.dirname(dir_name))

# Generated at 2022-06-13 18:56:51.681528
# Unit test for function unzip
def test_unzip():
    zip_name = "test_repo.zip"
    test_dir = "tests/test-output/test-zip"
    unzip_path = unzip(zip_name, False, test_dir)
    assert os.path.exists(unzip_path)

# Generated at 2022-06-13 18:56:54.596644
# Unit test for function unzip
def test_unzip():
    """Verifies if the unzip function works."""
    with tempfile.TemporaryDirectory() as clone_to_dir:
        unzip('https://github.com/Cookiecutter/cookiecutter/archive/master.zip', True, clone_to_dir)

# Generated at 2022-06-13 18:56:56.078253
# Unit test for function unzip
def test_unzip():
    # TODO: Add test for function unzip
    return

# Generated at 2022-06-13 18:57:11.225314
# Unit test for function unzip
def test_unzip():
    # Build a temporary directory containing the zip archive
    import shutil
    from cookiecutter.main import cookiecutter

    # Build a temporary zipfile containing the repository
    tmp_repo_dir = tempfile.mkdtemp()
    repo_contents = '{{cookiecutter.project_name}}'
    cookiecutter(
        test_repo,
        no_input=True,
        extra_context={'project_name': 'foobar'},
        overwrite_if_exists=True,
        output_dir=tmp_repo_dir
    )
    zip_file_name = tempfile.mkstemp()[1]
    shutil.make_archive(zip_file_name, 'zip', tmp_repo_dir)

    # Unzip the repository into a temporary directory
    tmp_dest_dir = tempfile

# Generated at 2022-06-13 18:57:20.069202
# Unit test for function unzip
def test_unzip():
    import shutil
    
    try:
        unzip('https://github.com/audreyr/cookiecutter-pypackage/zipball/master', 
            is_url=True)
        unzip('/tmp/cookiecutter-pypackage-master.zip', 
            is_url=False)
    except:
        print('unzip failed')
        return False
    
    return True

if __name__ == '__main__':
    print(test_unzip())

# Generated at 2022-06-13 18:59:06.954204
# Unit test for function unzip
def test_unzip():
    try:
        unzip('http://github.com/audreyr/cookiecutter-pypackage/archive/master.zip', True)
    except ValueError:
        return True
    else:
        return False

# Generated at 2022-06-13 18:59:16.241302
# Unit test for function unzip
def test_unzip():
    # Test in a directory with no write access
    try:
        clone_to_dir = '/root'
        make_sure_path_exists(clone_to_dir)
        unzip_path = unzip('tests/files/test-repo.zip', False, clone_to_dir)    
    except BaseException as e:
        assert type(e) == IOError
        assert e.strerror == 'Permission denied'
        assert e.filename == '/root'
    else:
        assert False
    # Test in a valid directory
    clone_to_dir = '.'
    unzip_path = unzip('tests/files/test-repo.zip', False, clone_to_dir)

# Generated at 2022-06-13 18:59:27.494016
# Unit test for function unzip
def test_unzip():
    import shutil
    import sys
    try:
        import unittest
        import unittest.mock as mock
        from unittest import skipIf
        from unittest.mock import patch
    except ImportError:
        import mock
        from mock import patch
        import unittest
        from unittest import skipIf
    from tempfile import mkdtemp

    from cookiecutter.utils import rmtree

    class TestUnzip(unittest.TestCase):

        @classmethod
        def setUpClass(cls):
            pass

        def tearDown(self):
            rmtree(self.temp_dir)


# Generated at 2022-06-13 18:59:32.609325
# Unit test for function unzip
def test_unzip():
    assert unzip('../templates/example-repo-cookiecutter-master.zip', is_url=False)
    assert unzip('https://github.com/chuckbutler/example-repo-cookiecutter/archive/master.zip', is_url=True)
    assert unzip('https://github.com/chuckbutler/example-repo-cookiecutter/archive/master.zip', is_url=True, clone_to_dir='/tmp')

# Generated at 2022-06-13 18:59:38.066180
# Unit test for function unzip
def test_unzip():
    """
    Test the function unzip
    """
    import pytest
    import shutil
    import tempfile
    import zipfile
    
    tempdir = tempfile.mkdtemp()
    

# Generated at 2022-06-13 18:59:42.384290
# Unit test for function unzip
def test_unzip():
    unzip('~/cookiecutter-repo/cookiecutter-pypackage.zip',
          is_url=False,
          clone_to_dir='~/cookiecutter-repo',
          no_input=True,
          password='password')

# Generated at 2022-06-13 18:59:52.800664
# Unit test for function unzip
def test_unzip():
    from mock import patch
    from .utils import make_zip_repo
    from .utils import clone_repo
    from .utils import rmtree

    with make_zip_repo() as zip_repo:
        with patch.object(cookiecutter.prompt, 'read_user_yes_no') as read_user_yes_no:
            with patch.object(cookiecutter.prompt, 'read_repo_password') as read_repo_password:
                read_user_yes_no.return_value = True
                read_repo_password.return_value = ''
                clone_to_dir = tempfile.mkdtemp()
                unzip_path = unzip(zip_repo, is_url=False, clone_to_dir=clone_to_dir)
                clone = clone_repo