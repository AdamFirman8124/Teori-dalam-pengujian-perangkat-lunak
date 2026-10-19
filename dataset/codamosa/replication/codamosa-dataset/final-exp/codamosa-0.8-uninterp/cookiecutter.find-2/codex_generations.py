

# Generated at 2022-06-13 18:27:40.924786
# Unit test for function find_template
def test_find_template():
    repo_dir = "tests/fake-repo/"
    project_template = find_template(repo_dir)
    assert project_template.endswith("fake-repo/{{cookiecutter.repo_name}}")

# Generated at 2022-06-13 18:27:49.738064
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        'tests',
        'fake-repo-pre'
    )
    project_template_dir = find_template(repo_dir=repo_dir)
    assert 'fake-project' in project_template_dir
    assert 'cookiecutter' in project_template_dir

# Generated at 2022-06-13 18:27:56.535173
# Unit test for function find_template
def test_find_template():
    """Test the find_template function."""
    try:
        find_template('test/fake-repo/')
    except NonTemplatedInputDirException as e:
        msg = 'Could not find cookiecutter.json in fake repository'
        assert msg in str(e), str(e)
        # assert "Could not find cookiecutter.json in fake repository" in str(e)
    else:
        assert False, "NonTemplatedInputDirException not raised"

# Generated at 2022-06-13 18:28:10.300313
# Unit test for function find_template

# Generated at 2022-06-13 18:28:14.450118
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        '..',
        'tests',
        'test-find-template'
    )
    assert find_template(repo_dir) == os.path.join(repo_dir, '{{cookiecutter.dir_name}}')


# Generated at 2022-06-13 18:28:17.890433
# Unit test for function find_template
def test_find_template():
    assert find_template('examples/multiple-repos') == 'examples/multiple-repos/{{cookiecutter.project_name}}'

# Generated at 2022-06-13 18:28:23.284055
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.abspath('tests/fake-repo-tmpl')
    os.listdir(repo_dir)
    assert find_template(repo_dir) == os.path.join(repo_dir, 'project_name{{cookiecutter.project_slug}}')

# Generated at 2022-06-13 18:28:32.177649
# Unit test for function find_template
def test_find_template():
    """Verify find_template()."""
    import shutil
    import tempfile
    import textwrap

    new_dir = tempfile.mkdtemp()
    new_dir_contents = textwrap.dedent("""\
        foo
        first_cookiecutter_dir__{{cookiecutter.directory}}__
        second_cookiecutter_dir__{{cookiecutter.directory}}__
        bar
    """.split('\n'))

    for item in new_dir_contents:
        os.mkdir(os.path.join(new_dir, item))

    assert find_template(new_dir) == '{0}/second_cookiecutter_dir__{{cookiecutter.directory}}__'.format(new_dir)

    shutil.rmtree(new_dir)

# Generated at 2022-06-13 18:28:36.686187
# Unit test for function find_template
def test_find_template():
    test_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'test-template')

    found_template = find_template(test_dir)

    assert found_template == os.path.join(test_dir, '{{cookiecutter.repo_name}}')

# Generated at 2022-06-13 18:28:41.440367
# Unit test for function find_template
def test_find_template():
    """Unit test for function find_template"""
    repo_dir = os.environ['HOME']
    project_template = find_template(repo_dir)
    print('project template: %s' % project_template)
    assert project_template


if __name__ == '__main__':
    test_find_template()

# Generated at 2022-06-13 18:28:49.557677
# Unit test for function find_template
def test_find_template():
    """Verify that the function returns the expected project template."""
    expected_output = (
        'C:\\source\\cookiecutter-pypackage\\{{cookiecutter.repo_name}}'
    )

    output = find_template('C:\\source\\cookiecutter-pypackage')

    assert output == expected_output

# Generated at 2022-06-13 18:28:54.980752
# Unit test for function find_template
def test_find_template():
    """Verify that the function successfully finds the project template."""
    template_dir = os.path.join(
        os.path.dirname(__file__),
        'tests/test-template'
    )
    project_template = find_template(template_dir)
    assert project_template == os.path.join(template_dir, '{{cookiecutter.repo_name}}')



# Generated at 2022-06-13 18:29:03.637612
# Unit test for function find_template
def test_find_template():
    """Verify function find_template()."""
    template_dir = os.path.join(
        os.path.dirname(__file__),
        'tests/files/cookiecutters/fake-repo-tmpl',
    )

# Generated at 2022-06-13 18:29:07.801628
# Unit test for function find_template
def test_find_template():
    input_dir = 'test/test_dir/testdir'
    project_template = find_template(input_dir)
    assert 'test/test_dir/testdir/test-project' in project_template

# Generated at 2022-06-13 18:29:18.001873
# Unit test for function find_template
def test_find_template():
    import shutil
    import tempfile

    repo_dir = tempfile.mkdtemp()

    logger.debug('Made a temporary working directory at %s', repo_dir)

    src = os.path.join(os.path.dirname(__file__), os.pardir, 'tests',
                       'fake-repo-tmpl')
    logger.debug('The test source dir is %s', src)
    shutil.copytree(src, repo_dir)

    logger.debug('Copied the test repo to %s', repo_dir)

    project_template = find_template(repo_dir)

    logger.debug('The test project template is at %s', project_template)

    assert os.path.exists(project_template)    
    shutil.rmtree(repo_dir)

# Generated at 2022-06-13 18:29:26.982222
# Unit test for function find_template
def test_find_template():
    repo_dir = '/Users/audreyr/cookiecutter-pypackage'
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
    else:
        raise Exception

# Generated at 2022-06-13 18:29:31.207345
# Unit test for function find_template
def test_find_template():
    # Setup
    repo_dir = os.path.abspath(__file__)
    project_template = '{{cookiecutter.project_name}}'

    # Actual
    actual_template = find_template(repo_dir)

    # Expected
    expected_template = os.path.join(repo_dir, project_template)

    # Test
    assert actual_template == expected_template

# Generated at 2022-06-13 18:29:34.905015
# Unit test for function find_template
def test_find_template():
    repo_dir = '../tests/fake-repo/'
    project_template = find_template(repo_dir)
    assert 'fake-repo-master/{{cookiecutter.repo_name}}' == project_template

# Generated at 2022-06-13 18:29:41.251004
# Unit test for function find_template
def test_find_template():
    """Verify that find_template() works correctly"""

    # Set up test variables
    repo_dir = os.path.join('tests','sample_repos','cookiecutter-pypackage')
    repo_dir_contents = os.listdir(repo_dir)
    project_template = None
    for item in repo_dir_contents:
        if 'cookiecutter' in item and '{{' in item and '}}' in item:
            project_template = item
            break

    assert find_template(repo_dir) == os.path.join(repo_dir,project_template)

# Generated at 2022-06-13 18:29:44.526364
# Unit test for function find_template
def test_find_template():
    """Test find_template with non-existent data."""
    repo_dir = 'foo'
    assert find_template(repo_dir) == 'foo'

# Generated at 2022-06-13 18:29:53.450242
# Unit test for function find_template
def test_find_template():
    repo_dir_contents = [
        'pyramid_project', 'django_project', 'cookiecutter-cookiecutter',
        'cookiecutter-pypackage', 'cookiecutter-audreyr'
    ]
    repo_dir = repo_dir_contents[2]
    result = find_template(repo_dir)
    assert result == 'repo_dir'


# Generated at 2022-06-13 18:29:58.348844
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.join('tests', 'fake-repo-tmpl')
    project_template = find_template(repo_dir)
    assert project_template == os.path.join(repo_dir, '{{cookiecutter.repo_name}}')
    return project_template

# Generated at 2022-06-13 18:30:06.884244
# Unit test for function find_template
def test_find_template():
    """
    """
    cwd = os.path.dirname(os.path.abspath(__file__))
    repo_dir = os.path.join(cwd, 'tests/fake-repo-tmpl')

    # If find_template() works correctly, it should find
    # 'fake-repo-tmpl/cookiecutter-pypackage{{cookiecutter.project_slug}}'
    expected_path = os.path.join(
        repo_dir,
        'cookiecutter-pypackage{{cookiecutter.project_slug}}'
    )
    assert expected_path == find_template(repo_dir)

# Generated at 2022-06-13 18:30:15.875823
# Unit test for function find_template
def test_find_template():
    """Verify proper operation of the find_template function."""

    # Path to a fixture that is a git repository.
    git_repo_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        os.pardir,
        'tests',
        'test-repo',
        '{{cookiecutter.repo_name}}',
    )

    expected_result = os.path.join(git_repo_dir, '{{cookiecutter.repo_name}}')
    actual_result = find_template(git_repo_dir)
    assert expected_result == actual_result

# Generated at 2022-06-13 18:30:21.968426
# Unit test for function find_template
def test_find_template():
    """Test find_template function."""
    assert find_template('tests/fake-repo-1') == 'tests/fake-repo-1/{{cookiecutter.repo_name}}'
    assert find_template('tests/fake-repo-2') == 'tests/fake-repo-2/{{cookiecutter.repo_name}}'
    assert find_template('tests/fake-repo-3') == 'tests/fake-repo-3/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:30:24.172761
# Unit test for function find_template
def test_find_template():
    """
    test to see if the find_template function returns the expected output
    """
    assert find_template(repo_dir='~/.cookiecutters') == '~/.cookiecutters/template'

# Generated at 2022-06-13 18:30:28.454438
# Unit test for function find_template
def test_find_template():
    """Unit test for function find_template"""
    repo_dir = "tests/fake-repo/"
    project_template = find_template(repo_dir)
    assert project_template == "tests/fake-repo/cookiecutter-pypackage/"


# Generated at 2022-06-13 18:30:29.308882
# Unit test for function find_template
def test_find_template():
    pass


# Generated at 2022-06-13 18:30:36.065491
# Unit test for function find_template
def test_find_template():
    assert find_template(os.path.join(
                                os.getcwd(), 'tests', 'fake-repo-pre')) == \
                                os.path.join(os.getcwd(), 'tests', 'fake-repo-pre',
                                'fake_project_{{cookiecutter.project_slug}}')

# Generated at 2022-06-13 18:30:44.175052
# Unit test for function find_template
def test_find_template():
    import io
    import shutil
    import tempfile

    from .context import Context

    def touch(path):
        with io.open(path, 'a'):
            os.utime(path, None)

    repo_dir = tempfile.mkdtemp()
    touch(os.path.join(repo_dir, 'cookiecutter.json'))
    touch(os.path.join(repo_dir, 'file.txt'))
    touch(os.path.join(repo_dir, 'README.rst'))
    touch(os.path.join(repo_dir, '{{cookiecutter.repo_name}}'))

    project_template = find_template(repo_dir)

    assert project_template.endswith('{{cookiecutter.repo_name}}')

    shut

# Generated at 2022-06-13 18:30:55.865258
# Unit test for function find_template
def test_find_template():
    from cookiecutter.utils import rmtree
    from tempfile import mkdtemp

    template = mkdtemp()
    context = mkdtemp()
    template_dir = os.path.join(template, '{{cookiecutter.repo_name}}')
    os.makedirs(template_dir)

    try:
        assert find_template(template) == template_dir
        rmtree(template)
        rmtree(context)
    except Exception:
        rmtree(template)
        rmtree(context)
        raise

# Generated at 2022-06-13 18:30:59.156823
# Unit test for function find_template
def test_find_template():
    """Test that the project template was found in the repository."""
    assert find_template('./tests/fake-repo-template-dir') == './tests/fake-repo-template-dir/cookiecutter-{{cookiecutter.github_username}}'

# Generated at 2022-06-13 18:31:05.964911
# Unit test for function find_template
def test_find_template():
    """
    Unit tests for function find_template
    """
    assert find_template('/repo_dir') == '/repo_dir/{{cookiecutter.project_slug}}'

    try:
        find_template('/repo_dir')
    except NonTemplatedInputDirException:
        assert True

    assert find_template('{{cookiecutter.project_slug}}') == '{{cookiecutter.project_slug}}'

    try:
        find_template('{{cookiecutter.project_slug}}')
    except NonTemplatedInputDirException:
        assert True

# Generated at 2022-06-13 18:31:18.454435
# Unit test for function find_template
def test_find_template():
    """
    Unit test for cookiecutter.find_template
    """

    # Create a project template in a temporary folder
    import tempfile
    temp_dir = tempfile.mkdtemp()

    project_template = os.path.join(temp_dir, 'cookiecutter-project')
    os.mkdir(project_template)

    # Create the project template with dummy content
    template_content = os.path.join(project_template, 'temp_content')
    with open(template_content, 'w') as content:
        content.write('This is a dummy project template')

    template_found = find_template(temp_dir)

    assert template_found == project_template

# Generated at 2022-06-13 18:31:20.384573
# Unit test for function find_template
def test_find_template():
    template_path = find_template('/Users/audreyr/cookiecutter-pypackage')
    print(template_path)

# Generated at 2022-06-13 18:31:23.934506
# Unit test for function find_template
def test_find_template():
    repo_dir = '/home/vagrant/sync/cookiecutter-pypackage'
    project_template = find_template(repo_dir)
    assert project_template == '/home/vagrant/sync/cookiecutter-pypackage/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:31:36.857574
# Unit test for function find_template
def test_find_template():
    """An example of testing a function."""
    import os
    import shutil

    tmp_dir = 'example_tmp'

    os.mkdir(tmp_dir)
    os.mkdir(os.path.join(tmp_dir, 'example_repo'))
    os.mkdir(os.path.join(tmp_dir, 'example_repo', '{{cookiecutter.repo_name}}'))

    assert find_template(os.path.join(tmp_dir, 'example_repo')) == os.path.join(tmp_dir, 'example_repo', '{{cookiecutter.repo_name}}')

    shutil.rmtree(tmp_dir)

    assert 1==1

# Generated at 2022-06-13 18:31:40.960844
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.join(
        os.path.dirname(__file__),
        '..',
    )

    assert 'cookiecutter-pypackage' in find_template(repo_dir)

# Generated at 2022-06-13 18:31:48.402786
# Unit test for function find_template
def test_find_template():
    """Test find_template function."""
    import tempfile

    with tempfile.TemporaryDirectory() as tmpdir:
        os.makedirs(os.path.join(tmpdir, '{{cookiecutter.repo_name}}'))
        assert find_template(tmpdir) == os.path.join(
            tmpdir, '{{cookiecutter.repo_name}}')

# Generated at 2022-06-13 18:31:54.678269
# Unit test for function find_template
def test_find_template():
    """Test if Cookiecutter is able to identify the project template
    in a non-templated directory.
    """
    repo_dir = '.cookiecutter-test'

    project_template = find_template(repo_dir)
    assert project_template == '.cookiecutter-test/cookiecutter-pypackage'

# Generated at 2022-06-13 18:31:59.888541
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'tests', 'test-input', 'repo-tmpl'))
    assert find_template(repo_dir) == 'repo-tmpl/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:32:07.490422
# Unit test for function find_template
def test_find_template():
    import codecs
    import shutil
    import tempfile
    import re

    test_dir = tempfile.mkdtemp()
    logger.debug('Create test directory: %s', test_dir)

    project_dir = os.path.join(test_dir, '{{cookiecutter.repo_name}}')
    os.mkdir(project_dir)
    logger.debug('Created test project dir: %s', project_dir)

    readme = os.path.join(project_dir, 'README.rst')
    with codecs.open(readme, 'w', encoding='utf-8') as f:
        f.write("Welcome to {{cookiecutter.repo_name}}.")
    logger.debug('Created test project README: %s', readme)


# Generated at 2022-06-13 18:32:15.758512
# Unit test for function find_template
def test_find_template():
    """Test if find_template finds template."""
    repo1 = "/home/joy/Desktop/advent/cookiecutter-django"
    temp_file1 = os.path.join(repo1, "{{cookiecutter.project_name}}")
    actual_template1 = find_template(repo1)
    assert actual_template1 == temp_file1

    repo2 = "/home/joy/Desktop/advent/cookiecutter-pypackage"
    temp_file2 = os.path.join(repo2, "{{cookiecutter.repo_name}}")
    actual_template2 = find_template(repo2)
    assert actual_template2 == temp_file2

# Generated at 2022-06-13 18:32:19.775455
# Unit test for function find_template
def test_find_template():
    """Test the find_template function."""
    template_dir = "/User/audreyr/cookiecutter-pypackage"
    result = find_template(template_dir)
    assert result == "/User/audreyr/cookiecutter-pypackage/package"

# Generated at 2022-06-13 18:32:27.598133
# Unit test for function find_template
def test_find_template():
    """Function for testing find_template()."""
    from .test.test_utils import generate_files
    from .exceptions import NonTemplatedInputDirException
    from .compat import mkdtemp

    def _remove(path):
        import os
        import shutil
        if os.path.exists(path):
            shutil.rmtree(path)

    temp_directory = mkdtemp()

    repo_dir = os.path.join(temp_directory, 'my-repo')
    os.makedirs(repo_dir)
    os.makedirs(os.path.join(repo_dir, '{{cookiecutter.repo_name}}'))

    repo_dir2 = os.path.join(temp_directory, 'my-repo2')

# Generated at 2022-06-13 18:32:35.463899
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '..',
            'tests',
            'fake-repo',
            '{{cookiecutter.repo_name}}'
        )
    )
    project_template = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '..',
            'tests',
            'fake-repo',
            '{{cookiecutter.repo_name}}',
            '{{cookiecutter.project_name}}'
        )
    )
    assert find_template(repo_dir) == project_template

# Generated at 2022-06-13 18:32:38.421628
# Unit test for function find_template
def test_find_template():
    repo_dir = "C:\cookiecutter-pypackage"
    template = "cookiecutter-pypackage"
    test = find_template(repo_dir)
    assert test == template

# Generated at 2022-06-13 18:32:48.493429
# Unit test for function find_template
def test_find_template():
    """Check that the correct subdirectory is found in the test repo."""
    # Get the directory of this script, so we can isolate the test repo
    dir_of_this_file = os.path.dirname(__file__)
    # The test repo is located in ./fake-repo/ inside the tests directory
    fake_repo_dir = os.path.join(dir_of_this_file, 'fake-repo')
    # The subdirectory named like a template is in ./fake-repo/tests/fake-repo/
    fake_repo_dir_project_template = os.path.join(fake_repo_dir, 'tests', 'fake-repo')

    # Try to find the subdirectory that looks like a project template
    found_project_template = find_template(fake_repo_dir)

    #

# Generated at 2022-06-13 18:32:54.511385
# Unit test for function find_template
def test_find_template():
    """Test the find_template function."""
    repo_dir = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__), '..', '..', 'tests', 'fake-repo-tmpl'
        )
    )
    project_template = find_template(repo_dir)
    assert project_template == os.path.join(repo_dir, 'fake-repo-{{cookiecutter.repo_name}}')

# Generated at 2022-06-13 18:32:59.615101
# Unit test for function find_template
def test_find_template():
    import os
    from cookiecutter.tests.test_find import our_path

    repo_dir = os.path.join(our_path, '..', 'fake-repo-pre-renames')
    find_template(repo_dir)

# Generated at 2022-06-13 18:33:11.988591
# Unit test for function find_template
def test_find_template():
    # The repo should not have cookiecutter in its path
    assert find_template('/path/to/repository/cookiecutter') is None

    # The repo should have cookiecutter in its path
    repo = '/path/to/repository/{{cookiecutter.repo_name}}'
    assert find_template(repo) == repo


# Generated at 2022-06-13 18:33:19.680510
# Unit test for function find_template
def test_find_template():

    if os.path.isdir('./tests/fake-repo-pre/'):
        repo_dir_contents = os.listdir('./tests/fake-repo-pre/')
        for item in repo_dir_contents:
            os.remove('./tests/fake-repo-pre/' + item)
        os.rmdir('./tests/fake-repo-pre/')

    os.mkdir('./tests/fake-repo-pre/')

    open('./tests/fake-repo-pre/random1.txt', 'w').close()
    open('./tests/fake-repo-pre/random2.txt', 'w').close()
    open('./tests/fake-repo-pre/random3.txt', 'w').close()

# Generated at 2022-06-13 18:33:25.520569
# Unit test for function find_template
def test_find_template():
    """Test that find_template is found from other functions in this module."""
    try:
        find_template(os.path.dirname(os.path.abspath(__file__)))
        assert True
    except NonTemplatedInputDirException:
        assert False

# Generated at 2022-06-13 18:33:30.537979
# Unit test for function find_template
def test_find_template():
    """Ensure that find_template finds the template."""
    repo_dir = 'tests/test-find-template'
    project_dir = 'tests/test-find-template/cookiecutter-pypackage'
    find_template(repo_dir)
    assert os.path.exists(project_dir)

# Generated at 2022-06-13 18:33:36.617762
# Unit test for function find_template
def test_find_template():
    # Normal template dir
    assert find_template('tests/fake-repo-tmpl/') == 'tests/fake-repo-tmpl/{{cookiecutter.repo_name}}'

    # Non-templated directory
    try:
        find_template('tests/fake-repo-pre/')
        raise Exception("Did not raise NonTemplatedInputDirException")
    except NonTemplatedInputDirException:
        pass

# Generated at 2022-06-13 18:33:47.140570
# Unit test for function find_template
def test_find_template():
    """ Test if the function find_template is working properly OR Not."""
    import shutil
    import tempfile

    from cookiecutter.main import cookiecutter

    def make_fake_repo(repo_dir):
        """ Make a fake repository for testing. """
        repo_dir_contents = (
            'my_fake_project_dir', 'my_fake_project_dir_two', 'another_dir'
        )
        for item in repo_dir_contents:
            full_item = os.path.join(repo_dir, item)
            os.mkdir(full_item)

    temp_repo_dir = tempfile.mkdtemp()

    # Create a fake repository
    make_fake_repo(temp_repo_dir)


# Generated at 2022-06-13 18:34:01.972518
# Unit test for function find_template
def test_find_template():
    """Validate the find_template function"""
    import tempfile
    import shutil
    import git
    import os

    # make a temporary directory
    repo_dir = tempfile.mkdtemp()

    # initialize a git repository in the temporary directory
    repo = git.Repo.init(repo_dir)

    # create an empty file
    cookiecutter_json = os.path.join(repo_dir, 'cookiecutter.json')
    open(cookiecutter_json, 'a').close()

    # add and commit the empty file
    repo.index.add([cookiecutter_json])
    repo.index.commit("Initial commit")

    # create a second file with template delimiters
    templated_file = os.path.join(repo_dir, '{{"cookiecutter"}}.json')

# Generated at 2022-06-13 18:34:05.707772
# Unit test for function find_template
def test_find_template():
    from tests.example_templates import example_repo

    assert find_template(example_repo) == 'tests/example-repo/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:34:13.934266
# Unit test for function find_template
def test_find_template():
    """Verify find_template() correctly finds the project template."""
    # Setup
    import pytest
    import tempfile
    import shutil
    import textwrap

    template = textwrap.dedent(
        '''\
        {{cookiecutter.repo_name}}_repo/
            {{cookiecutter.repo_name}}/
                hooksmoother/
                    __init__.py
            docs/
                Makefile
            tox.ini
        '''
    )

    template_dir = tempfile.mkdtemp()
    repo_dir = os.path.join(template_dir, '{{cookiecutter.repo_name}}_repo')
    os.mkdir(repo_dir)

# Generated at 2022-06-13 18:34:23.135482
# Unit test for function find_template
def test_find_template():
    # Given template path
    template_path = 'github.com/audreyr/cookiecutter-pypackage'

    # When find_template is called with the template path
    project_template = find_template(template_path)

    # Then it should return the correct path to the project template
    expected_path = 'github.com/audreyr/cookiecutter-pypackage/{{cookiecutter.repo_name}}'
    assert project_template == expected_path

# Generated at 2022-06-13 18:34:38.197419
# Unit test for function find_template
def test_find_template():
    assert find_template('tests/fake-repo-pre/') == 'tests/fake-repo-pre/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:34:42.465084
# Unit test for function find_template
def test_find_template():
    this_dir = os.path.dirname(os.path.abspath(__file__))
    repo_dir = os.path.join(this_dir, '..', 'tests', 'test-find-project-tmpl')
    project_template = find_template(repo_dir)
    assert 'nested_project_tmpl' in project_template

# Generated at 2022-06-13 18:34:47.402167
# Unit test for function find_template
def test_find_template():
    """
    Function to find template
    """
    input_directory = "/home/yxa/workspace/openpilot/python/cookiecutter-pypackage"

# Generated at 2022-06-13 18:34:48.056951
# Unit test for function find_template
def test_find_template():
    pass

# Generated at 2022-06-13 18:34:50.613116
# Unit test for function find_template
def test_find_template():
    find_template("C:/Users/Tobias/Documents/GitHub/cookiecutter-data-science/cookiecutter-data-science")

# Generated at 2022-06-13 18:34:55.166380
# Unit test for function find_template
def test_find_template():
    """Test that find_template correctly finds the project template."""
    test_dir = 'tests/test-find-template/fake-repo/'
    assert find_template(test_dir) == (
        'tests/test-find-template/fake-repo/fake-repo-{{cookiecutter.repo_name}}'
    )

# Generated at 2022-06-13 18:35:00.354362
# Unit test for function find_template
def test_find_template():
    """
    Test find_teplate function
    """
    from cookiecutter.main import cookiecutter
    repo_dir = cookiecutter("tests/test-find-template/")
    return find_template(repo_dir)

# Generated at 2022-06-13 18:35:10.756937
# Unit test for function find_template
def test_find_template():
    """Verify the correct template is returned by the function."""
    import tempfile

    def _gen_file():
        """Generate a temporary file."""
        fd, fp = tempfile.mkstemp()
        os.close(fd)
        return fp

    file1 = _gen_file()
    file2 = _gen_file()
    file3 = _gen_file()
    file4 = _gen_file()

    tmpl_file = tempfile.mkdtemp()

    os.rename(file1, os.path.join(tmpl_file, 'cookiecutter-{{cookiecutter.repo_name}}'))
    os.rename(file2, os.path.join(tmpl_file, 'cookiecutter-my-cool-project'))

# Generated at 2022-06-13 18:35:18.105571
# Unit test for function find_template

# Generated at 2022-06-13 18:35:22.245186
# Unit test for function find_template
def test_find_template():
    from cookiecutter import repository

    repo_dir = repository.clone("https://github.com/audreyr/cookiecutter-pypackage.git")
    assert find_template(repo_dir)

# Generated at 2022-06-13 18:35:49.176854
# Unit test for function find_template
def test_find_template():
    find_template(repo_dir='FakeRepo')
    NonTemplatedInputDirException

# Generated at 2022-06-13 18:35:54.840795
# Unit test for function find_template
def test_find_template():
    """ Test the ability to find the template in the root of a repo directory.
    """
    repo_dir = '/home/vanessa/code/cookiecutter-pypackage'
    project_template = find_template(repo_dir)
    expected = '/home/vanessa/code/cookiecutter-pypackage/{{cookiecutter.repo_name}}'
    assert project_template == expected


# Generated at 2022-06-13 18:36:02.645429
# Unit test for function find_template
def test_find_template():
    """Verify that find_template() finds the correct directory."""
    abs_path = os.path.abspath(__file__)
    test_dir = os.path.dirname(abs_path)
    repo_dir = os.path.join(test_dir, 'test-data', 'fake-repo')
    expected_project_template = os.path.join(repo_dir, 'fake-cookiecutter-project')

    result = find_template(repo_dir)

    assert result == expected_project_template

# Generated at 2022-06-13 18:36:16.763009
# Unit test for function find_template
def test_find_template():
    """Test for find_template.

    This is an exemplary test for find_template.
    """
    def _mock_listdir(path):
        """Mock os.listdir."""
        return ['{{cookiecutter.repo_name}}']

    def _mock_isfile(path):
        """Mock os.path.isfile."""
        return False

    original_listdir = os.listdir
    original_isfile = os.path.isfile

    os.listdir = _mock_listdir
    os.path.isfile = _mock_isfile

    try:
        find_template('/some/path')
    except Exception as e:
        assert type(e) == NonTemplatedInputDirException

    finally:
        os.listdir = original_listdir
        os.path

# Generated at 2022-06-13 18:36:27.444509
# Unit test for function find_template
def test_find_template():
    """
    Test case for find_template()
    """
    from tempfile import mkdtemp
    from shutil import rmtree
    from distutils.dir_util import copy_tree

    from .exceptions import NonTemplatedInputDirException

    logger.info('=== Running function test: test_find_template() ===')

    logger.debug('Creating temp directory to clone into')
    temp_dir = mkdtemp(prefix='cookiecutter-')
    temp_dir = temp_dir.rstrip('/') + '/'
    logger.debug('Temp directory: %s', temp_dir)

    logger.debug('Copying tests/test-data/test-template to %s', temp_dir)
    copy_tree('tests/test-data/test-template', temp_dir)


# Generated at 2022-06-13 18:36:28.069146
# Unit test for function find_template
def test_find_template():
    pass

# Generated at 2022-06-13 18:36:30.283507
# Unit test for function find_template
def test_find_template():
    # TODO
    find_template('tests/test-repo-pre')
# test_find_template()

# Generated at 2022-06-13 18:36:32.737517
# Unit test for function find_template
def test_find_template():
    repo_dir = '/Users/audreyr/cookiecutter-pypackage'
    template = '/Users/audreyr/cookiecutter-pypackage/{{cookiecutter.repo_name}}'
    assert find_template(repo_dir) == template

# Generated at 2022-06-13 18:36:37.258330
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.abspath('cookiecutter-templates/test/test-template')
    project_template = os.path.abspath('cookiecutter-templates/test/test-template/{{% cookiecutter.project_name %}}')
    assert find_template(repo_dir) == project_template

# Generated at 2022-06-13 18:36:48.560729
# Unit test for function find_template
def test_find_template():
    from . import utils
    temp_dir = utils.temp_dir()

    tmp_dir = os.path.join(temp_dir, 'repo-dir')
    os.makedirs(tmp_dir)

    assert find_template(temp_dir) == None

    os.makedirs(os.path.join(tmp_dir, '{{cookiecutter.repo_name}}'))

    assert find_template(temp_dir) == os.path.join(tmp_dir, '{{cookiecutter.repo_name}}')

    #TODO: need more tests to test out different cases including
    #TODO: multiple template directories, etc.

    utils.remove_temp_dir(temp_dir)