

# Generated at 2022-06-12 22:56:24.860545
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    class FakeModuleArgumentSpecValidator(ModuleArgumentSpecValidator):
        def __init__(self, *args, **kwargs):
            super(FakeModuleArgumentSpecValidator, self).__init__(*args, **kwargs)

        def validate(self, parameters):
            return super(FakeModuleArgumentSpecValidator, self).validate(parameters)

    class FakeAnsibleModule():
        def __init__(self, *args, **kwargs):
            self.params = {'name': 'bo', 'age': '42'}
            self.argument_spec = {
                'name': {'type': 'str'},
                'age': {'type': 'int'},
            }


# Generated at 2022-06-12 22:56:31.205108
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # Input parameters and output values
    argument_spec = {"foo": {"type": "bool"},
                     "bar": {"type": "int"}}
    parameters = {"foo": True, "bar": "foo"}
    module_arg_spec_validator = ModuleArgumentSpecValidator(argument_spec)
    result = module_arg_spec_validator.validate(parameters)
    assert {'foo': True, 'bar': None} == result.validated_parameters



# Generated at 2022-06-12 22:56:34.288622
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():
    argument_spec = {'name': {'type': 'str'}, 'age': {'type': 'int'}}
    validator = ArgumentSpecValidator(argument_spec, mutually_exclusive=[])
    return validator


# Generated at 2022-06-12 22:56:40.508361
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # Deprecation
    argument_spec = {
        'name': {'aliases': ['nickname']},
        'age': {'aliases': ['elderly']},
    }
    validator = ModuleArgumentSpecValidator(argument_spec)
    parameters = {'name': 'bo', 'age': '42'}
    result = validator.validate(parameters)
    assert result.validated_parameters == {'name': 'bo', 'age': '42'}
    assert result.error_messages == []
    assert len(result._deprecations) == 2
    assert result._deprecations[0]['name'] == 'nickname'
    assert result._deprecations[1]['name'] == 'elderly'

    # Warnings

# Generated at 2022-06-12 22:56:51.879919
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
        'languages': {'type': 'list'},
        'facts': {
            'type': 'dict',
            'options': {
                'first_name': {'type': 'str'},
                'last_name': {'type': 'str'},
                'birth_date': {'type': 'str'},
                'parents': {'type': 'list'},
            }
        },
    }


# Generated at 2022-06-12 22:57:01.088134
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():
    argument_spec={"attributes": {"type": "dict"}}
    mutually_exclusive = [['one', 'two']]
    required_together = [['one', 'two']]
    required_one_of = [['one', 'two']]
    required_if = [['one', 'two', ['three', 'four']]]
    required_by = {"one": ['two', 'three'], "four": ['two', 'five']}

    # test for creation with empty method
    assert ArgumentSpecValidator(argument_spec)
    # test for creation with non-empty method

# Generated at 2022-06-12 22:57:07.126210
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    """Test case for the method validate of class ArgumentSpecValidator
    """
    import warnings
    from ansible.module_utils.common.parameters import sanitize_keys
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int', 'required': True},
        'color': {'type': 'str'},
        'like': {'type': 'bool', 'default': False},
    }

    parameters = {
        'name': 'bo',
        'age': 42,
        'color': 'blue',
        'like': 'yes',
    }

    validator = ArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)
    assert result is not None
    assert set(result.validated_parameters.keys())

# Generated at 2022-06-12 22:57:17.081970
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():
    validator = ArgumentSpecValidator({
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    })

    # Test that defaults are populated correctly
    assert validator._mutually_exclusive is None
    assert validator._required_together is None
    assert validator._required_one_of is None
    assert validator._required_by is None
    assert validator._required_if is None
    assert validator._valid_parameter_names == {'age', 'name'}

    # Test that all arguments are populated correctly

# Generated at 2022-06-12 22:57:22.017929
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
        'aliased': {'type': 'str', 'aliases': ['aliased_alias']}
    }

    parameters = {
        'name': 'bo',
        'age': '42',
        'aliased': 'alice',
        'aliased_alias': 'bob'
    }

    validator = ModuleArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    print(result.error_messages)

# Generated at 2022-06-12 22:57:24.366470
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    _parameters = dict()
    _validator = ModuleArgumentSpecValidator(dict())
    _validator.validate(_parameters) == []

# Generated at 2022-06-12 22:57:32.142118
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    validator = ModuleArgumentSpecValidator(argument_spec={})
    parameters = {
        'name': 'bo',
        'age': '42',
    }
    param_result = validator.validate(parameters)

    assert param_result.validated_parameters == parameters
    assert param_result.errors == []

# Generated at 2022-06-12 22:57:41.556364
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    def check_validation_result(result, valid_parameters):
        assert hasattr(result, 'errors')
        assert hasattr(result, 'error_messages')
        assert hasattr(result, 'validated_parameters')
        assert isinstance(result.errors, AnsibleValidationErrorMultiple)
        assert isinstance(result.error_messages, list)
        assert result.validated_parameters == valid_parameters

    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }

    validator = ArgumentSpecValidator(argument_spec)

    # Intentionally leave out name
    params = {
        'age': '42',
    }

    result = validator.validate(params)
    assert result.error_messages

# Generated at 2022-06-12 22:57:49.892577
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    import pytest

    # Test empty spec returns without any errors
    mav = ModuleArgumentSpecValidator({})
    vr = mav.validate({})
    assert len(vr.error_messages) == 0

    # Test required parameter not present
    mav = ModuleArgumentSpecValidator({'param1': {'required': True, 'type': 'str'}})
    vr = mav.validate({})
    assert len(vr.error_messages) == 1
    assert isinstance(vr.errors[0], RequiredError)

    # Test required parameter present and valid
    mav = ModuleArgumentSpecValidator({'param1': {'required': True, 'type': 'str'}})
    vr = mav.validate({'param1': 'hello'})

# Generated at 2022-06-12 22:57:59.651616
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    pass
#    from ansible.module_utils.connection import Connection
#    from ansible.module_utils.six import iteritems
#    from ansible.module_utils.basic import AnsibleModule
#    from ansible.module_utils.common.network.config.utils import load_provider_arg_spec

    # The purpose of this test is to demonstrate a module using and defining
    # argument_spec. This test does not test all possible values. See
    # ansible.module_utils.common.parameters unit tests for that.
#    def test_parameters(module):
#        argument_spec = dict(
#            config=dict(type='str', required=False),
#            use_ssl=dict(type='bool', default=True),
#            validate_certs=dict(type='bool', default=True),
#           

# Generated at 2022-06-12 22:58:04.971882
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    """Unit test for method validate of class ArgumentSpecValidator"""
    from ansible.module_utils import basic

# Generated at 2022-06-12 22:58:12.259443
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }

    validator = ArgumentSpecValidator(argument_spec)

    parameters = {
        'name': 'bo',
        'age': '42',
    }

    result = validator.validate(parameters)
    valid_params = result.validated_parameters
    assert valid_params['age'] == 42
    errors = result.error_messages
    assert len(errors) == 0

# Generated at 2022-06-12 22:58:23.589382
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():

    mutually_exclusive = [['a', 'b'], ['a', 'c']]
    required_together = [['a', 'b']]
    required_one_of = [['a']]
    required_if = [[{'a': ['present']}, 'b']]
    required_by = {'a': ['b']}
    argument_spec = {
        'a': {'type': 'bool'},
        'b': {'type': 'str'},
        'c': {'type': 'int'},
    }

    parameters = {'a': True,
                  'b': 'test_b',
                  'c': 1,
                  }


# Generated at 2022-06-12 22:58:32.301365
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    '''
    Test ArgumentSpecValidator.validate
    '''
    import json
    import sys
    import tempfile
    import yaml

    # Load all the module argument specifications.
    list_directory = 'lib/ansible/modules/'
    module_names = [filename.rstrip('.py') for filename in os.listdir(list_directory)
                    if filename != '__init__.py']

    for module_name in module_names:
        module_path = os.path.join(list_directory, module_name) + '.py'
        module_arg_spec = {}

        with open(module_path, 'r') as f:
            module_text = f.read()

# Generated at 2022-06-12 22:58:38.269732
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    argument_spec = {
        'age': {
            'type': 'int',
            'required': True,
        },
        'name': {
            'type': 'str',
        },
    }

    mutually_exclusive = [
        ['age', 'name']
    ]

    required_one_of = [['age'], ['name']]

    required_if = [
        ['name', 42, ['age']]
    ]

    required_by = {
        'name': ['age']
    }

    parameters = {
        'age': '42',
        'name': 'bob',
        'fake': 12,
    }

    class TestResult:
        def __init__(self):
            self.warnings = []
            self.deprecations = []

    result = TestResult()

    validator

# Generated at 2022-06-12 22:58:48.609395
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    validator = ArgumentSpecValidator({
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    })

    parameters = {'name': b'cyrus', 'age': b'42'}
    result = validator.validate(parameters)

    assert not result.error_messages, "Got error_messages: {0}".format(result.error_messages)
    assert result.validated_parameters['name'] == 'cyrus', "Got name: {0}".format(result.validated_parameters['name'])
    assert result.validated_parameters['age'] == 42, "Got name: {0}".format(result.validated_parameters['age'])

# Generated at 2022-06-12 22:58:52.523820
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    validator = ArgumentSpecValidator({})
    result = validator.validate({})
    assert isinstance(result, ValidationResult)



# Generated at 2022-06-12 22:59:02.101262
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    from collections import OrderedDict
    spec_good = {
        'string': {'type': 'str', 'aliases': ['string_alias']},
        'integer': {'type': 'int', 'aliases': ['integer_alias']},
        'bool_no': {'type': 'bool', 'default': False},
        'bool_yes': {'type': 'bool', 'default': True},
        'dict': {'type': 'dict'},
        'list': {'type': 'list', 'aliases': ['list_alias']},
    }

    def check_spec(spec, parameters):
        validator = ArgumentSpecValidator(spec)
        result = validator.validate(parameters)
        assert isinstance(result, ValidationResult)

# Generated at 2022-06-12 22:59:13.074759
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    '''Tests ModuleArgumentSpecValidator.validate'''
    # Initialize ArgumentSpecValidator instance
    argument_spec = {
        'testvar': {
            'type': 'test_type'
        }
    }

    # Test ModuleArgumentSpecValidator instance 'validator'
    validator = ModuleArgumentSpecValidator(argument_spec)

    # Test support for alias deprecation
    alias_deprecation = dict(name="alias-d", version="2.14", date="2021-01-01")
    alias_warnings = []
    alias_deprecations = [alias_deprecation]

# Generated at 2022-06-12 22:59:20.666285
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    """Unit test for method validate of class ModuleArgumentSpecValidator."""
    argument_spec = {'name': {'type': 'str'}, 'my_list': {'type': 'list'}, 'my_dict': {'type': 'dict'}}
    validator = ModuleArgumentSpecValidator(argument_spec)
    parameters = {'name': 'bo', 'my_list': ["a", "b"], 'my_dict': {"a": 1}}
    result = validator.validate(parameters)

    assert result.validated_parameters == {'name': 'bo', 'my_list': ["a", "b"], 'my_dict': {"a": 1}}
    assert not result.error_messages

# Generated at 2022-06-12 22:59:31.593279
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():
    """Unit test for constructor of class ArgumentSpecValidator"""

    args = [
        {
            'type': 'str',
            'choices': ['client', 'server']
        },
        {
            'type': 'str',
            'choices': ['present', 'absent']
        }
    ]

    argument_spec = {
        'mode': {
            'type': 'str',
            'choices': ['client', 'server']
        },

        'state': {
            'type': 'str',
            'required': True,
            'choices': ['present', 'absent']
        },

        'name': {
            'type': 'str',
            'default': 'default_name'
        }
    }

    mutually_exclusive = [
        ['mode', 'name']
    ]

    required_

# Generated at 2022-06-12 22:59:36.305940
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    spec = ArgumentSpecValidator({'one': {'type': 'str'}, 'two': {'type': 'int'}, 'three': {'type': 'dict', 'default': {}}})

    assert isinstance(spec.validate({'one': 'foobar', 'two': 42}), ValidationResult)
    assert isinstance(spec.validate({'one': 'foobar', 'two': 1.2}), ValidationResult)
    assert isinstance(spec.validate({'one': 'foobar', 'two': '42'}), ValidationResult)
    assert isinstance(spec.validate({'one': 'foobar', 'two': 'not_a_number'}), ValidationResult)



# Generated at 2022-06-12 22:59:39.599029
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }
    validator = ArgumentSpecValidator(argument_spec)
    assert validator.argument_spec == argument_spec


# Generated at 2022-06-12 22:59:47.087856
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    argument_spec = {
        'name': {'type': 'str'}
    }
    parameters = {
        'name': 'bo'
    }
    validator = ArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)
    assert not result.errors, 'There should be no errors.'
    assert result.validated_parameters == parameters, 'The validated parameters should be the same as the parameters.'
    assert not result._deprecations, 'There should be no deprecations.'
    assert not result._warnings, 'There should be no warnings.'
    assert not result.unsupported_parameters, 'There should be no unsupported parameters.'

    result = validator.validate(parameters)
    assert not result.errors, 'There should be no errors.'

# Generated at 2022-06-12 22:59:56.535143
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    #  alias_warnings case 1
    module_argument_spec = {
        'name': {
            'type': 'str',
            'required': True
        },
        'age': {
            'type': 'int',
            'required': True
        },
        'state': {
            'type': 'str',
            'required': True,
            'aliases': ['status']
        },
    }

    parameters = {
        'name': 'bo',
        'age': 42,
        'status': 'present',
        'state': 'present'
    }

    validator = ModuleArgumentSpecValidator(module_argument_spec, [])
    result = validator.validate(parameters)

    #  alias_warnings case 2

# Generated at 2022-06-12 23:00:03.577630
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils.common.broken_pipe_error import BrokenPipeError
    from ansible.module_utils.common.collections import ImmutableDict

    class TestModule(object):
        argument_spec = {
            'blah': {'type': 'str'},
            'boom': {'type': 'int'},
        }

        mutually_exclusive = [
            ['blah', 'boom']
        ]

        required_together = [
            ['blah', 'boom']
        ]

        required_one_of = [
            ['blah', 'boom']
        ]

        required_if = [
            ['blah', 'blah', ['boom']]
        ]

        required_by = {
            'blah': ['boom']
        }


# Generated at 2022-06-12 23:00:17.016392
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():
    '''Test the __init__ method of class ArgumentSpecValidator'''
    argument_spec = dict(
        name=dict(
            type='str',
            required=True
        ),
        age=dict(
            type='int'
        ),
        pets=dict(
            type='list',
            elements='str')
    )
    mutually_exclusive = [['name', 'age']]
    required_one_of = [['name', 'age']]
    required_together = [['name', 'age']]
    required_if = [
        ['name', 'Joe', ['age', 'pets']],
        ['age', '42', ['name', 'pets']]
    ]
    required_by = dict(
        age=['name'],
        pets=['name', 'age']
    )
    valid

# Generated at 2022-06-12 23:00:24.424200
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    # Test 1
    # argument_spec = {"name": {"type": "str"}, "age": {"type": "int"}}
    # parameters = {"name": "bo", "age": "42"}
    # validator = ArgumentSpecValidator(argument_spec)
    # result = validator.validate(parameters)
    # assert result.error_messages == []
    # assert result.validated_parameters == {"name": "bo", "age": 42}
    # assert result.unsupported_parameters == set()
    # assert result._no_log_values == set()
    # assert result._deprecations == []
    # assert result._warnings == []
    pass



# Generated at 2022-06-12 23:00:28.885219
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():

    data = {
        'argument_spec': {
            'name': {'type': 'str'},
        },
        'parameters': {
            'name': 'bo',
        },
    }

    validator = ModuleArgumentSpecValidator(data['argument_spec'])
    validator.validate(data['parameters'])

# Generated at 2022-06-12 23:00:35.828906
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }

    parameters = {
        'name': 'bo',
        'age': '42',
    }

    validator = ArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    assert not result.errors
    assert result.validated_parameters == {'name': 'bo', 'age': 42}

# Generated at 2022-06-12 23:00:43.895696
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():

    def test_validator(validator, parameters, result_attrs):
        result = validator.validate(parameters)

        assert result.errors == result_attrs['errors']
        assert result.validated_parameters == result_attrs['validated_parameters']

    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }

    parameters = {
        'name': 'bo',
        'age': '42',
    }

    validator = ArgumentSpecValidator(argument_spec)
    test_validator(validator, parameters, {
        'errors': [],
        'validated_parameters': {'name': 'bo', 'age': 42},
    })


# Generated at 2022-06-12 23:00:55.432928
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils.basic import AnsibleModule

# Generated at 2022-06-12 23:00:59.756847
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    argument_spec = {
            'name': {
                'type': 'str',
                'default': 'default_name',
                'required': False
            }
        }

    validator = ArgumentSpecValidator(argument_spec)
    parameters = {'name': 'bo'}
    result = validator.validate(parameters)
    assert not result.errors
    assert result.validated_parameters == {'name': 'bo'}
    assert result.error_messages == []

    parameters = {}
    result = validator.validate(parameters)
    assert not result.errors
    assert result.validated_parameters == {'name': 'default_name'}
    assert result.error_messages == []



# Generated at 2022-06-12 23:01:08.449474
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    """The method ModuleArgumentSpecValidator.validate takes a dict named parameters and return the validation result.
    This method verify if the given parameters is None and validate the given parameters using ArgumentSpecValidator.validate.
    """
    # Create a dict with params to pass to the function under test
    parameters = {}

    # Create a mock instance of AnsibleModule without any arguments
    mocked_AnsibleModule = MagicMock()
    mocked_AnsibleModule.params = parameters

    # Create a mock instance of ArgumentSpecValidator without any arguments
    mocked_ArgumentSpecValidator = MagicMock(return_value=parameters)
    mocked_ArgumentSpecValidator.validate = MagicMock(return_value=parameters)

    # Create a mock instance of ModuleArgumentSpecValidator with arguments
    mock_ModuleArgumentSpecValidator = Module

# Generated at 2022-06-12 23:01:18.630416
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # expecting the deprecations to be shown in the output, i.e the test is passed
    def deprecate(msg, **kwargs):
        print(msg)
        print(kwargs)

    # expecting the warnings to be shown in the output, i.e the test is passed
    def warn(msg):
        print(msg)

    # arguments for the test
    argument_spec = {
        'name_1': {'type': 'str'},
        'name_2': {'type': 'int', 'aliases': ['name_2_alias']},
    }
    mutually_exclusive = None
    required_together = None
    required_one_of = None
    required_if = None
    required_by = None


# Generated at 2022-06-12 23:01:29.427514
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():
    '''
    Unit test for constructor of class ArgumentSpecValidator
    '''
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }

    # We will now test different variations of mutually exclusive case
    mutually_exclusive = [
        ['name', 'age'],
        [['name', 'age']]
    ]
    for mutually_exclusive_val in mutually_exclusive:
        validator = ArgumentSpecValidator(argument_spec, mutually_exclusive=mutually_exclusive_val)
        parameters = {
            'name': 'bo',
            'age': '42',
        }
        result = validator.validate(parameters)
        assert result.error_messages == [
            "Parameters 'name' and 'age' are mutually exclusive."]

# Generated at 2022-06-12 23:01:46.363077
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }

    mutually_exclusive = ['name', 'age']
    required_together = [['name', 'age']]
    required_one_of = [['name', 'age']]
    required_if = [('name', 'age', ['age'])]
    required_by = {'name': ['age']}

    validator = ArgumentSpecValidator(argument_spec,
                                      mutually_exclusive=mutually_exclusive,
                                      required_together=required_together,
                                      required_one_of=required_one_of,
                                      required_if=required_if,
                                      required_by=required_by)

    assert validator._mutually_exclusive == mutually_exclusive
   

# Generated at 2022-06-12 23:01:52.261598
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }

    parameters = {
        'name': 'bo',
        'age': '42',
    }
    results = {}

    validator = ModuleArgumentSpecValidator(argument_spec)
    results = validator.validate(parameters)

    # results
    assert results.validated_parameters['name'] is 'bo'
    assert results.validated_parameters['age'] is 42

# Generated at 2022-06-12 23:01:58.276365
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }

    parameters = {
        'name': 'bo',
        'age': '42',
    }

    validator = ArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)
    assert len(result.errors) == 0
    assert result.validated_parameters['age'] == 42
    assert result.unsupported_parameters == set()

# Generated at 2022-06-12 23:02:01.267291
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    """
    Unit test for method validate of class ModuleArgumentSpecValidator
    """
    assert hasattr(ModuleArgumentSpecValidator, "validate")
    validator = ModuleArgumentSpecValidator({})
    assert  callable(validator.validate)

# Generated at 2022-06-12 23:02:11.754876
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    """Unit test for method validate of class ModuleArgumentSpecValidator."""


# Generated at 2022-06-12 23:02:23.013501
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    argument_spec = {
        'param_a': {
            'type': 'str',
            'default': False,
            'aliases': ['param_b']},
        'param_c': {
            'type': 'list',
            'aliases': ['param_d'],
            },
        'param_e': {
            'type': 'str',
            'default': 'a'
            }
    }
    mutually_exclusive = [ ['param_a'], ['param_c', 'param_e']]
    validator = ModuleArgumentSpecValidator(argument_spec, mutually_exclusive=mutually_exclusive)
    param_a = 'param_a'
    param_b = 'param_b'
    param_c = 'param_c'
    param_d = 'param_d'
    param_

# Generated at 2022-06-12 23:02:25.087172
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    argument_spec = {'foo': {'type': 'str', 'aliases': ['bar']}}
    parameter = {'foo': 'baz'}
    result = ModuleArgumentSpecValidator(argument_spec).validate(parameter)
    assert result.validated_parameters['foo'] == 'baz'

# Generated at 2022-06-12 23:02:34.541439
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils.common.parameters import check_mutually_exclusive
    from ansible.module_utils.common.validation import check_required_arguments
    from ansible.module_utils.common.warnings import deprecate, warn

    argument_spec = {
        'age': {'type': 'int'},
    }

    parameters = {
        'age': '42',
    }

    # Test without deprecation
    validator = ModuleArgumentSpecValidator(argument_spec)
    check_mutually_exclusive.side_effect = None
    check_required_arguments.side_effect = None
    deprecate.side_effect = None
    warn.side_effect = None
    result = validator.validate(parameters)


# Generated at 2022-06-12 23:02:45.177185
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # Create and initialize an object of class ModuleArgumentSpecValidator
    argument_spec = {
        'name': {'type': 'str', 'aliases': ['username']}
    }
    mutually_exclusive = []
    required_together = []
    required_one_of = []
    required_if = []
    required_by = []
    validator = ModuleArgumentSpecValidator(argument_spec,
                                            mutually_exclusive=mutually_exclusive,
                                            required_together=required_together,
                                            required_one_of=required_one_of,
                                            required_if=required_if,
                                            required_by=required_by)

    parameters = {'name': 'bo'}
    result = validator.validate(parameters)
    assert result.error_messages == []

# Generated at 2022-06-12 23:02:53.504411
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    validate = ModuleArgumentSpecValidator.validate

    def assert_validation(spec, parameters, **kwargs):
        v = ModuleArgumentSpecValidator(spec, **kwargs)
        result = v.validate(parameters)
        assert result.error_messages == []
        return result

    # Test the validation of a value which is the default value of a parameter
    # with a type which is bool.
    assert_validation(
        spec={
            'parameter_with_default_value': {
                'type': 'bool',
                'default': True
            }
        },
        parameters={
            'parameter_with_default_value': True,
        })

    # Test the validation of a value of an unsupported parameter

# Generated at 2022-06-12 23:03:14.492115
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():

    # Remove name from this variable and move to test_data.
    # Uncomment the code after creating the test data file.
    parameters = {
        'name': 'name',
        'aliases': 'a',
        'default': 'default',
        'fallback': 0,
        'fallback_values': ['default'],
        'options': ['value'],
        'required': False,
        'no_log': False,
        'type': 'type',
        'mutually_exclusive': ['value'],
        'required_together': ['value'],
        'required_one_of': ['value'],
        'required_if': ['value'],
        'required_by': ['value'],
    }

    # Remove argument_spec from this variable and move to test_data.
    # Uncomment the code after creating the

# Generated at 2022-06-12 23:03:23.389970
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # Test normal case
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }
    parameters = {
        'name': 'bo',
        'age': 42,
    }
    validator = ModuleArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    assert result.validated_parameters == parameters

    # Test error case
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int', 'required': True},
    }
    parameters = {
        'name': 'bo',
    }
    validator = ModuleArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)


# Generated at 2022-06-12 23:03:31.250592
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }

    parameters = {
        'name': 'bo',
        'age': '42',
    }

    validator = ArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)


# Generated at 2022-06-12 23:03:37.188026
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    """
    ansible.module_utils.common.arg_spec.ModuleArgumentSpecValidator.validate()
    works correctly when there are no deprecations, warnings or errors
    """
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }

    parameters = {
        'name': 'bo',
        'age': 42,
    }

    validator = ModuleArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    assert result.error_messages == []
    assert result.validated_parameters == parameters

# Generated at 2022-06-12 23:03:38.137943
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    pass



# Generated at 2022-06-12 23:03:40.930550
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    #is a ModuleArgumentSpecValidator object
    m = ModuleArgumentSpecValidator(dict())
    m.validate(dict())


# Generated at 2022-06-12 23:03:50.667743
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # validator for class ModuleArgumentSpecValidator used for unit test
    validator = ModuleArgumentSpecValidator({'param': {'type': 'str'}}, required_together=[['param']])
    # result for unit test
    result = validator.validate({'param': 'a'})
    assert len(result.errors) == 0
    result = validator.validate({'param': 1})
    assert len(result.errors) != 0
    result = validator.validate({'param': None})
    assert len(result.errors) != 0
    result = validator.validate({'param': False})
    assert len(result.errors) != 0
    result = validator.validate({})
    assert len(result.errors) != 0
    result = validator.validate(None)

# Generated at 2022-06-12 23:03:57.267507
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    arg_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }

    parameters = {
        'name': 'bo',
        'age': '42',
    }

    validator = ArgumentSpecValidator(argument_spec=arg_spec)
    result = validator.validate(parameters)

    assert not result.errors

    assert result.validated_parameters == {
        'name': 'bo',
        'age': 42,
    }

    assert result.unsupported_parameters == set()

# Generated at 2022-06-12 23:04:05.879141
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    argument_spec = {
        "name": {
            "type": "str",
        },
        "age": {
            "type": "int",
            "aliases": ["old"],
        }
    }

    parameters = {
        "name": "bo",
        "age": "42",
    }

    validator = ArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    assert result.validated_parameters == {
        "name": "bo",
        "age": 42,
    }
    assert not result.error_messages

# Generated at 2022-06-12 23:04:14.993286
# Unit test for method validate of class ArgumentSpecValidator

# Generated at 2022-06-12 23:04:41.894125
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }

    parameters = {
        'name': 'bo',
        'age': '42',
    }

    validator = ArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    if result.error_messages:
        sys.exit("Validation failed: {0}".format(", ".join(result.error_messages)))

    valid_params = result.validated_parameters

# Generated at 2022-06-12 23:04:42.371345
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    pass

# Generated at 2022-06-12 23:04:50.204405
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # GIVEN
    argument_spec = {'key': {'type': 'str'}}
    mutually_exclusive = None
    required_together = None
    required_one_of = None
    required_if = None
    required_by = None
    validator = ModuleArgumentSpecValidator(argument_spec, mutually_exclusive, required_together, required_one_of, required_if, required_by)
    parameters = {'key': 'value'}
    # WHEN
    result = validator.validate(parameters)
    # THEN
    assert result.validated_parameters == {'key': 'value'}
    assert not result.error_messages
    assert result.unsupported_parameters == set()
    assert result._warnings == []
    assert result._deprecations == []

# Generated at 2022-06-12 23:04:57.613608
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    import sys

    argument_spec = {'name': {'type': 'str'},
                     'age': {'type': 'int'}}

    parameters = {'name': 'bo',
                  'age': '42'}

    validator = ArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    if result.error_messages:
        sys.exit("Validation failed: {0}".format(", ".join(result.error_messages)))

    valid_params = result.validated_parameters

    print("name: {0}".format(valid_params['name']))
    print("age: {0}".format(valid_params['age']))

# Generated at 2022-06-12 23:05:08.371578
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    test_params = {'key1': "value1", 'key2': "value2"}
    test_params_deprecated = {'key1': "value1", 'key2': "value2", 'deprecated_key': "value"}

    test_mock_args = [
        {'mutually_exclusive': [{'key1', 'key2'}], 'required_together': [['key1', 'key2']]},
        {'required_one_of': [['key1', 'key2']]},
        {'required_if': [['key1', "value1", ['key2']]]},
        {'required_by': {'key1': ['key2']}},
        {'deprecated_key': {'aliases': ['key1']}},
    ]
    validation_result = ModuleArg

# Generated at 2022-06-12 23:05:14.053898
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    argument_spec = {'all': {'type': 'bool', 'default': None}, 'all_type': {'type': 'bool', 'default': False}}
    parameters = {'all': True, 'all_type': 'True'}
    validator = ArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)
    assert result.validated_parameters['all'] == True
    assert result.validated_parameters['all_type'] == True
    assert result.errors == []

# Generated at 2022-06-12 23:05:23.088036
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    """Unit test for method validate of class ModuleArgumentSpecValidator"""
    # First parameter is argument_spec, which is dict type
    # It is required, therefore, test both None and valid values
    argument_spec = {'argument_spec': {'type': 'dict'}}
    validator_None = ModuleArgumentSpecValidator(None)
    validator_argument_spec = ModuleArgumentSpecValidator(argument_spec)
    # Second parameters are optional, can be None
    validator_None2 = ModuleArgumentSpecValidator(argument_spec, None, None, None, None, None)
    validator_allNone = ModuleArgumentSpecValidator(None, None, None, None, None, None)
    validator_allNonNone = ModuleArgumentSpecValidator(argument_spec, [], [], [], [], {})


# Generated at 2022-06-12 23:05:27.849244
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils.common.parameters import _AnsibleModule
    test_module = _AnsibleModule(argument_spec={})
    validator = ModuleArgumentSpecValidator(argument_spec={})
    result = validator.validate({})
    assert isinstance(result, ValidationResult)

# Generated at 2022-06-12 23:05:37.638587
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    from ansible.module_utils.common.parameters import ArgumentSpec
    from ansible.module_utils.common.arg_spec import ArgumentSpecValidator
    from ansible.module_utils.common.text.converters import to_text

    spec = ArgumentSpec()
    spec.params = {
        'name': dict(type='str', default='bo'),
        'age': dict(type='int', default='42'),
    }

    validator = ArgumentSpecValidator(spec)

    # test the validation with valid parameters
    parameters = dict(name='bo', age=42)
    result = validator.validate(parameters)
    assert result.errors == []
    assert result.validated_parameters == dict(name='bo', age=42)

    # test the validation with invalid parameters

# Generated at 2022-06-12 23:05:42.667004
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    spec = {'name': {'type': 'str'}, 'age': {'type': 'int'}}
    parameters = {'name': 'bo', 'age': '42'}
    validator = ArgumentSpecValidator(spec)
    result = validator.validate(parameters)
    assert result.validated_parameters == {'name': 'bo', 'age': 42}

