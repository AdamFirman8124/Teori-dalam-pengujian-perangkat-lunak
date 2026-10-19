

# Generated at 2022-06-13 18:38:23.248221
# Unit test for function dump
def test_dump():
    """Unit test for function dump."""
    assert(dump)



# Generated at 2022-06-13 18:38:31.228545
# Unit test for function load
def test_load():
    template_name = "kube_pods"
    context = {"cookiecutter": {
        "project_name": "Hello World",
        "kube_namespace": "kube-system",
        "cpu_request": "100m",
        "cpu_limit": "100m",
        "memory_request": "100Mi",
        "memory_limit": "100Mi",
    }}
    replay_dir = os.path.join(os.getcwd(), 'test')
    dump(replay_dir, template_name, context)
    assert context == load(replay_dir, template_name)
    os.remove(get_file_name(replay_dir, template_name))



# Generated at 2022-06-13 18:38:33.353371
# Unit test for function load
def test_load():
    replay_dir = os.path.dirname(os.path.realpath(__file__))
    context = load(replay_dir, 'test')
    assert 'cookiecutter' in context

# Generated at 2022-06-13 18:38:36.079491
# Unit test for function dump
def test_dump():
    replay_dir = '../tests/test-replay'
    make_sure_path_exists(replay_dir)
    template_name = 'test'
    context = {'cookiecutter': {'full_name': 'James Smith'}}
    dump(replay_dir, template_name, context)



# Generated at 2022-06-13 18:38:45.576365
# Unit test for function get_file_name
def test_get_file_name():
    assert get_file_name('.', 'my-project') == './my-project.json'
    assert get_file_name('.', 'my-project.json') == './my-project.json'
    assert get_file_name('.', 'my-project/') == './my-project.json'
    assert get_file_name('.', 'my-project.json/') == './my-project.json'
    assert get_file_name('my-project/', 'my-project.json') == 'my-project/my-project.json'
    assert get_file_name('my-project/', 'path/to/my-project.json') == 'my-project/path/to/my-project.json'

# Generated at 2022-06-13 18:38:46.981842
# Unit test for function load
def test_load():
    template_name = "fibo"
    replay_dir = "../undefined/fibo"
    context = load(replay_dir, template_name)
    print(context)


# Generated at 2022-06-13 18:38:54.929242
# Unit test for function dump
def test_dump():
    replay_dir = 'tests/test-replay/'
    template_name = 'test-replay'
    context = {
        'cookiecutter':
            {
                'full_name': 'Audreys Tests',
                'email': 'test@test.com',
                'project_name': 'test project'
            }
    }

    dump(replay_dir, template_name, context)


# Generated at 2022-06-13 18:38:57.703320
# Unit test for function load
def test_load():
    context = load(os.getcwd(), 'test')
    print(context)


# Generated at 2022-06-13 18:39:05.771837
# Unit test for function dump
def test_dump():
    """Test to write json data to file."""
    template_name = "cookiemonster"
    replay_dir = "/home/user1/Desktop/replay"
    user_input = "apple"
    context = {
        "name": user_input,
        "cookiecutter": {
            "template_name": template_name
        }
    }
    dump(replay_dir, template_name, context)
    assert os.path.isfile("/home/user1/Desktop/replay/cookiemonster.json")


# Generated at 2022-06-13 18:39:09.564981
# Unit test for function load
def test_load():
    context = load('tests/fixtures/fake-repo-pre/', 'fake-repo-pre')
    assert context == {'cookiecutter': {'full_name': 'Audrey Roy', 'project_name': 'cookiecutter-pypackage', 'replay': True, 'use_pytest': True, 'open_source_license': 'MIT license'}}

# Generated at 2022-06-13 18:39:16.097615
# Unit test for function load
def test_load():
    class fake_open(object):
        def __init__(self, test_replay):
            self.test_replay = test_replay
        def __enter__(self):
            return self.test_replay
        def __exit__(self, type, value, traceback):
            return
    cookiecutter_test_dir = os.path.dirname(__file__)
    replay_dir = os.path.join(cookiecutter_test_dir, 'test_replay')

    with fake_open(open(os.path.join(replay_dir, 'testcookiecutter.json'), 'r')) as infile:
        context = json.load(infile)
    assert 'cookiecutter' in context
    assert context['cookiecutter']['replay'] == 'y'

# Generated at 2022-06-13 18:39:20.182125
# Unit test for function load
def test_load():
	#Load the record
	record = load('..','cookiecutter')
	#The record is an array
	assert(isinstance(record, dict))
	#The record has the keyword 'cookiecutter'
	assert('cookiecutter' in record)


# Generated at 2022-06-13 18:39:25.686727
# Unit test for function dump
def test_dump():
    replay_dir_ = 'tests/replay_dir'
    make_sure_path_exists(replay_dir_)
    template_name_ = '{{cookiecutter.repo_name}}'
    context_ = {'cookiecutter': {'repo_name': 'sampleproject', 'package_name': 'sample-project'}}
    dump(replay_dir_, template_name_, context_)


# Generated at 2022-06-13 18:39:32.636867
# Unit test for function load
def test_load():
    context = load('/home/hongxwing/travis-ci/cookiecutter', 'datascience')
    assert isinstance(context, dict)
    assert context['cookiecutter']['project_name'] == 'Data Science Project Template'
    assert context['cookiecutter']['project_name_slug'] == 'data-science-project-template'
    assert context['cookiecutter']['version'] == '0.1.0'
    assert context['cookiecutter']['full_name'] == 'Hongxu Wang'
    assert context['cookiecutter']['email'] == 'hongxwing@gmail.com'
    assert context['cookiecutter']['github_username'] == 'hongxwing'

# Generated at 2022-06-13 18:39:36.197342
# Unit test for function load
def test_load():
    replay_dir='/home/tianyuliu/testload'
    template_name='testload'
    a=load(replay_dir,template_name)
    print (a)


# Generated at 2022-06-13 18:39:37.139476
# Unit test for function load
def test_load():
    pass


# Generated at 2022-06-13 18:39:39.843214
# Unit test for function load
def test_load():
    assert load('tests/test-load', 'test-load') == {"cookiecutter": {"test": "load"}}

# Generated at 2022-06-13 18:39:44.071546
# Unit test for function load
def test_load():
    context = load(replay_dir = 'C:/Users/Tianqi/Desktop/Source',
                   template_name = 'P4_2')
    print(context)

# Generated at 2022-06-13 18:39:52.051569
# Unit test for function load
def test_load():
    replay_dir = 'C:/Users/Jacqueline/Desktop/cookiecutter/'
    replay_file = 'C:/Users/Jacqueline/Desktop/cookiecutter/template.json'

    with open(replay_file, 'r') as infile:
        context = json.load(infile)

    assert 'cookiecutter' in context



# Generated at 2022-06-13 18:39:55.846378
# Unit test for function load
def test_load():
    replay_dir = 'C:\\Users\\jltsa\\cookiecutter-tpl2\\tests\\test-drive\\replay'
    template_name = 'my-new-project'
    context = load(replay_dir, template_name)
    print(context)
    return context



# Generated at 2022-06-13 18:39:58.446722
# Unit test for function load
def test_load():
    """Unit test for function load."""
    assert load('unit test', 'unit_test') != None

# Generated at 2022-06-13 18:40:04.766937
# Unit test for function load
def test_load():
    filename = 'tests/test-load-output.json'
    test_obj = {
        'cookiecutter': {
        },
        'a': 'b',
        'c': 'd'
    }
    with open(filename, 'w') as outfile:
        json.dump(test_obj, outfile, indent=2)
    result_obj = load('', filename)
    os.remove(filename)
    assert test_obj == result_obj



# Generated at 2022-06-13 18:40:09.035163
# Unit test for function dump
def test_dump():
    context = {}
    context["cookiecutter"] = {"_template": "cookiecutter-pypackage"}
    dump("tests/test-replay/", "cookiecutter-pypackage", context)
    assert os.path.isfile("tests/test-replay/cookiecutter-pypackage.json")



# Generated at 2022-06-13 18:40:12.127953
# Unit test for function load
def test_load():
    replay_dir="/home/tux/.cookiecutters"
    template_name="django-project"
    context=load(replay_dir, template_name)
    print(context["cookiecutter"])


# Generated at 2022-06-13 18:40:21.402796
# Unit test for function dump
def test_dump():
    replay_dir = 'tests/test-output'
    template_name = 'pypackage'
    #context = {'repo_name': 'hello_world', 'full_name': 'Abhinav', 'email': 'abhinav.rajput00@gmail.com', 'package_name': 'hello_world', 'project_short_description': 'Test package', 'cookiecutter': {'_template': 'https://github.com/audreyr/cookiecutter-pypackage.git', 'name': 'cookiecutter'}, 'year': '2019'}
    context = {'r1': 'r1', 'r2': 'r2', 'r3': 'r3'}
    dump(replay_dir, template_name, context)
    return


# Generated at 2022-06-13 18:40:27.592943
# Unit test for function load
def test_load():
    import cookiecutter.replay
    import os

    # Test loading of replay file
    replay_dir = os.path.join(os.path.dirname(__file__), 'mock_replay')
    template_name = os.path.join(replay_dir, 'mock_replay.json')
    context = cookiecutter.replay.load(replay_dir, template_name)
    assert context == {u'cookiecutter': {u'first_name': u'Audrey',
                                         u'last_name': u'Roy'}
                       }
    # Test loads file from ./ if no replay_dir defined (or relative path)
    replay_dir = os.path.join(os.path.dirname(__file__), 'mock_replay')
    template_name = os.path.join

# Generated at 2022-06-13 18:40:39.943459
# Unit test for function dump
def test_dump():
    """
    Testing function dump.
    1. Create the replay file in the tmp folder
    2. Dump data into it
    3. Verify the data
    """
    replay_dir = 'tests/files/replay-test'
    template_name = 'test-template'
    context = {
        'cookiecutter': {
            'year': '2016',
            'project_name': 'test-project'
        }
    }
    dump(replay_dir, template_name, context)
    # The repeat of dumping will cover the original data
    context = {
        'cookiecutter': {
            'year': '2017',
            'project_name': 'test-project'
        }
    }
    dump(replay_dir, template_name, context)

# Generated at 2022-06-13 18:40:43.718375
# Unit test for function load
def test_load():
    """Test the load function."""
    assert load("./tests/test-repo", "foobar") == {"cookiecutter": {"foo": "{{cookiecutter.bar}}", "bar": "baz"}}

# Generated at 2022-06-13 18:40:51.668826
# Unit test for function load
def test_load():
    """Test the load function."""
    # Create a json file and mock data
    replay_dir = '.'
    template_name='Template'
    template_file=get_file_name(replay_dir, template_name)
    context = {'cookiecutter': {'json_key': 'json_value'}}
    # Check the load function
    with open(template_file,'w') as outfile:
        json.dump(context, outfile, indent=2)

    context_test=load(replay_dir, template_name)
    ok_(context_test == context)
    # Remove the template file
    os.remove(template_file)

# Generated at 2022-06-13 18:41:00.039313
# Unit test for function load
def test_load():
    replay_dir = os.path.join(os.path.dirname(__file__), '..', 'tests')
    template_name = 'base'
    with open('tests/base.json', 'r') as infile:
        json_data = json.load(infile)
    json_data['cookiecutter']['_copy_without_render'] = '{{cookiecutter.project_name}}'
    json_data['cookiecutter']['_copy_without_render1'] = '{{cookiecutter.project_slug}}'
    json_data['cookiecutter']['_copy_without_render2'] = '{{cookiecutter.project_slug}}'
    json_data['cookiecutter']['project_slug'] = 'Test_Project_slug'

# Generated at 2022-06-13 18:41:03.965822
# Unit test for function load
def test_load():
    load('cookiecutter.replay/tests/replay_files/', 'replay_1')

# Generated at 2022-06-13 18:41:05.776775
# Unit test for function load
def test_load():
    print(load('replay', '{{cookiecutter.project_name}}'))

if __name__ == '__main__':
    test_load()

# Generated at 2022-06-13 18:41:08.559821
# Unit test for function load
def test_load():
    template_name = 'test'
    context = {'cookiecutter': 'dict'}
    replay_dir = 'test_replay_dir'
    dump(replay_dir=replay_dir, template_name=template_name, context=context)
    load(replay_dir=replay_dir, template_name=template_name)


if __name__ == "__main__":
    test_load()

# Generated at 2022-06-13 18:41:09.418393
# Unit test for function load
def test_load():
    assert isinstance(load('parameters/', 'bacon'), dict)


# Generated at 2022-06-13 18:41:13.282431
# Unit test for function load
def test_load():
    os.mkdir("test_replay")
    with open("test_replay/test.json", 'w') as f:
        json.dump({'cookiecutter': {'cookie1': 'value1', 'cookie2': 'value2'}}, f)

    context = load("test_replay", "test")
    assert context['cookiecutter']['cookie1'] == 'value1'
    assert context['cookiecutter']['cookie2'] == 'value2'
    os.remove("test_replay/test.json")
    os.removedirs("test_replay")

# Generated at 2022-06-13 18:41:22.839025
# Unit test for function dump
def test_dump():
    # Make a temporary directory
    import tempfile, shutil, os
    tmpdir = tempfile.mkdtemp()
    print(tmpdir)
    # This directory and everything in it will be removed later
    #replay_dir = os.path.join(tmpdir, 'output')
    replay_dir = tmpdir
    template_name = "my_replay_file"
    context = {'cookiecutter': {'full_name': 'Dmitri Soshnikov', 'email': 'dmitri.soshnikov@gmail.com' }}
    dump(replay_dir,template_name,context)
    # Test that the replay file exists
    replay_file = get_file_name(replay_dir, template_name)
    assert(os.path.exists(replay_file))

# Generated at 2022-06-13 18:41:23.605034
# Unit test for function load
def test_load():
    assert 1==1


# Generated at 2022-06-13 18:41:33.903290
# Unit test for function load
def test_load():
    replay_dir = "./replay"
    template_name = "test"
    context = load(replay_dir, template_name)
    #print(context)

# Generated at 2022-06-13 18:41:41.541133
# Unit test for function load
def test_load():
    """Test load()."""
    # Test missing file
    replay_file = get_file_name('./tests/replay', 'no_file')
    try:
        load('./tests/replay', 'no_file')
        assert False
    except FileNotFoundError as e:
        err_msg = e.args[0]
        assert err_msg == 'File not found: ' + replay_file

    # Test missing cookiecutter key
    replay_file = get_file_name('./tests/replay', 'tox')
    try:
        load('./tests/replay', 'tox')
        assert False
    except ValueError as e:
        err_msg = e.args[0]
        assert err_msg == 'Context is required to contain a cookiecutter key'

    # Test success

# Generated at 2022-06-13 18:41:46.578298
# Unit test for function dump
def test_dump():
    replay_dir = 'tests/test-replay/'
    template_name = 'test_template'
    context = {'cookiecutter': 'hello cookiecutter'}
    dump(replay_dir, template_name, context)
    try:
        assert os.path.isfile(get_file_name(replay_dir, template_name))
    finally:
        os.remove(get_file_name(replay_dir, template_name))


# Generated at 2022-06-13 18:41:53.298120
# Unit test for function load
def test_load():
    test_context = {'cookiecutter': 'test'}
    test_name = 'test_cookiecutter'
    test_dir = '/test'
    dump(test_dir, test_name, test_context)
    assert load(test_dir, test_name) == test_context


# Generated at 2022-06-13 18:41:55.494808
# Unit test for function load
def test_load():
	replay_dir = ""
	template_name = "cookiecutter.json"
	assert load(replay_dir, template_name)

if __name__ == '__main__':
	test_load()

# Generated at 2022-06-13 18:42:05.872838
# Unit test for function dump
def test_dump():
    # Check exception thrown when replay directory is not created
    from cookiecutter.replay import dump
    import os
    from pytest import raises

    with raises(IOError) as excinfo:
        template_name = 'my_template'
        context = {
            "cookiecutter": {
                "full_name": "Your Name",
                "email": "Your email"
            }
        }
        dump('random_dir_that_does_not_exist', template_name, context)
    assert 'Unable to create replay dir at random_dir_that_does_not_exist' in str(excinfo)

    # Check exception thrown when template_name is not a string
    with raises(TypeError) as excinfo:
        replay_dir = os.path.join(os.getcwd(), 'random_replay_dir')


# Generated at 2022-06-13 18:42:08.955097
# Unit test for function load
def test_load():
    replay_dir = "C:/Users/saura/Downloads/cookiecutter-django-crud"
    template_name = "cookiecutter.json"
    context = load(replay_dir,template_name)
    assert context['cookiecutter']['repo_name'] == "Cookiecutter Django CRUD"
    

# Generated at 2022-06-13 18:42:09.775754
# Unit test for function load
def test_load():
    print(load(None, 'abc'))

# Generated at 2022-06-13 18:42:17.674324
# Unit test for function load
def test_load():
    """
    Unit test for function load

    :return:
    """
    template_name = "dummy_template"
    replay_dir = "C:\\Users\\User\\Desktop\\replay"

    template_name = "dummy_template"
    replay_dir = "C:\\Users\\User\\Desktop\\replay"

    if not isinstance(template_name, str):
        raise TypeError('Template name is required to be of type str')

    replay_file = get_file_name(replay_dir, template_name)

    with open(replay_file, 'r') as infile:
        context = json.load(infile)

    if 'cookiecutter' not in context:
        raise ValueError('Context is required to contain a cookiecutter key')

    assert context

    return context



# Unit

# Generated at 2022-06-13 18:42:28.177281
# Unit test for function load
def test_load():
    """Test load replay json file and compare it with a sample."""
    import sys
    test_dir = os.path.dirname(__file__)
    template_name = 'tests/fake-repo-pre/'
    replay_dir = os.path.join(test_dir, 'test_replay')
    sample_name = os.path.join(test_dir, 'test_replay.json')
    sys.argv = ['cookiecutter', template_name, '--no-input', '--replay-dir', replay_dir]
    from cookiecutter.main import cookiecutter
    cookiecutter(template_name)
    context = load(replay_dir, template_name)
    with open(sample_name, 'r+') as infile:
        sample = json.load(infile)
       

# Generated at 2022-06-13 18:42:32.030715
# Unit test for function load
def test_load():
    template_name = 'bootstrap-python'
    replay_dir = './cookiecutter-replay'
    context = load(replay_dir, template_name)
    assert(context is not None)
    assert('cookiecutter' in context)
    assert(context['cookiecutter']['full_name'] == 'Ben Nuttall')


# Generated at 2022-06-13 18:42:36.472723
# Unit test for function dump
def test_dump():
    context = {
        'cookiecutter': {
            'full_name': 'Audrey Roy',
            'email': 'audreyr@example.com',
            'github_username': 'audreyr',
            'project_name': 'cookiecutter-pypackage',
            'repo_name': 'cookiecutter-pypackage',
            'release_date': '2014-10-10',
            'version': '0.1.0',
            'open_source_license': 'MIT license'
        },
        'foo': {
            'bar': 'baz'
        }
    }

    replay_dir = '.'
    template_name = 'cookiecutter-pypackage'

    # Unit test for function dump
    dump(replay_dir, template_name, context)


# Unit

# Generated at 2022-06-13 18:42:37.918603
# Unit test for function load
def test_load():
    ctx = {}
    replay_file = '~/cookiecutters/unity-cookiecutter-master/replays/cookiecutter.json'
    ctx = load(None, replay_file)
    print(ctx)


# Generated at 2022-06-13 18:42:46.597920
# Unit test for function load
def test_load():
    context = load('replay', 'test_replay')
    assert isinstance(context, dict)
    assert 'cookiecutter' in context


# Generated at 2022-06-13 18:42:52.595208
# Unit test for function load
def test_load():
    """Unit test for function load"""
    replay_dir = '/tmp/cookiecutter_test_load'
    template_name = 'test_template'
    context = {"cookiecutter": {"name": "test_name"}}
    dump(replay_dir, template_name, context)
    assert load(replay_dir, template_name) == context

# Generated at 2022-06-13 18:42:56.413637
# Unit test for function load
def test_load():
    """Unit test for function load"""
    context = load(os.path.join(os.path.dirname(__file__), 'fixtures'),
                   'testproject')
    assert context['cookiecutter']['project_name'] == 'TestProject'



# Generated at 2022-06-13 18:43:00.802666
# Unit test for function dump
def test_dump():
    from tempfile import mkdtemp
    from shutil import rmtree
    from cookiecutter.main import cookiecutter
    import os
    import json

    temp_dir = mkdtemp()
    context = cookiecutter(
        'tests/test-repo-pre/',
        no_input=True,
        replay_dir=temp_dir,
    )
    replay_file = os.path.join(temp_dir, 'tests-test-repo-pre-json')
    with open(replay_file, 'r') as f:
        data = json.load(f)

    assert data['cookiecutter']['full_name'] == 'Audrey Roy Greenfeld'
    assert data['cookiecutter']['email'] == 'audreyr@example.com'

# Generated at 2022-06-13 18:43:04.480915
# Unit test for function load
def test_load():
    template_name = "cookiecutter-pypackage"
    context = load("/home/jarvis/Documents/replay/",template_name)
    print("Load successfully")
    return context

# Generated at 2022-06-13 18:43:10.622205
# Unit test for function dump
def test_dump():
    replay_dir = 'tests/test-output/cookiecutter_replay_dir'
    template_name = 'replay_test'
    context = {
        'cookiecutter': {
            'project_name': 'replay_test',
            'full_name': 'replay_test',
            'email': 'replay_test@email.com'
        },
        'language': 'python'
    }
    dump(replay_dir, template_name, context)
    file_name = get_file_name(replay_dir, template_name)
    assert 'replay_test/replay_test.json' == file_name



# Generated at 2022-06-13 18:43:19.052785
# Unit test for function load
def test_load():
    """Check load function works well."""
    context = {'cookiecutter': {
            '_copy_without_render': [
                'CHANGELOG.rst',
                'LICENSE',
                'README.rst',
            ],
        }
    }
    replay_dir = os.path.join(os.path.expanduser('~'), '.cookiecutters')
    template_name = 'cookiecutter-pypackage'

    dump(replay_dir, template_name, context)
    context_loaded = load(replay_dir, template_name)
    assert context == context_loaded

# Generated at 2022-06-13 18:43:19.764761
# Unit test for function load
def test_load():
    assert True

# Generated at 2022-06-13 18:43:25.661278
# Unit test for function load
def test_load():
    replay_dir = "/Users/joe/Documents/cookiecutter_test/replay"
    template_name = "my_template"
    context = load(replay_dir, template_name)

    output_baseurl = context['cookiecutter']['baseurl']
    output_name = context['cookiecutter']['name']

    assert(output_baseurl == "http://abcd.com")
    assert(output_name == "en")



# Generated at 2022-06-13 18:43:26.663498
# Unit test for function load
def test_load():
    load('test_path', 'test_name')

# Generated at 2022-06-13 18:43:37.002876
# Unit test for function load
def test_load():
    assert load("replay_dir", "template_name")



# Generated at 2022-06-13 18:43:38.306166
# Unit test for function load
def test_load():
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 18:43:39.379301
# Unit test for function load
def test_load():
    load("","")



# Generated at 2022-06-13 18:43:47.012296
# Unit test for function load
def test_load():
    from cookiecutter.config import REPLAY_DIR
    from cookiecutter.exceptions import ReplayUnavailable
    import os
    import shutil
    import tempfile
    import unittest

    class ReplayTest(unittest.TestCase):
        def setUp(self):
            # Create a temporary test directory
            self.test_dir = tempfile.mkdtemp()
            # Use the temporary directory as replay directory
            self.replay_dir = os.path.join(self.test_dir, REPLAY_DIR)
            make_sure_path_exists(self.replay_dir)

        def test_load(self):
            context = {'cookiecutter': {'first_name': 'First', 'last_name': 'Last'}}

# Generated at 2022-06-13 18:43:53.812127
# Unit test for function load
def test_load():
    """Unit test for function load."""
    context = load("/Users/kunjian_song/Dropbox", "test_project")

    # Check the value of key cookiecutter in context
    assert 'cookiecutter' in context
    assert context['cookiecutter']['project_name'] == "test_project"
    assert context['cookiecutter']['author_name'] == "Kunjian Song"



# Generated at 2022-06-13 18:43:58.276290
# Unit test for function dump
def test_dump():
    replay_dir = '/tmp/replay'
    template_name = 'cc-test-template1'
    context = {'cookiecutter': {'project_name': 'cc-test-template1'}}
    dump(replay_dir, template_name, context)
    assert os.path.exists(get_file_name(replay_dir, template_name))
    os.remove(get_file_name(replay_dir, template_name))


# Generated at 2022-06-13 18:44:06.489096
# Unit test for function dump
def test_dump():
    replay_dir = '{{cookiecutter.replay_dir}}'
    template_name = '{{cookiecutter.project_name}}'
    context = dict(cookiecutter=dict(project_name=template_name))
    dump(replay_dir, template_name, context)

    replay_file = get_file_name(replay_dir, template_name)
    assert os.path.isfile(replay_file)
    assert open(replay_file, 'r').read() == json.dumps(context, indent=2)

    os.remove(replay_file)
    assert not os.path.isfile(replay_file)

# Generated at 2022-06-13 18:44:13.545421
# Unit test for function load
def test_load():
    rd = '/Users/yennanliu/Dropbox/UT-TOR-2018/UT-TOR-2018-C/Cookiecutter/test_replay-dir'
    tn = 'cookiecutter-pypackage'
    # open json file
    context = load(rd, tn)
    # assert value
    print (context['cookiecutter']['project_slug'])
    assert context['cookiecutter']['project_slug'] == 'cookiecutter-pypackage'
    # dump json file
    # dump(rd, tn, context)

if __name__ == '__main__':
    test_load()

# Generated at 2022-06-13 18:44:16.923688
# Unit test for function load
def test_load():
    import pdb
    pdb.set_trace()

    replay_dir = '/home/heath/repos/cookiecutter-pypackage'
    template_name = 'cookiecutter-pypackage'

    context = load(replay_dir, template_name)
    dump(replay_dir, template_name, context)


# Generated at 2022-06-13 18:44:20.004694
# Unit test for function load
def test_load():
    template_name="cookiecutter-pypackage"
    replay_dir="./replay"

    context = load(replay_dir=replay_dir,template_name=template_name)
    print(context)



# Generated at 2022-06-13 18:44:43.676402
# Unit test for function load
def test_load():
    tmp_dir = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        'test_load_dir'
    )
    test_file = os.path.join(tmp_dir, 'test_load_file.json')
    with open(test_file, 'w') as f:
        f.write('{"test_key": "test_value"}')
    assert load(tmp_dir, 'test_load_file') == {'test_key': 'test_value'}

if __name__ == '__main__':
    test_load()

# Generated at 2022-06-13 18:44:48.404747
# Unit test for function dump
def test_dump():
    context = {'cookiecutter': {'full_name': 'sachin',
                                'email': 'sachin@guidesmiths.com'}}
    dump('../temp', 'replay_test', context)
    file = '../temp/replay_test.json'
    assert os.path.exists(file)
    os.remove(file)


# Generated at 2022-06-13 18:44:52.188333
# Unit test for function load
def test_load():
    res = load('C:\\Users\\lxk-9\\Desktop\\cookiecutter_projects\\cookiecutter-pypackage-minimal','cookiecutter')
    print(res)

# Generated at 2022-06-13 18:45:01.198284
# Unit test for function load
def test_load():
    replay_file = get_file_name(os.path.expanduser('~/.cookiecutters'),'project.json')
    print(replay_file)
    with open(replay_file, 'r') as infile:
        context = json.load(infile)
    if 'cookiecutter' not in context:
        print('Context is required to contain a cookiecutter key')
    return context


# Generated at 2022-06-13 18:45:08.235952
# Unit test for function dump
def test_dump():
    replay_dir = "tests/generated-files/dump_test"
    template_name = "template_name"
    context = {"cookiecutter":{"name":"Replace",
                               "version":"1.2.3"}}
    dump(replay_dir, template_name, context)
    file_name = get_file_name(replay_dir, template_name)
    assert os.path.isfile(file_name)
    os.remove(file_name)
    os.rmdir(replay_dir)


# Generated at 2022-06-13 18:45:14.816789
# Unit test for function dump
def test_dump():
    # Step 1: Get replay dir and template name
    replay_dir = os.path.expanduser('~/.cookiecutters')
    template_name = 'test_replay_file'
    
    # Step 2: Get context for replay
    context = {'cookiecutter': {'replay': True}}

    # Step 3: Call dump function to write data to replay file
    dump(replay_dir, template_name, context)

    # Step 4: Call load function to read data from replay file
    replay_context = load(replay_dir, template_name)

    # Step 5: Check if context from replay is same
    assert replay_context == context


if __name__ == '__main__':
    test_dump()

# Generated at 2022-06-13 18:45:20.495452
# Unit test for function dump
def test_dump():
    replay_dir = "replay_dir"
    template_name = 'test_template'
    context = {'cookiecutter': {'test': 'test'}}
    dump(replay_dir, template_name, context)
    context2 = load(replay_dir, template_name)
    assert context == context2
    os.remove('replay_dir/test_template.json')


# Generated at 2022-06-13 18:45:27.427766
# Unit test for function load
def test_load():
    """ """
    from cookiecutter.config import DEFAULT_CONFIG
    from cookiecutter.utils import get_user_config

    # set up user config file pointer
    DEFAULT_CONFIG['replay_dir'] = '/Users/liuyaqing/Desktop/cookiecutter/replays'
    user_config = get_user_config(config_file='~/.cookiecutterrc')

    # load replay
    replay = load(user_config['replay_dir'], 'pypackage')
    print(replay)
    return replay



# Generated at 2022-06-13 18:45:36.284536
# Unit test for function load
def test_load():
    replay_dir = "./tests/fixtures/fake-repo-pre/{{cookiecutter.repo_name}}/"
    template_name = "python_module"
    non_existent_template_name = "fake_template"
    context = load(replay_dir, template_name)
    assert context['cookiecutter']['repo_name'] == 'cookiecutter-pypackage'
    assert context['cookiecutter']['project_name'] == 'Python Module'
    assert context['cookiecutter']['project_slug'] == 'python-module'
    assert context['cookiecutter']['release_date'] == '2013-07-24'
    assert context['cookiecutter']['year'] == '2013'

if __name__ == '__main__':
    test_load()

# Generated at 2022-06-13 18:45:43.211889
# Unit test for function load
def test_load():
    print('test_load')
    os.system('rm -rf test/')
    os.system('mkdir test/')
    os.system('echo \'{"cookiecutter":{}}\' > test/test1.json')
    context = load('test/', 'test1')
    print(context)
    assert 'cookiecutter' in context



# Generated at 2022-06-13 18:46:27.264860
# Unit test for function load
def test_load():
    import cookiecutter.replay
    context = cookiecutter.replay.load('replay/', '_.py')
    assert context['cookiecutter'] == {'full_name': 'Audrey Roy Greenfeld'}


# Generated at 2022-06-13 18:46:32.499672
# Unit test for function load
def test_load():
    replay_dir = '/home/sala/PycharmProjects/cookiecutter-pypackage-minimal'
    template_name = 'cookiecutter.json'
    context = load(replay_dir, template_name)

# Generated at 2022-06-13 18:46:39.620301
# Unit test for function load
def test_load():
    replay_dir = 'C:/Users/sudhakar/Desktop/cookiecutter'
    template_name = '{{cookiecutter.repo_name}}'
    context = {'cookiecutter': {'repo_name': 'my_awesome_project'}}
    dump(replay_dir, template_name, context)

    file_name = get_file_name(replay_dir, template_name)
    with open(file_name, 'r') as infile:
        file_content = json.load(infile)

    assert file_content['cookiecutter']['repo_name'] == 'my_awesome_project'

# Generated at 2022-06-13 18:46:41.948449
# Unit test for function load
def test_load():
    context = load(os.path.join(os.path.dirname(__file__), 'replay'), 'example_main')
    assert 'cookiecutter' in context
    assert context['cookiecutter'] is not None


# Generated at 2022-06-13 18:46:47.256088
# Unit test for function dump
def test_dump():
    
    template_name = 'test_name'
    context = {'cookiecutter': {'cookiecutter': 'test_data'}}
    replay_dir = os.path.expanduser('~/.cookiecutters')
    
    dump(replay_dir, template_name, context)
    assert os.path.exists(os.path.join(replay_dir, '%s.json' % template_name))
    
    os.remove(os.path.join(replay_dir, '%s.json' % template_name))
    assert not os.path.exists(os.path.join(replay_dir, '%s.json' % template_name))
    

# Generated at 2022-06-13 18:46:50.905844
# Unit test for function dump
def test_dump():
    replay_dir = '~/Documents/replay'
    template_name = 'test_template'
    context = {'cookiecutter': {'test': 'test', 'test2': 'test2'}}
    dump(replay_dir, template_name, context)



# Generated at 2022-06-13 18:46:53.510258
# Unit test for function load
def test_load(): 
    assert(load('UserNum','V1')=={'cookiecutter': {}, 'UserNum': '2'})


# Generated at 2022-06-13 18:46:57.988875
# Unit test for function dump
def test_dump():
    replay_dir = 'tmp/replay'
    template_name = 'tmp/hello-world-2'
    context = {'cookiecutter': {'_template': template_name}}

    dump(replay_dir, template_name, context)
    out = load(replay_dir, template_name)

    assert out['cookiecutter']['_template'] == template_name


# Generated at 2022-06-13 18:47:05.476483
# Unit test for function load
def test_load():
    """Unit test for function load"""
    from tempfile import mkdtemp
    from shutil import rmtree

    replay_dir = mkdtemp()
    context = {'cookiecutter': {'name': 'cookiecutter'}}
    template_name = 'cookiecutter'
    dump(replay_dir, template_name, context)
    loaded_context = load(replay_dir, template_name)
    rmtree(replay_dir)

    assert context == loaded_context


# Generated at 2022-06-13 18:47:07.374134
# Unit test for function load
def test_load():
    loaded_context = load('.','tests/fake-repo-tmpl')

