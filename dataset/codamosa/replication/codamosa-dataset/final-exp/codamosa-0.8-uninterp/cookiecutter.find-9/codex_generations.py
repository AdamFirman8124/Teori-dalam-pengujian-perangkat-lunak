

# Generated at 2022-06-13 18:27:35.989144
# Unit test for function find_template
def test_find_template():
	pass


# Generated at 2022-06-13 18:27:41.304559
# Unit test for function find_template
def test_find_template():
    """
    Find template when the cookiecutter.json file is in the root directory.
    """
    assert find_template(os.path.join(
        os.path.dirname(os.path.realpath(__file__)), '../fake-repo')) == os.path.join(
            os.path.dirname(os.path.realpath(__file__)), '../fake-repo/fake-project')

# Generated at 2022-06-13 18:27:47.974257
# Unit test for function find_template
def test_find_template():
    """Verify find_template works in the expected way."""
    repo_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'fake-repo'
    )
    assert find_template(repo_dir) == os.path.join(repo_dir, '{{cookiecutter.repo_name}}')

if __name__ == '__main__':
    test_find_template()

# Generated at 2022-06-13 18:27:56.996080
# Unit test for function find_template
def test_find_template():
    dataset = [
        ('tests/test-input/{{cookiecutter.repo_name}}', 'tests/test-input/fake-repo'),
        ('tests/test-input/fake-{{cookiecutter.repo_name}}', 'tests/test-input/fake-repo-name'),
        ('tests/test-input/{{cookiecutter.repo_name}}-fake', 'tests/test-input/repo-name-fake'),
        ('tests/test-input/{{cookiecutter.repo_name}}-{{cookiecutter.project_name}}', 'tests/test-input/repo-name-project-name'),
    ]

    for result, directory in dataset:
        assert result == find_template(directory)

# Generated at 2022-06-13 18:28:04.482503
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.join(os.path.abspath(os.getcwd()),'../test-repo/tests/test-repo-tmpl/')
    project_template = os.path.join(repo_dir, '{{cookiecutter.repo_name}}')
    assert find_template(repo_dir) == project_template

# Generated at 2022-06-13 18:28:10.612964
# Unit test for function find_template
def test_find_template():
    from cookiecutter.prompt import read_user_variable
    from cookiecutter.repository import clone

    result_dir, project_dir = clone(
        'https://github.com/audreyr/cookiecutter-pypackage.git',
        'foobar',
        no_input=True,
        checkout=None,
        clone=True,
        overwrite_if_exists=True,
        password=None,
        skip_if_file_exists=False,
        extra_context={},
        password=None,
        username=None,
        verify_ssl=True,
    )
    assert project_dir == find_template(result_dir)

# Generated at 2022-06-13 18:28:18.194503
# Unit test for function find_template
def test_find_template():
    assert find_template('tests/fake-repo-pre/') == 'tests/fake-repo-pre/fake-repo/{{cookiecutter.repo_name}}'
    assert find_template('tests/fake-repo-pre/fake-repo/') == 'tests/fake-repo-pre/fake-repo/{{cookiecutter.repo_name}}'
    assert find_template('tests/fake-repo-pre/fake-repo') == 'tests/fake-repo-pre/fake-repo/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:28:25.330611
# Unit test for function find_template
def test_find_template():
    import tempfile

    test_project_template = tempfile.mkdtemp()
    test_template_file = tempfile.NamedTemporaryFile(
        mode='w+',
        dir=test_project_template,
        delete=False,
        prefix='cookiecutter-{{'
    )
    test_template_file.close()

    assert find_template(test_project_template) == test_template_file.name

# Generated at 2022-06-13 18:28:30.183157
# Unit test for function find_template
def test_find_template():
    # Local path to the cookiecutter-pypackage/ directory.
    repo_dir = os.path.abspath(os.path.dirname(__file__))
    result = find_template(repo_dir)
    assert result == repo_dir

if __name__ == '__main__':
    test_find_template()

# Generated at 2022-06-13 18:28:35.441683
# Unit test for function find_template
def test_find_template():
    repo_dir = 'tests\\test-repo'
    repo_dir_contents = ['PyPI_project', '{{cookiecutter.project_slug}}']
    os.listdir = lambda x: repo_dir_contents
    assert find_template(repo_dir) == 'tests\\test-repo\\PyPI_project'

# Generated at 2022-06-13 18:28:41.219717
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.abspath('tests/fake-repo-tmpl')
    expected_template = os.path.join(repo_dir, '{{cookiecutter.repo_name}}')
    assert find_template(repo_dir) == expected_template



# Generated at 2022-06-13 18:28:46.054221
# Unit test for function find_template
def test_find_template():
    """ Test function find_template()
    """
    from cookiecutter import main

    current_dir = os.getcwd()
    main.cookiecutter(
        'tests/test-find-template/',
        no_input=True,
        overwrite_if_exists=True,
        output_dir=current_dir,
    )

    assert os.path.exists('mysql-master')
    assert os.path.exists('mysql-master/mysql-master-{{cookiecutter.repo_name}}')

# Generated at 2022-06-13 18:28:56.531389
# Unit test for function find_template
def test_find_template():
    """
    Unit test for function find_template.
    :returns exit_code: 0 on success, 1 on failure.
    """
    from .utils import make_repo
    import tempfile
    import shutil


# Generated at 2022-06-13 18:29:02.045838
# Unit test for function find_template
def test_find_template():
    """Test function `find_template`."""

    test_dir = os.path.join(
        os.path.dirname(__file__),
        '..',
        'tests',
        'test-input'
    )
    test_template_find = find_template(test_dir)
    assert test_template_find == os.path.join(
        test_dir,
        '{{cookiecutter.repo_name}}'
    )



# Generated at 2022-06-13 18:29:08.730742
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.join(
        os.path.abspath(os.path.dirname(__file__)), '..', 'tests', 'fake-repo'
    )
    project_template = find_template(repo_dir)
    assert project_template == os.path.join(repo_dir, '{{cookiecutter.repo_name}}')

# Generated at 2022-06-13 18:29:17.295679
# Unit test for function find_template
def test_find_template():
    import tempfile
    import shutil
    temp_dir = tempfile.mkdtemp()
    content = (
        '# this is a cookiecutter template\n'
        '{{ cookiecutter.project_name }}'
    )
    file_path = os.path.join(temp_dir, '{{cookiecutter.project_name}}')
    open(file_path, 'w').write(content)
    assert find_template(temp_dir) == file_path

    shutil.rmtree(temp_dir)



# Generated at 2022-06-13 18:29:22.415840
# Unit test for function find_template
def test_find_template():
    # test_dir = os.path.join(os.getcwd(), 'tests/test-find-template/')
    test_dir = 'tests/test-find-template/'
    assert find_template(test_dir) == os.path.join(test_dir, '{{cookiecutter.rtd_project_name}}')

# Generated at 2022-06-13 18:29:29.017486
# Unit test for function find_template
def test_find_template():
    """ Test the find_template function """
    from cookiecutter.main import cookiecutter
    template_dir = cookiecutter(
        'https://github.com/audreyr/cookiecutter-pypackage.git',
        'temp',
        no_input=True
    )[1]
    os.rmdir(os.path.join(template_dir, 'cookiecutter-pypackage'))
    assert find_template(template_dir) == os.path.join(
        template_dir,
        'cookiecutter-pypackage'
    )

# Generated at 2022-06-13 18:29:33.843583
# Unit test for function find_template
def test_find_template():
    """Unit test for function find_template."""

    find_template("/Users/gengwg/Documents/course/cookiecutter-template/cookiecutter-pypackage")
    #find_template("/Users/gengwg/Documents/course/cookiecutter-template/cookiecutter-django")

# Generated at 2022-06-13 18:29:43.253609
# Unit test for function find_template
def test_find_template():
    import shutil

    test_dir = os.path.join(os.path.dirname(__file__), 'test_find_template')
    template_dir = os.path.join(test_dir, 'foobar-cookiecutter-{{cookiecutter.repo_name}}')

    if not os.path.exists(template_dir):
        shutil.copytree(
            os.path.join(test_dir, 'foobar-cookiecutter-cookiecutter-example'),
            template_dir
        )

    try:
        template_found = find_template(test_dir)
        assert template_found == template_dir
    finally:
        shutil.rmtree(template_dir)

# Generated at 2022-06-13 18:29:55.601946
# Unit test for function find_template
def test_find_template():
    from cookiecutter.compat import TemporaryDirectory

    with TemporaryDirectory() as repo_dir:
        expected_result = os.path.join(repo_dir, '{{cookiecutter.project_name}}')
        os.makedirs(expected_result)
        output = find_template(repo_dir)
        assert output == expected_result

    try:
        output = find_template(repo_dir)
        assert False, 'expected NonTemplatedInputDirException'
    except NonTemplatedInputDirException:
        pass

# Generated at 2022-06-13 18:30:05.367275
# Unit test for function find_template
def test_find_template():
    """Test that find_template() returns the correct template path."""
    import shutil
    from cookiecutter.repository import determine_repo_dir
    from cookiecutter.utils import rmtree

    # Create a fake repository
    repo_path = "tests/fake-repo-tmpl/"
    repo_dir = determine_repo_dir(repo_path)
    template_dir = "tests/fake-repo-pre/"

    # Test if the template is detected correctly
    shutil.copytree(template_dir, repo_dir)
    assert find_template(repo_dir) == os.path.join(repo_dir, "{{cookiecutter.repo_name}}")

    # Clean up fake repository
    rmtree(repo_path)

    return

# Generated at 2022-06-13 18:30:11.704820
# Unit test for function find_template
def test_find_template():
    """
    Determine if the function finds the template.
    """
    template_dir = 'tests/fake-repo-tmpl'
    assert find_template(template_dir) == 'tests/fake-repo-tmpl/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:30:19.160178
# Unit test for function find_template
def test_find_template():
    """Unit test for function find_template"""
    logging.disable(logging.CRITICAL)
    file_path = os.path.dirname(os.path.abspath(__file__))
    test_dir = os.path.join(file_path, 'test_find_template')
    assert find_template(test_dir) == os.path.join(test_dir, '{{cookiecutter.repo_name}}')

# Generated at 2022-06-13 18:30:26.609213
# Unit test for function find_template
def test_find_template():
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
    template_dir = os.path.join(root_dir, 'tests/fake-repo-tmpl')
    expected_result = os.path.join(template_dir, '{{cookiecutter.repo_name}}')
    assert find_template(template_dir) == expected_result



# Generated at 2022-06-13 18:30:29.890930
# Unit test for function find_template
def test_find_template():
    """Unit test for the find_template function."""
    path = 'tests/test-find-file/test-template'

    project_template = find_template(path)

    assert project_template == 'tests/test-find-file/test-template/test-template'

# Generated at 2022-06-13 18:30:42.325171
# Unit test for function find_template
def test_find_template():
    """Test find_template removing stubs and testing for error"""
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    os.chdir('..')
    os.chdir('..')
    os.chdir('tests')
    import shutil
    shutil.rmtree('repo-with-project-template')
    shutil.rmtree('repo-without-project-template')
    os.mkdir('repo-with-project-template')
    with open('repo-with-project-template/test.test','w') as f:
        f.write('test')
    with open('repo-with-project-template/cookiecutter-test','w') as f:
        f.write('test')

# Generated at 2022-06-13 18:30:47.560781
# Unit test for function find_template
def test_find_template():
    """Test to see if find_template can find a project template."""
    real_dir = os.path.dirname(os.path.realpath(__file__))

    repo_dir = os.path.join(real_dir, 'fake-repo-pre')
    project_template = find_template(repo_dir)

    assert '{{' in project_template
    assert '}}' in project_template



# Generated at 2022-06-13 18:30:52.382322
# Unit test for function find_template
def test_find_template():
    """
    Tests function find_template
    """
    from .compat import mock
    from .exceptions import NonTemplatedInputDirException
    from .main import find_template
    from .main import logger
    
    # Set up mock
    mock_listdir = mock.Mock()
    mock_listdir.return_value = [
        'fake_directory',
        'fake_project_template_cookiecutter.png'
    ]
    
    # Set up mock, then patch it
    mock_os = mock.Mock()
    mock_os.listdir = mock_listdir
    mock_os.path.join = os.path.join
    
    # Mock logger
    mock_logger = mock.MagicMock()
    
    # Use mock objects for open and listdir, then patch it

# Generated at 2022-06-13 18:30:53.164064
# Unit test for function find_template
def test_find_template():
    pass

# Generated at 2022-06-13 18:31:02.489697
# Unit test for function find_template
def test_find_template():
    """Test the find_template function"""
    os.chdir('tests/files/fake-repo-pre-commit/')    
    expected = 'tests/files/fake-repo-pre-commit'
    assert find_template(os.getcwd()) == expected


# Generated at 2022-06-13 18:31:08.080413
# Unit test for function find_template
def test_find_template():
    """
    Tests for the function find_template.
    """
    test_dir = os.path.abspath(os.path.dirname(__file__))
    fixture_dir = os.path.join(test_dir, 'fixtures/fake-repo-pre/')

    actual_repo_dir = find_template(fixture_dir)

    expected_repo_dir = os.path.join(fixture_dir, '{{cookiecutter.repo_name}}/')

    assert actual_repo_dir == expected_repo_dir

# Generated at 2022-06-13 18:31:12.996696
# Unit test for function find_template
def test_find_template():
    # test for a valid template
    assert 'example_nested' in find_template('test_repo')

    # test for a *non-valid* template
    assert 'example_nested' not in find_template('test_repo_missing')

# Generated at 2022-06-13 18:31:21.600236
# Unit test for function find_template
def test_find_template():

    test_template_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        '..',
        'tests',
        'test-find-repo'
    )

    test_template_name = 'cookiecutter-pypackage'

    test_template = find_template(test_template_dir)

    assert test_template == test_template_dir + \
        '/{{cookiecutter.project_slug}}'

# Generated at 2022-06-13 18:31:22.883118
# Unit test for function find_template
def test_find_template():
    pass

# Generated at 2022-06-13 18:31:27.755890
# Unit test for function find_template
def test_find_template():
    user_config_path = '/home/user/.cookiecutters/cookiecutter-pypackage'
    from os.path import isdir
    assert isdir(user_config_path)
    find_template(user_config_path)

# Generated at 2022-06-13 18:31:36.399991
# Unit test for function find_template
def test_find_template():
    import shutil
    import tempfile
    from cookiecutter.utils import rmtree

    temp_dir = tempfile.mkdtemp()
    project_dir = os.path.join(temp_dir, 'foobarbaz-{{cookiecutter.repo_name}}')
    os.makedirs(project_dir)
    project_template = find_template(temp_dir)
    assert project_template == project_dir
    rmtree(temp_dir)



# Generated at 2022-06-13 18:31:40.185731
# Unit test for function find_template
def test_find_template():
    test_dir = '/path/to/test/dir'
    assert find_template(test_dir) == '/path/to/test/dir/cookiecutter-{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:31:50.145667
# Unit test for function find_template
def test_find_template():
    repo_dir = "/tmp/cookiecutter-random"
    os.makedirs(repo_dir)
    os.makedirs(os.path.join(repo_dir, "cookiecutter-random-{{cookiecutter.repo_name}}"))
    repo_dir_contents = os.listdir(repo_dir)
    project_template = find_template(repo_dir)
    assert project_template == os.path.join(repo_dir, "cookiecutter-random-{{cookiecutter.repo_name}}")

# Generated at 2022-06-13 18:31:55.659256
# Unit test for function find_template
def test_find_template():

    repo_dir = '/Users/yotam/PycharmProjects/cookiecutter/tests/test-repo/'

    find_template(repo_dir)
    # assert find_template(repo_dir) == '/Users/yotam/PycharmProjects/cookiecutter/tests/test-repo/cookiecutter-pypackage'

# Generated at 2022-06-13 18:32:11.238492
# Unit test for function find_template
def test_find_template():
    repo_dir = '/home/audreyr/cookiecutter-pypackage'
    project_template = '/home/audreyr/cookiecutter-pypackage/{{cookiecutter.project_name}}'

    assert find_template(repo_dir=repo_dir) == project_template

# Generated at 2022-06-13 18:32:13.997634
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.dirname(__file__)
    project_template = find_template(repo_dir)
    assert isinstance(project_template, basestring)

# Generated at 2022-06-13 18:32:17.260924
# Unit test for function find_template
def test_find_template():
    test_dir = 'tests/files/'
    assert find_template(test_dir) == os.path.join(test_dir, 'cookiecutter-{{cookiecutter.repo_name}}')

# Generated at 2022-06-13 18:32:18.760829
# Unit test for function find_template
def test_find_template():
    """Test function find_template
    """
    assert find_template('.') is None

# Generated at 2022-06-13 18:32:22.322543
# Unit test for function find_template
def test_find_template():
    repo_dir = 'tests/test-find-template'
    expected_template = 'tests/test-find-template/simple-{{cookiecutter.repo_name}}'
    template = find_template(repo_dir)
    assert template == expected_template

# Generated at 2022-06-13 18:32:25.816456
# Unit test for function find_template
def test_find_template():
    """
    Unit test for function find_template
    """
    repo_dir = '/home/nonrootuser/cookiecutter-pypackage'
    project_template = find_template(repo_dir)
    assert project_template == '/home/nonrootuser/cookiecutter-pypackage/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:32:35.196154
# Unit test for function find_template
def test_find_template():
    from cookiecutter.tests.test_find import TEST_TEMPLATES_DIR
    from cookiecutter.compat import input

    template_dir = os.path.join(TEST_TEMPLATES_DIR, '_abbreviated-repo-tmpl')

    try:
        find_template(template_dir)
    except NonTemplatedInputDirException:
        pass
    else:
        raise AssertionError(
            "Should have received a NonTemplatedInputDirException "
            "when trying to find template from abbrev repo."
        )

    template_dir = os.path.join(TEST_TEMPLATES_DIR, '_bakery-scaffold-tmpl')
    returned = find_template(template_dir)

# Generated at 2022-06-13 18:32:43.274318
# Unit test for function find_template
def test_find_template():
    import tempfile
    import shutil
    import sys
    import os

    def touch(path):
        with open(path, 'a'):
            os.utime(path, None)

    # odd test code. #Evee

    temp_dir = tempfile.mkdtemp()
    cwd = os.getcwd()


# Generated at 2022-06-13 18:32:50.440740
# Unit test for function find_template
def test_find_template():
    '''
    Unit test for function find_template
    '''

# Generated at 2022-06-13 18:32:52.273176
# Unit test for function find_template
def test_find_template():
    """Unit test for find_template()"""
    template_dir = "./tests/fake-repo/{{cookiecutter.repo_name}}"
    assert find_template("./tests/fake-repo/") == template_dir

# Generated at 2022-06-13 18:33:20.296682
# Unit test for function find_template
def test_find_template():
    from cookiecutter import utils
    from cookiecutter.config import get_user_config
    from cookiecutter import DEFAULT_CONFIG
    from cookiecutter import exceptions

    repo_path = '/Users/audreyr/cookiecutters/cookiecutter-pypackage'

    user_config = get_user_config(
        config_file=DEFAULT_CONFIG['config_file'],
        defaults=DEFAULT_CONFIG,
    )
    utils.git.git_clone(user_config['cookiecutters_dir'], repo_path)

    project_template = find_template(repo_path)

    assert project_template == '/Users/audreyr/cookiecutters/cookiecutter-pypackage/{{cookiecutter.repo_name}}'


# Generated at 2022-06-13 18:33:23.248619
# Unit test for function find_template
def test_find_template():
    """Test function `find_template`"""
    result = find_template('/home/foo/bar')
    assert result == os.path.join('/home/foo/bar', 'cookiecutter-pypackage')

# Generated at 2022-06-13 18:33:26.596383
# Unit test for function find_template
def test_find_template():
    print(find_template('/Users/olgabot/repos/cookiecutter-pypackage/tests/test-output'))
test_find_template()

# Generated at 2022-06-13 18:33:31.076481
# Unit test for function find_template
def test_find_template():
    repo_dir = '/Users/audreyr/cookiecutter-pypackage/'
    expected = '/Users/audreyr/cookiecutter-pypackage/{{cookiecutter.repo_name}}'

    assert find_template(repo_dir) == expected

# Generated at 2022-06-13 18:33:40.592396
# Unit test for function find_template
def test_find_template():
    import os
    import tempfile
    from cookiecutter import utils
    from cookiecutter.exceptions import NonTemplatedInputDirException

    cwd = os.getcwd()
    repo_dir = os.path.join(cwd, 'tests/test-repo/')
    template = utils.find_template(repo_dir)
    assert template == os.path.join(repo_dir, '{{cookiecutter.repo_name}}')

    tmp_dir, new_repo_dir = tempfile.mkstemp(suffix='-cookiecutter')
    try:
        utils.rmtree(new_repo_dir)
    except (OSError, IOError):
        pass
    os.mkdir(new_repo_dir)

# Generated at 2022-06-13 18:33:46.074805
# Unit test for function find_template
def test_find_template():
    """Test the find_template() function"""
    repo_dir = os.path.join(os.getcwd(), 'tests', 'fake-repo')
    project_template = find_template(repo_dir)
    expected_project_template = os.path.join(repo_dir, 'cookiecutter-{{cookiecutter.repo_name}}')
    assert project_template == expected_project_template

# Generated at 2022-06-13 18:33:54.910584
# Unit test for function find_template
def test_find_template():
    """Tests for find_template"""
    from cookiecutter import utils
    from cookiecutter.config import DEFAULT_CONFIG
    from cookiecutter.exceptions import NonTemplatedInputDirException
    from cookiecutter.utils import rmtree
    from . import TEST_TEMPLATES_DIR

    #
    # Setup
    #

    env_vars = ('HOME', 'USERPROFILE')
    for env_var in env_vars:
        try:
            user_home = os.environ[env_var]
        except KeyError:
            pass
    user_home = os.path.expanduser('~')

    #
    # Tests
    #

    # Invalid
    # repo_dir_path is None
    with pytest.raises(NonTemplatedInputDirException):
        find

# Generated at 2022-06-13 18:33:59.222102
# Unit test for function find_template
def test_find_template():
    """Test the `find_template` function."""
    assert find_template('tests/test-input') == \
        os.path.join('tests/test-input', '{{cookiecutter.repo_name}}')


# TODO: Fix.

# Generated at 2022-06-13 18:34:11.199315
# Unit test for function find_template

# Generated at 2022-06-13 18:34:24.595103
# Unit test for function find_template
def test_find_template():
    # Import os.path module
    import os.path
    # Import os.path.isdir function
    from os.path import isdir
    # Import os.makedirs function
    from os import makedirs
    # Import shutil module
    import shutil
    # Import tempfile module
    import tempfile
    # Import filecmp module
    import filecmp
    # Import test_find_template function
    from cookiecutter.utils import find_template

    # Prepare a temporary directory to work in
    temp_dir = tempfile.mkdtemp(prefix='cookiecutter-')
    # Prepare directory containing the fixture
    fixture_dir = os.path.join(temp_dir, 'test')
    # Prepare a directory containing the expected output
    expected_dir = os.path.join(temp_dir, 'expected')
    # Prepare

# Generated at 2022-06-13 18:35:17.137554
# Unit test for function find_template
def test_find_template():
    assert find_template('/Users/audreyr/cookiecutter-pypackage/tests/') == \
        '/Users/audreyr/cookiecutter-pypackage/tests/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:35:23.805969
# Unit test for function find_template
def test_find_template():
    """Verify function for finding a template in a newly cloned project works."""
    test_repo_dir = os.path.join(
        os.path.dirname(__file__),
        'test_repo'
    )
    template = find_template(test_repo_dir)
    assert os.path.exists(template)

# Generated at 2022-06-13 18:35:26.946884
# Unit test for function find_template
def test_find_template():
    """Tests that the correct template is found."""
    repo_dir = '.tests/'
    project_template = 'fake-project-template'

    correct_template = find_template(repo_dir)
    assert correct_template.endswith(project_template)

# Generated at 2022-06-13 18:35:35.737877
# Unit test for function find_template
def test_find_template():
    """Test that the find_template function works as expected."""
    from cookiecutter import utils
    from cookiecutter.compat import UnicodeMixin
    from cookiecutter import exceptions

    class MockRepoDir(UnicodeMixin):
        """
        Defines a "mock" repository that the function find_template can find the
        file name of a template in.

        The test should pass if the "template" file is detected from within the
        "mock" repository.

        The test should fail if the "not_template" file is detected from within
        the "mock" repository.
        """
        def __init__(self, template_file_name, not_template_file_name):
            self.template_file_name = template_file_name
            self.not_template_file_name = not_template_file

# Generated at 2022-06-13 18:35:36.653186
# Unit test for function find_template
def test_find_template():
    """ """
    pass

# Generated at 2022-06-13 18:35:40.586711
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.join('tests', 'fake-repo')
    project_template = find_template(repo_dir)
    assert 'tests/fake-repo/{{cookiecutter.project_name}}' in project_template

# Generated at 2022-06-13 18:35:43.627940
# Unit test for function find_template
def test_find_template():
    """Unit test for function find_template."""
    # import pytest
    # import os
    # os.chdir('test/test-cookiecutter/fake-repo-pre/')
    # repo_dir = os.getcwd()
    # project_template = find_template(repo_dir)
    # assert 'fake-repo-pre' in project_template
    # assert 'cookiecutter-pypackage' in project_template
    # os.chdir('../..')
    pass

# Generated at 2022-06-13 18:35:49.985992
# Unit test for function find_template
def test_find_template():
    """Verify find_template function."""
    from cookiecutter.main import cookiecutter

    context = cookiecutter('tests/fake-repo-templated', no_input=True)

    template_dir = find_template('tests/fake-repo-templated')
    assert template_dir == 'tests/fake-repo-templated/{{cookiecutter.repo_name}}'



# Generated at 2022-06-13 18:35:58.009936
# Unit test for function find_template
def test_find_template():
    import shutil
    import tempfile

    template_dir = tempfile.mkdtemp()

    try:
        os.makedirs(os.path.join(template_dir, 'my-repo'))
        os.makedirs(os.path.join(template_dir, 'my-repo', '{{cookiecutter.repo_name}}'))

        template = find_template(os.path.join(template_dir, 'my-repo'))
        assert template.endswith(os.path.join(template_dir, 'my-repo', '{{cookiecutter.repo_name}}'))

    finally:
        shutil.rmtree(template_dir)

# Generated at 2022-06-13 18:35:59.246767
# Unit test for function find_template
def test_find_template():
    pass
