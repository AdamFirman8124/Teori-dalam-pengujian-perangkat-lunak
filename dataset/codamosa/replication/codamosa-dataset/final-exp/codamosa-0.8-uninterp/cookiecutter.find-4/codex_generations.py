

# Generated at 2022-06-13 18:27:45.035464
# Unit test for function find_template
def test_find_template():
    """Validate ``find_template`` behaves as expected."""
    import shutil
    import tempfile

    # We create a directory hierarchy like:
    # cookiecutter-tmp-test/
    #     fake_template/
    #     other_template/
    #     not_a_template
    #     cookiecutter.json
    fake_template = os.path.join('cookiecutter-tmp-test', 'fake_template')
    other_template = os.path.join('cookiecutter-tmp-test', 'other_template')
    not_a_template = os.path.join('cookiecutter-tmp-test', 'not_a_template')
    cookiecutter_json = os.path.join('cookiecutter-tmp-test', 'cookiecutter.json')

# Generated at 2022-06-13 18:27:46.760693
# Unit test for function find_template
def test_find_template():
    import nose.tools as nt
    nt.assert_equal(
        find_template(''),
        ''
    )

# Generated at 2022-06-13 18:27:52.544873
# Unit test for function find_template
def test_find_template():
    os.getcwd()
    print(find_template('/home/brandon/src/cookiecutter/cookiecutter-pypackage'))

if __name__ == '__main__':
    test_find_template()

# Generated at 2022-06-13 18:27:57.174821
# Unit test for function find_template
def test_find_template():
    expected_result = '/home/audreyr/cookiecutters_do_not_open/jquery/{{cookiecutter.repo_name}}'
    result = find_template('/home/audreyr/cookiecutters_do_not_open/jquery')
    assert expected_result == result

# Generated at 2022-06-13 18:28:05.101507
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        '..', 'tests', 'test-data'
    )
    project_template_dir = os.path.join(repo_dir, 'cookiecutter-django')
    assert find_template(repo_dir) == project_template_dir


# Generated at 2022-06-13 18:28:10.045078
# Unit test for function find_template
def test_find_template():
    """ Ensure the proper template is returned """
    repo_dir = "/tmp/Cookiecutter-pOI1rG"
    assert find_template(repo_dir) == '/tmp/Cookiecutter-pOI1rG/{{cookiecutter.repo_name}}'


# Generated at 2022-06-13 18:28:16.377748
# Unit test for function find_template
def test_find_template():
    """Test finding the template when there is one."""
    import tempfile
    from shutil import rmtree
    from os.path import join
    from cookiecutter.repository import determine_repo_dir
    test_dir = tempfile.mkdtemp()
    os.mkdir(join(test_dir, 'cookiecutter-foobar'))
    os.mkdir(join(test_dir, 'some-other-dir'))
    assert 'cookiecutter-foobar' == \
        os.path.basename(find_template(determine_repo_dir(test_dir)))
    rmtree(test_dir)


# Generated at 2022-06-13 18:28:25.917715
# Unit test for function find_template
def test_find_template():
    from cookiecutter.tests.test_utils import make_empty_dir

    with make_empty_dir() as d:
        with open(os.path.join(d, 'test{{cookiecutter.test}}test'), 'a'):
            pass

        found = find_template(d)

        assert found == os.path.join(
            d,
            'test{{cookiecutter}}test'
        ), "Expected found == %s, got %s" % (os.path.join(
            d,
            'test{{cookiecutter}}test'
        ), found)

# Generated at 2022-06-13 18:28:37.416812
# Unit test for function find_template
def test_find_template():
    """Test find_template function"""
    import shutil
    import tempfile
    import textwrap

    from cookiecutter import utils
    from .compat import OrderedDict

    tmpdir_parent = tempfile.gettempdir()

    # Create temp dir and add a few files
    tmpdir = tempfile.mkdtemp(dir=tmpdir_parent)
    repo_dir = os.path.join(tmpdir, 'cookiecutter-pypackage')
    os.makedirs(repo_dir)
    # Add a project template
    project_template = os.path.join(repo_dir, '{{cookiecutter.project_name}}')
    os.makedirs(project_template)
    # Add a non-template dir

# Generated at 2022-06-13 18:28:40.485024
# Unit test for function find_template
def test_find_template():
    print("Testing for find_template")
    path = '/home/shivani/Desktop/cookiecutter/tests/test-repos/fake-repo-pre/'
    find_template(path)

#Executing the test function for find_template
test_find_template()


# Generated at 2022-06-13 18:28:49.777090
# Unit test for function find_template
def test_find_template():
    """Verify that find_template finds the project directory"""
    test_dir = '/Users/audreyr/cookiecutter-django/tests/fake-repo'
    template_dir = '/Users/audreyr/cookiecutter-django/tests/fake-repo/cookiecutter-django'
    assert find_template(test_dir) == template_dir

# Generated at 2022-06-13 18:28:54.238813
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.join(os.path.dirname(__file__), '../tests/test-input')
    project_template = find_template(repo_dir)
    assert project_template == os.path.join(repo_dir, '{{cookiecutter.repo_name}}')

# Generated at 2022-06-13 18:29:03.737224
# Unit test for function find_template
def test_find_template():
    """ Test find_template function.

    Test cases are:
        Input directory that doesn't contain template
        Input directory that contains template
        Input path that is not a directory
        Input directory that contains subdirectory with template
    """
    # Create directory with template
    import tempfile
    from cookiecutter import utils
    template_dir = tempfile.mkdtemp()
    utils.workaround_git_false_positives_in_dir(template_dir)
    os.mkdir(os.path.join(template_dir, 'my_template'))

    # Create directory with template and subdirectory
    no_template_dir = tempfile.mkdtemp()
    subdir_path = os.path.join(no_template_dir, 'subdir')

# Generated at 2022-06-13 18:29:07.801966
# Unit test for function find_template
def test_find_template():
    repo_dir = '{{ cookiecutter.project_name }}'
    project_template = find_template(repo_dir)
    assert project_template == '{{ cookiecutter.project_name }}'

# Generated at 2022-06-13 18:29:12.250612
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.join('tests','test-find-template','my_project_template')
    project_template = find_template(repo_dir)
    assert project_template==os.path.join(repo_dir, 'my_project_template')

# Generated at 2022-06-13 18:29:21.801385
# Unit test for function find_template
def test_find_template():
    template_dir = os.path.join(
        os.path.dirname(__file__), os.path.pardir, 'tests', 'fake-repo',
    )
    template_dir = os.path.normpath(template_dir)
    template_dir_contents = os.listdir(template_dir)
    assert '{{cookiecutter.repo_name}}' in template_dir_contents

    template_dir_expected = os.path.join(template_dir, '{{cookiecutter.repo_name}}')
    template_dir_actual = find_template(template_dir)

    assert template_dir_actual == template_dir_expected

# Generated at 2022-06-13 18:29:24.835771
# Unit test for function find_template
def test_find_template():
    """Test function to check for find_template functionality"""
    repo_dir = os.path.join('tests', 'fake-repo')
    project_template = find_template(repo_dir)
    expected_template = os.path.join(
        repo_dir, 'fake-project-{{cookiecutter.repo_name}}'
    )

    assert project_template == expected_template

# Generated at 2022-06-13 18:29:31.295342
# Unit test for function find_template
def test_find_template():

    repo_dir = "cookiecutters/python"

    # project_template = None
    # project_template = find_template(repo_dir)

    # assert(project_template == "cookiecutters/python/cookiecutter-pypackage")

# Generated at 2022-06-13 18:29:34.514933
# Unit test for function find_template
def test_find_template():
    """ Verify that the proper path is returned for a templated input directory """
    test_template = '/Users/me/path/to/templates/{{cookiecutter.project_type}}-package'
    repo_dir = '/Users/me/path/to/templates'
    assert find_template(repo_dir) == test_template

# Generated at 2022-06-13 18:29:37.217649
# Unit test for function find_template
def test_find_template():
    from cookiecutter.tests import test_find

    results = find_template(test_find.templated_repo)
    assert results == test_find.templated_repo_path


# Generated at 2022-06-13 18:29:42.752127
# Unit test for function find_template
def test_find_template():
    import tempfile
    from cookiecutter import main

    input_dir = 'fake-repo-tmpl'
    main.cookiecutter(input_dir)

    with tempfile.TemporaryDirectory() as tmpdir:
        output_dir = os.path.join(tmpdir, 'fake-repo')
        main.cookiecutter(input_dir, output_dir=output_dir)
        assert find_template(output_dir) == os.path.join(output_dir, 'fake-repo')

# Generated at 2022-06-13 18:29:49.005309
# Unit test for function find_template
def test_find_template():
    """Test locating the project template."""
    fake_dir_name = 'fake_dir'
    fake_dir = os.path.join(os.path.dirname(__file__), fake_dir_name)

    assert find_template(fake_dir) == os.path.join(fake_dir, 'cookiecutter-{{cookiecutter.repo_name}}')



# Generated at 2022-06-13 18:29:54.767030
# Unit test for function find_template
def test_find_template():
    test_dir = '/Users/audreyr/Code/cookiecutter/tests/test-find-repo'
    t_cookiecutter = os.path.join(test_dir, '{{cookiecutter.repo_name}}')
    assert t_cookiecutter == find_template(test_dir)

# Generated at 2022-06-13 18:30:05.167451
# Unit test for function find_template
def test_find_template():
    """Test for `cookiecutter.find_template` function."""

    from cookiecutter.utils import rmtree

    import shutil
    import tempfile

    repo_dir = None
    temp_dir = tempfile.mkdtemp()

    try:
        repo_dir = os.path.join(temp_dir, 'cookiecutter-pypackage')
        os.makedirs(repo_dir)
        template_dir = os.path.join(repo_dir, '{{cookiecutter.repo_name}}')
        os.makedirs(template_dir)

        template_dir_found = find_template(repo_dir)

    finally:
        if repo_dir:
            rmtree(temp_dir)

    assert template_dir_found == template_dir

# Generated at 2022-06-13 18:30:08.708854
# Unit test for function find_template
def test_find_template():
    test_repo_dir = 'tests/fake-repo/'

    project_template = find_template(test_repo_dir)
    assert 'cookiecutter' in project_template
    assert '{{' in project_template
    assert '}}' in project_template

# Generated at 2022-06-13 18:30:18.172684
# Unit test for function find_template
def test_find_template():
    import shutil
    import tempfile
    import unittest

    class TestFindTemplate(unittest.TestCase):

        def setUp(self):
            self.tmpdir = tempfile.mkdtemp()

        def tearDown(self):
            shutil.rmtree(self.tmpdir)

        def test_find_template(self):
            repo_dir = os.path.join(self.tmpdir, 'fake-repo-7')
            os.mkdir(repo_dir)

            project_template = os.path.join(repo_dir, '{{cookiecutter.project_name}}')
            os.mkdir(project_template)
            self.assertEqual(find_template(repo_dir), project_template)

    unittest.main()

# Generated at 2022-06-13 18:30:19.033931
# Unit test for function find_template
def test_find_template():
    """Test for function find_template."""
    pass

# Generated at 2022-06-13 18:30:30.446127
# Unit test for function find_template
def test_find_template():
    
    # Create and define the test environment
    import os
    import tempfile
    import shutil
    def setUpModule():
        """Prepare the test environment"""
        self.cwd = os.getcwd()
        self.test_dir = tempfile.mkdtemp()
        os.chdir(self.test_dir)

    def tearDownModule():
        """Clean up the test environment"""
        os.chdir(self.cwd)
        shutil.rmtree(self.test_dir)

    # Create a repository for testing
    os.makedirs('test_find_template/test')
    os.makedirs('test_find_template/test/test')
    os.makedirs('test_find_template/test/test/test')

# Generated at 2022-06-13 18:30:36.980030
# Unit test for function find_template
def test_find_template():
    """Find the template directory for a cookiecutter project in a local
    git repository.
    """
    repo_dir = os.path.join(os.path.dirname(__file__),
                            'fake-repo-tmpl')

    project_template = find_template(repo_dir)

    assert project_template == '{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:30:45.066392
# Unit test for function find_template
def test_find_template():
    """Verify that the function `find_template` is working properly."""
    # Create a fake cookiecutter template
    os.chdir(os.path.expanduser('~'))
    repo_dir = os.path.join('fake_repo', 'fake_template')
    os.makedirs(repo_dir)
    with open(os.path.join(repo_dir, 'cookiecutter.json'), 'w') as f:
        f.write('{{cookiecutter}}')
    with open(os.path.join(repo_dir, 'README.md'), 'w') as f:
        f.write('readme')

    project_template = find_template(repo_dir)

    # Verify that find_template returns the correct template

# Generated at 2022-06-13 18:30:51.110059
# Unit test for function find_template
def test_find_template():
    repo_dir = 'tests/fake-repo/'
    project_template = find_template(repo_dir)
    assert project_template == os.path.join(repo_dir, '{{cookiecutter.repo_name}}')



# Generated at 2022-06-13 18:30:52.060208
# Unit test for function find_template
def test_find_template():
    pass

# Generated at 2022-06-13 18:31:02.918078
# Unit test for function find_template
def test_find_template():
    """Ensure that `find_template` returns a valid template."""
    test_dir = os.path.join(os.path.dirname(__file__), 'templates')

    # Test with standard template structure
    template = find_template(test_dir)
    assert template == os.path.join(test_dir, 'test-template'), template

    # Test with no template structure
    test_dir_fake = os.path.join(test_dir, 'no-template-here')
    try:
        find_template(test_dir_fake)
        assert False, 'find_template did not raise exception'
    except NonTemplatedInputDirException:
        pass
    except:
        assert False, 'find_template raised the wrong exception'


# Generated at 2022-06-13 18:31:12.152980
# Unit test for function find_template
def test_find_template():
    """Verify that `find_template` can detect project templates."""
    import os
    import shutil
    import tempfile

    from cookiecutter.exceptions import NonTemplatedInputDirException

    with tempfile.NamedTemporaryFile() as tfile:
        empty_dir = tempfile.mkdtemp()

        # Test for empty directory
        try:
            find_template(empty_dir)
            assert True is False
        except NonTemplatedInputDirException:
            pass

        # Test for non-templated directory
        os.makedirs(os.path.join(empty_dir, 'notemplate'))
        try:
            find_template(empty_dir)
            assert True is False
        except NonTemplatedInputDirException:
            pass

        # Test for templated directory
        template_

# Generated at 2022-06-13 18:31:14.336692
# Unit test for function find_template
def test_find_template():
    repo_dir = '/home/chris/code/template-project/{{cookiecutter.project_name}}'
    assert find_template(repo_dir) == '/home/chris/code/template-project/{{cookiecutter.project_name}}'

# Generated at 2022-06-13 18:31:18.795121
# Unit test for function find_template
def test_find_template():
    """Test the function `find_template`."""
    repo_dir = os.path.join(
        os.getcwd(),
        'tests/test-output/find-template-repo'
    )
    project_template = find_template(repo_dir)
    assert os.path.exists(project_template)
    assert os.path.isdir(project_template)

# Generated at 2022-06-13 18:31:24.461022
# Unit test for function find_template
def test_find_template():
    '''test_find_template'''
    #import unittest
    #class TestFindTemplate(unittest.TestCase):
    #    def test_find_template(self):
    #        assert 'cookiecutter-pypackage' ==
    project_template = find_template('tests/test-data/fake-repo')
    assert 'tests/test-data/fake-repo/{{cookiecutter.repo_name}}' == project_template
    #        assert 'cookiecutter-pypackage' ==

# Generated at 2022-06-13 18:31:28.375100
# Unit test for function find_template
def test_find_template():
    assert find_template('my_project/{{cookiecutter.project_name}}') == 'my_project/{{cookiecutter.project_name}}'


# Generated at 2022-06-13 18:31:31.019813
# Unit test for function find_template

# Generated at 2022-06-13 18:31:36.662205
# Unit test for function find_template
def test_find_template():
    """Check that find_template finds a templated dir."""
    repo_dir = 'tests/fake-repo-tmpl'
    tmpl_dir = find_template(repo_dir)
    assert 'fake-repo-tmpl/{{cookiecutter.repo_name}}' in tmpl_dir

# Generated at 2022-06-13 18:31:41.571717
# Unit test for function find_template
def test_find_template():
    result = find_template('tests/fake-repo-pre/')
    assert result == 'tests/fake-repo-pre/{{cookiecutter.repo_name}}'


# Generated at 2022-06-13 18:31:49.321056
# Unit test for function find_template
def test_find_template():
    # Create mock repo_dir
    repo_dir = '/home/johan/.cookiecutters/cookiecutter-pypackage'

    # Call function to test
    project_template = find_template(repo_dir)

    # Assert result
    assert project_template == '/home/johan/.cookiecutters/cookiecutter-pypackage/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:31:57.039109
# Unit test for function find_template
def test_find_template():
    from tests.test_utils import create_clean_temp_dir

    temp_dir = create_clean_temp_dir()
    test_template = os.path.join(temp_dir, '{{cookiecutter.repo_name}}')
    os.mkdir(test_template)

    project_template = find_template(temp_dir)
    expected_project_template = test_template

    assert project_template == expected_project_template

# Generated at 2022-06-13 18:31:58.271930
# Unit test for function find_template
def test_find_template():
    os.chdir('tests/fake-repo-tmpl')
    assert find_template('.') == './fake-repo-tmpl'
    os.chdir('../..')

# Generated at 2022-06-13 18:32:05.244826
# Unit test for function find_template
def test_find_template():
    """Sample unit test for function find_template.
    """
    root_dir = os.path.abspath(os.path.dirname(__file__))
    template_dir = os.path.join(root_dir, '..', 'fake-repo-tmpl')
    template_path = find_template(template_dir)
    assert template_path == os.path.join(template_dir, 'fake-project-{{cookiecutter.repo_name}}')

# Generated at 2022-06-13 18:32:09.935223
# Unit test for function find_template
def test_find_template():
    """Integration test for finding the project template."""
    repo_dir = os.path.dirname(
        os.path.dirname(
            os.path.dirname(
                os.path.dirname(
                    os.path.abspath(__file__)
                )
            )
        )
    )
    project_template = find_template(repo_dir)
    assert project_template == os.path.join(repo_dir, 'cookiecutter-pypackage')

# Generated at 2022-06-13 18:32:18.099337
# Unit test for function find_template
def test_find_template():
    '''
    Confirm that find_template returns the correct value.
    '''

    assert find_template(os.path.join(
        os.path.dirname(__file__), 'test-workflow/repo')) == os.path.join(
       os.path.dirname(__file__), 'test-workflow/repo/{{cookiecutter.project_name}}')
    assert find_template(os.path.join(
        os.path.dirname(__file__), 'test-workflow/repo-no-variables')) is None

# Generated at 2022-06-13 18:32:20.743448
# Unit test for function find_template
def test_find_template():
    fake_repo_dir = 'tests/fake-repo/'
    assert 'fake-cookiecutter-project' == find_template(fake_repo_dir)

# Generated at 2022-06-13 18:32:24.836151
# Unit test for function find_template
def test_find_template():
    """
    Tests that the function finds the right template.
    """
    template_dir = os.path.join('tests', 'test-find-project-template-expected')
    project_template = find_template(template_dir)
    expected = os.path.join(template_dir, 'cookiecutter-pypackage')
    assert project_template == expected

# Generated at 2022-06-13 18:32:30.399632
# Unit test for function find_template
def test_find_template():
    template_dir = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        '..', 'tests', 'test-template')

    template = find_template(template_dir)
    assert template == os.path.join(template_dir, '{{cookiecutter.repo_name}}')


# Generated at 2022-06-13 18:32:37.843034
# Unit test for function find_template
def test_find_template():
    repo_dir = 'tests/test_repo'
    expected_template = os.path.join(repo_dir, '{{cookiecutter.repo_name}}')
    actual_template = find_template(repo_dir)
    assert actual_template == expected_template


# Generated at 2022-06-13 18:32:48.375545
# Unit test for function find_template
def test_find_template():
    """Verify correct template is found."""
    from cookiecutter import utils
    from cookiecutter.exceptions import NonTemplatedInputDirException

    # Mock, patch
    import os
    from mock import patch
    mock_listdir = patch('os.listdir').start()
    mock_listdir.return_value = [
        'not-the-project-template',
        'so-not-the-project-template',
        'cookiecutter-{{cookiecutter.repo_name}}',
        'also-not-the-project-template',
    ]

    template = utils.find_template('path/to/local/clone')

    assert template == 'path/to/local/clone/cookiecutter-{{cookiecutter.repo_name}}'

    # Reset os.listdir
    patch.stop

# Generated at 2022-06-13 18:32:56.188082
# Unit test for function find_template

# Generated at 2022-06-13 18:33:01.131637
# Unit test for function find_template
def test_find_template():
    REPO_DIR = 'tests/fake-repo-tmpl'
    PROJECT_TEMPLATE = find_template(REPO_DIR)
    assert PROJECT_TEMPLATE == 'tests/fake-repo-tmpl/fake-project-tmpl'

# Generated at 2022-06-13 18:33:10.470053
# Unit test for function find_template
def test_find_template():
    repo_dir = 'fake-repo'
    repo_dir_contents = ['cookiecutter-fake', 'not-template-one', 'not-template-two', 'fake-project-template']
    repo_dir_contents2 = ['not-template-one', 'not-template-two', 'fake-project-template']
    repo_dir_contents3 = ['not-template-one', 'not-template-two']
    project_template = find_template(repo_dir_contents)
    project_template2 = find_template(repo_dir_contents2)
    project_template3 = find_template(repo_dir_contents3)
    assert project_template == 'fake-repo/cookiecutter-fake'

# Generated at 2022-06-13 18:33:13.685389
# Unit test for function find_template
def test_find_template():
    """Tests function find_template."""
    assert find_template('tests/fake-repo-tmpl') == 'tests/fake-repo-tmpl/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:33:19.319539
# Unit test for function find_template
def test_find_template():
    test_dir = os.path.join('tests', 'files', 'project_template')
    assert find_template(test_dir) == os.path.join(test_dir, 'project_name')



# Generated at 2022-06-13 18:33:24.481018
# Unit test for function find_template
def test_find_template():
    assert find_template('/home/bob/cookiecutter-web-jekyll') == '/home/bob/cookiecutter-web-jekyll/cookiecutter-web-jekyll'

# Generated at 2022-06-13 18:33:34.116614
# Unit test for function find_template
def test_find_template():
    """Test ``find_template`` function, symlink scenario."""
    repo_dir = '/my/fake/path/to/repo'
    repo_dir_contents = [
        {'name': '__init__.py', 'is_dir': False},
        {'name': 'README.rst', 'is_dir': False},
        {'name': 'LICENCE', 'is_dir': False},
        {'name': '{{cookiecutter.repo_name}}', 'is_dir': True},
    ]

    assert find_template(repo_dir) == repo_dir_contents[3]['name']



# Generated at 2022-06-13 18:33:38.236995
# Unit test for function find_template
def test_find_template():
    """Test find_template function from finding_template.py"""
    from cookiecutter.find import find_template
    test_dir = 'tests/test-find-project-tmpl'
    result = find_template(test_dir)
    assert result == 'tests/test-find-project-tmpl/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:33:50.329126
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.dirname(__file__)
    project_template = find_template(repo_dir)
    assert project_template == '/home/joncrall/projects/cookiecutter/tests/fake-repo'
    assert os.path.exists(project_template)



# Generated at 2022-06-13 18:33:55.937999
# Unit test for function find_template
def test_find_template():
    repo_dir = 'tests/test-find-template/test-repo'
    project_template = find_template(repo_dir)
    assert project_template == 'tests/test-find-template/test-repo/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:34:01.529859
# Unit test for function find_template
def test_find_template():
    template_dir = os.path.abspath(os.path.join(
        os.path.dirname(__file__),
        '..',
        'tests',
        'fake-repo'
    ))

    expected_template = os.path.abspath(os.path.join(
        template_dir,
        '{{ cookiecutter.repo_name }}'
    ))

    actual_template = find_template(template_dir)

    assert expected_template == actual_template

# Generated at 2022-06-13 18:34:09.757912
# Unit test for function find_template
def test_find_template():
    """Verify that the right project template was found."""
    repo_dir = os.path.abspath(os.path.join(
        os.path.dirname(__file__), '..', '..', 'tests', 'fake-repo', 'input'
    ))

    project_template = find_template(repo_dir)
    assert os.path.abspath(project_template) == os.path.abspath(
        os.path.join(repo_dir, '{{cookiecutter.repo_name}}')
    )

# Generated at 2022-06-13 18:34:17.580945
# Unit test for function find_template
def test_find_template():
    """
    Unit test for function find_template

    :returns: None
    """
    # test find_template function
    import sys
    import shutil
    import tempfile

# Generated at 2022-06-13 18:34:20.107784
# Unit test for function find_template
def test_find_template():
    find_template('/Users/marcdanielberger/projects/cookiecutter/cookiecutter-pypackage')

# Generated at 2022-06-13 18:34:27.916023
# Unit test for function find_template
def test_find_template():
    """Test to see if find_template will detect and return the project template file."""
    testdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    fake_repo = os.path.join(testdir, 'fake-repo')

    try:
        project_template = find_template(fake_repo)
        assert project_template is not None
        assert project_template.endswith('fake-repo/{{cookiecutter.project_name}}')
    except NonTemplatedInputDirException:
        assert False

# Generated at 2022-06-13 18:34:37.442844
# Unit test for function find_template
def test_find_template():
    """Test function for finding template."""
    # Create a temporary directory
    import tempfile
    tmp_dir = tempfile.mkdtemp()

    # Create a repo with a template under it
    repo_dir = os.path.join(tmp_dir, 'my_repo')
    os.mkdir(repo_dir)
    proj_tmpl_dir = os.path.join(repo_dir, '{{cookiecutter.repo_name}}')
    os.mkdir(proj_tmpl_dir)

    # Run the function
    assert(os.path.join(repo_dir, '{{cookiecutter.repo_name}}') == find_template(repo_dir))

    # Clean up
    import shutil
    shutil.rmtree(tmp_dir)

# Generated at 2022-06-13 18:34:44.214318
# Unit test for function find_template
def test_find_template():
    import os
    import shutil
    from cookiecutter import utils

    os.makedirs('tests/files/fake-repo/')
    os.makedirs('tests/files/fake-repo/{{cookiecutter.repo_name}}')
    os.makedirs('tests/files/fake-repo/code')
    project_template = utils.find_template('tests/files/fake-repo')
    assert project_template == 'tests/files/fake-repo/{{cookiecutter.repo_name}}'
    shutil.rmtree('tests/files/fake-repo/')

# Generated at 2022-06-13 18:34:55.765735
# Unit test for function find_template
def test_find_template():
    """Unit test for function find_template"""
    import nose
    import tempfile
    import shutil

    logger.debug('enter test_find_template')

    # create temp dir
    tempdir = tempfile.mkdtemp()

    # create subdir for repo
    temprepo = os.path.join(tempdir, 'testrepo')
    os.mkdir(temprepo)

    # create subdir with template
    templatedir = os.path.join(temprepo, 'templatedir')
    os.mkdir(templatedir)

    # create subdir without template
    nontemplatedir = os.path.join(temprepo, 'nontemplatedir')
    os.mkdir(nontemplatedir)

    # run find_template

# Generated at 2022-06-13 18:35:02.289000
# Unit test for function find_template
def test_find_template():
    pass

# Generated at 2022-06-13 18:35:07.670328
# Unit test for function find_template
def test_find_template():
    """Verify find_template function raises exception in empty dir."""
    try:
        find_template('/tmp/__test_cookiecutter__/')
        assert False, 'Exception should be raised if no Cookiecutter template ' \
                      'is found in the repository.'
    except NonTemplatedInputDirException:
        assert True

# Generated at 2022-06-13 18:35:10.122524
# Unit test for function find_template
def test_find_template():
    test_dir = "/Users/mario/dev/cookiecutter/tests/test-find-template"
    assert find_template(test_dir) == "/Users/mario/dev/cookiecutter/tests/test-find-template/cookiecutter-pypackage"

# Generated at 2022-06-13 18:35:19.727769
# Unit test for function find_template
def test_find_template():
    '''
    Unit tests for find_template.
    '''
    # Create a directory with a template in it and see if find_template picks it up
    import tempfile
    import shutil
    repo_name = 'Some-repo'
    repo_dir = tempfile.mkdtemp()
    project_template = os.path.join(repo_name, '{{cookiecutter.repo_name}}')

    # Create the directory with the template name
    os.makedirs(os.path.join(repo_dir, project_template))
    os.makedirs(os.path.join(repo_dir, 'foo'))
    os.makedirs(os.path.join(repo_dir, 'bar'))
    template_dir = find_template(repo_dir)
    assert template_

# Generated at 2022-06-13 18:35:25.697336
# Unit test for function find_template
def test_find_template():
    """Test the find_template function."""
    logger = logging.getLogger(__name__)
    repo_dir = '{{cookiecutter.repo_name}}'

    find_template(repo_dir)
    assert repo_dir == '{{cookiecutter.repo_name}}'


# Generated at 2022-06-13 18:35:35.749506
# Unit test for function find_template
def test_find_template():
    with open('test_find_template/test_input.txt') as f:
        test_input_dirs = f.read().splitlines()

    with open('test_find_template/test_output.txt') as f:
        test_output_dirs = f.read().splitlines()

    with open('test_find_template/test_error.txt') as f:
        test_error_dirs = f.read().splitlines()

    for i, test_input in enumerate(test_input_dirs):
        if test_input in test_error_dirs:
            try:
                logger.info('Expecting a NonTemplatedInputDirException')
                find_template(test_input)
            except NonTemplatedInputDirException as e:
                logger.debug(e)
        else:
            expected

# Generated at 2022-06-13 18:35:40.102396
# Unit test for function find_template
def test_find_template():
    repo_dir = './tests/fake-repo'
    project_template = find_template(repo_dir)
    assert project_template == './tests/fake-repo/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:35:51.695119
# Unit test for function find_template
def test_find_template():

    # First test
    # Create a repo dir and make it the current working dir
    os.mkdir('fake_repo_dir')
    os.chdir('fake_repo_dir')
    # Create a fake cookiecutter template dir and make it the current working dir
    os.mkdir('fake-{{cookiecutter.repo_name}}-dir')
    os.chdir('fake-{{cookiecutter.repo_name}}-dir')
    find_template(os.path.join(os.getcwd(), os.pardir))
    os.chdir(os.path.join(os.getcwd(), os.pardir))
    os.chdir(os.path.join(os.getcwd(), os.pardir))

    # Second Test

# Generated at 2022-06-13 18:35:56.983348
# Unit test for function find_template
def test_find_template():
    """
    Test if find_template function works as expected
    """
    import pytest
    from cookiecutter import prompt

    answers = prompt.prompt_for_config(
        context_file='../cookiecutter-pypackage',
    )

    with pytest.raises(NonTemplatedInputDirException):
        find_template('tests/test-find-template')

    find_template('tests/test-find-template-templated')

# Generated at 2022-06-13 18:36:01.392346
# Unit test for function find_template
def test_find_template():
    from ..repository import get_repo
    repo_dir = get_repo('https://github.com/pytest-dev/cookiecutter-pytest-plugin.git')
    result = find_template(repo_dir)
    assert result == repo_dir

# Generated at 2022-06-13 18:36:18.196094
# Unit test for function find_template
def test_find_template():
    """Test the find_template function by using it on a test template."""
    test_template_directory = os.path.join("tests", "test-templates", "fake-repo-pre-render")
    result = find_template(test_template_directory)
    assert os.path.normpath(result) == os.path.normpath("tests/test-templates/fake-repo-pre-render/{{cookiecutter.repo_name}}")

# Generated at 2022-06-13 18:36:20.022508
# Unit test for function find_template
def test_find_template():
    repo_dir = '/my/repo/dir'
    find_template(repo_dir)

# Generated at 2022-06-13 18:36:23.316668
# Unit test for function find_template
def test_find_template():
    assert find_template('/Users/marilyn/Documents/code/cookiecutter/tests') == '/Users/marilyn/Documents/code/cookiecutter/tests/cookiecutter-pypackage-tests'

# Generated at 2022-06-13 18:36:31.568040
# Unit test for function find_template
def test_find_template():
    """Verify function can find the project template in a directory."""
    from cookiecutter import utils
    from cookiecutter.exceptions import NonTemplatedInputDirException

    tests_dir = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        '..',
        'tests',
        'files',
        'test-repo'
    )

    project_template = utils.find_template(tests_dir)
    assert project_template == os.path.join(tests_dir, '{{cookiecutter.repo_name}}')

    with pytest.raises(NonTemplatedInputDirException):
        utils.find_template('/some/bogus/directory')


# Generated at 2022-06-13 18:36:35.758711
# Unit test for function find_template
def test_find_template():
    test_dir_contents = ['test_item', 'cookiecuttertest{{test}}test']
    assert find_template(test_dir_contents) == \
        os.path.join(test_dir_contents, test_dir_contents[1])


# Generated at 2022-06-13 18:36:38.518361
# Unit test for function find_template
def test_find_template():
    data_dir = 'tests/test-find-template'
    repo_dir = '/home/audreyr/cookiecutter-pypackage/'
    project_template = find_template(repo_dir)
    assert project_template == '/home/audreyr/cookiecutter-pypackage/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:36:44.358877
# Unit test for function find_template
def test_find_template():
    # Test 1
    repo_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        '..',
        'tests',
        'test-input-repo',
    )
    result = find_template(repo_dir)
    expected_output = os.path.join(repo_dir, '{{cookiecutter.repo_name}}')
    assert result == expected_output

    # Test 2
    repo_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        '..',
        'tests',
        'test-input-two-templates',
    )
    result = find_template(repo_dir)
    # The one chosen should be the first one that contains

# Generated at 2022-06-13 18:36:50.999434
# Unit test for function find_template
def test_find_template():
    from cookiecutter.main import cookiecutter
    from shutil import rmtree
    from . import modified_searchpath
    from . import tempdir
    from . import UNICODE_TEXT

    context = {
        'full_name': 'Test Cookiecutter',
        'project_name': 'Project Name',
        'repo_name': 'cookiecutter-project-name'
    }
    tmp_dir = os.path.abspath(tempdir.tempdir())
    template = 'https://github.com/audreyr/cookiecutter-pypackage.git'
    # Use original searchpath instead of modified one to avoid
    # Conflict between local and repo being tested
    cookiecutter(template, context, no_input=True, overwrite_if_exists=True, output_dir=tmp_dir)
   

# Generated at 2022-06-13 18:36:58.503735
# Unit test for function find_template
def test_find_template():
    test_repo_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'tests',
        'fake-repo-pre'))
    test_repo_dir = os.path.normpath(test_repo_dir)
    logger.debug('test_repo_dir is %s.', test_repo_dir)
    project_template = find_template(test_repo_dir)
    assert project_template == os.path.join(
        test_repo_dir,
        '{{cookiecutter.repo_name}}'
    )

# Generated at 2022-06-13 18:37:06.522900
# Unit test for function find_template
def test_find_template():
    """Verify find_template() function."""
    import tempfile
    import shutil
    import sys

    repo_dir = os.path.join('tests', 'fake-repo-pre-render')
    fake_dir = tempfile.mkdtemp()
    try:
        shutil.copytree(repo_dir, fake_dir)
        project_template = find_template(fake_dir)
        assert project_template == os.path.join(fake_dir, 'fake-{{cookiecutter.repo_name}}-pre-render')
    finally:
        shutil.rmtree(fake_dir)