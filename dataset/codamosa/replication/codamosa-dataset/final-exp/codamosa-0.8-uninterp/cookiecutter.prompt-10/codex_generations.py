

# Generated at 2022-06-22 12:24:51.791856
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Unit test for function prompt_for_config"""
    context = {
        "cookiecutter": {
            "project_name": "Test",
            "_copy_without_render": ["foobar"],
            "__private_type_var": "secret stuff",
            "var_with_default": "default value",
            "var_without_default": "",
            "var_choice": ["First Choice", "Second Choice"],
            "var_with_complex_default": "{{ cookiecutter.var_without_default }}",
            "var_dict": {"one": 1, "two": 2},
        }
    }

    cookiecutter_dict = prompt_for_config(context)
    assert cookiecutter_dict["project_name"] == "Test"

# Generated at 2022-06-22 12:25:02.095163
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Unit test for function prompt_for_config"""
    context = {
        'cookiecutter': {
            'project_name': 'My project',
            'repo_name': '{{ cookiecutter.project_name.lower().replace(" ", "_") }}',
            'license': 'MIT',
            'python_interpreter': 'python2',
            '_template': {
                'url': 'https://github.com/foo',
                'revision': 'master',
                'verbose': 'yes',
                '__static': {'spam': 'foo', 'ham': 'bar'},
            },
            'spam': 'foo',
            'ham': 'bar',
            'extras': 'eggs',
        },
        'default_context': {'answer': 42},
    }
    env = Strict

# Generated at 2022-06-22 12:25:12.463209
# Unit test for function prompt_for_config
def test_prompt_for_config():
    import os
    import tempfile

    from cookiecutter import generate
    from cookiecutter.repository import determine_repo_dir

    # Make a temporary working directory
    build_dir = tempfile.mkdtemp()

    # Make a fake cookiecutter.json file
    repo_dir = build_dir + '/fake-repo'
    os.makedirs(repo_dir)

    json_file = repo_dir + '/cookiecutter.json'
    with open(json_file, 'w') as f:
        f.write(
            """
            {"_extra_context": "facts = {'ip_address': '8.8.8.8'}", "project_name": "{{ cookiecutter.ip_address }}"}
            """
        )


# Generated at 2022-06-22 12:25:20.352004
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Check that a prompt is created correctly."""
    # Setup
    context = {
        "cookiecutter": {
            "project_name": "My Project",
            "author_name": "Your Name",
            "email": "your@email.com",
            "year": "2015",
            "domain_name": "example.com",
            "repo_name": "{{ cookiecutter.project_name.replace(' ', '_') }}",
            "description": "A short description of the project.",
            "version": "0.1.0",
        }
    }
    # Exercise
    result = prompt_for_config(context=context, no_input=True)
    # Verify
    assert result["author_name"] == "Your Name"
    assert result["repo_name"] == "My_Project"

# Generated at 2022-06-22 12:25:22.511450
# Unit test for function process_json
def test_process_json():
    assert {'key': 'value'} == process_json(json.dumps({'key': 'value'}))



# Generated at 2022-06-22 12:25:28.202819
# Unit test for function prompt_choice_for_config
def test_prompt_choice_for_config():
    context = {}
    context["cookiecutter"] = {"choice_var": ["choice1", "choice2"]}
    env = StrictEnvironment(context=context)
    choices = prompt_choice_for_config(context, env, "choice_var", ["choice1", "choice2"], True)
    assert(choices == ["choice1", "choice2"])

# Generated at 2022-06-22 12:25:30.752439
# Unit test for function read_user_dict
def test_read_user_dict():
    """
    Unit test for function read_user_dict
    """
    assert "abcd" == read_user_dict("Enter the value: ", "abcd")


# Generated at 2022-06-22 12:25:41.024304
# Unit test for function process_json
def test_process_json():
    assert process_json('{"a": 1, "b": 2}') == {"a": 1, "b": 2}
    assert process_json('{"a": 1, "b": 2, "c": [3, 4, 5]}') == {"a": 1, "b": 2, "c": [3, 4, 5]}
    assert process_json('{"a": "b"}') == {"a": "b"}
    assert process_json('{"a": true}') == {"a": True}
    assert process_json('{"a": false}') == {"a": False}
    assert process_json('{"a": null}') == {"a": None}

# Generated at 2022-06-22 12:25:49.924354
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Test function prompt_for_config."""
    from cookiecutter.main import cookiecutter

    project_dir = cookiecutter(
        'tests/test-dataclasses/', no_input=True, output_dir='tests/fake-repo-pre/')
    assert project_dir == 'tests/fake-repo-pre/'
    project_dir = cookiecutter(
        'tests/test-dataclasses/', no_input=False, output_dir='tests/fake-repo-post/')
    assert project_dir == 'tests/fake-repo-post/'

# Generated at 2022-06-22 12:25:57.987878
# Unit test for function process_json
def test_process_json():
    assert process_json('{}') == {}
    assert process_json('{"foo": "bar"') == {"foo": "bar"}
    assert process_json('["foo", "bar"]') == ["foo", "bar"]
    assert process_json('{"foo": {"bar": "baz"}}') == {"foo": {"bar": "baz"}}
    assert process_json('{"foo": [1, 2, 3]}') == {"foo": [1, 2, 3]}
    assert process_json('{"foo": {"bar": {"baz": [1, 2, 3]}}}') == {"foo": {"bar": {"baz": [1, 2, 3]}}}

# Generated at 2022-06-22 12:26:06.902316
# Unit test for function read_user_dict
def test_read_user_dict():
    user_dict = read_user_dict('test', {'key': 'value'})
    assert user_dict == {'key': 'value'}
    user_dict = read_user_dict('test', {'key': 'value', 'key2': 'value2'})
    assert user_dict == {'key': 'value', 'key2': 'value2'}

# Generated at 2022-06-22 12:26:18.436607
# Unit test for function prompt_for_config
def test_prompt_for_config():
    from cookiecutter.prompt import prompt_for_config


# Generated at 2022-06-22 12:26:22.696233
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Test the prompt_for_config function."""
    cookiecutter_dict = prompt_for_config({})
    assert isinstance(cookiecutter_dict, OrderedDict)
    assert cookiecutter_dict == OrderedDict()

# Generated at 2022-06-22 12:26:30.937505
# Unit test for function read_user_dict
def test_read_user_dict():
	context = {
		'cookiecutter': {
			'custom': {
				'config': {
					'greeting': {'hello': 'world'}
				}
			}
		}
	}

	default_val = {'greeting': {'hello': 'world'}}
	user_dict = read_user_dict('custom', default_val)
	assert user_dict
	assert context['cookiecutter']['custom']['config']['greeting'] == user_dict['greeting']

# Generated at 2022-06-22 12:26:41.033985
# Unit test for function render_variable
def test_render_variable():
    """Test the rendering of a variable."""
    from jinja2 import Environment, FileSystemLoader


# Generated at 2022-06-22 12:26:50.720389
# Unit test for function read_user_dict
def test_read_user_dict():
    """Unit test for function read_user_dict"""
    dict_var_name = "test"
    dict_default_value = {'test': 'test'}
    assert read_user_dict(dict_var_name, dict_default_value) == {'test': 'test'}
    dict_user_return = '{"test": "test"}'
    import getpass
    user = getpass.getuser()
    dict_interactive_return = '{"test": "test", "test_add": {"test_sub": "test_sub"}}'
    dict_interactive_return2 = '{"test": "test", "test_add": {"test_sub": "test_sub", "test_sub_add": "test_sub_add"}}'

# Generated at 2022-06-22 12:26:59.545910
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:27:03.431572
# Unit test for function read_user_dict
def test_read_user_dict():
    varName = 'test'
    default = {"test": "default"}
    assert read_user_dict(varName, default) == default

    user_input = '{"test": "test"}'
    expected = {"test": "test"}
    assert read_user_dict(varName, default) == expected

# Generated at 2022-06-22 12:27:12.777253
# Unit test for function render_variable
def test_render_variable():
    """Test for function render_variable
    """
    from cookiecutter.render import render_variable, UndefinedVariableInTemplate
    from jinja2 import Environment, Template
    import os

    dir_path = os.path.dirname(os.path.realpath(__file__))
    tests_path = os.path.join(dir_path, 'tests')
    json_file = os.path.join(tests_path, 'test_render_variable.json')

    with open(json_file) as json_data:
        context = json.load(json_data)

    env = Environment(context=context)

    # Test value None is returned if passed None
    assert render_variable(env, None, None) is None

    # Test value str is returned if passed str
    assert render_variable(env, 'foo', None)

# Generated at 2022-06-22 12:27:24.251676
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Assert that prompt_for_config is ok."""
    from cookiecutter import main
    from cookiecutter import utils
    from jinja2.exceptions import UndefinedError

    # Create dummy template for testing
    utils.make_sure_path_exists('fake-template')
    repo_dir = 'fake-template'
    template_dir = '{{ cookiecutter.repo_name }}'
    project_dir = '{{ cookiecutter.repo_name }}'
    repo_name = 'mock-repo-name'
    mock_project_name = 'mock-project-name'
    mock_project_slug = 'mock-project-slug'
    # Update file in 'fake-template'
    utils.work_in(repo_dir)

# Generated at 2022-06-22 12:27:45.752778
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Unit test for function prompt_for_config."""

# Generated at 2022-06-22 12:27:57.160606
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Unit test for function prompt_for_config"""
    # Execute the function with no_input set to True

# Generated at 2022-06-22 12:28:08.730903
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:28:20.556998
# Unit test for function prompt_for_config
def test_prompt_for_config():
    test_context={
        'cookiecutter': {
            'project_name': "Peanut Butter",
            '_template': {},
            'select_list': ['first', 'second'],
            '_select_double': ['first', 'second'],
            '_select_double_default': 'second',
            'test_dict': {'test_key': 'test_value'}
        }
    }
    result = prompt_for_config(test_context)
    assert result == {
        'project_name': "Peanut Butter",
        '_template': {},
        'select_list': 'first',
        '_select_double': 'second',
        '_select_double_default': 'second',
        'test_dict': {'test_key': 'test_value'}
    }

# Generated at 2022-06-22 12:28:29.403798
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Test function prompt_for_config"""
    context = {
    "cookiecutter": {
        "project_name": "Example project name",
        "project_slug": "example_project_name",
        "license": "MIT license",
        "author_name": "Author Name",
        "email": "example@gmail.com",
        "description": "A short description of the project.",
        "domain_name": "example.com",
        "version": "0.1.0",
        "timezone": "UTC",
        "use_pycharm": "n",
        "use_docker": "n",
        "use_travis": "n",
        "command_line_interface": "click",
        "open_source_project": "y"
        }
    }


    cookiecutter_dict

# Generated at 2022-06-22 12:28:40.211982
# Unit test for function prompt_for_config
def test_prompt_for_config():

    from cookiecutter.main import cookiecutter

    tmp_folder = 'tmp_folder'
    template_folder = 'tests/test-template'

    cookiecutter(template_folder, no_input=True, output_dir=tmp_folder)

    context = cookiecutter(template_folder, no_input=True, output_dir=tmp_folder)
    context['cookiecutter']['project_name'] = 'test_project'

    context = cookiecutter(template_folder, no_input=True, extra_context=context, output_dir=tmp_folder)

    assert context['cookiecutter']['project_name'] == 'test_project'
    assert context['cookiecutter']['repo_name'] == 'test_project'

# Generated at 2022-06-22 12:28:48.970108
# Unit test for function prompt_for_config
def test_prompt_for_config():
    from cookiecutter.environment import DEFAULT_CONFIG
    import os
    import pytest

    DIR = os.path.realpath(os.path.curdir)

    if os.path.isdir(DIR):
        og_dir = os.path.realpath(os.curdir)
        os.chdir(str(DIR))

    try:
        json_file = os.path.join(DIR, 'tests/test-prompt-for-config/cookiecutter.json')
        with pytest.raises(UndefinedVariableInTemplate):
            # Can't render test.
            prompt_for_config(DEFAULT_CONFIG.get_dict(json_file=json_file))
    except:
        import traceback; traceback.print_exc()

# Generated at 2022-06-22 12:28:56.741803
# Unit test for function render_variable
def test_render_variable():
    """Test function render_variable by using an example."""
    env = StrictEnvironment(
        context={'cookiecutter': {'project_name': 'My Awesome Project'}}
    )
    raw = '{{ cookiecutter.project_name.replace(" ", "_") }}'
    cookiecutter_dict = {'project_name': 'My Awesome Project'}

    expected_result = 'My_Awesome_Project'
    result = render_variable(env, raw, cookiecutter_dict)
    assert result == expected_result

    # Test with a list
    raw = [
        '{{ cookiecutter.project_name.replace(" ", "_") }}',
        '{{ cookiecutter.project_name.replace(" ", "-") }}',
    ]
    cookiecutter_dict = {'project_name': 'My Awesome Project'}



# Generated at 2022-06-22 12:29:03.947201
# Unit test for function read_user_dict
def test_read_user_dict():
    dict_name = 'hello'
    dict_default = {'a': 'b'}
    test_dict = {'a': 'b'}

    input_return = '{"a":"b"}'
    click.echo = click.echo_via_pager = click.pause = lambda x: None

    try:
        click.getchar = lambda: b'\n'
        assert read_user_dict(dict_name, dict_default) == dict_default
    except Exception:
        assert False

    try:
        click.getchar = lambda: b'\n'
        assert read_user_dict(dict_name, dict_default) == dict_default
    except Exception:
        assert False


# Generated at 2022-06-22 12:29:08.820427
# Unit test for function prompt_for_config
def test_prompt_for_config():
    import json
    import os
    from cookiecutter.prompt import prompt_for_config
    # Load the config file, then ask user to fill in the values
    context = json.load(open('cookiecutter.json'), object_pairs_hook=OrderedDict)
    cookiecutter_dict_values = prompt_for_config(context)
    # Write the values to the config file
    with open('cookiecutter.json', 'w') as f:
        json.dump(cookiecutter_dict_values, f, indent=4)

    config_file = os.path.join(os.getcwd(), 'cookiecutter.json')
    # Test to make sure config_file was created
    if os.path.exists(config_file):
        print('Test Prompt for Config: PASSED\n')
        os

# Generated at 2022-06-22 12:29:24.205775
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {}

# Generated at 2022-06-22 12:29:30.826563
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Test for function prompt_for_config."""
    from cookiecutter.main import cookiecutter
    from cookiecutter.prompt import read_user_variable
    from cookiecutter.utils import rmtree
    from pytest import raises

    # Prompt the user at command line for manual configuration
    result = cookiecutter('tests/fake-repo-templates/prompt-for-config/', no_input=False)
    assert result['repo_name'] == 'cookiecutter'

    # Let the shell configure the project
    result = cookiecutter(
        'tests/fake-repo-templates/prompt-for-config/',
        no_input=True,
        extra_context={'repo_name': 'cookiecutter-test'},
    )

# Generated at 2022-06-22 12:29:33.917566
# Unit test for function read_user_dict
def test_read_user_dict():
    # Test with default value
    default_test = read_user_dict('test', {'test': 'default'})
    assert default_test == {'test': 'default'}

    # Test with user input
    input_test = read_user_dict('test', {'test': 'default'})
    assert input_test == {'test': 'default'}


# Generated at 2022-06-22 12:29:45.637970
# Unit test for function read_user_dict
def test_read_user_dict():
    # The following tests was copied from the test_prompt_for_config function
    # from cookiecutter/tests/test_prompt.py.
    # It was adjusted by removing all prompts, because read_user_dict is unit tested
    # in isolation.
    from cookiecutter.prompt import read_user_dict
    from click.testing import CliRunner


# Generated at 2022-06-22 12:29:55.885265
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:30:02.004124
# Unit test for function prompt_for_config
def test_prompt_for_config():

    context = {}

# Generated at 2022-06-22 12:30:07.411325
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:30:16.598164
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """
    Encoding tests:
        - String encoding
        - String encoding with space
        - String encoding with unicode
        - String encoding with special characters
    """

    # Verifying if prompt_for_config returns the same string entered
    context_str = {
        "cookiecutter": {"str": "Sample string"}
    }
    cookiecutter_dict = prompt_for_config(context_str, no_input=True)
    assert cookiecutter_dict["str"] == context_str["cookiecutter"]["str"]

    # Verifying if prompt_for_config returns the same string entered
    # with space as default value
    context_str_space = {
        "cookiecutter": {"str": "Sample string with space"}
    }

# Generated at 2022-06-22 12:30:20.159609
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Unit test for function prompt_for_config."""
    try:
        prompt_for_config({})
    except click.ClickException as err:
        assert err.code == 2



# Generated at 2022-06-22 12:30:23.611393
# Unit test for function process_json
def test_process_json():
    """Test the function process_json()."""
    assert process_json('{"name": "Matt"}') == {'name': 'Matt'}



# Generated at 2022-06-22 12:30:42.546311
# Unit test for function read_user_dict
def test_read_user_dict():
    from click.testing import CliRunner

    class UserDict(object):

        def __init__(self):
            self.data = {}

        def __call__(self, var_name, default_value):
            return self.data[var_name]

        def set_data(self, var_name, data):
            self.data[var_name] = data

    user_dict = UserDict()
    runner = CliRunner()

    # Test default_value
    user_dict.set_data('test_1', 'default')
    assert read_user_dict('test_1', {'test': 'default'}) == {'test': 'default'}

    # Test JSON loading
    user_dict.set_data('test_2', '{"test": "json"}')

# Generated at 2022-06-22 12:30:50.222014
# Unit test for function render_variable
def test_render_variable():

    env = StrictEnvironment()
    cookiecutter_dict = OrderedDict([("project_name", "Peanut Butter Cookie")])

    # Test non-string types
    assert render_variable(env, None, cookiecutter_dict) is None
    assert render_variable(env, 1, cookiecutter_dict) == "1"
    assert render_variable(env, 1.0, cookiecutter_dict) == "1.0"
    assert render_variable(env, [1, 2, 3], cookiecutter_dict) == [1, 2, 3]
    assert render_variable(env, ["{{ cookiecutter.project_name }}", 2, 3], cookiecutter_dict) == [
        "Peanut Butter Cookie",
        2,
        3,
    ]

# Generated at 2022-06-22 12:30:59.575610
# Unit test for function prompt_for_config
def test_prompt_for_config():

    import os

    this_dir = os.path.abspath(os.path.dirname(__file__))

    # A small "try it out" example context that came pre-installed with
    # Cookiecutter when I tried it in early 2014.

# Generated at 2022-06-22 12:31:09.177487
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:31:14.433751
# Unit test for function read_user_choice
def test_read_user_choice():
    # Sample data
    options = ["python", "java", "javascript"]
    # Testing functionality
    user_choice = read_user_choice("Select a programming language", options)
    # We assume that the default value is set to the first item of the list
    default_value = options[0]
    if user_choice != default_value:
        return True
    else:
        return False


# Generated at 2022-06-22 12:31:20.920385
# Unit test for function render_variable
def test_render_variable():
    """
    Asserts if all the values are properly rendered
    """
    # Set all the variables
    raw = "['true', 'false', 'other']"
    env = StrictEnvironment(context={})
    cookiecutter_dict = OrderedDict([])
    # Check if the values are being properly rendered
    rendered = render_variable(env, raw, cookiecutter_dict)
    assert(rendered == ['true', 'false', 'other'])

# Generated at 2022-06-22 12:31:22.940663
# Unit test for function read_user_choice
def test_read_user_choice():
    choices = ['choice1', 'choice2', 'choice3', 'choice4']
    assert read_user_choice('choice', choices) == 'choice1'

# Generated at 2022-06-22 12:31:29.501650
# Unit test for function prompt_for_config
def test_prompt_for_config():
    from cookiecutter.main import cookiecutter

    extra_context = {
        'full_name': 'Audrey Roy Greenfeld',
        'email': 'audreyr@example.com',
        'github_username': 'audreyr',
    }

    # no_input=True
    with pytest.raises(SystemExit) as excinfo:
        cookiecutter(
            'tests/test-cookiecutter-json/',
            no_input=True,
            extra_context=extra_context,
            replay=False,
        )
    assert os.path.exists('foobar')
    assert excinfo.value.code == 0

    # no_input=False

# Generated at 2022-06-22 12:31:39.577257
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """
    Test prompt_for_config function.
    """
    import os
    import sys

    # Make the prompt function return values set in the os env.
    def mock_prompt(prompt, default, value_proc):
        # Environment variables to be used with this mock.
        # Note: This is a bit of a hack and an alternative might be to use
        # a click testing module, such as click-testing.
        #   With that being said, this is a lot simpler.
        return os.environ.get('{}_{}'.format(prompt, default))

    # Make the prompt function for dictionaries return the default
    # value without asking the user.
    def mock_dict_prompt(prompt, default, value_proc):
        return value_proc(default)

    # Make the read_user_choice function return

# Generated at 2022-06-22 12:31:45.955781
# Unit test for function prompt_for_config
def test_prompt_for_config():
    from cookiecutter.main import cookiecutter

    # Set to True if you need to see the output of the rendering
    # process from this interactive test.
    trace = False

    no_input = False
    project_dir = "mytestproject"
    extra_context = {}

    # Use the standard Cookiecutter test repository as the source.
    repo_dir = cookiecutter('.', no_input=True, output_dir='mytestproject',
                            overwrite_if_exists=True, skip_if_file_exists=True)

    # Make sure that empty directories get created as well.
    # We don't want to skip those in the testing process.
    extra_context['cookiedozer'] = True

    # Make sure to apply a fake GitHub token, to prevent wrong token
    # prompts in case this code is run on a

# Generated at 2022-06-22 12:32:02.751938
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Test that the function prompt_for_config works correctly."""
    # Note : due to the nature of this function, the values returned
    # are hard coded. However, it is not necessarily a bad thing.
    # The function is meant to interact with the user, so it will
    # always ask for a user's input. The tests check if the input
    # given by the user is saved correctly.
    # The values for the dicts should be in the same order as shown
    # here.

    # Case 1 : a simple dictionary
    context1 = {
        'cookiecutter': {
            'a_dict': {'first_name': 'John', 'last_name': 'Smith'},
            'a_number': 42,
            'a_string': 'Hello',
        }
    }


# Generated at 2022-06-22 12:32:05.685468
# Unit test for function render_variable
def test_render_variable():
    """Test render_variable."""
    context = {'cookiecutter': {'project_name': 'Peanut Butter Cookie'}}
    variable = 'Hello, my name is {{ cookiecutter.project_name }}'
    variable = render_variable(None, variable, context)
    assert variable == 'Hello, my name is Peanut Butter Cookie'

# Generated at 2022-06-22 12:32:12.844564
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {
        'cookiecutter': {
            'project_name': 'Cookie Monster',
            'favorite_color': 'blue',
            'colors': ['red', 'green', 'blue'],
            '_secret_stuff': {
                'username': 'tpdye',
                'sex': 'm',
                'occupation': 'Programmer',
            },
            '__COMPANY': 'Lucware LLC',
        }
    }
    cookiecutter_dict = prompt_for_config(context)
    assert cookiecutter_dict['project_name'] == 'Cookie Monster'
    assert cookiecutter_dict['favorite_color'] == 'blue'
    assert cookiecutter_dict['colors'] == 'blue'

# Generated at 2022-06-22 12:32:17.045791
# Unit test for function prompt_for_config
def test_prompt_for_config():
    # GIVEN a template with a hierarchy of variables
    # WHEN we have no input from the user
    context = [
        {
            'cookiecutter': {
                '_template': {
                    'raw_variable': '{{ cookiecutter.variable }}',
                    'dict_variable': {
                        'key': '{{ cookiecutter.variable }}',
                        'key2': '{{ cookiecutter.variable }}',
                    }
                },
                'variable': 'value'
            }
        },
    ]

    # THEN we expect the user to be prompted with
    # 'raw_variable' : 'value'
    # 'dict_variable' : {
    #   'key' : 'value',
    #   'key2' : 'value'
    # }

    # GIVEN a template with a hierarchy of variables
    #

# Generated at 2022-06-22 12:32:24.363393
# Unit test for function read_user_dict
def test_read_user_dict():
    """Unit test for function read_user_dict."""
    env = StrictEnvironment()
    try:
        assert read_user_dict("foo", "bar") == "bar"
    except TypeError:
        assert True
    try:
        assert read_user_dict("foo", [1, 2, 3]) == [1, 2, 3]
    except TypeError:
        assert True

# Generated at 2022-06-22 12:32:31.019499
# Unit test for function process_json
def test_process_json():
    # Test the case where we cannot JSON decode the string.
    with pytest.raises(click.UsageError):
        process_json("{'a': 'b'}")
    # Test the case where we have a JSON string that is not a dictionary.
    with pytest.raises(click.UsageError):
        process_json('"a"')
    # Test the case where we have a valid JSON string.
    user_dict = process_json('{"a": "b"}')
    assert user_dict == {"a": "b"}

# Generated at 2022-06-22 12:32:42.234633
# Unit test for function read_user_dict
def test_read_user_dict():
    import pytest
    from click.testing import CliRunner
    from click.exceptions import BadParameter, UsageError

    class Runner(CliRunner):
        def invoke(self, cli, args=None, input=None, env=None, catch_exceptions=False):
            """
            Runs a command similar to how a user would run it.  Unlike the
            regular CliRunner.invoke, it allows passing an input to the
            command.
            """
            args = args or []
            env = env or {}
            assert isinstance(input, str)
            env['_INPUT'] = input
            return super().invoke(cli, args=args, env=env, catch_exceptions=catch_exceptions)


# Generated at 2022-06-22 12:32:52.601316
# Unit test for function process_json
def test_process_json():
    """Unit test for function process_json."""
    # Test cases

# Generated at 2022-06-22 12:33:03.774109
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Test prompt_for_config function."""


# Generated at 2022-06-22 12:33:15.262527
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:33:32.569677
# Unit test for function prompt_for_config
def test_prompt_for_config():
    from cookiecutter.main import cookiecutter
    from cookiecutter.config import DEFAULT_CONFIG
    from cookiecutter.config import get_config_from_filename
    cfg_filename = 'cookiecutter/tests/test-config.yaml'
    options = dict(
        no_input=False,
        config_file=cfg_filename,
        default_config=True,
        overwrite_if_exists=True,
        extra_context='{"who_are_you":"Tester"}',
        output_dir='/tmp',
        reuse_dir=False,
    )
    config = get_config_from_filename(options['config_file'], options['default_config'])
    config.update(DEFAULT_CONFIG)

    context = dict(config)
    context.update(options)
    context

# Generated at 2022-06-22 12:33:42.566884
# Unit test for function read_user_dict
def test_read_user_dict():
    context = {'cookiecutter': {}}
    context['cookiecutter']['project_name'] = 'Peanut Butter Cookie'
    context['cookiecutter']['package_name'] = '{{ cookiecutter.project_name.lower() }}'

    # Not testing the user_dict_invalid_json function
    # because it will cause the program to exit with an error message.

    user_dict = read_user_dict("test", default_value={"test": "test"})
    assert isinstance(user_dict, dict), "Returns a dict"
    assert user_dict == {"test": "test"}, "Can return default value"

    perfect_user_dict = {"test": "test"}
    user_dict = read_user_dict("test", default_value=perfect_user_dict)

# Generated at 2022-06-22 12:33:45.086103
# Unit test for function read_user_dict
def test_read_user_dict():
    """
    Test if the function can return the dict value the user has input.
    """
    var_name, default_value = 'test', {'test1': 'test1'}
    test_dict = read_user_dict(var_name, default_value)
    assert test_dict == {'test1': 'test1'}

# Generated at 2022-06-22 12:33:52.428877
# Unit test for function prompt_for_config
def test_prompt_for_config():
    # Create a dict with all the available options for testing
    context = {
        'cookiecutter': {'project_name': 'Foobar', 'repo_name': 'foobar'}
    }

    # Call prompt_for_config with this context and no_input=True
    cookiecutter_dict = prompt_for_config(context, no_input=True)

    assert cookiecutter_dict['project_name'] == 'Foobar'
    assert cookiecutter_dict['repo_name'] == 'foobar'

# Generated at 2022-06-22 12:34:02.814408
# Unit test for function read_user_dict
def test_read_user_dict():
    template_vars = {
        "project_name": "{{ cookiecutter.project_slug | replace(\"_\", \"\") }}",
        "project_slug": "{{ cookiecutter.project_name | replace(\" \", \"_\") }}"
    }
    project_name = read_user_dict("project_name", template_vars)
    try:
        assert project_name == template_vars["project_name"], "Wrong answer"
    except Exception as e:
        print(e)
        print("The project name is: " + project_name)
    project_slug = read_user_dict("project_slug", template_vars)

# Generated at 2022-06-22 12:34:10.888293
# Unit test for function prompt_for_config
def test_prompt_for_config():
    # Quite complicated to test. Therefore I created a JSON file
    # with different possible configurations.
    with open("tests/test_prompt_for_config.json") as f:
        test_config = json.load(f)

    # Now go through all the different possible configurations
    for test_case in test_config:
        if test_case["expected_result"] == "UndefinedVariableInTemplate":
            # Then we should expect an error
            unexpected_result_encountered = False
            try:
                prompt_for_config(test_case["context"], test_case["no_input"])
                unexpected_result_encountered = True
            except UndefinedVariableInTemplate:
                pass
            assert unexpected_result_encountered is False

# Generated at 2022-06-22 12:34:17.161776
# Unit test for function prompt_for_config
def test_prompt_for_config():
    # pylint: disable=W0612
    from cookiecutter.main import cookiecutter

    output = cookiecutter(
        'tests/fake-repo-tmpl', no_input=False,
        default_config={'full_name': 'Test person'}
    )
    assert output['repo_name'] == 'test-repo-tmpl'
    assert output['project_name'] == 'Test project'



# Generated at 2022-06-22 12:34:23.545091
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {
        'cookiecutter': {
            "foo": "bar",
            "baz": "{{cookiecutter.foo}}"
        }
    }

    cookiecutter_dict = prompt_for_config(context)

    assert cookiecutter_dict['foo'] == 'bar'
    assert cookiecutter_dict['baz'] == 'bar'

# Generated at 2022-06-22 12:34:25.635575
# Unit test for function read_user_dict
def test_read_user_dict():
    user_dict = read_user_dict("yaar", {'foo': 'bar'})
