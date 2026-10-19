

# Generated at 2022-06-13 18:50:04.300683
# Unit test for function unzip
def test_unzip():
    # TODO: add test_unzip
    pass

# Generated at 2022-06-13 18:50:05.265997
# Unit test for function unzip
def test_unzip():
    pass

# Generated at 2022-06-13 18:50:14.519196
# Unit test for function unzip
def test_unzip():
    # Test on non-password protected zip archive
    test_path = unzip('./tests/test-zip-repos/test-zip-1.zip', False) 
    assert test_path == '/tmp/test-zip-repos/test-zip-1'
    os.removedirs(test_path)
    os.removedirs('/tmp/test-zip-repos')
    
    # Test on password protected zip archive with valid password
    test_path = unzip('./tests/test-zip-repos/test-zip-2.zip', False, password='pass')
    assert test_path == '/tmp/test-zip-repos/test-zip-2'
    os.removedirs(test_path)
    os.removedirs('/tmp/test-zip-repos')
    
   

# Generated at 2022-06-13 18:50:20.181331
# Unit test for function unzip
def test_unzip():
    temp_dir = tempfile.mkdtemp()
    assert unzip('{}/sample.zip'.format(temp_dir), False ) != ''
    assert unzip('{}/sample.zip'.format(temp_dir), False, password='test') != ''
    #assert unzip('{}/sample.zip'.format(temp_dir), False, password='test1') != ''

# Generated at 2022-06-13 18:50:20.965254
# Unit test for function unzip
def test_unzip():
    test_unzip.called = True
    pass

# Generated at 2022-06-13 18:50:27.472490
# Unit test for function unzip
def test_unzip():
    """
    This test is to ensure that the unzip function works with
    different common types of ZIP files, including those that
    were password protected and those that were not.
    """

    def test_unzip_helper(zip_uri, is_url, password=None):
        result = unzip(zip_uri, is_url, password=password)
        assert os.path.exists(os.path.join(result, 'master'))
        assert os.path.exists(os.path.join(result, 'master', 'README.md'))
        assert os.path.exists(os.path.join(result, 'master', 'requirements.txt'))

    test_unzip_helper('tests/test-unzip/zip-repo.zip', False)

# Generated at 2022-06-13 18:50:31.930377
# Unit test for function unzip
def test_unzip():
    unzip('https://github.com/larsks/cookiecutter-puppet-module/archive/master.zip', True, '.', True)
    unzip('cookiecutter-puppet-module.zip', False, '.', True)

# Generated at 2022-06-13 18:50:40.631921
# Unit test for function unzip
def test_unzip():
    import tempfile
    from zipfile import ZipFile

    # Create a zip file containing a test file
    src_file = tempfile.NamedTemporaryFile(delete=False)
    src_file.write('hello world'.encode('utf-8'))
    src_file.close()
    src_zip = tempfile.NamedTemporaryFile(delete=False)
    zip_file = ZipFile(src_zip.file, 'w')
    zip_file.write(src_file.name, 'test.txt')
    zip_file.close()
    src_zip.close()

    # Call the unzip function
    temp_dir = tempfile.mkdtemp()
    repo_dir = unzip(src_zip.name, False, clone_to_dir=temp_dir, no_input=True)
    # Check

# Generated at 2022-06-13 18:50:49.593765
# Unit test for function unzip
def test_unzip():
  from os import path
  from PyInquirer import prompt
  from cookiecutter.main import cookiecutter
  from cookiecutter.utils import make_sure_path_exists

  base_dir = '~/cookiecutter_test'
  make_sure_path_exists(base_dir)
  repo_dir = path.abspath(path.join(base_dir, 'https___github.com_audreyr_cookiecutter-pypackage.git'))
  make_sure_path_exists(repo_dir)

  ans = {'repo_url': 'https://github.com/audreyr/cookiecutter-pypackage.git'}
  cookiecutter('.', no_input=True, extra_context=ans)

# Generated at 2022-06-13 18:51:02.398638
# Unit test for function unzip
def test_unzip():
    from .vendor.mock import patch
    zip_uri = "/cookiecutter-pypackage/archive/master.zip"
    is_url = True
    clone_to_dir = tempfile.mkdtemp()
    no_input = False

# Generated at 2022-06-13 18:51:37.769440
# Unit test for function unzip
def test_unzip():
    """Unit test function unzip"""
    import shutil

    # Create a test directory
    test_dir = os.path.join(os.getcwd(), 'tests/test-unzip')
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)

    # Download a valid zip file
    download_uri = 'https://github.com/audreyr/cookiecutter-pypackage/archive/master.zip'
    test_zip_path = unzip(
        zip_uri=download_uri,
        is_url=True,
        clone_to_dir=test_dir,
        no_input=True
    )
    # Check that zip file is valid
    assert os.path.exists(test_zip_path)

    # Create a password protected zip file


# Generated at 2022-06-13 18:51:50.682324
# Unit test for function unzip
def test_unzip():
    # Create dummy zip file
    import shutil
    import zlib
    import zipfile
    # Create dummy zip file
    filepath = '/tmp/test_cookiecutter.zip'
    shutil.copyfile('tests/test-repo/foobarbaz.zip', filepath)
    print('created dummy zip archive {}'.format(filepath))
    # Extract to folder foo
    unzip_path = unzip(filepath, False)
    print('extracted dummy zip archive to {}'.format(unzip_path))
    assert unzip_path == '/tmp/tmp_cookiecutter/foobarbaz'
    assert os.path.exists('/tmp/tmp_cookiecutter/foobarbaz/hooks/post_gen_project.py')

# Generated at 2022-06-13 18:52:04.088774
# Unit test for function unzip
def test_unzip():
    assert unzip('file1.zip', False) == 'project1'
    assert os.path.exists('project1')
    assert os.path.exists('project1/file1.py')

    assert unzip('file2.zip', False, password='password') == 'project2'
    assert os.path.exists('project1')
    assert os.path.exists('project1/file1.py')

    assert unzip('https://github.com/audreyr/cookiecutter/archive/dev.zip', True) == 'project3'
    assert os.path.exists('project3')
    assert os.path.exists('project3/cookiecutter-dev')
    assert os.path.exists('project3/cookiecutter-dev/tests')

# Generated at 2022-06-13 18:52:13.780942
# Unit test for function unzip
def test_unzip():
    this_path = os.path.abspath(os.path.dirname(__file__))
    test_path = os.path.join(this_path, 'test_unzip')
    make_sure_path_exists(test_path)
    target_path = os.path.join(test_path, 'test_repo')
    zip_uri = os.path.join(this_path, 'test_zip_repo.zip')
    unzip_path = unzip(zip_uri, False, test_path)
    assert unzip_path == target_path
    shutil.rmtree(test_path)

if __name__ == '__main__':
    test_unzip()

# Generated at 2022-06-13 18:52:24.551205
# Unit test for function unzip
def test_unzip():
    import requests
    from zipfile import BadZipFile, ZipFile
    from cookiecutter.exceptions import InvalidZipRepository
    import os
    import shutil

    url = "https://github.com/audreyr/cookiecutter-pypackage/archive/master.zip"
    cache_dir = 'test-cache'
    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)
    # ensure old copies of the file are deleted, else the download test will not be run
    try:
        os.remove(cache_dir + '/master.zip')
    except:
        pass
    # test download and unzip
    unzip_path = unzip(url, True, clone_to_dir=cache_dir)
    # test that the content is as expected

# Generated at 2022-06-13 18:52:25.698999
# Unit test for function unzip
def test_unzip():
    """Test function unzip"""
    assert isinstance(unzip(),str)

# Generated at 2022-06-13 18:52:27.142582
# Unit test for function unzip
def test_unzip():
    """ Test unzip function """
    unzip('cookiecutter-example-1.zip', True, '.')

# Generated at 2022-06-13 18:52:36.062533
# Unit test for function unzip
def test_unzip():
    """Test that unzip function works"""

    # Create a temporary directory to test the unzip function
    # The cookiecutter source code has no directories
    # It contains only one file - LICENSE
    # The first unzipped entry should be the directory cookiecutter
    # This is the directory that contains LICENSE
    # The directory cookiecutter should be unzipped in the
    # temporary directory
    from cookiecutter.tests import get_test_data_dir
    import shutil
    import os

    # Get the directory path where the tests are located
    test_folder = get_test_data_dir()

    # Create a temporary directory for testing
    tmpdir = tempfile.mkdtemp()

    # Test unzip with local file
    url_or_local_file = False
    # Get the path to the zip file
    zip_uri

# Generated at 2022-06-13 18:52:36.947797
# Unit test for function unzip
def test_unzip():
    pass

# Generated at 2022-06-13 18:52:44.453912
# Unit test for function unzip
def test_unzip():
    test_cases = [
        {
            'zip_uri': 'https://github.com/cookiecutter/cookiecutter-pypackage/archive/master.zip',
            'is_url': True,
            'clone_to_dir': '',
            'no_input': False,
            'password': ''
        },
        # {
        #     'zip_uri': '',
        #     'is_url': False,
        #     'clone_to_dir': '',
        #     'no_input': False,
        #     'password': ''
        # },
    ]

    for t in test_cases:
        unzip(**t)

# Generated at 2022-06-13 18:53:07.762319
# Unit test for function unzip
def test_unzip():
    """
    Test that unzipping a zip archive to a temporary directory
    actually works
    """
    from cookiecutter.utils import rmtree

    # Create a test zip archive to unzip
    test_zip_directory = os.path.join(os.path.dirname(__file__), 'test_zip')
    test_zip_path = os.path.join(test_zip_directory, 'test.zip')
    with ZipFile(test_zip_path, 'w') as f:
        # Create an empty file
        f.writestr('test_dir/test.txt', 'test file')

    # Unzip the test file
    unzip_path = unzip(test_zip_path, False, test_zip_directory)

    # Compare the result with the original

# Generated at 2022-06-13 18:53:08.340568
# Unit test for function unzip
def test_unzip():
    pass

# Generated at 2022-06-13 18:53:09.504376
# Unit test for function unzip
def test_unzip():
    assert True

# Generated at 2022-06-13 18:53:15.667788
# Unit test for function unzip
def test_unzip():
    tempzip = tempfile.NamedTemporaryFile(suffix='.zip')
    with ZipFile(tempzip.name, 'w') as zf:
        zf.writestr('bob/','')
    unzip_path = unzip(tempzip.name, is_url=False)
    assert os.path.exists(unzip_path) and os.path.isdir(unzip_path)
    # Clean up
    shutil.rmtree(unzip_path)

# Generated at 2022-06-13 18:53:25.276703
# Unit test for function unzip
def test_unzip():
    import zipfile
    import os
    import shutil
    import tempfile
    import unittest

    URL = 'https://github.com/audreyr/cookiecutter-pypackage/archive/master.zip'
    URL2 = 'https://github.com/audreyr/cookiecutter-pypackage/archive/master.zip'
    TEST_ZIP_FILE_URL = 'https://github.com/audreyr/cookiecutter-pypackage/archive/master.zip'
    TEST_ZIP_FILE = 'master.zip'
    TEST_DIRECTORY = 'cookiecutter-pypackage-master'
    TEST_DIRECTORY_1 = 'cookiecutter-pypackage-master'

    # Truncate file extension to simulate a password-protected zip file
    TRUNC

# Generated at 2022-06-13 18:53:36.597013
# Unit test for function unzip
def test_unzip():
    """
    Unit test for function unzip.
    """
    import os
    import shutil
    from zipfile import ZipFile
    from tempfile import mkdtemp
    from cookiecutter.utils import read_repo_password

    def touch(path):
        """
        Create a file at ``path`` with minimal content.
        """
        with open(path, 'w') as f:
            f.write('Test file')

    repo_name = 'testing_repo'
    repo_path = os.path.join(mkdtemp(), repo_name)
    os.mkdir(repo_path)
    os.mkdir(os.path.join(repo_path, 'foo'))
    os.mkdir(os.path.join(repo_path, 'bar'))

# Generated at 2022-06-13 18:53:47.324461
# Unit test for function unzip
def test_unzip():
    r"""Test for function unzip."""
    import shutil
    import zipfile


# Generated at 2022-06-13 18:53:49.615091
# Unit test for function unzip
def test_unzip():
    assert os.path.exists(unzip(zip_uri, is_url, clone_to_dir, no_input, password)) == True

# Generated at 2022-06-13 18:53:59.754346
# Unit test for function unzip
def test_unzip():
    """Ensure the unzip function works as expected. """
    import shutil
    import time
    import zipfile

    # Set up the base zip file
    test_tmp_dir = tempfile.mkdtemp()
    zip_file_name = 'test_zip.zip'
    zip_file_path = os.path.join(test_tmp_dir, zip_file_name)
    test_zip_file = zipfile.ZipFile(zip_file_path, 'w')
    test_zip_file.writestr('test/test_file.txt', bytes('test_text', 'utf-8'))
    test_zip_file.close()

    # Set up the base cached zip file
    test_cache_dir = os.path.join(test_tmp_dir, 'cache')

# Generated at 2022-06-13 18:54:01.075429
# Unit test for function unzip
def test_unzip():
    unzip('https://github.com/matthewmccullough/masteringgithub/archive/master.zip', True)

# Generated at 2022-06-13 18:54:18.790550
# Unit test for function unzip
def test_unzip():
    unzip('/home/georg/test.zip', False)

test_unzip()

# Generated at 2022-06-13 18:54:26.465313
# Unit test for function unzip
def test_unzip():
    """Test for unzip function"""
    import requests
    import shutil
    import os
    import tempfile
    with tempfile.TemporaryDirectory() as tmpdirname:
        with open(os.path.join(tmpdirname, 'test.zip'), 'wb') as f:
            r = requests.get('https://github.com/audreyr/cookiecutter-pypackage/archive/master.zip', stream=True)
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)
        unzip_path = unzip('test.zip', False, tmpdirname)
        shutil.rmtree(unzip_path)

# Generated at 2022-06-13 18:54:27.241737
# Unit test for function unzip
def test_unzip():
    raise NotImplementedError

# Generated at 2022-06-13 18:54:27.746281
# Unit test for function unzip
def test_unzip():
    pass

# Generated at 2022-06-13 18:54:37.860120
# Unit test for function unzip
def test_unzip():
    import os
    import subprocess
    import shutil
    from tempfile import mkdtemp
    from zipfile import ZipFile

    # Create a zipfile to unpack
    test_dir = mkdtemp()
    os.makedirs(os.path.join(test_dir, 'test_repo'))
    test_zip = os.path.join(test_dir, 'test.zip')

    with ZipFile(test_zip, 'w') as test_zipfile:
        test_zipfile.write(__file__, 'test_repo/test_zip.py')

    # Do the test
    unzipped_dir = unzip(test_zip, False)

    # Teardown the test
    shutil.rmtree(unzipped_dir)
    os.remove(test_zip)
    shut

# Generated at 2022-06-13 18:54:48.720164
# Unit test for function unzip
def test_unzip():
    try:
        os.remove('tests/test-unzip.zip')
    except:
        pass

    import shutil
    try:
        shutil.rmtree('tests/test-unzip')
    except:
        pass

    os.system('zip -r tests/test-unzip.zip tests/test-unzip')
    os.system('rm -rf tests/test-unzip')
    unzip('tests/test-unzip.zip', False)
    assert(os.path.exists('tests/test-unzip'))
    shutil.rmtree('tests/test-unzip')

# Generated at 2022-06-13 18:54:56.215850
# Unit test for function unzip
def test_unzip():
    """Test if unzip is working as expected"""
    import shutil
    from nose.tools import ok_, eq_
    from cookiecutter.config import DEFAULT_CONFIG

    zip_path = os.path.join('tests','test-zip','cookiecutter-pypackage.zip')
    clone_to_dir = tempfile.mkdtemp()
    unzip_path = unzip(zip_path, is_url=False, clone_to_dir=clone_to_dir, no_input=True)
    eq_(unzip_path[-16:],'/cookiecutter-pypackage')
    cookiecutter_json_path = os.path.join(unzip_path, 'cookiecutter.json')
    ok_(os.path.exists(cookiecutter_json_path))

# Generated at 2022-06-13 18:54:59.575285
# Unit test for function unzip
def test_unzip():
    def test():
        test_zip = './tests/test-repo.zip'
        unzip(test_zip, True)

    test()


# Generated at 2022-06-13 18:55:05.315615
# Unit test for function unzip
def test_unzip():

    zip_uri = 'https://github.com/audreyr/cookiecutter-pypackage/archive/master.zip'
    assert unzip(zip_uri, is_url=True, clone_to_dir='.', no_input=False, password=None) == unzip(zip_uri, is_url=True, clone_to_dir='.', no_input=False, password=None)

# Generated at 2022-06-13 18:55:10.158214
# Unit test for function unzip
def test_unzip():
    # Test public function
    unzip("tests/test-repo/test-zip.zip", False)
    # Test private function
    # unzip("tests/test-repo/test-zip.zip", False, True)
    # Test password lock
    # unzip("tests/test-repo/test-zip-password.zip", False, False, b'password')

# Generated at 2022-06-13 18:55:33.037026
# Unit test for function unzip
def test_unzip():
    # TODO
    pass

# Generated at 2022-06-13 18:55:42.443029
# Unit test for function unzip
def test_unzip():
    """
    Unit test for unzip function.
    """
    import shutil
    from zipfile import ZipFile
    from cookiecutter.exceptions import InvalidZipRepository

    # create test zip file
    test_zip = '/tmp/test_zip.zip'
    with ZipFile(test_zip, 'w') as test:
        test.writestr('test/test.txt', 'test')

    assert unzip(test_zip, is_url=True) is not None

    try:
        unzip(test_zip, is_url=True, password='blar')
    except InvalidZipRepository:
        pass
    else:
        raise AssertionError

    # remove test files
    shutil.rmtree(unzip(test_zip, is_url=True))
    os.remove(test_zip)

# Generated at 2022-06-13 18:55:43.864253
# Unit test for function unzip
def test_unzip():
    assert unzip('http://example.com/test.zip', True) is not None



# Generated at 2022-06-13 18:55:53.632351
# Unit test for function unzip
def test_unzip():
    # Create a zip file
    import zipfile
    # Create a test zip
    zf = zipfile.ZipFile('test.zip', mode='w')
    # Add a file to the zip
    zf.writestr('test/fake_file.txt', 'Holla!')
    # Close the zip file
    zf.close()
    # Now unzip and ensure the expected file exists.
    unzip_path = unzip('test.zip', is_url=False)
    assert os.path.exists(os.path.join(unzip_path, 'fake_file.txt'))

# Generated at 2022-06-13 18:55:56.668365
# Unit test for function unzip
def test_unzip():
    try:
        unzip('https://github.com/audreyr/cookiecutter-pypackage/archive/master.zip', True)
    except requests.exceptions.RequestException:
        pass

# Generated at 2022-06-13 18:56:00.942505
# Unit test for function unzip
def test_unzip():

    test_files_dir = os.path.join(os.path.dirname(__file__), 'files')
    zip_path = os.path.join(test_files_dir, 'zipfile.zip')
    unzip_path = unzip(zip_uri=zip_path, is_url=False, no_input=False)
    assert os.path.isfile(os.path.join(unzip_path, 'key.txt')) is True
    assert os.path.isfile(os.path.join(unzip_path, 'greetings.txt')) is True
    assert os.path.isfile(os.path.join(unzip_path, 'nested', 'greetings.txt')) is True

# Generated at 2022-06-13 18:56:02.092781
# Unit test for function unzip
def test_unzip():
    pass

# Generated at 2022-06-13 18:56:12.008861
# Unit test for function unzip
def test_unzip():
    """Test unzip function."""
    # Travis CI doesn't have git-lfs installed and so will fail to download
    # the test repo.
    if 'TRAVIS' in os.environ and os.environ['TRAVIS'].lower() == 'true':
        return

    zipfile_path = 'https://github.com/audreyr/cookiecutter-pypackage/archive/master.zip'
    clone_to_dir = 'tests/test-unzip'
    unzipped_path = unzip(zipfile_path, True, clone_to_dir)
    assert unzipped_path.endswith('tests/test-unzip/cookiecutter-pypackage-master')

# Generated at 2022-06-13 18:56:18.715180
# Unit test for function unzip
def test_unzip():
    import os
    import shutil
    from unittest.mock import patch
    from tempfile import mkdtemp
    from cookiecutter import utils
    from cookiecutter.utils import rmtree

    with patch('cookiecutter.zipfile.ZipFile') as mock_zipfile:
        base_path = mkdtemp()
        unzip_path = unzip('non-existant-file.zip', is_url=False, clone_to_dir=base_path)

        assert os.path.isdir(unzip_path)

        with patch('cookiecutter.zipfile.ZipFile.namelist', lambda s: ['foo/', 'foo/project_name/file.txt']):
            assert os.path.exists(os.path.join(base_path, 'non-existant-file.zip'))


# Generated at 2022-06-13 18:56:27.593608
# Unit test for function unzip
def test_unzip():
    # From repository templates/test_cookiecutter_jinja2/
    test_repo = 'https://github.com/okken/cookiecutter-test-repo/archive/master.zip'
    # From GitHub templates/test_cookiecutter_jinja2/
    test_repo_password = 'https://github.com/okken/cookiecutter-test-repo/archive/master-password.zip'

    passwd = 'mytopsecretpassword'

    # No password
    unzip_path = unzip(zip_uri=test_repo, is_url=True, no_input=True)
    assert os.path.exists(unzip_path)
    assert os.path.isdir(unzip_path)

    # With password

# Generated at 2022-06-13 18:57:03.990090
# Unit test for function unzip
def test_unzip():
    # Test valid zip archive
    zip_uri = 'https://github.com/rnd-iscte/cookiecutter-paw_template/archive/master.zip'
    unzip_path = unzip(zip_uri, True, ".")
    print(unzip_path)
    os.remove(os.path.join(unzip_path, 'cookiecutter.json'))

    # Test invalid zip archive doesn't throw exceptions
    zip_uri = 'https://github.com/jacebrowning/cookiecutter-pytube/archive/master.zip'
    try:
        unzip_path = unzip(zip_uri, True, ".")
    except InvalidZipRepository:
        print('Invalid zip archive')

    # Test password protected repository

# Generated at 2022-06-13 18:57:13.211606
# Unit test for function unzip
def test_unzip():
    zip_uri = 'https://github.com/audreyr/cookiecutter-pypackage/zipball/master'
    is_url = '[y]'
    clone_to_dir = tempfile.mkdtemp()
    no_input = '[n]'
    password = 'cookie'
    testing_dir = unzip(zip_uri, is_url, clone_to_dir, no_input, password)
    project_name = zip_uri.rsplit('/', 1)[1]
    testing_path = os.path.join(testing_dir, project_name)
    assert os.path.exists(testing_path)

# Generated at 2022-06-13 18:57:26.423324
# Unit test for function unzip
def test_unzip():
    import shutil
    import zipfile

    import pytest

    zip_uri = 'test-repo.zip'
    password = 'pass123'

    # Create a test zip file
    zip_file = zipfile.ZipFile(zip_uri, 'w')
    zip_file.writestr('test/test_file', b'Test')
    zip_file.writestr('test/test_dir/test_file2', b'Test2')
    zip_file.close()

    # Password protect the zip file
    zip_file = zipfile.ZipFile(zip_uri, 'a')
    zip_file.setpassword(password.encode('utf-8'))
    zip_file.writestr('test/secret_file', b'Secret')
    zip_file.close()


# Generated at 2022-06-13 18:57:32.568229
# Unit test for function unzip
def test_unzip():
    """
    unzip(zip_uri, is_url, clone_to_dir='.', no_input=False, password=None)
    """
    from cookiecutter import __version__

    this_dir = os.path.abspath(os.path.dirname(__file__))
    fixture_path = os.path.join(this_dir, 'test-unzip', 'test.zip')

    assert os.path.exists(fixture_path)

    unzip_test_path = unzip(fixture_path, False)

    assert os.path.exists(os.path.join(unzip_test_path, 'test.txt'))

    # Clean up the temporary directory
    os.remove(os.path.join(unzip_test_path, 'test.txt'))
    os.r

# Generated at 2022-06-13 18:57:45.694705
# Unit test for function unzip
def test_unzip():
    import pytest
    from cookiecutter.utils import rmtree

    def test_generate_files(result):
        assert os.path.isdir(result['unzip_path'])
        assert os.path.isdir(result.get('clone_to_dir'))
        assert os.path.isfile(result['zip_path'])

    def test_no_repo_dir(result):
        assert os.path.isfile(result['zip_path'])

    def test_delete_repo_dir(result):
        assert os.path.isfile(result['zip_path'])

    def test_no_input(result):
        assert os.path.isfile(result['zip_path'])


# Generated at 2022-06-13 18:57:58.483721
# Unit test for function unzip
def test_unzip():
    # Test unzip with a zipURL
    tempdir = unzip('https://github.com/audreyr/cookiecutter-pypackage/archive/master.zip', True)
    assert os.path.exists(tempdir)
    assert os.path.exists(os.path.join(tempdir,'.gitignore'))
    # Test unzip with a zipfile
    tempdir2 = unzip('tests/test-repos/test-repo-template.zip', False)
    assert os.path.exists(tempdir2)
    assert os.path.exists(os.path.join(tempdir2,'bin','test.exe'))
    # Test unzip with an invalid zipURL

# Generated at 2022-06-13 18:58:03.766117
# Unit test for function unzip
def test_unzip():
    assert os.path.exists(unzip('tests/fake-repo-zip/', is_url=False))
    assert os.path.exists(unzip('tests/fake-repo-zip-empty/', is_url=False))
    assert os.path.exists(unzip('tests/fake-repo-zip-protected/', is_url=False, password='cookiecutter'))

# Generated at 2022-06-13 18:58:13.088149
# Unit test for function unzip
def test_unzip():
    # Test existing unencrypted file
    unzip_path = unzip(
        zip_uri=os.path.join(os.path.dirname(__file__), 'data/test-unzip.zip'),
        is_url=False,
        clone_to_dir='.',
        no_input=True,
    )
    assert os.path.exists(unzip_path)
    assert os.path.exists(os.path.join(unzip_path, 'test-unzip/foo.txt'))
    assert os.path.exists(os.path.join(unzip_path, 'test-unzip/bar.txt'))
    assert not os.path.exists(os.path.join(unzip_path, 'test-unzip.zip'))
    assert not os.path.exists

# Generated at 2022-06-13 18:58:21.557624
# Unit test for function unzip
def test_unzip():
    import subprocess
    import sys
    from shutil import rmtree
    from tempfile import mkdtemp
    from unittest import TestCase
    from unittest.mock import mock_open, patch

    from cookiecutter.utils.paths import map_repo_template

    if sys.version_info < (3, 5):
        raise ImportError('Only runs on Python 3.5+')

    class UnzipTest(TestCase):

        @classmethod
        def setUpClass(self):
            # Create temporary path to test repo
            self.tmp_path = mkdtemp()
            # Create temporary path to zip file
            self.tmp_zip_path = mkdtemp()
            # Create temporary path to unzip file
            self.tmp_unzip_path = mkdtemp()


# Generated at 2022-06-13 18:58:28.465041
# Unit test for function unzip
def test_unzip():
    """ Unit test for function unzip()
    """
    test_dir = os.path.join('tests','test-unzip-repo')
    if (os.path.isdir(test_dir)):
        import shutil
        shutil.rmtree(test_dir)

    cookiecutter_dir = os.path.join(os.path.expanduser('~'), '.cookiecutters')
    if (os.path.isdir(cookiecutter_dir)):
        import shutil
        shutil.rmtree(cookiecutter_dir)

    repo_name = 'unzip-repo'
    url = 'https://github.com/audreyr/{}/zipball/master'.format(repo_name)
    unzip_path = unzip(url, True, test_dir, False)


# Generated at 2022-06-13 18:59:45.105254
# Unit test for function unzip
def test_unzip():
    """Test unzipping a zip file."""
    from . import context

    class Options:
        no_input = False

    zip_url = 'https://github.com/cookiecutter/cookiecutter-pypackage/zipball/0.4.4'
    clone_to_dir='.'
    no_input = Options().no_input
    password = None
    expected_unzip_path = u'/tmp/cookiecutter-pypackage-0.4.4'

    unzip_path = unzip(
        zip_url, is_url=True, clone_to_dir=clone_to_dir,
        no_input=no_input, password=password
    )
    assert unzip_path == expected_unzip_path, ("Couldn't unzip file "
                                               "from url properly.")

# Generated at 2022-06-13 18:59:50.551846
# Unit test for function unzip
def test_unzip():
    # unzip function does not exist in v0.6.0, this is here for
    # testing purpose
    def unzip(zip_uri, is_url, clone_to_dir='.', no_input=False, password=None):
        raise NotImplementedError

    try:
        unzip('https://github.com/audreyr/cookiecutter-pypackage.git')
    except NotImplementedError:
        pass

# Generated at 2022-06-13 19:00:05.555039
# Unit test for function unzip
def test_unzip():
    # Test URL
    assert os.path.exists('/tmp/pytest-cookies/cookiecutter-pypackage/')
    unzip_path = unzip('https://github.com/audreyr/cookiecutter-pypackage/archive/master.zip', 'URL', clone_to_dir='/tmp/pytest-cookies')
    unzip_path = '/'.join(unzip_path.split('/')[:-1])
    assert os.path.exists('/tmp/pytest-cookies/cookiecutter-pypackage/')
    # Test File
    assert os.path.exists('/tmp/pytest-cookies/cookiecutter-pypackage/')