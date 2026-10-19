

# Generated at 2022-06-13 18:38:24.576614
# Unit test for function load
def test_load():
    '''
    test_load
    '''
    # Unit test for function load
    def test_load(self):
        '''
        test_load
        '''
        self.replay_dir = '/home/daniel/Downloads/cookiecutter/build/tmp/cookiecutter-example-project-0.1.0/cookiecutter'
        self.template_name = 'cookiecutter.json'
        self.outfile = get_file_name(replay_dir, template_name)
        context = get_file_name(replay_dir, template_name)
        self.assertEqual(context, context)
        return context



# Generated at 2022-06-13 18:38:28.447459
# Unit test for function get_file_name
def test_get_file_name():
    file_name = 'demo'
    template_name = 'demo'
    replay_dir = 'C:/Users/Yongyu/CookiecutterDemo'
    out = get_file_name(replay_dir, template_name)
    assert out == file_name



# Generated at 2022-06-13 18:38:29.649718
# Unit test for function load
def test_load():
    assert 0 == load("/tmp", "test.json")


# Generated at 2022-06-13 18:38:31.994344
# Unit test for function load
def test_load():
    replay_dir = 'C:/Users/zhengyang.song/Documents/replay1'
    template_name = 'tmp'
    context = load(replay_dir, template_name)
    return context

# Generated at 2022-06-13 18:38:35.491773
# Unit test for function load
def test_load():
    replay_dir = os.path.join(
        os.path.dirname(__file__),
        '..',
        '..',
        'tests',
        'test-replay'
    )
    template_name = "foo"
    context = load(replay_dir, template_name)
    assert context['cookiecutter']['repo_dir'] == '.'


# Generated at 2022-06-13 18:38:45.697799
# Unit test for function dump
def test_dump():
    """Unit test for function dump."""
    # Function dump should raise a TypeError if replay_dir is not of type str
    try:
        dump(None, None, None)
    except TypeError:
        pass
    else:
        raise AssertionError('Function dump should raise a TypeError'
            ' if replay_dir is not of type str')

    # Function dump should raise a TypeError if template_name is not of type str
    try:
        dump('replay', None, None)
    except TypeError:
        pass
    else:
        raise AssertionError('Function dump should raise a TypeError'
            ' if template_name is not of type str')

    # Function dump should raise a TypeError if context is not of type dict

# Generated at 2022-06-13 18:38:50.628054
# Unit test for function load
def test_load():
    dir_ = os.path.join(os.getcwd(), 'tests/test-replay')
    expected = {
        'cookiecutter': {
            'full_name': 'Audrey Roy',
            'email': 'audreyr@example.com',
            'project_name': 'test-replay',
            'project_slug': 'test_replay',
        }
    }
    context = load(dir_, 'test-replay')
    assert context == expected


# Generated at 2022-06-13 18:38:57.896433
# Unit test for function dump
def test_dump():
    template_name = 'alok_prajapati'
    replay_dir = '/home/alok/Documents/cookiecutter/cookiecutter/tests/test-replay'
    context = {'cookiecutter': {'first_name': 'Alok', 'last_name': 'Prajapati', 'email': 'alok@gmail.com'}}
    dump(replay_dir, template_name, context)


# Generated at 2022-06-13 18:39:00.310639
# Unit test for function load
def test_load():
    """ Unit test for function load """

    load("replay/", "add2")

# Generated at 2022-06-13 18:39:02.467164
# Unit test for function load
def test_load():
    assert load("replay", "mytemplate") == {"cookiecutter": "mytemplate", "name": "myproject"}

# Generated at 2022-06-13 18:39:09.990920
# Unit test for function load
def test_load():
    replay_dir= 'replay_dir'
    template_name= 'template_name'
    expected_context= {'cookiecutter': 'test_cookiecutter'}
    dump(replay_dir, template_name, expected_context)
    actual_context= load(replay_dir, template_name)
    assert actual_context == expected_context


# Generated at 2022-06-13 18:39:15.164049
# Unit test for function load
def test_load():
    context = load("./tests/testrep", "testrep")
    assert type(context) is dict # check that function returns dictionary
    assert context["cookiecutter"]["project_slug"] == "testrep"
    assert type(context["cookiecutter"]["_template"]) is str
    assert type(context["cookiecutter"]["project_name"]) is str
    assert type(context["cookiecutter"]["owner_name"]) is str
    assert type(context["cookiecutter"]["author_name"]) is str
    assert type(context["cookiecutter"]["email"]) is str
    assert type(context["cookiecutter"]["description"]) is str
    assert type(context["cookiecutter"]["domain_name"]) is str

# Generated at 2022-06-13 18:39:18.572718
# Unit test for function load
def test_load():
    # Load the context
    context = load('tests/test-repo', 'example-repo')
    
    # Check if the context dictionary contains the key 'cookiecutter'
    assert 'cookiecutter' in context


# Generated at 2022-06-13 18:39:26.078839
# Unit test for function dump
def test_dump():
    import json
    import os
    import shutil

    path = 'Test'
    template = 'Test'
    context = {'cookiecutter': {'hello': 'world'}}
    dump('Test', 'Test', context)
    filename = get_file_name(path, template)
    assert os.path.exists(path)
    with open(filename) as f:
        json_data = json.load(f)
        for key in context:
            assert key in json_data
        for key in json_data:
            assert key in context
    shutil.rmtree(path)



# Generated at 2022-06-13 18:39:32.889278
# Unit test for function load
def test_load():
    """Unit test for function load."""

    # Test invalid template name type
    try:
        load(replay_dir='test/test_data', template_name=None)
        assert False
    except TypeError:
        assert True
    except Exception:
        assert False

    # Test invalid template
    try:
        load(replay_dir='test/test_data', template_name='Invalid')
        assert False
    except IOError:
        assert True
    except Exception:
        assert False

    # Test valid template

# Generated at 2022-06-13 18:39:40.688851
# Unit test for function load
def test_load():
    context = load('/Users/Stella/Desktop/privacy_attestation/cookiecutter/tests', 'test_template')
    print(context)
    assert(context['cookiecutter']['full_name'] == 'Audrey Roy Greenfeld')
    assert(context['cookiecutter']['email'] == 'audreyr@example.com')
    assert(context['cookiecutter']['github_username'] == 'audreyr')
    assert(context['cookiecutter']['project_name'] == 'Cookiecutter-Pylibrary')
    assert(context['cookiecutter']['project_slug'] == 'cookiecutter-pylibrary')
    assert(context['cookiecutter']['project_short_description'] == 'A Python library project')

# Generated at 2022-06-13 18:39:55.543175
# Unit test for function load
def test_load():
    import cookiecutter.main
    import tempfile

    template = 'https://github.com/audreyr/cookiecutter-pypackage.git'
    replay_dir = tempfile.mkdtemp()
    context = {
        'full_name': 'Test Testerson',
        'email': 'test@example.com',
        'github_username': 'audreyr',
        'cookiecutter': {
            'full_name': 'Test Testerson',
            'email': 'test@example.com',
            'github_username': 'audreyr',
            'replay': 'y'
        }
    }
    # First run
    cookiecutter.main.cookiecutter(template, replay_dir=replay_dir, no_input=True)

    # Analysis
    # tmp_dir = '/

# Generated at 2022-06-13 18:40:01.390685
# Unit test for function load
def test_load():
    from cookiecutter.main import cookiecutter
    from cookiecutter import replay
    from cookiecutter.utils import rmtree
    from cookiecutter.config import get_user_config, USER_CONFIG_PATH
    import os

    # create user config for test
    test_config_dict = {
        "cookiecutters_dir": "/Users/hongkui/.cookiecutters",
        "replay_dir": "/Users/hongkui/.cookiecutters/replay"
    }
    if os.path.exists(USER_CONFIG_PATH):
        os.remove(USER_CONFIG_PATH)
    with open(USER_CONFIG_PATH, 'w') as user_config_file:
        json.dump(test_config_dict, user_config_file, indent=4)

    cookiecut

# Generated at 2022-06-13 18:40:10.373532
# Unit test for function load
def test_load():
    # Test with no context cookiecutter key
    replay_dir = "test_replay_dir"
    template_name = "test_template_name"
    with open('test.json', 'w') as outfile:
        json.dump({'not_cookiecutter': 'test'}, outfile, indent=2)
    try:
        load(replay_dir, template_name)
    except ValueError as e:
        print(e)
    else:
        assert False

    # Test with correct context
    with open('test.json', 'w') as outfile:
        json.dump({'cookiecutter': 'test'}, outfile, indent=2)
    try:
        load(replay_dir, template_name)
    except ValueError as e:
        print(e)
        assert False

# Generated at 2022-06-13 18:40:13.375320
# Unit test for function load
def test_load():
    load_test = load("/home/wangyu/", "test")
    print(load_test)
    
    
if __name__ == '__main__':
    test_load()

# Generated at 2022-06-13 18:40:22.766561
# Unit test for function dump

# Generated at 2022-06-13 18:40:25.585326
# Unit test for function load
def test_load():
    print("test_load:")
    replay_dir = os.path.join(os.path.dirname(__file__), os.pardir, 'replay')
    template_name = 'cookiecutter-pypackage'
    context = load(replay_dir, template_name)
    assert context is not None


# Generated at 2022-06-13 18:40:37.107710
# Unit test for function dump
def test_dump():
    """Test for dump function."""
    import tempfile
    from cookiecutter import main
    from cookiecutter.main import cookiecutter
    import os
    import shutil
    import json

    replay_dir = tempfile.mkdtemp()

# Generated at 2022-06-13 18:40:46.436976
# Unit test for function load
def test_load():
    replay_dir = "~/Desktop/cedar10/cookiecutter-cedar/tests/test-load"
    template_name = "~/Desktop/cedar10/cookiecutter-cedar/tests/test-load/test.json"
    context = {"cookiecutter": {"full_name": "kevin-roche", "email": "kevin-roche@hotmail.com"}}
    if not make_sure_path_exists(replay_dir):
        raise IOError('Unable to create replay dir at {}'.format(replay_dir))

    if not isinstance(template_name, str):
        raise TypeError('Template name is required to be of type str')

    if not isinstance(context, dict):
        raise TypeError('Context is required to be of type dict')


# Generated at 2022-06-13 18:40:51.883166
# Unit test for function dump
def test_dump():
    global replay_file
    template_name = 'test'
    replay_file = get_file_name('replays', template_name)
    if os.path.exists(replay_file):
        os.remove(replay_file)
    context = {'cookiecutter': {}}
    dump('replays', template_name, context)
    assert context == load('replays', template_name)
    os.remove(replay_file)

# Generated at 2022-06-13 18:40:54.248706
# Unit test for function load
def test_load():
    assert load('~/cookiecutter-pypackage', 'foobar') == None
    print('Passed unit test for function load!')


# Generated at 2022-06-13 18:40:58.106657
# Unit test for function load
def test_load():
    replay_dir = os.path.join('tests', 'test-load-replay')
    template_name = 'test_load'
    context = load(replay_dir, template_name)
    assert 'cookiecutter' in context
    assert context['cookiecutter'] == {'full_name': 'test_load', 'email': 'test@test.com'}


# Generated at 2022-06-13 18:41:00.292826
# Unit test for function load
def test_load():
    template_name = 'name'
    context = {'cookiecutter' : {'test': 'name'}}
    load(None, template_name)

# Generated at 2022-06-13 18:41:03.478442
# Unit test for function load
def test_load():
    """Unit test function."""
    context = load('./tests/files/fake-replay-dir', 'fake-repo')
    assert context == {u'cookiecutter': {u'pypackage_name': u'pytest', u'pypackage_version': u'1.1.0'}}




# Generated at 2022-06-13 18:41:06.358005
# Unit test for function load
def test_load():
    template_name = "cookiecutter-pypackage"
    replay_dir = "c:/code/cookiecutter-replay/"
    context = load(replay_dir, template_name)
    assert search("cookiecutter",context)

# Generated at 2022-06-13 18:41:12.124890
# Unit test for function load
def test_load():
    template_name = 'cookiecutter-pypackage'
    replay_dir = '/home/vagrant/.cookiecutter/replay/'
    replay_file = get_file_name(replay_dir, template_name)
    context = load(replay_dir, template_name)
    assert replay_file == '/home/vagrant/.cookiecutter/replay/cookiecutter-pypackage.json'
    assert context['cookiecutter']['author_email'] == 'vagrant@example.com'
    assert context['cookiecutter']['repo_name'] == 'test-cookiecutter-pypackage'


# Generated at 2022-06-13 18:41:14.306840
# Unit test for function load
def test_load():
    replay_dir = '.'
    template_name = 'new_project'
    context = load(replay_dir, template_name)
    assert 'cookiecutter' in context
    assert isinstance(context['cookiecutter'], dict)


# Generated at 2022-06-13 18:41:18.977158
# Unit test for function load
def test_load():
  context = load("C:/Users/qxu/git/cookiecutter-opencv-python-travis/{{cookiecutter.repo_name}}", "{{cookiecutter.repo_name}}")
  for key in context:
    print("{} is {}".format(key, context[key]))
    
    

# Generated at 2022-06-13 18:41:21.548938
# Unit test for function load

# Generated at 2022-06-13 18:41:23.852438
# Unit test for function load
def test_load():
    context = load(os.path.expanduser('~/.cookiecutters/cookiecutter-pypackage'), 'cookiecutter-pypackage')
    print(context)

# Generated at 2022-06-13 18:41:34.132208
# Unit test for function load
def test_load():
    """Unit test for load."""
    replay_dir = './'
    template_name = 'cookiecutter-pypackage'

    if not os.path.exists(get_file_name(replay_dir, template_name)):
        replay_dir_alt = '../'
        assert os.path.exists(get_file_name(replay_dir_alt, template_name))
        replay_dir = replay_dir_alt

    context = load(replay_dir, template_name)
    cookiecutter = context['cookiecutter']
    assert isinstance(cookiecutter, dict)


# Generated at 2022-06-13 18:41:41.723629
# Unit test for function load
def test_load():
    """Test for load"""
    replay_file = './examples/simple-example/.cookiecutters/cookiecutter-pypackage/cookiecutter.json'
    with open(replay_file, 'r') as infile:
        context = json.load(infile)

# Generated at 2022-06-13 18:41:47.786512
# Unit test for function dump
def test_dump():
    import os.path
    import sys
    import tempfile
    temp_file = tempfile.mkstemp()[1]
    context = {'cookiecutter': {'replay': 'hello'}}
    dump(temp_file, 'hello', context)
    file_path = os.path.join(temp_file, 'hello.json')
    with open(file_path, 'r') as infile:
        str_json = infile.read()
    assert str_json =='{\n  "cookiecutter": {\n    "replay": "hello"\n  }\n}'

# Generated at 2022-06-13 18:41:53.084512
# Unit test for function load
def test_load():
    """Run unit tests for function load."""
    try:
        load('something', 123)
    except Exception as e:
        assert e.args[0] == 'Template name is required to be of type str'
    try:
        load('something', 'hello')
    except Exception as e:
        assert e.args[0] == 'Context is required to contain a cookiecutter key'

# Generated at 2022-06-13 18:41:55.189610
# Unit test for function load
def test_load():
    context = load('tests/tests/replay', 'tests/tests/replay/example')
    assert context is not None
    assert 'cookiecutter' in context
    assert context['cookiecutter']['full_name'] == 'Audrey Roy'
    assert context['cookiecutter']['project_name'] == 'example'


# Generated at 2022-06-13 18:42:01.651486
# Unit test for function dump
def test_dump():
    replay_dir = '../tests/test-replay'
    template_name = 'test1'
    context = {'cookiecutter': {'key1': 'value1','key2': 'value2'}}
    
    if os.path.exists(replay_dir):
        shutil.rmtree(replay_dir)
    os.makedirs(replay_dir)
    
    try:
        dump(replay_dir, template_name, context)
    except IOError as e:
        print(e)
    except TypeError as e:
        print(e)
    
    

# Generated at 2022-06-13 18:42:10.931827
# Unit test for function dump
def test_dump():
    context = {'cookiecutter': {'full_name': 'Test User',
                                'email': 'test@example.com',
                                'github_username': 'test',
                                'project_name': 'Test project',
                                'project_slug': 'test-project',
                                'project_short_description': 'Dummy project',
                                'pypi_username': 'test',
                                'release_date': '19/02/2017',
                                'version': '0.1.0',
                                'year': '2017'}}

    try:
        dump('tests/test-replay', 'test-template', context)
    except:
        assert False
    else:
        assert True

    # Ensure that directories are created if they are missing

# Generated at 2022-06-13 18:42:16.206961
# Unit test for function load
def test_load():
    assert isinstance(load('/Users/tdhite/src/cookiecutter-template-project/cookiecutter-template-project', 'cookiecutter.json'), dict)
    assert isinstance(load('/Users/tdhite/src/cookiecutter-template-project/cookiecutter-template-project', 'cookiecutter.json')['cookiecutter'], dict)
    assert 'cookiecutter' in load('/Users/tdhite/src/cookiecutter-template-project/cookiecutter-template-project', 'cookiecutter.json')


# Generated at 2022-06-13 18:42:18.738520
# Unit test for function load
def test_load():
    """Test load function."""
    tests = {
        "test1": "Test 1",
        "test2": "Test 2",
        "test3": "Test 3",
    }

    assert tests == load('/Users/ptp/.cookiecutters/replay', 'cookiecutters')



# Generated at 2022-06-13 18:42:23.468446
# Unit test for function load
def test_load():
    assert(load('tests/test-data/test-replay', 'test-replay-load') ==
           {'cookiecutter': {'full_name': 'Test Load',
                             'email': 'load@example.com',
                             'github_username': 'load'}})



# Generated at 2022-06-13 18:42:26.578210
# Unit test for function load
def test_load():
    r_d = 'C:/Users/Sobong/Desktop/cookiecutter/my-new-project-master/'
    template_name = 'my-project-master'
    context = load(r_d, template_name)
    print(context)


# Generated at 2022-06-13 18:42:29.709674
# Unit test for function load
def test_load():
    template_name = 'test'
    context = {'cookiecutter': {'test': 'test'}}
    replay_dir = './test'
    dump(replay_dir, template_name, context)
    load(replay_dir, template_name)

# Generated at 2022-06-13 18:42:31.084596
# Unit test for function load
def test_load():
    replay_dir = "../templates"
    template_name = "Python-package-example-1"
    context = load(replay_dir, template_name)
    print(context)


# Generated at 2022-06-13 18:42:33.495267
# Unit test for function load
def test_load():
    template_name = 'test'
    replay_dir = 'replay'
    context = {'cookiecutter':{'test':'test'}}
    dump(replay_dir, template_name, context)
    result = load(replay_dir, template_name)
    assert result.get('cookiecutter' , None) == {'test':'test'}

# Generated at 2022-06-13 18:42:39.709204
# Unit test for function load
def test_load():
    template_name = 'robotframework'
    replay_dir = '.'
    replay_file = 'robotframework.json'
    context = load(replay_dir, template_name)
    assert context['name'] == 'robotframework'
    assert context['description'] == 'robotframework'
    assert context['author_name'] == 'Tosin Damilare James Animashaun'
    assert context['email'] == 'test@test.test'
    assert context['github_username'] == 'tosindamilare'
    assert context['open_source_license'] == 'tosindamilare'


# Generated at 2022-06-13 18:42:55.627145
# Unit test for function load
def test_load():
    """Unit test for function load."""
    replay_dir = "/home/david/code/cookiecutter"
    template_name = "cookiecutter-pypackage"
    
# test 1
    real_context = load(replay_dir, template_name)
    assert isinstance(real_context, dict)

# test 2
    try:
        real_context = load(replay_dir, 1)
    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)
    else:
        raise AssertionError
    
# test 3
    not_cookiecutter_context = {'not_cookiecutter': '1'}

# Generated at 2022-06-13 18:42:59.363435
# Unit test for function dump
def test_dump():
    template_name = 'test'
    replay_dir = 'C:\\Users\\i042416\\Documents\\GitHub\\cookiecutter-pylibrary'
    dump(replay_dir, template_name, {'cookiecutter': {'project_name': 'cookiecutter-pylibrary', '_template': 'test'}})

#Unit test for function load

# Generated at 2022-06-13 18:43:04.886123
# Unit test for function load
def test_load():
    # Test exception with load
    # load({}, template_name)
    # load(replay_dir, {})
    # load(replay_dir=None, template_name=None)
    # load(replay_dir, template_name) template_name does not exist
    # load(replay_dir, template_name) replay_dir does not exist
    pass

# Generated at 2022-06-13 18:43:09.941560
# Unit test for function load
def test_load():
    replay_dir = 'tests/test-replay-files'
    template_name = 'test_project_replay'
    replay_file = get_file_name(replay_dir, template_name)
    with open(replay_file, 'r') as infile:
        context = json.load(infile)
    print(context)
    print(context['cookiecutter']['project_name'])

if __name__ == '__main__':
    test_load()

# Generated at 2022-06-13 18:43:14.452968
# Unit test for function load
def test_load():
    """Unit test for function load."""
    assert isinstance(re.load('.', 'cookiecutter-pypackage'), dict)


"""
cookiecutter.replay.dump.

-----------------------
"""

"""
cookiecutter.replay.load.

-----------------------
"""

# Generated at 2022-06-13 18:43:23.360003
# Unit test for function dump
def test_dump():
    testdic = {}
    testdic['cookiecutter'] = {}
    testdic['cookiecutter']['full_name'] = "Ivan Montiel"
    testdic['cookiecutter']['email'] = "ivan.montiel@gmail.com"
    testdic['cookiecutter']['version'] = "0.0.1"
    testdic['cookiecutter']['project_name'] = "cookiecutter-example-python-api"
    testdic['cookiecutter']['repo_name'] = "cookiecutter-example-python-api"
    testdic['cookiecutter']['project_short_description'] = "Example python api cookiecutter"
    testdic['cookiecutter']['release_date'] = "2017-11-02"
    test

# Generated at 2022-06-13 18:43:30.253016
# Unit test for function load
def test_load():
    """Test function load."""
    assert load("/Users/tianhub/PycharmProjects/cookiecutter/tests/test-replay/", "test_project") == {
        "cookiecutter": {
            "full_name": "Your Name",
            "email": "your@email.com",
            "github_username": "YourUsername",
            "project_name": "Cookiecutter Test",
            "project_short_description": "A short description of the project.",
            "release_date": "2013-10-03",
            "year": "2013"
        }
    }


# Generated at 2022-06-13 18:43:35.417463
# Unit test for function load
def test_load():
    context = load('test', 'test')
    assert context is not None
    assert context['cookiecutter'] is not None
    assert context['cookiecutter']['repo_dir'] is not None


if __name__ == '__main__':
    test_load()

# Generated at 2022-06-13 18:43:42.716232
# Unit test for function load
def test_load():
    replay_dir = os.getcwd()
    template_name = 'test_template'
    dump(replay_dir, template_name, {'cookiecutter': {'test': 'test'}})
    context = load(replay_dir, template_name)
    assert context['cookiecutter']['test'] == 'test'
    os.remove(get_file_name(replay_dir, template_name))

# Generated at 2022-06-13 18:43:47.033032
# Unit test for function load
def test_load():
    '''
    Testing load function
    :return:
    '''
    # Load a dictionary from file for testing.
    dic = load('tests/test-replay/', 'test-replay/tests/fake-repo-pre/')
    # Display all keys in dictionary
    print(dic.keys())
    # Display value of 'cookiecutter' key
    print(dic['cookiecutter'])


test_load()

# Generated at 2022-06-13 18:43:58.711561
# Unit test for function load
def test_load():
    from modulefinder import ModuleFinder
    import inspect
    import os
    import pytest
    from cookiecutter.replay import load
    from cookiecutter.main import cookiecutter

    test_dir = os.path.dirname(os.path.abspath(__file__))
    projects_dir = os.path.sep.join(test_dir.split(os.path.sep)[:-2])
    templates_dir = os.path.join(projects_dir, 'tests', 'files', 'test-template')

    # Create a project directory
    os.chdir(templates_dir)
    cookiecutter(
        '.',
        no_input=True,
        replay_dir=os.path.join(projects_dir, 'replay')
    )

    # Inspect module finder for replay related v

# Generated at 2022-06-13 18:44:02.152066
# Unit test for function load
def test_load():
    filename = 'cookiecutter.json'
    with open(filename, 'r') as infile:
        context = json.load(infile)

    assert isinstance(context, dict)
    assert 'cookiecutter' in context


# Generated at 2022-06-13 18:44:09.712505
# Unit test for function dump
def test_dump():
    replay_dir = os.path.join(os.getcwd(),"test_replays")
    make_sure_path_exists(replay_dir)
    template_name = "test_template"
    context = '{"test_template": {"key": "value"}}'
    assert dump(replay_dir, template_name, context) == None
    replay_file = get_file_name(replay_dir, template_name)
    assert os.path.isfile(replay_file)
    os.remove(replay_file)
    os.rmdir(replay_dir)


# Generated at 2022-06-13 18:44:16.838313
# Unit test for function load
def test_load():
    """Unit test for function load."""
    import json
    import os

    # Write a file first
    replay_dir = '/test/test_load'
    template_name = "test"

# Generated at 2022-06-13 18:44:22.845134
# Unit test for function load
def test_load():
    # Test that load can be called
    replay_dir = "test_replies"
    template_name = "test_template"
    context = {'cookiecutter': {'test': 'test'}}
    dump(replay_dir, template_name, context)
    context = load(replay_dir, template_name)
    assert 'cookiecutter' in context
    os.remove(replay_dir+"/"+template_name+".json")


# Generated at 2022-06-13 18:44:26.150619
# Unit test for function load
def test_load():
    # Failing test case
    # context = load('/tmp', 'unknown')

    # Succeeding test case
    context = load('/tmp', 'new-project')
    assert context['cookiecutter']['project_name'] == 'Test Project'

# Generated at 2022-06-13 18:44:28.177363
# Unit test for function load
def test_load():
    context = load('/Users/Jiajia/.cookiecutters', 'cookiecutter-pypackage')
    return context


# Generated at 2022-06-13 18:44:33.632622
# Unit test for function load
def test_load():
    replay_file = 'cookiecutter_test'
    template_name = 'cookiecutter_test'
    context = {
        'cookiecutter': {
            'full_name': 'cookiecutter_test',
            'project_name': 'cookiecutter_test',
            'version': '0'
        }
    }
    dump(replay_file, template_name, context)
    result = load('cookiecutter_test', 'cookiecutter_test')
    assert result == context
    os.remove('cookiecutter_test/cookiecutter_test.json')


# Generated at 2022-06-13 18:44:35.728724
# Unit test for function load
def test_load():
    assert load("/home/adriana/Git_projects/cookiecutter-pypackage/replay", "replay")

# Generated at 2022-06-13 18:44:40.822171
# Unit test for function load
def test_load():
    """
    test load function.
    
    test if load function can load json file in correct format
    """
    # make the test
    file = 'template.json'
    template_name = 'empty-cookiecutter-template'
    context = load('~/.cookiecutter_replay/', template_name)
    assert context == {'cookiecutter': {'name_template': 'Test Template'}}


# Generated at 2022-06-13 18:44:52.330967
# Unit test for function load
def test_load():
    replay_dir = "."
    template_name = "Jinja2_full"
    c = load(replay_dir, template_name)

# Generated at 2022-06-13 18:44:53.412001
# Unit test for function load

# Generated at 2022-06-13 18:45:04.682804
# Unit test for function load
def test_load():
    # Test that it loads a dict
    d = load('C:/Users/leehh/Documents/GitHub/cookiecutter-data-science', 'default')
    assert isinstance(d, dict)
    # Test that it raises the appropriate error if the file is not a dict
    with open('C:/Users/leehh/Documents/GitHub/cookiecutter-data-science/default.json', 'w') as outfile:
        json.dump("no dict", outfile)
    with pytest.raises(ValueError):
        load('C:/Users/leehh/Documents/GitHub/cookiecutter-data-science', 'default')
        

# Generated at 2022-06-13 18:45:11.691599
# Unit test for function dump
def test_dump():
    replay_dir = os.path.join(os.path.expanduser('~'), '.cookiecutter_replay')
    template_name = 'my_template'
    context = {'cookiecutter': {'user_email': 'me@gmail.com'}}

    dump(replay_dir, template_name, context)

    assert(os.path.isdir(replay_dir))
    replay_file = get_file_name(replay_dir, template_name)
    assert( os.path.isfile(replay_file))


# Generated at 2022-06-13 18:45:14.182144
# Unit test for function load
def test_load():
    template_name = 'actron2018'
    replay_dir = os.path.join(os.getcwd(), 'cookiecutter', 'replay')
    context = load(replay_dir, template_name)
    assert isinstance(context, dict)


# Generated at 2022-06-13 18:45:17.392828
# Unit test for function load
def test_load():
    context = load('/Users/wangchaojiang/Desktop/drcookiecutter', '', 'wangchaojiang')
    print(context)



# Generated at 2022-06-13 18:45:26.916781
# Unit test for function dump
def test_dump():
    try:
        # create context, replay_dir, template_name
        context = {'cookiecutter': {'repo_dir': '.',
                                    'checksum': 'some-sha',
                                    'no_input': True,
                                    'extra_context': {},
                                    'abbreviations': {}}}
        replay_dir = '/path/to/replay_dir'
        template_name = 'my_template'

        # dump the context into json file
        dump(replay_dir, template_name, context)

        # check if exists the file
        replay_file = get_file_name(replay_dir, template_name)
        assert os.path.exists(replay_file)
    finally:
        # delete the file
        os.remove(replay_file)


# Generated at 2022-06-13 18:45:35.580320
# Unit test for function load
def test_load():
    replay_dir = "Templates"
    template_name = "hello"
    context = load(replay_dir, template_name)
    assert context == {
      'cookiecutter': {
        '_template': 'hello/',
        'full_name': 'James',
        'email': 'james@example.com',
        'project_name': 'My Project',
        'project_short_description': 'A short description of the project.',
        'pypi_username': 'example',
        'github_username': 'example',
        'repo_name': 'my_project',
        'year': '2016',
        'version': '0.1.0',
        'open_source_license': 'Not open source'
      }
    }

# Generated at 2022-06-13 18:45:43.457288
# Unit test for function load
def test_load():
    """Load context from json file."""
    # test load 'master'
    assert(load('cookiecutter.replay/cookiecutter/master', 'master') == {'cookiecutter': {'master': 'master'}})
    # test load 'master.json'
    assert(load('cookiecutter.replay/cookiecutter/master', 'master.json') == {'cookiecutter': {'master': 'master'}})

# Generated at 2022-06-13 18:45:52.849027
# Unit test for function load
def test_load():
    """Unit test for load function."""
    my_dir = os.path.dirname(os.path.abspath(__file__))
    replay_dir = os.path.join(my_dir, '_replay')
    template_name = 'cookiecutter-pypackage'

    context = load(replay_dir, template_name)
    assert isinstance(context, dict)
    assert 'cookiecutter' in context
    assert isinstance(context['cookiecutter'], dict)
    assert '_template' not in context['cookiecutter']
    assert context['cookiecutter']['project_name'] == 'cookiecutter-pypackage'


# Generated at 2022-06-13 18:46:39.552884
# Unit test for function load
def test_load():
    try:
        load('', "")
    except TypeError:
        pass


# Generated at 2022-06-13 18:46:42.650088
# Unit test for function load
def test_load():
    """Test function load()."""
    from cookiecutter import replay
    from pathlib2 import Path
    import json
    path = Path(__file__).parent / 'replay'
    data = replay.load(path, 'cookiecutter')
    assert isinstance(data, dict)
    assert isinstance(data['cookiecutter'], dict)

# Generated at 2022-06-13 18:46:48.536094
# Unit test for function load
def test_load():
    # no template name
    try:
        load('./', None)
        assert False
    except TypeError:
        assert True

    # no replay dir
    try:
        load(None, 'test')
        assert False
    except TypeError:
        assert True

    # no cookiecutter key in context
    try:
        load('./', 'test')
        assert False
    except ValueError:
        assert True

    # success case
    try:
        context = load('./tests/fixtures/replay', 'test')
        assert 'cookiecutter' in context
        assert context['cookiecutter']['project_name'] == 'Test Project'
    except Exception:
        assert False


# Generated at 2022-06-13 18:46:53.651685
# Unit test for function load
def test_load():
    """Test the load function."""
    template_name = 'requirements'
    replay_dir = 'tests/test-replay'
    context = load(replay_dir, template_name)
    assert context['cookiecutter']['repo_name'] == 'pip-tools'
    print('test_load successful')



# Generated at 2022-06-13 18:46:57.214914
# Unit test for function load
def test_load():
    try:
        load(replay_dir = "C:/Users/piete/OneDrive/Bureaublad/Github/cookiecutter-data-science/tests/test-data/", template_name = 'data-science', context = {})
    except:
        raise


# Generated at 2022-06-13 18:46:59.850990
# Unit test for function load
def test_load():
    replay_dir = '.cookie_replay'
    template_name = 'python_package'
    context = load(replay_dir, template_name)
    print(context)

# Generated at 2022-06-13 18:47:06.080964
# Unit test for function load
def test_load():
    from cookiecutter.main import cookiecutter
    from jinja2 import Environment, FileSystemLoader
    from pytest import raises

    template = Environment(loader=FileSystemLoader('tests/test-templates')).get_template('test-replay')

    with raises(ValueError) as excinfo:
        context = load('/tmp', template.name)
    assert 'Context is required to contain a cookiecutter key' in str(excinfo)

    rendered_template = template.render({'cookiecutter': {'foo': 'bar'}})
    cookiecutter('/tmp', no_input=True, extra_context={'replay': rendered_template})
    context = load('/tmp', template.name)
    context['cookiecutter']['foo'] == 'bar'


# Generated at 2022-06-13 18:47:14.645478
# Unit test for function load
def test_load():
    """Load replay files."""
    assert isinstance(load('/home/lzhao/programming/xkcd_comics_cookiecutter/tests/', 'other_replay'), dict)
    assert isinstance(load('/home/lzhao/programming/xkcd_comics_cookiecutter/tests/', 'replay'), dict)
    assert load('/home/lzhao/programming/xkcd_comics_cookiecutter/tests/', 'replay')['cookiecutter']
    assert load('/home/lzhao/programming/xkcd_comics_cookiecutter/tests/', 'other_replay')['cookiecutter']

# Generated at 2022-06-13 18:47:18.482914
# Unit test for function load
def test_load():
    file_name = "./../data/13-vectors/1/cookiecutter.json"
    context = load("./", file_name)
    return context


# Generated at 2022-06-13 18:47:21.905446
# Unit test for function load
def test_load():
    # Set location of test dir
    test_dir = "test"
    context = load(test_dir, "conda-project")
    # Test that the context contains the cookiecutter key
    assert "cookiecutter" in context


# Generated at 2022-06-13 18:48:12.091345
# Unit test for function load
def test_load():
    """Test the load function."""
    assert load('/Users/michelle.zhu/code/GitHub/cookiecutter/tests/fixtures/test-replay-dir/', 'simple') == ({'cookiecutter': {'project_name': 'Test Project', '_copy_without_render': ['LICENSE.md', 'README.md', 'docs/contributing.rst', 'docs/history.rst']}, 'replay': True},)


# Generated at 2022-06-13 18:48:12.998431
# Unit test for function load
def test_load():
    # TODO
    raise NotImplementedError

# Generated at 2022-06-13 18:48:20.913505
# Unit test for function load