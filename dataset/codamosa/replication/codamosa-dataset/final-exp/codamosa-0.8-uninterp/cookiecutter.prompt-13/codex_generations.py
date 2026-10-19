

# Generated at 2022-06-22 12:24:47.111604
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:24:57.822786
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:25:03.912153
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {
        'cookiecutter': {
            'name': 'My Test Project',
            'email': 'test@example.com',
            '_copy_without_render': ['special_file.txt'],
        }
    }

    cookiecutter_dict = prompt_for_config(context, no_input=True)

    assert 'name' in cookiecutter_dict
    assert 'email' in cookiecutter_dict
    assert '_copy_without_render' in cookiecutter_dict

# Generated at 2022-06-22 12:25:13.660713
# Unit test for function prompt_for_config
def test_prompt_for_config():
    def read_user_variable(var_name, default_value):
        return "Test_Variable"

    def read_user_yes_no(question, default_value):
        return "True"

    def read_repo_password(question):
        return "Test_Password"

    def read_user_choice(var_name, options):
        return "choice_1"

    def read_user_dict(var_name, default_value):
        return "Test_Dict"


# Generated at 2022-06-22 12:25:21.046622
# Unit test for function render_variable
def test_render_variable():
    """ Test the render_variable function using dictionaries as variables. """
    # Testa the project_name got rendered correctly.
    env = StrictEnvironment()
    cookiecutter_dict = {
        'cookiecutter': {
            'project_name': 'Peanut butter cookie',
        },
    }
    raw = raw = '{{ cookiecutter.project_name.replace(" ", "_") }}'
    assert render_variable(env, raw, cookiecutter_dict) == 'Peanut_butter_cookie'
    # Test that the date got rendered correctly.
    raw = '{{ cookiecutter.__today }}'
    assert render_variable(env, raw, cookiecutter_dict) == '2020-09-07'
    # Test that the year got rendered correctly.
    raw = '{{ cookiecutter.__today.year }}'

# Generated at 2022-06-22 12:25:33.467273
# Unit test for function read_user_dict
def test_read_user_dict():
    """Test case for function read_user_dict"""
    # Provided test data with default value
    dict_provided_data = {
        'project_name': 'projectname',
        'package_name': 'packagename',
        'version': 'version',
        'description': 'description',
        'author_name': 'authorname',
        'email': 'email@email.com',
        'license': 'license',
        'repo_name': 'reponame',
        'keywords': 'keywords',
        'project_slug': 'project_slug'
    }

    # User inputs for dict data
    dict_input_data = {
        'a': 'value for a',
        'b': 'value for b',
        'c': 'value for c'
    }

    # JSON string for dict


# Generated at 2022-06-22 12:25:42.138298
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {
        'cookiecutter': {
            'project_name': 'My Test Project',
            'description': 'A short description of the project.',
            'author_name': 'Firstname Lastname',
            'email': 'me@example.com',
            'version': '0.1.0',
            'open_source_license': 'MIT license'
        }
    }
    cookiecutter_dict = prompt_for_config(context, no_input=True)
    for key in context['cookiecutter'].keys():
        assert key in cookiecutter_dict.keys(), "Missing key in prompt for config."

# Generated at 2022-06-22 12:25:53.715119
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:25:57.326029
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {
        'cookiecutter': {
            'name': 'example',
            'email': 'example@example.com',
        }
    }
    cookiecutter_dict = prompt_for_config(context, True)
    print(cookiecutter_dict)

# Generated at 2022-06-22 12:26:05.969345
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """ Test a scenario of asking for input for a config and check the inputs """
    # Test case 1

# Generated at 2022-06-22 12:26:22.023998
# Unit test for function prompt_for_config
def test_prompt_for_config():
    from cookiecutter.environment import StrictEnvironment
    from cookiecutter.prompt import prompt_for_config
    from cookiecutter.main import cookiecutter
    from click.testing import CliRunner

    response = CliRunner().invoke(
        cookiecutter,
        [
            'tests/fake-repo-pre/',
            '--no-input',
        ],
        catch_exceptions=False,
    )
    assert response.exit_code == 0, response.output

    # Load the context.
    env = StrictEnvironment()
    context = cookiecutter('tests/fake-repo-pre/', no_input=True)
    generated_project = prompt_for_config(context, no_input=True)
    assert generated_project['repo_name'] == "cookiecutter-pypackage"

# Generated at 2022-06-22 12:26:22.770103
# Unit test for function prompt_for_config
def test_prompt_for_config():
    pass


# Generated at 2022-06-22 12:26:33.151839
# Unit test for function prompt_for_config
def test_prompt_for_config():

    context = {
        'cookiecutter': {
            'project_slug': 'monkey',
            '_template': {
                'repo_name': 'peanut_butter_cookie.tmpl',
                'project_name': '{{ cookiecutter.project_slug | capitalize }}',
                'open_source_license': 'MIT license',
                'release_date': 'to be released',
                'use_pypi_deployment_with_travis': True,
                'use_python2': True,
                'command_line_interface': 'Click',
                'version': '0.1.0',
                'use_pytest': True,
            },
        }
    }
    result = prompt_for_config(context, no_input=True)

# Generated at 2022-06-22 12:26:42.712084
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """ Test if function prompt_for_config returns a correct variable """
    # Test if function is returning a correct variable
    context = {
        "cookiecutter": {
            "full_name": "Your Name",
            "email": "Your email",
            "project_name": "Your project name",
        }
    }

    expected = {
        "full_name": "Your Name",
        "email": "Your email",
        "project_name": "Your project name",
    }

    cookies = prompt_for_config(context, True)
    assert expected == cookies

    # Test if function is working with a full_name without a space.
    # The prompt_for_config function is expecting a first and last name.
    # This test makes sure it is returning a firstname and no lastname.

# Generated at 2022-06-22 12:26:47.906796
# Unit test for function read_user_dict
def test_read_user_dict():
    user_value='{"host":null}'
    class Test:
        def __init__(self, msg):
            self.msg = msg
    test = Test(user_value)
    dict = read_user_dict('test', test.msg)
    assert dict['host'] == None
    assert dict != test.msg


# Generated at 2022-06-22 12:26:53.284746
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {
        'cookiecutter': {
            'name': 'Jinja2',
            'description': 'Jinja2 is a full featured template engine for Python.',
            'open_source_license': 'MIT',
            'author_name': 'Armin Ronacher',
            'version': '2.8',
            'release': '2.8.0',
            'python_versions': '*.*'
        }
    }

    cookiecutter_dict = prompt_for_config(context, True)

    assert cookiecutter_dict['name'] == 'Jinja2'

# Generated at 2022-06-22 12:27:02.624741
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Unit-test for function prompt_for_config()."""
    context = {
        'cookiecutter': {
            'repo_name': 'My Fake Repo',
            'repo_url': 'https://github.com/my-org/my-fake-repo.git',
            'repo_desc': 'My fake repository',
            'author_name': 'Fake Author',
            'project_license': 'MIT',
            'py_version': '3.7.0',
            'open_source_license': 'MIT',
            'pypi_username': 'fakeuser',
            'full_name': 'Fake User',
            'email': 'fake@email.com',
            'github_username': 'fakeuser',
        }
    }

# Generated at 2022-06-22 12:27:11.983355
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {
        "cookiecutter": {
            "project_name": "Awesome Project",
            "description": "A short description of the project.",
            "author_name": "Your Name",
            "open_source_license": "MIT license",
            "repo_name": "{{ cookiecutter.project_name.lower().replace(' ', '-') }}",
            "python_version": "2.7",
            "use_whitespace_in_filename": "no"
        }
    }
    cookiecutter_dict = OrderedDict([])
    no_input = True
    cookiecutter_dict = prompt_for_config(context, no_input)
    assert(cookiecutter_dict["repo_name"] == "awesome-project")




# Generated at 2022-06-22 12:27:16.412373
# Unit test for function render_variable
def test_render_variable():
    context = {
        'cookiecutter': {
            '_copy_without_render': {
                'foo': 'bar',
                'baz': ['qux'],
            },
            'example': '{{cookiecutter.foo}} {{cookiecutter._copy_without_render.baz[0]}}',
            'foo': 'my',
        },
    }

    env = StrictEnvironment(context=context)

    result = render_variable(env, '{{cookiecutter.example}}', context['cookiecutter'])

    assert result == 'my bar'

# Generated at 2022-06-22 12:27:22.867755
# Unit test for function read_user_dict
def test_read_user_dict():
    var_name = 'some_dict'
    default_value = {'some_key': 'some_value'}
    user_value = '{"some_key2": "some_value2"}'
    assert read_user_dict(var_name, default_value) == default_value
    assert read_user_dict(var_name, default_value, input_str=user_value) == json.loads(user_value)


# Generated at 2022-06-22 12:27:38.560845
# Unit test for function render_variable
def test_render_variable():
    context = {'cookiecutter': {'name': 'John Doe'}}
    env = StrictEnvironment(context=context)
    template = '{{cookiecutter.name}}'
    assert render_variable(env, template, context['cookiecutter']) == 'John Doe'

# Generated at 2022-06-22 12:27:45.646907
# Unit test for function process_json
def test_process_json():
    """Test to check that process_json is actually processing and returns json
    """
    test_string = '{\n    "cookiecutter": {\n        "project_name": "test json"\n    }\n}'
    test_output = process_json(test_string)
    # Checking if the json is a dictionary
    assert isinstance(test_output, dict)
    # Checking if the project name is test json
    assert test_output['cookiecutter']['project_name'] == 'test json'

# Generated at 2022-06-22 12:27:50.808462
# Unit test for function process_json
def test_process_json():
    test_data = dict(key=dict(key=None), key2="{{ cookiecutter.key2 }}")
    assert test_data == process_json(json.dumps(test_data))

    # Test value_proc
    with pytest.raises(click.UsageError):
        process_json("{{ cookiecutter.key2 }}")

# Generated at 2022-06-22 12:28:00.206236
# Unit test for function read_user_dict
def test_read_user_dict():
    """
    Test for function read_user_dict in prompt.py
    """
    from cookiecutter.context import DEFAULT_CONTEXT
    from cookiecutter.environment import StrictEnvironment
    from cookiecutter.utils import debug_object
    assert read_user_dict('variable', {"key": "value"})
    assert not read_user_dict('variable', None)
    context = DEFAULT_CONTEXT.copy()
    env = StrictEnvironment(context=context)
    rendered_variable = debug_object(render_variable(env, 'version', context))
    assert read_user_dict('variable', rendered_variable)
    assert not read_user_dict('variable', rendered_variable)

test_read_user_dict()

# Generated at 2022-06-22 12:28:03.114819
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Test prompt_for_config on a simple dict."""
    prompt_for_config({'cookiecutter': {'key': 'value'}})


# Generated at 2022-06-22 12:28:15.027908
# Unit test for function read_user_dict
def test_read_user_dict():
    """Unit test for function read_user_dict"""
    import mock
    import click

    invalid_dicts = [
        # Test: reading empty string
        ('test_read_user_dict_1', [''], ''),
        # Test: reading non JSON string
        ('test_read_user_dict_2', ['invalid'], 'invalid'),
        # Test: reading invalid JSON string
        ('test_read_user_dict_3', ['{"invalid": "dict"}'], '{"invalid": "dict"}'),
        # Test: reading valid JSON string that is not a dict
        ('test_read_user_dict_4', ['[1,2,3]'], '[1,2,3]'),
    ]

    # Test: Invalid dictionary values are and lead to error

# Generated at 2022-06-22 12:28:25.542460
# Unit test for function read_user_choice
def test_read_user_choice():
    # test no option case
    options = []
    var_name = 'var name'
    try:
        read_user_choice(var_name, options)
        assert False
    except ValueError:
        assert True
    # test one option case
    options = ['option0']
    assert read_user_choice(var_name, options) == 'option0'
    # test multiple options
    options = ['option0', 'option1']
    assert read_user_choice(var_name, options) in options
    # test wrong type of options
    try:
        options = {'option0': 'option1'}
        read_user_choice(var_name, options)
        assert False
    except TypeError:
        assert True
    return

# Generated at 2022-06-22 12:28:32.186366
# Unit test for function process_json
def test_process_json():
    """Test the two cases where process_json can fail."""
    user_value1 = '{"test": "string"}'
    user_value2 = '["test", "string"]'
    valid_dict = json.loads(user_value1)
    assert valid_dict == process_json(user_value1)
    try:
        invalid_dict = json.loads(user_value2)
        assert process_json(user_value2) != invalid_dict
    except Exception:
        pass
    try:
        process_json('test')
    except click.UsageError:
        pass

# Generated at 2022-06-22 12:28:38.203766
# Unit test for function process_json
def test_process_json():
    # Given
    json_dict = {'key1': 'value1',
                 'key2': 'value2'}
    json_string = json.dumps(json_dict)

    # When
    user_dict = process_json(json_string)

    # Then
    assert isinstance(user_dict, dict)
    assert user_dict == json_dict

# Generated at 2022-06-22 12:28:43.096374
# Unit test for function render_variable
def test_render_variable():
    from cookiecutter.main import cookiecutter

    with_variables_file = 'Tests/tests/test-generate-prompts/'
    without_variables_file = 'Tests/tests/test-generate-prompts/no-json-config'

    cookiecutter(with_variables_file)
    cookiecutter(without_variables_file)

# Generated at 2022-06-22 12:29:04.524634
# Unit test for function read_user_dict
def test_read_user_dict():
    # Arrange
    var_name = 'var_name'
    default_value = {}
    user_value = None

    # Act
    result = read_user_dict(var_name, default_value)

    # Assert
    assert result is default_value

    # Act
    user_value = '{"1": "foo", "2": "bar"}'
    result = read_user_dict(var_name, default_value)
    assert result is not default_value

    # Assert
    assert result['1'] == 'foo'
    assert result['2'] == 'bar'

# Generated at 2022-06-22 12:29:07.994949
# Unit test for function read_user_choice
def test_read_user_choice():
    options = ["choice1","choice2","choice3"]
    choice = read_user_choice("Test", options)
    assert choice == options[0]

# Generated at 2022-06-22 12:29:14.720411
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {}
    context['cookiecutter'] = {
        'project_name': '{{cookiecutter.test_variable.title()}}',
        'test_variable': 'test',
    }

    cookiecutter_dict = prompt_for_config(context, no_input=True)
    assert cookiecutter_dict['project_name'] == 'Test'
    assert cookiecutter_dict['test_variable'] == 'test'

# Generated at 2022-06-22 12:29:20.505376
# Unit test for function prompt_for_config
def test_prompt_for_config():
    # Example of context
    context = {
        'cookiecutter': {
            'app_name': 'hugo',
            'project_name': 'Hello Hugo',
            'year': '2020',
            'version': '0.55.3',
            'author': 'Jean-Luc Picard',
        }
    }
    cookiecutter_dict = prompt_for_config(context)
    assert cookiecutter_dict['project_name'] == 'Hello Hugo'
    assert cookiecutter_dict['version'] == '0.55.3'

# Generated at 2022-06-22 12:29:24.148795
# Unit test for function process_json
def test_process_json():
    assert process_json('{ "foo": "bar" }') == { 'foo': 'bar' }

    with pytest.raises(click.UsageError):
        process_json('{ "foo": "bar" ')

    with pytest.raises(click.UsageError):
        process_json('Not a dict')

# Generated at 2022-06-22 12:29:35.759697
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:29:37.032140
# Unit test for function prompt_for_config
def test_prompt_for_config():
    #TODO
    pass

# Generated at 2022-06-22 12:29:47.356998
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:29:56.743807
# Unit test for function read_user_dict
def test_read_user_dict():
    """Function for testing function read_user_dict."""
    from click.testing import CliRunner
    from cookiecutter.prompt import read_user_dict

    runner = CliRunner()
    results = runner.invoke(read_user_dict, input='{"a":1}\n')
    assert results.exception is None
    assert results.exit_code == 0
    assert results.output == 'a\n'

    runner = CliRunner()
    results = runner.invoke(read_user_dict, input='{"a":1}\n{"a":1}\n')
    assert results.exception is None
    assert results.exit_code == 0
    assert results.output == 'a\n{"a": 1}\n'

    runner = CliRunner()

# Generated at 2022-06-22 12:30:08.951549
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:30:30.978563
# Unit test for function render_variable
def test_render_variable():
    # Given
    raw = "{{ cookiecutter.project_name.replace(' ', '_') }}"
    cookiecutter_dict = OrderedDict([('project_name', "Peanut Butter Cookie")])
    env = StrictEnvironment(context=cookiecutter_dict)

    # When
    result = render_variable(env, raw, cookiecutter_dict)

    # Then
    assert result == "Peanut_Butter_Cookie"

# Generated at 2022-06-22 12:30:42.013441
# Unit test for function prompt_for_config
def test_prompt_for_config():
    import os
    import tempfile

    if not os.path.exists(os.path.expanduser('~/.config/cookiecutterrc')):
        os.makedirs(os.path.expanduser('~/.config/'))
    with tempfile.NamedTemporaryFile(mode='w+',
                                     dir=None,
                                     delete=False,
                                     prefix='cookiecutterrc_test_') as f:
        f.write('foo: bar')

    os.environ['COOKIECUTTER_CONFIG_FILE'] = f.name


# Generated at 2022-06-22 12:30:49.856437
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Prompt user to enter a new config."""
    context = {
        "cookiecutter": {
            "full_name": "Your Name",
            "email": "Your email",
            "repo_name": "{{ cookiecutter.project_name | lower }}",
            "project_name": "{{ cookiecutter.full_name | replace(' ', '_') }}",
            "project_slug": "{{ cookiecutter.project_name | lower | replace(':', '') | replace('.', '') }}",
            "project_short_description": "A short description of the project.",
            "release_date" : "{{cookiecutter.current_date}}"
        },
        "current_date" : "01/01/2019",
    }
    env = StrictEnvironment(context=context)

    cookiecut

# Generated at 2022-06-22 12:30:55.446946
# Unit test for function process_json
def test_process_json():
    tested_content = "test"
    returned_content = process_json(tested_content)
    # Returns an OrderedDict to keep the json order and ease testing
    assert(isinstance(returned_content, OrderedDict))
    assert(len(returned_content) == 1)
    assert(returned_content["test"])


# Generated at 2022-06-22 12:31:06.634152
# Unit test for function prompt_for_config
def test_prompt_for_config():
    from cookiecutter.exceptions import UndefinedVariableInTemplate
    from cookiecutter.utils.paths import normalize_path


# Generated at 2022-06-22 12:31:11.404754
# Unit test for function prompt_for_config
def test_prompt_for_config():

    # Tests that a dictionary is properly returned given a valid json_data string
    context = {"cookiecutter":{
        "full_name": "Firstname Lastname",
        "email": "user@email.com",
        "github_username": "user"
    }}
    
    cookiecutter_dict = prompt_for_config(context)
    assert isinstance(cookiecutter_dict, dict)

# Generated at 2022-06-22 12:31:22.949964
# Unit test for function prompt_for_config
def test_prompt_for_config():
    from cookiecutter.utils import create_context_from_dicts
    from pyfakefs.fake_filesystem_unittest import TestCase

    class TestPromptForConfig(TestCase):
        """ Tests for prompt_for_config"""
        def setUp(self):
            """ SetUp """
            self.setUpPyfakefs()
            self.fs.create_file('example/cookiecutter.json', contents=b'{"name": "example"}')
            self.context = create_context_from_dicts(
                context_file='example/cookiecutter.json'
            )

        # Test regular variable
        def test_prompt_for_config_regular_variable(self):
            """ Test regular variable """

# Generated at 2022-06-22 12:31:29.500617
# Unit test for function read_user_choice
def test_read_user_choice():
    # Case 1: No options are given
    options = []
    try:
        read_user_choice('foo', options)
    except ValueError:
        pass
    else:
        raise AssertionError(
            'Expected function to raise ValueError when no options are given'
        )

    # Case 2: The options are not given in a list
    options = 'A, B, C'
    try:
        read_user_choice('foo', options)
    except TypeError:
        pass
    else:
        raise AssertionError('Expected function to raise TypeError when options are given as string')

    # Case 3: Only one option is given
    options = ['A']
    assert read_user_choice('foo', options) == 'A'

    # Case 4: Several options are given, and the user chooses the first


# Generated at 2022-06-22 12:31:37.511502
# Unit test for function prompt_for_config
def test_prompt_for_config():
    import os
    import shutil

    current_directory = os.path.dirname(os.path.abspath(__file__))
    context_file = os.path.join(
        current_directory, 'test_project', 'cookiecutter.json'
    )
    context = json.load(open(context_file), object_pairs_hook=OrderedDict)
    cookiecutter_dict = prompt_for_config(context, no_input=True)

# Generated at 2022-06-22 12:31:44.559676
# Unit test for function prompt_for_config
def test_prompt_for_config():
    cookiecutter_dict = OrderedDict([])
    context = {
       'cookiecutter': {
           'project_name': '{{ cookiecutter.project_slug.replace("-", "_") }}',
           'project_slug': 'Cookie Cutter',
           'repo_name': '{{ cookiecutter.project_name.replace(" ", "_") }}',
       }
    }
    env = StrictEnvironment(context=context)
    for key, raw in context['cookiecutter'].items():
        # We are dealing with a regular variable
        val = render_variable(env, raw, cookiecutter_dict)
        print(key, val)

# Generated at 2022-06-22 12:32:06.371955
# Unit test for function render_variable

# Generated at 2022-06-22 12:32:18.265582
# Unit test for function prompt_for_config
def test_prompt_for_config():
    # arrange
    context = {
        'cookiecutter': {
            'project_name': 'Kirby',
            'project_slug': 'kirby',
            'author_name': 'Kirby',
            'release': '2.2.3',
            'year': '2019'
        }
    }

    # act
    cookiecutter_dict = prompt_for_config(context, True)

    # assert
    assert cookiecutter_dict['project_name'] == 'Kirby'
    assert cookiecutter_dict['project_slug'] == 'kirby'
    assert cookiecutter_dict['author_name'] == 'Kirby'
    assert cookiecutter_dict['release'] == '2.2.3'
    assert cookiecutter_dict['year'] == '2019'

   

# Generated at 2022-06-22 12:32:29.860344
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """
    Unit test for function prompt_for_config
    """

# Generated at 2022-06-22 12:32:34.210507
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {'cookiecutter': {'full_name': 'Your name', 'email': 'Your email'}}
    cookiecutter_dict = prompt_for_config(context, no_input='true')
    assert cookiecutter_dict['full_name'] == 'Your name'
    assert cookiecutter_dict['email'] == 'Your email'

# Generated at 2022-06-22 12:32:44.959976
# Unit test for function render_variable
def test_render_variable():
    context = {
        'cookiecutter': {
            'name': 'Elena',
            'project_name': {'first': 'peanut butter', 'second': 'jelly'},
            'language': 'Python'
        }
    }
    env = StrictEnvironment(context=context)

    # Check for rendering strings.
    string = 'The {{ cookiecutter.name }}'
    assert render_variable(env, string, context) == 'The {{ cookiecutter.name }}'
    string = 'The {{ cookiecutter[\'name\'] }}'
    assert render_variable(env, string, context) == 'The Elena'

    # Check for rendering dicts.
    dict = '{{ cookiecutter.project_name }}'

# Generated at 2022-06-22 12:32:52.158930
# Unit test for function read_user_dict
def test_read_user_dict():
    test_dict = {'name': 'John Doe','age': 30}
    test_dict_str = '{"name": "John Doe","age": 30}'
    assert read_user_dict("Name and Age", test_dict) == test_dict
    assert read_user_dict("Name and Age", test_dict) == test_dict
    assert read_user_dict("Name and Age", test_dict) != test_dict_str
    assert read_user_dict("Name and Age", test_dict) == read_user_dict("Name and Age", test_dict)

# Generated at 2022-06-22 12:33:03.593881
# Unit test for function prompt_for_config
def test_prompt_for_config():
    from cookiecutter.main import cookiecutter
    from cookiecutter.exceptions import (
        FailedHookException,
        OutputDirExistsException,
    )
    from cookiecutter.environment import StrictEnvironment
    from cookiecutter.utils.paths import (
        make_sure_path_exists,
        make_sure_path_is_writable,
    )

    hooks = {
        'pre_gen_project': [
            'prompt_for_config.test_pre_gen_project'
        ],
        'post_gen_project': []
    }


# Generated at 2022-06-22 12:33:11.703150
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {'cookiecutter': {
        'full_name': 'First Last',
        'email': 'first.last@example.com',
        'github_username': 'first-last',
        'project_name': 'Awesome Project',
        'project_slug': 'awesome_project',
        'project_short_description': 'An awesome project'
    }}

    cookiecutter_dict = prompt_for_config(context, no_input=False)
    assert cookiecutter_dict["project_short_description"] == 'An awesome project'


# Generated at 2022-06-22 12:33:23.275809
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:33:31.366351
# Unit test for function prompt_for_config
def test_prompt_for_config():

    # Initial Cookiecutter dict
    context = {"cookiecutter": {"testing_key": "testing_value", "testing_key_2": {"testing_inner_key": "testing_inner_value"}}}

    # Process the context to get user variables
    cookiecutter_dict = prompt_for_config(context)

    # Test for keys and values in the returned cookiecutter_dict
    assert cookiecutter_dict['testing_key'] == "testing_value"
    assert cookiecutter_dict['testing_key_2']['testing_inner_key'] == "testing_inner_value"

# Generated at 2022-06-22 12:34:12.405448
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Test prompt_for_config
    """

# Generated at 2022-06-22 12:34:17.128411
# Unit test for function render_variable
def test_render_variable():
    env = StrictEnvironment(context={'cookiecutter': {'var_name': True}})
    test_dict1 = render_variable(env, "{% if cookiecutter.var_name %}True{% else %}False{% endif %}", {})
    assert test_dict1 == 'True'



# Generated at 2022-06-22 12:34:22.693489
# Unit test for function read_user_dict
def test_read_user_dict():
    # test with an empty dict
    assert read_user_dict("test_key_1", {}) == {}
    
    # test with an non-empty dict
    assert read_user_dict("test_key_2", {"a": 1, "b": "b"}) == {"a": 1, "b": "b"}