

# Generated at 2022-06-13 18:38:24.346368
# Unit test for function load
def test_load():
    data1 = load("/home/manish/PycharmProjects/cookiecutter/examples/tests/test-replay","b")
    print(data1)


# Generated at 2022-06-13 18:38:25.630991
# Unit test for function load
def test_load():
    """Unit test for function load."""
    context = {}
    load(context, '')

# Generated at 2022-06-13 18:38:30.101010
# Unit test for function dump
def test_dump():
    replay_dir = './tests/files/fake-replay'
    template_name = 'example'
    context = {
        'cookiecutter': {
            'author_name': 'John Cleese',
            'author_location': 'Monty Python'
        }
    }
    dump(replay_dir, template_name, context)



# Generated at 2022-06-13 18:38:35.262025
# Unit test for function get_file_name
def test_get_file_name():
    """Unit test for function get_file_name."""
    assert get_file_name('a_path', 'a_name') == 'a_path/a_name.json'
    assert get_file_name('another_path', 'a_name.json') == 'another_path/a_name.json'
    assert get_file_name('/', 'a_name.json') == '/a_name.json'
    assert get_file_name('/a_path', 'a_name.json') == '/a_path/a_name.json'
    assert get_file_name('/a_path', 'a_name') == '/a_path/a_name.json'

# Generated at 2022-06-13 18:38:45.574993
# Unit test for function get_file_name
def test_get_file_name():
    replay_dir = '/tmp'

    # Test with a json suffix
    template_name = 'cookiecutter-pypackage'
    replay_file = get_file_name(replay_dir, template_name)
    # This is the expected result
    exp_replay_file = '/tmp/cookiecutter-pypackage.json'
    assert replay_file == exp_replay_file

    # Test without a json suffix
    template_name = 'cookiecutter-pypackage.json'
    replay_file = get_file_name(replay_dir, template_name)
    # This is the expected result
    exp_replay_file = '/tmp/cookiecutter-pypackage.json'
    assert replay_file == exp_replay_file



# Generated at 2022-06-13 18:38:52.758143
# Unit test for function dump
def test_dump():
    """Test replay.dump function."""
    template_name = 'cookiecutter-pypackage'
    context = {'cookiecutter':
        {
            'project_name': 'My Test Project',
            'repo_name': 'my_test_project',
            'version': '0.1.0',
            'description': 'A short description of the project.',
            'author_name': 'Your Name',
            'email': 'you@example.com',
            'year': '2016',
            'full_name': 'Your Name',
            'github_username': 'your_github_username',
            'select_license': 'MIT license',
        }
    }
    replay_dir = './tests/test_replay/replay'
    #dump(replay_dir, template_name, context)


# Generated at 2022-06-13 18:38:53.981820
# Unit test for function load
def test_load():
    assert isinstance(load('',''), dict)

# Generated at 2022-06-13 18:39:01.228033
# Unit test for function dump
def test_dump():
    """ Unit test for function dump """
    # Overwrite the existing template.json file with the new context
    replay_dir = '.'
    template_name = 'template.json'
    context = {
        'cookiecutter': {
            'project_name': 'PyProject',
            'project_slug': 'pyproject'
        },
        'version': 1.0
    }
    dump(replay_dir, template_name, context)


# Generated at 2022-06-13 18:39:05.532860
# Unit test for function load
def test_load():
    base_path = os.getcwd()
    template_name = "pytest_example"
    replay_dir = os.path.join(base_path, "tests", "test-replay")
    context = load(replay_dir, template_name)
    assert isinstance(context, dict)
    assert 'cookiecutter' in context


# Generated at 2022-06-13 18:39:12.765073
# Unit test for function dump
def test_dump():
    replay_dir = os.path.join(os.getcwd(), 'tests/files/fake-replay')
    template_name = 'fake-repo-pre/'
    context = {
        'cookiecutter': {
            'full_name': {
                'default': 'Jack Scully',
                'description': 'Your full name',
                'name': 'full_name',
                'type': 'string'
            }
        }
    }
    expected = '''{
  "cookiecutter": {
    "full_name": {
      "default": "Jack Scully",
      "description": "Your full name",
      "name": "full_name",
      "type": "string"
    }
  }
}'''
    dump(replay_dir, template_name, context)
    replay_file

# Generated at 2022-06-13 18:39:22.969967
# Unit test for function load
def test_load():
    cookiecutter_dict = {
        u'cookiecutter': {
            u'author': u'Your Name',
            u'email': u'you@example.com',
            u'github_username': u'your-username',
            u'full_name': u'Your Name',
            u'project_name': u'project_name'
        }
    }
    with open('test', 'w') as outfile:
        json.dump(cookiecutter_dict, outfile, indent=2)

# Generated at 2022-06-13 18:39:30.486726
# Unit test for function load
def test_load():
    import json
    #for file in os.listdir('/Users/camelia/Desktop/cookiecutter/cookiecutter-pypackage/tests/fixtures/replay'):
    #    print(file)

    # read data from json file
    #with open('/Users/camelia/Desktop/cookiecutter/cookiecutter-pypackage/tests/fixtures/replay/cookiecutter-pypackage.json','r') as infile:
    #    context=json.load(infile)
    #print(context)
    #context={u'full_name': u'Camelia C. Dragomir', u'email': u'camelia.c.dragomir@gmail.com', u'github_username': u'ccaruntu', u'version': u'0.1

# Generated at 2022-06-13 18:39:36.576851
# Unit test for function load
def test_load():
    assert load('tests/test-data/fake-repo-pre/', 'fake-repo-pre') == {
        'cookiecutter': {
            'full_name': 'Your Name',
            'email': 'you@example.com',
            'project_name': 'project_name',
            'project_slug': 'project_slug',
            'repo_name': 'repo_name',
            'release_date': 'YYYY-MM-DD',
            'version': '0.1.0',
            'year': 'YYYY',
            'project_short_description': 'project_short_description'
        }
    }


# Generated at 2022-06-13 18:39:42.361281
# Unit test for function dump
def test_dump():
    context = {
        'cookiecutter': {
            'full_name': 'Audrey Roy Greenfeld',
            'email': 'audreyr@example.com'}
    }
    replay_dir = 'tests/files/test-replay1'
    template_name = 'audreyr/cookiecutter-pypackage'
    dump(replay_dir=replay_dir, context=context, template_name=template_name)

    replay_file = 'tests/files/test-replay1/audreyr---cookiecutter-pypackage.json'
    with open(replay_file, 'r') as fp:
        content = json.load(fp)


# Generated at 2022-06-13 18:39:45.139730
# Unit test for function load
def test_load():
    """Unit test for function load."""
    pass


# Generated at 2022-06-13 18:39:51.820340
# Unit test for function load
def test_load():
    """Unit test for function load."""
    conf = load("/home/johnny/.cookiecutters/", "cookie_master")
    print("\n")
    print("The following is the context from JSON read from the replay file")
    print("\n")
    print(conf)


# Generated at 2022-06-13 18:39:59.361670
# Unit test for function load
def test_load():
    replay_dir = "tests/test-output/replay"
    if not make_sure_path_exists(replay_dir):
        raise IOError('Unable to create replay dir at {}'.format(replay_dir))
    else:
        print("replay dir created")
    replay_file = get_file_name(replay_dir, "test-template/.cookiecutter.json")

# Generated at 2022-06-13 18:40:08.969354
# Unit test for function load
def test_load():
    """ Test function load"""
    #load(replay_dir, template_name)
    assert load('.', 'test.json') == {'cookiecutter': 'default'}
    assert load('.', 'test') == {'cookiecutter': 'default'}
    assert load('.', 'invalid.json') == None
    assert load('.', 'invalid') == None
    assert load('.', None) == None
    assert load(None, 'test.json') == None
    assert load(None, 'test') == None
    assert load(None, 'invalid.json') == None
    assert load(None, 'invalid') == None
    assert load(None, None) == None
    assert load(None) == None
    assert load('.', {}) == None
    assert load('.', []) == None

# Generated at 2022-06-13 18:40:18.693676
# Unit test for function load

# Generated at 2022-06-13 18:40:23.462665
# Unit test for function load
def test_load():
    print(load('/home/shweta/Documents/6th semester/cloud_security/assignment_3', 'cookiecutter.json'))
  #  print(load('/home/shweta/Documents/6th semester/cloud_security/assignment_3', 'cookiecutter.json1'))
    print(load('/home/shweta/Documents/6th semester/cloud_security/assignment_3', 'cookie.json'))


# Generated at 2022-06-13 18:40:31.326377
# Unit test for function dump
def test_dump():
    replay_dir = 'replay-dir'
    template_name = 'test-template'
    context = {
        'cookiecutter': {
            'test-key': 'test-value'
        }
    }
    try:
        dump(replay_dir, template_name, context)
    except:
        print("test_dump failed")


# Generated at 2022-06-13 18:40:38.610088
# Unit test for function load
def test_load():
    # Test good input
    result = load('.', 'cookiecutter.json')
    assert result, "test_load() test1 failed, should return value"

    # Test bad input
    try:
        load('.', 'cookiecutter1.json')
    except ValueError as exception:
        assert str(exception) == 'Context is required to contain a cookiecutter key', "test_load() test2 failed, should raise ValueError exception"


# Generated at 2022-06-13 18:40:43.865490
# Unit test for function load
def test_load():
    # Prepare data
    replay_dir = '.'
    template_name = 'test'
    context_expected = {'cookiecutter': {'user_name': 'Gary', 'project_name': 'test'}}
    # Run function
    context_actual = load(replay_dir, template_name)
    # Assert
    assert context_expected == context_actual


# Generated at 2022-06-13 18:40:53.709937
# Unit test for function load
def test_load():
    import json
    import os
    import tempfile

    replay_dir = tempfile.mkdtemp()
    template_name = 'test'
    replay_file_name = os.path.join(replay_dir, template_name + '.json')

    template = {
        'cookiecutter': {
            '_template': 'https://github.com/audreyr/cookiecutter-pypackage.git',
            'project_name': 'my-awesome-project',
            'release_date': '2014-12-11',
            'use_pypi_deployment_with_travis': 'y'  # standard prompt: 'y/N'
        }
    }


# Generated at 2022-06-13 18:40:55.374706
# Unit test for function load
def test_load():
    assert load('/home/todo/cookiecutter-pypackage', 'cookiecutter-pypackage')



# Generated at 2022-06-13 18:40:56.238180
# Unit test for function load
def test_load():
    assert callable(load)

# Generated at 2022-06-13 18:41:04.493373
# Unit test for function dump
def test_dump():
    import os
    import shutil
    context2 = {
        "cookiecutter": {
            "full_name": "Test",
            "email": "test@test.com",
        },
    }


# Generated at 2022-06-13 18:41:08.561432
# Unit test for function dump
def test_dump():

    template_name = 'test_template'
    replay_dir = 'test_replay_dir'
    context = {
        'cookiecutter': {
            '_template': template_name
        }
    }

    dump(replay_dir, template_name, context)
    file_name = get_file_name(replay_dir, template_name)
    assert os.path.exists(file_name)


# Generated at 2022-06-13 18:41:10.254526
# Unit test for function dump
def test_dump():
    context = {'cookiecutter': {'name': 'example', 'platform': 'example', 'version': '1.0'}}
    dump('test', 'template_replay', context)
    return True


# Generated at 2022-06-13 18:41:11.461878
# Unit test for function load
def test_load():
    """Unit test for function load."""
    assert load('/tmp/test_dir', 'templatename') == None


# Generated at 2022-06-13 18:41:18.180858
# Unit test for function load
def test_load():
    template_name = 'LapPD'
    replay_dir = os.path.join('..', '.cookiecutters')
    context = load(replay_dir, template_name)

    assert isinstance(context, dict)
    assert context['cookiecutter']['full_name'] == 'Thomas Draper'



# Generated at 2022-06-13 18:41:21.589508
# Unit test for function load
def test_load():
    """Function to test load function for replay.py."""
    context = load('./tests/fake-repo-pre/', 'fake-repo-pre')
    assert context['cookiecutter']['full_name'] == 'Audrey Roy'



# Generated at 2022-06-13 18:41:31.762994
# Unit test for function load
def test_load():
    replay_dir = os.path.join(os.path.expanduser('~'), '.cookiecutter_replay')
    template_name = 'example'
    template_context = {
        'cookiecutter': {
            'full_name': 'Arthur Dent',
            'email': 'earthling@example.com',
        }
    }

    # Ensure that the template file doesn't already exist
    replay_file = get_file_name(replay_dir, template_name)
    if os.path.isfile(replay_file):
        os.remove(replay_file)

    # Dump the template
    dump(replay_dir, template_name, template_context)

    # Read it from disk
    template_context_loaded = load(replay_dir, template_name)

    # Remove the template file

# Generated at 2022-06-13 18:41:35.242275
# Unit test for function load
def test_load():
    replay_dir = os.path.join('tests', 'test-replay')
    template_name = 'test-repo'
    context = load(replay_dir, template_name)
    assert 'cookiecutter' in context
    print(context)


# Generated at 2022-06-13 18:41:39.158409
# Unit test for function load
def test_load():
    context = load('replay', 'test')
    cookiecutter = context['cookiecutter']
    assert cookiecutter['repo_dir'] == '~/Documents/GitHub/test'


# Generated at 2022-06-13 18:41:42.174731
# Unit test for function load
def test_load():
    replay_dir = ".."
    template_name =  "cookiecutter"
    result = load(replay_dir, template_name)
    #print (result)


# Generated at 2022-06-13 18:41:44.420680
# Unit test for function load
def test_load():
    context = load('tests/test-replay/', 'example_cookie.json')
    assert len(context['cookiecutter'].keys()) == 7


# Generated at 2022-06-13 18:41:54.633391
# Unit test for function load

# Generated at 2022-06-13 18:41:59.733893
# Unit test for function dump
def test_dump():
    template_name = "test_template"
    replay_dir = "test_replay"
    context = dict()
    context["cookiecutter"] = dict()
    context["cookiecutter"]["replay"] = "test_replay"
    context["cookiecutter"]["template_name"] = "test_template"
    context["cookiecutter"]["project_name"] = "test_project_name"
    dump(replay_dir, template_name, context)
    loaded_context = load(replay_dir, template_name)
    assert context == loaded_context
    os.remove("{}/{}.json".format(replay_dir, template_name))

# Generated at 2022-06-13 18:42:01.070188
# Unit test for function load
def test_load():
    try: 
        context = load("","")
        assert False
    except ValueError:
        assert True
    except:
        assert False


# Generated at 2022-06-13 18:42:05.617641
# Unit test for function load
def test_load():
    replay_dir = '/Users/yemilice/workspace/myplayground/cookiecutter/tests/replay'
    template_name = 'tests/fake-repo-tmpl'
    context = load(replay_dir, template_name)
    print(context)


# Generated at 2022-06-13 18:42:12.288293
# Unit test for function dump
def test_dump():
    """Test the dump function"""
    replay_dir = "test"
    template_name = "template1"
    context = {'cookiecutter': {'name': "value"}}
    context_file = get_file_name(replay_dir, template_name)
    try:
        dump(replay_dir, template_name, context)
    except:
        assert False, "Failed to dump context to file"

    assert os.path.exists(replay_dir), "Replay directory does not exist"
    assert os.path.isfile(context_file), "Context file does not exist"

    try:
        os.remove(context_file)
    except:
        assert False, "Failed to cleanup context file"

# Generated at 2022-06-13 18:42:15.113454
# Unit test for function load
def test_load():
    """Test function load"""
    load_result = load('.', 'test.json')
    assert load_result == {'cookiecutter': 'test'}
    print('Unit test success!')

test_load()

# Generated at 2022-06-13 18:42:17.472193
# Unit test for function load
def test_load():
    """Use function load to get context"""
    context = load("C:/Users/dell/Desktop/cookiecutter-pypackage-minimal", "cookiecutter.json")
    print(context)

if __name__ == '__main__':
    test_load()

# Generated at 2022-06-13 18:42:24.351823
# Unit test for function load
def test_load():
    # replay_dir = '/home/repos/cookiecutter-python'
    # context = load(replay_dir, 'cookiecutter-python')

    replay_dir = '/home/repos/cookiecutter-pypackage'
    context = load(replay_dir, 'cookiecutter-pypackage')

    assert context['cookiecutter']['project_name'] == 'cookiecutter-pypackage'

# Generated at 2022-06-13 18:42:26.238978
# Unit test for function load
def test_load():
    context = load('/Users/yuanguo/Projects/cookiecutter-project-template', 'audience')
    print(context)


# Generated at 2022-06-13 18:42:29.674142
# Unit test for function load
def test_load():
    """Test function load."""
    try:
        load(replay_dir="~", template_name="~")
    except TypeError as e:
        print(e)

    try:
        load(replay_dir="~", template_name="~")
    except ValueError as e:
        print(e)

# Generated at 2022-06-13 18:42:34.320818
# Unit test for function load
def test_load():
    with open("replay-tests.json", "r") as file:
        tests = json.load(file)
        for test in tests:
            print("Cargando test " + test['nombre'] + "...")
            respuesta = load("replay", test['nombre'])
            print("Comprobando que el test " + test['nombre'] + " pase...")
            assert respuesta == test['respuesta']


# Generated at 2022-06-13 18:42:42.421714
# Unit test for function load
def test_load():
    """Unit test for function load."""
    from cookiecutter import __file__ as CCFILE, main, logging
    from cookiecutter import utils
    from cookiecutter.main import cookiecutter

    utils.WORKING_DIR = os.path.dirname(os.path.abspath(CCFILE))
    logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

    context = load('/home/gopi/cookiecutter-blog/tests/test-replay', 'tests/test-replay/use_replay')
    assert isinstance(context, dict), 'Context is not a valid dict'


# Generated at 2022-06-13 18:42:54.312835
# Unit test for function dump
def test_dump():
    from tempfile import TemporaryDirectory
    from cookiecutter import replay

    with TemporaryDirectory() as replay_dir:
        template_name = 'example-template'
        context = {
            'cookiecutter': {
                'name': 'Mike',
                'project_slug': 'mike',
                'description': 'This is a cookiecutter template',
                'year': '2018',
                'full_name': 'Mike Bright',
                'email': 'mike@example.com',
                'github_username': 'mikebright',
            }
        }

        expected_file_name = replay.get_file_name(replay_dir, template_name)

        replay.dump(replay_dir, template_name, context)

        assert os.path.isfile(expected_file_name)



# Generated at 2022-06-13 18:43:00.632798
# Unit test for function dump
def test_dump():
    replay_dir = 'tests/dummy_replays'
    if not os.path.exists(replay_dir):
        os.makedirs(replay_dir)
    template_name = 'cookie_test1'
    context = {'cookiecutter': {'test_key': 'test_value'}}
    dump(replay_dir, template_name, context)
    replay_file = get_file_name(replay_dir, template_name)
    assert os.path.exists(replay_file) == True


# Generated at 2022-06-13 18:43:04.658168
# Unit test for function load
def test_load():
    context=load('C:/Users/zhong/Desktop/try/test_cookiecutter/replay', 'template')
    print(context)
    assert True

if __name__ == '__main__':
    test_load()

# Generated at 2022-06-13 18:43:07.745975
# Unit test for function load
def test_load():
    context = load("/home/xixi/.cookiecutters/test_project_chiwan/", "test_cookiecutter.json")
    print(context)


if __name__ == '__main__':
    test_load()

# Generated at 2022-06-13 18:43:10.342703
# Unit test for function load
def test_load():
    test_context = {'cookiecutter': {'_template': 'fake', 'extra_context': {'_template': 'fake'}}}
    assert test_contex

# Generated at 2022-06-13 18:43:20.600428
# Unit test for function load
def test_load():
    from cookiecutter import config
    from cookiecutter.utils import rmtree
    from cookiecutter.main import cookiecutter

    # Setup
    project = 'example-repo2'
    template_name = 'tests/test-data/{{cookiecutter.repo_name}}'
    output_dir = 'tests/test-data/{{cookiecutter.repo_name}}/{{cookiecutter.repo_name}}'

# Generated at 2022-06-13 18:43:22.819998
# Unit test for function load
def test_load():
    load('/Users/simon/Desktop/cookiecutter-pypackage', 'cookiecutter.json')

# Generated at 2022-06-13 18:43:31.021756
# Unit test for function load
def test_load():
    """Unit test for function load."""

    import json

    from cookiecutter.generate import generate_context, generate_files

    from cookiecutter import main, exceptions

    expected = {
        'cookiecutter': {
            'project_name': 'Python Package'
        }
    }

    replay_dir = 'tests/test-output'
    template_name = 'tests/fake-repo-pre/'

    try:
        context = load(replay_dir, template_name)
    except exceptions.InvalidModeException:
        pass
    else:
        raise Exception('Exception InvalidModeException not raised')

    try:
        context = load(replay_dir, template_name)
    except exceptions.RepoNotFoundException:
        pass
    else:
        raise Exception('Exception RepoNotFoundException not raised')



# Generated at 2022-06-13 18:43:35.366315
# Unit test for function load
def test_load():
    replay_dir = 'test_dir'
    template_name = 'test_template'
    context = {'cookiecutter': 'test'}
    dump(replay_dir, template_name, context)
    assert context == load(replay_dir, template_name)

# Generated at 2022-06-13 18:43:41.105962
# Unit test for function dump
def test_dump():
    """Test the dump function."""
    template_name = 'hello_world'
    replay_dir = '.'
    context = {'cookiecutter': {'full_name': 'Janet Doe', 'email': 'janetdoe@example.com'}}
    dump(replay_dir, template_name, context)


# Generated at 2022-06-13 18:43:42.199755
# Unit test for function load
def test_load():
    pass



# Generated at 2022-06-13 18:43:44.251261
# Unit test for function load
def test_load():
    assert(load('/test/test_template', 'test_template') == {'cookiecutter': 'test_template'})

# Generated at 2022-06-13 18:43:48.618702
# Unit test for function dump
def test_dump():
    replay_dir = '/Users/huimingzhao/cookiecutter-example-2/dump'
    template_name = 'cookiecutter-example-2'
    context = {
        'cookiecutter': {
            'project_name': 'cookiecutter-example-2',
            'repo_name': 'yourname/cookiecutter-example',
            'description': 'An example package from Cookiecutter',
        }
    }
    dump(replay_dir, template_name, context)


# Generated at 2022-06-13 18:43:52.605487
# Unit test for function load
def test_load():
    template_name = 'test_template'
    context = load(test_replay_dir, template_name)
    assert isinstance(context, dict)
    assert 'cookiecutter' in context.keys()



# Generated at 2022-06-13 18:43:59.145501
# Unit test for function load
def test_load():
    template_name = os.path.join(os.path.dirname(__file__), '../test-template')
    replay_dir = os.path.join(os.path.dirname(__file__), '../test-replay')
    dump(replay_dir, template_name, {'cookiecutter': {'name': 'cookiecutter', 'version': '0.9.1'}})
    dump(replay_dir, 'test-template', {'cookiecutter': {'name': 'cookiecutter', 'version': '0.9.1'}})
    result = load(replay_dir, template_name)
    assert result['cookiecutter']['name'] == 'cookiecutter'
    assert result['cookiecutter']['version'] == '0.9.1'
    result = load

# Generated at 2022-06-13 18:44:06.146208
# Unit test for function load
def test_load():
    replay_dir = '.test_replay'
    if not os.path.exists(replay_dir):
        os.makedirs(replay_dir)
    with open('.test_replay/test.json', 'w') as f:
        f.write('{"cookiecutter":{"default_context":true}}')

    context = load(replay_dir, 'test')
    assert context.get('cookiecutter').get('default_context') == True

    import shutil
    shutil.rmtree(replay_dir)


# Generated at 2022-06-13 18:44:08.186523
# Unit test for function load
def test_load():
    """
    load function test.
    """
    assert isinstance(load('', ''), dict)



# Generated at 2022-06-13 18:44:13.049840
# Unit test for function dump
def test_dump():
    replay_dir = '../tests/test-output/'
    template_name = 'test_template'
    context = {'cookiecutter': {'full_name': 'test_user', 'email': 'test_user@test.test'}}
    replay.dump(replay_dir, template_name, context)
    with open(replay_dir + template_name + '.json', 'r') as infile:
        assert (json.load(infile) == context)


# Generated at 2022-06-13 18:44:14.732455
# Unit test for function load
def test_load():
    context = load('.', 'template_name')
    assert context['cookiecutter'] == '{{cookiecutter.project_slug}}'

# Generated at 2022-06-13 18:44:16.261570
# Unit test for function load
def test_load():
    context = load('replay', 'project_name')
    assert 'project_name' in context['cookiecutter']



# Generated at 2022-06-13 18:44:21.994965
# Unit test for function load
def test_load():
    """Test load function."""
    import tempfile
    template_name='dummy_template'
    replay_dir = tempfile.mkdtemp()
    context = {'cookiecutter': {'hello': 'world'}}
    dump(replay_dir, template_name, context)
    assert load(replay_dir, template_name) == context
    os.chdir(replay_dir)
    os.remove(template_name)

# Generated at 2022-06-13 18:44:28.289030
# Unit test for function load
def test_load():
    context = load('./tests/replay_integration', './tests/fake-repo-pre/')
    assert(context.get('cookiecutter').get('foo') == 'bar')
    assert(context.get('cookiecutter').get('baz') == 'qux')



# Generated at 2022-06-13 18:44:34.740680
# Unit test for function load
def test_load():
    answer = {'full_name': 'Audrey Roy', 'email': 'audreyr@gmail.com', 'github_username': 'audreyr', 'project_name': 'cookiecutter-pypackage', 'repo_name': 'cookiecutter-pypackage', 'pypi_username': 'audreyr', 'project_short_description': 'A Python package project template.', 'cookiecutter': {'github_repo': 'audreyr/cookiecutter-pypackage', 'replay_dir': '~/.cookiecutters', 'no_input': False, 'extra_context': {}, 'verbose': False}, 'version': '0.1.0', 'open_source_license': 'BSD license'}

# Generated at 2022-06-13 18:44:38.070026
# Unit test for function load
def test_load():
    replay_dir = os.path.join(os.path.abspath('.'), 'tests', 'test-replay')
    template_name = 'test-template'
    context = load(replay_dir, template_name)
    print(context)

# Generated at 2022-06-13 18:44:40.373116
# Unit test for function load
def test_load():
    replay_dir = "replay_dir"
    template_name = "test_load"
    context = load(replay_dir, template_name)
    assert isinstance(context['cookiecutter'], dict) is True

# Generated at 2022-06-13 18:44:44.995417
# Unit test for function load
def test_load():
    replay_dir = "C:/Users/koutil/OneDrive/Python/E4E-BackendEngineer/cookiecutter-Honeywell"
    template_name = "Honeywell-BackendEngineer"
    context = load(replay_dir, template_name)
    print(context)


# Generated at 2022-06-13 18:44:49.713896
# Unit test for function load
def test_load():
    import os
    replay_dir = os.getcwd()
    print(replay_dir)
    template_name = 'flask-sample-app'
    print(load(replay_dir, template_name))


# Generated at 2022-06-13 18:44:55.909089
# Unit test for function load
def test_load():
    template_name = 'template_name'
    replay_dir = os.path.join(os.path.expanduser('~'), '.cookiecutters')
    context = {'cookiecutter': {}}
    dump(replay_dir, template_name, context)
    load(replay_dir, template_name)

# Generated at 2022-06-13 18:45:05.261266
# Unit test for function load
def test_load():
    replay_dir = 'tests_dir'
    template_name = 'replay_test_template'
    context = {}
    context['cookiecutter'] = {}
    context['cookiecutter']['author_name'] = "John Doe"
    context['cookiecutter']['repository_name'] = "hello_world"
    dump(replay_dir, template_name, context)
    new_context = load(replay_dir, template_name)
    assert new_context['cookiecutter']['author_name'] == "John Doe"
    assert new_context['cookiecutter']['repository_name'] == "hello_world"


# Generated at 2022-06-13 18:45:08.316113
# Unit test for function load
def test_load():
    """Unit test for function load"""
    template_name = 'generate_file_from_replay'
    context = load('replays', template_name)
    print(context)


# Generated at 2022-06-13 18:45:15.206169
# Unit test for function dump
def test_dump():
    """Test dump."""
    import tempfile
    import shutil
    from os.path import join
    from os import linesep
    import json
    
    # Create a temporary directory to work with
    tmpdir = tempfile.mkdtemp()
    # dummy contect
    dummy_context = {'foo': 'bar'}
    # get file name
    replay_file = get_file_name(tmpdir, 'template')
    # run dump with our dummy context
    dump(tmpdir, 'template', dummy_context)
    # Open file to check if we're loading a valid json
    with open(replay_file, 'r') as replay_file_handle:
        # load the file
        replay_content = json.load(replay_file_handle)
    # We should win
    assert replay_content == dummy_context

# Generated at 2022-06-13 18:45:25.821459
# Unit test for function load
def test_load():
    template_name = "{{cookiecutter.project_name}}"

# Generated at 2022-06-13 18:45:27.842489
# Unit test for function dump
def test_dump():
    """
    Unit test for function dump.
    
    :return: no return
    """
    assert True
    
    

# Generated at 2022-06-13 18:45:33.763481
# Unit test for function load
def test_load():
    """Need a better unit test."""
    replay_dir = os.path.abspath(os.path.join('tests/fake-repo-pre', '{{cookiecutter.repo_name}}'))
    template_name = 'fake-repo-pre'
    context = load(replay_dir, template_name)
    assert context.get('cookiecutter').get('repo_name') == 'test-this-repo'



# Generated at 2022-06-13 18:45:35.396940
# Unit test for function load
def test_load():
    context = load('replay/', 'homepage')
    print(context)

# Generated at 2022-06-13 18:45:39.846890
# Unit test for function load
def test_load():
    replay_dir=os.getcwd()
    template_name='daemons'
    context=load(replay_dir,template_name)
    # print (context)


# Generated at 2022-06-13 18:45:45.463001
# Unit test for function load
def test_load():
    replay_file = "./tests/files/cookiecutter.json"

    context = load('./tests/files', 'cookiecutter')
    if context.get('cookiecutter', {}).get('project_name', {}) == 'project_name':
        print("Test load success")
    else:
        print("Test load failed")



# Generated at 2022-06-13 18:45:55.059127
# Unit test for function load
def test_load():
    replay_dir = "test_replay"
    template_name = "test_name"
    context = {'cookiecutter':
                    {"full_name": "Your Name",
                        "email": "your@email.com",
                        "github_username": "your_github_username",
                        "project_slug": "your_project_slug",
                        "project_name": "Your Project Name",
                        "project_short_description": "A short description of the project.",
                        "release_date": "2013-04-06",
                        "year": "2013",
                        "version": "0.1.0"}}
    dump(replay_dir, template_name, context)
    result = load(replay_dir, template_name)
    assert result == context

# Generated at 2022-06-13 18:46:00.027535
# Unit test for function dump
def test_dump():
    """Test dump."""
    with pytest.raises(TypeError):
        dump(replay_dir=None, template_name=None, context=None)
        dump(replay_dir='replays', template_name=None, context=None)
        dump(replay_dir='replays', template_name='cookiecutter-pypackage', context=None)
        dump(replay_dir='replays', template_name='cookiecutter-pypackage', context=[])


# Generated at 2022-06-13 18:46:04.861698
# Unit test for function dump
def test_dump():
    replay_dir = '/Users/tongfeiwang/Downloads/tmp'
    template_name = 'my_project'
    context = {
        'cookiecutter': {
            'author_name': 'Test Author',
            'project_name': 'Test Project',
            'repo_name': 'Test Repo'
        }
    }

    dump(replay_dir, template_name, context)
    test_file = get_file_name(replay_dir, template_name)
    print("test file: " + test_file)



# Generated at 2022-06-13 18:46:07.871606
# Unit test for function dump
def test_dump():
    replay_dir = os.path.join(os.getcwd(), 'replay')
    template_name = 'test'
    context = {'cookiecutter': {}}
    dump(replay_dir, template_name, context)


# Generated at 2022-06-13 18:46:34.395578
# Unit test for function load
def test_load():
    # Test that a replay file of the wrong name is not found.
    replay_dir = '/Users/matthewmckenna/Desktop/ProjectsWithPython/CookiecutterTest/cookiecutter_test/'
    template_name = 'not_a_real_replay.json'
    try:
        context = load(replay_dir, template_name)
    except:
        pass
    else:
        raise AssertionError('load function should return an error when a file is not found.')

    # Test that a replay file with the wrong type name is not found
    template_name = 'wrong_filetype.txt'
    try:
        context = load(replay_dir, template_name)
    except:
        pass

# Generated at 2022-06-13 18:46:41.496193
# Unit test for function load
def test_load():
    import inspect
    import sys
    import os

    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    parentdir = os.path.dirname(currentdir)
    sys.path.insert(0,parentdir)
    import cookiecutter.main

    # Test load function works correctly
    test_dir = 'tests/files/test-checkout-latest'
    result = load(test_dir, 'fake-project-name')
    assert result == {u'cookiecutter': {u'cookiecutter_version': '1.2.2dev', u'_copy_without_render': ['{{cookiecutter.repo_name}}']}}


# Generated at 2022-06-13 18:46:42.143737
# Unit test for function load
def test_load():
    pass
    

# Generated at 2022-06-13 18:46:46.108435
# Unit test for function load
def test_load():
    dir = "tests/files/replay"
    template_name = "tests/files/replay/test_replay.json"
    context = load(dir, template_name)
    assert type(context) == dict
    assert 'cookiecutter' in context
    assert '_template' in context
    assert type(context['cookiecutter']) == dict
    assert 'project_name' in context['cookiecutter']




# Generated at 2022-06-13 18:46:47.454613
# Unit test for function load
def test_load():
    context = load('/Users/samuelpeng/Desktop/pytorch-gan-master', 'pytorch-gan-master')


# Generated at 2022-06-13 18:46:57.140058
# Unit test for function load
def test_load():
    replay_dir = os.path.join(os.getcwd(), 'replay_dir')
    template_name = 'Yotube-Playlist-Downloader'
    
    if not make_sure_path_exists(replay_dir):
        raise IOError('Unable to create replay dir at {}'.format(replay_dir))
    

# Generated at 2022-06-13 18:46:59.219780
# Unit test for function load
def test_load():
    input_json = r'{"cookiecutter": {"project_name": "Default project_name"}}'
    input_file = 'test_load.json'

    with open(input_file, 'w') as infile:
        infile.write(input_json)

    assert load('./', input_file) == json.loads(input_json)


# Generated at 2022-06-13 18:47:00.738753
# Unit test for function load
def test_load():
	d = load("../cookiecutter_test","example")
	assert d["cookiecutter"]["full_name"] == "Your Name"


# Generated at 2022-06-13 18:47:06.786661
# Unit test for function load
def test_load():
    # Ensure that FileNotFoundError is raised when non-existing file is loaded
    non_existing_file = '/path/to/nonexisting.json'
    try:
        load(non_existing_file)
    except FileNotFoundError:
        pass

    # Ensure that TypeError is raised when non-string path is provided
    non_string_path = ['/path/to/existing.json']
    try:
        load(non_string_path)
    except TypeError:
        pass

    # Ensure that ValueError is raised when non-dictionary is loaded
    non_dict_file = '/path/to/nondict.json'
    try:
        load(non_dict_file)
    except ValueError:
        pass

    # Ensure that dictionary is returned when valid file is loaded

# Generated at 2022-06-13 18:47:14.833582
# Unit test for function dump
def test_dump():
    from cookiecutter import replay
    from tempfile import mkdtemp
    import shutil
    import os

    directory = mkdtemp()

    # Test for non string template name
    try:
        replay.dump(directory, 4, {})
    except TypeError as e:
        assert 'Template name is required to be of type str' in str(e)

    # Test for non dict context
    try:
        replay.dump(directory, 'test', '')
    except TypeError as e:
        assert 'Context is required to be of type dict' in str(e)

    # Test for missing cookiecutter key in context
    try:
        replay.dump(directory, 'test', {'foo': 'bar'})
    except ValueError as e:
        assert 'Context is required to contain a cookiecutter key' in str(e)

# Generated at 2022-06-13 18:47:36.135230
# Unit test for function load
def test_load():
    """Test the load function."""
    os.chdir('..') # Move out of replays/
    import cookiecutter.main
    from cookiecutter.main import cookiecutter

    context = cookiecutter('.', no_input=True) # First run
    cc_json = 'replays/cookiecutter.json'

    if os.path.exists(cc_json):
        os.remove(cc_json)

    if os.path.exists('cookiecutter.json'):
        os.remove('cookiecutter.json')

    dump('replays', 'cookiecutter', context) # Second run
    new_dict = load('replays', 'cookiecutter') # Third run

    if new_dict == context:
        print('\nTest load: TEST PASSED!')

# Generated at 2022-06-13 18:47:43.091919
# Unit test for function dump
def test_dump():
    context = {
        'cookiecutter': {}
    }
    import tempfile, shutil
    temp_dir = tempfile.mkdtemp()
    dump(temp_dir, 'abc', context)
    replay_file = get_file_name(temp_dir, 'abc')
    with open(replay_file, 'r') as infile:
        assert json.load(infile) == context
    shutil.rmtree(temp_dir)


# Generated at 2022-06-13 18:47:45.350613
# Unit test for function dump
def test_dump():
	replay_dir = '~'
	template_name = 'a'
	context = {'cookiecutter':'hello'}
	dump(replay_dir, template_name, context)


# Generated at 2022-06-13 18:47:53.347026
# Unit test for function load
def test_load():
    replay_dir = os.path.normpath("test_dir")
    template_name = "4-4-4"
    expected_answer = {u'cookiecutter': {u'project_name': u'My Project', u'year': u'2013', u'project_slug': u'myproject', u'full_name': u'Firstname Lastname'}}
    assert (load(replay_dir, template_name)==expected_answer)
    

# Generated at 2022-06-13 18:48:00.297496
# Unit test for function dump
def test_dump():
    replay_dir = "/tmp/cookiecutter_replay/test_dump"
    template_name = "_index.rst"
    context = {'cookiecutter': {'date': '2017-10-30-20-28'}}
    dump(replay_dir, template_name, context)
    assert os.path.exists(get_file_name(replay_dir, template_name))
    try:
        dump("/tmp/cookiecutter_replay", "", "")
        assert False
    except TypeError:
        assert True
    except ValueError:
        assert False
    except IOError:
        assert False



# Generated at 2022-06-13 18:48:02.978979
# Unit test for function load
def test_load():
    """Test function load"""
    context = load('/Users/chriswu/Documents/GitHubs/cookiecutter-pytorch-module', 'cookiecutter.json')
    assert context is not None
    assert 'module_name' in context['cookiecutter']


# Generated at 2022-06-13 18:48:11.564968
# Unit test for function dump
def test_dump():
    # Set up the input
    replay_dir = "/Users/gongyinan/Desktop/test"
    template_name = "template"
    context = {"cookiecutter": {"full_name": "Gong Yinan"}}
    # Do the test
    dump(replay_dir, template_name, context)
    # Check the result
    file_path = get_file_name(replay_dir, template_name)
    with open(file_path, 'r') as input_file:
        data = json.load(input_file)
    assert(data["cookiecutter"]["full_name"] == "Gong Yinan")


# Generated at 2022-06-13 18:48:14.732489
# Unit test for function load
def test_load():
    replay_file = 'C:\\Users\\Administrator\\Desktop\\cookiecutter-pypackage\\cookiecutter.json'    
    with open(replay_file, 'r') as infile:
        context = json.load(infile)
    print(context)


# Generated at 2022-06-13 18:48:20.025491
# Unit test for function dump
def test_dump():
    cwd = os.getcwd()
    replay_dir = os.path.join(cwd, 'cookiecutter-replay')
    template_name = 'CookiecutterTest'
    context = {'cookiecutter': {'name': 'CookiecutterTest'}}
    dump(replay_dir, template_name, context)
    replay_file = get_file_name(replay_dir, template_name)
    os.remove(replay_file)
    os.rmdir(replay_dir)
