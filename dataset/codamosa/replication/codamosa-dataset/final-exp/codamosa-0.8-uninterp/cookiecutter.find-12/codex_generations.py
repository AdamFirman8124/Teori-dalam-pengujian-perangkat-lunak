

# Generated at 2022-06-13 18:27:47.163093
# Unit test for function find_template
def test_find_template():
    from cookiecutter import repo
    from cookiecutter import utils
    import os

    repo_dir = repo.clone('https://github.com/audreyr/cookiecutter-pypackage.git')

    project_template = utils.find_template(repo_dir)

    repo_dir_contents = os.listdir(repo_dir)
    assert project_template in repo_dir_contents
    assert '{{' in project_template
    assert '}}' in project_template

# Generated at 2022-06-13 18:27:53.593968
# Unit test for function find_template
def test_find_template():
    """
    Make sure that find_template() works as expected
    """
    assert find_template('/home/audreyr/cookiecutter-pypackage') == '/home/audreyr/cookiecutter-pypackage/{{cookiecutter.repo_name}}'


# Generated at 2022-06-13 18:27:59.650691
# Unit test for function find_template
def test_find_template():
    """Run py.test for find_template function."""
    test_result_contents = 'cookiecutter-pypackage'
    repo_dir = './tests/files/fake-repo'
    result = find_template(repo_dir)
    assert test_result_contents in result

# Generated at 2022-06-13 18:28:01.574656
# Unit test for function find_template
def test_find_template():
    repo_dir = None
    assert find_template(repo_dir) is None

# Generated at 2022-06-13 18:28:09.821918
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.join(
        os.getcwd(),
        'tests',
        'test-repo-pre/'
    )
    project_template = find_template(repo_dir)

    expected_project_template = os.path.join(
        os.getcwd(),
        'tests',
        'test-repo-pre/{{cookiecutter.repo_name}}/'
    )
    assert project_template == expected_project_template

# Generated at 2022-06-13 18:28:17.055493
# Unit test for function find_template
def test_find_template():
    """Expect to get a path to project_template"""
    import tempfile
    import shutil

    tmp_dir = tempfile.mkdtemp()
    input_dir = os.path.join(tmp_dir, 'test-repo')
    os.mkdir(input_dir)
    os.mkdir(os.path.join(input_dir, 'test-cookiecutter-master'))
    os.mkdir(os.path.join(input_dir, 'test-cookiecutter{{cookiecutter.example_variable}}'))

    output = find_template(input_dir)

    assert output == os.path.join(input_dir, 'test-cookiecutter{{cookiecutter.example_variable}}'), "Output should match expected"

    shutil.rmtree(tmp_dir)



# Generated at 2022-06-13 18:28:19.790107
# Unit test for function find_template

# Generated at 2022-06-13 18:28:30.128163
# Unit test for function find_template
def test_find_template():
    # test when there is a template
    test_template = 'A-cookiecutter-template'
    test_repo = ['some_other_file', test_template, 'third_file']
    test_list = os.listdir
    os.listdir = lambda path: test_repo
    template = find_template(None)
    assert template == test_template
    # test when there is not a template
    test_repo = ['some_other_file', 'third_file']
    os.listdir = lambda path: test_repo
    raises(NonTemplatedInputDirException, find_template, None)
    # reset functions
    os.listdir = test_list

# Generated at 2022-06-13 18:28:39.622335
# Unit test for function find_template
def test_find_template():
    """Verify CookiecutterDjango's repository is properly discovered."""
    import os
    import tempfile

    from cookiecutter import utils
    from cookiecutter.exceptions import NonTemplatedInputDirException

    temp_dir = tempfile.mkdtemp()

    try:
        utils.make_sure_path_exists(temp_dir)
        utils.rmtree(temp_dir)

        cookiecutter_dir = os.path.join(
            temp_dir,
            'cookiecutter-django',
            '{{cookiecutter.repo_name}}'
        )
        utils.make_sure_path_exists(cookiecutter_dir)
        template = find_template(temp_dir)
        assert template == cookiecutter_dir

    finally:
        utils.r

# Generated at 2022-06-13 18:28:45.076716
# Unit test for function find_template
def test_find_template():
    """Test find_template."""
    test_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'fake-repo-pre-gen'
    )
    expected_project_template = os.path.join(
        test_dir,
        '{{ cookiecutter.repo_name }}'
    )
    project_template = find_template(test_dir)
    assert expected_project_template == project_template

# Generated at 2022-06-13 18:28:51.135056
# Unit test for function find_template
def test_find_template():
    repo_dir = "./tests/test-data/non-repo/cookiecutter-simple-master"
    assert find_template(repo_dir) == "./tests/test-data/non-repo/cookiecutter-simple-master/{{cookiecutter.repo_name}}"

# Generated at 2022-06-13 18:28:56.261604
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        '../tests/test-data/repo-tmpl'
    )
    project_template = find_template(repo_dir)
    assert project_template == "{{cookiecutter.repo_name}}"

# Generated at 2022-06-13 18:29:04.440498
# Unit test for function find_template
def test_find_template():
    import tempfile
    import shutil
    import re

    cookiecutter_regex = re.compile('(?<=cookiecutter)[^/umlaut]+')

    def create_temp_dir():
        return tempfile.mkdtemp()

    def create_temp_file(dir, filename, contents=''):
        open(os.path.join(dir, filename), 'a').close()

    def is_cookiecutter(path):
        return cookiecutter_regex.search(path)

    # Create a temporary directory
    tmp_dir = create_temp_dir()

    # Create a couple of files inside the temporary directory
    create_temp_file(tmp_dir, 'abracadabra.py')
    create_temp_file(tmp_dir, 'cookiecutter-magic.py')

    # Create

# Generated at 2022-06-13 18:29:09.899180
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.join(os.path.dirname(__file__), '..', 'tests', 'fake-repo-tmpl')
    assert find_template(repo_dir) == os.path.join(repo_dir, '{{cookiecutter.repo_name}}')

# Generated at 2022-06-13 18:29:19.382669
# Unit test for function find_template
def test_find_template():
    """ Unit test for function find_template """
    import tempfile
    with tempfile.TemporaryDirectory() as repo_dir:
        repo_dir_contents = ["cookiecutter-{{cookiecutter.repo_name}}", "cookiecutter-{{cookiecutter.repo_name}}.git"]
        for item in repo_dir_contents:
            os.mkdir(os.path.join(repo_dir, item))
        project_template = find_template(repo_dir)

        assert project_template == os.path.join(repo_dir, repo_dir_contents[0])

# Generated at 2022-06-13 18:29:22.644091
# Unit test for function find_template
def test_find_template():
    """Test function find_template()."""

    result = find_template('/Users/tony/')
    assert result == '/Users/tony/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:29:31.211316
# Unit test for function find_template
def test_find_template():
    """Test that the find_template function returns the location of the template folder
    """
    import os
    import shutil
    import tempfile

    # create a temporary working directory
    temp_dir = tempfile.mkdtemp()

    # create a test directory tree
    print(temp_dir)
    os.makedirs(os.path.join(temp_dir, 'inputdir', 'dir1', 'dir2'))
    os.makedirs(os.path.join(temp_dir, 'inputdir', 'dir3', 'dir4'))

    # create a project template inside the tree
    project_template = os.path.join(temp_dir, 'inputdir', '{{cookiecutter.project_name}}', '{{cookiecutter.project_name}}')
    os.makedirs(project_template)

    #

# Generated at 2022-06-13 18:29:39.538291
# Unit test for function find_template
def test_find_template():
    from cookiecutter.utils import rmtree

    # Create a repo with a template dir
    test_dir = os.path.join(
        os.path.expanduser('~'), 'cookiecutter-test-find-tmp'
    )
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)
    template_dir = os.path.join(test_dir, '{{cookiecutter.repo_name}}')
    os.makedirs(template_dir)

    try:
        assert find_template(test_dir) == template_dir
    finally:
        rmtree(test_dir)

# Generated at 2022-06-13 18:29:48.334467
# Unit test for function find_template
def test_find_template():
    """Test finding the project template."""
    import os
    import shutil
    import tempfile

    temp_dir = tempfile.mkdtemp(suffix='cookiecutter')
    os.makedirs(os.path.join(temp_dir, 'cookiecutter-foobar'))
    os.makedirs(os.path.join(temp_dir, 'cookiecutter-{{cookiecutter.project_name}}'))
    os.makedirs(os.path.join(temp_dir, 'cookiecutter-{{cookiecutter.project_slug}}'))
    os.makedirs(os.path.join(temp_dir, 'cookiecutter-project-name'))
    os.makedirs(os.path.join(temp_dir, 'cookiecutter_project_slug'))
    os

# Generated at 2022-06-13 18:29:55.691122
# Unit test for function find_template
def test_find_template():
    """Find a project template in a repo clone."""
    repo_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'fake-repo'
    )
    project_template = os.path.join(repo_dir, 'cookiecutter-pypackage')
    assert find_template(repo_dir) == project_template



# Generated at 2022-06-13 18:30:04.928764
# Unit test for function find_template
def test_find_template():
    """Unit test for function find_template."""

    import mock

    @mock.patch('cookiecutter.repository.find_template')
    def test(repo_dir, project_template):
        """Unit test for function find_template."""
        from cookiecutter.repository import find_template

        assert find_template(repo_dir) == project_template

    test('tests/test-repo-pre/', 'tests/test-repo-pre/{{cookiecutter.repo_name}}')
    test('tests/test-repo-post/', 'tests/test-repo-post/')


# Generated at 2022-06-13 18:30:09.658082
# Unit test for function find_template
def test_find_template():
    """Verify that find_template() is able to find project template"""
    input_path = os.path.join(os.getcwd(), 'tests', 'test-find-project-tmpl')
    project_tmpl_path = find_template(input_path)
    assert (project_tmpl_path == input_path + '/{{cookiecutter.repo_name}}')


# Generated at 2022-06-13 18:30:11.913852
# Unit test for function find_template
def test_find_template():
    """Test that find_template works as expected."""
    find_template('/path/to/repo')

# Generated at 2022-06-13 18:30:22.527585
# Unit test for function find_template
def test_find_template():

    # Create a testing directory
    import tempfile
    temp_dir = tempfile.mkdtemp()
    os.mkdir(os.path.join(temp_dir, 'foo{{cookiecutter.project_name}}bar'))
    assert find_template(temp_dir) == os.path.join(temp_dir, 'foo{{cookiecutter.project_name}}bar')
    import shutil
    shutil.rmtree(temp_dir)

    # Create a testing directory
    import tempfile
    temp_dir = tempfile.mkdtemp()
    os.mkdir(os.path.join(temp_dir, 'foo'))
    assert find_template(temp_dir) != os.path.join(temp_dir, 'foo')
    import shutil
    shutil.rmtree(temp_dir)

# Generated at 2022-06-13 18:30:25.863494
# Unit test for function find_template
def test_find_template():
    logger.debug('Running unit test for function find_template.')
    repo_dir = os.path.expanduser('~/.cookiecutters/cookiecutter-pypackage')
    project_template = find_template(repo_dir)
    assert project_template == '~/.cookiecutters/cookiecutter-pypackage/{{cookiecutter.repo_name}}', 'Wrong project template.'

# Generated at 2022-06-13 18:30:26.964106
# Unit test for function find_template
def test_find_template():
    """Verify find_template function."""
    pass

# Generated at 2022-06-13 18:30:29.744745
# Unit test for function find_template
def test_find_template():
    """Unit test for the find_template function."""
    find_template('./tests/fake-repo-pre/') == './tests/fake-repo-pre/cookiecutter-pypackage'

# Generated at 2022-06-13 18:30:42.645225
# Unit test for function find_template
def test_find_template():
    """Test `find_template` function."""
    import git
    import pytest
    from cookiecutter.main import cookiecutter

    user_config = {
        'cookiecutters_dir': '~/.cookiecutters',
        'replay_dir': '~/.cookiecutters-replay',
    }
    result = cookiecutter('https://github.com/audreyr/cookiecutter-pypackage',
                          no_input=True,
                          checkout='0.1.1',
                          replay=True,
                          user_config=user_config)
    assert os.path.exists(result) is True

    # Remove the cloned repo
    cookiecutters_dir = os.path.expanduser(user_config['cookiecutters_dir'])

# Generated at 2022-06-13 18:30:43.860720
# Unit test for function find_template
def test_find_template():
    pass

# Generated at 2022-06-13 18:30:45.551174
# Unit test for function find_template
def test_find_template():
    """Test for function find_template."""
    pass

# Generated at 2022-06-13 18:30:50.991897
# Unit test for function find_template
def test_find_template():
    """Test find_template function."""
    from cookiecutter.tests.test_find_template import \
        find_template_test_dir
    find_template(find_template_test_dir)

# Generated at 2022-06-13 18:31:02.347694
# Unit test for function find_template
def test_find_template():
    import os
    import shutil
    import tempfile
    from cookiecutter.exceptions import NonTemplatedInputDirException

    repo_dir = tempfile.mkdtemp()
    cookiecutter_dir = os.path.join(repo_dir, 'cookiecutter-foobar')
    os.makedirs(cookiecutter_dir)
    try:
        template_dir = find_template(repo_dir)
        assert template_dir == cookiecutter_dir
    finally:
        shutil.rmtree(repo_dir)

    try:
        find_template(repo_dir)
        assert False, 'Should raise NonTemplatedInputDirException.'
    except NonTemplatedInputDirException:
        pass

# Generated at 2022-06-13 18:31:09.614948
# Unit test for function find_template
def test_find_template():
    """Test `find_template`."""
    import tempfile
    from cookiecutter.compat import TemporaryDirectory

    with TemporaryDirectory() as tmpdir:
        tmpdir = os.path.realpath(tmpdir)
        os.chdir(tmpdir)

        list_of_dirs = [
            'cookiecutter-foobar',
            'cookiecutter-{{cookiecutter.repo_name}}',
            'cookiecutter-myproject',
        ]

        for item in list_of_dirs:
            os.mkdir(item)

        assert find_template(tmpdir) == os.path.join(
            tmpdir,
            'cookiecutter-{{cookiecutter.repo_name}}'
        )

# Generated at 2022-06-13 18:31:13.806306
# Unit test for function find_template
def test_find_template():
    from cookiecutter.tests.test_find import is_non_template

    assert find_template('cookiecutter/tests/fake-repo-pre/') == \
        'cookiecutter/tests/fake-repo-pre/{{cookiecutter.repo_name}}'
    assert is_non_template(find_template('cookiecutter/tests/empty/'))
    assert is_non_template(find_template('cookiecutter/tests/fake-repo-raw/'))

# Generated at 2022-06-13 18:31:19.099941
# Unit test for function find_template
def test_find_template():
    #todo see if this is the best test
    test_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'test_find_template'
    )
    template_expected = os.path.join(test_dir, '{{cookiecutter.repo_name}}')
    template_found = find_template(test_dir)
    assert template_expected == template_found

# Generated at 2022-06-13 18:31:26.491158
# Unit test for function find_template
def test_find_template():
    """Verify template finding functionality.

    Create a new directory with files and subdirectories. Check for a correctly
    templated directory.
    """
    from cookiecutter.tests.test_utils import make_localdir

    repo_dir = make_localdir()
    template = find_template(repo_dir)
    expected = os.path.join(repo_dir, '{{cookiecutter.repo_name}}')
    assert template == expected

    not_templated_dir = make_localdir()
    os.rmdir(not_templated_dir)
    os.mkdir(not_templated_dir)
    expected = os.path.join(repo_dir, '{{cookiecutter.repo_name}}')

# Generated at 2022-06-13 18:31:36.921885
# Unit test for function find_template
def test_find_template():
    from unittest import TestCase
    from cookiecutter.main import cookiecutter

    # Create a dummy Cookiecutter package
    repo_dir = cookiecutter('tests/test-repo-pre/', no_input=True)

    class TestFindTemplate(TestCase):
        def test_find_template_success(self):
            """
            find_template should find the generated project template
            inside the repo folder.
            """
            template = find_template(repo_dir)
            self.assertTrue('dummy-project-{{cookiecutter.repo_name}}' in template)

# Generated at 2022-06-13 18:31:45.236124
# Unit test for function find_template
def test_find_template():
    from cookiecutter import repo
    from .compat import patch

    with patch('cookiecutter.utils.find_template') as mock_find_template:
        mock_find_template.return_value = 'mock_template_dir'
        with patch('cookiecutter.utils.make_sure_path_exists') as mock_make_sure_path_exists:
            with patch('cookiecutter.utils.configure_logger') as mock_configure_logger:
                with patch('cookiecutter.utils.work_in') as mock_work_in:
                    repo.generate_files('mock_repo_dir', 'mock_output_dir', 'mock_context_file')

                    mock_find_template.assert_called_once_with('mock_repo_dir')
                    mock_make

# Generated at 2022-06-13 18:31:58.313632
# Unit test for function find_template
def test_find_template():
    """The function find_template should return the string path of the
    project template. When called on a repo_dir with no project template,
    the function should raise an exception.
    """

    # Create a test directory with several items in it
    test_dir_path = 'test_dir'
    os.mkdir(test_dir_path)

    test_file1 = 'test_file1.txt'
    test_dir = 'test_dir'

    test_file2 = 'test_file2.txt'
    test_dir2 = 'test_dir2'

    # Create a subdirectory that contains a cookiecutter template
    test_dir3 = 'test_dir3'
    test_dir3_path = os.path.join(test_dir_path, test_dir3)
    project_template = 'test_template'

# Generated at 2022-06-13 18:32:02.980650
# Unit test for function find_template
def test_find_template():
    """
    Unit test for find_template.
    """
    repo_dir = '/home/brian/repo'
    expected = '/home/brian/repo/cookiecutter-tpl-repo'
    result = find_template(repo_dir)
    assert result == expected

# Generated at 2022-06-13 18:32:12.183862
# Unit test for function find_template
def test_find_template():
    test_repo_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        '..',
        'tests',
        'fake-repo'
    )
    assert find_template(test_repo_dir) == os.path.join(
        test_repo_dir,
        'fake-project/{{cookiecutter.project_name}}/'
    )

# Generated at 2022-06-13 18:32:18.002129
# Unit test for function find_template
def test_find_template():
    """Read a test directory and get the path to the template."""
    repo_dir = os.path.join(
        os.path.dirname(__file__),
        'test-data/fake-repo-tmpl/'
    )
    assert find_template(repo_dir) == os.path.join(repo_dir, '{{cookiecutter.repo_name}}')

# Generated at 2022-06-13 18:32:26.500076
# Unit test for function find_template
def test_find_template():
    """Verify find_template() identifies templates correctly."""
    import tempfile
    import shutil
    template_dir, output_dir = None, None


# Generated at 2022-06-13 18:32:29.357205
# Unit test for function find_template
def test_find_template():
    """Test find_template function"""

    assert 'cookiecutter-pypackage' in find_template('https://github.com/audreyr/cookiecutter-pypackage.git')
    assert 'cookiecutter-pypackage' in find_template('/tmp/test-cookiecutter/')

# Generated at 2022-06-13 18:32:31.418732
# Unit test for function find_template
def test_find_template():
    find_template("/Users/cody/Dropbox/projects/master_cookiecutter")

# Generated at 2022-06-13 18:32:33.020998
# Unit test for function find_template
def test_find_template():
    pass

# Generated at 2022-06-13 18:32:37.582554
# Unit test for function find_template
def test_find_template():
    repo_dir = current_dir = os.path.abspath(os.path.dirname(__file__))
    project_template = find_template(repo_dir)
    assert project_template == os.path.join(repo_dir, '{{cookiecutter.repo_name}}')

# Generated at 2022-06-13 18:32:48.276381
# Unit test for function find_template
def test_find_template():  #pragma: no cover
    """Verify expected templates returned by find_template()."""
    import os
    import shutil
    import tempfile
    from cookiecutter import main

    test_templates = [
        # A template with two levels of nested templates
        # {{cookiecutter.repo_name}}/{{cookiecutter.repo_name}}-{{cookiecutter.version}}
        # E.g. cookiecutter-pypackage/cookiecutter-pypackage-2015.06.09
        ('py_package_template', 'cookiecutter-pypackage'),
        # A template with no nested templates. No version number
        ('py_package_template_no_nesting', 'cookiecutter-pypackage-2015.06.09'),
    ]

    # Create temporary directories, clone templates

# Generated at 2022-06-13 18:32:50.990413
# Unit test for function find_template
def test_find_template():
    assert find_template('repo_dir') == 'repo_dir/cookiecutter-{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:32:53.323387
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'repo-tmpl')
    project_template = find_template(repo_dir)
    assert os.path.basename(project_template) == '{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:33:09.904967
# Unit test for function find_template
def test_find_template():
    """Verify that `find_template` works as expected."""
    import tempfile
    from cookiecutter import utils
    from cookiecutter.exceptions import NonTemplatedInputDirException

    with utils.work_in(tempfile.mkdtemp()):
        utils.make_sure_path_exists('fake_template')
        utils.make_sure_path_exists('fake_template/cookiecutter.json')
        utils.make_sure_path_exists('fake_template/{{fake_var}}')
        utils.make_sure_path_exists('fake_template/{{fake_var2}}')

        project_template = find_template('.')

        assert project_template == 'fake_template/{{fake_var}}'

        # Test when there is no templated directory
       

# Generated at 2022-06-13 18:33:18.629897
# Unit test for function find_template
def test_find_template():
    """
    Unit test for find_template function,
    verifies if all the cases are covered
    """

    from cookiecutter.utils import path_to_url

    class Args:
        """
        Mock class for args
        """
        extra_context = {}
        overwrite_if_exists = False
        no_input = False

    test_repo = 'tests/test-repo-pre/'
    test_repo_contents = os.listdir(test_repo)

    project_template = find_template(test_repo)
    assert project_template == 'tests/test-repo-pre/cookiecutter-pypackage'

    test_repo = 'tests/test-repo-tmpl/'
    project_template = find_template(test_repo)
    assert project_

# Generated at 2022-06-13 18:33:24.106575
# Unit test for function find_template
def test_find_template():
    """Unit test for function find_template"""
    os.chdir(os.path.join(os.path.dirname(__file__),
                          '..', 'tests', 'test-find-template'))
    template_from_src = find_template('.')
    template_from_dst = find_template('.')
    assert template_from_src == template_from_dst

# Generated at 2022-06-13 18:33:25.512911
# Unit test for function find_template
def test_find_template():
    os.path.join(os.path.dirname(__file__), os.pardir, 'repos', 'tests', 'fake-repo-tmpl', 'cookiecutter-foobar')

# Generated at 2022-06-13 18:33:27.140899
# Unit test for function find_template
def test_find_template():
    # TODO: add a test for when there are multiple possible templates
    pass

# Generated at 2022-06-13 18:33:27.778689
# Unit test for function find_template
def test_find_template():
    pass

# Generated at 2022-06-13 18:33:33.879665
# Unit test for function find_template
def test_find_template():
    os.chdir("tests/files/find-template")
    repo_dir = os.path.join("tests/files/find-template")
    project_template = find_template(repo_dir)
    assert project_template is not None
    template_dir_expected = os.path.abspath("tests/files/find-template/{{cookiecutter.repo_name}}")
    assert project_template == template_dir_expected

######################################################################
# Functions for finding files and directories which match a pattern
######################################################################


# Generated at 2022-06-13 18:33:40.295494
# Unit test for function find_template
def test_find_template():
    """Verify find_template works as expected"""
    from cookiecutter import config


    test_template_name = 'foobar-{{cookiecutter.project_slug}}'
    repo_dir = os.path.join(config.USER_CACHE_DIRECTORY, test_template_name)
    os.mkdir(repo_dir)

    project_template = find_template(repo_dir)
    assert project_template == os.path.join(repo_dir, test_template_name)

    os.rmdir(repo_dir)

# Generated at 2022-06-13 18:33:41.640973
# Unit test for function find_template
def test_find_template():
    assert find_template('test')

# Generated at 2022-06-13 18:33:48.484424
# Unit test for function find_template
def test_find_template():
    repo_dir = 'repo_dir'
    repo_dir_contents = [
        'bin',
        'README.md',
        '{{cookiecutter.project_name}}'
    ]

    m = Mock(return_value=repo_dir_contents)
    monkeypatch.setattr(os, 'listdir', m)
    assert find_template(repo_dir) == os.path.join(repo_dir, '{{cookiecutter.project_name}}')
    #assert os.path.join(repo_dir, '{{cookiecutter.project_name}}') == find_template(repo_dir)

# Generated at 2022-06-13 18:33:55.576117
# Unit test for function find_template
def test_find_template():
    pass

# Generated at 2022-06-13 18:33:59.185546
# Unit test for function find_template
def test_find_template():
    repo_dir = 'cookiecutter-pypackage'
    project_template = find_template(repo_dir)
    assert project_template == 'cookiecutter-pypackage/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:34:05.995583
# Unit test for function find_template
def test_find_template():
    repo_dir = 'tests/test-find-repo'

    project_template = find_template(repo_dir)

    # Check that the function returns the path to the directory, not the
    # directory itself.
    assert os.path.split(project_template)[-1] == '{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:34:14.080523
# Unit test for function find_template
def test_find_template():
    """
    Basic sanity checks for find_template
    """
    # Create a local directory with a couple of files and directories
    from .compat import TemporaryDirectory
    from .main import get_user_config
    from .main import get_template

    log_fmt = '%(levelname)s %(asctime)s %(module)s %(lineno)d %(message)s'
    logging.basicConfig(level=logging.DEBUG, format=log_fmt)

    user_config_file = get_user_config()
    user_config = {}
    user_config['replay_dir'] = '~/.cookiecutter_replay'

# Generated at 2022-06-13 18:34:14.828519
# Unit test for function find_template
def test_find_template():
    pass

# Generated at 2022-06-13 18:34:27.346748
# Unit test for function find_template
def test_find_template():
    """Verify that find_template returns the appropriate string."""
    find_template_input_output = [
        ('input/fake-repo-tmpl', 'input/fake-repo-tmpl/{{cookiecutter.repo_name}}'),
        ('input/fake-repo-pre', 'input/fake-repo-pre/cookiecutter-fake-repo-pre'),
        ('input/fake-repo-post', 'input/fake-repo-post/fake-repo-post-cookiecutter'),
        ('input/fake-repo-both', 'input/fake-repo-both/cookiecutter-fake-repo-both-cookiecutter'),
        ('input/fake-repo-neither', None)
    ]

    for item in find_template_input_output:
        find_template

# Generated at 2022-06-13 18:34:28.873713
# Unit test for function find_template
def test_find_template():
    find_template('test/fixture/repo-tmpl')

# Generated at 2022-06-13 18:34:35.507582
# Unit test for function find_template
def test_find_template():
    logging.disable(logging.CRITICAL)
    repo_dir = os.path.abspath(os.path.join(
        os.path.dirname(__file__), '..', 'tests', 'test-template'
    ))
    repo_dir_contents = os.listdir(repo_dir)

    project_template = find_template(repo_dir)
    assert project_template == os.path.join(repo_dir, '{{cookiecutter.repo_name}}')

# Generated at 2022-06-13 18:34:39.508470
# Unit test for function find_template
def test_find_template():
    """Test that find_template finds the expected template"""
    template_dir = os.path.join(os.path.dirname(__file__), '..', 'fake-repo-tmpl')

    project_template = find_template(template_dir)

    assert project_template == os.path.join(template_dir, '{{cookiecutter.repo_name}}')


# Generated at 2022-06-13 18:34:44.731137
# Unit test for function find_template
def test_find_template():
    filename = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        '../tests/test-find-template-samples'
    )
    project_template = find_template(filename)
    assert project_template == os.path.join(filename, 'my-custom-cookiecutter')

# Generated at 2022-06-13 18:35:00.842935
# Unit test for function find_template
def test_find_template():
    find_template('/home/chris/projects/unfuddle_thirdparty_infrastructure')

# Generated at 2022-06-13 18:35:03.864634
# Unit test for function find_template
def test_find_template():
    os.chdir('tests/fake-repo')
    assert find_template('./') == os.path.join('.', '{{cookiecutter.repo_name}}')

# Generated at 2022-06-13 18:35:05.056895
# Unit test for function find_template
def test_find_template():
    # TODO: write tests
    pass

# Generated at 2022-06-13 18:35:10.229385
# Unit test for function find_template
def test_find_template():
    repo_dir = 'tests/test-data/fake-repo'
    repo_dir_contents = os.listdir(repo_dir)
    project_template = find_template(repo_dir)
    assert '{{cookiecutter.repo_name}}' in project_template
    assert '.git' not in repo_dir_contents

# Generated at 2022-06-13 18:35:15.720495
# Unit test for function find_template
def test_find_template():
    assert find_template('/home/audreyr/cookiecutter-pypackage') == '/home/audreyr/cookiecutter-pypackage/{{cookiecutter.repo_name}}'
    assert find_template('/home/audreyr/jquery-cookiecutter') == '/home/audreyr/jquery-cookiecutter/{{cookiecutter.github_username}}-{{cookiecutter.project_name}}'

# Generated at 2022-06-13 18:35:28.807409
# Unit test for function find_template
def test_find_template():
    """Test find_template function."""
    repo_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'fake-repo-pre-gen',
        '{{cookiecutter.repo_name}}',
    )
    project_template = find_template(repo_dir)
    assert project_template == os.path.join(repo_dir, '{{cookiecutter.repo_name}}')

    repo_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'fake-repo-pre-gen',
        'no-templated-dir',
    )
    non_templated_dir_exc = False

# Generated at 2022-06-13 18:35:34.768879
# Unit test for function find_template
def test_find_template():
    # Testing normal operation
    testing_dir = 'tests/fake-repo-tmpl'
    expected_tmpl = os.path.join(testing_dir, 'cookiecutter-{{cookiecutter.repo_name}}')
    result = find_template(testing_dir)
    assert result == expected_tmpl

    # Testing bad directory
    testing_dir = 'tests/fake-repo'
    try:
        result = find_template(testing_dir)
        assert False, 'Expected an exception to be raised.'
    except NonTemplatedInputDirException:
        assert True

# Generated at 2022-06-13 18:35:37.349311
# Unit test for function find_template
def test_find_template():
    from cookiecutter.tests.test_utils.paths import fixtures_path
    repo_dir = os.path.join(fixtures_path('fake-repo'), 'cookiecutter-pypackage')
    template = find_template(repo_dir)
    assert os.path.exists(template)

# Generated at 2022-06-13 18:35:41.490038
# Unit test for function find_template
def test_find_template():
    logger.debug('Testing function find_template')

    repo_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    project_template = find_template(repo_dir)
    assert "cookiecutter-pypackage" in project_template

# Generated at 2022-06-13 18:35:49.044769
# Unit test for function find_template
def test_find_template():
    f_find_template = find_template

# Generated at 2022-06-13 18:36:18.702437
# Unit test for function find_template
def test_find_template():
    """Test find_template function."""


# Generated at 2022-06-13 18:36:28.997339
# Unit test for function find_template
def test_find_template():
    """Test the find_template function
    """
    # pylint:disable=missing-docstring,unused-variable
    import pytest
    from cookiecutter.main import find_template

    repo_dir = 'tests/fake-repo-tmpl/'
    project_template = 'tests/fake-repo-tmpl/{{cookiecutter.repo_name}}/'

    def test_find_template(monkeypatch):
        monkeypatch.chdir(repo_dir)
        assert find_template(repo_dir) == project_template

    def test_find_template_non_template():
        with pytest.raises(NonTemplatedInputDirException) as excinfo:
            find_template(repo_dir + 'notemplate')

# Generated at 2022-06-13 18:36:32.252576
# Unit test for function find_template
def test_find_template():
    assert find_template('tests/test-data/fake-reo/') == 'tests/test-data/fake-reo/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:36:39.452639
# Unit test for function find_template
def test_find_template():
    from cookiecutter.main import cookiecutter
    import os

    repo_dir = os.path.join(os.getcwd(), 'tests/test-find-templates')
    context_file = os.path.join(repo_dir, 'cookiecutter.json')
    output_dir = os.path.join(repo_dir, 'fake-repo')

    cookiecutter(
        repo_dir=repo_dir,
        context_file=context_file,
        no_input=True,
        overwrite_if_exists=True
    )

    assert os.path.exists(output_dir)

# Generated at 2022-06-13 18:36:45.422566
# Unit test for function find_template
def test_find_template():
    here = os.path.dirname(os.path.abspath(__file__))
    test_repo = os.path.join(here, '..', 'tests', 'test-find-template-repo')
    template = find_template(test_repo)
    assert template == os.path.join(test_repo, '{{cookiecutter.project_slug}}')

# Generated at 2022-06-13 18:36:51.622061
# Unit test for function find_template
def test_find_template():
    import os
    import shutil
    from cookiecutter.utils.paths import normalize_path
    from cookiecutter.utils import rmtree
    import logging

    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

    repo_dir = normalize_path('.')


# Generated at 2022-06-13 18:36:53.332897
# Unit test for function find_template
def test_find_template():
    find_template(r"C:\Users\Naveen\Desktop\cookiecutter-master\cookiecutter")

# Generated at 2022-06-13 18:36:57.481709
# Unit test for function find_template
def test_find_template():
    """
    Test function find_template
    """
    import tempfile
    from cookiecutter.compat import NamedTemporaryFile

    test_dir = tempfile.mkdtemp()

    os.makedirs(os.path.join(
        test_dir, '{{cookiecutter.repo_name}}'))

    project_dir = find_template(test_dir)
    assert '{{cookiecutter.repo_name}}' == os.path.basename(project_dir)

    repo_dir_contents = os.listdir(test_dir)
    assert len(repo_dir_contents) == 1

    os.removedirs(project_dir)

# Generated at 2022-06-13 18:37:00.930146
# Unit test for function find_template
def test_find_template():
    template = find_template('tests/test-data/fake-repo-pre/')
    assert template == 'tests/test-data/fake-repo-pre/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:37:05.125526
# Unit test for function find_template
def test_find_template():
    """ Verify find_template() returns the correct value """

    repo_dir = 'fakerepo'
    template_dir = 'fakerepo/fakerepo-{{cookiecutter.repo_name}}'
    result = find_template(repo_dir)
    assert result == template_dir