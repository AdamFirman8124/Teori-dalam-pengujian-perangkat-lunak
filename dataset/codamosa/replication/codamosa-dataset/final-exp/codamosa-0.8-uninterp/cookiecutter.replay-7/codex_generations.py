

# Generated at 2022-06-13 18:38:25.196491
# Unit test for function load
def test_load():
    context = load('/Users/mahmoud/replay','mahmoud-shawqi')
    assert 'cookiecutter' in context
    

# Generated at 2022-06-13 18:38:26.570006
# Unit test for function load

# Generated at 2022-06-13 18:38:32.301256
# Unit test for function load
def test_load():

    # Create replay file for unit test
    replay_dir = 'test_dir'
    template_name = 'test_template'
    context = {
        'cookiecutter': {
            'project_name': 'test_name',
            'author_name': 'test_author'
        }
    }
    dump(replay_dir, template_name, context)

    context_load = load(replay_dir, template_name)

    assert context == context_load


if __name__ == '__main__':
    test_load()

# Generated at 2022-06-13 18:38:35.081907
# Unit test for function load
def test_load():
    replay_dir = os.path.join('tests', 'test-replay')
    template_name = 'cookiecutter-pypackage-minimal'
    context = load(replay_dir, template_name)
    assert isinstance(context, dict)
    assert 'cookiecutter' in context


# Generated at 2022-06-13 18:38:39.885311
# Unit test for function dump
def test_dump():
    test_context = {'cookiecutter': {'test': True}}
    dump('test', 'dump_test', test_context)

    with open(get_file_name('test', 'dump_test')) as data_file:
        data = json.load(data_file)

    print(data)
    assert data == test_context


# Generated at 2022-06-13 18:38:49.266281
# Unit test for function load
def test_load():
    replay_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))),
        'tests', 'test-generate-files-replay', 'replay'
    )
    tmp_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))),
        'tests', 'test-generate-files-replay')

    os.chdir(tmp_dir)
    context = load(replay_dir, 'cookiecutter-pypackage')
    assert context['_template'] == 'https://github.com/audreyr/cookiecutter-pypackage.git'
    assert context

# Generated at 2022-06-13 18:39:01.992922
# Unit test for function dump
def test_dump():
    """Unit test for function dump"""
    # test for case replay_dir not exist
    replay_dir = 'test_dump'
    template_name = 'test_dump'
    context = {'cookiecutter': {'_template': 'test_dump'}}
    try:
        dump(replay_dir, template_name, context)
        assert False
    except IOError:
        assert True

    # test for case template_name not string
    replay_dir = 'tests/test-replay/dump'
    template_name = 1
    context = {'cookiecutter': {'_template': 'test_dump'}}
    try:
        dump(replay_dir, template_name, context)
        assert False
    except TypeError:
        assert True

    # test for case context not dict

# Generated at 2022-06-13 18:39:06.508432
# Unit test for function get_file_name
def test_get_file_name():
    file_name = get_file_name("./", "bar")
    assert(file_name == "./bar.json")
    file_name = get_file_name("./", "bar.json")
    assert(file_name == "./bar.json")
    file_name = get_file_name("./", "foo/bar.json")
    assert(file_name == "./foo/bar.json")


# Generated at 2022-06-13 18:39:11.417149
# Unit test for function get_file_name
def test_get_file_name():
    """Unit test for function get_file_name."""

    template_name = 'cookiecutter-pypackage'
    replay_dir = '/Users/wjia/.cookiecutters'

    assert os.path.join(replay_dir, template_name) == get_file_name(replay_dir, template_name)
    assert os.path.join(replay_dir, template_name + '.json') == get_file_name(replay_dir, template_name + '.json')

# Generated at 2022-06-13 18:39:16.132265
# Unit test for function dump
def test_dump():
    # Test template name not of type string
    try:
        dump('/tmp', 2, {})
        assert False
    except TypeError:
        pass

    # Test context not of type dict
    try:
        dump('/tmp', 'test', 2)
        assert False
    except TypeError:
        pass

    # Test context does not contain a cookiecutter key
    try:
        dump('/tmp', 'test', {})
        assert False
    except ValueError:
        pass

    # Test successful dump
    context = {'cookiecutter': {}},
    dump('/tmp/test', 'test', context)

    # Test unsuccessful dump
    try:
        dump('/test', 'test', context)
        assert False
    except IOError:
        pass


# Generated at 2022-06-13 18:39:20.423188
# Unit test for function load
def test_load():
    context = load('./tests/test.json')
    assert context == {'cookiecutter': {'repo_dir': '/home/silas/Documents/projects/project-name'}}

# Generated at 2022-06-13 18:39:24.980739
# Unit test for function dump
def test_dump():
    path = "./tests/replay/"
    template_name = "cookiecutter-pypackage"
    dict = {'cookiecutter':
        {'full_name': 'Hengler',
         'email': 'zhanghengler@gmail.com'}
    }
    dump(path, template_name, dict)


# Generated at 2022-06-13 18:39:32.155676
# Unit test for function dump
def test_dump():
    import shutil
    replay_dir = 'test-replay'
    shutil.rmtree(replay_dir, ignore_errors=True)
    make_sure_path_exists(replay_dir)

    template_name = 'test-template'
    answer_file = '%s.json' % template_name

# Generated at 2022-06-13 18:39:36.333220
# Unit test for function load
def test_load():
    replay_dir = 'replay'
    template_name = 'python-module'
    context = load(replay_dir, template_name)
    print(context)


if __name__ == '__main__':
    test_load()

# Generated at 2022-06-13 18:39:40.347210
# Unit test for function load
def test_load():
    """Unit test for function load."""
    context = load('./tests/fake-repo-pre/', 'fake-repo-pre')
    assert "cookiecutter" in context
    assert context["project_name"] == "Cookiecutter Template for Python"
    assert context["domain_name"] == "example.com"
    assert context["email"] == "pydanny@example.com"

# Generated at 2022-06-13 18:39:55.435634
# Unit test for function dump
def test_dump():
    assert os.path.isfile('/home/travis/build/audreyr/cookiecutter-pypackage/tests/fake-repo-pre/{{cookiecutter.repo_name}}.json') == True
    assert os.path.isfile('/home/travis/build/audreyr/cookiecutter-pypackage/tests/fake-repo-pre/cookiecutter.json') == True
    #should fail
    try:
        os.path.isfile('/home/travis/build/audreyr/cookiecutter-pypackage/tests/fake-repo-pre/{{cookiecutter.repo_name}}') == True
    except ValueError:
        print("ValueError: Context is required to contain a cookiecutter key")

# Generated at 2022-06-13 18:39:57.310684
# Unit test for function load
def test_load():
    context = load('./replay', 'gh:liming-wang/cookiecutter-python-script')
    assert context['cookiecutter']['project_name'] == 'My Project'

# Generated at 2022-06-13 18:39:59.882671
# Unit test for function load
def test_load():
    load("./mytest/testreplay", "mytest")


# Generated at 2022-06-13 18:40:06.332092
# Unit test for function dump
def test_dump():
    replay_dir = 'TEST'
    context = {'cookiecutter': {'testkey1': 'testvalue1'}}
    template_name = 'TEST'
    dump(replay_dir, template_name, context)

    with open('TEST.json', 'r') as replay_file:
        read_context = json.load(replay_file)
    assert context == read_context
    os.remove('TEST.json')


# Generated at 2022-06-13 18:40:12.204509
# Unit test for function load
def test_load():
    replay_dir = os.getcwd()
    template_name = "template_name"
    context = {"cookiecutter": {"version": "1.1"}}
    test_file = get_file_name(replay_dir, template_name)
    try:
        with open(test_file, 'w') as outfile:
            json.dump(context, outfile, indent=2)

        context = load(replay_dir, template_name)
        if not isinstance(context, dict):
            raise TypeError('Context is required to be of type dict')
        if 'cookiecutter' not in context:
            raise ValueError('Context is required to contain a cookiecutter key')
    finally:
        os.remove(test_file)

# Generated at 2022-06-13 18:40:20.862935
# Unit test for function dump
def test_dump():
    replay_dir = 'tests/test-replay'
    template_name = 'mytemplate'
    context = {'cookiecutter': {'username': 'myuser'}}

    dump(replay_dir, template_name, context)

    replay_file = get_file_name(replay_dir, template_name)
    with open(replay_file, 'r') as infile:
        content = infile.read()

    assert content == '{\n  "cookiecutter": {\n    "username": "myuser"\n  }\n}'



# Generated at 2022-06-13 18:40:27.121749
# Unit test for function dump
def test_dump():
    # Test the case that param context is not a dictionary
    replay_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    template_name = 'test_template'

    try:
        dump(replay_dir, template_name, 'a')
    except TypeError as e:
        if 'dict' in e.args[0]:
            pass
        else:
            assert False

    # Test the case that 'cookiecutter' key is not in param context
    context = {
                'project_slug': 'cookiecutter_test',
                'replay_dir': replay_dir,
                'replay': 'True'
              }
    

# Generated at 2022-06-13 18:40:33.768330
# Unit test for function load
def test_load():
    #prepare a file to read
    with open(get_file_name('replay', 'test.json'), 'w') as outfile:
        json.dump({'cookiecutter': {}}, outfile, indent=2)
    try:
        load('replay', 'test.json')
    except ValueError:
        assert False
    os.remove('replay/test.json')


# Generated at 2022-06-13 18:40:42.300906
# Unit test for function dump
def test_dump():
    """Test function dump."""
    from cookiecutter.main import cookiecutter
    from tempfile import mkdtemp

    top_level_dir = mkdtemp()
    cookiecutter(
        'https://github.com/audreyr/cookiecutter-pypackage.git',
        replay_dir=top_level_dir,
        checkout='0.4.2',
        no_input=True)
    replay_file = os.path.join(top_level_dir, 'cookiecutter-pypackage.json')
    assert os.path.isfile(replay_file)

    with open(replay_file, 'r') as infile:
        context = json.load(infile)

    assert context['cookiecutter']['full_name'] == 'Audrey Roy Greenfeld'

   

# Generated at 2022-06-13 18:40:49.486913
# Unit test for function load
def test_load():
    template_name = "ansible_role_test"
    replay_file = get_file_name(replay_dir, template_name)
    context = load(replay_dir, template_name)
    assert 'cookiecutter' in context

if __name__ == '__main__':
    replay_dir = '~/replay'
    template_name = "ansible_role_test"

# Generated at 2022-06-13 18:40:50.771818
# Unit test for function load
def test_load():
    context = load('../tests', 'basic')
    print(context)


# Generated at 2022-06-13 18:40:58.918065
# Unit test for function dump
def test_dump():
    replay_dir = 'tests/test-output'
    template_name = 'test_template'
    context = {'cookiecutter': {'full_name': 'Dump Test',
                                'email': 'dump-test@cookiecutter.io',
                                'github_username': 'cookiecutter-test',
                                'project_name': 'Dump Test',
                                'project_slug': 'dump_test',
                                'repo_name': 'Dump Test'}}
    dump(replay_dir, template_name, context)
    replay_file = get_file_name(replay_dir, template_name)
    assert os.path.exists(replay_file)
    os.remove(replay_file)


# Generated at 2022-06-13 18:41:01.642977
# Unit test for function load
def test_load():
    replay_dir = 'tests/files/replay'
    template_name = 'tests/files/replay/cookiecutter-pypackage-min'
    assert(load(replay_dir, template_name))


# Generated at 2022-06-13 18:41:07.044531
# Unit test for function dump
def test_dump():
    template_name = 'test_replay'
    replay_dir = 'templates'
    context = {'cookiecutter': {'name': 'test-replay'}}
    dump(replay_dir, template_name, context)

    replay_file = get_file_name(replay_dir, template_name)

    with open(replay_file, 'r') as infile:
        context_read = json.load(infile)

    assert context == context_read



# Generated at 2022-06-13 18:41:12.614798
# Unit test for function load
def test_load():
    """Test load."""
    replay_dir = 'tests/test-output/replay-dir'

    # Test load with all correct parameters
    template_name = 'project_template'
    context = load(replay_dir, template_name)
    assert context['cookiecutter'] == {'full_name': 'Monty Python'}

    # Test load with invalid template_name
    template_name = 123
    try:
        load(replay_dir, template_name)
    except TypeError as e:
        assert str(e) == 'Template name is required to be of type str'
    except Exception:
        assert False

    # Test load with invalid replay_file
    template_name = 'invalid_template_name'

# Generated at 2022-06-13 18:41:21.057635
# Unit test for function load
def test_load():
    """Unit test for function load."""
    assert load(".", "test") == {
        "cookiecutter": {
            "first_name": "test_first_name",
            "last_name": "test_last_name",
            "email": "test@example.com",
            "github_username": "test_github_username",
            "project_name": "test_project_name"
        }
    }


# Generated at 2022-06-13 18:41:27.243567
# Unit test for function load
def test_load():
    context = load('tests/test-repo-pre/', 'json-file')

# Generated at 2022-06-13 18:41:29.562708
# Unit test for function load
def test_load():
    """Test function load"""
    dict_new = load('.', 'cookiecutter.json')
    print(dict_new)



# Generated at 2022-06-13 18:41:38.274721
# Unit test for function load
def test_load():
    # test.json file exists in tests/test_files/test
    context = load('tests/test_files/test', 'test')
    if context['cookiecutter'] is not None:
        pass
    else:
        raise ValueError('test.json does not contain a cookiecutter key')
    context = load('tests/test_files', 'test')
    if context['cookiecutter'] is not None:
        pass
    else:
        raise ValueError('test.json does not contain a cookiecutter key')
    context = load('tests/test_files', 'test.json')
    if context['cookiecutter'] is not None:
        pass
    else:
        raise ValueError('test.json does not contain a cookiecutter key')
    print('test_load passed')


# Generated at 2022-06-13 18:41:44.537875
# Unit test for function load
def test_load():
    replay_dir = "/home/danny/WorkSpace/personal/cookiecutter/tests/fixtures/test_replay_dir"
    template_name = "test_replay"
    test_context = load(replay_dir, template_name)

    if test_context["cookiecutter"]["name"] == "test_replay":
        print("Loaded context is right")
    else:
        print("Loaded context is wrong")


# Generated at 2022-06-13 18:41:54.736627
# Unit test for function dump
def test_dump():
    """test the dump function."""
    import os
    from contextlib import contextmanager
    from tempfile import NamedTemporaryFile, mkdtemp

    @contextmanager
    def temp_dir():
        """Create a temporary directory and delete it afterwards."""
        tempdir = mkdtemp()
        try:
            yield tempdir
        finally:
            os.rmdir(tempdir)

    @contextmanager
    def temp_named_file(suffix=''):
        """Create a temporary file and delete it afterwards."""
        with NamedTemporaryFile(delete=False, suffix=suffix) as tf:
            fname = tf.name
        yield fname
        os.remove(fname)


# Generated at 2022-06-13 18:42:00.587751
# Unit test for function dump
def test_dump():
    replay_dir = 'tests/files/test-replay'
    template_name = 'test'
  
    if not make_sure_path_exists(replay_dir):
        raise IOError('Unable to create replay dir at {}'.format(replay_dir))

    if not isinstance(template_name, str):
        raise TypeError('Template name is required to be of type str')

    # get context file for testing
    context = {'cookiecutter': {'project_name': 'Test-Project'}}

    if not isinstance(context, dict):
        raise TypeError('Context is required to be of type dict')

    if 'cookiecutter' not in context:
        raise ValueError('Context is required to contain a cookiecutter key')


# Generated at 2022-06-13 18:42:03.248066
# Unit test for function load
def test_load():
    assert load('./tests/test-load/', 'test') == {
        'cookiecutter': {
            'cookiecutter-replay': 'no',
            'project_name': 'Test'
        }
    }

# Generated at 2022-06-13 18:42:06.074836
# Unit test for function load
def test_load():
    # Test when file exist
    result = load('tests/test-replay', 'tests/test-replay/cookiecutter.json')

    # Test when file does not exist
    try:
        load('tests/test-replay', 'tests/test-replay/cookiecutter.jso')
    except:
        pass

# Generated at 2022-06-13 18:42:12.259030
# Unit test for function load
def test_load():
    """Unit test for function load."""
    context = load("../", "lion")

# Generated at 2022-06-13 18:42:17.343002
# Unit test for function load
def test_load():
    assert load('/tmp/cchistory', 'twine') == {
                    'cookiecutter': {
                        '_copy_without_render': ['CHANGES.rst', 'setup.cfg']
                        }
                    }



# Generated at 2022-06-13 18:42:27.946016
# Unit test for function load
def test_load():
    """Unit test for function load"""
    from cookiecutter import repository
    from cookiecutter import main
    from cookiecutter.config import DEFAULT_CONFIG
    from cookiecutter.config import get_config

    p = 'dummy'
    while os.path.exists(p):
        p = 'dummy' + str(random.randint(1, 1000))
    replay_dir = p

    p = 'dummy'
    while os.path.exists(p):
        p = 'dummy' + str(random.randint(1, 1000))
    output_dir = p


# Generated at 2022-06-13 18:42:32.372445
# Unit test for function dump
def test_dump():
    replay_dir = os.getcwd()
    template_name = 'test_dump'
    context = {template_name: 'test_dump'}
    dump(replay_dir, template_name, context)
    assert os.path.isfile(get_file_name(replay_dir, template_name))
    os.remove(get_file_name(replay_dir, template_name))


# Generated at 2022-06-13 18:42:36.019582
# Unit test for function load
def test_load():
    test_template_name="python-package-test"
    test_replay_dir = os.path.join(os.path.expanduser('~'), "cookiecutterspace")
    print(load(test_replay_dir, test_template_name))


# Generated at 2022-06-13 18:42:41.898292
# Unit test for function load
def test_load():
    replay_dir = os.getcwd()
    template_name = 'test-templa'
    context = {'cookiecutter': {'full_name': 'Soliciting feedback',
    'email': 'weibo.com', 'github_username': 'Soliciting feedback', 'project_name': 'Soliciting feedback',
    'repo_name': 'Soliciting feedback'
    }}
    dump(replay_dir, template_name, context)
    loaded_context = load(replay_dir, template_name)
    assert loaded_context == context


# Generated at 2022-06-13 18:42:46.538884
# Unit test for function load
def test_load():
    assert load('D:/Cookiecutters/keystone-py35/cookiecutter.json')
    assert load('D:/Cookiecutters/keystone-py35/cookiecutter.json')

# Generated at 2022-06-13 18:42:54.958031
# Unit test for function load
def test_load():
    """Unit test for function load."""
    context_file_name = 'test_context.json'
    replay_dir = 'tests/files/replay-test'
    context = load(replay_dir, context_file_name)
    assert isinstance(context, dict)
    assert context['cookiecutter']['project_slug'] == 'example'
    assert context['cookiecutter']['author_name'] == '{{cookiecutter.author_name}}'



# Generated at 2022-06-13 18:43:01.537605
# Unit test for function load
def test_load():
    context = load("C:\\Users\\prems\\OneDrive\\Documents\\CSCI-599\\Project\\cookiecutter-flask\\tests\\test_project\\", "master")
    assert(context['cookiecutter']['project_name'] == 'Test Project')
    assert(context['cookiecutter']['project_slug'] == 'test_project')
    assert(context['cookiecutter']['repo_name'] == 'test_project')
    assert(context['cookiecutter']['select_open_source_license'] == 'MIT license')
    assert(context['cookiecutter']['app_name'] == 'app')
    assert(context['cookiecutter']['author_name'] == 'Prem Subedi')

# Generated at 2022-06-13 18:43:09.915808
# Unit test for function dump
def test_dump():
    """Unit test for function dump."""
    replay_dir = os.getenv('TEST_DIR')
    template_name = 'basic'
    context = {
        'cookiecutter': {
            'full_name': 'Viktor Varvarin',
            'email': 'viktorvarvarin@gmail.com',
            'github_username': 'vvvarvarin',
            'project_name': 'example_cookiecutter_replay',
            'project_short_description': "Cookiecutter's answer to Yeoman's replay mode"
        }
    }
    dump(replay_dir, template_name, context)
    context2 = load(replay_dir, template_name)

    assert context == context2



# Generated at 2022-06-13 18:43:14.003058
# Unit test for function load
def test_load():
    data = {"cookiecutter": {"full_name": "Your name", "email": "Your email"}}
    with open('tests/test.json', 'r') as f:
        expected = json.load(f)

    results = load('tests', 'test')
    assert data == expected

# Generated at 2022-06-13 18:43:26.703616
# Unit test for function load
def test_load():
    """Test the load function."""
    replay_dir = os.path.join(
        os.getcwd(), 'cookiecutter', 'tests', 'test-load-replay'
    )
    template_name = 'test-case'
    context = load(replay_dir, template_name)
    assert type(context) == dict
    assert context['cookiecutter'] == {
        'project_name': 'Cookiecutter',
        'author_name': 'Audrey Roy Greenfeld',
        'email': 'audreyr@example.com'
    }



# Generated at 2022-06-13 18:43:29.459154
# Unit test for function load
def test_load():
    replay_file = '/Users/yangliya/PycharmProjects/cookiecutter/tests/test-replay/cc_test/wangxueli.json'
    context = load(replay_file)
    print(context)


# Generated at 2022-06-13 18:43:42.774680
# Unit test for function load
def test_load():
    file_name = 'test.json'
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    
    # NOTE: File keys must be snake_case.
    context = load(os.path.dirname(__file__), file_name) # {u'cookiecutter': {u'cookiecutter_dict': {u'key_a': u'value_a', u'nest_b': {u'key_b': u'value_b', u'key_c': u'value_c'}}}}

# Generated at 2022-06-13 18:43:44.078084
# Unit test for function load
def test_load():
    context = load('', 'setup_py')
    print(context)


# Generated at 2022-06-13 18:43:48.504043
# Unit test for function load
def test_load():
    data = {
        'cookiecutter': {
            '_copy_without_render': [],
            'replay': False,
            'no_input': False,
            'extra_context': {},
            'default_config': True,
            'context_file': 'C:\\Users\\Wyatt\\Desktop\\testing\\cookiecutter.json'
        },
    }

    test_value = load('C:\\Users\\Wyatt\\Desktop\\testing', 'cookiecutter.json')
    assert test_value == data

# Generated at 2022-06-13 18:43:54.535183
# Unit test for function dump
def test_dump():
    replay_dir = '/home/six/Documents/python/cookiecutter/cookiecutter/tests/fixtures/project_dir'
    template_name = 'bob'
    context = {'cookiecutter': {'name': 'bob', 'email': 'bob@bob.com'}}
    dump(replay_dir,template_name,context)

# Generated at 2022-06-13 18:44:01.292043
# Unit test for function load
def test_load():
    test_template_name = 'test_template'
    test_value_1 = 'test_value_1'
    test_value_2 = 'test_value_2'
    test_value_3 = 'test_value_3'
    test_context = {
        'cookiecutter': {
            'key_1': test_value_1,
            'key_2': test_value_2,
            'key_3': test_value_3
        }
    }
    test_replay_dir = 'test_replay_dir'
    if os.path.isdir(test_replay_dir):
        os.removedirs(test_replay_dir)
    assert not os.path.isdir(test_replay_dir)


# Generated at 2022-06-13 18:44:08.273300
# Unit test for function load
def test_load():
    context = load('tests/test-repo/', 'get_simple_project')
    assert context == {
        u'cookiecutter': {
            u'_copy_without_render': [
                u'.gitignore',
            ],
            u'project_name': u'get simple project',
            u'project_slug': u'get_simple_project',
            u'project_short_description': u'A short description of the project.',
            u'pypi_username': u'audreyr',
        },
    }



# Generated at 2022-06-13 18:44:11.786924
# Unit test for function load
def test_load():
    try:
        replay_dir = '/Users/jiaojing/Desktop/cookiecutter-example-template-jiaojing'
        template_name = 'example-template'
        context = load(replay_dir,template_name)
        print(context)
    except Error as err:
        print(err)


# Generated at 2022-06-13 18:44:18.394791
# Unit test for function dump
def test_dump():
    replay_file = get_file_name('tests/test_replay', 'unit_test_template')
    context = {'cookiecutter': {'github_username': 'username', 'full_name': 'full_name'}}
    dump('tests/test_replay', 'unit_test_template', context)
    assert open(replay_file).readlines()[0] == '{\n'
    assert open(replay_file).readlines()[1] == '  "cookiecutter": {\n'
    assert open(replay_file).readlines()[2] == '    "full_name": "full_name", \n'
    assert open(replay_file).readlines()[3] == '    "github_username": "username"\n'

# Generated at 2022-06-13 18:44:32.695115
# Unit test for function load
def test_load():
    # Create .cookiecutter.replay dir
    replay_dir = ".cookiecutter.replay"
    if not os.path.exists(replay_dir):
        os.mkdir(replay_dir)

    # Create test tempate
    template_name = "test_template"
    template_file_name = os.path.join(replay_dir, template_name + ".json")
    if os.path.exists(template_file_name):
        os.remove(template_file_name)

    template_context = {
        "cookiecutter": {
            "test1": {
                "test1_1": "test1_1"
            },
            "test2": {
                "test2_1": "test2_1"
            }
        }
    }

    # Create template

# Generated at 2022-06-13 18:44:37.529376
# Unit test for function load
def test_load():
    # public function unit test
    replay_dir = os.path.dirname(os.path.realpath(__file__))
    file_name = 'test_load.json'
    expected_context = {'cookiecutter':{'a':'b'}}
    context = load(replay_dir, file_name)
    assert expected_context == context

# Generated at 2022-06-13 18:44:47.176561
# Unit test for function load
def test_load():
    """ Test function load(). """
    # Test on a valid replay file
    template_name = 'example'
    replay_dir = 'tests/test-data'
    if not os.path.exists(replay_dir):
        os.mkdir(replay_dir)
    context = load(replay_dir, template_name)
    assert isinstance(context, dict)
    assert 'cookiecutter' in context

    # Test on a invalid replay file
    template_name = 'example'
    replay_dir = 'tests/test-data'
    if not os.path.exists(replay_dir):
        os.mkdir(replay_dir)
    context = load(replay_dir, template_name)
    assert isinstance(context, dict)
    assert 'cookiecutter' in context

# Unit

# Generated at 2022-06-13 18:44:48.099823
# Unit test for function load
def test_load():
    context = load('../', 'masters')
    print(context)


# Generated at 2022-06-13 18:45:03.596512
# Unit test for function dump
def test_dump():
    cookiecutter = {
        "full_name": "Your Name",
        "email": "your@email.com",
        "github_name": "YourName",
        "project_name": "Your Project Name",
        "project_short_description": "What does the project do?",
        "pypi_username": "YourPyPIUsername",
        "version": "0.1.0",
        "release_date": "2015-01-11"
    }

    context = {
        "cookiecutter": cookiecutter,
        "_template": "cookiecutter-pypackage"
    }

    template = 'cookiecutter-pypackage'
    replay_dir = '.'

    dump(replay_dir, template, context)


# Generated at 2022-06-13 18:45:07.065461
# Unit test for function load
def test_load():
    context = load('/Users/liam/Dropbox/Projects/sandbox/cookiecutter-pypackage-minimal', 'cookiecutter.json')
    assert context['cookiecutter']


# Generated at 2022-06-13 18:45:09.334955
# Unit test for function load
def test_load():
    context = load("./", "myproject")
    print(context)

if __name__ == "__main__":
    test_load()

# Generated at 2022-06-13 18:45:11.730906
# Unit test for function load
def test_load():
    file_name = 'tests/files/cookiecutter_template/template_load.json'
    context = load('', file_name)
    print(context)
    return



# Generated at 2022-06-13 18:45:22.355424
# Unit test for function dump
def test_dump():
    """Test dump function."""
    # Create the directory
    os.makedirs('tests/replay_dir')

    # Test dump with a valid template name
    dump('tests/replay_dir', 'default-repo', 
         {'cookiecutter': {'full_name': 'Audrey Roy Greenfeld'}})
    assert os.path.exists('tests/replay_dir/default-repo.json')

    # Test dump with a valid template name with suffix .json
    dump('tests/replay_dir', 'default-repo.json', 
         {'cookiecutter': {'full_name': 'Audrey Roy Greenfeld'}})
    assert os.path.exists('tests/replay_dir/default-repo.json')

    # Test dump with invalid template name

# Generated at 2022-06-13 18:45:29.417126
# Unit test for function dump
def test_dump():
    import os
    import shutil
    from cookiecutter.utils import make_sure_path_exists
    from cookiecutter.replay import dump, load
    from cookiecutter.main import cookiecutter
    
    
    replay_dir = r'../tests/replay/'
    template_name = '../tests/fake-repo-pre/'
    context = cookiecutter(template_name)
    dump(replay_dir, template_name, context)
    assert load(replay_dir, template_name) == context



# Generated at 2022-06-13 18:45:47.476332
# Unit test for function load
def test_load():
    replay_dir = 'cookiecutter-replay-tests'
    template_name = 'example-replay'
    #context = {'cookiecutter': {'hello': 'world', 'project_name': 'example-replay'}}
    context = {'cookiecutter': {'hello': 'world', 'project_name': 'example-replay'}}
    dump(replay_dir, template_name, context)
    new_context = load(replay_dir, template_name)
    assert new_context == context
    os.remove(replay_dir + '/' + template_name + '.json')
    os.rmdir(replay_dir)

if __name__ == "__main__":
    test_load()

# Generated at 2022-06-13 18:45:52.032980
# Unit test for function load
def test_load():
	load('/home/vamsi/Desktop/cookiecuter-master/cookiecutter/tests/test-replay', 'cookiecutter-jquery')
	assert type(load('/home/vamsi/Desktop/cookiecuter-master/cookiecutter/tests/test-replay', 'cookiecutter-jquery')) is dict


# Generated at 2022-06-13 18:45:59.642332
# Unit test for function dump
def test_dump():
    """Test that replay data is correctly dumped."""
    import tempfile
    import os
    import shutil
    from .main import replay
    from .exceptions import ReplayDoesNotExistException
    from cookiecutter.main import cookiecutter
    from .utils import make_sure_path_exists

    user_config_path = os.path.join(tempfile.mkdtemp(), 'cookiecutterrc')
    temp_path = os.path.join(tempfile.mkdtemp(), 'cookiecutter')

    make_sure_path_exists(user_config_path)
    make_sure_path_exists(temp_path)
    
    context = cookiecutter('tests/test-repo-tmpl', no_input=True, replay_dir=temp_path)

# Generated at 2022-06-13 18:46:05.488974
# Unit test for function load
def test_load():
    import sys, tempfile
    from .test_replay import load_data

    print("sys.version_info=", sys.version_info)
    print("sys.version=", sys.version)
    if sys.version_info < (3, 5):
        return

    template_name = 'test_template'
    replay_dir = tempfile.mkdtemp()
    dump(replay_dir, template_name, load_data())
    context = load(replay_dir, template_name)

    assert context['cookiecutter'] == load_data()['cookiecutter']

# Generated at 2022-06-13 18:46:12.217958
# Unit test for function dump
def test_dump():
    replay_dir = 'tests/test-output'
    template_name = 'replay'
    context = {
        'cookiecutter': {
            'project_name': 'TOMTOM',
            'project_slug': 'TOMTOM',
            'author_email': 'toto.toto@toto.com',
            'domain_name': 'toto.com',
            'description': 'yes',
            'version': '0.1.0',
            'open_source_license': 'MIT license',
            'year': '2017'
        }
    }
    dump(replay_dir, template_name, context)
    context_test = load(replay_dir, template_name)
    assert context_test['cookiecutter']['project_slug'] == 'TOMTOM'


# Generated at 2022-06-13 18:46:14.785945
# Unit test for function load
def test_load():
    replay_dir = './tests/test-replay'
    template_name = 'example-replay'
    context = load(replay_dir, template_name)
    print(context)


# Generated at 2022-06-13 18:46:17.759624
# Unit test for function dump
def test_dump():
    template_name = 'test'
    replay_dir = '.cookiecutter_test'
    context = {'cookiecutter': {'test': 'value'}}
    dump(replay_dir, template_name, context)
    loaded_context = load(replay_dir, template_name)
    assert context == loaded_context

# Generated at 2022-06-13 18:46:22.773609
# Unit test for function load
def test_load():
    """Test if load function can load data from file."""
    template_name = 'testing'
    replay_dir = os.path.join(os.getcwd(), 'tests', 'test_files', 'test_replay')
    context = load(replay_dir, template_name)
    cookiecutter = context.get('cookiecutter')
    full_name = cookiecutter.get('full_name')
    email = cookiecutter.get('email')
    assert full_name == 'Cookiecutter User1'
    assert email == 'cookiecutteruser1@example.com'

# Generated at 2022-06-13 18:46:27.900494
# Unit test for function load
def test_load():
    start_dir = os.getcwd()
    os.chdir('tests/fixtures/fake-repo-pre')
    context = load('fake-repo-pre/.cookiecutters', 'fake-repo-pre')
    os.chdir(start_dir)
    return context


# Generated at 2022-06-13 18:46:33.230479
# Unit test for function load
def test_load():
    replay_dir = os.path.dirname(__file__)
    template_name = "main"
    context = load(replay_dir,template_name)
    print(context)
    assert context

if __name__ == "__main__":
    test_load()

# Generated at 2022-06-13 18:46:50.270975
# Unit test for function load
def test_load():
    import pprint

    template_name = 'cookiecutter-pypackage'
    replay_dir = '{}/.cookiecutters'.format(os.path.expanduser('~'))

    context = load(replay_dir, template_name)
    pprint.pprint(context)



# Generated at 2022-06-13 18:46:59.610712
# Unit test for function dump
def test_dump():
    test_dir = 'test_dir'
    test_file = 'test_file'
    test_name = 'test_name'
    expected_file_name = os.path.join(test_dir, test_file)
    context = {
        'cookiecutter': {
            'test_name': test_name
        }
    }
    # check if file name is correct
    assert(get_file_name(test_dir, test_file) == os.path.join(test_dir, test_file))
    # check if file is not created
    assert(os.path.isfile(expected_file_name) == False)
    # dump to file
    dump(test_dir, test_file, context)
    # check if file re-created

# Generated at 2022-06-13 18:47:10.230500
# Unit test for function load

# Generated at 2022-06-13 18:47:13.941896
# Unit test for function load
def test_load():
    """
    Get the name of file in the replay directory.
    """
    file_name = 'load'
    replay_file = get_file_name('./', file_name)
    context = load('./', file_name)
    print(context)

if __name__ == '__main__':
    test_load()

# Generated at 2022-06-13 18:47:26.051548
# Unit test for function dump
def test_dump():
    from random import randint, random
    from string import ascii_letters
    from os import remove
    from os.path import exists

    replay_dir = 'test_dir'
    template_name = 'test_name'

    context = {
        'cookiecutter': {
            'random_str': ''.join([ascii_letters[randint(1, 52)] for i in range(randint(50, 100))]),
            'random_int': randint(1, 100),
            'random_float': random()
        }
    }

    try:
        dump(replay_dir, template_name, context)
        assert exists(replay_dir)
        assert exists(get_file_name(replay_dir, template_name))
    except IOError:
        assert False

# Generated at 2022-06-13 18:47:28.981910
# Unit test for function load
def test_load():
    # This runs the function
    load("/Users/vamsihassan/Desktop/test_cc_replay", "test_template")


# Generated at 2022-06-13 18:47:34.933901
# Unit test for function load
def test_load():
    replay_dir = os.path.join(os.path.expanduser('~'), '.cookiecutters')
    template_name = 'xilinx-pynq'
    try:
        context = load(replay_dir, template_name)
        assert context['cookiecutter']['project_name'] == 'pynq-helloworld'
    except ValueError:
        assert True
    except TypeError:
        assert True
    except FileNotFoundError:
        assert True


# Generated at 2022-06-13 18:47:44.640205
# Unit test for function load
def test_load():
    context1 = load(replay_dir="cookiecutter-sample-project", template_name="sample")
    assert "cookiecutter" in context1

# Generated at 2022-06-13 18:47:47.641751
# Unit test for function load
def test_load():
    from cookiecutter import replay
    replay.load('./tests/fake-repo-pre/', 'fake-repo-pre')


# Generated at 2022-06-13 18:47:58.153571
# Unit test for function load
def test_load():
    from dateutil import parser
    import datetime

    replay_dir = os.getcwd()
    template_name = 'python-flask'

    context = load(replay_dir, template_name)
    assert isinstance(context, dict)
    assert context['cookiecutter']['full_name'] == "Audrey Roy Greenfeld"
    assert parser.parse(context['cookiecutter']['date']) == datetime.datetime(2016, 10, 21, 6, 47, 39, 747000)
    assert context['cookiecutter']['email'] == "audreyr@example.com"
    assert context['cookiecutter']['project_name'] == "Python Flask Boilerplate"
    assert context['cookiecutter']['project_slug'] == "python_flask_boilerplate"