

# Generated at 2022-06-13 18:38:28.687897
# Unit test for function load
def test_load():
    a=load('./','project_name')
    assert isinstance(a,dict)==True


# Generated at 2022-06-13 18:38:35.769794
# Unit test for function load
def test_load():
    # get the path of this file
    currentDir = os.path.dirname(os.path.abspath(__file__))
    # get the path of the parent directory
    parenrDir = os.path.dirname(currentDir)
    # get the name of this file
    fileName = os.path.basename(__file__)
    # get the name of the file without extension
    fileName = fileName.split('.')[0]
    
    replay_dir = parenrDir+ "/" + fileName + "_replay"
    template_name = "test_template"
    context = {
        "cookiecutter": {
            "full_name": "Dong Wang",
            "email": "wdong@wdong.org"
        }
    }

# Generated at 2022-06-13 18:38:42.081219
# Unit test for function load
def test_load():
    replay_dir = 'replay_dir'
    template_name = 'test_name'
    replay_file = get_file_name(replay_dir, template_name)
    context = {'cookiecutter': {'test_json': 'test_json'}}
    with open(replay_file, 'w') as outfile:
        json.dump(context, outfile, indent=2)

    assert load(replay_dir, template_name) == context

# Generated at 2022-06-13 18:38:43.599203
# Unit test for function load
def test_load():
    context = load(os.path.expanduser("~/.cookiecutters"), "tutorial")
    assert context["cookiecutter"]["repo_name"] == 'cookiecutter-tutorial'

# Generated at 2022-06-13 18:38:48.384328
# Unit test for function load
def test_load():
    """
    Unit test for function load
    """
    import os
    import shutil
    import cookiecutter

    template = cookiecutter.repository.find_template()
    context = cookiecutter.generate_context(template)

    template_name = template.split('/')[-1]
    template_dir = os.path.dirname(template)

    replay_dir = '/tmp/cookiecutter_test'
    if os.path.exists(replay_dir):
        shutil.rmtree(replay_dir)

    dump(replay_dir, template_name, context)
    assert load(replay_dir, template_name) == context

    # replay file does not exist
    replay_file = get_file_name(replay_dir, template_name)

# Generated at 2022-06-13 18:38:54.992221
# Unit test for function load
def test_load():
    # Given
    replay_dir = "/Users/mike/Dev/cookiecutter_test_replay_4"
    template_name = "cookiecutter-pypackage-minimal"
    # When
    context = load(replay_dir, template_name)
    # Then
    assert context["cookiecutter"]["project_name"] == "Python Package"

# Generated at 2022-06-13 18:39:04.937283
# Unit test for function load
def test_load():
    """Unit testing."""
    from tempfile import mkdtemp
    from shutil import rmtree

    tmpdir = mkdtemp()

    context = {
        'cookiecutter': {
            'full_name': 'full_name',
        },
    }

    dump(tmpdir, 'test_replay', context)
    replay_context = load(tmpdir, 'test_replay')

    if context == replay_context:
        print('unit test passed!')
    else:
        print('unit test failed!')

    rmtree(tmpdir)
    print('test_load() finished execution')

# Generated at 2022-06-13 18:39:11.852092
# Unit test for function load
def test_load():
    # file name
    fn = 'replay_test.json'
    # json data
    jd = '{"hello": "world"}'

    # create replay_test.json
    with open(fn, 'w') as jsonfile:
        jsonfile.write(jd)
    # load from file
    jdreturn = load('.', fn)

    # delete replay_test.json
    os.remove(fn)

    # check the json data
    assert jdreturn == {"hello": "world"}


# Generated at 2022-06-13 18:39:14.163856
# Unit test for function load
def test_load():
    context = load('replay','test')
    assert isinstance(context, dict)
    # Test if the file has a required key
    try:
        assert 'cookiecutter' in context
    except AssertionError:
        raise ValueError('Context is required to contain a cookiecutter key')


# Generated at 2022-06-13 18:39:21.013990
# Unit test for function load
def test_load():
    replay_dir = './tests/test-load-replay/'
    template_name = 'test-replay'
    context = {'cookiecutter': {
        'project_name': 'test-replay', 'project_slug': 'test_replay'}}
    dump(replay_dir, template_name, context)
    loaded_context = load(replay_dir, template_name)
    if loaded_context == context:
        pass
    else:
        raise Exception


# Generated at 2022-06-13 18:39:23.629331
# Unit test for function load
def test_load():
    replay_dir = "replay"
    template_name = "test.json"
    context = load(replay_dir, template_name)
    print(context)



# Generated at 2022-06-13 18:39:27.596164
# Unit test for function load
def test_load():
    import pudb;pu.db
    replay_dir = '/Users/Ryan/gee/geoedf/cookiecutter-cookiecutter-python'
    template_name = 'your_full_name'
    context = load(replay_dir, template_name)
    print(context)


if __name__ == '__main__':
    test_load()

# Generated at 2022-06-13 18:39:33.538611
# Unit test for function load
def test_load():
    # Create a test directory to perform a test
    from tempfile import mkdtemp
    from shutil import rmtree
    tmpdir = mkdtemp()
    context = {'cookiecutter' : {'first_name' : 'Foo', 'last_name' : 'Bar'}}
    dump(tmpdir, 'test', context)
    loaded = load(tmpdir, 'test')
    rmtree(tmpdir)
    if context == loaded:
        print('test_load success')
    else:
        print('test_load failure')

# Generated at 2022-06-13 18:39:37.581013
# Unit test for function load

# Generated at 2022-06-13 18:39:53.933582
# Unit test for function dump
def test_dump():
    replay_dir = '/tmp/replay_dir'
    template_name = 'dummy_project'

# Generated at 2022-06-13 18:39:56.566232
# Unit test for function dump
def test_dump():
    replay_dir = '.replay'
    template_name = 'test'
    context = {'cookiecutter': {'key1': 'value1'}}
    dump(replay_dir, template_name, context)


# Generated at 2022-06-13 18:40:02.043157
# Unit test for function dump
def test_dump():
    import os
    import shutil
    from cookiecutter.replay import dump
    from cookiecutter.utils import make_sure_path_exists

    # Make a fake directory
    temp_dir = os.path.join(os.getcwd(), 'test_temp_dir')
    if make_sure_path_exists(temp_dir):
        shutil.rmtree(temp_dir)

    # Write some data to a file
    test_context = {'cookiecutter': {'project_name': 'Python Boilerplate'}}
    dump(temp_dir, 'foobar_template', test_context)

    # Load the data from the file
    from cookiecutter.replay import load
    new_context = load(temp_dir, 'foobar_template')

    # Compare the two
    import pprint


# Generated at 2022-06-13 18:40:06.441037
# Unit test for function load
def test_load():
    context = load('replay_files/', 'cookiecutter-pypackage')
    if context['cookiecutter']['description'] == '':
        print('context_description is empty')
    else:
        print(context['cookiecutter']['description'])

# Generated at 2022-06-13 18:40:08.042629
# Unit test for function load
def test_load():
    assert load('replay', 'foo123')
    # assert load(123, 'foo123')


# Generated at 2022-06-13 18:40:12.456160
# Unit test for function load
def test_load(): # pragma: no cover
    replay_dir = os.path.join(os.getcwd(), 'tests', 'test-replay')
    template_name = 'fake'
    context = load(replay_dir, template_name)
    assert context['cookiecutter']['project_name'] == 'Fake Project'


# Generated at 2022-06-13 18:40:17.257671
# Unit test for function load
def test_load():
    replay_dir = "../report_temp1"
    template_name = "report_template"
    context = load(replay_dir, template_name)

# Generated at 2022-06-13 18:40:20.247251
# Unit test for function load
def test_load():
    template_name = 'test_template'
    replay_dir = 'test_dir'
    context = load(replay_dir, template_name)
    assert isinstance(context, dict)
    assert 'cookiecutter' in context


# Generated at 2022-06-13 18:40:21.609865
# Unit test for function load
def test_load():
    assert load(replay_dir="replay", template_name="test") == {"test":0}


# Generated at 2022-06-13 18:40:26.191869
# Unit test for function dump
def test_dump():
    context = {'cookiecutter': {'full_name': 'Test User',
                                'email': 'test@example.com',
                                'project_name': 'Test Project'}}

    replay_dir = os.path.join(os.path.dirname(__file__), '..', 'tests', 'test-replay')
    template_name = 'dummy-project'

    dump(replay_dir, template_name, context)

    assert os.path.isfile(os.path.join(replay_dir, template_name))


# Generated at 2022-06-13 18:40:31.276275
# Unit test for function load

# Generated at 2022-06-13 18:40:41.233635
# Unit test for function dump
def test_dump():
    replay_dir = 'tests/files/test-replay'
    template_name = 'test-project'


# Generated at 2022-06-13 18:40:45.905538
# Unit test for function load
def test_load():
    # Params
    replay_dir = "/Users/hejunfei/Documents/GitHub/Cookiecutter-Templates/project-templates/python-library/"
    template_name = "python-library"
    
    # Call function to test
    context = load(replay_dir, template_name)
    print(context)
    print(context.keys())


# Generated at 2022-06-13 18:40:52.620656
# Unit test for function load
def test_load():
    """Test for function load."""
    # Test for ValueError
    template_name = 'cookiecutter-pypackage'
    replay_dir = 'replay'
    context = {}
    try:
        load(replay_dir, template_name, context)
        assert False
    except ValueError:
        assert True
    # Test for TypeError
    template_name = 0
    try:
        load(replay_dir, template_name, context)
        assert False
    except TypeError:
        assert True


# Generated at 2022-06-13 18:40:55.990322
# Unit test for function load
def test_load():
	replay_dir = '../' #the path of the replay file
	template_name = 'cookiecutter.json' #the template file name
	context = load(replay_dir, template_name)
	print(context)

if __name__ == '__main__':
	test_load()

# Generated at 2022-06-13 18:41:05.176665
# Unit test for function load
def test_load():
	print("test_load started")

	# 1. Load file	
	context = load("replay", "C:\\Users\\Eilat\\documents\\license-cookiecutter")
	#print(context)

	# 2. check that file includes all the keys in context
	assert 'cookiecutter' in context
	assert 'project_slug' in context
	assert 'project_name' in context
	assert 'description' in context
	assert 'author_name' in context
	assert 'email' in context
	assert 'version' in context
	assert 'open_source_license' in context
	assert 'year' in context
	assert 'full_name' in context

	print("test_load ended")

# Generated at 2022-06-13 18:41:10.348844
# Unit test for function dump
def test_dump():
    json_content = {'cookiecutter': {'name': 'John'}}
    template_name = 'non_existing_template'
    replay_dir = './cookiecutter'
    if not make_sure_path_exists(replay_dir):
        assert False
    replay_file = get_file_name(replay_dir, template_name)
    dump(replay_dir, template_name, json_content)
    assert os.path.isfile(replay_file)


# Generated at 2022-06-13 18:41:15.616979
# Unit test for function load
def test_load():
    replay_dir = 'C:\\Users\\mishe\\Desktop\\untitled1\\untitled1\\tests\\fixtures\\test-replay'
    template_name = 'test-template'
    a = load(replay_dir, template_name)
    print(a)
    pass

test_load()

# Generated at 2022-06-13 18:41:24.356204
# Unit test for function load
def test_load():
    """Unit tests for load."""
    import sys
    import json
    import ast
    import os
    import tempfile
    # from cookiecutter.utils import work_in
    from cookiecutter.replay import load

    os.chdir(os.path.expanduser('~'))
    replay_dir = os.path.join(tempfile.gettempdir(), 'cookiecutter_test')
    template_name = 'simple'
    context = {
        "full_name": "Your Name",
        "email": "your_email@example.com",
        "gh_username": "your-username",
        "cookiecutter": {
            "replay_dir": replay_dir,
            "template": template_name,
        }
    }
    # with work_in(replay_dir):

# Generated at 2022-06-13 18:41:34.282861
# Unit test for function load
def test_load():
    """ Unit test for function load """
    import os

    import cookiecutter.replay

    replay_dir = 'tests/test-data/playback'
    template_name = 'fake-repo-pre'

    context = cookiecutter.replay.load(replay_dir, template_name)

    assert context
    assert context['cookiecutter']
    assert 'repo_name' in context['cookiecutter']
    assert 'project_name' in context['cookiecutter']
    assert 'project_slug' in context['cookiecutter']
    assert 'author_name' in context['cookiecutter']
    assert 'email' in context['cookiecutter']
    assert 'description' in context['cookiecutter']
    assert 'domain_name' in context['cookiecutter']

# Generated at 2022-06-13 18:41:35.558989
# Unit test for function dump
def test_dump():
    assert dump('/home/mehdi/cookiecutter/tests/fixtures', 'my-repo', {'cookiecutter': {'foo': 'bar'}})
    assert False


# Generated at 2022-06-13 18:41:41.295846
# Unit test for function load
def test_load():
    replay_dir = "/Users/baiyunfei/Documents/workspace/code/python/cookiecutter-python/cookiecutter/replay"
    template_name = "pypackage"

    load(replay_dir, template_name)

if __name__ == '__main__':
    test_load()

# Generated at 2022-06-13 18:41:45.740140
# Unit test for function load
def test_load():
    """Test for load function."""
    import pytest
    from cookiecutter.replay import load
    from cookiecutter.exceptions import FailedHookException

    template_name = '{{cookiecutter.project_name}}'
    replay_dir = 'tests/test-load-dir'
    with pytest.raises(FailedHookException):
        load(replay_dir, template_name)

# Generated at 2022-06-13 18:41:54.730747
# Unit test for function dump
def test_dump():
    output_dir = 'tests/fake-repo-pre/'
    template_name = 'fake-repo-pre'
    context = {'cookiecutter': {
        'full_name': 'Audrey Roy',
        'email': 'audreyr@example.com',
        'github_username': 'audreyr',
        'project_name': 'Cookiecutter-Pypackage',
        'project_slug': 'cookiecutter-pypackage',
        'release_date': '2014-10-06',
    }}
    dump(output_dir, template_name, context)
    new_context = load(output_dir, template_name)
    assert context == new_context

# Generated at 2022-06-13 18:41:56.689893
# Unit test for function load
def test_load():
    context = load('/Users/yujizhou/Documents/GitHub/cookiecutter_template/replay', 'yujizhou')
    test_dict = {u'cookiecutter': {u'full_name': u'Yujie Zhou'}}
    assert context == test_dict

# Generated at 2022-06-13 18:42:06.138165
# Unit test for function load
def test_load():
    """Test function load."""

# Generated at 2022-06-13 18:42:11.786480
# Unit test for function load
def test_load():
    from cookiecutter import replay
    import os
    import json

    replay_dir = 'tests/files/replay'
    template_name = 'hello-world'
    context = replay.load(replay_dir, template_name)
    assert context['cookiecutter']['hello_world'] == 'Hello World'

# Generated at 2022-06-13 18:42:14.687107
# Unit test for function load
def test_load():
    try:
        load("./tests/test-replay", "test_replay")
    except ValueError:
        print("load replay file failure")
        assert False
    else:
        assert True

# Generated at 2022-06-13 18:42:16.929893
# Unit test for function load
def test_load():
    replay_dir = '~/workspace/cookiecutter-pypackage/replay'
    template_name = 'replay.json'
    context = load(replay_dir, template_name)
    print(context)


# Generated at 2022-06-13 18:42:19.195744
# Unit test for function load
def test_load():
    template_name = "backend_project"
    replay_dir = os.getcwd() + "/cookiecutter-django-app/tests/fixtures/replay"
    context = load(replay_dir, template_name)
    print(context)

# Generated at 2022-06-13 18:42:24.581206
# Unit test for function load
def test_load():
    """ Unit test function load"""
    try:
        load(None, "test_name")
        assert False
    except TypeError:
        assert True

    try:
        load("test_dir", 2)
        assert False
    except TypeError:
        assert True
    try:
        load("test_dir", "test_name")
        assert False
    except ValueError:
        assert True



# Generated at 2022-06-13 18:42:28.639330
# Unit test for function load
def test_load():
    from cookiecutter.main import cookiecutter
    test_dir = os.path.join(os.path.dirname(__file__), 'test_dir')
    replay_dir = os.path.join(test_dir, 'replay')
    template_name = 'cookiecutter-pypackage'
    replay_file = get_file_name(replay_dir, template_name)

    with open(replay_file, 'r') as infile:
        context = json.load(infile)

    if 'cookiecutter' not in context:
        raise ValueError('Context is required to contain a cookiecutter key')

    assert context['cookiecutter'] == template_name

# Generated at 2022-06-13 18:42:36.568701
# Unit test for function dump
def test_dump():
    context = {
      "project_name": "Test",
      "version": "1.0.0",
      "author": "Cookiecutter",
      "description": "Cookiecutter test",
      "cookiecutter": {
        "replay_dir": "some_dir",
        "no_input": True
      }
    }
    context['cookiecutter']['replay_dir'] = os.path.join(os.getcwd(), 'cookiecutters')
    template_name = 'Cookiecutter-a-demo'
    replay_dir = 'cookiecutters'
    dump(replay_dir, template_name, context)
    result = os.path.exists(get_file_name(replay_dir, template_name))
    assert result


# Generated at 2022-06-13 18:42:37.107986
# Unit test for function load
def test_load():
    assert load(None, None) == ValueError

# Generated at 2022-06-13 18:42:41.082029
# Unit test for function load
def test_load():
    src_dir = os.path.dirname(os.path.abspath(__file__))
    replay_dir = os.path.join(src_dir, 'test_replay')
    template_name = 'test_template'
    replay_file = get_file_name(replay_dir, template_name)
    cookiecutter_dict = {"cookiecutter": {"replay_dir": replay_dir, "no_input": True}}
    cookiecutter_json = json.dumps(cookiecutter_dict)
    with open(replay_file, 'w') as outfile:
        outfile.write(cookiecutter_json)
    test_context = load(replay_dir, template_name)
    assert test_context == cookiecutter_dict
    os.remove(replay_file)



# Generated at 2022-06-13 18:42:53.545183
# Unit test for function dump
def test_dump():
    replay_dir = "/Users/linda/projects/linda-github/cookiecutter/test_replay_dir/"
    template_name = "test_template"

# Generated at 2022-06-13 18:43:01.903563
# Unit test for function load
def test_load():
    context = {
        "app_name": "Django REST Framework Boilerplate",
        "app_slug": "drf-boilerplate",
        "author": "Mary Jane",
        "author_email": "mary.jane@example.com",
        "cookiecutter": {
            "full_name": "Mary Jane",
            "email": "mary.jane@example.com",
            "github_username": None,
        },
        "description": "Django REST Framework Boilerplate",
        "package_name": "drf_boilerplate",
        "python_version": "3.7",
    }
    replay_dir = 'tests/test-output/replay'
    template_name = 'peterbekos/django-rest-framework-boilerplate'
    replay_file_

# Generated at 2022-06-13 18:43:09.324192
# Unit test for function dump
def test_dump():
    context = {
        'cookiecutter': {
            'full_name': 'Templeton Peck',
            'email': 'templeton.peck@a-team.com',
            'github_username': 'faceman',
        },
    }

    template_name = 'cookiecutter-pypackage'
    replay_dir = 'tests/test-replay'
    dump(replay_dir, template_name, context)
    new_context = load(replay_dir, template_name)
    assert context == new_context


if __name__ == '__main__':
    test_dump()

# Generated at 2022-06-13 18:43:17.848685
# Unit test for function dump
def test_dump():
    """Unit test for function dump."""
    context = dict()
    context["cookiecutter"] = dict()
    context["cookiecutter"]["name"] = "{{cookiecutter.project_name}}"

    replay_dir = "tests/test-replay"
    template_name = "cookiecutter-pypackage"
    dump(replay_dir, template_name, context)

    loaded_context = load(replay_dir, template_name)

    for key in loaded_context["cookiecutter"].keys():
        assert loaded_context["cookiecutter"][key] == context["cookiecutter"][key]

# Generated at 2022-06-13 18:43:19.322165
# Unit test for function load
def test_load():
    context = load('replays', 'a')
    print(context)


# Generated at 2022-06-13 18:43:23.962182
# Unit test for function load
def test_load():
    json_path = '~/.cookiecutter_replay/replays'
    with open(json_path,'w') as json_file:
        json.dump({"fruit":"apple","size":"large"},json_file)
    ans = load(json_path,"replays")
    print(ans)
    assert ans == {"fruit":"apple","size":"large"}



# Generated at 2022-06-13 18:43:31.045352
# Unit test for function dump
def test_dump():
    """Tests the dump function."""
    os.system("rm -rf tmp")
    os.system("mkdir tmp")
    replay_dir = "tmp"
    template_name = "template"
    context = { 'context': 'value' }
    dump(replay_dir, template_name, context)
    context2 = load(replay_dir, template_name)
    # Assert subset equivalency
    assert(set(context.keys()).issubset(context2.keys()))
    assert(set(context.values()).issubset(context2.values()))
    os.system("rm -rf tmp")

if __name__ == '__main__':
    test_dump()

# Generated at 2022-06-13 18:43:34.983076
# Unit test for function load
def test_load():
    a = load('replay', 'https://github.com/DennisMitchell/cookiecutter-pypackage-minimal.git')
    print(a)
    assert False

if __name__ == '__main__':
    test_load()

# Generated at 2022-06-13 18:43:35.728639
# Unit test for function dump
def test_dump():
    assert 0

# Generated at 2022-06-13 18:43:42.473608
# Unit test for function load
def test_load():
    #Test to get context in the file of the template
    try:
        load('../cookiecutter-pypackage', 'cookiecutter-pypackage')
    except:
        assert False

    #Test to get an exception, because file does not exist
    try:
        load('../cookiecutter-pypackage', 'unknown')
        assert False
    except:
        assert True


# Generated at 2022-06-13 18:43:43.955356
# Unit test for function load
def test_load():
    """Unit test for function load."""
    context = load("../tests", "cookiecutter.json")
    assert context.get("project_name") == "Test project name"

# Generated at 2022-06-13 18:43:50.717760
# Unit test for function load
def test_load():
    if __name__ == "__main__":
        context = load(os.path.join(os.getcwd(), "replay"), "cookiecutter-pypackage")
        print(context)

# Generated at 2022-06-13 18:43:58.058351
# Unit test for function load
def test_load():
    print('Testing the load function...')
    replay_dir = 'tests/test-output'
    template_name = 'cookiecutter-pypackage'
    context = load(replay_dir, template_name)

    # Test context
    assert isinstance(context, dict)
    assert 'cookiecutter' in context
    # Test cookiecutter
    assert isinstance(context['cookiecutter'], dict)
    assert 'full_name' in context['cookiecutter']
    assert isinstance(context['cookiecutter']['full_name'], str)
    assert len(context['cookiecutter']['full_name']) > 0
    print('Test passed!')
    print('Load context: {}'.format(context))


# Generated at 2022-06-13 18:44:00.490627
# Unit test for function load
def test_load():

    assert isinstance(load('.', '{{ cookiecutter.repo_name }}'), dict)



# Generated at 2022-06-13 18:44:02.383232
# Unit test for function load
def test_load():
    context = load('.', '{{cookiecutter.project_name}}')
    assert isinstance(context, dict)



# Generated at 2022-06-13 18:44:04.645059
# Unit test for function load
def test_load():
    try:
        context = load("replay","test")
        assert context != None
    except ValueError:
        pass


# Generated at 2022-06-13 18:44:05.718900
# Unit test for function load
def test_load():
    assert isinstance(load('tests/files', 'dummy'), dict)



# Generated at 2022-06-13 18:44:07.904279
# Unit test for function load
def test_load():
    context = load('.', 'replay-file')
    print(context)

if __name__ == "__main__":
    test_load()

# Generated at 2022-06-13 18:44:10.598900
# Unit test for function dump
def test_dump():
    tempdir = os.path.join(os.path.dirname(__file__), 'test_inputs')
    dump(tempdir, 'paper', {'cookiecutter': {'project_name': 'Cookiecutter'}})


# Generated at 2022-06-13 18:44:12.751605
# Unit test for function load
def test_load():
    test_context = load('./tests/test-data', 'test-replay')
    assert (test_context == {'cookiecutter': {'test_key': 'test_value'}})


# Generated at 2022-06-13 18:44:14.112334
# Unit test for function load
def test_load():
    load('/Users/minquan/.cookiecutters', 'cookiecutter-pypackage')


# Generated at 2022-06-13 18:44:22.953273
# Unit test for function load
def test_load():
    template_name = 'my_template'
    replay_dir = 'replays'
    context = load(replay_dir, template_name)
    assert isinstance(context, dict) and 'cookiecutter' in context
    assert 'close_on_finish' in context['cookiecutter']


# Generated at 2022-06-13 18:44:27.805286
# Unit test for function load
def test_load():
    # given
    replay_dir = 'tests/files/replay'
    template_name = 'tests/files/template'
    # when
    context = load(replay_dir, template_name)
    # then
    assert context.get('cookiecutter') is not None
    assert context.get('cookiecutter').get('name') is not None


# Generated at 2022-06-13 18:44:34.471995
# Unit test for function load
def test_load():
    """Test the load function."""
    # pylint: disable=too-many-statements
    context = load('tests/test-replay',
                   'tests/fake-repo-pre/{{cookiecutter.repo_name}}')
    #print context
    assert context['cookiecutter']['repo_name'] == 'foobar'
    assert context['cookiecutter']['project_name'] == 'Foobar'
    assert context['cookiecutter']['project_slug'] == 'foobar'
    assert context['cookiecutter']['project_short_description'] == 'A short description of the project.'
    assert context['cookiecutter']['author_name'] == 'Your Name'
    assert context['cookiecutter']['author_email'] == 'me@example.com'

# Generated at 2022-06-13 18:44:43.037132
# Unit test for function load
def test_load():
    print("Testing load...")

    # Test empty template name
    try:
        replay_dir = 'replay'
        template_name = ''
        context = load(replay_dir, template_name)
        print("Fail: Did not raise expected TypeError")
    except TypeError as e:
        print("Pass: Raised TypeError")
    except Exception as e:
        print("Fail: Did not raise TypeError")
        print("Raised", type(e), ":", e)

    # Test pypi repo
    try:
        template_name = 'pypi'
        context = load(replay_dir, template_name)
        print("Pass")
        for key in context:
            print(key, ":", context[key])
    except Exception as e:
        print("Fail")

# Generated at 2022-06-13 18:44:48.441361
# Unit test for function load
def test_load():
    """Unit test for function load."""
    context = {
        'a': 'b'
    }
    template_name = 'abc'
    replay_dir = 'replays'
    # Write context to the file
    dump(replay_dir, template_name, context)
    # Read context from file
    context_loaded = load(replay_dir, template_name)
    # Compare values
    assert context_loaded == context

# Generated at 2022-06-13 18:44:54.343678
# Unit test for function load
def test_load():
    """Test the load function."""
    context = load("./test/test_replay_dir/","test_project")

# Generated at 2022-06-13 18:44:56.771804
# Unit test for function dump
def test_dump():
    """Unit test for function dump."""
    context = {
        'cookiecutter':{
            'repo_dir': 'django',
            'project_name': 'example_project',
        },
        'full_name': 'Peter O'
    }
    template_name = 'django'
    replay_dir = '{{ cookiecutter.repo_dir }}'
    dump(replay_dir, template_name,context)



# Generated at 2022-06-13 18:44:58.288606
# Unit test for function load
def test_load():
    ctx = load('replay', 'cookiecutter-template')
    assert 'cookiecutter' in ctx
    assert isinstance(ctx, dict)



# Generated at 2022-06-13 18:45:03.748072
# Unit test for function load
def test_load():
    replay_dir = "test_dir"
    template_name = "test_load"
    context = {}
    context["cookiecutter"] = {}
    context["cookiecutter"]["full_name"] = "test_name"

    dump(replay_dir, template_name, context)
    context = load(replay_dir, template_name)
    assert context["cookiecutter"]["full_name"] == "test_name"


# Generated at 2022-06-13 18:45:12.977551
# Unit test for function load
def test_load():
    context = load('./', 'cookiecutter.json')

# Generated at 2022-06-13 18:45:31.300109
# Unit test for function dump
def test_dump():
    replay_file = 'cookiecutter'
    template_name = 'my_project'
    context = {'how_many_green': 8}
    dump(replay_file, template_name, context)
    assert os.path.isfile(os.path.join(replay_file,'my_project.json')) == True
    os.remove(os.path.join(replay_file,'my_project.json'))
    assert os.path.isfile(os.path.join(replay_file,'my_project.json')) == False


# Generated at 2022-06-13 18:45:32.895447
# Unit test for function load
def test_load():
    assert load('/home/cxs106/Desktop/cookiecutter_temp', 'cookiecutter.json') != None

# Generated at 2022-06-13 18:45:33.706482
# Unit test for function dump
def test_dump():
    pass


# Generated at 2022-06-13 18:45:37.379217
# Unit test for function load
def test_load():
    template_name = 'test'
    replay_dir = '.'
    context = 'x'

    assert(context == load(replay_dir, template_name))
    assert(context != load(replay_dir, 'y'))



# Generated at 2022-06-13 18:45:43.099317
# Unit test for function load
def test_load():
  context1=load('/home/till/python/cookiecutter_project/', 'cookiecutter.json')
  context2=load('/home/till/python/cookiecutter_project/', 'cookiecutter2.json')

# Generated at 2022-06-13 18:45:48.582845
# Unit test for function dump
def test_dump():
    """Test dump function."""
    import os

    context = {'foo': 'bar'}
    template_name = 'foo'
    replay_dir = './tests/replay'
    replay_file = get_file_name(replay_dir, template_name)

    dump(replay_dir, template_name, context)

    assert os.path.exists(replay_file)

    context_reloaded = load(replay_dir, template_name)

    assert context_reloaded == context



# Generated at 2022-06-13 18:45:54.151745
# Unit test for function load
def test_load():
    from cookiecutter import main
    replay_dir = 'tests/test-replay'
    template_name = 'foobar'
    context = main.generate_context({'replay': replay_dir, 'template': template_name})
    # dump context to file
    dump(replay_dir, template_name, context)
    # load context from file
    context2 = load(replay_dir, template_name)
    # compare context and context2
    assert context == context2
    print('test load passed.')


# Generated at 2022-06-13 18:46:01.543170
# Unit test for function dump

# Generated at 2022-06-13 18:46:03.753953
# Unit test for function load
def test_load():
    assert load("{}/{}".format(os.getcwd(), 'qe_cookiecutter'), "example_replay1.json")["cookiecutter"]["portal_name"] == "portal"


# Generated at 2022-06-13 18:46:06.859438
# Unit test for function dump
def test_dump():
    replay_dir = 'test_test'
    template_name = 'test_test'
    context = {'cookiecutter': {'hello': 'world'}}
    dump(replay_dir, template_name, context)


# Generated at 2022-06-13 18:46:38.544658
# Unit test for function load
def test_load():
    dir_name = "replay/nested/folder"
    make_sure_path_exists(dir_name)
    file_name = get_file_name(dir_name, "template")
    file_content = {"cookiecutter": {"foobar": "baz", "ab": "cd"}, "foobar": "bar"}

    with open(file_name, 'w') as outfile:
        json.dump(file_content, outfile, indent=2)

    file_content = load(dir_name, "template")
    assert file_content == {"cookiecutter": {"foobar": "baz", "ab": "cd"}}



# Generated at 2022-06-13 18:46:39.784982
# Unit test for function dump
def test_dump():
    # Test for invalid replay dir

    # Test for invalid type for template name
    pass


# Generated at 2022-06-13 18:46:42.368059
# Unit test for function load
def test_load():
    replay_dir = '../tests/replay/replay_dir'
    template_name = '../tests/replay/replay_dir/example_replay.json'
    context = load(replay_dir, template_name)
    print(context)


# Generated at 2022-06-13 18:46:46.471077
# Unit test for function load
def test_load():
    """Test for load function."""
    path = './tests/test-replay/tests/test-template/'
    template_name = 'test-template'
    res = load(path, template_name)
    print(res)

if __name__ == '__main__':
    test_load()

# Generated at 2022-06-13 18:46:56.320052
# Unit test for function dump
def test_dump():
    # Write to a file named example.json
    template_name = 'example'
    # Change the work directory to the directory of this python file
    replay_dir = os.path.dirname(os.path.realpath(__file__))
    if not make_sure_path_exists(replay_dir):
        raise IOError('Unable to create replay dir at {}'.format(replay_dir))
    # Write data to the file
    context = {
        'cookiecutter': {'name': 'John', 'surname': 'Doe'}
    }
    dump(replay_dir, template_name, context)
    # Read data from the file
    assert list(load(replay_dir, template_name).keys()) == list(context.keys())
    # Delete the file
    replay_file = get_

# Generated at 2022-06-13 18:47:02.663059
# Unit test for function dump
def test_dump():
    template_name = 'cookiecutter-pypackage'
    context = {
        'cookiecutter': {
            'project_name': 'cookiecutter-pypackage',
            'full_name': 'Audrey Roy Greenfeld',
            'email': 'audreyr@example.com',
            'project_slug': 'cookiecutter-pypackage',
            'repo_name': 'cookiecutter-pypackage',
            'year': '2013',
            'description': "A Python package project template",
        }
    }
    replay_dir = 'tests/test-replay'
    dump(replay_dir, template_name, context)


# Generated at 2022-06-13 18:47:07.568841
# Unit test for function dump
def test_dump():
    replay_dir = '~/.cookiecutters/'
    template_name = 'templates'
    context = {'cookiecutter': {'test': 'test', 'test2': 'test3'}}
    dump(replay_dir, template_name, context)


# Generated at 2022-06-13 18:47:22.336545
# Unit test for function load
def test_load():
    # Load from an actual existing path
    import os
    import os.path

    p = os.path.abspath('../')
    assert (load(p, 'test') is not None)
    assert (load(p, 'testing') is not None)

    # Check the integrity of the data
    assert (load(p, 'test')['cookiecutter']['replay_dir'] == 'true')
    assert (load(p, 'test')['cookiecutter']['replay_file'] == 'test.json')
    assert (load(p, 'test')['cookiecutter']['template'] == 'test')

    # Check the integrity of the data
    assert (load(p, 'testing')['cookiecutter']['replay_dir'] == 'true')

# Generated at 2022-06-13 18:47:33.800505
# Unit test for function load
def test_load():
    from cookiecutter import main
    import os
    import shutil
    here = os.path.dirname(os.path.abspath(__file__))
    replay_dir = os.path.join(here, 'cookiecutter_replay')
    template_name = 'replay_test01'
    context = main.cookiecutter(
        template=os.path.join(here, 'tests/files/replay_test01'),
        output_dir=replay_dir,
        overwrite_if_exists=True,
        no_input=True
    )
    dump(replay_dir, template_name, context)
    dict_loaded = load(replay_dir, template_name)
    assert dict_loaded == context

# Generated at 2022-06-13 18:47:36.639289
# Unit test for function load
def test_load():
    replay_dir = '.cookiecutters'
    template_name = 'cookiecutter-pypackage'
    context = load(replay_dir, template_name)
    print(context)