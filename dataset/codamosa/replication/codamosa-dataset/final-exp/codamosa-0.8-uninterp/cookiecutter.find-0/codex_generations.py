

# Generated at 2022-06-13 18:27:45.297056
# Unit test for function find_template
def test_find_template():
    """
    Given a directory that contains a subdirectory that is the project template,
    this function should find it.
    """
    repo_dir = 'tests/fake-repo/'
    project_template = find_template(repo_dir)
    expected = 'tests/fake-repo/{{cookiecutter.repo_name}}'
    assert project_template == expected

# Generated at 2022-06-13 18:27:48.278725
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.realpath('tests/fake-repo-tmpl')
    project_template = find_template(repo_dir)
    print(project_template)
    assert os.path.isfile(os.path.join(project_template, 'cookiecutter.json'))

# Generated at 2022-06-13 18:27:58.079856
# Unit test for function find_template
def test_find_template():
    """Verify that find_template() returns the correct directory."""
    import pytest
    import shutil
    import tempfile

    repo_dir = tempfile.mkdtemp()

    # Create two directories, with one being the project template.
    os.mkdir(os.path.join(repo_dir, 'foobar'))
    os.mkdir(os.path.join(repo_dir, '{{cookiecutter.repo_name}}'))

    try:
        assert '{{cookiecutter.repo_name}}' == \
            os.path.basename(find_template(repo_dir))
    finally:
        shutil.rmtree(repo_dir)



# Generated at 2022-06-13 18:28:11.184355
# Unit test for function find_template
def test_find_template():
    from cookiecutter.main import cookiecutter
    from cookiecutter import utils
    from cookiecutter.exceptions import (
        RepositoryNotFound,
        OutputDirExistsException
    )

    try:
        cookiecutter('tests/fake-repo-pre/', no_input=True)
    except (RepositoryNotFound, OutputDirExistsException) as e:
        utils.rmtree('fake-repo-pre')
        raise e

    try:
        cookiecutter('tests/fake-repo-post/', no_input=True)
    except (RepositoryNotFound, OutputDirExistsException) as e:
        utils.rmtree('fake-repo-post')
        raise e


# Generated at 2022-06-13 18:28:13.654673
# Unit test for function find_template
def test_find_template():
    input_path = 'tests/fake-repo-pre/'
    output_path = 'tests/fake-repo-pre/fake-project'

    assert find_template(input_path) == output_path

# Generated at 2022-06-13 18:28:26.575661
# Unit test for function find_template
def test_find_template():
    """Load a call to find_template with a pre-constructed directory."""
    import tempfile
    import shutil
    import os

    temp_repo_dir = tempfile.mkdtemp()
    os.mkdir(os.path.join(temp_repo_dir, 'cookiecutter-project-name'))
    os.mkdir(os.path.join(temp_repo_dir, 'cookiecutter-project-name-{{cookiecutter.repo_name}}'))
    os.mkdir(os.path.join(temp_repo_dir, 'cookiecutter-{{cookiecutter.repo_name}}'))

    find_template(temp_repo_dir)
    shutil.rmtree(temp_repo_dir)

# Generated at 2022-06-13 18:28:33.996418
# Unit test for function find_template
def test_find_template():
    import tempfile
    import shutil

    repo_dir = tempfile.mkdtemp()

    # Create a fake project template dir
    fake_project_template_dir = os.path.join(repo_dir, 'fake_project_template')
    os.makedirs(fake_project_template_dir)

    assert find_template(repo_dir) == fake_project_template_dir

    shutil.rmtree(repo_dir)

# Generated at 2022-06-13 18:28:36.002431
# Unit test for function find_template
def test_find_template():
    pass

# Generated at 2022-06-13 18:28:40.657562
# Unit test for function find_template
def test_find_template():
    """
    Test that the right project template is found
    """

# Generated at 2022-06-13 18:28:45.109290
# Unit test for function find_template
def test_find_template():
    from cookiecutter.config import USE_DOT_AS_SEPARATOR
    from cookiecutter.generate import DEFAULT_CONFIG
    from tests.test_find_template_basic import expected_find_template_result, repo_dir

    DEFAULT_CONFIG['use_dot_as_separator'] = USE_DOT_AS_SEPARATOR
    template = find_template(repo_dir)
    assert expected_find_template_result == template

# Generated at 2022-06-13 18:28:48.476723
# Unit test for function find_template
def test_find_template():
    """Test for function find_template."""
    pass

# Generated at 2022-06-13 18:28:55.832584
# Unit test for function find_template
def test_find_template():
    """Test whether finding a template works."""

    repo_dir = 'tests/test-find-template/fake-repo'
    project_template = find_template(repo_dir)
    assert 'tests/test-find-template/fake-repo/{{cookiecutter.repo_name}}' == project_template

    repo_dir2 = 'tests/fake-repo-pre/'
    project_template2 = find_template(repo_dir2)
    assert 'tests/fake-repo-pre/' == project_template2

# Generated at 2022-06-13 18:29:04.162366
# Unit test for function find_template
def test_find_template():
    """Verify that find_template() works as expected."""
    import shutil
    import tempfile

    tmpdir = tempfile.mkdtemp()

    # Create repo_dir
    repo_dir_path = os.path.join(tmpdir, 'fake-repo')
    os.makedirs(repo_dir_path)

    # Create cookiecutter.json
    cookiecutter_json_path = os.path.join(repo_dir_path, 'cookiecutter.json')
    with open(cookiecutter_json_path, 'w') as fh:
        fh.write('{"foo": "bar"}')

    # Create fake project template
    project_template_path = os.path.join(repo_dir_path, 'fake-project-template')

# Generated at 2022-06-13 18:29:09.602278
# Unit test for function find_template
def test_find_template():
    repo_dir = '/home/user/TestRepo'
    os.listdir = lambda path: ['cookiecutter-test']
    project_template = find_template(repo_dir)
    assert project_template == os.path.join(repo_dir, 'cookiecutter-test')

# Generated at 2022-06-13 18:29:10.538221
# Unit test for function find_template
def test_find_template():
    pass

# Generated at 2022-06-13 18:29:16.920912
# Unit test for function find_template
def test_find_template():
    from cookiecutter import utils

    repo_dir = '/Users/hackebrot/Dropbox/personal/git/cookiecutter-find-test'

    expected = '/Users/hackebrot/Dropbox/personal/git/cookiecutter-find-test/{{cookiecutter.project_name}}'
    result = utils.find_template(repo_dir)

    assert (result == expected)

# Generated at 2022-06-13 18:29:23.259592
# Unit test for function find_template
def test_find_template():
    """
    Unit test for function find_template
    """
    repo_dir = 'cookiecutter_test/tests/test-input/hook-project-name'
    project_template = find_template(repo_dir)

    assert project_template == 'cookiecutter_test/tests/test-input/hook-project-name/{{cookiecutter.repo_name}}', \
        'The project template is not what it should be!'

# Generated at 2022-06-13 18:29:25.464544
# Unit test for function find_template
def test_find_template():
    find_template('test_dir_contents', 'test_dir')

# Generated at 2022-06-13 18:29:32.571533
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.join(os.getcwd(), 'tests-no-output', 'fake-repo')
    template = 'fake-repo-{{cookiecutter.repo_name}}'
    assert find_template(repo_dir) == os.path.join(repo_dir, template)

# Generated at 2022-06-13 18:29:34.126784
# Unit test for function find_template
def test_find_template():
    find_template("./")


# Generated at 2022-06-13 18:29:46.069399
# Unit test for function find_template
def test_find_template():
    """Unit test for function find_template."""
    import os
    import sys

    print(__file__)
    print(os.path.dirname(__file__))
    print(os.path.dirname(os.path.dirname(__file__)))
    print(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    sys.path.append(os.getcwd())
    import cookiecutter

    template_dir = cookiecutter.find_template('tests/test-repo-pre')
    assert template_dir == 'tests/test-repo-pre/{{cookiecutter.repo_name}}'



# Generated at 2022-06-13 18:29:46.904499
# Unit test for function find_template
def test_find_template():
    pass

# Generated at 2022-06-13 18:29:49.245073
# Unit test for function find_template

# Generated at 2022-06-13 18:30:00.418898
# Unit test for function find_template
def test_find_template():
    assert find_template('/home/audreyr/cookiecutter-pypackage') is None
    assert find_template('tests/fake-repo-pre') is None
    assert find_template('tests/fake-repo-pre/{{cookiecutter.repo_name}}') is None
    assert find_template('tests/fake-repo-pre/fake-repo-post') == 'tests/fake-repo-pre/fake-repo-post'
    assert find_template('tests/fake-repo-pre/fake-repo-post/') == 'tests/fake-repo-pre/fake-repo-post'
    assert find_template('tests/fake-repo-pre/fake-repo-post/should-be-ignored') is None

# Generated at 2022-06-13 18:30:02.772433
# Unit test for function find_template
def test_find_template():
    # If there was no Cookiecutter config file found...
    # Cookiecutter(repo_dir=self.current_repo_dir)
    pass

# Generated at 2022-06-13 18:30:06.835824
# Unit test for function find_template
def test_find_template():
    assert find_template('../' + '../' + '../') == '../' + '../' + '../' + 'cookiecutter-pypackage-minimal'
    assert find_template('../') == '../' + 'cookiecutter-pypackage'

# Generated at 2022-06-13 18:30:15.877052
# Unit test for function find_template
def test_find_template():
    """
    Test find_template function
    """
    # check if returns the right path
    repo_dir = 'tests/test-repo/'
    actual_return = find_template(repo_dir)
    expected_return = os.path.join('tests/test-repo', '{{ cookiecutter.repo_name }}')
    assert actual_return == expected_return

    # check if it raises NonTemplatedInputDirException
    repo_dir = 'tests/fake-repo/'
    try:
        find_template(repo_dir)
        assert False
    except NonTemplatedInputDirException:
        assert True

# Generated at 2022-06-13 18:30:18.749054
# Unit test for function find_template
def test_find_template():
    find_template('/home/vagrant')
    find_template('')



# Generated at 2022-06-13 18:30:21.831982
# Unit test for function find_template
def test_find_template():
    test_dir = os.path.join(
        os.path.dirname(__file__), '..', 'tests', 'fake-repo', '{{cookiecutter.repo_name}}'
    )
    assert find_template(test_dir) == test_dir

# Generated at 2022-06-13 18:30:24.344313
# Unit test for function find_template
def test_find_template():
    """ Sanity check for repo_dir"""
    repo_dir = 'tests/fake-repo-pre/'
    assert find_template(repo_dir) == 'tests/fake-repo-pre/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:30:28.350202
# Unit test for function find_template
def test_find_template():
    find_template('/Users/carolinebenn/cookiecutter')



# Generated at 2022-06-13 18:30:35.457892
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..', 'tests', 'fake-repo-tmpl')
    )
    try:
        find_template(repo_dir)
    except NonTemplatedInputDirException:
        raise AssertionError('Failed to find a tempated directory')


# Generated at 2022-06-13 18:30:37.313802
# Unit test for function find_template
def test_find_template():
    repo_dir = '/Users/hackebrot/code/cookiecutter-demo'
    find_template(repo_dir)

# Generated at 2022-06-13 18:30:42.212226
# Unit test for function find_template
def test_find_template():
    repo_dir_contents = {
       '__init__.py': None,
       'README.md': None,
       'cookiecutter-pypackage': None,
       'hooks': None,
       'tests': None,
       '{{cookiecutter.project_name}}': None,
       'pyproject.toml': None,
    }
    assert find_template(repo_dir_contents) == '{{cookiecutter.project_name}}'

# Generated at 2022-06-13 18:30:49.160587
# Unit test for function find_template
def test_find_template():
    import tempfile
    import shutil

    repo = tempfile.mkdtemp()

    template_dir = os.path.join(repo, '{{cookiecutter.repo_name}}')
    os.makedirs(template_dir)

    try:
        repo_dir = os.path.dirname(template_dir)
        result = find_template(repo_dir)
        assert result == template_dir
    finally:
        shutil.rmtree(repo)


# Generated at 2022-06-13 18:30:59.386899
# Unit test for function find_template
def test_find_template():
    """Test the find_template function."""
    import os
    import tempfile
    from cookiecutter.utils import rmtree

    # Create the template
    template = tempfile.mkdtemp()

    # Write out a simple 'cookiecutter.json' file
    f = open('cookiecutter.json', 'w')
    f.write('{"foo": "bar"}')
    f.close()

    # Find the template
    repo_dir = find_template(template)

    # It should be the same as what we created
    assert template == repo_dir

    rmtree(template)

# Generated at 2022-06-13 18:31:03.613443
# Unit test for function find_template
def test_find_template():
    repo_dir = '~/code/cookiecutter-pypackage'
    project_template = find_template(repo_dir)
    assert project_template
    assert project_template == '~/code/cookiecutter-pypackage/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:31:17.880999
# Unit test for function find_template
def test_find_template():
    """Test the find_template() function."""
    from cookiecutter import utils
    from tempfile import mkdtemp
    from shutil import rmtree

    repo_dir = mkdtemp()

    try:
        os.mkdir(os.path.join(repo_dir, 'does_not_fit_any_criteria'))
        os.mkdir(os.path.join(repo_dir, '{{cookiecutter.repo_name}}'))
        project_template = utils.find_template(repo_dir)
        assert project_template == os.path.join(
            repo_dir,
            '{{cookiecutter.repo_name}}'
        )
    finally:
        rmtree(repo_dir)

# Generated at 2022-06-13 18:31:23.798750
# Unit test for function find_template
def test_find_template():
    repo_dir_contents = [
        '.git',
        '.cookiecutter.yaml',
        'CHANGELOG.rst',
        'LICENSE',
        'README.md',
        'cookiecutter-pypackage'
    ]

    # Mock os.listdir
    os.listdir = lambda x: repo_dir_contents

    project_template = find_template('fakedir')
    assert project_template == 'fakedir/cookiecutter-pypackage'

# Generated at 2022-06-13 18:31:37.249106
# Unit test for function find_template
def test_find_template():
    """
    Test to ensure that the find_template function works as anticipated
    """

    import shutil
    import tempfile

    absolute_path = os.path.dirname(os.path.abspath(__file__))
    temporary_directory = tempfile.mkdtemp()
    template_directory = os.path.join(absolute_path, 'templates', 'cookiecutter-pypackage')

    shutil.copytree(template_directory, temporary_directory)

    test_directory = find_template(temporary_directory)

    assert test_directory == os.path.join(temporary_directory, '{{cookiecutter.repo_name}}')

    shutil.rmtree(temporary_directory)



# Generated at 2022-06-13 18:31:52.241725
# Unit test for function find_template
def test_find_template():
    """
    Test to find template in the cookiecutter-pypackage repository:
    https://github.com/audreyr/cookiecutter-pypackage
    """
    repo_dir = os.path.join(
        os.path.abspath(
            os.path.dirname(__file__)
        ),
        '..',
        'tests',
        'fake-repo',
        'cookiecutter-pypackage'
    )
    project_template = find_template(repo_dir)
    expected = os.path.join(repo_dir, '{{cookiecutter.repo_name}}')
    assert expected == project_template

# Generated at 2022-06-13 18:31:56.668443
# Unit test for function find_template

# Generated at 2022-06-13 18:32:02.929591
# Unit test for function find_template
def test_find_template():
    repo_dir = 'tests/test-find-dir/cookiecutter-pypackage'
    project_template = find_template(repo_dir)
    assert project_template == os.path.join(
        repo_dir,
        'cookiecutter-pypackage'
    ), ("find_template should return the full path to the project template "
        "directory")

# Generated at 2022-06-13 18:32:14.146354
# Unit test for function find_template
def test_find_template():
    """Verify that find_template returns the correct project_template."""

    # Create a temporary directory
    from tempfile import mkdtemp
    from shutil import rmtree
    temp_dir = mkdtemp()

    # Create a fake project template with fake content
    project_template = '{{cookiecutter.project_name}}'
    os.mkdir(os.path.join(temp_dir, project_template))
    test_file = os.path.join(temp_dir, project_template, 'test.txt')
    with open(test_file, 'w') as file:
        file.write('Test file')

    # Now create a fake directory containing the project_template
    fake_repo_dir = os.path.join(temp_dir, 'fake_repo')

# Generated at 2022-06-13 18:32:15.867264
# Unit test for function find_template
def test_find_template():
    repo_dir = '/Users/audreyr/Documents/GitHub/cookiecutter-pypackage'
    find_template(repo_dir)

# Generated at 2022-06-13 18:32:19.467307
# Unit test for function find_template

# Generated at 2022-06-13 18:32:24.726074
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.join('tests', 'fake-repo-tmpl')
    project_dir = os.path.join(repo_dir, '{{cookiecutter.repo_name}}')
    template_dir = os.path.join(project_dir, 'content', '{{cookiecutter.project_name}}')
    assert os.path.normcase(find_template(repo_dir)) == os.path.normcase(template_dir)

# Generated at 2022-06-13 18:32:30.356514
# Unit test for function find_template
def test_find_template():
    """
    """
    print('Testing find_template()')
    directory = os.path.join(os.getcwd(), 'tests', 'test-find-template')
    template = find_template(directory)
    print('\t', template)
    assert template == os.path.join(directory, 'cookiecutter-project')
    print('\tPASSED')



# Generated at 2022-06-13 18:32:32.027003
# Unit test for function find_template
def test_find_template():
    """Test the case of a clean repo that contains a templated project."""
    find_template('test_repo')

# Generated at 2022-06-13 18:32:35.893900
# Unit test for function find_template
def test_find_template():
    """Verify that find_template finds the expected template"""

    assert(find_template('/home/user/projects/sample') == '/home/user/projects/sample/{{ cookiecutter.repo_name }}')
    assert(find_template('/mnt/c/my/projects/sample') == '/mnt/c/my/projects/sample/{{ cookiecutter.repo_name }}')

# Generated at 2022-06-13 18:32:52.598785
# Unit test for function find_template
def test_find_template():
    class MockThing(object):
        def __init__(self):
            self.debug = list()

        def debug(self, message):
            self.debug.append(str(message))

    logger = MockThing()
    logger = logging.getLogger(__name__)
    logger.debug = logger.debug
    repo_dir = 'tests/fake-repo-tmpl/'
    project_template = find_template(repo_dir)
    assert project_template == 'tests/fake-repo-tmpl/{{cookiecutter.repo_name}}/'

# Generated at 2022-06-13 18:32:58.798688
# Unit test for function find_template
def test_find_template():
    from cookiecutter.utils.paths import fixture
    repo_dir = fixture('non-templated-repo')
    project_template = find_template(repo_dir)
    assert project_template == repo_dir + '/{{cookiecutter.repo_name}}/'

# Generated at 2022-06-13 18:33:06.370729
# Unit test for function find_template
def test_find_template():
    """Ensure that input directory is detected if it contains 'cookiecutter'."""
    logger.debug('Testing that an input dir containing "cookiecutter" is the '
                 'template dir.')
    repo_dir = 'tests/test-repo-tmpl/{{cookiecutter.repo_name}}'
    project_template = find_template(repo_dir)
    expected_project_template = 'tests/test-repo-tmpl/{{cookiecutter.repo_name}}'

    assert project_template == expected_project_template

# Generated at 2022-06-13 18:33:08.916493
# Unit test for function find_template
def test_find_template():
    assert find_template('/home') == '/home/cookiecutter-{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:33:17.716728
# Unit test for function find_template
def test_find_template():
    """Determine if find_template is working."""

    from .tests import root_dir, assert_paths_exist

    # Get the real repo dir for cookiecutter-pypackage
    real_repo_dir = str(root_dir.join('cookiecutter-pypackage'))

    # Run find_template
    find_template(real_repo_dir)

    # Make sure that a file called 'cookiecutter-pypackage' exists
    assert_paths_exist(
        [real_repo_dir + '/cookiecutter-pypackage']
    )

    # It's a directory
    assert os.path.isdir(real_repo_dir + '/cookiecutter-pypackage')

    # It contains a file called 'setup.py'
    assert_paths_

# Generated at 2022-06-13 18:33:24.107185
# Unit test for function find_template
def test_find_template():
    """Test the find_template function"""
    dir_name = os.path.dirname(os.path.realpath(__file__))
    repo_dir = os.path.join(dir_name, '..', 'tests', 'fake-repo-tmpl')
    project_template = find_template(repo_dir)
    assert project_template == os.path.join(repo_dir, '{{cookiecutter.repo_name}}')

# Generated at 2022-06-13 18:33:35.667617
# Unit test for function find_template
def test_find_template():
    """
    Determine which child directory of `repo_dir` is the project template.

    :param repo_dir: Local directory of newly cloned repo.
    :returns project_template: Relative path to project template.
    """
    repo_dir = "/home/cookiecutter/repos"
    repo_dir_contents = os.listdir(repo_dir)

    project_template = None
    for item in repo_dir_contents:
        if 'cookiecutter' in item and '{{' in item and '}}' in item:
            project_template = item
            break

    if project_template:
        project_template = os.path.join(repo_dir, project_template)
        return project_template
    else:
        raise NonTemplatedInputDirException


# Generated at 2022-06-13 18:33:41.997838
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.join(
        os.path.dirname(__file__),
        '..',
        'tests',
        'test-data',
        'hello-world-jinja2'
    )
    project_template = find_template(repo_dir)
    assert project_template == os.path.join(
        repo_dir,
        '{{cookiecutter.repo_name}}'
    )

# Generated at 2022-06-13 18:33:44.716537
# Unit test for function find_template
def test_find_template():
    """Test that find_template is finding the correct template."""
    assert find_template('tests/fake-repo-tmpl') == 'tests/fake-repo-tmpl/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:33:50.256348
# Unit test for function find_template
def test_find_template():
    repo_dir = 'tests/fake-repo-tmpl/{{cookiecutter.repo_name}}'
    expected = 'tests/fake-repo-tmpl/{{cookiecutter.repo_name}}/{{cookiecutter.repo_name}}'
    result = find_template(repo_dir)
    assert expected == result


# Generated at 2022-06-13 18:34:06.157908
# Unit test for function find_template
def test_find_template():
    """Test for function find_template"""
    import logging

    logger = logging.getLogger(__name__)

    try:
        find_template('/Users/msidd/MyWorkspace/Python/cookiecutter/tests/fake-repo-pre/')
    except NonTemplatedInputDirException:
        logger.info('Function find_template returns the correct value')


# Generated at 2022-06-13 18:34:11.655945
# Unit test for function find_template
def test_find_template():
    """Unit test for function `find_template`."""
    repo_dir = os.path.abspath(os.path.dirname(__file__))
    project_template = find_template(repo_dir)
    assert 'tests' in project_template
    assert '.{{' in project_template
    assert '}}' in project_template

# Generated at 2022-06-13 18:34:12.888953
# Unit test for function find_template
def test_find_template():
    pass

# Generated at 2022-06-13 18:34:13.693985
# Unit test for function find_template
def test_find_template():
    pass

# Generated at 2022-06-13 18:34:25.098791
# Unit test for function find_template
def test_find_template():
    import os
    import shutil
    import tempfile

    from cookiecutter.utils import rmtree


# Generated at 2022-06-13 18:34:36.182951
# Unit test for function find_template
def test_find_template():
    """Verify the correct project template is identified."""
    import tempfile

    def make_temp_repo_dir(name, rel_template_path_list):
        """Create a temporary repo directory with specified path(s) to project template."""
        temp_repo_dir = tempfile.mkdtemp()

        for rel_template_path in rel_template_path_list:
            template_dir = os.path.join(temp_repo_dir, rel_template_path)
            os.makedirs(template_dir)
            with open(os.path.join(template_dir, 'somefile.txt'), 'w') as f:
                f.write('Hello World!')

            if name != rel_template_path:
                os.makedirs(os.path.join(template_dir, name))

        return

# Generated at 2022-06-13 18:34:36.668213
# Unit test for function find_template
def test_find_template():
    pass

# Generated at 2022-06-13 18:34:37.671918
# Unit test for function find_template
def test_find_template():
    find_template(repo_dir)

# Generic cookiecutter render function

# Generated at 2022-06-13 18:34:39.240049
# Unit test for function find_template
def test_find_template():
    """Unit test for function find_template"""
    # TODO: Add unit test for function find_template
    pass

# Generated at 2022-06-13 18:34:40.246139
# Unit test for function find_template
def test_find_template():
    pass

# Generated at 2022-06-13 18:34:51.738299
# Unit test for function find_template
def test_find_template():
    repo_dir = "cookiecutter-pypackage/"
    repo_dir_contents = os.listdir(repo_dir)
    print(find_template(repo_dir))

test_find_template()

# Generated at 2022-06-13 18:34:54.346395
# Unit test for function find_template
def test_find_template():
    assert find_template('./tests/fake-repo/') == './tests/fake-repo/{{cookiecutter.repo_name}}'



# Generated at 2022-06-13 18:35:07.219726
# Unit test for function find_template
def test_find_template():
    """Verify find_template returns a template directory"""
    import mock
    import shutil
    import tempfile

    cookiecutter_json = '{"repo_dir": ".", "cookiecutter": {}, "extra_context": {}, "output_dir": ".", "overwrite_if_exists": false, "abort_if_exists": false}'
    # Create a temporary directory inside the system temporary directory
    tmp_dir = tempfile.mkdtemp()
    tmpl_dir = os.path.join(tmp_dir, '{{cookiecutter.project_name}}')
    os.mkdir(tmpl_dir)

    with mock.patch('__builtin__.open', mock.mock_open(read_data=cookiecutter_json)):
        template = find_template(tmp_dir)
       

# Generated at 2022-06-13 18:35:10.718124
# Unit test for function find_template
def test_find_template():
    repo_dir = 'FAKE_DIR'
    os.listdir = lambda x: ['cookiecutter', '{{cookiecutter.foo}}']
    with mock.patch('cookiecutter.find.os.path.join') as mock_join:
        find_template(repo_dir)
        mock_join.assert_called_once_with(repo_dir, '{{cookiecutter.foo}}')

# Generated at 2022-06-13 18:35:24.292555
# Unit test for function find_template
def test_find_template():
    """
    Unit test for function find_template
    """
    os.system("rm -rf /home/simon/cookiecutter-test")
    os.system("cp -r /home/simon/cookiecutter-personal/ /home/simon/cookiecutter-test")
    repo_dir = "/home/simon/cookiecutter-test"
    expected_output = "/home/simon/cookiecutter-test/{{cookiecutter.repo_name}}"
    output = find_template(repo_dir)
    os.system("rm -rf /home/simon/cookiecutter-test")
    assert output == expected_output

if __name__ == "__main__":
    test_find_template()

# Generated at 2022-06-13 18:35:27.781936
# Unit test for function find_template
def test_find_template():
    """Verify ``find_template`` can detect the project template."""
    find_template('tests/test-repo-tmpl')

# Generated at 2022-06-13 18:35:33.476688
# Unit test for function find_template
def test_find_template():
    from cookiecutter import cli
    from .utils import workdir
    from .utils import rmdir

    cli.main(extra_context={'foo': 'Foo'})
    assert os.path.isdir('Foo')

    try:
        with workdir('tests/input'):
            with workdir('cookiecutter-pypackage-tests'):
                project_template = find_template('.')
                assert os.path.isdir(project_template)
    finally:
        rmdir('Foo')

# Generated at 2022-06-13 18:35:37.459290
# Unit test for function find_template
def test_find_template():
    """Tests for function find_template."""

    # FIXME: use tempdirs
    # create some directories in a temporary dir structure
    # test that expected one is found
    # test that exception is raised if there are no directories

    assert 1 == 1

# Generated at 2022-06-13 18:35:40.193524
# Unit test for function find_template
def test_find_template():
    """
    Check that the find_template function
    works as intended
    """
    assert find_template('/home/foo') == '/home/foo/cookiecutter-pypackage'

# Generated at 2022-06-13 18:35:43.952356
# Unit test for function find_template
def test_find_template():
    assert find_template('/home/audreyr/cookiecutter-pypackage') == '/home/audreyr/cookiecutter-pypackage/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:36:14.790681
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
        'tests',
        'test-repo-tmpl'
    )

    expected_template = os.path.abspath(os.path.join(
        repo_dir,
        '{{cookiecutter.repo_name}}'
    ))

    template = find_template(repo_dir)
    assert expected_template == template

# Generated at 2022-06-13 18:36:23.176844
# Unit test for function find_template
def test_find_template():
    from cookiecutter.tests.test_repo_dirs import clone_test_repo
    from cookiecutter.tests.fake_repo import fake_repo

    fake_repo('cookiecutter-pypackage')
    test_repo_dir = clone_test_repo('cookiecutter-pypackage')
    expected_project_template = os.path.join(
        test_repo_dir,
        u'{{cookiecutter.repo_name}}',
    )
    assert find_template(test_repo_dir) == expected_project_template

# Generated at 2022-06-13 18:36:26.112979
# Unit test for function find_template
def test_find_template():
    """Unit test for function find_template."""
    assert find_template('tests/fake-repo-pre/') == \
        'tests/fake-repo-pre/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:36:36.973482
# Unit test for function find_template
def test_find_template():
    """Verify that the find_template function works correctly."""

    from .compat import patch

    repo_dir = os.path.abspath('fixtures/fake-repo-tmpl')

    # When a valid project template can be found
    # Then project_template is the expected path to the template
    expected_result = os.path.join(repo_dir, '{{cookiecutter.repo_name}}')
    with patch('cookiecutter.find.os.path.abspath') as mock_abspath:
        mock_abspath.return_value = repo_dir
        with patch('cookiecutter.find.os.listdir') as mock_listdir:
            mock_listdir.return_value = ['{{cookiecutter.repo_name}}', 'other_file']
            result = find_template

# Generated at 2022-06-13 18:36:46.021480
# Unit test for function find_template
def test_find_template():
    """Make sure we can find the `cookiecutter-pypackage` template."""
    repo_dir = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__), '..', '..', 'tests', 'fake-repo-pre'))
    project_template = find_template(repo_dir)

    assert project_template == os.path.join(repo_dir, '{{cookiecutter.repo_name}}')

# Generated at 2022-06-13 18:36:50.137158
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..', 'tests', 'fake-repo-tmpl'))
    project_template = find_template(repo_dir)
    assert project_template == os.path.join(repo_dir, '{{cookiecutter.repo_name}}')

# Generated at 2022-06-13 18:36:53.370515
# Unit test for function find_template
def test_find_template():
    repo_dir = 'test/test'
    project_template = find_template(repo_dir)

    assert project_template == 'test/test/{{cookiecutter.repo_name}}'



# Generated at 2022-06-13 18:36:56.492852
# Unit test for function find_template
def test_find_template():
    # fake_repo_dir = os.path.abspath(os.path.join(
    #     os.path.dirname(__file__), '..', '..', 'tests', 'fake-repo-pre'
    # ))

    # project_template = find_template(fake_repo_dir)

    # assert 'fake-repo-pre' in project_template
    # assert 'cookiecutter-pypackage' not in project_template

    pass

# Generated at 2022-06-13 18:37:07.262027
# Unit test for function find_template
def test_find_template():

    # TODO: create a template that uses a simple 'cookiecutter'
    # folder name, rather than a templated 'cookiecutter-{{ cookiecutter.repo_name }}'
    # to avoid forcing this test to fail if the master branch changes.

    # Mock the json which should be returned by the API
    repo_dir = '/home/audreyr/cookiecutters/cookiecutter-pypackage'
    repo_dir_contents = [
        'README.md',
        'cookiecutter.json',
        'documentation_builder',
        'hooks',
        'tests',
        'travis_pypi_setup.py'
    ]

    for item in repo_dir_contents:
        os.mkdir(os.path.join(repo_dir, item))

    project_

# Generated at 2022-06-13 18:37:16.704963
# Unit test for function find_template
def test_find_template():
    from unittest import mock
    import os
    from cookiecutter.utils import find_template

    template_dir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..', 'tests', 'fake-repo-tmpl')
    )
    expected_project_template = os.path.join(template_dir, 'foobar{{cookiecutter.repo_name}}')

    with mock.patch('cookiecutter.utils.os.listdir') as listdir_mock:
        listdir_mock.return_value = ['foobar', 'barfoo']
        with mock.patch('cookiecutter.utils.os.path.abspath') as abspath_mock:
            abspath_mock.return_value = expected_project_template
            actual