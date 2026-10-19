

# Generated at 2022-06-22 12:24:48.151136
# Unit test for function read_user_dict
def test_read_user_dict():
    # If the user types 'default' the dict will return the default_value provided
    default_value = {'a': 'b', 'c': 'd'}
    assert read_user_dict('', default_value) == default_value
    # Invalid JSON will raise an UsageError exception
    with pytest.raises(click.UsageError):
        read_user_dict('', '{"a": "a"')
    # JSON that is not a dict will raise an UsageError exception
    with pytest.raises(click.UsageError):
        read_user_dict('', '"a"')
    # Empty JSON is not accepted
    with pytest.raises(click.UsageError):
        read_user_dict('', '{}')
    # If the user types 'default' the dict will return the default_value provided
    output_

# Generated at 2022-06-22 12:24:53.514609
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Task: Test function prompt_for_config"""
    # Tests
    context = {'cookiecutter': {'project_name': 'Awesome Project', '_template': {}}}
    ret = prompt_for_config(context)
    assert ret == {'project_name': 'Awesome Project', '_template': {}}

if __name__ == '__main__':
    # test_prompt_for_config()
    pass

# Generated at 2022-06-22 12:25:04.396795
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Unit test for prompt_for_config."""
    context = {
        'cookiecutter': {
            'project_name': {
                '__prompt_message': 'User prompt message',
                'default': 'Default Project Name',
            },
            'project_slug': '{{cookiecutter.project_name|lower|replace(" ","_")}}',
            'project_url': {
                '__prompt_message': 'User prompt message',
                'default': 'https://github.com/{}'.format('{{cookiecutter.project_slug}}'),
            },
        }
    }
    cookiecutter_dict = prompt_for_config(context)
    assert cookiecutter_dict['project_name'] == "Default Project Name"


if __name__ == '__main__':
    test_prom

# Generated at 2022-06-22 12:25:14.319850
# Unit test for function read_user_dict
def test_read_user_dict():
    # Example of successful user input
    assert read_user_dict("User input", {"default_key": "default_value"}) == {"default_key": "default_value"}
    assert read_user_dict("User input", {"key1":"value1"}) == {"key1":"value1"}
    # User provided input successfully decoded
    assert read_user_dict("User input", {"default_key": "default_value"}) == {
        "user_key": "user_value"
    }
    # Spaces are allowed
    assert read_user_dict("User input", {"default_key": "default_value"}) == {
        "user key": "user value"
    }
    # Equal signs are allowed

# Generated at 2022-06-22 12:25:24.065371
# Unit test for function prompt_for_config
def test_prompt_for_config():
    config = {
        "cookiecutter": {
            "name": "Project",
            "description": "Blah, blah, blah",
            "list": [
                "1",
                {"item": "2"},
                "item",
                ["one", "two", "three"]
            ]
        }
    }

    result = prompt_for_config(config)

    assert isinstance(result, OrderedDict)
    assert isinstance(result["list"], list)
    assert len(result["list"]) == 4
    assert result["list"][1]["item"] == "2"
    assert result["list"][2] == "item"
    assert len(result["list"][3]) == 3

# Generated at 2022-06-22 12:25:36.463768
# Unit test for function read_user_dict
def test_read_user_dict():
    """Ensure 'read_user_dict' returns a dictionary."""
    # Please see https://click.palletsprojects.com/en/7.x/api/#click.prompt
    from click.testing import CliRunner
    from cookiecutter.config import DEFAULT_CONFIG

    # Test for valid input
    runner = CliRunner()
    result = runner.invoke(
        read_user_dict,
        ['key', DEFAULT_CONFIG['cookiecutter']['default_context']]
    )
    assert isinstance(result.output, str)
    assert isinstance(result.exit_code, int)
    assert result.exit_code == 0
    assert isinstance(result.exc_info, type(None))
    assert isinstance(result.exception, type(None))

# Generated at 2022-06-22 12:25:46.219911
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {
        'cookiecutter': {
            'project_name': 'example',
            'project_slug': '{{ cookiecutter.project_name.replace(" ", "") }}',
            'repo_name': '{{ cookiecutter.project_name.replace(" ", "_") }}',
        }
    }

    # Default values
    cookiecutter_dict = prompt_for_config(context, no_input=True)
    assert 'example' == cookiecutter_dict['project_name']
    assert 'example' == cookiecutter_dict['project_slug']
    assert 'example' == cookiecutter_dict['repo_name']

    # Custom values
    cookiecutter_dict = prompt_for_config(context, no_input=False)

# Generated at 2022-06-22 12:25:48.590570
# Unit test for function read_user_dict
def test_read_user_dict():
    defaults={"dict_key":"default_value"}
    result=read_user_dict("dict_key",defaults)
    assert result == defaults

# Generated at 2022-06-22 12:25:53.603054
# Unit test for function read_user_dict
def test_read_user_dict():
    """Test with valid type"""
    var_name = "dict_var"
    valid_dict = {'key': 'value'}
    # Env is not needed for this test
    env = StrictEnvironment()
    returned_dict = read_user_dict(var_name, valid_dict)
    assert valid_dict == returned_dict


# Generated at 2022-06-22 12:26:02.704211
# Unit test for function render_variable
def test_render_variable():
    """Unit testing of the function render_variable."""
    from .main import get_context

    test_context = get_context('tests/test-render-variable/fake-repo', '.')
    env = StrictEnvironment(context=test_context)
    # Given a test context
    assert test_context == {
        'cookiecutter': {
            'firstvar1': 'firstvalue1',
            'firstvar2': {'subvar2': 'subvalue2'},
            'secondvar1': '{{ cookiecutter.firstvar1 }}-{{ cookiecutter.firstvar2.subvar2 }}',
            'secondvar2': {'subvar2': 'subvalue2'},
        }
    }
    # When we render the variable in the test context

# Generated at 2022-06-22 12:26:20.641869
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Test the functioning of the prompt_for_config function."""
    # create a context
    context = dict(foo='Foo', dict_variable_name='bar', empty_dict='None')

    # create an env
    env = StrictEnvironment(context=context)

    # create a cookiecutter_dict
    cookiecutter_dict = OrderedDict([('foo', 'Foo')])

    # test prompt_for_config function with a dict variable
    assert prompt_for_config(context={'cookiecutter': {'dict_variable_name': {'bar': 'baz'}}}, no_input=False) == {'dict_variable_name': {'bar': 'baz'}}

# Generated at 2022-06-22 12:26:31.687497
# Unit test for function prompt_for_config
def test_prompt_for_config():
    from cookiecutter.main import cookiecutter
    from cookiecutter.utils import work_in
    from tempfile import mkdtemp
    from os import getcwd
    from os.path import join, dirname, abspath
    import shutil
    import sys
    import pytest
    import shlex
    import re

    BASE_TEMPLATE = 'basic'
    CUSTOM_TEMPLATE = abspath(join(dirname(__file__), '..', '..', 'tests/fake-repo-pre/', BASE_TEMPLATE))

    TEMPLATE_DIR = join(getcwd(), 'tests/fake-repo-pre/', BASE_TEMPLATE)

# Generated at 2022-06-22 12:26:41.549181
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:26:43.707942
# Unit test for function read_user_dict
def test_read_user_dict():
    read_user_dict('test_key', {'test': 'test'})
test_read_user_dict()


# Generated at 2022-06-22 12:26:52.686415
# Unit test for function prompt_for_config
def test_prompt_for_config():
    from cookiecutter.main import cookiecutter

    context = cookiecutter('.', no_input=True)
    assert context['cookiecutter']['author_name'] == 'Audrey Roy Greenfeld'
    assert context['cookiecutter']['author_email'] == 'audreyr@example.com'
    assert context['cookiecutter']['package_name'] == 'cookiecutter-pypackage'
    assert context['cookiecutter']['repo_name'] == 'cookiecutter-pypackage'
    assert context['cookiecutter']['project_short_description'] == 'A Python package project template.'
    assert context['cookiecutter']['release_date'] == '2014-04-01'
    assert context['cookiecutter']['version'] == '0.1.0'
   

# Generated at 2022-06-22 12:26:53.341484
# Unit test for function prompt_for_config
def test_prompt_for_config():
    # TODO: Create test
    assert False

# Generated at 2022-06-22 12:27:01.973896
# Unit test for function read_user_dict
def test_read_user_dict():
    var_name = "var_name"
    default_value = {'a': 'b'}
    user_value = [{"a": "b"}]
    user_values = [["a", "b"]]
    user_value1 = 'a'

    assert isinstance(read_user_dict(var_name, default_value), dict)
    assert read_user_dict(var_name, default_value) == user_value[0]
    assert read_user_dict(var_name, default_value) != user_values[0]
    assert read_user_dict(var_name, default_value) != user_value1


# Generated at 2022-06-22 12:27:10.342551
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {
        "cookiecutter": {
            "full_name": "Author",
            "email": "author@example.com",
            "repo_name": "Repo Name",
            "project_name": "{{ cookiecutter.repo_name | replace(\" \", \"_\") }}",
            "repo_description": "No project description.",
            "release_date": "2019-01-01",
        }
    }

    no_input = True

    cookiecutter_dict = prompt_for_config(context, no_input)
    assert cookiecutter_dict['project_name'] == "Repo_Name"

# Generated at 2022-06-22 12:27:19.455031
# Unit test for function prompt_for_config
def test_prompt_for_config():
    from jinja2 import StrictUndefined
    from cookiecutter import utils
    from .main import DEFAULT_CONFIG

    no_input = True
    context = utils.make_context(DEFAULT_CONFIG)
    env = StrictEnvironment(undefined=StrictUndefined)

    cookiecutter_dict = prompt_for_config(context, no_input)

    rendered_template = render_variable(env, context['cookiecutter']['repo_name'], cookiecutter_dict)
    print(rendered_template)


if __name__ == '__main__':
    test_prompt_for_config()

# Generated at 2022-06-22 12:27:29.829651
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:27:50.697753
# Unit test for function prompt_for_config
def test_prompt_for_config():
    # Default values
    context = {
        'cookiecutter': {
            'project_name': "Jane's Bakery",
            'project_slug': "{{ cookiecutter.project_name.lower().replace(' ', '_') }}",
            'release_date': "2013-01-01",
            'pypi_username': 'janedoe',
            'github_username': 'janedoe',
            'version': '0.1.0',
            'open_source_license': 'MIT',
        }
    }
    # Copy default values
    cookiecutter_dict = context.copy()
    # Create env object from context
    env = StrictEnvironment(context=context)
    # Create dictionary from prompt_for_config without user interaction

# Generated at 2022-06-22 12:28:00.734902
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:28:10.843519
# Unit test for function process_json
def test_process_json():
    inputs = [
        {"a": "b"},
        "{\"a\": \"b\"}",
        '{"a": "b"}',
        '{a: b}',
        'a',
        '"a"',
    ]
    outputs = [
        {"a": "b"},
        {"a": "b"},
        {"a": "b"},
        {"a": "b"},
        "a",
        "a",
    ]

    error_message = "process_json(value) == {!r}"
    for input, output in zip(inputs, outputs):
        assert process_json(input) == output, error_message.format(output)

# Generated at 2022-06-22 12:28:22.440418
# Unit test for function prompt_for_config
def test_prompt_for_config():

    # Test 1: Test it is possible to enter default values for the config
    context = {
        'cookiecutter': {
            'project_name': 'Awesome Project',
            'project_slug': 'awesome_project',
            'author_name': 'Your Name',
        }
    }
    config = prompt_for_config(context)
    assert 'project_name' in config
    assert 'project_slug' in config
    assert 'author_name' in config
    assert config['project_name'] == 'Awesome Project'
    assert config['project_slug'] == 'awesome_project'
    assert config['author_name'] == 'Your Name'

    # Test 2: Test it is possible to enter custom values for the config
    config = prompt_for_config(context)
    assert 'project_name' in config


# Generated at 2022-06-22 12:28:31.076075
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {
        'cookiecutter': {
            'author_name': 'Audrey Roy Greenfeld',
            'email': 'audreyr@example.com',
            'project_name': '{{ cookiecutter.author_name }} project'
        }
    }
    cookiecutter_dict = prompt_for_config(context, no_input=True)
    assert 'Audrey Roy Greenfeld project' == cookiecutter_dict['project_name']
    assert 'Audrey Roy Greenfeld' == cookiecutter_dict['author_name']

    context = {
        'cookiecutter': {
            'author_name': 'Audrey Roy Greenfeld',
            'email': 'audreyr@example.com',
            'project_name': '{{ cookiecutter.author_name }} project'
        }
    }
    cookie

# Generated at 2022-06-22 12:28:34.529171
# Unit test for function process_json
def test_process_json():
    """Test process_json function"""
    assert process_json('{"b": "2", "a": "1"}') == {"a": "1", "b": "2"}

# Generated at 2022-06-22 12:28:45.097041
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {
        'cookiecutter': {
            'name': 'Audrey Roy',
            'email': 'audreyr@cartwheel.com',
            'github_username': 'audreyr',
            'project_name': 'cookiecutter-pypackage',
            'repo_name': '{{ cookiecutter.project_name.replace(" ", "_") }}',
            'pypi_username': '{{ cookiecutter.github_username }}',
            'description': 'A Python package project template.',
            'domain_name': 'cartwheel.com',
            'version': '0.1.0',
            'timezone': 'UTC',
            'use_pycharm': 'n',
            'use_docker': 'y',
            'open_source_license': 'MIT license',
        }
    }

# Generated at 2022-06-22 12:28:45.614993
# Unit test for function prompt_for_config
def test_prompt_for_config():
    # TODO
    pass

# Generated at 2022-06-22 12:28:50.273828
# Unit test for function process_json
def test_process_json():
    # Arrange
    user_value_1 = '{"name": "John", "address": {"number": 3, "street": "High Street"}}'  # noqa
    user_value_2 = '{name: John, address: {number: 3, street: High Street}}'  # noqa
    user_value_3 = '{"name": "John"}'
    user_value_4 = '{name: "John"}'

    # Act
    user_dict_1 = process_json(user_value_1)
    user_dict_2 = process_json(user_value_2)
    user_dict_3 = process_json(user_value_3)
    user_dict_4 = process_json(user_value_4)

    # Assert
    assert isinstance(user_dict_1, dict)


# Generated at 2022-06-22 12:28:56.303206
# Unit test for function read_user_dict
def test_read_user_dict():
    from click.types import STRING

    STRING.convert('', None, None)
    STRING.convert('default', None, None)
    STRING.convert('{}', None, None)
    STRING.convert('{"foo": "bar"}', None, None)
    
    try:
        STRING.convert('3', None, None)
    except:
        assert True

    try:
        STRING.convert('[3, 4, 5]', None, None)
    except:
        assert True

    try:
        STRING.convert('{"foo": }', None, None)
    except:
        assert True

# Generated at 2022-06-22 12:29:17.753524
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """prompt_for_config - Unit test"""

    # Given a context

# Generated at 2022-06-22 12:29:29.500933
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Ensure prompt_for_config works even with non-string vars"""

    from pathlib import Path

    template_path = '__cookiecuttertest.test_prompt_for_config'
    raw_template = """
cookiecutter.repo_name = '{{ cookiecutter.project_name.replace(" ", "_") }}'
cookiecutter.user_dict = {{ cookiecutter.repo_name }}
cookiecutter.user_choice = '{{ cookiecutter.repo_name }}'
"""
    test_path = Path(template_path)
    test_path.mkdir(parents=True, exist_ok=True)
    test_path /= 'cookiecutter.json'
    test_path.write_text(raw_template)


# Generated at 2022-06-22 12:29:37.519406
# Unit test for function prompt_for_config
def test_prompt_for_config():

    from cookiecutter.main import cookiecutter

    context = cookiecutter('.')

    assert isinstance(context, dict)
    assert 'cookiecutter' in context
    assert isinstance(context['cookiecutter'], dict)

    cookiecutter_dict = prompt_for_config(context, no_input=True)

    assert isinstance(cookiecutter_dict, dict)

    assert 'project_name' in cookiecutter_dict
    assert cookiecutter_dict['project_name'] == 'Cookiecutter Test Project'

# Generated at 2022-06-22 12:29:45.836809
# Unit test for function read_user_dict
def test_read_user_dict():
    """
    >>> read_user_dict('test1', 'default1')
    Traceback (most recent call last):
    ...
    TypeError: ...
    >>> read_user_dict('test2', {})
    Traceback (recent call last):
    ...
    UsageError: ...
    >>> read_user_dict('test3', {'a': 'b'})
    Traceback (recent call last):
    ...
    UsageError: ...
    >>> read_user_dict('test4', {'a': True})
    {'a': True}
"""

# Generated at 2022-06-22 12:29:54.689718
# Unit test for function read_user_dict
def test_read_user_dict():
    # Parse
    var_name = 'HOST'
    default_value = {'host': '1.1.1.1', 'port': 8090}
    user_value_dict = read_user_dict(var_name, default_value)
    assert user_value_dict == default_value

    # Parse with input
    var_name = 'HOST'
    default_value = {'host': '2.2.2.2', 'port': 8090}
    input = '{"host": "3.3.3.3", "port": 8090}'
    user_value_dict = read_user_dict(var_name, default_value)
    assert user_value_dict == {'host': '3.3.3.3', 'port': 8090}

    # Parse with empty input
   

# Generated at 2022-06-22 12:29:57.545533
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {"cookiecutter": {"project_name": "Foo bar"}}
    result = prompt_for_config(context, no_input=True)
    expected = {"project_name": "Foo bar"}
    assert result == expected

# Generated at 2022-06-22 12:30:03.300215
# Unit test for function process_json
def test_process_json():
    user_value = '{"project_name": "My Project", "repo_name": "my_project"}'
    expected = {'project_name': 'My Project', 'repo_name': 'my_project'}
    result = process_json(user_value)
    assert result == expected

# Generated at 2022-06-22 12:30:14.249034
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {
        "cookiecutter": {
            "project_name": "Cool Project",
            "project_slug": "{{ cookiecutter.project_name|lower|replace(' ', '_') }}",
            "release_date": "2017-07-28",
            "created_date": "{{ cookiecutter.release_date }}",
            "_copy_without_render": ["__file__"],
            "favorite_color": {
                "type": "string",
                "allowed": ["blue", "green", "orange"],
                "default": "orange",
            },
            "__file__": "{{ cookiecutter.project_slug }}/{{ cookiecutter.project_slug }}.py",
        }
    }


# Generated at 2022-06-22 12:30:24.137577
# Unit test for function process_json
def test_process_json():
    env = StrictEnvironment(context={})
    assert read_user_variable("Enter value", "default") == "default"
    assert read_user_yes_no("Enter value", "default") == "default"
    assert read_repo_password("Enter value", "default") == "default"
    test_list = ["123", "456"]
    assert read_user_choice("Enter value", test_list) == "123"
    assert process_json("test") == 'test'
    assert read_user_dict("Enter value", test_list) == test_list
    assert render_variable(env, "test value", {}) == "test value"

# Generated at 2022-06-22 12:30:36.452587
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {
        'cookiecutter': {
            'project_name': 'Project',
            'project_slug': 'project',
            '_template': {
                'foo': 'bar',
                'baz': 'blah'
            },
            'owner': {
                'name': 'Gajus Kuizinas',
                'email': 'gajus@kuizinas.lt',
                '__version__': '0.4.2'
            },
            'year': '2014'
        }
    }
    cookiecutter_dict = prompt_for_config(context, no_input=True)

# Generated at 2022-06-22 12:31:08.047807
# Unit test for function prompt_for_config
def test_prompt_for_config():
    class ConfigClass(object):
        config_var = 'config_var_value'


# Generated at 2022-06-22 12:31:13.933611
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Ensure basic usage of prompt_for_config works."""
    context = {
        'cookiecutter': {
            'project_name': 'My Project',
            'project_slug': 'my_project',
            'pypi_username': 'audreyr',
            'open_source_license': 'MIT license',
            'year': '2014',
            'project_short_description': 'An example package',
        }
    }

    cookiecutter_dict = prompt_for_config(context)

    assert 'project_name' in cookiecutter_dict
    assert 'project_slug' in cookiecutter_dict
    assert 'pypi_username' in cookiecutter_dict
    assert 'open_source_license' in cookiecutter_dict
    assert 'year' in cookiecutter_dict

# Generated at 2022-06-22 12:31:24.911158
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """unit test for prompt_for_config"""
    context = {
        'cookiecutter': {
            'project_name': 'Cookiecutter Test Project',
            'repo_name': 'cookiecutter-test-project',
            'open_source_license': 'MIT license',
            'project_short_description': 'A short description of the project.',
            'pypi_username': 'my_pypi_username',
        },
    }

# Generated at 2022-06-22 12:31:30.844426
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {}
    context['cookiecutter'] = {
        'project_name': '{{ cookiecutter.project_short_description }}',
        'project_short_description': 'My Project',
        'author_name': 'Your name',
        'email': 'Your email',
        'description': 'A short description of the project.',
        'domain_name': 'example.com',
        'version': '0.1.0',
        'license': 'MIT',
        'github_username': 'your-github-username',
        'year': '{{ cookiecutter.current_year }}',
        'current_year': '2019',
    }
    config_dict = prompt_for_config(context, True)
    assert config_dict['project_short_description'] == 'My Project'
    assert config_dict['email']

# Generated at 2022-06-22 12:31:42.515485
# Unit test for function prompt_for_config
def test_prompt_for_config():
    from cookiecutter.main import cookiecutter
    from tempfile import TemporaryDirectory
    from os.path import join

    # Create a cookiecutter template
    with TemporaryDirectory() as temp_dir:
        repo_dir = join(temp_dir, 'hello')
        cookiecutter(
            'tests/test-projects/simple-cookiecutter-cli-hello',
            no_input=True,
            output_dir=temp_dir,
            extra_context={
                'full_name': 'Test McTester',
                'email': 'test@example.com',
            },
        )
        assert join(temp_dir, 'hello') == repo_dir

        # Test the function prompt_for_config
        from cookiecutter.config import get_user_config
        from cookiecutter.environment import StrictEnvironment

# Generated at 2022-06-22 12:31:46.014678
# Unit test for function process_json
def test_process_json():
    assert process_json('{"foo": "foo", "bar": "bar"}') == {'foo': 'foo', 'bar': 'bar'}

# Generated at 2022-06-22 12:31:56.710498
# Unit test for function prompt_for_config
def test_prompt_for_config():
    import os

    units_path = os.path.abspath(os.path.join(
        os.path.dirname(__file__), '../tests/files/files-001/'))

    context = json.load(open(os.path.join(units_path, 'cookiecutter.json')))

    cookiecutter_dict = prompt_for_config(
        context, no_input=True
    )

    assert sorted(cookiecutter_dict.keys()) == sorted([
        '_copy_without_render',
        '__version__',
        'comment',
        'cookiecutter_dict',
        'date',
        'email_address',
        'full_name',
        'project_name',
        'repo_name',
        'version',
    ])


# Generated at 2022-06-22 12:32:00.148052
# Unit test for function prompt_for_config
def test_prompt_for_config():
    prompt_for_config({
        'cookiecutter': {
            'project_name': 'foo',
            '_template': {'description': 'description', 'foo': 'bar'},
            '__locations__': {'foo': 'bar'},
        },
    })

# Generated at 2022-06-22 12:32:02.905504
# Unit test for function read_user_dict
def test_read_user_dict():
    var_name = 'foo'
    default_value = {'bar': 'baz'}
    assert read_user_dict(var_name, default_value) == default_value

# Generated at 2022-06-22 12:32:11.524858
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Unit test for function prompt_for_config."""
    context = {
        'cookiecutter': {
            'customer_name': 'World Domination Inc',
            'domain_name': 'worlddomination.me',
            'project_name': 'Hello World',
            'project_slug': 'hello-world',
            'release_date': '2015-08-22',
            'year': '2015',
            'project_short_description': 'A short description of the project.',
            'pypi_username': 'worlddom',
            'github_username': 'worlddom',
            'email': 'me@worlddomination.me',
            'description': 'A short description of the project.',
            'version': '0.1.0',
        }
    }

    rendered_context = prompt_for_config

# Generated at 2022-06-22 12:32:51.931673
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {}

# Generated at 2022-06-22 12:33:03.593493
# Unit test for function render_variable
def test_render_variable():
    """Test the render_variable function."""

# Generated at 2022-06-22 12:33:15.063606
# Unit test for function prompt_for_config
def test_prompt_for_config():
    from cookiecutter import utils
    from cookiecutter.main import cookiecutter
    from tests.test_prompt_for_config import context
    repo_dir = utils.find_repo(
        'tests/fake-repo-pre/',
        abbreviations={'tests/fake-repo-pre/': '.'},
        default_repo='.',
    )
    context['repo_dir'] = repo_dir
    cookiecutter_dict = prompt_for_config(context, no_input=True)
    result = cookiecutter(
        '.',
        extra_context=cookiecutter_dict,
        no_input=False,
        overwrite_if_exists=True,
    )
    print(result)

# Generated at 2022-06-22 12:33:25.733082
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Ensure that cookiecutter prompts correctly when passed in a mocked context."""
    # Mock up a JSON-equivalent context dict
    context = {}

# Generated at 2022-06-22 12:33:31.598132
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {
        "cookiecutter":{
            "project_name":"Hello World",
            "_copy_without_render":[
                "somefile.txt"
            ]
        }
    }

    cookiecutter_dict = prompt_for_config(context)
    assert(cookiecutter_dict["project_name"] == "Hello World")
    assert("_copy_without_render" in cookiecutter_dict)
    assert(cookiecutter_dict["_copy_without_render"] == ["somefile.txt"])

# Generated at 2022-06-22 12:33:41.901765
# Unit test for function prompt_for_config
def test_prompt_for_config():
    from cookiecutter.environment import setup_default_env
    from cookiecutter import utils

    # nyu_config.json was created as a copy of cookiecutter.json for use in
    # this unit test.
    # It is located in the root dir.
    # Load context from json file
    context = utils.get_project_renderer(
        extra_context=None,
        default_context={},
        config_file='tests/nyu_config.json',
        search_dir='.'
    ).context

    # Set up testing environment
    env = setup_default_env(context, {'cookiecutter': {'project_name': 'test'}})

    # Run function
    cookiecutter_dict = prompt_for_config(context, no_input=True)

    # Expected output
    expected_

# Generated at 2022-06-22 12:33:46.470700
# Unit test for function read_user_choice
def test_read_user_choice():
    options = ["my_awesome_repo"]
    var_name = "project_slug"
    result = read_user_choice(var_name, options)
    assert result == "my_awesome_repo"

if __name__ == "__main__":
    test_read_user_choice()

# Generated at 2022-06-22 12:33:49.150066
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {'cookiecutter': {'full_name': 'Your Name', 'email': 'Your email'}}
    assert prompt_for_config(context) == {'full_name': 'Your Name', 'email': 'Your email'}

# Generated at 2022-06-22 12:33:56.969531
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {
      'cookiecutter': {
        'project_name': "Cookie",
        '_test': {'test': "test"},
        'test': {"cookie": "{{ cookiecutter.project_name }}"},
        'test_dict': {'test': "test"},
        '__test': "{{ cookiecutter.test.cookie }}"
      }
    }

    cookiecutter_dict = prompt_for_config(context, True)
    assert cookiecutter_dict['project_name'] == "Cookie"
    assert cookiecutter_dict['test']['cookie'] == "Cookie"
    assert cookiecutter_dict['__test'] == "Cookie"



# Generated at 2022-06-22 12:33:59.744129
# Unit test for function read_user_dict
def test_read_user_dict():
    var_name = "crush_name"
    default_value = [{'first': 'John'}, {'last': 'Doe'}]

    assert read_user_dict(var_name, default_value) == default_value