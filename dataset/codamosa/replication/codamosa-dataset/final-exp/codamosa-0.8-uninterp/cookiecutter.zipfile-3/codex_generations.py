

# Generated at 2022-06-13 18:49:59.610039
# Unit test for function unzip
def test_unzip():
    assert unzip is not None

# Generated at 2022-06-13 18:50:03.199128
# Unit test for function unzip
def test_unzip():
    assert unzip('https://github.com/audreyr/cookiecutter-pypackage/archive/master.zip', True)
    assert unzip('https://github.com/audreyr/cookiecutter-pypackage/archive/master.zip', True)

# Generated at 2022-06-13 18:50:03.871533
# Unit test for function unzip
def test_unzip():
    pass

# Generated at 2022-06-13 18:50:13.965252
# Unit test for function unzip
def test_unzip():
    import pytest
    import os
    import os.path
    import shutil
    import subprocess
    import sys
    import tempfile
    import time
    import zipfile
    import zipimport
    from cookiecutter.utils import make_sure_path_exists
    from cookiecutter.utils import rmtree


    from cookiecutter.utils import unzip

    def zip_archive_factory(root_path, archive_path, test_file_name, password=None):
        zip_file = zipfile.ZipFile(archive_path, 'w', zipfile.ZIP_DEFLATED)
        for root, _, files in os.walk(root_path):
            for filename in files:
                filepath = os.path.join(root, filename)

# Generated at 2022-06-13 18:50:23.846077
# Unit test for function unzip
def test_unzip():
    import logging
    import shutil
    import time
    import tempfile
    import zipfile

    logger = logging.getLogger(__name__)

    logger.debug('Starting unzip function unit test...')
    

# Generated at 2022-06-13 18:50:35.726286
# Unit test for function unzip
def test_unzip():
    from io import BytesIO
    from io import StringIO
    from zipfile import ZipFile
    from zipfile import ZIP_DEFLATED

    # Create a temp file-like object to use as the zip archive
    data = BytesIO()
    zip_file = ZipFile(data, mode='w', compression=ZIP_DEFLATED)

    # Add a single file, with a text content 'Hello, world!'
    filename = 'test_file'
    content = 'Hello, world!'

    zip_info = zip_file.getinfo(filename)
    zip_info.filename = filename.encode('utf-8')
    zip_info.external_attr = 0o600 << 16
    zip_file.writestr(zip_info, content.encode('utf-8'))

    # Close the zip file
    zip_file

# Generated at 2022-06-13 18:50:42.809962
# Unit test for function unzip
def test_unzip():
    import shutil
    import zipfile
    #create test repo zipfile
    file_name = 'test_repo.zip'
    zf = zipfile.ZipFile(file_name, mode='w')
    zf.writestr('cookiecutter.json', '{"foo": "bar"}')
    zf.writestr('README.md', 'Test repo with cookiecutter.json')
    zf.close()

    #clone to directory
    clone_to_dir = '.'
    unzip_path = unzip(zip_uri=file_name, is_url=False, clone_to_dir=clone_to_dir)

    #check that cookiecutter.json exists
    assert os.path.isfile(os.path.join(unzip_path, 'cookiecutter.json'))

    #

# Generated at 2022-06-13 18:50:50.851441
# Unit test for function unzip
def test_unzip():
    # Test an open zip repository
    test_repo = unzip('https://github.com/audreyr/cookiecutter-pypackage/archive/master.zip',
                      is_url=True, clone_to_dir='/tmp/cookiecutter-master.zip')

    assert os.path.basename(test_repo) == 'cookiecutter-pypackage-master'

    # Test a password-protected zip repository
    test_repo = unzip('https://github.com/audreyr/cookiecutter-pypackage/archive/test.zip',
                      is_url=True, clone_to_dir='/tmp/cookiecutter-password.zip',
                      password='password')
    assert os.path.basename(test_repo) == 'cookiecutter-pypackage-test'

# Generated at 2022-06-13 18:50:57.445316
# Unit test for function unzip
def test_unzip():
    from cookiecutter.utils import rmtree
    from cookiecutter import config
    from cookiecutter.main import cookiecutter

    # Download and unpack a password-protected repository
    password = 'password'
    zip_uri = 'https://bitbucket.org/audreyr/cookiecutter-pypackage-encrypt/get/master.zip'
    repo_dir = cookiecutter(zip_uri, extra_context={}, no_input=True, password=password)
    assert os.path.exists(repo_dir)
    assert os.path.exists(os.path.join(repo_dir, 'setup.py'))
    rmtree(repo_dir)

    # Now unpack a valid repository

# Generated at 2022-06-13 18:51:01.718923
# Unit test for function unzip
def test_unzip():
    unzip('https://github.com/audreyr/cookiecutter-pypackage/zipball/master', True)
    unzip('https://github.com/audreyr/cookiecutter-pypackage/archive/master.zip', True)
    unzip('https://github.com/audreyr/cookiecutter-pypackage/archive/master.zip', False)
    # unzip('https://github.com/audreyr/cookiecutter-pypackage/archive/master.zip', False, '.')

# Generated at 2022-06-13 18:51:18.932412
# Unit test for function unzip
def test_unzip():
    """Check unzip function."""
    import shutil
    import tempfile
    import zipfile

    # create zip file
    test_zip_file = os.path.join(tempfile.mkdtemp(), 'test_unzip.zip')
    test_dir = os.path.join(tempfile.mkdtemp(), 'test_dir')
    test_dir_content = os.path.join(test_dir, 'test_content.txt')
    os.mkdir(test_dir)
    with open(test_dir_content, 'w') as content_file:
        content_file.write("test_content")

    file_list = [test_dir_content]
    zip_obj = zipfile.ZipFile(test_zip_file, 'w')
    for file_name in file_list:
        zip_obj

# Generated at 2022-06-13 18:51:25.735401
# Unit test for function unzip
def test_unzip():
    """
    Simple test to ensure the function unzip is working.
    """
    import shutil

# Generated at 2022-06-13 18:51:35.420279
# Unit test for function unzip
def test_unzip():
    import shutil

    # zip file url for unit test
    url = 'https://codeload.github.com/stiivi/valid-zip-repo/zip/master'

    # create tmp dir
    tmp_dir = tempfile.mkdtemp()

    # create unit test zip
    unzip_path = unzip(url, True, tmp_dir)

    # check unit test zip
    assert os.path.exists(unzip_path)
    assert os.path.isdir(unzip_path)

    # delete tmp dirs
    shutil.rmtree(unzip_path)
    shutil.rmtree(tmp_dir)

# Generated at 2022-06-13 18:51:49.128289
# Unit test for function unzip
def test_unzip():
    import os
    import shutil
    from cookiecutter.exceptions import InvalidZipRepository
    from cookiecutter import utils
    utils.make_sure_path_exists = lambda path: None

    # Create the repository to be zipped
    base_dir = os.getcwd()
    source_dir = os.path.join(base_dir, 'tests', 'test-unzip')
    shutil.copytree(source_dir, os.path.join(base_dir, 'tests', 'test-repo'))

    zip_file = os.path.join(base_dir, 'tests', 'test-repo.zip')
    os.chdir('tests')
    shutil.make_archive('test-repo', 'zip', 'test-repo')
    os.chdir(base_dir)


# Generated at 2022-06-13 18:51:56.157692
# Unit test for function unzip
def test_unzip():
    """Test getting a repo from zip archive."""
    import pytest

    from cookiecutter.main import cookiecutter

    args = {
        'extra_context': {
            'full_name': 'Test User',
            'email': 'test@example.com',
            'github_username': 'audreyr'
        },
        'no_input': True,
        'replay': False,
        'overwrite_if_exists': False,
        'output_dir': '.'
    }

    with pytest.raises(InvalidZipRepository) as excinfo:
        cookiecutter(
            'unittest_template', zip_repo='https://github.com/audreyr/cookiecutter-pypackage/zipball/master',
            **args
        )

# Generated at 2022-06-13 18:51:59.364461
# Unit test for function unzip

# Generated at 2022-06-13 18:52:09.923135
# Unit test for function unzip
def test_unzip():
    """ Test function unzip """
    import shutil
    import tempfile
    import zipfile
    from os.path import join

    # Test empty repository
    with tempfile.TemporaryDirectory() as tmp_dir:
        # Create empty archive
        zip_path = join(tmp_dir, 'empty.zip')
        with zipfile.ZipFile(zip_path, mode='w') as zf:
            pass

        # Verify exception when empty archive is unpacked
        try:
            unzip(zip_path, is_url=False)
        except InvalidZipRepository:
            pass
        else:
            assert False # unzip did not raise exception InvalidZipRepository

    # Test archive without top level directory

# Generated at 2022-06-13 18:52:17.928850
# Unit test for function unzip
def test_unzip():
    import shutil
    # test unzip function
    unzip('https://github.com/jef-spaleta/python-cookiecutter-alembic/archive/master.zip', True, clone_to_dir='.', no_input=False, password=None)
    result_name = os.path.expanduser('./master.zip')
    assert os.path.isfile(result_name)

    # test unzip function
    test_path = os.path.expanduser('~/test')
    unzip(result_name, False, clone_to_dir=test_path, no_input=False, password=None)
    assert os.path.isdir(test_path)

    shutil.rmtree(test_path)
    os.remove(result_name)

# Generated at 2022-06-13 18:52:27.969302
# Unit test for function unzip
def test_unzip():
    import contextlib
    import mock
    import shutil
    import sys
    from io import BytesIO
    from io import StringIO
    import unittest

    _open_patch = mock.patch('zipfile.ZipFile.open')
    _file_patch = mock.patch('io.open', create=True)

    @contextlib.contextmanager
    def tempdir():
        dirpath = tempfile.mkdtemp()
        try:
            yield dirpath
        finally:
            shutil.rmtree(dirpath)

    @contextlib.contextmanager
    def mock_stdout():
        _stdout = sys.stdout
        fake_stdout = StringIO()
        sys.stdout = fake_stdout
        try:
            yield fake_stdout
        finally:
            sys.stdout = _stdout

# Generated at 2022-06-13 18:52:28.760045
# Unit test for function unzip
def test_unzip():
    pass

# Generated at 2022-06-13 18:52:44.974509
# Unit test for function unzip
def test_unzip():
    import tempfile, os, shutil
    import zipfile

# Generated at 2022-06-13 18:52:48.502612
# Unit test for function unzip
def test_unzip():
    pass
    # TODO: unzip unit tests
    # # Test 1: zip is empty
    # # Test 2: zip does not include a top-level directory
    # # Test 3: zip is password protected
    # # Test 4: zip is not a valid zip archive

# Generated at 2022-06-13 18:52:59.851621
# Unit test for function unzip
def test_unzip():
    import zipfile
    zip_url = 'https://codeload.github.com/audreyr/cookiecutter-pypackage/zip/master'
    # Build the name of the cached zipfile,
    # and prompt to delete if it already exists.
    identifier = zip_url.rsplit('/', 1)[1]
    zip_path = "cookiecutter-pypackage-master.zip" #os.path.join(clone_to_dir, identifier)

    # (Re) download the zipfile
    r = requests.get(zip_url, stream=True)
    with open(zip_path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)


# Generated at 2022-06-13 18:53:04.453010
# Unit test for function unzip
def test_unzip():
    assert unzip('tests/test_unzip', False, no_input=True) == 'tests/test_unzip/cookiecutter-pypackage'
    assert unzip('https://github.com/audreyr/cookiecutter-pypackage/archive/master.zip', True, no_input=True) == 'cookiecutter-pypackage-master'

# Generated at 2022-06-13 18:53:15.189323
# Unit test for function unzip
def test_unzip():
    import pytest
    import shutil
    import time
    # Ignore PyTest Warning: Function and class names must be valid Python identifiers
    # pylint: disable=C0103
    # Create empty zip file
    test_file_uri = tempfile.mkdtemp()
    test_uri = os.path.join(test_file_uri, 'test.zip')
    test_zip = ZipFile(test_uri, 'w')
    test_zip.close()
    try:
        assert unzip(test_uri, False)
    except InvalidZipRepository:
        pass
    except Exception:
        pytest.fail('unzip() raised ExceptionType unexpectedly!')

    # Create zip files
    test_dir = os.path.join(test_file_uri, 'test_dir')
    os.mkdir(test_dir)

# Generated at 2022-06-13 18:53:15.700112
# Unit test for function unzip
def test_unzip():
    pass

# Generated at 2022-06-13 18:53:23.109544
# Unit test for function unzip
def test_unzip():
    import os, shutil
    password = 'Cookie123'
    pass_dir = os.path.join(os.path.dirname(__file__), 'password-zip')

    try:
        shutil.rmtree(os.path.join(pass_dir, 'unzip'))
    except OSError:
        pass
    unzip_path = unzip(pass_dir, False, password=password)
    assert os.path.exists(os.path.join(unzip_path, 'password-zip', 'pass.txt'))

# Generated at 2022-06-13 18:53:35.372963
# Unit test for function unzip
def test_unzip():
    """Test of unzip"""
    import shutil
    import subprocess
    import sys

    if sys.version_info < (3, 4):
        return

    # Create a temporary directory for tests
    tmp = tempfile.mkdtemp()
    clone_to_dir = os.path.join(tmp, 'clone_dir')
    os.makedirs(clone_to_dir)

    # Create a password protected zip repository
    repo_name = "test-repo"
    repo_dir = os.path.join(tmp, repo_name)
    os.makedirs(repo_dir)
    repo_file = os.path.join(repo_dir, '{}.zip'.format(repo_name))

# Generated at 2022-06-13 18:53:39.098554
# Unit test for function unzip
def test_unzip():
    zip_file = os.path.abspath(__file__)
    unzip(zip_file, False)

# Generated at 2022-06-13 18:53:48.998871
# Unit test for function unzip
def test_unzip():
    # determine the location of the test zip
    this_directory = os.path.dirname(os.path.abspath(__file__))
    test_zip = os.path.join(this_directory, 'testing', 'test-repo.zip')

    # check that the test zip exists
    assert os.path.exists(test_zip)

    # check that a BadZipFile exception is raised for the empty zip
    empty_zip = os.path.join(this_directory, 'testing', 'empty.zip')
    assert not os.path.exists(empty_zip)

    # run the tests
    # Unzip a zip URI
    unzip(test_zip, False)
    # Unzip a zip URL without a password

# Generated at 2022-06-13 18:54:17.505649
# Unit test for function unzip
def test_unzip():
    #prepare local path for zip file
    clone_to_dir = tempfile.mkdtemp()

    #create a temporary zip file with a single file
    with tempfile.NamedTemporaryFile(suffix='.zip', delete=False) as test_zip:
        with ZipFile(test_zip.name, 'w') as zf:
            zf.writestr('test/file.txt', b'')

    #unpack zip and delete temp file

# Generated at 2022-06-13 18:54:31.906751
# Unit test for function unzip
def test_unzip():
    # Prepare test data
    zip_repo_path = 'tests/test-repos/zip-repo'
    zip_repo_url = (
        'http://github.com/audreyr/cookiecutter-pypackage/zipball/master'
    )
    zip_repo_protected_path = 'tests/test-repos/zip-repo-protected/protected-repo.zip'
    zip_repo_protected_url = (
        'https://github.com/makiolo/cookiecutter-pypackage/zipball/master'
    )
    zip_repo_password = '123456'
    clone_to_dir = tempfile.mkdtemp()

    # Test zip file in local

# Generated at 2022-06-13 18:54:40.085968
# Unit test for function unzip
def test_unzip():
    """Unit testing for the unzip() function."""
    # Create a temporary directory to hold the unzipped archive,
    # and a temporary zipfile
    unzip_base = tempfile.mkdtemp()
    temp_zip = tempfile.NamedTemporaryFile()
    temp_zip.close()

    # Create a zip archive with a test file
    with ZipFile(temp_zip.name, 'a') as myzip:
        myzip.writestr('test.txt', 'This is a test')

    # Unzip the file
    unzip_path = unzip(temp_zip.name, False, unzip_base)

    # Check that the file was unzipped as expected
    assert os.path.exists(os.path.join(unzip_base, 'test.txt'))

    # Clean up
    shut

# Generated at 2022-06-13 18:54:46.415973
# Unit test for function unzip
def test_unzip():
    print('Testing unzip function')
    is_url = True
    clone_to_dir = '.'
    no_input = True
    assert unzip('https://github.com/audreyr/cookiecutter-pypackage/archive/master.zip', is_url, clone_to_dir, no_input)

# Generated at 2022-06-13 18:54:47.066297
# Unit test for function unzip
def test_unzip():
    from cookiecutter.tests.test_repo import mock_github_api
    pass

# Generated at 2022-06-13 18:54:47.735026
# Unit test for function unzip
def test_unzip():  # pragma: no cover
        unzip()

# Generated at 2022-06-13 18:54:52.740987
# Unit test for function unzip
def test_unzip():
    ## remove when refactor is done
    import os
    os.chdir('/home/travis/build/audreyr/cookiecutter/tests')
    os.chdir('/home/travis/build/audreyr/cookiecutter/tests'/home/travis/build/audreyr/cookiecutter/tests)
    print(os.listdir('.'))
    assert os.listdir('../tests/fake-repo-tmpl') == os.listdir(
        unzip('../tests/fake-repo-tmpl.zip', False)
    )

# Generated at 2022-06-13 18:54:59.254028
# Unit test for function unzip
def test_unzip():
    """Tests the unzip function for the default case of a zipfile
    """
    from . import tests_dir
    import shutil

    zip_path = os.path.join(tests_dir, 'fake-repo-tmpl', 'fake-repo.zip')
    clone_to_dir = os.path.join(tests_dir, 'fake-repo-tmpl')
    unzip_path = unzip(zip_path, False, clone_to_dir)
    test_path = os.path.join(tests_dir, 'fake-repo-tmpl', 'fake-repo')
    assert os.path.exists(test_path)
    # Cleanup the unzipped directory
    shutil.rmtree(unzip_path)

# Generated at 2022-06-13 18:55:09.586241
# Unit test for function unzip
def test_unzip():
    """test unzip function"""

    import shutil

    # Define a test definition
    test_def = {
        "template_path": "https://github.com/cookiecutter-test/test_template/archive/master.zip",
        "no_input": True,
    }

    unzip_path = unzip(**test_def)
    shutil.rmtree(unzip_path)
    assert os.path.isdir(unzip_path)

    # Test that a protected archive raises an error
    test_def["template_path"] = "https://github.com/cookiecutter-test/test_protected/archive/master.zip"

# Generated at 2022-06-13 18:55:19.386214
# Unit test for function unzip
def test_unzip():
    """
    Assert that the function unzip correct extracts files.
    """

    # Arrange
    import shutil
    import tarfile
    import tempfile

    # Create the directory for the test archive
    working_path = tempfile.mkdtemp()
    test_path = os.path.join(working_path, "test")

    # Create test files
    file_a = os.path.join(test_path, "a.txt")
    file_b = os.path.join(test_path, "b.txt")
    file_c = os.path.join(test_path, "c.txt")

    # Create the test archive
    os.mkdir(test_path)
    with open(file_a, "w") as f:
        f.write("file a")

# Generated at 2022-06-13 18:55:53.924522
# Unit test for function unzip
def test_unzip():
    assert unzip('test/test-repo.zip', is_url=False) == '/tmp/tmpr-kwrpl_'

# Generated at 2022-06-13 18:56:02.153447
# Unit test for function unzip
def test_unzip():
    from multiprocessing import Process
    import time
    import shutil
    from urllib.parse import urlparse
    from http.server import HTTPServer
    from socketserver import ThreadingMixIn
    from http.server import SimpleHTTPRequestHandler
    from cookiecutter.main import cookiecutter
    from cookiecutter import utils

    class MultiThreadingHTTPServer(ThreadingMixIn, HTTPServer):
        pass

    # Start test http server and wait 5s
    def start_http_server(server_url):
        handler = SimpleHTTPRequestHandler
        httpd = MultiThreadingHTTPServer(('localhost', 8080), handler)
        server_url = ''.join(['http://localhost:8080', server_url])
        httpd.serve_forever()
        return server_url


# Generated at 2022-06-13 18:56:12.082672
# Unit test for function unzip
def test_unzip():
    """Tests that unzip correctly raises BadZipFile on a non-zip file."""
    import subprocess
    import shutil

    # Build the repository path
    dir_path = os.path.dirname(os.path.realpath(__file__))
    test_dir = os.path.join(dir_path, '..', 'tests')
    repo_dir = os.path.join(test_dir, 'test-repo-pre')
    repo_file = os.path.join(test_dir, 'test-pre-norepo.zip')

    # Check that the test file does not currently exist
    assert not os.path.exists(repo_file)

    # Create the zipfile
    subprocess.check_call(['zip', '-q', '-r', repo_file, repo_dir])

   

# Generated at 2022-06-13 18:56:12.827557
# Unit test for function unzip
def test_unzip():
    assert 'User1' in unzip('User1.zip', False)

# Generated at 2022-06-13 18:56:19.255799
# Unit test for function unzip
def test_unzip():
    # First, create a temporary zip file
    import string
    import random

    unzip_path = tempfile.mkdtemp()
    zip_path = os.path.join(unzip_path, 'test_repo.zip')

    # We're going to create a directory, place a file inside and then zip it
    base_dir = tempfile.mkdtemp()
    test_dir = os.path.join(base_dir, 'test_dir')
    make_sure_path_exists(test_dir)
    with open(os.path.join(test_dir, 'test_file.txt'), 'w') as f:
        pass

    with ZipFile(zip_path, 'w') as zipping:
        zipping.write(test_dir)

    # Now, test that the zip file has been created and unzip

# Generated at 2022-06-13 18:56:21.498473
# Unit test for function unzip
def test_unzip():
    """
    Test the unzip function for valid and invalid zip files
    """
    unzip('cookiecutter-pypackage/tests/test-repo-tmpl.zip', project_name='test-repo-tmpl')
    with pytest.raises(InvalidZipRepository):
        unzip('cookiecutter-pypackage/tests/test-repo-tmpl_bad.zip', project_name='test-repo-tmpl')

# Generated at 2022-06-13 18:56:22.651982
# Unit test for function unzip
def test_unzip():
    # TODO: test failing URL and not existing ZIP file (invalid URI)
    pass

# Generated at 2022-06-13 18:56:23.153116
# Unit test for function unzip
def test_unzip():
    pass

# Generated at 2022-06-13 18:56:30.651554
# Unit test for function unzip
def test_unzip():
    import pytest
    from os.path import isdir
    from . import unzip
    from requests import get

    test_dir = 'tests/test-data/'
    unzip_dir = unzip.unzip(
        test_dir + 'test-cookiecutter.zip',
        is_url=False,
        clone_to_dir=test_dir,
        no_input=True
    )
    assert isdir(unzip_dir)
    assert isdir(unzip_dir + '/{{cookiecutter.repo_name}}')


# Generated at 2022-06-13 18:56:41.101690
# Unit test for function unzip
def test_unzip():
    # Test passing of invalid zip file to unzip
    try:
        unzip(zip_uri='', is_url=False, clone_to_dir='.', no_input=False, password=None)
    except InvalidZipRepository:
        print('InvalidZipRepository exception caught')
    # Test unzipping of verilog files
    unzip_path = unzip(
        zip_uri='https://github.com/mahesh-bhatta/VLSI_Mini_Project/archive/master.zip',
        is_url=True,
        clone_to_dir='.',
        no_input=False,
        password=None)
    print(unzip_path)

# Generated at 2022-06-13 18:57:45.693810
# Unit test for function unzip
def test_unzip():
    zip_uri = 'https://github.com/audreyr/cookiecutter-pypackage/archive/master.zip'
    is_url = True
    clone_to_dir = '.'
    no_input = True
    password = None
    unzip(zip_uri, is_url, clone_to_dir, no_input, password)

if __name__ == '__main__':
    test_unzip()

# Generated at 2022-06-13 18:57:58.484833
# Unit test for function unzip
def test_unzip():
    """テスト用"""
    from urllib.request import urlopen
    from zipfile import is_zipfile

    # githubからzipをダウンロードして検証する
    zip_uri = 'https://github.com/matthewwithanm/cookiecutter-pypackage-minimal/archive/master.zip'
    is_url = True
    unzip_path = unzip(zip_uri, is_url)
    assert os.path.exists(unzip_path)

    # zipファイルがダウンロードされているか
    # zipファイルが空ではないこと
    identifier = zip_uri.rsplit('/', 1)[1]

# Generated at 2022-06-13 18:58:04.492975
# Unit test for function unzip
def test_unzip():
    """Testing functionality of unzip function."""
    import shutil
    from git import Repo

    # Download a git repo
    test_dir = tempfile.mkdtemp()
    test_repo = 'https://github.com/audreyr/cookiecutter-pypackage.git'
    Repo.clone_from(test_repo, test_dir)

    # Convert the git repo to a zip file
    zip_file = shutil.make_archive(base_name=test_dir, format='zip', root_dir=test_dir)
    zip_file = zip_file.split('.')[0] + '.zip'

    # Extract zip file
    unzip(zip_uri=zip_file, is_url=False, clone_to_dir=test_dir)

    # We don't need to check the name

# Generated at 2022-06-13 18:58:05.098080
# Unit test for function unzip
def test_unzip():
    pass

# Generated at 2022-06-13 18:58:06.909440
# Unit test for function unzip
def test_unzip():
    unzip('test/test-repo.zip',False)
    unzip('test/test-repo.zip',False,'test/',False,'password')

# Generated at 2022-06-13 18:58:16.595464
# Unit test for function unzip
def test_unzip():

    # Postive test
    zip_uri = 'http://www.decalage.info/files/zipfile_py3k.zip'
    is_url = True
    clone_to_dir = '.'
    no_input = True
    password = None
    unzip_path = unzip(zip_uri, is_url, clone_to_dir, no_input, password)
    print(unzip_path)
    # Negative test
    # No such file or directory
    zip_uri = 'No such file or directory'
    is_url = False
    clone_to_dir = '.'
    no_input = True
    password = None
    unzip_path = unzip(zip_uri, is_url, clone_to_dir, no_input, password)
    print(unzip_path)

    # Negative

# Generated at 2022-06-13 18:58:24.959987
# Unit test for function unzip
def test_unzip():
    import shutil
    import pytest
    import requests
    from cookiecutter.exceptions import InvalidZipRepository

    from .utils import TestCase

    clone_to_dir = '.'
    download = False
    is_url = True

    # Ensure that clone_to_dir exists
    clone_to_dir = os.path.expanduser(clone_to_dir)

    # Build the name of the cached zipfile,
    # and prompt to delete if it already exists.
    download = True

    identifier = 'https://github.com/audreyr/cookiecutter-pypackage/archive/master.zip'
    zip_path = os.path.join(clone_to_dir, identifier.rsplit('/', 1)[1])

    # (Re) download the zipfile

# Generated at 2022-06-13 18:58:25.614347
# Unit test for function unzip
def test_unzip():
    pass

# Generated at 2022-06-13 18:58:29.066269
# Unit test for function unzip
def test_unzip():
    """Test that unzip works with a GitHub file."""
    url = 'https://github.com/audreyr/cookiecutter-pypackage/archive/master.zip'
    unzip(url, True, clone_to_dir='tests/fake-repo-templates')

# Generated at 2022-06-13 18:58:34.664175
# Unit test for function unzip
def test_unzip():
    test_zip = "https://github.com/audreyr/cookiecutter-pypackage/archive/master.zip"
    test_zip_path = "/tmp/cookiecutter_test_unzip_master.zip"
    test_zip_dir = "/tmp/cookiecutter-master/"
    import shutil
    assert not os.path.exists(test_zip_path)
    assert not os.path.exists(test_zip_dir)
    unzip(test_zip, is_url=True, clone_to_dir='/tmp')
    assert os.path.exists(test_zip_path)
    assert os.path.exists(test_zip_dir)
    shutil.rmtree(test_zip_dir)
    os.remove(test_zip_path)


# Unit test