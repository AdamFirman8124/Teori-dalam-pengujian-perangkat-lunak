

# Generated at 2022-06-13 18:27:44.478916
# Unit test for function find_template
def test_find_template():
    from cookiecutter import utils
    from cookiecutter.exceptions import NonTemplatedInputDirException
    from mock import MagicMock

    utils.listdir = MagicMock(return_value=['some_project'])

    assert find_template('some_dir') == 'some_dir/some_project'

    utils.listdir = MagicMock(return_value=['some_project', 'some_other_project'])

    assert find_template('some_dir') == 'some_dir/some_project'

    utils.listdir = MagicMock(return_value=[])

    try:
        find_template('some_dir')
        assert False
    except NonTemplatedInputDirException:
        assert True

# Generated at 2022-06-13 18:27:49.255948
# Unit test for function find_template
def test_find_template():
    repo_dir = 'tests/files'
    project_template = 'tests/files/{{cookiecutter.repo_name}}'
    assert project_template == find_template(repo_dir)

# Generated at 2022-06-13 18:27:55.827408
# Unit test for function find_template
def test_find_template():
    import tempfile

    repo_dir = tempfile.mkdtemp()
    os.makedirs(os.path.join(repo_dir, 'my-product-{{ cookiecutter.repo_name }}-1.0'))
    template = find_template(repo_dir)

    assert os.path.basename(template) == 'my-product-{{ cookiecutter.repo_name }}-1.0'

# Generated at 2022-06-13 18:28:08.856986
# Unit test for function find_template
def test_find_template():
    import os
    import shutil
    import tempfile
    from cookiecutter.utils import find_template

    input_dir = tempfile.mkdtemp()
    template_file = 'template.txt'
    repo_dir = os.path.join(input_dir, '{{cookiecutter.repo_name}}')
    os.mkdir(repo_dir)
    template_path = os.path.join(repo_dir, template_file)

    with open(template_path, 'w') as f:
        f.write("{{cookiecutter.first_name}}")

    template_found = find_template(input_dir)

    assert template_path == template_found

    shutil.rmtree(input_dir)

# Generated at 2022-06-13 18:28:14.582649
# Unit test for function find_template
def test_find_template():
    """Assert that function find_template returns the correct directory."""
    os.chdir(os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        '..',
        'tests',
        'test-repo',
        'fake-repo-tmpl'
    ))

    template_dir = find_template('.')
    assert template_dir == 'cookiecutter-fake-repo-tmpl'



# Generated at 2022-06-13 18:28:19.519060
# Unit test for function find_template
def test_find_template():
    repo_dir = '/home/vagrant/cookiecutter-pypackage'
    assert find_template(repo_dir) == '/home/vagrant/cookiecutter-pypackage/{{cookiecutter.repo_name}}'



# Generated at 2022-06-13 18:28:24.216178
# Unit test for function find_template
def test_find_template():
    repo_dir = '/home/username/documents/cookiecutter-cookiecutter'
    assert find_template(repo_dir) == '/home/username/documents/\
cookiecutter-cookiecutter/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:28:32.178839
# Unit test for function find_template
def test_find_template():
    """Test the find_template() function."""
    # Test the case where project_dir is a Cookiecutter template.
    find_template_dir = os.path.join(
        os.path.dirname(__file__), '..',
        'tests', 'test-find-template', 'cookiecutter-pypackage'
    )
    assert find_template(find_template_dir)
    # Test the case where project_dir is not a Cookiecutter template.
    find_template_dir = os.path.join(
        os.path.dirname(__file__), '..',
        'tests', 'test-find-template', 'not-a-template'
    )
    assert find_template(find_template_dir)

# Generated at 2022-06-13 18:28:35.779595
# Unit test for function find_template
def test_find_template():
    path = '/home/username/directory-name-with-{{cookiecutter.argument_name}}'
    assert find_template(path) == '/home/username/directory-name-with-{{cookiecutter.argument_name}}'

# Generated at 2022-06-13 18:28:41.493143
# Unit test for function find_template
def test_find_template():
    """
    Test that find_template is able to find an existing template
    """
    repo_dir = os.path.join(
        os.path.dirname(__file__), '..', '..', '..', 'tests', 'fake-repo'
    )
    assert "cookiecutter-pypackage" in find_template(repo_dir)
    repo_dir = os.path.join(
        os.path.dirname(__file__), '..', '..', '..', 'tests', 'fake-repo-two'
    )
    assert "cookiecutter-python" in find_template(repo_dir)

# Generated at 2022-06-13 18:28:51.633068
# Unit test for function find_template
def test_find_template():
    os.chdir('functional_tests')

    template_directory = 'input'
    path_to_input_dir = find_template(template_directory)

    assert path_to_input_dir.endswith('input/{{cookiecutter.directory_name}}')
    path_to_input_dir = find_template(path_to_input_dir)

    assert path_to_input_dir.endswith('input/{{cookiecutter.directory_name}}/{{cookiecutter.directory_name}}')


# Generated at 2022-06-13 18:28:57.331261
# Unit test for function find_template
def test_find_template():
    """Test for function find_template."""

    import os
    from cookiecutter import utils

    repo_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    real_project_template = find_template(repo_dir)
    assert real_project_template == utils.make_absolute('tests/fake-repo-pre/{{cookiecutter.repo_name}}')

# Generated at 2022-06-13 18:28:59.939624
# Unit test for function find_template
def test_find_template():
    assert find_template('tests/test-output/fake-repo') == 'tests/test-output/fake-repo/cookiecutter-pypackage'

# Generated at 2022-06-13 18:29:10.970425
# Unit test for function find_template
def test_find_template():
    """Validate function for find template."""
    def _test_find_template_inner(input_dir, expected_output):
        assert expected_output == find_template(input_dir)

    _test_find_template_inner('tests/test-data/fake-repo-tmpl',
                              'tests/test-data/fake-repo-tmpl/{{cookiecutter.repo_name}}')

    _test_find_template_inner('tests/test-data/fake-repo-no-tmpl',
                              NonTemplatedInputDirException)

# Generated at 2022-06-13 18:29:12.702894
# Unit test for function find_template
def test_find_template():
    """Test find_template() function."""
    # TODO Implement.
    pass

# Generated at 2022-06-13 18:29:19.164211
# Unit test for function find_template
def test_find_template():
    this_dir = os.path.normpath(os.path.dirname(__file__))
    expected_template = os.path.join(this_dir, 'fake_repo_pre_jj-master/{{cookiecutter.repo_name}}')
    actual_template = find_template(os.path.join(this_dir, 'fake_repo_pre_jj-master'))
    assert actual_template == expected_template


# Generated at 2022-06-13 18:29:28.862843
# Unit test for function find_template
def test_find_template():
    import mock
    import shutil
    from cookiecutter.compat import TemporaryDirectory
    from cookiecutter.main import cookiecutter

    with TemporaryDirectory() as temp_dir:
        cookiecutter(
            'tests/fake-repo-tmpl/',
            no_input=True,
            output_dir=temp_dir,
            overwrite_if_exists=True,
            default_config=True,
        )
        test_template = find_template(temp_dir)
        assert test_template == os.path.join(temp_dir, 'fake-project-tmpl')
        test_template = find_template('tests/fake-repo-tmpl/')
        assert test_template == 'tests/fake-repo-tmpl/{{cookiecutter.project_name}}'

# Generated at 2022-06-13 18:29:34.761249
# Unit test for function find_template
def test_find_template():
    test_repo_dir = '/Users/audreyr/cookiecutter-test-template-master/'
    test_project_template = 'cookiecutter-test-template-{{cookiecutter.github_username}}-master'
    assert find_template(test_repo_dir) == os.path.join(test_repo_dir, test_project_template)

# Generated at 2022-06-13 18:29:40.550435
# Unit test for function find_template
def test_find_template():
    """Verify function for determining which child directory of cloned repo is
    the project template.
    """
    repo_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'fake-repo',
    )
    project_template = 'fake-repo-master/{{cookiecutter.repo_name}}'

    this_project_template = find_template(repo_dir)

    assert this_project_template == project_template

# Generated at 2022-06-13 18:29:53.832289
# Unit test for function find_template
def test_find_template():
    from cookiecutter import main
    from cookiecutter.utils import rmtree
    from tempfile import mkdtemp
    from pytest import raises
    from shutil import copytree

    # Create a temporary directory that will serve as the template repo
    template_repo_dir = mkdtemp()
    repo_dir = os.path.join(template_repo_dir, 'foobar')

    # Copy template from tests/test-templates/test-template to the repo dir
    test_template_dir = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        'test-templates',
        'test-template'
    )
    copytree(test_template_dir, repo_dir)

    # Make sure it copied correctly

# Generated at 2022-06-13 18:29:57.479866
# Unit test for function find_template
def test_find_template():
    """Check that the find_template function works as expected."""
    pass

# Generated at 2022-06-13 18:30:00.875189
# Unit test for function find_template
def test_find_template():
    repo_dir = '/code/cookiecutter-pypackage'
    project_template = find_template(repo_dir)
    assert 'cookiecutter-pypackage' in project_template
    assert '{{' in project_template
    assert '}}' in project_template

# Generated at 2022-06-13 18:30:04.771829
# Unit test for function find_template
def test_find_template():
    repo_dir = 'home/cookiebuilder/cookiecutters/test_cookiecutter'
    assert find_template(repo_dir) == 'home/cookiebuilder/cookiecutters/test_cookiecutter/my_cookiecutter_project'

# Generated at 2022-06-13 18:30:09.563380
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'test-find-template',
        'repo'
    )
    project_template = find_template(repo_dir)
    assert project_template == os.path.join(repo_dir, '{{cookiecutter.repo_name}}')

# Generated at 2022-06-13 18:30:16.653778
# Unit test for function find_template
def test_find_template():
    """Unit test for function `find_template`."""
    from cookiecutter.tests.fake_input_repo import fake_input_repo

    # Create a new, fake Cookiecutter input repo
    repository_dir = fake_input_repo()

    # Check that find_template finds the 'fake-repo-tmpl' directory
    returned_dir = find_template(repository_dir)
    returned_dir_basename = os.path.basename(returned_dir)
    assert returned_dir_basename == 'fake_repo_tmpl'

# Generated at 2022-06-13 18:30:29.251227
# Unit test for function find_template
def test_find_template():
    """Verify behavior of find_template()."""
    from git import Repo
    from cookiecutter.utils import get_user_config
    from cookiecutter import main

    repo_dir = 'tests/test-repo-pre/'
    config_file = get_user_config()
    context = config_file['default_context']

    # Clone the test repo
    main.cookiecutter(
        repo_dir, checkout='master', no_input=True,
        extra_context=context
    )

    # Get the path of the rendered template
    template_dir = find_template(repo_dir)

    # Verify that the rendered template contains the custom config
    with open(template_dir, 'r') as f:
        assert 'full_name: "Audrey Roy"' in f.read()

# Generated at 2022-06-13 18:30:34.651801
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    )
    assert find_template(repo_dir).endswith('tests/fake-repo-tmpl')

# Generated at 2022-06-13 18:30:39.923460
# Unit test for function find_template
def test_find_template():
    repo_dir = '/home/brian/code/cookiecutter/tests/fake-repo/'
    project_template = find_template(repo_dir)
    assert project_template == '/home/brian/code/cookiecutter/tests/fake-repo/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:30:44.077757
# Unit test for function find_template
def test_find_template():
    """Sample test for function find_template"""
    # It is expected to exist inside of tests/test-find-template/
    template_dir = 'test-find-template'

    # function find_template() is called
    found_template = find_template(template_dir)

    assert found_template == os.path.join('test-find-template','{{cookiecutter.project_slug}}')

# Generated at 2022-06-13 18:30:55.862738
# Unit test for function find_template
def test_find_template():
    from cookiecutter import utils
    from cookiecutter.exceptions import NonTemplatedInputDirException
    from tempfile import mkdtemp
    import shutil
    import os

    temp_dir = mkdtemp('-cookiecutter')
    old_dir = os.getcwd()

# Generated at 2022-06-13 18:31:06.996340
# Unit test for function find_template
def test_find_template():
    """Verify that find_template function works."""

    def _make_test_repo(tmpdir, repo_contents):
        """Create a local test repo with specified contents."""
        repo_dir = os.path.join(tmpdir.strpath, 'repo')
        os.mkdir(repo_dir)

        for item in repo_contents:
            if os.path.isdir(item):
                os.mkdir(item)
            else:
                open(item, 'a').close()

        for item in repo_contents:
            item_path = os.path.join(repo_dir, item)
            os.rename(item, item_path)

        return repo_dir

    from py import path
    import pytest

    # Create a temporary testing directory
    tmpdir = path.local

# Generated at 2022-06-13 18:31:10.595168
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.join(
        os.path.dirname(__file__), '..', 'tests', 'test-input'
    )
    project_template = find_template(repo_dir)
    assert 'test-app' in project_template
    assert os.path.exists(project_template)

# Generated at 2022-06-13 18:31:16.859322
# Unit test for function find_template
def test_find_template():
    pytest.raises(NonTemplatedInputDirException)
    find_template('repo_dir')

# Generated at 2022-06-13 18:31:22.310356
# Unit test for function find_template
def test_find_template():
    """Unit test."""
    assert find_template('tests/fake-repo/') == 'tests/fake-repo/{{cookiecutter.repo_name}}'
    assert find_template('tests/fake-repo-multi/') == 'tests/fake-repo-multi/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:31:28.729958
# Unit test for function find_template
def test_find_template():
    test_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'clones', 'djangopackage')
    project_template = find_template(test_dir)
    assert project_template == os.path.join(test_dir, '{{cookiecutter.repo_name}}')

# Generated at 2022-06-13 18:31:39.216936
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.abspath(os.path.join(
        os.path.dirname(__file__), '..', 'tests', 'fake-repo', 'input'
    ))
    project_template = find_template(repo_dir)
    expected_project_template_path = os.path.abspath(os.path.join(
        os.path.dirname(__file__), '..', 'tests', 'fake-repo', 'input', '{{cookiecutter.repo_name}}'
    ))
    assert project_template == expected_project_template_path

# Generated at 2022-06-13 18:31:43.166211
# Unit test for function find_template
def test_find_template():
    """Verify that find_template locates the project template."""
    from os import path
    from cookiecutter.tests.fake_project import random_project_dir

    repo_dir = random_project_dir()

    result = find_template(repo_dir)

    assert result == path.join(repo_dir, 'hello_world')

# Generated at 2022-06-13 18:31:49.941421
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.join(os.path.abspath('tests'), 'fake-repo-pre')
    assert find_template(repo_dir) == os.path.join(os.path.abspath('tests'), 'fake-repo-pre/{{cookiecutter.repo_name}}')



# Generated at 2022-06-13 18:31:54.111970
# Unit test for function find_template
def test_find_template():
    test_dir = os.path.join(os.path.dirname(__file__), 'test')
    project_template = find_template(test_dir)
    assert project_template



# Generated at 2022-06-13 18:32:00.161014
# Unit test for function find_template
def test_find_template():
    """
    Validate that find_template returns the correct template directory
    """
    repo_dir = os.path.dirname(os.path.abspath(__file__))
    expected_template = os.path.join(repo_dir, '{{ cookiecutter.repo_name }}')
    assert find_template(repo_dir) == expected_template

# Generated at 2022-06-13 18:32:03.056170
# Unit test for function find_template
def test_find_template():
    """Test find_template() function."""
    find_template('.')

# Generated at 2022-06-13 18:32:07.173725
# Unit test for function find_template
def test_find_template():
    assert find_template('tests/fake-repo-tmpl/') == 'tests/fake-repo-tmpl/{{cookiecutter.repo_name}}'



# Generated at 2022-06-13 18:32:08.728498
# Unit test for function find_template
def test_find_template():
    assert find_template('.') == '.cookiecutter-example'

# Generated at 2022-06-13 18:32:18.373868
# Unit test for function find_template
def test_find_template():

    import os
    import pytest

    test_dir = os.path.dirname(os.path.abspath(__file__))
    fixtures_dir = os.path.join(test_dir, 'fixtures')
    template_dir = os.path.join(fixtures_dir, 'files')
    os.chdir(template_dir)

    assert find_template(template_dir) == os.path.join(
        template_dir, '{{cookiecutter.repo_name}}'
    )

    # Check if NonTemplatedInputDirException raised if non-templated repo passed
    with pytest.raises(NonTemplatedInputDirException):
        find_template(os.path.join(fixtures_dir, 'hello-world'))

# Generated at 2022-06-13 18:32:24.237700
# Unit test for function find_template
def test_find_template():
    # repo_dir = join(dirname(__file__), 'fake-repo-pre-commit')
    # GitHub requires `/` as directory separator
    repo_dir = os.path.join('tests', 'fake-repo-pre-commit')
    repo_dir = repo_dir.replace('\\', '/')
    assert find_template(repo_dir) == repo_dir + '/{{cookiecutter.repo_name}}'
    logger.info('find_template passed the test.')

# Generated at 2022-06-13 18:32:24.728118
# Unit test for function find_template
def test_find_template():
    find_template()

# Generated at 2022-06-13 18:32:31.000766
# Unit test for function find_template
def test_find_template():
    # Check that the function correctly returns the template directory
    repo_dir = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        '..',
        '..',
        'tests',
        'fake-repo',
    )
    rel_path = find_template(repo_dir)
    full_path = os.path.join(repo_dir, rel_path)
    dir_name = os.path.basename(full_path)
    assert 'fake-repo-{{cookiecutter.repo_name}}' == dir_name

    # Check that the function detects if a template directory does not exist

# Generated at 2022-06-13 18:32:37.888706
# Unit test for function find_template
def test_find_template():
    """Check that the function correctly finds a template file."""
    import os
    import shutil
    import tempfile

    directory = tempfile.mkdtemp()

    # Create a dummy Cookiecutter project
    with open(os.path.join(directory, 'cookiecutter.json'), 'w') as f:
        f.write('{"key": "value"}')

    with open(os.path.join(directory, 'README.md'), 'w') as f:
        f.write('This is a test')

    # Create a template file
    template_filename = os.path.join(directory, '{{cookiecutter.key}}.html')
    with open(template_filename, 'w') as f:
        f.write('<html>')

    # Make sure the template file is found
    template_file = find_template

# Generated at 2022-06-13 18:32:48.399463
# Unit test for function find_template
def test_find_template():
    test_root = os.path.join(os.path.dirname(__file__), 'templates')
    
    test_cases = {
        #'absolute-template-dir': 'repo_without_cookiecutter_json',
        'repo_bad': 'repo_bad',
        'repo_missing_fields': 'repo_missing_fields',
        'repo_ok': '{{cookiecutter.folder_name}}',
        #'repo_with_other_templates': 'repo_with_other_templates'
    }

    for template_name, expected_result in test_cases.items():
        full_path = os.path.join(test_root, template_name)
        assert find_template(full_path) == os.path.join(full_path, expected_result)

# Generated at 2022-06-13 18:32:54.455015
# Unit test for function find_template
def test_find_template():
    """Test the find_template function to ensure that it returns the
    project template.
    """
    sample_repo_dir = os.path.abspath(os.path.join(
        os.path.dirname(__file__),
        '..',
        'tests',
        'test-repo'
    ))

    ret = find_template(sample_repo_dir)
    print(ret)
    assert 'tests/test-repo/{{cookiecutter.repo_name}}' in ret

# Generated at 2022-06-13 18:32:57.042069
# Unit test for function find_template
def test_find_template():
    pass

# Generated at 2022-06-13 18:33:01.893095
# Unit test for function find_template
def test_find_template():
    assert find_template("/home/Matt/cookiecutter-pypackage") == "/home/Matt/cookiecutter-pypackage/{{cookiecutter.repo_name}}"
    print("test_find_template ran with no errors")

test_find_template()

# Generated at 2022-06-13 18:33:07.852655
# Unit test for function find_template
def test_find_template():
    """Unit test for function find_template
    """
    test_dir = os.path.dirname(__file__)
    repo = os.path.join(test_dir, 'fake-repo-pre-123')
    project_template = find_template(repo)

    assert project_template == os.path.join(repo, 'fake-repo', '{{cookiecutter.repo_name}}')



# Generated at 2022-06-13 18:33:15.726905
# Unit test for function find_template
def test_find_template():
    """Validate that a template directory is detected when present."""
    # Create a fake directory to make sure that the function is getting
    # the directory list properly.
    test_dir = os.path.abspath(os.path.join(os.path.curdir, 'tests', 'fake-repo'))

    project_dir = find_template(test_dir)

    expected_dir = os.path.abspath(
        os.path.join(test_dir, 'cookiecutter-pypackage')
    )

    assert project_dir == expected_dir


# Generated at 2022-06-13 18:33:20.864493
# Unit test for function find_template
def test_find_template():
    assert find_template(os.path.join('tests', 'fake-repo-pre')) == os.path.join('tests', 'fake-repo-pre', 
        '{{cookiecutter.repo_name}}')

# Generated at 2022-06-13 18:33:23.073771
# Unit test for function find_template
def test_find_template():
    assert 'dir-{{ cookiecutter.dir1 }}-dir2' == find_template('you are here')

# Generated at 2022-06-13 18:33:30.264094
# Unit test for function find_template
def test_find_template():
    repo_dir = 'fake-repo'

    repo_dir_contents = os.path.join(repo_dir, 'test_cookiecutter')

    os.mkdir(repo_dir)
    os.mkdir(repo_dir_contents)

    project_template = find_template(repo_dir)
    assert (project_template is not None)

    shutil.rmtree(repo_dir)

# Generated at 2022-06-13 18:33:37.765251
# Unit test for function find_template
def test_find_template():
    # Test a correct output
    os.listdir = lambda x: ['cookiecutter', 'cookiecutter_{{cookiecutter.repo_name}}', 'cool_app', '{{cookiecutter.repo_name}}', '.git']
    # Assert that the correct output is found.
    assert find_template('.') == 'cookiecutter_{{cookiecutter.repo_name}}'
    # Test an incorrect output
    os.listdir = lambda x: ['cookiecutter', '.git']
    # Assert that the correct Exception is raised
    try:
        find_template('.')
    except NonTemplatedInputDirException:
        assert True
    else:
        assert False

# Generated at 2022-06-13 18:33:45.522859
# Unit test for function find_template
def test_find_template():
    import shutil
    import tempfile
    import os

    repo_dir = tempfile.mkdtemp()
    os.mkdir(os.path.join(repo_dir, 'my{{cookiecutter.repo_name}}'))
    os.mkdir(os.path.join(repo_dir, 'some_other_dir'))

    template = find_template(repo_dir)
    assert template.endswith(os.path.join('my{{cookiecutter.repo_name}}'))

    shutil.rmtree(repo_dir)

# Generated at 2022-06-13 18:33:52.779358
# Unit test for function find_template
def test_find_template():
    """Verify that find_template returns correct directory."""
    DIR = os.path.dirname(os.path.abspath(__file__))
    repo_dir = os.path.join(os.path.dirname(DIR), 'tests', 'test-repo')

    expect = 'basic/{{cookiecutter.project_name}}/{{cookiecutter.repo_name}}'
    result = find_template(repo_dir)
    folder = os.path.basename(result)
    assert folder == expect

# Generated at 2022-06-13 18:33:56.964801
# Unit test for function find_template
def test_find_template():
    assert find_template('test_repo') == 'test_repo/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:33:58.537563
# Unit test for function find_template
def test_find_template():
    """Verify find_template() looks for a cookiecutter template."""
    pass

# Generated at 2022-06-13 18:34:10.895159
# Unit test for function find_template
def test_find_template():
    test_find_template_path = 'tests/test-find-template'
    test_find_template_non_templated_path = 'tests/test-find-template-non-templated'
    test_find_template_missing_opening_curly = 'tests/test-find-template-missing-opening-curly'
    test_find_template_missing_closing_curly = 'tests/test-find-template-missing-closing-curly'
    test_find_template_missing_cookiecutter_string = 'tests/test-find-template-missing-cookiecutter-string'

    assert find_template(test_find_template_path) == test_find_template_path + '/{{cookiecutter.repo_name}}'


# Generated at 2022-06-13 18:34:17.415063
# Unit test for function find_template
def test_find_template():
    repo_dir = '/Users/robinandeer/Code/python/cookiecutter-pypackage'
    project_template = 'cookiecutter-pypackage'

    assert find_template(repo_dir) == os.path.join(repo_dir, project_template)

# Generated at 2022-06-13 18:34:24.116315
# Unit test for function find_template
def test_find_template():
    repo_dir = '/Users/audreyr/code/cookiecutter-pypackage'
    expected_project_template = '/Users/audreyr/code/cookiecutter-pypackage/{{cookiecutter.repo_name}}'

    project_template = find_template(repo_dir)
    assert expected_project_template == project_template

# Generated at 2022-06-13 18:34:31.200690
# Unit test for function find_template
def test_find_template():
    """Verify find_template function."""
    template_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'fake-repo',
        'cookiecutter-pypackage'
    )
    result = find_template(template_dir)
    assert result.endswith('fake-repo/cookiecutter-pypackage/{{cookiecutter.repo_name}}')

# Generated at 2022-06-13 18:34:36.880225
# Unit test for function find_template
def test_find_template():
    """find_template should return the correct path."""
    repo_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', '..', 'fake-repo')
    template = find_template(repo_dir)
    template_expected = os.path.join(repo_dir, '{{cookiecutter.repo_name}}')
    assert template == template_expected

# Generated at 2022-06-13 18:34:43.536992
# Unit test for function find_template
def test_find_template():
    """Check that find_template finds the repo directory in a standard repo."""

    repo_dir = os.path.join(
        os.path.dirname(__file__),
        'test-data',
        'fake-repo',
        '{{cookiecutter.repo_name}}'
    )
    expected_template = os.path.join(
        os.path.dirname(__file__),
        'test-data',
        'fake-repo',
        'cookiecutter-pypackage'
    )
    assert expected_template == find_template(repo_dir)

# Generated at 2022-06-13 18:34:48.591066
# Unit test for function find_template
def test_find_template():
    """
    Unit test for function find_template
    """
    repo_dir = 'Dummy-Project'
    project_template = find_template(repo_dir)


if __name__ == "__main__":
    test_find_template()

# Generated at 2022-06-13 18:34:52.712426
# Unit test for function find_template
def test_find_template():
    """
    Return path to template in tests/fake-repo-tmpl
    """
    assert find_template('/Users/audreyr/src/cookiecutter/tests/fake-repo-tmpl') == '/Users/audreyr/src/cookiecutter/tests/fake-repo-tmpl/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:35:02.569440
# Unit test for function find_template
def test_find_template():
    """Verify find_template() detects template."""
    test_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'fake-repo',
    )

    assert find_template(test_dir) == os.path.join(test_dir, u'{{cookiecutter.repo_name}}')


# Generated at 2022-06-13 18:35:11.691786
# Unit test for function find_template
def test_find_template():
    import shutil
    from cookiecutter.compat import ensure_ascii, remove_trailing_slash

    repo_dir = 'tests/test-find-template/'
    project_template = '{{cookiecutter.project_name}}'
    template_dir = os.path.join(repo_dir, project_template)
    os.mkdir(template_dir)
    test_file = os.path.join(template_dir, 'test.txt')
    test_file_contents = 'xyz'
    template_file = open(test_file, 'w')
    template_file.write(str(test_file_contents))
    template_file.close()

    logger = logging.getLogger()
    logger.debug = lambda *args: None

    assert find_template(repo_dir)

# Generated at 2022-06-13 18:35:12.516506
# Unit test for function find_template
def test_find_template():
    pass

# Generated at 2022-06-13 18:35:19.108813
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.abspath(os.path.dirname(__file__))
    repo_dir = os.path.join(repo_dir, 'test-find-template-repo')
    project_dir = find_template(repo_dir)
    assert project_dir.endswith('project_name')

# Generated at 2022-06-13 18:35:28.807346
# Unit test for function find_template
def test_find_template():
    """Verify function `find_template`."""
    import os
    import shutil
    import tempfile
    from cookiecutter import utils

    def cleanup_tmp_repo(repo_dir):
        shutil.rmtree(repo_dir)

    template_dirs = [
        'my-fake-repo/{{cookiecutter.repo_name}}',
        'my-fake-repo/{{cookiecutter.repo_name}}-repo',
        'my-fake-repo/cookiecutter-{{cookiecutter.repo_name}}',
        'my-fake-repo/cookiecutter-{{cookiecutter.repo_name}}-repo',
    ]

    # Create the fake repo
    repo_dir = tempfile.mkdtemp()


# Generated at 2022-06-13 18:35:30.717332
# Unit test for function find_template
def test_find_template():
    from cookiecutter import main
    main.cookiecutter('tests/fake-repo-pre/', no_input=True)

# Generated at 2022-06-13 18:35:37.735105
# Unit test for function find_template
def test_find_template():
    """Test that the correct template directory is found in a repo."""
    from cookiecutter import utils
    from cookiecutter.exceptions import NonTemplatedInputDirException
    from unittest.case import TestCase

    class TestFindTemplate(TestCase):
        """Test the `find_template` function."""

        def setUp(self):
            """Create a non-templated and templated directories."""
            self.repo_dir = os.path.abspath('/non-templated-dir')
            self.non_templated_dir = os.path.abspath(
                os.path.join(self.repo_dir, 'non-templated-dir')
            )
            os.makedirs(self.non_templated_dir)

            self.templated_

# Generated at 2022-06-13 18:35:43.140460
# Unit test for function find_template
def test_find_template():
    test_repo_dir = os.path.abspath(os.path.join(
        os.path.dirname(__file__),
        '..',
        'tests',
        'test-find-template',
        '{{cookiecutter.repo_name}}',
    ))
    assert find_template(test_repo_dir) == os.path.join(
        test_repo_dir,
        'cookiecutter-pypackage',
    )

# Generated at 2022-06-13 18:35:50.517954
# Unit test for function find_template
def test_find_template():
    """Verify proper functioning of find_template function."""
    # Create a fake project_dir to inspect
    this_dir = os.path.abspath(os.path.dirname(__file__))
    test_repo_dir = os.path.join(this_dir, 'fake-repo')
    template_path = find_template(test_repo_dir)
    assert template_path == os.path.join(test_repo_dir, '{{cookiecutter.repo_name}}')

# Generated at 2022-06-13 18:35:54.242793
# Unit test for function find_template
def test_find_template():
    """Verify find_template() returns the name of the child dir of the repo
    that contains our template.
    """
    assert find_template('tests/test-data') == 'tests/test-data/cookiecutter-pypackage-{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:36:06.138309
# Unit test for function find_template
def test_find_template():
    assert find_template('./tests/test-data/fake-repo-tmpl') == './tests/test-data/fake-repo-tmpl/{{cookiecutter.repo_name}}'


# Generated at 2022-06-13 18:36:13.419317
# Unit test for function find_template
def test_find_template():
    template_path = os.path.join(
        os.path.dirname(__file__), '..', '..', 'tests', 'test-input',
        '{{cookiecutter.repo_name}}'
    )

    found_path = find_template(
        os.path.dirname(template_path)
    )

    assert found_path == template_path

# Generated at 2022-06-13 18:36:23.844023
# Unit test for function find_template
def test_find_template():
    from tempfile import mkdtemp
    from cookiecutter.prompt import read_user_yes_no
    import shutil

    repo_json = """
{
    "cookiecutters": ["fake_user/dummy-repo-master"],
    "repo": "https://github.com/fake_user/dummy-repo.git"
}"""

    # Create a temporary directory
    repo_dir = mkdtemp()
    os.mkdir(os.path.join(repo_dir, 'foo'))
    os.mkdir(os.path.join(repo_dir, '{{cookiecutter.repo}}'))
    os.mkdir(os.path.join(repo_dir, '{{cookiecutter.repo}}-master'))


# Generated at 2022-06-13 18:36:32.160904
# Unit test for function find_template
def test_find_template():
    """Unit test for function find_template."""
    import os
    from shutil import rmtree

    # Create a temporary directory and get its path
    this_dir, this_filename = os.path.split(__file__)
    tmp_dir = os.path.join(this_dir, "the_test_dir")

    # Create a few files and a subdirectory
    os.mkdir(tmp_dir)
    for name in ["bar", "baz", "{{cookiecutter.foo}}quux", "quux"]:
        with open(os.path.join(tmp_dir, name), "w") as f:
            f.write(name)
    os.mkdir(os.path.join(tmp_dir, "quux"))

    # Check to make sure it can find the project template

# Generated at 2022-06-13 18:36:40.611109
# Unit test for function find_template
def test_find_template():
    """Test that find_template works when given a valid input."""
    import tempfile
    import shutil
    from os.path import join

    from cookiecutter.exceptions import (
        RepositoryNotFound,
        InvalidMode,
        NonTemplatedInputDirException
    )

    # Create a bogus repo
    repo_dir = tempfile.mkdtemp()

# Generated at 2022-06-13 18:36:44.966654
# Unit test for function find_template
def test_find_template():
    """
    Finding template

    Tests finding a template in a given directory
    """
    template = find_template('tests/fake-repo-tmpl')
    assert template == 'tests/fake-repo-tmpl/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:36:47.654453
# Unit test for function find_template
def test_find_template():
    """Test find_template function."""

    project_template = find_template('repo_dir')
    assert project_template == 'repo_dir/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:36:50.523759
# Unit test for function find_template
def test_find_template():
    """Unit test for function find_template."""
    try:
        find_template(os.path.abspath('./tests/fake-repo-pre/'))
    except NonTemplatedInputDirException:
        logger.debug('The project template was not found.')
    else:
        assert False, 'This should not happen.'

# Generated at 2022-06-13 18:36:54.642194
# Unit test for function find_template
def test_find_template():
    """Test that find_template finds the appropriate directory."""
    try:
        template_dir = find_template('tests/fake-repo-pre/')
    except Exception:
        template_dir = None

    assert template_dir == os.path.realpath('tests/fake-repo-pre/{{cookiecutter.repo_name}}')

# Generated at 2022-06-13 18:37:01.621823
# Unit test for function find_template
def test_find_template():
    """
    Unit test for function find_template
    """
    import pytest
    from cookiecutter.main import cookiecutter

    # create a fake cookiecutter template
    result = cookiecutter('tests/fake-repo-tmpl', output_dir='tests')
    assert 'fake-repo-tmpl' in result['project_dir']

    project_template = find_template('tests/fake-repo-tmpl')

    assert os.path.exists(project_template)

    # clean up the fake cookiecutter template
    import shutil
    shutil.rmtree(project_template)
    shutil.rmtree('tests/fake-repo-tmpl')

# Generated at 2022-06-13 18:37:18.767155
# Unit test for function find_template
def test_find_template():
    assert find_template('tests/test-output/fake-repo') == 'tests/test-output/fake-repo/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:37:27.596129
# Unit test for function find_template
def test_find_template():
    """
    find_template() finds 'cookiecutter' directory with {{ and }}

    :returns: '{repo_dir}/cookiecutter-pypackage/' or raises error.
    """
    # Check that find_template doesn't freak out if template name has dashes
    repo_dir = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        '..',
        'fake-repo-tmpl',
    )
    answer = os.path.join(repo_dir, 'cookiecutter-pypackage')
    assert find_template(repo_dir) == answer

    # Check that find_template finds a template with underscores

# Generated at 2022-06-13 18:37:40.014042
# Unit test for function find_template
def test_find_template():
    # Test with a templated repo dir
    template_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'fake-repo'
    )
    pd = find_template(template_dir)
    assert pd == os.path.join(template_dir, '{{cookiecutter.repo_name}}')

    # Test with a non-templated repo dir should raise an error
    non_templated_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'fixture'
    )
    try:
        pd = find_template(non_templated_dir)
    except Exception as e:
        assert type(e) is NonTemplatedInput