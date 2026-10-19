

# Generated at 2022-06-13 18:38:13.779051
# Unit test for function load
def test_load():
    assert load("/Users/xujie/.cookiecutters", "pypackage")

# Generated at 2022-06-13 18:38:22.081380
# Unit test for function load
def test_load():
    replay_file_content = {
        "cookiecutter": {
            "project_slug": "my-project-slug",
            "project_name": "My Project",
            "project_verbose_name": "My Project"
        }
    }
    test_template_name = 'test_template'
    test_replay_dir = '.test_replay_dir'
    test_replay_file = os.path.join(test_replay_dir, test_template_name + '.json')
    with open(test_replay_file, 'w') as outfile:
        json.dump(replay_file_content, outfile, indent=2)
    context = load(test_replay_dir, test_template_name)
    assert replay_file_content == context


# Generated at 2022-06-13 18:38:31.293762
# Unit test for function load
def test_load():

    # Create a replay directory 
    import tempfile
    temp_dir = tempfile.mkdtemp()

    # Store a context
    context = {
        'cookiecutter': {
            'full_name': 'Audrey Roy Greenfeld',
            'email': 'aroy@example.com',
            'github_username': 'audreyr',
            'version': '0.1.2',
            'project_name': 'Cookiecutter-Pylibrary',
            'project_slug': 'cookiecutter-pylibrary',
            'repo_name': 'cookiecutter-pylibrary',
            'release_date': '2014-08-14',
            'year': '2014'
        }
    }
    template_name = "fake_template"

# Generated at 2022-06-13 18:38:33.151434
# Unit test for function load
def test_load():
    context = load(replay_dir = 'replay_dir', template_name = 'template_name')
    assert 'cookiecutter' in context


# Generated at 2022-06-13 18:38:40.005612
# Unit test for function load
def test_load():
    temp_dir = os.path.dirname(os.path.abspath(__file__))
    temp_dir = os.path.join(temp_dir, 'test_tmp')
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    temp_file = os.path.join(temp_dir, 'cookiecutter.json')
    f = open(temp_file, 'w')
    f.write(
        '{\n'
        '    "cookiecutter": {\n'
        '        "full_name": "Test",\n'
        '        "email": "Test"\n'
        '    }\n'
        '}\n'
    )
    f.close()
    context = load(temp_dir, 'cookiecutter')


# Generated at 2022-06-13 18:38:40.766753
# Unit test for function load
def test_load():
    assert isinstance(load('/tmp', 'template_name'), dict)


# Generated at 2022-06-13 18:38:49.749775
# Unit test for function load

# Generated at 2022-06-13 18:38:52.066033
# Unit test for function load
def test_load():
    """Test for function load."""
    result = load('test', 'test')
    assert 'cookiecutter' in result

# Generated at 2022-06-13 18:39:04.221057
# Unit test for function load
def test_load():
    if not make_sure_path_exists('/home/shivang/.cc_replay/'):
        raise IOError('Unable to create replay dir at {}'.format('/home/shivang/.cc_replay/'))
    context = {'cookiecutter': {'full_name': 'Shivang Arora', 'email': 'arorashivang@gmail.com'}}
    replay_file = get_file_name('/home/shivang/.cc_replay/', 'cookiecutter-pypackage')
    with open(replay_file, 'w') as outfile:
        json.dump(context, outfile, indent=2)
    jsonData = load('/home/shivang/.cc_replay/', 'cookiecutter-pypackage.json')
    assert jsonData

# Generated at 2022-06-13 18:39:10.992468
# Unit test for function get_file_name
def test_get_file_name():
    test_dir='/abc/def'
    test_template_name='xyz'
    test_suffix='.json'
    assert get_file_name(test_dir,test_template_name)=='/abc/def/xyz.json'
    test_template_name='xyz.json'
    assert get_file_name(test_dir,test_template_name)=='/abc/def/xyz.json'

# Generated at 2022-06-13 18:39:23.431087
# Unit test for function load
def test_load():
    # Test load function with template_name
    replay_dir = 'src/tests/test-replay/'
    template_name = 'src/tests/test-repo'
    assert load(replay_dir, template_name)["cookiecutter"]["repo_name"] == "{{ cookiecutter.repo_name }}"

    # Test load function with template_name and .json suffix
    template_name = 'src/tests/test-repo.json'
    assert load(replay_dir, template_name)["cookiecutter"]["repo_name"] == "{{ cookiecutter.repo_name }}"

    # Test load function with non-existing directory
    replay_dir = 'src/tests/test-replay-does-not-exist'

# Generated at 2022-06-13 18:39:29.236578
# Unit test for function dump
def test_dump():
    # Test if the function handle wrong type
    replay_dir="./tests"
    template_name=123
    context="test"
    try:
        dump(replay_dir,template_name,context)
    except:
        pass
    else:
        assert False, "Did not see Type Error"

    # Test if the function handel missing required data
    template_name="test"
    context={}
    try:
        dump(replay_dir,template_name,context)
    except:
        pass
    else:
        assert False, "Did not see Value Error"


# Generated at 2022-06-13 18:39:35.069531
# Unit test for function load
def test_load():
    if not os.path.exists('test'):
        os.makedirs('test')
    if not os.path.exists('test/replay'):
        os.makedirs('test/replay')
    context = {'cookiecutter': {'first_name': u'Audrey', 'last_name': u'Roy Greenfeld', 'username': u'audreyr'}}
    dump('test/replay', 'my_template', context)
    assert load('test/replay', 'my_template') == context

if __name__ == '__main__':
    test_load()

# Generated at 2022-06-13 18:39:40.809366
# Unit test for function dump
def test_dump():
    """Unit test for function dump."""
    replay_dir = os.path.join("tests", "test-replay")
    if not make_sure_path_exists(replay_dir):
        raise IOError('Unable to create replay dir at {}'.format(replay_dir))
    elif make_sure_path_exists(replay_dir):
        template_name = "fixture-replay"
        context = {'cookiecutter': {'full_name': 'Vitor Hugo', 'email': 'vitorh@example.com', 'foo': 'bar'}}
        dump(replay_dir, template_name, context)
        assert os.path.exists(os.path.join(replay_dir, template_name) + '.json') is True


# Generated at 2022-06-13 18:39:46.367965
# Unit test for function load
def test_load():
    replay_dir = os.path.join('.', 'tests', 'test_data', 'replay_dir')
    context = load(replay_dir, 'pypackage')
    assert context['cookiecutter']


# Generated at 2022-06-13 18:39:52.058161
# Unit test for function dump
def test_dump():
    replay_dir = '/tmp/cookiecutter-replay/'
    template_name = 'replay-test'
    context = {'cookiecutter': {'hello': 'world'}}
    dump(replay_dir, template_name, context)
    context = load(replay_dir, template_name)
    assert(context == {'cookiecutter': {'hello': 'world'}})

# Generated at 2022-06-13 18:39:56.668194
# Unit test for function dump
def test_dump():
    # Given
    template_name = 'dummy'
    replay_dir = '/Users/paul/cookiecutter'
    context = {'cookiecutter': {'dummy': 'dummy'}}

    # When
    dump(replay_dir, template_name, context)

    # Then
    assert os.path.exists(get_file_name(replay_dir, template_name))

# Generated at 2022-06-13 18:40:01.514933
# Unit test for function dump
def test_dump():
    replay_dir = os.path.join(
        os.path.expanduser('~'), '.cookiecutters', 'replay'
    )
    make_sure_path_exists(replay_dir)
    template_name = 'cookiecutter-pypackage'
    context = {
        'cookiecutter': {
            '_template': template_name,
            'email': 'example@gmail.com',
            'full_name': 'Example Example',
            'github_username': 'example',
            'project_name': 'test-project',
            'project_slug': 'test_project',
            'pypi_username': 'example',
        },
    }
    dump(replay_dir, template_name, context)


# Generated at 2022-06-13 18:40:04.407346
# Unit test for function load
def test_load():
    """Test function load"""
    if __name__ == "__main__":
        print(load('./replay', 'grunt_project'))


# Generated at 2022-06-13 18:40:11.211068
# Unit test for function dump
def test_dump():
    """Unit test for dump function."""
    from tempfile import mkdtemp
    template_name = '{{cookiecutter.repo_name}}'
    context = {
        'cookiecutter': {'repo_name': 'name'},
    }

    replay_dir = mkdtemp()
    replay_file = get_file_name(replay_dir, template_name)
    dump(replay_dir, template_name, context)
    assert os.path.exists(replay_file)
    assert os.path.isdir(replay_dir)

    # clean up
    os.remove(replay_file)
    os.rmdir(replay_dir)



# Generated at 2022-06-13 18:40:16.197979
# Unit test for function load
def test_load():
    assert load('/Users/lzx1311/Desktop/CookieCutters/cookiecutter-pypackage/', 'foobar') == {'cookiecutter': {}}


# Generated at 2022-06-13 18:40:17.882669
# Unit test for function dump
def test_dump():
    context = {'name': 'Martin', 'age': 35}
    dump('', 'testfile', context)


# Generated at 2022-06-13 18:40:20.247998
# Unit test for function load
def test_load():
    assert load(replay_dir="C:\\Users\\sweethome\\Documents\\GitHub\\Cookiecutter-Template",template_name="cookiecutter.json") 

# Generated at 2022-06-13 18:40:22.136894
# Unit test for function load
def test_load():
    context = load('~/.cookiecutters', 'cookiecutter-pypackage')
    assert(context['cookiecutter']['author_email'] == 'me@localhost')

# Generated at 2022-06-13 18:40:28.040735
# Unit test for function load
def test_load():

    cookiecutter_dict = {
        "cookiecutter": {
            "full_name": "Your Name",
            "email": "your@email.com",
            "github_username": "yourname",
            "project_name": "Project Name",
            "project_slug": "project_name",
            "pypi_username": "yourname",
            "version": "0.1.0",
            "release": "0.1.0",
            "_copy_without_render": [
               "{{cookiecutter.project_slug}}/pyproject.toml"
            ],
            "use_pycharm": true,
            "use_github": true,
            "open_source_license": "MIT"
         }
    }

    # Test file does not exist

# Generated at 2022-06-13 18:40:39.613736
# Unit test for function load
def test_load():
    from cookiecutter.config import DEFAULT_REPLAY_DIR
    # Test case 1: A file is not found at path
    # Excepted: Raise IOError
    try:
        load("example", "notfound")
    except IOError:
        pass

    replay_file = get_file_name(DEFAULT_REPLAY_DIR, "example")
    with open(replay_file, 'w') as outfile:
        json.dump({"cookiecutter": {"key": "value"}}, outfile, indent=2)

    # Test case 2: A context does not contain a cookiecutter key
    # Excepted: Raise ValueError
    try:
        load(DEFAULT_REPLAY_DIR, "example")
    except ValueError:
        pass


# Generated at 2022-06-13 18:40:42.465484
# Unit test for function load
def test_load():
    """Unit test for function load."""
    assert load("replay/", "foobar") == {"cookiecutter": {}}


# Generated at 2022-06-13 18:40:43.972124
# Unit test for function load
def test_load():
    assert load('/home/cdsw/.cookiecutters/', 'test', )



# Generated at 2022-06-13 18:40:48.061083
# Unit test for function load
def test_load():
    file_path = os.path.dirname(os.path.abspath(__file__))
    test_dir = os.path.join(file_path, 'test.json')
    context = load(file_path, 'test')
    assert context['cookiecutter'] == {'a': '1'}

# Generated at 2022-06-13 18:40:51.333072
# Unit test for function load
def test_load():
    context = load('cookiecutter/tests/test-replay', 'example-replay')
    assert context['cookiecutter']['full_name'] == 'Audrey Roy'


# Generated at 2022-06-13 18:40:55.542571
# Unit test for function load
def test_load():
    replay_dir = '.'
    template_name = 'cookie-board'
    context = load(replay_dir, template_name)
    assert(context != None)

# Generated at 2022-06-13 18:41:05.704397
# Unit test for function load
def test_load():
    """Test for function load."""
    from tempfile import mkdtemp
    from shutil import rmtree
    from random import randint
    import json
    import os

    # Create a temporary directory to store the replay_dir.
    replay_dir = mkdtemp()
    # Create a random list
    context = {'cookiecutter': {'random_list': [randint(0, 100) for x in range(10)]}}
    # Write the list to a json file
    with open(os.path.join(replay_dir, 'replay_test.json'), 'w') as f:
        json.dump(context, f)
    # Load context
    result = load(replay_dir, 'replay_test')
    # Remove the temporary directory
    rmtree(replay_dir)
    # Compare the

# Generated at 2022-06-13 18:41:09.900525
# Unit test for function dump
def test_dump():
    replay_dir = 'test_replay_dir'
    template_name = 'test_template'
    context = {
        'cookiecutter': {
            'project_name': 'test',
            'description': 'test'
        }
    }
    dump(replay_dir, template_name, context)
    result = load(replay_dir, template_name)
    os.remove(get_file_name(replay_dir, template_name))
    assert context == result


# Generated at 2022-06-13 18:41:14.568180
# Unit test for function load
def test_load():
    """Unit test for function load."""
    import tempfile

    replay_dir = tempfile.mkdtemp()
    template_name = '{{ cookiecutter.templatename }}'

    context = {
        'cookiecutter': {
            'templatename': 'test',
        }
    }
    dump(replay_dir, template_name, context)

    context = load(replay_dir, template_name)
    assert context['cookiecutter']['templatename'] == 'test'

    # test with a non existent template
    try:
        context = load(replay_dir, 'nonexistent')
        assert False
    except IOError:
        assert True

    # test with a non JSON file

# Generated at 2022-06-13 18:41:23.715541
# Unit test for function dump
def test_dump():
    """Test the dump method."""
    import json
    import os

    # test if the replay file is created
    replay_dir = 'tests/test-output/replays'
    template_name = 'hello-world'

# Generated at 2022-06-13 18:41:25.937101
# Unit test for function load
def test_load():
    assert load('../tests/replay', 'cookiecutter-pypackage') is not None


# Generated at 2022-06-13 18:41:35.466534
# Unit test for function load
def test_load():
    import json
    import os
    import shutil
    from cookiecutter.utils import make_sure_path_exists

    # create test directory
    replay_dir = 'test_load_directory'
    make_sure_path_exists(replay_dir)
    # write test replay file
    replay_file = os.path.join(replay_dir, 'test_load.json')
    file1 = open(replay_file, 'w')
    file1.write('{"cookiecutter": {"test_load": "test_data"}}')
    file1.close()

    # test load
    context = load(replay_dir, 'test_load')
    assert type(context) is dict
    assert context['cookiecutter']['test_load'] == 'test_data'

    # clean up test directory

# Generated at 2022-06-13 18:41:42.684234
# Unit test for function load
def test_load():
    replay_file = "cookiecutter.json"
    if not os.path.exists(replay_file):
        raise IOError('Unable to find replay file at {}'.format(replay_file))

    with open(replay_file, 'r') as infile:
        context = json.load(infile)

    if 'cookiecutter' not in context:
        raise ValueError('Context is required to contain a cookiecutter key')

    return context

# Generated at 2022-06-13 18:41:47.227152
# Unit test for function dump
def test_dump():
    replay_dir = 'tests/test-replay-dir'
    template_name = 'test'
    context = {'cookiecutter': {'test': 'test-value'}}
    dump(replay_dir, template_name, context)
    context_loaded = load(replay_dir, template_name)
    assert context_loaded == context
    os.remove(replay_dir + '/' + template_name + '.json')

# Generated at 2022-06-13 18:41:50.086861
# Unit test for function load
def test_load():
    context = load('/home', 'test-replay')
    print(context)
    print(type(context))


if __name__ == '__main__':
    test_load()

# Generated at 2022-06-13 18:41:58.076122
# Unit test for function load
def test_load():
    # Open the file and load the context
    context = load('tests/test-load-replay', 'tests/fake-repo-tmpl')
    assert context['cookiecutter'] == {
        'full_name': 'Audrey Roy',
        'email': 'audreyr@example.com',
        'project_name': 'cookiecutter-pypackage',
        'project_slug': 'cookiecutter-pypackage',
        'project_license': 'MIT license',
        'year': '2013',
        'version': '0.1.0',
    }

# Generated at 2022-06-13 18:42:02.670588
# Unit test for function load

# Generated at 2022-06-13 18:42:03.907164
# Unit test for function load
def test_load():
    assert load("/my/home/andy/.cookiecutters/","foo.json") != None

# Generated at 2022-06-13 18:42:08.314437
# Unit test for function load
def test_load():
    """Unit test for function load."""
    class TestClass:
        def __init__(self):
            self.name = 'Bad file'
            self.location = '.'

    test_data = [
        {'name': 'Good file',
         'location': os.path.join('tests', 'test-data', 'replies', 'alpha.json')},
        {'name': 'Good file',
         'location': os.path.join('tests', 'test-data', 'replies', 'alpha.json')}

    ]
    test_data.append(TestClass())
    test_data.append([])
    test_data.append({})
    test_data.append(123)


# Generated at 2022-06-13 18:42:16.884160
# Unit test for function dump
def test_dump():
    """Unit test for function dump"""
    from cookiecutter import utils
    replay_dir = os.path.join(os.path.dirname(__file__), 'mock_replay_dir')
    template_name = 'mock_template_name'
    context = {
        'cookiecutter': {
            'project_name': 'mock_project_name',
            'repo_name': 'mock_repo_name',
        }
    }
    mock_replay_dir = os.path.join(replay_dir, template_name + '.json')
    try:
        dump(replay_dir, template_name, context)
        assert os.path.exists(mock_replay_dir)
    finally:
        utils.rmtree(mock_replay_dir)

# Generated at 2022-06-13 18:42:20.677754
# Unit test for function load
def test_load():
    test_replay_dir = os.path.join(os.getcwd(), 'tests/test-replay')
    template_name = 'foobar'
    context = load(test_replay_dir, template_name)
    context_expected = {
        'cookiecutter': {
            'foo': 'bar',
            'bar': 'baz',
        }
    }
    assert isinstance(context, dict)
    assert context == context_expected


if __name__ == '__main__':
    test_load()

# Generated at 2022-06-13 18:42:26.276618
# Unit test for function dump
def test_dump():
    data1 = {
        'foo': '{{cookiecutter.repo_name}}',
        'bar': '{{cookiecutter.repo_name}}',
        'cookiecutter': {
            'repo_name': 'foo'
        }
    }
    dump()
    assert data1 == {'foo': 'test_repo', 'bar': 'test_repo', 'cookiecutter': {'repo_name': 'test_repo'}}

# Generated at 2022-06-13 18:42:32.370979
# Unit test for function dump
def test_dump():
    """Unit test for function dump."""
    replay_dir = 'tmp/replay'
    template_name = 'cookiecutter-pypackage'
    context = {'cookiecutter': '1234567890'}
    dump(replay_dir, template_name, context)

    replay_file = get_file_name(replay_dir, template_name)
    with open(replay_file) as f:
        content = f.read()
    expected_content = '{\n  "cookiecutter": "1234567890"\n}'
    assert content == expected_content


# Generated at 2022-06-13 18:42:34.980390
# Unit test for function load
def test_load():
    replay_dir = '/Users/ljb/workspace/python/cookiecutter-replay/tests/tests_replay'
    context = load(replay_dir, 'pypackage')
    print(context)


# Generated at 2022-06-13 18:42:37.203355
# Unit test for function load
def test_load():
    assert load('replay/', "templateName") == {'cookiecutter': {'key1': 'value1', 'key2': 'value2'}}, 'Error: load'

# Generated at 2022-06-13 18:42:54.603122
# Unit test for function load
def test_load():
    """Unit test for function load."""
    import json
    import os
    
    import pytest
    
    from cookiecutter.operations import load
    from cookiecutter.replay import get_file_name

    replay_dir = os.getcwd()
    
    with pytest.raises(TypeError) as excinfo:
        load(replay_dir, None)
    assert 'template name' in str(excinfo.value).lower()
    
    with pytest.raises(FileNotFoundError) as excinfo:
        load(replay_dir, 'foo')

    template_name = 'tests/fake-repo-pre/'
    context = load(replay_dir, template_name)
    assert 'cookiecutter' in context
    assert context['cookiecutter']['full_name']

# Generated at 2022-06-13 18:42:58.897415
# Unit test for function dump
def test_dump():
    replay_dir = "../test/test_directory_for_replay"
    template_name = "test_template"
    context = {
        "cookiecutter": {
            "test_key1": "test_value1",
            "test_key2": "test_value2"
        }
    }

    dump(replay_dir, template_name, context)


# Generated at 2022-06-13 18:43:08.880117
# Unit test for function dump
def test_dump():
    import os
    import os.path
    path = os.path.join(os.path.dirname(__file__), '../tests/fake-repo-pre/')
    template_name = "{{cookiecutter.project_slug}}"
    context = {}
    context["cookiecutter"] = {}
    context["cookiecutter"]["project_name"] = "Project Name"
    context["cookiecutter"]["project_slug"] = "project_name"
    context["cookiecutter"]["author_name"] = "Your Name"
    context["cookiecutter"]["email"] = "your email"
    context["cookiecutter"]["description"] = "A short description of the project."
    context["cookiecutter"]["version"] = "0.1.0"

# Generated at 2022-06-13 18:43:11.452244
# Unit test for function load

# Generated at 2022-06-13 18:43:18.139216
# Unit test for function load
def test_load():
    context_test = {'cookiecutter':{'project_name':'tests', 'project_slug':'test'}}
    dump('tests', 'test.json', context_test)
    context_load = load('tests', 'test.json')
    for key, value in context_test.items():
        for key2, value2 in value.items():
            assert key2 in context_load[key]
            assert value2 == context_load[key][key2]

# Generated at 2022-06-13 18:43:23.795822
# Unit test for function dump
def test_dump():
    """Test the dump function."""
    template_name = 'test'
    context = {'cookiecutter': {'foo': 'bar'}}

    replay_dir = 'somereplaydir'
    dump(replay_dir, template_name, context)
    assert os.path.exists(get_file_name(replay_dir, template_name)) is True
    os.remove(get_file_name(replay_dir, template_name))
    assert os.path.exists(get_file_name(replay_dir, template_name)) is False



# Generated at 2022-06-13 18:43:27.586250
# Unit test for function load
def test_load():
    """Test the load function."""
    assert load('templates', 'cookiecutter-pypackage') != None
    try:
        load('templates', 'cookiecutter-pypackage')
    except ValueError:
        print('ValueError is raised')


# Generated at 2022-06-13 18:43:33.565281
# Unit test for function dump
def test_dump():
    replay_dir = '.'
    template_name = './{{cookiecutter.directory_name}}'
    context = {'cookiecutter': {'directory_name': 'name'}}
    dump(replay_dir, template_name, context)
    assert os.path.exists(template_name + '.json')



# Generated at 2022-06-13 18:43:44.828669
# Unit test for function load
def test_load():
    from cookiecutter import main
    from cookiecutter.replay import load
    from cookiecutter.config import DEFAULT_CONFIG
    from cookiecutter.context_file import generate_context_file

    main.cookiecutter('tests/fake-repo-tmpl', no_input=True, replay=False)

    ctx_file = generate_context_file('tests/fake-repo-tmpl')
    loaded_context = load(DEFAULT_CONFIG['replay_dir'], ctx_file)
    assert loaded_context == {
        'cookiecutter': {
            'fake_key': 'fake_value',
            '_template': 'tests/fake-repo-tmpl'
        }
    }

    os.remove(ctx_file)

# Generated at 2022-06-13 18:43:49.324350
# Unit test for function dump
def test_dump():
    basepath = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data')
    context = {'cookiecutter': {'name': 'test_name'}}
    dump(basepath, 'test_name', context)

    context_loaded = load(basepath, 'test_name')
    if context_loaded['cookiecutter']['name'] == 'test_name':
        print("Context_loaded is equal to what set.")
    else:
        print("Context_loaded is not equal to what set..")



# Generated at 2022-06-13 18:44:07.545681
# Unit test for function dump
def test_dump():
    replay_dir = os.path.abspath('tests/test-output')
    template_name = 'test-template'
    context = {
        'cookiecutter': {
            'key': 'value'
        }
    }
    dump(replay_dir, template_name, context)
    dump_file = os.path.join(replay_dir, 'test-template.json')
    if os.path.isfile(dump_file):
        assert True
    else:
        assert False


# Generated at 2022-06-13 18:44:12.164249
# Unit test for function dump
def test_dump():
    template_name = 'template1'
    context = {
        "cookiecutter": {
            "full_name": "Your Name",
            "email": "your@email.com",
            "github_username": "YourGitHubUsername"
        }
    }

    replay_dir = 'tmp'

    dump(replay_dir, template_name, context)
    result = load(replay_dir, template_name)


# Generated at 2022-06-13 18:44:16.000116
# Unit test for function load
def test_load():
    #create context
    from cookiecutter.main import cookiecutter
    from cookiecutter import utils

    template_name = 'cookiecutter-pypackage'
    context = cookiecutter(template_name)

    #create replay directory
    replay_dir = "replay"
    utils.make_sure_path_exists(replay_dir)

    #dump context to replay directory
    dump(replay_dir, template_name, context)

    #load context from replay directory
    context_test = load(replay_dir, template_name)
    print (context == context_test)
    return context == context_test

if __name__ == '__main__':
    print(test_load())

# Generated at 2022-06-13 18:44:25.811380
# Unit test for function load
def test_load():
    dump('/home/i320999/PycharmProjects/cookiecutter/tests/test-load', 'test_load', {
    'cookiecutter': {
        'full_name': 'Audrey Roy',
        'email': 'audreyr@example.com',
        'github_username': 'audreyr',
        'project_name': '{{ cookiecutter.repo_name }}',
        'description': 'A short description of the project.',
        'project_short_description': 'A short description of the project.',
        'version': '0.1',
        'open_source_license': 'BSD license',
        'pypi_username': 'audreyr',
        'use_pypi_deployment_with_travis': 'y',
        }}
    )

# Generated at 2022-06-13 18:44:28.178255
# Unit test for function load
def test_load():
    res = load("./tests/fixtures/fake-replay/", "foobar")
    assert res['cookiecutter'] == {'replay': 'true'}


# Generated at 2022-06-13 18:44:33.634186
# Unit test for function dump
def test_dump():
    from tempfile import mkdtemp

    temp_dir = mkdtemp()
    path = os.path.join(temp_dir, 'replay')

    test_context = {
        'cookiecutter': {
            'full_name': 'Test User',
            'email': 'test@example.com',
            'github_username': 'testuser',
        }
    }
    dump(path, 'test', test_context)

    with open(get_file_name(path, 'test'), 'r') as infile:
        written_context = json.load(infile)

    assert written_context == test_context

# Generated at 2022-06-13 18:44:38.259197
# Unit test for function load
def test_load():
    context = load('/home/anthea/Documents/cookiecutter-django/cookiecutter/tests/files/fake-replay-dir', 'bogus-file')
    assert context == {'cookiecutter': {'full_name': 'Simon', 'email': 'motor@gmx.de'}}

#Unit test for function dump

# Generated at 2022-06-13 18:44:41.445083
# Unit test for function load
def test_load():
    print("test load started")
    context1 = load('replay', 'python-simple-module')
    context2 = load('replay', 'python-copycat')
    if context1 != None and context2 != None:
        print("test load passed")
    else:
        print("test load failed")


# Generated at 2022-06-13 18:44:50.299665
# Unit test for function dump
def test_dump():

    # templete_name is not string
    template_name_int = 1
    replay_dir_int = "./"
    context_int = {"cookiecutter":{"pi":3.14} }
    try:
        dump(replay_dir_int, template_name_int, context_int)
    except Exception:
        pass
    else:
        assert False

    # context is not dictionary
    template_name_dict = "test"
    replay_dir_dict = "./"
    context_dict = "cookiecutter"
    try:
        dump(replay_dir_dict, template_name_dict, context_dict)
    except Exception:
        pass
    else:
        assert False

    # context does not contain cookiecutter key
    template_name_key = "test"

# Generated at 2022-06-13 18:45:04.433287
# Unit test for function load
def test_load():
    replay_dir = os.path.join(os.getcwd(), '.cookiecutters')
    template_name = 'example-strict'

    context = load(replay_dir, template_name)

    assert type(context) == dict
    print(context)

# Generated at 2022-06-13 18:45:21.146772
# Unit test for function dump
def test_dump():
    template_name = 'my_template'
    context = {'key': 'value', 'cookiecutter': {'a': 'b', 'b': 'c'}}
    replay_dir = os.path.join(os.path.expanduser('~'), '.cookiecutters')
    dump(replay_dir, template_name, context)


# Generated at 2022-06-13 18:45:24.281242
# Unit test for function load
def test_load():
    context = load("./test_template", "test_template")
    assert context == {'cookiecutter': {'full_name': 'Monty Python', 'email': 'monty@python.org', 'github_username': 'montypython'}}

# Generated at 2022-06-13 18:45:26.993127
# Unit test for function load
def test_load():
    print("Output of load function:")
    print(load("C:\\Users\\harit\\Desktop\\replay", "sas"))
    print("\n")



# Generated at 2022-06-13 18:45:35.938886
# Unit test for function load
def test_load():
    template_name= "cookiecutter-pypackage"
    replay_dir= "/home/sinead/replay/package"
    out= load(replay_dir, template_name)

# Generated at 2022-06-13 18:45:44.397414
# Unit test for function dump
def test_dump():
    test_dict = {'name': 'Github user name'}
    template = 'test'
    DIR = '/tmp/test_replay'
    dump(DIR, template, test_dict)
    assert(os.path.exists(DIR))

    with open('/tmp/test_replay/test.json','r') as replay_file:
        json_data = json.load(replay_file)

    assert(json_data == test_dict)


# Generated at 2022-06-13 18:45:54.249743
# Unit test for function load
def test_load():
    """Test case for load."""
    from cookiecutter import prompt
    from cookiecutter import main
    from tempfile import mkdtemp
    from shutil import rmtree
    from os.path import join
    from copy import copy

    tmp_dir = mkdtemp()
    replay_dir = join(tmp_dir, 'replay')
    template_name = 'foobar'

    try:
        ctxt = load(replay_dir, template_name)
        assert False
    except EnvironmentError:
        assert True

    try:
        ctxt = load(replay_dir, template_name)
        assert False
    except ValueError:
        assert True

    # Prompt should be disbled
    template_dir = join(tmp_dir, 'foobar')

# Generated at 2022-06-13 18:45:55.624594
# Unit test for function load
def test_load():
    assert load('data','template') == {'cookiecutter': {'key':'value'}}


# Generated at 2022-06-13 18:45:59.121163
# Unit test for function load
def test_load():
    context = load('/Users/edwardyoon/projects/cookiecutter-pypackage', 'cookiecutter.json')

# Generated at 2022-06-13 18:46:00.459124
# Unit test for function load
def test_load():
    load(r'C:\Users\shir-l\PycharmProjects\cookiecutter', 'cookiecutter')

# Generated at 2022-06-13 18:46:06.937048
# Unit test for function dump
def test_dump():
    import shutil
    # Unit test for function dump
    global replay_dir, template_name, context
    
    #create files to dump information
    replay_dir = './test'
    template_name = 'example'
    context = {'cookiecutter':
                  {'full_name': 'First Last',
                   'email': 'flast@example.com',
                   'github_username': 'flast',
                   'project_name': 'Cookiecutter-Example',
                   'project_short_description': 'Cookiecutter Example Project.',
                   'release_date': '2014/01/01',
                   'year': '2014',
                   'version': '0.1.0'}
              }
    dump(replay_dir, template_name, context)
    
    #delete files
    #shutil.r

# Generated at 2022-06-13 18:46:35.222043
# Unit test for function load
def test_load():
    # Dummy template_name
    template_name = 'name_of_the_template'
    # Dummy context
    dummy_context = {'name': 'Test name', 'surname': 'Test surname'}
    # Dummy replay_dir
    replay_dir = 'test/test_cookiecutter/test_replay/'
    # Dump dummy context
    dump(replay_dir, template_name, dummy_context)
    # Load dumped context
    context = load(replay_dir, template_name)
    # Compare the dummy context and the loaded context
    assert dummy_context == context

    # Test function load with wrong template name
    try:
        load(replay_dir, "wrong_template_name")
    except Exception:
        pass
        
    # Test function load with wrong replay_dir (directory does

# Generated at 2022-06-13 18:46:37.027328
# Unit test for function load
def test_load():
    from json import load
    from os import path
    from sys import argv

    load(argv[1], argv[2])


# Generated at 2022-06-13 18:46:38.962336
# Unit test for function load
def test_load():
    print(load('/Users/carmenchu/Documents/GitHub/mycookiecutter/mycookiecutter/replay', 'abc.json'))


# Generated at 2022-06-13 18:46:42.592206
# Unit test for function dump
def test_dump():
    template_name = 'test_dump'
    replay_dir = 'testing_replay'
    context = {'cookiecutter': {'test_key': 'test_value'}}
    dump(replay_dir, template_name, context)
    assert os.path.exists(get_file_name(replay_dir, template_name))


if __name__ == '__main__':
    test_dump()

# Generated at 2022-06-13 18:46:47.762828
# Unit test for function load
def test_load():
    #Test if template_name is wrong
    try:
        load('C:/Users/Nathan/PycharmProjects/cookiecutter/tests/files', 123)
        assert False
    except TypeError:
        assert True
    #Test if replay_dir is wrong
    try:
        load(123, 'fake')
        assert False
    except TypeError:
        assert True
    #Test if context is wrong
    try:
        load('C:/Users/Nathan/PycharmProjects/cookiecutter/tests/files', 'fake')
        assert False
    except ValueError:
        assert True


# Generated at 2022-06-13 18:46:48.836176
# Unit test for function dump
def test_dump():
    assert dump(replay_dir, template_name, context)


# Generated at 2022-06-13 18:46:57.024255
# Unit test for function load
def test_load():
    replay_dir = '~/cookie/replay/dir'
    template_name = 'test'
    context = {
        'cookiecutter': {
            'full_name': 'Your Name',
            'email': 'Your email'}
        }
    fname = get_file_name(replay_dir, template_name)
    #print 'fname=', fname
    dump(replay_dir, template_name, context)
    context_read = load(replay_dir, template_name)
    assert (context == context_read)
    #assert (context != context_read)
    #os.remove(fname)


# Generated at 2022-06-13 18:46:59.946401
# Unit test for function load
def test_load():
    template_name = 'project_name'
    replay_dir = '/home/yunxingz/cookiecutter/cookiecutter-pypackage/replay'
    context = load(replay_dir, template_name)
    print(context)


# Generated at 2022-06-13 18:47:05.237464
# Unit test for function load
def test_load():

    replay_dir = "../tests/test-replay/replays"
    template_name = "sub-sub-subfolder"
    replay_file = get_file_name(replay_dir, template_name)
    context = load(replay_dir, template_name)

    assert context is not None


# Generated at 2022-06-13 18:47:08.532553
# Unit test for function load
def test_load():
    """Unit test for function load."""
    dir="tests/test-replay"
    template_name="simple-cookiecutter-template"
    template = load(dir,template_name)
    assert type(template)==dict


# Generated at 2022-06-13 18:47:37.982666
# Unit test for function load
def test_load():
    replay_dir = r'C:\Users\prozach\Documents\GitHub\cookiecutter\tests\test-generate-files'
    template_name = r'{{cookiecutter.project_slug}}'
    context = load(replay_dir, template_name)
    print('type(context):',type(context))
    print('type(context[cookiecutter]):',type(context['cookiecutter']))
    print('keys:',context.keys())
    print('context[cookiecutter] keys:',context['cookiecutter'].keys())
    print('context[cookiecutter] values:')
    for k in context['cookiecutter']:
        print('{}: {}'.format(k, context['cookiecutter'][k]))


# Generated at 2022-06-13 18:47:45.914575
# Unit test for function load
def test_load():
    replay_dir = 'tests/replay-tests'
    template_name = 'long-description'

    expected_context = {
        'cookiecutter' : {
            'description': 'An amazing Python package.',
            'full_name': 'Audrey Roy Greenfeld',
            'project_name': 'cookiecutter-pypackage',
            'project_slug': 'cookiecutter-pypackage',
            'project_short_description': 'A short description of the project',
            'release_date': '2013/09/03'
        }
    }

    context = load(replay_dir, template_name)
    assert context == expected_context

# Generated at 2022-06-13 18:47:49.819868
# Unit test for function load
def test_load():
    replay_dir = 'C:/Users/18234/Desktop/GitHub/cookiecutter/cookiecutter'
    template_name = 'my-fake-project'
    context = load(replay_dir,template_name)
    print(context)


# Generated at 2022-06-13 18:47:54.866144
# Unit test for function load
def test_load():
    """Unit test for function load"""
    template_name = 'gh:audreyr/cookiecutter-pypackage'
    replay_file = get_file_name(os.getcwd(), template_name)
    context = load(os.getcwd(), template_name)
    assert 'cookiecutter' in context

# Generated at 2022-06-13 18:47:57.417766
# Unit test for function load
def test_load():
    replay_dir = "cookiecutter"
    template_name = "cookiecutter"
    print(load(replay_dir, template_name))


# Generated at 2022-06-13 18:48:03.677840
# Unit test for function dump
def test_dump():
    # create an empty replay file
    replay_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../tests/replay'))
    template_name = 'empty'
    context = {}

    dump(replay_dir, template_name, context)
    # check the content of the created file is empty
    replay_file = get_file_name(replay_dir, template_name)
    with open(replay_file, 'r') as infile:
        content = json.load(infile)
    if content != {}:
        print('error dump empty replay')

    print('pass test_dump')



# Generated at 2022-06-13 18:48:07.736157
# Unit test for function load
def test_load():
    """Test load"""
    answer = load('{{cookiecutter.replay_dir}}', '{{cookiecutter.template}}')
    assert answer['cookiecutter']['full_name'] == \
        '{{cookiecutter.full_name}}'


# Generated at 2022-06-13 18:48:12.004103
# Unit test for function load
def test_load():
    # Replay file is existent
    context = load(os.getcwd(), 'cookiecutter-pypackage')
    print(context['cookiecutter']['pkg_name'])

    # Replay file is nonexistent
    context = load(os.getcwd(), 'cookiecutter-nopypackage')
    print(context['cookiecutter']['pkg_name'])