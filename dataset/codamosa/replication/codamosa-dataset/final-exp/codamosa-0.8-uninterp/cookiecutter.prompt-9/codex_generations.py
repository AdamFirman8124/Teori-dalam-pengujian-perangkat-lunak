

# Generated at 2022-06-22 12:24:47.011760
# Unit test for function read_user_dict
def test_read_user_dict():
    var_name = "dict1"
    default_val = {'k1':'v1'}
    user_input = '{"k1": "v1"}'
    assert read_user_dict(var_name, default_val) == json.loads(user_input, object_pairs_hook=OrderedDict)

# Generated at 2022-06-22 12:24:50.969891
# Unit test for function prompt_for_config
def test_prompt_for_config():
    from test_cookiecutter import pb_cookie, env
    context = pb_cookie.get_config()
    cookiecutter_dict = prompt_for_config(context, no_input=True)
    print (cookiecutter_dict)

#test_prompt_for_config()

# Generated at 2022-06-22 12:25:01.125877
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {'cookiecutter': {'project_name': 'Cookiecutter-Pypackage',
                                'project_slug': 'cookiecutter-pypackage',
                                'author_name': 'Audrey Roy Greenfeld',
                                'email': 'audreyr@example.com',
                                'description': 'A Python package project template.',
                                'version': '0.1.0',
                                'open_source_license': 'MIT',
                                'command_line_interface': 'No CLI'}}
    cookiecutter_dict = prompt_for_config(context)
    assert isinstance(cookiecutter_dict, dict)
    assert len(cookiecutter_dict) == 8
    assert cookiecutter_dict['project_name'] == 'Cookiecutter-Pypackage'


# Generated at 2022-06-22 12:25:09.107977
# Unit test for function process_json
def test_process_json():
    """Verify that process_json works as expected.

    """
    # Test valid JSON
    test_dict = {"key1": "value1", "key2": "value2"}
    user_value = json.dumps(test_dict)
    test_output = process_json(user_value)
    assert test_output == test_dict

    # Test invalid JSON
    user_value = '{ "key1: "value1", "key2": "value2"'
    with pytest.raises(click.UsageError):
        process_json(user_value)

# Generated at 2022-06-22 12:25:17.240746
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """
    test functions for prompt_for_config
    """
    from .config import DEFAULT_CONFIG
    from .environment import DEFAULT_CONFIG_FILE
    #default_config_path = os.path.join(DEFAULT_CONFIG, DEFAULT_CONFIG_FILE)
    default_config_path = DEFAULT_CONFIG_FILE

    with open(default_config_path, 'r') as config_file:
        context = json.loads(config_file.read(), object_pairs_hook=OrderedDict)
    print(context)
    print(context['cookiecutter'])

    cookiecutter_dict = prompt_for_config(context)
    print(cookiecutter_dict)

# Generated at 2022-06-22 12:25:28.608997
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {
        'cookiecutter': {
            'project_slug': 'My Project',
            'repo_name': 'my-repo-name',
            'select_framework': [
                'React',
                'Angular',
                'Vue.js'
            ]
        }
    }
    cookiecutter_dict = prompt_for_config(context, True)
    assert cookiecutter_dict['project_slug'] == 'My Project'
    assert cookiecutter_dict['repo_name'] == 'my-repo-name'
    assert cookiecutter_dict['select_framework'] == 'React'

if __name__ == '__main__':
    print("Testing prompt_for_config")
    test_prompt_for_config()

# Generated at 2022-06-22 12:25:34.215414
# Unit test for function read_user_dict
def test_read_user_dict():
    assert read_user_dict('woof', default_value={'a': 1}) == {'a': 1}
    assert read_user_dict('woof', default_value={}) == {}
    # Should raise click UsageError exception
    click.UsageError('Unable to decode to JSON.')
    click.UsageError('Requires JSON dict.')

# Generated at 2022-06-22 12:25:40.069084
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Test the function for prompting for config."""
    from cookiecutter.main import cookiecutter

    project_dir = cookiecutter(
        'tests/test-data/fake-repo-pre/', context_file='tests/test-data/fake-repo-pre/cookiecutter.json'
    )
    assert project_dir == 'fake-project'



# Generated at 2022-06-22 12:25:42.788281
# Unit test for function read_user_dict
def test_read_user_dict():
    key =  "django_settings_module"
    default_value = "project_name.settings.local"
    user_input = read_user_dict(key, default_value)
    print(user_input)


# Generated at 2022-06-22 12:25:54.228647
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Unit test for prompt_for_config function."""

# Generated at 2022-06-22 12:26:10.755961
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Test function prompt_for_config"""

# Generated at 2022-06-22 12:26:15.432040
# Unit test for function prompt_for_config
def test_prompt_for_config():
    import cookiecutter
    
    context = cookiecutter.prompt.prompt_for_config('.', no_input=True)
    print(context)
    assert isinstance(context, dict)
    assert context['project_name'] == 'Foo Bar'

if __name__ == '__main__':
    test_prompt_for_config()

# Generated at 2022-06-22 12:26:23.459769
# Unit test for function read_user_dict
def test_read_user_dict():
    value = read_user_dict("key", "default")
    assert value == "default"

    value = read_user_dict("key", {'a': 1, 'b': '2', 'c': 3.0})
    assert value == {'a': 1, 'b': '2', 'c': 3.0}

    value = read_user_dict("key", {'a': {'b': 1}, 'c': {'d': '2'}})
    assert value == {'a': {'b': 1}, 'c': {'d': '2'}}

    value = read_user_dict("key", {'a': [1,2,3]})
    assert value == {'a': [1,2,3]}

# Generated at 2022-06-22 12:26:33.632119
# Unit test for function read_user_dict
def test_read_user_dict():
    var_name = 'testing_variable'
    default_value = dict()

    #test if a string is passed in
    user_value = 'this is a string'
    try:
        result = read_user_dict(var_name, default_value)
    except click.UsageError as err:
        assert "Requires JSON dict" in str(err)

    #test if a list is passed in
    user_value = ['this', 'is', 'a', 'list']
    try:
        result = read_user_dict(var_name, default_value)
    except click.UsageError as err:
        assert "Requires JSON dict" in str(err)

    #test if an empty dictionary is passed in
    user_value = dict()
    result = read_user_dict(var_name, default_value)
    assert result

# Generated at 2022-06-22 12:26:43.261255
# Unit test for function read_user_dict
def test_read_user_dict():
    # Test with no input
    no_input_dict = OrderedDict([("a", 1), ("b", 2)])
    assert read_user_dict("Test", no_input_dict) == no_input_dict

    # Test with JSON input
    json_input_dict = OrderedDict([("c", 3), ("d", 4)])
    json_input_str = json.dumps(json_input_dict, separators=(',', ':'))
    assert read_user_dict("Test", no_input_dict) == json_input_dict

    # Test with invalid JSON input
    json_input_str = "Not JSON"
    try:
        read_user_dict("Test", no_input_dict)
    except click.exceptions.Abort:
        pass
    else:
        assert False

    #

# Generated at 2022-06-22 12:26:52.432415
# Unit test for function prompt_for_config
def test_prompt_for_config():
    # It should handle simple variables
    context = {
        'cookiecutter': {
            'project_name':'Awesome Project',
            'author': 'Bernardo Heynemann',
        }
    }

    config = prompt_for_config(context, no_input=True)

    assert config['project_name'] == 'Awesome Project'
    assert config['author'] == 'Bernardo Heynemann'

    # It should handle list variables
    context = {
        'cookiecutter': {
            'framework': ['django', 'flask'],
        }
    }

    config = prompt_for_config(context, no_input=True)

    assert config['framework'] == 'django'

    # It should handle dict variables

# Generated at 2022-06-22 12:27:01.974306
# Unit test for function prompt_for_config
def test_prompt_for_config():
    from cookiecutter.vcs import vcs_initialize

    project_dict = {
        'full_name': 'Audrey Roy Greenfeld',
        'email': 'audreyr@example.com',
        'github_username': 'audreyr'
    }

# Generated at 2022-06-22 12:27:11.805744
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:27:17.911715
# Unit test for function prompt_for_config
def test_prompt_for_config():
    cookiecutter_dict = OrderedDict([])
    env = StrictEnvironment(context="context")

    # First pass: Handle simple and raw variables, plus choices.
    # These must be done first because the dictionaries keys and
    # values might refer to them.
    for key, raw in context['cookiecutter'].items():
        if key.startswith('_') and not key.startswith('__'):
            cookiecutter_dict[key] = raw
            continue
        elif key.startswith('__'):
            cookiecutter_dict[key] = render_variable(env, raw, cookiecutter_dict)
            continue


# Generated at 2022-06-22 12:27:25.295320
# Unit test for function prompt_for_config
def test_prompt_for_config():
    from cookiecutter.main import cookiecutter


# Generated at 2022-06-22 12:27:41.558597
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:27:43.821107
# Unit test for function read_user_dict
def test_read_user_dict():
    user_dict = read_user_dict("Test", "foo")
    assert user_dict == "foo"


# Generated at 2022-06-22 12:27:51.864212
# Unit test for function read_user_dict
def test_read_user_dict():
    user_dict = {
        'foo': 'A foo',
        'bar': 'A bar',
        'baz': 4,
    }

    # Create a context with some data in it
    context = {
        'cookiecutter': {
            '_dict': {
                'foo': 'A foo',
                'bar': 'A bar',
                'baz': 4,
                'baz_with_default': 'baz_with_default',
            },
        },
    }

    # Read a normal dict
    assert read_user_dict('_dict', user_dict) == user_dict

    # Read a dict with a default value
    val = read_user_dict('_dict_with_default', user_dict)
    assert val == user_dict

# Generated at 2022-06-22 12:27:59.720924
# Unit test for function process_json
def test_process_json():
    correct_dict = {
        "project_name": "Hello World",
        "project_slug": "hello_world",
        "author": "AUTHOR",
    }

    correct_input = '{ "author": "AUTHOR", "project_slug": "hello_world", "project_name": "Hello World"}'
    assert process_json(correct_input) == correct_dict

    incorrect_input = "{ \"author\": 'AUTHOR', \"project_slug\": 'hello_world', \"project_name\": 'Hello World'}"
    assert process_json(incorrect_input) != correct_dict

# Generated at 2022-06-22 12:28:11.620774
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Test prompt_for_config()."""

# Generated at 2022-06-22 12:28:23.149611
# Unit test for function read_user_dict
def test_read_user_dict():
    test_key = 'test_var'
    test_val = 42
    default_value = {'test_key': test_val, 'another_key': 'Another Value'}
    test_ok = {'test_key': test_val, 'another_key': 'Another Value'}
    test_nok_1 = 42
    test_nok_2 = 'test_string'
    test_nok_3 = [test_val, 'test_string']
    test_nok_4 = (test_val, 'test_string')

    # Sanity check
    assert read_user_dict(test_key, default_value) == default_value

    with pytest.raises(TypeError):
        read_user_dict(test_key, test_nok_1)

# Generated at 2022-06-22 12:28:30.629411
# Unit test for function prompt_for_config
def test_prompt_for_config():
    def _test_prompt_for_config(context, expected):
        cookiecutter_dict = prompt_for_config(context)
        assert cookiecutter_dict == expected


# Generated at 2022-06-22 12:28:42.069940
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:28:50.674825
# Unit test for function process_json
def test_process_json():
    """Test the function process_json."""
    from_dict = {'key1': 'value1', 'key2': 'value2', 'key3': ['value3', 'value4']}
    user_value = json.dumps(from_dict, sort_keys=True, indent=4)
    d = process_json(user_value)
    assert d == {'key1': 'value1', 'key2': 'value2', 'key3': ['value3', 'value4']}



# Generated at 2022-06-22 12:28:58.002458
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Test function prompt_for_config."""
    from cookiecutter.environment import StrictEnvironment
    from cookiecutter.repository import check_vcs_for_repo, get_repo_url
    from cookiecutter.main import cookiecutter
    from cookiecutter.config import DEFAULT_CONFIG
    import pytest

    context = DEFAULT_CONFIG
    context['cookiecutter'] = [{'key': 'value'}]
    context['_test_repo'] = 'https://github.com/cookiecutter/cookiecutter.git'
    repo_dir = '/tmp/cookiecutter-test-repo'

    vcs_repo = check_vcs_for_repo(context['_test_repo'])

# Generated at 2022-06-22 12:29:10.915124
# Unit test for function read_user_dict
def test_read_user_dict():
    # This dict is valid input
    test_input = '[{"first_name":"John"},{"last_name":"Smith"}]'
    # This dict is not valid input
    test_invalid_input = '[{"first_name":"John"}'

    # Process valid input
    test_dict = process_json(test_input)
    assert test_dict == [{"first_name": "John"}, {"last_name": "Smith"}]

    # Process invalid input
    try:
        test_dict = process_json(test_invalid_input)
    except:
        test_dict = ""
    assert test_dict == ""

# Generated at 2022-06-22 12:29:20.470463
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Tests the prompt_for_config function"""
    import inspect
    import os
    import sys
    import tempfile
    from cookiecutter import utils
    from cookiecutter.compat import string_types

    try:
        import pypandoc
        pypandoc_available = True
    except ImportError:
        pypandoc_available = False

    current_path = inspect.getfile(inspect.currentframe())
    current_dir = os.path.dirname(os.path.abspath(current_path))
    templates_dir = os.path.join(current_dir, "templates")

    # Sample output from prompt_for_config

# Generated at 2022-06-22 12:29:27.347283
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Test function prompt_for_config."""

# Generated at 2022-06-22 12:29:29.823927
# Unit test for function read_user_dict
def test_read_user_dict():
    result = read_user_dict('test_variable', {'foo': 'bar'})
    assert result == {'foo': 'bar'}

# Generated at 2022-06-22 12:29:36.478509
# Unit test for function read_user_dict
def test_read_user_dict():
    #The function read_user_dict takes default value as an argument
    #default value is a dictionary and hence it is a dictionary
    default_value = {'hello':'world'}
    #variable name is a string value
    var_name = "Enter a dictionary"
    #the variable choice_value accepts the returned value of read_user_dict
    choice_value = read_user_dict(var_name, default_value)
    print(choice_value)

# Generated at 2022-06-22 12:29:47.080021
# Unit test for function prompt_for_config
def test_prompt_for_config():
    # Test a regular variable
    context = {
        'cookiecutter': {
            'project_name': 'Default project name',
        }
    }
    cookiecutter_dict = prompt_for_config(context)
    assert 'project_name' in cookiecutter_dict

    # Test a regular variable that is to be used in a dictionary
    context = {
        'cookiecutter': {
            'project_name': 'Default project name',
            'repo_name': {
                'default': '{{ cookiecutter.project_name.replace(" ", "_") }}'
            }
        }
    }
    cookiecutter_dict = prompt_for_config(context)
    assert 'project_name' in cookiecutter_dict
    assert 'repo_name' in cookiecutter_dict

    # Test a dict variable

# Generated at 2022-06-22 12:29:52.781335
# Unit test for function read_user_dict
def test_read_user_dict():
    default_value = {
        "test": {
                "test1": "test1"
                }
        }
    user_value = '{"test": {"test1": "test1"}}'
    for valid_json_dict in [default_value, user_value]:
        dict = read_user_dict("var_name", default_value)
        if valid_json_dict:
            assert dict == valid_json_dict

# Generated at 2022-06-22 12:30:04.725460
# Unit test for function prompt_for_config
def test_prompt_for_config():
    '''
    Test function prompt_for_config
    '''


# Generated at 2022-06-22 12:30:15.129543
# Unit test for function prompt_for_config
def test_prompt_for_config():
    # Test1: input is a single option -> return that
    assert prompt_for_config({'cookiecutter': {'opt1': 5}}, no_input=True) == {'opt1': 5}

    # Test2: input is a list of options -> return first option
    assert prompt_for_config({'cookiecutter': {'opt1': [5, 6, 7]}}, no_input=True) == {'opt1': 5}

    # Test3: nested input (opt1's value depends on opt2) and user provides no input -> return default
    assert prompt_for_config({'cookiecutter': {'opt1': '{{ opt2 }}', 'opt2': 10}}, no_input=True) == {'opt1': 10, 'opt2': 10}

    # Test4: nested input (opt1's value depends on

# Generated at 2022-06-22 12:30:27.380684
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """
    This is a unit test for the prompt_for_config function.
    This function tests the expected output with inputs of different kinds
    """
    #Code to test the positive scenarios
    context = {
        'cookiecutter': {
        'project_name': 'My Test Project',
        'repo_name': '{{ cookiecutter.project_name.replace(" ", "_") }}',
        'repo_name_in_lowercase':
            '{{ cookiecutter.repo_name.lower() }}'
        }
    }
    cookiecutter_dict = {'project_name': 'My Test Project',
                         'repo_name': 'My_Test_Project',
                         'repo_name_in_lowercase': 'my_test_project'}
    assert prompt_for_config(context) == cookiecutter

# Generated at 2022-06-22 12:30:44.195188
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:30:55.928444
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {
        'cookiecutter': {
            'project_name': 'Awesome Project',
            'author_name': 'Joe Doe',
            'description': 'An awesome project',
            'open_source_license': 'MIT license',
            'email': 'joe.doe@example.com',
            'version': '0.1.0',
        }
    }
    result = prompt_for_config(context, no_input=True)
    assert result == {'project_name': 'Awesome Project',
                      'author_name': 'Joe Doe',
                      'description': 'An awesome project',
                      'open_source_license': 'MIT license',
                      'email': 'joe.doe@example.com',
                      'version': '0.1.0'}

# Generated at 2022-06-22 12:31:07.126854
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {
        "cookiecutter": {
            "full_name": "Frank the Tank",
            "email": "frank@cookiecutter.example.org",
            "github_username": "frankthetank",
            "project_name": "cookiecutter-pypackage",
            "repo_name": "cookiecutter-pypackage",
            "project_short_description": "A short description of the project.",
            "select_linter": [
                "flake8",
                "pylint",
                "none",
            ],
            "pypi_username": "",
            "use_pycharm": "n",
        }
    }

    cookiecutter_dict = prompt_for_config(context)

# Generated at 2022-06-22 12:31:09.975894
# Unit test for function read_user_dict
def test_read_user_dict():
    user_value = '{"testkey": "testvalue"}'
    result = read_user_dict('test', default_value=None, user_value=user_value)
    assert result['testkey'] == 'testvalue'

# Generated at 2022-06-22 12:31:18.112999
# Unit test for function prompt_for_config
def test_prompt_for_config():
    test_context = {
        'cookiecutter': {
            'project_name': "{{cookiecutter.repo_name}}",
            'repo_name': '{{cookiecutter.repo_name}}',
            'repo_name': 'myproject',
            'repo_url': 'https://github.com/{{cookiecutter.repo_name}}',
            'select_option': [
                'option1',
                'option2',
                'option3',
                '{{cookiecutter.project_name}}',
            ],
            '_private': 'hidden',
            '__nonprivate': "{{cookiecutter.repo_name}}",
        }
    }


# Generated at 2022-06-22 12:31:23.144209
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {
        'cookiecutter': {
            'full_name': 'Full Name',
            'email': 'Email Address'
        }
    }
    cookiecutter_dict = prompt_for_config(context)
    assert cookiecutter_dict['full_name'] is not None
    assert cookiecutter_dict['email'] is not None

# Generated at 2022-06-22 12:31:34.206234
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """ Unit test for function prompt_for_config """

    # Test for function prompt_for_config with all testing scenarios
    prompt_for_config(
        {
            'cookiecutter': {
                'project_name': "My project's name",
                'use_pypi_deployment_with_travis': True,
                'open_source_license': "MIT",
                'python_version': "py36",
                'create_author_file': True,
                'command_line_interface': "click",
                'use_pytest': True,
                'use_cookiecutter': True,
            }
        },
    )


# Generated at 2022-06-22 12:31:42.343828
# Unit test for function read_user_dict
def test_read_user_dict():
    """Test function read_user_dict to be used in cookiecutter.tests.test_prompt.py"""
    var_name = 'var_name'
    var_dict = {'var_name': {'a': 'A', 'b': 'B'}}
    response_default = True

    user_dict = read_user_dict(var_name, var_dict)
    assert user_dict == var_dict

    user_dict = read_user_dict(var_name, var_dict, default_value=response_default)

# Generated at 2022-06-22 12:31:45.758043
# Unit test for function process_json
def test_process_json():
    user_value = "{'author': 'abc'}"
    assert process_json(user_value) == {'author': 'abc'}

# Generated at 2022-06-22 12:31:56.137379
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """ Test function prompt_for_config """
    # Unit test setup
    context = {
        "cookiecutter": {
            "project_name": "test_project_name",
            "repo_name": "test_repo_name"
        }
    }
    # Unit tests

    # Test no config input
    cookiecutter_dict = prompt_for_config(context, True)
    assert cookiecutter_dict == {"project_name": "test_project_name", "repo_name": "test_repo_name"}

    # Test config input
    cookiecutter_dict = prompt_for_config(context, False)
    assert cookiecutter_dict == {"project_name": "test_project_name", "repo_name": "test_repo_name"}

# Generated at 2022-06-22 12:32:07.476934
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Unit test for function prompt_for_config"""
    test_context = {}
    test_context['cookiecutter'] = {}
    test_context['cookiecutter']['project_slug'] = "project_slug"
    test_context['cookiecutter_dict'] = {}
    result = prompt_for_config(test_context)

    assert result == {}

# Generated at 2022-06-22 12:32:13.655719
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Test for function prompt_for_config"""
    context = {
        "cookiecutter": {
            "key1": "y",
            "key2": "n",
            "key3": "",
            "key4": "",
            "key5": "v1",
        }
    }

    cookiecutter_dict = prompt_for_config(context, no_input=True)
    print(cookiecutter_dict)
    assert cookiecutter_dict["key1"] == "y"
    assert cookiecutter_dict["key2"] == "n"
    assert cookiecutter_dict["key3"] == ""
    assert cookiecutter_dict["key4"] == ""
    assert cookiecutter_dict["key5"] == "v1"

if __name__ == "__main__":
    import sys

# Generated at 2022-06-22 12:32:25.997054
# Unit test for function render_variable
def test_render_variable():
    env = StrictEnvironment(context={'foo': 'bar'})
    assert render_variable(env, '{{ cookiecutter.foo }}', {}) == 'bar'

    assert render_variable(env, '{{ cookiecutter.foo }}',
        {'a':'b', 'c':'d'}) == 'bar'

    # TODO: add a test for a dict variable

    ctx = {
        'cookiecutter': {
            'choice_one': ['One', 'Two', 'Three'],
            'choice_two': ['Four', 'Five', 'Six'],
            'choice_three': ['Seven', 'Eight', 'Nine'],
        }
    }

    env = StrictEnvironment(context=ctx)

    # Test single level nested choices

# Generated at 2022-06-22 12:32:34.123533
# Unit test for function read_user_dict
def test_read_user_dict():
    # Test that it returns the default value if no user input happens
    default_dict = OrderedDict([('a', '1'), ('b', '2')])
    result = read_user_dict('var_name', default_dict)
    assert result == default_dict

    # Test that TypeError is raised if the default value is not a dict
    try:
        read_user_dict('var_name', 'not a dict')
    except TypeError:
        pass
    else:
        assert False

    # Test that ValueError is raised if the default value is an empty dict
    try:
        read_user_dict('var_name', {})
    except ValueError:
        pass
    else:
        assert False



# Generated at 2022-06-22 12:32:44.912732
# Unit test for function read_user_dict
def test_read_user_dict():
    """Unit test for function read_user_dict."""
    from jinja2.exceptions import UndefinedError

    env = StrictEnvironment()

    cct_dict = {
        '__keys': ['key1', 'key2'],
        'key2': 'default2',
        'key1': {'key1_1': 'default1_1'},
    }

    ### Choose to replace all keys

    # Create a new context from cct_dict, so we can use it again
    context = {'cookiecutter': cct_dict.copy()}
    # Call function to be tested
    new_dict = read_user_dict('keys', cct_dict, env, context)

    # Test new_dict
    assert new_dict['__keys'] == ['key1', 'key2']
    assert new_dict

# Generated at 2022-06-22 12:32:53.620608
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Unit test for function prompt_for_config."""
    from collections import OrderedDict

    # Set up the context
    # This must be an OrderedDict to preserve ordering

# Generated at 2022-06-22 12:33:04.316355
# Unit test for function render_variable
def test_render_variable():
    import os
    import random
    from cookiecutter.utils import rmtree

    from .prompt import render_variable

    test_dir = os.path.abspath(os.path.dirname(__file__))


# Generated at 2022-06-22 12:33:15.906943
# Unit test for function read_user_choice
def test_read_user_choice():
    # Test if everything is fine / Case 1
    #
    # Notice that read_user_choice() is a prompt function,
    # in this case we are providing the input to it, so for us the input is
    # not the output.
    #
    # This is called white box testing.
    #
    # The scope of white box testing is limited to the code that we have
    # written i.e. this function and its unit test function.
    #
    # The scope of black box testing is NOT limited to the code that we have
    # written.

    # Arrange
    expected_choice = 'Saturday'
    var_name = 'Weekday'
    options = ['Saturday', 'Sunday']
    # Act
    # We are providing the input for read_user_choice()

# Generated at 2022-06-22 12:33:20.947411
# Unit test for function prompt_for_config
def test_prompt_for_config():
    from cookiecutter.main import cookiecutter

    context = cookiecutter('tests/fake-repo-tmpl/', no_input=True)
    context["cookiecutter"]["author_name"] = "Test"
    assert context["cookiecutter"] == prompt_for_config(context, no_input=True)

# Generated at 2022-06-22 12:33:31.036872
# Unit test for function read_user_choice
def test_read_user_choice():
    # test empty choice
    options = []
    var_name = 'var_name'
    with pytest.raises(ValueError) as err:
        read_user_choice(var_name, options)
    assert str(err.value) == 'No choices provided'

    # test no input
    options = [1, 2]
    var_name = 'var_name'
    user_choice = read_user_choice(var_name, options)
    assert user_choice == options[0]

    # test incorrect input
    options = [1, 2]
    var_name = 'var_name'
    user_input = 'a'
    with pytest.raises(ValueError) as err:
        user_choice = read_user_choice(var_name, options, user_input)

# Generated at 2022-06-22 12:33:41.666659
# Unit test for function read_user_dict
def test_read_user_dict():
    """
    Unit test for function read_user_dict
    """
    dict_str = """
    {
        "test": "1"
    }
    """
    dict_ret = read_user_dict("test", {'test': '1'})

    assert dict_ret == json.loads(dict_str)

# Generated at 2022-06-22 12:33:48.361963
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:33:54.093774
# Unit test for function read_user_dict
def test_read_user_dict():
    """Unit test for function read_user_dict."""
    from cookiecutter.main import cookiecutter
    context = cookiecutter(
      '.',
      no_input=True,
      extra_context={
        'dict_var': { 'this': 'that' }
      }
    )
    assert 'dict_var' in context
    assert isinstance(context['dict_var'], dict)
    assert context['dict_var']['this'] == 'that'


# Generated at 2022-06-22 12:34:03.667485
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:34:12.255910
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Test function prompt_for_config."""
    # Test the empty template
    context = {'cookiecutter': OrderedDict([])}
    assert prompt_for_config(context) == {}

    # Test a simple variable
    context = {
        'cookiecutter': OrderedDict([('project_name', 'default_project_name')])
    }
    assert prompt_for_config(context) == {'project_name': 'default_project_name'}

    # Test a choice variable
    context = {
        'cookiecutter': OrderedDict(
            [('option', [1, 2, 3]), ('another_option', ['a', 'b', 'c'])]
        )
    }

# Generated at 2022-06-22 12:34:20.230975
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {
        'cookiecutter': {
            'repo_name': 'Repo Name',
            'repo_description': '{{ cookiecutter.repo_name }} is a short description.',
            'open_source_license': 'MIT',
            'author_name': 'Author Name',
            'author_email': 'author@email.com',
        }
    }

    cookiecutter_dict = prompt_for_config(context, no_input=True)
    assert cookiecutter_dict['author_name'] == 'Author Name'
    assert cookiecutter_dict['repo_name'] == 'Repo Name'
    assert cookiecutter_dict['repo_description'] == 'Repo Name is a short description.'

# Generated at 2022-06-22 12:34:30.569457
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {
        'cookiecutter': {
            'project_name': 'Cookiecutter',
            'description': "A command-line utility that creates projects from "
                           "cookiecutters (project templates), e.g. Python "
                           "package projects, VueJS projects.",
            'author_name': "Audrey Roy",
            'email': "audreyr@example.com",
            'github_username': "audreyr",
            'version': '0.1.0',
            'open_source_license': 'MIT',
        }
    }
    cookiecutter_dict = prompt_for_config(context, no_input=True)
    assert cookiecutter_dict == context['cookiecutter']