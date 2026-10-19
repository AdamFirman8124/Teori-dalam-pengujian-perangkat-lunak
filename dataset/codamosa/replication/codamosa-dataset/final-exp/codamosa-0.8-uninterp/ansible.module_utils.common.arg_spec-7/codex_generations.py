

# Generated at 2022-06-12 22:56:28.413782
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():

    # Create a dummy module class
    class AnsibleModule(object):
        def __init__(self, *args, **kwargs):
            pass

    # Create a dummy argument_spec
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }

    # Create a module with our dummy class and argument spec
    module = AnsibleModule(argument_spec=argument_spec)

    # Create a Validation object using the module's .validate_arguments() method
    result = module.validate_arguments(validate_spec={'arguments': argument_spec})

    # Ensure that validate_arguments returned a ValidationResult object
    assert isinstance(result, ValidationResult)

    # The following is a list of variables that are contained within the ValidationResult

# Generated at 2022-06-12 22:56:37.260944
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # Set up the test values
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

    # Check the returned values
    assert result.validated_parameters == parameters
    assert result.unsupported_parameters == set()
    assert result.error_messages == []
    # No log should be set for this test
    assert result._no_log_values == set()
    # No warnings or deprecate messages expected
    assert result._warnings == []
    assert result._deprecations == []



# Generated at 2022-06-12 22:56:47.675551
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    import ansible.module_utils.common.warnings

    argument_spec = {
        'name': {
            'type': 'str',
            'aliases': ['my_name']
        },
        'age': {'type': 'int'},
    }

    parameters = {
        'name': 'bo',
        'age': '42',
    }

    validator = ModuleArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    assert result.validated_parameters['name'] == 'bo'
    assert result.validated_parameters['age'] == 42
    assert result.error_messages == []
    assert not result._deprecations
    assert not result._warnings

# Generated at 2022-06-12 22:56:58.269511
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    class MyMockedModule:
        def __init__(self, error_messages, deprecations, warnings):
            self._deprecations = deprecations
            self._warnings = warnings
            self.fail_json_msgs = error_messages

        def deprecate(self, msg, version, collection_name=None, date=None):
            data = dict(msg=msg, version=version, collection_name=collection_name, date=date)
            self._deprecations.append(data)

        def fail_json(self, msg):
            self.fail_json_msgs.append(msg)

        def warn(self, msg):
            self._warnings.append(msg)

    def mock_create_validator(argument_spec):
        validator = ModuleArgumentSpecValidator(argument_spec)


# Generated at 2022-06-12 22:57:06.610617
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int', 'aliases': ['age_int']},
        'list_age': {'type': 'list', 'elements': 'int'},
    }

    parameters = {
        'name': 'bo',
        'age': '42',
        'age_int': '66',
        'list_age': ['5', '6'],
    }

    validator = ModuleArgumentSpecValidator(argument_spec, required_by={'age': ['age_int']})

    result = validator.validate(parameters)
    assert not result.error_messages
    assert(result.validated_parameters == parameters)

# Generated at 2022-06-12 22:57:12.959800
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    validator = ArgumentSpecValidator({'name': {'type': 'str'}, 'age': {'type': 'int'}})
    result = validator.validate({'name': 'bo', 'age': '42'})
    assert result.validated_parameters == {'name': 'bo', 'age': 42}
    assert result.unsupported_parameters == set()
    assert result.error_messages == []



# Generated at 2022-06-12 22:57:20.656864
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():
    argument_spec = {
        'a_argument': {'type': 'int', 'required': True, 'aliases': ['a_parameter']},
        'b_argument': {'type': 'list', 'required': False, 'default': [], 'aliases': ['b_parameter']},
        'c_argument': {'type': 'dict', 'required': False, 'default': {}, 'aliases': ['c_parameter']},
    }

    mutually_exclusive = [
        ['a_argument', 'b_argument'],
        ['b_argument', 'c_argument'],
        ['a_argument', 'c_argument'],
    ]

    required_together = [['a_argument', 'b_argument']]

    required_one_of = [['b_argument', 'c_argument']]

    required

# Generated at 2022-06-12 22:57:24.086062
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    v = ModuleArgumentSpecValidator({'option': {'type': 'str', 'aliases': ['alias']}})
    v.validate({'option': 'some value', 'alias': 'some other value'})
    assert True

# Generated at 2022-06-12 22:57:34.407324
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    """Test ModuleArgumentSpecValidator.validate"""
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }

    parameters = {'name': 'bo', 'age': '42'}

    validator = ModuleArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    assert(isinstance(result, ValidationResult))
    assert(isinstance(result.errors, AnsibleValidationErrorMultiple))
    assert(isinstance(result.error_messages, list))
    assert(isinstance(result._no_log_values, set))
    assert(isinstance(result._unsupported_parameters, set))
    assert(isinstance(result.validated_parameters, dict))

# Unit test

# Generated at 2022-06-12 22:57:43.472736
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # Case 1
    # Expected: None
    # Actual: None
    mutually_exclusive = [
        [
            "force",
            "noop"
        ],
        [
            "yes",
            "no"
        ],
        [
            "state",
            "overwrite"
        ]
    ]
    required_together = [
        [
            "yes",
            "no"
        ]
    ]
    required_one_of = [
        [
            "src",
            "path"
        ]
    ]
    required_if = [
        {
            "state": "merged"
        },
        {
            "state": "replaced"
        },
        {
            "state": "absent"
        }
    ]

# Generated at 2022-06-12 22:57:54.084274
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    from ansible.module_utils.common.removed import remove_deprecated_args
    class TestArgSpecValidator(ArgumentSpecValidator):
        def __init__(self, argument_spec, remove_deprecated_parameters=False):
            super(TestArgSpecValidator, self).__init__(argument_spec)
            self.remove_deprecated_parameters = remove_deprecated_parameters

        def validate(self, parameters):
            result = super(TestArgSpecValidator, self).validate(parameters)
            if self.remove_deprecated_parameters:
                result._validated_parameters = remove_deprecated_args(result._validated_parameters, self.argument_spec)
            return result


# Generated at 2022-06-12 22:58:03.746164
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils.common.warnings import set_option, reset_warning_registry
    from ansible.module_utils._text import to_bytes, to_text
    from io import StringIO
    from ansible.module_utils import basic
    import ansible.module_utils.common.arg_spec as arg_spec
    import ansible.module_utils.common.validation as validation

    set_option('action', 'once')
    reset_warning_registry()
    parameters_input = {'a': 'b'}

    argument_spec_input = {'c': {'type': 'int'}}
    mutually_exclusive_input = [['c', 'd']]
    required_together_input = [['c', 'd']]

# Generated at 2022-06-12 22:58:11.125009
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

    assert result.error_messages == []

    valid_params = result.validated_parameters

    assert valid_params['name'] == 'bo'
    assert valid_params['age'] == 42

# Generated at 2022-06-12 22:58:22.283449
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    """Unit test to test method validate in ModuleArgumentSpecValidator class."""
    # Create instance of argument spec validator
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }
    module_argument_spec_validator = ModuleArgumentSpecValidator(argument_spec)

    # Call method validate of ArgumentSpecValidator class
    parameters = {
        'name': 'bo',
        'age': '42',
    }
    result = module_argument_spec_validator.validate(parameters)

    # Check exception for error messages
    if result.error_messages:
        sys.exit("Validation failed: {0}".format(result.error_messages))

    # Assign validated parameters
    valid_params = result.validated

# Generated at 2022-06-12 22:58:31.614322
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # Test validation of parameters and aliases
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int', 'aliases': ['years', 'old']},
    }

    parameters = {
        'name': 'bo',
        'age': '42',
    }

    result = None
    validator = ModuleArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    assert len(result.errors) == 0

    # Test validation of parameters and aliases
    argument_spec1 = {
        'name': {'type': 'str'},
        'age': {'type': 'int', 'aliases': ['years', 'old']},
    }


# Generated at 2022-06-12 22:58:37.853670
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils.common.warnings import AnsibleModuleDeprecationWarning
    from ansible.module_utils.six import PY2

    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
        'aliases': {'aliases': ['aliases_1', 'aliases_2']},
        'aliases2': {'aliases': 'aliases3'},
    }

    parameters = {
        'name': 'bo',
        'age': '42',
        'aliases': 'aliases_1',
        'aliases2': 'aliases3',
    }

    validator = ModuleArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    assert result.validated_

# Generated at 2022-06-12 22:58:46.844339
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    """
    Retrun value is instance of ArgumentSpecValidator
    """
    args = [{'name': {'type': 'str'}, 'age': {'type': 'int'}}]
    kwargs = {'mutually_exclusive': None,
         'required_together': None,
         'required_one_of': None,
         'required_if': None,
         'required_by': None}
    argument_spec = ModuleArgumentSpecValidator(*args, **kwargs)
    parameters = {'name': 'bo', 'age': '42'}

    return type(argument_spec.validate(parameters)) == ValidationResult

# Generated at 2022-06-12 22:58:49.129695
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    # Test for ArgumentSpecValidator.validate
    # Create and use an instance of ArgumentSpecValidator
    pass



# Generated at 2022-06-12 22:58:57.093230
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    import unittest

    class ValidateTestCase(unittest.TestCase):
        def test__handle_aliases_ConflictError(self):
            import mock
            argument_spec = {'name': {'type': 'str', 'aliases': ['fake']}}
            mutually_exclusive = None
            required_together = None
            required_one_of = None
            required_if = None
            required_by = None
            test = ModuleArgumentSpecValidator(argument_spec, mutually_exclusive,
                                               required_together, required_one_of,
                                               required_if, required_by)
            parameters = {'name': 'bo', 'fake': 2}

# Generated at 2022-06-12 22:59:09.455034
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    """
    Unit test for method validate of class ModuleArgumentSpecValidator.
    """
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'str'},
        'children': {'type': 'list', 'elements': 'str'},
    }

    parameters = {
        'name': 'bo',
        'age': '42',
        'children': ['kim', 'tom'],
    }

    validator = ModuleArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    assert len(result.error_messages) == 2
    assert 'age' in result.error_messages[0]
    assert 'children' in result.error_messages[1]




# Generated at 2022-06-12 22:59:15.994596
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    validator = ArgumentSpecValidator({})
    results = validator.validate({})
    assert results.validated_parameters == {}
    assert results.unsupported_parameters == {}
    assert results.error_messages == []

# Generated at 2022-06-12 22:59:26.570939
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int', 'aliases': ['age_alias']},
    }

    parameters = {
        'name': 'bo',
        'age_alias': 'number'
    }

    validator = ModuleArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    assert result.error_messages == ["The value for age () must be an integer, got <type 'unicode'>. Aliases: age_alias."], \
                                           "Error message is not expected for `age`"

    assert result.unsupported_parameters == set(), \
                                           "No unsupported parameters are expected as `age_alias` is an alias for `age`"


# Generated at 2022-06-12 22:59:36.931102
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }

    mutually_exclusive = ['name', 'age']
    required_together = [['name', 'age']]
    required_one_of = [['name', 'age']]
    required_if = [['name', 'bo', ['age']]]
    required_by = {
        'name': ['age']
    }

    validator = ArgumentSpecValidator(argument_spec,
                                      mutually_exclusive=mutually_exclusive,
                                      required_together=required_together,
                                      required_one_of=required_one_of,
                                      required_if=required_if,
                                      required_by=required_by)

# Generated at 2022-06-12 22:59:39.869507
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # verify ModuleArgumentSpecValidator.validate() calls super.validate()
    called = False
    class ArgumentSpecValidator_validate:
        def validate(self, parameters):
            nonlocal called
            called = True
            return None

    m = ModuleArgumentSpecValidator()
    m.validate(parameters=None, ArgumentSpecValidator_validate=ArgumentSpecValidator_validate)
    assert called

# Generated at 2022-06-12 22:59:47.434880
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    # Mock imports.
    import sys
    import unittest.mock as mock

    import pytest

    # Set up mocks.
    mock_get_legal_inputs = mock.MagicMock(name='get_legal_inputs')
    mock_get_legal_inputs.return_value = []

    mock_set_defaults = mock.MagicMock(name='set_defaults')
    mock_set_defaults.return_value = ()

    mock_list_no_log_values = mock.MagicMock(name='list_no_log_values')
    mock_list_no_log_values.return_value = set()

    mock_get_unsupported_parameters = mock.MagicMock(name='get_unsupported_parameters')
    mock_get_unsupported_parameters.return_

# Generated at 2022-06-12 22:59:56.931941
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils.common.warnings import AnsibleDeprecationWarning

    syntax_error = {
        "name": {
            "required": True,
            "default": "Default Value",
            "aliases": ["name-alias"],
        }
    }

    result = ModuleArgumentSpecValidator(syntax_error).validate({"name": "test"})
    assert '".name" is not of type "str"' in result.errors[0].message
    assert result.errors[0].__class__.__name__ == "AnsibleValidationError"


# Generated at 2022-06-12 23:00:06.248216
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    from ansible.module_utils import basic
    from ansible.module_utils.common.arg_spec import (
        ArgumentSpecValidator,
        ValidationResult,
    )
    from ansible.module_utils.common.parameters import (
        InvalidTypeError,
        InvalidValueError,
        DeprecatedAliasWarning,
    )
    from ansible.module_utils.common.warnings import (
        DeprecatedWarning,
        AnsibleDeprecationWarning,
        AnsibleCollectionWarning,
    )


# Generated at 2022-06-12 23:00:15.907833
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    '''
    Unit test for method validate of class ModuleArgumentSpecValidator
    '''
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'}
    }

    parameters = {
        'name': 'bo',
        'age': '42',
    }

    validator = ModuleArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    assert result.error_messages == [], "failed to validate parameters"
    assert result.validated_parameters == {'name': 'bo', 'age': 42}, "failed to validate parameters"
    assert result.unsupported_parameters == set(), "failed to validate parameters"

# Generated at 2022-06-12 23:00:24.756369
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # test case with alias deprecated
    argument_spec = {
        'name': {'type': 'str', 'aliases': ['my_alias']},
        'age': {'type': 'int'},
    }
    mutually_exclusive = []
    required_together = []
    required_if = []
    required_one_of = []
    required_by = {}
    parameters = {
        'name': 'bo',
        'age': '42',
        'my_alias': 'new_deprecated_value'
    }


# Generated at 2022-06-12 23:00:27.042862
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    """ArgumentSpecValidator.validate() function is tested in unit test ``TestArgSpec``."""
    # No need to test the dummy class
    pass


# Generated at 2022-06-12 23:00:40.004949
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

    assert len(result.error_messages) == 0
    assert result.validated_parameters == {'name': 'bo', 'age': 42}
    assert result.unsupported_parameters == set()
    assert result.errors == AnsibleValidationErrorMultiple()
    assert len(result.error_messages) == 0



# Generated at 2022-06-12 23:00:50.186371
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

    assert result.error_messages == []

    valid_params = result.validated_parameters

    assert 'name' in valid_params
    assert valid_params['name'] == 'bo'
    assert isinstance(valid_params['name'], str)

    assert 'age' in valid_params
    assert valid_params['age'] == 42
    assert isinstance(valid_params['age'], int)



# Generated at 2022-06-12 23:01:01.204945
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():

    # define argument_spec
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
        'gender': {'type': 'str', 'choices': ['male', 'female']},
        'address': {'type': 'dict', 'options': {
            'city': {'type': 'str', 'default': 'beijing'},
            'country': {'type': 'str'}
        }},
        'result': {'type': 'list', 'elements': 'str'}
    }


# Generated at 2022-06-12 23:01:09.336887
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():

    import unittest

    class TestModuleArgumentSpecValidator(unittest.TestCase):

        def setUp(self):
            self.validator = ModuleArgumentSpecValidator(
                {'a': {'type': 'bool', 'aliases': ['b']}}
            )

        def test_warn_on_aliases_with_value(self):
            # test that existing module code that uses aliases with value still works
            with self.assertWarns(Warning) as cm:
                result = self.validator.validate({'a': True, 'b': False})
                self.assertEqual(cm.warning.args[0], "Both option 'a' and its alias 'b' are set.")
            self.assertTrue(result.validated_parameters.get('a'))


# Generated at 2022-06-12 23:01:19.689496
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():

    from ansible.module_utils.common.collections import is_iterable

    # use a simple argument_spec to test with
    argument_spec = {
        'test_str': {'type': 'str'},
        'test_int': {'type': 'int'},
        'test_list': {'type': 'list'},
        'test_dict': {'type': 'dict'},
        'test_bool': {'type': 'bool', 'default': False},
        'test_path': {'type': 'path'},
    }

    # test parameter

# Generated at 2022-06-12 23:01:30.261384
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    """Unit test for method validate of class ModuleArgumentSpecValidator"""
    from ansible.module_utils import basic
    import warnings

    def test_argument_spec_deprecate():
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter('always')
            argument_spec = basic.AnsibleModule.argument_spec()
            validator = ModuleArgumentSpecValidator(argument_spec)
            validator.validate({'test': 'hello world'})

            assert len(w) == 1
            assert issubclass(w[-1].category, DeprecationWarning)
            assert 'Alias' in str(w[-1].message)
            assert 'is deprecated' in str(w[-1].message)

# Generated at 2022-06-12 23:01:37.591735
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    params = dict(
        name = 'bo',
        age = '42',
    )
    required_together = None
    mutually_exclusive = None
    required_one_of = None
    required_if = None
    required_by = None
    argument_spec = dict(
        name = dict(type='str'),
        age = dict(type='int'),
    )

    validator = ArgumentSpecValidator(argument_spec,
                                      mutually_exclusive=mutually_exclusive,
                                      required_together=required_together,
                                      required_one_of=required_one_of,
                                      required_if=required_if,
                                      required_by=required_by,
                                      )
    result = validator.validate(params)
    print(result.error_messages)

# Generated at 2022-06-12 23:01:40.293943
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    v = ModuleArgumentSpecValidator({'a': {'type': 'int'}}, None, None, None, None, None)
    assert v.validate({'a': 2})

# Generated at 2022-06-12 23:01:46.753097
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

# Generated at 2022-06-12 23:01:55.819176
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

    assert result._validated_parameters['name'] == 'bo'
    assert result._validated_parameters['age'] == 42

    assert isinstance(result.errors, AnsibleValidationErrorMultiple)
    assert "Unsupported parameters" in result.error_messages
    assert not result.errors

    parameters = {
        'name': 'bo',
        'age': 'fortytwo',
    }

    validator = ArgumentSpecValidator(argument_spec)
   

# Generated at 2022-06-12 23:02:05.743817
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    validator = ModuleArgumentSpecValidator({
        'name': {'type': 'str'},
        'age': {'type': 'int', 'required': True},
        'gender': {'type': 'str'},
        'weight': {'type': 'float'},
    })

    parameters = dict(
        name='bo',
        age='42',
        gender='male',
    )

    result = validator.validate(parameters)

    assert result.errors == []

# Generated at 2022-06-12 23:02:10.604821
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    '''Unit test for method validate of class ModuleArgumentSpecValidator'''
    my_validator = ModuleArgumentSpecValidator()
    parameters = {
        'name': 'bo',
        'age': '42',
    }
    valid_params = my_validator.validate(parameters)
    assert valid_params == parameters

# Generated at 2022-06-12 23:02:21.734781
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    class ValidationPass(Exception):
        '''Thrown when validation passes'''
        pass

    # Create validator for argument spec

# Generated at 2022-06-12 23:02:31.183616
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    argument_spec = {'test_key': {'type': 'str'},
                     'test_key2': {'type': 'str'}}

    parameters = {'test_key': 'test_value',
                  'test_key2': 'test_value2'}

    validator = ModuleArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    assert result.validated_parameters == parameters
    assert result._no_log_values == set()
    assert result._unsupported_parameters == set()
    assert result._deprecations == []
    assert result._warnings == []
    assert result.errors == []
    assert result.error_messages == []

# Generated at 2022-06-12 23:02:37.892254
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    parameter_spec_dict = dict(
        age=dict(type='int', required=True),
        name=dict(type='str', required=True),
    )
    return_dict = dict(
        age='42',
        name='John',
    )
    validator = ArgumentSpecValidator(parameter_spec_dict)
    result = validator.validate(return_dict)
    assert bool(result.error_messages) == False
    assert result.validated_parameters == {'age': 42, 'name': 'John'}

# Generated at 2022-06-12 23:02:47.850444
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils.common import ANSIBLE_ARGS
    from ansible.module_utils._text import to_bytes

    argument_spec = {}
    parameters = {}

    # Test for deprecate
    validator = ModuleArgumentSpecValidator(argument_spec)
    validator.argument_spec._deprecations = [{
        'name': 'b',
        'version': '1.0.0',
        'date': '0',
        'collection_name': 't'
    }]


    # Test for warn
    validator = ModuleArgumentSpecValidator(argument_spec)
    validator.argument_spec._warnings = [{
        'option': 'b',
        'alias': 'c'
    }]

    # Test for errors
    validator = ModuleArgumentSpecValidator

# Generated at 2022-06-12 23:02:54.109875
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    #Create a ArgumentSpecValidator object for testing
    argument_spec = {'name': {'type': 'str'}, 'age': {'type': 'int'}, }
    mutually_exclusive = None
    required_together = None
    required_one_of = None
    required_if = None
    required_by = None
    validator = ModuleArgumentSpecValidator(argument_spec, mutually_exclusive,
                                            required_together, required_one_of, required_if, required_by)
    parameters = {'name': 'bo', 'age': '42', }
    result = validator.validate(parameters)
    print(result)

# Generated at 2022-06-12 23:02:57.382645
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():
    argument_spec = dict(
        name=dict(type='str'),
        age=dict(type='int'),
    )
    validator = ArgumentSpecValidator(argument_spec)
    assert validator.argument_spec == argument_spec

# Generated at 2022-06-12 23:03:05.844255
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils.common.arg_spec import ModuleArgumentSpecValidator
    # given
    arg_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }
    parameters = {
        'name': 'bo',
        'age': '42'
    }
    # when
    validator = ModuleArgumentSpecValidator(arg_spec)
    result = validator.validate(parameters)
    # then
    assert isinstance(result, ValidationResult)
    assert isinstance(result.errors, AnsibleValidationErrorMultiple)


# Generated at 2022-06-12 23:03:11.784146
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # test for alias deprecation warning
    validator = ModuleArgumentSpecValidator({'new': {'type': 'str', 'aliases': ['old']}})
    validator.validate({'new': 'foo', 'old': 'bar'})
    # test for alias conflict warning
    validator = ModuleArgumentSpecValidator({'new': {'type': 'str', 'aliases': ['old']}})
    validator.validate({'new': 'foo', 'old': 'foo'})

# Generated at 2022-06-12 23:03:16.649404
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():
    assert(isinstance(ArgumentSpecValidator({}), ArgumentSpecValidator))

# Generated at 2022-06-12 23:03:26.575472
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    validator = ModuleArgumentSpecValidator({'status': {'type': 'bool', 'aliases': ['enable']}})
    assert validator is not None

    # check deprecations and warnings with aliases
    result = validator.validate({'status': True, 'enable': False})
    assert result is not None
    assert result.validated_parameters == {'status': False}
    assert len(result._deprecations) == 1
    assert len(result._warnings) == 1
    assert result._deprecations[0]['name'] == 'enable'
    assert result._warnings[0]['option'] == 'status'
    assert result._warnings[0]['alias'] == 'enable'

    # no deprecations nor warnings with aliases disabled

# Generated at 2022-06-12 23:03:35.052321
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    # Suppress AnsibleDeprecationWarning:
    #    alias_warnings = []
    #    alias_deprecations = []
    with warnings.catch_warnings():
        warnings.filterwarnings('ignore', category=AnsibleDeprecationWarning)
        argument_spec = {
            'name': {'type': 'str'},
            'age': {'type': 'int'},
            'sex': {'type': 'str', 'default': 'M', 'choices': ['M', 'F']},
            'pets': {'type': 'dict', 'required': True, 'elements': 'str'},
            'aliases': {'type': 'str', 'aliases': ['alias']}
        }

# Generated at 2022-06-12 23:03:46.203956
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    mutually_exclusive = [
        ['a', 'b'],
        ['c', 'd'],
        'cd',
    ]
    required_together = [
        ['one', 'two'],
        ['three', 'four'],
        'threefour',
    ]
    required_one_of = [
        ['one', 'two'],
        ['three', 'four'],
        'threefour',
    ]
    required_if = [
        ['one', 'two', ['threefour']],
        ['three', 'four', 'threefour'],
        ['threefour', 'three', 'four'],
    ]
    required_by = {
        'one': ['threefour'],
        'two': 'threefour',
    }


# Generated at 2022-06-12 23:03:55.480858
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    """Unit test for method validate of class ArgumentSpecValidator"""

    from ansible.module_utils.six import PY3

    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
        'stats': {
            'type': 'dict',
            'options': {
                'stat1': {'type': 'int'},
                'stat2': {'type': 'int'},
                'stat3': {'type': 'int'},
            },
            'default': {'stat1': 1, 'stat2': 2, 'stat3': 3}
        }
    }

    mutually_exclusive = [
        ['name', 'age'],
        ['age', 'stats.stat1'],
    ]


# Generated at 2022-06-12 23:04:02.752243
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    # Initialize validated_parameters to be empty
    validated_parameters = {}
    # Initialize actual_result to be empty
    actual_result = None
    # Initialize exception_thrown to be False
    exception_thrown = False
    
    # Try to validate the parameters
    try:
        validator = ArgumentSpecValidator(argument_spec=None)
        actual_result = validator.validate(validated_parameters)
    except Exception:
        # If any exception is thrown, then set exception_thrown to be True
        exception_thrown = True
    
    # Verify if validate() method of ArgumentSpecValidator class throws any exception
    assert exception_thrown == False
    
    # Verify if the validated parameters is equal to the validated_parameters input
    assert actual_result.validated_parameters == validated_param

# Generated at 2022-06-12 23:04:09.137710
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():

    params = {'name': 'bo', 'age': '42'}
    argument_spec = {'name': {'type': 'str'},
                     'age': {'type': 'int'}}

    validator = ArgumentSpecValidator(argument_spec)
    r = validator.validate(params)
    assert(isinstance(r, ValidationResult))
    assert(not r.error_messages)
    assert(r.validated_parameters == {'age': 42, 'name': 'bo'})

# Generated at 2022-06-12 23:04:17.132030
# Unit test for method validate of class ModuleArgumentSpecValidator

# Generated at 2022-06-12 23:04:22.040748
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    param_data = {
        'name': 'bo',
        'age': 42,
    }
    param_vaild = {
        'name': 'bo',
        'age': '42',
    }
    argspec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }
    validator = ArgumentSpecValidator(argspec)
    invalid_params = validator.validate(param_data)
    valid_params = validator.validate(param_vaild)
    assert invalid_params is not None
    assert valid_params is not None
    assert invalid_params.validated_parameters == valid_params.validated_parameters

# Generated at 2022-06-12 23:04:32.342808
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():

    def_arg_spec = {'no_log': {'type': 'bool', 'default': False, 'no_log': True}}
    def_arg_spec_no_log = {'no_log': {'type': 'bool', 'default': False}}
    parameters = {'no_log': True}
    parameters_no_log = {'no_log': True}

    validator = ModuleArgumentSpecValidator(def_arg_spec)
    result = validator.validate(parameters)
    assert id(result) != id(parameters)
    assert result.validated_parameters['no_log'] == True
    assert result._no_log_values == set([True])

    validator = ModuleArgumentSpecValidator(def_arg_spec_no_log)

# Generated at 2022-06-12 23:04:49.037292
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # given
    argument_spec = {
        'valid_param_name': {'type': 'str', 'required': True, 'fallback': ('other_valid_param', 'another_valid_param')},
        'other_valid_param': {'type': 'str'},
        'another_valid_param': {'type': 'str'},
    },
    mutually_exclusive = [
     ['other_valid_param', 'another_valid_param']
    ]
    validator = ModuleArgumentSpecValidator(argument_spec, mutually_exclusive=mutually_exclusive)

    # when
    parameters = {
        'not_valid_param': 'should raise an error',
        'valid_param_name': 'some_valid_param_value'
    }
    result = validator.validate(parameters)

    #

# Generated at 2022-06-12 23:04:55.865363
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
    assert result.validated_parameters == {
        'name': 'bo',
        'age': 42,
    }
    assert result.unsupported_parameters == set()
    assert result.validated_parameters == {
        'name': 'bo',
        'age': 42,
    }
    assert result.error_messages == []

# Generated at 2022-06-12 23:05:06.860893
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # Initialize mock objects
    from ansible.module_utils.six import iteritems
    from ansible.module_utils.common.text.converters import to_native
    from ansible.module_utils.common.validation import check_mutually_exclusive, check_required_arguments

# Generated at 2022-06-12 23:05:15.525369
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():

    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
        'legacy': {'type': 'bool', 'required': False, 'aliases': ['value']},
        'nested': {'type': 'dict', 'options': {
            'first': {'type': 'str'},
            'second': {'type': 'list', 'elements': 'str'},
        }}
    }

    parameters = {
        'name': 'bo',
        'age': '42',
        'nested': {
            'first': 'foo',
            'second': ['bar', 'baz'],
        }
    }

    validator = ArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)


# Generated at 2022-06-12 23:05:22.067858
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

    assert result.error_messages == []
    assert result.validated_parameters == {'name': 'bo', 'age': 42}
    assert result.unsupported_parameters == set()

# Generated at 2022-06-12 23:05:32.561151
# Unit test for method validate of class ModuleArgumentSpecValidator

# Generated at 2022-06-12 23:05:41.274852
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    spec = dict(
        a=dict(),
        b=dict(aliases=['c']),
        d=dict(),
    )
    val = ModuleArgumentSpecValidator(spec)
    val._deprecations = [{'name': 'a', 'version': '1.2.3', 'date': '2020-03-23'}] # pylint: disable=protected-access
    val._warnings = [{'option': 'a', 'alias': 'b'}] # pylint: disable=protected-access
    val._valid_parameter_names = set() # pylint: disable=protected-access

# Generated at 2022-06-12 23:05:48.046006
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils.common.arg_spec import ModuleArgumentSpecValidator

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

    assert result.error_messages == []
    assert result.validated_parameters == {'name': 'bo', 'age': 42}

# Generated at 2022-06-12 23:05:56.765940
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    class _ModuleArgumentSpecValidator(ModuleArgumentSpecValidator):
        def __init__(self, *args, **kwargs):
            super(_ModuleArgumentSpecValidator, self).__init__(*args, **kwargs)
            self._valid_parameter_names = set()
            self.argument_spec = dict()

        def _deprecate(self, *args, **kwargs):
            pass

        def _warn(self, *args, **kwargs):
            pass

    class _ValidationResult(ValidationResult):
        def __init__(self, parameters=None, validated_parameters=None):
            ValidationResult.__init__(self, parameters)
            self._validated_parameters = validated_parameters

    v = _ModuleArgumentSpecValidator()
    p = dict()

# Generated at 2022-06-12 23:06:04.946520
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    '''
    Unit Tests for method `validate` of class `ArgumentSpecValidator`
    '''

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

    assert result.validated_parameters == {
        'name': 'bo',
        'age': 42,
    }

if __name__ == '__main__':
    test_ArgumentSpecValidator_validate()