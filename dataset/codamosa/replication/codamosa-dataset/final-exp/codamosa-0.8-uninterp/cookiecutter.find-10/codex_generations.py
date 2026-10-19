

# Generated at 2022-06-13 18:27:38.436595
# Unit test for function find_template
def test_find_template():
    template_dir = 'tests/files/fake-repo-pre/'
    result = find_template(template_dir)
    assert result == 'tests/files/fake-repo-pre/{{cookiecutter.repo_name}}'



# Generated at 2022-06-13 18:27:46.050299
# Unit test for function find_template
def test_find_template():
    """Test function 'find_template'."""
    import pytest

    template_str = 'templatetemplate'
    repo_dir = 'tests/' + template_str + '/'
    os.makedirs(repo_dir)
    os.makedirs(repo_dir + 'template{{cookiecutter.repo_name}}')
    os.makedirs(repo_dir + template_str)
    os.makedirs(repo_dir + 'Template')
    os.makedirs(repo_dir + 'template_random')
    os.makedirs(repo_dir + 'package')
    os.makedirs(repo_dir + 'template')
    os.makedirs(repo_dir + 'Cookiecutter')


# Generated at 2022-06-13 18:27:49.631869
# Unit test for function find_template
def test_find_template():
    assert find_template('test') == 'test/test_cookiecutter-{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:27:53.086085
# Unit test for function find_template
def test_find_template():
    find_test = find_template('test/test_repo/')
    assert find_test == 'test/test_repo/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:28:02.773992
# Unit test for function find_template
def test_find_template():
    import tempfile
    import shutil

    test_dir = tempfile.mkdtemp()
    normal_dir = os.path.join(test_dir, 'normal')
    os.mkdir(normal_dir)
    template_dir = os.path.join(test_dir, '{{cookiecutter.repo_name}}')
    os.mkdir(template_dir)

    result = find_template(test_dir)
    assert result == template_dir

    shutil.rmtree(test_dir)



# Generated at 2022-06-13 18:28:14.256384
# Unit test for function find_template
def test_find_template():
    """ Test find template function if it returns the correct directory and 
    handles exception correctly.
    """
    from nose.tools import assert_equal, assert_raises
    import os

    # Get the path to the test template and the non-templated directory
    path = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(path, 'fixtures/fake-repo-tmpl')
    path_non_templated = os.path.join(path, 'non-templated')

    # Get the paths to both the templated and non-templated directories
    project_template = find_template(path)
    project_template_non_templated = find_template(path_non_templated)

    # Check if the returned template is the same for the

# Generated at 2022-06-13 18:28:19.268378
# Unit test for function find_template
def test_find_template():
    """Find project template in local directory."""
    assert find_template('tests/test-repo-pre/') == \
        os.path.abspath('tests/test-repo-pre/{{cookiecutter.repo_name}}')



# Generated at 2022-06-13 18:28:26.314173
# Unit test for function find_template
def test_find_template():
    """Test finding a project template inside a cookiecutter project."""
    this_dir = os.path.dirname(__file__)
    repo_dir = os.path.join(this_dir, 'fake-repo-pre')
    project_template = find_template(repo_dir)
    expected_output = os.path.join(repo_dir, '{{cookiecutter.repo_name}}')
    assert project_template == expected_output

# Generated at 2022-06-13 18:28:31.850152
# Unit test for function find_template
def test_find_template():
    """Verify that the project template is correctly located."""
    repo_dir = 'fake-repo/{{cookiecutter.repo_name}}'
    project_template = find_template(repo_dir)
    assert project_template == 'fake-repo/{{cookiecutter.repo_name}}'


# Generated at 2022-06-13 18:28:32.787071
# Unit test for function find_template
def test_find_template():
    pass

# Generated at 2022-06-13 18:28:44.577515
# Unit test for function find_template
def test_find_template():
    """Test for function find_template."""
    import sys, os
    import pkg_resources
    from cookiecutter import utils
    from cookiecutter.exceptions import NonTemplatedInputDirException

    cookiecutters_dir = pkg_resources.resource_filename(
        'cookiecutter', 'cookiecutters'
    )
    cookiecutter_django = os.path.join(
        cookiecutters_dir, 'cookiecutter-django'
    )

    # dir has {{ cookiecutter.project_name }}
    repo_dir = os.path.join(cookiecutter_django, '{{ cookiecutter.repo_name }}')

# Generated at 2022-06-13 18:28:46.949335
# Unit test for function find_template

# Generated at 2022-06-13 18:28:55.345884
# Unit test for function find_template
def test_find_template():
    """Test find_template() for expected behavior."""
    from cookiecutter import utils
    from cookiecutter import exceptions

    # Create a fake repo with folders
    cc_dir = os.path.abspath(os.path.dirname(__file__))
    tests_dir = os.path.dirname(cc_dir)
    fake_dir = os.path.join(
        tests_dir, 'fake-repo-pre'
    )
    fake_template_dir = os.path.join(
        fake_dir, 'fake-project-{{cookiecutter.repo_name}}'
    )

    # This should return the template dir
    output_dir = utils.find_template(fake_dir)
    assert output_dir == fake_template_dir

    # Make sure NonTemplatedInputDirException is

# Generated at 2022-06-13 18:29:03.925465
# Unit test for function find_template
def test_find_template():
    """Ensure find_template is properly searching for a repo"""
    #Normal
    test_dir = os.path.join('tests', 'input', 'repo_with_dir')
    project_template = find_template(test_dir)
    assert project_template == os.path.join(test_dir, '{{cookiecutter.repo_name}}')
    #Non-templated
    test_dir = os.path.join('tests', 'input', 'repo_without_dir')
    project_template = find_template(test_dir)
    assert project_template == os.path.join(test_dir, 'cookiecutter-pypackage')
    #No directory
    test_dir = os.path.join('tests', 'input', 'repo_without_any_dir')
    project_template = find

# Generated at 2022-06-13 18:29:15.799908
# Unit test for function find_template
def test_find_template():
    """
    Test that it can find the project template
    """
    import tempfile
    import shutil
    import os

    repo_dir = tempfile.mkdtemp()

    os.mkdir(os.path.join(repo_dir, 'something'))
    os.mkdir(os.path.join(repo_dir, 'cookiecutter-something'))
    os.mkdir(os.path.join(repo_dir, 'cookiecutter-{{something}}'))
    os.mkdir(os.path.join(repo_dir, '{{cookiecutter.project_name}}'))

    project_template = find_template(repo_dir)
    assert project_template == os.path.join(repo_dir, '{{cookiecutter.project_name}}')

    shutil.rmt

# Generated at 2022-06-13 18:29:20.003517
# Unit test for function find_template
def test_find_template():
    import pytest
    from cookiecutter.utils.paths import ensure_dir
    from tempfile import mkdtemp

    temp_dir = mkdtemp()
    ensure_dir(os.path.join(temp_dir, '{{cookiecutter.repo_name}}'))
    template_path = find_template(temp_dir)
    assert os.path.join(temp_dir, '{{cookiecutter.repo_name}}') == template_path

    # Test for exception
    with pytest.raises(NonTemplatedInputDirException):
        template_path = find_template('/')

    # Clean up
    shutil.rmtree(temp_dir)

# Generated at 2022-06-13 18:29:25.096288
# Unit test for function find_template
def test_find_template():
    repo_dir = '/Users/audreyr/cookiecutter-pypackage'
    project_template = find_template(repo_dir)
    assert project_template == '/Users/audreyr/cookiecutter-pypackage/{{cookiecutter.repo_name}}'

if __name__ == '__main__':
    test_find_template()

# Generated at 2022-06-13 18:29:29.980838
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        '..',
        '..',
        'cookiecutter-pypackage'
    )
    template = find_template(repo_dir)
    assert template == os.path.join(
        repo_dir,
        '{{cookiecutter.repo_name}}',
    )

# Generated at 2022-06-13 18:29:35.605049
# Unit test for function find_template
def test_find_template():
    """Verify find_template function works properly."""
    test_dir = os.path.join(os.path.dirname(__file__), '..',
                            'tests/test-output/input', 'test_pattern')

    expected_dir = os.path.join(test_dir, '{{cookiecutter.project_slug}}')
    assert find_template(test_dir) == expected_dir

# Generated at 2022-06-13 18:29:38.073909
# Unit test for function find_template
def test_find_template():
    """Verify that find_template() finds the project template in a repo."""
    pass

# Generated at 2022-06-13 18:29:40.329037
# Unit test for function find_template
def test_find_template():
    pass



# Generated at 2022-06-13 18:29:52.781814
# Unit test for function find_template
def test_find_template():
    """Test `find_template` using a fake Git repo."""
    try:
        from tests.test_utils import make_fake_repo
    except (ImportError, SyntaxError):
        logger.debug('Skipping test_find_template tests')
    else:
        logger.debug('Testing `find_template` function')

        template_dir = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            'fake-repo'
        )

        repo_dir = make_fake_repo(template_dir)

        assert find_template(template_dir) == os.path.join(
            repo_dir,
            '{{cookiecutter.repo_name}}'
        )

# Generated at 2022-06-13 18:30:03.630956
# Unit test for function find_template
def test_find_template():
    """
    Simple unit test, not 100% comprehensive but covers all paths
    """
    os.mkdir(os.getcwd() + "/foo")
    os.mkdir(os.getcwd() + "/foo/bar")
    os.mkdir(os.getcwd() + "/foo/corge")
    os.mkdir(os.getcwd() + "/foo/garply")
    open(os.getcwd() + "/foo/README", 'w').close()
    open(os.getcwd() + "/foo/foo.txt", 'w').close()
    open(os.getcwd() + "/foo/bar/README", 'w').close()
    open(os.getcwd() + "/foo/bar/foo.txt", 'w').close()

# Generated at 2022-06-13 18:30:04.460575
# Unit test for function find_template
def test_find_template():
    pass

# Generated at 2022-06-13 18:30:06.323672
# Unit test for function find_template
def test_find_template():
    assert find_template('.') == './{{cookiecutter.repo_name}}'


# Generated at 2022-06-13 18:30:17.603314
# Unit test for function find_template
def test_find_template():
    from unittest import TestCase
    import tempfile
    import shutil
    import os
    from cookiecutter.utils import rmtree
    from cookiecutter.utils import ensure_dir
    from cookiecutter.utils import work_in
    from cookiecutter.utils import make_sure_path_exists

    class TestFindTemplate(TestCase):

        def setUp(self):
            self.base_dir = tempfile.mkdtemp()
            self.clone_dir = os.path.join(self.base_dir, 'fake-repo')
            self.repo_dir = os.path.join(self.base_dir, 'fake-repo', '{{ cookiecutter.repo_name }}')
            make_sure_path_exists(self.repo_dir)


# Generated at 2022-06-13 18:30:23.104275
# Unit test for function find_template
def test_find_template():
    """Test that the function find_template works."""
    test_path = os.path.join(os.getcwd(), 'tests', 'files', 'cookiecutter-templated')
    assert find_template(test_path) == os.path.join(test_path, '{{cookiecutter.repo_name}}')

# Generated at 2022-06-13 18:30:27.578518
# Unit test for function find_template
def test_find_template():
    assert find_template(os.path.join('tests', 'fake-repo-pre-AB')) == os.path.join('tests', 'fake-repo-pre-AB', '{{cookiecutter.repo_name}}')

# Generated at 2022-06-13 18:30:35.773222
# Unit test for function find_template
def test_find_template():
    """Verify find_template."""
    from cookiecutter.tests.test_utils import template_folder
    # setup
    template_folder = template_folder()
    os.chdir(template_folder)
    # test
    result = find_template(template_folder)
    # assert
    assert result == os.path.abspath(os.path.join(template_folder, '{{cookiecutter.repo_name}}'))


# Generated at 2022-06-13 18:30:43.637940
# Unit test for function find_template
def test_find_template():
    """
    The test file is a copy of the actual input directory and the actual
    template directory.
    """
    logger.debug('Unit testing find_template()')

    # test_repo_dir = os.path.abspath(
    test_repo_dir = os.path.abspath(
        os.path.join(os.path.dirname(os.path.realpath(__file__)),
                     'tests/fake-repo-pre-normalize/{{cookiecutter.repo_name}}'))
    test_project_template = os.path.join(
        test_repo_dir,
        'tests/fake-repo-pre-normalize/{{cookiecutter.repo_name}}'
    )

    # The result here depends on platform. We can't rely on os.path.se

# Generated at 2022-06-13 18:30:47.956425
# Unit test for function find_template
def test_find_template():
    """Validate that find_template() returns an expected value"""
    repo_dir = os.path.join('tests', 'test-checkout-input')
    answer = os.path.join(repo_dir, 'cookiecutter-pypackage')
    assert find_template(repo_dir) == answer

# Generated at 2022-06-13 18:31:01.097096
# Unit test for function find_template
def test_find_template():
    """Verify find_template function."""
    # Create a new directory and write some files
    import tempfile
    repo_dir = tempfile.mkdtemp()
    with open(os.path.join(repo_dir, 'cookiecutter.json'), 'w') as f:
        f.write('this is a fake cookiecutter.json')
    with open(os.path.join(repo_dir, 'README'), 'w') as f:
        f.write('this is a fake README')
    # Test function
    template_dir = find_template(repo_dir)
    assert template_dir == repo_dir
    # Get rid of the temp files
    os.remove(os.path.join(repo_dir, 'cookiecutter.json'))

# Generated at 2022-06-13 18:31:05.563456
# Unit test for function find_template
def test_find_template():
    import tempfile
    import shutil
    import os.path

    template_dir = tempfile.mkdtemp()
    try:
        os.mkdir(os.path.join(template_dir, 'cookiecutter-foobar'))
        assert 'cookiecutter-foobar' == find_template(template_dir)
    finally:
        shutil.rmtree(template_dir)


# Generated at 2022-06-13 18:31:12.904499
# Unit test for function find_template
def test_find_template():
    """Test find_template."""
    # try:
    #     import pytest
    # except ImportError:
    #     return
    #
    # import os
    # from cookiecutter import find
    #
    # @pytest.fixture(scope='function', autouse=True)
    # def cleanup_dir(request):
    #     os.chdir(os.path.expanduser('~'))
    #
    # def test_find_template_non_repo(monkeypatch):
    #     monkeypatch.chdir(os.path.expanduser('~'))
    #     with pytest.raises(NonTemplatedInputDirException):
    #         find.find_template(os.path.expanduser('~'))
    #
    # def test_find_template(monkeypatch):

# Generated at 2022-06-13 18:31:21.087778
# Unit test for function find_template
def test_find_template():
    """
    Test find a template in a new repository.
    """
    from cookiecutter.tests.test_find_no_input_dir import _clean_up
    from cookiecutter.tests.test_find_no_input_dir import _create_repo
    from cookiecutter.tests.test_find_no_input_dir import _assert_repo_contents

    repo_dir, template = _create_repo('tests/test-find-input')
    find_template(repo_dir)
    _assert_repo_contents(repo_dir, template)
    _clean_up(repo_dir)

if __name__ == "__main__":
    test_find_template()

# Generated at 2022-06-13 18:31:25.440237
# Unit test for function find_template
def test_find_template():
    """Verify that function find_template returns correct directory."""
    this_dir = os.path.abspath(os.path.dirname(__file__))
    fixture = os.path.join(this_dir, 'tests', 'fixtures', 'fake-repo')
    expected = os.path.join(fixture, '{{cookiecutter.project_slug}}')
    project_template = find_template(fixture)
    assert project_template == expected

# Generated at 2022-06-13 18:31:30.591743
# Unit test for function find_template
def test_find_template():
    repo_dir = "C:/Users/Brazos/Desktop/Cookie-Cutter/"

    project_template = find_template(repo_dir)
    assert type(project_template) == str
    logger.info(project_template)

# Generated at 2022-06-13 18:31:41.654363
# Unit test for function find_template
def test_find_template():
    """Unit test for function find_template."""
    from tempfile import mkdtemp
    from shutil import rmtree
    from cookiecutter import repository

    test_repo_dir = mkdtemp()
    test_repo = get_test_repo()
    test_repo.clone(test_repo_dir)

    test_project_template = find_template(test_repo_dir)

    test_project_template = os.path.join(test_project_template, 'cookiecutter.json')
    assert os.path.exists(test_project_template)

    assert repository.validate_repo(test_repo_dir)

    rmtree(test_repo_dir)


# Generated at 2022-06-13 18:31:55.904800
# Unit test for function find_template
def test_find_template():
    from cookiecutter import find
    from cookiecutter import utils
    from cookiecutter.exceptions import NonTemplatedInputDirException
    from unittest import TestCase
    
    class TestFindTemplate(TestCase):
        """Unit tests for `find.find_template`."""
        
        def setUp(self):
            self.test_dir = os.path.dirname(os.path.abspath(__file__))
            self.repo_dir = os.path.join(self.test_dir, 'fake-repo-pre')
            self.repo_dir_non_templated = os.path.join(self.test_dir, 'fake-repo-no-templated-dir')
            

# Generated at 2022-06-13 18:32:03.578848
# Unit test for function find_template
def test_find_template():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    repo_dir = os.path.abspath(os.path.join(base_dir, 'fake-repo'))
    expected = os.path.abspath(os.path.join(base_dir, 'fake-repo', 'fake{{cookiecutter.repo_name}}'))

    assert find_template(repo_dir) == expected


# Generated at 2022-06-13 18:32:08.072893
# Unit test for function find_template
def test_find_template():
    return find_template('/Users/justin/Repositories/cookiecutter-r')

# Generated at 2022-06-13 18:32:17.650458
# Unit test for function find_template
def test_find_template():
    """Verify expected behavior of the find_template function.
    """
    # Setup
    repo_dir = os.path.abspath(os.path.join(
        os.path.dirname(__file__),
        os.pardir,
        os.pardir,
        os.pardir,
        'tests',
        'test-repo-pre'
    ))

    # Exercise
    project_template = find_template(repo_dir)


# Generated at 2022-06-13 18:32:25.195825
# Unit test for function find_template
def test_find_template():
    import os
    from cookiecutter import utils

    tests = os.path.join(os.path.join(os.path.dirname(__file__), 'tests'))

    repo_dir_contents = os.listdir(tests)

    project_template = None
    for item in repo_dir_contents:
        if 'cookiecutter' in item and '{{' in item and '}}' in item:
            project_template = item
            break

    project_template = os.path.join(os.path.join(os.path.dirname(__file__), 'tests'), project_template)
    assert utils.find_template(tests) == project_template

# Generated at 2022-06-13 18:32:27.584110
# Unit test for function find_template
def test_find_template():
    """Unit test for find_template function."""
    find_template('/Users/audreyr/code/cookiecutter-pypackage')

# Generated at 2022-06-13 18:32:36.188624
# Unit test for function find_template
def test_find_template():
    from cookiecutter import repo
    from cookiecutter.utils import rmtree
    from cookiecutter.exceptions import NonTemplatedInputDirException

    repo_dir = repo.clone("https://github.com/audreyr/cookiecutter-pypackage.git")
    project_template = find_template(repo_dir)

    assert '{{cookiecutter.project_name}}' in project_template

    rmtree(repo_dir)

    # Now test that it raises an error with a bad repo
    repo_dir = repo.clone("https://github.com/tbenthompson/bad-cookiecutter-test.git")
    try:
        find_template(repo_dir)
    except NonTemplatedInputDirException:
        # Success
        pass
    except:
        raise Assert

# Generated at 2022-06-13 18:32:41.488144
# Unit test for function find_template
def test_find_template():
    from .repository import make_repo_dir
    from cookiecutter.utils import rmtree

    repo_dir = make_repo_dir('tests/fake-repo-pre/')
    repo_dir = os.path.abspath(repo_dir)
    try:
        template = find_template(repo_dir)
    finally:
        rmtree(repo_dir)

    assert template == os.path.join(repo_dir, 'fake-project-template')

# Generated at 2022-06-13 18:32:43.854635
# Unit test for function find_template
def test_find_template():
    import os
    template_dir = os.path.join(os.path.dirname(__file__), 'test-template')
    template_name = find_template(template_dir)
    assert template_name == os.path.join(template_dir, 'test-template')

# Generated at 2022-06-13 18:32:46.462288
# Unit test for function find_template
def test_find_template():
    t = find_template('test')
    assert t == 'test/test'

# Generated at 2022-06-13 18:32:55.511472
# Unit test for function find_template
def test_find_template():
    """Test finding a directory with a project template."""
    import shutil
    import tempfile

    template_dir = tempfile.mkdtemp()

    test_dirs = [
        os.path.join(template_dir, 'my-awesome-project-template'),
        os.path.join(template_dir, 'test_test'),
    ]

    cookies = ['vegan', 'chocolate', 'peanutbutter']


# Generated at 2022-06-13 18:32:56.950153
# Unit test for function find_template
def test_find_template():
    """ Verify find_template() """
    find_template('tests/fake-repo-templated')
    find_template('tests/fake-repo-pre/')


# Generated at 2022-06-13 18:33:05.343491
# Unit test for function find_template
def test_find_template():
    """
    Test the find_template function for correct behavior.
    """
    assert find_template('tests/test-repo-pre/') == 'tests/test-repo-pre/{{cookiecutter.repo_name}}/'
    assert find_template('tests/test-repo-post/') == 'tests/test-repo-post/'



# Generated at 2022-06-13 18:33:08.061700
# Unit test for function find_template
def test_find_template():
    from cookiecutter import utils
    utils.find_template('tests/test-repo-pre/')

# Generated at 2022-06-13 18:33:15.251527
# Unit test for function find_template
def test_find_template():
    assert find_template('tests/test-repo-pre/') == 'tests/test-repo-pre/{{cookiecutter.repo_name}}/'
    assert find_template('tests/test-repo-post/') == 'tests/test-repo-post/{{cookiecutter.repo_name}}/'
    assert find_template('tests/test-repo-pre/tests/test-repo-post/') == 'tests/test-repo-pre/tests/test-repo-post/{{cookiecutter.repo_name}}/'

# Generated at 2022-06-13 18:33:20.383536
# Unit test for function find_template
def test_find_template():
    """Verify that find_template looks in the right places."""
    import tempfile

    repo_dir = tempfile.mkdtemp()


# Generated at 2022-06-13 18:33:28.437955
# Unit test for function find_template
def test_find_template():
    """Test find_template function."""
    repo_dir = '/Users/test/test_project'
    repo_dir_contents = [
        'cookiecutter-pypackage',
        'cookiecutter-pyramid',
        'cookiecutter-django',
        'cookiecutter-flask',
        'cookiecutter-mkdir',
        'cookiecutter-tox-travis'
    ]
    for item in repo_dir_contents:
        os.makedirs('/Users/test/test_project/' + item)
    assert find_template(repo_dir) == '/Users/test/test_project/cookiecutter-mkdir'

# Generated at 2022-06-13 18:33:38.760960
# Unit test for function find_template
def test_find_template():
    from mock import patch, Mock
    from pytest import raises
    from cookiecutter import find

    mock_repo_dir = Mock()
    mock_repo_dir_contents = Mock()
    mock_repo_dir_contents.__iter__.return_value = ['something', 'cookiecutter-something-{{something-else}}']

    mock_repo_dir.__iter__.return_value = mock_repo_dir_contents

    with patch('cookiecutter._os.path.exists') as mock_path_exists, \
         patch('cookiecutter.find.os.walk') as mock_walk, \
         patch('cookiecutter.find.os.listdir') as mock_listdir:

        mock_path_exists.return_value = True

# Generated at 2022-06-13 18:33:44.841729
# Unit test for function find_template
def test_find_template():
    """Ensure the find_template function works properly."""
    template_dir = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        'test-data',
        'fake-repo'
    )
    assert find_template(template_dir) == os.path.join(
            template_dir,
            '{{cookiecutter.repo_name}}'
    )

# Generated at 2022-06-13 18:33:50.652240
# Unit test for function find_template
def test_find_template():
    """Test to check if the template is found"""
    repo_dir = os.path.abspath('../cookiecutter/tests/fake-repo-pre/')
    project_template = find_template(repo_dir)
    expected_template = 'fake-repo-pre/{{cookiecutter.repo_name}}'
    assert project_template == expected_template

# Generated at 2022-06-13 18:34:01.415042
# Unit test for function find_template
def test_find_template():
    """ Unit test for function find_template """
    # Test if we can find the template
    repo_dir = "cookiecutter/tests/test-input/fake-repo-tmpl"
    project_template = find_template(repo_dir)
    assert "fake-project-tmpl" in project_template
    assert os.path.isdir(project_template)

    # Test if exceptions are raised correctly when the template dir is missing
    repo_dir_no_tmpl = "cookiecutter/tests/test-input/fake-repo-no-tmpl"
    try:
        project_template = find_template(repo_dir_no_tmpl)
    except NonTemplatedInputDirException:
        pass
    else:
        assert False, "Did not raise NonTemplatedInputDirException"

# Generated at 2022-06-13 18:34:07.419424
# Unit test for function find_template
def test_find_template():
    repo_dir = "/Users/audreyr/Documents/GitHub/cookiecutter-pypackage"
    project_template = find_template(repo_dir)
    assert project_template == "/Users/audreyr/Documents/GitHub/cookiecutter-pypackage/{{cookiecutter.repo_name}}"

# Generated at 2022-06-13 18:34:13.043506
# Unit test for function find_template
def test_find_template():
    assert find_template("repos/cookiecutter-pypackage") == "repos/cookiecutter-pypackage/{{cookiecutter.repo_name}}"
    assert find_template("repos/cookiecutter-pypackage/{{cookiecutter.repo_name}}") == None

# Generated at 2022-06-13 18:34:15.598682
# Unit test for function find_template
def test_find_template():
    import tempfile
    repo_dir = tempfile.mkdtemp()
    template = '{{cookiecutter.repo_name}}'
    os.mkdir(os.path.join(repo_dir, template))
    assert find_template(repo_dir) == os.path.join(repo_dir, 'template')

# Generated at 2022-06-13 18:34:17.301648
# Unit test for function find_template
def test_find_template():
    # TODO: put this test_find_template in /tests
    pass

# Generated at 2022-06-13 18:34:20.824285
# Unit test for function find_template
def test_find_template():
    assert find_template('../tests/test-repo-pre/') == '../tests/test-repo-pre/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:34:25.047707
# Unit test for function find_template
def test_find_template():
    repo_dir = 'tests/fake-repo-pre/'
    project_template = 'fake-repo-pre/{{cookiecutter.repo_name|lower}}'

# Generated at 2022-06-13 18:34:36.084562
# Unit test for function find_template
def test_find_template():
    """Test function for `find_template`."""
    from cookiecutter import utils
    from cookiecutter import exceptions

    from .fake_project import make_fake_repo

    class TestCase(object):
        def __init__(self, repo_dir, should_raise):
            self.repo_dir = repo_dir
            self.should_raise = should_raise

    # Test Case 1: False positive due to directory name
    t1_repo_dir = make_fake_repo(context={'repo_name': 'test-cookiecutter'})
    t1_test_case = TestCase(t1_repo_dir, should_raise=True)
    assert t1_test_case

# Generated at 2022-06-13 18:34:39.173155
# Unit test for function find_template
def test_find_template():
    """Ensure that find_template() accurately identifies the project template
    directory.
    """
    pass
    # TODO: create the necessary test set up and run both successful and
    #       unsuccessful tests to ensure that find_template() is working as
    #       expected.

# Generated at 2022-06-13 18:34:40.991857
# Unit test for function find_template
def test_find_template():
    assert find_template('/home/audreyr/cookiecutter-pypackage') == 'cookiecutter-pypackage/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:34:43.984536
# Unit test for function find_template
def test_find_template():
    """Verify find_template returns correct path in mock directory."""
    repo_dir = os.path.abspath('tests/mock-repo-tmpl/')
    correct_template_path = os.path.abspath('tests/mock-repo-tmpl/{{cookiecutter.repo_name}}')

    assert find_template(repo_dir) == correct_template_path

# Generated at 2022-06-13 18:34:50.293709
# Unit test for function find_template
def test_find_template():
    """Unit test for function find_template()"""
    repo_dir = os.path.join('tests', 'test-find-template')
    expected_dir = os.path.join(repo_dir, '{{cookiecutter.project_slug}}')
    actual_dir = find_template(repo_dir)
    assert actual_dir == expected_dir

# Generated at 2022-06-13 18:35:05.111935
# Unit test for function find_template
def test_find_template():
    """Verify that find_template can find a template in a repo."""
    import tempfile
    from cookiecutter import utils

    temp_dir = tempfile.mkdtemp()
    repo_dir = os.path.join(temp_dir, '{{cookiecutter.repo_name}}')
    os.makedirs(repo_dir)

    template = find_template(repo_dir)
    assert utils.is_exe(template)


# Generated at 2022-06-13 18:35:08.569472
# Unit test for function find_template
def test_find_template():
    repo_dir_contents = os.listdir(repo_dir)
    assert find_template(repo_dir) == os.path.join(repo_dir, repo_dir_contents[0])

# Generated at 2022-06-13 18:35:10.158322
# Unit test for function find_template
def test_find_template():
    pass
    # TODO

# Generated at 2022-06-13 18:35:12.770486
# Unit test for function find_template
def test_find_template():
    # repo_dir is a non-templated input directory
    repo_dir = '/Users/me/somedir/someproject'
    assert find_template(repo_dir) == NonTemplatedInputDirException

# Generated at 2022-06-13 18:35:17.745363
# Unit test for function find_template
def test_find_template():
    """Verify that find_template() returns the correct value."""
    assert find_template('tests/fake-repo-pre/') == 'tests/fake-repo-pre/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:35:20.321297
# Unit test for function find_template
def test_find_template():
    find_template('/Users/arnavg/Desktop/cookiecutter-test/test-repo')

# Generated at 2022-06-13 18:35:29.729258
# Unit test for function find_template
def test_find_template():
    template_input_path = os.path.join(
        os.path.dirname(__file__),
        '..',
        'tests',
        'test-data',
        'template-project'
    )
    assert find_template(template_input_path) == os.path.join(
        template_input_path,
        '{{cookiecutter.repo_name}}'
    )

    non_template_input_path = os.path.join(
        os.path.dirname(__file__),
        '..',
        'tests',
        'test-data',
        'non-template-project'
    )
    try:
        find_template(non_template_input_path)
    except NonTemplatedInputDirException:
        assert True
    else:
        assert False

# Generated at 2022-06-13 18:35:36.632006
# Unit test for function find_template
def test_find_template():
    """Unit test for function `find_template`."""
    # Create a temp dir
    import tempfile
    cur_path = os.path.abspath(os.curdir)
    temp_dir = tempfile.mkdtemp()

    # Create a fake input dir
    os.chdir(temp_dir)
    os.makedirs('not_the_one')
    os.makedirs('{{cookiecutter.project}}')
    os.chdir(cur_path)

    # Find the template
    assert find_template(temp_dir) == os.path.join(temp_dir, '{{cookiecutter.project}}')

    # Clean up the temp dir
    import shutil
    shutil.rmtree(temp_dir)

# Generated at 2022-06-13 18:35:42.191525
# Unit test for function find_template
def test_find_template():
    # Unit test for function find_template
    template_dir = os.path.join('tests', 'files', 'test-template')
    actual_template_path = find_template(template_dir)
    expected_template_path = os.path.join(
        template_dir, '{{cookiecutter.repo_name}}'
    )
    assert actual_template_path == expected_template_path

# Generated at 2022-06-13 18:35:47.535989
# Unit test for function find_template
def test_find_template():
    import tempfile
    import shutil
    test_repo_dir = tempfile.mkdtemp('find_template_test')
    os.mkdir(os.path.join(test_repo_dir, '{{cookiecutter.project_name}}'))
    os.mkdir(os.path.join(test_repo_dir, 'test-project'))
    project_template = find_template(test_repo_dir)
    assert project_template.endswith('{{cookiecutter.project_name}}')
    shutil.rmtree(test_repo_dir)

# Generated at 2022-06-13 18:35:53.458027
# Unit test for function find_template
def test_find_template():
    """Test the `find_template` function."""
    pass

# Generated at 2022-06-13 18:35:54.727444
# Unit test for function find_template
def test_find_template():
    find_template('tests/test-input/fake-repo-pre/')

# Generated at 2022-06-13 18:35:55.405423
# Unit test for function find_template
def test_find_template():
    pass

# Generated at 2022-06-13 18:35:56.796042
# Unit test for function find_template
def test_find_template():
    assert(find_template('') == None)

# Generated at 2022-06-13 18:36:00.404892
# Unit test for function find_template
def test_find_template():
    repo_dir = 'fake-repo-dir'
    assert find_template(repo_dir) == os.path.join(repo_dir, 'cookiecutter-foobar')

# Generated at 2022-06-13 18:36:14.713812
# Unit test for function find_template
def test_find_template():
    """
    Run test for find_template.
    """
    import os
    import sys
    import tempfile
    import shutil
    from cookiecutter.exceptions import NonTemplatedInputDirException

    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()
    os.chdir(temp_dir)

    # Create a dir that contains cookiecutter, but not both.
    open('cookiecutterfoo', 'a').close()
    with pytest.raises(NonTemplatedInputDirException):
        find_template(temp_dir)

    # Create a dir that contains {{ and }} but not cookiecutter.
    shutil.rmtree(temp_dir)
    temp_dir = tempfile.mkdtemp()
    os.chdir(temp_dir)


# Generated at 2022-06-13 18:36:18.756012
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.abspath(os.path.dirname(__file__))
    repo_dir = os.path.join(repo_dir, 'fake-repo-pre/')

    project_template = find_template(repo_dir)
    assert '{{cookiecutter.repo_name}}' in project_template
    assert os.path.exists(project_template)

# Generated at 2022-06-13 18:36:20.202510
# Unit test for function find_template
def test_find_template():
    """Test function find_template"""
    pass

# Repo finder functions

# Generated at 2022-06-13 18:36:21.851797
# Unit test for function find_template
def test_find_template():
    find_template("tests/fixtures/repo-tmpl")

# Generated at 2022-06-13 18:36:24.030251
# Unit test for function find_template
def test_find_template():
    assert find_template('/path/to/repo')
    assert find_template('/path/to/repo') == 'The project template appears to be'

# Generated at 2022-06-13 18:36:37.982684
# Unit test for function find_template
def test_find_template():
    find_template(repo_dir = 'tests/fake-repo-pre/{{cookiecutter.repo_name}}')

# Generated at 2022-06-13 18:36:45.708183
# Unit test for function find_template
def test_find_template():
    """Unit test for function `find_template`."""
    from .utils import TEST_DIR
    repo_dir = os.path.join(TEST_DIR, 'fake-repo')
    project_template = os.path.join(repo_dir, 'fake-project-tmpl')
    assert os.path.abspath(project_template) == \
        os.path.abspath(find_template(repo_dir))

# Generated at 2022-06-13 18:36:46.291620
# Unit test for function find_template
def test_find_template():
    pass

# Generated at 2022-06-13 18:36:50.196064
# Unit test for function find_template
def test_find_template():
    import tempfile
    from .repository import make_empty_dir
    from shutil import rmtree
    repo_dir = tempfile.mkdtemp()
    template_dir = os.path.join(repo_dir, '{{cookiecutter.repo_name}}')
    make_empty_dir(template_dir)
    assert find_template(repo_dir) == template_dir
    rmtree(repo_dir)

# Generated at 2022-06-13 18:37:00.611958
# Unit test for function find_template
def test_find_template():
    """Check that find_template works."""
    from cookiecutter.utils import rmtree

    from .compat import patch, Mock

    import tempfile

    # Create a temp directory and populate the project template inside it.
    # and then remove the temp directory.
    def remove_template(template_dir):
        logger.debug('Removing {0}'.format(template_dir))
        rmtree(template_dir)

    # Create a temp directory
    template_dir = tempfile.mkdtemp()

    # Create a project template inside the temp directory
    template_name = 'my-fake-template'
    full_template_dir = os.path.join(template_dir, template_name)
    os.mkdir(full_template_dir)

    # Mock os.listdir inside find_template

# Generated at 2022-06-13 18:37:02.095024
# Unit test for function find_template
def test_find_template():
    # check for a true value
    assert True


# Generated at 2022-06-13 18:37:08.213504
# Unit test for function find_template
def test_find_template():

    test_repo_dir = os.path.join(
        os.path.dirname(__file__), 'true-repo-tmpl', 'cookiecutter-pypackage')
    output = find_template(test_repo_dir)
    expected_output = os.path.join(
        os.path.dirname(__file__), 'true-repo-tmpl', 'cookiecutter-pypackage',
        '{{cookiecutter.repo_name}}')

    assert output == expected_output

# Generated at 2022-06-13 18:37:15.609031
# Unit test for function find_template
def test_find_template():
    """
    Tests find_template()
    """

    # Test against incorrect "cookiecutter" directory
    repo_dir = 'cookiecutter-pypackage'
    project_template = find_template(repo_dir)
    assert project_template == 'cookiecutter-pypackage'

    # Test against correct "cookiecutter" directory
    repo_dir = '{{cookiecutter.repo_name}}'
    project_template = find_template(repo_dir)
    assert project_template == 'cookiecutter-pypackage'

# Generated at 2022-06-13 18:37:21.029592
# Unit test for function find_template
def test_find_template():
    project_dir = os.path.dirname(__file__)
    find_template(os.path.join(project_dir, '..', 'tests', 'fake-repo-pre'))
    find_template(os.path.join(project_dir, '..', 'tests', 'fake-repo-post'))

# Generated at 2022-06-13 18:37:30.172536
# Unit test for function find_template
def test_find_template():
    """Check that the template dir is found properly in the fixture repo"""
    repo_path = os.path.join(
        os.path.dirname(__file__),
        '..',
        'tests',
        'test-repo-tmpl'
    )

    test_template = find_template(repo_path)
    assert test_template == os.path.join(repo_path, '{{ cookiecutter.repo_name }}')