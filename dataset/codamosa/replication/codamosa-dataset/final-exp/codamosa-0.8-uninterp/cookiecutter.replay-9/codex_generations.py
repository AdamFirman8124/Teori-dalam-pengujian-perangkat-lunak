

# Generated at 2022-06-13 18:38:14.983509
# Unit test for function load
def test_load():
    import json
    import json.decoder as decoder
    import os
    import shutil
    import tempfile

    test_dir = tempfile.mkdtemp()
    replay_dir = os.path.join(test_dir, 'cookiecutter', 'replay')
    os.makedirs(replay_dir)
    template_name = 'python_name'
    replay_file = get_file_name(replay_dir, template_name)
    assert os.path.isdir(replay_dir)
    assert os.path.isfile(replay_file) == False
    context = {'cookiecutter': {'full_name': 'Anupam Ghosh',
                                'github_username': 'anupamoipai'}}
    dump(replay_dir, template_name, context)

# Generated at 2022-06-13 18:38:24.460300
# Unit test for function load
def test_load():
    """Test load function."""
    context = {}
    context['cookiecutter'] = {}
    context['cookiecutter']['full_name'] = 'Duc Tran'
    context['cookiecutter']['email'] = 'drunkencoder@hotmail.com'
    context['cookiecutter']['project_name'] = 'aws-lambda-apache-cx-common'
    context['cookiecutter']['command_handler'] = 'get-item'
    context['cookiecutter']['package_name'] = 'aws_lambda_apache_cx_common'
    context['cookiecutter']['module'] = 'get_item'
    context['cookiecutter']['class'] = 'GetItem'
    context['cookiecutter']['class_file'] = 'get_item.py'


# Generated at 2022-06-13 18:38:30.300633
# Unit test for function dump
def test_dump():
    # Prepare the arguments
    replay_dir = 'tests/files/test-replay'
    template_name = 'test-template'
    context = {'cookiecutter': {'name': 'Test', 'version': '1.0.0'}}
    # Call the function
    dump(replay_dir, template_name, context)
    # Test if the file is created
    file_name = get_file_name(replay_dir, template_name)
    assert os.path.isfile(file_name)

# Generated at 2022-06-13 18:38:35.843240
# Unit test for function load
def test_load():
    import pytest
    from cookiecutter.utils import ensure_dir
    from cookiecutter.environment import StrictEnvironment
    from cookiecutter import main
    from cookiecutter.main import cookiecutter
    from cookiecutter.context import make_context
    from cookiecutter.exceptions import FailedHookException
    from cookiecutter.prompt import read_user_yes_no
    from cookiecutter.exceptions import NonTemplatedInputDirException
    from cookiecutter.exceptions import OutputDirectoryExistsException
    from cookiecutter import utils

    test_dir = os.path.realpath(
        os.path.join(os.path.dirname(__file__), 'files')
    )
    temp_dir = os.path.join(test_dir, 'temp')

# Generated at 2022-06-13 18:38:38.283848
# Unit test for function load
def test_load():
    replay_dir = 'C:\\Users\\francisco.paulino\\Desktop\\cookiecutterUser'
    template_name = 'v1'

    context = load(replay_dir, template_name)
    assert attr in context


# Generated at 2022-06-13 18:38:45.737433
# Unit test for function load
def test_load():
    # testing load function on a directory that doesn't exist
    try:
        load('/Users/KetakiShriram/Desktop/whatever', 'github-repo')
    except ValueError:
        pass
    else:
        raise Exception("Should have raised ValueError.")

    # testing load function on a file that doesn't exist
    try:
        load('/Users/KetakiShriram/Desktop/cookiecutter-pypackage', 'whatever')
    except ValueError:
        pass
    else:
        raise Exception("Should have raised ValueError.")



# Generated at 2022-06-13 18:38:49.881915
# Unit test for function dump
def test_dump():
    replay_dir = '/Users/akshay/Documents/cookiecutter/tests/test-replay'
    template_name = 'cookiecutter-pypackage'
    context = {'project_name':'test_project', 'cookiecutter':{'replay':True, 'no_input':True, 'extra_context':{}}}
    dump(replay_dir, template_name, context)



# Generated at 2022-06-13 18:38:58.440231
# Unit test for function dump
def test_dump():
    replay_dir = 'tests/files/test-replay'
    template_name = 'project/cookiecutter.json'
    context = {"cookiecutter": "No cookie for you"}

    dump(replay_dir, template_name, context)

    assert os.path.isfile(replay_dir + '/project/cookiecutter.json')
    try:
        os.remove(replay_dir + '/project/cookiecutter.json')
    except OSError:
        pass


# Generated at 2022-06-13 18:39:01.870330
# Unit test for function load
def test_load():
	assert (load("D:\OneDrive\Github\Cookiecutter\cookiecutter\newrepo-cookiecutter@master","cookiecutter")!=None)


# Generated at 2022-06-13 18:39:06.029705
# Unit test for function get_file_name
def test_get_file_name():
    """Unit test for function get_file_name"""
    if os.path.exists("/tmp/test_get_file_name.json"):
        os.remove("/tmp/test_get_file_name.json")
    assert get_file_name("/tmp/test_get_file_name") == "/tmp/test_get_file_name.json"



# Generated at 2022-06-13 18:39:11.173912
# Unit test for function load
def test_load():
    replay_dir = r'.\tests\test-load-replay'
    template_name = 'test-load'
    try:
        load(replay_dir, template_name)
    except ValueError as err:
        print(err)
    else:
        print("there is no cookiecutter in json file")


# Generated at 2022-06-13 18:39:16.245002
# Unit test for function load
def test_load():
    """test_load."""
    replay_dir = "test/test_file"
    template_nam = "test_file"
    context = {'cookiecutter': {'_replay_dir': replay_dir,
                                '_template_dir': template_nam,
                                'key': 'value'}}
    if (not(os.path.exists(replay_dir))):
        os.mkdir(replay_dir)
    dump(replay_dir, template_nam, context)
    context1 = load(replay_dir, template_nam)
    assert context == context1
    os.remove(get_file_name(replay_dir, template_nam))
    os.rmdir(replay_dir)


# Generated at 2022-06-13 18:39:17.147795
# Unit test for function load
def test_load():
    print(load("replay", "abi"))

# Generated at 2022-06-13 18:39:20.222790
# Unit test for function dump
def test_dump():
    template_name = 'hello.json'
    context = {'cookiecutter': {'first_name': 'Testing'}}
    dump('', template_name, context)

# Generated at 2022-06-13 18:39:22.775112
# Unit test for function load
def test_load():
    a = load('C:\source\cookiecutter-python\cookiecutter', 'cookiecutter.json')

# Generated at 2022-06-13 18:39:27.414679
# Unit test for function load
def test_load():
    # Define the path
    testfile_path = os.path.join(os.path.expanduser("~"), 'cookiecutter.json')
    # Define the json file
    json_data = open(testfile_path)
    # Reading data back
    data = json.load(json_data)
    # print(data)
    # Close the json file
    json_data.close()
    return data


# Generated at 2022-06-13 18:39:28.033051
# Unit test for function load
def test_load():
    pass

# Generated at 2022-06-13 18:39:36.024067
# Unit test for function load
def test_load():
    # Initialize the directory for the test
    replay_dir = os.path.join(os.path.expanduser('~'), '.cookiecutters')
    template_name = 'pypackage'

    # Put input data
    context = dict()
    context['cookiecutter'] = dict()
    context['cookiecutter']['full_name'] = 'Kamal Mustafa'
    context['cookiecutter']['email'] = 'sepamuty@gmail.com'
    context['cookiecutter']['project_name'] = 'django_cookiecutter'
    context['cookiecutter']['project_slug'] = 'django_cookiecutter'
    context['cookiecutter']['project_short_description'] = 'A short description'
    context['cookiecutter']['project_license']

# Generated at 2022-06-13 18:39:37.131252
# Unit test for function load
def test_load():
    load('example/{{cookiecutter.repo_name}}', 'README.rst')



# Generated at 2022-06-13 18:39:45.118054
# Unit test for function load
def test_load():
    """Test the function load."""
    test_file_name = '{{cookiecutter.project_name}}.json'
    test_file_path = 'test/test_file/'
    context = load(test_file_path, test_file_name)
    assert isinstance(context, dict)
    assert 'cookiecutter' in context


# Generated at 2022-06-13 18:39:55.045822
# Unit test for function load
def test_load():
    """
    Test for load function.
    """
    replay_dir = '/tmp/cookiecutter-replay'
    template_name = 'simple-master-detail'
    try:
        context = load(replay_dir, template_name)
    except IOError as e:
        print('Please create dir {} and put replay data in it'.format(replay_dir))
    print('context: {}'.format(context))


# Generated at 2022-06-13 18:39:57.739218
# Unit test for function load
def test_load():
    context = load(r'/home/ren/py_learn/cookiecutter-create/tests/test_files/fake-replay', 'fake-project')
    print(context)
    print(type(context))
    print(context.keys())



# Generated at 2022-06-13 18:40:01.947980
# Unit test for function load
def test_load():
    replay_dir = "/Users/angelayufan/PycharmProjects/cookiecutter-pypackage/data"
    template_name = "cookiecutter.json"
    context = load(replay_dir, template_name)
    print(context)


# Generated at 2022-06-13 18:40:04.227960
# Unit test for function load
def test_load():
    assert isinstance(load('replay_dir', 'template_name'), dict)

# Generated at 2022-06-13 18:40:07.967981
# Unit test for function dump
def test_dump():
    replay_dir = "/Users/jimmy/Desktop/test_replay"
    template_name = "test_temp"
    context = {"cookiecutter":{"a":"1"}}
    dump(replay_dir, template_name, context)



# Generated at 2022-06-13 18:40:18.117287
# Unit test for function dump
def test_dump():
    """Test the dump function."""
    # File structure
    replay_dir = './tests/files/replay_files'
    # Template name
    template_name = 'replay_file_example'
    # Context
    context = {
        "cookiecutter": {
            "full_name": "Audrey Roy Greenfeld",
            "email": "audreyr@example.com",
            "github_username": "audreyr",
            "project_name": "Example",
            "project_slug": "example",
            "release_date": "2014-10-06",
            "version": "0.1.0"
        }
    }

    dump(replay_dir, template_name, context)
    assert os.path.isfile(get_file_name(replay_dir, template_name))

# Generated at 2022-06-13 18:40:25.347620
# Unit test for function dump
def test_dump():
    """Test for function dump."""
    context = {'cookiecutter': {'name': 'test'}}
    replay_dir = 'test_dir'
    template_name = 'test'
    dump(replay_dir, template_name, context)

    assert os.path.isfile('test_dir/test.json')
    with open('test_dir/test.json') as f:
        data = json.load(f)
    assert data == context
    os.remove('test_dir/test.json')

    replay_dir = os.path.join('test_dir', 'test_dir')
    template_name = 'test'
    dump(replay_dir, template_name, context)

    assert os.path.isfile('test_dir/test_dir/test.json')

# Generated at 2022-06-13 18:40:36.858412
# Unit test for function load
def test_load():
    test_dir = 'test_dir'
    test_template_name = 'test_template'
    test_context = {'cookiecutter': {'test_key': 'test_value'}}
    if not make_sure_path_exists(test_dir):
        raise IOError('Unable to create replay dir at {}'.format(test_dir))
    dump(test_dir, test_template_name, test_context)
    loaded_context = load(test_dir, test_template_name)
    assert loaded_context == test_context
    os.remove(get_file_name(test_dir, test_template_name))
    os.removedirs(test_dir)


# Generated at 2022-06-13 18:40:46.344020
# Unit test for function dump
def test_dump():
    template_name = 'template1'
    replay_dir = '/home/kris/code/lomax_cookiecutter/test_dump'
    context = {'cookiecutter': {
            'full_name': 'kris',
            'email': 'kris@example.com',
            'project_name': 'Test1',
            'repository_name': 'test1',
            'affiliation': 'somewhere',
            'use_pytest': True,
            'use_travis': True,
            'use_sphinx': True,
            'use_devpi': True,
            'use_pyup': True,
            'use_coveralls': True,
            'use_landscape': True,
            'version': 1.0
                    }
                }

# Generated at 2022-06-13 18:40:48.392596
# Unit test for function load
def test_load():
    context = load('./', 'test_cc_replay.json')
    assert isinstance(context, dict)
    assert 'cookiecutter' in context
    assert 'full_name' in context['cookiecutter']

# Generated at 2022-06-13 18:40:51.713439
# Unit test for function load
def test_load():
    load("/Users/viktorie/Documents/Python/dev/cookiecutter/tests", "mycheese")



# Generated at 2022-06-13 18:41:00.294465
# Unit test for function load

# Generated at 2022-06-13 18:41:05.595066
# Unit test for function load
def test_load():
    template_name = 'cookiecutter-pypackage'
    replay_file = '{}-{}'.format(template_name, 'cookiecutter.json')
    replay_dir = os.path.abspath(os.path.join('tests', 'files', 'output', 'test-replay'))
    replay_file = os.path.join(replay_dir, replay_file)
    context = load(replay_dir, template_name)
    print(context)
    assert(context['cookiecutter']['package_name'] == 'test_package')
    assert(context['cookiecutter']['namespace_package_name'] == '')

# Generated at 2022-06-13 18:41:12.952655
# Unit test for function load
def test_load():
    #load(replay_dir, template_name)
    #replay_dir = 'test/test_dir'
    #template_name = 'test_template'
    # Save replay dump file
    #dump(replay_dir, template_name,{'cookiecutter':{'version':'0.7.2', 'full_name':'simon', 'email':'simon@simon.com'}})
    # Read replay dump file
    #context = load(replay_dir, template_name)
    #print(context)
    context = load('test/test_dir', 'test_template')
    print('Cookiecutter version:', context['cookiecutter']['version'])
    print('Full name:', context['cookiecutter']['full_name'])

# Generated at 2022-06-13 18:41:14.802610
# Unit test for function load
def test_load():
    assert load('./', 'test') == {'cookiecutter': {}}

test_load()

# Generated at 2022-06-13 18:41:15.763603
# Unit test for function load
def test_load():
    return



# Generated at 2022-06-13 18:41:22.876350
# Unit test for function load
def test_load():
    import pytest
    # bad file name
    template_name = 'definitely/the/wrong/name.json'
    with pytest.raises(IOError):
        load('/', template_name)
    # bad file type
    template_name = '.empty'
    with pytest.raises(TypeError):
        load('/', template_name)
    # bad file content
    template_name = 'bad_json'
    with pytest.raises(ValueError):
        load('/', template_name)

if __name__ == '__main__':
    test_load()

# Generated at 2022-06-13 18:41:26.928321
# Unit test for function load
def test_load():
    replay_dir = '../replay'
    template_name = 'evo-master'
    context = load(replay_dir, template_name)
    print(context)
    assert ('cookiecutter' in context) == True


# Generated at 2022-06-13 18:41:30.269884
# Unit test for function load
def test_load():
    replay_dir = '.'
    template_name = 'cookiecutter-pypackage'
    context = load(replay_dir, template_name)
    print(context)


if __name__ == '__main__':
    test_load()

# Generated at 2022-06-13 18:41:34.899767
# Unit test for function load
def test_load():
    replay_dir = "/home/travis/build/kst_tong/cookiecutter-drf-vue/cookiecutter.replay/"
    template_name = "drf-vue-template"
    context = load(replay_dir, template_name)
    assert context['cookiecutter']['project_name'] == 'app_name'

# Generated at 2022-06-13 18:41:45.109547
# Unit test for function load
def test_load():
    from tempfile import mkdtemp
    from shutil import rmtree

    replay_dir = mkdtemp(suffix='_cookiecutter')
    template_name = 'test'
    context = {'cookiecutter': {'project_name': 'Test'}}
    dump(replay_dir, template_name, context)
    result = load(replay_dir, template_name)
    # rmtree(replay_dir)
    assert result == context

if __name__ == "__main__":
    test_load()

# Generated at 2022-06-13 18:41:52.639250
# Unit test for function load
def test_load():
    import tempfile
    import shutil
    template_name = "TEST_DUMP"
    replay_dir = tempfile.mkdtemp()
    context = {}
    context['cookiecutter'] = {}
    context['cookiecutter']['test_load'] = 'test_load'
    dump(replay_dir, template_name, context)
    context_new = load(replay_dir, template_name)
    shutil.rmtree(replay_dir)
    assert context == context_new


# Generated at 2022-06-13 18:41:56.025722
# Unit test for function load
def test_load():
    """Test load function."""
    def _load(replay_dir, template_name):
        return context

    with mock.patch(
        'cookiecutter.replay.json.load',
        side_effect=_load
    ):
        assert replay.load('replay_dir', 'template_name') == context



# Generated at 2022-06-13 18:42:02.335268
# Unit test for function load
def test_load():
    template_name = 'test'
    replay_dir = os.path.join(os.getcwd(), 'tests/test-output/replay')
    context = load(replay_dir, template_name)
    assert type(context) == dict
    assert 'cookiecutter' in context
    assert context['cookiecutter']['project_name'] == 'Test Project'


# Generated at 2022-06-13 18:42:08.905101
# Unit test for function load
def test_load():
    """Test for function load."""
    _dir = "cc-test-replay"
    template = "example-template"
    make_sure_path_exists(_dir)
    replay_file = get_file_name(_dir, template)

    context = {"cookiecutter": {}}
    with open(replay_file, 'w') as outfile:
        json.dump(context, outfile, indent=2)

    answer = load(_dir, template)
    if answer == context:
        return True
    else:
        return False



# Generated at 2022-06-13 18:42:14.142574
# Unit test for function load
def test_load():
    
    replay_dir = "/Users/snehal/Desktop/Cookiecutter/cookiecutter_test/replay"
    template_name = "test_test"
    context = load(replay_dir,template_name)
    
    print(context)
    assert 'cookiecutter' in context
    assert context["cookiecutter"]["author_name"] == "Snehal"
    

# Generated at 2022-06-13 18:42:17.357433
# Unit test for function load
def test_load():
    replay_dir = "./cookiecutter"
    template_name = "./cookiecutter/cookiecutter.json"
    context = {"cookiecutter": {"author_email": "g@k.com"}}

    context_read = load(replay_dir, template_name)
    assert context == context_read


# Generated at 2022-06-13 18:42:23.654924
# Unit test for function load
def test_load():
    print("\nCookiecutter.replay.load()")
    context = load("replay", "cookiecutter-pypackage")
    print("Keys of context: ")
    for key in context.keys():
        print(key, ":", context[key])
    print("\n")


if __name__ == '__main__':
    test_load()

# Generated at 2022-06-13 18:42:31.823705
# Unit test for function dump
def test_dump():
    replay_dir = 'tests/files/fake-repo-pre/'
    template_name = 'fake-repo-pre'

# Generated at 2022-06-13 18:42:35.920129
# Unit test for function dump
def test_dump():
    context = {'cookiecutter': {'project_name': 'my_project', 'author_name': 'Anurag', 'author_email': 'anurag.kamble@mavs.uta.edu'}}
    dump('/tmp','temp',context)


# Generated at 2022-06-13 18:42:50.748809
# Unit test for function dump
def test_dump():
    replay_dir = r'C:\Users\Tristan\Desktop\CS4242_Coursework\cookiecutter-webdev\tests\files'
    template_name = 'test_template'
    sample_context = {'cookiecutter': {'project_name': 'Example Project',
                                       'replay_dir': replay_dir,
                                       'project_slug': 'example_project',
                                       'replay_file': 'example_project.json',
                                       'timezone': 'Europe/Brussels'}}
    dump(replay_dir, template_name, sample_context)


# Generated at 2022-06-13 18:42:57.277420
# Unit test for function dump
def test_dump():
    os.makedirs('temp')
    context = {'cookiecutter': {'first_name': 'First',
                                'last_name': 'Last',
                                'email': 'first.last@example.com'}}

    dump('temp', 'test', context)
    expected_replay = {'cookiecutter': {'first_name': 'First', 'last_name': 'Last', 'email': 'first.last@example.com'}}
    assert load('temp', 'test') == expected_replay


# Generated at 2022-06-13 18:43:08.196290
# Unit test for function dump
def test_dump():
    replay_dir = 'tests/test-replay'
    template_name = 'test'
    context = {}
    context['cookiecutter'] = {}
    context['cookiecutter']['repo_name'] = 'test-repo'
    context['cookiecutter']['repo_url'] = 'test-repo-url'
    context['cookiecutter']['author_name'] = 'test-author'
    context['cookiecutter']['project_name'] = 'test-project'
    context['cookiecutter']['open_source_license'] = 'test-license'
    context['cookiecutter']['is_public_repo'] = 'n'
    context['cookiecutter']['pypi_username'] = 'test-pypi-username'


# Generated at 2022-06-13 18:43:19.146187
# Unit test for function load
def test_load():

    replay_dir = "replays"
    file_name = "helloworld"
    template_name = file_name + ".json"

# Generated at 2022-06-13 18:43:23.098056
# Unit test for function load
def test_load():
    folder = '/Users/guodongzhao/Desktop/Python/cookiecutter-django/tests/fixtures/github-cookiecutter-django/{{cookiecutter.repo_name}}'
    template_name = 'cookiecutter-django'

# Generated at 2022-06-13 18:43:26.495897
# Unit test for function load
def test_load():
    print('Unittest for function load')
    replay_dir = '.'
    template_name = 'test_template'
    context = load(replay_dir, template_name)
    print(context)


# Generated at 2022-06-13 18:43:30.281125
# Unit test for function load
def test_load():
    template_name = 'gh:audreyr/cookiecutter-pypackage'
    replay_dir = os.path.join(os.path.dirname(__file__), 'fixtures')
    context = load(replay_dir, template_name)
    assert isinstance(context, dict)
    assert 'cookiecutter' in context


# Generated at 2022-06-13 18:43:43.504474
# Unit test for function dump
def test_dump():
    replay_dir = os.path.abspath('tests/files/replay')
    template_name = 'tests/files/replay/cookiecutter-pypackage'
    context = {
        'cookiecutter': {
            '_template': template_name,
            'author_github_username': 'audreyr',
            'author_name': 'Audrey Roy',
            'command_line_interface': 'click',
            'description': 'A Cookiecutter template for a Python package.',
            'full_name': 'Audrey Roy',
            'open_source_license': 'MIT license',
            'repo_name': 'cctestrepo',
            'year': '2013',
        }
    }
    replay_file = dump(replay_dir, template_name, context)

# Generated at 2022-06-13 18:43:46.250665
# Unit test for function load
def test_load():
    list_of_variables = load("./testing/fixtures/tests/replay_dir", "jinja2_replay_fixture")
    print(list_of_variables)

if __name__ == "__main__":
    test_load()

# Generated at 2022-06-13 18:43:48.034601
# Unit test for function load
def test_load():
    pass


# Generated at 2022-06-13 18:44:08.564871
# Unit test for function dump
def test_dump():
    global path
    global template_name
    global context
    path = os.getcwd()
    template_name = 'test'
    context = {
        'cookiecutter': {
            'full_name': 'Test Name',
            'email': 'test@test.com',
            'username': 'test',
            'project_name': 'Test Project',
            'project_short_description': 'Test Description',
            'project_name_choices': {
                'one': 'one',
                'two': 'two',
                'three': 'three'
            }
        }
    }
    dump(path, template_name, context)
    assert os.path.exists(os.path.join(path, 'test.json'))

# Generated at 2022-06-13 18:44:13.710705
# Unit test for function dump
def test_dump():
    """Unit test for function dump."""
    import tempfile

    template_name = 'template'
    replay_dir = '{}/replay_dir'.format(tempfile.gettempdir())
    context = {'cookiecutter': {'sample_key': 'A value', 'replay_dir': replay_dir}}
    dump(replay_dir, template_name, context)

    # Load the context from test dump
    loaded_context = load(replay_dir, template_name)
    assert loaded_context == context



# Generated at 2022-06-13 18:44:18.771032
# Unit test for function dump
def test_dump():
    replay_dir = 'tests/files/edit_me/.cookiecutter.replay'
    template_name = 'tests/files/edit_me'

    context = {
        'cookiecutter': {
            'full_name': 'Benjamin Bach',
        }
    }

    try:
        dump(replay_dir, template_name, context)
        assert os.path.isfile(get_file_name(replay_dir, template_name))

        assert context == load(replay_dir, template_name)
    finally:
        os.remove(get_file_name(replay_dir, template_name))

# Generated at 2022-06-13 18:44:28.325830
# Unit test for function load
def test_load():
    """Test load function."""
    file_name = 'example_template'
    context = {'cookiecutter': {'text': 'Hello world!'}}

    try:
        # Invalid test case: file name not string
        load(None, 123)
    except TypeError:
        pass
    else:
        raise AssertionError('Template name must be a string')

    try:
        # Invalid test case: context not dictionary
        load(None, file_name)
    except ValueError:
        pass
    else:
        raise AssertionError('Context must contain cookiecutter key')

    # Invalid test case: replay directory does not exist
    try:
        load('invalid_directory', file_name)
    except IOError:
        pass
    else:
        raise AssertionError('Unable to create replay dir')



# Generated at 2022-06-13 18:44:30.723606
# Unit test for function load
def test_load():
    res = load("/Users/yezhuohui/Documents/cookiecutter-test/test/test1", "test")

# Generated at 2022-06-13 18:44:33.247801
# Unit test for function load
def test_load():
    """Unit test for function load."""
    context = load('./tests/test-output/replay/', 'cookiecutter-pypackage')
    assert context['cookiecutter']['project_slug'] == 'test-test'



# Generated at 2022-06-13 18:44:36.787589
# Unit test for function load
def test_load():
    file_path = './tests/test-load.json'
    context = load(file_path)
    assert context['cookiecutter']['project_name'] == '{{ cookiecutter.repo_name }}'


# Generated at 2022-06-13 18:44:40.080720
# Unit test for function dump
def test_dump():
    replay_dir = "path/to/new/dir"
    template_name = "some/name"
    context = {"foo": "bar"}
    try:
        dump(replay_dir, template_name, context)
    except:
        assert False



# Generated at 2022-06-13 18:44:46.844743
# Unit test for function dump
def test_dump():
    """test_dump."""
    import tempfile
    replay_dir = tempfile.mkdtemp()
    template_name = 'test_template'
    context = {'cookiecutter': 'hello'}
    try:
        dump(replay_dir, template_name, context)
        assert os.path.exists(os.path.join(replay_dir, template_name+'.json'))
    finally:
        import shutil
        shutil.rmtree(replay_dir)


# Generated at 2022-06-13 18:44:51.668289
# Unit test for function load
def test_load():
    cur_dir = '/tmp/cookiecutter-load-test'
    replays_dir = os.path.join(cur_dir, 'replays')
    replay_file = os.path.join(replays_dir, 'test.json')
    with open(replay_file, 'w') as outfile:
        json.dump({'cookiecutter': 'test'}, outfile, indent=2)
    context = load(replays_dir, 'test')
    assert(context['cookiecutter'] == 'test')


# Generated at 2022-06-13 18:45:42.533039
# Unit test for function load
def test_load():
    template_name = 'django-project-template'
    replay_dir = '.cache'
    context = load(replay_dir, template_name)
    assert 'cookiecutter' in context
    #assert context['cookiecutter']['project_name'] == 'my_project'
    print(context)

if __name__ == "__main__":
    test_load()

# Generated at 2022-06-13 18:45:45.907352
# Unit test for function load
def test_load():
    """Unit test for load."""
    assert load("~/Downloads/cookiecutter-python/tests/test-generate-files/", "cookiecutter.json")


# Generated at 2022-06-13 18:45:47.674515
# Unit test for function load
def test_load():
    print(load('replay', 'fruits'))



# Generated at 2022-06-13 18:45:55.992932
# Unit test for function load
def test_load():
    """
    test_load
    """

# Generated at 2022-06-13 18:45:58.585878
# Unit test for function load
def test_load():
    context = load("D:/Projects/cookiecutter","cookiecutter.json")
    assert isinstance(context, dict)
    assert 'cookiecutter' in context

if __name__ == '__main__':
    test_load()

# Generated at 2022-06-13 18:46:02.026490
# Unit test for function load
def test_load():
    replay_dir = r"/cs/engproj/3rd/wujx/CookieCutterDemo/cookiecutter-demo/cookiecutter_demo/demo_replay"
    template_name = "cookiecutter-pypackage"
    context = load(replay_dir, template_name)
    print(context)


# Generated at 2022-06-13 18:46:03.954148
# Unit test for function load
def test_load():
    context = load(replay_dir="cookie/replay", template_name="{{ cookiecutter.project_name}}")
    assert context["cookiecutter"]["project_name"] == "django"



# Generated at 2022-06-13 18:46:10.457572
# Unit test for function load
def test_load():
    if 'CC_REPLAY_DIR' in os.environ:
        replay_dir = os.environ['CC_REPLAY_DIR']
    else:
        replay_dir = os.path.join(os.path.expanduser('~'), '.cookiecutters')
    template_name = 'cookiecutter-pypackage'
    try:
        cookiecutter = load(replay_dir, template_name)
    except ValueError:
        return False
    if 'cookiecutter' not in cookiecutter:
        return False
    try:
        cookiecutter['cookiecutter']
    except KeyError:
        return False
    return True


# Generated at 2022-06-13 18:46:15.026696
# Unit test for function dump
def test_dump():
    replay_dir = '.'
    template_name = 'test-template'
    context = {'cookiecutter': {'full_name': 'user'}}
    dump(replay_dir, template_name, context)
    assert os.path.isfile(os.path.join(replay_dir, 'test-template.json'))
    os.remove(os.path.join(replay_dir, 'test-template.json'))


# Generated at 2022-06-13 18:46:18.213365
# Unit test for function load
def test_load():
    """Unit test for function load"""
    print("\nTesting load function of replay module with example json file")
    template_name = "cookiecutter-pypackage"
    replay_dir = os.path.join("tests","data","replay")
    context = load(replay_dir, template_name)
    print("Data is successfully loaded and return as a dictionary")



# Generated at 2022-06-13 18:47:04.249013
# Unit test for function dump
def test_dump():
    test_template_name = 'test_template_name'
    test_replay_dir = 'test_replay_dir'
    context = {'cookiecutter': {'replay': None}}

    # TODO: mock function calls
    dump(test_replay_dir, test_template_name, context)
    context_loaded = load(test_replay_dir, test_template_name)
    assert context == context_loaded

    os.remove('{}/{}.json'.format(test_replay_dir, test_template_name))
    os.rmdir(test_replay_dir)

# Generated at 2022-06-13 18:47:07.756975
# Unit test for function dump
def test_dump():
    replay_dir = os.path.join('/tmp/replay-test/')
    template_name = 'test-template'
    context = {}
    context['cookiecutter'] = {
        'full_name': 'Vikram Hegde',
        'email': 'hegdevikram@gmail.com'
    }
    dump(replay_dir, template_name, context)

    context_new = load(replay_dir, template_name)
    assert context_new == context


# Generated at 2022-06-13 18:47:22.475362
# Unit test for function dump
def test_dump():
    """Unit test for function dump."""
    import tempfile

    replay_dir = tempfile.mkdtemp()
    template_name = 'some_template_name'
    cookiecutter = {'some': 'value'}
    context = {'cookiecutter': cookiecutter}
    file_name = get_file_name(replay_dir, template_name)

    # dump should create the file
    assert not os.path.isfile(file_name)
    dump(replay_dir, template_name, context)
    assert os.path.isfile(file_name)

    # load should be able to read the file
    new_context = load(replay_dir, template_name)
    assert 'cookiecutter' in new_context
    assert new_context['cookiecutter'] == cookiecutter


#

# Generated at 2022-06-13 18:47:23.597023
# Unit test for function load
def test_load():
    assert load('/tmp', 'hello') == {}

# Generated at 2022-06-13 18:47:34.712883
# Unit test for function load

# Generated at 2022-06-13 18:47:37.503568
# Unit test for function load
def test_load():
    context = load("tests/test-data/replies", "audreyr-cookiecutter-pypackage")
    assert 'author_name' in context['cookiecutter']
    assert 'project_name' in context['cookiecutter']

# Generated at 2022-06-13 18:47:43.417170
# Unit test for function dump
def test_dump():
    file_name = "test_dump.json"
    template_name = "test_dump.html"
    replay_dir = "replay"
    context = {'cookiecutter': {'replay': True}}
    dump(replay_dir, template_name, context)
    assert os.path.isfile(file_name)
    os.remove(file_name)


# Generated at 2022-06-13 18:47:44.824952
# Unit test for function load
def test_load():
    assert load('./tests/test-replay/', 'bacon-project') == None


# Generated at 2022-06-13 18:47:54.903492
# Unit test for function load
def test_load():
    """Unit test for function load."""
    from click.testing import CliRunner
    from cookiecutter.cli import main

    runner = CliRunner()
    result = runner.invoke(
        main,
        [
            'gh:audreyr/cookiecutter-pypackage',
            '--no-input',
            '--replay',
            '--replay-dir',
            os.path.join(os.getcwd(), 'tests/test-load'),
            'project_name=example_app',
            'project_slug=example_app',
            '--no-input'
        ]
    )
    assert result.exit_code == 0

# Generated at 2022-06-13 18:48:03.042863
# Unit test for function load
def test_load():
    """Unit test for function load"""
    import os
    import shutil
    import time
    import json
    template_name = os.getcwd()
    replay_dir = os.path.join(os.getcwd(), '{{cookiecutter.project_slug}}/replay')
    shutil.copyfile(os.path.join(os.getcwd(), '{{cookiecutter.project_slug}}/replay/{{cookiecutter.project_slug}}.json'), os.path.join(os.getcwd(), '{{cookiecutter.project_slug}}/replay/{{cookiecutter.project_slug}}.json.tmp'))