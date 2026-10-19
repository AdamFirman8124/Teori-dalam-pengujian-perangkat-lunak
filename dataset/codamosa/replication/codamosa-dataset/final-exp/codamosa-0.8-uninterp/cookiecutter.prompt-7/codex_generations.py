

# Generated at 2022-06-22 12:24:48.201195
# Unit test for function render_variable
def test_render_variable():
    """
    This is only a unit test for function render_variable,
    not all variables could be tested here.
    """
    context = {
        "cookiecutter": {
            "{{cookiecutter.test_string}}": "test_string",
            "{{cookiecutter.test_int}}": "test_int",
            "{{cookiecutter.test_list}}": "test_list",
            "{{cookiecutter.test_list_list}}": "test_list_list",
            "{{cookiecutter.test_dict}}": "test_dict",
            "{{cookiecutter.test_dict_dict}}": "test_dict_dict",
        }
    }

# Generated at 2022-06-22 12:24:58.073922
# Unit test for function prompt_for_config
def test_prompt_for_config():
    # a simple config file
    class Config1:
        project_name = 'Project Name'

    # a config file with choices
    class Config2:
        choices = ['c1', 'c2']
        project_name = 'Project Name'

    # a config file with a nested dict
    class Config3:
        project_name = 'Project Name'
        meta = {
            'ses': 'SES',
        }

    # a config file with a nested dict and choices
    class Config4:
        choices = ['c1', 'c2']
        project_name = 'Project Name'
        meta = {
            'ses': 'SES',
        }

    # a config file with a project_var
    class Config5:
        project_name = 'Project Name'

# Generated at 2022-06-22 12:25:06.081771
# Unit test for function read_user_dict
def test_read_user_dict():
    var_name = 'test_dict'
    test_dict = {'test_key':'test_val'} 
    default_value = test_dict
    default_dict = {'test_key':'test_val'}

    user_value = "json_object"
    json_object = {}

    user_dict = read_user_dict(var_name, default_value)
    assert user_dict == default_dict

    user_dict = read_user_dict(var_name, default_value)
    assert user_dict == default_dict

    user_dict = read_user_dict(var_name, default_value)
    assert user_dict == default_dict

# Generated at 2022-06-22 12:25:15.736486
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:25:22.441440
# Unit test for function process_json
def test_process_json():
    user_value = process_json("{}")
    assert isinstance(user_value, dict), "user_value should be dict"

    user_value = process_json("[]")
    assert isinstance(user_value, list), "user_value should be list"

    user_value = process_json("asd")
    assert isinstance(user_value, str), "user_value should be string"

if __name__ == "__main__":
    test_process_json()

# Generated at 2022-06-22 12:25:34.929090
# Unit test for function prompt_for_config
def test_prompt_for_config():
    empty_context = {'cookiecutter': OrderedDict([])}
    assert prompt_for_config(empty_context, no_input=True) == {}

    context = {
        'cookiecutter': {
            'project_name': 'My Project',
            'project_slug': 'my_project',
            '_template': {'license': 'MIT', 'foo': 'bar'},
            '__default': {
                'foo': 'bar',
                'num': 1,
                'list': ['a', 'b', 'c'],
                'dict': {'x': 'y'},
                'nested_dict': {'a': {'b': {'c': 'd'}}}
            },
        }
    }


# Generated at 2022-06-22 12:25:39.363237
# Unit test for function process_json
def test_process_json():
    assert process_json('{"a": 1, "b": "foo"}') == {'a': 1, 'b': 'foo'}
    assert process_json('{"a": 1, "b": "foo", "c": [1, 2, 3]}') == \
        {'a': 1, 'b': 'foo', 'c': [1, 2, 3]}
    assert process_json('{"a": 1}') == {'a': 1}
    assert process_json('{"a": {"c": 2, "b": 1}}') == {'a': {'c': 2, 'b': 1}}
    assert process_json('{"a": {"b": {"c": 2, "d": 1}}}') == \
        {'a': {'b': {'c': 2, 'd': 1}}}

# Generated at 2022-06-22 12:25:42.538153
# Unit test for function read_user_dict
def test_read_user_dict():
    user_value = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
    assert read_user_dict('test_var_name', default_value=user_value) == user_value

# Generated at 2022-06-22 12:25:53.992964
# Unit test for function prompt_for_config
def test_prompt_for_config():
    import click
    import click.testing
    import json
    import os
    import tempfile
    import textwrap

    # Create a temporary directory
    temp_directory = tempfile.mkdtemp()
    print("Created temporary directory: {}".format(temp_directory))

    # Change to the temporary directory
    os.chdir(temp_directory)

    # Create the cookiecutter.json file

# Generated at 2022-06-22 12:26:01.108809
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:26:14.627214
# Unit test for function read_user_dict
def test_read_user_dict():
    """Test if user_dict is correctly read
    """
    from .context_dict import prompt_for_config
    from .main import render_variable
    import os
    import pytest
    
    
    # test if user_dict is correctly read and returns a dictionary
    def test_read_user_dict():
            assert read_user_dict('var_name', {'default': 'value'}) == {'default': 'value'}

    # test if an invalid type is not accepted
    def test_read_user_dict_type():
        with pytest.raises(TypeError):
            read_user_dict('var_name', 'default_value')

    # test if an invalid dictionary is not accepted
    def test_read_user_dict_value():
        with pytest.raises(ValueError):
            read_user_

# Generated at 2022-06-22 12:26:17.692228
# Unit test for function read_user_dict
def test_read_user_dict():

    try:
        read_user_dict(1, "test")
    except TypeError:
        pass

    try:
        read_user_dict("Test", {"a": "b"})
        assert True
    except TypeError:
        assert False

# Generated at 2022-06-22 12:26:26.941527
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Unit test for function prompt_for_config."""

    context = {
        'cookiecutter': {
            'project_name': 'Cookiecutter',
            '_template': {
                'repo_name': '{{ cookiecutter.project_name.lower() }}',
                'repo_owner': '{{ cookiecutter.project_name }}',
                'repo_url': 'https://github.com/{{ cookiecutter.repo_owner }}/'
                '{{ cookiecutter.repo_name }}',
                '_copy_without_render': ['COPYING'],
            },
            '_copy_without_render': ['LICENSE'],
        }
    }

    # Test to ensure that a single variable is converted to a string

# Generated at 2022-06-22 12:26:28.458341
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Unit test for function prompt_for_config."""
    pass


# Generated at 2022-06-22 12:26:32.857825
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {"cookiecutter": {"project_name": "Test", "repo_name": "test"}}

    cookiecutter_dict = prompt_for_config(context, no_input=True)

    assert cookiecutter_dict["project_name"] == "Test"
    assert cookiecutter_dict["repo_name"] == "test"

# Generated at 2022-06-22 12:26:42.500985
# Unit test for function read_user_dict
def test_read_user_dict():
    test_dict = {'a': 'b', 'c': 'd'}
    # The `process_json` function will be called by prompt, so let's just
    # mock that.
    process_json_orig = process_json
    click.prompt = lambda *args, **kwargs: '{"a": "b", "c":"d"}'
    process_json = lambda x: test_dict

    test_output = read_user_dict('test', {'e': 'f'})
    click.prompt = lambda *args, **kwargs: '{"e": "f"}'
    test_output2 = read_user_dict('test', {'e': 'f'})
    assert test_dict == test_output
    assert {'e': 'f'} == test_output2
    process_json = process_json

# Generated at 2022-06-22 12:26:53.819105
# Unit test for function prompt_for_config
def test_prompt_for_config():
    import os
    from cookiecutter import utils

    context = utils.load_context_raw(
        os.path.join(os.path.dirname(__file__), '.')
    )

    # test the ordinary variables and choices
    cookiecutter_dict = prompt_for_config(context)

# Generated at 2022-06-22 12:27:00.975545
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Assert function prompt_for_config works as expected"""
    context = {
        "cookiecutter": {
            "project_name": "{{ cookiecutter.full_name | replace(' ', '') | lower }}",
            "full_name": "John Doe",
            "email": "johndoe@example.com"
        }
    }
    assert prompt_for_config(context) == {'project_name': 'johndoe', 'full_name': 'John Doe', 'email': 'johndoe@example.com'}

# Generated at 2022-06-22 12:27:03.123891
# Unit test for function read_user_dict
def test_read_user_dict():
    user_dict = read_user_dict('{}', default_value={'test': 500})
    assert user_dict['test'] == 500

# Generated at 2022-06-22 12:27:13.869976
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:27:25.442588
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """
    This method is used to verify the validity of the prompt_for_config() method.
    The test is by no means exhaustive, but rather a basic test to verify it can be run.
    """
    context = {'cookiecutter': {'name' : 'test_project'}}
    result = prompt_for_config(context)

    assert result['name'] == 'test_project'

# Generated at 2022-06-22 12:27:34.923391
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {
        'cookiecutter': {
            'project_name': 'Test Project',
            'repo_name': '{{ cookiecutter.project_name.replace(" ", "_") }}',
            'description': 'This is a test project',
            'open_source_license': 'MIT',
            'use_pytest': True,
            'use_pypi_deployment_with_travis': True,
            'command_line_interface': 'click',
            'version': '0.1.0',
            'include_python_version_in_package_name': True,
        }
    }
    cookiecutter_dict = prompt_for_config(context, no_input=False)


# Generated at 2022-06-22 12:27:43.375463
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:27:54.221300
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Test prompt_for_config function."""
    import os
    import random
    import string
    import tempfile

    def random_string(length=8):
        """Return a random string of the given length."""
        return ''.join(
            random.choice(string.ascii_lowercase) for i in range(length)
        )

    project_name = random_string()
    full_name = random_string()
    email = '{}@{}.com'.format(random_string(4), random_string(4))
    repo_name = random_string()

    root_dir = tempfile.mkdtemp()

    os.chdir(root_dir)


# Generated at 2022-06-22 12:27:55.710950
# Unit test for function prompt_for_config
def test_prompt_for_config():
    # please see tests/test_prompt_for_config.py
    pass

# Generated at 2022-06-22 12:28:00.520625
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """
    Function to test prompt_for_config function
    """
    from cookiecutter.main import cookiecutter
    context = cookiecutter(template='.', no_input=True)
    assert context['full_name'] == 'Your Name'
    cookiecutter_dict = prompt_for_config(context, no_input=False)
    assert len(cookiecutter_dict) > 0



# Generated at 2022-06-22 12:28:12.312453
# Unit test for function read_user_dict
def test_read_user_dict():
    var_name = "VAR_NAME"
    user_dict = read_user_dict(var_name, {})
    assert user_dict == {}
    user_dict = read_user_dict(var_name, {"a": "b", "c": {"d": "e"}})
    assert user_dict == {"a": "b", "c": {"d": "e"}}
    # Malformed JSON
    try:
        user_dict = read_user_dict(var_name, "")
    except click.UsageError:
        assert True
    else:
        assert False
    # Non-dict JSON
    try:
        user_dict = read_user_dict(var_name, "[]")
    except click.UsageError:
        assert True
    else:
        assert False

# Generated at 2022-06-22 12:28:15.930960
# Unit test for function read_user_dict
def test_read_user_dict():
    # Test non-default value
    assert read_user_dict('blabla', {"a": 1, "b": 2, "c": 3}) == {"a": 1, "b": 2, "c": 3}
    # Test default value
    assert read_user_dict('blabla', 'default_value') == 'default_value'

# Generated at 2022-06-22 12:28:27.069726
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Validate the prompt_for_config function."""

# Generated at 2022-06-22 12:28:38.556322
# Unit test for function read_user_dict
def test_read_user_dict():
    variable_name = "Enter a dictionary"
    default_value = {'key1': {'key2': 'value2'}}
    assert read_user_dict(variable_name, default_value) == default_value

    user_value = '{"key1": {"key2": "value2"}}'
    assert read_user_dict(variable_name, default_value) == default_value

    user_value = '{"key1": {"key2": "value2"}, "key3": "value3"}'
    assert read_user_dict(variable_name, default_value) == json.loads(user_value, object_pairs_hook=OrderedDict)

    user_value = '{"key1": "value1", "key3": "value3"}'

# Generated at 2022-06-22 12:28:50.671254
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:28:54.317114
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """
        test function prompt_for_config
    """
    no_input = True
    context = {'cookiecutter': {'test': '11test'}}
    cookiecutter_dict = prompt_for_config(context, no_input)
    assert cookiecutter_dict == {'test': '11test'}


# Generated at 2022-06-22 12:29:06.229937
# Unit test for function read_user_dict
def test_read_user_dict():
    """Test for function read_user_dict."""
    # Test invalid data type of default_value
    context = {"cookiecutter": {"original_variable": 15}}
    try:
        read_user_dict("original_variable", 1234)
        print("Not the correct type.")
    except TypeError:
        print("The correct type.")

    # Test invalid value type of default_value
    try:
        read_user_dict("original_variable", [])
        print("Not the correct type.")
    except TypeError:
        print("The correct type.")

    # Test empty default value
    try:
        read_user_dict("original_variable", {})
        print("Not the correct type.")
    except TypeError:
        print("The correct type.")

    # Test user input the default value

# Generated at 2022-06-22 12:29:09.651233
# Unit test for function read_user_dict
def test_read_user_dict():
    user_dict = read_user_dict("Read user dict", {'a': 1, 'b': 2})
    assert isinstance(user_dict, dict)



# Generated at 2022-06-22 12:29:12.203560
# Unit test for function read_user_dict
def test_read_user_dict():
	assert read_user_dict('project_name', {"project_name": "project_name_test"}) == {"project_name": "project_name_test"}


# Generated at 2022-06-22 12:29:20.736311
# Unit test for function render_variable
def test_render_variable():
    """ Tests the function render_variable """
    from .main import testing_workflow
    from .replay import record_responses
    from .compat import TemporaryDirectory

    with TemporaryDirectory(suffix='-cookiecutter') as temp_dir:
        with record_responses('tests/fixtures/responses/test_render_variable', temp_dir):
            testing_workflow(temp_dir, 'tests/fixtures/fake-repo-pre/', no_input=False)
        
        with record_responses('tests/fixtures/responses/test_render_variable', temp_dir):
            testing_workflow(temp_dir, 'tests/fixtures/fake-repo-pre/', no_input=True)

# Generated at 2022-06-22 12:29:28.829561
# Unit test for function read_user_dict
def test_read_user_dict():
    context = {
        'cookiecutter': {
            'dict_variable': {
                'key-1': 'value-1',
                'key-2': 'value-2',
                'key-3': 'value-3',
            }
        }
    }
    derived_dict = prompt_for_config(context)
    assert derived_dict['dict_variable'] == {
        'key-1': 'value-1',
        'key-2': 'value-2',
        'key-3': 'value-3',
    }

# Generated at 2022-06-22 12:29:41.093538
# Unit test for function prompt_for_config
def test_prompt_for_config():

    from collections import OrderedDict

    from jinja2 import Environment, FileSystemLoader
    from cookiecutter.main import cookiecutter
    from cookiecutter.context_file import generate_context_file

    fixture = 'tests/fixtures/prompts-cookiecutter-dict'

    result = cookiecutter(
        template=fixture,
        default_config=False,
        output_dir = '',
        no_input=False,
        overwrite_if_exists=False,
    )

    # Create the template context
    context_file = generate_context_file(result['context_file'])
    context = context_file.read()
    context = json.loads(context, object_pairs_hook=OrderedDict)

    # Setup jinja environment

# Generated at 2022-06-22 12:29:51.443999
# Unit test for function read_user_dict
def test_read_user_dict():
    """Test for the function read_user_dict."""
    # Test for the default case.
    user_dict = read_user_dict(
        "dict_1",
        {
            "key1": "value1",
            "key2": "value2",
        },
    )
    assert user_dict == {
        "key1": "value1",
        "key2": "value2",
    }

    # Test for the non default case.
    user_dict = read_user_dict(
        "dict_2",
        {
            "key1": "value1",
            "key2": "value2",
        },
    )
    assert user_dict == {
        "key3": "value3",
        "key4": "value4",
    }

# Generated at 2022-06-22 12:29:54.104754
# Unit test for function read_user_choice
def test_read_user_choice():
    options = [1, 2, 3]
    var_name = "This is a test"
    assert 1 == read_user_choice(var_name, options)


# Generated at 2022-06-22 12:30:03.977219
# Unit test for function prompt_for_config
def test_prompt_for_config():
    # README.md does not include cookiecutter dict, so add it for test.
    context = {"cookiecutter": {"repo_name": "Test"}}

    # Use no_input because we are skipping command prompt.
    cookiecutter_dict = prompt_for_config(context, no_input=True)
    assert cookiecutter_dict["repo_name"] == "Test"

# Generated at 2022-06-22 12:30:14.666993
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Integration test for function prompt_for_config."""
    from tests.functional.cookiecutter_dict_templates import (
        simple_dict_template, raw_template,
    )

    context = {'cookiecutter': simple_dict_template()}
    cookiecutter_dict = prompt_for_config(context, no_input=True)
    assert cookiecutter_dict == {
        'project_name': 'Jinja2',
        'author_name': 'Armin Ronacher and the Pallets team',
        'package_name': 'jinja2',
        'pypi_username': 'mitsuhiko',
    }

    context = {'cookiecutter': raw_template()}
    cookiecutter_dict = prompt_for_config(context, no_input=True)
    assert cookiecutter_

# Generated at 2022-06-22 12:30:26.777581
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:30:38.859860
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Make sure the function prompt_for_config works fine."""

# Generated at 2022-06-22 12:30:47.338866
# Unit test for function read_user_dict
def test_read_user_dict():
    '''
    Testing read_user_dict function
    '''
    from contextlib import redirect_stdout
    from io import StringIO
    import sys
    from cookiecutter.main import cookiecutter

    # Run the cookiecutter
    with redirect_stdout(StringIO()):
        result = cookiecutter(
            'tests/test-hooks-repo/', no_input=False, extra_context={'read_user_dict': 1}
        )

    # Check output
    print(result['read_user_dict'])

    context_test_json = {'key1': 'value1', 'key2': ['value2a', 'value2b']}
    if result['read_user_dict'] == context_test_json:
        print('Read User Dict function works as expected')

# Generated at 2022-06-22 12:30:58.792717
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:31:09.513120
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """
    Test that cookiecutter configuration works properly.
    """
    from cookiecutter.main import determine_repo_dir


# Generated at 2022-06-22 12:31:17.147232
# Unit test for function prompt_for_config
def test_prompt_for_config():

    #Test without any input
    value1 = prompt_for_config({})

    assert isinstance(value1,dict)
    assert value1 == {}


    #Test for with default values
    value2 = prompt_for_config({ 'cookiecutter': {'name':'value1'}})

    assert isinstance(value2,dict)
    assert value2 == {'name':'value1'}


    #Test for with a input via prompt question
    value3 = prompt_for_config({ 'cookiecutter': {'name':'value1'}})

    assert isinstance(value3,dict)
    assert value3 == {'name':'value2'}

# Generated at 2022-06-22 12:31:27.995857
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """A unit test for the prompt_for_config function"""
    from mock import Mock, patch

    from cookiecutter.main import cookiecutter

    def mock_read_user_variable(var_name, default_value):
        return default_value

    def mock_read_user_yes_no(question, default_value):
        return default_value

    def mock_read_user_choice(var_name, options):
        return options[0]

    def mock_read_user_dict(var_name, default_value):
        return default_value


# Generated at 2022-06-22 12:31:35.718175
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Test prompt to enter a new config."""
    assert prompt_for_config({'cookiecutter': {'project_name': 'example'}}) == {'project_name': 'example'}
    assert prompt_for_config({'cookiecutter': {'project_name': 'example'}}, True) == {'project_name': 'example'}
    assert prompt_for_config({
        'cookiecutter': {'project_name': '{{ cookiecutter.project_name }}'}
    }) == {'project_name': ''}

# Generated at 2022-06-22 12:31:48.038519
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {'cookiecutter': {'name': 'Test', 'surname': 'Dev'}}
    assert prompt_for_config(context, no_input=True) == {'name': 'Test', 'surname': 'Dev'}

# Generated at 2022-06-22 12:31:59.049248
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {
        'cookiecutter': {
            'project_name': 'Example Project',
            'repo_name': 'example_project',
            'open_source_license': 'MIT license',
            'project_short_description': 'An example project',
            'author_name': 'Joe Doe',
            'email': 'joe.doe@example.org',
            'github_username': 'jdoe',
        }
    }
    cookiecutter = prompt_for_config(context, no_input=True)
    assert cookiecutter['project_name'] == 'Example Project'
    assert cookiecutter['repo_name'] == 'example_project'
    assert cookiecutter['open_source_license'] == 'MIT license'
    assert cookiecutter['project_short_description'] == 'An example project'

# Generated at 2022-06-22 12:32:05.981019
# Unit test for function prompt_for_config
def test_prompt_for_config():
    click.confirm = lambda _, prompt_suffix: True
    click.prompt = lambda _, default: 'fake_key'
    

# Generated at 2022-06-22 12:32:12.623013
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context={'cookiecutter': OrderedDict([('project_name', 'project-name'), ('repo_name', '{{ project_name | lower }}')])}
    cookiecutter_dict = prompt_for_config(context)
    assert cookiecutter_dict['project_name'] == 'project-name'
    assert cookiecutter_dict['repo_name'] == 'project-name'



# Generated at 2022-06-22 12:32:24.926880
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Unit test for prompt_for_config"""
    import json
    from collections import OrderedDict
    from cookiecutter import environment


    context = {}
    context['cookiecutter'] = OrderedDict()

    with open("tests/test-data/fake-repo-pre/cookiecutter.json") as f:
        context['cookiecutter'] = json.load(f, object_pairs_hook=OrderedDict)


    cookiecutter_dict = prompt_for_config(context)

    env = environment.StrictEnvironment(context=context)
    cookiecutter_dict['repo_name'] = env.from_string("{{ cookiecutter.project_name.replace(' ', '_') }}").render(
        cookiecutter=cookiecutter_dict)

    # display all the keys

# Generated at 2022-06-22 12:32:34.006821
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Test that renders the sample variables and runs
    them all through.
    """
    from cookiecutter import default_config
    from cookiecutter.prompt import read_user_choice
    from cookiecutter import utils
    from tests.test_prompt import monkeypatch_environment

    monkeypatch_environment({
        'no_input': True,
        'overwrite_if_exists': True,
    })

    config_dict = default_config.get_user_config()
    config_dict['cookiecutter']['full_name'] = 'Peter Pan'
    config_dict['cookiecutter']['email'] = 'peterpan@example.com'
    config_dict['cookiecutter']['project_name'] = 'Awesome Project'

# Generated at 2022-06-22 12:32:44.870143
# Unit test for function prompt_for_config
def test_prompt_for_config():
    # Instantiate the necessary objects
    context = {}
    context['cookiecutter'] = {}
    # Add a simple variable
    context['cookiecutter']['full_name'] = "Jane Doe"

    # Add a dictionary
    context['cookiecutter']['social_links'] = {}
    context['cookiecutter']['social_links']['facebook'] = "http://facebook.com/"
    context['cookiecutter']['social_links']['twitter'] = "http://twitter.com/"

    # Add a list of choices
    context['cookiecutter']['choices'] = []
    context['cookiecutter']['choices'].append('Choice 1')
    context['cookiecutter']['choices'].append('Choice 2')

# Generated at 2022-06-22 12:32:53.620853
# Unit test for function read_user_dict
def test_read_user_dict():
    import unittest

    class TestReadUserDict(unittest.TestCase):

        def test_read_user_dict_1(self):
            """Test user input for dictionary"""
            first_dict = {"name": "Gurpreet", "age": 22}
            self.assertEqual(first_dict,read_user_dict("Enter user details",first_dict))

        def test_read_user_dict_2(self):
            """Test user input for dictionary"""
            second_dict = {"name": "Jack"}
            self.assertEqual(second_dict,read_user_dict("Enter user details",second_dict))

        def test_read_user_dict_3(self):
            """Test user input for dictionary"""
            third_dict = {"age": 25}

# Generated at 2022-06-22 12:33:00.728408
# Unit test for function read_user_dict
def test_read_user_dict():
    assert read_user_dict('a key', {'a': 'b'}) == {'a': 'b'}
    assert read_user_dict('a key', {'a': {'b': 'c', 'd': 'e'}}) == {'a': {'b': 'c', 'd': 'e'}, 'a key': {'b': 'c', 'd': 'e'}}

# Generated at 2022-06-22 12:33:07.029176
# Unit test for function prompt_for_config
def test_prompt_for_config():
    import os
    import pprint
    import json


# Generated at 2022-06-22 12:33:25.154487
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:33:30.540405
# Unit test for function read_user_dict
def test_read_user_dict():
    user_dict = read_user_dict('Enter a JSON dict', {'foo': 'foo_def'})
    assert isinstance(user_dict, dict)
    assert user_dict == {'foo': 'foo_def'}

    user_dict = read_user_dict('Enter a JSON dict', {})
    assert isinstance(user_dict, dict)
    assert user_dict == {}

# Generated at 2022-06-22 12:33:41.204928
# Unit test for function render_variable
def test_render_variable():
    from cookiecutter.config import DEFAULT_CONFIG

    env = StrictEnvironment(context={})
    context = {
        'cookiecutter': {
            'project_name': 'my-project-name',
            'cookiecutter': DEFAULT_CONFIG['cookiecutter'],
        }
    }
    cookiecutter_dict = {}
    assert render_variable(env, '{{ cookiecutter.project_name }}', cookiecutter_dict) == 'my-project-name'
    assert render_variable(env, None, cookiecutter_dict) is None
    assert render_variable(env, 5, cookiecutter_dict) == '5'
    assert render_variable(env, [1, 2, 3], cookiecutter_dict) == ['1', '2', '3']

# Generated at 2022-06-22 12:33:47.919220
# Unit test for function render_variable
def test_render_variable():
    """Test that render_variable returns the correct value."""
    context = {
        'cookiecutter': {
            'project_name': 'Python Boilerplate',
            'project_slug': '{{ cookiecutter.project_name.lower().replace(" ", "-") }}',
            'test_test': '{{ cookiecutter.test }}'
        }
    }

    env = StrictEnvironment(context=context)
    print(env.list_templates(context))
    assert render_variable(env,
        '{{ cookiecutter.project_name.lower().replace(" ", "-") }}',
        context['cookiecutter']) == 'python-boilerplate'
    assert render_variable(env,
        '{{ cookiecutter.test_test }}',
        context['cookiecutter']) == ''

# Generated at 2022-06-22 12:33:55.267065
# Unit test for function read_user_dict
def test_read_user_dict():
    dict_var_name = 'dictionary_variable'
    dict_default_value = {'key1': 'value1', 'key2': 123}
    dict_user_value = '{"key1": "foo", "key2": 234}'
    dict_result = {'key1': 'foo', 'key2': 234}

    assert read_user_dict(dict_var_name, dict_default_value) == dict_default_value
    assert read_user_dict(dict_var_name, dict_default_value, dict_user_value) == dict_result


test_read_user_dict()

# Generated at 2022-06-22 12:34:04.492570
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {
        "cookiecutter": {
            "project_name": "Cookiecutter",
            "project_slug": "cookiecutter",
            "license": "BSD license",
            "domain_name": "example.com",
            "email": "your_email@example.com",
            "description": "A command-line utility that creates projects from "
            "project templates, e.g. creating a Python package project "
            "from a Python package project template.",
            "timezone": "UTC",
            "version": "0.1.0",
            "open_source_license": "BSD license",
            "_copy_without_render": ["{{cookiecutter.project_slug}}/tests/"],
        }
    }
    config = prompt_for_config(context)
    print(config)
   

# Generated at 2022-06-22 12:34:06.145313
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {
        "cookiecutter": {"name": "foo bar"}
    }
    config = prompt_for_config(context)
    assert config['name'] == 'foo bar'

# Generated at 2022-06-22 12:34:12.922394
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Test prompt_for_config()."""

# Generated at 2022-06-22 12:34:21.027538
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Test prompt_for_config function."""

# Generated at 2022-06-22 12:34:23.845315
# Unit test for function prompt_for_config
def test_prompt_for_config():
    import json
    import copy

    test_context = copy.deepcopy(__test_context)

    cookiecutter_dict = prompt_for_config(test_context)