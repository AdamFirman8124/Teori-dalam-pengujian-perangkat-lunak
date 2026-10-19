

# Generated at 2022-06-13 18:50:04.562660
# Unit test for function unzip
def test_unzip():
    """
    Just a simple assertion.
    :raises: AssertionError: if the test doesn't pass
    """
    assert unzip("test",True) == "test"

# Generated at 2022-06-13 18:50:14.177135
# Unit test for function unzip
def test_unzip():
    # Import unzip for unit tests
    from cookiecutter.utils.unzip import unzip
    from pyfakefs.fake_filesystem_unittest import TestCase
    from tempfile import TemporaryDirectory

    class TestUnzip(TestCase):

        def setUp(self):
            self.setUpPyfakefs()
            self.zip_path = self.make_path('/test.zip')
            self.temp_path = TemporaryDirectory()
            self.clone_to_dir = self.make_path('/fake_dir')

        def tearDown(self):
            self.tearDownPyfakefs()
            self.temp_path.cleanup()

        def test_unzip(self):
            # Create fake zipfile
            with ZipFile(self.zip_path, 'w') as archive:
                archive.writestr

# Generated at 2022-06-13 18:50:24.016884
# Unit test for function unzip

# Generated at 2022-06-13 18:50:35.812327
# Unit test for function unzip
def test_unzip():
    from tempfile import mkdtemp
    import shutil
    from zipfile import ZipFile
    from time import time

    # Write a zip file to a temporary directory
    tmp_dir = mkdtemp()
    zip_name = os.path.join(tmp_dir, "test_zip-" + str(int(time())) + ".zip")
    with ZipFile(zip_name, 'w') as zip_file:
        zip_file.writestr("test_file.txt", "This is the zip file.")

    unzip_dir = unzip(zip_name, False)
    unzip_path = os.path.join(unzip_dir, "test_file.txt")

    # Clean up
    shutil.rmtree(tmp_dir)
    shutil.rmtree(unzip_dir)

    # Conf

# Generated at 2022-06-13 18:50:42.818180
# Unit test for function unzip
def test_unzip():
    # Test that unzip raises an error when the zipfile is bad
    from cookiecutter import utils
    from cookiecutter.config import DEFAULT_CONFIG

    class FakeZipFile(object):
        def __init__(self, raises=False):
            self.namelist = []
            self.raises = raises

        def extractall(self, *args, **kwargs):
            if self.raises:
                raise RuntimeError()
            self.namelist = kwargs['path']

    bad_zip_file = FakeZipFile(raises=True)
    good_zip_file = FakeZipFile(raises=False)

    assert os.path.exists(DEFAULT_CONFIG['cookiecutters_dir'])

    # Test that unzip raises an error when the zipfile is bad

# Generated at 2022-06-13 18:50:45.125725
# Unit test for function unzip
def test_unzip():
    unzip('https://github.com/audreyr/cookiecutter-pypackage/archive/master.zip', True)

# Generated at 2022-06-13 18:50:50.784977
# Unit test for function unzip
def test_unzip():
    import shutil

    # Assert that we can unzip a repository
    tempdir = tempfile.mkdtemp()

    try:
        unzip_dir = unzip(
            'https://github.com/hackebrot/cookiecutter-pypackage/archive/master.zip',
            True,
            clone_to_dir=tempdir,
        )
        assert unzip_dir == os.path.join(tempdir, 'cookiecutter-pypackage-master')

        assert os.path.exists(unzip_dir)
    finally:
        shutil.rmtree(tempdir)

# Generated at 2022-06-13 18:51:03.322752
# Unit test for function unzip
def test_unzip():
    from .utils import get_project
    from .config import get_user_config
    from .main import expand_abbreviations
    from .generate import generate_context
    from .replay import dump, load
    from .exceptions import InvalidZipRepository

    my_config = get_user_config()
    no_input = my_config.get('no_input', False)

    # Get project_dir
    repo_dir, cleanup_repo_dir = get_project('tests/test-repo-pre/', my_config)
    assert repo_dir is not None

    # Get template_name
    project_dir = 'tests/fake-repo-tmpl/'
    repo_dir, cleanup_repo_dir = get_project(project_dir, my_config)
    assert repo_dir is not None



# Generated at 2022-06-13 18:51:08.050806
# Unit test for function unzip
def test_unzip():
    unzip('xxx', True, clone_to_dir='.', no_input=False, password=None)
    unzip('https://github.com/pytest-dev/pytest-cov/archive/2.2.1.zip', True, clone_to_dir='.', no_input=False, password=None)
    unzip('https://github.com/pytest-dev/pytest-cov/archive/2.2.1.zip', False, clone_to_dir='.', no_input=False, password=None)
    unzip('https://github.com/pytest-dev/pytest-cov/archive/2.2.1.zip', False, clone_to_dir='.', no_input=True, password=None)

# Generated at 2022-06-13 18:51:16.442977
# Unit test for function unzip
def test_unzip():
    tempdir = tempfile.mkdtemp()
    try:
        unzip_file = unzip('tests/files/test-repo.zip', is_url=False, clone_to_dir=tempdir)
        assert os.path.isdir(unzip_file)
        assert os.path.isfile(os.path.join(unzip_file, 'README.md'))
    except InvalidZipRepository as e:
        assert False, 'unzip raised InvalidZipRepository unexpectedly: {}'.format(e)
    finally:
        os.rmdir(tempdir)

# Generated at 2022-06-13 18:51:56.456992
# Unit test for function unzip
def test_unzip():
    import os
    import shutil
    from cookiecutter.config import DEFAULT_DIRECTORY
    from cookiecutter.utils import rmtree
    from cookiecutter.utils.tests import patch_fake_github_api
    from .utils import is_dir, temp_dir

    repo_dir = 'tests/test-repo/{{cookiecutter.repo_name}}'

    with temp_dir() as clone_to_dir:
        with patch_fake_github_api(repo_dir) as zip_url:
            unzip_path = unzip(
                zip_url, is_url=True, clone_to_dir=clone_to_dir, no_input=True
            )

        # Work in a temporary directory

# Generated at 2022-06-13 18:51:57.215542
# Unit test for function unzip
def test_unzip():
    pass

# Generated at 2022-06-13 18:52:07.914876
# Unit test for function unzip
def test_unzip():
    import shutil

    # Testing function on a test zipfile.
    # A .zip file, which contains only a top-level folder
    # with a file called "cookiecutter.json".
    # Download test_zipfile.zip to /tmp/.
    raw_url = 'http://raw.github.com/audreyr/cookiecutter/master/tests/test-repo.zip'
    r = requests.get(raw_url, stream=True)

    temp_dir = tempfile.mkdtemp()
    zip_path = os.path.join(temp_dir, 'test-repo.zip')
    with open(zip_path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write

# Generated at 2022-06-13 18:52:09.888711
# Unit test for function unzip
def test_unzip():
    """Test unzip function"""
    unzip('repo-name', True)



# Generated at 2022-06-13 18:52:17.905189
# Unit test for function unzip
def test_unzip():
    # url
    temp_dir = os.path.join(os.path.expanduser('~'), '.cookiecutters')
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    unzip("https://github.com/audreyr/cookiecutter-pypackage/archive/1.0.2.zip", True,
          clone_to_dir=temp_dir, no_input=True)
    assert os.path.exists(temp_dir)
    assert os.path.isfile(os.path.join(temp_dir, "cookiecutter-pypackage-1.0.2.zip"))

    zip_path = os.path.join(temp_dir, "cookiecutter-pypackage-1.0.2.zip")
   

# Generated at 2022-06-13 18:52:27.917574
# Unit test for function unzip
def test_unzip():
    import os
    import subprocess
    from cookiecutter.utils import rmtree

    # Create a temporary directory to store the zip file to download.
    # We want to test downloading and unzipping the zip file.
    clone_to_dir = tempfile.mkdtemp()

    # Build a zip file to download.
    # The zip file will contain just the directory 'hello_world'
    # which contains the file 'testfile'.
    zip_path = 'test_unzip.zip'
    subprocess.check_call(['zip', zip_path, 'hello_world/'])
    subprocess.check_call(['zip', '-j', zip_path, 'hello_world/testfile'])
    os.remove('hello_world/testfile')
    os.rmdir('hello_world')

    # We want

# Generated at 2022-06-13 18:52:32.884945
# Unit test for function unzip
def test_unzip():
    import shutil
    import requests
    import os
    import re
    import tempfile

    # Download the zip file
    url = 'https://github.com/jacebrowning/template-pack/archive/master.zip'
    r = requests.get(url, stream=True)

    # Create an archive file
    temp_dir = tempfile.mkdtemp()
    archive_file = os.path.join(temp_dir, 'master.zip')
    with open(archive_file, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)

    # Test the unzip function
    unzip_path = unzip(archive_file, False)


# Generated at 2022-06-13 18:52:35.529124
# Unit test for function unzip
def test_unzip():
    """Test function unzip with path
    """
    unzip('test/test-repo.zip', False, clone_to_dir='./test')


# Generated at 2022-06-13 18:52:43.335553
# Unit test for function unzip
def test_unzip():
    password = None
    url = 'https://github.com/wd/zip-test/archive/master.zip'
    is_url = True
    unzip(url, is_url)

    password = 'xxx'
    with open('test.zip', mode='wb') as f:
        f.write(password.encode('utf-8'))
    url = 'test.zip'
    is_url = False
    # UnsupportedPasswordScheme: non-empty end of central directory record
    # at the end of the archive
    try:
        unzip(url, is_url)
    except InvalidZipRepository:
        pass


# Generated at 2022-06-13 18:52:47.398260
# Unit test for function unzip
def test_unzip():
    assert unzip(
        os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..', 'repos', 'jinja', 'cookiecutter-jinja')
        ),
        is_url=False
    )



# Generated at 2022-06-13 18:53:19.654244
# Unit test for function unzip
def test_unzip():
    import shutil
    import tempfile
    import pytest
    import requests
    import os
    import pathlib
    def test_unzip_url():
        """Test that a zip file is correctly downloaded, unzipped, and can be
        deleted.
        """

        # build a test zip file
        test_zip_fod = tempfile.TemporaryDirectory()
        test_zip_path = os.path.join(test_zip_fod.name,'test_zip.zip')

        with open(test_zip_path, 'wb') as temp_zip_file:
            r = requests.get('https://github.com/sloria/cookiecutter-pypackage/archive/master.zip')
            temp_zip_file.write(r.content)

        # create temporary file to delete (pypi package archive)

# Generated at 2022-06-13 18:53:24.507504
# Unit test for function unzip
def test_unzip():
    filename = 'test.zip'
    zip_path = os.path.join(clone_to_dir, filename)
    zip_path = 'test.zip'
    url = 'https://github.com/audreyr/cookiecutter-pypackage/archive/master.zip'
    assert unzip(url, True) == os.path.join(unzip_base, project_name)

# Generated at 2022-06-13 18:53:36.034468
# Unit test for function unzip
def test_unzip():
    """Test the unzip function to check if it is able to extract the zip file"""
    import shutil
    import sys
    import tempfile
    
    def _get_delete_zip_path(zip_path):
        zip_path = os.path.abspath(zip_path)
        zip_dir = os.path.dirname(zip_path)
    
        # Does the zip file need to be created?
        if not os.path.exists(zip_path):
            # Create the zip file with only one file
            with ZipFile(zip_path, 'w') as zip_file:
                zip_file.writestr('test.txt', 'Some test content')
                zip_file.writestr('other.txt', 'More test content')
    
        return zip_dir
    

# Generated at 2022-06-13 18:53:47.282203
# Unit test for function unzip
def test_unzip():
    from cookiecutter.compat import is_windows
    from cookiecutter.main import cookiecutter

    template_path = cookiecutter(
        'tests/test-repo-pre/',
        no_input=True,
        extra_context={
            'full_name': 'Test Author',
            'email': 'author@example.com',
            'github_username': 'hackebrot',
            'project_name': 'Test Project',
            'project_slug': 'testproject',
            'project_short_description': 'The best project ever!',
            'pypi_username': 'user_name',
            'domain_name': 'example.org',
            'version': '0.1.0',
            'release': '0.1.0',
        },
    )


# Generated at 2022-06-13 18:53:58.069991
# Unit test for function unzip
def test_unzip():
    import shutil
    import requests
    import re
    import sys
    import os

    # Ensure that clone_to_dir exists
    clone_to_dir = "tmp"
    if os.path.exists(clone_to_dir):
        shutil.rmtree(clone_to_dir)
    os.mkdir(clone_to_dir)

    # Download zip file
    identifier = "jinja2-cookiecutter.zip"
    zip_path = os.path.join(clone_to_dir, identifier)
    url = "https://github.com/pytest-dev/cookiecutter-pytest-plugin/archive/master.zip"
    r = requests.get(url, stream=True)

# Generated at 2022-06-13 18:53:59.510721
# Unit test for function unzip
def test_unzip():
    pass


# Generated at 2022-06-13 18:54:11.070790
# Unit test for function unzip
def test_unzip():

    import os
    import shutil
    import tempfile

    from cookiecutter.utils import rmtree

    def setup_project_files():
        project_files = {
            'cookiecutter.json': '{"key": "value"}',
            'README.md': 'README',
            '{{ cookiecutter.key }}/file.py': 'content',
        }

        for path, content in project_files.items():
            path = os.path.join(temp_dir, path)
            folder = os.path.dirname(path)
            if not os.path.isdir(folder):
                os.makedirs(folder)
            with open(path, 'w') as f:
                f.write(content)

    def compare_project_files(unzipped):
        assert unzipped.endsw

# Generated at 2022-06-13 18:54:21.854121
# Unit test for function unzip
def test_unzip():
    import os
    import subprocess
    import tempfile
    import unittest
    import zipfile

    import requests_mock
    
    class TestUnzip(unittest.TestCase):

        def setUp(self):
            self.test_url = 'https://github.com/audreyr/cookiecutter-pypackage/archive/master.zip'
            self.zip_path = os.path.join(tempfile.mkdtemp(), 'test_master.zip')
            self.password = None
            self.is_url = False


# Generated at 2022-06-13 18:54:29.556668
# Unit test for function unzip
def test_unzip():
    # TODO: TEMP_DIR/unzip_path is still a hardcoded path, not that it matters;
    # this module needs more work.
    unzip_path = unzip(
        zip_uri='https://github.com/audreyr/cookiecutter-pypackage/archive/master.zip',
        is_url=True,
        clone_to_dir='TEMP_DIR',
        no_input=False,
        password=None
    )
    assert unzip_path == "TEMP_DIR/cookiecutter-pypackage-master"

# Generated at 2022-06-13 18:54:38.749307
# Unit test for function unzip
def test_unzip():
    import os
    import tempfile
    import shutil
    from zipfile import ZipFile
    from cookiecutter.exceptions import InvalidZipRepository
    import utils

    # Create temporary directory to unpack zipfile
    tmpdir = tempfile.mkdtemp()
    file_content = 'test_file'
    zip_file = ZipFile(os.path.join(tmpdir, 'test_zip.zip'), 'w')
    zip_file.writestr('test_file.txt', file_content)
    zip_file.close()

    # Unpack zipfile
    unzip_path = utils.unzip(zip_uri=zip_file.filename, is_url=False)

    # Test if unzipped file and content is correct

# Generated at 2022-06-13 18:55:37.262364
# Unit test for function unzip
def test_unzip():
    "Make sure unzip works"

    import os
    import shutil
    import tempfile
    from zipfile import ZipFile
    from cookiecutter.utils import unzip

    # Make a little test zipfile
    zip_base = tempfile.mkdtemp()
    zip_file = ZipFile(os.path.join(zip_base, 'test.zip'), 'w')
    zip_file.writestr('test_folder/file1.txt', 'Hello')
    zip_file.writestr('test_folder/file2.txt', 'World !')
    zip_file.close()

    # Unzip it and test it

# Generated at 2022-06-13 18:55:39.519588
# Unit test for function unzip
def test_unzip():
    """Test not a valid zip file"""
    try:
        unzip('foobar.zip', False)
        assert False
    except InvalidZipRepository:
        assert True


# Generated at 2022-06-13 18:55:47.547549
# Unit test for function unzip
def test_unzip():
    import shutil
    from cookiecutter.compat import NamedTemporaryFile

    with NamedTemporaryFile(delete=False) as zip_file:
        zip_path = zip_file.name

    with NamedTemporaryFile(delete=False) as text_file:
        text_path = text_file.name
        text_file.write(u'Hello'.encode('utf-8'))

    import zipfile
    zip_file = zipfile.ZipFile(zip_path, 'w')
    zip_file.write(text_path, 'cookiecutter_text.txt')
    zip_file.close()

    with NamedTemporaryFile(delete=False) as d:
        clone_to_dir = d.name


# Generated at 2022-06-13 18:55:48.252079
# Unit test for function unzip
def test_unzip():
    pass

# Generated at 2022-06-13 18:55:56.687970
# Unit test for function unzip
def test_unzip():
    # Create a minimal sample zipfile.
    temp_dir = tempfile.mkdtemp()

# Generated at 2022-06-13 18:55:57.140770
# Unit test for function unzip
def test_unzip():
    pass

# Generated at 2022-06-13 18:56:04.745589
# Unit test for function unzip
def test_unzip():
    """
    This function tests the unzip function with a non url and url.
    """
    # Test non url
    non_url = '/path/to/zip.zip'
    assert unzip(non_url, False, '.', False, None)

    # Test url
    url = 'http://localhost/path/to/zip/zip.zip'
    assert unzip(url, True, '.', False, 'password')


# pylint: disable=unused-argument

# Generated at 2022-06-13 18:56:12.046831
# Unit test for function unzip
def test_unzip():
    try:
        unzip('https://github.com/audreyr/cookiecutter-pypackage/archive/master.zip',
            True,
            clone_to_dir='./cookiecutters_tmp/',
            no_input=False)
        unzip('cookiecutters_tmp/master.zip',
            False,
            clone_to_dir='./cookiecutters_tmp/',
            no_input=False)
    except Exception as e:
        print(e)
        assert False
    else:
        assert True

if __name__ == "__main__":
    test_unzip()

# Generated at 2022-06-13 18:56:14.733084
# Unit test for function unzip
def test_unzip():
    """Test to confirm unzip() is working correctly."""
    unzip_path = unzip(
        zip_uri='./tests/test-data/fake-repo-tmpl/',
        is_url=False,
        clone_to_dir='.',
        no_input=True,
        password=None
    )

    assert os.path.basename(unzip_path) == 'fake-repo-tmpl'

# Generated at 2022-06-13 18:56:24.706612
# Unit test for function unzip
def test_unzip():
    """Unit tests for unzip."""
    from tempfile import mkdtemp
    from shutil import rmtree
    import zipfile
    TEST_DIR = mkdtemp()
    TEST_FILE = os.path.join(TEST_DIR, 'test.zip')
    TEST_PWD = 'cookiecutter'

    def _create_zip_file(path):
        with zipfile.ZipFile(path, 'w') as myzip:
            myzip.writestr('test_directory/test_file.txt', 'test')
            myzip.setpassword(TEST_PWD.encode('utf-8'))

    _create_zip_file(TEST_FILE)


# Generated at 2022-06-13 18:58:12.548395
# Unit test for function unzip
def test_unzip():
    """Function that tests unzip function."""
    # Test on non existing zip_uri
    try:
        unzip('some_file.zip', is_url=False, no_input=True)
    except Exception as e:
        assert isinstance(e, FileNotFoundError)

    try:
        # Test on existing zip_uri
        unzip('tests/files/zip_repo/test.zip', is_url=False, no_input=True)
        # Test on existing url_uri
        unzip('https://github.com/audreyr/cookiecutter-pypackage/archive/master.zip', is_url=True, no_input=True)
    except Exception as e:
        assert isinstance(e, InvalidZipRepository)

# Generated at 2022-06-13 18:58:18.898968
# Unit test for function unzip
def test_unzip():
    from .common import TEST_COOKIECUTTER_REPO, TEST_ZIP_REPO, TEST_ZIP_BAD_REPO
    import shutil
    import tempfile
    with tempfile.TemporaryDirectory() as clone_to_dir:
        unzip(TEST_COOKIECUTTER_REPO, True, clone_to_dir)
        unzip(TEST_ZIP_REPO, False, clone_to_dir)
        unzip(TEST_ZIP_BAD_REPO, False, clone_to_dir)



# Generated at 2022-06-13 18:58:23.292060
# Unit test for function unzip
def test_unzip():
    unzip(r"E:\Playground\Cookiecutter\cookiecutter\tests\test-repo-pre/", False)
    unzip(r"E:\Playground\Cookiecutter\cookiecutter\tests\test-repo-pre/test_repo.zip", False)
    unzip(r"https://github.com/audreyr/cookiecutter-pypackage/archive/master.zip", True)

# Generated at 2022-06-13 18:58:31.833489
# Unit test for function unzip
def test_unzip():
    """
    Create a zip file, and test unzip on the zip file.
    """
    import shutil
    import platform
    # Create a directory structure to zip up
    os.makedirs('test/test_zip')
    with open('test/test_zip/test.txt', 'w') as f:
        f.write('test')
    # Compress the directory into a zip file
    with ZipFile('test/test_zip.zip', 'w') as zip_file:
        zip_file.write('test/test_zip/test.txt', 'test_zip/test.txt')
    # Test unzip function
    unzip_path = unzip('test/test_zip.zip', False)
    # Check that the zip file was unpacked correctly

# Generated at 2022-06-13 18:58:44.752599
# Unit test for function unzip
def test_unzip():
    # 1. Test that zip_path that is for a zip file is passed through as is.
    zip_uri = 'tests/fake-repo-tmpl/fake-repo.zip'
    current_dir = os.getcwd()
    unzip_path = unzip(zip_uri, is_url=False, clone_to_dir=current_dir)
    assert os.path.abspath(unzip_path) == os.path.abspath(zip_uri)

    # 2. Test that unzip repos that are not password-protected result in a
    # unzipped folder in the temp directory.
    zip_uri = 'https://github.com/audreyr/cookiecutter-pypackage/archive/master.zip'

# Generated at 2022-06-13 18:58:50.828197
# Unit test for function unzip
def test_unzip(): 
    """Unit test for function unzip"""
    # Testing that it raises a InvalidRepository if the password is incorrect
    try:
        assert os.path.exists(unzip('tests/test-repo-tmpl', False, password='incorrectpass'))
    except InvalidZipRepository:
        pass
    else:
        assert False, 'Test Failed'
    
    # Testing that it raises a InvalidRepository if the password is not provided
    try:
        assert os.path.exists(unzip('tests/test-repo-tmpl', False))
    except InvalidZipRepository:
        pass
    else:
        assert False, 'Test Failed'
    
    # Testing that it returns the path of the repo if the password is correct

# Generated at 2022-06-13 18:58:57.441056
# Unit test for function unzip
def test_unzip():
    """Test for unzip function."""

    import os

    dir_path = os.path.dirname(os.path.abspath(__file__))
    zip_uri = os.path.join(dir_path, '..', 'tests', 'test-repo', 'test-repo.zip')

    unzip(zip_uri, False)

# Generated at 2022-06-13 18:59:04.613484
# Unit test for function unzip
def test_unzip():
    """
    Test unzip Function
    """
    from cookiecutter.zipfile_utils import unzip_repo_url

    test_url = 'https://github.com/hhatto/autopep8/zipball/master'
    result = unzip_repo_url(test_url)
    assert 'autopep8' in result
    assert 'master' in result

# Generated at 2022-06-13 18:59:06.044990
# Unit test for function unzip
def test_unzip():
    print("Test for unzip function")
    unzip("~/", True, "~/test", False, None)

# Generated at 2022-06-13 18:59:12.507729
# Unit test for function unzip
def test_unzip():
    """
    This is an unit test for the function unzip.
    """
    import sys
    from cookiecutter.main import cookiecutter

    sys.argv[1] = 'git+https://github.com/pydanny/cookiecutter-djangopackage.git'
    sys.argv = sys.argv[:2]
    cookiecutter(debug=True)
    sys.argv[1] = 'git+https://pypi.org/packages/source/p/pytest/pytest-1.0.0.zip'
    sys.argv = sys.argv[:2]
    cookiecutter(debug=True)