

# Generated at 2022-06-13 18:27:35.773023
# Unit test for function find_template
def test_find_template():
    assert find_template()

# Generated at 2022-06-13 18:27:36.314880
# Unit test for function find_template
def test_find_template():
    pass

# Generated at 2022-06-13 18:27:44.875561
# Unit test for function find_template
def test_find_template():
    from cookiecutter.main import cookiecutter

    # Create a fake git repo
    context_file = os.path.join(os.getcwd(), 'fake-repo', 'fake-repo.json')
    repo_dir = os.path.join(os.getcwd(), '{{cookiecutter.repo_name}}')
    template = find_template(repo_dir)

    # Run cookiecutter against the simple template

# Generated at 2022-06-13 18:27:48.425707
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'fake-repo-tmpl'
    )

    expected = os.path.join(repo_dir, '{{cookiecutter.repo_name}}')
    result = find_template(repo_dir)

    assert expected == result

# Generated at 2022-06-13 18:27:50.489370
# Unit test for function find_template
def test_find_template():
    # template_dir_contents = os.listdir()
    find_template('/Users/axil/PycharmProjects/cookiecutter-pypackage/')

test_find_template()

# Generated at 2022-06-13 18:27:54.875533
# Unit test for function find_template
def test_find_template():
    """Test finding project template."""
    assert find_template('invalid_path') == None
    assert find_template('tests/fake-repo-pre/') == 'tests/fake-repo-pre/{{cookiecutter.repo_name}}'


# Generated at 2022-06-13 18:27:59.649497
# Unit test for function find_template
def test_find_template():
    test_dir_contents = ['a file', 'a_dir', '{{cookiecutter.repo_name}}', 'another_dir']
    assert find_template(test_dir_contents) == '{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:28:11.799365
# Unit test for function find_template
def test_find_template():
    """Verify function find_template() works as expected."""
    logger.debug("Starting tests")
    import os
    import tempfile
    # Create a temporary directory
    repo_dir = tempfile.mkdtemp()
    dir_template = os.path.join(repo_dir, '{{cookiecutter.repo_name}}')
    os.mkdir(dir_template)
    for i in range(3):
        os.mkdir(os.path.join(repo_dir, "test{0}".format(i)))
    assert find_template(repo_dir) == dir_template
    os.rmdir(dir_template)
    os.rmdir(os.path.join(repo_dir, "test0"))

# Generated at 2022-06-13 18:28:17.741472
# Unit test for function find_template
def test_find_template():
    """
    Unit test for function find_template
    """
    print("\nTESTING FUNCTION: find_template()\n")

    # Get absolute path to directory containing test data
    DIR_PATH = os.path.dirname(os.path.abspath(__file__))
    TEST_DATA_DIR = os.path.join(DIR_PATH, 'test_data')

    # Make list of test directories
    TEST_DIRS = [os.path.join(DIR_NAME) for DIR_NAME in os.listdir(TEST_DATA_DIR)]

    # Make list of expected results
    EXPECTED_RESULTS = ['{{cookiecutter.repo_name}}',
                        '{{cookiecutter.repo_name}}',
                        'test']

    #  Loop through test directories

# Generated at 2022-06-13 18:28:20.255638
# Unit test for function find_template
def test_find_template():
    """Test find_template function."""
    # FIXME: create tests for find_template
    assert True

# Generated at 2022-06-13 18:28:27.368566
# Unit test for function find_template
def test_find_template():
    test_repo_dir = os.path.join(os.getcwd(), 'tests/test-find-repo/input')
    test_project_template = os.path.join(test_repo_dir, '{{ cookiecutter.repo_name }}')

    assert find_template(test_repo_dir) == test_project_template

# Generated at 2022-06-13 18:28:31.169123
# Unit test for function find_template
def test_find_template():
    """
    Test find_template function.
    """
    # for now just testing the function finding the correct file
    # the logic needs to be cleaned up a lot

    os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),
        '..', '..', 'tests', 'test-folders'))
    repo_dir = 'repo-with-cookiecutter-dir'

    assert find_template(repo_dir) == os.path.join(repo_dir, '{{cookiecutter.test_cookiecutter_dir_name}}')

# Generated at 2022-06-13 18:28:37.797804
# Unit test for function find_template
def test_find_template():
    """Verify that find_template returns the proper directory."""
    repo_dir_contents = os.listdir(repo_dir)
    project_template = None
    for item in repo_dir_contents:
        if 'cookiecutter' in item and '{{' in item and '}}' in item:
            project_template = item
            break
    assert project_template == '{{cookiecutter.project_name}}', (
        "find_template did not properly return the templated directory")

# Generated at 2022-06-13 18:28:46.028587
# Unit test for function find_template
def test_find_template():
    from cookiecutter import main
    from tempfile import mkdtemp
    from shutil import rmtree
    from os import mkdir
    from os.path import join
    from subprocess import check_output
    from os import listdir

    temp_dir = mkdtemp()
    source_dir = join(temp_dir, '{{cookiecutter.repo_name}}')
    mkdir(source_dir)
    check_output(['git', 'init', temp_dir], cwd=temp_dir)
    main.cookiecutter(
        source_dir, extra_context={'repo_name': 'gh_jhermann'}
    )
    assert len(listdir(temp_dir)) == 2
    assert listdir(temp_dir)[0] == 'gh_jhermann'

# Generated at 2022-06-13 18:28:52.522304
# Unit test for function find_template
def test_find_template():
    """Function to test find_template function."""
    # import pdb; pdb.set_trace()
    assert find_template(
        'C:\Python34\Scripts\cookiecutter'
        '\tests\test-data\git-repos\jquery-plugin') == (
        'C:\Python34\Scripts\cookiecutter'
        '\tests\test-data\git-repos\jquery-plugin'
        '\{{cookiecutter.repo_name}}')



# Generated at 2022-06-13 18:28:59.370797
# Unit test for function find_template
def test_find_template():
    template_dir = os.path.abspath(
        os.path.join(os.path.dirname(__file__),
        '..',
        '..',
        'tests',
        'test-input-example-cookiecutter',
        '{{cookiecutter.repo_name}}'))
    template_dir_parent = os.path.abspath(
        os.path.join(os.path.dirname(__file__),
        '..',
        '..',
        'tests',
        'test-input-example-cookiecutter'))
    assert(template_dir == find_template(template_dir_parent))


# Generated at 2022-06-13 18:29:08.986913
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.abspath(os.path.join(
        os.path.dirname(__file__),
        '../skeleton'
    ))
    project_template = os.path.abspath(os.path.join(
        repo_dir,
        '{{cookiecutter.repo_name}}'
    ))
    assert find_template(repo_dir) == project_template



# Generated at 2022-06-13 18:29:13.447378
# Unit test for function find_template
def test_find_template():
    assert find_template("c:\\Users\\David\\.cookiecutters\\cookiecutter-pypackage")== 'c:\\Users\\David\\.cookiecutters\\cookiecutter-pypackage\\{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:29:16.752148
# Unit test for function find_template
def test_find_template():
    assert find_template('C:\Github\cookiecutter-pypackage') == 'C:\Github\cookiecutter-pypackage\{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:29:18.399292
# Unit test for function find_template
def test_find_template():
    pass
#    os.dir
#    assert find_template() == expected_project_template

# Generated at 2022-06-13 18:29:27.618605
# Unit test for function find_template
def test_find_template():
    # Test that the valid repo_dir is returned
    res = find_template('tests/test-with-cookiecutterjson')
    assert res == 'tests/test-with-cookiecutterjson/{{cookiecutter.wow}}'

    # Test that an exception is raised when no project template found
    # ~ from cookiecutter.exceptions import NonTemplatedInputDirException
    import pytest
    with pytest.raises(NonTemplatedInputDirException):
        res = find_template('tests/test-without-cookiecutterjson')
        assert res == None

test_find_template()

# Generated at 2022-06-13 18:29:33.317151
# Unit test for function find_template
def test_find_template():
    import py
    import mock

    repo_dir = py.path.local('tests/fake-repo-tmpl/')
    project_template = 'tests/fake-repo-tmpl/{{cookiecutter.repo_name}}'

    assert find_template(repo_dir) == project_template
    assert find_template(mock.Mock())

# Generated at 2022-06-13 18:29:41.698068
# Unit test for function find_template
def test_find_template():
    import shutil
    import tempfile
    temp_directory = tempfile.mkdtemp(prefix='cookiecutter-')
    cookiecutters = [
        '{{cookiecutter.repo_name}}',
        '{{cookiecutter.repo_name}}-master',
        'cookiecutter.{{cookiecutter.repo_name}}',
    ]

    for cookiecutter in cookiecutters:
        os.makedirs(os.path.join(temp_directory, cookiecutter))

    # Make a non-template to test that it is ignored.
    os.makedirs(os.path.join(temp_directory, 'not-a-template'))
    os.makedirs(os.path.join(temp_directory, 'not-a-template'))
    assert find_template(temp_directory).end

# Generated at 2022-06-13 18:29:48.749761
# Unit test for function find_template
def test_find_template():
    """Verify that find_template() returns the correct value."""
    repo_dir = os.path.join(os.path.dirname(__file__), '../fake-repo')
    project_template = find_template(repo_dir)

    project_template_check = os.path.join(repo_dir, 'fake-project')
    assert project_template == project_template_check

# Generated at 2022-06-13 18:29:55.051124
# Unit test for function find_template
def test_find_template():
    answer_1 = find_template('tests/test-repo-pre/')
    answer_2 = find_template('tests/test-repo-post/')
    assert answer_1 == 'tests/test-repo-pre/{{cookiecutter.repo_name}}'
    assert answer_2 == 'tests/test-repo-post/'

# Generated at 2022-06-13 18:30:00.164981
# Unit test for function find_template
def test_find_template():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    repo_dir = os.path.join(base_dir, 'tests', 'fake-repo-pre-rendered')
    project_template = find_template(repo_dir)
    assert project_template == os.path.join(repo_dir, 'cookiecutter-pypackage')

# Generated at 2022-06-13 18:30:09.118678
# Unit test for function find_template
def test_find_template():
    import shutil
    import tempfile

    repo_dir = tempfile.mkdtemp()
    os.makedirs(os.path.join(repo_dir, 'foo', 'bar'))
    os.makedirs(os.path.join(repo_dir, 'cookiecutter-{{ cookiecutter.repo_name }}'))
    os.makedirs(os.path.join(repo_dir, 'hello-world'))

    project_template = find_template(repo_dir)

    assert project_template == os.path.join(repo_dir, 'cookiecutter-{{ cookiecutter.repo_name }}')

    shutil.rmtree(repo_dir)

# Generated at 2022-06-13 18:30:12.281901
# Unit test for function find_template
def test_find_template():
    """Asserts that find_template returns the project_template.
    """
    assert 'basic_app' == find_template('/Users/mjbright/git/webapp-test')

# Generated at 2022-06-13 18:30:22.856876
# Unit test for function find_template
def test_find_template():
    """
    Test function to find template
    """
    import tempfile
    from shutil import rmtree
    import os

    temp_dir = tempfile.mkdtemp()
    try:
        repo_dir_contents = ['my_project', os.path.join('{{','cookiecutter','}}','project_name')]
        for item in repo_dir_contents:
            os.makedirs(os.path.join(temp_dir, item))
        project_template = find_template(temp_dir)
        assert project_template == os.path.join(temp_dir, '{{', 'cookiecutter', '}}', 'project_name'), \
            'The project template does not appear to be {{cookiecutter.project_name}}'
    finally:
        rmtree(temp_dir)

test_

# Generated at 2022-06-13 18:30:28.251393
# Unit test for function find_template
def test_find_template():
    """Test function find_template()."""
    import shutil

    os.mkdir('cookiecutter-test')
    os.mkdir('cookiecutter-test/cookiecutter-test-project')
    os.mkdir('cookiecutter-test/cookiecutter-test-project-2')
    os.mkdir('cookiecutter-test/cookiecutter-test-project-2-2')
    shutil.copy('README.md', 'cookiecutter-test')
    project_template = os.path.join(os.getcwd(), 'cookiecutter-test/cookiecutter-test-project')
    assert find_template('cookiecutter-test') == project_template
    shutil.rmtree('cookiecutter-test')


# Generated at 2022-06-13 18:30:42.335474
# Unit test for function find_template
def test_find_template():
    # Test successful find
    project_directory = os.path.abspath(os.path.join(
        os.path.dirname(__file__),
        '..', 'tests', 'fake-repo-tmpl'))
    proj_tmpl = find_template(project_directory)

    assert os.path.normpath(proj_tmpl) == os.path.normpath(os.path.join(project_directory, '{{cookiecutter.repo_name}}'))

    # Test non-templated input directory
    project_directory = os.path.abspath(os.path.join(
        os.path.dirname(__file__),
        '..', 'tests', 'fake-repo-pre'))

# Generated at 2022-06-13 18:30:47.078022
# Unit test for function find_template
def test_find_template():
    repo_dir = 'tests/fake-repo/'

    project_template = find_template(repo_dir)
    assert project_template == 'tests/fake-repo/{{cookiecutter.repo_name}}'


# Do not use find_template, use find_template_in_working_directory instead.

# Generated at 2022-06-13 18:30:57.560626
# Unit test for function find_template
def test_find_template():
    # Passing test
    repo_dir = os.path.join(
        'tests', 'test-find-template', 'basic_repo', 'cookiecutter-pypackage'
    )
    got = find_template(repo_dir)
    expected = os.path.join(repo_dir, '{{cookiecutter.repo_name}}')
    assert got == expected

    # Test for error case
    repo_dir = os.path.join(
        'tests', 'test-find-template', 'basic_repo', 'no_templated_dir'
    )
    import pytest
    with pytest.raises(NonTemplatedInputDirException):
        find_template(repo_dir)

# Generated at 2022-06-13 18:31:05.563429
# Unit test for function find_template
def test_find_template():
    """Find project template from cloned repo_dir."""
    import os
    import shutil
    from cookiecutter.config import DEFAULT_CONFIG
    
    config = DEFAULT_CONFIG
    repo_dir = os.path.join(config["replay_dir"], "cookiecutter-pypackage")
    project_template = find_template(repo_dir)
    assert project_template == os.path.join(repo_dir, "{{cookiecutter.repo_name}}")
    
    shutil.rmtree(config["replay_dir"])
    print("test_find_template: pass")


# Generated at 2022-06-13 18:31:11.693856
# Unit test for function find_template
def test_find_template():
    """Verify that no template directory is found in a non-Cookiecutter repo."""
    from cookiecutter import generate
    template_dir = generate.find_template('tests/test-repo-tmpl')
    assert template_dir == os.path.abspath('tests/test-repo-tmpl')

# Generated at 2022-06-13 18:31:16.673886
# Unit test for function find_template
def test_find_template():
    """Verify that find_template returns the most obvious template."""
    import tempfile

    test_dir = tempfile.mkdtemp()
    os.makedirs(os.path.join(test_dir, '{{cookiecutter.repo_name}}'))
    os.makedirs(os.path.join(test_dir, 'cookiecutter-pypackage'))
    os.makedirs(os.path.join(test_dir, 'cookiecutter-djangopackage'))

    found_template = find_template(test_dir)

    assert found_template == os.path.join(test_dir, '{{cookiecutter.repo_name}}')



# Generated at 2022-06-13 18:31:25.849374
# Unit test for function find_template
def test_find_template():
    """
    Finds the template in the tests dir.
    """
    import pytest

    base_dir = os.path.abspath(os.path.dirname(__file__))
    repo_dir = os.path.join(base_dir, 'test-templates', 'foo-bar')
    logger.debug('base dir is {0}'.format(base_dir))
    logger.debug('Repo dir is {0}'.format(repo_dir))
    logger.debug('Repo dir contents are {0}'.format(os.listdir(repo_dir)))
    project_template = find_template(repo_dir)
    assert project_template is not None
    assert 'foo-bar' in project_template
    assert '{{cookiecutter' in project_template
    assert '.git' not in project_

# Generated at 2022-06-13 18:31:29.101201
# Unit test for function find_template
def test_find_template():
    find_template("C:\\Users\\Admin\PycharmProjects\cookiecutter-pypackage")

#test_find_template()

# Generated at 2022-06-13 18:31:33.334777
# Unit test for function find_template
def test_find_template():
    repo_dir = 'tests/fake-repo-tmpl'
    assert find_template(repo_dir) == 'tests/fake-repo-tmpl/cookiecutter-pypackage'

# Generated at 2022-06-13 18:31:40.876390
# Unit test for function find_template
def test_find_template():
    """Test the find_template function using a temporary folder"""
    import tempfile
    from os.path import join
    from shutil import rmtree

    from cookiecutter import find_template

    template_dir = '{{project_name}}'
    tmp_dir = tempfile.mkdtemp()
    os.mkdir(join(tmp_dir, template_dir))

    template_dirname = find_template(tmp_dir)
    assert template_dirname == join(tmp_dir, template_dir)

    rmtree(tmp_dir)

# Generated at 2022-06-13 18:31:55.288728
# Unit test for function find_template
def test_find_template():
    """
    Test to ensure find_template() works as expected.
    """
    import shutil
    import tempfile

    repo_dir = tempfile.mkdtemp()
    project_dir = os.path.join(repo_dir, 'cookiecutter-pypackage')
    os.makedirs(project_dir)

    try:
        project_template = find_template(repo_dir)

        assert project_template == project_dir, (
            "find_template() failed to find the project template directory.")

    except NonTemplatedInputDirException as e:
        assert False, "Failed to find the project template directory."

    finally:
        shutil.rmtree(repo_dir)

# Generated at 2022-06-13 18:32:06.017716
# Unit test for function find_template

# Generated at 2022-06-13 18:32:15.424800
# Unit test for function find_template
def test_find_template():
    """Verify that find_template is working."""
    import tempfile
    import shutil
    import textwrap

    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()

    # Create a repo_dir subdirectory
    repo_dir = os.path.join(temp_dir, 'repo_dir')
    os.makedirs(repo_dir)

    # Create a {{cookiecutter.project_name}} directory
    project_template_dir = os.path.join(repo_dir, '{{cookiecutter.project_name}}')
    os.makedirs(project_template_dir)

    # Create a README.md, with a cookiecutter variable in it

# Generated at 2022-06-13 18:32:17.856072
# Unit test for function find_template
def test_find_template():
    repo_dir = os.getcwd()
    assert find_template(repo_dir) == './cookiecutter-pypackage'

# Generated at 2022-06-13 18:32:26.391305
# Unit test for function find_template
def test_find_template():
    import pytest
    from cookiecutter import exceptions
    from cookiecutter import utils

    input_dir = 'tests/fake-repo-tmpl/'

    assert find_template('tests/fake-repo-tmpl/') == 'tests/fake-repo-tmpl/{{cookiecutter.repo_name}}/'

    with pytest.raises(exceptions.NonTemplatedInputDirException):
        assert find_template('tests/fake-repo-pre/')
        assert find_template('tests/fake-repo-post/')

    utils.rmtree('tests/fake-repo-tmpl/bad_template_dir')

# Generated at 2022-06-13 18:32:28.280328
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.join(os.path.dirname(__file__), 'test-repo-pre')
    assert 'test-repo-pre' in find_template(repo_dir)

# Generated at 2022-06-13 18:32:34.161486
# Unit test for function find_template
def test_find_template():
    assert find_template('tests/test-repo-pre/') == 'tests/test-repo-pre/{{cookiecutter.repo_name}}'
    assert find_template('tests/fake-repo/') == 'tests/fake-repo/{{cookiecutter.repo_name}}'


# Generated at 2022-06-13 18:32:47.324074
# Unit test for function find_template
def test_find_template():
    """Verify find_template returns correct relative directory path."""
    from cookiecutter.utils import rmtree
    from cookiecutter import config

    # Temporarily change to testing directory
    current_dir = os.getcwd()
    os.chdir(config.USER_HOME_PATH)

    # Clone into a temporary folder, run the function under test, delete temporary folder
    import shutil
    temp_dir = 'tests/files/test-find-template'
    temp_dir = os.path.join(config.USER_HOME_PATH, temp_dir)
    shutil.copytree('tests/files/test-find-template-skeleton', temp_dir)
    project_template_dir = find_template(temp_dir)
    rmtree(temp_dir)

    # Revert to original working directory

# Generated at 2022-06-13 18:32:52.154231
# Unit test for function find_template
def test_find_template():
    """Test finding the project template within a directory"""
    from cookiecutter.main import cookiecutter

    result = cookiecutter('tests/test-cookiecutter-repo')
    assert find_template(result) == os.path.join(result, '{{cookiecutter.repo_name}}')


# Generated at 2022-06-13 18:32:57.867366
# Unit test for function find_template
def test_find_template():

    test_dir = os.path.join(os.path.dirname(__file__), 'test_repo')
    template_path = find_template(test_dir)

    assert os.path.exists(template_path)

# Generated at 2022-06-13 18:33:06.326164
# Unit test for function find_template
def test_find_template():
    assert find_template('my_repo')

# Generated at 2022-06-13 18:33:16.734276
# Unit test for function find_template
def test_find_template():
    template_dir = 'tests/test-find-template'
    abs_template_dir = os.path.abspath(template_dir)


# Generated at 2022-06-13 18:33:20.582877
# Unit test for function find_template
def test_find_template():
    repo_dir = '/repo/dir'
    repo_dir_contents = [
        'license',
        'cookiecutter_stuff',
        'README.md',
        '{{cookiecutter.repo_name}}',
    ]
    with patch('cookiecutter.find.os.listdir', return_value=repo_dir_contents):
        assert find_template(repo_dir) == '/repo/dir/{{cookiecutter.repo_name}}'



# Generated at 2022-06-13 18:33:23.171706
# Unit test for function find_template
def test_find_template():
    template_dir = 'fixtures/fake-repo'
    assert "cookiecutter-pypackage" == os.path.basename(find_template(template_dir))

# Generated at 2022-06-13 18:33:26.019475
# Unit test for function find_template
def test_find_template():
    """Test of find_template function."""
    find_template('/home/audreyr/cookiecutter-pypackage')

# Generated at 2022-06-13 18:33:27.191196
# Unit test for function find_template
def test_find_template():
    # TODO
    pass

# Generated at 2022-06-13 18:33:34.832457
# Unit test for function find_template
def test_find_template():
    """Find template function returns expected result."""
    repo_dir = os.path.join(
        os.path.dirname(__file__),
        '..',
        '..',
        'tests',
        'test-output',
        'no-user-config',
        'cookiecutter-djangopackage'
    )

    assert find_template(repo_dir) == os.path.join(
        repo_dir, '{{cookiecutter.repo_name}}'
    )

# Generated at 2022-06-13 18:33:38.521772
# Unit test for function find_template
def test_find_template():
    temp_dir = os.path.join('tests', 'files', 'test-repo-pre', 'fake-repo')
    expected = os.path.join(temp_dir, '{{cookiecutter.repo_name}}')
    result = find_template(temp_dir)
    assert result == expected

# Generated at 2022-06-13 18:33:39.068846
# Unit test for function find_template
def test_find_template():
    pass

# Generated at 2022-06-13 18:33:48.524352
# Unit test for function find_template
def test_find_template():
    """Test the find_template function."""

    from .compat import TemporaryDirectory
    from .utils import rmtree

    project_template_name = '{{cookiecutter.repo_name}}'

    with TemporaryDirectory() as tmp_dir:
        os.mkdir(os.path.join(tmp_dir, project_template_name))
        result = find_template(tmp_dir)
        assert result == os.path.join(tmp_dir, project_template_name)

    with TemporaryDirectory() as tmp_dir:
        os.mkdir(os.path.join(tmp_dir, 'abc'))
        os.mkdir(os.path.join(tmp_dir, project_template_name))
        result = find_template(tmp_dir)

# Generated at 2022-06-13 18:34:08.517584
# Unit test for function find_template
def test_find_template():
    repo_dir = os.path.join(
        os.path.dirname(__file__),
        '..', '..', 'tests', 'fake-repo', 'input'
    )
    project_template = find_template(repo_dir)
    assert project_template == os.path.join(repo_dir, 'fake-cookiecutter-project')

# Generated at 2022-06-13 18:34:15.032579
# Unit test for function find_template
def test_find_template():
    """
    Test the find_template function.

    :returns: True or False.
    """
    import tempfile
    import shutil

    base_dir = tempfile.mkdtemp()
    repo_dir = os.path.join(base_dir, 'repo_dir')
    os.mkdir(repo_dir)

    templated_template_dir = os.path.join(repo_dir, '{{cookiecutter.project_name}}')
    os.mkdir(templated_template_dir)

    template = find_template(repo_dir)

    shutil.rmtree(base_dir)

    if template == templated_template_dir:
        return True
    else:
        return False

# Generated at 2022-06-13 18:34:23.227125
# Unit test for function find_template
def test_find_template():
    """Verify Cookiecutter discovers templates properly."""
    this_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(this_dir)

    expected_path = os.path.join(
        parent_dir,
        'scaffold',
        '_cookiecutter'
    )

    assert find_template(parent_dir) == expected_path

# Generated at 2022-06-13 18:34:26.111288
# Unit test for function find_template
def test_find_template():
    """Test the function find_template"""
    result = find_template("tests/test-output")
    assert result == "tests/test-output/cookiecutter-pypackage"


# Generated at 2022-06-13 18:34:34.437865
# Unit test for function find_template
def test_find_template():
    """Verify that the function find_template works correctly.
    """
    repo_dir = os.path.abspath("tests/fake-repo")
    project_template = find_template(repo_dir)
    
    assert project_template.endswith("tests/fake-repo/{{cookiecutter.project_slug}}")
    os.remove("tests/fake-repo/{{cookiecutter.project_slug}}/README.md")
    os.removedirs("tests/fake-repo/{{cookiecutter.project_slug}}")

# Generated at 2022-06-13 18:34:36.737878
# Unit test for function find_template
def test_find_template():
    assert find_template('tests/test-repos/hook-repo') == 'tests/test-repos/hook-repo/{{cookiecutter.repo_name}}'



# Generated at 2022-06-13 18:34:43.147472
# Unit test for function find_template
def test_find_template():
    template_dir = os.path.join(os.path.dirname(__file__),
                                'test-templates',
                                'find-the-cookiecutter-templated-directory')
    expected_template = os.path.join(template_dir, '{{cookiecutter.project_name}}')
    result_template = find_template(template_dir)
    assert result_template == expected_template
    return


# Generated at 2022-06-13 18:34:48.149683
# Unit test for function find_template
def test_find_template():
    from tests.test_utils import TEST_TEMPLATE_PATH
    assert find_template(TEST_TEMPLATE_PATH) == os.path.join(TEST_TEMPLATE_PATH, '{{cookiecutter.repo_name}}')

# Generated at 2022-06-13 18:34:50.019258
# Unit test for function find_template
def test_find_template():
    """Verify that a non-templated input directory raises an exception.

    This test passes when NonTemplatedInputDirException is raised by find_template,
    which is the intended behavior for that function.
    """
    repo_dir = os.path.join('tests', 'test-find-template')
    find_template(repo_dir)

# Generated at 2022-06-13 18:34:53.892125
# Unit test for function find_template
def test_find_template():
    repo_dir = "./tests/test-repo"
    expected_project_template = "./tests/test-repo/{{cookiecutter.repo_name}}"
    project_template = find_template(repo_dir)
    assert project_template == expected_project_template

# Generated at 2022-06-13 18:35:28.634910
# Unit test for function find_template
def test_find_template():
    import inspect
    from cookiecutter import utils
    path = inspect.getfile(utils)
    path = os.path.join(os.path.dirname(path), '..', 'tests')
    assert find_template(path) == '{{cookiecutter.repo_name}}'


# Generated at 2022-06-13 18:35:29.419601
# Unit test for function find_template
def test_find_template():
    pass

# Generated at 2022-06-13 18:35:29.967870
# Unit test for function find_template
def test_find_template():
    pass

# Generated at 2022-06-13 18:35:35.702585
# Unit test for function find_template
def test_find_template():
    """Test that the function finds the intended project template."""
    import tempfile

    repo_dir = tempfile.mkdtemp()
    # Make a dummy template
    dummy_dir = os.path.join(repo_dir, 'dummy')
    os.mkdir(dummy_dir)

    # Make a template with the correct name
    templated_dirpath = os.path.join(repo_dir, 'templated_dir')
    os.mkdir(templated_dirpath)

    project_template = find_template(repo_dir)

    assert project_template == templated_dirpath

# Generated at 2022-06-13 18:35:44.658315
# Unit test for function find_template
def test_find_template():
    """Test that find_template works when supplied with various directories.
    """
    import tempfile
    from cookiecutter.config import DEFAULT_CONFIG

    # setup temporary repo
    sample_repo = tempfile.mkdtemp()
    template_dir = tempfile.mkdtemp(dir=sample_repo)
    os.makedirs(os.path.join(template_dir, 'content'))
    template_dir = os.path.join(template_dir, 'content')
    DEFAULT_CONFIG.update({'replay_dir': template_dir})
    other_dir = tempfile.mkdtemp(dir=sample_repo)
    os.makedirs(os.path.join(other_dir, 'content'))
    other_dir = os.path.join(other_dir, 'content')



# Generated at 2022-06-13 18:35:51.739662
# Unit test for function find_template
def test_find_template():
    """Test find_template()."""
    # Setup
    repo_dir_contents = os.listdir('./tests/fake-repo-pre/')
    repo_dir = './tests/fake-repo-pre/'
    expected_project_template = './tests/fake-repo-pre/{{cookiecutter.repo_name}}'

    # Run
    project_template = find_template(repo_dir)

    # Test
    assert project_template == expected_project_template

# Generated at 2022-06-13 18:35:57.043327
# Unit test for function find_template
def test_find_template():
    """Find the project template using a mocked repo_dir."""
    test_repo_dir = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        'mock-repo'
    )
    assert find_template(test_repo_dir) == os.path.join(
        test_repo_dir,
        '{{cookiecutter.repo_name}}'
    )

# Generated at 2022-06-13 18:36:02.834287
# Unit test for function find_template
def test_find_template():
    """
    Basic unit test for function find_template.
    """
    this_dir, this_filename = os.path.split(__file__)
    test_dir = os.path.join(this_dir, 'test_find_template')
    found = find_template(test_dir)
    expected = os.path.join(test_dir, '{{cookiecutter.repo_name}}')
    assert found == expected

# Generated at 2022-06-13 18:36:05.852655
# Unit test for function find_template
def test_find_template():
    repo_dir = "./tests/test-find-template"
    print(find_template(repo_dir))

# Generated at 2022-06-13 18:36:18.048654
# Unit test for function find_template
def test_find_template():
    '''
    Unit tests for function find_template
    '''

    import unittest
    import os
    from shutil import rmtree
    from cookiecutter import main
    from cookiecutter import exceptions

    class TestFindTemplate(unittest.TestCase):

        def setUp(self):
            # Create a fake project to clone into
            if not os.path.isdir(self.project_dir):
                main.cookiecutter(self.project_dir)

# Generated at 2022-06-13 18:37:17.198421
# Unit test for function find_template
def test_find_template():
    pass

# Generated at 2022-06-13 18:37:26.893083
# Unit test for function find_template

# Generated at 2022-06-13 18:37:38.948886
# Unit test for function find_template
def test_find_template():
    """
    Test the find_template function.
    """
    from cookiecutter.tests.test_find import make_test_repo
    from cookiecutter.utils import rmtree

    test_repo_dir = make_test_repo()
    try:
        project_template = find_template(test_repo_dir)
    finally:
        rmtree(test_repo_dir)

    assert project_template == os.path.join(
        test_repo_dir, '{{cookiecutter.repo_name}}'
    )