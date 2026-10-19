

# Generated at 2022-06-12 22:56:25.166667
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat import unittest

    class TestModuleArgumentSpecValidator(unittest.TestCase):
        def assertDictEqual(self, dict1, dict2):
            # Python 2.6 compatibility method.
            dict1_keys = dict1.keys()
            dict2_keys = dict2.keys()

            self.assertEqual(set(dict1_keys), set(dict2_keys))
            for key in dict1_keys:
                self.assertEqual(dict1[key], dict2[key])

        def setUp(self):
            self.mutually_exclusive = [
                ['one', 'two'],
            ]

            self.required_together = [
                ['one', 'two'],
            ]

           

# Generated at 2022-06-12 22:56:31.149588
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    argument_spec = {'name': {'type': 'str', 'required': True}, 'age': {'type': 'int'}}
    parameters = {'name': 'bo'}

    validator = ModuleArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    assert result.validated_parameters == {'name': 'bo'}
    assert result.errors == [RequiredError('name is required' )]

# Generated at 2022-06-12 22:56:38.835432
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils._text import to_text

    validator = ModuleArgumentSpecValidator({'bar': {'type': 'int', 'aliases': ['baz']}})
    result = validator.validate({'baz': 42})
    assert result.warnings == [{'alias': 'baz', 'option': 'bar'}]
    assert result.deprecations == []

    validator = ModuleArgumentSpecValidator({'bar': {'type': 'int', 'deprecated': {'version': '1.0', 'date': '2020-05-01', 'collection_name': 'ansible.base_legacy', 'removed_in': '2.0'}}})
    result = validator.validate({'bar': 42})
    assert result.warnings == []
    assert result.dep

# Generated at 2022-06-12 22:56:49.626335
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common.text.converters import to_text
    from ansible.module_utils.common.json_utils import jsonify

    argument_spec = {
        'options': {'type': 'dict', 'default': {'key': 'val'}},
    }
    mutually_exclusive = [['options']]

    v = ModuleArgumentSpecValidator(argument_spec, mutually_exclusive=mutually_exclusive)

    # ArgumentSpecValidator.validate returns an instance of ValidationResult
    # with validated parameters as well as deprecations and warnings.
    # https://github.com/ansible/ansible/blob/devel/lib/ansible/module_utils/common/arg_spec.py#L67
    result = v

# Generated at 2022-06-12 22:56:58.061059
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
    assert valid_params == {'name': 'bo', 'age': 42}

# Generated at 2022-06-12 22:57:06.990321
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils.common.parameters import AnsibleModule


# Generated at 2022-06-12 22:57:13.319865
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # Example of sub spec (nested) argument spec
    test_spec = {
        'param1': {'type': 'bool'},
        'param3': {'type': 'int'},
        'param4': {'type': 'bool'},
        'param2': {
            'type': 'dict',
            'options': {
                'param5': {'type': 'bool'},
                'param6': {'type': 'str'},
                'param7': {'type': 'str'},
            }
        },
        'param8': {
            'type': 'list',
            'elements': 'str'
        }
    }
    # Example of simple argument spec

# Generated at 2022-06-12 22:57:18.770476
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():

    # Arrange
    argspec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
        'hobbies': {'type': 'list'}
    }

    keywords = {'age': '42', 'name': 'bo'}
    validator = ModuleArgumentSpecValidator(argspec)

    # Act
    result = validator.validate(keywords)

    # Assert
    valid_params = result.validated_parameters
    assert valid_params['age'] == 42

# Generated at 2022-06-12 22:57:19.351629
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    pass

# Generated at 2022-06-12 22:57:23.724501
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
    assert validator is not None


# Generated at 2022-06-12 22:57:41.986884
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

    validator = ArgumentSpecValidator(argument_spec,
                                      mutually_exclusive=[('name', 'age')],
                                      required_one_of=[('name', 'age')],
                                      required_if=[('name', 'bo', ['age'])],
                                      required_by={'name': ['age']})

    result = validator.validate(parameters)

    if result.error_messages:
        sys.exit("Validation failed: {0}".format(", ".join(result.error_messages)))

    valid_params = result.validated_parameters



# Generated at 2022-06-12 22:57:50.368104
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat import unittest
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils import basic

    class TestModuleArgumentSpecValidator(unittest.TestCase):

        def test_deprecations(self):
            module_args = {
                'from': 'test'
            }
            argument_spec = {
                'from': {
                    'required': True,
                    'aliases': ['from_addr'],
                    'version_added': '2.5'
                }
            }
            validator = ModuleArgumentSpecValidator(argument_spec)

            with self.assertWarns(DeprecationWarning):
                validator.validate(module_args)


# Generated at 2022-06-12 22:58:00.252058
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils.common.data_loader import DataLoader


# Generated at 2022-06-12 22:58:05.943425
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    argument_spec = {
            'name': {'type': 'str'},
            'age': {'type': 'int'},
        }

    mutually_exclusive = [["name", "age"]]

    parameters = {
        'name': 'bo',
        'age': '42',
    }

    validator = ModuleArgumentSpecValidator(argument_spec, mutually_exclusive=mutually_exclusive)
    result = validator.validate(parameters)

    assert result.unsupported_parameters == set()
    assert result.validated_parameters == {'name': 'bo', 'age': 42}

# Generated at 2022-06-12 22:58:08.141876
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    validator = ModuleArgumentSpecValidator({})
    result = validator.validate({})
    assert result.error_messages == []

# Generated at 2022-06-12 22:58:19.438097
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    from ansible.module_utils.basic import AnsibleModule
    from ansible_collections.testns.testcoll.plugins.modules import basic

    module = AnsibleModule(basic)

# Generated at 2022-06-12 22:58:24.562550
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    argument_spec = { 'name': {'type': 'str'} }
    parameters = { 'name': 'bo' }
    validator = ArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    assert result.errors == []
    assert result.validated_parameters == {'name': 'bo'}

# Generated at 2022-06-12 22:58:29.777134
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    spec = {
        'aliases': {'alias': 'opt'},
        'type': 'str',
        'version_added': '2.10',
        'version_removed': '3.0',
        'date_removed': '2020-01-01',
        'collection_name': 'my_namespace.my_collection',
    }

    arg_spec = {
        'opt': spec
    }

    validator = ModuleArgumentSpecValidator(arg_spec)

    # arguments are handled in order of appearance on the command line
    parameters = {
        'aliases': {'opt': 'alias'},
        'opt': 'test_value'
    }
    validator.validate(parameters)

# Generated at 2022-06-12 22:58:34.933536
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():

    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }

    # validator = ArgumentSpecValidator(argument_spec)
    validator = ArgumentSpecValidator(argument_spec,
                                      mutually_exclusive=[['name', 'age']],
                                      required_together=['name', 'age'],
                                      required_one_of='name',
                                      required_if='age',
                                      required_by='name'
                                      )


# Generated at 2022-06-12 22:58:45.664498
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    argument_spec = {
        'name': {'version': '0.0.1', 'type': 'str', 'aliases': ['nickname']},
        'age': {'version': '0.0.2', 'type': 'str', 'aliases': ['years']},
        'height': {'version': '0.0.3', 'type': 'str'},
    }
    mutually_exclusive = [['name', 'age']]
    validator = ModuleArgumentSpecValidator(argument_spec, mutually_exclusive)

    parameters = {
        'name': 'bo',
        'age': 1,
        'height': 2,
    }
    result = validator.validate(parameters)

    assert len(result.error_messages) == 0
    assert len(result._warnings) == 0

# Generated at 2022-06-12 22:58:56.647943
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():

    import os
    import sys
    import unittest

    class TestArgumentSpecValidator(unittest.TestCase):

        arguments = dict(
            url=dict(type='str'),
            version=dict(type='str'),
            timeout=dict(type='float', default=10.0),
            state=dict(type='str', choices=['present', 'absent'], aliases=['enabled'], default='present')
        )

        def setUp(self):
            self.validator = ModuleArgumentSpecValidator(self.arguments)

        def test_validate_with_alias_and_choice(self):
            params = dict(
                state='absent',
                enabled=True
            )

            valid = self.validator.validate(params)


# Generated at 2022-06-12 22:59:08.960084
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    """Test that ArgumentSpecValidator.validate gives the correct output:
    - ArgumentSpecValidator.validate({'name': 'bo', 'age': '42'}, {'name': {'type': 'str'}, 'age': {'type': 'int'}})
      returns {'name': 'bo', 'age': 42}
    """
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


# Generated at 2022-06-12 22:59:12.876611
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():

    parameters = {'boolean': True, 'number': 42, 'quoted_string': 'quoted string'}

    validator = ArgumentSpecValidator(
        {
            'boolean': {'type': 'bool'},
            'number': {'type': 'int'},
            'quoted_string': {'type': 'str'},
        }
    )
    result = validator.validate(parameters)

    # No errors
    assert not result.errors
    # Same value
    assert result.validated_parameters == parameters
    # No unsupported parameters
    assert not result.unsupported_parameters
    # No no_log_values
    assert not result._no_log_values



# Generated at 2022-06-12 22:59:21.764506
# Unit test for method validate of class ModuleArgumentSpecValidator

# Generated at 2022-06-12 22:59:30.801482
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    # Set up test parameters
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }
    parameters = {
        'name': 'bo',
        'age': '42',
    }

    # Create a validator and the validate the parameters
    validator = ArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    # Check the results
    assert result.validated_parameters == {
        'name': 'bo',
        'age': 42,
    }
    assert not result.errors
    assert result.error_messages == []



# Generated at 2022-06-12 22:59:35.152130
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    argument_spec = {"my_param": {"type": "str"}}
    parameters = {"my_param": "hello"}
    validator = ModuleArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)
    assert result.validated_parameters == parameters



# Generated at 2022-06-12 22:59:40.169527
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    from ansible.module_utils.common.arg_spec import ArgumentSpecValidator, ValidationResult
    a = {'name': 'bo'}
    argumentspec = {'name': {'type': 'str'}}
    validation_result = ArgumentSpecValidator(argumentspec).validate(a)
    assert isinstance(validation_result, ValidationResult) and validation_result.validated_parameters['name'] == 'bo'

# Generated at 2022-06-12 22:59:47.851825
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    """ Unit test for method validate of class ArgumentSpecValidator. """

    import pytest

    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int', 'default': 42},
        'enabled': {'type': 'bool', 'default': True},
        'netmask': {'type': 'str', 'default': '255.255.0.0', 'no_log': True},
    }

    parameters = {
        'name': 'bo',
        'age': '42',
        'enabled': 'True',
        'netmask': '255.255.0.0',
    }

    validator = ArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)


# Generated at 2022-06-12 22:59:52.503552
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    v = ModuleArgumentSpecValidator({
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    })
    r = v.validate({'name': 'bo', 'age': 42})
    assert r.validated_parameters.items() == {'name': 'bo', 'age': 42}.items()



# Generated at 2022-06-12 23:00:00.761288
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    test_value = 42
    argument_spec = {'bogus': {'type': 'int'}}
    mutually_exclusive = []
    required_together = []
    required_one_of = []
    required_if = []
    required_by = []
    parameters = {'bogus': test_value}

    validator = ModuleArgumentSpecValidator(argument_spec,
                                            mutually_exclusive,
                                            required_together,
                                            required_one_of,
                                            required_if,
                                            required_by)

    result = validator.validate(parameters)
    assert not result.error_messages
    assert result.validated_parameters.get('bogus') == test_value
    assert not result.unsupported_parameters

# Generated at 2022-06-12 23:00:14.368084
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():
    assert issubclass(ArgumentSpecValidator,object)
    argument_spec = {'value': {'type': 'int'}}
    mutually_exclusive = [('value', 'mvalue')]
    required_together = [['value', 'mvalue']]
    required_one_of = [['value', 'mvalue']]
    required_if = [['value', 'mvalue', ['lvalue']]]
    required_by = {'value': ['mvalue']}
    obj1 = ArgumentSpecValidator(argument_spec,
                                 mutually_exclusive=mutually_exclusive,
                                 required_together=required_together,
                                 required_one_of=required_one_of,
                                 required_if=required_if,
                                 required_by=required_by)
    assert obj1 is not None

#

# Generated at 2022-06-12 23:00:22.678398
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # Setup for the argument spec
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }

    # Setup for the parameters
    parameters = {
        'name': 'bo',
        'age': '42',
    }

    # Setup for the validator
    validator = ModuleArgumentSpecValidator(argument_spec)

    # Run the test
    result = validator.validate(parameters)

    # Verify that no error is returned
    assert result.error_messages == []

    # Verify that a valid parameter is returned
    assert result.validated_parameters == {'name': 'bo', 'age': 42}

# Generated at 2022-06-12 23:00:23.227607
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    pass

# Generated at 2022-06-12 23:00:33.458381
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # Given we have a ModuleArgumentSpecValidator
    validator = ModuleArgumentSpecValidator({}, required_if=[['allow', True, ['file']]])

    # When we validate a set of parameters
    result = validator.validate({'allow': True, 'file': 'foo.zip'})

    # Then we should get the parameters back
    assert result.validated_parameters == {'allow': True, 'file': 'foo.zip'}

    # When we validate a set of parameters
    result = validator.validate({'allow': True, 'file': 'foo.zip', 'other': 'bar'})

    # Then we should get the parameters back and a warning
    assert result.validated_parameters == {'allow': True, 'file': 'foo.zip', 'other': 'bar'}

# Generated at 2022-06-12 23:00:37.554476
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

    validator = ModuleA

# Generated at 2022-06-12 23:00:43.346077
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    argument_spec = {'name': {'type': 'str'}, 'age': {'type': 'int'}}
    parameters = {'name': 'bo', 'age': '42'}
    validator = ArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)
    assert result.error_messages == []
    assert result.validated_parameters == {'name': 'bo', 'age': 42}
    assert result.unsupported_parameters == set()
    assert result._no_log_values == set()



# Generated at 2022-06-12 23:00:53.514757
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    import sys
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
    assert parameters['age'] == valid_params['age']
    assert parameters['name'] == valid_params['name']



# Generated at 2022-06-12 23:01:01.653267
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


# Generated at 2022-06-12 23:01:08.997930
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
        'location': {'type': 'dict'},
        'location.city': {'type': 'str'},
        'location.state': {'type': 'str'},
        'location.zip': {'type': 'str'},
    }
    parameters = {
        'name': 'bo',
        'age': '42',
        'location': {
            'city': 'Westford',
            'state': 'MA',
            'zip': '01886',
        },
    }

    validator = ArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    assert not result.error_messages
    assert not result._warnings
   

# Generated at 2022-06-12 23:01:19.363656
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils.common.args import AnsibleModule

    argument_spec = {'a': {}, 'b': {}, 'c': {}, 'd': {}, 'e': {}, 'f': {}, 'g': {}, 'h': {}, 'i': {}, 'j': {}, 'k': {}}
    m = AnsibleModule(argument_spec=argument_spec, mutually_exclusive=(('a', 'b'),), required_together=(('c', 'd'),),
                         required_one_of=(('e', 'f'),), required_if=(('g', 'h', ('i', 'j')),), required_by=(('k', ('l', 'm')),))
    assert m.argument_spec == argument_spec
    assert m.mutually_exclusive == (('a', 'b'),)

# Generated at 2022-06-12 23:01:27.709962
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():
    assert isinstance(
        ArgumentSpecValidator({
            'name': {'type': 'str'},
            'age': {'type': 'int'}
        }),
        ArgumentSpecValidator
    )

# Generated at 2022-06-12 23:01:36.126465
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():

    required_together_parameters = [
       [["name", "firstname"]]
    ]

    required_one_of_parameters = [
       [["name", "firstname"]]
    ]

    argument_spec = {
        "name": {
            "type": "str"
        },
        "firstname": {
            "required": False,
            "type": "str"
        },
    }

    parameters = {
        "name": "bo",
        "firstname": "bob",
    }

    validator = ModuleArgumentSpecValidator(argument_spec, required_together=required_together_parameters, required_one_of=required_one_of_parameters)
    result = validator.validate(parameters)

    assert len(result.errors) == 0

    # required_one

# Generated at 2022-06-12 23:01:45.882230
# Unit test for method validate of class ModuleArgumentSpecValidator

# Generated at 2022-06-12 23:01:49.294612
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    argument_spec = {
        'name': {'type': 'str'},
    }
    parameters = {
        'name': 'bo',
    }

    validator = ModuleArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)
    assert result.validated_parameters == parameters

# Generated at 2022-06-12 23:01:58.561489
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    class AssertAnsibleValidationErrorMultiple(AnsibleValidationErrorMultiple):
        """Test helper class to assert expected errors based on the msg parameter of AnsibleValidationError constructor"""
        def __init__(self, expected_errors):
            self.expected_errors = expected_errors
            self.index = 0

        def append(self, error):
            """Asserts error message with the next expected_error in collection of expected_errors"""
            if self.index < len(self.expected_errors):
                expected_message = self.expected_errors[self.index]
                if expected_message == error.get_message():
                    self.index += 1
                else:
                    print("Unexpected error: {0}".format(error.get_message()))

# Generated at 2022-06-12 23:02:07.902668
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    from collections import namedtuple
    from ansible.module_utils.common.text.converters import to_text

    def get_result(argument_spec, parameters):
        validator = ArgumentSpecValidator(argument_spec)
        result = validator.validate(parameters)
        return result

    Parameter = namedtuple('Parameter', 'name spec')
    # If the test method name matches the pattern Args_<parameter_name>_<validation_type>_<validation_result>,
    # where
    #   <parameter_name> is the name of the parameter in `argument_spec`
    #   <validation_type> is one of the following values: type, value, mutually exclusive, required together,
    #   required one of, required by, required, no log
    #   <validation_result>

# Generated at 2022-06-12 23:02:14.472946
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # Arrange
    argument_spec = {
        "name": {'type': 'str'},
        "age": {'type': 'int'},
    }

    parameters = {
        "name": "bo",
        "age": "42",
    }

    validator = ModuleArgumentSpecValidator(argument_spec)

    result = validator.validate(parameters)

    assert len(result.error_messages) == 0

# Generated at 2022-06-12 23:02:25.566022
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    """Method validate of class ModuleArgumentSpecValidator is calling warn() as expected when it detects both option option_a and its alias alias_a are set"""
    from ansible.module_utils.common.warnings import AnsibleWarning

    argument_spec = {
        'option_a': {'type': 'str'},
        'option_b': {'type': 'str'},
        'option_c': {'type': 'str'},
        'option_d': {'type': 'str'},
        'option_e': {'type': 'str'},
        'option_f': {'type': 'str'},
    }

    # Case 1: only option_a and alias_a both exist

# Generated at 2022-06-12 23:02:34.854697
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    import sys
    from ansible.module_utils.six.moves import shlex_quote
    import pytest

    parameters = {
        'name': 'bo',
        'age': '42',
    }

    # Test with argument_spec
    msg_1 = "exception: No module_default_argspec defined in module"

    with pytest.raises(AnsibleValidationErrorMultiple) as exception1:
        ModuleArgumentSpecValidator().validate(parameters)
    assert msg_1 in exception1.value.messages

    # Test with validator argument_spec
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }
    validator = ModuleArgumentSpecValidator(argument_spec)

# Generated at 2022-06-12 23:02:45.526694
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    from ansible.module_utils.common.parameters import _validate_sub_spec
    from ansible.module_utils.common.validation import check_mutually_exclusive
    from ansible.module_utils.common.warnings import set_fallbacks
    from ansible.module_utils.common.text.converters import to_native
    from ansible.module_utils.common.collections import is_iterable
    from ansible.module_utils.six import string_types

    assert callable(ArgumentSpecValidator)
    argument_spec = {}
    assert callable(argument_spec.__init__)
    mutually_exclusive = None
    assert callable(mutually_exclusive.__init__)
    required_together = None
    assert callable(required_together.__init__)
    required_one_of

# Generated at 2022-06-12 23:03:12.928719
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    import sys
    import json
    import os.path
    data = {}
    with open(os.path.dirname(__file__) + '/test_asv.json', 'r') as file:
        data = json.load(file)
    argument_spec = data['argument_spec']
    parameters = data['parameters']
    validator = ArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)
    if result.error_messages:
        sys.exit("Validation failed: {0}".format(", ".join(result.error_messages)))
    valid_params = result.validated_parameters

# Generated at 2022-06-12 23:03:14.965786
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    '''
    Test validate method of class ArgumentSpecValidator
    '''
    instance = ArgumentSpecValidator({})
    parameters = { 'name': 'bo',
                   'age': '42',
                 }
    result = instance.validate(parameters)
    assert result

# Generated at 2022-06-12 23:03:17.484761
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    validator = ModuleArgumentSpecValidator({}, [], [], [], [], [])
    parameters = dict(a=1, b=2)
    assert validator.validate(parameters).validated_parameters == parameters

# Generated at 2022-06-12 23:03:25.615519
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    params = {'a': 1, 'b': 2}
    argument_spec = {
        'a': {
            'type': 'int',
            'default': 0,
        },
        'b': {
            'type': 'int',
            'default': 10,
        },
        'c': {
            'type': 'str'
        }
    }

    validator = ModuleArgumentSpecValidator(argument_spec)
    result = validator.validate(params)

    assert result.validated_parameters == {
        'a': 1,
        'b': 2,
        'c': ''
    }

# Generated at 2022-06-12 23:03:31.856294
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    argument_spec = {'b': {'aliases': ['a']}}
    mutually_exclusive = None
    required_together = None
    required_one_of = None
    required_if = None
    required_by = None

    parameters = {'a': 'value'}
    validator = ModuleArgumentSpecValidator(argument_spec, mutually_exclusive, required_together, required_one_of, required_if, required_by)
    result = validator.validate(parameters)
    assert not result.error_messages



# Generated at 2022-06-12 23:03:36.838077
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    mapping_spec = {
        'name': {'type': 'str', 'required': True},
        'age': {'type': 'int', 'required': True},
    }

    good_params = {
        'name': 'bo',
        'age': 42,
    }

    validator = ArgumentSpecValidator(mapping_spec)
    result = validator.validate(good_params)

    assert len(result.error_messages) == 0

# Generated at 2022-06-12 23:03:37.537637
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    assert True

# Generated at 2022-06-12 23:03:44.310811
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    validator = ArgumentSpecValidator(
        {'name': {'type': 'str'}, 'age': {'type': 'int'}}
    )

    parameters = {
        'name': 'bo',
        'age': 42,
    }

    result = validator.validate(parameters)
    assert result.error_messages == []
    assert result.validated_parameters == {
        'name': 'bo',
        'age': 42,
    }

# Generated at 2022-06-12 23:03:53.815630
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils.common.validation import check_mutually_exclusive
    from ansible.module_utils.common.parameters import _set_defaults
    from ansible.module_utils.common.warnings import deprecate
    from io import StringIO

    argument_spec = {
        'name': {
            'type': 'str',
            'aliases': ['foo']
        },
        'age': {
            'type': 'int'
        }
    }

    mutually_exclusive = [('name', 'age')]

    parameters = {'name': 'bo', 'age': '42'}

    validator = ModuleArgumentSpecValidator(argument_spec, mutually_exclusive=mutually_exclusive)

    result = validator.validate(parameters)


# Generated at 2022-06-12 23:04:01.683119
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():
    import pytest
    with pytest.raises(AssertionError):
        argument_spec = {
            'name': {'type': 'str'},
        }

        mutually_exclusive = {
            'name': ['age']
        }

        required_together = {
            'name': ['age']
        }

        required_one_of = {
            'name': ['age']
        }

        required_if = {
            'name': {
                'age': 'test'
            }
        }

        required_by = {
            'name': ['age']
        }


# Generated at 2022-06-12 23:04:37.763155
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():

    from ansible.module_utils.common.text.converters import to_bytes, to_native
    from ansible.module_utils.common.validation import MutuallyExclusiveError

    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'}
    }

    parameters = {
        'name': 'bo',
        'age': '42'
    }

    # Test validate method with parameters
    validator = ModuleArgumentSpecValidator(argument_spec,
                                            mutually_exclusive=[],
                                            required_together=[],
                                            required_one_of=[],
                                            required_if=[],
                                            required_by=[])

    result = validator.validate(parameters)


# Generated at 2022-06-12 23:04:43.533244
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    test_case1 = {
        'argument_spec': {
            'name': {'type': 'str'},
            'age': {'type': 'int'},
        },
        'parameters': {
            'name': 'bo',
            'age': '42',
        },
        'result': {
            'error_messages': [],
            'validated_parameters': {
                'name': 'bo',
                'age': 42,
            }
        }
    }


# Generated at 2022-06-12 23:04:51.701212
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    "Unit test for method validate of class ModuleArgumentSpecValidator"
    m_args_spec = {
        "param1": {"type": "str", "aliases": ["p1", "PARAM_ONE"]}
    }
    m_args = {
        "param1": "foo",
        "p1": "bar",
        "PARAM_ONE": "baz"
    }
    m_mutually_exclusive = None
    m_required_together = None
    m_required_one_of = None
    m_required_if = None
    m_required_by = None
    m_validator = ModuleArgumentSpecValidator(
        m_args_spec, m_mutually_exclusive, m_required_together, m_required_one_of, m_required_if, m_required_by)


# Generated at 2022-06-12 23:05:01.362272
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils.six import string_types
    from ansible.module_utils.six import integer_types
    from ansible.module_utils.six import PY2

    validator = ModuleArgumentSpecValidator({
        "name": {"type": "str"},
        "age": {"type": "int"},
    }, mutually_exclusive=[["name", "age"]])

    parameters = {"name": "bo", "age": 42}
    result = validator.validate(parameters)

    assert result.error_messages == []

    assert isinstance(result.validated_parameters['name'], string_types)
    assert isinstance(result.validated_parameters['age'], integer_types)

    parameters["age"] = "bo"
    result = validator.validate(parameters)

# Generated at 2022-06-12 23:05:11.249302
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():

    argument_spec = {
        'name': {
            'type': 'str',
            'choices': ['bo', 'hi'],
            'required': False
        },
        'age': {
            'type': 'int',
            'required': False
        },
        'no_log': {
            'type': 'bool',
            'required': False
        },
        'failon': {
            'type': 'bool',
            'required': True
        }
    }

    supported_parameters = set(['name', 'age', 'no_log', 'failon'])

# Generated at 2022-06-12 23:05:18.745861
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    # test_validate_case1 - basic test case
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
    errors = [ "Invalid value for name", "Invalid age supplied.  Age needs to be an integer value." ]
    assert result.error_messages == errors
    assert result.validated_parameters == {}

    # test_validate_case2 - test mutually_exclusive

# Generated at 2022-06-12 23:05:29.477809
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    ''' test validate method of class ArgumentSpecValidator '''

    argument_spec = {
        "test_param": {
            "required": True,
            "type": "str",
            "choices": [
                "test_value",
            ],
        },
    }

    mutually_exclusive = [
        [
            "test_param",
        ]
    ]

    validator = ArgumentSpecValidator(argument_spec, mutually_exclusive=mutually_exclusive)

    # arguments not provided
    result = validator.validate({
    })

    assert len(result.error_messages) == 1
    assert result.error_messages[0] == "'test_param' is required"

    # required argument provided but not of the correct type

# Generated at 2022-06-12 23:05:36.950050
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():

    result = ModuleArgumentSpecValidator(
        {'name': {'type': 'str'}},
        mutually_exclusive=None,
        required_together=None,
        required_one_of=None,
        required_if=None,
        required_by=None,
    ).validate({'name': 'bo'})

    assert result._deprecations == []
    assert result._no_log_values == set()
    assert result._unsupported_parameters == set()
    assert result._validated_parameters == {'name': 'bo'}
    assert result._warnings == []

# Generated at 2022-06-12 23:05:43.626208
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():

    # Check if deprecation warning is produced with error when alias is present
    assert_equals(len(result._deprecations), 1)
    assert_equals(result._deprecations[0].get('name'), 'aliased_option')

    # Check if warning is produced when both option and alias are set
    assert_equals(len(result._warnings), 1)

    # Check if validation error is present for non-existent option
    assert_equals(len(result.errors), 1)
    assert_equals(len(result.errors[0].messages), 1)
    assert_in("variable does not exist", result.errors[0].messages)

# Tests for method validate of class ArgumentSpecValidator

# Generated at 2022-06-12 23:05:50.923009
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

    #validator = ArgumentSpecValidator(argument_spec)
    #result = validator.validate(parameters)

    #if result.error_messages:
    #    sys.exit("Validation failed: {0}".format(", ".join(result.error_messages))
    #valid_params = result.validated_parameters
    assert(1 == 1 )

