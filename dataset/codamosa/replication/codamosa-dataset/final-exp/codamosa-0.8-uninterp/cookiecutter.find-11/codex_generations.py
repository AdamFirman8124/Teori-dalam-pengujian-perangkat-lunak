

# Generated at 2022-06-13 18:27:41.864374
# Unit test for function find_template
def test_find_template():
    """
    Test that find_template finds the project template
    for a sample project.
    """
    repo_dir = 'tests/test-find-template/fake-repo'
    repo_dir_contents = os.listdir(repo_dir)
    project_template = find_template(repo_dir)
    assert 'project_template' in project_template
    assert os.path.basename(project_template) == 'project_template'

# Generated at 2022-06-13 18:27:46.013481
# Unit test for function find_template
def test_find_template():
    assert find_template(os.getcwd()) == os.path.join(os.getcwd(),
                                                      'cookiecutter-{{cookiecutter.repo_name}}')

# Generated at 2022-06-13 18:27:46.490977
# Unit test for function find_template
def test_find_template():
    pass

# Generated at 2022-06-13 18:27:48.931380
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.abspath('tests/fake-repo-pre/')
    project_template = find_template(repo_dir)
    assert project_template == os.path.join(repo_dir, 'cookiecutter-pypackage')

# Generated at 2022-06-13 18:27:51.203143
# Unit test for function find_template
def test_find_template():
    """Test to find the template in the current repo."""
    find_template(os.getcwd())

# Generated at 2022-06-13 18:28:00.238178
# Unit test for function find_template
def test_find_template():
    import tempfile
    import shutil

    this_dir, this_filename = os.path.split(__file__)

    # Make a temporary directory
    repo_dir = tempfile.mkdtemp()

    # Copy cookiecutter-pypackage/ to temp dir
    shutil.copytree(
        os.path.join(this_dir, '..', '..', 'tests', 'fake-repo-pre/'),
        repo_dir
    )

    # Test for un-rendered project dir
    template_dir = find_template(repo_dir)

    assert os.path.basename(template_dir) == '{{cookiecutter.repo_name}}'

    # Add a rendered project dir

# Generated at 2022-06-13 18:28:04.125389
# Unit test for function find_template
def test_find_template():
    template_dir = 'tests/test-find-template'
    result = find_template(template_dir)
    assert result == 'tests/test-find-template/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:28:04.859910
# Unit test for function find_template
def test_find_template():
    pass

# Generated at 2022-06-13 18:28:09.696587
# Unit test for function find_template
def test_find_template():
    # Setup
    repo_dir = os.path.abspath(os.path.dirname(__file__))
    expect = os.path.join(repo_dir, "cookiecutter-demo")
    # Run
    found = find_template(repo_dir)
    # Verify
    assert found == expect

# Generated at 2022-06-13 18:28:13.619795
# Unit test for function find_template
def test_find_template():
    with patch.object(
        os, 'listdir', return_value=['my_template-{{cookiecutter.project_name}}', 'my_other_template']
    ):
        assert find_template('/root/') == '/root/my_template-{{cookiecutter.project_name}}'

# Generated at 2022-06-13 18:28:20.890540
# Unit test for function find_template
def test_find_template():
    """Make sure find_template() returns the templated directory."""
    import message_box
    message_box.boxit(find_template('/Users/donjoseph/devel/Projects/cookiecutter/cookiecutter/tests/test-verses/actual-repo'))

# Generated at 2022-06-13 18:28:27.313134
# Unit test for function find_template
def test_find_template():
    if os.path.exists('/tmp/cookiecutter-pypackage'):
        shutil.rmtree('/tmp/cookiecutter-pypackage')
    os.makedirs('/tmp/cookiecutter-pypackage/{{cookiecutter.repo_name}}')
    test = find_template('/tmp/cookiecutter-pypackage/')
    return test

# Generated at 2022-06-13 18:28:37.235792
# Unit test for function find_template
def test_find_template():
    """Verify Cookiecutter discovers the project template correctly."""
    import shutil
    import tempfile
    from cookiecutter import search

    template_dir = os.path.abspath(
        os.path.join(
            os.path.dirname(os.path.abspath(__file__)), 'fake-repo-tmpl'
        )
    )
    temp_dir = tempfile.mkdtemp()

    shutil.copytree(template_dir, temp_dir)

    assert search.find_template(temp_dir) == os.path.abspath(
        os.path.join(temp_dir, 'fake-project', '{{cookiecutter.repo_name}}')
    )

# Generated at 2022-06-13 18:28:43.488395
# Unit test for function find_template
def test_find_template():
    template_dir = os.path.join(os.path.dirname(__file__), 'fake-repo')
    expected_template = os.path.join(
        template_dir,
        '{{cookiecutter.repo_name}}-{{cookiecutter.repo_name_owner}}'
    )

    assert find_template(template_dir) == expected_template

    # Test a repo where the template isn't templated
    template_dir_2 = os.path.join(template_dir, 'fake-repo-2')
    os.makedirs(template_dir_2)
    os.makedirs(os.path.join(template_dir_2, 'foobar'))

# Generated at 2022-06-13 18:28:49.383447
# Unit test for function find_template
def test_find_template():
    """Unit test for function find_template"""
    from cookiecutter import utils
    os.chdir(utils.TEST_TEMPLATE)
    project_template = find_template('.')
    assert project_template == 'cookiecutter-django/{{cookiecutter.repo_name}}'



# Generated at 2022-06-13 18:28:53.841105
# Unit test for function find_template
def test_find_template():
    "The unit test for the function find_template."
    try:
        find_template('../cookiecutter-pypackage')
    except NonTemplatedInputDirException:
        pass
    else:
        raise AssertionError("A NonTemplatedInputDirException should have been raised")

# Generated at 2022-06-13 18:28:59.290637
# Unit test for function find_template
def test_find_template():
    """Make sure that the correct template is set"""
    template_text = """
{{ cookiecutter.project_name }}
{{ cookiecutter.repo_name }}
{{ cookiecutter.project_slug }}
"""
    with tempdir() as template_dir:
        template_file = os.path.join(template_dir, 'my_template')
        with open(template_file, 'w') as f:
            f.write(template_text)
        assert find_template(template_dir) == template_file



# Generated at 2022-06-13 18:29:14.460396
# Unit test for function find_template
def test_find_template():
    """Determine which child directory of `repo_dir` is the project template.

    :param repo_dir: Local directory of newly cloned repo.
    :returns project_template: Relative path to project template.
    """
    repo_dir = '/home/user/cookiecutter-pypackage'
    logger.debug('Searching %s for the project template.', repo_dir)

    repo_dir_contents = os.listdir(repo_dir)

# Generated at 2022-06-13 18:29:14.823620
# Unit test for function find_template
def test_find_template():
    pass

# Generated at 2022-06-13 18:29:21.750539
# Unit test for function find_template
def test_find_template():

    import tempfile, shutil

    repo_dir = tempfile.mkdtemp()
    os.mkdir(os.path.join(repo_dir, '{{cookiecutter.repo_name}}'))

    if not find_template(repo_dir).endswith("{{cookiecutter.repo_name}}"):
        raise AssertionError("Template does not end with {{cookiecutter.repo_name}}")

    shutil.rmtree(repo_dir)

# Generated at 2022-06-13 18:29:29.953304
# Unit test for function find_template
def test_find_template():
    assert find_template('/home/audreyr/projects/cookiecutter-pypackage/{{ cookiecutter.repo_name }}') == '/home/audreyr/projects/cookiecutter-pypackage/{{ cookiecutter.repo_name }}'

# Generated at 2022-06-13 18:29:34.856319
# Unit test for function find_template
def test_find_template():
    import tempfile
    import shutil
    import os

    tmp_dir = tempfile.mkdtemp()
    tmp_template = os.path.join(tmp_dir, 'my_template')
    os.mkdir(tmp_template)

    assert find_template(tmp_dir) == tmp_template

    shutil.rmtree(tmp_dir)

# Generated at 2022-06-13 18:29:38.175131
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.join('tests', 'fake-repo-tmpl')
    project_template = find_template(repo_dir)
    assert project_template == os.path.join(repo_dir, '{{cookiecutter.repo_name}}')

# Generated at 2022-06-13 18:29:43.348084
# Unit test for function find_template
def test_find_template():
    """Test function."""
    logging.disable(logging.CRITICAL)
    repo_dir = os.path.abspath(os.path.dirname(__file__))
    expected = os.path.join(repo_dir, 'tests/fake-repo-pre/{{cookiecutter.repo_name}}')
    actual = find_template(repo_dir)
    assert expected == actual

# Generated at 2022-06-13 18:29:55.333371
# Unit test for function find_template
def test_find_template():
    """Test that the correct template directory is found given a input_dir."""
    # Create a temporary dir same as a repo dir
    repo_dir = "/home/chris/dev/myproject"
    os.mkdir(repo_dir)

    # This will be the template
    os.mkdir(os.path.join(repo_dir, "myproject"))

    # This should not be the template
    os.mkdir(os.path.join(repo_dir, "foobar"))
    os.mkdir(os.path.join(repo_dir, "foobar-{{cookiecutter.project_name}}"))

    template_dir = find_template(repo_dir)
    assert template_dir == "/home/chris/dev/myproject/myproject"

    # Clean up
    os.rmdir

# Generated at 2022-06-13 18:30:05.730986
# Unit test for function find_template
def test_find_template():
    """Verify find_template function."""
    # Ensure function fails when passed a path to something that is not
    # templated.
    non_template_dir = '/tmp/cookiecutter-non-templated'
    if not os.path.exists(non_template_dir):
        os.makedirs(non_template_dir)
    try:
        find_template(non_template_dir)
        raise Exception('find_template did not fail on non-template dir')
    except NonTemplatedInputDirException:
        pass

    # Ensure function finds the project template when passed a path to a
    # templated repo.
    from cookiecutter.tests.test_replay import make_templated_repo
    templated_repo_dir = make_templated_repo()
    project

# Generated at 2022-06-13 18:30:17.493531
# Unit test for function find_template
def test_find_template():
    """Determine which child directory of `repo_dir` is the project template."""
    import shutil
    import tempfile
    import textwrap
    from cookiecutter.main import cookiecutter

    # Create a temporary directory to be our 'home' dir
    home_dir = tempfile.mkdtemp()

    # Create a temporary directory to be our 'repo' dir
    repo_dir = tempfile.mkdtemp()

    # Create a fake cookiecutter.json file

# Generated at 2022-06-13 18:30:22.699748
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.join(os.path.dirname(__file__), '..', 'tests', 'fake-repo')
    project_template = find_template(repo_dir)
    assert project_template.endswith('tests/fake-repo/{{cookiecutter.repo_name}}')

# Generated at 2022-06-13 18:30:28.476203
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                '..', '..', 'tests', 'test-data', 'cookiecutters',
                                'pypackage'))
    template_dir = find_template(repo_dir)
    assert 'cookiecutter-pypackage' in template_dir

# Generated at 2022-06-13 18:30:35.070222
# Unit test for function find_template
def test_find_template():
    input_dir = "/Users/brian/code/cookiecutter-pypackage/tests/fake-repo-pre/"
    project_template = find_template(input_dir)
    assert project_template == "/Users/brian/code/cookiecutter-pypackage/tests/fake-repo-pre/fake-project"


# Generated at 2022-06-13 18:30:45.093488
# Unit test for function find_template
def test_find_template():
    import time
    import random
    import shutil
    import tempfile

    logger.debug('Creating a temporary directory to test find_template()')
    tmpdir = tempfile.mkdtemp()

# Generated at 2022-06-13 18:30:47.356030
# Unit test for function find_template
def test_find_template():
    repo_dir = 'tests/test-repo'
    project_template = find_template(repo_dir)
    assert project_template == 'tests/test-repo/{{cookiecutter.project_name}}'

# Generated at 2022-06-13 18:30:51.547985
# Unit test for function find_template
def test_find_template():
    with open('tests/test-find-template/cookiecutter.json', 'r') as f:
        assert find_template('tests/test-find-template') == 'tests/test-find-template/cookiecutter-pypackage'

# Generated at 2022-06-13 18:31:01.284247
# Unit test for function find_template
def test_find_template():

    from cookiecutter.tests.test_utils import make_repo, remove_repo
    from cookiecutter import utils
    from cookiecutter.exceptions import NonTemplatedInputDirException

    # Generate a fake repo for testing
    repo_dir = make_repo()


# Generated at 2022-06-13 18:31:05.384044
# Unit test for function find_template
def test_find_template():
    """Test the find_template function."""
    repo_dir = 'tests/fake-repo-templated'
    project_template = 'tests/fake-repo-templated/{{cookiecutter.repo_name}}'
    found_project_template = find_template(repo_dir)
    assert found_project_template == project_template



# Generated at 2022-06-13 18:31:12.050699
# Unit test for function find_template
def test_find_template():
    test_repo = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        '..',
        'fixtures',
        'test-find-template'
    )
    _find_template = find_template(test_repo)
    expected_path = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        '..',
        'fixtures',
        'test-find-template',
        '{{cookiecutter.repo_name}}'
    )
    assert _find_template == expected_path


# Generated at 2022-06-13 18:31:13.554258
# Unit test for function find_template
def test_find_template():
    """Ensure function `find_template` operates as expected."""
    pass

# Generated at 2022-06-13 18:31:17.907132
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'tests', 'test-find-template')
    project_template = find_template(repo_dir)
    assert project_template == os.path.join(repo_dir, '{{cookiecutter.repo_name}}')

# Generated at 2022-06-13 18:31:20.810024
# Unit test for function find_template
def test_find_template():
    """Checked if the method finds a template or not.

    :returns: True if the method returns a template.
    """
    find_template('/Users/marco/Desktop/pycharm_projects/pypackage_boilerplate')

# Generated at 2022-06-13 18:31:24.009385
# Unit test for function find_template
def test_find_template():
    """Test that find_template returns a proper path/string"""
    from cookiecutter.tests import mock_find_no_repo_template, mock_find_repo_template

    assert type(find_template(mock_find_repo_template)) is str


# Generated at 2022-06-13 18:31:30.660320
# Unit test for function find_template
def test_find_template():
    """Verify find_template"""
    find_template('~/cookiecutter-demo')

# Generated at 2022-06-13 18:31:39.998038
# Unit test for function find_template
def test_find_template():
    # Temp dir to clone the repo into
    repo_dir = "/home/audreyr/pycharm-debug-py3k/test_find_template"
    # Function to test
    template_dir = find_template(repo_dir)
    # What we expect to get
    expected = "/home/audreyr/pycharm-debug-py3k/test_find_template/{{cookiecutter.repo_name}}"
    assert template_dir == expected

# Generated at 2022-06-13 18:31:47.495435
# Unit test for function find_template
def test_find_template():
    from os import path
    from cookiecutter.tests.test_utils import TEST_TEMPLATES_DIR
    from cookiecutter.tests.test_utils import make_repo

    temp_dir = make_repo(TEST_TEMPLATES_DIR)
    template = find_template(temp_dir)
    assert path.isdir(template) is True

# Generated at 2022-06-13 18:31:57.622153
# Unit test for function find_template
def test_find_template():
    # TODO: refactor this test and move it to tests/test_finders.py
    import shutil
    import tempfile

    _, temp_dir = tempfile.mkstemp()

    # Create a temporary directory to clone into
    repo_dir = os.path.join(temp_dir, 'cookiecutter-pypackage')
    os.makedirs(repo_dir)

    # Create the project dir inside the repo
    project_dir = os.path.join(repo_dir, '{{cookiecutter.repo_name}}')
    os.makedirs(project_dir)

    # Test 1: Should find the project template dir.
    project_template = find_template(repo_dir)
    assert project_template == project_dir

    # Test 2: Should find the project template dir, even if

# Generated at 2022-06-13 18:32:00.646925
# Unit test for function find_template
def test_find_template():
    """ Find a cookiecutter template in a directory """

    # create a temp folder with a template
    from tempfile import mkdtemp
    repo_dir = mkdtemp()
    os.mkdir(os.path.join(repo_dir, '{{cookiecutter.project_name}}'))

    # run the function
    result = find_template(repo_dir)

    # check that the directory was found
    assert repo_dir in result
    assert '{{cookiecutter.project_name}}' in result

# Generated at 2022-06-13 18:32:04.810185
# Unit test for function find_template
def test_find_template():
    repo_dir = '/Users/danny/src/cookiecutter-django'
    project_template = find_template(repo_dir)
    assert project_template == '/Users/danny/src/cookiecutter-django/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:32:11.449137
# Unit test for function find_template
def test_find_template():
    from cookiecutter import utils
    this_dir = os.path.dirname(os.path.abspath(utils.__file__))
    repo_dir = os.path.abspath(os.path.join(this_dir, '..', 'tests', 'fake-repo'))
    assert find_template(repo_dir) == os.path.join(repo_dir, '{{cookiecutter.repo_name}}')

# Generated at 2022-06-13 18:32:21.977723
# Unit test for function find_template
def test_find_template():
    """Test search of the input directory for a Cookiecutter template."""
    import pytest
    from tempfile import mkdtemp
    from shutil import rmtree
    import os.path
    import os

    repo_dir_contents = [
        'index.rst',
        'cookiecutter.json',
        '{{cookiecutter.project_name}}',
    ]

    # Create a temporary directory for the test repo.
    repo_dir = mkdtemp()
    for fname in repo_dir_contents:
        open(os.path.join(repo_dir, fname), 'w').close()

    # Test that find_template() returns the expected template directory.
    expected_result = os.path.join(repo_dir, '{{cookiecutter.project_name}}')
    assert find_template

# Generated at 2022-06-13 18:32:27.006924
# Unit test for function find_template
def test_find_template():
    assert find_template("./tests/test-repo") == "./tests/test-repo/{{cookiecutter.repo_name}}"

# Generated at 2022-06-13 18:32:31.743381
# Unit test for function find_template
def test_find_template():
    repo_dir_contents = ['cookiecutter-pypackage', 'cookiecutter-pymodule']
    project_template = None
    for item in repo_dir_contents:
        if 'cookiecutter' in item and '{{' in item and '}}' in item:
            project_template = item
            break

    if project_template:
        project_template = os.path.join(repo_dir_contents, project_template)
        print('The project template appears to be %s', project_template)
        return project_template
    else:
        raise NonTemplatedInputDirException

test_find_template()

# Generated at 2022-06-13 18:32:49.265129
# Unit test for function find_template
def test_find_template():
    """Verify expected template path for a given input directory."""
    import tempfile

    def _create_cookiecutter_project(repo_dir):
        """Helper function to create Cookiecutter project files.

        :param repo_dir: Path to repo_dir.
        """
        project_template = os.path.join(repo_dir, 'cookiecutter-foobar')
        os.makedirs(project_template)
        open(os.path.join(project_template, 'README.md'), 'w').close()

    repo_dir = tempfile.mkdtemp()
    _create_cookiecutter_project(repo_dir)


# Generated at 2022-06-13 18:32:53.043071
# Unit test for function find_template
def test_find_template():
    """ Unit test for the find_template() function."""
    assert find_template('/home/audreyr/cookiecutter-pypackage') == '/home/audreyr/cookiecutter-pypackage/{{cookiecutter.project_name}}'

# Generated at 2022-06-13 18:32:55.638704
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        'tests', 'test-generate'
    )
    project_template = find_template(repo_dir)

    assert project_template == os.path.join(repo_dir, 'cookiecutter-pypackage')



# Generated at 2022-06-13 18:32:59.577703
# Unit test for function find_template
def test_find_template():
    """Verify function `find_template`."""
    path_to_test_templates = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'test-templates'
    )
    path_to_templated = os.path.join(path_to_test_templates, 'templated')
    assert(find_template(path_to_templated) == os.path.join(
        path_to_templated, '{{cookiecutter.repo_name}}'
    ))

# Generated at 2022-06-13 18:33:05.120983
# Unit test for function find_template
def test_find_template():
    """Test find_template function."""
    repo_dir = os.path.join(os.path.dirname(__file__), 'fake-repo')
    project_template = find_template(repo_dir)
    expected_result = os.path.join(repo_dir, '{{cookiecutter.repo_name}}')
    assert project_template == expected_result

# Generated at 2022-06-13 18:33:11.563625
# Unit test for function find_template
def test_find_template():
    assert find_template('tests/test-repo-pre/') == 'tests/test-repo-pre/{{cookiecutter.repo_name}}/'


# Generated at 2022-06-13 18:33:19.463692
# Unit test for function find_template
def test_find_template():
    """
    Tests function find_template
    """
    VALID_TEMPLATE = os.path.join('tests', 'fixtures', 'valid-template')
    INVALID_TEMPLATE = os.path.join('tests', 'fixtures', 'invalid-template')
    NON_TEMPLATED_TEMPLATE = os.path.join('tests', 'fixtures',
                                          'non-templated-template')

    valid_template_path = find_template(VALID_TEMPLATE)
    assert valid_template_path == os.path.join(VALID_TEMPLATE, '{{cookiecutter.repo_name}}')

    try:
        find_template(INVALID_TEMPLATE)
    except NonTemplatedInputDirException:
        pass

# Generated at 2022-06-13 18:33:28.110465
# Unit test for function find_template
def test_find_template():
    """
    Test find_template function with a mocked input directory.
    """
    input_directory = os.path.join(
        os.path.dirname(__file__),
        '..',
        'tests',
        'test-find-template'
    )
    project_template = find_template(input_directory)

    assert project_template == os.path.join(
        input_directory,
        'cookiecutter-pypackage'
    )

# Generated at 2022-06-13 18:33:34.877850
# Unit test for function find_template
def test_find_template():
    """Verify normal usage"""
    repo_dir = 'tests/fake-repo-tmpl'
    result = find_template(repo_dir)
    expected = os.path.join(repo_dir, '{{cookiecutter.repo_name}}')
    msg = 'find_template("{}") should be "{}"'.format(repo_dir, expected)
    assert result == expected, msg



# Generated at 2022-06-13 18:33:36.603140
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.join(os.path.expanduser('~'), 'cookiecutter')
    assert 'cookiecutter-pypackage' in find_template(repo_dir)

# Generated at 2022-06-13 18:34:07.314778
# Unit test for function find_template
def test_find_template():
    """Unit test for function find_template."""
    try:
        find_template('/non/existent/dir')
    except OSError:
        pass
    else:
        raise Exception('OSError should have been raised')

# Generated at 2022-06-13 18:34:18.124467
# Unit test for function find_template
def test_find_template():
    import tempfile
    from cookiecutter import utils

    tmp_dir = tempfile.mkdtemp()
    try:
        template_dir = utils.work_in(
            tmp_dir,
            lambda: utils.generate_files(
                (
                    ('{{cookiecutter.my_var}}', '{{cookiecutter.my_var}}'),
                    ('foo', 'foo'),
                    ('bar/', 'bar/'),
                    ('bar/baz', 'bar/baz'),
                )
            )
        )
        assert find_template(tmp_dir) == os.path.join(template_dir, '{{cookiecutter.my_var}}')
    finally:
        utils.rmtree(tmp_dir)

# Generated at 2022-06-13 18:34:22.646637
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.dirname(os.path.abspath(__file__))
    template = find_template(repo_dir)
    assert 'cookiecutter-template' in template

# Generated at 2022-06-13 18:34:23.793657
# Unit test for function find_template
def test_find_template():
    find_template('/home/user/foo')

# Generated at 2022-06-13 18:34:28.494262
# Unit test for function find_template
def test_find_template():
    from cookiecutter import utils

    if utils.is_windows():
        expected_project_template = 'tests\\test-input\\{{lower_case_project_name}}'
    else:
        expected_project_template = 'tests/test-input/{{lower_case_project_name}}'

    project_template = find_template('tests/test-output/clone')
    assert project_template == expected_project_template

# Generated at 2022-06-13 18:34:30.911844
# Unit test for function find_template
def test_find_template():
    assert find_template('../tests/test-repo-pre/') == '../tests/test-repo-pre/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:34:37.197154
# Unit test for function find_template
def test_find_template():
    """Test the find_template() function."""
    import os

    TEST_ROOT = os.path.join('tests', 'resources')
    os.chdir(TEST_ROOT)

    # Test 1
    repo_dir = 'fake_repo_pre_and_post_render'

    project_template = find_template(repo_dir)

    assert project_template == 'fake_repo_pre_and_post_render/{{cookiecutter.repo_name}}'


# Generated at 2022-06-13 18:34:40.738191
# Unit test for function find_template
def test_find_template():

    test_repo_dir = "/Users/audreyr/Develop/cookiecutter-pypackage"
    project_template = find_template(test_repo_dir)
    assert project_template == "/Users/audreyr/Develop/cookiecutter-pypackage/{{cookiecutter.repo_name}}"

# Generated at 2022-06-13 18:34:48.003559
# Unit test for function find_template
def test_find_template():
    os.system('rm -rf /tmp/cookiecutter-tryton')
    os.system('git clone https://github.com/fedefrappi/cookiecutter-tryton.git /tmp/cookiecutter-tryton')
    path_proyect = find_template('/tmp/cookiecutter-tryton')
    assert path_proyect == '/tmp/cookiecutter-tryton/cookiecutter-tryton'

# Generated at 2022-06-13 18:34:52.745512
# Unit test for function find_template
def test_find_template():
    """Verify function properly finds the project template."""
    project_template = find_template('tests/test-repo-pre/')
    assert project_template == 'tests/test-repo-pre/{{cookiecutter.repo_name}}'
    assert 'cookiecutter' in project_template
    assert '{{' in project_template
    assert '}}' in project_template