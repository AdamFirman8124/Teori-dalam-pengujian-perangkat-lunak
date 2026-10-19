

# Generated at 2022-06-13 18:38:11.007299
# Unit test for function load
def test_load():
    context = load('/home/jovyan/adb/cookiecutter/replay/','space_server/cookiecutter.json')
    #print(context)
    print(repr(context))
    print(context['cookiecutter']['project_slug'])

#test_load()

# Generated at 2022-06-13 18:38:13.694209
# Unit test for function load
def test_load():
    """Test function load."""
    context=load(r"D:\programming\cookiecutter\cookiecutter\tests\test-replay",
                 'test_template')
    print(context)
    
    

# Generated at 2022-06-13 18:38:23.243055
# Unit test for function dump
def test_dump():
    """Unit test for function dump."""
    from cookiecutter import replay
    context={}
    context["cookiecutter"]={}
    context["cookiecutter"]["full_name"]="The Cookiecutter Developers"
    context["cookiecutter"]["email"]="dev@cookiecutter.com"
    context["cookiecutter"]["github_username"]="cookiecutter"
    context["cookiecutter"]["project_name"]="Cookiecutter"
    context["cookiecutter"]["project_slug"]="cookiecutter"
    context["cookiecutter"]["project_short_description"]="A command-line utility that creates projects from cookiecutters (project templates)."
    context["cookiecutter"]["pypi_username"]="cookiecutter"
    context["cookiecutter"]["version"]

# Generated at 2022-06-13 18:38:30.365828
# Unit test for function load
def test_load():
    import json
    import os
    import random
    import string
    import tempfile

    # Generate input file
    dirpath = tempfile.mkdtemp()
    filename = ''.join([random.choice(string.ascii_lowercase) for i in range(8)])
    filename = os.path.join(dirpath, filename)
    with open(filename, 'w') as fout:
        json_data = {'cookiecutter': {'name': 'dummy'}}
        json.dump(json_data, fout)

    # Test
    context = load(dirpath, filename)
    assert context['cookiecutter']['name'] == 'dummy'

    # Cleanup
    os.unlink(filename)
    os.rmdir(dirpath)

# Generated at 2022-06-13 18:38:33.501219
# Unit test for function load
def test_load():
    with open('./tests/fake-repo/cookiecutter.json', 'r') as infile:
        context = json.load(infile)
    assert isinstance(replay.load('./tests/fake-repo/', 'tests/fake-repo'), dict) == True



# Generated at 2022-06-13 18:38:39.940501
# Unit test for function load
def test_load():
    replay_dir = '~/.cookiecutters'
    template_name = 'cookiecutter-pypackage'
    context = {}

    replay_file = get_file_name(replay_dir, template_name)
    with open(replay_file, 'r') as infile:
        context = json.load(infile)

    assert 'cookiecutter' in context, "Context should contain a cookiecutter key for dump function"
    return None


# Generated at 2022-06-13 18:38:45.200644
# Unit test for function dump
def test_dump():
    replay_dir = './tests/test-replay'
    template_name = 'test'
    context = {'project_name':'foobar', 'cookiecutter':{'version':'1.0'}}
    dump(replay_dir, template_name, context)
    data = load(replay_dir, template_name)
    assert context == data


# Generated at 2022-06-13 18:38:49.158222
# Unit test for function load
def test_load():
    context = load('test_data', 'test_data\\cookiecutter.json')
    assert isinstance(context, dict)
    assert 'cookiecutter' in context
    assert isinstance(context['cookiecutter'], dict)
    assert 'project_name' in context['cookiecutter']
    assert isinstance(context['cookiecutter']['project_name'], str)

# Generated at 2022-06-13 18:38:53.860685
# Unit test for function load
def test_load():
    context = load('./', 'replay')
    assert 'cookiecutter' in context
    assert 'cookiecutter' in context['cookiecutter']

if __name__ == '__main__':
    test_load()

# Generated at 2022-06-13 18:39:00.245108
# Unit test for function dump
def test_dump():
    replay_dir = 'C:\\TMP\\ccreplay'
    template_name = 'TEST'
    dump(replay_dir, template_name, {'cookiecutter': 'abcd'})
    if os.path.exists(get_file_name(replay_dir, template_name)):
        os.remove(get_file_name(replay_dir, template_name))


# Generated at 2022-06-13 18:39:06.150618
# Unit test for function load
def test_load():
    """Test loading a replay file."""
    replay_dir = '/tmp/cookiecutter_load_test'
    template_name = 'name_load_test'
    context = {'cookiecutter': {'name': 'Chocolate Chip'}}
    dump(replay_dir, template_name, context)
    replay = load(replay_dir, template_name)
    assert replay == context



# Generated at 2022-06-13 18:39:10.245578
# Unit test for function dump
def test_dump():
    replay_dir = './tests/files/replay'
    template_name = 'cookiecutter-pypackage'
    context = {'cookiecutter': {'full_name': 'Your Name'}}
    dump(replay_dir, template_name, context)
    new_context = load(replay_dir, template_name)
    assert new_context == context


# Generated at 2022-06-13 18:39:13.556652
# Unit test for function load
def test_load():
    from cookiecutter import replay
    replay_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'tests', 'test-replay'))
    template_name = "test-template"
    context = replay.load(replay_dir, template_name)
    print(context["cookiecutter"])



# Generated at 2022-06-13 18:39:19.937757
# Unit test for function load
def test_load():
    """
    testing load function
    """
    replay_dir = '../cookiecutter'
    template_name = "example/cookiecutter.json"

    context = load(replay_dir, template_name)
    print("Testing load()")
    print("Is 'cookiecutter' in context: {}".format('cookiecutter' in context))
    return


if __name__ == "__main__":
    test_load()

# Generated at 2022-06-13 18:39:23.430874
# Unit test for function load
def test_load():
    replay_dir = "D:/cookiecuttertest"
    template_name = "D:/cookiecuttertest/cookiecutter-pypackage"
    context = load(replay_dir, template_name)
    print(context)


# Generated at 2022-06-13 18:39:24.363527
# Unit test for function load
def test_load():
    context = load(os.getcwd(), template_name='')
    assert context == {}

# Generated at 2022-06-13 18:39:31.423180
# Unit test for function load
def test_load():
    import os
    import json
    import shutil

    tmp_dir = '/home/mdalponte/fake_template'
    tmp_replay = '{}/replay'.format(tmp_dir)

    if os.path.exists(tmp_dir):
        shutil.rmtree(tmp_dir)

    os.mkdir(tmp_dir)

    f = open("{}/fake_file.json".format(tmp_replay), "w")
    f.write("{\"cookiecutter\": {\"fake_key\": \"fake_value\"}}")
    f.close()

    load_result = load(tmp_replay, 'fake_file')
    assert  load_result['cookiecutter']['fake_key'] == 'fake_value'

# Generated at 2022-06-13 18:39:36.721491
# Unit test for function load
def test_load():
    replay_dir = os.path.expanduser("~/.cookiecutters/")
    template_name = 'gh:hackebrot/cookiecutter-pypackage-minimal'
    context = load(replay_dir, template_name)
    print(context)


# Generated at 2022-06-13 18:39:40.698443
# Unit test for function load
def test_load():
    """Test the function load."""
    # TODO: create valid replay file
    replay_dir = "C:\\Users\\mswad\\Desktop\\Cookiecutter\\cookiecutter-pypackage-minimal-master\\hooks"
    template_name = "cookiecutter_example_dict.json"
    context = load(replay_dir, template_name)
    print(context)
    print(type(context))

# Generated at 2022-06-13 18:39:45.004339
# Unit test for function load
def test_load():
    replay_dir = 'replay'
    template_name = 'cookiecutter-pypackage'
    context = load(replay_dir, template_name)
    assert context['cookiecutter']['project_name'] == 'My Test Project'

# Generated at 2022-06-13 18:39:56.919201
# Unit test for function load
def test_load():
    """Tests function load."""

    # Test invalid argument types
    with pytest.raises(TypeError):
        load(None, None)
    with pytest.raises(TypeError):
        load(0, 0)
    with pytest.raises(TypeError):
        load({}, {})
    with pytest.raises(TypeError):
        load([], [])
    with pytest.raises(TypeError):
        load('', '')
    with pytest.raises(TypeError):
        load(1.1, 1.1)
    with pytest.raises(TypeError):
        load(True, True)
    with pytest.raises(TypeError):
        load([1,2,3], [1,2,3])

    # Test positive path

# Generated at 2022-06-13 18:40:08.403383
# Unit test for function dump
def test_dump():
    from unittest import TestCase, mock
    from cookiecutter import replay

    class Mock_load(TestCase):

        @classmethod
        def setUpClass(cls):
            cls.replay_dir = 'path/to/replay_dir'
            cls.template_name = 'template'
            cls.context = {'cookiecutter': {'project_name': 'test_dump'}}

        def test_get_file_name(self):
            """_get_file_name return a valid file name"""
            file_name = replay._get_file_name(self.replay_dir, self.template_name)
            if file_name:
                self.assertIs(type(file_name), str)
            else:
                self.fail("File name is invalid.")


# Generated at 2022-06-13 18:40:11.505986
# Unit test for function load
def test_load():
    """Unit test for function load."""
    print(load(os.path.join(os.path.expanduser('~'), '.cookiecutters'), 'cookiecutter-pypackage'))

# Generated at 2022-06-13 18:40:21.091100
# Unit test for function load
def test_load():
    replay_dir = 'test_replay_dir'
    template_name = 'test_template_name'
    replay_file = get_file_name(replay_dir, template_name)
    test_context = {
        'cookiecutter': {
            'full_name': 'Test Name',
            'email': 'test@mail.com',
            'project_name': 'test_project_name',
            'project_slug': 'test-project-name',
            'project_url': 'https://github.com/test/test_project_name'
        }
    }
    with open(replay_file, 'w') as outfile:
        json.dump(test_context, outfile, indent=2)
    context = load(replay_dir, template_name)
    assert context == test_context

# Generated at 2022-06-13 18:40:23.432351
# Unit test for function load
def test_load():
    replay_dir = "/Users/xianan/PycharmProjects/cookiecutter/tests/"
    template_name = "test_template"
    context = load(replay_dir, template_name)
    print(context)



# Generated at 2022-06-13 18:40:24.621476
# Unit test for function dump
def test_dump():
    assert(False)


# Generated at 2022-06-13 18:40:26.886610
# Unit test for function load
def test_load():
    replay_dir = "./tests/test-replay"
    template_name = "test-template"
    context = load(replay_dir, template_name)
    print(context)

if __name__ == "__main__":
    test_load()

# Generated at 2022-06-13 18:40:39.427852
# Unit test for function load
def test_load():
    """Unit test for function load."""
    # create test data
    replay_dir = '.cookiecutter-replay'
    template_name = './cookiecutter-pypackage'

# Generated at 2022-06-13 18:40:47.189708
# Unit test for function load
def test_load():
    cur_dir = os.getcwd()
    test_dir = os.path.join(cur_dir, 'tests', 'files', 'default')
    replay_dir = os.path.join(test_dir, 'replay')
    replay_file = os.path.join(replay_dir, 'replay.json')
    try:
        context = load(replay_dir, 'replay')
        assert os.path.exists(replay_file) == True
        assert 'cookiecutter' in context
    finally:
        if os.path.exists(replay_file):
            os.remove(replay_file)


# Generated at 2022-06-13 18:40:50.889934
# Unit test for function load
def test_load():
    replay_dir = os.path.join(os.path.expanduser('~'), '.cookiecutters')
    template_name = 'cookiecutter-pypackage'
    context = load(replay_dir, template_name)
    print(context)

# Generated at 2022-06-13 18:41:00.618312
# Unit test for function dump
def test_dump():
    FILE_DIR = os.path.dirname(os.path.abspath(__file__))
    TEST_FILE_DIR = os.path.join(FILE_DIR, 'test_files', 'replay')
    replay_dir = os.path.join(TEST_FILE_DIR, 'tmp')
    template_name = 'test_template1.json'

    context = {'cookiecutter': {'full_name': 'Sam'}}

    if os.path.exists(replay_dir):
        os.rmdir(replay_dir)
    dump(replay_dir, template_name, context)
    assert os.path.exists(replay_dir)

    replay_file = get_file_name(replay_dir, template_name)

# Generated at 2022-06-13 18:41:02.777552
# Unit test for function load
def test_load():
    data = load(
        replay_dir='./tests/fixtures', template_name='mock.json')
    assert isinstance(data, dict)
    assert 'cookiecutter' in data

# Generated at 2022-06-13 18:41:07.403776
# Unit test for function dump
def test_dump():
    replay_dir = '/Users/jadeshi/Documents/Github/cookiecutter/tests/test-replay'
    template_name = 'replay_test'
    context = {'cookiecutter': {'full_name': 'Jade Shi', 'email': 'jade.shi16@gmail.com', 'github_username': 'jadeshi'}}

    dump(replay_dir, template_name, context)


# Generated at 2022-06-13 18:41:11.542099
# Unit test for function dump
def test_dump():
    """Testing for dump function."""
    a = {
        'cookiecutter': {
            'project_name': 'Foo',
            'project_slug': 'foo',
            'repo_name': 'audreyr/cookiecutter-pypackage',
            'timezone': 'America/Los_Angeles',
            'year': '2015'
        }
    }
    dump('replay', 'foodir', a)
    with open('replay/foodir.json', 'r') as outfile:
        b = json.load(outfile)
        assert a == b



# Generated at 2022-06-13 18:41:21.631008
# Unit test for function load
def test_load():

    from cookiecutter import utils

    test_dir = utils.get_project_dir('tests', 'fixtures', 'fake-repo-pre')
    template_name = 'fake-repo-pre'

# Generated at 2022-06-13 18:41:29.207486
# Unit test for function dump
def test_dump():
    replay_dir = os.path.join(os.path.curdir, 'tests')
    template_name = 'cookiecutter-pypackage'
    cookiecutter = {
        'full_name': 'Audrey Roy Greenfeld',
        'email': 'audreyr@example.com',
        'github_username': 'audreyr',
        'project_name': 'cookiecutter-pypackage'
    }
    context = {'cookiecutter': cookiecutter}
    dump(replay_dir, template_name, context)


# Generated at 2022-06-13 18:41:38.015048
# Unit test for function load
def test_load():
    # mock user_config when the file is present
    template_name = 'test.json'
    replay_dir = os.path.join(os.getcwd(), 'user_config')
    assert os.path.exists(replay_dir)
    # this file path is specific to this test, so it fails
    replay_file = os.path.join(os.getcwd(), 'test_replay_file.json')
    assert not os.path.exists(replay_file)
    context = load(replay_dir, template_name)
    print(context.keys())
    assert 'cookiecutter' in context
    assert '_template' in context['cookiecutter']
    assert template_name == context['cookiecutter']['_template']

if __name__ == '__main__':
    test

# Generated at 2022-06-13 18:41:43.892728
# Unit test for function load
def test_load():
    with open('tests/test_context.json', 'r') as infile:
        expected = json.load(infile)
    result = load('.', 'tests/test_context.json')
    for k, v in result.items():
        if isinstance(v, str):
            assert v == expected[k]


if __name__ == "__main__":
    test_load()

# Generated at 2022-06-13 18:41:46.303705
# Unit test for function load
def test_load():
    """Test load!"""
    path = "/Users/LukeWang/Documents/Hack/Python/cookiecutter/replay/tmp.json"
    context = load(path)
    print(context)

# Generated at 2022-06-13 18:41:49.903776
# Unit test for function load
def test_load():
    """Unit test for function load."""
    template_name= "template_name.json"
    replay_file = get_file_name(template_name)

    context = load(replay_file)
    assert context is not None

# Generated at 2022-06-13 18:41:55.339953
# Unit test for function dump
def test_dump():
    replay_dir = '~/.cookiecutters/sample_cookiecutter'
    template_name = 'cookiecutter-pypackage'
    context = {
        'cookiecutter': {
            'foo': 'bar'
        }
    }

    dump(replay_dir, template_name, context)

    # Remove the just created file to keep the test function clean
    os.remove(replay_file)


# Generated at 2022-06-13 18:42:03.620953
# Unit test for function load
def test_load():
    replay_dir = '/home/vagrant/cookiecutter-pypackage'
    template_name = 'cookiecutter-pypackage'
    expected = load(replay_dir, template_name)
    assert type(expected) == dict
    assert len(expected) == 2
    assert 'cookiecutter' in expected
    assert '_template' in expected
    assert type(expected['cookiecutter']) == dict
    assert len(expected['cookiecutter']) == 1
    assert 'project_slug' in expected['cookiecutter']
    

# Generated at 2022-06-13 18:42:07.229764
# Unit test for function dump
def test_dump():
    """Unit test for function dump."""
    # Initiate a dict of input info
    context = {'cookiecutter': '{{cookiecutter}}'}
    dump('/tmp', 'test', context)

    # Get the output
    output = open('/tmp/test.json').read()

    # Compare output with expected result
    assert output == json.dumps(context, indent=2)



# Generated at 2022-06-13 18:42:16.029836
# Unit test for function load
def test_load():
    # Create a valid JSON file
    context = {'cookiecutter': {'project_name': 'project', 'project_slug': 'project'}}
    file_name = 'file'
    replay_dir = '.'
    dump(replay_dir, file_name, context)

    # Attempt to load a non-existent file
    try:
        load(replay_dir, 'asdf')
        assert False, 'load passed with a non-existent file'
    except (IOError, ValueError) as e:
        pass

    # Attempt to load a valid JSON file
    json_dict = load(replay_dir, file_name)
    assert json_dict == context, "load failed with a valid JSON file"


# Generated at 2022-06-13 18:42:19.416427
# Unit test for function dump
def test_dump():
    """Test function dump"""
    replay_dir = './'
    template_name = 'test_template'
    context = {'cookiecutter':{'name':'test'}}
    dump(replay_dir, template_name, context)
    assert os.path.isfile(get_file_name(replay_dir, template_name))
    os.remove(get_file_name(replay_dir, template_name))


# Generated at 2022-06-13 18:42:24.428866
# Unit test for function dump
def test_dump():
    replay_dir = 'tests/test-output/replay'
    template_name = 'tests/fake-repo-tmpl'
    context = {
        'cookiecutter': {
            'full_name': 'Your Name',
            'email': 'your@email.com',
        }
    }
    dump(replay_dir, template_name, context)



# Generated at 2022-06-13 18:42:32.508411
# Unit test for function dump
def test_dump():
    replay_dir = './tests/test-replay'
    template_name = 'test-template'
    context = {
        'cookiecutter': {
            'test': {
                'test1': 'test1',
                'test2': 'test2'
            }
        }
    }
    dump(replay_dir, template_name, context)
    check_file = get_file_name(replay_dir, template_name)
    with open(check_file, 'r') as check:
        check_list = check.read().splitlines()
    # context_list = json.dump(context, indent=2).splitlines()
    # print(context_list)

# Generated at 2022-06-13 18:42:38.159445
# Unit test for function dump
def test_dump():
    """Unit test for function dump."""
    from tempfile import TemporaryDirectory

    template_name = 'test'
    context = {'cookiecutter': {'full_name': 'Jane Doe'}}

    with TemporaryDirectory() as replay_dir:
        file_name = get_file_name(replay_dir, template_name)
        dump(replay_dir, template_name, context)
        with open(file_name, 'r') as f:
            assert json.load(f) == context


# Generated at 2022-06-13 18:42:40.937794
# Unit test for function load
def test_load():
    template_name='cookiecutter-pypackage'
    context=load('{}/..'.format(os.getcwd()),template_name)
    assert 'cookiecutter' in context

# Generated at 2022-06-13 18:42:46.095829
# Unit test for function load
def test_load():
    print('Testing load')
    replay_file = 'replay_data.json'
    template_name = 'replay_data'
    replay_dir = '.'
    context = load(replay_dir, template_name)
    print(context)


# Generated at 2022-06-13 18:42:52.734042
# Unit test for function load
def test_load():
    context = load('.','test_data')
    assert context

# Generated at 2022-06-13 18:42:58.476855
# Unit test for function load
def test_load():
    replay_file = 'cupcake-django/cookiecutter.json'
    # TODO: don't hardcode replay_file

# Generated at 2022-06-13 18:43:08.703899
# Unit test for function dump
def test_dump():
    replay_dir = "tests/replay"
    template_name = "default_context"
    context = {"cookiecutter": {"full_name": "Monty Python", "email": "monty@python.com", "github_username": "montypython", "project_name": "cookiecutter-pypackage", "project_slug": "cookiecutter-pypackage", "release_date": "2014/10/18", "project_short_description": "A Python package project template", "pypi_username": "audreyr", "version": "0.1.0", "create_author_file": "y", "use_pypi_deployment_with_travis": "y", "command_line_interface": "Click", "open_source_license": "MIT license"}}

# Generated at 2022-06-13 18:43:14.502176
# Unit test for function load
def test_load():
    try:
        a = load('', 1)
    except TypeError as e:
        print(e)
    try:
        a = load('', 'test_tpl')
        assert 'cookiecutter' in a.keys()
    except ValueError as e:
        print('exception')
    else:
        print(a)


if __name__ == '__main__':
    test_load()

# Generated at 2022-06-13 18:43:17.387460
# Unit test for function load
def test_load():
    for cookie in range(1,4):
        for cake in range(1,4):
            assert "cookie" in load("../", "cookie="+str(cookie)+"cake="+str(cake))

# Generated at 2022-06-13 18:43:24.884008
# Unit test for function load
def test_load():
    print("Begin Unit test for function load")
    replay_dir = '.'
    template_name = 'abc.json'
    file_name = get_file_name(replay_dir, template_name)
    print("File name: ", file_name)
    if os.path.isfile(file_name):
        os.remove(file_name)
    if os.path.isfile(file_name):
        print("Failed to delete the original abc.json file ", file_name)
    else:
        print("Successfully deleted the original abc.json file")
    print("Begin to test try-except block with empty abc.json file")
    try:
        load(replay_dir, template_name)
    except ValueError as e:
        print("Exception raised: ", e)

# Generated at 2022-06-13 18:43:32.126026
# Unit test for function dump
def test_dump():
    '''Test the dump function from the replay.py file
    '''
    template_name = 'example'
    context = {'cookiecutter': {'project_name': 'Example'}}

    # Create a temporary directory to test the function
    try:
        os.mkdir('test_dump')

        # Test the function
        dump('test_dump', template_name, context)

        # Read the replay file and check if the written context is equal to the context to be written
        with open('test_dump/example.json', 'r') as infile:
            written_context = json.load(infile)

        assert context == written_context

    finally:
        # Remove the replay file
        os.remove('test_dump/example.json')
        # Remove the directory that was created for testing

# Generated at 2022-06-13 18:43:38.256641
# Unit test for function load
def test_load():
    template_name = 'python-cli'
    # replay_dir = os.path.expanduser('~/.cookiecutter_replay')
    replay_dir = os.path.join(os.path.dirname(__file__), '.cookiecutter_replay')

    context = load(replay_dir, template_name)
    print(context)


# Generated at 2022-06-13 18:43:43.607525
# Unit test for function load
def test_load():
    replay_context = load('./tests/playback', 'replay_test')

    # Assert that context is a dictionary
    assert isinstance(replay_context, dict)

    # Assert that cookiecutter key exists in context
    assert 'cookiecutter' in replay_context

    # Assert that cookiecutter key is also a dictionary
    assert isinstance(replay_context['cookiecutter'], dict)



# Generated at 2022-06-13 18:43:45.221347
# Unit test for function load
def test_load():
    """Unit test for function load"""

# Generated at 2022-06-13 18:44:00.491617
# Unit test for function load
def test_load():
    # Make sure file exists
    try:
        load("", "test_file")
    except IOError as e:
        assert "Unable to open replay file at " in str(e)

    # Make sure file is json
    try:
        load(os.getcwd(), "README.rst")
    except ValueError as e:
        assert "Context read from replay file must be a JSON object" in str(e)

    # Make sure file has cookiecutter key
    try:
        load(os.getcwd(), "test_file")
    except ValueError as e:
        assert "Context is required to contain a cookiecutter key" in str(e)


# Generated at 2022-06-13 18:44:09.458943
# Unit test for function load
def test_load():
    # Create a replay_dir
    replay_dir = 'tests/test-load-replay-dir'
    template_name = 'test-load-template'
    template_file = 'tests/test-load-template.json'
    make_sure_path_exists(replay_dir)
    os.system('cp {} {}/{}.json'.format(template_file, replay_dir, template_name))
    context = load(replay_dir, template_name)

    # Check the context
    assert(isinstance(context, dict))
    assert(context['cookiecutter']['full_name'] == 'John Doe')

    # Remove the replay_dir
    os.system('rm -rf {}'.format(replay_dir))


# Generated at 2022-06-13 18:44:15.069192
# Unit test for function load
def test_load():
    template_file_name = 'cookiecutter.json'
    template_file = 'test/test_cookiecutterjson/' + template_file_name
    replay_file_name = 'test/test_replayjson/test_template.json'

    with open(template_file, 'r') as infile:
        context = json.load(infile)

    with open(replay_file_name, 'r') as infile:
        replay_context = json.load(infile)

    load_context = load(replay_file_name)
    assert load_context == replay_context

test_load()

# Generated at 2022-06-13 18:44:17.514315
# Unit test for function load
def test_load():
    """Unit test for load."""
    assert(load('/home/chenjianfeng/ROS/tmp/ros_templates', 'src_template.json'))

# Generated at 2022-06-13 18:44:25.297574
# Unit test for function dump
def test_dump():
    replay_dir = 'tests/files/replay'
    template_name = 'tests/files/fake-repo-pre/{{cookiecutter.project_name}}'
    context = {'cookiecutter': {'project_name': 'foobar', 'repo_name': 'baz'}}
    dump(replay_dir, template_name, context)

    try:
        os.remove(get_file_name(replay_dir, template_name))
    except:
        print('Unable to delete file: {}'.format(get_file_name(replay_dir, template_name)))


# Generated at 2022-06-13 18:44:28.916551
# Unit test for function load
def test_load():
    with open('test_replay_context.json', 'r') as infile:
        context = json.load(infile)

    if 'cookiecutter' not in context:
        raise ValueError('Context is required to contain a cookiecutter key')
    print(context)

test_load()

# Generated at 2022-06-13 18:44:33.487130
# Unit test for function load
def test_load():
    assert load('/Users/r/notebooks/cookiecutter-project/tests/test_replay', 'basic_project') == {
  "cookiecutter": {
    "description": "A basic project",
    "full_name": "Audrey Roy",
    "email": "audreyr@example.com",
    "project_name": "Basic Project",
    "project_slug": "basic_project",
    "version": "0.1.0",
    "release": "y"
  }
}

# Generated at 2022-06-13 18:44:42.332165
# Unit test for function load
def test_load():
    """Unit test for function load"""
    from cookiecutter import replay
    from cookiecutter import utils
    import os
    import shutil
    # Create a folder for save replay file
    replay_dir = os.path.join(os.path.dirname(__file__), 'files', 'replay')
    context = {
        'cookiecutter': {
            'full_name': 'Audrey Roy',
            'email': 'audreyr@example.com',
            'project_name': 'Cookiecutter Example Project',
            'project_slug': 'cookiecutter-example-project',
            'release_date': '2014-04-01',
        }
    }
    # Write context to file
    replay.dump(replay_dir, 'cookiecutter-example-project', context)
    # Test load

# Generated at 2022-06-13 18:44:42.830272
# Unit test for function load
def test_load():

    context = load('', '')
    assert context

# Generated at 2022-06-13 18:44:47.929874
# Unit test for function load
def test_load():
    context1 = load('/Users/mengxi/Downloads/cookiecutter-pypackage/tests/test-repo-pre/', 'test-repo-pre')
    print(context1)
    assert context1['cookiecutter']['project_name'] == 'Test project'
    assert context1['cookiecutter']['full_name'] == 'audreyr'
    assert context1['cookiecutter']['email'] == 'audreyr@example.com'
    assert context1['cookiecutter']['github_username'] == 'audreyr'
    assert context1['cookiecutter']['project_name'] == 'Test project'


# Generated at 2022-06-13 18:45:10.912590
# Unit test for function load
def test_load():
    replay_file = 'tests/test-load.txt'
    context = load('tests/', replay_file)
    assert context == {'cookiecutter': {}}



# Generated at 2022-06-13 18:45:15.008140
# Unit test for function dump
def test_dump():
    replay_dir = 'tmp/replay'
    template_name = 'tmp'

    context = {
        'cookiecutter': {
            'full_name': 'test user',
            'email': 'test@user.com',
            'github_username': 'testuser',
            'project_name': 'test project'
        }
    }

    try:
        dump(replay_dir, template_name, context)
        assert True
    except:
        assert False


# Generated at 2022-06-13 18:45:19.470035
# Unit test for function load
def test_load():
    context = load("/Users/tianyuan/Downloads/repos-master/cookiecutter-pypackage-minimal", "cookiecutter-pypackage-minimal")
    print(context)

if __name__ == "__main__":
    test_load()

# Generated at 2022-06-13 18:45:21.226279
# Unit test for function load
def test_load():
    assert load('replay/foo', 'foos') == {'cookiecutter': {}}

# Generated at 2022-06-13 18:45:31.091657
# Unit test for function dump
def test_dump():
    "Testing function dump."
    test_dir = os.path.join(os.getcwd(), 'test_dir')
    try:
        os.rmdir(test_dir)
    except OSError:
        pass
    template_name = 'template'
    context = {'cookiecutter': {}}
    context['cookiecutter']['cookiecutter_demo_user_name'] = 'Cookie Cutter'
    context['cookiecutter']['cookiecutter_demo_password'] = 'password'
    dump(test_dir, template_name, context)

    with open(os.path.join(test_dir, template_name + '.json'), 'r') as log_file:
        log = log_file.read()
    

# Generated at 2022-06-13 18:45:36.313236
# Unit test for function load
def test_load():
    from nose.tools import assert_true
    from cookiecutter.utils import rmtree
    from pprint import pprint

    test_replay_dir = 'tests/files/test-replay'
    test_template_name = 'fake-project'

    rmtree(test_replay_dir, ignore_errors=True)
    context = load(test_replay_dir, test_template_name)
    pprint(context)
    assert_true(False)



# Generated at 2022-06-13 18:45:42.227809
# Unit test for function load
def test_load():
    working_dir = os.getcwd()
    replay_dir = working_dir + "/cookiecutter-data/replay"

    context = load(replay_dir, "feature_tests/get_started_basic")

    assert isinstance(context, dict)
    assert 'cookiecutter' in context



# Generated at 2022-06-13 18:45:52.962714
# Unit test for function dump
def test_dump():
    replay_dir = os.path.join('tests', 'test-output', 'replay')
    template_name = 'example-repo'
    context = {
        'cookiecutter': {
            'full_name': 'Cookiecutter',
            'email': 'your-email@example.com',
            'github_username': 'your-github-username',
            'project_name': 'Example Repo',
            'project_slug': 'example_repo',
            'use_pytest': 'y',
            'use_pypi_deployment_with_travis': 'y',
            'command_line_interface': 'click',
            'open_source_license': 'MIT license',
            'pypi_username': 'your-pypi-username',
        }
    }


# Generated at 2022-06-13 18:45:55.577169
# Unit test for function load
def test_load():
    context = load(template_name='cookiecutter-pypackage', replay_dir= 'C:\\Users\\souman_kundu\\PycharmProjects\\cookiecutter-pypackage')
    print(context)

test_load()

# Generated at 2022-06-13 18:46:02.805678
# Unit test for function load
def test_load():
    replay_file = get_file_name("tests/files", "cookiecutter.json")
    with open(replay_file, 'r') as infile:
        context = json.load(infile)
    assert(context["cookiecutter"]["full_name"] == "Your Name")
    assert(context["cookiecutter"]["email"] == "your@email.com")
    assert(context["cookiecutter"]["github_username"] == "yourname")
    assert(context["cookiecutter"]["project_name"] == "project_name")
    assert(context["cookiecutter"]["project_slug"] == "project_slug")
    assert(context["cookiecutter"]["project_short_description"] == "project_short_description")

# Generated at 2022-06-13 18:46:53.793073
# Unit test for function dump
def test_dump():
    r = {}
    r['cookiecutter'] = {}
    r['cookiecutter']['full_name'] = 'Piotr Uszok'
    r['cookiecutter']['short_name'] = 'peter'
    r['cookiecutter']['description'] = 'A short description of the project.'

    dump('replay', 'cookiecutter-pypackage', r)

# Generated at 2022-06-13 18:46:56.403025
# Unit test for function load
def test_load():
    replay_dir = './tests/fake-repo/'
    template_name = 'foobar'
    context = load(replay_dir, template_name)

    assert isinstance(context, dict)

# Generated at 2022-06-13 18:46:57.738500
# Unit test for function dump
def test_dump():
    replay_dir = 'test_replay_dir'
    template_name = 'test_template'
    dump(replay_dir, template_name, {})


# Generated at 2022-06-13 18:46:58.098371
# Unit test for function load
def test_load():
    pass

# Generated at 2022-06-13 18:46:59.537878
# Unit test for function load
def test_load():
    load("./cookiecutter.replay", "cookiecutter-pypackage")


# Generated at 2022-06-13 18:47:01.304216
# Unit test for function load
def test_load():
    """ """
    #dump(context)
    context = load("../test_replay/", "test_cookiecutter")
    print(context)



# Generated at 2022-06-13 18:47:05.997911
# Unit test for function load
def test_load():
    # Should raise error if template_name is not a string
    try:
        load('great_name', 123456)
    except TypeError:
        pass
    
    # Should return the correct json data
    try:
        context = load('great_name', 'test_template')
    except TypeError:
        pass
    assert(isinstance(context, dict))
    assert('cookiecutter' in context)

    # Should raise error if cookiecutter key is not present
    try:
        load('great_name', 'test_template2')
    except ValueError:
        pass


# Generated at 2022-06-13 18:47:14.605237
# Unit test for function load
def test_load():
    import sys
    import unittest


    class ReplayTests(unittest.TestCase):
        def setUp(self):
            self.replay_file = os.path.join(os.path.dirname(__file__), 'replay_file.json')
            self.replay_dir = os.path.dirname(__file__)
            self.template_name = 'replay_file.json'
            self.context = {'cookiecutter': {'key1': 'value1'},
                            'key2': 'value2'}

        def test_load_type_error(self):
            """Test the load function raises TypeError if the template name is not of type str."""
            with self.assertRaises(TypeError) as err:
                load(self.replay_dir, 1)



# Generated at 2022-06-13 18:47:20.144359
# Unit test for function load
def test_load():
    replay_dir = os.path.join(os.path.dirname(__file__), 'replays')
    template_name = 'c_template'
    context = load(replay_dir, template_name)
    assert context['cookiecutter']['project_name'] == 'c-project'

if __name__ == "__main__":
    test_load()

# Generated at 2022-06-13 18:47:25.320380
# Unit test for function load
def test_load():
    replay_dir = os.getcwd()
    template_name = 'test_load'
    context = {'cookiecutter': 'test_1'}
    replay_file = get_file_name(replay_dir, template_name)
    with open(replay_file, 'w') as outfile:
        json.dump(context, outfile, indent=2)

    context_new = load(replay_dir, template_name)
    assert context_new == context
    os.remove(replay_file)
