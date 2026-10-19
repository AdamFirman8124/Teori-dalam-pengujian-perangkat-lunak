

# Generated at 2022-06-13 18:50:11.154718
# Unit test for function unzip
def test_unzip():
    import pytest
    import subprocess

    # Test url and file with correct repo
    correct_url = 'https://github.com/audreyr/cookiecutter-pypackage/archive/master.zip'
    correct_file = 'audreyr/cookiecutter-pypackage/archive/master.zip'
    correct_password = 'testpassword'

    # Test url and file with incorrect repo
    incorrect_url = 'https://github.com/audreyr/cookiecutter-pypackage/archive/master'
    incorrect_file = 'audreyr/cookiecutter-pypackage/archive/master'

    # Test password protected zipfile

# Generated at 2022-06-13 18:50:17.615883
# Unit test for function unzip
def test_unzip():
    import tempfile
    import zipfile
    from cookiecutter.main import cookiecutter
    from os import path
    from shutil import rmtree

    original_dir = path.realpath(path.curdir)
    temp_dir = tempfile.mkdtemp()


# Generated at 2022-06-13 18:50:25.411283
# Unit test for function unzip
def test_unzip():
    from cookiecutter import prompt
    import zipfile
    import tempfile
    import os

    with tempfile.TemporaryDirectory() as tmpdirname:
        os.makedirs('{}/cookiecutter/'.format(tmpdirname))
        with open('{}/cookiecutter/test.txt'.format(tmpdirname), 'w') as zip_test:
            zip_test.write('test file')
        zip_file = zipfile.ZipFile(
            '{}/cookiecutter/test_zip.zip'.format(tmpdirname),
            'w',
            compression=zipfile.ZIP_DEFLATED,
        )

# Generated at 2022-06-13 18:50:36.524162
# Unit test for function unzip
def test_unzip():
    import os
    import pytest
    from zipfile import ZipFile, is_zipfile

    from cookiecutter.utils import unzip

    class Archive:
        """Fake archive with common tests"""

        is_url = False
        clone_to_dir = None
        no_input = True
        password = None

        def __init__(self, zip_uri):
            self.zip_uri = zip_uri

        def test(self):
            unzip_path = unzip(
                zip_uri=self.zip_uri,
                is_url=self.is_url,
                clone_to_dir=self.clone_to_dir,
                no_input=self.no_input,
                password=self.password,
            )
            assert os.path.isdir(unzip_path)
            assert os.list

# Generated at 2022-06-13 18:50:48.023818
# Unit test for function unzip
def test_unzip():
    def mockget(url, stream=True):
        class Content(object):
            def __init__(self,content):
                self.content = content

            def iter_content(self,chunk_size):
                return (c for c in self.content)

        return Content([b'test',b'content'])

    def mockread(prompt):
        return 'test'

    with tempfile.TemporaryDirectory() as root:
        test_url = "http://example.com/test.zip"
        test_path = root + "/test.zip"
        backup,requests.get = requests.get,mockget
        backupread,cookiecutter.prompt.read_repo_password = \
                cookiecutter.prompt.read_repo_password,mockread

# Generated at 2022-06-13 18:50:51.527927
# Unit test for function unzip
def test_unzip():
    zip_uri='https://github.com/audreyr/cookiecutter-pypackage/archive/0.6.0.zip'
    unzip(zip_uri,True)
# End unit test

# Generated at 2022-06-13 18:50:53.803372
# Unit test for function unzip
def test_unzip():
    unzip('test_archive/test_archive.zip', False, clone_to_dir='./test_archive')

# Generated at 2022-06-13 18:51:04.768271
# Unit test for function unzip
def test_unzip():

    #Test url
    url = 'https://github.com/audreyr/cookiecutter-pypackage/archive/master.zip'
    assert type(unzip(url, True)) == str

    #Test local path
    assert type(unzip(url, False)) == str

    #Test invalid path
    try:
        invalid_url = 'http://github.com/audreyr/cookiecutter-pypackage/archive/master.zip'
        unzip(invalid_url, True)
        assert False
    except InvalidZipRepository:
        assert True

    #Test password protected zip file
    protected_url = 'https://github.com/cookiecutter/cookiecutter/raw/master/test_utils/test_protected_zip.zip'

# Generated at 2022-06-13 18:51:09.467801
# Unit test for function unzip
def test_unzip():
    # Unit test that tests unzip
    import pytest
    import os
    import shutil

    # Create a temporary directory to store the archive
    temp_dir = tempfile.mkdtemp()

    # Create a dummy zip file
    target_zip_file_name = os.path.join(temp_dir, 'test_zip_file.zip')

    # Open the zip file, and add a dummy file.
    target_zip_file = ZipFile(target_zip_file_name, 'w')

    # Add a single file, with a single line of content, to the zip file.
    filename = 'test_file.txt'
    original_contents = 'test_file_content'
    zipfile_entry = 'test_zip_file/test_file.txt'

# Generated at 2022-06-13 18:51:19.239914
# Unit test for function unzip
def test_unzip():
    import zipfile
    import shutil
    import os
    import tempfile
    import requests
    import os.path
    from contextlib import contextmanager

    @contextmanager
    def temp_directory():
        tmppath = tempfile.mkdtemp()
        yield tmppath
        shutil.rmtree(tmppath)

    def create_temp_zip(sources):
        with temp_directory() as tmppath:
            zip_path = os.path.join(tmppath, 'temp.zip')
            zf = zipfile.ZipFile(zip_path, mode='w')
            for source in sources:
                zf.write(source, os.path.basename(source))
            return zip_path


# Generated at 2022-06-13 18:51:25.946600
# Unit test for function unzip
def test_unzip():
    pass

# Generated at 2022-06-13 18:51:36.644107
# Unit test for function unzip
def test_unzip():
    file_path = os.path.abspath(os.path.join(
        os.path.dirname(__file__),
        '..',
        '..',
        'tests',
        'test-repo-pre/',
        '{{cookiecutter.repo_name}}.zip'
    ))

    unzip_path = unzip(
        zip_uri=file_path,
        is_url=0,
        clone_to_dir = os.path.abspath(os.path.join(
            os.path.dirname(__file__),
            '..',
            '..',
            'tests',
            'test-repo-pre'
        )),
        no_input=1,
        password=None
    )
    files = os.listdir(unzip_path)

# Generated at 2022-06-13 18:51:37.424596
# Unit test for function unzip
def test_unzip():
    pass

# Generated at 2022-06-13 18:51:42.279056
# Unit test for function unzip
def test_unzip():
    repo = "https://github.com/audreyr/cookiecutter-pypackage/archive/master.zip"
    zip_uri = unzip(repo, True)
    assert os.path.exists(zip_uri) is True

# Generated at 2022-06-13 18:51:51.897494
# Unit test for function unzip
def test_unzip():
    test_uri = "https://github.com/audreyr/cookiecutter-pypackage/archive/master.zip"
    test_path = os.path.join(tempfile.mkdtemp(), "master.zip")

    r = requests.get(test_uri, stream=True)
    with open(test_path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)

    unzip_path = unzip(test_path, False)

    assert os.path.isdir(unzip_path)
    assert "setup.py" in os.listdir(unzip_path)

# Generated at 2022-06-13 18:52:05.009697
# Unit test for function unzip
def test_unzip():
    import shutil
    import zipfile
    import requests
    import tempfile
    from cookiecutter.utils import make_sure_path_exists

    clone_to_dir = tempfile.mkdtemp()
    make_sure_path_exists(clone_to_dir)

    identifier = 'cookiecutter-pypackage-test.zip'
    zip_path = os.path.join(clone_to_dir, identifier)
    url = 'https://codeload.github.com/audreyr/cookiecutter-pypackage/zip/master'

    r = requests.get(url, stream=True)

# Generated at 2022-06-13 18:52:15.491910
# Unit test for function unzip
def test_unzip():
    import pytest
    unzip_path = unzip(zip_uri="http://www.erikasarti.net/efs-template.zip",
                       is_url=True)
    assert unzip_path is not None
    assert os.path.exists(unzip_path)
    assert os.path.isdir(unzip_path)
    assert os.path.exists(os.path.join(unzip_path, 'template'))
    assert os.path.isdir(os.path.join(unzip_path, 'template'))

    # Check that password protected repos work

# Generated at 2022-06-13 18:52:20.144227
# Unit test for function unzip
def test_unzip():
    zip_uri = 'https://github.com/yehyang/cookiecutter-pypackage/archive/master.zip'
    unzip(zip_uri, True)

if __name__ == '__main__':
    test_unzip()

# Generated at 2022-06-13 18:52:28.652219
# Unit test for function unzip
def test_unzip():
    import shutil
    from cookiecutter.prompt import read_user_yes_no
    from cookiecutter.utils import rmtree

    # Test simple case of unzipping a local repo
    local_zip_path = os.path.join(
        os.path.dirname(__file__), '..', '..', 'tests', 'test-repo-tmpl-pre.zip'
    )
    clone_to_dir = tempfile.mkdtemp()
    unzip_path = unzip(local_zip_path, False, clone_to_dir=clone_to_dir)
    assert os.path.isdir(os.path.join(unzip_path, 'hooks'))
    assert os.path.isfile(os.path.join(unzip_path, 'README.md'))

   

# Generated at 2022-06-13 18:52:32.721655
# Unit test for function unzip
def test_unzip():
    ret_val = unzip("https://github.com/audreyr/cookiecutter-pypackage/archive/master.zip", is_url=True, no_input=True)
    assert os.path.isdir(ret_val)
    assert len(os.listdir(ret_val)) != 0

# Generated at 2022-06-13 18:52:42.062859
# Unit test for function unzip
def test_unzip():
    return 1
    # assert unzip('url|master.zip', 'env', 'cookiecutter') == 1

if __name__ == '__main__':
    test_unzip()

# Generated at 2022-06-13 18:52:57.033815
# Unit test for function unzip
def test_unzip():
    import shutil

    temp_dir = tempfile.mkdtemp()
    clone_to_dir = os.path.join(temp_dir, "clone")
    os.mkdir(clone_to_dir)


# Generated at 2022-06-13 18:52:58.136241
# Unit test for function unzip
def test_unzip():
    # Pytest test case
    assert 0 == 0


# Generated at 2022-06-13 18:53:01.774642
# Unit test for function unzip
def test_unzip():
    import shutil
    from cookiecutter.main import cookiecutter
    zip_uri = 'https://github.com/hadi/cookiecutter-pypackage-minimal/archive/master.zip'
    unzip_path = unzip(zip_uri, True, '.', True)
    shutil.rmtree(unzip_path)

# Generated at 2022-06-13 18:53:08.105571
# Unit test for function unzip
def test_unzip():
    test_zip_uri = "https://github.com/audreyr/cookiecutter-pypackage/archive/master.zip"
    test_is_url = True
    test_clone_to_dir = "/tmp/test-cookiecutter-repos"
    test_no_input = True
    test_password = None
    assert unzip(test_zip_uri, test_is_url, test_clone_to_dir, test_no_input, test_password) != ''

# Generated at 2022-06-13 18:53:17.669336
# Unit test for function unzip
def test_unzip():
    import json
    import shutil
    import requests_mock
    import requests
    import responses
    import os
    import sys
    import zipfile

    test_dir = os.path.dirname(os.path.abspath(__file__))
    responses.add(
        responses.GET,
        "http://example.com/malformed.zip",
        body=open(os.path.join(test_dir, 'malformed_archive.zip'), 'rb'),
        status=200,
        content_type='application/zip'
    )


# Generated at 2022-06-13 18:53:26.273838
# Unit test for function unzip
def test_unzip():
    import requests_mock
    import responses
    import pytest

    # Test repo zip file
    test_zip_url = 'https://github.com/audreyr/cookiecutter-pypackage/archive/master.zip'
    test_zip_file = 'tests/files/cookiecutter-pypackage-master.zip'
    test_password = 'Password1'
    test_password_bad = 'BadPassword'

    # Test unzip with a URL
    with requests_mock.Mocker() as m:
        m.register_uri('GET', test_zip_url, body=open(test_password_zipped, 'rb'))
        with pytest.raises(InvalidZipRepository):
            unzip(test_zip_url, True)

# Generated at 2022-06-13 18:53:26.931888
# Unit test for function unzip
def test_unzip():
    pass

# Generated at 2022-06-13 18:53:37.413146
# Unit test for function unzip
def test_unzip():
    from glob import glob
    from shutil import rmtree
    from zipfile import ZipFile
    from cookiecutter import utils


# Generated at 2022-06-13 18:53:43.589605
# Unit test for function unzip
def test_unzip():
    """Test unzip function.
    """
    from cookiecutter import main

    result = main.cookiecutter('tests/fixtures/fake-repo-tmpl', no_input=True)

    assert result == 'fake-repo', result

    result = unzip('tests/fixtures/fake-repo-tmpl.zip', True)

    assert result == '/tmp/fake-repo-tmpl', result

# Generated at 2022-06-13 18:54:04.397855
# Unit test for function unzip
def test_unzip():
    unzip('https://github.com/audreyr/cookiecutter-pypackage/zipball/master', is_url=True)
    unzip('https://codeload.github.com/audreyr/cookiecutter-pypackage/zip/master', is_url=True)

# Generated at 2022-06-13 18:54:14.308812
# Unit test for function unzip
def test_unzip():
    """Test function unzip."""

    # Test unzipping an unprotected local repo
    unzip_path = unzip('tests/test-repo/test-repo.zip', False)
    assert os.path.exists(unzip_path)

    # Test unzipping a protected local repo
    password = 'pw'
    unzip_path = unzip('tests/test-repo/test-repo-pw.zip', False, password=password)
    assert os.path.exists(unzip_path)

    # Test unzipping an unprotected URL repo
    unzip_path = unzip('https://github.com/audreyr/cookiecutter-pypackage/archive/master.zip', True)
    assert os.path.exists(unzip_path)

# Generated at 2022-06-13 18:54:24.085868
# Unit test for function unzip
def test_unzip():
    import io
    import zipfile
    from cookiecutter.prompt import read_repo_password
    from cookiecutter.utils import make_sure_path_exists
    from cookiecutter.utils.unzip import unzip

    # Create a zip file with a top level directory
    f = io.BytesIO()
    z = zipfile.ZipFile(f, 'w')
    z.writestr('dir/', b'')
    z.writestr('dir/file', b'')
    z.close()

    # Create a zip file without a top level directory
    f2 = io.BytesIO()
    z2 = zipfile.ZipFile(f2, 'w')
    z2.writestr('file', b'')
    z2.close()

    # Create a zip file with password
    f3

# Generated at 2022-06-13 18:54:34.097599
# Unit test for function unzip
def test_unzip():
    import os
    import shutil
    from zipfile import BadZipFile, ZipFile
    from pathlib import Path

    repo_uri = 'https://github.com/audreyr/cookiecutter-pypackage'
    repo_path = unzip(repo_uri, True)
    assert os.path.isdir(repo_path)
    assert os.path.isfile(os.path.join(repo_path, "setup.py"))
    shutil.rmtree(repo_path)

    repo_path = unzip(repo_uri, True)
    assert os.path.isdir(repo_path)
    assert os.path.isfile(os.path.join(repo_path, "setup.py"))
    shutil.rmtree(repo_path)

    repo_

# Generated at 2022-06-13 18:54:41.117880
# Unit test for function unzip
def test_unzip():
    test_zip = ('https://github.com/audreyr/cookiecutter-pypackage'
                '/archive/master.zip')
    unzip(test_zip, True)
    unzip(test_zip, True, no_input=True)

    test_zip_file_path = \
        'C:/Users/user/Documents/GitHub/' \
        'cookiecutter-python-cli-application/tests/test-repo-templates/' \
        'hackathon-starter/hackathon-starter-master.zip'
    unzip(test_zip_file_path, False)
    unzip(test_zip_file_path, False, no_input=True)


# Generated at 2022-06-13 18:54:52.338051
# Unit test for function unzip
def test_unzip():
    """
    test_unzip
    """
    # Initialise
    import shutil
    import time
    import glob
    import unittest
    import zipfile
    import os
    import codecs

    # Set up
    # set up temporary directory
    temp_dir = tempfile.mkdtemp()
    # set up cookiecutter project directory
    projdir = os.path.join(temp_dir, 'test-project')
    os.mkdir(projdir)
    # Set up zip file to download
    zipname = 'testzip.zip'
    zip_path = os.path.join(temp_dir, zipname)

    readme = u'\n'.join(codecs.open(os.path.join('tests', 'files', 'README.md'), encoding='utf-8').readlines())

# Generated at 2022-06-13 18:54:54.768206
# Unit test for function unzip
def test_unzip():
    #import pprint
    #pprint.pprint(unzip('../tests/files/cookiecutter-design-patterns/cookiecutter-design-patterns.zip', False))
    assert True

# Generated at 2022-06-13 18:54:55.971384
# Unit test for function unzip
def test_unzip():
    """Test that unzip works as expected."""
    pass

# Generated at 2022-06-13 18:55:00.815683
# Unit test for function unzip
def test_unzip():
    # Given
    is_url = False
    zip_uri = "./test_cookiecutter_unzip/no_templates.zip"
    clone_to_dir = "./test_cookiecutter_unzip"

    # When
    unzip(zip_uri, is_url, clone_to_dir)

# Generated at 2022-06-13 18:55:04.607723
# Unit test for function unzip
def test_unzip():
    # Path to test file
    path = os.path.abspath('tests/files/fake-repo.zip')
    # unzip will raise a badzipfile exception if it cannot unzip the file
    unzip(path, False)

# Generated at 2022-06-13 18:55:52.899659
# Unit test for function unzip
def test_unzip():
    """Test unzip function in various scenarios."""
    assert True

# Generated at 2022-06-13 18:56:00.942356
# Unit test for function unzip
def test_unzip():
    import unittest
    # Test with a dummy zipfile
    # Create a dummy zipfile with one file
    import tempfile
    from zipfile import ZipFile
    file_contents = "pizza is delicious"
    f = tempfile.NamedTemporaryFile(delete=False)
    with ZipFile(f.name, "w") as z:
        z.writestr("pizza", file_contents)

    unzip_path = unzip(zip_uri=f.name, is_url=False)
    assert os.path.exists(unzip_path)
    assert os.path.exists(unzip_path)
    assert file_contents == open(os.path.join(unzip_path, "pizza"), "r").read()

# Generated at 2022-06-13 18:56:11.313811
# Unit test for function unzip
def test_unzip():
    import requests_mock
    import pytest
    from cookiecutter.config import DEFAULT_CONFIG

    DEFAULT_CONFIG['no_input'] = True

    with requests_mock.Mocker() as m:
        url = 'https://api.github.com/v1/repos/example_owner/example_name/zipball'
        m.get(url, content=b'', headers={'content-type':'application/octet-stream'})

        ret = unzip(url, True, DEFAULT_CONFIG['repository_dir'])

        assert os.path.exists(ret)
        assert os.path.isdir(ret)


# Generated at 2022-06-13 18:56:21.352301
# Unit test for function unzip
def test_unzip():
    import shutil
    import zipfile
    from cookiecutter.utils import rmtree
    
    # Test zip is a valid zip file with a top-level directory.
    # However, this test zip file does not have a password
    test_zip_path = os.path.join("tests", "files", "test.zip")
    
    # Create the zip file to test unzip
    output_zip_path = os.path.join("tests", "files", "output", "output.zip")
    shutil.copyfile(test_zip_path, output_zip_path)
    
    # Create a temporary directory to save unpacked files
    output_path = tempfile.mkdtemp()
    
    # Unzip zip file
    unzip_path = unzip(output_zip_path, False, output_path)

# Generated at 2022-06-13 18:56:22.497449
# Unit test for function unzip
def test_unzip():
    """Test the unzip function of the utils module."""
    pass

# Generated at 2022-06-13 18:56:25.580977
# Unit test for function unzip
def test_unzip():
    unzip("http://www.example.com/foo.zip",True)
    unzip("http://www.example.com/foo.zip",True,'/tmp')
    unzip("http://www.example.com/foo.zip",True,'/tmp',True)

# Generated at 2022-06-13 18:56:32.347635
# Unit test for function unzip
def test_unzip():
    repo_name = 'git+https://github.com/audreyr/cookiecutter-pypackage.git'
    clone_to_dir = os.path.join(os.path.abspath('tests/test-data/test_zip_repo'), repo_name)
    repo_name = repo_name.split('/')[-1]
    repo_name = repo_name.split('.')[0]
    target_folder = '{0}-master/{1}'.format(repo_name, repo_name)

    assert os.path.isdir(os.path.join(clone_to_dir, target_folder))

    readme_txt = os.path.join(clone_to_dir, target_folder, 'README.rst')

# Generated at 2022-06-13 18:56:39.015367
# Unit test for function unzip
def test_unzip():
    assert unzip('tests/fake-repo-tmpl/', is_url=False)
    assert unzip('/tmp/', is_url=False)
    assert unzip('https://github.com/audreyr/cookiecutter-pypackage/zipball/0.5.0', is_url=True)
    assert unzip('http://www.repo-provider.com/fake-repo-tmpl.zip', is_url=True)

# Generated at 2022-06-13 18:56:45.498819
# Unit test for function unzip
def test_unzip():
    import pytest

    with pytest.raises(IOError):
        unzip(None, None, clone_to_dir='.')

    with pytest.raises(ValueError):
        unzip('.', None, clone_to_dir='.')

    with pytest.raises(ValueError):
        unzip('/non/existing/path/', None, clone_to_dir='.')

    with pytest.raises(ValueError):
        unzip('/non/existing/path/', False, clone_to_dir='.')

# Generated at 2022-06-13 18:56:53.978282
# Unit test for function unzip
def test_unzip():
    # Create test zip file
    import io
    import zipfile
    import shutil

    zip_loc = os.path.join(os.getcwd(), 'test.zip')
    loc = os.path.join(os.getcwd(), 'test')
    os.mkdir(loc)

# Generated at 2022-06-13 18:58:27.784245
# Unit test for function unzip
def test_unzip():
    pass

# Generated at 2022-06-13 18:58:34.231104
# Unit test for function unzip
def test_unzip():
    import shutil
    import pytest
    import tempfile

    # Create a cookiecutter repo dir in a tempdir
    unzip_path = unzip("https://github.com/mehalter/cookiecutter-pytest-plugin/archive/master.zip",
                     True, clone_to_dir=tempfile.gettempdir())
 
    # Now ensure we can see the repo
    assert os.listdir(unzip_path) == ["cookiecutter-pytest-plugin-master"]
    assert os.listdir(os.path.join(unzip_path, "cookiecutter-pytest-plugin-master")) == ["pytest_skeleton"]

# Generated at 2022-06-13 18:58:37.406675
# Unit test for function unzip
def test_unzip():
    """Unit test for function unzip"""
    unzip('https://github.com/audreyr/cookiecutter-pypackage/archive/master.zip', True, '.')

# Generated at 2022-06-13 18:58:43.265677
# Unit test for function unzip
def test_unzip():
    """Test unzips a file"""
    path = unzip("/home/gulbahar/PycharmProjects/CookieCutter/CookieCutter.zip", is_url=False)
    assert os.path.exists(path)
    assert os.path.isdir(path)
    print("File unzipped into " + path)

# Generated at 2022-06-13 18:58:51.986390
# Unit test for function unzip
def test_unzip():
    import shutil
    from cookiecutter.config import get_user_config
    from cookiecutter.utils import rmtree
    from tempfile import mkdtemp
    from zipfile import ZipFile, ZIP_DEFLATED
    from unittest import TestCase, skip

    class TestZip(TestCase):
        def setUp(self):
            self.password = 'test'
            self.test_files = ['foo.txt', 'bar.txt']
            self.test_dir = mkdtemp()
            self.test_zip_file = os.path.join(self.test_dir, 'zip.zip')
            self.test_zip_file_password = os.path.join(self.test_dir, 'zip_password.zip')

# Generated at 2022-06-13 18:59:02.944244
# Unit test for function unzip
def test_unzip():
    import tempfile
    import unittest
    from unittest import mock

    import pytest
    from cookiecutter.repository import unzip, InvalidZipRepository


    class UnzipTestCase(unittest.TestCase):
        def setUp(self):
            self.unzip_base = tempfile.mkdtemp()
            self.zip_path = os.path.join(self.unzip_base, 'tests/test_files/fake-repo.zip')
            self.unzip_path = os.path.join(self.unzip_base, 'bake-off-cookiecutter')

        def tearDown(self):
            os.remove(self.zip_path)
            os.rmdir(self.unzip_base)


# Generated at 2022-06-13 18:59:07.635599
# Unit test for function unzip
def test_unzip():
    # TODO: take the test zipfile out of the git repo
    zip_uri = 'https://github.com/audreyr/cookiecutter-pypackage/archive/master.zip'
    project_dir = unzip(zip_uri, True, clone_to_dir='.')

# Generated at 2022-06-13 18:59:16.672437
# Unit test for function unzip

# Generated at 2022-06-13 18:59:28.030981
# Unit test for function unzip
def test_unzip():
    import shutil
    import stat
    import warnings
    from pathlib import Path
    from zipfile import ZIP_DEFLATED, ZIP_STORED
    from cookiecutter.utils import rmtree
    # Test content
    content = {
        "a": "a",
        "b/c": "c",
        "b/d/e": "e",
        "b/d/f": "f",
        "b/d/g/h": "h",
        "b/d/g/i": "i",
        "b/d/g/j/k": "k",
    }
    # Create test zip file
    zip_path = Path("unzip-test.zip")
    # In case the file exists
    if zip_path.exists():
        zip_path.unlink()
    # Create

# Generated at 2022-06-13 18:59:35.481095
# Unit test for function unzip
def test_unzip():
    from cookiecutter.tests.test_repo import test_repo_dir
    import shutil
    import requests_mock
    import requests_toolbelt

    zip_uri = os.path.join(test_repo_dir, 'cookiecutter_example.zip')
    with requests_mock.Mocker() as m:
        is_url = True
        clone_to_dir = os.path.join(test_repo_dir, 'archive')
        zip_path = os.path.join(clone_to_dir, 'cookiecutter_example.zip')

        m.get(
            'https://github.com/audreyr/cookiecutter-example/archive/master.zip',
            content=open(zip_uri, 'rb').read()
        )
