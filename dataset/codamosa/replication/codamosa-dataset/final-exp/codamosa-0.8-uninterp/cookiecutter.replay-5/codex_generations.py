

# Generated at 2022-06-13 18:38:07.512558
# Unit test for function dump
def test_dump():
    return None


# Generated at 2022-06-13 18:38:11.260647
# Unit test for function load
def test_load():
    replay_dir = '/home/cookiecutter-test'
    template_name = 'cookiecutter.json'
    context = load(replay_dir, template_name)
    # print context
    # print context.keys()
    assert u'cookiecutter' in context


# Generated at 2022-06-13 18:38:12.921488
# Unit test for function load
def test_load():
    assert not load('./crawler_settings', 'cookiecutter.json')



# Generated at 2022-06-13 18:38:22.527268
# Unit test for function dump
def test_dump():
    """Unit test for function dump."""
    # 'template_name' param should be a string
    try:
        dump('temp', 1, {})
    except TypeError as e:
        pass
    else:
        raise Exception("Didn't raise TypeError when 'template_name' is not a string")

    # 'context' param should be a dict
    try:
        dump('temp', 'foo', 1)
    except TypeError as e:
        pass
    else:
        raise Exception("Didn't raise TypeError when 'context' is not a dict")

    # 'context' param should contain a 'cookiecutter' key
    try:
        dump('temp', 'foo', {})
    except ValueError as e:
        pass

# Generated at 2022-06-13 18:38:26.194161
# Unit test for function load
def test_load():
    assert load('.','cake') == {'cookiecutter': {'art': 'big cake', 'size': '30'},'cake': {'flavour': 'vanilla','size': '30'}}#EDIT: 'cake' is a example, you don't need to write this

# Generated at 2022-06-13 18:38:34.161621
# Unit test for function load
def test_load():
    replay_dir = os.path.join(os.path.dirname(__file__), '..', 'tests', 'test-output')
    template_name = 'test'
    context = load(replay_dir, template_name)['cookiecutter']

# Generated at 2022-06-13 18:38:39.603445
# Unit test for function load
def test_load():
    template_name = 'template_name'
    replay_dir = os.path.abspath('./replays')
    with open('test_replay.json', 'r') as infile:
        expected_context = json.load(infile)
    context = load(replay_dir, template_name)
    assert context == expected_context, "Expected context does not match actual context"

# Generated at 2022-06-13 18:38:44.950254
# Unit test for function load
def test_load():
    os.mkdir('replay_dir')
    dict = {}
    dict['cookiecutter'] = 'template_name'
    dict['additional_context'] = 'random_context'
    dump('replay_dir', 'template_name', dict)
    context = load('replay_dir', 'template_name')
    print(context)



# Generated at 2022-06-13 18:38:47.787846
# Unit test for function load
def test_load():
    assert load('/Users/chunchengfang/Desktop/jupyter-repo/template/my-template-replay/', "context.json") == {'cookiecutter': {'full_name': 'Chuncheng Fang', 'email': 'chunchengfang@gmail.com', 'project_name': 'Jupyter Notebook', 'repo_name': 'jupyter-repo', 'repo_description': 'My Jupyter Notebook', 'year': '2019'}}

# Generated at 2022-06-13 18:38:53.245102
# Unit test for function load
def test_load():
    replay_dir = 'tests/test-replay'
    template_name = "tests/fake-repo-pre/{{cookiecutter.repo_name}}"
    assert load(replay_dir, template_name) == \
        {'cookiecutter': {}}

# Generated at 2022-06-13 18:39:06.457231
# Unit test for function load
def test_load():
    """Tests load function."""

# Generated at 2022-06-13 18:39:13.426287
# Unit test for function dump
def test_dump():
    temp_dir = tempfile.mkdtemp()

# Generated at 2022-06-13 18:39:17.691800
# Unit test for function load
def test_load():
    replay_dir = '/xxx/cookiecutter-pypackage'
    template_name = 'cookiecutter-pypackage'
    context = load(replay_dir,template_name)
    print(context)

if __name__ == '__main__':
    test_load()

# Generated at 2022-06-13 18:39:24.051149
# Unit test for function dump
def test_dump():
    replay_dir = '/home/ubuntu/workspace/git/cookiecutter/cookiecutter/tests/test-render/'
    template_name = 'test-render'
    context ={'cookiecutter': {'hello': 'world'}}

    dump(replay_dir, template_name, context)
    assert(os.path.isfile(replay_dir+template_name+'.json'))


# Generated at 2022-06-13 18:39:26.194722
# Unit test for function load
def test_load():
    context = load('/Users/chenchi/lab/cookiecutter/tests/test-replay/', 'projects')
    print(context)


# Generated at 2022-06-13 18:39:28.662398
# Unit test for function load
def test_load():
    context = load('.', 'cookiecutter.json')
    assert 'cookiecutter' in context
    assert 'username' in context['cookiecutter']
    assert 'email' in context['cookiecutter']


# Generated at 2022-06-13 18:39:30.293456
# Unit test for function load
def test_load():
    """Test function load."""
    assert load('./', 'template') != None



# Generated at 2022-06-13 18:39:36.718444
# Unit test for function dump
def test_dump():
    import shutil
    replay_dir = './tests/replay_dir'
    try:
        dump(replay_dir, './tests/fake-repo-pre/{{cookiecutter.repo_name}}',
             {
                 'cookiecutter':
                     {
                         'full_name': 'Joe Doe',
                         'email': 'joe@doe.com',
                         'project_name': 'Hello World',
                         'project_slug': 'hello-world',
                         'release_date': '2013-03-03'
                     }
             })
        shutil.rmtree(replay_dir)
    except:
        return False
    else:
        return True


# Generated at 2022-06-13 18:39:38.827869
# Unit test for function load
def test_load():
    replay_dir = "/home/peng/.cookiecutters"
    template_name = "python-package-project"
    context = load(replay_dir, template_name)

    assert(isinstance(context, dict))
    assert('cookiecutter' in context)


# Generated at 2022-06-13 18:39:46.368342
# Unit test for function load
def test_load():
    from pprint import pprint
    context = load('/home/khanh/Videos/Mastering Python for Finance/code/Chapter03', 'MasteringPythonforFinance-master')
    if isinstance(context, dict):
        print('OK')
    else:
        print('Fail')
    pprint(context)

# Generated at 2022-06-13 18:39:50.784875
# Unit test for function load
def test_load():
    replay_dir = '/tmp/'
    template_name = 'test'
    load(replay_dir, template_name)
    return 0


# Generated at 2022-06-13 18:39:53.680116
# Unit test for function load
def test_load():
    from pprint import pprint
    foo = load('./tests/foo', 'bar.json')
    print(foo)

if __name__ == '__main__':
    test_load()

# Generated at 2022-06-13 18:39:59.859262
# Unit test for function load
def test_load():
	assert load('{{cookiecutter.replay_dir}}','{{cookiecutter.project_slug}}') == {'cookiecutter': {'full_name': 'Shivani Garg', 'email': 'shivani.garg2@students.iiit.ac.in', 'project_name': 'test_proj', 'project_slug': 'test_proj', 'release_date': '2018-08-05', 'version': '0.1.0', 'use_pytest': False, 'use_pypi_deployment_with_travis': False, 'use_docker': False, 'use_pyramid': False, 'command_line_interface': 'click', 'open_source_license': 'MIT license'}}

# Generated at 2022-06-13 18:40:09.345667
# Unit test for function dump
def test_dump():
    """Test function dump in file replay.py."""
    from cookiecutter import replay
    context = {"cookiecutter": {"full_name": "Audrey Roy Greenfeld",
                                "email": "audreyr@example.com",
                                "github_username": "audreyr",
                                "project_name": "Example Package",
                                "project_slug": "example_package",
                                "release_date": "2014-12-22",
                                "project_short_description": "Example Package is a package",
                                "pypi_username": "pypi-username",
                                "version": "0.1",
                                "open_source_license": "MIT license"}}
    replay.dump(context, 'tests/test-repo-pre/', 'example-pkg')

# Generated at 2022-06-13 18:40:18.935385
# Unit test for function load
def test_load():
    replay_dir = "/home/wg/Documents/repo/cookiecutter-datascience"
    template_name = "cookiecutter-datascience/%cookiecutter.repo_name%"
    context = load(replay_dir, template_name)
    print(context)
    #{'cookiecutter': {'template_name': 'cookiecutter-datascience', 'full_name': 'William Greenleaf', 'email': 'wg2113@cumc.columbia.edu', 'open_source_license': 'MIT license', 'pypi_username': 'wg2113', 'use_pytest': 'y', 'use_pypi_deployment_with_travis': 'y', 'command_line_interface': 'No CLI', 'console_script': 'y'}}


# Generated at 2022-06-13 18:40:25.135736
# Unit test for function load
def test_load():
    template_name = 'my-template'
    context = {
        'cookiecutter': {
            "full_name": "First Last",
            "email": "first@example.com",
            "project_name": "My Project",
            "project_slug": "my-project",
            "project_short_description": "A short description of the project.",
            "use_pytest": "y",
            "use_pypi_deployment_with_travis": "y",
            "command_line_interface": "click",
            "open_source_license": "MIT license"
        }
    }
    replay_dir = os.path.expanduser('~/.cookiecutter_replay')


# Generated at 2022-06-13 18:40:36.683243
# Unit test for function dump
def test_dump():
    """test."""
    if not make_sure_path_exists('test'):
        raise IOError('Unable to create replay dir at {}'.format('test'))

    replay_file = get_file_name('test', 'test')

    context_test = {
        'project_name': 'test',
        'cookiecutter': {}
    }

    if not isinstance(context_test, dict):
        raise TypeError('Context is required to be of type dict')

    if 'cookiecutter' not in context_test:
        raise ValueError('Context is required to contain a cookiecutter key')

    with open(replay_file, 'w') as outfile:
        json.dump(context_test, outfile, indent=2)


if __name__ == '__main__':
    test_dump()

# Generated at 2022-06-13 18:40:43.059202
# Unit test for function load
def test_load():
    # Test if the function load is working
    # create a data file
    replay_dir = 'tests/test-load/'
    dump(replay_dir, 'test_load', {'cookiecutter':{'cookiecutter':'test_load'}})
    # test if the data load correctly
    context = load(replay_dir, 'test_load')
    assert context['cookiecutter']['cookiecutter'] == 'test_load'

# Generated at 2022-06-13 18:40:52.801402
# Unit test for function load
def test_load():
    context=load('C:\\Users\\kaipc\\PycharmProjects\\My-Cookiecutter\\tests\\fixtures\\test-replay', 'test_template')
    #print(context)
    a=repr(context)
    print(a)


test_load()

# Generated at 2022-06-13 18:41:03.403285
# Unit test for function dump
def test_dump():
    import tempfile
    import shutil
    template_dir = 'tests'

# Generated at 2022-06-13 18:41:10.485633
# Unit test for function load
def test_load():
    """Test replay.load when replay file exists."""
    import tempfile

    with tempfile.TemporaryDirectory() as tmp_dir:
        replay_dir = os.path.join(tmp_dir, 'replay')
        os.makedirs(replay_dir)

        template_name = 'old-and-unused'
        replay_file = get_file_name(replay_dir, template_name)

        with open(replay_file, 'w') as outfile:
            json.dump({'hello': 'world'}, outfile, indent=2)

        context = load(replay_dir, template_name)

        assert context['hello'] == 'world'


# Generated at 2022-06-13 18:41:14.955358
# Unit test for function load
def test_load():
    template_name = 'test_load'
    replay_dir = os.path.join(os.path.dirname(__file__), 'replay_dir')
    context = {
        'cookiecutter': {
            '_template': template_name,
            'author_email': 'test@example.com',
            'author_name': 'test',
            'description': 'test',
            'full_name': 'test',
            'open_source_license': 'MIT',
            'pypi_username': 'test',
            'repo_name': 'test',
            'year': '2016'
        }
    }

    # Loading from an empty directory should raise an Error

# Generated at 2022-06-13 18:41:21.634437
# Unit test for function dump
def test_dump():
    import shutil

    context = {
                'cookiecutter': {
                    'project_name': 'fizzbuzz',
                    'project_slug': 'fizzbuzz'
                }
              }

    template_name = 'my_template'
    replay_dir = 'my_replay_dir'

    try:
        shutil.rmtree(replay_dir)
        dump(replay_dir, template_name, context)
    finally:
        shutil.rmtree(replay_dir)



# Generated at 2022-06-13 18:41:27.193527
# Unit test for function load
def test_load():
    replay_file = get_file_name('test/test_replay/', 'testing_get_file_name')
    assert os.path.isfile(replay_file)
    foo = load('test/test_replay', 'testing_get_file_name')
    assert foo == {'cookiecutter': {'first_name': 'Audrey', 'last_name': 'Roy'}}


# Generated at 2022-06-13 18:41:31.681788
# Unit test for function load
def test_load():
    """
    Test load function
    """
    template_name = os.path.join(os.path.dirname(__file__), 'test')
    replay_dir = os.path.join(os.path.dirname(__file__), 'test')

    assert isinstance(load(replay_dir, template_name), dict)



# Generated at 2022-06-13 18:41:36.106827
# Unit test for function dump
def test_dump():
    replay_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'test_replay'))
    template_name = 'test'
    context = {'cookiecutter': {'full_name': 'Audrey Roy Greenfeld'}}
    #dump(replay_dir, template_name, context)



# Generated at 2022-06-13 18:41:41.065315
# Unit test for function dump
def test_dump():
    replay_dir = os.path.join(os.path.dirname(__file__), 'test_replay')
    template_name = 'test_template'
    context = {'cookiecutter': 'key'}
    dump(replay_dir, template_name, context)
    assert load(replay_dir, template_name) == context

    # Clean up
    file_name = get_file_name(replay_dir, template_name)
    os.remove(file_name)

# Generated at 2022-06-13 18:41:43.351859
# Unit test for function load
def test_load():
    result = False
    try:
        load('/tmp/', 'fake_template')
    except:
        result = True
    assert result


# Generated at 2022-06-13 18:41:50.195248
# Unit test for function load
def test_load():
    #test in which context is empty
    context = {}
    template_name = 'test_template'
    replay_dir = 'tmp'
    dump(replay_dir, template_name, context)
    context_test = load(replay_dir, template_name)
    assert context == context_test

    #test in which context contains cookiecutter key
    context = {'cookiecutter': 'test'}
    template_name = 'test_template'
    replay_dir = 'tmp'
    dump(replay_dir, template_name, context)
    context_test = load(replay_dir, template_name)
    assert context == context_test

    #test in which context does not contain cookiecutter key
    context = {'cookie': 'test'}
    template_name = 'test_template'
    replay

# Generated at 2022-06-13 18:41:52.885238
# Unit test for function load
def test_load():
    context = load('../templates','/cookiecutter-pypackage/')
    assert context['cookiecutter']['Python_package'] == 'Python_package'

# Generated at 2022-06-13 18:41:56.025400
# Unit test for function dump
def test_dump():
    dump('', '', {})


# Generated at 2022-06-13 18:42:02.334799
# Unit test for function dump
def test_dump():
    template_name = 'test_template'
    replay_dir = 'tests/test-data/replay'
    context = {
        'cookiecutter': {
            '_template': 'test_template'
        },
        'project_name': 'foo',
        'github_username': 'bar'
    }

    dump(replay_dir, template_name, context)



# Generated at 2022-06-13 18:42:08.904707
# Unit test for function load
def test_load():
    context = load('./tests/files/hello-world', 'hello-world')
    assert context == {
        '_template': './tests/files/hello-world',
        'cookiecutter': {
            'audience': 'World',
            'full_name': 'Audrey Roy Greenfeld',
            'name': 'Audrey',
            'project_name': 'Cookie Cutter',
            'project_slug': 'cookie-cutter',
            'release_date': '2014-10-15',
            'year': '2014',
        }
    }

# Generated at 2022-06-13 18:42:17.138360
# Unit test for function dump
def test_dump():
    # Test 1: correct file name and context input
    replay_dir = 'test_replay_dir'
    template_name = 'test_template'
    context = { "cookiecutter": { "project_name": "test_template_project" } }
    dump(replay_dir, template_name, context)

    # Test 2: dir name is invalid
    replay_dir = '$$'
    template_name = 'test_template'
    context = { "cookiecutter": { "project_name": "test_template_project" } }

# Generated at 2022-06-13 18:42:21.413406
# Unit test for function dump
def test_dump():
    replay_dir = 'tests/test-replay/'
    make_sure_path_exists(replay_dir)

    template_name = 'test-replay-template'
    context = {
        "cookiecutter": {
            "full_name": "Test User",
            "email": "testuser@example.com",
        }
    }
    dump(replay_dir, template_name, context)

    # Check if file exists
    replay_file = get_file_name(replay_dir, template_name)
    assert(os.path.isfile(replay_file))


# Generated at 2022-06-13 18:42:28.286448
# Unit test for function load
def test_load():
    """Test replay.load."""
    from cookiecutter.main import cookiecutter  # pylint: disable=I0011,W0611
    # Create a fake template
    template_folder, context = cookiecutter('.', no_input=True, replay=False)

    replay_file = get_file_name(template_folder, '_cookiecutter')

    with open(replay_file, 'w') as outfile:
        json.dump(context, outfile, indent=2)

    replay_context = load(template_folder, '_cookiecutter')

    assert replay_context == context

# Generated at 2022-06-13 18:42:30.439701
# Unit test for function load
def test_load():
    replay_dir = '../tests/test-replay'
    template_name = 'test'
    print(load(replay_dir, template_name))


# Generated at 2022-06-13 18:42:31.473074
# Unit test for function load
def test_load():
    assert load("/", "cookie") == {"cookiecutter": "Hello"}



# Generated at 2022-06-13 18:42:38.927519
# Unit test for function load
def test_load():
    template_name = "test_load_delete"
    context_1 = {'cookiecutter': {'full_name': "test_load_delete"}}
    context_2 = {'cookiecutter': {'full_name': "test_load_delete", 'project_name': "test_load_delete"}}
    try:
        load(replay_dir = ".", template_name = template_name)
    except ValueError:
        pass
    dump(replay_dir = ".", template_name = template_name, context = context_1)
    dump(replay_dir = ".", template_name = template_name, context = context_2)
    assert(load(replay_dir = ".", template_name = template_name) == context_2)


# Generated at 2022-06-13 18:42:43.043063
# Unit test for function load
def test_load():
    """Test load."""
    replay_dir = "tests/test-repo"
    template_name = "pypackage"
    replay_file = get_file_name(replay_dir, template_name)
    context = load(replay_dir, template_name)
    assert context["project_name"] == "My Project"
# End of unit test for function load


# Generated at 2022-06-13 18:42:56.048123
# Unit test for function load
def test_load():
    context = load('./', 'template-test')
    if context == None:
        print("Context from json file is null")
        assert False
    else:
        if not isinstance(context, dict):
            print("Context is not a dictionary")
            assert False
        elif 'cookiecutter' not in context:
            print("Context does not contain cookiecutter key")
            assert False
        else:
            return True
if __name__ == "__main__":
    test_load()

# Generated at 2022-06-13 18:43:06.632959
# Unit test for function dump
def test_dump():
    import tempfile
    import shutil
    import os

    replay_dir = os.path.join(tempfile.gettempdir(), "test_replay_dir")
    if os.path.exists(replay_dir):
        shutil.rmtree(replay_dir)

    template_name = "fixtures/cookiecutter-pypackage"
    context = {'cookiecutter': {"project_slug": "test_project", "full_name": "Test name"}}
    dump(replay_dir, template_name, context)

    # Test if the file was created
    filename = os.path.join(replay_dir, "fixtures-cookiecutter-pypackage.json")
    assert os.path.isfile(filename)

    # Test if the context was written correctly.

# Generated at 2022-06-13 18:43:11.951306
# Unit test for function load
def test_load():
    # create a dict
    dict_obj = dict()
    dict_obj["key_1"] = "value_1"
    dict_obj["key_2"] = "value_2"
    # write the dict to a json file
    replay_file_obj = open("tmp.json", "w")
    json.dump(dict_obj, replay_file_obj, indent=2)
    replay_file_obj.close()
    # load the json file and check its content
    loaded_dict = load("", "tmp.json")
    assert len(dict_obj) == len(loaded_dict)
    for key in dict_obj.keys():
        assert dict_obj[key] == loaded_dict[key]
    # remove the json file
    os.remove("tmp.json")

# Generated at 2022-06-13 18:43:15.674224
# Unit test for function load
def test_load():
    template_name = 'cookiecutter-pypackage-minimal'
    replay_dir = r'C:\Users\yanlh\.cookiecutters'
    context = load(replay_dir, template_name)
    print(context)



# Generated at 2022-06-13 18:43:20.095302
# Unit test for function load
def test_load():
    replay_dir = 'C:/Users/zhan9/PycharmProjects/galileo/cookiecutter/tests/replay'
    template_name = 'gh:audreyr/cookiecutter-pypackage'
    context = load(replay_dir, template_name)
    assert "cookiecutter" in context


# Generated at 2022-06-13 18:43:27.378991
# Unit test for function dump
def test_dump():
    """Unit test for function dump."""
    import tempfile
    import shutil
    import json

    template_name = 'test'
    context = {'test':'test2'}

    replay_dir = tempfile.mkdtemp()
    dump(replay_dir, template_name, context)

    with open(replay_dir + '/test.json', 'r') as infile:
        context_from_file = json.load(infile)

    assert context == context_from_file
    shutil.rmtree(replay_dir)


# Generated at 2022-06-13 18:43:37.498755
# Unit test for function dump
def test_dump():
    """Unit test for function dump."""
    replay_dir = 'C:\\Users\\Injinie\\Documents\\Cookiecutter-temp\\cookiecutter-pypackage-jin\\cookiecutter-pypackage\\{{cookiecutter.project_slug}}\\replay'
    template_name = 'cookiecutter-pypackage-jin'

    context = dict()
    context['cookiecutter'] = dict()
    context['cookiecutter']['project_name'] = 'My amazing project'

    dump(replay_dir, template_name, context)

if __name__ == '__main__':
    test_dump()

# Generated at 2022-06-13 18:43:40.105718
# Unit test for function dump
def test_dump():
    dump('tests/', 'hello', {'cookiecutter': {'hello': 'world', 'bingo': 'bar'}})


# Generated at 2022-06-13 18:43:44.864400
# Unit test for function load

# Generated at 2022-06-13 18:43:49.814108
# Unit test for function load
def test_load():
    """Unit test for function load."""
    import random
    import string
    import shutil

    replay_dir = 'aaa'
    template_name = ''.join(random.choice(string.ascii_uppercase) for _ in range(10))
    context = {
        'cookiecutter': {
            'full_name': 'bbb',
            'email': 'ccc',
            'github_username': 'ddd'
        }
    }
    dump(replay_dir, template_name, context)

    replay_context = load(replay_dir, template_name)
    assert replay_context == context

    shutil.rmtree(replay_dir)



# Generated at 2022-06-13 18:44:05.233715
# Unit test for function load
def test_load():
    import os

    replay_dir = os.path.join(os.getcwd(), "tests", "replay")
    template_name = "cookiecutter-pypackage"

    # Test file exists and loads
    assert load(replay_dir, template_name)

    # Test file does not exist
    template_name = "cookiecutter-foobar"
    assert load(replay_dir, template_name) is None

# Generated at 2022-06-13 18:44:07.719898
# Unit test for function dump
def test_dump():
    context = {'cookiecutter': {'project_name': 'Hello', 'project_slug': 'hello'}}
    dump('.', 'test', context)



# Generated at 2022-06-13 18:44:09.019506
# Unit test for function load
def test_load():
    assert load('../', 'test') == 'test'



# Generated at 2022-06-13 18:44:13.845341
# Unit test for function load
def test_load():
    """Unit test for function load."""
    print('Unit test for function load')
    if not(os.path.isfile('cookiecutter.json')):
        print('No cookiecutter.json, skip the test')
    else:
        save_file = 'cookiecutter.json'
        context = load(os.getcwd(), save_file)
        print('Loaded file: {}'.format(save_file))
        print('Context: {}'.format(context))


# Generated at 2022-06-13 18:44:19.825514
# Unit test for function dump
def test_dump():
    """Unit test for function dump."""
    template_name = 'tests/fake-repo-pre/'
    replay_dir = './cookiecutter'
    context = {
        'cookiecutter': {
            'full_name': 'Brian Okken',
            'email': 'brian@pythontesting.net',
            'project_name': 'python-hello-world-20170611-2042',
            'project_slug': 'python-hello-world',
            'project_short_description': 'A short description of the project.',
            'release_date': '20170611',
            'year': '2017',
            'pypi_username': 'okken',
            'open_source_license': 'MIT license'
        }
    }

# Generated at 2022-06-13 18:44:29.474153
# Unit test for function load
def test_load():
    """Test for function load."""
    import json
    import os
    import pytest
    from cookiecutter import replay
    from cookiecutter.utils import make_sure_path_exists

    # Make sure replay dir can be created if it doesn't already exists.
    replay_dir = os.path.join(os.getcwd(), 'tests/files/abc')
    make_sure_path_exists(replay_dir)

    # Populate replay_dir
    file_name = os.path.join(os.getcwd(), 'tests/files/abc/test.json')
    example_context = {"cookiecutter": {"full_name": "Audrey Roy", "email": "audreyr@example.com"}}

# Generated at 2022-06-13 18:44:31.761704
# Unit test for function load
def test_load():
    context = load('cookiecutter', 'cookiecutter.json')
    print(context)
    # context is a dict
    assert context.get('cookiecutter') is not None



# Generated at 2022-06-13 18:44:36.788294
# Unit test for function load
def test_load():
    replay_dir = "~/replay_dir/"
    template_name = "pypackage"
    context = {}
    
    assert load(replay_dir, template_name) == context
    assert load(replay_dir, template_name = "") == None
    assert load("~/aaaaaaaaa/", template_name) == None


# Generated at 2022-06-13 18:44:40.677319
# Unit test for function load
def test_load():
    """Test load function."""
    context = load(
        'C:\\Users\\sgavr\\PycharmProjects\\cookiecutter\\tests\\replay',
        'cookiecutter'
    )
    if context:
        print(context)
        print(context['cookiecutter'])
    assert context


# Generated at 2022-06-13 18:44:44.002514
# Unit test for function load
def test_load():
    context = load('/Users/brandon.graham/code/cookiecutter-twoscoops', 'cookiecutter-twoscoops')
    print(context)

# Generated at 2022-06-13 18:45:09.568485
# Unit test for function load
def test_load():
    replay_dir = os.path.join(os.getcwd(), 'tests/fixtures/replay-dir')
    template_name = 'cookiecutter-pypackage'
    context = load(replay_dir, template_name)
    assert 'project_name' in context['cookiecutter']


# Generated at 2022-06-13 18:45:12.851030
# Unit test for function load
def test_load():
    """Unit tests for replay load."""
    replay_dir = 'replays/test'
    template_name = 'pypackage'
    context = load(replay_dir, template_name)
    assert context['cookiecutter']['author_name'] == 'xyz'

# Generated at 2022-06-13 18:45:17.115274
# Unit test for function load
def test_load():
    with open('testreplay.json', 'r') as infile:
        context = json.load(infile)
    assert context["cookiecutter"]["project_name"] == "sluggo"


# Generated at 2022-06-13 18:45:20.531674
# Unit test for function load
def test_load():
    template_name="airbnb"
    replay_dir="C:\\Users\\sunfei\\Desktop\\cookiecutter"
    context=load(replay_dir,template_name)
    assert isinstance(context,dict)
    assert 'cookiecutter' in context

# Generated at 2022-06-13 18:45:24.972411
# Unit test for function load
def test_load():
    replay_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../tests/test-replay'))
    template_name = 'simple'
    context = load(replay_dir, template_name)
    assert isinstance(context,dict)
    assert 'cookiecutter' in context.keys()


# Generated at 2022-06-13 18:45:29.070313
# Unit test for function load
def test_load():
    """Function load test."""
    context = load('replay', 'python-package')
    assert 'cookiecutter' in context
    assert 'full_name' in context['cookiecutter']
    assert 'email' in context['cookiecutter']
    assert 'project_name' in context['cookiecutter']

# Generated at 2022-06-13 18:45:32.437876
# Unit test for function dump
def test_dump():
    template_name = 'my_template'
    context ={'cookiecutter':{'key':'value'}}
    replay_dir = 'replay_dir'
    dump(replay_dir, template_name, context)


# Generated at 2022-06-13 18:45:35.181107
# Unit test for function load
def test_load():
    context = load('../replay', 'cookiecutter-pypackage')
    assert isinstance(context, dict)
    assert context['cookiecutter']['replay_dir'] == '../replay'


# Generated at 2022-06-13 18:45:40.595582
# Unit test for function load
def test_load():
    """
    Unit test for function load.
    """
    return load(r"C:\Users\Administrator\PycharmProjects\cookiecutter-setup-py\aravind\cookiecutter-setup-py\tests\data\cc_replay", "data")

# Generated at 2022-06-13 18:45:44.277657
# Unit test for function load
def test_load():
    file_name = r'/home/shuai/lab/test_replay.json'
    replay = load(file_name, '')
    print(replay)

test_load()

# Generated at 2022-06-13 18:46:36.505007
# Unit test for function load
def test_load():
    """Test load json data from file."""
    os.environ['REPLAY_DIR'] = 'tests/test-load-replay'
    if not make_sure_path_exists('tests/test-load-replay'):
        raise IOError('Unable to create replay dir at tests/test-load-replay')
    replay_file = get_file_name('tests/test-load-replay', 'test_template')
    f = open(replay_file, 'w')
    context = dict()
    context['cookiecutter'] = dict()
    json.dump(context, f, indent=2)
    f.close()
    context = load('tests/test-load-replay', 'test_template')
    assert context['cookiecutter'] == dict()
    os.remove(replay_file)


# Generated at 2022-06-13 18:46:43.371963
# Unit test for function dump
def test_dump():
    from tempfile import mkdtemp
    test_replay_dir = mkdtemp()

# Generated at 2022-06-13 18:46:47.370858
# Unit test for function load
def test_load():

    #Test normal input
    test1 = load('replay/', 'template_name')
    assert type(test1) is dict
    #assert type(test1.get('cookiecutter')) is dict

    #Test no replay_dir
    #test2 = load('replay')
    #assert type(test2) is IOError

    #Test no template_name
    #test3 = load('replay/')
    #assert type(test3) is TypeError


# Generated at 2022-06-13 18:46:52.811204
# Unit test for function load
def test_load():
    replay_dir = 'tests/test-data/replay'
    template_name = 'json_test'

    try:
        context = load(replay_dir, template_name)
    except ValueError:
        assert True

    template_name = 'example'

    try:
        context = load(replay_dir, template_name)
    except ValueError:
        assert False

    return True

# Generated at 2022-06-13 18:46:58.132679
# Unit test for function load
def test_load():
    template_name = 'my_template'
    replay_dir = 'replay'
    context = {'cookiecutter': {'full_name': 'Codio', 'email': 'support@codio.com', 'github_username': 'CodioHQ'}}
    dump(replay_dir, template_name, context)

    context_loaded = load(replay_dir, template_name)

    assert context_loaded['cookiecutter'] == context['cookiecutter']

# Generated at 2022-06-13 18:47:05.123932
# Unit test for function load
def test_load():
    replay_dir = '/Users/sarahsundari/Desktop/cookiecutter/tests/test-generate/cookiecutter-pypackage-minimal'
    template_name = '{{cookiecutter.project_slug}}'
    context = load(replay_dir, template_name)

    print(context)
    print(replay_file)
    assert load(replay_dir, template_name)['author_name'] == 'Sarah Sundari'


# Generated at 2022-06-13 18:47:09.674882
# Unit test for function dump
def test_dump():
    """Test function dump."""
    replay_dir = '/tmp/cookiecutter-replay'
    context = {'cookiecutter': {}}
    dump(replay_dir, 'test_template', context)
    assert os.path.isfile(get_file_name(replay_dir, 'test_template'))



# Generated at 2022-06-13 18:47:14.076000
# Unit test for function dump
def test_dump():
    context = {'cookiecutter': {'full_name': 'Arthur Dent'}}
    template_name = 'planetexpress'
    replay_dir = '~/.cookiecutter_replay'
    dump(replay_dir, template_name, context)
    assert("Cookies" in os.listdir("."))
    assert("planetexpress.json" in os.listdir("Cookies"))


# Generated at 2022-06-13 18:47:20.336683
# Unit test for function load
def test_load():
    file_name = './test.json'

    if os.path.exists(file_name):
        os.remove(file_name)

    with open(file_name, 'w') as outfile:
        json.dump({'int': 1, 'string': '2'}, outfile)

    obj = load('', file_name)
    assert obj['int'] == 1
    assert obj['string'] == '2'



# Generated at 2022-06-13 18:47:24.777018
# Unit test for function load
def test_load():
    """Unit test for function load."""
    reload(replay)

    # Replace outfile.write with a mock function
    replay.make_sure_path_exists = MagicMock(return_value=True)
    replay.open = MagicMock()

    replay.load('', '')
    replay.open.assert_called_once_with('')

    # Restore function since we're testing other functions that call this one
    reload(replay)