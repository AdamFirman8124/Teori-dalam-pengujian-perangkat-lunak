

# Generated at 2022-06-22 12:24:53.298280
# Unit test for function process_json
def test_process_json():
    user_values = ['{}', '[]', '["test"]', '{"values": "test"}', 'false']
    user_values_2 = ['{', '[[["{}"]]]', '["test]', '{"values": "test"', 'false}']
    expected_values = [{}, [], ["test"], {"values": "test"}, False]
    expected_values_2 = None, None, None, None, None

    for user_value, expected_value in zip(user_values, expected_values):
        assert process_json(user_value) == expected_value

    for user_value, expected_value in zip(user_values_2, expected_values_2):
        try:
            process_json(user_value)
            assert False
        except click.UsageError:
            pass

# Generated at 2022-06-22 12:25:04.100627
# Unit test for function prompt_for_config
def test_prompt_for_config():
    config = {
        'cookiecutter':{
            'full_name': 'Jane Doe',
            'email': 'janedoe@foo.com',
            'github_username': 'janedoe',
            'project_name': 'My Project',
            'date': '2010-01-01',
            'timezone': 'Europe/Berlin',
            '_timezone': ['Europe/Berlin', 'UTC', 'America/Lima']
        }
    }

    test_config = prompt_for_config(config)

    assert (test_config['full_name'] == 'Jane Doe')
    assert (test_config['email'] == 'janedoe@foo.com')
    assert (test_config['github_username'] == 'janedoe')
    assert (test_config['project_name'] == 'My Project')


# Generated at 2022-06-22 12:25:09.033029
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {
        'cookiecutter': {
            'project_name': 'Awesome Project',
        }
    }
    cookiecutter_dict = prompt_for_config(context)

    expected_cookiecutter_dict = {
        'project_name': 'Awesome Project',
    }
    assert cookiecutter_dict == expected_cookiecutter_dict



# Generated at 2022-06-22 12:25:18.085350
# Unit test for function prompt_for_config
def test_prompt_for_config():
    ctx = {
        'cookiecutter': {
            'project_name': 'Foobar',
            'repo_name': '{{ cookiecutter.project_name.replace(" ", "_") }}',
            'project_slug': '{{ cookiecutter.repo_name|lower }}',
            'select_tech': [
                'A',
                'B',
                'C',
            ],
            'platform': {
                'select_os': [
                    'Linux',
                    'MacOS',
                    'Windows',
                ],
            },
        }
    }

    no_input = False
    cookiecutter_dict = prompt_for_config(ctx, no_input=no_input)

    assert cookiecutter_dict['project_name'] == 'Foobar'

# Generated at 2022-06-22 12:25:21.844005
# Unit test for function process_json
def test_process_json():
    """
    Test if the process_json function is working
    """
    user_value_json = '{"name":"test"}'
    user_dict = process_json(user_value_json)
    assert user_dict['name'] == 'test'

# Generated at 2022-06-22 12:25:34.270317
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Test function prompt_for_config"""
    # Test with no input
    no_input_context = {
        "cookiecutter": {
            "project_name": "My Project",
            "myvar": "{{cookiecutter.project_name}}",
            "mylist": ["{{cookiecutter.project_name}}", "foo"],
            "mydict": {"{{cookiecutter.project_name}}": "foo"},
        }
    }

    no_input_cookiecutter_dict = prompt_for_config(no_input_context, True)

    assert no_input_cookiecutter_dict["project_name"] == "My Project"
    assert no_input_cookiecutter_dict["myvar"] == "My Project"

# Generated at 2022-06-22 12:25:44.727784
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """
    Test whether user prompts are working as expected.
    """
    context = {
        "cookiecutter": {
            "project_name": "test_project",
            "github_repository": "test_github_repository",
            "github_username": "test_github_username",
            "project_slug": "{{ cookiecutter.project_name | slugify }}",
            "author": "test_author"
        }
    }

    config = prompt_for_config(context, no_input=True)
    assert config["project_name"] == "test_project"
    assert config["github_repository"] == "test_github_repository"
    assert config["github_username"] == "test_github_username"
    assert config["project_slug"] == "test-project"


# Generated at 2022-06-22 12:25:55.618875
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:26:04.585731
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Test function prompt_for_config."""
    # pylint: disable=line-too-long

# Generated at 2022-06-22 12:26:08.206997
# Unit test for function process_json
def test_process_json():
    """Test process_json"""
    assert process_json('{"key": "val"}') == {"key": "val"}
    assert process_json('{"key": "val", "key2": "val2"}') == {"key": "val", "key2": "val2"}

# Generated at 2022-06-22 12:26:22.865984
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Unit tests for prompt_for_config function."""

    # Unit tests for prompt_choice_for_config
    # Define test context for prompt_for_config
    context = {
        "cookiecutter": {
            "project_name": "Test Project",
            "test_value": "Test Value",
            '__test_value': "Test Value",
            "test_value_2": "Test Value 2",
        }
    }

    # Test calling prompt_choice_for_config with no_input=True
    rendered_project_name = prompt_choice_for_config(
        context['cookiecutter'], StrictEnvironment(context=context),
        "project_name",
        ['Test Project'],
        True,
    )
    assert rendered_project_name == 'Test Project'

    # Test calling prompt_choice

# Generated at 2022-06-22 12:26:33.232090
# Unit test for function process_json
def test_process_json():
    """Test function process_json."""
    # '{"key1": "val1"}'  ->  {'key1': 'val1'}
    assert process_json('{"key1": "val1"}') == {'key1': 'val1'}
    # '{"key1": "val1", "key2": "val2"}'  ->  {'key1': 'val1', 'key2': 'val2'}
    assert (
        process_json('{"key1": "val1", "key2": "val2"}')
        == {'key1': 'val1', 'key2': 'val2'}
    )
    # '{"key1": "val1", "key2": "val2", "key3": "val3"}'  ->  {'key1': 'val1', 'key2

# Generated at 2022-06-22 12:26:42.875935
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {'cookiecutter': {
        'project_name': 'A project',
        'project_slug': '{{ cookiecutter.project_name.lower().replace(" ", "_") }}',
        'project_dir': '{{ cookiecutter.project_slug }}',
        '_template': {
            'license': 'MIT license',
            'repo_name': '{{ cookiecutter.project_slug }}',
            'author_name': '{{ cookiecutter.owner_name }}'
        },
        '__version__': 'v{{ cookiecutter.version }}'
    }}

# Generated at 2022-06-22 12:26:47.681667
# Unit test for function process_json
def test_process_json():
    """Test for function process_json
    """
    if process_json('{"mydict": "myvalue"}') == dict(mydict='myvalue'):
        print('Unit test for function process_json successful')
    else:
        print('Unit test for function process_json unsuccessful')


# Generated at 2022-06-22 12:26:56.030182
# Unit test for function read_user_dict
def test_read_user_dict():
    var_name = 'variable name'
    default_value = OrderedDict([
        ('dict_key', 'dict_value'),
        ('key_2', 'value_2')
    ])
    expected_value = OrderedDict([
        ('dict_key', 'dict_value'),
        ('key_2', 'value_2'),
        ('key_3', 'value_3')
    ])
    user_value = '''
       {
         "dict_key": "dict_value",
         "key_2": "value_2",
         "key_3": "value_3"
       }
    '''

    user_response = process_json(user_value)
    assert process_json(default_value) == default_value
    assert read_user_dict(var_name, default_value) == expected

# Generated at 2022-06-22 12:26:57.767100
# Unit test for function process_json
def test_process_json():
    assert process_json('{"name": "bob"}') == {'name': 'bob'}

# Generated at 2022-06-22 12:27:00.620448
# Unit test for function read_user_dict
def test_read_user_dict():
    var_name = 'testkey'
    default = 'testkey'
    options = read_user_dict(var_name, default)
    print(options)

if __name__ == '__main__':
    test_read_user_dict()

# Generated at 2022-06-22 12:27:05.656821
# Unit test for function prompt_for_config
def test_prompt_for_config():
    from cookiecutter.context_config import DEFAULT_CONFIG

    expected_prompts = {
        'project_name': 'project_name',
        'package_name': 'package_name',
    }

    context = {
        'cookiecutter': DEFAULT_CONFIG,
    }

    prompt_for_config(context, no_input=True)

# Generated at 2022-06-22 12:27:17.311530
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """ Unit test for the function prompt_for_config

    Tests the following cases:
    1. Simple variable
    2. Raw variable
    3. Choice variable
    4. Dictionary variable

    """
    context = {'cookiecutter':{'project_name':'example',
                               '_raw_project_name':'example',
                               '__project_name':'example',
                               'colors':['Red', 'Green', 'Blue'],
                               '_colors':['Red', 'Green', 'Blue'],
                               '__colors':['Red', 'Green', 'Blue'],
                               'dict':{'a':'b'},
                               '_dict':{'a':'b'},
                               '__dict':{'a':'b'}}}
    cookiecutter_dict = prompt_for

# Generated at 2022-06-22 12:27:19.485203
# Unit test for function read_user_choice
def test_read_user_choice():
    my_list = ['A', 'B', 'C']
    user_choice = read_user_choice('test', my_list)
    assert user_choice in my_list

# Generated at 2022-06-22 12:27:33.258396
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Test the prompt_for_config function."""
    context = {
        'cookiecutter': {
            'project_name': 'Cookiecutter',
        }
    }

    context = prompt_for_config(context, no_input=True)
    assert context['project_name'] == 'Cookiecutter'

# Generated at 2022-06-22 12:27:44.200612
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Test the prompt_for_config function."""
    # Get the fixture context, which is basically cookiecutter.json as a dict
    from cookiecutter import fixtures

    # Let's add a list and a dict to our context and then render them
    context = fixtures.context()
    # A basic list
    context['cookiecutter']['list_var'] = ['foo', 'bar', 'baz']
    # A list with a raw value
    context['cookiecutter']['list_var_2'] = [
        'foo', 'bar', 'baz', '{{ cookiecutter.hello }}'
    ]
    # A more complex list with a raw value

# Generated at 2022-06-22 12:27:52.041651
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:28:02.010381
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:28:05.568837
# Unit test for function prompt_for_config
def test_prompt_for_config():
    from cookiecutter.main import cookiecutter

    context = cookiecutter('tests/fake-repo-tmpl')

    # This should not raise an exception
    prompt_for_config(context, no_input=True)

# Generated at 2022-06-22 12:28:17.647702
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {
        "cookiecutter": {
            "project_name": "{{ cookiecutter.project_name_short.replace('_', ' ').title() }}",
            "project_name_short": "awesome_lib",
            "author_name": "David Fischer",
            "email": "djfische@example.com",
            "_copy_without_render": ["CHANGELOG.rst", "build_docs.py"],
            "__version__": "{{ cookiecutter.release_date.strftime('%Y.%m.%d') }}",
            "release_date": "{{ cookiecutter.year }}-{{ cookiecutter.month }}-{{ cookiecutter.day }}",
        }
    }
    cookiecutter_dict = prompt_for_config(context)
    assert cookiecutter_

# Generated at 2022-06-22 12:28:27.989001
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:28:39.663471
# Unit test for function prompt_for_config
def test_prompt_for_config():
    # Test 1
    context = {
        'cookiecutter': {
            'project_name': 'Test Project',
            'repo_name': '{{ cookiecutter.project_name.replace(" ", "_") }}',
            'package_name': '{{ cookiecutter.repo_name.replace("-", "_") }}',
            '_template': {
                'source': 'https://github.com/Cookiecutter/'
            },
            '__version__': '1.0.0'
        }
    }
    cookiecutter_dict = prompt_for_config(context, no_input=True)

# Generated at 2022-06-22 12:28:50.962290
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {'cookiecutter': {
        'project_name': 'TestName',
        'project_description': 'test project description',
        'author_name': 'testauthor',
        'author_email': 'testauthor@test.com',
        'version': '0.1.0',
        'license': 'Apache-2.0',
        'maintainer': 'maintainer',
    }}

    user_config = prompt_for_config(context, True)
    # check if the config is created

# Generated at 2022-06-22 12:28:57.931088
# Unit test for function prompt_for_config
def test_prompt_for_config():
    # Example from pytest
    context = {
        'cookiecutter': {
            'project_name': '{{ cookiecutter.full_name.replace(" ", "_") | lower }}',
            'author': '{{ cookiecutter.full_name }}',
            'email': '{{ cookiecutter.email }}',
            'full_name': 'Jannis Leidel',
            'email': 'jannis@leidel.info',
        }
    }

    result = prompt_for_config(context, no_input=True)
    assert result == {
        'project_name': 'jannis_leidel',
        'author': 'Jannis Leidel',
        'email': 'jannis@leidel.info',
        'full_name': 'Jannis Leidel',
    }

# Generated at 2022-06-22 12:29:08.860853
# Unit test for function prompt_for_config
def test_prompt_for_config():
    # Test with empty context
    context = {}
    cookiecutter_dict = prompt_for_config(context)
    assert cookiecutter_dict == {}

    # Test with None as context entry
    context['cookiecutter'] = {'key': None}
    cookiecutter_dict = prompt_for_config(context)
    assert cookiecutter_dict == {'key': None}

    # Test with integer as context entry
    context['cookiecutter'] = {'key': 1}
    cookiecutter_dict = prompt_for_config(context)
    assert cookiecutter_dict == {'key': '1'}

    # Test with nested dict as context entry
    context['cookiecutter'] = {'key': {'nested_key': 1}}
    cookiecutter_dict = prompt_for_config(context)
   

# Generated at 2022-06-22 12:29:19.282880
# Unit test for function prompt_for_config
def test_prompt_for_config():
    from cookiecutter.generate import generate_context

    template_dir = 'tests/test-project-tmpl/'
    ctx = generate_context(template_dir, default_context=True)

    result = prompt_for_config(ctx)

    assert result['project_name'] == 'Cookiecutter'
    assert result['repo_name'] == 'cookiecutter-cookiecutter'
    assert result['package_name'] == 'cookiecutter'
    assert result['version'] == '0.1.0'
    assert result['description'] == 'A command-line utility that creates projects from project templates'
    assert result['open_source_license'] == 'MIT'
    assert result['author_name'] == 'Audrey Roy Greenfeld'
    assert result['email'] == 'audreyr@example.com'

# Generated at 2022-06-22 12:29:23.787454
# Unit test for function prompt_for_config
def test_prompt_for_config():
    cookiecutter_dict = prompt_for_config({'cookiecutter': {'project_name': 'test', '_template': {'test': 'test'}}}, True)
    assert cookiecutter_dict['project_name'] == 'test'

test_prompt_for_config()

# Generated at 2022-06-22 12:29:34.343294
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = dict(
        cookiecutter={
            'project_name': '{{ cookiecutter.project_slug.upper() }}',
            'project_slug': 'myFakeProject',
            'base_directory': '{{ cookiecutter.project_slug.lower() }}',
            'version': '0.1.0',
        }
    )

    cookiecutter_dict = prompt_for_config(context, no_input=True)

    expected_result = {'project_name': 'MYFAKEPROJECT',
                       'project_slug': 'myFakeProject',
                       'base_directory': 'myfakeproject',
                       'version': '0.1.0'}

    assert expected_result == cookiecutter_dict



# Generated at 2022-06-22 12:29:45.937489
# Unit test for function read_user_dict
def test_read_user_dict():
    # 1. Run the test case when there is default value and user not input
    test_default_value = {'a': 1, 'b': 'default'}
    test_user_value = ''
    result = read_user_dict('test', test_default_value)
    assert result == test_default_value

    # 2. Run the test case when there is default value and user input
    test_default_value = {'a': 1, 'b': 'default'}
    test_user_value = {'a': 2, 'b': 'user'}
    result = read_user_dict('test', test_default_value)
    assert result == test_user_value

    # 3. Run the test case when there is not default value
    test_default_value = {'a': 1, 'b': 'default'}


# Generated at 2022-06-22 12:29:56.166136
# Unit test for function read_user_dict
def test_read_user_dict():
    key = 'project_name'
    default_value = 'Cookiecutter'
    # dictionary with the same key and value
    user_value = {'project_name':'Cookiecutter'}
    assert read_user_dict(key, default_value) == user_value
    # dictionary with the same key and empty value
    user_value = {'project_name':''}
    assert read_user_dict(key, default_value) == user_value
    # dictionary with the same key and a different value
    user_value = {'project_name':'CookieCutter'}
    assert read_user_dict(key, default_value) == user_value
    # dictionary with the same key and a None value
    user_value = {'project_name':None}

# Generated at 2022-06-22 12:30:00.092916
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context_to_test = {
        "cookiecutter": {
            "project_slug": "{{ cookiecutter.repo_name.lower().replace('-', '_') }}",
            "repo_name": "TestApp"
        }
    }
    cookiecutter_dict = prompt_for_config(context=context_to_test, no_input=True)
    assert cookiecutter_dict["project_slug"] == "testapp"

# Generated at 2022-06-22 12:30:04.782881
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {
        'cookiecutter': {
            'full_name': 'Noah',
        }
    }
    cookiecutter_dict = prompt_for_config(context, True)
    assert cookiecutter_dict['full_name'] == 'Noah'



# Generated at 2022-06-22 12:30:10.535342
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Test prompt_for_config function."""
    cookiecutter_dict = OrderedDict([])

# Generated at 2022-06-22 12:30:18.239677
# Unit test for function render_variable
def test_render_variable():
    assert "test" == render_variable(StrictEnvironment(), "test", {})
    assert 5 == render_variable(StrictEnvironment(), 5, {})
    assert [] == render_variable(StrictEnvironment(), [], {})
    assert [1, 2] == render_variable(StrictEnvironment(), [1, 2], {})
    assert {} == render_variable(StrictEnvironment(), {}, {})
    assert {"a": 1} == render_variable(StrictEnvironment(), {"a": 1}, {})

    # Checking for special `cookiecutter` variable
    cookiecutter_dict = {"project_name": 1}
    assert {"project_name": 1} == render_variable(StrictEnvironment(), cookiecutter_dict, cookiecutter_dict)

    # Checking for special boolean `no_input` variable

# Generated at 2022-06-22 12:30:43.692960
# Unit test for function read_user_dict
def test_read_user_dict():
    from cookiecutter import utils
    test_context_dict = {
        'company_name': 'ACME',
        'comma_in_field': 'B,C',
        'company_names': {
            '__test_field_dict': {
                'test_dict': {
                    'test_field': 'test_value'
                }
            }
        }
    }
    user_dict = read_user_dict('company_names', test_context_dict['company_names'])
    assert user_dict == test_context_dict['company_names'], 'Dictionary input has not been accepted'

    # Unit test for function read_user_variable
    user_variable = read_user_variable('company_name', 'ACME')
    assert user_variable == 'ACME', 'User input has not been accepted'

# Generated at 2022-06-22 12:30:54.737065
# Unit test for function prompt_for_config
def test_prompt_for_config():

    from .main import load_config_file
    from .main import load_extra_context
    from .main import prompt_config

    context = load_config_file("tests/fake-repo-pre/")
    extra_context = load_extra_context("", context.get("cookiecutter"))

    context["cookiecutter"].update(extra_context)
    cookiecutter_dict = prompt_for_config(context)

    assert isinstance(cookiecutter_dict, OrderedDict)
    assert "project_name" in cookiecutter_dict
    assert "project_slug" in cookiecutter_dict
    assert "release_date" in cookiecutter_dict
    assert "project_short_description" in cookiecutter_dict

# Generated at 2022-06-22 12:30:59.661571
# Unit test for function render_variable
def test_render_variable():
    context = {'cookiecutter': {'project_name': "Peanut Butter Cookie"}}
    env = StrictEnvironment(context=context)
    key = 'repo_name'
    raw = '{{ cookiecutter.project_name.replace(" ", "_") }}'
    cookiecutter_dict = {key: render_variable(env, raw, context)}
    assert cookiecutter_dict[key] == "Peanut_Butter_Cookie"


# Generated at 2022-06-22 12:31:09.205501
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {
        'cookiecutter': {
            'project_name': 'Cookiecutter Test Project',
            'project_slug': 'cookiecutter-test-project',
            'open_source_license': 'MIT license',
            'year': '2018',
            'full_name': 'Your Name',
            'email': 'you@example.com',
        }
    }

    cookiecutter_dict = prompt_for_config(context, no_input=True)

    assert cookiecutter_dict['project_name'] == 'Cookiecutter Test Project'
    assert cookiecutter_dict['project_slug'] == 'cookiecutter-test-project'
    assert cookiecutter_dict['open_source_license'] == 'MIT license'
    assert cookiecutter_dict['year'] == '2018'
   

# Generated at 2022-06-22 12:31:17.781738
# Unit test for function render_variable
def test_render_variable():
    # source context
    context = {
        'cookiecutter': {
            'testvar1': 'blue',
            'testvar2': 'red',
            'testvar3': '{{ cookiecutter.testvar1 }}',
            'testvar4': '{{ cookiecutter.testvar2 }}',
            'testvar5': '{{ cookiecutter.testvar4 }}',
            'testvar6': '{% if cookiecutter.testvar5 == "red" %}RED{% endif %}',
            'testvar7': ["a", "b", "c"],
            'testvar8': {"0": "a", "1": "b", "2": "c"}
        }
    }

    # test for simple variable
    raw = '{{ cookiecutter.testvar1 }}'

# Generated at 2022-06-22 12:31:20.056218
# Unit test for function prompt_for_config
def test_prompt_for_config():

    d = {'cookiecutter': {'b': '2', 'a': '1'}}
    answer = {'a': '1', 'b': '2'}

    assert prompt_for_config(d, no_input=True) == answer



# Generated at 2022-06-22 12:31:20.705190
# Unit test for function prompt_for_config
def test_prompt_for_config():
    pass

# Generated at 2022-06-22 12:31:31.977535
# Unit test for function prompt_for_config
def test_prompt_for_config():
    # TODO: fix this test and then uncomment this
    # from pytest_cookies.plugin import assert_files_equal
    import os
    from cookiecutter.environment import StrictEnvironment


# Generated at 2022-06-22 12:31:43.524037
# Unit test for function prompt_for_config
def test_prompt_for_config():
    from cookiecutter.main import cookiecutter


# Generated at 2022-06-22 12:31:55.125032
# Unit test for function prompt_for_config
def test_prompt_for_config():
    from cookiecutter.environment import StrictEnvironment
    from cookiecutter.main import cookiecutter
    from click.testing import CliRunner
    import os

    # Assert default value is used
    defaults = {
        'full_name': 'Firstname Lastname',
    }
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(
            cookiecutter, 'tests/test-cookiecutter-prompt/', '--no-input'
        )
        assert result.exit_code == 0
        assert os.path.exists('Firstname-Lastname')

    defaults = {
        'full_name': 'Firstname Lastname',
        'email': 'me@example.com',
    }
    runner = CliRunner()

# Generated at 2022-06-22 12:32:22.242917
# Unit test for function prompt_for_config
def test_prompt_for_config():
    # The following is a subset of the real context
    context = {
        "cookiecutter": {
            "app_name": "MyApp",
            "app_description": "A simple app",
            "app_version": "0.1.0",
            "app_license": "BSD",
            "github_repository": "{{ cookiecutter.app_name.replace(' ', '') }}",
            "open_source_license": "{{ cookiecutter.app_license }}",
            "author_name": "Your name",
            "author_email": "your.name@example.com",
            "requires_python": ">=3.6",
            "__fake_list_variable": [1, 2, 3],
        }
    }


# Generated at 2022-06-22 12:32:25.896815
# Unit test for function read_user_dict
def test_read_user_dict():
    var_name = 'test_dict'
    default_value = {'a': 'b', 'c': 'd'}
    user_dict = read_user_dict(var_name, default_value)
    assert user_dict == default_value

# Generated at 2022-06-22 12:32:34.381252
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:32:40.873071
# Unit test for function render_variable
def test_render_variable():
    env = StrictEnvironment()
    template = "{{ cookiecutter.project_name }} is an {{ cookiecutter.project_slug }}"
    rendered_template = render_variable(
        env,
        template,
        {
            "project_name": "Peanut Butter Cookie",
            "project_slug": "awesome cookie",
        },
    )
    assert rendered_template == "Peanut Butter Cookie is an awesome cookie"

# Generated at 2022-06-22 12:32:45.903321
# Unit test for function process_json
def test_process_json():
    """Make sure the process_json function properly raises JSON errors."""

    user_value = "Whatever"
    user_dict = process_json(user_value)

    assert isinstance(user_dict, dict)

    user_value = "What"
    with pytest.raises(click.UsageError):
        user_dict = process_json(user_value)

# Generated at 2022-06-22 12:32:53.690745
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Unit test for function prompt_for_config
    """
    context = {
        'cookiecutter': {
            'project_name': 'CookieCutter',
            '_input_method': 'prompt',
            '_copy_without_render': [
                'doc/CONTRIBUTING.md',
                '.github/ISSUE_TEMPLATE.md',
                '.github/PULL_REQUEST_TEMPLATE.md',
            ]
        }
    }
    cookiecutter_dict = prompt_for_config(context)
    assert '_input_method' in cookiecutter_dict
    assert '_copy_without_render' in cookiecutter_dict
    assert 'project_name' in cookiecutter_dict

# Generated at 2022-06-22 12:33:03.097773
# Unit test for function render_variable
def test_render_variable():
    """Test basic rendering of a variable."""
    from jinja2 import Environment, DictLoader
    from cookiecutter.prompt import render_variable

    env = Environment(
        autoescape=False,
        loader=DictLoader({'fake': '{{ cookiecutter.foo }}'}),
    )
    next_variable = 'foo'
    default = 'bar'
    cookiecutter_dict = {next_variable: default}

    actual = render_variable(env, '{{ cookiecutter.foo }}', cookiecutter_dict)
    assert actual == default


# Unit tests for function prompt_for_config.

# Generated at 2022-06-22 12:33:14.521329
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:33:25.282274
# Unit test for function render_variable
def test_render_variable():
    """Test if render_variable is working as expected."""
    # Test replacing `cookiecutter.text` with context
    assert render_variable(
        StrictEnvironment(context={'cookiecutter': {'text': 'value'}}),
        '{{ cookiecutter.text }}',
        {}
    ) == 'value'

    # Test default value if `cookiecutter.text` is undefined in context
    assert render_variable(
        StrictEnvironment(),
        '{{ cookiecutter.text }}',
        {}
    ) == ''

    # Test replacing `cookiecutter.project_name.replace(" ", "_")` with context

# Generated at 2022-06-22 12:33:36.941574
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:33:57.832163
# Unit test for function process_json
def test_process_json():
    """Test the function process_json.
    """
    data = {"name" : "Test Data"}
    data_str = json.dumps(data)
    assert process_json(data_str) == data

# Generated at 2022-06-22 12:34:05.953647
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:34:12.905017
# Unit test for function prompt_for_config
def test_prompt_for_config():
    # TODO MJS Make this more robust
    if hasattr(prompt_for_config, 'test_called'):
        return
    else:
        setattr(prompt_for_config, 'test_called', True)

    import os
    import shutil
    import tempfile

    import yaml

    # Create a temporary test directory
    temp_dir = tempfile.mkdtemp()

    # Write fake cookiecutter.json file
    cookiefile = os.path.join(temp_dir, 'cookiecutter.json')
    fake_cookiefile = """
    {"cookiecutter": {"_template": {"description": "Fake template"}}}
    """
    with open(cookiefile, 'w') as fh:
        fh.write(fake_cookiefile)

    # Create a fake context with a dict

# Generated at 2022-06-22 12:34:18.501427
# Unit test for function process_json
def test_process_json():
    print('\nTesting process_json()')
    user_value = '{"a": 1, "b": 2}'
    expected_dict = OrderedDict({"a": 1, "b": 2})
    actual_dict = process_json(user_value)

    if expected_dict == actual_dict:
        print('PASSED: process_json() is working correctly')
    else:
        print('FAILED: process_json() is not working correctly')


# Generated at 2022-06-22 12:34:30.338193
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Unit test for function prompt_for_config"""