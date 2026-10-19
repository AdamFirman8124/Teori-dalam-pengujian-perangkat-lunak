

# Generated at 2022-06-13 18:27:41.833673
# Unit test for function find_template
def test_find_template():
    """Check that the function `find_template` returns the correct value."""
    import shutil
    import tempfile
    logger.warning('This test might be flaky.')
    try:
        my_dir = tempfile.mkdtemp()
        testdir = os.path.join(my_dir, 'tests')
        os.makedirs(testdir)
        template = os.path.join(testdir, '{{cookiecutter.repo_name}}')
        os.makedirs(template)
        project_template = find_template(testdir)
        assert project_template == template
    finally:
        shutil.rmtree(my_dir)

# Generated at 2022-06-13 18:27:49.898200
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.join(
        os.path.expanduser('~'),
        '.cookiecutters',
        'cookiecutter-pypackage'
    )
    project_template = find_template(repo_dir)

    assert project_template == os.path.join(repo_dir, '{{cookiecutter.repo_name}}')

# Generated at 2022-06-13 18:27:54.875488
# Unit test for function find_template
def test_find_template():
    """Verify if template can be found."""
    from tests.test_repos.test_repo import test_repo_dir
    test_repo_dir = os.path.abspath(test_repo_dir)
    find_template(test_repo_dir)
    assert True

# Generated at 2022-06-13 18:28:06.625494
# Unit test for function find_template
def test_find_template():
    """Test the find_template function."""
    test_dir = os.path.join('tests', 'files')
    valid_input_dir = os.path.join(test_dir, 'test-valid-input-dir')
    project_template = find_template(valid_input_dir)
    assert project_template == os.path.join(valid_input_dir, '{{cookiecutter.repo_name}}')

    try:
        invalid_input_dir = os.path.join(test_dir, 'test-invalid-input-dir')
        find_template(invalid_input_dir)
    except NonTemplatedInputDirException:
        pass
    else:
        raise AssertionError('Invalid input directory should raise an exception')

# Generated at 2022-06-13 18:28:11.586727
# Unit test for function find_template
def test_find_template():
    repo_dir = 'test'
    project_template = find_template(repo_dir)
    project_template_expected = 'test/cookiecutter-pypackage'
    assert project_template == project_template_expected


# Generated at 2022-06-13 18:28:15.668471
# Unit test for function find_template
def test_find_template():
    """
    Function find_template() should return the relative path to the project
    template if it can be found.
    """
    repo_dir = os.path.join('tests', 'test-find-project-template', '{{cookiecutter.test_test}}')
    project_template = find_template(repo_dir)
    assert os.path.join(repo_dir, '{{cookiecutter.test_test}}') in project_template



# Generated at 2022-06-13 18:28:17.058408
# Unit test for function find_template
def test_find_template():
    pass

# Generated at 2022-06-13 18:28:23.715031
# Unit test for function find_template
def test_find_template():
    """Test the function which finds the project template directory."""
    test_file_dir = os.path.dirname(__file__)
    test_template = os.path.join(
        test_file_dir,
        'test_template'
    )
    full_template_path = find_template(test_file_dir)
    assert full_template_path == test_template

# Generated at 2022-06-13 18:28:26.862347
# Unit test for function find_template
def test_find_template():
    assert 'tests/fixtures/fake-repo-pre/{{cookiecutter.repo_name}}' == find_template('tests/fixtures/fake-repo-pre')


# Generated at 2022-06-13 18:28:30.299232
# Unit test for function find_template
def test_find_template():
    """Unit test for find_template"""
    logger.debug('Testing find_template')
    logger.debug('Tested find_template')
    return True

# Generated at 2022-06-13 18:28:37.682233
# Unit test for function find_template
def test_find_template():
    import tempfile
    import shutil
    import os

    temp_dir = tempfile.mkdtemp()
    full_path = os.path.join(temp_dir, 'hooks')
    os.mkdir(full_path)
    f = open(full_path + "/post_gen_project.py", "w+")
    f.close()
    test_file = "hooks"
    assert test_file == full_path

# Generated at 2022-06-13 18:28:42.418808
# Unit test for function find_template
def test_find_template():
    template_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'fake-repo/{{cookiecutter.repo_name}}'
    )
    assert find_template(os.path.dirname(os.path.abspath(__file__))) == template_dir

# Generated at 2022-06-13 18:28:48.320825
# Unit test for function find_template
def test_find_template():
    find_template('/home/user/projects/myproject')
    find_template(os.getcwd())
    find_template(os.path.abspath(os.path.join(os.path.curdir, '..')))

# Generated at 2022-06-13 18:28:49.689955
# Unit test for function find_template
def test_find_template():
    # TODO: write test for function find_template
    pass

# Generated at 2022-06-13 18:28:58.904209
# Unit test for function find_template
def test_find_template():
    """Test find template function."""
    # Create a temporary directory
    import pytest
    from cookiecutter.utils import rmtree
    from cookiecutter.compat import sh
    from py._path.local import LocalPath

    tmp_dir = LocalPath(pytest.ensuretemp('test-find-template'))
    tmp_dir.ensure(dir=True)
    tmp_dir.join('test.txt').write('test-content')

    # Create a second directory inside the first
    tmp_cookiecutters_dir = tmp_dir.mkdir('{{cookiecutter.project}}')
    tmp_cookiecutters_dir.join('test2.txt').write('test2-content')

    # Try to find the cookiecutter directory
    project_template = find_template(str(tmp_dir))
    assert project_

# Generated at 2022-06-13 18:28:59.566073
# Unit test for function find_template
def test_find_template():
    pass

# Generated at 2022-06-13 18:29:14.458398
# Unit test for function find_template
def test_find_template():
    from tempfile import mkdtemp
    from shutil import rmtree
    import os

    # Create a bunch of subdirectories
    temp_dir = mkdtemp()
    os.mkdir(os.path.join(temp_dir, 'subdir1'))
    os.mkdir(os.path.join(temp_dir, 'subdir2'))
    os.mkdir(os.path.join(temp_dir, 'subdir3'))
    os.mkdir(os.path.join(temp_dir, 'subdir4'))

    # Template is in subdir1
    result = find_template(temp_dir)
    actual_dir = os.path.dirname(os.path.abspath(result))
    assert actual_dir == temp_dir
    assert os.path.basename(result)

# Generated at 2022-06-13 18:29:16.805233
# Unit test for function find_template
def test_find_template():
    import tempfile
    from cookiecutter.tests.test_utils.create_project import create_project

    repo_dir = tempfile.mkdtemp()
    create_project(repo_dir)

    assert find_template(repo_dir) == os.path.join(repo_dir, '{{cookiecutter.repo_name}}')

# Generated at 2022-06-13 18:29:24.687312
# Unit test for function find_template
def test_find_template():
    """Test find_template function."""
    import tempfile
    import shutil

    repo_dir = tempfile.mkdtemp()
    test_file = os.path.join(repo_dir, 'cookiecutter.json')
    open(test_file, 'a').close()
    try:
        project_template = find_template(repo_dir)
    except NonTemplatedInputDirException:
        assert False
    else:
        assert project_template == test_file
    finally:
        shutil.rmtree(repo_dir, ignore_errors=True)

# Generated at 2022-06-13 18:29:37.219676
# Unit test for function find_template
def test_find_template():
    import pytest
    from cookiecutter.utils import rmtree

    repo_dir = 'tests/fake-repo-tmpl'
    project_template = find_template(repo_dir)
    assert project_template == os.path.join(repo_dir, 'fake-project')

    # Test for NonTemplatedInputDirException
    repo_dir = 'tests/fake-repo'
    exception_raised = False
    try:
        find_template(repo_dir)
    except NonTemplatedInputDirException:
        exception_raised = True
    assert exception_raised == True

    # Clean up
    rmtree(os.path.join(repo_dir, 'fake-project'))



# Generated at 2022-06-13 18:29:53.582096
# Unit test for function find_template
def test_find_template():
    """Verifies that find_template() returns the expected directory name."""
    from cookiecutter.tests.test_utils.test_repos import (
        cookiecutter_py_repo_tmpl_dir, cookiecutter_py_repo_tmpl_dir_no_tmpl
    )

    assert find_template(cookiecutter_py_repo_tmpl_dir) == os.path.join(
        cookiecutter_py_repo_tmpl_dir,
        '{{cookiecutter.repo_name}}'
    )

    # Should raise an exception because no project template is found
    try:
        find_template(cookiecutter_py_repo_tmpl_dir_no_tmpl)
    except NonTemplatedInputDirException as e:
        pass


# Generated at 2022-06-13 18:29:58.388483
# Unit test for function find_template
def test_find_template():
    """Unit test for function find_template."""
    repo_dir = '/Users/example/Dev/code/cookiecutter-django'

    project_template = find_template(repo_dir)
    assert project_template == '/Users/example/Dev/code/cookiecutter-django/cookiecutter-django'

# Generated at 2022-06-13 18:30:08.418387
# Unit test for function find_template
def test_find_template():
    """
    ensure that find_template has the desired behavior.
    """
    import copy
    import shutil
    import tempfile
    import unittest

    class TestFindTemplate(unittest.TestCase):

        def setUp(self):
            self.temp_dir = tempfile.mkdtemp()
            self.temp_repo_dir = os.path.join(self.temp_dir, 'test_repo')

            os.mkdir(self.temp_repo_dir)

            self.temp_template_dir = os.path.join(self.temp_repo_dir, 'my_template')
            os.mkdir(self.temp_template_dir)


# Generated at 2022-06-13 18:30:12.437591
# Unit test for function find_template
def test_find_template():
    """
    Test `find_template`.

    """
    assert find_template('./tests/test-repo-pre/') == './tests/test-repo-pre/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:30:22.000886
# Unit test for function find_template
def test_find_template():
    import tempfile
    
    repo_dir = tempfile.mkdtemp()
    cookiecutter_json_path = os.path.join(
        repo_dir, '{{cookiecutter.repo_name}}'
    )
    
    # Create a fake cookiecutter.json file
    with open(cookiecutter_json_path, 'wt') as fh:
        fh.write('{"repo_name": "test_project"}')
        
    assert find_template(repo_dir) == cookiecutter_json_path
    # Cleanup temp dir
    os.unlink(cookiecutter_json_path)
    os.removedirs(cookiecutter_json_path)

# Generated at 2022-06-13 18:30:26.811800
# Unit test for function find_template
def test_find_template():
    repo_dir = '/Users/audreyr/cookiecutter-pypackage.git'
    assert find_template(repo_dir) == '/Users/audreyr/cookiecutter-pypackage.git/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:30:31.125337
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'tests', 'fake-repo-tmpl')
    project_tmpl = find_template(repo_dir)
    expected_project_tmpl = os.path.join(repo_dir, 'fake_project_tmpl')
    assert project_tmpl == expected_project_tmpl


# Generated at 2022-06-13 18:30:36.624510
# Unit test for function find_template
def test_find_template():
    """Verify function find_template returns expected value."""
    assert find_template('/Users/audreyr/code/cookiecutter-pypackage') == '/Users/audreyr/code/cookiecutter-pypackage/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:30:40.467073
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.join(os.path.dirname(__file__), 'files', 'foobar-master')
    assert find_template(repo_dir) == os.path.join(repo_dir, '{{cookiecutter.repo_name}}')

# Generated at 2022-06-13 18:30:51.928238
# Unit test for function find_template
def test_find_template():
    """Verify that simple templates are identified."""
    logger.debug('Determining template with name {{cookiecutter.repo_name}}')
    assert find_template('templates/tests/fake-repo-tmpl') == 'templates/tests/fake-repo-tmpl/{{cookiecutter.repo_name}}'

    logger.debug('Determining template with name '
        '{{cookiecutter.repo_name}}-{{cookiecutter.py_module_name}}')
    assert find_template('templates/tests/fake-repo-tmpl-module') == 'templates/tests/fake-repo-tmpl-module/{{cookiecutter.repo_name}}-{{cookiecutter.py_module_name}}'



# Generated at 2022-06-13 18:31:02.912050
# Unit test for function find_template
def test_find_template():
    """Assert that find_template() returns the project template dir."""
    template_dir = 'tests/files/fake-repo-pre/'
    actual = find_template(template_dir)
    expected = 'tests/files/fake-repo-pre/fake-project-{{ cookiecutter.repo_name }}'
    assert actual == expected

# Generated at 2022-06-13 18:31:07.743416
# Unit test for function find_template
def test_find_template():
    find_template("https://github.com/titovanton/cookiecutter-npm.git")
    logging.error('the project template appears to be %s', find_template.__doc__)

# Generated at 2022-06-13 18:31:10.893124
# Unit test for function find_template
def test_find_template():
    repo_dir = '/home/whoever/projects/cookiecutter-pypackage'
    project_template = find_template(repo_dir)
    assert project_template == '/home/whoever/projects/cookiecutter-pypackage/{{cookiecutter.repo_name}}'



# Generated at 2022-06-13 18:31:16.246523
# Unit test for function find_template
def test_find_template():
    cwd = os.getcwd()
    repo_dir = os.path.join(cwd, 'tests/fake-repo-tmpl')
    project_template = find_template(repo_dir)
    assert 'fake-repo-tmpl/{{cookiecutter.repo_name}}' in project_template

# Generated at 2022-06-13 18:31:21.796731
# Unit test for function find_template
def test_find_template():
    test_dir = os.path.abspath(os.path.dirname(__file__))
    input_dir = os.path.join(test_dir, 'cheese-repo', 'cookiecutter-{{cookiecutter.cheese}}')
    assert find_template(test_dir) == input_dir

# Generated at 2022-06-13 18:31:29.946919
# Unit test for function find_template
def test_find_template():
    input_dir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..', 'test-repos')
    )
    template = find_template(input_dir)
    assert os.path.exists(template)
    assert template == os.path.abspath(
        os.path.join(input_dir, 'cookiecutter-demo')
    )

# Generated at 2022-06-13 18:31:30.765531
# Unit test for function find_template
def test_find_template():
    pass

# Generated at 2022-06-13 18:31:35.929233
# Unit test for function find_template
def test_find_template():
    """Verify that find_template() correctly finds a template given a path"""
    assert find_template('/tmp/cookiecutter-foobar/{{cookiecutter.repo_name}}') == '/tmp/cookiecutter-foobar/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:31:44.809859
# Unit test for function find_template
def test_find_template():
    """Verify a template can be found in a test repo."""
    import tempfile
    from ..utils import clone

    logger.debug('Creating a temp dir to test `find_template` with.')
    temp_dir = tempfile.mkdtemp()

    logger.debug(
        'Cloning the test repo into {}'.format(os.path.join(temp_dir, 'repo'))
    )
    clone('tests/test-repo', os.path.join(temp_dir, 'repo'))

    project_template = find_template(os.path.join(temp_dir, 'repo'))

    assert 'tests/test-repo/{{cookiecutter.repo_name}}' == project_template
    logger.debug('Deleting %s', temp_dir)

# Generated at 2022-06-13 18:31:50.089526
# Unit test for function find_template
def test_find_template():
    """Test the find_template function."""
    # Test cases
    # The template is not in the "repo_dir"
    # The template is in the "repo_dir"
    # The template is the "repo_dir"
    # The template has dependencies
    pass

# Generated at 2022-06-13 18:32:10.938471
# Unit test for function find_template
def test_find_template():
    working_dir = os.path.dirname(__file__)
    print(working_dir)
    myrepodir = os.path.join(working_dir, "myrepo")
    print(myrepodir)
    print(find_template(myrepodir))
    # TODO: add a test non-template repo (no cookiecutter), and check it raises
    # NonTemplatedInputDirException

if __name__ == '__main__':
    test_find_template()

# Generated at 2022-06-13 18:32:15.986200
# Unit test for function find_template
def test_find_template():
    """
    Test the find_template function and make sure it returns the correct directory
    """
    assert find_template('C:\\Users\\Christopher\\cookiecutter-master\\tests\\test-repo') == 'C:\\Users\\Christopher\\cookiecutter-master\\tests\\test-repo\\{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:32:17.573274
# Unit test for function find_template
def test_find_template():

    find_template("../tests/fake-repo-pre/")

    return True

# Generated at 2022-06-13 18:32:26.288632
# Unit test for function find_template
def test_find_template():
    # Given a non-templated repo_dir, find_template should raise an exception
    wrong_repo_dir = os.path.join(
        os.path.dirname(__file__), '../', 'tests/test-data/fake-repo'
    )
    # check that the exception is raised
    # TODO:: fix this test, it doesn't work on CircleCI
    # assert_raises(NonTemplatedInputDirException, find_template, wrong_repo_dir)

    # Given a templated repo_dir, find_template should find the template.
    repo_dir = os.path.join(
        os.path.dirname(__file__), '../', 'tests/test-data/fake-repo-tmpl'
    )
    # check that the path to the template is returned


# Generated at 2022-06-13 18:32:26.960073
# Unit test for function find_template
def test_find_template():
    pass

# Generated at 2022-06-13 18:32:32.677058
# Unit test for function find_template
def test_find_template():
    """Ensure that `find_template` finds what it should."""
    logger.debug('Running tests...')

    import shutil
    import tempfile

    project_template = '{{cookiecutter.repo_name}}'

    # Create a temporary directory to work in
    temp_dir = tempfile.mkdtemp()

    # Create a child directory of the temp directory
    repo_dir = os.path.join(temp_dir, 'cookiecutter-pypackage')
    os.mkdir(repo_dir)

    # Change to the new directory
    os.chdir(repo_dir)

    # Run find_template in the repo directory
    output = find_template(repo_dir)

    # Check that the project template was found
    assert temp_dir in output
    assert project_template in output

    shut

# Generated at 2022-06-13 18:32:34.725299
# Unit test for function find_template
def test_find_template():
	assert find_template('test_dir') == 'test_dir\/test_template'


# Generated at 2022-06-13 18:32:47.680231
# Unit test for function find_template
def test_find_template():
    """
    Run the test.
    """
    # pylint: disable=import-outside-toplevel
    import tempfile
    import shutil
    import os

    template_dir = tempfile.mkdtemp()
    logger.debug('Working in temporary directory %s', template_dir)
    template_dir_contents = [
        '{{cookiecutter.repo_name}}',
        'placeholder',
        '{{cookiecutter.repo_name}}-placeholder',
        '{{cookiecutter.repo_name}}-placeholder }}',
        '{cookiecutter.repo_name}}',
        'cookiecutter.repo_name}}',
        'placeholder {{cookiecutter.repo_name',
        'placeholder {{cookiecutter.repo_name}}}}',
    ]


# Generated at 2022-06-13 18:32:51.266685
# Unit test for function find_template
def test_find_template():
    template_path = find_template('/Users/tonyfast/Desktop/ProjectTemplate/')
    assert template_path == '/Users/tonyfast/Desktop/ProjectTemplate/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:32:52.244083
# Unit test for function find_template
def test_find_template():
    find_template('cookiecutter-pypackage')

# Generated at 2022-06-13 18:33:24.292566
# Unit test for function find_template
def test_find_template():
    """Unit testing function for find_template function."""
    import os

    # Create test directory
    TEST_DIR = './tests/test-dir'
    os.mkdir(TEST_DIR)
    os.mkdir(os.path.join(TEST_DIR, '{{cookiecutter.project_name}}'))

    # Test functions
    assert find_template(TEST_DIR) == \
        os.path.join(TEST_DIR, '{{cookiecutter.project_name}}')

# Generated at 2022-06-13 18:33:29.382434
# Unit test for function find_template
def test_find_template():
    cc_repo_path = os.path.join('tests', 'test-repos', 'py-library')
    cc_path = find_template(cc_repo_path)
    assert 'cookiecutter' in cc_path
    assert '{{' in cc_path
    assert '}}' in cc_path

# Generated at 2022-06-13 18:33:34.162273
# Unit test for function find_template
def test_find_template():
    """
    Test the find_template function.
    """
    repo_dir = "tests/test-repo-tmpl"
    project_template = find_template(repo_dir)

    assert project_template == "tests/test-repo-tmpl/{{cookiecutter.repo_name}}"

# Generated at 2022-06-13 18:33:37.615832
# Unit test for function find_template
def test_find_template():
    repo_dir = r'C:\python\cookiecutter'
    repo_dir_contents = ['{{cookiecutter.repo_name}}']
    assert find_template(repo_dir) == r'C:\python\cookiecutter\{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:33:39.627504
# Unit test for function find_template
def test_find_template():
    find_template('/Users/landonb/repos/cookiecutter-pypackage')

# Generated at 2022-06-13 18:33:48.714387
# Unit test for function find_template
def test_find_template():
    # Create tests/fake-repo-pre/{{cookiecutter.repo_name}}/ with contents.
    repo_dir = 'tests/fake-repo-pre/'
    logger.debug('Searching %s for the project template', repo_dir)
    assert find_template(repo_dir) == 'tests/fake-repo-pre/fake-repo/'

    # Create tests/fake-repo-post/fake-repo/ with contents.
    repo_dir = 'tests/fake-repo-post/'
    logger.debug('Searching %s for the project template', repo_dir)
    assert find_template(repo_dir) == 'tests/fake-repo-post/fake-repo/'

    # Create tests/fake-repo-no-templating/ with contents.
   

# Generated at 2022-06-13 18:33:53.032118
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                            'fake-repo')
    project_template = find_template(repo_dir)
    assert project_template == 'fake-repo/{{cookiecutter.repo_name}}', \
        'The project template has been found'

# Generated at 2022-06-13 18:33:56.283524
# Unit test for function find_template
def test_find_template():
    repo_dir=os.getcwd()
    print(find_template(repo_dir))

if __name__ == '__main__':
    test_find_template()

# Generated at 2022-06-13 18:34:02.448261
# Unit test for function find_template
def test_find_template():
    """Test function find_template."""
    assert find_template(
        'tests/test-repo/tests/fake-repo-tmpl/',
    ) == 'tests/test-repo/tests/fake-repo-tmpl/{{cookiecutter.repo_name}}/'



# Generated at 2022-06-13 18:34:10.856507
# Unit test for function find_template
def test_find_template():
    fixture_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "fixtures/cli")
    )
    repo_dir = os.path.join(fixture_path, 'find-template')

    repo_dir_contents = os.listdir(repo_dir)
    assert repo_dir_contents == ['new-project-template', '.travis.yml']

    project_template = find_template(repo_dir)
    assert project_template == os.path.join(repo_dir, 'new-project-template')

# Generated at 2022-06-13 18:35:08.239415
# Unit test for function find_template
def test_find_template():
    # Given
    repo_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
        'conf_templates',
        '{{cookiecutter.repo_name}}'
    )
    # When
    ret = find_template(repo_dir)

    # Then
    assert repo_dir == ret

# Generated at 2022-06-13 18:35:13.149536
# Unit test for function find_template
def test_find_template():
    """Determine which child directory of `repo_dir` is the project template.

    :param repo_dir: Local directory of newly cloned repo.
    :returns project_template: Relative path to project template.
    """
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
        return project_template


# Generated at 2022-06-13 18:35:19.866372
# Unit test for function find_template
def test_find_template():
    repo_dir = 'test_find_template'
    assert find_template(repo_dir) == 'test_find_template/{{cookiecutter.repo_name}}'
    assert not find_template('/test_find_template')

if __name__ == "__main__":
    test_find_template()

# Generated at 2022-06-13 18:35:21.296258
# Unit test for function find_template
def test_find_template():
    # TODO
    pass

# Generated at 2022-06-13 18:35:24.584048
# Unit test for function find_template
def test_find_template():
    """Verify find_template() returns the correct directory."""
    assert find_template('tests/fake-repo-pre/') == 'tests/fake-repo-pre/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:35:25.495592
# Unit test for function find_template
def test_find_template():
    pass



# Generated at 2022-06-13 18:35:32.654619
# Unit test for function find_template
def test_find_template():
    """Function to test finding the template in the repo"""
    base_path = os.path.normpath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    repo_path = os.path.join(base_path, 'tests', 'test-repo-pre')
    template_path = find_template(repo_path)
    assert template_path == os.path.join(repo_path, '{{cookiecutter.repo_name}}')


# Generated at 2022-06-13 18:35:38.938748
# Unit test for function find_template
def test_find_template():
    """Check that find_template does not modify an un-templated dir."""
    repo_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'fake-repo-pre-render'
    )
    assert find_template(repo_dir) == os.path.join(repo_dir, '{{cookiecutter.repo_name}}')

# Generated at 2022-06-13 18:35:42.635049
# Unit test for function find_template
def test_find_template():
    """Test that find_template returns the correct result."""
    repo_dir = '/home/todd/myrepo'
    project_template = find_template(repo_dir)
    assert project_template == '/home/todd/myrepo/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:35:48.289614
# Unit test for function find_template
def test_find_template():
    """Verify find_template() returns expected output."""
    from .compat import patch
    from .compat import mock

    m = mock.mock_open(read_data='foo')
    with patch('codecs.open', m, create=True):
        cwd = os.getcwd()
        repo_dir = os.path.join(cwd, 'tests/fake-repo-tmpl')
        assert find_template(repo_dir) == os.path.join(repo_dir, 'cookiecutter-pypackage')
        m.assert_called_once_with(os.path.join(repo_dir, 'cookiecutter-pypackage'), encoding='utf-8')