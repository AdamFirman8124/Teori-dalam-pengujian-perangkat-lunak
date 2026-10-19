

# Generated at 2024-06-01 16:48:41.060771
# Unit test for function prompt_for_config
def test_prompt_for_config():    context = {
        'cookiecutter': {
            'project_name': 'Test Project',
            'repo_name': '{{ cookiecutter.project_name|lower|replace(" ", "_") }}',
            'author': 'Test Author',
            'license': ['MIT', 'BSD', 'GPL'],
            '__private_key': 'private_value',
            '_hidden_key': 'hidden_value'
        }
    }


# Generated at 2024-06-01 16:48:45.118452
# Unit test for function process_json
def test_process_json():    valid_json = '{"key": "value"}'

# Generated at 2024-06-01 16:48:48.261988
# Unit test for function prompt_for_config
def test_prompt_for_config():    context = {
        'cookiecutter': {
            'project_name': 'Test Project',
            'repo_name': '{{ cookiecutter.project_name|lower|replace(" ", "_") }}',
            'author': 'Test Author',
            'license': ['MIT', 'BSD', 'GPL'],
            '_private': 'should not be rendered',
            '__hidden': 'should be rendered'
        }
    }


# Generated at 2024-06-01 16:48:51.563310
# Unit test for function render_variable
def test_render_variable():    env = StrictEnvironment()

# Generated at 2024-06-01 16:48:55.975100
# Unit test for function read_user_dict
def test_read_user_dict():    from click.testing import CliRunner


# Generated at 2024-06-01 16:48:59.401091
# Unit test for function prompt_for_config
def test_prompt_for_config():    context = {
        'cookiecutter': {
            'project_name': 'Test Project',
            'repo_name': '{{ cookiecutter.project_name|lower|replace(" ", "_") }}',
            'author': 'Test Author',
            'license': ['MIT', 'BSD', 'GPL'],
            '_private': 'should not be prompted',
            '__hidden': 'should be rendered'
        }
    }


# Generated at 2024-06-01 16:49:02.162990
# Unit test for function process_json
def test_process_json():    valid_json = '{"key": "value"}'

# Generated at 2024-06-01 16:49:04.965145
# Unit test for function read_user_dict
def test_read_user_dict():    from click.testing import CliRunner


# Generated at 2024-06-01 16:49:09.058446
# Unit test for function render_variable
def test_render_variable():    from jinja2 import Environment

# Generated at 2024-06-01 16:49:12.274355
# Unit test for function prompt_for_config
def test_prompt_for_config():    context = {
        'cookiecutter': {
            'project_name': 'Test Project',
            'repo_name': '{{ cookiecutter.project_name|lower|replace(" ", "_") }}',
            'author': 'Test Author',
            'license': ['MIT', 'BSD', 'GPL'],
            '_private': 'should not be prompted',
            '__hidden': 'should be rendered'
        }
    }


# Generated at 2024-06-01 16:49:27.104204
# Unit test for function prompt_for_config
def test_prompt_for_config():    context = {
        'cookiecutter': {
            'project_name': 'Test Project',
            'repo_name': '{{ cookiecutter.project_name|lower|replace(" ", "_") }}',
            'description': 'A test project.',
            'author': 'Test Author',
            'license': ['MIT', 'BSD', 'GPL'],
            '_private': 'should be ignored',
            '__private_rendered': '{{ cookiecutter.project_name }} rendered'
        }
    }


# Generated at 2024-06-01 16:49:30.286478
# Unit test for function prompt_for_config
def test_prompt_for_config():    context = {
        'cookiecutter': {
            'project_name': 'Test Project',
            'repo_name': '{{ cookiecutter.project_name|lower|replace(" ", "_") }}',
            'description': 'A test project.',
            'author': 'Test Author',
            'license': ['MIT', 'BSD', 'GPL'],
            '_private': 'should not be prompted',
            '__hidden': 'should be rendered'
        }
    }


# Generated at 2024-06-01 16:49:33.767720
# Unit test for function render_variable
def test_render_variable():    from jinja2 import Environment

# Generated at 2024-06-01 16:49:39.193797
# Unit test for function read_user_dict
def test_read_user_dict():    from click.testing import CliRunner


# Generated at 2024-06-01 16:49:43.464152
# Unit test for function process_json
def test_process_json():    valid_json = '{"key": "value"}'

# Generated at 2024-06-01 16:49:46.723507
# Unit test for function process_json
def test_process_json():    valid_json = '{"key": "value"}'

# Generated at 2024-06-01 16:49:49.770869
# Unit test for function prompt_for_config
def test_prompt_for_config():    context = {
        'cookiecutter': {
            'project_name': 'Test Project',
            'repo_name': '{{ cookiecutter.project_name|lower|replace(" ", "_") }}',
            'description': 'A test project.',
            'author': 'Test Author',
            'open_source': ['yes', 'no'],
            'license': {
                'type': 'MIT',
                'year': '2023',
                'holder': '{{ cookiecutter.author }}'
            }
        }
    }


# Generated at 2024-06-01 16:49:53.503870
# Unit test for function process_json
def test_process_json():    valid_json = '{"key": "value"}'

# Generated at 2024-06-01 16:49:57.351556
# Unit test for function read_user_dict
def test_read_user_dict():    from click.testing import CliRunner


# Generated at 2024-06-01 16:50:00.570912
# Unit test for function prompt_for_config
def test_prompt_for_config():    context = {
        'cookiecutter': {
            'project_name': 'Test Project',
            'repo_name': '{{ cookiecutter.project_name|lower|replace(" ", "_") }}',
            'author': 'Test Author',
            'license': ['MIT', 'BSD', 'GPL'],
            '_private': 'should not be rendered',
            '__private_dict': {'key': 'value'}
        }
    }


# Generated at 2024-06-01 16:50:10.237909
# Unit test for function prompt_for_config
def test_prompt_for_config():    context = {
        'cookiecutter': {
            'project_name': 'Test Project',
            'repo_name': '{{ cookiecutter.project_name|lower|replace(" ", "_") }}',
            'author': 'Test Author',
            'license': ['MIT', 'BSD', 'GPL'],
            '_private': 'should not be rendered',
            '__hidden': 'should be rendered'
        }
    }


# Generated at 2024-06-01 16:50:13.758820
# Unit test for function prompt_for_config
def test_prompt_for_config():    context = {
        'cookiecutter': {
            'project_name': 'Test Project',
            'repo_name': '{{ cookiecutter.project_name|lower|replace(" ", "_") }}',
            'description': 'A simple project.',
            'author': 'Test Author',
            'license': ['MIT', 'BSD', 'GPL'],
            '_private': 'This should be ignored',
            '__metadata': {
                'version': '1.0.0',
                'maintainer': '{{ cookiecutter.author }}'
            }
        }
    }


# Generated at 2024-06-01 16:50:16.992847
# Unit test for function prompt_for_config
def test_prompt_for_config():    context = {
        'cookiecutter': {
            'project_name': 'Test Project',
            'repo_name': '{{ cookiecutter.project_name|lower|replace(" ", "_") }}',
            'author': 'Test Author',
            'license': ['MIT', 'BSD', 'GPL'],
            '_private': 'should not be prompted',
            '__hidden': 'should be rendered'
        }
    }


# Generated at 2024-06-01 16:50:20.205191
# Unit test for function prompt_for_config
def test_prompt_for_config():    context = {
        'cookiecutter': {
            'project_name': 'Test Project',
            'repo_name': '{{ cookiecutter.project_name|lower|replace(" ", "_") }}',
            'author': 'Test Author',
            'license': ['MIT', 'BSD', 'GPL'],
            '_private': 'should not be prompted',
            '__hidden': 'should be rendered'
        }
    }


# Generated at 2024-06-01 16:50:22.669075
# Unit test for function process_json
def test_process_json():    valid_json = '{"key": "value"}'

# Generated at 2024-06-01 16:50:24.965317
# Unit test for function process_json
def test_process_json():    valid_json = '{"key": "value"}'

# Generated at 2024-06-01 16:50:29.086978
# Unit test for function prompt_for_config
def test_prompt_for_config():    context = {
        'cookiecutter': {
            'project_name': 'Test Project',
            'repo_name': '{{ cookiecutter.project_name|lower|replace(" ", "_") }}',
            'description': 'A test project.',
            'author': 'Test Author',
            'license': ['MIT', 'BSD', 'GPL'],
            '_private': 'This should be ignored',
            '__hidden': 'This should be rendered'
        }
    }


# Generated at 2024-06-01 16:50:35.227088
# Unit test for function prompt_for_config
def test_prompt_for_config():    context = {
        'cookiecutter': {
            'project_name': 'Test Project',
            'repo_name': '{{ cookiecutter.project_name|lower|replace(" ", "_") }}',
            'author': 'Test Author',
            'license': ['MIT', 'BSD', 'GPL'],
            '_private': 'should not be rendered',
            '__hidden': 'should be rendered'
        }
    }


# Generated at 2024-06-01 16:50:37.646732
# Unit test for function process_json
def test_process_json():    valid_json = '{"key": "value"}'

# Generated at 2024-06-01 16:50:41.075585
# Unit test for function prompt_for_config
def test_prompt_for_config():    context = {
        'cookiecutter': {
            'project_name': 'Test Project',
            'repo_name': '{{ cookiecutter.project_name|lower|replace(" ", "_") }}',
            'author': 'Test Author',
            'license': ['MIT', 'BSD', 'GPL'],
            '_private': 'should not be prompted',
            '__hidden': 'should be rendered'
        }
    }


# Generated at 2024-06-01 16:50:52.624302
# Unit test for function prompt_for_config
def test_prompt_for_config():    context = {
        'cookiecutter': {
            'project_name': 'Test Project',
            'repo_name': '{{ cookiecutter.project_name|lower|replace(" ", "_") }}',
            'description': 'A test project.',
            'author': 'Test Author',
            'open_source': ['yes', 'no'],
            '__private_key': 'private_value',
            '_hidden_key': 'hidden_value'
        }
    }


# Generated at 2024-06-01 16:50:55.653672
# Unit test for function prompt_for_config
def test_prompt_for_config():    context = {
        'cookiecutter': {
            'project_name': 'Test Project',
            'repo_name': '{{ cookiecutter.project_name|lower|replace(" ", "_") }}',
            'author': 'Test Author',
            'license': ['MIT', 'BSD', 'GPL'],
            '_private': 'should not be prompted',
            '__hidden': 'should be rendered'
        }
    }


# Generated at 2024-06-01 16:50:58.361142
# Unit test for function read_user_dict
def test_read_user_dict():    from click.testing import CliRunner


# Generated at 2024-06-01 16:51:01.193336
# Unit test for function read_user_dict
def test_read_user_dict():    from click.testing import CliRunner


# Generated at 2024-06-01 16:51:05.925975
# Unit test for function prompt_for_config
def test_prompt_for_config():    context = {
        'cookiecutter': {
            'project_name': 'Test Project',
            'repo_name': '{{ cookiecutter.project_name|lower|replace(" ", "_") }}',
            'author': 'Test Author',
            'languages': ['Python', 'JavaScript', 'Go'],
            '__private_var': 'should not be prompted',
            '_hidden_var': 'should not be prompted'
        }
    }


# Generated at 2024-06-01 16:51:09.626830
# Unit test for function prompt_for_config
def test_prompt_for_config():    context = {
        'cookiecutter': {
            'project_name': 'Test Project',
            'repo_name': '{{ cookiecutter.project_name|lower|replace(" ", "_") }}',
            'description': 'A test project.',
            'author': 'Test Author',
            'license': ['MIT', 'BSD', 'GPL'],
            '_private': 'should not be rendered',
            '__hidden': 'should be rendered'
        }
    }


# Generated at 2024-06-01 16:51:12.382737
# Unit test for function process_json
def test_process_json():    valid_json = '{"key": "value"}'

# Generated at 2024-06-01 16:51:17.058622
# Unit test for function read_user_dict
def test_read_user_dict():    from click.testing import CliRunner


# Generated at 2024-06-01 16:51:19.602453
# Unit test for function read_user_choice
def test_read_user_choice():    import pytest

# Generated at 2024-06-01 16:51:22.539168
# Unit test for function prompt_for_config
def test_prompt_for_config():    context = {
        'cookiecutter': {
            'project_name': 'Test Project',
            'repo_name': '{{ cookiecutter.project_name|lower|replace(" ", "_") }}',
            'author': 'Test Author',
            'license': ['MIT', 'BSD', 'GPL'],
            '_private': 'should not be prompted',
            '__hidden': 'should be rendered'
        }
    }


# Generated at 2024-06-01 16:51:51.290039
# Unit test for function prompt_for_config
def test_prompt_for_config():    context = {
        'cookiecutter': {
            'project_name': 'Test Project',
            'repo_name': '{{ cookiecutter.project_name|lower|replace(" ", "_") }}',
            'author': 'Test Author',
            'license': ['MIT', 'BSD', 'GPL'],
            '_private': 'should not be prompted',
            '__hidden': 'should be rendered'
        }
    }


# Generated at 2024-06-01 16:51:55.566868
# Unit test for function prompt_for_config
def test_prompt_for_config():    context = {
        'cookiecutter': {
            'project_name': 'Test Project',
            'repo_name': '{{ cookiecutter.project_name|lower|replace(" ", "_") }}',
            'author': 'Test Author',
            'license': ['MIT', 'BSD', 'GPL'],
            '_private': 'should not be prompted',
            '__hidden': 'should be rendered'
        }
    }


# Generated at 2024-06-01 16:51:59.495867
# Unit test for function prompt_for_config
def test_prompt_for_config():    context = {
        'cookiecutter': {
            'project_name': 'Test Project',
            'repo_name': '{{ cookiecutter.project_name|lower|replace(" ", "_") }}',
            'author': 'Test Author',
            'license': ['MIT', 'BSD', 'GPL'],
            '_private': 'should not be rendered',
            '__hidden': 'should be rendered'
        }
    }


# Generated at 2024-06-01 16:52:03.269917
# Unit test for function prompt_for_config
def test_prompt_for_config():    context = {
        'cookiecutter': {
            'project_name': 'Test Project',
            'repo_name': '{{ cookiecutter.project_name|lower|replace(" ", "_") }}',
            'author': 'Test Author',
            'license': ['MIT', 'BSD', 'GPL'],
            '_private': 'should not be rendered',
            '__hidden': 'should be rendered'
        }
    }


# Generated at 2024-06-01 16:52:08.276502
# Unit test for function read_user_dict
def test_read_user_dict():    from click.testing import CliRunner


# Generated at 2024-06-01 16:52:11.018211
# Unit test for function prompt_for_config
def test_prompt_for_config():    context = {
        'cookiecutter': {
            'project_name': 'Test Project',
            'repo_name': '{{ cookiecutter.project_name|lower|replace(" ", "_") }}',
            'author': 'Test Author',
            'license': ['MIT', 'BSD', 'GPL'],
            '_private': 'should not be rendered',
            '__private_rendered': '{{ cookiecutter.author }}'
        }
    }


# Generated at 2024-06-01 16:52:16.539219
# Unit test for function prompt_for_config
def test_prompt_for_config():    context = {
        'cookiecutter': {
            'project_name': 'Test Project',
            'repo_name': '{{ cookiecutter.project_name|lower|replace(" ", "_") }}',
            'description': 'A test project.',
            'author': 'Test Author',
            'nested': {
                'key1': 'value1',
                'key2': '{{ cookiecutter.project_name }} Nested'
            },
            'choices': ['option1', 'option2', 'option3']
        }
    }


# Generated at 2024-06-01 16:52:20.345321
# Unit test for function read_user_dict
def test_read_user_dict():    from click.testing import CliRunner


# Generated at 2024-06-01 16:52:23.044745
# Unit test for function process_json
def test_process_json():    valid_json = '{"key": "value"}'

# Generated at 2024-06-01 16:52:25.427594
# Unit test for function process_json
def test_process_json():    # Test with valid JSON string
    valid_json = '{"key": "value"}'
    assert process_json(valid_json) == OrderedDict([('key', 'value')])

    # Test with invalid JSON string
    invalid_json = '{"key": "value"'
    try:
        process_json(invalid_json)
    except click.UsageError as e:
        assert str(e) == 'Unable to decode to JSON.'

    # Test with non-dict JSON
    non_dict_json = '["value1", "value2"]'
    try:
        process_json(non_dict_json)
    except click.UsageError as e:
        assert str(e) == 'Requires JSON dict.'


# Generated at 2024-06-01 16:52:42.866652
# Unit test for function prompt_for_config
def test_prompt_for_config():    context = {
        'cookiecutter': {
            'project_name': 'Test Project',
            'repo_name': '{{ cookiecutter.project_name|lower|replace(" ", "_") }}',
            'author': 'Test Author',
            'license': ['MIT', 'BSD', 'GPL'],
            '_private': 'should not be rendered',
            '__hidden': 'should be rendered'
        }
    }


# Generated at 2024-06-01 16:52:45.029119
# Unit test for function process_json
def test_process_json():    valid_json = '{"key": "value"}'

# Generated at 2024-06-01 16:52:48.978241
# Unit test for function process_json
def test_process_json():    valid_json = '{"key": "value"}'

# Generated at 2024-06-01 16:52:52.198976
# Unit test for function prompt_for_config
def test_prompt_for_config():    context = {
        'cookiecutter': {
            'project_name': 'Test Project',
            'repo_name': '{{ cookiecutter.project_name|lower|replace(" ", "_") }}',
            'author': 'Test Author',
            'license': ['MIT', 'BSD', 'GPL'],
            '_private': 'should not be prompted',
            '__hidden': 'should be rendered'
        }
    }


# Generated at 2024-06-01 16:52:55.216225
# Unit test for function prompt_for_config
def test_prompt_for_config():    context = {
        'cookiecutter': {
            'project_name': 'Test Project',
            'repo_name': '{{ cookiecutter.project_name|lower|replace(" ", "_") }}',
            'author': 'Test Author',
            'license': ['MIT', 'BSD', 'GPL'],
            '_private': 'should not be prompted',
            '__hidden': 'should be rendered'
        }
    }


# Generated at 2024-06-01 16:52:57.830608
# Unit test for function process_json
def test_process_json():    valid_json = '{"key": "value"}'

# Generated at 2024-06-01 16:53:01.001974
# Unit test for function process_json
def test_process_json():    valid_json = '{"key": "value"}'

# Generated at 2024-06-01 16:53:06.026719
# Unit test for function prompt_for_config
def test_prompt_for_config():    context = {
        'cookiecutter': {
            'project_name': 'Test Project',
            'repo_name': '{{ cookiecutter.project_name|lower|replace(" ", "_") }}',
            'description': 'A test project.',
            'author': 'Test Author',
            'license': 'MIT',
            '_private_var': 'should not be prompted',
            '__private_rendered_var': '{{ cookiecutter.project_name }} rendered'
        }
    }


# Generated at 2024-06-01 16:53:09.048424
# Unit test for function read_user_dict
def test_read_user_dict():    from click.testing import CliRunner


# Generated at 2024-06-01 16:53:11.814051
# Unit test for function process_json
def test_process_json():    valid_json = '{"key": "value"}'

# Generated at 2024-06-01 16:53:29.023292
# Unit test for function read_user_dict
def test_read_user_dict():    from click.testing import CliRunner


# Generated at 2024-06-01 16:53:31.512967
# Unit test for function process_json
def test_process_json():    valid_json = '{"key": "value"}'

# Generated at 2024-06-01 16:53:34.354526
# Unit test for function prompt_for_config
def test_prompt_for_config():    context = {
        'cookiecutter': {
            'project_name': 'Test Project',
            'repo_name': '{{ cookiecutter.project_name|lower|replace(" ", "_") }}',
            'author': 'Test Author',
            'license': ['MIT', 'BSD', 'GPL'],
            '_private': 'should not be prompted',
            '__hidden': 'should be rendered'
        }
    }


# Generated at 2024-06-01 16:53:37.374306
# Unit test for function prompt_for_config
def test_prompt_for_config():    context = {
        'cookiecutter': {
            'project_name': 'Test Project',
            'repo_name': '{{ cookiecutter.project_name|lower|replace(" ", "_") }}',
            'author': 'Test Author',
            'license': ['MIT', 'BSD', 'GPL'],
            '__private_key': 'private_value',
            '_hidden_key': 'hidden_value'
        }
    }


# Generated at 2024-06-01 16:53:40.295814
# Unit test for function read_user_dict
def test_read_user_dict():    from click.testing import CliRunner


# Generated at 2024-06-01 16:53:43.578138
# Unit test for function read_user_dict
def test_read_user_dict():    from click.testing import CliRunner


# Generated at 2024-06-01 16:53:47.014732
# Unit test for function process_json
def test_process_json():    valid_json = '{"key": "value"}'

# Generated at 2024-06-01 16:53:50.066205
# Unit test for function prompt_for_config
def test_prompt_for_config():    context = {
        'cookiecutter': {
            'project_name': 'Test Project',
            'repo_name': '{{ cookiecutter.project_name|lower|replace(" ", "_") }}',
            'author': 'Test Author',
            'license': ['MIT', 'BSD', 'GPL'],
            '_private': 'should not be rendered',
            '__hidden': 'should be rendered'
        }
    }


# Generated at 2024-06-01 16:53:52.957599
# Unit test for function read_user_dict
def test_read_user_dict():    from click.testing import CliRunner


# Generated at 2024-06-01 16:53:56.576487
# Unit test for function prompt_for_config
def test_prompt_for_config():    context = {
        'cookiecutter': {
            'project_name': 'Test Project',
            'repo_name': '{{ cookiecutter.project_name|lower|replace(" ", "_") }}',
            'author': 'Test Author',
            'license': ['MIT', 'BSD', 'GPL'],
            '_private': 'should not be rendered',
            '__hidden': 'should be rendered'
        }
    }


# Generated at 2024-06-01 16:54:31.431993
# Unit test for function read_user_dict
def test_read_user_dict():    from click.testing import CliRunner


# Generated at 2024-06-01 16:54:34.130247
# Unit test for function process_json
def test_process_json():    valid_json = '{"key": "value"}'

# Generated at 2024-06-01 16:54:37.045090
# Unit test for function read_user_dict
def test_read_user_dict():    from click.testing import CliRunner


# Generated at 2024-06-01 16:54:41.042136
# Unit test for function prompt_for_config
def test_prompt_for_config():    context = {
        'cookiecutter': {
            'project_name': 'Test Project',
            'repo_name': '{{ cookiecutter.project_name|lower|replace(" ", "_") }}',
            'description': 'A simple project.',
            'author': 'Test Author',
            'license': ['MIT', 'BSD', 'GPL'],
            '_private': 'This should be ignored',
            '__metadata': {
                'version': '1.0.0',
                'maintainer': '{{ cookiecutter.author }}'
            }
        }
    }


# Generated at 2024-06-01 16:54:43.813208
# Unit test for function prompt_for_config
def test_prompt_for_config():    context = {
        'cookiecutter': {
            'project_name': 'Test Project',
            'repo_name': '{{ cookiecutter.project_name|lower|replace(" ", "_") }}',
            'author': 'Test Author',
            'license': ['MIT', 'BSD', 'GPL'],
            '_private': 'should not be rendered',
            '__hidden': 'should be rendered'
        }
    }


# Generated at 2024-06-01 16:54:47.315459
# Unit test for function prompt_for_config
def test_prompt_for_config():    context = {
        'cookiecutter': {
            'project_name': 'Test Project',
            'repo_name': '{{ cookiecutter.project_name|lower|replace(" ", "_") }}',
            'description': 'A test project.',
            'author': 'Test Author',
            'open_source': ['yes', 'no'],
            'license': {
                'name': 'MIT',
                'url': 'https://opensource.org/licenses/MIT'
            }
        }
    }


# Generated at 2024-06-01 16:54:49.915056
# Unit test for function read_user_dict
def test_read_user_dict():    from click.testing import CliRunner


# Generated at 2024-06-01 16:54:52.983122
# Unit test for function read_user_dict
def test_read_user_dict():    from click.testing import CliRunner


# Generated at 2024-06-01 16:54:56.014645
# Unit test for function prompt_for_config
def test_prompt_for_config():    context = {
        'cookiecutter': {
            'project_name': 'Test Project',
            'repo_name': '{{ cookiecutter.project_name|lower|replace(" ", "_") }}',
            'author': 'Test Author',
            'license': ['MIT', 'BSD', 'GPL'],
            '_private': 'This should be ignored',
            '__hidden': 'This should be rendered'
        }
    }


# Generated at 2024-06-01 16:55:00.025542
# Unit test for function prompt_for_config
def test_prompt_for_config():    context = {
        'cookiecutter': {
            'project_name': 'Test Project',
            'repo_name': '{{ cookiecutter.project_name|lower|replace(" ", "_") }}',
            'author': 'Test Author',
            'license': ['MIT', 'BSD', 'GPL'],
            '_private': 'should not be rendered',
            '__hidden': 'should be rendered'
        }
    }


# Generated at 2024-06-01 16:56:01.729370
# Unit test for function read_user_dict
def test_read_user_dict():    from click.testing import CliRunner


# Generated at 2024-06-01 16:56:04.719072
# Unit test for function read_user_dict
def test_read_user_dict():    from click.testing import CliRunner


# Generated at 2024-06-01 16:56:08.253862
# Unit test for function read_user_dict
def test_read_user_dict():    from click.testing import CliRunner


# Generated at 2024-06-01 16:56:11.724000
# Unit test for function prompt_for_config
def test_prompt_for_config():    context = {
        'cookiecutter': {
            'project_name': 'Test Project',
            'repo_name': '{{ cookiecutter.project_name|lower|replace(" ", "_") }}',
            'author': 'Test Author',
            'license': ['MIT', 'BSD', 'GPL'],
            '_private': 'should not be rendered',
            '__hidden': 'should be rendered'
        }
    }


# Generated at 2024-06-01 16:56:14.569222
# Unit test for function render_variable
def test_render_variable():    env = StrictEnvironment()

# Generated at 2024-06-01 16:56:19.341925
# Unit test for function prompt_for_config
def test_prompt_for_config():    context = {
        'cookiecutter': {
            'project_name': 'Test Project',
            'repo_name': '{{ cookiecutter.project_name|lower|replace(" ", "_") }}',
            'author': 'Test Author',
            'license': ['MIT', 'BSD', 'GPL'],
            '_private': 'should not be prompted',
            '__hidden': 'should be rendered'
        }
    }


# Generated at 2024-06-01 16:56:23.055107
# Unit test for function process_json
def test_process_json():    valid_json = '{"key": "value"}'

# Generated at 2024-06-01 16:56:26.539028
# Unit test for function render_variable
def test_render_variable():    env = StrictEnvironment()

# Generated at 2024-06-01 16:56:30.070982
# Unit test for function prompt_for_config
def test_prompt_for_config():    context = {
        'cookiecutter': {
            'project_name': 'Test Project',
            'repo_name': '{{ cookiecutter.project_name|lower|replace(" ", "_") }}',
            'author': 'Test Author',
            'license': ['MIT', 'BSD', 'GPL'],
            '_private': 'should not be prompted',
            '__hidden': 'should be rendered'
        }
    }


# Generated at 2024-06-01 16:56:33.992212
# Unit test for function read_user_dict
def test_read_user_dict():    from click.testing import CliRunner


# Generated at 2024-06-01 16:57:37.549283
# Unit test for function process_json
def test_process_json():    valid_json = '{"key": "value"}'

# Generated at 2024-06-01 16:57:41.533198
# Unit test for function prompt_for_config
def test_prompt_for_config():    context = {
        'cookiecutter': {
            'project_name': 'Test Project',
            'repo_name': '{{ cookiecutter.project_name|lower|replace(" ", "_") }}',
            'author': 'Test Author',
            'license': ['MIT', 'BSD', 'GPL'],
            '_private': 'This should not be prompted',
            '__hidden': 'This should be rendered'
        }
    }


# Generated at 2024-06-01 16:57:44.327026
# Unit test for function render_variable
def test_render_variable():    env = StrictEnvironment()

# Generated at 2024-06-01 16:57:48.918962
# Unit test for function prompt_for_config
def test_prompt_for_config():    context = {
        'cookiecutter': {
            'project_name': 'Test Project',
            'repo_name': '{{ cookiecutter.project_name|lower|replace(" ", "_") }}',
            'author': 'Test Author',
            'license': ['MIT', 'BSD', 'GPL'],
            '_private': 'should not be rendered',
            '__private_rendered': '{{ cookiecutter.project_name }} rendered'
        }
    }


# Generated at 2024-06-01 16:57:54.420881
# Unit test for function prompt_for_config
def test_prompt_for_config():    context = {
        'cookiecutter': {
            'project_name': 'Test Project',
            'repo_name': '{{ cookiecutter.project_name|lower|replace(" ", "_") }}',
            'author': 'Test Author',
            'license': ['MIT', 'BSD', 'GPL'],
            '__private_key': 'private_value',
            '_hidden_key': 'hidden_value'
        }
    }


# Generated at 2024-06-01 16:57:57.129685
# Unit test for function prompt_for_config
def test_prompt_for_config():    context = {
        'cookiecutter': {
            'project_name': 'Test Project',
            'repo_name': '{{ cookiecutter.project_name|lower|replace(" ", "_") }}',
            'author': 'Test Author',
            'license': ['MIT', 'BSD', 'GPL'],
            '_private': 'should not be prompted',
            '__hidden': 'should be rendered'
        }
    }


# Generated at 2024-06-01 16:58:00.575338
# Unit test for function read_user_dict
def test_read_user_dict():    from click.testing import CliRunner


# Generated at 2024-06-01 16:58:03.790682
# Unit test for function prompt_for_config
def test_prompt_for_config():    context = {
        'cookiecutter': {
            'project_name': 'Test Project',
            'repo_name': '{{ cookiecutter.project_name|lower|replace(" ", "_") }}',
            'description': 'A test project.',
            'author': 'Test Author',
            'license': ['MIT', 'BSD', 'GPL'],
            '_private': 'This should be ignored',
            '__hidden': 'This should be rendered'
        }
    }


# Generated at 2024-06-01 16:58:07.085814
# Unit test for function read_user_choice
def test_read_user_choice():    from click.testing import CliRunner


# Generated at 2024-06-01 16:58:10.157517
# Unit test for function read_user_dict
def test_read_user_dict():    from click.testing import CliRunner
