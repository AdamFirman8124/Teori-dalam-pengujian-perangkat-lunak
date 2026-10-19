

# Generated at 2022-06-13 18:27:44.121071
# Unit test for function find_template
def test_find_template():
    from cookiecutter import main
    from cookiecutter.config import DEFAULT_CONFIG
    from cookiecutter.environment import StrictEnvironment
    from cookiecutter.exceptions import NonTemplatedInputDirException

    repo_path = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        '..',
        'tests',
        'test-repo-pre-abbreviations',
    )
    repo_path = os.path.normpath(repo_path)
    template_path = find_template(repo_path)
    assert os.path.exists(template_path)
    assert '{{' in template_path
    assert '}}' in template_path


# Generated at 2022-06-13 18:27:53.547097
# Unit test for function find_template
def test_find_template():
    """Validate the find_template function with valid and invalid directories."""
    directory = os.path.join('tests', 'fake-repo-tmpl')
    assert find_template(directory) == os.path.join('tests', 'fake-repo-tmpl', '{{cookiecutter.repo_name}}')
    directory = os.path.join('tests', 'fake-repo-pre')
    try:
        assert find_template(directory)
    except NonTemplatedInputDirException:
        assert True

# Generated at 2022-06-13 18:28:06.623762
# Unit test for function find_template
def test_find_template():
    """
    Unit test for function find_template
    """
    import os
    import tempfile

    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()

    # Create project-dir in temporary directory
    test_dir = os.path.join(temp_dir, "project-dir")
    os.makedirs(test_dir)

    # Create cookiecutter-dir.
    template_dir = os.path.join(temp_dir, "cookiecutter-django")
    os.makedirs(template_dir)

    # Create file in cookiecutter-dir
    template_file = os.path.join(template_dir, '{{ cookiecutter.project_name }}')
    f = open(template_file, 'w')
    f.write("This is a test!")

# Generated at 2022-06-13 18:28:13.233061
# Unit test for function find_template
def test_find_template():
    template = find_template(os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'project_template'
    ))

    assert template == os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'project_template',
        'cookiecutter-pypackage'
    )

# Generated at 2022-06-13 18:28:21.208912
# Unit test for function find_template
def test_find_template():
    """Verify repo_dir returns correct project template"""
    repo_dir_contents = os.listdir('fake-repo')

    project_template = None
    for item in repo_dir_contents:
        if 'cookiecutter' in item and '{{' in item and '}}' in item:
            project_template = item
            break

    assert project_template == 'cookiecutter-pypackage'

# Generated at 2022-06-13 18:28:21.910483
# Unit test for function find_template
def test_find_template():
    pass

# Generated at 2022-06-13 18:28:27.967679
# Unit test for function find_template
def test_find_template():
    test_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tests")
    assert find_template(
        os.path.join(test_dir, "fake-repo-precached")
    ) == os.path.join(test_dir, "fake-repo-precached", "{{cookiecutter.repo_name}}")

# Generated at 2022-06-13 18:28:34.192141
# Unit test for function find_template
def test_find_template():

    from cookiecutter.utils import rmtree

    temp_dir = 'tests/files/fake-repo-tmpl'
    template = find_template(temp_dir)
    expected = os.path.normpath(os.path.join(temp_dir, '{{cookiecutter.repo_name}}'))
    assert template == expected

    # Clean up
    rmtree(temp_dir)

# Generated at 2022-06-13 18:28:40.005187
# Unit test for function find_template
def test_find_template():
    test_repo_dir = '/Users/audreyr/Documents/GitHub/cookiecutter-pypackage'
    result = find_template(test_repo_dir)
    assert result == '/Users/audreyr/Documents/GitHub/cookiecutter-pypackage/{{cookiecutter.repo_name}}'



# Generated at 2022-06-13 18:28:41.894688
# Unit test for function find_template
def test_find_template():
    assert find_template('/home/invalidUser/Cookiecutter/') == 'Cookiecutter/'

# Generated at 2022-06-13 18:28:53.979663
# Unit test for function find_template
def test_find_template():
    """Function for unit testing find_template function"""
    from os import (
        getcwd,
        rmdir,
        listdir
    )

    from cookiecutter import (
        utils,
        exceptions
    )

    template_dir = 'test_template'
    os.mkdir(template_dir)
    with open(os.path.join(template_dir, 'cookiecutter.json'), 'w') as f:
        f.write('''
        {{cookiecutter.repo_dir}}
        ''')

    assert (
        listdir(os.path.join(getcwd(), template_dir)) == ['cookiecutter.json']
    )
    assert (
        utils.find_template(getcwd()) == os.path.join(getcwd(), template_dir)
    )

# Generated at 2022-06-13 18:28:58.490661
# Unit test for function find_template
def test_find_template():
    input_test_dir = 'cookiecutter-testing/input-project'
    test_result = find_template(input_test_dir)
    assert 'input-project/{{cookiecutter.repo_name}}' in test_result

# Generated at 2022-06-13 18:29:02.586299
# Unit test for function find_template
def test_find_template():
    test_repo_dir = os.path.abspath('tests/test-output/fake-repo')
    test_template = os.path.abspath(
        'tests/test-output/fake-repo/cookiecutter-pypackage')

    assert find_template(test_repo_dir) == test_template


# Generated at 2022-06-13 18:29:04.487218
# Unit test for function find_template
def test_find_template():
    find_template('/home/user/Desktop/simple-django-cookie')

# Generated at 2022-06-13 18:29:17.378920
# Unit test for function find_template
def test_find_template():
    """Determine which child directory of `repo_dir` is the project template.

    :param repo_dir: Local directory of newly cloned repo.
    :returns project_template: Relative path to project template.
    """
    print('testing function find_template...')
    repo_dir = os.getcwd()
    repo_dir_contents = os.listdir(repo_dir)
    project_template = None
    for item in repo_dir_contents:
        if 'cookiecutter' in item and '{{' in item and '}}' in item:
            project_template = item
            break

    if project_template:
        project_template = os.path.join(repo_dir, project_template)
        print(project_template)
        return project_template
    else:
        raise NonTem

# Generated at 2022-06-13 18:29:27.628018
# Unit test for function find_template
def test_find_template():
    """Unit test for ``find_template`` function."""
    import tempfile

    # Create a temp dir, and add two regular folders
    tmp_dir = tempfile.mkdtemp()
    first_dir = os.path.join(tmp_dir, 'first_dir')
    second_dir = os.path.join(tmp_dir, 'second_dir')
    os.mkdir(first_dir)
    os.mkdir(second_dir)

    # Add a templated dir
    templated_dir = os.path.join(tmp_dir, '{{cookiecutter.repo_name}}')
    os.mkdir(templated_dir)

    # Try to find the template dir
    found_dir = find_template(tmp_dir)
    expected_dir = templated_dir
    assert found_

# Generated at 2022-06-13 18:29:28.616482
# Unit test for function find_template
def test_find_template():
    find_template('repo_dir')
    assert True

# Generated at 2022-06-13 18:29:33.121682
# Unit test for function find_template
def test_find_template():
    """Verify that find_template returns the expected value."""
    test_dir = "tests/test-find-template"
    assert find_template(test_dir) == test_dir + '/cookiecutter-foo{{cookiecutter.repo_name}}'


# Generated at 2022-06-13 18:29:39.324250
# Unit test for function find_template
def test_find_template():
    """Verify if the template directory is found properly."""
    from cookiecutter.tests.test_utils.fake_project import make_fake_repo
    from cookiecutter import utils

    test_repo = make_fake_repo('tests/fake-repo-tmpl')
    found_template = utils.find_template(test_repo)
    assert found_template == os.path.join(test_repo, 'fake-project', '{{cookiecutter.repo_name}}')


# Generated at 2022-06-13 18:29:46.645409
# Unit test for function find_template
def test_find_template():
    """Find the project template from a zip file."""
    from .archive import unzip_file
    from .utils import rmtree
    from .config import get_user_config

    user_config = get_user_config(False)

    template = 'https://github.com/audreyr/cookiecutter-pypackage.git'

    new_repo_dir = unzip_file(template, user_config['replay_dir'])

    project_template = find_template(new_repo_dir)

    rmtree(new_repo_dir)

    assert 'cookiecutter-pypackage' in project_template

# Generated at 2022-06-13 18:29:59.922492
# Unit test for function find_template
def test_find_template():
    """Test the find_template function"""
    base_dir = os.path.split(os.getcwd())
    repo_dir = os.path.join(base_dir, 'tests/fake-repo-pre/')
    project_template = find_template(repo_dir)
    assert project_template == 'tests/fake-repo-pre/{{cookiecutter.repo_name}}'
    
    repo_dir = os.path.join(base_dir, 'tests/fake-repo-post/')
    project_template = find_template(repo_dir)
    assert project_template == 'tests/fake-repo-post/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:30:08.950111
# Unit test for function find_template
def test_find_template():
    import os
    import shutil
    import tempfile

    TEST_REPO = tempfile.mkdtemp()
    TEMPLATE_NAME = 'cookiecutter-pypackage'

    template_dir = os.path.join(TEST_REPO, TEMPLATE_NAME)
    os.makedirs(template_dir)

    template_dir_analogue = os.path.join(TEST_REPO, 'cookiecutter-project')
    os.makedirs(template_dir_analogue)

    found_template = find_template(TEST_REPO)

    assert found_template == template_dir

    shutil.rmtree(TEST_REPO)

# Generated at 2022-06-13 18:30:14.048353
# Unit test for function find_template
def test_find_template():
    current_dir = os.path.dirname(__file__)
    repo_dir = os.path.join(current_dir, os.pardir, 'tests')
    template_dir = find_template(repo_dir)
    assert template_dir == os.path.join(repo_dir, 'fake-repo-pre/')

# Generated at 2022-06-13 18:30:16.795049
# Unit test for function find_template
def test_find_template():
    """Unit test for function find_template."""
    #TODO
    pass

# Generated at 2022-06-13 18:30:22.878496
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.join(os.getcwd(), 'tests/fake-repo-pre/')
    project_template = find_template(repo_dir)
    project_template_expected = os.path.join(repo_dir, '{{cookiecutter.repo_name}}')
    assert project_template == project_template_expected

# Generated at 2022-06-13 18:30:28.441990
# Unit test for function find_template
def test_find_template():
    """Function to test find_template with mocked filesystem."""
    from mock import Mock, patch

    # set up mock object to represent repo_dir
    mock_repo_dir = Mock()
    # mock repo_dir for testing
    # so it only contains one file that is not cookiecutter-formatted
    mock_repo_dir.listdir.return_value = ['readme']
    # run find_template function with mock repo_dir
    logger.debug('About to run test_find_template1')
    test_find_template1 = find_template(mock_repo_dir)
    # assert that it was not able to find a cookiecutter-formatted file
    logger.debug('About to assert test_find_template1 == None')
    assert test_find_template1 == None

    # mock repo_dir for testing


# Generated at 2022-06-13 18:30:36.023862
# Unit test for function find_template
def test_find_template():
    OTHER_DIR = os.path.dirname(os.path.abspath(__file__))
    TEMPLATE = 'cookiecutter-pypackage'
    TEMPLATE_DIR = os.path.join(OTHER_DIR, TEMPLATE)

    template = find_template(TEMPLATE_DIR)

    assert template == os.path.join(TEMPLATE_DIR, '{{cookiecutter.repo_name}}')

# Generated at 2022-06-13 18:30:41.123949
# Unit test for function find_template
def test_find_template():
    """Verify that find_template() returns the correct project template."""
    this_dir = os.path.dirname(os.path.abspath(__file__))
    repo_dir = os.path.join(this_dir, '..', 'fake-repo')

    assert find_template(repo_dir) == \
        os.path.abspath(os.path.join(repo_dir, '{{cookiecutter.repo_name}}'))

# Generated at 2022-06-13 18:30:52.571188
# Unit test for function find_template
def test_find_template():
    import shutil
    import tempfile
    import textwrap

    os.chdir(os.path.dirname(__file__))

    # Create a repo with a non-templated and templated directory
    non_templated_dir = os.path.join(tempfile.mkdtemp(), 'project-repo')
    with open(os.path.join(non_templated_dir, 'README.md'), 'w') as f:
        f.write('# Project Repo')
    templated_dir = os.path.join(non_templated_dir, '{{project_name}}')
    os.makedirs(templated_dir)

# Generated at 2022-06-13 18:30:58.336650
# Unit test for function find_template
def test_find_template():
    """Test to verify that it works."""
    repo_dir = os.path.join(os.path.dirname(__file__), '..', 'fake-repo')
    project_template = find_template(repo_dir)
    assert project_template == os.path.join(repo_dir, 'fake_project_tmpl')

# Generated at 2022-06-13 18:31:09.907817
# Unit test for function find_template
def test_find_template():
    repo_dir = "/home/username/cc_templates/cookiecutter-pypackage"
    project_template = find_template(repo_dir)
    assert project_template == "/home/username/cc_templates/cookiecutter-pypackage/{{cookiecutter.repo_name}}"

# Generated at 2022-06-13 18:31:11.715307
# Unit test for function find_template
def test_find_template():
    assert(find_template('tests/fake-repo') == 'tests/fake-repo/{{cookiecutter.repo_name}}')


# Generated at 2022-06-13 18:31:13.701176
# Unit test for function find_template
def test_find_template():
    assert find_template('/Users/audreyr/cookiecutter-pypackage') == '/Users/audreyr/cookiecutter-pypackage/{{cookiecutter.repo_name}}'



# Generated at 2022-06-13 18:31:17.674785
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..', 'fake-repo')
    )
    project_template = find_template(repo_dir)
    assert 'fake-repo' in project_template


# Generated at 2022-06-13 18:31:19.453635
# Unit test for function find_template
def test_find_template():
    find_template('/tmp/cookiecutter-nose/')

# Generated at 2022-06-13 18:31:25.189108
# Unit test for function find_template
def test_find_template():
    import tempfile
    from cookiecutter import utils

    repo_dir = tempfile.mkdtemp()
    utils.make_empty_dir(os.path.join(repo_dir, 'cookiecutter-{{cookiecutter.project_name}}'))
    utils.make_empty_dir(os.path.join(repo_dir, 'hello-world'))

    result = find_template(repo_dir)
    assert result == os.path.join(repo_dir, 'cookiecutter-{{cookiecutter.project_name}}')

# Generated at 2022-06-13 18:31:33.676869
# Unit test for function find_template
def test_find_template():
    """Unit test for function find_template."""
    repo_dir = os.path.join(
        os.path.dirname(__file__),
        'test-data',
        'fake-repo'
    )
    project_template = find_template(repo_dir)
    assert project_template == os.path.join(
        repo_dir,
        '{{cookiecutter.repo_name}}'
    )

# Generated at 2022-06-13 18:31:43.519087
# Unit test for function find_template
def test_find_template():

    def get_mock_template(mock_template_name):
        """Mock Cookiecutter template.
        :param mock_template_name: Template name.
        :return: Template path.
        """
        import tempfile
        tmpdir = tempfile.mkdtemp()
        return os.path.join(tmpdir, mock_template_name)

    get_mock_template('cookiecutter')
    assert find_template(tmpdir) == os.path.join(tmpdir, 'cookiecutter')

    get_mock_template('cookiecutter-foo')
    assert find_template(tmpdir) == os.path.join(tmpdir, 'cookiecutter-foo')

    get_mock_template('cookiecutter-{{cookiecutter.foo}}')

# Generated at 2022-06-13 18:31:53.068106
# Unit test for function find_template
def test_find_template():
    """Test find_template()"""
    FindTemplateTestCase(
        '/Users/audreyr/Documents/projects/cookiecutter-pypackage',
        'cookiecutter-pypackage'
    ).assert_returned_correct_project_template()

    FindTemplateTestCase(
        '/Users/audreyr/Documents/projects/cookiecutter-pypackage/cookiecutter-pypackage',
        'cookiecutter-pypackage/cookiecutter-pypackage'
    ).assert_returned_correct_project_template()


# Generated at 2022-06-13 18:32:05.176231
# Unit test for function find_template
def test_find_template():
    """Test find_template function."""
    # Create a temporary repo_dir for testing purposes.
    import tempfile
    repo_dir = tempfile.mkdtemp()

    # Empty temp directory
    temp_dir_contents = []

    # Expected output
    expected_output = None

    # Test empty directory
    assert find_template(repo_dir) == expected_output

    # Create a temporary file
    temp_file = tempfile.NamedTemporaryFile(dir=repo_dir)
    temp_dir_contents.append(temp_file.name)

    # Test non-empty directory without cookiecutter template
    assert find_template(repo_dir) == expected_output

    # Create a temporary directory that contains a possible template
    template_dir = tempfile.mkdtemp(dir=repo_dir)


# Generated at 2022-06-13 18:32:26.184165
# Unit test for function find_template
def test_find_template():
    """
    Test the find_template function.
    It should return the project_template if it exists.
    It should raise a NonTemplatedInputDirException if
    it doesn't exist.
    """
    repo_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "..", "tests", "fake-repo",
    )
    project_template = os.path.join(repo_dir, "{{cookiecutter.template_name}}")
    assert find_template(repo_dir) == project_template
    assert os.path.isdir(project_template) is True

# Generated at 2022-06-13 18:32:30.929154
# Unit test for function find_template
def test_find_template():
    test_path = os.path.join(
        os.path.dirname(__file__),
        '..',
        '..',
        'tests',
        'test-find-template'
    )
    assert find_template(test_path) == os.path.join(test_path, '{{cookiecutter.repo_name}}')

# Generated at 2022-06-13 18:32:36.253518
# Unit test for function find_template
def test_find_template():
    """Test finding the project template in a fake repo."""
    # TODO: Find a better place for this unittest.
    import tempfile
    import shutil
    fake_repo_dir = tempfile.mkdtemp()

    template_dir = os.path.join(fake_repo_dir, '{{cookiecutter.repo_name}}')
    os.mkdir(template_dir)

    assert find_template(fake_repo_dir) == template_dir

    shutil.rmtree(fake_repo_dir)

# Generated at 2022-06-13 18:32:36.897550
# Unit test for function find_template
def test_find_template():
    pass



# Generated at 2022-06-13 18:32:41.095827
# Unit test for function find_template
def test_find_template():
    assert find_template('~/code/cookiecutter-pypackage') == '~/code/cookiecutter-pypackage/cookiecutter-pypackage'

# Generated at 2022-06-13 18:32:44.002124
# Unit test for function find_template
def test_find_template():
    assert find_template('./tests/fake-repo-template-traditional') == './tests/fake-repo-template-traditional/cookiecutter-pypackage'


# Generated at 2022-06-13 18:32:48.056523
# Unit test for function find_template
def test_find_template():
    project_dir = 'tests/fake-repo-pre/'
    assert 'fake-repo' in  find_template(project_dir)


# Generated at 2022-06-13 18:32:53.531410
# Unit test for function find_template
def test_find_template():
    from cookiecutter import utils

    template_dir = os.path.join(utils.get_project_root(), 'tests', 'test-input')

    result = find_template(template_dir)

    assert '{{' in result
    assert '}}' in result

    expected = os.path.join(template_dir, '{{cookiecutter.repo_name}}')
    assert result == expected

# Generated at 2022-06-13 18:32:56.820814
# Unit test for function find_template
def test_find_template():
    test_repo_dir = os.path.join(
            os.path.dirname(__file__),
            '..',
            'tests',
            'test-repos',
            'cookiecutter-pypackage'
    )

    project_template = find_template(test_repo_dir)

    assert project_template != None
    assert 'cookiecutter-pypackage' in project_template
    assert '{{' not in project_template
    assert '}}' not in project_template

# Generated at 2022-06-13 18:33:02.106343
# Unit test for function find_template
def test_find_template():
    root_dir_contents = os.listdir('.')

    if 'cookiecutter-pypackage' not in root_dir_contents:
        raise NonTemplatedInputDirException

    project_template = find_template('.')
    assert project_template == './cookiecutter-pypackage'

# Generated at 2022-06-13 18:33:20.434012
# Unit test for function find_template
def test_find_template():
    test_repo_dir = os.path.abspath(os.path.join('tests', 'test-data', 'infra'))
    assert 'puppet' in find_template(test_repo_dir)

# Generated at 2022-06-13 18:33:23.663562
# Unit test for function find_template
def test_find_template():
    template = find_template('/Users/audreyr/code/cookiecutter-pypackage')
    assert template == '/Users/audreyr/code/cookiecutter-pypackage/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:33:26.020486
# Unit test for function find_template
def test_find_template():
    """Test that the find_template function works."""

# TODO: test for NonTemplatedInputDirException

# Generated at 2022-06-13 18:33:28.548390
# Unit test for function find_template
def test_find_template():
    assert find_template('tests/fake-repo-tmpl') == 'tests/fake-repo-tmpl/fake-project-{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:33:32.754461
# Unit test for function find_template
def test_find_template():
    """Test function for finding template dir."""
    repo_dir = 'tests/test-data/'
    project_template = 'tests/test-data/{{cookiecutter.project_name}}/'
    assert find_template(repo_dir) == project_template

# Generated at 2022-06-13 18:33:36.050725
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.join(os.path.dirname(__file__), '..', 'tests', 'fake-repo-pre')
    project_template = find_template(repo_dir)

    assert project_template == os.path.join(repo_dir, '{{cookiecutter.repo_name}}')

# Generated at 2022-06-13 18:33:42.683109
# Unit test for function find_template
def test_find_template():
    """
    Verifies the find_template function returns the correct path.
    """

    # Arrange
    repo_dir = "/test/test/test/test"
    repo_dir_contents = [
        "/test/test/test/test/file",
        "/test/test/test/test/cookiecutter_test",
        "/test/test/test/test/Cookiecutter_test",
    ]
    os.listdir = lambda x: repo_dir_contents

    # Act
    project_template = find_template(repo_dir)

    # Assert
    assert project_template == "/test/test/test/test/cookiecutter_test"



# Generated at 2022-06-13 18:33:44.332655
# Unit test for function find_template
def test_find_template():
    find_template('tests/test-repo/fake-repo-tmpl')



# Generated at 2022-06-13 18:33:50.065829
# Unit test for function find_template
def test_find_template():
    """Verify usage of find_template()."""
    from .mock import MockEnvironment
    from .replay import mock_chdir
    from .replay import replay
    from .fixtures import fixture

    with replay():
        env = MockEnvironment()
        repo_dir = fixture('fake-repo-tmpl')
        logger.debug('Searching %s for the project template.', repo_dir)

        with mock_chdir(repo_dir):
            assert find_template(repo_dir) == os.path.join(repo_dir, '{{cookiecutter.directory_name}}')

# Generated at 2022-06-13 18:33:52.248654
# Unit test for function find_template
def test_find_template():
    """Test basic functionality of find_template."""
    # FIXME
    pass

# Generated at 2022-06-13 18:34:28.542866
# Unit test for function find_template
def test_find_template():
    """Verify that find_template returns the correct value."""
    import tempfile
    from cookiecutter import config

    tmp_dir = tempfile.mkdtemp()
    config.repo_dir = tmp_dir

    # Create a couple of directories that mimic a local repository
    # clone, one of which is a template.
    not_a_template = tempfile.mkdtemp(dir=tmp_dir)
    template = tempfile.mkdtemp(dir=tmp_dir)
    os.rename(template, os.path.join(tmp_dir, '{{cookiecutter.template}}'))

    project_template = find_template(config.repo_dir)
    # It should only have one item in its listing
    assert len(os.listdir(project_template)) == 0

# Generated at 2022-06-13 18:34:33.701293
# Unit test for function find_template
def test_find_template():
    """Test the find_template function."""
    template_dir = '/home/audreyr/cookiecutter-pypackage'
    real_template = '/home/audreyr/cookiecutter-pypackage/{{cookiecutter.repo_name}}'

    found_template = find_template(template_dir)
    assert found_template == real_template

# Generated at 2022-06-13 18:34:36.416349
# Unit test for function find_template
def test_find_template():
    repo_dir = 'tests/test-find-template'
    project_template = find_template(repo_dir)
    assert project_template == 'tests/test-find-template/cookiecutter-pypackage'

# Generated at 2022-06-13 18:34:40.068487
# Unit test for function find_template
def test_find_template():
    """Test find_template function, which is used to find template inside a
    repo folder"""
    repo_dir = os.path.join(os.path.dirname(__file__), 'fake-repo')
    project_template = find_template(repo_dir)
    assert 'cookiecutter-pypackage' in project_template

# Generated at 2022-06-13 18:34:46.973902
# Unit test for function find_template
def test_find_template():
    # repo_dir = git clone https://github.com/audreyr/cookiecutter-pypackage.git
    repo_dir = 'tests/test-find-repo/cookiecutter-pypackage-master'
    assert (
        find_template(repo_dir) ==
        'tests/test-find-repo/cookiecutter-pypackage-master/{{cookiecutter.repo_name}}'
    )

# Generated at 2022-06-13 18:34:55.798029
# Unit test for function find_template
def test_find_template():
    """Verify return path of find template."""
    repo_dir = os.path.abspath('tests/test-repo-tmpl')
    repo_dir_contents = os.listdir(repo_dir)
    # project_template is not a real item
    project_template = os.path.join('test-repo-tmpl', '{{project_name}}')
    assert find_template(repo_dir) == project_template

    # verify searching non-template directory
    repo_dir = os.path.abspath('tests')
    assert find_template(repo_dir) == os.path.join('tests', 'test-repo')

# Generated at 2022-06-13 18:34:56.754108
# Unit test for function find_template
def test_find_template():
    pass

# Generated at 2022-06-13 18:35:04.207929
# Unit test for function find_template
def test_find_template():
    input_dir = os.path.join(
        os.path.dirname(__file__),
        '..', '..', 'tests', 'test-find-template-input', 'repo_dir'
    )
    assert find_template(input_dir) == os.path.join(
        input_dir, '{{cookiecutter.repo_name}}'
    )

# Generated at 2022-06-13 18:35:10.629350
# Unit test for function find_template
def test_find_template():
    """Verify the find_template function works as expected."""
    import pytest
    from .utils import make_repo

    repo_dir = make_repo(template=False)

    err_msg = 'Repo without a template should throw NonTemplatedInputDirException.'
    with pytest.raises(NonTemplatedInputDirException):
        find_template(repo_dir)

    find_template(make_repo(no_input=True, extra_context={'hello': 'world'}))

# Generated at 2022-06-13 18:35:11.739347
# Unit test for function find_template
def test_find_template():
    pass

# Generated at 2022-06-13 18:36:17.997658
# Unit test for function find_template
def test_find_template():
    from Cookiecutter import repo
    from Cookiecutter.config import DEFAULT_CONFIG

    # Test for find_template
    input_dir = repo.clone(DEFAULT_CONFIG['default_repo'])
    project_template = find_template(input_dir)
    assert os.path.basename(project_template) == '{{cookiecutter.repo_name}}'

    # Test for find_template using the default repo
    input_dir = repo.clone(DEFAULT_CONFIG['default_repo'])
    project_template = find_template(input_dir)
    assert os.path.basename(project_template) == '{{cookiecutter.repo_name}}'

    # Test for find_template using an empty repo

# Generated at 2022-06-13 18:36:20.258384
# Unit test for function find_template
def test_find_template():
    find_template('pytest-cookiecutter/tests/test-input/fake-repo-pre/')


# Generated at 2022-06-13 18:36:29.211746
# Unit test for function find_template
def test_find_template():
    '''
    Tests find_template with a directory containing a template
    '''
    from nose.tools import assert_equals
    from cookiecutter.utils import rmtree

    project_template = "cookiecutter-foobar{{cookiecutter.project_name}}"
    repo_dir = "tests/fake-repo-pre/{{cookiecutter.github_repo}}"
    expected_template = "tests/fake-repo-pre/cookiecutter-foobar{{cookiecutter.project_name}}"
    found_template = find_template(repo_dir)

    assert_equals(expected_template, found_template)

    rmtree(repo_dir)



# Generated at 2022-06-13 18:36:30.173037
# Unit test for function find_template
def test_find_template():
    pass

# Generated at 2022-06-13 18:36:31.645803
# Unit test for function find_template
def test_find_template():
    find_template('cookiecutter-django')



# Generated at 2022-06-13 18:36:32.410319
# Unit test for function find_template
def test_find_template():
    pass

# Generated at 2022-06-13 18:36:38.490567
# Unit test for function find_template
def test_find_template():
    # testing for correct path
    assert find_template(
        os.path.join(os.path.dirname(__file__), 'data/fake-repo/')
    ) == os.path.join(os.path.dirname(__file__), 'data/fake-repo/{{cookiecutter.repo_name}}')
    # testing for when no template found
    try:
        find_template(".")
        assert False
    except NonTemplatedInputDirException:
        pass

# Generated at 2022-06-13 18:36:42.907204
# Unit test for function find_template
def test_find_template():
    repo_dir_contents = ['cookiecutter-pypackage']
    test_repo_dir = 'path/to/test/package'
    test_project_template_path = 'path/to/test/package/cookiecutter-pypackage'

    repo_dir_contents = ['pytest']
    assert find_template(test_repo_dir_contents) == find_template(test_repo_dir)
    assert find_template(test_repo_dir) is None
    assert find_template(test_repo_dir_contents) is None

# Generated at 2022-06-13 18:36:46.780847
# Unit test for function find_template
def test_find_template():
    repo_dir_contents = os.listdir('~/github/pycon-zambia-2016-cookiecutter/')
    project_template = None
    for item in repo_dir_contents:
        if 'cookiecutter' in item and '{{' in item and '}}' in item:
            project_template = item
            break
    # Expected result is true i.e project_template is not None
    assert project_template

# Generated at 2022-06-13 18:36:49.693225
# Unit test for function find_template
def test_find_template():
    assert find_template('../tests/fake-repo-templated/') == '../tests/fake-repo-templated/{{cookiecutter.repo_name}}'
    assert find_template('../tests/fake-repo-pre/') == '../tests/fake-repo-pre/pre'