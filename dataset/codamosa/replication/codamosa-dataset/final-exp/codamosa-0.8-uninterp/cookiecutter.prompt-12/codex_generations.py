

# Generated at 2022-06-22 12:24:48.101095
# Unit test for function read_user_dict
def test_read_user_dict():
    # test empty dictionary
    user_dict = read_user_dict("Enter a dictionary in JSON format: ", {})
    assert user_dict == {}

    user_dict = read_user_dict("Enter a dictionary in JSON format: ", {"key": "value"})
    assert user_dict == {"key": "value"}

    # test for a dictionary with nested dictionary
    user_dict = read_user_dict("Enter a dictionary in JSON format: ", {"key": {"nested_key":"value"}})
    assert user_dict == {"key": {"nested_key":"value"}}

    # test for a dictionary with nested list
    user_dict = read_user_dict("Enter a dictionary in JSON format: ", {"key": ["value1", "value2"]})
    assert user_dict == {"key": ["value1", "value2"]}



# Generated at 2022-06-22 12:24:53.089977
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {"cookiecutter": {"repo_name": "Cookiecutter", "slugify_name": "cookiecutter"}}
    context = prompt_for_config(context, no_input=True)
    assert context['repo_name'] == 'Cookiecutter'
    assert context['slugify_name'] == 'cookiecutter'


# Generated at 2022-06-22 12:24:59.911929
# Unit test for function process_json
def test_process_json():
    assert process_json('{"dict_key": "dict_val"}') == {'dict_key': 'dict_val'}
    assert process_json('{"dict_key": {"sub_key": "sub_val"}}') == {'dict_key': {'sub_key': 'sub_val'}}
    assert process_json('{"int_key": 1}') == {'int_key': 1}

# Generated at 2022-06-22 12:25:10.657437
# Unit test for function read_user_dict
def test_read_user_dict():
    dict_test = OrderedDict([('test', 'test')])
    assert read_user_dict('test', dict_test) == dict_test
    # dict with dicts
    dict_test2 = OrderedDict([('test', {'test': 'test'})])
    assert read_user_dict('test', dict_test2) == dict_test2
    # dict with lists
    dict_test3 = OrderedDict([('test', [1, 2, 3])])
    assert read_user_dict('test', dict_test3) == dict_test3
    # dict with string
    dict_test4 = OrderedDict([('test', 'test')])
    assert read_user_dict('test', dict_test4) == dict_test4



# Generated at 2022-06-22 12:25:19.148796
# Unit test for function prompt_for_config
def test_prompt_for_config():
    from cookiecutter.main import cookiecutter
    from pytest import raises
    from .fake_context import FakeContext
    import os
    import shutil
    import tempfile
    import json

    # Setup a fake context for Cookiecutter
    temp_folder = tempfile.mkdtemp()
    fake_json_context_file = os.path.join(temp_folder, 'cookiecutter.json')

    with open(fake_json_context_file, 'w') as f:
        f.write(json.dumps(FakeContext, indent=4))

    # Make sure we can get the prompt
    context = cookiecutter(temp_folder)
    assert context['repo_name'] == 'Cookiecutter'
    assert context['project_name'] == 'Cookiecutter'

    # Try some bad input

# Generated at 2022-06-22 12:25:23.934136
# Unit test for function prompt_for_config
def test_prompt_for_config():
    from .main import generate_context
    from .main import get_context_variables
    from .main import get_repo_info

    # Load the config from a local repo_name
    context = generate_context(None, repository_dir='./tests/test-repo-pre/', no_input=True)

    # do the thing you want to test
    cookiecutter_dict = prompt_for_config(context, no_input=True)

# Generated at 2022-06-22 12:25:35.582826
# Unit test for function process_json
def test_process_json():
    user_inputs = [
        ('{"foo":"bar"}', {"foo": "bar"}),
        ('{"foo":1}', {"foo": 1}),
        ('{"foo":true}', {"foo": True}),
        ('{"foo":null}', {"foo": None}),
        ('{"foo":{"bar":"baz"}}', {"foo": {"bar": "baz"}}),
        ('{"foo":{"bar":1}}', {"foo": {"bar": 1}}),
        ('{"foo":[{"bar":"baz"},{"bar":1}]}', {"foo": [{"bar": "baz"}, {"bar": 1}]}),
    ]

    for user_input, output in user_inputs:
        assert output == process_json(user_input)

# Generated at 2022-06-22 12:25:41.024587
# Unit test for function process_json
def test_process_json():
    """Testing for function process_json."""
    assert process_json('{"name": "Tester", "status": "FullTime"}') == {
        'name': 'Tester',
        'status': 'FullTime',
    }
    assert process_json('{"name": "Tester"}') == {'name': 'Tester'}
    assert process_json('{"status": "FullTime"}') == {'status': 'FullTime'}

# Generated at 2022-06-22 12:25:52.297065
# Unit test for function read_user_dict
def test_read_user_dict():
    new_context_data = {
        "cookiecutter": {
            'first_name': 'John',
            'last_name': 'Doe',
            "address": {
                "street": "123 Sesame St.",
                "city": "New York",
            }
        }
    }
    user_context = prompt_for_config(new_context_data, no_input=True)
    assert user_context['first_name'] == 'John'
    assert user_context['last_name'] == 'Doe'
    assert 'address' in user_context
    assert len(user_context['address'].keys()) == 2
    assert user_context['address']['street'] == "123 Sesame St."
    assert user_context['address']['city'] == "New York"


# Generated at 2022-06-22 12:25:53.753305
# Unit test for function prompt_for_config
def test_prompt_for_config():
    pass #TODO: Write a unit test for function prompt_for_config

# Generated at 2022-06-22 12:26:06.578555
# Unit test for function prompt_for_config
def test_prompt_for_config():
    # We are creating a simple context to test this function.
    context = {
        'cookiecutter': {'project_name': 'Cool Project', 'version': '0.1.0'}
    }
    cookiecutter_dict = prompt_for_config(context, no_input=True)

    # Assert that the user input is the same as the input defined in the
    # context variable.
    assert cookiecutter_dict == context['cookiecutter']

# Generated at 2022-06-22 12:26:09.826362
# Unit test for function read_user_dict
def test_read_user_dict():
    read_user_dict('var_name','options')   


# Generated at 2022-06-22 12:26:12.499371
# Unit test for function read_user_dict
def test_read_user_dict():
    user_dict = read_user_dict("question", {"c": "d"})
    assert user_dict == {"c": "d"}
    assert type(user_dict) is dict

# Generated at 2022-06-22 12:26:15.304506
# Unit test for function process_json
def test_process_json():
    try:
        test_value = process_json('{}')
    except:
        test_value = False

    assert test_value == {}


# Generated at 2022-06-22 12:26:20.187586
# Unit test for function read_user_dict
def test_read_user_dict():
    assert read_user_dict('test_read_user_dict', {'test_read_user_dict': 'test_read_user_dict'}) == {'test_read_user_dict': 'test_read_user_dict'}

if __name__ == '__main__':
    test_read_user_dict()

# Generated at 2022-06-22 12:26:25.494680
# Unit test for function read_user_dict
def test_read_user_dict():
    var_name = 'Var Name'
    default_value = {'default': 'value'}
    assert read_user_dict(var_name, default_value) == default_value

    user_value = '{"item": "value"}'
    assert read_user_dict(var_name, default_value) == json.loads(user_value)

# Generated at 2022-06-22 12:26:34.154108
# Unit test for function render_variable
def test_render_variable():
    """Test that rendering is working as expected."""
    from cookiecutter.environment import StrictEnvironment
    env = StrictEnvironment(context={'cookiecutter': {}})
    data = {
        'cookiecutter': {
            'name': "{{cookiecutter.greeting}} {{cookiecutter.surname}}",
            'greeting': "Hello",
            'surname': "World"
        }
    }
    rendered = render_variable(env, data, data['cookiecutter'])
    assert rendered['name'] == 'Hello World'

# Generated at 2022-06-22 12:26:38.108831
# Unit test for function read_user_dict
def test_read_user_dict():
    user_dict = read_user_dict("test", {'a':'b'})
    assert isinstance(user_dict, dict)
    assert user_dict == {'a':'b'}

# Generated at 2022-06-22 12:26:44.105372
# Unit test for function read_user_dict
def test_read_user_dict():
    default_dict = {'key1':'value1', 'key2':'value2'}
    assert read_user_dict('test',default_dict) == default_dict
    assert read_user_dict('test',[1,2,3]) == [1,2,3]


if __name__ == '__main__':
    test_read_user_dict()

# Generated at 2022-06-22 12:26:55.581063
# Unit test for function prompt_for_config
def test_prompt_for_config():
    # Test 1
    context = {
        'cookiecutter': {
            'project_name': 'Awesome Project',
            'repo_name': '{{ cookiecutter.project_name.lower().replace(" ", "-") }}',
        }
    }
    expected = {
        'project_name': 'Awesome Project',
        'repo_name': 'awesome-project',
    }

    actual = prompt_for_config(context)
    assert actual == expected

    # Test 2
    context = {
        'cookiecutter': {
            'project_name': 'Awesome Project',
            'repo_name': '{{ cookiecutter.project_name.lower().replace(" ", "-") }}',
            'is_open_source': True,
            'license': 'MIT license',
        }
    }

# Generated at 2022-06-22 12:27:10.582439
# Unit test for function prompt_for_config
def test_prompt_for_config():
    # Tests for choices feature
    context = {
        'cookiecutter': {
            "repo_name": "{{ cookiecutter.project_name.replace(' ', '_') }}",
            'license': [
                'MIT license',
                'BSD license',
                'ISC license',
                'Apache Software License 2.0',
                'GNU General Public License v3',
            ],
            'open_source_license': True,
            '_no_input': 'True',
        }
    }
    # Tests for choices feature

# Generated at 2022-06-22 12:27:21.715492
# Unit test for function prompt_for_config
def test_prompt_for_config():
    from cookiecutter.main import cookiecutter

    # Test that name variable is in the final output
    context = cookiecutter('tests/fake-repo-tmpl/', no_input=False)
    assert 'project_name' in context

    # Test that email variable is in the final output
    context = cookiecutter('tests/fake-repo-tmpl/', no_input=False)
    assert 'email' in context

    # Test that repo_name variable is in the final output
    context = cookiecutter('tests/fake-repo-tmpl/', no_input=False)
    assert 'repo_name' in context

    # Test that project_name matches the input
    context = cookiecutter('tests/fake-repo-tmpl/', no_input=False)

# Generated at 2022-06-22 12:27:31.100853
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Unit test for function prompt_for_config."""

# Generated at 2022-06-22 12:27:42.222951
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {
        "cookiecutter": {
            "_copy_without_render": [
                ".pre-commit-config.yaml",
                "{{cookiecutter.repo_name}}/tests/",
            ],
            "_copy_without_render_test_dotfiles": [".coveragerc"],
            "license": "MIT",
            "repo_name": "{{cookiecutter.project_name.lower()|replace(' ', '-')}}",
            "project_short_description": "A short description of {{cookiecutter.project_name}}.",
            "project_name": "{{cookiecutter.project_name.lower()|replace(' ', '_')}}",
        }
    }

# Generated at 2022-06-22 12:27:49.254167
# Unit test for function prompt_for_config
def test_prompt_for_config():

    # Setup
    context = {"cookiecutter": {"full_name": "Audrey Roy"}}
    no_input = False
    _input = "Audrey Roy Greenfeld"
    expected_output = "Audrey Roy Greenfeld"

    import builtins

    def mock_input(s):
        return _input

    builtins.input = mock_input

    # Test
    output = prompt_for_config(context, no_input)

    # Verify
    assert output == expected_output

# Generated at 2022-06-22 12:27:59.839534
# Unit test for function process_json
def test_process_json():
    """Test that process_json can handle all kinds of inputs"""
    assert process_json('{"hello": "world"}') == {'hello': 'world'}
    assert process_json('{"hello": "world,"}') == {'hello': 'world,'}
    assert process_json('{"hello": "world."}') == {'hello': 'world.'}
    assert process_json('{"hello": "world!"}') == {'hello': 'world!'}
    assert process_json('{"hello": "world?"}') == {'hello': 'world?'}
    assert process_json('{"hello": "world:", "hello2": "world2"}') == {'hello': 'world:', 'hello2': 'world2'}

# Generated at 2022-06-22 12:28:11.775857
# Unit test for function read_user_dict
def test_read_user_dict():
    choice_map = OrderedDict(
        ('{}'.format(i), value) for i, value in enumerate(["foo", "bar"], 1)
    )
    choices = choice_map.keys()
    default = '1'
    choice_lines = ['{} - {}'.format(*c) for c in choice_map.items()]
    prompt = '\n'.join(
        (
            'Select {}:'.format("var_name"),
            '\n'.join(choice_lines),
            'Choose from {}'.format(', '.join(choices)),
        )
    )
    user_choice = click.prompt(
        prompt, type=click.Choice(choices), default=default, show_choices=False
    )
    assert choice_map[user_choice] == "foo"

# Generated at 2022-06-22 12:28:23.298012
# Unit test for function read_user_dict
def test_read_user_dict():
    """Unit test for function read_user_dict."""
    assert read_user_dict(
        "Do you want to add another dependency?", {"server": "CherryPy"}
    ) == {"server": "CherryPy"}
    assert read_user_dict(
        "Do you want to add another dependency?", {"server": "CherryPy"}
    ) == {"server": "CherryPy"}
    # Ensure that the user input is accepted when valid JSON is entered.
    assert read_user_dict(
        "Do you want to add another dependency?", {"server": "CherryPy"}
    ) == {'server_1': 'Flask'}
    assert read_user_dict(
        "Do you want to add another dependency?", {"server": "CherryPy"}
    ) == {'server': 'CherryPy'}

    assert read_

# Generated at 2022-06-22 12:28:28.978618
# Unit test for function prompt_for_config
def test_prompt_for_config():
    from cookiecutter.main import cookiecutter

    # Make sure the user is prompted for new config
    context = cookiecutter('tests/test-cookiecutters/', no_input=False)
    assert context['cookiecutter']['repo_name'] == 'cookiecutter-pypackage'
    assert context['cookiecutter']['package_name'] == 'cookiecutter'
    assert context['cookiecutter']['open_source_license'] == 'MIT license'



# Generated at 2022-06-22 12:28:37.008095
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {
        'cookiecutter': {
            'project_name': 'Default',
            '_template': {
                'repo_name': 'Default',
                'repo_url': 'https://github.com/{0}/{0}.git'.format(
                    '{{ cookiecutter.repo_name }}')
            }
        }
    }

    cookiecutter_dict = prompt_for_config(context)
    assert cookiecutter_dict['project_name'] == 'Default'


# Generated at 2022-06-22 12:28:56.036711
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Test prompt_for_config to return a dictionary of values.

    This test will pass if the function prompt_for_config returns a dictionary
    of values.
    """
    # Create a context to be rendered
    test_context = {'cookiecutter': {'project_name': 'test_project', 'boolean': True}}
    # Create a prompt for the user to answer
    test_cookiecutter_dict = prompt_for_config(test_context, no_input=True)
    # Check if the test_cookiecutter_dict is a dictionary
    assert isinstance(test_cookiecutter_dict, dict)
    # Check if the test_cookiecutter_dict contains the key 'project_name'
    assert 'project_name' in test_cookiecutter_dict
    # Check if the value of the key 'project_name'

# Generated at 2022-06-22 12:29:07.549777
# Unit test for function read_user_dict
def test_read_user_dict():
    import json

    dict_input = '{}'
    dict_output = {
        "key1": "value1",
        "key2": "value2"
    }
    dict_output = json.dumps(dict_output)
    assert(dict_output == json.dumps(process_json(dict_input)))

    dict_input = '{\n"key1": "value1",\n "key2": "value2"\n}'
    dict_output = {
        "key1": "value1",
        "key2": "value2"
    }
    dict_output = json.dumps(dict_output)
    assert(dict_output == json.dumps(process_json(dict_input)))


# Generated at 2022-06-22 12:29:10.962926
# Unit test for function read_user_dict
def test_read_user_dict():
    import doctest
    doctest.testmod(verbose=True)

if __name__=='__main__':
    test_read_user_dict()
    print(prompt_for_config(context))

# Generated at 2022-06-22 12:29:20.499189
# Unit test for function prompt_for_config
def test_prompt_for_config():
    import os
    import tempfile

    context = {
        'cookiecutter': {
            'project_name': 'Awesome Project',
            'project_slug': 'awesome_project',
            'repo_name': 'awesome_project',
            'keys': [
                'key1',
                'key2',
                'key3'
            ]
        }
    }

    write_file_contents = '{{ cookiecutter.project_name }} {{ cookiecutter.project_slug }} {{ cookiecutter.repo_name }}'

    with tempfile.TemporaryDirectory() as tmp_dir:
        write_file = os.path.join(tmp_dir, 'write_file')
        hidden_file = os.path.join(tmp_dir, 'hidden_file')

        cookiecutter_dict = prompt

# Generated at 2022-06-22 12:29:23.902589
# Unit test for function process_json
def test_process_json():
    user_dict = {'a':'1', 'b':'2'}
    user_value = json.dumps(user_dict)
    result_dict = process_json(user_value)
    assert user_dict == result_dict

test_process_json()

# Generated at 2022-06-22 12:29:25.814026
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """
    Test the function prompt_for_config
    """
    assert callable(prompt_for_config)

# Generated at 2022-06-22 12:29:37.598537
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {
        'cookiecutter': {
            'full_name': 'First Last',
            'email': 'first.last@gmail.com',
            'github_username': 'username',
            'project_name': 'project_name',
            'project_slug': '{{ cookiecutter.project_name.replace(" ", "_") }}',
            'project_type': "thing"
        }
    }

    cookiecutter_dict = prompt_for_config(context, no_input=False)

# Generated at 2022-06-22 12:29:44.925610
# Unit test for function read_user_dict
def test_read_user_dict():
    # Create a new console prompt to collect user input
    # Please see https://click.palletsprojects.com/en/7.x/api/#click.get_text_stream
    click_prompt = click.get_text_stream('stdin')

    # Create a new click context for the function
    # Please see https://click.palletsprojects.com/en/7.x/api/#click.Context
    click_context = click.Context(read_user_dict)

    user_value = '{"my-key": "my-value"}'

    # Mock the raw_input function call inside click as this function is
    # not available in Python 3 (Python 3 has input)
    # Please see https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch

# Generated at 2022-06-22 12:29:55.529882
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:29:57.735972
# Unit test for function process_json
def test_process_json():
    user_dict = {'a': '1', 'b':'2'}
    user_value = '{"a": "1", "b": "2"}'
    assert process_json(user_value) == user_dict

# Generated at 2022-06-22 12:30:12.743867
# Unit test for function read_user_dict
def test_read_user_dict():
    user_dict = read_user_dict('user_dict', {'key': 'value'})
    assert isinstance(user_dict, dict)
    assert user_dict['key'] == 'value'

# Generated at 2022-06-22 12:30:19.199982
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Unit test for function prompt_for_config"""
    # Fixture

# Generated at 2022-06-22 12:30:31.334748
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:30:34.309822
# Unit test for function process_json
def test_process_json():
    user_value = '{"name":"hong", "age":"20"}'
    assert (process_json(user_value)['name'] == 'hong')

# Generated at 2022-06-22 12:30:44.003770
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {
        'cookiecutter': {
            'project_name': 'My Project',
            '_template': {
                'project_name': 'My Project',
                'project_slug': 'my_project',
                'cookiecutter': {
                    'repo_name': 'My Project',
                    'repo_slug': 'my_project'
                }
            }
        }
    }

    cookiecutter_dict = prompt_for_config(context, True)
    assert cookiecutter_dict['project_name'] == 'My Project'
    assert cookiecutter_dict['project_slug'] == 'my_project'
    assert cookiecutter_dict['cookiecutter']['repo_name'] == 'My Project'

# Generated at 2022-06-22 12:30:56.324301
# Unit test for function read_user_dict
def test_read_user_dict():
    # basic test
    default_value = {'a': 1, 'b': 2}
    user_value = "{\"a\": 3, \"c\": 4}"
    expected_value = {"a": 3, "c": 4}
    assert read_user_dict('test_dict', default_value) == expected_value
    # test with a empty dictionary
    user_value = "{}"
    expected_value = {}
    assert read_user_dict('test_dict', default_value) == expected_value
    # test with a dictionary with only key
    user_value = "{\"b\": 2}"
    expected_value = {"b": 2}
    assert read_user_dict('test_dict', default_value) == expected_value
    # test with a dictionary with only value
    user_value = "{\"a\": 1}"
    expected_

# Generated at 2022-06-22 12:30:58.264538
# Unit test for function read_user_dict
def test_read_user_dict():
    assert read_user_dict('repo_name', 'test_cookiecutter') == 'test_cookiecutter'

# Generated at 2022-06-22 12:31:09.165294
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Test prompt_for_config with different types of inputs.

    The test_inputs and the expected_outputs should be updated to
    test the user input cases.
    """
    # Testing a simple question
    test_inputs = {
        "cookiecutter": {
            "name": "test_name",
            "version": "test_version",
            "description": "test_description"
        }
    }

    expected_outputs = {
        'name': 'test_name',
        'version': 'test_version',
        'description': 'test_description'
    }

    cookiecutter_dict = prompt_for_config(test_inputs)

    assert expected_outputs == cookiecutter_dict

    # Testing a simple question. Assume that user entered no inputs.

# Generated at 2022-06-22 12:31:17.757995
# Unit test for function prompt_for_config
def test_prompt_for_config():
    no_input = False

# Generated at 2022-06-22 12:31:28.536886
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:32:00.751236
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Test the prompt_for_config function."""
    import os
    import json
    import re
    import subprocess
    #The following module didn't work in Python 3.
    # import mock
    #============================================================================
    #    with mock.patch('click.prompt', return_value='tiger'): 
    #         prompt_for_config(
    #             {'cookiecutter': {'animal': 'dog'}},
    #             no_input=False
    #         )
    #============================================================================
    #The following is a work around for the above module.
    if not os.path.exists('cookiecutter_test'):
        os.mkdir('cookiecutter_test')
    os.chdir('cookiecutter_test')

# Generated at 2022-06-22 12:32:09.368954
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {
        'cookiecutter': {
            'project_name': 'Test',
            'author_name': 'Test Biggins',
            'license': 'MIT',
            'email': 'test@example.com',
            'version': '0.1.0'
        }
    }
    cookiecutter_dict = prompt_for_config(context, no_input=True)
    assert cookiecutter_dict == {
        'project_name': 'Test',
        'author_name': 'Test Biggins',
        'license': 'MIT',
        'email': 'test@example.com',
        'version': '0.1.0'
    }

# Generated at 2022-06-22 12:32:17.484682
# Unit test for function read_user_dict
def test_read_user_dict():
    """Testing inputs for the function read_user_dict."""

    # Setup
    user_value = '{"hello": "world", "foo": "{{cookiecutter.bar}}"}'
    result = {'hello': 'world', 'foo': '{{cookiecutter.bar}}'}
    expected = {'hello': 'world', 'foo': '{{cookiecutter.bar}}'}

    cookiecutter_dict = {}

    env = StrictEnvironment()

    # Execute
    result = process_json(user_value)

    # Verify
    assert (result == expected)

# Generated at 2022-06-22 12:32:20.886697
# Unit test for function prompt_for_config
def test_prompt_for_config():
    try:
        from cookiecutter import prompt
        from cookiecutter import config
        from cookiecutter import utils
        from cookiecutter import main
        from cookiecutter import cli
        from cookiecutter import __main__ as cookiecutter_main
    except:
        print('test_prompt_for_config failed')


test_prompt_for_config()



# Generated at 2022-06-22 12:32:27.322937
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {
        'cookiecutter': {
            'project_name': 'Awesome Project',
            'project_slug': 'awesome_project',
            'pypi_username': 'awesome_username',
            'email': 'you@example.com',
            'description': 'An awesome project. Really!',
            'domain_name': 'example.com',
            'version': '0.1.0',
            'open_source_license': 'MIT license',
            'year': '2014',
            'copyright_holder': 'Your Name',
            'repo_name': 'awesome_project',
            'github_username': 'johndoe',
            'bootstrap_version': '3.3.0',
        }
    }
    no_input = True
    cookiecutter_dict = prompt_

# Generated at 2022-06-22 12:32:32.934962
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Unit test for function prompt_for_config"""
    from cookiecutter.main import cookiecutter
    from cookiecutter.utils.paths import in_repo

    assert in_repo('tests/test-cookiecutters/fake-repo-pre/cookiecutter.json')
    assert in_repo('tests/test-cookiecutters/fake-repo-pre/')
    assert in_repo('tests/test-cookiecutters/fake-repo-pre/README.rst')

    context = cookiecutter(
        'tests/test-cookiecutters/fake-repo-pre/',
        no_input=True,
        output_dir='tests/test-output',
    )

    assert isinstance(context, dict)
    assert context == {}

# Generated at 2022-06-22 12:32:38.873397
# Unit test for function prompt_for_config
def test_prompt_for_config():
    assert prompt_for_config(
        {'cookiecutter': {'key': 'value', 'key2': {'name': 'dict_value'}}}) == \
           {'key': 'value', 'key2': {'name': 'dict_value'}}

if __name__ == "__main__":
    test_prompt_for_config()

# Generated at 2022-06-22 12:32:45.703733
# Unit test for function prompt_for_config
def test_prompt_for_config():
    config_dict = {
        'default_context': {
            'cookiecutter': {'full_name': "Your Name"}
        },
        'cookiecutter_dict': {
            'full_name': "Your Name",
            'project_name': "Akela",
        },
    }
    context = config_dict['default_context']
    cookiecutter_dict = prompt_for_config(context, no_input=True)
    assert cookiecutter_dict == config_dict['cookiecutter_dict']



# Generated at 2022-06-22 12:32:51.291758
# Unit test for function read_user_dict
def test_read_user_dict():
    """Test read_user_dict."""
    dict_ = {'name': 'user_dict'}
    assert dict_ == read_user_dict('user_dict', dict_)

    # Test function with argument default_value = None
    assert {} == read_user_dict('user_dict', None)

    # Test function with argument default_value = list
    assert {} == read_user_dict('user_dict', [])

# Generated at 2022-06-22 12:33:03.281585
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:34:04.466058
# Unit test for function read_user_dict
def test_read_user_dict():
    """Unit test for function read_user_dict."""
    # Can't use click.testing.CliRunner as it is not compatible with
    # pytest-xdist.
    # Thank you to micktwomey on gitter for helping me figure this out.

    # This used to work with click.testing.CliRunner.
    # result = runner.invoke(
    #     cookiecutter.main.cookiecutter,
    #     ['tests/test-cookiecutters'],
    #     input='{"full_name": "Test Author", "email": "test@test.test"}'
    # )
    from click.testing import CliRunner
    from cookiecutter import main as cookiecutter_main
    runner = CliRunner()


# Generated at 2022-06-22 12:34:13.808339
# Unit test for function read_user_dict
def test_read_user_dict():
    from click.testing import CliRunner
    from cookiecutter.prompt import read_user_dict

    def test_prompt_for_config(key, default_value, expected_value):
        runner = CliRunner()
        result = runner.invoke(
            read_user_dict,
            input=expected_value,
            args=[key, default_value],
            catch_exceptions=False,
        )
        assert result.exit_code == 0
        assert result.output == expected_value + '\n'

    test_prompt_for_config(
        key='foo',
        default_value={'k1': 'v1'},
        expected_value='{"k2": "v2"}'
    )


# Generated at 2022-06-22 12:34:21.416262
# Unit test for function read_user_dict
def test_read_user_dict():
    user_input = """{
    "project_name": "TEST_PROJECT_NAME",
    "author": "TEST_AUTHOR",
    "email": "TEST_EMAIL",
    "description": "TEST_DESCRIPTION",
    "project_slug": "TEST_PROJECT_SLUG",
    "release": "remake-engines",
    "repo": "git@github.com:TEST_PROJECT_SLUG/TEST_PROJECT_SLUG.git",
    "version": "0.1.0",
    "year": "2020",
    "select_license": "MIT",
    "open_source_license": "MIT License"
}"""

    answer = read_user_dict('destructive_tests', {}, user_input)

    assert 'author' in answer
