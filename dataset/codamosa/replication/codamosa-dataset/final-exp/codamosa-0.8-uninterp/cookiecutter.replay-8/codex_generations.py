

# Generated at 2022-06-13 18:38:16.237127
# Unit test for function dump
def test_dump():
    """Unit test for function dump."""
    from cookiecutter.main import cookiecutter

    template_name = 'cookiecutter-pypackage'
    template_url = 'https://github.com/audreyr/cookiecutter-pypackage.git'
    replay_dir = 'cookiecutter/tests/test-output/replay'


# Generated at 2022-06-13 18:38:19.445350
# Unit test for function dump
def test_dump():
    try:
        dump("/temp", "context", "test")
    except TypeError as e:
        assert str(e) == "Context is required to be of type dict"


# Generated at 2022-06-13 18:38:23.833886
# Unit test for function load
def test_load():
    template_name = 'cookiecutter-pypackage'
    replay_dir = '~/.cookiecutters_replay'
    dic = load(replay_dir, template_name)
    assert dic['_template'] == template_name and 'cookiecutter' in dic
    print('test_load() passed')



# Generated at 2022-06-13 18:38:25.590934
# Unit test for function dump
def test_dump():
    assert dump('my_file', 'my_stuff', 'my_things') == True

## Unit test for function load

# Generated at 2022-06-13 18:38:31.042882
# Unit test for function dump
def test_dump():
    """Test that "dump" function works as expected."""

    replay_dir = './'
    template_name = 'test'
    context = {'name': 'test'}
    dump(replay_dir, template_name, context)
    file_name = get_file_name(replay_dir, template_name)
    assert os.path.isfile(file_name)
    os.remove(file_name)

# Unit test function load

# Generated at 2022-06-13 18:38:34.712360
# Unit test for function load
def test_load():
    test_dict = {'cookiecutter': {'project_name': 'cookiecutter-dummy'}}
    test_dir = os.path.join(os.getcwd(), 'cookiecutter', 'tests')
    dump(test_dir, 'cookiecutter-dummy', test_dict)
    assert(load(test_dir, 'cookiecutter-dummy') == test_dict)


# Generated at 2022-06-13 18:38:43.204181
# Unit test for function dump
def test_dump():
    template_name = "python_project"
    context = {"cookiecutter": {"project_name": "python_project", 
                                "author_name": "Cookiecutter",
                                "author_email": "development@hackebrot.de",
                                "cookiecutter_replay": "/Users/phuongnguyen/research/crawler/cookiecutter-python-project/cookiecutter.replay"}} 
    replay_dir = "cookiecutter.replay"
    dump(replay_dir, template_name, context)
    assert load(replay_dir, template_name) == context


# Generated at 2022-06-13 18:38:45.904011
# Unit test for function load
def test_load():
    load('/Users/Haoji/Desktop/cookiecutter/testing-cookiecutter/cookiecutter-django', 'cookiecutter.json')

if __name__ == '__main__':
    test_load()

# Generated at 2022-06-13 18:38:47.453372
# Unit test for function load
def test_load():
    replay_dir = '/Users/shenliang/Documents/GitHub/cookiecutter/tests/test-load-replay/'
    context = load(replay_dir, 'test')
    print(context)


# Generated at 2022-06-13 18:38:54.693691
# Unit test for function dump
def test_dump():
    replay_dir = '/home/tcgeng/cookiecutter/tests/pipelines-replay-test/'
    template_name = 'test-template'
    context = {}
    context['cookiecutter'] = {'test':'test', 'answer':'42'}
    dump(replay_dir, template_name, context)


# Generated at 2022-06-13 18:39:05.886756
# Unit test for function dump
def test_dump():
    """
    Unit test function.

    @rtype:   bool
    @return:  succes of unit test
    """
    success = True
    try:
        replay_dir = os.path.join(os.path.abspath(os.path.curdir), 'test_replay_dir')
        template_name = 'test_template'
        context = {'cookiecutter': {'test': 'test value'}}
        dump(replay_dir, template_name, context)
    except IOError:
        success = False
    except TypeError:
        success = False
    except ValueError:
        success = False

    return success


# Generated at 2022-06-13 18:39:08.130125
# Unit test for function load
def test_load():
    assert isinstance(load('~/Desktop/Desktop/Cookiecutter_Testing',
                           'replay-file-name'), dict), \
        "load function fail to load a dictionary"



# Generated at 2022-06-13 18:39:09.603611
# Unit test for function load
def test_load():
    global context
    #context = load(replay_dir, template_name="django-pipeline")
    #print(context)
    context['cookiecutter']['app_name'] = "test"
    print(context)

# Generated at 2022-06-13 18:39:12.404812
# Unit test for function load
def test_load():
    template_name = 'templatename'
    replay_dir = '.'
    result = load(replay_dir, template_name)
    assert result['cookiecutter'] is not None
    assert result['cookiecutter']['project_name'] is not None



# Generated at 2022-06-13 18:39:14.160331
# Unit test for function load
def test_load():
    """Just Test."""
    print(load('/Users/huangjie/cookiecutter/cookiecutter-django/test/test_replay/', 'cookiecutter.json'))



# Generated at 2022-06-13 18:39:17.455790
# Unit test for function load
def test_load():
    context = load('replay', 'cookiecutter-pypackage')
    assert len(context.keys()) == 8
    assert context.get('_template') == 'cookiecutter-pypackage'


# Generated at 2022-06-13 18:39:23.431903
# Unit test for function dump
def test_dump():
    """Test the dump function."""
    replay_dir = "/home/test"
    template_name = "sample"
    context = {'cookiecutter': {'first_name': 'Srinivas'}}

    dump(replay_dir, template_name, context)
    assert os.path.isfile(get_file_name(replay_dir, template_name)) is True


# Generated at 2022-06-13 18:39:25.925344
# Unit test for function load
def test_load():
    replay_dir = "../../tests/replay/"
    template_name = "replay_test"
    context = load(replay_dir, template_name)
    return context


# Generated at 2022-06-13 18:39:35.069715
# Unit test for function load
def test_load():
    cookiecutter_dict = {}
    cookiecutter_dict['cookiecutter'] = {}
    cookiecutter_dict['cookiecutter']['full_name'] = 'Jing Wu'
    cookiecutter_dict['cookiecutter']['email'] = 'jingwu@brandeis.edu'
    cookiecutter_dict['cookiecutter']['github_username'] = 'jingwu06'
    cookiecutter_dict['cookiecutter']['project_name'] = 'doubly_linked_list'
    cookiecutter_dict['cookiecutter']['project_short_description'] = \
    'A doubly linked list class'
    cookiecutter_dict['cookiecutter']['pypi_username'] = 'jingwu06'
    cookiecutter_dict['cookiecutter']['version']

# Generated at 2022-06-13 18:39:40.809321
# Unit test for function load
def test_load():
    # Create a sample file in the replay_dir
    replay_dir = 'test_replay_dir'
    template_name = 'test_replay'
    # Creating the directory if it doesn't exist
    make_sure_path_exists(replay_dir)
    context = '{ "cookiecutter": {"testkey": "testvalue"} }'
    replay_file = get_file_name(replay_dir, template_name)
    with open(replay_file, 'w') as outfile:
        outfile.write(context)
    # Calling the load function
    context = load(replay_dir, template_name)
    assert context['cookiecutter']['testkey'] == "testvalue"
    # Cleaning up
    os.remove(replay_file)

# Generated at 2022-06-13 18:39:55.592985
# Unit test for function load
def test_load():
    template_name = 'my-awesome-template'
    test_replay_dir = '.testreplay'
    replay_file = get_file_name(test_replay_dir, template_name)
    replay_file_bak = replay_file + '.bak'
    with open(replay_file_bak, 'r') as infile:
        context = json.load(infile)
    try:
        dump(test_replay_dir, template_name, context)
        context = load(test_replay_dir, template_name)
        assert context['cookiecutter']['github_username'] == 'pydanny'
    finally:
        os.remove(replay_file)



# Generated at 2022-06-13 18:40:00.460610
# Unit test for function dump
def test_dump():
    """Test function dump."""
    replay_dir = 'tests/test-output'
    template_name = 'TESTTEMPLATE'
    context = {'cookiecutter': {'hello': 'world'}}

    dump(replay_dir, template_name, context)

    # Check if the file has been written
    replay_file = get_file_name(replay_dir, template_name)
    assert os.path.exists(replay_file)

    # Check if the content is correct
    with open(replay_file, 'r') as infile:
        data = json.load(infile)
        assert data == context

    # Clean up
    os.remove(replay_file)



# Generated at 2022-06-13 18:40:03.567217
# Unit test for function load
def test_load():
    print("Unit test for function load")
    context = load(".", "cookiecutter-SwaggerPetstore")
    print("Context is")
    print(context)
    print("Done test for function load")


# Generated at 2022-06-13 18:40:07.267983
# Unit test for function load
def test_load():
    template_name = "testcase"
    replay_dir = os.path.join(os.path.dirname(__file__), "testcases")
    context = load(replay_dir, template_name)

# Generated at 2022-06-13 18:40:11.410867
# Unit test for function dump
def test_dump():
    from cookiecutter.main import cookiecutter
    os.chdir(os.path.join(os.path.dirname(__file__), '..'))
    cookiecutter('.', overwrite_if_exists=True, no_input=True)
    assert os.path.isfile('tests/fake-repo/fake.json')
    with open('tests/fake-repo/fake.json', 'r') as infile:
        context = json.load(infile)
    assert context['full_name'] == 'Your name goes here'
    assert context['repo_name'] == 'cookiecutter-fake-repo'
    #os.remove('tests/fake-repo/fake.json')
    #os.rmdir('tests/fake-repo')


# Generated at 2022-06-13 18:40:14.760139
# Unit test for function load
def test_load():
    context = load('./tests/files/', 'example-replay')
    context = load('./tests/files/', 'example-replay.json')



# Generated at 2022-06-13 18:40:22.798573
# Unit test for function load
def test_load():
    import os
    import shutil
    from cookiecutter import replay
    from cookiecutter.compat import TemporaryDirectory

    template_name = 'test'

    context = {
        'cookiecutter': {
            'full_name': 'Smythe',
            'email': 'Smythe@example.com',
            'project_name': 'test'
        }
    }

    temp_path = TemporaryDirectory()
    replay_dir = os.path.join(temp_path.name, 'cookiecutter-replay')

    replay.dump(replay_dir, template_name, context)

    # Load replay file
    loaded_context = replay.load(replay_dir, template_name)
    assert loaded_context == context

    shutil.rmtree(temp_path.name)


# Generated at 2022-06-13 18:40:33.768579
# Unit test for function load
def test_load():
    """Unit test for function load."""
    replay_dir = '~/.cookiecutter_replay'
    template_name = 'cookiecutter-pypackage'

    # 1. Test when replay file does not exist
    expected_context = None
    context = load(replay_dir, template_name)
    assert context == expected_context

    # 2. Test when replay file exists but does not contain cookiecutter key
    expected_context = None
    dump(replay_dir, template_name, {})
    context = load(replay_dir, template_name)
    assert context == expected_context

    # 3. Test when replay file exists and does contain cookiecutter key
    expected_context = {'cookiecutter': {'full_name': 'Jane Doe', 'email': 'janedoe@example.com'}}


# Generated at 2022-06-13 18:40:40.090583
# Unit test for function load
def test_load():
    replay_file_name = 'x.json'
    context = {'a':'1', 'b':'2', 'cookiecutter':{}}
    with open(replay_file_name, 'w') as outfile:
        json.dump(context, outfile, indent=2)
    loaded_dict = load('.', replay_file_name)
    assert loaded_dict == context
    os.remove(replay_file_name)

# Generated at 2022-06-13 18:40:46.209118
# Unit test for function load
def test_load():
    # Create test.json
    with open('test.json', 'w') as outfile:
        json.dump({'cookiecutter': {'project_name': 'Test'}}, outfile, indent=2)
    # Test loading test.json
    with open('test.json', 'r') as infile:
        context = json.load(infile)
    assert context['cookiecutter']['project_name'] == 'Test'

# Main function to run if module is run as a script

# Generated at 2022-06-13 18:40:51.446875
# Unit test for function load
def test_load():
    """Unit test for function load.

    _cookiecutter/load.py_
    """
    context = load('./tests/test-replay/', 'fake')
    assert context['cookiecutter']['fake_option'] == 'fake-option-value'



# Generated at 2022-06-13 18:40:59.704835
# Unit test for function load
def test_load():
    context_dict = {
        'cookiecutter': {
            'full_name': 'Joe Doe',
            'email': 'joe@doe.com',
            'project_name': 'Example'
        }
    }
    rd = 'cookiecutter/tests/test-data/replay'
    tp = 'cookiecutter-pypackage'
    replay_file = get_file_name(rd, tp)
    with open(replay_file, 'w') as outfile:
        json.dump(context_dict, outfile, indent=2)
    with open(replay_file, 'r') as infile:
        context = json.load(infile)
    if 'cookiecutter' not in context:
        raise ValueError('Context is required to contain a cookiecutter key')




# Generated at 2022-06-13 18:41:00.933327
# Unit test for function load
def test_load():
    print(load("replay","python_package"))


# Generated at 2022-06-13 18:41:06.935177
# Unit test for function load
def test_load():
    import pandas as pd
    import pandas.util.testing as pdtest
    from .cookiecutter import generate_context as gc
    from .cookiecutter import load
    from .cookiecutter import dump
    from .cookiecutter import get_file_name
    from pathlib import Path
    assert gc.__doc__ is not None
    print(gc.__doc__)
    assert Path(r'C:\Users\Gaurav\OneDrive - University of Guelph\1 MS\1 Course Work\1 Semester-1\Coures 2\cookiecutter_package\cookiecutter\cookiecutter_package\cookiecutter\tests').exists()

# Generated at 2022-06-13 18:41:11.053476
# Unit test for function dump
def test_dump():
    """Test dump function"""
    replay_dir = '/home/zoe/'
    template_name = 'my-first-project'
    context = {
        'cookiecutter': {
            'project_name': 'my-first-project',
            'author_name': 'Zoe',
            'email': 'zoe@test.org',
            'college': ['pku', 'tsinghua']
        }
    }

    dump(replay_dir, template_name, context)
    read_context = load(replay_dir, template_name)
    assert context == read_context



# Generated at 2022-06-13 18:41:13.541324
# Unit test for function dump
def test_dump():
    replay_dir = 'tests/files/replay'
    template_name = 'tests/fake-repo-pre/'
    context = {
        'cookiecutter': {
            'hello': 'world',
        }
    }
    dump(replay_dir, template_name, context)


# Generated at 2022-06-13 18:41:17.125402
# Unit test for function dump
def test_dump():
    try:
        dump('/home/dave/Desktop/a/b', 'hello', {'cookiecutter':{'repo':'', 'repo_dir':'.'}})
    except:
        print('Test failed')


# Generated at 2022-06-13 18:41:20.740513
# Unit test for function load
def test_load():
	replay_dir = "/Users/saravananmk/Downloads/cookiecutter-test/testfiles"
	template_name = "test_file"
	context = load(replay_dir, template_name)

# Generated at 2022-06-13 18:41:23.428346
# Unit test for function dump
def test_dump():
    template_name = "python-basic-cli"
    context = {"cookiecutter": {"role": "cli", "cli_command": "cookie"}}
    dump('/tmp/', template_name, context)

# unit test for function load

# Generated at 2022-06-13 18:41:33.903154
# Unit test for function load
def test_load():
    template_name = 'template'
    replay_dir = 'C:/chris/replaydir'
    make_sure_path_exists(replay_dir)
    replay_file = get_file_name(replay_dir, template_name)
    context = {
        'cookiecutter': {
            'full_name': 'Chris Hsiao',
            'email': 'hsiao.chris@gmail.com',
            'github_username': 'hsiao-christopher',
        }
    }
    with open(replay_file, 'w') as outfile:
        json.dump(context, outfile, indent=2)
    context = load(replay_dir, template_name)
    print(context)
    os.remove(replay_file)

# Generated at 2022-06-13 18:41:43.470538
# Unit test for function dump
def test_dump():
    replay_dir = '{{ cookiecutter.project_slug }}/tests/replay'
    filename = replay_dir + '/' + 'cookiecutter_config.json'
    c = {'cookiecutter' : 'contextdump'}
    dump(replay_dir, 'cookiecutter_config', c)

    #Check if the file got created or not
    if(os.path.exists(filename)):
        print("File got successfully created.")
        os.remove(filename)
    else:
        print("Failed to create file")



# Generated at 2022-06-13 18:41:48.831260
# Unit test for function dump
def test_dump():
    try:
        dump(replay_dir=None, template_name=None, context=None)
        assert False
    except TypeError:
        pass
    try:
        dump(replay_dir='', template_name='', context={})
        assert False
    except ValueError:
        pass
    try:
        dump(replay_dir='', template_name='t', context={'cookiecutter':{}})
        assert True
    except ValueError:
        assert False
    # tear down
    os.remove('t.json')


# Generated at 2022-06-13 18:41:54.666009
# Unit test for function load
def test_load():
    # Template_name is required to be str
    try:
        load('fake', 1)
        assert False
    except TypeError:
        assert True

    # Context is required to have 'cookiecutter' in it
    try:
        load('fake', 'fake')
        assert False
    except ValueError:
        assert True

    # If template_name is str, returns dict
    assert isinstance(load('fake', 'fake'), dict)

# Unit tests for function dump

# Generated at 2022-06-13 18:41:56.153865
# Unit test for function load
def test_load():
    assert load('./cookiecutter_pypackage', 'cookiecutter_pypackage') != None


# Generated at 2022-06-13 18:42:04.717991
# Unit test for function load
def test_load():
    # create a test_dir
    test_dir = '/home/kevj'
    test_template = 'test_template'
    
    # create a test context
    test_context = {
        'cookiecutter': {
            'full_name': 'Kev Jones',
            'email': 'kevjones1989@gmail.com',
            'has_replay': 'y',
            'replay_dir': test_dir
        }
    }
    dump(test_dir, test_template, test_context)
    output_context = load(test_dir, test_template)
    assert test_context == output_context



# Generated at 2022-06-13 18:42:08.076916
# Unit test for function load
def test_load():
    context = {"cookiecutter": {
        "full_name": "Your Name",
        "email": "youremail@domain.com",
        "repo_name": "myrepo",
        "project_name": "myproject"
    }}
    replay_dir = 'tests/files/replay/'
    template_name = 'test_template'
    dump(replay_dir, template_name, context)

    context_from_file = load(replay_dir, template_name)

    if context_from_file != context:
        raise ValueError('Context from file should be the same as context')

if __name__ == '__main__':
    test_load()

# Generated at 2022-06-13 18:42:11.398670
# Unit test for function load
def test_load():
    """Test load function."""
    context = load('/Users/fang/.cookiecutters', 'hackbright-projects')
    assert context == {u'cookiecutter': {u'full_name': u'Fang Wang'}}


# Generated at 2022-06-13 18:42:16.883754
# Unit test for function dump
def test_dump():
    replay_dir = '.travis/replay'
    template_name = 'template'
    context = {'cookiecutter': {'name': 'a', 'version': '0.1.0'}}
    dump(replay_dir, template_name, context) 
    file_name = get_file_name(replay_dir, template_name)
    assert os.path.isfile(file_name)
    os.remove(file_name)
    os.rmdir(replay_dir)


# Generated at 2022-06-13 18:42:22.011768
# Unit test for function load
def test_load():
    replay_dir = 'tests/files/tests/replay_dir/'
    template_name = 'fake-repo-pre/'
    context = load(replay_dir, template_name)
    assert context['cookiecutter']['full_name'] == "Your Name"
    assert context['cookiecutter']['email'] == 'your.name@gmail.com'
    assert context['cookiecutter']['github_username'] == 'your-name'
    assert context['cookiecutter']['project_name'] == "Your Name"
    assert context['cookiecutter']['project_slug'] == 'your-name'
    assert context['cookiecutter']['pypi_username'] == 'your-name'
    assert context['cookiecutter']['description'] == 'Common files for your projects'


# Generated at 2022-06-13 18:42:28.062193
# Unit test for function load
def test_load():
    global template_name
    template_name = 'example_baselined'
    replay_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'replay')
    replay_file = os.path.join(replay_dir, template_name + '.json')
    if os.path.isfile(replay_file):
        context = load(replay_dir, template_name)
        return context


if __name__ == "__main__":
    context = test_load()

# Generated at 2022-06-13 18:42:34.891748
# Unit test for function dump
def test_dump():
    replay_dir = os.path.join('tests',"test_replay_dir")
    template_name = "test"
    
    make_sure_path_exists(replay_dir)
    context_entry = {"cookiecutter": {"exercise": "name"}}
    context = {"cookiecutter": {"exercise": "name"}}
    for i in range(0,3):
        context.update(context_entry)
    context["cookiecutter"].update({"exercise": "name"})
    dump(replay_dir, template_name, context)
    context2 = load(replay_dir, template_name)
    assert(context == context2)


# Generated at 2022-06-13 18:42:39.374672
# Unit test for function dump
def test_dump():
    replay_dir = './data'
    template_name = 'frame'
    context = {
        'cookiecutter': {
            'project_name': 'frame',
            'repo_name': 'frame',
        },
    }

    dump(replay_dir, template_name, context)

    assert os.path.exists(os.path.join(replay_dir, template_name + '.json'))



# Generated at 2022-06-13 18:42:50.695904
# Unit test for function load
def test_load():
    """Test the load function."""
    # Get the path to this file
    path = os.path.dirname(__file__)
    # Load the context for this file
    data = load('replay_dir','replay')
    # Assert that the results of the load function are in the expected format
    try:
        assert isinstance(data,dict)
    except AssertionError:
        raise AssertionError("Output is not a dictionary")

# Generated at 2022-06-13 18:42:55.253239
# Unit test for function load
def test_load():
    context = load('D:\\cookiecutter\\project_template', 'kang-project')
    print(context)
    print(context['cookiecutter']['project_name'])


if __name__ == '__main__':
    test_load()

# Generated at 2022-06-13 18:42:58.031768
# Unit test for function load
def test_load():
    replay_file = get_file_name(replay_dir, template_name)
    print (replay_file)
    context = load(replay_dir, template_name)
    print (context)



# Generated at 2022-06-13 18:43:04.525240
# Unit test for function load
def test_load():
    """Test that load works as expected."""
    template_name = 'test_template_name'
    replay_dir = './test_replay_dir'
    context = {'cookiecutter': {'data': 'test_data'}}
    dump(replay_dir, template_name, context)
    loaded_context = load(replay_dir, template_name)
    assert loaded_context == context

# Generated at 2022-06-13 18:43:06.185884
# Unit test for function load
def test_load():
    """Test load function."""
    assert load('replay', 'foo') == {}



# Generated at 2022-06-13 18:43:11.904567
# Unit test for function load
def test_load():
    print('\nRuning Unit Test for function load...')
    # Test 1
    replay_dir = r'd:\temp'
    template_name = 'test1'
    context = {
        'cookiecutter': {
            'project_name': 'test1.project.name',
            'replay_dir': 'test1.replay.dir',
            'template_name': 'test1.template.name'
        }
    }
    dump(replay_dir, template_name, context)
    context = load(replay_dir, template_name)
    assert context['cookiecutter']['project_name'] == 'test1.project.name'
    assert context['cookiecutter']['replay_dir'] == 'test1.replay.dir'

# Generated at 2022-06-13 18:43:21.563329
# Unit test for function load
def test_load():
    context1 = {'cookiecutter': {'author_name': 'vaibhav'}}
    dumptest = load('./cookiecutter-pypackage/tests/test_dump', 'default')
    assert (context1 == dumptest)
    assert (dumptest['cookiecutter']['author_name'] == 'vaibhav')
    assert (dumptest['cookiecutter']['full_name'] == 'vaibhav choudhary')
    assert (dumptest['cookiecutter']['email'] == 'vaibhav.iitk@gmail.com')
    assert (dumptest['cookiecutter']['boilerplate'] == 'no')

# Generated at 2022-06-13 18:43:24.566075
# Unit test for function load
def test_load():
    assert(load('/Users/shaoxian/Desktop/cookiecutter-jupyter', 'cookiecutter-jupyter').get('cookiecutter') is not None)


# Generated at 2022-06-13 18:43:32.874168
# Unit test for function load
def test_load():
    assert isinstance(load(replay_dir, template_name), dict)


# Generated at 2022-06-13 18:43:38.902290
# Unit test for function load
def test_load():
    import shutil
    import tempfile

    tempdir = tempfile.mkdtemp()
    dump(tempdir, 'bar', {'cookiecutter': {'foo': 'bar'}})
    context = load(tempdir, 'bar')
    shutil.rmtree(tempdir)
    assert context['cookiecutter']['foo'] == 'bar'



# Generated at 2022-06-13 18:43:47.841512
# Unit test for function dump
def test_dump():
    """Test dump function."""
    replay_dir = 'C:\\Users\\soporte_it\\AppData\\Local\\Temp\\replay'
    template_name = 'another_cookiecutter_template'

# Generated at 2022-06-13 18:43:49.653785
# Unit test for function load
def test_load():
    assert load("/tmp/replay_dir", "foo") == {'cookiecutter': {}}

# Generated at 2022-06-13 18:43:56.348904
# Unit test for function load
def test_load():
    replay_dir = 'C:\\Users\\lihui\\PycharmProjects\\cookiecutter\\tests\\test-replay'
    template_name = 'tests\\test-repo-pre'
    # template_name = 'tests\\test-repo-pre'
    replay_file = get_file_name(replay_dir, template_name)
    with open(replay_file, 'r') as infile:
        context = json.load(infile)
    print(context)
    print(type(context))


# Generated at 2022-06-13 18:44:01.687115
# Unit test for function load
def test_load():
    replay_dir = os.path.dirname(os.path.realpath(__file__))
    template_name = "replay_file"
    context = load(replay_dir, template_name)
    print(context['cookiecutter']['cookiecutter_dict_example'])
    print(context['cookiecutter']['cookiecutter_list_example'])


# Generated at 2022-06-13 18:44:05.478911
# Unit test for function load
def test_load():
    test_dir = os.path.dirname(os.path.realpath(__file__))
    replay_dir = os.path.join(test_dir, 'test_replay')

    assert(load(replay_dir, 'test') == {'cookiecutter': 'test'})



# Generated at 2022-06-13 18:44:07.758625
# Unit test for function load
def test_load():
    assert load('./replay', 'unit_test_cc')['cookiecutter']['project_name'] == 'Unit Test Cookiecutter'

# Generated at 2022-06-13 18:44:15.362901
# Unit test for function load
def test_load():
    context = load('replay', 'blaze')
    assert(context['cookiecutter']['project_name'] == 'Blaze')
    assert(context['cookiecutter']['pip_package_name'] == 'blaze')
    assert(context['cookiecutter']['pypi_username'] == 'Blaze')
    assert(context['cookiecutter']['project_short_description'] == 'Blazing fast Python Dask')
    assert(context['cookiecutter']['use_pip'] == 'y')
    assert(context['cookiecutter']['use_pytest'] == 'y')
    assert(context['cookiecutter']['use_docker'] == 'y')
    assert(context['cookiecutter']['open_source_license'] == 'MIT license')

# Generated at 2022-06-13 18:44:24.483609
# Unit test for function load
def test_load():
    """Unit test for function load."""
    test_context = {"cookiecutter": {"this": "works"}}
    test_template_name = 'test_template_name'

    replay_dir = 'test_replay_dir'
    replay_file_name = get_file_name(replay_dir, test_template_name)
    if os.path.exists(replay_file_name):
        os.remove(replay_file_name)

    dump(replay_dir, test_template_name, test_context)
    load_context = load(replay_dir, test_template_name)

    assert load_context["cookiecutter"]["this"] == test_context["cookiecutter"]["this"]

# Generated at 2022-06-13 18:44:42.023078
# Unit test for function load
def test_load():
    """Test for function load."""
    import json
    testdict = {'cookiecutter': {'full_name': 'Yvonne Ortega', 'email': 'yvonneortega@gmail.com'}}
    template_name = "testtemplate.json"
    replay_dir = "testing"
    dump(replay_dir, template_name, testdict)
    context = load(replay_dir, template_name)
    print(context)

# Generated at 2022-06-13 18:44:44.320941
# Unit test for function load
def test_load():
    load('C:\\cygwin64\\home\\joycehe\\programming\\python\\cookiecutter', 'json')



# Generated at 2022-06-13 18:44:47.019929
# Unit test for function load
def test_load():
    """Unit test for function load."""
    file_dir = os.path.dirname(os.path.realpath('__file__'))
    file_path = os.path.join(file_dir, 'tests/test-replay/')
    print(load(file_path, "cookiecutter.json"))



# Generated at 2022-06-13 18:44:53.669243
# Unit test for function load
def test_load():
    replay_dir = 'test_load'
    template_name = 'test_load'
    context = {'cookiecutter': {'project_name': 'test_load'}}
    dump(replay_dir, template_name, context)
    context2 = load(replay_dir, template_name)
    assert context == context2

# Generated at 2022-06-13 18:45:03.575350
# Unit test for function load
def test_load():
    replay_dir = "test"
    template_name = "test.json"
    if not make_sure_path_exists(replay_dir):
        raise IOError('Unable to create replay dir at {}'.format(replay_dir))

    if not isinstance(template_name, str):
        raise TypeError('Template name is required to be of type str')

    context = {"cookiecutter": { "replay_dir": "test", "template_name": "test.json"}}

    if 'cookiecutter' not in context:
        raise ValueError('Context is required to contain a cookiecutter key')

    replay_file = get_file_name(replay_dir, template_name)


# Generated at 2022-06-13 18:45:08.680274
# Unit test for function dump
def test_dump():
    base = 'tmp'
    template = 'foo'
    context = {'cookiecutter': {'bar': 'baz'}}

    dump(base, template, context)
    assert os.path.exists("tmp/foo.json")
    # Cleanup
    os.remove("tmp/foo.json")
    os.rmdir("tmp")


# Generated at 2022-06-13 18:45:13.728847
# Unit test for function dump
def test_dump():
    """A unit test for the dump function.
    """
    import shutil
    replay_dir = 'replay-data'
    
    try:
        context = {'cookiecutter': {'a': 1, 'b': 2, 'c': 3, 'd': 4}}
        dump('replay-data', 'test_a', context)
        dump('replay-data', 'test_a.json', context)
    finally:
        shutil.rmtree(replay_dir)
        

# Generated at 2022-06-13 18:45:15.736245
# Unit test for function load
def test_load():
    data = load("C:\git\cookiecutter\cookiecutter\replay", "stdlib.json")

# Generated at 2022-06-13 18:45:23.545484
# Unit test for function load
def test_load():
    replay_dir = './tests/files'
    template_name = 'test'
    file_name = get_file_name(replay_dir, template_name)
    if os.path.isfile(file_name):
        os.remove(file_name)
    context = {'cookiecutter': {'project_name': 'Hello World', 'author_name': 'PQD'}}
    dump(replay_dir, template_name, context)
    assert os.path.isfile(file_name)
    assert load(replay_dir, template_name) == context
    os.remove(file_name)


# Generated at 2022-06-13 18:45:25.899805
# Unit test for function load
def test_load():
    load('/home/alan/Documents/python/workshop/cookiecutter-pypackage/tests/test_replay', 'package')


# Generated at 2022-06-13 18:45:53.075135
# Unit test for function load
def test_load():
    """Test load function."""
    template_name = 'pyramid_cookiecutter_alchemy'
    replay_dir = os.path.join(os.path.dirname(__file__), '..', 'replay')
    context = load(replay_dir, template_name)

    assert(isinstance(context, dict))
    assert('cookiecutter' in context)
    assert('full_name' in context['cookiecutter'])

# Generated at 2022-06-13 18:46:00.454166
# Unit test for function load
def test_load():
    """Unit test for load."""
    # Arrange
    from click.testing import CliRunner
    from cookiecutter.cli import main
    from cookiecutter.exceptions import NonTemplatedInputDirException
    import shutil
    import tempfile
    
    output_dir = tempfile.mkdtemp()
    temp_dir = tempfile.mkdtemp()
    shutil.copytree(
        os.path.join(
            os.path.dirname(os.path.abspath(__file__)), 'test-template'
        ),
        os.path.join(temp_dir, 'test-template')
    )
    template = os.path.join(temp_dir, 'test-template')
    
    os.mkdir(os.path.join(temp_dir, '.cookiecutters'))
    

# Generated at 2022-06-13 18:46:03.016272
# Unit test for function load
def test_load():
    """Unit test for function load."""
    template_name = 'python-hello-world-2019-03-25-19-13-13'
    context = load('/home/zhaozhou/workspace/replay', template_name)
    print(context)



# Generated at 2022-06-13 18:46:08.537212
# Unit test for function load
def test_load():
    template_name = "test"
    context={"cookiecutter": {"full_name": "Alain", "email": "test@test.test"}}
    replay_dir = "test"

    dump(replay_dir, template_name, context)
    new_context = load(replay_dir, template_name)
    assert new_context["cookiecutter"]["full_name"] == context["cookiecutter"]["full_name"]
    assert new_context["cookiecutter"]["email"] == context["cookiecutter"]["email"]

test_load()

# Generated at 2022-06-13 18:46:15.859070
# Unit test for function dump
def test_dump():
    """
    Test for dump.
    """
    import tempfile
    from cookiecutter.config import get_user_config

    user_config = get_user_config()

    user_config['replay_dir'] = tempfile.gettempdir()
    user_config['replay'] = True

    replay_dir = user_config['replay_dir']
    replay_file = get_file_name(replay_dir, 'cookiecutter-pypackage')

    # Remove any existing replay file
    if os.path.exists(replay_file):
        os.remove(replay_file)

    context = {
        'cookiecutter': {'full_name': 'Test Python Developer'}
    }

    dump(replay_dir, 'cookiecutter-pypackage', context)


# Generated at 2022-06-13 18:46:22.830519
# Unit test for function dump

# Generated at 2022-06-13 18:46:26.122756
# Unit test for function load
def test_load():
    template_name = 'python_package'
    replay_dir = 'cookiecutter-replay'
    context = load(replay_dir, template_name)
    assert context is not None

# Generated at 2022-06-13 18:46:31.959390
# Unit test for function load
def test_load():
    load('/home/user/.cookiecutters', 'cookiecutter_pypackage')
    load('/home/user/.cookiecutters', 'cookiecutter_pypackage.json')
    load('/home/user/.cookiecutters', 'cookiecutter_pypackage.JSO')

# Generated at 2022-06-13 18:46:36.110544
# Unit test for function load
def test_load():
    rd = 'replay_dir'
    tn = 'bingo'
    cc = 'cookiecutter'
    context = {cc: {}}
    dump(rd, tn, context)
    ans = load(rd, tn)

# Generated at 2022-06-13 18:46:39.123243
# Unit test for function dump
def test_dump():
    replay_dir="this/is/a/test/replay"
    template_name="{{cookiecutter.project_name.replace(' ', '')}}.sublime-project"
    context={'foo': 'bar'}
    dump(replay_dir, template_name, context)

# Generated at 2022-06-13 18:47:36.170706
# Unit test for function dump
def test_dump():
    context = {}
    context['cookiecutter'] = {}
    context['cookiecutter']['full_name'] = 'Siddhartha Kotharu'
    context['cookiecutter']['email'] = 'siddhartha@protonmail.com'
    context['cookiecutter']['github_username'] = 'sidkot'
    context['cookiecutter']['project_name'] = 'speedsters'
    context['cookiecutter']['project_slug'] = 'speedsters'
    context['cookiecutter']['py_module'] = 'speedsters'
    context['cookiecutter']['pypi_user'] = 'sidkot'
    context['cookiecutter']['project_short_description'] = 'Speedsters is a Python package for producing summary statistics of dataframes'

# Generated at 2022-06-13 18:47:41.690860
# Unit test for function load
def test_load():
    replay_dir = '../cookiecutter-pypackage/cookiecutter.replay'
    template_name = 'cookiecutter-pypackage'
    context = load(replay_dir, template_name)
    print(context)
    assert(context != None)

if __name__ == '__main__':
    test_load()

# Generated at 2022-06-13 18:47:47.275123
# Unit test for function dump
def test_dump():
    from cookiecutter.config import get_user_config
    config_dict = get_user_config()
    replay_dir = config_dict['replay_dir']
    template_name = 'test_project'
    context = {'cookiecutter': {'project_name':'test_project'}, 'full_name': 'Yanyan Zhao', 'email': 'zhaoyanyan@gene.com'}
    replay = dump(replay_dir, template_name, context)
    assert os.path.exists(os.path.join(replay_dir, 'test_project.json'))


# Generated at 2022-06-13 18:47:52.284325
# Unit test for function load
def test_load():
    context = load(replay_dir='tests', template_name='cookiecutter-pypackage')
    assert 'cookiecutter' in context
    assert 'project_name' in context['cookiecutter']
    assert context['cookiecutter'].get('project_name') == 'Cookiecutter PyPackage Skeleton'


# Generated at 2022-06-13 18:48:01.363569
# Unit test for function load
def test_load():
    print("testing load")
    input_template_name = 'foo'
    input_context = [
        {
            'cookiecutter': {
                'author_name': 'Renan Ivo',
                'project_name': 'Test Project',
                'project_slug': 'test-project',
                'project_description': 'Test project description',
                'src_project_slug': 'test-project',
                'use_pypi_deployment_with_travis': False,
                'open_source_license': 'None',
                'python_version': '2.7',
            }
        }
    ]

    replay_dir = os.path.join('tests', 'test-replay')

    # Create a test json file in a test directory

# Generated at 2022-06-13 18:48:13.815169
# Unit test for function load
def test_load():

    if not make_sure_path_exists('.cookiecutters'):
        raise IOError('Unable to create replay dir at {}'.format('.cookiecutters'))

    if not isinstance('.', str):
        raise TypeError('Template name is required to be of type str')

    replay_file = get_file_name('.', '.cookiecutters')

    with open(replay_file, 'r') as infile:
        context = json.load(infile)

    if 'cookiecutter' not in context:
        raise ValueError('Context is required to contain a cookiecutter key')

    return context