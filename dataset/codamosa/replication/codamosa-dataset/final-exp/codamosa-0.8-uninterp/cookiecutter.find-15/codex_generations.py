

# Generated at 2022-06-13 18:27:50.649316
# Unit test for function find_template
def test_find_template():
    """Verify find_template function works correctly."""
    repo_dir = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__), '..', '..', 'tests', 'fake-repo',
        )
    )
    project_template = find_template(repo_dir)
    expected_project_template = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__), '..', '..', 'tests', 'fake-repo',
            'fake-project',
        )
    )

    assert project_template == expected_project_template

# Generated at 2022-06-13 18:27:59.873508
# Unit test for function find_template
def test_find_template():

    # Test for single directory within repo_dir
    test_dir = os.path.abspath(os.path.dirname(__file__))
    input_dir = os.path.join(test_dir, '..', 'test-input')
    assert os.path.exists(input_dir)
    assert os.path.isdir(input_dir)
    assert os.listdir(input_dir) == [
        os.path.join(input_dir, 'cookiecutter-pypackage')
    ]

    project_template = find_template(input_dir)

    assert project_template == 'cookiecutter-pypackage'
    assert os.path.exists(project_template)
    assert os.path.isdir(project_template)

    # Test for multiple directories within repo_dir
    input

# Generated at 2022-06-13 18:28:09.435434
# Unit test for function find_template
def test_find_template():
    """Verify find_template() returns expected values."""
    from .repository import git_clone

    repo_dir = git_clone(
        'https://github.com/audreyr/cookiecutter-pypackage.git'
    )

    # The cookiecutter-pypackage repo has the templated directory named
    # cookiecutter-{{cookiecutter.repo_name}}
    expected = os.path.join(
        repo_dir, 'cookiecutter-{{cookiecutter.repo_name}}'
    )
    assert find_template(repo_dir) == expected

    return

# Generated at 2022-06-13 18:28:16.947418
# Unit test for function find_template
def test_find_template():
    """
    Assert that the function find_template returns the correct template
    """
    from cookiecutter.main import cookiecutter
    from cookiecutter import utils
    from nose.tools import assert_equal, assert_false
    from jinja2 import Environment
    from jinja2 import meta

    # Setting up a test cookiecutter environment
    result = cookiecutter('tests/fake-repo-tmpl/')
    temp_repo_path = os.path.join(result['repo_dir'], "{{cookiecutter.repo_name}}")
    cookiecutter_rfuture = utils.make_sure_path_exists(temp_repo_path)
    env = Environment()
    template = env.from_string(cookiecutter_rfuture)

# Generated at 2022-06-13 18:28:22.801890
# Unit test for function find_template
def test_find_template():

    repo_dir = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        'test_repo',
        'json',
    )

    project_template = find_template(repo_dir)
    assert 'cookiecutter-json' in project_template

# Generated at 2022-06-13 18:28:23.988224
# Unit test for function find_template
def test_find_template():
    os.path.exists(find_template)

# Generated at 2022-06-13 18:28:32.403639
# Unit test for function find_template
def test_find_template():
    from cookiecutter.tests.test_utils import temp_chdir
    from cookiecutter import utils
    from cookiecutter import repository
    from cookiecutter import vcs

    jinja = utils.test_mock('Jinja2')
    os = utils.test_mock('os')
    vcs = utils.test_mock('cookiecutter.vcs')

    old_cwd = os.getcwd.return_value = '/home/audreyr/projects'
    repo_dir = os.path.join(old_cwd, 'fake-repo')
    os.makedirs(repo_dir)

    project_dir = os.path.join(repo_dir, '{{cookiecutter.repo_name}}')
    os.makedirs(project_dir)



# Generated at 2022-06-13 18:28:33.045629
# Unit test for function find_template
def test_find_template():
    pass

# Generated at 2022-06-13 18:28:39.952255
# Unit test for function find_template
def test_find_template():
    """
    Verifies function can find project template in cloned repo
    """

    # Create temporary folder and create test template inside
    import tempfile
    import shutil
    from cookiecutter.main import cookiecutter

    temp_dir = tempfile.mkdtemp()

    test_name = os.path.join(temp_dir, '{{ cookiecutter.repo_name }}')
    cookiecutter(os.path.join(temp_dir, '{{ cookiecutter.repo_name }}'), no_input=True)

    assert find_template(temp_dir) == test_name

    shutil.rmtree(temp_dir)

# Generated at 2022-06-13 18:28:41.854725
# Unit test for function find_template
def test_find_template():
    find_template("/cookiecutter-master/cookiecutter-master/tests/test-tmp")

# Generated at 2022-06-13 18:28:48.882733
# Unit test for function find_template
def test_find_template():
    local_repo = 'tests/test-cookiecutters/fake-repo'
    get_template = find_template(local_repo)
    assert 'fake-repo/{{cookiecutter.repo_name}}' in get_template

# Generated at 2022-06-13 18:28:50.782031
# Unit test for function find_template
def test_find_template():
    repo_dir = 'C:/Users/vishal/PycharmProjects/mendel'
    return repo_dir

# Generated at 2022-06-13 18:28:56.656489
# Unit test for function find_template
def test_find_template():
    """Return 'cookiecutter/{{cookiecutter.repo_name}}' from repo_dir."""
    from .compat import TemporaryDirectory

    with TemporaryDirectory() as tmpdir:
        template_dir = os.path.join(tmpdir, 'cookiecutter/{{cookiecutter.repo_name}}')
        os.makedirs(template_dir)
        output = find_template(tmpdir)

        assert output == template_dir


# Generated at 2022-06-13 18:29:04.015238
# Unit test for function find_template
def test_find_template():
    """Verify find_template() works properly."""
    # TODO: Need to mock out git.Repo, not just os.*
    import shutil
    import tempfile

    repo_dir = tempfile.mkdtemp()
    origin = os.path.join(repo_dir, 'cookiecutter-pypackage')
    shutil.copytree(
        os.path.join(os.path.dirname(__file__), '..', 'tests', 'fake-repo-pre-gen'),
        origin
    )

    template_path = find_template(origin)

    assert os.path.isfile(template_path)

    shutil.rmtree(origin)

# Generated at 2022-06-13 18:29:10.420721
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'tests', 'test-repo-pre'))
    project_template = find_template(repo_dir)
    assert project_template == 'tests/test-repo-pre/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:29:20.578168
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.abspath(os.path.join(
        os.path.dirname(os.path.abspath(__file__)), '..', 'tests',
        'fake-repo', '{{cookiecutter.repo}}'
    ))

    project_template_dir = os.path.join(repo_dir, 'project_template')
    os.mkdir(project_template_dir)

    project_template = find_template(repo_dir)
    assert os.path.exists(project_template)
    assert project_template == project_template_dir
    os.rmdir(project_template_dir)


# Generated at 2022-06-13 18:29:26.103494
# Unit test for function find_template
def test_find_template():
    """If a templated item exists in a vanilla input dir, return it as the template."""
    # Path to the vanilla cookiecutter-pypackage template
    repo_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        '..',
        'tests',
        'test-find-template',
    )

    # Test with a templated item in the root of the directory
    repo_dir_contents = os.listdir(repo_dir)
    for item in repo_dir_contents:
        assert 'cookiecutter' in item and '{{' in item and '}}' in item
    assert find_template(repo_dir)

# Generated at 2022-06-13 18:29:30.500145
# Unit test for function find_template
def test_find_template():
    import tempfile
    import shutil
    import os

    repo_dir = tempfile.mkdtemp()

    project_template = os.path.join(repo_dir, '{{cookiecutter.project_name}}')
    os.mkdir(project_template)

    assert find_template(repo_dir) == '{}'.format(project_template)

    shutil.rmtree(repo_dir)

# Generated at 2022-06-13 18:29:36.046700
# Unit test for function find_template
def test_find_template():
    test_repo_dir = os.path.join(os.path.dirname(__file__), os.pardir, 'tests', 'fake_repo_pre_gen', 'fake_repo')
    test_project_template = os.path.join(test_repo_dir, '{{cookiecutter.repo_name}}')
    assert find_template(test_repo_dir) == test_project_template

# Generated at 2022-06-13 18:29:46.136251
# Unit test for function find_template
def test_find_template():
    from cookiecutter.main import cookiecutter as cc
    from cookiecutter import utils
    pwd = os.path.dirname(os.path.abspath(__file__))
    cc_dir = utils.get_user_config_path()
    templates_dir = os.path.join(cc_dir, 'templates')
    shutil.rmtree(templates_dir, ignore_errors=True)
    shutil.copytree(
        os.path.join(pwd, '..', 'tests', 'test-template'),
        os.path.join(templates_dir, 'test-template')
    )
    template = os.path.join(templates_dir, 'test-template')
    shutil.rmtree(template, ignore_errors=True)

# Generated at 2022-06-13 18:29:50.740455
# Unit test for function find_template
def test_find_template():
    pass

# Generated at 2022-06-13 18:29:59.333347
# Unit test for function find_template
def test_find_template():
    """Verify `find_template` function."""
    from cookiecutter import utils

    template = utils.find_template(
        os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'tests', 'fake-repo-pre'))
    )

    assert template == os.path.abspath(os.path.join(
        os.path.dirname(__file__), '..', 'tests', 'fake-repo-pre',
        '{{cookiecutter.repo_name}}'
    ))

# Generated at 2022-06-13 18:30:05.877536
# Unit test for function find_template
def test_find_template():
    """ Test to check if the find_template function is working """

    sample_dir = "/home/sidhant/cookiecutter_test_repo/cookiecutter-pypackage"
    project_template = find_template(sample_dir)
    reference_template = os.path.join(sample_dir,
                                      "cookiecutter-pypackage")
    if project_template == reference_template:
        return True
    else:
        return False

# Generated at 2022-06-13 18:30:17.549532
# Unit test for function find_template
def test_find_template():
    assert(find_template('./tests/fake-repo-tmpl') ==
           './tests/fake-repo-tmpl/{{cookiecutter.repo_name}}')
    assert(find_template('./tests/fake-repo-pre/') ==
           './tests/fake-repo-pre/fake-project')
    assert(find_template('./tests/fake-repo-post') ==
           './tests/fake-repo-post/fake-project')
    assert(find_template('./tests/fake-repo-pre/fake-project') ==
           './tests/fake-repo-pre/fake-project')

# Generated at 2022-06-13 18:30:25.936534
# Unit test for function find_template
def test_find_template():
    test_files = ['cookiecutter-pypackage', 'cookiecutter-demo1']
    for test_file in test_files:
        repo_dir = os.path.join(os.path.dirname(__file__),
                                'tests/test-input',
                                test_file)
        project_template = find_template(repo_dir)
        assert(project_template == os.path.join(repo_dir, 'cookiecutter-{{cookiecutter.repo_name}}'))

# Generated at 2022-06-13 18:30:33.006552
# Unit test for function find_template
def test_find_template():
    """Test function find_template

    Any directory in which this function runs is searched for a directory
    containing the string `cookiecutter`. This is not a perfect solution,
    but assuming the unit test is run in the `cookiecutter` repo it will
    successfully locate the templates directory.
    """
    import sys
    import pytest

    test_dir = os.path.abspath(os.path.dirname(__file__))
    project_template = os.path.join(test_dir, '..', '..', 'cookiecutter')
    result = find_template(test_dir)
    assert result == project_template



# Generated at 2022-06-13 18:30:43.566377
# Unit test for function find_template
def test_find_template():
    from cookiecutter import utils
    from cookiecutter import exceptions
    from mock import patch

    repo_dir = '/Users/audreyr/projects/cookiecutter-pypackage'

    # Test when the project template exists.
    find_template_mock = patch(
        '{0}.find_template'.format(utils.__name__),
        return_value='{{cookiecutter.repo_name}}'
    )
    with find_template_mock:
        test_template_dir = utils.find_template(repo_dir)
        assert test_template_dir == '{{cookiecutter.repo_name}}'

    # Test when there is no project template.

# Generated at 2022-06-13 18:30:48.766203
# Unit test for function find_template
def test_find_template():
    """Find the template in a repository."""
    repo_dir = 'tests/fake-repo'
    project_template = find_template(repo_dir)
    assert project_template == 'tests/fake-repo/{{cookiecutter.repo_name}}', 'project_template is not correct.'



# Generated at 2022-06-13 18:30:57.719031
# Unit test for function find_template
def test_find_template():
    """Unit test for function ``find_template``."""
    test_repo_dir = os.path.join(
        os.path.dirname(__file__),
        '..',
        'tests',
        'test-data'
    )
    test_project_template = os.path.join(
        test_repo_dir,
        'mytemplate-{{cookiecutter.repo_name}}'
    )

    assert find_template(test_repo_dir) == test_project_template

# Generated at 2022-06-13 18:31:06.995967
# Unit test for function find_template
def test_find_template():
    """Test the find_template function from utils.py"""
    import shutil
    from cookiecutter.compat import TemporaryDirectory

    with TemporaryDirectory() as temp_dir:
        # Create a repo containing the project template
        temp_repo = os.path.join(temp_dir, 'test_repo', 'fake')
        os.makedirs(temp_repo)
        shutil.copyfile(
            os.path.join(os.path.dirname(__file__), '..', 'tests', 'fake_repo',
                         '{{cookiecutter.repo_name}}', 'README.rst'),
            os.path.join(temp_repo, 'README.rst')
        )

        # Run find_template
        template = find_template(temp_repo)

# Generated at 2022-06-13 18:31:22.914364
# Unit test for function find_template
def test_find_template():
    """Verify find_template() returns expected results.
    """
    from cookiecutter import cli
    from cookiecutter import main

    # Create a new empty dir to use as the repo dir
    repo_dir = cli.make_empty_dir()

    # Create a new directory that should not be found
    os.mkdir(os.path.join(repo_dir, 'foo'))

    # Create a new directory that should be found
    os.mkdir(os.path.join(repo_dir, '{{cookiecutter.repo_name}}'))

    # Check that our find_template function returns the correct path
    expected = os.path.join(repo_dir, '{{cookiecutter.repo_name}}')
    results = find_template(repo_dir)
    assert expected == results

# Generated at 2022-06-13 18:31:27.755458
# Unit test for function find_template
def test_find_template():
    repo_dir = 'tests/files/fake-repo'
    project_template = find_template(repo_dir)
    assert os.path.basename(project_template) == '{{cookiecutter.repo_name}}'


# Generated at 2022-06-13 18:31:32.222867
# Unit test for function find_template
def test_find_template():
    repo_dir = "/Users/audreyr/cookiecutter-pypackage/"
    repo_dir_contents = os.listdir(repo_dir)

    project_template = None
    for item in repo_dir_contents:
        if 'cookiecutter' in item and '{{' in item and '}}' in item:
            project_template = item
            break

    if project_template:
        project_template = os.path.join(repo_dir, project_template)
        logging.debug('The project template appears to be %s', project_template)
        assert project_template == "/Users/audreyr/cookiecutter-pypackage/{{cookiecutter.repo_name}}"

# Generated at 2022-06-13 18:31:42.598807
# Unit test for function find_template
def test_find_template():
    """Test to see if all the project template are found"""

    # Mock Testing
    from unittest.mock import patch
    from cookiecutter.exceptions import NonTemplatedInputDirException

    repo_dir_contents = {
        'project_template': True, 'git': False, 'gitignore': False, 'README': False, 'ReAdmE': False
    }

    with patch('cookiecutter.prompt.read_directory', return_value=repo_dir_contents):
        project_template = find_template('repo_dir')
        assert project_template is True

    repo_dir_contents = {
        'dummy': True, 'git': False, 'gitignore': False, 'README': False, 'ReAdmE': False
    }


# Generated at 2022-06-13 18:31:53.010879
# Unit test for function find_template
def test_find_template():
    """Unit test to assert that the find_template function is working as expected."""

    # Create a directory and give it a file called hello
    os.makedirs('/test_dir')
    with open('/test_dir/hello', 'w'):
        pass

    assert find_template('/test_dir') == '/test_dir/hello'
    os.remove('/test_dir/hello')
    os.rmdir('/test_dir')

if __name__ == '__main__':
    test_find_template()

# Generated at 2022-06-13 18:32:05.175886
# Unit test for function find_template
def test_find_template():
    """Unit test for function find_template."""
    from cookiecutter import utils
    from .compat import patch

    repo_dir = os.path.sep.join(
        os.path.abspath(__file__).split(os.path.sep)[:-2] + ['tests', 'fake-repo']
    )
    expected_project_template = os.path.sep.join(
        [repo_dir, '{{cookiecutter.repo_name}}']
    )

    find_template_func = patch.object(
        utils, 'find_template', return_value=expected_project_template
    )

    with find_template_func as mock_find_template:
        result = utils.find_template(repo_dir)
        mock_find_template.assert_called_

# Generated at 2022-06-13 18:32:10.681989
# Unit test for function find_template
def test_find_template():
    import tempfile
    import shutil

    repo_dir = tempfile.mkdtemp()
    os.makedirs(os.path.join(repo_dir, '{{cookiecutter.repo_name}}'))
    os.makedirs(os.path.join(repo_dir, 'not-a-project-template'))
    expected = os.path.join(repo_dir, '{{cookiecutter.repo_name}}')
    assert find_template(repo_dir) == expected

    shutil.rmtree(repo_dir)

# Generated at 2022-06-13 18:32:16.196809
# Unit test for function find_template
def test_find_template():
    """Check if find_template returns the correct template directory path."""
    repo_dir = '/Users/audreyr/code/cookiecutter-pypackage/tests/test-find-repo'
    project_template = find_template(repo_dir)

    assert project_template == os.path.join(repo_dir, 'cookiecutter-pypackage')

# Generated at 2022-06-13 18:32:21.283819
# Unit test for function find_template
def test_find_template():
    this_dir, this_filename = os.path.split(__file__)
    fixture_dir = os.path.join(this_dir, 'fixtures', 'find_template')
    template_dir = find_template(fixture_dir)
    assert template_dir == os.path.join(fixture_dir, '{{cookiecutter.repo_name}}')

# Generated at 2022-06-13 18:32:26.355223
# Unit test for function find_template
def test_find_template():
    assert find_template(os.path.abspath(os.path.join(
        os.path.dirname(__file__),
        '..',
        'tests',
        'fake-repo-pre'
    ))) == os.path.abspath(os.path.join(
        os.path.dirname(__file__),
        '..',
        'tests',
        'fake-repo-pre',
        '{{cookiecutter.repo_name}}',
    ))

# Generated at 2022-06-13 18:32:47.683234
# Unit test for function find_template
def test_find_template():
    """Test the function find_template."""
    from shutil import rmtree
    from cookiecutter.utils import rmtree

    # Create a project template with a templated dirname
    repo_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                            'fake-repo-tmpl')
    project_template = find_template(repo_dir)
    assert project_template == os.path.join(repo_dir, '{{cookiecutter.repo_name}}')
    # Clean up
    rmtree(repo_dir)

# Generated at 2022-06-13 18:32:49.956693
# Unit test for function find_template
def test_find_template():
    find_template('django-cookiecutter-2/tests/fake-repo-pre/')

# Generated at 2022-06-13 18:32:50.717917
# Unit test for function find_template
def test_find_template():
    #TODO
    pass

# Generated at 2022-06-13 18:32:52.786697
# Unit test for function find_template
def test_find_template():
    find_template('/home/tylerlk/projects/cookiecutter-code-snippets/tests/fake-repo-tmpl')

# Generated at 2022-06-13 18:32:57.297635
# Unit test for function find_template

# Generated at 2022-06-13 18:33:08.457534
# Unit test for function find_template
def test_find_template():
    """Unit testing for find_template.

    Creates a test directory, clones a Cookiecutter repo into it, and makes sure
    that find_template finds the correct directory.
    """
    from shutil import rmtree
    from tempfile import mkdtemp
    from cookiecutter.repository import git
    from cookiecutter import __version__

    # Create a temporary directory and give it a Cookiecutter template dir
    test_dir = mkdtemp()
    repo_dir = os.path.join(test_dir, 'test_template')
    git.clone(
        'https://github.com/audreyr/cookiecutter-pypackage.git',
        repo_dir,
        checkout='',
        no_input=True,
    )

    project_template = find_template(repo_dir)

   

# Generated at 2022-06-13 18:33:09.881299
# Unit test for function find_template
def test_find_template():
    """Return a project template when repo_dir is not a template."""
    pass

# Generated at 2022-06-13 18:33:16.231268
# Unit test for function find_template
def test_find_template():
    log = logging.getLogger(__name__)
    log.info('Unit test for function find_template')
    testdir = os.path.dirname(__file__)
    test_template = find_template(testdir)
    expected_template = os.path.join(testdir, 'tests', 'fake-repo-pre', '{{cookiecutter.repo_name}}')
    log.info('Asserting test_template == expected_template')
    assert test_template == expected_template

# Generated at 2022-06-13 18:33:18.500259
# Unit test for function find_template
def test_find_template():
    repo_dir = 'a/path/to/some/repo/on/the/file-system'
    actual_result = find_template(repo_dir)
    expected_result = os.path.join(repo_dir, 'other_dir')
    assert actual_result == expected_result

# Generated at 2022-06-13 18:33:24.780368
# Unit test for function find_template
def test_find_template():
    """Verify that the find_template function works as expected."""
    repo_dir = (
        os.path.abspath(os.path.join(
            os.path.dirname(__file__), '..', 'tests', 'test-find-template'
        ))
    )

    project_template = os.path.abspath(find_template(repo_dir))

    assert project_template == os.path.join(repo_dir, '{{cookiecutter.project_name}}')

# Generated at 2022-06-13 18:33:59.224784
# Unit test for function find_template
def test_find_template():
    assert find_template('tests/test-repos/good-repo') == 'tests/test-repos/good-repo/{{cookiecutter.repo_name}}'
    try:
        assert find_template('tests/test-repos/bad-repo')
    except NonTemplatedInputDirException:
        True

if __name__ == '__main__':
    test_find_template()

# Generated at 2022-06-13 18:34:11.200346
# Unit test for function find_template
def test_find_template():
    """Test function find_template()."""
    import shutil
    import tempfile

    # Make a fake repo using a temp directory
    temp_dir_name = tempfile.mkdtemp()
    os.mkdir(os.path.join(temp_dir_name, 'another_dir'))
    os.mkdir(os.path.join(temp_dir_name, 'cookiecutter-pypackage'))
    os.mkdir(os.path.join(temp_dir_name, 'cookiecutter-pypackage-master'))
    os.mkdir(os.path.join(temp_dir_name, 'cookiecutter-pypackage-{{cookiecutter.repo_name}}'))

# Generated at 2022-06-13 18:34:18.635759
# Unit test for function find_template
def test_find_template():
    input_dir = '/home/audreyr/code/cookiecutter-pypackage'
    project_template = '/home/audreyr/code/cookiecutter-pypackage/{{cookiecutter.project_slug}}'
    assert find_template(input_dir) == project_template

test_find_template()

# Generated at 2022-06-13 18:34:22.427464
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.expanduser('~/.cookiecutters/cookiecutter-pypackage')
    find_template(repo_dir)

# Generated at 2022-06-13 18:34:24.062182
# Unit test for function find_template
def test_find_template():
    find_template('/home/vagrant/cookiecutter-pypackage/tests')

# Generated at 2022-06-13 18:34:28.921002
# Unit test for function find_template
def test_find_template():
    """Test find template function."""

    # Create test project template
    os.makedirs('.tests/fake-repo/fake_project/')

    # Run find_template function
    project_template = find_template('.tests/fake-repo/')

    assert project_template == '.tests/fake-repo/fake_project/'

    # Clean up
    os.rmdir('.tests/fake-repo/fake_project/')

# Generated at 2022-06-13 18:34:35.194779
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'tests', 'fake-repo-pre')
    template_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'tests', 'fake-repo-pre', '{{cookiecutter.repo_name}}')
    find_template(repo_dir)
    assert find_template(repo_dir) == template_dir

# Generated at 2022-06-13 18:34:42.552203
# Unit test for function find_template
def test_find_template():
    """
    Test that the function can find the project template in a git repo.
    """
    import shutil
    import tempfile
    import git

    git_repo = git.Repo.init(tempfile.mkdtemp())
    os.makedirs(os.path.join(git_repo.working_dir, '{{cookiecutter.repo_name}}'))
    open(os.path.join(git_repo.working_dir, 'readme.md'), 'a').close()

    try:
        template_dir = find_template(git_repo.working_dir)
    finally:
        shutil.rmtree(git_repo.working_dir)


# Generated at 2022-06-13 18:34:50.294486
# Unit test for function find_template
def test_find_template():
    """Verify find_template returns the correct template dir."""
    from cookiecutter import utils
    template_dir = os.path.join(
        os.path.dirname(utils.__file__),
        '..',
        'tests',
        'fake-repo-pre',
        '{{cookiecutter.repo_name}}'
    )
    assert find_template(os.path.dirname(template_dir)) == template_dir

# Generated at 2022-06-13 18:34:57.131973
# Unit test for function find_template
def test_find_template():
    repo_dir = 'some/path/some_repo'
    non_template_dir = 'some/path/some_repo/whatever'
    template_dir = 'some/path/some_repo/{{cookiecutter.repo_name}}'
    repo_dir_contents = [non_template_dir, template_dir]

    # Patched os.listdir
    original_listdir = os.listdir
    os.listdir = lambda repo_dir: repo_dir_contents
    try:
        assert find_template(repo_dir) == template_dir
    finally:
        os.listdir = original_listdir

# Generated at 2022-06-13 18:36:00.790857
# Unit test for function find_template
def test_find_template():
    repo_dir = '/Users/foo/{{cookiecutter.repo_name}}'
    project_template = '/Users/foo/{{cookiecutter.repo_name}}/{{cookiecutter.repo_name}}'

    assert find_template(repo_dir) == project_template

# Generated at 2022-06-13 18:36:02.259163
# Unit test for function find_template
def test_find_template():
    pass


# Generated at 2022-06-13 18:36:05.855277
# Unit test for function find_template
def test_find_template():
    assert find_template('./tests/fake-repo-tmpl') == '/fake-repo-tmpl/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:36:08.382413
# Unit test for function find_template
def test_find_template():
    print("Testing...find_template")
    assert find_template('repo_dir') == project_template

# Generated at 2022-06-13 18:36:20.035615
# Unit test for function find_template
def test_find_template():
    """Test that the find_template function returns the correct value"""
    # mock a repo_dir containing a viable template directory.
    template_dir = 'cookiecutter-{{cookiecutter.author_name}}'
    repo_dir = "/home/user/.cookiecutters/malev/test"
    template_path = os.path.join(repo_dir, template_dir)
    repo_dir = [os.path.basename(template_path), "README.rst"]

    # Call find_template with mock repo_dir and validate the return value
    assert find_template(repo_dir) == template_path

    # Mock a repo_dir with no viable template directory
    repo_dir.remove(os.path.basename(template_path))

    # Call find_template with mock repo_dir and validate the return value
   

# Generated at 2022-06-13 18:36:24.077826
# Unit test for function find_template
def test_find_template():
    path = os.path.join('tests', 'files', 'fake-repo-tmpl')
    assert find_template(os.path.join(path)) == os.path.join(
        path, '{{cookiecutter.repo_name}}'
    )

# Generated at 2022-06-13 18:36:26.913121
# Unit test for function find_template
def test_find_template():
    template_path = find_template('/my/path/to/repo/')
    assert(template_path == '/my/path/to/repo/cookiecutter-my-repo')



# Generated at 2022-06-13 18:36:30.279212
# Unit test for function find_template
def test_find_template():
    assert find_template('/Users/audreyr/cookiecutter-pypackage') == \
        '/Users/audreyr/cookiecutter-pypackage/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:36:39.611997
# Unit test for function find_template
def test_find_template():
    # Create a test repo directory with child directories
    test_repo_dir = 'tests/test-find-template'
    os.makedirs(
        os.path.join(test_repo_dir, 'cookiecutter-{{ cookiecutter.project_slug }}')
    )
    os.makedirs(
        os.path.join(test_repo_dir, 'cookiecutter-cookiecutter-py')
    )
    os.makedirs(
        os.path.join(test_repo_dir, 'cookiecutter-python')
    )
    os.makedirs(
        os.path.join(test_repo_dir, 'cookiecutter-foo')
    )

# Generated at 2022-06-13 18:36:44.160219
# Unit test for function find_template
def test_find_template():
    test_dir = os.path.join(
         os.path.dirname(__file__), 'files', 'test-repo-pre-gen',
    )
    project_template_dir = find_template(test_dir)
    project_template_dir_expected = os.path.join(
         os.path.dirname(__file__), 'files', 'test-repo-pre-gen',
         'cookiecutter-pypackage',
    )
    assert project_template_dir == project_template_dir_expected, \
        'find_template() did not find expected directory'