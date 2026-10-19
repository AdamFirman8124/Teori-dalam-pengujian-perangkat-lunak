

# Generated at 2022-06-13 18:50:05.324616
# Unit test for function unzip
def test_unzip():
    # TODO: write tests for unzip here
    assert False

# Generated at 2022-06-13 18:50:08.521872
# Unit test for function unzip
def test_unzip():
    repo_url = 'https://github.com/audreyr/cookiecutter-pypackage/archive/master.zip'

    unzip(repo_url, is_url=True, no_input=True)

# Generated at 2022-06-13 18:50:10.536491
# Unit test for function unzip
def test_unzip():
    unzip("https://github.com/audreyr/cookiecutter-pypackage/archive/master.zip", True)

# Generated at 2022-06-13 18:50:16.029599
# Unit test for function unzip
def test_unzip():
    """
    Test to ensure unzip() works without error, does not raise an error,
    and returns a string.
    """
    # Test for a function that works with a zip file.
    # THIS IS RUN ONLY IF BEFORE running pytest.
    # ZIP FILE MUST BE ALREADY PRESENT in repos/
    result_string = unzip(
        zip_uri='repos/zip/cookiecutter-jquery.zip', is_url=False,
        clone_to_dir='/tmp', no_input=True)
    assert isinstance(result_string, str)

    # Test for a function that works with a password-protected zip file.
    # THIS IS RUN ONLY IF BEFORE running pytest.
    # ZIP FILE MUST BE ALREADY PRESENT in repos/

# Generated at 2022-06-13 18:50:25.056829
# Unit test for function unzip
def test_unzip():
    import shutil
    import requests_mock
    from os import path, unlink
    from zipfile import ZipFile
    from tempfile import mkdtemp

    with requests_mock.mock() as m:
        m.get('http://ex/test.zip',
              content=open(path.join(path.dirname(__file__), 'test_repo.zip'), 'rb').read())
        test_dir = mkdtemp()

        unzip('http://ex/test.zip', True, clone_to_dir=test_dir)

        assert path.exists(path.join(test_dir, 'test.zip'))
        assert path.exists(path.join(test_dir, 'test_repo'))


# Generated at 2022-06-13 18:50:26.930730
# Unit test for function unzip
def test_unzip():
    # TODO: Need to figure out how to test this function
    #       with a password protected zip file.
    pass

# Generated at 2022-06-13 18:50:37.755947
# Unit test for function unzip
def test_unzip():
    from .utils import TMP_DIRECTORY, TMP_ZIP_PATH, TMP_ZIP_PATH_URL

    # Simple zip file without password
    unzip(TMP_ZIP_PATH, False)

    # Simple zip file without password
    unzip(TMP_ZIP_PATH_URL, True)

    # Zip file with password
    password = 'test'
    os.system('zip -P {} {}'.format(password, TMP_ZIP_PATH))
    unzip(TMP_ZIP_PATH, False, password=password)
    os.system('zip -P {} {}'.format(password, TMP_ZIP_PATH))
    unzip(TMP_ZIP_PATH_URL, True, password=password)

# Generated at 2022-06-13 18:50:40.709800
# Unit test for function unzip
def test_unzip():
    unzip('https://github.com/audreyr/cookiecutter-pypackage/archive/master.zip',True)

test_unzip()

# Generated at 2022-06-13 18:50:43.735585
# Unit test for function unzip
def test_unzip():
    """
    Sample function test to help you get started.
    """
    assert unzip != None
    # unzip should return the string 'test'.
    # assert unzip(input) == 'test'

# Generated at 2022-06-13 18:50:51.818177
# Unit test for function unzip
def test_unzip():
    def dummy_downloader_symlinks_removed(repo_url, repo_dir, clone_to_dir=''):
        assert clone_to_dir == ''
        assert repo_url == 'http://archive.url'
        assert repo_dir == 'http://archive.url'
        return '/tmp/archive.zip'

    def dummy_downloader_symlinks_preserved(repo_url, repo_dir, clone_to_dir=''):
        assert clone_to_dir == ''
        assert repo_url == 'http://archive.url'
        assert repo_dir == 'http://archive.url'
        return '/tmp/archive.zip'

    def dummy_downloader_bad_zip(repo_url, repo_dir, clone_to_dir=''):
        assert clone_to_dir == ''

# Generated at 2022-06-13 18:51:00.428533
# Unit test for function unzip
def test_unzip():
    is_url = True
    clone_to_dir = '.'
    zip_uri = 'https://github.com/audreyr/cookiecutter-pypackage/archive/master.zip'
    unzip(is_url, zip_uri, clone_to_dir)

# test_unzip()

# Generated at 2022-06-13 18:51:04.983368
# Unit test for function unzip
def test_unzip():
    zip_path = 'tests/test-repo-templates/testzip-master.zip'
    zip_uri = 'https://github.com/audreyr/cookiecutter-pypackage/archive/master.zip'
    unzip_path = unzip(zip_uri, True, 'tests/test-repo-templates/')
    assert os.path.exists(unzip_path)

# Generated at 2022-06-13 18:51:06.404453
# Unit test for function unzip
def test_unzip():
    """unzip test
    """
    pass


# Generated at 2022-06-13 18:51:17.114804
# Unit test for function unzip
def test_unzip():
    """Test function unzip."""
    import pytest
    from py._path.local import LocalPath
    from pytest_mock import MockFixture

    @pytest.fixture
    def mock_download(tmpdir, mock_files):
        (mock_files/'repo_dir').ensure_dir()
        (mock_files/'repo_dir'/'bar.zip').write('foo')
        mock_path = LocalPath(str(mock_files))
        mock_download.path = mock_path
        return mock_path

    response = requests.Response()
    response.raw = b'test'
    def request_get(url, stream=True):
        return response

    def read_repo_password(url, stream=True):
        return 'password'


# Generated at 2022-06-13 18:51:24.499917
# Unit test for function unzip
def test_unzip():

    dir_path = os.path.dirname(os.path.realpath(__file__))
    # Zip file not exist
    with pytest.raises(InvalidZipRepository) as ex_info:
        unzip('not_exist_zip.zip', False)

    assert 'not_exist_zip.zip is not a valid zip archive' == str(ex_info.value)

    # Zip file is empty
    with pytest.raises(InvalidZipRepository) as ex_info:
        unzip(os.path.join(dir_path, '../tests/fake-repo-tmpl/empty.zip'), False)


# Generated at 2022-06-13 18:51:33.529958
# Unit test for function unzip
def test_unzip():
    # Test URLs
    zip_uri = 'https://bitbucket.org/pokonski/cookiecutter-pypackage-minimal/get/master.zip'
    unzip(zip_uri,True)

    # Test local zip
    zip_uri = './tests/test-repos/py3.zip'
    unzip(zip_uri,False)

    # Test local zip
    zip_uri = './tests/test-repos/py3.zip'
    unzip(zip_uri, False, '.', password="test")

# Generated at 2022-06-13 18:51:47.057836
# Unit test for function unzip
def test_unzip():

    tmpdir = tempfile.mkdtemp()
    local_zip_file = os.path.join(tmpdir, 'test_file.zip')
    local_zip_file_with_password = os.path.join(tmpdir, 'test_file_with_password.zip')

    # create plain text files

    with open(os.path.join(tmpdir, 'test_dir1', 'test_file1.txt'), 'w') as f:
        f.write('test_file1')
    with open(os.path.join(tmpdir, 'test_dir2', 'test_file2.txt'), 'w') as f:
        f.write('test_file2')

    # create zip file with plain text files

    import zipfile

# Generated at 2022-06-13 18:51:55.390435
# Unit test for function unzip
def test_unzip():
    if os.path.isdir('./tests/files/unzip-test/test-cookiecutter-dist'):
        # Remove old test folder
        for root, dirs, files in os.walk('./tests/files/unzip-test'):
            for f in files:
                os.unlink(os.path.join(root, f))
            for d in dirs:
                shutil.rmtree(os.path.join(root, d))
    unzip('./tests/files/test-cookiecutter-dist.zip', False, './tests/files/unzip-test', False)
    assert os.path.isdir('./tests/files/unzip-test/test-cookiecutter-dist')

# Generated at 2022-06-13 18:51:56.143519
# Unit test for function unzip
def test_unzip():
    return

# Generated at 2022-06-13 18:52:07.546180
# Unit test for function unzip
def test_unzip():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    project_dir = os.path.join(dir_path, '..', '..', 'tests', 'files',
                               'test-repo-tmpl')
    repo_dir = os.path.join(project_dir, '{{cookiecutter.repo_name}}')
    template_dir = os.path.join(repo_dir, '{{cookiecutter.repo_name}}')
    unzip_path = unzip(
        zip_uri=project_dir,
        is_url=False,
        clone_to_dir=os.path.join(os.path.expanduser('./'), '_repos')
    )
    assert os.path.isdir(unzip_path)

# Generated at 2022-06-13 18:52:14.410020
# Unit test for function unzip
def test_unzip():
    assert unzip('git+https://github.com/pytest-dev/cookiecutter-pytest-plugin.git', False)

# Generated at 2022-06-13 18:52:25.302065
# Unit test for function unzip
def test_unzip():
    """
    Test unzip function with both valid and invalid zip files.
    """
    temp_dir = tempfile.mkdtemp()

# Generated at 2022-06-13 18:52:34.520734
# Unit test for function unzip
def test_unzip():
    import shutil
    import subprocess

    # Create a simple git repo with one file in it.
    repo_name = 'tmp'
    repo_path = os.path.abspath(repo_name)
    shutil.rmtree(repo_name, ignore_errors=True)
    subprocess.check_call(['git', 'init', repo_name])
    with open(os.path.join(repo_path, 'foo.txt'), 'w') as fp:
        fp.write("bar\n")
    subprocess.check_call(['git', 'add', 'foo.txt'], cwd=repo_path)
    subprocess.check_call(
        ['git', 'commit', '-m', 'Add foo.txt'], cwd=repo_path
    )

    #

# Generated at 2022-06-13 18:52:39.663579
# Unit test for function unzip
def test_unzip():
    assert os.path.isdir(unzip(zip_uri='https://github.com/audreyr/cookiecutter-pypackage/archive/master.zip',is_url=True))
    assert os.path.isdir(unzip(zip_uri='tests/unzip_test.zip',is_url=False))

if __name__ =='__main__':
    test_unzip()

# Generated at 2022-06-13 18:52:46.338474
# Unit test for function unzip
def test_unzip():
    """Test the unzip function."""
    assert unzip(
        zip_uri='https://github.com/audreyr/cookiecutter-pypackage/zipball/master',
        is_url=True,
        clone_to_dir='.',
        no_input=True,
        password=None
    )

# Generated at 2022-06-13 18:52:55.352631
# Unit test for function unzip
def test_unzip():
    from shutil import copy
    from os import path
    from tempfile import mkdtemp
    from os import remove
    from os import path
    from os import getcwd, chdir

    input_filename = 'input.zip'
    copy(input_filename, 'input.zip.bak')

    temp_directory = mkdtemp()
    chdir(temp_directory)
    working_directory = getcwd()

    unzip_path = unzip('input.zip', False)
    new_input_filename = path.join(unzip_path, 'input.txt')

    assert path.isfile(new_input_filename)

    chdir(working_directory)
    # cleanup
    remove(path.join(temp_directory, 'input.zip'))

# Generated at 2022-06-13 18:52:57.791777
# Unit test for function unzip
def test_unzip():
    filename = 'unzip_test.zip'
    unzip_path = unzip(zip_uri=filename, is_url=False, clone_to_dir='.')
    assert unzip_path == '/tmp/AAA'

# Generated at 2022-06-13 18:53:06.880275
# Unit test for function unzip
def test_unzip():
    import sys
    import tempfile
    import filecmp
    from cookiecutter.utils import rmtree
    from cookiecutter.zipfile_utils import unzip
    
    # FIXME: Need test cases for the free_games and the password protected repos...
    test_data_dir = os.path.join(
        os.path.normpath(os.path.dirname(__file__)), 'test_data')
    assert os.path.exists(test_data_dir)

    # Test case: zip_file = cookiecutter-master
    test_cookiecutter_zip_file = os.path.join(test_data_dir, 'zip_file', 'cookiecutter-master.zip')

# Generated at 2022-06-13 18:53:16.962575
# Unit test for function unzip
def test_unzip():
    """Unit test for unzip function.
    """
    import shutil
    import tempfile
    import zipfile

    # Create temporary directory
    tmp_dir = tempfile.mkdtemp()
    tmp_zip_path = os.path.join(tmp_dir, 'cookiecutter_unzip_test.zip')

    # Create a zipfile with a directory at the root
    with zipfile.ZipFile(tmp_zip_path, 'w') as f:
        f.write('cookiecutter_unzip_test/')
        f.write('cookiecutter_unzip_test/file.txt')

    # Unzip to temporary directory
    unzip_dir = unzip('', False, tmp_dir)

    # Check files were correctly extracted

# Generated at 2022-06-13 18:53:26.019712
# Unit test for function unzip
def test_unzip():
    import shutil
    from pathlib import Path
    from tempfile import TemporaryDirectory
    from cookiecutter.utils import chdir
    
    with TemporaryDirectory() as tmpdir:
        with chdir(tmpdir):

            # Create our minimal test repo
            minimal_test_repo = Path(tmpdir, 'minimal_test_repo.zip')

            minimal_test_repo_path = Path(tmpdir, 'minimal_test_repo')
            minimal_test_repo_path.mkdir()

            bar_file_path = Path(minimal_test_repo_path, 'bar_file.yml')
            bar_file_path.touch()


# Generated at 2022-06-13 18:53:56.147587
# Unit test for function unzip
def test_unzip():
    zip_uri = 'https://github.com/miloharper/cookiecutter-pypackage-minimal/archive/master.zip'
    is_url = True
    clone_to_dir = '.'
    no_input = True

    unzip(zip_uri, is_url, clone_to_dir, no_input)

# Generated at 2022-06-13 18:53:59.753627
# Unit test for function unzip
def test_unzip():
    project_tmp = unzip(zip_uri, False)

    assert os.path.isdir(project_tmp)
    assert os.path.isdir(os.path.join(project_tmp, 'tests'))
    assert os.path.isfile(os.path.join(project_tmp, 'README.rst'))

# Generated at 2022-06-13 18:54:00.829074
# Unit test for function unzip
def test_unzip():
    import doctest
    doctest.testmod(verbose=True)

# Generated at 2022-06-13 18:54:06.770773
# Unit test for function unzip
def test_unzip():
    import sys
    import os 
    #sys.dont_write_bytecode = True
    CURDIR = os.path.abspath('./')
    sys.path.append(CURDIR)
    import unzip
    assert unzip.unzip('https://github.com/audreyr/cookiecutter-pypackage/archive/master.zip', True, '.', False, None)

# Generated at 2022-06-13 18:54:16.077326
# Unit test for function unzip
def test_unzip():
    import shutil
    import requests
    import pytest
    import random

    # Create a temporary repository to store zip file
    clone_to_dir = tempfile.mkdtemp()

    # Get zip location
    r = requests.get('https://github.com/audreyr/cookiecutter-pypackage.git')
    debug_zip_uri = r.url
    debug_zip_uri = debug_zip_uri.replace('github.com/', 'codeload.github.com/')
    debug_zip_uri = '{}/zip/master'.format(debug_zip_uri)

    # Get zip file and unzip
    debug_unzip_path = unzip(debug_zip_uri, is_url=True, clone_to_dir=clone_to_dir)

    # Check if unzipping file yielded

# Generated at 2022-06-13 18:54:20.438749
# Unit test for function unzip
def test_unzip():
    # Test with git repository
    try:
        unzip("https://github.com/audreyr/cookiecutter-pypackage/archive/master")
    except InvalidZipRepository:
        print("Zip file is a valid zip archive")

# Generated at 2022-06-13 18:54:29.011440
# Unit test for function unzip
def test_unzip():
    # GIVEN
    import json
    import zipfile
    zip_file_name = 'test_zipfile.zip'
    zip_content = {'path_in_zip':'cookiecutter.json', 'user_key':'value_from_zip'}
    with zipfile.ZipFile(zip_file_name, 'w', compression=zipfile.ZIP_DEFLATED) as zf:
        zf.writestr('cookiecutter.json', json.dumps(zip_content))

    # WHEN
    # unzipped_path = 'path_to_unzip'
    unzipped_path = unzip(zip_file_name, True, '.', False, 'none')

    # THEN
    assert unzipped_path != 'path_to_unzip'
    assert os.path.ex

# Generated at 2022-06-13 18:54:38.436689
# Unit test for function unzip
def test_unzip():
    # Test when password is provided
    assert unzip('https://github.com/jichu4n/cookiecutter-simple/archive/master.zip', True, no_input=True, password='password') == unzip_path
    assert os.path.isdir(unzip_path)

    # Test when no password is provided should raise error
    try:
        unzip('https://github.com/jichu4n/cookiecutter-simple/archive/master.zip', True, no_input=True)
    except InvalidZipRepository:
        pass
    else:
        raise TestError('No password provided but still works')
    
    assert os.path.isdir(unzip_path)


# Generated at 2022-06-13 18:54:50.679925
# Unit test for function unzip
def test_unzip():
    # unzip() should download a zip repository, unzip it, and return the path
    # to the unzipped repository.

    import shutil
    import os
    import requests
    from cookiecutter.zipfile import ZipFile
    from cookiecutter import utils
    from cookiecutter.utils import make_sure_path_exists
    from cookiecutter.prompt import prompt_and_delete
    from cookiecutter.exceptions import InvalidZipRepository
    from cookiecutter.repository import get_user_info

    # Create a test repository for this function
    # Build a directory for the test repository to live in
    temp_dir = tempfile.mkdtemp()

    # Create the zip file

# Generated at 2022-06-13 18:54:52.227198
# Unit test for function unzip
def test_unzip():
    assert unzip('cookiecutter-django/tests/test_files/fake-repo.zip', False)

# Generated at 2022-06-13 18:56:09.268182
# Unit test for function unzip
def test_unzip():
    import os
    import shutil
    import unittest
    from cookiecutter.utils import zipdir
    from cookiecutter import utils

    class TestUnzip(unittest.TestCase):

        def setUp(self):
            self.test_dir = os.path.join(
                os.path.dirname(__file__),
                'test_unzip'
            )
            self.empty_dir = os.path.join(
                os.path.dirname(__file__),
                'empty_dir'
            )
            self.empty_zipfile = os.path.join(
                os.path.dirname(__file__),
                'empty_zipfile.zip'
            )

# Generated at 2022-06-13 18:56:13.307038
# Unit test for function unzip
def test_unzip():
    repo_name = 'cookiecutter-pypackage'
    repo_url = 'https://github.com/audreyr/{0}/archive/master.zip'.format(repo_name)
    repo_path = unzip(repo_url, is_url=True)
    assert repo_path
    assert repo_path.endswith(repo_name)

# Generated at 2022-06-13 18:56:23.304203
# Unit test for function unzip
def test_unzip():
    """Unit test for the unzip function.

    This test case creates a zip file that contains a single directory
    with a single file. It then calls the unzip function to retrieve the
    file and make sure the contents are complete.

    This is a very simple test case, but it does exercise the basic
    functionality.
    """
    temp_dir = tempfile.mkdtemp()
    repo_dir = os.path.join(temp_dir, 'repo')
    readme_path = os.path.join(repo_dir, 'README.md')
    zip_path = os.path.join(temp_dir, 'test.zip')

    os.mkdir(repo_dir)
    with open(readme_path, 'w', encoding='utf-8') as readme:
        readme.write('README')



# Generated at 2022-06-13 18:56:30.532786
# Unit test for function unzip
def test_unzip():
    from requests.exceptions import HTTPError
    from unittest.mock import patch

    import cookiecutter

    with patch('cookiecutter.vcs.unzip.requests.get',
               side_effect=HTTPError()):
        with patch('cookiecutter.vcs.unzip.ZipFile',
                   side_effect=InvalidZipRepository()):
            assert cookiecutter.vcs.unzip.unzip(None, None, None)

    with patch('cookiecutter.vcs.unzip.requests.get',
               side_effect=HTTPError()):
        with patch('cookiecutter.vcs.unzip.ZipFile',
                   side_effect=BadZipFile()):
            assert cookiecutter.vcs.unzip.unzip(None, None, None)

# Generated at 2022-06-13 18:56:38.932855
# Unit test for function unzip
def test_unzip():
    """ Unit test for function unzip. """
    unzip_path = unzip('/Users/xiangxiao/Codes/cookiecutter-django_rest/cookiecutter-django_rest/tests/test-repo-template/new_name', False, clone_to_dir='.', no_input=False, password=None)
    assert unzip_path == '/var/folders/jt/gyq3ssj54tq3lh8p0nlsbxjm0000gn/T/tmpe8u2obf2/new_name'
    return

# Generated at 2022-06-13 18:56:48.273060
# Unit test for function unzip
def test_unzip():
    import pytest
    from cookiecutter.prompt import prompt_choice_ex
    from requests.exceptions import HTTPError

    # Prep for unit tests
    # Big thanks to https://gist.github.com/hrldcpr/2012250
    import shutil
    import stat
    import sys
    import zipfile

    def zip_subdir(path, zip_file, base_dir=None):
        base_dir = base_dir or os.path.basename(path)
        for root, dirs, files in os.walk(path):
            # add directory (needed for empty dirs)
            zip_file.write(root, os.path.join(base_dir, root[len(path) + 1 :]))
            for file in files:
                filename = os.path.join(root, file)

# Generated at 2022-06-13 18:56:56.135633
# Unit test for function unzip
def test_unzip():
    """
    Test that the unzip function works properly.
    """
    # Create a test archive
    import shutil
    import zipfile
    import tempfile
    import os

    # Create a temporary directory
    unzip_base = tempfile.mkdtemp()

    # Create an empty temp directory to serve as a project directory
    project_dir = tempfile.mkdtemp()

    # Create a file in the project directory
    with open(os.path.join(project_dir, 'file.txt'), 'w+') as f:
        f.write('file text')

    # Build a temporary zip file

# Generated at 2022-06-13 18:57:03.680875
# Unit test for function unzip
def test_unzip():
    """Test unzip()"""
    import tempfile
    import shutil
    import os
    import zipfile
    import requests
    import os
    import shutil

    tempdir = tempfile.mkdtemp()


# Generated at 2022-06-13 18:57:07.661128
# Unit test for function unzip
def test_unzip():
    result = unzip(zip_uri='/Users/peterdunn/mycookiecutter/mytemplate.zip', is_url=False)
    assert true

# Generated at 2022-06-13 18:57:14.103781
# Unit test for function unzip
def test_unzip():
    """Unit test for function unzip."""

    # test zip file created using
    #   $ zip -r test.zip test
    # where test is a dir containing:
    #   $ touch test/a.txt
    #   $ echo 'Hi' >> test/a.txt

    # add zip_uri

    # add unzip_path

    return 1
    # try to extract with wrong password
    # expect to raise InvalidZipRepository

    # try to extract with right password
    # expect it to work

    # try to extract with no password
    # expect to raise InvalidZipRepository

    # check that the test.zip file exists in unzip_path

# Generated at 2022-06-13 18:59:30.380000
# Unit test for function unzip
def test_unzip():
    os.mkdir('./repository')
    try:
        result = unzip('./test/test-repo.zip', "False", './repository', True)
        assert os.path.isdir('./repository/test-repo')
    finally:
        os.remove('./repository/test-repo')
        os.rmdir('./repository')

# Generated at 2022-06-13 18:59:31.380708
# Unit test for function unzip
def test_unzip():
    test = unzip('../tests/test-unzip/',True,'./')
    print(test)

# Generated at 2022-06-13 18:59:31.881270
# Unit test for function unzip
def test_unzip():
    pass

# Generated at 2022-06-13 18:59:43.384957
# Unit test for function unzip
def test_unzip():
    import glob
    import shutil
    tmpdir = tempfile.mkdtemp()

# Generated at 2022-06-13 18:59:53.151771
# Unit test for function unzip
def test_unzip():
    import subprocess

    def _get_test_data_zip_file(zip_uri):
        """Download and unpack the test-data archive.

        :param zip_uri: The URI for the zipfile.
        """
        # Build the name of the cached zipfile,
        # and prompt to delete if it already exists.
        identifier = zip_uri.rsplit('/', 1)[1]
        zip_path = os.path.join('/tmp', identifier)

        if os.path.exists(zip_path):
            subprocess.call(['rm', '-f', zip_path])

        # Download the zipfile
        r = requests.get(zip_uri, stream=True)