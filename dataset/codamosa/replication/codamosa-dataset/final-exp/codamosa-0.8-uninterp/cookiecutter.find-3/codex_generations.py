

# Generated at 2022-06-13 18:27:40.661411
# Unit test for function find_template
def test_find_template():
    """Test find_template(repo_dir)"""
    repo_dir = os.getenv('TESTS_DIR', '/tmp/cookiecutter-test/')
    repo_dir = os.path.join(repo_dir, 'tests/fixtures/fake-repo-pre/')
    assert find_template(repo_dir) == (
        '%s{{cookiecutter.repo_name}}/' % repo_dir
    )

# Generated at 2022-06-13 18:27:45.526903
# Unit test for function find_template
def test_find_template():
    # Given
    expected = '../tests/input/{{cookiecutter.repo_name}}'
    actual = find_template('../tests/input')

    # Then
    assert expected == actual



# Generated at 2022-06-13 18:27:49.187935
# Unit test for function find_template
def test_find_template():
    """Finding the template relative path."""
    this_dir = os.path.dirname(os.path.abspath(__file__))
    repo_dir = os.path.join(this_dir, 'fake-repo')
    project_template = os.path.join(repo_dir, 'fake-project-{{ cookiecutter.repo_name }}')
    assert find_template(repo_dir) == project_template


# Generated at 2022-06-13 18:27:50.459453
# Unit test for function find_template
def test_find_template():
    #TODO
    return

# Generated at 2022-06-13 18:27:59.795457
# Unit test for function find_template
def test_find_template():
    """Verify function find_template"""
    # No template found should raise exception
    os.chdir(os.path.normpath('tests/fake-repo/input'))
    test_repo = os.path.abspath(os.curdir)
    assert os.path.isdir(test_repo)
    try:
        find_template(test_repo)
    except NonTemplatedInputDirException:
        logger.debug('find_template:%s', 'No template found!')
    # Template found in repo
    os.chdir(os.path.normpath('../fake-repo-templated/input'))
    test_repo = os.path.abspath(os.curdir)
    assert os.path.isdir(test_repo)
    assert find_template

# Generated at 2022-06-13 18:28:02.231505
# Unit test for function find_template
def test_find_template():
    """
    decide upon a child directory that is the project template
    """
    # TODO: write unit tests
    

# Generated at 2022-06-13 18:28:05.395890
# Unit test for function find_template
def test_find_template():
    assert find_template('./tests/test-find-template') == './tests/test-find-template/cookiecutter-{{cookiecutter.repo_name}}'



# Generated at 2022-06-13 18:28:11.044824
# Unit test for function find_template
def test_find_template():
    from cookiecutter.repository import determine_repo_dir
    repo_dir = 'tests/fake-repo-pre/'
    template_dir = 'fake-project'
    repo_dir = determine_repo_dir(repo_dir)
    assert find_template(repo_dir) == os.path.join(repo_dir, template_dir)

# Generated at 2022-06-13 18:28:16.183887
# Unit test for function find_template
def test_find_template():
    """Test that find_template returns the correct results."""
    # Set up
    repo_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        '..', 'tests', 'fake-repo', 'input', 'fake-repo'
    )

    # Run & check
    project_template = find_template(repo_dir)
    assert project_template == os.path.join(
        repo_dir,
        '{{cookiecutter.repo_name}}',
    )



# Generated at 2022-06-13 18:28:23.044689
# Unit test for function find_template
def test_find_template():
    repo_dir = '/Users/mattdum/cookiecutters_playground/cookiecutter-pypackage'
    #print find_template(repo_dir)
    assert find_template(repo_dir) == '/Users/mattdum/cookiecutters_playground/cookiecutter-pypackage/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:28:28.637138
# Unit test for function find_template
def test_find_template():
    """Test find_template()"""
    template_path = find_template('test_repo')
    assert os.path.basename(template_path) == '{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:28:38.846647
# Unit test for function find_template
def test_find_template():
    from cookiecutter.main import cookiecutter
    from cookiecutter.prompt import read_user_yes_no

    directory = os.path.expanduser('~/fake-repo-pre')
    cookiecutter(directory, extra_context={'project_name': 'frozz-pop'})

    repo_dir = os.path.join(directory, 'frozz-pop')
    template = find_template(repo_dir)
    assert os.path.isdir(template)
    assert 'fake-repo' in os.path.basename(template)
    assert 'frozz-pop' in os.path.basename(template)

    # Clean up
    answer = read_user_yes_no('Would you like to delete the generated project? [y/N] ')

# Generated at 2022-06-13 18:28:41.052491
# Unit test for function find_template
def test_find_template():
    mockdir = 'tests/test-find-template'
    expected_result = 'tests/test-find-template/{{cookiecutter.repo_name}}'
    assert(find_template(mockdir) == expected_result)

# Generated at 2022-06-13 18:28:41.696945
# Unit test for function find_template
def test_find_template():
    pass

# Generated at 2022-06-13 18:28:43.128685
# Unit test for function find_template
def test_find_template():
    """Test the find_template function."""
    find_template('tests/fake-repo-tmpl/')

# Generated at 2022-06-13 18:28:53.946381
# Unit test for function find_template
def test_find_template():
    """Test determining which directory is to be considered the project template."""
    import shutil
    import tempfile
    import unittest

    from cookiecutter import exceptions

    class TestFindTemplate(unittest.TestCase):
        def setUp(self):
            self.repo_dir = tempfile.mkdtemp()

        def tearDown(self):
            shutil.rmtree(self.repo_dir)

        def test_standard(self):
            """Test typical example"""

# Generated at 2022-06-13 18:29:00.836725
# Unit test for function find_template
def test_find_template():
    """Verify Cookiecutter can find templates."""
    tests_dir = os.path.dirname(os.path.abspath(__file__))
    template_dir = os.path.join(tests_dir, 'fake-repo-pre/')
    project_template = find_template(template_dir)
    assert os.path.isdir(template_dir)
    assert os.path.isdir(project_template)
    assert 'fake-repo-pre' in project_template
    assert not os.path.exists(os.path.join(template_dir, '{{cookiecutter.repo_name}}'))
    assert os.path.exists(os.path.join(template_dir, '{{cookiecutter.repo_name}}-post'))

# Generated at 2022-06-13 18:29:02.696851
# Unit test for function find_template
def test_find_template():
    """Verify find_template()"""
    pass

# Generated at 2022-06-13 18:29:11.784687
# Unit test for function find_template
def test_find_template():
    # Mock up repo_dir
    repo_dir = '/Users/audreyr/cookiecutters/cookiecutter-pypackage'
    # Make sure the project template directory is there
    assert os.path.isdir(os.path.join(repo_dir, 'cookiecutter-pypackage'))
    # Call find_template() and assert that it returns the template directory
    assert (
        find_template(repo_dir) ==
        os.path.join(repo_dir, 'cookiecutter-pypackage')
    )

# Generated at 2022-06-13 18:29:12.510580
# Unit test for function find_template
def test_find_template():
    pass

# Generated at 2022-06-13 18:29:19.009872
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.join(os.path.dirname(__file__), "test-repo")
    template_dir = find_template(repo_dir)
    assert template_dir.endswith("cookiecutter-test-repo/{{cookiecutter.repo_name}}")

# Generated at 2022-06-13 18:29:22.688720
# Unit test for function find_template
def test_find_template():

    template = find_template('/home/user/projects/cookiecutter-pypackage')
    assert template == '/home/user/projects/cookiecutter-pypackage/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:29:28.233984
# Unit test for function find_template
def test_find_template():
    # get the path to tests/fake-repo
    test_dir = os.path.dirname(os.path.abspath(__file__))
    repo_dir = os.path.join(test_dir, 'fake-repo')
    found_template = find_template(repo_dir)
    expected_template = os.path.join(repo_dir, 'cookiecutter-pypackage')

    assert found_template == expected_template

# Generated at 2022-06-13 18:29:30.947197
# Unit test for function find_template
def test_find_template():
    assert find_template('/home/audreyr/') == '/home/audreyr/cookiecutter-{{cookiecutter.project_name'

# Generated at 2022-06-13 18:29:31.575225
# Unit test for function find_template
def test_find_template():
    pass

# Generated at 2022-06-13 18:29:40.898625
# Unit test for function find_template
def test_find_template():
    """
    Test find_template function.
    """
    from cookiecutter import utils
    from cookiecutter.exceptions import NonTemplatedInputDirException

    cur_dir = os.path.realpath(os.path.curdir)
    repo_dir = os.path.join(cur_dir, 'tests', 'test-repo-pre')
    template_dir = os.path.join('{{cookiecutter.repo_name}}', '{{cookiecutter.repo_name}}')
    assert repo_dir == os.path.abspath(utils.find_template(repo_dir))
    assert template_dir == os.path.abspath(utils.find_template(repo_dir))

    repo_dir = os.path.join(cur_dir, 'tests')

# Generated at 2022-06-13 18:29:46.775561
# Unit test for function find_template
def test_find_template():
    """Verify non-debug log message when debug is disabled."""

    # Check enable debug
    n_handlers = len(logger.handlers)
    logger.debug('Testing find_template')
    assert len(logger.handlers) == n_handlers, 'Debug Logger added handler'



# Generated at 2022-06-13 18:29:51.533076
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.join(os.path.dirname(__file__), 'fake-repo')
    project_template = find_template(repo_dir)
    assert project_template == os.path.join(repo_dir, 'fake-project')

# Generated at 2022-06-13 18:29:53.583709
# Unit test for function find_template

# Generated at 2022-06-13 18:29:58.096516
# Unit test for function find_template
def test_find_template():
    repo_dir = 'tests/test-repo-pre/{{cookiecutter.repo_name}}'
    assert find_template(repo_dir) == \
        os.path.abspath('tests/test-repo-pre/{{cookiecutter.repo_name}}/{{cookiecutter.project_name}}')


# Generated at 2022-06-13 18:30:06.193313
# Unit test for function find_template
def test_find_template():
    """Verify that the find_template() function works"""
    repo_dir = '.'
    expected = os.path.abspath(os.path.join(repo_dir, '{{cookiecutter.project_slug}}'))
    actual = find_template(repo_dir)
    assert expected == actual

# Generated at 2022-06-13 18:30:14.777753
# Unit test for function find_template
def test_find_template():
    import tempfile
    import shutil

    template_dir, project_dir = tempfile.mkdtemp(), tempfile.mkdtemp()

    os.makedirs(os.path.join(template_dir, 'my_cool_project'))
    shutil.copytree(template_dir, project_dir)

    assert find_template(project_dir) == os.path.join(project_dir, 'my_cool_project')

    shutil.rmtree(template_dir)
    shutil.rmtree(project_dir)


# Generated at 2022-06-13 18:30:19.997575
# Unit test for function find_template
def test_find_template():
    assert find_template('./tests/test-repo-pre/') == './tests/test-repo-pre/{{cookiecutter.repo_name}}'
    try:
        assert find_template('./tests/fake-repo/')
    except NonTemplatedInputDirException:
        pass
    else:
        assert False

# Generated at 2022-06-13 18:30:22.496001
# Unit test for function find_template
def test_find_template():
    """Tests ``find_template`` function which finds the Cookiecutter template.
    """
    assert find_template('tests/test-find-template') \
        == 'tests/test-find-template/cookiecutter-pypackage'

# Generated at 2022-06-13 18:30:23.649246
# Unit test for function find_template
def test_find_template():
    assert find_template('cookiecutter-pypackage')

# Generated at 2022-06-13 18:30:30.993516
# Unit test for function find_template
def test_find_template():
    assert find_template('tests/fake-repo-pre/') == 'tests/fake-repo-pre/{{cookiecutter.repo_name}}/'
    assert find_template('tests/fake-repo-post/') == 'tests/fake-repo-post/my-fake-cookiecutter-repo/'
    assert find_template('tests/fake-repo-pre/tests/fake-repo-pre/cookiecutter-pypackage/') == 'tests/fake-repo-pre/tests/fake-repo-pre/cookiecutter-pypackage/{{cookiecutter.repo_name}}/'



# Generated at 2022-06-13 18:30:35.955071
# Unit test for function find_template
def test_find_template():
    repo_dir = '/home/audreyr/cookiecutter-pypackage'
    project_template = find_template(repo_dir)
    assert project_template == '/home/audreyr/cookiecutter-pypackage/cookiecutter-pypackage'

# Generated at 2022-06-13 18:30:41.866742
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            'test-find-template')
    template = find_template(repo_dir)
    expected = os.path.join(repo_dir, '{{cookiecutter.repo_name}}-master')

    assert template == expected

# Generated at 2022-06-13 18:30:46.794978
# Unit test for function find_template
def test_find_template():
    """Unit test for function find_template"""
    assert find_template(os.path.join('tests', 'fixtures', 'fake-repo-pre')) == os.path.join('tests', 'fixtures', 'fake-repo-pre', '{{cookiecutter.repo_name}}')



# Generated at 2022-06-13 18:31:00.172412
# Unit test for function find_template
def test_find_template():
    from unittest import TestCase
    from tempfile import mkdtemp
    from cookiecutter import utils

    class TestFindTemplate(TestCase):

        def setUp(self):
            self.test_dir = mkdtemp()
            self.test_dir_contents = [
                'cookiecutter-foobar'
            ]
            self.test_dir_contents_abs = [
                os.path.join(self.test_dir, item)
                for item in self.test_dir_contents
            ]
            for item in self.test_dir_contents_abs:
                os.mkdir(item)

        def tearDown(self):
            utils.rmtree(self.test_dir)


# Generated at 2022-06-13 18:31:10.168524
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.join('tests', 'test-find-template')
    project_template = find_template(repo_dir)

    expected_path = os.path.join(repo_dir, '{{cookiecutter.repo_name}}')

    assert project_template == expected_path

# Generated at 2022-06-13 18:31:16.204447
# Unit test for function find_template
def test_find_template():
    """ Test :py:find_template """
    repo_dir = "/my/repo/dir"
    test_dirs = {
        "other": ("/my/repo/dir/other"),
        "other/non-template": ("/my/repo/dir/other/non-template"),
        "project_dir/{{cookiecutter.reponame}}": ("/my/repo/dir/project_dir/{{cookiecutter.reponame}}"),
        "project_dir/reponame": ("/my/repo/dir/project_dir/reponame"),
        "project_dir/reponame/{{cookiecutter.reponame}}": ("/my/repo/dir/project_dir/reponame/{{cookiecutter.reponame}}"),
        }


# Generated at 2022-06-13 18:31:20.713535
# Unit test for function find_template
def test_find_template():
    """Test function find_template"""
    cwd = os.getcwd()
    assert find_template(cwd) is None
    os.makedirs('temp')

# Generated at 2022-06-13 18:31:27.055243
# Unit test for function find_template
def test_find_template():
    """Verify the `find_template` function returns the correct project template.

    Assert that:
    - the function returns the correct relative path
    - None is returned if the template directory is not found
    """
    import tempfile
    import unittest

    from cookiecutter.exceptions import NonTemplatedInputDirException

    class TestFindTemplate(unittest.TestCase):

        def setUp(self):
            self.temporary_directory = tempfile.mkdtemp()
            self.temporary_directory2 = tempfile.mkdtemp()
            self.template_directory = os.path.join(self.temporary_directory, 'cookiecutter-foobar')
            os.makedirs(self.template_directory)

# Generated at 2022-06-13 18:31:30.806082
# Unit test for function find_template
def test_find_template():
    """A unit test for function find_template"""
    assert find_template("unit_test_content") == "unit_test_content"

test_find_template()

# Generated at 2022-06-13 18:31:40.064405
# Unit test for function find_template
def test_find_template():
    """ Test find_template function """
    assert find_template(os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        '..', 'tests', 'fake-repo-pre'
    )) == os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        '..', 'tests', 'fake-repo-pre', '{{cookiecutter.repo_name}}'
    )

# Generated at 2022-06-13 18:31:46.329515
# Unit test for function find_template
def test_find_template():

    import tempfile

    temp_dir = tempfile.mkdtemp()

    INVALID_TEMPLATE_DIR = os.path.join(temp_dir, 'no-cookiecutter-in-template')
    os.mkdir(INVALID_TEMPLATE_DIR)


# Generated at 2022-06-13 18:31:59.039612
# Unit test for function find_template
def test_find_template():
    """Verify expected folder is returned."""
    import os
    # Folder containing the expected template
    fname = os.path.join('tests', 'templates', 'default')
    # Folder containing the expected template (compressed archive)
    fname_tgz = os.path.realpath(os.path.join('tests', 'templates', 'default.tgz'))
    # Folder containing the expected template and one extra
    fname_extra = os.path.join('tests', 'templates', 'extra-template')
    # Folder containing the expected template and one extra (compressed archive)
    fname_extra_tgz = os.path.realpath(os.path.join('tests', 'templates', 'extra-template.tgz'))


# Generated at 2022-06-13 18:32:07.090582
# Unit test for function find_template
def test_find_template():
    import shutil
    from cookiecutter.compat import TemporaryDirectory
    from cookiecutter.main import get_user_config

    user_config = get_user_config()
    temp_dir = TemporaryDirectory()


# Generated at 2022-06-13 18:32:10.460374
# Unit test for function find_template
def test_find_template():
    """Test if the function can find the project template."""
    repo_dir = 'tests'
    assert find_template(repo_dir) == 'tests\\cookiecutter-pypackage'

# Generated at 2022-06-13 18:32:34.725897
# Unit test for function find_template
def test_find_template():
    """
    Test find_template function.

    Test function looks for 'cookiecutter' in repo_dir
    and if it finds it will assign it to project_template.
    The path is created by joining repo_dir with project_template.
    """
    mock_repo_dir = ('/home/user/'
                     'cookiecutter-pypackage/'
                     '{{cookiecutter.project_name}}')
    mock_repo_dir_contents = os.listdir(mock_repo_dir)
    mock_project_name = 'cookiecutter'

    mock_project_template = None
    for item in mock_repo_dir_contents:
        if mock_project_name in item:
            mock_project_template = item
            break


# Generated at 2022-06-13 18:32:36.060860
# Unit test for function find_template
def test_find_template():
    """Unit test for function find_template."""
    pass

# Generated at 2022-06-13 18:32:43.020382
# Unit test for function find_template
def test_find_template():
    """
    """
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    GOOD_REPO = os.path.join(ROOT_DIR, 'good-repo')
    BAD_REPO = os.path.join(ROOT_DIR, 'bad-repo')
    EXPECTED_TEMPLATE = os.path.join(ROOT_DIR, 'good-repo', '{{cookiecutter.repo_name}}')

    print(find_template(GOOD_REPO))
    assert find_template(GOOD_REPO) == EXPECTED_TEMPLATE
    find_template(BAD_REPO)

# Generated at 2022-06-13 18:32:45.729463
# Unit test for function find_template
def test_find_template():
    pass


# TODO: add unit test for this function

# Generated at 2022-06-13 18:32:55.197468
# Unit test for function find_template
def test_find_template():
    dir_with_template = 'tests/test-find-template/{{cookiecutter.directory_name}}/{{cookiecutter.directory_name}}'
    dir_without_template = 'tests/test-find-template/{{cookiecutter.directory_name}}/{{cookiecutter.directory_name'
    dir_without_template2 = 'tests/test-find-template/{{cookiecutter.directory_name}}/cookiecutter.directory_name}}'
    dir_without_template3 = 'tests/test-find-template/{{cookiecutter.directory_name}}/cookiecutter.directory_name'

    assert find_template(dir_without_template) == \
        'tests/test-find-template/{{cookiecutter.directory_name}}/{{cookiecutter.directory_name}}'

# Generated at 2022-06-13 18:33:00.467602
# Unit test for function find_template
def test_find_template():
    # Test project template found
    repo_dir = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        'test_find_template',
        'expected_project_template'
    )
    project_template = os.path.join(repo_dir, 'my-{{cookiecutter.repo_name}}-template')

    assert find_template(repo_dir) == project_template

    # Test project template not found
    repo_dir = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        'test_find_template',
        'no_project_template'
    )


# Generated at 2022-06-13 18:33:03.643839
# Unit test for function find_template
def test_find_template():
    repo_dir = "/home/user/adfasdfasd"
    project_template = find_template(repo_dir)

test_find_template()

# Generated at 2022-06-13 18:33:13.479238
# Unit test for function find_template
def test_find_template():
    """Test function find_template."""
    from test_cookiecutter import find_project_template, project_dir

    repo_dir = os.path.join(os.path.dirname(__file__), 'tests/fake-repo-tmpl')
    template = find_template(repo_dir)
    assert template == find_project_template(repo_dir)

    repo_dir = os.path.join(os.path.dirname(__file__), project_dir)
    template = find_template(repo_dir)
    assert template == find_project_template(repo_dir)

# Generated at 2022-06-13 18:33:24.234096
# Unit test for function find_template
def test_find_template():
    this_dir = os.path.dirname(os.path.abspath(__file__))
    repo_dir = os.path.join(this_dir, '..', 'tests', 'fake-repo-tmpl')
    assert find_template(repo_dir) == os.path.join(repo_dir, '{{cookiecutter.repo_name}}')

    repo_dir = os.path.join(this_dir, '..', 'tests', 'fake-repo-no-tmpl')
    try:
        find_template(repo_dir)
    except NonTemplatedInputDirException:
        assert True

# Generated at 2022-06-13 18:33:35.064305
# Unit test for function find_template
def test_find_template():
    """Verify the project template is found correctly."""
    import shutil
    import tempfile

    repo_dir = os.path.join('tests', 'fake-repo-tmpl')
    temp_dir = tempfile.mkdtemp()

    try:
        shutil.copytree(repo_dir, os.path.join(temp_dir, 'fake-repo-tmpl'))
        repo_dir = os.path.join(temp_dir, 'fake-repo-tmpl')
        project_template = find_template(repo_dir)
    finally:
        shutil.rmtree(temp_dir)

    assert project_template == os.path.join(repo_dir, '{{cookiecutter.repo_name}}')

# Generated at 2022-06-13 18:34:05.495892
# Unit test for function find_template
def test_find_template():
    assert find_template('/home/vagrant/cookiecutter') == '/home/vagrant/cookiecutter/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:34:10.080875
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.join(os.path.dirname(__file__), '..', 'tests', 'fake-repo-tmpl')
    expected_template = os.path.join(repo_dir, '{{cookiecutter.repo_name}}')
    assert find_template(repo_dir) == expected_template

# Generated at 2022-06-13 18:34:13.021263
# Unit test for function find_template
def test_find_template():
    from cookiecutter.tests.test_utils import make_repo
    project_dir = make_repo('tests/files/cookiecutter-custom-format', 'project_template')
    project_template = find_template(project_dir)
    assert os.path.basename(project_template) == 'project_template'

# Generated at 2022-06-13 18:34:22.306843
# Unit test for function find_template
def test_find_template():
    from cookiecutter.exceptions import NonTemplatedInputDirException
    from tempfile import mkdtemp
    from shutil import rmtree

    project_temp = mkdtemp(prefix='cookiecutter-')

# Generated at 2022-06-13 18:34:30.449331
# Unit test for function find_template
def test_find_template():
    """Test that the cookiecutter template has been correctly found."""
    from cookiecutter.main import cookiecutter

    # Create a test cookiecutter template
    cookiecutter(
        'tests/test-data/',
        extra_context={'full_name': 'Test Author Name', 'email': 'author@example.com'}
    )

    repo_dir = 'tests/test-data/{{cookiecutter.full_name}}'
    assert find_template(repo_dir).endswith('tests/test-data/{{cookiecutter.full_name}}/cookiecutter/{{cookiecutter.full_name}}')

    # Remove test cookiecutter template
    import shutil
    shutil.rmtree(repo_dir, ignore_errors=True)

# Generated at 2022-06-13 18:34:36.258023
# Unit test for function find_template
def test_find_template():
    root_dir = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), '..')
    repo_dir = os.path.join(root_dir, 'tests/test-repo-pre/')
    project_template = os.path.join(repo_dir, '{{cookiecutter.repo_name}}')
    assert find_template(repo_dir) == project_template

# Generated at 2022-06-13 18:34:44.843796
# Unit test for function find_template
def test_find_template():
    """Unit test for function find_template."""
    # Test when `repo_dir` contains project template with templating
    repo_dir_contents = ['fake_file', 'fake_dir', 'fake_project_template{{}}']
    current_dir = os.path.abspath('.')
    os.listdir = lambda p: repo_dir_contents
    template = find_template(current_dir)
    assert template == os.path.join(current_dir, repo_dir_contents[-1])
    repo_dir_contents = ['fake_file', 'fake_dir', 'fake_project_template{{}}']

    # Test when `repo_dir` contains project template with no templating
    repo_dir_contents = ['fake_file', 'fake_dir', 'fake_project_template']

# Generated at 2022-06-13 18:34:49.240461
# Unit test for function find_template
def test_find_template():
    input_dir = '/tmp/cookiecutter-django/tests/files'
    expected = '/tmp/cookiecutter-django/tests/files/{{ cookiecutter.repo_name }}'
    actual = find_template(input_dir)
    assert actual == expected

# Generated at 2022-06-13 18:34:53.085588
# Unit test for function find_template
def test_find_template():
    test_dir = '/Users/audreyr/Documents/GitHub/cookiecutter-pypackage/tests/test-find-template/'
    test_temp = 'cookiecutter-pypackage'

    assert find_template(test_dir) == test_dir + test_temp

# Generated at 2022-06-13 18:34:56.568808
# Unit test for function find_template
def test_find_template():
    """
    Tests for find_template
    """
    # Find templates in current directory
    cwd = os.getcwd()
    project_template = find_template(cwd)
    # If a file is found, it will be the current working directory
    assert project_template == cwd, "Template not found in current directory."

# Generated at 2022-06-13 18:35:58.965244
# Unit test for function find_template
def test_find_template():
    import shutil
    import tempfile
    from cookiecutter.utils import rmtree

    tmpdir = tempfile.mkdtemp()
    testdir = os.path.join(tmpdir, 'testdir')
    os.mkdir(testdir)

    template_dir = os.path.join(testdir, 'my-repo-project')
    os.mkdir(template_dir)

    template = find_template(testdir)
    assert template == template_dir

    rmtree(tmpdir)



# Generated at 2022-06-13 18:36:06.664532
# Unit test for function find_template
def test_find_template():
    """Test that if there is a cookiecutter template in the repo, it is returned
    as the project template.
    """

    from cookiecutter import utils
    from cookiecutter import exceptions
    import os

    ROOT_DIR = os.path.abspath(os.path.dirname(os.getcwd()))
    repo_dir = os.path.join(ROOT_DIR, 'tests/test-repo/fake-repo-tmpl')
    result = utils.find_template(repo_dir)
    assert result == os.path.join(repo_dir, 'fake-project-tmpl')


# Generated at 2022-06-13 18:36:12.806848
# Unit test for function find_template
def test_find_template():
    template_dir = '/home/user/myproject'
    os.makedirs(template_dir)
    os.chdir(template_dir)
    open('cookiecutter.json', 'a').close()
    assert find_template(template_dir) == '/home/user/myproject/cookiecutter.json'

# Generated at 2022-06-13 18:36:17.152608
# Unit test for function find_template
def test_find_template():
    repo_dir = '/home/vagrant/cookiecutter-django/'
    project_template = find_template(repo_dir)
    assert project_template == '/home/vagrant/cookiecutter-django/{{cookiecutter.repo_name}}'



# Generated at 2022-06-13 18:36:25.901653
# Unit test for function find_template
def test_find_template():
    """Verify the correct template is found."""
    import tempfile
    import shutil

    # We will create a temporary directory
    temp_dir = tempfile.mkdtemp()

    # Within this temporary directory create a child directory
    # with the name of the template
    child_dir_name = '{{cookiecutter.project_name}}'
    child_dir = os.path.join(temp_dir, child_dir_name)
    os.mkdir(child_dir)

    template_dir = find_template(temp_dir)

    assert template_dir == child_dir
    shutil.rmtree(temp_dir)

# Generated at 2022-06-13 18:36:36.931909
# Unit test for function find_template
def test_find_template():
    """
    Tests for the find_template function
    """
    # Create the test template
    template_dir = tempfile.mkdtemp()
    open(os.path.join(template_dir, 'test.txt'), 'w')
    open(os.path.join(template_dir, 'test{{cookiecutter.test}}test.txt'), 'w')

    # Test that the function returns the correct file
    template = find_template(template_dir)
    expected = os.path.join(template_dir, 'test{{cookiecutter.test}}test.txt')
    assert template == expected

    # Test that it raises a NonTemplatedInputDirException
    shutil.rmtree(template_dir)
    template_dir = tempfile.mkdtemp()

# Generated at 2022-06-13 18:36:48.974945
# Unit test for function find_template
def test_find_template():
    """Verify correct behaviour of find_template function."""
    import shutil
    import tempfile

    temp_dir = tempfile.mkdtemp()

# Generated at 2022-06-13 18:37:00.135816
# Unit test for function find_template
def test_find_template():
    import tempfile
    repo_dir = tempfile.mkdtemp()
    fh, path = tempfile.mkstemp(dir=repo_dir)
    dirpath = path + '.d'
    os.mkdir(dirpath)
    fh, path = tempfile.mkstemp(dir=dirpath)
    dirpath2 = path + '.d'
    os.mkdir(dirpath2)
    fh, path = tempfile.mkstemp(dir=dirpath2)
    fh, path = tempfile.mkstemp(dir=dirpath2)
    fh, path = tempfile.mkstemp(dir=dirpath2)
    fh, path = tempfile.mkstemp(dir=dirpath2)
    fh, path = tempfile.mkstemp(dir=dirpath2)

# Generated at 2022-06-13 18:37:05.040594
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.abspath('./tests/fake-repo-tmpl/')
    exp_tmpl_path = os.path.join(repo_dir, 'fake-project-tmpl')
    tmpl_path = find_template(repo_dir)
    assert tmpl_path == exp_tmpl_path

# Generated at 2022-06-13 18:37:07.500014
# Unit test for function find_template
def test_find_template():
    """Unit test for :func:`find_template`."""
    from cookiecutter.tests.test_find import template_dir
    assert find_template(template_dir) == os.path.join(
        template_dir, '{{cookiecutter.repo_name}}'
    )