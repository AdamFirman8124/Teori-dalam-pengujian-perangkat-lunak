

# Generated at 2022-06-13 18:49:54.037180
# Unit test for function repository_has_cookiecutter_json
def test_repository_has_cookiecutter_json():
    assert repository_has_cookiecutter_json(
        'tests/fixtures/test-repo-tmpl/') == True
    assert repository_has_cookiecutter_json(
        'tests/fixtures/test-repo-pre/'
        ) == False

# Generated at 2022-06-13 18:49:55.617295
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    pass

# Generated at 2022-06-13 18:50:05.402083
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    def test_case(template, abbreviations, clone_to_dir, checkout, no_input,
                  password=None, directory=None,
                  expected_repo_dir=None, expected_cleanup=None):
        repo_dir, cleanup = determine_repo_dir(
            template, abbreviations, clone_to_dir, checkout, no_input,
            password, directory,
        )
        assert (expected_repo_dir is None or repo_dir == expected_repo_dir), \
            "Unexpected repository directory '{}'".format(repo_dir)
        assert (expected_cleanup is None or cleanup == expected_cleanup), \
            "Unexpected cleanup {}".fomrat(cleanup)


# Generated at 2022-06-13 18:50:12.667175
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    template = 'https://github.com/audreyr/cookiecutter-pypackage'
    abbreviations = {}
    clone_to_dir = '/home/randy/Desktop'
    checkout = 'master'
    no_input = False
    password = None
    directory = None
    expected_output = '/home/randy/Desktop/cookiecutter-pypackage', False
    assert determine_repo_dir(
        template,
        abbreviations,
        clone_to_dir,
        checkout,
        no_input,
        password,
        directory
    ) == expected_output

# Generated at 2022-06-13 18:50:13.668515
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    pass

# Generated at 2022-06-13 18:50:22.468575
# Unit test for function repository_has_cookiecutter_json
def test_repository_has_cookiecutter_json():
    """Assumes testing is being run from the cookiecutter dir.

    Tests for valid, invalid, and non-existent template dirs.
    """
    # test for valid template directory
    template_dir = 'tests/test-template'
    assert repository_has_cookiecutter_json(template_dir) == True

    # test for invalid template directory
    template_dir = 'tests/test-template-no-json'
    assert repository_has_cookiecutter_json(template_dir) == False

    # test for non-existent template directory
    template_dir = 'tests/does-not-exist'
    assert repository_has_cookiecutter_json(template_dir) == False

# Generated at 2022-06-13 18:50:35.268200
# Unit test for function expand_abbreviations
def test_expand_abbreviations():
    abbreviations = {
        "gh": "https://github.com/{}.git",
        "bb": "https://bitbucket.org/{}.git",
    }
    assert expand_abbreviations("audreyr", abbreviations) == "audreyr"
    assert expand_abbreviations("gh:audreyr", abbreviations) == "https://github.com/audreyr.git"
    assert expand_abbreviations("gh:audreyr/cookiecutter", abbreviations) == "https://github.com/audreyr/cookiecutter.git"
    assert expand_abbreviations("audreyr/cookiecutter", abbreviations) == "audreyr/cookiecutter.git"

# Generated at 2022-06-13 18:50:36.145882
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    assert determine_repo_dir()

# Generated at 2022-06-13 18:50:42.415832
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    template = '{{cookiecutter.repo_name}}/{{cookiecutter.dir_name}}'
    abbreviations = {'gh': 'https://github.com/{}'}
    clone_to_dir = '.'
    checkout = 'master'
    no_input = False
    password = ''
    directory = ''

    result = determine_repo_dir(template,
        abbreviations,
        clone_to_dir,
        checkout,
        no_input,
        password,
        directory)
    assert result
    assert result[0] == './{{cookiecutter.repo_name}}/{{cookiecutter.dir_name}}'
    assert result[1] == False

# Generated at 2022-06-13 18:50:50.530444
# Unit test for function expand_abbreviations
def test_expand_abbreviations():
    """ Test expand abbreviations for various test cases."""
    abbreviations = {
        'gh': 'https://{}/',
        'ghu': 'https://{}/{}',
        'ghr': 'https://{}/{}/{}',
    }

    # Normal cases.

# Generated at 2022-06-13 18:51:01.904526
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    template = "https://github.com/ronnie76er/cookiecutter-django-crud"
    abbreviations = {}
    clone_to_dir = os.path.join(os.getcwd(), "tests", "test_repo")
    checkout = "master"
    password = None
    directory = None

    try:
        determine_repo_dir(template, abbreviations, clone_to_dir, checkout, False, password, directory)
    except:
        assert(False)

    assert(True)

test_determine_repo_dir()

# Generated at 2022-06-13 18:51:08.719316
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    # This is a real directory.
    template = os.path.dirname(os.path.abspath(__file__))
    # This should be moved to a more appropriate location
    abbreviations = {'gh': 'https://github.com/{}.git'}
    clone_to_dir = '.'
    checkout = None
    no_input = False
    password = None
    directory = None

    assert os.path.isdir(determine_repo_dir(template, abbreviations, clone_to_dir, checkout,
                                            no_input, password, directory))


if __name__ == '__main__':
    test_determine_repo_dir()

# Generated at 2022-06-13 18:51:18.231406
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    """Unit test for function `determine_repo_dir`."""
    from cookiecutter.config import DEFAULT_CONFIG

    template = 'gh:audreyr/cookiecutter-pypackage'
    abbreviations = DEFAULT_CONFIG['abbreviations']
    clone_to_dir = '~/Code/cookiecutters'
    checkout = 'master'
    no_input = True
    password = None
    directory = None

    repo_dir, cleanup = determine_repo_dir(
        template,
        abbreviations,
        clone_to_dir,
        checkout,
        no_input,
        password,
        directory
    )

    assert isinstance(repo_dir, str)
    assert not cleanup

# Generated at 2022-06-13 18:51:26.438414
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    """ Test determine_repo_dir function """
    from cookiecutter.main import cookiecutter
    from cookiecutter.config import DEFAULT_CONFIG
    repo_dir = determine_repo_dir(
        'gh:audreyr/cookiecutter-pypackage',
        abbreviations=DEFAULT_CONFIG['abbreviations'],
        clone_to_dir='/tmp',
        checkout='',
        no_input=False,
        directory=None,
    )
    assert repo_dir[0] == '/tmp/cookiecutter-pypackage'
    assert repo_dir[1] == False


# Generated at 2022-06-13 18:51:36.121481
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    """
    Test for function determine_repo_dir
    """
    template = "abc"
    test_abbreviations = {"abc": "git@github.com:abc.git"}
    clone_to_dir = "."
    checkout = ""
    no_input = False
    password = None
    directory = None

    result_template, result_clean_up = determine_repo_dir(
        template,
        test_abbreviations,
        clone_to_dir,
        checkout,
        no_input,
        password,
        directory,
    )

    assert result_template == "git@github.com:abc.git"
    assert result_clean_up == False

# Generated at 2022-06-13 18:51:39.227670
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    template = "https://github.com/rpi-project-template/rpi_project_template.git"
    output = determine_repo_dir(template, {}, '.', None, False)
    assert type(output) == tuple
    repo_dir, cleanup = output[0], output[1]
    assert os.path.isdir(repo_dir)
    assert cleanup == False

# Generated at 2022-06-13 18:51:51.317293
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    """Unit test for function determine_repo_dir"""
    from cookiecutter import main
    #git clone
    repo_dir, cleanup = determine_repo_dir('https://github.com/jhonpale/cookiecutter-django-crud.git', main.DEFAULT_ABBREVIATIONS, '~/.cookiecutters', 'master', True, None)
    assert repo_dir == "/home/jhonpale/.cookiecutters/cookiecutter-django-crud" and cleanup == False
    #dir
    repo_dir, cleanup = determine_repo_dir('/home/jhonpale/workspace/cookiecutter-django-crud', main.DEFAULT_ABBREVIATIONS, '~/.cookiecutters', 'master', True, None)

# Generated at 2022-06-13 18:52:04.439238
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    """Unit test for function determine_repo_dir."""
    import pytest
    from unittest import mock
    from cookiecutter.repository import expand_abbreviations, repository_has_cookiecutter_json

    with mock.patch('cookiecutter.repository.clone') as mock_clone:
        with mock.patch('cookiecutter.repository.unzip') as mock_unzip:
            mock_clone.return_value = '/does/not/exist'
            mock_unzip.return_value = '/does/not/exist'
            abbreviations = {'my_abbrev': 'git@github.com:pytest-dev/cookiecutter-pytest-plugin'}


# Generated at 2022-06-13 18:52:15.020319
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    # test valid abbreviated git repo
    abbrevs = {
        'gh': 'https://github.com/{}.git',
    }
    template = 'gh:audreyr/cookiecutter-pypackage'
    repo_dir, cleanup = determine_repo_dir(
        template,
        abbreviations=abbrevs,
        clone_to_dir='./',
        checkout=None,
        no_input=False,
        password=None,
        directory=None,
    )
    repo_url = 'https://github.com/audreyr/cookiecutter-pypackage.git'
    assert repo_dir == repo_url

    # test invalid abbreviated git repo
    template = 'gh:audreyr/cookiecutter-pypackage-invalid'
    # noinspection PyBroad

# Generated at 2022-06-13 18:52:26.142777
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    # not a repo URL
    template = './py'
    abbreviations = {}
    clone_to_dir = '.'
    checkout = None
    password = None
    no_input = False
    directory = None

    # returns tuple (template, cleanup)

    assert determine_repo_dir(template, abbreviations, clone_to_dir, checkout, no_input, password, directory) == ('./py/cookiecutter.json', False)

    # test is_repo_url()
    template = 'https://xyz.com/py'
    assert determine_repo_dir(template, abbreviations, clone_to_dir, checkout, no_input, password, directory) == ('./.cookiecutters/py/cookiecutter.json', False)

    assert is_repo_url(template) == True


# Generated at 2022-06-13 18:52:37.312629
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    """
    Test for function determine_repo_dir.

    The function expand_abbreviations is tested as well.
    """
    # Test for function expand_abbreviations
    abbreviations = {
        'gh': 'https://github.com/{}.git',
        'bb': 'https://bitbucket.org/{}',
    }
    assert 'https://github.com/audreyr/cookiecutter-pypackage.git' == expand_abbreviations('gh:audreyr/cookiecutter-pypackage', abbreviations)
    assert 'https://github.com/audreyr/cookiecutter-pypackage' == expand_abbreviations('gh:audreyr/cookiecutter-pypackage/', abbreviations)

# Generated at 2022-06-13 18:52:45.609763
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    try:
        determine_repo_dir("https://github.com/xurxosanz/cookiecutter-example",
                                  {},
                                  "~/Example/Repo",
                                  "master",
                                  True)
        assert False
    except RepositoryNotFound:
        assert True
        pass
    finally:
        try:
            determine_repo_dir("~/cookiecutter-example",
                                      {},
                                      "~/Example/Repo",
                                      "master",
                                      True)
        except RepositoryNotFound:
            assert False
            pass


# Generated at 2022-06-13 18:52:54.178872
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    from unittest import TestCase

    class DetermineRepoDirTests(TestCase):
        def test_determine_repo_dir_without_directory(self):
            template = 'https://github.com/audreyr/cookiecutter-pypackage.git'
            abbreviations = {}
            clone_to_dir = './test'
            checkout = None
            no_input = True
            password = None
            directory = None

            repo, cleanup = determine_repo_dir(
                template,
                abbreviations,
                clone_to_dir,
                checkout,
                no_input,
                password,
                directory,
            )

            self.assertEqual(repo, os.path.join(clone_to_dir, template))
            self.assertIs(cleanup, False)


# Generated at 2022-06-13 18:53:02.232266
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    """Unit test for determine_repo_dir()
    """
    import os
    import shutil
    import tempfile
    import unittest
    from cookiecutter.vcs import git
    from cookiecutter.exceptions import RepositoryNotFound

    class TestDetermineRepoDir(unittest.TestCase):
        """
        A unit test class for determine_repo_dir()
        """

        def setUp(self):
            """
            Initializer for the unit test
            """
            self.template = None
            self.clone_to_dir = tempfile.mkdtemp()
            self.checkout = None
            self.no_input = True
            self.password = None
            self.directory = None

        def tearDown(self):
            """
            Cleanup for the unit test
            """
           

# Generated at 2022-06-13 18:53:13.107246
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    """ Verify that determine_repo_dir works with valid input
    """

    # Valid input from the command line
    assert determine_repo_dir("https://github.com/fake/repo.git",
        {}, "", "", True)

    # With a directory
    assert determine_repo_dir("https://github.com/fake/repo.git",
        {}, "", "", True, directory="fake/directory")

    # With abbreviations
    assert determine_repo_dir("abbrev",
        { "abbrev": "https://github.com/fake/repo.git" },
        "", "", True)

    # With a zip file
    assert determine_repo_dir("https://github.com/fake/repo.zip",
        {}, "", "", True)

    # With

# Generated at 2022-06-13 18:53:24.228781
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    """
    Determines the repo directory for a given test cases.
    """
    print("Entering test_determine_repo_dir.")
    test_hash_list = [] # List of tuples including (test_name, template, abbreviations_list, clone_to_dir, checkout, no_input, expected_output)

    # Test 1
    test_hash_list.append(("Test 1", "handy", {}, "clone_to_dir", "checkout", "no_input", "Template:handy") )

    # Test 2

# Generated at 2022-06-13 18:53:31.324349
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    '''Testing the determine_repo_dir function above'''

    template = 'PLACEHOLDER'
    abbreviations = {}
    clone_to_dir = 'PLACEHOLDER'
    checkout = 'PLACEHOLDER'
    no_input = 'PLACEHOLDER'
    directory = 'PLACEHOLDER'

    assert determine_repo_dir(template, abbreviations, clone_to_dir, checkout, no_input, directory)

# Generated at 2022-06-13 18:53:45.867128
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    '''
    Test determine_repo_dir for all possible input and output conditions.
    '''

    # if template is a zip file
    if is_zip_file(template):
        unzipped_dir = unzip(
            zip_uri=template,
            is_url=is_repo_url(template),
            clone_to_dir=clone_to_dir,
            no_input=no_input,
            password=password,
        )
        repository_candidates = [unzipped_dir]
        cleanup = True
    # if template is a repo_url

# Generated at 2022-06-13 18:53:46.285814
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    pass

# Generated at 2022-06-13 18:53:57.169042
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    """Unit test for determine_repo_dir
    """
    assert determine_repo_dir('git@github.com:acabunoc/moz-gfx-html-templates.git',
        {}, '.', '.', False, 'password', None) is not None

    assert determine_repo_dir('git@github.com:acabunoc/moz-gfx-html-templates.git?ref=master',
        {}, '.', '.', False, 'password', None) is not None

    assert determine_repo_dir('git@github.com:acabunoc/moz-gfx-html-templates.git',
        {}, None, '.', False, 'password', None) is not None


# Generated at 2022-06-13 18:54:14.356237
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    """
    Ensure determine_repo_dir returns the expected directory.
    """
    clone_to_dir = 'fixtures'
    # First, test a local directory
    template = 'fixtures/fake-repo-tmpl'
    repo_dir, cleanup_dir = determine_repo_dir(template, abbreviations={},
                                               clone_to_dir=clone_to_dir,
                                               checkout=None,
                                               no_input=False)
    assert repo_dir == template
    assert cleanup_dir == False

    # Next, test a GitHub URL
    template = 'https://github.com/audreyr/cookiecutter-pypackage.git'

# Generated at 2022-06-13 18:54:24.145527
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    template = "git@github.com:audreyr/cookiecutter-pypackage.git#some-tag"
    abbreviations = {
        'gh': 'https://github.com/{}.git',
        'bb': 'https://bitbucket.org/{}.git',
        'gd': 'https://gitlab.com/{}.git',
    }
    clone_to_dir = "/Users/audreyr/Documents/mycookiecutters"
    checkout = "master"
    no_input = True
    password = "123password"
    directory = "testdir"

# Generated at 2022-06-13 18:54:32.273203
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    repo_url = 'git@github.com:audreyr/cookiecutter-pypackage.git'
    clone_to_dir = 'tests/fake-repo-tmpl'
    template = 'https://github.com/audreyr/cookiecutter-pypackage.git'
    d, c = determine_repo_dir(
        template=template,
        abbreviations={},
        clone_to_dir=clone_to_dir,
        checkout=None,
        no_input=False,
        password=None,
        directory=None,
    )

    assert repo_url in str(d)

# Generated at 2022-06-13 18:54:40.456846
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    import pytest
    import os
    # test a local path directory
    assert determine_repo_dir('cookiecutter-pypackage', {}, '/tmp',
                              None, None, None) == (
                                  os.path.join(os.getcwd(), 'cookiecutter-pypackage'),
                                  False)
    # test a directory with a directory inside it
    assert determine_repo_dir('cookiecutter-pypackage', {}, '/tmp',
                              None, None, None) == (
                                  os.path.join(os.getcwd(), 'cookiecutter-pypackage'),
                                  False)
    # test .zip file

# Generated at 2022-06-13 18:54:51.813614
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    abbreviations = {
        'gh': 'https://github.com/{}.git',
        'bb': 'https://bitbucket.org/{}.git',
        'up': 'https://{}.uipath.com/svn/Product/'
    }

    repo_dir = determine_repo_dir(
        template='gh:python-patterns/cookiecutter-pypackage',
        abbreviations=abbreviations,
        clone_to_dir=None,
        checkout=None,
        no_input=False,
        password=None,
        directory=None,
    )
    print(repo_dir)
    assert repo_dir[0] == 'd:\\Documents\\projects\\my-projects\\cookiecutter-pypackage'



# Generated at 2022-06-13 18:54:58.947413
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    """Unit test for function determine_repo_dir."""
    import unittest
    import urllib
    from tempfile import mkdtemp
    from shutil import rmtree

    from cookiecutter.utils.paths import ensure_dir
    from cookiecutter.main import cookiecutter

    class TestRepository(unittest.TestCase):
        def setUp(self):
            self.abbreviations = {'gh': 'https://github.com/{}',
                                  'bb': 'https://bitbucket.org/{}'}
            self.template = 'gh:audreyr/cookiecutter-pypackage'
            self.cookiecutters_dir = mkdtemp()
            self.clone_to_dir = mkdtemp()


# Generated at 2022-06-13 18:55:04.056111
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    assert(determine_repo_dir
           ('git@github.com:audreyr/cookiecutter-pypackage.git',
            {},
            None,
            None,
            None,
            None,
            None)==
           ('git@github.com:audreyr/cookiecutter-pypackage.git',False))
    assert(determine_repo_dir
           ('git@github.com:audreyr/cookiecutter-pypackage.git:master',
            {},
            None,
            None,
            None,
            None,
            None)==
           ('git@github.com:audreyr/cookiecutter-pypackage.git:master',False))

# Generated at 2022-06-13 18:55:07.008605
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    template = 'cheese'
    abbreviations = {'cheese': 'foo/bar/baz'}
    clone_to_dir = '/foo/bar'
    checkout = 'master'
    no_input = False
    password = '1234'
    directory = 'test-directory'
    assert determine_repo_dir(template, abbreviations,
                               clone_to_dir, checkout, no_input, password, directory) == '/foo/bar/test-directory'

# Generated at 2022-06-13 18:55:14.695218
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    # 1. test for a zip file
    template = '{{cookiecutter.repo_name}}.zip'
    abbreviations = dict()
    clone_to_dir = '~/.cookiecutters' 
    checkout = ''
    no_input = False
    password = ''
    directory = None
    determine_result = determine_repo_dir(template, abbreviations, clone_to_dir, checkout, no_input, password, directory)
    assert determine_result[0] == '~/.cookiecutters/.{{cookiecutter.repo_name}}'
    assert determine_result[1] == True

    # 2. test for a git repo
    template = 'https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}.git'
    abbreviations = dict()
    clone

# Generated at 2022-06-13 18:55:25.829287
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    # Test with a path to a JS project directory
    template = '.'
    abbreviations = {}
    clone_to_dir = '/Users/foo/bar/'
    checkout = None
    no_input = False
    directory = None
    expected_path = '/Users/foo/bar/.'
    path_and_cleanup = determine_repo_dir(
        template,
        abbreviations,
        clone_to_dir,
        checkout,
        no_input,
        directory=directory
    )
    path = path_and_cleanup[0]
    assert path == expected_path

    # Test with a path to a JS project directory with a subdir
    template = '.'
    abbreviations = {}
    clone_to_dir = '/Users/foo/bar/'
    checkout = None
    no_input = False


# Generated at 2022-06-13 18:55:44.674813
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    assert(determine_repo_dir("a/b/c", {}, "/tmp/test", "master", True) == ("a/b/c", False))
    assert(determine_repo_dir("a/b/c", {}, "/tmp/test", "master", True, directory="d") == ("a/b/c/d", False))

# Generated at 2022-06-13 18:55:46.481909
# Unit test for function determine_repo_dir
def test_determine_repo_dir():

    assert determine_repo_dir
    assert determine_repo_dir('https://github.com/cookiecutter/cookiecutter')

# Generated at 2022-06-13 18:55:48.098336
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    pass

# Generated at 2022-06-13 18:55:56.612951
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    repo_candidates = []

    template_has_cookiecutter_json = 'https://example.com/test_repo.git'
    repo_candidate = determine_repo_dir(
        template=template_has_cookiecutter_json,
        abbreviations={},
        clone_to_dir='.',
        checkout=None,
        no_input=True,
        password=None,
        directory=None,
    )
    repo_candidates.append(repo_candidate)

    # Test with directory that exists

# Generated at 2022-06-13 18:56:03.533009
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    # Local repo
    assert (
        determine_repo_dir(
            template='/home/repo/dir',
            abbreviations={},
            clone_to_dir='/tmp',
            checkout='',
            no_input=False,
        )
        == ('/home/repo/dir', False)
    )

    # Local repo with extra directory
    assert (
        determine_repo_dir(
            template='/home/repo/dir',
            abbreviations={},
            clone_to_dir='/tmp',
            checkout='',
            no_input=False,
            directory='otherdir',
        )
        == ('/home/repo/dir/otherdir', False)
    )

    # Git repo

# Generated at 2022-06-13 18:56:06.710218
# Unit test for function determine_repo_dir
def test_determine_repo_dir():

    template = '/abc/def'
    abbreviations = {}
    clone_to_dir = '/tmp'
    checkout = 'master'
    no_input = False
    password = None
    directory = None

    try:
        determine_repo_dir(template, abbreviations, clone_to_dir, checkout,
                           no_input, password, directory)
    except RepositoryNotFound:
        print('A valid repository for "{}" could not be found in the '
              'following locations:\n{}'.format(template, clone_to_dir))



# Generated at 2022-06-13 18:56:09.500815
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    # make a temp directory for testing purposes
    template = './tests/fixtures/fake-repo-tmpl'
    clone_to_dir = '/tmp'
    repo_dir, cleanup = determine_repo_dir(
        template, {}, clone_to_dir, 'master', False
    )
    assert repo_dir == "./tests/fixtures/fake-repo-tmpl"
    assert cleanup == False

# Generated at 2022-06-13 18:56:16.987407
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    """
    test to ensure that determine_repo_dir is working properly
    """
    template = 'https://github.com/audreyr/cookiecutter-pypackage.git'
    abbreviations = {
        'gh': 'https://github.com/{}.git',
        'bb': 'https://bitbucket.org/{}.git',
        'ghe': 'git@github.com:{}.git',
        'bbe': 'git@bitbucket.org:{}.git',
    }
    clone_to_dir = '.'
    checkout = None
    no_input = False

    repository_candidates = 'https://github.com/audreyr/cookiecutter-pypackage.git'

# Generated at 2022-06-13 18:56:22.264213
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    template = 'https://github.com/audreyr/cookiecutter-pypackage.git'
    abbreviations = 'foo:bar'
    no_input = None
    password = 'foo'
    clone_to_dir = '.'
    directory = None
    checkout = None
    output = determine_repo_dir(template, abbreviations, clone_to_dir, checkout, no_input, password, directory)

# Generated at 2022-06-13 18:56:24.476164
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    """Unit test for function determine_repo_dir."""
    assert determine_repo_dir(None,{},"","","", "", "") == (None,)

# Generated at 2022-06-13 18:57:00.404741
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    """Test determine_repo_dir function"""
    repo_dir = determine_repo_dir(
        template=None,
        abbreviations=None,
        clone_to_dir=None,
        checkout=None,
        no_input=False,
        password=None,
        directory=None,
    )
    assert repo_dir == (None, False)

# Generated at 2022-06-13 18:57:12.185613
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    template = 'https://github.com/audreyr/cookiecutter-pypackage'
    abbreviations = {'gh': 'https://github.com/{}'}
    clone_to_dir = 'test_cookiecutter_repos'
    checkout = 'master'
    no_input = True
    password = None
    directory = None
    repo_dir, cleanup = determine_repo_dir(
        template,
        abbreviations,
        clone_to_dir,
        checkout,
        no_input,
        password,
        directory,
    )
    # From test_determine_repo_dir, get repo_dir
    assert repo_dir == 'test_cookiecutter_repos/audreyr/cookiecutter-pypackage'
    # cleanup should be false since template is a repo

# Generated at 2022-06-13 18:57:25.393699
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    """Test determine_repo_dir."""

    tmp_dir = tempfile.mkdtemp()
    os.mkdir(os.path.join(tmp_dir, 'foo'))
    with open(os.path.join(tmp_dir, 'foo', 'cookiecutter.json'), 'w') as fp:
        fp.write('{"foo": "bar"}')

    # test is_repo_url
    repo_url = 'https://github.com/audreyr/cookiecutter-pypackage.git'
    result = determine_repo_dir(
        repo_url,
        abbreviations={},
        clone_to_dir=tmp_dir,
        checkout='0.1.2',
        no_input=True
    )

# Generated at 2022-06-13 18:57:32.211754
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    # Ensure abbreviations are expanded
    abbreviations = {'gh': 'https://github.com/{}.git'}
    template = 'gh:audreyr/cookiecutter-pypackage'
    repo_dir, cleanup = determine_repo_dir(
        template=template,
        abbreviations=abbreviations,
        clone_to_dir='test_determine_repo_dir',
        checkout=None,
        no_input=False,
        password=None,
    )
    assert repo_dir == 'test_determine_repo_dir/audreyr/cookiecutter-pypackage'
    assert cleanup is False

    # Ensure that local directories are used as-is
    template = 'audreyr/cookiecutter-pypackage'
    repo_dir, cleanup = determine_

# Generated at 2022-06-13 18:57:45.665367
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    """
    Test determine_repo_dir
    """
    from cookiecutter.config import DEFAULT_ABBREVIATIONS
    from tempfile import mkdtemp
    import shutil

    template = 'https://github.com/audreyr/cookiecutter-pypackage'

# Generated at 2022-06-13 18:57:58.981096
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    repo_dir1 = determine_repo_dir('meh', {}, '.', 'default', False)
    repo_dir2 = determine_repo_dir('meh', {'meh': 'meh'}, '.', 'default', False)
    repo_dir3 = determine_repo_dir('meh:', {'meh': 'meh'}, '.', 'default', False)
    repo_dir4 = determine_repo_dir('meh:foo', {'meh': 'meh'}, '.', 'default', False)

    assert repo_dir1[0] == 'meh'
    assert repo_dir2[0] == 'meh'
    assert repo_dir3[0] == 'meh:'
    assert repo_dir4[0] == 'meh:foo'

# Generated at 2022-06-13 18:58:03.020605
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    result = determine_repo_dir("./cookiecutter-pypackage", {}, ".", "", False)
    assert result[0] == "./cookiecutter-pypackage"
    assert result[1] == False

# Generated at 2022-06-13 18:58:11.374573
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    template = 'my/cool/project'
    abbreviations = {
        'gh': 'https://github.com/{}.git',
        'bb': 'https://bitbucket.org/{}.git',
    }
    clone_to_dir = 'projects'
    checkout = None
    no_input = True
    password = 'foobar'
    directory = None

    repository_directory, cleanup = determine_repo_dir(
        template,
        abbreviations,
        clone_to_dir,
        checkout,
        no_input,
        password=password,
        directory=directory,
    )
    assert repository_directory == 'my/cool/project'
    assert cleanup == False


# Generated at 2022-06-13 18:58:16.801231
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    from tempfile import TemporaryDirectory

    template = 'https://github.com/audreyr/cookiecutter-pypackage.git'
    directory = None
    with TemporaryDirectory(prefix='cookiecutter-') as clone_to_dir:
        repo_dir, cleanup = determine_repo_dir(
            template=template,
            abbreviations={},
            clone_to_dir=clone_to_dir,
            checkout='master',
            no_input=True,
            password=None,
            directory=directory,
        )
        assert repo_dir.startswith('/tmp/cookiecutter-')
        assert cleanup is False

        template = 'audreyr/cookiecutter-pypackage'

# Generated at 2022-06-13 18:58:24.954460
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    """Unit test for function determine_repo_dir."""
    cookiecutter_dir = "C:/Users/user/PycharmProjects/cookiecutter"
    os.chdir(cookiecutter_dir)
    template = "dummy"
    abbreviations = {
        "dummy": "https://github.com/audreyr/cookiecutter-pypackage.git"
    }
    clone_to_dir = "C:/Users/user/PycharmProjects/cookiecutter"
    checkout = None
    no_input = True
    password = None
    directory = None

# Generated at 2022-06-13 18:59:27.070006
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    template = 'my-awesome-project'
    clone_to_dir = '/Users/Myself/temp'
    abbreviations = {'gh': 'https://github.com/{}', 'bb': 'https://bitbucket.org/{}'}
    checkout = 'master'
    no_input = False
    directory = None
    
    # Verify fails with RepositoryNotFound exception when no repo exists
    import pytest
    with pytest.raises(RepositoryNotFound):
        determine_repo_dir(template, abbreviations, clone_to_dir, checkout, no_input, None, directory)

# Generated at 2022-06-13 18:59:29.494209
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    repo_dir = determine_repo_dir(template='https://github.com/audreyr/cookiecutter-pypackage',
        abbreviations={}, clone_to_dir='/home/dev/.cookiecutters', checkout=None, no_input=False,
        password=None, directory='')
    print(repo_dir)


# Generated at 2022-06-13 18:59:36.266760
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    """Check the clone_repo function."""
    import shutil
    import tempfile

    # Create a temporary working directory
    temp_dir = tempfile.mkdtemp()

    # Get the directory containing the test cookiecutter.json
    local_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'fake-repo-tmpl'
    )

    # Create a temporary directory containing the test cookiecutter.json
    test_dir = temp_dir + '/fake-repo-tmpl'
    shutil.copytree(local_dir, test_dir)

    # Test that the temp directory created is found as a valid repository

# Generated at 2022-06-13 18:59:43.318598
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    template = 'https://github.com/pystachio/cookiecutter-pystachio.git'
    abbreviations = {}
    clone_to_dir = ''
    checkout = ''
    no_input = ''
    password = ''
    directory = 'tests'
    repo_dir, cleanup = determine_repo_dir(template, abbreviations, clone_to_dir, checkout, no_input, password, directory)
    assert repo_dir == 'tests'
    assert cleanup == False

test_determine_repo_dir()

# Generated at 2022-06-13 18:59:51.524902
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        # The setting is always a string
        clone_to_dir = d
        # Verify that it is working as expected
        result = determine_repo_dir(
            'https://github.com/cookiecutter/cookiecutter-django',
            {},
            clone_to_dir = clone_to_dir,
            checkout = None,
            no_input = True,
            password = None,
            directory = None
        )
        assert result == (os.path.join(clone_to_dir, 'cookiecutter-django'), False)