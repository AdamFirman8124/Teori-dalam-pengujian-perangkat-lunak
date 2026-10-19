

# Generated at 2022-06-13 18:50:07.695538
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    ######################################################################
    ######### TESTS FOR GIVEN CANDIDATES, WITH AND WITHOUT COOKIECUTTER.JSON
    ######################################################################
    # Create a temporary directory
    test_temp_dir = get_unique_directory()
    # git init the directory (creates .git)
    os.system('git init %s' % test_temp_dir)
    # Create a file for testing
    test_file = os.path.join(test_temp_dir, 'testfile')
    with open(test_file, 'w') as f:
        f.write('test')
    # Add test_temp_dir to git repository
    os.system('git add %s' % test_file)
    # Commit test_temp_dir to git repository

# Generated at 2022-06-13 18:50:11.371922
# Unit test for function expand_abbreviations
def test_expand_abbreviations():
    abbreviations = {'gh': 'https://github.com/{}.git'}
    assert expand_abbreviations('gh:audreyr/cookiecutter-pypackage',
                                abbreviations) == 'https://github.com/audreyr/cookiecutter-pypackage.git'

# Generated at 2022-06-13 18:50:23.044350
# Unit test for function expand_abbreviations
def test_expand_abbreviations():
    abbreviations = {'dict': 'https://github.com/audreyr/cookiecutter-pypackage.git'}
    assert expand_abbreviations(template='dict', abbreviations=abbreviations) == 'https://github.com/audreyr/cookiecutter-pypackage.git'

    abbreviations = {'dict': 'https://github.com/audreyr/cookiecutter-pypackage.git'}
    assert expand_abbreviations(template='dict:abc', abbreviations=abbreviations) == 'https://github.com/audreyr/cookiecutter-pypackage.git:abc'

    abbreviations = {'gh': 'https://github.com/{0}.git'}

# Generated at 2022-06-13 18:50:35.459060
# Unit test for function expand_abbreviations
def test_expand_abbreviations():
    abbreviations = {
        'gh': 'https://github.com/{}.git',
        'bb': 'https://bitbucket.org/{}.git',
        'gl': 'https://gitlab.com/{}.git'
    }

    assert expand_abbreviations('gh:audreyr/cookiecutter-pypackage', abbreviations) == 'https://github.com/audreyr/cookiecutter-pypackage.git'
    assert expand_abbreviations('audreyr/cookiecutter-pypackage', abbreviations) == 'audreyr/cookiecutter-pypackage'


# Generated at 2022-06-13 18:50:37.338198
# Unit test for function repository_has_cookiecutter_json
def test_repository_has_cookiecutter_json():
    assert(repository_has_cookiecutter_json('.'))
    assert(not repository_has_cookiecutter_json('notfound/'))

# Generated at 2022-06-13 18:50:41.104817
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    repo_dir, cleanup = determine_repo_dir('baidu', {}, '', '', False)
    assert repo_dir == 'baidu'
    assert cleanup is False

# Generated at 2022-06-13 18:50:48.060880
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    template = 'test'
    abbreviations = {'test': 'https://test.com'}
    clone_to_dir = 'test'
    checkout = None
    no_input = False
    password = None
    directory = None

    repo_dir, cleanup = determine_repo_dir(template,
                                           abbreviations,
                                           clone_to_dir,
                                           checkout,
                                           no_input,
                                           password,
                                           directory)
    assert repo_dir == 'https://test.com'
    assert cleanup == False

# Generated at 2022-06-13 18:50:52.050062
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    """Test that determine_repo_dir works well."""
    pass
    # Test if it finds the correct repo with a URL
    # Test if it finds the correct repo with a zip
    # Test if it finds the correct repo with a directory

# Generated at 2022-06-13 18:50:52.822856
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    pass

# Generated at 2022-06-13 18:51:03.355878
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    template = 'gh:pydanny/cookiecutter-django'
    abbreviations = {'gh': 'https://github.com/{}.git'}
    clone_to_dir = '/Users/pydanny/repos'
    checkout = 'develop'
    no_input = False
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
    assert '/Users/pydanny/repos/cookiecutter-django' == repo
    assert not cleanup



# Generated at 2022-06-13 18:51:15.580673
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    """
    Test determine_repo_dir function
    """
    template = "https://github.com/audreyr/cookiecutter-pypackage.git"
    abbreviations = {}
    clone_to_dir = os.getcwd()
    checkout = ""
    no_input = False
    password = None
    directory = None

    repo, cleanup = determine_repo_dir(
        template, abbreviations, clone_to_dir, checkout,
        no_input, password, directory
    )
    assert type(repo) == str

# Generated at 2022-06-13 18:51:21.897570
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    from pathlib import Path
    from cookiecutter import config

    template_directory = os.path.abspath(
        Path(
            os.path.dirname(__file__),
            '..',
            'tests',
            'fake-repo-tmpl',
        )
    )
    result = determine_repo_dir(
        template=template_directory,
        abbreviations={},
        clone_to_dir=os.path.abspath(config.DEFAULT_REPO_DIR),
        checkout='master',
        no_input=False,
    )
    assert result[0] == os.path.join(template_directory)

# Generated at 2022-06-13 18:51:28.401082
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    """Unit test for function determine_repo_dir."""
    # pylint: disable=redefined-outer-name
    import pytest

    # Test valid repository
    test_template = "https://github.com/audreyr/cookiecutter-pypackage.git"
    abbreviations = {}

    clone_to_dir = "testdir"

    checkout = None

    no_input = False

    with pytest.raises(RepositoryNotFound):
        determine_repo_dir(
            test_template,
            abbreviations,
            clone_to_dir,
            checkout,
            no_input
        )

    # Test invalid repository
    test_template = "https://github.com/audreyr/cookiecutter-pypackage-none.git"


# Generated at 2022-06-13 18:51:34.875599
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    test_dir = os.path.dirname(os.path.abspath(__file__))
    template = "https://github.com/bootstrap-vz/bootstrap-vz.git"
    repo_dir, cleanup = determine_repo_dir(template, {}, test_dir, None, False, None, None)
    assert (os.path.basename(repo_dir) == 'bootstrap-vz')

# Generated at 2022-06-13 18:51:48.887864
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    template = 'somelong/ghname'
    clone_to_dir = 'somedir'
    abbreviations = {
        'somelong': 'https://github.com/user/{}'
    }
    repository_candidates = determine_repo_dir(
        template,
        abbreviations,
        clone_to_dir,
        None,
        None,
        None,
        None
        )
    assert repository_candidates == ('somedir/https://github.com/user/somelong/ghname', False)

    template = 'https://github.com:user/ghname'
    clone_to_dir = 'somedir'
    abbreviations = {
        'somelong': 'https://github.com/user/{}'
    }
    repository_candidates = determine_repo

# Generated at 2022-06-13 18:51:56.063665
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    """Unit test for function determine_repo_dir."""
    # Test abbreviations
    abbreviations = {'gh': 'https://github.com/{}.git'}
    template = 'gh:audreyr/cookiecutter-pypackage'
    repo_dir, cleanup = determine_repo_dir(
        template, abbreviations, '.', '', False
    )
    assert repo_dir == 'cookiecutter-pypackage'
    assert cleanup

    # Test abbreviations containing user
    abbreviations = {'gh': 'https://{0}@github.com/{1}.git'}
    template = 'gh:myuser/mytemplate:myrepo'
    repo_dir, cleanup = determine_repo_dir(
        template, abbreviations, '.', '', False
    )
    assert repo

# Generated at 2022-06-13 18:51:57.352328
# Unit test for function determine_repo_dir
def test_determine_repo_dir():  # type: ignore
    pass

# Generated at 2022-06-13 18:52:09.368348
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    # success case
    abbreviations = {
        'gh': 'https://github.com/{}.git',
    }
    template = 'gh:tbosch/cookiecutter-jasmine'
    repository_dir, cleanup = determine_repo_dir(
        template=template,
        abbreviations=abbreviations,
        clone_to_dir='.',
        checkout=None,
        no_input=False,
        directory=None
    )
    assert repository_dir == 'cookiecutter-jasmine'
    assert cleanup == False
    # failure case
    template = 'gh:tbosch_cookiecutter-jasmine'

# Generated at 2022-06-13 18:52:17.610907
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    # Example from the documentation
    abbreviations = {
        'gh': 'https://github.com/{}.git',
        'bb': 'https://bitbucket.org/{}.git',
    }
    template = determine_repo_dir(
        'gh:audreyr/cookiecutter-pypackage',
        abbreviations,
        clone_to_dir='.',
        checkout='master',
    )
    assert (
        template ==
        'https://github.com/audreyr/cookiecutter-pypackage',
        False,
    )

    # A more complicated example

# Generated at 2022-06-13 18:52:27.798990
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    template_path = "/Users/q/cookiecutter-django"
    clone_to_dir = "/Users/q/cookiecutter-django"
    abbreviations = {
        'ah': 'https://github.com/audreyr/cookiecutter-pypackage.git',
        'gh': 'https://github.com/{0}.git',
        'bb': 'https://bitbucket.org/{0}'
    }
    checkout = None
    no_input = False

    # Test for local valid project template

# Generated at 2022-06-13 18:52:36.377841
# Unit test for function determine_repo_dir
def test_determine_repo_dir():

    # Using a git URL, resolve the repository
    template = 'https://github.com/audreyr/cookiecutter-pypackage.git'
    template_dir, cleanup = determine_repo_dir(
        template=template,
        abbreviations={},
        clone_to_dir='/',
        checkout=None,
        no_input=False,
    )
    # We should be able to use the determined repo
    assert repository_has_cookiecutter_json(template_dir)

    # Using a local directory, resolve the repository
    template = 'tests/fake-repo-pre/'
    template_dir, cleanup = determine_repo_dir(
        template=template,
        abbreviations={},
        clone_to_dir='/',
        checkout=None,
        no_input=False,
    )

# Generated at 2022-06-13 18:52:37.180732
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    pass

# Generated at 2022-06-13 18:52:46.040732
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    template = 'git@github.com:Audreyr/cookiecutter-pypackage.git'
    abbreviations = {}
    clone_to_dir = os.path.join(os.path.expanduser('~'), 'dev', 'cookiecutters')
    checkout = None
    no_input = False
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

    print('repo_dir is: {}'.format(repo_dir))
    print('cleanup is: {}'.format(cleanup))

if __name__ == '__main__':
    test_determine_repo_dir()

# Generated at 2022-06-13 18:52:51.989240
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    """Case for determining repo dir"""

    # Case 1: Template is in current working directory
    template = '.'
    abbreviations = {}
    clone_to_dir = "C:\\Users\\yoges\\cookiecutter-example"
    checkout = "master"
    no_input = False
    password = None
    directory = None

    expected = 'C:\\Users\\yoges\\cookiecutter-example', False

    assert(determine_repo_dir(template, abbreviations,
                              clone_to_dir, checkout, no_input, password,
                              directory) == expected)



# Generated at 2022-06-13 18:52:52.786236
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    pass

# Generated at 2022-06-13 18:52:58.172236
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    from cookiecutter import main
    from cookiecutter.main import cookiecutter

    results = cookiecutter(
        'https://github.com/audreyr/cookiecutter-pypackage.git',
        no_input=True,
        output_dir='../',
    )
    assert results['project_name'] == 'cookiecutter-pypackage'

# Generated at 2022-06-13 18:53:07.577580
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    template = 'git@github.com:user/repo.git'
    abbreviations = {'user':'user', 'repo':'repo'}
    clone_to_dir = 'C:\\Users\\user\\git'
    checkout = None
    no_input = False

    # Test when template is a git URI
    repo_dir, cleanup = determine_repo_dir(
        template, abbreviations, clone_to_dir, checkout, no_input,
        password=None, directory=None)
    assert repo_dir == 'C:\\Users\\user\\git\\repo'
    assert cleanup == False

    # Test when template is path to a directory
    template = 'C:\\Users\\user\\git\\repo'

# Generated at 2022-06-13 18:53:17.305353
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    """Unit test for function determine_repo_dir."""
    abbreviations = {
        'gh': 'https://github.com/{}.git',
        'bb': 'https://bitbucket.org/{}',
    }
    template = 'gh:audreyr/cookiecutter-pypackage'
    repo_dir, cleanup = determine_repo_dir(
        template, abbreviations, 'fake-path', None, False, 'fake-pwd', 'fake'
    )
    assert repo_dir == 'https://github.com/audreyr/cookiecutter-pypackage.git'
    assert cleanup is False

    template = 'gh:audreyr/cookiecutter-pypackage.git'

# Generated at 2022-06-13 18:53:24.827854
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    assert determine_repo_dir("azure-security-center") == "azure-security-center"
    assert determine_repo_dir("azure-security-center", "") == "azure-security-center"
    assert determine_repo_dir("azure-security-center", "", "") == "azure-security-center"
    assert determine_repo_dir("azure-security-center", "", "", "") == "azure-security-center"
    assert determine_repo_dir("azure-security-center", "", "", "", "") == "azure-security-center"

# Generated at 2022-06-13 18:53:36.286953
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    """Assert that determine_repo_dir() works as expected."""
    from os.path import dirname, join, abspath
    from tests.test_utils import TEST_COOKIE_DIR

    template = 'https://github.com/audreyr/cookiecutter-pypackage.git'

    # Determine the path of the current file's directory.
    current_dir = dirname(abspath(__file__))
    # Determine the path of the fixtures directory.
    fixtures_dir = abspath(join(current_dir, '..', 'fixtures'))

    # Mock "abbreviations"

# Generated at 2022-06-13 18:53:50.759808
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    template = 'https://github.com/cookiecutter/cookiecutter'
    abbreviations = {'cc': 'https://github.com/cookiecutter/cookiecutter'}
    clone_to_dir = 'fake'
    checkout = None
    no_input = True

    result = determine_repo_dir(
        template,
        abbreviations,
        clone_to_dir,
        checkout,
        no_input
    )

    assert result == (os.path.join(clone_to_dir, 'cookiecutter'), False)


# Generated at 2022-06-13 18:53:59.149831
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    template_name = 'https://github.com/audreyr/cookiecutter-pypackage'
    abbreviations = {'gh': 'https://github.com/{}.git'}
    clone_to_dir = 'test'
    checkout = 'master'
    no_input = False
    password = None
    template_dir = determine_repo_dir(
        template_name,
        abbreviations,
        clone_to_dir,
        checkout,
        no_input,
        password,
    )
    assert template_dir[0].endswith('cookiecutter-pypackage')
    assert template_dir[1] == False

# Generated at 2022-06-13 18:54:06.832419
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    import pytest
    from cookiecutter.utils import rmtree
    from cookiecutter.config import DEFAULT_CONFIG

    TEMPLATE_REPO_DIR = os.path.join(
        os.path.abspath(os.path.dirname(__file__)), 'fake-repo-tmpl'
    )

    def expand_abbreviations(template, abbreviations):
        return template
    # Determine repo dir should return expected values for valid templates

# Generated at 2022-06-13 18:54:12.116705
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    """
    Unit test for function determine_repo_dir
    """
    # 1. test if it can extract abbreviation correctly
    test_abbreviations={}
    test_abbreviations['abbre']='abbre'
    assert determine_repo_dir("abbre",test_abbreviations, 'clone_to_dir', 'checkout', 'no_input')==('abbre',False)
    
    # 2. test if it can extract abbreviation correctly
    test_abbreviations['abbre']='abbre:hello'
    assert determine_repo_dir("abbre:world",test_abbreviations, 'clone_to_dir', 'checkout', 'no_input')==('abbre:world',False)

# Generated at 2022-06-13 18:54:22.792205
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    """
    Test determine_repo_dir function
    :return: None
    """
    import tempfile
    import shutil
    import zipfile
    import json
    import os

    d = tempfile.mkdtemp()

    # create git repo with cookiecutter.json
    repo_name = 'test_repo'
    cookiecutter_json = os.path.join(d, repo_name, 'cookiecutter.json')
    repo_dir = os.path.join(d, repo_name)
    os.makedirs(repo_dir)
    with open(cookiecutter_json, 'w') as f:
        json.dump({'name': 'test_repo'}, f)
    os.system('git init {}'.format(repo_dir))

# Generated at 2022-06-13 18:54:29.511521
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    template = 'git@github.com:{{cookiecutter.full_name}}/{{cookiecutter.repo_name}}.git'
    abbreviations = {}
    clone_to_dir = '~/'
    checkout = 'master'
    no_input = True
    password = None
    directory = None
    repo_dir, cleanup = determine_repo_dir(template, abbreviations, clone_to_dir, checkout, no_input, password, directory)
    print(repo_dir)
    print(cleanup)

# Generated at 2022-06-13 18:54:38.716664
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    """
    Determines whether the function determine_repo_dir works as desired.

    :return: True if test passes, else False.
    """
    from cookiecutter.config import DEFAULT_ABBREVIATIONS
    import tempfile
    import shutil
    import filecmp

    clone_to_dir = tempfile.mkdtemp()

# Generated at 2022-06-13 18:54:43.783694
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    """
    test_determine_repo_dir
    """
    repo_url = 'https://gitlab.com/frostming/cookiecutter-example'
    return determine_repo_dir(
            repo_url,
            {},
            '.',
            'master',
            False,
    )

# Generated at 2022-06-13 18:54:52.991364
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    """
    Test for determine_repo_dir function.
    """
    import tempfile
    template = "https://github.com/audreyr/cookiecutter-pypackage.git"
    abbreviations = {"pypackage":"https://github.com/audreyr/cookiecutter-pypackage.git"}
    clone_to_dir = tempfile.gettempdir()
    checkout = ""
    no_input = True
    password = ""
    directory = ""
    assert determine_repo_dir(template, abbreviations, clone_to_dir, checkout, no_input, password, directory)[0] == clone_to_dir + "/cookiecutter-pypackage"
    
    template = "/home/user/cookiecutter-pypackage"

# Generated at 2022-06-13 18:54:55.636993
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    abbreviations = {'gh': 'https://github.com/{}.git'}
    template = ''

    assert determine_repo_dir(template, abbreviations, '', '', False)


test_determine_repo_dir()

# Generated at 2022-06-13 18:55:16.425431
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    result = determine_repo_dir(template='git@github.com:username/repo.git',
    abbreviations={},
    clone_to_dir='.',
    checkout='master',
    no_input=True,
    password=None,
    directory=None,
    )
    assert result[0] == '.'
    assert result[1] == False

# Generated at 2022-06-13 18:55:26.778584
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    from cookiecutter.main import cookiecutter

    template = 'https://github.com/pydanny/cookiecutter-django.git'
    abbreviations = {
        'gh': 'https://github.com/{}.git',
        'bb': 'https://bitbucket.org/{}',
    }
    directory = None
    clone_to_dir = '.'
    checkout = None

    repo_dir, cleanup = determine_repo_dir(
        template,
        abbreviations,
        clone_to_dir,
        checkout,
        True,
        directory=directory,
    )

    print("repo_dir:", repo_dir)
    assert os.path.isdir(repo_dir)
    assert not cleanup

# Generated at 2022-06-13 18:55:34.562368
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    template = 'git@github.com:user/repo.git'
    abbreviations = {}
    clone_to_dir = '/my/clone/dir'
    checkout = 'master'
    no_input = True
    password = 'passw0rd'
    directory = 'dir1/dir2'
    repo_dir, cleanup = determine_repo_dir(template, abbreviations, clone_to_dir, checkout, no_input, password, directory)
    print('repo_dir: ' + repo_dir)
    print('cleanup: ' + str(cleanup))


if __name__ == '__main__':
    test_determine_repo_dir()

# Generated at 2022-06-13 18:55:43.029324
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
	import pytest
	repo_dir = os.getcwd()
	#repo_dir_exists = repository_has_cookiecutter_json(repo_dir)
	#print repo_dir_exists
	template = os.path.join(repo_dir, '../')
	# No exceptions should be raised
	determine_repo_dir(template, {}, '.', None, False)
	#valid_repo_dir, cleanup_needed = determine_repo_dir(template, {}, '.', None, False)
	#assert valid_repo_dir == os.path.abspath(os.path.join(repo_dir, '../'))
	#assert cleanup_needed == False

# Generated at 2022-06-13 18:55:44.035788
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    pass

# Generated at 2022-06-13 18:55:55.278898
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    """
    Run unit tests to determine repo dir.
    """

    assert determine_repo_dir(template="https://github.com/this/is/my/repo.git",
                              abbreviations={},
                              clone_to_dir="/tmp",
                              checkout="master",
                              no_input=False) == ("/tmp/this/is/my/repo", False)

    assert determine_repo_dir(
        template="/home/awesome/repository",
        abbreviations={},
        clone_to_dir="/tmp",
        checkout="master",
        no_input=False) == ("/home/awesome/repository", False)


# Generated at 2022-06-13 18:55:59.703730
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    """Unit test for function determine_repo_dir."""
    fake_repo_dir = '/fake/repo/directory'
    fake_template = 'fake_template'
    fake_abbreviations = {
        'gh': 'https://github.com/{}.git',
        'bb': 'https://bitbucket.org/{}',
    }
    fake_clone_to_dir = '/fake/clone/to/directory'
    fake_checkout = 'master'
    fake_no_input = False
    fake_password = 'test123'

    fake_repo_url_1 = 'https://github.com/fake/repo/directory.git'
    fake_repo_url_2 = 'gh:fake/repo/directory'

# Generated at 2022-06-13 18:56:10.553371
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    from cookiecutter.config import DEFAULT_CONFIG

    template = 'https://github.com/audreyr/cookiecutter-pypackage.git'
    dir_, cleanup = determine_repo_dir(
        template,
        DEFAULT_CONFIG['abbreviations'],
        DEFAULT_CONFIG['default_root_dir'],
        None,
        False
    )
    assert 'cookiecutter-pypackage' in dir_
    assert cleanup == False

    template = 'https://github.com/audreyr/cookiecutter-pypackage/zipball/master'

# Generated at 2022-06-13 18:56:17.700476
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    """ Unit test for function determine_repo_dir
    """

    def mock_repository_has_cookiecutter_json(repo_directory):
        """Mock function repository_has_cookiecutter_json
        """
        return True

    abbreviations = {"gh": "https://github.com/{}.git"}
    template = "example_name"
    clone_to_dir = "."
    checkout = "master"
    password = None
    directory = None
    no_input = True

    a_repo_directory = "."

# Generated at 2022-06-13 18:56:23.613821
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    abbreviations = {'gh': 'https://github.com/{}.git'}
    template = 'gh:user/repo:feature'
    clone_to_dir = os.path.abspath('user_repos')
    checkout = 'master'
    no_input = False
    password=None
    directory=None

    determine_repo_dir(template, abbreviations, clone_to_dir, checkout, no_input, password, directory)




# Generated at 2022-06-13 18:56:58.354789
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    """Test function to see if determine repo dir works."""
    determine_repo_dir(template='template',
                       abbreviations=None,
                       clone_to_dir=None,
                       checkout=None,
                       no_input=False,
                       password=None,
                       directory=None)

# Generated at 2022-06-13 18:57:01.271501
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    assert determine_repo_dir('a', {'a': '/tmp/a'}, '/clone', '', True) == ('/tmp/a', False)
    assert determine_repo_dir('/tmp/b', {'a': '/tmp/a'}, '/clone', '', True) == (
        '/tmp/b',
        False,
    )

# Generated at 2022-06-13 18:57:04.891037
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    # Create a local copy of cookiecutter-pypackage/
    dir(determine_repo_dir(template, abbreviations, clone_to_dir, checkout, no_input, password=None, directory=None))

    # Check local cookiecutter-pypackage/ exists
    directory = os.path.dirname(os.path.abspath(__file__))
    template_directory = os.path.join(directory, "cookiecutter-pypackage")
    assert os.path.isdir(template_directory)



# Generated at 2022-06-13 18:57:14.397694
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    abbreviations = {
        'gh': 'https://github.com/{}.git',
        'bb': 'https://bitbucket.org/{}.git',
    }
    assert is_repo_url('https://github.com/test.git')
    assert is_repo_url('git@github.com:test.git')
    assert is_repo_url('git@github.com:test.git')
    assert is_repo_url('https://www.github.com/test.git')
    assert not is_repo_url('https://github.com/test')
    assert not is_repo_url('git@github.com:test')
    assert not is_repo_url('git@github.com/test.git')

# Generated at 2022-06-13 18:57:27.429353
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    """
    should return the expected values

    """
    # given

# Generated at 2022-06-13 18:57:38.387738
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    """Verify the determine_repo_dir function."""
    template = 'gh:audreyr/cookiecutter-pypackage'
    abbreviations = {'gh': 'https://github.com/{}'}
    clone_to_dir = '.'
    checkout = None
    no_input = False
    password = None
    directory = None

    repo_dir, should_cleanup = determine_repo_dir(
        template,
        abbreviations,
        clone_to_dir,
        checkout,
        no_input,
        password,
        directory,
    )

    assert repo_dir == './audreyr-cookiecutter-pypackage'
    assert should_cleanup is False

# Generated at 2022-06-13 18:57:43.153144
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    template = 'https://github.com/audreyr/cookiecutter-pypackage.git'
    abbreviations = {'gh': 'https://github.com/{}.git'}
    template_expanded = expand_abbreviations(template, abbreviations)
    print(template_expanded)
    clone_to_dir = 'C:/Users/hans-/Downloads'
    checkout = None
    no_input = True

    repo_dir, cleanup = determine_repo_dir(
        template_expanded,
        abbreviations,
        clone_to_dir,
        checkout,
        no_input
    )

    print(repo_dir, cleanup)

test_determine_repo_dir()

# Generated at 2022-06-13 18:57:45.206844
# Unit test for function determine_repo_dir
def test_determine_repo_dir():

    assert(determine_repo_dir("user/repo", {}, "", "", False))


# Generated at 2022-06-13 18:57:51.061866
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    assert determine_repo_dir('.', {}, '', None, False) == ('.', False)
    assert determine_repo_dir(
        'https://github.com/foo/bar',
        {},
        '',
        None,
        False,
    ) == ('https://github.com/foo/bar', False)

# Generated at 2022-06-13 18:58:00.200519
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    template = 'https://github.com/audreyr/cookiecutter-pypackage'
    abbreviations = {'gh': 'https://github.com/{}'}
    clone_to_dir = '.test_cookiecutter'
    assert determine_repo_dir(template=template, abbreviations=abbreviations, clone_to_dir=clone_to_dir)[0] == os.path.join(clone_to_dir, 'cookiecutter_pypackage')



# Generated at 2022-06-13 18:59:04.499141
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    res = determine_repo_dir('aalanse/cookiecutter-pypackage', {}, '/tmp/foo', None, True, None, None)
    assert res[0] == '/tmp/foo/cookiecutter-pypackage'

# Generated at 2022-06-13 18:59:13.044690
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    test_template = 'cookiecutter-pypackage'
    test_abbreviations = {
        "gh": "https://github.com/{}.git"
    }
    test_clone_to_dir = 'cookiecutter-pypackage'
    test_checkout = ''
    test_no_input = True,
    expected_output = ('cookiecutter-pypackage', False)
    actual_output = determine_repo_dir(
        template=test_template,
        abbreviations=test_abbreviations,
        clone_to_dir=test_clone_to_dir,
        checkout=test_checkout,
        no_input=test_no_input,
    )
    assert actual_output == expected_output, "Actual output is not equal to expected output"

# Generated at 2022-06-13 18:59:14.320153
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    """
    Unit test for function determine_repo_dir
    """
    assert True

# Generated at 2022-06-13 18:59:16.480053
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    """Test that determine_repo_dir returns the correct repository."""
    determine_repo_dir('my_template', {}, '/tmp', None, True)

# Generated at 2022-06-13 18:59:26.857791
# Unit test for function determine_repo_dir
def test_determine_repo_dir():

    current_directory = os.getcwd()
    template = 'https://github.com/audreyr/cookiecutter-pypackage.git'
    abbreviations = {'gh': 'https://github.com/{}.git'}
    clone_to_dir = os.path.join(current_directory, "repositories")
    checkout = 'version_0_7_2'
    no_input = True
    password = 'test'
    directory = 'cookiecutter-pypackage-master'

    repo_candidate = determine_repo_dir(template,abbreviations,clone_to_dir,checkout,no_input,password,directory)
    print(repo_candidate)

# Generated at 2022-06-13 18:59:33.586483
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    template = '/path/to/repo'
    abbreviations = {'gh': 'https://github.com/{}.git'}
    clone_to_dir = '/tmp/cookiecutter-test'
    checkout = 'master'
    no_input = False
    password = None
    directory = None
    repo_candidate, cleanup = determine_repo_dir(
        template,
        abbreviations,
        clone_to_dir,
        checkout,
        no_input,
        password=password,
        directory=directory,
    )
    assert repo_candidate == '/path/to/repo'
    assert cleanup == False

# Generated at 2022-06-13 18:59:44.360400
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    from cookiecutter.config import DEFAULT_CONFIG

    # setup
    template = 'https://github.com/audreyr/cookiecutter-pypackage.git'
    abbreviations = DEFAULT_CONFIG['abbreviations']
    clone_to_dir = '/tmp'
    checkout = 'master'
    no_input = True
    password = None
    directory = 'tests/workdir/fake-repo-tmpl'
    folder_name = template.split('/')[-1].split('.')[0]
    expected_dir = os.path.join(clone_to_dir, folder_name, directory)

    # run test
    actual_dir, cleanup = determine_repo_dir(template, abbreviations, clone_to_dir, checkout, no_input, password, directory)

    # set test

# Generated at 2022-06-13 18:59:45.188498
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    pass

# Generated at 2022-06-13 18:59:49.283099
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    # Default: no input, not local repo, not URL
    with pytest.raises(RepositoryNotFound):
        determine_repo_dir(
            template='foo',
            abbreviations={},
            clone_to_dir='foo',
            checkout='master',
            no_input=True,
        )


# Generated at 2022-06-13 19:00:04.513563
# Unit test for function determine_repo_dir
def test_determine_repo_dir():
    abbreviations = {
        'gh': 'https://github.com/{}.git',
        'bb': 'https://bitbucket.org/{}.git',
    }
    tests = []
    test_id = 1