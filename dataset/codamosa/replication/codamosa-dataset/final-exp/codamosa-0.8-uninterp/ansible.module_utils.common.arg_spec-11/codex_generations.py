

# Generated at 2022-06-12 22:56:14.375963
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    import pytest
    # Instance of class ModuleArgumentSpecValidator
    instance = ModuleArgumentSpecValidator(arguments)
    # Test validate method.
    assert result == instance.validate(parameters)


# Generated at 2022-06-12 22:56:14.986310
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    assert True

# Generated at 2022-06-12 22:56:25.468651
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():
    import pytest

    # validator with no validation options
    argument_spec1 = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }
    validator1 = ArgumentSpecValidator(argument_spec1)

    assert validator1.argument_spec == argument_spec1

    # validator with all validation options
    mutually_exclusive = ['a', ['b', 'c']]
    required_together = [['d', 'e']]
    required_one_of = [['f', 'g']]
    required_by = {
        'h': ['i', 'j'],
    }
    required_if = ['k', 'l', 'm']


# Generated at 2022-06-12 22:56:30.068382
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    # test for empty parameters 
    argument_spec = {
        "name": {'type': 'str'}, 
        "age": {'type': 'int'}
    }
    parameters = {}
    
    validator = ArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)
    assert(result.error_messages == ["The following fields are required: name, age"])
    
    # test for one required field exist
    argument_spec = {
        "name": {'type': 'str'}, 
        "age": {'type': 'int'}
    }
    parameters = {
        "name": "bo"
    }
    
    validator = ArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

# Generated at 2022-06-12 22:56:30.720878
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    assert False

# Generated at 2022-06-12 22:56:38.634250
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # Parameter 'names' is deprecated and has a default
    argument_spec = {
        'names': {
            'type': 'list',
            'aliases': ['name'],
            'deprecated': {
                'alternative': 'deprecated_names',
                'why': 'For the common case of a list of names.',
            },
            'default': [],
        },
        'deprecated_names': {
            'type': 'list',
            'default': [],
        },
    }

    # The module docstring below is parsed by AnsibleModule to set
    # documentation specific to each argument.
    """
    :deprecated: alternative='deprecated_names' why='For the common case of a list of names.'
    """

    # Parameter 'name' is deprecated

# Generated at 2022-06-12 22:56:49.471181
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    import ansible.module_utils.common.arg_spec as arg_spec
    argument_spec = {
        "name": {"type": str},
        "age": {"type": int},
        "message": {"type": str, "aliases": ["msg"]},
        "new_alias": {"type": str, "aliases": ["old_alias"]},
        "address": {
            "type": "dict",
            "options": {
                "city": {"type": str, "aliases": ["town"]},
                "state": {"type": str, "aliases": ["county"]},
            },
        },
    }


# Generated at 2022-06-12 22:56:58.914291
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }
    mutually_exclusive = [
        ['name', 'age'],
    ]
    parameters = {
        'name': 'bo',
        'age': '42',
    }
    validator = ModuleArgumentSpecValidator(argument_spec, mutually_exclusive=mutually_exclusive)
    result = validator.validate(parameters)
    assert result.error_messages == ["The parameter 'name' is mutually exclusive with the parameter 'age'. All of them cannot be used together."]
    assert result.validated_parameters == {'name': 'bo', 'age': '42'}

# Generated at 2022-06-12 22:57:09.147847
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():

    """
    Tests to validate parameter types and if they are optional or not.
    Checks for the exceptions like alias error,no-log error,required-default-error etc.
    """

    validator = ArgumentSpecValidator(argument_spec = {'name': {'type': 'str'},
                                                       'age': {'type': 'int'},
                                                       'aliases': {'type': 'list'}
                                                      })

    parameters = {'name': 'bo',
                  'age': '42',
                  'aliases': ['bo', 'name']
                 }

    result = validator.validate(parameters)
    assert result.errors.messages == ['Invalid alias in argument "aliases". It has an invalid key: "name".']


# Generated at 2022-06-12 22:57:16.713187
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    test_arg_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'}
    }
    test_params = {'name': 'bo', 'age': 42}
    validator = ModuleArgumentSpecValidator(test_arg_spec)
    result = validator.validate(test_params)
    assert result.validated_parameters == test_params

    test_params = {'name': 'bo', 'age': 42, 'state': 'present'}
    result = validator.validate(test_params)
    assert result.error_messages == ['Invalid parameters: state']

# Generated at 2022-06-12 22:57:22.005842
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # TODO: test_ModuleArgumentSpecValidator_validate
    pass

# Generated at 2022-06-12 22:57:30.699743
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }
    parameters = {
        'name': 'bo'
    }
    mutually_exclusive = None
    required_together = None
    required_one_of = None
    required_if = None
    required_by = None
    validator = ArgumentSpecValidator(argument_spec, mutually_exclusive, required_together, required_one_of, required_if, required_by)
    result = validator.validate(parameters)
    if not result.error_messages:
        assert False


# Generated at 2022-06-12 22:57:33.243917
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # Initialize `result`
    result = None

    # ModuleArgumentSpecValidator cannot be used outside of AnsibleModule
    # `result` should be None
    assert result == None

# Generated at 2022-06-12 22:57:38.766188
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    argument_spec ={
    'name': {'type': 'str'},
    'age': {'type': 'int'},
    }

    parameters = {
        'name': 'bo',
        'age': '42',
    }

    validator = ArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)
    assert result.validated_parameters == {'name': 'bo', 'age': 42}

# Generated at 2022-06-12 22:57:43.840929
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    """ArgumentSpecValidator.validate should return a ValidationResult"""
    spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }

    params = {
        'name': 'bo',
        'age': '42',
    }

    validator = ArgumentSpecValidator(spec)
    result = validator.validate(params)

    assert isinstance(result, ValidationResult)



# Generated at 2022-06-12 22:57:50.991216
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    def mock_super_validate(self, parameters):
        result = ValidationResult(parameters)
        result._deprecations.append({'name': 'foo', 'version': '2.5'})
        result._warnings.append({'option': 'name', 'alias': 'name'})
        return result

    test_obj = ModuleArgumentSpecValidator()
    validator_mock = ModuleArgumentSpecValidator
    validator_mock.validate = mock_super_validate
    result = test_obj.validate({})
    assert result._warnings[0]['option'] == 'name'
    assert result._warnings[0]['alias'] == 'name'

# Generated at 2022-06-12 22:58:00.979593
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # Set up ArgumentSpecValidator
    argument_spec = {'foo': {'type': 'int'}}
    mutually_exclusive = [['foo', 'bar']]
    validator = ModuleArgumentSpecValidator(
        argument_spec=argument_spec,
        mutually_exclusive=mutually_exclusive,
        required_together=None,
        required_one_of=None,
        required_if=None,
        required_by=None,
    )

    # Test validation with mutually exclusive but no conflicting parameters
    parameters = {'foo': 1}
    result = validator.validate(parameters)
    assert 'error_messages' not in result
    assert result['validated_parameters'] == parameters

    # Test validation with mutually exclusive and conflicting parameters
    parameters = {'foo': 1, 'bar': 2}
    result

# Generated at 2022-06-12 22:58:02.667034
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils.common.parameters import get_empty_argspec
    assert ModuleArgumentSpecValidator(get_empty_argspec()).validate({})

# Generated at 2022-06-12 22:58:12.925794
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    """Unit test for method validate of class ModuleArgumentSpecValidator"""
    import tempfile
    import traceback

    fd, tmp_path = tempfile.mkstemp()

# Generated at 2022-06-12 22:58:24.297637
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils.network.common.utils import dict_merge
    from ansible.module_utils.network.common.config import NetworkConfig
    argument_spec = {
        'name': {'type': 'str', 'required': True},
        'age': {'type': 'int', 'default': 42},
    }
    parameters = {
        'name': 'bo',
        'age': '42',
    }
    validator = ArgumentSpecValidator(argument_spec)
    result_validator = validator.validate(parameters)
    result_module = ModuleArgumentSpecValidator(argument_spec).validate(parameters)
    assert result_module._deprecations == result_validator._deprecations
    assert result_module._warnings == result_validator._warnings
    assert result_

# Generated at 2022-06-12 22:58:30.800173
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    v = ModuleArgumentSpecValidator({})
    result = v.validate({})

    assert isinstance(result, ValidationResult)
    assert isinstance(result.error_messages, list)
    assert isinstance(result.validated_parameters, dict)

# Generated at 2022-06-12 22:58:37.124434
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    """ test class ArgumentSpecValidator validate method
    """
    argument_spec = {
        'a': {'type': 'str'},
        'b': {'type': 'int'},
        'c': {'type': 'dict', 'options': {
            'd': {'type': 'str'},
            'e': {'type': 'list', 'elements': 'str'}
        }},
        'f': {'type': 'list', 'elements': 'dict', 'options': {
            'g': {'type': 'bool'}
        }},
        'h': {'type': 'int', 'required': False}
    }

# Generated at 2022-06-12 22:58:48.208276
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    class TestModuleArgumentSpecValidator(ModuleArgumentSpecValidator):
        def __init__(self, *args, **kwargs):
            super(TestModuleArgumentSpecValidator, self).__init__(*args, **kwargs)
            self._warnings = [{'alias': 'a', 'option': 'x'}]
            self._deprecations = [{'name': 'b'}]

    class TestAnsibleModule:
        def __init__(self):
            self.warnings = []
            self.deprecations = []

    class MockWarnings:
        def warn(self, msg):
            self.msg = msg

    class MockDeprecate:
        def deprecate(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs



# Generated at 2022-06-12 22:58:56.620505
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_text
    from ansible.module_utils.basic import AnsibleModule

    argument_spec = dict(
        state=dict(type='str', default='present', choices=['present', 'absent']),
        mode=dict(type='str', default='0644'),
        src=dict(type='str'),
        dest=dict(type='str', required=True, aliases=['name']),
        required_if=dict(type='str'),
    )

    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=True)

    parameters = module.params
    validator = ArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    # No Val

# Generated at 2022-06-12 22:59:08.960242
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    argument_spec = {
        'name': {'type': 'str', 'aliases': ['bar']},
        'age': {'type': 'int'},
    }

    mutually_exclusive = [
        ['name', 'age'],
    ]

    required_if = [
        ['name', 'present', ['age']],
    ]

    validator = ModuleArgumentSpecValidator(argument_spec,
                                            mutually_exclusive=mutually_exclusive,
                                            required_if=required_if,
                                            )

    parameters = {
        'name': 'bo',
        'age': '42',
    }

    result = validator.validate(parameters)

    errors = []
    for error in result.errors:
        errors.append(error.message)


# Generated at 2022-06-12 22:59:17.328339
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    # unit test for ansible.module_utils.common.arg_spec.ArgumentSpecValidator.validate()
    from ansible.module_utils.common.arg_spec import ArgumentSpecValidator
    from ansible.module_utils.common.warnings import deprecate, warn
    import os
    import sys

    class ArgumentValidationErrorMock:
        def __init__(self):
            self.message = "AnsibleValidationError : {0}"
            self.num = 0
            self.warning_num = 0

        def append(self, e):
            self.num += 1
            print(
                "Validation: {0}. This test case is expected to fail".format(self.message.format(e)),
                file=sys.stderr)


# Generated at 2022-06-12 22:59:19.870380
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    validator = ModuleArgumentSpecValidator({})
    parameters = {}
    result = validator.validate(parameters)
    assert isinstance(result, ValidationResult)



# Generated at 2022-06-12 22:59:30.903000
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # arguments used for instantiation of ArgumentSpecValidator
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }

    mutually_exclusive = None
    required_together = None
    required_one_of = None
    required_if = None
    required_by = None
    # arguments used for parameter each of method validate
    parameters = {
        'name': 'bo',
        'age': '42',
    }

    # expected values
    expected_messages = []
    expected_validated_parameters = {
        'name': 'bo',
        'age': 42,
    }


# Generated at 2022-06-12 22:59:37.712121
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

    assert(result.validated_parameters['name'] == 'bo')
    assert(result.validated_parameters['age'] == 42)
    assert(len(result.errors) == 0)

# Generated at 2022-06-12 22:59:44.755676
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }

    mutually_exclusive = [["name", "age"]]
    required_together = [["name"], ["age"]]
    required_one_of = [["name"], ["age"]]
    required_if = [["name", "bo", ["name"]]]
    required_by = {'name': ['name']}

    validator = ArgumentSpecValidator(argument_spec, mutually_exclusive=mutually_exclusive, required_together=required_together,
                                      required_one_of=required_one_of, required_if=required_if, required_by=required_by)
    assert validator is not None

# Generated at 2022-06-12 22:59:57.888093
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.common.warnings import DeprecationWarning

    class MockValidator(ModuleArgumentSpecValidator):
        def __init__(self, *args, **kwargs):
            super(MockValidator, self).__init__(*args, **kwargs)

    # Ensure we get a DeprecationWarning
    validator = MockValidator(argument_spec={
        'a': {'type': 'str', 'aliases': ['p', 'x', 'y', 'z']},
    }, required_by={'a': ['p']})

    result = validator.validate({'a': 'valid'})
    assert result.errors == []
    assert result.validated_parameters == {'a': 'valid'}

# Generated at 2022-06-12 23:00:07.377630
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    import json

    parameter_spec = {
        "name": {
            "type": "str",
            "required": True
        },
        "age": {
            "type": "int",
            "required": True,
        },
        "password": {
            "type": "str",
            "no_log": True,
            "required": True,
        },
        "facts": {
            "type": "dict",
            "options": {
                "pen": {
                    "type": "str",
                },
                "book": {
                    "type": "str",
                },
                "paper": {
                    "type": "str",
                },
            },
            "aliases": ["tools"],
        },
    }


# Generated at 2022-06-12 23:00:17.885574
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int', 'required': True},
        'gender': {'type': 'str', 'default': 'male'},
        'address': {'type': 'dict', 'options': {
            'street_name': {'type': 'str'},
            'zipcode': {'type': 'int'}
        }}
    }

    parameters = {
        'name': 'bo',
        'address': {'street_name': 'Baker Street', 'zipcode': 110},
        'age': '42'
    }

    validator = ArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    assert(result.validated_parameters['name'] == 'bo')
   

# Generated at 2022-06-12 23:00:25.965996
# Unit test for method validate of class ModuleArgumentSpecValidator

# Generated at 2022-06-12 23:00:26.864628
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    pass


# Generated at 2022-06-12 23:00:32.958724
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

    if result.errors:
        raise result.errors

# Generated at 2022-06-12 23:00:42.339368
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    mutually_exclusive = [
        ['option1', 'option2'],
        ['option3', 'option4'],
        ['option5', 'option6', 'option7'],
    ]
    required_one_of = [
        ['option1', 'option2'],
        ['option3', 'option4', 'option5'],
    ]
    required_if = [
        ['option1', 'option2', 'option5'],
        ['option3', 'option4', 'option6'],
    ]
    required_by = {
        'option2': ['option1'],
        'option4': ['option3'],
    }


# Generated at 2022-06-12 23:00:53.566228
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils.common.arg_spec import ModuleArgumentSpecValidator

    assert_set_equal = set.__eq__

    ##############################################################################
    # prepare

# Generated at 2022-06-12 23:00:56.002713
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    argument_spec = {}
    validator = ModuleArgumentSpecValidator(argument_spec)
    validator.validate({})

# Generated at 2022-06-12 23:01:06.052632
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():

    import pytest

    # Test 1
    def test_1():
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

        assert not result.error_messages
        assert result.validated_parameters['name'] == 'bo'
        assert result.validated_parameters['age'] == 42

    test_1()

    # Test 2
    def test_2():
        argument_spec = {
            'name': {'type': 'str'},
            'age': {'type': 'int'},
        }

# Generated at 2022-06-12 23:01:20.430228
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

    assert result.errors == []
    assert result.validated_parameters == {
        'name': 'bo',
        'age': 42,
    }

# Generated at 2022-06-12 23:01:21.500498
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():

    assert False, "NOT WRITTEN"

# Generated at 2022-06-12 23:01:31.940560
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    """
    Validate method for class ModuleArgumentSpecValidator.
    """
    expected_result = {'name': 'bo', 'age': 42}
    # pylint: disable=unused-variable
    # pylint: disable=bare-except
    # pylint: disable=expression-not-assigned
    # pylint: disable=try-except-raise

    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }

    # Success cases
    parameters = {'name': 'bo', 'age': '42'}
    validator = ModuleArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)
    assert result.validated_parameters == expected_result

    # Error cases


# Generated at 2022-06-12 23:01:36.824234
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    import unittest

    class TestValidation(unittest.TestCase):
        def test_validate(self):
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

            assert not result.error_messages

            self.result_validated_parameters = result.validated_parameters
            self.result_no_log_values = result.no_log_values
            self.result_unsupported_parameters = result.unsupported_parameters
            self.result_errors = result.errors


# Generated at 2022-06-12 23:01:41.522321
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    ModuleArgumentSpecValidator(argument_spec={}).validate({'a': 'alias', 'b': None})

    ModuleArgumentSpecValidator(argument_spec={}).validate({'a': 'alias'})

    # Test in case the validated_parameters is empty
    ModuleArgumentSpecValidator(argument_spec={}).validate({})

# Generated at 2022-06-12 23:01:47.601058
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    # test_ArgumentSpecValidator_validate():
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

    assert result.validated_parameters['name'] == 'bo'
    assert result.validated_parameters['age'] == 42

    assert not result.error_messages

# Generated at 2022-06-12 23:01:56.857148
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    """Unit tests for argument specification validation"""

    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }

    # Simple validation
    parameters = {
        'name': 'bo',
        'age': '42',
    }

    validator = ArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)
    assert parameters['age'] == '42'
    assert result.validated_parameters['age'] == 42

    # Validation of nested parameters

# Generated at 2022-06-12 23:02:05.019686
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils.basic import AnsibleModule

    # ArgumentSpecValidator.validate is called by AnsibleModule.validate_parameters
    # test calling AnsibleModule.validate_parameters here to test
    # ArgumentSpecValidator.validate
    def test_AnsibleModule_validate_parameters(self):
        result = super(AnsibleModule, self).validate_parameters(params=self._params)
        return result

    # test argument spec
    # {'type': 'string'} is the default

# Generated at 2022-06-12 23:02:05.620336
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    pass

# Generated at 2022-06-12 23:02:10.451249
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    """Unit test for method validate of class ModuleArgumentSpecValidator"""
    validator = ModuleArgumentSpecValidator({
        'a': {'type': 'str'},
        'b': {'type': 'str'},
    })

    result = validator.validate({'a': 'test'})

    assert not result.errors

# Generated at 2022-06-12 23:02:45.526764
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

    assert result.validated_parameters == {'name': 'bo', 'age': 42}
    assert result.error_messages == []
    assert result.unsupported_parameters == set()



# Generated at 2022-06-12 23:02:53.714917
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():

    from ansible.module_utils.common.warnings import _module_warnings

    class TestModuleArgumentSpecValidator(ModuleArgumentSpecValidator):
        def __init__(self, argument_spec, mutually_exclusive=None, required_together=None, required_one_of=None, required_if=None, required_by=None):
            super(TestModuleArgumentSpecValidator, self). __init__(argument_spec, mutually_exclusive=mutually_exclusive, required_together=required_together,
                                                                  required_one_of=required_one_of, required_if=required_if, required_by=required_by)
        def validate(self, parameters, *args, **kwargs):
            return super(TestModuleArgumentSpecValidator, self). validate(parameters, *args, **kwargs)

   

# Generated at 2022-06-12 23:03:02.117175
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    # Create example argument_spec
    argument_spec = {
        'name': {'type': 'str', 'default': 'bo'},
        'age': {'type': 'int', 'default': 42},
    }

    # Create example parameters
    parameters = {
        'name': 'bo',
        'age': '42',
    }

    # Create new ArgumentSpecValidator
    validator = ArgumentSpecValidator(argument_spec)

    # Parameter validation
    result = validator.validate(parameters)
    assert result.validated_parameters == {
        'name': 'bo',
        'age': 42,
    }



# Generated at 2022-06-12 23:03:07.805254
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():

    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int', 'default': 42, 'required': True},
    }

    parameters = {
        'name': 'bo',
        'age': '42',
    }

    validator = ArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    assert not result.error_messages



# Generated at 2022-06-12 23:03:16.273257
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():

    for success in (
        {'name': 'bo'},
        {'name': 'bo', 'age': 42},
        {'name': 'bo', 'age': None},
    ):
        result = ModuleArgumentSpecValidator({
            'name': {'type': 'str'},
            'age': {'type': 'int'}
        }).validate(success)
        assert not result.error_messages
        assert isinstance(result.validated_parameters, dict)
        assert set(result.validated_parameters.keys()) == set(success.keys())


# Generated at 2022-06-12 23:03:24.538590
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

    result = ModuleArgumentSpecValidator(argument_spec).validate(parameters)

    assert result.error_messages == []
    assert result.validated_parameters == {'name': 'bo', 'age': 42}
    assert result._no_log_values == set()
    assert result._unsupported_parameters == set()
    assert result._deprecations == []
    assert result._warnings == []

# Generated at 2022-06-12 23:03:33.454986
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils.six import StringIO

    from ansible.errors import AnsibleParserError

    from ansible.module_utils.common.collections import ImmutableDict

    argument_spec = ImmutableDict({
        'a': {'type': 'str', 'required': True},
        'b': {'type': 'str', 'required': True, 'default': 'B'},
    })

    parameters = {'a': 'a'}

    validator = ModuleArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)
    assert result.validated_parameters == parameters
    assert result.error_messages == []
    assert result.errors == []

    parameters = {'a': 'a', 'b': 'b'}

    validator = ModuleArgumentSpecValid

# Generated at 2022-06-12 23:03:43.950486
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

    assert(isinstance(result, ValidationResult))
    assert(isinstance(result.errors, AnsibleValidationErrorMultiple))
    assert(isinstance(result.validated_parameters, dict))
    assert(isinstance(result._unsupported_parameters, set))
    assert(isinstance(result._no_log_values, set))
    assert(result.error_messages == [])

# Generated at 2022-06-12 23:03:53.464163
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    def my_func(arg1, arg2, arg3):
        # This should never occur unless the test is broken
        raise RuntimeError("my_func should not be called")

    # Test with no argument spec
    parameters = {
        'arg1': "my_string",
        'arg2': 42,
        'arg3': [1, 2, 3],
    }
    argument_spec = {}
    validator = ArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)
    assert result.errors == AnsibleValidationErrorMultiple()
    assert result.validated_parameters == parameters

    # Test with argument spec (no options)

# Generated at 2022-06-12 23:03:58.737758
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    argument_spec = {
        "age": {
            "type": "str",
            "required": True
        }
    }
    validator = ArgumentSpecValidator(argument_spec)
    parameters = {}
    result = validator.validate(parameters)
    assert len(result.errors) == 1
    assert result.errors[0].message == "the field 'age' is required but was not provided"
    assert result.validated_parameters == {}

# Generated at 2022-06-12 23:04:18.183266
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    from ansible.module_utils.common.text.converters import to_native
    from ansible.module_utils.common.validation import check_mutually_exclusive
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.module_utils.common.parameters import _set_defaults
    from ansible.module_utils.common.parameters import _validate_argument_types
    from ansible.module_utils.common.parameters import _validate_argument_values
    from ansible.module_utils.common.validation import check_required_arguments

# Generated at 2022-06-12 23:04:27.173172
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    mutually_exclusive = ['foo', 'bar']
    arg_spec = dict(
        foo=dict(type='str'),
        bar=dict(type='str'),
    )
    module = dict(
        foo=1,
        bar=1,
    )
    validator = ModuleArgumentSpecValidator(
        argument_spec=arg_spec,
        mutually_exclusive=mutually_exclusive,
        required_together=None,
        required_one_of=None,
        required_if=None,
        required_by=None,
    )
    result = validator.validate(module)
    assert result.errors
    assert len(result.errors) == 1
    for error in result.errors:
        assert isinstance(error, MutuallyExclusiveError)

# Generated at 2022-06-12 23:04:37.066858
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():

    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
        'aliased_parameter': {'type': 'str', 'aliases': ['alias_1', 'alias_2']},
        'state': {'type': 'str', 'aliases': ['alias_3', 'alias_4'], 'deprecated': {'msg': 'deprecated'}},
    }

    # Parameters without any errors or deprecations or warnings
    parameters = {
        'name': 'bo',
        'age': '42',
    }

    # Parameters with a deprecation warning
    parameters_alias_deprecation = {
        'name': 'bo',
        'age': '42',
        'state': 'present',
    }

    # parameters with an alias

# Generated at 2022-06-12 23:04:44.576364
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    class DummyClass(ModuleArgumentSpecValidator):
        def __init__(self, cli_args):
            super(DummyClass, self).__init__(cli_args)
    cli_args = dict(
        argument_spec=dict(
            name=dict(type='str'),
            age=dict(type='int'),
        )
    )
    dummy_module_argument_spec_validator = DummyClass(cli_args)

    # simple case ok
    parameters = dict(name='bo', age=42)
    result = dummy_module_argument_spec_validator.validate(parameters)
    assert result._warnings == []
    assert result._deprecations == []
    assert result.errors.messages == []

    # both option and alias set

# Generated at 2022-06-12 23:04:52.775094
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    # Test cases to test validate method
    validator = ArgumentSpecValidator({
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    })


# Generated at 2022-06-12 23:04:59.623685
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
    assert result.errors == [], result.error_messages
    assert result.validated_parameters == {'name': 'bo', 'age': 42}



# Generated at 2022-06-12 23:05:01.104494
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    assert hasattr(ModuleArgumentSpecValidator, "validate")


# Generated at 2022-06-12 23:05:09.663380
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    # ---- set spec ---- #
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }
    # ---- set parameters ---- #
    parameters = {
        'name': 'bo',
        'age': '42',
    }
    # ---- check ---- #
    validator = ArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    if result.error_messages:
        sys.exit("Validation failed: {0}".format(", ".join(result.error_messages)))

    valid_params = result.validated_parameters

# Generated at 2022-06-12 23:05:14.328118
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    from ansible.module_utils._text import to_text

    raw_params = {}
    parameters = {to_text(k): to_text(v) for k, v in raw_params.items()}

    argument_spec = {
        'name': {'type': 'str', 'default': 'world'}
    }

    validator = ArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)
    assert result.error_messages == []
    assert result.validated_parameters == {'name': 'world'}

# Generated at 2022-06-12 23:05:23.535774
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible_collections.ansible.netcommon.tests.unit.compat import unittest
    from ansible.module_utils.six import assertRaisesRegex, PY3

    class TestModuleArgumentSpecValidator(unittest.TestCase):
        def test_basic_validation(self):
            argument_spec = {
                'name': {'type': 'str'},
                'age': {'type': 'int', 'default': 18},
            }

            parameters = {
                'name': 'Ansible',
                'age': '42',
            }

            validator = ModuleArgumentSpecValidator(argument_spec)
            result = validator.validate(parameters)


# Generated at 2022-06-12 23:05:40.357031
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    argument_spec = {'key1': {'type': 'str', 'default': 'default_key1'}, 'key2': {'type': 'str', 'required': True}}
    parameters = {'key1': 'value1'}
    validator = ModuleArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    assert set(result._validated_parameters.keys()) == {'key1', }
    assert result._validated_parameters['key1'] == 'value1'

# Generated at 2022-06-12 23:05:46.947455
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    """ArgumentSpecValidator#validate tests."""
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

# Generated at 2022-06-12 23:05:55.795300
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils.common.parameters import (
        get_validated_arguments,
        set_defaults_no_log,
        validate_argument_types)

    def validate_parameter_values(spec, module_arguments, errors):
        if 'name' in module_arguments:
            if module_arguments['name'] == 'error':
                errors.append(AnsibleValidationError(errors=['Error']))
            elif module_arguments['name'] == 'fail':
                raise ValueError("Error")

    argument_spec = dict(
        name=dict(type='str', required=True),
        age=dict(type='int'),
    )


# Generated at 2022-06-12 23:06:04.691674
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    from ansible.module_utils.six import string_types
    from ansible.module_utils.common._collections_compat import MutableMapping, MutableSequence
    from ansible.module_utils.common.arg_spec import ArgumentSpecValidator
    class TestAnsibleModule(object):
        def __init__(self, argument_spec, **kwargs):
            self.argument_spec = argument_spec

    # Simple Example of argument_spec

# Generated at 2022-06-12 23:06:10.216901
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    import datetime
    import json
    import os

    from ansible.module_utils.common.deprecation import Deprecation

    def validate_args(arg_spec, parameters):
        validator = ModuleArgumentSpecValidator(arg_spec)
        return validator.validate(parameters)

    def validate_json(arg_spec, json_path):
        arg_spec_file = os.path.join(os.path.dirname(__file__), json_path)
        arg_spec_data = json.load(open(arg_spec_file))

        return validate_args(arg_spec_data['argument_spec'], arg_spec_data['parameters'])

    def init_deprecation_mock():
        Deprecation._instance = None
        Deprecation._warnings = []
        Deprec