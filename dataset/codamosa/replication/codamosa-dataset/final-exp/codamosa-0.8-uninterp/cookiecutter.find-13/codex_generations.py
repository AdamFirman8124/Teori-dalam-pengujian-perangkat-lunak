

# Generated at 2022-06-13 18:27:38.917781
# Unit test for function find_template
def test_find_template():
    assert find_template('/home/annie/projects/cookiecutter-pypackage') == '/home/annie/projects/cookiecutter-pypackage/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:27:45.630832
# Unit test for function find_template
def test_find_template():
    """Unit testing for function."""
    test_repo_dir = 'tests/test-repo'
    project_template = find_template(test_repo_dir)
    assert project_template == 'tests/test-repo/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:27:46.385606
# Unit test for function find_template
def test_find_template():
    # TODO
    pass

# Generated at 2022-06-13 18:27:49.258423
# Unit test for function find_template
def test_find_template():
    """Tests the find_template() function."""
    repo_dir = 'tests/test-find-template/fake-repo'
    template_dir = find_template(repo_dir)
    assert template_dir == 'tests/test-find-template/fake-repo/fake-project/'

test_find_template()

# Generated at 2022-06-13 18:27:58.803320
# Unit test for function find_template
def test_find_template():
    """Test function find_template()."""
    import time
    import shutil
    from cookiecutter.vcs import clone

    repo_url = 'https://github.com/audreyr/cookiecutter-pypackage.git'
    repo_dir = 'tests/test-find-repo/{0}'.format(int(time.time()))
    clone(repo_url, repo_dir)

    project_template = find_template(repo_dir)

    # Clean up the cloned repo
    shutil.rmtree(repo_dir)

    assert project_template == 'tests/test-find-repo/{0}/{{cookiecutter.repo_name}}'.format(int(time.time()))

# Generated at 2022-06-13 18:28:08.914230
# Unit test for function find_template
def test_find_template():
    """Smoke test for find_template()."""
    from cookiecutter.compat import TemporaryDirectory
    from tests.test_repository import a_hexsha
    from tests.test_repository import a_repo

    with TemporaryDirectory() as repo_dir:
        repo = a_repo(repo_dir)
        repo.git.checkout(a_hexsha(repo))
        project_template = find_template(repo_dir)
        assert project_template == os.path.join(repo_dir, '{{cookiecutter.repo_name}}')


# Generated at 2022-06-13 18:28:13.515238
# Unit test for function find_template
def test_find_template():
    # TODO: This test only tests a single edge case, but it's better than
    # nothing...
    expected = 'tests/fake-repo-tmpl/{{cookiecutter.project_name}}'

    repo_dir = 'tests/fake-repo-tmpl'
    actual = find_template(repo_dir)

    assert expected == actual

# Generated at 2022-06-13 18:28:18.016539
# Unit test for function find_template
def test_find_template():
    assert find_template('tests/fixtures/fake-repo') == 'tests/fixtures/fake-repo/{{cookiecutter.repo}}-{{cookiecutter.repo_type}}'

# Generated at 2022-06-13 18:28:29.996683
# Unit test for function find_template
def test_find_template():
    """Test find_template with a real repo clone."""
    import os
    import tempfile
    #from mock import patch
    
    sample_repo = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__), 
            '..', 
            '..', 
            'tests', 
            'test-data', 
            'fake-repo'
        )
    )
    repo_dir = tempfile.mkdtemp()
    #with patch.object(os, 'listdir') as listdir_mock:
    #    listdir_mock(repo_dir)
    #    os.listdir(sample_repo)
    #
    #    result = find_template(repo_dir)
    #
    #    expected = os

# Generated at 2022-06-13 18:28:39.523141
# Unit test for function find_template
def test_find_template():
    from unittest import TestCase
    import shutil
    from cookiecutter import utils
    from cookiecutter.exceptions import NonTemplatedInputDirException

    repo_dir = 'tests/fake-repo-tmpl'
    template = 'fake-project'

    class TestFindTemplate(TestCase):
        """Test the find_template function."""

        def tearDown(self):
            """Clean up copied fake repo."""
            repo_tmpl_path = os.path.join(repo_dir, '{{cookiecutter.repo_name}}')
            template_path = os.path.join(repo_dir, template)
            shutil.rmtree(template_path)
            os.rename(repo_tmpl_path, template_path)


# Generated at 2022-06-13 18:28:47.429363
# Unit test for function find_template
def test_find_template():
    # Create a directory that contains a subdirectory with a cookiecutter
    # reference.
    import tempfile
    template_dir = tempfile.mkdtemp()
    os.makedirs(os.path.join(template_dir, 'cookiecutter-django'))

    # Try to find the template
    tmpl = find_template(template_dir)
    assert tmpl == os.path.join(template_dir, 'cookiecutter-django')

    # Make sure the function handles it if no cookiecutter-based directory
    # exists in the input dir
    bad_template_dir = tempfile.mkdtemp()
    os.makedirs(os.path.join(bad_template_dir, 'some-other-dir'))

# Generated at 2022-06-13 18:28:50.415897
# Unit test for function find_template
def test_find_template():
    """Unit test for function find_template"""
    repo_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),
        '..', 'tests', 'fake-repo'))
    template = 'fake-repo/{{cookiecutter.repo_name}}/{{cookiecutter.repo_name}}'
    assert find_template(repo_dir) == template

# Generated at 2022-06-13 18:28:57.198105
# Unit test for function find_template
def test_find_template():
    """Unit tests for the function find_template"""
    cwd = os.getcwd()
    repo_dir = os.path.join(cwd, 'tests', 'test-find-template')
    logger.debug('Running unit test on repo_dir: %s', repo_dir)
    test_template = find_template(repo_dir)
    assert test_template == os.path.join(repo_dir,
                                         'cookiecutter-pypackage-{{cookiecutter.repo_name}}'), "Test template dir incorrect"

# Generated at 2022-06-13 18:29:02.808513
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '../tests/test-input/fake-repo-pre/'
        )
    )
    result = find_template(repo_dir)

    assert os.path.exists(result)

    template_dir_contents = os.listdir(result)
    assert '{{cookiecutter.repo_name}}' in template_dir_contents

# Generated at 2022-06-13 18:29:05.745626
# Unit test for function find_template
def test_find_template():
    assert find_template('html5-boilerplate') == 'html5-boilerplate/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:29:11.308559
# Unit test for function find_template
def test_find_template():
    cookiecutter_dict = {
            'repo_dir': 'tests/fake-repo',
            'project_template': 'tests/fake-repo/{{cookiecutter.repo_name}}'
    }
    assert find_template(cookiecutter_dict['repo_dir']) == cookiecutter_dict['project_template']



# Generated at 2022-06-13 18:29:22.689337
# Unit test for function find_template
def test_find_template():
    """Verify that we find the template directory in a repo.

    Also verify that we raise a NonTemplatedInputDirException
    when the repo has no template.
    """
    repo_dir = os.path.abspath(os.path.dirname(__file__))
    template = find_template(repo_dir)
    assert template.endswith('tests/fake-repo-pre/fake_template')

    # Testing template does not exist
    os.chdir('tests')
    repo_dir = os.path.abspath(os.path.dirname(__file__))
    from cookiecutter.exceptions import NonTemplatedInputDirException
    try:
        find_template(repo_dir)
    except NonTemplatedInputDirException:
        pass

    os.chdir('..')

# Generated at 2022-06-13 18:29:27.575976
# Unit test for function find_template
def test_find_template():
    """ """
    from cookiecutter.utils import run

    repo_dir = run('git clone git@github.com:audreyr/cookiecutter-pypackage.git')
    project_template = find_template(repo_dir)
    assert 'cookiecutter-pypackage' in project_template
    assert '{{' in project_template
    assert '}}' in project_template

# Generated at 2022-06-13 18:29:31.574070
# Unit test for function find_template
def test_find_template():
    repo_dir = 'tests/test-find-repo/fake-repo'
    assert find_template(repo_dir) == 'tests/test-find-repo/fake-repo/{{cookiecutter.project_name}}'

# Generated at 2022-06-13 18:29:34.808789
# Unit test for function find_template
def test_find_template():
    assert find_template('/Users/audreyr/cookiecutter-pypackage') == '/Users/audreyr/cookiecutter-pypackage/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:29:43.790293
# Unit test for function find_template
def test_find_template():
    """Verify find_template() can detect the project template."""
    import tempfile

    dirpath = tempfile.mkdtemp()
    templated_dirname = 'cookiecutter-{{cookiecutter.repo_name}}'
    templated_dir = os.path.join(dirpath, templated_dirname)
    os.makedirs(templated_dir)

    project_template = find_template(dirpath)

    assert project_template == templated_dir

    # Clean up
    os.remove(templated_dir)
    os.rmdir(dirpath)

# Generated at 2022-06-13 18:29:51.477771
# Unit test for function find_template
def test_find_template():
    print("==========")
    print("Find_template")
    print("==========")
    print("Repo dir: ")
    repo_dir = input()
    print(find_template(repo_dir))

# Test function find_template()
#repo_dir = "C:\\Users\\nicoh\\Desktop\\cookiecutter\\cookiecutter-pypackage-minimal"
#test_find_template()

# Generated at 2022-06-13 18:29:58.228329
# Unit test for function find_template
def test_find_template():
    """
    Test that the right template is being found
    """
    repo_dir = os.path.expanduser("~/projects/cookiecutter-pypackage")
    project_template = find_template(repo_dir)
    print("The project template is at: " + project_template)
    assert project_template == repo_dir + "/{{cookiecutter.project_name}}"


# Generated at 2022-06-13 18:30:06.750884
# Unit test for function find_template
def test_find_template():
    # The setup
    import tempfile
    from shutil import rmtree
    import os

    temp_dir = tempfile.mkdtemp()

    repo_dir = os.path.join(temp_dir, 'repo_dir')
    os.mkdir(repo_dir)

    template_dir = os.path.join(repo_dir, 'some_template_dir')
    os.mkdir(template_dir)

    # The test
    from cookiecutter import finder
    project_template = finder.find_template(repo_dir)
    assert project_template == template_dir

    # The teardown
    rmtree(temp_dir)



# Generated at 2022-06-13 18:30:10.568662
# Unit test for function find_template
def test_find_template():
    assert find_template('tests/test-data/fake-repo') == 'tests/test-data/fake-repo/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:30:11.813563
# Unit test for function find_template
def test_find_template():
    """Unit test for function find_template."""
    pass

# Generated at 2022-06-13 18:30:18.151558
# Unit test for function find_template
def test_find_template():
    """Verify that the function find_template works as expected"""

    repo_dir = "D:/workspace/github/cookiecutter-django/"
    project_template = find_template(repo_dir)

    assert project_template == "D:/workspace/github/cookiecutter-django/{{cookiecutter.project_name}}"

# Generated at 2022-06-13 18:30:18.696482
# Unit test for function find_template
def test_find_template():
    pass



# Generated at 2022-06-13 18:30:19.365481
# Unit test for function find_template
def test_find_template():
    pass

# Generated at 2022-06-13 18:30:23.552361
# Unit test for function find_template
def test_find_template():
    """Test find_template()."""
    import pytest
    from cookiecutter import cli
    from click.testing import CliRunner

    runner = CliRunner()
    project_dir = runner.invoke(cli.main, ['tests/fake-repo-tmpl/'])
    print(project_dir)

if __name__ == '__main__':
    test_find_template()

# Generated at 2022-06-13 18:30:41.762405
# Unit test for function find_template
def test_find_template():
    import pytest
    from cookiecutter import utils
    from cookiecutter.exceptions import NonTemplatedInputDirException
    from tests import fake_repo
    from tests import fixture_path

    repo_dir = fake_repo.make_repo(
        'tests/fake-repo-tmpl',
        checkout='develop'
    )

    project_tmpl = fixture_path('fake-repo-tmpl/{{cookiecutter.repo_name}}')
    logger.debug('project_tmpl is %s', project_tmpl)
    logger.debug('repo_dir is %s', repo_dir)

    template_dir = utils.find_template(repo_dir)
    assert template_dir == project_tmpl

    fake_repo.remove_repo(repo_dir)



# Generated at 2022-06-13 18:30:50.380721
# Unit test for function find_template
def test_find_template():
    '''
    Unit test for function find_template
    '''
    repo_dir_temp = None
    try:
        repo_dir_temp = os.getcwd()
        repo_dir_temp = repo_dir_temp + '/tests/test-find-template'
        os.chdir(repo_dir_temp)

        result = find_template(repo_dir_temp)
        assert os.path.join(repo_dir_temp, '{{cookiecutter.repo_name}}') == result
    finally:
        if repo_dir_temp:
            os.chdir(repo_dir_temp)


# Generated at 2022-06-13 18:31:01.637284
# Unit test for function find_template
def test_find_template():
    """Function to test the find_template function."""
    import tempfile
    import shutil
    import os
    from cookiecutter.utils import rmtree

    temp_dir = tempfile.mkdtemp()
    cookiecutters_dir = os.path.join(temp_dir, 'cookiecutters')
    shutil.copytree(
        'tests/test-data/fake-repo-no-json/',
        cookiecutters_dir
    )
    template_dir = find_template(cookiecutters_dir)

# Generated at 2022-06-13 18:31:08.019133
# Unit test for function find_template
def test_find_template():
    """Unit test for function find_template."""
    # Given a non-templated directory, find_template raises an exception
    try:
        find_template('/Users/audreyr/cookiecutter-pypackage')
    except:
        pass
    else:
        assert False

    # Given a name-templated directory, find_template returns the expected path
    assert find_template('/Users/audreyr/cookiecutter-pypackage-templated') ==\
        '/Users/audreyr/cookiecutter-pypackage-templated/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:31:14.086364
# Unit test for function find_template
def test_find_template():
    test_dir = 'tests/fake-repo-tmpl'
    project_tmpl = find_template(test_dir)
    expected_project_tmpl = os.path.join(test_dir, '{{cookiecutter.repo_name}}')
    assert project_tmpl == expected_project_tmpl

# Generated at 2022-06-13 18:31:22.706114
# Unit test for function find_template
def test_find_template():
    """Find and return the template folder in a repo."""
    import shutil

    # Create a temp repo for testing
    test_repo_path = os.path.abspath('/tmp/test_find_template_repo')
    os.makedirs(test_repo_path)
    template_dir_path = os.path.join(test_repo_path, '{{cookiecutter.repo_name}}')
    os.makedirs(template_dir_path)

    logger.debug('Created test repo in %s', test_repo_path)

    test_template = find_template(test_repo_path)
    assert test_template == template_dir_path

    # Clean up temp repo
    shutil.rmtree(test_repo_path)

# Generated at 2022-06-13 18:31:37.765043
# Unit test for function find_template
def test_find_template():
    """Unit test for function find_template."""
    import tempfile
    from cookiecutter import utils
    from cookiecutter.exceptions import NonTemplatedInputDirException

    def _create_template(template_name):
        """Create a basic project template."""
        template_dir = tempfile.mkdtemp()
        template = os.path.join(template_dir, template_name)
        os.makedirs(template)
        utils.workaround_missing_parent_dir(template)
        return template_dir

    def _remove_template(template):
        """Remove a basic project template."""
        utils.rmtree(template)

    template_name = 'fake-cookiecutter-{{cookiecutter.repo_name}}'
    template_dir = _create_template(template_name)
   

# Generated at 2022-06-13 18:31:44.341735
# Unit test for function find_template
def test_find_template():
    repo_dir = '/tmp/sometemplates'
    repo_dir_contents = ['README.md', 'cookiecutter-{{ cookiecutter.name }}']

    # check if it works with the right repo_dir_contents
    assert find_template(repo_dir) == 'cookiecutter-{{ cookiecutter.name }}'

    # check it raises the right exception if it can't find the template
    repo_dir_contents = ['README.md', 'somenewproject']
    assert find_template(repo_dir) == NonTemplatedInputDirException

# Generated at 2022-06-13 18:31:56.718194
# Unit test for function find_template
def test_find_template():
    """
    Unit test for function find_template.
        :returns project_template: Relative path to project template.
    """
    repo_dir = os.getcwd() + '/test_find_template/test_find_template'

    logger.debug('Searching %s for the project template.', repo_dir)

    repo_dir_contents = os.listdir(repo_dir)

    project_template = None
    for item in repo_dir_contents:
        if 'cookiecutter' in item and '{{' in item and '}}' in item:
            project_template = item
            break

    if project_template:
        project_template = os.path.join(repo_dir, project_template)
        logger.debug('The project template appears to be %s', project_template)

# Generated at 2022-06-13 18:31:59.417120
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.abspath(os.path.join(
        os.path.dirname(__file__), '..', 'tests', 'fake-repo', 'input')
    )
    project_template = find_template(repo_dir)

    expected_project_template = os.path.join(
        repo_dir, '{{cookiecutter.repo_name}}')
    assert project_template == expected_project_template

# Generated at 2022-06-13 18:32:13.616145
# Unit test for function find_template
def test_find_template():
    """
    :returns project_template: Relative path to project template.
    """
    os.chdir('../tests')
    project_template = find_template('.')
    return project_template

# Generated at 2022-06-13 18:32:18.243174
# Unit test for function find_template
def test_find_template():
    pwd = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    template_path = find_template(pwd)
    assert template_path == pwd
    assert os.path.isdir(template_path)


# Generated at 2022-06-13 18:32:23.517509
# Unit test for function find_template
def test_find_template():
    """To be run by py.test."""
    test_repo_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'test-find-template'
    )

    actual = find_template(test_repo_dir)
    assert actual == os.path.join(test_repo_dir, '{{cookiecutter.repo_name}}')



# Generated at 2022-06-13 18:32:30.680140
# Unit test for function find_template
def test_find_template():
    cwd = os.getcwd()
    repo_dir = os.path.join(cwd, 'tests', 'fake-repo')
    project_template = os.path.join(repo_dir, '{{cookiecutter.repo_name}}')
    assert find_template(repo_dir) == project_template

if __name__ == "__main__":
    test_find_template()

# Generated at 2022-06-13 18:32:35.388646
# Unit test for function find_template
def test_find_template():
    """Test for function find_template"""
    PROJECT_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    find_template(os.path.join(PROJECT_DIR, 'test/test_template'))

# To run the unit test, at command line:
# python -c "import cookiecutter.find; cookiecutter.find.test_find_template()"

# Generated at 2022-06-13 18:32:38.380204
# Unit test for function find_template
def test_find_template():
    repo_dir = "~/repos/cookiecutter-pypackage"
    assert find_template(repo_dir) == "cookiecutter-{{cookiecutter.repo_name}}"

# Generated at 2022-06-13 18:32:43.467001
# Unit test for function find_template
def test_find_template():
    repo_dir = '/home/vanessa/Desktop/tests/cookiecutter-pypackage'
    assert find_template(repo_dir) == '/home/vanessa/Desktop/tests/cookiecutter-pypackage/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:32:53.431800
# Unit test for function find_template
def test_find_template():
    """Test for function find_template"""

    repo_dir = '/home/test/cookiecutter-test-repo-1'
    result = find_template(repo_dir)
    repo_dir_contents = os.listdir(repo_dir)
    assert result in repo_dir_contents
    assert result

    repo_dir = '/home/test/cookiecutter-test-repo-2'
    result = find_template(repo_dir)
    repo_dir_contents = os.listdir(repo_dir)
    assert result in repo_dir_contents
    assert result == None


# Generated at 2022-06-13 18:33:01.607169
# Unit test for function find_template
def test_find_template():
    """Test behavior of find_template"""
    import tempfile
    import shutil

    cookiecutter_dir = tempfile.mkdtemp()

    template = os.path.join(cookiecutter_dir, '{{cookiecutter.repo_name}}')
    os.mkdir(template)

    project_template = find_template(cookiecutter_dir)
    assert project_template == template

    shutil.rmtree(cookiecutter_dir)

# Generated at 2022-06-13 18:33:04.580299
# Unit test for function find_template
def test_find_template():
    """Test function find_template using a local repo"""

    find_template("/Users/michaelk/Projects/bootcamp/bootcamp-part-1/bootcamp-1")



# Generated at 2022-06-13 18:33:29.708630
# Unit test for function find_template
def test_find_template():
    template_dir = 'tests/test-data/fake-repo'
    print(find_template(template_dir))

# Run the unit test.
# test_find_template()

# Generated at 2022-06-13 18:33:34.065680
# Unit test for function find_template
def test_find_template():
    repo_dir = '/home/joe/new-repo'
    item = '{{cookiecutter.project_name}}'
    project_template = os.path.join(repo_dir, item)
    
    assert find_template(repo_dir) == project_template

# Generated at 2022-06-13 18:33:39.486760
# Unit test for function find_template
def test_find_template():

    repo_dir = os.path.join('tests', 'test-repo')
    repo_dir_contents = os.listdir(repo_dir)

    assert 'cookiecutter' in repo_dir_contents
    assert '{{' in repo_dir_contents
    assert '}}' in repo_dir_contents

    template = find_template(repo_dir)

    assert 'cookiecutter' in template
    assert '{{' in template
    assert '}}' in template

# Generated at 2022-06-13 18:33:42.088153
# Unit test for function find_template
def test_find_template():
    assert find_template('/path/to/repo') == '/path/to/repo/cookiecutter-{{ cookiecutter.repo_name }}'

# Generated at 2022-06-13 18:33:46.034167
# Unit test for function find_template
def test_find_template():
    repo_dir = repo_dir = os.path.join(
        os.path.dirname(__file__), '..', 'tests', 'fake-repo')
    project_template = find_template(repo_dir)
    assert project_template == os.path.join(repo_dir, 'fake_template')

# Generated at 2022-06-13 18:33:47.298865
# Unit test for function find_template
def test_find_template():
    find_template("example_cookiecutter")



# Generated at 2022-06-13 18:33:53.934543
# Unit test for function find_template
def test_find_template():
    """Test if the function find_template is able to find the proper path"""
    # Without the function argument os.path.exists raise an exception
    if os.path.exists("tests/fake-repo-pre/"):
        no_template = find_template("tests/fake-repo-pre/")
    if os.path.exists("tests/fake-repo/"):
        template = find_template("tests/fake-repo/")
    assert no_template is None
    assert template == "tests/fake-repo/{{cookiecutter.repo_name}}"

# Generated at 2022-06-13 18:33:58.863406
# Unit test for function find_template
def test_find_template():
    assert find_template('tests/fake-repo-pre/') == 'tests/fake-repo-pre/{{cookiecutter.repo_name}}'
    assert find_template('tests/fake-repo-post/') == 'tests/fake-repo-post/fake-repo'

# Generated at 2022-06-13 18:34:08.110868
# Unit test for function find_template
def test_find_template():
    from cookiecutter.tests.test_repo import clone_test_repo
    from cookiecutter import utils

    # Make a temporary 'fake' repository
    tmp_repo_dir = clone_test_repo('pymodule')
    assert find_template(tmp_repo_dir) == os.path.join(
        tmp_repo_dir,
        '{{cookiecutter.repo_name}}'
    )

    utils.rmtree(tmp_repo_dir)



# Generated at 2022-06-13 18:34:11.127531
# Unit test for function find_template
def test_find_template():
    repo_dir = 'tests/fake-repo-tmpl'
    project_template = 'tests/fake-repo-tmpl/{{cookiecutter.repo_name}}'
    assert find_template(repo_dir) == project_template

# Generated at 2022-06-13 18:35:06.509346
# Unit test for function find_template
def test_find_template():
    """Determine which child directory of `repo_dir` is the project template.
    """
    repo_dir = 'files/tests/non-templated'
    project_template = find_template(repo_dir)
    assert project_template == None

    repo_dir = 'files/tests/fake-repo'
    project_template = find_template(repo_dir)
    assert project_template == 'files/tests/fake-repo/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:35:10.226789
# Unit test for function find_template
def test_find_template():
    testdir = 'tests/test-find-repo/fake-repo'
    templated_dir = find_template(testdir)

    assert os.path.isdir(templated_dir) is True
    assert templated_dir == 'tests/test-find-repo/fake-repo/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:35:15.416902
# Unit test for function find_template
def test_find_template():
    """Verify that we can find the template inside a repo we've cloned."""
    #from cookiecutter import main
    #main.cookiecutter(
    #    'tests/fake-repo-pre/',
    #    no_input=True,
    #    overwrite_if_exists=True
    #)
    #TODO: Not sure how to test this with the current API.
    pass

# Generated at 2022-06-13 18:35:30.006922
# Unit test for function find_template
def test_find_template():
    """Test that find_template returns correctly."""
    # Create a fake project
    new_project_name = 'vagrant-debian-python'
    test_cookiecutter_dir = os.path.realpath(
        os.path.join(
            os.path.dirname(__file__),
            '..',
            'tests',
            'test-find-template',
            new_project_name
        )
    )
    test_cookiecutter_path = os.path.join(
        test_cookiecutter_dir,
        '{{cookiecutter.project_name}}'
    )
    expected_output = os.path.abspath(test_cookiecutter_path)

    output = find_template(test_cookiecutter_dir)
    assert expected_output == output

# Generated at 2022-06-13 18:35:30.897475
# Unit test for function find_template
def test_find_template():
    # to be implemented
    pass

# Generated at 2022-06-13 18:35:41.165667
# Unit test for function find_template
def test_find_template():
    """Verify that find_template returns the correct template name."""
    logger.debug('Testing find_template')
    from cookiecutter import utils
    repo_dir = utils.find_repo_dir(
        'https://github.com/audreyr/cookiecutter-pypackage.git',
        'audreyr/cookiecutter-pypackage',
        'cookiecutter-pypackage',
        None,
        overwrite_if_exists=True,
        clone_to_dir='tests/test-find-template'
    )
    return find_template(repo_dir) == os.path.join(repo_dir, '{{cookiecutter.repo_name}}')

# Generated at 2022-06-13 18:35:46.241082
# Unit test for function find_template
def test_find_template():
    """Verify that find_template correctly finds a project template."""
    from cookiecutter import repo

    # Create a repo in a temporary directory
    temp_repo = repo.generate_files(context={'cookiecutter': 'mochi'})
    project_template = find_template(temp_repo)
    assert os.path.join(temp_repo, '{{cookiecutter.repo_name}}') == project_template



# Generated at 2022-06-13 18:35:51.111240
# Unit test for function find_template
def test_find_template():
    """Just for test case.
    """
    test_templated_input_dir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..', 'tests', 'fake-repo-pre'))
    result = find_template(test_templated_input_dir)

# Generated at 2022-06-13 18:35:54.015871
# Unit test for function find_template
def test_find_template():
    assert find_template('test/test-find-template') == os.path.join(
        'test/test-find-template',
        '{{cookiecutter.repo_name}}'
    )



# Generated at 2022-06-13 18:36:03.241821
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.join(
        os.getcwd(),
        'tests',
        'test-find-template'
    )
    project_template = find_template(repo_dir)
    project_template_rel_path = os.path.relpath(project_template, repo_dir)

    logger.debug(
        'We are attempting to assert that %s and %s are equivalent.',
        project_template_rel_path,
        'template-{{cookiecutter.repo_name}}'
    )
    assert project_template_rel_path == 'template-{{cookiecutter.repo_name}}'