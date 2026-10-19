

# Generated at 2022-06-13 18:38:29.322986
# Unit test for function load
def test_load():
    replay_dir = os.path.join('/home/vld/daven/Semestr_4/MD/PyCharmProjects/MD-lab4/cookiecutter-pypackage', 'replay')
    template_name = os.path.join(replay_dir, 'default.json')
    context = load(replay_dir, template_name)
    print(context)
    f = open('newfile.txt', 'w')
    f.write(str(context))
    f.close()



# Generated at 2022-06-13 18:38:32.988681
# Unit test for function get_file_name
def test_get_file_name():
    replay_dir = './data/replay'
    file_name = 'template_name.json'
    assert get_file_name(replay_dir, file_name) == './data/replay/template_name.json'
    file_name = 'template_name'
    assert get_file_name(replay_dir, file_name) == './data/replay/template_name.json'
    file_name = 'template_name.html'
    assert get_file_name(replay_dir, file_name) == './data/replay/template_name.html.json'


# Generated at 2022-06-13 18:38:41.630950
# Unit test for function dump
def test_dump():
    """Unit test for function dump."""
    import shutil
    import tempfile
    template_name = 'foobar'
    replay_dir = tempfile.mkdtemp()
    context = {'a': 1, 'b': 2, 'c': 3, 'cookiecutter': {'foo': 'bar'}}
    dump(replay_dir, template_name, context)
    replay_file = get_file_name(replay_dir, template_name)
    assert os.path.isfile(replay_file)
    shutil.rmtree(replay_dir)


# Generated at 2022-06-13 18:38:47.969266
# Unit test for function load
def test_load():
    temp_dir = os.path.abspath(os.path.join(os.getcwd(), '..', 'tests', 'files', 'test-load'))
    replay_dir = os.path.abspath(os.path.join(temp_dir, '..', 'replay'))
    template_name = 'dump_test'
    context = load(replay_dir, template_name)
    print(context)
    assert isinstance(context, dict)
    assert 'cookiecutter' in context


# Generated at 2022-06-13 18:38:57.046627
# Unit test for function dump
def test_dump():

    replay_dir = './tests/files/replay/'
    template_name = 'dummy_replay_file'
    context = {
        'cookiecutter': {
            '_template': 'dummy_replay_file'
        },
        'test_value': 'This is a sample test value'
    }
    dump(replay_dir, template_name, context)
    context = load(replay_dir, template_name)
    assert context['test_value'] == 'This is a sample test value'


# Generated at 2022-06-13 18:39:07.011404
# Unit test for function load
def test_load():
    from cookiecutter import replay
    from cookiecutter.exceptions import FailedHookException
    from cookiecutter.main import cookiecutter

    replay.load('tests/test-output/', 'test-template')

    t = cookiecutter('tests/test-output/test-template/', replay_dir='tests/test-output/', no_input=True)
    assert t == {
        'answer': '42',
        'cookiecutter': {
            '_template': 'tests/test-output/test-template',
            'abc': '2',
            'eggs': 'spam',
            'foo': '1',
            'project_name': 'Bacon',
            'upper_case_color': 'Green'
        },
        'replay': True
    }

# Generated at 2022-06-13 18:39:12.517619
# Unit test for function load
def test_load():
    test_template_name = '{{cookiecutter.repo_name}}'
    test_replay_dir = 'tests/test-load-replay-data/'
    test_context = {
        'cookiecutter': {
            'repo_name': 'hello-world',
        }
    }
    with open('tests/test-load-replay-data/hello-world.json', 'w') as outfile:
        json.dump(test_context, outfile, indent=2)
    context = load(test_replay_dir, test_template_name)
    assert context == test_context

# Generated at 2022-06-13 18:39:16.483973
# Unit test for function dump
def test_dump():
    cookie = {'cookiecutter': {'name': 'keke'}}
    dump('/tmp', 'test', cookie)

    assert load('/tmp', 'test') == cookie

    os.remove(get_file_name('/tmp', 'test'))


# Generated at 2022-06-13 18:39:21.915711
# Unit test for function load
def test_load():
    """Testing load function."""
    replay_dir = '/Users/apple/Cookiecutter-Test/cookiecutter-pypackage/unit_test_replay_dir'
    template_name = 'cookiecutter-pypackage'
    context = load(replay_dir, template_name)
    assert isinstance(context, dict)
    assert 'cookiecutter' in context.values()


# Generated at 2022-06-13 18:39:30.189188
# Unit test for function load

# Generated at 2022-06-13 18:39:40.320392
# Unit test for function load
def test_load():
    context1 = load('/Users/ruiguo/Documents/GitHub/headfirst-cookiecutter/tests/files', 'cookiecutter.json')
    # print(context1)
    assert context1['cookiecutter'] == {'author': 'Ruiguo', 'full_name': 'Ruiguo Wang'}
    context2 = load('/Users/ruiguo/Documents/GitHub/headfirst-cookiecutter/tests/files', 'wrong_cookiecutter.json')
    # print(context1)
    assert context2['cookiecutter'] == {'author': 'Ruiguo', 'full_name': 'Ruiguo Wang'}
    context3 = load('/Users/ruiguo/Documents/GitHub/headfirst-cookiecutter/tests/files', 'throws_error.json')

#

# Generated at 2022-06-13 18:39:50.413693
# Unit test for function load
def test_load():
    template_name = "cookiecutter-pypackage-minimal"
    replay_file = get_file_name("/Users/mooziisaac/Documents/GitHub/Cookiecutter/cookiecutter/tests", template_name)
    assert replay_file == '/Users/mooziisaac/Documents/GitHub/Cookiecutter/cookiecutter/tests/cookiecutter-pypackage-minimal.json'


# Generated at 2022-06-13 18:39:58.475007
# Unit test for function load
def test_load():
    import json
    import os
    template_name = "."
    replay_dir = "replay/templates"
    replay_file = get_file_name(replay_dir="replay/templates", template_name=template_name)
    context = load(replay_dir="replay/templates", template_name=template_name)
    assert context['cookiecutter']['full_name'] == 'Jeff Forcier'
    assert context['cookiecutter']['email'] == 'jeff@bitprophet.org'
    assert context['cookiecutter']['github_username'] == 'bitprophet'
    assert context['cookiecutter']['project_name'] == 'soa'
    assert context['cookiecutter']['project_slug'] == 'soa'

# Generated at 2022-06-13 18:40:01.461869
# Unit test for function load
def test_load():
    assert len(load('tmp', 'cookiecutter-pypackage')) == 4
    assert len(load('tmp', 'cookiecutter-pypackage.json')) == 4


# Generated at 2022-06-13 18:40:10.428249
# Unit test for function load
def test_load():
    replay_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fixtures/replay')
    template_name = 'cookiecutter-pypackage'
    context = load(replay_dir, template_name)

# Generated at 2022-06-13 18:40:20.250380
# Unit test for function load
def test_load():
    template_name='test'
    replay_dir='./replay/'
    #context={'cookiecutter':{'Poject_name':'test','Poject_desc':'test','Poject_type':'test','Poject_release':'test','Poject_version':'test','Poject_name_short':'test','Poject_desc_short':'test','Poject_version_short':'test','Poject_desc_short':'test','Poject_author':'test','Poject_email':'test','Poject_url':'test','Poject_licence':'test','Poject_copyright':'test','Poject_copyright_email':'test','Poject_copyright_url':'test','Poject_trello_url':'test','Poject_trello_board_id':'

# Generated at 2022-06-13 18:40:23.349791
# Unit test for function dump
def test_dump():
    os.chdir(os.path.dirname(__file__))
    replay_dir = "test_cookiecutter_replay"
    template_name = "test_replay_file"
    context = {"cookiecutter": {'hello': "world"}}
    dump(replay_dir, template_name, context)



# Generated at 2022-06-13 18:40:27.554215
# Unit test for function load
def test_load():
    replay_dir = '/Users/wjlee/git/cookiecutter-replay'
    template_name = 'example'
    context = load(replay_dir, template_name)
    print(context)
    assert 1==1

# Generated at 2022-06-13 18:40:38.628956
# Unit test for function load
def test_load():
	replay_dir = "test_file"
	template_name = "test_data"
	context = load(replay_dir,template_name)
	assert context == {'cookiecutter': {'project_name': 'Test Project', 'use_pypi_deployment_with_travis': 'y', 'description': 'A short description of the project.', 'author_name': 'Liam Coleman', 'email': 'ilc4940@rit.edu', 'github_username': 'lcoleman', 'domain_name': 'http://www.example.com', 'open_source_license': 'MIT license', 'pypi_username': 'lcoleman'}}


# Generated at 2022-06-13 18:40:41.059133
# Unit test for function load
def test_load():
    context = load("tests/fixtures/fake-repo-pre/", "fake_repo.json")
    print(context)

# Generated at 2022-06-13 18:40:44.520358
# Unit test for function load
def test_load():
    """Unit test for function load."""
    (load('.', 'tests/fake-repo-tmpl/{{cookiecutter.repo_name}}'))
    return


# Generated at 2022-06-13 18:40:49.406989
# Unit test for function load
def test_load():
    print('Testing load()')
    context = load(replay_dir='/Users/u6007452/Documents/cookiecutter-demo/replay',
                   template_name='cookiecutter-demo')
    assert context['cookiecutter']['year'] == '2014', 'Failed to read replay file'
    print('Passed load()')


# Generated at 2022-06-13 18:40:50.775762
# Unit test for function load
def test_load():
    print(load('replay', 'cookiecutter-demo'))


# Generated at 2022-06-13 18:40:59.143199
# Unit test for function load

# Generated at 2022-06-13 18:41:02.905937
# Unit test for function load
def test_load():
    """Function to test load function"""
    replay_dir = "tests/test-replay/simple"
    template_name = "simple.json"
    context = load(replay_dir, template_name)
    assert context["cookiecutter"]
    assert context["_template"] == "tests/fake-repo-pre/"


# Generated at 2022-06-13 18:41:04.017638
# Unit test for function load
def test_load():
    try:
        a = load('./','tests/test-repo-pre/')
    except ValueError:
        pass
    return True

# Generated at 2022-06-13 18:41:10.639991
# Unit test for function load
def test_load():
    context = load('replay', 'example-repo-name')
    assert isinstance(context, dict)
    assert context['cookiecutter']['full_name'] == \
           'Audrey Roy Greenfeld'
    assert context['cookiecutter']['email'] == \
           'audreyr@example.com'
    assert context['cookiecutter']['github_username'] == 'audreyr'
    assert context['cookiecutter']['project_name'] == \
           'Cookiecutter Example'
    assert context['cookiecutter']['project_slug'] == 'example_repo_name'
    assert context['cookiecutter']['pypi_username'] == 'audreyr'
    assert context['cookiecutter']['repo_name'] == 'example-repo-name'


# Generated at 2022-06-13 18:41:12.603639
# Unit test for function load
def test_load():
    context = load('~/.cookiecutters/', 'python-cli')
    assert(context['cookiecutter']['repo_name']=='cookiecutter-pypackage-minimal')
    assert(context['cookiecutter']['project_name']=='Python CLI')




# Generated at 2022-06-13 18:41:14.923681
# Unit test for function load
def test_load():
    replay_dir = os.path.join(os.path.dirname(__file__), '..', 'tests', 'files', 'replay')
    template_name = 'project'

# Generated at 2022-06-13 18:41:19.976900
# Unit test for function load
def test_load():
    context = load('context', 'context')
    print(context)
    assert context is not None
    assert type(context) is dict
    assert 'cookiecutter' in context
    assert 'project_name' in context['cookiecutter']
    assert context['cookiecutter']['project_name'] == '{{ cookiecutter.project_name }}'


# Generated at 2022-06-13 18:41:27.230419
# Unit test for function load
def test_load():
    replay_dir = os.path.dirname(os.path.realpath(__file__)) + "/test_replay_dir"
    template_name = "test_template"
    context = load(replay_dir, template_name)
    assert "cookiecutter" in context



# Generated at 2022-06-13 18:41:30.563195
# Unit test for function load
def test_load():
    from cookiecutter.main import cookiecutter
    replay_dir = 'replay'
    load_dir = load(replay_dir, 'https://github.com/audreyr/cookiecutter-pypackage')
    assert load_dir != None

# Generated at 2022-06-13 18:41:39.092184
# Unit test for function load
def test_load():
    template_name = "fake_template"
    replay_dir = "fake_dir"
    context = "fake_context"

    # test for when context doesn't contain 'cookiecutter' key
    with pytest.raises(ValueError):
        replay.load(replay_dir, template_name)

    # test for when context doesn't contain 'cookiecutter' key
    with pytest.raises(ValueError):
        replay.load(replay_dir, template_name)

    # test for when template name isn't a str
    with pytest.raises(TypeError):
        replay.load(replay_dir, 1)

    # test for when context isn't a dict
    with pytest.raises(TypeError):
        replay.load(replay_dir, template_name, "fake_context")

    #

# Generated at 2022-06-13 18:41:45.702290
# Unit test for function load
def test_load():
    context = load('./cookiecutter-pypackage', 'cookiecutter-pypackage')
    assert type(context) == dict
    assert 'cookiecutter' in context
    assert 'full_name' in context['cookiecutter']
    assert 'project_name' in context['cookiecutter']
    assert 'project_slug' in context['cookiecutter']
    assert 'project_short_description' in context['cookiecutter']
    assert 'version' in context['cookiecutter']
    assert 'release' in context['cookiecutter']



# Generated at 2022-06-13 18:41:53.804290
# Unit test for function dump
def test_dump():
    replay_dir = os.path.join(
        os.path.expanduser('~'),
        '.cookiecutters')
    template_name = 'cookiecutter-project-template'
    context = {
        'cookiecutter': {
            'full_name': 'Joe Smith',
            'email': 'joe@example.com',
            'project_name': 'Awesome Project',
            'project_slug': 'awesome-project',
            'repo_name': 'awesome-project'
        }
    }
    dump(replay_dir, template_name, context)


# Generated at 2022-06-13 18:41:56.865932
# Unit test for function load
def test_load():
    replay_dir = 'TEST'
    template_name = 'TEST'

    with open('TEST.json', 'r') as infile:
        context = json.load(infile)

    if 'cookiecutter' not in context:
        raise ValueError('Context is required to contain a cookiecutter key')



# Generated at 2022-06-13 18:42:00.654794
# Unit test for function load
def test_load():
    assert load(os.getcwd(), "") == {'replay': True}
    # assert load(os.getcwd(), "Test") == {'replay': True}
    # assert load(os.getcwd(),"Test") == {'replay': True}

# Generated at 2022-06-13 18:42:10.135202
# Unit test for function load
def test_load():
    """Unit test function load."""
    # pylint: disable=too-many-branches,too-many-statements
    # pylint: disable=import-error
    import pytest
    from cookiecutter.operations import load as cc_load

    # set up some variables to use during the test
    replay_dir = 'tests/test-replay'
    template_name = 'cookiecutter-pypackage'
    context = {'cookiecutter': {}}

    # make sure that the test-replay directory exists
    if os.path.exists(replay_dir):
        os.removedirs(replay_dir)

    # test for the case where the replay file does not exist
    with pytest.raises(IOError):
        load(replay_dir, template_name)

    #

# Generated at 2022-06-13 18:42:12.567047
# Unit test for function load
def test_load():
    json_data = load('replay', 'cookiecutter-pypackage-minimal')
    assert isinstance(json_data, dict)
    assert isinstance(json_data['cookiecutter'], dict)


# Generated at 2022-06-13 18:42:15.807031
# Unit test for function load
def test_load():
    import pprint
    file_path = "D:/TEMP/cookiecutter-pypackage-minimal/" + "replay/"+"replay.json"
    context = load(file_path, file_path)
    pprint.pprint(context)


# Generated at 2022-06-13 18:42:25.068061
# Unit test for function load
def test_load():
    replay_dir = '.'
    template_name = '.'
    test_context = {'cookiecutter': {'project_name': 'tmp', 'repo_name': 'tmp'}}
    dump(replay_dir, template_name, test_context)
    replay_context = load(replay_dir, template_name)
    assert test_context == replay_context
    os.remove(get_file_name(replay_dir, template_name))



# Generated at 2022-06-13 18:42:32.977762
# Unit test for function dump
def test_dump():
    replay_dir = '.cookiecutters'
    template_name = 'cookiecutter-pypackage'

# Generated at 2022-06-13 18:42:41.363774
# Unit test for function load
def test_load():
    import pytest
    replay_dir = '/home/test_cookiecutter/replay/'
    template_name = 'my_template'

# Generated at 2022-06-13 18:42:45.559372
# Unit test for function load
def test_load():
    context = load('C:\\Users\\Bingchao Wang\\GitHub\\cookiecutter-Pytorch-GAN', 'cookiecutter-Pytorch-GAN')
    print(context)


# Generated at 2022-06-13 18:42:47.066663
# Unit test for function load
def test_load():
    """Unit test for load."""
    assert True


# Generated at 2022-06-13 18:42:58.475318
# Unit test for function dump
def test_dump():
    """Unit test for function dump."""
    # Record the current directory
    pwd = os.getcwd()

    # Change to the folder tests/test-data, which contains the test data
    os.chdir('tests/test-data')

    # Set the directory to which the replay data will be dumped
    replay_dir = os.path.abspath('simple/simple')
    print("Directory:", os.listdir(replay_dir))

    # Set the template name
    template_name = 'simple'

    # Set the replay data
    context = {
        'cookiecutter': {
            'full_name': 'Elmo Muppet',
            'email': 'elmo@sesamestreet.org'
        }
    }

    dump(replay_dir, template_name, context)

    # Get the file

# Generated at 2022-06-13 18:43:08.704114
# Unit test for function dump
def test_dump():
    """Unit test for function dump."""
    # Check raise TypeError if template_name is not string
    try:
        dump("", 100, {"a": "A"})
    except TypeError:
        print("TypeError raised")
    else:
        raise AssertionError('ExpectedTypeError')

    # Check raise TypeError if context is not dict
    try:
        dump("", "", "A")
    except TypeError:
        print("TypeError raised")
    else:
        raise AssertionError('ExpectedTypeError')

    # Check raise ValueError if context does not contain cookiecutter value
    try:
        dump("", "", {"a": "A"})
    except ValueError:
        print("ValueError raised")
    else:
        raise AssertionError('ExpectedValueError')

    # Check raise

# Generated at 2022-06-13 18:43:11.373577
# Unit test for function load
def test_load():
    assert(load('cookiecutter', 'cookiecutter') == {'cookiecutter': {}})

if __name__ == '__main__':
    test_load()

# Generated at 2022-06-13 18:43:15.907597
# Unit test for function load
def test_load():
    template_name = 'tutorial-cookiecutter-pypackage'
    replay_dir = os.path.join(os.path.expanduser('~'),'cookiecutter','replay')
    context = load(replay_dir, template_name)
    assert 'cookiecutter' in context


# Generated at 2022-06-13 18:43:21.694113
# Unit test for function load
def test_load():

    from os.path import dirname, realpath

    replay_dir = os.path.join(dirname(dirname(dirname(dirname(realpath(__file__))))), 'tests', 'replay')
    template_name = "test"

    template_name = str(template_name)

    context = load(replay_dir, template_name)


# Generated at 2022-06-13 18:43:28.597658
# Unit test for function load
def test_load():
    replay_file = "tests/test-replay/0.0.1/cookiecutter.json"
    assert os.path.exists(replay_file)

    with open(replay_file, 'r') as infile:
        context = json.load(infile)

    assert 'cookiecutter' in context


test_load()

# Generated at 2022-06-13 18:43:37.076931
# Unit test for function load
def test_load():
    # Test a normal case
    template_name = "test_template"
    replay_file = get_file_name('.', template_name)
    context = {'cookiecutter': {'full_name': 'firstName lastName', 'email': 'email@example.com'}}
    with open(replay_file, 'w') as outfile:
        json.dump(context, outfile, indent=2)

    loaded_context = load('.', template_name)

    assert (loaded_context == context)


# Generated at 2022-06-13 18:43:43.343772
# Unit test for function load
def test_load():
	context = { "cookiecutter": 'my_awesome_app' }
	replay_dir = 'test_replay'
	template_name = '/test_replay_templ.json'
	dump(replay_dir, template_name, context)
	print(load(replay_dir, template_name))
	# assert load(replay_dir, template_name) == context

if __name__ == '__main__':
	test_load()

# Generated at 2022-06-13 18:43:46.383712
# Unit test for function load
def test_load():
    """Test load function."""
    load(r'C:\Users\Administrator\AppData\Local\Programs\Python\Python35\Lib\site-packages\cookiecutter\replay',
    'cookiecutter-pypackage')

if __name__ == '__main__':
    test_load()

# Generated at 2022-06-13 18:43:53.409191
# Unit test for function dump
def test_dump():
    """Unit test for function dump."""
    from cookiecutter import utils

    context = {'cookiecutter': {'full_name': 'bobby'}}
    utils.ensure_dir('./tests/test-dump')
    dump('./tests/test-dump', 'test', context)
    loaded_context = load('./tests/test-dump', 'test')
    assert loaded_context == context



# Generated at 2022-06-13 18:43:59.485632
# Unit test for function load
def test_load():
    test_context = load('tests/test-output/project_replay', "test_template")

# Generated at 2022-06-13 18:44:09.201619
# Unit test for function dump
def test_dump():
    replay_dir = os.path.expanduser('~/.cookiecutters/')
    template_name = 'python_package'
    context = {}
    context['cookiecutter'] = {'_template': 'https://github.com/audreyr/cookiecutter-pypackage'}
    context['cookiecutter']['project_name'] = 'hello'
    context['cookiecutter']['author_name'] = 'Audrey'
    context['cookiecutter']['version'] = '0.1.0'
    context['cookiecutter']['package_name'] = 'hello'
    context['cookiecutter']['repo_name'] = 'hello'
    context['cookiecutter']['description'] = 'A minimal Python package'

# Generated at 2022-06-13 18:44:13.481319
# Unit test for function load
def test_load():
    """Unit test for the load function.
    """
    replay_dir = 'tests/fake-repo-pre/'
    template_name = 'fake-repo-pre'
    context = {
        'cookiecutter': {
            'key1': 'value1'
        }
    }
    dump(replay_dir, template_name, context)
    assert load(replay_dir, template_name) == context


# Generated at 2022-06-13 18:44:18.188933
# Unit test for function load
def test_load():
    replay_dir = '/home/cw/cookiecutter-pypackage-min/tests'
    template_name = 'cookiecutter.json'
    context = load(replay_dir, template_name)
# print(context) --> {'cookiecutter': {'project_name': 'cookiecutter-pypackage-min', 'author_name': 'Cindy Wang', 'description': 'A lightweight Python package', 'version': '0.1.0', 'use_pytest': True, 'open_source_license': 'MIT license'}}


# Generated at 2022-06-13 18:44:22.844824
# Unit test for function load
def test_load():
    test_path = os.path.dirname(os.path.abspath(__file__))
    replay_dir = os.path.join(test_path, 'tests/replay')
    context = load(replay_dir, '{{cookiecutter.repo_name}}')
    assert context['cookiecutter']['repo_name'] == 'foobar'

# Generated at 2022-06-13 18:44:31.453156
# Unit test for function dump
def test_dump():
    context = {'cookiecutter': {'test': {'test': 'test'}}}
    dump(replay_dir='tests/test_replay', template_name='test', context=context)
    loaded = load(replay_dir='tests/test_replay', template_name='test')

    assert context == loaded

# Generated at 2022-06-13 18:44:33.918532
# Unit test for function load
def test_load():
    load(os.path.abspath('./replay/'), 'cookiecutter-pypackage')


# Generated at 2022-06-13 18:44:36.170636
# Unit test for function load
def test_load():
    load("/Users/margaretdeng/software_dev_tools/cookiecutter-pypackage", "pytest_cookiecutter")

# Generated at 2022-06-13 18:44:39.043879
# Unit test for function load
def test_load():
    context = load('../tests/test-load/', 'test-load')
    assert 'cookiecutter' in context
    assert context['cookiecutter']['name'] == 'audreyr'


# Generated at 2022-06-13 18:44:42.802229
# Unit test for function dump
def test_dump():
	replay_dir="cookiecutter/replay"
	template_name="dummy_template"
	# context= {"cookiecutter":{"_copy_without_render":["Dockerfile"]}}
	context= {"cookiecutter":{"_copy_without_render":["dummy_template"]}}
	dump(replay_dir, template_name, context)


# Generated at 2022-06-13 18:44:44.515416
# Unit test for function load
def test_load():
    context = load('/home/shikher/work/cookiecutter-shikherverma/new_cookie', 'cookiecutter')
    print(context)


# Generated at 2022-06-13 18:44:46.797288
# Unit test for function load
def test_load():
    return load('replay_tests/', 'test')



# Generated at 2022-06-13 18:44:52.262385
# Unit test for function load
def test_load():
    replay_dir = """fake_source_path\cookiecutter-{{cookiecutter.repo_name}}"""
    template_name = 'cookiecutter.json'
    print(load(replay_dir, template_name))
    
    

# Generated at 2022-06-13 18:45:04.992274
# Unit test for function load
def test_load():
    """Function construct_template_directories_and_files unit test"""
    import os
    import json
    import sys
    import pytest
    # template_dir = os.path.join(os.path.dirname(__file__), "..", "..", "tests", "fake-repo-pre"))
    test_dir = os.path.dirname(__file__)
    template_dir = os.path.join(test_dir, "..", "..", "tests", "fake-repo-pre")
    template_name = 'cookiecutter-pypackage'

# Generated at 2022-06-13 18:45:12.211056
# Unit test for function dump
def test_dump():
    """Unit test for function dump."""
    try:
        dump('/tmp/fake_replay_dir', 'fake_template', {})
        replay_file = get_file_name('/tmp/fake_replay_dir', 'fake_template')
        assert os.path.exists(replay_file), ('Replay file {} could '
                                             'not be created').format(replay_file)
    finally:
        if os.path.exists('/tmp/fake_replay_dir'):
            os.rmdir('/tmp/fake_replay_dir')


# Generated at 2022-06-13 18:45:33.564469
# Unit test for function load
def test_load():
    if __name__ == "__main__":
        # test for normal case
        context_expected = {'cookiecutter': {'project_name': 'Test repo', 'repo_name': 'repo-name'}}
        context_result = load('tests/test-replay/', 'cookiecutter-pypackage')
        if context_expected != context_result:
            raise ValueError('Load Error!')

        # test for template_name is not string
        try:
            context_result = load('tests/test-replay/', 1)
        except TypeError as e:
            print('Template name is required to be of type str')

        # test for context is not dict

# Generated at 2022-06-13 18:45:35.900034
# Unit test for function load
def test_load():
    template_name = 'cookiecutter-pypackage'
    replay_dir = '.cookiecutters'
    context = load(replay_dir, template_name)
    print(context)


# Generated at 2022-06-13 18:45:40.410390
# Unit test for function load
def test_load():

    result = load(os.path.join(os.path.abspath('.'), 'replay'), 'test.json')

    assert isinstance(result, dict) == True
    assert 'cookiecutter' in result == True

# Generated at 2022-06-13 18:45:46.319523
# Unit test for function load
def test_load():
    """Unit test for function load."""
    import os

    cwd = os.getcwd()
    packer_path = cwd + 'cookiecutter-docker-slim-db'
    os.chdir(packer_path)
    load('./replay', 'cookiecutter.json')
    os.chdir(cwd)

# Generated at 2022-06-13 18:45:55.361637
# Unit test for function dump
def test_dump():
    # Given
    replay_dir = 'tests/files/test-replay'
    template_name = 'test_template_name'
    context = {
        'cookiecutter': {
            'test_key_1': 'test_value_1',
            'test_key_2': 'test_value_2'
        }
    }

    # When
    dump(replay_dir, template_name, context)

    # Then
    replay_file = get_file_name(replay_dir, template_name)
    try:
        with open(replay_file, 'r') as infile:
            assert json.load(infile) == context
    except IOError as e:
        assert 'Unable to open replay file at' in e.message

# Generated at 2022-06-13 18:45:58.250630
# Unit test for function load
def test_load():
    """Unit test for function load."""
    context = load('tests/fixtures/replay', 'foobar')
    assert context == {'cookiecutter': {'full_name': 'John Smith', 'email': 'john@smith.com'}}



# Generated at 2022-06-13 18:46:05.541398
# Unit test for function load

# Generated at 2022-06-13 18:46:11.580671
# Unit test for function load
def test_load():
    """Test replay.load()."""
    template_name = 'test_template_name'
    context = {'cookiecutter': {'test_key': 'test_value'}}

    fname = get_file_name('tests/test-replay', template_name)
    if not make_sure_path_exists('tests/test-replay'):
        raise IOError('Unable to create replay dir at {}'.format('tests/test-replay'))

    with open(fname, 'w') as outfile:
        json.dump(context, outfile, indent=2)

    ctext = load('tests/test-replay', template_name)

    assert context == ctext



# Generated at 2022-06-13 18:46:14.989371
# Unit test for function load
def test_load():
    """Test load function."""
    replay_dir = 'test_dir'
    template_name = 'test_template'

    context = {'cookiecutter': {}}
    dump(replay_dir, template_name, context)

    context = load(replay_dir, template_name)


# Generated at 2022-06-13 18:46:17.013460
# Unit test for function load
def test_load():
    ctx = load('tests/fixtures/cookiecutters/simple', 'simple')
    assert isinstance(ctx, dict)
    assert 'cookiecutter' in ctx
    return ctx


# Generated at 2022-06-13 18:46:41.365225
# Unit test for function dump
def test_dump():
    assert 1

# Generated at 2022-06-13 18:46:44.712569
# Unit test for function dump
def test_dump():
    replay_dir = '{{ cookiecutter.project_slug }}/tests/files/replay'
    context = {'cookiecutter': {
        'project_name': 'Hellol',
        'project_slug': 'hellol',
        'author_name': 'Your name'
    }}
    template_name = 'hellol'
    dump(replay_dir, template_name, context)



# Generated at 2022-06-13 18:46:48.453845
# Unit test for function load
def test_load():
    dict1 = load('/home/zw262/csci5253-fall2018/cookiecutter-exercise/generated-files/cookiecutter-pypackage-playground', 'cookiecutter-pypackage-playground')
    dict2 = load('/home/zw262/csci5253-fall2018/cookiecutter-exercise/generated-files/cookiecutter-pypackage-playground', 'cookiecutter-pypackage-playground.json')
    assert dict1 == dict2



# Generated at 2022-06-13 18:46:52.656419
# Unit test for function load
def test_load():
    replay_dir = "/home/nikhil/.cookiecutters"
    template_name = "poc"
    context = load(replay_dir, template_name)
    print(context)
    assert context != None
    assert 'cookiecutter' in context


# Generated at 2022-06-13 18:46:54.857060
# Unit test for function load
def test_load():
    print(load('C:\\Users\\APPS\\Downloads\\Cookiecutter---Master','cookiecutter.json'))

test_load()

# Generated at 2022-06-13 18:46:58.699744
# Unit test for function load
def test_load():
    replay_dir = "C:/Users/wjdth/PycharmProjects/pattern"
    template_name = "simple"
    test_context = load(replay_dir, template_name)
    for key, value in test_context.items():
        print(key + " : " + value)


# Generated at 2022-06-13 18:47:02.150180
# Unit test for function load
def test_load():
    replay_dir = 'tests/test-replay/'
    template_name = 'test-cookiecutter-json'
    context = load(replay_dir, template_name)
    assert(context['cookiecutter']['full_name'] == 'Some Person')

# Generated at 2022-06-13 18:47:09.712053
# Unit test for function load
def test_load():
    template_name = 'DummyTemplate'
    replay_dir = 'Cookiecutter_replay'
    context = {'cookiecutter': {}}
    dump(replay_dir, template_name, context)
    loaded_context = load(replay_dir, template_name)
    assert loaded_context == context
    # Cleanup test input file
    replay_file = get_file_name(replay_dir, template_name)
    os.remove(replay_file)


# Generated at 2022-06-13 18:47:12.990869
# Unit test for function load
def test_load():
    replay_dir = '~/git/Tutoria/INSE/cookiecutter-nask'
    template_name = 'nask'
    context = load(replay_dir, template_name)
    print(context)


# Generated at 2022-06-13 18:47:16.468764
# Unit test for function load
def test_load():
    replay_dir = "/home/t13/.cookiecutters/"
    template_name = "jinja2-template"
    print(load(replay_dir, template_name))


# Generated at 2022-06-13 18:47:45.984071
# Unit test for function load
def test_load():
    """test load function
    """
    from .path import get_user_dir
    from .generate import cookiecutter
    try:
        load("/home/ubuntu/.cookiecutters", "cookiecutter-pypackage")
    except ValueError:
        pass
    replay_dir = get_user_dir()
    #template_name = "https://github.com/audreyr/cookiecutter-pypackage.git"

    #cookiecutter(template_name, replay_dir=replay_dir)
    try:
        load(replay_dir, "cookiecutter-pypackage")
    except IOError:
        pass
    except TypeError:
        pass


# Generated at 2022-06-13 18:47:57.038656
# Unit test for function dump
def test_dump():
    import random
    import string
    import datetime
    replay_dir = 'cookiecutter/tests/test-replay/replay'
    template_name = ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(10))
    context = dict()
    context['cookiecutter'] = dict()
    context['cookiecutter']['_template'] = template_name
    now = datetime.datetime.now()
    context['cookiecutter']['year'] = now.year
    context['cookiecutter']['author_name'] = 'cookiecutter'
    context['cookiecutter']['description'] = 'description'
    context['cookiecutter']['author_email'] = 'author_email'

# Generated at 2022-06-13 18:47:58.522840
# Unit test for function load
def test_load():
    context = load('tests/replay', 'tests/fake-repo-tmpl')
    assert isinstance(context, dict)
    assert 'cookiecutter' in context


# Generated at 2022-06-13 18:48:02.520798
# Unit test for function dump
def test_dump():
    replay_dir = 'hello'
    template_name = 'thisisatest'
    context = {'cookiecutter': {'test': 'pass'}}
    dump(replay_dir, template_name, context)

    with open('hello/thisisatest.json', 'r') as infile:
        data = json.load(infile)
    assert(data == context)



# Generated at 2022-06-13 18:48:15.351169
# Unit test for function dump
def test_dump():
    # Create a temporary directory to store the replay file
    from tempfile import mkdtemp
    replay_dir = mkdtemp()
    template_name = 'test_template'
    context = {'cookiecutter':{'test_variable':'test_value'}}
    # Dump context to replay file
    dump(replay_dir, template_name, context)
    # Read context from replay file
    replay_context = load(replay_dir, template_name)
    # Check if read context is same as dumped context
    assert context == replay_context
    # Cleanup temporary directory
    import shutil
    shutil.rmtree(replay_dir)

# Generated at 2022-06-13 18:48:18.642244
# Unit test for function load
def test_load():
    template_name = "collect_pull_requests"
    replay_dir = "./"
    context = load(replay_dir, template_name)
    print (context)
    print ("test_load done")

if __name__ == '__main__':
    
    test_load()

# Generated at 2022-06-13 18:48:25.050419
# Unit test for function load
def test_load():
    replay_dir = 'test_replay_dir'
    template_name = 'test_template_name'
    test_context = dict()
    test_context['cookiecutter'] = dict()

    try:
        os.mkdir(replay_dir)
    except OSError:
        print("Creation of the test_replay_dir failed")
    else:
        print("Successfully created the directory test_replay_dir")
    replay_file = get_file_name(replay_dir, template_name)

    try:
        # dump the test_context
        dump(replay_dir, template_name, test_context)
        context = load(replay_dir, template_name)
        assert context == test_context
    except:
        print('Dump and load test failed')