

# Generated at 2022-06-22 12:24:45.685655
# Unit test for function prompt_for_config
def test_prompt_for_config():
    # Test data:
    context = {}
    cookiecutter_dict = OrderedDict([])
    env = StrictEnvironment(context=context)

    # Case 1: Test a regular string variable, without user input.
    dict_key_1 = 'regular_string'
    raw_1 = 'Some String'
    cookiecutter_dict[dict_key_1] = raw_1
    val = render_variable(env, raw_1, cookiecutter_dict)
    assert val == 'Some String'

    # Case 2: Test a regular string variable, with user input.
    dict_key_2 = 'regular_string'
    raw_2 = 'Some String'
    cookiecutter_dict[dict_key_2] = raw_2
    val = render_variable(env, raw_2, cookiecutter_dict)

# Generated at 2022-06-22 12:24:57.053623
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Unit test for function prompt_for_config."""
    import os
    from cookiecutter.main import cookiecutter

    path = os.path.dirname(__file__)
    path = os.path.join(path, '..', '..', 'tests', 'files', 'test-cli', 'bake')
    path = os.path.abspath(path)


# Generated at 2022-06-22 12:25:06.759225
# Unit test for function prompt_for_config
def test_prompt_for_config():
    # Create a first context with some fields
    context_example= {
      "cookiecutter": {
        "full_name": "Your Name",
        "email": "Your email",
        "github_username": "Your username",
        "project_name": "My Project",
        "project_slug": "project_name",
        "pypi_username": "Your PyPI username",
        "select_linter": [
          "flake8",
          "pylint"
        ],
        "select_forms": [
          "django",
          "flask"
        ],
        "open_source_license": [
          "MIT",
          "BSD"
        ],
        "select_test": [
          "pytest",
          "nose"
        ]
      }
    }
    cookiecutter

# Generated at 2022-06-22 12:25:16.265883
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:25:27.899972
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:25:39.444558
# Unit test for function process_json
def test_process_json():
    json_test_string = '{"test1": "test2", "test3": [{"test4": "test5"}]}'
    json_test_string_dict = {'test1': 'test2', 'test3': [{'test4': 'test5'}]}
    assert process_json(json_test_string) == json_test_string_dict
    try:
        process_json(json.dumps(json_test_string)) == json_test_string_dict
    except click.UsageError as err:
        assert "Unable to decode to JSON" in err
    try:
        assert process_json(json.dumps(json_test_string_dict)) == json_test_string_dict
    except click.UsageError as err:
        assert "Requires JSON dict" in err

# Generated at 2022-06-22 12:25:50.668078
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {
        'cookiecutter': {
            'project_name': 'Example',
            'project_slug': '{{ cookiecutter.project_name.lower().replace(" ", "-") }}',
            'repo_name': '{{ cookiecutter.project_name.lower().replace(" ", "-") }}',
            'author_name': 'Your Name',
            'author_username': '{{ cookiecutter.author_name.replace(" ", "").lower() }}',
            'email': 'example@example.com',
            'description': 'A short description of the project.',
            'version': '0.1.0',
            'keywords': 'example',
            'timezone': 'UTC',
            'use_pycharm': 'n',
            'open_source_license': 'MIT'
        }
    }

# Generated at 2022-06-22 12:25:54.180260
# Unit test for function prompt_for_config
def test_prompt_for_config():

    project_dir, project_name, clean_dir = setup()

    cookiecutter_dict = prompt_for_config(
        context={}, no_input=True)
    assert isinstance(cookiecutter_dict, OrderedDict)



# Generated at 2022-06-22 12:26:03.225889
# Unit test for function read_user_dict
def test_read_user_dict():
    # Test if the default value is rendered
    default_to_render = {"foo": [{"bar": ["baz"]}]}
    expected_default = "{'foo': [{'bar': ['baz']}]}"
    assert (
        read_user_dict('test', default_to_render) == expected_default
    )

    # Test if the user value is successfully read and rendered
    user_value = '{"foo": ["bar", "baz"]}'
    expected_user_value = "{'foo': ['bar', 'baz']}"
    assert (
        read_user_dict('test', default_to_render, no_input=False, user_value=user_value) == expected_user_value
    )

    # Test if the user value is empty
    invalid_user_value = ''
    expected_user_

# Generated at 2022-06-22 12:26:12.702804
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:26:26.735142
# Unit test for function read_user_dict
def test_read_user_dict():
    from .replay import get_replay_data
    from .main import cookiecutter

    # Load test context
    replay_data = get_replay_data()
    replay_context = replay_data['replay_context']
    replay_context['cookiecutter']['author_github'] = 'gilles-k'
    replay_context['cookiecutter']['author_email'] = 'gilles_k@yahoo.com'
    replay_context['cookiecutter']['_template'] = 'x/y'

    # Custom test: we add an extra dict variable to prompt for

# Generated at 2022-06-22 12:26:36.099207
# Unit test for function process_json
def test_process_json():
    user_value = '{"foo": "bar", "baz": 1}'
    expected_output = {'foo': 'bar', 'baz': 1}
    actual_output = process_json(user_value)
    assert actual_output == expected_output, 'Output is not as expected'
    user_value = '{"a": ["b", "c", {"d": 5}]}'
    expected_output = {'a': ['b', 'c', {'d': 5}]}
    actual_output = process_json(user_value)
    assert actual_output == expected_output, 'Output is not as expected'

# Generated at 2022-06-22 12:26:40.576942
# Unit test for function process_json
def test_process_json():
    test_input = json.dumps({
        "test_key": "test_value"
    })

    output = process_json(test_input)

    assert output == {
        "test_key": "test_value"
    }



# Generated at 2022-06-22 12:26:52.232146
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Test for validating prompt_for_config function.

    The test uses a context loaded from cookiecutter.json
    in valid_cookiecutter directory.

    :param no_input: Produce no prompts to the user.
    """


# Generated at 2022-06-22 12:27:01.918014
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:27:06.205629
# Unit test for function read_user_dict
def test_read_user_dict():
    user_input = '[{"name": "John Doe", "hobbies": ["painting", "soccer"]}]'
    assert read_user_dict('test', default_value=user_input) == [{
        "name": "John Doe",
        "hobbies": ["painting", "soccer"],
    }]

# Generated at 2022-06-22 12:27:17.880144
# Unit test for function render_variable
def test_render_variable():
    context = {"cookiecutter": {"name": "{{ cookiecutter.name }}"}, 'name': 'name'}
    env = StrictEnvironment(context=context)

    # should return the same dict
    res = render_variable(env, {"hey": "{{ cookiecutter.name }}"}, context)
    assert res == {"hey": "{{ cookiecutter.name }}"}
    # should return the same list
    res = render_variable(env, ["hey", "{{ cookiecutter.name }}"], context)
    assert res == ["hey", "{{ cookiecutter.name }}"]
    # should return the same str
    res = render_variable(env, "hey {{ cookiecutter.name }}", context)
    assert res == "hey {{ cookiecutter.name }}"
    # should render the str

# Generated at 2022-06-22 12:27:20.618674
# Unit test for function read_user_dict
def test_read_user_dict():
    var_name = 'foo_bar_dict'
    default_value = {"foo": "foo"}

    assert read_user_dict(var_name, default_value) == default_value

# Generated at 2022-06-22 12:27:26.887022
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {
        "cookiecutter": {
            "project_name": "Cookiecutter",
            "project_slug": "cookiecutter",
            "release_date": "2014/04/14"
        }
    }
    no_input = False
    cookiecutter_dict = prompt_for_config(context, no_input=no_input)
    assert len(cookiecutter_dict) == 3


# Generated at 2022-06-22 12:27:33.347544
# Unit test for function render_variable
def test_render_variable():
    import json
    import re


# Generated at 2022-06-22 12:27:46.564030
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Test the prompt_for_config function."""
    context = {
        'cookiecutter': {
            'full_name': 'First Last',
            'email': 'first.last@example.com',
            'github_username': 'flast',
        }
    }

    cookiecutter_dict = prompt_for_config(context, no_input=True)

    assert cookiecutter_dict == {
        'full_name': 'First Last',
        'email': 'first.last@example.com',
        'github_username': 'flast'}

# Generated at 2022-06-22 12:27:53.365527
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {
        'cookiecutter': {
            'project_name': 'Cookie Monster',
            'null_value': None,
            'raw_context_value': '{{project_name}}',
            'dict_value': {
                'foo': 'bar',
                'baz': 'qux',
                'a': '{{project_name}}'
            },
            'list_dict_value': [
                {
                    'foo': 'bar',
                    'baz': 'qux'
                },
                {
                    'foo': 'baz',
                    'bar': 'foo'
                }
            ]
        }
    }


# Generated at 2022-06-22 12:28:02.955328
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:28:14.864621
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Test function prompt_for_config."""
    from cookiecutter.main import cookiecutter

    context = cookiecutter(
        'tests/fake-repo-pre/', no_input=True, output_dir='tests/fake-repo-pre'
    )
    # print(context['cookiecutter']['repo_name'])
    # print(context['cookiecutter']['repo_name'])
    # print(context['cookiecutter']['repo_name'])
    # print(context['cookiecutter']['repo_name'])
    assert context['cookiecutter']['full_name'] == 'Audrey Roy Greenfeld'
    # The default name here is the one from the fake-repo-pre/cookiecutter.json file.

# Generated at 2022-06-22 12:28:26.206032
# Unit test for function read_user_dict
def test_read_user_dict():
    from jinja2 import Template
    from jinja2.environment import Environment
    import os
    import sys


    #Build template environment
    #-----------------------------------------------------------------
    # Jinja environment is used to render the cookiecutter.json and
    # prompt user input for the values of variables.
    env = Environment(
        undefined=StrictUndefined, trim_blocks=True, lstrip_blocks=True
    )
    #-----------------------------------------------------------------

    # all provided variable name, variable value, variable description

# Generated at 2022-06-22 12:28:29.538415
# Unit test for function read_user_dict
def test_read_user_dict():
    """Test function"""
    var_name = 'var_name'
    default_value = {'a': 1, 'b': 2}
    print(read_user_dict(var_name, default_value))


# Generated at 2022-06-22 12:28:36.241002
# Unit test for function prompt_for_config
def test_prompt_for_config():
    # TODO: move to unit tests
    prompt_for_config(
        {
            'cookiecutter': {
                'full_name': "Your Name",
                'project_name': '{{ cookiecutter.full_name }} {{ cookiecutter.repo_name }}',
                'repo_name': 'My',
            }
        },
        no_input=True,
    )

# Generated at 2022-06-22 12:28:44.548658
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """
    test presence of various type of variables
    """
    context = {
        "cookiecutter": {
            "project_name": "Peanut Butter Cookie",
            "version": "{{ cookiecutter.project_name.split()[-1].lower() }}",
            "_copy_without_render": {"ignore/this/dir/file.txt": "file.txt"},
            "__copy_without_render": {"foo.txt": "ignore/this/dir/file.txt"},
            "select_from_a_set": [
                "one",
                "two",
                "three",
                "four",
                "five",
                "six",
            ],
        }
    }
    cookiecutter_dict = prompt_for_config(context, no_input=True)
    assert "project_name" in cookie

# Generated at 2022-06-22 12:28:55.367827
# Unit test for function read_user_dict
def test_read_user_dict():
    # test case 1
    # input: a normal dict
    input_dict = {'key1': 'value1', 'key2': ['value2']}
    # output: the original dict
    output_dict = {'key1': 'value1', 'key2': ['value2']}
    assert (read_user_dict('var_name', input_dict) == output_dict), "test case 1 failed"

    # test case 2
    # input: a normal dict
    input_dict = {'key1': 'value1', 'key2': ['value2']}
    # output: the original dict
    output_dict = {'key1': 'value1', 'key2': ['value2']}
    assert (read_user_dict('var_name', input_dict) == output_dict), "test case 2 failed"

   

# Generated at 2022-06-22 12:29:07.395609
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = json.loads(
        """
        {
            "cookiecutter": {
                "full_name": "Firstname Lastname",
                "email": "me@example.com",
                "project_name": "Awesome Project",
                "project_slug": "awesome_project",
                "year": "2016",

                "repo_name": "{{ cookiecutter.project_slug }}",
                "project_short_description": "The best project ever.",

                "version": "0.1.0",
                "release": "0.1.0",

                "use_pycharm": false,
                "open_source_license": "MIT",

                "_copy_without_render": {
                    "my_private_key": "secret"
                }
            }
        }
        """
    )


# Generated at 2022-06-22 12:29:26.656225
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Unit test for function prompt_for_config."""
    from copy import deepcopy
    from cookiecutter.environment import StrictEnvironment
    from cookiecutter.generate import generate_context
    from cookiecutter.repository import determine_repo_dir


# Generated at 2022-06-22 12:29:38.663961
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {
        'cookiecutter': {
            'full_name': 'Wesley Chun',
            'email': 'wesc@cyberweb.consulting',
            'github_username': 'wesc',
            'project_name': 'Foo Bar',
            'repo_name': '{{ cookiecutter.project_name.replace(" ", "_") }}',
            'description': 'This is an awesome project!',
            'bug_tracker': 'https://github.com/wesc/foo-bar/issues',
            'version': '0.1.0',
            'license': 'MIT',
            'year': '2015',
            '_template': 'https://github.com/wesc/cookiecutter-pycon-talk',
            '_copy_without_render': ['extra/*']
        }
    }

# Generated at 2022-06-22 12:29:43.445380
# Unit test for function read_user_dict
def test_read_user_dict():
    env = StrictEnvironment(context={})
    assert read_user_dict(
        var_name='Muffin',
        default_value={'name': 'Chocolate Muffin', 'tastiness': 6},
    ) == {'name': 'Chocolate Muffin', 'tastiness': 6}

# Generated at 2022-06-22 12:29:54.651967
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:29:58.215257
# Unit test for function read_user_dict
def test_read_user_dict():
    user_value = '{"key1": "value1", "key2": "value2"}'
    user_dict = read_user_dict("variable name", user_value)
    assert user_dict == {'key1': 'value1', 'key2': 'value2'}

    # TODO: test different input from user (etc. incorrect json)

# Generated at 2022-06-22 12:30:03.721327
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:30:06.934093
# Unit test for function prompt_for_config
def test_prompt_for_config():
    # TODO: Test this properly
    assert prompt_for_config({'cookiecutter': {'_template': 'cookiecutter-pypackage'}}, no_input=False) is not None

# Generated at 2022-06-22 12:30:16.452347
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Test the prompt_for_config function"""

# Generated at 2022-06-22 12:30:21.400404
# Unit test for function read_user_choice
def test_read_user_choice():
    """Sample Test
    """
    import click.testing
    runner = click.testing.CliRunner()
    result = runner.invoke(test_read_user_choice)
    assert result.exit_code == 0
    assert result.output == 'Hello, World!\n'


# Generated at 2022-06-22 12:30:22.097910
# Unit test for function prompt_for_config
def test_prompt_for_config():
    pass

# Generated at 2022-06-22 12:30:39.067482
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {'cookiecutter': {'name': 'Foobar'}, 'default_context': {}}
    result = prompt_for_config(context)
    assert result['name'] == 'Foobar'

# Generated at 2022-06-22 12:30:47.674456
# Unit test for function prompt_for_config
def test_prompt_for_config():
    import os
    import shutil
    import tempfile

    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()

    # Create the project
    os.system('cookiecutter gh:mbdevpl/cookiecutter-django')

    # Copy the project to the temporary directory
    shutil.move(
        os.path.join(temp_dir, 'cookiecutter-django'),
        os.path.join(temp_dir, 'test_project'),
    )

    # Go to the previously created directory
    os.chdir(os.path.join(temp_dir, 'test_project'))

    # Run the command to create a new config file
    os.system('cookiecutter cookiecutter-django.json')

    # Remove the project directory

# Generated at 2022-06-22 12:30:57.661356
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Test prompting for config file."""

# Generated at 2022-06-22 12:31:08.549298
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {
        'cookiecutter': {
            'project_name': 'Cookiecutter Example',
            'project_slug': 'cookiecutter-example',
            'release_date': '{{ cookiecutter.year }}-{{ cookiecutter.month }}-'
            '{{ cookiecutter.day }}',
            'year': '{{ cookiecutter.month }}',
            'month': '08',
            'day': '14',
            'version': '0.1.0',
            'author': 'Your name',
            'email': 'you@example.com',
        }
    }

    cookiecutter_dict = prompt_for_config(context)

# Generated at 2022-06-22 12:31:16.635818
# Unit test for function read_user_dict
def test_read_user_dict():
    result = read_user_dict('fake', OrderedDict([('name', 'default')]))
    assert result == OrderedDict([('name', 'default')])
    result = read_user_dict(
        'fake',
        OrderedDict(
            [
                ('window', OrderedDict([('title', 'Hello World')])),
                ('image', OrderedDict([('src', 'something')])),
            ]
        ),
    )
    assert result == OrderedDict(
        [
            ('window', OrderedDict([('title', 'Hello World')])),
            ('image', OrderedDict([('src', 'something')])),
        ]
    )

# Generated at 2022-06-22 12:31:22.278805
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {'cookiecutter': {
        'project_name': 'Jinja2 {{ cookiecutter.test }}',
        'test': 'Best test ever'
    }}
    result = prompt_for_config(context=context, no_input=True)
    assert result == {'project_name': 'Jinja2 Best test ever', 'test': 'Best test ever'}

# Generated at 2022-06-22 12:31:33.402425
# Unit test for function render_variable
def test_render_variable():
    env = StrictEnvironment()
    env_context = { "a": "{{ cookiecutter.b }}" }
    json_context = { "cookiecutter": env_context }

    cookiecutter_dict = { "a": "Hello", "b": "world!" }

    # Test1; raw = None
    assert render_variable(env, None, cookiecutter_dict) == None

    # Test2: raw = {"a": "hello", "b": "world!"}
    assert render_variable(env, cookiecutter_dict, cookiecutter_dict) == cookiecutter_dict

    # Test3: raw = "{{ cookiecutter.b }}"
    assert render_variable(env, "{{ cookiecutter.b }}", cookiecutter_dict) == "world!"

    # Test4: env_context = {"a":

# Generated at 2022-06-22 12:31:43.693504
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Test function prompt_for_config"""
    context = {'cookiecutter': {'model_name': 'toy_example',
                                '_copy_without_render': ['LICENSE.rst', '.coveragerc'],
                                '__repo_name': '{{ cookiecutter.model_name }}',
                                '__repo_description': 'Machine learning model boilerplate '
                                'for "{{ cookiecutter.model_name }}" model.'}}
    cookiecutter_dict = prompt_for_config(context, no_input=True)
    del cookiecutter_dict['_copy_without_render']

# Generated at 2022-06-22 12:31:50.432538
# Unit test for function prompt_for_config
def test_prompt_for_config():
    from cookiecutter.main import cookiecutter

    context = cookiecutter('tests/test-generate-unicode/', no_input=True)
    context.update(prompt_for_config(context, no_input=True))

    print('\nCOMBINED CONTEXT')
    print(120 * '=')
    print(json.dumps(context, indent=2))

    return context

# Generated at 2022-06-22 12:31:56.711986
# Unit test for function render_variable
def test_render_variable():
    """Verify functions for prompting for config info."""
    from cookiecutter.main import cookiecutter

    context = cookiecutter(
        'https://github.com/willingc/cookiecutter-prompt-demo-repo',
        no_input=True,
        extra_context={
            'project_name': 'Static Example',
            'repo_name': 'Do Not Render Me',
        },
    )
    print(context)


# Generated at 2022-06-22 12:32:25.129025
# Unit test for function prompt_for_config
def test_prompt_for_config():
    #debugging
    print("Testing prompt_for_config()")

# Generated at 2022-06-22 12:32:27.467746
# Unit test for function prompt_for_config
def test_prompt_for_config():
    from cookiecutter.main import cookiecutter

    cookiecutter_dict = cookiecutter(
        "file:///{{cookiecutter.project_slug}}",
        no_input=True,
        extra_context={
            'project_slug': "jp_project"
        }
    )

    print(cookiecutter_dict)

# Generated at 2022-06-22 12:32:35.526376
# Unit test for function process_json
def test_process_json():
    # invalid json
    with click.Context(
        click.Command('', callback=read_user_dict, params=[click.Argument(['var_name'])])
    ) as ctx:
        with pytest.raises(click.UsageError):
            process_json('{"test1": "test1"}')

    # json that is a list
    with click.Context(
        click.Command('', callback=read_user_dict, params=[click.Argument(['var_name'])])
    ) as ctx:
        with pytest.raises(click.UsageError):
            process_json('["test1", "test2"]')

    # valid json

# Generated at 2022-06-22 12:32:46.039004
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:32:52.543579
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """ test function prompt_for_config """
    context = {}
    context['cookiecutter'] = OrderedDict([
        ('_template_dir', '.'),
        ('project_name', 'My Project'),
        ('project_slug', 'my_project'),
        ('author_name', 'Your Name'),
        ('email', 'your@email.com'),
        ('description', 'A short description of the project.')
    ])
    res = prompt_for_config(context)
    assert res['project_name'] == 'My Project'

# Generated at 2022-06-22 12:32:58.332279
# Unit test for function read_user_dict
def test_read_user_dict():
    """
    Test to ensure a dict is returned when a dict format is given.
    """
    user_input = '{"key": "value"}'
    key_name = 'test_key'
    expected = OrderedDict([('key', 'value')])
    result = process_json(user_input)
    assert result == expected

# Generated at 2022-06-22 12:33:06.244322
# Unit test for function prompt_for_config
def test_prompt_for_config():
    from cookiecutter.generate import generate_context
    from cookiecutter.main import cookiecutter
    from cookiecutter.utils import rmtree

    context = generate_context(
        repo_dir='tests/fake-repo-pre/',
        context_file='cookiecutter.json',
        default_context=True,
    )
    new_context = dict(prompt_for_config(context, no_input=False))
    assert new_context['project_name'] == context['cookiecutter']['project_name']
    assert new_context['other_choice_variable'] == 'Made a choice'

    result_folder = 'fake-project-pre'
    result_file = 'README.rst'

# Generated at 2022-06-22 12:33:10.393239
# Unit test for function process_json
def test_process_json():
    user_value = '{"test":"test"}'
    assert process_json(user_value) == {"test":"test"}
    user_value = '{"test":'
    assert process_json(user_value) == '{"test":'

# Generated at 2022-06-22 12:33:22.034902
# Unit test for function prompt_for_config
def test_prompt_for_config():
    # test for complex config
    context = {
        'cookiecutter': {
            'project_name': {
                'val': '{{cookiecutter.project_name}}',
                'repo_name': {
                    'val': '{{cookiecutter.repo_name}}',
                    'repo_name': '{{cookiecutter.project_name|lower}}',
                },
            }
        }
    }
    no_input = False
    result = prompt_for_config(context, no_input)

# Generated at 2022-06-22 12:33:28.325030
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Ensure that prompt_for_config() raises an exception if given bad input."""
    wrong_inputs = [{}, [], None, '']
    for wrong_input in wrong_inputs:
        try:
            prompt_for_config(wrong_input)
        except TypeError:
            pass
        else:
            assert False

# Generated at 2022-06-22 12:34:10.857304
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Test the prompt_for_config function."""
    context = {
        'cookiecutter': {
            'project_name': 'Cookiecutter-Test',
            'project_slug': 'cookiecutter-test',
            'repo_name': 'cookiecutter-test',
            'author_name': 'Raphaël Barrois',
            'author_email': 'raphael.barrois+cookiecutter@polytechnique.org',
            'description': 'A short description of the project',
        },
    }

    cookiecutter_dict = prompt_for_config(context, no_input=True)

    assert cookiecutter_dict == context['cookiecutter']

# Unit tests for function render_variable

# Generated at 2022-06-22 12:34:17.180177
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Test for function prompt_for_config(context, no_input=False)."""
    from .main import find_template
    from .config import get_user_config, get_config_from_file
    from .generate import generate_context

    # get the default user config
    user_config = get_user_config(get_config_from_file())

    # get the template
    template_dir = find_template(None, user_config)

    # get the config populated with defaults
    config_dict = json.loads(template_dir.read_text("config.json"))
    context = generate_context(
        template_dir, None, config_dict, user_config['context_file']
    )

    # test with no_input = True

# Generated at 2022-06-22 12:34:29.600283
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """
    Test the prompt for config, with and without input
    """