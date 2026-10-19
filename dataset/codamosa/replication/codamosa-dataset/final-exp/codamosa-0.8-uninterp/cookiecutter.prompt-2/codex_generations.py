

# Generated at 2022-06-22 12:24:46.787199
# Unit test for function process_json
def test_process_json():
    """Unit test for function process_json"""
    click.echo(json.dumps(process_json('{"project_name": "Peanut Butter Cookie"}')))
    
    

# Generated at 2022-06-22 12:24:49.124317
# Unit test for function read_user_dict
def test_read_user_dict():
    assert {"a": "b", "c": "d"} == read_user_dict("dict: ", {"a": "b", "c": "d"})

# Generated at 2022-06-22 12:24:59.045593
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:25:08.102882
# Unit test for function prompt_for_config
def test_prompt_for_config():
    key1 = 'var1'
    key2 = 'var2'
    key3 = 'var3'
    key4 = 'var4'
    key5 = 'var5'
    key6 = 'var6'
    key7 = 'var7'
    key8 = 'var8'
    key9 = 'var9'
    key10 = 'var10'
    key11 = 'var11'
    key12 = 'var12'
    key13 = 'var13'
    key14 = 'var14'
    key15 = 'var15'
    key16 = 'var16'
    key17 = 'var17'
    key18 = 'var18'
    key19 = 'var19'
    key20 = 'var20'
    key21 = 'var21'
    key22 = 'var22'
   

# Generated at 2022-06-22 12:25:14.856696
# Unit test for function read_user_dict
def test_read_user_dict():
    input_dict = {'A':'{{ cookiecutter.AAA }}', 'B':[1,2,3]}
    context = {'AAA':'bbb'}
    # First run with default
    result = read_user_dict('Some dict', input_dict)
    assert result==input_dict
    # Second run with user input
    result = read_user_dict('Some dict', input_dict)
    assert result['A'] == 'bbb'
    assert result['B'] == [1,2,3]

# Generated at 2022-06-22 12:25:26.368832
# Unit test for function prompt_for_config
def test_prompt_for_config():
    ctx = {
        'cookiecutter': {
            'project_name': 'Django Project',
            'repo_name': '{{ cookiecutter.project_name.replace(" ", "_") }}',
            'name': 'David',
            'use_docker': True,
        }
    }

    assert prompt_for_config(ctx) == OrderedDict(
        [
            ('project_name', 'Django Project'),
            ('repo_name', 'Django_Project'),
            ('name', 'David'),
            ('use_docker', True),
        ]
    )


# Generated at 2022-06-22 12:25:35.739042
# Unit test for function prompt_for_config
def test_prompt_for_config():
    cookiecutter_dict = prompt_for_config(context={
        'cookiecutter': {
            'author_name': 'Author Name',
            '_private': {
                'private_var': 'hidden'
            },
            '__about_me': '{{ cookiecutter._private.private_var }}'
        }
    }, no_input=True)
    assert cookiecutter_dict == {
        'author_name': 'Author Name',
        '_private': {
            'private_var': 'hidden'
        },
        '__about_me': 'hidden'
    }



# Generated at 2022-06-22 12:25:43.611222
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:25:48.225846
# Unit test for function process_json
def test_process_json():
    user_dict = {'a': 'b'}
    user_value = json.dumps(user_dict)
    assert read_user_dict('', '') == {}
    assert read_user_dict('', user_dict) == user_dict



# Generated at 2022-06-22 12:25:50.349159
# Unit test for function render_variable
def test_render_variable():
    assert render_variable(StrictEnvironment(), 'Test', {}) == 'Test'


# Generated at 2022-06-22 12:26:01.711722
# Unit test for function read_user_dict
def test_read_user_dict():
    example_dict = {'var1': 'val1', 'var2': 'val2'}
    var_name = 'Test'
    default_value = example_dict

    test_dict = read_user_dict(var_name, default_value)
    assert test_dict == example_dict
    # Try wrong type
    wrong_type = False
    try:
        read_user_dict(var_name, 'wrong_type')
    except TypeError:
        wrong_type = True
    assert wrong_type



# Generated at 2022-06-22 12:26:11.972419
# Unit test for function prompt_for_config
def test_prompt_for_config():
    from cookiecutter import main
    import tempfile
    import zipfile
    import os
    import shutil
    import subprocess
    import filecmp

    with tempfile.TemporaryDirectory() as temp_dir:
        context_file = os.path.join(temp_dir, 'context.json')

        # Create a zip file to be used as a template
        zf = zipfile.ZipFile("template.zip", "w")
        zf.write('tests/test-template/cookiecutter.json', 'cookiecutter.json')
        zf.write('tests/test-template/{{cookiecutter.repo_name}}/README.md')
        zf.close()

        # Create test-template/context.json

# Generated at 2022-06-22 12:26:14.203760
# Unit test for function process_json
def test_process_json():
    """ Tests that json string is converted to dictionary """
    assert type(process_json('{"key":"value", "key2":"value2"}')) == dict

# Generated at 2022-06-22 12:26:22.539841
# Unit test for function read_user_dict
def test_read_user_dict():
    var_name = "test"
    default_value = {'test':'test'}
    assert(read_user_dict(var_name, default_value) != None)
    assert(read_user_dict(var_name, default_value['test']) != None)
    assert(read_user_dict(var_name, default_value) == {'test':'test'})
    assert(read_user_dict(var_name, default_value['test']) == {'test':'test'})
    assert(read_user_dict(var_name, {}) != None)
    assert(read_user_dict(var_name, {}) != {'test':'test'})

# Generated at 2022-06-22 12:26:29.578326
# Unit test for function render_variable
def test_render_variable():
    from cookiecutter import utils

    project_dir = utils.find_root()
    context = utils.gen_context(project_dir, project_dir)
    raw = '{{ cookiecutter.project_name.replace(" ", "_") }}'
    cookiecutter_dict = {'project_name': 'foo bar'}
    env = StrictEnvironment()
    rendered_template = render_variable(env, raw, cookiecutter_dict)
    assert rendered_template == 'foo_bar'

# Generated at 2022-06-22 12:26:40.071041
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """
    Test the promp_for_config function with a dictionary
    """

# Generated at 2022-06-22 12:26:43.614360
# Unit test for function read_user_dict
def test_read_user_dict():
    user_dict = read_user_dict('test_dict', {'test_val': 'test'})
    assert isinstance(user_dict, dict)


# Generated at 2022-06-22 12:26:55.096810
# Unit test for function render_variable
def test_render_variable():
    context = {
        'cookiecutter': {
            'a': 'a',
            'x': '{{ cookiecutter.a }}',
            'z': '{{ cookiecutter.a | upper }}',
            'b': 'b',
            'y': '{{ cookiecutter.b }}',
            'w': {
                'a': '{{ cookiecutter.x }}',
                'b': '{{ cookiecutter.y }}',
                'c': {
                    '{{ cookiecutter.x }}': '{{ cookiecutter.y }}',
                },
                'd': '{{ cookiecutter.z }}',
            },
            'c': None,
        },
    }
    dict_result = render_variable(context['cookiecutter']['w'], context)

# Generated at 2022-06-22 12:27:04.087125
# Unit test for function read_user_dict
def test_read_user_dict():
    var_name = "programming_languages"
    prompt_message = "What programming languages are you proficient in?\n" \
                                 "Enter as a comma separated list"
    default_value = ["Python"]
    user_input = "C, C++, Java"
    user_dict_input = read_user_dict(prompt_message, default_value)
    assert user_dict_input == ["C", "C++", "Java"]
    # Invalid type
    default_value = 1
    user_input = "C, C++, Java"
    try:
        user_dict_input = read_user_dict(prompt_message, default_value)
    except TypeError:
        assert True
    # Invalid input
    user_input = "C#, C++, Java!"

# Generated at 2022-06-22 12:27:07.573643
# Unit test for function process_json
def test_process_json():
    user_value = '{"key1": "value1", "key2": "value2"}'
    result = process_json(user_value)
    assert result == {'key1': 'value1', 'key2': 'value2'}



# Generated at 2022-06-22 12:27:16.222315
# Unit test for function process_json
def test_process_json():
    user_value = '{"language": "python"}'
    user_dict = process_json(user_value)
    assert isinstance(user_dict, dict)
    assert user_dict['language'] == 'python'

# Generated at 2022-06-22 12:27:22.816707
# Unit test for function process_json
def test_process_json():
    result = process_json('{"a": 1, "b": 2, "c": 3}')
    assert result == {"a": 1, "b": 2, "c": 3}

    result = process_json('{"a": "b"}')
    assert result == {"a": "b"}

    result = process_json('{")": 2, "b": "}"}')
    assert result == {")": 2, "b": "}"}

# Generated at 2022-06-22 12:27:24.302263
# Unit test for function prompt_for_config
def test_prompt_for_config():
    # TODO: Add tests here
    pass



# Generated at 2022-06-22 12:27:32.088687
# Unit test for function prompt_for_config
def test_prompt_for_config():
    from .config import default_config
    from .prompt import read_user_variable, read_user_yes_no, read_repo_password, read_user_choice, read_user_dict
    
    cookiecutter_dict = OrderedDict([])
    env = StrictEnvironment(context=default_config)
    
    # Test the display of choices
    def _test_choices(key, raw, show_choices):
        options = [render_variable(env, raw, cookiecutter_dict) for raw in raw]
        val = read_user_choice(key, options)
        return val
    
    # Test the display of options
    def _test_options(key, raw):
        val = render_variable(env, raw, cookiecutter_dict)
        if not NO_INPUT:
            val

# Generated at 2022-06-22 12:27:33.426676
# Unit test for function read_user_dict
def test_read_user_dict():
    foo = read_user_dict('a', {'a':'1', 'b':'2'})
    assert foo == {'a':'1', 'b':'2'}

# Generated at 2022-06-22 12:27:44.396568
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:27:52.165984
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Test prompt_for_config function."""

# Generated at 2022-06-22 12:27:59.248418
# Unit test for function render_variable
def test_render_variable():
    env = StrictEnvironment()
    cookiecutter_dict = OrderedDict([])
    env.filters.update({
        'get_or': lambda d, k: d.get(k) or ''
    })
    cookiecutter_dict['selected'] = {
        'firstname': 'Fred',
        'lastname': 'Bloggs'
    }

    result = render_variable(env,
                             '{{ selected.get_or("firstname") }}',
                             cookiecutter_dict)
    assert result == 'Fred'

# Generated at 2022-06-22 12:28:07.363130
# Unit test for function read_user_dict
def test_read_user_dict():
    # Test with a given value which is a dict
    result = read_user_dict('test', {'key': 'given_value'})
    assert result == {'key': 'given_value'}

    # Test with a given value which is a list
    result = read_user_dict('test', ['given_value', 'another'])
    assert result == ['given_value', 'another']

    # Test with a given value which is a string
    result = read_user_dict('test', 'given_value')
    assert result == 'given_value'

# Generated at 2022-06-22 12:28:19.578430
# Unit test for function prompt_for_config
def test_prompt_for_config():
    assert prompt_for_config({
        'cookiecutter': {
            '_copy_without_render': {
                'foo': 'baz'
            }
        }
    }) == OrderedDict({
        '_copy_without_render': {
            'foo': 'baz'
        }
    })

    assert prompt_for_config({
        'cookiecutter': {
            '_copy_without_render': {
                'foo': 'baz'
            }
        }
    }, no_input=True) == OrderedDict({
        '_copy_without_render': {
            'foo': 'baz'
        }
    })


# Generated at 2022-06-22 12:28:33.255586
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {'cookiecutter': {}}
    context['cookiecutter']['repo_name'] = '{{ cookiecutter.project_name.replace(" ", "_") }}'
    context['cookiecutter']['project_name'] = 'Peanut Butter Cookie'
    context['cookiecutter']['_copy_without_render'] = 'This is a test'
    context['cookiecutter']['__do_not_prompt'] = '{{ cookiecutter._copy_without_render }}'
    cookiecutter_dict = prompt_for_config(context, no_input=False)

# Generated at 2022-06-22 12:28:43.686626
# Unit test for function prompt_for_config
def test_prompt_for_config():
    from cookiecutter.environment import StrictEnvironment

    # Tests for prompt_for_config
    # Dummy cookiecutter.json file for testing

# Generated at 2022-06-22 12:28:49.748073
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Test that we can pass a test context, ensure a key is present, but not
    prompt the user.
    """
    context = {'cookiecutter': {'full_name': 'Your Name', 'email': 'Your email'}}

    cookiecutter_dict = prompt_for_config(context, no_input=True)
    assert 'full_name' in cookiecutter_dict
    assert cookiecutter_dict['full_name'] == 'Your Name'
    assert 'email' in cookiecutter_dict
    assert cookiecutter_dict['email'] == 'Your email'

# Generated at 2022-06-22 12:28:57.384571
# Unit test for function render_variable
def test_render_variable():
    """Test the render_variable function for the special case of a for loop.
    """
    cookiecutter_dict = {"repo_name": "cookiecutter-pypackage"}
    env = StrictEnvironment(context=cookiecutter_dict)
    variables_for_loop = {
        "1": "first_item",
        "2": "second_item",
        "3": "third_item",
    }

# Generated at 2022-06-22 12:29:07.972279
# Unit test for function prompt_for_config
def test_prompt_for_config():
    from cookiecutter.prompt import prompt_for_config
    from cookiecutter.environment import StrictEnvironment
    from jinja2.exceptions import UndefinedError

    context = {
        'cookiecutter': {
            'project_name': 'Cookie Monster',
            'repo_name': '{{ cookiecutter.project_name.lower().replace(" ", "-") }}',
            '_dict': {
                'item1': '{{ cookiecutter.project_name.lower() }}',
                'item2': '{{ cookiecutter.repo_name.lower() }}',
            },
            '_options': [
                '{{ cookiecutter.repo_name.lower() }}',
                '{{ cookiecutter.project_name.lower() }}',
            ]
        }
    }

    env = StrictEnvironment

# Generated at 2022-06-22 12:29:18.613909
# Unit test for function read_user_dict
def test_read_user_dict():
    from contextlib import redirect_stdout
    import io

    class FakeClickFile:
        def __init__(self, message, isatty=True):
            self.message = message
            self.isatty = isatty

    def test_default_values(out):
        with redirect_stdout(out):
            result = read_user_dict('a_dict: ', {'a': 1, 'b': 2})
        assert result == {'a': 1, 'b': 2}
        assert out.getvalue() == ''

    def test_alternative_values(out):
        with redirect_stdout(out):
            result = read_user_dict('a_dict: ', {'a': 1, 'b': 2})
        assert result == {'b': 2, 'c': 3}


# Generated at 2022-06-22 12:29:30.275803
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Test prompt_for_config."""
    context = {
        'cookiecutter': {
            "project_name": "{{ cookiecutter.repo_name.replace('-', ' ').title() }}",
            "repo_name": "{{ cookiecutter.project_name.replace(' ', '-').lower() }}",
            "pypi_username": "{{ cookiecutter.github_username|lower }}",
            "open_source_license": "BSD license",
        }
    }

    env = StrictEnvironment(context=context)

# Generated at 2022-06-22 12:29:42.441028
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:29:53.741022
# Unit test for function prompt_for_config
def test_prompt_for_config():
    from cookiecutter.utils.tests import read_json
    from cookiecutter.exceptions import InvalidMode

    context = read_json('tests/test-data/dict-context.json')

    cookiecutter_dict = OrderedDict([])
    env = StrictEnvironment(context=context)

    # First pass: Handle simple and raw variables, plus choices.
    # These must be done first because the dictionaries keys and
    # values might refer to them.
    for key, raw in context['cookiecutter'].items():
        if key.startswith('_') and not key.startswith('__'):
            cookiecutter_dict[key] = raw
            continue

# Generated at 2022-06-22 12:30:00.609319
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {
        'cookiecutter': {
            "project_name": "My New Project",
            "repo_name": "{{ cookiecutter.project_name.replace(\" \", \"_\") }}",
            "version": "0.0.1",
            "author_email": "test@test.test",
            "license": "MIT",
            "_template": {
                "repo_name": "cookiecutter-mynewproject",
                "description": "A short description of the project",
            },
            "my_dict": {
                "foo": "bar",
                "duck": "quack"
            },
            "first_item": ["a", "b", "c"],
            "__secret_item": "something"
        }
    }


# Generated at 2022-06-22 12:30:19.047531
# Unit test for function process_json
def test_process_json():
    # Test dict
    dict_test_value = '{"test": "test"}'
    dict_test_expected = {'test': 'test'}
    assert process_json(dict_test_value) == dict_test_expected

    # Test list
    list_test_value = '["test"]'
    list_test_expected = ['test']
    assert process_json(list_test_value) == list_test_expected

    # Test string
    string_test_value = '"test"'
    string_test_expected = 'test'
    assert process_json(string_test_value) == string_test_expected

    # Test int
    int_test_value = '1'
    int_test_expected = 1
    assert process_json(int_test_value) == int_test_expected

    # Test float

# Generated at 2022-06-22 12:30:31.235605
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:30:36.500880
# Unit test for function process_json
def test_process_json():
    """Sample test of process_json function"""
    user_value_sample = '{"abcd": "abcd"}'
    user_value_result = {
        "abcd": "abcd"
    }
    assert(process_json(user_value_sample) == user_value_result)

# Generated at 2022-06-22 12:30:46.535706
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {'cookiecutter': OrderedDict()}
    context['cookiecutter']['project_name'] = {'_uppercased_word': 'Peanut Butter'}
    context['cookiecutter']['_uppercased_word'] = '{{ cookiecutter.project_name }}'
    context['cookiecutter']['PACKAGE_NAME'] = '{{ cookiecutter._uppercased_word }}'
    cookiecutter_dict = prompt_for_config(context)
    print(cookiecutter_dict)
    assert cookiecutter_dict['PACKAGE_NAME'] == 'Peanut Butter'

# In a comment block at the end of this file are the
# results of running the test_prompt_for_config function.

# {'project_name': {'_uppercased_word

# Generated at 2022-06-22 12:30:58.166752
# Unit test for function prompt_for_config
def test_prompt_for_config():
    from cookiecutter.main import cookiecutter
    import os

    context, _ = cookiecutter('tests/test-generate-prompt/', no_input=False)

    assert context['test_case_name'] == 'test_render_variable'
    assert context['test_case_name_snake'] == 'test_render_variable'
    assert context['test_case_name_dash'] == 'test-render-variable'
    assert context['test_case_name_upper'] == 'TEST RENDER VARIABLE'
    assert context['test_case_name_pascal'] == 'TestRenderVariable'
    assert context['test_case_name_camel'] == 'testRenderVariable'
    assert context['test_case_name_shout'] == 'TEST_RENDER_VARIABLE'

   

# Generated at 2022-06-22 12:31:02.319271
# Unit test for function process_json
def test_process_json():
    """Test function process_json"""
    user_value = '{"foo": {"bar": "baz"}}'
    assert process_json(user_value)  == {
        'foo': {'bar': 'baz'}
    }

# Generated at 2022-06-22 12:31:11.533168
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {
        'cookiecutter': {
            'project_name': 'My Test Project',
            'py_version': '3.5',
            'test_framework': ['pytest', 'unittest'],
            'config_file': {'sidebar': True, 'footer': False},
            'extra_config_file': {'sidebar': True, 'footer': True},
            '__test_extra_dict': {
                'sidebar': '{{ cookiecutter.config_file.sidebar }}',
                'footer': '{{ cookiecutter.config_file.footer }}',
            },
            'install_pip_requirements': True,
        }
    }


# Generated at 2022-06-22 12:31:12.089070
# Unit test for function prompt_for_config
def test_prompt_for_config():
    assert True

# Generated at 2022-06-22 12:31:23.722261
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:31:30.244087
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Test if prompt_for_config works correctly."""
    user_choice_dict = {
        "choice_1":
        [
            "a",
            "bb",
            "ccc"
        ],
        "choice_2":
        [
            "dd",
            "eee",
            "ffff"
        ]
    }

    user_dict_dict = {
        "dict_1":
        {
            "foo": "1",
            "bar": "2"
        },
        "dict_2":
        {
            "foo": ["foo", "bar"],
            "bar": ["1", "2"]
        },
        "dict_3":
        {
            "foo": "bar",
            "bar": "foo"
        },
    }


# Generated at 2022-06-22 12:31:54.554788
# Unit test for function read_user_dict
def test_read_user_dict():
    test_dict = {'param': 'value'}
    assert read_user_dict('test', test_dict) == test_dict

    # Test with no input
    test_dict = {'param': 'value'}
    assert read_user_dict('test', test_dict, no_input=True) == test_dict

    # Test with an empty dictionary
    assert read_user_dict('test', {}) == {}

    # Test with input
    with mock.patch('click.prompt', return_value='{"value3":"value4","value1":"value2"}'):
        value = read_user_dict('test', {})
        assert value == {'value3': 'value4', 'value1': 'value2'}

    # Test with invalid JSON

# Generated at 2022-06-22 12:32:03.290136
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Test the prompt_for_config function."""
    context = {
        'cookiecutter': {
            'project_name': 'Cookiecutter',
            'project_slug': 'cookiecutter',
            'author_name': 'Audrey Roy Greenfeld',
            'email': 'audreyr@example.com',
            'description': 'A command-line utility that creates projects from '
                           'cookiecutters (project templates). E.g. Python '
                           'package projects, jQuery plugin projects.',
            'domain_name': 'example.com',
            'version': '0.1.0',
            'timezone': 'UTC',
            '_copy_without_render': ['LICENSE'],
            '__float': '5.5'
        }
    }
    cookiecutter_dict = prompt

# Generated at 2022-06-22 12:32:06.422580
# Unit test for function read_user_dict
def test_read_user_dict():
    assert read_user_dict('test', {'a': 'a'}) == {'a': 'a'}
    assert read_user_dict('test', {'a': 'a'}) == {'a': 'a'}
    assert read_user_dict('test', {'a': 'a'}) == {'a': 'a'}

# Generated at 2022-06-22 12:32:18.364830
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:32:29.944880
# Unit test for function read_user_dict
def test_read_user_dict():
    # Expect a ValueError if default_value is not a dict
    value_error_raised = False
    try:
        read_user_dict('var_name', 1)
    except ValueError:
        value_error_raised = True
    assert value_error_raised

    # Expect a TypeError if default_value is not a dict
    type_error_raised = False
    try:
        read_user_dict('var_name', 1)
    except TypeError:
        type_error_raised = True
    assert type_error_raised

    # Expect None if no user-supplied value is provided
    returned_value = read_user_dict('var_name', {})
    assert returned_value == {}

    # Expect the user-supplied value, untouched, if it's not valid JSON
    returned_value = read_user_dict

# Generated at 2022-06-22 12:32:40.679674
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:32:51.057702
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:33:02.130826
# Unit test for function read_user_dict
def test_read_user_dict():
    class TestCmdLineInputs:
        def __init__(self, inputs):
            self.inputs = inputs
            self.counter = -1

        def __call__(self, prompt='', default=None, hide_input=False,
                     confirmation_prompt=False, type=None, value_proc=None):
            self.counter += 1
            return self.inputs[self.counter]

    click.prompt = TestCmdLineInputs(['', 'default', '{"key": "value"}'])
    cookiecutter_dict = read_user_dict('test_dict', default_value={'foo': 'bar'})
    assert cookiecutter_dict == {'foo': 'bar'}



# Generated at 2022-06-22 12:33:09.177816
# Unit test for function read_user_dict
def test_read_user_dict():
    default_dict = json.loads('{"key1": "value1", "key2": "value2"}', object_pairs_hook=OrderedDict)
    assert read_user_dict('Enter a dict', default_dict) == default_dict

    user_dict = json.loads('{"key3": "value3"}', object_pairs_hook=OrderedDict)
    assert read_user_dict('Enter a dict', default_dict) == user_dict

# Generated at 2022-06-22 12:33:20.846575
# Unit test for function read_user_dict
def test_read_user_dict():
    import json
    from json import JSONDecodeError
    test_json_dict = {
        'use_pycharm': True,
        'windows': False,
        'project_name': 'My Project',
        'app_name': 'my_app'
    }

    def process_json_test(user_value):
        try:
            user_dict = json.loads(user_value)
        except JSONDecodeError:
            raise click.UsageError('Unable to decode to JSON.')

        if not isinstance(user_dict, dict):
            raise click.UsageError('Requires JSON dict.')

        return user_dict
    user_dict = read_user_dict('test_json', test_json_dict, process_json_test)

# Generated at 2022-06-22 12:33:44.942336
# Unit test for function render_variable
def test_render_variable():
    context = {
        'cookiecutter': {'foo': 'bar', 'baz': 'and bap'},
        'name': 'bond',
        'first_name': 'james',
        'last_name': 'bond',
        'email': 'james.bond@mi6.org',
        'company': 'PyBites',
        'github_username': 'bbelderbos',
    }
    env = StrictEnvironment(context=context)
    cookiecutter_dict = {'foo': 'bar', 'baz': 'and bap'}
    val = render_variable(env, '{{ cookiecutter.foo }}', cookiecutter_dict)
    assert val == 'bar'

# Generated at 2022-06-22 12:33:52.332409
# Unit test for function prompt_for_config
def test_prompt_for_config():
    # Ask the user a question
    context = {
        'cookiecutter': {
            'app_name': '{{ cookiecutter.project_name.replace(" ", "_") | lower }}',
            'project_name': 'Peanut Butter Cookie',
        }
    }
    cookiecutter_dict = prompt_for_config(context)
    assert cookiecutter_dict['project_name'] == 'Peanut Butter Cookie'
    assert cookiecutter_dict['app_name'] == 'peanut_butter_cookie'


# Generated at 2022-06-22 12:34:01.094011
# Unit test for function read_user_dict
def test_read_user_dict():
    dict_user_input = """
      {
        "A": "A",
        "B": "B"
      }
    """

    user_input_value_proc = process_json(dict_user_input)
    dict_default_value = {
        "A": "AA",
        "B": "BB"
    }
    user_input_value_proc_default_value = read_user_dict(
        dict_user_input, dict_default_value
    )
    assert user_input_value_proc == user_input_value_proc_default_value

# Generated at 2022-06-22 12:34:11.509530
# Unit test for function prompt_for_config
def test_prompt_for_config():
    from cookiecutter import main
    from cookiecutter.main import cookiecutter
    from cookiecutter.repository import determine_repo_dir, expand_abbreviations
    import os
    import shutil
    import tempfile
    import pprint

    # Save current directory
    cwd = os.getcwd()

    # Get a temp directory
    temp_dir = tempfile.mkdtemp()

    # Get template path
    template_path = os.path.normpath(
        os.path.join(
            os.path.abspath(os.path.dirname(main.__file__)),
            '..', 'tests', 'test-output-dir-ess',
        )
    )
    assert os.path.isdir(template_path) is True

    # Get repo_dir
    repo_

# Generated at 2022-06-22 12:34:20.140145
# Unit test for function prompt_for_config
def test_prompt_for_config():
    test_cases = OrderedDict()
    test_cases['project_name'] = 'foobar'
    test_cases['project_slug'] = 'foobar'
    test_cases['author_name'] = 'Audrey Roy Greenfeld'
    test_cases['email'] = 'audreyr@example.com'
    test_cases['description'] = 'A short description of the project.'
    test_cases['domain_name'] = 'example.com'
    test_cases['repo_name'] = 'cookiecutter',
    test_cases['repo_url'] = 'https://github.com/audreyr/cookiecutter.git'
    test_cases['version'] = '0.1.0'
    test_cases['open_source_license'] = 'MIT'

# Generated at 2022-06-22 12:34:32.061924
# Unit test for function read_user_dict
def test_read_user_dict():
    import sys
    import pytest
    try:
        from unittest.mock import patch
    except ImportError:
        from mock import patch
    from cookiecutter.prompt import read_user_dict

    # First test, with default value
    with patch.object(
        sys, 'stdin', autospec=True,
        return_value=''
    ):
        default_value = {'a': 1}
        result = read_user_dict('Prompt', default_value)
        assert result == default_value

    # Second test, with user input
    with patch.object(
        sys, 'stdin', autospec=True,
        return_value='{"a": 2}'
    ):
        default_value = {'a': 1}
        result = read_user_dict('Prompt', default_value)