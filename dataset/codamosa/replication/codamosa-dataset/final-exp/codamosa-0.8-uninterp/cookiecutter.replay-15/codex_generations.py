

# Generated at 2022-06-13 18:38:15.378528
# Unit test for function load
def test_load():
    replay_dir = 'tests/replay'
    template_name = 'tests/big-repo-name'
    context = load(replay_dir, template_name)
    assert type(context) == dict
    assert context['cookiecutter']['full_name'] == 'Audrey Roy Greenfeld'
    assert context['cookiecutter']['email'] == 'audreyr@example.com'



# Generated at 2022-06-13 18:38:22.852359
# Unit test for function load
def test_load():
    """Unit test for function load"""
    # Create a file to test
    test_file = 'test_file.json'
    test_context = {'cookiecutter': {'full_name': 'Test Name', 'email': 'test@test.com'}}

    # Write to file
    with open(test_file, 'w') as outfile:
        json.dump(test_context, outfile, indent=2)

    # Check that the function returns the written context
    assert load('', 'test_file') == test_context

    # Delete the test file
    os.remove(test_file)



# Generated at 2022-06-13 18:38:28.809256
# Unit test for function dump
def test_dump():
    replay_dir = 'tests/files/fake-repo-tmpl/'
    template_name = 'fake-repo-tmpl'
    context = {
        "cookiecutter": {
            "foo": "baz",
            "bar": "baz"
        }
    }
    dump(replay_dir, template_name, context)
    assert(os.path.exists('tests/files/fake-repo-tmpl/fake-repo-tmpl.json'))
    context_test = load(replay_dir, template_name)
    assert(context == context_test)

# Generated at 2022-06-13 18:38:35.841728
# Unit test for function load
def test_load():
    """Test the load function."""
    # Test proper context loading
    context = load('/usr/local/cookiecutter_tests/replay', 'cookiecutter-pypackage')
    assert context['cookiecutter']['project_name'] == 'cookiecutter-pypackage'

    # Test proper error raising when no cookiecutter key
    try:
        load('/usr/local/cookiecutter_tests/replay', 'cookiecutter-pypackage')
    except ValueError as e:
        assert str(e) == 'Context is required to contain a cookiecutter key'

    # Test proper error raising when template_name is not string

# Generated at 2022-06-13 18:38:41.281639
# Unit test for function load
def test_load():
    import json
    import os
    from cookiecutter.replay import load
    replay_dir = os.path.join("testdata")
    template_name = "test"
    context = load(replay_dir, template_name)
    with open("testdata/test.json", "r") as infile:
        context2 = json.load(infile)
    assert context == context2

# Generated at 2022-06-13 18:38:46.535568
# Unit test for function dump
def test_dump():
    replay_dir = 'C:\\Users\\User1\\cookiecutter-example\\.cookiecutter-replay'
    template_name = 'cookiecutter-example\\{{cookiecutter.project_name}}'
    context = {'cookiecutter': {'project_name': 'pyBAR'}}
    dump(replay_dir, template_name, context)
    return


# Generated at 2022-06-13 18:38:50.277123
# Unit test for function dump
def test_dump():
    """Test for function dump."""
    import tempfile
    replay_dir = tempfile.mkdtemp()
    test_filename = 'test_template'
    test_context = {'cookiecutter': {'lava_test_keys': 'lava_test_values'}}
    dump(replay_dir, test_filename, test_context)


# Generated at 2022-06-13 18:38:55.839624
# Unit test for function get_file_name
def test_get_file_name():
    # Test: adds file suffix
    assert get_file_name('test', 'mytest') == 'test/mytest.json'
    # Test: does not add file suffix
    assert get_file_name('test', 'mytest.json') == 'test/mytest.json'


# Generated at 2022-06-13 18:39:06.632035
# Unit test for function dump
def test_dump():
    """Test the dump funtion."""

# Generated at 2022-06-13 18:39:11.769446
# Unit test for function dump
def test_dump():
    """
    test_dump function
    """
    replay_dir = '.'
    template_name = 'test'
    context = {'cookiecutter': {'test': 'test'}}

    dump(replay_dir, template_name, context)
    context_read = load(replay_dir, template_name)

    if os.path.exists(template_name + '.json'):
        os.remove(template_name + '.json')

    assert context_read == context, 'Dump and load function failed'


# Generated at 2022-06-13 18:39:20.225408
# Unit test for function load
def test_load():
    """Unit test for function load."""
    context = load('replay_tests/replay', 'tests')
    assert context['cookiecutter']['project_slug'] == 'tests'
    assert context['cookiecutter']['full_name'] == 'Your name'
    assert context['cookiecutter']['email'] == 'Your email'
    assert context['cookiecutter']['description'] == 'A short description of the project.'
    assert context['cookiecutter']['version'] == '0.1.0'

# Generated at 2022-06-13 18:39:23.392213
# Unit test for function load
def test_load():
    replay_dir = '~/.cookiecutters'
    template_name = 'cookiecutter-pypackage'
    context = load(replay_dir, template_name)
    assert 'cookiecutter' in context

# Generated at 2022-06-13 18:39:26.472417
# Unit test for function load
def test_load():
    replay_dir = 'tests/fake-repo-pre/'
    template_name = 'fake-repo-pre'
    context = load(replay_dir, template_name)
    assert context
    assert 'cookiecutter' in context

# Generated at 2022-06-13 18:39:33.176983
# Unit test for function load
def test_load():
    d = (os.path.dirname(os.path.realpath(__file__)))
    os.chdir(d)
    context = load('Test-replay', 'Test-template')

# Generated at 2022-06-13 18:39:40.688791
# Unit test for function dump
def test_dump():
    """Unit test for function dump."""
    test_context = {
        'cookiecutter': {
            'project_slug': 'test-project',
            'author_name': 'test author',
            'open_source_license': 'MIT',
            'pypi_username': 'test-user',
            'repo_name': 'test-repo',
            'description': 'Test project',
            'domain_name': 'example.com'
        }
    }
    replay_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'test', 'replay'
    )
    template_name = 'foo'
    dump(replay_dir, template_name, test_context)

# Generated at 2022-06-13 18:39:43.668257
# Unit test for function load
def test_load():
    load('/Users/user/.cookiecutters/', 'newprojectmock')



# Generated at 2022-06-13 18:39:49.138569
# Unit test for function load
def test_load():
    context = load('tests/test-repo', 'project_slug')
    assert isinstance(context, dict)
    assert 'cookiecutter' in context
    assert context['part_number'] == 'P09382780C'


# Generated at 2022-06-13 18:39:56.203426
# Unit test for function load
def test_load():
    replay_dir = '/tmp/cookiecutter-test'
    cookiecutter_context = {
        'cookiecutter': {
            'full_name': 'Tester',
            'email': 'test@test.com'
        }
    }
    template_name = 'testing-cookiecutter'

    dump(replay_dir, template_name, cookiecutter_context)
    loaded_context = load(replay_dir, template_name)

    assert loaded_context == cookiecutter_context

# Generated at 2022-06-13 18:39:58.886295
# Unit test for function load
def test_load():
    """TODO: Docstring for test_load.
    :returns: TODO

    """
    context = load('replay/', 'tests/fake-repo-pre/')
    assert context['cookiecutter']['full_name'] == 'Audrey Roy Greenfeld'
    return



# Generated at 2022-06-13 18:40:06.076190
# Unit test for function dump
def test_dump():
    replay_dir = '.'
    template_name = 'cookiecutter-pypackage'
    context = {
        'full_name': 'Test',
        'email': 'test@example.com',
        'project_name': 'testing_project_name'
    }
    dump(replay_dir, template_name, context)

    replay_file = 'cookiecutter-pypackage.json'
    assert os.path.exists(replay_file) == True
    os.remove(replay_file)


# Generated at 2022-06-13 18:40:18.153142
# Unit test for function load
def test_load():
    """Unit test for function load"""
    # Normal case
    try:
        expected = {'cookiecutter': {'replay': 'y'}}
        actual = load('test_replay_dir', 'test_replay_file')
        assert expected == actual
    except Exception as exc:
        assert "TypeError" in str(exc)

    # Type error
    try:
        load('test_replay_dir', 123)
    except Exception as exc:
        assert "TypeError" in str(exc)

    # Value error
    expected = {'cookiecutter': {'replay': 'y'}}
    actual = load('test_replay_dir', 'test_replay_file_normal')

# Generated at 2022-06-13 18:40:23.247329
# Unit test for function load
def test_load():
    """Unit test for function load."""
    try:
        load(replay_dir="./tests/replay", template_name="test")
    except TypeError as exception:
        assert "Template name is required to be of type str" in str(exception)
    except ValueError as exception:
        assert "Context is required to contain a cookiecutter key" in str(exception)
    except IOError as exception:
        assert "Unable to create replay dir at" in str(exception)


# Generated at 2022-06-13 18:40:33.445628
# Unit test for function dump
def test_dump():
    replay_dir = os.path.join('/tmp', 'cookiecutter_replay')
    template_name = 'Blog template'
    context = {
        'cookiecutter': {
            'title': 'My blog title',
            'author': 'Me',
            'type': 'post'
        }
    }

    dump(replay_dir, template_name, context)

    assert os.path.isfile(get_file_name(replay_dir, template_name))
    assert context == load(replay_dir, template_name)

    os.remove(get_file_name(replay_dir, template_name))
    os.rmdir(replay_dir)

# Generated at 2022-06-13 18:40:39.391854
# Unit test for function dump
def test_dump():
    from . import ROOT_DIR
    replay_dir = os.path.join(ROOT_DIR, 'replay')
    template_name = 'python'
    context = {'cookiecutter':{'_copy_without_render':['docs', 'tests', 'macros.html']}}
    dump(replay_dir, template_name, context)


# Generated at 2022-06-13 18:40:48.138980
# Unit test for function load
def test_load():
    """Test for function load."""
    replay_dir = 'examples/tests/test-load/replay'
    template_name = 'test-load'

    context = load(replay_dir, template_name)

    assert isinstance(context, dict)
    assert 'cookiecutter' in context
    assert context['cookiecutter']['full_name'] == 'Audrey Roy'
    assert context['cookiecutter']['email'] == 'audreyr@example.com'
    assert context['cookiecutter']['project_name'] == 'test-load'
    assert context['cookiecutter']['repo_name'] == 'test-load'
    assert context['cookiecutter']['project_slug'] == 'test_load'
    assert context['cookiecutter']['project_short_description']

# Generated at 2022-06-13 18:40:51.953758
# Unit test for function load
def test_load():
	import os
	print(os.path.abspath('.'))
	replay_dir = './test/replay'
	template_name = 'test'
	context = load(replay_dir, template_name)
	print(context)



# Generated at 2022-06-13 18:40:53.462159
# Unit test for function load

# Generated at 2022-06-13 18:40:56.028993
# Unit test for function load
def test_load():
    try:
        load("C:\\Users\\yfeng\\Downloads\\cookiecutter-master\\cookiecutter-master\\tests\\test-replay", "test-template")
    except ValueError:
        print("ERROR: Found the unexpected value in context.")

# Generated at 2022-06-13 18:40:59.587929
# Unit test for function load
def test_load():
    """Test method load."""
    context = load('./tests', 'tests/basic-py')
    assert 'cookiecutter' in context

# Generated at 2022-06-13 18:41:03.331213
# Unit test for function load
def test_load():
    """Test function load."""
    replay_dir = os.path.join(
        os.path.expanduser('~'), '.cookiecutters', 'replay')
    template_name = 'cookiecutter-pypackage'
    data = load(replay_dir, template_name)
    assert isinstance(data, dict)

# Generated at 2022-06-13 18:41:12.419918
# Unit test for function load
def test_load():
    dir1 = "/Users/felipe/Desktop/cookiecutter-master/cookiecutter/replay"
    template_name = "{{cookiecutter.project_slug}}.json"
    context = {"cookiecutter": "https://github.com/audreyr/cookiecutter-pypackage.git"}
    replay_file = get_file_name(dir1, template_name)
    print(replay_file)
    with open(replay_file, 'r') as infile:
        context = json.load(infile)

    if 'cookiecutter' not in context:
        raise ValueError('Context is required to contain a cookiecutter key')

    return context


if __name__ == '__main__':
    test_load()

# Generated at 2022-06-13 18:41:14.924231
# Unit test for function load
def test_load():
    global replay_dir
    global template_name
    replay_file = get_file_name(replay_dir, template_name)
    
    with open(replay_file, 'r') as infile:
        context = json.load(infile)
    print(context)
    return context


# Generated at 2022-06-13 18:41:19.579780
# Unit test for function load
def test_load():
    with open("test.json", 'w') as outfile:
        json.dump(context, outfile, indent=2)
    context = load("test.json","test.json")
    context = json.load("test.json")
    assert isinstance(context,dict)
    context = load("test.json","test1.json")


# Generated at 2022-06-13 18:41:29.449377
# Unit test for function load
def test_load():
    import os
    import shutil
    template_name = "test"
    # Generate a replay file
    replay_dir = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '..',
            '..',
            'test',
            'loadfile'
        )
    )
    context = {}
    context['cookiecutter'] = {}
    context['cookiecutter']['full_name'] = 'Max Mustermann'
    context['cookiecutter']['email'] = 'm.mustermann@example.com'
    context['cookiecutter']['github_username'] = 'mmustermann'
    context['cookiecutter']['project_name'] = 'pip-check-reqs'

# Generated at 2022-06-13 18:41:38.200444
# Unit test for function dump
def test_dump():
    tempdir = os.path.dirname(__file__)  # directory of this file
    input_dir = os.path.join(tempdir, 'templates', 'simple')  # templates file
    replay_dir = os.path.join(tempdir)
    template_name = 'simple'
    context = {
        'cookiecutter': {
            'full_name': 'r1.r1',
            'email': 'r1@r1.com',
            'project_name': 'test-project-r1-r1'
        }
    }
    try:
        dump(replay_dir, template_name, context)
    except Exception as e:
        assert False, "dump() failed due to the following exception: {}".format(e)

# Generated at 2022-06-13 18:41:42.173603
# Unit test for function load
def test_load():
    template_name = 'arjunneupane/jinja2-ubuntu-18.04'
    replay_dir = '~/.cookiecutter-replay/'
    load(replay_dir, template_name)


# Generated at 2022-06-13 18:41:49.546389
# Unit test for function load
def test_load():
    """Test if load is working correctly."""
    import os
    import shutil
    import tempfile
    import json
    base_path = 'files/tests/test-replay/'
    context = {
        'cookiecutter': {
            'full_name': 'Ines Montani',
            'email': 'ines@ines.io',
            'github_username': 'ines',
            'project_name': 'cookiecutter-pypackage',
        }
    }
    # store information in a temp directory
    temp_dir = tempfile.mkdtemp()
    dump(temp_dir, 'cookiecutter-pypackage', context)
    # load the information back
    extracted_context = load(temp_dir, 'cookiecutter-pypackage')


# Generated at 2022-06-13 18:41:50.983350
# Unit test for function load
def test_load():
    assert load('/home/path', 'test') == {'cookiecutter': {}}

# Generated at 2022-06-13 18:41:58.306443
# Unit test for function load
def test_load():
    assert load('C:\\Users\\Zoe\\Dropbox\\GitHub\\cookiecutter\\tests\\test-replay\\.', 'test-replay') == {
    'cookiecutter': {
        'author_name': 'Audrey Roy Greenfeld',
        'author_email': 'audreyr@example.com',
        'project_name': 'cookiecutter-pypackage',
        'release_date': '2014/10/01',
        'project_version': '0.1.0',
        'project_short_description': 'A Python package project template.',
        'use_travis': True,
        'use_pytest': False,
        'use_pypi_deployment_with_travis': True
    }
}


# Generated at 2022-06-13 18:42:08.057889
# Unit test for function load
def test_load():
    input_json = {
        "cookiecutter": {
            "full_name": "Audrey Roy",
            "email": "audreyr@example.com",
            "project_name": "cookiecutter-pypackage-minimal",
            "package_name": "minimal",
            "repo_name": "minimal",
            "description": "A minimal Cookiecutter template for a Python package.",
            "release_year": "2017",
            "year": "2017"
        }
    }
    replay_dir = '.'
    template_name = 'cookiecutter-pypackage-minimal'
    dump(replay_dir, template_name, input_json)
    output_json = load(replay_dir, template_name)

# Generated at 2022-06-13 18:42:19.218561
# Unit test for function dump
def test_dump():
    import os
    from cookiecutter.main import cookiecutter
    template = os.path.join(os.path.dirname(__file__), "..", "tests", "fake-repo-tmpl")
    output = cookiecutter(template)
    dump(output["cookiecutter"]["replay_dir"],output["cookiecutter"]["template_name"], output)


# Generated at 2022-06-13 18:42:21.586062
# Unit test for function load
def test_load():
    context = load(os.path.dirname(__file__), 'replay')
    assert isinstance(context, dict)


# Generated at 2022-06-13 18:42:30.369595
# Unit test for function dump
def test_dump():
    """Test the dump function."""
    replay_dir = 'test_replay_dir'
    template_name = 'test_template_name'
    context = {'foo': 'bar', 'baz': 'buz'}
    dump(replay_dir, template_name, context)

    # Get file name
    suffix = '.json' if not template_name.endswith('.json') else ''
    file_name = '{}{}'.format(template_name, suffix)
    file_path = os.path.join(replay_dir, file_name)

    try:
        # Load data from file
        with open(file_path, 'r') as infile:
            data = json.load(infile)

        # Compare data
        assert data == context

    finally:
        # Delete file
        os

# Generated at 2022-06-13 18:42:34.944274
# Unit test for function dump
def test_dump():
    print('Testing dump function')
    import tempfile
    template_name = 'template'
    replay_dir = tempfile.mkdtemp()
    context = {'cookiecutter': {'year': '2019', 'name': 'template'}}
    dump(replay_dir, template_name, context)
    with open(get_file_name(replay_dir, template_name), 'r') as infile:
        assert json.load(infile) == context


# Generated at 2022-06-13 18:42:39.133266
# Unit test for function dump
def test_dump():
    try:
        replay_dir = 'cookiecutter.replay'
        template_name = 'template_name'
        context = {'cookiecutter': 'context1', 'cookiecutter2': 'context2'}
        dump(replay_dir, template_name, context)
    except:
        print("dump error")
    else:
        print("dump success")


# Generated at 2022-06-13 18:42:41.633925
# Unit test for function load
def test_load():
    assert load("/home/mrcode/cookiecutter-django-app/tests/replay_dir", "mrcode/cookiecutter-django-app/master")

# Generated at 2022-06-13 18:42:52.121098
# Unit test for function dump
def test_dump():
    assert get_file_name('replay_dir', 'template_name') == 'replay_dir\\template_name.json'
    assert make_sure_path_exists('replay_dir') == True
    # assert dump('replay_dir', 'template_name', {}) == None
    assert dump('', 'template_name', {}) == None
    assert dump('replay_dir', '', {}) == None
    assert dump('replay_dir', 'template_name', {'cookiecutter': 'test'}) == None
    assert dump('replay_dir', 'template_name', {'not_cookiecutter': 'test'}) == None


# Generated at 2022-06-13 18:42:57.204793
# Unit test for function dump
def test_dump():
    config_dict=dict(config_dict={
        'cookiecutter': {
            'name': 'Leap',
            'email': 'leap@leap.se',
            'username': 'leap'
        }
    })

    template_name = 'template'

    dump('replays/', template_name, config_dict)

    loaded_dict = load('replays/', template_name)
    assert loaded_dict == config_dict

# Generated at 2022-06-13 18:43:06.063423
# Unit test for function load
def test_load():
    """Test function load."""
    import json
    import tempfile

    template_name = 'test_template'
    context = {'cookiecutter': {'test_key': 'test_value'}}
    replay_dir = tempfile.mkdtemp()

    try:
        dump(replay_dir=replay_dir, template_name=template_name, context=context)
        loaded_context = load(replay_dir=replay_dir, template_name=template_name)
    finally:
        os.rmdir(replay_dir)

    assert context == loaded_context

# Generated at 2022-06-13 18:43:09.152861
# Unit test for function load
def test_load():
    try:
        context = load("D:\Code\GitHub\cookiecutter\cookiecutter\tests\test-replay", "test-template")
    except ValueError:
        raise RuntimeError
    if "cookiecutter" not in context:
        raise RuntimeError


# Generated at 2022-06-13 18:43:19.190047
# Unit test for function load
def test_load():
    replay_dir = '/home/luan/Workspace/cookiecutter-pptex'
    template_name = 'manuscript'
    context = load(replay_dir, template_name)
    print(context)
    print(context['cookiecutter']['author_name'])
    print(context['cookiecutter']['manuscript_title'])

# Generated at 2022-06-13 18:43:25.577693
# Unit test for function load
def test_load():
    tname = 'a'
    rdir = './test/'
    tname2 = 'b'
    rdir2 = './test/test/'

    try:
        os.makedirs(rdir)
    except OSError:
        if not os.path.isdir(rdir):
            raise
    
    try:
        os.makedirs(rdir2)
    except OSError:
        if not os.path.isdir(rdir2):
            raise
    

# Generated at 2022-06-13 18:43:29.740965
# Unit test for function dump
def test_dump():
    """Unit test for function dump."""
    # Arrange
    replay_dir = 'test_dir'
    template_name = 'test_template'
    context = 'test_context'
    # Act
    status = dump(replay_dir, template_name, context)
    # Assert
    # Dump returns nothing
    assert status is None


# Generated at 2022-06-13 18:43:35.481796
# Unit test for function load
def test_load():
    data = load("/Users/yefeichen/Database/from_yefeichen/Cookiecutter-Examples/cookiecutter-pypackage-minimal/", "{{cookiecutter.project_name}}.json")
    print(data)
    print("test_load OK!")



# Generated at 2022-06-13 18:43:41.229898
# Unit test for function dump
def test_dump():
	replay_dir = "testreplay"
	template_name = "test_name"
	context = {}

	context['cookiecutter'] = "test"
	context['test2'] = {}
	context['test3'] = 1
	dump(replay_dir,template_name,context)
	assert 1 == 1


# Generated at 2022-06-13 18:43:47.836960
# Unit test for function dump
def test_dump():

    from cookiecutter.config import get_user_config
    from cookiecutter.replay import dump
    from cookiecutter.utils import rmtree

    user_config = get_user_config()

    base_context = {
        'cookiecutter': {
            'full_name': 'Audrey Roy',
            'email': 'audreyr@example.com',
            'github_username': 'audreyr'
        }
    }

    user_config['replay_dir'] = '/tmp/test-cookies'
    rmtree(user_config['replay_dir'])

    dump(
        replay_dir=user_config['replay_dir'],
        template_name='cookiecutter-pypackage',
        context=base_context
    )


# Generated at 2022-06-13 18:43:57.217315
# Unit test for function load
def test_load():
    template_name = 'cookiecutter-pypackage'

# Generated at 2022-06-13 18:44:00.153785
# Unit test for function load
def test_load():
    file_name = os.path.join(os.curdir, 'tests', 'test_load.json')
    with open(file_name, 'r', encoding='UTF-8') as infile:
        expected = json.load(infile)
    context = load(os.curdir, 'test_load')
    assert context == expected


# Generated at 2022-06-13 18:44:03.359226
# Unit test for function load
def test_load():
    context = load(os.getcwd(), 'cookiecutter-pypackage')
    assert isinstance(context, dict)
    assert 'cookiecutter' in context
    assert 'full_name' in context['cookiecutter']


# Generated at 2022-06-13 18:44:12.029297
# Unit test for function load
def test_load():
    """Test for function load."""
    import json
    import os
    from cookiecutter.utils import make_sure_path_exists
    from cookiecutter import config

    replay_dir = os.path.join(
        config.USER_HOME, '.cookiecutters', 'cookiecutter-pypackage'
    )
    make_sure_path_exists(replay_dir)
    template_name = 'cookiecutter-pypackage'

# Generated at 2022-06-13 18:44:23.195828
# Unit test for function load
def test_load():
    template_name = './tests/test-template'
    context = "./tests/replay"

    a = load(context, template_name)

    # Prints the contents of json file
    print(a)


# Generated at 2022-06-13 18:44:31.417082
# Unit test for function dump
def test_dump():
    file_dir = os.path.dirname(os.path.realpath('__file__'))
    replay_dir = os.path.join(file_dir, 'tests/test-dump-replay/')
    template_name = 'test-template'
    context = {'cookiecutter': {'key': 'value'}}
    try:
        dump(replay_dir, template_name, context)
        written = load(replay_dir, template_name)
        assert written == context
    except Exception as e:
        raise e
    finally:
        os.remove(os.path.join(replay_dir, 'test-template.json'))
        os.rmdir(replay_dir)


# Generated at 2022-06-13 18:44:33.502970
# Unit test for function load
def test_load():
    try:
        load("replay", "cookiecutter.json")
    except:
        False


# Generated at 2022-06-13 18:44:42.324466
# Unit test for function dump
def test_dump():
    replay_dir = "test_dir/"
    template_name = "template_name"
    context = {
        "cookiecutter": {
            "project_name": "project_name",
            "hello": "hello"
        }
    }

    dump(replay_dir, template_name, context)
    assert os.path.exists("{}{}.json".format(replay_dir, template_name))

    with open("{}{}.json".format(replay_dir, template_name), "r") as f:
        lines = f.readlines()
        assert lines[0] == "{\n"
        assert lines[1] == '    "cookiecutter": {\n'
        assert lines[2] == '        "project_name": "project_name",\n'

# Generated at 2022-06-13 18:44:44.659561
# Unit test for function load
def test_load():
    # load(replay_dir, template_name)
    assert load(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, "cookiecutter_examples/replay")), "Nikkolaus")

# Generated at 2022-06-13 18:44:49.077659
# Unit test for function load
def test_load():
    import tempfile

    temp_dir = tempfile.mkdtemp()
    replay_file = os.path.join(temp_dir, 'replay.json')
    test_context = {
        'cookiecutter': {
            'full_name': 'Test',
            'email': 'test@test.com',
            'github_username': 'test_user'
        }
    }

    with open(replay_file, 'w') as outfile:
        json.dump(test_context, outfile, indent=2)

    context = load(temp_dir, 'replay')
    assert context == test_context

# Generated at 2022-06-13 18:44:56.500805
# Unit test for function dump
def test_dump():
    template_name = '{{cookiecutter.github_repo_name}}'
    context = {}
    context['cookiecutter'] = {}
    context['cookiecutter']['github_repo_name'] = '{{cookiecutter.github_repo_name}}'

    dump('./', template_name, context)
    return True


# Generated at 2022-06-13 18:45:04.504695
# Unit test for function dump
def test_dump():
    replay_dir = 'C:\\Users\\NguyenT\\PycharmProjects\\cookiecutter\\tests\\test-replay'
    template_name = 'template'
    context = {'cookiecutter': {'name': 'name', 'password': 'pass'}, 'first': 'first'}
    dump(replay_dir, template_name, context)


if __name__ == '__main__':
    # Unit test
    #test_dump()
    pass

# Generated at 2022-06-13 18:45:12.470400
# Unit test for function load
def test_load():
    replay_dir = os.path.expanduser("~/.cookiecutters")
    template_name = 'hello-world-python-cli'
    context = load(replay_dir, template_name)
    assert context["cookiecutter"]["project_name"] == "hello-world-python-cli"
    assert context["cookiecutter"]["project_slug"] == "hello_world_python_cli"
    assert context["cookiecutter"]["project_short_description"] == "A CLI that prints \"Hello world!\" in your console. Showcases argparse and logging."
    assert context["cookiecutter"]["open_source_license"] == "MIT license"


# Generated at 2022-06-13 18:45:14.840651
# Unit test for function load
def test_load():
    context = load('/Users/paul/Documents/github//cookiecutter/tests/test-replay', './cookiecutter.json')
    print(context['cookiecutter']['cookiecutter_dict'])

if __name__ == '__main__':
	test_load()

# Generated at 2022-06-13 18:45:48.454891
# Unit test for function load
def test_load():
    """Return context from file."""
    from cookiecutter.main import cookiecutter

    replay_dir = '.cookiecutters'
    template_name = 'https://github.com/j0nathanj/cookiecutter-website'
    replay_file = get_file_name(replay_dir, template_name)
    context = load(replay_dir, template_name)
    assert 'cookiecutter' in context


if __name__ == "__main__":

    test_load()

# Generated at 2022-06-13 18:45:57.017931
# Unit test for function load
def test_load():
    """Test load function."""
    try:
        context = load('.', 'test')
    except Exception:
        context = None
    assert context['cookiecutter']['rabbitmq_server'] == 'rabbitmq'
    assert context['cookiecutter']['keystone_server'] ==  'keystone'
    assert context['cookiecutter']['glance_server'] == 'glance'
    assert context['cookiecutter']['nova_server'] == 'nova'
    assert context['cookiecutter']['neutron_server'] == 'neutron'
    assert context['cookiecutter']['heat_server'] == 'heat'
    assert context['cookiecutter']['cinder_server'] == 'cinder'

# Generated at 2022-06-13 18:45:59.569605
# Unit test for function load
def test_load():
    replay_dir = "/Users/qiushi/github/pycookiecutter/replay"
    template_name = "python"
    print(load(replay_dir,template_name))


# Generated at 2022-06-13 18:46:07.031120
# Unit test for function load
def test_load():
    # Test case 1: replay_dir doesn't exist
    try:
        load(replay_dir='a/b/c', template_name='test')
    except Exception:
        assert True
    else:
        assert False

    # Test case 2: template_name is not a string
    try:
        load(replay_dir='', template_name=123)
    except TypeError:
        assert True
    else:
        assert False

    # Test case 3: context doesn't contain cookiecutter key
    try:
        load(replay_dir='', template_name='')
    except ValueError:
        assert True
    else:
        assert False

    # Test case 4: no exception is raised
    try:
        load(replay_dir='', template_name='test')
    except Exception:
        assert False

# Generated at 2022-06-13 18:46:11.963023
# Unit test for function dump
def test_dump():
    """Unit test for function dump"""
    replay_dir = 'test_replay'
    make_sure_path_exists(replay_dir)
    template_name = 'test_template'
    context = {
        'cookiecutter': {
            'full_name': 'John Smith',
            'email': 'john@example.com',
        }
    }
    try:
        dump(replay_dir, template_name, context)
    except Exception as e:
        print("Error: exception {}".format(e))
    else:
        print("Succeeded.")


# Generated at 2022-06-13 18:46:14.613148
# Unit test for function dump
def test_dump():
    """Unit test for function dump."""
    context = {'cookiecutter': {'template_name': 'hello'}}
    dump('replay_test', 'hello', context)



# Generated at 2022-06-13 18:46:16.684609
# Unit test for function load
def test_load():
    context = load("/Users/peng.xue/Downloads/cookiecutter-pypackage-minimal-master", "audit.json")
    print(context)



# Generated at 2022-06-13 18:46:21.648403
# Unit test for function load
def test_load():
    test_name = 'test.json'
    replay_dir = 'replay_test/'
    test_context = {'cookiecutter': 'test'}

    dump(replay_dir, test_name, test_context)
    result_context = load(replay_dir, test_name)
    assert test_context == result_context
    os.remove('{}{}'.format(replay_dir, test_name))
    os.rmdir(replay_dir)



# Generated at 2022-06-13 18:46:27.900150
# Unit test for function load
def test_load():
    replay_dir = "replay"
    template_name = "{{ cookiecutter.project_name }}"
    context = {"a": 1}
    dump(replay_dir, template_name, context)
    assert load(replay_dir, template_name) == context
    os.remove(get_file_name(replay_dir, template_name))


# Generated at 2022-06-13 18:46:32.780281
# Unit test for function load
def test_load():
    """Unit test for function load."""
    assert(load('tests/test-output/replay', 'test-replay') == {'cookiecutter': {'cookiecutter': {'test_variable': 'default'}, 'replay': True}})


# Generated at 2022-06-13 18:47:06.128291
# Unit test for function load
def test_load():
    """Unit test for load"""
    # TODO: Add mock data to test this function
    pass

# Generated at 2022-06-13 18:47:11.038585
# Unit test for function load
def test_load():
    replay_dir = os.path.join('..', '..', 'tests', 'test-replay')
    template_name = 'test-template'
    context = load(replay_dir, template_name)
    assert context['cookiecutter']['full_name'] == 'James Bond'


# Generated at 2022-06-13 18:47:12.964396
# Unit test for function load
def test_load():
    print(load(replay_dir, template_name))



# Generated at 2022-06-13 18:47:19.823576
# Unit test for function load
def test_load():
    replay_dir = './tests/fixtures'
    template_name = 'pip-cookiecutter'

    context = load(replay_dir, template_name)

    assert isinstance(context, dict)
    assert 'cookiecutter' in context
    assert context['cookiecutter']['full_name'] == 'Audrey Roy'

# Generated at 2022-06-13 18:47:26.654551
# Unit test for function load
def test_load():
    import os
    import shutil
    from cookiecutter import replay

    current_directory = os.getcwd()
    test_directory = os.path.join(current_directory, 'test_load')
    template_name = 'test_load'
    replay_dir = os.path.join(test_directory, '{{cookiecutter.replay_dir}}')
    replay_file = replay.get_file_name(replay_dir, template_name)
    os.makedirs(replay_dir, exist_ok=True)
    # Create replay file with json data
    test_data = {'cookiecutter': {'test_key': 'test_value'}}
    with open(replay_file, 'w') as outfile:
        json.dump(test_data, outfile, indent=2)
   

# Generated at 2022-06-13 18:47:32.241714
# Unit test for function load
def test_load():
    template_name = 'template'
    replay_dir = 'replay_dir'
    with open('tests/fixtures/test.json', 'r') as infile:
        context = json.load(infile)

    assert load(replay_dir, template_name) == context, \
        "Context should be exactly the same"

if __name__ == "__main__":
    test_load()

# Generated at 2022-06-13 18:47:39.178020
# Unit test for function load
def test_load():
    """Unit test for function load.
    """

    template_name = "python_package"
    replay_dir = os.path.join(os.path.dirname(__file__), "test_replay_dir")
    data = load(replay_dir, template_name)

    assert isinstance(data, dict)
    assert data["cookiecutter"] != {}
    assert data["cookiecutter"]["full_name"] == "Yuhuang Hu"
    assert data["cookiecutter"]["email"] == "duguyue100@gmail.com"
    assert data["cookiecutter"]["project_name"] == "my-python-project"
    assert data["cookiecutter"]["repo_name"] == "my_python_project"

# Generated at 2022-06-13 18:47:41.024963
# Unit test for function load
def test_load():
    assert load('/home/hongxiwang/Desktop/project1', 'cookiecutter') != None


# Generated at 2022-06-13 18:47:42.261263
# Unit test for function load
def test_load():
    pass


# Generated at 2022-06-13 18:47:48.418909
# Unit test for function load
def test_load():
	import os, tempfile
	from cookiecutter.utils import rmtree

	# Set up a temporary temporary working dir
	tmp_dir = tempfile.mkdtemp()

	# Create a simple config file at tmp_dir/cookiecutter.json
	config = {"cookiecutter": {"project_name": "Example", "repo_name": "example", "email": "example@example.com", "timezone": "Europe/Paris"}}
	config_file = os.path.join(tmp_dir, 'cookiecutter.json')

	with open(config_file, 'w') as f:
		json.dump(config, f)

	# Call the 'load' function
	config_loaded = load(tmp_dir, 'cookiecutter')

	# Check returned config matches the one we set up
	assert config == config_