

# Generated at 2022-06-22 12:24:41.771892
# Unit test for function process_json
def test_process_json():
    """Test json processing for read_user_dict function."""
    #Test for success
    with_quotes = '{"a": "b"}'
    with_quotes_result = {'a': 'b'}

    without_quotes = '{"a": b}'
    without_quotes_result = {'a': 'b'}

    assert process_json(with_quotes) == with_quotes_result
    assert process_json(without_quotes) == without_quotes_result

    #Test for failure
    float_value = '{"a": 1.0}'
    boolean_value = '{"a": True}'
    list_value = '{"a": [1, 2, 3]}'

    with raises(click.UsageError):
        process_json(float_value)


# Generated at 2022-06-22 12:24:52.176547
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:24:54.898436
# Unit test for function prompt_for_config
def test_prompt_for_config():
    cookiecutter_dict = prompt_for_config({'cookiecutter': {'project_name': 'test'}})
    assert cookiecutter_dict['project_name'] == 'test'

# Generated at 2022-06-22 12:25:04.504007
# Unit test for function process_json
def test_process_json():
    # testing valid json
    valid_json_str = '{"sample": "valid json"}'
    try:
        valid_json = process_json(valid_json_str)
        assert valid_json == {"sample": "valid json"}
    except click.UsageError:
        assert False

    # testing invalid json
    invalid_json_str = '{"sample": "invalid json'
    try:
        process_json(invalid_json_str)
        assert False
    except click.UsageError:
        assert True

    # testing json dict
    invalid_json_dict = '["invalid json dict"]'
    try:
        process_json(invalid_json_dict)
        assert False
    except click.UsageError:
        assert True

# Generated at 2022-06-22 12:25:14.378123
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Unit test for function prompt_for_config."""
    import pytest

    context = {
        'cookiecutter': {
            'project_name': 'Awesome Project',
            '_copy_without_render': {
                'foo': 'bar'
            },
            '__copy_with_render': {
                '{{ cookiecutter.project_name }}': 'bar'
            }
        }
    }

    try:
        cookiecutter_dict = prompt_for_config(context, no_input=False)
    except Exception as err:
        pytest.fail("Reading user input failed: " + str(err))
    else:
        assert cookiecutter_dict['project_name'] == 'Awesome Project'
        assert cookiecutter_dict['_copy_without_render']['foo'] == 'bar'
       

# Generated at 2022-06-22 12:25:18.491819
# Unit test for function prompt_for_config
def test_prompt_for_config():
    d = prompt_for_config({'cookiecutter': {'a': 'hello', 'b': 'world', 'c': '{{a}} {{b}}'}})
    assert d == {'a': 'hello', 'b': 'world', 'c': 'hello world'}

# Generated at 2022-06-22 12:25:26.200859
# Unit test for function prompt_for_config
def test_prompt_for_config():
    #Dummy context variable.
    context = {
        'cookiecutter':
            {'full_name': 'Donald Duck', 'Project name': 'Test',
             'project_short_description': 'This is a test project',
             'open_source_license': 'MIT'}
    }
    #Dummy value to return
    return_value = 'Test'

    #Simple test to check if we get the right return value.
    assert prompt_for_config(context, no_input=True) == return_value

# Generated at 2022-06-22 12:25:38.023207
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Verify that the 'validate_cookiecutter_dict' function is working
    properly and returns a cookiecutter dict.
    """
    context = {
        "cookiecutter": {
            "project_name": "My Project",
            "project_slug": "my_project",
            "author_name": "Your Name",
            "domain_name": "example.com",
            "email": "me@example.com",
            "description": "A short description of the project.",
            "version": "0.1.0",
            "timezone": "Europe/Paris",
            "use_pycharm": 1,
            "use_docker": 1,
            "select_linter": ["pylint", "flake8", "pep8"],
        }
    }


# Generated at 2022-06-22 12:25:47.732125
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Testing prompt_for_config
    """

# Generated at 2022-06-22 12:25:58.485354
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """
    Unit test for function "prompt_for_config"
    """

    # Test 1: Verify that repeated template variables work
    # Define context for testing
    context_test_repeated_variable = {
        'cookiecutter': {
            'project_name': '{{ cookiecutter.project_name }}',
            'project_slug': '{{ cookiecutter.project_name.replace(" ", "-") }}',
            'author_name': 'Jon Snow',
            'repo_name': '{{ cookiecutter.project_slug }}'
        }
    }
    # Define expected o/p for testing

# Generated at 2022-06-22 12:26:12.876766
# Unit test for function read_user_dict
def test_read_user_dict():
    """Unit test for read_user_dict()"""
    # Positive test case with positive data
    variable_name = 'company'
    default_value = {
        'name': 'Linux',
        'place': 'Bangalore'
    }
    user_input = '{"name":"Linux", "place": "Bangalore"}'
    result = read_user_dict(variable_name, default_value)
    assert result == default_value
    # Positive test case with negative data
    variable_name = 'company'
    default_value = {
        'name': 'Linux',
        'place': 'Bangalore'
    }
    user_input = '{"name":"Linux", "place": "Bangalore"}'
    result = read_user_dict(variable_name, default_value)

# Generated at 2022-06-22 12:26:20.453486
# Unit test for function read_user_dict
def test_read_user_dict():
    dic = {'a': 1, 'b': 2}
    assert read_user_dict("a", dic) == {'a': 1, 'b': 2}
    assert read_user_dict("a", {}) == {}
    # Test error handling
    try:
        read_user_dict("a", [])
    except TypeError:
        pass
    else:
        raise Exception("Should have raised TypeError")
    try:
        read_user_dict("a", "")
    except TypeError:
        pass
    else:
        raise Exception("Should have raised TypeError")

# Generated at 2022-06-22 12:26:31.513209
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Check whether the prompt_for_config function works properly
    """
    assert prompt_for_config({'cookiecutter': {'first_name': 'Pascal', 'last_name': 'Precht', 'country': 'Germany', 'first_choice': 'Choice 1', 'second_choice': 'Choice 2', '_secret_key': 'secret', '__default_key': 'default', 'dict': {'key': 'value'}}}) == {'first_name': 'Pascal', 'last_name': 'Precht', 'country': 'Germany', 'first_choice': 'Choice 1', 'second_choice': 'Choice 2', '_secret_key': 'secret', '__default_key': 'default', 'dict': {'key': 'value'}}

# Generated at 2022-06-22 12:26:34.977798
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {"cookiecutter": {"test_variable": "test"}}
    val = prompt_for_config(context, no_input=True)
    assert val == {"test_variable": "test"}

# Generated at 2022-06-22 12:26:44.166388
# Unit test for function prompt_for_config
def test_prompt_for_config():
    import os
    import shutil
    import tempfile
    from click.testing import CliRunner

    from cookiecutter.cli import main

    cli_runner = CliRunner()
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create test template in temporary directory
        template_dir = os.path.join(temp_dir, 'simple_template')
        os.mkdir(template_dir)
        with open(os.path.join(template_dir, 'README.md'), 'w') as f:
            f.write('# README\n')

# Generated at 2022-06-22 12:26:51.793260
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {
        'cookiecutter': {
            'project_name': 'My Project',
            '_template': {
                '__file__': 'README.rst',
                '__content__': '{{ cookiecutter.project_name }}',
            },
        }
    }
    cookiecutter_dict = prompt_for_config(context, True)
    assert cookiecutter_dict['project_name'] == 'My Project'
    assert cookiecutter_dict['_template']['__file__'] == 'README.rst'
    assert cookiecutter_dict['_template']['__content__'] == 'My Project'

# Generated at 2022-06-22 12:26:58.840977
# Unit test for function read_user_dict
def test_read_user_dict():
    # Unit test for function read_user_dict
    test_dict = OrderedDict([('First_key', 'First_value'), ('Second_key', 'Second_value')])
    user_dict = read_user_dict('Test_dict_variable', default_value=test_dict)
    assert user_dict == test_dict

    test_dict['New_key'] = 'New_value'
    user_dict = read_user_dict('Test_dict_variable', default_value=test_dict)
    assert user_dict == test_dict

# Generated at 2022-06-22 12:27:08.363853
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:27:19.559084
# Unit test for function prompt_for_config
def test_prompt_for_config():
    # Testing for defaults
    context = {
        'cookiecutter': {
            'full_name': 'Firstname Lastname',
            'email': 'test@example.com',
            'github_username': 'test_user',
            'project_name': 'Test Project',
            'repo_name': 'test_repo',
            'project_short_description': 'A short description of the project.',
            'use_pypi_deployment_with_travis': 'y',
            'open_source_license': 'MIT license',
        }
    }

    no_input = False
    config_dict = prompt_for_config(context, no_input)

    assert config_dict['full_name'] == 'Firstname Lastname'
    assert config_dict['email'] == 'test@example.com'


# Generated at 2022-06-22 12:27:29.396478
# Unit test for function read_user_dict
def test_read_user_dict():
    from click.testing import CliRunner
    from cookiecutter.prompt import read_user_dict
    from cookiecutter.main import cookiecutter

    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(
            cookiecutter,
            [
                'tests/fake-repo-pre/{{cookiecutter.version_control}}-workflow',
                '--no-input',
                '-c',
                'tests/test-config.yaml',
            ],
            input='{ "cc_config_key": "cc_config_value" }\n',
        )
        assert result.exit_code == 0
        assert result.exception is None


# Generated at 2022-06-22 12:27:37.974708
# Unit test for function read_user_dict
def test_read_user_dict():
    var_name = 'test'
    default_value = {'test': 1}
    result = read_user_dict(var_name, default_value)
    assert result == default_value

# Generated at 2022-06-22 12:27:48.781665
# Unit test for function read_user_dict
def test_read_user_dict():
    # Test user enters dictionary correctly
    assert read_user_dict('test', {'test': 'dict'}) == {'test': 'dict'}

    # Test user enters string of dictionary
    assert read_user_dict('test', {'test': 'dict'}) == {'test': 'dict'}

    # Test user enters new dictionary
    assert read_user_dict('test', {'test': 'dict'}) == {'test2': 'dict2'}

    # Test user enters string that can't be converted
    assert read_user_dict('test', {'test': 'dict'}) == {'test': 'dict'}

    # Test user enters invalid value
    assert read_user_dict('test', {'test': 'dict'}) == {'test': 'dict'}

# Generated at 2022-06-22 12:27:59.394274
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:28:07.507612
# Unit test for function read_user_dict
def test_read_user_dict():
    dict_value = OrderedDict(
        [
            ("distribution", "Ubuntu"),
            ("version", "18.04"),
            ("operation", "install"),
        ]
    )
    dict_value_input = "{" + '"' + "distribution" + '"' + ": " + '"' + "Fedora" + '"' + "}"

    assert read_user_dict("package_manager", dict_value) == dict_value
    assert read_user_dict("package_manager", dict_value) != dict_value_input

# Generated at 2022-06-22 12:28:19.683117
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:28:22.296160
# Unit test for function read_user_choice
def test_read_user_choice():
    expected = ['p', 'peanut']
    actual = read_user_choice("Select an option", expected)
    assert actual in expected
    assert isinstance(actual, str)

# Generated at 2022-06-22 12:28:25.617952
# Unit test for function prompt_for_config
def test_prompt_for_config():
    from cookiecutter.config import load_config

    config = load_config()
    context = config.context

    assert prompt_for_config(context)


test_prompt_for_config()

# Generated at 2022-06-22 12:28:30.526549
# Unit test for function read_user_dict
def test_read_user_dict():
    user_dict = read_user_dict("test_dict:", {"test":"test"})
    assert(isinstance(user_dict, dict))
    assert(user_dict["test"] == "test")
    try:
        user_dict = read_user_dict("test_dict:", "")
    except TypeError:
        # Exception caught
        print("TypeError Caught")


# Generated at 2022-06-22 12:28:42.025492
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Test prompt_for_config."""
    context = {
        'cookiecutter': {
            '_template': 'twoslashdot/cookiecutter-pypackage',
            'project_name': '{{ cookiecutter.repo_name.replace("_", " ") }}',
            'repo_name': '{{ cookiecutter.project_name.replace(" ", "_") }}',
            'project_short_description': 'A short description of the project.',
            'release_date': '{{ cookiecutter.year }}-{{ cookiecutter.month }}-{{ cookiecutter.day }}',
            'version': '0.1.0',
        }
    }
    cookiecutter_dict = prompt_for_config(context)

# Generated at 2022-06-22 12:28:51.004861
# Unit test for function read_user_dict
def test_read_user_dict():
    default_value = { "key1":"value1", "key2":"value2"}
    cookiecutter_dict = { "key3":"value3", "key4":"value4"}

    value = read_user_dict("test", default_value)
    assert value == default_value

    value = read_user_dict("test", default_value, cookiecutter_dict)
    assert value == default_value

    value = read_user_dict("test", default_value, cookiecutter_dict, False)
    assert value == default_value

# Generated at 2022-06-22 12:29:17.752398
# Unit test for function prompt_for_config
def test_prompt_for_config():
    from cookiecutter.main import cookiecutter
    from cookiecutter import utils
    from simple_test_project import expected_context
    from simple_test_project.expected_context import expected_context_full
    from simple_test_project.expected_context import expected_context_raw_config
    
    # Save test project to temporary directory
    output_dir = utils.make_tempdir()
    temp_project_dir = cookiecutter('simple_test_project', output_dir=output_dir)
    
    # Load cookiecutter.json
    with open(temp_project_dir + '\cookiecutter.json') as json_file:
        cookiecutter_json = json.load(json_file, object_pairs_hook=OrderedDict)
    
    # Get result of prompt_for_config
   

# Generated at 2022-06-22 12:29:24.386273
# Unit test for function prompt_for_config
def test_prompt_for_config():
    from cookiecutter.config import generate_context

    default_context = generate_context(
        context_file='tests/test-data/fake-repo/cookiecutter.json'
    )

    cookiecutter_dict = prompt_for_config(default_context)

    assert cookiecutter_dict == {
        'repo_name': 'pypackage_skeleton',
        'project_name': 'Example Project Name'
    }



# Generated at 2022-06-22 12:29:27.828088
# Unit test for function read_user_dict
def test_read_user_dict():

   target_dd = read_user_dict("Src  Dict",{ "a": "A", "b": "B" })
   assert target_dd == { "a": "A", "b": "B" }

# Generated at 2022-06-22 12:29:39.220977
# Unit test for function read_user_dict
def test_read_user_dict():

    default_dict = {'a': 0, 'b': 1, 'c': '2'}
    empty_dict = {}
    result_dict = read_user_dict('test_dict', default_dict)
    if not result_dict:
        raise ValueError('Empty resulted dictionary')
    elif len(default_dict.keys()) != len(result_dict.keys()):
        raise ValueError('Resulted dictionary does not match the default one')
    elif isinstance(result_dict, dict):
        pass
    else:
        raise ValueError('Resulted dictionary is not a dictionary')

    try:
        read_user_dict('test_dict', empty_dict)
        raise ValueError('Empty default dictionary should not be allowed')
    except:
        pass

# Generated at 2022-06-22 12:29:48.369328
# Unit test for function prompt_for_config
def test_prompt_for_config():
    "Unit test for function prompt_for_config"
    data = {
        'project_name': 'CodeProject',
        'project_slug': 'codeproject',
        'author_name': 'Hugh Brown',
        'email': 'me@example.com',
        'description': 'CodeProject is amazing!',
        'domain_name': 'example.com',
        'version': '0.1.0',
        'timezone': 'UTC',
        'has_py': True,
    }

    #TODO: test 1 - 
    #TODO: test 2 - 
    #TODO: test 3 - 

    cookiecutter_dict = prompt_for_config(data, no_input=True)
    assert cookiecutter_dict['project_name'] == data['project_name']


# Generated at 2022-06-22 12:29:59.017882
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Verify that all the function prompt_for_config do not have any issue."""
    from .generate import _prompt_for_config
    from .load import get_context_for_repo
    from .load import get_user_config_data

    repo_dict = get_context_for_repo('tests/test-repo-tmpl/')
    user_config_data = get_user_config_data('~/.cookiecutterrc')

# Generated at 2022-06-22 12:30:10.662778
# Unit test for function read_user_dict
def test_read_user_dict():
    test_variable = "test_variable"
    test_dict = {"a":"A","b":"B","c":"C"}
    test_user_value = '{"user_a":"A","user_b":"B","user_c":"C","user_d":"D"}'

    assert read_user_dict(test_variable, test_dict) == test_dict
    assert read_user_dict(test_variable, test_dict) == test_dict
    assert read_user_dict(test_variable, test_dict) == test_dict
    assert read_user_dict(test_variable, test_dict) == test_dict
    assert read_user_dict(test_variable, test_dict) == test_dict
    assert read_user_dict(test_variable, test_dict) == test_dict

# Generated at 2022-06-22 12:30:18.112607
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Provide sample data and render it based on user input."""
    sample_context = {
        'repo_name': '{{ cookiecutter.project_name.replace(" ", "_") }}',
        'project_name': 'Test Project',
        'your_email': 'dev@example.com',
    }
    # Need to add 'cookiecutter' because it's needed to render the variables
    sample_context['cookiecutter'] = sample_context
    sample_output = prompt_for_config(sample_context, no_input=True)
    assert sample_output['project_name'] == 'Test Project'
    assert sample_output['repo_name'] == 'Test_Project'
    assert sample_output['your_email'] == 'dev@example.com'

# Generated at 2022-06-22 12:30:30.145041
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:30:37.180959
# Unit test for function process_json
def test_process_json():
    """Test if the function returns the correct value"""
    dict_actual = {'foo': 'bar'}
    # test if the function returns the same dict object
    dict_expected = process_json(str(dict_actual))
    assert dict_actual == dict_expected
    # test if the function returns an Exception when the string is not in json format
    with pytest.raises(click.UsageError):
        process_json('123')



# Generated at 2022-06-22 12:31:04.024279
# Unit test for function prompt_for_config
def test_prompt_for_config():
    from cookiecutter.utils import rmtree
    from cookiecutter.main import cookiecutter
    from cookiecutter.compat import input

    template = r'tests/test-output/{{ cookiecutter.repo_name }}/'

# Generated at 2022-06-22 12:31:12.300652
# Unit test for function prompt_for_config
def test_prompt_for_config():
    from cookiecutter.main import cookiecutter

    context = cookiecutter(
        'tests/fake-repo-pre/',
        no_input=True,
        extra_context={'cookiecutter': {'full_name': 'Peter Pan'}},
    )

    assert 'full_name' in context['cookiecutter']
    assert context['cookiecutter']['full_name'] == 'Peter Pan'

    ############################################################################

    full_name = 'Peter Pan'
    context = cookiecutter(
        'tests/fake-repo-pre/',
        no_input=True,
        extra_context={'cookiecutter': {'full_name': full_name}},
        overwrite_if_exists=True,
    )

    assert 'full_name' in context['cookiecutter']


# Generated at 2022-06-22 12:31:15.822556
# Unit test for function read_user_dict
def test_read_user_dict():
    user_value = "this is a test"
    user_variable = read_user_dict("test", None)
    print(user_variable )


# Generated at 2022-06-22 12:31:26.448241
# Unit test for function prompt_for_config
def test_prompt_for_config():
    user_dict = {
        'full_name': 'Firstname Lastname',
        'email': 'user@example.com',
        'github_username': 'octocat',
        # 'project_name': 'My Project',
        'repo_name': 'my_repo',
        # 'project_short_description': 'A short description of the project.',
    }
    context = {
        'cookiecutter': OrderedDict(
            [(key, None) for key in sorted(user_dict.keys())]
        )
    }
    for key in user_dict:
        context['cookiecutter'][key] = user_dict[key]

    # Re-init with the user_dict filled out
    user_dict = prompt_for_config(context, no_input=False)

    # Test
   

# Generated at 2022-06-22 12:31:30.874633
# Unit test for function prompt_for_config
def test_prompt_for_config():
    import contextlib
    import io
    import sys


# Generated at 2022-06-22 12:31:42.577507
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """
    Unit test to ensure that the function returns the expected dictionary
    """
    context = {}
    context['cookiecutter'] = {}
    context['cookiecutter']['repo_name'] = '{{ cookiecutter.project_dir.replace("/", "_") }}'
    context['cookiecutter']['project_dir'] = 'hello-world'
    context['cookiecutter']['name'] = '__test__'
    context['cookiecutter']['description'] = 'Test'
    context['cookiecutter']['github_username'] = 'hackebrot'
    context['cookiecutter']['project_name'] = 'Cookiecutter Cookiecutter'
    context['cookiecutter']['pypi_username'] = 'hackebrot'

# Generated at 2022-06-22 12:31:54.702003
# Unit test for function prompt_for_config
def test_prompt_for_config():
    def make_context(cookiecutter_dict):
        return {'cookiecutter': cookiecutter_dict}

    def compare_dicts(dict1, dict2):
        assert len(dict1) == len(dict2)
        for k, v in dict1.items():
            assert k in dict2
            assert v == dict2[k]

    # test with no input
    context = make_context({
        'project_name': 'Peanut Butter Cookie',
        'username': 'audreyr'
    })
    compare_dicts(context['cookiecutter'], prompt_for_config(context, no_input=True))

    # test with choices

# Generated at 2022-06-22 12:32:03.288977
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:32:06.971852
# Unit test for function read_user_dict
def test_read_user_dict():
    default_value = {"spam": "eggs", "ham": "eggs"}
    var_name = "spam"
    results = read_user_dict(var_name, default_value)
    assert results == {"spam": "eggs", "ham": "eggs"}

# Generated at 2022-06-22 12:32:12.622632
# Unit test for function read_user_choice
def test_read_user_choice():
    options = ["one", "two", "three"]
    assert read_user_choice("user_choice", options) in options
    assert read_user_choice("user_choice", options) in options
    assert read_user_choice("user_choice", options) in options
    assert read_user_choice("user_choice", options) in options

# Generated at 2022-06-22 12:32:41.498099
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """ Test Prompts """
    dict = {
        "cookiecutter": {"project_name": "My Project"}}
    assert prompt_for_config(dict) == {'project_name': 'My Project'}

    dict = {
        "cookiecutter": {"project_name": "A {{ cookiecutter.project_name }}"}}
    assert prompt_for_config(dict) == {'project_name': 'A My Project'}

    dict = {
        "cookiecutter": {"project_name": ["A", "B", "C"]}}
    assert prompt_for_config(dict, no_input=True) == {
        'project_name': 'A'}


# Generated at 2022-06-22 12:32:52.021945
# Unit test for function read_user_dict
def test_read_user_dict():
    from collections import OrderedDict

    from cookiecutter.main import prompt_for_config
    from cookiecutter.environment import StrictEnvironment


    def get_context(**kwargs):
        """
        Given dict, returns dict with the dict as the
        cookiecutter key and the items in kwargs as keys in there.
        """
        keys = list(kwargs.keys())
        return {
            'cookiecutter': {
                keys[0]: kwargs[keys[0]],
                keys[1]: kwargs[keys[1]],
                keys[2]: kwargs[keys[2]],
            }
        }

    # set up fake context dicts

# Generated at 2022-06-22 12:33:03.593749
# Unit test for function prompt_for_config
def test_prompt_for_config():
    """Unit test for prompt_for_config"""
    from click.testing import CliRunner
    from cookiecutter.prompt import prompt_for_config
    from cookiecutter import utils
    from collections import OrderedDict
    from tests.test_utils import is_dict_subset
    from jinja2 import Environment
    from pytest import raises
    from cookiecutter.exceptions import UndefinedVariableInTemplate
    from cookiecutter.utils import make_sure_path_exists

    # Read the template context
    template = 'tests/test-templates/prompt-context'
    project_dir = utils.get_project_dir(template)
    make_sure_path_exists(project_dir)
    template_dir = utils.get_template_dir(template, project_dir)
    context = ut

# Generated at 2022-06-22 12:33:15.114163
# Unit test for function read_user_dict
def test_read_user_dict():

    dict1 = {'key1': 'value1', 'key2': 'value2'}
    dict2 = {'key1': 'value1', 'key2': 'value2', '__validators': ['validator1', 'validator2']}
    dict3 = {'key1': 'value1', 'key2': 'value2', '__validators': 'validator1'}
    dict4 = ['validator1', 'validator2']
    dict5 = ['validator1']
    dict6 = 'validator1'
    dict7 = {'key1': 'value1', 'key2': 'value2', '__invalid': 'validator1'}
    dict8 = {'key1': 'value1', 'key2': 'value2', '__validators': ['invalid1', 'invalid2']}

# Generated at 2022-06-22 12:33:25.773760
# Unit test for function prompt_for_config
def test_prompt_for_config():
    '''Unit test for prompt_for_config'''
    expected = '''{
        "full_name": "carlie",
        "first_name": "carlie",
        "third": 0.3333333333333333,
        "__plus_one_first_name": "carlie1",
        "__plus_two_first_name": "carlie2",
        "__plus_one_full_name": "carlie1",
        "__plus_two_full_name": "carlie2",
        "__capitalized_first_name": "Carlie",
        "__capitalized_full_name": "Carlie"
    }'''


# Generated at 2022-06-22 12:33:36.977695
# Unit test for function prompt_for_config

# Generated at 2022-06-22 12:33:40.196698
# Unit test for function read_user_dict
def test_read_user_dict():
    assert read_user_dict('prompt', {'foo': 'bar'}) == {'foo': 'bar'}
    assert read_user_dict('prompt', {'foo': 'bar'})['foo'] == 'bar'

# Generated at 2022-06-22 12:33:44.848834
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {
        'cookiecutter': {
            'project_name': 'Awesome Project',
            'repo_name': '{{ cookiecutter.project_name.lower().replace(" ", "-") }}',
            'author': 'Your Name',
            'email': 'your@email.com',
            'description': 'A short description of the project.',
            'version': '0.1.0',
            'license': 'MIT',
            'open_source': 'y',
            'use_pycharm': 'n',
            'command_line_interface': {
                'use_click': 'y',
                'use_argparse': 'n'
            }
        }
    }
    cookiecutter_dict = prompt_for_config(context)

# Generated at 2022-06-22 12:33:46.470081
# Unit test for function process_json
def test_process_json():
    assert process_json('{"foo": "bar"}') == {'foo': 'bar'}

# Generated at 2022-06-22 12:33:55.596631
# Unit test for function prompt_for_config
def test_prompt_for_config():
    context = {
        'cookiecutter': {
            'project_name': 'Awesome Project',
            'project_slug': 'awesome_project',
            'description': 'The best Python project ever',
            'author': 'Your name here',
            'email': 'your_email@example.com',
            'copyright': '2014, Your name here',
            'version': '0.1.0',
            'full_name': 'Your name here',
        }
    }
    cookiecutter_dict = prompt_for_config(context, no_input=True)
    assert isinstance(cookiecutter_dict, dict)
    assert cookiecutter_dict['project_name'] == 'Awesome Project'



# Generated at 2022-06-22 12:34:16.536400
# Unit test for function prompt_for_config
def test_prompt_for_config():
    from cookiecutter.main import cookiecutter
    import pytest
    with pytest.raises(SystemExit) as e:
        cookiecutter('tests/test-data/fake-repo-pre/', no_input=True)

    assert e.value.code == 0

# Generated at 2022-06-22 12:34:26.700978
# Unit test for function read_user_dict
def test_read_user_dict():
    # No default
    assert read_user_dict('foo', {}) == {}
    assert read_user_dict('foo', {'b': 'c'}) == {'b': 'c'}
    assert read_user_dict('foo', {'b': {'c': 'd'}}) == {'b': {'c': 'd'}}

    # With default
    assert read_user_dict('foo', {'a': 'b'}) == {'a': 'b'}
    assert read_user_dict('foo', {'a': {'b': 'c'}}) == {'a': {'b': 'c'}}