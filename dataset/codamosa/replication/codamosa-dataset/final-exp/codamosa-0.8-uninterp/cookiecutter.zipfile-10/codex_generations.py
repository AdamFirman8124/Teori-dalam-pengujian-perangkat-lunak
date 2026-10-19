

# Generated at 2022-06-13 18:50:10.718955
# Unit test for function unzip
def test_unzip():
    def mock_make_sure_path_exists(path):
        print("creating dir: {0}".format(path))
    
    def mock_prompt_and_delete(path, no_input=False):
        if no_input:
            return True
        else:
            return False
    
    def mock_read_repo_password(msg):
        password = input("{0}: ".format(msg))
        return password

    # Note: Change this to your own url that has a zip file.
    url = 'https://github.com/ly-wang/python-package-example/archive/python-package-example-v0.0.2.zip'
    
    orig_make_sure_path_exists = make_sure_path_exists
    orig_prompt_and_delete = prompt_and_

# Generated at 2022-06-13 18:50:16.029504
# Unit test for function unzip
def test_unzip():
    import subprocess
    import shutil
    import os

    test_dir = os.path.join(os.path.dirname(__file__), 'test_dir')
    test_zip = os.path.join(test_dir, 'test.zip')
    ref_dir = os.path.join(test_dir, 'test_dir')
    download_path = unzip(test_zip, False, test_dir)
    try:
        assert os.path.exists(download_path)
        assert os.path.isdir(download_path)
        subprocess.check_call(['diff', '-rN', '-x', '"__pycache__"', ref_dir,
                               download_path])
    finally:
        shutil.rmtree(download_path)

# Generated at 2022-06-13 18:50:25.056439
# Unit test for function unzip
def test_unzip():
    """Test function unzip by using real cookies and dirs"""
    from cookiecutter.main import cookiecutter  #import cookiecutter
    from cookiecutter.config import get_user_config
    from cookiecutter.utils import work_in
    import os
    import shutil
    import hashlib

    config_file = get_user_config()

    base_dir = os.getcwd()
    tmp_zip_path = os.path.expanduser(os.path.join('~', 'tmp_cookiecutter.zip'))
    tmp_dir = '/tmp/cookiecutter_git_repo_test'

    # Create a git repo with test cookiecutter first
    with work_in(tmp_dir):
        repo_dir = cookiecutter('tests/test-extended-cookiecutter')

        # Zip

# Generated at 2022-06-13 18:50:30.379697
# Unit test for function unzip
def test_unzip():
    import shutil
    import tempfile
    import zipfile

    from cookiecutter.main import cookiecutter

    sdir = 'tests/fake-repo-tmpl'
    tmpdir = tempfile.mkdtemp()
    zipf = os.path.join(sdir, 'fake-repo-tmpl.zip')
    tmpl = os.path.join(tmpdir, 'fake-repo-tmpl')
    tmpl_dir = os.path.join(tmpl, '{{cookiecutter.repo_name}}')
    shutil.make_archive(tmpl, 'zip', sdir)
    loading_dir = unzip(zipf, False)
    search_dir = os.path.basename(zipf).split('-')[0]
    cwd = os.getcwd()


# Generated at 2022-06-13 18:50:30.981420
# Unit test for function unzip
def test_unzip():
    pass

# Generated at 2022-06-13 18:50:37.062897
# Unit test for function unzip
def test_unzip():
    """
    Tests function unzip
    """
    clone_to_dir = os.path.expanduser(tempfile.mkdtemp())
    make_sure_path_exists(clone_to_dir)

    identifier = 'test.zip'
    zip_path = os.path.join(clone_to_dir, identifier)

    unzip_path = unzip(zip_path, False)
    assert(os.path.isdir(unzip_path))

# Generated at 2022-06-13 18:50:41.106455
# Unit test for function unzip
def test_unzip():
    assert unzip(zip_uri = 'tests/test-repo/', is_url = False, clone_to_dir='.', no_input=True, password=None)

# Generated at 2022-06-13 18:50:43.347430
# Unit test for function unzip
def test_unzip():
    """Test of unzip function."""
    assert os.path.isdir(unzip('tests/test-repo-pre/', False))
    assert os.path.isdir(unzip('tests/test-repo-pre/', False))

# Generated at 2022-06-13 18:50:50.981771
# Unit test for function unzip
def test_unzip():
    repo_url = 'https://github.com/audreyr/cookiecutter-pypackage/archive/master.zip'
    is_url = True
    # Empty dir, except for this file
    clone_to_dir = os.path.dirname(__file__)
    no_input = True
    password = None
    print("unzip({}, {}, {}, {}, {}, {})".format(
        repo_url, is_url, clone_to_dir, no_input, password
    ))
    # This should pass
    print("  Should pass: ")
    unzip_path = unzip(
        repo_url, is_url, clone_to_dir, no_input, password
    )
    assert unzip_path.startswith('/tmp/')
    # assert os.path.isd

# Generated at 2022-06-13 18:50:51.711190
# Unit test for function unzip
def test_unzip():
    assert False

# Generated at 2022-06-13 18:51:03.306487
# Unit test for function unzip
def test_unzip():
    """Make sure function unzip() works."""
    import pytest
    import requests
    import tarfile
    import zipfile
    import os
    import shutil
    def download(url: str, filename: str):
        """Mock requests.get method"""
        with open(filename, 'wb') as f:
            f.write(requests.get(url).content)

    if __name__ == '__main__':
        test_url = 'https://github.com/datascienceinc/cookiecutter-data-science/archive/1.1.0.zip'
        test_zip_url = 'https://github.com/datascienceinc/cookiecutter-data-science/archive/1.1.0.zip'
        test_cookie_zip = 'cookie.zip'

# Generated at 2022-06-13 18:51:04.229053
# Unit test for function unzip
def test_unzip():
    import pytest
    # TODO test this function.
    assert False

# Generated at 2022-06-13 18:51:06.223046
# Unit test for function unzip
def test_unzip():
    test_unzip.unzip = unzip("https://github.com/audreyr/cookiecutter-pypackage/archive/master.zip", True)
    if os.path.exists("test_unzip.unzip"):
        assert True
    else:
        assert False

# Generated at 2022-06-13 18:51:16.956791
# Unit test for function unzip
def test_unzip():
    import pytest
    from cookiecutter.utils import rmtree

    # Test with an archive that is not a valid zipfile
    with pytest.raises(InvalidZipRepository):
        unzip('tests/test-invalid-zip/invalid-zip.zip', is_url=False)

    # Test with an valid zipfile that does not have a top-level directory
    with pytest.raises(InvalidZipRepository):
        unzip('tests/test-invalid-zip/no-top-level-dir.zip', is_url=False)

    # Test with a valid empty zipfile
    with pytest.raises(InvalidZipRepository):
        unzip('tests/test-invalid-zip/empty-zip.zip', is_url=False)

    # Test with a valid zipfile that contains a password
    password

# Generated at 2022-06-13 18:51:21.108866
# Unit test for function unzip
def test_unzip():
    is_url = True
    #zip_uri = 'https://github.com/audreyr/cookiecutter-pypackage/archive/master.zip'
    zip_uri = 'https://github.com/audreyr/cookiecutter-pypackage/archive/0.0.0.zip'
    print('zip_uri =' , zip_uri)
    unzip(zip_uri, is_url)

# Generated at 2022-06-13 18:51:24.976956
# Unit test for function unzip
def test_unzip():
    from cookiecutter.tests import mock_zip_url
    from cookiecutter.config import DEFAULT_CONFIG
    import shutil

    unzip_path = unzip(mock_zip_url, is_url=True, **DEFAULT_CONFIG)
    assert os.path.exists(unzip_path)
    assert os.listdir(unzip_path)
    shutil.rmtree(unzip_path)


# Generated at 2022-06-13 18:51:36.194210
# Unit test for function unzip
def test_unzip():
    import logging
    import shutil

    from .contextmanagers import our_directory
    from .prompt import FakeReply

    tmpd = tempfile.gettempdir()
    log = logging.getLogger('cookiecutter')
    log.setLevel(logging.DEBUG)

    with our_directory(tmpd) as clone_to_dir, our_directory(tmpd) as test_dir:
        clone_to_dir = os.path.join(clone_to_dir, 'cookiecutter')
        os.mkdir(clone_to_dir)
        os.chdir(clone_to_dir)
        # Build a _simple_ zipfile by hand.
        with ZipFile('test1.zip', 'w') as zf:
            zf.writestr('top/', '')
            zf.writestr

# Generated at 2022-06-13 18:51:38.232734
# Unit test for function unzip
def test_unzip():
    unzip('./Tests/test-repo-pre/test-repo-zip', is_url=False, clone_to_dir='.', no_input=True, password=None)

# Generated at 2022-06-13 18:51:41.046776
# Unit test for function unzip
def test_unzip():
    pass

if __name__ == '__main__':
    test_unzip()

# Generated at 2022-06-13 18:51:51.794219
# Unit test for function unzip
def test_unzip():
    import unittest
    import shutil
    import os
    import filecmp
    # Create temporary test folder
    current_directory = os.path.dirname(os.path.realpath(__file__))
    temp_directory = os.path.join(current_directory,'test_unzip')

# Generated at 2022-06-13 18:52:06.050680
# Unit test for function unzip
def test_unzip():
    uri = 'https://github.com/abhirama/cookiecutter-matlab/archive/master.zip'
    is_url = True
    no_input = True
    clone_to_dir = '.'
    temp_dir = unzip(uri, is_url, clone_to_dir, no_input)
    assert temp_dir is not None
    assert os.path.isdir(temp_dir)
    os.rmdir(temp_dir)
    return

# Generated at 2022-06-13 18:52:16.004044
# Unit test for function unzip
def test_unzip():
    import codecs
    #from unittest import skip
    from zipfile import ZipFile

    #@skip('development')
    def test_zip_without_password():
        '''
        Tests for the unzip function.

        We do this by creating a zip file that does not include a password,
        and then testing for the presence of one of the files in the archive.

        This test fails if the file is not found.
        '''
        #os.path.expanduser(clone_to_dir)
        #make_sure_path_exists(clone_to_dir)
        # Get the path of the file that we will put in the test zip file

# Generated at 2022-06-13 18:52:26.987401
# Unit test for function unzip
def test_unzip():
    import shutil
    import zipfile
    import requests
    import tempfile
    from .config import DEFAULT_CONFIG, find_cookiecutters
    from .prompt import read_repo_password
    from .utils import (
        make_sure_path_exists,
        prompt_and_delete,
    )

    # First, check the case of a zip file with a top-level directory
    # Create a temporary zip file with a top-level directory
    tmp_template_dir = tempfile.mkdtemp()
    template_name = 'test_template'
    top_level_tmp_template = os.path.join(tmp_template_dir, template_name)
    make_sure_path_exists(top_level_tmp_template)

# Generated at 2022-06-13 18:52:28.897520
# Unit test for function unzip
def test_unzip():
    print(unzip('/Users/jasender/Desktop/TEST.zip', False))
    assert True

# Generated at 2022-06-13 18:52:37.080281
# Unit test for function unzip
def test_unzip():
    """Test function unzip."""
    import shutil
    from cookiecutter import __version__ as cookiecutter_version

    dir_path = os.path.dirname(os.path.realpath(__file__))
    test_template_path = os.path.join(dir_path, '..', 'tests', 'test-template')
    zip_path = os.path.join(dir_path, '..', 'tests', 'test-template.zip')
    unzip_path = unzip(
        zip_uri=zip_path, is_url=False, no_input=True
    )
    assert unzip_path == test_template_path


# Generated at 2022-06-13 18:52:38.728458
# Unit test for function unzip
def test_unzip():
    unzip('test_cookiecutter/test_unzip/test_zip.zip', False)

# Generated at 2022-06-13 18:52:53.729614
# Unit test for function unzip
def test_unzip():
    from os import path
    from zipfile import ZipFile
    from shutil import rmtree
    from tempfile import mktemp
    from zipfile import ZIP_DEFLATED
    from zipfile import ZIP_STORED

    def zipfile(compress_type, files):
        temp_zip = ZipFile(mktemp(prefix='cookiecutter-', suffix='.zip'), 'w')
        for f in files:
            temp_zip.write(f, compress_type=compress_type)
        temp_zip.close()
        return temp_zip.filename

    def delete(files):
        for f in files:
            if path.isfile(f):
                os.remove(f)
            elif path.isdir(f):
                rmtree(f)


# Generated at 2022-06-13 18:53:02.014742
# Unit test for function unzip
def test_unzip():
    """
    Unit test for function unzip

    :return:
    """
    import sys
    sys.path.append('./cookiecutter')
    from pytest import fixture
    import shutil

    zip_url = 'https://github.com/iammukul/cookiecutter-flutter-app/archive/master.zip'

    @fixture
    def zippath(tmpdir):
        return os.path.join(str(tmpdir), 'test.zip')

    @fixture
    def unzippath(tmpdir):
        return os.path.join(str(tmpdir), 'test')

    @fixture
    def zippath2(tmpdir):
        return os.path.join(str(tmpdir), 'test2.zip')


# Generated at 2022-06-13 18:53:09.993103
# Unit test for function unzip
def test_unzip():
    """Test unzip function."""
    from zipfile import ZipFile
    from io import BytesIO

    content = b'{"cookiecutter":{"foo": "bar"}}'

    buf = BytesIO()

    with ZipFile(buf, 'w') as z:
        z.writestr("testing/cookiecutter.json", content)

    buf.seek(0)
    path = unzip(zip_uri=buf, is_url=False)
    assert os.path.isfile(os.path.join(path, 'cookiecutter.json'))



# Generated at 2022-06-13 18:53:11.264238
# Unit test for function unzip
def test_unzip():
    """Unit tests for function unzip."""
    pass

# Generated at 2022-06-13 18:53:25.282695
# Unit test for function unzip
def test_unzip():
    import contextlib
    import requests_mock
    import shutil
    import tempfile
    import zipfile

    @contextlib.contextmanager
    def create_zip():
        zip_path = tempfile.mktemp()
        zip_file = zipfile.ZipFile(zip_path, 'w')
        zip_file.write('cookiecutter.json', '{{cookiecutter.project_name}}/cookiecutter.json')
        zip_file.close()
        try:
            yield zip_path
        finally:
            os.remove(zip_path)


# Generated at 2022-06-13 18:53:30.801123
# Unit test for function unzip
def test_unzip():
    clone_to_dir='./';
    zip_uri = 'https://github.com/kam1n0/cookiecutter-matlab-class/archive/master.zip';
    return unzip(zip_uri, is_url=True, clone_to_dir=clone_to_dir, no_input=True, password=None)

# Generated at 2022-06-13 18:53:39.227037
# Unit test for function unzip
def test_unzip():
    import shutil
    import zipfile

    # Create a dummy zip file
    zip_path = os.path.join(os.path.expanduser('~'), 'cookiecutter.zip')
    if os.path.exists(zip_path):
        os.remove(zip_path)
    if not os.path.exists(zip_path):
        with zipfile.ZipFile(zip_path, 'w') as test_zip:
            test_zip.writestr('test', b'A test')

    # Define the test uri
    test_uri = 'file:{}'.format(zip_path)

    # Create a temporary directory to store the zip file
    tmp_dir = tempfile.mkdtemp()

    # Run the test

# Generated at 2022-06-13 18:53:40.675495
# Unit test for function unzip
def test_unzip():
    """Test for function unzip."""
    pass

# End function test_unzip

# Generated at 2022-06-13 18:53:41.314640
# Unit test for function unzip
def test_unzip():
    assert 1 == 1

# Generated at 2022-06-13 18:53:51.829022
# Unit test for function unzip
def test_unzip():
    import os.path
    import tempfile
    import shutil
    import sys

    unzip_path = None
    clone_to_dir = None
    password = None


# Generated at 2022-06-13 18:53:54.457887
# Unit test for function unzip
def test_unzip():
    unzip_path = unzip('/tmp/file.zip', False)
    assert isinstance(unzip_path, basestring)

# Generated at 2022-06-13 18:54:02.131208
# Unit test for function unzip
def test_unzip():
    import pytest
    import sys
    import os
    import shutil
    import requests
    import zipfile

    # create fake file
    os.chdir(os.path.dirname(__file__))
    temp_dir = tempfile.mkdtemp()
    os.chdir(temp_dir)
    new_zip = 'test_unzip_archive.zip'

    # test url downloading
    url = 'https://github.com/audreyr/cookiecutter-pypackage/zipball/master'
    unzip(url, True, no_input=True)
    assert os.path.isdir(os.path.join(temp_dir, 'audreyr-cookiecutter-pypackage-*'))

    # test file downloading
    # create a fake zipfile

# Generated at 2022-06-13 18:54:10.602108
# Unit test for function unzip
def test_unzip():
    import shutil
    tmp_dir = tempfile.mkdtemp()
    # Clone repository to a temporary directory
    unzip_path = unzip('https://github.com/audreyr/cookiecutter-pypackage/zipball/master', True, clone_to_dir=tmp_dir)
    # Test we have created a directory in the temporary directory
    assert os.path.isdir(unzip_path)
    # Remove temporary directory
    shutil.rmtree(unzip_path)
    os.rmdir(tmp_dir)

# Generated at 2022-06-13 18:54:18.069821
# Unit test for function unzip
def test_unzip():
    """Unit test for unzip()"""
    file_name = "testfile.zip"
    clone_to_dir = tempfile.mkdtemp()
    zip_path = os.path.join(clone_to_dir, file_name)
    r = requests.get("https://github.com/audreyr/cookiecutter/archive/master.zip", stream=True)
    with open(zip_path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
    zip_file = ZipFile(zip_path)
    if len(zip_file.namelist()) == 0:
        raise Exception('Zip repository {} is empty'.format(zip_path))

    # The first record in

# Generated at 2022-06-13 18:54:50.066733
# Unit test for function unzip
def test_unzip():
    import shutil
    import random
    import string
    random_path=''.join(random.choice(string.ascii_uppercase) for _ in range(5))
    zip_path=os.path.join('/tmp',random_path)
    os.system('mkdir '+zip_path)
    unzip_path=unzip('https://github.com/audreyr/cookiecutter-pypackage/archive/master.zip',True,clone_to_dir=zip_path,no_input=True)
    assert os.path.exists(unzip_path)
    shutil.rmtree(zip_path)

# Generated at 2022-06-13 18:55:00.457786
# Unit test for function unzip
def test_unzip():
    import zipfile 
    import os
    import shutil
    from random import randint
    from six.moves.urllib.request import urlopen
    from six.moves.urllib.parse import urlunparse
    from cookiecutter.main import cookiecutter

    zip_url = urlunparse(('https', 'github.com', '/audreyr/cookiecutter-pypackage/archive/master.zip', '', '', ''))
    r = requests.get(zip_url, stream=True)
    with open('test_archive.zip', 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
    

# Generated at 2022-06-13 18:55:01.261303
# Unit test for function unzip
def test_unzip():
    pass

# Generated at 2022-06-13 18:55:02.497527
# Unit test for function unzip
def test_unzip():
    # TODO: write unit test
    pass

# Generated at 2022-06-13 18:55:11.862358
# Unit test for function unzip
def test_unzip():
    import pytest
    from cookiecutter.utils import rmtree
    from cookiecutter import main
    
    # test to get zip from a URL
    no_input = True
    unzip_path = unzip('http://github.com/audreyr/cookiecutter-pypackage/archive/master.zip', True, 'tests/test-unzip', no_input=no_input, password=None)
    # unzip_path is not None
    assert unzip_path is not None
    # function main should work fine
    main.cookiecutter(
        'tests/test-unzip/cookiecutter-pypackage-master',
        no_input=True,
        extra_context={'full_name': 'Oscar Bluth', 'project_name': 'banana'},
    )
    # Files

# Generated at 2022-06-13 18:55:12.506309
# Unit test for function unzip
def test_unzip():

    assert True

# Generated at 2022-06-13 18:55:20.099945
# Unit test for function unzip
def test_unzip():
    assert os.path.isfile('test_unzip/unzipme.zip')
    unzip_path = unzip('test_unzip/unzipme.zip', False)
    assert os.path.isdir(unzip_path)
    assert os.path.isdir(unzip_path + '/unzipme')
    assert os.path.isfile(unzip_path + '/unzipme/.gitignore')
    assert os.path.isfile(unzip_path + '/unzipme/README.md')
    assert os.path.isfile(unzip_path + '/unzipme/hooks/pre_gen_project.py')
    assert os.path.isfile(unzip_path + '/unzipme/{{cookiecutter.repo_name}}/__init__.py')

# Generated at 2022-06-13 18:55:30.748685
# Unit test for function unzip
def test_unzip():
    import os
    import pytest
    import requests
    import shutil
    import tempfile
    import zipfile
    from cookiecutter.main import cookiecutter
    from cookiecutter.utils import rmtree
    from cookiecutter.prompt import read_repo_password
    
    repo_folder = tempfile.mkdtemp()
    repo_url = 'https://github.com/audreyr/cookiecutter-pypackage/archive/master.zip'
    
    # test that unzip works with a regular repository
    template_folder  = unzip(repo_url, True, repo_folder)
    assert os.path.exists(template_folder)
    
    # test that unzip works with a protected repository

# Generated at 2022-06-13 18:55:40.133460
# Unit test for function unzip
def test_unzip():
    import shutil
    import sys
    import tempfile

    # Build a temporary directory.
    temp_dir = tempfile.mkdtemp()
    clone_to_dir = os.path.join(temp_dir, 'cookiecutter')

    # Build a test repo that is a zip archive.
    test_repo_name = 'test-zip-repo'
    test_repo_dir = os.path.join(temp_dir, test_repo_name)
    os.makedirs(test_repo_dir)

    zip_repo_path = os.path.join(temp_dir, '{}.zip'.format(test_repo_name))
    zip_file = ZipFile(zip_repo_path, 'w')

# Generated at 2022-06-13 18:55:40.661246
# Unit test for function unzip
def test_unzip():
    pass

# Generated at 2022-06-13 18:56:30.733528
# Unit test for function unzip
def test_unzip():
    assert os.path.isdir(unzip('tests/test-repo.zip', False))

# Generated at 2022-06-13 18:56:40.603369
# Unit test for function unzip
def test_unzip():
    import shutil
    import zipfile
    import tempfile
    from cookiecutter.utils import rmtree

    test_dir = tempfile.mkdtemp()
    repo_dir = os.path.join(test_dir, 'myrepo')
    zip_path = os.path.join(test_dir, 'zipper.zip')

    try:
        zip_file = zipfile.ZipFile(zip_path, 'w')
        zip_file.write(__file__, 'yupfile.py')
        zip_file.close()

        print(unzip(zip_path, False))
    finally:
        shutil.rmtree(test_dir)

if __name__ == '__main__':
    test_unzip()

# Generated at 2022-06-13 18:56:50.066518
# Unit test for function unzip
def test_unzip():
    import os, shutil, tempfile, textwrap
    from zipfile import ZipFile
    from cookiecutter.utils import unzip

    tempdir = tempfile.mkdtemp()
    try:
        zip_path = os.path.join(tempdir, 'test.zip')
        with open(zip_path, 'wb') as f:
            zf = ZipFile(f, 'w')
            zf.writestr('test/temp.txt', str(os.getpid()))
            zf.close()
        unzip_path = unzip(zip_path, is_url=False)
        assert os.path.exists(os.path.join(unzip_path, 'temp.txt'))
    except Exception:
        raise
    finally:
        shutil.rmtree(tempdir)


# Generated at 2022-06-13 18:56:57.571335
# Unit test for function unzip
def test_unzip():
    """Verify that unzip is able to correctly unpack a repository archive."""
    from .repo import get_repo

    # Get the repository
    cookiecutter_json = get_repo(
        repo_url='https://github.com/audreyr/cookiecutter-pypackage.git',
        checkout='0.3.0',
        no_input=True
    )
    repo_dir, cleanup_repo = cookiecutter_json
    name = os.path.basename(repo_dir)

    # Verify that the repo unzips correctly and looks as it should
    repo_uri = os.path.join(repo_dir, '{}.zip'.format(name))
    zip_path = unzip(zip_uri=repo_uri, is_url=False)

    # Do some basic

# Generated at 2022-06-13 18:57:04.329057
# Unit test for function unzip

# Generated at 2022-06-13 18:57:14.372331
# Unit test for function unzip
def test_unzip():
    import os
    import shutil
    import tempfile
    import zipfile
    
    # Create temporary directory to store the zip file
    clone_to_dir = tempfile.mkdtemp()
    # Create zip file
    identifier = '12345'
    zip_path = os.path.join(clone_to_dir, identifier)
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
        z.write(__file__) 
    is_url = False
    no_input = True
    password = None
    
    # Do the the unzip 

# Generated at 2022-06-13 18:57:26.942937
# Unit test for function unzip
def test_unzip():
    """
    Make sure that the function unzip can be used for
    both local files and remote URLs.
    """
    # Test zip archive from local file
    zip_uri = 'test.zip'
    is_url = False
    clone_to_dir = '.'
    no_input = False
    password = None
    unzip(zip_uri, is_url, clone_to_dir, no_input, password)

    # Test zip archive from remote file
    zip_uri = 'http://www.sample-videos.com/zip/10mb.zip'
    is_url = True
    clone_to_dir = '.'
    no_input = False
    password = None
    unzip(zip_uri, is_url, clone_to_dir, no_input, password)

# Generated at 2022-06-13 18:57:28.438004
# Unit test for function unzip
def test_unzip():
    # Check with valid parameters
    unzip('test.zip')


# Generated at 2022-06-13 18:57:40.867000
# Unit test for function unzip
def test_unzip():
    """
    Test to make sure the function unzips a .zip file
    """
    import random
    from cookiecutter.utils import rmtree
    from shutil import copyfile
    import sys
    import unittest

    class TestUnzip(unittest.TestCase):
        
        def setUp(self):
            self.zip_uri = os.path.join(os.path.dirname(__file__),'fixtures', 'fake_repo.zip')
            self.clone_to_dir = tempfile.mkdtemp()
            self.download_repo_to = os.path.join(self.clone_to_dir, 'fake_repo.zip')
            random_dir = str(random.randint(1,100))

# Generated at 2022-06-13 18:57:49.022811
# Unit test for function unzip
def test_unzip():
    from plumbum import local
    from cookiecutter.compat import TemporaryDirectory

    def mock_requests_get(url, stream=None):
        return open(os.path.join(local.cwd, "tests", "test-repo.zip"), "rb")

    with TemporaryDirectory() as tmpdir:
        local.cwd.chdir() # Change to tmpdir
        with open("repo-urls.txt", "w") as fh:
            fh.write("https://github.com/audreyr/cookiecutter/archive/master.zip")

        # Mock requests
        import sys
        import requests as _requests
        import __builtin__

        original_get = _requests.get
        _requests.get = mock_requests_get
        sys.modules['__builtin__'].raw