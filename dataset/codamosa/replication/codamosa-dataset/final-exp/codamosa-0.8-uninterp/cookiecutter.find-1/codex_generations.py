

# Generated at 2022-06-13 18:27:39.119794
# Unit test for function find_template
def test_find_template():
    assert find_template("E:\Python\Python36\Lib\site-packages\cookiecutter\repository") == "E:\Python\Python36\Lib\site-packages\cookiecutter\repository\{{cookiecutter.repo_name}}"

# Generated at 2022-06-13 18:27:42.477223
# Unit test for function find_template
def test_find_template():
    assert find_template('{{cookiecutter.repo_dir}}') == '{{cookiecutter.repo_dir}}'

# Generated at 2022-06-13 18:27:44.723762
# Unit test for function find_template
def test_find_template():
    """Unit test for function find_template"""
    # TODO: Fix this.
    pass

# Generated at 2022-06-13 18:27:46.339041
# Unit test for function find_template
def test_find_template():
    """Search for template in repo dir."""
    re

# Generated at 2022-06-13 18:27:50.422841
# Unit test for function find_template
def test_find_template():
    assert find_template('tests/test-repo') == os.path.join('tests', 'test-repo', '{{cookiecutter.repo_name}}')

# Generated at 2022-06-13 18:27:59.770076
# Unit test for function find_template
def test_find_template():
    """Verify function find_template works as expected."""
    # Non templated root directory
    root_dir = os.path.abspath(os.path.dirname(__file__))
    repo_dir = os.path.join(root_dir, 'fake-repo')
    try:
        find_template(repo_dir)
    except NonTemplatedInputDirException:
        pass
    else:
        raise AssertionError('NonTemplatedInputDirException not raised for '
                             'non-templated repo.')

    # Templated root directory
    repo_dir = os.path.join(root_dir, 'fake-repo-templated')

# Generated at 2022-06-13 18:28:03.248714
# Unit test for function find_template
def test_find_template():
    """Verify that find_template returns the correct path when called."""
    assert find_template('fake_dir') == 'fake_dir/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:28:10.405324
# Unit test for function find_template
def test_find_template():
    try:
        from cookiecutter.tests.test_utils import TEST_CWD
    except ImportError:
        TEST_CWD = os.path.dirname(__file__)

    result_dir = find_template(os.path.join(TEST_CWD, 'fake-repo-pre/fake-repo'))
    assert result_dir.endswith('fake-repo-pre/fake-repo/{{cookiecutter.repo_name}}')



# Generated at 2022-06-13 18:28:13.588930
# Unit test for function find_template
def test_find_template():
    """ Test the find_template function """
    assert find_template('tests/test-input') == 'tests/test-input/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:28:25.510492
# Unit test for function find_template
def test_find_template():
    os.rename('tests/test-generate-repo/cookiecutter-foobar', 'tests/test-generate-repo/{{cookiecutter.repo_name}}')
    assert find_template('tests/test-generate-repo') == 'tests/test-generate-repo/{{cookiecutter.repo_name}}'
    os.rename('tests/test-generate-repo/{{cookiecutter.repo_name}}', 'tests/test-generate-repo/cookiecutter-foobar')
    assert find_template('tests/test-generate-repo') == 'tests/test-generate-repo/cookiecutter-foobar'

# Generated at 2022-06-13 18:28:31.638584
# Unit test for function find_template
def test_find_template():
    """Verify that find_template function works expected."""
    #import pdb; pdb.set_trace()
    find_template('/home/kvaps/workdir/code/emcy/python-projects/cookiecutter-pypackage')

# Generated at 2022-06-13 18:28:40.544452
# Unit test for function find_template
def test_find_template():
    from cookiecutter import utils
    import os
    import shutil
    import tempfile

    # Create a temporary project directory
    project_dir = tempfile.mkdtemp()
    repo_dir = os.path.join(project_dir, 'test_repo')
    os.makedirs(repo_dir)

    # Create a test template
    template_dir = os.path.join(repo_dir, '{{cookiecutter.repo_name}}')
    os.makedirs(template_dir)

    # Write a test template
    template_file = open(os.path.join(template_dir, 'test_template.txt'), 'w')
    template_file.write('This is a test template.')
    template_file.close()

    # Find the template and assert that it exists

# Generated at 2022-06-13 18:28:42.413288
# Unit test for function find_template
def test_find_template():
    assert(find_template('/home') == '{{cookiecutter.repo_dir}}/{{cookiecutter.repo_dir}}')

# Generated at 2022-06-13 18:28:53.816243
# Unit test for function find_template
def test_find_template():

    # Setup
    import tempfile

    repo_dir = tempfile.mkdtemp()

    template = "{{cookiecutter.repo_name}}"
    path = os.path.join(repo_dir, template)

    # Tests

    # This is the default behaviour
    with open(path, 'w') as f:
        f.write('Test')

    assert find_template(repo_dir) == path

    # The template directory is still found if it's nested
    nested_path = os.path.join(repo_dir, 'nested')
    os.makedirs(nested_path)
    with open(os.path.join(nested_path, template), 'w') as f:
        f.write('Test')


# Generated at 2022-06-13 18:29:00.156646
# Unit test for function find_template
def test_find_template():
    import tempfile
    import shutil
    import os

    tmp_dir = tempfile.mkdtemp()

    os.mkdir(os.path.join(tmp_dir, 'cookiecutter-foobar'))

    template = find_template(tmp_dir)

    assert template == os.path.join(tmp_dir, 'cookiecutter-foobar')

    shutil.rmtree(tmp_dir)

# Generated at 2022-06-13 18:29:07.413995
# Unit test for function find_template
def test_find_template():
    assert find_template(repo_dir='tests/fake-repo-pre/') == 'tests/fake-repo-pre/{{cookiecutter.repo_name}}'
    assert find_template(repo_dir='tests/fake-repo-post/') == 'tests/fake-repo-post/safe_project_slug'

# Generated at 2022-06-13 18:29:10.134716
# Unit test for function find_template
def test_find_template():
    repo_dir = "/Users/audreyr/Documents/cookiecutter-pypackage/"
    find_template(repo_dir)

# Generated at 2022-06-13 18:29:18.245576
# Unit test for function find_template
def test_find_template():
    import shutil
    from cookiecutter import utils

    template_dir = 'tests/test-template/'
    test_dir = 'tests/test-dir/'
    utils.make_sure_path_exists(test_dir)
    shutil.copytree(template_dir, test_dir + template_dir)
    template = find_template(test_dir)

    assert template == 'tests/test-dir/tests/test-template/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:29:28.154853
# Unit test for function find_template
def test_find_template():
    """Unit test for function find_template"""
    import shutil
    import tempfile

# Generated at 2022-06-13 18:29:31.330882
# Unit test for function find_template
def test_find_template():
    test_repo_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'test_find_template_repo'
    )
    assert 'test-repo' == find_template(test_repo_dir)

# Generated at 2022-06-13 18:29:39.666107
# Unit test for function find_template
def test_find_template():
    dir1 = os.path.join(os.path.dirname(__file__), 'fake-repo-pre', '{{cookiecutter.repo_name}}')
    dir2 = os.path.join(os.path.dirname(__file__), 'fake-repo-post')

    assert find_template(dir1) == os.path.join(dir1, 'fake-repo-pre')
    assert find_template(dir2) == os.path.join(dir2, '{{cookiecutter.repo_name}}')

# Generated at 2022-06-13 18:29:40.564806
# Unit test for function find_template
def test_find_template():
    pass



# Generated at 2022-06-13 18:29:46.253804
# Unit test for function find_template
def test_find_template():
    """Unit test for function find_template"""
    repo_dir = '/home/whatevs/hello_cookiecutter'
    project_template = find_template(repo_dir)
    assert project_template == '/home/whatevs/hello_cookiecutter'


# Generated at 2022-06-13 18:29:47.601226
# Unit test for function find_template
def test_find_template():
    # TODO: fix this test to pass
    pass

# Generated at 2022-06-13 18:29:49.368604
# Unit test for function find_template
def test_find_template():
    """
    Test `find_template` function.
    """
    pass

# Generated at 2022-06-13 18:29:57.339144
# Unit test for function find_template
def test_find_template():
    """Tests if the correct template was found."""
    from cookiecutter import utils
    os.chdir(utils.TESTS_DIR)
    test_template = find_template(os.path.abspath("tests/fake-repo-pre/fake_repo_pre/"))
    assert test_template == os.path.abspath("tests/fake-repo-pre/fake_repo_pre/{{cookiecutter.repo_name}}/")


# Generated at 2022-06-13 18:30:02.798276
# Unit test for function find_template
def test_find_template():
    from cookiecutter import repo
    repo_dir = repo.get_repo_contents(
        repo_url='https://github.com/audreyr/cookiecutter-pypackage.git',
        checkout=None,
        no_input=True
    )
    project_template = find_template(repo_dir)
    assert project_template == os.path.join(repo_dir, 'cookiecutter-pypackage')

# Generated at 2022-06-13 18:30:03.472412
# Unit test for function find_template
def test_find_template():
    pass

# Generated at 2022-06-13 18:30:08.186058
# Unit test for function find_template
def test_find_template():
    from cookiecutter.compat import TemporaryDirectory
    with TemporaryDirectory() as repo_dir:
        os.makedirs(os.path.join(repo_dir, 'my_template'))
        template = find_template(repo_dir)
        assert template == os.path.join(repo_dir, 'my_template')

# Generated at 2022-06-13 18:30:13.872276
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        '../tests/test-repo-tmpl'
    )
    template_dir = find_template(repo_dir)
    assert template_dir == os.path.join(repo_dir, '{{cookiecutter.repo_name}}')

# Generated at 2022-06-13 18:30:25.553144
# Unit test for function find_template
def test_find_template():
    '''
    Test that find_template raises an exception if a cookiecutter template dir
    cannot be found
    '''
    # create fake folder structure
    tmp_dir = tempfile.mkdtemp()
    os.mkdir(os.path.join(tmp_dir, 'fake'))
    with pytest.raises(NonTemplatedInputDirException):
        find_template(tmp_dir)
    # remove fake folder structure
    shutil.rmtree(tmp_dir)


# Generated at 2022-06-13 18:30:34.261563
# Unit test for function find_template
def test_find_template():
    from cookiecutter import utils
    from cookiecutter.config import config
    from cookiecutter.compat import TemporaryDirectory
    from cookiecutter.exceptions import InvalidModeException

    with TemporaryDirectory() as repo_dir:
        os.makedirs('test_template')
        os.makedirs('test_template_files')
        open('test_template/test.txt', 'w')
        open('test_template_files/test.txt', 'w')

        # Test when no file or directory is cookiecutter-templated
        assert find_template(repo_dir) == None

        os.makedirs('{{cookiecutter.test_template}}')
        assert os.path.join(repo_dir, '{{cookiecutter.test_template}}') == find_template(repo_dir)

        #

# Generated at 2022-06-13 18:30:36.576414
# Unit test for function find_template
def test_find_template():
    """Verify ``find_template`` works as expected."""
    find_template('tests/fake-repo-tmpl')

# Generated at 2022-06-13 18:30:44.600675
# Unit test for function find_template
def test_find_template():
    def find_template(repo_dir):
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

# Generated at 2022-06-13 18:30:55.502212
# Unit test for function find_template
def test_find_template():
    template_dir = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        '..',
        'tests',
        'test-templates',
        'input'
    )
    assert os.path.join(
        template_dir,
        '{{cookiecutter.project_name}}'
    ) == find_template(template_dir)

    assert os.path.join(
        template_dir,
        '{{cookiecutter.project_name}}-{{cookiecutter.package_name}}'
    ) == find_template(
        os.path.join(template_dir, '{{cookiecutter.project_name}}-{{cookiecutter.package_name}}')
    )

# Generated at 2022-06-13 18:31:01.561164
# Unit test for function find_template
def test_find_template():
    """Test the find_template function.

    :returns: None
    """
    repo_dir = os.path.join(
        os.path.dirname(__file__),
        '..',
        'tests',
        'fake-repo',
    )
    project_template = find_template(repo_dir)
    test_dir = os.path.join(repo_dir, '{{cookiecutter.repo_name}}')
    assert project_template == test_dir

# Generated at 2022-06-13 18:31:04.432231
# Unit test for function find_template
def test_find_template():
    find_template('~/cookiecutter-pypackage')
    try:
        find_template('~/cookiecutter-pypackage/scripts')
    except:
        logger.debug("test_find_template function passed")

# Generated at 2022-06-13 18:31:07.781733
# Unit test for function find_template
def test_find_template():
    assert find_template('.') == './cookiecutter-pypackage'


# Generated at 2022-06-13 18:31:11.808968
# Unit test for function find_template
def test_find_template():
    test_repo = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'tests', 'fake-repo'))
    test_template = os.path.join(test_repo, '{{cookiecutter.repo_name}}')
    assert find_template(test_repo) == test_template

# Generated at 2022-06-13 18:31:17.064199
# Unit test for function find_template
def test_find_template():
    """Verify that find_template identifies the project template folder."""
    import shutil
    from cookiecutter.repository import determine_repo_dir

    tmp_dir = ''
    try:
        tmp_dir = os.path.abspath('/tmp/find_template')
        shutil.copytree(
            os.path.abspath('tests/files/find_template'),
            tmp_dir
        )

        logger.debug('Using temporary directory %s', tmp_dir)
        repo_dir = determine_repo_dir(tmp_dir)
        assert find_template(repo_dir) == os.path.join(tmp_dir, '{{cookiecutter.project_name}}')
    finally:
        shutil.rmtree(tmp_dir)

# Generated at 2022-06-13 18:31:21.132573
# Unit test for function find_template
def test_find_template():
    test_find_template.__test__ = False
    if __name__ == '__main__':
        print(find_template(repo_dir='./tests/fake-repo-pre/'))

# Generated at 2022-06-13 18:31:25.270193
# Unit test for function find_template
def test_find_template():
    parent_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    repo_dir = os.path.join(parent_folder, 'tests', 'test-repo-pre/')
    project_template = find_template(repo_dir)
    assert project_template.endswith('cookiecutter-{{cookiecutter.repo_name}}')


# Generated at 2022-06-13 18:31:37.446107
# Unit test for function find_template
def test_find_template():
    """Test that template was found inside a repo."""

    assert find_template('tests/fake-repo-pre/') == \
        'tests/fake-repo-pre/{{cookiecutter.repo_name}}'

    try:
        find_template('tests/fake-repo-post-no-tpl')
        raise AssertionError("find_template didn't raise exception when it "\
            "should have.")
    except NonTemplatedInputDirException as e:
        pass
    except Exception as e:
        raise AssertionError("Unknown exception raised when a "\
            "NonTemplatedInputDirException was expected.")

test_find_template()

# Generated at 2022-06-13 18:31:41.448591
# Unit test for function find_template
def test_find_template():
    """Test finding the project template.

    Uses a custom repo for testing purposes.
    """
    template = find_template('tests/custom-repo')
    assert template == os.path.join('tests/custom-repo', 'my-custom-repo')

# Generated at 2022-06-13 18:31:46.545785
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.join('tests', 'test-repo')
    project_template = find_template(repo_dir)
    assert project_template == os.path.join(repo_dir, 'cookiecutter-pypackage')

# Generated at 2022-06-13 18:31:47.328803
# Unit test for function find_template
def test_find_template():
    pass

# Generated at 2022-06-13 18:31:50.580222
# Unit test for function find_template
def test_find_template():
    assert find_template('tests/fake-repo-tmpl') == 'tests/fake-repo-tmpl/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:31:52.625121
# Unit test for function find_template
def test_find_template():
    """Verify find_template() works properly."""
    # TODO: Need to write unit tests for this function
    pass

# Generated at 2022-06-13 18:31:57.972548
# Unit test for function find_template
def test_find_template():
    repo_dir = '/Users/audreyr/projects/cookiecutter/tests/test-data/fake-repo'
    find_template(repo_dir)

# Generated at 2022-06-13 18:32:06.593772
# Unit test for function find_template
def test_find_template():
    if os.path.exists('project_template_test'):
        os.remove('project_template_test')
    os.mkdir('project_template_test')

    os.mkdir(os.path.join('project_template_test', 'foo'))
    os.mkdir(os.path.join('project_template_test', '{{cookiecutter.bar}}'))

    template_folder = find_template('project_template_test')
    assert template_folder == os.path.join('project_template_test', '{{cookiecutter.bar}}')

    os.rmdir(os.path.join('project_template_test', 'foo'))
    os.rmdir(os.path.join('project_template_test', '{{cookiecutter.bar}}'))

# Generated at 2022-06-13 18:32:14.172992
# Unit test for function find_template
def test_find_template():
    """Unit test for function find_template. """

    # Create a non-templated repo
    import tempfile
    tmp_dir = tempfile.mkdtemp()
    os.mkdir(os.path.join(tmp_dir, 'dir1'))
    os.mkdir(os.path.join(tmp_dir, 'dir2'))
    os.mkdir(os.path.join(tmp_dir, 'dir3'))
    assert find_template(tmp_dir) == NonTemplatedInputDirException

# Generated at 2022-06-13 18:32:18.709886
# Unit test for function find_template
def test_find_template():
    """Test find_template function.
    """
    repo_dir = 'tests/fake-repo-pre/'
    project_template = find_template(repo_dir)
    assert project_template == 'tests/fake-repo-pre/hooks-{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:32:22.608091
# Unit test for function find_template
def test_find_template():
    """Function for testing find_template(repo_dir)"""
    repo_dir = os.path.join('tests', 'test-find-template')
    project_template = find_template(repo_dir)
    assert project_template == os.path.join(repo_dir, 'cookiecutter')

# Generated at 2022-06-13 18:32:33.184990
# Unit test for function find_template
def test_find_template():
    # Create the mock objects
    import os
    import tempfile
    import shutil

    dirpath = tempfile.mkdtemp()

    os.makedirs(os.path.join(dirpath, 'cookiecutter-project-name'))
    os.makedirs(os.path.join(dirpath, 'randomdir'))

    # Call the function
    template = find_template(dirpath)

    # Assert that the returned path is correct
    assert template == os.path.join(dirpath, 'cookiecutter-project-name')

    # Cleanup
    shutil.rmtree(dirpath)


# Generated at 2022-06-13 18:32:40.273581
# Unit test for function find_template
def test_find_template():
    """Check that the correct directory is found and returned."""
    from cookiecutter import utils
    from os.path import dirname, join
    parent_dir = dirname(os.path.realpath(__file__))
    test_dir = join(parent_dir, 'test-files', 'fake-repo-tmpl')
    project_template = utils.find_template(test_dir)
    expected_project_template = join(test_dir, '{{cookiecutter.repo_name}}')
    assert project_template == expected_project_template



# Generated at 2022-06-13 18:32:46.229186
# Unit test for function find_template
def test_find_template():
    tgt_dir = os.path.dirname(os.path.abspath(__file__))
    tgt_dir = os.path.join(tgt_dir, 'test-find-template')
    expected_dir = os.path.join(tgt_dir, '{{cookiecutter.repo_name}}')
    assert find_template(tgt_dir) == expected_dir

# Generated at 2022-06-13 18:32:48.449428
# Unit test for function find_template
def test_find_template():
    find_template('/Users/sampanna.kahu/Desktop/cookiecutter-webapp')

# Generated at 2022-06-13 18:32:56.229819
# Unit test for function find_template
def test_find_template():
    """ Test case for find_template """
    
    # Set up
    # Create a directory and two files
    os.mkdir('test')
    os.mkdir('test/cookiecutter')
    open('test/cookiecutter/a.txt', 'w').close()
    open('test/b.txt', 'w').close()
    
    # Call the function to test
    project_template = find_template('test')
    
    # Clean up
    os.remove('test/cookiecutter/a.txt')
    os.remove('test/b.txt')
    os.rmdir('test/cookiecutter')
    os.rmdir('test')
    
    print(project_template)
    # Check results
    assert project_template == 'test/cookiecutter'

# Generated at 2022-06-13 18:32:59.367908
# Unit test for function find_template
def test_find_template():
    """Verify that find_template works."""
    os.chdir(os.path.normpath(os.path.join(os.path.dirname(__file__), '..')))
    template = find_template('test/test-input')
    assert template == 'test/test-input/test-template-repo-{{cookiecutter.repo_name}}', \
           "find_template returned '{}'".format(template)

# Generated at 2022-06-13 18:33:03.490923
# Unit test for function find_template
def test_find_template():
    '''
    NonTemplatedInputDirException is thrown if the template is non-templated
    directory.
    '''
    try:
        find_template('tests/fake-repo')
    except NonTemplatedInputDirException:
        pass

# Generated at 2022-06-13 18:33:16.931599
# Unit test for function find_template
def test_find_template():
    import os
    import pytest
    from cookiecutter.exceptions import NonTemplatedInputDirException

    repo_dir = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        'fake-repo-tmpl'
    )

    assert '/tests/fake-repo-tmpl/{{cookiecutter.repo_name}}' == find_template(repo_dir)

    repo_dir = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        'fake-repo-pre'
    )

    # pre-generating the repo should raise a NonTemplatedInputDirException
    with pytest.raises(NonTemplatedInputDirException):
        find_template(repo_dir)

# Generated at 2022-06-13 18:33:26.900691
# Unit test for function find_template
def test_find_template():
    from cookiecutter import utils
    from cookiecutter.main import cookiecutter
    from unittest import TestCase
    from tempfile import mkdtemp
    import shutil
    import logging

    logger.setLevel(logging.DEBUG)

    class FindTemplateTests(TestCase):

        def setUp(self):
            self.context = {}
            self.test_dir = mkdtemp()
            self.repo_dir = cookiecutter(
                'tests/fake-repo-tmpl/',
                no_input=True,
                context=self.context
            )
            self.repo_dir_contents = os.listdir(self.repo_dir)

        def test_find_template(self):
            json_file = find_template(self.repo_dir)

# Generated at 2022-06-13 18:33:37.788491
# Unit test for function find_template
def test_find_template():
    """Try to find the project template in a sample repo.

    This test repo is the same as the one used in the Cookiecutter docs:
    https://github.com/audreyr/cookiecutter-pypackage

    """
    import os
    import shutil
    from cookiecutter.main import cookiecutter

    project_slug = 'cookiecutter-pypackage'
    clone_to_dir = cookiecutter(
        'https://github.com/audreyr/cookiecutter-pypackage.git',
        no_input=True,
        checkout='0.3.0',
    )
    project_template = find_template(clone_to_dir)


# Generated at 2022-06-13 18:33:41.037944
# Unit test for function find_template
def test_find_template():
    os.path.abspath('/Users/audreyr/cookiecutters/cookiecutter-pypackage')

# find_project_dir
# find_hooks
# find_config

# Generated at 2022-06-13 18:33:49.568306
# Unit test for function find_template
def test_find_template():
    """ Test that the function find_template works correctly."""
    current_dir = os.path.dirname(__file__)
    test_dir = os.path.join(current_dir, os.pardir, 'test-repo-pre')

    # Test that the repo is not empty
    repo_dir_contents = os.listdir(test_dir)
    assert repo_dir_contents, 'The directory is empty.'

    # Test that the template is found in the repo
    assert find_template(test_dir) is not None

    # Test that a NonTemplatedInputDirException is raised if the repo doesn't
    # contain a template
    os.chdir(current_dir)
    empty_dir = os.path.join(current_dir, 'test-empty-dir')

# Generated at 2022-06-13 18:33:55.103238
# Unit test for function find_template
def test_find_template():
    """Test find_template."""
    try:
        find_template('/Users/audreyr/Documents/cookiecutters_do_not_open/academic')
    except NonTemplatedInputDirException as e:
        pass
    else:
        assert False

# Generated at 2022-06-13 18:33:56.955594
# Unit test for function find_template
def test_find_template():
    path = os.path.abspath(os.path.join(
        os.path.dirname(__file__),
        'fake-repo',
        '{{cookiecutter.repo_name}}'
    ))
    assert find_template(os.path.dirname(path)) == path

# Generated at 2022-06-13 18:34:01.321092
# Unit test for function find_template
def test_find_template():
    # Initialize input
    repo_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "tests", "fake-repo")
    # Execute function with input
    output = find_template(repo_dir)
    # Check output
    assert output == os.path.join(repo_dir, '{{cookiecutter.repo_name}}')

# Generated at 2022-06-13 18:34:06.416673
# Unit test for function find_template
def test_find_template():
    # test
    assert find_template('../tests/test-find-repo') == '../tests/test-find-repo/{{cookiecutter.repo_name}}'
    # missing cookiecutter
    assert find_template('../tests/test-find-error') == None

# Generated at 2022-06-13 18:34:12.862899
# Unit test for function find_template

# Generated at 2022-06-13 18:34:26.212641
# Unit test for function find_template
def test_find_template():
    item1 = 'cookiecutter-faux'
    item2 = 'cookiecutter-faux-{{cookiecutter.repo_name}}'
    item3 = 'cookiecutter-faux-demo'
    items = [item1, item2, item3]

    assert find_template(items) == 'cookiecutter-faux-{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:34:29.312882
# Unit test for function find_template
def test_find_template():
    find_template('/Users/Wendy/Desktop/my_cookiecutter/TEST/my_project')


# Generated at 2022-06-13 18:34:29.855261
# Unit test for function find_template
def test_find_template():
    pass

# Generated at 2022-06-13 18:34:31.827230
# Unit test for function find_template
def test_find_template():
    """Verify if the find_template function is working properly."""
    assert find_template("/home/username/cookiecutter") == "Cookiecutter"

# Generated at 2022-06-13 18:34:34.125445
# Unit test for function find_template
def test_find_template():
    """Test find_template function."""
    template_dir = 'tests/test-find-template/fake-repo/{{cookiecutter.repo_name}}'
    assert find_template(os.path.dirname(template_dir)) == template_dir

# Generated at 2022-06-13 18:34:37.341281
# Unit test for function find_template
def test_find_template():
    repo_dir = 'tests/test-repo/fake-repo'
    template = find_template(repo_dir)
    assert template == 'tests/test-repo/fake-repo/{{cookiecutter.repo_name}}'



# Generated at 2022-06-13 18:34:40.507995
# Unit test for function find_template
def test_find_template():
    path = '/Users/jacebrowning/repos/cookiecutter-pypackage'
    assert find_template(repo_dir=path) == os.path.join(path, '{{cookiecutter.project_slug}}')

# Generated at 2022-06-13 18:34:41.194891
# Unit test for function find_template
def test_find_template():
    assert find_template('repo-dir') is None

# Generated at 2022-06-13 18:34:43.606405
# Unit test for function find_template
def test_find_template():
    """Verify function returns expected output."""
    input_dir = os.path.join(os.getcwd(), 'tests/test-find-template')
    expected = os.path.join(input_dir, '{{cookiecutter.repo_name}}')
    assert find_template(input_dir) == expected

# Generated at 2022-06-13 18:34:51.794932
# Unit test for function find_template
def test_find_template():
    """Test function for finding the project template."""
    repo_dir = 'tests/test-repo-tmpl/'
    repo_contents = os.listdir(repo_dir)
    project_template = find_template(repo_dir)

    assert project_template == "/Users/example/cookiecutters/tests/test-repo-tmpl/{{cookiecutter.repo_name}}"
    assert 'test-repo-tmpl' not in repo_contents

test_find_template()

# Generated at 2022-06-13 18:35:09.251374
# Unit test for function find_template
def test_find_template():
    repo_dir = 'tests/fake-repo-pre/'
    project_template = find_template(repo_dir)
    assert project_template == 'tests/fake-repo-pre/{{cookiecutter.project_name}}/'



# Generated at 2022-06-13 18:35:13.128554
# Unit test for function find_template
def test_find_template():
    from cookiecutter.utils.paths import fixture
    repo_dir = fixture('fake_repo_pre_0.7.0')
    template_dir = find_template(repo_dir)
    assert 'fake_project' == os.path.basename(template_dir)


# Generated at 2022-06-13 18:35:24.557140
# Unit test for function find_template
def test_find_template():
    """Verify `find_template` returns a relative path to a directory."""
    base_dir = os.path.abspath(os.path.dirname(__file__))
    repo_dir = os.path.join(base_dir, 'fake-repo')
    project_template = find_template(repo_dir)
    assert os.path.basename(project_template) == '{{cookiecutter.repo_name}}'
    assert os.path.dirname(project_template) == repo_dir
    assert os.path.exists(os.path.join(project_template, 'README.md'))

# Generated at 2022-06-13 18:35:28.565446
# Unit test for function find_template
def test_find_template():
    output = find_template('tests/fake-repo-pre/')
    assert output == 'tests/fake-repo-pre/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:35:31.076518
# Unit test for function find_template
def test_find_template():
    assert find_template('fixtures/fake-repo-pre/') == 'fixtures/fake-repo-pre/{{cookiecutter.repo_name}}'


# Generated at 2022-06-13 18:35:35.083288
# Unit test for function find_template
def test_find_template():
    """Test find_template() for error conditions."""
    import pytest

    with pytest.raises(NonTemplatedInputDirException):
        find_template(repo_dir='tests/fake-repo-pre/')

# Generated at 2022-06-13 18:35:37.852925
# Unit test for function find_template
def test_find_template():
    """Test to find files with {{ and }} in their name and see if they are templates"""
    repo_dir = 'C:\\Users\\Jorge\\Desktop\\Project\\cookiecutter-pypackage'
    template_file = find_template(repo_dir)
    print(template_file)

if __name__ == '__main__':
    test_find_template()

# Generated at 2022-06-13 18:35:41.289988
# Unit test for function find_template
def test_find_template():
    """Verify that find_template returns the correct relative path."""
    assert (find_template('tests/fake-repo-pre/') ==
            'tests/fake-repo-pre/{{cookiecutter.repo_name}}/')

# Generated at 2022-06-13 18:35:48.584126
# Unit test for function find_template
def test_find_template():
    """Verify that find_template function is working as expected."""
    from cookiecutter.main import cookiecutter
    from cookiecutter import utils
    from tempfile import mkdtemp
    from shutil import rmtree

    repo_dir = mkdtemp()

# Generated at 2022-06-13 18:35:54.140331
# Unit test for function find_template
def test_find_template():
    repo_dir = '/home/marcin/Desktop/cookiecutter/cookiecutter-django/tests/test-repo'
    actual_template_path = '/home/marcin/Desktop/cookiecutter/cookiecutter-django/tests/test-repo/{{cookiecutter.repo_name}}'
    assert find_template(repo_dir) == actual_template_path


# Generated at 2022-06-13 18:36:36.204893
# Unit test for function find_template
def test_find_template():
    """Unit test for function find_template"""
    import os
    import shutil
    import tempfile
    from cookiecutter.tests.test_main import remove_dir

    # Create a temporary test directory
    repo_dir = tempfile.mkdtemp()
    template_dir = os.path.join(repo_dir, 'cookiecutter-pypackage')
    os.makedirs(template_dir)
    template_dir = os.path.abspath(template_dir)

    # Find the template
    found_template = find_template(repo_dir)

    # Compare the found template to the one we expect
    assert found_template == template_dir

    # Delete the temporary directory
    remove_dir(repo_dir)

# Generated at 2022-06-13 18:36:39.625820
# Unit test for function find_template
def test_find_template():
    local_repo_dir = os.path.join(os.path.dirname(__file__), '..', 'tests', 'test-find-template')
    project_template = find_template(local_repo_dir)
    expected_project_template = os.path.join(local_repo_dir, 'cookiecutter-{{cookiecutter.repo_name}}')
    assert project_template == expected_project_template

# Generated at 2022-06-13 18:36:42.157445
# Unit test for function find_template
def test_find_template():
    """Verify Cookiecutter can find the project template."""
    repo_dir = 'tests/fake-repo-pre/'
    project_template = 'fake-repo-pre/{{cookiecutter.repo_name}}/'
    assert find_template(repo_dir) == project_template

# Generated at 2022-06-13 18:36:48.908410
# Unit test for function find_template
def test_find_template():
    import tempfile
    from cookiecutter import utils
    from cookiecutter import exceptions


# Generated at 2022-06-13 18:36:54.412858
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.abspath(os.path.join(
        os.path.dirname(__file__),
        '..', '..', 'tests', 'fake-repo', '{{cookiecutter.repo_name}}'))
    assert (
        'fake-repo' in
        find_template(repo_dir)
    )

# Generated at 2022-06-13 18:36:55.586054
# Unit test for function find_template
def test_find_template():
    assert find_template('fixtures/fake-repo') == 'fixtures/fake-repo/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:36:57.992654
# Unit test for function find_template
def test_find_template():
    repo_dir = '/home/audreyr/cookiecutter-pypackage/'
    project_template = find_template(repo_dir)
    assert project_template == '/home/audreyr/cookiecutter-pypackage/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:37:07.325896
# Unit test for function find_template
def test_find_template():
    """Verify that find_template() returns the expected results."""
    assert find_template(
        'tests/test-template/fake-repo-pre/'
    ) == 'tests/test-template/fake-repo-pre/{{cookiecutter.repo_name}}'

    assert find_template(
        'tests/test-template/fake-repo-post/'
    ) == 'tests/test-template/fake-repo-post/{{cookiecutter.repo_name}}'

    assert find_template(
        'tests/test-template/fake-repo-pre-and-post/'
    ) == 'tests/test-template/fake-repo-pre-and-post/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:37:13.656186
# Unit test for function find_template
def test_find_template():
    repo_dir = '/Users/audreyr/Development/cookiecutter-pypackage'
    project_template = '/Users/audreyr/Development/cookiecutter-pypackage/{{cookiecutter.repo_name}}'

    assert find_template(repo_dir) == project_template

# Generated at 2022-06-13 18:37:16.800597
# Unit test for function find_template
def test_find_template():
    """
    Dummy test
    """
    find_te