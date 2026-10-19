

# Generated at 2022-06-22 12:24:37.126606
# Unit test for function read_user_dict
def test_read_user_dict():
    dict1 = dict(key1='value1', key2='value2')
    dict2 = dict(key3='value3', key4='value4')

    dict_rep = json.dumps(dict(dict1, **dict2))
    dict_rep = dict_rep.replace('"', '\\"')

    user_input = click.prompt(
        'dict_rep', default='default', type=click.STRING, value_proc=process_json
    )

    assert dict_rep == user_input

# Generated at 2022-06-22 12:24:49.208801
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:25:00.095683
# Unit test for function process_json
def test_process_json():
    context = {
        'cookiecutter': {
            'my_var': "{{ cookiecutter.my_dict['my_key'] }}",
            'my_dict': {
                'my_key': "{{ cookiecutter.my_other_dict['my_other_key'] }}",
                'my_other_key': "{{ cookiecutter.my_var }}",
            },
            'my_other_dict': {
                'my_other_key': "{{ cookiecutter.my_dict['my_other_key'] }}",
            },
        }
    }
    cookiecutter_dict = prompt_for_config(context, no_input=False)

# Generated at 2022-06-22 12:25:11.205420
# Unit test for function process_json
def test_process_json():
    """Unit test function for function process_json()."""
    # Test basic JSON
    result = process_json('{"a": "b"}')
    assert result == {'a': 'b'}

    # Test JSON with number
    result = process_json('{"a": 2}')
    assert result == {'a': 2}

    # Test JSON with list
    result = process_json('{"a": [1,2,3]}')
    assert result == {'a': [1, 2, 3]}

    # Test JSON with dictionary
    result = process_json('{"a": {"x": "y"}}')
    assert result == {'a': {'x': 'y'}}

    # Test invalid JSON
    try:
        result = process_json('{"a": "b"')
    except:
        assert True
   

# Generated at 2022-06-22 12:25:19.502776
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """
    Test prompt_for_config function
    """


# Generated at 2022-06-22 12:25:31.531847
# Unit test for function prompt_for_config
def test_prompt_for_config():

    context = {
        'cookiecutter': {
            'full_name': 'Peter Pan',
            'email': 'peterpan@example.com',
            'github_username': 'pete',
            'project_name': 'flying',
            'project_slug': '{{ cookiecutter.project_name | lower }}',
            'release_date': '{{ cookiecutter.year }}-{{ cookiecutter.month }}-{{ cookiecutter.day }}',
            'year': '2019',
            'month': '01',
            'day': '01',
            'project_short_description': 'Take to the sky!',
            'version': '0.1.0'
        }
    }

# Generated at 2022-06-22 12:25:34.055295
# Unit test for function process_json
def test_process_json():
    test_value = '{"answer": 42}'
    assert process_json(test_value) == {"answer": 42}



# Generated at 2022-06-22 12:25:37.228633
# Unit test for function read_user_choice
def test_read_user_choice():
    var_name = 'my_var'
    options = [1, 2, 3]
    choice = read_user_choice(var_name, options)
    assert choice == 1



# Generated at 2022-06-22 12:25:44.218483
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {
        'cookiecutter': {
            'repo_name': 'repo_name',
            'project_name': 'project_name',
            'project_slug': '{{ cookiecutter.project_name.lower().replace(" ", "-") }}',
            'project_dir': '{{ cookiecutter.project_slug }}',
            'release_date': '2016-01-01'
        }
    }
    result = prompt_for_config(context, True)
    assert result['repo_name'] == 'repo_name'
    assert result['project_name'] == 'project_name'
    assert result['project_slug'] == 'project-name'
    assert result['project_dir'] == 'project-name'
    assert result['release_date'] == '2016-01-01'

# Generated at 2022-06-22 12:25:54.088141
# Unit test for function read_user_dict
def test_read_user_dict():
    var_name = "test_var"
    default_value = {"test_key":"test_value"}
    assert read_user_dict(var_name, default_value) == {"test_key":"test_value"}
    assert read_user_dict(var_name, default_value) == default_value
    assert read_user_dict(var_name, default_value) != {"test_key":"test_value", "test_key2":"test_value2"}
    assert read_user_dict(var_name, default_value) == {"test_key":"test_value", "test_key2":"test_value2"}
    assert read_user_dict(var_name, default_value) != {}

# Generated at 2022-06-22 12:26:10.682868
# Unit test for function render_variable
def test_render_variable():
    from cookiecutter.utils import rmtree
    from cookiecutter import generate
    from shutil import copytree
    from os import getcwd
    from os.path import join
    from pytest import raises

    source = 'tests/test-render-var/{{cookiecutter.var}}'
    dest = 'tests/test-render-var-result'
    copytree(source, dest)
    generate.generate_files(
        repo_dir=dest, context={'cookiecutter': {'var': "maxim"}, }
    )

    assert 'tests/test-render-var-result/file1'
    assert 'tests/test-render-var-result/file2'

    assert 'tests/test-render-var-result/dir1/dir11/file11'

# Generated at 2022-06-22 12:26:18.390311
# Unit test for function prompt_for_config
def test_prompt_for_config():
    test_context = {'cookiecutter': {'text': 'test',
                                     'numbers': [1, 2, 3],
                                     'dict': {'test':'test'},
                                     '__jinja_test': '{{ cookiecutter.text }}',
                                     '_test': 'This is a private variable'}, }

    config = prompt_for_config(test_context, no_input=True)
    assert config['text'] == 'test'
    assert config['numbers'] == [1, 2, 3]
    assert config['dict'] == {'test': 'test'}


# Generated at 2022-06-22 12:26:29.881625
# Unit test for function prompt_for_config
def test_prompt_for_config():
    # export PYTHONPATH=./
    import unittest
    from unittest.mock import patch

    from cookiecutter.main import cookiecutter

    class TestCase(unittest.TestCase):
        @classmethod
        def setUpClass(cls):
            pass

        def setUp(self):
            pass

        def tearDown(self):
            pass

        def test_prompt_for_config(self):
            test_data = {'cookiecutter': {
                'project_name': 'Test Project',
                'repo_name': '{{ cookiecutter.project_name.lower().replace(" ", "") }}'
            }}

            with patch('cookiecutter.config.read_user_variable') as mock_method:
                mock_method.return_value = 'Test Project'
                response

# Generated at 2022-06-22 12:26:40.916412
# Unit test for function prompt_for_config
def test_prompt_for_config():
    assert prompt_for_config({'cookiecutter': {'project_name': 'test'}}) == {
        'cookiecutter': {'project_name': 'test'},
    }

    assert prompt_for_config({'cookiecutter': {'project_slug': 'test_project'}}) == {
        'cookiecutter': {'project_slug': 'test_project'},
    }

    assert prompt_for_config({'cookiecutter': {'_template': '.'}}) == {
        'cookiecutter': {'_template': '.'},
    }


# Generated at 2022-06-22 12:26:50.594151
# Unit test for function prompt_for_config
def test_prompt_for_config():
    from cookiecutter.main import cookiecutter
    from jinja2.exceptions import UndefinedError
    from jinja2 import StrictUndefined
    from cookiecutter.environment import StrictEnvironment

    class TestEnvironment(StrictEnvironment):
        def get_template(self, template):
            if template == "":
                raise UndefinedError("")
            else:
                return super().get_template(template)

    cookiecutter_dict = prompt_for_config(
        {
            'cookiecutter': {
                'project_name': 'Cookiecutter-pypackage',
                'repo_name': '{{ cookiecutter.project_name.lower().replace("-", "_") }}',
            }
        },
        no_input=True,
    )

# Generated at 2022-06-22 12:26:52.745228
# Unit test for function process_json
def test_process_json():
    assert process_json('{"Key": "Value"}') == {"Key": "Value"}



# Generated at 2022-06-22 12:27:02.120411
# Unit test for function read_user_dict
def test_read_user_dict():
    arb_dict = {
        'name': 'val',
        'more': "{{cookiecutter.project_name}}"
    }
    # Return the given default w/o any processing
    assert(read_user_dict('question', arb_dict) == arb_dict)
    # Return the given default w/o any processing
    assert(read_user_dict('question', {'name':'val'}) == {'name':'val'})
    # Expected correct dict
    dict_string = '{"name": "val", "more": "Unit_Test"}'
    assert(read_user_dict('question', {'name':'val'}, dict_string) == {'name':'val', "more": "Unit_Test"})

# Generated at 2022-06-22 12:27:12.888842
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:27:19.564515
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:27:26.538812
# Unit test for function prompt_for_config
def test_prompt_for_config():
    print('---Start of test_prompt_for_config---')
    cookiecutter_dict = OrderedDict([])

# Generated at 2022-06-22 12:27:42.459533
# Unit test for function read_user_dict
def test_read_user_dict():
    # Check that a given default value works
    default = OrderedDict([('key', 'value')])
    assert read_user_dict('foo', default) == default

    # Check that a given default value works
    default = OrderedDict([('key', 'value')])
    assert read_user_dict('foo', default) == default

    # Check that a given default value is rendered
    env = StrictEnvironment(context={'project_name':'test_project_name'})
    default = OrderedDict([('key', '{{ cookiecutter.project_name }}')])
    cookiecutter_dict = OrderedDict()
    assert read_user_dict('foo', default) == {'key': 'test_project_name'}

    # Check that the default value is shown to the user
    # and is available as a

# Generated at 2022-06-22 12:27:46.277887
# Unit test for function read_user_dict
def test_read_user_dict():
    from click._compat import raw_input

    def _input(prompt: str):
        print(prompt)
        return "Jeeves"

    raw_input = _input
    read_user_dict("Test", "Test")

# Generated at 2022-06-22 12:27:53.128723
# Unit test for function read_user_dict
def test_read_user_dict():
    """Unittest for function read_user_dict"""

    error_dict = {'first': 'primary'}
    default_dict = {'first': 'primary', 'second': 'secondary', 'third': 'tertiary'}
    user_dict = {'first': 'primary', 'second': 'secondary'}

    assert read_user_dict('variable', error_dict) == error_dict
    assert read_user_dict('variable', default_dict) == default_dict

    # Test with string
    value = read_user_dict('variable', default_dict)
    assert isinstance(value, dict)
    assert value == user_dict

    # Test with dict
    value = read_user_dict('variable', json.dumps(default_dict))
    assert isinstance(value, dict)
    assert value == user_dict



# Generated at 2022-06-22 12:28:02.800711
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Verify functionality of prompt_for_config function."""
    cookiecutter_dict = {
    }

    context = {
        'cookiecutter': {
            '_copy_without_render': ['.gitignore'],
            'repo_name': 'myrepo',
            'full_name': '',
            'email': '',
            'github_username': '',
            'project_name': 'Custom Project',
            'project_slug': 'myproject',
            'project_short_description': 'An awesome Python project',
            'pypi_username': '',
            'version': '0.1.0',
            'use_pytest': True
        }
    }

    cookiecutter_dict = prompt_for_config(context, no_input=True)
    assert cookiecutter_dict

# Generated at 2022-06-22 12:28:14.691793
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:28:26.058946
# Unit test for function render_variable
def test_render_variable():
    '''This unit test is used to test render_variable() located within
    cookiecutter.prompt.py. This function is called when the user runs
    cookiecutter. It will return the rendered value for the default variable
    or raise an UndefinedVariableInTemplate exception.
    '''

    # Arrange
    context = {}
    context['cookiecutter'] = {
        'project_name': 'cookiecutter-pypackage',
        'owner': 'audreyr',
    }

    env = StrictEnvironment(context=context) # Assertion that this is a StrictEnvironment
    raw = '{{ cookiecutter.project_name.replace(" ", "-") }}' # String to be used for the raw var
    cookiecutter_dict = OrderedDict([])

    # Act

# Generated at 2022-06-22 12:28:29.107333
# Unit test for function render_variable
def test_render_variable():
    env = StrictEnvironment(context={})
    res = render_variable(env, '{{ some_var }}', cookiecutter={"some_var": "hello"})
    assert res == "hello"

# Generated at 2022-06-22 12:28:40.797480
# Unit test for function prompt_for_config
def test_prompt_for_config():
    from .config import DEFAULT_CONFIG
    from .repository import expand_abbreviations
    from .environment import StrictEnvironment
    from .exceptions import ConfigDoesNotExist
    import pprint
    import os
    import sys

    # Load the cookiecutter's config file
    try:
        default_config = expand_abbreviations(DEFAULT_CONFIG)
    except ConfigDoesNotExist:
        sys.stderr.write('\n')
        msg = "Default config file ({}) could not be found!\n"
        sys.stderr.write(msg.format(DEFAULT_CONFIG))
        sys.exit(1)

    env = StrictEnvironment(context=default_config)
    pprint.pprint(prompt_for_config(default_config))

# Generated at 2022-06-22 12:28:52.448418
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:29:04.375395
# Unit test for function prompt_for_config
def test_prompt_for_config():
    test_context = {
    "cookiecutter": {
        "project_name": "Cookiecutter Test Project",
        "repo_name": "{{ cookiecutter.project_name.replace(' ', '_').lower() }}",
        "select": [
            "value1",
            "value2",
            "value3"
        ],
        "dict": {
            "key": "value"
        },
        "defaultdict": {
            "key": "value"
        }
    }
    }
    config_result = prompt_for_config(test_context, True)


# Generated at 2022-06-22 12:29:19.861631
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:29:31.587352
# Unit test for function prompt_for_config
def test_prompt_for_config():
    from os import path
    from cookiecutter.main import cookiecutter

    # Create a temporary working dir for testing
    temp_test_dir = path.abspath('test_prompt_for_config')

    # Path to the test project we want to render
    project_dir = path.abspath('tests/files/test-project')

    # Call our function with a test file as argument
    result = prompt_for_config(project_dir, no_input=True)

    assert result['full_name'] == 'Your name'
    assert result['email'] == 'your@email.com'
    assert result['github_username'] == 'your-github-username'
    assert result['repo_name'] == 'your_repo'
    assert result['project_name'] == 'Test project'

# Generated at 2022-06-22 12:29:36.609491
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Test function prompt_for_config."""
    config = dict()
    config['cookiecutter'] = dict()

    config['cookiecutter']['project_name'] = 'Example project'
    config['cookiecutter']['author_name'] = 'Example name'
    config['cookiecutter']['github_org'] = 'Example org'

    config['cookiecutter']['project_name2'] = 'Example project2'
    config['cookiecutter']['author_name2'] = 'Example name2'
    config['cookiecutter']['github_org2'] = 'Example org2'

    config['cookiecutter']['_private_dict1'] = dict()
    config['cookiecutter']['_private_dict1']['a'] = 'A'

# Generated at 2022-06-22 12:29:47.170782
# Unit test for function prompt_for_config
def test_prompt_for_config():
    class TestException(Exception):
        pass


# Generated at 2022-06-22 12:29:57.374163
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Test prompt_for_config function."""
    context = {
        "cookiecutter": {
            "project_name": "Cookiecutter Awesome Project",
            "repo_name": "{{ cookiecutter.project_name.replace(' ', '_') }}",
            "author_name": "Your name",
            "epoch": 1496214503,
            "project_slug": "cookiecutter-awesome-project",
            "repo_slug": "cookiecutter_awesome_project",
            "project_short_description": "A short description of the project.",
            "__project_dir": "{{ cookiecutter.repo_slug }}",
            "pypi_username": "audreyr",
            "_copy_without_render": ["test.txt"],
        }
    }
    output

# Generated at 2022-06-22 12:30:03.125500
# Unit test for function prompt_for_config
def test_prompt_for_config():
    # TODO: Add more tests
    context = {'cookiecutter': {'full_name': 'Your Name'}}
    cookiecutter_dict = prompt_for_config(context, no_input=True)
    assert cookiecutter_dict['full_name'] == 'Your Name'



# Generated at 2022-06-22 12:30:14.098090
# Unit test for function process_json
def test_process_json():
    """Test conversion of user input to a JSON dict."""
    # "Simple" dictionary
    json_dict = process_json('{"my_var": "Hello World"}')

    assert json_dict == {
        'my_var': 'Hello World',
    }

    # Dictionary with several values
    json_dict = process_json(
        '{"my_var": "Hello World", "your_var": {"sub": "foobar"}}'
    )

    assert json_dict == {
        'my_var': 'Hello World',
        'your_var': {
            'sub': "foobar",
        },
    }

    # Test ordering of input and output
    json_dict = process_json('{"my_var": "Hello World", "a": 1, "b": 2}')


# Generated at 2022-06-22 12:30:26.124825
# Unit test for function render_variable
def test_render_variable():
    """Test that render_variable() works as expected"""
    from .main import DEFAULT_CONTEXT
    env = StrictEnvironment(context=DEFAULT_CONTEXT)

    cookiecutter_dict = OrderedDict([])
    cookiecutter_dict['project_name'] = 'First Project'

    user_response = render_variable(env, '{{ cookiecutter.project_name }}', cookiecutter_dict)
    assert user_response == 'First Project'

    user_response = render_variable(env, '{{ cookiecutter.project_name.upper() }}', cookiecutter_dict)
    assert user_response == 'FIRST PROJECT'

    user_response = render_variable(env, '{{ cookiecutter.fake_var.upper() }}', cookiecutter_dict)
    assert user_response is None

    user_

# Generated at 2022-06-22 12:30:34.517463
# Unit test for function process_json
def test_process_json():
    """Tests the process_json.

    This is called from ./tests/cli/test_new_project.py
    """
    input_user_value = '{"a": 1, "b": true, "c": "3"}'
    expected_output = {"a": 1, "b": True, "c": "3"}
    # Please see https://click.palletsprojects.com/en/7.x/api/#click.prompt
    assert process_json(input_user_value) == expected_output

# Generated at 2022-06-22 12:30:44.161237
# Unit test for function process_json
def test_process_json():
    """Ensure that process_json works with a valid JSON input."""
    context = {'cookiecutter': {'test_var': '{"foo": "bar"}'}}
    env = StrictEnvironment(context=context)
    rendered_context = env.from_string(context['cookiecutter']['test_var']).render()
    assert process_json(rendered_context) == {'foo': 'bar'}

    context = {'cookiecutter': {'test_var': '[{"foo": "bar"}]'}}
    env = StrictEnvironment(context=context)
    rendered_context = env.from_string(context['cookiecutter']['test_var']).render()
    assert process_json(rendered_context) == [{'foo': 'bar'}]



# Generated at 2022-06-22 12:31:02.715231
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Test the function prompt_for_config."""
    context = {
        "cookiecutter": {
            "project_name": "A",
            "project_slug": "a",
            "project_dir": "a",
            "project_short_description": "A.",
            "select_license": "BSD",
            "author_name": "A",
            "email": "a@a.com",
            "github_username": "a",
            "repo_name": "a",
            "repo_description": "A project.",
            "domain_name": "example.com",
            "version": "0.1.0",
            "timezone": "UTC",
            "pypi_username": "a",
            "ci_vendor": "travis",
        }
    }
    cookie

# Generated at 2022-06-22 12:31:11.726090
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Unit test for function prompt_for_config
    """
    context = {
        "cookiecutter": {
            "project_name": "Example project",
            "year": "2019",
            "__key1": "{% raw %}{% for key, value in cookiecutter.items() if key.startswith('project_') %}{% endfor %}{% endraw %}",
            "__key2": "${{ year }}",
            "project_name2": {
                "default": "example_project",
                "description": "Name of the project"
            }
        }}
    cookiecutter_dict = prompt_for_config(context, no_input=True)
    assert cookiecutter_dict['project_name'] == 'Example project'
    assert cookiecutter_dict['year'] == '2019'

# Generated at 2022-06-22 12:31:23.337020
# Unit test for function read_user_dict
def test_read_user_dict():
    user_value = '{"key": "value"}'
    user_dict = process_json(user_value)
    assert isinstance(user_dict, dict)
    assert user_dict['key'] == 'value'

    user_value = """{
        "key": "value",
        "key2": {"key3": "value"},
        "key4": ["value1", "value2"],
        "key5": [{"key6": "value3"}, {"key7": "value4"}]
    }"""
    user_dict = process_json(user_value)
    assert isinstance(user_dict, dict)
    assert isinstance(user_dict['key2'], dict)
    assert user_dict['key2']['key3'] == "value"

# Generated at 2022-06-22 12:31:24.867915
# Unit test for function read_user_dict
def test_read_user_dict():
    assert read_user_dict('input', {'input':'myinput'}) == {'input':'myinput'}

# Generated at 2022-06-22 12:31:28.279806
# Unit test for function prompt_for_config
def test_prompt_for_config():

    print('Testing test_prompt_for_config()...')
    print('Testing test_prompt_for_config()...')
    print('Testing test_prompt_for_config()...')
    print('Testing test_prompt_for_config()...')
    print('Testing test_prompt_for_config()...')


if __name__ == '__main__':
    test_prompt_for_config()

# Generated at 2022-06-22 12:31:38.469012
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:31:49.530968
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:31:57.444936
# Unit test for function prompt_for_config
def test_prompt_for_config():
    cookiecutter_dict = {'cookiecutter':{'repo_name':'Super Awesome Project', 'author_name':'Audrey Roy', 'google_analytics_id':'UA-7777777-7', 'select_license':'MIT', '_template':{'cookiecutter':{'repo_name':'Super Awesome Project', 'author_name':'Audrey Roy', 'google_analytics_id':'UA-7777777-7', 'select_license':'MIT'}}}}
    function_result = prompt_for_config(cookiecutter_dict)
    assert function_result == cookiecutter_dict

# Generated at 2022-06-22 12:32:02.786544
# Unit test for function process_json
def test_process_json():
    process_json('{"name": "somename"}')
    process_json('{"name": "somename", "repo_name": "somerepo"}')
    process_json('{"name": "somename", "repo_name": "somerepo", "repo_url": "somerepo"}')
    process_json('{"name": "somename", "repo_name": "somerepo", "repo_url": "somerepo", "project_slug": "somerepo"}')


# Generated at 2022-06-22 12:32:06.878852
# Unit test for function prompt_for_config
def test_prompt_for_config():
    from cookiecutter.main import cookiecutter

    context = cookiecutter(
        'tests/fake-repo-templated',
        no_input=False,
        extra_context={'project_name': 'Foo Bar'},
    )
    assert context['project_name'] == 'Foo Bar'

# Generated at 2022-06-22 12:32:24.976079
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Unit test prompt_for_config() function."""
    context = {'cookiecutter': {'key': 'value'}}
    print(prompt_for_config(context, no_input=True))

# Generated at 2022-06-22 12:32:31.558819
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """ Unit test for function prompt_for_config()."""
    from cookiecutter.prompt import prompt_for_config
    from click.testing import CliRunner
    from cookiecutter.main import cookiecutter
    from cookiecutter import __version__

    # check if prompt_for_config(context, no_input=False) works correctly
    context = {
      'cookiecutter': {
        'full_name': 'Your full name',
        'email': 'Your email address',
        'project_name': 'Your project name'
      }
    }
    runner = CliRunner()
    result = runner.invoke(cookiecutter, ['-v'])
    assert result.exit_code == 0
    assert __version__ in result.output


# Generated at 2022-06-22 12:32:42.951829
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:32:51.675280
# Unit test for function process_json
def test_process_json():
    """Tests the process_json function."""
    # Test with a valid JSON dict
    json_dict_valid = {
        'name': 'joe',
        'age': 15,
        'grade': 'A',
        'class_data': {
            'student_data': [
                {
                    'student': 'guy',
                }
            ]
        }
    }
    json_str_valid = json.dumps(json_dict_valid, indent=4)
    json_dict_valid = process_json(json_str_valid)

    # Test with a valid JSON list

# Generated at 2022-06-22 12:33:03.523469
# Unit test for function read_user_dict
def test_read_user_dict():
    """Test processing of user-provided dictionaries."""
    import click
    from click.testing import CliRunner

    runner = CliRunner()

    context = {
        'cookiecutter': {
            'company_name': 'Big Enterprise'
        }
    }

    # Single key, single value

# Generated at 2022-06-22 12:33:15.013325
# Unit test for function prompt_for_config
def test_prompt_for_config():
    from .config import DEFAULT_CONFIG
    cookiecutter_dict = prompt_for_config(DEFAULT_CONFIG, no_input=True)
    assert cookiecutter_dict['project_name'] == 'Cookiecutter Test Project'
    assert cookiecutter_dict['repo_name'] == 'cookiecutter-test-project'
    assert cookiecutter_dict['project_slug'] == 'cookiecutter_test_project'
    assert cookiecutter_dict['project_short_description'] == 'A short description of the project.'
    assert cookiecutter_dict['pypi_username'] == 'example'
    assert cookiecutter_dict['full_name'] == 'Your Name'
    assert cookiecutter_dict['email'] == 'example@example.com'
    assert cookiecutter_dict['github_username']

# Generated at 2022-06-22 12:33:24.682777
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = dict(
        cookiecutter=dict(
            repo_name='Dummy',
            full_name='Dummy Author',
            email='dummy@example.com',
            description='Some description',
            domain_name='dummy.example.com',
            version='0.1.0',
            timezone='UTC',
            use_pycharm=True,
            open_source_license='MIT',
            use_docker=True,
            command_line_interface='click',
            use_pytest=False,
            create_author_file=False,
            year=2019,
        ),
    )
    assert prompt_for_config(context, no_input=True) == context['cookiecutter']

# Generated at 2022-06-22 12:33:30.334371
# Unit test for function read_user_dict
def test_read_user_dict():
    var_name = 'should_create_config_file'
    default_value = {'config': {'name': 'configuration'}}
    user_input = '{"config": {"name": "configuration"}}'
    assert read_user_dict(var_name, default_value) == read_user_dict(var_name, default_value)

# Generated at 2022-06-22 12:33:41.009408
# Unit test for function read_user_choice
def test_read_user_choice():

    var_name = "test_var"
    options = ["A", "B", "C"]
    expected_result = "A"
    # Due to the specification of "read_user_choice" this test case can only be executed
    # with a human doing the input. It is still tested agains a "hard-coded" input.
    user_input = "1"
    # This is a mock object of the click.prompt function, which is called in the function
    # "read_user_choice". The necessary input is stored in the variable "user_input".
    def input(question, default, type, show_choices):
        return user_input

    # The original click.prompt function is swapped out with the newly created mock object.
    original_prompt = click.prompt
    click.prompt = input

    assert expected_result

# Generated at 2022-06-22 12:33:42.225974
# Unit test for function read_user_dict
def test_read_user_dict():
    assert read_user_dict('Foo', {'bar': 'spam'}) == {'bar': 'spam'}

# Generated at 2022-06-22 12:34:21.001010
# Unit test for function prompt_for_config