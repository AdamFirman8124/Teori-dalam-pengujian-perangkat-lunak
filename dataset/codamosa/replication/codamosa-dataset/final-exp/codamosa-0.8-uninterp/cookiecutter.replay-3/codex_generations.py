

# Generated at 2022-06-13 18:38:08.745415
# Unit test for function dump
def test_dump():
    template_name = "test_template"
    context = {'cookiecutter': {'test_dir': 'test_dir_val'}}
    try:
        dump('test_dir', template_name, context)
    except Exception:
        assert False
    assert True


# Generated at 2022-06-13 18:38:18.289240
# Unit test for function dump
def test_dump():

	file_name = "tests/test_replay/test_replay.json"
	template_name = 'test_replay.json'
	context = {'cookiecutter':{'name':"vivian"}}

	dump(template_name, context)

	assert os.path.exists(file_name)

	with open(file_name, 'r') as infile:
		test_context = json.load(infile)

	assert context == test_context

	try:
		invalid_context = {'name':'vivian'}
		dump(template_name, invalid_context)
	except ValueError:
		print("'cookiecutter' key doesn't exist in the context")
	else:
		assert False

	os.remove(file_name)

# Unit test

# Generated at 2022-06-13 18:38:22.847062
# Unit test for function load
def test_load():
    template_name = 'template'
    replay_dir = './replay_dir'
    context = {'cookiecutter': {'name': 'template'}}
    dump(replay_dir, template_name, context)
    try:
        result = load(replay_dir, template_name)
    except Exception as e:
        print(e)


# Generated at 2022-06-13 18:38:27.192173
# Unit test for function load
def test_load():
    """Test if it can load a JSON file and return a dictionary."""
    replay_file = load(os.path.join(os.path.expanduser('~'), '.cookiecutters'), 'github.com/audreyr/cookiecutter-pypackage')
    assert isinstance(replay_file, dict)


# Generated at 2022-06-13 18:38:30.102455
# Unit test for function load
def test_load():
    # example of replay context
    expected = {'cookiecutter': {'date_created': '2010-01-01', 'project_name': 'Project Name'}}
    assert load('.', 'cookiecutter-pypackage-minimal') == expected

# Generated at 2022-06-13 18:38:33.185497
# Unit test for function get_file_name
def test_get_file_name():
    template_name = "fake_template_name"
    replay_dir = os.path.expanduser('~/.cookiecutter_replay')
    result = get_file_name(replay_dir,template_name)
    assert result == replay_dir + "/fake_template_name.json"

# Generated at 2022-06-13 18:38:38.241311
# Unit test for function get_file_name
def test_get_file_name():
    """Get file names of replay files."""
    replay_dir = '/test/dir'
    template = 'test'
    suffix = '.json'
    test_fn = 'test.json'

    template_with_suffix = 'test.json'
    test_fn_with_suffix = 'test.json'

    assert get_file_name(replay_dir, template) == os.path.join(replay_dir, test_fn)
    assert get_file_name(replay_dir, template_with_suffix) == os.path.join(replay_dir, test_fn_with_suffix)



# Generated at 2022-06-13 18:38:44.342193
# Unit test for function load
def test_load():
    with open('load_data.json', 'w') as outfile:
        json.dump({'cookiecutter': {'project_name': 'jello'}}, outfile)
    context = load('.', 'load_data')
    if context['cookiecutter']['project_name'] == 'jello':
        print('Unit test for load PASSED')
    else:
        print('Unit test for load FAILED')


# Generated at 2022-06-13 18:38:45.558386
# Unit test for function get_file_name
def test_get_file_name():
    if get_file_name('replay_dir', 'template') != 'replay_dir/template.json':
        raise ValueError("Something went wrong")


# Generated at 2022-06-13 18:38:49.439828
# Unit test for function get_file_name
def test_get_file_name():
    replay_dir = 'test_data/'
    template_name = 'test'
    assert 'test_data/test.json' == get_file_name(replay_dir, template_name)
    template_name = 'test.json'
    assert 'test_data/test.json' == get_file_name(replay_dir, template_name)


# Generated at 2022-06-13 18:39:03.301169
# Unit test for function dump
def test_dump():
    # Initialize replay directory
    replay_dir = '.cookiecutters'
    make_sure_path_exists(replay_dir)

    # Store a context into a dictionary
    store_context = {
        "cookiecutter": {
            "project_name": "foobar",
            "duration": "5",
        }
    }

    # Use dump function to save the context into replay file
    template_name = 'obscure-repo-name'
    dump(replay_dir, template_name, store_context)

    # Load the context from replay file
    load_context = load(replay_dir, template_name)

    # Assert the equality of two contexts
    assert load_context == store_context

    # Remove the replay file

# Generated at 2022-06-13 18:39:06.558478
# Unit test for function dump
def test_dump():
    template_name = 'template_name'
    context = {
        'cookiecutter': {
            'full_name': 'Test User',
            'email': 'testuser@example.com',
        }
    }
    
    try:
        dump(replay_dir, template_name, context)
    except Exception as e:
        assert False



# Generated at 2022-06-13 18:39:13.505006
# Unit test for function load
def test_load():
    replay_dir = '.'
    template_name = '.'
    file_name = 'cookiecutter.json'
    if not make_sure_path_exists(replay_dir):
        raise IOError('Unable to create replay dir at {}'.format(replay_dir))

    if not isinstance(template_name, str):
        raise TypeError('Template name is required to be of type str')
    template_name = '.json'
    replay_file = get_file_name(replay_dir, template_name)

    with open(replay_file, 'r') as infile:
        context = json.load(infile)

    if 'cookiecutter' not in context:
        raise ValueError('Context is required to contain a cookiecutter key')

# Generated at 2022-06-13 18:39:17.368327
# Unit test for function load
def test_load():
    a=load('/home/lohias/.cookiecutters/cookiecutter-pypackage-minimal/', 'cookiecutter.json')
    print(a)

if __name__ == '__main__':
    test_load()

# Generated at 2022-06-13 18:39:24.392231
# Unit test for function dump
def test_dump():

    # setup
    replay_dir = '/home/tom/'
    template_name = 'first_project'
    context = {'cookiecutter':{'pytho_interpreter':'python3'}}

    # execute
    dump(replay_dir, template_name, context)

    # assert
    path = get_file_name(replay_dir, template_name)
    assert os.path.isfile(path)

    # tear down
    os.remove(path)


# Generated at 2022-06-13 18:39:27.953656
# Unit test for function load
def test_load():
    """Unit test for function load"""
    from tempfile import mkdtemp

    template_name = 'cookiecutter-pypackage'
    replay_dir = os.path.join(mkdtemp(), 'cookiecutter-replay')
    context = load(replay_dir, template_name)
    print(context)



# Generated at 2022-06-13 18:39:35.995273
# Unit test for function dump
def test_dump():
    import random
    import tempfile
    import os
    replay_dir = tempfile.mkdtemp()
    template_name = 'ex_dump'
    context = {
        'cookiecutter': {},
        'replay': {
            'cookiecutter': {},
            'replay': {}
        }
    }
    dump(replay_dir, template_name, context)
    assert os.path.exists(get_file_name(replay_dir, template_name))
    assert os.path.getsize(get_file_name(replay_dir, template_name)) > 0
    # Assert that the file contains the expected number of lines
    lines = load(replay_dir, template_name)
    if lines != context:
        raise ValueError("Incorrect file contents. Different to actual.")



# Generated at 2022-06-13 18:39:38.368412
# Unit test for function load
def test_load():
    replay_dir = '/home/akshay/cookiecutter-test/cookiecutter_test/.cookiecutter-replay'
    template_name = 'test'
    context = load(replay_dir, template_name)
    assert context is not None
    print(context)


# Generated at 2022-06-13 18:39:44.555087
# Unit test for function load
def test_load():
    context = {
        "cookiecutter": {
            "replay_dir" : "tests/"
        }
    }

    context = load(context['cookiecutter']['replay_dir'], 'default')
    assert context != None



# Generated at 2022-06-13 18:39:48.714674
# Unit test for function load
def test_load():
    t = load('/home/genius/Documents/1Semester/dip/cookiecutter/cookiecutter/replay', 'default')
    print(t)


# Generated at 2022-06-13 18:39:58.158904
# Unit test for function dump
def test_dump():
    
    replay_dir = './'
    template_name = 'test_dump_test'

# Generated at 2022-06-13 18:40:07.119922
# Unit test for function load
def test_load():
    """Test load function
    """
    test_replay_dir = 'tests/test-replay'
    test_load_context = load(test_replay_dir, 'test-template')
    test_load_context_bad_file = load(test_replay_dir, 'test-template-bad')
    assert isinstance(test_load_context, dict)
    assert test_load_context.get('cookiecutter', None) is not None
    assert isinstance(test_load_context_bad_file, dict)
    assert test_load_context_bad_file.get('cookiecutter', None) is not None


# Generated at 2022-06-13 18:40:11.666491
# Unit test for function load
def test_load():
    replay_dir = 'D:\\'
    template_name = 'test_example'
    context = {'cookiecutter': {'first_name': 'First', 'last_name': 'Last', 'email': 'first@example.com', 'replay_dir': 'D:\\', 'replay': 'True'}}
    dump(replay_dir, template_name, context)
    context2 = load(replay_dir, template_name)
    assert (context == context2)
    os.remove(get_file_name(replay_dir, template_name))

# Generated at 2022-06-13 18:40:14.412347
# Unit test for function load
def test_load():
    assert load('~/work/cookiecutter-test/test', 'test_template')


# Generated at 2022-06-13 18:40:17.736345
# Unit test for function load
def test_load():
    from sys import argv
    if len(argv) == 2:
        dirname = argv[1]
        load(dirname, 'test-repo')

# Generated at 2022-06-13 18:40:23.217958
# Unit test for function load
def test_load():
    replay_dir = os.path.join(os.getcwd(), 'replay_dir')
    template_name = 'python'
    assert len(load(replay_dir, template_name)) >= 1, 'No keys in the context'
    assert 'cookiecutter' in load(replay_dir, template_name).keys(), 'No cookiecutter in context keys'
    assert isinstance(load(replay_dir, template_name), dict), 'Context is not a dictionary'
    assert isinstance(load(replay_dir, template_name)['cookiecutter'], dict), 'cookiecutter is not a dictionary'

# Generated at 2022-06-13 18:40:25.022549
# Unit test for function load
def test_load():
    context = load('replay_dir', 'template_name')
    

# Generated at 2022-06-13 18:40:26.105057
# Unit test for function dump
def test_dump():
	return


# Generated at 2022-06-13 18:40:35.367023
# Unit test for function load
def test_load():
    from cookiecutter import utils
    from cookiecutter.vcs import clone
    from cookiecutter.main import cookiecutter
    from shutil import rmtree
    import tempfile
    import os

    cookiecutters = 'https://github.com/audreyr/cookiecutter-pypackage.git'
    output = cookiecutter(cookiecutters)
    context = load(output['cookiecutter']['replay_dir'],template_name="cookiecutter-pypackage")
    assert context == output['cookiecutter']
    rmtree(output['cookiecutter']['replay_dir'])


# Generated at 2022-06-13 18:40:40.916574
# Unit test for function dump
def test_dump():
    replay_dir = 'testreplaydir'
    template_name = 'testtemplatename'
    context = {
        "cookiecutter":
            {
                "full_name": "Audrey Roy",
                "email": "audreyr@example.com",
                "org_name": "Your Organization",
                "repo_name": "hello_world_pytest"
            }
    }
    dump(replay_dir, template_name, context)


# Generated at 2022-06-13 18:40:43.682517
# Unit test for function load
def test_load():
    assert(load("replay_dir", "template_name") == context)


# Generated at 2022-06-13 18:40:51.632923
# Unit test for function load
def test_load():
    import tempfile
    import shutil
    test_dir = tempfile.mkdtemp()

    tmpl_context_file = os.path.join(test_dir, 'test_tmpl.json')
    tmpl_context = {'cookiecutter': {'full_name': 'John Doe', 'email': 'jdoe@example.com'}}
    with open(tmpl_context_file, 'w') as outfile:
        json.dump(tmpl_context, outfile, indent=2)

    assert load(test_dir, 'test_tmpl') == tmpl_context

    shutil.rmtree(test_dir)

# Generated at 2022-06-13 18:40:56.142294
# Unit test for function load
def test_load():
    """Test the load function"""
    replay_dir = os.path.join(os.path.dirname(__file__), '../')
    template_name = 'cookiecutter-pypackage'
    try:
        load(replay_dir, template_name)
    except ValueError:
        print('Error:Context is required to contain a cookiecutter key.')
    

# Generated at 2022-06-13 18:41:04.358006
# Unit test for function load
def test_load():
    replay_dir = os.path.join(
        os.path.abspath('.'),
        'tests',
        'replay',
        'cookiecutter-pypackage',
        'replay'
    )
    template_name = 'cookiecutter-pypackage'
    context = load(replay_dir, template_name)
    assert context['cookiecutter']['repo_name']=='cookiecutter-pypackage'
    #assert context['cookiecutter']['repo_name'] == 'cookiecutter-pypackage'


# Generated at 2022-06-13 18:41:10.871366
# Unit test for function load
def test_load():
    test_file = open("file_template.json", 'w+')

# Generated at 2022-06-13 18:41:21.430304
# Unit test for function dump
def test_dump():
    template_path = "."
    project_dir = "cookiecutter-pypackage"
    replay_dir = ".cookiecutters_replay"
    context = {"cookiecutter":
               {"full_name": "Audrey Roy",
                "email": "audreyr@example.com",
                "project_name": "Cookiecutter PyPackage",
                "project_short_description": "A Python package project template.",
                "pypi_username": "cookiecutter",
                "repo_name": "cookiecutter-pypackage",
                "year": "2015",
                "version": "0.1.0"}}

    dump(replay_dir, project_dir, context)

    actual_data = load(replay_dir, project_dir)
    expected_data = context
    
   

# Generated at 2022-06-13 18:41:27.266900
# Unit test for function dump
def test_dump():
    """Unit testing for function dump."""
    replay_dir = 'project_template/.replay'
    template_name = 'project_template'
    context = {
        'cookiecutter': {
            'replay_dir': '.replay',
            'replay': False,
            'no_input': False
        },
        'project_name': 'test_project',
        'project_dir': 'test_project',
        'full_name': 'test_user',
        'email': 'test_user@test.com',
        'short_description': 'test project',
        'version': '0.1.0',
        'open_source_license': 'MIT'
    }
    dump(replay_dir, template_name, context)


# Generated at 2022-06-13 18:41:28.762120
# Unit test for function load
def test_load():
    assert load('acookiecu', 'test')


# Generated at 2022-06-13 18:41:31.955010
# Unit test for function load
def test_load():
    assert isinstance(load('C:\\Users\\Michael\\Documents\\GitHub\\SHREC\\replay',
                           'C:\\Users\\Michael\\Documents\\GitHub\\SHREC\\poetry_template'), dict)


# Generated at 2022-06-13 18:41:33.255002
# Unit test for function load
def test_load():
    assert load('','cookiecutter') == None

# Generated at 2022-06-13 18:41:40.088442
# Unit test for function load
def test_load():
    replay_file = 'tests/files/replay/' + 'replay_test.json'
    with open(replay_file, 'r') as infile:
        context = json.load(infile)

    if 'cookiecutter' not in context:
        raise ValueError('Context is required to contain a cookiecutter key')
    print(context)

if __name__ == '__main__':
    test_load()

# Generated at 2022-06-13 18:41:41.978011
# Unit test for function load
def test_load():
    assert load('replay','curryking')['cookiecutter']['repo_name'] == 'CK'

# Generated at 2022-06-13 18:41:48.175562
# Unit test for function load
def test_load():
    """Unit test for function load."""
    template_name = "slug"
    context = {}
    context['commit_uri'] = "https://github.com/cookiecutter/cookiecutter.git"
    context['cookiecutter'] = {}
    context['cookiecutter']['repo_name'] = "repo_name"
    json_dump = json.dumps(context, indent=2)
    with open(get_file_name(".", template_name), 'w') as outfile:
        outfile.write(json_dump)
    context_load = load(".", template_name)
    assert context_load == context

# Generated at 2022-06-13 18:41:51.688038
# Unit test for function dump
def test_dump():
    context = {
        'cookiecutter':{
            'first_name':'Ananth',
            'last_name':'Hebbalalu',
            'email':'ananth@gmail.com',
            'github_username':'ananth',
            'project_name':'XYZ',
        }
    }
    dump('/tmp', 'ananth.json', context)
    assert context == load('/tmp', 'ananth.json')


# Generated at 2022-06-13 18:41:58.951337
# Unit test for function load
def test_load():
    # Set up variables
    replay_dir = os.path.join(os.path.dirname(__file__), 'replay')

# Generated at 2022-06-13 18:42:05.104333
# Unit test for function dump
def test_dump():
    replay_dir = 'tests/files/'
    template_name = 'test'
    context = {'cookiecutter': {'email': 'luochen1990@gmail.com'}}
    dump(replay_dir, template_name, context)
    replay_file = get_file_name(replay_dir, template_name)
    assert os.path.isfile(replay_file)
    os.remove(replay_file)


# Generated at 2022-06-13 18:42:08.350492
# Unit test for function dump
def test_dump():
    replay_dir = r'C:\Users\Adam\Desktop\hacker-news\test_replay'
    template_name = 'test_template_name'
    context = {"cookiecutter": {"test1": "test1", "test2": "test2"}}
    dump(replay_dir, template_name, context)
    # assert statements here


# Generated at 2022-06-13 18:42:15.448634
# Unit test for function dump
def test_dump():
    """Test for dump function."""
    if os.path.exists('/tmp/tests_cookiecutter'):
        os.remove('/tmp/tests_cookiecutter')
    replay_dir = '/tmp/tests_cookiecutter'
    template_name = 'example'
    context = {'cookiecutter': {'full_name': 'Audrey Roy Greenfeld', 'project_name': 'cookiecutter-pypackage'}}
    dump(replay_dir, template_name, context)
    assert os.path.exists('/tmp/tests_cookiecutter/example.json')

# Generated at 2022-06-13 18:42:20.998817
# Unit test for function load
def test_load():
    """Unit test for function load."""
    replay_dir = os.getcwd()
    template_name = 'cookiecutter-django'

# Generated at 2022-06-13 18:42:27.945471
# Unit test for function load
def test_load():
    replay_dir = os.path.join(os.path.dirname(__file__), os.pardir, 'tests', 'files', 'test-replay')
    template_name = 'simple-example'
    context = load(replay_dir, template_name)
    print(os.path.join(replay_dir, template_name))

    # Load simple-example (without any replays)
    assert context == {'cookiecutter': {'full_name': 'Firstname Lastname', 'email': 'email@example.org', 'github_username': 'audi0', 'project_name': 'simple-example'}}

# Generated at 2022-06-13 18:42:36.744389
# Unit test for function load
def test_load():
    """Test function load."""
    assert load('.', 'tests/fixtures/test-repo-tmpl') == {
        'cookiecutter': {
            'full_name': 'Audrey Roy Greenfeld',
            'email': 'audreyr@example.com',
            'project_name': 'test-project'
        }
    }

# Generated at 2022-06-13 18:42:39.169041
# Unit test for function dump
def test_dump():
    replay_dir = "C:/Users/haowe/Desktop/cookiecutter/"
    template_name = "haowe"
    context = {"cookiecutter": "123"}
    dump(replay_dir, template_name,context)



# Generated at 2022-06-13 18:42:41.266167
# Unit test for function load
def test_load():
    raw_context = load('project_slug', '/Users/username/cookiecutter-django/_cookiecutter.json')
    print(raw_context)


# Generated at 2022-06-13 18:42:47.663635
# Unit test for function dump
def test_dump():
    replay_dir = os.path.join(os.getcwd(), 'cookiecutter_replay')
    template_name = 'nanodegree_frontend'
    context = {'cookiecutter': {'full_name': 'TestUser', 'email': 'example@email.com'}}
    dump(replay_dir, template_name, context)



# Generated at 2022-06-13 18:42:57.736702
# Unit test for function load
def test_load():
    template_name = 'test_template'
    replay_dir = os.path.join(os.path.dirname(__file__), 'test_replay')
    replay_file = get_file_name(replay_dir, template_name)

    if os.path.exists(replay_dir):
        os.rmdir(replay_dir)

    context = load(replay_dir, template_name)
    assert context == {}
    assert os.path.exists(replay_dir)

    context = load(replay_dir, template_name)
    assert context == {}
    assert os.path.exists(replay_file)

# Generated at 2022-06-13 18:43:01.349834
# Unit test for function load
def test_load():
    dump('/tmp', 'example_template', {'cookiecutter': {'name': 'example_name'}})
    print(load('/tmp', 'example_template'))

test_load()

# Generated at 2022-06-13 18:43:10.236237
# Unit test for function load
def test_load():
    template_name = 'example_template'
    replay_dir = 'my_test_directory'
    assert make_sure_path_exists(replay_dir), 'test directory created successfully'
    replay_file = get_file_name(replay_dir,template_name)
    expected_context = {'cookiecutter': {'full_name': 'First Last',
                                              'email': 'me@example.com',
                                              'github_username': 'me',
                                              'project_name': 'My Project',
                                              'project_slug': 'my_project',
                                              'release_date': '2014-12-30',
                                              'version': '0.1.0'}}


# Generated at 2022-06-13 18:43:17.145478
# Unit test for function load
def test_load():
    """Unit test for function load"""
    template = "dummy-repo-template"
    replay_dir = "/tmp/cc_replay"
    context = {"cookiecutter":{"repo_dir": "/tmp/dummy-repo",},}
    dump(replay_dir, template, context)
    context_loaded = load(replay_dir, template)
    if context_loaded != context:
        raise Exception("load failed")
if __name__ == '__main__':
    test_load()

# Generated at 2022-06-13 18:43:24.743259
# Unit test for function dump
def test_dump():
    import sys
    test_dir = os.path.join(os.path.dirname(__file__), 'test')
    replay_dir = os.path.join(test_dir, 'replay')
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)
    if not os.path.exists(replay_dir):
        os.makedirs(replay_dir)
    template_name = 'test-repo/{{cookiecutter.test_key}}'
    context = {
        'cookiecutter': {
            'test_key': 'success',
        },
    }
    try:
        dump(replay_dir, template_name, context)
    except Exception as e:
        print(e)

# Generated at 2022-06-13 18:43:28.137755
# Unit test for function load
def test_load():
    sample_dir = os.path.join(os.path.dirname(__file__),
                              'tests', 'test-load-dir')

    assert isinstance(load(sample_dir, 'sample-context'), dict)



# Generated at 2022-06-13 18:43:41.456245
# Unit test for function load
def test_load():
    load(replay_dir='/Users/sgu/git_repo/cookiecutter/cookiecutter/replay', template_name='cookiecutter-pypackage')


# Generated at 2022-06-13 18:43:46.951148
# Unit test for function load
def test_load():
    import tempfile
    import shutil
    import os

    template_name = 'template_name'
    expected_context = {'cookiecutter': {'test': "It's working"}}
    with tempfile.TemporaryDirectory() as tmp_dir:
        dump(tmp_dir, template_name, expected_context)
        full_path = os.path.join(tmp_dir, template_name + '.json')
        assert os.path.exists(full_path)
        context = load(tmp_dir, template_name)
        assert context == expected_context
        assert os.path.exists(full_path)
    


# Generated at 2022-06-13 18:43:55.718748
# Unit test for function load
def test_load():
    """Test load function."""
    replay_dir = 'my_test'

    template_name = 'my_template'

    context = {'cookiecutter': {'full_name': 'Jane Doe'}}

    dump(replay_dir, template_name, context)

    file_name = get_file_name(replay_dir, template_name)

    assert os.path.isfile(file_name)

    context_loaded = load(replay_dir, template_name)

    assert isinstance(context_loaded, dict)

    assert context_loaded['cookiecutter'] == context['cookiecutter']

    os.remove(file_name)

# Generated at 2022-06-13 18:44:05.513927
# Unit test for function dump
def test_dump():
    """Unit test for function dump."""
    import tempfile, shutil
    context = {
        'cookiecutter': {
            'full_name': 'n/a',
            'email': 'n/a',
            'github_username': 'n/a',
        },
        'foobar': {
            'baz': 'buzz',
            'biz': 'buzz',
        },
    }
    tempdir = tempfile.mkdtemp()
    dump(tempdir, 'template', context)

    # open and read the file after the appending:
    replay_file = get_file_name(tempdir, 'template')
    with open(replay_file, "r") as f:
        content = json.loads(f.read())
    assert content == context

    # cleanup
    shutil.rmt

# Generated at 2022-06-13 18:44:07.023962
# Unit test for function load
def test_load():
    result = load('cookiecutter/tests/test-data', 'foobar')
    assert result != None

# Generated at 2022-06-13 18:44:13.745460
# Unit test for function load
def test_load():
    template_name = 'test1'
    context = {'cookiecutter': {'test': 'test2'}}

    # Test load
    replay_dir = '.cookiecutters'
    if os.path.exists(replay_dir):
        replay_file = get_file_name(replay_dir, template_name)
        os.remove(replay_file)
    dump(replay_dir, template_name, context)
    assert context == load(replay_dir, template_name)
    os.remove(replay_file)
    os.rmdir(replay_dir)


# Generated at 2022-06-13 18:44:16.867351
# Unit test for function load
def test_load():
    replay_dir = 'tests/test-output/replay'
    template_name = 'python_boilerplate'
    context = load(replay_dir, template_name)
    assert isinstance(context, dict)
    assert 'cookiecutter' in context
    print('load', context)
    return context


# Generated at 2022-06-13 18:44:26.903289
# Unit test for function dump
def test_dump():
    replays_dir = '../../cookiecutter-pypackage/tests/test-replay'

# Generated at 2022-06-13 18:44:28.030295
# Unit test for function dump
def test_dump():
    #TODO: add test here
    pass


# Generated at 2022-06-13 18:44:33.104811
# Unit test for function load
def test_load():
    """Unit test for function load."""
    replay_file = get_file_name('/home/me/cookiecutter/replay', 'template')
    new_file = '/home/me/cookiecutter/test.json'

# Generated at 2022-06-13 18:44:58.612325
# Unit test for function dump
def test_dump():
    """Unit test for dump"""
    os.mkdir("tmp")
    replay_dir = os.path.abspath("tmp")
    template_name = "test_dummy_project"
    cookiecutter_vars = {"cookiecutter": {}}
    dump(replay_dir, template_name, cookiecutter_vars)
    file_name = get_file_name(replay_dir, template_name)
    assert(os.path.isfile(file_name))
    os.remove("tmp/test_dummy_project.json")
    os.rmdir("tmp")


# Generated at 2022-06-13 18:45:04.052780
# Unit test for function dump
def test_dump():
    context = {
        "cookiecutter": {
            "name": "{{cookiecutter.project_name}}",
            "version": "{{cookiecutter.project_version}}",
            "author": "{{cookiecutter.project_author}}"
        },
        "project_name": "test",
        "project_version": "0.1.0",
        "project_author": "test"
    }
    file_name = 'test-dump.json'
    replay_dir = 'tests/data/'
    dump(replay_dir, file_name, context)
    new_context = load(replay_dir, file_name)
    assert(new_context == context)

if __name__ == '__main__':
    test_dump()

# Generated at 2022-06-13 18:45:12.040764
# Unit test for function dump
def test_dump():
    template_name = 'test'
    replay_dir = os.path.join('/tmp', 'cookiecutter-replay')
    context = {'cookiecutter': {'full_name': 'error'}}
    dump(replay_dir, template_name, context)
    context = {'cookiecutter': {'full_name': 'error'}, 'error': 'error'}
    dump(replay_dir, template_name, context)
    context = {'cookiecutter': {'full_name': 'error'}}
    dump(replay_dir, '', context)
    dump(replay_dir, '', 'context')


# Generated at 2022-06-13 18:45:19.767068
# Unit test for function load
def test_load():
    """ Unit test for load. """
    # Test IOError
    shutil.rmtree('/tmp/replay')
    with pytest.raises(IOError):
        load('/tmp/replay', 'template_name')

    # Test TypeError
    with pytest.raises(TypeError):
        load(1, 'template_name')
    with pytest.raises(TypeError):
        load('template_name', 1)
    
    # Create a test repla

# Generated at 2022-06-13 18:45:29.388832
# Unit test for function dump
def test_dump():
    """Test results of cookiecutter.replay.dump."""
    context = {
        "cookiecutter": {
            "full_name": "Audrey Roy Greenfeld",
            "email": "audreyr@example.com",
            "project_name": "Cookiecutter-pypackage-min",
            "repo_name": "cookiecutter-pypackage-min",
            "project_short_description": "A short description of the project.",
            "pypi_username": "audreyr",
            "release_date": "2013-07-07",
            "version": "0.1.0",
            "year": "2013",
            "version_added_to_module": "0.1"
        }
    }
    replay_dir = 'tests/test-replay'
   

# Generated at 2022-06-13 18:45:36.557606
# Unit test for function load
def test_load():
    replay_dir = os.path.join('/tmp', 'ccut')
    template_name = os.path.join(replay_dir, 'cookiecutter.json')
    replay_file = get_file_name(replay_dir, template_name)
    context = {'cookiecutter': 'ccut'}
    dump(replay_dir, template_name, context)
    data = load(replay_dir, template_name)
    print(data)
    if 'cookiecutter' not in data:
        print("FAIL")
    else:
        print("PASS")
    os.remove(replay_file)


#test_load()

# Generated at 2022-06-13 18:45:50.232660
# Unit test for function dump
def test_dump():

    replay_dir = os.path.abspath('cc-replay')
    template_name = 'potatocookie'

    context = {'cookiecutter':{'full_name':'Juz',
                               'email':'juz@gmail.com',
                               'replay_dir':replay_dir,
                               'template_name':template_name},
               'potato':'russet',
               'carrot':'orange'}

    dump(replay_dir, template_name, context)

    context_loaded = load(replay_dir, template_name)

    assert isinstance(context_loaded, dict)
    assert isinstance(context_loaded['cookiecutter'], dict)
    assert isinstance(context_loaded['potato'], str)

# Generated at 2022-06-13 18:45:58.657291
# Unit test for function load
def test_load():
    """Test function load."""
    # Load a valid file
    context = load(os.path.join(os.path.dirname(__file__), 'tests/fixtures/test-replay'), 'test')
    # Check that the cookiecutter key is in place
    assert 'cookiecutter' in context
    # Check that the file exists
    replay_file = get_file_name(os.path.join(os.path.dirname(__file__), 'tests/fixtures/test-replay'), 'test')
    assert os.path.exists(replay_file)
    # Check that the cookiecutter key is valid
    assert type(context['cookiecutter']) == dict
    # Check that the cookiecutter key has the relevant fields

# Generated at 2022-06-13 18:46:06.116995
# Unit test for function dump
def test_dump():
    """Unit test for function dump."""
    from tempfile import mkdtemp
    from shutil import rmtree
    from json import dumps

    DIR = mkdtemp()
    json_file = get_file_name(DIR, 'test_template')

    # Create directory (if it doesn't exist) and then dump info into it
    try:
        make_sure_path_exists(DIR)
        dump(DIR, 'test_template', {'cookiecutter': {}})

        with open(json_file) as f:
            json_str = f.read()
        assert dumps({'cookiecutter': {}}) == json_str

    except:
        print("Unit test for function dump in replay failed.")
    finally:
        try:
            rmtree(DIR)
        except:
            pass


# Unit

# Generated at 2022-06-13 18:46:12.314344
# Unit test for function dump
def test_dump():
    replay_dir='/home/c/.cookiecutters'
    template_name='apitest'
    context={
        "cookiecutter": {
            "full_name": "Gregory P. Smith",
            "email": "greg@krypto.org",
            "github_username": "gpshead",
            "project_name": "Python Test Project",
            "project_short_description": "A short description of the project.",
            "pypi_username": "greg",
            "version": "0.1.0",
            "release_date": "2015-12-17",
            "year": "2015",
            "project_license": "MIT license"
        }
    }
    dump(replay_dir,template_name,context)


# Generated at 2022-06-13 18:46:59.743451
# Unit test for function dump
def test_dump():
    replay_dir = '/tmp/replay'
    template_name = 'test'
    context = {'cookiecutter': {'other_key': 'other_value'}}
    dump(replay_dir, template_name, context)

    output = load(replay_dir, template_name)
    assert context == output



# Generated at 2022-06-13 18:47:02.724457
# Unit test for function load
def test_load():
    c=load('.','tests/fake-repo')
    assert c == {'cookiecutter': {'cloned_from': 'file:///d/test/github/cookiecutter-test-repo'}}



# Generated at 2022-06-13 18:47:08.670781
# Unit test for function load
def test_load():
    """Unit test for function load."""
    import pdb; pdb.set_trace()
    replay_dir = os.path.join(os.getcwd(),'tests', 'test-replay')
    template_name = 'test-template'
    c = load(replay_dir, template_name)
    assert 'cookiecutter' in c



# Generated at 2022-06-13 18:47:11.448479
# Unit test for function load
def test_load():
    assert(load('~/.cookiecutter_replay', '.')['cookiecutter']['project_name'] == 'hello_bob')

# Generated at 2022-06-13 18:47:22.983619
# Unit test for function load
def test_load():
    context = load('/home/vagrant/CloudComputing/cookiecutter/tests/test-replay', 'tests_only_repo')
    assert isinstance(context, dict)
    assert context['cookiecutter']['full_name'] == 'Audrey Roy Greenfeld'
    assert context['cookiecutter']['email'] == 'audreyr@example.com'
    assert context['cookiecutter']['project_name'] == "Cookiecutter Python Package"
    assert context['cookiecutter']['package_name'] == 'cookiecutter'
    assert context['cookiecutter']['repo_name'] == 'cookiecutter'
    assert context['cookiecutter']['year'] == '2012'
    assert context['cookiecutter']['github_username'] == 'audreyr'
    assert context

# Generated at 2022-06-13 18:47:24.861785
# Unit test for function load
def test_load():
	pass



# Generated at 2022-06-13 18:47:26.451773
# Unit test for function load
def test_load():
    # test loading invalid file
    load("this/is/not/a/path", "test")
    # test loading invalid file
    load("this/is/not/a/path", 1)

# Generated at 2022-06-13 18:47:34.355217
# Unit test for function load
def test_load():
    """Test function load."""
    template_name = 'ccut_test'
    replay_dir = './tests/replay'
    context = load(replay_dir, template_name)
    # test load function
    assert context is not None
    assert 'cookiecutter' in context
    assert 'full_name' in context['cookiecutter']
    assert 'repo_name' in context['cookiecutter']
    assert 'project_desc' in context['cookiecutter']
    assert 'year' in context['cookiecutter']
    assert 'version' in context['cookiecutter']
    assert 'email' in context['cookiecutter']

# Generated at 2022-06-13 18:47:38.458972
# Unit test for function load
def test_load():
    from cookiecutter.main import cookiecutter

    cookiecutter(
        'tests/test-repo',
        no_input=True,
        replay=True,
        replay_dir='tests/fake-replay-dir',
    )
    assert os.path.exists('tests/fake-replay-dir/fake-repo.json')
    assert load('tests/fake-replay-dir', 'fake-repo')



# Generated at 2022-06-13 18:47:43.846575
# Unit test for function load
def test_load():
    replay_dir = "/tmp"
    template_name = "test_load.json"
    context = {"cookiecutter": "cookiecutter"}
    dump(replay_dir, template_name, context)
    context2 = load(replay_dir, template_name)
    assert context == context2
    os.remove("/tmp/test_load.json")
