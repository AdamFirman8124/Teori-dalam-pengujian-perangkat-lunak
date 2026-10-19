

# Generated at 2022-06-13 18:27:40.554387
# Unit test for function find_template
def test_find_template():
    """Find the template in the fixture."""
    project_template = find_template('tests/fixtures/fake-repo-tmpl')

    assert project_template == 'tests/fixtures/fake-repo-tmpl/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:27:46.489626
# Unit test for function find_template
def test_find_template():
    """Test the find_template function."""
    test_template_dir = os.path.join('tests', 'test-find-dir')
    test_dir = find_template(test_template_dir)
    assert test_dir == os.path.join(test_template_dir, "{{cookiecutter.project_name}}")

# Generated at 2022-06-13 18:27:50.643256
# Unit test for function find_template
def test_find_template():
    """Verify that function find_template returns a proper path"""
    from cookiecutter.find import find_template
    from os.path import join
    from cookiecutter import __file__ as cc_root
    cc_root = cc_root[0:cc_root.rfind('/')]
    template_path = find_template(join(cc_root, 'tests/test-data/fake-repo-pre/'))
    assert template_path == join(cc_root, 'tests/test-data/fake-repo-pre/{{cookiecutter.repo_name}}/')

# Generated at 2022-06-13 18:27:56.508440
# Unit test for function find_template
def test_find_template():
    """Test find_template function"""
    repo_dir = os.path.expanduser('~/.cookiecutters/cookiecutter-pypackage')
    project_template = find_template(repo_dir)
    assert project_template == os.path.expanduser('~/.cookiecutters/cookiecutter-pypackage/{{cookiecutter.repo_name}}')

# Generated at 2022-06-13 18:28:10.298520
# Unit test for function find_template
def test_find_template():
    """Load the unit test project and call find_template.
    """
    import pytest
    import tempfile
    import shutil

    from cookiecutter.main import cookiecutter

    temp_dir = tempfile.mkdtemp()
    cookiecutter(os.path.join(os.path.dirname(__file__), '..', 'tests', 'fake-repo-pre/'),
                 no_input=True,
                 output_dir=temp_dir)

    repo_dir_contents = os.listdir(temp_dir)
    assert (
        sorted(repo_dir_contents) ==
        ['README.rst', 'fake_repo_pre', 'hooks', '.gitignore', '.git']
    )


# Generated at 2022-06-13 18:28:14.915444
# Unit test for function find_template
def test_find_template():
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    template_path = os.path.join(cur_dir, 'test-template')

    project_template = find_template(template_path)

    assert os.path.basename(project_template) == '{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:28:27.154769
# Unit test for function find_template
def test_find_template():
    from cookiecutter.compat import TemporaryDirectory
    from .config import default_config
    from .main import cookiecutter

    repo_dir = os.path.join(os.path.dirname(__file__), '..', 'tests', 'fake-repo-pre')

    with TemporaryDirectory() as template_dir:
        template_dir = os.path.abspath(template_dir)
        cookiecutter(
            repo_dir,
            no_input=True,
            output_dir=template_dir,
            config_file=default_config
        )
        project_template = find_template(template_dir)

    assert '.git' in project_template
    assert '{{cookiecutter.test_var}}' in project_template

# Generated at 2022-06-13 18:28:35.040732
# Unit test for function find_template
def test_find_template():
    find_template("../tests/test-repo-pre/")
    find_template("../tests/test-repo-post/")

    # assert that the function raises an error if the input directory
    # does not appear to be a template.
    try:
        find_template("../")
    except NonTemplatedInputDirException:
        return True
    return False

# Run unit tests
if __name__ == '__main__':
    print(test_find_template())

# Generated at 2022-06-13 18:28:39.786242
# Unit test for function find_template
def test_find_template():
    """Verify find_template() returns the correct directory."""
    repo_dir = '/home/audreyr/cookiecutter-pypackage'
    project_template = find_template(repo_dir)
    project_template = os.path.join(repo_dir, '{{cookiecutter.repo_name}}')
    assert project_template == '/home/audreyr/cookiecutter-pypackage/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:28:44.063252
# Unit test for function find_template
def test_find_template():
    from cookiecutter import find
    from cookiecutter import utils
    import os

    repo_dir = os.path.abspath(
        os.path.join('tests', 'files', 'fake-repo-pre')
    )
    # Set up a fake repository
    utils.make_sure_path_exists(repo_dir)

    pr

# Generated at 2022-06-13 18:28:48.579979
# Unit test for function find_template
def test_find_template():
    from cookiecutter.tests.test_find import test_find_template as _test_find_template
    _test_find_template()



# Generated at 2022-06-13 18:28:51.985888
# Unit test for function find_template
def test_find_template():
    repo_dir = '../test-repo'
    template = find_template(repo_dir)
    assert template == '../test-repo/{{cookiecutter.repo_name}}'



# Generated at 2022-06-13 18:28:59.916871
# Unit test for function find_template
def test_find_template():
    """Test find_template."""
    # test on cloned repo
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    repo = os.path.join(cur_dir, 'test-key', 'cookiecutter-pypackage')
    assert find_template(repo) == os.path.join(repo, '{{cookiecutter.repo_name}}')

    # test on existing repo
    existing_repo = 'https://github.com/audreyr/cookiecutter-pypackage.git'
    assert find_template(existing_repo) == os.path.join(existing_repo, '{{cookiecutter.repo_name}}')

    # test on local dir

# Generated at 2022-06-13 18:29:09.496981
# Unit test for function find_template
def test_find_template():
    """Verify find_template function finds project template"""
    repo_dir_contents = ['cookiecutter-pypackage',
                         'cookiecutter-jquery',
                         '.git',
                         'other_file.txt']
    repo_dir = '/tmp/cookiecutter-test-repo'
    project_template = os.path.join(repo_dir, 'cookiecutter-jquery')
    assert find_template(repo_dir) == project_template

# Generated at 2022-06-13 18:29:16.576260
# Unit test for function find_template
def test_find_template():
    # Unit test for function find_template
    # TODO: Make this a test
    my_dir = os.path.dirname(os.path.abspath(__file__))
    temp_dir = os.path.join(my_dir, '..', 'tests', 'files', 'test-input')
    assert find_template(temp_dir) == os.path.join(temp_dir, 'cookiecutter-pypackage')

# Generated at 2022-06-13 18:29:24.137730
# Unit test for function find_template
def test_find_template():
    """Verify that the function works as expected."""
    test_repo_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        '..',
        'tests',
        'test-repo'
    )
    test_project_template = os.path.join(
        test_repo_dir,
        '{{cookiecutter.repo_name}}',
    )
    assert find_template(test_repo_dir) == test_project_template

# Generated at 2022-06-13 18:29:28.157164
# Unit test for function find_template
def test_find_template():
    """
    Test find_template.

    It should only return directories that are in the format of a Cookiecutter
    project template.
    """

    template_path = 'tests/test-find-template/{{cookiecutter.repo_name}}'

    assert find_template('tests/test-find-template') == template_path

# Generated at 2022-06-13 18:29:35.463491
# Unit test for function find_template
def test_find_template():
    """Sanity check for the function that finds the template within a cloned
    repo.
    """
    test_repo_dir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), 'test-repo-pre-gen')
    )
    project_dir = os.path.join(test_repo_dir, '{{cookiecutter.repo_name}}')
    assert project_dir == find_template(test_repo_dir)

# Generated at 2022-06-13 18:29:38.073893
# Unit test for function find_template
def test_find_template():
    """
    TODO: Figure out a way to test this.
    """
    pass

# Generated at 2022-06-13 18:29:47.169147
# Unit test for function find_template
def test_find_template():
    """Test find_template method."""

    # Create temporary directory
    import tempfile
    temp_dir = tempfile.mkdtemp()

    # Create a directory inside temporary directory
    test_dir = tempfile.mkdtemp(dir=temp_dir)

    # Create a repository directory inside temporary directory
    repo_dir = tempfile.mkdtemp(dir=temp_dir)

    # Create a project template directory inside temporary directory
    proj_dir = tempfile.mkdtemp(dir=temp_dir)

    # Create a cookiecutter.json file
    import json
    with open(os.path.join(proj_dir, 'cookiecutter.json'), 'w') as f:
        json.dump({}, f)

    # Test that it can find project template
    assert find_template(repo_dir) == None



# Generated at 2022-06-13 18:29:56.989843
# Unit test for function find_template
def test_find_template():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    test_dir = os.path.join(base_dir, 'test-repo', 'test_template')
    repo_dir = os.path.join(test_dir, '{{cookiecutter.repo_name}}')
    expected = os.path.join(test_dir, '{{cookiecutter.reponame}}')
    assert find_template(repo_dir) == expected

# Generated at 2022-06-13 18:30:01.427218
# Unit test for function find_template
def test_find_template():
    """Test find_template function to ensure that it can find the template directory in a git repo."""
    repo_dir = "/Users/hongbo/Projects/cookiecutter-flask/tests"
    assert find_template(repo_dir) == "/Users/hongbo/Projects/cookiecutter-flask/tests/project_name"

# Generated at 2022-06-13 18:30:05.321897
# Unit test for function find_template
def test_find_template():
    repo_dir = '/home/vanessa/Desktop/cookiecutters/cookiecutter-pypackage'
    project_template = find_template(repo_dir)
    assert 'cookiecutter-pypackage' in project_template

# Generated at 2022-06-13 18:30:14.042864
# Unit test for function find_template
def test_find_template():
    """Verify find_template correctly finds a template dir."""
    function_results = find_template(os.path.join(os.path.dirname(__file__), 'test-cookiecutters', 'fake-repo'))
    expected_results = os.path.join(os.path.dirname(__file__), 'test-cookiecutters', 'fake-repo', '{{cookiecutter.repo_name}}')

    assert function_results == expected_results

# Generated at 2022-06-13 18:30:19.284687
# Unit test for function find_template
def test_find_template():
    assert find_template('/home/audreyr/cookiecutter-pypackage') == '/home/audreyr/cookiecutter-pypackage/{{cookiecutter.repo_name}}'
    assert find_template('/home/audreyr/cookiecutter-pypackage-new') == None

# Generated at 2022-06-13 18:30:26.325696
# Unit test for function find_template
def test_find_template():
    """Test the find_template function with a special Cookiecutter repo."""
    repo_dir = os.path.join(
        os.path.dirname(__file__),
        'test-find-template'
    )
    project_template = find_template(repo_dir)
    assert project_template == os.path.join(repo_dir, '{{cookiecutter.repo_name}}')

# Generated at 2022-06-13 18:30:34.751544
# Unit test for function find_template
def test_find_template():
    """Verify find_template()."""
    from .compat import TemporaryDirectory

    def _generate_template_dir(suffix=None):
        s = ('{{ cookiecutter.repo_name }}/' +
             '{{ cookiecutter.repo_name }}/{{ cookiecutter.repo_name }}')
        if suffix:
            s += '-' + suffix
        s += '/'
        return s

    with TemporaryDirectory() as temp_dir:
        templated_dirname = _generate_template_dir()
        templated_dirpath = os.path.join(temp_dir, templated_dirname)
        os.makedirs(templated_dirpath)

        non_templated_dirname = _generate_template_dir(suffix='no')
        non_tem

# Generated at 2022-06-13 18:30:43.288704
# Unit test for function find_template
def test_find_template():
    # Simple case
    test_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                            '..',
                                            'tests',
                                            'test-cookiecutter',
                                            'cookiecutter-django',
                                            '{{cookiecutter.repo_name}}'))
    assert find_template(os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                      '..',
                                                      'tests',
                                                      'test-cookiecutter',
                                                      'cookiecutter-django')))  == test_dir

    # Handle case when there are no templated names

# Generated at 2022-06-13 18:30:49.855709
# Unit test for function find_template
def test_find_template():
    """Test find_template."""

    TEST_ROOT = os.path.dirname(os.path.abspath(__file__))

    # Test 1; with templated directory
    templated_dir = os.path.join(
        TEST_ROOT,
        'fake-repo-pre/my-fake-repo'
    )
    assert find_template(templated_dir) == os.path.join(
        TEST_ROOT,
        'fake-repo-pre/my-fake-repo/{{cookiecutter.repo_name}}'
    )

    # Test 2; with non-templated dir

# Generated at 2022-06-13 18:30:56.155408
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.join(os.path.dirname(__file__), '..', 'tests', 'fake-repo-pre')
    project_template = find_template(repo_dir)
    assert project_template == os.path.join(repo_dir, 'cookiecutter-pypackage')

# Generated at 2022-06-13 18:31:07.783910
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


# Generated at 2022-06-13 18:31:10.203046
# Unit test for function find_template
def test_find_template():
    """Find the project template and assert that it is the expected one."""
    repo_dir = os.getcwd()
    assert 'cookiecutter-pypackage' in find_template(repo_dir)

# Generated at 2022-06-13 18:31:12.747559
# Unit test for function find_template
def test_find_template():
    """Verify that the correct directory is identified"""
    template_dir = find_template('Tests/test-repo-pre/')
    assert template_dir == 'Tests/test-repo-pre/{{cookiecutter.repo_name}}'


# Generated at 2022-06-13 18:31:16.513239
# Unit test for function find_template
def test_find_template():
    """Test function for `find_template`."""
    assert find_template.__doc__ is not None
    # assert find_template(repo_dir) is not None

# Generated at 2022-06-13 18:31:25.846902
# Unit test for function find_template
def test_find_template():
    """Unit test for function find_template"""
    from cookiecutter.main import cookiecutter

    # Create a temporary repo
    token_path = 'https://github.com/audreyr/cookiecutter-pypackage'
    cloned_repo_dir = cookiecutter(
        token_path,
        no_input=True,
        extra_context={'full_name': 'Audrey Roy'}
    )

    # Find the template in the repo
    template_dir = find_template(cloned_repo_dir)

    # Make sure that it looks correct
    expected_template_dir = os.path.join(cloned_repo_dir, '{{cookiecutter.repo_name}}')

# Generated at 2022-06-13 18:31:37.437522
# Unit test for function find_template
def test_find_template():
    from unittest import TestCase
    from cookiecutter.tests import get_test_data

    class FindTemplateTest(TestCase):
        def test_non_templated_dir(self):
            """`find_template` raises exception when input dir is not templated."""
            non_templated_input_path = get_test_data('non-templated-input')
            with self.assertRaises(NonTemplatedInputDirException):
                find_template(non_templated_input_path)

    test_find_template = FindTemplateTest()
    test_find_template.test_non_templated_dir()

# Generated at 2022-06-13 18:31:40.447970
# Unit test for function find_template
def test_find_template():
    assert find_template('Users', 'my-user-name', 'cookiecutter-pypackage') == 'cookiecutter-pypackage'

# Generated at 2022-06-13 18:31:54.067898
# Unit test for function find_template
def test_find_template():
    """Quick test of find_template"""
    test_repo_contents = [
        "cookiecutter-{{cookiecutter.test}}",
        "cookiecutter",
        "cookiecutter_2",
        "cookiecutter_3-{{cookiecutter.test}}",
        "cookiecutter_4-{{cookiecutter.test}}",
        "cookiecutter_4-{{cookiecutter.test}}-repo",
        "cookiecutter_4-{{cookiecutter.test}}-repo-{{cookiecutter.test}}",
        "cookiecutter_5-{{cookiecutter.test}}",
        "cookiecutter_6-{{cookiecutter.test}}",
        "cookiecutter_7"
    ]


# Generated at 2022-06-13 18:32:05.010419
# Unit test for function find_template
def test_find_template():
    import os
    import pytest
    from cookiecutter import utils

    os.chdir(os.path.join(os.path.dirname(__file__), '..'))

    # Test 1: successfully find the project template
    assert find_template(utils.workdir_join('tests', 'fake-repo-tmpl')) == os.path.join(os.getcwd(), 'tests', 'fake-repo-tmpl', '{{cookiecutter.repo_name}}')

    # Test 2: returning NonTemplatedInputDirException
    with pytest.raises(NonTemplatedInputDirException):
        assert find_template(utils.workdir_join('tests', 'fake-repo-no-template'))

# Generated at 2022-06-13 18:32:09.638884
# Unit test for function find_template
def test_find_template():
    repo_dir = "/home/user/cookiecutter-cookiecutter"
    project_template = find_template(repo_dir)
    assert project_template == "/home/user/cookiecutter-cookiecutter/{{cookiecutter.repo_name}}"

# Generated at 2022-06-13 18:32:22.378695
# Unit test for function find_template
def test_find_template():
    """
    Test the find_template function by mocking the contents of a git repo
    """
    os.listdir = lambda x: ['cookiecutter-{{cookiecutter.project_slug}}']
    assert 'cookiecutter-{{cookiecutter.project_slug}}' == find_template('.')
    os.listdir = lambda x: ['cookiecutter-{{cookiecutter.project_slug}}', 'cookiecutter-pypackage']
    assert 'cookiecutter-{{cookiecutter.project_slug}}' == find_template('.')
    os.listdir = lambda x: ['cookiecutter-pypackage']
    assert 'cookiecutter-pypackage' == find_template('.')

# Generated at 2022-06-13 18:32:30.035616
# Unit test for function find_template
def test_find_template():
    """Unit test for function `find_template`."""
    template_dir = os.path.join(os.path.dirname(__file__), '..', 'fake-repo-tmpl')
    template = find_template(template_dir)

    assert template == os.path.join(template_dir, '{{cookiecutter.repo_name}}')

# Generated at 2022-06-13 18:32:30.624958
# Unit test for function find_template
def test_find_template():
    pass # TODO

# Generated at 2022-06-13 18:32:31.212094
# Unit test for function find_template
def test_find_template():
    """
    """

# Generated at 2022-06-13 18:32:37.949717
# Unit test for function find_template
def test_find_template():
    """Test find_template(repo_dir) function."""
    from cookiecutter.main import cookiecutter

    # Generate project from template
    template_dir = "tests/fake-repo-tmpl"
    context_file = "tests/fake-repo-pre/fake-repo/cookiecutter.json"
    output_dir = cookiecutter(template_dir, context_file)
    assert output_dir == os.path.abspath("fake-repo-pre")

    # Test find_template
    template_dir = os.path.join(output_dir, "tests/fake-repo-tmpl")
    assert os.path.exists(template_dir)
    project_template = find_template(template_dir)

# Generated at 2022-06-13 18:32:44.396911
# Unit test for function find_template
def test_find_template():
    """
    Test the find_template function for the case that template file appears in the
    root directory.
    """
    template_name = "project_template"
    repo_dir = "/test/repo_dir"
    project_template = find_template(repo_dir)
    assert project_template == os.path.join(repo_dir, template_name)

# Generated at 2022-06-13 18:32:49.309636
# Unit test for function find_template
def test_find_template():
    templated_idir = os.path.join('tests', 'test-repo-pre', '{{cookiecutter.repo_name}}')
    assert find_template('tests/test-repo-pre') == templated_idir


# Generated at 2022-06-13 18:32:51.788121
# Unit test for function find_template
def test_find_template():
    assert find_template('tests/test-find-template') == 'tests/test-find-template/{{ cookiecutter.repo_name }}'

# Generated at 2022-06-13 18:32:59.668906
# Unit test for function find_template
def test_find_template():
    assert find_template(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__), '..', 'tests', 'fake-repo-tmpl',
            )
        )
    ).endswith('fake-repo-tmpl/{{cookiecutter.repo_name}}')

# Generated at 2022-06-13 18:33:09.630608
# Unit test for function find_template
def test_find_template():
    os.makedirs(os.path.join('./repo_dir', '{{cookiecutter.repo_name}}'))
    assert find_template('./repo_dir') == os.path.join('./repo_dir', '{{cookiecutter.repo_name}}')
    os.removedirs(os.path.join('./repo_dir', '{{cookiecutter.repo_name}}'))
    os.makedirs(os.path.join('./repo_dir', '{{cookiecutter.repo_name_extended}}'))
    assert find_template('./repo_dir') == os.path.join('./repo_dir', '{{cookiecutter.repo_name_extended}}')

# Generated at 2022-06-13 18:33:17.076193
# Unit test for function find_template
def test_find_template():
    test_dir_name = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'test_dir')
    assert find_template(test_dir_name) == os.path.join(test_dir_name, 'cookiecutter-foobar')

if __name__ == '__main__':
    test_find_template()

# Generated at 2022-06-13 18:33:21.979563
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.abspath('tests/fake-repo-tmpl')
    project_template = find_template(repo_dir)
    assert project_template == os.path.abspath('tests/fake-repo-tmpl/{{cookiecutter.repo_name}}')

# Generated at 2022-06-13 18:33:34.209365
# Unit test for function find_template
def test_find_template():
    """Unit test for function find_template"""
    from cookiecutter.main import cookiecutter
    from shutil import rmtree
    import tempfile

    temp_dir = tempfile.mkdtemp()

    repo_dir = cookiecutter(
        'https://github.com/audreyr/cookiecutter-pypackage.git',
        no_input=True,
        output_dir=temp_dir,
        overwrite_if_exists=True
    )

    repo_dir_contents = os.listdir(repo_dir)
    assert repo_dir_contents == ['cookiecutter-pypackage']

    project_template = find_template(repo_dir)
    assert project_template == os.path.join(repo_dir, 'cookiecutter-pypackage')

    r

# Generated at 2022-06-13 18:33:39.554015
# Unit test for function find_template
def test_find_template():
    # Using function `test_input_dir` from here:
    # https://github.com/audreyr/cookiecutter/blob/master/tests/test_find.py
    # For convenience, the local variable `test_input_dir` is renamed
    # `test_input_dir_function` in this function.
    import os
    import shutil
    import tempfile

    import cookiecutter
    from cookiecutter.config import DEFAULT_CONFIG

    class TestInputDir(object):

        def __init__(self):
            self.test_input_dir_function = None

        def __enter__(self):
            repo_dir = tempfile.mkdtemp()

# Generated at 2022-06-13 18:33:48.684055
# Unit test for function find_template
def test_find_template():
    """Verify that find_template's behavior is correct.

    :returns: True if behavior is correct, False otherwise.
    """
    repo_dir = '/Explicit/Path/To/Cookiecutter-foo-bar'
    expected_project_template = '/Explicit/Path/To/Cookiecutter-foo-bar/cookiecutter-{{cookiecutter.repo_name}}'

    assert find_template(repo_dir) == expected_project_template

    repo_dir = '/Explicit/Path/To/Cookiecutter-foo-bar'
    expected_project_template = '/Explicit/Path/To/Cookiecutter-foo-bar/cookiecutter-{{cookiecutter.repo_name}}'

    assert find_template(repo_dir) == expected_project_template


# Generated at 2022-06-13 18:33:51.253968
# Unit test for function find_template
def test_find_template():
    assert find_template('/tmp/cookiecutter-dw') == '/tmp/cookiecutter-dw/cookiecutter-{{ cookiecutter.project_name }}'


# Generated at 2022-06-13 18:33:52.068930
# Unit test for function find_template
def test_find_template():
    pass

# Generated at 2022-06-13 18:33:56.576460
# Unit test for function find_template
def test_find_template():
    from cookiecutter.tests.test_find import project_dir

    pass_template_dir = find_template(project_dir)
    assert pass_template_dir == os.path.join(project_dir, '{{cookiecutter.repo_name}}')

# Generated at 2022-06-13 18:33:57.424662
# Unit test for function find_template
def test_find_template():
    pass

# Generated at 2022-06-13 18:34:10.205647
# Unit test for function find_template
def test_find_template():
    assert find_template('c:\temp\test_project') == 'c:\temp\test_project\cookiecutter_test_template'

# Generated at 2022-06-13 18:34:21.686673
# Unit test for function find_template
def test_find_template():
    from tests.test_find_repo import mocked_repos
    from nose.tools import assert_equals

    for repo in mocked_repos.values():
        project_template = find_template(repo["dir"])
        assert_equals(project_template, repo["template"])

# Generated at 2022-06-13 18:34:28.498624
# Unit test for function find_template
def test_find_template():
    here = os.path.abspath(os.path.dirname(__file__))
    fixtures = os.path.join(here, 'fixtures')
    cookiecutter_py = os.path.join(fixtures, 'cookiecutter-py')
    assert os.path.isdir(cookiecutter_py)
    project_template = find_template(cookiecutter_py)
    assert project_template == (
        os.path.join(cookiecutter_py, '{{cookiecutter.repo_name}}')
    )



# Generated at 2022-06-13 18:34:34.690292
# Unit test for function find_template
def test_find_template():
    """Asserts that a templated directory can be found"""
    os.chdir('tests/fake-repo-pre/')
    project_template = find_template('./tests/fake-repo-pre/')
    # Should be fake-repo-pre/{{cookiecutter.project_name}}/
    assert project_template == './tests/fake-repo-pre/{{cookiecutter.project_name}}/'
    os.chdir('..')

# Generated at 2022-06-13 18:34:38.681236
# Unit test for function find_template
def test_find_template():
    repo_dir = '{{cookiecutter.repo_name}}/tests/fake-repo/'
    project_template = find_template(repo_dir)
    assert project_template == '{{cookiecutter.repo_name}}/tests/fake-repo/fake-project', 'wrong project template'


# Generated at 2022-06-13 18:34:46.012495
# Unit test for function find_template
def test_find_template():
    """Find the project template"""
    repo_dir = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        'tests/test-data/fake-repo-tmpl/{{cookiecutter.repo_name}}'
    )
    template = find_template(repo_dir)
    assert 'fake-repo-tmpl' in template

# Generated at 2022-06-13 18:34:51.074159
# Unit test for function find_template
def test_find_template():
    """Verify function for finding project_template."""
    from cookiecutter import utils
    repo_dir = os.path.dirname(utils.__file__)
    project_template = find_template(repo_dir)

    assert project_template == os.path.join(repo_dir, '{{cookiecutter.repo_name}}')

# Generated at 2022-06-13 18:34:57.728052
# Unit test for function find_template
def test_find_template():
    """Verify the find_template function works."""
    from .utils import make_bare_repo
    from .compat import TemporaryDirectory

    repo_dir_name = 'bare_repo'
    template_dir_name = '{{cookiecutter.repo_name}}'
    with TemporaryDirectory() as tmpdir:
        bare_repo_dir = make_bare_repo(repo_dir_name, template_dir_name, tmpdir)
        template_dir_path = find_template(bare_repo_dir)

    assert template_dir_path.endswith('bare_repo{{cookiecutter.repo_name}}')



# Generated at 2022-06-13 18:35:06.188122
# Unit test for function find_template
def test_find_template():
    """Run function find_template."""
    repo_dir = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '..',
            'tests',
            'fake-repo',
            '{{cookiecutter.repo_name}}'
        )
    )

    project_template = find_template(repo_dir)

    assert 'fake-repo' in project_template
    assert '{{cookiecutter.repo_name}}' not in project_template

# Generated at 2022-06-13 18:35:09.568891
# Unit test for function find_template
def test_find_template():
    from . import data
    repo_dir = data.get_repo_dir()
    content = os.listdir(repo_dir)
    assert 'hello_world' in content, "template is not found"

# Generated at 2022-06-13 18:35:15.494460
# Unit test for function find_template
def test_find_template():
    import shutil
    import tempfile

    repo_dir = tempfile.mkdtemp()
    shutil.copytree('tests/test-input', repo_dir)
    try:
        template_dir = find_template(repo_dir)
        assert os.path.join(repo_dir, '{{cookiecutter.repo_name}}') == template_dir, template_dir
    finally:
        shutil.rmtree(repo_dir)

# Generated at 2022-06-13 18:35:30.635446
# Unit test for function find_template
def test_find_template():
    find_template('/../input_to_cookiecutter/')


# Generated at 2022-06-13 18:35:37.692793
# Unit test for function find_template
def test_find_template():
    import shutil
    import tempfile
    import unittest
    
    class TestCase(unittest.TestCase):
        test_dir = None
        def setUp(self):
            if self.test_dir is None:
                self.test_dir = tempfile.mkdtemp()
            template_dir = os.path.join(self.test_dir, 'repo_dir')
            os.makedirs(template_dir)
            os.makedirs(os.path.join(template_dir, '{{cookiecutter.repo_name}}'))
            self.test_dir = template_dir

        def tearDown(self):
            shutil.rmtree(self.test_dir)
            
        def test_find_template(self):
            found = find_template(self.test_dir)

# Generated at 2022-06-13 18:35:42.631707
# Unit test for function find_template
def test_find_template():
    """Test whether find_template returns the correct answer from a directory of dummy files."""
    repo_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        '..', 'tests', 'test-find-template'
    )
    project_template = find_template(repo_dir)
    assert 'cookiecutter-pypackage' in project_template

# Generated at 2022-06-13 18:35:45.157399
# Unit test for function find_template
def test_find_template():
    repo_dir = '.'
    assert find_template(repo_dir) == '{{cookiecutter.repo_name}}'
    # Add your own tests here

if __name__ == '__main__':
    test_find_template()

# Generated at 2022-06-13 18:35:48.358092
# Unit test for function find_template
def test_find_template():
    """Test that `find_template` finds an template folder, only one."""
    # TODO: finish this test
    assert True

# Generated at 2022-06-13 18:35:55.480395
# Unit test for function find_template
def test_find_template():
    '''find_template: Check to see if template is returned'''
    tempdir = mkdtemp()
    os.makedirs(os.path.join(tempdir, 'cookiecutter-{{cookiecutter_repo_name}}'))
    os.makedirs(os.path.join(tempdir, 'cookiecutter-{{cookiecutter_repo_name}}', '{{cookiecutter_repo_name}}'))
    template = find_template(tempdir)
    assert template == os.path.join(tempdir, 'cookiecutter-{{cookiecutter_repo_name}}')

# Generated at 2022-06-13 18:36:00.751356
# Unit test for function find_template
def test_find_template():
    repo_dir = '/Users/audreyr/cookiecutter-pypackage'
    project_template = os.path.join(repo_dir, '{{cookiecutter.repo_name}}')
    assert find_template(repo_dir) == project_template



# Generated at 2022-06-13 18:36:08.994859
# Unit test for function find_template
def test_find_template():
    assert find_template('cookiecutter/tests/test-data/{{cookiecutter.repo_name}}') == 'cookiecutter/tests/test-data/{{cookiecutter.repo_name}}/{{cookiecutter.project_name}}'
    assert find_template('cookiecutter/tests/test-data/jquery') != 'cookiecutter/tests/test-data/jquery/{{cookiecutter.project_name}}'

# Generated at 2022-06-13 18:36:15.324327
# Unit test for function find_template
def test_find_template():
    """Verify that the right directory is found."""
    expected = 'tests/files/fake-repo/{{cookiecutter.repo_name}}'
    repo_dir = 'tests/files/fake-repo/'
    found = find_template(repo_dir)
    assert expected == found, 'Wrong project template found.'

# Generated at 2022-06-13 18:36:21.446388
# Unit test for function find_template
def test_find_template():
    """Unit test for function find_template."""
    repo_dir = os.path.join(os.path.dirname(__file__), os.pardir, 'fake-repo')
    project_template = find_template(repo_dir)
    assert project_template == os.path.join(
        repo_dir, '{{cookiecutter.repo_name}}'
    )

# Generated at 2022-06-13 18:36:37.716036
# Unit test for function find_template
def test_find_template():
    """Find a template in a directory."""
    import tempfile
    from cookiecutter import utils

    test_dir = tempfile.mkdtemp()
    templ_dir = os.path.join(test_dir, 'cookiecutter-foobar')
  

# Generated at 2022-06-13 18:36:42.928465
# Unit test for function find_template
def test_find_template():
    assert find_template('tests/fake-repo-tmpl') == \
          os.path.join('tests', 'fake-repo-tmpl', '{{cookiecutter.repo_name}}')

# Generated at 2022-06-13 18:36:45.934286
# Unit test for function find_template
def test_find_template():
    # TODO: Will create the following:
    # - a test repo with a subdir that contains a cookiecutter.json
    # - a test repo with a subdir that contains a file called cookiecutter
    # - a test repo with a subdir that contains a file called cookiecutter
    #   and a cookiecutter.json
    pass

# Generated at 2022-06-13 18:36:48.521665
# Unit test for function find_template
def test_find_template():
    """Test ``find_template`` function."""

    assert find_template('tests/fake-repo-tmpl') == 'tests/fake-repo-tmpl/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:37:00.042263
# Unit test for function find_template
def test_find_template():
    """Verify find_template function."""
    import shutil

    from cookiecutter.config import USER_CONFIG_PATH
    from cookiecutter.main import cookiecutter

    # Store original config path so we can put it back at the end
    ORIG_USER_CONFIG_PATH = USER_CONFIG_PATH

    # Create a fake user config dir
    fake_user_config_path = os.path.join('fake-user-config-path', '.cookiecutter')
    USER_CONFIG_PATH = fake_user_config_path
    os.makedirs(USER_CONFIG_PATH)

    # Make a fake repo
    tmp_repo_dir = os.path.abspath('./fake-repo-tmpl')

# Generated at 2022-06-13 18:37:03.960980
# Unit test for function find_template
def test_find_template():
    """Verify find_template finds existing template dir."""
    template = find_template('tests/fake-repo-pre/')
    assert template == 'tests/fake-repo-pre/{{cookiecutter.repo_name}}'


# Generated at 2022-06-13 18:37:07.623482
# Unit test for function find_template
def test_find_template():
    """Test the find_template function."""
    test_repo_dir = os.path.join(os.getcwd(), 'tests/test-repo-tmpl/')
    test_project_template = os.path.join(
        test_repo_dir, 'cookiecutter-{{cookiecutter.repo_name}}'
    )

    result = find_template(test_repo_dir)
    assert result == test_project_template

# Generated at 2022-06-13 18:37:12.853827
# Unit test for function find_template
def test_find_template():
    expected = 'subdir/{{ cookiecutter.repo_name }}'
    assert find_template('tests/test-find-template') == expected
    assert find_template('tests/test-find-template/subdir') == expected

# Generated at 2022-06-13 18:37:15.089221
# Unit test for function find_template
def test_find_template():
    """
    Unit test for function find_template
    """
    repo_dir = os.path.abspath('.')
    project_template = find_template(repo_dir)
    print(project_template)

# Generated at 2022-06-13 18:37:16.463497
# Unit test for function find_template
def test_find_template():
    find_template('project_template')

