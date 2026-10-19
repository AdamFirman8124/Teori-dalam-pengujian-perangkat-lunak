

# Generated at 2022-06-13 18:38:29.486671
# Unit test for function load
def test_load():
    file_name = 'tests/fixtures/cookiecutters/foobar/cookiecutter.json'
    with open(file_name, 'r') as infile:
        context = json.load(infile)
    assert context == load('tests/fixtures/cookiecutters/foobar', 'cookiecutter')


# Generated at 2022-06-13 18:38:34.538005
# Unit test for function load
def test_load():
    """Test load function."""

    replay_dir = './replay_dir'
    template_name = './my_template'
    context = {
        'cookiecutter': {
            'repo_dir': '.',
            'abbreviations': {},
            'project_slug': 'test',
        }
    }
    dump(replay_dir, template_name, context)
    result = load(replay_dir, template_name)
    assert result == context
    os.remove(template_name+'.json')

# Generated at 2022-06-13 18:38:39.423789
# Unit test for function load
def test_load():
    replay_dir = './tests/fixtures/fake-replay-dir/'
    template_name = 'fake-replay-file'
    context = load(replay_dir, template_name)
    assert 'cookiecutter' in context
    assert '_template' in context['cookiecutter']
    assert context['cookiecutter']['_template'] == template_name

# Generated at 2022-06-13 18:38:41.413128
# Unit test for function load
def test_load():
    context_load = load('/tmp', 'test')
    assert isinstance(context_load, dict)


# Generated at 2022-06-13 18:38:47.892201
# Unit test for function dump
def test_dump():
    replay_dir = 'tests/fake-repo-pre/'
    template_name = 'fake-repo-pre'
    context = {'repo_name': 'dummy', 'cookiecutter': {'_template': 'tests/fake-repo-pre'}}
    dump(replay_dir, template_name, context)
    assert os.path.exists(get_file_name(replay_dir, template_name))

    # Cleanup
    os.remove(get_file_name(replay_dir, template_name))

# Generated at 2022-06-13 18:38:50.310420
# Unit test for function load
def test_load():
    """Test for function load."""
    print(load(None, None))


# Generated at 2022-06-13 18:39:03.138580
# Unit test for function load
def test_load():
    import json
    import os
    import pprint
    from cookiecutter import replay
    replay_dir = r'C:\Projects\cookiecutter'
    template_name = 'cookiecutter-pypackage'
    replay_file = replay.get_file_name(replay_dir, template_name)
    #pprint.pprint(replay_file)
    #print(os.path.exists(replay_file))
    #print(template_name.endswith('.json'))
    #print(os.path.join(replay_dir, template_name+'.json'))
    #print(os.path.join(replay_dir, template_name))
    #replay_file = os.path.join(replay_dir, template_name)
    #print(os.path

# Generated at 2022-06-13 18:39:05.072259
# Unit test for function load
def test_load():
    replay_context = load(replay_dir='.', template_name='cookiecutter-pypackage')
    print(replay_context)


# Generated at 2022-06-13 18:39:12.543583
# Unit test for function load
def test_load():
    replay_dir = "C:\\Users\\ashis\\PycharmProjects\\cookiecutter-pypackage (1)\\cookiecutter-pypackage\\tests\\test-output\\scenario"
    template_name = "cookiecutter-pypackage-master"
    context = load(replay_dir,template_name)
    print("context:", context)
    assert context['cookiecutter']['project_slug'] == 'cookiecutter-pypackage-master'
    assert context['cookiecutter']['project_name'] == 'Cookiecutter PyPackage Master'


# Generated at 2022-06-13 18:39:21.410751
# Unit test for function load
def test_load():
    """Unit test for function load."""
    import tempfile
    import json

    content = {'cookiecutter': {'name': 'cookiecutter-load-test-1'}}
    with tempfile.NamedTemporaryFile(
        mode='w+',
        suffix='.json',
        prefix='replay-',
        delete=True
    ) as tmp_file:
        json.dump(content, tmp_file)
        tmp_file.flush()

        replay_dir = os.path.dirname(tmp_file.name)
        assert load(replay_dir, 'replay-load-test-1.json') == content



# Generated at 2022-06-13 18:39:25.137736
# Unit test for function load
def test_load():
    template_name = 'simple_project'
    replay_dir = os.path.join(os.getcwd(), 'cookiecutter.replay')
    result = load(replay_dir, template_name)
    if not isinstance(result, dict):
        return False
    elif 'cookiecutter' not in result:
        return False
    else:
        return True



# Generated at 2022-06-13 18:39:28.169816
# Unit test for function load
def test_load():
    replay_dir = 'C:/cookiecutter-c2'
    template_name = 'conan-cmake-gtest'
    try:
        context = load(replay_dir, template_name)
        cookie_key = 'cookiecutter'
        if cookie_key in context:
            return True
        else:
            return False
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)
    except Exception as e:
        print(e)
    return False


# Generated at 2022-06-13 18:39:32.384372
# Unit test for function dump
def test_dump():
    replay_dir = os.path.expanduser('~')
    template_name = 'test'
    context = {'cookiecutter': {'key': 'value'}}
    dump(replay_dir, template_name, context)
    result = load(replay_dir, template_name)
    assert(result == context)



# Generated at 2022-06-13 18:39:40.271514
# Unit test for function load
def test_load():
    """Unit test for function load."""
    from cookiecutter.main import cookiecutter
    replay_dir = './replay'
    template_name = 'gh:audreyr/cookiecutter-pypackage'
    # replay_dir = '{{ cookiecutter.replay_dir }}'
    # template_name = '{{ cookiecutter.replay_template }}'

    # context = cookiecutter(template_name, replay_dir=replay_dir, overwrite_if_exists=True)
    # print('context: {}'.format(context))
    context = load(replay_dir, template_name)
    print('context: {}'.format(context))

if __name__ == '__main__':
    # Unit test for function load
    test_load()

# Generated at 2022-06-13 18:39:43.259450
# Unit test for function load
def test_load():
    assert load("replay_dir", "template_name") == {"cookiecutter": "context"}

# Generated at 2022-06-13 18:39:46.118716
# Unit test for function load
def test_load():
    assert load('test_dir', 'test_templates') == { 'cookiecutter' : {} }

# Generated at 2022-06-13 18:39:48.978279
# Unit test for function load
def test_load():
    assert load(replay_dir = "replay_dir", template_name = "template_name" )


# Generated at 2022-06-13 18:39:53.567539
# Unit test for function load
def test_load():
    file = load('./tests/test-load-replay', 'fake-template')
    default = file['cookiecutter']['default_context']
    assert default['full_name'] is 'Your Name'
    assert default['email'] is 'your@email.example.com'
    assert default['github_username'] is 'your_github_username_here'

# Generated at 2022-06-13 18:39:56.218557
# Unit test for function load
def test_load():
    replay_dir = '/Users/taylorp/Desktop/replay-test/'
    template_name = 'test-replay.json'
    assert isinstance(load(replay_dir, template_name), dict)


# Generated at 2022-06-13 18:39:59.710430
# Unit test for function load
def test_load():
    """Unit test for function load"""
    # Load context
    replay_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'tests/fixtures/fake-replay-dir/'
    )
    template_name = 'fake-repo-pre/'
    context = load(replay_dir, template_name)

    # Check context
    assert context['cookiecutter']['project_name'] == 'Cookiecutter Admin'

# Generated at 2022-06-13 18:40:06.568232
# Unit test for function load
def test_load():
    replay_dir='/home/sarachaii/Documents/mycookiecutter/cookiecutter-pypackage/tests/replay_dir/'
    template_name='cookiecutter-pypackage'
    load(replay_dir, template_name)



# Generated at 2022-06-13 18:40:09.301374
# Unit test for function load
def test_load():
    load(replay_dir="cookiecutter.replay", template_name="test")
    return



# Generated at 2022-06-13 18:40:14.830796
# Unit test for function load
def test_load():
    """Test the load function."""
    test_dir = r'C:\Users\Administrator\cookiecutters\tests\test-load-replay'
    template_name = 'foo'
    context = load(test_dir, template_name)
    print(context)
    assert context is not None
    assert context['cookiecutter'] is not None


# Generated at 2022-06-13 18:40:22.865837
# Unit test for function dump
def test_dump():
    replay_dir = '/tmp/cookiecutter-tests/'
    template_name = 'test-template'

    context = {
        'cookiecutter': {
            'first_name': 'Audrey',
            'last_name': 'Roy',
            'email': 'audreyr@example.com',
            'project_name': 'My Project',
            'repo_name': 'my_project',
            'project_short_description': 'A short description of the project.'
        }
    }

    dump(replay_dir, template_name, context)

    replay_file = get_file_name(replay_dir, template_name)

    assert os.path.isfile(replay_file) is True


# Generated at 2022-06-13 18:40:33.874910
# Unit test for function dump
def test_dump():
    from cookiecutter.main import cookiecutter
    import tempfile
    import shutil
    import json

    template = 'https://github.com/JWKennington/cookiecutter-pypackage-minimal.git'
    context = {
        'cookiecutter': {
            'package_name': 'Hi',
            'project_name': 'Hello',
            'project_short_description': 'what',
        }
    }

    replay_dir = tempfile.mkdtemp()
    cookiecutter(template, replay_dir=replay_dir)

    replay_file = get_file_name(replay_dir, template)

    with open(replay_file, 'r') as infile:
        replay_data = json.load(infile)

    # Check the replay file contains the correct values

# Generated at 2022-06-13 18:40:42.346163
# Unit test for function dump
def test_dump():
    """Unit test for function dump"""
    import tempfile
    from cookiecutter.main import cookiecutter

    with tempfile.TemporaryDirectory() as tmpdir:
        # Only way to test dump is to call cookiecutter
        # and then test replay file is written.
        cookiecutter(
            'tests/test-cookiecutter-repo/',
            no_input=True,
            replay_dir=tmpdir,
        )
        assert os.path.exists(os.path.join(tmpdir, 'example_template.json'))

        # Run cookiecutter again, but this time with no-input true and
        # use replay file.

# Generated at 2022-06-13 18:40:49.514266
# Unit test for function load
def test_load():
    test_context = {
        "cookiecutter": {
            "name": "NirantK",
            "email": "nirantk@gmail.com",
            "github_username": "nirantk",
            "project_name": "cookiecutter-pylibrary",
            "project_short_description": "A Python library",
            "release_date": "2017-06-01",
            "use_pytest": "y",
            "command_line_interface": "Click",
            "open_source_license": "MIT",
            "pypi_username": "nirantk",
            "version": "0.1.0"
        }
    }
    test_dir = os.getcwd()+'/test'
    test_template_name = 'cookiecutter-pylibrary'

# Generated at 2022-06-13 18:40:53.321306
# Unit test for function load
def test_load():
    replay_dir = 'foo'
    template_name = 'bar'
    with open('foo/bar.json', 'w') as infile:
        msg = "abc"
        infile.write(msg)
    context = load(replay_dir, template_name)
    assert context == msg


# Generated at 2022-06-13 18:40:59.414453
# Unit test for function dump
def test_dump():
    # Instantiate the replay dir
    replay_dir = 'cookiecutter_replays'

    try:
        # Instantiate the name of the file
        template_name = 'cookiecutter-pypackage'

        # Instantiate the context
        context = {'cookiecutter': {'full_name': 'Your Name',
                                    'project_name': 'Hello World'}}

        # Call the function dump
        dump(replay_dir, template_name, context)
    finally:
        # Delete the file
        os.remove(get_file_name(replay_dir, template_name))


# Generated at 2022-06-13 18:41:03.163691
# Unit test for function load
def test_load():
    """Test function load"""
    tp_name = 'xzf'
    context = {'cookiecutter': {'cc_project_name': 'cookiecutter-xzf'}}
    # print(load(replay_dir, tp_name))
    assert load('replay', tp_name) == context


# Generated at 2022-06-13 18:41:12.011385
# Unit test for function dump
def test_dump():
    replay_dir = 'tests/test-output/replay'
    template_name = 'test-replay'
    context = {'cookiecutter': 'test'}
    try:
        dump(replay_dir, template_name, context)
    except:
        assert False
    finally:
        try:
            os.remove('tests/test-output/replay/test-replay.json')
            os.removedirs('tests/test-output/replay')
        except:
            pass

if __name__ == '__main__':
    test_dump()

# Generated at 2022-06-13 18:41:16.890785
# Unit test for function dump
def test_dump():
    # test case
    replay_dir = ".tests"
    context = {"cookiecutter": "{{cookiecutter}}"}
    template_name = "123.json"
    dump(replay_dir, template_name, context)
    t = load(replay_dir, template_name)
    assert t == context


# Generated at 2022-06-13 18:41:22.724244
# Unit test for function dump
def test_dump():
    replay_dir = "input"
    template_name = "test"
    context = {
        'cookiecutter': {
            "first_name": "Jonathan",
            "last_name": "Pepin",
            "email": "jonathan.pepin@gmail.com",
            "github_username": "jonathanpepin",
            "project_name": "cookiecutter-cspot"
        }
    }
    dump(replay_dir, template_name, context)


# Generated at 2022-06-13 18:41:33.510193
# Unit test for function load
def test_load():
    replay_dir = os.path.normpath(os.path.join(
        os.path.dirname(__file__), '..', 'tests', 'files', 'replay', 'tests'))
    template_name = 'test_template'
    context = load(replay_dir, template_name)
    expected = {
        'cookiecutter': {
            'full_name': 'Your Name',
            'email': 'youremail@whatever.com',
            'project_name': 'Cookiecutter-Test-Project-Template',
            'repo_name': 'cookiecutter_test_project',
            'project_slug': 'cookiecutter_test_project',
            'project_short_description': 'A short description of the project.'
        }
    }
    assert context == expected


# Generated at 2022-06-13 18:41:36.146723
# Unit test for function load
def test_load():
    """Unit test for function load."""
    load(replay_dir='./', template_name='replay_test')


# Generated at 2022-06-13 18:41:43.085000
# Unit test for function dump
def test_dump():

    replay_dir = '~/.cookiecutters'
    template_name = 'cookiecutter-pypackage'

# Generated at 2022-06-13 18:41:50.031684
# Unit test for function dump
def test_dump():
    replay_dir = "replay"
    template_name = "template_name"

# Generated at 2022-06-13 18:41:57.011128
# Unit test for function load
def test_load():
    """Unit test for function load."""
    context = load('replay', 'cookiecutter-pypackage')
    assert(isinstance(context, dict))
    assert(context['cookiecutter']['full_name'] == 'Samuel Bishop')
    assert(not context['cookiecutter']['open_source_license'] == 'MIT')
    context = load('replay', 'cookiecutter-pypackage.json')
    assert(isinstance(context, dict))
    assert(context['cookiecutter']['full_name'] == 'Samuel Bishop')
    assert(not context['cookiecutter']['open_source_license'] == 'MIT')

# Generated at 2022-06-13 18:41:59.517992
# Unit test for function load
def test_load():
    import doctest
    #doctest.testmod()
    doctest.run_docstring_examples(load, globals())

# Debugging
#test_load()

# Generated at 2022-06-13 18:42:05.932388
# Unit test for function dump
def test_dump():
    replay_dir = 'C:\\Users\\shuangluo\\Desktop\\test_replay'
    template_name = 'test_template'
    context = {'cookiecutter': {'full_name': 'Shuang Luo', 'email': 'shuangluo@shuangluo@gmail.com', 'replay_dir': 'C:\\Users\\shuangluo\\Desktop\\test_replay'}}
    dump(replay_dir, template_name, context)
    print('Write data successfully!')


# Generated at 2022-06-13 18:42:12.372389
# Unit test for function load
def test_load():
    assert(load("C:/Users/Legion/Desktop", "xxx.json"))

# Generated at 2022-06-13 18:42:15.964948
# Unit test for function load
def test_load():
    template_name = 'test_template'
    replay_dir = 'test_replay'
    context = {'cookiecutter': {'key': 'value'}}
    dump(replay_dir, template_name, context)
    assert context == load(replay_dir, template_name)



# Generated at 2022-06-13 18:42:21.413321
# Unit test for function dump
def test_dump():
    from cookiecutter.main import cookiecutter
    from cookiecutter.main import get_user_config
    from cookiecutter.main import get_config_from_repo
    from cookiecutter.main import expand_abbreviations
    from cookiecutter.main import expand_abbreviations_interactively
    from cookiecutter.main import make_context_file
    from cookiecutter.main import generate_context
    from cookiecutter.main import temp_and_replay_dir
    from cookiecutter.main import prompt_for_config

    user_config = get_user_config()
    config_dict = get_config_from_repo(user_config['default_repo'])

# Generated at 2022-06-13 18:42:23.693867
# Unit test for function load
def test_load():
    context = load('tests/test-replay', 'tests/test-repo-pre/')
    assert 'cookiecutter' in context


# Generated at 2022-06-13 18:42:31.007592
# Unit test for function dump
def test_dump():
    import os
    import shutil
    replay_dir = '/tmp'
    template_name = 'example.json'
    context = {"cookiecutter":{"a":"b"}}
    #  test dump
    dump(replay_dir, template_name, context)
    #  test load
    load(replay_dir, template_name)
    #  test load with wrong replay_dir
    load(replay_dir+"_", template_name)
    #  test load with wrong template_name
    load(replay_dir, template_name+"_")
    # clean up
    file_name = get_file_name(replay_dir, template_name)
    os.remove(file_name)

# Generated at 2022-06-13 18:42:31.363977
# Unit test for function load
def test_load():
    assert 1 == 1

# Generated at 2022-06-13 18:42:33.637536
# Unit test for function load
def test_load():
    replay_file = get_file_name("/home/xzou2/Desktop/Cookiecutter/tests/fake-repo-pre/", "fake_repo_pre")
    with open(replay_file, 'r') as infile:
        context = json.load(infile)
    print("Replay file:", context)

test_load()

# Generated at 2022-06-13 18:42:41.897775
# Unit test for function dump
def test_dump():
    replay_dir = os.path.join(os.getcwd(), 'tests', 'test_replay')
    template_name = 'test_project'
    empty_context = {
        'cookiecutter': {},
    }

# Generated at 2022-06-13 18:42:54.202604
# Unit test for function load
def test_load():
    """
    Test load function.
    """
    from cookiecutter import replay
    from cookiecutter import utils
    from cookiecutter.main import cookiecutter
    replay_dir = utils.make_sure_path_exists('/tmp/cookiecutter-tests')
    template_name = 'cookiecutter-pypackage'
    context = cookiecutter(
        'https://github.com/audreyr/cookiecutter-pypackage.git',
        extra_context={'replay_dir': replay_dir},
        replay=True,
    )
    replay.dump(replay_dir, template_name, context)
    context = replay.load(replay_dir, template_name)
    assert context['package_name'] == 'cookiecutter-pypackage'

# Generated at 2022-06-13 18:43:00.891617
# Unit test for function dump
def test_dump():
    """Test function Replay.dump()."""
    import tempfile
    replay_dir = tempfile.mkdtemp()
    template = 'cookiecutter-pypackage'
    context = {
        'cookiecutter': {
            'full_name': 'Julien Duponchelle',
            'email': 'julien@duponchelle.info',
            'github_username': 'juliendupond'
        }
    }

    dump(replay_dir, template, context)

    assert os.path.exists(get_file_name(replay_dir, template))
    os.remove(get_file_name(replay_dir, template))
    os.rmdir(replay_dir)



# Generated at 2022-06-13 18:43:07.365772
# Unit test for function load
def test_load():
    context = load("..", "cookiecutter.json")
    assert 'cookiecutter' in context


# Generated at 2022-06-13 18:43:11.451361
# Unit test for function load
def test_load():
    replay_dir = './tests/files/replay'
    template_name = 'fake-repo-pre'
    context = load(replay_dir, template_name)

    assert isinstance(context, dict)
    assert 'cookiecutter' in context


# Generated at 2022-06-13 18:43:15.670088
# Unit test for function load
def test_load():

    context = load('./tests/fake-repo-pre/', 'fake-repo')

    assert 'cookiecutter' in context
    assert len(context.keys()) == 1
    assert len(context['cookiecutter'].keys()) == 2



# Generated at 2022-06-13 18:43:19.253549
# Unit test for function load
def test_load():
    print("Testing function load")
    context = load("examples/replay-dir", "cookiecutter-pypackage")
    assert context
    assert isinstance(context, dict)
    assert 'cookiecutter' in context


# Generated at 2022-06-13 18:43:25.597120
# Unit test for function dump
def test_dump():
    """Unit test for function dump."""
    replay_dir = os.path.join(os.getcwd(), "tests", "test_replay")

    template_name = "test_template"
    context = {"cookiecutter": {"full_name": "Full Name", "email": "test@example.com"}}

    dump(replay_dir, template_name, context)

    # Check if file is created
    replay_file = os.path.join(replay_dir, template_name + ".json")
    try:
        with open(replay_file, 'r') as infile:
            json_data = json.load(infile)

        # Check if dict keys are as expected
        assert set(json_data.keys()) == set(context.keys())
    except IOError:
        assert False


# Unit

# Generated at 2022-06-13 18:43:32.397206
# Unit test for function load
def test_load():
    from os.path import join, dirname, abspath
    here = abspath(dirname(__file__))
    replay_dir = join(here, 'replay')
    template_name = 'cookiecutter-pypackage'
    context = load(replay_dir, template_name)

# Generated at 2022-06-13 18:43:44.592212
# Unit test for function dump
def test_dump():
    """Test for function dump."""
    import tempfile
    reload(tempfile)
    from tempfile import mkdtemp
    tmp_dir = mkdtemp()

    import os
    from cookiecutter.replay import dump
    from cookiecutter.replay import load

    context = {
        'cookiecutter': {
            'name': 'Donald E. Knuth',
        }
    }
    template_name = 'template1'
    dump(tmp_dir, template_name, context)

    assert os.path.exists(
        os.path.join(tmp_dir, template_name + '.json')
    )

    context_load = load(tmp_dir, template_name)

    # Test that the saved and loaded contexts are equal
    assert context == context_load

    # Test that the saved and loaded contexts are

# Generated at 2022-06-13 18:43:49.035294
# Unit test for function load
def test_load():
    temp_context = {"cookiecutter": {"a": "b"}}
    replay_dir = "tests/test_load"
    template_name = "test_replay_file"
    replay_file = get_file_name(replay_dir, template_name)

    with open(replay_file, 'w') as outfile:
        json.dump(temp_context, outfile, indent = 2)

    context = load(replay_dir, template_name)

    assert context == temp_context

    os.remove(replay_file)


# Generated at 2022-06-13 18:43:51.822307
# Unit test for function load
def test_load():
    """Unit test for function load."""
    context = load("replay_dir/", "template_name")
    assert context

# Generated at 2022-06-13 18:43:55.303183
# Unit test for function load
def test_load():
    replay_dir=os.path.join(os.getcwd(),'tests','files','test-load-replay')
    template_name='load-replay-file'

    context=load(replay_dir,template_name)
    print(context)


# Generated at 2022-06-13 18:44:09.129908
# Unit test for function load
def test_load():
    template_name = 'cookiecutter-pypackage'
    replay_dir = 'C:\\Users\\zihaoz\\Desktop\\cookiecutter-pypackage\\.cookiecutter_replay'
    context = load(replay_dir, template_name)
    print(context)

if __name__ == '__main__':
    test_load()

# Generated at 2022-06-13 18:44:16.422817
# Unit test for function load

# Generated at 2022-06-13 18:44:23.059485
# Unit test for function dump
def test_dump():
    import tempfile
    from cookiecutter.main import cookiecutter
    from cookiecutter import exceptions
    from cookiecutter import replay

    replay_dir = tempfile.mkdtemp()
    context = cookiecutter('.', output_dir=replay_dir, replay=True, replay_dir=replay_dir)
    template_name = '.'

    replay.dump(replay_dir, template_name, context)
    context_test = replay.load(replay_dir, template_name)
    assert context_test == context

# Generated at 2022-06-13 18:44:25.776436
# Unit test for function load
def test_load():
    print(load('/home/wankun/.cookiecutters','pip-python'))


if __name__ == '__main__':
    test_load()

# Generated at 2022-06-13 18:44:29.397969
# Unit test for function load
def test_load():
    replay_dir = 'test/myreplaydir/'
    template_name = 'cookiecutter-pypackage'
    context = load(replay_dir, template_name)
    assert(context['cookiecutter']['project_slug'] == 'cookiecutter-pypackage')

# Generated at 2022-06-13 18:44:32.755633
# Unit test for function dump
def test_dump():
    # Write json data to file
    context = {'cookiecutter': {'project_name': 'foo'}}
    dump('/tmp/replay', 'bar', context)
    # Load json data from file
    loaded_context = load('/tmp/replay', 'bar')
    # Confirm that the replay file works
    assert loaded_context == context

# Generated at 2022-06-13 18:44:39.121449
# Unit test for function dump
def test_dump():
    import os
    import shutil
    replay_dir = 'tests/test-output/replay'
    template_name = 'example'
    context = {'cookiecutter': {'replay': True}}
    dump(replay_dir, template_name, context)
    assert os.path.exists(os.path.join(replay_dir, 'example.json'))
    shutil.rmtree(replay_dir)


# Generated at 2022-06-13 18:44:41.683040
# Unit test for function load
def test_load():
    test_exception = False
    try:
        load(os.path.expanduser("~/.cookiecutters"), "Nonexisting")
    except Exception:
        test_exception = True

    assert(test_exception)



# Generated at 2022-06-13 18:44:45.476339
# Unit test for function dump
def test_dump():
    path = './tests/files/'
    name = path + 'replay.json'
    context = {'cookiecutter':{'full_name': 'tom', 'email': 'tom@tom.com'}}
    dump(path, name, context)


# Generated at 2022-06-13 18:44:47.978914
# Unit test for function load
def test_load():
    load('/home/wangqiang/cookiecutter-demo', 'demo')
    



# Generated at 2022-06-13 18:45:13.436492
# Unit test for function load
def test_load():
    """Unit testing for function load."""
    replay_dir = 'cookiecutter/tests/test-load-replay'
    template_name = 'test'
    context = { 'cookiecutter' : {'name': 'test'} }
    dump(replay_dir, template_name, context)
    check_context = load(replay_dir, template_name)
    os.remove(get_file_name(replay_dir, template_name))
    assert context == check_context
        

# Generated at 2022-06-13 18:45:23.428510
# Unit test for function load
def test_load():
    """Test load function."""
    from cookiecutter.main import cookiecutter
    template = 'tests/test-slash-in-dir-name/'
    replay_dir = os.path.join('tests', 'test-output', 'test-slash-in-dir-name')
    replay_file = get_file_name(replay_dir, 'tests/test-slash-in-dir-name')
    make_sure_path_exists(replay_dir)

    # Create an example file in user defined replay_dir
    with open(replay_file, 'w') as outfile:
        context = cookiecutter(template)
        json.dump(context, outfile, indent=2)

    # Test the load function
    load_context = load(replay_dir, replay_file)
    assert load

# Generated at 2022-06-13 18:45:24.658717
# Unit test for function load
def test_load():
    context = load('/home/thomas', 'test.json')
    assert "cookiecutter" in context
    assert type(context['cookiecutter'])



# Generated at 2022-06-13 18:45:28.613343
# Unit test for function load
def test_load():
    """Unit test for function load."""
    expected = {
        'project_name': 'DjangoTest',
        'project_slug': 'djangotest'
    }
    assert load('tests/test-replay', 'tests/test-replay/DjangoTest.json') == expected

# Generated at 2022-06-13 18:45:31.501278
# Unit test for function dump
def test_dump():
    dump('C:/Users/user/AppData/Local/cookiecutter/replay/', 'test', {'cookiecutter': 'test'})



# Generated at 2022-06-13 18:45:38.292248
# Unit test for function load
def test_load():
    import random
    import string
    replay_dir = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(20))
    template_name = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(20))
    context = {'cookiecutter':'hi'}
    fname = get_file_name(replay_dir, template_name)
    with open(fname, 'w') as outfile:
        json.dump(context, outfile, indent=2)
    res = load(replay_dir, template_name)
    assert res['cookiecutter'] == 'hi'
    os.remove(fname)

# Generated at 2022-06-13 18:45:39.009295
# Unit test for function load
def test_load():
    pass

# Generated at 2022-06-13 18:45:45.173008
# Unit test for function dump
def test_dump():
    template_name = 'example_path'
    context = {'cookiecutter': {'abc': '123'}}
    import tempfile
    with tempfile.TemporaryDirectory() as replay_dir:
        dump(replay_dir, template_name, context)
        context2 = load(replay_dir, template_name)
        assert context == context2
test_dump()

# Generated at 2022-06-13 18:45:50.710070
# Unit test for function load
def test_load():
    context = load('/Users/yancharung/Desktop/mission-Impossible2/cookiecutter-pypackage', 'mission-Impossible2')
    print(context)
    assert isinstance(context, dict)
    assert 'cookiecutter' in context.keys()

test_load()

# Generated at 2022-06-13 18:45:57.742242
# Unit test for function dump
def test_dump():
    template_name = 'cc_cookiecutter_pypackage'
    replay_dir = 'tests/test-output/.cookiecutters'
    context = { 'cookiecutter': {'_template': 'cc_cookiecutter_pypackage',
                                'author_name': 'Test', 'full_name': 'Test',
                                'github_username': 'Tester',
                                'project_name': 'test', 'project_slug': 'test',
                                'project_type': 'pypackage',
                                'release_date': '', 'year': '2017'} }
    dump(replay_dir, template_name, context)



# Generated at 2022-06-13 18:46:45.281745
# Unit test for function dump
def test_dump():
    test_template_name = 'hello'
    test_context = {'cookiecutter': {'test_input':'test_value'}}
    test_replay_dir = os.path.join(os.getcwd(), 'tests', 'test-replay')
    test_replay_file_name = get_file_name(test_replay_dir, test_template_name)
    dump(test_replay_dir, test_template_name, test_context)

    assert os.path.exists(test_replay_file_name) == True, 'error: cannot create replay file'
    os.remove(test_replay_file_name)



# Generated at 2022-06-13 18:46:48.522157
# Unit test for function dump
def test_dump():   #pylint: disable=R0201
    """Make sure dump works as expected."""
    dump_path = os.path.realpath('tests/test-dump')
    dump(dump_path, 'test-dump', {'cookiecutter': {'hello': 'world'}})
    assert os.path.isfile(get_file_name(dump_path, 'test-dump'))
    os.remove(get_file_name(dump_path, 'test-dump'))

# Generated at 2022-06-13 18:46:56.070240
# Unit test for function load
def test_load():
    replay_file = get_file_name(replay_dir = 'replays', template_name = 'jk-project-test')
    context = load(replay_file, template_name = 'jk-project-test')
    print('context is: ' + str(context))
    print('cookiecutter.project_name is: ' + str(context['cookiecutter']['project_name']))
    if not context['cookiecutter']['project_name']:
        print('Error')
    else:
        print('Success')


# Generated at 2022-06-13 18:47:00.742474
# Unit test for function load
def test_load():
    context = {'cookiecutter': {'test_load': 'test_load'}}
    replay_file = "test_load.json"
    dump('.', replay_file, context)
    assert get_file_name('.', replay_file) == "./test_load.json"
    assert load('.', replay_file) == context
    os.remove(replay_file)

if __name__ == '__main__':
    test_load()

# Generated at 2022-06-13 18:47:04.800300
# Unit test for function dump
def test_dump():
    # Set up fake data
    cookiecutter = {'cookiecutter': 'test_cookiecutter'}
    test_data = cookiecutter
    # Create an empty directory
    replay_dir = 'tests/test_replay'
    template_name = 'test_template_name'
    # Run function
    dump(replay_dir, template_name, test_data)
    # Open file and read content
    read_file = open(get_file_name(replay_dir, template_name), 'r')
    read_data = json.load(read_file)
    # Close file
    read_file.close()
    # Assert that test data is the same as the content in the file
    assert test_data == read_data


# Generated at 2022-06-13 18:47:14.075906
# Unit test for function dump
def test_dump():
    # Test with a None replay dir
    replay_dir = None
    template_name = 'test_template_name'
    context = {}
    try:
        dump(replay_dir, template_name, context)
        assert False
    except TypeError:
        assert True

    # Test with a None template_name
    replay_dir = './test_replay_dir'
    template_name = None
    try:
        dump(replay_dir, template_name, context)
        assert False
    except TypeError:
        assert True
    
    # Test with a None context
    template_name = 'test_template_name'
    context = None
    try:
        dump(replay_dir, template_name, context)
        assert False
    except TypeError:
        assert True

    # Test success
   

# Generated at 2022-06-13 18:47:19.552500
# Unit test for function dump
def test_dump():
    """Unit test for function dump."""
    replay_dir = '/Users/sebastiantoth/Desktop/pip'
    template_name = 'cookiecutter-pypackage'
    context = {'project_name': 'My Project', 'project_slug': 'my_project'}
    dump(replay_dir, template_name, context)


# Generated at 2022-06-13 18:47:23.185915
# Unit test for function load
def test_load():
    replay_dir = 'tests/test-replay/'
    template_name = 'python-basic/'
    context = load(replay_dir, template_name)
    Cookiecutter = context['cookiecutter']

# Generated at 2022-06-13 18:47:34.470594
# Unit test for function load
def test_load():
    replay_dir = "./fake_dir"
    template_name = "fake_template"
    context = {"cookiecutter": {"project_name": "fake_project_name"}}
    context_bad = {"cookiecutter":{}}
    try:
        load(replay_dir, template_name)
    except IOError:
        pass
    make_sure_path_exists(replay_dir)
    try:
        load(replay_dir, template_name)
    except FileNotFoundError:
        pass
    dump(replay_dir, template_name, context)
    new_context = load(replay_dir, template_name)
    assert new_context == context
    try:
        dump(replay_dir, template_name, context_bad)
    except ValueError:
        pass

# Generated at 2022-06-13 18:47:36.135417
# Unit test for function load
def test_load():
    assert load('./', './') == load('./', './')