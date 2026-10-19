

# Generated at 2022-06-13 18:38:22.240657
# Unit test for function dump
def test_dump():
    print("test the functions dump")
    replay_dir = "test_files"
    template_name = "test_template"

# Generated at 2022-06-13 18:38:25.457972
# Unit test for function load
def test_load():
    dir = os.path.expanduser('~/.cookiecutters')
    name = 'https://github.com/audreyr/cookiecutter-pypackage'
    context = load(dir, name)
    print(context)


# Generated at 2022-06-13 18:38:27.932454
# Unit test for function load
def test_load():
    print(load(".", "foo"))
    print(load('~/Downloads/cookiecutter-pypackage', 'cookiecutter-pypackage'))

# Generated at 2022-06-13 18:38:34.129439
# Unit test for function dump
def test_dump():
    replay_dir='tests/test-output/replay'
    template_name='hello-world-cookiecutter'
    context={'cookiecutter': {'full_name': 'Audrey Roy Greenfeld', 'email': 'audreyr@example.com', 'github_username': 'audreyr', 'project_name': 'Hello World', 'project_slug': 'hello-world', 'pypi_username': 'audreyr', 'release_date': '2014-10-03', 'year': '2014', 'version': '0.1.0'}}
    dump(replay_dir, template_name, context)


# Generated at 2022-06-13 18:38:36.089831
# Unit test for function load
def test_load():
    assert load('./tests/fake-repo-pre/', 'fake-repo-pre') != {}

# Generated at 2022-06-13 18:38:39.000275
# Unit test for function load
def test_load():
    # Arrange
    template_name = ''

# Generated at 2022-06-13 18:38:42.937158
# Unit test for function dump
def test_dump():
    context = {
        'cookiecutter': {
            'full_name': 'Robi',
            'email': 'robi@robi.com',
        }
    }

    dump('replay', 'test_dump', context)


# Generated at 2022-06-13 18:38:47.832398
# Unit test for function load
def test_load():
    """Test load."""
    data = {'cookiecutter': 'test'}
    replay_dir = 'test_replay_dir'
    template_name = 'test_template_name'
    filename = get_file_name(replay_dir, template_name)

    # Test that the data does not exist before saving it
    if os.path.isfile(filename):
        os.remove(filename)
    assert os.path.isfile(filename) is False

    # Test saving data
    dump(replay_dir, template_name, data)
    assert os.path.isfile(filename) is True

    # Test loading data
    data2 = load(replay_dir, template_name)
    assert data == data2

    # Test that we have an error if we try to load a file that has no cookiecutter

# Generated at 2022-06-13 18:39:00.839376
# Unit test for function dump
def test_dump():
# if __name__ == '__main__':
#     import unittest
#     import os

    def _test_setup_and_teardown():
        replay_dir = 'replay'
        if os.path.exists(replay_dir):
            os.system("rm -rf '{0}'".format(replay_dir))

        os.makedirs(replay_dir)

        return replay_dir

    # def test_dump(self):
    replay_dir = _test_setup_and_teardown()


# Generated at 2022-06-13 18:39:05.526455
# Unit test for function load
def test_load():
    """Unit test for function load."""
    if __name__ == '__main__':
        context = load('./tests/fixtures/fake-replay-dir', 'jquery-ui')
        assert type(context) is dict
        assert 'cookiecutter' in context
        assert context['cookiecutter'] == {'project_name': 'jQuery UI'}



# Generated at 2022-06-13 18:39:11.999899
# Unit test for function load
def test_load():
    replay_dir = 'cookiecutter-pypackage-2017-08-02T19:01:47.109567'
    template_name = 'cookiecutter-pypackage'
    # cookiecutter(replay=True,no_input=True,output_dir='cookiecutter-pypackage-2017-08-02T19:01:47.109567',replay_dir='cookiecutter-pypackage-2017-08-02T19:01:47.109567')


# def test():


# Generated at 2022-06-13 18:39:17.015142
# Unit test for function load
def test_load():
    # Create replay directory and template file
    replay_dir = '/tmp/replay_dir'
    make_sure_path_exists(replay_dir)

    template_name = 'my_template'
    json_data = '{"cookiecutter": {"slug": "your_slug"}}'

    replay_file = get_file_name(replay_dir, template_name)

    with open(replay_file, 'w') as outfile:
        outfile.write(json_data)

    context = load(replay_dir, template_name)

    assert context['cookiecutter']['slug'] == 'your_slug'

    # Cleanup
    os.remove(replay_file)
    os.rmdir(replay_dir)



# Generated at 2022-06-13 18:39:24.435197
# Unit test for function get_file_name
def test_get_file_name():
    # Testing a file_name that do not end with .json
    if(get_file_name("abcd", "abcd") == "abcd/abcd.json"):
        print("Test1: OK")
    else:
        print("Test1: NO")
    # Testing a file_name that end with .json
    if(get_file_name("abcd", "abcd.json") == "abcd/abcd.json"):
        print("Test2: OK")
    else:
        print("Test2: NO")


# Generated at 2022-06-13 18:39:27.413957
# Unit test for function get_file_name
def test_get_file_name():
    template_name = '{{ cookiecutter.repo_name }}'

    assert get_file_name('/tmp', 'bar') == '/tmp/bar.json'
    assert get_file_name('/tmp', 'bar.json') == '/tmp/bar.json'


# Generated at 2022-06-13 18:39:29.918491
# Unit test for function get_file_name
def test_get_file_name():
  assert get_file_name('/home/user/cookiecutter-replay/', 'test') == '/home/user/cookiecutter-replay/test.json'



# Generated at 2022-06-13 18:39:32.553894
# Unit test for function load
def test_load():
    test_context = cookiecutter.replay.load('replay/','ex_mako')
    assert isinstance(test_context,dict)
    assert isinstance(test_context['cookiecutter'],dict)

# Generated at 2022-06-13 18:39:34.746044
# Unit test for function dump
def test_dump():
    '''
    test function dump
    
    '''

# Generated at 2022-06-13 18:39:37.024902
# Unit test for function get_file_name
def test_get_file_name():
    assert get_file_name('testdir', 'testdir') == 'testdir/testdir.json'
    assert get_file_name('testdir', 'testdir.json') == 'testdir/testdir.json'


# Generated at 2022-06-13 18:39:44.389485
# Unit test for function get_file_name
def test_get_file_name():
    # Setup function get_file_name
    replay_dir = 'path/to/replay/dir'
    template_name = 'template_name'

    # Test assertion of get_file_name
    assert 'path/to/replay/dir/template_name.json' == get_file_name(replay_dir, template_name)

# Generated at 2022-06-13 18:39:55.435688
# Unit test for function dump
def test_dump():
    """Unit test function dump"""
    replay_dir = os.getcwd()
    template_name = 'test_template'
    context = {
        'cookiecutter': {
            'key1': 'value1',
            'key2': 'value2'
        }
    }

    dump(replay_dir, template_name, context)
    context_to_check = load(replay_dir, template_name)
    if context != context_to_check:
        print('[test_dump] Failed')
    else:
        print('[test_dump] Passed')


# Generated at 2022-06-13 18:40:01.718669
# Unit test for function dump
def test_dump():
    """
    Unit test for correct operation of function dump.
    """
    # Create a dictionary that can be dumped
    context = {'cookiecutter':
        {
            'sugar': 'white',
            'cream': 'peppermint',
            'options': {
                'finish': 'mint',
                'sprinkles': 'yes',
            },
        }
    }

    # Create a directory to dump the file
    replay_dir = '/tmp'

    # Create a template name
    template_name = "template_one"

    # Dump the dictionary
    dump(replay_dir=replay_dir, template_name=template_name, context=context)

    # Load the file
    context_loaded = load(replay_dir=replay_dir, template_name=template_name)

    # Assert

# Generated at 2022-06-13 18:40:02.573753
# Unit test for function load
def test_load():
    load('','galaxy-cookiecutter')

# Generated at 2022-06-13 18:40:10.693371
# Unit test for function dump
def test_dump():
    """Unit test for function dump."""
    # Sets test directory
    replay_dir = os.path.join(os.getcwd(), 'test', 'test_dump')
    # Gets the filepath to dump the replay
    replay_file = get_file_name(replay_dir, 'test')
    # The template name
    template_name = 'test'
    # The context as a dictionary
    context = {'cookiecutter': {'project_name': 'test'}}

    dump(replay_dir, template_name, context)
    from replay import load
    context_replayed = load(replay_dir, template_name)
    print(context_replayed)

if __name__ == '__main__':
    test_dump()

# Generated at 2022-06-13 18:40:16.975553
# Unit test for function load
def test_load():
    current_dir = os.getcwd()
    replay_dir = os.path.join(current_dir, 'test_data/replay')
    template_name = 'test_template'
    context = load(replay_dir, template_name)
    assert context['cookiecutter'] == {'test_key': 'test_value'}

if __name__ == '__main__':
    load(replay_dir, template_name)
    print('Unit test end')

# Generated at 2022-06-13 18:40:19.992332
# Unit test for function load
def test_load():
    """Test function load."""
    context = load(replay_dir='~/.cookiecutters/replay', template_name='replay')
    assert isinstance(context, dict)
    assert 'cookiecutter' in context


# Generated at 2022-06-13 18:40:26.504030
# Unit test for function dump
def test_dump():
    context = dict(cookiecutter={'_template': 'test', 'abc': 1, 'test': 'yes'})
    # dump a valid context
    try:
        dump('replay', 'test', context)
    except Exception:
        assert False
    # dump a non-dict context
    try:
        dump('replay', 'test', 2)
        assert False
    except TypeError:
        assert True
    except Exception:
        assert False
    # dump a non-str template name
    try:
        dump('replay', 2, context)
        assert False
    except TypeError:
        assert True
    except Exception:
        assert False
    # dump a context without cookiecutter key
    try:
        dump('replay', 'test', dict())
        assert False
    except ValueError:
        assert True
   

# Generated at 2022-06-13 18:40:33.714868
# Unit test for function load
def test_load():
    """Test the load function."""
    replay_dir = os.path.join('tests', 'files', 'download-tests', 'replay')
    template = os.path.join('tests', 'files', 'download-tests', 'context.json')
    context = load(replay_dir, template)
    assert context == {"cookiecutter": {"full_name": "Ana Balica", "email": "ana@example.com", "github_username": "anabalica"}}



# Generated at 2022-06-13 18:40:36.801648
# Unit test for function load
def test_load():
    replay_dir = ''
    replay_file = ''
    context = load(replay_dir, replay_file)

# Generated at 2022-06-13 18:40:46.344293
# Unit test for function load
def test_load():
    # Create mock context to be dumped
    replay_dir = "tests/fixtures/fake-repo-tmpl/{{cookiecutter.repo_name}}"
    template_name = "tests/fixtures/fake-repo-tmpl"

# Generated at 2022-06-13 18:40:50.222590
# Unit test for function dump
def test_dump():
    replay_dir = 'tests'
    template_name = 'test.json'
    context = {'cookiecutter': {'project_name': 'test'}}
    dump(replay_dir, template_name, context)

    replay_file = get_file_name(replay_dir, template_name)
    assert os.path.exists(replay_file)
    os.remove(replay_file)


# Generated at 2022-06-13 18:40:56.106068
# Unit test for function dump
def test_dump():
    replay_dir = 'tmp'
    template_name = 'test'
    context = {
        "cookiecutter": {
            "project_name": "Test Project Name"
        }
    }
    dump(replay_dir, template_name, context)
    assert 1 == 1


# Generated at 2022-06-13 18:40:59.670075
# Unit test for function load
def test_load():
    context = load('test_cookiecutter', 'foobar')
    assert 'cookiecutter' in context, "Context is required to contain a cookiecutter key"

# Generated at 2022-06-13 18:41:06.169681
# Unit test for function load
def test_load():
    print("\nUnit test for function load")
    replay_dir = '/tmp/cookiecutter_tests/replay'
    template_name = 'foobar'
    context = {
        'cookiecutter': {
            'full_name': "Audrey Roy",
            'email': 'audreyr@gmail.com',
            'project_name': 'cookiecutter-pypackage',
        }
    }

# Generated at 2022-06-13 18:41:08.441567
# Unit test for function load
def test_load():
    context = load('{{cookiecutter.replay_dir}}', '{{cookiecutter.template_name}}')
    for k, v in context.items():
        print('{}: {}'.format(k, v))


# Generated at 2022-06-13 18:41:12.482168
# Unit test for function dump
def test_dump():
    """Unit test for function dump."""
    replay_dir = 'tests/test-dump-dir/'
    template_name = 'test-dump-template'
    context = {'cookiecutter': {'key': 'value'}}
    dump(replay_dir, template_name, context)

    replay_file = get_file_name(replay_dir, template_name)
    with open(replay_file, 'r') as infile:
        json_data = json.load(infile)

    assert 'cookiecutter' in json_data
    assert json_data['cookiecutter']['key'] == 'value'


# Generated at 2022-06-13 18:41:18.534740
# Unit test for function dump
def test_dump():
    """Unit test for function dump"""

    # TODO: Add more detailed exception handling
    try:
        dump(None, None, None)
        assert False
    except Exception:
        assert True

    try:
        dump('replay/', None, None)
        assert False
    except Exception:
        assert True

    try:
        dump('replay/', 'test', None)
        assert False
    except Exception:
        assert True

    try:
        dump('replay/', 1, None)
        assert False
    except Exception:
        assert True

    try:
        dump('replay/', {}, None)
        assert False
    except Exception:
        assert True
    
    try:
        dump('replay/', 'test', 1)
        assert False
    except Exception:
        assert True


# Generated at 2022-06-13 18:41:22.110377
# Unit test for function load
def test_load():
    # print(load('/home/lily/hyper_gp/output/cookiecutter-example', 'example'))
    print(load('/home/lily/hyper_gp/output/cookiecutter-pymodule', 'pymodule'))

if __name__ == '__main__':
    test_load()

# Generated at 2022-06-13 18:41:24.899985
# Unit test for function dump
def test_dump():
    content = {"test": "test"}
    filename = "test.json"
    replay_dir = "../test/test_dir"
    dump(replay_dir, filename, content)
    load(replay_dir, filename)
    assert load(replay_dir, filename) == content
    os.remove(filename)

# Generated at 2022-06-13 18:41:29.794982
# Unit test for function dump
def test_dump():
    """Test dumping json data into file."""
    replay_dir = 'replay'
    template_name = 'swagger-php'
    context = {'cookiecutter': {'package': 'mugur'}}

    dump(replay_dir, template_name, context)
    context_loaded = load(replay_dir, template_name)
    assert context == context_loaded

# Generated at 2022-06-13 18:41:31.817005
# Unit test for function load
def test_load():
    if not isinstance(load("../testdata/", "test"), dict):
        raise RuntimeError("load function is not giving out a dict")



# Generated at 2022-06-13 18:41:38.417010
# Unit test for function load
def test_load():
    template_name = 'testtemplate'
    replay_dir = './'
    context = {'cookiecutter': {'testkey': 'testvalue'}}
    dump(replay_dir, template_name, context)
    loaded = load(replay_dir, template_name)
    assert(loaded == context)
    os.remove(get_file_name(replay_dir, template_name))

# Generated at 2022-06-13 18:41:45.185960
# Unit test for function load
def test_load():
    test_replay_dir = 'C:\\Users\\SMILISAL\\cookiecutter-data-science\\tests\\test-data\\'
    test_template_name = 'tox.ini'
    assert load(test_replay_dir, test_template_name) == {u'cookiecutter': {u'full_name': u'Salil Agrawal', u'email': u'salil.agrawal@synechron.com', u'github_username': u'salilagrawal'}}
    
    

# Generated at 2022-06-13 18:41:55.139294
# Unit test for function dump
def test_dump():
    replay_dir = './replay'
    template = './tests/fake-repo-pre/'
    filename = get_file_name(replay_dir, template)
    print(filename)

    context = {
        'project_name': 'TestProject',
        'author_name': 'Tester',
        'email': 'test@cookiecutter.io',
        'description': 'A short description of the project.',
        'domain_name': 'example.com',
        'version': '0.1.0',
        'open_source_license': 'MIT license',
        'python_version': '2.7',
        'cookiecutter': {
            'replay_dir': replay_dir,
            'no_input': True
        },
    }


# Generated at 2022-06-13 18:41:57.831164
# Unit test for function load
def test_load():
    template_name = 'cookiecutter-pypackage'
    path = 'tests/test-load'
    replay_dir = os.path.join(os.getcwd(), path)
    context = load(replay_dir, template_name)
    assert "cookiecutter" in context

# Generated at 2022-06-13 18:41:58.924750
# Unit test for function load
def test_load():
    context = load('./', 'test_load')
    assert(isinstance(context, dict))


# Generated at 2022-06-13 18:42:08.819127
# Unit test for function load
def test_load():
    """Test for load function."""
    # Get the current directory
    curdir = os.path.dirname(os.path.realpath(__file__))
    # File with valid json
    file_name_valid_json = 'test.json'
    # File with invalid json
    file_name_invalid_json = 'test_invalid.json'

    # Call load function with valid file name and directory
    context = load(curdir, file_name_valid_json)
    assert isinstance(context, dict), 'context should be of type dict'
    assert context['cookiecutter']['project_name'] == 'neo-cookiecutter-test', 'project_name should be neo-cookiecutter-test'

    # Call load function with invalid file name and directory

# Generated at 2022-06-13 18:42:17.090039
# Unit test for function load
def test_load():
    """Unit test for function load."""
    from cookiecutter import main
    import os
    import shutil

    original_dir = os.path.abspath(os.getcwd())
    replay_dir = os.path.join(original_dir, 'tests/test-replay')

    # Delete previous tests/test-replay directory
    if os.path.isdir(replay_dir):
        shutil.rmtree(replay_dir)

    # Create empty tests/test-replay directory
    os.mkdir(replay_dir)

    # Run cookiecutter on the tests/fake-repo-tmpl/ directory

# Generated at 2022-06-13 18:42:22.134386
# Unit test for function dump
def test_dump():
    test_dir = "/tmp/cookiecutter_test"
    template_name = "basic_django"
    test_dict = {"cookiecutter":{"replay_dir":"{{ cookiecutter.replay_dir }}", "full_name":"{{cookiecutter.full_name }}", "email":"{{ cookiecutter.email }}", "repo_name":"{{ cookiecutter.repo_name }}", "project_name":"{{ cookiecutter.repo_name }}", "project_slug":"{{ cookiecutter.repo_name }}", "version":"{{ cookiecutter.version }}"}, "other":"value"}
    dump(test_dir, template_name, test_dict)
    file_name = get_file_name(test_dir, template_name)

# Generated at 2022-06-13 18:42:30.726764
# Unit test for function load
def test_load():
    input = {"cookiecutter": {"project_name": "test_load", "full_name": "test_load", "email": "test_load", "description": "test_load", "version": "test_load", "domain_name": "test_load", "timezone": "test_load", "python_version": "test_load"}}
    replay_dir = "/home/jaideep/code/cookiecutter-new/tests/test_replay"
    template_name = "simple"
    actual = load(replay_dir, template_name)
    try:
        assert(actual==input)
        print("SUCCESS: test_load function, test_replay package")
    except:
        print("FAILED: test_load function, test_replay package")



# Generated at 2022-06-13 18:42:38.511881
# Unit test for function load
def test_load():
    dir = '/Users/lohitjaiswal/Desktop'
    template_name = 'template1'
    context = {}
    

# Generated at 2022-06-13 18:42:57.172085
# Unit test for function load
def test_load():
    replay_file_name = 'tests/test-data/fake-replay/fake-repo.json'
    replay_dict = load('tests/test-data/fake-replay', 'fake-repo')

# Generated at 2022-06-13 18:43:03.092789
# Unit test for function dump
def test_dump():
    context = dict(cookiecutter={'test': 'test'})
    dump('.cookiecutters', 'test', context)

    with open('.cookiecutters/test.json') as infile:
        assert json.load(infile) == context

    os.remove('.cookiecutters/test.json')
    os.rmdir('.cookiecutters')


# Generated at 2022-06-13 18:43:08.305928
# Unit test for function load
def test_load():
    replay_dir = 'replay'
    template_name = 'myreplay1'
    context = {'cookiecutter': {'full_name': 'John Doe',
                                'email': 'john@example.com'}}
    
    dump(replay_dir, template_name, context)
    context_loaded = load(replay_dir, template_name)
    print (context_loaded['cookiecutter'])

# Generated at 2022-06-13 18:43:18.653299
# Unit test for function dump
def test_dump():
    """Unit test for replay.dump"""
    import string
    import random
    import shutil

    test_dict = {
        'cookiecutter': {
            'project_name': 'Test Project',
            'repo_name': 'test_project',
        }
    }

    template_name = ''.join([random.choice(string.ascii_letters) for n in range(10)])  # noqa
    replay_dir = '/tmp/cookiecutter_replay_test'

    dump(replay_dir, template_name, test_dict)

    result = load(replay_dir, template_name)

    assert result == test_dict

    shutil.rmtree(replay_dir)



# Generated at 2022-06-13 18:43:28.523398
# Unit test for function load

# Generated at 2022-06-13 18:43:40.693220
# Unit test for function dump
def test_dump():
    import shutil


# Generated at 2022-06-13 18:43:46.543062
# Unit test for function load
def test_load():
    """Unit test for function load"""
    replay_dir = 'replay'
    template_name = 'template_name'
    answer = {u'cookiecutter': {u'full_name': u'full_name'}, u'first_context': u'first_context'}
    replay_file = get_file_name(replay_dir, template_name)
    with open(replay_file, 'r') as infile:
        context = json.load(infile)

    assert context == answer

# Generated at 2022-06-13 18:43:51.823393
# Unit test for function load
def test_load():
    replay_dir = os.path.join(os.getcwd(), 'cookiecutter')
    template_name = 'hello_world'
    context = load(replay_dir, template_name)
    assert 'cookiecutter' in context


# Generated at 2022-06-13 18:43:58.774826
# Unit test for function dump
def test_dump():
    replay_dir = os.path.expanduser('~/.cookiecutter_replay')
    if not os.path.exists(replay_dir):
        os.mkdir(replay_dir)
    template_name = 'test'
    json_file = "{}/{}".format(replay_dir, template_name)
    dump(replay_dir, template_name, {'test_key': 'test_value', 'test_key2': 'test_value2'})
    with open(json_file, 'r') as f:
        assert f.read() == '{\n  "test_key": "test_value", \n  "test_key2": "test_value2"\n}'

# Generated at 2022-06-13 18:44:02.493666
# Unit test for function dump
def test_dump():
    replay_dir = '.cookiecutters'
    template_name = 'base.json'
    expected_result = replay_dir+'/base.json'
    assert(get_file_name(replay_dir, template_name)==expected_result)


# Generated at 2022-06-13 18:44:09.459320
# Unit test for function load
def test_load():
    assert load('replay', 'cookiecutter') == {"cookiecutter": {"name": "My Project"}}


# Generated at 2022-06-13 18:44:14.349344
# Unit test for function dump
def test_dump():
    replay_dir = os.path.join(os.getcwd(), 'my-replay-folder')
    make_sure_path_exists(replay_dir)
    template_name = 'cookiecutter-pypackage'

# Generated at 2022-06-13 18:44:23.329159
# Unit test for function load
def test_load():
    import sys
    from cookiecutter.main import cookiecutter, DIR_DEFAULT_CONFIG
    from cookiecutter import utils
    template_path = os.path.join(utils.root_project_dir(), '{{ cookiecutter.repo_name }}', '{{ cookiecutter.base_path }}')
    # Load default config
    sys.argv = ['cookiecutter', template_path]
    try:
        config_file = os.path.join(DIR_DEFAULT_CONFIG, 'cookiecutter.yaml')
        with open(config_file) as file_handle:
            config = utils.load_yaml(file_handle.read())
    except IOError:
        config = {}

# Generated at 2022-06-13 18:44:28.436405
# Unit test for function load
def test_load():
    if not os.path.exists('/tmp/replay'):
        os.makedirs('/tmp/replay' )
        with open('/tmp/replay/cookies.json', 'w') as f:
            json.dump({'cookiecutter':{'project_name': 'cookie'}}, f)

# Generated at 2022-06-13 18:44:31.416360
# Unit test for function load
def test_load():
    """Unit test for function load"""
    template = load(os.path.expanduser("~/.cookiecutter_replay"), 'cookiecutter-pypackage')
    
if __name__ == '__main__':
    # test_load()
    pass

# Generated at 2022-06-13 18:44:41.093190
# Unit test for function dump
def test_dump():
    replay_dir = os.path.join(
        os.path.dirname(__file__), "tests/test-replay/"
    )

    if os.path.exists(replay_dir):
        print("Deleting old test-replay folder")
        import shutil
        shutil.rmtree(replay_dir)

    os.makedirs(replay_dir)

    template_name = "test_dump.json"
    test_context = {
        "cookiecutter": {
            "full_name": "Your Name",
            "email": "your.email@domain.com",
            "project_name": "Your Project Name",
        }
    }

    dump(replay_dir, template_name, test_context)

# Generated at 2022-06-13 18:44:45.603894
# Unit test for function load
def test_load():
    """Unit test for the function load."""
    try:
        load(replay_dir='/home/hongbin/Github/cookiecutter', template_name='tests')
        'We should have an exception'
        assert False
    except ValueError:
        assert True



# Generated at 2022-06-13 18:44:57.453443
# Unit test for function load
def test_load():
    """Test for load function."""
    from cookiecutter import replay
    replay_dir = os.path.join(os.getcwd(), 'tests/test-load-dir/')
    template_name = 'my_template'
    context = {
        "cookiecutter": {
            "version": "0.8.0",
            "project_name": "Project Name",
            "project_slug": "project_slug",
        }
    }
    replay.dump(replay_dir, template_name, context)
    loaded_context = replay.load(replay_dir, template_name)
    assert loaded_context == context

# Generated at 2022-06-13 18:44:59.514666
# Unit test for function load
def test_load():
    res = load('/home/taochengwei/git/Cookiecutter_test/tests/test-replay', 'test_json')
    print(res)


# Generated at 2022-06-13 18:45:03.709621
# Unit test for function dump

# Generated at 2022-06-13 18:45:15.505668
# Unit test for function load
def test_load():
    assert load(replay_dir="../tests/",template_name="test_replay") is not None

# Generated at 2022-06-13 18:45:25.305879
# Unit test for function load
def test_load():
    template_name = 'test_template'
    # mock_context = {
    #     'cookiecutter': {
    #         'project_name': 'My Project',
    #         'project_slug': 'my_project',
    #         '_copy_without_render': [],
    #         '_template': '/tmp/test_template'
    #     }
    # }
    expected_context = {
        'cookiecutter': {
            'project_name': 'My Project',
            'project_slug': 'my_project',
            '_copy_without_render': ['test_unrendered_file'],
            '_template': '/tmp/test_template'
        }
    }
    template_path = '/tmp/test_template'

# Generated at 2022-06-13 18:45:28.113579
# Unit test for function load
def test_load():
    """Unit test for function load"""
    context = load('/Users/kumar/Lab/cookiecutter', 'default')
    assert context['cookiecutter']['project_name'] == 'default'

# Generated at 2022-06-13 18:45:34.041792
# Unit test for function dump
def test_dump():
    ''' Test for the dump function'''

    # Test for dumping data
    replay_dir = 'replay_dir'
    make_sure_path_exists(replay_dir)

    template_name = 'template.json'
    data = {'cookiecutter': 'cookie'}

    dump(replay_dir, template_name, data)

    assert os.path.exists(os.path.join(replay_dir, template_name))



# Generated at 2022-06-13 18:45:36.761595
# Unit test for function load
def test_load():
    """Test load"""
    context = load('/home/jdkim/.cookiecutter_replay', 'biolab/python-project')
    print(context)



# Generated at 2022-06-13 18:45:44.991105
# Unit test for function load
def test_load():
    replay_file = get_file_name('/Users/thomashui/Dev/cookiecutter/cookiecutter-pypackage/replay', 'cookiecutter-pypackage')

    with open(replay_file, 'r') as infile:
        context = json.load(infile)

    if 'cookiecutter' not in context:
        raise ValueError('Context is required to contain a cookiecutter key')

    return context


# Generated at 2022-06-13 18:45:49.439124
# Unit test for function load
def test_load():
    # Test context is required to contain a cookiecutter key
    try:
        context = load('', '')
    except ValueError:
        context = None
    assert context == None

    # Test template name is required to be of type str
    try:
        context = load('', 123)
    except TypeError:
        context = None
    assert context == None

    # Test context is required to be of type dict
    try:
        context = load('replay', 'my_template')
    except TypeError:
        context = None
    assert context == None
        


# Generated at 2022-06-13 18:45:53.881306
# Unit test for function load
def test_load():
    context = load('/Users/shengyu/project/replay', 'cookiecutter-pypackage')
    assert context is not None
    assert context['Cookiecutter']['project_name'] == 'Cookiecutter pypackage'



# Generated at 2022-06-13 18:45:59.675296
# Unit test for function load
def test_load():
    """Unit test for function load."""
    replay_dir = os.path.join(os.path.expanduser("~"), '.cookiecutter-replay')
    template_name = 'my-template'
    context = {'cookiecutter': {'full_name': 'Your name'}}
    dump(replay_dir, template_name, context)

    replay_context = load(replay_dir, template_name)
    assert replay_context == context

    # Remove replay file
    os.remove(get_file_name(replay_dir, template_name))


# Generated at 2022-06-13 18:46:04.405788
# Unit test for function load
def test_load():
    """Load the `replay_file` as a dict."""
    test_replay_file = 'C:\\Users\\Lenovo\\AppData\\Local\\cookiecutters\\cookiecutter-pypackage'
    replay_file = get_file_name(test_replay_file, 'cookiecutter-pypackage')
    with open(replay_file, 'r') as infile:
        context = json.load(infile)
    print(context)
    #from pprint import pprint
    #pprint(context)


# Generated at 2022-06-13 18:46:33.982406
# Unit test for function load
def test_load():
    replay_dir = 'test'
    template_name = 'test'
    context = {'cookiecutter': {'test': 'test'}}
    dump(replay_dir, template_name, context)
    lcontext = load(replay_dir, template_name)
    assert lcontext == context
    os.remove('{}/{}'.format(replay_dir, template_name))



# Generated at 2022-06-13 18:46:37.698926
# Unit test for function load
def test_load():
    template_name = 'cookiecutter.json'
    replay_dir = os.path.join('tests', 'test-load')
    replay_file = get_file_name(replay_dir, template_name)

    context = load(replay_dir, template_name)
    assert context == {}


# Generated at 2022-06-13 18:46:44.403561
# Unit test for function load
def test_load():
    """Test load."""
    # Call load
    context = load('./test/test_replay', 'test')

# Generated at 2022-06-13 18:46:49.527611
# Unit test for function dump
def test_dump():
    replay_dir = 'tests/test-output/replay'
    template_name = 'cookiecutter-pypackage'

# Generated at 2022-06-13 18:46:52.437892
# Unit test for function load
def test_load():
    """Test load function."""
    context = load('scaffold-replay/', 'tem.json')
    print(context)



# Generated at 2022-06-13 18:46:55.991588
# Unit test for function load
def test_load():
    replay_dir = os.getcwd()
    template_name = 'pokemaster'

    context = load(replay_dir, template_name)
    print(context)

if __name__ == '__main__':
    test_load()

# Generated at 2022-06-13 18:47:00.149036
# Unit test for function dump
def test_dump():
  context = {
    "cookiecutter": {
      "company": "ACME",
      "project_name": "Foo Bar",
      "project_slug": "foo-bar",
      "package_name": "foo_bar"
    }
  }
  dump('.', 'foo-bar', context)
  assert load('.', 'foo-bar') == context


# Generated at 2022-06-13 18:47:01.366577
# Unit test for function load
def test_load():
    replay = load('.', 'cookiecutter-pypackage')
    return replay


# Generated at 2022-06-13 18:47:06.877521
# Unit test for function load
def test_load():
    """Unit test for function load."""
    from cookiecutter.main import cookiecutter
    from cookiecutter import utils
    import os
    import shutil

    template_dir = 'tests/test-templates/generate-project-name'
    replay_dir = utils.make_generate_dir('replay')

    cookiecutter(template_dir, replay_dir=replay_dir)

    replay_file = os.path.join(replay_dir, 'generate-project-name.json')
    assert os.path.exists(replay_file)

    context = load(replay_dir, 'generate-project-name')
    assert context

    shutil.rmtree(replay_dir)



# Generated at 2022-06-13 18:47:13.178132
# Unit test for function load
def test_load():
    replay_dir = 'tests/files/replay_dir'
    template_name = 'greeting'
    dump(replay_dir, template_name, {'cookiecutter': {'answer': 'world'}})
    context = load(replay_dir, template_name)
    assert context['cookiecutter']['answer'] == 'world'

# Generated at 2022-06-13 18:48:08.637527
# Unit test for function load
def test_load():
    """unit test for function load"""
    replay_dir = "/home/lucas/Desktop/cookiecutter-testing"
    template_name = "test-replay"
    test_context = {
        'cookiecutter': {
            'full_name': 'Lucas Tunesi',
            'email': 'lucas.tunesi@gmail.com',
            'project_name': 'best project ever'
        }
    }
    dump(replay_dir, template_name, test_context)
    actual_context = load(replay_dir, template_name)
    assert test_context == actual_context
    
if __name__ == "__main__":
    test_load()