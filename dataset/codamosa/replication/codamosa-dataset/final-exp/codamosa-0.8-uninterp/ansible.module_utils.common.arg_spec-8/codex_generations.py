

# Generated at 2022-06-12 22:56:22.077899
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    class ValidationResultMock:
        _deprecations = []
        _warnings = []

    assert ModuleArgumentSpecValidator.validate(ValidationResultMock())

# Generated at 2022-06-12 22:56:32.548740
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():
    argument_spec = dict(
        name=dict(type="str"),
        age=dict(type="int")
    )
    mutually_exclusive = [['name', 'age']]
    required_together = []
    required_one_of = []
    required_if = []
    required_by = {}

    assert ArgumentSpecValidator(argument_spec, mutually_exclusive, required_together,
                                 required_one_of, required_if, required_by).argument_spec == argument_spec
    assert ArgumentSpecValidator(argument_spec, mutually_exclusive, required_together,
                                 required_one_of, required_if, required_by)._mutually_exclusive == mutually_exclusive

# Generated at 2022-06-12 22:56:41.073158
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    class MyModuleArgumentSpecValidator(ModuleArgumentSpecValidator):
        def __init__(self):
            argument_spec = {'a': {'type': 'str'}, 'b': {'type': 'str'}}
            super(MyModuleArgumentSpecValidator, self).__init__(argument_spec)

        def validate(self, parameters):
            return super(MyModuleArgumentSpecValidator, self).validate(parameters)

    class MyArgumentSpecValidator(ArgumentSpecValidator):
        def __init__(self):
            argument_spec = {'a': {'type': 'str'}, 'b': {'type': 'str'}}
            super(MyArgumentSpecValidator, self).__init__(argument_spec)


# Generated at 2022-06-12 22:56:48.821335
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    argument_spec = {
        'name': {
            'type': 'str'
        },
        'age': {
            'type': 'int'
        },
    }

    parameters = {
        'name': 'bo',
        'age': '42',
    }

    validator = ArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    assert(result._validated_parameters == {
        'name': 'bo',
        'age': 42,
    })



# Generated at 2022-06-12 22:56:55.637716
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    spec = {'a': {'type': 'int'}}
    validator = ArgumentSpecValidator(spec)
    # no error
    parameters = {'a': '3'}
    results = validator.validate(parameters)
    assert not results.errors
    # error: type 'str' is not compatible with type 'int'
    parameters = {'a': '3f'}
    results = validator.validate(parameters)
    assert len(results.errors) == 1

# Generated at 2022-06-12 22:56:59.246829
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    class FakeAnsibleModule:
        def fail_json(self, msg, **kwargs):
            pass
        def exit_json(self, **kwargs):
            pass

    argument_spec = {"option": {"type": "str", "default": "default", "required": True}}
    parameters = {"option": "value"}

    validator = ModuleArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    assert result.validated_parameters == {"option": "value"}
    assert not result.errors
    assert not result.error_messages

# Generated at 2022-06-12 22:57:05.666167
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    # prepare arguments
    argument_spec = {"test": {"type": "str"}}
    parameters = {"test": "string"}

    validator = ArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    assert isinstance(result, ValidationResult)
    assert isinstance(result.errors, AnsibleValidationErrorMultiple)
    assert isinstance(result.error_messages, list)
    assert isinstance(result.validated_parameters, dict)



# Generated at 2022-06-12 22:57:15.929328
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # Instantiate a ModuleArgumentSpecValidator object
    my_val = ModuleArgumentSpecValidator(argument_spec={}, mutually_exclusive=None, required_together=None, required_one_of=None, required_if=None, required_by=None)

# Generated at 2022-06-12 22:57:25.365415
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():

    # given
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }
    mutually_exclusive = [
        ['name', 'age'],
    ]
    required_together = [
        ['name', 'age'],
    ]
    required_if = [
        ['name', 'bo', ['age']],
    ]
    mutually_exclusive_error = MutuallyExclusiveError("Parameters are mutually exclusive: ['age', 'name']")
    mutually_exclusive_error.message = "Parameters are mutually exclusive: ['age', 'name']"

# Generated at 2022-06-12 22:57:35.489925
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
        'occupation': {'type': 'dict', 'required': True},
    }
    mutually_exclusive = [['name', 'age']]
    validator = ArgumentSpecValidator(spec, mutually_exclusive=mutually_exclusive)

    params = {
        'occupation': 'secret_agent',
    }
    result = validator.validate(params)

    assert isinstance(result, ValidationResult)
    assert result.error_messages == ["'occupation' is required"]

    params = {
        'name': 'Alice',
        'age': 42,
    }
    result = validator.validate(params)

# Generated at 2022-06-12 22:57:48.725464
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    argument_spec = {
                'name': {'type': 'str'},
                'age': {'type': 'int'},
                'dob': {'type': 'datetime'},
                'parents': {'type': 'dict'},
                'parents.mother': {'type': 'str'},
                'parents.father': {'type': 'str'},
                }

    invalid_parameters = {
        'name': 'bo',
        'age': '42',
        'dob': '2014-10-21 15:02:45.463779',
        'parents': {'mother':'bo', 'father': 'wang'},
        }

    validator = ArgumentSpecValidator(argument_spec)
    result = validator.validate(invalid_parameters)


# Generated at 2022-06-12 22:57:57.015381
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():

    import sys
    A = sys.modules[__name__]

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


# Generated at 2022-06-12 22:57:58.819694
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():
    assert ArgumentSpecValidator({'b': {'type': 'bool'}})



# Generated at 2022-06-12 22:58:00.933708
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    """Unit test for the validate method of class ModuleArgumentSpecValidator"""
    # TODO: Implement this unit test
    pass


# Generated at 2022-06-12 22:58:08.071090
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():

    # Setup
    argument_spec = {
        'name': {'type': 'str', 'default': 'bo'},
        'age': {'type': 'int'},
        'credentials': {'type': 'dict', 'default': {'username': 'bo', 'password': 'pass'}}
    }
    mutually_exclusive = ['name', 'age']
    required_together = [('name', 'age')]
    required_one_of = [('name', 'age', 'credentials')]

    parameter_set_1 = {
        'name': 'bo',
        'age': 42,
        'credentials': {'username': 'bo', 'password': 'pass'}
    }

# Generated at 2022-06-12 22:58:19.372964
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    import sys
    import unittest

    class TestArgumentSpecValidator(unittest.TestCase):
        """TestArgumentSpecValidator."""
        def test_simple_example(self):
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

            self.assertEqual(result.error_messages, [])
            self.assertEqual(result.unsupported_parameters, set())
            self.assertEqual(result.validated_parameters, {'name': 'bo', 'age': 42})



# Generated at 2022-06-12 22:58:24.925779
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    _args = dict()
    _kwargs = dict(
        mutually_exclusive=None,
        required_together=None,
        required_one_of=None,
        required_if=None,
        required_by=None,
    )
    validator = ModuleArgumentSpecValidator(**_kwargs)
    assert validator.validate(_args)

# Generated at 2022-06-12 22:58:30.596723
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

    validator = ModuleArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    assert len(result._deprecations) == 0
    assert len(result._warnings) == 0
    assert len(result._no_log_values) == 0
    assert len(result._unsupported_parameters) == 0
    assert len(result.errors) == 0

    assert result.validated_parameters == {
        'name': 'bo',
        'age': 42,
    }

# Generated at 2022-06-12 22:58:36.880962
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    # Test basic use
    argument_spec = {
        'name': {'type': 'str'},
        'path': {'type': 'str'},
    }
    parameters = {
        'name': 'bo',
        'path': '/foo',
    }
    validator = ArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)
    assert result.validated_parameters == parameters
    assert len(result.error_messages) == 0
    assert result._no_log_values == set()

    # Test default values are set and type is coerced

# Generated at 2022-06-12 22:58:47.139196
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    argument_spec = {"options": {"type": "list", "elements": "str"}}
    options = ["a", "b", "c", "d"]
    result = ArgumentSpecValidator(argument_spec).validate({"options": options})

    assert result.error_messages == []
    assert result.validated_parameters == {"options": options}
    assert result.unsupported_parameters == set()

    options = "a,b,c,d"
    result = ArgumentSpecValidator(argument_spec).validate({"options": options})

    assert result.error_messages == []
    assert result.validated_parameters == {"options": options}
    assert result.unsupported_parameters == set()


# Generated at 2022-06-12 22:59:00.511111
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():

    class FakeAliasError(object):
        def __init__(self, msg='test'):
            self.msg = msg

        @property
        def message(self):
            return self.msg

    class FakeAnsibleValidationErrorMultiple(object):
        def __init__(self):
            self.errors = []

        def append(self, error):
            self.errors.append(error)

        def messages(self):
            return [e.msg for e in self.errors]

    class FakeUnsupportedError(object):
        def __init__(self, *args, **kwargs):
            self.msg = 'test'

    class FakeMutuallyExclusiveError(object):
        def __init__(self, *args, **kwargs):
            self.msg = 'test'


# Generated at 2022-06-12 22:59:12.161671
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    validator = ModuleArgumentSpecValidator(dict(
        name=dict(type='str'),
        state=dict(type='str', required=True,
                   choices=['present', 'absent']),
        age=dict(type='int', aliases=['how_old']),
        update=dict(type='bool', aliases=['update_pkgs']),
        force=dict(type='bool', aliases=['force_install']),
        options=dict(type='list', aliases=['extra_options']),
        updated=dict(type='bool', default=False, removed_in_version='2.10')
    ))

# Generated at 2022-06-12 22:59:20.372207
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
#
# The code below is generated, do not edit it, modify the template instead.
#

    # Validate valid parameters with no deprecation warnings and no warnings.
    warnings = []
    deprecations = []
    def warn(msg):
        warnings.append(msg)

    def deprecate(msg, version=None, date=None, collection_name=None):
        deprecations.append(msg)


# Generated at 2022-06-12 22:59:31.281749
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    """
    This function is a unit test for method validate of class ArgumentSpecValidator
    """
    check_module = ArgumentSpecValidator(argument_spec={
                                                     'name': {'type': 'str'},
                                                     'age': {'type': 'int'},
                                                     'sex': {'type': 'str', 'choices': ['male', 'female']}
                                                     }
                                         )

    parameters = {'name': 'bo', 'age': '42', 'sex': 'male'}

    result = check_module.validate(parameters)

    assert result.validated_parameters['name'] == 'bo'
    assert result.validated_parameters['age'] == 42

    parameters = {'name': 'bo', 'age': '42', 'sex': 'alien'}


# Generated at 2022-06-12 22:59:40.674476
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int', 'aliases': ['old'], 'version_added': '3.0', 'collection_name': 'collection.name'},
    }
    parameters = {
        'name': 'bo',
        'age': '42',
    }
    expected_warnings = """\
Both option age and its alias old are set.
"""
    expected_deprecations = """\
DEPRECATED DEPRECATED DEPRECATED in versions 3.0 and later! Alias 'old' is deprecated. See the module docs for more information
[DEPRECATION WARNING]: Alias 'old' is deprecated. See the module docs for more information
This feature will be removed in version 3.0.
"""

    validator = ModuleArgumentSpec

# Generated at 2022-06-12 22:59:48.329163
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():

    import pytest
    from ansible.module_utils.common.warnings import AnsibleDeprecationWarning, AnsibleUserWarning

    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
        'gender': {'type': 'str', 'choices': ['male', 'female']},
        'deprecated_alias': {'type': 'str', 'aliases': ['new_name']},
        'no_log_alias': {'type': 'bool', 'no_log': True, 'aliases': ['no_log']},
    }


# Generated at 2022-06-12 22:59:57.810278
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    import sys
    result = {}
    arg_spec = {
        'name': {'type': 'str', 'required': True, 'no_log': True},
        'age': {'type': 'int', 'required': True},
    }

    parameters = {
        'name': 'bo',
        'age': '42',
    }

    validator = ModuleArgumentSpecValidator(argument_spec=arg_spec, mutually_exclusive=None, required_together=None,
                                            required_one_of=None, required_if=None, required_by=None)
    result = validator.validate(parameters=parameters)
    if result.error_messages:
        sys.exit("Validation failed: {0}".format(", ".join(result.error_messages)))


# Generated at 2022-06-12 22:59:59.236457
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    validator = ModuleArgumentSpecValidator()
    assert isinstance(validator.validate({}), ValidationResult)

# Generated at 2022-06-12 23:00:08.908972
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # test call with alias warnings
    argument_spec = {
        'name': {'type': 'str', 'aliases': ['hostname']},
        'age': {'type': 'int'},
        'show': {'type': 'bool', 'default': True, 'aliases': ['verbose']},
    }

    parameters = {
        'name': 'bo',
        'age': '42',
        'verbose': False,
    }

    validator = ModuleArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    assert result.errors == []
    assert result.warnings == []
    assert result.validated_parameters == {'name': 'bo', 'age': 42, 'show': False}

# Generated at 2022-06-12 23:00:19.328072
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():

    from inspect import signature

    from ansible.module_utils.connection import Connection
    from ansible.module_utils.six import PY3
    from ansible.module_utils.six.moves import configparser as ConfigParser

    validator = ArgumentSpecValidator({
        'foo': {'type': 'str'},
        'bar': {'type': 'int'}
    })

    parameters = {
        'foo': 'FOO',
        'bar': 'BAR',
    }

    result = validator.validate(parameters)

# Generated at 2022-06-12 23:00:25.554310
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    validator = ModuleArgumentSpecValidator(argument_spec={})
    # validator.validate()

# Generated at 2022-06-12 23:00:31.313468
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

    validator = ArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)
    assert result.error_messages == []

# Generated at 2022-06-12 23:00:41.258014
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    argument_spec = {
        'name': {'type': 'str'},
        'state': {'type': 'str', 'default': 'foo'},
        'age': {'type': 'int'},
        'arguments': {
            'type': 'dict',
            'options': {
                'size': {'type': 'int'},
                'name': {'type': 'str'},
                'state': {'type': 'str', 'default': 'bar'},
            },
            'aliases': ['bar'],
        },
        'children': {'type': 'list', 'elements': 'dict'},
    }


# Generated at 2022-06-12 23:00:50.075942
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():

    result = None

    # The following test case expects that the module alias is deprecated.
    def test_module_alias():
        argument_spec = {
            'user': {'type': 'str', 'aliases': ['module_alias']},
        }
        spec_validator = ModuleArgumentSpecValidator(argument_spec)
        try:
            parameters = {'module_alias': 'user1'}
            result = spec_validator.validate(parameters)
        except:
            assert result.error_messages == "Invalid arguments passed to ValidationResult constructor. 'no_log_values' must be a set object."

    test_module_alias()

# Generated at 2022-06-12 23:00:57.651202
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    # pylint: disable=invalid-name
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

# Generated at 2022-06-12 23:01:07.075976
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    #This is the argument spec for Ansible's Ping module
    argument_spec = {
        'data': {
            'default': 'pong',
            'type': 'str',
        },
        'host': {
            'default': 'localhost',
            'type': 'str',
        },
        'port': {
            'default': 22,
            'type': 'int',
        },
        'timeout': {
            'default': 2,
            'type': 'int',
        },
    }
    parameters = {
        'data': 'pong',
        'port': 22,
        'timeout': 2,
    }
    validator = ModuleArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    assert(result is not None)

# Generated at 2022-06-12 23:01:17.251778
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    number_required = [ ['test_int'], ['test_str'], ['test_float'] ]
    number_required_message = "One of the following is required: ['test_int', 'test_str', 'test_float']"
    test_arg_spec = {
        'test_int': {
            'type': 'int',
            'required': True,
        },
        'test_str': {
            'type': 'str',
            'required': True,
        },
        'test_float': {
            'type': 'float',
            'required': True,
        },
    }

    parameters = {}
    validator = ArgumentSpecValidator(test_arg_spec)
    result = validator.validate(parameters)
    assert result.error_messages == [ number_required_message ]

   

# Generated at 2022-06-12 23:01:20.804444
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    result = ModuleArgumentSpecValidator(argument_spec={'some_arg': {'type': 'str'}}).validate({'some_arg': 'x'})
    assert result.validated_parameters == {'some_arg': 'x'}

# Generated at 2022-06-12 23:01:31.290311
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # Make Mock Object by using side_effect
    mock_result_validate = ValidationResult({})
    mock_result_validate.errors = AnsibleValidationErrorMultiple()
    mock_result_validate._deprecations = [{'name':'test_name', 'version':'test_version', 'date':'test_date', 'collection_name':'test_collection_name'}]
    mock_result_validate._warnings = [{'option':'test_option', 'alias':'test_alias'}]

    # Call side_effect function
    def side_effect(*args, **kwargs):
        return mock_result_validate
    
    # Mock super()
    ModuleArgumentSpecValidator.validate = MagicMock(side_effect=side_effect)

    # Mocking warn method
    Module

# Generated at 2022-06-12 23:01:38.017048
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    """Unit test for method validate of class ArgumentSpecValidator
    """
    from ansible.module_utils.common.arg_spec import (
        ArgumentSpecValidator,
        ValidationResult,
    )

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


# Generated at 2022-06-12 23:01:57.266375
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    """test_ArgumentSpecValidator_validate checks if the ValidationResult returned by the validate method of
    ArgumentSpecValidator contains the expected validated parameters and has the expected errors.

    This up-to-date test should be maintained alongside the validate method.
    """
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
        'description': {'type': 'str', 'no_log': True},
    }

    parameters = {
        'name': 'bo',
        'age': '42',
        'description': 'This is no_log',
    }

    validator = ArgumentSpecValidator(argument_spec)

    result = validator.validate(parameters)
    assert result is not None
    assert type(result) == ValidationResult

   

# Generated at 2022-06-12 23:01:57.826082
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    pass

# Generated at 2022-06-12 23:02:05.021028
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils.six import iteritems
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.common.validation import ensure_type
    from ansible.module_utils.urls import open_url

    # pylint: disable=no-name-in-module,import-error
    from nose2.tools import params

    class AnsibleModule(object):
        def __init__(self, *args, **kwargs):
            self.params = self.argument_spec = {}
            self.check_mode = False
            self.fail_json = {'msg': 'FAIL_JSON_MSG'}
            self.warn = {}


# Generated at 2022-06-12 23:02:15.860048
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }

    mutually_exclusive = [['name', 'age']]
    required_together = [ ['name', 'age'] ]
    required_one_of = []
    required_if = []
    required_by = {}

    validator = ArgumentSpecValidator(argument_spec,
                                      mutually_exclusive=mutually_exclusive,
                                      required_together=required_together,
                                      required_one_of=required_one_of,
                                      required_if=required_if,
                                      required_by=required_by)

    parameters = []

    parameters.append({ 'name': 'bo', 'age': '42' })

# Generated at 2022-06-12 23:02:27.063376
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    result = False

    # Create a parameter to validate and fail
    parameter_bad_parameter = {
        'name': 'bo',
        'age': '42',
        'bad_parameter': 'oops'
    }

    validator = ModuleArgumentSpecValidator(argument_spec,
                                            mutually_exclusive=mutually_exclusive,
                                            required_together=required_together,
                                            required_one_of=required_one_of,
                                            required_if=required_if,
                                            required_by=required_by)
    result = validator.validate(parameter_bad_parameter)

    if result:
        sys.exit('UnitTest: Failed to validate parameter with bad parameter')

    # Create a parameter to validate and succeed

# Generated at 2022-06-12 23:02:35.722136
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # Set up
    f = 'test_ModuleArgumentSpecValidator_validate'
    argument_spec = {'state': {'type': 'str', 'required': True, 'default': 'present', 'choices': ['absent', 'present']},
                     'changes': {'type': 'list', 'required': False},
                     'state2': {'type': 'str', 'required': True, 'default': 'active', 'choices': ['active', 'present']},
                     'include_inactive': {'type': 'bool', 'default': False, 'type': 'bool'},
                     'external': {'type': 'bool', 'default': False, 'type': 'bool'}}
    mutually_exclusive = [['state', 'state2']]
    required_together = [['state', 'state2']]
    required_one

# Generated at 2022-06-12 23:02:46.332647
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    def find_deprecate_warn(log_string):
        deprecate_warn_regex = re.compile(r'DEPRECATION_WARNING.*')
        warn_regex = re.compile(r'WARNING.*module.*')
        deprecate_warns = deprecate_warn_regex.findall(log_string)
        warns = warn_regex.findall(log_string)
        return deprecate_warns,warns

    import ansible.module_utils.common.warnings as warning_module
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
    handler

# Generated at 2022-06-12 23:02:49.467153
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    module_spec = deepcopy(argument_spec)
    module_arguments = {
        'name': 'bo',
        'age': '42',
    }
    validator = ModuleArgumentSpecValidator(module_spec)
    result = validator.validate(module_arguments)

    assert len(result.errors) == 0
    assert result.validated_parameters == {'name': 'bo', 'age': 42}

# Generated at 2022-06-12 23:02:55.540806
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    from ansible.module_utils.common.arg_spec import ArgumentSpecValidator
    from ansible.module_utils.basic import AnsibleModule

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

    assert isinstance(result, ValidationResult)



# Generated at 2022-06-12 23:03:00.882257
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    argument_spec = {'name': {'type': 'str'}, 'age': {'type': 'int'}}
    parameters = {'name': 'bo', 'age': '42'}

    validator = ArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    assert False == result.errors
    assert 42 == result.validated_parameters['age']

# Generated at 2022-06-12 23:03:30.545620
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # test parameters
    parameters = {}

    # test argument_spec
    argument_spec = {}

    # test mutually_exclusive
    mutually_exclusive = None

    # test required_together
    required_together = None

    # test required_one_of
    required_one_of = None

    # test required_if
    required_if = None

    # test required_by
    required_by = None

    a = ModuleArgumentSpecValidator(argument_spec, mutually_exclusive, required_together, required_one_of, required_if, required_by)
    b = a.validate(parameters)

# Generated at 2022-06-12 23:03:33.155511
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    validator = ArgumentSpecValidator({})
    result = validator.validate({})
    assert result.validated_parameters == {}
    assert result.errors == []
    assert result.error_messages == []


# Generated at 2022-06-12 23:03:39.670121
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
    assert result.validated_parameters == {'name': 'bo', 'age': 42}

# Generated at 2022-06-12 23:03:49.679080
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }
    mutually_exclusive = []
    required_together = []
    required_one_of = []
    required_if = []
    required_by = []

    validator = ArgumentSpecValidator(argument_spec,mutually_exclusive=mutually_exclusive,required_together=required_together,required_one_of=required_one_of,required_if=required_if,required_by=required_by)

    parameters = {
        'name': 'bo',
        'age': '42',
    }

    result = validator.validate(parameters)

    assert result.validated_parameters == {'age': 42, 'name': 'bo'}
    assert result.errors

# Generated at 2022-06-12 23:03:58.700787
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    date_string = '2018'
    version_string = '1.0'
    deprecation_warnings = []
    deprecated_aliases = []
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
        '__foo': {
            'aliases': ['bar'],
            'type': 'dict'
        },
        'money': {
            'default': '$',
            'type': 'str'
        }
    }
    parameters = {
        'name': 'bo',
        'age': '42',
        'money': 'USD'
    }
    validator = ModuleArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    assert result._deprecations == deprecation

# Generated at 2022-06-12 23:04:00.073888
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    # TODO: Use this method to trigger the "for loop" above in ArgumentSpecValidator.validate()
    pass

# Generated at 2022-06-12 23:04:11.573066
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():
    # test check_mutually_exclusive() function
    # Create a list of lists. The lists contain
    # 1. parameters that should not be provided together
    # 2. parameters that are required together

    m_exclusive = [['a'], ['b', 'c']]

    # Create a list of lists of parameters
    # where one from each list is required

    r_together = [['d', 'e']]

    # Create a dictionary of parameters
    # that are required if another parameter has a value

    r_if = [['f', 'yes', ['g', 'h']]]

    # Create a dictionary of parameters
    # that require other parameters to be present

    r_by = {'i': ['j']}

    # Create an argument spec

# Generated at 2022-06-12 23:04:18.617633
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    from ansible.module_utils.common.text.converters import to_native
    from ansible.module_utils.common.text.utils import to_text
    from ansible.module_utils.common.validation import check_mutually_exclusive, check_required_arguments
    from ansible.module_utils.basic import AnsibleModule


# Generated at 2022-06-12 23:04:28.190181
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    spec_data = {'name': {'type': 'str', 'aliases': ['name_alias']}}
    mutually_exclusive = [['name', 'name_alias']]
    validator = ModuleArgumentSpecValidator(spec_data, mutually_exclusive)
    # When both "name" and "name_alias" are set
    parameters = {"name": "test", "name_alias": "test_alias"}
    result = validator.validate(parameters)
    assert result.validated_parameters == parameters
    assert result.errors == []
    assert result.error_messages == []
    assert result._no_log_values == set()
    assert result.unsupported_parameters == set()
    assert len(result._warnings) == 1
    assert result._warnings[0]['option'] == 'name'
   

# Generated at 2022-06-12 23:04:38.059667
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    """ Unit test for method validate of class ArgumentSpecValidator
    """
    # setup
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }
    parameters = {
        'name': 'bo',
        'age': '42',
    }
    validator = ArgumentSpecValidator(argument_spec)
    # test
    result = validator.validate(parameters)
    # asserts
    assert result.validated_parameters == {'name': 'bo', 'age': 42}

    # setup
    parameters = {'age': '42'}
    validator2 = ArgumentSpecValidator(argument_spec)
    # test
    result = validator2.validate(parameters)
    # asserts
    assert result.validated_

# Generated at 2022-06-12 23:05:08.934606
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int', 'default': 42},
        'weight': {'type': 'float', 'default': 12.5},
    }

    parameters = {
        'name': 'bo',
        'age': '42',
    }

    validator = ModuleArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)


# Generated at 2022-06-12 23:05:17.118415
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    def assert_result_equals_validator(result, validator):
        assert result._unsupported_parameters == validator._unsupported_parameters
        assert result._validated_parameters == validator._validated_parameters
        assert result.errors == validator.errors

    spec = dict(x=dict(type='str', required=True, default='a'),
                y=dict(type='str', required=False),
                z=dict(type='str', choices=['a', 'b']),
                s=dict(type='str', default='s'),
                f=dict(type='str', no_log=True, default='f'),
                )

    mutually_exclusive = [['x']]
    required_together = [['x']]
    required_one_of = [['x']]

# Generated at 2022-06-12 23:05:27.701019
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():

    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }
    mutually_exclusive = [['name', 'age']]
    required_together = [['name', 'age']]
    required_one_of = [['name', 'age']]
    required_if = [['name', 'age', ['name', 'age']]]
    required_by = {'name': ['age'], 'age': ['name']}

    validator = ModuleArgumentSpecValidator(argument_spec,
        mutually_exclusive=mutually_exclusive,
        required_together=required_together,
        required_one_of=required_one_of,
        required_if=required_if,
        required_by=required_by,
    )
    
   

# Generated at 2022-06-12 23:05:37.518747
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # test parameters
    parameters = {'age': '42', 'name': 'bo'}
    # test mutually_exclusive
    mutually_exclusive = False
    # test required_together
    required_together = False
    # test required_one_of
    required_one_of = False
    # test required_if
    required_if = False
    # test required_by
    required_by = False
    # test argument_spec
    argument_spec = {'name': {'type': 'str'}, 'age': {'type': 'int'}}
    # test aliases
    aliases = False
    # test _deprecations
    _deprecations = False
    # test _warnings
    _warnings = False
    # test errors
    errors = False
    # test _validated_parameters
    _validated_param

# Generated at 2022-06-12 23:05:43.605539
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():
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

    assert result.error_messages == []
    assert result.validated_parameters == {'name': 'bo', 'age': 42}

# Generated at 2022-06-12 23:05:52.582731
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    # Some strange test values
    weird_value = '\x00\xff'
    weird_value_set = set()
    weird_value_set.add(weird_value)
    weird_value_dict = {}
    weird_value_dict[weird_value] = weird_value
    weird_value_dict_2 = {}
    weird_value_dict_2[weird_value] = weird_value
    weird_value_dict_2[weird_value_set] = weird_value_set
    weird_value_list = []
    weird_value_list.append(weird_value)
    weird_value_list.append(weird_value_set)
    weird_value_list.append(weird_value_dict)

# Generated at 2022-06-12 23:06:01.484682
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    # Set up arguments for ArgumentSpecValidator.__init__
    argument_spec = \
    {
        "str_with_default": {"type": "str", "default": "default value"},
        "required_str_1": {"type": "str", "required": True},
        "required_str_2": {"type": "str", "required": True},
        "str_with_choices": {"type": "str", "choices": ["a", "b", "c"]},
        "suboptions": {"type": "dict",
                       "options": {"suboption": {"type": "str", "default": "suboption_default"}}}
    }

# Generated at 2022-06-12 23:06:07.193412
# Unit test for method validate of class ArgumentSpecValidator