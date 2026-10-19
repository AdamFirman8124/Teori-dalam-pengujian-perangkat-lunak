

# Generated at 2022-06-12 22:56:28.941519
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    from collections import OrderedDict
    from ansible.module_utils.common.arg_spec import ArgumentSpecValidator
    from ansible.module_utils.common.text.converters import to_text
    from ansible.module_utils.common.validation import check_mutually_exclusive


# Generated at 2022-06-12 22:56:34.712841
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # arrange
    argument_spec = {}
    mutually_exclusive = None
    required_together = None
    required_one_of = None
    required_if = None
    required_by = None
    validator = ModuleArgumentSpecValidator(argument_spec, mutually_exclusive, required_together, required_one_of, required_if, required_by)
    parameters = {}

    # act
    result = validator.validate(parameters)

    # assert
    assert result

# Generated at 2022-06-12 22:56:40.974010
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

    assert not result.errors, ", ".join(result.error_messages)
    assert result.validated_parameters['age'] == 42
    assert result.validated_parameters['name'] == 'bo'

# Generated at 2022-06-12 22:56:52.382088
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    argument_spec = {
        'test_arg': {'type': 'str', 'default': 'default value'},
        'test_arg2': {'type': 'str', 'default': 'default value'},
    }

    mutually_exclusive = [['test_arg', 'test_arg2']]

    required_together = [['test_arg', 'test_arg2']]

    required_one_of = [['test_arg', 'test_arg2']]

    required_if = [['test_arg', 'test_arg2']]

    required_by = {'test_arg': ['test_arg2']}

    parameters = dict(
        test_arg='set value',
        test_arg2='set value 2',
    )


# Generated at 2022-06-12 22:56:55.225638
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    # Tests that the validation of an ArgumentSpecValidator with an argument spec of a dict throws an error
    args = dict(argument_spec=dict())
    validator = ArgumentSpecValidator(**args)
    assert validator.validate({"name":"bo","age":"42"}).validated_parameters == {"name": "bo", "age": "42"}

# Generated at 2022-06-12 22:57:00.863484
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int', 'required': True},
    }
    parameters = {
        'name': 'bo',
        'age': '42',
    }
    validator = ArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)
    assert result.error_messages == []
    assert result.validated_parameters.get('age') == 42



# Generated at 2022-06-12 22:57:11.661132
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    """
    Test for ArgumentSpecValidator.validate
    """
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
        'dob': {'type': 'str', 'aliases': ['date_of_birth']}
    }
    mutually_exclusive = [
        ['name', 'age']
    ]
    parameters = {
        'name': 'bo',
        'age': '42',
        'dob': '2019-11-22'
    }
    validator = ArgumentSpecValidator(argument_spec, mutually_exclusive=mutually_exclusive)
    result = validator.validate(parameters)
    assert len(result.error_messages) == 0
    assert result.validated_parameters['name'] == 'bo'

# Generated at 2022-06-12 22:57:19.885870
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    arg_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int', 'default': 42}
    }

    parameters = {
        'name': 'bo',
        'age': '42'
    }

    # Tests for simple parameters
    validator = ArgumentSpecValidator(arg_spec)
    result = validator.validate(parameters)

    assert len(result.errors) == 0
    assert result.validated_parameters == {'name': 'bo', 'age': 42}
    assert result.validated_parameters['name'] == 'bo'
    assert result.validated_parameters['age'] == 42

    # Tests for list parameters using nested argument spec

# Generated at 2022-06-12 22:57:30.406356
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    argument_spec = {'name': dict(), 'age': dict()}
    mutually_exclusive = [['name', 'age']]
    required_together = [['name', 'age']]
    required_one_of = [['name', 'age']]
    required_if = [['name', 'age', 'name', 'age']]
    required_by = {'name': 'age', 'age': 'name'}

    parameters = {'name': 'bo', 'age': '42'}

    validator = ArgumentSpecValidator(argument_spec,
                                      mutually_exclusive=mutually_exclusive,
                                      required_together=required_together,
                                      required_one_of=required_one_of,
                                      required_if=required_if,
                                      required_by=required_by)

    result = validator

# Generated at 2022-06-12 22:57:40.122922
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils.common.arg_spec import ModuleArgumentSpecValidator

    input_parameters = {}
    validator = ModuleArgumentSpecValidator({})
    result = validator.validate(input_parameters)
    assert isinstance(result, ValidationResult)
    assert len(result.error_messages) == 0
    assert len(result.unsupported_parameters) == 0
    assert len(result._no_log_values) == 0
    assert len(result._validated_parameters) == 0
    assert len(result._deprecations) == 0
    assert len(result._warnings) == 0

    # Test handling of required arguments

# Generated at 2022-06-12 22:57:52.162413
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    import sys
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }
    mutually_exclusive = []
    required_together = []
    required_one_of = []
    required_if = []
    required_by = []
    parameters = {
        'name': 'bo',
        'age': '42',
    }
    validator = ModuleArgumentSpecValidator(argument_spec,mutually_exclusive,required_together,required_one_of,required_if,required_by)
    try:
        result = validator.validate(parameters)
    except SystemExit as e:
        sys.exit("Validation failed: {0}".format(", ".join(result.error_messages)))

test_ModuleArgumentSpec

# Generated at 2022-06-12 22:57:59.160998
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():

    test_spec = {
        'some_arg': {
            'type': 'bool',
            'default': False,
        },
        'some_other_arg': {
            'type': 'list',
            'elements': 'bool',
            'default': False,
        },
    }

    v = ArgumentSpecValidator(test_spec)

    result = v.validate({'some_other_arg': 'false'})
    assert result.validated_parameters == {'some_arg': False, 'some_other_arg': [False]}

# Generated at 2022-06-12 22:58:07.066547
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    import re
    from ansible.module_utils._text import to_text

    from ansible.module_utils.six.moves import StringIO

    from ansible.module_utils.common.warnings import AnsibleWarning

    # Redirect stdout and stderr
    stdout = sys.stdout
    stderr = sys.stderr
    sys.stdout = TextIO()
    sys.stderr = TextIO()

    # Define the common argument spec

# Generated at 2022-06-12 22:58:18.304549
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    """
    unit test for method validate of class ArgumentSpecValidator
    """

# Generated at 2022-06-12 22:58:23.911018
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # test for method validate of class ModuleArgumentSpecValidator
    # mock object for method validate
    ModuleArgumentSpecValidator_validate_obj = ModuleArgumentSpecValidator()
    test_method_obj = ModuleArgumentSpecValidator_validate_obj.validate(parameters={'name': 'bo', 'age': '42'})
    assert test_method_obj is not None

# Generated at 2022-06-12 22:58:32.483038
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    # Test validate where no arguments are provided
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

    # Test validate where a required argument is missing
    del parameters['age']

    result = validator.validate(parameters)

    assert result.error_messages == ['missing required arguments: (age,)']


# Generated at 2022-06-12 22:58:38.375530
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    """
    Test method validate of class ModuleArgumentSpecValidator
    """
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
        'deprecated_alias': {'type': 'str', 'aliases': ['deprecated_alias_list']},
        'deprecated': {'type': 'str', 'aliases': ['deprecated_list'], 'deprecated': {'version': '2.9', 'date': '1/1/1970'}},
        'deprecated_collection': {'type': 'str', 'aliases': ['deprecated_list_collection'], 'deprecated': {'collection_name': 'test_collection'}},
    }


# Generated at 2022-06-12 22:58:45.664487
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
    assert result.validated_parameters == {'name': 'bo', 'age': 42}


# Generated at 2022-06-12 22:58:53.600573
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    validator = ArgumentSpecValidator({
        'name': {'type': 'str'},
        'age': {'type': 'int'},
        })

    parameters = {
        'name': 'bo',
        'age': '42',
    }

    result = validator.validate(parameters)

    assert result.error_messages == [
        "age: The actual value (42) is of type <type 'int'> and we were unable to convert to the correct type (<type 'str'>)",
    ]

    assert result.validated_parameters == {
        'name': 'bo',
        'age': 42,
    }

# Generated at 2022-06-12 22:59:04.646752
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    argument_spec = {
        'name': {
            'type': 'str',
        }
    }

    mutually_exclusive = [['name', 'age']]
    required_together = [['name', 'age']]
    required_one_of = [['name', 'age']]
    required_if = [['name', 'age', ['age']]]
    required_by = {'name': ['age']}

    validator = ArgumentSpecValidator(argument_spec, mutually_exclusive=mutually_exclusive,
                                      required_together=required_together,
                                      required_one_of=required_one_of,
                                      required_if=required_if,
                                      required_by=required_by,
                                      )

    parameters = {
        'name': 'bo',
    }

    result = validator

# Generated at 2022-06-12 22:59:14.449183
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    validator = ModuleArgumentSpecValidator({'local': {'type': 'bool'}}, mutually_exclusive=[], required_together=[], required_one_of=[], required_if=[], required_by=[])
    assert validator.validate({'local': False})

# Generated at 2022-06-12 22:59:19.846208
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    test_case = [
        {
            "argument_spec": {
                "name": {
                    "type": "str"
                },
                "age": {
                    "type": "int"
                }
            },
            "parameters": {
                "name": "bo",
                "age": "42"
            }
        }
    ]
    for tc in test_case:
        m = ModuleArgumentSpecValidator(tc["argument_spec"])
        result = m.validate(tc["parameters"])
        assert result.validated_parameters["name"] == "bo"
        assert result.validated_parameters["age"] == 42

# Generated at 2022-06-12 22:59:30.851683
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    from ansible.module_utils.common.validation import check_required_arguments

    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
        'bio': {'type': 'dict', 'required': True, 'options': {'city': {'type': 'str'}}},
        'library': {'type': 'list', 'required': True, 'options': {'name': {'type': 'str'}}}
    }

    parameters = {
        'name': 'bo',
        'age': '42',
        'bio': {'city': 'San Francisco'},
        'library': [{'name': 'Baker Street Irregulars'}, {'name': 'Sweeney Todd'}],
    }

    validator = ArgumentSpecValid

# Generated at 2022-06-12 22:59:40.331581
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    # simple parameter test
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
        'gender': {'type': 'str', 'default': 'Male', 'choices': ['Male', 'Female']},
    }

    parameters = {
        'name': 'bo',
        'age': '42',
    }

    validator = ArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    assert result.validated_parameters == {'name': 'bo', 'age': 42, 'gender': 'Male'}, 'simple parameter test failed'
    assert result.error_messages == [], 'simple parameter test failed'

    # simple parameter test

# Generated at 2022-06-12 22:59:48.038697
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    parameters = {
        'name': 'bo',
        'age': '42',
        'remark': 'A bo is always 42'
    }

    argument_spec = {
        'name': {
            'type': 'str',
            'removed': '1.2.3'
        },
        'age': {
            'type': 'int'
        },
        'remark': {
            'type': 'str',
            'aliases': ['description'],
            'deprecated': {
                'date': '2021-12-31',
                'reason': 'Use comment instead',
                'version': '2.3',
            },
            'no_log': True
        },
    }

    validator = ModuleArgumentSpecValidator(argument_spec)

# Generated at 2022-06-12 22:59:57.573993
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # Define the argument_spec 
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
        }
    # Define parameters
    parameters = {
        'name': 'bo',
        'age': '42',
        }
    # Instanciate a ModuleArgumentSpecValidator
    validator = ModuleArgumentSpecValidator(argument_spec)
    # Validate parameters
    result = validator.validate(parameters)
    # Test if it works
    assert result.error_messages == [
        "Could not convert 'age' to an int. Value was: 42",
    ]
    assert result.validated_parameters == {
        'name': 'bo',
        'age': None,
    }

# Generated at 2022-06-12 23:00:02.962718
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
    valid_params = result.validated_parameters
    assert valid_params == {'name': 'bo', 'age': 42}, "valid_params should match"

# Generated at 2022-06-12 23:00:13.879604
# Unit test for method validate of class ArgumentSpecValidator

# Generated at 2022-06-12 23:00:16.574466
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    argument_spec = {}
    validator = ArgumentSpecValidator(argument_spec)
    result = validator.validate({})
    assert result.validated_parameters == {}

# Generated at 2022-06-12 23:00:25.166372
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    param = {'name': 'bo'}

    validator = ModuleArgumentSpecValidator({'name': {'type': 'str'}})
    result = validator.validate(param)

    assert result._deprecations == []
    assert result._warnings == []

    validator = ModuleArgumentSpecValidator({'name': {'type': 'str', 'aliases': ['n']}})
    result = validator.validate(param)

    assert result._deprecations == []
    assert result._warnings == [{'option': 'name', 'alias': 'n'}]


# Generated at 2022-06-12 23:00:44.376315
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    def check_validate_errors(validator, parameters, expected_errors, expected_warnings=None):
        result = validator.validate(parameters)
        assert result.errors.messages == expected_errors, "Got unexpected errors: {0}".format(result.errors)
        if expected_warnings is not None:
            warnings = [w['option'] for w in result._warnings]
            assert warnings == expected_warnings, "Got unexpected warnings: {0}".format(result._warnings)

    argument_spec = {'name': {'type': 'str'},
                     'age': {'type': 'int'},
                     'extra': {'type': 'dict'}}

    parameters = {'name': 'bo',
                  'age': '42',
                  'extra': {'item': 'val'}}

   

# Generated at 2022-06-12 23:00:55.893064
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    argument_spec = {
                    'name': {'type': 'str'},
                    'age': {'type': 'int'},
                    }
    mutually_exclusive = None
    required_together = None
    required_one_of = None
    required_if = None
    required_by = None

    # case1: name=bo age=42
    parameters={'name': 'bo', 'age': '42'}
    validator = ModuleArgumentSpecValidator(argument_spec, mutually_exclusive, required_together, required_one_of, required_if, required_by)
    result = validator.validate(parameters)
    assert result.validated_parameters == {'name': 'bo', 'age': 42}

    # case2: name=bo age is required
    parameters={'name': 'bo'}


# Generated at 2022-06-12 23:01:05.927401
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    """
    Unit test for ArgumentSpecValidator class
    """

    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
        'sex': {'type': 'str', 'choices': ['m', 'f'], 'default': 'm'},
        'children': {'type': 'list', 'default': []},
    }

    parameters = {
        'name': 'bo',
        'age': '42',
        'children': [
            {'name': 'sparkly'},
            {'name': 'terry'}
        ]
    }

    result = ArgumentSpecValidator(argument_spec).validate(parameters)
    valid_params = result.validated_parameters

    assert result.error_messages == []
   

# Generated at 2022-06-12 23:01:16.209657
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    validator = ArgumentSpecValidator({
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    })
    output = validator.validate({
        'name': 'bo',
        'age': '42',
    })

    assert(
        output.error_messages == [
            'The following arguments are required: name, age',
        ]
    )
    assert(
        output.validated_parameters == {
            'name': 'bo',
            'age': 42,
        }
    )

    output = validator.validate({
        'name': 'bo',
    })

    assert(
        output.error_messages == [
            'The following arguments are required: age',
        ]
    )

# Generated at 2022-06-12 23:01:27.167528
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # test for alias deprecations
    argument_spec = {
        'name': {'type': 'str', 'aliases': ['alias_name']},
        'state': {'type': 'str', 'default': 'present', 'aliases': ['state']},
    }

    parameters = {
        'name': 'bo',
        'state': 'absent',
    }

    validator = ModuleArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    assert result.validated_parameters == {'name': 'bo', 'state': 'absent'}
    assert result.error_messages == []
    assert result.deprecations == [{'name': 'alias_name'}]
    assert result.warnings == []

    # test for alias warnings
    argument_spec

# Generated at 2022-06-12 23:01:35.733032
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    class Result:
        def __init__(self):
            self.errors = ''
            self._warnings = ''
            self._deprecations = ''


    class Parent:
        def __init__(self):
            self.check_mode = False


    class AnsibleModule:
        def __init__(self):
            self.parent = Parent()
            self.params = None
            self.result = Result()

        def fail_json(self, msg, **kwargs):
            print('fail_json: {0}'.format(msg))
            print(kwargs)

        def warn(self, msg, **kwargs):
            print('warn: {0}'.format(msg))
            print(kwargs)


# Generated at 2022-06-12 23:01:44.913768
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    """Test: `ModuleArgumentSpecValidator.validate`

    Unit tests for method `validate` of class `ModuleArgumentSpecValidator`
    """
    import sys
    import os
    sys.path.append(os.path.dirname(os.getcwd()))
    from ansible.module_utils.common.arg_spec import ModuleArgumentSpecValidator

    if __name__ == '__main__':
        validator = ModuleArgumentSpecValidator({})
        result = validator.validate({})

        if result.error_messages:
            sys.exit("Validation failed: {0}".format(", ".join(result.error_messages)))

        valid_params = result.validated_parameters
        pass

# Generated at 2022-06-12 23:01:51.158130
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
   }
    mutually_exclusive = [['name', 'age']]
    parameters = {
        'name': 'bo',
        'age': '42',
    }
    validator = ModuleArgumentSpecValidator(argument_spec, mutually_exclusive=mutually_exclusive)
    result = validator.validate(parameters)
    assert result.error_messages
    if result.error_messages:
        assert "name" in result.error_messages[0]
        assert "age" in result.error_messages[0]

# Generated at 2022-06-12 23:01:59.000719
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():

    result = {
        'params': {
            'aliases': ['parameters'],
            'type': 'dict',
        },
    }

    spec = {
        'parameters': {
            'aliases': ['params'],
            'type': 'dict',
        },
        'params': {
            'aliases': ['parameters'],
            'type': 'dict',
        },
    }

    v = ModuleArgumentSpecValidator(spec)
    result = v.validate(result)

    assert len(result.error_messages) == 0
    assert result.validated_parameters['parameters'] == result.validated_parameters['params'] == {}

# Generated at 2022-06-12 23:02:08.414872
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    """Unit Test for class ArgumentSpecValidator"""
    import sys
    from ansible.module_utils.common.text.converters import to_text
    from ansible.module_utils.common.parameters import sanitize_keys

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
        sys.exit("Validation failed: {0}".format(", ".join(map(to_text, result.error_messages))))

    valid_params = result.validated_parameters

# Generated at 2022-06-12 23:02:35.838568
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    """
    This method should validate if the parameters to the method validate of class ArgumentSpecValidator
    is in the valid format
    """
    args_spec = {"name": {"type": "str"}}
    result = ArgumentSpecValidator(args_spec).validate({
    })
    assert result.error_messages == [u"name is required"], "ArgumentSpecValidator fails to validate"\
        " parameters"

    result = ArgumentSpecValidator(args_spec).validate({
        "name": "test"
    })
    assert result.error_messages == [], "ArgumentSpecValidator fails to validate"\
        " parameters"

    args_spec = {"name": {"type": "str"}}
    result = ArgumentSpecValidator(args_spec).validate({
        "name": 1
    })
    assert result

# Generated at 2022-06-12 23:02:46.463485
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    """
    Test method validate of class ModuleArgumentSpecValidator
    """
    # Test ModuleArgumentSpecValidator._warning_messages
    # Test ModuleArgumentSpecValidator._deprecation_messages
    # Test ModuleArgumentSpecValidator._validated_parameters

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
    assert len(result._deprecation_messages) == 0
    assert len(result._warning_messages) == 0

# Generated at 2022-06-12 23:02:52.818473
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    def test_deprecate_callback(msg, version, date, collection_name):
        print("Deprecation: {msg}".format(msg=msg))

    def test_warn_callback(msg):
        print("Warning: {msg}".format(msg=msg))

    deprecation_callbacks = [test_deprecate_callback]
    warning_callbacks = [test_warn_callback]

    argument_spec = {
        'name': {'type': 'str', 'aliases': ['fullname']},
        'age': {'type': 'int'},
        'dict': {'type': 'dict'},
        'list': {'type': 'list'},
        'bool': {'type': 'bool'},
    }


# Generated at 2022-06-12 23:02:58.486192
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    arg = ArgumentSpecValidator({'age': {'type': 'int'}})
    assert arg.validate({'age': '42'}).error_messages == []
    assert arg.validate({'age': '42'}).validated_parameters == {'age': 42}
    assert arg.validate({'age': '42', 'random_key': 'random_value'}).unsupported_parameters == {'random_key'}

# Generated at 2022-06-12 23:03:01.216900
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    parameters = dict()
    assert ModuleArgumentSpecValidator(argument_spec={}).validate(parameters) == ValidationResult(parameters)


# Generated at 2022-06-12 23:03:09.952961
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    argument_spec = {
        'age': {'type': 'int'},
        'name': {'type': 'str'},
    }

    mutually_exclusive = [('name', 'age')]
    required_together = [('name', 'age')]

    required_by = {'name': ['age']}

    validator = ArgumentSpecValidator(argument_spec, mutually_exclusive=mutually_exclusive, required_together=required_together, required_by=required_by)

    result = validator.validate({'name': 'bo'})

    assert ['age is required when name is set'] == result.error_messages
    assert ['age'] == list(result.unsupported_parameters)



# Generated at 2022-06-12 23:03:17.745032
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
        'aliases': {
            'type': 'list',
            'elements': 'str',
        }
    }

    validator = ArgumentSpecValidator(argument_spec)

    parameters = {
        'name': 'bo',
        'age': '42',
        'aliases': ['one', 1]
    }

    result = validator.validate(parameters)

    assert len(result.errors) == 1
    assert result.errors[0].message == 'The value (1) for aliases[1] is of type "str" but "int" was expected.'

# Generated at 2022-06-12 23:03:27.825144
# Unit test for method validate of class ArgumentSpecValidator

# Generated at 2022-06-12 23:03:35.976392
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    from ansible.module_utils.common.arg_spec import ArgumentSpecValidator
    from ansible.module_utils.common.validation import check_mutually_exclusive
    from ansible.module_utils.common.validation import check_required_arguments
    from ansible.module_utils.common.parameters import _set_defaults
    from ansible.module_utils.common.parameters import _validate_argument_types
    from ansible.module_utils.common.parameters import _validate_argument_values
    from ansible.module_utils.common.parameters import _validate_sub_spec
    from ansible.module_utils.common.warnings import deprecate, warn
    from ansible.module_utils.errors import MutuallyExclusiveError, RequiredDefaultError, RequiredError, UnsupportedError

    argument_

# Generated at 2022-06-12 23:03:47.038093
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils.six import PY2

    class FakeResult():
        """This is a stub for ValidationResult class to test module_utils.common.arg_spec.ModuleArgumentSpecValidator"""
        def __init__(self, parameters):
            self._deprecations = []
            self._warnings = []
            self.errors = AnsibleValidationErrorMultiple()
            self.validated_parameters = deepcopy(parameters)

    class FakeModuleArgumentSpecValidator(ModuleArgumentSpecValidator):
        """This is a stub for ModuleArgumentSpecValidator to test module_utils.common.arg_spec.ModuleArgumentSpecValidator"""
        def __init__(self, *args, **kwargs):
            super(FakeModuleArgumentSpecValidator, self).__init__(*args, **kwargs)

# Generated at 2022-06-12 23:04:10.126660
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    validator = ModuleArgumentSpecValidator({'arg1': {'type': 'str', 'required': True, 'aliases': ['arg2']}})

    args = {'arg1': 'value1'}
    result = validator.validate(args)

    assert len(result._warnings) == 0
    assert len(result._deprecations) == 1

    args = {'arg1': 'value1', 'arg2': 'value2'}
    result = validator.validate(args)

    assert len(result._warnings) == 1
    assert len(result._deprecations) == 1

# Generated at 2022-06-12 23:04:13.599612
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    argument_spec = {
        'name': {'type': 'list', 'aliases': ['names']},
        'age': {'type': 'int'},
    }
    parameters = {
        'name': 'bo',
        'age': '42',
    }

    validator = ModuleArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)
    
    assert result.errors == []
    assert result.validated_parameters['name'] == ['bo']

# Generated at 2022-06-12 23:04:19.242276
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    test_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }

    test_params = {
        'name': 'bo',
        'age': '42',
    }

    test_validator = ModuleArgumentSpecValidator(test_spec)
    result = test_validator.validate(test_params)

    assert result.validated_parameters == test_params
    assert result.unsupported_parameters == set()
    assert result.error_messages == []



# Generated at 2022-06-12 23:04:29.132417
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    """Test for method validate of class ModuleArgumentSpecValidator"""

    specs = dict(
        name=dict(type='str'),
        age=dict(type='int'),
        stuff=dict(type='str'),
        nest_me=dict(type='dict', options=dict(
            nest_me_more=dict(type='dict', options=dict(
                foo=dict(type='str')
            )))
        )
    )

    parameters = dict(
        name='bo',
        age='42',
        stuff='none',
        nest_me=dict(
            nest_me_more=dict(
                foo='bar'
            )
        )
    )

    validator = ModuleArgumentSpecValidator(specs)
    result = validator.validate(parameters)

    assert not result.errors

# Generated at 2022-06-12 23:04:31.330228
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    result = ModuleArgumentSpecValidator(None).validate(None)
    assert result is not None
    assert isinstance(result, ValidationResult)

# Generated at 2022-06-12 23:04:40.541102
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    from ansible.module_utils.six import PY3
    from ansible.module_utils.common.collections import ImmutableDict

    with open('tests/units/module_utils/common/arg_spec/ansible_module_argument_spec.json') as f:
        argument_spec = ImmutableDict(eval(f.read()))

    # First module argument spec validation example
    parameters = {
        'name': 'bo',
        'age': '42',
    }

    validator = ArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    if result.error_messages:
        raise Exception('Validation failed: {0}'.format(", ".join(result.error_messages)))

    # Second module argument spec validation example

# Generated at 2022-06-12 23:04:48.878957
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():

    def test_method():

        def run_test(validator, parameters, expected_output, expected_result):
            result = validator.validate(parameters)
            assert result._validated_parameters == expected_output
            assert result._unsupported_parameters == expected_result['unsupported_parameters']
            assert result._no_log_values == expected_result['no_log_values']
            assert result._deprecations == expected_result['deprecations']
            assert result._warnings == expected_result['warnings']
            assert result.error_messages == expected_result['errors']

        # module arguments
        argument_spec = {
            'name': {'type': 'str'},
            'age': {'type': 'int'},
        }


# Generated at 2022-06-12 23:04:56.502281
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    try:
        import importlib
    except:
        importlib = None

    utils_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'test', 'utils')
    if importlib and os.path.exists(utils_path):
        specs = importlib.import_module('test.utils.arg_spec_validator_specs')
    else:
        specs = None


# Generated at 2022-06-12 23:05:05.546271
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils import basic

    argument_spec = basic.AnsibleModule._load_params()

    v = ModuleArgumentSpecValidator(argument_spec)

    result = v.validate({})

    assert (result.error_messages == ['Required value not defined: "msg"'])
    assert (result.validated_parameters == {})
    assert (result.unsupported_parameters == set())
    assert (result.error_messages == ['Required value not defined: "msg"'])
    assert (result.errors.exceptions == [RequiredError('Required value not defined: "msg"')])
    #assert ()



# Generated at 2022-06-12 23:05:12.430328
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

# Generated at 2022-06-12 23:05:58.074855
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    # Basic test
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
        'options': {
            'type': 'dict',
            'options': {
                'verbose': {'type': 'bool', 'default': False}
            }
        }
    }

    parameters = {
        'name': 'bo',
        'age': 42,
    }

    validator = ArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    assert not result.errors
    assert result.validated_parameters == {'name': 'bo', 'age': 42, 'options': {'verbose': False}}

    # Test errors

# Generated at 2022-06-12 23:06:02.017618
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    validator = ModuleArgumentSpecValidator({'key': {'required': True, 'type': 'str'}})
    validator.validate({'key': 'val'})
    validator.validate({'key': 'val', 'other': 'other'})