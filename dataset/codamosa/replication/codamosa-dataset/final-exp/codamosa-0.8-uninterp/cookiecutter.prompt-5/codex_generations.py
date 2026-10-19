

# Generated at 2022-06-22 12:24:39.713545
# Unit test for function render_variable
def test_render_variable():
    context = {
        'cookiecutter': {
            "project_name": "{{ cookiecutter.project_slug.upper() }}"
        }
    }
    rendered = render_variable(StrictEnvironment(context=context),
                               '{{ cookiecutter.project_name.upper() }}',
                               {'cookiecutter': {'project_slug': 'test_project'}})

    assert rendered == 'TEST_PROJECT'

# Generated at 2022-06-22 12:24:43.272641
# Unit test for function process_json
def test_process_json():
    assert process_json('{"a":1, "b":2}') == {"a":1, "b":2}

# Generated at 2022-06-22 12:24:53.056414
# Unit test for function process_json
def test_process_json():
    user_value = '{"bool_dict": {"a": true, "b": false}}'
    result = process_json(user_value)
    assert result == {"bool_dict": {"a": True, "b": False}}, (
        'process_json failed to process bools in dicts'
    )

    user_value = '{"str_dict": {"a": true, "b": "false"}}'
    result = process_json(user_value)
    assert result == {"str_dict": {"a": True, "b": "false"}}, (
        'process_json failed to process bools in dicts'
    )

    user_value = '{"bool_list": [true, false]}'
    result = process_json(user_value)

# Generated at 2022-06-22 12:24:57.052739
# Unit test for function process_json
def test_process_json():
    input = '{"test1": "test2"}'
    output = process_json(input)
    assert type(output) == dict
    assert output['test1'] == 'test2'


# Generated at 2022-06-22 12:25:06.759310
# Unit test for function process_json
def test_process_json():
    assert (process_json('{"foo": "bar"}') == {'foo': 'bar'})
    assert (process_json('["foo", "bar"]') == ['foo', 'bar'])
    assert (process_json('["foo", ["bar"], {"baz": "qux"}]') == ['foo', ['bar'], {'baz': 'qux'}])
    assert (process_json('["foo", ["bar"]]') == ['foo', ['bar']])
    assert (process_json('{"foo": {"bar": "baz"}}') == {'foo': {'bar': 'baz'}})
    assert (process_json('{"foo": ["bar", {"baz": "qux"}]}') == {'foo': ['bar', {'baz': 'qux'}]})

# Generated at 2022-06-22 12:25:15.251429
# Unit test for function read_user_dict
def test_read_user_dict():
    import pytest
    env = StrictEnvironment()
    context = {'cookiecutter': {'foo': {'bar': 'baz'}}}
    user_input = read_user_dict('foo', {'bar': 'baz'})
    assert 'baz' in user_input.values()
    with pytest.raises(TypeError):
        read_user_dict('foo', 'bar')
    cookiecutter_dict = {'foo': {'bar': 'baz'}}
    assert render_variable(env, 'bar', cookiecutter_dict) == 'bar'
    with pytest.raises(UndefinedVariableInTemplate):
        render_variable(env, 'bar', {})

# Generated at 2022-06-22 12:25:20.777945
# Unit test for function process_json
def test_process_json():
    """Test for function process_json"""

    # test for a valid json
    result = process_json('{"key": "value"}')
    assert isinstance(result, dict)

    # test for a invalid json
    try:
        process_json('{"key": value"}')
    except click.UsageError:
        pass
    else:
        raise AssertionError

# Generated at 2022-06-22 12:25:23.895195
# Unit test for function process_json
def test_process_json():
    user_value = '{"foo": "bar"}'
    assert process_json(user_value) == {"foo": "bar"}
    user_value = 'foo'
    try:
        process_json(user_value)
    except click.UsageError:
        assert True
    except:
        assert False

# Generated at 2022-06-22 12:25:30.689995
# Unit test for function read_user_choice
def test_read_user_choice():
    var_name = "Enter a number"
    options = ['a', 'b', 'c', 'd']

    # Test if all options are printed correctly
    choice_lines = ['1 - a\n2 - b\n3 - c\n4 - d']
    correct_prompt = var_name + '\n' + '\n'.join(choice_lines) + '\nChoose from 1, 2, 3, 4'
    assert read_user_choice(var_name, options) == 'a'



# Generated at 2022-06-22 12:25:41.352834
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """ Test that prompt_for_config works correctly """
    import json
    import os
    import tempfile

    # Test values
    question = "What is your name?"
    default_value = "Alice"
    options = [
        "A very long option",
        "Another long option"
    ]
    custom_dict = {
        "key": "value",
        "another_key": "another value"
    }
    choice_option = options[0]
    invalid_json_dict = "{'key': 'value', 'another_key': 'another_value'}"
    invalid_json_string = "\"key\": \"value\", \"another_key\": \"another_value\""
    invalid_json_list = "[\"key\", \"another_key\"]"

    # Create a temporary context file

# Generated at 2022-06-22 12:25:57.502744
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {'cookiecutter': {'name': 'My name', 'age': 18}}
    result = prompt_for_config(context, no_input=True)
    expected = {'name': 'My name', 'age': 18}
    assert result == expected, result

# Generated at 2022-06-22 12:26:04.329661
# Unit test for function read_user_dict
def test_read_user_dict():
    """
    Test method to check behavior for function read_user_dict
    """
    input_dict = {'key_1': 'Test_1', 'key_2': 'Test_2'}
    chosen_dict = {'key_1': 'Test_1', 'key_2': 'Test_3'}

    assert chosen_dict == read_user_dict('test_dict', input_dict)

# Generated at 2022-06-22 12:26:09.564653
# Unit test for function read_user_dict
def test_read_user_dict():
    assert {'a': 1, 'b': 2} == read_user_dict('', {'a': 1, 'b': 2})
    assert {'a': 1, 'b': 2} == read_user_dict('', {'a': 1, 'b': 2})
    assert {'a': 1, 'b': 2} == read_user_dict(
        '',
        {'a': 1, 'b': 2},
    )

# Generated at 2022-06-22 12:26:19.907009
# Unit test for function prompt_for_config
def test_prompt_for_config():
    no_input_result = prompt_for_config({'cookiecutter': {
        'key1': 'value1',
        'key2': 'value2',
        # _key3 is a dictionary, but the keys and values of that dictionary
        # aren't specified until the second pass, so it's ok in the first pass.
        '_key3': {
            'choice1': 'value3',
            'choice2': 'value4',
        },
        'dict': {
            # It's allowed to nest a private variable here also, since it
            # doesn't need to be processed during the first pass.
            '_private_key': 'private_value',
            'dict_key': '{{ cookiecutter.key1 }}',
        }
    }}, no_input=True)

# Generated at 2022-06-22 12:26:31.038143
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:26:41.112089
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {"cookiecutter": {"cookie_id":1, "cookie_name": None, "cookie_origin": "China", "cookie_toppings": ["chocolate", "peanut butter"]}}
    cookies_dict = OrderedDict()
    env = StrictEnvironment(context=context)
    for key, raw in context['cookiecutter'].items():
        if key.startswith('_') and not key.startswith('__'):
            cookies_dict[key] = raw
            continue
        elif key.startswith('__'):
            cookies_dict[key] = render_variable(env, raw, cookies_dict)
            continue


# Generated at 2022-06-22 12:26:50.778032
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Check prompt_for_config function."""
    import os

    import pytest

    from cookiecutter.main import cookiecutter

    @pytest.fixture
    def context():
        """Get the context to be used in the test."""

# Generated at 2022-06-22 12:26:55.193142
# Unit test for function render_variable
def test_render_variable():
    assert render_variable(
        {'cookiecutter': {'project_name': 'Peanut Butter Cookie'}},
        '{{ cookiecutter.project_name.replace(" ", "_") }}',
        {},
    ) == 'Peanut_Butter_Cookie'

# Generated at 2022-06-22 12:27:04.656276
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {
        'cookiecutter': {
            'cookiecutter': {'cookiecutter': 'text'},
            'cookie': {'cookie': 'text'},
            'option1': ['option1', 'option2'],
            'option2': ['option1', 'option2'],
            'project_name': 'text',
            'repo_name': "{{ cookiecutter.project_name.replace(' ', '_') }}",
            '_private': {'private': 'text'}
        }
    }
    cookiecutter_dict = prompt_for_config(context, no_input=True)
    assert cookiecutter_dict['cookiecutter'] == 'text'
    assert cookiecutter_dict['cookie'] == 'text'
    assert cookiecutter_dict['option1'] == 'option1'

# Generated at 2022-06-22 12:27:10.441454
# Unit test for function read_user_dict
def test_read_user_dict():
    env = StrictEnvironment(context=context)
    key = "mydict"
    default_value = {'k1': 'v1'}
    output = read_user_dict(key, default_value)
    assert output == {'k1': 'v1'}, "test_read_user_dict failed"
    # print("test_read_user_dict passed")

# Generated at 2022-06-22 12:27:18.681873
# Unit test for function read_user_dict
def test_read_user_dict():
    var_name = 'foo'
    default_value = 'bar'

    assert read_user_dict(var_name, default_value) == default_value

# Generated at 2022-06-22 12:27:29.349021
# Unit test for function prompt_for_config
def test_prompt_for_config():
    # pylint: disable=unused-import, unused-variable, invalid-name
    import_error = None
    try:
        import click
    except ImportError:
        import_error = ImportError('Failed "import click" in prompt.py')
    else:
        pass
    if import_error:
        raise import_error


# Generated at 2022-06-22 12:27:40.439380
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Ensure prompt for config works fine with dummy params..

    :return: Boolean value indicating success or failure
    """
    # Dummy context

# Generated at 2022-06-22 12:27:42.369524
# Unit test for function prompt_for_config
def test_prompt_for_config():
    from cookiecutter.main import cookiecutter

    cookiecutter('.', no_input=True)

# Generated at 2022-06-22 12:27:53.926433
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Test for function prompt_for_config."""
    click.echo = click.echo_via_pager = click.style = click.secho = click.edit = click.getchar = click.get_text_stream = lambda *args, **kwargs: args

    # Prepare context
    context = {
        'cookiecutter': {
            'user_choice': [
                'Option 1',
                'Option 2',
                'Option 3',
            ],
            'choices': {
                'choice_1': 'Item 1',
                'choice_2': 'Item 2',
            }
        }
    }
    env = StrictEnvironment(context=context)

    # Test for simple variable
    user_input = 'User input'
    user_input_with_default = 'User input (default: default value)'
    user_

# Generated at 2022-06-22 12:28:02.725441
# Unit test for function render_variable
def test_render_variable():
    context = {
        "cookiecutter": {
            "app_name": "My Test Project",
            "app_name_slug": "my_test_project"
        }
    }
    env = StrictEnvironment(context=context)
    cookiecutter_dict = {'cookiecutter':context['cookiecutter']}
    # Test variable: {{ cookiecutter.app_name.replace(" ", "_") }}
    # Output: My_Test_Project
    # Should not: My Test Project
    raw = '{{ cookiecutter.app_name.replace(" ", "_") }}'
    rendered_template = render_variable(env, raw, cookiecutter_dict)
    assert rendered_template == 'My_Test_Project'

# Generated at 2022-06-22 12:28:14.630551
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:28:26.007863
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:28:34.336255
# Unit test for function prompt_for_config
def test_prompt_for_config():
    from cookiecutter.environment import StrictEnvironment


# Generated at 2022-06-22 12:28:44.476101
# Unit test for function prompt_for_config
def test_prompt_for_config():
    from cookiecutter.main import cookiecutter

    c = cookiecutter(
        'tests/fake-repo-tmpl/',
        no_input=True,
        extra_context={
            'repo_name': 'cookiecutter-django',
            'project_name': 'Cookiecutter Django',
            'project_slug': 'cookiecutter-django',
            'project_version': '0.1.0',
            'description': 'A cookiecutter template for Django projects.',
            'domain_name': 'example.com',
            'timezone': 'Europe/Paris',
            'python_version': '3.7',
            'version': '0.1.0',
            'use_pycharm': 'n',
        },
    )

    #  viva la recursion!


# Generated at 2022-06-22 12:28:54.994808
# Unit test for function prompt_for_config
def test_prompt_for_config():
    test_context = {'cookiecutter': {'project_name': "test_project", 'puppies': ["test_pup"]}}
    test_cookiecutter_dict = {'project_name': "test_project", 'puppies': ["test_pup"]}
    assert(prompt_for_config(test_context) == test_cookiecutter_dict)

# Generated at 2022-06-22 12:29:03.779343
# Unit test for function prompt_for_config
def test_prompt_for_config():
    test_context = {
        "cookiecutter": {
            "project_name": "Peanut Butter Cookies",
            "project_name_slug": "{{ cookiecutter.project_name.replace(' ', '_') }}"
        }
    }
    result = prompt_for_config(test_context, no_input=True)
    expected_result = {"project_name": "Peanut Butter Cookies", "project_name_slug": "Peanut_Butter_Cookies"}
    assert result == expected_result



# Generated at 2022-06-22 12:29:08.132518
# Unit test for function read_user_dict
def test_read_user_dict():
    """Functions for testing the read_user_dict prompt."""
    from click.testing import CliRunner

    result = CliRunner().invoke(
        read_user_dict,
        args=('blah', 'default'),
        catch_exceptions=False
    )
    assert result.exit_code == 0



# Generated at 2022-06-22 12:29:12.523928
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {
        "cookiecutter": {
            "author_email": "test_email@testemail.com"
        }
    }

    cookiecutter_dict = prompt_for_config(context, no_input=True)

    assert cookiecutter_dict["author_email"] is not None

# Generated at 2022-06-22 12:29:20.051711
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {
        'cookiecutter': {
            'project_name': 'Build a Foo',
            'repo_name': '{{ cookiecutter.project_name.lower().replace(" ", "_") }}',
            'author_name': 'Your name here',
            'email': 'Your email here',
        }
    }
    user = {
        'project_name': 'Build a Foo',
        'repo_name': 'build_a_foo',
        'author_name': 'Your name here',
        'email': 'Your email here',
    }
    assert prompt_for_config(context) == user

# Generated at 2022-06-22 12:29:28.584885
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Tests for the prompt_for_config function."""
    from cookiecutter.main import cookiecutter

    context = cookiecutter(
        'tests/test-files/invalid-ctx-with-choice-dict-entry/', no_input=True
    )
    assert context == {
        'foo': 'a',
        'bar': 'b',
        'foo_bar': {'_copy_without_render': True},
        'dict_entry': 'bar',
        'spam': 'c',
        'baz': 'd',
    }

# Generated at 2022-06-22 12:29:40.884671
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:29:49.354098
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Test prompt_for_config() function."""
    import os
    import copy

    from cookiecutter.utils import rmtree

    from .utils import WORKING_DIR

    test_context = OrderedDict()
    test_context['project_slug'] = 'cookiecutter_project_slug'
    test_context['project_name'] = 'Cookiecutter Project Name'
    test_context['project_short_description'] = 'Cookiecutter project short description'
    test_context['repo_name'] = 'Cookiecutter Repo Name'
    test_context['repo_description'] = 'Cookiecutter Repo Description'
    test_context['select_license'] = 'MIT license'
    test_context['pypi_username'] = 'cookiecutter'

# Generated at 2022-06-22 12:29:57.024897
# Unit test for function prompt_for_config
def test_prompt_for_config():
    import pytest
    cookiecutter_dict = prompt_for_config({ 'cookiecutter': {
      'project_name': 'example',
      'project_slug': '{{ cookiecutter.project_name.lower().replace(" ", "-") }}',
      'repo_name': '{{ cookiecutter.project_name.replace(" ", "_") }}'
    }})
    assert cookiecutter_dict['project_name'] == 'example'
    assert cookiecutter_dict['project_slug'] == 'example'
    assert cookiecutter_dict['repo_name'] == 'example'

# Generated at 2022-06-22 12:30:03.130644
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {
        'cookiecutter': {
            'project_name': {'project_name': '{{ cookiecutter.project_name.upper() }}'}
        }
    }
    result = prompt_for_config(context, no_input=True)

    assert result == {}
# End of unit test for function prompt_for_config

# Generated at 2022-06-22 12:30:30.145349
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Unit test for function prompt_for_config."""
    # test with 1
    context = {"cookiecutter": {"one_num": 1}}
    cookiecutter_dict = prompt_for_config(context)
    assert cookiecutter_dict == {"one_num": 1}

    # test with word
    context = {"cookiecutter": {"one_word": "one"}}
    cookiecutter_dict = prompt_for_config(context)
    assert cookiecutter_dict == {"one_word": "one"}

    # test with 2
    context = {"cookiecutter": {"two_num": 2}}
    cookiecutter_dict = prompt_for_config(context)
    assert cookiecutter_dict == {"two_num": 2}

    # test with choice

# Generated at 2022-06-22 12:30:35.738769
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = dict(
        cookiecutter={
            'project_name': 'Awesome Project',
            'repo_name': '{{ cookiecutter.project_name.lower().replace(" ", "-") }}',
            'pypi_username': '{{ cookiecutter.github_username }}',
            'open_source_license': 'MIT',
            'year': '{{ "%s"|format(datetime.date.today().year) }}',
            'version': '0.1.0',
        }
    )

    cookiecutter_dict = prompt_for_config(context, no_input=True)

    assert cookiecutter_dict['project_name'] == 'Awesome Project'
    assert cookiecutter_dict['repo_name'] == 'awesome-project'
    assert cookiecutter_dict['year'] == '2018'

# Generated at 2022-06-22 12:30:45.295724
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {
        'cookiecutter': {
            'username': '{{ cookiecutter.first_name }} {{ cookiecutter.last_name }}',
            'first_name': 'First',
            'last_name': 'Last',
            'greeting': 'Hello {{ cookiecutter.username }}!',
            '_copy_without_render': {'no_jinja': '{{ cookiecutter.greeting }}'}
        }
    }

    cookiecutter_dict = prompt_for_config(context)
    assert cookiecutter_dict['username'] == 'First Last'
    assert cookiecutter_dict['greeting'] == 'Hello First Last!'
    assert cookiecutter_dict['_copy_without_render']['no_jinja'] == '{{ cookiecutter.greeting }}'

# Generated at 2022-06-22 12:30:57.535078
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Unit test for function prompt_for_config()"""
    no_input=True

# Generated at 2022-06-22 12:31:08.501364
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {
        'cookiecutter': {
            'full_name': 'Colin',
            'email': 'awesome@colin.com',
            'github_username': 'colinsurprenant',
            'project_name': 'awesomeproject',
            'project_slug': 'awesomeproject',
            'release_date': '2014/02/16',
            'version': '0.1.0',
            'pypi_username': 'colinsurprenant',
            'select_license': ['MIT', 'BSD', 'GPL'],
            'open_source_license': 'MIT',
        }
    }
    
    rendered_project_name = '{{ cookiecutter.project_name }}'

# Generated at 2022-06-22 12:31:17.259880
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:31:28.088227
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Unit test for function prompt_for_config"""
    import cookiecutter.prompt as cp
    
    context = {
        "cookiecutter": {
            "key1": "{{cookiecutter.key2}}",
            "key2": "val1",
            "keyDict1": {"key1": "{{cookiecutter.key2}}"},
            "keyDict2": {"dictkey1": "val1"},
            "keyDict3": {"key1": "{{'cookiecutter.key2'}}"},
            "keyDict4": {"key1": "{{cookiecutter.noop1}}"}
        }
    }
    cookiecutter_dict = cp.prompt_for_config(context, no_input=True)

# Generated at 2022-06-22 12:31:32.455985
# Unit test for function read_user_dict
def test_read_user_dict():
    user_dict = read_user_dict('testVal', {"testKey":"testVal"})
    if not isinstance(user_dict, dict):
        print('test_read_user_dict: user variable is not a dict')
        return False
    return True

# Generated at 2022-06-22 12:31:41.335254
# Unit test for function prompt_for_config
def test_prompt_for_config():
    json_data = '''{
        "project_name": "{{ cookiecutter.project_slug|upper }}",
        "project_slug": "{{ cookiecutter.project_name|lower }}",
        "project_type": ["a", "b", "c"],
        "use_pipenv": "{{ cookiecutter.use_pipenv|upper }}",
        "use_pytest": "{{ cookiecutter.use_pytest|upper }}",
        "open_source_license": "{{ cookiecutter.open_source_license|lower }}",
        "_template": {
            "repo_name": "{{ cookiecutter.project_name.replace(' ', '_')|lower }}"
        }
    }'''

# Generated at 2022-06-22 12:31:47.106937
# Unit test for function read_user_choice
def test_read_user_choice():
    assert (
        read_user_choice('test', [{'t': 'e', 's': 't'}, 'test']) == {'t': 'e', 's': 't'}
    )
    assert read_user_choice('test', ['test']) == 'test'
    assert read_user_choice('test', []) == []

# Generated at 2022-06-22 12:32:23.721577
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:32:27.169052
# Unit test for function prompt_for_config
def test_prompt_for_config():
    from cookiecutter.main import cookiecutter
    from cookiecutter.vcs import git_clone_url, git_clone

    with click.testing.CliRunner().isolated_filesystem():
        repo_dir = git_clone(
            git_clone_url(),
            checkout='test_prompt_for_config',
            no_input=True,
        )
        cookiecutter(repo_dir)

# Generated at 2022-06-22 12:32:33.010995
# Unit test for function read_user_dict
def test_read_user_dict():

    class Cli(object):
        default = "default"

        def __init__(self):
            self.prompts = []

        def prompt(self, prompt, default, type, value_proc):
            self.prompts.append(prompt)

            if len(self.prompts) == 1:
                return "default"

            elif len(self.prompts) == 2:
                return "{}"

            elif len(self.prompts) == 3:
                return "{\"a\": 5}"

            else:
                raise Exception("Don't call this function again.")

    class FakeContext(object):
        def __init__(self, obj):
            self.obj = obj

        def get_default(self, key):
            return self.obj[key]

    var_name = 'var_name'

# Generated at 2022-06-22 12:32:41.353703
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Unit test for function prompt_for_config."""
    # pylint: disable=protected-access
    from cookiecutter.main import cookiecutter

    # Read the cookiecutter.json file.
    context = cookiecutter('{{ cookiecutter.project_name }}')
    # pylint: enable=protected-access
    del context['encoding']
    # pylint: disable=unused-variable
    rendered_context = prompt_for_config(context, no_input=True)
    # pylint: enable=unused-variable

# Generated at 2022-06-22 12:32:51.869456
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:33:00.617756
# Unit test for function prompt_for_config
def test_prompt_for_config():
    config = {'cookiecutter': {
        'project_name': 'Test Project',
        'repo_name': "{{cookiecutter.project_name.lower() | slugify}}"
    }}
    user_config = prompt_for_config(config)
    assert 'project_name' in user_config
    assert user_config['project_name'] == 'Test Project'
    assert 'repo_name' in user_config
    assert user_config['repo_name'] == 'test-project'

# Generated at 2022-06-22 12:33:06.989217
# Unit test for function prompt_for_config
def test_prompt_for_config():
    from cookiecutter import config, utils
    from cookiecutter.repository import determine_repo_dir

    # TODO: Add unit tests for function prompt_for_config
    args = {
        "no_input": True,
        "extra_context": {},
        "replay": False,
        "overwrite_if_exists": False,
        "output_dir": ".",
        "config_file": config.DEFAULT_CONFIG_FILE,
        "default_config": True,
    }
    cwd = utils.get_src_root()
    config_dict = config.get_user_config(args=args)
    repo_dir = determine_repo_dir(
        config_dict["cookiecutters_dir"], config_dict["replay_dir"]
    )
    context = ut

# Generated at 2022-06-22 12:33:10.247126
# Unit test for function read_user_dict
def test_read_user_dict():
    var_name = "Dict item"
    default_value = {"key1": "value1", "key2": "value2"}
    print(read_user_dict(var_name, default_value))

# Generated at 2022-06-22 12:33:19.438980
# Unit test for function read_user_dict
def test_read_user_dict():
    test_cases = [
        ("Empty dict", {}, {}, {}),
        ("Value dict", {"a": "b"}, {}, {"a": "b"}),
        ("Default dict", {}, {"a": "b"}, {"a": "b"}),
        ("Multi level dict", {"b": "c"}, {"a": {"b": "c"}}, {"a": {"b": "c"}}),
    ]

    for (tc_name, tc_context, tc_default, tc_expected) in test_cases:
        result = read_user_dict(tc_name, tc_default)
        assert result == tc_expected

# Generated at 2022-06-22 12:33:21.677565
# Unit test for function read_user_choice
def test_read_user_choice():
    options = ['foo', 'bar']
    assert read_user_choice(var_name='var_name', options=options) == 'foo'

# Generated at 2022-06-22 12:33:59.480012
# Unit test for function read_user_choice
def test_read_user_choice():
    options = ['Apple', 'Orange', 'Tomato']
    variable = 'fruit'
    choice = read_user_choice(variable, options)
    assert choice in options

# Generated at 2022-06-22 12:34:10.969359
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {
        "cookiecutter": {
            "project_name": "{{cookiecutter.project_slug.replace('-', ' ')|title}}",
            "_template": {"description": "Description for {{cookiecutter.project_name}}"},
            "project_slug": "my-new-project",
            "pypi_username": "audreyr",
            "open_source_license": "MIT",
            "__copyright_holder": "Tania Allard",
            "__copyright_year": "2018",
            "__version__": "0.1.0",
        }
    }
    cookiecutter_dict = prompt_for_config(context)
    assert cookiecutter_dict['project_slug'] == 'my-new-project'

# Generated at 2022-06-22 12:34:16.602535
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Test that the prompt for config function returns
    a valid cookiecutter dictionary."""
    context = {
        'cookiecutter': {
            'project_name': 'test_project',
        }
    }
    cookiecutter_dict = prompt_for_config(context, no_input=True)

    assert cookiecutter_dict['project_name'] == 'test_project'

# Generated at 2022-06-22 12:34:28.816726
# Unit test for function prompt_for_config
def test_prompt_for_config():
    def assert_dict_keys(dictionary, *args):
        # helper method to check if dictionary has keys
        # that are defined in the *args list
        assert sorted(dictionary.keys()) == sorted(list(*args))
